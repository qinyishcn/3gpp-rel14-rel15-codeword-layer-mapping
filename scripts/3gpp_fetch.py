#!/usr/bin/env python3
"""Download 3GPP files without depending on OpenClaw.

The public 3GPP file tree is available both as HTTPS under
https://www.3gpp.org/ftp/ and as anonymous FTP on ftp.3gpp.org.  This tool
uses HTTPS first for file transfers and falls back to passive FTP.  FTP is
also used for directory listings.

Examples:
  python scripts/3gpp_fetch.py list /tsg_ran/WG1_RL1/TSGR1_125/Docs
  python scripts/3gpp_fetch.py tdoc R1-2604704 --wg RAN1 --meeting 125
  python scripts/3gpp_fetch.py get /Specs/archive/38_series/38.323/38323-j10.zip
"""

from __future__ import annotations

import argparse
import ftplib
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Iterable


FTP_HOST = "ftp.3gpp.org"
FTP_USER = "anonymous"
FTP_PASSWORD = "anonymous@"
HTTPS_ROOT = "https://www.3gpp.org/ftp"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) 3GPP-KB-Downloader/1.0"

WORKSPACE_ROOT = Path(__file__).resolve().parents[1]
CORPUS_ROOT = WORKSPACE_ROOT / "knowledge" / "openclaw-workspace" / "3gpp-standards"

WG_PREFIXES = {
    "RAN": "/tsg_ran/TSG_RAN",
    "RAN1": "/tsg_ran/WG1_RL1",
    "RAN2": "/tsg_ran/WG2_RL2",
    "RAN3": "/tsg_ran/WG3_Iu",
    "RAN4": "/tsg_ran/WG4_Radio",
    "SA2": "/tsg_sa/WG2_Arch",
    "SA4": "/tsg_sa/WG4_CODEC",
}

WG_MEETING_STEMS = {
    "RAN": "TSGR_",
    "RAN1": "TSGR1_",
    "RAN2": "TSGR2_",
    "RAN3": "TSGR3_",
    "RAN4": "TSGR4_",
    "SA2": "TSGS2_",
    "SA4": "TSGS4_",
}


class DownloadError(RuntimeError):
    pass


TRANSFER_ERRORS = (OSError, urllib.error.URLError, DownloadError) + ftplib.all_errors


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def normalize_remote_path(value: str) -> str:
    value = value.strip()
    if value.startswith(("ftp://", "http://", "https://")):
        parsed = urllib.parse.urlparse(value)
        path = urllib.parse.unquote(parsed.path)
        # 3GPP filenames legitimately contain '#'. A pasted, unescaped URL is
        # parsed as a fragment by urllib; reattach it to the remote filename.
        if parsed.fragment:
            path += "#" + urllib.parse.unquote(parsed.fragment)
        if parsed.scheme in {"http", "https"} and path.lower().startswith("/ftp/"):
            path = path[4:]
    else:
        path = value

    path = "/" + path.lstrip("/")
    parts = PurePosixPath(path).parts
    if ".." in parts:
        raise ValueError("Remote path must not contain '..'")
    return path


def https_url(remote_path: str) -> str:
    # '#' is part of several 3GPP filenames and must be percent-encoded; otherwise
    # an HTTP client treats it as a URL fragment and requests the wrong file.
    quoted = urllib.parse.quote(normalize_remote_path(remote_path), safe="/-_.()")
    return HTTPS_ROOT + quoted


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_download(path: Path, expected_size: int | None = None) -> dict:
    size = path.stat().st_size
    if size <= 0:
        raise DownloadError("Downloaded file is empty")
    if expected_size is not None and size != expected_size:
        raise DownloadError(f"Size mismatch: expected {expected_size}, got {size}")

    zip_ok = None
    encrypted_members: list[str] = []
    if path.suffix.lower() == ".zip" or path.name.lower().endswith(".zip.part"):
        try:
            with zipfile.ZipFile(path) as archive:
                # ZipFile.testzip() aborts on password-protected members.  A
                # small number of official TDocs legitimately contain such
                # attachments, so validate every readable member and record
                # encrypted members as not CRC-verifiable instead of treating
                # the whole official archive as corrupt.
                for member in archive.infolist():
                    if member.flag_bits & 0x1:
                        encrypted_members.append(member.filename)
                        continue
                    with archive.open(member) as stream:
                        for _chunk in iter(lambda: stream.read(1024 * 1024), b""):
                            pass
                zip_ok = True if not encrypted_members else None
        except zipfile.BadZipFile as exc:
            raise DownloadError(f"Invalid ZIP file: {exc}") from exc

    result = {"size": size, "sha256": sha256_file(path), "zip_ok": zip_ok}
    if encrypted_members:
        result["zip_encrypted_members"] = encrypted_members
        result["zip_validation_note"] = "All unencrypted members passed CRC; encrypted members require a password."
    return result


def write_receipt(
    output: Path,
    remote_path: str,
    transport: str,
    validation: dict,
) -> Path:
    receipt = output.with_name(output.name + ".download.json")
    temporary = receipt.with_name(receipt.name + ".tmp")
    payload = {
        "schema_version": 1,
        "downloaded_at": utc_now(),
        "remote_path": remote_path,
        "ftp_url": f"ftp://{FTP_HOST}{remote_path}",
        "https_url": https_url(remote_path),
        "transport": transport,
        **validation,
    }
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, receipt)
    return receipt


def download_https(remote_path: str, temporary: Path, timeout: int) -> int | None:
    request = urllib.request.Request(
        https_url(remote_path),
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/octet-stream,*/*;q=0.8",
        },
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        length_header = response.headers.get("Content-Length")
        expected_size = int(length_header) if length_header and length_header.isdigit() else None
        with temporary.open("wb") as handle:
            shutil.copyfileobj(response, handle, length=1024 * 1024)
    return expected_size


def download_ftp(remote_path: str, temporary: Path, timeout: int) -> int | None:
    with ftplib.FTP(FTP_HOST, timeout=timeout) as ftp:
        ftp.login(FTP_USER, FTP_PASSWORD)
        ftp.set_pasv(True)
        ftp.voidcmd("TYPE I")
        try:
            expected_size = ftp.size(remote_path)
        except ftplib.all_errors:
            expected_size = None
        with temporary.open("wb") as handle:
            ftp.retrbinary(f"RETR {remote_path}", handle.write, blocksize=256 * 1024)
    return expected_size


def download_file(
    remote_path: str,
    output: Path,
    transport: str = "auto",
    retries: int = 3,
    timeout: int = 60,
    force: bool = False,
) -> dict:
    remote_path = normalize_remote_path(remote_path)
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    if output.exists() and not force:
        validation = validate_download(output)
        return {
            "status": "exists",
            "output": str(output),
            "receipt": None,
            **validation,
        }

    temporary = output.with_name(output.name + ".part")
    transports = [transport] if transport != "auto" else ["https", "ftp"]
    errors: list[str] = []

    for selected in transports:
        for attempt in range(1, retries + 1):
            try:
                if temporary.exists():
                    temporary.unlink()
                if selected == "https":
                    expected_size = download_https(remote_path, temporary, timeout)
                elif selected == "ftp":
                    expected_size = download_ftp(remote_path, temporary, timeout)
                else:
                    raise ValueError(f"Unsupported transport: {selected}")

                validation = validate_download(temporary, expected_size)
                os.replace(temporary, output)
                receipt = write_receipt(output, remote_path, selected, validation)
                return {
                    "status": "downloaded",
                    "transport": selected,
                    "output": str(output),
                    "receipt": str(receipt),
                    **validation,
                }
            except TRANSFER_ERRORS as exc:
                errors.append(f"{selected} attempt {attempt}: {exc}")
                if temporary.exists():
                    temporary.unlink()
                if attempt < retries:
                    time.sleep(min(2 ** (attempt - 1), 4))

    raise DownloadError("All download attempts failed:\n  " + "\n  ".join(errors))


def ftp_list(remote_dir: str, timeout: int = 60) -> list[dict]:
    remote_dir = normalize_remote_path(remote_dir)
    with ftplib.FTP(FTP_HOST, timeout=timeout) as ftp:
        ftp.login(FTP_USER, FTP_PASSWORD)
        ftp.set_pasv(True)
        try:
            entries = []
            for name, facts in ftp.mlsd(remote_dir):
                entries.append(
                    {
                        "name": name,
                        "type": facts.get("type", "unknown"),
                        "size": int(facts["size"]) if facts.get("size", "").isdigit() else None,
                        "modify": facts.get("modify"),
                    }
                )
            return sorted(entries, key=lambda item: item["name"].lower())
        except ftplib.all_errors:
            names = ftp.nlst(remote_dir)
            return [
                {"name": PurePosixPath(name).name, "type": "unknown", "size": None, "modify": None}
                for name in sorted(names, key=str.lower)
            ]


def filter_entries(entries: Iterable[dict], pattern: str | None) -> list[dict]:
    if not pattern:
        return list(entries)
    regex = re.compile(pattern, re.IGNORECASE)
    return [entry for entry in entries if regex.search(entry["name"])]


def default_get_output(remote_path: str) -> Path:
    return Path.cwd() / PurePosixPath(remote_path).name


def build_tdoc_paths(args: argparse.Namespace) -> tuple[str, Path]:
    tdoc_id = args.tdoc_id.upper().removesuffix(".ZIP")
    if not re.fullmatch(r"(?:[RSC][1-6]|[RSC]P)-\d{6,7}", tdoc_id):
        raise ValueError(f"Invalid TDoc number: {args.tdoc_id}")

    wg = args.wg.upper()
    if args.remote_dir:
        remote_dir = normalize_remote_path(args.remote_dir)
    else:
        if wg not in WG_PREFIXES:
            raise ValueError(f"Unsupported WG {wg}; use --remote-dir for an unlisted group")
        meeting_dir = args.meeting_dir or f"{WG_MEETING_STEMS[wg]}{args.meeting}"
        remote_dir = f"{WG_PREFIXES[wg]}/{meeting_dir}/Docs"

    remote_path = f"{remote_dir.rstrip('/')}/{tdoc_id}.zip"
    local_meeting = args.local_meeting or f"{wg}_{args.meeting}"
    output = Path(args.output) if args.output else CORPUS_ROOT / "tdocs" / local_meeting / f"{tdoc_id}.zip"
    return remote_path, output


def sync_directory(args: argparse.Namespace) -> dict:
    remote_dir = normalize_remote_path(args.remote_dir).rstrip("/")
    destination = Path(args.dest_dir).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    entries = filter_entries(ftp_list(remote_dir, args.timeout), args.pattern)
    entries = [entry for entry in entries if entry["type"] != "dir"]
    priority = getattr(args, "priority_pattern", None)
    if priority:
        preferred = re.compile(priority, re.IGNORECASE)
        entries.sort(key=lambda entry: not bool(preferred.search(entry["name"])))
    if args.limit is not None:
        entries = entries[: max(0, args.limit)]

    results: list[dict] = []
    failures: list[dict] = []

    def transfer(entry: dict) -> dict:
        name = entry["name"]
        result = download_file(
            f"{remote_dir}/{name}",
            destination / name,
            transport=args.transport,
            retries=max(1, args.retries),
            timeout=max(5, args.timeout),
            force=args.force,
        )
        result["name"] = name
        return result

    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 8))) as executor:
        future_to_entry = {executor.submit(transfer, entry): entry for entry in entries}
        for future in as_completed(future_to_entry):
            entry = future_to_entry[future]
            try:
                results.append(future.result())
            except TRANSFER_ERRORS as exc:
                failures.append({"name": entry["name"], "error": str(exc)})

    results.sort(key=lambda item: item["name"].lower())
    failures.sort(key=lambda item: item["name"].lower())
    summary = {
        "schema_version": 1,
        "run_at": utc_now(),
        "remote_dir": remote_dir,
        "destination": str(destination),
        "matched": len(entries),
        "downloaded": sum(item["status"] == "downloaded" for item in results),
        "existing": sum(item["status"] == "exists" for item in results),
        "failed": len(failures),
        "files": results,
        "failures": failures,
    }
    manifest = destination / ".3gpp-sync-manifest.json"
    temporary = manifest.with_name(manifest.name + ".tmp")
    temporary.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, manifest)
    summary["manifest"] = str(manifest)
    return summary


def add_transfer_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--transport", choices=["auto", "https", "ftp"], default="auto")
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--force", action="store_true", help="Replace an existing file")


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Independent 3GPP HTTPS/FTP downloader")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List a 3GPP FTP directory")
    list_parser.add_argument("remote_dir")
    list_parser.add_argument("--pattern", help="Case-insensitive regular expression")
    list_parser.add_argument("--json", action="store_true")
    list_parser.add_argument("--timeout", type=int, default=60)

    get_parser = subparsers.add_parser("get", help="Download an arbitrary 3GPP file")
    get_parser.add_argument("remote_path")
    get_parser.add_argument("--output", "-o")
    add_transfer_options(get_parser)

    tdoc_parser = subparsers.add_parser("tdoc", help="Download one meeting contribution")
    tdoc_parser.add_argument("tdoc_id")
    tdoc_parser.add_argument("--wg", required=True, help="For example RAN1 or RAN2")
    tdoc_parser.add_argument("--meeting", required=True, help="For example 125 or 133bis")
    tdoc_parser.add_argument("--meeting-dir", help="Exact FTP meeting directory name")
    tdoc_parser.add_argument("--remote-dir", help="Exact remote Docs directory; overrides WG mapping")
    tdoc_parser.add_argument("--local-meeting", help="Local folder name, for example RAN1_125")
    tdoc_parser.add_argument("--output", "-o")
    add_transfer_options(tdoc_parser)

    sync_parser = subparsers.add_parser("sync", help="Incrementally download files from one directory")
    sync_parser.add_argument("remote_dir")
    sync_parser.add_argument("dest_dir")
    sync_parser.add_argument(
        "--pattern",
        default=r"(?:\.zip$|TDoc_List.*\.(?:xlsx|xls)$)",
        help="Case-insensitive regular expression used to select filenames",
    )
    sync_parser.add_argument("--limit", type=int, help="Limit transfers; useful for a probe")
    sync_parser.add_argument("--workers", type=int, default=4)
    add_transfer_options(sync_parser)
    return parser


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    try:
        if args.command == "list":
            entries = filter_entries(ftp_list(args.remote_dir, args.timeout), args.pattern)
            if args.json:
                print(json.dumps(entries, ensure_ascii=False, indent=2))
            else:
                for entry in entries:
                    size = "-" if entry["size"] is None else str(entry["size"])
                    print(f"{entry['type']:<8} {size:>12}  {entry['name']}")
                print(f"Total: {len(entries)}")
            return 0

        if args.command == "sync":
            summary = sync_directory(args)
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return 1 if summary["failed"] else 0

        if args.command == "get":
            remote_path = normalize_remote_path(args.remote_path)
            output = Path(args.output) if args.output else default_get_output(remote_path)
        else:
            remote_path, output = build_tdoc_paths(args)

        result = download_file(
            remote_path,
            output,
            transport=args.transport,
            retries=max(1, args.retries),
            timeout=max(5, args.timeout),
            force=args.force,
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError,) + TRANSFER_ERRORS as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

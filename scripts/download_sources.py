"""Re-download the validated source set, using HTTPS then anonymous passive FTP."""
from pathlib import Path
import json,importlib.util,urllib.parse,concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fetch',Path(__file__).with_name('3gpp_fetch.py'))
fetch=importlib.util.module_from_spec(spec);spec.loader.exec_module(fetch)
rows=json.loads((ROOT/'data/source-manifest.json').read_text(encoding='utf-8'))
def one(row):
    remote=urllib.parse.unquote(urllib.parse.urlparse(row['official_url']).path)
    if remote.lower().startswith('/ftp/'):remote=remote[4:]
    r=fetch.download_file(remote,ROOT/row['path'],retries=2,timeout=45)
    assert r['sha256']==row['sha256'],('Official source changed; retain old copy and inspect',row['path'])
    print(r['status'],row['path'],flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(one,rows))

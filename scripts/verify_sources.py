"""Verify raw archives, provenance, quoted evidence and table row counts locally."""
from pathlib import Path
import json,hashlib,zipfile,csv,re
ROOT=Path(__file__).resolve().parents[1]
load=lambda n:json.loads((ROOT/'data'/n).read_text(encoding='utf-8'))
manifest=load('source-manifest.json'); ev=load('evidence.json');out=load('outcomes.json'); stats=load('coverage-stats.json')
for x in manifest:
    p=ROOT/x['path']; assert p.is_file(),p
    assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'],p
    assert p.stat().st_size==x['size'],p
    with zipfile.ZipFile(p) as z:assert z.testzip() is None,p
for x in ev+out:
    p=ROOT/x['source_path'];t=p.read_text(encoding='utf-8');assert x['quote'] in t,(x.get('id'),p)
    line=x.get('quote_line',x.get('source_line'));assert line==t[:t.index(x['quote'])].count('\n')+1
for name,count in [('simulation-evidence.csv',len(ev)),('meeting-outcomes.csv',len(out)),('source-catalog.csv',stats['title_candidates']),('meeting-coverage.csv',stats['meetings'])]:
    with (ROOT/'data'/name).open(encoding='utf-8-sig',newline='') as f:assert len(list(csv.DictReader(f)))==count,name
assert len({e['tdoc'] for e in ev})==stats['simulation_documents_including_revisions']
assert len({e['company_group'] for e in ev})==stats['company_groups']
assert len(load('meeting-coverage.json'))==27
assert len(manifest)==stats['validated_source_archives']
print(json.dumps({'result':'passed','raw_archives':len(manifest),'quote_records':len(ev)+len(out),'evidence_rows':len(ev),'simulation_documents_including_revisions':len({r['tdoc'] for r in ev}),'gaps':len(stats['gaps'])},indent=2))

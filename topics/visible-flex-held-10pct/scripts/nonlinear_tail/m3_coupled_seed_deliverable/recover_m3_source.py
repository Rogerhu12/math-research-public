#!/usr/bin/env python3
"""Restore immutable, hash-checked original m3 source to a new scratch folder."""
from pathlib import Path
import argparse,hashlib,json,subprocess
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--repo',type=Path,required=True);p.add_argument('--dest',type=Path,required=True)
p.add_argument('--manifest',type=Path,default=Path(__file__).with_name('m3_source_recovery_manifest.json'))
a=p.parse_args();repo=a.repo.resolve();dest=a.dest.resolve()
if dest==repo or repo in dest.parents:raise ValueError('Restored source and generated data must stay outside the repository')
dest.mkdir(parents=True,exist_ok=False);m=json.loads(a.manifest.read_text())
for r in m['files']:
 data=subprocess.check_output(['git','-C',str(repo),'show',r['revision']+':'+r['path']])
 if len(data)!=r['bytes']or hashlib.sha256(data).hexdigest()!=r['sha256']:raise RuntimeError('Immutable source hash mismatch: '+r['path'])
 target=dest/r['target'];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
print(json.dumps(dict(source_topic=str(dest/'bundle/topics/visible-flexible-closed-surface'),short_bridge=str(dest/'bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py'),files=len(m['files']),source_manifest_sha256=hashlib.sha256(a.manifest.read_bytes()).hexdigest())))

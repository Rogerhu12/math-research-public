#!/usr/bin/env python3
"""Recover and checksum immutable sources from a partial Git checkout."""
import argparse,hashlib,json,subprocess
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
a=p.parse_args();manifest=Path(__file__).with_name('sources_manifest.json')
for row in json.loads(manifest.read_text())['files']:
 target=a.output/row['target']
 data=target.read_bytes()if target.exists()else subprocess.check_output(['git','-C',str(a.repo),'show',row['revision']+':'+row['path']])
 if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256']:raise RuntimeError('Immutable source checksum mismatch: '+str(target))
 if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
print(json.dumps({'recovered':len(json.loads(manifest.read_text())['files']),'root':str(a.output.resolve())}))

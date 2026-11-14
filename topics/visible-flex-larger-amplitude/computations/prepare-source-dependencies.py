#!/usr/bin/env python3
"""Materialize the recorded small source subset from Git, never a whole topic.

Authentication, if Git needs it for a promised blob, belongs in the caller's
ephemeral terminal environment. This script stores no credentials. The output
contains only the committed files in source-dependencies.json at its revision.
"""
import argparse,hashlib,json,subprocess
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[3])
    p.add_argument('--dest',type=Path,required=True)
    p.add_argument('--manifest',type=Path,default=Path(__file__).with_name('source-dependencies.json'))
    a=p.parse_args();rec=json.loads(a.manifest.read_text());dest=a.dest.resolve()
    for entry in rec['files']:
        path=Path(entry['path'])
        if path.is_absolute() or '..' in path.parts:raise ValueError('Invalid relative source path')
        target=dest/path
        if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest()==entry['sha256']:continue
        data=subprocess.check_output(['git','-C',str(a.repo),'show',rec['source_revision']+':'+entry['path']])
        if hashlib.sha256(data).hexdigest()!=entry['sha256']:raise ValueError('Source hash mismatch: '+entry['path'])
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    origin=dict(source_revision=rec['source_revision'],files=len(rec['files']),bytes=rec['total_bytes'],
        manifest_sha256=hashlib.sha256(a.manifest.read_bytes()).hexdigest())
    topic=dest/'topics/visible-flexible-closed-surface'
    (topic/'source-origin.json').write_text(json.dumps(origin,indent=2)+'\n')
    print(json.dumps(dict(source_topic=str(topic),**origin)))

if __name__=='__main__':main()

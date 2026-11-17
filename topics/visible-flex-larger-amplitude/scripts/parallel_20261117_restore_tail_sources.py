#!/usr/bin/env python3
"""Recover only the 13 verified scalar-background source files outside git."""
import argparse,hashlib,json,subprocess
from pathlib import Path


def main(a):
    repo=a.repo.resolve();out=a.out.resolve()
    if out.is_relative_to(repo):raise ValueError('Recovered source must stay outside the research checkout')
    revision=subprocess.check_output(['git','-C',str(repo),'rev-parse',a.revision]).decode().strip()
    base='topics/visible-flexible-closed-surface/'
    def read(p):return subprocess.check_output(['git','-C',str(repo),'show',revision+':'+base+p])
    paths=['scripts/closing_weighted_tail.mjs','scripts/closing_recalibrated_tail.mjs','scripts/closing_tail_sources.mjs','notes/closing_tail_dependency_blobs.json']
    manifest=json.loads(read(paths[-1]));paths += ['repro/source-root/topics/large-amplitude-twist-flex/scripts/'+name for name in manifest]
    records=[]
    for p in paths:
        raw=read(p);target=out/p;blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if target.name in manifest and manifest[target.name]!=blob:raise ValueError('Git blob verification failed: '+p)
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
        records.append(dict(path=base+p,bytes=len(raw),git_blob=blob,sha256=hashlib.sha256(raw).hexdigest()))
    report=dict(repository='Rogerhu12/math-research-public',revision=revision,files=records)
    (out/'recovery.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(root=str(out),revision=revision,files=len(records),bytes=sum(r['bytes'] for r in records))))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=Path('.'));p.add_argument('--out',type=Path,required=True)
    p.add_argument('--revision',default='HEAD');main(p.parse_args())

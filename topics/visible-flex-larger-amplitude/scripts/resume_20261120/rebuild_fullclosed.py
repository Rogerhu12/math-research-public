#!/usr/bin/env python3
"""Restore the documented fullclosed initial-guess chain after scratch loss.

Only the genuine historical accepted .99 blob is restored. Later fields are
new reproductions with new identities, never relabelled as the lost raw files.
No old continuous certificate or failed nonlinear budget is rerun.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

OLD_COMMIT = '60321451c058c6a51da58c37ae5ec6f2d1145f74'
OLD_PATH = 'topics/visible-flex-larger-amplitude/notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz'
OLD_SHA = 'b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff'

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--work', type=Path, required=True)
    a=p.parse_args()
    a.repo=a.repo.resolve();a.work=a.work.resolve()
    data=a.work/'data';logs=a.work/'logs'
    data.mkdir(parents=True, exist_ok=True);logs.mkdir(exist_ok=True)
    source=a.repo/'topics/visible-flex-larger-amplitude/scripts/parallel_20261117_continue.py'
    manifest=a.work/'rebuild-prefix-manifest.json'
    if manifest.exists():
        report=json.loads(manifest.read_text())
        if report['continue_source_sha256']!=sha(source):
            raise RuntimeError('Source changed since this recovery started')
    else:
        report=dict(schema='fullclosed-prefix-recovery-20261120-v1',
            historical_blob=dict(commit=OLD_COMMIT,path=OLD_PATH,sha256=OLD_SHA),
            continue_source_sha256=sha(source),driver_sha256=sha(__file__),
            outputs_are_new_reproductions=True,old_continuous_certificates_reused=False,
            stages=[])
    def save():manifest.write_text(json.dumps(report,indent=2)+'\n')
    initial=data/'accepted099.json.gz'
    if not initial.exists():
        with initial.open('wb') as f:
            subprocess.run(['git','show',OLD_COMMIT+':'+OLD_PATH],cwd=a.repo,stdout=f,check=True)
    if sha(initial)!=OLD_SHA:raise RuntimeError('Historical accepted blob identity mismatch')
    commands=[
        ('continue0991','accepted099', ['--duration','.001']),
        ('continue0992','continue0991', ['--duration','.001']),
        ('refine0992m112','continue0992', ['--boundary-input',str(data/'continue0991.json.gz'),'--duration','0','--tol','1e-8','--max-nodes','1400','--modes','112','--angles','2048']),
        ('continue0993m112','refine0992m112', ['--duration','.001','--step','.0002','--fixed-modes','3','--modes','112','--angles','2048','--tol','1e-8','--max-nodes','1600']),
        ('continue0995m112','continue0993m112', ['--duration','.002','--step','.00025','--fixed-modes','3','--modes','112','--angles','2048','--tol','1e-8','--max-nodes','1800']),
    ]
    env=os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    for name,parent,extra in commands:
        inp=data/(parent+'.json.gz');out=data/(name+'.json.gz');log=logs/(name+'.log')
        cmd=[sys.executable,'-u',str(source),'--input',str(inp),*extra,'--out',str(out)]
        old=next((x for x in report['stages'] if x['name']==name),None)
        if old and old.get('success') and out.exists() and sha(out)==old['output_sha256']:
            print(json.dumps(dict(event='reuse_completed_recovery_stage',name=name)),flush=True)
            continue
        if out.exists():raise RuntimeError('An incomplete old output must be inspected before retrying: '+str(out))
        record=dict(name=name,command=cmd,input_sha256=sha(inp),started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),log=str(log))
        report['stages'].append(record);save()
        print(json.dumps(dict(event='start_recovery_stage',name=name)),flush=True)
        clock=time.monotonic()
        with log.open('w') as f:
            r=subprocess.run(cmd,cwd=a.repo,env=env,stdout=f,stderr=subprocess.STDOUT)
        record.update(returncode=r.returncode,seconds=time.monotonic()-clock)
        if out.exists():
            d=json.loads(gzip.decompress(out.read_bytes()))
            record.update(output_sha256=sha(out),success=bool(d.get('success')),
                nodes=len(d['mesh']),M=d['M'],N=d['N'],endpoint=d['mesh'][-1],
                collocation_rms_max=d['collocation_rms_max'],
                boundary_residual_max=d['boundary_residual_max'])
        save();print(json.dumps(dict(event='finish_recovery_stage',**record)),flush=True)
        if r.returncode or not record.get('success'):raise RuntimeError('Recovery stage did not produce an accepted prefix: '+name)
    report['complete']=True;report['final_prefix']=str(data/'continue0995m112.json.gz');save()
    print(json.dumps(dict(event='prefix_recovery_complete',manifest=str(manifest),prefix=report['final_prefix'])),flush=True)

if __name__=='__main__':main()

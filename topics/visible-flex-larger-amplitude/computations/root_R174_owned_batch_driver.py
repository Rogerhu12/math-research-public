#!/usr/bin/env python3
"""Run/recover exact R174 batches; reuse only complete matching owned exit0.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This changes ownership granularity only, never mathematical tolerances.
"""
import argparse
import datetime
import fcntl
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    p=Path(p);raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def atomic(p,data):
    q=Path(str(p)+'.next');q.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');q.replace(p)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--plan',type=Path,required=True);ap.add_argument('--out-dir',type=Path,required=True)
    a=ap.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);lock=(a.out_dir/'driver.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    plan=load(a.plan);started=time.monotonic();plan_sha=sha(a.plan)
    for name in ('worker','wrapper'):assert sha(plan[name])==plan[name+'_sha256']
    assert sha(plan['input_manifest'])==plan['input_manifest_sha256']
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    complete={};todo=[];active={};failure=[]
    def validate(batch,resource_path):
        r=load(resource_path)
        if r['exitcode']!=0 or r.get('termination_signal') is not None:return None
        command=r['command'];prefix=Path(command[command.index('--out-prefix')+1]);primary=Path(str(prefix)+'-certificate.json.gz')
        q=load(primary)
        assert q['all_gates'] and q['batch_range']==[batch['start_row'],batch['end_row']]
        assert q['source_sha256']==plan['worker_sha256'] and q['input_manifest_sha256']==plan['input_manifest_sha256']
        assert q['finite_inverse_order']==plan['inverse_order'] and q['precision_bits']==256
        assert q['refined_leaves']==batch['end_row']-batch['start_row']
        for row in q['profile_chunks']:assert sha(row['path'])==row['sha256']
        return dict(id=batch['id'],batch_range=q['batch_range'],primary=str(primary),primary_sha256=sha(primary),resource=str(resource_path),resource_sha256=sha(resource_path),owned_exitcode=0)
    for batch in plan['batches']:
        candidates=sorted(a.out_dir.glob(f"batch{batch['id']:03d}-attempt*-resource.json"))
        bad=[]
        for p in candidates:
            r=validate(batch,p)
            if r is not None:complete[batch['id']]=r;break
            bad.append(str(p))
        if batch['id'] not in complete:
            if bad:raise ArithmeticError('A completed failed batch requires diagnosis, not an identical blind retry: '+','.join(bad))
            todo.append(batch)
    def progress():
        atomic(a.out_dir/'progress.json',dict(schema='actual-owned-R174-batch-progress-v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),plan_sha256=plan_sha,
            completed=[complete[i] for i in sorted(complete)],active=[v['launch'] for v in active.values()],remaining=[x['id'] for x in todo],failures=failure))
    progress();print(json.dumps(dict(event='resume_exact_complete_batches',completed=len(complete),remaining=len(todo),plan_sha256=plan_sha)),flush=True)
    while todo or active:
        while todo and len(active)<plan['max_parallel'] and not failure:
            batch=todo.pop(0);bid=batch['id'];previous=list(a.out_dir.glob(f'batch{bid:03d}-attempt*'))
            numbers=[int(re.search(r'attempt(\d+)',p.name).group(1)) for p in previous]
            attempt=max(numbers,default=0)+1;prefix=a.out_dir/f'batch{bid:03d}-attempt{attempt:02d}'
            resource_path=Path(str(prefix)+'-resource.json');log=Path(str(prefix)+'-stdout.log')
            # Output stem is deliberately distinct from launch/log/resource.
            result_prefix=Path(str(prefix)+'-result')
            command=['python',plan['worker'],'--inputs',plan['input_manifest'],'--out-prefix',str(result_prefix),'--inverse-order',str(plan['inverse_order']),
                     '--rss-kib',str(plan['rss_kib']),'--start-row',str(batch['start_row']),'--end-row',str(batch['end_row'])]
            argv=['python',plan['wrapper'],'--out',str(resource_path),'--',*command]
            launch=dict(batch=batch,attempt=attempt,command=command,wrapper_command=argv,worker_sha256=plan['worker_sha256'],input_manifest_sha256=plan['input_manifest_sha256'],
                        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),cpu_threads=1,planned_peak_rss_kib=plan['rss_kib'],resource=str(resource_path),log=str(log))
            lp=Path(str(prefix)+'-launch.json');lp.write_text(json.dumps(launch,indent=2)+'\n')
            f=log.open('x');p=subprocess.Popen(argv,stdout=f,stderr=subprocess.STDOUT,env=env)
            active[bid]=dict(process=p,file=f,batch=batch,resource=resource_path,launch=str(lp),log=log)
            print(json.dumps(dict(event='actual_owned_batch_started',batch=bid,attempt=attempt,rows=command[-3::2])),flush=True);progress()
        ended=[]
        for bid,v in active.items():
            code=v['process'].poll()
            if code is None:continue
            v['file'].close();ended.append(bid)
            if code==0:
                record=validate(v['batch'],v['resource']);assert record is not None;complete[bid]=record
                print(json.dumps(dict(event='actual_owned_batch_completed',batch=bid,completed=len(complete),primary_sha256=record['primary_sha256'])),flush=True)
            else:
                failure.append(dict(batch=bid,wrapper_returncode=code,resource=str(v['resource']),log=str(v['log'])))
                print(json.dumps(dict(event='actual_batch_failed',**failure[-1])),flush=True)
        for bid in ended:del active[bid]
        if ended:progress()
        if failure and not active:break
        time.sleep(.2)
    if failure:raise SystemExit(1)
    assert len(complete)==len(plan['batches'])
    final=dict(schema='all_R174_original_leaves_in_complete_owned_batches-v1',all_required_batches_owned_zero=True,plan=str(a.plan),plan_sha256=plan_sha,
               worker_sha256=plan['worker_sha256'],input_manifest_sha256=plan['input_manifest_sha256'],whole_refined_leaves=3976,
               batches=[complete[i] for i in sorted(complete)],elapsed_seconds=time.monotonic()-started)
    atomic(a.out_dir/'complete.json',final);print(json.dumps(dict(event='all_actual_owned_batches_complete',batches=len(complete),path=str(a.out_dir/'complete.json'))),flush=True)

if __name__=='__main__':main()

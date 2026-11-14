#!/usr/bin/env python3
"""Consume complete same-H RK48 nodes with the explicit target-metric rr rule.

Runs the full f8/f16 six-jet comparison and the complete closed-map branch in
parallel, at most two single-threaded consumers. No node integration, tail
Newton, source geometry, complete H, phase range or cut width is changed.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import threading
import time


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repo-root','source-topic','config','readout-dir','out'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();repo=a.repo_root.resolve();comp=repo/'topics/visible-flex-larger-amplitude/computations';notes=comp.parent/'notes'
    out=a.out.resolve();out.mkdir(parents=True,exist_ok=False);raw=a.readout_dir.resolve()
    sources=['target_metric_finish.py','target_metric_common_grid.py','target_metric_closed_assembly.py',
             'target_metric_collar.py','source_knot_rr_probe.py','regional_common_grid.py','common_grid_refinement.py',
             'refined_tail_adapter.py','resolved_closed_assembly.py','refined_closed_assembly.py','closed_display_adapter.py',
             'finite_collar_bound.py','closed_background.mjs','closed_mesh_summary.py']
    hashes={str(comp/('exact_20261114_'+name)):hashlib.sha256((comp/('exact_20261114_'+name)).read_bytes()).hexdigest()for name in sources}
    def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
    def write(path,data):
        with path.open('x')as f:json.dump(data,f,indent=2,allow_nan=False);f.write('\n')
    write(out/'intent.json',dict(argv=sys.argv,started_utc=utc(),source_sha256_at_start=hashes,
                               complete_readout=raw.as_posix(),cut_width=.01,scope=__doc__))
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    commands=[];lock=threading.Lock();start=time.monotonic()
    def event(data):
        with lock:
            with(out/'lifecycle.jsonl').open('a')as f:f.write(json.dumps(data)+'\n')
            print(json.dumps(data),flush=True)
    def run(label,argv):
        row=dict(label=label,command=list(map(str,argv)),started_utc=utc());begin=time.monotonic();event(dict(event='start',**row))
        with(out/(label+'.log')).open('wb')as log:code=subprocess.run(row['command'],cwd=repo,env=env,stdout=log,stderr=subprocess.STDOUT).returncode
        row.update(actual_exit_code=code,finished_utc=utc(),seconds=time.monotonic()-begin)
        with lock:commands.append(row)
        event(dict(event='exit',**row))
        if code:raise RuntimeError(label+' exited '+str(code))
    checkpoint=notes/'2026-11-13-strong-q126-m32-tail2-actual-r1.json.gz';port=comp/'alternative-neck-provider-smallcut30-port32-r2048.json'
    complete=raw/'cusp48-sixteen/complete.json';eight=raw/'cusp48-eight/complete.json'
    shared=['--source-topic',a.source_topic,'--checkpoint',checkpoint,'--port',port]
    def common():
        run('target-common-eight-to-sixteen',[sys.executable,'-u',comp/'exact_20261114_target_metric_common_grid.py',
            '--complete',eight,'--complete',complete,'--labels','rk48-f8-cusp-GW,rk48-f16-cusp-GW',
            '--background',raw/'cusp48-sixteen/background-16.json','--out',out/'common-eight-to-sixteen.json',
            '--angles','1024','--cut-width','.01']+shared)
    def closed():
        run('target-finite-collar',[sys.executable,'-u',comp/'exact_20261114_target_metric_collar.py','--complete',complete,'--out',out/'finite-collar.json'])
        dest=out/'closed';dest.mkdir();prefix=dest/'refined-A-closed';plan=Path(str(prefix)+'-plan.json');background=dest/'background.json'
        entry=[sys.executable,'-u',comp/'exact_20261114_target_metric_closed_assembly.py'];args=shared+['--config',a.config,'--complete',complete,'--out-prefix',prefix]
        run('target-closed-plan',entry+['plan']+args+['--angular','96','--phase-samples','9','--cut-correction-width','.01'])
        run('target-closed-source-background',['node','--expose-gc','--max-old-space-size=384','--max-semi-space-size=4',comp/'exact_20261114_closed_background.mjs',
            '--repo-root',repo,'--source-topic',a.source_topic,'--config',a.config,'--plan',plan,'--out',background])
        run('target-closed-render',entry+['render']+args+['--plan',plan,'--heights',background])
        run('target-closed-summary',[sys.executable,'-u',comp/'exact_20261114_closed_mesh_summary.py','--directory',dest,'--out',dest/'summary.json'])
    success=False;failure=None
    try:
        with ThreadPoolExecutor(max_workers=2)as pool:
            jobs=[pool.submit(common),pool.submit(closed)]
            for job in jobs:job.result()
        success=True
    except Exception as error:failure=str(error)
    terminal=dict(finished=True,success=success,failure=failure,finished_utc=utc(),seconds=time.monotonic()-start,
                  source_sha256_at_start=hashes,commands=commands,task_completed=False)
    write(out/'terminal.json',terminal);event(dict(event='terminal',success=success,failure=failure))
    return 0 if success else 1


if __name__=='__main__':raise SystemExit(main())

#!/usr/bin/env python3
"""Solve an explicitly new first-valley physical metric with the original DN.

Only the first valley control changes. The prefix delta is solved afresh;
previous accepted coordinates serve only as initial guesses.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    p = argparse.ArgumentParser()
    for key in ['source-topic','short-bridge','sparse-helper','chart','prefix-restart','tail-restart','restart-port','outdir']:
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--beta0', type=float, required=True)
    p.add_argument('--amplitude', type=float, required=True)
    p.add_argument('--nodes', type=int, default=801)
    p.add_argument('--max-nodes', type=int, default=6000)
    p.add_argument('--warmup-scales',type=float,nargs='+',default=[1.])
    p.add_argument('--cold-tail',action='store_true')
    a=p.parse_args()
    out=a.outdir.resolve();out.mkdir(parents=True,exist_ok=True)
    here=Path(__file__).resolve().parent
    old=json.load(gzip.open(a.prefix_restart,'rt'))
    cfg=dict(old['tail_config'])
    for key in ['initialCheckpoint','traceFile','secantCheckpoint','designInitialCheckpoint']:
        cfg.pop(key,None)
    controls=list(cfg['valleyControls']);previous=controls[0];controls[0]=a.beta0;cfg['valleyControls']=controls
    startup=out/'startup-config.json';startup.write_text(json.dumps(cfg,indent=2)+'\n')
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
             VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(a.sparse_helper.resolve()),
             VISIBLE_FLEX_SPARSE_TRACE=str(out/'linear-trace.jsonl'))
    raw=out/'worker-port.json'
    subprocess.run([sys.executable,str(here/'recovered_q021/export_original_worker_port.py'),
                    '--source-topic',str(a.source_topic.resolve()),'--config',str(startup),'--out',str(raw)],env=env,check=True)
    port=json.loads(raw.read_text());port['cut']['_prefix_bridge']=old['frozen_profile']['prefix_bridge']
    portfile=out/'port.json';portfile.write_text(json.dumps(port,indent=2)+'\n')
    if not a.cold_tail:
        cfg['designInitialCheckpoint']=str(a.tail_restart.resolve())
    cfg['traceFile']=str(out/'worker-trace.jsonl')
    config=out/'config.json';config.write_text(json.dumps(cfg,indent=2)+'\n')
    profile=out/'profile.json';profile.write_text(json.dumps(old['frozen_profile'],indent=2)+'\n')
    numeric=old['config'];angular=numeric['angular']
    command=[sys.executable,str(here/'couple_new_first_valley.py'),
             '--source-topic',str(a.source_topic.resolve()),'--short-bridge',str(a.short_bridge.resolve()),
             '--restart-port',str(a.restart_port.resolve()),
             '--profile',str(profile),'--chart',str(a.chart.resolve()),'--linear-port',str(portfile),
             '--tail-config',str(config),'--out-prefix',str(out/'seed'),'--restart',str(a.prefix_restart.resolve()),
             '--amplitude',str(a.amplitude),'--warp-reference',str(a.amplitude),
             '--modes',str(numeric['modes']),'--angular',str(angular),'--audit-angular',str(2*angular),
             '--nodes',str(a.nodes),'--max-nodes',str(a.max_nodes),'--tol',str(numeric['tol']),
             '--bc-tol',str(numeric['bc_tol']),'--physical-bc-tol',str(numeric['physical_bc_tol']),
             '--node-heap','2304','--warmup-scales',*[str(x) for x in a.warmup_scales],'--lagged-tail']
    record=dict(scope=__doc__,command=command,beta0_change=[previous,a.beta0],
                 tail_initialization='new_metric_linear_state' if a.cold_tail else 'explicit_old_metric_initial_coordinates',
                 inputs={str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest()
                         for f in [a.prefix_restart,a.tail_restart,a.restart_port,a.chart,a.sparse_helper,a.short_bridge]},
                 prefix_delta_solved_again=True,same_metric_refinement=False)
    (out/'continuation-command.json').write_text(json.dumps(record,indent=2)+'\n')
    result=subprocess.run(command,env=env)
    record['returncode']=result.returncode
    (out/'continuation-command.json').write_text(json.dumps(record,indent=2)+'\n')
    raise SystemExit(result.returncode)


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Continue an accepted actual m3 state along the raw projected compact-core path."""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','short-bridge','sparse-helper','chart','linear-port','prefix-restart','tail-restart','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--homotopy',type=float,required=True)
    p.add_argument('--amplitude',type=float)
    p.add_argument('--round-halfwidth',type=float,default=.21)
    p.add_argument('--round-transition',type=float,default=.08)
    p.add_argument('--control-transition',type=float,default=.16)
    p.add_argument('--nodes',type=int,default=801)
    p.add_argument('--max-nodes',type=int,default=6000)
    p.add_argument('--tail-parts',type=int)
    a=p.parse_args();out=a.outdir.resolve();out.mkdir(parents=True,exist_ok=True)
    rec=json.load(gzip.open(a.prefix_restart,'rt'))
    q=rec['actual_primary_amplitude'] if a.amplitude is None else a.amplitude
    cfg=dict(rec['tail_config'])
    for key in ('initialCheckpoint','secantCheckpoint','designInitialCheckpoint','traceFile','geometricAmplitudePredictor'):
        cfg.pop(key,None)
    cfg['initialCheckpoint']=str(a.tail_restart.resolve());cfg['traceFile']=str(out/'worker-trace.jsonl')
    if a.tail_parts is not None:
        if a.tail_parts<cfg['shootingParts']:raise ValueError('Do not decrease shooting resolution at this entry')
        cfg['shootingParts']=a.tail_parts
    config=out/'config.json';profile=out/'profile.json'
    config.write_text(json.dumps(cfg,indent=2)+'\n')
    profile.write_text(json.dumps(rec['frozen_profile'],indent=2)+'\n')
    command=[sys.executable,str(Path(__file__).with_name('couple_m3_round_core_raw.py')),
      '--source-topic',str(a.source_topic.resolve()),'--short-bridge',str(a.short_bridge.resolve()),
      '--homotopy',str(a.homotopy),'--round-halfwidth',str(a.round_halfwidth),
      '--round-transition',str(a.round_transition),'--control-transition',str(a.control_transition),
      '--profile',str(profile),'--chart',str(a.chart.resolve()),'--linear-port',str(a.linear_port.resolve()),
      '--tail-config',str(config),'--out-prefix',str(out/'seed'),'--restart',str(a.prefix_restart.resolve()),
      '--amplitude',str(q),'--warp-reference',str(rec['warp_reference_q']),
      '--modes',str(rec['config']['modes']),'--angular',str(rec['config']['angular']),
      '--audit-angular',str(2*rec['config']['angular']),'--nodes',str(a.nodes),'--max-nodes',str(a.max_nodes),
      '--tol',str(rec['config']['tol']),'--bc-tol',str(rec['config']['bc_tol']),
      '--physical-bc-tol',str(rec['config']['physical_bc_tol']),
      '--node-heap','2304','--warmup-scales','1','--lagged-tail']
    env=dict(os.environ)
    env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
               VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(a.sparse_helper.resolve()),
               VISIBLE_FLEX_SPARSE_TRACE=str(out/'linear-trace.jsonl'))
    record=dict(scope=__doc__,command=command,exact_circle_only_at_lambda_one=True,
        physical_design_continuation=True,control_path='raw-mean-primary-compact-v1',
        tail_shooting_parts=cfg['shootingParts'],unchanged_tail_acceptance=cfg['solveTolerance'],
        inputs={str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest() for f in
                (a.prefix_restart,a.tail_restart,a.linear_port,a.chart,a.short_bridge,a.sparse_helper)})
    file=out/'continuation-command.json';file.write_text(json.dumps(record,indent=2)+'\n')
    result=subprocess.run(command,env=env);record['returncode']=result.returncode
    file.write_text(json.dumps(record,indent=2)+'\n');raise SystemExit(result.returncode)


if __name__=='__main__':main()

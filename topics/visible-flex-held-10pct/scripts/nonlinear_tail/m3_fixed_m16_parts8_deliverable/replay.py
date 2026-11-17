#!/usr/bin/env python3
"""Reconstruct the accepted M16/parts8 trial from regenerated warm inputs.

Inputs are the fixed M8 prefix and the failed original M16 state described
by record.json. That failed state is only an initial guess. This entry uses
the already published 70-source recovery, sparse source generator and m3
seed package; it stores all regenerated ports and fields in --work.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

p=argparse.ArgumentParser(description=__doc__)
for name in ('base-package','sparse-package','source-topic','short-bridge','chart',
             'initial-prefix','initial-tail','work'):
    p.add_argument('--'+name,type=Path,required=True)
a=p.parse_args();here=Path(__file__).resolve().parent;w=a.work.resolve()
w.mkdir(parents=True,exist_ok=False)
env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1',
     'VISIBLE_FLEX_SPARSE_LINEAR_HELPER':str((a.sparse_package/'sparse_shooting_linear.py').resolve()),
     'VISIBLE_FLEX_SPARSE_TRACE':str(w/'linear-trace.jsonl')}
def write(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')
def run(script,*args):subprocess.run([sys.executable,str(script),*map(str,args)],env=env,check=True)
config=json.loads((here/'tail-config.json').read_text())
write(w/'startup-config.json',config)
run(a.base_package/'export_original_worker_port.py','--source-topic',a.source_topic,
    '--config',w/'startup-config.json','--out',w/'worker-port16.json')
profile=json.loads((here/'profile.json').read_text())
port=json.loads((w/'worker-port16.json').read_text())
port['cut']['_prefix_bridge']=profile['prefix_bridge']
write(w/'port16.json',port);write(w/'profile.json',profile)
config.update(initialCheckpoint=str(a.initial_tail.resolve()),traceFile=str(w/'worker-trace.jsonl'))
write(w/'config.json',config)
run(a.base_package/'couple_m3_smallcut.py','--source-topic',a.source_topic,
    '--short-bridge',a.short_bridge,'--profile',w/'profile.json','--chart',a.chart,
    '--linear-port',w/'port16.json','--tail-config',w/'config.json','--out-prefix',w/'seed',
    '--restart',a.initial_prefix,'--amplitude','.02','--warp-reference','.02','--modes','16',
    '--angular','512','--audit-angular','1024','--nodes','701','--max-nodes','4000',
    '--tol','3e-7','--bc-tol','1e-7','--physical-bc-tol','2e-9','--node-heap','2304',
    '--warmup-scales','1','--lagged-tail','--fixed')
summary=json.loads((w/'seed-summary.json').read_text())
if not summary.get('solver_success'):raise RuntimeError('Original acceptance did not pass')
run(a.base_package/'m3_prefix_endpoint.py','--source-topic',a.source_topic,
    '--short-bridge',a.short_bridge,'--checkpoint',w/'seed.json.gz','--port',w/'port16.json',
    '--output',w/'prefix-endpoint','--angular','512')
run(a.base_package/'m3_prefix_tensor_diagnostic.py','--source-topic',a.source_topic,
    '--short-bridge',a.short_bridge,'--checkpoint',w/'seed.json.gz','--port',w/'port16.json',
    '--output',w/'prefix-tensor-diagnostic.json','--angular','1024')
tail=w/summary['tail_seam']['tail_record']
subprocess.run(['node',str(a.base_package/'export_cut_cartesian.mjs'),str(a.source_topic),
    str(a.source_topic/'scripts/closing_weighted_tail.mjs'),str(tail),str(w/'tail-endpoint.json'),
    '512','.0004'],check=True,env=env)
run(a.base_package/'compare_cut_cartesian.py',w/'prefix-endpoint.npz',w/'tail-endpoint.json',
    w/'cartesian-seam.json')

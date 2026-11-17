#!/usr/bin/env python3
"""Replay the fixed-g radial refinement and its actual saved-map audits.

The previous accepted prefix and tail are regenerated from the earlier
M16/parts8 package. Source recovery and sparse-source construction are
specified in those existing packages. All computed arrays go into --work.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

p=argparse.ArgumentParser(description=__doc__)
for name in ('base-package','m16-package','sparse-package','source-topic','short-bridge',
             'chart','initial-prefix','initial-tail','work'):
    p.add_argument('--'+name,type=Path,required=True)
a=p.parse_args();here=Path(__file__).resolve().parent;w=a.work.resolve()
w.mkdir(parents=True,exist_ok=False)
env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1',
     'VISIBLE_FLEX_SPARSE_LINEAR_HELPER':str((a.sparse_package/'sparse_shooting_linear.py').resolve()),
     'VISIBLE_FLEX_SPARSE_TRACE':str(w/'linear-trace.jsonl')}
def write(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')
def run(script,*args):subprocess.run([sys.executable,str(script),*map(str,args)],env=env,check=True)
config=json.loads((a.m16_package/'tail-config.json').read_text())
write(w/'startup-config.json',config)
run(a.base_package/'export_original_worker_port.py','--source-topic',a.source_topic,
    '--config',w/'startup-config.json','--out',w/'worker-port16.json')
profile=json.loads((a.m16_package/'profile.json').read_text())
port=json.loads((w/'worker-port16.json').read_text());port['cut']['_prefix_bridge']=profile['prefix_bridge']
write(w/'port16.json',port);write(w/'profile.json',profile)
config.update(initialCheckpoint=str(a.initial_tail.resolve()),traceFile=str(w/'worker-trace.jsonl'))
write(w/'config.json',config)
run(here/'couple_m3_radial_refine.py','--source-topic',a.source_topic,
    '--short-bridge',a.short_bridge,'--profile',w/'profile.json','--chart',a.chart,
    '--linear-port',w/'port16.json','--tail-config',w/'config.json','--out-prefix',w/'seed',
    '--restart',a.initial_prefix,'--restart-bisections','1','--amplitude','.02',
    '--warp-reference','.02','--modes','16','--angular','512','--audit-angular','1024',
    '--nodes','1965','--max-nodes','6000','--tol','1e-8','--bc-tol','1e-7',
    '--physical-bc-tol','2e-9','--node-heap','2304','--warmup-scales','1','--lagged-tail',
    '--fixed','--preserve-restart-mesh')
summary=json.loads((w/'seed-summary.json').read_text())
if not summary.get('solver_success'):raise RuntimeError('Original coupled acceptance did not pass')
common=['--source-topic',a.source_topic,'--short-bridge',a.short_bridge,
        '--checkpoint',w/'seed.json.gz','--port',w/'port16.json']
run(a.base_package/'m3_prefix_endpoint.py',*common,'--output',w/'prefix-endpoint','--angular','512')
run(a.base_package/'m3_prefix_tensor_diagnostic.py',*common,
    '--output',w/'prefix-tensor-diagnostic.json','--angular','1024')
tail=w/summary['tail_seam']['tail_record']
subprocess.run(['node',str(a.base_package/'export_cut_cartesian.mjs'),str(a.source_topic),
    str(a.source_topic/'scripts/closing_weighted_tail.mjs'),str(tail),str(w/'tail-endpoint.json'),
    '512','.0004'],check=True,env=env)
run(a.base_package/'compare_cut_cartesian.py',w/'prefix-endpoint.npz',w/'tail-endpoint.json',
    w/'cartesian-seam.json')
run(here/'m3_compare_prefix_jets.py','--source-topic',a.source_topic,'--short-bridge',a.short_bridge,
    '--coarse',a.initial_prefix,'--fine',w/'seed.json.gz','--port',w/'port16.json',
    '--output',w/'prefix-two-map-jets.json','--angular','512')

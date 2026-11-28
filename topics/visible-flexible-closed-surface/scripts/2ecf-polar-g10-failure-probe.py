#!/usr/bin/env python3
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,time,argparse,numpy as np
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import importlib.util
W=Path(__file__).parent; S=Path('/workspace/scratch/2ecfcd6930d6/math-research-public/topics/visible-flexible-closed-surface/scripts')
spec=importlib.util.spec_from_file_location('dense',W/'2ecf-polar-c2-g10-prepare.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
a=argparse.Namespace(scripts=S,parent_entry=W/'2ecf-polar-c2-prefix-prepare.py',parent_prepared=W/'polar-c2-extended-prepared.json',third_observer=W/'polar-independent-G3-shifted256-independent.json')
parent,definition,basis,caches,mods,obs=p.load_parent(a)
nodes,added,_,_=p.dense_grid(caches['training'].nodes,basis,obs)
u=caches['training'].u;s=float(added[667]); rows=[]
with mods['background'].NonfoldPolarBackground(S,S.parent/'notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json',W/'target-zero.json',W/'gap105-prefix-ramp-master.npz',W/'gap105-prefix-coast-master.npz') as source:
 for count in (1,2,4,8,128):
  t=time.monotonic(); trials=[];packets=[]
  for idx in np.array_split(np.arange(len(u)),count):
   try:
    q=source.sample([s],u[idx]);trials.append(dict(lo=int(idx[0]),hi=int(idx[-1])+1,success=True,diagnostics=q['source_point_diagnostics']));packets.append(q['jets'])
   except ArithmeticError as e:trials.append(dict(lo=int(idx[0]),hi=int(idx[-1])+1,success=False,error=str(e)))
  row=dict(chunks=count,s=s,allSuccess=all(v['success'] for v in trials),trials=trials,seconds=time.monotonic()-t);rows.append(row); print(json.dumps(row),flush=True)
  if row['allSuccess']:
   np.save(W/'polar-G10-failure-probe-success-jets.npy',np.concatenate(packets,axis=2));break
p.write(W/'polar-G10-failure-probe.json',dict(sourceMetadata=source.metadata,exit=source.exit_receipt,physicalMissingRowIndex=667,rows=rows,unchangedInverseTolerance=5e-14,changedSourceFunction=False))

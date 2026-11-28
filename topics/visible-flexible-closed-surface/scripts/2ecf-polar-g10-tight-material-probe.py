#!/usr/bin/env python3
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json,time,importlib.util,sys,numpy as np
from pathlib import Path
W=Path(__file__).parent;S=Path('/workspace/scratch/2ecfcd6930d6/math-research-public/topics/visible-flexible-closed-surface/scripts')
def load(p,name):
 q=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(q);sys.modules[name]=m;q.loader.exec_module(m);return m
m=load(S/'6a65-geometry-nonfold-polar-background-v2.py','tightprobe')
rows=[]
with m.NonfoldPolarBackground(S,S.parent/'notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json',W/'target-zero.json',W/'gap105-prefix-ramp-master.npz',W/'gap105-prefix-coast-master.npz') as source:
 core=source.field.master._ports.core;orig=core.at_material
 for tol in (2e-15,5e-16):
  def refined(*args,**kwargs):
   kwargs['tolerance']=tol;kwargs['max_iterations']=100;return orig(*args,**kwargs)
  core.at_material=refined;source.field.clock_cache=None
  start=time.monotonic()
  try:
   q=source.sample([.856679790800223],2*np.pi*np.arange(128)/128)
   row=dict(tolerance=tol,success=True,diagnostics=q['source_point_diagnostics'],seconds=time.monotonic()-start);np.save(W/('polar-G10-tight-material-'+str(tol)+'-jets.npy'),q['jets'])
  except Exception as e:row=dict(tolerance=tol,success=False,error=str(e),seconds=time.monotonic()-start)
  rows.append(row);print(json.dumps(row),flush=True)
 core.at_material=orig
(W/'polar-G10-tight-material-probe.json').write_text(json.dumps(dict(rows=rows,exit=source.exit_receipt),separators=(',',':'))+'\n')

"""Calibrate the three physical cell phases with fixed residual scales.

The former angular residual z/hypot(u,z) saturated because momentum uses
cell-dependent tiny source units. This version scales each momentum by its
initial magnitude, keeps all original ODE equations, and bounds design controls.
It is a linear metric design calculation, not nonlinear capacity evidence.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,json,subprocess,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
p=argparse.ArgumentParser();p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--config',type=Path,required=True);p.add_argument('--factory',type=Path,required=True);p.add_argument('--control-count',type=int);p.add_argument('--out',type=Path,required=True);p.add_argument('--steps',type=int,default=128);p.add_argument('--max-evals',type=int,default=80);a=p.parse_args()
cfg=json.loads(a.config.read_text());worker=Path(__file__).with_name('calibration_physical_worker.mjs');a.out.parent.mkdir(parents=True,exist_ok=True)
proc=subprocess.Popen(['node',str(worker),str(a.source_topic),str(a.factory),str(a.config),str(a.steps)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
initial=list(cfg['outerCellDesign']['valleyControls'] if 'outerCellDesign' in cfg else cfg['valleyControls']);initial=initial[:a.control_count] if a.control_count else initial
trace=[];started=time.monotonic();scales=None
def fun(x):
 global scales
 proc.stdin.write(json.dumps(list(map(float,x)))+'\n');proc.stdin.flush();line=proc.stdout.readline()
 if not line:raise RuntimeError('Calibration worker closed')
 r=json.loads(line);r['seconds']=time.monotonic()-started
 if 'error'in r:raise RuntimeError(r['error'])
 z=np.array([v['momentum']for v in r['rows']])
 if scales is None:scales=np.maximum(abs(z),1.)
 f=z/scales;r['fixed_scaled_residual']=f.tolist();trace.append(r)
 with a.out.with_suffix('.jsonl').open('a')as h:h.write(json.dumps(r)+'\n')
 print(json.dumps(dict(controls=r['controls'],residual=f.tolist(),gains=[v['gain']for v in r['rows']],seconds=r['seconds'])),flush=True)
 return f
try:
 result=least_squares(fun,np.array(initial),bounds=(-5.,15.),diff_step=1e-4,x_scale='jac',ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=a.max_evals)
 score=float(np.max(np.abs(fun(result.x))));best=min(trace,key=lambda r:max(map(abs,r['fixed_scaled_residual'])))
 out=dict(scope=__doc__,success=bool(score<1e-7),message=str(result.message),steps=a.steps,controls=list(map(float,result.x)),fixed_scales=scales.tolist(),residual_max=score,best=best,seconds=time.monotonic()-started,config_sha256=hashlib.sha256(a.config.read_bytes()).hexdigest(),worker_sha256=hashlib.sha256(worker.read_bytes()).hexdigest(),evaluations=len(trace))
 a.out.write_text(json.dumps(out,indent=2)+'\n')
 if score<1e-7:
  if 'outerCellDesign' in cfg:cfg['outerCellDesign']['valleyControls']=list(map(float,result.x))
  else:cfg['valleyControls'][:len(result.x)]=list(map(float,result.x))
  a.out.with_name(a.out.stem+'-config.json').write_text(json.dumps(cfg,indent=2)+'\n')
 print(json.dumps(out),flush=True)
finally:
 proc.stdin.close();proc.wait(timeout=10)

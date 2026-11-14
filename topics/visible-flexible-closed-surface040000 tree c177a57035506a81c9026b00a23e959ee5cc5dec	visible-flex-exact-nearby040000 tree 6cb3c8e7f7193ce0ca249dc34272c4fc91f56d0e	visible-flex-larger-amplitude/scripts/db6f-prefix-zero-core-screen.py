#!/usr/bin/env python3
"""Re-screen stored meridian designs using an endpoint support witness, ell=0.
All outputs are first-order, sampled geometric diagnostics, not isometries.
A design satisfying these comparisons must subsequently be solved nonlinearly.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse, importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq
S=Path(__file__).resolve().parent;N=S.parent/'notes'
def module(name,file):
 spec=importlib.util.spec_from_file_location(name,file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--old-screen',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--target',type=float,default=.051);a=p.parse_args()
sys.path[:0]=[str(N),str(a.source_root/'topics/large-amplitude-twist-flex/scripts')]
m=module('flat_screen',S/'950f-prefix-flat-accel-screen.py');Flat,Cos=m.build_flow();port=json.loads(a.port.read_text());old=json.loads(a.old_screen.read_text())
report=dict(scope=__doc__,target_comparison_hold_ratio=a.target,rows=[]);start=time.time()
for item in old['rows']:
 for r in item['roots']:
  cfg=r['config'];cls=Flat if cfg['ramp_law']=='flat' else Cos
  try:
   f=cls(cfg,port,1,.001,32,3);line=f.backward_line();s=np.unique(np.r_[np.linspace(0,f.end,1201),f.breaks]);fg=np.empty((2,len(s)))
   for j,(lo,hi,sol,scale) in enumerate(line.segments):
    mask=(s>=lo)&((s<hi) if j+1<len(line.segments) else (s<=hi))
    if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
   aa,ap,app=f.profile(s);b=np.sqrt(1-ap*ap);h=cumulative_trapezoid(b,s,initial=0);K=float(np.maximum(abs(app)/b,b/aa).max())
   def diam(q):return 2*math.sqrt(float(np.maximum((aa+q*fg[0])**2+(h+q*fg[1])**2,(aa-q*fg[0])**2+(h-q*fg[1])**2).max()))
   if .24/diam(.12)<a.target:continue
   q=brentq(lambda q:2*q/diam(q)-a.target,.001,.12,xtol=1e-13);D=diam(q)
   th=2*np.pi*np.arange(768)/768;co=np.cos(3*th);si=np.sin(3*th);cs=np.cos(th-np.pi/3);sn=np.sin(th-np.pi/3)
   horizontal=(aa[:,None]+q*fg[0,:,None]*co)*cs+q*fg[0,:,None]*si*sn/3
   A=horizontal.max(axis=1);B=h-q*abs(fg[1]);bounds=np.sqrt(np.maximum(1+q-A,0)**2+np.maximum(B,0)**2);j=int(bounds.argmin())
   row=dict(config=cfg,q=q,D=D,comparison_hold_ratio=2*q/D,support_projection_bound=float(bounds[j]),support_projection_ratio=float(bounds[j]/D),support_witness_s=float(s[j]),cut_height=float(abs(q*fg[1,-1])),cut_gain=float(fg[1,-1]),background_K=K,background_KD=K*D,core_KD=D/(1-8*q),meridian_length=f.end,background_height=float(h[-1]),core_line_residual=float(line.core[1]),min_height_sample=float(B.min()))
   report['rows'].append(row)
  except Exception as e:report['rows'].append(dict(config=cfg,error=repr(e)))
 report['seconds']=time.time()-start;report['ranked'] = sorted([r for r in report['rows']if 'cut_height'in r and max(r['background_KD'],r['core_KD'])<32 and r['support_projection_ratio']>.05],key=lambda r:r['cut_height'])[:20];a.out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(count=len(report['rows']),seconds=report['seconds'],top=report['ranked'][:6])),flush=True)

#!/usr/bin/env python3
"""First-order meridian-design search; no nonlinear or certified geometric claim."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import cumulative_trapezoid
S=Path(__file__).resolve().parent;N=S.parent/'notes'
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--target',type=float,default=.051);a=p.parse_args()
sys.path[:0]=[str(N),str(a.source_root/'topics/large-amplitude-twist-flex/scripts')]
spec=importlib.util.spec_from_file_location('flat_screen',S/'950f-prefix-flat-accel-screen.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);Flat,Cos=m.build_flow();port=json.loads(a.port.read_text())
configs=[dict(direction='outward',vu=vu,vd=vd,ramp=eps,cycles=1,cut_radius=.6,cut_slope=.5,ramp_law='flat',ramp_eta=.05)for vu in [.14,.17,.2,.23]for vd in [.18,.22,.26]for eps in [.4,.48]]
report=dict(scope=__doc__,target=a.target,rows=[]);start=time.time()
for cfg in configs:
 row=dict(config=cfg)
 try:
  def scalar(delta):return float(Flat({**cfg,'delta':delta},port,1,.001,32,3).backward_line().core[1])
  br=None;old=None
  for d in [.025,.04,.055,.07,.085,.10,.12,.15]:
   z=scalar(d)
   if old and z*old[1]<0:br=(old[0],d);break
   old=d,z
  if br is None:raise ValueError('No first root in scan')
  delta=brentq(scalar,*br,xtol=2e-12);cfg={**cfg,'delta':delta};f=Flat(cfg,port,1,.001,32,3);line=f.backward_line();s=np.unique(np.r_[np.linspace(0,f.end,1201),f.breaks]);fg=np.empty((2,len(s)))
  for j,(lo,hi,sol,scale)in enumerate(line.segments):
   mask=(s>=lo)&((s<hi)if j+1<len(line.segments)else(s<=hi))
   if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
  aa,ap,app=f.profile(s);b=np.sqrt(1-ap*ap);h=cumulative_trapezoid(b,s,initial=0);K=float(np.maximum(abs(app)/b,b/aa).max())
  def diam(q):return 2*math.sqrt(float(np.maximum((aa+q*fg[0])**2+(h+q*fg[1])**2,(aa-q*fg[0])**2+(h-q*fg[1])**2).max()))
  if .24/diam(.12)<a.target:raise ValueError('Required q exceeds .12')
  q=brentq(lambda q:2*q/diam(q)-a.target,.001,.12,xtol=1e-13);D=diam(q)
  row=dict(config=cfg,q=q,D=D,cut_height=float(abs(q*fg[1,-1])),cut_gain=float(fg[1,-1]),background_K=K,background_KD=K*D,core_KD=D/(1-8*q),meridian_length=f.end,background_height=float(h[-1]),line_residual=float(line.core[1]))
 except Exception as e:row['error']=repr(e)
 report['rows'].append(row);report['seconds']=time.time()-start;report['ranked']=sorted([r for r in report['rows']if 'cut_height'in r and max(r['background_KD'],r['core_KD'])<32],key=lambda r:r['cut_height'])[:12];a.out.write_text(json.dumps(report,indent=2)+'\n')
 if len(report['rows'])%4==0:print(json.dumps(dict(count=len(report['rows']),seconds=report['seconds'],best=report['ranked'][:2])),flush=True)

#!/usr/bin/env python3
"""Small, fully identified linear m3 prefix design against an actual tail port.

This solves only the linear first-mode branch equation. The printed height,
curvature and transfer are diagnostics, not a nonlinear or closed candidate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
import argparse,copy,hashlib,importlib.util,json,math,time
import numpy as np
from scipy.optimize import brentq

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
 p=argparse.ArgumentParser();p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
 p.add_argument('--vu',type=float,required=True);p.add_argument('--vd',type=float,required=True);p.add_argument('--delta-guess',type=float,default=.07254)
 p.add_argument('--short-bridge',type=Path);p.add_argument('--curvature',type=float,default=4.);p.add_argument('--peak-fraction',type=float,default=.2);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 src=a.source_topic;ad=module('m3_design_adaptive',src/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');patch=module('m3_design_flat',src/'scripts/db6f-prefix-flat-profile.py');patch.install(ad);ad.old.install_source(src/'repro/source-root')
 port=json.loads(a.port.read_text());cfg=dict(direction='outward',vu=a.vu,vd=a.vd,ramp=.4,ramp_eta=.05,ramp_law='flat',cycles=1,delta=a.delta_guess)
 if any(m!=3*(j+1)for j,m in enumerate(port['modes'])):raise ValueError('Port must use literal physical modes 3,6,...')
 if a.short_bridge:
  bridge=module('m3_design_short',a.short_bridge);bridge.install();cfg['prefix_bridge']=dict(kind='turn_plateau_v1',curvature=a.curvature,peak_fraction=a.peak_fraction);port['cut']['_prefix_bridge']=cfg['prefix_bridge']
 Flow,_=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.));cache={};started=time.time()
 def make(d):return Flow({**cfg,'delta':float(d)},port,4,.02,128,3)
 def target(d):
  d=float(d)
  if d not in cache:cache[d]=float(make(d).backward_line().core[1])
  return cache[d]
 lo=max(.002,a.delta_guess*.6);hi=min(.6,a.delta_guess*1.6)
 if target(lo)*target(hi)>0:
  values=[(x,target(x))for x in [.004,.008,.015,.025,.04,.06,.08,.11,.15,.22,.32,.48]]
  intervals=[(x0,x1)for(x0,y0),(x1,y1)in zip(values,values[1:])if y0*y1<0]
  if not intervals:raise RuntimeError('No scanned linear root: '+str(values))
  lo,hi=min(intervals,key=lambda z:abs((z[0]+z[1])/2-a.delta_guess))
 delta=brentq(target,lo,hi,xtol=2e-12);cfg['delta']=float(delta);f=make(delta);line=f.backward_line()
 x=np.linspace(0,1,65);s=x*f.end;fg=np.empty((2,len(s)))
 for j,(lo,hi,sol,scale)in enumerate(line.segments):
  mask=(s>=lo)&((s<hi)if j+1<len(line.segments)else(s<=hi))
  if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
 ar,ap,_=f.profile(s);h=fg[0]/ar;rhs=f.linear_rhs(f.end,fg[:,-1]);hp=(rhs[0]*ar[-1]-fg[0,-1]*ap[-1])/ar[-1]**2*f.end
 chart=dict(scope='Normalized linear m3 f/a; numerical chart only, frozen when used in one design.',reference_profile=cfg,knots=x.tolist(),values=h.tolist(),final_derivative=float(hp))
 ss=np.unique(np.r_[np.linspace(0,f.end,2049),f.breaks]);aa,vv,acc=f.profile(ss);bb=np.sqrt(1-vv*vv)
 bridge_info=f.bridge.summary() if hasattr(f.bridge,'summary') else dict(kind='original_DirectionalBridge',length=float(f.bridge.L),cut=port['cut'])
 result=dict(scope=__doc__,source_topic=str(src),port=str(a.port),port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest(),profile=cfg,meridian_length=f.end,bridge=bridge_info,linear_H3_per_q=float(fg[1,-1]),linear_core_m6_transversality=float(f.backward_line(1).core[1]),chart_range=[float(h.min()),float(h.max())],sampled_background=dict(height=float(np.trapezoid(bb,ss)),meridian_curvature=float(np.max(np.abs(acc)/bb)),parallel_curvature=float(np.max(bb/aa)),radius_max=float(np.max(aa))),root_samples=sorted(cache.items()),seconds=time.time()-started)
 for name,value in [('linear',result),('profile',cfg),('chart',chart)]: (a.out/(name+'.json')).write_text(json.dumps(value,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items()if k not in ['scope','source_topic','port','port_sha256','root_samples','bridge']}) ,flush=True)
if __name__=='__main__':main()

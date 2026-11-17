#!/usr/bin/env python3
"""Actual low-mode transfer through multicycle meridians; linear design only.

Each record is a distinct physical metric. No sampled background number or
linear transfer is a nonlinear isometric or closed-surface certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse, hashlib, importlib.util, json, math, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--short-bridge',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
 p.add_argument('--direction',choices=['outward','inward'],default='outward');p.add_argument('--mode',type=int,default=2);p.add_argument('--cycles',type=int,default=2);p.add_argument('--speeds',default='.65:.7,.75:.75,.85:.8')
 p.add_argument('--scan',default='.025,.04,.06,.09,.13,.18,.24,.31,.4,.52,.68')
 p.add_argument('--ramp',type=float,default=.4);p.add_argument('--eta',type=float,default=.05);p.add_argument('--curvature',type=float,default=4.);p.add_argument('--peak-fraction',type=float,default=.2)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);src=a.source_topic
 ad=module('transfer_ad',src/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');module('transfer_flat',src/'scripts/db6f-prefix-flat-profile.py').install(ad);ad.old.install_source(src/'repro/source-root');module('transfer_short',a.short_bridge).install()
 port=json.loads(a.port.read_text());assert port['modes'][0]==a.mode
 Flow,_=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.));record=dict(scope=__doc__,argv=sys.argv,port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest(),source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in (Path(__file__),a.short_bridge,src/'scripts/950f-prefix-adaptive-chart-bvp-v2.py',src/'scripts/db6f-prefix-flat-profile.py')},designs=[]);started=time.monotonic()
 for speed in a.speeds.split(','):
  vu,vd=map(float,speed.split(':'));cfg=dict(direction=a.direction,vu=vu,vd=vd,ramp=a.ramp,ramp_eta=a.eta,ramp_law='flat',delta=.1,cycles=a.cycles,prefix_bridge=dict(kind='turn_plateau_v1',curvature=a.curvature,peak_fraction=a.peak_fraction));port['cut']['_prefix_bridge']=cfg['prefix_bridge'];cache={}
  def make(d):return Flow({**cfg,'delta':float(d)},port,4,.02,128,a.mode)
  def target(d):
   d=float(d)
   if d not in cache:cache[d]=float(make(d).backward_line().core[1])
   return cache[d]
  row=dict(profile=cfg,scan=[],roots=[],failures=[])
  for d in map(float,a.scan.split(',')):
   try:row['scan'].append([d,target(d)])
   except Exception as e:row['scan'].append([d,None]);row['failures'].append(dict(delta=d,error=repr(e)))
  for index,((lo,y0),(hi,y1))in enumerate(zip(row['scan'],row['scan'][1:])):
   if y0 is None or y1 is None or y0*y1>=0:continue
   try:
    delta=brentq(target,lo,hi,xtol=2e-12);f=make(delta);line=f.backward_line();xs=np.linspace(0,1,65);s=xs*f.end;fg=np.empty((2,len(s)))
    for j,(l,h,sol,scale)in enumerate(line.segments):
     mask=(s>=l)&((s<h)if j+1<len(line.segments)else(s<=h))
     if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
    ar,ap,_=f.profile(s);hv=fg[0]/ar;rhs=f.linear_rhs(f.end,fg[:,-1]);hp=(rhs[0]*ar[-1]-fg[0,-1]*ap[-1])/ar[-1]**2*f.end
    ss=np.unique(np.r_[np.linspace(0,f.end,4097),f.breaks]);aa,v,acc=f.profile(ss);bb=np.sqrt(1-v*v);z=np.r_[0.,np.cumsum(np.diff(ss)*(bb[:-1]+bb[1:])/2)];radius=float(np.hypot(aa,z).max());K=float(np.max(np.maximum(np.abs(acc)/bb,bb/aa)))
    config={**cfg,'delta':float(delta)};entry=dict(bracket=[lo,hi],delta=delta,core_residual=target(delta),linear_H_per_q=float(fg[1,-1]),background=dict(height=float(z[-1]),center_radius=radius,curvature=K,diameter_upper_sample=2*radius,KD_product_sample=2*radius*max(K,8.002)),meridian_length=f.end,chart_range=[float(hv.min()),float(hv.max())],higher_transversality=[float(f.backward_line(j).core[1])for j in (1,2,3)])
    folder=a.out/f'v{vu:g}-{vd:g}-root{len(row["roots"])}';folder.mkdir(exist_ok=True);(folder/'profile.json').write_text(json.dumps(config,indent=2)+'\n');(folder/'chart.json').write_text(json.dumps(dict(reference_profile=config,knots=xs.tolist(),values=hv.tolist(),final_derivative=float(hp)),indent=2)+'\n');entry['directory']=str(folder);row['roots'].append(entry);print(json.dumps(dict(speed=speed,**entry)),flush=True)
   except Exception as e:row['failures'].append(dict(bracket=[lo,hi],error=repr(e)));print(json.dumps(row['failures'][-1]),flush=True)
  record['designs'].append(row);record['seconds']=time.monotonic()-started;(a.out/'summary.json').write_text(json.dumps(record,indent=2)+'\n')
if __name__=='__main__':main()

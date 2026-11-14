#!/usr/bin/env python3
"""Exact finite transfer search for two linear core resonances.

The matrices on constant radial-speed segments are exact for the linearized
Frenet equation. Turns are instantaneous in this design screen, so resulting
profiles are NOT C2 surfaces. The final original smooth bridge is integrated
from the existing physical finite linear tail port. Candidates must be
smoothed, re-solved nonlinearly and matched to the true tail at fixed metric.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares,minimize

S=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('alternative_root_scan',S/'root_profile_scan.py');base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)

def transfer(a0,a1,v,m):
 b=math.sqrt(1-v*v);q=m*m
 P=np.array([[-(q-1),-q*b/v],[(q-1)*v/b,q]])
 return np.eye(2)+(a1/a0-1)*P

def dwell(radius,length,m):return np.array([[1.,-m*m*length/radius],[0.,1.]])

def segments(x,kind):
 if kind=='one':
  delta,up,down=x
  return [(1.,1+delta,up),(1+delta,1.,-down)],[]
 if kind=='dwell':
  delta,up,down,wait=x
  return [(1.,1+delta,up),(1+delta,1.,-down)],[(1,wait)]
 if kind=='two':
  d1,d2,u1,v1,u2,v2=x
  return [(1.,1+d1,u1),(1+d1,1.,-v1),(1.,1+d2,u2),(1+d2,1.,-v2)],[]
 if kind=='valley':
  upR,lowR,up,down,back=x
  return [(1.,upR,up),(upR,lowR,-down),(lowR,1.,back)],[]
 raise ValueError(kind)

class Search:
 def __init__(self,port,kind):
  self.port=port;self.kind=kind;self.bridges={}
  for m in [2,4]:
   cut,slope=base.parse_port(port,m);self.bridges[m]=base.Bridge(cut,m,slope)
  bridge=self.bridges[2];s=np.linspace(0,bridge.L,2001);a,v,acc=bridge.profile(s)
  self.bridge_height=float(np.trapezoid(np.sqrt(1-v*v),s))
  self.bounds={
   'one':([.005,.12,.12],[.7,.94,.94]),
   'dwell':([.005,.12,.12,0.],[.6,.94,.94,.7]),
   'two':([.005,.005,.15,.15,.15,.15],[.6,.6,.94,.94,.94,.94]),
   'valley':([1.005,.5,.15,.15,.15],[1.6,.995,.94,.94,.94])}[kind]
 def image(self,x,m):
  segs,pauses=segments(x,self.kind);pauses=dict(pauses);y=np.array([1.,0.])
  for j,(a0,a1,v) in enumerate(segs):
   if j in pauses:y=dwell(a0,pauses[j],m)@y
   y=transfer(a0,a1,v,m)@y
  return y
 def residual(self,x):
  out=[]
  for m in [2,4]:
   y=self.image(x,m);y/=np.linalg.norm(y);b=self.bridges[m].initial
   out.append(y[0]*b[1]-y[1]*b[0])
  return np.array(out)
 def height(self,x):
  segs,pauses=segments(x,self.kind)
  return self.bridge_height+sum(abs(a1-a0)*math.sqrt(1-v*v)/abs(v) for a0,a1,v in segs)+sum(t for j,t in pauses)
 def summary(self,x):
  segs,pauses=segments(x,self.kind)
  turns=[math.asin(segs[0][2])]+[math.asin(segs[j+1][2])-math.asin(segs[j][2]) for j in range(len(segs)-1)]+[-math.asin(segs[-1][2])]
  gains={str(m):self.image(x,m).tolist() for m in [2,4]}
  return dict(kind=self.kind,x=list(x),segments=[dict(a0=a0,a1=a1,v=v,length=(a1-a0)/v,height=abs(a1-a0)*math.sqrt(1-v*v)/abs(v)) for a0,a1,v in segs],pauses=pauses,residual=self.residual(x).tolist(),residual_max=float(abs(self.residual(x)).max()),height=self.height(x),bridge_height=self.bridge_height,bridge_length=self.bridges[2].L,turn_total_angle=sum(abs(t)for t in turns),optimistic_turn_length_at_K8=sum(abs(t)for t in turns)/8,maximum_radius=max(max(a0,a1)for a0,a1,v in segs),minimum_radius=min(min(a0,a1)for a0,a1,v in segs),terminal_vectors=gains)
 def run(self,seeds,seed):
  rng=np.random.default_rng(seed);lo=np.array(self.bounds[0]);hi=np.array(self.bounds[1]);found=[];begin=time.time()
  for j in range(seeds):
   x0=lo+(hi-lo)*rng.uniform(.05,.95,len(lo))
   z=least_squares(self.residual,x0,bounds=(lo,hi),xtol=3e-11,ftol=3e-11,gtol=3e-11,max_nfev=180)
   if max(abs(self.residual(z.x)))<2e-7:
    zz=minimize(self.height,z.x,bounds=list(zip(lo,hi)),constraints=[dict(type='eq',fun=self.residual)],method='SLSQP',options=dict(ftol=2e-11,maxiter=200))
    xx=zz.x if max(abs(self.residual(zz.x)))<1e-7 else z.x
    row=self.summary(xx);row.update(seed_index=j,optimized=bool(zz.success))
    if not any(np.linalg.norm(np.array(r['x'])-xx)<1e-4 for r in found):found.append(row)
  found.sort(key=lambda r:r['height'])
  return dict(scope=__doc__,kind=self.kind,seed=seed,seeds=seeds,seconds=time.time()-begin,bridge_initial={str(m):self.bridges[m].initial.tolist() for m in [2,4]},rows=found)

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--kind',choices=['one','dwell','two','valley'],default='one');p.add_argument('--seeds',type=int,default=100);p.add_argument('--seed',type=int,default=20261110);p.add_argument('--first-max',type=float,default=.94);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 search=Search(json.loads(a.port.read_text()),a.kind);search.bounds[1][{'one':1,'dwell':1,'two':2,'valley':2}[a.kind]]=a.first_max;r=search.run(a.seeds,a.seed);a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(kind=a.kind,candidates=len(r['rows']),seconds=r['seconds'],best=r['rows'][:3])))
if __name__=='__main__':main()

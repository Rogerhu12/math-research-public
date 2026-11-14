#!/usr/bin/env python3
"""Fixed-metric Hermite outward and C2 turning probes.

The finite Fourier Frenet initial-value system is not a validated existence
method in its elliptic regime. Failed refinement or domain exit is retained
as a failed probe, not interpreted as nonexistence. All extrema are samples.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
 os.environ[key]='1'
import argparse,gzip,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_control_base',P/'alternative-outward-probe.py');base=importlib.util.module_from_spec(sp);sp.loader.exec_module(base)

def read_json(path):
 raw=gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_bytes()
 return json.loads(raw)

class HermiteOutward:
 def __init__(self,velocity=.4,length=.65,initial_acceleration=.45):
  self.v=float(velocity);self.S=float(length);self.k0=float(initial_acceleration)
  if not (0<self.v<1 and self.S>0 and 0<=self.k0*self.S<=3*self.v):raise ValueError('Nonmonotone or invalid outward law')
  self.aend=1+self.S*self.v/2+self.k0*self.S**2/12
 def profile(self,s):
  if s>=self.S:return self.aend+self.v*(s-self.S),self.v,0.
  u=max(0.,s/self.S);b=self.k0*self.S;c=3*self.v-2*b;d=b-2*self.v
  return 1+self.S*(b*u*u/2+c*u**3/3+d*u**4/4),b*u+c*u*u+d*u**3,(b+2*c*u+3*d*u*u)/self.S

def law_from_config(cfg):
 if cfg.get('radial_law')=='controlled':
  law=cfg['law']
  if law['kind']=='hermite_outward':return HermiteOutward(law['velocity'],law['length'],law['initial_acceleration']).profile
  if law['kind']=='continued':
   prior=law_from_config(law['base_config']);s0=law['start'];a0,v0,q0=prior(s0)
   if abs(q0)>1e-10:raise ValueError('Continuation entry must have zero acceleration')
   coast=law['coast'];L=law['turn_length'];v1=law['turn_speed'];a1=a0+v0*coast;send=s0+coast+L
   def continued(s):
    if s<=s0:return prior(s)
    if s<=s0+coast:return a0+v0*(s-s0),v0,0.
    if s>=send:return a1+L*(v0+v1)/2+v1*(s-send),v1,0.
    u=(s-s0-coast)/L;dv=v1-v0
    return a1+L*(v0*u+dv*(u**3-u**4/2)),v0+dv*(3*u*u-2*u**3),dv/L*6*u*(1-u)
   return continued
  raise ValueError('Unknown controlled law')
 if cfg.get('radial_law')=='fast_outward':
  sf=importlib.util.spec_from_file_location('alternative_control_fast',P/'alternative-fast-profile.py');fast=importlib.util.module_from_spec(sf);sf.loader.exec_module(fast)
  return fast.FastOutwardLeg(cfg['v'],cfg['S'],cfg['power']).profile
 q=base.Probe(cfg['A'],1,16,cfg['v'],cfg['S'],cfg['amax'],cfg.get('coast_at'),cfg.get('coast_length',.1))
 return q.profile

class ControlledProbe(base.Probe):
 def __init__(self,cfg,M,N):
  self.control_config=cfg;self.control_law=law_from_config(cfg)
  super().__init__(cfg['A'],M,N,.5,1.,2.)
 def profile(self,s):return self.control_law(s)
 def stats(self,s,y):
  row=super().stats(s,y);fr=self.frame(s,y);F=fr['F'];cc=np.cos(self.phi);ss=np.sin(self.phi)
  X=np.stack([cc*F[:,0]-ss*F[:,1],ss*F[:,0]+cc*F[:,1],F[:,2]],axis=1)
  hmajor=1+self.A-self.A/(10*np.sqrt(2));p=np.array([0.,hmajor,0.])
  row.update(ball_radius_max=float(np.linalg.norm(X,axis=1).max()),core_major_witness_latitude_distance=float(np.linalg.norm(X-p,axis=1).min()),minor_axis_point=X[self.N//4].tolist(),app=float(fr['app']))
  return row

def make_probe(cfg,N=None,M=None):
 return ControlledProbe(cfg,M or cfg['M'],N or cfg['N'])

def run(q,y,start,end,steps,rtol,maxstep):
 begin=time.time();rows=[q.stats(start,y)];states=[y.tolist()];last=start;status='success'
 for right in np.linspace(start,end,steps+1)[1:]:
  try:
   sol=solve_ivp(q.fun,(last,right),y,method='DOP853',rtol=rtol,atol=rtol*.01,max_step=min(maxstep,(right-last)/2))
   if not sol.success:raise RuntimeError(sol.message)
   y=sol.y[:,-1];last=float(right);rows.append(q.stats(last,y));states.append(y.tolist())
  except Exception as e:status=repr(e);break
 return dict(status=status,reached_s=last,target_s=end,initial_s=start,rows=rows,coefficient_states=states,final_coefficients=y.tolist(),seconds=time.time()-begin,calls=q.calls,whole_sample_max_metric=max(r['metric_sample']for r in rows),whole_sample_max_kappa=max(r['surface_kappa_sample']for r in rows),whole_sample_min_margin=min(r['margin']for r in rows),whole_sample_ball_radius_max=max(r['ball_radius_max']for r in rows),whole_sample_core_witness_distance=min(r['core_major_witness_latitude_distance']for r in rows))

def main():
 p=argparse.ArgumentParser();p.add_argument('--A',type=float,default=.38);p.add_argument('--M',type=int,default=72);p.add_argument('--N',type=int,default=1152);p.add_argument('--v',type=float,default=.4);p.add_argument('--S',type=float,default=.65);p.add_argument('--k0',type=float,default=.45);p.add_argument('--input',type=Path);p.add_argument('--coast',type=float,default=.1);p.add_argument('--turn-length',type=float,default=.4);p.add_argument('--turn-speed',type=float,default=-.6);p.add_argument('--turn-fraction',type=float,default=1.);p.add_argument('--rtol',type=float,default=1e-11);p.add_argument('--maxstep',type=float,default=.00025);p.add_argument('--steps',type=int,default=40);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
 if args.input:
  prior=read_json(args.input);old=prior['config'];start=prior['reached_s']
  cfg=dict(A=old['A'],M=args.M,N=args.N,radial_law='controlled',law=dict(kind='continued',base_config=old,start=start,coast=args.coast,turn_length=args.turn_length,turn_speed=args.turn_speed))
  end=start+args.coast+args.turn_length*args.turn_fraction
  oldM=old['M'];oldy=np.asarray(prior['final_coefficients']);rr=oldy[:oldM+1];tt=oldy[oldM+1:2*oldM+1];zz=oldy[2*oldM+1:]
  y=np.zeros(3*args.M+2);n=min(oldM,args.M);y[:n+1]=rr[:n+1];y[args.M+1:args.M+1+n]=tt[:n];y[2*args.M+1:2*args.M+2+n]=zz[:n+1]
 else:
  cfg=dict(A=args.A,M=args.M,N=args.N,radial_law='controlled',law=dict(kind='hermite_outward',velocity=args.v,length=args.S,initial_acceleration=args.k0));start=0.;end=args.S
  y=np.zeros(3*args.M+2);y[0]=1;y[1]=args.A;y[2]=-args.A/(10*np.sqrt(2));y[args.M+1]=-2*args.A;y[args.M+2]=4*args.A/(10*np.sqrt(2))
 q=make_probe(cfg);result=run(q,y,start,end,args.steps,args.rtol,args.maxstep)
 cfg.update(rtol=args.rtol,maxstep=args.maxstep,steps=args.steps)
 result.update(scope=__doc__,config=cfg,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),probe_source_sha256=hashlib.sha256((P/'alternative-outward-probe.py').read_bytes()).hexdigest(),fixed_metric_parameter_sha256=hashlib.sha256(json.dumps(dict(A=cfg['A'],law=cfg['law']),sort_keys=True).encode()).hexdigest())
 if args.input:result.update(input=str(args.input),input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),inherited_prefix_max_metric=prior['whole_sample_max_metric'],inherited_prefix_max_kappa=prior['whole_sample_max_kappa'])
 raw=(json.dumps(result,indent=2)+'\n').encode()
 if len(raw)>1000000:
  target=args.out.with_suffix(args.out.suffix+'.gz') if args.out.suffix!='.gz' else args.out;target.write_bytes(gzip.compress(raw,mtime=0))
 else:target=args.out;target.write_bytes(raw)
 print(json.dumps(dict(file=str(target),status=result['status'],reached_s=result['reached_s'],target_s=result['target_s'],seconds=result['seconds'],whole_sample_max_metric=result['whole_sample_max_metric'],whole_sample_max_kappa=result['whole_sample_max_kappa'],whole_sample_core_witness_distance=result['whole_sample_core_witness_distance'],last=result['rows'][-1])))
if __name__=='__main__':main()

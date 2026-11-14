#!/usr/bin/env python3
"""A C2 Hermite outward/turn/coast/brake cycle and linear BVP design search.

The provider is ready to install on PlanarSymmetryFlow. The search concerns
the exact linearized two-mode ODE and the supplied finite linear tail port;
it does not assert a nonlinear solution or a closed-surface certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares,minimize,brentq
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_cycle_scan_base',P/'root_profile_scan.py');scan=importlib.util.module_from_spec(sp);sp.loader.exec_module(scan)

class HermiteTurnCycle:
 def __init__(self,cfg):
  if int(cfg.get('cycles',1))!=1:raise ValueError('HermiteTurnCycle defines one cycle')
  self.cfg=dict(cfg);self.delta=float(cfg['delta']);self.V=float(cfg['vu']);self.W=float(cfg['vd']);self.k0=float(cfg.get('start_acceleration',.45))
  self.T= float(cfg['turn_length']);self.B=float(cfg['brake_length']);self.C=float(cfg.get('coast_outward',0.))
  if min(self.delta,self.V,self.W,self.T,self.B)<=0 or max(self.V,self.W)>=1 or self.k0<0 or self.C<0:raise ValueError('Invalid Hermite cycle parameters')
  self.S=12*self.delta/(math.sqrt(9*self.V*self.V+12*self.k0*self.delta)+3*self.V)
  if self.k0*self.S>3*self.V:raise ValueError('Nonmonotone outward Hermite speed')
  self.L=(self.delta+self.V*self.C+self.T*(self.V-self.W)/2-self.W*self.B/2)/self.W
  if self.L < -2e-12:raise ValueError('Negative inward constant-speed interval')
  self.L=max(self.L,0.);self.end=self.S+self.C+self.T+self.L+self.B
  self.knots=np.unique(np.cumsum([0.,self.S,self.C,self.T,self.L,self.B]));self.Tu=self.S;self.Td=self.end-self.S
 def profile(self,s):
  scalar=np.ndim(s)==0;s=np.asarray(s,float);flat=s.reshape(-1);a=np.ones(flat.size);v=np.zeros(flat.size);acc=np.zeros(flat.size)
  V,W,S,C,T,L,B=self.V,self.W,self.S,self.C,self.T,self.L,self.B
  masks=[flat<=S,(flat>S)&(flat<=S+C),(flat>S+C)&(flat<=S+C+T),(flat>S+C+T)&(flat<=S+C+T+L),flat>S+C+T+L]
  u=np.clip(flat/S,0,1);b=self.k0*S;c=3*V-2*b;d=b-2*V
  a[masks[0]]=1+S*(b*u*u/2+c*u**3/3+d*u**4/4)[masks[0]];v[masks[0]]=(b*u+c*u*u+d*u**3)[masks[0]];acc[masks[0]]=((b+2*c*u+3*d*u*u)/S)[masks[0]]
  a[masks[1]]=1+self.delta+V*(flat[masks[1]]-S);v[masks[1]]=V
  u=np.clip((flat-S-C)/T,0,1);a0=1+self.delta+V*C;dv=-W-V
  a[masks[2]]=(a0+T*(V*u+dv*(u**3-u**4/2)))[masks[2]];v[masks[2]]=(V+dv*(3*u*u-2*u**3))[masks[2]];acc[masks[2]]=(dv/T*6*u*(1-u))[masks[2]]
  a1=a0+T*(V-W)/2
  a[masks[3]]=a1-W*(flat[masks[3]]-S-C-T);v[masks[3]]=-W
  u=np.clip((flat-S-C-T-L)/B,0,1);a2=a1-W*L
  a[masks[4]]=(a2-W*B*(u-u**3+u**4/2))[masks[4]];v[masks[4]]=(-W*(1-3*u*u+2*u**3))[masks[4]];acc[masks[4]]=(6*W/B*u*(1-u))[masks[4]]
  result=tuple(z.reshape(s.shape)for z in (a,v,acc))
  return tuple(float(z)for z in result)if scalar else result
 def summary(self):
  s=np.unique(np.concatenate([np.linspace(l,r,151)for l,r in zip(self.knots[:-1],self.knots[1:])]))
  a,v,acc=self.profile(s);bg=np.sqrt(1-v*v)
  return dict(config=self.cfg,initial_jets=list(self.profile(0.)),terminal_jets=list(self.profile(self.end)),up_time=self.S,inward_coast=self.L,meridian_length=self.end,maximum_radius=float(a.max()),background_height=float(np.trapezoid(bg,s)),background_kappa_sample=float(np.max(np.maximum(abs(acc)/bg,bg/a))),knots=self.knots.tolist())

def install(flow_class=None):
 if flow_class is None:
  from fixed_metric_mode3_flow import PlanarSymmetryFlow
  flow_class=PlanarSymmetryFlow
 if getattr(flow_class,'alternative_hermite_cycle_installed',False):return
 old_init=flow_class.__init__;old_prefix=flow_class.prefix_profile
 def init(self,cfg,*args,**kwargs):
  old_init(self,cfg,*args,**kwargs)
  if cfg.get('ramp_law')=='hermite_turn':
   law=HermiteTurnCycle(cfg);self._hermite_turn_law=law;self.Tu=law.S;self.Td=law.end-law.S;self.period=law.end;self.prefix_end=law.end;self.end=law.end+self.bridge.L;self.breakpoints=law.knots.copy();self.breaks=np.unique(np.r_[law.knots,self.end])
 def prefix(self,s):
  if self.cfg.get('ramp_law')=='hermite_turn':return self._hermite_turn_law.profile(s)
  return old_prefix(self,s)
 flow_class.__init__=init;flow_class.prefix_profile=prefix;flow_class.alternative_hermite_cycle_installed=True

class Search:
 def __init__(self,port,V=.35,S=.65,k0=.45,max_coast=.1):
  self.V=V;self.k0=k0;self.delta=V*S/2+k0*S*S/12;self.max_coast=max_coast;self.bridges={}
  for m in (2,4):
   cut,slope=scan.parse_port(port,m);self.bridges[m]=scan.Bridge(cut,m,slope)
  s=np.linspace(0,self.bridges[2].L,1001);a,v,acc=self.bridges[2].profile(s);self.bridge_height=float(np.trapezoid(np.sqrt(1-v*v),s));self.bridge_kappa=float(np.max(np.maximum(abs(acc)/np.sqrt(1-v*v),np.sqrt(1-v*v)/a)))
 def config(self,x):
  down,T,eta,C=map(float,x);area=self.delta+self.V*C+T*(self.V-down)/2
  return dict(direction='outward',cycles=1,ramp=.4,ramp_law='hermite_turn',delta=self.delta,vu=self.V,vd=down,start_acceleration=self.k0,turn_length=T,brake_length=2*eta*area/down,coast_outward=C)
 def residual(self,x,details=False):
  law=HermiteTurnCycle(self.config(x));y=np.r_[self.bridges[2].initial,self.bridges[4].initial];gains=np.ones(2)
  for l,r in reversed(list(zip(law.knots[:-1],law.knots[1:]))):
   def fun(s,y):
    a,v,acc=law.profile(s)
    return np.r_[scan.linear_matrix(a,v,2)@y[:2],scan.linear_matrix(a,v,4)@y[2:]]
   sol=solve_ivp(fun,(r,l),y,method='DOP853',rtol=2e-9,atol=2e-11,max_step=(r-l)/10)
   if not sol.success:raise RuntimeError(sol.message)
   y=sol.y[:,-1]
   for j in (0,1):
    norm=np.linalg.norm(y[2*j:2*j+2]);gains[j]*=norm;y[2*j:2*j+2]/=norm
  residual=np.array([y[1],y[3]])
  return (residual,law,y,gains)if details else residual
 def summary(self,x):
  res,law,y,gains=self.residual(x,True);data=law.summary();data.update(x=list(map(float,x)),residual=res.tolist(),residual_max=float(abs(res).max()),core_lines=dict(m2=y[:2].tolist(),m4=y[2:].tolist()),transport_norm_gains=gains.tolist(),total_background_height=data['background_height']+self.bridge_height,bridge_length=self.bridges[2].L,bridge_kappa_sample=self.bridge_kappa)
  return data
 def run(self,seeds=12):
  # Positive area is automatic for these bounds at the default fixed prefix.
  lo=np.array([.3,.16,.18,0.]);hi=np.array([.88,.44,.92,self.max_coast]);rng=np.random.default_rng(20261110);rows=[];attempts=[];begin=time.time()
  for index in range(seeds):
   x=lo+(hi-lo)*rng.uniform(.05,.95,4)
   try:
    z=least_squares(self.residual,x,bounds=(lo,hi),xtol=2e-9,ftol=2e-9,gtol=2e-9,max_nfev=130)
    row=self.summary(z.x);attempts.append(dict(seed=index,residual_max=row['residual_max'],x=row['x'],height=row['total_background_height'],kappa=row['background_kappa_sample']))
    if row['residual_max']<2e-6 and not any(np.linalg.norm(np.asarray(r['x'])-z.x)<1e-4 for r in rows):rows.append(row)
   except Exception as e:attempts.append(dict(seed=index,error=repr(e)))
  rows.sort(key=lambda r:r['total_background_height'])
  return dict(scope=__doc__,seconds=time.time()-begin,V=self.V,delta=self.delta,k0=self.k0,rows=rows,attempts=attempts)

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--V',type=float,default=.35);p.add_argument('--S',type=float,default=.65);p.add_argument('--k0',type=float,default=.45);p.add_argument('--max-coast',type=float,default=.1);p.add_argument('--seeds',type=int,default=12);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
 data=Search(json.loads(args.port.read_text()),args.V,args.S,args.k0,args.max_coast).run(args.seeds);data.update(script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),port_sha256=hashlib.sha256(args.port.read_bytes()).hexdigest());args.out.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(dict(seconds=data['seconds'],candidates=len(data['rows']),best=data['rows'][:3],attempts=data['attempts'])))
if __name__=='__main__':main()

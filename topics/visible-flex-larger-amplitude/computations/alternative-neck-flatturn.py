#!/usr/bin/env python3
"""Neck design with C2 flat-top angular-speed turns.

Extends the explicit C2 neck program in alternative-neck-excursion.py.
The angular speed ramps smoothly from zero to K, stays constant, and
returns smoothly to zero. No instantaneous angular or radial-slope turn
is used. All matching and attenuation claims remain linear design data.
"""
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_flat_neck_base',P/'alternative-neck-excursion.py');base=importlib.util.module_from_spec(sp);sp.loader.exec_module(base)
old_phase=base.phase

def ramp(u,eps):
 u=np.asarray(u);z=np.clip(np.minimum(u,1-u)/eps,0,1);w=3*z*z-2*z*z*z
 v=np.clip(u/eps,0,1);left=eps*(v**3-v**4/2)
 v=np.clip((1-u)/eps,0,1);right=1-eps-eps*(v**3-v**4/2)
 I=np.where(u<eps,left,np.where(u>1-eps,right,u-eps/2))
 return w,I

def phase(seg,u):
 if 'turn_ramp' not in seg:return old_phase(seg,u)
 return seg['p0']+(seg['p1']-seg['p0'])*ramp(u,seg['turn_ramp'])[1]/(1-seg['turn_ramp'])

def integral(seg,u,which='sin'):
 u=np.asarray(u);value=np.zeros_like(u,dtype=float);fn=np.sin if which=='sin' else np.cos
 cuts=[0.,1.]
 if 'turn_ramp'in seg:cuts=[0.,seg['turn_ramp'],1-seg['turn_ramp'],1.]
 for left,right in zip(cuts[:-1],cuts[1:]):
  width=np.clip(u-left,0,right-left);q=left+width[...,None]*base.gu
  value+=width/2*(fn(phase(seg,q))@base.gw)
 return value

def turn(p0,p1,K):
 eps=.08;L=abs(p1-p0)/(K*(1-eps));seg=dict(kind='turn',p0=p0,p1=p1,length=L,K=K,turn_ramp=eps)
 seg['dr']=L*float(integral(seg,1.));seg['dh']=L*float(integral(seg,1.,'cos'))
 u=np.linspace(0,1,301);rr=L*integral(seg,u);seg['dr_min']=float(rr.min());seg['dr_max']=float(rr.max());return seg

base.phase=phase;base.turn=turn

def program_summary(self):
 kmax=0.;bmin=1.
 for seg in self.segments:
  u=np.linspace(0,1,201);a=seg['a0']+seg['length']*integral(seg,u);pp=phase(seg,u)
  if 'turn_ramp'in seg:dp=np.sign(seg['p1']-seg['p0'])*seg['K']*ramp(u,seg['turn_ramp'])[0]
  elif seg['kind']=='brake':dp=2*(seg['p1']-seg['p0'])*u/seg['length']
  else:dp=np.zeros_like(u)
  kmax=max(kmax,float(np.max(np.maximum(abs(dp),np.cos(pp)/a))));bmin=min(bmin,float(np.cos(pp).min()))
 return dict(x=self.x,segments=self.segments,connector_length=self.end,connector_height=self.height,connector_minimum_radius=self.minimum_radius,connector_maximum_radius=self.maximum_radius,connector_background_kappa_sample=kmax,minimum_background_vertical_speed=bmin,terminal_radius=self.end_radius)
base.Program.summary=program_summary

class Search(base.Search):
 def residual(self,x,details=False):
  res,program,core,gains,H=super().residual(x,True)
  if details:return res,program,core,gains,H
  return np.r_[res,.06*math.log10(max(abs(.38*H[0]),1e-30)/5e-4),.15*max(0.,self.prefix_height+program.height-1.85)]
 def summary(self,x):
  res,program,core,gains,H=self.residual(x,True);r=program.summary();r.update(core_resonance=res.tolist(),resonance_max=float(abs(res).max()),full_core_amplification=gains.tolist(),unit_core_terminal_height=H.tolist(),terminal_height_at_core_A038=[.38*H[0],-.38/(10*math.sqrt(2))*H[1]],prefix_height=self.prefix_height,total_background_height=self.prefix_height+program.height)
  maxnorm=0.;pstart=0.
  for seg in program.segments:
   u=np.linspace(0,1,201);a=seg['a0']+seg['length']*integral(seg,u);h=self.prefix_height+seg['h0']+seg['length']*integral(seg,u,'cos');maxnorm=max(maxnorm,float(np.sqrt(a*a+h*h).max()))
   if seg['kind']=='turn' and seg['p0']<0<seg['p1']:pstart=self.prefix_height+seg['h0']
  r.update(connector_background_centered_D_sample=2*maxnorm,neck_reverse_begin_background_height=pstart)
  return r
 def run(self,seeds,out):
  lo=np.array([.2,.85,.85,0.,.05,4.]);hi=np.array([.4,.97,.97,.25,.93,8.]);rng=np.random.default_rng(20261110);rows=[];attempts=[];begin=time.time();report=dict(scope=__doc__,V=self.V,S=self.S,k0=self.k0,cut=self.cut,turn_ramp=.08,rows=rows,attempts=attempts)
  for index in range(seeds):
   x=lo+(hi-lo)*rng.uniform(.04,.96,6)
   try:
    z=least_squares(self.residual,x,bounds=(lo,hi),xtol=5e-9,ftol=5e-9,gtol=5e-9,max_nfev=130);r=self.summary(z.x);attempts.append(dict(seed=index,x=r['x'],resonance=r['resonance_max'],residual=r['core_resonance'],height=r['total_background_height'],H=r['terminal_height_at_core_A038'],D=r['connector_background_centered_D_sample']))
    if r['resonance_max']<2e-5 and abs(r['terminal_height_at_core_A038'][0])<6e-4 and not any(np.linalg.norm(np.array(row['x'])-z.x)<1e-4 for row in rows):rows.append(r);rows.sort(key=lambda rr:rr['total_background_height'])
    print(json.dumps(dict(event='seed',index=index,resonance=r['resonance_max'],height=r['total_background_height'],H=r['terminal_height_at_core_A038'],D=r['connector_background_centered_D_sample'])),flush=True)
   except Exception as e:attempts.append(dict(seed=index,error=repr(e)));print(json.dumps(dict(event='error',index=index,error=repr(e))),flush=True)
   report['seconds']=time.time()-begin;out.write_text(json.dumps(report,indent=2)+'\n')
  return report

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--V',type=float,default=.25);p.add_argument('--S',type=float,default=.65);p.add_argument('--k0',type=float,default=.45);p.add_argument('--seeds',type=int,default=8);p.add_argument('--out',type=Path,required=True);a=p.parse_args();report=Search(json.loads(a.port.read_text()),a.V,a.S,a.k0).run(a.seeds,a.out);report.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),base_source_sha256=hashlib.sha256((P/'alternative-neck-excursion.py').read_bytes()).hexdigest(),port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest());a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='complete',seconds=report['seconds'],candidates=len(report['rows']),best=report['rows'][:1])))
if __name__=='__main__':main()

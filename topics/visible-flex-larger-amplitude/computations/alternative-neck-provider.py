#!/usr/bin/env python3
"""BVP-ready C2 Hermite/late-boost/finite-neck metric and terminal bridge.

The two design controls retain their physical meanings: delta is the
initial Hermite radius increase, and vd is the speed of the inward leg
before a C2 transition to the fixed loop speed. The loop and terminal
bridge are finite. Linear roots are only seeds for a nonlinear BVP.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_provider_flatturn',P/'alternative-neck-flatturn.py');fl=importlib.util.module_from_spec(sp);sp.loader.exec_module(fl)
base=fl.base

def velocity(seg,u):
 if seg['kind']=='hermite':
  b=seg['k0']*seg['length'];V=seg['v1'];return b*u+(3*V-2*b)*u*u+(b-2*V)*u**3
 if seg['kind']=='boost':return seg['v0']+(seg['v1']-seg['v0'])*(3*u*u-2*u**3)
 return np.sin(fl.phase(seg,u))

def piece_jet(seg,u):
 u=np.asarray(u);L=seg['length']
 if seg['kind']=='hermite':
  b=seg['k0']*L;V=seg['v1'];c=3*V-2*b;d=b-2*V
  return seg['a0']+L*(b*u*u/2+c*u**3/3+d*u**4/4),b*u+c*u*u+d*u**3,(b+2*c*u+3*d*u*u)/L
 if seg['kind']=='boost':
  v=seg['v0'];dv=seg['v1']-v
  return seg['a0']+L*(v*u+dv*(u**3-u**4/2)),v+dv*(3*u*u-2*u**3),dv/L*6*u*(1-u)
 phi=fl.phase(seg,u)
 if 'turn_ramp'in seg:dp=np.sign(seg['p1']-seg['p0'])*seg['K']*fl.ramp(u,seg['turn_ramp'])[0]
 elif seg['kind']=='brake':dp=2*(seg['p1']-seg['p0'])*u/L
 else:dp=np.zeros_like(u)
 return seg['a0']+L*fl.integral(seg,u),np.sin(phi),np.cos(phi)*dp

class Pieces:
 def __init__(self,a0):self.segments=[];self.aend=float(a0);self.end=0.;self.height=0.
 def append(self,seg):
  if seg['length']<1e-14:return
  seg=dict(seg);seg.update(a0=self.aend,s0=self.end,h0=self.height)
  if seg['kind']in('hermite','boost'):
   aend=float(piece_jet(seg,1.)[0]);dh=seg['length']/2*float(np.dot(np.sqrt(1-velocity(seg,base.gu)**2),base.gw));seg.update(dr=aend-self.aend,dh=dh)
  self.aend+=seg['dr'];self.end+=seg['length'];self.height+=seg['dh'];seg.update(a1=self.aend,s1=self.end,h1=self.height);self.segments.append(seg)
 def coast(self,target,v):
  L=(target-self.aend)/v
  if L< -2e-11:raise ValueError('Negative provider coast')
  self.append(dict(kind='coast',length=max(0.,L),p0=math.asin(v),p1=math.asin(v),dr=target-self.aend,dh=max(0.,L)*math.sqrt(1-v*v),K=0.))
 def profile(self,s):
  scalar=np.ndim(s)==0;s=np.asarray(s,float);ss=s.ravel();out=[np.zeros(len(ss))for _ in range(3)]
  for j,seg in enumerate(self.segments):
   mask=(ss>=seg['s0']-1e-13)&((ss<seg['s1'])if j+1<len(self.segments)else(ss<=seg['s1']+1e-12))
   if np.any(mask):
    jet=piece_jet(seg,np.clip((ss[mask]-seg['s0'])/seg['length'],0.,1.))
    for z,w in zip(out,jet):z[mask]=w
  return tuple(float(z[0])for z in out)if scalar else tuple(z.reshape(s.shape)for z in out)
 def breaks(self):
  out=[0.,self.end]
  for seg in self.segments:
   out.extend([seg['s0'],seg['s1']])
   if 'turn_ramp'in seg:out.extend([seg['s0']+seg['length']*seg['turn_ramp'],seg['s0']+seg['length']*(1-seg['turn_ramp'])])
  return np.unique(out)
 def summary(self):
  rows=[]
  for seg in self.segments:
   u=np.linspace(0,1,101);a,v,acc=piece_jet(seg,u);b=np.sqrt(1-v*v)
   rows.append(dict(a_min=float(a.min()),a_max=float(a.max()),kappa=float(np.max(np.maximum(abs(acc)/b,b/a)))))
  return dict(length=self.end,background_height=self.height,minimum_radius=min(r['a_min']for r in rows),maximum_radius=max(r['a_max']for r in rows),background_kappa_sample=max(r['kappa']for r in rows),initial_jets=[float(np.ravel(z)[0])for z in self.profile(0.)],terminal_jets=[float(np.ravel(z)[0])for z in self.profile(self.end)],segments=self.segments)

class NeckPrefix(Pieces):
 def __init__(self,cfg):
  super().__init__(1.);self.cfg=dict(cfg);delta=float(cfg['delta']);V=float(cfg['vu']);vd=float(cfg['vd']);k0=float(cfg.get('start_acceleration',.45));vp=float(cfg.get('boost_speed',.65));LB=float(cfg.get('boost_length',.2));C=float(cfg.get('coast_outward',0.));r=float(cfg.get('loop_radius',.35));q=float(cfg.get('loop_ratio',2.2));vl=float(cfg.get('loop_speed',.985));K=float(cfg.get('loop_curvature',8.));Ks=float(cfg.get('descending_turn_curvature',4.5));Ksync=float(cfg.get('descending_sync_curvature',8.))
  if not(0<V<1 and 0<vd<1 and 0<vp<1 and 0<vl<1 and delta>0 and LB>0 and C>=0 and r>0 and q>1):raise ValueError('Invalid physical neck parameters')
  self.S=12*delta/(math.sqrt(9*V*V+12*k0*delta)+3*V)
  if k0*self.S>3*V:raise ValueError('Nonmonotone initial Hermite speed')
  self.append(dict(kind='hermite',length=self.S,k0=k0,v1=V));self.append(dict(kind='boost',length=LB,v0=V,v1=vp));self.coast(self.aend+vp*C,vp)
  self.append(fl.turn(math.asin(vp),-math.asin(vd),Ks))
  sync=fl.turn(-math.asin(vd),-math.asin(vl),Ksync)if abs(vd-vl)>1e-12 else None
  self.coast(r-(sync['dr']if sync else 0.),-vd)
  if sync:self.append(sync)
  self.loop_begin=self.end;self.append(fl.turn(-math.asin(vl),math.asin(vl),K));self.coast(q*r,vl);self.append(fl.turn(math.asin(vl),-math.asin(vl),K));self.coast(r,-vl)
  self.Tu=self.S;self.Td=self.end-self.S;self.period=self.end

class NeckTerminalBridge(Pieces):
 def __init__(self,cut):
  spec=cut['_prefix_bridge'];r=float(spec['radius']);v=float(spec['speed']);K=float(spec.get('curvature',8.));fraction=float(spec.get('peak_fraction',.1));super().__init__(r);self.cut=cut;self.sigma=-1.
  pt=-math.atan2(1.,cut['backgroundSlope']);ps=-cut['backgroundSecond']/(1+cut['backgroundSlope']**2)**1.5;gap=fraction*(math.pi/2+pt);peak=pt-gap
  self.append(fl.turn(-math.asin(v),peak,K));brake=dict(kind='brake',p0=peak,p1=pt,length=2*gap/ps,K=ps);brake['dr']=brake['length']*float(fl.integral(brake,1.));brake['dh']=brake['length']*float(fl.integral(brake,1.,'cos'))
  self.coast(cut['radius']-brake['dr'],math.sin(peak));self.append(brake);self.L=self.end;self.breakpoints=self.breaks();self.parameters=dict(spec)
 def profile(self,s):
  # Original bridge interface returns arrays even for a scalar input.
  return super().profile(np.atleast_1d(s))

def tagged_port(port,cfg):
 out=json.loads(json.dumps(port));out['cut']['_prefix_bridge']=dict(kind='finite_neck_terminal_v1',radius=float(cfg.get('loop_radius',.35)),speed=float(cfg.get('loop_speed',.985)),curvature=float(cfg.get('loop_curvature',8.)),peak_fraction=float(cfg.get('terminal_peak_fraction',.1)))
 return out

def install():
 """Install after the source loader and any root_short_bridge installation."""
 import f6curve_bidirectional_bridge as bm
 import fixed_metric_mode3_flow as fm
 if not hasattr(bm,'_alternative_neck_previous_factory'):bm._alternative_neck_previous_factory=bm.DirectionalBridge
 previous=bm._alternative_neck_previous_factory
 def factory(cut,a_start=1.):
  tag=cut.get('_prefix_bridge',{})
  if tag.get('kind')=='finite_neck_terminal_v1':return NeckTerminalBridge(cut)
  return previous(cut,a_start)
 bm.DirectionalBridge=factory;fm.DirectionalBridge=factory
 if getattr(fm.PlanarSymmetryFlow,'_alternative_neck_installed',False):return
 old_init=fm.PlanarSymmetryFlow.__init__;old_prefix=fm.PlanarSymmetryFlow.prefix_profile
 def init(self,cfg,*args,**kwargs):
  old_init(self,cfg,*args,**kwargs)
  if cfg.get('ramp_law')=='hermite_boost_neck':
   law=NeckPrefix(cfg);self._alternative_neck=law;self.Tu=law.Tu;self.Td=law.Td;self.period=law.end;self.prefix_end=law.end;self.end=law.end+self.bridge.L;self.breakpoints=law.breaks();self.breaks=np.unique(np.r_[self.breakpoints,self.prefix_end+self.bridge.breakpoints])
 def prefix(self,s):
  if self.cfg.get('ramp_law')=='hermite_boost_neck':return self._alternative_neck.profile(s)
  return old_prefix(self,s)
 fm.PlanarSymmetryFlow.__init__=init;fm.PlanarSymmetryFlow.prefix_profile=prefix;fm.PlanarSymmetryFlow._alternative_neck_installed=True

class LinearScreen:
 def __init__(self,port,cfg):
  self.cfg=dict(cfg);self.port=tagged_port(port,cfg);self.bridge=NeckTerminalBridge(self.port['cut']);self.terminal=[]
  for m in(2,4):
   r=port['cut']['radius'];w=port['cut']['backgroundSlope'];D=port['linearSlope'][port['modes'].index(m)];z=np.array([-w*(r*D-m*m)/(m*m-1),1.]);self.terminal.append(z/np.linalg.norm(z))
 def evaluate(self,x,details=False):
  cfg={**self.cfg,'delta':float(x[0]),'vd':float(x[1])};prefix=NeckPrefix(cfg);state=np.r_[self.port['cut']['radius'],self.terminal[0],self.terminal[1]];gains=np.ones(2)
  for seg in reversed(prefix.segments+self.bridge.segments):
   if seg['kind']=='coast':
    for j,m in enumerate((2,4)):state[1+2*j:3+2*j]=base.pl.constant_transfer(seg['a1'],seg['a0'],math.sin(seg['p0']),m)@state[1+2*j:3+2*j]
    state[0]=seg['a0']
   else:
    def rhs(u,y):
     v=float(velocity(seg,u));b=math.sqrt(1-v*v);a=y[0];f,g,F,G=y[1:]
     return seg['length']*np.array([v,(-3*v*f-4*b*g)/a,(3*v*v/b*f+4*v*g)/a,(-15*v*F-16*b*G)/a,(15*v*v/b*F+16*v*G)/a])
    sol=solve_ivp(rhs,(1.,0.),state,method='DOP853',rtol=2e-10,atol=2e-12,max_step=.04)
    if not sol.success:raise RuntimeError(sol.message)
    state=sol.y[:,-1]
   for j in range(2):
    sl=slice(1+2*j,3+2*j);norm=np.linalg.norm(state[sl]);state[sl]/=norm;gains[j]*=norm
  res=np.array([state[2],state[4]]);H=[self.terminal[j][1]/(gains[j]*state[1+2*j])for j in range(2)]
  if not details:return res
  return dict(profile=cfg,residual=res.tolist(),residual_max=float(abs(res).max()),full_core_amplification=gains.tolist(),unit_core_terminal_height=H,terminal_height_at_core_A038=[.38*H[0],-.38/(10*math.sqrt(2))*H[1]],prefix=prefix.summary(),bridge=self.bridge.summary(),total_background_height=prefix.height+self.bridge.height)

def default_cfg():
 return dict(direction='outward',cycles=1,ramp=.4,ramp_law='hermite_boost_neck',delta=.09709375,vu=.25,vd=.9,start_acceleration=.45,boost_speed=.65,boost_length=.2,coast_outward=0.,loop_radius=.35,loop_ratio=2.2,loop_speed=.985,loop_curvature=8.,descending_turn_curvature=4.5,descending_sync_curvature=8.,terminal_peak_fraction=.1)

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--profile',type=Path);p.add_argument('--out',type=Path,required=True);p.add_argument('--seeds',type=int,default=6);p.add_argument('--seed-only',action='store_true');a=p.parse_args();cfg=json.loads(a.profile.read_text())if a.profile else default_cfg();screen=LinearScreen(json.loads(a.port.read_text()),cfg);rows=[];attempts=[];report=dict(scope=__doc__,config=cfg,rows=rows,attempts=attempts);start=time.time()
 if a.seed_only:rows.append(screen.evaluate([cfg['delta'],cfg['vd']],True))
 else:
  seeds=[(cfg['delta'],cfg['vd']),(.07,.7),(.12,.6),(.16,.8),(.22,.4),(.04,.95)]
  for seed in seeds[:a.seeds]:
   try:
    z=least_squares(screen.evaluate,seed,bounds=([.025,.3],[.29,.965]),xtol=3e-10,ftol=3e-10,gtol=3e-10,max_nfev=100);r=screen.evaluate(z.x,True);attempts.append(dict(seed=seed,residual=r['residual'],x=z.x.tolist(),height=r['total_background_height'],H=r['terminal_height_at_core_A038']));
    if r['residual_max']<2e-6 and not any(np.linalg.norm(np.array([rr['profile']['delta'],rr['profile']['vd']])-z.x)<1e-5 for rr in rows):rows.append(r)
    print(json.dumps(attempts[-1]),flush=True)
   except Exception as e:attempts.append(dict(seed=seed,error=repr(e)));print(json.dumps(attempts[-1]),flush=True)
   report['seconds']=time.time()-start;a.out.write_text(json.dumps(report,indent=2)+'\n')
 report.update(seconds=time.time()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest());a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='complete',seconds=report['seconds'],roots=len(rows),best=[{k:r[k]for k in('profile','residual','total_background_height','terminal_height_at_core_A038')}for r in rows])))
# Optional local design extension. Profiles without boost_law='angle' keep
# the original cubic boost and all original arithmetic unchanged.
import importlib.util as _boost_importlib
_boost_spec=_boost_importlib.spec_from_file_location('strong_angle_boost_provider_hook',P/'strong_angle_boost.py')
_boost_hook=_boost_importlib.module_from_spec(_boost_spec);_boost_spec.loader.exec_module(_boost_hook)
_boost_hook.install_globals(globals())

if __name__=='__main__':main()

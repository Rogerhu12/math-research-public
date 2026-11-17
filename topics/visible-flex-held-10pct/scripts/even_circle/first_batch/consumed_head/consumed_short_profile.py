"""Explicit C2 meridian with a configurable negative-K head and short cut.

Only geometry and linear variational equations are provided. No nonlinear
isometric embedding or closed surface is asserted by this design module.
"""
import importlib.util,math
from pathlib import Path
import numpy as np

HEAD=None
SHORT=None
TURN=None

def configure(head_path,short_path):
 global HEAD,SHORT,TURN
 def mod(name,path):
  spec=importlib.util.spec_from_file_location(name,Path(path));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
 h=mod('n4_consumed_head',head_path);b=mod('n4_consumed_short',short_path)
 HEAD=h.ConsumedWindowProfile;TURN=h.turn;SHORT=b.ShortBridge

class ConsumedShortLoop:
 def __init__(self,cut,delta=.03,vu=.25,epsilon=.4,eta=.05,extra_speed=.6,extra_acceleration=2.,return_speed=.6,turn_acceleration=5.5,stop_acceleration=4.,bridge_radius=1.,bridge_curvature=4.,peak_fraction=.2):
  if HEAD is None:raise RuntimeError('Call configure with explicit immutable source paths first')
  self.parameters=dict(delta=delta,vu=vu,epsilon=epsilon,eta=eta,extra_speed=extra_speed,extra_acceleration=extra_acceleration,return_speed=return_speed,turn_acceleration=turn_acceleration,stop_acceleration=stop_acceleration,bridge_radius=bridge_radius,bridge_curvature=bridge_curvature,peak_fraction=peak_fraction)
  self.head=HEAD(delta=delta,vu=vu,epsilon=epsilon,eta=eta,extra_speed=extra_speed,extra_acceleration=extra_acceleration)
  self.bridge=SHORT(cut,a_start=bridge_radius,curvature=bridge_curvature,peak_fraction=peak_fraction)
  self.delta=delta;self.vu=vu;self.Tu=self.head.Tu;self.hold_end=self.head.hold_end;self.direction='outward';self.eta=eta;self.cut=cut
  self.v1=extra_speed;self.v2=-return_speed
  Lturn=(extra_speed+return_speed)/(turn_acceleration*(1-eta));Lstop=return_speed/(stop_acceleration*(1-eta))
  self.a_extra=self.head.a_extra;self.a_turn=self.a_extra+Lturn*(extra_speed-return_speed)/2
  self.a_stop=bridge_radius+Lstop*return_speed/2
  Lcoast=(self.a_turn-self.a_stop)/return_speed
  self.lengths=np.array([*self.head.lengths[:2],Lturn,Lcoast,Lstop,self.bridge.L])
  if min(self.lengths)<=0:raise ValueError('Nonpositive segment length')
  self.ends=np.r_[0.,np.cumsum(self.lengths)];self.end=float(self.ends[-1]);self.prefix_end=float(self.ends[5]);self.first_positive_K=float(self.ends[2])
  self.breaks=np.unique(np.r_[self.head.breaks[self.head.breaks<=self.head.ends[2]],self.ends,self.ends[2]+Lturn*np.array([eta,1-eta]),self.ends[4]+Lstop*np.array([eta,1-eta]),self.prefix_end+self.bridge.breakpoints]);self.breakpoints=self.breaks
 def profile(self,s):
  s=np.atleast_1d(s).astype(float);A=np.zeros_like(s);V=A.copy();K=A.copy();early=s<self.ends[2]
  if np.any(early):A[early],V[early],K[early]=self.head.profile(s[early])
  for j in range(2,6):
   mask=(s>=self.ends[j])&((s<self.ends[j+1])if j<5 else(s<=self.end+1e-12))
   if not np.any(mask):continue
   l=s[mask]-self.ends[j];L=self.lengths[j]
   if j in (2,4):
    a0=self.a_extra if j==2 else self.a_stop;v0=self.v1 if j==2 else self.v2;v1=self.v2 if j==2 else 0.
    F,P,d=TURN(l/L,self.eta);A[mask]=a0+v0*l+(v1-v0)*L*P;V[mask]=v0+(v1-v0)*F;K[mask]=(v1-v0)*d/L
   elif j==3:A[mask]=self.a_turn+self.v2*l;V[mask]=self.v2
   else:A[mask],V[mask],K[mask]=self.bridge.profile(l)
  return A,V,K

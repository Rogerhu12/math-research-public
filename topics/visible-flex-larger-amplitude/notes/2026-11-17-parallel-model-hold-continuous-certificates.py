#!/usr/bin/env python3
"""Finite continuous Gram/scaling certificates for the unchanged aa1 hold field.

The target scalar is transported from the exact .99 old jet to the exact
binary .995 cut. Its fall/hold/rise use exact binary durations and clamped
smoothstep primitives; stored rounded alpha/kappa are not new initial data.
Only the explicitly selected original cell or rational boundary piece is
covered. This is not a full-prefix, curvature, reach or closed-flex proof.
"""
import argparse,hashlib,importlib.util,math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

ENGINE_SHA='d0661f3d4de85ef7370fc1faaf370dd5b41aa58fa0476e67f42962ffd2f17882'
NODE_SHA='e6ddb8c54093b27b03984dac56f86c2864dac0d167c74f133600d50533427927'
HOLD_SHA='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'
INPUT_SHA='aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15'
PULSE_SHA='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 spec=importlib.util.spec_from_file_location(name,p);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

def hold_scalar(base):
 class Scalar(base):
  def __init__(self,oracle,data,panels):
   spec=data['hold_scalar_profile']
   fixed=dict(cut=.995,negative_curvature=-2.5,fall=.002,hold=.02,rise=.02,positive_curvature=1.5)
   if spec.get('kind')!='negative-curvature-hold-v1' or any(spec.get(k)!=v for k,v in fixed.items()):raise ValueError('Different hold scalar definition')
   if data['hold_profile_source_sha256']!=HOLD_SHA:raise ValueError('Wrong hold source in fixed field')
   proxy=dict(data);proxy['inward_scalar_profile']=spec
   # This frozen base initializer transports the original exact .99 jet.
   # It never reads stored alpha0, kappa0, shift, plateau or radius.
   super().__init__(oracle,proxy,panels)
   self.fall=Q.from_float(spec['fall']);self.hold=Q.from_float(spec['hold']);self.rise=Q.from_float(spec['rise'])
   self.kn=Q.from_float(spec['negative_curvature']);self.kp=Q.from_float(spec['positive_curvature'])
   if self.fall<Q(1,500)or self.rise<Q(1,50):raise ValueError('Derivative budgets require declared durations')
   self.fall_end=self.cut+self.fall;self.hold_end=self.fall_end+self.hold;self.rise_end=self.hold_end+self.rise
  def interval_kind(self,left,right):
   if self.origin<=left<right<=self.cut:return 'analytic_turn_Taylor',10
   if self.cut<=left<right<=self.fall_end:return 'hold_fall_exact_integral_Taylor',7100000
   if self.fall_end<=left<right<=self.hold_end:return 'hold_constant_exact_integral_Taylor',16
   if self.hold_end<=left<right<=self.rise_end:return 'hold_rise_exact_integral_Taylor',63000
   raise ValueError('A representative piece crosses an exact scalar boundary')
  def at(self,s):
   if s<=self.cut:return super().at(s)
   o=self.o;h=self.h;t=s-self.cut
   if not 0<=t<=self.fall+self.hold+self.rise:raise ValueError('Outside the declared first three hold segments')
   delta=o.subtract(h.interval(self.kn),self.K)
   def angle(z):
    drop=h.add(h.scale(self.K,z),h.scale(delta,self.fall*self.P(z/self.fall)))
    drop=h.add(drop,h.interval((self.kp-self.kn)*self.rise*self.P((z-self.fall-self.hold)/self.rise)))
    v=o.subtract(self.angle,drop)
    if not -h.S<v[0]<=v[1]<h.S:raise ValueError('Angle escaped certified sine/cosine domain')
    return v
   total=(0,0);error=Q(0)
   # |kappa|<=2.5.  S'<=15/8 and |S''|<=10*sqrt(3)/3<6.
   # Fall: |k'|<4362.1875, |k''|<6979500.
   # Rise: |k'|<=375, |k''|<=60000.
   # Thus |(sin alpha)''|<4370 (fall), <382 (rise).
   for left,right,m2 in ((Q(0),min(t,self.fall),4370),(self.fall+self.hold,t,382)):
    if right<=left:continue
    width=right-left;summation=(0,0)
    for j in range(self.panels):
     z=left+width*Q(2*j+1,2*self.panels)
     summation=h.add(summation,h.sine_cosine(angle(z))[0])
    err=width**3*m2/(24*self.panels**2)
    total=h.add(total,h.add(h.scale(summation,width/self.panels),o.box(-err,err)))
    error+=err
   end=min(t,self.fall+self.hold)
   if end>self.fall:
    # For constant kappa=kn, integral sin(alpha)=cos(alpha)/kn.
    diff=o.subtract(h.sine_cosine(angle(end))[1],h.sine_cosine(angle(self.fall))[1])
    total=h.add(total,h.scale(diff,1/self.kn))
   radius=h.add(self.ac,total);sn,cs=h.sine_cosine(angle(t))
   kap=h.add(self.K,h.scale(delta,self.S(t/self.fall)))
   kap=h.add(kap,h.interval((self.kp-self.kn)*self.S((t-self.fall-self.hold)/self.rise)))
   kapp=h.add(h.scale(delta,self.Sd(t/self.fall)/self.fall),h.interval((self.kp-self.kn)*self.Sd((t-self.fall-self.hold)/self.rise)/self.rise))
   acc=h.neg(h.multiply(kap,cs))
   third=h.neg(h.add(h.multiply(kapp,cs),h.multiply(h.multiply(kap,kap),sn)))
   def binary(v):
    left,right=Q(v[0],h.S),Q(v[1],h.S)
    lo=np.nextafter(float(left),-np.inf);hi=np.nextafter(float(right),np.inf)
    if not Q.from_float(float(lo))<=left<=right<=Q.from_float(float(hi)):raise ValueError('Scalar conversion not outward')
    return lo,hi
   error_float=0. if error==0 else float(np.nextafter(float(error),np.inf))
   if Q.from_float(error_float)<error:raise ValueError('Midpoint error not outward')
   return [binary(v)for v in (radius,sn,acc,third)],error_float,0
 return Scalar

PARTITION=r'''
 original_left=Q.from_float(float(x[i]));original_right=Q.from_float(float(x[i+1]));left=original_left;right=original_right
 spec=data['hold_scalar_profile'];cut=Q.from_float(spec['cut'])
 fall=Q.from_float(spec['fall']);hold=Q.from_float(spec['hold']);rise=Q.from_float(spec['rise'])
 boundaries=[Q.from_float(data['analytic_extension_origin']),cut,cut+fall,cut+fall+hold,cut+fall+hold+rise]
 cuts=[left]+[v for v in boundaries if left<v<right]+[right]
 if len(cuts)>2:
  if a.piece is None or not 0<=a.piece<len(cuts)-1:raise ValueError('Select one exact boundary piece: '+str(cuts))
  left,right=cuts[a.piece:a.piece+2];a.part='piece-'+str(a.piece)
 else:
  if a.piece not in (None,0):raise ValueError('No such representative piece')
  a.part='all'
'''

def main(a):
 for path,expected in ((a.engine,ENGINE_SHA),(a.node_kernel,NODE_SHA),(a.hold_source,HOLD_SHA)):
  if sha(path)!=expected:raise ValueError('Frozen certificate dependency changed: '+str(path))
 base=load(a.engine,'hold_frozen_scalar_preparation');nodes=load(a.node_kernel,'hold_frozen_node_kernel')
 text=a.engine.read_text()
 if a.mode=='nodes':
  cut=' F,T=jet(co);V,_=jet(pder(co));G=pdot(T,T);Mix=pdot(V,T);E=pdot(V,V)'
  if text.count(cut)!=1:raise ValueError('Missing fixed preparation endpoint')
  text=text[:text.index(cut)]+nodes.NODE_TAIL
 def replace(old,new):
  nonlocal text
  if text.count(old)!=1:raise ValueError('Expected unique preparation anchor: '+old[:70])
  text=text.replace(old,new)
 replace(PULSE_SHA,INPUT_SHA)
 first=text.index('"""');last=text.index('"""',first+3)+3;text=text[:first]+repr(__doc__)+text[last:]
 start=text.index('class Scalar:');end=text.index('def main(a):',start);text=text[:start]+'Scalar=HoldScalar\n\n'+text[end:]
 start=text.index(' original_left=Q.from_float(');end=text.index(' hq=right-left;mid=',start);text=text[:start]+PARTITION+text[end:]
 start=text.index("  if scalar.width<Q(1,200)");end=text.index('  for j in range(4):',start)
 text=text[:start]+"  scalar_kind,a4bound=scalar.interval_kind(left,right)\n  jets,miderr,_=scalar.at(mid);ac=[]\n"+text[end:]
 replace('exact_pulse_midpoint=str(boundary)','exact_hold_boundaries=[str(v)for v in boundaries]')
 anchor=" for p,s in dependency_hashes.items():"
 replace(anchor," dependency_hashes.update({a.engine:ENGINE_SHA,a.node_kernel:NODE_SHA,a.hold_source:HOLD_SHA})\n"+anchor)
 if a.mode=='nodes':
  replace('Qn<=N or Qn&(Qn-1)','Qn!=N or Qn&(Qn-1)')
  start=text.index('  F=[tr.cosine_sine(');end=text.index('\n',start)+1;text=text[:start]+text[end:]
  replace('  return F,t','  return t')
  start=text.index(' rho1=float(I.sum_upper(');end=text.index(' # Exact old quintic, or cubic Taylor',start)
  text=text[:start]+" rho_min=float(rho[0].min());rho_max=float(rho[1].max())\n if rho_min<=0:raise ValueError('Construction-node density not positive')\n rho_sq=I.square(rho)\n"+text[end:]
 replace(' a.out.write_text(json.dumps(report,indent=2)'," report.update(hold_profile_source_sha256=HOLD_SHA,representative_engine_sha256=ENGINE_SHA,node_kernel_source_sha256=NODE_SHA,generated_hold_kernel_sha256=GENERATED_SHA,mode=a.mode)\n a.out.write_text(json.dumps(report,indent=2)")
 generated_sha=hashlib.sha256(text.encode()).hexdigest()
 namespace=dict(__name__='hold_continuous_certificate_kernel',__file__=__file__,HoldScalar=hold_scalar(base.Scalar),ENGINE_SHA=ENGINE_SHA,NODE_SHA=NODE_SHA,HOLD_SHA=HOLD_SHA,GENERATED_SHA=generated_sha,REFERENCE_SHA=nodes.REFERENCE_SHA)
 a.angles=16384 if a.mode=='gram'else 4096;a.scalar_panels=4096;a.reference=None
 exec(compile(text,str(a.engine)+'::same-exact-hold-scalar-and-boundary-pieces','exec'),namespace)
 namespace['main'](a)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('input','engine','node-kernel','hold-source','interval-source','scalar-oracle','out'):p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--cell',type=int,required=True);p.add_argument('--piece',type=int);p.add_argument('--mode',choices=['gram','nodes'],required=True)
 main(p.parse_args())

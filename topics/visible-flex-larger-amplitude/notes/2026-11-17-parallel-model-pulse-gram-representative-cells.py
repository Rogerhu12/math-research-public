#!/usr/bin/env python3
"""A specified unchanged pulse-field cell or exact subcell, continuous Gram bound.

Old scalar pieces are exact rational quintics. Analytic and pulse pieces use
the original exact-integral scalar. No new field/metric or unrestricted scan.
"""
import argparse,gzip,hashlib,importlib.util,json,math,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

class Scalar:
 """The same exact integral scalar, transported from its .99 origin."""
 def __init__(self,oracle,data,panels):
  self.o=oracle;self.h=oracle.h;self.panels=panels;h=self.h
  self.origin=Q.from_float(float(data['analytic_extension_origin']))
  self.cut=Q.from_float(float(data['inward_scalar_profile']['cut']))
  self.width=Q.from_float(.005);self.ramp=Q.from_float(.02);self.A=Q(-5);self.k1=Q(3,2)
  a0=oracle.box('1.16660641061202','1.16660641061204')
  v0=oracle.box('.35794863891029','.35794863891032')
  u0=oracle.box('-2.01012061072760','-2.01012061072757')
  node=data['fixed_scalar_profile']['geometry']['knots'][-1]
  if self.origin!=Q.from_float(float(node['s'])):raise ValueError('Wrong analytic origin')
  for b,k in ((a0,'a'),(v0,'ap'),(u0,'app')):
   if not oracle.contains(b,Q.from_float(float(node[k]))):raise ValueError('Original scalar jet box missed its node')
  self.K=oracle.divide(h.neg(u0),oracle.square_root(oracle.subtract(h.interval(Q(1)),h.multiply(v0,v0))))
  angle0=oracle.arcsine(v0);self.a0=a0;self.angle_origin=angle0;self.angle=oracle.subtract(angle0,h.scale(self.K,self.cut-self.origin))
  self.ac=h.add(a0,oracle.divide(oracle.subtract(h.sine_cosine(self.angle)[1],h.sine_cosine(angle0)[1]),self.K))
 @staticmethod
 def P(u):return Q(0)if u<=0 else u-Q(1,2)if u>=1 else Q(5,2)*u**4-3*u**5+u**6
 @staticmethod
 def S(u):return Q(0)if u<=0 else Q(1)if u>=1 else 10*u**3-15*u**4+6*u**5
 @staticmethod
 def Sd(u):return Q(0)if u<=0 or u>=1 else 30*u*u*(1-u)*(1-u)
 def at(self,s):
  o=self.o;h=self.h;t=s-self.cut
  def binary(v):
   l,r=Q(v[0],h.S),Q(v[1],h.S);lo=np.nextafter(float(l),-np.inf);hi=np.nextafter(float(r),np.inf)
   assert Q.from_float(float(lo))<=l and Q.from_float(float(hi))>=r
   return lo,hi
  if self.origin<=s<=self.cut:
   angle=o.subtract(self.angle_origin,h.scale(self.K,s-self.origin));sn,cs=h.sine_cosine(angle)
   rad=h.add(self.a0,o.divide(o.subtract(cs,h.sine_cosine(self.angle_origin)[1]),self.K))
   return [binary(rad),binary(sn),binary(h.neg(h.multiply(self.K,cs))),binary(h.neg(h.multiply(h.multiply(self.K,self.K),sn)))],0.,10
  if not 0<=t<=2*self.width:raise ValueError('Only analytic turn and compact-pulse support covered')
  def angle(z):
   drop=h.add(h.scale(self.K,z),h.scale(o.subtract(h.interval(self.k1),self.K),self.ramp*self.P(z/self.ramp)))
   drop=h.add(drop,h.interval(self.A*self.width*(self.P(z/self.width)-self.P(z/self.width-1))))
   out=o.subtract(self.angle,drop)
   if not -h.S<out[0]<=out[1]<h.S:raise ValueError('Trigonometric domain not certified')
   return out
  total=(0,0)
  for j in range(self.panels):total=h.add(total,h.sine_cosine(angle(t*Q(2*j+1,2*self.panels)))[0])
  # The base curvature is in [1.5,K] and the clamped pulse difference is
  # in [0,1]; hence |kappa|<=3.5 and |kappa'|<1936.21875 on both halves.
  # The two pulse derivative supports are disjoint. Thus |(sin alpha)''|<2000.
  error=t**3*2000/(24*self.panels**2)
  radius=h.add(self.ac,h.add(h.scale(total,t/self.panels),o.box(-error,error)))
  sn,cs=h.sine_cosine(angle(t))
  kap=h.add(self.K,h.scale(o.subtract(h.interval(self.k1),self.K),self.S(t/self.ramp)))
  kap=h.add(kap,h.interval(self.A*(self.S(t/self.width)-self.S(t/self.width-1))))
  acc=h.neg(h.multiply(kap,cs))
  kapp=h.add(h.scale(o.subtract(h.interval(self.k1),self.K),self.Sd(t/self.ramp)/self.ramp),h.interval(self.A*(self.Sd(t/self.width)-self.Sd(t/self.width-1))/self.width))
  appp=h.neg(h.add(h.multiply(kapp,cs),h.multiply(h.multiply(kap,kap),sn)))
  return [binary(radius),binary(sn),binary(acc),binary(appp)],float(error),1300000

def main(a):
 start=time.perf_counter();source_sha=sha(__file__);raw=a.input.read_bytes();data=json.loads(gzip.decompress(raw))
 expected='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
 if hashlib.sha256(raw).hexdigest()!=expected:raise ValueError('Fixed complete pulse field required')
 dependency_hashes={a.interval_source:'f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d',a.scalar_oracle:'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'}
 for p,s in dependency_hashes.items():
  if sha(p)!=s:raise ValueError('Frozen dependency changed: '+str(p))
 I=load(a.interval_source,'fixed_interval_cancellation');O=load(a.scalar_oracle,'fixed_scalar_cancellation')
 np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
 M=data['M'];N=4096;Qn=a.angles;i=a.cell
 if M!=320 or Qn<=N or Qn&(Qn-1)or a.scalar_panels<1:raise ValueError('Wrong finite prototype parameters')
 tr=I.Transform(Qn);x=np.asarray(data['mesh'],dtype=float);Y=np.asarray(data['states'],dtype=float);Vn=np.asarray(data['rhs'],dtype=float);DD=np.asarray(data['d2'],dtype=float)
 if not 0<=i<len(x)-1 or not np.all(np.isfinite(x))or not np.all(np.diff(x)>0):raise ValueError('Invalid mesh')
 if any(z.shape!=(len(x),3*M+2)or not np.all(np.isfinite(z))for z in (Y,Vn,DD)):raise ValueError('Invalid jets')
 original_left=Q.from_float(float(x[i]));original_right=Q.from_float(float(x[i+1]));left=original_left;right=original_right
 boundary=Q.from_float(float(data['inward_scalar_profile']['cut']))+Q.from_float(.005)
 if a.part!='all':
  if not left<boundary<right:raise ValueError('Cell does not straddle the exact pulse midpoint')
  if a.part=='before':right=boundary
  else:left=boundary
 elif left<boundary<right:raise ValueError('Use explicit before/after covers for this exact scalar knot')
 hq=right-left;mid=(right+left)/2;parent_h=I.sub(I.exact(x[i+1]),I.exact(x[i]));co=I.cell_coeff(Y[i],Y[i+1],Vn[i],Vn[i+1],DD[i],DD[i+1],parent_h)
 def frac(v):
  lo=I.down(float(v));hi=I.up(float(v));assert Q.from_float(float(lo))<=v<=Q.from_float(float(hi));return lo,hi
 h=frac(hq)
 if a.part!='all':
  shift=frac((left-original_left)/(original_right-original_left));dilation=frac(hq/(original_right-original_left));new=[]
  for k in range(6):
   z=I.exact(np.zeros(3*M+2))
   for j in range(k,6):
    power=I.exact(1.)
    for _ in range(j-k):power=I.mul(power,shift)
    z=I.add(z,I.scale(I.mul(I.at(co,j),power),math.comb(j,k)))
   for _ in range(k):z=I.mul(z,dilation)
   new.append(z)
  co=I.stack(new)
 def uadd(*xs):return float(I.sum_upper(np.array(xs,dtype=float)))
 def umul(x,y):return float(I.mul(I.exact(x),I.exact(y))[1])
 def udiv(x,y):return float(I.div(I.exact(x),I.exact(y))[1])
 def usqrt(x):return float(I.sqrt(I.exact(x))[1])
 def ladd(x,y):return float(I.add(I.exact(x),I.exact(y))[0])
 def lmul(x,y):return float(I.mul(I.exact(x),I.exact(y))[0])
 def lowdiff(x,y):return float(I.sub(I.exact(x),I.exact(y))[0])
 def upower(x,n):
  out=1.
  for _ in range(n):out=umul(out,x)
  return out
 def lpower(x,n):
  out=1.
  for _ in range(n):out=lmul(out,x)
  return out
 def padd(v,w,sign=1):
  length=max(len(v[0]),len(w[0]));shape=np.broadcast_shapes(v[0].shape[1:],w[0].shape[1:]);out=(np.zeros((length,)+shape),np.zeros((length,)+shape))
  for j in range(length):
   z=I.exact(np.zeros(shape))
   if j<len(v[0]):z=I.add(z,I.at(v,j))
   if j<len(w[0]):z=I.add(z,I.scale(I.at(w,j),sign))
   out[0][j]=z[0];out[1][j]=z[1]
  return out
 def pmul(v,w):
  shape=np.broadcast_shapes(v[0].shape[1:],w[0].shape[1:]);out=I.exact(np.zeros((len(v[0])+len(w[0])-1,)+shape));out=(out[0].copy(),out[1].copy())
  for j in range(len(v[0])):
   for k in range(len(w[0])):
    z=I.add(I.at(out,j+k),I.mul(I.at(v,j),I.at(w,k)));out[0][j+k]=z[0];out[1][j+k]=z[1]
  return out
 def pder(v):return I.div(I.scale(I.at(v,slice(1,None)),np.arange(1,len(v[0])).reshape((-1,)+(1,)*(v[0].ndim-1))),h)
 def bern(v):
  n=len(v[0])-1;out=[]
  for j in range(n+1):
   z=I.exact(np.zeros(v[0].shape[1:]))
   for k in range(j+1):z=I.add(z,I.div(I.scale(I.at(v,k),math.comb(j,k)),I.exact(math.comb(n,k))))
   out.append(z)
  return I.stack(out)
 def pbound(v):return float(I.absolute_upper(bern(v)).max())
 def pmean(v):return I.scale((-I.sum_upper(-v[0]),I.sum_upper(v[1])),1/N)
 def prepend(v,z):return np.concatenate([z[0][...,None],v[0]],axis=-1),np.concatenate([z[1][...,None],v[1]],axis=-1)
 nu=2*np.arange(1,M+1)
 def jet(v):
  R=I.at(v,(...,slice(1,M+1)));T=I.at(v,(...,slice(M+1,2*M+1)));Z=I.at(v,(...,slice(2*M+2,None)))
  z=I.exact(np.zeros(v[0].shape[:-1]));r0=I.at(v,(...,0));z0=I.at(v,(...,2*M+1))
  F=[tr.cosine_sine(prepend(R,r0),Qn,'cos'),tr.cosine_sine(prepend(T,z),Qn,'sin'),tr.cosine_sine(prepend(Z,z0),Qn,'cos')]
  t=[tr.cosine_sine(prepend(I.neg(I.add(I.scale(R,nu),T)),z),Qn,'sin'),tr.cosine_sine(prepend(I.add(R,I.scale(T,nu)),r0),Qn,'cos'),tr.cosine_sine(prepend(I.neg(I.scale(Z,nu)),z),Qn,'sin')]
  return F,t
 def pdot(v,w):
  out=pmul(v[0],w[0])
  for j in range(1,3):out=padd(out,pmul(v[j],w[j]))
  return out
 def even_interpolant(v,primitive=False):
  hat,_=tr.fft(v,I.exact(np.zeros(v[0].shape)),sign=-1);hat=I.scale(hat,1/N)
  shape=v[0].shape[:-1]+(Qn,);rl=np.zeros(shape);rh=np.zeros(shape);il=np.zeros(shape);ih=np.zeros(shape)
  k=np.arange(2,N//2,2);cc=I.at(hat,(...,k));ny=I.scale(I.at(hat,(...,N//2)),.5)
  if primitive:
   cc=I.div(cc,I.exact(k));ny=I.div(ny,I.exact(N//2))
   il[...,k]=-cc[1];ih[...,k]=-cc[0];il[...,-k]=cc[0];ih[...,-k]=cc[1]
   il[...,N//2]=-ny[1];ih[...,N//2]=-ny[0];il[...,-N//2]=ny[0];ih[...,-N//2]=ny[1]
  else:
   rl[...,0]=hat[0][...,0];rh[...,0]=hat[1][...,0]
   rl[...,k]=rl[...,-k]=cc[0];rh[...,k]=rh[...,-k]=cc[1]
   rl[...,N//2]=rl[...,-N//2]=ny[0];rh[...,N//2]=rh[...,-N//2]=ny[1]
  return tr.fft((rl,rh),(il,ih))[0]
 def angular_d2(v,parity,K):
  rh,ih=tr.fft(v,I.exact(np.zeros(v[0].shape)),sign=-1);cc=I.scale(rh if parity=='even' else ih,1/Qn);k=np.arange(2,K+1,2)
  return float(np.max(I.up(2*I.sum_upper(I.up((k*k)*I.absolute_upper(I.at(cc,(...,k))))))))
 core=np.asarray(data.get('original_core_coefficients',Y[0,1:M+1]),dtype=float)
 if core.shape!=(M,)or not np.all(np.isfinite(core)):raise ValueError('Invalid full core density')
 amp=I.scale(I.exact(core),1-nu*nu);rho=tr.cosine_sine(prepend(amp,I.exact(1.)),Qn,'cos')
 rho1=float(I.sum_upper(I.up(nu*I.absolute_upper(amp))));rho2=float(I.sum_upper(I.up((nu*nu)*I.absolute_upper(amp))))
 angstep=udiv(tr.pi_upper,Qn);rho_min=lowdiff(float(rho[0].min()),umul(angstep,rho1));rho_max=uadd(float(rho[1].max()),umul(angstep,rho1))
 if rho_min<=0:raise ValueError('Density not certified positive')
 rho_sq=I.square(rho);rho_sq_d2=angular_d2((rho_sq[0][None,:],rho_sq[1][None,:]),'even',4*M)
 fee=udiv(upower(tr.pi_upper,2),2*Qn*Qn)
 cover_stats={}
 def cover(v,name,parity,K,denom=0):
  b=bern(v)
  den=I.exact(1.)if denom==0 else rho if denom==1 else rho_sq
  grid=float(I.div(I.exact(I.absolute_upper(b)),den)[1].max())
  d2_fft=angular_d2(b,parity,K)
  # For a real trigonometric polynomial of degree K, Bernstein gives
  # ||p''||_infinity <= K^2 ||p||_infinity. At an absolute extremum p'=0;
  # a nearest Q-grid point is at distance <=pi/Q. Hence its sup norm is
  # at most max_grid|p|/(1-pi^2 K^2/(2 Q^2)). This avoids amplifying
  # independent FFT interval widths by a sum of all squared frequencies.
  grid_absolute=float(I.absolute_upper(b).max());sampling_discount=lowdiff(1.,umul(fee,K*K))
  if sampling_discount<=0:raise ValueError('Insufficient oversampling for Bernstein cover')
  d2_bernstein=umul(K*K,udiv(grid_absolute,sampling_discount));d2=min(d2_fft,d2_bernstein)
  den2=0. if denom==0 else rho2 if denom==1 else rho_sq_d2
  denmin=1. if denom==0 else rho_min if denom==1 else float(I.square(I.exact(rho_min))[0])
  discount=lowdiff(1.,udiv(umul(fee,den2),denmin))
  if discount<=0:raise ValueError('Angular grid too coarse for weighted cover')
  bound=udiv(uadd(grid,udiv(umul(fee,d2),denmin)),discount)
  cover_stats[name]=dict(grid_upper=grid,grid_absolute_upper=grid_absolute,d2_upper=d2,d2_fft_upper=d2_fft,d2_bernstein_upper=d2_bernstein,all_radius_all_angle_upper=bound,degree=len(v[0])-1,frequency=K,denominator_power=denom)
  return bound
 # Exact old quintic, or cubic Taylor of the SAME exact analytic/pulse scalar.
 origin=Q.from_float(float(data['analytic_extension_origin']));scalar_knot=None
 if right<=origin:
  geom=data['fixed_scalar_profile']['geometry'];knots=geom['knots'];sx=[Q.from_float(float(k['s']))for k in knots]
  js=[j for j in range(len(sx)-1)if sx[j]<=left and right<=sx[j+1]]
  if len(js)!=1:raise ValueError('Split the field cell at its exact scalar knots first')
  scalar_knot=js[0];j=scalar_knot;hj=sx[j+1]-sx[j]
  tj=[tuple(Q.from_float(float(k[v]))for v in ('a','ap','app'))for k in knots]
  law=geom['initial_law'];length,velocity,k0=(Q.from_float(float(law[k]))for k in ('length','velocity','k0'))
  uu=sx[0]/length;bb=k0*length;cc=3*velocity-2*bb;dd=bb-2*velocity
  tj[0]=(1+length*(bb*uu*uu/2+cc*uu**3/3+dd*uu**4/4),bb*uu+cc*uu*uu+dd*uu**3,(bb+2*cc*uu+3*dd*uu*uu)/length)
  c0,c1,c2=tj[j][0],hj*tj[j][1],hj*hj*tj[j][2]/2
  aa=tj[j+1][0]-c0-c1-c2;bb=hj*tj[j+1][1]-c1-2*c2;cc=hj*hj*tj[j+1][2]-2*c2
  c=[c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2]
  shift=(left-sx[j])/hj;dilation=hq/hj;ac=[]
  for k in range(6):
   value=dilation**k*sum((c[jj]*math.comb(jj,k)*shift**(jj-k)for jj in range(k,6)),Q(0));z=frac(value);ac.append((np.asarray(z[0])[None],np.asarray(z[1])[None]))
  A=I.stack(ac);ea=0.;eap=0.;miderr=0.;a4bound=0;scalar_kind='exact_rational_old_quintic'
 else:
  scalar=Scalar(O,data,a.scalar_panels);hh=O.h
  if not (Q(3,2)<Q(scalar.K[0],hh.S) and Q(scalar.K[1],hh.S)<Q(2153,1000)):raise ValueError('Curvature bound assumption failed')
  if scalar.width<Q(1,200)or scalar.ramp<Q(1,50):raise ValueError('Derivative budgets failed')
  if origin<=left and right<=scalar.cut:scalar_kind='analytic_turn_Taylor'
  elif scalar.cut<=left and right<=scalar.cut+2*scalar.width:scalar_kind='clamped_pulse_Taylor'
  else:raise ValueError('Split at an exact scalar formula boundary first')
  jets,miderr,a4bound=scalar.at(mid);ac=[]
  for j in range(4):
   z=I.exact(0.)
   for k in range(j,4):
    hp=I.exact(1.)
    for _ in range(k):hp=I.mul(hp,h)
    term=I.div(I.mul(jets[k],hp),I.exact(math.factorial(k)));term=I.scale(term,math.comb(k,j)*(-.5)**(k-j));z=I.add(z,term)
   ac.append((np.asarray(z[0])[None],np.asarray(z[1])[None]))
  A=I.stack(ac);eaQ=Q(a4bound)*(hq/2)**4/24;eapQ=Q(a4bound)*(hq/2)**3/6
  ea=float(I.up(float(eaQ)));eap=float(I.up(float(eapQ)));assert Q.from_float(ea)>=eaQ and Q.from_float(eap)>=eapQ
 Ap=pder(A);Ab=bern(A);Amin=float(Ab[0].min());Amax=float(Ab[1].max());Apmax=pbound(Ap)
 if Amin<=ea:raise ValueError('Scalar radius lost positivity')
 F,T=jet(co);V,_=jet(pder(co));G=pdot(T,T);Mix=pdot(V,T);E=pdot(V,V)
 E[0][0]=I.down(E[0][0]-1);E[1][0]=I.up(E[1][0]-1)
 AA=pmul(A,A);DG=padd(G,I.mul(AA,rho_sq),-1);RG=padd(pmul(A,pder(G)),I.scale(pmul(Ap,G),2),-1)
 d=I.div(I.at(DG,(slice(None),slice(None,None,Qn//N))),I.at(rho,slice(None,None,Qn//N)))
 r=I.div(I.at(RG,(slice(None),slice(None,None,Qn//N))),I.at(rho,slice(None,None,Qn//N)))
 dn=even_interpolant(d);J=even_interpolant(r,True);Jd=even_interpolant(d,True)
 Pf=padd(I.scale(pmul(A,Mix),2),I.mul(J,rho),-1);Pg=padd(I.mul(dn,rho),DG,-1)
 En=cover(E,'E','even',4*M);Dn=cover(DG,'D_over_rho2','even',4*M,2);Rn=cover(RG,'R_over_rho','even',4*M,1)
 Mn=cover(Mix,'M_over_rho','odd',4*M,1);dnn=cover(dn,'dN_over_rho','even',N//2,1)
 Jn=cover(J,'J','odd',N//2);Jdn=cover(Jd,'Jd','odd',N//2)
 Pfn=cover(Pf,'Pf_over_rho','odd',N//2+2*M,1);Pgn=cover(Pg,'Pg_over_rho2','even',N//2+2*M,2)
 mD=pbound(pmean(d));mR=pbound(pmean(r));U=udiv(Dn,lpower(Amin,2))
 if U>=1:raise ValueError('Square root expansion not valid')
 oneU=lowdiff(1.,U);sqrtUlo=float(I.sqrt(I.exact(oneU))[0]);eq=udiv(umul(umul(Amax,rho_max),upower(U,2)),lmul(8.,lmul(oneU,sqrtUlo)))
 en=umul(usqrt(N),eq);bA=uadd(udiv(mD,2*Amin),eq);bmin=lowdiff(Amin,bA)
 if bmin<=0:raise ValueError('Mean speed not positive')
 ld=udiv(uadd(ea,bA),bmin);lm=uadd(1.,ld)
 C0=udiv(Rn,lmul(2.,lpower(Amin,2)));ec=umul(C0,udiv(U,lmul(sqrtUlo,ladd(1.,sqrtUlo))))
 meanC=uadd(udiv(mR,lmul(2.,lpower(Amin,2))),ec);gamma=udiv(meanC,bmin)
 ratioerr=udiv(uadd(umul(eap,Amax),umul(Apmax,ea)),lmul(lowdiff(Amin,ea),Amin));ls=umul(lm,uadd(ratioerr,gamma))
 Vrel=uadd(udiv(dnn,lmul(2.,lpower(Amin,2))),udiv(en,lmul(Amin,rho_min)))
 if Vrel>=1:raise ValueError('Interpolated speed expansion not valid')
 oneV=lowdiff(1.,Vrel);qnmin=umul(umul(Amin,rho_min),oneV)
 # Lower bound must use downward arithmetic rather than the upper product helper.
 qnmin=float(I.mul(I.mul(I.exact(Amin),I.exact(rho_min)),I.exact(oneV))[0])
 Irho=float(I.sum_upper(I.div(I.exact(I.absolute_upper(amp)),I.exact(nu))[1]));qprim=uadd(umul(Amax,Irho),udiv(Jdn,2*Amin),eq)
 eB=uadd(ec,umul(gamma,qprim));B0=udiv(Jn,lmul(2.,lpower(Amin,2)));Bmax=uadd(B0,eB);ps=udiv(Bmax,qnmin)
 fcenter=list(F);zmean=I.at(co,(slice(None),2*M+1));fcenter[2]=I.sub(fcenter[2],(zmean[0][:,None],zmean[1][:,None]))
 fcn=[cover(z,'Fcenter'+str(j),'odd' if j==1 else 'even',2*M)for j,z in enumerate(fcenter)]
 Fc=usqrt(uadd(*(upower(v,2)for v in fcn)));csbound=pbound(I.at(pder(co),(slice(None),2*M+1)))
 deltaC=uadd(umul(ld,csbound),umul(ls,Fc));Tmax=umul(umul(Amax,rho_max),usqrt(uadd(1.,U)));Mmax=umul(Mn,rho_max)
 frlead=udiv(Pfn,lmul(2.,lpower(Amin,2)));factorG=udiv(uadd(1.,U),lpower(oneV,2));factorGerr=udiv(uadd(U,umul(2.,Vrel),upower(Vrel,2)),lpower(oneV,2))
 fr=umul(lm,uadd(frlead,umul(udiv(Mn,Amin),udiv(Vrel,oneV)),umul(B0,factorGerr),umul(factorG,eB)))
 fr=uadd(fr,umul(deltaC,udiv(usqrt(uadd(1.,U)),oneV)))
 grden=lmul(lpower(Amin,2),lpower(oneV,2))
 gr=uadd(udiv(Pgn,grden),udiv(upower(dnn,2),lmul(4.,lmul(lpower(Amin,4),lpower(oneV,2)))))
 Qoverrho=uadd(Amax,udiv(dnn,2*Amin))
 gr=uadd(gr,udiv(umul(umul(2.,Qoverrho),en),lmul(grden,rho_min)),udiv(upower(en,2),lmul(grden,lpower(rho_min,2))))
 er=uadd(umul(ld,uadd(2.,ld)),umul(upower(lm,2),En),umul(umul(umul(2.,lm),usqrt(uadd(1.,En))),deltaC),upower(deltaC,2),umul(umul(2.,umul(lm,ps)),uadd(umul(lm,Mmax),umul(Tmax,deltaC))),umul(umul(upower(lm,2),upower(Tmax,2)),upower(ps,2)))
 op=I.scale(I.add(I.add(I.exact(er),I.exact(gr)),I.sqrt(I.add(I.square(I.sub(I.exact(er),I.exact(gr))),I.scale(I.square(I.exact(fr)),4.)))),.5)[1]
 report=dict(scope=__doc__,input_sha256=expected,source_sha256=source_sha,dependencies={str(p):s for p,s in dependency_hashes.items()},cell=i,part=a.part,original_left=float(x[i]),original_right=float(x[i+1]),left_exact=str(left),right_exact=str(right),exact_pulse_midpoint=str(boundary),whole_original_cell_covered=bool(a.part=='all'),construction_angles=N,audit_angles=Qn,scalar_panels=a.scalar_panels,
  scalar_kind=scalar_kind,scalar_quintic_knot=scalar_knot,scalar_polynomial_degree=len(A[0])-1,a_fourth_derivative_bound=a4bound,scalar_midpoint_integral_error=miderr,Amin=Amin,Amax=Amax,a_Taylor_error=ea,ap_Taylor_error=eap,rho_lower=rho_min,rho_upper=rho_max,
  polynomial_covers=cover_stats,mean_D_over_rho_bound=mD,mean_R_over_rho_bound=mR,U=U,Vrel=Vrel,sqrt_remainder=eq,interpolated_sqrt_remainder=en,mean_speed_difference=bA,lambda_minus_one=ld,lambda_s=ls,gamma=gamma,C_remainder=ec,B_remainder=eB,B0=B0,psi_s=ps,delta_center_velocity=deltaC,
  er_bound=er,gr_bound=gr,fr_bound=fr,gram_operator_bound=float(op),all_radius_and_angle_covered=True,complete_prefix_covered=False,strict_under_stated_IEEE_arithmetic=True,below_1e_minus_6=bool(op<1e-6),seconds=time.perf_counter()-start)
 if not np.isfinite(op)or sha(__file__)!=source_sha:raise ValueError('Nonfinite bound or changed source')
 if any(sha(p)!=s for p,s in dependency_hashes.items()):raise ValueError('Dependency changed during certificate')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print('report_sha256',sha(a.out))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('input','interval-source','scalar-oracle','out'):p.add_argument('--'+k,type=Path,required=True)
 p.add_argument('--cell',type=int,default=804);p.add_argument('--part',choices=['all','before','after'],default='all');p.add_argument('--angles',type=int,default=16384);p.add_argument('--scalar-panels',type=int,default=4096)
 main(p.parse_args())

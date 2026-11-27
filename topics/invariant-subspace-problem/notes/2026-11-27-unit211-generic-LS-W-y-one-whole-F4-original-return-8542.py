#!/usr/bin/env python3
"""R150 W: complete monic F4 cover, exact same-k/e original return.
New finite input from the successful complete fixed QQ projections.
Previous original Gram recovery is the necessary regeneration prefix.
R150 W: whole finite Gram y=1 original same-point recovery.
Use the original singleton-mean identity and the original E1 t coefficient
to determine x and t on y=1 using already paid ell and H only.
Return the same original N1, weighted N/P and physical D in two weights.
No multivariate gcd-one emptiness claim. No old cofactor or GB is repeated.
180 seconds / 4 GiB. Self-contained exact original Gram identities.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(x=None,**kw):
 if x is None:x=kw
 x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k','x','y','t','dummy_t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d);assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d
e,k,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);u=e+1;Q=e*k;Vbar=(e+1)*k+2;l=(e+1)*((k+2)**2-2*e*k)/(k*Vbar);Delta=1-Q
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj();bc=(l*l-(u-l)**2/Delta)/4
ivdiff=E(0,-1/(2*Delta));ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
V2=2*u-l*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
X=E(x0,x1);Y=X.conj()
f=(u*x0+(u-l*Q)*x1-T0/2)/(2*u)
W2=V2*x0+(2*u-u*Q-l*Q)*x1
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*t)/P02
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
g=lam*P02-(1-u)*T0
T=(g*T0-Pf*f-Phi*bc*Q*t)/(Q*P02)-l
r=X-a*p-c*E(t);s=Y-a*q-b*E(t);A=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
rows=[[E(),E(),p,q],[E(),A,r,s],[p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(a,v):return [a*b for b in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert F2==E(2*f)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC

def N4(v):
 return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
v=rows[0];zzv=rows[1]
Nv=N4(va(v,zzv))-N4(v)-N4(zzv)
vc=va(v,vs(-tau(v),one));zc=va(zzv,vs(-tau(zzv),one))
Pj=3*tau(vm(vm(vc,vc),zc))
NH=Nv-E(lam*fmpq(4,3))*Pj
assert not NH.b




assert N4(rows[0])==E(2*lam*P02)
assert Pj==E(3*(lam-1-T)*P02)
assert (Phi*(J-2*u*Q)-Pf)==0
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1

def P2(vv):
 cc=va(vv,vs(-tau(vv),one));return tau(vm(vm(cc,cc),cc))
NS=b*N4(rows[2])+c*N4(rows[3])-E(2*lam*P02*(l+2*T+A2))
PS=b*P2(rows[2])+c*P2(rows[3])-E(P02*(l+3*T+3*A2+B3))
assert not NS.b and not PS.b

# Explicit original value traces for the two weighted singleton rows.
assert P2(rows[0])==E(P02)
v1=(T-l*zeta)/u;v0=v1+zeta;hh=E(1+v0,v1);kk=hh.conj()
M=l*(2*u-l*Q)-u*u;Dphysical=l*A2-T*T
HA=l*M*zeta*zeta-2*T*M*zeta+V2*T*T-u*u*A2
zvalue=(hh-1)*(kk-1);assert not zvalue.b
HB=u*u*(B3-2*v0*A2+zvalue.a*T)
assert b*(hh-1)+c*(kk-1)==E(T)
assert b*hh*hh+c*kk*kk==E(l+2*T+A2+HA/(u*u))
assert b*hh**3+c*kk**3==E(l+3*T+3*A2+B3+((3+2*v0)*HA-HB)/(u*u))
weightedNB=b*(N4(rows[2])-E(2*lam*P02)*hh*hh)+c*(N4(rows[3])-E(2*lam*P02)*kk*kk)
weightedPB=b*(P2(rows[2])-E(P02)*hh**3)+c*(P2(rows[3])-E(P02)*kk**3)
assert weightedNB==NS-E(2*lam*P02*HA/(u*u))
assert weightedPB==PS-E(P02*((3+2*v0)*HA-HB)/(u*u))
assert E(Dphysical+l*HA/(u*u))==E(bc)*(hh-kk)**2
assert 4*bc*(1-Q)==M
Vlead=u*(Q+2)-2
assert Vlead==e*Vbar
W=(Phi*(J-2*u*Q)-Pf)/2;assert not W
Pp=2*e*k-k*k-5*k-8
M13=4*e**3*k*k-3*e*e*k**3-12*e*e*k*k-16*e*e*k+e*k**4+8*e*k**3+24*e*k*k+32*e*k+16*e-k**3-8*k*k-20*k-16
assert P02==-2*e*e*(e+1)*Pp/Vbar
assert Phi==-2*e*e*(k+4)/Vbar
assert M==-(e+1)**2*M13/(k*Vbar**2)
symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'EBe':EB.a,'EBo':EB.b,'N1':NH.a,'NS':NS.a,'PS':PS.a}
say(stage='same_original_Gram_and_weighted_NP_trace_identities',originalE0N0P1Verified=True,originalMeanAndN1Verified=True,P2BaseIdentityVerified=True,weightedOriginalNAndPTracesThroughHAHBVerified=True,HankelPhysicalUnitIdentityVerified=True,WWeightAndPaidUnitIdentitiesVerified=True,noXMinusUMinusOneInverted=True,claimExcluded=False)

M=l*(2*u-l*Q)-u*u
units=[('e',ep),('k',kp),('u',ep+1),('distinct_p_q',ep*kp-1),('W_paid_leading',ep*kp+kp+2),('Phi',kp+4),('P02',P02.n),('bc',M.n)]
out=[];cleared_polys=[];cleared_scales=[]
for name,rr,deg in [('E1',E1.a,2),('EBe',EB.a,2),('EBo',EB.b,2),('N1',NH.a,2),('weighted_N',NS.a,3),('weighted_P',PS.a,3)]:
 assert all(int(m[2])+int(m[3])+int(m[4])<=deg for m in rr.n.to_dict())
 po=rr.n;paid=oo;hist=[]
 for name0,atom in units:
  ct=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   po=po/gg;paid*=gg;ct+=1
  if ct:hist.append([name0,ct])
 assert po*paid==rr.n
 den=rr.d
 for name0,atom in units:
  while den:
   gg=den.gcd(atom)
   if gg.total_degree()==0:break
   den=den/gg
 assert den.total_degree()==0
 rec={'name':name,'poly':[[list(map(int,m)),str(a)] for m,a in po.to_dict().items()],'den':[[list(map(int,m)),str(a)] for m,a in rr.d.to_dict().items()]};out.append(rec);cleared_polys.append(po);cleared_scales.append(R(rr.d,paid))
 say({'stage':'new_W0_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})


Hpaid=4*ep*kp-kp*kp-4*kp-8
C9paid=4*ep*ep*kp*kp-ep*(kp**4+9*kp**3+20*kp*kp+16*kp)+kp**3+10*kp*kp+24*kp+16
known=units+[('previous_whole_k_minus_one',kp+1),('previous_complete_H_zero',Hpaid),('previous_general_ell_zero',l.n),('previous_general_equal_weights',(l-u).n),('previous_W_u_equals_Q',(u-Q).n),('equal_weights_implied_k_plus_two',kp+2),('previous_whole_C9',C9paid),('previous_whole_u_half',2*ep+1)]
def strip(po):
 initial=po;removed=oo;hist=[]
 for name,atom in known:
  count=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   quotient=po/gg;assert quotient*gg==po
   po=quotient;removed*=gg;count+=1
  if count:hist.append([name,count])
 assert po*removed==initial
 return po,removed,hist
def paid_den(rr):return strip(R(rr).d)[0].total_degree()==0
def coeffmap(rr):
 rr=R(rr);outc={}
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in rr.d.to_dict())
 for mm,cc in rr.n.to_dict().items():
  assert mm[5]==mm[6]==mm[7]==0
  mon=tuple(map(int,mm[2:5]))
  outc[mon]=outc.get(mon,zz)+cc*ep**int(mm[0])*kp**int(mm[1])
 return {mon:R(pp,rr.d) for mon,pp in outc.items() if pp}
xx,yy,tt=map(R,(Lp,Tp,fp))
def sub(rr,xv,yv,tv):
 outv=sum((cf*xv**mm[0]*yv**mm[1]*tv**mm[2] for mm,cf in coeffmap(rr).items()),R())
 assert paid_den(outv)
 return outv
def factor_info(po):
 if not po:return dict(zero=True)
 sc,fac=po.factor();back=ctx.constant(sc);facts=[]
 for ff,mul in fac:
  back*=ff**int(mul);dd=ff.to_dict()
  assert all(all(mm[j]==0 for j in range(2,8)) for mm in dd)
  rec=dict(degrees=list(map(int,ff.degrees()[:2])),totalDegree=int(ff.total_degree()),terms=len(dd),multiplicity=int(mul),sha256=hashlib.sha256(str(ff).encode()).hexdigest())
  if len(dd)<=120:rec['coefficients_e_k']=[[int(mm[0]),int(mm[1]),str(cc)] for mm,cc in dd.items()]
  facts.append(rec)
 assert back==po
 return dict(content=str(sc),factors=facts,allFactorProductsMultipliedBack=True)
def param_report(name,rr):
 rr=R(rr);assert paid_den(rr)
 assert all(mm==(0,0,0) for mm in coeffmap(rr))
 rem,paid,hist=strip(rr.n)
 say(stage='new_W_y_one_complete_original_parameter_return',name=name,numeratorDegrees=list(map(int,rr.n.degrees()[:2])),denominatorDegrees=list(map(int,rr.d.degrees()[:2])),paidRemoved=hist,remainingFactorization=factor_info(rem),sha256=hashlib.sha256((str(rr.n)+' / '+str(rr.d)).encode()).hexdigest(),constantNonzero=bool(rem) and rem.total_degree()==0,claimExcluded=False)
 return rem
Nweight=u*(2-2*u-Q)+l*Q*(2*u-1)
assert Nweight==-e*e*u*R(Hpaid)/Vbar
assert paid_den(Nweight) and paid_den(1/Nweight)
meancombo=(u-l)*symbolic['EBe']+l*(1-Q)*symbolic['EBo']
xstar=1+u-u/l
assert paid_den(xstar)
assert sub(meancombo,xx,R(1),tt)==-l*Nweight/u*(xx-xstar)
tc=sum((cf*xx**mm[0]*yy**mm[1] for mm,cf in coeffmap(meancombo).items() if mm[2]==1),R())
assert tc==M*(yy-1)
assert all(mm[2]<=1 for mm in coeffmap(meancombo))
e1=symbolic['E1']
tcE=sum((cf*xx**mm[0]*yy**mm[1] for mm,cf in coeffmap(e1).items() if mm[2]==1),R())
assert tcE==4*bc*(xx-u-1)
assert all(mm[2]<=1 for mm in coeffmap(e1))
pE=sub(e1,xstar,R(1),tt)
alpha=-4*bc*u/l
beta=sub(e1,xstar,R(1),R())
assert pE==alpha*tt+beta
assert paid_den(alpha) and paid_den(1/alpha)
tstar=-beta/alpha
assert paid_den(tstar)
assert not sub(e1,xstar,R(1),tstar)
assert not sub(meancombo,xstar,R(1),tstar)
say(stage='new_W_y_one_original_mean_and_E1_reconstruction',y=1,recoveredX='1+u-u/ell',recoveredT='-E1(xstar,1,0)/(-4bc*u/ell)',fullSingletonMeanCombinationIdentityVerified=True,fullGeneralMeanTcoefficient='M*(y-1)',fullGeneralE1Tcoefficient='4bc*(x-u-1)',allOriginalPaidInverseProductsVerified=True,noUnpaidXMinusUMinusOneInverted=True,claimExcluded=False)

# New input: the complete QQ cover from source d15791c9..., run 45973280857.
# The old two QQ resultants are not rerun. This source returns every same-k/e
# original parameter row on the entire monic four-dimensional cover.
from flint import fmpq_poly
def qp(v=()):
 return fmpq_poly(list(v))
def qco(p):
 return [str(c) for c in p.coeffs()]
cover=qp([32,64,48,12,1])
gg,ss,tt=cover.xgcd(cover.derivative())
assert gg.degree()==0 and ss*cover+tt*cover.derivative()==gg
F0=cover
source_rows=[]
source_denominators=[]
for name in ['EBe','EBo','N1','NS','PS']:
 rr=sub(symbolic[name],xstar,R(1),tstar)
 pp,removed,hist=strip(rr.n)
 assert pp*removed==rr.n and paid_den(rr)
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in pp.to_dict())
 source_rows.append((name,pp))
 source_denominators.append((name,rr.d))
Dstar=sub(symbolic['Dphysical'],xstar,R(1),tstar)
assert paid_den(Dstar)
unit_sources=list(known)+[('recovered_original_physical_D_numerator',Dstar.n)]
say(stage='new_W_y_one_F4_entire_original_input',baseCover=qco(cover),baseDegree=int(cover.degree()),coverSourceSHA256='d15791c981788f6ef2aa1ebc9d9a770f2b4c97b6b1beb4fbe35883478a3e0e48',coverRun=45973280857,coverIsEntireAndSquareFreeVerified=True,originalRows=[name for name,pp in source_rows],allSameOriginalRecoveryAndPaidScaleProductsVerified=True,originalDUnitIdentity='Dphysical+ell*HA/u^2=bc*(hU-kU)^2',twoOldQQResultantsRerun=False,claimExcluded=False)

class BaseNonunit(Exception):
 def __init__(self,factor):
  self.factor=factor/factor[factor.degree()]
  super().__init__('actual QQ[k] nonunit; retain both exact factors')
returns=[]
def whole_base(F,path):
 F=F/F[F.degree()]
 inverse_count=0
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.p=v.p;return
   if not isinstance(v,fmpq_poly):v=qp([v])
   qq,rr=divmod(v,F);assert qq*F+rr==v;self.p=rr
  def __bool__(self):return bool(self.p)
  def __neg__(self):return K(-self.p)
  def __add__(self,v):return K(self.p+K(v).p)
  __radd__=__add__
  def __sub__(self,v):return self+-K(v)
  def __rsub__(self,v):return K(v)+-self
  def __mul__(self,v):return K(self.p*K(v).p)
  __rmul__=__mul__
  def __eq__(self,v):return self.p==K(v).p
  def inv(self):
   nonlocal inverse_count
   assert self
   g,s,t=self.p.xgcd(F)
   assert s*self.p+t*F==g
   if g.degree()!=0:raise BaseNonunit(g)
   answer=K(s/g[0]);assert self*answer==1
   inverse_count+=1;return answer
  def __truediv__(self,v):return self*K(v).inv()
  def __rtruediv__(self,v):return K(v)*self.inv()
  def __pow__(self,n):
   assert n>=0
   a0=K(1);b0=self
   while n:
    if n&1:a0=a0*b0
    b0=b0*b0;n//=2
   return a0
  def data(self):return qco(self.p)
 class U:
  def __init__(self,v=()):
   if isinstance(v,U):self.c=v.c[:];return
   if isinstance(v,(K,int,fmpq)):v=[v]
   self.c=[K(z) for z in v]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def deg(self):return len(self.c)-1
  def __eq__(self,v):return self.c==U(v).c
  def __neg__(self):return U([-v for v in self.c])
  def __add__(self,v):
   v=U(v);n=max(len(self.c),len(v.c))
   return U([(self.c[i] if i<len(self.c) else K())+(v.c[i] if i<len(v.c) else K()) for i in range(n)])
  __radd__=__add__
  def __sub__(self,v):return self+-U(v)
  def __rsub__(self,v):return U(v)+-self
  def __mul__(self,v):
   v=U(v)
   if not self or not v:return U()
   w=[K() for _ in range(len(self.c)+len(v.c)-1)]
   for i,aa in enumerate(self.c):
    for j,bb in enumerate(v.c):w[i+j]=w[i+j]+aa*bb
   return U(w)
  __rmul__=__mul__
  def scale(self,z):return U([v*K(z) for v in self.c])
  def __pow__(self,n):
   assert n>=0
   w=U(1);b0=self
   while n:
    if n&1:w=w*b0
    b0=b0*b0;n//=2
   return w
  def data(self):return [c.data() for c in self.c]
 def dr(A0,B0):
  A0=U(A0);B0=U(B0);assert B0
  q0=U();r0=U(A0)
  leadinv=B0.c[-1].inv()
  while r0 and r0.deg()>=B0.deg():
   shift=r0.deg()-B0.deg();a0=r0.c[-1]*leadinv
   term=U([K()]*shift+[a0])
   q0=q0+term;r0=r0-term*B0
  assert q0*B0+r0==A0
  assert not r0 or r0.deg()<B0.deg()
  return q0,r0
 def xg(A0,B0):
  A0=U(A0);B0=U(B0)
  a0,b0=A0,B0;s0,s1=U(1),U();t0,t1=U(),U(1)
  while b0:
   q0,r0=dr(a0,b0)
   a0,b0=b0,r0;s0,s1=s1,s0-q0*s1;t0,t1=t1,t0-q0*t1
  if a0:
   iv=a0.c[-1].inv();a0=a0.scale(iv);s0=s0.scale(iv);t0=t0.scale(iv)
  assert s0*A0+t0*B0==a0
  if a0:
   assert not dr(A0,a0)[1] and not dr(B0,a0)[1]
  return a0,s0,t0
 def cv(pp):
  dd=pp.to_dict();de=max((int(mm[0]) for mm in dd),default=-1)
  vals=[K() for _ in range(de+1)]
  for mm,cc in dd.items():
   assert all(mm[j]==0 for j in range(2,8))
   vals[int(mm[0])]=vals[int(mm[0])]+K(qp([0]*int(mm[1])+[cc]))
  return U(vals)
 rows=[cv(pp) for name,pp in source_rows]
 units0=[(name,cv(pp)) for name,pp in unit_sources]
 denominators=[(name,cv(pp)) for name,pp in source_denominators]+[('Dphysical',cv(Dstar.d))]
 g=U();tags=[U() for _ in rows];row_quotients=[]
 profile=[]
 for i,(name,pp) in enumerate(source_rows):
  newg,s,t=xg(g,rows[i])
  tags=[s*v for v in tags];tags[i]=tags[i]+t;g=newg
  assert sum((tag*row for tag,row in zip(tags,rows)),U())==g
  profile.append(dict(name=name,specializedEDegree=rows[i].deg(),commonEDegree=g.deg(),sameOriginalCombinationProductsVerified=True))
  say(stage='new_W_y_one_F4_same_e_original_QQ_gcd',path=path,**profile[-1],claimExcluded=False)
  if g and g.deg()==0:break
 if g:
  for row in rows:
   q0,r0=dr(row,g);assert not r0 and q0*g==row
   row_quotients.append(q0)
 original_g=g
 remaining=U(g);removed=U(1);unit_removed_records=[];unit_trace=[]
 impossible_unit=None
 for name,atom in units0:
  if not atom:
   impossible_unit=name
   break
  count=0;pieces=[]
  while remaining and remaining.deg()>0:
   common,s,t=xg(remaining,atom)
   if not common or common.deg()==0:break
   quotient,r0=dr(remaining,common);assert not r0 and quotient*common==remaining
   aq,ar=dr(atom,common);assert not ar and aq*common==atom
   pieces.append(dict(common=common.data(),unitQuotient=aq.data()))
   remaining=quotient;removed=removed*common;count+=1
  if count:
   unit_trace.append(dict(name=name,pieces=pieces))
   unit_removed_records.append(dict(name=name,count=count,remainingEDegree=remaining.deg(),eachRemovedFactorDividesActualPaidUnitVerified=True))
   say(stage='new_W_y_one_F4_original_unit_saturation',path=path,**unit_removed_records[-1],claimExcluded=False)
 assert remaining*removed==original_g
 if remaining and remaining.deg()>0:
  for name,atom in units0+denominators:
   common,s,t=xg(remaining,atom)
   assert common==U(1) and s*remaining+t*atom==1
 certificate=dict(baseCover=qco(F),originalRowNames=[name for name,pp in source_rows],originalRows=[row.data() for row in rows],sameEOriginalCombination=[v.data() for v in tags],originalCommonEPolynomial=original_g.data(),rowQuotients=[v.data() for v in row_quotients],paidRemoved=removed.data(),remainingSameEPolynomial=remaining.data(),unitDivisionTraces=unit_trace,identicallyZeroOriginalUnit=impossible_unit)
 cb=json.dumps(certificate,separators=(',',':')).encode()
 closed=impossible_unit is not None or bool(remaining) and remaining.deg()==0
 rec=dict(path=path,baseCover=qco(F),baseQQDegree=int(F.degree()),originalRowProfile=profile,originalCommonEDegree=original_g.deg(),unitRemovalProfile=unit_removed_records,remainingEDegree=remaining.deg(),remainingSameECoefficients=remaining.data() if len(json.dumps(remaining.data()))<=8192 else None,identicallyZeroOriginalUnit=impossible_unit,allOriginalCombinationAndUnitDivisionProductsActual=True,allOriginalRowsSameKAndSameE=True,actualBaseInverseProducts=inverse_count,physicalDOriginalUnitRetained=True,certificateBytes=len(cb),certificateSHA256=hashlib.sha256(cb).hexdigest(),excluded=closed)
 returns.append(rec)
 say(stage='new_W_y_one_entire_F4_original_same_point_return',**rec,claimExcluded=closed)
def process(F,path):
 try:whole_base(F,path)
 except BaseNonunit as err:
  g=err.factor;q0,r0=divmod(F,g)
  assert not r0 and q0*g==F and g.degree()>0 and q0.degree()>0
  say(stage='new_W_y_one_F4_actual_base_nonunit_split',path=path,factor=qco(g),complement=qco(q0),entireOriginalCoverRetained=True,allProductsVerified=True,claimExcluded=False)
  process(g,path+'/a');process(q0,path+'/b')
process(cover,'F4')
closed=bool(returns) and all(r['excluded'] for r in returns)
signal.alarm(0)
say(stage='new_W_y_one_complete_original_F4_return_gate_complete',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),completePublishedQQCover=qco(cover),originalQQCoverAllBranchesReturned=True,allOriginalSamePointAndPaidInverseProductsVerified=True,returns=returns,wholeW_y_oneExcluded=closed,wholeWExcluded=False,oldQQResultantsRerun=False,claimExcluded=closed,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

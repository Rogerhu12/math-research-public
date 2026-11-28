#!/usr/bin/env python3
"""NEW h=k on the entire symmetric p+q=2, u=1 original fiber.
This is not the old p=1, u_old=1 fiber.  Rebuild the true Gram using
kappa=bc*t/ell, pay the entire NV slope-zero fiber, then keep free Q.
Four predetermined original Q projections only, with all head-zero
fibers retained.  120 seconds / 1 GiB. No old cofactor target replay.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
START=time.perf_counter()
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
path=Path(__file__).with_name('2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py')
raw=path.read_text()
assert hashlib.sha256(raw.encode()).hexdigest()=='2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2'
ar=raw[raw.index('ctx=fmpq_mpoly_ctx'):raw.index('lam,u,Q=map')]
ur=raw[raw.index('def trim(v):'):raw.index('z=U([0,1]);')]
assert len(ar.encode())==1628 and hashlib.sha256(ar.encode()).hexdigest()=='208b244cf063707ca4613f8c61d8a351860639348961a77815d1f8fafd149765'
assert len(ur.encode())==1127 and hashlib.sha256(ur.encode()).hexdigest()=='441ac944e389144cc94a7358f4fd1c011736d28f77daaf3edd4e15544aa0e3c9'
env={'fmpq_mpoly_ctx':fmpq_mpoly_ctx}
exec(compile(ar+'\n'+ur,str(path)+'#arithmetic_definitions_only','exec'),env)
R,U,ctx=env['R'],env['U'],env['ctx']
Lp,unused_up,Qp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
lam,Q=R(Lp),R(Qp);u=R(1);disc=1-Q
A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
xi=B/A;ell=A**3/(B*B);T=A*A/B;w=lam-1-T
hh=1+xi;S=2*xi+3-2*lam;eta=xi+3-2*lam
m=u-ell;a=1-ell;bc=(ell*ell-m*m/disc)/4
V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q;P02=(2-3*u)*V2-Q*u+2*u**3
Pf=T0*(J-Q);M=ell*V2-u*u
Eslope=lam*lam+lam-1
assert A+B==lam*(2*lam-1)**2
assert ell*xi==T and ell*xi*xi==A
assert P02==(ell-1)*Q and Pf==ell*(1-ell)*Q*Q
assert T0==-ell*Q and Phi==(1-ell)*Q and M==4*bc*disc
kappa=U([0,1])
f=lam+hh-kappa;t=ell*kappa/bc;z=Q*t
vn=U(Q*(lam+ell*hh));Wstar=T0+4*f
G=lam*P02;Pc=Q*P02*(ell+T)-G*T0
assert Pf*f+bc*Phi*z+Pc==U()
nv=Q*(2*Eslope*(kappa-hh)+lam*hh*hh)
def higher(fn):
 def call(self,other):
  if getattr(other,'_isp_quotient_level',0)>1:return NotImplemented
  return fn(self,other)
 return call
for name in ['__add__','__radd__','__sub__','__rsub__','__mul__','__rmul__','__truediv__','__eq__']:
 setattr(U,name,higher(getattr(U,name)))
class E:
 _isp_quotient_level=2
 def __init__(self,x=0,y=0):
  if isinstance(x,E):
   assert not y;self.x=x.x;self.y=x.y
  else:self.x=U(x);self.y=U(y)
 def __bool__(self):return bool(self.x) or bool(self.y)
 def __add__(self,o):o=E(o);return E(self.x+o.x,self.y+o.y)
 __radd__=__add__
 def __neg__(self):return E(-self.x,-self.y)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):
  o=E(o);return E(self.x*o.x+disc*self.y*o.y,self.x*o.y+self.y*o.x)
 __rmul__=__mul__
 def __truediv__(self,o):
  assert not isinstance(o,(U,E))
  return E(self.x/o,self.y/o)
 def __pow__(self,n):
  assert n>=0
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):
  o=E(o);return self.x==o.x and self.y==o.y
 def conj(self):return E(self.x,-self.y)
p=E(1,1);q=p.conj()
bb=E(ell/2,m/(2*disc));cc=bb.conj()
assert bb+cc==E(ell) and bb*cc==E(bc) and bb*p+cc*q==E(u)
VV=vn/Q;WW=Wstar/2;t=z/Q
xx=((u-ell*Q)*VV-m*WW)/M
yy=(ell*WW-u*VV)/M
X=E(xx,yy);Y=X.conj()
assert bb*X+cc*Y==E(VV) and bb*p*X+cc*q*Y==E(WW)
r=X-E(a)*p-cc*E(t);s=Y-E(a)*q-bb*E(t)
AA=E(2*f-2*VV+2*bc*t)
rows=[[E(),E(),p,q],[E(),AA,r,s],
      [p,r,E(),E(t)],[q,s,E(t),E()]]
unit=[E(1),E(),E(1),E(1)]
def va(v,z):return [x+y for x,y in zip(v,z)]
def vs(x,v):x=E(x);return [x*y for y in v]
def vm(v,z):
 return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return E(a)*v[0]+v[1]+bb*v[2]+cc*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(unit);F2=tau(d);Kd=DK(d)
assert F2==E(2*f) and d[0]==E(u)
def mean(j):
 e=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return e-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
def N4(v):
 tv=tau(v);vv=vm(v,v)
 return 2*tau(vm(d,vv))-F2*tau(vv)-4*tv*tau(vm(d,v))+2*F2*tv**2+tau(vm(v,DK(v)))
def centered(v):return va(v,vs(-tau(v),unit))
def P2(v):
 cv=centered(v);return tau(vm(vm(cv,cv),cv))
Pj=3*tau(vm(vm(centered(rows[0]),centered(rows[0])),centered(rows[1])))
assert P2(rows[0])==E(P02)
assert N4(rows[0])==E(2*lam*P02)
assert Pj==E(3*w*P02)
value=[E(1),E(w),E(hh),E(hh)]
assert tau(value)==E(lam) and tau(vm(value,value))==E(2*lam*lam)
assert tau(vm(vm(value,value),value))==E(4*lam**3)
assert E(Q)*N4(value)==E(2*nv)
# The preceding exact free-kappa Gram returns prove
# (Q/2)N4(V)=Q*(2*Eslope*(kappa-hh)+lambda*hh^2).
# Eslope=0 forces lambda*hh^2=0.  lambda, A, 2lambda-1
# are actual units here, and A*hh=lambda*(2lambda-1)^2.
# Thus the WHOLE slope-zero fiber is empty without dividing the slope there.
kstar=hh-lam*hh*hh/(2*Eslope)
def ev(v):
 v=U(v);out=R()
 for c0 in reversed(v.c):out=out*kstar+c0
 return out
assert ev(nv)==R()
assert ev(f)==lam+lam*hh*hh/(2*Eslope)
assert ev(AA.x)==(1-ell)*lam*hh*hh/Eslope and not AA.y
E1=mean(1);EB=mean(2);EC=mean(3)
N1=N4(va(rows[0],rows[1]))-N4(rows[0])-N4(rows[1])-E(4*lam*w*P02)
NB=N4(rows[2])-E(2*lam*P02*hh*hh)
NCrow=N4(rows[3])-E(2*lam*P02*hh*hh)
PB=P2(rows[2])-E(P02*hh**3)
PC=P2(rows[3])-E(P02*hh**3)
assert not E1.y and not N1.y
assert EB.conj()==EC and NB.conj()==NCrow and PB.conj()==PC
names=['E1','EBe','EBo','N1','NBe','NBo','PBe','PBo']
values=[ev(v) for v in [E1.x,EB.x,EB.y,N1.x,NB.x,NB.y,PB.x,PB.y]]
say('new_hk_symmetric_u_one_complete_original_Nv_slope',
 originalNormalization='p+q=2, u=bp+cq=1',
 originalFreeKappa='bc*t/ell',
 exactOriginalNvIdentity='N4(V)/2=2*(lambda^2+lambda-1)*(kappa-h)+lambda*h^2',
 fullFreeKappaGramE0N0P0P1AndMomentsReturned=True,
 entireSlopeZeroExcludedByOriginalLambdaHalfAndNonzeroMean=True,
 noOldP1UoneExclusionImported=True,
 noDeltaOrNVGenericSlopeZeroFiberDropped=True,
 originalEightRowsReturned=True)
def pure_lam(p):return all(e[1]==e[2]==0 for e in p.to_dict())
def degreeQ(p):return max((int(e[2]) for e in p.to_dict()),default=-1)
def profile(p):
 return dict(degrees_lambda_unused_Q=list(map(int,p.degrees())) if p else [-1]*3,
             terms=len(p.to_dict()),
             sha256=hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest())
divisions=0
def dex(a,b):
 global divisions
 q0,r0=divmod(a,b);assert not r0 and q0*b==a
 divisions+=1;return q0
# lambda=0, lambda=1/2, A*B=0 have their independent physical exclusions.
# ell-1 follows from P02=(ell-1)Q; kstar from the whole true t=0 exclusion.
paid_lambda=Lp*A.n*B.n*(2*Lp-1)*Eslope.n*(ell-1).n*kstar.n
assert pure_lam(paid_lambda)
paid_all=paid_lambda*Qp*(1-Qp)*M.n
def strip(p,paid):
 original=p;rem=p;removed=oneP;rounds=0
 while rem and int(rem.total_degree())>0:
  g=rem.gcd(paid)
  if int(g.total_degree())<=0:break
  rem=dex(rem,g);removed*=g;rounds+=1
 assert rem*removed==original
 return rem,removed,rounds
prepared=[]
for name,rr in zip(names,values):
 assert all(e[1]==0 for p0 in [rr.n,rr.d] for e in p0.to_dict())
 den,dd,n0=strip(rr.d,paid_all)
 assert den and int(den.total_degree())==0,(name,'unpaid denominator',profile(den))
 core,removed,n1=strip(rr.n,paid_all)
 assert R(core)*R(removed,rr.d)==rr
 prepared.append(core)
 say('new_hk_symmetric_u_one_true_original_row',name=name,
  QDegree=degreeQ(core),profile=profile(core),
  onlyActualPaidNumeratorGCDRounds=n1,fullOriginalRowScalingReturned=True)
def qcols(p):
 out=[zeroP]*(degreeQ(p)+1)
 for e,cc0 in p.to_dict().items():
  assert e[1]==0
  out[int(e[2])]+=cc0*Lp**int(e[0])
 assert sum((v*Qp**i for i,v in enumerate(out)),zeroP)==p
 return out
def determinant(mat):
 n=len(mat)
 if not n:return oneP
 work=[r[:] for r in mat];previous=oneP;sign=1
 for k in range(n-1):
  pivot=next((j for j in range(k,n) if work[j][k]),None)
  if pivot is None:return zeroP
  if pivot!=k:work[k],work[pivot]=work[pivot],work[k];sign=-sign
  p0=work[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    work[i][j]=dex(p0*work[i][j]-work[i][k]*work[k][j],previous)
   work[i][k]=zeroP
  previous=p0
 return sign*work[-1][-1]
def fixed_projection(a0,b0):
 if not a0 or not b0:return zeroP,0
 ac,bc0=qcols(a0),qcols(b0);m0,n0=len(ac)-1,len(bc0)-1
 if m0==0:return ac[0],1
 if n0==0:return bc0[0],1
 matrix=[]
 for cols,mult in [(ac,n0),(bc0,m0)]:
  for shift in range(mult):
   row=[zeroP]*shift+cols+[zeroP]*(m0+n0-shift-len(cols))
   assert len(row)==m0+n0
   assert sum((cc0*Qp**j for j,cc0 in enumerate(row)),zeroP)==Qp**shift*sum((cc0*Qp**j for j,cc0 in enumerate(cols)),zeroP)
   matrix.append(row)
 return determinant(matrix),m0+n0
def to_lam(p):
 assert pure_lam(p)
 out=[fmpq(0)]*(int(p.degrees()[0])+1 if p else 0)
 for e,v in p.to_dict().items():out[int(e[0])]=fmpq(v)
 return fmpq_poly(out)
def from_lam(p):return sum((cc0*Lp**j for j,cc0 in enumerate(p.coeffs())),zeroP)
targets=[];gcd_poly=fmpq_poly([]);tags=[]
for ia,ib in [(0,1),(0,2),(1,2),(2,3)]:
 target,size=fixed_projection(prepared[ia],prepared[ib])
 assert pure_lam(target)
 if not target:
  say('new_hk_symmetric_u_one_fixed_projection_zero',rows=[names[ia],names[ib]],fixedSize=size)
  continue
 core,removed,n0=strip(target,paid_lambda)
 assert core and pure_lam(core)
 lp=to_lam(core);targets.append(lp)
 newg,ss,tt= gcd_poly.xgcd(lp)
 assert ss*gcd_poly+tt*lp==newg
 tags=[ss*v for v in tags]+[tt]
 assert sum((v*p0 for v,p0 in zip(tags,targets)),fmpq_poly([]))==newg
 gcd_poly=newg
 say('new_hk_symmetric_u_one_fixed_original_Q_projection',
  rows=[names[ia],names[ib]],fixedSize=size,originalDeterminant=profile(target),
  retainedLambdaPolynomial=profile(core),paidOnlyLambdaGCDRounds=n0,
  exactAccumulatedQQBezout=profile(from_lam(gcd_poly)),
  everyOriginalQLeadingZeroFiberKept=True,
  entireUoneExcluded=gcd_poly.degree()==0)
 if gcd_poly.degree()==0:break
say('new_hk_symmetric_u_one_original_return_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 numberOfNonzeroFixedProjections=len(targets),
 exactPolynomialDivisions=divisions,
 finalNecessaryLambdaCover=profile(from_lam(gcd_poly)),
 entireSymmetricUoneExcluded=bool(gcd_poly) and gcd_poly.degree()==0,
 allRetainedLambdaAndFreeQFibersKept=True,
 entireHkExcluded=False,ordinaryISPClaim=False)

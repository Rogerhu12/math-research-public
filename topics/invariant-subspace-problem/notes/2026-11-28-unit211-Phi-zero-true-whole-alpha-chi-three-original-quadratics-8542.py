#!/usr/bin/env python3
"""NEW corrected Phi: whole alpha/chi raw original three-quadratic input.
The old TRUE entire equal-weight theorem pays m=u-ell.  Original Rw=
-(u-1)*A and the already closed A face pay Rw.  No alpha, chi, theta,
D, lambda, or new head is inverted.  Three raw EBe/EBo/N1 polynomials
are quadratic in alpha.  A fixed 3x3 cofactor and two fixed 4x4 quadratic resultants return
same-point necessary chi/weight polynomials, including every leading-zero
fiber.  Only each set of actual multipliers' common content is canceled.
Self-contained first input, 120 seconds / 1 GiB, small summaries only.
"""
import hashlib,json,resource,signal,time
from flint import fmpq_mpoly_ctx
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.alarm(120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','chi','alpha'),'lex')
up,Qp,chip,alp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oneP if d is None else poly(d);assert d
  if not n:self.n=zeroP;self.d=oneP;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,z):
  z=R(z)
  if not self:return z
  if not z:return self
  g=self.d.gcd(z.d);a=self.d/g;b=z.d/g
  return R(self.n*b+z.n*a,a*z.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,z):return self+-R(z)
 def __rsub__(self,z):return R(z)+-self
 def __mul__(self,z):
  z=R(z)
  if not self or not z:return R()
  g=self.n.gcd(z.d);h=z.n.gcd(self.d)
  return R((self.n/g)*(z.n/h),(self.d/h)*(z.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,z):
  z=R(z);assert z
  return self*R(z.d,z.n,False)
 def __rtruediv__(self,z):return R(z)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return R(self.n**n,self.d**n,False)
 def __eq__(self,z):
  z=R(z);return self.n*z.d==z.n*self.d
u,Q,chi,alpha=map(R,(up,Qp,chip,alp))
s=u-1;delta=1-Q;L=Q-2*s*(u-2);K=Q+4*s
ell=L/Q;a=1-ell;m=u-ell;theta=u-L
Mn=2*u*L-L*L-u*u*Q;M=Mn/Q;bc=M/(4*delta)
T0=-K;J0=2*u*(1-u)+L;P02=2*s*L
Ahead=4*s*s-Q
Rw=2*u*(1-u)-u*Q+(2*u-1)*L
Z=u*(u-1)+ell*(1-ell)*Q
assert Rw==-s*Ahead
# These are the published FREE original coordinates, now on true Phi.
# All denominators below are pure old weight units, not alpha or chi.
tt=-alpha*chi/(m*Rw)-2*delta*ell/m
ff=u+(alpha+theta*tt)/(4*delta)
VV=ff+(M-Z-chi)*tt/(4*delta)
A1=(chi+Z)*tt/(2*delta)
W1=(T0+4*u*ff)/2
xx=(theta*VV-m*W1)/M;yy=(ell*W1-u*VV)/M
lam=(J0*ff+bc*Q*tt-Q*VV-s*T0)/P02
Tr=T0*A1/(2*P02)-ell
ww=lam-1-Tr
assert A1==2*ff-2*VV+2*bc*tt
assert 4*delta*(ff-u)-theta*tt==alpha
assert 2*delta*A1==(chi+Z)*tt
assert ell*xx+m*yy==VV and u*xx+theta*yy==W1
assert m*Rw*tt==-alpha*chi-2*delta*ell*Rw
R4=(16*delta*(ff-u)*(VV-ff)+M*tt*tt+4*M*u*tt
    -4*theta*VV*tt+2*m*T0*tt+8*m*u*ff*tt)
assert not R4
paidP=(up*Qp*(1-Qp)*(up-1)*K.n*L.n*Mn.n*Ahead.n*(up*Qp-L.n))
def weight(p):return all(int(ex[2])==0 and int(ex[3])==0 for ex in p.to_dict())
def alpha_free(p):return all(int(ex[3])==0 for ex in p.to_dict())
divisionReturns=0;den_seen=set()
def exact(p,g):
 global divisionReturns
 q,r=divmod(p,g);assert not r and q*g==p
 divisionReturns+=1;return q
def strip_paid(p):
 assert alpha_free(p)
 if not p:return p,oneP
 rem=p;removed=oneP
 while int(rem.total_degree())>0:
  g=rem.gcd(paidP)
  if int(g.total_degree())<=0:break
  rem=exact(rem,g);removed*=g
 assert rem*removed==p
 return rem,removed
def paid(p):
 assert p and weight(p)
 key=str(p)
 if key in den_seen:return
 rest,_=strip_paid(p);assert int(rest.total_degree())==0
 den_seen.add(key)
def ck(v):
 v=R(v);paid(v.d);return v
def adeg(v):
 v=R(v);assert weight(v.d)
 return max((int(ex[3]) for ex in v.n.to_dict()),default=-1)
def ac(v,j):
 v=R(v);assert weight(v.d)
 return R(ctx.from_dict({(ex[0],ex[1],ex[2],0):c
           for ex,c in v.n.to_dict().items() if int(ex[3])==j}),v.d)
def info(p):
 out={'zero':not bool(p),'degrees':list(map(int,p.degrees())) if p else [-1]*4,
      'totalDegree':int(p.total_degree()) if p else -1,'terms':len(p.to_dict()),
      'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
 if p and len(p.to_dict())<=35:out['polynomial']=str(p)
 return out
for value in [tt,ff,VV,A1,W1,xx,yy,lam,Tr]:
 ck(value);assert adeg(value)<=1
say('new_correct_Phi_whole_alpha_chi_original_coordinate_input',
 pureWeightDenominatorsPaid=True,originalRReturned=True,
 alphaChiThetaZeroFibersKept=True,
 mPayment='old true whole equal-weight original theorem; independently audited vm(d,d)[1]',
 noOldWrongPhiHeadOrModuleUsed=True,
 originalVariableDegrees={name:adeg(value) for name,value in
  [('t',tt),('f',ff),('V',VV),('A1',A1),('lambda',lam),('T',Tr)]})
# Actual quadratic rho extension and ORIGINAL dual multiplication.
def E(c=0,d=0):return [R(c),R(d)]
def ea(v,w):return [v[0]+w[0],v[1]+w[1]]
def en(v):return [-v[0],-v[1]]
def es(v,w):return ea(v,en(w))
def em(v,w):return [v[0]*w[0]+delta*v[1]*w[1],v[0]*w[1]+v[1]*w[0]]
def ec(v,c):c=R(c);return [c*v[0],c*v[1]]
def cj(v):return [v[0],-v[1]]
def esm(*vs):
 out=E()
 for v in vs:out=ea(out,v)
 return out
bp=E(ell/2,m/(2*delta));cp=cj(bp)
pPhys=E(1,1);qPhys=cj(pPhys)
XP=E(xx,yy);YP=cj(XP)
rP=es(es(XP,ec(pPhys,a)),ec(cp,tt));sP=cj(rP)
rows=[[E(),E(),pPhys,qPhys],[E(),E(A1),rP,sP],
      [pPhys,rP,E(),E(tt)],[qPhys,sP,E(tt),E()]]
one=[E(1),E(),E(1),E(1)]
def vm(v,w):
 return [em(v[0],w[0]),ea(em(v[0],w[1]),em(v[1],w[0])),
         em(v[2],w[2]),em(v[3],w[3])]
def va(v,w):return [ea(c,d) for c,d in zip(v,w)]
def vs(c,v):return [em(c,d) for d in v]
def tau(v):return esm(ec(v[0],a),v[1],em(bp,v[2]),em(cp,v[3]))
def DK(v):return [tau(vm(row,v)) for row in rows]
dv=DK(one);F2=tau(dv);kd=DK(dv);d2=vm(dv,dv)
assert F2==E(2*ff)
def mean(i):
 first=ec(tau(vm(rows[0],rows[1])),2) if i==1 else tau(vm(rows[i],rows[i]))
 return esm(first,ec(kd[i],-2),ec(d2[i],-2),ec(em(F2,dv[i]),2))
def N4(v):
 tv=tau(v);v2=vm(v,v)
 return esm(ec(tau(vm(dv,v2)),2),en(em(F2,tau(v2))),
  ec(em(tv,tau(vm(dv,v))),-4),ec(em(F2,em(tv,tv)),2),tau(vm(v,DK(v))))
def centered(v):return va(v,vs(en(tau(v)),one))
def P2(v):
 cv=centered(v);return tau(vm(vm(cv,cv),cv))
def pure(v):assert not v[1];return v[0]
assert mean(0)==E()
EB=mean(2);EC=mean(3)
assert EC==cj(EB)
EW=ea(em(bp,EB),em(cp,EC))
assert mean(1)==EW
assert P2(rows[0])==E(P02)
N0=N4(rows[0]);assert N0==E(2*lam*P02)
C0=centered(rows[0]);C1=centered(rows[1])
Pjet=ec(tau(vm(vm(C0,C0),C1)),3)
assert Pjet==E(3*ww*P02)
Njet=es(es(N4(va(rows[0],rows[1])),N0),N4(rows[1]))
N1=pure(Njet)-4*lam*ww*P02
original=[EB[0],EB[1],N1]
mat=[]
for fi in original:
 assert adeg(fi)<=2
 row=[ck(ac(fi,j)) for j in range(3)]
 assert fi==row[0]+row[1]*alpha+row[2]*alpha*alpha
 mat.append(row)
say('new_whole_alpha_chi_three_original_alpha_quadratics',
 rows=['EBe','EBo','N1'],actualAlphaDegrees=[adeg(fi) for fi in original],
 allOriginalDualGramAndN0PjetReturns=True,
 allNineCoefficientDenominatorsOnlyOldWeightUnits=True,
 coefficients=[[{'n':info(v.n),'d':info(v.d)} for v in row] for row in mat])
# Fixed 3x3 cofactor for the constant coordinate, with no leading inverse.
mu=[mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1],
    mat[2][1]*mat[0][2]-mat[2][2]*mat[0][1],
    mat[0][1]*mat[1][2]-mat[0][2]*mat[1][1]]
det=sum((mu[i]*mat[i][0] for i in range(3)),R())
assert sum((mu[i]*mat[i][1] for i in range(3)),R())==0
assert sum((mu[i]*mat[i][2] for i in range(3)),R())==0
assert sum((mu[i]*original[i] for i in range(3)),R())==det
for value in mu+[det]:ck(value)
if not any(mu):
 say('new_whole_alpha_chi_fixed_original_cofactor_zero',
  allThreeOriginalCoordinatesReturned=True,wholePhiExcluded=False,
  noAlphaHeadOrOtherZeroFiberRemoved=True,
  exactDivisionReturns=divisionReturns,ordinaryISPClaim=False)
else:
 common_den=oneP
 for value in mu:common_den=exact(common_den,common_den.gcd(value.d))*value.d
 paid(common_den)
 numer=[value.n*exact(common_den,value.d) for value in mu]
 content=zeroP
 for p in numer:content=content.gcd(p)
 assert content
 primitive=[exact(p,content) for p in numer]
 C=sum((R(primitive[i])*mat[i][0] for i in range(3)),R())
 assert sum((R(primitive[i])*mat[i][1] for i in range(3)),R())==0
 assert sum((R(primitive[i])*mat[i][2] for i in range(3)),R())==0
 assert sum((R(primitive[i])*original[i] for i in range(3)),R())==C
 assert R(content)*C==R(common_den)*det
 ck(C);assert alpha_free(C.n)
 retained,removed=strip_paid(C.n)
 if retained:
  lc=retained.coefficient(0);retained/=lc;removed*=lc
 assert retained*removed==C.n
 say('new_whole_alpha_chi_fixed_three_original_cofactor',
  actualThreeMultiplierCommon=info(content),
  originalScalarNumerator=info(C.n),originalScalarDenominator=info(C.d),
  retainedNecessaryChiWeightPolynomial=info(retained),
  allThreeOriginalCoordinatesReturnedAfterCancellation=True,
  entireActualCommonMultiplierZeroFaceKept=True,
  allAlphaLeadingZeroFacesKept=True,thetaZeroFaceKept=True,
  onlyPublishedPhysicalWeightUnitsRemoved=True,
  wholePhiExcluded=bool(retained) and int(retained.total_degree())==0,
  exactDivisionReturns=divisionReturns,ordinaryISPClaim=False)

# Two further NEW fixed quadratic/quadratic Sylvester identities.
# A=a*x^2+b*x+c, B=d*x^2+e*x+f:
# p=a*f-c*d, q=a*e-b*d, r=b*f-c*e, Res=p^2-q*r.
# [q*e-p*d+q*d*x] A + [-q*b+p*a-q*a*x] B = Res.
# No quadratic/linear leading coefficient is divided.
for i,j in [(1,0),(1,2)]:
 c,b,aa=mat[i];f,e,dd=mat[j]
 pp=aa*f-c*dd;qq=aa*e-b*dd;rr=b*f-c*e
 mul=[qq*e-pp*dd,qq*dd,-qq*b+pp*aa,-qq*aa]
 target=pp*pp-qq*rr
 rowA,rowB=mat[i],mat[j]
 def pair_return(mm):
  out=[R() for _ in range(4)]
  for k in range(3):
   out[k]+=mm[0]*rowA[k]+mm[2]*rowB[k]
   out[k+1]+=mm[1]*rowA[k]+mm[3]*rowB[k]
  return out
 ret=pair_return(mul)
 assert ret[0]==target and all(not value for value in ret[1:])
 for value in mul+[target]:ck(value)
 if not any(mul):
  say('new_alpha_chi_fixed_four_by_four_zero',
   pair=[['EBe','EBo','N1'][k] for k in (i,j)],
   allFourOriginalCoordinatesReturned=True,wholePhiExcluded=False)
  continue
 den=oneP
 for value in mul:den=exact(den,den.gcd(value.d))*value.d
 paid(den)
 nums=[value.n*exact(den,value.d) for value in mul]
 common=zeroP
 for p in nums:common=common.gcd(p)
 assert common
 prim=[R(exact(p,common)) for p in nums]
 ret=pair_return(prim)
 assert all(not value for value in ret[1:])
 val=ret[0];ck(val)
 assert R(common)*val==R(den)*target
 retained,removed=strip_paid(val.n)
 if retained:
  lc=retained.coefficient(0);retained/=lc;removed*=lc
 assert retained*removed==val.n
 say('new_alpha_chi_fixed_four_by_four_original_pair',
  pair=[['EBe','EBo','N1'][k] for k in (i,j)],
  fixedSylvesterDegrees=[2,2],
  originalScalarNumerator=info(val.n),originalScalarDenominator=info(val.d),
  actualFourMultiplierCommon=info(common),
  retainedNecessaryChiWeightPolynomial=info(retained),
  allFourOriginalCoordinatesReturnedAfterCancellation=True,
  allLeadingCoefficientZeroFibersKept=True,
  noAlphaChiThetaOrNewHeadInverse=True,
  wholePhiExcluded=bool(retained) and int(retained.total_degree())==0)
say('new_correct_whole_Phi_alpha_chi_input_complete',
 originalRows=['EBe','EBo','N1'],fixedScalarTargets=3,
 exactDivisionReturns=divisionReturns,
 completeOriginalNSPSNotClaimed=True,
 noOldCofactorOrFiniteMatrixGateReplayed=True,
 noCoefficientPayloadSaved=True,ordinaryISPClaim=False)

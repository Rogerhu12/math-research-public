#!/usr/bin/env python3
"""NEW correct Phi: the WHOLE alpha=0 graph, after true t and f-u units.
No W weight identity, old equal-weight exclusion, old Phi head, or
B/C76 calculation is imported.  The free R identity plus Rw=-(u-1)A
pays m and theta ON THIS graph; f,t are pure weights, V remains free.
The raw original odd mean has V^2 head 4*u*theta/M^2, an actual paid
unit here.  Reduce the new complete N1/NS/PS in this monic two-dimensional
environment, then form three new same-point original scalar pairs.
120 seconds / 1 GiB; self-contained, small summaries only.
"""
import hashlib,json,resource,signal,time
from flint import fmpq_mpoly_ctx
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.alarm(120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','V'),'lex')
up,Qp,Vp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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
u,Q,V=R(up),R(Qp),R(Vp)
s=u-1;delta=1-Q;L=Q-2*s*(u-2);K=Q+4*s
ell=L/Q;a=1-ell;m=u-ell;theta=u-L
Mn=2*u*L-L*L-u*u*Q;M=Mn/Q;bc=M/(4*delta)
T0=-K;J0=2*u*(1-u)+L;P02=2*s*L
Ahead=4*s*s-Q
Rw=2*u*(1-u)-u*Q+(2*u-1)*L
assert Rw==-s*Ahead
# m and theta are not assumed units on the general Phi graph.
# The input note proves their complete alpha=0 payment from true units
# t, f-u, ell, delta, Rw; these formulas cover the whole current alpha face.
tt=-2*ell*delta/m
ff=u-ell*theta/(2*m)
eta=ff-u;alpha=4*delta*eta-theta*tt
assert alpha==0 and 2*m*eta+ell*theta==0
assert m*tt+2*ell*delta==0
W1=(T0+4*u*ff)/2
xx=(theta*V-m*W1)/M;yy=(ell*W1-u*V)/M
A1=2*ff-2*V+2*bc*tt
lam=(J0*ff+bc*Q*tt-Q*V-s*T0)/P02
Tr=T0*A1/(2*P02)-ell
ww=lam-1-Tr;GG=lam*P02+s*T0
Pf=T0*(J0-Q)
assert ell*xx+m*yy==V and u*xx+theta*yy==W1
assert Pf*ff+Q*P02*(ell+Tr)-GG*T0==0
R4=(16*delta*eta*(V-ff)+M*tt*tt+4*M*u*tt
    -4*theta*V*tt+2*m*T0*tt+8*m*u*ff*tt)
assert R4==0
paidP=(up*Qp*(1-Qp)*(up-1)*K.n*L.n*Mn.n*Ahead.n
       *(up*Qp-L.n)*theta.n)
def weight(p):return all(int(ex[2])==0 for ex in p.to_dict())
divisionReturns=0;den_seen=set()
def exact(p,g):
 global divisionReturns
 q,r=divmod(p,g);assert not r and q*g==p
 divisionReturns+=1;return q
def strip(p):
 assert weight(p)
 rem=p;removed=oneP
 if not rem:return rem,removed
 while int(rem.total_degree())>0:
  g=rem.gcd(paidP)
  if int(g.total_degree())<=0:break
  rem=exact(rem,g);removed*=g
 assert rem*removed==p;return rem,removed
def paid(p):
 assert p and weight(p)
 key=str(p)
 if key in den_seen:return
 rem,removed=strip(p);assert int(rem.total_degree())==0
 den_seen.add(key)
def ck(v):v=R(v);paid(v.d);return v
def vdegree(v):
 v=R(v);assert weight(v.d)
 return max((int(ex[2]) for ex in v.n.to_dict()),default=-1)
def vc(v,j):
 v=R(v);assert weight(v.d)
 p=ctx.from_dict({(ex[0],ex[1],0):c for ex,c in v.n.to_dict().items() if int(ex[2])==j})
 return R(p,v.d)
def info(p):
 out={'zero':not bool(p),'degrees':list(map(int,p.degrees())) if p else [-1]*3,
      'totalDegree':int(p.total_degree()) if p else -1,'terms':len(p.to_dict()),
      'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
 if p and len(p.to_dict())<=35:out['polynomial']=str(p)
 return out
for value in [ff,tt,W1,xx,yy,A1,lam,Tr]:
 ck(value)
# This factory always uses the original dual multiplication.  First use:
# the actual raw mean polynomial in V.  Second use: complete raw N/P
# in the NEW monic odd-mean quotient, with no free-module assumption.
def gram(lift):
 def e(c=0,d=0):return [lift(c),lift(d)]
 dd=lift(delta)
 def ea(v,w):return [v[0]+w[0],v[1]+w[1]]
 def en(v):return [-v[0],-v[1]]
 def es(v,w):return ea(v,en(w))
 def em(v,w):return [v[0]*w[0]+dd*v[1]*w[1],v[0]*w[1]+v[1]*w[0]]
 def ec(v,c):c=lift(c);return [c*v[0],c*v[1]]
 def cj(v):return [v[0],-v[1]]
 def esm(*vs):
  out=e()
  for v in vs:out=ea(out,v)
  return out
 bp=e(ell/2,m/(2*delta));cp=cj(bp)
 pPhys=e(1,1);qPhys=cj(pPhys)
 XP=e(xx,yy);YP=cj(XP)
 rP=es(es(XP,ec(pPhys,a)),ec(cp,tt));sP=cj(rP)
 rows=[[e(),e(),pPhys,qPhys],[e(),e(A1),rP,sP],
       [pPhys,rP,e(),e(tt)],[qPhys,sP,e(tt),e()]]
 one=[e(1),e(),e(1),e(1)]
 def vm(v,w):
  return [em(v[0],w[0]),ea(em(v[0],w[1]),em(v[1],w[0])),
          em(v[2],w[2]),em(v[3],w[3])]
 def va(v,w):return [ea(c,d) for c,d in zip(v,w)]
 def vs(c,v):return [em(c,d) for d in v]
 def tau(v):return esm(ec(v[0],a),v[1],em(bp,v[2]),em(cp,v[3]))
 def DK(v):return [tau(vm(row,v)) for row in rows]
 dv=DK(one);F2=tau(dv);kd=DK(dv);d2=vm(dv,dv)
 def mean(i):
  first=ec(tau(vm(rows[0],rows[1])),2) if i==1 else tau(vm(rows[i],rows[i]))
  return esm(first,ec(kd[i],-2),ec(d2[i],-2),ec(em(F2,dv[i]),2))
 def N4(v):
  tv=tau(v);v2=vm(v,v)
  return esm(ec(tau(vm(dv,v2)),2),en(em(F2,tau(v2))),
       ec(em(tv,tau(vm(dv,v))),-4),ec(em(F2,em(tv,tv)),2),tau(vm(v,DK(v))))
 def centered(v):return va(v,vs(en(tau(v)),one))
 def P2(v):
  cv0=centered(v);return tau(vm(vm(cv0,cv0),cv0))
 return locals()
raw=gram(R)
assert raw['F2']==[2*ff,R()]
E0=raw['mean'](0);E1=raw['mean'](1)
EB=raw['mean'](2);EC=raw['mean'](3)
assert E0==[R(),R()] and EC==[EB[0],-EB[1]]
EW=raw['ea'](raw['em'](raw['bp'],EB),raw['em'](raw['cp'],EC))
assert raw['es'](E1,EW)==[R(),R()]
EBe,EBo=EB
assert vdegree(EBo)==2 and vdegree(EBe)<=2
head=vc(EBo,2)
assert head==4*u*theta/(M*M)
paid(head.n);paid(head.d)
qcoeff=[vc(EBo,j)/head for j in range(3)]
assert qcoeff[2]==1
assert EBo==head*(qcoeff[0]+qcoeff[1]*V+V*V)
for value in qcoeff:ck(value)
say('new_correct_Phi_whole_alpha_zero_original_monic_V_two',
 wholeAlphaZeroChartCovered=True,
 mAndThetaPaidOnThisFaceByOriginalRAndTrueTAndFuUnits=True,
 noWWeightPaymentOrOldEqualWeightExclusionUsed=True,
 allRawMeanAndCoordinateReturns=True,
 exactOriginalOddMeanHead='4*u*theta/M^2',
 monicVQuadraticCoefficients=[{'n':info(v.n),'d':info(v.d)} for v in qcoeff[:2]],
 originalR4AndP1Returned=True)
jproducts=0;jreturns=0
class A2:
 def __init__(self,c0=0,c1=0):
  if isinstance(c0,A2):assert not c1;self.c0=c0.c0;self.c1=c0.c1;return
  self.c0=R(c0);self.c1=R(c1)
 def __bool__(self):return bool(self.c0 or self.c1)
 def __add__(self,z):z=A2(z);return A2(self.c0+z.c0,self.c1+z.c1)
 __radd__=__add__
 def __neg__(self):return A2(-self.c0,-self.c1)
 def __sub__(self,z):return self+-A2(z)
 def __rsub__(self,z):return A2(z)+-self
 def __mul__(self,z):
  global jproducts,jreturns
  z=A2(z);c0=self.c0*z.c0;c1=self.c0*z.c1+self.c1*z.c0;c2=self.c1*z.c1
  out=A2(c0-c2*qcoeff[0],c1-c2*qcoeff[1])
  assert out.c0+c2*qcoeff[0]==c0 and out.c1+c2*qcoeff[1]==c1
  jproducts+=1;jreturns+=2;return out
 __rmul__=__mul__
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=A2(1);p=self
  while n:
   if n&1:out=out*p
   n//=2
   if n:p=p*p
  return out
 def __eq__(self,z):z=A2(z);return self.c0==z.c0 and self.c1==z.c1
def lift(v):
 if isinstance(v,A2):return v
 v=R(v);assert weight(v.d)
 paid(v.d);out=A2()
 for j in range(vdegree(v),-1,-1):
  out=out*A2(0,1)+A2(vc(v,j))
 return out
alg=gram(lift)
assert alg['F2']==[lift(2*ff),A2()]
assert alg['mean'](3)==[alg['mean'](2)[0],-alg['mean'](2)[1]]
assert not alg['mean'](2)[1]
assert alg['mean'](2)[0]==lift(EBe)
def pure(v):assert not v[1];return v[0]
rows=alg['rows'];N4=alg['N4'];P2=alg['P2']
n0=N4(rows[0]);assert pure(n0)==2*lift(lam*P02)
nj=alg['es'](alg['es'](N4(alg['va'](rows[0],rows[1])),n0),N4(rows[1]))
N1=pure(nj)-lift(4*lam*ww*P02)
Al=2*lift(lam)**2-2*lift(lam)+1
Bl=4*lift(lam)**3-6*lift(lam)**2+3*lift(lam)-1
NS=pure(alg['ea'](alg['em'](alg['bp'],N4(rows[2])),
                   alg['em'](alg['cp'],N4(rows[3]))))-2*lift(lam*P02)*(lift(ell+2*Tr)+Al)
PS=pure(alg['ea'](alg['em'](alg['bp'],P2(rows[2])),
                   alg['em'](alg['cp'],P2(rows[3]))))-lift(P02)*(lift(ell+3*Tr)+3*Al+Bl)
valueRows=[lift(EBe),N1,NS,PS]
for row in valueRows:
 for coefficient in [row.c0,row.c1]:
  assert weight(coefficient.n);ck(coefficient)
say('new_alpha_zero_complete_original_value_two_columns',
 originalRows=['EBe','N1','NS','PS'],
 allOriginalOddRhoCoefficientsReturnedZero=True,
 completeRawN4P2Used=True,allCoefficientsOnlyPaidWeightDenominators=True,
 sourceQuotient='qV=EBo/(4*u*theta/M^2), actual monic polynomial quotient',
 actualProductCoefficientReturns=jreturns,
 rows=[[{'n':info(row.c0.n),'d':info(row.c0.d)},
        {'n':info(row.c1.n),'d':info(row.c1.d)}] for row in valueRows])
results=[]
for index,label in [(1,'N1'),(2,'NS'),(3,'PS')]:
 left=valueRows[0];right=valueRows[index]
 mu=right.c1;nu=-left.c1
 if not mu and not nu:
  say('new_alpha_zero_pair_constant_rows',pair=['EBe',label],
      first=info(left.c0.n),second=info(right.c0.n),wholeFaceExcluded=False)
  continue
 den=exact(mu.d,mu.d.gcd(nu.d))*nu.d
 paid(den)
 mp=mu.n*exact(den,mu.d);np=nu.n*exact(den,nu.d)
 common=mp.gcd(np);assert common
 muP=exact(mp,common);nuP=exact(np,common)
 scalar=R(muP)*left.c0+R(nuP)*right.c0
 assert R(muP)*left.c1+R(nuP)*right.c1==0
 assert A2(muP)*left+A2(nuP)*right==A2(scalar)
 ck(scalar)
 remaining,removed=strip(scalar.n)
 if remaining:
  c=remaining.coefficient(0);remaining/=c;removed*=c
 assert remaining*removed==scalar.n
 rec={'pair':['EBe',label],'actualMultiplierCommon':info(common),
      'scalarNumerator':info(scalar.n),'scalarDenominator':info(scalar.d),
      'retainedNecessaryWeightPolynomial':info(remaining),
      'bothOriginalCoordinatesReturned':True,
      'wholeActualMultiplierCommonZeroFaceKept':True,
      'onlyPaidWeightFactorsRemoved':True}
 results.append(rec);say('new_alpha_zero_original_weight_pair_return',**rec)
say('new_correct_Phi_alpha_zero_first_input_complete',
 wholeAlphaZeroExcluded=any(r['retainedNecessaryWeightPolynomial']['totalDegree']==0 for r in results),
 wholePhiExcluded=False,ordinaryISPClaim=False,
 originalMonicVEnvironmentPaidGloballyOnThisFace=True,
 allOtherWeightZeroFibersKept=True,
 exactWeightDivisionProducts=divisionReturns,actualQuotientProducts=jproducts,
 noOldBOrPhiScalarGateReplayed=True,noCoefficientCachePayloadSaved=True)

#!/usr/bin/env python3
"""NEW whole b0=0 on the current original W distinct-value graph.
On this entire face Astar=4*u*Q-J is a unit: otherwise b0=0 forces
lambda=3/2, already independently excluded in this W graph.  This
does NOT pay Astar on the complementary W graph.
Recover T=-u*Q*ell*(3-2*lambda)/Astar.  Original C4 and D!=0 give
the true lambda quadratic 2*aDelta/ell; retain original R6 of degree6.
Only NEW fixed 8x8 lambda Sylvester, paid weight stripping and complete
QQ factorization.  All lambda heads remain; no native/old target replay.
180 seconds /4 GiB; source is self-contained. Small summaries only.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k','lam'),'lex')
ep,kp,lp=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
def polynomial(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=polynomial(n);d=O if d is None else polynomial(d);assert d
  if not n:self.n=Z;self.d=O;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  s=d.coefficient(0);self.n=n/s;self.d=d/s
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=R(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=self.d/g;b=v.d/g
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R((self.n/g)*(v.n/h),(self.d/h)*(v.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);assert v
  return self*R(v.d,v.n,False)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return R(self.n**n,self.d**n,False)
 def __eq__(self,v):
  v=R(v);return self.n*v.d==v.n*self.d
e,k,lam=R(ep),R(kp),R(lp)
u=e+1;Q=e*k;Vbar=u*k+2;delta=1-Q
ell=u*((k+2)**2-2*e*k)/(k*Vbar)
m=u-ell;V2=2*u-ell*Q
M=ell*V2-u*u;bc=M/(4*delta)
T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
P02=(2-3*u)*V2-Q*u+2*u**3
Ast=4*u*Q-J;Cst=Ast*m*m+J*delta*ell*ell
assert M==ell*ell*delta-m*m
assert M*Ast+Cst==4*u*Q*delta*ell*ell
kap=u*Q*ell/Ast
n=2*lam-1;cval=3-2*lam
T=-kap*cval
Aval=2*lam*lam-2*lam+1
Bval=4*lam**3-6*lam*lam+3*lam-1
D=ell*Aval-T*T
K=ell*ell*Bval-3*ell*Aval*T+2*T**3
ad=(M*ell*ell*Q*(3-4*lam)+M*Ast*T*T
    +2*M*u*Q*cval*ell*T+D*Cst)
b0=2*m*(Ast*T+u*Q*cval*ell);bd=M*b0
assert not b0 and not bd
C4=2*m*D*ad+K*bd
assert C4==2*m*D*ad
quad=2*ad/ell
qcompact=(2*M*ell*Q*(1-2*n)+Cst*(n*n+1)
          -8*u*Q*delta*ell*kap*kap*(n-2)**2)
assert quad==qcompact
R6=M*K*K-4*m*m*D**3

# These are the already published CURRENT W pure-weight supports.
# Only Astar is newly paid, and only on this entire b0=0 branch.
Hold=4*ep*kp-kp*kp-4*kp-8
J19=(16*ep**4*kp**3-8*ep**3*kp**4-16*ep**3*kp**3-96*ep**3*kp**2
 -ep**2*kp**5-8*ep**2*kp**4+24*ep**2*kp**3+64*ep**2*kp**2+192*ep**2*kp
 -2*ep*kp**5-14*ep*kp**4-12*ep*kp**3-128*ep
 -kp**5-10*kp**4-40*kp**3-104*kp**2-160*kp-128)
C9=(4*ep*ep*kp*kp-ep*(kp**4+9*kp**3+20*kp*kp+16*kp)
    +kp**3+10*kp*kp+24*kp+16)
paid_atoms=[('e',ep),('k',kp),('u',ep+1),('delta',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),('P02',P02.n),
 ('M',M.n),('whole_k_plus_one',kp+1),('whole_H_old',Hold),
 ('whole_equal_weights_k_plus_two',kp+2),('whole_ell_zero',ell.n),
 ('whole_equal_weights_m',m.n),('whole_original_J19',J19),
 ('whole_original_C9',C9),('whole_original_Lhalf', (2*ell-1).n),
 ('Astar_paid_only_on_entire_b0_zero',Ast.n)]
statistics={'exactDivisionProducts':0,'bareissProducts':0,
            'paidSupportProducts':0,'factorProductReturns':0}
def weight(p):return all(int(ex[2])==0 for ex in p.to_dict())
def exact(p,g):
 q,r=divmod(p,g);assert not r and q*g==p
 statistics['exactDivisionProducts']+=1;return q
def strip(p):
 before=p;removed=O;history=[]
 if not p:return p,removed,history
 for label,atom in paid_atoms:
  assert atom and weight(atom)
  layers=0
  while p:
   g=p.gcd(atom)
   if int(g.total_degree())==0:break
   p=exact(p,g);removed*=g;layers+=1
   statistics['paidSupportProducts']+=1
  if layers:history.append({'paidSupport':label,'gcdLayers':layers})
 assert p*removed==before
 return p,removed,history
paid_seen=set()
def paid(p):
 assert p and weight(p)
 key=str(p)
 if key in paid_seen:return
 r,_,_=strip(p);assert r and int(r.total_degree())==0
 paid_seen.add(key)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return dict(zero=not bool(p),degrees_e_k_lambda=list(map(int,p.degrees())) if p else [-1]*3,
             totalDegree=int(p.total_degree()) if p else -1,
             terms=len(data),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def ldeg(p):return max((int(ex[2]) for ex in p.to_dict()),default=-1)
for rr in [ell,m,M,P02,Ast,kap,T,D,K,quad,R6]:
 paid(rr.d)
assert ldeg(quad.n)<=2 and ldeg(R6.n)<=6
inputs=[]
for label,rr,cap in [('original_aDelta_quadratic',quad,2),
                     ('original_R6',R6,6)]:
 pp,removed,hist=strip(rr.n)
 assert pp and ldeg(pp)<=cap
 scalar=pp.coefficient(0);pp/=scalar
 assert pp*scalar*removed==rr.n
 inputs.append(pp)
 say('new_entire_b0_zero_original_lambda_input',
     label=label,raw=profile(rr.n),necessary=profile(pp),
     fullClearingProductReturned=True,onlyPaidSupportRemoval=hist,
     coefficientDenominatorsPaidOnThisWholeBranch=True,
     allLambdaLeadingZeroFibersKept=True)
aa,bb=inputs
say('new_entire_b0_zero_same_value_recovery',
 AstarPaidOnlyOnThisFace=True,
 AstarZeroOriginalReason='b0=0 and Astar=0 force lambda=3/2; its whole current W fiber was independently excluded',
 uniqueT='-u*Q*ell*(3-2*lambda)/Astar',
 originalB0AndC4ProductsReturned=True,
 quadraticIdentity='2*aDelta/ell=2*M*ell*Q*(1-2*n)+Cstar*(n^2+1)-8*u*Q*delta*ell*kappa^2*(n-2)^2, n=2*lambda-1',
 originalPhysicalDNonzeroUsedOnlyToInfer_aDeltaZero=True,
 R6IsFullOriginalNecessaryValueEquation=True,
 noNativeGramOrPreviousQuarticPairRebuilt=True)

# Fixed degree bounds 2,6: every finite common lambda root gives a
# nonzero Vandermonde kernel vector even if one or both heads vanish.
def lc(p,j):
 return ctx.from_dict({(ex[0],ex[1],0):c for ex,c in p.to_dict().items() if int(ex[2])==j})
matrix=[]
for pp,degree,count in [(aa,2,6),(bb,6,2)]:
 coeff=[lc(pp,j) for j in range(degree+1)]
 assert sum((v*lp**j for j,v in enumerate(coeff)),Z)==pp
 for shift in range(count):
  row=[Z]*8
  for j,v in enumerate(coeff):row[j+shift]=v
  assert sum((v*lp**j for j,v in enumerate(row)),Z)==pp*lp**shift
  matrix.append(row)
assert len(matrix)==8 and all(len(row)==8 for row in matrix)
say('new_entire_b0_zero_fixed_lambda_eight_defined',
 fixedSize=8,actualDegrees=[ldeg(aa),ldeg(bb)],
 allOriginalFixedRowsReturned=True,noLambdaHeadInverted=True)
def det_bareiss(original):
 A=[row[:] for row in original];previous=O;sgn=1
 for k0 in range(7):
  pivotrow=next((i for i in range(k0,8) if A[i][k0]),None)
  if pivotrow is None:return Z
  if pivotrow!=k0:A[k0],A[pivotrow]=A[pivotrow],A[k0];sgn=-sgn
  pivot=A[k0][k0]
  for i in range(k0+1,8):
   for j in range(k0+1,8):
    numerator=pivot*A[i][j]-A[i][k0]*A[k0][j]
    A[i][j]=exact(numerator,previous)
    statistics['bareissProducts']+=1
   A[i][k0]=Z
  previous=pivot
  say('new_entire_b0_zero_fixed_lambda_eight_complete_step',
      step=k0,pivot=profile(pivot),
      exactBareissProducts=statistics['bareissProducts'],
      allIntermediatePivotZerosKeptByPolynomialIdentity=True)
 return sgn*A[7][7]
raw=det_bareiss(matrix)
assert weight(raw)
say('new_entire_b0_zero_original_weight_resultant',
 result=profile(raw),allFiniteCommonLambdaRootsCovered=True,
 allLambdaLeadingZerosKept=True,noOriginalBranchExclusionYet=True)
if not raw:
 say('new_entire_b0_zero_resultant_identically_zero',
     wholeB0FaceExcluded=False,noNewWeightCurveClaim=True,statistics=statistics)
else:
 rem,removed,hist=strip(raw)
 scalar=rem.coefficient(0);rem/=scalar
 assert rem*scalar*removed==raw
 say('new_entire_b0_zero_retained_original_weight_curve',
     necessary=profile(rem),onlyPaidSupportRemoval=hist,
     fullOriginalClearingProductReturned=True,
     allUnpaidWeightFactorsKept=True,
     wholeB0FaceExcluded=int(rem.total_degree())==0)
 content,factors=rem.factor();back=ctx.constant(content);records=[]
 for ff,exponent in factors:
  back*=ff**int(exponent)
  records.append({'multiplicity':int(exponent),'factor':profile(ff)})
 assert back==rem;statistics['factorProductReturns']+=1
 say('new_entire_b0_zero_complete_QQ_weight_factorization',
     factors=records,completeQQFactorProductReturned=True,
     noMultivariateGcdOrModularEmptinessInference=True,
     allUnpaidFactorZeroFibersRemain=int(rem.total_degree())>0,
     wholeB0FaceExcluded=int(rem.total_degree())==0)
say('new_entire_b0_zero_first_input_complete',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    statistics=statistics,allAstarZeroCasesAlreadyCoveredOnThisFace=True,
    noAstarPaymentOutsideB0Face=True,
    currentWComplementStillRetained=True,ordinaryISPClaim=False,
    noCoefficientCachePayloadOrChunksSaved=True,
    peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)

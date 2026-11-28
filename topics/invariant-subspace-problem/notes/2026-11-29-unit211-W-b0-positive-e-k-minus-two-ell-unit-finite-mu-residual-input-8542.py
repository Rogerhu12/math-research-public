#!/usr/bin/env python3
"""NEW p=1009 residual input for W/b0, v(e)>0, k -> -2, ell unit.
Only the finite-mu generic residue model is tested.  L=0,1/2,1,3
are excluded from THIS input by separate original paper branches.
Two NEW fixed mu Sylvesters (2,6) and (2,5), followed by their actual
Fp[L] Bezout.  All fixed-degree drops and intermediate pivot zero
loci are retained by complete polynomial coordinate returns.
No original two-variable curve/resultant/initial-ideal is rebuilt.
Self-contained, 120 seconds / 1 GiB.  No dispatch or output cache.
"""
import hashlib,json,resource,signal,time
from flint import fmpq_mpoly_ctx,nmod_poly
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
P=1009
STAT={'qqOriginalReturns':0,'exactPolynomialProducts':0,
      'sylvesterCoordinates':0,'newThreeSourceCoordinates':0,
      'univariateBezoutProducts':0,'paidSupportProducts':0}
def say(stage,**d):
 d.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(d,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('L','mu'),'lex')
lp,mp=ctx.gens();ZZ=ctx.constant(0);OO=ctx.constant(1)
def pol(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
class R:
 def __init__(self,n=0,d=None):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=pol(n);d=OO if d is None else pol(d);assert d
  if not n:self.n=ZZ;self.d=OO;return
  g=n.gcd(d);n=n/g;d=d/g
  c=d.coefficient(0);self.n=n/c;self.d=d/c
 def __bool__(self):return bool(self.n)
 def __add__(self,x):
  x=R(x);return R(self.n*x.d+x.n*self.d,self.d*x.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d)
 def __sub__(self,x):return self+-R(x)
 def __rsub__(self,x):return R(x)+-self
 def __mul__(self,x):
  x=R(x);return R(self.n*x.n,self.d*x.d)
 __rmul__=__mul__
 def __truediv__(self,x):
  x=R(x);assert x;return R(self.n*x.d,self.d*x.n)
 def __rtruediv__(self,x):return R(x)/self
 def __pow__(self,j):
  assert isinstance(j,int) and j>=0
  return R(self.n**j,self.d**j)
 def __eq__(self,x):
  x=R(x);return self.n*x.d==x.n*self.d
def ret(a,b):
 assert a==b;STAT['qqOriginalReturns']+=1
L,mu=R(lp),R(mp);lam=(mu+3)/2
H=3-L;m=1-L;M=2*L-1;bc=M/4
T=L*mu/H;Ac=(mu*mu+4*mu+5)/2
Bc=(mu**3+6*mu*mu+12*mu+7)/2
D=L*Ac-T*T;K=L*L*Bc-3*L*Ac*T+2*T**3
B=6*L*L-7*L+3
q=4*L*T*T-B*Ac+L*M*(2*mu+3)
# Actual q2/e is 4*q in this residual chart.
ret((-4*B*Ac-4*L*M*(3-4*lam)+16*L*T*T)/4,q)
ret((L-3)*T,-L*mu)
R6=M*K*K-4*m*m*D**3
# These are the f-constant coefficients of the COMPLETE original NV.
# They do not impose physical f=0.
Vs=L+T-lam
bt=Vs+L*lam
ys=-Vs/M;xs=Vs/M;w=lam-1-T;cval=-mu
A1s=2*L*lam
ret(A1s,-2*Vs+2*bt)
z1=-2*(L*cval+2*T)*ys-2*L*w+4*m*T*bt/M
z2=-2*L*lam+4*m*Vs/M
ret(z2,2*(L*xs-m*ys-bt))
Z0=2*(L*cval+T)*(L*w+Vs*T)+2*bt*T*T
Zraw=(L*L*A1s+2*L*w*(L*cval+T)
      +2*Vs*(L*L+L*cval*T+T*T)+2*bt*(T*T-L*L))
ret(Z0,Zraw)
N5=2*m*D*(Z0+D*z2)+M*K*z1
raw=[q,R6,N5]
atoms=[lp,lp-1,2*lp-1,lp-3]
for f in raw:
 assert all(int(ex[1])==0 for ex in f.d.to_dict())
 d=f.d
 for a in atoms:
  while True:
   g=d.gcd(a)
   if int(g.total_degree())==0:break
   nd,rr=divmod(d,g);assert not rr and nd*g==d;d=nd
   STAT['paidSupportProducts']+=1
 assert int(d.total_degree())==0
def qprofile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 b=json.dumps(data,separators=(',',':')).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1,-1],
         'terms':len(data),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def modq(x):
 s=str(x)
 if '/' in s:
  a,b=s.split('/');b=int(b)%P;assert b
  return int(a)%P*pow(b,-1,P)%P
 return int(s)%P
def np(c=0):
 if isinstance(c,nmod_poly):return c
 if isinstance(c,list):return nmod_poly(c,P)
 return nmod_poly([int(c)%P],P)
Z=np(0);O=np(1);X=np([0,1])
def trim(v):
 v=list(v)
 while v and not v[-1]:v.pop()
 return v
def add(a,b):
 return trim([(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z)
              for i in range(max(len(a),len(b)))])
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 if not a or not b:return []
 v=[Z for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]=v[i+j]+x*y
 return trim(v)
def scale(a,c):return trim([x*c for x in a])
def shift(a,n):return [Z]*n+list(a) if a else []
def const(a):return [] if not a else [a]
def convert(p):
 out=[]
 for ex,c in p.to_dict().items():
  i,j=map(int,ex)
  while len(out)<=j:out.append(Z)
  v=[0]*(i+1);v[i]=modq(c)
  out[j]=out[j]+np(v)
 return trim(out)
F=[convert(f.n) for f in raw]
for f in raw:convert(f.d)  # every denominator coefficient is p-integral
assert len(F[0])<=3 and len(F[1])<=7 and len(F[2])<=6
def profile(p):
 if isinstance(p,nmod_poly):data=list(map(int,p.coeffs()))
 else:data=[list(map(int,x.coeffs())) for x in p]
 b=json.dumps(data,separators=(',',':')).encode()
 return {'degree':int(p.degree()) if isinstance(p,nmod_poly) else len(p)-1,
         'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
say('new_finite_mu_complete_original_residual_model',
 parameterPrime=P,finiteMuOnly=True,
 excludedResidueSupports=['L','L-1','2L-1','L-3'],
 qqNumerators=[qprofile(f.n) for f in raw],
 qqDenominators=[qprofile(f.d) for f in raw],
 modOriginalNumerators=[profile(f) for f in F],
 completeOriginalNV=True,noPhysicalFZero=True,
 noOldProjectionOrInitialIdeal=True)
def exact(a,b):
 q,r=divmod(a,b)
 assert not r and q*b==a
 STAT['exactPolynomialProducts']+=1;return q
def fixed_resultant(first,second,dp,dq,label):
 assert len(first)<=dp+1 and len(second)<=dq+1
 rows=[shift(first,j) for j in range(dq)]+[shift(second,j) for j in range(dp)]
 n=dp+dq;rows=[v+[Z]*(n-len(v)) for v in rows]
 # Columns of A are the actual polynomial multiples.
 A=[[rows[j][i] for j in range(n)] for i in range(n)]
 W=[list(A[i])+[O if i==0 else Z] for i in range(n)]
 previous=O;sgn=1
 for k in range(n-1):
  pivot=next((i for i in range(k,n) if W[i][k]),None)
  if pivot is None:
   say('new_fixed_resultant_identically_zero',label=label,step=k)
   return None
  if pivot!=k:W[k],W[pivot]=W[pivot],W[k];sgn=-sgn
  pk=W[k][k]
  for i in range(k+1,n):
   aik=W[i][k]
   for j in range(k+1,n+1):
    W[i][j]=exact(pk*W[i][j]-aik*W[k][j],previous)
   W[i][k]=Z
  previous=pk
 if not W[-1][-2]:
  say('new_fixed_resultant_identically_zero',label=label,step=n-1)
  return None
 det=W[-1][-2]*sgn
 coefficients=[Z]*n
 for i in range(n-1,-1,-1):
  v=det*W[i][-1]
  for j in range(i+1,n):v=v-W[i][j]*coefficients[j]
  coefficients[i]=exact(v,W[i][i])
 for i in range(n):
  got=sum((A[i][j]*coefficients[j] for j in range(n)),Z)
  assert got==(det if i==0 else Z)
  STAT['sylvesterCoordinates']+=1
 left=trim(coefficients[:dq]);right=trim(coefficients[dq:])
 assert add(mul(left,first),mul(right,second))==const(det)
 STAT['newThreeSourceCoordinates']+=n
 say('new_fixed_mu_resultant_complete_original_return',
     label=label,capacities=[dp,dq],matrixOrder=n,
     determinant=profile(det),fullPolynomialCoordinates=True,
     allLeadingDropAndPivotZeroFacesRetained=True)
 return det,left,right
A=fixed_resultant(F[0],F[1],2,6,'q2_R6')
B=fixed_resultant(F[0],F[2],2,5,'q2_complete_N5')
if A is None or B is None:
 say('new_target_not_returned',reason='a fixed determinant is identically zero',
     entireResidualModelRetained=True,statistics=STAT)
 raise SystemExit(0)
ga,sa,ta=A[0].xgcd(B[0])
assert sa*A[0]+ta*B[0]==ga
STAT['univariateBezoutProducts']+=1
tags=[add(scale(A[1],sa),scale(B[1],ta)),scale(A[2],sa),scale(B[2],ta)]
got=[]
for i in range(3):got=add(got,mul(tags[i],F[i]))
assert got==const(ga)
STAT['newThreeSourceCoordinates']+=max(1,len(got))
say('new_three_original_residual_Bezout',
 gcd=profile(ga),completeThreeOriginalNumeratorsReturned=True)
U=X*(X-1)*(2*X-1)*(X-3)
left=ga;removed=O;layers=0
while left:
 gg=left.gcd(U)
 if int(gg.degree())==0:break
 left=exact(left,gg);removed*=gg;layers+=1
assert removed*left==ga
if int(left.degree())==0:
 power=max(1,int(ga.degree()))
 target=U**power
 quotient=exact(target,ga)
 final=[scale(t,quotient) for t in tags]
 got=[]
 for i in range(3):got=add(got,mul(final[i],F[i]))
 assert got==const(target)
 STAT['newThreeSourceCoordinates']+=max(1,len(got))
 say('new_generic_finite_mu_residue_exclusion_complete',
     paidUnitTargetPower=power,paidUnitTarget=profile(target),
     fullThreeOriginalSourceCoordinates=True,
     onlyP1009ResidueModel=True,noQQEmptyLift=True,
     specialLZeroOneHalfOneThreeNotIncluded=True,statistics=STAT)
else:
 say('new_generic_finite_mu_unpaid_residue_cover',
     remaining=profile(left),paidSupportGcdLayers=layers,
     fullResidualZeroSetRetained=True,
     noEmptyConclusion=True,statistics=STAT)

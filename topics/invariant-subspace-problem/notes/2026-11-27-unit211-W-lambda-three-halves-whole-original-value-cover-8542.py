#!/usr/bin/env python3
"""Whole current W, lambda=3/2: new fixed six-column original value cover.
No geometric root or unpaid leading coefficient is selected.  The fixed
Sylvester cofactor is multiplied against all original columns.  Only paid
weight factors may be removed.  No whole-W exclusion is claimed.
180 seconds / 4 GiB.  Self-contained python-flint exact QQ computation.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
start=time.perf_counter();signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k'),'lex')
ep,kp=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
def poly(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
class C:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,C):self.n=n.n;self.d=n.d;return
  n=poly(n);d=one if d is None else poly(d);assert d
  if not n:self.n=zero;self.d=one;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __neg__(self):return C(-self.n,self.d,False)
 def __add__(self,v):
  v=C(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=self.d/g;b=v.d/g
  return C(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-C(v)
 def __rsub__(self,v):return C(v)+-self
 def __mul__(self,v):
  v=C(v)
  if not self or not v:return C()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return C((self.n/g)*(v.n/h),(self.d/h)*(v.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,v):v=C(v);assert v;return self*C(v.d,v.n,False)
 def __rtruediv__(self,v):return C(v)/self
 def __pow__(self,n):
  return C(self.d**(-n),self.n**(-n),False) if n<0 else C(self.n**n,self.d**n,False)
 def __eq__(self,v):v=C(v);return self.n*v.d==v.n*self.d
 def data(self):
  return dict(n=[[list(map(int,m)),str(c)] for m,c in sorted(self.n.to_dict().items())],
              d=[[list(map(int,m)),str(c)] for m,c in sorted(self.d.to_dict().items())])

e,k=C(ep),C(kp);u=e+1;Q=e*k;d=1-Q;V=u*k+2
ell=u*((k+2)**2-2*e*k)/(k*V);m=u-ell
M=ell*ell*d-m*m;T0=2*u-ell*Q-2*u*u
J=2*u*(1-u)+ell*Q;Phi=T0+4*e+Q
P02=(2-3*u)*(2*u-ell*Q)-Q*u+2*u**3
bc=M/(4*d);Pf=T0*(J-Q)
assert Phi*(J-2*u*Q)==Pf
assert 2*e*(J-u*Q)==u*Q*Phi
atoms=[e,k,u,Q,d,V,ell,m,M,Phi,P02,bc,2*e+1,k+1,k+2,k+4,T0,J-Q]
atom_names=['e','k','u','Q','d','V','ell','m','M','Phi','P02','bc','2e+1','k+1','k+2','k+4','T0','J-Q']
den_checked=set()
def check_paid_den(x):
 x=C(x);key=str(x.d)
 if key in den_checked:return
 rem=x.d
 for atom in atoms:
  while True:
   g=rem.gcd(atom.n)
   if g.total_degree()==0:break
   before=rem;rem=rem/g;assert rem*g==before
 assert rem.total_degree()==0,'unpaid denominator'
 den_checked.add(key)
def trim(v):
 v=[C(c) for c in v]
 while v and not v[-1]:v.pop()
 return v
def add(a,b):
 c=[C() for _ in range(max(len(a),len(b)))]
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return trim(c)
def scale(a,c):return trim([x*c for x in a])
def mul(a,b):
 if not a or not b:return []
 c=[C() for _ in range(len(a)+len(b)-1)]
 for i,v in enumerate(a):
  for j,w in enumerate(b):c[i+j]+=v*w
 return trim(c)
def sub(a,b):return add(a,scale(b,-1))
def power(a,n):
 out=[C(1)]
 for _ in range(n):out=mul(out,a)
 return out
lam=C(fmpq(3,2));Al=2*lam*lam-2*lam+1;Bl=4*lam**3-6*lam*lam+3*lam-1
assert Al==fmpq(5,2) and Bl==fmpq(7,2)
Ts=[C(),C(1)];D=[ell*Al,C(),C(-1)]
K=[ell*ell*Bl,-3*ell*Al,C(),C(2)]
astar=4*u*Q-J;cstar=astar*m*m+J*d*ell*ell
ad=add([M*ell*ell*Q*(3-4*lam)],add(scale(power(Ts,2),M*astar),scale(D,cstar)))
bd=scale(Ts,2*M*m*astar)
R4=sub(scale(power(ad,2),M),mul(D,power(bd,2)))
C4=add(scale(mul(D,ad),2*m),mul(K,bd))
alpha2=-2*ell*Al-M*(3-4*lam)/(4*u*d)
alpha1=M*astar*Bl/(4*u*Q*d)
alpha0=cstar*Al*Al/(4*u*Q*d)+M*ell*(3-4*lam)*Al/(4*u*d)
qT=[alpha0,alpha1,alpha2,C(),C(1)]
assert sub(qT,scale(C4,1/(8*m*u*Q*ell*ell*d)))==[]
rT=sub(R4,scale(qT,R4[4]));assert len(rT)<=3 and rT
for f in [qT,rT,R4,C4]:
 for c in f:check_paid_den(c)
def pprofile(po,include=True):
 dd=[[list(map(int,mm)),str(cf)] for mm,cf in sorted(po.to_dict().items())]
 bb=json.dumps(dd,separators=(',',':')).encode()
 r=dict(terms=len(dd),degrees=list(map(int,po.degrees())),totalDegree=int(po.total_degree()),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if include and len(bb)<=8192:r['coefficients']=dd
 return r
def clear(f):
 den=one
 for c in f:den=den*c.d/den.gcd(c.d)
 out=[c.n*(den/c.d) for c in f]
 for a,c in zip(out,f):assert C(a,den)==c
 check_paid_den(C(1,den));return out,den
qt,qden=clear(qT);rt,rden=clear(rT)
assert len(qt)==5 and len(rt)<=3
# Include every degree drop: the 6 fixed rows are actual polynomial multiples.
rows=[]
for sh in range(2):rows.append([zero]*sh+qt+[zero]*(1-sh))
for sh in range(4):rows.append([zero]*sh+rt+[zero]*(6-sh-len(rt)))
assert len(rows)==6 and all(len(r)==6 for r in rows)
def det(mat):
 a=[r[:] for r in mat];n=len(a)
 if not n:return one
 prev=one;sgn=1
 for j in range(n-1):
  h=next((i for i in range(j,n) if a[i][j]),None)
  if h is None:return zero
  if h!=j:a[h],a[j]=a[j],a[h];sgn=-sgn
  pv=a[j][j]
  for i in range(j+1,n):
   for k0 in range(j+1,n):
    num=pv*a[i][k0]-a[i][j]*a[j][k0]
    nxt=num/prev;assert nxt*prev==num
    a[i][k0]=nxt
   a[i][j]=zero
  prev=pv
 return a[-1][-1]*sgn
det0=det(rows);assert det0
cof=[]
for i in range(6):
 mm=[[rows[j][k0] for k0 in range(1,6)] for j in range(6) if j!=i]
 cof.append(det(mm)*((-1)**i))
assert all(sum((cof[i]*rows[i][j] for i in range(6)),zero)==(det0 if j==0 else zero) for j in range(6))
# The cofactor above is an original polynomial-combination certificate.
# Strip only separately paid weight atoms, with an exact product identity.
remaining=det0;removed=one;paid_records=[]
for name,at in zip(atom_names,atoms):
 count=0;degree=0
 while True:
  g=remaining.gcd(at.n)
  if g.total_degree()==0:break
  before=remaining;remaining=remaining/g;assert remaining*g==before
  removed*=g;degree+=int(g.total_degree());count+=1
 if count:paid_records.append(dict(atom=name,passes=count,totalDegreeRemoved=degree))
assert removed*remaining==det0
lc=remaining.coefficient(0);remaining=remaining/lc;removed*=lc
assert removed*remaining==det0
content,factors=remaining.factor()
product=ctx.constant(content)
factor_records=[]
for fac,mult in factors:
 product*=fac**mult
 factor_records.append(dict(multiplicity=int(mult),factor=pprofile(fac)))
assert product==remaining
# Independent same-root value-ratio form; no use of this chart in the cover.
# At lambda=3/2, Sval=2*v0 is a physical unit, s is a physical unit,
# z=s/v0 !=0 and A_z*v0^2=3Q.  Clear the common paid u*e/V.
zc=fmpq_mpoly_ctx.get(('e','k','z'),'lex');ze,zk,zz=zc.gens()
def lift(po):
 out=zc.constant(0)
 for mm,cf in po.to_dict().items():out+=cf*ze**int(mm[0])*zk**int(mm[1])
 return out
def clear_z(cs):
 den=one
 for c in cs:den=den*c.d/den.gcd(c.d)
 out=zc.constant(0)
 for j,c in enumerate(cs):out+=lift(c.n*(den/c.d))*zz**j
 return out,den
general=[6*Q*ell-5*astar,-12*Q*m,d*(6*Q*ell-5*J)]
fac=u*e/V;normalized=[c/fac for c in general]
ratio,ratio_den=clear_z(normalized);assert ratio_den==one
ratio_expected=(1-ze*zk)*(zk*zk+(8*ze+14)*zk+24)*zz**2-12*(zk+2)*(ze*zk-2)*zz-(20*ze+9)*zk**2-(32*ze+6)*zk+24
assert ratio==ratio_expected
e2part=sum((cf*zk**int(mm[1])*zz**int(mm[2]) for mm,cf in ratio.to_dict().items() if mm[0]==2),zc.constant(0))
assert e2part==-8*zk**2*zz**2 and all(mm[0]<=2 for mm in ratio.to_dict())
trace_data=[pprofile(c,False) for c in cof]
say(stage='W_lambda_three_halves_entire_original_value_cover',
 lambdaNumerator=3,lambdaDenominator=2,
 qTDegree=4,rTDegree=len(rT)-1,
 qTMonicAndOriginalC4IdentityActuallyVerified=True,
 fixedOriginalMatrixShape=[6,6],rowLabels=['qT','T*qT','rT','T*rT','T^2*rT','T^3*rT'],
 allSixOriginalCofactorColumnsActuallyReturned=True,
 allLeadingDegreeDropsRetained=True,noGeometricInverse=True,
 rawDeterminant=pprofile(det0,False),paidFactorsRemoved=paid_records,
 remainingNecessaryWeightPolynomial=pprofile(remaining),completeQQFactorization=factor_records,
 cofactorProfiles=trace_data,distinctPaidDenominatorsChecked=len(den_checked),
 ratioIdentity=dict(exactlyVerified=True,polynomial=str(ratio),eLeading='-8*k^2*z^2',
 physicalZNonzeroNeededOnlyForFutureMonicEChart=True,
 signConvention='z=s/v0, m=u-ell, coefficient of z is -12*(k+2)*(e*k-2)'),
 valueSqrtOrRootNotSelected=True,wholeLambdaFiberExcluded=False,
 largeCachesWritten=False,sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

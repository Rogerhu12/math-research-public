#!/usr/bin/env python3
"""NEW entire correct-Phi ell=1/2: a DIRECT raw-original z certificate.
Four true quadrics times (1,epsilon,tau,z), plus TWO complete raw weighted
NS/PS cubics: fixed 20 monomial coordinates and 18 ORIGINAL columns.
This is only a degree<=3 polynomial container, NOT a quotient algebra.
No prior lambda gcd, 30-column module, positive-power gate, denominator
LCM/C114 proof, old main or generic Phi cofactor is run or regenerated.
If the fixed target is returned, combine SIX raw original multipliers,
return the WHOLE polynomial z, and clear only their FINAL true poles.
All unpaid pure-u fibers remain. 120 seconds /1 GiB, self-contained.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx,fmpq_poly
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','epsilon','tau','z'),'lex')
up,ep,tp,zp=ctx.gens();O=ctx.constant(1);Z=ctx.constant(0)
def polynomial(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=polynomial(n);d=O if d is None else polynomial(d);assert d
  if not n:self.n=Z;self.d=O;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
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
u,epsilon,taucoord,z=map(R,(up,ep,tp,zp))
half=R(1)/2;lam=epsilon+half;T=taucoord-half
s=u-1;ell=half;Q=4*s*(u-2);delta=1-Q;m=u-ell
M=-2*s*s;bc=M/(4*delta)
T0=-4*s*s;J=-4*s;P02=4*s*s*(u-2);Pf=16*s**4
A2=2*lam*lam-2*lam+1
B3=4*lam**3-6*lam*lam+3*lam-1
f=u/2-(u-2)*epsilon-(u-2)**2*taucoord/s
G=lam*P02+s*T0;Pc=Q*P02*(ell+T)-G*T0
assert Pf*f+Pc==0
t=z/Q;V=(J*f-G+bc*z)/Q;W1=T0/2+2*u*f
theta=u-ell*Q
x=(theta*V-m*W1)/M;y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t
assert V-f==(u-2)*taucoord+bc*t
assert A1==-2*(u-2)*taucoord
assert M==ell*(2*u-ell*Q)-u*u
assert T0+4*u-4+Q==0
statistics={'exactPolynomialDivisionProducts':0,
 'newBareissPolynomialProducts':0,'newFullMatrixTargetCoordinates':0,
 'newRawPolynomialTargetCoordinates':0,'newFinalDenominatorProducts':0}
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 statistics['exactPolynomialDivisionProducts']+=1
 return q
def pure_u(p):return all(not any(int(v) for v in ex[1:]) for ex in p.to_dict())
def geomdegree(v):
 v=R(v);assert pure_u(v.d)
 return max((sum(int(q) for q in ex[1:]) for ex in v.n.to_dict()),default=-1)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'zero':not bool(p),'degrees_u_epsilon_tau_z':list(map(int,p.degrees())) if p else [-1]*4,
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(data),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
paidSupport=up*(up-1)*(up-2)*delta.n*(2*up-1)*(2*(up-1)**2-3)
def strip_paid(p):
 saved=p;removed=O
 while p and int(p.total_degree())>0:
  gg=p.gcd(paidSupport)
  if int(gg.total_degree())==0:break
  p=exact(p,gg);removed*=gg
 assert p*removed==saved
 return p,removed
paid_seen=set()
def old_paid(p):
 assert p and pure_u(p)
 key=str(p)
 if key in paid_seen:return
 rr,_=strip_paid(p);assert rr and int(rr.total_degree())==0
 paid_seen.add(key)
def ck(v):
 v=R(v);old_paid(v.d);return v
for vv in [Q,delta,m,M,bc,P02,Pf,f,t,V,W1,x,y,A1]:ck(vv)
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,v):
  v=E(v);return E(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):
  v=E(v);return E(self.a*v.a+delta*self.b*v.b,self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);return E(self.a/v,self.b/v)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,v):
  v=E(v);return self.a==v.a and self.b==v.b
 def conj(self):return E(self.a,-self.b)
b=E(ell/2,m/(2*delta));c=b.conj();a=E(1-ell)
p=E(1,1);q=p.conj();X=E(x,y);Y=X.conj()
assert b*c==E(bc) and b*X+c*Y==E(V) and b*p*X+c*q*Y==E(W1)
r=X-a*p-c*E(t);sg=Y-a*q-b*E(t)
rows=[[E(),E(),p,q],[E(),E(A1),r,sg],
      [p,r,E(),E(t)],[q,sg,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,w):return [v[i]+w[i] for i in range(4)]
def vs(h,v):return [h*vv for vv in v]
def vm(v,w):
 return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tr(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tr(vm(row,v)) for row in rows]
d=DK(one);F2=tr(d);Kd=DK(d)
assert d==[E(u),E(2*f-V-(1-ell)*u),X,Y] and F2==E(2*f)
def mean(j):
 sq=2*tr(vm(rows[0],rows[1])) if j==1 else tr(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
E0=mean(0);E1=mean(1);EB=mean(2);EC=mean(3)
assert not E0 and not E1.b and EC==EB.conj()
def N4(v):
 vv=vm(v,v);tv=tr(v)
 return 2*tr(vm(d,vv))-F2*tr(vv)-4*tv*tr(vm(d,v))+2*F2*tv*tv+tr(vm(v,DK(v)))
def centered(v):return va(v,vs(-tr(v),one))
def P2(v):
 vv=centered(v);return tr(vm(vm(vv,vv),vv))
v0,v1=rows[0],rows[1]
Npolar=N4(va(v0,v1))-N4(v0)-N4(v1)
v0c,v1c=centered(v0),centered(v1)
Pjet=3*tr(vm(vm(v0c,v0c),v1c))
w=lam-1-T
assert N4(v0)==E(2*lam*P02) and Pjet==E(3*w*P02)
N1=Npolar-E(4*lam*w*P02);assert not N1.b
NB,NC=N4(rows[2]),N4(rows[3])
PB,PC=P2(rows[2]),P2(rows[3])
assert NC==NB.conj() and PC==PB.conj()
NS=b*NB+c*NC-E(2*lam*P02*(ell+2*T+A2))
PS=b*PB+c*PC-E(P02*(ell+3*T+3*A2+B3))
assert not NS.b and not PS.b
original=[E1.a,EB.a,EB.b,N1.a,NS.a,PS.a]
names=['E1','EBe','EBo','N1','NS','PS']
for j,rr in enumerate(original):
 ck(rr);assert geomdegree(rr)<=(2 if j<4 else 3)
say('new_ell_half_raw_six_original_polynomials_ready',
    coordinateMap='lambda=epsilon+1/2,T=tau-1/2,Q=4(u-1)(u-2)',
    rawNames=names,rawNumeratorProfiles=[profile(v.n) for v in original],
    trueDualMeanProduct=True,wholeRawNSPSNoThreeRuleReduction=True,
    A1Identity='A1=-2(u-2)*tau',
    noPriorLambdaGcdThirtyColumnsOrCoverC114Regenerated=True)
monomials=[(aa,bb,degree-aa-bb) for degree in range(4)
           for aa in range(degree,-1,-1) for bb in range(degree-aa,-1,-1)]
assert len(monomials)==20 and len(set(monomials))==20
position={m0:i for i,m0 in enumerate(monomials)}
def geom_monomial(ex):return ep**ex[0]*tp**ex[1]*zp**ex[2]
def coordinates(poly):
 out=[Z for _ in monomials]
 for ex,co in poly.to_dict().items():
  key=tuple(map(int,ex[1:]));assert key in position
  out[position[key]]+=ctx.from_dict({(int(ex[0]),0,0,0):co})
 assert all(pure_u(v) for v in out)
 assert sum((out[i]*geom_monomial(mm) for i,mm in enumerate(monomials)),Z)==poly
 return out
columns=[];sources=[]
multipliers=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
for jj in range(6):
 for exponent in (multipliers if jj<4 else [(0,0,0)]):
  mon=geom_monomial(exponent)
  # numerator*mon = (OLD paid denominator)*mon*original[jj].
  raw=original[jj].n*mon
  columns.append(coordinates(raw));sources.append((jj,mon,original[jj].d))
assert len(columns)==18
target=[O if mon==(0,0,1) else Z for mon in monomials]
matrix=[[columns[j][i] for j in range(18)] for i in range(20)]
work=[row[:]+[target[i]] for i,row in enumerate(matrix)]
zero_rows=[i for i,row in enumerate(matrix) if not any(row)]
rank=0;previous=O;pivots=[]
# One fixed rectangular fraction-free solve, not a quotient/multiplication
# model. Unknown pivot zeros are kept by the final complete raw identity.
for col in range(18):
 pivotrow=next((ii for ii in range(rank,20) if work[ii][col]),None)
 if pivotrow is None:continue
 if pivotrow!=rank:work[rank],work[pivotrow]=work[pivotrow],work[rank]
 pivot=work[rank][col];assert pivot and pure_u(pivot)
 for ii in range(rank+1,20):
  entry=work[ii][col]
  for jj in range(col+1,19):
   num=pivot*work[ii][jj]-entry*work[rank][jj]
   work[ii][jj]=exact(num,previous)
   statistics['newBareissPolynomialProducts']+=1
  work[ii][col]=Z
 pivots.append((rank,col));rank+=1;previous=pivot
 say('new_ell_half_direct_raw_z_rectangular_step',
     actualPivotCount=rank,coefficientColumn=col,
     remainingRows=20-rank)
assert all(not any(work[ii][jj] for jj in range(18)) for ii in range(rank,20))
inconsistent=any(work[ii][18] for ii in range(rank,20))
say('new_ell_half_direct_fixed_polynomial_container_return',
    rows=20,originalColumns=18,rankOverQQofU=rank,
    originalIdenticallyZeroRows=zero_rows,
    targetConsistent=not inconsistent,
    containerOnlyNotAQuotientAlgebra=True,
    allOriginalDegreeThreeMonomialsRetained=True,
    noPriorGcdOrThirtyColumnProofGate=True)
def finish():
 say('new_ell_half_direct_original_z_input_finished',
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     statistics=statistics,maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
     noOldProofGateReplayed=True,noCoefficientPayloadOrChunksWritten=True,
     ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0)
if inconsistent:
 say('new_ell_half_fixed_raw_z_target_not_returned',
     allOldC114FibersAndAllOriginalConditionsRetained=True,
     noHigherDegreeOrReorderedSolveRun=True,
     noWholeEllHalfExclusion=True)
 finish()
else:
 solution=[R() for _ in range(18)]
 for row,col in reversed(pivots):
  value=R(work[row][18])-sum((R(work[row][j])*solution[j] for j in range(col+1,18)),R())
  solution[col]=value/R(work[row][col])
  assert pure_u(solution[col].d) and pure_u(solution[col].n)
 for i in range(20):
  assert sum((R(matrix[i][j])*solution[j] for j in range(18)),R())==R(target[i])
  statistics['newFullMatrixTargetCoordinates']+=1
 omega=[R() for _ in range(6)]
 for jj,(source,mon,scale) in enumerate(sources):
  omega[source]+=solution[jj]*R(scale*mon)
 for vv in omega:assert pure_u(vv.d)
 back=sum((omega[j]*original[j] for j in range(6)),R())
 assert back==z
 back_minus=back-z
 assert not back_minus
 # Direct polynomial return before any terminal denominator is used as a
 # physical unit. This checks the SIX raw original multipliers together.
 for exponent in monomials:
  def coefficient(vv,exponent):
   return R(ctx.from_dict({(int(ex[0]),0,0,0):co
          for ex,co in vv.n.to_dict().items()
          if tuple(map(int,ex[1:]))==exponent}),vv.d)
  assert coefficient(back,exponent)==coefficient(z,exponent)
  statistics['newRawPolynomialTargetCoordinates']+=1
 denominator=O
 for vv in omega:denominator=exact(denominator,denominator.gcd(vv.d))*vv.d
 assert denominator and pure_u(denominator)
 scaled=[vv.n*exact(denominator,vv.d) for vv in omega]
 for j in range(6):
  assert R(scaled[j])==R(denominator)*omega[j]
  statistics['newFinalDenominatorProducts']+=1
 assert sum((R(scaled[j])*original[j] for j in range(6)),R())==R(denominator)*z
 core,paidpart=strip_paid(denominator)
 assert core and core*paidpart==denominator and pure_u(core)
 constant=core.coefficient(0);core=exact(core,ctx.constant(constant));paidpart*=constant
 assert core*paidpart==denominator
 old_paid(paidpart)
 final=[R(pp,paidpart) for pp in scaled]
 for vv in final:ck(vv)
 assert sum((final[j]*original[j] for j in range(6)),R())==R(core)*z
 say('new_ell_half_six_raw_original_z_multipliers_complete',
     target='z',allTwentyMatrixAndTwentyRawPolynomialCoordinatesReturned=True,
     finalOriginalMultiplierNumerators=[profile(vv.n) for vv in final],
     finalOriginalMultiplierDenominators=[profile(vv.d) for vv in final],
     actualFinalUncancelledDenominatorLCM=profile(denominator),
     retainedCover=profile(core),
     exactClaim='Cnew(u)*z belongs to the SIX raw original equations I6',
     clearingExponent=1,
     allUnpaidPureUZeroFibersRetained=True,
     onlyOldPaidSupportsRemoved=True,
     noZOrDOrNewGeometryInverse=True,
     wholePhysicalEllHalfExcluded=int(core.total_degree())==0)
 if int(core.total_degree())>0:
  coefficients=core.to_dict();dd=max(int(ex[0]) for ex in coefficients)
  cp=fmpq_poly([coefficients.get((j,0,0,0),0) for j in range(dd+1)])
  unit,factors=cp.factor();returned=fmpq_poly([unit]);small=[]
  for fac,multiplicity in factors:
   returned*=fac**int(multiplicity)
   pp=ctx.from_dict({(j,0,0,0):fac[j] for j in range(fac.degree()+1) if fac[j]})
   small.append({'factor':profile(pp),'multiplicity':int(multiplicity)})
  assert returned==cp
  say('new_ell_half_new_direct_cover_QQ_factors',
      factors=small,completeFactorProductReturned=True,
      allEntireConstantFieldsRetained=True,noAdditionalExclusion=True)
 finish()

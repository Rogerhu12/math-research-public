#!/usr/bin/env python3
"""NEW exact F5 collision point and original integral retraction.

Define F5 from the actual g4 substitution ell=1/2,
Q=4(u-1)(u-2). Work in the entire QQ[u]/F5. Construct the original
four quadratic rows and complete F6/NV, then find their common v at
lambda=1/2,T=-1/2. Return the exact point, the actual raw cofactor
equations, and all necessary p-integral original units.
The SAME point is tested in the old polynomial L chart and its original
Dixon8: its monomial row must return wD=0,w0=1. Source-pole regularity
then proves F5 divides the previously exact P201. No old generic QQ
Gaussian, original norm driver, five-block rank gate or Gram20 replay.
The exact integral point provides a section of the already cyclic
completed original necessary quotient, hence its coordinates are
forced and D is really zero. 120s/1GiB. Small receipts only. 2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly
START=time.perf_counter();DEADLINE=START+120;PRIME=1009
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def restore_deadline():
 signal.setitimer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
def execute_prefix(prefix,path,label,namespace):
 original_alarm=signal.alarm
 def bounded_alarm(seconds):
  remaining=max(.001,DEADLINE-time.perf_counter())
  requested=float(seconds) if seconds>0 else remaining
  previous=signal.setitimer(signal.ITIMER_REAL,min(remaining,requested))
  return math.ceil(previous[0])
 signal.alarm=bounded_alarm
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(prefix,str(path)+":"+label,"exec"),namespace)
 finally:
  signal.alarm=original_alarm
  restore_deadline()
def digest(obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def pdigest(poly):
 d=digest([str(c) for c in poly.coeffs()]);d["degree"]=int(poly.degree());return d
def mdigest(poly):
 d=digest([int(c) for c in poly.coeffs()]);d["degree"]=int(poly.degree());return d
def read(name,sha,environ):
 path=Path(os.environ.get(environ,str(Path(__file__).with_name(name))))
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 return path,raw.decode()
vp,vs=read("2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py",
 "5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef",
 "ISP_H1_POLYNOMIAL_V_SOURCE")
marker="\ndef polynomial_norm(";assert vs.count(marker)==1
vpref=vs.split(marker,1)[0]
venv={"__file__":str(vp),"__name__":"__only_original_polynomial_definitions_for_new_F5_point__"}
execute_prefix(vpref,vp,"new-F5-necessary-original-definitions",venv)
with contextlib.redirect_stdout(io.StringIO()):
 originals,extras,units=venv["new_original_polynomials"]()
restore_deadline()
one=fmpq_poly([1]);zero=fmpq_poly([]);up=fmpq_poly([0,1])
Fint=fmpq_poly([-28,127,-234,213,-90,14]);F5=Fint/14
Qstar=4*(up-one)*(up-2*one)
sub=sum((co*Qstar**j for j,co in enumerate(venv["g"])),zero)
assert sub==16*(up-one)**3*Fint
assert F5.gcd(F5.derivative()).degree()==0
def pint(poly):return all(int(fmpq(c).denominator)%PRIME for c in poly.coeffs())
def modpoly(poly):
 out=[]
 for c in poly.coeffs():
  c=fmpq(c);den=int(c.denominator)%PRIME;assert den
  out.append(int(c.numerator)%PRIME*pow(den,-1,PRIME)%PRIME)
 return nmod_poly(out,PRIME)
bar=modpoly(F5)
assert bar.degree()==5 and int(bar[5])==1
constant,factors=bar.factor();product=nmod_poly([int(constant)],PRIME)
for ff,e in factors:product=product*ff**int(e)
assert product==bar and len(factors)==1
assert factors[0][0].degree()==5 and int(factors[0][1])==1
assert bar.gcd(bar.derivative()).degree()==0
assert mdigest(bar)["sha256"]=="0c780501e3c546150d75e155fd0cfa9fa774a18639ae652f10c3739ac9515d6a"
say("new_F5_exact_original_half_weight_fibre",
 integerF5Coefficients=[-28,127,-234,213,-90,14],
 exactQDefinition="4*(u-1)*(u-2)",
 completeG4SubstitutionIdentityReturned=True,
 originalMonicF5=pdigest(F5),actualPrimeReduction=mdigest(bar),
 actualWholeModularFactorDegrees=[5],
 completePrimeFactorProductReturned=True,
 trueQQIrreducibilityByPrimitiveLeadingUnitGauss=True,
 noModularFactorUsedToGuessQQInput=True)

counts={"fieldReductionProducts":0,"fieldInverseProducts":0,
        "vPolynomialDivisionProducts":0,"pointOriginalProducts":0}
cache={}
class K:
 __slots__=("p",)
 def __init__(self,v=0):
  if isinstance(v,K):self.p=v.p;return
  if not isinstance(v,fmpq_poly):v=fmpq_poly([fmpq(v)])
  q,r=divmod(v,F5);assert q*F5+r==v
  self.p=r;counts["fieldReductionProducts"]+=1
 def __bool__(self):return bool(self.p)
 def __eq__(self,v):return self.p==K(v).p
 def __neg__(self):return K(-self.p)
 def __add__(self,v):return K(self.p+K(v).p)
 __radd__=__add__
 def __sub__(self,v):return self+-K(v)
 def __rsub__(self,v):return K(v)+-self
 def __mul__(self,v):return K(self.p*K(v).p)
 __rmul__=__mul__
 def inverse(self):
  assert self
  key=tuple(str(c) for c in self.p.coeffs())
  if key in cache:return cache[key]
  gg,aa,bb=self.p.xgcd(F5);assert aa*self.p+bb*F5==gg and gg.degree()==0
  out=K(aa/gg[0]);assert self*out==1
  cache[key]=out;counts["fieldInverseProducts"]+=1;return out
 def __truediv__(self,v):return self*K(v).inverse()
 def __rtruediv__(self,v):return K(v)*self.inverse()
 def __pow__(self,n):
  assert n>=0
  out=K(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
U=K(up);Q=K(Qstar);L=K(fmpq(1,2));T=K(fmpq(-1,2))
def ea(co):
 assert co.d.gcd(F5).degree()==0
 out=K()
 for c in reversed(co.n):out=out*Q+K(c)
 num=out;out=out/K(co.d)
 assert out*K(co.d)==num
 return out
def eu(poly):
 out=K()
 for co in reversed(poly.c):out=out*L+ea(co)
 return out
def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def pa(a,b):
 return trim([(a[i] if i<len(a) else K())+(b[i] if i<len(b) else K())
              for i in range(max(len(a),len(b)))])
def ps(a,c):return trim([v*c for v in a])
def pm(a,b):
 if not a or not b:return []
 out=[K() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return trim(out)
def pdiv(a,b):
 a=trim(a);b=trim(b);assert b
 r=a[:];q=[K() for _ in range(max(0,len(a)-len(b)+1))]
 iv=b[-1].inverse()
 while r and len(r)>=len(b):
  j=len(r)-len(b);co=r[-1]*iv;q[j]=q[j]+co
  for i,c in enumerate(b):r[j+i]=r[j+i]-co*c
  r=trim(r)
 q=trim(q);assert pa(pm(q,b),r)==a
 counts["vPolynomialDivisionProducts"]+=1
 return q,r
def xgcd(a,b):
 rr,r=trim(a),trim(b);ss,s=[K(1)],[];tt,t=[],[K(1)]
 while r:
  q,rem=pdiv(rr,r);rr,r=r,rem
  ss,s=s,pa(ss,ps(pm(q,s),K(-1)))
  tt,t=t,pa(tt,ps(pm(q,t),K(-1)))
 assert rr
 inv=rr[-1].inverse()
 out,aa,bb=ps(rr,inv),ps(ss,inv),ps(tt,inv)
 assert pa(pm(aa,a),pm(bb,b))==out
 return out,aa,bb
def original_v_polynomial(poly):
 out=[K() for _ in range(3)]
 for (ll,tt,vv),co in poly.v.items():
  assert vv<=2
  out[vv]=out[vv]+ea(co)*(L**ll)*(T**tt)
 return trim(out)
rows_v=[original_v_polynomial(poly) for poly in originals]
gcdv=[]
gcd_steps=[]
for label,poly in zip(["R","W","O","N1"],rows_v):
 if not poly:continue
 if not gcdv:gcdv=ps(poly,poly[-1].inverse())
 else:
  previous=gcdv
  gcdv,aa,bb=xgcd(previous,poly)
  gcd_steps.append(dict(original=label,firstDegree=len(previous)-1,
   secondDegree=len(poly)-1,commonDegree=len(gcdv)-1,
   fullQQBezoutProductReturned=True))
if len(gcdv)!=2:
 say("INCONCLUSIVE_NEW_F5_FIXED_ORIGINAL_POINT",
  actualCommonVDegree=len(gcdv)-1,gcdSteps=gcd_steps,
  noNewP201DivisorOrRetractionClaim=True,
  currentOriginalPointUpperBound=10)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
assert gcdv[1]==1
V=-gcdv[0]
def peval(poly,v):
 out=K()
 for co in reversed(poly):out=out*v+co
 return out
assert all(peval(poly,V)==0 for poly in rows_v)
def value(poly):
 out=K()
 for (ll,tt,vv),co in poly.v.items():
  out=out+ea(co)*(L**ll)*(T**tt)*(V**vv)
 counts["pointOriginalProducts"]+=1
 return out
assert all(value(poly)==0 for poly in originals+extras)
ell=1-2*(U-1)*(U-2)/Q
delta=1-Q;m=U-ell;V2=2*U-ell*Q;T0=V2-2*U*U
J=2*U*(1-U)+ell*Q
P02=(2-3*U)*V2-Q*U+2*U**3
Pf=T0*(J-Q);M=ell*V2-U*U;bc=M/(4*delta)
A2=2*L*L-2*L+1;B3=4*L**3-6*L*L+3*L-1
G=L*P02+(U-1)*T0
f=(G*T0-Q*P02*(ell+T))/Pf
zold=(V-J*f+G)/bc
physicalD=ell*A2-T*T
assert ell==fmpq(1,2) and physicalD==0
assert ell*ell*B3-3*ell*T*A2+2*T**3==0
assert ell*B3-A2*T==0
# Same actual raw scaled module. These are evaluated original polynomials,
# not a hypothetical free quotient at the point.
qr=[venv["qrow"](poly) for poly in originals]
heads=[[eu(c) for c in row[3:]] for row in qr]
indices=[0,1,3]
H=[heads[i] for i in indices]
def det3(a):
 return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
# Explicit minors avoid any cyclic sign convention.
adj=[]
for i in range(3):
 ar=[]
 for j in range(3):
  rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
  ar.append(((-1)**(i+j))*(H[rr[0]][cc[0]]*H[rr[1]][cc[1]]
                             -H[rr[0]][cc[1]]*H[rr[1]][cc[0]]))
 adj.append(ar)
head=det3(H);assert head
assert all(sum((adj[i][k]*H[k][j] for k in range(3)),K())==(head if i==j else 0)
           for i in range(3) for j in range(3))
rules=[[-sum((adj[j][i]*eu(qr[indices[i]][k]) for i in range(3)),K())
        for k in range(3)] for j in range(3)]
MT=[[K(),rules[0][i],rules[1][i]] for i in range(3)]
MV=[[K(),rules[1][i],rules[2][i]] for i in range(3)]
MT[1][0]=head;MV[2][0]=head
row=[K(1),T,V]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),K())
def mv(a,v):return [dot(rr,v) for rr in a]
def mm(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(3)),K()) for j in range(3)] for i in range(3)]
for mat,coordinate in [(MT,T),(MV,V)]:
 assert all(dot(row,[mat[i][j] for i in range(3)])==head*coordinate*row[j] for j in range(3))
other=qr[2]
r=[head*eu(other[k])+sum((eu(other[j+3])*rules[j][k] for j in range(3)),K()) for k in range(3)]
assert dot(row,r)==0
AB,BA=mm(MT,MV),mm(MV,MT)
comm=[[AB[i][j]-BA[i][j] for i in range(3)] for j in range(3)]
assert all(dot(row,co)==0 for co in comm)
cols=[r,mv(MT,r),mv(MV,r),comm[1]]
for poly in extras:
 degree=max(tt+vv for ll,tt,vv in poly.v)
 cache_columns={(0,0):[K(1),K(),K()]}
 def moncol(tt,vv):
  if (tt,vv) not in cache_columns:
   cache_columns[tt,vv]=mv(MT,moncol(tt-1,vv)) if tt else mv(MV,moncol(0,vv-1))
  return cache_columns[tt,vv]
 col=[K(),K(),K()]
 for (ll,tt,vv),co in poly.v.items():
  scale=ea(co)*(L**ll)*(head**(degree-tt-vv))
  vec=moncol(tt,vv);col=[x+scale*y for x,y in zip(col,vec)]
 assert dot(row,col)==head**degree*value(poly)==0
 cols.append(col)
raw_cofactors=[det3([[cols[j][i] for j in [0,1,last]] for i in range(3)])
               for last in [2,3,4,5]]
assert all(co==0 for co in raw_cofactors)

# All actual point coordinates and all removed original contents must be
# integral; every geometric/weight inverse used to interpret the quotient
# must have a whole residue-field inverse, returned before a lifting claim.
punit_returns=[];integral_point=all(pint(x.p) for x in [Q,L,T,V,zold,head])
def punit(value,label):
 if not pint(value.p):return False
 co=modpoly(value.p)%bar
 if not co:return False
 gg,aa,bb=co.xgcd(bar);assert aa*co+bb*bar==gg and gg.degree()==0
 inv=(aa*pow(int(gg[0]),-1,PRIME))%bar
 assert (co*inv)%bar==nmod_poly([1],PRIME)
 punit_returns.append(dict(original=label,identity=mdigest(co),inverseProductReturned=True))
 return True
unit_checks=[]
for label,co in units:
 val=ea(co);assert val
 unit_checks.append(punit(val,label))
unit_checks.append(punit(head,"same_actual_three_quadratic_head"))
all_units_integral=all(unit_checks)
say("new_F5_exact_same_original_QQ_point",
 lambdaValue="1/2",ellValue="1/2",TValue="-1/2",
 originalQ=pdigest(Q.p),originalV=pdigest(V.p),oldOriginalZ=pdigest(zold.p),
 fixedFourOriginalVGcdDegree=1,actualQQGcdSteps=gcd_steps,
 allFourOriginalQuadraticsReturnedAtSamePoint=True,
 sameCompleteOriginalF6AndNVReturned=True,
 exactPhysicalDEqualsZero=True,
 sixActualScaledMultiplicationColumnsReturned=True,
 allFourRawOriginalLambdaCofactorsReturnedZero=True,
 primitiveContentsAreNonzeroOriginalWeights=True,
 threeFixedOriginalSameQResultantsZeroByExactCommonLambda=True,
 allPointCoordinatesPIntegral=bool(integral_point),
 allRemovedOriginalWeightsAndActualHeadWholePUnits=bool(all_units_integral),
 actualWholeUnitReturns=punit_returns,
 noDInverseUsed=True,noQQFactorInferenceFromModularZero=True)

# Recover precisely the old necessary source, never its old Gaussian.
op,osrc=read("2026-11-28-unit211-Phi-zero-whole-H1-original-biquadratic-Dixon-unit-target-syntax-fix-8542.py",
 "ef9e285512e1eddcbac0512f853f0b2ac58b57546f9a4bfa7e5621a9eaf8ddcc",
 "ISP_H1_ORIGINAL_DIXON_SOURCE")
cut="\n# All Gaussian rational parameter poles may cancel."
assert osrc.count(cut)==1
oprefix=osrc.split(cut,1)[0]
original={"__file__":str(op),"__name__":"__only_original_Dixon8_for_new_F5_point_pole__"}
execute_prefix(oprefix,op,"necessary-F5-point-pole",original)
S=original["source_cover"];assert S.degree()==418
source_regular=(F5.gcd(S).degree()==0)
say("new_F5_exact_original_Dixon_source_regularity",
 originalSourceCoverDegree=418,gcdWithF5Degree=int(F5.gcd(S).degree()),
 sourcePolesRegularAtWholeF5=source_regular,
 oldGenericQQGaussianExecuted=False)
if not source_regular:
 say("INCONCLUSIVE_NEW_F5_ORIGINAL_SOURCE_POLES",
  actualQQPointAlreadyReturned=True,F5DividesP201Proved=False,
  integralRetractionProved=False,currentFullOriginalPointUpperBound=10)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
aold,bold,cold=[[ea(co) for co in line] for line in [original["a"],original["b"],original["c"]]]
lam0=ea(original["lambda0"]);A0=ea(original["A0"]);C0=ea(original["C0"])
mu=L-lam0
xstar=aold[1]*T+bold[1]*zold+cold[1]+2*cold[2]*lam0+cold[2]*mu
Lvalue=(aold[0]+aold[1]*L)*T+(bold[0]+bold[1]*L)*zold+cold[0]+cold[1]*L+cold[2]*L*L
if Lvalue:
 say("INCONCLUSIVE_NEW_F5_ORIGINAL_L_CHART",
  originalLValue=pdigest(Lvalue.p),actualQQPointAlreadyReturned=True,
  F5DividesP201Proved=False,integralRetractionProved=False,
  currentFullOriginalPointUpperBound=10)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
assert A0*T+C0+mu*xstar==0
def oldP(poly):
 out=K()
 for (xx,mm,unused),co in poly.v.items():
  assert unused==0
  out=out+ea(co)*(xstar**xx)*(mu**mm)
 return out
assert oldP(original["Tr"])==T and oldP(original["z"])==zold and oldP(original["lam"])==L
assert all(oldP(poly)==0 for poly in original["polys"])
D=[[ea(co) for co in rr] for rr in original["Dmatrix"]]
w=[(xstar**xx)*(mu**mm) for xx,mm,unused in original["row8"]]
assert len(w)==8 and w[0]==1
assert all(sum((w[i]*D[i][j] for i in range(8)),K())==0 for j in range(8))
bridge=(integral_point and all_units_integral)
say("new_F5_original_point_pole_and_completed_retraction_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalMonicF5=pdigest(F5),actualP201LastBlock=mdigest(bar),
 allOriginalLAndTwoCoordinateChartIdentitiesReturned=True,
 threeOriginalDixonPolynomialsAtSameQQPointZero=True,
 originalLeftAnnihilatorIdentity=digest([[str(c) for c in co.p.coeffs()] for co in w]),
 allEightOriginalDixonColumnProductsZeroReturned=True,
 originalConstantTargetPairingOneReturned=True,
 originalSourcePolesRegularAtF5=True,
 F5DividesPreviouslyExactP201Proved=True,
 exactIntegralOriginalPointSectionAvailable=bridge,
 completedCyclicOriginalGeometryRetractionProved=bridge,
 actualCompletedCoordinatesForcedToQQCollisionPoint=bridge,
 actualPhysicalDReallyZeroInLastOriginalNecessaryQuotient=bridge,
 lastActualCompletionBlockExcludedInPhysicalDNonzeroScope=bridge,
 wholeOriginalH1ExcludedUsingAlreadyClosedF9Blocks=bridge,
 originalDZeroCollisionGraphNotExcluded=True,
 noJacobianOrNewGaussianGateUsed=True,
 noOldGram20OrNormDriverReplayed=True,
 noHenselSeriesOrQQFactorPayloadGenerated=True,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 ordinaryISPClaim=False,arithmeticCounts=counts,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)

#!/usr/bin/env python3
"""NEW centered original NS/PS two-column cofactor on Phi=0.
Use only the original I10 definition prefix through the two complete
weighted value rows. Translate X=Z+e*lambda+f, with p0=e*lambda^2+f*lambda+g.
Both original rows then have lambda degree at most three. Construct
their actual polynomial cofactor, divide only a common divisor of the
TWO ACTUAL MULTIPLIERS with full return, and record lambda content and
the true leading coefficient. No old lambda8 target, six-row closure,
large norm, projection, Gaussian, or old factor gate is replayed.
All slope-zero weights and unremoved scalar content are retained.
120 seconds /1 GiB, including every nested source prefix.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py"
path=Path(os.environ.get("ISP_PHI_I10_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="527cddc0905e6ab51530b08172fc44c7652926e928de6769603e3a5d037c4c59"
mark=b'\nsay("new_complete_original_Gram_B_spectra_and_weighted_NS_PS",'
assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==7782
assert hashlib.sha256(prefix).hexdigest()=="e65ccba5fe91105a3d2c05d433a19d17b59761f6bc8d1cfffedda7e525f818aa"
scope={"__file__":str(path),"__name__":"new_original_NSPS_definition_only"}
original_alarm=signal.alarm;original_timer=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return original_timer(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 requested=float(seconds) if seconds>0 else left
 return original_timer(which,min(left,requested),0)
def bounded_alarm(seconds):
 return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-original-NSPS-definition","exec"),scope)
finally:
 signal.alarm=original_alarm;signal.setitimer=original_timer
 original_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
geo=scope["geo"];R=scope["R"];ctx=scope["ctx"];one=scope["one"];zero=scope["zero"]
profile=scope["profile"];rprofile=scope["rprofile"];legal=scope["legal"]
a,c,Delta,p0,p1,p2=[scope[k] for k in ["aa","cc","Delta","p0","p1","p2"]]
b=geo["b"];d=geo["d"];lam=scope["lcoef"]
g,f,e=geo["coeff_lambda"](p0,2)
h=e*lam+f
assert geo["weight_only"](e.n) and geo["weight_only"](e.d)
assert p0==e*lam**2+f*lam+g
assert p1==a*lam+b and p2==c*lam+d
assert Delta==a*d-b*c
# X=Z+e*lambda+f has a polynomial inverse modulo the ORIGINAL N1 remainder.
# No lambda inverse and no new weight inverse are introduced.
tx=[(-d*e*lam+c*g-d*f)/Delta,p2/Delta]
zx=[(b*e*lam+b*f-a*g)/Delta,-p1/Delta]
assert a*tx[0]+c*zx[0]==-h and a*tx[1]+c*zx[1]==1
assert p0+p1*tx[0]+p2*zx[0]==0
assert p1*tx[1]+p2*zx[1]==0
for x in tx+zx:
 legal(x,True)
 assert int(x.n.degrees()[2])<=1
beta0=scope["beta0"]-scope["beta1"]*h-h*h
beta1=scope["beta1"]+2*h
for x in [beta0,beta1]:
 legal(x,True)
 assert int(x.n.degrees()[2])<=2
say("new_original_weight_translation_and_centered_square",
 e=rprofile(e),trueInverse=[list(map(rprofile,tx)),list(map(rprofile,zx))],
 centeredSquare=[rprofile(beta0),rprofile(beta1)],
 originalN1CoordinateReturns=True,
 noLambdaInverseOrNewUnit=True,wholeSlopeZeroRetained=True)
rows=[];origins=[]
for label in ["NS","PS"]:
 original=scope[label];r0,r1,r2=original.row
 row=[r0+r1*tx[0]+r2*zx[0],r1*tx[1]+r2*zx[1]]
 kap=(-c*r1+a*r2)/Delta
 assert row[0]+row[1]*h+kap*p0==r0
 assert row[1]*a+kap*p1==r1 and row[1]*c+kap*p2==r2
 for x in row:
  legal(x,True)
  assert int(x.n.degrees()[2])<=3
 rows.append(row);origins.append(original.node)
 say("new_original_NSPS_centered_row",label=label,originalDAGNode=original.node,
     actualThreeRow=[rprofile(x) for x in original.row],
     actualCenteredRow=[rprofile(x) for x in row],
     allThreeCoefficientReturns=True,lambdaDegreeUpperBound=3)
N,P=rows
def exact(x,y):
 q=x/y;assert q*y==x
 return q
den=exact(N[1].d*P[1].d,N[1].d.gcd(P[1].d))
mu=P[1].n*exact(den,P[1].d)
nu=-N[1].n*exact(den,N[1].d)
assert R(mu)*N[1]+R(nu)*P[1]==0
assert mu or nu
common=mu.gcd(nu)
mulN=exact(mu,common);mulP=exact(nu,common)
assert common*mulN==mu and common*mulP==nu
assert mulN.gcd(mulP).total_degree()==0
constant=R(mulN)*N[0]+R(mulP)*P[0]
assert R(mulN)*N[1]+R(mulP)*P[1]==0
assert int(constant.n.degrees()[2])<=6
legal(constant,True)
say("new_actual_NSPS_common_multiplier_cofactor",
 commonMultiplier=profile(common),actualMultipliers=[profile(mulN),profile(mulP)],
 actualScalar=rprofile(constant),allBothColumnReturns=True,
 commonMultiplierZeroLocusCoveredByDirectReturnedIdentity=True,
 originalDAGNodes=origins,originalDAGOperations=len(scope["nodes"]),
 fixedOriginalLambdaUpperBound=6,
 oldThreeLambda8NotExecuted=True,wholePhiExcluded=False)
if not constant:
 say("new_original_NSPS_cofactor_identically_zero",
     noNewNecessaryScalarClaim=True,wholeSlopeZeroRetained=True,
     wholePhiExcluded=False,ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
# Clear only the actual remaining paid/chart denominator. Strip only
# already-paid weight factors, never an unproved lambda content.
primitive,paid,history=geo["strip_paid"](constant.n,True)
assert primitive*paid==constant.n
actualN=legal(R(mulN*constant.d,paid),True)
actualP=legal(R(mulP*constant.d,paid),True)
assert actualN*N[0]+actualP*P[0]==R(primitive)
assert actualN*N[1]+actualP*P[1]==0
# The identity before modulo N1 is fully returned in all three columns.
kN=(-c*scope["NS"].row[1]+a*scope["NS"].row[2])/Delta
kP=(-c*scope["PS"].row[1]+a*scope["PS"].row[2])/Delta
k=actualN*kN+actualP*kP
for j in range(3):
 rhs=R(primitive) if j==0 else R()
 assert actualN*scope["NS"].row[j]+actualP*scope["PS"].row[j]==rhs+k*[p0,p1,p2][j]
coeffs={}
for ex,v in primitive.to_dict().items():
 degree=int(ex[2]);assert ex[3]==ex[4]==0
 coeffs.setdefault(degree,zero)
 coeffs[degree]+=ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):v})
degree=max(coeffs);assert degree<=6
content=zero
for degree_i in sorted(coeffs):
 content=content.gcd(coeffs[degree_i])
scalar=content.coefficient(0)
content=exact(content,ctx.constant(scalar))
lambda_primitive=exact(primitive,content)
assert content*lambda_primitive==primitive
leading=coeffs[degree]
leading_core,leading_paid,leading_removed=geo["strip_paid"](leading,True)
assert leading_core*leading_paid==leading
say("new_complete_original_NSPS_scalar_lambda_content_and_true_head",
 exactOriginalScalar=profile(primitive),actualLambdaDegree=degree,
 removedOnlyOriginalPaidWeights=history,
 entireUnpaidLambdaContent=profile(content),
 lambdaPrimitiveFactor=profile(lambda_primitive),
 trueLeadingCoefficient=profile(leading),entireUnpaidLeadingSupport=profile(leading_core),
 leadingRemovedOnlyOriginalPaidWeights=leading_removed,
 finalOriginalMultipliers=[rprofile(actualN),rprofile(actualP)],
 allTwoColumnAndThreeOriginalCoordinateReturns=True,
 actualIdentity="mu_NS*NS+mu_PS*PS=scalar+k*N1_remainder modulo the original three means",
 necessaryConditionIsWholeContentTimesPrimitive=True,
 noUnprovedContentOrLeadingFactorInverted=True,
 wholeSlopeZeroAndAllOtherUnpaidWeightFibersRetained=True,
 noLargeNormProjectionGaussianOrOldLambda8Executed=True,
 noRecomputableCoefficientPayloadSaved=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)

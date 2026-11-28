#!/usr/bin/env python3
"""NEW whole-Phi extension target for the original NSPS scalar.
Inspect the ACTUAL third original multiplier k in the original N1
relation, and return all three source coordinates using only old
whole-Phi paid weight denominators. Do not assume the slope-zero
locus is covered from two polynomial multipliers. If any new pole
remains, retain its entire support and make no whole-Phi claim.
Only the necessary definition of the already-published scalar and k
is used. No old lambda-content/head computation or large target.
120 seconds /1 GiB including nested prefixes. Small receipts only.
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
name="2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py"
path=Path(os.environ.get("ISP_PHI_CENTERED_NSPS_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="baaac1d2cb05437b6c771856aea8991692cad5ff62276e6bce12584d15da8ca6"
marker=b"\nfor j in range(3):\n rhs=R(primitive) if j==0 else R()\n"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==6125
assert hashlib.sha256(prefix).hexdigest()=="4b152304c41026c94b93147d1360644217c5f15fff88e30264d2e7b02ae6b31d"
scope={"__file__":str(path),"__name__":"new_whole_source_regular_extension_definition"}
original_alarm=signal.alarm;original_timer=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return original_timer(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 return original_timer(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):
 return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-exact-scalar-and-three-multiplier-definition","exec"),scope)
finally:
 signal.alarm=original_alarm;signal.setitimer=original_timer
 original_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
geo=scope["geo"];R=scope["R"];profile=scope["profile"];rprofile=scope["rprofile"]
mu,nu,k=[scope[s] for s in ["actualN","actualP","k"]]
scalar=scope["primitive"];n=[scope[s] for s in ["p0","p1","p2"]]
N=scope["scope"]["NS"];P=scope["scope"]["PS"]
multipliers=[mu,nu,-k];regular=True;poles=[]
for label,value in zip(["NS","PS","original_N1"],multipliers):
 assert geo["weight_only"](value.d)
 residual,paid,history=geo["strip_paid"](value.d,False)
 assert residual*paid==value.d
 all_paid=residual.total_degree()==0
 regular=regular and all_paid
 poles.append(dict(label=label,allDenominatorOldPaid=all_paid,
                   multiplier=rprofile(value),retainedPoleSupport=profile(residual),
                   removedOnlyOldWholePhiWeights=history))
say("new_actual_three_original_multipliers_whole_weight_regularity",
 sourceScope="current Phi=0,D!=0, entire first head already excluded",
 scalarDefinition=profile(scalar),multipliers=poles,
 noSlopeInverseAllowedInNewRegularityTest=True,
 actualThirdMultiplierReturned=True,allOldWeightRegular=regular)
# These are rational identities originally proved on the slope chart;
# their new coefficients are returned WITHOUT that localization.
for j in range(3):
 target=R(scalar) if j==0 else R()
 assert mu*N.row[j]+nu*P.row[j]-k*n[j]==target
if not regular:
 say("new_whole_Phi_source_extension_not_paid",
     entireResidualPoleSupportsRetained=True,
     allThreeCoordinateIdentitiesReturned=True,
     oldSlopeChartStatementOnly=True,
     noNewWholePhiNecessaryScalarClaim=True,
     wholePhiExcluded=False,ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
for value in multipliers:geo["legal"](value,False)
say("new_entire_Phi_actual_NSPS_sixth_scalar_original_ideal",
 exactOriginalScalar=profile(scalar),
 allThreeOriginalCoefficientIdentitiesReturned=True,
 actualIdentity="mu*NS+nu*PS-k*N1_remainder=C6 modulo three original means",
 originalNSPSDAGNodes=[N.node,P.node],
 noSlopeInverseInAnyFinalOriginalCoefficient=True,
 wholeSlopeZeroLocusNowCoveredForThisScalar=True,
 entireExistingUnpaidTrueLeadingLocusStillRetained=True,
 noNewCofactorContentHeadOrLargeProjectionGate=True,
 lambdaDegree=int(scalar.degrees()[2]),
 lambdaDegreeSixLeadingOpenNecessaryLengthAtMost=18,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)

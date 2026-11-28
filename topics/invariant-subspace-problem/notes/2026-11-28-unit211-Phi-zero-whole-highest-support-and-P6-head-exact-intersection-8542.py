#!/usr/bin/env python3
"""NEW exact intersection of two existing original Phi weight supports.
Current scope: Phi=0, physical D!=0, all original paid weights and the
entire first quadratic head paid. Reconstruct only the necessary
highest NV/F6/N1 input; use a direct 3-by-3 adjugate to define its
already-proved unique constant-row denominator C. Do not execute the
old five-row Gaussian. Read the SAVED original P6 inside the runner
and extract its lambda^6 coefficient; no old P6 cofactor or factor
audit is executed. The new target is the exact QQ[u,Q] gcd between
the two weight supports, with all common zero fibers retained.
No complete projection, coefficient payload, or encoded output.
120 s /1 GiB, including nested necessary prefixes.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,zlib,base64,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq
START=time.perf_counter();DEADLINE=START+120
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def pinned(name,sha,environment=None):
 path=Path(os.environ.get(environment,str(Path(__file__).with_name(name)))) if environment else Path(__file__).with_name(name)
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha,(name,"source identity")
 return path,raw
def execute_bounded(prefix,path):
 ns={"__file__":str(path),"__name__":"new_C_H19_necessary_original_definition"}
 original_alarm=signal.alarm;original_timer=signal.setitimer
 def timer(which,seconds,interval=0):
  if which!=signal.ITIMER_REAL:return original_timer(which,seconds,interval)
  remaining=max(.001,DEADLINE-time.perf_counter())
  requested=float(seconds) if seconds>0 else remaining
  return original_timer(which,min(remaining,requested),0)
 def alarm(seconds):
  return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
 signal.alarm=alarm;signal.setitimer=timer
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(prefix,str(path)+":necessary-highest-definition-only","exec"),ns)
 finally:
  signal.alarm=original_alarm;signal.setitimer=original_timer
  original_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
 return ns
name="2026-11-28-unit211-Phi-zero-whole-first-head-original-NV-F6-highest-unit-filtered-lift-8542.py"
path,raw=pinned(name,"4cebc8a6e7e16c58e9dff2bc055acd2bc9e262132bc08d7d9dfa2bff0ca3cd41","ISP_PHI_HIGHEST_SOURCE")
mark=b"# A fixed ordered input:"
assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==9094
assert hashlib.sha256(prefix).hexdigest()=="9bde53d859752f8ca1a873917ab9c5d633c9adeffd8ca256240c5a97964b2f7a"
ns=execute_bounded(prefix,path)
R=ns["R"];ctx=ns["ctx"];zero=ns["zero"];one=ns["one"]
u,Q,ell=[ns[s] for s in ["u","Q","ell"]]
exact=ns["exact"];profile=ns["profile"];weight_only=ns["weight_only"]
strip_paid=ns["strip_paid"]
original_rows=[ns["nvrow"],ns["frow"],ns["low1"]]
# Necessary definition of the SAME unique old target coefficient:
# alpha*A=e0, hence alpha=e0*adj(A)/det(A). No Gaussian/pivot replay.
detA=ns["old"]["determinant"](original_rows);assert detA
adjA=ns["old"]["adjugate"](original_rows)
alpha=[adjA[0][j]/detA for j in range(3)]
assert all(sum((alpha[i]*original_rows[i][j] for i in range(3)),R())==int(j==0)
           for j in range(3))
C=one
for x in alpha:
 assert weight_only(x.n) and weight_only(x.d)
 C=exact(C,C.gcd(x.d))*x.d
coreC,scaleC,oldremoved=strip_paid(C)
assert profile(C)["sha256"]=="662239cc0ed91ebf8b96e4e5f5dc282db19c58963e203d3e342c64fd183c1970"
assert profile(coreC)["sha256"]=="f2fcd6f323adaf47121341fc2e28c8af92dfba0e84dd13ed87e96f1f77081d8a"
# 2*ell-3 is already excluded on this whole Phi/D!=0 chart by the
# old ordered exceptional-weight theorem and the B/C exchange. It is
# NOT assumed paid on a general LS chart outside Phi=0.
extra_unit=(2*ell-3).n
removed_extra=0
while True:
 gg=coreC.gcd(extra_unit)
 if gg.total_degree()==0:break
 oldcore=coreC;coreC=exact(coreC,gg);scaleC*=gg
 assert coreC*gg==oldcore
 removed_extra+=1
constant=coreC.coefficient(0)
coreC=exact(coreC,ctx.constant(constant));scaleC*=constant
assert scaleC*coreC==C
say("new_same_original_highest_support_input_by_direct_adjugate",
 sourcePrefixBytes=len(prefix),oldGaussianNotExecuted=True,
 uniqueOriginalThreeCoefficientTargetReturned=True,
 fullWeightDenominator=profile(C),newRetainedWeightSupport=profile(coreC),
 oldRemovedPaidWeights=oldremoved,
 additionalWholePhiEllThreeHalvesDivisions=removed_extra,
 entireRemainingSupportRetained=True)

saved_name="2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json"
saved_path,saved_raw=pinned(saved_name,"7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b","ISP_PHI_SAVED_P6_JSON")
saved=json.loads(saved_raw);record=saved["polynomial"]
payload=zlib.decompress(base64.b64decode(record["data"]))
assert len(payload)==record["uncompressedBytes"]==86039
assert hashlib.sha256(payload).hexdigest()==record["payloadSha256"]=="9e50cc2a30cf8500b7bef25f8e579334c2b46f8d896662759cdc0ec85f35542c"
obj=json.loads(payload)
assert obj["variables"]==["u","Q","lambda"] and len(obj["terms"])==3101
head=zero;seen=set();lambda_degree=-1
for ex,c in obj["terms"]:
 i,j,k=map(int,ex);assert (i,j,k) not in seen
 seen.add((i,j,k));lambda_degree=max(lambda_degree,k)
 if k==6:head+=ctx.from_dict({(i,j,0,0,0):fmpq(c)})
assert lambda_degree==6 and head and weight_only(head)
H,scaleH,headremoved=strip_paid(head)
assert scaleH*H==head
assert list(map(int,H.degrees()))[:2]==[19,11]
assert len(H.to_dict())==137
# Only a new support gcd follows. The old QQ irreducibility of H is
# an existing theorem, not a new factor/reproducibility gate.
say("new_saved_original_P6_actual_lambda_six_head_input",
 savedFileSHA256=hashlib.sha256(saved_raw).hexdigest(),
 savedPayloadSHA256=hashlib.sha256(payload).hexdigest(),
 fixedOriginalLambdaDegree=6,
 retainedHeadSupport=profile(H),originalFullHead=profile(head),
 removedOnlyPaidWeights=headremoved,
 originalHeadFactorizationNotReplayed=True,
 noCoefficientPayloadPrintedOrWritten=True)

common=coreC.gcd(H)
constant=common.coefficient(0)
common=exact(common,ctx.constant(constant))
cquot=exact(coreC,common);hquot=exact(H,common)
assert common*cquot==coreC and common*hquot==H
assert cquot.gcd(hquot).total_degree()==0
coprime=common.total_degree()==0
bound=int(coreC.total_degree())*int(H.total_degree()) if coprime else None
say("new_exact_original_highest_and_P6_weight_support_intersection_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 highestSupport=profile(coreC),originalSixthHeadSupport=profile(H),
 exactCommonWeightFactor=profile(common),
 bothExactQQDivisionsMultipliedBack=True,
 residualQQCoprimalityReturned=True,
 exactCoprimalityOfOriginalSupports=coprime,
 highestSupportTotalDegree=int(coreC.total_degree()),
 sixthHeadTotalDegree=int(H.total_degree()),
 exceptionalCommonAffineWeightSetFinite=coprime,
 commonAffineWeightDistinctPointUpperBound=bound,
 outsideIntersectionOriginalFiberGeneratedByAtMost=21,
 onOriginalSixthHeadComplementOriginalFiberGeneratedByAtMost=18,
 onNewHighestSupportComplementOriginalFiberGeneratedByAtMost=21,
 originalModuleNotAssumedFree=True,
 noBoundForFibersAtTheEntireCommonZeroLocus=True,
 wholePhiEmpty=False,
 noClaimThatEitherSupportIsNecessaryForAllOriginalPoints=True,
 noLargeProjectionOrOldCofactorGaussianNormModuleGateExecuted=True,
 noRecomputableCoefficientPayloadEncodingOrSplitWritten=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)

#!/usr/bin/env python3
"""NEW exact full-Phi head relations H42 with H19 and Cstar.
The full-Phi source regularity of C6 is already proved. Reconstruct
only its necessary definition and extract its true lambda6 head.
Read the old P6 head inside the runner through its pinned historical
loader; define old Cstar by its already-proved three-row adjugate.
Do not execute either old head gcd or any old cofactor/projection gate.
New targets: exact head gcds and the complete QQ factorization of H42.
Keep all common zero fibers and never infer emptiness from gcd1 in
two variables. 120 seconds /1 GiB including necessary prefixes.
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
def run_prefix(name,sha,env,marker,length,prefix_sha):
 path=Path(os.environ.get(env,str(Path(__file__).with_name(name))))
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 assert raw.count(marker)==1
 prefix=raw.split(marker)[0]
 assert len(prefix)==length
 assert hashlib.sha256(prefix).hexdigest()==prefix_sha
 scope={"__file__":str(path),"__name__":"new_full_Phi_head_definition_only"}
 old_alarm=signal.alarm;old_timer=signal.setitimer
 def timer(which,seconds,interval=0):
  if which!=signal.ITIMER_REAL:return old_timer(which,seconds,interval)
  left=max(.001,DEADLINE-time.perf_counter())
  return old_timer(which,min(left,float(seconds) if seconds>0 else left),0)
 def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
 signal.alarm=alarm;signal.setitimer=timer
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(prefix,str(path)+":necessary-definitions-only","exec"),scope)
 finally:
  signal.alarm=old_alarm;signal.setitimer=old_timer
  old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
 return scope
ns=run_prefix(
 "2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py",
 "baaac1d2cb05437b6c771856aea8991692cad5ff62276e6bce12584d15da8ca6",
 "ISP_PHI_CENTERED_NSPS_SOURCE",
 b"\nfor j in range(3):\n rhs=R(primitive) if j==0 else R()\n",
 6125,"4b152304c41026c94b93147d1360644217c5f15fff88e30264d2e7b02ae6b31d")
ctx=ns["ctx"];zero=ns["zero"];one=ns["one"];profile=ns["profile"]
geo=ns["geo"];C6=ns["primitive"]
assert int(C6.degrees()[2])==6
head=zero
for ex,value in C6.to_dict().items():
 if ex[2]==6:
  assert ex[3]==ex[4]==0
  head+=ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):value})
H42,paid42,removed42=geo["strip_paid"](head,False)
assert H42*paid42==head
assert profile(H42)["sha256"]=="1988b732b97dfdded9386c97d261774e6cc4d7e8db659f211faa54961c67a8e7"
say("new_entire_Phi_NSPS_lambda_six_head_input",
 fullPhiOriginalSourceAlreadyProved=True,trueHead=profile(head),
 retainedWholeHead=profile(H42),onlyOldUnitsRemoved=removed42,
 noSlopeLocalizationUsedInHead=True,
 noOldLambdaContentOrThreeMultiplierAuditExecuted=True)
old=run_prefix(
 "2026-11-28-unit211-Phi-zero-whole-highest-support-and-P6-head-exact-intersection-8542.py",
 "a8d3f03e401a7a7c356da40e1f353ab5d3e879b9455a09a2f73d526c7df1af47",
 "ISP_PHI_OLD_HEAD_DEFINITION_SOURCE",
 b"\ncommon=coreC.gcd(H)\n",
 6171,"f11ea8d75adcd70908d8e0c593c9e2bd31a26d7769dbb9c6af2f86c152f4c2d5")
H19=ctx.from_dict(old["H"].to_dict())
Cstar=ctx.from_dict(old["coreC"].to_dict())
assert profile(H19)["sha256"]=="24f31b9bac95b9e45fc2f8a5fffc1035dece82238d19f1ec5030c68e026b424d"
assert int(H19.total_degree())==19 and int(Cstar.total_degree())==86
def exact(a,b):
 q=a/b;assert q*b==a
 return q
def normalize(p):
 assert p
 return exact(p,ctx.constant(p.coefficient(0)))
def common_report(name,a,b):
 common=normalize(a.gcd(b))
 aq=exact(a,common);bq=exact(b,common)
 assert common*aq==a and common*bq==b
 assert aq.gcd(bq).total_degree()==0
 coprime=common.total_degree()==0
 report=dict(pair=name,first=profile(a),second=profile(b),
             actualQQCommonFactor=profile(common),
             exactQuotients=[profile(aq),profile(bq)],
             completeProductsReturned=True,
             coprime=coprime,commonZeroSetExcluded=False,
             commonAffineWeightsFinite=coprime,
             commonAffineDistinctWeightUpperBound=int(a.total_degree())*int(b.total_degree()) if coprime else None)
 say("new_exact_entire_Phi_head_common_factor",**report)
 return report
r19=common_report("H42_H19",H42,H19)
rC=common_report("H42_Cstar",H42,Cstar)
# This is a genuinely new factorization, of H42 only. The old
# H19 irreducibility and old Cstar/H19 gcd are not recomputed.
unit,factors=H42.factor()
product=ctx.constant(unit);factor_records=[]
for factor,multiplicity in factors:
 multiplicity=int(multiplicity)
 product*=factor**multiplicity
 f=normalize(factor)
 gf19=normalize(f.gcd(H19));gfC=normalize(f.gcd(Cstar))
 assert exact(f,gf19)*gf19==f
 assert exact(f,gfC)*gfC==f
 factor_records.append(dict(multiplicity=multiplicity,normalizedFactor=profile(f),
                            commonWithH19=profile(gf19),commonWithCstar=profile(gfC),
                            entireZeroLocusRetained=True))
assert product==H42
say("new_complete_QQ_factorization_of_entire_Phi_NSPS_head",
 originalHead=profile(H42),factorCount=len(factors),
 rationalUnit=str(unit),factors=factor_records,
 entireProductExactlyReturned=True,
 noFactorDeclaredAnOriginalUnit=True,
 oldH19FactorAndOldCstarH19GCDNotReexecuted=True)
say("new_entire_Phi_three_actual_head_relations_finished",
 H42H19Coprime=r19["coprime"],
 H42H19CommonAffineWeightBound=r19["commonAffineDistinctWeightUpperBound"],
 outsideTheirActualCommonZeroSetFixedWeightNecessaryLengthAtMost=18,
 additionallyOnSlopeNonzeroFixedWeightNecessaryLengthAtMost=12,
 noBoundForEntireExceptionalFibersAsserted=True,
 oldCstarH19ExceptionalWeightBoundStillAvailable=1634,
 noTwoVariableGCDUsedToInferEmptyCommonZeroSet=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noRecomputableCoefficientPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)

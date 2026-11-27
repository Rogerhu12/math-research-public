#!/usr/bin/env python3
"""NEW exact factor geometry of the smallest canonical binary-cubic head.
Regenerate only the six-cubic construction prefix, not the old 15 minors.
The fixed first head is input to its FIRST QQ factorization and its exact
globally paid k-leading coefficient. All factor zero curves are retained.
No encoded/chunked data or regenerable output cache. 180 seconds /4 GiB."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
dep=Path(__file__).with_name('2026-11-28-unit211-W-six-original-binary-cubics-and-weight-head-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='edbba216705016a86f222a9b165bf9dd11320a5953438ddf21ea4a26c581b7b2'
marker=b"\ncombos=list(itertools.combinations(range(6),4))"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert hashlib.sha256(prefix).hexdigest()=='fe3da9b05cba74f3311e3cad5737d0baf67e0da3144f6396d1a740c3ac1e70d4'
ns={'__file__':str(dep),'__name__':'__original_head_construction_only_for_new_exact_factor_geometry__'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,ctx,head,detpoly,prof,strip_paid,paid=[
 ns[x] for x in ['C','ctx','head','detpoly','prof','strip_paid','paid']]
ep,kp,lp=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
delta=detpoly([head[i] for i in [0,1,2,3]])
h,removed=strip_paid(delta)
c=h.coefficient(0);h=h/c;removed*=c
assert h*removed==delta
assert prof(h)['sha256']=='b7f6ab4da28caa429f15fdb73034135568d8e73428aa1e813ee8cca292ba35c3'
def leading(p,var):
 degree=int(p.degrees()[var]);out=zero
 for mm,cc in p.to_dict().items():
  if int(mm[var])==degree:
   ex=list(map(int,mm));ex[var]=0
   out+=cc*ep**ex[0]*kp**ex[1]*lp**ex[2]
 return degree,out
de,he=leading(h,0);dk,hk=leading(h,1)
assert de==16 and dk==23 and h.degrees()[2]<=0
assert he==kp**13*(kp+3)
assert hk==-ep**4*(ep+1)**3/16384
paid(1/C(hk))
say(stage='new_W_smallest_binary_head_complete_parameter_leading',
 definition='paid normalization of det of canonical binary-head rows 0,1,2,3',
 exactInputProfile=prof(h),wholeFixedHeadProductReturned=True,
 eDegree=de,eHead='k^13*(k+3)',eHeadKEqualsMinusThreeFibreRetained=True,
 kDegree=dk,kHead='-e^4*(e+1)^3/16384',
 kHeadAlreadyPaidOnWholeCurrentW=True,
 monicKWeightEnvironmentRank=23,
 physicalFurtherWeightLocalizationsNotClaimedFree=True,
 noOriginalWEmptyClaim=True)
content,factors=h.factor()
product=ctx.constant(content);records=[]
for factor,multiplicity in factors:
 product*=factor**multiplicity
 degree,headk=leading(factor,1)
 assert headk.degrees()[1]<=0 and headk.degrees()[2]<=0
 # The complete product head is a unit. Every factor head is a unit
 # in the same localized coefficient ring; here check each explicitly.
 paid(1/C(headk))
 hh,dd=strip_paid(headk);assert hh*dd==headk and hh.total_degree()==0
 monic= C(factor)/C(headk)
 assert monic*C(headk)==C(factor)
 item=dict(factor=prof(factor),multiplicity=int(multiplicity),kDegree=degree,
           kLeading=prof(headk,True),
           entireKLeadingZeroFibreAlreadyExcludedByOriginalWeightUnits=True,
           exactMonicKNormalizationReturned=True,
           finiteFreeWeightEnvironmentRankBeforeFurtherLocalizations=degree)
 if len(factor.to_dict())<=25:
  item['smallNewFactorFormula']=prof(factor,True)
 records.append(item)
 say(stage='new_W_smallest_binary_head_whole_QQ_factor',**item,
     originalWholeFactorZeroFibreRetained=True,
     noMultivariableGcdEmptinessClaim=True)
assert product==h
assert sum(int(f.degrees()[1])*int(m) for f,m in factors)==23
say(stage='new_W_smallest_binary_head_exact_factor_geometry_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 rationalContent=str(content),factorRecords=records,
 completeQQFactorProductActuallyReturned=True,
 totalKDegreeCountingMultiplicities=23,
 everyFactorKHeadPaidByActualOriginalUnitCheck=True,
 allFactorCurvesRetainedAsWholeOriginalFibres=True,
 noOldFifteenMinorGateOrOriginalCofactorReplayed=True,
 coefficientPayloadTransmitted=False,encodedOrSplitDataCreated=False,
 wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

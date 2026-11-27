#!/usr/bin/env python3
"""Whole W: new complete C5-(T+gamma4)q4 cubic cancellation,
then one q3 subtraction, with all T2 leading-zero fibers kept.
Only new value-polynomial formulas are regenerated; no old N4 or cofactor
gate is replayed. 180 seconds / 4 GiB."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-entire-original-NV-pure-T-quintic-three-column-minors-8542.py')
raw=dep.read_bytes();assert hashlib.sha256(raw).hexdigest()=='da64f23af9b938e60c5aa3978b066098d88104093c412878e5b0278f873d79e9'
marker=b"\n# Entire raw N4, before either monic rule and before any norm reduction.\n"
assert raw.count(marker)==1
pref=raw.split(marker)[0];seed={'__file__':str(dep),'__name__':'__new_C5_formula_only_for_cubic_cancellation__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(pref,str(dep),'exec'),seed)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,C5,leading,T,lam,q4=[seed[x] for x in ['C','P','C5','leading','T','lam','q4']]
ns=seed['ns'];q3=ns['q3'];ppaid=seed['ppaid'];prof=seed['prof'];strip_paid=seed['strip_paid'];profile=seed['profile']
q5=C5.scale(1/leading);gamma4=q5.t.get((0,4),C())-10*lam
NV3=q5-(T+P(gamma4))*q4
assert all(mm[0]==0 for mm in NV3.t) and NV3.degree()<=3
mu3=NV3.t.get((0,3),C())
NV2=NV3-q3.scale(mu3)
assert all(mm[0]==0 for mm in NV2.t) and NV2.degree()<=2
assert NV2+q3.scale(mu3)+(T+P(gamma4))*q4==q5
for p in [P(gamma4),P(mu3),NV2]:ppaid(p)
head=NV2.t.get((0,2),C())
say(stage='whole_W_entire_NV_new_direct_T_quadratic_original_identity',
 fullOriginalPolynomialIdentityActuallyReturned=True,
 identity='q5=(T+gamma4)*q4+mu3*q3+NV2',
 gamma4Definition='T4 coefficient of q5, i.e. S4 coefficient minus 10lambda',
 onlyOneQ3Subtraction=True,
 originalQ4Kept=True,allLeadingZeroFibersRetained=True,
 noUnpaidHeadOrPhysicalDOrNormInverse=True,
 NV2=profile(NV2),claimExcluded=False)
if not head:
 say(stage='whole_W_entire_NV_direct_quadratic_head_identically_zero',
     actualDegree=NV2.degree(),wholeWExcluded=False)
else:
 remaining,removed=strip_paid(head.n)
 assert remaining*removed==head.n
 content,factors=head.n.factor()
 product=seed['ctx'].constant(content)
 for po,exponent in factors:product*=po**int(exponent)
 assert product==head.n
 factorProfiles=[dict(exponent=int(exponent),polynomial=prof(po,True)) for po,exponent in factors]
 actualPaid=remaining.total_degree()==0
 say(stage='whole_W_entire_NV_direct_T2_full_original_leading_factorization',
     actualHeadNumerator=prof(head.n),actualHeadDenominator=prof(head.d),
     allFactorsAndMultiplicitiesActuallyMultipliedBack=True,
     rationalContent=str(content),factors=factorProfiles,
     remainingUnpaid=prof(remaining,True),
     globallyPaidOnCurrentWholeW=actualPaid,
     noUnpaidFactorRemoved=True,wholeWExcluded=False)
 if actualPaid:
  monic=NV2.scale(1/head);assert monic.t.get((0,2),C())==1
  for cf in monic.t.values():
   dd,unitpart=strip_paid(cf.d)
   assert dd*unitpart==cf.d and dd.total_degree()==0
  assert monic.scale(head)==NV2
  say(stage='whole_W_new_global_monic_T2_from_entire_NV_original',
      allLeadingFactorsAlreadyPaid=True,
      monicT2=profile(monic),noNewParameterBoundaryDeleted=True,
      originalQ3Q4R6AndAllGramNPStillRetained=True,wholeWExcluded=False)
say(stage='whole_W_new_direct_NV_T2_identity_and_head_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 oldN4GateAndAllOldCofactorGatesRerun=False,
 largeRegenerableCachesWritten=False,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

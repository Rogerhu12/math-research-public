#!/usr/bin/env python3
"""Whole W: two actual original pure-T quadratics give a same-S affine row,
retaining the complete common-head-zero locus. Separately test the actual
three affine F coefficients for a weight-only Cramer unit.
No old parameter cofactor or head-factorization gate is replayed.
180 seconds / 4 GiB."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-entire-NV-direct-T-quadratic-leading-8542.py')
raw=dep.read_bytes();assert hashlib.sha256(raw).hexdigest()=='1be650ddcc4671d0a11ce366f5dddf01814d16365516a7665fb962a26611d63e'
marker=b"\nsay(stage='whole_W_entire_NV_new_direct_T_quadratic_original_identity',"
assert raw.count(marker)==1
nv={'__file__':str(dep),'__name__':'__NV2_formula_only_for_new_original_affine_rows__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(raw.split(marker)[0],str(dep),'exec'),nv)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
seed=nv['seed']['inp']
C,P,ctx,lam,F,S,AA,BB,R=[seed[x] for x in ['C','P','ctx','lam','F','S','AA','BB','R']]
ep,kp,lp=ctx.gens();strip_paid=seed['strip_paid'];prof=seed['prof']
profile=nv['profile'];ppaid=nv['ppaid'];primitive=seed['primitive_row']
T,q3,q4,NV2=[nv[x] for x in ['T','q3','q4','NV2']]
beta2=q3.t.get((0,2),C())-6*lam
r2=q4-(T-P(beta2))*q3
assert r2.degree()<=2 and all(mm[0]==0 for mm in r2.t)
a2=r2.t.get((0,2),C());b2=NV2.t.get((0,2),C())
SL=r2.scale(b2)-NV2.scale(a2)
assert all(mm[0]==0 and mm[1]<=1 for mm in SL.t)
assert SL+NV2.scale(a2)==r2.scale(b2)
ppaid(SL)
row,trace=primitive(SL);assert not row[2]
say(stage='whole_W_two_original_value_quadratics_new_same_S_affine_identity',
 identity='SL=b2*r2-a2*NV2',
 fullOriginalPolynomialIdentityActuallyReturned=True,
 originalQ3AndBothQuadraticsRetained=True,
 allOriginalH411AndCommonHeadZeroFibersRetained=True,
 noA2OrB2OrPhysicalDInverse=True,
 coefficientTrace=trace,
 constantCoefficient=prof(row[0],True),SLinearCoefficient=prof(row[1],True),
 claimExcluded=False)
if row[1]:
 rem,removed=strip_paid(row[1]);assert rem*removed==row[1]
 say(stage='whole_W_same_S_affine_original_leading_cover',
     remainingUnpaid=prof(rem,True),
     wholeLeadingZeroFiberRetained=True,
     globallyPaidOnCurrentWholeW=rem.total_degree()==0,
     noNewUnitAssumed=True,claimExcluded=False)
 if rem.total_degree()==0:
  Sp=C(-row[0],row[1])
  dr,du=strip_paid(Sp.d);assert dr*du==Sp.d and dr.total_degree()==0
  assert C(row[1])*Sp+C(row[0])==0
  say(stage='whole_W_true_same_S_unique_recovery_from_paid_original_head',
      exactS=profile(P(Sp)),allInverseProductsActuallyVerified=True,
      allOtherOriginalRowsRetained=True,claimExcluded=False)
else:
 say(stage='whole_W_same_S_affine_original_head_identically_zero',
     entireConstantConstraintRetained=True,constantIsZero=not bool(row[0]),
     noRankOrExclusionInferred=True)

def cl(cf,j):
 cf=C(cf);assert cf.d.degrees()[2]<=0
 n=ctx.constant(0)
 for mm,v in cf.n.to_dict().items():
  if mm[2]==j:n+=v*ep**int(mm[0])*kp**int(mm[1])
 return C(n,cf.d)
matrix=[]
for i,bb in enumerate(BB):
 assert all(mm[0]==0 and mm[1]<=1 for mm in bb.t)
 a0=bb.t.get((0,0),C());aS=bb.t.get((0,1),C())
 assert a0.n.degrees()[2]<=1 and aS.n.degrees()[2]<=0 and aS.d.degrees()[2]<=0
 aL=cl(a0,1);aC=cl(a0,0)
 assert bb==P(aC)+P(lam*aL)+S.scale(aS)
 matrix.append([aC,aL,aS])
a,b,c=matrix
cof=[b[1]*c[2]-b[2]*c[1],a[2]*c[1]-a[1]*c[2],a[1]*b[2]-a[2]*b[1]]
det=sum((cof[i]*matrix[i][0] for i in range(3)),C())
assert all(sum((cof[i]*matrix[i][j] for i in range(3)),C())==(det if j==0 else C()) for j in range(3))
assert sum((BB[i].scale(cof[i]) for i in range(3)),P())==P(det)
say(stage='whole_W_actual_three_F_coefficients_weight_Cramer_identity',
 originalRows=['E1','EBe','N1'],actualColumns=['1','lambda','S'],
 allThreeOriginalBEmbeddingsActuallyReturned=True,
 allThreeConstantCofactorColumnsActuallyReturned=True,
 allOriginalFLeadingZeroFibersRetained=True,determinantZero=not bool(det),
 noRankSamplingOrUnpaidInverse=True,claimExcluded=False)
if det:
 assert det.n.degrees()[2]<=0 and det.d.degrees()[2]<=0
 rem,paid=strip_paid(det.n);assert rem*paid==det.n
 content,factors=det.n.factor();prod=ctx.constant(content)
 for fac,mul in factors:prod*=fac**int(mul)
 assert prod==det.n
 say(stage='whole_W_three_original_F_coefficients_complete_weight_determinant',
     numerator=prof(det.n),denominator=prof(det.d),
     allFactorProductsActuallyReturned=True,
     rationalContent=str(content),
     factors=[dict(exponent=int(mul),polynomial=prof(fac,True)) for fac,mul in factors],
     remainingUnpaid=prof(rem,True),
     globalOnCurrentPaidW=rem.total_degree()==0,claimExcluded=False)
 if rem.total_degree()==0:
  Fp=-sum((AA[i].scale(cof[i]/det) for i in range(3)),P())
  assert all(mm[0]==0 for mm in Fp.t) and Fp.degree()<=2
  assert sum((R[i].scale(cof[i]) for i in range(3)),P())==(F-Fp).scale(det)
  for cf in Fp.t.values():
   dd,uu=strip_paid(cf.d);assert dd*uu==cf.d and dd.total_degree()==0
  say(stage='whole_W_actual_global_original_F_affine_elimination',
      actualOriginalIdentityReturned=True,
      formula='F=-sum(cofactor_i*A_i)/det',
      allInverseDenominatorsAlreadyPaid=True,
      physicalFLeadingZeroFibersCoveredByWholeWeightUnit=True,
      F=profile(Fp),originalQFAndOtherRowsStillRetained=True,claimExcluded=False)
say(stage='whole_W_new_two_quadratic_affine_and_F_weight_Cramer_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allEarlierN4HeadAndParameterCofactorGatesReplayed=False,
 allUnpaidLeadingZeroFibersRetained=True,
 largeRegenerableCachesWritten=False,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

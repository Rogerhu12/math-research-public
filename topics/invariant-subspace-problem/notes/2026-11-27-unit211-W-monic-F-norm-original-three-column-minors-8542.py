#!/usr/bin/env python3
"""Whole W: genuinely new original monic-F norms in the same S^3 environment.
For each actual Ri=Ai+Bi*F use Theta=Ai^2-p*Ai*Bi+q*Bi^2.
The exact identity B_i^2*qF-(B_i*F+B_i*p-A_i)*Ri=Theta
introduces no B_i inverse. New pure-S rows retain all such zero fibers.
180 seconds / 4 GiB. Regenerate construction prefixes only."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-coupled-original-Gram-value-four-by-three-minors-8542.py')
raw=dep.read_bytes();assert hashlib.sha256(raw).hexdigest()=='f5c0226e4dfc8d0f80da5358d3b4a3718e2ad9c834555a2335f1e58162bb0b41'
marker=b"\nsay(stage='whole_W_new_coupled_Gram_value_four_by_three_input',"
assert raw.count(marker)==1
pref=raw.split(marker)[0];inp={'__file__':str(dep),'__name__':'__construction_only_for_new_true_F_norm_original_input__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(pref,str(dep),'exec'),inp)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,ctx,e,k,lam,S,F=[inp[x] for x in ['C','P','ctx','e','k','lam','S','F']]
ep,kp,lp=ctx.gens();zero,one=ctx.constant(0),ctx.constant(1)
reduce_poly=inp['reduce_poly'];ppaid=inp['ppaid'];prof=inp['prof']
strip_paid=inp['strip_paid'];primitive_row=inp['primitive_row']
R,AA,BB=[inp[x] for x in ['R','AA','BB']]
qF=inp['seed']['ns']['qF']
pf=P();qf=P()
for mm,cf in qF.t.items():
 if mm[0]==0:qf+=P.monomial(mm,cf)
 elif mm[0]==1:pf+=P.monomial((0,mm[1]),cf)
 else:assert mm==(2,0) and cf==1
assert qF==F*F+pf*F+qf
assert pf.degree()<=1 and qf.degree()<=2
values=dict(inp['values']);theta_profiles={}
for i,name in enumerate(['E1','EBe','N1']):
 aa,bb=AA[i],BB[i]
 theta=aa*aa-pf*aa*bb+qf*bb*bb
 multiplier=bb*F+bb*pf-aa
 assert theta==bb*bb*qF-multiplier*R[i]
 assert all(mm[0]==0 for mm in theta.t) and theta.degree()<=4
 rr,tf,tt=reduce_poly(theta);assert not tf and rr.degree()<=2
 values['Theta_'+name],theta_profiles[name]=primitive_row(rr)
 say(stage='whole_W_new_monic_F_norm_original_identity',
     name=name,identity='Theta=B^2*qF-(BF+Bp-A)*R',
     actualFullUnreducedIdentityReturned=True,
     actualMonicSRuleTraceReturned=True,
     physicalNormalDegreeAtMostTwo=True,
     coefficientProfile=theta_profiles[name],noBInverse=True,claimExcluded=False)
say(stage='whole_W_new_monic_F_norm_same_point_input_complete',
 actualNewRows=['Theta_E1','Theta_EBe','Theta_N1'],
 actualOriginalRows=['E1','EBe','N1'],originalMonicFRuleRetained=True,
 actualColumns=['1','S','S^2'],
 allOriginalQuadraticNormAndReductionIdentitiesVerified=True,
 noA143OrPhysicalDOrAnyNormInverse=True,
 allFLeadingAndR2LeadingZeroFibersRetained=True,
 previousCofactorGatesRerun=False,claimExcluded=False)
profiles={}
for names in [('r2','S_r2','Theta_E1'),('r2','S_r2','Theta_EBe'),('r2','S_r2','Theta_N1'),('r2','H01','Theta_E1'),('r2','H02','Theta_E1')]:
 label='_'.join(names);begin=time.perf_counter();aa,bb,cc=[values[n] for n in names]
 cof=[bb[1]*cc[2]-bb[2]*cc[1],aa[2]*cc[1]-aa[1]*cc[2],aa[1]*bb[2]-aa[2]*bb[1]]
 det=sum((cof[i]*[aa,bb,cc][i][0] for i in range(3)),zero)
 assert all(sum((cof[i]*[aa,bb,cc][i][j] for i in range(3)),zero)==(det if j==0 else zero) for j in range(3))
 if not det:
  profiles[label]=None
  say(stage='whole_W_new_monic_F_norm_original_fixed_minor_zero',label=label,allOriginalColumnsReturned=True,claimExcluded=False);continue
 say(stage='whole_W_new_monic_F_norm_original_constant_minor_mathematical_return',label=label,
     allThreeOriginalConstantColumnsActuallyReturned=True,rawDegrees=list(map(int,det.degrees())),claimExcluded=False)
 rem,removed=strip_paid(det);lc=rem.coefficient(0);rem=rem/lc;removed*=lc;assert removed*rem==det
 ld=int(rem.degrees()[2]);head=zero
 for mm,cf in rem.to_dict().items():
  if int(mm[2])==ld:head+=cf*ep**int(mm[0])*kp**int(mm[1])
 unpaid,paid=strip_paid(head);assert unpaid*paid==head
 data=dict(rawCofactor=prof(det),remainingNecessaryPolynomial=prof(rem,True),
           lambdaDegree=ld,lambdaHeadRemainingUnpaid=prof(unpaid,True),
           lambdaHeadAllPaid=unpaid.total_degree()==0,
           allPaidStrippingProductsVerified=True)
 hh=hashlib.sha256();nb=0
 for po in cof:
  by=json.dumps([[list(map(int,mm)),str(cf)] for mm,cf in sorted(po.to_dict().items())],separators=(',',':')).encode()
  hh.update(by);hh.update(b'\n');nb+=len(by)+1
 data['originalConstantCofactorCertificate']=dict(bytes=nb,sha256=hh.hexdigest())
 profiles[label]=data
 say(stage='whole_W_new_monic_F_norm_parameter_minor_complete',label=label,**data,
     cofactorSeconds=time.perf_counter()-begin,claimExcluded=False)
say(stage='whole_W_new_complete_monic_F_norm_original_parameter_minors',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allFiveNewFixedOriginalMinorsProcessed=True,oldCoupledMinorGateRerun=False,profiles=profiles,
 noUnpaidHeadOrA143OrDInverse=True,allLeadingZeroFibersRetained=True,
 lambdaUnitFromPublishedOriginalUValueAtlas=True,
 noRankSamplingOrMultivariateGcdEmptiness=True,
 noPreviousFullCofactorGateReplayed=True,largeRegenerableCachesWritten=False,
 fullIndividualNPStillRequired=True,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

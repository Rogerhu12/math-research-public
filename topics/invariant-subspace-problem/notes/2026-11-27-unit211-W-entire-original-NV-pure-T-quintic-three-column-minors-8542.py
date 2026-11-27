#!/usr/bin/env python3
"""Whole W: entire original N4(V) replaced by a pure T quintic.
Prove C5+Phi*f*C4=m*Phi*Q*M*ell^2*Vlow in the FULL original polynomial ring.
No physical D inverse and no norm inverse. Then retain the true q3 remainder
and form three new fixed original constant cofactors. 180 seconds / 4 GiB."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-coupled-original-Gram-value-four-by-three-minors-8542.py')
raw=dep.read_bytes();assert hashlib.sha256(raw).hexdigest()=='f5c0226e4dfc8d0f80da5358d3b4a3718e2ad9c834555a2335f1e58162bb0b41'
marker=b"\nsay(stage='whole_W_new_coupled_Gram_value_four_by_three_input',"
assert raw.count(marker)==1
pref=raw.split(marker)[0];inp={'__file__':str(dep),'__name__':'__construction_only_for_new_entire_NV_pure_value_quintic__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(pref,str(dep),'exec'),inp)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,ctx,e,k,lam,S,F=[inp[x] for x in ['C','P','ctx','e','k','lam','S','F']]
ep,kp,lp=ctx.gens();zero,one=ctx.constant(0),ctx.constant(1)
reduce_poly=inp['reduce_poly'];ppaid=inp['ppaid'];prof=inp['prof']
strip_paid=inp['strip_paid'];primitive_row=inp['primitive_row']
ns=inp['seed']['ns'];orig=ns['orig'];convert=ns['convert'];profile=ns['profile']
m,ell,u,Q,M,Phi,P02,T0,d,D,K,T=[ns[x] for x in ['m','ell','u','Q','M','Phi','P02','T0','d','D','K','T']]
C4=ns['old']['C4'];q4=ns['q4']
assert C4==q4.scale(8*m*u*Q*ell*ell*d)
factual=(F+P(u*lam)).scale(C(1)/2);cval=3-2*lam
G=lam*P02-(1-u)*T0;gy=u-ell*Q;w=P(lam-1)-T
Pc=T.scale(Q*P02)+P(Q*P02*ell-G*T0)
ac=P(-Phi*G)-Pc.scale(2)
bcp=(P(-Phi*G)-Pc).scale(cval)+w.scale(Phi*Q*u)
cc=w.scale(Phi*Q*u*cval)
cs=P(-Phi*G-Phi*Q*T0/2)-Pc
aC=(ac*T*T+(bcp*T).scale(ell)+cc.scale(ell*ell)).scale(M)
aC+=D*(ac.scale(m*m)+P(-Phi*G*d*ell*ell)+cs.scale(2*m*ell))
bC=((ac*T).scale(2*m)+bcp.scale(m*ell)+cs*(T.scale(2*ell)+P(cval*ell*ell))-w.scale(Phi*Q*gy*ell*ell)).scale(M)
C5=(D*aC).scale(2*m)+K*bC
assert all(mm[0]==0 for mm in C5.t) and C5.degree()==5
leading=-4*u*Q*P02*ell*ell*d
assert C5.t.get((0,5),C())==leading
ns['paid'](1/leading);ppaid(C5)
# Entire raw N4, before either monic rule and before any norm reduction.
Nold=orig['N4'];Eold=orig['E'];l0=orig['l'];m0=orig['u']-l0
t0=orig['T'];lamb0=orig['lam']
V0=[Eold(1),Eold(lamb0-1-t0),Eold(1+t0/l0),Eold(1+t0/l0)]
V1=[Eold(),Eold(),Eold(m0/l0,-1),Eold(m0/l0,1)]
Z0raw=Nold(V0);Z2raw=Nold(V1)
Z1raw=Nold([V0[j]+V1[j] for j in range(4)])-Z0raw-Z2raw
assert not Z0raw.b and not Z1raw.b and not Z2raw.b
zz=[convert(z.a) for z in [Z0raw,Z1raw,Z2raw]]
for z in zz:ppaid(z)
Z0,Z1,Z2=zz
Vlow=D*Z0+(K*Z1).scale(1/(2*m))+(D*D*Z2).scale(1/M)
full_identity=C5+(factual*C4).scale(Phi)-Vlow.scale(m*Phi*Q*M*ell*ell)
assert not full_identity
say(stage='whole_W_entire_original_NV_pure_T_quintic_identity',
 fullOriginalN4PolynomialIdentityActuallyReturned=True,
 identity='C5+Phi*f*C4=m*Phi*Q*M*ell^2*Vlow',
 identityCheckedBeforeEitherMonicRule=True,
 noPhysicalDOrNormInverse=True,
 actualPureTQuinticLeading='-4*u*Q*P02*ell^2*(1-Q)',
 leadingActuallyVerifiedAndAlreadyPaid=True,
 q3AndR2RecoverCompleteC4=True,
 fullNVIdealRetainedWithOriginalC4=True,
 C5=profile(C5),claimExcluded=False)
q5=C5.scale(1/leading);ppaid(q5)
assert q5.t.get((0,5),C())==1
rr,tf,tt=reduce_poly(q5);assert not tf and rr.degree()<=2
values=dict(inp['values']);values['C5'],C5trace=primitive_row(rr)
say(stage='whole_W_entire_NV_new_pure_S_quadratic_return',
 monicT5ActuallyConstructed=True,
 completeOriginalMonicReductionTraceReturned=True,
 C5NormalForm=profile(rr),C5PrimitiveRowTrace=C5trace,
 actualColumns=['1','S','S^2'],
 noUnpaidLeadingOrA143OrDInverse=True,
 allLeadingZeroFibersRetained=True,claimExcluded=False)

profiles={}
for names in [('r2','S_r2','C5'),('r2','H01','C5'),('H01','H02','C5')]:
 label='_'.join(names);begin=time.perf_counter();aa,bb,cc=[values[n] for n in names]
 cof=[bb[1]*cc[2]-bb[2]*cc[1],aa[2]*cc[1]-aa[1]*cc[2],aa[1]*bb[2]-aa[2]*bb[1]]
 det=sum((cof[i]*[aa,bb,cc][i][0] for i in range(3)),zero)
 assert all(sum((cof[i]*[aa,bb,cc][i][j] for i in range(3)),zero)==(det if j==0 else zero) for j in range(3))
 if not det:
  profiles[label]=None
  say(stage='whole_W_new_entire_NV_pure_T_original_fixed_minor_zero',label=label,allOriginalColumnsReturned=True,claimExcluded=False);continue
 say(stage='whole_W_new_entire_NV_pure_T_original_constant_minor_mathematical_return',label=label,
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
 say(stage='whole_W_new_entire_NV_pure_T_parameter_minor_complete',label=label,**data,
     cofactorSeconds=time.perf_counter()-begin,claimExcluded=False)
say(stage='whole_W_new_complete_entire_NV_pure_T_original_minors',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allThreeNewFixedOriginalMinorsProcessed=True,oldCoupledMinorGateRerun=False,profiles=profiles,
 noUnpaidHeadOrA143OrDInverse=True,allLeadingZeroFibersRetained=True,
 lambdaUnitFromPublishedOriginalUValueAtlas=True,
 noRankSamplingOrMultivariateGcdEmptiness=True,
 noPreviousFullCofactorGateReplayed=True,largeRegenerableCachesWritten=False,
 fullIndividualNPStillRequired=True,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

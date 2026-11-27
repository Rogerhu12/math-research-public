#!/usr/bin/env python3
"""Whole W: new lower-degree complete original eleven-row six-column input.
Replace D^2 N / D^3 P pairs by their D-linear odd equations using R6 and NS/PS.
Keep the entire N4(V) through its exact s-quadratic form, also only D-linear.
Only prior monic construction and class definitions are regenerated; neither
the old twelve multiplication gate nor the forty-megabyte row gate is rerun.
180 seconds / 4 GiB. No physical D or norm inverse."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-global-monic-T3-F2-full-original-six-column-return-8542.py')
raw=dep.read_bytes();assert hashlib.sha256(raw).hexdigest()=='394bb2ed7d65474e46a693c4eab6474e36841b65c4dc49c5b499317884713a68'
marker=b"\nsay(stage='whole_W_new_actual_monic_T3_F2_input',"
assert raw.count(marker)==1
pref=raw.split(marker)[0]
a=raw.index(b'class A6:\n');b=raw.index(b'pointrows=[];labels=[]\n')
assert a<b
classes=raw[a:b]
ns={'__file__':str(dep),'__name__':'__construction_and_classes_only_for_new_D_linear_original_input__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(pref+b'\n'+classes,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,A6,E6=[ns[n] for n in ['C','P','A6','E6']]
m,ell,M,P02,lam,d,D,K,T,q4=[ns[n] for n in ['m','ell','M','P02','lam','d','D','K','T','q4']]
orig=ns['orig'];original=ns['original'];convert=ns['convert']
reduce_poly=ns['reduce_poly'];ppaid=ns['ppaid'];profile=ns['profile'];digest=ns['digest_parts']
rows=[];labels=[]
def save(name,v,route):
 pp=A6(v).p;ppaid(pp);rows.append(pp);labels.append(name)
 say(stage='whole_W_new_D_linear_original_row_mathematical_return',name=name,
     route=route,allSixOriginalNormalCoefficientsActuallyReturned=True,
     everyNewRuleRewriteProductVerified=True,claimExcluded=False)
 say(stage='whole_W_new_D_linear_original_row_profile',name=name,
     normalForm=profile(pp),claimExcluded=False)
for name in ['E1','EBe','EBo','N1','NS','PS']:
 rr,tf,tt=reduce_poly(original[name])
 save(name,A6.remainder(rr),'frozen original Gram polynomial as new low-input coefficient')
r2,tf,tt=reduce_poly(q4);assert not tf and r2.degree()<=2
save('original_q4_remainder_r2',A6.remainder(r2),'retained full original C4; no new quadratic head inverse')
R6=(K*K).scale(M)-(D**3).scale(4*m*m)
rr,tf,tt=reduce_poly(R6);assert not tf
save('original_same_value_R6',A6.remainder(rr),'retained complete original second/third moment condition')
DQ,TQ,KQ=A6(D),A6(T),A6(K);D2=DQ*DQ
A0=A6(1)+TQ.scale(1/ell)
Nold,Pold=orig['N4'],orig['P2'];gram=orig['rows']
nbraw=Nold(gram[2]).b;pbraw=Pold(gram[2]).b
nbp,pbp=convert(nbraw),convert(pbraw);ppaid(nbp);ppaid(pbp)
nb,pb=A6(nbp),A6(pbp)
Nlow=DQ*nb+(KQ*A0).scale(2*lam*P02/m)+D2.scale(4*lam*P02*m/(ell*M))
save('D_linear_individual_N_odd_complete',Nlow,
     'DNodd=D*Nlow+lambda*P02*R6/(m*ell*M); NS and R6 recover the even row')
Plow=DQ*pb+(KQ*A0*A0).scale(3*P02/(2*m))+(KQ*DQ).scale(P02*(3*m*m/(ell*ell)+d)/(2*m*M))+(A0*D2).scale(6*P02*m/(ell*M))
save('D_linear_individual_P_odd_complete',Plow,
     'DPodd=D^2*Plow+explicit R6 multiple; PS and R6 recover the even row')
# Full N4(V0+s*V1), not a selected weighted trace or a Phi multiple.
Eold=orig['E'];l0=orig['l'];m0=orig['u']-l0;t0=orig['T'];lamb0=orig['lam']
V0=[Eold(1),Eold(lamb0-1-t0),Eold(1+t0/l0),Eold(1+t0/l0)]
V1=[Eold(),Eold(),Eold(m0/l0,-1),Eold(m0/l0,1)]
Z0raw=Nold(V0);Z2raw=Nold(V1)
Z1raw=Nold([V0[j]+V1[j] for j in range(4)])-Z0raw-Z2raw
assert not Z0raw.b and not Z1raw.b and not Z2raw.b
zz=[]
for z in [Z0raw,Z1raw,Z2raw]:
 pp=convert(z.a);ppaid(pp);zz.append(A6(pp))
Z0,Z1,Z2=zz
Vlow=DQ*Z0+(KQ*Z1).scale(1/(2*m))+(D2*Z2).scale(1/M)
save('D_linear_entire_original_N4_Vval',Vlow,
     'N4(D*Vval)=D*Vlow+Z2*R6/(4*m^2*M); entire original quadratic form')
assert len(rows)==11 and len(labels)==11
say(stage='whole_W_new_complete_original_D_linear_eleven_by_six_input',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 frozenOldSourceSHA256='394bb2ed7d65474e46a693c4eab6474e36841b65c4dc49c5b499317884713a68',
 exactOriginalLoweringIdentitySourceSHA256='f083869fe46a453e014dabd0a8b3079ed0a5fa80d956d1694e9d2813075064df',
 classAndConstructionOnly=True,oldLargeThirteenRowAndTwelveColumnGatesRerun=False,
 scalarVariables=['e','k','lambda'],basis=['1','S','S^2','F','F*S','F*S^2'],
 actualRows=labels,allElevenOriginalNecessaryRowsActuallyReturned=True,
 allThreeNewLowerDOriginalEquationsActuallyConstructed=True,
 originalDNonzeroDomainForEquivalenceRetained=True,
 noPhysicalDOrAnyNormInverse=True,noA143OrB239Inverse=True,
 r2LeadingZeroFiberRetained=True,
 actualNewOriginalRuleRewriteProducts=ns['rewrite_count'],
 allFinalCoefficientDenominatorsActuallyPaid=True,
 distinctPaidDenominators=len(ns['den_checked']),
 coefficientCertificate=digest(rows),largeRegenerableCachesWritten=False,
 noParameterCofactorYetComputed=True,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

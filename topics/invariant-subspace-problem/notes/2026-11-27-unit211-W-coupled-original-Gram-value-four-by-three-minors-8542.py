#!/usr/bin/env python3
"""Whole W: new mean/N1 F-elimination coupled to original r2.
Four exact maximal constant minors of a fixed four-by-three same-S matrix.
All F-leading and r2-leading zero fibers retained; no A143 inverse.
Regenerate construction inputs only. 180 seconds / 4 GiB."""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-global-monic-T3-pure-value-three-column-cofactors-8542.py')
raw=dep.read_bytes();assert hashlib.sha256(raw).hexdigest()=='50564e34579c279923537519429c2a230093619488b5990b40704dcdd1a2a5d6'
marker=b"\nsay(stage='whole_W_new_pure_T_original_three_column_input_complete',"
assert raw.count(marker)==1
pref=raw.split(marker)[0];seed={'__file__':str(dep),'__name__':'__construction_only_for_new_coupled_Gram_value_minors__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(pref,str(dep),'exec'),seed)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,ctx,e,k,lam,S=[seed[x] for x in ['C','P','ctx','e','k','lam','S']]
ep,kp,lp=ctx.gens();zero,one=ctx.constant(0),ctx.constant(1)
reduce_poly=seed['reduce_poly'];ppaid=seed['ppaid'];prof=seed['prof']
# The original U atlas explicitly gives lambda=m/U0 != 0 on this chart.
seed['atoms'].append(lam.n)
strip_paid=seed['strip_paid'];primitive_row=seed['primitive_row']
original=seed['ns']['original'];F=seed['ns']['F']
def primitive_FS(pp):
 ppaid(pp);den=one
 for cf in pp.t.values():
  gg=den.gcd(cf.d);quo=den/gg;assert quo*gg==den;den=quo*cf.d
 nums={}
 for mm,cf in pp.t.items():
  quo=den/cf.d;assert quo*cf.d==den;nums[mm]=cf.n*quo
 content=next(iter(nums.values()))
 for z in nums.values():content=content.gcd(z)
 unused,removed=strip_paid(content);rr=P()
 for mm,z in nums.items():
  zz=z/removed;assert zz*removed==z;rr+=P.monomial(mm,C(zz))
  assert C(zz*removed,den)==pp.t[mm]
 return rr,dict(originalDenominator=prof(den),paidContentRemoved=prof(removed),allOriginalCoefficientsActuallyMultipliedBack=True)
R=[];AA=[];BB=[];provenance={}
for name in ['E1','EBe','N1']:
 rr,tf,tt=reduce_poly(original[name])
 assert all(mm[0]<=1 for mm in rr.t)
 pp,rec=primitive_FS(rr);R.append(pp);provenance[name]=rec
 aa=P();bb=P()
 for mm,cf in pp.t.items():
  if mm[0]==0:aa+=P.monomial(mm,cf)
  else:bb+=P.monomial((0,mm[1]),cf)
 assert pp==aa+F*bb and aa.degree()<=2 and bb.degree()<=1
 AA.append(aa);BB.append(bb)
values={'r2':seed['values']['r2'],'S_r2':seed['values']['S_r2']};pairprofiles={}
for i,j in [(0,1),(0,2),(1,2)]:
 name='H'+str(i)+str(j)
 hh=BB[j]*R[i]-BB[i]*R[j]
 assert hh==AA[i]*BB[j]-AA[j]*BB[i]
 assert all(mm[0]==0 for mm in hh.t) and hh.degree()<=3
 rr,tf,tt=reduce_poly(hh);assert not tf and rr.degree()<=2
 values[name],pairprofiles[name]=primitive_row(rr)
say(stage='whole_W_new_coupled_Gram_value_four_by_three_input',
 originalMeans=['E1','EBe','N1'],originalMeanTraceProfiles=provenance,
 exactPairDefinitions='Hij=Bj*Ri-Bi*Rj; no Bi inversion',
 allThreeOriginalPairAndMonicRuleProductsActuallyVerified=True,
 actualRows=['r2','S_r2','H01','H02'],actualColumns=['1','S','S^2'],
 pairProfiles=pairprofiles,allFLeadingAndR2LeadingZeroFibersRetained=True,
 noA143OrPhysicalDInverse=True,claimExcluded=False)
profiles={}
for names in itertools.combinations(['r2','S_r2','H01','H02'],3):
 label='_'.join(names);begin=time.perf_counter();aa,bb,cc=[values[n] for n in names]
 cof=[bb[1]*cc[2]-bb[2]*cc[1],aa[2]*cc[1]-aa[1]*cc[2],aa[1]*bb[2]-aa[2]*bb[1]]
 det=sum((cof[i]*[aa,bb,cc][i][0] for i in range(3)),zero)
 assert all(sum((cof[i]*[aa,bb,cc][i][j] for i in range(3)),zero)==(det if j==0 else zero) for j in range(3))
 if not det:
  profiles[label]=None
  say(stage='whole_W_coupled_original_fixed_minor_zero',label=label,allOriginalColumnsReturned=True,claimExcluded=False);continue
 say(stage='whole_W_coupled_original_constant_minor_mathematical_return',label=label,
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
 say(stage='whole_W_new_coupled_Gram_value_parameter_minor_complete',label=label,**data,
     cofactorSeconds=time.perf_counter()-begin,claimExcluded=False)
say(stage='whole_W_new_complete_coupled_Gram_value_four_by_three_minors',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allFourFixedMaximalOriginalMinorsProcessed=True,profiles=profiles,
 noUnpaidHeadOrA143OrDInverse=True,allLeadingZeroFibersRetained=True,
 lambdaUnitFromPublishedOriginalUValueAtlas=True,
 noRankSamplingOrMultivariateGcdEmptiness=True,
 noPreviousFullCofactorGateReplayed=True,largeRegenerableCachesWritten=False,
 fullIndividualNPStillRequired=True,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

#!/usr/bin/env python3
"""New whole-W pure-T three-column original parameter cofactors.
Use the paid monic T3, retain the original q4 remainder r2 and original R6,
and compute three fixed 3x3 constant-column identities. No new head inverse.
No old six-column or thirteen-row gate is replayed. 180 seconds / 4 GiB."""
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
ns={'__file__':str(dep),'__name__':'__construction_only_for_new_original_pure_T_cofactors__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(pref,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P=ns['C'],ns['P'];ctx=ns['old']['ctx'];ep,kp,lp=ctx.gens()
zero,one=ctx.constant(0),ctx.constant(1)
e,k,u,Q,ell,M,Phi,P02,J,T0,Pf,d,m,lam,S,q3,q4,D,K=[
 ns[x] for x in ['e','k','u','Q','ell','M','Phi','P02','J','T0','Pf','d','m','lam','S','q3','q4','D','K']]
reduce_poly=ns['reduce_poly'];paid=ns['paid'];ppaid=ns['ppaid']
atoms=list(ns['new_atoms'])
more=[
 ('2e+1',2*e+1),('k+1',k+1),('k+2',k+2),('k+4',k+4),
 ('u-Q',u-Q),('H',4*e*k-k*k-4*k-8),
 ('C9',4*e*e*k*k-e*(k**4+9*k**3+20*k*k+16*k)+k**3+10*k*k+24*k+16),
 ('J19',16*e**4*k**3-8*e**3*k**4-16*e**3*k**3-96*e**3*k*k-e*e*k**5-8*e*e*k**4+24*e*e*k**3+64*e*e*k*k+192*e*e*k-2*e*k**5-14*e*k**4-12*e*k**3-128*e-k**5-10*k**4-40*k**3-104*k*k-160*k-128),
 ('D27',16*e**5*k**4-4*e**4*k**5+32*e**4*k**4+2*e**3*k**6-12*e**3*k**5-96*e**3*k**4-384*e**3*k**3-384*e**3*k*k+3*e*e*k**6+8*e*e*k**5+60*e*e*k**4+384*e*e*k**3+1088*e*e*k*k+1024*e*e*k-10*e*k**5-28*e*k**4+48*e*k**3+64*e*k*k-512*e*k-768*e-k**6-18*k**5-120*k**4-440*k**3-1008*k*k-1344*k-768)
]
atoms += [C(v).n for name,v in more]
def prof(pp,include=False):
 dd=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(pp.to_dict().items())]
 bb=json.dumps(dd,separators=(',',':')).encode()
 rec=dict(degrees=list(map(int,pp.degrees())),totalDegree=int(pp.total_degree()),terms=len(dd),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if include and len(bb)<=8192:rec['coefficients']=dd
 return rec
def strip_paid(pp):
 remaining=pp;removed=one
 for atom in atoms:
  while True:
   gg=remaining.gcd(atom)
   if gg.total_degree()==0:break
   qq=remaining/gg;assert qq*gg==remaining;remaining=qq;removed*=gg
 return remaining,removed
def primitive_row(pp):
 pp=P(pp);assert all(mm[0]==0 and mm[1]<=2 for mm in pp.t);ppaid(pp)
 cc=[pp.t.get((0,j),C()) for j in range(3)]
 den=one
 for cf in cc:
  gg=den.gcd(cf.d);quo=den/gg;assert quo*gg==den
  den=quo*cf.d
 row=[]
 for cf in cc:
  quo=den/cf.d;assert quo*cf.d==den
  row.append(cf.n*quo)
 common=next((p for p in row if p),None)
 if common is None:return row,dict(zeroRow=True)
 for p in row:common=common.gcd(p)
 unused,removed=strip_paid(common)
 result=[p/removed for p in row]
 assert all(result[j]*removed==row[j] and C(result[j]*removed,den)==cc[j] for j in range(3))
 # Each removed factor is a divisor of named already paid numerator atoms.
 return result,dict(commonDenominator=prof(den),paidContentRemoved=prof(removed),allThreeOriginalEmbeddingProductsActuallyVerified=True)
r2,tf,tt=reduce_poly(q4);assert not tf and r2.degree()<=2
R6=(K*K).scale(M)-(D**3).scale(4*m*m)
r6,tf,tt=reduce_poly(R6);assert not tf and r6.degree()<=2
values={};traces={}
for name,pp in [('r2',r2),('S_r2',S*r2),('S2_r2',S*S*r2),
                ('R6',r6),('S_R6',S*r6)]:
 rr,tf,tt=reduce_poly(pp);assert not tf
 values[name],traces[name]=primitive_row(rr)
say(stage='whole_W_new_pure_T_original_three_column_input_complete',
 originalValueRows=['q4_remainder_r2','original_same_value_R6'],
 trueColumns=['1','S','S^2'],allFiveOriginalRuleTracesActuallyReturned=True,
 rowTraces=traces,noUnpaidLeadingInverse=True,
 originalR2LeadingZeroFiberRetained=True,claimExcluded=False)
pairs=[('r2_norm',['r2','S_r2','S2_r2']),
       ('r2_R6_first',['r2','S_r2','R6']),
       ('r2_R6_second',['r2','R6','S_R6'])]
profiles={}
for label,names in pairs:
 begin=time.perf_counter();aa,bb,cc=[values[n] for n in names]
 cof=[bb[1]*cc[2]-bb[2]*cc[1],
      aa[2]*cc[1]-aa[1]*cc[2],
      aa[1]*bb[2]-aa[2]*bb[1]]
 det=sum((cof[j]*[aa,bb,cc][j][0] for j in range(3)),zero)
 assert all(sum((cof[i]*[aa,bb,cc][i][j] for i in range(3)),zero)==(det if j==0 else zero) for j in range(3))
 if not det:
  profiles[label]=None
  say(stage='whole_W_new_pure_T_constant_cofactor_zero',label=label,fullOriginalColumnsActuallyReturned=True,claimExcluded=False)
  continue
 say(stage='whole_W_new_pure_T_constant_cofactor_mathematical_return',
     label=label,originalRows=names,allThreeOriginalConstantColumnsActuallyVerified=True,
     rawDegree=list(map(int,det.degrees())),claimExcluded=False)
 remaining,removed=strip_paid(det);lc=remaining.coefficient(0)
 remaining=remaining/lc;removed*=lc
 assert removed*remaining==det
 degree=int(remaining.degrees()[2]);head=zero
 for mm,cf in remaining.to_dict().items():
  if int(mm[2])==degree:head+=cf*ep**int(mm[0])*kp**int(mm[1])
 unpaid_head,paid_head=strip_paid(head)
 assert unpaid_head*paid_head==head
 data=dict(rawCofactor=prof(det),remainingNecessaryPolynomial=prof(remaining,True),
           lambdaDegree=degree,lambdaLeadingAfterOnlyPaidStripping=prof(unpaid_head,True),
           wholeLambdaLeadingPaid=unpaid_head.total_degree()==0,
           allStrippingProductsActuallyVerified=True,
           noLambdaLeadingZeroFiberRemoved=True)
 # Small certificate only; no expanded matrix is written.
 hh=hashlib.sha256();nbytes=0
 for cf in cof:
  bts=json.dumps([[list(map(int,mm)),str(v)] for mm,v in sorted(cf.to_dict().items())],separators=(',',':')).encode()
  hh.update(bts);hh.update(b'\n');nbytes+=len(bts)+1
 data['originalCofactorCertificate']=dict(bytes=nbytes,sha256=hh.hexdigest())
 profiles[label]=data
 say(stage='whole_W_new_pure_T_three_column_parameter_curve_complete',
     label=label,**data,cofactorSeconds=time.perf_counter()-begin,claimExcluded=False)
say(stage='whole_W_original_pure_T_three_column_parameter_cofactors_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allThreeFixedOriginalCofactorsProcessed=True,necessaryProfiles=profiles,
 originalRuleRewriteProducts=ns['rewrite_count'],
 allUnpaidLeadingZeroFibersRetained=True,noDOrNormInverse=True,
 fullIndividualNPStillRequired=True,noMultivariateGcdEmptinessClaim=True,
 largeRegenerableCachesWritten=False,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

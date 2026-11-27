#!/usr/bin/env python3
"""Current W: genuinely new two-column original system on A143 != 0.
A143 is the common affine-F / pure-S2 cofactor head.  Its entire zero fiber
remains outside this explicitly stated chart.  Return all original means,
N1, weighted NS/PS, qT/R4, and true F/S multiplications with complete traces.
Compute selected original two-column cofactors; no parameter/unit claim.
180 seconds / 4 GiB; no old row/matrix or factorization gate is repeated.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-global-monic-T4-F2-original-eight-column-return-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='af928bbd7240d5235feb3188e65fc8ee5c92aaf8866433a077f1ab96b7507913'
marker=b"say(stage='new_W_actual_monic_T4_F2_same_original_input',"
assert raw.count(marker)==1
prefix=raw.split(marker)[0];ns={'__file__':str(dep),'__name__':'__new_original_A143_nonzero_two_column_input__'}
log=io.StringIO()
with contextlib.redirect_stdout(log):exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,F,S,qF,qT,R4=[ns[n] for n in ['C','P','F','S','qF','qT','R4']]
original,profile,ctx,zero,one=[ns[n] for n in ['original','profile','ctx','zero','one']]
def redF2(pp):
 org=P(pp);rr=P(pp);tr=P()
 while any(mm[0]>=2 for mm in rr.t):
  mm=max((m for m in rr.t if m[0]>=2),key=lambda a:(a[0],a[1]))
  term=P.monomial((mm[0]-2,mm[1]),rr.t[mm]);rr=rr-term*qF;tr=tr+term
 assert rr+tr*qF==org;return rr,tr
labels=['E1','EBe','N1'];rrs=[];trs=[]
for name in labels:
 rr,tr=redF2(original[name])
 assert all(mm in [(0,0),(0,1),(0,2),(1,0),(1,1)] for mm in rr.t)
 rrs.append(rr);trs.append(tr)
def col(mm):return [r.t.get(mm,C()) for r in rrs]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
wl=cross(col((1,1)),col((0,2)));wq=cross(col((1,0)),col((1,1)))
lin=sum((rrs[i].scale(wl[i]) for i in range(3)),P())
quad=sum((rrs[i].scale(wq[i]) for i in range(3)),P())
tl=sum((trs[i].scale(wl[i]) for i in range(3)),P())
tq=sum((trs[i].scale(wq[i]) for i in range(3)),P())
assert lin+tl*qF==sum((original[labels[i]].scale(wl[i]) for i in range(3)),P())
assert quad+tq*qF==sum((original[labels[i]].scale(wq[i]) for i in range(3)),P())
alpha=lin.t.get((1,0),C())
assert alpha and quad.t.get((0,2),C())==alpha
assert all(mm in [(1,0),(0,1),(0,0)] for mm in lin.t)
assert all(mm in [(0,2),(0,1),(0,0)] for mm in quad.t)
qLin=lin.scale(1/alpha);qQuad=quad.scale(1/alpha)
assert qLin.t[(1,0)]==1 and qQuad.t[(0,2)]==1
# This is explicitly A143 != 0: alpha is paid times the actual A143.
# Preserve every alpha-zero point for another chart; no global payment claimed.
units=list(ns['paid_atoms'])+[alpha.n];checked=set()
def paid(c):
 c=C(c);key=str(c.d)
 if key in checked:return
 rem=c.d
 for atom in units:
  while True:
   g=rem.gcd(atom)
   if g.total_degree()==0:break
   nxt=rem/g;assert nxt*g==rem;rem=nxt
 assert rem.total_degree()==0,'denominator outside paid weights and A143 chart'
 checked.add(key)
def ppcheck(pp):
 for c in pp.t.values():paid(c)
for pp in [qLin,qQuad,lin,quad,tl,tq]:ppcheck(pp)
def digest(parts):
 h=hashlib.sha256();count=0
 for po in parts:
  bb=json.dumps(po.data(),separators=(',',':')).encode();h.update(bb);h.update(b'\n');count+=len(bb)+1
 return dict(bytes=count,sha256=h.hexdigest())
say(stage='W_A143_nonzero_new_two_column_original_environment',
 sharedAffineFAndPureS2HeadActuallyEqual=True,
 fullOriginalCofactorTracesActuallyReturned=True,
 chart='A143 != 0 only; alpha-zero entire fiber retained separately',
 monicLinearF=profile(qLin),monicS2=profile(qQuad),
 sourceMeanQFStillRequiredAsOriginalEquation=True,
 claimExcluded=False)
def red2(pp):
 org=P(pp);rr=P(pp);uf=P();us=P()
 while any(mm[0]>=1 for mm in rr.t):
  mm=max((m for m in rr.t if m[0]>=1),key=lambda a:(a[0],a[1]))
  term=P.monomial((mm[0]-1,mm[1]),rr.t[mm]);rr=rr-term*qLin;uf=uf+term
 while any(mm[1]>=2 for mm in rr.t):
  mm=max((m for m in rr.t if m[1]>=2),key=lambda a:(a[1],a[0]))
  term=P.monomial((mm[0],mm[1]-2),rr.t[mm]);rr=rr-term*qQuad;us=us+term
 assert rr+uf*qLin+us*qQuad==org
 assert all(mm in [(0,0),(0,1)] for mm in rr.t)
 for po in [rr,uf,us]:ppcheck(po)
 return [rr.t.get((0,0),C()),rr.t.get((0,1),C())],uf,us
def rowpoly(row):return P(row[0])+S.scale(row[1])
rows={}
target=[(name,original[name]) for name in ['E1','EBe','EBo','N1','NS','PS']]
target += [('original_mean_qF',qF),('original_value_qT',qT),('original_value_R4',R4)]
for name,po in target:
 begin=time.perf_counter();row,uf,us=red2(po)
 assert rowpoly(row)+uf*qLin+us*qQuad==po
 rows[name]=row
 say(stage='W_A143_nonzero_original_two_column_return',name=name,
     remainder=profile(rowpoly(row)),
     allOriginalCoefficientProductsActuallyVerified=True,
     originalTrace=digest([rowpoly(row),uf,us]),
     rowSeconds=time.perf_counter()-begin,claimExcluded=False)
maps={}
for name,var in [('F',F),('S',S)]:
 mat=[]
 for po in [P(1),S]:
  row,uf,us=red2(po*var);assert rowpoly(row)+uf*qLin+us*qQuad==po*var
  mat.append(row)
 maps[name]=mat
 say(stage='W_A143_nonzero_actual_two_column_multiplication',variable=name,
     allTwoTrueProductsActuallyReturned=True,
     matrixCertificate=digest([rowpoly(r) for r in mat]),claimExcluded=False)
drow,du,dv=red2(ns['D'])
assert rowpoly(drow)+du*qLin+dv*qQuad==ns['D']
def polyprofile(pol,include=False):
 dd=[[list(map(int,mm)),str(cf)] for mm,cf in sorted(pol.to_dict().items())]
 bb=json.dumps(dd,separators=(',',':')).encode()
 r=dict(degrees=list(map(int,pol.degrees())),totalDegree=int(pol.total_degree()),terms=len(dd),
 bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if include and len(bb)<=8192:r['coefficients']=dd
 return r
cofresults=[]
# Each selected 2x2 constant cofactor is itself a real original combination.
# All rows are kept, including where the chosen first row vanishes.
for n1,n2 in [('original_mean_qF','E1'),('original_mean_qF','original_value_qT'),
               ('original_mean_qF','original_value_R4')]:
 begin=time.perf_counter();a=rows[n1];b=rows[n2]
 det=a[0]*b[1]-a[1]*b[0];c0=b[1];c1=-a[1]
 assert c0*a[0]+c1*b[0]==det and c0*a[1]+c1*b[1]==0
 for cf in [det,c0,c1]:paid(cf)
 if not det:
  rr=dict(pair=[n1,n2],zeroCofactor=True,allTwoColumnsActuallyReturned=True)
 else:
  rem=det.n;removed=one;parts=[]
  for ind,atom in enumerate(units):
   count=0
   while True:
    g=rem.gcd(atom)
    if g.total_degree()==0:break
    nxt=rem/g;assert nxt*g==rem
    removed*=g;rem=nxt;count+=1
   if count:parts.append(dict(unitIndex=ind,passes=count))
  lc=rem.coefficient(0);rem=rem/lc;removed*=lc
  assert rem*removed==det.n
  ld=int(rem.degrees()[2]);lead=zero
  for mm,cf in rem.to_dict().items():
   if mm[2]==ld:lead+=cf*ctx.gens()[0]**int(mm[0])*ctx.gens()[1]**int(mm[1])
  rr=dict(pair=[n1,n2],zeroCofactor=False,allTwoColumnsActuallyReturned=True,
          rawNumerator=polyprofile(det.n),removedOnlyChartUnits=parts,
          remainingNecessaryParameterPolynomial=polyprofile(rem,True),
          lambdaLeadingCoefficient=polyprofile(lead,True),
          originalCofactorCertificate=digest([P(c0),P(c1),P(det)]))
 rr['cofactorSeconds']=time.perf_counter()-begin;cofresults.append(rr)
 say(stage='W_A143_nonzero_new_original_two_column_cofactor',**rr)
say(stage='W_A143_nonzero_original_two_column_and_new_cofactors_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allNineOriginalRowsAndFourMultiplicationColumnsActuallyReturned=True,
 meanQFExplicitlyRetained=True,
 physicalDReturned=profile(rowpoly(drow)),noPhysicalDOrNormInverse=True,
 onlyNewChartInverse='A143',allA143ZeroPointsStillUnresolvedHere=True,
 distinctDenominatorsActuallyPaid=len(checked),
 ambientTwoDimensionalButFinalOriginalQuotientNotClaimedFree=True,
 completeIndividualValueNPStillRequired=True,
 wholeWExcluded=False,largeMatrixCachesWritten=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

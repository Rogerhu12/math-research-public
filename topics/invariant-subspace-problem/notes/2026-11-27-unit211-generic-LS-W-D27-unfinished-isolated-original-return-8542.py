#!/usr/bin/env python3
"""D27/F782: only previously unreturned original finite constant-algebra fibers.
Old 21400 SIGSEGV has unknown cause. Each new k factor has its own process.
The exceptional index 11/e-linear branch uses a genuinely new M5 (100x56).
Other unfinished indices use original M4, then M5 only if full rank is absent.
Only actual original constant 1 is certified, with every column multiplied back.
180 seconds / 4 GiB. No old generic unit or completed finite fiber is rerun.
"""
import sys,os,json,time,hashlib,signal,resource,subprocess,contextlib,io,math
from pathlib import Path
from fractions import Fraction
from flint import nmod_poly,fmpz_mod_poly_ctx,fq_default_ctx,fq_default_poly_ctx
start=time.perf_counter();deadline=start+177
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
def digest(obj):
 bb=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
PRIME=1009
FACTORS=[{"degree":1,"multiplicity":1,"coefficients":[39,1]},{"degree":1,"multiplicity":1,"coefficients":[209,1]},{"degree":1,"multiplicity":1,"coefficients":[721,1]},{"degree":1,"multiplicity":1,"coefficients":[857,1]},{"degree":2,"multiplicity":1,"coefficients":[405,374,1]},{"degree":2,"multiplicity":1,"coefficients":[341,442,1]},{"degree":2,"multiplicity":1,"coefficients":[756,774,1]},{"degree":2,"multiplicity":1,"coefficients":[974,781,1]},{"degree":2,"multiplicity":1,"coefficients":[51,809,1]},{"degree":2,"multiplicity":1,"coefficients":[543,943,1]},{"degree":2,"multiplicity":1,"coefficients":[120,977,1]},{"degree":3,"multiplicity":1,"coefficients":[12,14,7,1]},{"degree":3,"multiplicity":1,"coefficients":[653,130,281,1]},{"degree":3,"multiplicity":1,"coefficients":[784,85,487,1]},{"degree":3,"multiplicity":1,"coefficients":[47,504,552,1]},{"degree":3,"multiplicity":1,"coefficients":[954,435,841,1]},{"degree":3,"multiplicity":1,"coefficients":[566,746,898,1]},{"degree":3,"multiplicity":1,"coefficients":[459,489,992,1]},{"degree":4,"multiplicity":1,"coefficients":[57,805,326,69,1]},{"degree":4,"multiplicity":1,"coefficients":[949,1005,655,237,1]},{"degree":4,"multiplicity":1,"coefficients":[328,700,928,363,1]},{"degree":4,"multiplicity":1,"coefficients":[207,781,153,909,1]},{"degree":5,"multiplicity":1,"coefficients":[938,275,407,107,598,1]},{"degree":6,"multiplicity":1,"coefficients":[142,259,122,948,690,427,1]},{"degree":6,"multiplicity":1,"coefficients":[875,80,203,525,921,603,1]},{"degree":7,"multiplicity":1,"coefficients":[176,956,446,129,501,16,931,1]},{"degree":8,"multiplicity":1,"coefficients":[496,334,965,476,93,479,401,27,1]},{"degree":8,"multiplicity":1,"coefficients":[887,757,992,925,997,325,34,957,1]},{"degree":9,"multiplicity":1,"coefficients":[355,928,741,459,368,277,352,153,131,1]},{"degree":10,"multiplicity":1,"coefficients":[643,371,604,174,910,340,359,714,125,456,1]},{"degree":11,"multiplicity":1,"coefficients":[245,623,787,767,388,293,867,139,306,639,364,1]},{"degree":12,"multiplicity":1,"coefficients":[1003,413,776,410,658,116,922,550,664,747,725,966,1]},{"degree":15,"multiplicity":1,"coefficients":[240,386,264,93,837,895,359,929,111,711,373,61,709,353,524,1]},{"degree":16,"multiplicity":1,"coefficients":[34,101,355,664,144,701,437,60,252,814,843,995,188,362,491,964,1]},{"degree":17,"multiplicity":1,"coefficients":[678,257,346,266,584,627,551,752,510,359,683,443,109,714,142,748,459,1]},{"degree":20,"multiplicity":1,"coefficients":[800,587,657,586,117,458,249,950,288,780,903,474,222,570,304,777,437,339,987,774,1]},{"degree":22,"multiplicity":1,"coefficients":[255,663,149,673,1001,426,969,735,820,385,141,48,778,898,888,127,784,154,830,754,74,102,1]},{"degree":29,"multiplicity":1,"coefficients":[591,549,610,947,1006,310,583,319,312,447,763,509,578,392,138,493,26,883,940,935,370,525,660,151,680,154,518,21,736,1]},{"degree":37,"multiplicity":1,"coefficients":[261,99,882,79,84,222,203,911,707,617,48,400,633,351,379,179,118,164,393,647,613,742,329,765,447,948,467,778,407,996,935,513,244,267,446,642,212,1]},{"degree":44,"multiplicity":1,"coefficients":[604,810,958,441,121,429,851,653,564,544,308,773,868,53,786,652,491,965,601,950,176,49,116,944,870,951,57,863,517,327,378,795,416,375,92,872,389,789,800,807,908,375,380,490,1]},{"degree":52,"multiplicity":1,"coefficients":[423,284,685,755,22,602,571,192,539,150,644,22,124,472,66,195,763,989,464,385,1004,675,421,973,159,22,520,51,356,365,39,634,429,817,616,928,1005,688,845,343,434,915,67,179,308,215,590,120,285,849,883,390,1]},{"degree":63,"multiplicity":1,"coefficients":[1004,603,875,542,799,488,562,22,76,598,360,7,937,863,637,536,984,136,203,192,139,843,365,349,555,872,323,243,430,547,212,1004,117,550,13,230,526,703,257,227,677,84,130,391,151,698,647,22,4,587,427,576,601,853,842,788,914,173,419,123,441,437,636,1]},{"degree":64,"multiplicity":1,"coefficients":[451,582,786,568,163,508,3,571,49,645,120,896,204,598,426,631,366,639,524,171,175,358,193,947,235,257,299,129,728,675,420,72,396,795,145,559,536,915,98,268,668,994,199,124,71,354,575,832,117,917,5,67,533,958,855,451,95,734,24,490,481,47,225,789,1]},{"degree":73,"multiplicity":1,"coefficients":[426,410,642,544,146,305,559,180,520,341,642,963,669,966,530,404,523,987,365,175,696,374,74,531,321,203,526,825,488,37,11,205,961,91,478,134,9,956,651,17,396,352,841,503,774,576,274,74,225,887,857,694,418,56,227,124,133,458,215,991,972,764,753,891,346,1005,284,523,266,468,209,1002,252,1]},{"degree":90,"multiplicity":1,"coefficients":[526,329,275,814,852,435,18,648,914,66,55,10,887,309,452,280,370,17,901,667,624,973,878,317,342,31,205,691,119,326,823,442,524,47,567,74,748,131,241,438,350,167,413,7,615,41,16,183,687,93,510,935,20,2,957,476,21,287,395,764,469,635,745,89,62,592,291,161,496,52,488,395,766,395,775,993,194,797,134,511,33,980,562,194,206,408,671,1005,904,896,1]},{"degree":103,"multiplicity":1,"coefficients":[99,547,334,399,776,791,129,577,276,687,224,167,582,659,883,807,90,807,725,614,862,947,658,776,861,614,420,201,921,358,67,628,215,612,855,913,162,332,24,515,641,723,59,165,65,666,970,355,170,159,910,725,141,693,388,559,831,818,375,564,406,248,97,459,627,823,273,634,21,22,447,576,649,1,479,900,366,879,111,665,512,594,288,352,941,801,543,485,391,290,456,559,335,43,539,692,631,748,788,682,540,1008,616,1]}]
PREVIOUS_COMPLETE=[{"i":0,"path":"D27","eDegree":5,"certificate":{"bytes":16865,"sha256":"d5501d0ee9f33ff2393d5296b3f119be137f1b94ecfb5ecc148deeecb424520e"}},{"i":1,"path":"D27","eDegree":5,"certificate":{"bytes":16851,"sha256":"1e2ed06b5f911d20a0ca9a141337ad2482e9dc13a91a6357e8ad80fc30dbb3f6"}},{"i":2,"path":"D27","eDegree":5,"certificate":{"bytes":16858,"sha256":"72f91f946297413186ab341d9d89978d646af88a1429441de717613331110a3e"}},{"i":3,"path":"D27","eDegree":5,"certificate":{"bytes":16874,"sha256":"5f89c50e00b5dc535625e24b129602e42fc14fe9aaeca09840e90fda0d47b622"}},{"i":4,"path":"D27","eDegree":5,"certificate":{"bytes":25420,"sha256":"55c858edbc6cb03fd11d2edd6354fcdf2cc38942c97d3bffe30ae5c75559568d"}},{"i":5,"path":"D27","eDegree":5,"certificate":{"bytes":25411,"sha256":"ba3108700d69fd03657d7eeb9c7476493f965d771c7ac63f469edb9314cbf01a"}},{"i":6,"path":"D27","eDegree":5,"certificate":{"bytes":25419,"sha256":"86daba415a0494a4edddf83dd688a5f1b4e671b603247e6ed30ee95ad5dba9fd"}},{"i":7,"path":"D27","eDegree":5,"certificate":{"bytes":25439,"sha256":"add6890ce92f816e9c769913b32dfdb417e6ed94b79f3804dcb427c72c1dc0fe"}},{"i":8,"path":"D27","eDegree":5,"certificate":{"bytes":25436,"sha256":"6541da482b758cc4c4352e9b234a0cfb91e622e0fdde1f0d88d16e005bda51d4"}},{"i":9,"path":"D27","eDegree":5,"certificate":{"bytes":25415,"sha256":"e1bc69d7e6acc3fbe879cd5bfba50cb879a88497138b64a53268c6954aa038b4"}},{"i":10,"path":"D27","eDegree":5,"certificate":{"bytes":25456,"sha256":"d039428b91e506c6247e603b608b1304c377d2cff34c98dd07089119ecd4bf53"}},{"i":11,"path":"D27/b","eDegree":4,"certificate":{"bytes":27973,"sha256":"4b8702a0fbb57312843c7d2cd4d3c96c4614d2a5eb108be30b784ec85dbd059d"}},{"i":12,"path":"D27","eDegree":5,"certificate":{"bytes":33992,"sha256":"7c4e3f20eb160a3e2e8c31ab134c561316dd7c971c7b2e06633511d011be1623"}},{"i":13,"path":"D27","eDegree":5,"certificate":{"bytes":34024,"sha256":"74c4244d3072122b67cf4e5a8520a6336c2f4f1d94d536fea5d11cc44df2456a"}}]
OLD_LEFT=[[1,758,757],[1,0,0]]
OLD_RIGHT=[[739,733,460],[383,412,436],[672,79,966],[1,503,252],[1,0,0]]
OLD_SOURCE_SHA='21400b018185d10166cb6eedf441849e3fa4041259b29609f54b64f2e1bbe4a5'
OLD_ACTUAL_RUN=46004204867
OLD_ACTUAL_JOB=140523158558
HIGH_QQ_SHA='1114db34d767cb4a696161318fea9a8560349ad8d493a9ea557b291936c8cafa'
HIGH_MOD_SHA='7913fb7ab5462c8a8a8998f500ec4ddc0d1a11ef388fff4545831537cd7fbb35'
def finite_child(payload):
 signal.alarm(max(1,int(payload['budget'])))
 fi=payload['index'];fr=FACTORS[fi];coeff=fr['coefficients']
 fcmod=fmpz_mod_poly_ctx(PRIME)(coeff)
 FC=fq_default_ctx(modulus=fcmod,var='k',check_modulus=True)
 assert FC.modulus()==fcmod
 PC=fq_default_poly_ctx(FC);fc0,fc1=FC(0),FC(1);kg=FC([0,1])
 assert sum((FC(c)*kg**i for i,c in enumerate(coeff)),fc0)==0
 ev=lambda cc:FC(cc)
 fpol=PC([ev(c) for c in payload['D27']]);lead=ev(payload['D27'][-1])
 li=lead.inverse();assert lead*li==fc1
 whole=fpol*li;assert whole.degree()==5 and whole*lead==fpol
 originals=[]
 for rr in payload['original']:
  out={}
  for mm,nn,dd in rr:
   den=ev(dd);di=den.inverse();assert den*di==fc1
   out[tuple(mm)]=PC([ev(v) for v in nn])*di
  originals.append(out)
 def pdata(pp):return [[int(c) for c in v.to_list()] for v in pp.coeffs()]
 if fi==11:
  left,right=PC([FC(v) for v in OLD_LEFT]),PC([FC(v) for v in OLD_RIGHT])
  assert left*right==whole and left.degree()==1 and right.degree()==4
  initial,path,first_degree=left,'D27/a',5
  say(stage='new_D27_factor11_original_e_split_recovery',kFactorIndex=fi,
      wholeESplitProductActuallyVerified=True,onlyUnreturnedLeftLinearBranchActive=True,
      alreadySuccessfulRightQuarticNotRerun=True,newOriginalMacaulayDegree=5,claimExcluded=False)
 else:initial,path,first_degree=whole,'D27',4
 class Nonunit(Exception):
  def __init__(self,g,q):self.g=g;self.q=q
 outcomes=[];splits=[];inverses=0
 def process(H,path,first_degree):
  nonlocal inverses
  class A:
   def __init__(self,v=0):
    if isinstance(v,A):self.p=v.p;return
    pp=PC(v);q,r=divmod(pp,H);assert q*H+r==pp;self.p=r
   def __bool__(self):return bool(self.p)
   def __neg__(self):return A(-self.p)
   def __add__(self,v):return A(self.p+A(v).p)
   __radd__=__add__
   def __sub__(self,v):return A(self.p-A(v).p)
   def __rsub__(self,v):return A(v)-self
   def __mul__(self,v):return A(self.p.mul_mod(A(v).p,H))
   __rmul__=__mul__
   def __eq__(self,v):return self.p==A(v).p
   def inv(self):
    nonlocal inverses
    assert self
    g,s,t=self.p.xgcd(H);assert s*self.p+t*H==g
    if g.degree()>0:
     q,r=divmod(H,g);assert not r and q*g==H and 0<g.degree()<H.degree()
     raise Nonunit(g,q)
    inv=A(s*g[0].inverse());assert self*inv==1;inverses+=1;return inv
   def data(self):return pdata(self.p)
  def matrix_return(bound):
   mons=sorted([(i,j,h) for i in range(bound+1) for j in range(bound+1-i)
                for h in range(bound+1-i-j)],
               key=lambda z:(sum(z),z[1],z[0],z[2]),reverse=True)
   ncol=len(mons);assert ncol==(35 if bound==4 else 56)
   assert mons[-1]==(0,0,0);mi={m:i for i,m in enumerate(mons)}
   rows=[];labels=[]
   for ni,rr in enumerate(originals):
    formal_degree=2 if ni<4 else 3
    multipliers=sorted([m for m in mons if sum(m)<=bound-formal_degree],
                       key=lambda z:(sum(z),z[1],z[0],z[2]))
    for mm in multipliers:
     row=[A() for _ in mons]
     for mon,cf in rr.items():
      shifted=tuple(mon[j]+mm[j] for j in range(3))
      assert sum(shifted)<=bound
      row[mi[shifted]]=row[mi[shifted]]+A(cf)
     rows.append(row);labels.append([payload['names'][ni],mm])
   assert len(rows)==(48 if bound==4 else 100)
   basis=[];pivots=[];tags=[]
   say(stage='new_D27_isolated_original_matrix_begin',kFactorIndex=fi,ePath=path,
       eDegree=int(H.degree()),bound=bound,rows=len(rows),columns=ncol,
       newOriginalInput=(fi==11 or fi>=14),claimExcluded=False)
   for ri,rawrow in enumerate(rows):
    row=rawrow[:];tag={ri:A(1)}
    for br,pv,bt in zip(basis,pivots,tags):
     c=row[pv]
     if not c:continue
     row=[row[j]-c*br[j] for j in range(ncol)]
     for ii,v in bt.items():tag[ii]=tag.get(ii,A())-c*v
    if not any(row):continue
    pv=next(j for j,v in enumerate(row) if v);iv=row[pv].inv()
    row=[v*iv for v in row];tag={j:v*iv for j,v in tag.items() if v}
    assert row[pv]==1 and all(not row[j] for j in pivots)
    for j in range(ncol):
     assert sum((v*rows[ii][j] for ii,v in tag.items()),A())==row[j]
    basis.append(row);pivots.append(pv);tags.append(tag)
    if len(basis)==ncol:break
   target=[A(int(j==ncol-1)) for j in range(ncol)];rem=target[:];unit={}
   for br,pv,bt in zip(basis,pivots,tags):
    c=rem[pv]
    if not c:continue
    rem=[rem[j]-c*br[j] for j in range(ncol)]
    for ii,v in bt.items():unit[ii]=unit.get(ii,A())+c*v
   unit_ok=not any(rem)
   if unit_ok:
    for j in range(ncol):
     assert sum((v*rows[ii][j] for ii,v in unit.items()),A())==target[j]
   else:
    for j in range(ncol):
     assert sum((v*rows[ii][j] for ii,v in unit.items()),A())+rem[j]==target[j]
   cert=dict(prime=PRIME,kFactor=coeff,eModulus=pdata(H),bound=bound,
             labels=labels,pivots=pivots,
             allBasisOriginalRows=[{str(j):v.data() for j,v in tag.items()} for tag in tags],
             originalConstantOneCombination={str(j):v.data() for j,v in unit.items()},
             targetRemainder=[v.data() for v in rem])
   rec=dict(kFactorIndex=fi,kDegree=fr['degree'],ePath=path,eDegree=int(H.degree()),
            bound=bound,rows=len(rows),columns=ncol,rank=len(basis),
            everyBasisRowAllOriginalColumnsActuallyMultipliedBack=True,
            actualConstantOneTargetAttempted=True,
            originalConstantOneAllColumnsActuallyMultipliedBack=unit_ok,
            targetRemainderActuallyMultipliedBack=True,fullColumnRank=len(basis)==ncol,
            allActualInversesMultipliedBackToOne=True,certificate=digest(cert))
   say(stage='new_D27_isolated_original_Macaulay_return',**rec,claimExcluded=False)
   return rec
  try:
   r=matrix_return(first_degree)
   if not r['fullColumnRank'] and first_degree==4:r=matrix_return(5)
   outcomes.append(r)
  except Nonunit as ex:
   assert ex.g*ex.q==H and 0<ex.g.degree()<H.degree() and 0<ex.q.degree()<H.degree()
   rec=dict(kFactorIndex=fi,ePath=path,left=pdata(ex.g),right=pdata(ex.q),
            wholeProductActuallyVerified=True,bothOriginalBranchesRetained=True)
   splits.append(rec)
   say(stage='new_D27_isolated_actual_e_nonunit_split',**rec,claimExcluded=False)
   process(ex.g,path+'/a',first_degree);process(ex.q,path+'/b',first_degree)
 process(initial,path,first_degree)
 passed=bool(outcomes) and all(r['fullColumnRank'] and r['originalConstantOneAllColumnsActuallyMultipliedBack'] for r in outcomes)
 signal.alarm(0)
 say(stage='new_D27_isolated_k_factor_return_complete',kFactorIndex=fi,
     outcomes=outcomes,completeESplits=splits,actualInverseCount=inverses,
     allActiveOriginalEFibersReturnedWithFullColumnRank=passed,
     previousCompletedEFibersNotRerun=True,claimExcluded=False,
     peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
if len(sys.argv)>1 and sys.argv[1]=='--finite-child':
 finite_child(json.load(sys.stdin));sys.exit(0)
# Frozen dependency is used only for the small original Gram prefix, not for
# replaying its completed six-generator generic certificate or F806 projection.
dependency=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-D27-entire-quintic-original-finite-cover-8542.py')
raw=dependency.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='acf41d9be1da123da81b05210ec45b03064a2196bf941f58f3dd3b3408d53929'
marker=b'# New exact six-generator circuit'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
ns={'__file__':str(dependency),'__name__':'__necessary_original_Gram_prefix_only__'}
log=io.StringIO()
with contextlib.redirect_stdout(log):exec(compile(prefix,str(dependency),'exec'),ns)
signal.alarm(180)
def modq(c):
 q=Fraction(str(c));assert q.denominator%PRIME
 return q.numerator%PRIME*pow(q.denominator%PRIME,-1,PRIME)%PRIME
def arr(pp):return [modq(c) for c in pp.coeffs()]
payloadbase=dict(D27=[arr(f) for f in ns['F']],names=ns['names'],
 original=[[[list(mm),[arr(pp) for pp in cf.n],arr(cf.d)]
            for mm,cf in row.terms.items()] for row in ns['original']])
assert len(payloadbase['D27'])==6 and len(payloadbase['original'])==6
product=nmod_poly([1],PRIME)
for f in FACTORS:
 assert f['multiplicity']==1 and len(f['coefficients'])==f['degree']+1
 product*=nmod_poly(f['coefficients'],PRIME)
assert product.degree()==782 and product[782]==1
assert digest([int(c) for c in product.coeffs()])['sha256']==HIGH_MOD_SHA
assert len(FACTORS)==46 and sum(f['degree'] for f in FACTORS)==782
assert {r['i'] for r in PREVIOUS_COMPLETE}==set(range(14))
assert [r['path'] for r in PREVIOUS_COMPLETE if r['i']==11]==['D27/b']
todo=[11]+list(range(14,46));allreturns=[];failed=[];unstarted=[]
say(stage='new_D27_F782_exact_continuation_input',
    oldActualRun=OLD_ACTUAL_RUN,oldActualJob=OLD_ACTUAL_JOB,oldSourceSHA256=OLD_SOURCE_SHA,
    oldNativeSIGSEGVCauseUnknown=True,oldQQHighCoverDegree=782,oldQQHighSHA256=HIGH_QQ_SHA,
    priorCompleteGoodPrimeAndNormPartitionUsed=True,completeModularFactorizationProductReturned=True,
    originalGramPrefixOnlySHA256=hashlib.sha256(prefix).hexdigest(),
    originalInputModularPayload=digest(payloadbase),previousCompletedFibers=PREVIOUS_COMPLETE,
    activeKFactorIndices=todo,newDegreeFiveOriginalRowsForFactor11=True,
    allActualOriginalRationalDenominatorsPUnits=True,
    genericCoverAndCompletedOriginalUnitsNotReplayed=True,claimExcluded=False)
for position,fi in enumerate(todo):
 remaining=deadline-time.perf_counter()
 if remaining<2:
  unstarted=todo[position:];break
 payload=dict(payloadbase,index=fi,budget=max(1,int(remaining)-1))
 begin=time.perf_counter()
 try:
  proc=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--finite-child'],
     input=json.dumps(payload,separators=(',',':')),text=True,stdout=subprocess.PIPE,
     stderr=subprocess.PIPE,timeout=max(1,remaining))
  out,err,code=proc.stdout,proc.stderr,proc.returncode
 except subprocess.TimeoutExpired as ex:
  def dec(x):return x.decode('utf-8',errors='replace') if isinstance(x,bytes) else (x or '')
  out,err,code=dec(ex.stdout),dec(ex.stderr),None
  unstarted=todo[position+1:]
 for line in out.splitlines():print(line,flush=True)
 if err:
  print(err[:8192],file=sys.stderr,flush=True)
 records=[]
 for line in out.splitlines():
  try:
   rr=json.loads(line)
   if isinstance(rr,dict):records.append(rr)
  except (ValueError,TypeError):pass
 finals=[r for r in records if r.get('stage')=='new_D27_isolated_k_factor_return_complete']
 good=code==0 and len(finals)==1 and finals[0]['allActiveOriginalEFibersReturnedWithFullColumnRank']
 rec=dict(kFactorIndex=fi,returncode=code,elapsedSeconds=time.perf_counter()-begin,
          stdoutBytes=len(out.encode()),stdoutSHA256=hashlib.sha256(out.encode()).hexdigest(),
          stderrBytes=len(err.encode()),stderrSHA256=hashlib.sha256(err.encode()).hexdigest(),
          completedOriginalReturn=good,
          lastCompletedStage=(records[-1].get('stage') if records else None))
 if good:allreturns.append(finals[0])
 else:failed.append(rec)
 say(stage='new_D27_isolated_process_actual_receipt',**rec,
     crashCauseNotGuessed=True,previousFinishedFactorsNotReplayed=True,claimExcluded=False)
 if code is None:break
signal.alarm(0)
passed=not failed and not unstarted and len(allreturns)==len(todo)
say(stage='new_D27_F782_previously_unreturned_constant_algebra_continuation_complete',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),prime=PRIME,
    priorCompleteOriginalReturns=PREVIOUS_COMPLETE,newCompleteOriginalReturns=allreturns,
    actualFailedOrUnresolvedProcesses=failed,unstartedKFactorIndices=unstarted,
    allFortySixKFactorsAndAllFiveEBranchesCovered=passed,
    high782QQFibersExcludedByPriorGoodPrimeFiniteFreeNakayama=passed,
    degreeFourFullSpanExtendsToDegreeFiveByOriginalMonomialMultiplication=True,
    allReportedConstantOneCertificatesActuallyVerified=True,
    lowF24RequiresItsIndependentEntireQQReturn=True,wholeD27Excluded=False,claimExcluded=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
sys.exit(0 if passed else 2)

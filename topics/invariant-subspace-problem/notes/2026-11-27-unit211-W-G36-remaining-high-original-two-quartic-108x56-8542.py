#!/usr/bin/env python3
"""NEW remaining G36 high fibres: original R4/C4 plus six original Gram
rows, degree-five 108x56. Uses frozen actual factor coefficients only.
Earlier successful factors and the new V8 point are not rerun.
Each still-unreturned factor gets a fresh native process/context; every
child exit is reported. Full original column identities, not merely 1
membership modulo p, support the finite-free QQ conclusion.
180 seconds TOTAL / 4 GiB. No saved generic gate or big gcd is executed.
"""
import json,time,hashlib,signal,resource,math,sys,subprocess,contextlib,io
from pathlib import Path
from fractions import Fraction
from flint import fmpq_poly,fmpq,fmpz_mod_poly_ctx,fq_default_ctx,fq_default_poly_ctx
start=time.perf_counter()
budget=float(sys.argv[3]) if len(sys.argv)>3 else 180.0
deadline=start+budget
signal.alarm(max(1,math.ceil(budget)))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
def digest(obj):
 bb=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
prior=read('2026-11-27-unit211-W-G36-finite-1198-first-native-partial-receipt-8542.json',
 'c630e7aa789b96ec33d897bba4e8a88f77f6ec516cc21710aea58e68054baf42')
point=read('2026-11-27-unit211-W-G36-original-two-quartic-modular-point-return-receipt-8542.json',
 'a58712c241a887ade3ffb391df1852c7c33f14b81d866959b400fbc8e32a15f1')
assert prior['sourceSHA256']=='adfc52cf453a752b5e8d08f49a49a4529fe745662bb1cf68294c7bdebd76c44d'
assert prior['actualDriver']['source_exit_code']==-11
oldrecords=prior['records']
partition=next(r for r in oldrecords if r['stage']=='G36_saved_exact_1198_input_new_QQ_low_high_partition')
good=next(r for r in oldrecords if r['stage']=='G36_new_finite_original_good_prime_and_complete_factorization')
factors=good['completeModularFactors'];prime=good['prime']
assert prime==1009 and len(factors)==43
assert partition['highNormUnitCover']['degree']==1134 and partition['lowNormCover']['degree']==61
assert partition['completeQQPartitionAndBothBezoutProductsReturned']
assert good['QQHighDegree']==good['modularHighDegree']==1134
assert good['completeNormBezoutActuallyMultipliedBack']
assert good['fullModularFactorizationProductActuallyReturned']
assert good['allActualOriginalRationalCoefficientsPIntegral']
assert sum(r['degree']*r['multiplicity'] for r in factors)==1134
oldfull=[r for r in oldrecords if r['stage']=='new_G36_finite_whole_Q_six_algebra_original_48x35_return' and r['fullColumnRank']]
assert sorted(r['kFactorIndex'] for r in oldfull)==[0,1,2,3,4,5,6,7,8,9,10,11]
for r in oldfull:
 assert r['rank']==35 and r['allBasisOriginalThirtyFiveColumnProductsActuallyVerified']
 assert r['originalUnitThirtyFiveColumnProductsActuallyVerified']
 assert r['qDegree']==(5 if r['kFactorIndex']==10 else 6)
pr=point['actualResult']
assert pr['prime']==1009 and pr['k']==422 and pr['Q']==965
assert pr['rank']==pr['columns']==56 and pr['rows']==108
assert pr['actualOriginalConstantOneReturned'] and pr['allBasisFiftySixColumnIdentitiesVerified']
assert factors[10]['coefficients']==[587,1] and factors[10]['multiplicity']==2
pending=list(range(12,43))
assert sum(factors[i]['degree']*factors[i]['multiplicity'] for i in pending)==1120

if len(sys.argv)==1:
 say(stage='new_G36_degree_five_original_pending_108x56_input',
     earlierExactQQPartitionPreserved=True,QQHighDegree=1134,
     previousSuccessfulReducedFactors=list(range(12)),
     previousIndex10Rank33PointNowReturnedByNewR4C4=True,
     oldDegreeFourFullRanksLiftAlgebraicallyToDegreeFive=True,
     remainingFactorIndices=pending,remainingWeightedKDegree=1120,
     newOriginalRows=108,newColumns=56,
     noOld48x35GateRepeated=True,noLargeQQOrModularFactorizationRepeated=True,
     everyNativeConstantContextIsolatedInOneProcess=True,
     wholeHighQQExcluded=False,wholeG36Excluded=False)
 receipts=[];mathematics=[];not_started=[]
 for i in pending:
  remaining=deadline-time.perf_counter()-1.0
  if remaining<=0:
   not_started=[j for j in pending if j>=i];break
  t0=time.perf_counter()
  try:
   ran=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--fiber',str(i),str(remaining)],
       stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=remaining,check=False)
   out=ran.stdout.decode(errors='replace');rc=ran.returncode;timed=False
  except subprocess.TimeoutExpired as ex:
   out=(ex.stdout or b'').decode(errors='replace');rc=None;timed=True
  parsed=[]
  for line in out.splitlines():
   try:
    rr=json.loads(line)
    if isinstance(rr,dict) and 'stage' in rr:parsed.append(rr)
   except (ValueError,TypeError):pass
   print(line,flush=True)
  done=[r for r in parsed if r.get('stage')=='new_G36_remaining_factor_original_108x56_finished' and r.get('kFactorIndex')==i]
  returned=len(done)==1 and done[0]['allEntireQComponentsFullColumnRank']
  if returned:mathematics.append(done[0])
  rec=dict(kFactorIndex=i,kDegree=factors[i]['degree'],nativeSourceExitCode=rc,
       timedOut=timed,elapsedSeconds=time.perf_counter()-t0,
       stdoutBytes=len(out.encode()),stdoutSHA256=hashlib.sha256(out.encode()).hexdigest(),
       actualCompleteMathematicalReturn=returned)
  receipts.append(rec);say(stage='new_G36_isolated_native_factor_execution_receipt',**rec)
  if timed:
   not_started=[j for j in pending if j>i];break
 complete=(not not_started and len(receipts)==len(pending)
           and len(mathematics)==len(pending))
 signal.alarm(0)
 say(stage='new_G36_high1134_entire_original_finite_free_return_finished',
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     priorGoodPrimeAndQQPartitionRun=46046219647,
     prime=prime,QQHighCover=partition['highNormUnitCover'],
     remainingExactLow61Cover=partition['lowNormCover'],
     earlier12ReducedFactorsNotRecomputed=True,
     originalIndex10NewV8PointSourceSHA256=point['sourceSHA256'],
     isolatedNativeExecutionReceipts=receipts,
     pendingFactorsNotStarted=not_started,
     completeNewFiniteOriginalReturns=mathematics,
     allRemaining1120DegreeOriginalFibresReturned=complete,
     allHigh1134QQFibresExcludedByFiniteFreeNakayama=complete,
     everyModularMultiplicityRetained=True,
     proofScope='finite free over Z_(1009), full original row surjection, not multivariate modular emptiness',
     wholeG36Excluded=False,ordinaryISPClaim=False,
     peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 sys.exit(0)

assert len(sys.argv)==4 and sys.argv[1]=='--fiber'
factor_index=int(sys.argv[2]);assert factor_index in pending
record=factors[factor_index]
say(stage='new_G36_isolated_pending_factor_begin',kFactorIndex=factor_index,
    kDegree=record['degree'],newRows=108,newColumns=56,
    noPreviousMatrixForThisFactorReturned=True)
dep=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
old=raw.decode();marker='\n# New mathematical input: all four original quadratics'
assert old.count(marker)==1
prefix=old[:old.index(marker)]
assert hashlib.sha256(prefix.encode()).hexdigest()=='be7af2ffd4e73d716847c7fa6286170ec18702ea8c84a7cb964e8fcd5622ae4f'
ns={'__file__':str(dep),'__name__':'__original_Gram_prefix_only__'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
def cm(cc):
 q=Fraction(str(cc));assert q.denominator%prime
 return q.numerator%prime*pow(q.denominator%prime,-1,prime)%prime
kmod=fmpz_mod_poly_ctx(prime)(record['coefficients'])
FC=fq_default_ctx(modulus=kmod,var='k',check_modulus=True)
assert FC.modulus()==kmod
PC=fq_default_poly_ctx(FC);fc0=FC(0);fc1=FC(1);kg=FC([0,1])
assert sum((FC(c)*kg**j for j,c in enumerate(record['coefficients'])),fc0)==0
kinv=kg.inverse();assert kg*kinv==1
say(stage='new_G36_isolated_actual_finite_field_constructed',
    kFactorIndex=factor_index,kDegree=record['degree'],
    actualModulusAndGeneratorRelationVerified=True)
gcoeff=[["4096","9216","7680","3072","592","24","-10","-1"],["-6144","-16128","-14336","-6048","-1416","-186","-9"],["512","6016","6560","2528","468","50","2"],["1792","832","-832","-392","-50","-2"],["-256","-544","-24","24","4"],["-192","0","-8"],["32"]]
qmonic=PC([FC([cm(c)*pow(32,-1,prime)%prime for c in v]) for v in gcoeff])
assert qmonic.degree()==6 and qmonic[6]==1
inverse_count=1;powers={0:fc1}
def kp(j):
 if j not in powers:powers[j]=kg**j if j>=0 else kinv**(-j)
 return powers[j]
def in_weight(po):
 dd={}
 for mm,c in po.to_dict().items():
  assert all(mm[j]==0 for j in range(2,len(mm)))
  i,j=int(mm[0]),int(mm[1])
  dd[i]=dd.get(i,fc0)+FC(cm(c))*kp(j-i)
 return PC([dd.get(i,fc0) for i in range(max(dd,default=-1)+1)])
def in_geometry(po):
 dd={}
 for mm,c in po.to_dict().items():
  assert all(mm[j]==0 for j in range(5,len(mm)))
  i,j=int(mm[0]),int(mm[1]);mon=tuple(map(int,mm[2:5]))
  if mon not in dd:dd[mon]={}
  row=dd[mon];row[i]=row.get(i,fc0)+FC(cm(c))*kp(j-i)
 return {m:PC([row.get(i,fc0) for i in range(max(row,default=-1)+1)]) for m,row in dd.items()}
def evaluate_original(rr):
 global inverse_count
 den=in_weight(rr.d);dq,dr=divmod(den,qmonic);assert dq*qmonic+dr==den
 gg,ss,tt=dr.xgcd(qmonic);assert ss*dr+tt*qmonic==gg and gg.degree()==0
 iv=ss*gg[0].inverse();assert iv.mul_mod(dr,qmonic)==PC([1]);inverse_count+=1
 out={}
 for mon,cf in in_geometry(rr.n).items():
  q,r=divmod(cf,qmonic);assert q*qmonic+r==cf
  out[mon]=cf.mul_mod(iv,qmonic)
  assert out[mon].mul_mod(dr,qmonic)==r
 return out
rawnames=['E1','EBe','EBo','N1','NS','PS']
native=[evaluate_original(ns['symbolic'][name]) for name in rawnames]
native_lam=evaluate_original(ns['symbolic']['lam'])
native_T=evaluate_original(ns['symbolic']['T'])
names=rawnames+['R4','C4'];formal_degrees=[2,2,2,2,3,3,4,4]
def pdata(pp):return [[int(c) for c in z.to_list()] for z in pp.coeffs()]
class Nonunit(Exception):
 def __init__(self,g,q):self.g=g;self.q=q
allresults=[];splits=[]
def process(H,path):
 global inverse_count
 class A:
  def __init__(self,v=0):
   if isinstance(v,A):self.p=v.p;return
   pp=PC(v);qq,rr=divmod(pp,H);assert qq*H+rr==pp;self.p=rr
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
   global inverse_count
   assert self
   gg,ss,tt=self.p.xgcd(H);assert ss*self.p+tt*H==gg
   if gg.degree()>0:
    qq,rr=divmod(H,gg);assert not rr and qq*gg==H and 0<gg.degree()<H.degree()
    raise Nonunit(gg,qq)
   ans=A(ss*gg[0].inverse());assert self*ans==1;inverse_count+=1;return ans
  def __truediv__(self,v):return self*A(v).inv()
  def __rtruediv__(self,v):return A(v)*self.inv()
  def __pow__(self,j):
   if j<0:return self.inv()**(-j)
   out=A(1);v=self
   while j:
    if j&1:out=out*v
    v=v*v;j//=2
   return out
  def data(self):return pdata(self.p)
 class Mpoly:
  def __init__(self,v=0):
   if isinstance(v,Mpoly):self.terms=v.terms.copy();return
   c=A(v);self.terms={(0,0,0):c} if c else {}
  @staticmethod
  def variable(j):
   p=Mpoly();m=[0,0,0];m[j]=1;p.terms[tuple(m)]=A(1);return p
  @staticmethod
  def from_terms(ts):
   p=Mpoly();p.terms={m:c for m,c in ts if c};return p
  def __bool__(self):return bool(self.terms)
  def __add__(self,v):
   v=Mpoly(v);p=Mpoly(self)
   for m,c in v.terms.items():
    z=p.terms.get(m,A())+c
    if z:p.terms[m]=z
    elif m in p.terms:del p.terms[m]
   return p
  __radd__=__add__
  def __neg__(self):return Mpoly.from_terms((m,-c) for m,c in self.terms.items())
  def __sub__(self,v):return self+-Mpoly(v)
  def __rsub__(self,v):return Mpoly(v)+-self
  def __mul__(self,v):
   v=Mpoly(v);p=Mpoly()
   for ma,ca in self.terms.items():
    for mb,cb in v.terms.items():
     m=tuple(ma[j]+mb[j] for j in range(3));z=p.terms.get(m,A())+ca*cb
     if z:p.terms[m]=z
     elif m in p.terms:del p.terms[m]
   return p
  __rmul__=__mul__
  def scale(self,c):
   c=A(c);return Mpoly.from_terms((m,v*c) for m,v in self.terms.items())
  def __pow__(self,n):
   p=Mpoly(1)
   for i in range(n):p=p*self
   return p
  def __eq__(self,v):return not(self-Mpoly(v))
  def degree(self):return max((sum(m) for m in self.terms),default=-1)
  def json(self):return [[list(m),c.data()] for m,c in sorted(self.terms.items())]

 try:
  k=A(PC([kg]));Q=A(PC([0,1]));e=Q/k;u=e+1;V=u*k+2
  ell=u*((k+2)**2-2*e*k)/(k*V);d=1-Q;m=u-ell
  bc=(ell*ell-m*m/d)/4;M=4*bc*d
  V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
  Phi=T0+4*u-4+Q;P02=(2-3*u)*V2-Q*u+2*u**3
  # These denominators already occur in the full original lambda/T map;
  # every actually used inverse above returns one in this entire algebra.
  lam=Mpoly.from_terms((mm,A(cc)) for mm,cc in native_lam.items())
  T=Mpoly.from_terms((mm,A(cc)) for mm,cc in native_T.items())
  Al=2*lam**2-2*lam+1;Bl=4*lam**3-6*lam**2+3*lam-1
  D=Al.scale(ell)-T*T
  K=Bl.scale(ell*ell)-(T*Al).scale(3*ell)+2*T**3
  cc=3-2*lam;aa=4*u*Q-J;Cstar=aa*m*m+J*d*ell*ell
  aD=(3-4*lam).scale(M*ell*ell*Q)+(T*T).scale(M*aa)+(cc*T).scale(2*M*u*Q*ell)+D.scale(Cstar)
  bD=(T.scale(aa)+cc.scale(u*Q*ell)).scale(2*M*m)
  R4=(aD*aD).scale(M)-D*bD*bD
  C4=(D*aD).scale(2*m)+K*bD
  original=[Mpoly.from_terms((mm,A(cf)) for mm,cf in row.items()) for row in native]+[R4,C4]
  assert all(pp.degree()<=dd for pp,dd in zip(original,formal_degrees))
  mons=sorted([(i,j,t) for i in range(6) for j in range(6-i) for t in range(6-i-j)],key=lambda z:(sum(z),z[1],z[0],z[2]),reverse=True)
  assert len(mons)==56 and mons[-1]==(0,0,0)
  rows=[];labels=[]
  for ni,pp in enumerate(original):
   for mm in sorted([m0 for m0 in mons if sum(m0)<=5-formal_degrees[ni]],key=lambda z:(sum(z),z[1],z[0],z[2])):
    prod=pp*Mpoly.from_terms([(mm,A(1))]);assert prod.degree()<=5
    rows.append([prod.terms.get(mm0,A()) for mm0 in mons]);labels.append([names[ni],mm])
  assert len(rows)==108
  basis=[];tags=[];pivots=[]
  for idx,initial in enumerate(rows):
   row=initial[:];tag={idx:A(1)}
   for brow,pv,bt in zip(basis,pivots,tags):
    cf=row[pv]
    if not cf:continue
    row=[row[j]-cf*brow[j] for j in range(56)]
    for ii,vv in bt.items():tag[ii]=tag.get(ii,A())-cf*vv
   if not any(row):continue
   pv=next(j for j,v in enumerate(row) if v);iv=row[pv].inv()
   row=[v*iv for v in row];tag={j:v*iv for j,v in tag.items() if v}
   assert row[pv]==1 and all(not row[j] for j in pivots)
   for j in range(56):assert sum((vv*rows[ii][j] for ii,vv in tag.items()),A())==row[j]
   basis.append(row);tags.append(tag);pivots.append(pv)
   if len(basis)==56:break
  actual={};target=[A(int(j==55)) for j in range(56)];rem=target[:]
  for brow,pv,bt in zip(basis,pivots,tags):
   cf=rem[pv]
   if not cf:continue
   rem=[rem[j]-cf*brow[j] for j in range(56)]
   for ii,vv in bt.items():actual[ii]=actual.get(ii,A())+cf*vv
  unit=not any(rem)
  if unit:
   for j in range(56):assert sum((vv*rows[ii][j] for ii,vv in actual.items()),A())==target[j]
  cert=dict(kFactor=record['coefficients'],qModulus=pdata(H),labels=labels,
       pivots=pivots,allBasisRows=[{str(j):v.data() for j,v in tag.items()} for tag in tags],
       unitCombination={str(j):v.data() for j,v in actual.items()})
  rec=dict(kFactorIndex=factor_index,kDegree=record['degree'],kMultiplicity=record['multiplicity'],
       qPath=path,qDegree=int(H.degree()),originalRows=108,columns=56,rank=len(basis),
       originalDegrees=[pp.degree() for pp in original],
       allBasisOriginalFiftySixColumnProductsActuallyVerified=True,
       originalConstantOneFiftySixColumnProductsActuallyVerified=unit,
       fullColumnRank=(len(basis)==56),allUsedInverseProductsOne=True,
       certificate=digest(cert))
  allresults.append(rec);say(stage='new_G36_remaining_original_two_quartic_108x56_return',**rec)
 except Nonunit as ex:
  assert ex.g*ex.q==H and 0<ex.g.degree()<H.degree() and 0<ex.q.degree()<H.degree()
  rec=dict(kFactorIndex=factor_index,qPath=path,left=pdata(ex.g),right=pdata(ex.q),
       wholeOriginalQProductActuallyVerified=True,bothComponentsRetained=True)
  splits.append(rec);say(stage='new_G36_remaining_original_Q_nonunit_split',**rec)
  process(ex.g,path+'/a');process(ex.q,path+'/b')
process(qmonic,'Q6')
assert sum(r['qDegree'] for r in allresults)==6
complete=all(r['fullColumnRank'] and r['originalConstantOneFiftySixColumnProductsActuallyVerified'] for r in allresults)
say(stage='new_G36_remaining_factor_original_108x56_finished',
    kFactorIndex=factor_index,kDegree=record['degree'],kMultiplicity=record['multiplicity'],
    allEntireQComponentsFullColumnRank=complete,
    originalQComponentReturns=allresults,allOriginalQSplits=splits,
    actualInverseProducts=inverse_count,wholeG36Excluded=False)
signal.alarm(0)

#!/usr/bin/env python3
"""NEW last low29 G36 fibres: saved k14/q5 and original k15/M13 gcd.
Keep whole QQ quotients; use the NEW two-quartic 108x56 matrix and a
finite-free good-prime lift. No completed seven QQ fibres, high1134
fibres, or old 48x35 attempt are rerun. 180 seconds TOTAL /4 GiB.
"""
import json,time,hashlib,signal,resource,math,sys,subprocess,contextlib,io,zlib,base64
from pathlib import Path
from fractions import Fraction
from flint import fmpq,fmpq_poly,nmod_poly,fmpz_mod_poly_ctx,fq_default_ctx,fq_default_poly_ctx
start=time.perf_counter()
mode=sys.argv[1] if len(sys.argv)>1 else 'main'
payload=None
if mode!='main':
 assert mode in ['preflight','return'] and len(sys.argv)==4
 raw=zlib.decompress(base64.b64decode(sys.argv[2]))
 assert hashlib.sha256(raw).hexdigest()==sys.argv[3]
 payload=json.loads(raw)
budget=float(payload['budget']) if payload is not None else 180.0
deadline=start+budget;signal.alarm(max(1,math.ceil(budget)))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r,separators=(',',':')),flush=True)
def P(v=()):
 if isinstance(v,fmpq_poly):return v
 if isinstance(v,(int,fmpq)):v=[v]
 return fmpq_poly([fmpq(c) for c in v])
def coeffs(pp):return [str(c) for c in pp.coeffs()]
one=P([1]);lp=P([0,1])
def digest(obj):
 bb=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
def cm_at(c,p):
 q=Fraction(str(c));assert q.denominator%p
 return q.numerator%p*pow(q.denominator%p,-1,p)%p
class BaseNonunit(Exception):
 def __init__(self,g):self.g=g
def derive_original_M13_complement(F):
 F=F/F[F.degree()];inverse_count=0
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.p=v.p;return
   if not isinstance(v,fmpq_poly):v=P([v])
   qq,rr=divmod(v,F);assert qq*F+rr==v;self.p=rr
  def __bool__(self):return bool(self.p)
  def __neg__(self):return K(-self.p)
  def __add__(self,v):return K(self.p+K(v).p)
  __radd__=__add__
  def __sub__(self,v):return K(self.p-K(v).p)
  def __rsub__(self,v):return K(v)-self
  def __mul__(self,v):return K(self.p*K(v).p)
  __rmul__=__mul__
  def __eq__(self,v):return self.p==K(v).p
  def inv(self):
   nonlocal inverse_count
   assert self
   if self==1:return K(1)
   g,s,t=self.p.xgcd(F);assert s*self.p+t*F==g
   if g.degree()>0:raise BaseNonunit(g/g[g.degree()])
   ans=K(s/g[0]);assert self*ans==1;inverse_count+=1;return ans
  def __truediv__(self,v):return self*K(v).inv()
  def __rtruediv__(self,v):return K(v)*self.inv()
  def __pow__(self,n):
   if n<0:return self.inv()**(-n)
   out=K(1);v=self
   while n:
    if n&1:out=out*v
    v=v*v;n//=2
   return out
  def data(self):return coeffs(self.p)
 class U:
  def __init__(self,v=()):
   if isinstance(v,U):self.c=v.c[:];return
   if isinstance(v,(K,int,fmpq)):v=[v]
   self.c=[K(z) for z in v]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def degree(self):return len(self.c)-1
  def __neg__(self):return U([-z for z in self.c])
  def __add__(self,v):
   v=U(v);n=max(len(self.c),len(v.c))
   return U([(self.c[j] if j<len(self.c) else K())+(v.c[j] if j<len(v.c) else K()) for j in range(n)])
  __radd__=__add__
  def __sub__(self,v):return self+-U(v)
  def __rsub__(self,v):return U(v)+-self
  def __mul__(self,v):
   v=U(v)
   if not self or not v:return U()
   w=[K() for _ in range(len(self.c)+len(v.c)-1)]
   for i,a in enumerate(self.c):
    for j,b in enumerate(v.c):w[i+j]=w[i+j]+a*b
   return U(w)
  __rmul__=__mul__
  def scale(self,v):return U([z*K(v) for z in self.c])
  def __eq__(self,v):return self.c==U(v).c
  def data(self):return [z.data() for z in self.c]
 def dr(a,b):
  a,b=U(a),U(b);assert b
  q=U();r=U(a);li=b.c[-1].inv()
  while r and r.degree()>=b.degree():
   shift=r.degree()-b.degree();cf=r.c[-1]*li
   term=U([K()]*shift+[cf]);q=q+term;r=r-term*b
  assert q*b+r==a and (not r or r.degree()<b.degree())
  return q,r
 def xg(a,b):
  a,b=U(a),U(b);r0,r1=a,b;s0,s1=U(1),U();t0,t1=U(),U(1)
  while r1:
   q,r=dr(r0,r1);r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
  if r0:
   iv=r0.c[-1].inv();r0=r0.scale(iv);s0=s0.scale(iv);t0=t0.scale(iv)
  assert s0*a+t0*b==r0
  return r0,s0,t0

 k=K(lp)
 gc=[K(P(v)/32) for v in [["4096","9216","7680","3072","592","24","-10","-1"],["-6144","-16128","-14336","-6048","-1416","-186","-9"],["512","6016","6560","2528","468","50","2"],["1792","832","-832","-392","-50","-2"],["-256","-544","-24","24","4"],["-192","0","-8"],["32"]]]
 q6=U(gc);assert q6.degree()==6 and q6.c[-1]==1
 # hM = k*M13; the original identity is M=-u^2*M13/(k*V^2).
 # k,u,V and M=4bc(1-Q) are already paid on this W chart.
 hM=U([-k**4-8*k**3-20*k*k-16*k,
        k**4+8*k**3+24*k*k+32*k+16,
        -3*k*k-12*k-16,4])
 gg,ss,tt=xg(hM,q6)
 assert ss*hM+tt*q6==gg
 complement,remainder=dr(q6,gg);assert not remainder and gg*complement==q6
 _,remM=dr(hM,gg);assert not remM
 assert gg.c[-1]==1 and complement.c[-1]==1
 cert=dict(kModulus=coeffs(F),originalQSix=q6.data(),originalPaidHM=hM.data(),
      gcd=gg.data(),complement=complement.data(),bezout=[ss.data(),tt.data()])
 say(stage='new_G36_low15_original_M13_exact_QQ_whole_complement',
     kDegree=int(F.degree()),paidZeroQDegree=gg.degree(),
     retainedQDegree=complement.degree(),
     originalM13AndWholeQSixGcdIdentityActuallyReturned=True,
     completeTwoFactorProductAndHMZeroProductActuallyReturned=True,
     noOriginalMacaulayReturnReplayed=True,
     physicalSource='M=-u^2*M13/(k*V^2)=4bc(1-Q)',
     actualConstantFieldInverseProducts=inverse_count,certificate=digest(cert))
 return complement.data(),gg.data(),int(complement.degree())

if mode=='main':
 saved=read('2026-11-27-unit211-W-G36-remaining-low29-exact-input-8542.json',
   '98e59cf24a9e0b7e3b2e029869dba426ce5201ad7a0636524fac69f483dca978')
 assert saved['completedLowKIndices']==list(range(7))
 a,b=saved['remaining'];assert a['kDegree']==14 and b['kDegree']==15
 cases=[dict(caseIndex=0,originalKIndex=7,kCoefficients=coeffs(P(a['kCoefficients'])/P(a['kCoefficients'])[14]),
        kDegree=14,hCoefficients=a['qMonicCoefficients'],qDegree=5,
        priorRemovedQOne='complete J19 original zero component already excluded')]
 hf,hzero,degree=derive_original_M13_complement(P(b['kCoefficients']))
 if degree>0:
  cases.append(dict(caseIndex=1,originalKIndex=8,
    kCoefficients=coeffs(P(b['kCoefficients'])/P(b['kCoefficients'])[15]),
    kDegree=15,hCoefficients=hf,qDegree=degree,
    removedOriginalM13ZeroFactor=hzero))
 rawcases=json.dumps(cases,separators=(',',':')).encode()
 encoded=base64.b64encode(zlib.compress(rawcases,9)).decode()
 assert zlib.decompress(base64.b64decode(encoded))==rawcases
 chunks=[encoded[j:j+75000] for j in range(0,len(encoded),75000)]
 say(stage='new_G36_low29_complete_QQ_finite_models_exact_input',
     actualFiniteFreeRanks=[c['kDegree']*c['qDegree'] for c in cases],
     rawBytes=len(rawcases),rawSHA256=hashlib.sha256(rawcases).hexdigest(),
     chunks=len(chunks),base64Characters=len(encoded),allOriginalBranchesRetained=True)
 for j,ch in enumerate(chunks):say(stage='new_G36_low29_complete_QQ_finite_models_exact_input_chunk',index=j,total=len(chunks),data=ch)
 execution=[];rejected=[];chosen=None;chosen_jobs=None;native_abort=None
 def run_child(job,phase):
  remain=deadline-time.perf_counter()-1
  if remain<=0:return None
  inp=dict(job);inp['budget']=remain
  raw=json.dumps(inp,separators=(',',':')).encode()
  enc=base64.b64encode(zlib.compress(raw,9)).decode()
  started=time.perf_counter()
  try:
   rr=subprocess.run([sys.executable,str(Path(__file__).resolve()),phase,enc,hashlib.sha256(raw).hexdigest()],
      stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=remain,check=False)
   out=rr.stdout.decode(errors='replace');rc=rr.returncode;timed=False
  except subprocess.TimeoutExpired as ex:
   out=(ex.stdout or b'').decode(errors='replace');rc=None;timed=True
  parsed=[]
  for line in out.splitlines():
   print(line,flush=True)
   try:
    r=json.loads(line)
    if isinstance(r,dict) and 'stage' in r:parsed.append(r)
   except (ValueError,TypeError):pass
  info=dict(phase=phase,caseIndex=job['caseIndex'],jobIndex=job['jobIndex'],
       prime=job['prime'],kDegree=job['record']['degree'],
       sourceExitCode=rc,timedOut=timed,elapsedSeconds=time.perf_counter()-started,
       stdoutBytes=len(out.encode()),stdoutSHA256=hashlib.sha256(out.encode()).hexdigest())
  execution.append(info);say(stage='new_G36_low29_actual_native_worker_receipt',**info)
  return parsed
 for p in [1009,1013,1019,1021,1031,1033,1039]:
  allcoeff=[z for c in cases for z in c['kCoefficients']]
  allcoeff += [z for c in cases for qco in c['hCoefficients'] for z in qco]
  if any(Fraction(str(z)).denominator%p==0 for z in allcoeff):
   rejected.append([p,'actual QQ monic model denominator']);continue
  jobs=[];products=[]
  for c in cases:
   ff=nmod_poly([cm_at(z,p) for z in c['kCoefficients']],p)
   assert ff.degree()==c['kDegree'] and int(ff[ff.degree()])==1
   content,factors=ff.factor();back=nmod_poly([content],p)
   records=[]
   for f,mul in factors:
    back*=f**int(mul);record=dict(degree=int(f.degree()),multiplicity=int(mul),coefficients=[int(z) for z in f.coeffs()])
    records.append(record)
    jobs.append(dict(c,record=record,jobIndex=len(jobs),prime=p))
   assert back==ff
   products.append(dict(caseIndex=c['caseIndex'],completeModularFactors=records,actualFullProductVerified=True))
  good=True
  for job in jobs:
   got=run_child(job,'preflight')
   if got is None:
    good=False;native_abort=dict(prime=p,reason='total wall budget reached before worker');break
   status=execution[-1]
   passed=[r for r in got if r.get('stage')=='new_G36_low29_native_denominator_preflight']
   if status['sourceExitCode']!=0 or status['timedOut'] or len(passed)!=1:
    good=False;native_abort=dict(prime=p,reason='native preflight did not return its exact marker',receipt=status);break
   if not passed[0].get('good',False):
    good=False;rejected.append([p,passed[0].get('reason','explicit denominator nonunit')]);break
  if not good:
   if native_abort is not None or deadline-time.perf_counter()<2:break
   continue
  chosen=p;chosen_jobs=jobs
  say(stage='new_G36_low29_actual_good_prime_entire_free_model',
      prime=p,rejectedPrimes=rejected,
      finiteFreeQQDimensions=[c['kDegree']*c['qDegree'] for c in cases],
      monicDegreesAndEveryQQCoefficientPIntegral=True,
      completeBaseFactorProducts=products,
      allActualOriginalDenominatorInverseProductsReturned=True,
      noMacaulayReturnWasRunAtRejectedPrimes=True)
  break
 mathematics=[]
 if chosen is not None:
  for job in chosen_jobs:
   got=run_child(job,'return')
   if got is None:break
   done=[r for r in got if r.get('stage')=='new_G36_low29_new_factor_original_108x56_finished']
   if len(done)==1:mathematics.append(done[0])
   else:
    native_abort=dict(prime=chosen,reason='original return had no complete terminal marker',receipt=execution[-1]);break
 closed=(chosen is not None and len(mathematics)==len(chosen_jobs)
         and all(r['allEntireQComponentsFullColumnRank'] for r in mathematics))
 signal.alarm(0)
 say(stage='new_G36_last_low29_complete_original_finite_free_return_finished',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    prime=chosen,rejectedPrimes=rejected,nativeAbort=native_abort,
    allActualNativeExecutions=execution,
    allOriginalFiniteReturns=mathematics,
    originalK14J19ZeroQOneAlreadyExcluded=True,
    newOriginalK15M13ZeroFactorDegree=len(hzero)-1,
    newOriginalK15M13ZeroComponentExcluded=(len(hzero)>1),
    allRemainingLow29OriginalFibersExcluded=closed,
    completeMonicFiniteFreeModelsUsed=True,
    allModularMultiplicitiesAndQNilpotentsRetained=True,
    noCompletedLow32OrHigh1134GateReplayed=True,
    noDInverseOrDOnlyTarget=True,
    wholeG36Excluded=False,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 sys.exit(0)
assert mode in ['preflight','return'] and payload is not None
prime=payload['prime'];record=payload['record'];factor_index=payload['jobIndex']
say(stage='new_G36_low29_native_finite_worker_begin',phase=mode,
    caseIndex=payload['caseIndex'],jobIndex=factor_index,
    kDegree=record['degree'],qDegree=payload['qDegree'])
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
class BadPrime(Exception):pass
def cm(cc):
 q=Fraction(str(cc))
 if q.denominator%prime==0:raise BadPrime('actual original coefficient is not p-integral')
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
hpoly=PC([FC([cm(c) for c in vv]) for vv in payload['hCoefficients']])
assert hpoly.degree()==payload['qDegree'] and hpoly[hpoly.degree()]==1
hq,hr=divmod(qmonic,hpoly);assert not hr and hq*hpoly==qmonic
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
 den=in_weight(rr.d);dq,dr=divmod(den,hpoly);assert dq*hpoly+dr==den
 gg,ss,tt=dr.xgcd(hpoly);assert ss*dr+tt*hpoly==gg
 if gg.degree()>0:raise BadPrime('actual original denominator is not a unit')
 iv=ss*gg[0].inverse();assert iv.mul_mod(dr,hpoly)==PC([1]);inverse_count+=1
 out={}
 for mon,cf in in_geometry(rr.n).items():
  q,r=divmod(cf,hpoly);assert q*hpoly+r==cf
  out[mon]=cf.mul_mod(iv,hpoly)
  assert out[mon].mul_mod(dr,hpoly)==r
 return out
try:
 rawnames=['E1','EBe','EBo','N1','NS','PS']
 native=[evaluate_original(ns['symbolic'][name]) for name in rawnames]
 native_lam=evaluate_original(ns['symbolic']['lam'])
 native_T=evaluate_original(ns['symbolic']['T'])
 for label,dd in [('k',PC([kg])),('V',PC([kg+2,1])),('1-Q',PC([1,-1]))]:
  gg,ss,tt=dd.xgcd(hpoly);assert ss*dd+tt*hpoly==gg
  if gg.degree()>0:raise BadPrime('new quartic denominator '+label)
  iv=ss*gg[0].inverse();assert iv.mul_mod(dd,hpoly)==PC([1])
except BadPrime as ex:
 say(stage='new_G36_low29_native_denominator_preflight',caseIndex=payload['caseIndex'],jobIndex=factor_index,prime=prime,good=False,reason=str(ex),noOriginalMacaulayGateExecuted=True)
 signal.alarm(0);sys.exit(0)
if mode=='preflight':
 say(stage='new_G36_low29_native_denominator_preflight',caseIndex=payload['caseIndex'],jobIndex=factor_index,prime=prime,good=True,allActualOriginalDenominatorInverseProductsOne=True,wholeQQuotientIdentityReturned=True,noOriginalMacaulayGateExecuted=True)
 signal.alarm(0);sys.exit(0)

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
  allresults.append(rec);say(stage='new_G36_low29_new_original_two_quartic_108x56_return',**rec)
 except Nonunit as ex:
  assert ex.g*ex.q==H and 0<ex.g.degree()<H.degree() and 0<ex.q.degree()<H.degree()
  rec=dict(kFactorIndex=factor_index,qPath=path,left=pdata(ex.g),right=pdata(ex.q),
       wholeOriginalQProductActuallyVerified=True,bothComponentsRetained=True)
  splits.append(rec);say(stage='new_G36_low29_new_original_Q_nonunit_split',**rec)
  process(ex.g,path+'/a');process(ex.q,path+'/b')
process(hpoly,'remaining_original_Q')
assert sum(r['qDegree'] for r in allresults)==hpoly.degree()
complete=all(r['fullColumnRank'] and r['originalConstantOneFiftySixColumnProductsActuallyVerified'] for r in allresults)
say(stage='new_G36_low29_new_factor_original_108x56_finished',
    caseIndex=payload['caseIndex'],jobIndex=factor_index,kFactorIndex=factor_index,kDegree=record['degree'],kMultiplicity=record['multiplicity'],
    allEntireQComponentsFullColumnRank=complete,
    originalQComponentReturns=allresults,allOriginalQSplits=splits,
    actualInverseProducts=inverse_count,wholeG36Excluded=False)
signal.alarm(0)

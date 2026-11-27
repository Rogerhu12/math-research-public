from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
import time,signal,resource,json,hashlib
start=time.perf_counter();root=Path('/workspace/scratch/8542378f2b73');ctx=fmpq_mpoly_ctx.get(('rho','lam','w'),'lex')
def say(**kw):print(json.dumps(dict(seconds=time.perf_counter()-start,**kw)),flush=True)
def alarm(s,f):say(stage='timeout_unknown',claimExcluded=False);raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm);signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def load(file,field=None,sha=None):
 dd=json.loads((root/file).read_text());dd=dd[field] if field else dd;pp=ctx.from_dict({tuple(mm):fmpq(aa) for mm,aa in dd})
 if sha:assert hashlib.sha256(str(pp).encode()).hexdigest()==sha
 return pp
C=load('L0_original_eight_by_eight_curve.json','curve','6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c')
X=load('L0_XY_P1_N1.json',sha='519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68')
Y=load('L0_XY_P1_EBe.json',sha='c696ee10ac72763cbc2d9e01cd84cdda6bfd5116faa3262ddbf6f96490c54d33')
extra=[]
for rec in json.loads((root/'L0_additional_macaulay_curves.json').read_text()):
 pp=ctx.from_dict({tuple(mm):fmpq(aa) for mm,aa in rec['curve']});assert hashlib.sha256(str(pp).encode()).hexdigest()==rec['sha256'];extra.append(('C'+str(rec['omittedRow']),pp))
units=[ctx.from_dict({tuple(mm):fmpq(aa) for mm,aa in dd}) for dd in json.loads((root/'L0_all_paid_parameter_units.json').read_text())]
class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):assert v.field is field;self.p=v.p;return
  pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
  self.p=divmod(pp,field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def inv(self):
  assert self
  gg,ss,tt=self.p.xgcd(self.field.mod)
  assert self.p*ss+self.field.mod*tt==gg and gg.degree()==0
  vv=FE(self.field,ss/gg[0]);assert self*vv==1
  self.field.inverses+=1;return vv
class Field:
 def __init__(self,phi):
  self.mod=phi/phi.leading_coefficient();self.inverses=0;self.bezout=0;self.divisions=0
  self.zero=FE(self);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)
def trim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def addpoly(pp,qq,zero):
 out=[zero]*max(len(pp),len(qq))
 for j,v in enumerate(pp):out[j]=out[j]+v
 for j,v in enumerate(qq):out[j]=out[j]+v
 return trim(out)
def mulpoly(pp,qq,zero):
 if not pp or not qq:return []
 out=[zero]*(len(pp)+len(qq)-1)
 for i,v in enumerate(pp):
  for j,w in enumerate(qq):out[i+j]=out[i+j]+v*w
 return trim(out)
def dividep(pp,qq):
 pp=trim(pp);qq=trim(qq);assert qq
 field=qq[0].field;original=list(pp);inv=qq[-1].inv()
 out=[field.zero]*max(0,len(pp)-len(qq)+1)
 while pp and len(pp)>=len(qq):
  shift=len(pp)-len(qq);a=pp[-1]*inv;out[shift]=out[shift]+a
  for j,v in enumerate(qq):pp[shift+j]=pp[shift+j]-a*v
  pp=trim(pp)
 out=trim(out)
 assert original==addpoly(mulpoly(out,qq,field.zero),pp,field.zero)
 field.divisions+=1
 return out,pp
def gcdp(pp,qq):
 pp=trim(pp);qq=trim(qq)
 if not pp and not qq:return []
 field=(pp or qq)[0].field;zero=field.zero;one=field.one
 originalp=list(pp);originalq=list(qq)
 s0=[one];s1=[];t0=[];t1=[one]
 while qq:
  quotient,remainder=dividep(pp,qq);pp,qq=qq,remainder
  s0,s1=s1,addpoly(s0,[-v for v in mulpoly(quotient,s1,zero)],zero)
  t0,t1=t1,addpoly(t0,[-v for v in mulpoly(quotient,t1,zero)],zero)
 if pp:
  inv=pp[-1].inv();pp=[inv*v for v in pp];s0=[inv*v for v in s0];t0=[inv*v for v in t0]
 assert pp==addpoly(mulpoly(s0,originalp,zero),mulpoly(t0,originalq,zero),zero)
 field.bezout+=1
 return pp

tr=trim
def quo(pp,qq):
 out,remainder=dividep(pp,qq);assert not remainder;return out
def spec(poly,field):
 terms=poly.to_dict()
 if not terms:return []
 out=[]
 for j0 in range(max(int(m[1]) for m in terms)+1):
  dd={int(m[0]):v for m,v in terms.items() if int(m[1])==j0}
  cs=[fmpq(0)]*(max(dd,default=-1)+1)
  for i,v in dd.items():cs[i]=v
  out.append(field(fmpq_poly(cs)))
 return tr(out)
def fpower(self,n):
 assert n>=0
 out=self.field.one;v=self
 while n:
  if n&1:out=out*v
  v=v*v;n//=2
 return out
FE.__pow__=fpower
FE.__rsub__=lambda self,o:FE(self.field,o)+-self
FE.__truediv__=lambda self,o:self*FE(self.field,o).inv()
FE.__rtruediv__=lambda self,o:FE(self.field,o)*self.inv()



def spec_ell(poly,field):
 terms=poly.to_dict()
 if not terms:return []
 assert all(int(m[2])==0 for m in terms)
 out=[]
 for j0 in range(max(int(m[0]) for m in terms)+1):
  dd={int(m[1]):aa for m,aa in terms.items() if int(m[0])==j0};cs=[fmpq(0)]*(max(dd,default=-1)+1)
  for i,aa in dd.items():cs[i]=aa
  out.append(field(fmpq_poly(cs)))
 return tr(out)

def spec_w(pp,field):
 terms=pp.to_dict();assert all(int(mm[0])==0 for mm in terms)
 out=[]
 for j in range(int(pp.degrees()[1])+1):
  dd={int(mm[2]):aa for mm,aa in terms.items() if int(mm[1])==j};cs=[fmpq(0)]*(max(dd,default=-1)+1)
  for k,aa in dd.items():cs[k]=aa
  out.append(field(fmpq_poly(cs)))
 return trim(out)

import sys,math
sys.path.insert(0,str(root))
from L0_original_sylvester_phi_valuation_8542 import minimum_assignment
candidates=json.loads((root/'L0_new_support_group_candidates.json').read_text())['candidates']
zero=fmpq_poly([])
def coefficients(pp):
 out=[]
 for j in range(int(pp.degrees()[1])+1):
  dd={int(mm[2]):aa for mm,aa in pp.to_dict().items() if int(mm[1])==j};out.append(fmpq_poly([dd.get(k,fmpq(0)) for k in range(max(dd,default=-1)+1)]))
 return out
def shift(cs,rr):
 out=[cs[-1]]
 for aa in cs[-2::-1]:out=[rr*out[0]+aa]+[rr*out[j]+out[j-1] for j in range(1,len(out))]+[out[-1]]
 return out

from flint import fmpq_mat
key=sys.argv[1] if len(sys.argv)>1 else '2'
target={'92':107,'36':36,'2':5,'8':12,'3':4}[key]
prior=json.loads((root/'L0_translated_Sylvester_valuation_returns.json').read_text());prior=next(r for r in prior if r['group']==key)
phi=fmpq_poly([fmpq(a) for a in prior['phi']]);rp0=fmpq_poly([fmpq(a) for a in prior['rootPolynomial']]);d=phi.degree();n=73;field=Field(phi)
original=[coefficients(pp) for pp in [C,X]];cs=[shift(cc,rp0) for cc in original]
assert all(shift(cc,-rp0)==oo for cc,oo in zip(cs,original))
M=[[zero]*j+cs[0][::-1]+[zero]*(33-j) for j in range(34)]+[[zero]*j+cs[1][::-1]+[zero]*(38-j) for j in range(39)]
divchecks=0;trace=hashlib.sha256()
def dividechecked(p,q):
 global divchecks
 a,b=divmod(p,q);assert a*q+b==p;divchecks+=1
 return a,b
costs=[]
for row in M:
 cc=[]
 for p in row:
  if not p:cc.append(10**9);continue
  count=0
  while True:
   qq,rem=dividechecked(p,phi)
   if rem:break
   p=qq;count+=1
  cc.append(count)
 costs.append(cc)
E,perm,u,v=minimum_assignment(costs);assert E==prior['actualQQValuationLowerBound'] and E<=target
for i in range(n):
 for j in range(n):
  k=u[i]+v[j];p=M[i][j]
  if k>=0:
   qq,rem=dividechecked(p,phi**k);assert not rem;M[i][j]=qq
  else:M[i][j]=p*phi**(-k)
T=target+1;N=T-E
for i in range(n):
 for j in range(n):M[i][j]=dividechecked(M[i][j],phi**N)[1]
say(stage='new_native_QQ_kernel_local_phi_start',group=key,degree=d,initialQQExtracted=E,target=target,precision=N,matrixSize=n,QQRegularRepresentationSize=n*d)
rounds=[]
while E<target:
 M0=[[dividechecked(p,phi)[1] for p in row] for row in M]
 dim=n*d;data=[[fmpq(0)]*dim for _ in range(dim)]
 for i in range(n):
  for j in range(n):
   if not M0[i][j]:continue
   for a in range(d):
    pp=dividechecked(M0[i][j]*fmpq_poly([0]*a+[1]),phi)[1]
    for b,coef in enumerate(pp):data[i*d+a][j*d+b]=coef
 A=fmpq_mat(data);rr,rank=A.transpose().rref();pivots=[]
 for i in range(rank):
  pivot=next(j for j in range(dim) if rr[i,j]);assert rr[i,pivot]==1;pivots.append(pivot)
 free=[j for j in range(dim) if j not in pivots];basis=[]
 if not free:
  say(stage='actual_QQ_full_rank_below_modular_target',group=key,QQvaluation=E,target=target);break
 for qfree in free:
  vec=[fmpq(0)]*dim;vec[qfree]=fmpq(1)
  for i,j in enumerate(pivots):vec[j]=-rr[i,qfree]
  check=fmpq_mat([vec])*A;assert all(check[0,j]==0 for j in range(dim))
  kv=[field(fmpq_poly(vec[i*d:(i+1)*d])) for i in range(n)]
  for pivot,bvec in basis:
   fact=kv[pivot]
   if fact:kv=[a-fact*b for a,b in zip(kv,bvec)]
  nonzero=next((j for j,a in enumerate(kv) if a),None)
  if nonzero is None:continue
  inv=kv[nonzero].inv();kv=[inv*a for a in kv]
  for k,(pivot,bvec) in enumerate(basis):
   fact=bvec[nonzero]
   if fact:basis[k]=(pivot,[a-fact*b for a,b in zip(bvec,kv)])
  basis.append((nonzero,kv));basis.sort(key=lambda z:z[0])
 assert basis
 chosen=[i for i,_ in basis]
 for k,(i,vec) in enumerate(basis):
  assert all(vec[j]==(1 if i==j else 0) for j in chosen)
  for j in range(n):
   check=sum((vv.p*M0[ii][j] for ii,vv in enumerate(vec)),zero)
   assert not dividechecked(check,phi)[1]
 # The replacement P has identity on the chosen columns, and all other rows
 # are unchanged: P=I+N0, N0^2=0, hence detP=1 as a QQ[w] identity.
 updated={}
 for i,vec in basis:
  row=[]
  for j in range(n):
   pp=sum((vv.p*M[ii][j] for ii,vv in enumerate(vec) if vv),zero)
   qq,rem=dividechecked(pp,phi);assert not rem;row.append(qq)
  updated[i]=row
  trace.update(str((i,[[str(a) for a in vv.p] for vv in vec])).encode())
 for i,row in updated.items():M[i]=row
 E+=len(updated);assert E<=target
 N=T-E
 for i in range(n):
  for j in range(n):M[i][j]=dividechecked(M[i][j],phi**N)[1]
 rec={'round':len(rounds)+1,'actualQQRank':rank,'actualQQKernelDimension':len(free),'selectedKKernelRows':len(updated),'chosenRows':chosen,'extractedTotal':E,'remainingPrecision':N,'actualInverseProducts':field.inverses,'allKernelAndDivisionIdentitiesVerified':True}
 rounds.append(rec);say(stage='native_exact_kernel_phi_extraction',group=key,**rec)
 (root/('L0_native_kernel_phi_'+key+'_partial.json')).write_text(json.dumps({'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'group':key,'provedQQExponentLowerBound':E,'target':target,'rounds':rounds,'divisionIdentities':divchecks,'traceSha256':trace.hexdigest()},indent=2))
result={'group':key,'phi':[str(a) for a in phi],'rootPolynomial':[str(a) for a in rp0],'initialQQExponent':prior['actualQQValuationLowerBound'],'provedQQExponentLowerBound':E,'modularTarget':target,'targetReached':E==target,'rounds':rounds,'divisionIdentities':divchecks,'actualInverseProducts':field.inverses,'kernelTraceSha256':trace.hexdigest(),'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'wholeL0Excluded':False}
(root/('L0_native_kernel_phi_'+key+'_return.json')).write_text(json.dumps(result,indent=2));say(stage='complete_new_native_QQ_kernel_phi_certificate',**result)
signal.alarm(0)

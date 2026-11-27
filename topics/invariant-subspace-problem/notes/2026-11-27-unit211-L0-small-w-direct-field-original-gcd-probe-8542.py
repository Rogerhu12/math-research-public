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
cands=json.loads((root/'L0_new_support_group_candidates.json').read_text())['candidates'];allrecords=[]
for key in ['92','36','2','8','3']:
 phi=fmpq_poly([fmpq(aa) for aa in cands[key]]);field=Field(phi);cc=spec_w(C,field);xx=spec_w(X,field);history=[]
 say(stage='BEGIN_whole_QQ_w_candidate_original_return',multiplicityGroup=key,phi=str(phi),degree=phi.degree(),Cdegree=len(cc)-1,Xdegree=len(xx)-1,claimExcluded=False)
 excluded=False
 for i,un in enumerate(units):
  at=spec_w(un,field)
  if not at:excluded=True;history.append(['entireFieldPaidUnitZero',i]);break
  while len(cc)>1:
   gg=gcdp(cc,at)
   if len(gg)<=1:break
   cc=quo(cc,gg);history.append([i,len(gg)-1]);say(stage='exact_paid_QQ_lambda_roots_removed',group=key,unit=i,degreeRemoved=len(gg)-1,remainingCdegree=len(cc)-1)
 if not excluded:
  for label,pp in [('X',X)]+extra+[('Y',Y)]:
   cc=gcdp(cc,spec_w(pp,field));say(stage='actual_QQ_candidate_original_gcd',group=key,curve=label,gcdDegree=len(cc)-1,inverses=field.inverses)
   if len(cc)==1 and cc[0]==1:excluded=True;break
 rec={'group':key,'phi':[str(aa) for aa in phi],'degree':phi.degree(),'excluded':excluded,'paidRootRemovals':history,'remainingLambdaDegree':len(cc)-1,'inverses':field.inverses,'divisions':field.divisions,'bezout':field.bezout,'remainingLambdaPolynomial':[[str(aa) for aa in ff.p] for ff in cc],'allEmbeddingsRetained':True}
 allrecords.append(rec);(root/'L0_new_small_w_QQ_original_returns.json').write_text(json.dumps(allrecords,indent=2))
 say(stage='whole_QQ_w_candidate_original_return',**rec)
say(stage='complete_new_small_w_QQ_returns',allFiveExcluded=all(r['excluded'] for r in allrecords),sourceSha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,wholeL0Excluded=False)
signal.alarm(0)

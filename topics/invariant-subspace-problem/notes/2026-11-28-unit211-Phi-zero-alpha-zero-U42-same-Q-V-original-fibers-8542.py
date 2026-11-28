#!/usr/bin/env python3
"""NEW alpha=0: entire U42 constant fibers, SAME Q, then complete original V.
Only earlier coefficient DEFINITIONS are regenerated and matched by SHA.
No old four-coordinate norm, vertical Bezout, resultant proof, or raw
Gram proof gate is replayed.  New QQ factors, same-Q Bezout, complete
K[Q,V] ideals, and positive D targets keep every complex embedding.
The small matrices have at most 18 rows over an entire QQ constant field.
120 seconds / 1 GiB; no large coefficient payload or cache is exported.
"""
import ast,hashlib,json,math,os,pathlib,resource,signal,time
from flint import fmpq_poly
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def bounded_alarm(seconds):
 tick();left=max(1,math.ceil(DEADLINE-time.perf_counter()))
 return RAW_ALARM(left if seconds<=0 else max(1,min(int(seconds),left)))
signal.alarm=bounded_alarm;signal.alarm(120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
BASE_NAME='2026-11-28-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-8542.py'
BASE_SHA='58cab31654894e8b4a4309f1c6b69619f5ee19591f74256f3128dd2026a4f025'
path=pathlib.Path(__file__).with_name(BASE_NAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASE_NAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
assert full.count('results=[]')==1
prefix=full[:full.index('results=[]')]
assert hashlib.sha256(prefix.encode()).hexdigest()=='7d6fc9ed844a83daccf3978ed572a4b3a803266875c229fb5d3a42e3a75e751c'
# This is a definition-only extraction, not a modification of the old source.
# The old top-level assertions/say records and three denominator-check
# loops are old proof gates, and are NOT executed.  Function/class bodies
# retain their exact arithmetic assertions.  All original coefficient
# assignments, the true Gram factory, and its monic V reduction are kept.
tree=ast.parse(prefix,str(path));kept=[];omitted=[]
for node in tree.body:
 skip=isinstance(node,ast.Assert)
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  skip=skip or isinstance(node.value.func,ast.Name) and node.value.func.id=='say'
 if isinstance(node,ast.For):
  assert isinstance(node.target,ast.Name) and node.target.id in ('value','row')
  skip=True
 if skip:omitted.append([node.lineno,type(node).__name__])
 else:kept.append(node)
program=ast.Module(body=kept,type_ignores=[])
ns={'__name__':'new_alpha_U42_necessary_original_parameter_definitions',
    '__file__':str(path),'print':lambda *a,**kw:None}
exec(compile(ast.fix_missing_locations(program),str(path)+'#definitions-only','exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];oneP=ns['oneP'];zeroP=ns['zeroP']
rows=ns['valueRows'];qcoeff=ns['qcoeff'];info=ns['info']
exact=ns['exact'];strip=ns['strip'];vc=ns['vc']
def normalized(p):
 rem,unit=strip(p)
 if rem:
  lc=rem.coefficient(0);rem/=lc;unit*=lc
 assert rem*unit==p
 return rem
def to_univar(p):
 assert all(int(ex[1])==int(ex[2])==0 for ex in p.to_dict())
 out=[0]*(int(p.degrees()[0])+1) if p else []
 for ex,c in p.to_dict().items():out[int(ex[0])]=c
 return fmpq_poly(out)
def embed_u(p):
 return ctx.from_dict({(j,0,0):p[j] for j in range(int(p.degree())+1) if p[j]})
def qqinfo(p):
 raw=str(p).encode()
 return {'degree':int(p.degree()),'coefficientBytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
# Regenerate the EXACT published N and three pair parameters; there is
# no second execution of any old source's certificate or factor gate.
aa,bb=rows[0].c0,rows[0].c1
q0,q1,_=qcoeff;e2=vc(ns['EBe'],2);head=ns['head']
norm=aa*aa-q1*aa*bb+q0*bb*bb
mu=[aa-q1*bb,-bb,(bb*bb-e2*(aa-q1*bb))/head,e2*bb/head]
den=oneP
for v in mu:den=exact(den,den.gcd(v.d))*v.d
common=zeroP
for v in mu:common=common.gcd(v.n*exact(den,v.d))
N=normalized((R(den)*norm/R(common)).n)
assert info(N)['sha256']=='22cb8b5ccc91ee178afa4abbceeae38e27066de5dbe0e4459c1f861d9c808e04'
expected=[
 '9da720bb18618e80ba9db96559e73dd25c9e4600a8e1576e6e8f046d36e61ad1',
 '80c26662a4c2cbde3cb5e55976061cb117ea9a8ad7d9954c50a2b5e22b95ae83',
 'c04b14a34183209fa97fc6c34f6b503afedbc212c29bbdcc98a0c9b517c5338f']
conditions=[N]
for row,sha in zip(rows[1:],expected):
 p=normalized((row.c1*aa-bb*row.c0).n)
 assert info(p)['sha256']==sha
 conditions.append(p)
# Only coefficient definitions of U42 are regenerated.  No old
# resultant metadata, degree proof, or Bezout coefficients are recomputed.
rN=to_univar(N.resultant(conditions[1],'Q'))
rS=to_univar(N.resultant(conditions[2],'Q'))
U42p=normalized(embed_u(rN.gcd(rS)));U42=to_univar(U42p)
assert info(U42p)['sha256']=='a2ad5fc1085bdb07f18030adf2aba55be3165c43aa773f31f71df30ffae03a65'
assert int(U42.degree())==42
say('new_alpha_U42_exact_parameter_definitions',
 originalFullSourceSHA256=BASE_SHA,
 originalNecessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 omittedOldTopLevelProofStatements=omitted,
 oldRawGramNormVerticalAndProjectionProofGatesNotExecuted=True,
 existingU42SHA256=info(U42p)['sha256'],
 existingFourNecessaryConditionSHA256=[info(p)['sha256'] for p in conditions])
unit,factors=U42.factor();back=fmpq_poly([unit])
factor_list=[]
for ph,e in factors:
 e=int(e);back*=ph**e
 monic=ph/ph[int(ph.degree())]
 factor_list.append((monic,e))
assert back==U42
factor_list.sort(key=lambda pe:(int(pe[0].degree()),str(pe[0])))
say('new_alpha_U42_complete_QQ_factorization',
 allFactorProductReturned=True,
 factors=[{'factor':qqinfo(ph),'multiplicity':e} for ph,e in factor_list],
 allComplexEmbeddingsAndAllQMultiplicitiesKept=True)
class WholeNonunit(Exception):pass

def run_factor(phi,multiplicity,index):
 tick();d=int(phi.degree())
 stat={'constantInverseReturns':0,'qShortDivisionReturns':0,
       'qBezoutReturns':0,'denominatorInverseReturns':0,
       'VProductCoordinateReturns':0,'newColumnCombinationCoordinates':0,
       'newTargetCombinationCoordinates':0}
 inv_cache={}
 class K:
  def __init__(self,p=0):
   if isinstance(p,K):self.p=p.p;return
   p=p if isinstance(p,fmpq_poly) else fmpq_poly([p])
   self.p=p%phi
  def __bool__(self):return bool(self.p)
  def __add__(self,z):return K(self.p+K(z).p)
  __radd__=__add__
  def __neg__(self):return K(-self.p)
  def __sub__(self,z):return self+-K(z)
  def __rsub__(self,z):return K(z)+-self
  def __mul__(self,z):return K(self.p*K(z).p)
  __rmul__=__mul__
  def inverse(self):
   tick();assert self
   key=str(self.p)
   if key in inv_cache:return inv_cache[key]
   g,a,b=self.p.xgcd(phi)
   assert a*self.p+b*phi==g and int(g.degree())==0
   out=K(a/g[0]);assert self*out==K(1) and out*self==K(1)
   if len(inv_cache)<2000:inv_cache[key]=out
   stat['constantInverseReturns']+=1
   return out
  def __truediv__(self,z):return self*K(z).inverse()
  def __rtruediv__(self,z):return K(z)*self.inverse()
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=K(1);v=self
   while n:
    if n&1:out=out*v
    n//=2
    if n:v=v*v
   return out
  def __eq__(self,z):return self.p==K(z).p
  def coordinates(self):return [str(self.p[j]) for j in range(d)]
 k0,k1=K(),K(1);U=K(fmpq_poly([0,1]));upowers=[k1]
 def upow(n):
  while len(upowers)<=n:upowers.append(upowers[-1]*U)
  return upowers[n]
 def trim(p):
  p=list(p)
  while p and not p[-1]:p.pop()
  return p
 def pa(a,b):
  return trim([(a[i] if i<len(a) else k0)+(b[i] if i<len(b) else k0)
               for i in range(max(len(a),len(b)))])
 def pn(a):return [-x for x in a]
 def ps(a,b):return pa(a,pn(b))
 def pc(a,c):return trim([x*c for x in a])
 def pm(a,b):
  if not a or not b:return []
  out=[k0]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
  return trim(out)
 def pd(a,b):
  tick();a=trim(a);b=trim(b);assert b
  rem=list(a);quo=[k0]*max(0,len(a)-len(b)+1);iv=b[-1].inverse()
  while rem and len(rem)>=len(b):
   j=len(rem)-len(b);c=rem[-1]*iv;quo[j]=quo[j]+c
   rem=ps(rem,[k0]*j+pc(b,c))
  quo=trim(quo)
  assert not ps(a,pa(pm(quo,b),rem))
  assert not rem or len(rem)<len(b)
  stat['qShortDivisionReturns']+=1
  return quo,rem
 def pgcd(a,b):
  r0,r1=trim(a),trim(b);s0,s1=[k1],[];t0,t1=[],[k1]
  while r1:
   q,r=pd(r0,r1)
   r0,r1=r1,r;s0,s1=s1,ps(s0,pm(q,s1));t0,t1=t1,ps(t0,pm(q,t1))
  if r0:
   iv=r0[-1].inverse();r0=pc(r0,iv);s0=pc(s0,iv);t0=pc(t0,iv)
  assert not ps(r0,pa(pm(s0,a),pm(t0,b)))
  stat['qBezoutReturns']+=1
  return r0,s0,t0
 def pinfo(p):
  raw=json.dumps([x.coordinates() for x in p],separators=(',',':')).encode()
  return {'QDegree':len(p)-1,'constantDegree':d,
          'coefficientBytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
 def weight(p):
  assert all(int(ex[2])==0 for ex in p.to_dict())
  out=[k0]*(int(p.degrees()[1])+1) if p else []
  for ex,c in p.to_dict().items():
   j=int(ex[1]);out[j]=out[j]+K(c)*upow(int(ex[0]))
  return trim(out)
 say('new_alpha_constant_fiber_started',factorIndex=index,
     factor=qqinfo(phi),multiplicity=multiplicity,
     originalRows=['EBe','N1','NS','PS'])
 inputs=[weight(p) for p in conditions]
 assert inputs[0] # N's already published coefficient Bezout is 1.
 g=[];bez=[]
 for j,p in enumerate(inputs):
  gg,a,b=pgcd(g,p);bez=[pm(a,x) for x in bez]+[b];g=gg
  check=[]
  for x,c in zip(bez,inputs):check=pa(check,pm(x,c))
  assert not ps(g,check)
  say('new_alpha_same_Q_original_scalar_Bezout',
      factorIndex=index,conditionIndex=j,monicCommonQDegree=len(g)-1,
      allActualCoefficientCombinationReturned=True)
  if len(g)==1:break
 assert g
 if len(g)==1:
  say('new_alpha_constant_fiber_result',factorIndex=index,factor=qqinfo(phi),
      wholePhysicalFiberExcluded=True,reason='same Q original scalar unit',
      newWeightPointUpperBound=0,newCompleteNormalizedPointUpperBound=0,
      statistics=stat)
  return {'closed':True,'weights':0,'complete':0,'QV':0}
 # Remove only whole primary factors supported on an ORIGINAL paid unit.
 # Every removal c divides U; after at most deg(g) such removals the
 # discarded product divides U^deg(g).  No field factor or mod root is chosen.
 paidQ=weight(ns['paidP']);good=list(g);discarded=[k1];steps=0
 while len(good)>1:
  c,_,_=pgcd(good,paidQ)
  if len(c)<=1:break
  good,rr=pd(good,c);assert not rr
  discarded=pm(discarded,c);steps+=1
 assert not ps(g,pm(discarded,good))
 if len(good)==1:
  say('new_alpha_constant_fiber_result',factorIndex=index,factor=qqinfo(phi),
      wholePhysicalFiberExcluded=True,reason='all same Q components violate original units',
      paidPrimaryRemovalSteps=steps,newWeightPointUpperBound=0,
      newCompleteNormalizedPointUpperBound=0,statistics=stat)
  return {'closed':True,'weights':0,'complete':0,'QV':0}
 gu,au,bu=pgcd(good,paidQ);assert len(gu)==1 and gu[0]==k1
 dq=len(good)-1;dim=2*dq
 assert dq<=9
 say('new_alpha_same_Q_whole_paid_model',factorIndex=index,
     monicQPolynomial=pinfo(good),retainedQDegree=dq,
     paidPrimaryRemovalSteps=steps,wholePaidUnitBezoutReturned=True,
     allRetainedQMultiplicitiesKept=True,
     KDimension=dim,QQDimension=d*dim)
 def lr(p):return pd(p,good)[1]
 def la(a,b):return lr(pa(a,b))
 def ls(a,b):return lr(ps(a,b))
 def lm(a,b):return lr(pm(a,b))
 linverse_cache={}
 def li(p):
  p=lr(p);key=str([x.p for x in p])
  if key in linverse_cache:return linverse_cache[key]
  gg,a,b=pgcd(p,good)
  if len(gg)!=1:raise WholeNonunit('complete retained Q algebra denominator is not a unit')
  inv=lr(pc(a,gg[0].inverse()))
  assert lm(p,inv)==[k1] and lm(inv,p)==[k1]
  linverse_cache[key]=inv;stat['denominatorInverseReturns']+=1
  return inv
 def lv(value):
  value=R(value);n=weight(value.n);de=weight(value.d)
  out=lm(lr(n),li(de))
  assert lm(out,lr(de))==lr(n)
  return out
 qv0,qv1=lv(qcoeff[0]),lv(qcoeff[1])
 def az():return [[],[]]
 def aa(a,b):return [la(a[0],b[0]),la(a[1],b[1])]
 def an(a):return [lr(pn(a[0])),lr(pn(a[1]))]
 def ass(a,b):return aa(a,an(b))
 def ac(a,c):return [lm(a[0],c),lm(a[1],c)]
 def am(a,b):
  z0=lm(a[0],b[0]);z1=la(lm(a[0],b[1]),lm(a[1],b[0]));z2=lm(a[1],b[1])
  out=[ls(z0,lm(z2,qv0)),ls(z1,lm(z2,qv1))]
  assert la(out[0],lm(z2,qv0))==z0 and la(out[1],lm(z2,qv1))==z1
  stat['VProductCoordinateReturns']+=2
  return out
 def ap(a,n):
  out=[[k1],[]]
  for _ in range(n):out=am(out,a)
  return out
 def av(value):
  value=R(value);assert ns['weight'](value.d)
  out=az();vv=[[],[k1]]
  for j in range(ns['vdegree'](value),-1,-1):
   out=aa(am(out,vv),[lv(vc(value,j)),[]])
  return out
 def flat(a):
  return [(a[k][j] if j<len(a[k]) else k0) for k in range(2) for j in range(dq)]
 originals=[[lv(row.c0),lv(row.c1)] for row in rows]
 basisA=[]
 for vpow in range(2):
  for j in range(dq):
   qj=lr([k0]*j+[k1])
   basisA.append([qj,[]] if vpow==0 else [[],qj])
 columns=[];column_labels=[]
 for i,row in enumerate(originals):
  for j,b in enumerate(basisA):
   columns.append(flat(am(row,b)));column_labels.append([i,j])
 # These are ALL basis multiples of the four original generators in
 # a genuine monic Q,V polynomial algebra, not a fixed-degree container.
 def zero_vec():return [k0]*dim
 def combo_sum(comb):
  out=zero_vec()
  for j,c in comb.items():
   for k in range(dim):out[k]=out[k]+c*columns[j][k]
  return out
 def cclean(c):return {i:x for i,x in c.items() if x}
 echelon={};selected=[]
 for j,col in enumerate(columns):
  tick();v=list(col);comb={j:k1}
  for piv in sorted(echelon):
   if not v[piv]:continue
   w,wb=echelon[piv];c=v[piv]
   v=[x-c*y for x,y in zip(v,w)]
   for i,x in wb.items():comb[i]=comb.get(i,k0)-c*x
   comb=cclean(comb)
  pivot=next((i for i,x in enumerate(v) if x),None)
  if pivot is None:continue
  iv=v[pivot].inverse();v=[x*iv for x in v];comb={i:x*iv for i,x in comb.items()}
  assert combo_sum(comb)==v
  stat['newColumnCombinationCoordinates']+=dim
  echelon[pivot]=(v,comb);selected.append(j)
  if len(echelon)==dim:break
 rank=len(echelon);remaining=dim-rank
 def target_return(target):
  v=list(target);comb={}
  for piv in sorted(echelon):
   if not v[piv]:continue
   w,wb=echelon[piv];c=v[piv]
   v=[x-c*y for x,y in zip(v,w)]
   for i,x in wb.items():comb[i]=comb.get(i,k0)+c*x
   comb=cclean(comb)
  returned=combo_sum(comb)
  assert [x+y for x,y in zip(returned,v)]==target
  stat['newTargetCombinationCoordinates']+=dim
  return v,comb
 one=[[k1],[]];res,comb=target_return(flat(one))
 exponent=0 if not any(res) else None
 if exponent is None:
  # The real same-point D = ell*(2 lambda^2-2 lambda+1)-T^2.
  # No geometric value or norm is inverted anywhere in this source.
  lam=av(ns['lam']);Tr=av(ns['Tr'])
  al=aa(ass(ac(am(lam,lam),[K(2)]),ac(lam,[K(2)])),one)
  D=ass(ac(al,lv(ns['ell'])),am(Tr,Tr))
  power=one
  for n in range(1,remaining+1):
   power=am(power,D);res,comb=target_return(flat(power))
   if not any(res):exponent=n;break
 closed=exponent is not None
 # A nonzero residual is retained; it is never called physical nonempty.
 qvbound=0 if closed else d*remaining
 weightbound=0 if closed else d*min(dq,remaining)
 result={'closed':closed,'weights':weightbound,'QV':qvbound,'complete':2*qvbound}
 say('new_alpha_constant_fiber_result',factorIndex=index,factor=qqinfo(phi),
     wholePhysicalFiberExcluded=closed,
     target='1' if exponent==0 else ('D^n' if closed else 'unreturned'),
     returnedPositiveDExponent=exponent,
     actualKMatrixRows=dim,actualOriginalColumns=len(columns),
     selectedOriginalColumnIndices=selected,actualIdealRankOverK=rank,
     remainingKAlgebraDimension=remaining,
     newWeightPointUpperBound=weightbound,
     newUQVPointUpperBound=qvbound,
     newCompleteNormalizedPointUpperBound=2*qvbound,
     everyTargetCoordinateReturned=True,noDInverseUsed=True,
     allComplexEmbeddingsKept=True,statistics=stat)
 return result

completed=[];retained_exceptional=[]
for index,(phi,e) in enumerate(factor_list):
 try:
  completed.append(run_factor(phi,e,index))
 except WholeNonunit as exc:
  d=int(phi.degree());retained_exceptional.append(index)
  completed.append({'closed':False,'weights':9*d,'QV':18*d,'complete':36*d})
  say('new_alpha_constant_fiber_nonunit_retained',factorIndex=index,
      factor=qqinfo(phi),reason=str(exc),wholeFactorRetained=True,
      noPartialEmbeddingOrPrimeSelection=True)
say('new_alpha_U42_same_Q_V_original_fibers_complete',
 entireAlphaZeroExcluded=all(x['closed'] for x in completed),
 completedWholeQQFactors=len(completed),
 retainedUnexpectedNonunitFactorIndices=retained_exceptional,
 distinctWeightPointUpperBound=min(378,sum(x['weights'] for x in completed)),
 distinctUQVPointUpperBound=min(756,sum(x['QV'] for x in completed)),
 distinctCompleteNormalizedPointUpperBound=min(1512,sum(x['complete'] for x in completed)),
 countsArePointUpperBoundsNotSchemeLengths=True,
 currentScope='correct Phi, original D nonzero, alpha zero',
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noOldProofGateReplayed=True,noCoefficientPayloadSaved=True)

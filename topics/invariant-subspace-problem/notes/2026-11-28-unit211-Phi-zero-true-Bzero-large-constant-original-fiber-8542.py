#!/usr/bin/env python3
"""NEW true B: one complete F34 or F40 constant fiber, selected by env.
ISP_B_FACTOR_DEGREE must be 34 or 40; each is a separate first input.
Only regenerate terminal DENOMINATOR DEFINITIONS to identify the already
proved C76/F34/F40 inputs by exact SHA.  Old full multiplier returns,
C76 support proof/classification, C315 and QQ2 gates are not executed.
New QQ constant-field I4 lambda cofactors give a genuine monic g, then
new original NS/PS live in K[lambda,omega]/(g,q_omega), all nilpotents.
Only full original-ideal membership of a positive physical-unit power
closes this entire fiber.  No D/norm inverse.  120 seconds / 1 GiB.
"""
import ast,gc,hashlib,itertools,json,math,os,pathlib,resource,signal,time
from flint import fmpq,fmpq_poly,fmpq_mat
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def bounded_alarm(seconds):
 if seconds<=0:return RAW_ALARM(0)
 tick();return RAW_ALARM(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
DEG=int(os.environ.get('ISP_B_FACTOR_DEGREE','34'))
assert DEG in (34,40)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def read_source(name,sha):
 path=pathlib.Path(__file__).with_name(name)
 if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/name
 full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==sha
 return path,full
BASE_NAME='2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py'
BASE_SHA='b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56'
base_path,base_full=read_source(BASE_NAME,BASE_SHA)
MARKER='newValues=[];quotients=[]';assert base_full.count(MARKER)==1
prefix=base_full[:base_full.index(MARKER)]
env={'__name__':'new_B_F34_F40_original_definition_only',
     '__file__':str(base_path),'print':lambda *a,**kw:None}
exec(compile(prefix,str(base_path)+'#necessary_definitions_only','exec'),env)
signal.alarm=bounded_alarm;signal.alarm(120)
# The following immutable old source is only an exact PARAMETER definition.
# It is not run as a source or as an old proof gate.  Its loader, NS/PS
# reductions, old factor-classification and every old proof check are skipped.
TERM_NAME='2026-11-28-unit211-Phi-zero-true-Bzero-terminal-original-multiplier-cancellation-8542.py'
TERM_SHA='73d4dd4167d48b5a5878338bdfe85dc6c59a194b97fa2ae23309e2c2226eac35'
term_path,term_full=read_source(TERM_NAME,TERM_SHA)
begin="R=env['R'];ctx=env['ctx'];up,Qp,Lp,Tp,zp=ctx.gens()"
end='scaled=[[R(cover)*a for a in beta] for beta in final]'
assert term_full.count(begin)==1 and term_full.count(end)==1
parameter_code=term_full[term_full.index(begin):term_full.index(end)]
old_check=(
"check=[]\n"
"for beta,fi in zip(final,changed):check=env['add'](check,env['mul'](beta,fi))\n"
"assert not env['sub'](check,[R(1)])\n"
)
assert parameter_code.count(old_check)==1
parameter_code=parameter_code.replace(old_check,'')
class ParameterDefinitionsOnly(ast.NodeTransformer):
 def visit_Assert(self,node):return ast.copy_location(ast.Pass(),node)
 def visit_Expr(self,node):
  if isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='say':
   return ast.copy_location(ast.Pass(),node)
  return self.generic_visit(node)
tree=ParameterDefinitionsOnly().visit(ast.parse(parameter_code))
ast.fix_missing_locations(tree)
params={'env':env,'START':START,'BASE_SHA':BASE_SHA,
        'hashlib':hashlib,'json':json,'time':time,'print':lambda *a,**kw:None}
exec(compile(tree,str(term_path)+'#terminal_denominator_parameter_definitions_only','exec'),params)
cover=params['cover']
cover_sha=hashlib.sha256(str(sorted(cover.to_dict().items())).encode()).hexdigest()
assert cover_sha=='5eb0b13c682928e24c8449fa7dbbfa7a890fd72438897a4ae98de523ae778242'
# Factoring here only retrieves the existing parameter, not a new C76
# factorization theorem.  Exact immutable factor SHAs identify the input.
EXPECTED={
 34:'b593d2770a0337dcaf2f4908e51cfc9feb3c5890ce21e5c3c6c1707ff98187ff',
 40:'ba88a205beb579a18de711c9fd61514716099afeed94954736246cedf733a16a'}
_,factor_defs=env['univar'](cover).factor()
hits=[]
for fac,power in factor_defs:
 if int(fac.degree())!=DEG:continue
 fp=env['multivar'](fac)
 hsh=hashlib.sha256(str(sorted(fp.to_dict().items())).encode()).hexdigest()
 assert int(power)==1 and hsh==EXPECTED[DEG]
 hits.append(fac)
assert len(hits)==1
phi=hits[0]/hits[0][DEG];d=DEG
say('new_B_large_constant_exact_parameter_defined',
 constantDegree=d,exactFactorSHA256=EXPECTED[d],existingC76SHA256=cover_sha,
 parameterDefinitionSourceSHA256=TERM_SHA,
 parameterTextSHA256=hashlib.sha256(parameter_code.encode()).hexdigest(),
 oldFullMultiplierIdentitiesNotExecuted=True,
 oldC76ProofAndClassificationNotRunAsGate=True,
 originalSixRowDefinitionPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 noCoefficientPayloadPrinted=True)
del params,tree,parameter_code,cover,factor_defs,hits
gc.collect()
stats={'constantReductions':0,'wholeConstantInverseReturns':0,
 'lambdaShortDivisions':0,'lambdaBezoutReturns':0,
 'originalCofactorCoordinates':0,'originalRowsReturned':0,
 'omegaProductReturns':0,'selectedMatrixInverseCoordinates':0,
 'allOriginalIdealColumnCoordinates':0,'targetCoordinates':0}
inv_cache={}
class K:
 def __init__(self,p=0):
  if isinstance(p,K):self.p=p.p;return
  p=p if isinstance(p,fmpq_poly) else fmpq_poly([p])
  self.p=p%phi;stats['constantReductions']+=1
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
  out=K(a/g[0])
  assert self*out==K(1) and out*self==K(1)
  inv_cache[key]=out;stats['wholeConstantInverseReturns']+=1
  return out
 def __truediv__(self,z):return self*K(z).inverse()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=K(1);a=self
  while n:
   if n&1:out=out*a
   n//=2
   if n:a=a*a
  return out
 def __eq__(self,z):return self.p==K(z).p
 def coordinates(self):return [str(self.p[j]) for j in range(d)]
K0=K();K1=K(1);X=K(fmpq_poly([0,1]))
def trim(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
def pa(a,b):
 return trim([(a[i] if i<len(a) else K0)+(b[i] if i<len(b) else K0)
              for i in range(max(len(a),len(b)))])
def pn(a):return [-c for c in a]
def ps(a,b):return pa(a,pn(b))
def pc(a,c):return trim([v*c for v in a])
def pm(a,b):
 if not a or not b:return []
 out=[K0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return trim(out)
def pd(a,b):
 tick();a=trim(a);b=trim(b);assert b
 rem=list(a);quo=[K0]*max(0,len(a)-len(b)+1);iv=b[-1].inverse()
 while rem and len(rem)>=len(b):
  j=len(rem)-len(b);c=rem[-1]*iv;quo[j]=quo[j]+c
  rem=ps(rem,[K0]*j+pc(b,c))
 quo=trim(quo)
 assert not ps(a,pa(pm(quo,b),rem))
 assert not rem or len(rem)<len(b)
 stats['lambdaShortDivisions']+=1;return quo,rem
def pgcd(a,b):
 r0,r1=trim(a),trim(b);s0,s1=[K1],[];t0,t1=[],[K1]
 while r1:
  q,r=pd(r0,r1)
  r0,r1=r1,r;s0,s1=s1,ps(s0,pm(q,s1));t0,t1=t1,ps(t0,pm(q,t1))
 if r0:
  iv=r0[-1].inverse();r0=pc(r0,iv);s0=pc(s0,iv);t0=pc(t0,iv)
 assert not ps(r0,pa(pm(s0,a),pm(t0,b)))
 stats['lambdaBezoutReturns']+=1;return r0,s0,t0
def pinfo(p):
 raw=json.dumps([v.coordinates() for v in p],separators=(',',':')).encode()
 return {'lambdaDegree':len(p)-1,'constantDegree':d,'coefficientBytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
def ew(p):
 assert env['pure_x'](p)
 data=p.to_dict();out=K0
 for j in range(int(p.degrees()[0]) if p else -1,-1,-1):
  out=out*X+K(data.get((j,0,0,0,0),0))
 return out
weight=ew(env['paid']);weight.inverse()
def cv(v):
 assert env['pure_x'](v.d)
 den=ew(v.d);iv=den.inverse();coeff={}
 for ex,a in v.n.to_dict().items():
  assert ex[1]==ex[3]==ex[4]==0
  j=int(ex[2]);value=K(a)*X**int(ex[0])
  coeff[j]=coeff.get(j,K0)+value
 out=trim([coeff.get(j,K0)*iv for j in range(max(coeff,default=-1)+1)])
 for j,val in coeff.items():assert (out[j] if j<len(out) else K0)*den==val
 return out
qw=[cv(v) for v in env['qw']]
assert len(qw)==3 and qw[2]==[K1]
fhat=[cv(v) for v in env['fhat']]
that=[cv(v) for v in env['that']]
linear=[[cv(v) for v in row] for row in env['linear']]
assert len(linear)==4
# All operations below are on this new complete constant field; no
# symbolic x/lambda scalar from the old C76 calculation is recomputed.
def oa(a,b):return [pa(a[0],b[0]),pa(a[1],b[1])]
def oc(a,c):return [pm(a[0],c),pm(a[1],c)]
def om(a,b):
 c0=pm(a[0],b[0]);c1=pa(pm(a[0],b[1]),pm(a[1],b[0]));c2=pm(a[1],b[1])
 out=[ps(c0,pm(c2,qw[0])),ps(c1,pm(c2,qw[1]))]
 assert not ps(c0,pa(out[0],pm(c2,qw[0])))
 assert not ps(c1,pa(out[1],pm(c2,qw[1])))
 stats['omegaProductReturns']+=1;return out
def op(a,n):
 out=[[K1],[]]
 for _ in range(n):out=om(out,a)
 return out
def raw_remainder(value,limit):
 out=[[],[]]
 for (i,j),v in env['coefficients'](value,limit).items():
  out=oa(out,oc(om(op(fhat,i),op(that,j)),cv(v)))
 return out
for i,value in enumerate(env['original']):
 row=raw_remainder(value,2)
 assert all(not ps(row[j],linear[i][j]) for j in range(2))
 stats['originalRowsReturned']+=1
say('new_B_complete_large_constant_I4_input',
 constantDegree=d,allComplexEmbeddingsKept=True,
 monicOmegaCoefficientLambdaDegrees=[len(v)-1 for v in qw],
 fourOriginalRowLambdaDegrees=[[len(v)-1 for v in row] for row in linear],
 allFourActualOriginalRowsReturned=True,
 allOriginalWeightAndCoordinateDenominatorsWholeUnitsReturned=True)
# NEW I4-only constant-field scalar combination.  If the degree is
# positive it is an actual original monic lambda relation, not a
# numerical observed degree or generic lambda leading localization.
cof=[];bez=[];g=[]
for i,j in itertools.combinations(range(4),2):
 tick();c=ps(pm(linear[i][0],linear[j][1]),pm(linear[i][1],linear[j][0]))
 assert not ps(c,ps(pm(linear[j][1],linear[i][0]),pm(linear[i][1],linear[j][0])))
 assert not ps(pm(linear[j][1],linear[i][1]),pm(linear[i][1],linear[j][1]))
 stats['originalCofactorCoordinates']+=2
 cof.append((i,j,c))
 if not c:bez.append([]);continue
 gg,a,b=pgcd(g,c);bez=[pm(a,v) for v in bez]+[b];g=gg
 check=[]
 for be,(_,_,ci) in zip(bez,cof):check=pa(check,pm(be,ci))
 assert not ps(check,g)
 say('new_B_large_constant_I4_lambda_gcd_checkpoint',
     constantDegree=d,originalPair=[i,j],cofactorDegree=len(c)-1,
     completedMonicGCDDegree=len(g)-1)
 if len(g)==1:break
comb=[[] for _ in range(4)]
for be,(i,j,c) in zip(bez,cof):
 comb[i]=pa(comb[i],pm(be,linear[j][1]))
 comb[j]=ps(comb[j],pm(be,linear[i][1]))
for k in range(2):
 ret=[]
 for c,row in zip(comb,linear):ret=pa(ret,pm(c,row[k]))
 assert not ps(ret,g if k==0 else [])
say('new_B_large_constant_complete_I4_lambda_Bezout',
 constantDegree=d,usedOriginalPairs=[[i,j] for i,j,_ in cof],
 monicOriginalLambdaRelation=pinfo(g),
 bothCompleteOriginalCombinationCoordinatesReturned=True,
 wholeFactorExcluded=len(g)==1)
if len(g)<=1:
 say('new_B_large_constant_terminal_result',constantDegree=d,
     wholeFactorExcluded=len(g)==1,
     reason='actual original 1' if g else 'no nonzero I4 scalar relation; whole factor retained',
     otherFactorNotTested=True,wholeBExcluded=False,ordinaryISPClaim=False,
     statistics=stats)
else:
 n=len(g)-1;DIM=2*d*n
 def br(p):return pd(p,g)[1]
 def ba(a,b):return br(pa(a,b))
 def bs(a,b):return br(ps(a,b))
 def bm(a,b):return br(pm(a,b))
 q0,q1=br(qw[0]),br(qw[1])
 def ar(a):return [br(a[0]),br(a[1])]
 def am(a,b):
  c0=bm(a[0],b[0]);c1=ba(bm(a[0],b[1]),bm(a[1],b[0]));c2=bm(a[1],b[1])
  out=[bs(c0,bm(c2,q0)),bs(c1,bm(c2,q1))]
  assert not bs(c0,ba(out[0],bm(c2,q0)))
  assert not bs(c1,ba(out[1],bm(c2,q1)))
  stats['omegaProductReturns']+=1;return out
 def aa(a,b):return [ba(a[0],b[0]),ba(a[1],b[1])]
 def ac(a,c):return [bm(a[0],c),bm(a[1],c)]
 def ap(a,k):
  out=ar([[K1],[]])
  for _ in range(k):out=am(out,a)
  return out
 FH,TH=ar(fhat),ar(that)
 def new_value_remainder(value,limit):
  out=[[],[]]
  for (i,j),v in env['coefficients'](value,limit).items():
   out=aa(out,ac(am(ap(FH,i),ap(TH,j)),br(cv(v))))
  return out
 original_rows=[ar(row) for row in linear]
 # Complete new raw weighted N/P, only AFTER the new I4 monic lambda
 # relation; every product remains in the original finite algebra.
 original_rows.extend([new_value_remainder(env['NS'],3),
                       new_value_remainder(env['PS'],3)])
 stats['originalRowsReturned']+=2
 say('new_B_large_constant_complete_original_NP_in_finite_model',
     constantDegree=d,monicLambdaDegree=n,monicOmegaDegree=2,
     fullQQAlgebraDimension=DIM,allSixOriginalRowsPresent=True,
     lambdaAndOmegaNilpotentsKept=True,
     noDOrLambdaOrTInverse=True)
 def flat(z):
  out=[]
  for omega in range(2):
   for j in range(n):
    value=z[omega][j] if j<len(z[omega]) else K0
    out.extend([value.p[i] for i in range(d)])
  assert len(out)==DIM;return out
 basis=[]
 for omega in range(2):
  for j in range(n):
   for k in range(d):
    row=[[],[]];row[omega]=[K0]*j+[K(fmpq_poly([0]*k+[1]))]
    basis.append(ar(row))
 for j,row in enumerate(basis):
  assert flat(row)==[fmpq(int(i==j)) for i in range(DIM)]
 columns=[];tags=[]
 for i,row in enumerate(original_rows):
  for j,b in enumerate(basis):
   tick();columns.append(flat(am(row,b)));tags.append([i,j])
 MAT=fmpq_mat([[columns[j][i] for j in range(len(columns))] for i in range(DIM)])
 RF,rank=MAT.rref();rank=int(rank)
 selected=[next(j for j in range(len(columns)) if RF[i,j]) for i in range(rank)]
 if rank:
  N=fmpq_mat([[MAT[i,j] for j in selected] for i in range(DIM)])
  RT,rnk=N.transpose().rref();assert int(rnk)==rank
  I=[next(j for j in range(DIM) if RT[i,j]) for i in range(rank)]
  SQ=fmpq_mat([[MAT[i,j] for j in selected] for i in I]);INV=SQ.inv()
  ID=fmpq_mat([[int(i==j) for j in range(rank)] for i in range(rank)])
  assert SQ*INV==ID and INV*SQ==ID
  stats['selectedMatrixInverseCoordinates']+=2*rank*rank
  restriction=fmpq_mat([[MAT[i,j] for j in range(len(columns))] for i in I])
  assert N*INV*restriction==MAT
  stats['allOriginalIdealColumnCoordinates']=DIM*len(columns)
 else:N=None;I=[];INV=None
 def member(v):
  rhs=flat(v)
  if not rank:
   okay=not any(rhs)
   if okay:stats['targetCoordinates']+=DIM
   return okay
  c=INV*fmpq_mat([[rhs[i]] for i in I]);ret=N*c
  okay=all(ret[i,0]==rhs[i] for i in range(DIM))
  if okay:stats['targetCoordinates']+=DIM
  return okay
 D0=env['ell']*(2*env['lam']**2-2*env['lam']+1)-env['T']**2
 Drow=new_value_remainder(D0,2)
 Lrow=ar([[K0,K1],[]])
 unit=am(am(Lrow,TH),Drow)
 ONE=ar([[K1],[]]);power=ONE;found=None
 for exponent in range(DIM+1):
  tick();ok=member(power)
  say('new_B_large_constant_actual_positive_unit_target',
      constantDegree=d,power=exponent,target='(lambda*t*Dval)^n',
      exactOriginalIdealMembershipReturned=ok,
      idealQQRank=rank,fullQQAlgebraDimension=DIM)
  if ok:found=exponent;break
  if exponent<DIM:power=am(power,unit)
 say('new_B_large_constant_full_original_ideal_return',
     constantDegree=d,monicLambdaDegree=n,fullQQAlgebraDimension=DIM,
     originalIdealMatrixShape=[DIM,len(columns)],actualIdealQQRank=rank,
     quotientQQDimension=DIM-rank,selectedOriginalColumns=selected,
     selectedCoefficientRows=I,selectedOriginalColumnTags=[tags[j] for j in selected],
     positivePhysicalUnitPowerReturned=found,
     entireLambdaAndOmegaNilpotentsKept=True,allComplexConstantEmbeddingsKept=True,
     physicalTargetIdentity='Dval=ell*(2lambda^2-2lambda+1)-T^2=bc*(h-k)^2',
     noDOrNormInverse=True,wholeFactorExcluded=found is not None,
     otherFactorNotTested=True,wholeBExcluded=False,wholePhiExcluded=False,
     ordinaryISPClaim=False,statistics=stats)
say('new_B_large_constant_first_input_finished',constantDegree=d,
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 noOldProofGateExecuted=True,noLargeCoefficientPayloadSaved=True)

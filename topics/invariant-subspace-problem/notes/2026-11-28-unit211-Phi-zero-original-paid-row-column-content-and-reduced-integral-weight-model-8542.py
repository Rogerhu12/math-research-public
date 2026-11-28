#!/usr/bin/env python3
"""NEW original paid row/column content of the same Phi22 matrix.
All divided factors are actual parts of previously paid original
weight units; every matrix entry is multiplied back. The exact789
degree already paid gives the reduced determinant degree by a
literal determinant identity. A new smaller modular polynomial is
computed only as coefficient input for its complete finite model
and factor-block structure, not to reprove the old determinant.
No H42 or physical D inverse. 120 seconds /1 GiB total.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,nmod_poly
START=time.perf_counter();DEADLINE=START+120
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-unlowered-twenty-two-original-columns-and-fixed-u-degree-8542.py"
path=Path(os.environ.get("ISP_PHI_RAW_TWENTYTWO_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="043ffc06d0a48f804111ff35cbfee0922fe9a69c87c414f75099b8413cf4b53e"
mark=b"\nN=22\n";assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==4080
assert hashlib.sha256(prefix).hexdigest()=="d6e4f9f2eaabf58efe7a06c7b4b4da8b3effb77cadc3f881c4a5ba12a3804e89"
sc={"__file__":str(path),"__name__":"new_original22_paid_content_definition"}
oa=signal.alarm;ot=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-original22-column-definition","exec"),sc)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))

R,ctx,one,zero,geo,columns,coordinate,exact,profile,C6=[
 sc[x] for x in ["R","ctx","one","zero","geo","columns","coordinate","exact","profile","C6"]]
n=22;p=1009;Q0=2
def pair(x):
 ab=str(x).split("/")
 return int(ab[0]),int(ab[1]) if len(ab)>1 else 1
def vp(a):
 if not a:return 10**9
 a=abs(a);v=0
 while a%p==0:a//=p;v+=1
 return v
def qmod(x):
 a,b=pair(x);assert b%p
 return a%p*pow(b%p,-1,p)%p
def gauss_primitive(poly):
 vals=[vp(pair(c)[0])-vp(pair(c)[1]) for c in poly.to_dict().values() if c]
 v=min(vals)
 scalar=fmpq(p**(-v)) if v<=0 else fmpq(1,p**v)
 result=poly*scalar
 assert result==poly*scalar
 assert min(vp(pair(c)[0])-vp(pair(c)[1]) for c in result.to_dict().values() if c)==0
 for c in result.to_dict().values():qmod(c)
 return result,-v
B=[[zero for _ in range(n)] for _ in range(n)]
original_clear_returns=0
for j,row in enumerate(columns):
 den=one
 for x in row:den=exact(den,den.gcd(x.d))*x.d
 polys=[x.n*exact(den,x.d) for x in row]
 for c,poly in enumerate(polys):
  assert R(poly)==row[c]*R(den);original_clear_returns+=1
  for ex,value in poly.to_dict().items():
   assert not ex[3] and not ex[4]
   i=coordinate(c,int(ex[2]))
   B[i][j]=B[i][j]+ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):value})
# The original p-Gauss column constants were all zero; retain the
# identical B22 and check its complete coefficient integrality.
for row in B:
 for poly in row:
  for x in poly.to_dict().values():qmod(x)
C=[[poly+zero for poly in row] for row in B]
rowunits=[one for _ in range(n)];colunits=[one for _ in range(n)]
events=[];returns=0
for axis in ["row","column"]:
 for k in range(n):
  vec=C[k] if axis=="row" else [C[i][k] for i in range(n)]
  gg=zero
  for x in vec:
   if x:gg=x if not gg else gg.gcd(x)
  assert gg
  residual,unit,history=geo["strip_paid"](gg,False)
  assert residual*unit==gg
  if int(unit.total_degree())==0:continue
  unit,constant_exp=gauss_primitive(unit)
  assert geo["weight_only"](unit)
  # Its physical unit source is the exact strip-paid sequence,
  # plus a nonzero rational constant, never a new weight inverse.
  rest,_,_=geo["strip_paid"](unit,False)
  assert int(rest.total_degree())==0
  for i,x in enumerate(vec):
   y=exact(x,unit);assert y*unit==x;returns+=1
   for q in y.to_dict().values():qmod(q)
   if axis=="row":C[k][i]=y
   else:C[i][k]=y
  if axis=="row":rowunits[k]=unit
  else:colunits[k]=unit
  event=dict(axis=axis,index=k,removedOnlyOriginalUnits=history,
             pGaussConstantExponent=constant_exp,actualPaidFactor=profile(unit),
             fullEntryDivisionReturns=n)
  events.append(event)
  say("new_actual_original_paid_matrix_content",**event)
for i in range(n):
 for j in range(n):
  assert rowunits[i]*C[i][j]*colunits[j]==B[i][j]
  returns+=1
allunits=rowunits+colunits
du=sum(int(x.degrees()[0]) for x in allunits)
dQ=sum(int(x.degrees()[1]) for x in allunits)
dt=sum(int(x.total_degree()) for x in allunits)
reduced_degree=789-du
assert 0<=reduced_degree<=789
def q2poly(poly):
 d={}
 for ex,c in poly.to_dict().items():
  assert not any(ex[2:])
  k=int(ex[0]);d[k]=(d.get(k,0)+qmod(c)*pow(Q0,int(ex[1]),p))%p
 return nmod_poly([d.get(i,0) for i in range(max(d)+1)],p) if d else nmod_poly([],p)
unit_lc=1
for unit in allunits:
 uu=q2poly(unit)
 assert int(uu.degree())==int(unit.degrees()[0])
 unit_lc=unit_lc*int(uu[int(uu.degree())])%p
assert unit_lc
expected_lc=790*pow(unit_lc,-1,p)%p
say("new_exact_reduced_original_weight_model_before_modular_input",
 originalQQDegreeAlreadyPaid=789,removedPaidProductUDegree=du,
 removedPaidProductQDegree=dQ,removedPaidProductTotalDegree=dt,
 exactReducedQQ_uDegree=reduced_degree,
 exactReducedQQ_Q2AndMod1009Degree=reduced_degree,
 reducedMod1009LeadingCoefficient=expected_lc,
 wholeQQMatrixFactorizationReturns=484,
 originalThreeCoordinateClearReturns=original_clear_returns,
 allMatrixDivisionReturns=returns,
 originalDeterminantIdentity="P=product(rowunits)*product(colunits)*det(C)",
 everyRemovedFactorOriginalPhysicalUnit=True,
 allReducedQQCoefficients1009Integral=True,
 finiteFreeRankOverLocalZ1009Q2=reduced_degree,
 wholeH42ZeroRetained=True,noPhysicalDInverse=True,
 noWholePhiExclusionClaim=True)
# Reconstruct only the NEW reduced determinant as actual coefficient
# input to the ensuing finite model. The old determinant proof and
# degree are not used as gates or rerun.
A=[[q2poly(poly) for poly in row] for row in C]
Z=nmod_poly([],p);O=nmod_poly([1],p)
W=[[x+Z for x in row] for row in A]
prev=O;sign=1;bareiss_returns=0;swaps=0
for k in range(n-1):
 prow=next((i for i in range(k,n) if W[i][k]),None)
 if prow is None:
  raise AssertionError("new reduced determinant contradicted already-paid nonzero P")
 if prow!=k:W[k],W[prow]=W[prow],W[k];sign=-sign;swaps+=1
 pivot=W[k][k]
 for i in range(k+1,n):
  entry=W[i][k]
  for j in range(k+1,n):
   num=pivot*W[i][j]-entry*W[k][j]
   q,r=divmod(num,prev);assert not r and q*prev==num
   W[i][j]=q;bareiss_returns+=1
  W[i][k]=Z
 prev=pivot
det=W[-1][-1]*sign
assert int(det.degree())==reduced_degree and int(det[reduced_degree])==expected_lc
fac_constant,factors=det.factor()
product=nmod_poly([int(fac_constant)],p)
for ff,ee in factors:product=product*(ff**int(ee))
assert product==det
def modprofile(poly):
 vals=[int(x) for x in poly.coeffs()]
 return dict(degree=int(poly.degree()),
             sha256=hashlib.sha256(json.dumps(vals,separators=(",",":")).encode()).hexdigest())
head=zero
for ex,c in C6.to_dict().items():
 if ex[2]==6:
  assert not ex[3] and not ex[4]
  head=head+ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):c})
headmod=q2poly(head)
unit_mods=[(label,q2poly(poly)) for label,poly in geo["paid"]]
blocks=[]
for ff,ee in factors:
 ee=int(ee);bad=[]
 for label,atom in unit_mods:
  if int(ff.gcd(atom).degree())>0:bad.append(label)
 hgood=int(ff.gcd(headmod).degree())==0
 blocks.append(dict(factor=modprofile(ff),multiplicity=ee,
                    completeWeightBlockRank=ee*int(ff.degree()),
                    originalWeightNonunitsModuloP=bad,
                    wholeC6HeadIsModUnit=hgood,
                    originalLambdaSixModelEligible=(not bad and hgood)))
blocks.sort(key=lambda x:(x["factor"]["degree"],x["factor"]["sha256"]))
assert sum(b["completeWeightBlockRank"] for b in blocks)==reduced_degree
say("new_reduced_original_modular_coefficient_input_and_complete_blocks",
 prime=p,Q=Q0,actualReducedPolynomial=modprofile(det),
 exactReducedQQ_uDegree=reduced_degree,
 actualModularLeadingCoefficient=expected_lc,
 fixedNew22BareissDivisionReturns=bareiss_returns,rowSwaps=swaps,
 fullFactorizationMultiplicationReturned=True,
 wholePrimaryBlocks=blocks,
 totalCompleteWeightRank=reduced_degree,
 eligibleOriginalLambdaSixWeightRank=sum(b["completeWeightBlockRank"] for b in blocks if b["originalLambdaSixModelEligible"]),
 badOrHeadZeroBlocksRetainedInFull=True,
 noModularFactorIdentifiedAsQQFactor=True,
 noPhysicalUnitDroppedSolelyByModularNonunit=True,
 oldDeterminantOnlyReplacedByNecessaryNewCoefficientInput=True,
 wholeH42ZeroRetained=True,wholePhiExcluded=False,ordinaryISPClaim=False,
 noRecomputableMatrixOrPolynomialPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)

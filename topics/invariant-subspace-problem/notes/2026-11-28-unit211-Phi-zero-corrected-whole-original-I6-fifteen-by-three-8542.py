#!/usr/bin/env python3
"""NEW correct whole Phi: exact original I6 presentation in fifteen columns.
The true first mean head is now globally paid by the COMPLETE A/B theorems.
Regenerate only its known three rules and N1 remainder as definitions.
New inputs: actual T/z actions, both cubic overlaps, full weighted NS/PS
through a same-source multiplication DAG, a stable 15-column presentation,
and two fixed three-column original cofactors.  No module freeness, new
slope inverse, lambda-head inverse, or D inverse.  120 s / 1 GiB.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def bounded_alarm(seconds):
 tick();left=max(1,math.ceil(DEADLINE-time.perf_counter()))
 return RAW_ALARM(left if seconds<=0 else min(int(seconds),left))
signal.alarm=bounded_alarm;signal.alarm(120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
NAME='2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py'
BASE_SHA='5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7'
path=pathlib.Path(__file__).with_name(NAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/NAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
marker='def param(p):'
assert full.count(marker)==1
prefix=full[:full.index(marker)]
assert hashlib.sha256(prefix.encode()).hexdigest()=='dd105b713040712dad7cebeefb489c8e1cf53f56cb5fce8ff0de0bf681d6c669'
env={'__name__':'correct_original_four_polynomial_definitions','__file__':str(path)}
exec(compile(prefix,str(path)+'#definitions_only','exec'),env)
signal.alarm=bounded_alarm;signal.alarm(120)
R=env['R'];ctx=env['ctx'];Z=env['zeroP'];O=env['oneP']
up,Qp,lp,Tp,zp=ctx.gens()
u,Q,lam,T,z=(env[k] for k in ('u','Q','lam','Tr','z'))
ell,m,delta,M,bc,P02,T0,J=(env[k] for k in
 ('ell','m','delta','M','bc','P02','T0','J'))
ff=env['ff'];tt=z/Q;V=env['vn']/Q;W=(T0+4*u*ff)/2
s=u-1;K=Q+4*s;L=Q-2*s*(u-2);Mn=2*u*L-L*L-u*u*Q
Af=4*s*s-Q;Bf=-Q*Q+(12*u*u-20*u+8)*Q-16*s*s
paidSupport=Qp*(1-Qp)*(up-1)*K.n*L.n*Mn.n*Af.n*Bf.n
statistics={'newActionCoordinates':0,'newOverlapOriginalReturns':0,
 'newMatrixDefectCoordinates':0,'newMultiplicationCoordinates':0,
 'newCofactorCoordinates':0,'exactDivisionProducts':0}
def exact(p,g):
 out,rem=divmod(p,g);assert not rem and out*g==p
 statistics['exactDivisionProducts']+=1;return out
def weight(p):return all(not any(ex[2:]) for ex in p.to_dict())
def scalar(p):return all(ex[3]==0 and ex[4]==0 for ex in p.to_dict())
def strip_paid(p):
 out=p;removed=O
 while out and int(out.total_degree())>0:
  g=out.gcd(paidSupport)
  if int(g.total_degree())==0:break
  out=exact(out,g);removed*=g
 assert out*removed==p
 return out,removed
den_seen=set()
def ck(v):
 v=R(v);assert weight(v.d)
 key=str(v.d)
 if key not in den_seen:
  rr,_=strip_paid(v.d);assert rr and int(rr.total_degree())==0
  den_seen.add(key)
 assert scalar(v.n)
 return v
def profile(p):
 data=str(sorted(p.to_dict().items())).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1]*5,
 'terms':len(p.to_dict()),'totalDegree':int(p.total_degree()) if p else -1,
 'sha256':hashlib.sha256(data).hexdigest()}
def rp(v):return {'numerator':profile(v.n),'denominator':profile(v.d)}
def ldegree(v):
 ck(v);return max((int(ex[2]) for ex in v.n.to_dict()),default=-1)
slots=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
def coefficients(value,cap):
 value=R(value);assert weight(value.d);out={}
 for ex,c in value.n.to_dict().items():
  i,j=int(ex[3]),int(ex[4]);assert i+j<=cap
  key=(i,j);small=(ex[0],ex[1],ex[2],0,0)
  out[key]=out.get(key,R())+R(ctx.from_dict({small:c}),value.d)
 return out
forms=[env[k] for k in ('Rbar','W4','Obar','N1')]
quad=[]
for f in forms:
 co=coefficients(f,2);quad.append([co.get(key,R()) for key in slots])
H=[row[3:] for row in quad[:3]]
low=[row[:3] for row in quad[:3]]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),R())
def mv(A,v):return [dot(row,v) for row in A]
def mm(A,B):
 return [[dot(row,[B[k][j] for k in range(len(B))])
          for j in range(len(B[0]))] for row in A]
def adj3(A):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   I=[r for r in range(3) if r!=j];Jj=[c for c in range(3) if c!=i]
   row.append((-1)**(i+j)*(A[I[0]][Jj[0]]*A[I[1]][Jj[1]]
                         -A[I[0]][Jj[1]]*A[I[1]][Jj[0]]))
  out.append(row)
 return out
# Known f62/fd9 parameter definitions, with the NEW whole-B payment.
# No old head factorization, original-rule proof, or slope gate is executed.
head=Mn**3*L**4*Af*Bf/(8*K**3*delta**4)
inv=[[v/head for v in row] for row in adj3(H)]
rules=[[-v for v in row] for row in mm(inv,low)]
ntrace=[sum((quad[3][3+i]*inv[i][j] for i in range(3)),R()) for j in range(3)]
rN=[quad[3][j]+sum((quad[3][3+i]*rules[i][j] for i in range(3)),R())
    for j in range(3)]
for row in rules+inv:
 for v in row:ck(v)
for v in rN+ntrace:ck(v)
I=[[R(int(i==j)) for j in range(3)] for i in range(3)]
basis=[R(1),T,z]
MT=[[R(int(i==1)),rules[0][i],rules[1][i]] for i in range(3)]
MZ=[[R(int(i==2)),rules[1][i],rules[2][i]] for i in range(3)]
# New action columns, compared to their exact six-coordinate product rule.
def product_coefficients(a,b):
 lo=[a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[2]*b[0]]
 hi=[a[1]*b[1],a[1]*b[2]+a[2]*b[1],a[2]*b[2]]
 out=[lo[j]+sum((hi[k]*rules[k][j] for k in range(3)),R()) for j in range(3)]
 return out,hi
for matrix,e in [(MT,[R(),R(1),R()]),(MZ,[R(),R(),R(1)])]:
 for j in range(3):
  out,_=product_coefficients(e,[R(int(i==j)) for i in range(3)])
  assert out==[matrix[i][j] for i in range(3)]
  statistics['newActionCoordinates']+=3
AB=mm(MT,MZ);BA=mm(MZ,MT)
comm=[[AB[i][j]-BA[i][j] for j in range(3)] for i in range(3)]
assert all(not comm[i][0] for i in range(3))
c1=[comm[i][1] for i in range(3)];c2=[comm[i][2] for i in range(3)]
# Actual original overlaps: z*fTT-T*fTZ and z*fTZ-T*fZZ.
# These signs give c1 and c2 AFTER the indicated rule reduction.
normalized=[T*T-dot(rules[0],basis),T*z-dot(rules[1],basis),
            z*z-dot(rules[2],basis)]
eT=[R(),R(1),R()];eZ=[R(),R(),R(1)]
for left,right,target,base_tag in [
 (rules[1],rules[0],c1,[z,-T,R()]),
 (rules[2],rules[1],c2,[R(),z,-T])]:
 outT,hiT=product_coefficients(eT,left)
 outZ,hiZ=product_coefficients(eZ,right)
 hi=[hiT[j]-hiZ[j] for j in range(3)]
 tag=[base_tag[j]-hi[j] for j in range(3)]
 assert dot(tag,normalized)==dot(target,basis)
 assert [outT[j]-outZ[j] for j in range(3)]==target
 statistics['newOverlapOriginalReturns']+=1
# Four exact matrix defects imply closure after ONE action layer.
AA=mm(MT,MT);BB=mm(MZ,MZ)
for actual,rule,target,column in [
 (AA,rules[0],c1,2),(BB,rules[2],[-v for v in c2],1),
 (AB,rules[1],c2,2),(BA,rules[1],[-v for v in c1],1)]:
 for i in range(3):
  for j in range(3):
   diff=actual[i][j]-rule[0]*I[i][j]-rule[1]*MT[i][j]-rule[2]*MZ[i][j]
   assert diff==(target[i] if j==column else R())
   statistics['newMatrixDefectCoordinates']+=1
say('new_correct_whole_Phi_T_z_actions_and_original_overlaps',
 oldCorrectFourPolynomialSourceSHA256=BASE_SHA,
 necessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 wholeAAndBOriginalExclusionsUsed=True,noOldSlopeGateReplayed=True,
 trueFirstMeanHead='Mn^3*L^4*A*B/(8*K^3*delta^4)',
 allEighteenActionCoordinatesReturned=True,
 bothFullOriginalOverlapIdentitiesReturned=True,
 allThirtySixMatrixDefectCoordinatesReturned=True,
 reducedN1LambdaDegrees=[ldegree(v) for v in rN],
 commutatorLambdaDegrees=[[ldegree(v) for v in row] for row in (c1,c2)],
 noFreenessOrAssociativityOfThreeCoefficientVectorsAssumed=True,
 wholeSlopeZeroLocusKept=True)
# Same-source DAG: every binary product retains its six raw coefficients.
# out = lo + hi*rules, so raw(v)*raw(w)-raw(out) =
# sum hi_i*(monomial_i-rules_i.basis), plus the two parent original errors.
# The independent action route returns all THREE output coefficients.
# Keep only the operation graph, not a large coefficient-history cache;
# every local hi coefficient is determined from its two actual operands.
nodes=[]
class A:
 def __init__(self,vec,op='input',parents=(),payload=None):
  self.v=[R(v) for v in vec];assert len(self.v)==3
  self.id=len(nodes);nodes.append((op,tuple(parents)))
 @staticmethod
 def scalar(value):
  value=R(value);assert scalar(value.n) and weight(value.d)
  return A([value,R(),R()],'scalar')
 @staticmethod
 def affine(value,label):
  co=coefficients(value,1)
  return A([co.get((0,0),R()),co.get((1,0),R()),co.get((0,1),R())],label)
 def __add__(self,other):
  other=other if isinstance(other,A) else A.scalar(other)
  return A([self.v[i]+other.v[i] for i in range(3)],'add',(self.id,other.id))
 __radd__=__add__
 def __neg__(self):return A([-v for v in self.v],'neg',(self.id,))
 def __sub__(self,other):return self+-other if isinstance(other,A) else self+-A.scalar(other)
 def scale(self,co):
  co=R(co);assert scalar(co.n) and weight(co.d)
  return A([v*co for v in self.v],'scale',(self.id,),co)
 def __mul__(self,other):
  tick();other=other if isinstance(other,A) else A.scalar(other)
  out,hi=product_coefficients(self.v,other.v)
  at=mv(MT,other.v);az=mv(MZ,other.v)
  via=[self.v[0]*other.v[i]+self.v[1]*at[i]+self.v[2]*az[i] for i in range(3)]
  assert out==via
  statistics['newMultiplicationCoordinates']+=3
  return A(out,'product',(self.id,other.id),hi)
 def iszero(self):return all(not v for v in self.v)
def a(value,label='affine_input'):
 return value if isinstance(value,A) else A.affine(value,label)
def E(c=0,d=0):return [a(c),a(d)]
def ea(v,w):return [v[i]+w[i] for i in range(2)]
def en(v):return [-v[0],-v[1]]
def es(v,w):return ea(v,en(w))
def ec(v,co):
 if isinstance(co,A):return [v[0]*co,v[1]*co]
 return [v[0].scale(co),v[1].scale(co)]
def em(v,w):
 return [v[0]*w[0]+(v[1]*w[1]).scale(delta),v[0]*w[1]+v[1]*w[0]]
def conj(v):return [v[0],-v[1]]
def esm(*vs):
 out=E()
 for v in vs:out=ea(out,v)
 return out
aw=1-ell;theta=u-ell*Q
A1=2*ff-2*V+2*bc*tt
xx=(theta*V-m*W)/M;yy=(ell*W-u*V)/M
b=E(ell/2,m/(2*delta));c=conj(b)
p=E(1,1);q=conj(p)
X=E(xx,yy);Y=conj(X)
tA=a(tt,'original_t');fA=a(ff,'original_f')
rr=es(es(X,ec(p,aw)),ec(c,tA));ss=conj(rr)
rows=[[E(),E(),p,q],[E(),E(A1),rr,ss],
      [p,rr,E(),E(tt)],[q,ss,E(tt),E()]]
unit=[E(1),E(),E(1),E(1)]
def vm(v,w):
 return [em(v[0],w[0]),ea(em(v[0],w[1]),em(v[1],w[0])),
         em(v[2],w[2]),em(v[3],w[3])]
def va(v,w):return [ea(c0,c1) for c0,c1 in zip(v,w)]
def vs(v,w):return [em(v,c0) for c0 in w]
def tau(v):return esm(ec(v[0],aw),v[1],em(b,v[2]),em(c,v[3]))
def DK(v):return [tau(vm(row,v)) for row in rows]
# These are the direct original row means, no old full-value audit.
dv=[E(u),E(2*ff-V-aw*u),X,Y]
F2=E(2*ff)
def N4(v):
 tv=tau(v);vv=vm(v,v)
 return esm(ec(tau(vm(dv,vv)),2),en(em(F2,tau(vv))),
  ec(em(tv,tau(vm(dv,v))),-4),ec(em(F2,em(tv,tv)),2),tau(vm(v,DK(v))))
def centered(v):return va(v,vs(en(tau(v)),unit))
def P2(v):
 cv=centered(v);return tau(vm(vm(cv,cv),cv))
A2=2*lam*lam-2*lam+1
B3=4*lam**3-6*lam*lam+3*lam-1
NS=es(esm(em(b,N4(rows[2])),em(c,N4(rows[3]))),
      E(2*lam*P02*(ell+2*T+A2)))
assert NS[1].iszero()
rNS=NS[0].v
for i,v in enumerate(rNS):ck(v);assert ldegree(v)<=3-(i>0)
say('new_correct_whole_Phi_full_original_NS_three_coefficients',
 coefficientProfiles=[rp(v) for v in rNS],
 lambdaDegrees=[ldegree(v) for v in rNS],
 sameRawDualGramAndSameParenthesizedOriginalN4=True,
 multiplicationDAGNodes=len(nodes),
 fullSixOriginalTraceExpansionNotRepeated=True)
PS=es(esm(em(b,P2(rows[2])),em(c,P2(rows[3]))),
      E(P02*(ell+3*T+3*A2+B3)))
assert PS[1].iszero()
rPS=PS[0].v
for i,v in enumerate(rPS):ck(v);assert ldegree(v)<=3-(i>0)
say('new_correct_whole_Phi_full_original_PS_three_coefficients',
 coefficientProfiles=[rp(v) for v in rPS],
 lambdaDegrees=[ldegree(v) for v in rPS],
 sameRawDualGramAndSameCenteredCubic=True,
 multiplicationDAGNodes=len(nodes))
seeds=[rN,rNS,rPS,c1,c2]
names=['N1','NS','PS','comm_T','comm_z']
relations=[]
for name,g in zip(names,seeds):
 for action,mat in [('one',I),('T',MT),('z',MZ)]:
  vec=mv(mat,g)
  for v in vec:ck(v)
  relations.append((name,action,vec))
say('new_correct_whole_Phi_exact_fifteen_by_three_original_I6',
 seedNames=names,relationCount=15,
 relationLambdaDegrees=[[name,action,[ldegree(v) for v in vec]]
                       for name,action,vec in relations],
 exactPresentation='coker of G,MT*G,MZ*G over paid-weight-ring[lambda]',
 oneActionClosureProvedByFourReturnedMatrixDefects=True,
 e0CyclicAndAllCommutatorColumnsKilled=True,
 fullOriginalI6NotOnlySamePointNecessaryRows=True,
 noFreenessAssumption=True,noLambdaLeadingCoefficientInverted=True,
 wholeOriginalSlopeZeroLocusIncluded=True,
 multiplicationDAGNodes=len(nodes))
# Two NEW original cofactors.  Only all three actual scalar multipliers'
# common numerator is canceled, followed by all three coefficient returns.
def original_cofactor(label,chosen):
 row=[seeds[i] for i in chosen]
 mu=[row[1][1]*row[2][2]-row[1][2]*row[2][1],
     row[2][1]*row[0][2]-row[2][2]*row[0][1],
     row[0][1]*row[1][2]-row[0][2]*row[1][1]]
 if not any(mu):
  say('new_correct_three_column_original_cofactor_zero',
      label=label,noPureWeightOrLambdaConclusion=True)
  return
 den=O
 for v in mu:ck(v);den=exact(den,den.gcd(v.d))*v.d
 common=Z;nums=[v.n*exact(den,v.d) for v in mu]
 for p0 in nums:common=common.gcd(p0)
 assert common
 primitive=[R(exact(v,common)) for v in nums]
 returned=[sum((primitive[i]*row[i][j] for i in range(3)),R()) for j in range(3)]
 assert not returned[1] and not returned[2]
 statistics['newCofactorCoordinates']+=3
 C=ck(returned[0]);core,removed=strip_paid(C.n)
 if core:
  lc=core.coefficient(0);core/=lc;removed*=lc
 assert core*removed==C.n
 degree=max((int(ex[2]) for ex in core.to_dict()),default=-1)
 leading=ctx.from_dict({(ex[0],ex[1],0,0,0):v
    for ex,v in core.to_dict().items() if int(ex[2])==degree}) if core else Z
 say('new_correct_three_column_original_cofactor_complete',
  label=label,originalRows=[names[i] for i in chosen],
  actualThreeMultiplierCommon=profile(common),
  originalScalarNumerator=profile(C.n),originalScalarDenominator=profile(C.d),
  allThreeOriginalModuleCoordinatesReturned=True,
  retainedNecessaryLambdaWeightPolynomial=profile(core),
  lambdaDegree=degree,actualLambdaLeadingNumerator=profile(leading),
  allMultiplierCommonZeroFibersKept=True,
  onlyWholeCurrentPhiPaidWeightSupportsRemoved=True,
  allLambdaLeadingZeroFibersKept=True,
  wholePhiExcluded=bool(core) and int(core.total_degree())==0)
original_cofactor('new_full_weighted_NP_with_N1',[0,1,2])
original_cofactor('new_two_original_overlaps_with_N1',[0,3,4])
say('new_correct_whole_Phi_original_fifteen_column_input_complete',
 statistics=statistics,multiplicationDAGNodes=len(nodes),
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 noOldWrongCompactSourceOrOldSlopeGateReplayed=True,
 noDOrItsNormInverse=True,noCoefficientPayloadOrChunksSaved=True,
 ordinaryISPClaim=False,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

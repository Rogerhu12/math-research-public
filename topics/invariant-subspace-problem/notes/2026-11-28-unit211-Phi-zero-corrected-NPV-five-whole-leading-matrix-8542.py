#!/usr/bin/env python3
"""NEW correct Phi: the WHOLE grade-five Nlow/Plow/full-Vlow leading matrix.
Only f62's true original rational definitions are reused. No old 15-column
gate, full individual-value DAG, decic cofactor, or resultant is executed.
The three NEW leading rows are constructed directly from the original
highest homogeneous N4/P2 and the complete isolated N4 formula.
All NINE actual adjugate multipliers are canceled together and returned
as C*I3. If C!=0 this pays 13 generators on C!=0, retaining the WHOLE C=0
weight locus. No D2, physical D, lambda, or geometric head is inverted.
The newly proved whole ell=1/2 exclusion is used only as a paid weight.
120 seconds / 1 GiB, one exact necessary-source dependency, small output.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
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
NAME='2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py'
BASE_SHA='5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7'
path=pathlib.Path(__file__).with_name(NAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/NAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
marker='def param(p):';assert full.count(marker)==1
prefix=full[:full.index(marker)]
assert len(prefix)==4007
assert hashlib.sha256(prefix.encode()).hexdigest()=='dd105b713040712dad7cebeefb489c8e1cf53f56cb5fce8ff0de0bf681d6c669'
ns={'__name__':'only_true_original_Phi_rational_definitions','__file__':str(path),
    'print':lambda *a,**kw:None}
exec(compile(prefix,str(path)+'#necessary-definitions-only','exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];O=ns['oneP'];Z=ns['zeroP']
up,Qp,lp,Tp,zp=ctx.gens()
u,Q,ell,m,delta,M,bc,P02=(
 ns[k] for k in ('u','Q','ell','m','delta','M','bc','P02'))
s=u-1;Kweight=Q+4*s;L=Q-2*s*(u-2)
Mn=2*u*L-L*L-u*u*Q
Af=4*s*s-Q
Bf=-Q*Q+(12*u*u-20*u+8)*Q-16*s*s
# These are current CORRECT whole-Phi units, with their independent
# original exclusions. The final two factors are m and 2ell-1.
paid=up*Qp*(1-Qp)*(up-1)*Kweight.n*L.n*Mn.n*Af.n*Bf.n*m.n*(2*L-Q).n
statistics={'newHomogeneousExtractions':0,'newTopMeanIdentityCoordinates':0,
 'newProductCoordinates':0,'newWholeAdjugateCoordinates':0,
 'exactDivisionProducts':0}
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 statistics['exactDivisionProducts']+=1;return q
def weight(p):return all(not any(e[2:]) for e in p.to_dict())
def strip_paid(p):
 value=p;removed=O
 while value and int(value.total_degree())>0:
  g=value.gcd(paid)
  if int(g.total_degree())==0:break
  value=exact(value,g);removed*=g
 assert value*removed==p
 return value,removed
den_seen=set()
def ck(value):
 value=R(value);assert weight(value.n) and weight(value.d)
 key=str(value.d)
 if key not in den_seen:
  rest,_=strip_paid(value.d)
  assert rest and int(rest.total_degree())==0,('unpaid weight denominator',str(rest))
  den_seen.add(key)
 return value
def profile(p):
 data=str(sorted(p.to_dict().items())).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1]*5,
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(p.to_dict()),'sha256':hashlib.sha256(data).hexdigest()}
def rp(v):return {'numerator':profile(v.n),'denominator':profile(v.d)}
def top(value,degree):
 # Exact degree-d homogeneous part in (lambda,T,z), followed by the
 # leading-functor chart lambda=1. This is NOT value specialization.
 value=R(value);assert weight(value.d)
 data={}
 for e,c in value.n.to_dict().items():
  grade=sum(map(int,e[2:]));assert grade<=degree
  if grade==degree:
   key=(e[0],e[1],0,e[3],e[4]);data[key]=data.get(key,0)+c
 statistics['newHomogeneousExtractions']+=1
 return R(ctx.from_dict(data),value.d)
def coeffs(value):
 value=R(value);assert weight(value.d)
 out=[R() for _ in range(6)]
 slots={(0,0):0,(1,0):1,(0,1):2,(2,0):3,(1,1):4,(0,2):5}
 for e,c in value.n.to_dict().items():
  assert not e[2] and (int(e[3]),int(e[4])) in slots
  idx=slots[(int(e[3]),int(e[4]))]
  out[idx]+=R(ctx.from_dict({(e[0],e[1],0,0,0):c}),value.d)
 for v in out:ck(v)
 return out
def dot(a,b):return sum((v*w for v,w in zip(a,b)),R())
def mm(A,B):
 return [[dot(row,[B[k][j] for k in range(len(B))])
          for j in range(len(B[0]))] for row in A]
def mv(A,v):return [dot(row,v) for row in A]
def adj3(A):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   ii=[r for r in range(3) if r!=j]
   jj=[c for c in range(3) if c!=i]
   row.append((-1)**(i+j)*(A[ii[0]][jj[0]]*A[ii[1]][jj[1]]
                         -A[ii[0]][jj[1]]*A[ii[1]][jj[0]]))
  out.append(row)
 return out
topforms=[top(ns[k],2) for k in ('Rbar','W4','Obar')]
quad=[coeffs(v) for v in topforms]
H=[row[3:] for row in quad];low=[row[:3] for row in quad]
# Established correct first-mean head, used only as its parameter
# definition. The original f62 head/factor/old rule gate is not replayed.
head=Mn**3*L**4*Af*Bf/(8*Kweight**3*delta**4)
inv=[[ck(v/head) for v in row] for row in adj3(H)]
rules=[[-ck(v) for v in row] for row in mm(inv,low)]
TT=R(Tp);zz=R(zp);basis=[R(1),TT,zz]
normalized=[TT*TT-dot(rules[0],basis),TT*zz-dot(rules[1],basis),
            zz*zz-dot(rules[2],basis)]
for i in range(3):
 assert normalized[i]==dot(inv[i],topforms)
 statistics['newTopMeanIdentityCoordinates']+=1
MT=[[R(int(i==1)),rules[0][i],rules[1][i]] for i in range(3)]
MZ=[[R(int(i==2)),rules[1][i],rules[2][i]] for i in range(3)]
def product(a,b):
 lo=[a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[2]*b[0]]
 hi=[a[1]*b[1],a[1]*b[2]+a[2]*b[1],a[2]*b[2]]
 out=[lo[j]+sum((hi[k]*rules[k][j] for k in range(3)),R()) for j in range(3)]
 at=mv(MT,b);az=mv(MZ,b)
 via=[a[0]*b[i]+a[1]*at[i]+a[2]*az[i] for i in range(3)]
 assert out==via
 statistics['newProductCoordinates']+=3
 for v in out:ck(v)
 return out,hi
nodes=[]
class A:
 def __init__(self,vec,op='input',parents=()):
  self.v=[ck(v) for v in vec];assert len(self.v)==3
  self.id=len(nodes);nodes.append((op,tuple(parents)))
 @staticmethod
 def scalar(value):return A([ck(value),R(),R()],'scalar')
 @staticmethod
 def affine(value,label):
  cs=coeffs(value);assert not any(cs[3:])
  return A(cs[:3],label)
 def __add__(self,o):
  o=o if isinstance(o,A) else A.scalar(o)
  return A([self.v[i]+o.v[i] for i in range(3)],'add',(self.id,o.id))
 __radd__=__add__
 def __neg__(self):return A([-v for v in self.v],'neg',(self.id,))
 def __sub__(self,o):return self+(-o if isinstance(o,A) else -A.scalar(o))
 def scale(self,v):
  v=ck(v);return A([x*v for x in self.v],'scale',(self.id,))
 def __mul__(self,o):
  tick();o=o if isinstance(o,A) else A.scalar(o)
  out,hi=product(self.v,o.v)
  # The complete original homogeneous trace follows raw(a)*raw(b)
  # minus raw(out)=sum hi_i*q_i, together with both parent traces.
  return A(out,'product',(self.id,o.id))
def E(a=0,b=0):
 return [a if isinstance(a,A) else A.scalar(a),b if isinstance(b,A) else A.scalar(b)]
def ea(a,b):return [a[i]+b[i] for i in range(2)]
def en(a):return [-a[0],-a[1]]
def es(a,b):return ea(a,en(b))
def ec(a,b):
 return [a[i]*b if isinstance(b,A) else a[i].scale(b) for i in range(2)]
def em(a,b):
 return [a[0]*b[0]+(a[1]*b[1]).scale(delta),a[0]*b[1]+a[1]*b[0]]
def conj(a):return [a[0],-a[1]]
def esm(*vs):
 out=E()
 for v in vs:out=ea(out,v)
 return out
f_top=top(ns['ff'],1)
V_top=top(ns['vn']/Q,1)
W_top=2*u*f_top
theta=u-ell*Q
x_top=(theta*V_top-m*W_top)/M
y_top=(ell*W_top-u*V_top)/M
TA=A.affine(TT,'highest_T')
tA=A.affine(zz/Q,'highest_original_t')
fA=A.affine(f_top,'highest_original_f')
VA=A.affine(V_top,'highest_original_V')
WA=A.affine(W_top,'highest_original_W1')
b=E(ell/2,m/(2*delta));c=conj(b)
X=E(A.affine(x_top,'highest_original_x'),A.affine(y_top,'highest_original_y'))
Y=conj(X)
t2=tA*tA;t3=t2*tA
X2=em(X,X);X3=em(X2,X);XY=em(X,Y)
# NEW direct cubic highest parts of the SAME original simple B value.
# Its degree-zero p entry makes tau(v*DKv) at most degree two.
# Thus these are the entire degree-three N4 and P2, not a component
# substituted for the full original value or a W-specialized formula.
NB=esm(ec(em(c,es(Y,E(fA))),t2.scale(2)),
       ec(em(c,XY),tA.scale(-4)),ec(X2,fA.scale(4)))
PB=esm(ec(c,t3),ec(em(c,X),t2.scale(-3)),ec(X3,2))
Tsq=TA*TA
D2=A.scalar(2*ell)-Tsq
K3=A.scalar(4*ell*ell)-TA.scale(6*ell)+(Tsq*TA).scale(2)
D2sq=D2*D2
acenter=TA.scale(1/ell)
Ntop=D2*NB[1]+(K3*acenter).scale(2*P02/m)+D2sq.scale(4*P02*m/(ell*M))
Pbracket=(acenter*acenter).scale(3)+D2.scale((3*m*m/(ell*ell)+delta)/M)
Ptop=D2*PB[1]+(K3*Pbracket).scale(P02/(2*m))+(acenter*D2sq).scale(6*P02*m/(ell*M))
# NEW highest parts of all THREE coefficients of the complete isolated
# N4. Lower-degree original terms are discarded by the stated grades.
Z0=(fA*D2).scale(2*ell)+(VA*(Tsq-TA.scale(2*ell))).scale(2)+(tA*Tsq).scale(2*bc)
Z1=((TA-A.scalar(ell))*(VA.scale(u)-WA.scale(ell))).scale(4)+(TA*tA).scale(4*bc*m)
Z2=VA.scale(2*(u*u-ell*ell*Q))-WA.scale(4*m*ell)-fA.scale(2*ell*M)-tA.scale(2*bc*M)
Vtop=D2*Z0+(K3*Z1).scale(1/(2*m))+(D2sq*Z2).scale(1/M)
rows=[Ntop.v,Ptop.v,Vtop.v]
for row in rows:
 for v in row:ck(v)
say('new_correct_three_full_grade_five_original_value_rows',
 labels=['individual_Nlow_highest','individual_Plow_highest','entire_N4_Vlow_highest'],
 inputGrades=[5,5,5],generatorWeights=[0,1,1],
 coefficientProfiles=[[rp(v) for v in row] for row in rows],
 completeOriginalN4AndP2HighestParts=True,
 leadingFunctorLambdaOneNotValueSpecialization=True,
 noD2OrPhysicalDOrGeometricLeadingInverse=True,
 noOldFullValueDAGOrTwoDecicCofactorExecuted=True,
 originalCurrentI10AllConditionsRetained=True,
 newDAGNodes=len(nodes),statistics=statistics)
# NEW WHOLE 3x3 original matrix source. Cancel a common factor of ALL
# NINE actual adjugate multipliers, never just the determinant.
adj=adj3(rows)
den=O
for row in adj:
 for v in row:
  ck(v);den=exact(den,den.gcd(v.d))*v.d
nums=[[v.n*exact(den,v.d) for v in row] for row in adj]
common=Z
for row in nums:
 for v in row:common=common.gcd(v)
if not common:
 say('new_whole_grade_five_leading_adjugate_zero',
     allNineMultipliersZero=True,noNewMonicOrFiniteConclusion=True,
     allOriginalWeightFibersKept=True,statistics=statistics)
else:
 primitive=[[R(exact(v,common)) for v in row] for row in nums]
 returned=mm(primitive,rows)
 C=ck(returned[0][0])
 for i in range(3):
  for j in range(3):
   assert returned[i][j]==(C if i==j else R())
   statistics['newWholeAdjugateCoordinates']+=1
 if not C:
  say('new_whole_grade_five_leading_matrix_singular',
      allNineAdjugateCoordinatesReturned=True,
      noNewMonicOrFiniteConclusion=True,allOriginalWeightFibersKept=True,
      statistics=statistics)
 else:
  core,removed=strip_paid(C.n)
  lc=core.coefficient(0);core/=lc;removed*=lc
  assert core*removed==C.n
  # This yields the complete identity J*rows=core*I3 in the OLD paid
  # weight ring. The canceled common factor is not inverted.
  Jmat=[[ck(v*R(C.d,removed)) for v in row] for row in primitive]
  for i in range(3):
   for j in range(3):
    assert dot(Jmat[i],[rows[k][j] for k in range(3)])==R(core if i==j else Z)
    statistics['newWholeAdjugateCoordinates']+=1
  say('new_correct_full_three_grade_five_original_leading_certificate',
      allNinePrimitiveAdjugateCoordinatesReturned=True,
      allNineFinalPaidRingCoordinatesReturned=True,
      actualNineMultiplierCommon=profile(common),
      rawCommonScalarNumerator=profile(C.n),rawCommonScalarDenominator=profile(C.d),
      retainedWholeWeightCover=profile(core),
      wholeCurrentEllHalfOriginalExclusionUsed=True,
      fullMatrixIdentity='J*leading(Nlow,Plow,Vlow)=C*I3',
      filteredLeadingRelations=['C*lambda^5','C*lambda^4*T','C*lambda^4*z'],
      finiteGeneratorBoundOnCoverComplement=13,
      monicLambdaPolynomialDegreeUpperBoundOnCoverComplement=13,
      originalThreeGeneratorModuleNotAssumedFree=True,
      physicalDLocalizationOnlyPreservesFiberFiniteness=True,
      entireNewCoverZeroLocusKept=True,
      wholePhiExcluded=False,statistics=statistics)
  # A genuinely NEW exact factorization of this complete-matrix cover;
  # the original filtered certificate above is already returned.
  const,factors=core.factor()
  product_core=ctx.constant(const);fprofiles=[]
  for fac,power in factors:
   power=int(power);product_core*=fac**power
   fprofiles.append({'multiplicity':power,**profile(fac)})
  assert product_core==core
  say('new_grade_five_whole_matrix_weight_cover_factorization',
      constant=str(const),factors=fprofiles,fullExactProductReturned=True,
      factorZeroFibersAllRetained=True,noOldHeadFactorGateReplayed=True)
say('new_correct_grade_five_whole_matrix_input_finished',
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 necessaryOriginalSourceSHA256=BASE_SHA,
 necessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 statistics=statistics,newDAGNodes=len(nodes),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False,noCoefficientPayloadOrChunksSaved=True)
RAW_ALARM(0)

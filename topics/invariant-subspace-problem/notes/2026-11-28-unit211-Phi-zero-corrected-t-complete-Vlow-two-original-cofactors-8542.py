#!/usr/bin/env python3
"""NEW complete isolated N4 in the corrected whole t-parameter model.
Only necessary true mean/N1/NS/PS coefficient definitions are regenerated.
Transport the COMPLETE Z0/Z1/Z2 identity to the original (t,f,V) variables.
Return the new total-degree-five Vlow against all three original means.
Then form ONLY the two new three-row cofactors (N1,NS,Vlow) and
(N1,PS,Vlow); cancel all THREE actual multipliers and return all coordinates.
No old centered model, global t sextic, H28, factor, or weighted pair gate.
No D inverse, no slope inverse, no head inverse beyond old paid mean head.
Self-contained, zero dependencies. Absolute 120 seconds / 1 GiB.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120-second boundary')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','t','f','V'),'lex')
up,Qp,tp,fp,Vp=ctx.gens();O=ctx.constant(1);Z=ctx.constant(0)
def polynomial(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=polynomial(n);d=O if d is None else polynomial(d);assert d
  if not n:self.n=Z;self.d=O;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=R(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=self.d/g;b=v.d/g
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R((self.n/g)*(v.n/h),(self.d/h)*(v.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);assert v
  return self*R(v.d,v.n,False)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return R(self.n**n,self.d**n,False)
 def __eq__(self,v):
  v=R(v);return self.n*v.d==v.n*self.d

u,Q,t,f,V=map(R,(up,Qp,tp,fp,Vp))
s=u-1;delta=1-Q;L=Q-2*s*(u-2);ell=L/Q;m=u-ell
T0=2*u-ell*Q-2*u*u;J=2*u*(1-u)+ell*Q
P02=2*s*ell*Q;Pf=T0*(J-Q)
M=ell*(2*u-ell*Q)-u*u;bc=M/(4*delta)
Kw=Q+4*s;Mn=Q*M;gg=2*ell-1
lam=(J*f-Q*V+bc*Q*t-s*T0)/P02
T=-ell+T0*(f-V+bc*t)/P02;w=lam-1-T
W1=T0/2+2*u*f;theta=u-ell*Q
x=(theta*V-m*W1)/M;y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t
statistics={'exactDivisionProducts':0,'parameterReductionSteps':0,
 'newVlowReductionSteps':0,'newVlowRawMeanReturns':0,
 'newVlowCoordinates':0,'newFixedCofactorCoordinates':0,
 'newOriginalScalarSupportReturns':0}
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 statistics['exactDivisionProducts']+=1;return q
def weight(p):return all(not any(map(int,ex[2:])) for ex in p.to_dict())
def scalar(p):return all(not any(map(int,ex[3:])) for ex in p.to_dict())
paid=up*Qp*(1-Qp)*(up-1)*Kw.n*L.n*Mn.n*gg.n*m.n
def strip(p,support=None):
 support=paid if support is None else support
 original=p;removed=O
 while p and int(p.total_degree())>0:
  q=p.gcd(support)
  if int(q.total_degree())==0:break
  p=exact(p,q);removed*=q
 assert p*removed==original
 return p,removed
def checkden(v,support=None):
 v=R(v);assert weight(v.d)
 rr,_=strip(v.d,support)
 assert rr and int(rr.total_degree())==0,('unpaid denominator',str(rr))
 return v
def ck(v):
 v=checkden(v);assert scalar(v.n);return v
def td(v,support=None):
 v=checkden(v,support);assert scalar(v.n)
 return max((int(ex[2]) for ex in v.n.to_dict()),default=-1)
def profile(p):
 raw=str(sorted(p.to_dict().items())).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1]*5,
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(p.to_dict()),'sha256':hashlib.sha256(raw).hexdigest()}
def rp(v):return {'numerator':profile(v.n),'denominator':profile(v.d)}
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,v):
  v=E(v);return E(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):
  v=E(v);return E(self.a*v.a+delta*self.b*v.b,self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);return E(self.a/v,self.b/v)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,v):
  v=E(v);return self.a==v.a and self.b==v.b
 def conj(self):return E(self.a,-self.b)

# Necessary original Gram definitions, with true dual multiplication.
b=E(ell/2,m/(2*delta));c=b.conj();aw=E(1-ell)
p=E(1,1);q=p.conj();X=E(x,y);Y=X.conj()
r=X-aw*p-c*E(t);ss=Y-aw*q-b*E(t)
rows=[[E(),E(),p,q],[E(),E(A1),r,ss],
      [p,r,E(),E(t)],[q,ss,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,w):return [v[i]+w[i] for i in range(4)]
def vs(a,v):return [a*x for x in v]
def vm(v,w):
 return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tr(v):return aw*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tr(vm(row,v)) for row in rows]
d=DK(one);F2=tr(d);Kd=DK(d)
def mean(j):
 sq=2*tr(vm(rows[0],rows[1])) if j==1 else tr(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
EB=mean(2)
Rcal=4*(f-u)*(V-f)+bc*t*t+t*(4*bc*u-ell*V+m*(T0+4*u*f-2*V)/(2*delta))
forms=[Rcal,EB.a,EB.b]
slots=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
def coeffs(value,cap=3):
 value=checkden(value);groups={}
 for ex,cc in value.n.to_dict().items():
  key=(int(ex[3]),int(ex[4]));assert sum(key)<=cap
  groups.setdefault(key,{})[(ex[0],ex[1],ex[2],0,0)]=cc
 return {key:R(ctx.from_dict(group),value.d) for key,group in groups.items()}
def six(value):
 co=coeffs(value,2);return [co.get(k,R()) for k in slots]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),R())
def adj3(A):
 out=[]
 for i in range(3):
  row=[]
  for j in range(3):
   ii=[r for r in range(3) if r!=j];jj=[c for c in range(3) if c!=i]
   row.append((-1)**(i+j)*(A[ii[0]][jj[0]]*A[ii[1]][jj[1]]
                         -A[ii[0]][jj[1]]*A[ii[1]][jj[0]]))
  out.append(row)
 return out
quad=[six(value) for value in forms]
H=[row[3:] for row in quad];low=[row[:3] for row in quad]
# Already proved whole paid determinant: necessary coefficient definition.
head=32*u*Q*gg/(M*M)
inv=[[v/head for v in row] for row in adj3(H)]
rules=[[-sum((inv[i][k]*low[k][j] for k in range(3)),R())
        for j in range(3)] for i in range(3)]
basis=[R(1),f,V]
def N4(v):
 vv=vm(v,v);tv=tr(v)
 return 2*tr(vm(d,vv))-F2*tr(vv)-4*tv*tr(vm(d,v))+2*F2*tv*tv+tr(vm(v,DK(v)))
def centered(v):return va(v,vs(-tr(v),one))
def P2(v):
 cv=centered(v);return tr(vm(vm(cv,cv),cv))
# Only the existing N1 coefficient definition is regenerated, not its
# old full proof gate, CH, slope factorization or six-row construction.
v0,v1=rows[0],rows[1]
N1=(N4(va(v0,v1))-N4(v0)-N4(v1)-E(4*lam*w*P02)).a
nq=six(N1)
rN=[nq[j]+sum((nq[3+i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
expectedN1=['84bdde216e7db3b309cee64f2b85445f07a38d1b76ecf2ef42af809e87101554',
 'eb53d324557d81df4535bdbbd89db877f1f09ff3c96cae2a889505336b35f4ca',
 '9d248069282c53e60dd5f33ae6afb26ff391988dfc306852a4bba261497743dd']
assert [profile(v.n)['sha256'] for v in rN]==expectedN1
# Necessary complete original cubic definitions; no old return gate below.
A2=2*lam*lam-2*lam+1
B3=4*lam**3-6*lam*lam+3*lam-1
NB=N4(rows[2]);PB=P2(rows[2])
# Conjugation sends the complete original B row and all physical
# coefficients to the C row, including DK and the centered cubic.
NSe=b*NB+c*NB.conj()-E(2*lam*P02*(ell+2*T+A2))
PSe=b*PB+c*PB.conj()-E(P02*(ell+3*T+3*A2+B3))
assert not NSe.b and not PSe.b
raw_values=[NSe.a,PSe.a]
for value in raw_values:
 checkden(value)
 assert max((sum(map(int,ex[2:])) for ex in value.n.to_dict()),default=-1)<=3


# Necessary deterministic coefficient/trace definitions only.
# Their prior separate ordinary-return gates are intentionally omitted.
def reduce_definition(value):
 work=coeffs(value,3);tags=[R(),R(),R()]
 while True:
  tick()
  active=[key for key,v in work.items() if v and sum(key)>=2]
  if not active:break
  key=max(active,key=lambda ij:(sum(ij),ij))
  coefficient=work.pop(key);i,j=key
  if i>=2:which=0;ii,jj=i-2,j
  elif i and j:which=1;ii,jj=i-1,j-1
  else:which=2;ii,jj=i,j-2
  multiplier=coefficient*f**ii*V**jj
  for k in range(3):tags[k]+=multiplier*inv[which][k]
  for k,increment in enumerate([(0,0),(1,0),(0,1)]):
   at=(ii+increment[0],jj+increment[1])
   work[at]=work.get(at,R())+coefficient*rules[which][k]
  statistics['parameterReductionSteps']+=1
 out=[work.get(key,R()) for key in slots[:3]]
 return out,tags
reduced=[reduce_definition(value) for value in raw_values]
rNS,tauNS=reduced[0];rPS,tauPS=reduced[1]
expectedNS=['3d2fd63718c6eb29287e64a247ecc3c8f5d1acc0f3273f1899763de5b3a2485e',
 '54379117639b58034d0496dd2209a7f1cbbbc793a7b6b877dd5b8146008e2d33',
 '1194f2d241fe9d018c838462a3e1dbcfc94fa6817adb7d3d42f590d97462b0c0']
expectedPS=['db8e07186876e607054c1cab5d8c3dc63daff6b94f82ab8ea84471bf6dc441f0',
 '5157c6de3cdff56ac29c6f99215a61bce48615ef36fa7b833c047ac369a5a9e3',
 'b5690fb21ed2ed788d4eecd558d5d5f0be166618abe01ba5928c5522cdbe59b9']
assert [profile(v.n)['sha256'] for v in rNS]==expectedNS
assert [profile(v.n)['sha256'] for v in rPS]==expectedPS
ntrace=[sum((nq[3+i]*inv[i][j] for i in range(3)),R()) for j in range(3)]


say('necessary_original_t_mean_and_three_row_parameters_defined',
 originalRows=['N1','NS','PS'],
 allExistingCoefficientProfilesMatched=True,
 onlyNecessaryOriginalCoefficientAndTraceDefinitions=True,
 noOldRawWeightedReturnOrCenteredOrSexticOrHeadProofGateExecuted=True,
 noSlopeInverseDefined=True)
tick()

# The following complete identity is already proved in nine FREE original
# variables (not merely W or Phi):
# ell^2*N4(Vphys)=Z0+Z1*sigma+Z2*sigma^2.
# Transport ALL its coefficients, not a component or a Phi multiple.
# sigma is the shifted singleton difference; the ORIGINAL two moment
# errors give q=M*sigma^2-D and H=K-2*m*D*sigma.
# Hence Vlow = D*ell^2*N4(Vphys)+Z1*H/(2m)-D*Z2*q/M.
# Only the OLD paid m,M,ell enter; D is multiplied, never inverted.
D=ell*A2-T*T
Kval=ell*ell*B3-3*ell*A2*T+2*T**3
c_lambda=3-2*lam
Z0=(ell*ell*A1+4*ell*ell*(1-2*lam)*f+2*ell*f*D
    +2*ell*u*w*(ell*c_lambda+T)
    +2*V*(ell*ell+ell*c_lambda*T+T*T)
    +2*bc*t*(T*T-ell*ell))
Z1=(2*(ell*c_lambda+2*T)*(u*V-ell*W1)
    -2*ell*M*w+4*bc*m*T*t)
Z2=2*((u*u-ell*ell*Q)*V-2*m*ell*W1-ell*M*f-bc*M*t)
Vlow=D*Z0+Kval*Z1/(2*m)+D*D*Z2/M

def geometry_degree(value):
 value=checkden(value)
 return max((sum(map(int,ex[2:])) for ex in value.n.to_dict()),default=-1)
for label,value,bound in [('D',D,2),('K',Kval,3),
                          ('Z0',Z0,3),('Z1',Z1,2),('Z2',Z2,1),
                          ('Vlow',Vlow,5)]:
 assert geometry_degree(value)<=bound,(label,geometry_degree(value),bound)
top5=ctx.from_dict({ex:cc for ex,cc in Vlow.n.to_dict().items()
                   if sum(map(int,ex[2:]))==5})
say('new_complete_original_Vlow_in_t_f_V_defined',
 completeOriginalScaledN4CoefficientDegrees=[
  geometry_degree(Z0),geometry_degree(Z1),geometry_degree(Z2)],
 originalMomentDGeometryDegree=geometry_degree(D),
 originalMomentKGeometryDegree=geometry_degree(Kval),
 fullVlow=rp(Vlow),actualGeometryDegree=geometry_degree(Vlow),
 topTotalDegreeFiveNumerator=profile(top5),
 originalSource='D*ell^2*N4(Vphys)+Z1*H/(2m)-D*Z2*q/M',
 allThreeEntireN4CoefficientsRetained=True,
 noIndividualComponentOrPhiMultipleSubstitution=True,
 physicalDOnlyMultipliedNeverInverted=True)
tick()

# GENUINELY NEW ordinary degree-five reduction. Every current multiplier
# multiplies a real original mean. The final ordinary identity is expanded
# and returned, so no associativity or freeness of a three-vector model is
# assumed. This is not the old lambda-model Vlow reduction.
def reduce_new_Vlow(value):
 work=coeffs(value,5);tags=[R(),R(),R()]
 while True:
  tick()
  active=[key for key,v in work.items() if v and sum(key)>=2]
  if not active:break
  key=max(active,key=lambda ij:(sum(ij),ij))
  coefficient=work.pop(key);i,j=key
  if i>=2:which=0;ii,jj=i-2,j
  elif i and j:which=1;ii,jj=i-1,j-1
  else:which=2;ii,jj=i,j-2
  multiplier=coefficient*f**ii*V**jj
  for k in range(3):tags[k]+=multiplier*inv[which][k]
  for k,increment in enumerate([(0,0),(1,0),(0,1)]):
   at=(ii+increment[0],jj+increment[1])
   work[at]=work.get(at,R())+coefficient*rules[which][k]
  statistics['newVlowReductionSteps']+=1
 out=[work.get(key,R()) for key in slots[:3]]
 assert value==dot(out,basis)+dot(tags,forms)
 statistics['newVlowRawMeanReturns']+=1
 for j,v in enumerate(out):
  ck(v);assert td(v)<=5-int(j!=0)
 for v in tags:
  checkden(v);assert geometry_degree(v)<=3
 statistics['newVlowCoordinates']+=3
 return out,tags

rVlow,nuVlow=reduce_new_Vlow(Vlow)
say('new_complete_Vlow_true_t_three_generator_original_return',
 coefficientProfiles=[rp(v) for v in rVlow],
 tDegrees=[td(v) for v in rVlow],
 originalMeanMultipliers=[rp(v) for v in nuVlow],
 ordinaryRawIdentityReturned=True,
 originalIdentity='Vlow=rVlow*(1,f,V)+nuVlow*(Rcal,EBe,EBo)',
 rawTotalGeometryDegreeUpperBound=5,
 coefficientTBounds=[5,4,4],
 exactAuxiliaryIdeal='I7=I6+(Vlow)',
 allOriginalI6ConditionsRetained=True,
 oldWholeThreeMeanHeadOnly=True,
 allH6H8AndH28WeightZeroFibersIncluded=True,
 noFreeThreeGeneratorAlgebraAssumed=True)
tick()

# Only these TWO new original cofactor targets. The determinant degree
# bound is 2+2+4=8 (respectively 1+3+4 and 1+2+5).
# All THREE actual multipliers must share the cancelled factor. This
# preserves its complete zero set; no division of a necessary equation.
def new_original_cofactor(label,second_name,second_row):
 rows3=[rN,second_row,rVlow]
 mu=[rows3[1][1]*rows3[2][2]-rows3[1][2]*rows3[2][1],
     rows3[2][1]*rows3[0][2]-rows3[2][2]*rows3[0][1],
     rows3[0][1]*rows3[1][2]-rows3[0][2]*rows3[1][1]]
 if not any(mu):
  say('new_full_NV_t_cofactor_zero',label=label,
      originalRows=['N1',second_name,'Vlow'],
      allOriginalRowsAndZeroFibersRetained=True)
  return
 denominator=O
 for v in mu:
  ck(v);denominator=exact(denominator,denominator.gcd(v.d))*v.d
 numerators=[v.n*exact(denominator,v.d) for v in mu]
 common=Z
 for value in numerators:common=common.gcd(value)
 assert common
 primitive=[R(exact(value,common)) for value in numerators]
 returned=[sum((primitive[i]*rows3[i][j] for i in range(3)),R())
           for j in range(3)]
 assert not returned[1] and not returned[2]
 statistics['newFixedCofactorCoordinates']+=3
 value=ck(returned[0])
 assert td(value)<=8
 core,removed=strip(value.n)
 if core:
  lead=core.coefficient(0);core/=lead;removed*=lead
 assert core*removed==value.n
 # Only OLD paid factors are removed; transport this same multiplier
 # to all THREE true original rows and return all coordinates again.
 final=[checkden(v*R(value.d)/R(removed)) for v in primitive]
 actual=[sum((final[i]*rows3[i][j] for i in range(3)),R())
         for j in range(3)]
 assert actual==[R(core),R(),R()]
 statistics['newOriginalScalarSupportReturns']+=3
 degree=max((int(ex[2]) for ex in core.to_dict()),default=-1)
 top=ctx.from_dict({(ex[0],ex[1],0,0,0):cc
       for ex,cc in core.to_dict().items() if int(ex[2])==degree}) if core else Z
 say('new_complete_full_NV_t_original_scalar_return',
     label=label,originalRows=['N1',second_name,'Vlow'],
     actualThreeMultiplierCommonContent=profile(common),
     actualScalarNumerator=profile(value.n),
     actualScalarDenominator=profile(value.d),
     threePrimitiveOriginalMultipliers=[rp(v) for v in primitive],
     completeThreeOriginalCoordinatesReturned=True,
     necessaryPolynomial=profile(core),tDegree=degree,
     tDegreeUpperBound=8,trueTLeadingNumerator=profile(top),
     normalizedThreeCoordinateOriginalReturn=True,
     originalSourceByExactMeanTraces=True,
     allCommonContentAndNewLeadingZeroFibersRetained=True,
     allOldSlopeAndH28ZeroLociIncluded=True,
     noDOrSlopeOrNewLeadingInverse=True,
     wholePhiExcluded=bool(core) and int(core.total_degree())==0)
 tick()

new_original_cofactor('original_N1_NS_complete_Vlow','NS',rNS)
new_original_cofactor('original_N1_PS_complete_Vlow','PS',rPS)
say('new_correct_t_complete_Vlow_two_original_scalar_input_finished',
 statistics=statistics,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noExternalDependency=True,
 noOldWeightedScalarOrGlobalSixMultiplierOrH28GateReplayed=True,
 allOriginalI6AndEntireVlowRetained=True,
 noCoefficientPayloadOrCacheOrChunksSaved=True,
 noNewWholeHeadUnitOrFinitePointClaim=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)

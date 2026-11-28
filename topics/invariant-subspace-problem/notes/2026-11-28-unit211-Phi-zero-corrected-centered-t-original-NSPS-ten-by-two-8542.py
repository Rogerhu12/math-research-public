#!/usr/bin/env python3
"""NEW correct Phi t-slope input: CENTERED full original NS/PS.
Only necessary true Gram/mean-rule/N1 coefficient definitions are
regenerated. No old lambda CH, slope factorization, uncentered qZ or
six-row proof gate is run. The new targets are complete ordinary
NS/PS-to-three-mean traces, the centered monic quadratic, their two
new linear rows and omega multiples, and their genuine two-source
cofactor after canceling only both actual multipliers' common content.
The entire two-curve slope-zero locus is retained.
Self-contained, zero dependencies, absolute 120 seconds / 1 GiB.
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
statistics={'exactDivisionProducts':0,'newRawNSPSReturns':0,
 'newDegreeThreeReductionSteps':0,'newCenteredInverseReturns':0,
 'newCenteredMonicRawReturns':0,'newWeightedRowCoordinateReturns':0,
 'newOmegaMultipleReturns':0,'newPrimitiveCofactorCoordinates':0}
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 statistics['exactDivisionProducts']+=1;return q
def weight(p):return all(not any(map(int,ex[2:])) for ex in p.to_dict())
def scalar(p):return all(not any(map(int,ex[3:])) for ex in p.to_dict())
paid=up*Qp*(1-Qp)*(up-1)*Kw.n*L.n*Mn.n*gg.n
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
def tc(value,k):
 value=ck(value)
 return R(ctx.from_dict({(ex[0],ex[1],0,0,0):cc
      for ex,cc in value.n.to_dict().items() if int(ex[2])==k}),value.d)
af=tc(rN[1],1);bf=tc(rN[1],0);av=tc(rN[2],1);bv=tc(rN[2],0)
slope=af*bv-bf*av
assert profile(slope.n)['sha256']=='f0dc5e9187e23d9e5528349a792d327f4e74d11f8cc51b90b8f2358053274592'
assert profile(slope.d)['sha256']=='8c88bcc2d5d2031285fa07f3f638132c4aa932d2aabc76560870a7d9446e7f4c'
support=paid*slope.n
say('necessary_t_mean_and_N1_coefficients_defined_for_new_centered_NSPS',
 existingN1AndSlopeProfileIdentitiesMatched=True,
 noOldLambdaCHOrSlopeFactorOrUncenteredSixRowProofExecuted=True,
 slopeZeroCurvesRetained=['H6','H8'])

# NEW original cubic sources, before any centered substitution.
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

# Polynomial reduction only by the three ORIGINAL mean rules.
# For every step retain ordinary f,V multipliers on those same means.
def reduce_raw(value):
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
  statistics['newDegreeThreeReductionSteps']+=1
 out=[work.get(key,R()) for key in slots[:3]]
 assert value-dot(out,basis)==dot(tags,forms)
 statistics['newRawNSPSReturns']+=1
 for j,v in enumerate(out):assert td(v)<=3-int(j>0)
 return out,tags
reduced=[]
for name,value in zip(['NS','PS'],raw_values):
 out,tags=reduce_raw(value);reduced.append((out,tags))
 say('new_complete_original_weighted_cubic_three_mean_return',
     name=name,tDegrees=[td(v) for v in out],
     remainderProfiles=[rp(v) for v in out],
     completeOrdinaryPolynomialIdentityReturned=True,
     originalMeanMultipliersGeometricDegrees=[
      max((int(ex[3])+int(ex[4]) for ex in v.n.to_dict()),default=-1) for v in tags],
     noOriginalFreeOrAssociativeThreeColumnModelAssumed=True)

# NEW centered coordinate. The f-slot is used for omega only after
# the raw three-mean identities above have been returned.
A=tc(rN[0],2);B=tc(rN[0],1);C=tc(rN[0],0)
omega=f;shift=A*t+B
fhat=((av*t+bv)*omega-A*bv*t-B*bv+av*C)/slope
Vhat=(-(af*t+bf)*omega+A*bf*t+B*bf-af*C)/slope
assert af*fhat+av*Vhat==omega-shift
assert rN[0]+rN[1]*fhat+rN[2]*Vhat==R()
statistics['newCenteredInverseReturns']+=2
def ock(v):
 v=checkden(v,support)
 assert all(not int(ex[4]) for ex in v.n.to_dict())
 return v
def ocs(value,cap=2):
 value=ock(value);groups={}
 for ex,cc in value.n.to_dict().items():
  k=int(ex[3]);assert k<=cap
  groups.setdefault(k,{})[(ex[0],ex[1],ex[2],0,0)]=cc
 return [R(ctx.from_dict(groups[k]),value.d) if k in groups else R()
         for k in range(cap+1)]
weights=[af*af,2*af*av,av*av]
gamma=[sum((weights[i]*inv[i][j] for i in range(3)),R()) for j in range(3)]
wr=[sum((weights[i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
qomega=(omega-shift)**2-(wr[0]+wr[1]*fhat+wr[2]*Vhat)
# Same new qomega returned on all ORIGINAL three-mean source coordinates.
q_from_original=R()
for row,coef in zip(quad,gamma):
 changed=(row[0]+row[1]*fhat+row[2]*Vhat+
          row[3]*fhat*fhat+row[4]*fhat*Vhat+row[5]*Vhat*Vhat)
 q_from_original+=coef*changed
assert qomega==q_from_original
statistics['newCenteredMonicRawReturns']+=1
qc=ocs(qomega)
assert qc[2]==R(1)
assert td(qc[0],support)<=2 and td(qc[1],support)<=2
say('new_centered_original_monic_omega_quadratic',
 coordinate='omega=af*f+av*V+A*t+B; n0=A*t^2+B*t+C',
 qCoefficientOrder=['one','omega','omega^2'],
 qProfiles=[rp(v) for v in qc],
 qTDegrees=[td(v,support) for v in qc],
 originalPureWeightGammaMeanCombinationReturned=True,
 centeredInverseIdentitiesReturned=True,
 noNewTOrGeometricHeadOrDInverse=True,
 allH6AndH8ZeroFibersRetained=True)

linear_rows=[];added_rows=[]
for name,(vec,tags) in zip(['NS','PS'],reduced):
 line=ock(vec[0]+vec[1]*fhat+vec[2]*Vhat)
 lc=ocs(line,1)
 assert line==lc[0]+lc[1]*omega
 for v in lc:assert td(v,support)<=3
 statistics['newWeightedRowCoordinateReturns']+=2
 linear_rows.append(lc);added_rows.append(lc)
 multiple=[-qc[0]*lc[1],lc[0]-qc[1]*lc[1]]
 assert omega*line-(multiple[0]+multiple[1]*omega)==lc[1]*qomega
 for v in multiple:assert td(v,support)<=5
 statistics['newOmegaMultipleReturns']+=1;added_rows.append(multiple)
 say('new_complete_original_centered_weighted_cubic_two_columns',
     name=name,linearProfiles=[rp(v) for v in lc],
     linearTDegrees=[td(v,support) for v in lc],
     omegaMultipleProfiles=[rp(v) for v in multiple],
     omegaMultipleTDegrees=[td(v,support) for v in multiple],
     fullOriginalCubicViaReturnedOrdinaryMeanTrace=True,
     singleAffineSubstitutionAfterOriginalReduction=True,
     onlyPaidWeightsAndExplicitSlopeInverted=True)

say('new_exact_I6_centered_t_ten_by_two_presentation',
 retainedOriginalMeanRowCount=6,newActualWeightedRows=4,totalRows=10,
 originalSixMeanRowsKeptByCoordinateTranslationNotReexecuted=True,
 exactness='original I4 quotient plus complete NS,PS and their omega multiples in the same monic quadratic',
 noModuleFreenessAssumedForOriginalQuotient=True,
 allSlopeZeroCurvesRetained=True,wholePhiExcluded=False)

# NEW fixed 2x2 original NS/PS scalar.  Cancel BOTH actual multiplier
# numerators jointly, then return both coordinates with those new
# polynomial multipliers. This is not division of an old scalar equation.
mu=[linear_rows[1][1],-linear_rows[0][1]]
if any(mu):
 den=O
 for v in mu:
  ock(v);assert scalar(v.n)
  den=exact(den,den.gcd(v.d))*v.d
 nums=[v.n*exact(den,v.d) for v in mu]
 common=Z
 for pp in nums:common=common.gcd(pp)
 assert common
 primitive=[R(exact(pp,common)) for pp in nums]
 returned=[sum((primitive[i]*linear_rows[i][j] for i in range(2)),R()) for j in range(2)]
 assert not returned[1]
 for v in returned:ock(v);assert scalar(v.n)
 statistics['newPrimitiveCofactorCoordinates']+=2
 value=returned[0]
 if value:
  core,removed=strip(value.n,support)
  lead=core.coefficient(0);core/=lead;removed*=lead
  assert core*removed==value.n
  degree=max((int(ex[2]) for ex in core.to_dict()),default=-1)
  assert degree<=6
  headp=ctx.from_dict({(ex[0],ex[1],0,0,0):cc
         for ex,cc in core.to_dict().items() if int(ex[2])==degree})
 else:core=Z;removed=O;degree=-1;headp=Z
 say('new_complete_original_centered_NSPS_fixed_pair_scalar',
     bothActualMultiplierCommon=profile(common),
     bothPrimitiveMultiplierProfiles=[rp(v) for v in primitive],
     bothOriginalCoordinatesReturned=True,
     originalScalarProfile=rp(value),retainedNecessaryTPolynomial=profile(core),
     tDegree=degree,tDegreeUpperBound=6,actualTLeadingNumerator=profile(headp),
     onlyAlreadyPaidWeightsAndExplicitOpenSlopeRemoved=True,
     allMultiplierCommonZeroFibersRetained=True,
     allTLeadingZeroFibersRetained=True,
     noNewWholeSlopeZeroConclusion=True,
     slopeComplementExcluded=bool(core) and int(core.total_degree())==0,
     wholePhiExcluded=False)
else:
 say('new_NSPS_pair_multipliers_zero_no_scalar_claim',
     completeTenRowPresentationKept=True,wholePhiExcluded=False)
say('new_centered_t_complete_original_NSPS_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=statistics,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noExternalDependency=True,noOldSixRowOrCHOrFactorGateReplayed=True,
 noLargeCoefficientPayloadOrCacheSaved=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)

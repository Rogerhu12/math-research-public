#!/usr/bin/env python3
"""NEW correct whole Phi: t-parameter true mean rules and original N1.
The whole ell=1/2 exclusion pays 2ell-1. The true (f,V)-quadratic head is
32*u*Q*(2ell-1)/M^2, so there is NO new weight exception for the three
original mean rules over weight[t]. This source constructs the ACTUAL
rules, the original monic lambda cubic, and the same N1 affine remainder.
A new pure-weight N1 slope is factored; only its nonzero locus is used
for the exact six-by-two model. Its entire zero locus is kept.
No old lambda-parameter rules, 15-column gate, C6/decic/NPV5 gate,
ell-half gate, or complete weighted cubic source is replayed.
Self-contained, no external dependencies. 120 seconds / 1 GiB.
"""
import hashlib,json,math,resource,signal,time
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
s=u-1;delta=1-Q;L=Q-2*s*(u-2);ell=L/Q
m=u-ell;T0=2*u-ell*Q-2*u*u;J=2*u*(1-u)+ell*Q
P02=2*s*ell*Q;Pf=T0*(J-Q)
M=ell*(2*u-ell*Q)-u*u;bc=M/(4*delta)
Kw=Q+4*s;Mn=Q*M;g=2*ell-1
lam=(J*f-Q*V+bc*Q*t-s*T0)/P02
T=-ell+T0*(f-V+bc*t)/P02
z=Q*t;w=lam-1-T
W1=T0/2+2*u*f;theta=u-ell*Q
x=(theta*V-m*W1)/M;y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t
statistics={'exactDivisionProducts':0,'newOriginalCoordinateReturns':0,
 'newThreeMeanRuleReturns':0,'newN1OriginalReturn':0,
 'newLambdaActionReturns':0,'newLambdaCayleyHamiltonCoordinates':0,
 'newSlopeCoordinateReturns':0,'newMonicAndSixRowReturns':0}
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 statistics['exactDivisionProducts']+=1;return q
def weight(p):return all(not any(int(j) for j in ex[2:]) for ex in p.to_dict())
def scalar(p):return all(not any(int(j) for j in ex[3:]) for ex in p.to_dict())
paid=up*Qp*(1-Qp)*(up-1)*Kw.n*L.n*Mn.n*g.n
def strip(p,support=None):
 support=paid if support is None else support
 original=p;removed=O
 while p and int(p.total_degree())>0:
  gg=p.gcd(support)
  if int(gg.total_degree())==0:break
  p=exact(p,gg);removed*=gg
 assert p*removed==original
 return p,removed
def checkden(value,support=None):
 value=R(value);assert weight(value.d)
 rr,_=strip(value.d,support)
 assert rr and int(rr.total_degree())==0,('unpaid denominator',str(rr))
 return value
def ck(value):
 value=checkden(value);assert scalar(value.n);return value
def tdegree(value):
 value=ck(value);return max((int(ex[2]) for ex in value.n.to_dict()),default=-1)
def geomdegree(value):
 value=checkden(value);return max((sum(map(int,ex[2:])) for ex in value.n.to_dict()),default=-1)
def profile(p):
 raw=str(sorted(p.to_dict().items())).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1]*5,
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(p.to_dict()),'sha256':hashlib.sha256(raw).hexdigest()}
def rp(v):return {'numerator':profile(v.n),'denominator':profile(v.d)}
for value in [ell,m,T0,J,P02,Pf,M,bc,g,lam,T,W1,x,y,A1]:checkden(value)
assert T0==-Kw and J-Q==-4*s*s and Pf==4*s*s*Kw
G=lam*P02+s*T0;Pc=Q*P02*(ell+T)-G*T0
assert Pf*f+Pc==0 and Q*V==J*f-G+bc*z
statistics['newOriginalCoordinateReturns']+=2
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

b=E(ell/2,m/(2*delta));c=b.conj();aw=E(1-ell)
p=E(1,1);q=p.conj();X=E(x,y);Y=X.conj()
rr=X-aw*p-c*E(t);ss=Y-aw*q-b*E(t)
rows=[[E(),E(),p,q],[E(),E(A1),rr,ss],
      [p,rr,E(),E(t)],[q,ss,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,w):return [v[i]+w[i] for i in range(4)]
def vs(a,v):return [a*x for x in v]
def vm(v,w):
 return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tr(v):return aw*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tr(vm(row,v)) for row in rows]
d=DK(one);F2=tr(d);Kd=DK(d)
assert d==[E(u),E(2*f-V-(1-ell)*u),X,Y] and F2==E(2*f)
assert b*c==E(bc) and b*X+c*Y==E(V) and b*p*X+c*q*Y==E(W1)
statistics['newOriginalCoordinateReturns']+=5
def mean(j):
 sq=2*tr(vm(rows[0],rows[1])) if j==1 else tr(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
E0=mean(0);E1=mean(1);EB=mean(2);EC=mean(3)
assert not E0 and not E1.b and EC==EB.conj()
Rcal=4*(f-u)*(V-f)+bc*t*t+t*(4*bc*u-ell*V+m*(T0+4*u*f-2*V)/(2*delta))
assert E(2*Rcal)+E1-b*EB-c*EC==E()
statistics['newOriginalCoordinateReturns']+=4
forms=[Rcal,EB.a,EB.b]
slots=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
def coefficients(value,cap=2):
 value=checkden(value);out={}
 for ex,cc in value.n.to_dict().items():
  key=(int(ex[3]),int(ex[4]));assert sum(key)<=cap
  term=ctx.from_dict({(ex[0],ex[1],ex[2],0,0):cc})
  out[key]=out.get(key,R())+R(term,value.d)
 for v in out.values():ck(v)
 return out
def six(value):
 co=coefficients(value)
 return [co.get(k,R()) for k in slots]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),R())
def mm(A,B):
 return [[dot(row,[B[k][j] for k in range(len(B))])
          for j in range(len(B[0]))] for row in A]
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
def det3(A):
 return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
        -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
        +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
quad=[six(value) for value in forms]
H=[row[3:] for row in quad];low=[row[:3] for row in quad]
assert all(weight(v.n) and weight(v.d) for row in H for v in row)
head=32*u*Q*g/(M*M)
assert det3(H)==head
inv=[[ck(v/head) for v in row] for row in adj3(H)]
rules=[[-v for v in row] for row in mm(inv,low)]
basis=[R(1),f,V];mons=[f*f,f*V,V*V]
normalized=[mons[i]-dot(rules[i],basis) for i in range(3)]
for i in range(3):
 assert normalized[i]==dot(inv[i],forms)
 for j,v in enumerate(rules[i]):
  ck(v);assert tdegree(v)<=2-int(j>0)
 statistics['newThreeMeanRuleReturns']+=1
say('new_whole_Phi_t_parameter_three_true_mean_rules',
 wholeNewEllHalfExclusionUsed=True,
 head='32*u*Q*(2ell-1)/M^2',headProfile=rp(head),
 threeFullOriginalPolynomialRulesReturned=True,
 rulesCoefficientProfiles=[[rp(v) for v in row] for row in rules],
 wholeUnlocalizedMeanQuotientGeneratedBy=['1','f','V'],
 coefficientParameter='original t',noNewWeightHeadOrTInverse=True,
 noOriginalN1NeededForThreeMeanHead=True,
 noFreeThreeGeneratorAlgebraAssumed=True,statistics=statistics)

# Genuinely NEW original lambda multiplication in this t presentation.
MF=[[R(int(i==1)),rules[0][i],rules[1][i]] for i in range(3)]
MV=[[R(int(i==2)),rules[1][i],rules[2][i]] for i in range(3)]
Id=[[R(int(i==j)) for j in range(3)] for i in range(3)]
lc0=(bc*Q*t-s*T0)/P02;lcf=J/P02;lcV=-Q/P02
ML=[[lc0*Id[i][j]+lcf*MF[i][j]+lcV*MV[i][j] for j in range(3)] for i in range(3)]
action_tags=[[R(),R(),R()],[lcf,lcV,R()],[R(),lcf,lcV]]
for j in range(3):
 assert lam*basis[j]-dot([ML[i][j] for i in range(3)],basis)==dot(action_tags[j],normalized)
 statistics['newLambdaActionReturns']+=1
trM=sum((ML[i][i] for i in range(3)),R())
c2=-trM
c1=sum((ML[i][i]*ML[j][j]-ML[i][j]*ML[j][i]
        for i in range(3) for j in range(i+1,3)),R())
c0=-det3(ML)
ML2=mm(ML,ML);ML3=mm(ML2,ML)
for i in range(3):
 for j in range(3):
  assert not (ML3[i][j]+c2*ML2[i][j]+c1*ML[i][j]+c0*Id[i][j])
  statistics['newLambdaCayleyHamiltonCoordinates']+=1
for v,bound in [(c2,1),(c1,2),(c0,3)]:assert tdegree(v)<=bound
say('new_original_lambda_monic_cubic_in_whole_t_model',
 coefficientOrder=['lambda^2','lambda','one'],
 coefficientProfiles=[rp(v) for v in (c2,c1,c0)],
 tDegrees=[tdegree(v) for v in (c2,c1,c0)],
 actualLambdaMonicDegree=3,totalLambdaTDegreeUpperBound=3,
 allThreeFullRawLambdaActionIdentitiesReturned=True,
 allNineCayleyHamiltonCoordinatesReturned=True,
 originalTraceGivenByTrueMeanRules=True,noModuleFreenessAssumed=True,
 wholePhiExcluded=False)

# NEW full true-germ polarization in the SAME original coordinates.
def N4(v):
 vv=vm(v,v);tv=tr(v)
 return 2*tr(vm(d,vv))-F2*tr(vv)-4*tv*tr(vm(d,v))+2*F2*tv*tv+tr(vm(v,DK(v)))
def centered(v):return va(v,vs(-tr(v),one))
v0,v1=rows[0],rows[1]
N0=N4(v0);Npolar=N4(va(v0,v1))-N0-N4(v1)
v0c,v1c=centered(v0),centered(v1)
Pjet=3*tr(vm(vm(v0c,v0c),v1c))
assert N0==E(2*lam*P02) and Pjet==E(3*w*P02)
N1E=Npolar-E(4*lam*w*P02);assert not N1E.b
N1=N1E.a
nq=six(N1);ntrace=[sum((nq[3+i]*inv[i][j] for i in range(3)),R()) for j in range(3)]
rN=[nq[j]+sum((nq[3+i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
assert dot(rN,basis)==N1-dot(ntrace,forms)
statistics['newN1OriginalReturn']+=1
for j,v in enumerate(rN):assert tdegree(v)<=2-int(j>0)
say('new_true_original_N1_affine_t_parameter_return',
 coefficientOrder=['one','f','V'],coefficientProfiles=[rp(v) for v in rN],
 tDegrees=[tdegree(v) for v in rN],
 completeOriginalPolarizationAndThreeMeanTraceReturned=True,
 noOldLambdaSlopeOrN1ModuleGateReplayed=True,
 originalFourEquationIdealKept=True)

def tc(value,k):
 value=ck(value)
 return R(ctx.from_dict({(ex[0],ex[1],0,0,0):cc
      for ex,cc in value.n.to_dict().items() if int(ex[2])==k}),value.d)
af=tc(rN[1],1);bf=tc(rN[1],0)
av=tc(rN[2],1);bv=tc(rN[2],0)
assert rN[1]==af*t+bf and rN[2]==av*t+bv
slope=ck(af*bv-bf*av);assert weight(slope.n)
say('new_t_parameter_N1_original_pure_weight_slope',
 slopeNumerator=profile(slope.n),slopeDenominator=profile(slope.d),
 slopeIsZero=not bool(slope),allSlopeZeroFibersRetained=True)
if slope:
 retained,paidpart=strip(slope.n)
 scale0=retained.coefficient(0);retained/=scale0;paidpart*=scale0
 assert retained*paidpart==slope.n
 const,factors=retained.factor();back=ctx.constant(const);facts=[]
 for fac,exponent in factors:
  exponent=int(exponent);back*=fac**exponent
  facts.append({'multiplicity':exponent,**profile(fac)})
 assert back==retained
 say('new_t_parameter_N1_slope_exact_remaining_support',
     retainedWeightSupport=profile(retained),factors=facts,
     constant=str(const),fullExactFactorProductReturned=True,
     slopePaidEverywhere=bool(retained) and int(retained.total_degree())==0,
     entireUnknownSlopeZeroLocusKept=True)
 # A new two-generator model ONLY where this pure-weight slope is
 # nonzero. The symbol in the f-slot now denotes the new coordinate Zc.
 support=paid*slope.n
 def ock(v):
  v=checkden(v,support)
  assert not any(int(ex[4]) for ex in v.n.to_dict())
  return v
 Zc=f
 fhat=((av*t+bv)*Zc+av*rN[0])/slope
 Vhat=(-(af*t+bf)*Zc-af*rN[0])/slope
 assert af*fhat+av*Vhat==Zc
 assert rN[0]+rN[1]*fhat+rN[2]*Vhat==R()
 statistics['newSlopeCoordinateReturns']+=2
 changed=[row[0]+row[1]*fhat+row[2]*Vhat+row[3]*fhat*fhat
          +row[4]*fhat*Vhat+row[5]*Vhat*Vhat for row in quad]
 monic_tags=[af*af*inv[0][j]+2*af*av*inv[1][j]+av*av*inv[2][j] for j in range(3)]
 qZ=ock(dot(monic_tags,changed))
 def zcs(v):
  v=ock(v);out=[R(),R(),R()]
  for ex,cc in v.n.to_dict().items():
   j=int(ex[3]);assert j<=2 and not ex[4]
   out[j]+=R(ctx.from_dict({(ex[0],ex[1],ex[2],0,0):cc}),v.d)
  return out
 qco=zcs(qZ);assert qco[2]==R(1)
 assert all(int(ex[2])<=2 for ex in qco[1].n.to_dict())
 assert all(int(ex[2])<=3 for ex in qco[0].n.to_dict())
 returned_rows=[]
 for i,value in enumerate(changed):
  cc=zcs(value);line=ock(value-cc[2]*qZ);lc=zcs(line);assert not lc[2]
  returned_rows.append([lc[0],lc[1]])
  zrem=[-qco[0]*lc[1],lc[0]-qco[1]*lc[1]]
  assert Zc*line-(zrem[0]+zrem[1]*Zc)==lc[1]*qZ
  returned_rows.append(zrem);statistics['newMonicAndSixRowReturns']+=2
 assert qZ==dot(monic_tags,changed)
 statistics['newMonicAndSixRowReturns']+=1
 for row in returned_rows:
  for v in row:ock(v);assert scalar(v.n)
 say('new_exact_original_t_slope_six_by_two_model',
     monicQCoordinate='Zc=af*f+av*V',
     monicQProfiles=[rp(v) for v in qco],
     monicQTDegrees=[max((int(ex[2]) for ex in v.n.to_dict()),default=-1) for v in qco],
     sixOriginalRowProfiles=[[rp(v) for v in row] for row in returned_rows],
     completeI4Presentation=True,
     exactIdeal='three changed means = (monic qZ, three linear remainders)',
     sameZIdealModule='six rows: each linear remainder and its Z multiple modulo qZ',
     noFreeOriginalTwoGeneratorAlgebraAssumed=True,
     onlyOriginalWeightAndExplicitSlopeInverses=True,
     allRemainingSlopeZeroFibersRetained=True,
     physicalDAndTNotInverted=True,wholePhiExcluded=False)
else:
 say('new_t_parameter_slope_identically_zero_no_two_column_claim',
     wholeThreeGeneratorAndMonicLambdaCubicKept=True,
     allOriginalFibersRetained=True)
say('new_correct_t_parameter_original_N1_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=statistics,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noExternalDependency=True,noOldMatrixOrCofactorGateReplayed=True,
 noLargeCoefficientPayloadOrCacheSaved=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)

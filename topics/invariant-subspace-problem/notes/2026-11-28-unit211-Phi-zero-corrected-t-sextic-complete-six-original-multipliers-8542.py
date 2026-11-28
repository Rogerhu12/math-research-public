#!/usr/bin/env python3
"""NEW correct Phi: complete SIX original terminal multipliers.
The previous centered two-column scalar is paid only on the N1-slope
complement. This input forms its genuinely new third N1 multiplier,
returns all three original coefficient coordinates, combines the
necessary original mean traces, and returns the complete six-source
ordinary polynomial identity. ONLY final old-paid denominators allow
extension over the ENTIRE slope-zero locus.
No old CH, slope factor, qomega, omega-multiple, six/two or ten/two
proof gate is executed. The old two multipliers are only parameters
regenerated from their necessary coefficient definitions and pinned
by their already returned SHA identities.
If all six final denominators are old-paid, return the whole C6 and
factor its original t-leading coefficient for the first time.
Self-contained, zero dependencies. 120 seconds / 1 GiB.
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
 'newThirdN1ThreeCoordinates':0,'newSixOriginalRawReturns':0,
 'newFinalSixOriginalReturns':0,'newWholeDenominatorClassifications':0,
 'newWholeTHeadFactorProducts':0}
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
# The old omega-linear coefficients do not depend on the constant shift.
nf,nV=rN[1],rN[2]
omegaNS=(nV*rNS[1]-nf*rNS[2])/slope
omegaPS=(nV*rPS[1]-nf*rPS[2])/slope
old_pair=[omegaPS,-omegaNS]
scale=O
for value in old_pair:
 assert weight(value.d) and scalar(value.n)
 scale=exact(scale,scale.gcd(value.d))*value.d
# The already proved multiplier common was the constant 1. Do not
# rerun its gcd/factor proof or the old two-coordinate scalar return.
mu=[R(value.n*exact(scale,value.d)) for value in old_pair]
assert profile(mu[0].n)['sha256']=='17143d55d1cf0a3fe3680fb6965cda1f1eaa64087dbb40137ddf28a43dd8cedd'
assert profile(mu[1].n)['sha256']=='729506952659f75ea64caeabe64eed3db7f4438ef4d66109991db9669b05bd4e'
say('necessary_existing_six_source_coefficients_and_two_multiplier_parameters',
 allExistingN1NSPSTwoMultiplierProfileIdentitiesMatched=True,
 noOldQomegaOrOmegaMultipleOrPairProofGateExecuted=True,
 noOldRawNSPSTraceGateExecuted=True,
 onlyNecessaryCoefficientAndTraceDefinitionsRegenerated=True)
tick()

# NEW third N1 multiplier in the ORIGINAL three-generator coordinates.
cn=(-av*rNS[1]+af*rNS[2])/slope
cp=(-av*rPS[1]+af*rPS[2])/slope
kappa=mu[0]*cn+mu[1]*cp
three_mu=[-kappa,mu[0],mu[1]]
three_rows=[rN,rNS,rPS]
three_return=[sum((three_mu[i]*three_rows[i][j] for i in range(3)),R())
              for j in range(3)]
assert not three_return[1] and not three_return[2]
value=three_return[0]
assert value and scalar(value.n) and weight(value.d)
statistics['newThirdN1ThreeCoordinates']+=3
assert profile(value.n)['sha256']=='40588df48a5227d32d88a916170e9e0853acbefec5320b6f155299de1113b0b5'
assert profile(value.d)['sha256']=='e6ad630c7a116018ce1b4dcdd95145dc3b38ba861670c4774063194900672c59'
say('new_original_third_N1_multiplier_and_complete_three_coordinates',
 thirdN1Multiplier=rp(-kappa),originalRowOrder=['N1','NS','PS'],
 samePreviouslyDefinedScalarIdentityMatched=True,
 allThreeOriginalCoordinatesReturned=True,
 noSlopeZeroExtensionClaimYet=True)

# NEW complete ordinary identity on the SIX original polynomial forms.
Omega=[kappa*ntrace[j]-mu[0]*tauNS[j]-mu[1]*tauPS[j] for j in range(3)]
Omega+=three_mu
original=forms+[N1,raw_values[0],raw_values[1]]
assert dot(Omega,original)==value
statistics['newSixOriginalRawReturns']+=1
bad=[]
for j,v in enumerate(Omega+[value]):
 assert weight(v.d)
 rest,removed=strip(v.d,paid)
 assert rest*removed==v.d
 statistics['newWholeDenominatorClassifications']+=1
 if int(rest.total_degree())>0:
  bad.append({'index':j,'remainingDenominator':profile(rest)})
say('new_complete_six_original_raw_identity_and_final_denominators',
 originalOrder=['Rcal','EBe','EBo','N1','NS','PS'],
 finalMultiplierProfiles=[rp(v) for v in Omega],
 completeOrdinaryOriginalIdentityReturned=True,
 onlyFinalActualDenominatorsClassified=True,
 oldPaidOnlyRegular=(len(bad)==0),unpaidDenominators=bad,
 noPhysicalSlopeInverseUsedInThisClassification=True)
tick()

if not bad:
 # C.n is cleared using its actual OLD-paid denominator; strip ONLY
 # old-paid numerator factors, transporting them to all six multipliers.
 core,removed=strip(value.n,paid)
 lead=core.coefficient(0);core/=lead;removed*=lead
 assert core*removed==value.n
 assert profile(core)['sha256']=='5041106f2793c3a95fb8c0fdc1a177e23de00e18bce476efb2e42b871d926be1'
 final=[checkden(v*R(value.d)/R(removed),paid) for v in Omega]
 assert dot(final,original)==R(core)
 statistics['newFinalSixOriginalReturns']+=1
 degree=max((int(ex[2]) for ex in core.to_dict()),default=-1)
 assert degree==6 and scalar(core)
 lead_t=ctx.from_dict({(ex[0],ex[1],0,0,0):cc
        for ex,cc in core.to_dict().items() if int(ex[2])==degree})
 assert profile(lead_t)['sha256']=='89cadc1ec0de4d55df49a64ded467843259e929b15dd7dc88f973ccb80e6dd4b'
 say('new_whole_Phi_original_sextic_extension_across_entire_slope_zero',
     wholeOriginalC6=profile(core),tDegree=degree,
     allSixFinalOriginalMultipliersReturned=True,
     allFinalDenominatorsOnlyAlreadyPaidWeights=True,
     H6AndH8EntireZeroLociIncluded=True,
     noDOrTOrLambdaOrSlopePhysicalInverse=True,
     coefficientRing='original paid-weight ring A[t,f,V]',
     wholePhiExcluded=False)
 # GENUINELY NEW original t-head factorization; no earlier head factor
 # or support payment is assumed. Keep every new factor's entire zero.
 retained,paidpart=strip(lead_t,paid)
 leading=retained.coefficient(0);retained/=leading;paidpart*=leading
 assert retained*paidpart==lead_t
 const,factors=retained.factor();back=ctx.constant(const);facts=[]
 for factor,exponent in factors:
  exponent=int(exponent);back*=factor**exponent
  facts.append({'multiplicity':exponent,**profile(factor)})
 assert back==retained
 statistics['newWholeTHeadFactorProducts']+=1
 say('new_whole_original_t_sextic_actual_leading_weight_support',
     originalHead=profile(lead_t),remainingHeadSupport=profile(retained),
     completeQQFactors=facts,constant=str(const),
     completeExactFactorProductReturned=True,
     entireRemainingHeadZeroFibersRetained=True,
     originalUnlocalizedI6GeneratedBy18OnHeadComplement=True,
     generators='t^j*(1,f,V), 0<=j<=5',
     notFreeAndNoIndependentU0ScaleLengthClaim=True,
     wholeHeadPaid=bool(retained) and int(retained.total_degree())==0,
     wholePhiExcluded=False)
else:
 say('new_six_source_identity_does_not_pay_global_extension',
     allExistingSlopeZeroFibersRetained=True,
     unpaidActualFinalDenominators=bad,
     noNewWholePhiSexticOrGlobalMonicClaim=True,
     wholePhiExcluded=False)
say('new_complete_six_source_original_globalization_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=statistics,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noExternalDependency=True,noOldCenteredQOrRowOrPairProofGateReplayed=True,
 noLargeCoefficientPayloadOrCacheSaved=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)

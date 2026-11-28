#!/usr/bin/env python3
"""NEW corrected Phi, entire second complete-NV t-head.
The ORIGINAL moments give q_lambda=-(E3-(lambda-3/2)*E2)/2, monic degree3.
Together with the new idempotent-polarization compact COMPLETE NV,
this defines an exact free-three ambient algebra over old-weight[sigma].
Only six new same-point columns and TWO prescribed 3-column cofactors:
[0,1,3] and [0,3,4]. Every scalar returns all THREE complete original
conditions before and after common multiplier cancellation.
No prior20/8-column source, first-head gate, scalar gcd, prime, factorization,
new leading inverse, M inverse, physical t=0, or full-system sufficiency.
Self-contained; 120 seconds /1 GiB, fixed target and original source order.
"""
import hashlib,json,resource,signal,time
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120-second boundary')
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','lambda','sigma'),'lex')
up,Qp,lp,sp=ctx.gens();ONE=ctx.constant(1);ZERO=ctx.constant(0)
STAT={'exactProducts':0,'monicOriginalReturns':0,'newMonicDivisions':0,
      'newOriginalColumns':0,'newColumnCoordinates':0,
      'newCofactorCoordinates':0,'threeOriginalFullReturns':0,
      'finalOldPaidDenominators':0}
def pp(p):
 return {'degrees':list(map(int,p.degrees())) if p else [-1]*4,
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(p.to_dict()),
         'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 STAT['exactProducts']+=1;return q
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=ONE if d is None else poly(d);assert d
  if not n:self.n=ZERO;self.d=ONE;return
  if reduce:
   g=n.gcd(d);n=exact(n,g);d=exact(d,g)
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __neg__(self):return R(-self.n,self.d,False)
 def __add__(self,v):
  v=R(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=exact(self.d,g);b=exact(v.d,g)
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R(exact(self.n,g)*exact(v.n,h),
           exact(self.d,h)*exact(v.d,g),False)
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
def rp(v):
 v=R(v);return {'numerator':pp(v.n),'denominator':pp(v.d)}
def weight(p):return all(not any(map(int,e[2:])) for e in p.to_dict())
def oldpaid(v,final=False):
 v=R(v);assert weight(v.d)
 d=v.d
 while int(d.total_degree())>0:
  g=d.gcd(PAID)
  if int(g.total_degree())==0:break
  d=exact(d,g)
 assert d and int(d.total_degree())==0,('unpaid denominator',pp(d))
 if final:STAT['finalOldPaidDenominators']+=1
 return v
def gd(v):
 v=oldpaid(v)
 return max((int(e[2])+int(e[3]) for e in v.n.to_dict()),default=-1)
def coeffs(v,index):
 v=oldpaid(v);groups={}
 for ex,c in v.n.to_dict().items():
  j=int(ex[index]);ee=list(ex);ee[index]=0
  groups.setdefault(j,{})[tuple(ee)]=c
 return [R(ctx.from_dict(groups.get(j,{})),v.d)
         for j in range(max(groups,default=-1)+1)]
def rebuild(v,x):
 out=R()
 for a in reversed(v):out=out*x+a
 return out
def trim(v):
 while v and not v[-1]:v.pop()
 return v
def monic_div(value,divisor,index):
 aa=trim(coeffs(value,index));bb=trim(coeffs(divisor,index))
 assert bb and bb[-1]==1
 qq=[R() for _ in range(max(0,len(aa)-len(bb)+1))]
 while aa and len(aa)>=len(bb):
  tick();k=len(aa)-len(bb);lc=aa[-1];qq[k]+=lc
  for j,bj in enumerate(bb):aa[k+j]-=lc*bj
  aa=trim(aa)
 x=(u,Q,lam,sigma)[index]
 quotient,remainder=rebuild(qq,x),rebuild(aa,x)
 assert value==quotient*divisor+remainder
 STAT['newMonicDivisions']+=1
 return quotient,remainder
def sigdegree(v):
 v=oldpaid(v)
 assert all(int(e[2])==0 for e in v.n.to_dict())
 return max((int(e[3]) for e in v.n.to_dict()),default=-1)
def leading_sigma(v):
 cs=coeffs(v,3)
 return cs[-1] if cs else R()

u,Q,lam,sigma=map(R,(up,Qp,lp,sp))
s=u-1;delta=1-Q;Kw=Q+4*s;L=Q-2*s*(u-2);ell=L/Q;m=u-ell
a0=1-ell;T0=-Kw;JminusQ=-4*s*s;P02=2*s*L
PAID=Qp*(up-1)*(Qp+4*(up-1))
# Only three old denominator supports, used in the displayed compact source.
# No division by M, m, ell, delta, lambda, sigma, t, D or any new head.
beta=R(3)/2-lam-sigma
e=L*(1-beta)-u*Q*sigma
D0=JminusQ*T0
F=P02*T0*lam-P02*e+s*T0*T0
f=F/D0;Er=P02*e/(Q*T0)
Cf=-1+2*a0*beta*beta-4*s*beta*sigma+4*s*s*sigma*sigma
Cu=(1-2*a0*beta+2*s*sigma)*(beta-2*s*sigma)
Pcompact=(f*Cf+u*Cu+2*Er*beta*(beta+2*sigma)
          -T0*sigma*(1-2*a0*beta)+2*lam*P02*sigma*sigma)
Cfh=-Q+2*(Q-L)*beta*beta-4*s*Q*beta*sigma+4*s*s*Q*sigma*sigma
Cuh=(Q-2*(Q-L)*beta+2*s*Q*sigma)*(beta-2*s*sigma)
C=(F*Cfh+D0*u*Cuh+2*JminusQ*P02*e*beta*(beta+2*sigma)
   -D0*T0*sigma*(Q-2*(Q-L)*beta)
   +2*D0*Q*lam*P02*sigma*sigma)
assert C.d==ONE and C==Q*D0*Pcompact and gd(C)<=3
a=lam-R(3)/2
A2=2*lam*lam-2*lam+1
B3=4*lam**3-6*lam*lam+3*lam-1
E2=ell*delta*sigma*sigma-2*m*a*sigma+ell*a*a-A2
E3=ell*a**3-3*m*a*a*sigma+3*ell*delta*a*sigma*sigma-m*delta*sigma**3-B3
q=(lam**3+(m*sigma-1)*lam*lam/2
   -(1+3*m*sigma+2*ell*delta*sigma*sigma)*lam/2
   +R(1)/4+9*m*sigma/8+3*ell*delta*sigma*sigma/2
   +m*delta*sigma**3/2)
assert q==-(E3-a*E2)/2
assert len(coeffs(q,2))==4 and coeffs(q,2)[3]==1 and gd(q)<=3
STAT['monicOriginalReturns']+=1
original=[oldpaid(E2),oldpaid(E3),oldpaid(C)]
raw=[v.n for v in original]
labels=['complete_second_moment','complete_third_moment',
        'new_small_complete_NV_numerator']
# q = sum(qtags[i]*raw[i]), an ordinary original identity.
qtags=[a/(2*E2.d),-R(1)/(2*E3.d),R()]
assert q==sum((qtags[i]*R(raw[i]) for i in range(3)),R())
STAT['monicOriginalReturns']+=1
say('new_original_monic_lambda_cubic_and_small_complete_NV_definitions',
    originalLabels=labels,originalProfiles=[rp(v) for v in original],
    monicLambdaCubic=rp(q),monicOriginalMultipliers=[rp(v) for v in qtags],
    completeNVScale=rp(Q*D0),minimalPaidSupport=pp(PAID),
    noMOrNewHeadInverse=True,noPhysicalTZeroSpecialization=True,
    noOldTwentyOrEightColumnGate=True)
tick()
basis=[R(1),lam,lam*lam]
columns=[];tags=[];metadata=[]
# Fixed source order: E2,lambda E2,lambda^2 E2,C,lambda C,lambda^2 C.
for source_index,degree in [(0,2),(2,3)]:
 for j in range(3):
  value=(lam**j)*original[source_index]
  quotient,rem=monic_div(value,q,2)
  cs=coeffs(rem,2);assert len(cs)<=3
  cs=cs+[R()]*(3-len(cs))
  omega=[-quotient*qtags[i] for i in range(3)]
  omega[source_index]+=(lam**j)/original[source_index].d
  assert rem==sum((omega[i]*R(raw[i]) for i in range(3)),R())
  assert rem==sum((cs[i]*basis[i] for i in range(3)),R())
  for i in range(3):
   assert sigdegree(cs[i])<=degree+j-i
   oldpaid(omega[i])
  columns.append(cs);tags.append(omega)
  metadata.append({'originalIndex':source_index,'lambdaPower':j,
                   'sigmaDegrees':[sigdegree(v) for v in cs],
                   'profiles':[rp(v) for v in cs]})
  STAT['newOriginalColumns']+=1;STAT['newColumnCoordinates']+=3
say('new_exact_same_point_three_by_six_original_columns',
    freeAmbientBasis=['1','lambda','lambda^2'],
    exactOriginalSubsystem=['E2','E3','complete_NV'],
    columns=metadata,statistics=STAT)
def det2(a,b,c,d):return a*d-b*c
def lcm(a,b):return exact(a,a.gcd(b))*b
# No adaptive cofactor choices, no scalar ideal test or gcd.
GROUPS=[([0,1,3],5),([0,3,4],6)]
for index,(group,bound) in enumerate(GROUPS):
 tick()
 mat=[[columns[j][i] for j in group] for i in range(3)]
 co=[det2(mat[1][1],mat[1][2],mat[2][1],mat[2][2]),
     -det2(mat[1][0],mat[1][2],mat[2][0],mat[2][2]),
      det2(mat[1][0],mat[1][1],mat[2][0],mat[2][1])]
 scalar=sum((mat[0][j]*co[j] for j in range(3)),R())
 for i in range(3):
  assert sum((mat[i][j]*co[j] for j in range(3)),R())==(scalar if i==0 else R())
  STAT['newCofactorCoordinates']+=1
 assert sigdegree(scalar)<=bound
 omega=[sum((co[j]*tags[group[j]][i] for j in range(3)),R()) for i in range(3)]
 assert scalar==sum((omega[i]*R(raw[i]) for i in range(3)),R())
 STAT['threeOriginalFullReturns']+=1
 if not scalar:
  say('new_prescribed_three_column_scalar_identically_zero',
      index=index,group=group,sigmaDegreeUpperBound=bound,
      allThreeOriginalMultipliersReturned=True,
      allWeightFibersRetained=True,statistics=STAT)
  continue
 den=scalar.d
 for v in omega:den=lcm(den,v.d)
 Op=[exact(den,v.d)*v.n for v in omega]
 S=exact(den,scalar.d)*scalar.n
 assert S==sum((Op[i]*raw[i] for i in range(3)),ZERO)
 STAT['threeOriginalFullReturns']+=1
 common=ZERO
 for oi in Op:
  if oi:common=oi if not common else common.gcd(oi)
 assert common
 common=common/common.coefficient(0)
 Op=[exact(oi,common) if oi else ZERO for oi in Op]
 S=exact(S,common)
 assert S==sum((Op[i]*raw[i] for i in range(3)),ZERO)
 STAT['threeOriginalFullReturns']+=1
 assert all(int(ex[2])==0 for ex in S.to_dict())
 paid_removed=ONE
 while S and int(S.total_degree())>0:
  gp=S.gcd(PAID)
  if int(gp.total_degree())==0:break
  S=exact(S,gp);paid_removed*=gp
 # Rational constant normalization only; old-paid support is returned
 # into ALL three final multipliers, including the complete NV scale.
 lc=S.coefficient(0);S=S/lc
 Omega=[R(oi,paid_removed*lc) for oi in Op]
 assert R(S)==sum((Omega[i]*R(raw[i]) for i in range(3)),R())
 STAT['threeOriginalFullReturns']+=1
 full=[Omega[0]*E2.d,Omega[1]*E3.d,Omega[2]*Q*D0]
 assert R(S)==full[0]*E2+full[1]*E3+full[2]*Pcompact
 STAT['threeOriginalFullReturns']+=1
 for v in full:oldpaid(v,True)
 final_degree=sigdegree(R(S));assert final_degree<=bound
 head=leading_sigma(R(S))
 say('new_prescribed_three_original_sigma_scalar_returned',
     index=index,group=group,sigmaDegreeUpperBound=bound,
     actualSigmaDegree=final_degree,scalar=pp(S),sigmaHead=rp(head),
     allThreeActualOriginalMultipliers=[rp(v) for v in full],
     allThreeMultiplierCommon=pp(common),clearedDenominator=pp(den),
     oldPaidRemoved=pp(paid_removed),
     originalSourceOrder=['E2','E3','complete_N4_of_physical_vector'],
     completeOriginalThreeSourceIdentityReturned=True,
     commonZeroLocusPreserved=True,allUnpaidWeightHeadsRetained=True,
     sigmaHeadUnitNotAsserted=True,noScalarGcdOrExclusionComputed=True,
     statistics=STAT)
say('new_second_head_small_monic_lambda_three_by_six_input_complete',
    fixedGroups=[g for g,bound in GROUPS],statistics=STAT,
    onlyNecessaryOriginalSubsystem=True,
    physicalTAndOtherMeansAndValuesAllRetained=True,
    noOldProofGateReplayed=True)

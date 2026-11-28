#!/usr/bin/env python3
"""NEW corrected Phi: the WHOLE second full-NV t-leading factor.
Two original monics q_sigma and q_t give a genuinely free four-generator
ambient algebra over the OLD paid weight ring[lambda], with all nilpotents.
J7=(E2,Rcal,EBe,EBo,N1,E3,COMPLETE NV) is represented by twenty actual
same-point columns. Only three fixed NEW four-column cofactors are formed:
[R,sigma R,EBe,N1], [R,sigma R,EBe,E3], [R,sigma R,EBe,NV].
Every cofactor is merged back into SEVEN ORIGINAL polynomial numerators
before common multiplier cancellation and old-paid support removal.
No generic gcd, factorization, lambda-head inversion, prime, selected root,
D inverse, prior first-head scalar target, Q extraction, or old matrix gate.
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
ctx=fmpq_mpoly_ctx.get(('u','Q','lambda','sigma','t'),'lex')
up,Qp,lp,sp,tp=ctx.gens();ONE=ctx.constant(1);ZERO=ctx.constant(0)
stats={'exactProducts':0,'newOriginalCoordinateReturns':0,
 'newMonicIdentities':0,'newMonicDivisionReturns':0,
 'newColumnRawReturns':0,'newColumnCoordinates':0,
 'newCofactorCoordinates':0,'newSevenSourceReturns':0,
 'newFinalDenominatorReturns':0}
def pp(p):
 return {'degrees':list(map(int,p.degrees())) if p else [-1]*5,
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(p.to_dict()),
         'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 stats['exactProducts']+=1;return q
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
def oldpaid(v):
 v=R(v);assert weight(v.d)
 a=v.d
 while int(a.total_degree())>0:
  g=a.gcd(PAID)
  if int(g.total_degree())==0:break
  a=exact(a,g)
 assert a and int(a.total_degree())==0,('unpaid original denominator',pp(a))
 return v
def geo(v):
 v=oldpaid(v)
 return max((sum(map(int,e[2:])) for e in v.n.to_dict()),default=-1)
def only_lambda(v):
 v=oldpaid(v)
 assert all(not any(map(int,e[3:])) for e in v.n.to_dict())
 return max((int(e[2]) for e in v.n.to_dict()),default=-1)
u,Q,lam,sigma,t=map(R,(up,Qp,lp,sp,tp))
s=u-1;delta=1-Q;L=Q-2*s*(u-2);ell=L/Q;m=u-ell
T0=2*u-ell*Q-2*u*u;J=2*u*(1-u)+ell*Q
P02=2*s*ell*Q;M=ell*(2*u-ell*Q)-u*u;bc=M/(4*delta)
Kw=Q+4*s;Mn=Q*M
# A deliberately minimal old-unit list. No m, u, 2ell-1, new head or D
# is needed by these formulae. Every actual denominator is checked.
PAID=Qp*(1-Qp)*(up-1)*Kw.n*L.n*Mn.n
a=lam-R(3)/2
T=ell*a-m*sigma
Er=P02*(T+ell)/T0
f=(P02*lam-Q*Er+s*T0)/(J-Q)
V=f+bc*t-Er
A1=2*f-2*V+2*bc*t;W1=T0/2+2*u*f
theta=u-ell*Q;x=(theta*V-m*W1)/M;y=(ell*W1-u*V)/M
w=lam-1-T
for value in [T,Er,f,V,A1,W1,x,y,w]:oldpaid(value)
assert J-Q==-4*s*s and T0==-Kw and A1==2*Er
assert lam==(J*f-Q*V+bc*Q*t-s*T0)/P02
assert T==-ell+T0*(f-V+bc*t)/P02
assert ell*(3-2*lam)+2*T+2*m*sigma==0
stats['newOriginalCoordinateReturns']+=6
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __neg__(self):return E(-self.a,-self.b)
 def __add__(self,v):
  v=E(v);return E(self.a+v.a,self.b+v.b)
 __radd__=__add__
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
p=E(1,1);qroot=p.conj();X=E(x,y);Y=X.conj()
r=X-aw*p-c*E(t);rr=Y-aw*qroot-b*E(t)
rows=[[E(),E(),p,qroot],[E(),E(A1),r,rr],
      [p,r,E(),E(t)],[qroot,rr,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,w):return [v[i]+w[i] for i in range(4)]
def vs(a,v):return [a*x for x in v]
def vm(v,w):return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tr(v):return aw*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tr(vm(row,v)) for row in rows]
d=DK(one);F2=tr(d);Kd=DK(d)
def N4(v):
 vv=vm(v,v);tv=tr(v)
 return 2*tr(vm(d,vv))-F2*tr(vv)-4*tv*tr(vm(d,v))+2*F2*tv*tv+tr(vm(v,DK(v)))
def center(v):return va(v,vs(-tr(v),one))
def mean(j):
 sq=2*tr(vm(rows[0],rows[1])) if j==1 else tr(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
E1=mean(1);EB=mean(2);EC=mean(3)
assert EC==EB.conj() and not E1.b
Rcal=4*(f-u)*(V-f)+bc*t*t+t*(4*bc*u-ell*V+m*(T0+4*u*f-2*V)/(2*delta))
assert E(2*Rcal)+E1-b*EB-c*EC==E()
E0=2*W1-T0-4*u*f;n0=N4(rows[0])-E(2*lam*P02)
cv0,cv1=center(rows[0]),center(rows[1])
Pjet=3*tr(vm(vm(cv0,cv0),cv1))
assert F2==E(2*f) and not E0 and not n0
assert Pjet==E(3*w*P02)
N1e=N4(va(rows[0],rows[1]))-N4(rows[0])-N4(rows[1])-E(4*lam*w*P02)
assert not N1e.b
N1=N1e.a
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
h=E(1+T/ell+m*sigma/ell,-sigma);k=h.conj()
assert h==E(lam-R(1)/2,-sigma)
vphys=[E(1),E(w),h,k]
E2e=b*(h-1)**2+c*(k-1)**2-E(A2)
E3e=b*(h-1)**3+c*(k-1)**3-E(B3)
NVe=N4(vphys)
assert not E2e.b and not E3e.b and not NVe.b
E2,E3,NV=E2e.a,E3e.a,NVe.a
assert E2==ell*delta*sigma*sigma-2*m*a*sigma+ell*a*a-A2
assert E3==ell*a**3-3*m*a*a*sigma+3*ell*delta*a*sigma*sigma-m*delta*sigma**3-B3
assert all(int(ex[4])==0 for ex in NV.n.to_dict())
stats['newOriginalCoordinateReturns']+=12

def trim(v):
 v=list(v)
 while v and not v[-1]:v.pop()
 return v
def coeffs(v,index):
 v=oldpaid(v);groups={}
 for ex,cc in v.n.to_dict().items():
  j=int(ex[index]);ee=list(ex);ee[index]=0
  groups.setdefault(j,{})[tuple(ee)]=cc
 return trim([R(ctx.from_dict(groups.get(j,{})),v.d)
              for j in range(max(groups,default=-1)+1)])
def rebuild(v,x):
 out=R()
 for q0 in reversed(v):out=out*x+q0
 return out
def at(v,index,degree):
 cc=coeffs(v,index);return cc[degree] if degree<len(cc) else R()
def monic_div(value,divisor,index):
 # Ordinary polynomial division in the declared variable only.
 # The other variables remain coefficients; no nonconstant inverse.
 aa=coeffs(value,index);bb=coeffs(divisor,index);assert bb and bb[-1]==1
 quo=[R() for _ in range(max(0,len(aa)-len(bb)+1))]
 while aa and len(aa)>=len(bb):
  tick();shift=len(aa)-len(bb);lc=aa[-1];quo[shift]+=lc
  for j,bj in enumerate(bb):aa[j+shift]-=lc*bj
  aa=trim(aa)
 var=[u,Q,lam,sigma,t][index]
 quotient=rebuild(quo,var);remainder=rebuild(aa,var)
 assert value==quotient*divisor+remainder
 stats['newMonicDivisionReturns']+=1
 return quotient,remainder
aR=-bc*s*(2*u-3)/delta
aO=m*(Q+2*s*s)/(4*delta*delta)
Bq=Q*Q+(2*u*u-3)*Q+2*s*(2*u-1)*(u-2)
gammaR=-Bq/(ell*bc*s*Q);gammaO=-8*delta/ell
assert at(Rcal,4,2)==aR and at(EB.b,4,2)==aO
assert Q*(2*m*(Q+2*s*s)+ell*delta)==(2*u-3)*Bq
assert gammaR*aR+gammaO*aO==1
qt=gammaR*Rcal+gammaO*EB.b
assert len(coeffs(qt,4))==3 and at(qt,4,2)==1 and geo(qt)<=2
qs=sigma*sigma-2*m*a*sigma/(ell*delta)-(A2-ell*a*a)/(ell*delta)
assert E2==ell*delta*qs and len(coeffs(qs,3))==3 and at(qs,3,2)==1
ws,qt_tilde=monic_div(qt,qs,3)
assert qt==qt_tilde+ws*qs and at(qt_tilde,4,2)==1
assert all(int(ex[3])<=1 for ex in qt_tilde.n.to_dict())
stats['newMonicIdentities']+=8
original=[oldpaid(x) for x in [E2,Rcal,EB.a,EB.b,N1,E3,NV]]
labels=['second_moment','mean_R','mean_even','mean_odd','N1','third_moment','complete_NV']
raw=[v.n for v in original]
assert all(geo(v)<=2 for v in original[:5])
assert geo(E3)<=3 and geo(NV)<=3
say('new_second_NV_head_original_two_monic_chart',
 head='ell*(3-2*lambda)+2*T+2*m*sigma',
 originalLabels=labels,originalProfiles=[rp(v) for v in original],
 monicSigma=rp(qs),monicT=rp(qt_tilde),
 monicTOriginalMultipliers=[rp(gammaR),rp(gammaO)],
 triangularMonicCorrection=rp(ws),
 freeAmbientBasis=['1','sigma','t','sigma*t'],
 correctedTrueDualMeanIdentityReturned=True,
 physicalTNotSpecializedToZero=True,
 noDOrNewHeadInverse=True)
tick()

basis=[R(1),sigma,t,sigma*t];basis_degrees=[0,1,1,2]
def four_coordinates(v):
 v=oldpaid(v);groups=[{}, {}, {}, {}]
 for ex,cc in v.n.to_dict().items():
  i,j=int(ex[3]),int(ex[4]);assert i<2 and j<2
  ee=list(ex);ee[3]=ee[4]=0
  groups[i+2*j][tuple(ee)]=cc
 out=[R(ctx.from_dict(g),v.d) for g in groups]
 assert v==sum((out[i]*basis[i] for i in range(4)),R())
 return out
def reduce_to_original(value):
 # value = remainder + U*E2 + V*Rcal + W*EBo, in the ordinary ring.
 # qt_tilde = qt - ws*qs, qt=gammaR*Rcal+gammaO*EBo.
 qt_mult,rr0=monic_div(value,qt_tilde,4)
 qs_mult,rem=monic_div(rr0,qs,3)
 U=(qs_mult-qt_mult*ws)/(ell*delta)
 Vtag=qt_mult*gammaR;Wtag=qt_mult*gammaO
 for x0 in [U,Vtag,Wtag]:oldpaid(x0)
 assert value==rem+U*E2+Vtag*Rcal+Wtag*EB.b
 out=four_coordinates(rem)
 stats['newColumnRawReturns']+=1
 stats['newColumnCoordinates']+=4
 return out,[U,Vtag,Wtag]
# EXACT source order and all twenty columns are fixed before execution.
seed_indices=[1,2,4,5,6]
seed_degrees=[2,2,2,3,3]
columns=[];traces=[];meta=[]
for si,(oi,gd) in enumerate(zip(seed_indices,seed_degrees)):
 block=[]
 for bi,monomial in enumerate(basis):
  cc,tag=reduce_to_original(monomial*original[oi])
  for row in range(4):
   assert only_lambda(cc[row])<=gd+basis_degrees[bi]-basis_degrees[row]
  columns.append(cc);traces.append(tag);meta.append((oi,bi))
  block.append([rp(v) for v in cc])
 say('new_second_NV_head_four_original_columns',
     seed=labels[oi],fixedColumnIndices=list(range(4*si,4*si+4)),
     columns=block,completeOrdinaryOriginalReturns=4,
     totalGeometricDegreeBound=gd,
     everyOriginalWeightPoleOldPaid=True)
 tick()
assert len(columns)==20

def det3(A):
 return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
        -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
        +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
FIXED=[('mean_N1', [0,1,4,8],5),
       ('mean_third_moment',[0,1,4,12],6),
       ('mean_complete_NV',[0,1,4,16],6)]
finished=[]
for label,indices,bound in FIXED:
 tick()
 matrix=[[columns[j][i] for j in indices] for i in range(4)]
 # Adjugate column adj(matrix)*e0; no determinant or head is inverted.
 omega=[]
 for j in range(4):
  submatrix=[[matrix[i][k] for k in range(4) if k!=j] for i in range(1,4)]
  omega.append((-1)**j*det3(submatrix))
 target=sum((matrix[0][j]*omega[j] for j in range(4)),R())
 for i in range(4):
  assert sum((matrix[i][j]*omega[j] for j in range(4)),R())==(target if i==0 else R())
  stats['newCofactorCoordinates']+=1
 assert only_lambda(target)<=bound
 # Merge every normal-form source BEFORE deciding common cancellation.
 coefficients=[R() for _ in range(7)]
 for j,ci in enumerate(indices):
  oi,bi=meta[ci];tag=traces[ci];c0=omega[j]
  coefficients[oi]+=c0*basis[bi]
  coefficients[0]-=c0*tag[0]
  coefficients[1]-=c0*tag[1]
  coefficients[3]-=c0*tag[2]
 assert target==sum((coefficients[i]*original[i] for i in range(7)),R())
 stats['newSevenSourceReturns']+=1
 if not target:
  say('new_second_NV_head_fixed_original_cofactor_zero',
      label=label,indices=indices,lambdaUpperBound=bound,
      completeFourCoordinateAndSevenOriginalReturn=True,
      allOriginalFibersRetained=True,wholeHeadExcluded=False)
  finished.append({'label':label,'zero':True})
  continue
 raw_coeff=[oldpaid(coefficients[i]/original[i].d) for i in range(7)]
 assert target==sum((raw_coeff[i]*R(raw[i]) for i in range(7)),R())
 stats['newSevenSourceReturns']+=1
 denominator=ONE
 for v in raw_coeff+[target]:
  oldpaid(v)
  denominator=exact(denominator,denominator.gcd(v.d))*v.d
 Om=[v.n*exact(denominator,v.d) for v in raw_coeff]
 rhs=target.n*exact(denominator,target.d)
 assert sum((Om[i]*raw[i] for i in range(7)),ZERO)==rhs
 stats['newSevenSourceReturns']+=1
 common=ZERO
 for p0 in Om:common=common.gcd(p0)
 assert common
 Om=[exact(p0,common) for p0 in Om];rhs=exact(rhs,common)
 assert sum((Om[i]*raw[i] for i in range(7)),ZERO)==rhs
 stats['newSevenSourceReturns']+=1
 # Only the declared old physical units are now removed.
 removed=ONE
 while rhs and int(rhs.total_degree())>0:
  gg=rhs.gcd(PAID)
  if int(gg.total_degree())==0:break
  rhs=exact(rhs,gg);removed*=gg
 lc=rhs.coefficient(0);rhs/=lc;removed*=lc
 final=[oldpaid(R(v,removed)) for v in Om]
 assert sum((final[i]*R(raw[i]) for i in range(7)),R())==R(rhs)
 stats['newSevenSourceReturns']+=1
 stats['newFinalDenominatorReturns']+=7
 degree=only_lambda(R(rhs));assert degree<=bound
 lead=at(R(rhs),2,degree) if degree>=0 else R()
 say('new_second_NV_head_fixed_seven_original_scalar',
     label=label,indices=indices,lambdaUpperBound=bound,
     actualLambdaDegree=degree,scalar=pp(rhs),lambdaLeadingCoefficient=rp(lead),
     commonOfAllSevenActualOriginalMultipliers=pp(common),
     initialFinalDenominator=pp(denominator),
     removedOnlyOldPaidUnits=pp(removed),
     sevenFinalOriginalMultipliers=[rp(v) for v in final],
     fourAdjugateCoordinatesReturned=True,
     completeSevenOriginalPolynomialIdentityReturned=True,
     everyCommonAndNewHeadZeroFiberRetained=True,
     noGenericUnivariateScalarGcdOrFactorizationOrPrime=True,
     wholeHeadExcluded=(int(rhs.total_degree())==0))
 finished.append({'label':label,'zero':False,'lambdaDegree':degree,
                  'oldPaidScalarUnit':int(rhs.total_degree())==0,'sha256':pp(rhs)['sha256']})
 tick()
say('new_second_NV_head_four_generator_input_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 basis=['1','sigma','t','sigma*t'],sourceCount=7,originalColumnCount=20,
 fixedCofactors=finished,statistics=stats,
 exactAmbientAndSamePointIdealPresentation=True,
 NSPSAndRemainingIndividualOriginalConditionsRetained=True,
 allUnpaidWeightOrLambdaHeadsRetained=True,
 noFirstHeadGcdReplay=True,
 wholeHeadExcludedByReturnedOriginalUnit=any(v.get('oldPaidScalarUnit',False) for v in finished),
 wholePhiExcluded=False,noExclusionFromDegreeOrProfileAlone=True)

#!/usr/bin/env python3
"""NEW correct Phi original full-NV t-leading factor T+u*sigma=0.
All original second/third moments and COMPLETE N4 use the SAME sigma.
Recover f,V from the true E0/N0/P1 coordinates; no t/D/sigma/V2 inverse.
On this whole head chart q is monic in lambda. Reduce only E3 and full NV.
Three NEW same-lambda scalars (norm E3, cross, norm NV), then one fixed
QQ(u,Q)[sigma] gcd and terminal THREE ORIGINAL multiplier cancellation.
All new pure-weight zero fibers survive in the actual final cover.
No old Q extraction, axis comparison, weighted/value cofactor, or
same-sigma N/P-cross gate is called. Self-contained; 120 sec / 1 GiB.
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
 'newMonicMomentReturns':0,'newLambdaDivisionReturns':0,
 'newScalarOriginalReturns':0,'newGcdDivisionReturns':0,
 'newGcdSourceReturns':0,'newTerminalOriginalReturns':0}
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
u,Q,lam,sigma,t=map(R,(up,Qp,lp,sp,tp))
s=u-1;delta=1-Q;L=Q-2*s*(u-2);ell=L/Q;m=u-ell
T0=2*u-ell*Q-2*u*u;J=2*u*(1-u)+ell*Q
P02=2*s*ell*Q;M=ell*(2*u-ell*Q)-u*u;bc=M/(4*delta)
Kw=Q+4*s;Mn=Q*M
PAID=up*Qp*(1-Qp)*(up-1)*Kw.n*L.n*Mn.n*(2*ell-1).n*m.n
# This is the WHOLE first factor of the complete original NV t head.
# Neither sigma nor u is used as a geometric divisor.
T=-u*sigma
Erestore=P02*(T+ell)/T0
f=(P02*lam-Q*Erestore+s*T0)/(J-Q)
V=f+bc*t-Erestore
A1=2*f-2*V+2*bc*t
W1=T0/2+2*u*f
theta=u-ell*Q
x=(theta*V-m*W1)/M;y=(ell*W1-u*V)/M
w=lam-1-T
for value in [T,Erestore,f,V,A1,W1,x,y,w]:oldpaid(value)
assert J-Q==-4*s*s and T0==-Kw
assert lam==(J*f-Q*V+bc*Q*t-s*T0)/P02
assert T==-ell+T0*(f-V+bc*t)/P02
assert T+u*sigma==0
stats['newOriginalCoordinateReturns']+=5
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
r=X-aw*p-c*E(t);sg=Y-aw*qroot-b*E(t)
rows=[[E(),E(),p,qroot],[E(),E(A1),r,sg],
      [p,r,E(),E(t)],[qroot,sg,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(a,b):return [a[i]+b[i] for i in range(4)]
def vs(a,v):return [a*x for x in v]
def vm(a,b):return [a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[2]*b[2],a[3]*b[3]]
def tr(v):return aw*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tr(vm(row,v)) for row in rows]
d=DK(one);F2=tr(d)
def N4(v):
 vv=vm(v,v);tv=tr(v)
 return 2*tr(vm(d,vv))-F2*tr(vv)-4*tv*tr(vm(d,v))+2*F2*tv*tv+tr(vm(v,DK(v)))
def center(v):return va(v,vs(-tr(v),one))
def polar(a,b):return N4(va(a,b))-N4(a)-N4(b)
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
D=ell*A2-T*T
A0=1+T/ell
h=E(A0+m*sigma/ell,-sigma)
k=h.conj()
assert h==E(1)-E(sigma)*p and k==E(1)-E(sigma)*qroot
vphys=[E(1),E(w),h,k]
e1=[E(),E(1),E(),E()]
assert vphys==va(va(one,vs(E(-sigma),rows[0])),vs(E(w),e1))
E0=2*W1-T0-4*u*f
n0=N4(rows[0])-E(2*lam*P02)
cv0,cv1=center(rows[0]),center(rows[1])
Pjet=3*tr(vm(vm(cv0,cv0),cv1))
assert F2==E(2*f) and not E0 and not n0
assert Pjet==E(3*w*P02)
assert N4(e1)==E(4*(f-u))
assert polar(one,e1)==E(2*(u-2*f))
assert polar(one,rows[0])==E(T0+E0)
assert polar(rows[0],e1)==E(-2*E0)
stats['newOriginalCoordinateReturns']+=10
fullNV=N4(vphys)
NV=oldpaid(fullNV.a)
assert not fullNV.b
smallNV=2*lam*P02*sigma*sigma+4*(f-u)*w*w-T0*sigma+2*(u-2*f)*w
assert NV==smallNV
assert all(int(ex[4])==0 for ex in NV.n.to_dict())
assert geo(NV)<=3
stats['newOriginalCoordinateReturns']+=2
V2=2*u-ell*Q;V3=2*V2-u*Q
E2=b*(h-1)**2+c*(k-1)**2-E(A2)
E3=b*(h-1)**3+c*(k-1)**3-E(B3)
assert not E2.b and not E3.b
assert E2.a==V2*sigma*sigma-A2
assert E3.a==-V3*sigma**3-B3
quad=lam*lam-lam+(1-V2*sigma*sigma)/2
assert quad==-E2.a/2
stats['newMonicMomentReturns']+=3
# These are the only new original equations used by this first target.
original=[oldpaid(E2.a),oldpaid(E3.a),NV]
raw=[v.n for v in original]
say('new_whole_NV_first_t_head_original_chart',
 head='T+u*sigma',originalCoordinatesReturned=True,
 sameSigmaFullMomentsReturned=True,completeNVFromTrueGramReturned=True,
 originalRawProfiles=[rp(v) for v in original],
 monicLambdaQuadratic=rp(quad),smallCompleteNV=rp(smallNV),
 noInverseOfDOrSigmaOrV2OrV3OrAnyNewHead=True,
 remainingSecondNVtHeadAndOtherOriginalConditionsRetained=True)
tick()

def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 return trim([(a[i] if i<len(a) else R())+(b[i] if i<len(b) else R())
              for i in range(max(len(a),len(b)))])
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def scale(a,c):return trim([x*c for x in a])
def mul(a,b):
 if not a or not b:return []
 out=[R() for _ in range(len(a)+len(b)-1)]
 for i,xv in enumerate(a):
  for j,yv in enumerate(b):out[i+j]+=xv*yv
 return trim(out)
def to_poly(v,index,only_weight_coefficients=False):
 v=R(v);assert weight(v.d)
 groups={}
 for ex,cc in v.n.to_dict().items():
  n=int(ex[index]);ee=list(ex);ee[index]=0
  groups.setdefault(n,{})[tuple(ee)]=cc
 out=[R(ctx.from_dict(groups.get(i,{})),v.d) for i in range(max(groups,default=-1)+1)]
 if only_weight_coefficients:
  assert all(weight(x.n) and weight(x.d) for x in out)
 return trim(out)
def from_poly(a,x):
 out=R()
 for c0 in reversed(a):out=out*x+c0
 return out
def pdiv(a,b,field_head):
 a=trim(a);b=trim(b);assert b
 if field_head:assert weight(b[-1].n) and weight(b[-1].d)
 else:assert b[-1]==1
 old=a[:];quo=[R() for _ in range(max(0,len(a)-len(b)+1))]
 while a and len(a)>=len(b):
  tick();shift=len(a)-len(b);cc=a[-1]/b[-1]
  quo[shift]+=cc
  for j,bj in enumerate(b):a[j+shift]-=cc*bj
  a=trim(a)
 assert add(mul(quo,b),a)==old
 stats['newGcdDivisionReturns' if field_head else 'newLambdaDivisionReturns']+=1
 return trim(quo),a
qpoly=to_poly(quad,2);assert len(qpoly)==3 and qpoly[-1]==1
rrows=[];qrows=[]
for label,value in [('third_moment',original[1]),('complete_NV',NV)]:
 quot,rem=pdiv(to_poly(value,2),qpoly,False)
 assert len(rem)<=2
 rem=rem+[R()]*(2-len(rem))
 qq=from_poly(quot,lam)
 assert value==rem[0]+rem[1]*lam+qq*quad
 rrows.append(rem);qrows.append(qq)
 say('new_first_NV_head_original_lambda_remainder',
     label=label,remainder=[rp(x) for x in rem],originalQuadraticMultiplier=rp(qq),
     completeOriginalPolynomialIdentityReturned=True)
 tick()
aH,bH=rrows[0];aV,bV=rrows[1];qh,qv=qrows
q0,q1=qpoly[:2]
partnerH=aH-bH*q1-bH*lam
partnerV=aV-bV*q1-bV*lam
normH=aH*aH-q1*aH*bH+q0*bH*bH
cross=aH*bV-aV*bH
normV=aV*aV-q1*aV*bV+q0*bV*bV
scalar_values=[normH,cross,normV]
scalar_tags=[
 [bH*bH-partnerH*qh,partnerH,R()],
 [bH*qv-bV*qh,bV,-bH],
 [bV*bV-partnerV*qv,R(),partnerV]]
base=[quad,original[1],NV]
for label,value,tag in zip(['norm_third_moment','cross_same_lambda','norm_complete_NV'],
                           scalar_values,scalar_tags):
 for x0 in tag:oldpaid(x0)
 assert value==sum((tag[i]*base[i] for i in range(3)),R())
 assert all(int(ex[2])==0 and int(ex[4])==0 for ex in value.n.to_dict())
 stats['newScalarOriginalReturns']+=1
 say('new_first_NV_head_original_sigma_scalar',
     label=label,scalar=rp(value),actualOriginalMultipliers=[rp(x0) for x0 in tag],
     completeThreeOriginalEquationIdentityReturned=True,
     noLambdaCoefficientDivided=True)
 tick()

# One fixed order only: norm(E3), cross(E3,NV), norm(NV).
# QQ(u,Q) inverses here are calculation coefficients, not physical units.
# ALL terminal denominators are carried back into the pure-weight cover.
seeds=[to_poly(v,3,True) for v in scalar_values]
g=[];gsource=[[],[],[]];used=[]
def xgcd(a,b):
 r0,r1=a[:],b[:];s0,s1=[R(1)],[];t0,t1=[],[R(1)]
 while r1:
  qq,rr=pdiv(r0,r1,True)
  r0,r1=r1,rr;s0,s1=s1,sub(s0,mul(qq,s1));t0,t1=t1,sub(t0,mul(qq,t1))
 if not r0:return [],[],[]
 invlc=1/r0[-1]
 gg=scale(r0,invlc);aa=scale(s0,invlc);bb=scale(t0,invlc)
 assert add(mul(aa,a),mul(bb,b))==gg
 stats['newGcdSourceReturns']+=1
 return gg,aa,bb
for i,seed in enumerate(seeds):
 if not seed:continue
 if not g:
  invlc=1/seed[-1];g=scale(seed,invlc);gsource[i]=[invlc]
 else:
  gg,aa,bb=xgcd(g,seed)
  gsource=[mul(aa,v) for v in gsource]
  gsource[i]=add(gsource[i],bb);g=gg
 assert sum((from_poly(gsource[j],sigma)*scalar_values[j] for j in range(3)),R())==from_poly(g,sigma)
 used.append(i)
 say('new_first_NV_head_same_sigma_gcd_step',
     index=i,gcdDegree=len(g)-1,gcd=rp(from_poly(g,sigma)),used=used,
     fullScalarSourceReturned=True,allNewWeightPolesReserved=True)
 tick()
 if len(g)==1:break
if not g:
 say('new_first_NV_head_three_scalars_all_zero',
     wholeHeadExcluded=False,allOriginalFibersRetained=True)
else:
 # Merge the fixed three scalar certificates into the THREE original
 # univariate-geometry equations before taking any final denominator.
 coefficients=[R(),R(),R()]
 for j in range(3):
  wj=from_poly(gsource[j],sigma)
  for i in range(3):coefficients[i]+=wj*scalar_tags[j][i]
 # quad=-E2/2; original raw numerators have only old-paid denominators.
 multipliers=[-coefficients[0]/(2*original[0].d),
              coefficients[1]/original[1].d,
              coefficients[2]/original[2].d]
 target=from_poly(g,sigma)
 assert target==sum((multipliers[i]*R(raw[i]) for i in range(3)),R())
 stats['newTerminalOriginalReturns']+=1
 denominator=ONE
 for v in multipliers+[target]:
  assert weight(v.d)
  denominator=exact(denominator,denominator.gcd(v.d))*v.d
 omega=[v.n*exact(denominator,v.d) for v in multipliers]
 rhs=target.n*exact(denominator,target.d)
 assert sum((omega[i]*raw[i] for i in range(3)),ZERO)==rhs
 stats['newTerminalOriginalReturns']+=1
 common=ZERO
 for p0 in omega:common=common.gcd(p0)
 assert common
 # This is common cancellation of all THREE ORIGINAL multipliers.
 omega=[exact(p0,common) for p0 in omega];rhs=exact(rhs,common)
 assert sum((omega[i]*raw[i] for i in range(3)),ZERO)==rhs
 stats['newTerminalOriginalReturns']+=1
 # Only already proved pure-weight physical units may be removed.
 removed=ONE
 while rhs and int(rhs.total_degree())>0:
  factor=rhs.gcd(PAID)
  if int(factor.total_degree())==0:break
  rhs=exact(rhs,factor);removed*=factor
 lc=rhs.coefficient(0);rhs/=lc;removed*=lc
 final=[oldpaid(R(p0,removed)) for p0 in omega]
 assert sum((final[i]*R(raw[i]) for i in range(3)),R())==R(rhs)
 stats['newTerminalOriginalReturns']+=1
 is_weight=weight(rhs)
 say('new_first_NV_head_terminal_three_original_return',
     genericSigmaGcdDegree=len(g)-1,usedScalarIndices=used,
     mergedOriginalEquations=['E2','E3','complete_NV'],
     terminalPureWeightLCM=pp(denominator),
     actualThreeOriginalCommonMultiplier=pp(common),
     finalNecessaryPolynomial=pp(rhs),
     finalThreeOriginalMultipliers=[rp(v) for v in final],
     pureWeightSupport=is_weight,
     wholeHeadExcluded=is_weight and int(rhs.total_degree())==0,
     allUnknownWeightAndGeometryZeroFibersRetained=True,
     noDOrSigmaOrV2OrV3OrNewHeadInverseUsedAsPhysicalUnit=True,
     noIndependentNormSameRootSufficiencyClaim=True)
 tick()
say('new_first_NV_t_head_original_value_target_finished',
 statistics=stats,sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 zeroDependencies=True,absoluteOriginalDeadlinePreserved=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noFrozenQOrOldCrossOrValueProjectionGateReplayed=True,
 noCoefficientPayloadOrChunksSaved=True)
signal.setitimer(signal.ITIMER_REAL,0)

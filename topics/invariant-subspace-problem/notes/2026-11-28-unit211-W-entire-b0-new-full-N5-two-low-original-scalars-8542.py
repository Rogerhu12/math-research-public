#!/usr/bin/env python3
"""NEW entire b0=0: full original N4 gives the NEW pure lambda quintic N5.
Only q2,R6 necessary definitions from the existing whole face are used.
No old fixed8/F78 computation or native matrix.  Pseudo-reduce R6 and
NEW N5 by q2 without any lambda head inverse; preserve all three actual
original multipliers.  New linear/linear and quadratic/linear scalar
combinations include N5, with exact source-coordinate returns.
180 seconds /4 GiB, self-contained, all unpaid head zero faces retained.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k','lam'),'lex')
ep,kp,lp=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
def polynomial(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=polynomial(n);d=O if d is None else polynomial(d);assert d
  if not n:self.n=Z;self.d=O;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  s=d.coefficient(0);self.n=n/s;self.d=d/s
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
e,k,lam=map(R,(ep,kp,lp))
u=e+1;Q=e*k;Vbar=u*k+2;delta=1-Q
ell=u*((k+2)**2-2*e*k)/(k*Vbar)
m=u-ell;theta=u-ell*Q;V2=2*u-ell*Q
M=ell*V2-u*u;bc=M/(4*delta)
T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
P02=(2-3*u)*V2-Q*u+2*u**3
assert M==ell*ell*delta-m*m
assert J*Phi-Pf==2*u*Q*Phi
Ast=4*u*Q-J;Cst=Ast*m*m+J*delta*ell*ell
# Astar is paid ONLY on this entire b0=0 face by the already excluded
# lambda=3/2 alternative.  It is not paid outside this face.
kap=u*Q*ell/Ast;T=-kap*(3-2*lam)
Aval=2*lam*lam-2*lam+1;Bval=4*lam**3-6*lam*lam+3*lam-1
cval=3-2*lam;w=lam-1-T
D=ell*Aval-T*T;K=ell*ell*Bval-3*ell*Aval*T+2*T**3
ad=(M*ell*ell*Q*(3-4*lam)+M*Ast*T*T
    +2*M*u*Q*cval*ell*T+D*Cst)
b0=2*m*(Ast*T+u*Q*cval*ell);assert not b0
q2=2*ad/ell
R6=M*K*K-4*m*m*D**3

# Exact f-constant input for the full original NV, not physical f=0.
G=lam*P02-(1-u)*T0;Pc=Q*P02*(ell+T)-G*T0
ts=-Pc/(bc*Q*Phi);Vs=-G/Q-Pc/(Q*Phi)
Ws=T0/2;A1s=2*G/Q
xs=(theta*Vs-m*Ws)/M;ys=(ell*Ws-u*Vs)/M
assert A1s==-2*Vs+2*bc*ts
z1=-2*(ell*cval+2*T)*ys-2*ell*w+m*T*ts/delta
z2=2*(ell*xs-m*ys-bc*ts)
Z0=(ell*ell*A1s+2*ell*u*w*(ell*cval+T)
    +2*Vs*(ell*ell+ell*cval*T+T*T)
    +2*bc*ts*(T*T-ell*ell))
N5=2*m*D*(Z0+D*z2)+M*K*z1
C4=2*m*D*ad+M*K*b0
Bpure=b0*(Z0+D*z2)-ad*z1
assert b0*N5-C4*z1==2*m*D*Bpure
# Its whole original source is the published identity
# N5=2*m*D*ell^2*NV+M*z1_full*H-2*m*D*z2_full*q
#                      -(2*f/(M*Q))*C4.
# No D/b0/norm inverse is used in this identity.

statistics={'exactPolynomialDivisionProducts':0,'originalCoordinateReturns':0,
 'pseudoDivisionSteps':0,'paidSupportProducts':0,'factorProductReturns':0,
 'newWeightGcdDivisionReturns':0}
def exact(p,g):
 v,r=divmod(p,g);assert not r and v*g==p
 statistics['exactPolynomialDivisionProducts']+=1;return v
def weight(p):return all(int(ex[2])==0 for ex in p.to_dict())
def degL(v):
 v=R(v);assert weight(v.d)
 return max((int(ex[2]) for ex in v.n.to_dict()),default=-1)
def coeffL(v,j):
 v=R(v);assert weight(v.d)
 return R(ctx.from_dict({(ex[0],ex[1],0):c for ex,c in v.n.to_dict().items()
                         if int(ex[2])==j}),v.d)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'zero':not bool(p),'degrees_e_k_lambda':list(map(int,p.degrees())) if p else [-1]*3,
         'totalDegree':int(p.total_degree()) if p else -1,'terms':len(data),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
paid_atoms=[('e',ep),('k',kp),('u',ep+1),('delta',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),('P02',P02.n),
 ('M',M.n),('whole_equal_weights_k_plus_two',kp+2),
 ('whole_ell_zero',ell.n),('whole_equal_weights_m',m.n),
 ('whole_original_Lhalf',(2*ell-1).n),
 ('Astar_paid_ONLY_on_entire_b0_zero',Ast.n)]
def strip(p):
 if not p:return p,O,[]
 before=p;removed=O;history=[]
 for label,atom in paid_atoms:
  assert atom and weight(atom);layers=0
  while p:
   gg=p.gcd(atom)
   if int(gg.total_degree())==0:break
   p=exact(p,gg);removed*=gg;layers+=1
   statistics['paidSupportProducts']+=1
  if layers:history.append({'paidSupport':label,'gcdLayers':layers})
 assert p*removed==before
 return p,removed,history
paid_seen=set()
def paid(p):
 assert p and weight(p);key=str(p)
 if key in paid_seen:return
 out,_,_=strip(p);assert out and int(out.total_degree())==0
 paid_seen.add(key)
def ck(v):v=R(v);paid(v.d);return v
for v in [q2,R6,N5,ts,Vs,xs,ys,z1,z2,Z0,Ast]:
 ck(v)
assert degL(q2)==2 and degL(R6)<=6 and degL(N5)<=5
rawbasis=[q2,R6,N5]
say('new_b0_full_N5_original_same_lambda_input',
 originalBasis=['2*aDelta/ell','R6','NEW_full_NV_pure_N5'],
 lambdaDegrees=[degL(v) for v in rawbasis],
 newN5Numerator=profile(N5.n),newN5Denominator=profile(N5.d),
 noPhysicalFZeroRestriction=True,
 AstarPaidOnlyOnWholeB0Face=True,
 fullN5OriginalSource='2*m*D*ell^2*NV+M*z1_full*H-2*m*D*z2_full*q-(2*f/(M*Q))*C4',
 noDOrLambdaHeadInverse=True,
 oldFixedEightAndF78NotRebuilt=True)
# Normalize each necessary INPUT only by existing paid pure-weight
# supports.  This avoids carrying already paid powers through new
# pseudo multiplication; its entire original scale is retained.
basis=[];basescales=[]
for label,val in zip(['q2','R6','NEW_N5'],rawbasis):
 pp,removed,hist=strip(val.n)
 if pp:
  cc=pp.coefficient(0);pp/=cc;removed*=cc
 assert pp*removed==val.n
 paid(removed)
 scale=R(val.d,removed);assert scale*val==R(pp)
 basis.append(R(pp));basescales.append(scale)
 say('new_N5_input_paid_normalization',
     label=label,polynomial=profile(pp),paidGcdLayers=hist,
     entireOriginalUnitScaleReturned=True)
q2,R6,N5=basis
def combine(tag):
 return sum((tag[i]*basis[i] for i in range(3)),R())
def check_source(value,tag):
 ret=combine(tag);assert ret==value
 assert sum((tag[i]*basescales[i]*rawbasis[i] for i in range(3)),R())==value
 for j in range(max(degL(ret),degL(value),0)+1):
  assert coeffL(ret,j)==coeffL(value,j)
  statistics['originalCoordinateReturns']+=1
def primitive(label,value,tag,cap):
 check_source(value,tag)
 den=O
 for v in tag:
  ck(v);den=exact(den,den.gcd(v.d))*v.d
 paid(den)
 nums=[v.n*exact(den,v.d) for v in tag];g=Z
 for pp in nums:g=g.gcd(pp)
 if not g:
  assert not value
  say('new_b0_three_original_multiplier_zero',label=label)
  return R(),[R(),R(),R()]
 newtag=[R(exact(pp,g)) for pp in nums]
 out=combine(newtag);ck(out)
 assert R(g)*out==R(den)*value and degL(out)<=cap
 check_source(out,newtag)
 say('new_b0_three_original_multiplier_primitive',
     label=label,lambdaDegree=degL(out),
     actualCommonMultiplier=profile(g),
     numerator=profile(out.n),denominator=profile(out.d),
     allLambdaCoordinatesReturned=True,
     entireMultiplierCommonZeroFaceRetained=True)
 return out,newtag
def prem_with_source(index,label):
 rem=basis[index];quo=R();scale=R(1)
 head=coeffL(q2,2)
 while rem and degL(rem)>=2:
  j=degL(rem)-2;lc=coeffL(rem,degL(rem))
  rem=head*rem-lc*lam**j*q2
  quo=head*quo+lc*lam**j;scale*=head
  assert scale*basis[index]==quo*q2+rem
  statistics['pseudoDivisionSteps']+=1
 tag=[-quo,R(),R()];tag[index]=scale
 return primitive(label,rem,tag,1)
R1,tagR=prem_with_source(1,'R6_pseudoremainder_FOR_NEW_N5_pair')
N1,tagN=prem_with_source(2,'NEW_N5_pseudoremainder')
a=coeffL(R1,0);b=coeffL(R1,1)
c=coeffL(N1,0);d=coeffL(N1,1)
assert R1==a+b*lam and N1==c+d*lam
newlin=d*R1-b*N1
lin,tagLin=primitive('NEW_R6_N5_linear_linear_constant',
 newlin,[d*tagR[i]-b*tagN[i] for i in range(3)],0)
assert degL(lin)<=0
def retain(label,val):
 ck(val);assert degL(val)<=0
 p,removed,hist=strip(val.n)
 if p:
  cc=p.coefficient(0);p/=cc;removed*=cc
 assert p*removed==val.n and weight(p)
 say('new_b0_retained_original_weight_condition',
     label=label,necessary=profile(p),
     onlyPaidWeightSupportRemoval=hist,
     fullClearAndSupportProductReturned=True,
     allUnpaidLeadingZeroFacesKept=True,
     wholeB0Excluded=bool(p) and int(p.total_degree())==0)
 return p
retained=[retain('NEW_R6_N5_linear_linear',lin)]
unit=bool(retained[0]) and int(retained[0].total_degree())==0
if unit:
 say('new_b0_first_scalar_is_paid_unit',
     nextQuadraticLinearTargetNotNeededAndNotRun=True)
else:
 # Fixed degree (2,1) identity on all simultaneous leading-zero fibers:
 # d^2 q2 - (A*d*lambda+B*d-A*c)*(c+d*lambda)
 #       = A*c^2-B*c*d+C*d^2.
 C,B,A=[coeffL(q2,j) for j in range(3)]
 multN=-(A*d*lam+B*d-A*c)
 target=d*d*q2+multN*N1
 expected=A*c*c-B*c*d+C*d*d
 assert target==expected
 tag=[d*d+multN*tagN[0],
      multN*tagN[1],multN*tagN[2]]
 scalar,tagScalar=primitive('NEW_fixed_quadratic_N5_linear_constant',
                           target,tag,0)
 retained.append(retain('NEW_q2_N5_fixed_three',scalar))
 unit=bool(retained[-1]) and int(retained[-1].total_degree())==0
g=Z
for p in retained:g=g.gcd(p)
if g:
 cc=g.coefficient(0);g/=cc
for p in retained:
 if p and g:
  qq=exact(p,g);assert qq*g==p
  statistics['newWeightGcdDivisionReturns']+=1
finite=bool(g) and int(g.total_degree())==0 and not unit and len(retained)==2 and all(retained)
bound=(int(retained[0].total_degree())*int(retained[1].total_degree())) if finite else None
say('new_b0_two_NEW_weight_conditions_complete_gcd',
    necessaryWeightProfiles=[profile(p) for p in retained],
    completeQQCommon=profile(g),
    wholeB0Excluded=unit,
    finiteWeightSupportProved=finite,
    affineWeightSchemeLengthUpperBound=bound,
    noGeometryFiberBoundClaimed=True,
    gcdOneNotUsedAsEmptiness=True,
    allCommonUnpaidCurveComponentsRetained=bool(g) and int(g.total_degree())>0)
# Complete factorization only of the remaining common weight support,
# which is NOT a statement of emptiness when it is a nonconstant curve.
if g and int(g.total_degree())>0:
 content,factors=g.factor();back=ctx.constant(content);facts=[]
 for pp,ex in factors:
  back*=pp**int(ex)
  facts.append({'multiplicity':int(ex),'factor':profile(pp)})
 assert back==g;statistics['factorProductReturns']+=1
 say('new_b0_common_unpaid_weight_curve_factorization',
     factors=facts,completeQQFactorProductReturned=True,
     everyNonconstantFactorZeroFiberRetained=True,wholeB0Excluded=False)
say('new_b0_full_N5_first_low_scalar_input_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=statistics,wholeB0Excluded=unit,
 noOldEightDeterminantOrF78Replayed=True,
 noOriginalEquationDividedByUnpaidHead=True,
 currentWComplementStillRetained=True,ordinaryISPClaim=False,
 noCoefficientPayloadOrCacheSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)

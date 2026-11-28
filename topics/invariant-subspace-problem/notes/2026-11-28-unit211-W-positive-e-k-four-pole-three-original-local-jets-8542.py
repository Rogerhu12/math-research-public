#!/usr/bin/env python3
"""FIRST new local original input: positive e, k residue 4, mu pole.
Compute exact order-four local jets of the SAME q2,R6,complete N5
after e=E, k=4+Y, mu=1/X. These are original equations, not gcds.
No old ray target, projection, head-stripping, or frozen job is resumed.
120 seconds, 1 GiB, exact QQ. No conclusion of local emptiness is assumed.
"""
import hashlib,json,resource,signal,time
from flint import fmpq_mpoly_ctx
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('E','Y','X'),'lex')
ep,yp,xp=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
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
e=R(ep);k=R(yp+4);lam=(1/R(xp)+3)/2
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


def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'zero':not bool(p),'degrees_E_Y_X':list(map(int,p.degrees())) if p else [-1]*3,
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(data),'sha256':hashlib.sha256(raw).hexdigest()}
def constant(p):
 return p.to_dict().get((0,0,0),0)
def integral_at_1009(p):
 return all(int(str(c).split('/')[-1])%1009 if '/' in str(c) else True
            for c in p.to_dict().values())
def trunc(p,degree):
 return ctx.from_dict({ex:c for ex,c in p.to_dict().items() if sum(ex)<=degree})
def taylor(v,degree):
 d0=constant(v.d)
 assert d0
 h=trunc(v.d/d0-O,degree)
 inv=O;power=O
 for i in range(1,degree+1):
  power=trunc(power*h,degree)
  inv+=(-1)**i*power
 ret=trunc(trunc(v.n,degree)*inv/d0,degree)
 defect=v.n-v.d*ret
 assert not trunc(defect,degree)
 return ret,defect,d0
mu=2*lam-3
assert mu==1/R(xp)
qhat=q2/(Q*mu**2)
rhat=R6/mu**6
nhat=N5/mu**5
say('new_positive_e_k_four_mu_pole_original_equations',
 variables=['E=e','Y=k-4','X=(2*lambda-3)^(-1)'],
 originalSourceBlob='47281af16fdd0ad7500ecda377c3cb9f9d65e725',
 originalSourceSHA256='e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8',
 originalScales=['q2*X^2/Q','R6*X^6','complete_N5*X^5'],
 noPhysicalFZero=True,noDInverse=True,noLambdaHeadInverse=True,
 exactContext='QQ[E,Y,X]',targetOrder=4,
 noOldRayExecutionOrGcd=True)
for label,v in [('q2_X2_over_Q',qhat),('R6_X6',rhat),('complete_N5_X5',nhat)]:
 jet,defect,d0=taylor(v,4)
 num,den=str(d0).split('/') if '/' in str(d0) else (str(d0),'1')
 assert int(num)%1009 and int(den)%1009
 say('new_complete_original_local_jet',label=label,
  numerator=profile(v.n),denominator=profile(v.d),
  denominatorAtOrigin=str(d0),denominatorUnitAt1009=True,
  constantTerm=str(constant(jet)),
  coefficientsIntegralAt1009=all(integral_at_1009(p) for p in (v.n,v.d,jet,defect)),
  completeJetOrderFour=str(jet),jetProfile=profile(jet),
  exactRemainderNumerator=profile(defect),
  originalTaylorRemainderOrderAtLeastFive=True,
  allCoordinatesRetained=True)
say('new_positive_e_k_four_local_input_completed',
 noEmptinessClaim=True,noAdditionalExecution=True,
 budgetSeconds=120,budgetBytes=1024**3)

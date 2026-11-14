#!/usr/bin/env python3
"""R298: exact central normalization through the original Kronecker resolvent.

Builds every polynomial from the curve y^2=x^3+1 and the ordinary division
recurrences.  No saved work file, numerical recognition, or prime scan is used.
The only external packages are sympy and python-flint.
"""
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)

import sympy as s,json
from pathlib import Path
r,x,y,b=s.symbols('r x y b')
def red(f):
 return s.Poly(s.expand(f),y).rem(s.Poly(y*y-x**3-b,y)).as_expr().expand()
def D(f):
 return red(-x*s.diff(f,r)+2*y*s.diff(f,x)+3*x*x*s.diff(f,y))
a=[0,r];t=-x
for j in range(2,8):
 a.append(t/s.factorial(j)-(b/s.Integer(210) if j==6 else 0));t=D(t)
E=[s.Integer(1)]
for n in range(1,8):E.append(red(sum(j*a[j]*E[n-j] for j in range(1,n+1))/n))
c=E[7]
for j in range(6):c=D(c)
c=red(c/720)
terms=s.Poly(c,r,x,y,b).terms()
universal={'terms':[[[int(k) for k in m],str(v)] for m,v in terms]}
check('universal Kronecker coefficient has fourteen terms',len(terms)==14)

from flint import fmpq_mpoly_ctx,fmpq_poly,fmpq
from pathlib import Path
import json,time
start=time.monotonic()
ctx=fmpq_mpoly_ctx.get(['A','t']);A,t=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
class E:
 def __init__(self,d=None):self.d={k:v for k,v in (d or {}).items() if v}
 def __add__(self,b):
  if not isinstance(b,E):b=C(b)
  z=self.d.copy()
  for k,v in b.d.items():z[k]=z.get(k,zero)+v
  return E(z)
 __radd__=__add__
 def __neg__(self):return E({k:-v for k,v in self.d.items()})
 def __sub__(self,b):return self+(-b if isinstance(b,E) else C(-b))
 def __rsub__(self,b):return C(b)-self
 def __mul__(self,b):
  if not isinstance(b,E):b=C(b)
  z={}
  for (i,j,k),v in self.d.items():
   for (ii,jj,kk),w in b.d.items():
    u=v*w;i0,j0,k0=i+ii,j+jj,k+kk
    if i0>=3:u*=t;i0-=3
    if j0>=2:u*=t+1;j0-=2
    if k0>=2:u*=-3;k0-=2
    key=(i0,j0,k0);z[key]=z.get(key,zero)+u
  return E(z)
 __rmul__=__mul__
 def __pow__(self,n):
  a,b=C(1),self
  while n:
   if n&1:a=a*b
   b=b*b;n//=2
  return a
 def __eq__(self,b):
  if not isinstance(b,E):b=C(b)
  return self.d==b.d

def C(x):
 if isinstance(x,(int,str,fmpq)):x=ctx.constant(fmpq(x))
 return E({(0,0,0):x})
x=E({(1,0,0):one});y=E({(0,1,0):one});d=E({(0,0,1):one});w=(d-1)*fmpq(1,2)
v=t*(t-8);NS=(y+3)*(x*x+2*w*x+4*w*w)
R1=A*x*x*y*(t-8)+w*w*v+t*NS
R2=t*t*NS*NS-(x+2*w)*v*v
R3=-y*v**3+t*NS*(x*v*v-R2)
raw=universal
powers=[[C(1)] for i in range(3)]
for i,rr in enumerate([R1,R2,R3]):
 for j in range(1,7):powers[i].append(powers[i][-1]*rr)
ans=C(0)
for (ar,bx,cy,db),coeff in raw['terms']:
 assert ar+2*bx+3*cy+6*db==13
 ans+=fmpq(coeff)*powers[0][ar]*powers[1][bx]*powers[2][cy]*v**(6*db)
const=[6*ans.d.get((0,0,j),zero) for j in range(2)]
print('trace polynomial sizes',[len(q.to_dict()) for q in const], 'elapsed',time.monotonic()-start,flush=True)
# Classical odd division polynomial, psi_even=2*y*f_even.
X=fmpq_poly([0,1]);V=X**3+1
fs={0:fmpq_poly([0]),1:fmpq_poly([1]),2:fmpq_poly([1]),3:3*X**4+12*X,4:2*(X**6+20*X**3-8)}
def dp(n):
 if n in fs:return fs[n]
 m=n//2
 if n%2:
  z1=dp(m+2)*dp(m)**3;z2=dp(m-1)*dp(m+1)**3
  if m%2==0:z1*=16*V**2
  else:z2*=16*V**2
  v=z1-z2
 else:v=dp(m)*(dp(m+2)*dp(m-1)**2-dp(m-2)*dp(m+1)**2)
 fs[n]=v;return v
D17=dp(17)
assert D17.degree()==144 and all(not D17[k] for k in range(145) if k%3)
P=fmpq_poly([D17[3*k]/17 for k in range(49)])
print('P48 ready',time.monotonic()-start,flush=True)
data={'trace_numerator_A_t_delta':[[[[int(j) for j in k],str(v)] for k,v in q.to_dict().items()] for q in const],'trace_denominator':'(t*(t-8))^13','P48':[str(q) for q in P]}
check('primitive Weber polynomial is squarefree',P.gcd(P.derivative()).degree()==0)
check('primitive Weber degree is forty-eight',P.degree()==48)

from flint import fmpq_poly,fmpq
from pathlib import Path
import json,time
start=time.monotonic()
P=fmpq_poly([fmpq(s) for s in data['P48']]);X=fmpq_poly([0,1])
class K:
 def __init__(self,a=0,b=0):
  if isinstance(a,K):self.a,self.b=a.a,a.b;return
  def cv(x):
   if isinstance(x,fmpq_poly):return x%P
   return fmpq_poly([fmpq(x)])
  self.a,self.b=cv(a),cv(b)
 def __add__(self,b):
  b=K(b);return K(self.a+b.a,self.b+b.b)
 __radd__=__add__
 def __neg__(self):return K(-self.a,-self.b)
 def __sub__(self,b):return self+-K(b)
 def __rsub__(self,b):return K(b)-self
 def __mul__(self,b):
  b=K(b);return K(self.a*b.a-3*self.b*b.b,self.a*b.b+self.b*b.a)
 __rmul__=__mul__
 def __truediv__(self,b):
  b=K(b);norm=(b.a*b.a+3*b.b*b.b)%P;g,s,_=norm.xgcd(P);assert g==fmpq_poly([1])
  return self*K((b.a*s)%P,(-b.b*s)%P)
 def __pow__(self,n):
  if n<0:return (K(1)/self)**(-n)
  a,b=K(1),self
  while n:
   if n&1:a*=b
   b*=b;n//=2
  return a
 def __eq__(self,b):
  b=K(b);return self.a==b.a and self.b==b.b
 def out(self):return [[str(v) for v in p] for p in [self.a,self.b]]
 def comp(self,v):
  aa=K(0);bb=K(0)
  for j in range(47,-1,-1):aa=aa*v+K(self.a[j]);bb=bb*v+K(self.b[j])
  return aa+d*bb
x=K(X);d=K(0,1);w=(d-1)/2;gamma=2-w;lam=-w*w
ap=-(2+3*x*K(P.derivative().derivative())/K(P.derivative())+3*x/(2*(x+1)))/289
vp=(x*(x-8))**13
apow=[ap**j for j in range(7)];xpow=[x**j for j in range(40)]
vv=[]
for poly in data['trace_numerator_A_t_delta']:
 vv.append(sum((K(fmpq(c))*apow[a]*xpow[t] for (a,t),c in poly),K(0)))
R=(vv[0]+d*vv[1])/vp
print('R ready',time.monotonic()-start,flush=True)
c=-(2+6*d)/7
U=x*x+(12-28*c)*x+7*c*c-24*c
phi=x*U**3/(gamma**6*(x+c)**6)
# The genuine CM7 image preserves the original division polynomial.
rr=K(0)
for j in range(48,-1,-1):rr=rr*phi+K(P[j])
check('true CM7 map preserves the original division polynomial',rr==0)
print('CM7 automorphism ready',time.monotonic()-start,flush=True)
# Sequential Horner compositions of the original trace column.
cur=R;res=K(0)
for j in range(48):
 res+=lam**j*cur
 cur=cur.comp(phi)
 if j%8==7:print('orbit',j+1,'elapsed',time.monotonic()-start,flush=True)
check('forty-eight original conjugates close',cur==R)
print('resolvent formed',time.monotonic()-start,flush=True)
check('actual weighted resolvent eigencharacter',res.comp(phi)==lam**(-1)*res)
six=res**6
expected=K(fmpq(15876**6,17**31))
check('exact sixth power of the full resolvent',six==expected)
check('resolvent is nonzero',res!=K(0))
# This is the finite residue action of gamma=2-omega, not an abstract generator.
mod=17
def fm(a,b):return ((a[0]*b[0]-3*a[1]*b[1])%mod,(a[0]*b[1]+a[1]*b[0])%mod)
def fp(a,n):
 z=(1,0)
 while n:
  if n&1:z=fm(z,a)
  a=fm(a,a);n//=2
 return z
gam=(11,8)
roots={fp((9,9),j) for j in range(6)}
check('CM7 residue has order 288',fp(gam,288)==(1,0) and all(fp(gam,288//q)!=(1,0) for q in [2,3]))
check('CM7 has projective order 48',next(j for j in range(1,49) if fp(gam,j) in roots)==48)
check('actual local character lambda=-omega^2',fp(gam,48)==(9,9))
check('delta local character is minus one',fp((0,1),48)==(16,0))
# All powers here are exact rational algebra, with the positive root selected
# only by the already proved Yang real-square formula.
kappa0=2**7*3**3*7**2*17**2
check('positive central constant',kappa0==48940416)
check('resolvent-to-central sixth-power transport',
      (fmpq(34**30*17**13,3**6)*expected.a[0])==fmpq(kappa0**6))
period_s=(3+d)/6
check('maximal-order period generator',period_s*(1-w)==1)
check('period sixth power',period_s**6==fmpq(-1,27))
check('complete CM-period central factor',K(1)/period_s==1-w)
output={
 'result':'R298',
 'status':'all exact checks passed',
 'checks':checks,
 'universal_c66_terms_r_x_y_b':universal['terms'],
 'original_weber_P48':data['P48'],
 'six_unit_trace_numerator_A_t_delta':data['trace_numerator_A_t_delta'],
 'six_unit_trace_denominator':data['trace_denominator'],
 'reduced_zeta_multiplier':'-(2+3*t*P48_second/P48_first+3*t/(2*(t+1)))/289',
 'cm7_gamma':'2-omega=(5-delta)/2',
 'cm7_weber_map':phi.out(),
 'six_unit_trace_reduced':R.out(),
 'full_resolvent':res.out(),
 'full_resolvent_sixth_power':six.out(),
 'resolvent_sixth_power_scalar':'15876^6/17^31',
 'positive_real_period_constant':kappa0,
 'CM_period_constant':'(1-omega)*48940416',
 'raw_real_period_weight':'102^(-m)',
 'CM_generator_period_weight':'34^(-m)',
}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(str(path))
print(str(len(checks))+' exact checks PASS')

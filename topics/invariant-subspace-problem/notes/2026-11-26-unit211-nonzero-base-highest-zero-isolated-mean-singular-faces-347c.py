#!/usr/bin/env python3
"""Original QQ exclusion of both singular N1 faces in the P0!=0,m=0 chart.
Common homogeneous normalization p+q=2 retains both kappa roots.
"""
import hashlib,json,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import time
start=time.perf_counter()
ctx=fmpq_mpoly_ctx.get(('f','g','l','u','Q'),'lex');fp,gp,lp,up,qp=ctx.gens();zero=ctx.constant(0);onep=ctx.constant(1)
class R:
 def __init__(self,x=0,d=None,reduce=True):
  if isinstance(x,R):self.n=x.n;self.d=x.d;return
  n=x if hasattr(x,'to_dict') else ctx.constant(x)
  d=onep if d is None else d
  if not n:self.n=zero;self.d=onep;return
  assert d
  if reduce:
   gg=n.gcd(d);n=n/gg;d=d/gg
  self.n=n;self.d=d
 def __add__(self,o):o=R(o);return R(self.n*o.d+o.n*self.d,self.d*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):o=R(o);return R(self.n*o.n,self.d*o.d)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);return R(self.n*o.d,self.d*o.n)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.n**n,self.d**n,False) if n>=0 else R(self.d**(-n),self.n**(-n),False)
 def iszero(self):return not self.n
ee=R(1-qp)
class Q:
 def __init__(self,x=0,y=0):
  if isinstance(x,Q):self.x=x.x;self.y=x.y
  else:self.x=R(x);self.y=R(y)
 def __add__(self,o):o=Q(o);return Q(self.x+o.x,self.y+o.y)
 __radd__=__add__
 def __neg__(self):return Q(-self.x,-self.y)
 def __sub__(self,o):return self+-Q(o)
 def __rsub__(self,o):return Q(o)+-self
 def __mul__(self,o):o=Q(o);return Q(self.x*o.x+ee*self.y*o.y,self.x*o.y+self.y*o.x)
 __rmul__=__mul__
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  r=Q(1);a=self
  while n:
   if n%2:r=r*a
   a=a*a;n//=2
  return r
 def inv(self):den=1/(self.x*self.x-ee*self.y*self.y);return Q(self.x*den,-self.y*den)
 def __truediv__(self,o):return self*Q(o).inv()
 def __rtruediv__(self,o):return Q(o)*self.inv()
 def iszero(self):return self.x.iszero() and self.y.iszero()
f=Q(R(fp));g=Q(R(gp));l=Q(R(lp));u=Q(R(up));qprod=Q(R(qp));k=Q(0,1)
p=1-k;q=1+k;a=1-l;b=(l*q-u)/(2*k);c=(u-l*p)/(2*k)
t=g/(b*c)
v2=2*u-l*qprod
W1=v2/2-u*u+2*f*u
W2=u*v2-2*u**3+f*(v2+2*u*u)-b*c*qprod*t
x=(q*W1-W2)/(b*p*(2*k));y=(W2-p*W1)/(c*q*(2*k))
r=x-a*p-c*t;s=y-a*q-b*t;A=2*f-2*b*x-2*c*y+2*b*c*t
assert A.y.iszero()
K=[[Q(0),Q(0),p,q],[Q(0),A,r,s],[p,r,Q(0),t],[q,s,t,Q(0)]]
one=[Q(1),Q(0),Q(1),Q(1)]
def add(x,y):return [xx+yy for xx,yy in zip(x,y)]
def scale(c,x):return [c*xx for xx in x]
def mul(x,y):return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
def dk(x):return [tau(mul(kk,x)) for kk in K]
d=dk(one);F=tau(d)/2
assert (F-f).iszero()
def P(x):
 z=add(x,scale(-tau(x),one));return tau(mul(mul(z,z),z))/2
def N(x):return tau(mul(add(d,scale(-F,one)),mul(x,x)))/2-tau(x)*tau(mul(d,x))+F*tau(x)**2+tau(mul(x,dk(x)))/4
def Pjet(x,y):
 z=add(x,scale(-tau(x),one));h=add(y,scale(-tau(y),one));return 3*tau(mul(mul(z,z),h))/2
def Njet(x,y):return N(add(x,y))-N(x)-N(y)
Ps=[P(K[0]),Pjet(K[0],K[1]),P(K[2]),P(K[3])]
Ns=[N(K[0]),Njet(K[0],K[1]),N(K[2]),N(K[3])]
evec=[tau(mul(K[0],K[0])),2*tau(mul(K[0],K[1])),tau(mul(K[2],K[2])),tau(mul(K[3],K[3]))]
E=add(add(evec,scale(-2,dk(d))),add(scale(-2,mul(d,d)),scale(4*F,d)))
assert E[0].iszero() and Ns[0].iszero()
vals=[E[1],E[2]+E[3],(E[2]-E[3])/k,Ns[1],Ns[2]+Ns[3],(Ns[2]-Ns[3])/k]
assert all(z.y.iszero() for z in vals)
def degree(po):return tuple(max((mm[i] for mm in po.to_dict()),default=-1) for i in range(5))
def normal(po):return po/po.leading_coefficient()
pols=[normal(z.x.n) for z in vals]

gvals=[z.x for z in vals]
gpols=pols
def spec(po,index,value):
 co={}
 for mm,cf in po.to_dict().items():
  key=tuple(0 if j==index else mm[j] for j in range(5));co[key]=co.get(key,fmpq(0))+cf*fmpq(value)**mm[index]
 return ctx.from_dict(co)
def eval_f(po,arg):
 groups={}
 for mm,cf in po.to_dict().items():
  key=(0,mm[1],mm[2],mm[3],mm[4]);groups.setdefault(mm[0],{})[key]=cf
 result=R(0)
 for i in range(max(groups,default=0),-1,-1):result=result*arg+R(ctx.from_dict(groups.get(i,{})))
 return result
def strip(po,kn):
 while po:
  gg=po.gcd(kn)
  if gg.total_degree()==0:return normal(po)
  po=po/gg
 return po
D=lp*lp*qp-2*lp*up+up*up
P0n=lp*qp*(3*up-2)+2*up**3-6*up*up+(4-qp)*up
assert (b*c-Q(R(D,4*(qp-1)))).iszero()
assert (Ps[0]-Q(R(P0n)/2)).iszero()
F1=2*fp*lp*up*qp-4*fp*up**3+4*fp*up*up-2*fp*up*qp+2*gp*up*qp-2*gp*qp-lp*lp*qp*qp+lp*qp*qp+4*up**4-8*up**3+2*up*up*qp+4*up*up-2*up*qp
F2=2*fp*lp*lp*qp*qp-4*fp*lp*up*up*qp+8*fp*up**3+4*fp*up*up*qp-8*fp*up*up-2*gp*lp*qp*qp+2*lp*lp*up*qp*qp-2*lp*lp*qp*qp+4*lp*up**3*qp-12*lp*up*up*qp-lp*up*qp*qp+8*lp*up*qp-8*up**4-2*up**3*qp+16*up**3+2*up*up*qp-8*up*up
assert normal(gpols[3])==normal(F1*F2)
assert spec(F1,3,1)==qp*(lp-1)*(2*fp-qp*lp)
assert spec(F2,2,0)==2*up*up*(2*fp*(2*up+qp-2)-(up-1)*(4*up-4+qp))

# The shared intersection u=1,l=0 is excluded by original mean alone.
inter=[strip(spec(spec(spec(gpols[i],0,0),2,0),3,1),qp*(qp-1)) for i in [0,1,2]]
assert inter[0]==zero and inter[1]==gp*gp-gp-fmpq(1,2) and inter[2]==gp*gp

import sympy as SX
F,G,L,U,Z=SX.symbols('F G L U Z')
def sx(po):
 po=normal(po)
 return SX.Add(*(SX.Rational(str(cf))*F**int(mm[0])*G**int(mm[1])*L**int(mm[2])*U**int(mm[3])*Z**int(mm[4]) for mm,cf in po.to_dict().items()))
# If the l=0 face has 2u+Q-2=0, its numerator forces u=1,Q=0.
assert SX.expand((2*U*U*(2*F*(2*U+Z-2)-(U-1)*(4*U-4+Z))).subs(Z,2-2*U)+4*U*U*(U-1)**2)==0

case_polys=[];degrees=[]
for label,idx,value,fval,kn,var,removed,wantdegrees,wantgcd in [
 ('u1',3,1,R(lp*qp)/2,qp*(qp-1)*(lp-1)*(lp*lp*qp-2*lp+1),'l',lp,[22,58,44],qp**8*(16*qp-15)**4),
 ('l0',2,0,R((up-1)*(4*up-4+qp),2*(2*up+qp-2)),up*qp*(qp-1)*(2*up+qp-2)*(2*up*up-6*up+4-qp),'u',up-1,[59,92,88],qp**45*(qp-4)**8)]:
 po=[strip(eval_f(spec(gpols[i],idx,value),fval).n,kn) for i in [0,1,2,4,5]]
 rr=[strip(po[0].resultant(pp,'g'),kn) for pp in po[1:]]
 rr=[strip(pp,removed) for pp in rr]
 last=[rr[0].resultant(pp,var) for pp in rr[1:]]
 dd=[int(degree(pp)[4]) for pp in last];assert dd==wantdegrees;degrees.append(dd)
 gg=last[0].gcd(last[1]).gcd(last[2]);assert normal(gg)==normal(wantgcd)
 case_polys.append(po)

# The only residual Q fibers are both paid in their complete original ideals.
bu=[sx(spec(po,4,fmpq(15,16))) for po in case_polys[0]]
bl=[sx(spec(po,4,4)) for po in case_polys[1]]
gbu=SX.groebner(bu,G,L,domain=SX.QQ)
gbl=SX.groebner(bl,G,U,domain=SX.QQ)
assert list(gbu)==[G*G,G*L*L-SX.Rational(32,15)*G*L+SX.Rational(16,15)*G,L**3-SX.Rational(52,15)*L*L+SX.Rational(176,45)*L-SX.Rational(64,45)]
assert gbu.reduce((SX.Rational(15,16)*L*L-2*L+1)**2)[1]==0
assert list(gbl)==[G+U/2,U*U]
print(json.dumps({'schema':'r150-unit211-P0nonzero-mzero-singular-faces-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'p+q=2,Q=pq nonzero and not one,P0 nonzero,m=0; F1=0,u=1 and F2=0,l=0 excluded with every new denominator fiber','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'secondResultantDegrees':degrees,'residualFibers':['u=1: Q=15/16 forces bc=0','l=0: Q=4 forces u=0'],'ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-start,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))

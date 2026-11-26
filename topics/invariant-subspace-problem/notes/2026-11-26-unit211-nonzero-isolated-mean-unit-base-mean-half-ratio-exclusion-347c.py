#!/usr/bin/env python3
"""Original QQ exclusion of l=0 and lambda=1/2 when u=1 and lambda=N0/P0 is nonzero.
Common homogeneous normalization p+q=2 retains both kappa roots.
"""
import hashlib,json,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import time
start=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1536*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(180,190))
ctx=fmpq_mpoly_ctx.get(('f','g','l','u','Q','lam'),'lex');fp,gp,lp,up,qp,amp=ctx.gens();zero=ctx.constant(0);onep=ctx.constant(1)
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
lam=Q(R(amp))
P0pred=(l*qprod*(3*u-2)+2*u**3-6*u*u+(4-qprod)*u)/2
v2=2*u-l*qprod
W1=v2/2-u*u+2*f*u
W2=u*v2-2*u**3+f*(v2+2*u*u)-b*c*qprod*t+2*lam*P0pred
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
assert E[0].iszero() and (Ns[0]-lam*Ps[0]).iszero() and (Ps[0]-P0pred).iszero()
Nbar=a*Ns[0]+Ns[1]+b*Ns[2]+c*Ns[3]
Pbar=a*Ps[0]+Ps[1]+b*Ps[2]+c*Ps[3]
vals=[E[1],E[2]+E[3],(E[2]-E[3])/k,3*Ns[1]-2*lam*Ps[1],Pbar-2*Nbar,Nbar-2*lam**3*Ps[0]]
assert all(v.y.iszero() for v in vals)
def deg(po):return tuple(max((mm[i] for mm in po.to_dict()),default=-1) for i in range(6))
def monic(po):return po/po.leading_coefficient() if po else po
ps=[monic(v.x.n) for v in vals]
def spec(po,index,value):
 co={}
 for mm,cf in po.to_dict().items():
  key=tuple(0 if j==index else mm[j] for j in range(6));co[key]=co.get(key,fmpq(0))+cf*fmpq(value)**mm[index]
 return ctx.from_dict(co)
def strip(po,kn):
 while po:
  gg=po.gcd(kn)
  if gg.total_degree()==0:return monic(po)
  po=po/gg
 return po
known=qp*(qp-1)*(lp-1)*(lp*lp*qp-2*lp+1)*amp
ups=[strip(spec(pp,3,1),known) for pp in ps]
import sympy as S
sf,sg,sl,sQ,sa=S.symbols('f g l Q lam')
def sx(po):
 assert all(mm[3]==0 for mm in po.to_dict())
 return S.Poly.from_dict({(mm[0],mm[1],mm[2],mm[4],mm[5]):S.Rational(str(cf)) for mm,cf in po.to_dict().items()},(sf,sg,sl,sQ,sa)).as_expr()
ss=list(map(sx,ups));Dg=2*sQ*sl*sa-sQ*sl+2*sf-2*sa
assert S.degree(ss[3],sg)==1
assert S.factor(S.diff(ss[3],sg)+sQ*sl*Dg/2)==0
fden=sl*sQ*(S.Rational(1,2)-sa)+sa
assert S.factor(ss[3].subs(sf,fden)-sQ**2*sl**2*sa*(2*sa-1)*(sQ*sl**2-2*sl+1))==0

# l=0: the original jet forces f=lambda, mean forces g=0, and S gives Q*lambda.
inter=[S.factor(v.subs(sl,0)) for v in ss]
assert inter[3]==2*(sf-sa)**2
assert S.factor(inter[2].subs(sf,sa)-2*sQ*sg**2)==0
assert S.factor(inter[1].subs({sf:sa,sg:0})-sQ*(2*sa**2-2*sa+1)/2)==0
assert S.factor(S.rem(inter[4].subs({sf:sa,sg:0}),2*sa**2-2*sa+1,sa)-sQ*sa)==0

# The only remaining zero leading coefficient has lambda=f=1/2.
half=[S.factor(v.subs({sf:S.Rational(1,2),sa:S.Rational(1,2)})) for v in ss]
kn=sQ*(sQ-1)*sl*(sl-1)*(sl*sl*sQ-2*sl+1)
def sstrip(v):
 v=S.fraction(S.factor(v))[0]
 while v:
  gg=S.gcd(v,kn)
  if S.total_degree(gg)==0:return S.factor(v)
  v=S.div(v,gg,sg,sl,sQ)[0]
 return v
hp=list(map(sstrip,half));gb=S.groebner(hp,sg,sl,sQ,domain=S.QQ,order='grevlex')
assert len(gb.polys)==6
nonzero=[]
for vv in gb:
 while vv!=0 and vv.subs(sg,0)==0:vv=S.div(vv,sg,sg,sl,sQ)[0]
 nonzero.append(vv)
gb2=list(S.groebner(nonzero,sg,sl,sQ,domain=S.QQ))
assert gb2==[sg-sQ**2/5+3*sQ/20,sl+7*sQ**2/5-61*sQ/20-S.Rational(1,2),sQ**3-S.Rational(11,4)*sQ**2+S.Rational(3,2)*sQ]
assert S.factor(hp[0].subs(sg,0)-(2*sl-1)*(sQ*sl*sl-2*sl+1))==0

# g=0 then l=1/2. Recover the same original Gram, not just an abstract root.
def fixed(v):
 n=v.n;d=v.d
 for idx,val in [(0,fmpq(1,2)),(1,0),(2,fmpq(1,2)),(3,1),(5,fmpq(1,2))]:n=spec(n,idx,val);d=spec(d,idx,val)
 assert d
 return R(n,d)
for vv in [A,r,s,t]:assert fixed(vv.x).iszero() and fixed(vv.y).iszero()
for vv in [Ps[1],Ps[2],Ps[3]]:assert fixed(vv.x).iszero() and fixed(vv.y).iszero()
assert (fixed(Ps[0].x)+R(qp)/4).iszero() and fixed(Ps[0].y).iszero()

# The remaining lambda=1/2 chart has 2f-1 nonzero and a globally legal g solution.
jet=S.factor(ss[3].subs(sa,S.Rational(1,2)))
lin=S.cancel(jet/(2*sf-1));gsol=S.solve(lin,sg);assert len(gsol)==1;gsol=S.factor(gsol[0])
assert S.factor(S.diff(lin,sg)+sQ*sl/2)==0
kn=sQ*(sQ-1)*sl*(sl-1)*(sl*sl*sQ-2*sl+1)*(2*sf-1)
def strip_main(v):
 v=S.fraction(S.factor(v))[0]
 while v:
  gg=S.gcd(v,kn)
  if S.total_degree(gg)==0:return S.factor(v)
  v=S.div(v,gg,sf,sl,sQ)[0]
 return v
mp=[strip_main(ss[j].subs(sa,S.Rational(1,2)).subs(sg,gsol)) for j in [0,1,2,4,5]]
ctx3=fmpq_mpoly_ctx.get(('f','l','Q'),'lex');f3,l3,q3=ctx3.gens()
def fp3(v):return ctx3.from_dict({mm:fmpq(str(cc)) for mm,cc in S.Poly(v,sf,sl,sQ,domain=S.QQ).terms()})
known3=q3*(q3-1)*l3*(l3-1)*(l3*l3*q3-2*l3+1)
def strip3(v):
 while v:
  gg=v.gcd(known3)
  if gg.total_degree()==0:return v/v.leading_coefficient()
  v=v/gg
 return v
pp3=list(map(fp3,mp));rr=[strip3(pp3[0].resultant(v,'f')) for v in pp3[1:]]
assert [tuple(v.degrees()) for v in rr]==[(0,12,8),(0,12,6),(0,18,11),(0,19,12)]
last=[rr[0].resultant(v,'l') for v in rr[1:]]
assert [tuple(v.degrees()) for v in last]==[(0,0,92),(0,0,162),(0,0,170)]
gg=last[0].gcd(last[1]).gcd(last[2]);target=q3**54*(q3-1)**8*(4*q3-5)
assert gg/gg.leading_coefficient()==target/target.leading_coefficient()
lastgb=list(S.groebner([v.subs(sQ,S.Rational(5,4)) for v in mp],sf,sl,domain=S.QQ))
assert lastgb==[sf-S.Rational(5,16)*sl-S.Rational(1,2),sl**2]
print(json.dumps({'status':'all exact original identities and rational ideal fibers verified','scope':'u=1,P0 nonzero,lambda=N0/P0 nonzero: l=0 and lambda=1/2 excluded; hence the g coefficient is nonzero','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runtime_seconds':time.perf_counter()-start,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'half_nonzero_g_groebner':[str(v) for v in gb2],'remaining_half_resultant_degrees':[92,162,170],'remaining_half_last_fiber':[str(v) for v in lastgb],'ordinary_isp_claim':False},sort_keys=True),flush=True)

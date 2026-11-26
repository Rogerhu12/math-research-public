#!/usr/bin/env python3
"""Complete original QQ exclusion of the remaining q=-1 regular chart.
Previously proved exceptional curves and singular mean charts are cited.
All resultants stay in memory; output is a small execution receipt.
"""
import hashlib,json,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import time
start=time.perf_counter()
ctx=fmpq_mpoly_ctx.get(('l','v','w'),'lex');lp,vp,wp=ctx.gens();zero=ctx.constant(0);onep=ctx.constant(1)
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
l=R(lp);v=R(vp);w=R(wp)
D1=-2*l+v-w+1;D2=-2*l*(v+1)+v*v+v*w-w+1
ee=l*(l*v**3-l*v*v-l*v*w*w-l*w*w+w*w)/(D1*D2)
TT=ee+(l*(v-1)*(v+w)-w*w)/(2*D1)
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
u=Q(0,1);lq=Q(l);vq=Q(v);wq=Q(w);eq=Q(ee);Tq=Q(TT)
a=1-lq;b=(lq+u)/2;c=(lq-u)/2;t=wq/u;X=Tq/u
x=X+(vq+1)/2;y=X-(vq+1)/2;f=(Tq+eq+lq*vq/2)/(2*u)
r=x-a-c*t;s=y+a-b*t;A=2*f-2*b*x-2*c*y+2*b*c*t
K=[[Q(0),Q(0),Q(1),Q(-1)],[Q(0),A,r,s],[Q(1),r,Q(0),t],[Q(-1),s,t,Q(0)]]
one=[Q(1),Q(0),Q(1),Q(1)]
def add(x,y):return [xx+yy for xx,yy in zip(x,y)]
def scale(c,x):return [c*xx for xx in x]
def mul(x,y):return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
def dk(x):return [tau(mul(k,x)) for k in K]
d=dk(one);F=tau(d)/2
def P(x):
 z=add(x,scale(-tau(x),one));return tau(mul(mul(z,z),z))/2
def N(x):return tau(mul(add(d,scale(-F,one)),mul(x,x)))/2-tau(x)*tau(mul(d,x))+F*tau(x)**2+tau(mul(x,dk(x)))/4
def Pjet(x,y):
 z=add(x,scale(-tau(x),one));h=add(y,scale(-tau(y),one));return 3*tau(mul(mul(z,z),h))/2
def Njet(x,y):return N(add(x,y))-N(x)-N(y)
Ps=[P(K[0]),Pjet(K[0],K[1]),P(K[2]),P(K[3])]
Ns=[N(K[0]),Njet(K[0],K[1]),N(K[2]),N(K[3])]
P0,P1,PB,PC=Ps;N0,N1,NB,NC=Ns
Nbar=a*N0+N1+b*NB+c*NC
Sval=a*P0+P1+b*PB+c*PC-2*Nbar
Cval=3*P0*N1-2*N0*P1
TR=3*N0*NB*NC-(3*a*P0+P1)*NB*NC-3*b*PB*N0*NC-3*c*PC*N0*NB
evec=[tau(mul(K[0],K[0])),2*tau(mul(K[0],K[1])),tau(mul(K[2],K[2])),tau(mul(K[3],K[3]))]
E=add(add(evec,scale(-2,dk(d))),add(scale(-2,mul(d,d)),scale(4*F,d)))
assert E[0].iszero() and E[2].iszero() and E[3].iszero()
Mval=eq*E[1]
assert Mval.y.iszero() and Sval.x.iszero() and Cval.y.iszero() and TR.x.iszero()
Hp=-2*lp*lp*vp-2*lp*lp+2*lp*vp*vp+lp*vp-2*lp*wp+lp-wp*wp
known=lp*(2*lp-1)*D1.n*D2.n*ee.n*Hp
def strip(poly,known):
 while poly:
  gg=poly.gcd(known)
  if gg.total_degree()==0:return poly
  poly=poly/gg
 return poly
def deg(po):return tuple(max((mm[i] for mm in po.to_dict()),default=-1) for i in range(3))
LB=2*NB**3-Nbar*PB**2;LC=2*NC**3-Nbar*PC**2
Ldiff=LB-LC;assert Ldiff.y.iszero()
def monic(po):return po/po.leading_coefficient()
pols=[monic(strip(val.n,known)) for val in [Mval.x,Sval.y,Cval.x,TR.y,Ldiff.x]]
assert [deg(po) for po in pols]==[(4,6,5),(4,7,5),(9,14,10),(19,27,22),(22,33,25)]
M,S,C,TRpoly,BD=pols
Bp=vp*vp+vp*wp-wp+1
Gm=vp**3-vp*wp*wp-vp*wp+vp-wp*wp-wp
Gp=vp**3-vp*wp*wp+vp*wp-vp-wp*wp-wp
kn=vp*wp*(vp+wp)*Bp*Gm*Gp
RMS,RMC,RMT,RMBD=[monic(strip(M.resultant(po,'l'),kn)) for po in [S,C,TRpoly,BD]]
assert [deg(po) for po in [RMS,RMC,RMT,RMBD]]==[(0,15,8),(0,32,23),(0,73,53),(0,96,63)]
RC,RT,RBD=[RMS.resultant(po,'v') for po in [RMC,RMT,RMBD]]
assert [deg(po)[2] for po in [RC,RT,RBD]]==[359,838,1011]
gg=RC.gcd(RT).gcd(RBD)
assert monic(gg)==monic(wp**90*(wp+1)**4*(wp*wp+2*wp-1)**2)

# The w=-1 fiber is retained and forces the already excluded v=0.
def wspec(po,value):
 co={}
 for mm,cf in po.to_dict().items():
  key=(mm[0],mm[1],0);co[key]=co.get(key,fmpq(0))+cf*fmpq(value)**mm[2]
 return ctx.from_dict(co)
gw=wspec(RMS,-1)
for po in [RMC,RMT,RMBD]:gw=gw.gcd(wspec(po,-1))
assert monic(gw)==vp

# Retain both roots of the irreducible w quadratic over QQ.
import sympy as SX
L,V,W=SX.symbols('L V W');Qw=W*W+2*W-1
def sx(po):
 po=monic(po)
 return SX.Add(*(SX.Rational(str(cf))*L**int(mm[0])*V**int(mm[1])*W**int(mm[2]) for mm,cf in po.to_dict().items()))
qr=[SX.rem(sx(po),Qw,W) for po in [RMS,RMC,RMT,RMBD]]
qgb=SX.groebner(qr+[Qw],V,W,domain=SX.QQ)
assert list(qgb)==[V-1,Qw]
original=[SX.rem(sx(po).subs(V,1),Qw,W) for po in [M,S,C]]
ogb=SX.groebner(original+[Qw],L,W,domain=SX.QQ)
assert list(ogb)==[L-SX.Rational(1,2),Qw]

# Division-free origin of the trace and norm-difference equations.
aa,bb,cc,U0,U1,UB,UC=SX.symbols('aa bb cc U0 U1 UB UC')
mm=aa*U0+U1+bb*UB+cc*UC
p0,p1,pb,pc=-U0**3,-3*U0*U0*U1,-UB**3,-UC**3
n0,n1,nb,nc=-mm*U0*U0,-2*mm*U0*U1,-mm*UB*UB,-mm*UC*UC
tr=3*n0*nb*nc-(3*aa*p0+p1)*nb*nc-3*bb*pb*n0*nc-3*cc*pc*n0*nb
assert SX.expand(tr)==0
assert SX.expand(2*nb**3+2*mm**3*pb**2)==0
assert SX.expand(2*nc**3+2*mm**3*pc**2)==0
print(json.dumps({'schema':'r150-unit211-opposite-regular-main-exclusion-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'remaining q=-1 regular mean chart; with cited complete boundaries, the entire opposite-base-pairing unit211 branch is empty','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'secondResultantDegrees':[359,838,1011],'gcdFactors':[['w',90],['w+1',4],['w^2+2*w-1',2]],'finalFibers':['w=-1 forces v=0','w^2+2*w-1=0 forces v=1 then l=1/2'],'ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-start,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))

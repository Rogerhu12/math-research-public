#!/usr/bin/env python3
"""Original QQ scaled-ratio finite cover and half-weight exclusion, u=1.
Prior l=0, lambda=0,1/2 and g-jet denominator exclusions are registered.
This source rebuilds the original equations but does not rerun those exclusions.
"""
import hashlib,json,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import time
start=time.perf_counter()
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

# New work begins here. No cached coefficient arrays are inputs.
import itertools
sv,sz=S.symbols('v z')
ss=list(map(sx,ups))
def say(stage,**data):
 print(json.dumps(dict(stage=stage,seconds=time.perf_counter()-start,**data),sort_keys=True),flush=True)
change={sf:(1+sv*sz)/2,sa:(1+sv)/2}
scaled=[S.expand(j.subs(change)) for j in ss]
jc=S.diff(scaled[3],sg)
assert S.expand(jc+sQ*sl*sv*(sz+sQ*sl-1)/2)==0
gsol=S.factor(-scaled[3].subs(sg,0)/jc)
assert S.cancel(scaled[3].subs(sg,gsol))==0
c4=fmpq_mpoly_ctx.get(('v','z','l','Q'),'lex')
v4,z4,l4,q4=c4.gens()
def cv4(f):
 f=S.Poly(f,sv,sz,sl,sQ,domain=S.QQ)
 return c4.from_dict({m:fmpq(str(c)) for m,c in f.terms()})
def sy4(f):
 return S.Poly.from_dict({m:S.Rational(str(c)) for m,c in f.to_dict().items()},(sv,sz,sl,sQ)).as_expr()
def norm4(f):return f/f.leading_coefficient() if f else f
def clear4(f,K):
 while f:
  g0=f.gcd(K)
  if g0.total_degree()==0:return norm4(f)
  f=f/g0
 return f
known4=v4*(v4+1)*q4*(q4-1)*l4*(l4-1)*(l4*l4*q4-2*l4+1)*(z4+q4*l4-1)
AA=[clear4(cv4(S.fraction(S.cancel(scaled[j].subs(sg,gsol)))[0]),known4) for j in [0,1,2,4,5]]
def cf(f,index,power):
 return c4.from_dict({tuple(0 if j==index else m[j] for j in range(4)):c for m,c in f.to_dict().items() if m[index]==power})
def at(f,index,value):
 value=fmpq(value);d={}
 for m,c in f.to_dict().items():
  mm=tuple(0 if j==index else m[j] for j in range(4))
  d[mm]=d.get(mm,fmpq(0))+c*value**m[index]
 return c4.from_dict(d)
def det4(rows):
 n=len(rows);ans=c4.constant(0)
 for p0 in itertools.permutations(range(n)):
  inversions=sum(p0[i]>p0[j] for i in range(n) for j in range(i+1,n))
  term=c4.constant((-1)**inversions)
  for i,j in enumerate(p0):term=term*rows[i][j]
  ans=ans+term
 return ans
def degrees(f):return list(map(int,f.degrees()))
def polyhash(f):
 serial=json.dumps([[list(m),str(c)] for m,c in sorted(f.to_dict().items())],separators=(',',':'))
 return hashlib.sha256(serial.encode()).hexdigest()
assert [degrees(a) for a in AA]==[[2,4,4,3],[2,4,9,6],[2,4,8,5],[3,6,12,8],[3,6,12,9]]
B=clear4(det4([[cf(a,0,j) for j in [2,1,0]] for a in AA[:3]]),known4)
assert degrees(B)==[0,6,8,6]
say('scaled_original_equations',degrees=[degrees(a) for a in AA],terms=[len(a.to_dict()) for a in AA],B_degrees=degrees(B))

# Finite z fibers: the exact coefficient ideal contains Q^2(Q-1).
BC=[sy4(cf(B,1,j)) for j in range(7)]
bg=S.groebner(BC,sl,sQ,domain=S.QQ,order='lex')
assert bg.reduce(sQ**2*(sQ-1))[1]==0
say('finite_z_fibers',coefficient_groebner=[str(q) for q in bg])

# Finite v fibers: pay the z=1 coefficient-zero locus first.
VC=[sy4(clear4(cf(a,0,j),known4)) for a in AA[:3] for j in range(3)]
vg=S.groebner(VC,sz,sl,sQ,domain=S.QQ,order='grevlex')
vg1=S.groebner([p0.subs(sz,1) for p0 in vg],sl,sQ,domain=S.QQ,order='lex')
assert vg1.reduce(sQ**3*sl**2)[1]==0
newc=[sy4(clear4(cv4(p0),known4*(z4-1))) for p0 in vg]
vl=S.groebner(newc,sz,sl,sQ,domain=S.QQ,order='lex')
targets=[
 (-80*sQ**3*sl+68*sQ**2*sl+8*sQ*sl**2-sQ*sl+21*sz-21)/21,
 sQ*sl*(32*sQ**2-28*sQ+2*sl**2-3*sl+1)/2,
 sQ**2*sl*(4*sQ+sl-5),
 sQ**2*sl*(4*sQ-3)**2/16]
assert all(vl.reduce(S.expand(t0))[1]==0 for t0 in targets)
assert S.expand((sl**2*sQ-2*sl+1).subs({sQ:S.Rational(3,4),sl:2}))==0
say('finite_v_fibers',z_one_unit='Q^3*l^2',remaining_coefficient_groebner=[str(q) for q in vl],forced_forbidden_D_zero=[str(S.Rational(3,4)),2,str(-S.Rational(1,2))])

# Entire l=1/2 branch, with the original z=1 fiber paid before division.
half_known=at(known4,2,fmpq(1,2))
HH=[clear4(at(a,2,fmpq(1,2)),half_known) for a in AA]
hz=[sy4(clear4(at(a,1,1),half_known)) for a in HH[:3]]
hzg=S.groebner(hz,sv,sQ,domain=S.QQ,order='lex')
assert hzg.reduce(sQ**2)[1]==0
HR=[clear4(HH[0].resultant(a,'v'),half_known*(z4-1)) for a in HH[1:]]
HL=[HR[0].resultant(a,'z') for a in HR[1:]]
assert all(HL)
HG=HL[0].gcd(HL[1]).gcd(HL[2])
assert clear4(HG,q4*(q4-1)).total_degree()==0
say('half_weight_excluded',z_one_groebner=[str(q) for q in hzg],final_resultant_degrees=[degrees(a) for a in HL],final_gcd=str(norm4(HG)))

# The finite fibers make the common mean projection a complete curve cover.
# Three equations in this open A^4 have every component dimension at least 1.
# Thus a component cannot project just to an isolated common-resultant point.
RR=[clear4(AA[0].resultant(a,'v'),known4) for a in AA[1:]]
PP=[clear4(B.resultant(RR[j],'z'),known4) for j in [0,1]]
GG=PP[0].gcd(PP[1])
CC=clear4(GG,known4*(2*l4-1))
assert degrees(CC)==[0,0,18,10]
say('complete_mean_curve_cover',mean_projection_degrees=[degrees(a) for a in PP],common_projection_factor_degrees=[[degrees(fac),int(power)] for fac,power in GG.factor()[1]],remaining_curve_degrees=degrees(CC),remaining_curve_terms=len(CC.to_dict()),remaining_curve_sha256=polyhash(CC))
say('complete',scope='u=1, nonzero isolated mean: finite curve cover and entire l=1/2 excluded; high curve and general u remain open',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,ordinary_isp_claim=False)

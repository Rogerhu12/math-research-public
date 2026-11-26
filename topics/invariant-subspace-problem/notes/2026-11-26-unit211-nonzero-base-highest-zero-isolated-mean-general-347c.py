#!/usr/bin/env python3
"""Original QQ reduction and exclusion for both remaining P0!=0,m=0 charts.
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
def degree(po):return tuple(int(max((mm[i] for mm in po.to_dict()),default=-1)) for i in range(5))
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
J=2*lp*up*qp-lp*qp-2*up*up-up*qp+2*up
lJ=R(up*(2*up+qp-2),qp*(2*up-1))
assert spec(J,3,fmpq(1,2))==-(qp-1)/2
def eval_index(po,arg,index):
 groups={}
 for mm,cf in po.to_dict().items():
  key=tuple(0 if j==index else mm[j] for j in range(5));groups.setdefault(mm[index],{})[key]=cf
 result=R(0)
 for i in range(max(groups,default=0),-1,-1):result=result*arg+R(ctx.from_dict(groups.get(i,{})))
 return result
assert (eval_index(P0n,lJ,2)-R(up*(up-1)*(qp+4*up*(up-1)),2*up-1)).iszero()
baseknown=up*qp*(qp-1)*D*P0n
def fcoeff(po,i):return ctx.from_dict({(0,mm[1],mm[2],mm[3],mm[4]):cf for mm,cf in po.to_dict().items() if mm[0]==i})

# Previously proved F1,u=1 / F2,l=0 and J=0 faces are cited, not rerun.
# All arrays below are generated from the original operations and kept in RAM.
def coeff_index(po,index,i):
 return ctx.from_dict({tuple(0 if j==index else mm[j] for j in range(5)):cf for mm,cf in po.to_dict().items() if mm[index]==i})
def same_up_to_QQ(a,b):return bool(a) and bool(b) and normal(a)==normal(b)
Pbar=a*Ps[0]+Ps[1]+b*Ps[2]+c*Ps[3]
assert Pbar.y.iszero()
data=[];bigs=[];sp=[]
for face,fi,den,dd in [(0,F1,up-1,(0,0,6,9,6)),(1,F2,lp,(0,0,8,11,7))]:
 gf=R(-spec(fi,1,0),fi.derivative('g'));kn=baseknown*den
 pp=[]
 for val in [gvals[i] for i in [0,1,2,4,5]]:
  ex=eval_index(val.n,gf,1)/eval_index(val.d,gf,1)
  pp.append(strip(ex.n,kn))
 sx=eval_index(Pbar.x.n,gf,1)/eval_index(Pbar.x.d,gf,1)
 sp.append(strip(sx.n,kn))
 rows=[[fcoeff(po,i) for i in [2,1,0]] for po in pp[:3]]
 aa,bb,cc=rows
 cross=[aa[1]*bb[2]-aa[2]*bb[1],aa[2]*bb[0]-aa[0]*bb[2],aa[0]*bb[1]-aa[1]*bb[0]]
 det=strip(sum((cross[j]*cc[j] for j in range(3)),zero),kn)
 bg=normal(det/J);assert same_up_to_QQ(bg*J,det) and degree(bg)==dd
 rr=[strip(pp[0].resultant(po,'f'),kn) for po in pp[1:]]
 data.append((gf,kn,pp,rr));bigs.append(bg)

# Finite l-fibers of the mean projection.
assert coeff_index(bigs[0],2,6)==qp**6
assert coeff_index(bigs[1],2,8)==qp**7*(up-fmpq(1,4))
quarter=spec(bigs[1],3,fmpq(1,4))
assert coeff_index(quarter,2,7)==qp**6*(9-qp)/32
assert coeff_index(quarter,2,6)==-qp**5*(271*qp+18)/256
assert spec(coeff_index(quarter,2,6),4,9)

# No legal weights make all three original mean conics identically zero in f.
# F1 face: the E1 constant coefficient has the factor L0.
cc0=[fcoeff(po,i) for po in data[0][2][:3] for i in [2,1,0]]
L0=lp*qp+2*up*(up-1);B0=cc0[2]/L0
assert B0*L0==cc0[2]
H4=4*up*up-4*up+qp;J0=2*up*up-2*up+qp
l0=R(-2*up*(up-1),qp)
assert same_up_to_QQ(eval_index(cc0[0],l0,2).n,up**2*(up-1)*H4**2)
assert same_up_to_QQ(eval_index(D,l0,2).n,up**2*H4)
# Thus L0=0 would force the already forbidden D=0.
qH=R(-4*up*(up-1));cH=[eval_index(po,qH,4).n for po in cc0]
assert same_up_to_QQ(cH[0],up**3*(up-1)**3*(2*lp-1)**2*(8*lp*up-6*lp+1))
assert not spec(eval_index(D,qH,4).n,2,fmpq(1,2))
lh=R(1,6-8*up)
ch1=eval_index(cH[1],lh,2).n;ch2=eval_index(cH[2],lh,2).n
zh=up*(up-1)*(2*up-1)*(6-8*up)
assert strip(ch1,zh).gcd(strip(ch2,zh)).total_degree()==0
# Away from H4=0, these four complete l-resultants retain all coefficient fibers.
rc=[cc0[0].resultant(po,'l') for po in [cc0[1],B0,cc0[3],cc0[6]]]
kc=up*qp*(qp-1)*(up-1)*H4
rc=[strip(po,kc) for po in rc]
rq=[rc[0].resultant(po,'u') for po in rc[1:]]
assert [degree(po)[4] for po in rq]==[-1,40,40]
assert same_up_to_QQ(rq[0].gcd(rq[1]).gcd(rq[2]),qp**17)
# F2 face: E1's quadratic coefficient is l*Q*alpha up to a QQ unit.
cc1=[fcoeff(po,i) for po in data[1][2][:3] for i in [2,1,0]]
alpha=qp*(lp-1)-2*up*(up-1)
assert same_up_to_QQ(cc1[0],lp*qp*alpha)
la=R(qp+2*up*(up-1),qp)
ca=[eval_index(po,la,2).n for po in cc1]
assert same_up_to_QQ(eval_index(P0n,la,2).n,(up-1)*H4)
assert same_up_to_QQ(ca[1],(up-1)*H4*(8*up*up-8*up+3*qp))
qa=R(-8*up*(up-1),ctx.constant(3))
ca2=strip(eval_index(ca[2],qa,4).n,up*(up-1))
ca6=strip(eval_index(ca[6],qa,4).n,up*(up-1))
assert same_up_to_QQ(ca2,11*up+6)
assert same_up_to_QQ(ca6,61*up*up-48*up+8)
assert ca2.gcd(ca6).total_degree()==0

# Compute the exact two mean projection resultants before any N constraints.
# The proof's dimension lemma, together with the preceding finite-fiber checks,
# justifies coverage by their gcd; no gcd is identified with a general 2D zero set.
projection=[]
for face in [0,1]:
 pp=data[face][2];rr=data[face][3];bg=bigs[face]
 second=[bg.resultant(rr[i],'l') for i in [0,1]]
 mg=second[0].gcd(second[1])
 kp=up*qp*(qp-1)*(up-1)*H4*J0*((2*up-qp) if face==0 else (up-2))
 high=strip(mg,kp)
 assert degree(high)==((0,0,0,10,6) if face==0 else (0,0,0,24,14))
 low=(qp**62*(qp-1)**6*up**16*(up-1)**26*H4**18*J0*(2*up-qp) if face==0 else
      qp**101*(qp-1)**6*up**54*(up-1)**8*H4**23*J0**2*(up-2))
 assert same_up_to_QQ(mg,low*high)
 projection.append((second,mg,kp,high))
 print(json.dumps({'stage':'exact_mean_projection','face':face,'degrees':[degree(po) for po in second],'highCurveDegree':degree(high)},sort_keys=True),flush=True)

# Pay every low projection curve with the original E/N/Pbar system.
low_cases=[
 ('H0',0,4,R(-4*up*(up-1)),onep,[45,39,72,60,69],(up-1)**2*up**7*(2*up-1)**7),
 ('H1',1,4,R(-4*up*(up-1)),onep,[115,105,155,145,160],(3*up-2)*(2*up-1)**8*up**14*(up-1)**17),
 ('J00',0,4,R(-2*up*(up-1)),lp-1,[76,66,121,108,113],(2*up*up-2*up+1)**6*up**11*(up-1)**18),
 ('J01',1,4,R(-2*up*(up-1)),lp-1,[163,149,219,204,223],(up-2)*(2*up*up-2*up+1)**6*(up-1)**28*up**41),
 ('UQ',0,4,R(2*up),lp-1,[94,92,140,136,138],up**11*(up-1)**19*(2*up-1)**24),
 ('U2',1,3,R(2),2*lp-1,[164,160,221,213,227],(qp+4)**2*(qp-1)**6*(qp+8)**14*qp**87),
 ('U1',1,3,R(1),onep,[38,36,67,61,69],(16*qp-15)**2*qp**17),
 ('Um2',1,3,R(-2),onep,[200,196,267,258,274],(qp+12)**2*(qp-1)**6*(qp+24)**23*qp**109)]
low_data={}
for name,face,index,arg,extra,wantdeg,wantgcd in low_cases:
 kn=eval_index(data[face][1],arg,index).n*arg.d*extra
 pp=[strip(eval_index(po,arg,index).n,kn) for po in data[face][2]+[sp[face]]]
 bg=strip(eval_index(bigs[face],arg,index).n,kn)
 rr=[strip(pp[0].resultant(po,'f'),kn) for po in pp[1:]]
 last=[bg.resultant(po,'l') for po in rr]
 jj=3 if index==4 else 4
 assert [degree(po)[jj] for po in last]==wantdeg
 gg=last[0]
 for po in last[1:]:gg=gg.gcd(po)
 assert same_up_to_QQ(gg,wantgcd)
 low_data[name]=(pp,kn)
# U2's apparent extra factor 2*l-1 is already a factor of H=2P0.
assert spec(P0n,3,2)==2*qp*(2*lp-1)

import sympy as SX
FF,LL=SX.symbols('f l')
def sx_fl(po):
 if not po:return SX.Integer(0)
 po=normal(po)
 assert all(mm[1]==0 and mm[3]==0 and mm[4]==0 for mm in po.to_dict())
 return SX.Add(*(SX.Rational(str(cf))*FF**int(mm[0])*LL**int(mm[2]) for mm,cf in po.to_dict().items()))
fiber_gbs=[]
for name,index,value,want in [
 ('H1',3,fmpq(2,3),[FF-SX.Rational(8,3)*LL**2+SX.Rational(4,3)*LL-SX.Rational(1,3),LL**3-LL**2/2]),
 ('J01',3,2,[FF+28*LL**3-38*LL**2+10*LL,LL**4-SX.Rational(3,2)*LL**3+LL**2/2]),
 ('U1',4,fmpq(15,16),[FF**2-SX.Rational(5,4)*FF+SX.Rational(45,256)*LL**2+SX.Rational(15,256)*LL,FF*LL-SX.Rational(4,3)*FF-SX.Rational(3,64)*LL**2+LL/16,LL**3-SX.Rational(4,3)*LL**2])]:
 gb=SX.groebner([sx_fl(spec(po,index,value)) for po in low_data[name][0]],FF,LL,domain=SX.QQ)
 assert all(SX.expand(x-y)==0 for x,y in zip(list(gb),want)) and len(gb)==len(want)
 fiber_gbs.append(name)
# H1: l=0 (forbidden) or l=1/2 (D=0).
assert not spec(spec(eval_index(D,qH,4).n,3,fmpq(2,3)),2,fmpq(1,2))
# J01: l=0,1,1/2; the first two were excluded on this subchart,
# and at u=2,Q=-4 the l=1/2 value has P0=0.
assert not spec(spec(spec(P0n,3,2),4,-4),2,fmpq(1,2))
# U1: l=0 (forbidden) or 4/3 (D=0).
assert not spec(spec(spec(D,3,1),4,fmpq(15,16)),2,fmpq(4,3))
# U2's only Q=-4,-8 are precisely its already paid J0 and H4 curves.
assert not spec(spec(J0,3,2),4,-4) and not spec(spec(H4,3,2),4,-8)
assert not spec(spec(J0,3,-2),4,-12) and not spec(spec(H4,3,-2),4,-24)

# The l=1 fibers deliberately retained outside the l!=1 low-curve calculations.
for face in [0,1]:
 kn=eval_index(spec(data[face][1],2,1),R(-2*up*(up-1)),4).n
 pp=[strip(eval_index(spec(po,2,1),R(-2*up*(up-1)),4).n,kn) for po in data[face][2]+[sp[face]]]
 target=fp*(2*fp+up*up-up) if face==0 else fp*(2*fp-3*up)
 assert same_up_to_QQ(pp[0],target)
 fa=R(-up*(up-1),ctx.constant(2)) if face==0 else R(3*up,ctx.constant(2))
 ff=[eval_index(po,fa,0).n for po in pp[1:]]
 gg=ff[0]
 for po in ff[1:]:gg=gg.gcd(po)
 assert same_up_to_QQ(gg,up**2*(up-1)**2 if face==0 else up**2)
# Hence f=0. Both original face equations then give g=0.
def star_pol(po):
 for index,value in [(0,0),(1,0),(2,1)]:po=spec(po,index,value)
 return eval_index(po,R(-2*up*(up-1)),4).n
assert not star_pol(F1) and not star_pol(F2)
for vv in [A,r,s,t,Ps[1],Ps[2],Ps[3]]:
 assert not star_pol(vv.x.n) and not star_pol(vv.y.n)
assert same_up_to_QQ(star_pol(P0n),up**2*(up-1))
# The proof uses the original highest equations to get U=(U0,0,0,0),
# making the full physical Gram rank 2, contrary to its rank at least 4.
kn=eval_index(spec(data[0][1],2,1),R(2*up),4).n
pp=[strip(eval_index(spec(po,2,1),R(2*up),4).n,kn) for po in data[0][2]+[sp[0]]]
assert same_up_to_QQ(pp[0],(fp-up)**2)
assert same_up_to_QQ(eval_index(pp[4],R(up),0).n,up**3*(up-1))

# All low projection factors are now paid for original solutions. Each high
# curve is intersected with TWO actual N-resultants, retaining isolated points.
high_degrees=[];high_gcd_factors=[]
for face in [0,1]:
 kp=projection[face][2];high=projection[face][3]
 nn=[strip(bigs[face].resultant(data[face][3][j],'l'),kp) for j in [2,3]]
 last=[]
 for j,po in enumerate(nn):
  zz=high.resultant(po,'Q');last.append(zz)
  print(json.dumps({'stage':'exact_high_curve_univariate','face':face,'index':j,'degreeU':degree(zz)[3],'elapsedSeconds':round(time.perf_counter()-start,6)},sort_keys=True),flush=True)
 gg=last[0].gcd(last[1]);high_degrees.append([degree(po)[3] for po in last])
 high_gcd_factors.append([(str(po),int(mm)) for po,mm in gg.factor()[1]])
 if face==0:
  assert high_degrees[-1]==[671,629]
  assert same_up_to_QQ(gg,up**78*(up-1)**96)
 else:
  # u=0 is forbidden and u=1,-2 are paid in the low-curve computation.
  assert strip(gg,up*(up-1)*(up+2)).total_degree()==0

print(json.dumps({'schema':'r150-unit211-P0nonzero-mzero-general-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'remaining two general N1 faces with P0 nonzero,m=0 and nonzero distinct nonopposite base pairings are physically empty','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'highCurveResultantDegrees':high_degrees,'highCurveGcdFactors':high_gcd_factors,'meanFiniteProjectionChecked':True,'ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-start,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))

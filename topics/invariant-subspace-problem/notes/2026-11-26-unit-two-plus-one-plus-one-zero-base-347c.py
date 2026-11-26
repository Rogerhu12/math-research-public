#!/usr/bin/env python3
"""Exact original unit(2+1+1) zero-base-pairing exclusion.
AI-assisted GPT-6 Astra Pro, Astra-ISP-347c-20261126 / unit31_general.
All active mean equations, the leading cubic/quadratic values at the double
point, the two simple-point values, and m=tau(U) are retained. Only p=q=0
is covered. No claim is made on other unit(2+1+1) pairings or ordinary ISP.
No generated arrays are written. SymPy 1.14.0 and python-flint 0.9.0.
"""
import argparse,hashlib,json,resource,signal
from pathlib import Path
from time import monotonic
ap=argparse.ArgumentParser();ap.add_argument('--wall-seconds',type=int,default=180);ap.add_argument('--memory-mib',type=int,default=1024)
args=ap.parse_args();assert 1<=args.wall_seconds<=600 and 256<=args.memory_mib<=4096
resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,)*2)
def timeout(signum,frame):raise TimeoutError('Exact unit211 zero-base wall budget')
signal.signal(signal.SIGALRM,timeout);signal.alarm(args.wall_seconds)
import sympy as S
from flint import fmpq,fmpq_mpoly_ctx
started=monotonic()
b,c,A,r,s,t,x,y,f,u,v,z=S.symbols('b c A r s t x y f u v z')
a=1-b-c;one=S.Matrix([1,0,1,1])
def mul(z,w):return S.Matrix([z[0]*w[0],z[0]*w[1]+z[1]*w[0],z[2]*w[2],z[3]*w[3]])
def tau(z):return a*z[0]+z[1]+b*z[2]+c*z[3]
K=S.Matrix([[0,0,0,0],[0,A,r,s],[0,r,0,t],[0,s,t,0]])
def DK(z):return S.Matrix([tau(mul(K.row(i).T,z)) for i in range(4)])
d=DK(one);F=S.expand(tau(d)/2)
def P(z):
 zz=z-tau(z)*one;return S.expand(tau(mul(zz,mul(zz,zz)))/2)
def N(z):return S.expand(tau(mul(d-F*one,mul(z,z)))/2-tau(z)*tau(mul(d,z))+F*tau(z)**2+tau(mul(z,DK(z)))/4)
rows=[K.row(i).T for i in range(4)]
e=S.Matrix([tau(mul(rows[0],rows[0])),2*tau(mul(rows[0],rows[1])),tau(mul(rows[2],rows[2])),tau(mul(rows[3],rows[3]))])
E=[S.expand(h) for h in e-2*DK(d)-2*mul(d,d)+4*F*d]
def eq(h,j=0):assert S.cancel(S.expand(h-j))==0
assert E[0]==0
eq(F,A/2+b*r+c*s+b*c*t)
Pall=[P(K[:,i]) for i in [1,2,3]];Nall=[N(K[:,i]) for i in [1,2,3]]
# t=0: exact mean forms and the two simple-node values.
eq(E[2].subs(t,0),2*r*(2*F.subs(t,0)-r));eq(E[3].subs(t,0),2*s*(2*F.subs(t,0)-s))
for var,i in [(r,1),(s,2)]:eq(Pall[i].subs(t,0),var**3);eq(Nall[i].subs(t,0),F.subs(t,0)*var**2)
w=S.symbols('w')
eq((2*A*A+6*A*w+4*w*w-2*w).subs(A,1-2*w),2*(1-2*w))
# t=1, exact d-coordinate chart. These equations hold even on x=1/2 or y=1/2.
coord={t:1,r:x-c,s:y-b,A:2*f-2*b*x-2*c*y+2*b*c}
Eq=[S.factor(h.subs(coord,simultaneous=True)) for h in E]
eq(F.subs(coord,simultaneous=True),f)
eq(Eq[1],8*f*f-4*f*(b*x+c*y)-2*(b*x*x+c*y*y)+2*b*c*(x+y))
eq(Eq[2],c*(1-2*y)-2*x*x+4*f*x);eq(Eq[3],b*(1-2*x)-2*y*y+4*f*y)
# Complete x=1/2 boundary, with the y=1/2 case obtained by exchanging nodes.
eq(Eq[2].subs(x,S.Rational(1,2)),c*(1-2*y)-S.Rational(1,2)+2*f)
eq(Eq[3].subs(x,S.Rational(1,2)),2*y*(2*f-y))
eq(Eq[1].subs({x:S.Rational(1,2),y:0,c:S.Rational(1,2)-2*f},simultaneous=True),4*f*(2*f-b))
eq(Eq[1].subs({x:S.Rational(1,2),y:S.Rational(1,2),f:S.Rational(1,4)},simultaneous=True),(2*b-1)*(2*c-1)/2)
Pvals=[S.expand(h.subs(t,1)) for h in Pall];Nvals=[S.expand(h.subs(t,1)) for h in Nall]
star={A:0,r:0,s:y-b,c:S.Rational(1,2)}
pp=[S.factor(h.subs(star,simultaneous=True)) for h in Pvals];nn=[S.factor(h.subs(star,simultaneous=True)) for h in Nvals]
assert pp[:2]==nn[:2]==[0,0];eq(nn[2],pp[2]/2)
exception={A:b*(1-2*b),r:b,s:-b,c:S.Rational(1,2)-b}
pp=[S.factor(h.subs(exception,simultaneous=True)) for h in Pvals];nn=[S.factor(h.subs(exception,simultaneous=True)) for h in Nvals]
mu=nn[0]*nn[1]*nn[2]-pp[0]*nn[1]*nn[2]-b*pp[1]*nn[0]*nn[2]-(S.Rational(1,2)-b)*pp[2]*nn[0]*nn[1]
chi=nn[1]**3*pp[2]**2-nn[2]**3*pp[1]**2
eq(mu,b**6*(2*b-1)*(4*b-3)/64);eq(chi,b**5*(5*b**3-3*b*b+3*b-1)/1024)
eq((5*b**3-3*b*b+3*b-1).subs(b,S.Rational(3,4)),S.Rational(107,64))
# The two exhaustive generic mean surfaces.
bgen=2*y*(y-2*f)/(1-2*x);cgen=2*x*(x-2*f)/(1-2*y)
eq(Eq[1].subs({b:bgen,c:cgen},simultaneous=True),8*(-f+x*y)*(-8*f*x*y+2*f*x+2*f*y-f+2*x*x*y+2*x*y*y-x*y)/((2*x-1)*(2*y-1)))
first={b:2*y*y,c:2*x*x,r:x*(1-2*x),s:y*(1-2*y),A:2*x*y*(1-2*x)*(1-2*y)}
for h in E:eq(h.subs(t,1).subs(first,simultaneous=True))
pp=[S.factor(h.subs(first,simultaneous=True)) for h in Pvals];nn=[S.factor(h.subs(first,simultaneous=True)) for h in Nvals]
eq(pp[1],-x*x*(2*x-1));eq(pp[2],-y*y*(2*y-1));eq(nn[1],y*pp[1]);eq(nn[2],x*pp[2])
mu=nn[0]*nn[1]*nn[2]-pp[0]*nn[1]*nn[2]-2*y*y*pp[1]*nn[0]*nn[2]-2*x*x*pp[2]*nn[0]*nn[1]
eq(mu,4*x**6*y**6*(2*x-1)**2*(2*y-1)**2*(x+y-1))
eq(y**3*pp[1]-x**3*pp[2],x*x*y*y*(y-x))
# Second surface: native QQ(x,y) evaluation, with D the already-nonzero denominator.
ctx=fmpq_mpoly_ctx.get(('x','y'),'lex');X,Y=ctx.gens();ZZ=ctx.constant(0);OO=ctx.constant(1)
DD=8*X*Y-2*X-2*Y+1;HH=2*X+2*Y-1;JJ=2*(X-Y)**2-X-Y;WW=4*(X-Y)**2-4*X-4*Y+1;EE=4*(X-Y)**2-1
nums=[2*Y**2*(2*X-2*Y+1),-2*X**2*(2*X-2*Y-1),2*X*Y*(2*X-1)*(2*Y-1)*(2*X-2*Y-1)*(2*X-2*Y+1),X*(2*X-1)*HH,Y*(2*Y-1)*HH]
wts=[1,1,2,1,1]
def rd(n,d=OO):
 if not n:return ZZ,OO
 g=n.gcd(d);return n/g,d/g
def ra(a,b):return rd(a[0]*b[1]+b[0]*a[1],a[1]*b[1])
def rm(a,b):return rd(a[0]*b[0],a[1]*b[1])
def rn(a):return -a[0],a[1]
def req(a,b):assert a[0]*b[1]==b[0]*a[1]
def ev(expr):
 terms=S.Poly(expr,b,c,A,r,s,domain=S.QQ).terms();degree=max((sum(ei*wi for ei,wi in zip(e,wts)) for e,co in terms),default=0);out=ZZ
 for ex,co in terms:
  term=ctx.constant(fmpq(str(co)))*DD**(degree-sum(ei*wi for ei,wi in zip(ex,wts)))
  for num,ei in zip(nums,ex):term*=num**ei
  out+=term
 return rd(out,DD**degree)
for h in E:req(ev(h.subs(t,1)),(ZZ,OO))
pp=[ev(h) for h in Pvals];nn=[ev(h) for h in Nvals]
A1=12*X*Y-2*X-4*Y*Y+1;A2=-4*X*X+12*X*Y-2*Y+1
pref=X*X*Y*Y*(2*X-1)**2*(2*Y-1)**2*EE
wantP=[(pref*JJ*WW,DD**4),(X*X*(2*X-1)**2*(2*Y+1),DD),(Y*Y*(2*Y-1)**2*(2*X+1),DD)]
wantN=[(-pref*JJ*HH,DD**4),(X*X*Y*(2*X-1)**2*A1,DD**2),(X*Y*Y*(2*Y-1)**2*A2,DD**2)]
for aa,bb in zip(pp,wantP):req(aa,bb)
for aa,bb in zip(nn,wantN):req(aa,bb)
Q=32*X**3*Y-4*X**3-64*X*X*Y*Y-4*X*X*Y+4*X*X+32*X*Y**3-4*X*Y*Y-4*X*Y-X-4*Y**3+4*Y*Y-Y
mu=ra(rm(rm(nn[0],nn[1]),nn[2]),rn(rm(rm(pp[0],nn[1]),nn[2])))
mu=ra(mu,rn(rm(rm((nums[0],DD),pp[1]),rm(nn[0],nn[2]))))
mu=ra(mu,rn(rm(rm((nums[1],DD),pp[2]),rm(nn[0],nn[1]))))
req(mu,(-32*EE*JJ*Q*(2*X-1)**4*(2*Y-1)**4*X**6*Y**6,DD**8))
# All subsequent gates are small exact QQ univariate resultants/gcd.
DDs=8*x*y-2*x-2*y+1;Hs=2*x+2*y-1;Js=2*(x-y)**2-x-y;Ws=4*(x-y)**2-4*x-4*y+1;Es=4*(x-y)**2-1
as1=12*x*y-2*x-4*y*y+1;as2=-4*x*x+12*x*y-2*y+1
qs=32*x**3*y-4*x**3-64*x*x*y*y-4*x*x*y+4*x*x+32*x*y**3-4*x*y*y-4*x*y-x-4*y**3+4*y*y-y
G1=y*as1**3*Ws**2+Es*(4*y*y-1)**2*Js*Hs**3
G2=x*as2**3*Ws**2+Es*(4*x*x-1)**2*Js*Hs**3
# m=0 is impossible: a1=a2=0 forces (x-y)*H=0, and N0 returns the contradiction.
eq(as1-as2,2*(x-y)*Hs)
eq((as1+as2).subs({x:(u+v)/2,y:(u-v)/2},simultaneous=True),4*u*u-8*v*v-2*u+2)
# On J=0 the derivative coordinate is zero; use the un-divided two-node m identity.
bs=2*y*y*(2*x-2*y+1)/DDs;cs=-2*x*x*(2*x-2*y-1)/DDs
ms=x*y*as1*as2-bs*x*DDs*(2*y+1)*as2-cs*y*DDs*(2*x+1)*as1
chs=y*(4*x*x-1)**2*as1**3-x*(4*y*y-1)**2*as2**3
su={x:v*(2*v+1)/2,y:v*(2*v-1)/2}
F4=12*v**4-5*v*v+1
G14=768*v**14-512*v**12-224*v**10+336*v**8-125*v**6+11*v**4+v*v+1
eq(ms.subs(su,simultaneous=True),v*v*(2*v-1)**3*(2*v+1)**3*F4/4)
eq(chs.subs(su,simultaneous=True),v*(2*v-1)**3*(2*v+1)**3*G14)
assert S.gcd(S.Poly(F4,v,domain=S.QQ),S.Poly(G14,v,domain=S.QQ)).monic()==S.Poly(1,v,domain=S.QQ)
assert S.resultant(F4,G14,v)==5699868278390784
# On J!=0, Q=G1=G2=0. Do not divide by x-y until its zero fiber is separately checked.
def symmetric(poly):
 pp=S.Poly(S.expand(poly.subs({x:(u+v)/2,y:(u-v)/2},simultaneous=True)),v)
 assert all(ex[0]%2==0 for ex,co in pp.terms())
 return S.expand(sum(co*z**(ex[0]//2) for ex,co in pp.terms()))
qq=symmetric(qs);gg=symmetric(G1+G2);hh=symmetric(S.cancel((G1-G2)/(x-y)))
eq(qq,-2*u**3+8*u*u*z+u*u-2*u*z-u-8*z*z+3*z)
assert S.gcd(S.Poly(qq.subs(z,0),u,domain=S.QQ),S.Poly(gg.subs(z,0),u,domain=S.QQ)).monic()==S.Poly(u,u,domain=S.QQ)
R1=S.resultant(qq,gg,z);R2=S.resultant(qq,hh,z)
assert S.gcd(S.Poly(R1,u,domain=S.QQ),S.Poly(R2,u,domain=S.QQ)).monic()==S.Poly((u-S.Rational(1,2))**11,u,domain=S.QQ)
signal.alarm(0)
print(json.dumps({'schema':'r150-unit211-zero-base-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'p=q=0 only; full t0, half-coordinate, both mean surfaces and all J0/diagonal fibers','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'resultantDegrees':[S.degree(R1,u),S.degree(R2,u)],'genericGcd':'(u-1/2)^11','JzeroResultant':5699868278390784,'elapsedSeconds':round(monotonic()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'ordinaryISPClaim':False},sort_keys=True,default=int),flush=True)

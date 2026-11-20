#!/usr/bin/env python3
# Author: Astra-ISP-b2a9acde-20261120 / r150_structure and root; AI-assisted GPT-6 Astra Pro.
"""Original QQ sources for the p!=0 half-weight unit3+1 branch.
Only expansion, degree-two remainders, and two univariate QQ gcds.
"""
import sympy as S
from time import monotonic
started=monotonic()
A,h,B,q,jj=S.symbols("A h B q jet")
one=S.Matrix([1,0,0,1])
half=S.Rational(1,2)
def clean(x):return S.cancel(S.expand(x))
def eq(x,y=0):assert clean(x-y)==0,(x,y)
def amul(x,y):
    return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],
                     x[0]*y[2]+x[1]*y[1]+x[2]*y[0],x[3]*y[3]])
def tau(x):return x[0]/2+x[2]+x[3]/2
C=-A*(2*h+1)
r=(h+1)*(2*A+1)
K=S.Matrix([[0,0,A,1],[0,-2*A,B,q],[A,B,C,r],[1,q,r,0]])
def DK(x):return S.Matrix([tau(amul(K.row(i).T,x)) for i in range(4)])
d=DK(one);F=tau(d)/2
def center(x):return x-tau(x)*one
def pv(x):
    z=center(x);return clean(tau(amul(z,amul(z,z)))/2)
def nv(x):
    return clean(tau(amul(d-F*one,amul(x,x)))/2
                 -tau(x)*tau(amul(d,x))+F*tau(x)**2
                 +tau(amul(x,DK(x)))/4)
rows=[K.row(i).T for i in range(4)]
ev=S.Matrix([tau(amul(rows[0],rows[0])),
             2*tau(amul(rows[0],rows[1])),
             2*tau(amul(rows[0],rows[2]))+tau(amul(rows[1],rows[1])),
             tau(amul(rows[3],rows[3]))])
mean=[clean(x) for x in ev-2*DK(d)-2*amul(d,d)+4*F*d]
Q=2*h*h+2*h+1
R2=2*A*A*(h+1)*(1-2*h)-3*A*Q
RP=-2*A*(Q+2*A*(h+1)*(2*h+1))
eq(F,A+h/2+S.Rational(3,4))
eq(mean[0])
eq(mean[1],2*((A+h)*B-A*h*q))
eq(mean[2],R2-4*B*B-3*B*q)
eq(mean[3],RP-2*B*q)
print("PASS complete half-weight original mean form",flush=True)

xj=K[:,0]+jj*K[:,1]+jj**2*K[:,2]
ps=S.expand(pv(xj));ns=S.expand(nv(xj))
p0,p1,p2=[ps.coeff(jj,i) for i in range(3)]
n0,n1,n2=[ns.coeff(jj,i) for i in range(3)]
eq(p0,A*A*(A+S.Rational(3,2)))
eq(n0,-A*A*(2*h+1)/4)
c0=clean(3*p0*n1-2*n0*p1)
c1=clean(6*p0*n2+p1*n1-4*n0*p2)
u,v,w,m=S.symbols("u v w m")
pp0=-u**3;pp1=-3*u*u*v;pp2=-3*u*u*w-3*u*v*v
nn0=-m*u*u;nn1=-2*m*u*v;nn2=-m*(v*v+2*u*w)
eq(3*pp0*nn1-2*nn0*pp1)
eq(6*pp0*nn2+pp1*nn1-4*nn0*pp2)
print("PASS original three jets and both division-free compatibilities",flush=True)

eq(R2.subs({A:-half,h:0},simultaneous=True),2)
T=4*h**3+4*h*h-1
B2=h*(3+8*h+4*h*h-4*h**3)/4
eq(RP.subs(A,-h),-2*h*T)
eq(R2.subs(A,-h),4*B2)
cc=clean(c1.subs({A:-h,q:0},simultaneous=True))
cc=S.rem(S.Poly(cc,B,domain=S.QQ.frac_field(h)),
         S.Poly(B*B-B2,B,domain=S.QQ.frac_field(h))).as_expr()
R=68*h*h-28*h-23
rem=S.rem(S.Poly(clean(cc-3*h**3*R/8),h,domain=S.QQ),
          S.Poly(T,h,domain=S.QQ))
assert rem.is_zero
eq(S.rem(S.Poly(T,h,domain=S.QQ),S.Poly(R,h,domain=S.QQ)).as_expr(),
   (1063*h+263)/S.Integer(289))
assert S.gcd(S.Poly(T,h,domain=S.QQ),S.Poly(R,h,domain=S.QQ)).monic()==S.Poly(1,h,domain=S.QQ)
print("PASS A+h=0 complete exception and its QQ obstruction",flush=True)

C0=4*h*h+6*h+3
alpha=A+h
eq(2*alpha*R2-(4*h*A+3*alpha)*RP,
   8*A*A*(2*A*(h+1)*Q+h*C0))
AA=-h*C0/(2*(h+1)*Q)
lam=-h*C0/T
q2=T*T/(2*Q*Q)
eq(AA+h,h*T/(2*(h+1)*Q))
eq(AA*h/(AA+h),lam)
eq(clean(RP.subs(A,AA))/(2*lam),q2)
f=16*h**5+56*h**4+92*h**3+86*h*h+45*h+12
g=144*h**6+584*h**5+1124*h**4+1268*h**3+893*h*h+372*h+75
sub={A:AA,B:lam*q}
def rq(x):
    return S.rem(S.Poly(clean(x),q,domain=S.QQ.frac_field(h)),
                 S.Poly(q*q-q2,q,domain=S.QQ.frac_field(h))).as_expr()
for x in mean:eq(rq(x.subs(sub,simultaneous=True)))
eq(rq(c0.subs(sub,simultaneous=True)),
   3*q*AA**4*f/(4*(h+1)*Q*T))
eq(rq(c1.subs(sub,simultaneous=True)),
   -3*AA**4*g/(8*(h+1)**2*Q**2))
assert S.gcd(S.Poly(f,h,domain=S.QQ),S.Poly(g,h,domain=S.QQ)).monic()==S.Poly(1,h,domain=S.QQ)
print("PASS regular original mean/jet identities and degree5/6 QQ gcd=1",flush=True)
print("ALL PASS: half-weight unit3+1 p!=0 sources",
      "seconds",round(monotonic()-started,3),flush=True)

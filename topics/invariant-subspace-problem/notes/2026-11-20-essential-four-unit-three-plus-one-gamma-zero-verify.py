#!/usr/bin/env python3
"""Original QQ sources for gamma=0 in the nonhalf unit3+1 chart.
AI-assisted research: Astra-ISP / r150_structure.
Only exact expansion, two small b-resultants, and a univariate QQ gcd.
"""
import sympy as S
from time import monotonic
started=monotonic()
b,x,k,B,q,s=S.symbols("b x kappa B q s")
one=S.Matrix([1,0,0,1])
def clean(z):return S.cancel(S.expand(z))
def eq(z,w=0):assert clean(z-w)==0,(z,w)
def amul(z,w):
    return S.Matrix([z[0]*w[0],z[0]*w[1]+z[1]*w[0],
                     z[0]*w[2]+z[1]*w[1]+z[2]*w[0],z[3]*w[3]])
a=1-b;delta=1-2*b
A=x-b;r=x*(1+k)-delta/2;C=b*(delta+k*(1-2*x))
K=S.Matrix([[0,0,A,1],[0,-2*A,B,q],[A,B,C,r],[1,q,r,0]])
def tau(z):return a*z[0]+z[2]+b*z[3]
def DK(z):return S.Matrix([tau(amul(K.row(i).T,z)) for i in range(4)])
d=DK(one);F=tau(d)/2
def cen(z):return z-tau(z)*one
def pv(z):
    zz=cen(z);return clean(tau(amul(zz,amul(zz,zz)))/2)
def pj(z,w):return clean(3*tau(amul(amul(cen(z),cen(z)),cen(w)))/2)
def nv(z):
    return clean(tau(amul(d-F*one,amul(z,z)))/2
                 -tau(z)*tau(amul(d,z))+F*tau(z)**2
                 +tau(amul(z,DK(z)))/4)
def nj(z,w):
    return clean(tau(amul(d-F*one,amul(z,w)))
                 -tau(z)*tau(amul(d,w))-tau(w)*tau(amul(d,z))
                 +2*F*tau(z)*tau(w)+tau(amul(z,DK(w)))/2)
rows=[K.row(i).T for i in range(4)]
ev=S.Matrix([tau(amul(rows[0],rows[0])),
             2*tau(amul(rows[0],rows[1])),
             2*tau(amul(rows[0],rows[2]))+tau(amul(rows[1],rows[1])),
             tau(amul(rows[3],rows[3]))])
mean=[clean(z) for z in ev-2*DK(d)-2*amul(d,d)+4*F*d]
alpha=x+b*(k-2);beta0=S.Rational(1,2)-k*x
eq(F,x+b*k/2);eq(mean[0])
eq(mean[1],2*(alpha*(B+b*q)+b*beta0*q))
R2=clean(mean[2].subs({B:0,q:0},simultaneous=True))
RP=clean(mean[3].subs({B:0,q:0},simultaneous=True))
eq(mean[2],R2-4*B*B-6*b*B*q+b*delta*q*q)
eq(mean[3],RP-2*B*q+delta*q*q)
p0=pv(K[:,0]);p1=pj(K[:,0],K[:,1])
p2=clean(pj(K[:,0],K[:,2])
         +3*tau(amul(cen(K[:,0]),amul(cen(K[:,1]),cen(K[:,1]))))/2)
n0=nv(K[:,0]);n1=nj(K[:,0],K[:,1])
n2=clean(nv(K[:,1])+nj(K[:,0],K[:,2]))
c0=clean(3*p0*n1-2*n0*p1)
c1=clean(6*p0*n2+p1*n1-4*n0*p2)
cb=clean(S.diff(c0,B));cq=clean(S.diff(c0,q))
eq(c0,cb*B+cq*q)

# q!=0 chart s=B/q+b, without dividing any unknown original source value.
p1s=clean(p1.subs(B,(s-b)*q))
c0s=clean(c0.subs(B,(s-b)*q)/q)
eq(mean[1].subs(B,(s-b)*q),2*q*(alpha*s+b*beta0))
eq(p1s,3*q*((x*x-b/2)*s+b*(1-2*x)/2))
eq(c0s,3*(p0*(x-b)*(2*x*s-b)+n0*(2*x*x-b)*(x-s)))
eq(mean[3].subs(B,(s-b)*q),RP+(1-2*s)*q*q)
eq(mean[2].subs(B,(s-b)*q),R2+(b*(1+2*s)-4*s*s)*q*q)
eq((alpha*s+b*beta0).subs(s,x),x*x-2*b*x+b/2)

# Complete s=x exclusion and the p0=0 return to that same excluded boundary.
bx=2*x*x/(4*x-1)
eq((x*x-2*b*x+b/2).subs(b,bx))
eq(c0s.subs({s:x,b:bx},simultaneous=True),
   12*x**5*(2*x-1)**4/(4*x-1)**3)
bp=2*x**3/(3*x-1)
eq(p0.subs(b,bp))
eq(p1s.subs(b,bp),3*q*x*x*(2*x-1)*(s-x)/(3*x-1))
print("PASS original s chart, s!=x obstruction and p0!=0 lemma",flush=True)

# s=1/2. The original mean first excludes x=1/2 unless b=1/2.
half=S.Rational(1,2)
eq((alpha*s+b*beta0).subs({s:half,x:half},simultaneous=True),(1-2*b)/4)
D=b*(1-2*x);kk=(b-x)/D
eq((alpha*s+b*beta0).subs({s:half,k:kk},simultaneous=True))
RPh=clean(D**2*RP.subs(k,kk))
R2h=clean(R2.subs(k,kk))
C0=clean(c0s.subs({s:half,k:kk},simultaneous=True))
qsq=clean(R2h/delta)
cq=S.Poly(clean(c1.subs({B:(half-b)*q,k:kk},simultaneous=True)),
          q,domain=S.QQ.frac_field(b,x))
assert cq.degree()<=2
eq(cq.nth(1))
C1=clean(b*(1-2*x)**2*delta*(cq.nth(0)+cq.nth(2)*qsq))
PP=S.Poly(RPh,b,x,domain=S.QQ)
CC0=S.Poly(C0,b,x,domain=S.QQ)
CC1=S.Poly(C1,b,x,domain=S.QQ)
assert [PP.degree(b),CC0.degree(b),CC1.degree(b)]==[3,3,6]
print("PASS gamma=0 original mean and compatibility polynomial sources",flush=True)

res0=S.Poly(S.resultant(PP.as_expr(),CC0.as_expr(),b),x,domain=S.QQ)
res1=S.Poly(S.resultant(PP.as_expr(),CC1.as_expr(),b),x,domain=S.QQ)
eq(res0.as_expr(),-S.Rational(27,64)*x**10*(2*x-1)**9*(8*x+15))
assert res1.degree()==39
gg=S.gcd(res0,res1).monic()
assert gg==S.Poly(x**10*(x-half)**9,x,domain=S.QQ),gg
eq(RPh.subs(x,0),b*b*(b-half))
print("PASS exact QQ resultants, gcd, and both returns to the original mean",flush=True)
print("ALL PASS: unit3+1 nonhalf gamma-zero sources",
      "seconds",round(monotonic()-started,3),flush=True)

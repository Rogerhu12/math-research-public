#!/usr/bin/env python3
"""Original QQ verification of the regular two-parameter unit3+1 chart.
AI-assisted research: Astra-ISP / r150_structure.
A degree-four QQ gcd and one cubic/quadratic b-resultant.
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

c0s=clean(c0.subs(B,(s-b)*q)/q)
eq(c0s,3*(p0*(x-b)*(2*x*s-b)+n0*(2*x*x-b)*(x-s)))
cq=S.Poly(clean(c1.subs(B,(s-b)*q)),q,domain=S.QQ.frac_field(b,x,k,s))
assert cq.degree()<=2
eq(cq.nth(1))

# x=0. Mean_1 and c0 have the displayed unique solution for kappa and s.
ss=-5*b/(2*(1-4*b));kk=(1+6*b)/(5*b)
sb={x:0,k:kk,s:ss}
eq((alpha*s+b*beta0).subs(sb,simultaneous=True))
eq(c0s.subs(sb,simultaneous=True))
eq(1-2*ss,(1+b)/(1-4*b))
qq=(32*b*b-36*b+7)/(10*(b+1))
eq(RP.subs(sb,simultaneous=True)+(1-2*ss)*qq)
ee=clean(R2.subs(sb,simultaneous=True)+(b*(1+2*ss)-4*ss*ss)*qq)
cc=clean((cq.nth(0)+cq.nth(2)*qq).subs(sb,simultaneous=True))
M4=3456*b**4-1136*b**3+981*b*b-56*b-4
C4=-7232*b**4+1672*b**3+8*b*b+447*b-32
eq(ee,M4/(50*(4*b-1)*(b+1)))
eq(cc,3*b*b*C4/(400*(4*b-1)*(b+1)))
assert S.gcd(S.Poly(M4,b,domain=S.QQ),
             S.Poly(C4,b,domain=S.QQ)).monic()==S.Poly(1,b,domain=S.QQ)
print("PASS x=0: original mean/c1 identities and exact quartic QQ gcd=1",
      flush=True)

# Solve the mean_1 for kappa using the previously proved s!=x.
kk=(s*(2*b-x)-b/2)/(b*(s-x))
L=-4*b**3+(16*x*x+x+1)*b*b-20*x**3*b+4*x**4*(x+1)
Cb=(S.Rational(5,2)-4*x)*b*b+(6*x*x-4*x)*b-6*x**4+4*x**3
eq((alpha*s+b*beta0).subs(k,kk))
eq(c0s.subs(k,kk),3*(L*s+b*Cb)/4)
rr=S.resultant(L,Cb,b)
eq(rr,-200*x**6*(2*x-1)**7)
eq(Cb.subs(x,0),5*b*b/2)
eq(Cb.subs(x,S.Rational(1,2)),(b-S.Rational(1,2))**2/2)
J=(8*x-S.Rational(5,2))*b*b+(-12*x*x+3*x)*b+2*x**4+2*x**3
eq(b*Cb+x*L,(2*x*x-b)*J)
print("PASS L=0 full boundary: exact small resultant and both original returns",
      flush=True)
print("ALL PASS: unit3+1 regular two-parameter chart sources",
      "seconds",round(monotonic()-started,3),flush=True)

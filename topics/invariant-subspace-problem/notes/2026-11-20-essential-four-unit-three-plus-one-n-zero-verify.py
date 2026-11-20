#!/usr/bin/env python3
"""Original QQ sources excluding n0=0 in the nonhalf unit3+1 chart.
AI-assisted research: Astra-ISP / r150_structure.
Only exact rational identities from original mean, highest, and N sources.
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
n1s=clean(n1.subs(B,(s-b)*q)/q)
eq(c0s,3*(p0*(x-b)*(2*x*s-b)+n0*(2*x*x-b)*(x-s)))
eq(n1s,(x-b)*(2*x*s-b)+2*n0)
eq(c0s.subs(b,2*x*x),6*x**4*(2*x-1)**2*(s-x))
nq=S.Poly(clean(n2.subs(B,(s-b)*q)),q,domain=S.QQ.frac_field(b,x,k,s))
assert nq.degree()<=2
eq(nq.nth(1))
print("PASS original n0/n1/n2 sources and T=0 return to s=x",flush=True)

# n0=0, x=b. Because p0!=0, the original highest and N imply m=0
# and in particular n2=0. The resulting n2 below is nonzero on this chart.
eq(n0.subs(x,b),b*(1-2*b)*(1+b*k)/4)
sb={x:b,k:-1/b}
eq((alpha*s+b*beta0).subs(sb,simultaneous=True),-(b+1)*s+3*b/2)
ss=3*b/(2*(b+1))
eq(RP.subs(sb,simultaneous=True),(1-2*b)/2)
eq(1-2*ss,(1-2*b)/(b+1))
qq=-(b+1)/2
eq(RP.subs(sb,simultaneous=True)+(1-2*ss)*qq)
sb={x:b,k:-1/b,s:ss}
nn=clean((nq.nth(0)+nq.nth(2)*qq).subs(sb,simultaneous=True))
eq(nn,-b*b*(2*b-1)**2/(16*(b+1)))
print("PASS x=b: original mean return and nonzero n2",flush=True)

# n0=0, x!=b. The original n1=0 forces 2*x*s=b.
T=2*x*x-b
kk=2*(x-b)/T
ss=b/(2*x)
sb={s:ss,k:kk}
eq((alpha*s+b*beta0).subs(sb,simultaneous=True))
G=4*b*b-(6*x+1)*b-4*x**3+6*x*x
eq(n0.subs(k,kk),b*G/(4*T))
RP2=clean(RP.subs(k,kk));R22=clean(R2.subs(k,kk))
lp=1-2*ss;l2=b*(1+2*ss)-4*ss*ss
eq(lp,(x-b)/x)
qq=clean(-RP2/lp)
h=x*x-2*b*x+b/2
eq(R22+l2*qq,T*h/(x*(x-b)))
bb=2*x*x/(4*x-1)
eq(h.subs(b,bb))
eq(G.subs(b,bb),-8*x*x*(2*x-1)**3/(4*x-1)**2)
print("PASS x!=b: original mean obstruction and return to the half-weight",flush=True)
print("ALL PASS: unit3+1 nonhalf n-zero sources",
      "seconds",round(monotonic()-started,3),flush=True)

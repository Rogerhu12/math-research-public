#!/usr/bin/env python3
# Author: Astra-ISP-b2a9acde-20261120 / r150_structure and root; AI-assisted GPT-6 Astra Pro.
"""Original QQ identities for the entire p=0 unit 3+1 isolated-zero branch.
No Groebner computation, finite-field step, or stored elimination tables.
"""
import sympy as S
from time import monotonic
started=monotonic()
b,q,r,s,kappa=S.symbols("b q r s kappa")
one=S.Matrix([1,0,0,1])
def clean(x):
    return S.cancel(S.expand(x))
def eq(x,y=0):
    assert clean(x-y)==0,(x,y)
def amul(x,y):
    return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],
                     x[0]*y[2]+x[1]*y[1]+x[2]*y[0],x[3]*y[3]])
def core(K,weight):
    a=1-weight
    def tau(x):
        return a*x[0]+x[2]+weight*x[3]
    def DK(x):
        return S.Matrix([tau(amul(K.row(i).T,x)) for i in range(4)])
    d=DK(one);phi=tau(d)/2
    def center(x):
        return x-tau(x)*one
    def pv(x):
        z=center(x)
        return clean(tau(amul(z,amul(z,z)))/2)
    def pj(x,v):
        z=center(x)
        return clean(3*tau(amul(amul(z,z),center(v)))/2)
    def nv(x):
        return clean(tau(amul(d-phi*one,amul(x,x)))/2
                     -tau(x)*tau(amul(d,x))+phi*tau(x)**2
                     +tau(amul(x,DK(x)))/4)
    def nj(x,v):
        return clean(nv(x+v)-nv(x)-nv(v))
    rows=[K.row(i).T for i in range(4)]
    e=S.Matrix([tau(amul(rows[0],rows[0])),
                2*tau(amul(rows[0],rows[1])),
                2*tau(amul(rows[0],rows[2]))+tau(amul(rows[1],rows[1])),
                tau(amul(rows[3],rows[3]))])
    mean=[clean(x) for x in e-2*DK(d)-2*amul(d,d)+4*phi*d]
    return mean,clean(phi),pv,pj,nv,nj

# A=1,p=0: the first two mean coefficients determine B,C.
B=b*q*(r-2);C=2*b*(1-r)
K=S.Matrix([[0,0,1,0],[0,-2,B,q],[1,B,C,r],[0,q,r,0]])
mean,phi,pv,pj,nv,nj=core(K,b)
eq(phi,1);eq(mean[0]);eq(mean[1])
ep=q*q*(1+2*b*(1-r))+2*r*(1-r)
e2=2+b*q*q-4*b+6*b*r-2*b*r*r+b*b*q*q*(-4*r*r+10*r-6)
eq(mean[3],ep);eq(mean[2],e2)
eq(pv(K[:,0]),1);eq(nv(K[:,0]))
eq(nj(K[:,0],K[:,1]),b*q*(r-1))
K0=K.subs({q:0,r:0,b:S.Rational(1,2)},simultaneous=True)
m0,f0,p0,p01,n0,n01=core(K0,S.Rational(1,2))
eq(n0(K0[:,1]),-2);eq(n01(K0[:,0],K0[:,2]),-1)
print("PASS A!=0: original means, highest/N base, first jet, second jet=-3",flush=True)

# A=p=0,q=1,F=0: all remaining candidates force the forbidden isotropic triple.
delta=1-2*b
B=delta/2
KF=S.Matrix([[0,0,0,0],[0,0,B,1],[0,B,0,0],[0,1,0,0]])
mf,ff,*_=core(KF,b)
eq(ff);eq(mf[0]);eq(mf[1]);eq(mf[3]);eq(mf[2],-delta)
print("PASS A=p=0,F=0 exceptional source",flush=True)

# A=p=0,q=1,F!=0: complete three-parameter mean chart.
B=s-b;C=b*kappa*(1-2*s);R=kappa*s
K=S.Matrix([[0,0,0,0],[0,0,B,1],[0,B,C,R],[0,1,R,0]])
mean,phi,*_=core(K,b)
eq(phi,b*kappa/2);eq(mean[0]);eq(mean[1])
ep=1-2*s+2*kappa*kappa*s*(b-s)
e2=b*(1+2*s)-4*s*s+2*b*kappa*kappa*(b*(1-s)-s*s)
eq(mean[3],ep);eq(mean[2],e2)
eq(s*(b-s)*e2-b*(b*(1-s)-s*s)*ep,
   (b-2*s*s)*((4*s-1)*b-2*s*s))
print("PASS complete mean chart and division-free factorization",flush=True)

def reduce_r(f,relation):
    field=S.QQ.frac_field(s)
    return S.rem(S.Poly(clean(f),r,domain=field),
                 S.Poly(relation,r,domain=field)).as_expr()

# Family I, retaining the actual active-point and zero-point sources.
bi=2*s*s;Bi=s-bi
KI=S.Matrix([[0,0,0,0],[0,0,Bi,1],[0,Bi,2*r*Bi,r],[0,1,r,0]])
mi,fi,pvi,pji,nvi,nji=core(KI,bi)
relI=r*r-S.Rational(1,2)
for x in mi:eq(reduce_r(x,relI))
eq(reduce_r(pvi(KI[:,3]),relI),-r)
eq(reduce_r(nvi(KI[:,3]),relI),-r*s)
for entry in KI*S.Matrix([0,-r,1,-Bi]):eq(entry)
print("PASS family I original point values and explicit second Gram kernel",flush=True)

# Family II and the two jets after cancellation in the actual original germ.
d0=4*s-1
bii=2*s*s/d0;Bii=s-bii
KII=S.Matrix([[0,0,0,0],[0,0,Bii,1],
              [0,Bii,-2*r*Bii,r],[0,1,r,0]])
mii,fii,pvii,pjii,nvii,njii=core(KII,bii)
relII=r*r+d0/2
for x in mii:eq(reduce_r(x,relII))
P0=pvii(KII[:,1]);P1=pjii(KII[:,1],KII[:,2])
N0=nvii(KII[:,1]);N1=njii(KII[:,1],KII[:,2])
eq(reduce_r(P0,relII),s*s*(2*s-1)**2/d0)
eq(reduce_r(N0,relII),-r*s*s*(2*s-1)**2/d0**2)
eq(reduce_r(P1,relII),-3*r*s*s*(2*s-1)**2*(2*s+1)/d0**2)
eq(reduce_r(N1,relII),s*s*(2*s-1)**3/d0**2)
eq(reduce_r(3*P0*N1-2*N0*P1,relII),
   12*s**5*(2*s-1)**4/d0**3)
v,w,m=S.symbols("v w m")
eq(3*(-v**3)*(-2*m*v*w)-2*(-m*v*v)*(-3*v*v*w))
print("PASS family II original divided-germ jet compatibility obstruction",flush=True)
print("ALL PASS: p=0 unit3+1 source identities",
      "seconds",round(monotonic()-started,3),flush=True)

#!/usr/bin/env python3
# Author: Astra-ISP-b2a9acde-20261120 / r150_structure and root; AI-assisted GPT-6 Astra Pro.
"""Original QQ sources for alpha=0 in the nonhalf unit3+1 chart.
Only expansion, quadratic remainders, and one univariate QQ gcd.
"""
import sympy as S
from time import monotonic
started=monotonic()
b,x,k,B,q,v=S.symbols("b x kappa B q v")
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
print("PASS original mean parametrization and first/second local compatibility sources",
      flush=True)

# alpha=0, q!=0.
bb=2*x*x/(4*x-1);kk=1/(2*x)
sub={b:bb,k:kk}
eq(alpha.subs(sub,simultaneous=True))
eq(beta0.subs(sub,simultaneous=True))
cb1=clean(cb.subs(sub,simultaneous=True))
cq1=clean(cq.subs(sub,simultaneous=True))
eq(cb1,6*x**4*(2*x-1)**3*(4*x+1)/(4*x-1)**3)
eq(cq1,6*x**5*(2*x-1)**4*(4*x-3)/(4*x-1)**4)
z=-x*(2*x-1)*(4*x-3)/((4*x-1)*(4*x+1))
eq(cb1*z+cq1)
R21=clean(R2.subs(sub,simultaneous=True))
RP1=clean(RP.subs(sub,simultaneous=True))
LP=1-2*bb-2*z;L2=-4*z*z-6*bb*z+bb*(1-2*bb)
eq(R21,6*x*x*(1-2*x)/(4*x-1)**2)
eq(RP1,(1-2*x)/(4*x-1))
eq(LP,(1-2*x)/(4*x+1))
eq(R21*LP-RP1*L2,32*x*x*(2*x-1)**3/(16*x*x-1)**2)
print("PASS q!=0 complete rational obstruction without any q^2 division",flush=True)

# alpha=0, q=0, retaining the actual quadratic relation for the weight b.
sub0={x:b*v,k:2-v,q:0}
eq(alpha.subs(sub0,simultaneous=True))
eq(RP.subs(sub0,simultaneous=True),-S.Rational(1,2)-2*b*b*v*(v-2)**3)
H=-1/(4*v*(v-2)**3)
def rb(z):
    return S.rem(S.Poly(clean(z),b,domain=S.QQ.frac_field(v)),
                 S.Poly(b*b-H,b,domain=S.QQ.frac_field(v))).as_expr()
R20=(2*b*v-1)/(v*(v-2))
eq(rb(R2.subs(sub0,simultaneous=True)),R20)
F2=v*v-8*v+8;G3=5*v**3-18*v*v+28*v-16
CB=3*(F2+2*b*G3)/(16*v*(v-2)**6)
eq(rb(cb.subs(sub0,simultaneous=True)),CB)
cc=clean(c1.subs(sub0,simultaneous=True))
cc=S.rem(S.Poly(cc,B,domain=S.QQ.frac_field(b,v)),
         S.Poly(B*B-R20/4,B,domain=S.QQ.frac_field(b,v))).as_expr()
F6=4*v**6-61*v**5+293*v**4-638*v**3+796*v*v-656*v+288
G6=-10*v**6+73*v**5-127*v**4-218*v**3+1012*v*v-1280*v+576
C1=3*(F6+2*b*v*(v-2)*G6)/(64*v*v*(v-2)**9)
eq(rb(cc),C1)
print("PASS q=0 original mean and compatibility remainders",flush=True)

N1=((v-2)**3+v)*(v*(v-2)**3*F2**2+G3**2)
N2=(v-2)*F6**2+v*G6**2
prod=R20*CB
eq(rb(prod*prod.subs(b,-b)),9*N1/(256*v**5*(v-2)**20))
eq(rb(C1*C1.subs(b,-b)),9*N2/(4096*v**4*(v-2)**19))
gcd=S.gcd(S.Poly(N1,v,domain=S.QQ),S.Poly(N2,v,domain=S.QQ)).monic()
assert gcd==S.Poly((v-1)**2,v,domain=S.QQ)
eq(R20.subs(v,1),1-2*b)
eq(CB.subs(v,1),3*(1-2*b)/16)
eq(prod.subs(v,1),3*(1-2*b)**2/16)
print("PASS both exact norm identities, QQ gcd=(v-1)^2, and return to original source",
      flush=True)
print("ALL PASS: unit3+1 alpha=0 sources",
      "seconds",round(monotonic()-started,3),flush=True)

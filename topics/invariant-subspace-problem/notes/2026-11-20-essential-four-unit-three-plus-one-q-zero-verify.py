#!/usr/bin/env python3
# Author: Astra-ISP-b2a9acde-20261120 / r150_structure and root; AI-assisted GPT-6 Astra Pro.
"""Original QQ verification for q=0, alpha!=0 in the nonhalf unit3+1 chart.
AI-assisted research: Astra-ISP / r150_structure.
Only exact expansions, quadratic remainders and univariate QQ gcds.
No finite-field assertion and no multivariate Groebner computation.
"""
import sympy as S
from time import monotonic
started=monotonic()
b,x,k,u=S.symbols("b x kappa u")
one=S.Matrix([1,0,0,1])
def clean(z):return S.cancel(S.expand(z))
def eq(z,w=0):assert clean(z-w)==0,(z,w)
def amul(z,w):
    return S.Matrix([z[0]*w[0],z[0]*w[1]+z[1]*w[0],
                     z[0]*w[2]+z[1]*w[1]+z[2]*w[0],z[3]*w[3]])
a=1-b;delta=1-2*b
A=x-b;r=x*(1+k)-delta/2;C=b*(delta+k*(1-2*x))
K=S.Matrix([[0,0,A,1],[0,-2*A,0,0],[A,0,C,r],[1,0,r,0]])
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
alpha=x+b*(k-2)
Db=2-k+2*x*k*(k+2)
Nb=x+S.Rational(1,2)+2*x*x*k*(1+k)
R2=(2*x*x-7*b*x+6*b*b-b/2+2*b*x*x*k+b*b*k-4*b*b*x*k
    -2*b*x*x*k*k+2*b*b*k*k-2*b*b*x*k*k)
eq(F,x+b*k/2);eq(mean[0]);eq(mean[1])
eq(mean[2],R2);eq(mean[3],b*Db-Nb)
p0=pv(K[:,0]);p1=pj(K[:,0],K[:,1])
p2=clean(pj(K[:,0],K[:,2])
         +3*tau(amul(cen(K[:,0]),amul(cen(K[:,1]),cen(K[:,1]))))/2)
n0=nv(K[:,0]);n1=nj(K[:,0],K[:,1])
n2=clean(nv(K[:,1])+nj(K[:,0],K[:,2]))
eq(p1);eq(n1)
c1=clean(6*p0*n2-4*n0*p2)
ps=pv(K[:,3]);ns=nv(K[:,3])
print("PASS original q=0 mean and local/point compatibility sources",flush=True)

# The denominator-zero mean boundary, before any division by Db.
dx=(k-2)/(2*k*(k+2))
eq(Nb.subs(x,dx),(k*k+k+2)/(k+2)**2)
rb=S.rem(S.Poly(clean(R2.subs(x,S.Rational(1,2))),k,
                domain=S.QQ.frac_field(b)),
         S.Poly(k*k+k+2,k,domain=S.QQ.frac_field(b))).as_expr()
eq(rb,(2*b-1)*((2-k)*b-S.Rational(1,2)))
eq(alpha.subs({x:S.Rational(1,2),b:1/(2*(2-k))},simultaneous=True))

# The complete regular mean factorization.
Q=(k+1)*(k+2)*u*u+2*(k+2)*u+k*k+k+2
eq(clean(R2.subs(b,Nb/Db))*Db**2,
   -(2*x-1)*((2*x*k)**2+1)*Q.subs(u,2*x*k)/2)
D=(k+2)*u+2-k
Sn=(k+1)*u*u+u+k
eq((k+2)*Sn+D,Q)
print("PASS complete mean factorization and Db=0 boundary",flush=True)

field=S.QQ.frac_field(k)
def quadratic_reducer(rel):
    pr=S.Poly(rel,u,domain=field)
    def red(z):
        return S.rem(S.Poly(clean(z),u,domain=field),pr).as_expr()
    return red
def norm_of(z,red,L,M):
    z=S.Poly(red(z),u,domain=field)
    aa=z.nth(0);cc=z.nth(1)
    return clean(aa*aa+L*aa*cc-M*cc*cc)
def qq_numerator(z):
    return S.Poly(S.fraction(clean(z))[0],k,domain=S.QQ)
def sources_in_quad(bb,xx,rel):
    red=quadratic_reducer(rel)
    sb={b:bb,x:xx}
    pp,nn,ss,nt,cc=[red(z.subs(sb,simultaneous=True))
                    for z in [p0,n0,ps,ns,c1]]
    chi=red(nn**3*ss**2-nt**3*pp**2)
    return red,cc,chi

# Q=0 component. k, k+1 and k+2 have already been excluded geometrically.
L=-2/(k+1)
M=-(k*k+k+2)/((k+1)*(k+2))
red,cc,chi=sources_in_quad(-1/(2*k*(k+2)),u/(2*k),u*u-L*u-M)
nc=norm_of(cc,red,L,M);nh=norm_of(chi,red,L,M)
H10=(k**10+11*k**9+49*k**8+99*k**7+125*k**6+175*k**5
     +226*k**4+152*k**3-32*k*k-48*k+32)
eq(nc,9*(k+1)*H10/(256*k**12*(k+2)**9))
gc=S.gcd(qq_numerator(nc),qq_numerator(nh)).monic()
assert gc==S.Poly(k+1,k,domain=S.QQ),gc
print("PASS Q component: original-source norm gcd=kappa+1",flush=True)

# u^2+1=0 component: handle k^2+4=0 before rationalizing the weight.
redI=quadratic_reducer(u*u+1)
eq(redI(D.subs(k,2*u)))
eq(redI(D.subs(k,-2*u)),4*(u+1))
eq(redI((u-1)*(k*k+4)-(k+2*u)*D))
ce=S.rem(S.Poly(c1.subs({b:-S.Rational(1,16),x:-S.Rational(1,4)},
                       simultaneous=True),k,domain=S.QQ),
         S.Poly(k*k+4,k,domain=S.QQ)).as_expr()
eq(ce,-243*(k+4)/65536)
assert S.gcd(S.Poly(ce,k,domain=S.QQ),
             S.Poly(k*k+4,k,domain=S.QQ)).degree()==0
red,cc,chi=sources_in_quad((k+2*u)/(2*k*(k*k+4)),u/(2*k),u*u+1)
nc=norm_of(cc,red,0,-1);nh=norm_of(chi,red,0,-1)
eq(nc,45*(k*k+1)**4*(5*k*k+8*k+4)/(128*k**12*(k*k+4)**4))
gc=S.gcd(qq_numerator(nc),qq_numerator(nh)).monic()
assert gc==S.Poly((k*k+1)**4,k,domain=S.QQ),gc
ce=S.rem(S.Poly(c1.subs({b:-S.Rational(1,6),x:-S.Rational(1,2)},
                       simultaneous=True),k,domain=S.QQ),
         S.Poly(k*k+1,k,domain=S.QQ)).as_expr()
eq(ce,-(3*k+11)/27)
assert S.gcd(S.Poly(ce,k,domain=S.QQ),
             S.Poly(k*k+1,k,domain=S.QQ)).degree()==0
print("PASS u^2+1 component: original-source norm gcd and both exceptional returns",
      flush=True)
print("ALL PASS: unit3+1 nonhalf alpha-nonzero q-zero sources",
      "seconds",round(monotonic()-started,3),flush=True)

#!/usr/bin/env python3
# Author: Astra-ISP-b2a9acde-20261120 / r150_structure; AI-assisted GPT-6 Astra Pro.
"""Exact QQ source check for the general unit 2+2 plus isolated-zero branch.
This is a bounded coefficient solve after the complete structural mean
classification; no original Bell generator is replaced by a finite-field claim.
"""
import sympy as s
from time import monotonic
started=monotonic()
rr,tt,dd,hh=s.symbols("r t delta h")
xx=s.symbols("X Y Z T")
one=s.Matrix([1,0,1,0])

def amul(a,b):
    return s.Matrix([a[0]*b[0],a[0]*b[1]+a[1]*b[0],
                     a[2]*b[2],a[2]*b[3]+a[3]*b[2]])
def clean(z):
    return s.cancel(s.expand(z))
def eq(a,b=0):
    assert clean(a-b)==0
def core(K,delta):
    a=(1+delta)/2;b=(1-delta)/2
    def tau(x):
        return a*x[0]+x[1]+b*x[2]+x[3]
    def DK(x):
        return s.Matrix([tau(amul(K.row(i).T,x)) for i in range(4)])
    d=DK(one);phi=tau(d)/2
    def pv(x):
        z=x-tau(x)*one
        return clean(tau(amul(z,amul(z,z)))/2)
    def pj(x,v):
        z=x-tau(x)*one;w=v-tau(v)*one
        return clean(3*tau(amul(amul(z,z),w))/2)
    def nv(x):
        return clean(tau(amul(d-phi*one,amul(x,x)))/2
                     -tau(x)*tau(amul(d,x))+phi*tau(x)**2
                     +tau(amul(x,DK(x)))/4)
    def nj(x,v):
        return clean(nv(x+v)-nv(x)-nv(v))
    rows=[K.row(i).T for i in range(4)]
    e=s.Matrix([tau(amul(rows[0],rows[0])),
                2*tau(amul(rows[0],rows[1])),
                tau(amul(rows[2],rows[2])),
                2*tau(amul(rows[2],rows[3]))])
    mean=[clean(z) for z in e-2*DK(d)-2*amul(d,d)+4*phi*d]
    vals=dict(p=pv(K[:,0]),p1=pj(K[:,0],K[:,1]),
              q=pv(K[:,2]),q1=pj(K[:,2],K[:,3]),
              n=nv(K[:,0]),n1=nj(K[:,0],K[:,1]),
              o=nv(K[:,2]),o1=nj(K[:,2],K[:,3]))
    vals["ca"]=clean(3*vals["p"]*vals["n1"]-2*vals["n"]*vals["p1"])
    vals["cb"]=clean(3*vals["q"]*vals["o1"]-2*vals["o"]*vals["q1"])
    vals["mu"]=clean(3*vals["n"]*vals["o"]
                    -(3*a*vals["p"]+vals["p1"])*vals["o"]
                    -(3*b*vals["q"]+vals["q1"])*vals["n"])
    return mean,vals,nv

# These three compatibility conditions are polynomial identities even when
# m, u, z, any value, or any derivative vanishes.
u,v,z,w,m,a=s.symbols("u v z w m a")
bb=1-a
eq(3*(-u**3)*(-2*m*u*v)-2*(-m*u**2)*(-3*u*u*v))
eq(3*(-m*u*u)*(-m*z*z)
   -(3*a*(-u**3)-3*u*u*v)*(-m*z*z)
   -(3*bb*(-z**3)-3*z*z*w)*(-m*u*u),
   3*m*u*u*z*z*(m-a*u-v-bb*z-w))
print("PASS division-free local and scalar-mean compatibility sources",flush=True)

# Complete regular mean parametrization:
# A=1, s=B+D !=0, r=B-D-delta !=0, t=s/r !=0,
# delta=t*(4*r*r-t*t-1)/2 !=0.
delta=tt*(4*rr*rr-tt*tt-1)/2
B=(rr*(tt+1)+delta)/2
D=(rr*(tt-1)-delta)/2
j=clean(delta*(rr*(tt-1)**2-delta*tt-1)/(4*tt))
k=clean(-delta*(rr*(tt+1)**2+delta*tt+1)/(4*tt))
E=clean(-delta*rr/2+delta*rr**2/(2*tt)-delta/(4*tt)
        -delta**2/8-delta**2/(8*tt**2))
K=s.Matrix([[0,0,1,B],[0,j-E,D,E],[1,D,0,0],[B,E,0,k-E]])
K=K.applyfunc(clean)
mean,V,nv=core(K,delta)
for x in mean:eq(x)
print("PASS original mean vanishes on the complete regular chart",flush=True)
Phi=tt*tt+1
Delta=4*rr*rr-Phi
pa=s.Poly(V["ca"],rr,tt,domain=s.QQ)
pb=s.Poly(V["cb"],rr,tt,domain=s.QQ)
phi2=s.Poly(Phi**2,rr,tt,domain=s.QQ)
qa,ra=s.div(pa,phi2);qb,rb=s.div(pb,phi2)
assert ra.is_zero and rb.is_zero
mu=s.Poly(V["mu"],rr,tt,domain=s.QQ)
def prim(p):
    return p.clear_denoms()[1].primitive()[1]
gens=[prim(qa),prim(qb),prim(mu)]
print("PASS original compatibility has Phi^2 factors; bounded QQ solve starts",flush=True)

# A fixed degree-24 coefficient solve replaces the timed-out Groebner step.
# The three ideal generators are unchanged under this invertible triangular
# transformation, and all later equalities are checked over the integers.
from flint import fmpz_mat
f1=qa-qb
f2=qa+qb+s.Poly(tt,rr,tt,domain=s.QQ)*f1
bounded_gens=[prim(f1),prim(f2),prim(mu)]
assert [int(p.total_degree()) for p in bounded_gens]==[9,10,14]
Dmax=24
monomials=[(i,d-i) for d in range(Dmax,-1,-1) for i in range(d,-1,-1)]
row_index={e:i for i,e in enumerate(monomials)}
columns=[]
for pol in bounded_gens:
    coeff={e:int(c) for e,c in pol.as_dict().items()}
    for d in range(Dmax-int(pol.total_degree())+1):
        for i in range(d,-1,-1):
            shift=(i,d-i)
            col=[0]*len(monomials)
            for e,c in coeff.items():
                col[row_index[(e[0]+shift[0],e[1]+shift[1])]]=c
            columns.append(col)
target=Delta*Phi**2
tv=[0]*len(monomials)
for e,c in s.Poly(target,rr,tt,domain=s.QQ).as_dict().items():
    tv[row_index[e]]=int(c)
assert (len(monomials),len(columns))==(325,322)

# This modular step ONLY picks a nonsingular square coefficient block.
# No membership assertion is lifted from it.  The recovered rational
# multipliers are checked against all 325 original coefficient rows below.
prime=10007
basis={}
picked=[]
pivot_rows=[]
for j,col in enumerate(columns):
    v=[x%prime for x in col]
    for i in range(len(v)):
        fac=v[i]
        if not fac:
            continue
        if i in basis:
            brow=basis[i]
            v[i:]=[(x-fac*y)%prime for x,y in zip(v[i:],brow[i:])]
        else:
            inv=pow(fac,-1,prime)
            v[i:]=[(x*inv)%prime for x in v[i:]]
            basis[i]=v
            picked.append(j)
            pivot_rows.append(i)
            break
assert len(picked)==294
square=fmpz_mat([[columns[j][i] for j in picked] for i in pivot_rows])
rhs=fmpz_mat([[tv[i]] for i in pivot_rows])
solution=square.solve(rhs)
numerator,denominator=solution.numer_denom()
wide=fmpz_mat([[columns[j][i] for j in picked] for i in range(len(monomials))])
expected=fmpz_mat([[int(denominator)*z] for z in tv])
assert wide*numerator==expected
assert int(denominator)!=0
print("PASS exact QQ multipliers: degree24, rows325, source columns322, block294",
      "seconds",round(monotonic()-started,3),flush=True)

# Therefore Phi !=0 is impossible on Delta !=0.  All Phi=0 exceptions are
# now handled explicitly, without dividing by n, o, m, or a support value.
def modphi(f):
    return s.rem(s.Poly(clean(f),tt,domain=s.QQ.frac_field(rr)),
                 s.Poly(Phi,tt,domain=s.QQ.frac_field(rr))).as_expr()
eq(modphi(V["o"]+V["n"]))
eq(modphi(V["mu"]-3*V["n"]**2))
Q=2*rr*rr-2*tt*rr-1
eq(modphi(V["n"]-tt*rr**2*Q/4))
for sig in (1,-1):
    subs={rr:(tt+sig)/2}
    def red(f):
        ff=clean(f.subs(subs))
        return s.rem(s.Poly(ff,tt,domain=s.QQ),
                     s.Poly(Phi,tt,domain=s.QQ)).as_expr()
    KC=K.applyfunc(red)
    VC={k:red(v) for k,v in V.items()}
    eq(red(delta),-sig)
    if sig==1:
        eq(VC["p"],(tt+1)/4);eq(VC["q"])
        eq(VC["p1"]);eq(VC["q1"])
        expected=s.Matrix([[0,0,1,(tt-1)/2],[0,0,0,0],
                           [1,0,0,0],[(tt-1)/2,0,0,0]])
    else:
        eq(VC["p"]);eq(VC["q"],(1-tt)/4)
        eq(VC["p1"]);eq(VC["q1"])
        expected=s.Matrix([[0,0,1,0],[0,0,-(1+tt)/2,0],
                           [1,-(1+tt)/2,0,0],[0,0,0,0]])
    assert KC==expected
    for k0 in ("n","n1","o","o1"):eq(VC[k0])
print("PASS all Phi=0 candidates have the explicit rank-two Gram obstruction",
      "seconds",round(monotonic()-started,3),flush=True)
print("ALL PASS: regular chart exact sources and every exceptional candidate")

"""Exact positive-coefficient calculations for q=3, delta=1 endpoints.

Modes: first (all L>=4, n=1); central4 (L=4, n=2).
Every denominator cleared is a product of explicitly positive Gram minors.
"""
import itertools
import sys
from math import comb, factorial, prod
from time import monotonic
import sympy as sp
from flint import fmpz_mpoly_ctx

mode = sys.argv[1] if len(sys.argv) > 1 else 'first'
assert mode in ('first', 'central4')
ctx = fmpz_mpoly_ctx.get(('y','z'), ordering='lex')
y,z = ctx.gens()
one = ctx.from_dict({(0,0):1}); zero = 0*one

def rising(a,n):
    v=one
    for j in range(n): v*=a+j
    return v

def Z(weights,k):
    v=zero
    for inds in itertools.combinations(range(4),k):
        t=one*prod((i-j)**2 for i,j in itertools.combinations(inds,2))
        for i in inds: t*=weights[i]
        v+=t
    return v

def moment(weights,k,root=None):
    return sum((weights[r]*r**k*(1 if root is None else (r-root)**2) for r in range(4)),zero)

def theta(v): return z*v.derivative('z')

a,b,c,d,p,q,r,t,X,Y,w=sp.symbols('a b c d p q r t X Y w')
lam=(a*c-b*b)+w*(a*d-b*c)+w*w*(b*d-c*c)
if mode=='first':
    weights=[]
    for i in range(4):
        row=[]
        for rr in range(4):
            k=i+rr-2
            row.append(comb(3,rr)*z**rr*factorial(k)*rising(y+1,4-k) if 0<=k<=4 else zero)
        weights.append(row)
    s2=moment(weights[1],2); s3=moment(weights[1],3); s4=moment(weights[1],4)
    z1m,z2m,z3m=[Z(weights[2],k) for k in (1,2,3)]
    z1u,z2u,z3u=[Z(weights[3],k) for k in (1,2,3)]
    tm,tu=theta(z2m),theta(z2u)
    ds=[s2,z2m,z1m,z2u,z1u]
    def E(*inds): return tuple(int(i in inds) for i in range(5))
    xn=s2*z2m-2*s3*z2m+tm*s2
    yn=-s3*z2m*z2u+2*tm*s2*z2u-tu*s2*z2m
    variables=(a,b,c,d,q,r,t,X,Y)
    nums=[sum((weights[0][rr]*rr**2*(rr-1)**2 for rr in range(4)),zero),s2*s4-s3*s3,z3m,z3u,s2,z2m,z2u,xn,yn]
    dens=[E(),E(0),E(1),E(3),E(),E(2),E(4),E(0,1),E(0,1,3)]
    F=q*(q*t-r*r)+w*q*r*t+w*w*r*r*t
    P=q*lam*F-w*q**3*r*(c+w*d)*(r+w*t)*X**2-w*q*q*r*r*t*(a+w*b)*Y**2-2*w*q*q*r*t*(b+w*c)*(q+w*r)*X*Y-w*w*q**3*r*r*t*X**2*Y**2
else:
    weights=[]
    for i in range(4):
        row=[]
        for rr in range(4):
            k=rr-1+i
            row.append(comb(3,rr)*z**rr*factorial(k)*factorial(4-k) if 0<=k<=4 else zero)
        weights.append(row)
    sl=[moment(weights[0],k,0) for k in range(3)]
    su=[moment(weights[3],k,3) for k in range(3)]
    z1l,z2l,z3l=[Z(weights[1],k) for k in (1,2,3)]
    z1u,z2u,z3u=[Z(weights[2],k) for k in (1,2,3)]
    tl,tu=theta(z2l),theta(z2u)
    ds=[sl[0],z2l,z1l,z2u,z1u,su[0]]
    def E(*inds): return tuple(int(i in inds) for i in range(6))
    xn=sl[1]*z2l*z2u-2*tl*sl[0]*z2u+tu*sl[0]*z2l
    yn=-tl*z2u*su[0]+2*tu*z2l*su[0]-(3*su[0]+su[1])*z2l*z2u
    variables=(a,b,c,d,p,q,r,t,X,Y)
    nums=[sl[0]*sl[2]-sl[1]**2,z3l,z3u,su[0]*su[2]-su[1]**2,sl[0],z2l,z2u,su[0],xn,yn]
    dens=[E(0),E(1),E(3),E(5),E(),E(2),E(4),E(),E(0,1,3),E(1,3,5)]
    F=p*q*(q*t-r*r)+w*q*r*(p*t-q*r)+w*w*r*t*(p*r-q*q)
    P=q*lam*F-w*p*q**3*r*(c+w*d)*(r+w*t)*X**2-w*q*q*r*r*t*(a+w*b)*(p+w*q)*Y**2-2*w*p*q*q*r*t*(b+w*c)*(q+w*r)*X*Y-w*w*p*q**3*r*r*t*X**2*Y**2

expected={'first':[(875,57),(2279,89),(2904,101),(1610,76),(1050,62)],'central4':[(36,47),(55,69),(63,79),(55,69),(36,45)]}
start=monotonic(); polys=nums+ds
for j in range(5):
    cp=sp.Poly(sp.expand(P).coeff(w,j),*variables)
    terms=cp.terms()
    de=[tuple(sum(ex[k]*dens[k][i] for k in range(len(variables))) for i in range(len(ds))) for ex,co in terms]
    common=tuple(max(v[i] for v in de) for i in range(len(ds)))
    out=zero; powers={}
    def power(k,e):
        if (k,e) not in powers: powers[k,e]=polys[k]**e
        return powers[k,e]
    for (ex,co),dd in zip(terms,de):
        factors=[power(k,e) for k,e in enumerate(ex) if e]+[power(len(nums)+k,common[k]-dd[k]) for k in range(len(ds)) if common[k]!=dd[k]]
        factors.sort(key=lambda v:len(v.to_dict()))
        v=int(co)*one
        for f in factors:v*=f
        out+=v
    tt=list(out.terms()); neg=[(m,str(co)) for m,co in tt if co<0]
    anchors=[(m,str(co)) for m,co in tt if m[0]==0 and co>0]
    print(mode,'P'+str(j),'den',common,'terms',len(tt),'neg',len(neg),'degree',out.total_degree(),'anchor',anchors[:1],'seconds',monotonic()-start,flush=True)
    if neg:print('NEGATIVE',neg[:5],flush=True)
    assert not neg
    assert anchors
    assert (len(tt),out.total_degree())==expected[mode][j]
print('ALL_PASS',mode,flush=True)

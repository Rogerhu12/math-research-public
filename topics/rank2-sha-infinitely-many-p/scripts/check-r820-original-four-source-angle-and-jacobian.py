#!/usr/bin/env python3
"""R820: genuine fourth source angle, original four jets, and fixed costs.
Public run only; no arguments; python-flint==0.9.0.  No output files.
The polynomial V is the proved original source in R816, not an output cache.
"""
from fractions import Fraction as Q
from math import gcd as igcd
from flint import fmpq_poly
import json

def tr(a):
    a=list(map(Q,a))
    while len(a)>1 and not a[-1]:a.pop()
    return a
def add(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return tr(c)
def scale(a,s):return tr([Q(s)*x for x in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tr(c)
def power(a,n):
    z=[Q(1)]
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z
def prod(*args):
    z=[Q(1)]
    for a in args:z=mul(z,a)
    return z
def dm(a,b):
    a=tr(a);b=tr(b);q=[Q(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        i=len(a)-len(b);u=a[-1]/b[-1];q[i]+=u
        for j,x in enumerate(b):a[i+j]-=u*x
        a=tr(a)
    return tr(q),a
def pgcd(a,b):
    while b!=[0]:a,b=b,dm(a,b)[1]
    return scale(a,1/a[-1])
def val(a,b):
    r=0
    while a!=[0]:
        q,s=dm(a,b)
        if s!=[0]:break
        a=q;r+=1
    return r
def enc(a):return [str(x) for x in a]
def factor(a):
    c,fs=fmpq_poly([str(x) for x in a]).factor()
    out=[{"polynomial": [str(f[i]) for i in range(f.degree()+1)],
          "multiplicity":n} for f,n in fs]
    return {"constant":str(c),"factors":out}
def det(A):
    A=[r[:] for r in A];z=Q(1);n=len(A)
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        if k is None:return Q(0)
        if k!=j:A[j],A[k]=A[k],A[j];z=-z
        p=A[j][j];z*=p
        for k in range(j+1,n):
            u=A[k][j]/p
            for h in range(j,n):A[k][h]-=u*A[j][h]
    return z

t=[0,1];tm1=[-1,1];d=[1,8];h7=[7,4,16]
a=prod(t,tm1,h7)
fS=scale(mul(a,d),Q(1,7))
fT=prod(fS,[1,-4],[1,-20,-8],[1,96,48,-64])
H=prod([-1,20,8],[13,-52,1536,-1024,256],
       [1,-40,2112,-3136,1792],
       [-1,1232,58688,-49408,439040,-2111488,1949696,-851968,32768])
fU=scale(mul(a,H),Q(1,91))
# R816 actual sigma^66 X^j coefficients, j=0,...,10.
cV=list(map(Q,["0","262144/7","393216/7","159744","119808",
              "212736/7","53376","-7248/7","-18156/7","1515/7","1"]))
fV=[Q(0)]*12
for j,c in enumerate(cV):fV[11-j]=c*((-1)**(11-j))
fV=tr(fV)
qV,rV=dm(fV,a)
fixed={"t":t,"t_minus_one":tm1,"h7":h7,"d":d}
divisors={k:val(fV,f) for k,f in fixed.items()}

# All formal jets come from the original differential equation x''=6x^2.
L=6
def cut(a):return list(map(Q,a[:L+1]))+[Q(0)]*max(0,L+1-len(a))
def sm(a,b):return cut(mul(a,b))
def sp(a,n):
    z=cut([1]);a=cut(a)
    while n:
        if n&1:z=sm(z,a)
        a=sm(a,a);n//=2
    return z
def si(a):
    a=cut(a);z=cut([Q(1)/a[0]])
    for n in range(1,L+1):z[n]=-sum(a[k]*z[n-k] for k in range(1,n+1))/a[0]
    return z
def se(a):
    a=cut(a);assert not a[0]
    z=cut([1])
    for n in range(1,L+1):z[n]=sum(k*a[k]*z[n-k] for k in range(1,n+1))/n
    return z
def sc(P,T):
    z=cut([0])
    for x in reversed(P):z=sm(z,T);z[0]+=x
    return z
W=cut([1]);W[1]=Q(-1,7)
for n in range(2,L+1):
    W[n]=sum(W[i]*W[n-i] for i in range(1,n))/((n-1)*(6*n+1))
F=cut([0])
for n in range(1,L+1):F[n]=-W[n]/(6*n*(6*n-1))
Theta=sm(W,se(scale(F,2)))
tw=scale(sm(cut([0,1]),sp(si(W),3)),-1)
names=["S34","T72","U136","V66"]
angles=[fS,fT,fU,fV]
charges=[17,36,68,33]
sources=[sm(sp(Theta,m),sc(f,tw)) for m,f in zip(charges,angles)]
assert all(isinstance(x,Q) for seq in [W,F,Theta,tw]+sources for x in seq)
assert all(v[0]==0 and v[1]==1 for v in sources)
assert sources[0][2]==Q(-988,105)
assert sources[1][2]==Q(-2938,35)
assert sources[2][2]==Q(135218,105)
minors={}
for high in (4,5,6):
    rows=[[v[high],v[3],v[2],v[1]] for v in sources]
    minors[str(high)+",3,2,1"]=str(det(rows))
numgcd=0
for x in minors.values():numgcd=igcd(numgcd,abs(Q(x).numerator))
report={
 "status":"PASS","field":"Q","source":"R816 original V66; all other sources R468",
 "angle_V_ascending":enc(fV),
 "angle_V_factorization":factor(fV),
 "V_divisors":divisors,
 "V_division_by_a":{"quotient":enc(qV),"remainder":enc(rV)},
 "V_gcd_with_a_d":enc(pgcd(fV,mul(a,d))),
 "V_normalization_weight33_condition":rV==[0] and len(fV)-1<=10,
 "low_w_jets_1_through_6":{n:enc(v[1:]) for n,v in zip(names,sources)},
 "four_row_minors":minors,
 "gcd_displayed_minor_numerators":numgcd,
 "relative_Gaussian_charges":["1","36/17","4","33/17"],
 "scope":"Fixed actual sources and full polynomial identities. No claim that four central zeros propagate to arbitrary products, or that four curves have transcendence degree four.",
 "output_files":False}
print(json.dumps(report,separators=(",",":")))

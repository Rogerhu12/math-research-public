#!/usr/bin/env python3
"""Exact degree-80 norm at p=41; no external algebra package.

Computes a multiplication determinant in Z[X]/Phi_41 by Bareiss,
checks both extra prime factors by complete trial division, and exhibits
an individual Fourier zero that is not a paired zero.
"""
from math import isqrt
import json

p=41
def fm(a,b):return ((a[0]*b[0]-3*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def fp(a,n):
    out=(1,0)
    while n:
        if n&1:out=fm(out,a)
        a=fm(a,a);n//=2
    return out
z=fp((1,1),(p*p-1)//3)
assert z!=(1,0) and fp(z,3)==(1,0)
lab={fp(z,i):i for i in range(3)}
cols=[lab[fp((1,b),(p*p-1)//3)] for b in range(p)]
roots=[(1,0),(0,1),(-1,-1)]
A=[roots[c][0] for c in cols]
B=[roots[c][1] for c in cols]
def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def red(a):
    a=a[:]
    while len(a)>p-1:
        d=len(a)-p;c=a[-1]
        for j in range(p):a[d+j]-=c
        a.pop()
    return a+[0]*(p-1-len(a))
aa,ab,bb=conv(A,A),conv(A,B),conv(B,B)
R=red([x-y+z for x,y,z in zip(aa,ab,bb)])
columns=[red([0]*j+R) for j in range(p-1)]
M=[[columns[j][i] for j in range(p-1)] for i in range(p-1)]
def determinant(mat):
    a=[row[:] for row in mat]
    n=len(a);prev=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next(i for i in range(k+1,n) if a[i][k])
            a[k],a[r]=a[r],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=a[i][j]*pivot-a[i][k]*a[k][j]
                assert v%prev==0
                a[i][j]=v//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]
norm=determinant(M)
factors=[12547,284186721943]
assert norm==3**40*(factors[0]*factors[1])**2
assert all(all(n%d for d in range(2,isqrt(n)+1)) for n in factors)
assert all(n%(3*p)==1 for n in factors)
assert isqrt(norm)**2==norm

ell=factors[0]
xi=next(pow(g,(ell-1)//p,ell) for g in range(2,ell)
        if pow(g,(ell-1)//p,ell)!=1)
zeta=next(pow(g,(ell-1)//3,ell) for g in range(2,ell)
          if pow(g,(ell-1)//3,ell)!=1)
assert pow(xi,p,ell)==pow(zeta,3,ell)==1
def fourier(a,sign):
    return sum(pow(zeta,sign*c%3,ell)*pow(xi,a*b%p,ell)
               for b,c in enumerate(cols))%ell
zeros=[dict(a=a,S=0,opposite_S=fourier(a,-1))
       for a in range(1,p) if fourier(a,1)==0]
assert zeros and all(t['opposite_S'] for t in zeros)
print(json.dumps(dict(p=p,A_coefficients=A,B_coefficients=B,
    full_cyclotomic_degree=80,real_subfield_degree=40,
    norm_full=str(norm),absolute_norm_real=str(isqrt(norm)),
    full_norm_factorization={'3':40,'12547':2,'284186721943':2},
    prime_factor_proofs='Complete trial division through each integer square root',
    individual_zero_example=dict(ell=ell,xi=xi,zeta=zeta,zeros=zeros),
    scope='A counterexample to individual-unit reasoning, not to paired nonvanishing.'),indent=2))

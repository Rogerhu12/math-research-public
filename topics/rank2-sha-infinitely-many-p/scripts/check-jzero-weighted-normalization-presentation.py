#!/usr/bin/env python3
"""R329 exact original normalization presentation; requires python-flint."""
from pathlib import Path
from flint import fmpz_poly, fmpq_poly, fmpq_mat, fmpz_mat, fmpq
from math import gcd, lcm
from functools import reduce
import json
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'check-jzero-weighted-normalization-presentation.json').read_text())
t=fmpz_poly([0,1])
q7=16*t**2+4*t+7
g2=8*t**2+20*t-1
f3=64*t**3-48*t**2+228*t-1
f4d=1792*t**4-3136*t**3+2112*t**2-40*t+1
f4=512*t**4-2048*t**3+1344*t**2-536*t-1
f6=4096*t**6-33792*t**5+204288*t**4-47936*t**3+11040*t**2+84*t+1
nf=27*(4*t-1)**2*f3*f4d
df=t**2*(t-1)**2*(8*t+1)*q7**2
nh=-64*g2**2*f4*f6
dh=t**3*(t-1)*(8*t+1)**2*q7**3

def powers(n):
    return [(n-3*j-4*k,j,k) for k in range(n//4+1) for j in range((n-4*k)//3+1)]

def den(n):
    a=3*n//4; b=2*n//3; c=n//2
    return t**a*(t-1)**b*(8*t+1)**c*q7**a

def col(n,j,k):
    a=3*n//4; b=2*n//3; c=n//2
    return nf**j*nh**k*t**(a-2*j-3*k)*(t-1)**(b-2*j-k)*(8*t+1)**(c-j-2*k)*q7**(a-2*j-3*k)

def matrix(n):
    mons=powers(n)
    cols=[col(n,j,k) for i,j,k in mons]
    rows=den(n).degree()+n//2+1
    return mons,cols,fmpz_mat([[poly[r] for poly in cols] for r in range(rows)])


assert nf.resultant(df)==2**90*3**118
assert nh.resultant(dh)==2**288*3**189*7

generators=[(d,fmpz_poly([int(v) for v in pp])) for d,pp in DATA['generators']]
expected=[(0,fmpz_poly([1]))]
for n,ratios in [(2,[(1,t),(1,q7),(t,q7),(1,8*t+1),(1,t-1),(t,1)]),
                 (3,[(1,t**2),(1,q7**2),(t,q7**2)]),
                 (4,[(1,t**3),(1,q7**3),(t,q7**3),(1,(8*t+1)**2)])]:
    for nu,de in ratios:
        poly,rem=divmod(den(n)*nu,fmpz_poly(de) if isinstance(de,int) else de)
        assert not rem
        expected.append((n,poly))
assert generators==expected
assert [rel['degree'] for rel in DATA['relations']]==[5]*5+[6]*4+[7]*5
common_den=1
for column,rel in enumerate(DATA['relations']):
    n=rel['degree']
    image=fmpq_poly()
    for (g,i,j,k),value in zip(rel['monomials'],rel['coefficients']):
        d,poly=generators[g]
        assert d+i+3*j+4*k==n
        quotient,rem=divmod(den(n),den(d)*df**j*dh**k)
        assert not rem
        value=fmpq(value)
        image+=value*fmpq_poly(poly*nf**j*nh**k*quotient)
        common_den=lcm(common_den,int(value.denominator))
    assert not image
    print(f'PASS relation {column+1}: weight {n}')
remainder=common_den
for p in (2,3,5,7,13):
    while remainder%p==0:remainder//=p
assert remainder==1
point=(1,2,3)
a,b,c=point
M=fmpq_mat(14,14)
for column,rel in enumerate(DATA['relations']):
    for (g,i,j,k),value in zip(rel['monomials'],rel['coefficients']):
        M[g,column]+=fmpq(value)*a**i*b**j*c**k
F=json.loads((ROOT/'check-jzero-weighted-conductor-integral.json').read_text())
fvalue=sum(int(value)*a**i*b**j*c**k for (i,j,k),value in zip(F['relation_monomials'],F['relation_coefficients']))
scalar=fmpq(7**8,2**72*3**65*5*13)
assert scalar==fmpq(DATA['determinant_scalar'])
assert M.det()==scalar*fvalue and fvalue!=0
assert sum(rel['degree'] for rel in DATA['relations'])-sum(d for d,poly in generators)==47
# Hilbert numerator from the explicit section-ring formula.
v=t
numer=(1-v**3)*(1-v**4)+3*(v**2+v**3+v**4)*(1-v**3)+2*v**2*(1-v**3)*(1+v**2)+(v**2+v**3)*(1-v**4)
assert numer==1+6*v**2+3*v**3+4*v**4-5*v**5-4*v**6-5*v**7
print('PASS: 14 exact original generators and relations; determinant scalar and Hilbert numerator.')

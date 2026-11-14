#!/usr/bin/env python3
"""Exact fixed numerator and the twelve residue cases of the full conductor.

Uses the already published R326 numerator, without rerunning its large return
certificate.  The all-degree assertions follow by period twelve in the proof.
"""
from pathlib import Path
from fractions import Fraction
from functools import reduce
from math import gcd
import json
from flint import fmpz_poly

ROOT = Path(__file__).resolve().parent
old = json.loads((ROOT / 'check-jzero-weighted-conductor-integral.json').read_text())
scale = Fraction(old['scale'])
N = fmpz_poly([int(Fraction(v)*scale) for v in old['conductor_numerator']])
t = fmpz_poly([0, 1])
q7 = 16*t*t+4*t+7
divisor = t**3*(t-1)*(8*t+1)**3*q7**3
P, rem = divmod(N, divisor)
assert not rem
assert P.degree() == 134
assert reduce(gcd, (int(v) for v in P)) == 1
assert P[0] == -3**4*3159421
assert P*divisor == N

def ceildiv(a, b):
    return (a+b-1)//b

def normal(n):
    u,v,c = 3*n//4,n//2,2*n//3
    return u,v,c,3*u+2*v+c

def canonical(m):
    a,b,c = ceildiv(3*m,4),ceildiv(m,2),ceildiv(2*m,3)
    return a,b,c,3*a+2*b+c-2

cases = []
for n in range(12):
    m = n+1
    a,b,c,e = canonical(m)
    u,v,cc,d = normal(m+39)
    et, ef, el = u-26-a,cc-24-c,v-16-b
    assert et == (3 if m%4 in (0,1) else 2)
    assert ef == (2 if m%3 == 0 else 1)
    assert el == 3
    numerator = P*t**et*(t-1)**ef*(8*t+1)**3*q7**et
    assert d-numerator.degree()-e == 5
    un,vn,cn,dn = normal(n)
    er,fr,lr = a-1-un,c-1-cn,b-1-vn
    assert er == int(n%4 in (1,2))
    assert fr == int(n%3 == 1)
    assert lr == 0
    degR = 3*er+fr
    assert e == dn+degR+4
    assert 13 + m - a == 13+m//4
    a12,b12,c12,e12 = canonical(m+12)
    assert (a12-a,b12-b,c12-c,e12-e) == (9,6,8,47)
    u12,v12,c12,d12 = normal(n+12)
    assert (u12-un,v12-vn,c12-cn,d12-dn) == (9,6,8,47)
    cases.append({'n_mod_12':n,'m_mod_12':m%12,
                  'normal_numerator_exponents':[et,ef,el,et],
                  'relative_factor_exponents':[er,fr],
                  'relative_quotient_rank':degR+4,
                  'canonical_dimension':e+1,
                  'relative_minimum_w_order':m//4})

ans = {'status':'PASS', 'fixed_numerator_degree':134,
       'fixed_numerator_coefficients':[str(v) for v in P],
       'fixed_numerator_constant':str(P[0]),
       'factorization':'N=t^3*(t-1)*(8*t+1)^3*q7^3*P134',
       'canonical_kappa':'P134/(t^26*(t-1)^24*(8*t+1)^16*q7^26)',
       'normal_numerator_degree_slack':5,
       'residue_cases':cases,
       'scope':'Exact fixed division and all twelve residue cases; no target-prime scan.'}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(ans,ensure_ascii=False,indent=2)+'\n')
print('PASS: fixed primitive numerator and 12 residue cases; '+out.name)

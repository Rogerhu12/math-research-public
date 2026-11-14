#!/usr/bin/env python3
"""Exact R124 checks: group characters, eta forms, L' bounds, and 5-adic logs.

Only the Python standard library is used.  Rank 2 uses the published
Gross--Zagier--Kolyvagin theorem after these exact analytic checks; this script
does not compute all rational points or quadratic-Chabauty heights.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb, gcd, isqrt
from pathlib import Path

from verify_r120_nine_cartan_twist import K, ecadd, ecmul, matmul, cosets


def character_identity():
    G = sorted(a for a in product(range(9), repeat=4)
               if gcd(a[0]*a[3]-a[1]*a[2], 9) == 1)
    subgroups = {
        'C': {(a, -b % 9, b, a) for a, b in product(range(9), repeat=2)
              if gcd(a*a+b*b, 9) == 1},
        'B0': {a for a in G if a[2] % 3 == 0},
        'B1': {a for a in G if a[1] % 3 == 0 and a[2] == 0},
        'T1': {a for a in G if a[1] % 3 == 0 and a[2] % 3 == 0},
        'T2': {a for a in G if a[1] == a[2] == 0},
    }
    chars, orders, indices = [], [], []
    for H in subgroups.values():
        reps, idx = cosets(G, H)
        assert len(idx) == 3888
        chars.append([sum(idx[matmul(g, r)] == k
                          for k, r in enumerate(reps)) for g in G])
        orders.append(len(H))
        indices.append(len(reps))
    rows = list(zip(*chars))
    assert all(c+2*b0+2*b1 == t2+2*t1+2 for c,b0,b1,t1,t2 in rows)
    histogram = sorted(Counter(rows).items())
    return dict(group_order=len(G), names=list(subgroups),
                subgroup_orders=orders, indices=indices,
                character_value_histogram=[[list(v), n] for v,n in histogram],
                all_3888_equalities=True)


DIVISORS = [1, 3, 9, 27, 81]


def eta_coefficients(exponents, bound=36):
    shift = sum(d*r for d,r in zip(DIVISORS, exponents))//24
    a = [1]+[0]*bound
    for d, r in zip(DIVISORS, exponents):
        if not r:
            continue
        for n in range(d, bound+1, d):
            if r > 0:
                b = [(-1)**j*comb(r,j) for j in range(min(r,bound//n)+1)]
            else:
                b = [comb(-r+j-1,j) for j in range(bound//n+1)]
            out = [0]*(bound+1)
            for j, z in enumerate(b):
                for k in range(bound+1-j*n):
                    out[k+j*n] += z*a[k]
            a = out
    return [0]*shift+a[:bound+1-shift]


def eta_data():
    exponents = [[0,-1,6,-1,0], [0,1,2,1,0],
                 [0,2,2,0,0], [0,0,2,2,0]]
    orders, coefficients = [], []
    for r in exponents:
        assert sum(r) == 4
        assert sum(d*e for d,e in zip(DIVISORS,r)) % 24 == 0
        assert sum((81//d)*e for d,e in zip(DIVISORS,r)) % 24 == 0
        assert sum(k*e for k,e in enumerate(r)) % 2 == 0
        order = [F(81,24*gcd(c,81//c)*c)*
                 sum((F(gcd(c,d)**2*e,d) for d,e in zip(DIVISORS,r)),F(0))
                 for c in DIVISORS]
        assert all(v > 0 and v.denominator == 1 for v in order)
        orders.append([int(v) for v in order])
        coefficients.append(eta_coefficients(r))
    e1,e2,h,h3 = coefficients
    T2 = lambda a: [a[2*n]+(2*a[n//2] if n % 2 == 0 else 0)
                    for n in range(19)]
    assert T2(e1) == [3*v for v in e2[:19]]
    assert T2(e2) == e1[:19]
    assert T2(h) == T2(h3) == [0]*19
    # Fricke: reversed exponents agree and product d^r = 81^2.
    for r in exponents[:2]:
        assert r == list(reversed(r))
        assert sum(k*e for k,e in enumerate(r)) == 8
    assert e1[1] == e2[2] == 1 and e2[5] == -1
    return dict(level=81, weight=2, sturm_bound=18,
                exponent_order=DIVISORS, exponents=exponents,
                cusp_orders=orders, coefficients_to_36=coefficients,
                new_T2_matrix=[[0,1],[3,0]],
                new_Fr_canonical_matrix=[[-1,0],[0,-1]],
                new_dimension=2, hecke_field_polynomial='x^2-3')


def exp_negative_upper(t, terms=48):
    """e^{-t} < 1 / sum_{k=0}^{terms} t^k/k!, for t>0."""
    s = a = F(1)
    for k in range(1, terms+1):
        a = a*t/k
        s += a
    return 1/s


def ceil_scaled(x, scale):
    return (x.numerator*scale+x.denominator-1)//x.denominator


def derivative_bound():
    # c=pi/18 lies between 17/100 and 9/50.
    v = F(41,59)   # (50/9-1)/(50/9+1)
    main_lower = 4*sum((v**(2*k+1)/F(2*k+1) for k in range(20)),F(0))-F(41,25)
    assert main_lower > F(178,100)
    terms, finite_upper = [], F(0)
    for n in range(5,41):
        if gcd(n,6) != 1:
            continue
        tau = sum(n % d == 0 for d in range(1,n+1))
        sqrt_lower = F(isqrt(n*10**6),1000)
        assert sqrt_lower**2 <= n
        bound = F(200,17)*tau*exp_negative_upper(F(17*n,100))/(n*sqrt_lower)
        numerator = ceil_scaled(bound,10**6)
        terms.append([n,tau,int(sqrt_lower*1000),numerator])
        finite_upper += F(numerator,10**6)
    r = F(100,117)
    remainder = F(400,17*41)*r**41/(1-r)
    remainder_upper = F(ceil_scaled(remainder,10**6),10**6)
    assert finite_upper+remainder_upper < F(3,2)
    return dict(c_interval=['17/100','9/50'],
                main_term_lower='178/100',
                finite_term_columns=['n','divisor_count','floor_1000_sqrt_n',
                                     'term_upper_times_10^6'],
                finite_terms=terms,
                finite_sum_upper=str(finite_upper),
                remainder_upper=str(remainder_upper),
                absolute_tail_upper='3/2',
                derivative_strict_lower='7/25',
                scope='both real embeddings, exact rational inequalities')


def valuation_fraction(x, p=5):
    if x == 0:
        return 10**9
    def val(n):
        n, v = abs(n), 0
        while n % p == 0:
            n, v = n//p, v+1
        return v
    return val(x.numerator)-val(x.denominator)


def v5(a):
    a = K.coerce(a)
    return min(valuation_fraction(a.a),valuation_fraction(a.b))


def residue(a, m):
    a = F(a)
    assert gcd(a.denominator,m) == 1
    return a.numerator*pow(a.denominator,-1,m) % m


def logarithm_data():
    w = K(0,1)
    A, B = -(21+27*w)/2, 28*w-10
    PH, P2 = ((7-w)/2,4*w-4), ((1+w)/2,2*w+4)
    assert v5(-16*(4*A**3+27*B**2)) == 0
    f25 = [K(a,b) for a,b in product(range(5),repeat=2)]
    def red(a):
        return residue(a.a,5),residue(a.b,5)
    square_counts = Counter(red(y*y) for y in f25)
    count = 1+sum(square_counts[red(x**3+A*x+B)] for x in f25)
    assert count == 33
    cols, valuations = [], []
    for P in [PH,P2]:
        Q = ecmul(P,33,A,None)
        assert Q[1]**2 == Q[0]**3+A*Q[0]+B
        vals = [v5(Q[0]),v5(Q[1])]
        assert vals == [-2,-3]
        t = -Q[0]/Q[1]
        assert v5(t) == 1
        cols.append([residue(t.a/5,125),residue(t.b/5,125)])
        valuations.append(vals)
    assert cols == [[35,21],[6,118]]
    # log(t)=t+2*A*t^5/5+O(t^7), so log(t)/5=t/5 modulo 125.
    # D1 maps to 4PH; D2 maps to P2-2PH.  Divide [33] out modulo 125.
    inv33,inv3 = pow(33,-1,125),pow(3,-1,125)
    div_cols = [[4*a % 125 for a in cols[0]],
                [(b-2*a) % 125 for a,b in zip(*cols)]]
    log_cols = []
    for a,b in div_cols:
        log_cols.append([(4*inv3*b*inv33) % 125,
                         (2*inv3*(a+b)*inv33) % 125])
    matrix = [list(row) for row in zip(*log_cols)]
    assert matrix == [[64,46],[2,76]]
    determinant = (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]) % 5
    assert determinant == 2
    return dict(prime=5, residue_field='F5[w]/(w^2+3)',
                elliptic_residue_order=count,
                point_order=['PH','P2'],
                valuations_of_33P=valuations,
                t_33P_div_5_mod_125=cols,
                jacobian_differentials=['dx/y','x dx/y'],
                divisor_order=['D1=Pplus-Pminus','D2=Qplus-Pplus'],
                log_div_5_mod_125=matrix,
                determinant_mod_5=determinant,
                caution='finite-index lattice, not a proved full MW basis')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--check', action='store_true')
    p.add_argument('--write', action='store_true')
    args = p.parse_args()
    data = dict(character_identity=character_identity(), eta_forms=eta_data(),
                derivative_bound=derivative_bound(), logarithms=logarithm_data(),
                limitations=['does not classify rational points',
                             'does not compute p-adic heights or QC zeros'])
    out = (json.dumps(data,indent=2,sort_keys=True)+'\n').encode()
    path = Path(__file__).with_name('r124_nine_twist_rank_certificate.json')
    if args.write:
        path.write_bytes(out)
    if args.check:
        assert path.read_bytes() == out
    print('R124 exact checks PASS')
    print('certificate sha256',hashlib.sha256(out).hexdigest())


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Check R702 against the independent original six-isogeny Bell system.

This finite validation is not the proof of the all-prime congruence.
Only ordinary derivatives are used; Pascal coefficients remain valid
across p, and no division by p or by factorials is performed.
"""
import argparse
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import time


def run(p):
    assert p >= 41 and p % 6 == 5 and all(p % d for d in range(2, isqrt(p)+1))
    start = time.monotonic()
    r = pow(4, pow(3, -1, p-1), p)
    def q(a=0, b=0): return (a % p, b % p)
    def add(x, y): return q(x[0]+y[0], x[1]+y[1])
    def scale(x, a): return q(x[0]*a, x[1]*a)
    def mul(x, y): return q(x[0]*y[0]+3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
    def inv(x):
        d = (x[0]*x[0]-3*x[1]*x[1]) % p
        assert d
        return scale(q(x[0], -x[1]), pow(d, -1, p))
    a = q(-180*r*r-240*r-375)
    s = q(2*r*r+4*r+5)
    odd_x = q(-4*r*r-6*r-1, r*r+2*r-6)
    odd_y = q(12*r*r-24*r+12, -9*r*r+12*r+6)
    odd_e = scale(q(-r*r+2*r+2, r*r+2), pow(2, -1, p))
    even_x = q(5+2*r*r, 2*(r*r+2*r+3))
    roots = {}
    for odd in [False, True]:
        x = [odd_x if odd else even_x]
        y = [odd_y if odd else q()]
        e = [odd_e if odd else q()]
        f = [q(1)]
        binom = [1]
        for n in range(2*p-1):
            xx = q()
            ef = q()
            for j, b in enumerate(binom):
                xx = add(xx, scale(mul(x[j], x[n-j]), b))
                ef = add(ef, scale(mul(e[j], f[n-j]), b))
            yn = scale(xx, 3)
            en = x[n]
            if n == 0:
                yn = add(yn, a)
                en = add(en, s)
            x.append(scale(y[n], 2))
            y.append(scale(yn, -1 if odd else 1))
            e.append(scale(en, 1 if odd else -1))
            f.append(ef)
            binom = [1]+[(binom[j-1]+binom[j]) % p for j in range(1, len(binom))]+[1]
        base_inv = inv(f[1 if odd else 4])
        for m in range(1 if odd else 4, 2*p, 6):
            if odd:
                exponent = (m-1)//2
                factor = pow(-1, exponent, p)*pow(2, -exponent, p) % p
            else:
                factor = 6*pow(2, -(m-4)//2, p) % p
            value = scale(mul(f[m], base_inv), factor)
            assert value[1] == 0, ('rationality', p, m, value)
            roots[m+1] = value[0]
    N = (p-5)//6
    B = (-1)**(N+1)*comb(3*N+2, 2*N+1) % p
    ell2 = pow(2, (p-1)//2, p)
    rows = []
    for t in range(2, p, 3):
        lhs, rhs = roots[p+t+1], 3*ell2*B*t*roots[t] % p
        assert lhs == rhs, (p, t, lhs, rhs)
        rows.append({'t': t, 'A_t': roots[t], 'A_shift': lhs, 'predicted': rhs})
    assert roots[p+3] == 6*ell2*B % p and roots[p+6] == 90*ell2*B % p
    return {'prime': p, 'B': B, 'legendre_2': ell2,
            'A_p_plus_3': roots[p+3], 'A_p_plus_6': roots[p+6],
            'pC_p_plus_3': 9*B*B % p,
            'pC_p_plus_6': -405*pow(2, -1, p)*B*B % p,
            'every_allowed_t_checked': rows,
            'ordinary_derivatives_used': True, 'division_by_p_used': False,
            'runtime_seconds': time.monotonic()-start}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prime', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    value = run(args.prime)
    value.update({'result': 'R702-independent-Bell-check',
                  'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'validation_is_all_prime_proof': False})
    args.output.write_text(json.dumps(value, indent=2)+'\n')
    print(json.dumps({k:value[k] for k in ['prime', 'A_p_plus_3', 'A_p_plus_6',
          'pC_p_plus_3', 'pC_p_plus_6', 'runtime_seconds']}))

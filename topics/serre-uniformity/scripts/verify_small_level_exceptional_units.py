#!/usr/bin/env python3
"""R92: integral Bezout certificates for p=41,47,59,83.

Both generation and verification use only Python's standard library. Polynomial
coefficients are in increasing order. No resultant factorization is required.
"""
import argparse
from fractions import Fraction
from functools import reduce
import hashlib
import json
from math import gcd, lcm
from pathlib import Path

CASES = [(41, 3), (47, 44), (59, 56), (83, 80)]


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return trim(out)


def scale(a, s):
    return trim([s * x for x in a])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def division(a, b):
    a, b = trim(map(Fraction, a)), trim(map(Fraction, b))
    assert b != [0]
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        k, c = len(a) - len(b), a[-1] / b[-1]
        q[k] += c
        a = add(a, [0] * k + scale(b, -c))
    return trim(q), a


def inverse_witness(a, b):
    old_r, r = a, b
    old_s, s, old_t, t = [1], [0], [0], [1]
    while r != [0]:
        q, new_r = division(old_r, r)
        old_r, r = r, new_r
        old_s, s = s, add(old_s, scale(mul(q, s), -1))
        old_t, t = t, add(old_t, scale(mul(q, t), -1))
    assert len(old_r) == 1 and old_r[0]
    old_s, old_t = scale(old_s, 1 / Fraction(old_r[0])), scale(old_t, 1 / Fraction(old_r[0]))
    d = lcm(*(Fraction(v).denominator for v in old_s + old_t))
    sa, tb = [int(v * d) for v in old_s], [int(v * d) for v in old_t]
    assert add(mul(sa, a), mul(tb, b)) == [d]
    return {'s': sa, 't': tb, 'd': d}


def egcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def fm(a, b, p, z):
    return ((a[0] * b[0] + z * a[1] * b[1]) % p,
            (a[0] * b[1] + a[1] * b[0]) % p)


def fp(a, n, p, z):
    b = (1, 0)
    while n:
        if n & 1:
            b = fm(b, a, p, z)
        a = fm(a, a, p, z)
        n //= 2
    return b


def polynomials(p, z):
    assert p % 3 == 2 and pow(z, (p - 1) // 2, p) == p - 1
    values = [fp((1, b), (p * p - 1) // 3, p, z) for b in range(p)]
    omega = next(v for v in values if v != (1, 0))
    roots = [(1, 0), omega, fm(omega, omega, p, z)]
    assert len(set(roots)) == 3 and fp(omega, 3, p, z) == (1, 0)
    colors = [[b for b, v in enumerate(values) if v == root] for root in roots]
    assert sorted(sum(colors, [])) == list(range(p))
    assert [len(x) for x in colors] == [(p + 1) // 3 - 1, (p + 1) // 3, (p + 1) // 3]
    assert set(colors[0]) == {-b % p for b in colors[0]}
    assert set(colors[2]) == {-b % p for b in colors[1]}
    n = (p - 1) // 2
    C, V = [[2], [0, 1]], [[1], [0, 1]]
    for _ in range(1, n):
        C.append(add([0] + C[-1], scale(C[-2], -1)))
        V.append(add([0] + V[-1], scale(V[-2], -1)))
    psi = reduce(add, C[1:], [1])
    A = reduce(add, (C[b] for b in colors[0] if 1 <= b <= n), [1])
    B = reduce(add, (scale(V[b-1], (b in colors[1]) - (b in colors[2]))
                     for b in range(1, n + 1)), [0])
    return {'p': p, 'z': z, 'colors': colors, 'Psi': psi, 'A': A, 'B': B}


def create():
    rows = []
    for p, z in CASES:
        row = polynomials(p, z)
        a, b = inverse_witness(row['A'], row['Psi']), inverse_witness(row['B'], row['Psi'])
        g, u, v = egcd(a['d'], b['d'])
        weights = [u, v]
        if g != 1:
            c = inverse_witness(add(row['A'], scale(row['B'], 2)), row['Psi'])
            gg, uu, vv = egcd(g, c['d'])
            assert gg == 1
            row['bezout_A_plus_2B'] = c
            weights = [uu * u, uu * v, vv]
        row.update({'bezout_A': a, 'bezout_B': b, 'integer_bezout': weights})
        rows.append(row)
    return {'version': 1, 'cases': rows}


def verify(data):
    assert data['version'] == 1 and len(data['cases']) == len(CASES)
    for row, (p, z) in zip(data['cases'], CASES):
        plain = polynomials(p, z)
        assert all(row[k] == v for k, v in plain.items())
        for name in ['A', 'B']:
            w = row['bezout_' + name]
            assert w['d'] > 0
            assert all(isinstance(x, int) for x in w['s'] + w['t'])
            assert add(mul(w['s'], row[name]), mul(w['t'], row['Psi'])) == [w['d']]
        constants = [row['bezout_A']['d'], row['bezout_B']['d']]
        if 'bezout_A_plus_2B' in row:
            w = row['bezout_A_plus_2B']
            assert all(isinstance(x, int) for x in w['s'] + w['t'])
            assert add(mul(w['s'], add(row['A'], scale(row['B'], 2))),
                       mul(w['t'], row['Psi'])) == [w['d']]
            constants.append(w['d'])
        weights = row['integer_bezout']
        assert len(weights) == len(constants) and sum(x * y for x, y in zip(weights, constants)) == 1
        print(f'p={p}: verified integral polynomial identities with constants {constants}, and their Bezout combination is 1.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    path = Path(__file__).with_name('data') / 'small_level_exceptional_units.json'
    if args.write:
        path.write_text(json.dumps(create(), indent=2) + '\n')
    data = json.loads(path.read_text())
    verify(data)
    print('Verified exact unit ideals for all four levels.')
    print('SHA256', hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()

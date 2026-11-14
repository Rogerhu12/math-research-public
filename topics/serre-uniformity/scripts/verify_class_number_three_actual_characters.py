#!/usr/bin/env python3
"""Exact finite certificate for R91; Python standard library only.

The proof supplies the necessity of the character conditions. This script checks
all integer norms, full gcd factorizations, field arithmetic and Hasse lists.
No elliptic curve is asserted to realize either surviving character.
"""
import argparse
import hashlib
import json
from functools import lru_cache
from math import gcd, isqrt, prod
from pathlib import Path

SEEDS = {
    23: [2], 31: [2, 7], 59: [3, 5], 83: [3, 7, 11],
    107: [3, 11, 13], 139: [5, 7], 211: [5, 11, 13],
    283: [7, 11, 13, 23], 307: [7, 11, 17, 19],
    331: [5, 17, 19], 379: [5, 19, 23, 37],
    499: [5, 29, 31], 547: [11, 13, 19, 29],
    643: [7, 23], 883: [13, 17, 29], 907: [13, 19, 23, 41],
}
LOCAL_EXCLUSIONS = {
    (139, 59): 5, (379, 47): 19, (379, 59): 107,
    (499, 41): 29, (499, 59): 31, (547, 59): 19,
    (643, 59): 31, (883, 47): 29,
}
COUPLED_PRIMES = {
    (283, 47): [11, 13], (331, 47): [31], (331, 59): [17],
    (643, 47): [23], (883, 41): [17, 29],
    (907, 47): [23], (907, 59): [41],
}
EXPECTED_SURVIVORS = [(643, 47, (35, 5)), (907, 47, (25, 14))]
PRIMES = [n for n in range(2, 1001)
          if all(n % d for d in range(2, isqrt(n) + 1))]


def chi(D, q):
    if q == 2:
        return 1 if (-D) % 8 in (1, 7) else -1
    if D % q == 0:
        return 0
    return 1 if pow(-D, (q - 1) // 2, q) == 1 else -1


def trace(t, n, k, modulus=None):
    if k == 0:
        return 2
    a, b = 2, t
    for _ in range(1, k):
        a, b = b, t * b - n * a
        if modulus is not None:
            a, b = a % modulus, b % modulus
    return b if modulus is None else b % modulus


@lru_cache(None)
def norms(D, n, pure=0):
    """Represent n by (T^2+D Y^2)/4, with T>=0,Y>0.

    D is one of the sixteen odd fundamental discriminant magnitudes of h=3.
    A prime n cannot have Y=0. For n=q^3, pure=q deletes mixed ideals.
    """
    out = []
    for y in range(1, isqrt(4 * n // D) + 1):
        v = 4 * n - D * y * y
        t = isqrt(v)
        if t * t == v and (t - y) % 2 == 0:
            if not pure or gcd(gcd(t, y), pure) == 1:
                out.append((t, y))
    return out


def factor(n):
    assert n > 0
    ans = []
    for q in PRIMES:
        e = 0
        while n % q == 0:
            e += 1
            n //= q
        if e:
            ans.append([q, e])
    assert n == 1, 'The displayed factors must be a complete factorization.'
    return ans


def mul(a, b, p, z):
    return ((a[0] * b[0] + z * a[1] * b[1]) % p,
            (a[0] * b[1] + a[1] * b[0]) % p)


def power(a, n, p, z):
    b = (1, 0)
    while n:
        if n & 1:
            b = mul(b, a, p, z)
        a = mul(a, a, p, z)
        n //= 2
    return b


def scale(a, n, p):
    return (a[0] * n % p, a[1] * n % p)


def field_roots(q, p, z):
    """All (integer Hasse trace, beta) with Tr(beta)=a and N(beta)=q."""
    assert pow(z, (p - 1) // 2, p) == p - 1
    out = []
    for a in range(-isqrt(4 * q), isqrt(4 * q) + 1):
        x = a * pow(2, -1, p) % p
        for y in range(p):
            if (x * x - z * y * y - q) % p == 0:
                beta = (x, y)
                assert power(beta, p, p, z) == (x, -y % p)
                assert power(beta, p + 1, p, z) == (q % p, 0)
                out.append((a, beta))
    return out


def local_test(D, p, q):
    assert q in PRIMES and chi(D, q) == 1 and q % p != 1
    sol = norms(D, q ** 3, q)
    assert len(sol) == 1
    t, y = sol[0]
    target = trace(t, q ** 3, 12, p)
    principal = bool(norms(D, q))
    by_trace = [a for a in range(-isqrt(4 * q), isqrt(4 * q) + 1)
                if trace(a, q, 36, p) == target]
    before_cubic = []
    allowed = []
    for a, beta in field_roots(q, p, -D % p):
        if a not in by_trace:
            continue
        before_cubic.append([a, list(beta)])
        is_cube = power(beta, (p * p - 1) // 3, p, -D % p) == (1, 0)
        if is_cube == principal:
            allowed.append([a, list(beta)])
    return {'D': D, 'p': p, 'q': q, 'T': t, 'Y': y,
            'principal': principal, 'target': target, 'trace_values': by_trace,
            'roots_before_cubic': before_cubic, 'allowed': allowed}


def coupled_test(D, p, qs):
    z, order = -D % p, p * p - 1
    assert chi(D, p) == -1 and p % 9 in (2, 5)
    e = next(4 + k * order // 3 for k in range(3)
             if (4 + k * order // 3) % 3 == 0)
    assert e % (p - 1) == 4 % (p - 1)
    q0 = next(q for q in PRIMES if q > 3 and chi(D, q) == 1
              and not norms(D, q))
    assert q0 % p != 1
    sol = norms(D, q0 ** 3, q0)
    assert len(sol) == 1
    t0, y0 = sol[0]
    a0 = scale((t0, y0), pow(2, -1, p), p)
    target = power(a0, e, p, z)
    cs = sorted({power(beta, 4, p, z)
                 for _, beta in field_roots(q0, p, z)
                 if power(beta, 12, p, z) == target
                 and power(beta, order // 3, p, z) != (1, 0)})
    r0 = -t0 * pow(y0, -1, q0) % q0
    assert (r0 * r0 + D) % q0 == 0
    rows = []
    survivors = []
    for c in cs:
        tests = []
        for q in qs:
            assert q != q0 and q in PRIMES and chi(D, q) == 1 and q % p != 1
            assert not norms(D, q)
            gamma = norms(D, q * q0)
            assert len(gamma) == 1
            u, v = gamma[0]
            if (u + v * r0) % q0 == 0:
                v = -v
            assert (u + v * r0) % q0 != 0
            assert (u - v * r0) % q0 == 0
            assert u * u + D * v * v == 4 * q * q0
            gamma_bar = scale((u, v), pow(2, -1, p), p)
            nu = scale(mul(power(gamma_bar, e, p, z), c, p, z),
                       pow(pow(q0, 4, p), -1, p), p)
            allowed = [[a, list(beta)] for a, beta in field_roots(q, p, z)
                       if power(beta, 4, p, z) == nu]
            tests.append({'q': q, 'U': u, 'V': v, 'nu': list(nu),
                          'allowed': allowed})
        survives = all(row['allowed'] for row in tests)
        if survives:
            survivors.append((D, p, c))
        rows.append({'c': list(c), 'tests': tests, 'survives': survives})
    return {'D': D, 'p': p, 'e': e, 'q0': q0, 'T0': t0, 'Y0': y0,
            'r0': r0, 'candidates': rows}, survivors


def calculate():
    gcd_rows = []
    first = []
    for D, qs in SEEDS.items():
        g, relations = 0, []
        for q in qs:
            assert q in PRIMES and chi(D, q) == 1 and not norms(D, q)
            sol = norms(D, q ** 3, q)
            assert len(sol) == 1
            t, y = sol[0]
            terms = [trace(a, q, 36) - trace(t, q ** 3, 12)
                     for a in range(isqrt(4 * q) + 1)]
            assert all(terms)
            b = abs((q - 1) * prod(terms))
            g = gcd(g, b)
            relations.append([q, t, y])
        factors = factor(g)
        assert prod(q ** e for q, e in factors) == g
        candidates = [p for p, _ in factors if p > 37 and chi(D, p) == -1
                      and p % 9 in (2, 5)]
        first.extend((D, p) for p in candidates)
        gcd_rows.append({'D': D, 'relations': relations, 'gcd': str(g),
                         'factorization': factors, 'candidates': candidates})
    assert set(first) == set(LOCAL_EXCLUSIONS) | set(COUPLED_PRIMES)
    local_rows = []
    for (D, p), q in LOCAL_EXCLUSIONS.items():
        row = local_test(D, p, q)
        assert not row['allowed']
        local_rows.append(row)
    coupled_rows, survivors = [], []
    for (D, p), qs in COUPLED_PRIMES.items():
        row, surviving = coupled_test(D, p, qs)
        coupled_rows.append(row)
        survivors.extend(surviving)
    assert survivors == EXPECTED_SURVIVORS
    return {'version': 1, 'gcd_stage': gcd_rows, 'local_cubic_stage': local_rows,
            'coupled_stage': coupled_rows,
            'remaining_necessary_candidates': [[D, p, list(c)] for D, p, c in survivors]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    output = calculate()
    path = Path(__file__).with_name('data') / 'class_number_three_actual_characters.json'
    if args.write:
        path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    stored = json.loads(path.read_text())
    assert output == stored
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print('Verified 16 complete integer gcds, 15 prime candidates, 8 cubic exclusions,')
    print('and 7 globally coupled fourth-power character tests.')
    print('Remaining necessary pairs: (D,p)=(643,47),(907,47).')
    print('No existence of an elliptic curve is asserted.')
    print('SHA256', digest)


if __name__ == '__main__':
    main()

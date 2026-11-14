#!/usr/bin/env python3
"""Exact, standard-library certificate for a small same-shape R56 example.

No class-group, regulator, GRH, or fundamental-unit assertion is used.
Each row is (a, b, exponent_in_alpha, exponent_in_epsilon), for a+b*theta.
The rows were found with PARI, but their verification below is independent.
"""
import json
import math
import sys
from collections import defaultdict

sys.dont_write_bytecode = True
N = 52632
Q = 432 * N * N - 1
ROWS = [
    (2, 0, 1181, -35803), (3, 0, 430, -11585),
    (17, 0, 42, -1108), (29, 0, -65, 1875),
    (43, 0, 42, -1325), (101, 0, 6, 158),
    (-35, 1, 9, -130), (68, 1, 94, -2745),
    (-72, 5, -33, 867), (383, -8, -70, 2008),
    (50, 1, -92, 2667), (51, -1, -234, 6595),
    (301, 4, 137, -3855), (-299, -8, 183, -5565),
    (42, 1, -107, 3200), (59, -1, -40, 965),
    (143, 1, -13, 418), (353, 6, 154, -4741),
    (9, 1, 169, -5528), (110, 1, 66, -2062),
    (92, -1, -190, 5880), (56, -5, -51, 1552),
    (43, 1, -77, 2471), (11, -2, -8, 287),
    (570, 11, -42, 1325), (151, -1, 127, -4083),
    (119, 1, 98, -2742), (-121, -7, -66, 2062),
    (-211, -10, 13, -418), (419, 11, 65, -1875),
    (-16, 1, -37, 975), (-89, 1, -101, 2603),
    (-162, 1, -62, 2074), (203, 1, 63, -1797),
    (47, 1, -178, 5566), (-95, 1, -146, 4682),
    (118, 1, 16, -766), (96, 1, -30, 1304),
    (-172, 1, -102, 2709),
]


def factor(value):
    """Trial division; also supplies an unconditional primality test."""
    value = abs(value)
    assert value
    ans, d = {}, 2
    while d * d <= value:
        while value % d == 0:
            ans[d] = ans.get(d, 0) + 1
            value //= d
        d += 1 if d == 2 else 2
    if value > 1:
        ans[value] = ans.get(value, 0) + 1
    return ans


def valuation(value, prime):
    assert value
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def lift_simple(poly, root, prime, digits):
    modulus = prime
    assert poly(root) % modulus == 0
    while modulus < prime ** digits:
        candidates = [root + j * modulus for j in range(prime)
                      if poly(root + j * modulus) % (prime * modulus) == 0]
        assert len(candidates) == 1
        root, modulus = candidates[0], prime * modulus
    return root


def f(x):
    return x ** 3 - x - 8 * N


assert factor(Q) == {Q: 1}
assert all(f(x) % 13 for x in range(13))
assert N % (3 * 43) == 0 and valuation(N, 2) == 3
assert (Q + 1) % 172 == 0
digits = 16
two_roots = {
    0: lift_simple(f, 0, 2, digits),
    1: (1 + 4 * lift_simple(lambda t: t + 6*t*t + 8*t*t*t - N,
                            0, 2, digits)) % 2 ** digits,
    -1: (-1 + 4 * lift_simple(lambda t: t - 6*t*t + 8*t*t*t - N,
                              0, 2, digits)) % 2 ** digits,
}
three_roots = [lift_simple(f, j, 3, digits) for j in range(3)]
for root in two_roots.values():
    assert f(root) % 2 ** digits == 0

divisors = [defaultdict(int), defaultdict(int)]
norm_divisors = [defaultdict(int), defaultdict(int)]
signs = [1, 1]
ray_residues = [[1, 1, 1], [1, 1, 1]]
ray_valuations = [[0, 0, 0], [0, 0, 0]]
norm_prime_set, ideal_prime_set = set(), set()

for a, b, *exponents in ROWS:
    norm = a*a*a - a*b*b + 8*N*b*b*b
    norm_factors = factor(norm)
    norm_prime_set.update(norm_factors)
    row_divisor = {}
    if b == 0:
        assert a > 0
        for prime, v in factor(a).items():
            roots = (list(two_roots) if prime == 2 else
                     [t for t in range(prime) if f(t) % prime == 0])
            # Every rational factor in this certificate splits completely.
            assert len(roots) == 3
            for root in roots:
                row_divisor[prime, root] = v
    else:
        assert math.gcd(a, b) == 1
        for prime, v in norm_factors.items():
            if prime == 2:
                found = 0
                for label, root in two_roots.items():
                    value = (a + b * root) % 2 ** digits
                    assert value
                    w = valuation(value, 2)
                    found += w
                    if w:
                        row_divisor[2, label] = w
                assert found == v
            else:
                assert prime != Q and b % prime
                root = -a * pow(b, -1, prime) % prime
                assert f(root) % prime == 0
                assert (3 * root * root - 1) % prime
                row_divisor[prime, root] = v
    ideal_prime_set.update(row_divisor)
    for k, exponent in enumerate(exponents):
        for key, v in row_divisor.items():
            divisors[k][key] += exponent * v
        for prime, v in norm_factors.items():
            norm_divisors[k][prime] += exponent * v
        if norm < 0 and exponent % 2:
            signs[k] *= -1
        for j, root in enumerate(three_roots):
            value = (a + b * root) % 3 ** digits
            assert value
            v = valuation(value, 3)
            unit = value // 3 ** v % 3
            assert unit
            ray_valuations[k][j] += exponent * v
            ray_residues[k][j] *= pow(unit, exponent, 3)
            ray_residues[k][j] %= 3

divisors = [{key: v for key, v in d.items() if v} for d in divisors]
norm_divisors = [{key: v for key, v in d.items() if v}
                 for d in norm_divisors]
assert divisors == [{(2, 0): 14}, {}]
assert norm_divisors == [{2: 14}, {}]
assert signs == [1, 1]
assert ray_valuations == [[0, 0, 0], [0, 0, 0]]
assert ray_residues == [[2, 1, 2], [2, 1, 2]]
gamma_residues = [x*y % 3 for x, y in zip(*ray_residues)]
assert gamma_residues == [1, 1, 1]

print(json.dumps({
    "n": N, "q": Q, "q_primality": "exhaustive integer trial division",
    "irreducible_modulus": 13, "factor_rows": len(ROWS),
    "norm_primes": sorted(norm_prime_set),
    "checked_prime_ideals": len(ideal_prime_set),
    "alpha_ideal": "P0^14", "epsilon_ideal": "O_L",
    "alpha_norm": 2 ** 14, "epsilon_norm": 1,
    "alpha_mod_3_roots_0_1_minus1": ray_residues[0],
    "epsilon_mod_3_roots_0_1_minus1": ray_residues[1],
    "gamma_mod_3": gamma_residues,
    "certified_ray_relation": "14*c0 = 0; hence 42*c0 = 0",
    "asserted_exact_order": None,
}, indent=2))

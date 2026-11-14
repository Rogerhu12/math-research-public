#!/usr/bin/env python3
"""Exact finite certificates for R472; no target-prime search.

The geometric proof in R472 applies to every indicated branch.  This script
checks its floor identities and one actual canonical-source normal image.
The sample branch is algebraic, not claimed to be the original theta branch.
"""

from fractions import Fraction
import json


def ceildiv(a, b):
    return -((-a) // b)


def abc(n):
    return (n + 1) // 4, (n + 1) // 3, n // 2


def e(n):
    m = n + 1
    return 3 * ceildiv(3 * m, 4) + 2 * ceildiv(m, 2) + ceildiv(2 * m, 3) - 2


def f(n):
    a, b, c = abc(n)
    return 3 * a + b - c + e(n)


def total(d):
    return sum(e(n) + 1 for n in range(d + 1))


period = [e(n) + 1 for n in range(12)]
assert period == [5, 9, 14, 15, 21, 24, 30, 31, 36, 40, 46, 46]
assert sum(period) == 317
for n in range(12):
    assert e(n + 12) == e(n) + 47
    assert f(n) == 9 * n // 2 + 4
    assert f(n + 12) == f(n) + 54

# Both sides of (20) are explicit quadratics in m after fixing b mod 4.
# Three evaluations recover their exact coefficients; no extrapolation from
# primes or matrices is used.
expected = [(86, 90, -12), (86, 137, 14), (86, 200, 63), (86, 247, 120)]
prefix = [5, 43, 118, 225]
quadratics = []
for j in range(4):
    values = []
    for m in range(3):
        b = 4 * m + j
        a = 3 * m + (3 * j + 1) // 4
        u = b + int(j % 2 == 0)
        k = 9 * b + 8 - 3 * a
        hb = a + b * k - (b - 1) * u + 2 * b - 2
        nd = 282 * m * m + (82 + 141 * j) * m + prefix[j]
        assert nd == total(3 * b)
        values.append(4 * hb - nd - 3)
    q2 = Fraction(values[2] - 2 * values[1] + values[0], 2)
    q1 = values[1] - values[0] - q2
    q0 = values[0]
    assert (q2, q1, q0) == expected[j]
    quadratics.append([int(q2), int(q1), int(q0)])


p = 101
d = 6
b = 2
u = 1  # F = Y^2 - 1 - t, the branch psi = (1+t)^(1/2).
a_d, b_d, _ = abc(d)
n0 = d - b + 1
k = 5 * n0 + 4 - n0 % 2 - 3 * a_d - b_d
h = a_d + b * k - (b - 1) * u + 2 * b - 2
length = h + 1
assert (n0, k, h, length) == (5, 23, 48, 49)
assert f(d) < p and length < p


def mul(a, b):
    c = [0] * length
    for i, x in enumerate(a[:length]):
        if x:
            for j, y in enumerate(b[:length-i]):
                if y:
                    c[i+j] = (c[i+j] + x * y) % p
    return c


def powpoly(poly, exponent):
    result = [1] + [0] * (length - 1)
    poly = poly + [0] * (length - len(poly))
    for _ in range(exponent):
        result = mul(result, poly)
    return result


def binomial_series(exponent, scalar):
    exponent %= p
    coeff = [1]
    for i in range(1, length):
        coeff.append(coeff[-1] * (exponent - i + 1) * scalar * pow(i, -1, p) % p)
    return coeff


columns = []
for n in range(1, d + 1):
    a_n, b_n, c_n = abc(n)
    # n * psi^n * q_n: the actual Euler derivative of a source column.
    base = binomial_series(n * pow(2, -1, p), 1)
    base = mul(base, powpoly([7, 4, 16], a_n))
    base = mul(base, powpoly([-1, 1], b_n))
    base = mul(base, binomial_series(-c_n, 8))
    base = [n * x % p for x in base]
    for polynomial_degree in range(e(n) + 1):
        shift = a_n + polynomial_degree
        vector = [0] * min(shift, length) + base[:max(0, length-shift)]
        assert len(vector) == length
        columns.append(vector)

pivots = {}
for column in columns:
    v = column[:]
    for row in range(length):
        if not v[row]:
            continue
        if row in pivots:
            pivot = pivots[row]
            scale = v[row]
            v = [(x - scale*y) % p for x, y in zip(v, pivot)]
        else:
            inverse = pow(v[row], -1, p)
            pivots[row] = [x * inverse % p for x in v]
            break
assert len(pivots) == length

print(json.dumps({
    "result": "passed",
    "source_period": period,
    "exact_four_residue_quadratics": quadratics,
    "normal_image_sample": {
        "prime": p,
        "D": d,
        "F": "Y^2-1-t",
        "branch": "psi(0)=1",
        "actual_positive_charge_columns": len(columns),
        "jet_length": length,
        "rank": len(pivots),
        "is_claimed_original_theta_branch": False,
    },
}, indent=2))

#!/usr/bin/env python3
"""Exact finite sums used in the F=-15 abelian-torsion proof; no tables."""

from math import gcd


def legendre(n, p):
    n %= p
    if not n:
        return 0
    value = pow(n, (p - 1) // 2, p)
    assert value in (1, p - 1)
    return 1 if value == 1 else -1


for p, expected_count, a, b in ((53, 68, -7, 2), (61, 74, -6, 5)):
    assert all(p % d for d in range(2, int(p**0.5) + 1))
    assert p % 4 == 1 and legendre(-15, p) == 1
    count = p + 1 + sum(legendre(x**3 - 17 * x, p) for x in range(p))
    assert count == expected_count
    assert p + 1 - count == 2 * a
    assert a * a + b * b == p
    print(f"q={p}: #E={count}, a_q={2*a}, Frobenius={a} +/- {b}i, gap={2*b}i")

assert gcd(4, 10) == 2
assert gcd(53, 10) == 1 and gcd(61, 4) == 1
print("Both primary exceptions vanish; the remaining torsion is killed by 2.")

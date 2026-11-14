#!/usr/bin/env python3
"""Exact rational R51 coefficients at m=(p-1)p^n; default p=13, n=0,1."""
import argparse
from fractions import Fraction as Q
from math import comb, factorial, isqrt


def mul(a, b, n):
    out = [Q(0)] * (n + 1)
    for i, x in enumerate(a[:n + 1]):
        for j, y in enumerate(b[:n + 1 - i]):
            out[i + j] += x * y
    return out


def inverse(a, n):
    out = [1 / a[0]] + [Q(0)] * n
    for j in range(1, n + 1):
        out[j] = -out[0] * sum(a[i] * out[j - i]
                               for i in range(1, min(j, len(a) - 1) + 1))
    return out


def power(a, e, n):
    if e < 0:
        a, e = inverse(a, n), -e
    out = [Q(1)] + [Q(0)] * n
    while e:
        if e & 1:
            out = mul(out, a, n)
        a, e = mul(a, a, n), e >> 1
    return out


def coefficient(m):
    assert m >= 4 and m % 4 == 0
    r = m // 4
    c = [Q(1)]
    for n in range(1, r + 1):
        c.append(c[-1] * Q(2 * n - 1, 2 * n))
    F = [c[n] / (4 * n + 1) for n in range(r + 1)]
    H = [c[n] / (4 * n + 3) for n in range(r + 1)]
    theta_log_prime = [x / 4 for x in mul(c, H, r)]
    theta17 = [Q(1)]
    for n in range(1, r + 1):
        theta17.append(Q(17, n) * sum(
            theta_log_prime[i] * theta17[n - 1 - i] for i in range(n)
        ))
    B = mul(theta17, [Q(0), Q(1), Q(3, 5), Q(-1, 5), Q(1, 5)], r)
    W = mul(B, c, r)
    return 17 ** (r - 1) * mul(W, power(F, -m - 1, r), r)[r]


def log_normalized(p, precision):
    """log(1+p)/p modulo p^precision, retaining exact p-denominators."""
    mod, total, k = p ** precision, 0, 1
    while True:
        lower, test = 0, k
        while test >= p:
            test //= p
            lower += 1
        if k - 1 - lower >= precision:
            break
        unit, valuation = k, 0
        while unit % p == 0:
            unit //= p
            valuation += 1
        term = pow(p, k - 1 - valuation, mod) * pow(unit, -1, mod)
        total = (total + (-1 if k % 2 == 0 else 1) * term) % mod
        k += 1
    return total


def main(p, maximum_n):
    assert p >= 13 and p % 4 == 1 and p != 17
    assert all(p % d for d in range(2, isqrt(p) + 1))
    assert maximum_n >= 0
    hasse = pow(-17, (p - 1) // 4, p) * comb((p - 1) // 2, (p - 1) // 4) % p
    previous = None
    for n in range(maximum_n + 1):
        m = (p - 1) * p ** n
        b = coefficient(m)
        if p == 13 and n == 0:
            assert b == Q(9313603, 50400)
        C = factorial(m - 1) * b
        modulus = p ** (n + 2)
        residue = C.numerator * pow(C.denominator, -1, modulus) % modulus
        assert residue % p == 0
        if previous is not None:
            assert (residue - previous) % (p ** (n + 1)) == 0
        slope_mod = p ** (n + 1)
        teich = pow(hasse, p ** (n + 1), slope_mod)
        log_unit = log_normalized(p, n + 1)
        slope = (residue // p) * pow(teich * log_unit, -1, slope_mod) % slope_mod
        print(f"p={p} n={n} m={m} C_n mod p^(n+2)={residue} "
              f"J'_p(0) mod p^(n+1)={slope}")
        previous = residue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=13)
    parser.add_argument("--maximum-n", type=int, default=1)
    args = parser.parse_args()
    main(args.prime, args.maximum_n)

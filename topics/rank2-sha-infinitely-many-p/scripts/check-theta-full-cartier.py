#!/usr/bin/env python3
"""Exact fixed-u coefficient checks for the full theta Cartier identity.

No Katz values, p-adic periods, or modular calibration are used.
The fixed rational series satisfy
Theta'/Theta=H/(4*sqrt(1-v)), A(z(u))*dz/du=W(17*u^4)/17.
"""
import argparse
from fractions import Fraction as Q
from math import comb, isqrt


def mul(a, b, nmax):
    return [
        sum(
            (a[j] * b[n - j] for j in range(
                max(0, n - len(b) + 1), min(n, len(a) - 1) + 1
            )),
            Q(0),
        )
        for n in range(nmax + 1)
    ]


def valuation(x, p):
    if not x:
        return float("inf")
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def residue(x, p):
    return x.numerator * pow(x.denominator, -1, p) % p


def fixed_w(nmax):
    c = [Q(comb(2 * n, n), 4 ** n) for n in range(nmax + 1)]
    h = [c[n] / (4 * n + 3) for n in range(nmax)]
    ell = [x / 4 for x in mul(h, c, nmax - 1)]
    theta17 = [Q(1)]
    for n in range(1, nmax + 1):
        theta17.append(Q(17, n) * sum(
            (ell[j] * theta17[n - 1 - j] for j in range(n)), Q(0)
        ))
    q = [Q(0), Q(1), Q(3, 5), Q(-1, 5), Q(1, 5)]
    return mul(mul(theta17, q, nmax), c, nmax)


def check(p):
    if (p < 13 or p == 17 or p % 4 != 1
            or any(p % d == 0 for d in range(2, isqrt(p) + 1))):
        raise ValueError("Require an ordinary target prime p>=13, p!=17.")
    r, nmax = (p - 1) // 4, (5 * p - 1) // 4
    w = fixed_w(nmax)
    assert all(valuation(x, p) >= 0 for x in w)
    y = [17 ** (n - 1) * w[n] / (4 * n + 1)
         for n in range(1, nmax + 1)]
    assert all(valuation(x, p) >= 0 for x in y[:-1])
    assert valuation(y[-1], p) == -1
    hasse = pow(-17, r, p) * comb(2 * r, r) % p
    coefficient = 17 ** (nmax - 1) * w[nmax]
    actual, predicted = residue(coefficient, p), pow(hasse, -4, p)
    assert actual == predicted
    print(
        f"p={p}: v_p(w_({r}))={valuation(w[r],p)}, "
        f"[u^(5p-1)] A*dz/du = {actual} = H_p^(-4) mod p; "
        f"first nonintegral primitive coefficient u^{5*p}, valuation -1."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int, default=[13, 29, 37, 41])
    args = parser.parse_args()
    for prime in args.primes:
        check(prime)

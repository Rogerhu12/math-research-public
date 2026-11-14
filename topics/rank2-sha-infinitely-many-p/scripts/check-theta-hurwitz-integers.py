#!/usr/bin/env python3
"""Exact integer Hurwitz recursion for the actual R51 theta factor.

All working arithmetic is in Z or Z[i].  Fractions are used only to compare
the final coefficients with the four independently certified R51 values.
No p-adic L-value, central trace, or numerical sigma evaluation is input.
"""
import argparse
from fractions import Fraction
from math import comb, factorial

GI = tuple[int, int]


def gi_mul(a: GI, b: GI) -> GI:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gi_pow(a: GI, n: int) -> GI:
    r = (1, 0)
    while n:
        if n & 1:
            r = gi_mul(r, a)
        a = gi_mul(a, a)
        n //= 2
    return r


def hurwitz_mul(a: list[GI], b: list[GI], nmax: int) -> list[GI]:
    out = [(0, 0)] * (nmax + 1)
    for n in range(nmax + 1):
        re = im = 0
        for j in range(n + 1):
            if a[j] == (0, 0) or b[n - j] == (0, 0):
                continue
            x, y = gi_mul(a[j], b[n - j])
            c = comb(n, j)
            re += c * x
            im += c * y
        out[n] = (re, im)
    return out


def universal_sigma_theta(nmax: int) -> tuple[list[int], list[int]]:
    """D=1 solution of u''=-2u^3, L'=u^2, theta'=L theta."""
    u = [0] * (nmax + 3)
    ell = [0] * (nmax + 2)
    theta = [0] * (nmax + 2)
    u2 = [0] * (nmax + 1)
    u[1] = 1
    theta[0] = 1
    for n in range(nmax + 1):
        u2[n] = sum(comb(n, j) * u[j] * u[n - j] for j in range(n + 1))
        u[n + 2] = -2 * sum(
            comb(n, j) * u[j] * u2[n - j] for j in range(n + 1)
        )
        ell[n + 1] = u2[n]
        theta[n + 1] = sum(
            comb(n, j) * ell[j] * theta[n - j] for j in range(n + 1)
        )
    sigma = [
        sum(comb(n, j) * u[j] * theta[n - j] for j in range(n + 1))
        for n in range(nmax + 1)
    ]
    assert all(t == 0 for n, t in enumerate(theta[: nmax + 1]) if n % 4)
    assert all(s == 0 for n, s in enumerate(sigma) if n % 4 != 1)
    return sigma, theta[: nmax + 1]


def scaled(a: list[int], param: GI, residue: int) -> list[GI]:
    out = []
    for n, value in enumerate(a):
        if value == 0:
            out.append((0, 0))
            continue
        assert n % 4 == residue
        power = gi_pow(param, (n - residue) // 4)
        out.append((value * power[0], value * power[1]))
    return out


def coefficients(nmax: int, D: int) -> list[int]:
    sigma, theta = universal_sigma_theta(nmax)
    factors = [
        scaled(theta, (D, 0), 0),
        scaled(theta, (16 * D, 0), 0),
        scaled(sigma, (D, 0), 1),
        scaled(sigma, (D, 0), 1),
        scaled(sigma, (-7 * D, 24 * D), 1),
        scaled(sigma, (-7 * D, -24 * D), 1),
    ]
    product = [(1, 0)] + [(0, 0)] * nmax
    for factor in factors:
        product = hurwitz_mul(product, factor, nmax)
    assert all(im == 0 for re, im in product)
    out = [re for re, im in product]
    assert all(h == 0 for n, h in enumerate(out) if n % 4 or n == 0)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-degree", type=int, default=32)
    args = parser.parse_args()
    if args.max_degree < 16:
        parser.error("--max-degree must be at least 16")
    universal = coefficients(args.max_degree, 1)
    actual = coefficients(args.max_degree, 17)
    certified = {
        4: Fraction(1),
        8: Fraction(1649, 60),
        12: Fraction(9313603, 50400),
        16: Fraction(2421363742117, 1297296000),
    }
    for n, b in certified.items():
        assert Fraction(actual[n], factorial(n)) == b
        print(f"m={n}: h_m={actual[n]}; b_m={b}")
    for n in range(4, args.max_degree + 1, 4):
        assert actual[n] == 17 ** (n // 4 - 1) * universal[n]
    print(f"All integer recursions and D-scaling checked through degree {args.max_degree}.")
    print("First universal integers a_k (D=1):")
    for n in range(4, min(args.max_degree, 24) + 1, 4):
        print(f"a_{n // 4}={universal[n]}")


if __name__ == "__main__":
    main()

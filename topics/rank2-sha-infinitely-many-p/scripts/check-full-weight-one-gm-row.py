#!/usr/bin/env python3
"""Exact checks of the actual weight-one Gauss--Manin critical rows.

Actual theta coefficients come from the independent integer polynomial flow.
The check then constructs the algebraic modular-function germ formally and
compares the two Euler/logarithm rows with the factorial square coefficients.
It also verifies the first unavoidable noncritical denominators.
"""
import argparse
import importlib.util
from fractions import Fraction
from math import factorial
from pathlib import Path

from flint import ctx, fmpq, fmpq_series


def as_fraction(x):
    return Fraction(int(x.numerator), int(x.denominator))


def vp(x, p):
    x = as_fraction(x) if not isinstance(x, Fraction) else x
    if x == 0:
        return 10**9
    a, b, v = x.numerator, x.denominator, 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def residue(x, p):
    x = as_fraction(x) if not isinstance(x, Fraction) else x
    assert x.denominator % p
    return (x.numerator * pow(x.denominator, -1, p)) % p


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", default="7,11,13,19,29,37")
    args = parser.parse_args()
    primes = [int(x) for x in args.primes.split(",")]
    assert all(p >= 7 and p != 17 for p in primes)
    nmax = max(primes) + 6
    ctx.cap = nmax + 1

    source = Path(__file__).with_name("check-theta-hurwitz-integers.py")
    spec = importlib.util.spec_from_file_location("hurwitz_flow", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    h = module.coefficients(nmax, 1)
    c = [fmpq(0) for _ in range(nmax + 1)]
    for m in range(4, nmax + 1, 4):
        c[m] = fmpq(h[m] ** 2, 24 * factorial(m) * 17 ** (m - 4))
    assert c[4] == 1

    k = [fmpq(0) for _ in range(nmax + 1)]
    l = [fmpq(0) for _ in range(nmax + 2)]
    k[0], l[1] = fmpq(1), fmpq(1)
    for n in range(nmax - 1):
        k[n + 2] = k[n] * fmpq((2 * n + 1) ** 2, (n + 1) * (n + 2))
    for n in range(nmax):
        l[n + 2] = l[n] * fmpq((2 * n + 1) ** 2, (n + 1) * (n + 2))
    t = fmpq_series([0, 1])
    K = fmpq_series(k)
    L = fmpq_series(l[: nmax + 1])
    J = fmpq_series(l[1 : nmax + 2])
    u = L / K
    # E(u)/K; no reversion is used in this direction.
    eu = fmpq_series([0])
    for m in range(nmax, -1, -1):
        eu = eu * u + c[m]
    M = eu / K
    assert M[4] == 1 and M[6] == fmpq(7, 2)
    assert all(M[n] == 0 for n in range(nmax + 1) if n % 2)
    ell = (K / J).log()
    Wi = M * K / ((1 - 4 * t**2) * J**2)
    Wo = M / ((1 - 4 * t**2) * K)
    Gi = fmpq_series(
        [Wi[n] / (n - 1) if n != 1 else fmpq(0) for n in range(nmax + 1)]
    ) + Wi * ell
    Wol = Wo * ell
    Go = fmpq_series(
        [Wo[n] / ((n + 1) ** 2) + Wol[n] / (n + 1) for n in range(nmax + 1)]
    ) + Wo * ell**2 / 2

    print("M4=1, M6=7/2; actual factorial-square coefficients used.")
    for p in primes:
        assert all(vp(M[n], p) >= 0 for n in range(nmax + 1))
        if p % 4 == 3:
            m, first = p + 1, p + 5
            direct = c[m] / p
            assert vp(direct, p) >= 0
            assert vp(Gi[m] - direct, p) >= 1
            assert all(vp(Gi[n], p) >= 0 for n in range(first))
            assert vp(Gi[first], p) == -1
            kappa = p * K[p + 1]
            assert residue(p * Gi[first] - 5 * kappa / 4, p) == 0
            print(
                f"inert p={p}: C_(p+1)/p={residue(direct,p)} mod p; "
                f"G_i first denominator at t^{first}, "
                f"p*coefficient={residue(p*Gi[first],p)}"
            )
        else:
            m, first = p - 1, p + 3
            direct = c[m] / (p * p)
            assert vp(direct, p) >= 0
            assert vp(Go[m] - direct, p) >= 1
            assert all(vp(Go[n], p) >= 0 for n in range(first))
            assert vp(Go[first], p) == -1
            kappa = p * J[p - 1]
            assert residue(p * Go[first] + kappa / 4, p) == 0
            print(
                f"ordinary p={p}: C_(p-1)/p^2={residue(direct,p)} mod p; "
                f"G_o first denominator at t^{first}, "
                f"p*coefficient={residue(p*Go[first],p)}"
            )
    print("Both critical rows and all stated first-break identities passed.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact actual-theta check of the integral PF principal-part reduction.

This is a calibration certificate, not a substitute for the triangular proof.
"""
import argparse
import importlib.util
from math import factorial
from pathlib import Path

from flint import ctx, fmpq, fmpq_series


def vp(x, p):
    if x == 0:
        return 10**9
    a, b, v = int(x.numerator), int(x.denominator), 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def residue(x, p):
    a, b = int(x.numerator), int(x.denominator)
    assert b % p
    return a * pow(b, -1, p) % p


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", default="7,11,19")
    args = parser.parse_args()
    primes = [int(p) for p in args.primes.split(",")]
    assert all(p >= 7 and p % 4 == 3 for p in primes)
    degree = max(primes) + 2
    ctx.cap = degree + 1

    source = Path(__file__).with_name("check-theta-hurwitz-integers.py")
    spec = importlib.util.spec_from_file_location("hurwitz_flow", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    h = module.coefficients(degree, 1)
    c = [fmpq(0) for _ in range(degree + 1)]
    for m in range(4, degree + 1, 4):
        c[m] = fmpq(h[m] ** 2, 24 * factorial(m) * 17 ** (m - 4))

    k = [fmpq(0) for _ in range(degree + 1)]
    l = [fmpq(0) for _ in range(degree + 2)]
    k[0], l[1] = fmpq(1), fmpq(1)
    for n in range(degree - 1):
        k[n + 2] = k[n] * fmpq((2 * n + 1) ** 2, (n + 1) * (n + 2))
    for n in range(degree):
        l[n + 2] = l[n] * fmpq((2 * n + 1) ** 2, (n + 1) * (n + 2))
    t = fmpq_series([0, 1])
    K, L = fmpq_series(k), fmpq_series(l[:degree + 1])
    J = fmpq_series(l[1:degree + 2])
    u, eu = L / K, fmpq_series([0])
    for m in range(degree, -1, -1):
        eu = eu * u + c[m]
    M = eu / K
    assert M[4] == 1 and M[6] == fmpq(7, 2)

    for p in primes:
        numerator = M * K**p / ((1 - 4 * t**2) * J**(p + 2))
        f = {j - p - 2: numerator[j] for j in range(4, p + 2, 2)}
        assert f[-p + 2] == 1
        assert all(vp(a, p) >= 0 for a in f.values())
        remainder, R = f.copy(), {}
        for pole in range(p - 2, 2, -2):
            m = pole - 2
            r = remainder.get(-pole, fmpq(0)) / (m * (m + 1))
            R[-m] = r
            remainder[-pole] = fmpq(0)
            remainder[-m] = remainder.get(-m, fmpq(0)) + (1 - 2*m)**2 * r
        C = remainder[-1]
        assert all(vp(a, p) >= 0 for a in R.values())
        assert all(a == 0 for e, a in remainder.items() if e != -1)
        assert C == c[p + 1]
        assert sum(a * K[-e - 1] for e, a in f.items()) == C
        assert sum(a * L[-e - 1] for e, a in f.items()) == 0
        reconstructed = {-1: C}
        for e, a in R.items():
            reconstructed[e - 2] = reconstructed.get(e - 2, fmpq(0)) + e*(e-1)*a
            reconstructed[e] = reconstructed.get(e, fmpq(0)) - (2*e+1)**2*a
        assert all(reconstructed.get(e, 0) == f.get(e, 0)
                   for e in set(reconstructed) | set(f))
        print(f"p={p}: exact f=D(R)+C/t; pole={p-2}; "
              f"R integral; C/p={residue(C/p,p)} mod p")
    print("All actual principal parts and factorial-square residues agree.")


if __name__ == "__main__":
    main()

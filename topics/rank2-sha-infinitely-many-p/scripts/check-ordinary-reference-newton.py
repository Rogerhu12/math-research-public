#!/usr/bin/env python3
"""Period-free ordinary slope certificate from two fixed integer sequences.

The certificate uses only weights j*(p-1), 1 <= j <= R <= p-2.
Euler factors are omitted using the proved p^(R+1) error bound.
The optional p=13, R=2 normalization check uses a separate reference weight156;
that high weight is not used to form the Newton certificate itself.
"""
import argparse
import importlib.util
from fractions import Fraction
from math import comb
from pathlib import Path

module_path = Path(__file__).with_name("check-theta-hurwitz-integers.py")
spec = importlib.util.spec_from_file_location("theta_hurwitz", module_path)
hurwitz = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hurwitz)


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def mod_fraction(x: Fraction, modulus: int) -> int:
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def certificate(p: int, R: int) -> tuple[Fraction, int]:
    nmax = R * (p - 1)
    actual = hurwitz.coefficients(nmax, 17)
    _, theta = hurwitz.universal_sigma_theta(nmax)
    rho = [Fraction(0)]
    for j in range(1, R + 1):
        m = j * (p - 1)
        reference = theta[m] * 17 ** (m // 4)
        assert reference % p != 0
        rho.append(Fraction(actual[m], reference))
    S = sum(
        Fraction((-1) ** (r + 1), r)
        * sum((-1) ** (r - j) * comb(r, j) * rho[j] for j in range(r + 1))
        for r in range(1, R + 1)
    )
    residue = mod_fraction(S, p ** (R + 1))
    assert residue % p == 0
    # R<=p-2, so every displayed denominator is a p-unit; omitted terms
    # of log(1+p)/p have valuation at least R.
    L_over_p = sum(Fraction((-1) ** (n + 1) * p ** (n - 1), n)
                   for n in range(1, R + 1))
    slope = (
        (residue // p)
        * pow(mod_fraction((p - 1) * L_over_p, p**R), -1, p**R)
    ) % (p**R)
    return S, slope


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=13)
    parser.add_argument("--precision", type=int, default=2)
    args = parser.parse_args()
    p, R = args.prime, args.precision
    if not is_prime(p) or p < 13 or p % 4 != 1 or p == 17:
        parser.error("use an ordinary target prime p>=13, p!=17")
    if not 1 <= R <= p - 2:
        parser.error("this finite implementation requires 1 <= R <= p-2")
    S, slope = certificate(p, R)
    residue = mod_fraction(S, p ** (R + 1))
    print(f"p={p}, R={R}, highest certificate weight={R*(p-1)}")
    print(f"pure rational Newton sum mod p^(R+1): {residue}")
    print(f"reference-normalized derivative mod p^R: {slope}")
    if p == 13 and R == 2:
        assert residue == 1248 and slope == 60
        _, theta = hurwitz.universal_sigma_theta(156)
        H = (-17) ** 3 * comb(6, 3) % 13
        assert H == 7
        teich_H = pow(H, 13, 13**2)
        t156 = theta[156] * 17**39
        ref_center = t156 * pow(teich_H, -1, 13**2) % 13**2
        assert ref_center == 133
        actual_slope = slope * ref_center % 13**2
        assert actual_slope == 37
        print("Separate reference-center normalization check (weight156):")
        print(f"J_theta(0) mod169={ref_center}; actual J_A'(0) mod169={actual_slope}")


if __name__ == "__main__":
    main()

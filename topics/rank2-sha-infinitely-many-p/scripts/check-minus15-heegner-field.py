"""Rigorous L'(E17^(-15), 1) > 0 certificate; requires python-flint.

Two independent coefficient generators: finite-field point counts and
Gaussian CM characters. All arithmetic before Arb evaluation is integral.
The mathematical conductor, sign, Mellin formula and tail bound are proved
in notes/2026-11-12-explicit-minus15-heegner-field.md.
"""

from hashlib import sha256
from math import isqrt

from flint import arb, ctx

LIMIT = 10000
CONDUCTOR = 2080800
BAD = {2, 3, 5, 17}
ctx.prec = 160


def smallest_prime_factors(bound):
    spf = list(range(bound + 1))
    for p in range(2, isqrt(bound) + 1):
        if spf[p] == p:
            for n in range(p * p, bound + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def trace_by_points(p):
    if p in BAD or p % 4 == 3:
        return 0
    legendre = [-1] * p
    for x in range(p):
        legendre[x * x % p] = 1
    legendre[0] = 0
    return -sum(legendre[(x * x * x - 3825 * x) % p] for x in range(p))


def trace_by_gaussian_cm(p):
    if p in BAD or p % 4 == 3:
        return 0
    for b in range(2, isqrt(p) + 1, 2):
        a = isqrt(p - b * b)
        if a * a + b * b == p:
            if (a + b) % 4 != 1:
                a = -a
            break
    else:
        raise AssertionError(("sum of two squares", p))
    assert a % 2 and (a + b) % 4 == 1
    i_mod_p = -a * pow(b, -1, p) % p
    assert i_mod_p * i_mod_p % p == p - 1
    quartic = pow(17, (p - 1) // 4, p)
    trace_e17 = {
        1: 2 * a, p - 1: -2 * a,
        i_mod_p: 2 * b, -i_mod_p % p: -2 * b,
    }[quartic]
    chi_minus3 = 1 if p % 3 == 1 else -1
    chi_5 = 1 if p % 5 in (1, 4) else -1
    return trace_e17 * chi_minus3 * chi_5


def coefficients(spf, trace):
    values = [0] * len(spf)
    values[1] = 1
    for n in range(2, len(spf)):
        p, m = spf[n], n // spf[n]
        if m == 1:
            values[n] = trace(p)
        else:
            values[n] = values[p] * values[m]
            if m % p == 0 and p not in BAD:
                values[n] -= p * values[m // p]
    return values


def main():
    assert CONDUCTOR == 2**5 * 3**2 * 5**2 * 17**2
    spf = smallest_prime_factors(LIMIT)
    coeff = coefficients(spf, trace_by_points)
    independent = coefficients(spf, trace_by_gaussian_cm)
    assert coeff == independent
    fingerprint = sha256(",".join(map(str, coeff[1:])).encode("ascii")).hexdigest()
    assert fingerprint == "90e3384900c4c11cc88ca71625d24332df0de5886a5ec2012f28edd4d4f85fc3"
    scale = arb(CONDUCTOR).sqrt() / (2 * arb.pi())
    partial = arb(0)
    for n, a_n in enumerate(coeff[1:], 1):
        if a_n:
            partial -= 2 * arb(a_n) / n * (-arb(n) / scale).ei()
    tail = (4 * scale / (LIMIT + 1)
            * (-arb(LIMIT + 1) / scale).exp()
            / (1 - (-1 / scale).exp()))
    enclosure = partial + arb(0, tail.upper())
    assert tail < arb("2.548e-18")
    assert enclosure > 12 and enclosure < 13
    print("two coefficient generators agree through", LIMIT)
    print("coefficient SHA256:", fingerprint)
    print("partial sum:", partial)
    print("tail bound:", tail)
    print("certified L-prime:", enclosure)
    print("proved: 12 < L'(E17^(-15), 1) < 13")


if __name__ == "__main__":
    main()

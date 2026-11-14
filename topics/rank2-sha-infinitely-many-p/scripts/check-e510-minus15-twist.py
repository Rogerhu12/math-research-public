"""Rigorous L'(E34^(-15),1)>0 and fixed negative-point certificate.

E34^(-15) is y^2=x^3-260100*x.  The conductor, functional-equation
sign, exact Mellin identity, and tail estimate are proved in
notes/2026-11-12-two-curve-negative-localization-and-e510-certificate.md.
Requires python-flint.  No BSD assumption or database rank is used.
"""

from hashlib import sha256
from math import isqrt

from flint import arb, ctx

LIMIT = 16000
CONDUCTOR = 4161600
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
    return -sum(legendre[(x * x * x - 260100 * x) % p]
                for x in range(p))


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
    chi = pow(510, (p - 1) // 2, p)
    assert chi in (1, p - 1)
    return (1 if chi == 1 else -1) * 2 * a


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
    assert 1144**2 == 121**3 - 3825 * 121
    assert 25200**2 == 960**3 - 260100 * 960
    assert 1144 % 11 == 0 and (64 * 3825**3) % 11 != 0
    assert 25200 % 7 == 0 and (64 * 260100**3) % 7 != 0
    assert CONDUCTOR == 2**6 * 3**2 * 5**2 * 17**2
    spf = smallest_prime_factors(LIMIT)
    coeff = coefficients(spf, trace_by_points)
    independent = coefficients(spf, trace_by_gaussian_cm)
    assert coeff == independent
    fingerprint = sha256(",".join(map(str, coeff[1:])).encode("ascii")).hexdigest()
    assert fingerprint == (
        "90ae9e9f8b23f8553fa8d92c4439cfacc09ec59e07aaf9f17c57030562d49562"
    )
    scale = arb(CONDUCTOR).sqrt() / (2 * arb.pi())
    partial = arb(0)
    for n, a_n in enumerate(coeff[1:], 1):
        if a_n:
            partial -= 2 * arb(a_n) / n * (-arb(n) / scale).ei()
    tail = (4 * scale / (LIMIT + 1)
            * (-arb(LIMIT + 1) / scale).exp()
            / (1 - (-1 / scale).exp()))
    enclosure = partial + arb(0, tail.upper())
    assert tail < arb("1.043e-20")
    assert enclosure > 13 and enclosure < 14
    print("fixed negative points verified exactly")
    print("two coefficient generators agree through", LIMIT)
    print("coefficient SHA256:", fingerprint)
    print("partial sum:", partial)
    print("tail bound:", tail)
    print("certified L-prime:", enclosure)
    print("proved: 13 < L'(E34^(-15), 1) < 14")


if __name__ == "__main__":
    main()

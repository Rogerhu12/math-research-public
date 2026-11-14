"""Exact arithmetic and Arb certificate for E389 twisted by -7.

No elliptic-curve database, rank routine, or floating zero threshold is used.
The note 2026-11-12-noncm-e389-and-minus7-heegner-field.md proves the
conductor, sign, Mellin identity, and analytic tail bound.

Requirements: python-flint.  Every coefficient is independently obtained
from (i) discriminant counts on the twist, and (ii) y-value histograms on
the original curve followed by the primitive character modulo 7.
"""

from hashlib import sha256
from math import isqrt

from flint import acb, arb, ctx


LIMIT = 2000
CM_LIMIT = 2500
CONDUCTOR = 389 * 7**2
BAD = {7, 389}
ctx.prec = 192


def smallest_prime_factors(bound):
    spf = list(range(bound + 1))
    for p in range(2, isqrt(bound) + 1):
        if spf[p] == p:
            for n in range(p * p, bound + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def count_histogram(p, a2, a4, a6):
    """Count the projective equation y^2+y=x^3+a2*x^2+a4*x+a6."""
    y_count = [0] * p
    for y in range(p):
        y_count[(y * y + y) % p] += 1
    return 1 + sum(y_count[(x**3 + a2*x*x + a4*x + a6) % p]
                   for x in range(p))


def trace_by_twist_discriminant(p):
    if p == 7:
        return 0  # additive I_0^*: the local Euler factor is 1
    if p == 2:
        return p + 1 - count_histogram(p, -7, -98, -86)
    legendre = [-1] * p
    for r in range(p):
        legendre[r * r % p] = 1
    legendre[0] = 0
    # Completing the square gives (2y+1)^2 = this cubic.
    # At 389 the same singular-projective count gives a_389=+1.
    return -sum(legendre[(4*x**3 - 28*x*x - 392*x - 343) % p]
                for x in range(p))


def trace_by_original_and_character(p):
    if p == 7:
        return 0
    base_trace = p + 1 - count_histogram(p, 1, -2, 0)
    residue = pow(p % 7, 3, 7)
    chi = -1 if residue == 6 else residue
    assert chi in (-1, 1)
    return chi * base_trace


def trace_by_original(p):
    return p + 1 - count_histogram(p, 1, -2, 0)


def coefficients(spf, prime_trace, bad=BAD):
    values = [0] * len(spf)
    values[1] = 1
    for n in range(2, len(spf)):
        p, m = spf[n], n // spf[n]
        if m == 1:
            values[n] = prime_trace(p)
        else:
            values[n] = values[p] * values[m]
            if m % p == 0 and p not in bad:
                values[n] -= p * values[m // p]
    return values


def invariants(a2, a3, a4, a6):
    b2, b4 = 4*a2, 2*a4
    b6 = a3*a3 + 4*a6
    b8 = 4*a2*a6 + a2*a3*a3 - a4*a4
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    delta = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    return c4, c6, delta


def main():
    assert invariants(1, 1, -2, 0) == (112, -856, 389)
    assert invariants(-7, 1, -98, -86) == (
        112*7**2, -856*(-7)**3, 389*7**6)
    x, y = 16, 25
    assert y*y+y == x**3-7*x*x-98*x-86
    assert count_histogram(5, -7, -98, -86) == 3
    assert count_histogram(11, -7, -98, -86) == 16
    assert count_histogram(29, 1, -2, 0) == 36
    assert 95**2 % 389 == 856 % 389  # split node at 389
    assert 185**2 % 389 == (-7) % 389  # 389 splits in Q(sqrt(-7))
    assert 29 == 1**2 + 7*2**2

    spf = smallest_prime_factors(LIMIT)
    coeff = coefficients(spf, trace_by_twist_discriminant)
    independent = coefficients(spf, trace_by_original_and_character)
    assert coeff == independent
    fingerprint = sha256(
        ",".join(map(str, coeff[1:])).encode("ascii")).hexdigest()
    assert fingerprint == (
        "93c2fada5a30865f0134e7fa3eb9bba60d80a09f8e750695eb30d54f94022524")
    assert coeff[389] == 1 and coeff[7] == 0 and coeff[29] == -6

    scale = arb(CONDUCTOR).sqrt() / (2 * arb.pi())
    partial = arb(0)
    for n, a_n in enumerate(coeff[1:], 1):
        if a_n:
            partial -= 2 * arb(a_n) / n * (-arb(n) / scale).ei()
    tail = (4 * scale / (LIMIT + 1)
            * (-arb(LIMIT + 1) / scale).exp()
            / (1 - (-1 / scale).exp()))
    enclosure = partial + arb(0, tail.upper())
    assert tail < arb("2.788e-40")
    assert enclosure > 4 and enclosure < 5

    print("coefficient generators agree through", LIMIT)
    print("coefficient SHA256:", fingerprint)
    print("partial sum:", partial)
    print("tail bound:", tail)
    print("certified L-prime:", enclosure)
    print("proved: 4 < L'(E389^(-7), 1) < 5")
    print("negative rational point: (16,25) on y^2+y=x^3-7x^2-98x-86")
    print("q=29: #E389(F29)=36, a29=-6")

    # The Heegner point is represented by (389,185,22), discriminant -7.
    # Each exponential is evaluated directly, avoiding rectangle-radius
    # growth from a long complex Horner evaluation.
    assert 185**2 - 4*389*22 == -7
    cm_spf = smallest_prime_factors(CM_LIMIT)
    base_coeff = coefficients(cm_spf, trace_by_original, bad={389})
    tau = acb(-arb(185)/778, arb(7).sqrt()/778)
    exponent = 2 * arb.pi() * acb(0, 1) * tau
    f_partial = acb(0)
    for n, a_n in enumerate(base_coeff[1:], 1):
        if a_n:
            f_partial += a_n * (n*exponent).exp()
    radius = exponent.real.exp()
    f_tail = (2 * radius**(CM_LIMIT+1)
              * ((CM_LIMIT+1)/(1-radius) + radius/(1-radius)**2))
    error_ball = arb(0, f_tail.upper())
    f_enclosure = f_partial + acb(error_ball, error_ball)
    assert f_tail < arb("1.492e-18")
    assert f_enclosure.real > -19 and f_enclosure.real < -18
    assert f_enclosure.imag > -67 and f_enclosure.imag < -66
    print("CM tau:", tau)
    print("f(tau) partial:", f_partial)
    print("f(tau) analytic tail:", f_tail)
    print("f(tau) certified rectangle:", f_enclosure)
    print("proved: the actual modular map is unramified at this CM point")


if __name__ == "__main__":
    main()

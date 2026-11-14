#!/usr/bin/env python3
"""Arb certificate for the sixteen actual full-class CM differentials.

For the R150 fixed map Phi_D = sum_{d|D0} pi(d*z), its differential is a
nonzero common scalar times sum_{d|D0} d*f(d*z).  This script evaluates
that precise sum, including every class term, at a primitive form of
discriminant D and leading coefficient 389*D0.

All Fourier coefficients are computed from the equation of E389a1,
twice (point histograms and discriminant character sums).  The omitted
tail uses |a_n| <= d(n)*sqrt(n) <= 2*n.  No rank or modular-form database
and no numerical zero threshold are used.

Requirement: python-flint.  Run from the repository or any directory.
"""

from hashlib import sha256
from math import gcd, isqrt

from flint import acb, arb, ctx


LIMIT = 10000
PRECISION = 192
ROWS = (
    (-7, 1, 185), (-11, 1, 355), (-67, 1, 189),
    (-20, 2, 330), (-24, 2, 216), (-35, 5, 1595), (-52, 2, 470),
    (-187, 11, 3927), (-232, 2, 508), (-267, 3, 1137),
    (-372, 6, 1866), (-483, 21, 2037), (-555, 15, 3975),
    (-795, 15, 1305), (-1435, 35, 2345), (-532, 14, 2366),
)
REAL_INTERVALS = {
    -7: (-19, -18), -11: (-36, -35), -67: (-16, -15),
    -20: (-39, -38), -24: (30, 31), -35: (-17, -16),
    -52: (-40, -39), -187: (-41, -40), -232: (9, 10),
    -267: (16, 17), -372: (19, 20), -483: (-46, -45),
    -555: (-25, -24), -795: (-75, -74), -1435: (-107, -106),
    -532: (26, 27),
}


def smallest_prime_factors(bound):
    spf = list(range(bound + 1))
    for p in range(2, isqrt(bound) + 1):
        if spf[p] == p:
            for n in range(p*p, bound + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def prime_trace_histogram(p):
    counts = [0] * p
    for y in range(p):
        counts[(y*y + y) % p] += 1
    return p - sum(counts[(x*x*x + x*x - 2*x) % p]
                   for x in range(p))


def prime_trace_discriminant(p):
    if p == 2:
        # Direct four affine substitutions give #E(F_2)=5.
        return -2
    chi = [-1] * p
    for y in range(p):
        chi[y*y % p] = 1
    chi[0] = 0
    return -sum(chi[(4*x*x*x + 4*x*x - 8*x + 1) % p]
                for x in range(p))


def coefficients(spf, prime_trace):
    result = [0] * len(spf)
    result[1] = 1
    for n in range(2, len(spf)):
        p, m = spf[n], n // spf[n]
        if m == 1:
            result[n] = prime_trace(p)
        else:
            result[n] = result[p] * result[m]
            if m % p == 0 and p != 389:
                result[n] -= p * result[m // p]
    return result


def old_coefficients(base, D0):
    divisors = [d for d in range(1, D0 + 1) if D0 % d == 0]
    old = [0] * len(base)
    for d in divisors:
        for n in range(d, len(base), d):
            old[n] += d * base[n // d]
    return divisors, old


def tail_bound(y, divisors):
    result = arb(0)
    for d in divisors:
        length = LIMIT // d
        radius = (-2*arb.pi()*d*y).exp()
        result += 2*d*radius**(length+1) * (
            (length+1)/(1-radius) + radius/(1-radius)**2)
    return result


def factor(n):
    ans = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            ans[q] = ans.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        ans[n] = 1
    return ans


def reduced_forms(D):
    result = []
    for a in range(1, isqrt((-D)//3)+1):
        for b in range(-a, a+1):
            if (b*b-D) % (4*a):
                continue
            c = (b*b-D)//(4*a)
            if a > c or gcd(gcd(a, abs(b)), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            result.append((a, b, c))
    return result


def reduce_form(a, b, c):
    D = b*b-4*a*c
    while True:
        k = (a-b)//(2*a)
        b, c = b+2*a*k, a*k*k+b*k+c
        if a > c:
            a, b, c = c, -b, a
            continue
        if a == c and b < 0:
            b = -b
        if b == -a:
            b = a
        assert -a < b <= a <= c and b*b-4*a*c == D
        return (a, b, c)


def certify_field_replacement(base):
    D = -532
    assert D//4 == -133 and (-133) % 4 == 3
    assert factor(133) == {7: 1, 19: 1}
    assert pow(D % 389, 194, 389) == 1
    expected = [(1, 0, 133), (2, 2, 67), (7, 0, 19), (13, 12, 13)]
    assert reduced_forms(D) == expected
    products = []
    for a in (1, 2, 7, 14):
        b = 0 if D % (4*a) == 0 else a
        assert (b*b-D) % (4*a) == 0
        products.append(reduce_form(a, b, (b*b-D)//(4*a)))
    assert products == expected
    assert 2**2 + 133 == 137 and factor(137) == {137: 1}
    assert base[137] == -2
    basis = {}
    for D, _, _ in ROWS:
        v = {-1} | {p for p, e in factor(-D).items() if e % 2}
        while v:
            leading = max(v)
            if leading in basis:
                v.symmetric_difference_update(basis[leading])
            else:
                basis[leading] = v
                break
        assert v, ("dependent quadratic character", D)
    assert len(basis) == 16
    print("replacement D=-532: exact class basis {2,7}, h=4, q=137, a_q=-2")
    print("replacement family: sixteen independent quadratic characters")


def certify_row(D, D0, b, base):
    A = 389*D0
    assert (b*b-D) % (4*A) == 0
    c = (b*b-D)//(4*A)
    assert gcd(gcd(A, b), c) == 1
    roots = [r for r in range(2*A)
             if (r*r-D) % (4*A) == 0
             and gcd(gcd(A, r), (r*r-D)//(4*A)) == 1]
    assert roots == [b, 2*A-b]
    tau = acb(-arb(b)/(2*A), arb(-D).sqrt()/(2*A))
    divisors, old = old_coefficients(base, D0)
    exponent = 2*arb.pi()*acb(0, 1)*tau
    partial = acb(0)
    for n, coefficient in enumerate(old[1:], 1):
        if coefficient:
            # Direct exponentials avoid long complex-ball power chains.
            partial += coefficient * (n*exponent).exp()
    tail = tail_bound(tau.imag, divisors)
    assert tail < arb("8e-31")
    error = arb(0, tail.upper())
    enclosure = partial + acb(error, error)
    nonzero = (enclosure.real > 0 or enclosure.real < 0
               or enclosure.imag > 0 or enclosure.imag < 0)
    if D in REAL_INTERVALS:
        lower, upper = REAL_INTERVALS[D]
        assert enclosure.real > lower and enclosure.real < upper
    print(f"D={D:5d} D0={D0:2d} form=({A},{b},{c})")
    print("  complete differential =", enclosure)
    print("  rigorous tail <=", tail)
    print("  nonzero certified:", nonzero)
    return nonzero


def main():
    ctx.prec = PRECISION
    spf = smallest_prime_factors(LIMIT)
    first = coefficients(spf, prime_trace_histogram)
    second = coefficients(spf, prime_trace_discriminant)
    assert first == second
    assert first[389] == 1  # split multiplicative reduction
    digest = sha256(",".join(map(str, first[1:])).encode("ascii")).hexdigest()
    assert digest == "fb0e6b8e5cd6bf515097b4ed5af33d7f7fabd00c6c0343d875237d25ad500a44"
    print("exact coefficient generators agree through", LIMIT)
    print("coefficient SHA256:", digest)
    certify_field_replacement(first)
    certified = [certify_row(*row, first) for row in ROWS]
    assert all(certified), ("unresolved CM differential rows",
                            [row[0] for row, good in zip(ROWS, certified) if not good])
    print("PASS: all sixteen actual full-class differentials are nonzero.")
    print("Galois conjugation and complex conjugation cover all 2*h_D centers.")
    # A targeted diagnostic of the excluded row.  A ball containing zero
    # proves no equality; this row is not used by the replacement theorem.
    ctx.prec = 512
    print("Excluded D=-19: higher-precision diagnostic, not a zero certificate.")
    certify_row(-19, 1, 337, first)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact finite certificate for the actual 68-level weight-one Hecke packet.

No floating-point arithmetic.  All cyclotomic calculations take place in
Z[X]/Phi_272(X), with zeta_68=X^4 and zeta_16=X^17.
"""

from collections import deque
from fractions import Fraction
from math import gcd

N = 68
ORDER = 272
DEGREE = 128
DIVISORS = (1, 2, 4, 17, 34, 68)
LOG17 = {pow(3, j, 17): j for j in range(16)}


def orbit():
    points = {(1, 67)}
    queue = deque(points)
    while queue:
        a, b = queue.popleft()
        for v in (((-3*a) % N, (-3*b) % N),
                  ((-2*a-b) % N, (a-2*b) % N)):
            if v not in points:
                points.add(v)
                queue.append(v)
    return points


S = orbit()
MINUS = {((-a) % N, (-b) % N) for a, b in S}
assert len(S) == 256 and not S.intersection(MINUS)


def weight(a, b):
    v = (a % N, b % N)
    return int(v in S) - int(v in MINUS)


ROWS = {b: [(a, weight(a, b)) for a in range(N) if weight(a, b)]
        for b in range(N)}


def reduce_cyclotomic(raw):
    v = list(raw) + [0] * (ORDER-len(raw))
    # Phi_272 = X^128-X^120+...-X^8+1.
    for e in range(ORDER-1, DEGREE-1, -1):
        c = v[e]
        if c:
            for j in range(16):
                v[e-DEGREE+8*j] -= c * (-1)**j
            v[e] = 0
    return tuple(v[:DEGREE])


def units(modulus):
    return ([x for x in range(modulus) if gcd(x, modulus) == 1]
            if modulus > 1 else [0])


def character_exponent(x, epsilon, k):
    ans = 136*epsilon*((x-1)//2 % 2) if epsilon else 0
    if k:
        ans += 17*k*LOG17[x % 17]
    return ans % ORDER


def C_raw(d, e):
    out = [0]*ORDER
    for a, value in ROWS[e % N]:
        out[(4*a*d) % ORDER] += value
    return out


def add_shift(out, raw, shift, scalar=1):
    for j, value in enumerate(raw):
        if value:
            out[(j+shift) % ORDER] += scalar*value


def main():
    scalar_group = {pow(-3, j, N) for j in range(16)}
    assert scalar_group == {u for u in range(N)
                            if gcd(u, N) == 1 and u % 4 == 1}
    for u in units(N):
        sign = 1 if u % 4 == 1 else -1
        for a, b in S | MINUS:
            assert weight(u*a, u*b) == sign*weight(a, b)
    assert all(b % 2 for a, b in S)
    constant = sum(Fraction(b, N)-Fraction(1, 2) for a, b in S)
    assert constant == 4

    # Coefficients A_(g,h,chi), stored before cyclotomic reduction.
    # The denominator is phi(68/g); psi=chi*chi_-4 on (Z/68)^x.
    coeffs = {}
    nonzero = []
    for g in DIVISORS:
        R = N//g
        xx = units(R)
        chars = [(ep, k)
                 for ep in range(2 if R % 4 == 0 else 1)
                 for k in range(16 if R % 17 == 0 else 1)]
        for h in (1, 17):
            for ep, k in chars:
                if h == 17 and k:
                    continue
                raw = [0]*ORDER
                for x in xx:
                    shift = -character_exponent(x, ep, k)
                    add_shift(raw, C_raw(g*x, h), shift)
                coeffs[g, h, ep, k] = (raw, len(xx))
                if any(reduce_cyclotomic(raw)):
                    nonzero.append((g, h, ep, k))

    expected = {(g, 1, int(g == 1), k)
                for g in (1, 2, 4) for k in range(16)}
    expected |= {(g, 17, int(g in (1, 17)), 0) for g in DIVISORS}
    expected |= {(g, 1, int(g == 17), 0) for g in (17, 34, 68)}
    assert set(nonzero) == expected and len(nonzero) == 57

    # Verify the entire finite multiplicative Fourier decomposition,
    # not just a few q-coefficients.  All denominators divide 32.
    for d in range(N):
        g = gcd(d, N)
        for e in range(N):
            h = gcd(e, N)
            raw = [0]*ORDER
            if h in (1, 17):
                x, y = d//g, e//h
                for (gg, hh, ep, k), (A, denominator) in coeffs.items():
                    if (gg, hh) != (g, h):
                        continue
                    shift = (character_exponent(x, ep, k) +
                             character_exponent(y, ep ^ 1, k))
                    add_shift(raw, A, shift, 32//denominator)
            assert reduce_cyclotomic(raw) == reduce_cyclotomic(
                [32*a for a in C_raw(d, e)]), (d, e)

    # Every primitive pair with k != 0 has zero constant term.
    # For k=0, an imprimitive factor at 2 or 17 kills the constant.
    # The only remaining primitive pair is (1 mod 1, chi_-4 mod 4).
    A, denominator = coeffs[68, 17, 0, 0]
    red = reduce_cyclotomic(A)
    assert denominator == 1 and red[0] == -16 and not any(red[1:])
    assert -Fraction(red[0], 4) == constant

    # Independent finite check of U_p f=V_p sigma_(p^2) f.
    bound = 300
    fourier = [[0]*ORDER for _ in range(bound+1)]
    fourier[0][0] = 4
    for d in range(1, bound+1):
        for e in range(1, bound//d+1):
            add_shift(fourier[d*e], C_raw(d, e), 0, -1)
    for p in (3, 7, 11, 19):
        for n in range(bound//p+1):
            target = [0]*ORDER
            if n % p == 0:
                for j, a in enumerate(fourier[n//p]):
                    target[j*p*p % ORDER] += a
            assert reduce_cyclotomic(fourier[p*n]) == \
                reduce_cyclotomic(target), (p, n)

    print("Exact 256-point orbit and scalar chi_-4 covariance: passed")
    print("All 68^2 residue pairs in the finite Fourier decomposition: passed")
    print("Nonzero components: 57; all 16 modulo-17 characters retained")
    print("Cusp constant: 4; unique contributing component A_(68,17)=-16")
    print("Inert U_p/V_p coefficient checks at p=3,7,11,19: passed")


if __name__ == "__main__":
    main()

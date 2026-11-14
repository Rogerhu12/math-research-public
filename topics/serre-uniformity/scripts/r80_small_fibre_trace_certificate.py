#!/usr/bin/env python3
"""Exact integer certificate for R80; no network or optional dependencies.

Phi_3 coefficients are from Andrew Sutherland's author-maintained data:
https://math.mit.edu/~drew/modpolys/jfiles/phi_j_3.txt
The file lists (i,j), i>=j; off-diagonal terms are reflected.
Their defining interpretation is justified in the proof, not by this script.
"""

from fractions import Fraction
from math import isqrt


def determinant3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def is_square(n):
    return n >= 0 and isqrt(n) ** 2 == n


def main():
    # Four points with short sides forming a perfect matching.
    twice_gram = ((2, 1, 1), (1, 4, 3), (1, 3, 4))
    gram_determinant = Fraction(determinant3(twice_gram), 8)
    assert gram_determinant == Fraction(3, 2)
    print("four-point difference Gram determinant / p^3 =", gram_determinant)

    # Symmetric coefficient table, including the leading X^4 and Y^4 terms.
    upper = {
        (1, 0): 1855425871872000000000,
        (1, 1): -770845966336000000,
        (2, 0): 452984832000000,
        (2, 1): 8900222976000,
        (2, 2): 2587918086,
        (3, 0): 36864000,
        (3, 1): -1069956,
        (3, 2): 2232,
        (3, 3): -1,
        (4, 0): 1,
    }
    J = 54000
    phi = [0] * 5  # ascending powers of Y in Phi_3(J,Y)
    for (i, j), coefficient in upper.items():
        phi[j] += coefficient * J**i
        if i != j:
            phi[i] += coefficient * J**j

    # Synthetic division by Y-J, in descending coefficient order.
    descending = list(reversed(phi))
    quotient = [descending[0]]
    for coefficient in descending[1:-1]:
        quotient.append(coefficient + J * quotient[-1])
    remainder = descending[-1] + J * quotient[-1]
    expected = [
        1,
        -151013228706000,
        224179462188000000,
        -1879994705688000000000,
    ]
    assert remainder == 0
    assert quotient == expected
    print("H_-108 coefficients, descending =", quotient)

    # The proof reduces the only unexcluded class-number-one conductor to M=108.
    # The necessary inequalities are M<3p and 16p<=7M.
    M = 108
    candidates = [
        p
        for p in range(38, 7 * M // 16 + 1)
        if is_prime(p)
        and p % 3 == 2
        and M < 3 * p
        and is_square(7 * M - 16 * p)
    ]
    assert candidates == [41, 47]
    print("remaining (p,M) candidates =", [(p, M) for p in candidates])

    trace = -quotient[1]
    for p in candidates:
        actual = trace % p
        collapsed = (-3 * 3375) % p
        assert actual != collapsed
        print(
            f"p={p}: trace(H_-108)={actual} mod p; "
            f"trace of (Y+3375)^3={collapsed} mod p"
        )

    assert (7 * 243) % 16 == 5
    assert 5 not in {n * n % 16 for n in range(16)}
    print("M=243: 7M-16p is 5 mod 16, hence never a square")


if __name__ == "__main__":
    main()

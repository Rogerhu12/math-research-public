#!/usr/bin/env python3
"""Exact certificate for the rational four-parameter theta section.

All power series are calculated over Q.  Reduction modulo 101 is used only
to certify a nonzero rational 10 by 10 determinant.  No floating point,
central L-value, p-adic L-value, or external package is used.
"""
from fractions import Fraction as Q

N = 10
ELL = 101


def series_log(a):
    """log(a), where a[0] = 1."""
    assert a[0] == 1
    out = [Q(0)] * (N + 1)
    for n in range(1, N + 1):
        out[n] = a[n] - sum(
            (k * out[k] * a[n-k] for k in range(1, n)), Q(0)
        ) / n
    return out


def series_exp(a):
    """exp(a), where a[0] = 0."""
    assert a[0] == 0
    out = [Q(1)] + [Q(0)] * N
    for n in range(1, N + 1):
        out[n] = sum(
            k * a[k] * out[n-k] for k in range(1, n + 1)
        ) / n
    return out


def coefficient_rows(D):
    # x(z)=z^-2 X(z^4); x''=6x^2-2D for y^2=x^3-Dx.
    X = [Q(1)] + [Q(0)] * N
    for n in range(1, N + 1):
        X[n] = (
            6 * sum((X[j] * X[n-j] for j in range(1, n)), Q(0))
            - 2 * D * (n == 1)
        ) / ((4*n-2)*(4*n-3)-12)

    # L=log(sigma(z)/z), and theta_T^2=x sigma^2.
    L = [Q(0)] + [
        -X[n] / (4*n*(4*n-1)) for n in range(1, N+1)
    ]
    log_X = series_log(X)
    basis = []
    for j in range(1, 5):
        exponent = [
            Q(17-4*j, 2) * log_X[n] + 17 * L[n]
            for n in range(N+1)
        ]
        unit = series_exp(exponent)
        basis.append([Q(0)]*j + unit[:N+1-j])
    return [
        [basis[j][n] for j in range(4)] for n in range(1, N+1)
    ]


def residue(x):
    assert x.denominator % ELL
    return x.numerator * pow(x.denominator, -1, ELL) % ELL


def square_matrix(rows):
    # Column order 11,12,13,14,22,23,24,33,34,44.
    return [
        [
            residue(row[i] * row[j] * (1 if i == j else 2))
            for i in range(4) for j in range(i, 4)
        ]
        for row in rows
    ]


def determinant_mod(M):
    a = [row[:] for row in M]
    d = 1
    for j in range(len(a)):
        r = next((r for r in range(j, len(a)) if a[r][j]), None)
        if r is None:
            return 0
        if r != j:
            a[j], a[r] = a[r], a[j]
            d = -d
        pivot = a[j][j]
        d = d * pivot % ELL
        scale = pow(pivot, -1, ELL)
        for r in range(j+1, len(a)):
            c = a[r][j] * scale % ELL
            a[r] = [
                (a[r][k] - c * a[j][k]) % ELL
                for k in range(len(a))
            ]
    return d % ELL


def main():
    rows_1 = coefficient_rows(1)
    rows_17 = coefficient_rows(17)
    for n in range(1, N+1):
        for j in range(1, 5):
            if n >= j:
                assert rows_17[n-1][j-1] == 17**(n-j) * rows_1[n-1][j-1]
            else:
                assert rows_1[n-1][j-1] == rows_17[n-1][j-1] == 0

    det_1 = determinant_mod(square_matrix(rows_1))
    det_17 = determinant_mod(square_matrix(rows_17))
    assert det_1 != 0
    assert det_17 == pow(17, 60, ELL) * det_1 % ELL
    print("Coefficient rows for D=1, reduced modulo 101:")
    for n, row in enumerate(rows_1, 1):
        print(n, *(residue(x) for x in row))
    print("Quadratic column order: 11 12 13 14 22 23 24 33 34 44")
    print("Determinant modulo 101, D=1:", det_1)
    print("Determinant modulo 101, D=17:", det_17)
    print("Exact D-scaling: verified.  Rational rank: 10.")


if __name__ == "__main__":
    main()

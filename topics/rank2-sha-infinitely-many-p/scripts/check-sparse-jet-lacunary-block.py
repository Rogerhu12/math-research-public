#!/usr/bin/env python3
"""Exact certificate for R194; no prime scan and no floating-point arithmetic."""

from fractions import Fraction as Q
from math import factorial


def determinant(matrix):
    a = [list(map(Q, row)) for row in matrix]
    answer = Q(1)
    for col in range(len(a)):
        pivot = next((i for i in range(col, len(a)) if a[i][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            answer = -answer
        value = a[col][col]
        answer *= value
        for i in range(col + 1, len(a)):
            ratio = a[i][col] / value
            for j in range(col + 1, len(a)):
                a[i][j] -= ratio * a[col][j]
    return answer


def residue(value, prime):
    value = Q(value)
    return value.numerator * pow(value.denominator, -1, prime) % prime


def rank_mod(matrix, prime):
    a = [[residue(value, prime) for value in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, prime)
        a[rank] = [value * inverse % prime for value in a[rank]]
        for i in range(rows):
            if i != rank:
                multiple = a[i][col]
                a[i] = [(x - multiple * y) % prime
                        for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def main():
    prime, r, degree, j = 23, 6, 7, 3
    nodes = []
    original = []
    for m in range(degree + 1):
        for c in range(m + 1):
            t, remainder = divmod(m + c, r)
            if remainder == j and t < prime:
                nodes.append((m, t))
                original.append((m - c, c, t))
    assert nodes == [(2, 0), (3, 0), (5, 1), (6, 1), (7, 1)]
    assert original == [(1, 1, 0), (3, 0, 0), (1, 4, 1),
                        (3, 3, 1), (5, 2, 1)]
    matrix = [[Q(m ** (h - t), factorial(h - t)) if h >= t else Q(0)
               for m, t in nodes] for h in range(6)]
    first = determinant(matrix[:5])
    next_minor = determinant([matrix[h] for h in (0, 1, 2, 3, 5)])
    assert first == Q(161, 24)
    assert next_minor == Q(3083, 90)
    assert rank_mod(matrix[:5], prime) == 4
    assert rank_mod(matrix, prime) == 5
    kernel = [5, 18, 7, 20, 1]
    images = [sum(residue(x, prime) * y for x, y in zip(row, kernel)) % prime
              for row in matrix]
    assert images[:5] == [0] * 5
    assert images[5] != 0
    actual_orders = [r * h + j for h in range(6)]
    assert max(actual_orders) < r * (prime - 1) + 1
    integral = Q(60) - Q(47, 2) + Q(12, 3) - Q(1, 4)
    assert integral == Q(161, 4)
    assert first == integral / 6
    assert residue(integral, prime) == residue(Q(-115, 512), prime) == 0

    # Finite algebraic calibration of the closed multiplicity formula.
    for degree in range(1, 33):
        multiplicities = [(h, 2 * degree - 4 * h + 1)
                          for h in range(degree // 2 + 1)]
        assert sum(count for _, count in multiplicities) == (degree + 1) * (degree + 2) // 2
        total = sum(h * count for h, count in multiplicities)
        d = degree // 2
        expected = (d * (d + 1) * (4 * d - 1) // 6 if degree % 2 == 0
                    else d * (d + 1) * (4 * d + 5) // 6)
        assert total == expected

    print("PASS: legal p=23, D=7, j=3 original columns")
    print("det(first five rows) =", first)
    print("det(rows 0,1,2,3,5) =", next_minor)
    print("mod-23 ranks = 4, 5; sixth kernel image =", images[5])
    print("integral factor =", integral, "; actual w orders =", actual_orders)
    print("PASS: sparse Smith multiplicities and determinant exponent formulas")


if __name__ == "__main__":
    main()

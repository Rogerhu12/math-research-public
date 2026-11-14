#!/usr/bin/env python3
"""Exact finite-field rank witness; no external packages or analytic input."""

from itertools import permutations
from math import prod


B = 635318657
POINTS = [
    (-24964, 549998),
    (-3481, -1472876),
    (-17956, 2370326),
    (-17689, 2388148),
]
CERTIFICATE = [
    (11, 12, (9, 2), [1, 2, 0, 2]),
    (23, 24, (3, 11), [0, 1, 1, 1]),
    (47, 48, (8, 1), [1, 2, 0, 0]),
    (59, 60, (29, 31), [0, 0, 1, 1]),
]


def add(left, right, q):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and (y + v) % q == 0:
        return None
    if x == u:
        slope = (3 * x * x - B) * pow(2 * y, -1, q) % q
    else:
        slope = (v - y) * pow(u - x, -1, q) % q
    z = (slope * slope - x - u) % q
    return z, (slope * (x - z) - y) % q


def mul(n, point, q):
    result = None
    while n:
        if n & 1:
            result = add(result, point, q)
        point = add(point, point, q)
        n >>= 1
    return result


def point_count(q):
    # Explicit enumeration is independent of the group law above.
    return 1 + sum(
        (y * y - x * x * x + B * x) % q == 0
        for x in range(q)
        for y in range(q)
    )


def determinant(matrix):
    n = len(matrix)
    total = 0
    for perm in permutations(range(n)):
        inversions = sum(
            perm[i] > perm[j] for i in range(n) for j in range(i + 1, n)
        )
        total += (-1) ** inversions * prod(matrix[i][perm[i]] for i in range(n))
    return total


def main():
    assert B == 158**4 + 59**4 == 134**4 + 133**4
    assert B == 41 * 113 * 241 * 569
    assert B % 16 == 1
    assert all(y * y == x * x * x - B * x for x, y in POINTS)
    assert point_count(5) == 10  # No rational 3-primary torsion.
    assert point_count(13) == 20  # Good ordinary witness prime p=13.
    matrix = []
    for q, count, generator, expected in CERTIFICATE:
        assert B % q and point_count(q) == count
        assert count % 3 == 0 and count % 9 != 0
        assert generator is not None and mul(3, generator, q) is None
        lookup = {None: 0, generator: 1, mul(2, generator, q): 2}
        row = [
            lookup[mul(count // 3, (x % q, y % q), q)] for x, y in POINTS
        ]
        assert row == expected
        matrix.append(row)
        print(f"q={q}, #E={count}, generator={generator}, row={row}")
    det = determinant(matrix)
    assert det % 3 == 2
    print(f"determinant={det}, determinant mod 3={det % 3}")
    print("Exact rank-at-least-four witness and good ordinary p=13 verified.")


if __name__ == "__main__":
    main()

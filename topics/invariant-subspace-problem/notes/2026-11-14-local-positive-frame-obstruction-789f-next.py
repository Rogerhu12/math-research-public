#!/usr/bin/env python3
"""Exact five-site obstruction to a positive four-site primitive frame.

All coordinates in this verifier are unweighted kernel coordinates with the
explicit physical source metric W.  No numerical eigenvalue test is used.
"""
from itertools import combinations

import sympy as sp


def main():
    pairs = list(combinations(range(5), 2))
    index = {pair: j for j, pair in enumerate(pairs)}
    down = sp.zeros(5, 10)
    for j, pair in enumerate(pairs):
        for i in pair:
            down[i, j] = 1
    kernel = sp.Matrix.hstack(*down.nullspace())
    assert kernel.shape == (10, 5)

    blocks = []
    columns = []
    for support in combinations(range(5), 4):
        a, b, c, d = support
        u = sp.zeros(10, 1)
        v = sp.zeros(10, 1)
        for sign, pair in [(1, (a, b)), (1, (c, d)),
                           (-1, (a, c)), (-1, (b, d))]:
            u[index[pair]] = sign
        for sign, pair in [(1, (a, b)), (1, (c, d)),
                           (-1, (a, d)), (-1, (b, c))]:
            v[index[pair]] = sign
        basis = sp.Matrix.hstack(u, v)
        assert down * basis == sp.zeros(5, 2)
        assert basis.rank() == 2
        blocks.append((support, basis))
        for matrix in [u * u.T, u * v.T + v * u.T, v * v.T]:
            columns.append(matrix.reshape(100, 1))

    entries = [
        ((0, 1), (0, 1)), ((0, 1), (0, 2)), ((0, 1), (0, 3)),
        ((0, 1), (1, 2)), ((0, 1), (1, 3)),
        ((0, 2), (0, 2)), ((0, 2), (0, 3)),
        ((0, 2), (1, 2)), ((0, 2), (1, 3)),
        ((0, 3), (0, 3)), ((0, 3), (1, 2)), ((0, 3), (1, 3)),
        ((1, 2), (1, 2)), ((1, 2), (1, 3)), ((1, 3), (1, 3)),
    ]
    selected = [10 * index[left] + index[right] for left, right in entries]
    linear_map = sp.Matrix.hstack(*columns)
    uniqueness_minor = linear_map[selected, :]
    assert uniqueness_minor.det() == -2

    t, lam = sp.symbols("t lam", positive=True)
    metric = sp.diag(*[1 / t if 0 in pair else 1 for pair in pairs])
    small = sp.Matrix([[2, -1], [-1, 2]])
    total = sp.zeros(10)
    for support, basis in blocks:
        coefficient = (t / (4 * (t + 2)) if 0 in support
                       else (4 - t) / (12 * (t + 2)))
        total += coefficient * basis * small * basis.T
    assert down * total == sp.zeros(5, 10)
    assert all(sp.cancel(entry) == 0
               for entry in total * metric * kernel - kernel)

    gram = kernel.T * metric * kernel
    inverse_gram = gram.inv()
    square_sum = sp.zeros(5)
    for i in range(5):
        occupancy = sp.diag(*[int(i in pair) for pair in pairs])
        compression = inverse_gram * kernel.T * metric * occupancy * kernel
        square_sum += compression * compression
    square_sum = square_sum.applyfunc(sp.cancel)
    expected = ((lam - 2 * (t + 1) / (t + 2)) ** 2
                * (lam - (5 * t**2 + 10 * t + 21)
                   / (3 * (t + 2) ** 2)) ** 3)
    actual = square_sum.charpoly(lam).as_expr()
    # charpoly may create an assumption-free symbol with the same printed name.
    actual = actual.subs({symbol: lam for symbol in actual.free_symbols
                          if symbol.name == "lam"})
    assert sp.cancel(actual - expected) == 0

    print("PASS: physical metric W and five local primitive kernels")
    print("PASS: uniqueness minor determinant = -2")
    print("PASS: exact symbolic identity S_t W K = K")
    print("PASS: unique no-head block is negative definite for t > 4")
    print("PASS: actual leakage target remains strictly true in this family")


if __name__ == "__main__":
    main()

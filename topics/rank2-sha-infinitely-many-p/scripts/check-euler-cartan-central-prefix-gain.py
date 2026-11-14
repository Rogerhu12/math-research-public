#!/usr/bin/env python3
"""Finite exact checks of R175 on the actual saturated source.

The series and prefix matrix are the original rational P,Q,W of R162.
Only six fixed (p,D) pairs are used.  No Cartan formula constructs a
series coefficient or a kernel vector; the derived congruence is tested
after integral least-valuation column elimination.
"""
import importlib.util
import json
from math import comb
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series


path = Path(__file__).with_name("check-theta-plane-saturated-jets.py")
spec = importlib.util.spec_from_file_location("actual_plane", path)
plane = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plane)


def reduction(value, prime):
    denominator = int(value.denominator) % prime
    assert denominator, (prime, value)
    return int(value.numerator) % prime * pow(denominator, -1, prime) % prime


def check(prime, degree):
    r = (prime + 1) // 4
    assert 1 <= degree < prime
    k = r * degree
    columns, matrix = plane.actual_rows(degree)
    assert k < len(matrix)
    cap = ctx.cap
    s = Series([0, 1], prec=cap)
    period = Series([fmpq(comb(2*n, n), 4**n * (4*n+1))
                     for n in range(cap)], prec=cap)
    inverse = (s * period**4).reversion()

    # Only the degree-one columns contribute to H_1.
    central = []
    for index, (j, c) in enumerate(columns):
        if j == 1:
            actual = Series([row[index] for row in matrix], prec=cap)
            central.append(actual(inverse)[r])
        else:
            central.append(fmpq(0))

    derivative_coefficient = fmpq(1, 3)
    for n in range(1, r):
        derivative_coefficient *= fmpq(4*n+1, 4*n+3)
    tau = reduction(prime * derivative_coefficient / r, prime)
    assert tau

    remaining = list(range(len(columns)))
    for n in range(k):
        if not remaining:
            break
        pivot = min(remaining, key=lambda col: plane.vp(matrix[n][col], prime))
        if not matrix[n][pivot]:
            continue
        remaining.remove(pivot)
        ratios = {col: matrix[n][col] / matrix[n][pivot]
                  for col in remaining if matrix[n][col]}
        assert all(plane.vp(value, prime) >= 0 for value in ratios.values())
        for row in matrix[n+1:]:
            value = row[pivot]
            for col, ratio in ratios.items():
                row[col] -= value * ratio
        value = central[pivot]
        for col, ratio in ratios.items():
            central[col] -= value * ratio

    assert remaining  # Each chosen example has an actual nonzero prefix kernel.
    factor = pow(-17*tau, degree-1, prime)
    for col in remaining:
        lhs = reduction(prime**(degree-1) * matrix[k][col], prime)
        rhs = factor * reduction(central[col], prime) % prime
        assert lhs == rhs, (prime, degree, col, lhs, rhs)
    print(json.dumps({
        "p": prime, "D": degree, "k": k,
        "kernel_rank": len(remaining),
        "jet_valuation": min(plane.vp(matrix[k][col], prime) for col in remaining),
        "verified": True
    }), flush=True)


if __name__ == "__main__":
    for pair in ((7, 1), (7, 2), (7, 4), (7, 6), (11, 3), (11, 4)):
        check(*pair)

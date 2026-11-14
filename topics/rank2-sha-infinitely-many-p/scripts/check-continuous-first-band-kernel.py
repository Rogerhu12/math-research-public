#!/usr/bin/env python3
"""R196: two fixed complete-prefix checks on the actual rational theta plane."""

import importlib.util
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


def row_space(rows, prime):
    a = [[int(x) % prime for x in row] for row in rows]
    if not a:
        return []
    rank, width = 0, len(a[0])
    for col in range(width):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, prime)
        a[rank] = [x * inverse % prime for x in a[rank]]
        for i in range(len(a)):
            if i != rank:
                value = a[i][col]
                a[i] = [(x - value * y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return a[:rank]


def main():
    prime, degree = 19, 5
    r = (prime + 1) // 4
    columns, source_rows = plane.actual_rows(degree)
    cap = ctx.cap
    s = Series([0, 1], prec=cap)
    period = Series([fmpq(comb(2*n, n), 4**n * (4*n+1))
                     for n in range(cap)], prec=cap)
    s_of_w = (s * period**4).reversion()
    actual_columns = [Series([row[c] for row in source_rows], prec=cap)(s_of_w)
                      for c in range(len(columns))]
    rows = [[value[k] for value in actual_columns] for k in range(cap)]
    first = actual_columns[columns.index((1, 0))]
    difference = actual_columns[columns.index((1, 1))]
    assert first[1] == 1 and difference[2] == -22

    # Only phi below A^r is used.  There the true curve and the U=0 axis agree.
    phi = difference(first.reversion())
    phi = Series([phi[n] if n < r else fmpq(0) for n in range(cap)], prec=cap)
    assert phi[2] == -22
    parameter = Series([0, 1], prec=cap)
    powers = [Series([1], prec=cap)]
    for _ in range(degree):
        powers.append(powers[-1] * phi)

    graph_hasse = {}
    for j in range(degree + 1):
        graph_hasse[j] = [comb(c, j) * parameter**(m-c) * powers[c-j]
                          if c >= j else Series([0], prec=cap)
                          for m, c in columns]

    derivative = fmpq(1, 3)
    for n in range(1, r):
        derivative *= fmpq(4*n+1, 4*n+3)
    tau = reduction(prime * derivative / r, prime)
    assert tau

    for q, angular in ((1, 4), (3, 0)):
        k = r*q + angular
        assert q <= prime-2 and k < r*(prime-1)+1
        normalized = [[reduction(prime**(n//r) * x, prime) for x in rows[n]]
                      for n in range(k)]
        graph_rows = []
        for j in range(q + 1):
            bound = max((r if j < q else angular) - 2*j, 0)
            for n in range(bound):
                graph_rows.append([reduction(value[n], prime)
                                   for value in graph_hasse[j]])
        actual_space = row_space(normalized, prime)
        graph_space = row_space(graph_rows, prime)
        assert actual_space == graph_space

        if angular >= 2*q:
            hasse_row = [value[angular-2*q] for value in graph_hasse[q]]
        else:
            hasse_row = [fmpq(0)] * len(columns)
        factor = pow(-17*(-22)*tau, q, prime)
        discrepancy = [(reduction(prime**q * x, prime)
                        - factor * reduction(y, prime)) % prime
                       for x, y in zip(rows[k], hasse_row)]
        assert row_space(normalized + [discrepancy], prime) == actual_space

        # Independent exact p-saturated elimination of the complete raw prefix.
        matrix = [row[:] for row in rows[:k+1]]
        expected = hasse_row[:]
        remaining = list(range(len(columns)))
        for n in range(k):
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
            value = expected[pivot]
            for col, ratio in ratios.items():
                expected[col] -= value * ratio
        assert remaining
        for col in remaining:
            assert reduction(prime**q * matrix[k][col], prime) == (
                factor * reduction(expected[col], prime) % prime)

        if q >= (r+1)//2:
            low = [index for index, (m, c) in enumerate(columns) if m+c < r]
            identity_rows = [[int(i == index) for i in range(len(columns))]
                             for index in low]
            assert row_space(normalized, prime) == row_space(identity_rows, prime)
            assert len(actual_space) == len(low)

        valuation = min(plane.vp(matrix[k][col], prime) for col in remaining)
        print({"p": prime, "D": degree, "q": q, "s": angular, "k": k,
               "normalized_mod_p_rank": len(actual_space),
               "exact_prefix_kernel_rank": len(remaining),
               "actual_next_valuation": valuation, "verified": True})


if __name__ == "__main__":
    main()

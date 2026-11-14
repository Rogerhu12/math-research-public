#!/usr/bin/env python3
"""R198: one exact complete matrix, p=23, D=7, k=30; no prime scan."""

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
    assert denominator, value
    return int(value.numerator) % prime * pow(denominator, -1, prime) % prime


def rank_mod(rows, prime):
    matrix = [[reduction(value, prime) for value in row] for row in rows]
    rank = 0
    for col in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][col], -1, prime)
        matrix[rank] = [value * inverse % prime for value in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank:
                multiple = matrix[i][col]
                matrix[i] = [(x - multiple*y) % prime
                             for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def main():
    prime, degree, r, k = 23, 7, 6, 30
    columns, s_rows = plane.actual_rows(degree)
    cap = ctx.cap
    parameter = Series([0, 1], prec=cap)
    period = Series([fmpq(comb(2*n, n), 4**n*(4*n+1))
                     for n in range(cap)], prec=cap)
    s_of_w = (parameter * period**4).reversion()
    values = [Series([row[col] for row in s_rows], prec=cap)(s_of_w)
              for col in range(len(columns))]
    raw = [[value[n] for value in values] for n in range(k)]
    normalized = [[prime**(n//r) * value for value in raw[n]] for n in range(k)]
    high = [index for index, (m, c) in enumerate(columns) if m+c >= r]
    divided = [[value/prime if col in high else value
                for col, value in enumerate(row)] for row in normalized]

    assert len(columns) == 36 and len(high) == 24
    rank_zero = rank_mod(normalized, prime)
    rank_one = rank_mod(divided, prime)
    assert rank_zero == 12 and rank_one == 30
    # Rank 30 of the divided matrix also certifies rational independence
    # of all thirty original rows.  The two ranks prove SNF 0^12,1^18.
    smith = [0]*rank_zero + [1]*(rank_one-rank_zero)
    assert len(smith) == k

    # Exact saturated original-prefix flags: only integral column operations.
    pivots, remaining = plane.saturated_orders(raw, prime)
    assert [n for n, _ in pivots] == list(range(k))
    valuations = [value for _, value in pivots]
    assert valuations == [0]*8 + [-1]*8 + [-2]*8 + [-3]*6
    assert len(remaining) == 6
    scaling_sum = sum(n//r for n in range(k))
    assert scaling_sum == 60 and sum(smith) == 18
    assert sum(valuations) == sum(smith)-scaling_sum == -42
    assert len(high) == (36-30) + (30-rank_zero)

    print({"p": prime, "D": degree, "rows": k, "source_rank": len(columns),
           "rank_J_mod_p": rank_zero, "rank_first_saturation_mod_p": rank_one,
           "normalized_smith": smith,
           "actual_prefix_valuations": valuations,
           "source_index": len(high), "image_index": sum(smith),
           "kernel_index": len(remaining), "sum_actual": sum(valuations),
           "verified": True})


if __name__ == "__main__":
    main()

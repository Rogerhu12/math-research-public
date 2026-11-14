#!/usr/bin/env python3
"""Exact saturated jets for the actual plane (A_2,B), in ordinary coefficients.

Uses the fixed P,Q,W of R162 and the integral source basis A_2^j V^c,
0 <= c <= j <= D.  The output parameter s=u^4 starts with z^4 with
coefficient one, so its exact prefix flags and leading jet norms agree
with those of the original curve.  No central vanishing is assumed.

Requires python-flint.  With no arguments, recomputes exactly the finite
D=4,D=8 records in the adjacent JSON.  --degree restricts to one of them.
The data are finite diagnostics, not a uniform arithmeticity theorem.
"""

import argparse
import json
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series


DATA = Path(__file__).with_suffix('.json')


def vp_integer(value: int, prime: int) -> int:
    """Only called with nonzero value."""
    order = 0
    while value % prime == 0:
        value //= prime
        order += 1
    return order


def vp(value, prime: int) -> int:
    if not value:
        return 10**9
    return (vp_integer(int(value.numerator), prime)
            - vp_integer(int(value.denominator), prime))


def actual_rows(degree: int):
    dimension = (degree + 1) * (degree + 2) // 2
    stop = dimension + 10
    ctx.cap = stop + 1
    s = Series([0, 1], prec=stop + 1)
    h1 = 1 + 4*s + 70*s**2 + 4*s**3 + s**4
    h2 = 1 + 20*s - 26*s**2 + 20*s**3 + s**4
    q8 = (1 + 364*s**2 - 1088*s**3 + 1190*s**4
          - 1088*s**5 + 364*s**6 + s**8)
    polynomial = (s*(1-s)**2*(1+s)*(1-2*s+5*s**2)
                  *(5-2*s+s**2)*h1*h2 / 5)
    ratio = (1+s)*q8 / ((1-s)*h1*h2) - 1
    logarithm = [fmpq(0)] * (stop + 1)
    derivative_coefficient = fmpq(17, 3)
    for m in range(1, stop + 1):
        logarithm[m] = derivative_coefficient / m
        derivative_coefficient *= fmpq(4*m + 1, 4*m + 3)
    first = polynomial * Series(logarithm, prec=stop + 1).exp()
    assert first[1] == 1 and first[2] == fmpq(394, 15)
    assert ratio[1] == -22
    first_powers = [Series([1], prec=stop + 1)]
    ratio_powers = [Series([1], prec=stop + 1)]
    for _ in range(degree):
        first_powers.append(first_powers[-1] * first)
        ratio_powers.append(ratio_powers[-1] * ratio)
    columns = [(j, c) for j in range(degree + 1) for c in range(j + 1)]
    values = [first_powers[j] * ratio_powers[c] for j, c in columns]
    matrix = [[column[k] for column in values] for k in range(stop + 1)]
    return columns, matrix


def saturated_orders(rows, prime: int):
    """Return (jet order, valuation) at every actual rank increase.

    Choose a least-valuation pivot in the current kernel coordinates.
    The ratios r_l/r_p are p-integral, so replacing column l by
    column l - (r_l/r_p) column p is a GL(Z_p) change.  Its other
    columns form the exact saturated kernel of the current row.
    Apply this change to every later row, then drop the pivot column.
    Thus the recorded minimum valuation is the original jet's value
    ideal on its actual saturated prefix kernel.  There is no row scaling.
    """
    matrix = [row[:] for row in rows]
    remaining = list(range(len(matrix[0])))
    answer = []
    for k, row in enumerate(matrix):
        if not remaining:
            break
        pivot = min(remaining, key=lambda column: vp(row[column], prime))
        order = vp(row[pivot], prime)
        if order == 10**9:
            continue
        answer.append((k, order))
        remaining.remove(pivot)
        ratios = {column: row[column]/row[pivot]
                  for column in remaining if row[column]}
        assert all(vp(ratio, prime) >= 0 for ratio in ratios.values())
        for later in matrix[k+1:]:
            if not later[pivot]:
                continue
            value = later[pivot]
            for column, ratio in ratios.items():
                later[column] -= value * ratio
    return answer, remaining


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--degree', type=int, choices=[4, 8])
    args = parser.parse_args()
    records = json.loads(DATA.read_text())
    if args.degree is not None:
        records = [record for record in records if record['D'] == args.degree]
    previous_degree, rows = None, None
    for record in records:
        degree, prime = record['D'], record['p']
        if degree != previous_degree:
            columns, rows = actual_rows(degree)
            previous_degree = degree
        answer, remaining = saturated_orders(rows, prime)
        assert not remaining
        assert [k for k, _ in answer] == list(range(record['rows']))
        valuations = [order for _, order in answer]
        assert valuations == record['v']
        assert sum(valuations) == record['sum_v']
        print(json.dumps({'D': degree, 'p': prime, 'dimension': len(columns),
                          'valuations': valuations, 'sum_v': sum(valuations),
                          'verified': True}, separators=(',', ':')), flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""R199: complete divided images from only the actual short axis jets.

Uses the already fixed R198 case p=23,D=7,k=30, not a prime scan.
The high-degree raw matrix and the short-input mod-p formula are compared
entry by entry; no unknown central derivative is supplied.
"""

import importlib.util
from math import comb, factorial
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series


def load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


plane = load("actual_plane", "check-theta-plane-saturated-jets.py")
joint = load("joint_image", "check-joint-prefix-saturation.py")


def mod(value, prime):
    return joint.reduction(value, prime)


def main():
    prime, degree, r, k = 23, 7, 6, 30
    columns, s_rows = plane.actual_rows(degree)
    cap = ctx.cap
    parameter = Series([0, 1], prec=cap)
    period = Series([fmpq(comb(2*n, n), 4**n*(4*n+1))
                     for n in range(cap)], prec=cap)
    s_of_w = (parameter * period**4).reversion()
    actual = [Series([row[col] for row in s_rows], prec=cap)(s_of_w)
              for col in range(len(columns))]
    first = actual[columns.index((1, 0))]
    difference = actual[columns.index((1, 1))]
    assert first[1] == 1 and difference[2] == -22

    # These are precisely the original jets identified with the axis by
    # R199 (20).  No original coefficient above r+1 is used by the formula.
    f_short = Series([first[n] if n <= r else fmpq(0)
                      for n in range(cap)], prec=cap)
    c_short = Series([difference[n] if n <= r+1 else fmpq(0)
                      for n in range(cap)], prec=cap)
    assert all(plane.vp(first[n], prime) >= 0 for n in range(r+1))
    assert all(plane.vp(difference[n], prime) >= 0 for n in range(r+2))
    f_powers = [Series([1], prec=cap)]
    c_powers = [Series([1], prec=cap)]
    for _ in range(degree):
        f_powers.append(f_powers[-1]*f_short)
        c_powers.append(c_powers[-1]*c_short)
    axis_columns = [f_powers[m-c]*c_powers[c] for m, c in columns]

    # The only pole in the s-logarithm through degree r is its r-th
    # coefficient; composition and exponentiation add integral terms.
    derivative = fmpq(1, 3)
    for n in range(1, r):
        derivative *= fmpq(4*n+1, 4*n+3)
    tau = mod(prime*derivative/r, prime)
    assert tau
    radial_unit = 17*tau % prime

    raw = [[value[n] for value in actual] for n in range(k)]
    normalized = [[prime**(n//r)*value for value in raw[n]]
                  for n in range(k)]
    checked = 0
    ranks = {}
    for label, divisions in (
            ("first_saturation", [int(m+c >= r) for m, c in columns]),
            ("canonical_diagonal", [(m+c)//r for m, c in columns])):
        actual_divided = [[value/prime**divisions[col]
                           for col, value in enumerate(row)]
                          for row in normalized]
        short_matrix = []
        for n in range(k):
            h, angular = divmod(n, r)
            row = []
            for col, (m, c) in enumerate(columns):
                t = divisions[col]
                if h < t:
                    predicted = 0
                else:
                    power = h-t
                    predicted = (
                        pow(radial_unit*m, power, prime)
                        * pow(factorial(power), -1, prime)
                        * mod(axis_columns[col][angular+r*t], prime)
                    ) % prime
                assert predicted == mod(actual_divided[n][col], prime), (
                    label, n, (m, c), t, predicted,
                    mod(actual_divided[n][col], prime))
                row.append(fmpq(predicted))
                checked += 1
            short_matrix.append(row)
        ranks[label] = joint.rank_mod(short_matrix, prime)
        assert ranks[label] == 30
    assert checked == 2*k*len(columns)
    print({"p": prime, "D": degree, "rows": k, "columns": len(columns),
           "max_original_short_jet": r+1,
           "tau_mod_p": tau, "entries_checked": checked,
           "short_matrix_ranks": ranks, "verified": True})


if __name__ == "__main__":
    main()

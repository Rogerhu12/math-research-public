#!/usr/bin/env python3
"""Exact rational certificate; no floating point, external packages, or sampling.

The target is the auxiliary arithmetic inequality, not strengthened S1.
Run from any directory; stdout is a small JSON certificate.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, prod
import hashlib
import json
from pathlib import Path


CORE = tuple(range(2, 10))
PAIRS = tuple(combinations(CORE, 2))
U = (
    73, 233, 431, 632, 1101, -1439, -1031,
    -341, -572, -796, -1361, 1736, 1261,
    -825, -1055, -1748, 2144, 1592,
    -1229, -2023, 2369, 1849,
    -2520, 2629, 2339,
    2561, 3990,
    -10000,
)
TRIAL_CORE = (-6226873, 3524959, 34809, -6327741, -22311254,
              -74665443, 173824267, 194042655)
TRIAL_TAIL = 2546340
GRID = 10**40
DISPLAY_GRID = 10**20
TAIL_END = 200


def floor_fraction(x):
    return x.numerator // x.denominator


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


def elementary_core():
    e = [F(1)] + [F(0)] * 4
    for i in CORE:
        for k in range(4, 0, -1):
            e[k] += F(1, i**4) * e[k - 1]
    return e


def enclose_tail():
    # Directed rounding for e_0,...,e_4 of coordinates 10,...,200.
    lo = [GRID, 0, 0, 0, 0]
    hi = lo.copy()
    for i in range(10, TAIL_END + 1):
        den = i**4
        for k in range(4, 0, -1):
            lo[k] += lo[k - 1] // den
            hi[k] += (hi[k - 1] + den - 1) // den
    lower = [F(x, GRID) for x in lo]
    finite_upper = [F(x, GRID) for x in hi]
    # sum_{i>200} i^-4 <= integral_200^infinity x^-4 dx.
    mass_upper = F(1, 3 * TAIL_END**3)
    upper = []
    for k in range(5):
        value = sum((finite_upper[k - j] * mass_upper**j / factorial(j)
                     for j in range(k + 1)), F(0))
        upper.append(F(ceil_fraction(value * GRID), GRID))
    return lower, upper


def solve_spd_ldl(matrix, rhs):
    # Complete rational LDL; every pivot is checked strictly positive.
    n = len(rhs)
    low = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    diag = []
    for i in range(n):
        for j in range(i):
            low[i][j] = (matrix[i][j] - sum(
                (low[i][t] * diag[t] * low[j][t] for t in range(j)), F(0))) / diag[j]
        pivot = matrix[i][i] - sum(
            (low[i][t]**2 * diag[t] for t in range(i)), F(0))
        assert pivot > 0
        diag.append(pivot)
    forward = []
    for i in range(n):
        forward.append(rhs[i] - sum(
            (low[i][j] * forward[j] for j in range(i)), F(0)))
    scaled = [forward[i] / diag[i] for i in range(n)]
    result = [F(0)] * n
    for i in range(n - 1, -1, -1):
        result[i] = scaled[i] - sum(
            (low[j][i] * result[j] for j in range(i + 1, n)), F(0))
    assert all(sum((matrix[i][j] * result[j] for j in range(n)), F(0)) == rhs[i]
               for i in range(n))
    return result, diag


def main():
    u = dict(zip(PAIRS, U))
    assert len(u) == 28
    assert all(sum(value for pair, value in u.items() if i in pair) == 0 for i in CORE)
    physical = {pair: value * pair[0]**2 * pair[1]**2 for pair, value in u.items()}
    coeff = {pair: value * pair[0]**4 * pair[1]**4 for pair, value in u.items()}
    norm = sum(x * x for x in physical.values())
    core_index = {i: j for j, i in enumerate(CORE)}
    trial = dict(zip(CORE, TRIAL_CORE))

    def weight(subset):
        return prod((F(1, i**4) for i in subset), start=F(1))

    def phi(subset):
        return sum(coeff[pair] for pair in combinations(subset, 2))

    tail_lo, tail_hi = enclose_tail()
    core_e = elementary_core()
    total_lo = [sum((core_e[k - j] * tail_lo[j] for j in range(k + 1)), F(0))
                for k in range(5)]
    total_hi = [sum((core_e[k - j] * tail_hi[j] for j in range(k + 1)), F(0))
                for k in range(5)]

    # Legal full infinite three-slice fit: eight core coefficients and one
    # constant coefficient on every tail coordinate, not a truncated inverse.
    c1_upper = F(0)
    for h in range(4):
        for subset in combinations(CORE, h):
            value = phi(subset) - sum(trial[i] for i in subset) - TRIAL_TAIL * (3 - h)
            c1_upper += weight(subset) * tail_hi[3 - h] * value**2

    # Complete finite four-slice nuisance: all eight linear features.
    # The constant is included because sum_i x_i=4 on this slice.
    gram = [[F(0) for _ in CORE] for _ in CORE]
    rhs = [F(0) for _ in CORE]
    square = F(0)
    for subset in combinations(CORE, 4):
        wt, value = weight(subset), phi(subset)
        square += wt * value**2
        for i in subset:
            ii = core_index[i]
            rhs[ii] += wt * value
            for j in subset:
                gram[ii][core_index[j]] += wt
    fitted, pivots = solve_spd_ldl(gram, rhs)
    c2_finite = square - sum((rhs[i] * fitted[i] for i in range(8)), F(0))
    residual_square = sum((weight(subset) * (
        phi(subset) - sum(fitted[core_index[i]] for i in subset))**2
        for subset in combinations(CORE, 4)), F(0))
    assert c2_finite == residual_square and c2_finite > 0

    # Compact, weaker rational enclosures used in the written proof.
    e2_num = floor_fraction(total_lo[2] * DISPLAY_GRID)
    e3_num = ceil_fraction(total_hi[3] * DISPLAY_GRID)
    e4_num = floor_fraction(total_lo[4] * DISPLAY_GRID)
    c1_int = ceil_fraction(c1_upper)
    c2_int = floor_fraction(c2_finite)
    left_num = e4_num * norm + e2_num * c2_int
    base_num = e3_num * c1_int
    margin_two_num = left_num - 2 * base_num
    margin_289_num = 100 * left_num - 289 * base_num
    assert margin_two_num > 0 and margin_289_num > 0
    output = {
        "status": "all_exact_rational_checks_passed",
        "target": "auxiliary_arithmetic_inequality_not_strengthened_s1",
        "original_tail": {"indices": "j>=2", "b_j": "j^-2", "s": 2, "n": 1},
        "source_core": list(CORE), "u_lexicographic_upper_triangle": list(U),
        "trial_core": list(TRIAL_CORE), "trial_constant_on_j_ge_10": TRIAL_TAIL,
        "norm_f_squared": norm,
        "tail_endpoint": TAIL_END, "tail_grid": GRID,
        "display_denominator": DISPLAY_GRID,
        "e2_lower_numerator": e2_num,
        "e3_upper_numerator": e3_num,
        "e4_lower_numerator": e4_num,
        "C1_trial_upper_integer": c1_int,
        "C2_full_finite_regression_lower_integer": c2_int,
        "full_finite_nuisance_dimension": 8,
        "positive_LDL_pivots": len(pivots),
        "primitive_row_checks": 8,
        "normal_equations_exact": True,
        "residual_square_exact": True,
        "margin_over_2_numerator_at_display_denominator": margin_two_num,
        "margin_over_289_100_numerator_at_100_display_denominator": margin_289_num,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

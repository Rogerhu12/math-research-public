#!/usr/bin/env python3
"""Exact one-parameter Boolean obstruction to coefficientwise pencil positivity.
No floating point spectra or sampled parameter search.
"""
import argparse
import itertools
import json
import time
from pathlib import Path

import sympy as sp


def simplify_matrix(mat):
    return mat.applyfunc(sp.cancel)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    start = time.monotonic()
    r = sp.symbols("r", positive=True)
    b = sp.Matrix([r, 1 / r, 1, 1])
    z = [x**2 for x in b]
    e2 = sum(z[i] * z[j] for i, j in itertools.combinations(range(4), 2))
    source = sp.Matrix(
        [[1, 0], [0, 1], [-r / 2, -1 / (2 * r)], [-r / 2, -1 / (2 * r)]]
    )
    metric = source.T * source
    metric_inv = simplify_matrix(metric.inv())
    full_first = sp.diag(*[sum(z) - 2 * q for q in z]) + b * b.T
    gram1 = simplify_matrix(source.T * full_first.inv() * source)
    gram2 = simplify_matrix(source.T * sp.diag(*[q**2 for q in z]) * source)
    g = simplify_matrix(metric_inv * gram1)
    ell = simplify_matrix(metric_inv * gram2)
    gi = simplify_matrix(g.inv())
    dual_row = b.applyfunc(lambda q: 1 / q).T * source
    cubic_row = b.applyfunc(lambda q: q**3).T * source
    bridge = simplify_matrix(metric_inv * cubic_row.T / e2)
    h0 = simplify_matrix(2 * g + bridge * dual_row)
    upper_bridge_square = simplify_matrix(gi * ell - 4 * g - bridge * dual_row)
    jordan_form = simplify_matrix(metric * (gi * ell + ell * gi))
    required_form = simplify_matrix(
        metric * upper_bridge_square
        + metric * h0 * gi * metric_inv * h0.T * metric
    )
    numerator = (
        2 * r**18 + r**16 + 14 * r**14 + 63 * r**12 + 160 * r**10
        + 179 * r**8 + 138 * r**6 + 73 * r**4 + 14 * r**2 + 4
    )
    positive8 = r**8 + 4 * r**6 + 8 * r**4 + 4 * r**2 + 1
    positive4 = r**4 + r**2 + 1
    expected_j = positive8 / positive4
    expected_n = numerator / (8 * positive4**3)
    assert sp.cancel(jordan_form[0, 0] - expected_j) == 0
    assert sp.cancel(required_form[0, 0] - expected_n) == 0
    ratio = sp.cancel(expected_n / expected_j)
    assert sp.limit(ratio / r**2, r, sp.oo) == sp.Rational(1, 4)
    assert b.T * source == sp.zeros(1, 2)

    subs = {r: sp.Integer(3)}
    hg = metric.subs(subs)
    gf = gram1.subs(subs)
    h = h0.subs(subs)
    v = sp.Matrix([1, 0])
    x = gf.inv() * h.T * hg * v
    assert list(x) == [sp.Rational(9330, 8281), sp.Rational(274752, 8281)]
    block = sp.Matrix(
        sp.BlockMatrix([
            [gf, -h.T * hg],
            [-hg * h, (jordan_form - metric * upper_bridge_square).subs(subs)],
        ]).as_explicit()
    )
    direction = x.col_join(v)
    value = sp.cancel((direction.T * block * direction)[0])
    assert value == -sp.Rational(31980847, 753571)
    assert block == block.T
    result = {
        "status": "all_passed",
        "scope": "coefficientwise positivity only; complete hard fee is not refuted",
        "old_weights": ["r", "1/r", "1", "1"],
        "parameter_domain": "r > 0",
        "exact_jordan_entry": str(sp.factor(expected_j)),
        "exact_required_entry": str(sp.factor(expected_n)),
        "necessary_kappa": str(sp.factor(ratio)),
        "limit_necessary_kappa_over_r_squared": "1/4",
        "r3_negative_coordinates_in_E3_blocks": [str(vv) for vv in direction] + ["0"],
        "r3_negative_value": str(value),
        "sympy_version": sp.__version__,
        "elapsed_seconds": round(time.monotonic() - start, 6),
    }
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()

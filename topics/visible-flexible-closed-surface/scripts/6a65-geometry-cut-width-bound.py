#!/usr/bin/env python3
"""Exact rational comparisons for the R205 cut-tangent width bound.

Only the finite rational arithmetic of the stated analytic inequalities is
evaluated.  This is not a numerical surface, metric, or reach certificate.
No external packages or raw state files are required.
"""

from fractions import Fraction as F
import json


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            out[j + k] += x * y
    return out


S = list(map(F, [0, 0, 0, 0, 0, 126, -420, 540, -315, 70]))
powers = [[F(1)]]
for _ in range(6):
    powers.append(multiply(powers[-1], S))
moments = {n: sum((x / (j + 1) for j, x in enumerate(powers[n])), F(0))
           for n in (2, 4, 6)}
assert moments[2] == F(38251, 92378)
assert moments[4] == F(376009639, 1094020070)


def bounds(A, R):
    """Rational lower/upper bounds for C_A(4/5)+R*(1-sin A)."""
    A, R = F(A), F(R)
    if not 0 <= A <= F(6, 5) or not R > 0:
        raise ValueError("Need 0 <= A <= 6/5 and R > 0")
    c4 = F(4, 5) - F(23, 50)*moments[2]*A**2/2 + F(23, 50)*moments[4]*A**4/24
    c6 = c4 - F(23, 50)*moments[6]*A**6/720
    s5 = A - A**3/6 + A**5/120
    s7 = s5 - A**7/5040
    return c6 + R*(1-s5), c4 + R*(1-s7)


def rational(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator),
            "decimal_for_display_only": float(q)}


def threshold_comparison(name, R, W, lo, hi):
    R, W, lo, hi = map(F, (R, W, lo, hi))
    lower_at_lo = bounds(lo, R)[0]
    upper_at_hi = bounds(hi, R)[1]
    assert lower_at_lo > W
    assert upper_at_hi < W
    return {"name": name, "R": rational(R), "W": rational(W),
            "threshold_strictly_between": [rational(lo), rational(hi)],
            "lower_at_lo_minus_W": rational(lower_at_lo-W),
            "W_minus_upper_at_hi": rational(W-upper_at_hi)}


def main():
    rows = [threshold_comparison("R204 final width", "0.097", "0.85", "0.3637", "0.3638"),
            threshold_comparison("Current finite guide", F(2, 19), "0.84", "0.4525", "0.4527"),
            threshold_comparison("Final reach with guide width", "0.097", "0.84", "0.4250", "0.4252"),
            threshold_comparison("Guide curvature with final width", F(2, 19), "0.85", "0.3952", "0.3955")]
    coarse = []
    for A, R, W in [(F(9, 25), F(97, 1000), F(17, 20)),
                    (F(9, 20), F(2, 19), F(21, 25))]:
        value = bounds(A, R)[0] - W
        assert value > 0
        coarse.append({"A": rational(A), "R": rational(R), "W": rational(W),
                       "strict_lower_margin": rational(value)})
    print(json.dumps({"schema": "6a65-R205-cut-width-exact-rational-comparisons-v1",
                      "moments": {str(n): rational(q) for n, q in moments.items()},
                      "thresholds": rows, "coarse_comparisons": coarse,
                      "all_assertions_passed": True,
                      "uses_exact_warped_metric_and_meridian_curvature_hypotheses": True,
                      "approximate_metric_fields_not_certified": True}, indent=2))


if __name__ == "__main__":
    main()


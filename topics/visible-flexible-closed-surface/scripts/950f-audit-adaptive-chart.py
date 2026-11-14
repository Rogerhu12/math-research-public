#!/usr/bin/env python3
"""Exact global invertibility bound for the frozen clamped-spline angle chart.

Input binary64 knot/value data are interpreted as exact rational numbers.
The theorem concerns the exact clamped cubic spline with those data; floating
evaluation roundoff and the numerical surface remain separate obligations.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def ratio(v: Q) -> dict:
    return {"numerator": str(v.numerator), "denominator": str(v.denominator),
            "decimal_diagnostic": float(v)}


def run(chart_path: Path, root: Path) -> dict:
    chart = json.loads(chart_path.read_text())
    x = [Q.from_float(float(v)) for v in chart["knots"]]
    y = [Q.from_float(float(v)) for v in chart["values"]]
    assert len(x) == len(y) >= 3 and x[0] == 0 and x[-1] == 1
    h = [b - a for a, b in zip(x, x[1:])]
    assert all(v > 0 for v in h)
    secants = [(b - a) / step for a, b, step in zip(y, y[1:], h)]
    d0, dn = Q(0), Q.from_float(float(chart["final_derivative"]))
    # Second derivatives solve the standard clamped-spline tridiagonal system.
    # At the maximum component its strictly positive row diagonal margin gives
    # ||h''||_infty <= max_i |rhs_i|/(diag_i-sum_j!=i |a_ij|).
    bounds = [6 * abs(secants[0] - d0) / h[0],
              6 * abs(dn - secants[-1]) / h[-1]]
    bounds += [6 * abs(secants[i] - secants[i - 1]) / (h[i] + h[i - 1])
               for i in range(1, len(secants))]
    second = max(bounds)
    # Green-function error from linear interpolation on each knot interval.
    height = max(map(abs, y)) + second * max(h) ** 2 / 8
    e0 = Q(16, 25)
    rho = 1 - e0 * height
    assert rho > Q(357, 1000) > Q(1, 3)
    # The cutoff c=1-S(4x-3) is in [0,1] and has zero first/second derivatives
    # at x=3/4,1, so multiplying a C2 spline preserves C2 regularity.
    checked = ["scripts/950f-prefix-adaptive-chart-bvp.py",
               "scripts/950f-prefix-warped-bvp.py",
               "scripts/950f-prefix-chart-twojet-check.py"]
    return {"status": "PASS: exact chart is C2 and globally orientation preserving",
            "chart_path": str(chart_path), "chart_sha256": hashlib.sha256(chart_path.read_bytes()).hexdigest(),
            "source_sha256": {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in checked},
            "interpretation": "Exact clamped C2 cubic spline through the recorded binary64 data, multiplied by the exact quintic cutoff; e0=16/25.",
            "spline_second_derivative_upper": ratio(second),
            "spline_abs_value_upper": ratio(height), "rho_global_lower": ratio(rho),
            "strict_rho_lower": "357/1000", "cut_chart_jets": "e=e_s=e_ss=0 exactly",
            "unpaid": ["floating spline coefficient error", "surface existence", "nonlinear tail matching", "global geometric bounds"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chart", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Refusing to overwrite an independent audit record")
    result = run(args.chart, args.root)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "rho": result["rho_global_lower"]["decimal_diagnostic"]}))

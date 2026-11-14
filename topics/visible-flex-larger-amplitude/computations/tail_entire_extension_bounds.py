#!/usr/bin/env python3
"""Exact rational bounds for R27's explicit star-shaped exterior extension.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.

This checks polynomial identities and conditional inequalities only. Input
trace/coordinate bounds must refer to actual Cartesian polar coordinates and
must be certified independently. The default box is illustrative; source ODE
coordinates are never silently identified with Cartesian coordinates.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path


BASES = [
    [F(1), F(0), F(0), F(-10), F(15), F(-6)],
    [F(0), F(1), F(0), F(-6), F(8), F(-3)],
    [F(0), F(0), F(1, 2), F(-3, 2), F(3, 2), F(-1, 2)],
]


def derivative(a):
    return [i * a[i] for i in range(1, len(a))] or [F(0)]


def value(a, x):
    result = F(0)
    for coefficient in reversed(a):
        result = result * x + coefficient
    return result


def bernstein(a):
    n = len(a) - 1
    return [
        sum((a[i] * F(comb(k, i), comb(n, i)) for i in range(k + 1)), F(0))
        for k in range(n + 1)
    ]


def encoded(x):
    return {"exact": str(x), "decimal": float(x)}


DEFAULT_BOX = {
    "scope": "Illustrative sufficient box, not measured Cartesian data.",
    "r_min": "29/100",
    "width": "1/10",
    "boundary_radius_derivative_bounds": ["1/1000", "1/100"],
    "mean_slope_interval": ["79/1000", "81/1000"],
    "mean_second_interval": ["-19/10", "-183/100"],
    "height_trace_bounds": ["13/100000", "27/100000", "58/100000"],
    "slope_trace_bounds": ["15/10000", "31/10000", "65/10000"],
    "second_trace_bounds": ["5/1000", "11/1000", "25/1000"],
    "inside_principal_curvature_bound": "33/4",
    "target_reach": "3/25",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--bounds", type=Path,
        help="Optional JSON in the documented rational box schema; its geometric validity is not checked.")
    args = parser.parse_args()
    box = json.loads(args.bounds.read_text()) if args.bounds else DEFAULT_BOX

    polynomial_rows = []
    beta = []
    for i, basis in enumerate(BASES):
        derivatives = []
        suprema = []
        current = basis
        for order in range(3):
            left, right = value(current, F(0)), value(current, F(1))
            assert left == (1 if order == i else 0)
            assert right == 0
            coefficients = bernstein(current)
            upper = max(map(abs, coefficients))
            suprema.append(upper)
            derivatives.append({
                "order": order,
                "power_coefficients": list(map(str, current)),
                "bernstein_coefficients": list(map(str, coefficients)),
                "supremum_bound": encoded(upper),
                "value_at_zero": str(left),
                "value_at_one": str(right),
            })
            current = derivative(current)
        beta.append(suprema)
        polynomial_rows.append({"basis": i, "derivatives": derivatives})
    assert beta == [
        [F(1), F(5), F(20)],
        [F(2, 5), F(2), F(12)],
        [F(1, 20), F(1, 4), F(2)],
    ]

    r = F(box["r_min"])
    length = F(box["width"])
    rho1, rho2 = map(F, box["boundary_radius_derivative_bounds"])
    slope_interval = list(map(F, box["mean_slope_interval"]))
    second_interval = list(map(F, box["mean_second_interval"]))
    U = list(map(F, box["height_trace_bounds"]))
    V = list(map(F, box["slope_trace_bounds"]))
    W = list(map(F, box["second_trace_bounds"]))
    assert r > 0 and length > 0
    assert len(U) == len(V) == len(W) == 3
    assert all(q >= 0 for q in [rho1, rho2, *U, *V, *W])
    assert slope_interval[0] <= slope_interval[1]
    assert second_interval[0] <= second_interval[1]
    c1 = max(map(abs, slope_interval))
    c2 = max(map(abs, second_interval))

    # General bounds for the cubic slope transition.
    mean_slope_bound = c1 + F(4, 27) * length * c2
    mean_second_bound = F(3, 2) * c1 / length + c2
    mean_bound_method = "general cubic Bernstein/elementary derivative bounds"
    ratio_interval = None
    # Optional sharper bound: c1>0, c2<0 and 3/2 <= -L*c2/c1 <= 3.
    if slope_interval[0] > 0 and second_interval[1] < 0:
        ratio_interval = [
            length * (-second_interval[1]) / slope_interval[1],
            length * (-second_interval[0]) / slope_interval[0],
        ]
        if F(3, 2) <= ratio_interval[0] <= ratio_interval[1] <= 3:
            mean_slope_bound = c1
            mean_second_bound = c2
            mean_bound_method = "monotone positive mean slope; ratio in [3/2,3]"

    # G(s,phi)=B(s)+u(phi)H0+L v(phi)H1+L^2 w(phi)H2.
    A = mean_second_bound + beta[0][2] * U[0] / length**2 + beta[1][2] * V[0] / length + beta[2][2] * W[0]
    B = mean_slope_bound + beta[0][1] * U[0] / length + beta[1][1] * V[0] + length * beta[2][1] * W[0]
    C = beta[0][0] * U[1] + length * beta[1][0] * V[1] + length**2 * beta[2][0] * W[1]
    D = beta[0][1] * U[1] / length + beta[1][1] * V[1] + length * beta[2][1] * W[1]
    E = beta[0][0] * U[2] + length * beta[1][0] * V[2] + length**2 * beta[2][0] * W[2]
    cross = (D + rho1 * A) / r + (C + rho1 * B) / r**2
    angular = (E + 2 * rho1 * D + rho1**2 * A + rho2 * B) / r**2 + B / r
    exterior_bound = max(A, angular) + cross
    assert exterior_bound >= 0

    inside_bound = F(box["inside_principal_curvature_bound"])
    target_reach = F(box["target_reach"])
    assert inside_bound > 0 and target_reach > 0
    total_bound = max(inside_bound, exterior_bound)
    reach_bound = 1 / total_bound
    report = {
        "scope": (
            "Exact rational verification of R27's polynomial identities and conditional "
            "exterior graph-Hessian/principal-curvature bounds. This neither verifies "
            "Cartesian boundary coordinates nor certifies the source ODE candidate."),
        "actual_cartesian_certificate": False,
        "input_is_default_illustrative_box": args.bounds is None,
        "input": box,
        "input_file": str(args.bounds) if args.bounds else None,
        "input_sha256": hashlib.sha256(args.bounds.read_bytes()).hexdigest() if args.bounds else None,
        "polynomial_checks": polynomial_rows,
        "mean_bound_method": mean_bound_method,
        "mean_ratio_interval": list(map(encoded, ratio_interval)) if ratio_interval else None,
        "bounds": {
            "G_ss": encoded(A), "G_s": encoded(B), "G_phi": encoded(C),
            "G_s_phi": encoded(D), "G_phi_phi": encoded(E),
            "euclidean_hessian_rr": encoded(A),
            "euclidean_hessian_cross": encoded(cross),
            "euclidean_hessian_angular": encoded(angular),
            "exterior_hessian_operator_and_principal_curvature": encoded(exterior_bound),
        },
        "exterior_bound_below_5_over_2": exterior_bound < F(5, 2),
        "conditional_whole_graph_curvature_bound": encoded(total_bound),
        "conditional_R25_reach_bound": encoded(reach_bound),
        "target_reach": encoded(target_reach),
        "conditional_reach_margin": encoded(reach_bound - target_reach),
        "target_covered_by_this_conditional_bound": reach_bound >= target_reach,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    with args.out.open("x") as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
    print(json.dumps({
        "out": str(args.out),
        "exterior_curvature_bound": report["bounds"]["exterior_hessian_operator_and_principal_curvature"],
        "conditional_reach": report["conditional_R25_reach_bound"],
        "conditional_reach_margin": report["conditional_reach_margin"],
        "actual_cartesian_certificate": False,
    }))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact R237 bounds for any accepted continuation of the scaled M96 core.

Use every output coefficient as an exact binary64 rational. The R236
reference is recomputed independently, rather than assuming that the latest
warm seed's angular density is still the original 32-mode density. This
certifies a finite planar core only; the continued surface is not certified.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path

from root_20261114_scaled_core import r225_coefficients, interval


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accepted", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    raw = args.accepted.read_bytes()
    data = json.loads(gzip.decompress(raw) if args.accepted.suffix == ".gz" else raw)
    if data.get("success") is not True or data.get("status") != 0 or data.get("M") != 96:
        raise ValueError("A completed actual M96 BVP output is required")
    if not (0 <= data["collocation_rms_max"] <= float(data["parameters"]["tol"])
            and 0 <= data["boundary_residual_max"] <= 1e-11):
        raise ValueError("The actual BVP did not satisfy its recorded original gates")
    base = [Q(6, 5) * x for x in r225_coefficients()]
    exact = [Q(x) for x in data["solved_metric_definition"]["core_coefficients_binary64_exact_rational"]]
    if exact != [Q(x) for x in data["core"]["coefficients"]] or len(exact) != 96:
        raise ValueError("Complete exact coefficients disagree with the accepted output")
    difference = [x - (base[n - 1] if n <= 32 else 0) for n, x in enumerate(exact, 1)]
    e0 = sum(abs(x) for x in difference)
    e1 = sum(2 * n * abs(x) for n, x in enumerate(difference, 1))
    erho = sum((4 * n * n - 1) * abs(x) for n, x in enumerate(difference, 1))
    earc = sum(Q(4 * n * n - 1, 2 * n) * abs(x) for n, x in enumerate(difference, 1))
    major = 1 + sum(base)
    minor = 1 + sum((-1) ** n * x for n, x in enumerate(base, 1))
    rminus = 1 + sum((1 - 4 * n * n) * x for n, x in enumerate(base, 1))
    rplus = 1 + sum((-1) ** n * (1 - 4 * n * n) * x for n, x in enumerate(base, 1))
    gap = 2 * sum(x for n, x in enumerate(exact, 1) if n % 2)
    rho_lower, rho_upper = rminus - erho, rplus + erho
    support_lower = minor - e0
    geometric_proof_applies = rho_lower > 0 and support_lower > 0 and gap > 0
    values = dict(coefficient_L1=e0, support_derivative_L1=e1,
                  curve_displacement_upper=e0 + e1,
                  rho_change_upper=erho, material_arc_change_upper=earc,
                  rho_lower=rho_lower, rho_upper=rho_upper,
                  support_lower=support_lower,
                  exact_axis_gap=gap,
                  core_diameter_upper=2 * (major + e0),
                  rotated_core_Hausdorff_upper=major - minor + 2 * e0)
    if rho_lower > 0:
        k0 = Q(float(data["solved_metric_definition"]["scalar_initial_law"]["k0"]))
        values["conditional_inlet_curvature_upper"] = max(1 / rho_lower, abs(k0) * rho_upper)
    enclosures = {key: interval(value) for key, value in values.items()}
    for key, value in values.items():
        if Q(enclosures[key][0]) == value:
            enclosures[key][0] = interval(value - Q(1, 10 ** 24))[0]
        if not Q(enclosures[key][0]) < value < Q(enclosures[key][1]):
            raise ArithmeticError("Strict decimal enclosure failed: " + key)
    result = dict(scope=__doc__,
                  accepted_sha256=hashlib.sha256(raw).hexdigest(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  base_source_sha256=hashlib.sha256(Path(__file__).with_name("root_20261114_scaled_core.py").read_bytes()).hexdigest(),
                  coefficients_exact=[str(x) for x in exact],
                  differences_from_R236_exact=[str(x) for x in difference],
                  exact_bounds={key: str(value) for key, value in values.items()},
                  strict_decimal_enclosures=enclosures,
                  checks=dict(all_96_coefficients_match_output=True,
                              rho_positive_for_all_angles=rho_lower > 0,
                              support_positive_for_all_angles=support_lower > 0,
                              axis_gap_positive=gap > 0,
                              first_32_exactly_round_R236=exact[:32] == [Q(float(x)) for x in base]),
                  analytic_strictly_convex_core_certified=geometric_proof_applies,
                  material_circle_diffeomorphism_certified=geometric_proof_applies,
                  axis_witness_distance_equals_gap=geometric_proof_applies,
                  proof_reference="results/R237-accepted-M96-core-global-certificate.md, sections 1-3",
                  changes_from_previous_seed_are_not_fixed_metric_refinement=True,
                  closed_surface_certified=False, continued_prefix_ball_exclusion_certified=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(dict(analytic_strictly_convex_core_certified=geometric_proof_applies,
                          enclosures=enclosures, checks=result["checks"])), flush=True)
    return 0 if geometric_proof_applies else 2


if __name__ == "__main__":
    raise SystemExit(main())

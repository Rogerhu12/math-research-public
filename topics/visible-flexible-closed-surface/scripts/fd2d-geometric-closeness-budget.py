#!/usr/bin/env python3
"""Exact scalar budget for the conditional C2 comparison theorem R110.

This does not read a new surface or certify any actual difference norm.
The three supplied tolerances remain hypotheses until a complete, own-map
comparison covers the prefix, tail, joins and fixed caps.  All inequalities
below use rational arithmetic; decimal displays are for orientation only.
"""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path


def record(x):
    return {"exact": str(x), "approximate": float(x)}


def budget(epsilon=Q(1, 10000), eta=Q(1, 1000), beta=Q(1, 10)):
    if epsilon < 0 or not 0 <= eta < 1 or beta < 0:
        raise ValueError("Require epsilon,beta >= 0 and 0 <= eta < 1")
    radius = Q(2131902881202937, 1125899906842624)
    diameter = 2 * radius
    support = Q(737, 1000)
    curvature = Q(105782, 12500)
    held = Q(199891, 1000000)
    holding_diameter = Q(17713, 5000)
    real_moment = Q(11, 25)

    new_support = support - 2 * radius * eta - epsilon
    new_curvature = (curvature + beta) / (1 - eta) ** 2
    new_diameter = diameter + 2 * epsilon
    new_held = held - 2 * epsilon
    new_holding = holding_diameter - 2 * epsilon
    reach = min(new_support, 1 / new_curvature)
    # 4*pi < 88/7.  This is the swept-volume bound for Re integral w^3.
    moment_error = (Q(88, 7) * epsilon * (radius + epsilon) ** 3
                    * (1 + eta) ** 2 * radius ** 3 / support)
    new_moment = real_moment - moment_error
    assertions = {
        "positive_support": new_support > 0,
        "reach_ratio_above_003": reach > Q(3, 100) * new_diameter,
        "held_ratio_above_005": new_held > Q(1, 20) * new_diameter,
        "holding_diameter_ratio_above_02": new_holding > Q(1, 5) * new_diameter,
        "positive_real_third_moment": new_moment > 0,
    }
    return {
        "status": "CONDITIONAL_SCALAR_BUDGET_ONLY",
        "actual_new_surface_difference_bounds_supplied": False,
        "metric_or_refinement_certified": False,
        "hypotheses": {k: record(v) for k, v in
                       {"epsilon_C0": epsilon, "eta_first_relative_to_old_metric": eta,
                        "beta_covariant_second_relative_to_old_metric": beta}.items()},
        "old_R21_R25_bounds": {k: record(v) for k, v in
                              {"radius_upper": radius, "diameter_upper": diameter,
                               "support_lower": support, "curvature_upper": curvature,
                               "held_lower": held, "holding_diameter_lower": holding_diameter,
                               "real_third_moment_lower": real_moment}.items()},
        "new_conditional_bounds": {k: record(v) for k, v in
                                  {"diameter_upper": new_diameter,
                                   "support_lower": new_support,
                                   "curvature_upper": new_curvature,
                                   "reach_lower": reach,
                                   "reach_ratio_lower": reach / new_diameter,
                                   "held_lower": new_held,
                                   "held_ratio_lower": new_held / new_diameter,
                                   "holding_diameter_lower": new_holding,
                                   "holding_diameter_ratio_lower": new_holding / new_diameter,
                                   "third_moment_error_upper": moment_error,
                                   "real_third_moment_lower": new_moment}.items()},
        "exact_comparisons": assertions,
        "all_conditional_geometric_thresholds_hold": all(assertions.values()),
        "scope": "Requires an actual C2 closed common-material chart, complete own-map "
                 "difference bounds and the original fixed-cap/symmetry construction. "
                 "It does not prove a new isometric solution or complete the topic.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epsilon", type=Q, default=Q(1, 10000))
    parser.add_argument("--eta", type=Q, default=Q(1, 1000))
    parser.add_argument("--beta", type=Q, default=Q(1, 10))
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = budget(args.epsilon, args.eta, args.beta)
    args.out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": result["status"],
                      "exact_comparisons": result["exact_comparisons"],
                      "new_conditional_approximate_bounds": {
                          k: v["approximate"] for k, v in
                          result["new_conditional_bounds"].items()}}, indent=2))

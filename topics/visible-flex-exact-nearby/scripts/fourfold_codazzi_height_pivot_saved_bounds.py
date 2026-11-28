#!/usr/bin/env python3
"""New exact combinations of CW/APHI/ASB/ANP saved constants only."""

from fractions import Fraction as F
import json


def main():
    h_lower, h_upper = F(".02513"), F(".02547")
    phase_lower, phase_upper = F(".038736784"), F(".038768096")
    p = F("1.543")
    f, tail, e = F(".0016047"), F(".00005330"), F(".0000006")
    mean = F(".0000284")
    joint96_error = e / h_lower + (
        F(".00017") * (f + e) / (h_lower * F(".0253"))
    )
    checks = {
        "height_reciprocal": 1 / h_lower < 40,
        "phase_ratio_lower": phase_lower / h_upper > F("1.5208"),
        "phase_ratio_upper": phase_upper / h_lower < p,
        "amplitude_ratio_lower": F(".006264") / h_upper > F(".2459"),
        "amplitude_ratio_upper": F(".006275") / h_lower < F(".2498"),
        "physical_norm": f / h_lower < F(".063856"),
        "physical_and_original_B_far_tail": tail / h_lower < F(".002121"),
        "original_B_full_norm": F(".1696") / h_lower < F("6.749"),
        "physical96_joint_error": joint96_error < F(".0004532"),
        "each_physical_mean": mean / h_lower < F(".001131"),
        "joint_two_mean_squared": 2 * (mean / h_lower) ** 2 < F(".001599") ** 2,
        "joint98_norm_squared": (
            F(".063856") ** 2 + F(".001599") ** 2 < F(".063877") ** 2
        ),
        "joint98_approximation_squared": (
            F(".0004532") ** 2 + F(".001599") ** 2 < F(".001663") ** 2
        ),
        "reduced_phase_root": 2600 + p * 94600 < 148568,
        "reduced_phase_root_source": 184 + p * 6693 < 10512,
        "reduced_phase_strict_source": 69 + p * 3024 < 4736,
        "reduced_phase_strict_jumps": 245 + p * 8907 < 13989,
        "world_position_port": p * F(27, 8) < F("5.208"),
        "world_rotation_port": p * F(4617, 2000) < F("3.563"),
    }
    products = {}
    for name, coefficient, whole, high in [
        ("root_and_root_jumps", 94600, "6040.7776", "200.6466"),
        ("root_source", 6693, "427.388208", "14.195853"),
        ("strict_source", 3024, "193.100544", "6.413904"),
        ("strict_jumps", 8907, "568.765392", "18.891747"),
    ]:
        checks[name + "_whole_product"] = F(".063856") * coefficient == F(whole)
        checks[name + "_high_product"] = F(".002121") * coefficient == F(high)
        products[name] = {"whole": whole, "high97": high}
    assert all(checks.values()), checks
    print(json.dumps({
        "kind": "new_exact_height_pivot_saved_scalar_consequences",
        "new_comparisons": len(checks),
        "all_passed": True,
        "old_scientific_targets_evaluated": 0,
        "physical96_error_exact_rational": str(joint96_error),
        "complete_original_source_feedback_products": products,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

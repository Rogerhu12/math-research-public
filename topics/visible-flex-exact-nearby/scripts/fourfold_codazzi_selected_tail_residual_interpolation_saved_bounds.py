#!/usr/bin/env python3
"""New SRH exact consequences of completed S/SREG/SHL bounds.

The same seventeen comparisons were first evaluated once in code mode.
No seed, Nash step, source, inverse, old reader, or scientific target is
called here. This file preserves the exact equivalent arithmetic.
"""
import json


def exact_consequences():
    checks = [
        ("source_interpolation_weight", 3320 * 227 == 166 * 4540),
        ("background_interpolation_weight", 2800 * 227 == 140 * 4540),
        ("source_exponent_dominates_background", 26 * 1856 - 11852 > 0),
        ("order4000_source_below_minus164", 166 * 4000 - 701252 < -164 * 227),
        ("order4000_background_below_minus164", 140 * 4000 - 689400 < -164 * 227),
        ("order4224_decay_above_quarter", 4 * (701252 - 166 * 4224) > 227),
        ("whole_geometric_ratio_below_half", 1500000 > 16),
        ("order4000_whole_tail_exponent", 184549391 - 164 * 1500000 == -61450609),
        ("order4000_tail_below_seed_comparison", 61450609 > 49999999),
        ("order4224_uniform_whole_tail_exponent", 184549391 - 1500000 // 4 == 184174391),
        ("actual_prior_window_background", 2204 + 1796 == 4000),
        ("actual_prior_window_source", 2204 + 1734 == 3938),
        ("actual_residual_source_order", 2204 + 1735 < 4000),
        ("actual_internal_coefficient_order", 2204 + 1742 < 4000),
        ("actual_outer_state_order", 2204 + 1780 < 4000),
        ("actual_outer_height_order", 2204 + 1782 < 4000),
        ("strong_cutoff_from_extra_order", 4001 <= 4224),
    ]
    if not all(passed for _, passed in checks):
        raise ArithmeticError("SRH exact consequence failed")
    return {
        "new_comparisons": [{"id": key, "passed": passed} for key, passed in checks],
        "new_comparison_count": len(checks),
        "old_science_runs": 0,
        "new_nash_iterations": 0,
        "unchanged_selector": True,
        "value_regular_order": 4224,
        "small_background_order": 4000,
        "actual_linearized_output_order": 2204,
        "rough_source_onto_asserted": False,
        "topic_completion_asserted": False,
    }


if __name__ == "__main__":
    print(json.dumps(exact_consequences(), sort_keys=True, separators=(",", ":")))

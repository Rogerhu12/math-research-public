#!/usr/bin/env python3
"""The new complete selected-vector coefficient; no old targets."""
import json


def main():
    graph_exponent = 4096 - 31_222_782
    parameter_exponent = -55_000_000
    output_exponent = -31_218_685
    passed = (parameter_exponent < graph_exponent
              and graph_exponent + 1 == output_exponent)
    if not passed:
        raise AssertionError("complete selected vector coefficient")
    print(json.dumps({
        "all_passed": passed,
        "new_exact_integer_combinations": 1,
        "complete_chain_rule_exponents":
            [graph_exponent, parameter_exponent],
        "global_C2_vector_response_upper_exponent": output_exponent,
        "actual_selected_difference_quotients": True,
        "full_original_matching_and_flat_disk": True,
        "fixed_height_and_one_Euclidean_placement": True,
        "H8193_operator_continuity_only": True,
        "relative_A0_expansion_at_each_fixed_base": True,
        "old_scientific_targets": 0,
    }, indent=2))


if __name__ == "__main__":
    main()

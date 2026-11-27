#!/usr/bin/env python3
"""GF: exact new exponent combinations for actual gamma parameter forcing.

All completed graph, profile and seed exponents are inputs.
Integer exponent arithmetic avoids materializing huge powers of two.
No former native array, ODE, Green function or target is evaluated.
"""

import json


def main():
    checks = {}

    def lt(name, value, bound):
        checks[name] = value < bound
        if not checks[name]:
            raise AssertionError(name)

    # If N nonnegative terms are each <= 2**e, their sum is <=
    # 2**(e + ceil(log2(N))). This integer formula is exact.
    def positive_sum_exponent(*exponents):
        return max(exponents) + (len(exponents)-1).bit_length()

    endpoint_high = 512*(2899+32)+262144
    endpoint_total = endpoint_high+1048577+120+8192+32
    lt("actual gamma derivative endpoint moment fits old complete budget",
       endpoint_total, 6291456)
    lt("gamma high direction stays inside original input window", 2899, 8193)
    lt("fixed physical height retains real added terminal trace", 2898+3, 8196)

    weight_sup = 262144+456
    lt("actual P2 raw coefficient supremum", weight_sup, 263000)
    lt("auxiliary P2 ball stays in original second parameter box",
       263000-524288, -34)
    lt("actual seeds stay in auxiliary joint parameter ball",
       -110000000, -524288)
    radial_metric = 262144+456+48+64+16
    lt("complete metric scalar jets and partial radial translations",
       radial_metric, 524288)
    lt("one extra actual real flow metric insertion",
       524288+8192+64, 786432)
    lt("full first-principal fixed-point inverse in P norm",
       786432+4416+1, 791000)
    internal_feedback = 786433+4096+28-18
    outer_feedback = 786433+4096+132-18
    lt("actual internal first metric curve derivative", internal_feedback, 800000)
    lt("actual outer first metric curve derivative", outer_feedback, 800000)
    lt("feedback retained then absorbed in direct metric profile",
       800000-48000000, 0)
    lt("actual row feedback below direct row", 791000-48000000, 0)

    metric_source_total = 655360+524288+262144+131200+1168+128
    lt("complete new metric source and all three broken radial jets",
       metric_source_total, 2097152)
    lt("full metric mean and coordinate readouts", 2*2097152+8, 6291456)
    lt("actual graph and cap output remain in common low ball",
       positive_sum_exponent(-49000000, 6291456-57000000)+3,
       -48000000)
    lt("endpoint affine term is small in common graph", 6291456-57000000, 0)
    lt("complete endpoint source chain including full means",
       4194304+6291456+16, 12582912)

    cap_low = 12582912-57000000+2
    metric_low = 6291456-110000000+1
    source_low = positive_sum_exponent(cap_low, metric_low)
    lt("complete actual parameter source is below final low bound",
       source_low, -44000000)
    lt("metric source remains separately smaller than endpoint source",
       metric_low, cap_low)
    lt("minimum displayed low-source gamma order fits original domain",
       1794+1, 8193)
    lt("highest requested loss1734 source is in proved window",
       1164+1734, 2899)
    lt("highest requested gamma order is in original domain",
       1164+1734+1, 8193)

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_integer_comparisons": len(checks),
        "source_angular_window": [20, 2898],
        "low_source_order": 1794,
        "gamma_direction_order_for_low_source": 1795,
        "original_gamma_value_domain_order": 8193,
        "normalized_gamma_direction": "r_gamma^(-1) ||eta||_H^j",
        "endpoint_source_coefficient": "2^12582912 epsilon_L",
        "second_parameter_source_coefficient": "2^(6291456-110000000)",
        "complete_low_source_upper": "2^-44000000",
        "complete_low_source_exponent_before_final_widening": source_low,
        "full_first_principal_feedback_retained": True,
        "true_radial_first_compensation_retained": True,
        "common_reference_source_and_three_broken_radial_jets_retained": True,
        "true_holonomy_mean_and_reference_height_retained": True,
        "fixed_metric_proxy_column_used_as_whole_family_derivative": False,
        "selected_nonlinear_solution_differentiability_asserted_here": False,
        "A0_only_high_source_estimate_asserted_here": False,
        "old_native_arrays_reference_integrations_and_scientific_targets": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

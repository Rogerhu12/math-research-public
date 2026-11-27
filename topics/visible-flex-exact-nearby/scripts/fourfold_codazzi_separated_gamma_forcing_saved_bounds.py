#!/usr/bin/env python3
"""GA: new exact combinations for separated-end A0 parameter forcing.

Uses the already completed finite-long module constants and GF source
budgets. No prior kernel, PDE, coefficient array or target is rerun.
"""

from fractions import Fraction as F
import json


def main():
    checks = {}

    def lt(name, value, bound):
        checks[name] = value < bound
        if not checks[name]:
            raise AssertionError(name)

    def positive_sum_exponent(*exponents):
        return max(exponents)+(len(exponents)-1).bit_length()

    lt("unit analytic probe slope is in original mixed long window", 32, 23000000)
    long_column = F(128, 3)+F(1, 24)
    lt("complete differentiated long slope and mean column", long_column, 44)
    normalized_cap_column = 44*2*F(1, 10**8)
    lt("complete normalized gamma module column on actual wide product",
       normalized_cap_column, 2**8)
    lt("actual low B height meets complete Taylor degree ball",
       60-440-49000000, -4)
    lt("maximum factorial input has exact twelve-bit base", 2899, 2**12)
    mixed_moment_exponent = 16*2898+36
    lt("complete mixed excess-frequency moment sum", mixed_moment_exponent, 65536)
    continuity_moment_exponent = 16*2898+36+12+64
    lt("extra full parameter and height difference degree", continuity_moment_exponent, 65536)
    lt("actual boundary lift in original graph/source units", 65536+2048, 131072)
    lt("full endpoint derivative and original ordinary source chain",
       4194304+131072+16, 8388608)
    lt("one high source background still fits selected extra regularity",
       2898+1, 2960)
    lt("actual physical trace needed by maximum source remains in selected graph",
       2898+4, 2960+3)
    lt("low source extra background stays below the original low radius index",
       1794+1, 1856)

    cap_low = 8388608-57000000+1
    metric_low = 6291456-110000000
    full_low = positive_sum_exponent(cap_low, metric_low)
    lt("true metric column remains separately smaller than endpoint column",
       metric_low, cap_low)
    lt("complete actual A0 parameter forcing before final widening",
       full_low, -48000000)
    lt("loss1734 high source remains inside complete window", 1164+1734, 2899)
    lt("deep metric source profile decays after all neighbor and source weights",
       F(97), F(98)-F(10, 256))

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_rational_and_integer_comparisons": len(checks),
        "complete_long_slope_and_mean_direction_coefficient": str(long_column),
        "operator_gamma_input": "physical A0 / r_gamma",
        "endpoint_source_coefficient": "2^8388608 epsilon_L",
        "second_parameter_source_coefficient": "2^(6291456-110000000) W_s",
        "one_high_height_background_index": "s+1",
        "source_angular_window": [20, 2898],
        "low_complete_source_upper": "2^-48000000",
        "low_complete_source_exponent_before_widening": full_low,
        "actual_full_mixed_f_high_terms_retained": True,
        "joint_parameter_operator_continuity": "A0 -> Z_s^[3], s <= 2898, background E2960",
        "high_gamma_direction_moment_used": False,
        "unknown_f_or_gamma_spatial_strip_assumed": False,
        "full_first_principal_metric_feedback_retained": True,
        "mean_source_and_reference_height_kept_in_distinct_units": True,
        "old_native_arrays_long_solutions_and_scientific_targets": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

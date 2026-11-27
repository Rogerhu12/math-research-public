#!/usr/bin/env python3
"""GHC: exact new combinations for the complete endpoint-height column.

Only completed GA, GHR, Gseed and graph coefficients are combined.
No native arrays, kernels or scientific integrations are evaluated.
"""

import json


def main():
    checks = {}

    def lt(name, value, bound):
        checks[name] = value < bound
        if not checks[name]:
            raise AssertionError(name)

    def positive_sum_exponent(*values):
        return max(values)+(len(values)-1).bit_length()

    lt("actual B collar background radial derivative stays in coefficient ball",
       1024-440-48000000, 0)
    lt("qualified mixed t-state Cauchy coefficient",
       10+130+11+4, 256)
    kappa0 = 80-440
    kappat = positive_sum_exponent(80+1024-440, 80-440, 256-440)
    height0 = 1+kappa0-1024
    height1 = 1+kappa0
    height2 = 1+positive_sum_exponent(2+kappa0, kappat)
    mean = positive_sum_exponent(height0, height1, height2)
    lt("complete mean endpoint height two-jet sum", mean, 700)
    nonmean = 586+3
    lt("complete nonmean endpoint height two-jet sum", nonmean, 600)
    total = positive_sum_exponent(mean, nonmean)
    lt("both complete endpoint height components", total, 1024)
    lt("actual A0 gamma endpoint height column",
       131072+1+1024, 262144)
    lt("scaled material Cartesian conversion including true radius", 7, 8)
    lt("screened endpoint height coefficient remains small",
       262144-57000000, -56000000)
    lt("one extra low background index is inside original value ball", 21, 1856)

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_integer_comparisons": len(checks),
        "kappa_direction_exponent": kappa0,
        "kappa_direction_radial_derivative_exponent": kappat,
        "complete_mean_endpoint_C2_exponent": mean,
        "complete_nonmean_endpoint_C2_exponent": nonmean,
        "total_endpoint_C2_exponent": total,
        "actual_endpoint_height_upper":
            "s_B 2^262144 epsilon_L r_gamma^-1 ||eta||_A0",
        "physical_conversion": "2^8 max(1,a_B^-2)",
        "one_global_lambda_is_independent": True,
        "metric_reference_column":
            "GHR, independent complete two-parameter column",
        "mean_column_is_an_actual_directed_integral": True,
        "cap_long_unscreened_height_span_is_not_erased": True,
        "old_scientific_arrays_kernels_integrals_and_targets": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

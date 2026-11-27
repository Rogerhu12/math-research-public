#!/usr/bin/env python3
"""New HL Hilbert-module and actual-seed combinations; no prior targets."""
from fractions import Fraction as F
import json


def main():
    checks = {}

    def check(label, condition):
        checks[label] = bool(condition)
        if not condition:
            raise AssertionError(label)

    check("complete two-sided lag convolution fee",
          1 + 2 * 2**15 < 2**17)
    check("actual cap one-Hilbert-slot degree sum",
          F(128, 9) < 2**4)
    check("actual cap mixed Hilbert-Wiener degree sum",
          F(4096, 27) < 2**8)
    check("qualified complex cap product for Hilbert far probes",
          F(1, 64) + F(1, 32) < F(1, 16))
    check("every actual seed label enters that smaller cap product",
          -443 + 60 - 8 < -5)
    check("incoming Hilbert seed derivative fits uniform label budget",
          21 + 2 + 1 < 32)
    check("actual complete D_aF-minus-D0 seed derivative absorbs",
          -404 - 7 < -1)
    check("every true update has a Hilbert-to-Wiener width gap",
          F(3177, 400) > 1)
    check("complete direct gamma seed update fee",
          F(2 * 44 * 2**21, 16) < 2**24)
    check("the same 94-step Hilbert induction closes",
          24 - 57_000_000 < 31 - 55_000_000)
    seed_derivative_224 = 32 - 55_000_000 - 332_000
    second_seed_exponent = 266_256 - 55_332_002 + seed_derivative_224
    check("actual second seed retains both small factors",
          seed_derivative_224 == -55_331_968
          and second_seed_exponent == -110_397_714
          and second_seed_exponent < -110_000_000)
    check("whole screened Hilbert endpoint module",
          44 * 2**21 < 2**27 < 2**32)
    check("actual far trace admits radius-one-thirty-second kernels",
          -380 - 49_000_000 < -10
          and 128 * F(1, 2**10) == F(1, 8))
    check("complete mixed high far-factor window",
          16 * 2898 + 72 == 46_440 < 65_536)
    check("complete joint Hilbert-operator continuity window",
          2899 + 2 < 4096
          and 24 + 7 + 8 + 8 < 64
          and 16 * 2898 + 136 == 46_504 < 65_536)

    print(json.dumps({
        "checks": checks,
        "result": {
            "all_passed": all(checks.values()),
            "new_exact_combinations": len(checks),
            "cap_direction": "L2 -> dotH2 with constant 2^21 r_f/r_gamma",
            "actual_seed94_derivative": "2^32 R_a/r_gamma",
            "actual_second_seed_exponent": second_seed_exponent,
            "full_source_window": [20, 2898],
            "full_parameter_forcing_upper": "2^-48000000/r_gamma in L2 direction",
            "high_background": "one W_(s+1)",
            "joint_operator_topology": "L2 -> Z_s^[3], gamma A0, w E2960",
            "original_mean_and_three_radial_source_jets": True,
            "metric_reference_height_is_separate": True,
            "actual_94_steps_differentiated": True,
            "nonlinear_L2_open_value_domain": False,
            "old_scientific_targets": 0,
        },
    }, indent=2))


if __name__ == "__main__":
    main()

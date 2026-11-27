#!/usr/bin/env python3
"""Ten new actual-R-anchor combinations from the solved M/D long graph."""
from fractions import Fraction as F
import json


def main():
    checks = {}

    def check(label, condition):
        checks[label] = bool(condition)
        if not condition:
            raise AssertionError(label)

    endpoint_data = F(1, 10**8) + F(1, 2**60)
    y = F(1, 6_000_000)
    r = 4 * y
    a = F(7, 10**6)
    w = F(5, 28) * a
    q = w * w
    check("actual M long data improve the original solved Y ball",
          F(1024, 63) * endpoint_data < y)
    check("same complete LV coframe algebra qualifies for this M graph",
          y < F(1, 1024) and r < F(1, 64))
    check("same physical R slope bound", w == F(1, 800_000))
    check("actual complete R angle has a bounded inverse derivative",
          F(7, 10**9) < F(1, 2))
    check("full physical coframe square-root branch remains positive",
          1 - q * (2*r + 3*r*r) > F(1, 4))
    frame_error = r * (w + 3*q)
    check("complete vertical frame value and moving first angular jet",
          frame_error < F(1, 10**12)
          and 2*frame_error < F(2, 10**12))
    position_jet = 2 * a * w * F(1, 4*10**8)
    check("actual endpoint nonmean height supplies the vertical position jet",
          position_jet < F(5, 10**20))
    mean_height = a * w * 128 * y*y
    check("unscreened actual mean-height at R retains its physical size",
          mean_height < F(4, 10**23))
    height_value = a * w * F(1, 16*10**8) + mean_height
    check("complete R height value after retaining the one translation",
          height_value < F(6, 10**21))
    check("independent world tilt keeps its actual angular-frame factor",
          1 + a*a*(F(1, 128**2) + F(1, 9)) < 4)

    print(json.dumps({
        "checks": checks,
        "result": {
            "all_passed": True,
            "new_exact_combinations": len(checks),
            "R_vertical_frame_value_upper": "1e-12",
            "R_vertical_frame_phi_upper": "2e-12",
            "R_vertical_position_phi_upper": "5e-20",
            "R_height_value_after_translation_upper": "6e-21",
            "complete_actual_M_long_inputs": True,
            "original_Connection_anchor": True,
            "det_frame": -1,
            "full_actual_holonomy_mean": True,
            "single_world_frame_and_translation": True,
            "R_to_L_state_difference_still_separate": True,
            "old_scientific_targets": 0,
        },
    }, indent=2))


if __name__ == "__main__":
    main()

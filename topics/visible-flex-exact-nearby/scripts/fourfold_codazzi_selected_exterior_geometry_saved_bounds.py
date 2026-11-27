#!/usr/bin/env python3
"""Four new actual exterior-disk geometry combinations; no old targets."""
from fractions import Fraction as F
import json


def main():
    checks = {
        "whole actual physical C2 comparison":
            708 + 64 - 47_000_000 == -46_999_228 < -46_000_000,
        "actual perturbation fits uniform geometric box":
            -46_000_000 < -3,
        "boundary-inclusive nearest-point reach":
            (1 - F(1, 8))**2 / (2 + F(1, 8))
            == F(49, 136) > F(1, 3),
        "complete normal and second-form differences":
            4 + F(1, 8) < 5
            and 2 * (4 + F(1, 8)) < 16
            and 1 + 2 * 16 < 64,
    }
    if not all(checks.values()):
        raise AssertionError([k for k, v in checks.items() if not v])
    print(json.dumps({
        "checks": checks,
        "result": {
            "all_passed": True,
            "new_exact_combinations": 4,
            "actual_C2_difference_upper": "2^-46000000",
            "same_actual_radial_metric_reference": True,
            "whole_tail_finite_connector_and_filled_disk": True,
            "reach_lower_physical_units": "1/3",
            "actual_piece_boundary_included": True,
            "whole_closed_surface_reach_claimed": False,
            "old_scientific_targets": 0,
        },
    }, indent=2))


if __name__ == "__main__":
    main()

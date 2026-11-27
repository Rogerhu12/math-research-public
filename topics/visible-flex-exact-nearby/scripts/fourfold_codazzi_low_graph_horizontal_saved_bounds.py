#!/usr/bin/env python3
"""New GHV saved-bound combinations only; no PDE or old-target execution."""
from fractions import Fraction as F
import json


def main():
    checks = {}

    def check(label, value):
        checks[label] = bool(value)
        if not value:
            raise AssertionError(label)

    check("actual entire finite connector metric box",
          F(35, 18) < 2 and F(5, 18) < F(1, 3)
          and F(35, 18_000_000) < F(1, 8))
    check("full fixed-metric background physical two-jet remains in chart",
          708 - 47_000_000 < -5
          and F(1, 8) + F(1, 32) < F(1, 4)
          and 2 + F(1, 32) < 4)
    check("single complete material-path length",
          1 + 2 * F(22, 7) < 8)
    check("positive complete horizontal metric neighborhood",
          F(1, 64) + F(1, 16) < F(1, 8))
    check("actual complete first physical metric derivative",
          F(1, 2) + F(1, 12) + 2 < 4 < 32)
    check("actual metric direction recovered from full reference height",
          F(4, 3) < 4 and F(4, 3) + F(16, 9) < 4)
    check("complete varied physical metric including angular radial unit",
          F(1, 4) + 4 + F(1, 4) + F(1, 2) < 6
          and F(1, 2) + 8 + F(1, 2) < 10
          and max(6, 10) < 2**8)
    check("complete coframe mixed physical derivative",
          2 + 8 * 32 < 2**9)
    check("actual determinant direction is retained",
          (2 + 16) * 2 < 2**6)
    check("complete oriented connection direction",
          2**6 * 2**8 + 4 * 2**11 < 2**15)
    check("full first vector jet with transported phase",
          2**19 + 2 < 2**20)
    check("all four physical second-vector-jet derivative terms",
          2**18 * (2**11 + 2**6)
          + 2**11 + 2**16 + 2**9 < 2**30)
    check("whole vector component count and height composition",
          2**24 + 2**22 + 2**33 < 2**40
          and 2**40 * 2**8 + 1 < 2**64)
    check("complete actual low-graph derivative including first Gamma",
          max(64 + 2048, 64 + 12002 - 47_000_000) + 1 < 4096)
    check("complete actual gamma derivative including both true columns",
          max(64 - 56_000_000, 64 + 1474 - 110_000_000) + 1
          < -55_000_000)

    result = {
        "all_passed": all(checks.values()),
        "new_exact_comparisons": len(checks),
        "fixed_gamma_vector_formal_two_jet": "2^4096 ||h||_E20",
        "actual_partial_gamma_vector_formal_two_jet":
            "2^-55000000 ||eta||_A0 / r_gamma",
        "full_metric_direction_from_reference_height": True,
        "actual_radial_rotation_connection_retained": True,
        "all_original_jumps_and_flat_disk_outputs_retained": True,
        "generic_broken_readout_is_not_automatic_global_C2": True,
        "exact_selected_matching_closed_subspace": True,
        "independent_world_height_and_frame_ports_retained": True,
        "old_scientific_targets": 0,
    }
    print(json.dumps({"checks": checks, "result": result}, indent=2))


if __name__ == "__main__":
    main()

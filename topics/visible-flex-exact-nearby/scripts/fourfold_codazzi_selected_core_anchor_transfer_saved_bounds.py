#!/usr/bin/env python3
"""ACT: exact NEW combinations of completed original bounds.

No scientific input is regenerated.  The 19 comparisons here are the
derivative/selected-core/receiver consequences proved in the companion
note.  This is not a validator for old geometry or old trial targets.
"""
from fractions import Fraction as F
import json


def fraction_text(x):
    return str(x.numerator) + "/" + str(x.denominator)


def conclusions():
    g = F(539, 250)
    length = F(97527, 50000)
    frequency = F(1152)
    state_error = F(2, 10**9)
    dm = F(15736315, 10**6) * state_error
    dc = F(30196406, 10**6) * state_error
    relative_derivative = (frequency + 2 * g) * dm
    kernel_l1 = dc + length * dm
    kernel_phi_l1 = (
        (frequency + g) * dc
        + (length * (frequency + 2 * g) + 8) * dm
    )
    frame_phi_fee = (frequency + 3 * g) * dm
    position_phi_fee = (
        kernel_phi_l1 + relative_derivative * kernel_l1
    )
    upper = {
        "frame_value_fee": F(3148, 10**11),
        "frame_phi_fee": F(36461, 10**9),
        "position_phi_fee": F(141, 10**6),
        "position_from_A1": F(1950541, 10**6),
        "position_from_A0": F(12205365, 10**6),
    }
    checks = []

    def compare(name, left, right):
        passed = left < right
        checks.append({
            "name": name,
            "left": fraction_text(left),
            "right": fraction_text(right),
            "strict": True,
            "passed": passed,
        })
        if not passed:
            raise ArithmeticError(name + ": outward inequality failed")

    compare("raw frame first derivative",
            F(4646383, 10**6), g * g)
    compare("raw position first derivative",
            2 * F(1275713422847, 10**12) * F(5970523, 10**6),
            F(16))
    compare("core frame C0 fee", dm, upper["frame_value_fee"])
    compare("core frame C1 fee", frame_phi_fee, upper["frame_phi_fee"])
    compare("core position C1 fee", position_phi_fee,
            upper["position_phi_fee"])
    compare("anchor A1 position coefficient",
            length + kernel_l1, upper["position_from_A1"])
    compare("anchor A0 position coefficient",
            g * length + 8 + g * kernel_l1,
            upper["position_from_A0"])

    old_base = (94000, 6650, 3000, 8850)
    old_a0 = (86061, 6086, 2919, 8098)
    old_a1 = (12531, 887, 441, 1180)
    old_b1 = (4590, 325, 210, 432)
    new_base = (94002, 6651, 3001, 8851)
    new_a0 = (196118, 13878, 7384, 18459)
    new_a1 = (21484, 1521, 851, 2023)
    source_names = (
        "root_Cauchy_plus_root_atoms",
        "root_Hminus_two_thirds_plus_Hminus1_L2dr",
        "strict_two_Hminus1_L2dr",
        "strict_original_atoms",
    )
    table = []
    for i, name in enumerate(source_names):
        a0 = (
            old_a0[i] + 2 * g * old_a1[i]
            + old_b1[i] * upper["position_from_A0"]
        )
        a1 = old_a1[i] + old_b1[i] * upper["position_from_A1"]
        bias = (
            old_a0[i] * upper["frame_value_fee"]
            + old_a1[i] * upper["frame_phi_fee"]
            + old_b1[i] * upper["position_phi_fee"]
        )
        compare("WRA source " + str(i) + " A0", a0, F(new_a0[i]))
        compare("WRA source " + str(i) + " A1", a1, F(new_a1[i]))
        compare("WRA source " + str(i) + " bias",
                bias, F(new_base[i] - old_base[i]))
        table.append({
            "original_source": name,
            "base": new_base[i],
            "coefficient_of_actual_L_vertical_frame_value": new_a0[i],
            "coefficient_of_actual_L_vertical_frame_derivative": new_a1[i],
            "coefficient_of_actual_L_vertical_position_derivative": old_b1[i],
        })

    exact = {
        "raw_frame_phi_upper": g,
        "raw_position_phi_upper": F(4),
        "raw_path_length_upper": length,
        "complete_difference_frequency": frequency,
        "selected_core_state_error": state_error,
        "connection_difference_L1": dm,
        "velocity_difference_L1": dc,
        "position_difference_kernel_L1": kernel_l1,
        "position_difference_kernel_phi_L1": kernel_phi_l1,
        "frame_phi_additive_fee": frame_phi_fee,
        "position_phi_additive_fee": position_phi_fee,
    }
    return {
        "kind": "selected_core_C1_anchor_transfer_saved_bounds_v1",
        "new_distinct_rational_comparisons": len(checks),
        "all_new_comparisons_passed": all(x["passed"] for x in checks),
        "exact_constants": {k: fraction_text(v) for k, v in exact.items()},
        "outward_transfer_constants": {
            k: fraction_text(v) for k, v in upper.items()
        },
        "complete_original_source_receiver_table": table,
        "comparisons": checks,
        "scope": {
            "same_original_selected_Qdelta": True,
            "same_eta0_and_original_moving_angle": True,
            "propagation_interval": ["9/50", "9/10"],
            "full_mean_and_complete_connection": True,
            "unknown_variations_are_not_Fourier_truncated": True,
            "absolute_frame_determinant": -1,
            "actual_cap_L_anchor_still_independent": True,
            "actual_full_TC_residuals_required": True,
            "varying_world_position_and_frame_ports_retained": True,
            "fourfold_periodicity_or_boundary_functional_required": True,
            "no_old_scientific_targets_recomputed": True,
            "full_bordered_inverse_proved": False,
            "topic_completion_proved": False,
        },
    }


if __name__ == "__main__":
    print(json.dumps(conclusions(), sort_keys=True, indent=2))

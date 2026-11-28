#!/usr/bin/env python3
"""New exact scalar consequences for the true strict second variational column."""

from fractions import Fraction as F
import json


def main():
    b, V, B0, C0 = F(9, 50), F(18, 5), F(".222"), F("1.176")
    M, L = F("75.01268"), F(".006179202")
    pure = F(".361") * (F(7, 5) * V**3 * F("2.028") + V**2 * F("6.139"))
    source = F("10.025") * M * L + 802 * L + pure
    a0, a1, b1 = F(".002235"), F(".015072"), F(".04748")
    checks = {
        "true_L1_state": F(".006176330577") + b * F(".00001594684") < L,
        "true_L2_state_squared": M * L < F(".681") ** 2,
        "true_raw_waist": 400 * F(".002834044286435") + F(".00001594684") < F("1.133634"),
        "complete_state_Hessian": F(48, 5) * B0 * V + 2 * C0 < F("10.025"),
        "complete_mixed_Hessian": F(22, 5) * 4 * V**2 + 2 * 24 * V < 401,
        "metric_support_sqrt": F(13, 100) < F(".361") ** 2,
        "complete_pure_metric_source": pure < 77,
        "complete_true_second_source": source < 87,
        "true_second_primitive_means": F("7.661355") * 87 < 667,
        "true_second_waist_density": F("4.253890") * 87 < 371,
        "d_value": F(".4") * B0 * 4**2 < F("1.421"),
        "d_first_L2": F(".5") * B0 * 4 == F(".444"),
        "d_first_Linfty": B0 * 4 == F(".888"),
        "d_second_state": F(8, 5) * B0 < F(".356"),
        "d_second_mixed": F(16, 100) < F(".356"),
        "d_second_parameter": F("51.2") / 10000 < F(".356"),
        "dvn_first": F(".444") * 4 + F("1.421") + F("5.684") == F("8.881"),
        "dvn_second": sum(map(F, ["1.424", "11.368", "1.776", "3.552", "2.842"])) < 21,
        "dn_first": F(".444") + F("1.421") < F("1.866"),
        "dn_second": F(".356") + 2 * F("1.421") + 2 * F(".444") < F("4.1"),
        "p_first": F(".211") * F("8.881") + F(".1055") * F("5.684") / 100 + F(".211") < F("2.1"),
        "p_second": F(".211") * 21 + 2 * F(".1055") * F("8.881") / 100 + F(".05275") * F("5.684") / 10000 < F("4.45"),
        "k_first": F("1.176") + 24 * 4 / F(100) + F("8.881") < F("11.02"),
        "k_second": 21 + 48 / F(100) + 24 * 4 / F(10000) < F("21.5"),
        "M_first": F("2.1") + F(9, 8) * (F("11.02") + F("1.866")) < F("16.6"),
        "M_second": F("4.45") + F(9, 8) * (F("21.5") + F("4.1")) < F("33.3"),
        "velocity_value": F(9, 8) * (F("1.12") + F("5.684") + F("4.48")) < F("12.7"),
        "velocity_first": F(9, 8) * (F(".0056") + F("8.881") + F("1.12") + F(".0224")) < F("11.3"),
        "velocity_second": F(9, 8) * (F(".000028") + 21 + F(".0112") + F(".000112")) < F("23.7"),
        "sqrt_b": b < F(".425") ** 2,
        "frame_first_product": F("16.6") * F(".425") == F("7.055"),
        "frame_second": 2 * F("7.055") ** 2 + F("33.3") < 133,
        "position_first_uniform_body": b * F("12.7") * F("7.055") + F("11.3") * F(".425") < 21,
        "position_first_uniform_anchor": b * F("12.7") < 21,
        "position_second_uniform": b * F("12.7") * 133 + 2 * F("7.055") * F("11.3") * F(".425") + F("23.7") < 396,
        "position_first_selected": b * F("3.8") * F("7.055") + F("11.3") * F(".425") < F("9.63"),
        "position_second_selected": b * F("3.8") * 133 + 2 * F("7.055") * F("11.3") * F(".425") + F("23.7") < 183,
        "moving_test_second": 2 * (4 * F("2.1") ** 2 + 4 * F("4.2") + 2 * F("2.1") * 5 + 10) == F("130.88"),
        "actual_waist_height": F(".000232743") + F(".004288") + F(".002235") * F(".684") < F(".00605"),
        "uniform_physical_height_Hessian": 8 * 396 + 2 * F("26.8") * 21 + F("130.88") * F(".01") < 4300,
        "selected_physical_height_Hessian": 8 * 183 + 2 * F("26.8") * F("9.63") + F("130.88") * F(".00605") < 2000,
        "uniform_mean_height_Hessian": 4 * 396 + 2 * 5 * 21 + 10 * F(".01") < 1800,
        "selected_mean_height_Hessian": 4 * 183 + 2 * 5 * F("9.63") + 10 * F(".00605") < 829,
        "strict_first_direction_norm": F(".681") + F("42.5") + F("1.133634") < F("44.315"),
        "second_state_phase_receiver": F("5.67") * F("1.03") * b * 667 < 702,
        "actual_height_body_kernel": 141 + F(70053, 640) * a0 + F(11367, 800) * a1 < 142,
        "actual_height_waist_kernel": F(".066025") + F(37359, 10000) * a0 + F(171, 200) * a1 + F(5, 4) * b1 < F(".147"),
        "second_state_height_receiver": (142 * b + F(".147")) * 667 < 17147,
        "complete_second_phase": F(21, 20) * 530 * F("100.681") ** 2 + 702 < 5650000,
        "complete_second_height": 829 * F("44.315") ** 2 + 17147 < 1650000,
        "phase_test_value_derivative": F(25, 24) * F(21, 20) * 150 * F("100.681") < 16613,
        "phase_test_slope_derivative": F(25, 24) ** 2 * F("2.16") * F("100.681") < 237,
        "two_mean_norm_squared": 2 * F(".0000284") ** 2 < F(".00004017") ** 2,
        "complete_mean_column_derivative": F("4.253890") * 87 + 2 * F(15, 16) * F("1.133634") * F(".00004017") < 371,
        "height_inverse_derivative": 1650000 / F(".02513") ** 2 < 2620000000,
        "phase_height_ratio_derivative": (5650000 + F("1.543") * 1650000) / F(".02513") < 327000000,
        "mean_height_ratio_derivative": (371 + F(".001599") * 1650000) / F(".02513") < 120000,
    }
    assert all(checks.values()), {k: v for k, v in checks.items() if not v}
    print(json.dumps({
        "kind": "new_exact_true_strict_second_variation_saved_scalar_consequences",
        "new_comparisons": len(checks),
        "all_passed": True,
        "old_scientific_targets_evaluated": 0,
        "complete_second_source_L1_Hminus1_exact_majorant": str(source),
        "true_second_state_is_full_frequency": True,
        "full_regular_inverse_or_iteration_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()


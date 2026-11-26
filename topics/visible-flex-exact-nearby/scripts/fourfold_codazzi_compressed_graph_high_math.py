"""DG: the complete ordered graph remainder using C = W S.

Pure directed formulas; no imports, IO, old target calls or numerical
backend. A public owner admits all complete same-selected inputs and the
DC/DB/R31/W analytic qualification. The exact envelope ||C^-1||_-4/3<2^14
is proved by integer comparisons in DG.3--7, not a new old-norm receipt.

The original CG module supplies its whole common6/PN56 admission. Passing
only two norm strings, partial positive outputs or new VQ L2 rows is not
qualification for this complete graph high block.
"""

KIND = "complete_same_density_compressed_graph_high_envelopes_v1"
COMMON_RECORD = "common_high_WPL_physical_primitive_upper"
PORT_RECORD = "negative_port_09_WPL_physical_primitive_upper"
NEW_RECORD_ORDER = (
    "complete_compressed_positive_feedback_high_addition_upper",
    "complete_compressed_coupled_reference_high_deviation_upper",
    "complete_compressed_genuine_physical96_high_factor_upper",
    "complete_compressed_physical96_augmented_high_deviation_upper",
)
PARAMETERS = {
    "ordinary_target_cutoff": "2^4608",
    "physical_frequency_factor": 4,
    "model_one_loss_constant": 256,
    "true_inverse_lift_complex_strip": "1/256",
    "true_inverse_lift_real_derivative_lower": "465/512",
    "true_inverse_lift_real_second_derivative_upper": "6",
    "true_inverse_lift_complex_first_derivative_upper": "11/10",
    "true_inverse_lift_real_third_derivative_upper": "720896/5",
    "same_C_inverse_Hminus_four_thirds_strict_upper": "2^14",
    "new_complete_homogeneous_high_deviation_strict_upper": "2^-437",
    "new_common_compression_factor": "2^-1462",
    "new_physical96_bound_factor": "2^-1479",
    "complete_transported_reference_factor": "2^-1470",
    "exact_complete_ordered_remainder":
        "B^-1 [Qa Rss A^-1 C + Qa Ti (S-C) + "
        "(Epartial+DeltaPartial) S] P97 C^-1 A Gbar",
    "exact_ordered_source_map": "S P97 C^-1 A",
    "same_C_distributional_inverse_and_original_negative_window": True,
    "one_Bessel_comparison_factor_included": True,
    "ordinary_low_complement_dimension": "2^4608-1",
    "changed_target_normalizer_or_full_mean_convention": False,
    "new_VQ_L2_bound_substituted_for_Theta": False,
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def admit_receivers(original_cg, admitted, common, physical_ports):
    """Reuse the complete original identities before the new same-map step."""
    original_cg.admit_receivers(admitted, common, physical_ports)
    require(original_cg.COMMON_RECORD == COMMON_RECORD
            and original_cg.PORT_RECORD == PORT_RECORD,
            "the same two whole physical receiver records")
    for key in (
        "whole_original_DC_DB_W_R31_analytic_qualification_verified",
        "R31_complete_Ldelta_is_the_complex_field_derivative_integral_verified",
        "same_true_C_equals_W_S_and_DB_distributional_inverse_verified",
        "complete_WDH_error_and_mean_ranks_retained_without_upper_subtraction",
    ):
        require(admitted.get(key) is True,
                "complete original same-operator qualification: "+key)
    return True


def complete_fixed_high_envelopes(api, core, original_cg, admitted,
                                  common, physical_ports, emit):
    """DG.1/19 for the fixed original cutoff, with every dependency saved.

    emit(name, point, 'upper') saves and reads the whole candidate and its
    public prefix, then returns the actual formally saved upper endpoint.
    The two physical norm inputs are from complete actual original receivers.
    The pure formulas are not an execution or proof of their prerequisites.
    """
    admit_receivers(original_cg, admitted, common, physical_ports)

    def read(actual, name):
        record = actual["new_records"][name]
        require(record["bound"] == "upper", "one whole saved receiver upper")
        value = core.saved_upper(api, record)
        require(value.is_finite() and bool(value >= api.zero),
                "a finite nonnegative complete receiver")
        return value

    cadd = read(common, COMMON_RECORD)
    d96 = read(physical_ports, PORT_RECORD)
    homogeneous = api.rational(1, 1 << 437)
    common_factor = api.rational(1, 1 << 1462)
    physical_factor = api.rational(1, 1 << 1479)
    reference = api.rational(1, 1 << 1470)
    order = []

    def save(name, value):
        require(name == NEW_RECORD_ORDER[len(order)],
                "the complete fixed new record order")
        point = core.upper(api, value)
        require(point.is_finite() and bool(point >= api.zero),
                "one directed whole high envelope")
        saved = emit(name, point, "upper")
        require(saved.is_finite() and bool(saved >= point),
                "dependent expressions consume the whole saved upper")
        order.append(name)
        return saved

    addition = save(NEW_RECORD_ORDER[0], common_factor*cadd)
    coupled = save(NEW_RECORD_ORDER[1], homogeneous+addition)
    finite = save(NEW_RECORD_ORDER[2], physical_factor*d96+reference)
    augmented = save(NEW_RECORD_ORDER[3], coupled+finite)
    half = api.rational(1, 2)
    common_pass = bool(coupled < half)
    physical_pass = bool(augmented < half)
    require(not physical_pass or common_pass,
            "positive complete fees preserve the strict high gate order")
    require(order == list(NEW_RECORD_ORDER), "all four whole records saved")
    return {
        "kind": KIND,
        "reference_identity": admitted["reference_identity"],
        "selected_member_identity": common["selected_member_identity"],
        "parameters": dict(PARAMETERS),
        "input_records": {
            "complete_same_common_WPL_addition": COMMON_RECORD,
            "complete_joint_physical_root96_WPL_column": PORT_RECORD,
        },
        "complete_new_record_count": 4,
        "complete_new_record_order": order,
        "same_original_homogeneous_WDH_high_gate_preserved": True,
        "new_complete_homogeneous_high_deviation_strict_bound": "2^-437",
        "coupled_reference_high_deviation_less_than_half_proved": common_pass,
        "coupled_reference_high_inverse_norm_strictly_less_than_two_proved": common_pass,
        "physical96_augmented_high_deviation_less_than_half_proved": physical_pass,
        "physical96_augmented_high_inverse_norm_strictly_less_than_two_proved": physical_pass,
        "whole_operator_collected_before_norm": True,
        "saved_composite_uppers_subtracted": False,
        "transported_projector_moved_through_model_or_Fourier_cutoff": False,
        "original_B_target_normalizer_and_A_source_map_retained": True,
        "complete_reference_difference_and_all_mean_ranks_retained": True,
        "source_Ni_or_Lambda_applied_again": False,
        "physical96_right_W_inverse_A_factor_applied": False,
        "physical96_columns_replaced_by_reference_columns": False,
        "extra_sqrt96_or_sign_block_sqrt2_applied": False,
        "new_VQ_L2_norm_used_for_Theta": False,
        "signed_entries_or_original_Theta_rows_reconstructed": False,
        "complete_finite_complement_inverse_proved": False,
        "complete_physical_mean_nu_phase_border_proved": False,
        "full_incoming_inverse_proved": False,
        "all_s_or_parameter_family_inverse_proved": False,
        "nonlinear_solution_or_topic_completion_proved": False,
        "old_completed_scientific_target_calls": 0,
    }

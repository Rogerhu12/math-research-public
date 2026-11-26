"""Pure ordered high-tail adapter for the true positive-feedback graph.

CG.10--26: whole actual common6 and physical-port56 are input certificates.
This module imports no numerical library, reads no file and repeats no old
scalar or moment.  A future public owner verifies the whole inputs and saves
each emitted ball before dependent arithmetic.  These values alone are not
a published scientific conclusion.
"""

COMMON_STAGE = "complete_actual_common_high_negative_receiver_stage_v1"
COMMON_RESULT = "complete_actual_common_high_WPN_to_negative_receivers_v1"
PORT_STAGE = "complete_actual_positive_to_negative_receiver_stage_v1"
PORT_RESULT = "complete_actual_fourteen_positive_ports_to_negative_receivers_v1"
COMMON_RECORD = "common_high_WPL_physical_primitive_upper"
PORT_RECORD = "negative_port_09_WPL_physical_primitive_upper"
NEW_RECORD_ORDER = (
    "complete_positive_feedback_high_addition_upper",
    "complete_coupled_reference_high_deviation_upper",
    "complete_genuine_physical96_high_factor_upper",
    "complete_physical96_augmented_high_deviation_upper",
)
PARAMETERS = {
    "ordinary_target_cutoff": "2^4608",
    "physical_frequency_factor": 4,
    "model_one_loss_constant": 256,
    "old_selected_homogeneous_high_deviation_strictly_less_than": "2^-44",
    "exact_ordered_source_map_after_adjacent_cancellation":
        "S P97 S^-1 W^-1 A; no commutation with Gbar or PJ",
    "new_common_compression_factor": "2^-1337",
    "new_physical96_bound_factor": "2^-1354",
    "complete_transported_reference_factor": "2^-1225",
    "input_original_Ni_applied_again": False,
    "physical96_right_W_inverse_A_factor_applied": False,
    "same_graph_L2_target_realization_only": True,
    "RNS_principal_minus_four_thirds_gate_substituted": False,
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def admit_receivers(admitted, common, physical_ports):
    """Type/domain check following the owner's whole-file actual admission."""
    require(isinstance(admitted, dict) and "private_token" in admitted,
            "private whole-file admission, not just two supplied norm strings")
    for key in (
        "whole_actual_common6_and56_science_execution_manifests_verified",
        "same_selected_WDH_model_graph_and_complete_coordinates_verified",
        "whole_WDH_old_sources_and_same_WX_forward_L2_verified",
        "actual_positive_square_and_homogeneous_negative_continuation_identified",
    ):
        require(admitted.get(key) is True, "complete original qualification: "+key)
    for actual, kind, result_kind, count in (
        (common, COMMON_STAGE, COMMON_RESULT, 6),
        (physical_ports, PORT_STAGE, PORT_RESULT, 56),
    ):
        require(actual["identity"]["kind"] == kind
                and actual["complete"] is True and actual["proved"] is True
                and actual["actual_returncode"] == 0 and actual["failure"] is None
                and actual["saved_record_count"] == count
                and len(actual["new_records"]) == count
                and actual["completed_targets"] == actual["result"]["complete_new_record_order"]
                and set(actual["new_records"]) == set(actual["completed_targets"])
                and actual["result"]["kind"] == result_kind
                and actual["result"]["complete_new_record_count"] == count
                and actual["result"]["topic_completion_proved"] is False,
                "one entire actual receiver conclusion, not an incomplete prefix")
        for key in ("old_scientific_target_calls", "new_arrays_published",
                    "new_artifacts", "new_Releases"):
            require(actual[key] == 0, "whole existing execution scope: "+key)
    require(common["reference_identity"] == physical_ports["reference_identity"]
                == admitted["reference_identity"]
            and common["high_response_source_binding"]
                == physical_ports["high_response_source_binding"],
            "same entire physical positive response and fixed reference")
    for role in ("gate_actual", "gate_execution", "gate_manifest",
                 "ports_actual", "ports_execution", "ports_manifest",
                 "wpn_actual", "wpn_execution", "wpn_manifest",
                 "SP_execution", "PW_execution", "WTA_actual", "WTA_execution", "WX_execution"):
        require(common["whole_completed_inputs"][role]
                    == physical_ports["whole_completed_inputs"][role],
                "the same whole original positive/negative/left receiver: "+role)
    for key in ("complete_family_identity", "selected_H_whole_source", "fixed_Js"):
        require(common["selected_receiver_identity"][key]
                    == physical_ports["selected_receiver_identity"][key],
                "the same selected full family and actual coordinate: "+key)
    cr, pr = common["result"], physical_ports["result"]
    require(cr["whole_source4_and_positive58_224_32_admitted"] is True
            and cr["same_NIF_common_domain_and_selected_WX_left_coordinate_verified"] is True
            and cr["common_high_Phi_Upsilon_strong_addition_size_proved"] is True
            and cr["input_domain"] == "Xfr_Hminus4over3_inherited_physical_norm"
            and cr["input_order"] == ["same_selected_frozen_common_high_unit_ball"]
            and cr["physical_prescribed_root_even96_is_zero"] is True
            and cr["state_induced_full_outer_mean_retained_in_D0"] is True
            and cr["auxiliary_Ec_star_e_assumed_zero"] is False
            and cr["independent_high_baseline_included"] is False
            and cr["rough_high_baseline_given_a_mixed_root_bound"] is False
            and cr["source_Ni_or_Lambda_applied_again"] is False
            and COMMON_RECORD in common["new_records"],
            "this same physical WPL strong addition, with no repeated baseline or right input")
    require(pr["all_fourteen_positive_port_to_negative_bounds_proved"] is True
            and len(pr["input_order"]) == 14
            and pr["input_order"][9] == "independent_low_root_even96_raw_boundary"
            and pr["physical_ports_promoted_to_common_Hminus4over3_input"] is False
            and pr["Ni_or_Lambda_right_input_change_performed"] is False
            and pr["original_high_root_factor9_repeated"] is False
            and PORT_RECORD in physical_ports["new_records"],
            "the actual joint physical96 input, with its own raw Euclidean norm")
    return True


def complete_fixed_high_envelopes(api, core, admitted, common, physical_ports, emit):
    """Four new whole envelopes after exact CG.10 cancellation.

    emit(name, point, "upper") must write/read/verify the entire candidate,
    then publish the completed prefix and return its actual saved upper.
    The old WDH deviation remains a strict bound <2^-44.  The scalar tests
    below only assert the specified graph high inverse with norm <2;
    neither they nor the resulting four uppers supply a finite inverse.
    """
    admit_receivers(admitted, common, physical_ports)

    def read(actual, name):
        record = actual["new_records"][name]
        require(record["bound"] == "upper", "whole formally saved receiver upper")
        value = core.saved_upper(api, record)
        require(value.is_finite() and bool(value >= api.zero), "finite nonnegative actual receiver")
        return value

    cadd = read(common, COMMON_RECORD)
    d96 = read(physical_ports, PORT_RECORD)
    old = api.rational(1, 1 << 44)
    common_factor = api.rational(1, 1 << 1337)
    physical_factor = api.rational(1, 1 << 1354)
    reference = api.rational(1, 1 << 1225)
    order = []

    def save(name, value):
        require(name == NEW_RECORD_ORDER[len(order)], "complete fixed new target order")
        point = core.upper(api, value)
        require(point.is_finite() and bool(point >= api.zero), "directed finite whole high fee")
        saved = emit(name, point, "upper")
        require(saved.is_finite() and bool(saved >= point),
                "dependent expressions require the verified whole saved upper")
        order.append(name)
        return saved

    addition = save(NEW_RECORD_ORDER[0], common_factor*cadd)
    coupled = save(NEW_RECORD_ORDER[1], old+addition)
    finite = save(NEW_RECORD_ORDER[2], physical_factor*d96+reference)
    augmented = save(NEW_RECORD_ORDER[3], coupled+finite)
    half = api.rational(1, 2)
    common_pass = bool(coupled < half)
    physical_pass = bool(augmented < half)
    require(not physical_pass or common_pass, "positive complete fees preserve the strict gate order")
    require(order == list(NEW_RECORD_ORDER), "all four whole new envelopes saved")
    return {
        "kind": "complete_same_selected_coupled_primitive_graph_high_envelopes_v1",
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
        "coupled_reference_high_deviation_less_than_half_proved": common_pass,
        "coupled_reference_high_inverse_norm_strictly_less_than_two_proved": common_pass,
        "physical96_augmented_high_deviation_less_than_half_proved": physical_pass,
        "physical96_augmented_high_inverse_norm_strictly_less_than_two_proved": physical_pass,
        "adjacent_true_inverse_cancellation_used_before_norm": True,
        "transported_projector_moved_through_model_or_Fourier_cutoff": False,
        "full_physical96_high_outputs_retained": True,
        "complete_reference_difference_retained": True,
        "physical96_columns_replaced_by_reference_columns": False,
        "extra_sqrt96_or_original_Ni_fee_applied": False,
        "complete96_signed_entries_or_Theta_entries_reconstructed": False,
        "complete_finite_complement_inverse_proved": False,
        "complete_physical_mean_nu_phase_border_proved": False,
        "full_incoming_inverse_proved": False,
        "all_s_or_parameter_family_inverse_proved": False,
        "nonlinear_solution_or_topic_completion_proved": False,
        "old_completed_scientific_target_calls": 0,
    }

"""Remaining-only continuation of the saved complete genuine waist-error posterior.
No entry point, I/O, old producer import, old Jet reconstruction or old target call.
The owner admits the exact 23 complete nodes and the 39-record partial prefix.
Only the previously uncomputed 13 + 8 + 9 new retained records are evaluated.
All three output conclusions retain their original complete mathematical schemas.
"""
from __future__ import annotations
from fractions import Fraction
from copy import deepcopy
from flint import arb

N0 = 388
FIRST_MODE = 97
WAIST_JS = 268435456
RECONSTRUCTION_NODE = "complete_exact_waist_finite_reconstruction"
NODE_NAMES = (
    "complete_free_waist_Airy_and_Schur_map",
    "complete_four_waist_endpoint_contributions",
    "complete_same_physical_whole_and_reduced_error",
)
NEW_RECORD_COUNTS = (13, 8, 9)
COMPLETE_RECORD_COUNTS = (52, 8, 15)
PREFIX_RECORD_COUNT = 39
PREFIX_KEYS = (
    "kind", "complete",
    "complete_real_Airy_constants",
    "complete_reconstruction_and_map_records",
    "complete_A0_angular_jet",
    "complete_A1_angular_jet",
    "complete_A0_plus_inverse_input_A1_angular_jet",
    "complete_symbol_ordinary_derivatives_0_2",
)
AIRY_EXACT = (
    {"k": 1, "u": "5/72", "signed_v": "-7/72"},
    {"k": 2, "u": "385/10368", "signed_v": "-455/10368"},
    {"k": 3, "u": "85085/2239488", "signed_v": "-95095/2239488"},
)
SYMBOL_COMPONENTS = tuple(
    {"input_sign": eps, "reference": reference, "phase_branch": sigma}
    for eps in (-1, 1) for reference in ("Ai", "Bi") for sigma in (-1, 1)
)
WAIST_RECORD_NAMES = (
    "waist_ng_upper", "waist_q_lower", "waist_q_upper",
    "waist_absolute_mean_lower", "waist_U_L2_upper_from_original_pair_A0",
    "WT_complete_A2_upper", "SW_complete_W_Hminus4_3_upper_before_ng",
)
WHOLE_RECORD_NAMES = ("Calg", "Rplus", "RF", "KHinv_L2",
                      "Ni_Hminus4_3", "D_infinity")
PHASE_RECORD_PATHS = {
    "phase_second_normalized_upper": [
        "complete_strict_geometry_conclusion", "complete_jets",
        "phase_derivatives", "group_upper", 2],
    "phase_first_lower": [
        "complete_higher_flow_and_cut_conclusion", "strict_phase_lower"],
}
_ACTIVE_RECORD_CAPTURE = None


def require(test, message):
    if not test:
        raise ValueError(message)


def ex(value):
    if isinstance(value, Fraction):
        return arb(value.numerator) / arb(value.denominator)
    if type(value) is not int:
        raise TypeError("exact integers or Fraction only")
    return arb(value)


def up(value):
    value = arb(value)
    if not value.is_finite() or value.upper() < 0:
        raise ArithmeticError("nonfinite or negative complete norm bound")
    return value.upper()


def lower(value, label):
    value = arb(value)
    if not value.is_finite() or not value.lower() > 0:
        raise ArithmeticError("missing complete positive lower: " + label)
    return value.lower()


def normalized_original_record(value):
    """Type projection only. The whole original object is retained by the owner."""
    if isinstance(value, str):
        return {"ball": value}
    require(isinstance(value, dict) and isinstance(value.get("ball"), str),
            "complete original ball string required")
    return {"ball": value["ball"]}


def read_up(value):
    require(isinstance(value, dict) and set(value) == {"ball"}
            and isinstance(value["ball"], str),
            "one unchanged complete saved record required")
    return up(arb(value["ball"]))


def read_lower(value, label):
    require(isinstance(value, dict) and set(value) == {"ball"}
            and isinstance(value["ball"], str),
            "one unchanged complete saved lower record required")
    return lower(arb(value["ball"]), label)


def _capture_printed_record(value, direction):
    if _ACTIVE_RECORD_CAPTURE is not None:
        event = {"direction": direction, "record": deepcopy(value)}
        _ACTIVE_RECORD_CAPTURE["records"].append(event)
        hook = _ACTIVE_RECORD_CAPTURE.get("on_record")
        if hook is not None:
            hook(deepcopy(event))
    return value


def record(value):
    return _capture_printed_record({"ball": up(value).str(75)}, "upper")


def save_upper(document, name, value):
    document[name] = record(up(value))
    return read_up(document[name])


def positive_power(value, exponent, label):
    exponent = Fraction(exponent)
    if exponent < 0:
        base = lower(value, label)
    else:
        base = up(value)
        if base == 0:
            require(exponent > 0, "zero nonpositive power: " + label)
            return ex(0)
    return up(base ** (ex(exponent.numerator) / ex(exponent.denominator)))


def all_saved_ball_strings(value):
    if isinstance(value, dict):
        if set(value) == {"ball"} and isinstance(value["ball"], str):
            return {value["ball"]}
        result = set()
        for item in value.values():
            result.update(all_saved_ball_strings(item))
        return result
    if isinstance(value, list):
        result = set()
        for item in value:
            result.update(all_saved_ball_strings(item))
        return result
    return set()


def record_count(value):
    if isinstance(value, dict):
        if set(value) == {"ball"} and isinstance(value["ball"], str):
            return 1
        return sum(record_count(item) for item in value.values())
    if isinstance(value, list):
        return sum(record_count(item) for item in value)
    return 0


def start_progress(progress_state, node_name, saved_prefix=None):
    require(isinstance(progress_state, dict), "mutable scientific prefix state")
    require(node_name not in progress_state,
            "a preserved target cannot be silently recomputed")
    state = {
        "kind": "recoverable_new_scientific_node_prefix_v1",
        "node_name": node_name, "complete": False,
        "persisted_complete_node": False, "current_stage": "initializing",
        "complete_scientific_document_prefix": (
            deepcopy(saved_prefix) if saved_prefix is not None
            else {"kind": node_name, "complete": False}),
        "all_record_events_durably_captured_by_owner_neutral_API": True,
    }
    progress_state[node_name] = state
    return state


def progress_group(state, stage, key=None, value=None):
    state["current_stage"] = stage
    if key is not None:
        state["complete_scientific_document_prefix"][key] = value


def finish_progress(state, document, publish_graph):
    require(callable(publish_graph), "atomic bare-math publication callback")
    state["complete"] = True
    state["current_stage"] = "complete_graph_before_atomic_publication"
    state["complete_scientific_document_prefix"] = document
    saved = publish_graph(state["node_name"], document)
    require(isinstance(saved, dict) and saved == document,
            "complete persisted mathematics changed on canonical readback")
    state["persisted_complete_node"] = True
    state["current_stage"] = "complete_graph_read_back"
    return saved


def validate_saved_prefix(prefix):
    require(isinstance(prefix, dict) and set(prefix) == set(PREFIX_KEYS)
            and prefix["kind"] == NODE_NAMES[0] and prefix["complete"] is False,
            "the exact admitted 39-record semantic prefix is required")
    require(record_count(prefix) == PREFIX_RECORD_COUNT,
            "the saved prefix must retain every one of its 39 original records")
    require(len(prefix["complete_real_Airy_constants"]) == 18
            and len(prefix["complete_reconstruction_and_map_records"]) == 9,
            "incomplete saved Airy or column-remainder records")
    for key in ("complete_A0_angular_jet", "complete_A1_angular_jet",
                "complete_A0_plus_inverse_input_A1_angular_jet"):
        item = prefix[key]
        require(item["shape"] == [2, 0]
                and len(item["normalized_angular_coefficients"]) == 3,
                "the complete retained angular jet is required")
    require(len(prefix["complete_symbol_ordinary_derivatives_0_2"]) == 3,
            "all saved ordinary symbol derivatives are required")


def admit_phase_records(WGS_main):
    """Read exactly two paid records. Never construct a Jet or assign a lift value."""
    phase = WGS_main["complete_strict_geometry_conclusion"]["complete_jets"]["phase_derivatives"]
    certificate = WGS_main["complete_derivative_request_certificate"]
    require(phase["shape"] == [15, 3] and phase["value_omitted_for_lift"] is True
            and phase["group_upper"][0] is None
            and certificate["fixed_degree_groups"][2] == [2, 2],
            "the original derivative-only real lift qualification changed")
    return {
        "phase_second_normalized_upper": deepcopy(phase["group_upper"][2]),
        "phase_first_lower": deepcopy(
            WGS_main["complete_higher_flow_and_cut_conclusion"]["strict_phase_lower"]),
        "derivative_multi_index": [0, 2],
        "ordinary_derivative_factorial": 2,
        "lift_value_omitted": True,
    }


def complete_tail_weights():
    """New, previously uncomputed complete two-sign series bounds."""
    rows = {}
    gamma = ex(1) + ex(1) / ex(16*FIRST_MODE*FIRST_MODE)
    gamma43 = save_upper(rows, "complete_Bessel_ratio_four_thirds_upper",
                        positive_power(gamma, Fraction(4, 3), "Bessel ratio"))
    xi0sq = save_upper(rows, "complete_Xi0_squared_upper",
                      ex(4) / (ex(4)**4 * ex(3) * ex(96)**3))
    xi2sq = save_upper(rows, "complete_Xi2_squared_upper",
        ex(6) * gamma43 *
        positive_power(ex(4), Fraction(-4, 3), "physical frequency four") *
        positive_power(ex(96), Fraction(-1, 3), "integral lower endpoint"))
    ximsq = save_upper(rows, "complete_Xi23_6_squared_upper",
                      ex(2) * gamma43 / (ex(4)**5 * ex(4) * ex(96)**4))
    xi0 = save_upper(rows, "complete_Xi0_upper", xi0sq.sqrt())
    xi2 = save_upper(rows, "complete_Xi2_upper", xi2sq.sqrt())
    xim = save_upper(rows, "complete_Xi23_6_upper", ximsq.sqrt())
    return {"Xi0": xi0, "Xi2": xi2, "Xi23_6": xim}, {
        "new_complete_records": rows,
        "first_positive_integer_mode": FIRST_MODE,
        "physical_frequency": "4*abs(j)",
        "integral_lower_endpoint": 96,
        "Xi0_reference_sign_count": 4,
        "Xi2_input_sign_count": 2,
        "Xi23_6_input_sign_count": 2,
        "bound": "sum from j=97 to infinity of j^-p is at most integral from 96 to infinity",
        "full_Bessel_weights_retained": True,
        "no_root_scattering_matrix_Hilbert_Schmidt_sum": True,
    }


def complete_free_map_suffix(prefix, phase_records, extension,
                             publish_graph, progress_state):
    validate_saved_prefix(prefix)
    state = start_progress(progress_state, NODE_NAMES[0], prefix)
    document = state["complete_scientific_document_prefix"]
    constants = document["complete_real_Airy_constants"]
    pieces = document["complete_reconstruction_and_map_records"]
    D = [read_up(v) for v in document["complete_symbol_ordinary_derivatives_0_2"]]
    require(set(phase_records) == {
        "phase_second_normalized_upper", "phase_first_lower",
        "derivative_multi_index", "ordinary_derivative_factorial", "lift_value_omitted"}
        and phase_records["derivative_multi_index"] == [0, 2]
        and phase_records["ordinary_derivative_factorial"] == 2
        and phase_records["lift_value_omitted"] is True,
        "only the paid second phase derivative may enter this continuation")
    ml = read_lower(phase_records["phase_first_lower"], "same true phase lower")
    # The first attempt failed before this scalar operation. No Phi(0) exists here.
    phi2 = up(ex(2) * read_up(phase_records["phase_second_normalized_upper"]))
    pi_up = read_up(constants["complete_pi_upper"])
    cpre = read_up(pieces["complete_common_column_remainder_upper"])
    A1zero = read_up(document["complete_A1_angular_jet"]["normalized_angular_coefficients"][0])
    progress_group(state, "remaining_symbol_schur")
    schur = save_upper(pieces, "complete_one_phase_reference_sign_Schur_upper",
        positive_power(ml, Fraction(-1, 2), "same true phase lower") *
        (D[0] + pi_up*pi_up/ex(48) * (D[2]/ml**2 + D[1]*phi2/ml**3)))
    schur_all = save_upper(pieces, "complete_all_eight_symbol_components_upper",
                          ex(len(SYMBOL_COMPONENTS)) * schur)
    progress_group(state, "remaining_complete_tail_weights")
    tail_work, tail_document = complete_tail_weights()
    progress_group(state, "remaining_complete_free_map", "complete_tail_weights", tail_document)
    free_remainder = save_upper(pieces, "complete_free_map_remainder_upper",
                               tail_work["Xi0"] * cpre)
    save_upper(pieces, "complete_free_map_L2_to_density_upper", schur_all + free_remainder)
    CB = read_up(extension["constants"]["complete_cB_upper"])
    A1bi = save_upper(pieces, "complete_Bi_first_coefficients_two_sign_two_phase_sum_upper",
                     ex(4) * A1zero)
    save_upper(pieces, "complete_first_cancellation_column_upper",
               (ex(1) + CB/ex(N0)) * cpre + CB*A1bi)
    document.update({
        "complete": True,
        "same_reconstruction_node": RECONSTRUCTION_NODE,
        "exact_Airy_coefficient_recurrence": [deepcopy(x) for x in AIRY_EXACT],
        "complete_symbol_components": [deepcopy(x) for x in SYMBOL_COMPONENTS],
        "one_complete_common_bound_applies_to_each_listed_component": True,
        "same_waist_density_factor_already_in_V_and_B": True,
        "Ai_and_Bi_real_remainders_retained": True,
        "cB_squared_and_first_Airy_cross_retained": True,
        "original_root_matrix_not_treated_as_column_HS_error": True,
        "all_low_outputs_means_and_two_physical_rows_retained": True,
        "new_scalar_exp_or_log_calls": 0,
        "original_successful_targets_recomputed": 0,
    })
    require(record_count(document) == COMPLETE_RECORD_COUNTS[0],
            "the complete free-map graph lost an inherited or new record")
    saved = finish_progress(state, document, publish_graph)
    return decode_free_map(saved), saved


def decode_free_map(saved):
    require(saved.get("kind") == NODE_NAMES[0] and saved.get("complete") is True
            and saved.get("same_reconstruction_node") == RECONSTRUCTION_NODE,
            "complete retained free waist map required")
    require(saved.get("original_root_matrix_not_treated_as_column_HS_error") is True
            and saved.get("all_low_outputs_means_and_two_physical_rows_retained") is True,
            "free waist map scope changed")
    pieces = saved["complete_reconstruction_and_map_records"]
    tails = saved["complete_tail_weights"]["new_complete_records"]
    return {
        "KF": read_up(pieces["complete_free_map_L2_to_density_upper"]),
        "K2": read_up(pieces["complete_first_cancellation_column_upper"]),
        "Cpre": read_up(pieces["complete_common_column_remainder_upper"]),
        "Xi2": read_up(tails["complete_Xi2_upper"]),
        "Xi23_6": read_up(tails["complete_Xi23_6_upper"]),
        "pi_upper": read_up(saved["complete_real_Airy_constants"]["complete_pi_upper"]),
        "original_node": NODE_NAMES[0],
    }


def complete_four_waist_endpoints(original, free_map_document, extension,
                                 mean_union, publish_graph, progress_state):
    state = start_progress(progress_state, NODE_NAMES[1])
    free_map = decode_free_map(free_map_document)
    require(mean_union.get("complete_root_to_waist_mean") is True
            and mean_union.get("coefficient_power") == "n^(-23/6)"
            and mean_union.get("full_feedback_and_R0_not_assumed_zero") is True,
            "the complete saved root-to-waist physical mean is required")
    records = {name: normalized_original_record(original[name])
               for name in WAIST_RECORD_NAMES}
    ng = read_up(records["waist_ng_upper"])
    qlo = read_lower(records["waist_q_lower"], "actual waist q")
    qhi = read_up(records["waist_q_upper"])
    ml = read_lower(records["waist_absolute_mean_lower"], "actual waist physical mean")
    U0 = read_up(records["waist_U_L2_upper_from_original_pair_A0"])
    WT = read_up(records["WT_complete_A2_upper"])
    SW = read_up(records["SW_complete_W_Hminus4_3_upper_before_ng"])
    constants = {}
    progress_group(state, "scattering_and_mean_endpoint_factors", "complete_new_constants", constants)
    Cs = save_upper(constants, "complete_root_scattering_Hminus4_3_to_L2_upper",
        ex(Fraction(6, 5)) * (ex(16384) +
        ex(2) * positive_power(ex(N0), Fraction(-2, 3), "fixed input cutoff") *
        ex(168) * free_map["pi_upper"] *
        read_up(extension["constants"]["complete_H1_upper"])))
    Ik = save_upper(constants, "complete_I_of_waist_Jb2_L2_upper", U0/(ex(4)*ml))
    vz = save_upper(constants, "complete_physical_mean_endpoint_vector_upper",
                    ng * (qhi + Ik*Ik/qlo).sqrt())
    Z = read_up(mean_union["new_complete_records"]["complete_physical_mean_upper"])
    contributions = {}
    progress_group(state, "all_four_endpoints", "complete_four_endpoint_records", contributions)
    scatter = save_upper(contributions, "complete_scattering_endpoint_upper", free_map["KF"]*Cs)
    cross = save_upper(contributions, "complete_second_order_endpoint_upper",
                       free_map["K2"] * free_map["Xi2"])
    normalizer = save_upper(contributions, "complete_old_waist_normalizer_endpoint_upper", ng*WT*SW)
    mean = save_upper(contributions, "complete_physical_mean_endpoint_upper",
                      vz*Z*free_map["Xi23_6"])
    save_upper(constants, "complete_same_old_trial_waist_endpoint_upper",
               scatter + cross + normalizer + mean)
    document = {
        "kind": NODE_NAMES[1], "complete": True,
        "same_free_waist_node": NODE_NAMES[0],
        "complete_new_constants": constants,
        "complete_four_endpoint_records": contributions,
        "exact_signed_operator":
          "B_F^V*S_n*(Droot+Jinfinity)*iota_Ai + E2 - ng0*(P*A2*W,0) + v_z*z_end",
        "same_original_old_trial": "Y_W,J at the actual waist including all stored means",
        "scattering_input_matrix_order_retained": True,
        "original_genuine_Cn_and_beta_n_retained": True,
        "root_matrix_not_replaced_by_a_second_independent_column": True,
        "WT_uses_the_whole_saved_forward_strong_remainder": True,
        "no_first_finite_upper_subtracted_from_WT": True,
        "waist_ng_factor_in_WT_SW_product_count": 1,
        "physical_mean_vector_exact_identity": "J_w*b2_w=u_w/m_w; v_z=D0_w*(-u_w/m_w,1)",
        "physical_two_stored_means_retained_in_q_term": True,
        "original_root_to_waist_mean_feedback_retained": True,
        "retained_true_finite_complement_and_parameter_rows": True,
        "original_Ni_and_final_waist_readout_not_applied_here": True,
        "complete_physical_whole_error_claimed": False,
        "finite_Schur_or_incoming_inverse_claimed": False,
        "old_successful_quantities_recomputed": 0,
    }
    require(record_count(document) == COMPLETE_RECORD_COUNTS[1],
            "the complete four-endpoint graph lost a new record")
    saved = finish_progress(state, document, publish_graph)
    return decode_endpoints(saved), saved


def decode_endpoints(saved):
    require(saved.get("kind") == NODE_NAMES[1] and saved.get("complete") is True
            and saved.get("same_free_waist_node") == NODE_NAMES[0]
            and saved.get("physical_two_stored_means_retained_in_q_term") is True
            and saved.get("original_Ni_and_final_waist_readout_not_applied_here") is True,
            "complete retained four-endpoint graph required")
    return {"Cend": read_up(saved["complete_new_constants"][
        "complete_same_old_trial_waist_endpoint_upper"]), "original_node": NODE_NAMES[1]}


def complete_whole_error(original, negative, endpoints_document,
                         publish_graph, progress_state):
    state = start_progress(progress_state, NODE_NAMES[2])
    require(negative.get("complete") is True and
            negative.get("kind") == "complete_original_negative_source_and_jump_reception_v1"
            and negative.get("ordinary_radial_dr_and_original_receiver_cut_retained") is True
            and negative.get("physical_mean_source_and_feedback_in_M_terms_retained") is True,
            "the complete saved negative source and all jumps are required")
    endpoints = decode_endpoints(endpoints_document)
    old = {name: normalized_original_record(original[name]) for name in WHOLE_RECORD_NAMES}
    rows = {}
    progress_group(state, "complete_old_whole_inputs", "complete_original_records", old)
    progress_group(state, "complete_new_whole_error", "complete_new_records", rows)
    alg, rp, rf, kh, ni, di = (read_up(old[name]) for name in WHOLE_RECORD_NAMES)
    cn = read_up(negative["complete_negative_source_and_all_jump_upper"])
    ce = endpoints["Cend"]
    invsqrt2 = save_upper(rows, "complete_inverse_sqrt_two_upper", ex(1)/ex(2).sqrt())
    left = save_upper(rows, "complete_final_left_readout_upper", kh*invsqrt2)
    ordered = save_upper(rows, "complete_left_readout_times_right_input_upper", left*ni)
    nonroot = save_upper(rows, "complete_positive_negative_endpoint_sum_upper", rp+cn+ce)
    allsource = save_upper(rows, "complete_positive_root_negative_endpoint_sum_upper", nonroot+rf)
    received = save_upper(rows, "complete_received_whole_trial_error_upper", ordered*allsource)
    save_upper(rows, "complete_same_physical_whole_error_upper", alg+received)
    reduced_received = save_upper(rows, "complete_received_error_after_exact_root_factor_upper",
                                  ordered*nonroot)
    save_upper(rows, "complete_infinite_error_after_exact_finite_factors_upper", di+reduced_received)
    document = {
        "kind": NODE_NAMES[2], "complete": True,
        "complete_original_records": old,
        "complete_new_records": rows,
        "complete_received_negative_predecessor": "negative_reception",
        "complete_endpoint_predecessor": NODE_NAMES[1],
        "whole_identity": "Calg+(KHinv_L2/sqrt(2))*Ni_Hminus4_3*(Rplus+RF+Cnegative+Cend)",
        "reduced_identity": "D_infinity+(KHinv_L2/sqrt(2))*Ni_Hminus4_3*(Rplus+Cnegative+Cend)",
        "same_operator_domain": "Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row",
        "exact_finite_parts_retained_in_auxiliary_border": [
            "WFR complete root trace factor with its full input/output columns",
            "WCF complete FJ term and both primitive ranks",
            "WCF -(h-1)*rho_i and +(h-1)*ell2"],
        "true_physical_96_columns_and_all_Theta_cross_blocks_retained": True,
        "physical_two_means_nu_and_infinite_radial_head_retained": True,
        "root_factor_auxiliary_dimension_is_not_physical_dimension": True,
        "whole_Calg_not_replaced_by_D_infinity": True,
        "the_reduced_bound_keeps_every_exact_finite_factor": True,
        "original_CG_ST4_and_coordinate_factors_not_multiplied_twice": True,
        "new_whole_and_reduced_norms_only": True,
        "passing_high_cutoff_proved": False,
        "finite_Schur_inverse_proved": False,
        "full_incoming_inverse_proved": False,
        "full_nonlinear_background_proved": False,
        "final_surface_proved": False,
        "old_scientific_calls": 0,
    }
    require(record_count(document) == COMPLETE_RECORD_COUNTS[2],
            "the whole-error graph lost an original or new record")
    saved = finish_progress(state, document, publish_graph)
    return decode_whole(saved), saved


def decode_whole(saved):
    require(saved.get("kind") == NODE_NAMES[2] and saved.get("complete") is True
            and saved.get("the_reduced_bound_keeps_every_exact_finite_factor") is True
            and saved.get("whole_Calg_not_replaced_by_D_infinity") is True,
            "complete retained whole and reduced norms required")
    return {name: read_up(value) for name, value in saved["complete_new_records"].items()}

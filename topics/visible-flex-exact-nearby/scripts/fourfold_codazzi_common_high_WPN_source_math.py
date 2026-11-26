"""True common-high unit ball -> complete original finite/tail WPN source.

Pure definitions only.  The public owner first admits whole WOBSA, all six
old small inputs, and the same complete D/S/true-root certificate.
No numerical imports, IO, old producer calls, synthetic solution, S-max
descriptor, or future inverse data occur in this module.
"""

SOURCE_KIND = "complete_actual_physical_WPN_source_pair_bounds_v1"
DATA_KIND = "complete_actual_WOB_physical_source_data_v1"
COMMON_ROLE = "same_selected_frozen_common_high_unit_ball"
INPUT_NORM = "Xfr_Hminus4over3_inherited_physical_norm"
NEW_RECORD_ORDER = (
    "actual_source_weighted_body_rhs_upper",
    "actual_source_raw_endpoint193_rhs_upper",
    "actual_source_complete_WPN_pair_rhs_upper",
    "actual_source_original_radial_tail_rhs_upper",
)
OLD_GRAPH = "complete_zero_IVP_rows"
ROOT_LOWER = (1191984371497, 5000000000000)
OUTER = (25, 8)
REFINEMENT = 160


def require(ok, message):
    if not ok:
        raise ValueError(message)


def common_unit_ball_packet(source_interface, selected_identity, evidence_id):
    """Exact CX.1--3 source family, not the absent value of a particular x.

    Only the common x norm is one.  Every zero is a proved independent-data
    identity of THIS linear column.  Nonzero state-induced outer mean lives
    in D0; it is not the independent physical mean input set to zero here.
    """
    require(source_interface.DATA_KIND == DATA_KIND
            and len(source_interface.DATA_INPUT_ORDER) == 18,
            "the entire original physical source interface")
    require(isinstance(selected_identity, dict) and selected_identity
            and isinstance(evidence_id, str) and evidence_id,
            "one exact selected member and its whole CX proof")
    key = "frozen_common_high_Hminus4over3"
    require(key in source_interface.DATA_INPUT_ORDER,
            "original common input slot, not any of the14 physical ports")
    norms = {name: {"ball": "1" if name == key else "0", "bound": "upper"}
             for name in source_interface.DATA_INPUT_ORDER}
    packet = {
        "kind": DATA_KIND, "complete": True,
        "source_identity": {
            "role": COMMON_ROLE, "domain": INPUT_NORM,
            "definition": "(F,e)=(V0 Phi x,-(V0_R Phi-B_R^H Upsilon)x)",
            "input_ball": "all real reflected x with original norm <= 1",
            "same_cause_Ni_in_Phi_Upsilon_exactly_once": True,
            "independent_physical_root_even96": "exact_zero",
            "state_induced_outer_mean_in_D0": True,
            "particular_input_vector_invented": False,
        },
        "selected_member_identity": dict(selected_identity),
        "norm_records": norms,
        "evidence_ids": {name: evidence_id+"#CX1:"+name
                         for name in source_interface.DATA_INPUT_ORDER},
        "zero_identity_keys": [name for name in source_interface.DATA_INPUT_ORDER
                               if name != key],
        "qualifications": {name: True for name in source_interface.DATA_QUALIFICATIONS},
        "input_qualification": {
            "operator_unit_ball": True, "single_particular_x_value": False,
            "both_rhs_are_same_linear_input": True,
            "additional_high_return_excludes_genuine_baseline": True,
        },
    }
    require(not source_interface.missing_actual_data(packet),
            "every actual source slot and its zero proof is present")
    return packet


def complete_common_input_source_pair(
        api, core, source_interface, admitted, wobsa, reference, packet, emit):
    """CX.5--9: four new full RHS bounds without a missing S-max descriptor.

    emit must save and read a whole candidate ball, check it contains the
    original directed upper, THEN commit the completed prefix; it returns
    that saved upper.  Original completed Bx/Dx/Phi/t0/dB are only read.
    """
    require(isinstance(admitted, dict) and "private_token" in admitted,
            "whole metadata admission before numerical use")
    for name in (
            "whole_WOBSA_actual_execution_manifest_and_six_originals_verified",
            "all_WOBSA_same_selected_common_scopes_and_records_verified",
            "whole_D_actual_execution_manifest_and_reference_identity_verified",
            "same_original_S_mean_column_and_true_mesh_definition_verified",
            "same_selected_NIF_reflected_Hminus4over3_domain_verified",
            "complete_common_unit_ball_zero_identities_verified"):
        require(admitted.get(name) is True, "required exact qualification: "+name)
    require(packet["kind"] == DATA_KIND and packet["complete"] is True
            and packet["selected_member_identity"] == admitted["selected_member_identity"]
            and packet["source_identity"]["role"] == COMMON_ROLE
            and packet["source_identity"]["domain"] == INPUT_NORM
            and packet["source_identity"]["state_induced_outer_mean_in_D0"] is True
            and packet["input_qualification"]["operator_unit_ball"] is True,
            "this exact common-input source family")
    require(packet == common_unit_ball_packet(
                source_interface, admitted["selected_member_identity"],
                admitted["whole_CX_proof_evidence_id"]),
            "all18 norms and all17 exact independent-data zero identities")
    require(reference["reference_identity"] == admitted["reference_identity"]
            and reference["boundary_lift"]["true_reference_independent_mean_retained"] is True
            and reference["parameters"]["parent_cells"] == 153
            and reference["parameters"]["uniform_refinement"] == REFINEMENT
            and reference["parameters"]["refined_cells"] == 24480,
            "same S and true24480 projection, with its exact mean column")
    scope = wobsa["retained_scope"]
    require(scope["same_selected_member_same_physical_eta0"] is True
            and scope["Ni_and_stable_inverse_in_original_right_order_once"] is True
            and scope["full_low193_rows_and_independent_even_mean_retained"] is True,
            "complete common observations and the nonzero physical outer mean")

    def up(value):
        return core.upper(api, value)

    def read(record):
        return core.saved_upper(api, record)

    def graph(group, key):
        return read(wobsa["complete_new_graphs"][group]["complete_new_records"][key])

    phi = graph("complete_genuine_and_rough_observations", "complete_Phi_upper")
    bx = graph(OLD_GRAPH, "complete_B0_high_body_row_upper")
    dx = graph(OLD_GRAPH, "complete_D0_high_endpoint_row_upper")
    t0 = read(wobsa["copied_original_scalar_records"]["C_R0"])
    db = read(reference["new_records"]["reference_weighted_right97_body_upper"])
    weighted_even = up(t0*db*phi)
    body = core.hypot(api, bx, weighted_even)
    hstar = up((api.rational(*OUTER)-api.rational(*ROOT_LOWER))/REFINEMENT)
    require(api.lower(hstar) > 0, "true positive whole original fine-cell upper")
    weighted_length = up(core.root(api, hstar)*db)
    mesh = weighted_length if bool(weighted_length > hstar) else hstar
    pi_lower = api.lower(api.pi())
    require(pi_lower > api.zero, "directed positive pi denominator")
    tail = up((mesh/pi_lower)*phi)
    order = []

    def save(name, value):
        require(name == NEW_RECORD_ORDER[len(order)], "exact whole four-record order")
        point = up(value)
        saved = emit(name, point, "upper")
        require(saved.is_finite() and bool(saved >= point),
                "whole saved candidate readback returned its safe upper")
        order.append(name)
        return saved

    body_saved = save(NEW_RECORD_ORDER[0], body)
    endpoint_saved = save(NEW_RECORD_ORDER[1], dx)
    save(NEW_RECORD_ORDER[2], core.hypot(api, body_saved, endpoint_saved))
    save(NEW_RECORD_ORDER[3], tail)
    require(order == list(NEW_RECORD_ORDER), "all four complete source bounds")
    return {
        "kind": SOURCE_KIND,
        "reference_identity": admitted["reference_identity"],
        "selected_member_identity": admitted["selected_member_identity"],
        "source_identity": packet["source_identity"],
        "complete_actual_input_order": list(source_interface.DATA_INPUT_ORDER),
        "complete_actual_input_evidence_ids": dict(packet["evidence_ids"]),
        "complete_new_record_order": order,
        "complete_new_record_count": 4,
        "complete_actual_source_pair_upper_bounds_proved": True,
        "original_finite_WPN_RHS_upper_record": NEW_RECORD_ORDER[2],
        "original_joint_finite_and_tail_WPN_RHS_upper_record": NEW_RECORD_ORDER[2],
        "original_radial_tail_WPN_RHS_upper_record": NEW_RECORD_ORDER[3],
        "operator_unit_ball_in_original_common_high_space": True,
        "generic_Smax_descriptor_used_or_fabricated": False,
        "weighted_body_and_tail_paid_by_same_D_mean_column": True,
        "same_24480_original_projection_and_independent_endpoint193_retained": True,
        "same_cause_two_paths_combined_before_norm_without_false_orthogonality": True,
        "all_actual_data_zero_claims_have_explicit_original_identity": True,
        "state_induced_full_outer_mean_retained_in_D0": True,
        "physical_prescribed_root_even96_is_zero": True,
        "auxiliary_Ec_star_e_assumed_zero": False,
        "Ni_applied_again": False,
        "arbitrary_L2_rhs_differentiated_or_traced": False,
        "independent_high_baseline_included_in_return_output": False,
        "rough_high_baseline_upgraded_to_raw_L2": False,
        "complete_physical_inverse_or_224_port_table_proved": False,
        "complete_32_WPN_response_table_proved": False,
        "particular_signed_solution_or_response_error_proved": False,
        "common_high_strong_addition_size_proved": False,
        "complete_incoming_inverse_proved": False,
        "true_nu_or_phase_Schur_proved": False,
        "nonlinear_background_or_surface_proved": False,
        "topic_completion_proved": False,
        "old_completed_scientific_targets_recomputed": 0,
    }

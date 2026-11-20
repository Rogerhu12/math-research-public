"""Actual physical WOB data -> the original finite and radial-tail WPN pair.

Pure definitions only: no numerical import, file IO, old producer, dummy
future inverse, or default-zero data.  A public owner must admit the whole
WOBSA/negative/D/mesh and actual data identities before numerical use.
The new result is four source-size bounds, not an inverse or a solution.
"""

KIND = 'complete_actual_physical_WPN_source_pair_bounds_v1'
DATA_KIND = 'complete_actual_WOB_physical_source_data_v1'
WOBSA_KIND = 'complete_outer_rows_and_rough_positive_observation_bounds_v1'
NEGATIVE_KIND = 'actual_full_real_delta_negative_one_positive_given_head_graph_v1'
REFERENCE_KIND = 'complete_fixed_WVC_reference_boundary_lifts_v1'
WOBSA_RUN = ('43844596176', '1')
SEVEN_PORTS = (
    'root_stable_Y_port',
    'collar_ordinary_Hminus2over3_source',
    'body_ordinary_Hminus2over3_source',
    'body_outer_mean_head_and_Y_weighted_jumps',
    'collar_Y_weighted_affine_jumps',
    'cut_stable_Y_jump',
    'cut_unstable_Y_jump',
)
SCALAR_INPUTS = (
    'root_even96_raw',
    'frozen_common_high_Hminus4over3',
    'rough_stable_Hminus3over2',
    'low_ordinary_raw_L2',
    'low_exactly_S_inverse_transformed_L2',
    'physical_outer_height_dotH_two_minus5over6',
    'physical_Robin_Hminus5over6',
    'physical_independent_mean_before_chart',
)
JUMP_INPUTS = (
    'all_low_jumps_weighted_step_body',
    'all_low_jumps_raw_endpoint_sum',
    'all_low_jumps_original_cell_tail',
)
DATA_INPUT_ORDER = SCALAR_INPUTS + SEVEN_PORTS + JUMP_INPUTS
NEW_RECORD_ORDER = (
    'actual_source_weighted_body_rhs_upper',
    'actual_source_raw_endpoint193_rhs_upper',
    'actual_source_complete_WPN_pair_rhs_upper',
    'actual_source_original_radial_tail_rhs_upper',
)
GEOMETRY_RECORDS = (
    'same_original_S_operator_upper',
    'same_original_cell_h_over_pi_S_operator_upper',
    'same_original_cell_h_over_pi_upper',
)
WOBSA_GRAPHS = (
    'complete_outer_low_and_affine_rows',
    'complete_positive_head_and_outer_columns',
    'complete_genuine_288_shell',
    'complete_genuine_and_rough_observations',
    'complete_zero_IVP_rows',
    'complete_zero_stable_root_receiver_rows',
)
DATA_QUALIFICATIONS = (
    'same_selected_member_and_fixed_physical_eta0',
    'complete_actual_positive_interval_and_true_root',
    'original_moving_angular_measure_and_physical_frequency',
    'complete_raw_even_mean_in_all_ordinary_sources',
    'physical_Robin_and_mean_not_replaced_by_derivative_norms',
    'physical_height_in_original_normalized_nonmean_units',
    'all_seven_original_Y_or_ordinary_source_units_retained',
    'seven_port_B_excludes_the_same_physical_exterior_affine_data',
    'unknown_outer_low_b_is_operator_input_not_RHS_data',
    'all_actual_raw_low_jumps_and_endpoint_signs_retained',
    'same_physical_cause_not_counted_in_two_input_representations',
    'no_general_L2_function_was_given_an_endpoint_trace',
)
ADMISSION_QUALIFICATIONS = (
    'whole_WOBSA_science_execution_manifest_and_all37_records_verified',
    'whole_WOBSA_six_old_receipts_and_all_scopes_verified',
    'whole_negative_given_head_graph_and_execution_verified',
    'whole_same_D_boundary_science_execution_and_all10_records_verified',
    'same_original_WOB_operator_and_S_verified',
    'same_selected_member_not_promoted_to_uniform_family',
    'actual_data_all_evidence_and_zero_identities_verified',
    'original_24480_cells_and_exact_q_floor_verified',
)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def missing_actual_data(packet):
    """Metadata-only missing list; absence is never an exact zero.

    This helper itself is safe before the numerical runtime is imported.
    It does not prove any scientific identity and does not synthesize a
    packet, a scalar ball, a manifest, or a future successful result.
    """
    if not isinstance(packet, dict):
        return ['complete_actual_source_packet']
    missing = []
    for key in ('kind', 'complete', 'source_identity',
                'selected_member_identity', 'norm_records', 'evidence_ids',
                'zero_identity_keys', 'qualifications'):
        if key not in packet:
            missing.append(key)
    records = packet.get('norm_records', {})
    evidence = packet.get('evidence_ids', {})
    if not isinstance(records, dict):
        missing.append('norm_records_mapping')
        records = {}
    if not isinstance(evidence, dict):
        missing.append('evidence_ids_mapping')
        evidence = {}
    for key in DATA_INPUT_ORDER:
        if key not in records:
            missing.append('norm_records.' + key)
        if not isinstance(evidence.get(key), str) or not evidence[key]:
            missing.append('evidence_ids.' + key)
    qualifications = packet.get('qualifications', {})
    if not isinstance(qualifications, dict):
        missing.append('qualifications_mapping')
        qualifications = {}
    for key in DATA_QUALIFICATIONS:
        if qualifications.get(key) is not True:
            missing.append('qualifications.' + key)
    return missing


def one_located_jump_tail_upper(api, core, left_length_upper,
                               right_length_upper, cell_length_lower,
                               original_S_jump_norm_upper):
    """S.7, after the owner proves this jump lies in this ORIGINAL cell.

    The endpoint numbers are directed bounds on a=tau-l and b=r-tau,
    and the positive denominator is a lower bound on a+b.  Their
    correlation is not discarded from the exact formula: only the final
    positive expression receives these separate directed enclosures.
    A midpoint cell assignment or a certification-cut cell is inadmissible.
    """
    values = (left_length_upper, right_length_upper,
              original_S_jump_norm_upper)
    require(all(value.is_finite() and bool(value >= api.zero)
                for value in values), 'nonnegative jump and true lengths')
    require(cell_length_lower.is_finite()
            and bool(cell_length_lower > api.zero),
            'positive lower bound on the same original fine-cell length')
    a, b, j = (core.upper(api, value) for value in values)
    return core.upper(api, core.root(
        api, core.upper(api, a*b/cell_length_lower))*j)


def complete_physical_source_pair(api, core, admitted, wobsa, negative,
                                  reference_boundary, geometry, packet, emit):
    """Four new bounds S.9--S.12 for one genuinely complete physical RHS.

    emit(name, upper, 'upper') must write the entire interval, parse it
    back, explicitly test contains(original upper), and return its upper
    endpoint.  The owner keeps the full completed prefix on every failure.
    No 224-record or 32-record future response is an input to this target.
    All exact-zero input bounds require their own accepted proof identity.
    """
    require(isinstance(admitted, dict) and 'private_token' in admitted,
            'complete public owner admission')
    for flag in ADMISSION_QUALIFICATIONS:
        require(admitted.get(flag) is True, 'required whole admission: ' + flag)
    require(not missing_actual_data(packet),
            'actual source data missing: ' + ', '.join(missing_actual_data(packet)))
    require(packet['kind'] == DATA_KIND and packet['complete'] is True,
            'complete actual physical source packet, not a proposal')
    require(packet['selected_member_identity']
            == admitted['selected_member_identity'],
            'every source is for this exact selected member')
    require(bool(packet['source_identity']), 'nonempty exact source identity')
    require(set(packet['norm_records']) == set(DATA_INPUT_ORDER),
            'all18 source quantities in exact units; no unknown slot')
    require(set(packet['zero_identity_keys']).issubset(DATA_INPUT_ORDER),
            'zero identities refer only to declared inputs')

    require(wobsa['kind'] == WOBSA_KIND
            and (wobsa['run_id'], wobsa['run_attempt']) == WOBSA_RUN
            and wobsa['complete'] is True and wobsa['proved'] is True
            and wobsa['failure'] is None and wobsa['actual_returncode'] == 0
            and wobsa['stage'] == 'complete'
            and len(wobsa['gates']) == 18
            and all(gate['passed'] is True for gate in wobsa['gates'])
            and wobsa['completed_targets'] == list(WOBSA_GRAPHS)
            and set(wobsa['complete_new_graphs']) == set(WOBSA_GRAPHS),
            'complete immutable WOBSA six graphs and all18 gates')
    require(sum(len(value['complete_new_records']) for value in
                wobsa['complete_new_graphs'].values()) == 37
            and len(wobsa['copied_original_scalar_records']) == 42,
            'all37 WOBSA and42 prior record objects retained')
    prior_scope = wobsa['retained_scope']
    for flag in (
            'all_six_complete_original_receipts_read_without_old_math',
            'full_low193_rows_and_independent_even_mean_retained',
            'same_selected_member_same_physical_eta0',
            'Ni_and_stable_inverse_in_original_right_order_once',
            'independent_physical_coordinates_receive_no_Ni',
            'original_WHVA_4096_strict_sufficient_test_false',
            'original_WHVA_no_resolvent_admitted'):
        require(prior_scope[flag] is True, 'complete WOBSA scope: ' + flag)
    for flag in ('finite_signed_inverse_proved', 'full_incoming_inverse_proved',
                 'nonlinear_background_or_surface_proved'):
        require(prior_scope[flag] is False, 'unpaid WOBSA scope: ' + flag)
    require(wobsa['actual_progress']['old_scientific_calls'] == 0
            and wobsa['actual_progress']['old_targets_recomputed'] == 0,
            'original successful production was not repeated')

    require(negative['kind'] == NEGATIVE_KIND and negative['complete'] is True
            and negative['failure'] is None
            and negative['input_order'] == list(SEVEN_PORTS)
            and all(len(row) == 7 for row in negative['response_rows'].values())
            and negative['all_affine_jump_inputs_are_in_new_Y_units'] is True
            and negative['ordinary_and_raw_jump_Bessel_conversions_paid'] is True
            and negative['high_to_head_uses_complete_original97_to288_shell_and1153_factor'] is True,
            'whole original seven-port graph including high-to-low shell')
    require(negative['exterior_input_order'] == [
                'low_nonmean_y_Hminus5over6',
                'independent_outer_height_dotH_two_minus5over6',
                'ordinary_Robin_Hminus5over6', 'independent_mean_residual'],
            'physical exterior source units before the full chart')
    reference_identity = admitted['reference_identity']
    require(reference_boundary['kind'] == REFERENCE_KIND
            and reference_boundary['complete'] is True
            and reference_boundary['proved'] is True
            and reference_boundary['failure'] is None
            and reference_boundary['actual_returncode'] == 0
            and reference_boundary['saved_record_count'] == 10
            and len(reference_boundary['completed_targets']) == 2
            and reference_boundary['reference_identity'] == reference_identity,
            'complete same D/S right97 and joint193 boundary certificate')
    lift = reference_boundary['boundary_lift']
    for flag in ('complete_reference_weighted_right97_lift_proved',
                 'same_original_D_S_and_true_root',
                 'true_reference_independent_mean_retained',
                 'complete_body_root97_outer96_and_atoms193_retained'):
        require(lift[flag] is True, 'D constant mean subcolumn: ' + flag)
    require(geometry['reference_identity'] == reference_identity
            and geometry['fine_cell_count'] == 24480
            and geometry['fine_refinement'] == 160
            and geometry['same_original_piecewise_constant_S'] is True
            and geometry['actual_true_cell_lengths'] is True
            and geometry['certification_cuts_not_substituted'] is True
            and geometry['q_floor_at_least_one_eighth'] is True
            and set(geometry['new_or_readonly_records']) == set(GEOMETRY_RECORDS),
            'true original24480 S/h descriptors, never numerical balance')

    def up(value):
        return core.upper(api, value)

    def read(record):
        value = core.saved_upper(api, record)
        require(value.is_finite() and bool(value >= api.zero),
                'whole saved nonnegative upper endpoint')
        return up(value)

    def graph(graph_name, record_name):
        return read(wobsa['complete_new_graphs'][graph_name][
            'complete_new_records'][record_name])

    data = {name: read(packet['norm_records'][name]) for name in DATA_INPUT_ORDER}
    for name, value in data.items():
        if bool(value == api.zero):
            require(name in packet['zero_identity_keys'],
                    'an exact zero must have its own proof identity: ' + name)
    old = wobsa['copied_original_scalar_records']
    v0, t0, Lstar = (read(old[name]) for name in ('C_V0', 'C_R0', 'L_star'))
    source_graph = 'complete_genuine_and_rough_observations'
    Phi = graph(source_graph, 'complete_Phi_upper')
    Phir = graph(source_graph, 'complete_rough_head_observation_upper')
    Yr = graph(source_graph, 'complete_rough_outer_observation_upper')
    row_graph = 'complete_outer_low_and_affine_rows'
    KRH = graph(row_graph, 'complete_high_outer_row_upper')
    affine = [graph(row_graph, name) for name in (
        'complete_affine_fB_low_pair_upper',
        'complete_affine_rB_low_pair_upper',
        'complete_affine_rC_low_pair_upper')]
    Bx = graph('complete_zero_IVP_rows', 'complete_B0_high_body_row_upper')
    Dx = graph('complete_zero_IVP_rows', 'complete_D0_high_endpoint_row_upper')
    dB = read(reference_boundary['new_records']['reference_weighted_right97_body_upper'])
    scale, mesh_scale, mesh_length = (
        read(geometry['new_or_readonly_records'][name]) for name in GEOMETRY_RECORDS)
    physical = [data[name] for name in SCALAR_INPUTS[5:8]]
    beta = [read(value) for value in negative['exterior_affine_Y_output_coefficients']]
    require(len(beta) == 4, 'b/height/Robin/mean all four actual affine coefficients')
    alpha = [data[name] for name in SEVEN_PORTS]
    alpha[3] = up(alpha[3] + sum((beta[i+1]*physical[i]
                                 for i in range(3)), api.zero))
    C_row = [read(value) for value in
             negative['response_rows']['entire_positive_raw_L2r_Hminus1']]
    Y_row = [read(value) for value in negative['response_rows']['body_Y_sup']]
    Cp = up(sum((C_row[i]*alpha[i] for i in range(7)), api.zero))
    Yp = up(sum((Y_row[i]*alpha[i] for i in range(7)), api.zero))
    shell_source = up(api.rational(1153)*Lstar*Cp)
    C, X, U, G, GS = (data[name] for name in SCALAR_INPUTS[:5])
    Qp = up(shell_source + G + api.rational(8)*GS)
    JB, JE, JT = (data[name] for name in JUMP_INPUTS)
    body = up(dB*C + scale*(Bx*X + v0*Phir*U + v0*Qp) + JB)
    endpoint = up(C + Dx*X + (t0*Phir+KRH*Yr)*U
                  + sum((affine[i]*physical[i] for i in range(3)), api.zero)
                  + api.rational(4)*KRH*Yp + t0*Qp + JE)
    tail = up(mesh_scale*(Phi*X + Phir*U + shell_source + G)
              + mesh_length*GS + JT)
    records = []
    final = {}

    def save(name, value):
        require(name == NEW_RECORD_ORDER[len(records)],
                'complete ordered four-target prefix')
        point = up(value)
        saved = emit(name, point, 'upper')
        require(saved.is_finite() and bool(saved >= point),
                'whole saved interval contains original upper and is reread')
        records.append(name)
        final[name] = saved
        return saved

    body_saved = save(NEW_RECORD_ORDER[0], body)
    endpoint_saved = save(NEW_RECORD_ORDER[1], endpoint)
    save(NEW_RECORD_ORDER[2], core.hypot(api, body_saved, endpoint_saved))
    save(NEW_RECORD_ORDER[3], tail)
    require(records == list(NEW_RECORD_ORDER), 'all four actual source quantities')
    return {
        'kind': KIND,
        'reference_identity': reference_identity,
        'selected_member_identity': admitted['selected_member_identity'],
        'source_identity': packet['source_identity'],
        'complete_actual_input_order': list(DATA_INPUT_ORDER),
        'complete_actual_input_evidence_ids': dict(packet['evidence_ids']),
        'complete_new_record_order': records,
        'complete_new_record_count': 4,
        'complete_actual_source_pair_upper_bounds_proved': True,
        'original_finite_WPN_RHS_upper_record': NEW_RECORD_ORDER[2],
        'original_joint_finite_and_tail_WPN_RHS_upper_record': NEW_RECORD_ORDER[2],
        'original_radial_tail_WPN_RHS_upper_record': NEW_RECORD_ORDER[3],
        'same_24480_original_projection_and_independent_endpoint193_retained': True,
        'all_physical_height_mean_and_high_particular_paths_retained': True,
        'same_cause_two_paths_combined_before_norm_without_false_orthogonality': True,
        'all_actual_data_zero_claims_have_explicit_original_identity': True,
        'low_jump_step_and_negative_endpoint_terms_retained': True,
        'arbitrary_L2_rhs_differentiated_or_traced': False,
        'complete_physical_inverse_or_224_port_table_proved': False,
        'complete_32_WPN_response_table_proved': False,
        'particular_signed_solution_or_response_error_proved': False,
        'independent_high_baseline_included_in_return_output': False,
        'rough_high_baseline_upgraded_to_raw_L2': False,
        'original_finite_rho_or_WJK_F_gate_proved': False,
        'negative_connection_waist_or_parameter_Schur_proved': False,
        'nonlinear_background_or_topic_completion_proved': False,
        'old_completed_scientific_targets_recomputed': 0,
        'new_final_upper_values': final,
    }

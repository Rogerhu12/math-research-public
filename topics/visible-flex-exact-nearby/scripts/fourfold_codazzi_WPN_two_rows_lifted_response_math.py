"""Both original WPN right-side rows through the exact WOB source lifting.

Pure definitions: no IO, numerical imports, old producer or hypothetical input.
Actual public execution is permitted only after the entire same-operator
physical gate and 14-by-16 port table have been completed and admitted whole.
The output is a new 16-by-2 response bound, not a particular RHS magnitude.
"""

KIND = 'complete_R141_WPN_both_rows_lifted_response_v1'
PORT_KIND = 'complete_R141_actual_physical_gate_original_port_response_v1'
REFERENCE_KIND = 'complete_fixed_WVC_reference_boundary_lifts_v1'
WHVA_KIND = 'complete_zero_volterra_positive_head_mesh_v1'
RHS_ORDER = ('finite', 'tail')
PORT_INPUT_ORDER = (
    'root_stable_Y_port',
    'collar_ordinary_Hminus2over3_source',
    'body_ordinary_Hminus2over3_source',
    'body_outer_mean_head_and_Y_weighted_jumps',
    'collar_Y_weighted_affine_jumps',
    'cut_stable_Y_jump',
    'cut_unstable_Y_jump',
    'low_ordinary_raw_L2_source',
    'low_transformed_L2_source_before_one_S_inverse',
    'independent_low_root_even96_raw_boundary',
    'independent_already_charted_right97_source',
    'physical_outer_height_dotH_two_minus5over6',
    'physical_ordinary_Robin_Hminus5over6_residual',
    'physical_independent_mean_residual_before_chart',
)
OUTPUT_CODES = (
    'right97', 'outer96', 'low_body', 'low_root97', 'low_outer96',
    'low_atoms193', 'low_complete', 'high_cut_stableY', 'high_cut_unstableY',
    'high_root_unstableY', 'high_bodyY', 'high_collarY', 'high_globalY',
    'high_raw_Hminus1', 'high_primitive_L2', 'high_root_mixed',
)
OUTPUT_QUALIFICATIONS = (
    'reference right97 of the regular lifted ODE state w; not a trace of general a',
    'original independent outer chart coordinate Theta b',
    'complete original transformed L2 body S a, including the rough RHS lift',
    'original independent d97, recovered from the legal root trace of w',
    'original independent Theta b96, recovered from the legal outer trace of w',
    'joint original independent d97 plus Theta b96, not traces of arbitrary a',
    'full WPN unknown norm: transformed body plus original independent193 coordinates',
    'zero-independent-high-port return: incoming stable cut Y',
    'zero-independent-high-port return: incoming unstable cut Y',
    'zero-independent-high-port return: true root outgoing Y',
    'zero-independent-high-port return: body Y supremum',
    'zero-independent-high-port return: collar Y supremum',
    'zero-independent-high-port return: full interval Y supremum',
    'zero-independent-high-port return: raw L2_dr H_phi^-1',
    'zero-independent-high-port return: nonmean primitive L2_dr L2_phi',
    'zero-independent-high-port return: true raw root H_phi^-2/3 times H_phi^-1',
)
COMPLETE_RECORD_COUNT = 32


def require(ok, message):
    if not ok:
        raise ValueError(message)


def record_order():
    return ['wpn_%s_%s_upper' % (rhs, code)
            for rhs in RHS_ORDER for code in OUTPUT_CODES]


def complete_two_row_response(api, core, admitted, ports, whva,
                              reference_boundary, read_saved_port_upper, emit):
    """Compute (L.20)--(L.22) using five prior input columns, whole readback.

    `ports` is the genuine complete pure-math metadata retained in a complete
    public 224-record result.  The owner binds its scientific, execution,
    manifest, same-family scope and the successful entire58 gate before this
    call.  `read_saved_port_upper(column, code)` reads the upper endpoint of
    the corresponding complete saved record; it never invokes the producer.

    `whva` and `reference_boundary` are the two complete immutable scientific
    objects, not selected scalar replacements.  The owner also binds their
    whole executions and original identities.  The WHVA mesh gate remains
    false: only its already proved complete coefficient/source bounds enter.

    emit(name, new_upper, 'upper') writes the whole ball, rereads it and checks
    contains(new_upper) before returning the saved upper endpoint.  A real
    failure leaves the actual completed finite-then-tail prefix in the owner.
    """
    require('private_token' in admitted
            and admitted['same_original_WOB_operator_and_S_verified'] is True
            and admitted['whole_prior_58_and_224_results_and_executions_verified'] is True
            and admitted['whole_WHVA_and_reference_boundary_executions_verified'] is True
            and admitted['original_24480_projection_and_q_floor_verified'] is True,
            'whole same-object prior admission; no missing future result')
    reference_identity = admitted['reference_identity']
    prior_order = ['port_%02d_%s_upper' % (column, code)
                   for column in range(14) for code in OUTPUT_CODES]
    require(ports['kind'] == PORT_KIND
            and ports['reference_identity'] == reference_identity
            and ports['input_order'] == list(PORT_INPUT_ORDER)
            and ports['output_order'] == list(OUTPUT_CODES)
            and ports['complete_new_record_order'] == prior_order
            and ports['complete_new_record_count'] == 224,
            'all original14 input and16 output rows in their exact complete order')
    for flag in (
            'complete_original_seven_Y_ports_and_eight_high_rows_proved',
            'complete_four_additional_low_or_chart_columns_proved',
            'complete_three_physical_height_Robin_mean_columns_proved',
            'all193_low_observations_and_both_split_endpoints_retained',
            'full_mean_source_and_same_original_four_low_source_roles_retained',
            'reference_right97_and_actual_outer96_unknowns_kept_separate'):
        require(ports[flag] is True, 'complete prior port qualification: '+flag)
    for flag in (
            'rough_high_upgraded_to_raw_L2', 'whole_high_unknown_truncated',
            'independent_source_columns_declared_orthogonal',
            'independent_raw_low_affine_jump_lifts_supplied_by_this_result',
            'nu_or_other_actual_RHS_magnitudes_supplied_by_this_result',
            'physical_density_mean_or_theta_readout_conversion_supplied',
            'original_WPN_finite_or_radial_tail_RHS_assembled',
            'old_WJK_F_replaced_by_actual_GH_without_paying_difference',
            'original_finite_rho_bridge_proved',
            'negative_connection_or_nonlinear_family_proved',
            'topic_completion_proved'):
        require(ports[flag] is False, 'all original unpaid prior scope retained: '+flag)
    require(ports['old_completed_scientific_targets_recomputed'] == 0,
            'prior port result did not recompute old targets')
    require(whva['kind'] == WHVA_KIND and whva['complete'] is True
            and whva['failure'] is None and whva['stage'] == 'complete'
            and len(whva['gates']) == 14
            and all(gate['passed'] is True for gate in whva['gates'])
            and whva['parameters']['head_dimension'] == 193
            and whva['parameters']['first_high_index'] == 97
            and whva['complete_body_source_choice']['selected'] == 'A_b_from_L'
            and whva['resolvent_admitted'] is False
            and whva['strict_mesh_gate']['passed'] is False,
            'complete WHVA old bounds retained with their original false mesh gate')
    require(whva['copied_original_scope'][
                'given_complete_head_positive_high_inverse_and_root_graph_proved'] is True
            and whva['copied_original_scope'][
                'independent_even_mean_and_all_head_and_affine_source_ports_retained'] is True
            and whva['retained_scope']['ordinary_dr_fixed_raw_fiber'] is True
            and whva['retained_scope']['original_chart_b_not_identified_with_raw_endpoint'] is True,
            'same complete raw coefficient and ordinary source norms')
    require(reference_boundary['kind'] == REFERENCE_KIND
            and reference_boundary['complete'] is True
            and reference_boundary['proved'] is True
            and reference_boundary['failure'] is None
            and reference_boundary['actual_returncode'] == 0
            and reference_boundary['saved_record_count'] == 10
            and len(reference_boundary['completed_targets']) == 2
            and reference_boundary['reference_identity'] == reference_identity,
            'complete exact same D/S reference boundary result')
    reference_scope = reference_boundary['boundary_lift']
    require(reference_scope['complete_reference_weighted_right97_lift_proved'] is True
            and reference_scope['same_original_D_S_and_true_root'] is True
            and reference_scope['true_reference_independent_mean_retained'] is True
            and reference_scope['complete_body_root97_outer96_and_atoms193_retained'] is True,
            'constant even lift uses the same q as the exact reference mean subcolumn')

    def up(value):
        return core.upper(api, value)

    def read(record):
        return core.saved_upper(api, record)

    old = whva['new_records']
    generator, collar, body, root_length = (
        read(old[name]) for name in ('A_infty', 'A_c', 'A_b_from_L', 'C_R0'))
    constant_even = read(reference_boundary['new_records'][
        'reference_weighted_right97_body_upper'])
    # The immutable exact floor q>=1/8 (and collar q=1) gives this rational
    # bound analytically; no old or new q extremum is evaluated here.
    inverse_S = api.rational(8)
    coefficients = {}
    for code in OUTPUT_CODES:
        values = {}
        for column in (1, 2, 7, 9, 10):
            value = read_saved_port_upper(column, code)
            require(value.is_finite() and bool(value >= api.zero),
                    'complete saved prior upper for %s/%s' % (column, code))
            values[column] = up(value)
        ordinary = up(collar*values[1]+body*values[2]+generator*values[7])
        body_coefficient = up(inverse_S*ordinary)
        endpoint_even_coefficient = up(root_length*ordinary+values[9])
        endpoint_other_coefficient = values[10]
        if code in ('low_body', 'low_complete'):
            # Only the transformed L2 body receives S k.  The original
            # independent d97/b96 are recovered from w, never from F traces.
            body_coefficient = up(body_coefficient+api.one)
            endpoint_even_coefficient = up(endpoint_even_coefficient+constant_even)
        coefficients[code] = (body_coefficient, endpoint_even_coefficient,
                              endpoint_other_coefficient)

    records = []
    final_values = {rhs: {} for rhs in RHS_ORDER}
    for rhs in RHS_ORDER:
        for code in OUTPUT_CODES:
            h, c, u = coefficients[code]
            if rhs == 'finite':
                # Three mutually orthogonal INPUT blocks: f_cell, raw
                # endpoint even96, raw endpoint odd96 plus moving mean.
                value = core.hypot(api, core.hypot(api, h, c), u)
            else:
                value = h
            name = 'wpn_%s_%s_upper' % (rhs, code)
            require(name == record_order()[len(records)],
                    'complete finite-then-tail response order')
            point = up(value)
            saved = emit(name, point, 'upper')
            require(saved.is_finite() and bool(saved >= point),
                    'whole saved record contains the new upper and is reread')
            records.append(name)
            final_values[rhs][code] = saved
    require(records == record_order() and len(records) == COMPLETE_RECORD_COUNT,
            'all16 output observations for both complete original RHS rows')
    return {
        'kind': KIND,
        'reference_identity': reference_identity,
        'input_order': list(RHS_ORDER),
        'input_qualifications': [
            'original finite f_f=(f_cell,raw endpoint193), full Euclidean Hilbert norm',
            'original complete radial-meanzero g_t in Q_N L2, with N=24480'],
        'output_order': list(OUTPUT_CODES),
        'output_qualifications': list(OUTPUT_QUALIFICATIONS),
        'complete_new_record_order': records,
        'complete_new_record_count': COMPLETE_RECORD_COUNT,
        'complete_both_WPN_row_operator_responses_proved': True,
        'full_WOB_square_inverse_via_completed_physical_gate_and_exact_lifting': True,
        'both_original_WPN_rows_retained_before_source_lifting': True,
        'arbitrary_L2_RHS_differentiated_or_traced': False,
        'original193_coordinates_recovered_from_regular_w_not_arbitrary_a': True,
        'reconstructed_body_and_independent_atoms_have_original_direct_sum_norm': True,
        'original_24480_cell_projection_retained': True,
        'independent_low_jump_step_and_endpoint_lifting_identity_proved': True,
        'actual_low_jump_source_norms_supplied_by_this_result': False,
        'actual_nu_or_physical_source_RHS_norms_supplied_by_this_result': False,
        'particular_complete_finite_and_tail_RHS_enclosures_supplied': False,
        'particular_signed_solution_or_approximation_computed': False,
        'independent_high_baseline_included_in_return_output': False,
        'rough_baseline_upgraded_to_whole_raw_Hminus1': False,
        'physical_density_mean_or_theta_readout_conversion_supplied': False,
        'old_finite_rho_or_paired_Neumann_gate_proved': False,
        'old_WJK_F_replaced_without_its_complete_difference': False,
        'negative_connection_or_nonlinear_family_proved': False,
        'topic_completion_proved': False,
        'old_completed_scientific_targets_recomputed': 0,
        'private_readback_values': final_values,
    }

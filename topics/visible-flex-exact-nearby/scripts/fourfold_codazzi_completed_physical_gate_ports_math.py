"""R141: original seven rough high ports after the actual physical gate.

Pure definitions only. No IO, numerical imports, old producers or fallback.
The future owner admits all whole inputs, then passes the genuinely paid
B4--B21 result and readback gap. No current low/gate result is fabricated.
All new final bounds are saved and reread through emit(name, value, bound).
"""

KIND = 'complete_R141_actual_physical_gate_original_port_response_v1'
WEIGHTED_KIND = 'complete_actual_GH_radially_weighted_head_response_v1'
NEGATIVE_KIND = 'actual_full_real_delta_negative_one_positive_given_head_graph_v1'
SEVEN_PORTS = (
    'root_stable_Y_port',
    'collar_ordinary_Hminus2over3_source',
    'body_ordinary_Hminus2over3_source',
    'body_outer_mean_head_and_Y_weighted_jumps',
    'collar_Y_weighted_affine_jumps',
    'cut_stable_Y_jump',
    'cut_unstable_Y_jump',
)
NEGATIVE_ROWS = (
    'body_incoming_stable_cut_Y_port',
    'collar_incoming_unstable_cut_Y_port',
    'full_root_outgoing_unstable_Y_port',
    'body_Y_sup',
    'collar_Y_sup',
    'entire_positive_Y_sup',
    'entire_positive_raw_L2r_Hminus1',
    'entire_positive_primitive_L2r_L2phi',
)
ADDITIONAL_INPUTS = (
    'low_ordinary_raw_L2_source',
    'low_transformed_L2_source_before_one_S_inverse',
    'independent_low_root_even96_raw_boundary',
    'independent_already_charted_right97_source',
    'physical_outer_height_dotH_two_minus5over6',
    'physical_ordinary_Robin_Hminus5over6_residual',
    'physical_independent_mean_residual_before_chart',
)
INPUT_ORDER = SEVEN_PORTS + ADDITIONAL_INPUTS
OUTPUT_CODES = (
    'right97', 'outer96', 'low_body', 'low_root97', 'low_outer96',
    'low_atoms193', 'low_complete', 'high_cut_stableY', 'high_cut_unstableY',
    'high_root_unstableY', 'high_bodyY', 'high_collarY', 'high_globalY',
    'high_raw_Hminus1', 'high_primitive_L2', 'high_root_mixed',
)
OUTPUT_QUALIFICATIONS = (
    'reference right97 datum (Theta times Robin96, independent moving mean)',
    'b=Theta low even96 at the true outer endpoint',
    'ordinary L2_dr transformed low body S h_L',
    'true raw root odd96 and independent moving mean',
    'Theta weighted true outer even96',
    'joint original root97 plus outer96 observations',
    'Hilbert direct sum of transformed low body and joint193 observations',
    'original negative-window body incoming stable cut Y',
    'original negative-window collar incoming unstable cut Y',
    'original negative-window true root outgoing unstable Y',
    'original body sup of Y=M^-1 Z',
    'original collar sup of Y=M^-1 Z',
    'original entire positive interval sup of Y=M^-1 Z',
    'entire positive high raw L2_dr H_phi^-1; no mean in the high state',
    'entire positive high nonmean primitive L2_dr L2_phi',
    'true high root raw mixed H_phi^-2/3 times H_phi^-1, both components',
)
RECEIVERS = ('body', 'root', 'outer', 'atoms')
GAP_RECORD = 'actual_internal_body_gap_lower'
EXPECTED_GATE_KIND = 'complete_low_high_and_physical_outer_scalar_gate_v1'
COMPLETE_RECORD_COUNT = len(INPUT_ORDER) * len(OUTPUT_CODES)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def record_order():
    return ['port_%02d_%s_upper' % (column, code)
            for column in range(len(INPUT_ORDER)) for code in OUTPUT_CODES]


def complete_original_ports(api, core, admitted, closed, weighted,
                            read_saved_gate_endpoint, emit):
    """Produce the 16-by-14 matrix only after the actual physical gate.

    `admitted` is the existing complete same-operator scalar admission.
    `closed` is the genuinely completed B4--B21 pure result (or its exact
    owner-restored readback representation), never a synthetic trial.
    The owner verifies the complete whole scientific/execution/manifest
    binding and all gates BEFORE constructing these private arguments.

    read_saved_gate_endpoint(name, bound) returns the actual saved endpoint
    of the paid 58-record result. It must not reevaluate the older target.
    `weighted` is the whole actual five-record result with the same identity.
    A previously proved gate using the older GH4 upper remains a valid gate;
    this module explicitly binds the weighted high leg for the NEW RHS
    response. No old GH4 identity is renamed or overwritten.
    """
    require('private_token' in admitted, 'complete original scalar admission')
    require(closed['kind'] == EXPECTED_GATE_KIND
            and closed['same_actual_internal_gate_passed'] is True
            and closed['same_actual_physical_outer_gate_passed'] is True
            and closed['actual_positive_given_root_input_inverse_proved'] is True
            and closed['complete_branch'] == 'complete_same_positive_physical_boundary_inverse_gate'
            and len(closed['complete_new_record_order']) == 58
            and closed['reference_identity'] == admitted['reference_identity']
            and closed['all193_output_atoms_retained'] is True
            and closed['root97_and_outer96_receivers_retained_separately'] is True,
            'genuinely paid complete58 same actual internal and physical boundary gate')
    for flag in ('actual_singularity_inferred', 'original_finite_rho_bridge_proved',
                 'old_WJK_F_replaced_without_paying_difference',
                 'full_original_seven_port_response_matrix_proved',
                 'either_original_WPN_RHS_proved', 'negative_connection_or_nonlinear_family_proved',
                 'topic_completion_proved'):
        require(closed[flag] is False, 'the exact scope of the prior gate: ' + flag)
    require(weighted['kind'] == WEIGHTED_KIND and weighted['complete'] is True
            and weighted['proved'] is True and weighted['actual_returncode'] == 0
            and weighted['failure'] is None and weighted['saved_record_count'] == 5
            and len(weighted['completed_targets']) == 5
            and weighted['reference_identity'] == admitted['reference_identity']
            and weighted['weighted_response']['complete_actual_head_to_high_weighted_response_proved'] is True
            and weighted['weighted_response']['same_full_family_mean_source_column_retained'] is True
            and weighted['weighted_response']['original_infinite_high_unknown_truncated'] is False,
            'same complete actual weighted head response, retained with its true identity')
    negative = admitted['negative']
    require(negative['kind'] == NEGATIVE_KIND and negative['complete'] is True
            and negative['input_order'] == list(SEVEN_PORTS)
            and set(negative['response_rows']) == set(NEGATIVE_ROWS)
            and all(len(negative['response_rows'][name]) == 7 for name in NEGATIVE_ROWS)
            and negative['all_affine_jump_inputs_are_in_new_Y_units'] is True
            and negative['ordinary_and_raw_jump_Bessel_conversions_paid'] is True
            and negative['root_input_and_output_mixed_Bessel_conversions_paid'] is True,
            'all seven original negative-window ports and all eight complete rows')
    require(negative['exterior_input_order'] == [
                'low_nonmean_y_Hminus5over6', 'independent_outer_height_dotH_two_minus5over6',
                'ordinary_Robin_Hminus5over6', 'independent_mean_residual']
            and negative['exterior_mean_input_order'] == [
                'full_nonmean_y_Hminus5over6', 'independent_outer_height_dotH_two_minus5over6',
                'independent_mean_residual'], 'whole physical chart input units')
    source = closed['source_receivers']
    require(set(source) == set(core.ROLES) and all(
                all(receiver in source[role] for receiver in RECEIVERS)
                for role in core.ROLES), 'all four original complete source roles remain present')

    def up(value):
        return core.upper(api, value)

    def read(record):
        return core.saved_upper(api, record)

    zero, one = api.zero, api.one
    gap = read_saved_gate_endpoint(GAP_RECORD, 'lower')
    require(gap.is_finite() and bool(gap > zero), 'actual saved strict internal gap lower')
    kappa = closed['kappa']
    require(bool(gap <= one-kappa['body']), 'saved gap has the correct direction')
    P, Q = closed['boundary']['right'], closed['boundary']['joint']
    J = closed['outer_b_poisson_low']
    inverse = closed['physical_block_inverse_majorant']
    require(len(inverse) == 2 and all(len(row) == 2 for row in inverse),
            'complete two-by-two positive inverse majorant')
    inverse = tuple(tuple(up(value) for value in row) for row in inverse)
    ah = up(read_saved_gate_endpoint('actual_physical_high_to_right97_upper', 'upper'))
    dC = admitted['delta_C']
    g0 = source['ordinary_raw_low_source']
    gS = source['transformed_low_source']
    gC = source['centre_high0_return_source']
    l160 = core.root(api, api.rational(1+16*160*160))
    l288 = core.root(api, api.rational(1+16*288*288))
    finite_return = {name: up(l160*gC[name]+l288*g0[name]*dC) for name in RECEIVERS}
    rows = {name: [read(value) for value in negative['response_rows'][name]] for name in NEGATIVE_ROWS}
    outer = negative['actual_complete_negative_order_outer_constants']
    beta = [read(value) for value in negative['exterior_affine_Y_output_coefficients']]
    mean = [read(value) for value in negative['exterior_mean_output_coefficients']]
    Ba, Ca = read(outer['independent_Robin_multiplier']), read(outer['independent_mean_multiplier'])
    UB, VB = read(outer['negative_DN_fB_to_d']), read(outer['negative_DN_fB_to_mean'])
    physical_g = (
        core.hypot(api, up(Ba*UB+Ca*VB), mean[1]),
        Ba,
        core.hypot(api, Ca, mean[2]),
    )
    wr = weighted['new_records']
    HB = read(wr['actual_GH_weighted_raw_L2_from_complete_head_upper'])
    HZ = read(wr['actual_GH_weighted_body_Z_sup_from_complete_head_upper'])
    HR = read(wr['actual_GH_weighted_root_outgoing_Z_from_complete_head_upper'])
    tX = read(wr['actual_GH_weighted_outer_even_Hminus5over6_from_complete_head_upper'])
    # W.9 gives U=Sc for this particular head response, with stable-root=0.
    # Thus HR also bounds its entire collar Z-sup; no rough port is upgraded.
    head_body_Y, head_collar_Y = up(HZ/388), up(HR/388)
    head_global_Y = up(api.hull([head_body_Y, head_collar_Y]))
    head_raw_negative = up(HB/388)
    head_rows = (head_body_Y, head_collar_Y, head_collar_Y,
                 head_body_Y, head_collar_Y, head_global_Y,
                 head_raw_negative, head_raw_negative)
    root_mixed_gain = read(negative['constants']['Y_to_raw_mixed_root_output'])
    records = []

    def save(column, code, value):
        name = 'port_%02d_%s_upper' % (column, code)
        expected = record_order()[len(records)]
        require(name == expected, 'full column-major response order without omission')
        point = up(value)
        saved = emit(name, point, 'upper')
        require(saved.is_finite() and bool(saved >= point), 'whole saved containing upper readback')
        records.append(name)
        return saved

    def internal_close(seed):
        body = up(seed['body']/gap)
        result = {'body': body}
        for name in ('root', 'outer', 'atoms'):
            result[name] = up(seed[name]+kappa[name]*body)
        return result

    def column_response(column, high_input, low_seed, chart_source, root_left=False):
        # high_input lists norms in the old exact seven Y/source units.
        # Same physical source may drive several rows; no false orthogonality.
        direct_high = {name: up(sum((entry*coefficient for entry, coefficient in
            zip(high_input, rows[name])), zero)) for name in NEGATIVE_ROWS}
        initial = {name: up(low_seed[name]+finite_return[name]*
            direct_high['entire_positive_raw_L2r_Hminus1']) for name in RECEIVERS}
        base = internal_close(initial)
        if root_left:
            # Q already is the fully internally closed joint boundary lift.
            # Its restriction to (left96, right97=0) needs no second closure.
            base = {name: up(base[name]+Q[name]) for name in RECEIVERS}
        td = up(4*direct_high['body_Y_sup'])
        er = up(chart_source+ah*(td+tX*base['body']))
        eb = base['outer']
        r = save(column, 'right97', inverse[0][0]*er+inverse[0][1]*eb)
        b = save(column, 'outer96', inverse[1][0]*er+inverse[1][1]*eb)
        low = {}
        for name, code in (('body', 'low_body'), ('root', 'low_root97'),
                           ('outer', 'low_outer96'), ('atoms', 'low_atoms193')):
            low[name] = save(column, code, base[name]+P[name]*r+J[name]*b)
        save(column, 'low_complete', core.hypot(api, low['body'], low['atoms']))
        actual_high = {}
        for name, head, code in zip(NEGATIVE_ROWS, head_rows, OUTPUT_CODES[7:15]):
            actual_high[name] = save(column, code,
                direct_high[name]+head*low['body']+rows[name][3]*beta[0]*b)
        save(column, 'high_root_mixed', root_mixed_gain*core.hypot(api,
            high_input[0], actual_high['full_root_outgoing_unstable_Y_port']))

    null_seed = {name: zero for name in RECEIVERS}
    for column in range(7):
        high = [zero]*7
        high[column] = one
        column_response(column, high, null_seed, zero)
    column_response(7, [zero]*7, {name: g0[name] for name in RECEIVERS}, zero)
    column_response(8, [zero]*7, {name: gS[name] for name in RECEIVERS}, zero)
    column_response(9, [zero]*7, null_seed, zero, root_left=True)
    column_response(10, [zero]*7, null_seed, one)
    for offset in range(3):
        high = [zero]*7
        high[3] = beta[offset+1]
        column_response(11+offset, high, null_seed, physical_g[offset])
    require(records == record_order() and len(records) == COMPLETE_RECORD_COUNT == 224,
            'all14 input columns and all16 output observations complete')
    return {'kind': KIND, 'reference_identity': admitted['reference_identity'],
        'input_order': list(INPUT_ORDER), 'output_order': list(OUTPUT_CODES),
        'output_qualifications': list(OUTPUT_QUALIFICATIONS),
        'record_layout': 'column-major; port_%02d_<output-code>_upper',
        'complete_new_record_order': records, 'complete_new_record_count': 224,
        'complete_original_seven_Y_ports_and_eight_high_rows_proved': True,
        'complete_four_additional_low_or_chart_columns_proved': True,
        'complete_three_physical_height_Robin_mean_columns_proved': True,
        'all193_low_observations_and_both_split_endpoints_retained': True,
        'full_mean_source_and_same_original_four_low_source_roles_retained': True,
        'rough_high_state_window': 'L2_dr_H_phi_minus_one',
        'rough_high_upgraded_to_raw_L2': False,
        'whole_high_unknown_truncated': False,
        'independent_source_columns_declared_orthogonal': False,
        'reference_right97_and_actual_outer96_unknowns_kept_separate': True,
        'independent_raw_low_affine_jump_lifts_supplied_by_this_result': False,
        'nu_or_other_actual_RHS_magnitudes_supplied_by_this_result': False,
        'physical_density_mean_or_theta_readout_conversion_supplied': False,
        'original_WPN_finite_or_radial_tail_RHS_assembled': False,
        'old_WJK_F_replaced_by_actual_GH_without_paying_difference': False,
        'original_finite_rho_bridge_proved': False,
        'negative_connection_or_nonlinear_family_proved': False,
        'topic_completion_proved': False,
        'old_completed_scientific_targets_recomputed': 0}

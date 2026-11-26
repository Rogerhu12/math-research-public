"""The completed physical positive inverse in the original negative receivers.

Pure arithmetic and exact type checks only: no IO, numerical import, old
producer, future input synthesis, signed matrix reconstruction, or execution.
The owner admits whole completed files and saves/reads back every requested
new quantity.  Returned bounds alone are not a public scientific certificate.
"""

PORT_KIND = 'complete_R141_actual_physical_gate_original_port_response_v1'
WPN_KIND = 'complete_R141_WPN_both_rows_lifted_response_v1'
SOURCE_KIND = 'complete_actual_physical_WPN_source_pair_bounds_v1'
SOURCE_DATA_KIND = 'complete_actual_WOB_physical_source_data_v1'
OUTPUT_CODES = (
    'right97', 'outer96', 'low_body', 'low_root97', 'low_outer96',
    'low_atoms193', 'low_complete', 'high_cut_stableY', 'high_cut_unstableY',
    'high_root_unstableY', 'high_bodyY', 'high_collarY', 'high_globalY',
    'high_raw_Hminus1', 'high_primitive_L2', 'high_root_mixed',
)
NEGATIVE_GAINS = (
    'root_or_affine_jump_to_waist_density_gain',
    'ordinary_root_window_source_to_waist_density_gain',
    'strict_L1_Hminus1_source_to_waist_density_gain',
    'strict_L2_Hminus1_source_to_waist_density_gain',
)
ROOT_SOURCE_WINDOW = (
    'L2_dr_H_phi_minus_two_thirds_first_plus_'
    'L2_dr_angular_constant_second'
)
FULL_ROOT_SOURCE_WINDOWS = (
    'L2_dr_H_phi_minus_two_thirds_pair',
    'L2_dr_H_phi_minus_two_thirds_first_plus_H_phi_minus_one_second',
)
STRICT_SOURCE_WINDOWS = ('L1_dr_H_phi_minus_one_pair',
                         'L2_dr_H_phi_minus_one_pair')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, core, value):
    require(value.is_finite() and bool(value >= api.zero),
            'finite nonnegative directed norm bound')
    return core.upper(api, value)


def full_root(api, core, root_even96, root_odd96_mean,
              high_root_mixed):
    """PN.6: orthogonal Fourier/output blocks, with low mixed weights <= 1.

    high_root_mixed is ALREADY in H^-2/3 x H^-1.  No additional factor9,
    Bessel conversion, S, or Theta is used here.  Neither low argument is
    the root of an arbitrary L2 function.
    """
    c, d, z = (upper(api, core, value) for value in
               (root_even96, root_odd96_mean, high_root_mixed))
    return upper(api, core, core.hypot(api, core.hypot(api, c, d), z))


def _admit_chain(admitted, ports, wpn=None):
    require(isinstance(admitted, dict) and 'private_token' in admitted,
            'whole actual file admission')
    for name in (
            'whole_actual_low_58_224_science_execution_and_manifest_verified',
            'same_selected_DF_physical_B_Cmean_height_and_jump_rows_verified',
            'whole_original_SP_PW_science_execution_and_domains_verified'):
        require(admitted.get(name) is True, 'required identity: ' + name)
    ref = admitted['reference_identity']
    require(ports['kind'] == PORT_KIND
            and ports['reference_identity'] == ref
            and ports['complete_new_record_count'] == 224
            and ports['output_order'] == list(OUTPUT_CODES)
            and len(ports['input_order']) == 14
            and ports['complete_new_record_order'] == [
                'port_%02d_%s_upper' % (j, code)
                for j in range(14) for code in OUTPUT_CODES],
            'whole224 original columns and receiver order')
    require(ports['input_order'][9]
            == 'independent_low_root_even96_raw_boundary',
            'the actual prescribed root-even96 input')
    if wpn is not None:
        require(admitted.get(
            'whole_actual_32_WPN_science_execution_and_manifest_verified') is True,
            'whole actual32, not a future response')
        require(wpn['kind'] == WPN_KIND
                and wpn['reference_identity'] == ref
                and wpn['input_order'] == ['finite', 'tail']
                and wpn['output_order'] == list(OUTPUT_CODES)
                and wpn['complete_new_record_count'] == 32
                and wpn['complete_new_record_order'] == [
                    'wpn_%s_%s_upper' % (rhs, code)
                    for rhs in ('finite', 'tail') for code in OUTPUT_CODES]
                and wpn[
                    'full_WOB_square_inverse_via_completed_physical_gate_and_exact_lifting'
                ] is True
                and wpn[
                    'original193_coordinates_recovered_from_regular_w_not_arbitrary_a'
                ] is True
                and wpn['independent_high_baseline_included_in_return_output'] is False,
                'whole32 exact WOB inverse and original independent coordinates')


def direct_ports_to_negative_waist(api, core, admitted, ports,
                                  read_saved_port_upper,
                                  read_saved_SP_upper):
    """All14 genuine positive columns -> homogeneous-negative complete density.

    Existing224 high_root_mixed includes that column's stable input and
    complete positive feedback.  Only column9 supplies a nonzero root-even96
    datum.  The negative equation in this operator column has zero source;
    an independent physical negative source is added by the separate function.
    """
    _admit_chain(admitted, ports)
    cr = upper(api, core, read_saved_SP_upper(NEGATIVE_GAINS[0]))
    result = []
    for j in range(14):
        c = api.one if j == 9 else api.zero
        d = upper(api, core, read_saved_port_upper(j, 'low_root97'))
        z = upper(api, core, read_saved_port_upper(j, 'high_root_mixed'))
        root = full_root(api, core, c, d, z)
        result.append({
            'input_name': ports['input_order'][j],
            'root_full_mixed_upper': root,
            'complete_waist_density_upper': upper(api, core, cr*root),
        })
    return result


def physical_WPN_return_to_negative_waist(
        api, core, source_math, admitted, ports, wpn, source_pair,
        physical_packet, read_saved_WPN_upper, read_saved_source_upper,
        read_saved_SP_upper):
    """PN.10--13 for ONE actually assembled physical WOB pair.

    The32 rows give d and the zero-independent-high return.  The physical
    source identity, not an L2 trace operation, gives a(root)=Ec*cstar+Ed*d.
    The high baseline is excluded.  For the frozen common x column the
    result is its complete strong addition to the already retained baseline.
    """
    _admit_chain(admitted, ports, wpn)
    require(admitted.get(
        'whole_actual_source_pair_packet_execution_and_root_identity_verified'
    ) is True, 'actual source and F(root)=Ec*cstar, including every true seam')
    require(not source_math.missing_actual_data(physical_packet),
            'all original physical source slots, evidence and zero identities')
    require(physical_packet['kind'] == SOURCE_DATA_KIND
            and physical_packet['complete'] is True
            and source_pair['kind'] == SOURCE_KIND
            and source_pair['complete_new_record_count'] == 4
            and source_pair['complete_new_record_order']
                == list(source_math.NEW_RECORD_ORDER)
            and source_pair['complete_actual_input_order']
                == list(source_math.DATA_INPUT_ORDER)
            and source_pair['complete_actual_source_pair_upper_bounds_proved'] is True
            and source_pair['reference_identity'] == admitted['reference_identity']
            and source_pair['selected_member_identity']
                == physical_packet['selected_member_identity']
                == admitted['selected_member_identity']
            and source_pair['source_identity'] == physical_packet['source_identity']
            and source_pair['complete_actual_input_evidence_ids']
                == physical_packet['evidence_ids'],
            'same actual physical pair, selected member and source evidence')
    require(source_pair['original_finite_WPN_RHS_upper_record']
            == 'actual_source_complete_WPN_pair_rhs_upper'
            and source_pair['original_radial_tail_WPN_RHS_upper_record']
            == 'actual_source_original_radial_tail_rhs_upper',
            'original finite and complete radial-tail source scales')
    ff = upper(api, core, read_saved_source_upper(
        source_pair['original_finite_WPN_RHS_upper_record']))
    gt = upper(api, core, read_saved_source_upper(
        source_pair['original_radial_tail_WPN_RHS_upper_record']))
    c = upper(api, core, core.saved_upper(
        api, physical_packet['norm_records']['root_even96_raw']))
    if bool(c == api.zero):
        require('root_even96_raw' in physical_packet['zero_identity_keys'],
                'the physical zero root input has an exact source identity')

    def response(code):
        uf = upper(api, core, read_saved_WPN_upper('finite', code))
        ut = upper(api, core, read_saved_WPN_upper('tail', code))
        # Both pieces belong to the SAME input, so use the triangle.
        return upper(api, core, uf*ff + ut*gt)

    d = response('low_root97')
    z = response('high_root_mixed')
    root = full_root(api, core, c, d, z)
    cr = upper(api, core, read_saved_SP_upper(NEGATIVE_GAINS[0]))
    return {
        'reference_identity': admitted['reference_identity'],
        'selected_member_identity': admitted['selected_member_identity'],
        'source_identity': physical_packet['source_identity'],
        'original_finite_RHS_upper': ff,
        'original_radial_tail_RHS_upper': gt,
        'physical_root_even96_upper': c,
        'physical_root_odd96_mean_upper': d,
        'zero_stable_return_high_root_mixed_upper': z,
        'correction_full_root_mixed_upper': root,
        'correction_complete_waist_density_upper': upper(api, core, cr*root),
        'independent_high_baseline_included': False,
        'rough_baseline_given_a_mixed_root_bound': False,
        'negative_ordinary_and_impulse_sources_included': False,
    }


def add_qualified_high_baseline(api, core, returned,
                                baseline_high_root_mixed_upper):
    """One complete mixed-root high baseline, in its original qualified window.

    Do not call this with a rough H^-3/2 stable input or a whole body bound.
    The latter has no admitted root mixed trace.  Same high outputs add by
    triangle; only the resulting full low/high Fourier split is orthogonal.
    """
    z = upper(api, core,
              returned['zero_stable_return_high_root_mixed_upper']
              + upper(api, core, baseline_high_root_mixed_upper))
    return full_root(api, core,
                     returned['physical_root_even96_upper'],
                     returned['physical_root_odd96_mean_upper'], z)


def complete_negative_density_from_root(
        api, core, root_mixed_upper, read_saved_SP_upper,
        negative_source, read_saved_negative_source_upper):
    """The original PW.15 with every negative source and genuine impulse.

    root ordinary: the old PW constant-second domain, or the explicitly
    admitted full two-source extension of the SAME completed E/N/SP bound.
    Isotropic H^-2/3 pairs and anisotropic H^-2/3 x H^-1 pairs are then legal.
    An unqualified second nonmean residual is rejected, never discarded.
    strict ordinary: exactly one of the original L1 or L2 pair alternatives.
    Impulses keep their own whole-sum norms and no artificial sqrt(length).
    Source identities and any exact zeros are owned by the actual source file.
    """
    require(negative_source['same_selected_original_SP_operator'] is True
            and negative_source['complete_true_root_and_strict_windows'] is True
            and negative_source['all_interfaces_and_both_physical_means_retained'] is True
            and negative_source['root_source_window'] in (
                (ROOT_SOURCE_WINDOW,) + FULL_ROOT_SOURCE_WINDOWS)
            and negative_source['strict_source_window'] in STRICT_SOURCE_WINDOWS
            and negative_source['all_source_and_zero_identities_verified'] is True,
            'complete original negative source domain and actual full source identity')
    if negative_source['root_source_window'] == ROOT_SOURCE_WINDOW:
        require(negative_source['root_second_source_is_angular_constant'] is True,
                'the original narrow PW second source is an angular constant')
    else:
        require(negative_source.get(
            'whole_large_root_Cauchy_N_SP_two_source_identity_verified') is True,
            'same completed E.6 source contraction and complete N/SP readout')
    names = (
        'root_window_mixed_impulse_sum_upper',
        'root_window_ordinary_in_declared_two_component_window_upper',
        'strict_ordinary_pair_upper',
        'strict_Hminus1_impulse_sum_upper',
    )
    jm, fm, fs, js = (upper(api, core, read_saved_negative_source_upper(name))
                      for name in names)
    cr, co, c1, c2 = (upper(api, core, read_saved_SP_upper(name))
                      for name in NEGATIVE_GAINS)
    cs = c1 if negative_source['strict_source_window'] == STRICT_SOURCE_WINDOWS[0] else c2
    root = upper(api, core, root_mixed_upper)
    return upper(api, core, cr*(root+jm) + co*fm + cs*fs + c1*js)


def left_normalized_waist_observations(
        api, core, admitted, complete_density_upper,
        selected_inverse_density_L2_upper, fixed_waist_normalizer_inverse_L2_upper):
    """PN.15--17: the actual left output receivers, with no input change.

    For a genuine common x column its Ni has already entered Phi/Upsilon.
    Independent physical-port inputs keep THEIR original spaces; this
    left observation does not turn them into common H^-4/3 inputs.

    The two exact left receivers are U_H^-1 J_+ T_W^-1 and
    U_Rotation^-1 U_H^-1 J_- T_W^-1.  Rotation is an isometry.
    The two physical density means remain available in the joint state.
    The WPL physical primitive uses its own receiver, without T_W^-1.
    """
    require(admitted.get(
        'whole_WTA_WX_and_original_left_receiver_order_verified') is True,
        'whole paid left receiver bounds and their original ordered realization')
    density = upper(api, core, complete_density_upper)
    bh = upper(api, core, selected_inverse_density_L2_upper)
    kw = upper(api, core, fixed_waist_normalizer_inverse_L2_upper)
    require(bool(kw >= api.one),
            'normalizer bound includes identity on the two physical means')
    joint = upper(api, core, bh*kw*density)
    primitive = upper(api, core, bh*density*core.root(api, api.rational(1, 2)))
    return {
        'left_normalized_incoming_branch_upper': joint,
        'left_normalized_outgoing_branch_upper': joint,
        'left_normalized_joint_two_branches_upper': joint,
        'both_original_density_means_joint_upper': density,
        'WPL_complete_physical_primitive_row_upper': primitive,
        'input_right_coordinate_change_performed': False,
        'physical_port_promoted_to_common_Hminus4over3_input': False,
        'Maslov_sign_moved_across_a_circle_map': False,
        'independent_physical_mean_equations_solved': False,
    }


def ordered_WGB_high_addition(api, core, physical_primitive_upper,
                             target_inverse_L2_upper,
                             original_right_W_inverse_A_source_Hminus4over3_upper):
    """Exact B_tgt^-1 Delta_partial W^-1 A_src order; norms only at the end.

    The right factor belongs to a high-coordinate column.  An independent
    physical root96 column receives the left target factor only.
    """
    row, left, right = (upper(api, core, value) for value in (
        physical_primitive_upper, target_inverse_L2_upper,
        original_right_W_inverse_A_source_Hminus4over3_upper))
    return upper(api, core, left*row*right)

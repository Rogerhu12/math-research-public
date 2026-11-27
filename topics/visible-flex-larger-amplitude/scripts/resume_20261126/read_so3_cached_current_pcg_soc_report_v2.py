#!/usr/bin/env python3
# Independent pure-reader v2.  The full ac03/76b/a0e scientific sources and
# report schema are unchanged.  Only the ac03 fixed-background policy shape
# and the resulting pure readout schema are corrected from complete 0d659.
"""Read the complete current-eight-column PCG with original normalized-parent SOC.

All source bodies and actual scalar/parent/cache identities are checked.
Only stdlib JSON/source/byte attribution is performed: no F, J, numerical
arrays, additional scientific fixture or previous field certificate is used.
"""
import argparse
import ast
import hashlib
import importlib.util
import sys
import json
import math
from pathlib import Path

DRIVER_SHA = 'a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743'
HELPER_SHA = 'e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021'
CACHE_SHA = '78f7924f89ee874d14ea9dd9b78630910ed6c0b5e53c9ed4771d910015fcdfb7'
DERIVER_SHA = '6420bb73edad599da723001fff95c4ab9c64ccecff6e2459cf1fc85a20209d3e'
REPORT_SCHEMA = 'complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1'
FRAME_SHA = 'ac03c43dba4c24016a79012e322d66a53b0ed155a1e5e00065e476846cc8ec33'
V5_SHA = '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8'
V3_SHA = 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'
FIELD_SHA = '234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42'
HESSIAN_SHA = '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4'
SPECTRAL_SHA = 'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def load_pins(path):
    values = [ast.literal_eval(node.value) for node in ast.parse(path.read_text()).body
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SOURCE_PINS'
            for t in node.targets)]
    if len(values) != 1:
        raise ValueError('One complete literal source registry is required')
    return values[0]


def statistic(value, profile):
    if value is None:
        return None
    if value.get('fixed_scalar_metric_identity_sha256') != profile:
        raise ValueError('A statistics record belongs to another actual target')
    spectrum = value['spectral']
    return dict(max_relative_gram=value['max_relative_gram'],
        legacy_max_relative_gram=value.get('legacy_max_relative_gram'),
        Phi=spectrum['centered_phi_normalized'], uncentered_Phi=spectrum['phi_normalized'],
        p=spectrum['p'], epsilon=spectrum['epsilon'], scale=spectrum['scale'],
        normalization=spectrum['normalization'],
        min_relative_E=value['min_relative_E'],
        min_relative_determinant=value['min_relative_determinant'],
        domain=value.get('domain'))


def geometric(value):
    if value is None:
        return None
    complete = value.get('complete') is True
    g = value.get('maximum_physical_g')
    real_feasible = bool(complete and isinstance(g, (int, float))
        and math.isfinite(g) and g <= 0 and value.get('passed') is True)
    result = dict(complete=complete, true_finite_geometry_feasible=real_feasible,
        maximum_physical_g=g, necessary_reach_product=value.get('necessary_reach_product'),
        reach_physical_g=value.get('reach_physical_g'), worst=value.get('worst'),
        farthest=value.get('farthest'), maximum_radius=value.get('maximum_radius'),
        min_area=value.get('min_area'), current_full_point_sha256=value.get('current_full_point_sha256'),
        maximum_absolute_principal_curvature=value.get('maximum_absolute_principal_curvature'),
        diameter_point_lower=value.get('diameter_point_lower'), current_height=value.get('current_height'),
        current_witness_radius=value.get('current_witness_radius'),
        permanent_unique_locations_read=value.get('permanent_unique_locations_read'),
        permanent_curvature_locations=value.get('permanent_curvature_locations'),
        permanent_radius_locations=value.get('permanent_radius_locations'),
        all_permanent_locations_read=value.get('all_permanent_curvature_and_radius_locations_read', False),
        both_witness_signs_read=value.get('both_witness_signs_read_at_every_point', False),
        continuous_geometry_certified=False)
    amplitude = value.get('amplitude')
    if amplitude is not None:
        result['amplitude_g'] = {key: amplitude[key] for key in
            ('body_diameter', 'distance_plus', 'distance_minus', 'cap_diameter', 'height_floor')}
    for key in ('error_type', 'error'):
        if key in value:
            result[key] = value[key]
    return result


def _finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _digest(value):
    return isinstance(value, str) and len(value) == 64 and all(ch in '0123456789abcdef' for ch in value)


def failure_classes(trial):
    failed, missing = [], []
    if trial.get('actual_read_error') is not None:
        failed.append('actual_numerical_read_error')
    if trial.get('domain_feasible') is False:
        failed.append('metric_domain')
    elif trial.get('domain_feasible') is None:
        missing.append('metric_domain')
    if trial.get('actual_Phi_descent') is False:
        failed.append('actual_same_Phi_descent')
    elif trial.get('actual_Phi_descent') is None:
        missing.append('actual_same_Phi_descent')
    geometry = trial.get('full_geometry')
    if not trial.get('full_true_geometry_read') or geometry is None:
        missing.append('complete_actual_geometry')
    elif geometry.get('complete') is not True:
        failed.append('actual_geometry_incomplete')
    else:
        if _finite(geometry.get('reach_physical_g')) and geometry['reach_physical_g'] > 0:
            failed.append('necessary_reach_product')
        amplitude = geometry.get('amplitude')
        if amplitude is None or amplitude.get('complete') is not True:
            missing.append('complete_actual_amplitude')
        else:
            for name in ('body_diameter', 'distance_plus', 'distance_minus', 'cap_diameter', 'height_floor'):
                if _finite(amplitude.get(name)) and amplitude[name] > 0:
                    failed.append(name)
    return failed, missing


def _same_measure(stats, baseline):
    if stats is None:
        return
    for key in ('p', 'epsilon', 'scale', 'normalization'):
        if stats[key] != baseline[key]:
            raise ValueError('A recorded trial changed its fixed positive measure or actual Phi: '+key)


def _actual_geometry(value, model):
    if value is not None and value.get('actual_model_identity_sha256') != model:
        raise ValueError('A current or rejected true geometry belongs to another full physical model')
    result = geometric(value)
    if result is not None and result['true_finite_geometry_feasible']:
        if (value.get('all_permanent_curvature_and_radius_locations_read') is not True
                or value.get('both_witness_signs_read_at_every_point') is not True
                or value.get('all_six_world_jets_read') is not True):
            raise ValueError('A passed true geometry must read every permanent address, both witness signs and all world jets')
    return result


def _trial(trial, profile, baseline, model):
    stats = statistic(trial.get('statistics'), profile)
    _same_measure(stats, baseline)
    geometry = _actual_geometry(trial.get('full_geometry'), model)
    failures, missing = failure_classes(trial)
    return dict(index=trial['index'], alpha=trial.get('alpha'), accepted=trial.get('accepted') is True,
        actual_Phi_descent=trial.get('actual_Phi_descent'),
        domain_feasible=trial.get('domain_feasible'),
        actual_positive_physical_g=trial.get('actual_positive_physical_g'),
        full_true_geometry_read=trial.get('full_true_geometry_read'),
        true_finite_geometry_feasible=trial.get('physically_feasible'),
        actual_seconds=trial.get('actual_seconds'), actual_read_error=trial.get('actual_read_error'),
        statistics=stats, geometry=geometry, failure_classes=failures,
        unperformed_or_missing_checks=missing,
        failure_classes_json=json.dumps(failures, separators=(',', ':')),
        unperformed_or_missing_checks_json=json.dumps(missing, separators=(',', ':')),
        provisional_original_ray_acceptance=trial.get('provisional_original_ray_acceptance'),
        provisional_complete_corrected_acceptance=trial.get('provisional_complete_corrected_acceptance'),
        accepted_selection_readback_index=trial.get('accepted_selection_readback_index'))


def _check_actual_metric_acceptance(trial, baseline, model):
    stats = trial.get('statistics')
    geometry = _actual_geometry(trial.get('full_geometry'), model)
    if (trial.get('full_true_geometry_read') is not True
            or trial.get('domain_feasible') is not True
            or trial.get('actual_Phi_descent') is not True
            or stats is None or stats['min_relative_E'] <= 0
            or stats['min_relative_determinant'] <= 0
            or stats['spectral']['centered_phi_normalized'] >= baseline['Phi']
            or geometry is None or not geometry['true_finite_geometry_feasible']):
        raise ValueError('A metric acceptance needs true same-Phi descent, positive domain and complete actual all-point geometry')


def _before_selection(trial):
    return trial.get('pre_selection_true_read', trial)


def backtracked_anchor_and_selection(value, profile, baseline, model):
    anchor = value.get('SOC_anchor')
    readbacks = value.get('candidate_selection_readbacks', [])
    choices = value.get('candidate_choice_order', [])
    if anchor is None:
        if readbacks or choices or value.get('soc_trials'):
            raise ValueError('No correction or candidate readback may use an undeclared immutable anchor')
        return dict(anchor=None, final_candidate_readbacks=[],
            actual_final_candidate_readback_count=0,
            post_ray_SOC_not_attempted_reason=value.get('post_ray_SOC_not_attempted_reason'))
    if value['phase'] != 'metric':
        raise ValueError('This complete backtracked correction belongs only to a metric direction')
    trials = value['trials']
    for index, item in enumerate(trials):
        if item['index'] != index or item['alpha'] != math.ldexp(1., -index):
            raise ValueError('Keep the actual complete ordered original dyadic backtracking sequence')
    fallback_index, anchor_index = anchor['fallback_ray_index'], anchor['ray_index']
    if (not isinstance(fallback_index, int) or not isinstance(anchor_index, int)
            or not 0 <= anchor_index < fallback_index < len(trials)
            or anchor['ray_alpha'] != trials[anchor_index]['alpha']
            or anchor['fallback_ray_alpha'] != trials[fallback_index]['alpha']
            or not anchor['ray_alpha'] > anchor['fallback_ray_alpha']
            or anchor.get('fixed_original_QP_direction') is not True
            or anchor.get('fixed_current_parent') is not True
            or anchor.get('closest_eligible_larger_ray_already_read') is not True
            or anchor.get('fallback_is_only_provisional_until_final_memory_readback') is not True):
        raise ValueError('The one SOC anchor must follow the complete true original-ray fallback search')
    for key in ('fallback_point_sha256', 'fixed_original_parent_sha256',
            'anchor_point_sha256', 'anchor_coordinate_step_sha256'):
        if not _digest(anchor.get(key)):
            raise ValueError('Bind every complete actual parent/anchor/fallback word vector: '+key)
    fallback = trials[fallback_index]
    if (fallback.get('provisional_original_ray_acceptance') is not True
            or any(item.get('provisional_original_ray_acceptance') is True for item in trials[:fallback_index])):
        raise ValueError('SOC requires the first genuinely feasible original-ray fallback, never an untested substitute')
    _check_actual_metric_acceptance(_before_selection(fallback), baseline, model)
    eligible = []
    for index, item in enumerate(trials[:fallback_index]):
        actual = _before_selection(item)
        geom = actual.get('full_geometry')
        if (actual.get('domain_feasible') is True
                and actual.get('actual_Phi_descent') is True
                and actual.get('full_true_geometry_read') is True
                and geom is not None and geom.get('complete') is True
                and _finite(actual.get('actual_positive_physical_g'))
                and actual['actual_positive_physical_g'] > 0):
            eligible.append(index)
    if not eligible or eligible[-1] != anchor_index:
        raise ValueError('Use exactly the closest already read eligible larger original ray')
    for trial in value.get('soc_trials', []):
        if (trial['anchor_ray_index'] != anchor_index or trial['anchor_alpha'] != anchor['ray_alpha']
                or trial.get('same_original_parent_and_anchor') is not True):
            raise ValueError('A later correction silently switched to another ray anchor')
        proposal = trial.get('proposal')
        if proposal is not None and (
                proposal['identity']['parent_coordinate_sha256'] != anchor['fixed_original_parent_sha256']
                or proposal['original_anchor_point_sha256'] != anchor['anchor_point_sha256']
                or proposal['original_anchor_step_sha256'] != anchor['anchor_coordinate_step_sha256']
                or proposal['anchor_alpha'] != anchor['ray_alpha']):
            raise ValueError('All C*d, nonlinear remainders and A*z must belong to this identical x/d anchor')
    if not 1 <= len(choices) <= 2:
        raise ValueError('Keep the actual original-ray fallback and at most the first complete corrected candidate')
    by_key = {}
    for choice in choices:
        key = (choice['kind'], choice['index'])
        if key in by_key or not _finite(choice.get('previously_read_actual_Phi')) or not _digest(choice.get('full_point_sha256')):
            raise ValueError('Every candidate choice requires one complete actual point and same-Phi value')
        if choice['kind'] == 'original_ray':
            if choice['index'] != fallback_index or choice['full_point_sha256'] != anchor['fallback_point_sha256']:
                raise ValueError('The fallback changed after the original complete ray read')
            item = fallback
        elif choice['kind'] == 'complete_separation_SOC':
            item = value['soc_trials'][choice['index']]
            if (item.get('provisional_complete_corrected_acceptance') is not True
                    or choice['full_point_sha256'] != item['corrected_candidate_sha256']):
                raise ValueError('A SOC alternative must be the actual fully read complete corrected point')
        else:
            raise ValueError('No hidden third or re-anchored candidate is allowed')
        previous = _before_selection(item)
        _check_actual_metric_acceptance(previous, baseline, model)
        if previous['statistics']['spectral']['centered_phi_normalized'] != choice['previously_read_actual_Phi']:
            raise ValueError('Candidate ordering changed the actual previously read same-Phi scalar')
        by_key[key] = item
    if ('original_ray', fallback_index) not in by_key:
        raise ValueError('The true original-ray fallback was silently omitted')
    order = [item['previously_read_actual_Phi'] for item in choices]
    if order != sorted(order):
        raise ValueError('Try true candidates in their explicitly declared observed same-Phi order')
    if not 1 <= len(readbacks) <= len(choices):
        raise ValueError('A deferred candidate needs a real complete current-memory readback')
    summaries, accepted = [], []
    for index, readback in enumerate(readbacks):
        choice = choices[index]
        key = (readback['candidate_kind'], readback['candidate_index'])
        if (readback['index'] != index or key != (choice['kind'], choice['index'])
                or readback['full_point_sha256'] != choice['full_point_sha256']
                or readback['original_parent_sha256'] != anchor['fixed_original_parent_sha256']
                or readback.get('all_original_and_SOC_discoveries_retained') is not True):
            raise ValueError('The final candidate must retain its full point, original parent and complete permanent memory')
        before, after = readback['permanent_counts_before'], readback['permanent_counts_after']
        for name in ('curvature', 'radius'):
            if (not isinstance(before[name], int) or before[name] < 0
                    or not isinstance(after[name], int) or after[name] < before[name]):
                raise ValueError('Permanent current-memory counts must remain complete and append-only')
        geom = readback.get('full_geometry')
        if geom is not None and geom.get('complete') is True:
            if (geom.get('current_full_point_sha256') != readback['full_point_screen_sha256']
                    or geom.get('permanent_curvature_locations') != after['curvature']
                    or geom.get('permanent_radius_locations') != after['radius']):
                raise ValueError('The accepted/rejected final screen omitted a new discovery or used another point')
        summary = _trial(readback, profile, baseline, model)
        summary.update(candidate_kind=readback['candidate_kind'], candidate_index=readback['candidate_index'],
            full_point_sha256=readback['full_point_sha256'],
            permanent_counts_before=before, permanent_counts_after=after,
            original_parent_sha256=readback['original_parent_sha256'])
        summaries.append(summary)
        if readback.get('accepted'):
            _check_actual_metric_acceptance(readback, baseline, model)
            item = by_key[key]
            if (index != len(readbacks)-1 or item.get('accepted') is not True
                    or item.get('accepted_selection_readback_index') != index
                    or value.get('accepted_selection_readback_index') != index
                    or item.get('statistics') != readback.get('statistics')
                    or item.get('full_geometry') != geom):
                raise ValueError('Only the final actually selected readback may mark its ray/SOC accepted')
            accepted.append(index)
    if len(accepted) > 1:
        raise ValueError('A direction cannot accept two different physical fields')
    if not accepted and (len(readbacks) != len(choices)
            or value.get('fallback_failed_final_memory_readback') is not True
            or value.get('remaining_original_ray_budget_continues_without_another_SOC_anchor') is not True):
        raise ValueError('A failed final-memory fallback is never accepted through its earlier passed flag')
    return dict(anchor=anchor, candidate_choice_order=choices,
        final_candidate_readbacks=summaries,
        actual_final_candidate_readback_count=len(readbacks),
        final_memory_selection_accepted=bool(accepted),
        original_fallback_invalidated=value.get('fallback_failed_final_memory_readback', False),
        later_original_ray_budget_continued=value.get('remaining_original_ray_budget_continues_without_another_SOC_anchor', False),
        candidate_choice_and_readbacks_json=json.dumps(dict(choices=choices,
            readbacks=[dict(kind=item['candidate_kind'], index=item['candidate_index'],
                accepted=item['accepted'], Phi=(item.get('statistics') or {}).get('Phi'),
                physical_g=(item.get('geometry') or {}).get('maximum_physical_g'),
                failure_classes=item['failure_classes']) for item in summaries]),
            separators=(',', ':'), allow_nan=False))



def current_preconditioner_policy(report):
    policy = report.get('current_full_QP_preconditioner_policy')
    if not isinstance(policy, dict):
        raise ValueError('The complete current-PCG policy must be explicit')
    if (policy.get('schema') != 'same-current-complete-SO3-eight-column-metric-only-PCG-policy-v1'
            or policy.get('preparation_source_sha256') != FRAME_SHA
            or policy.get('metric_consumer_source_sha256') != V5_SHA
            or policy.get('original_v3_source_sha256') != V3_SHA
            or policy.get('coarse_column_count') != 8
            or any(policy.get(key) is not True for key in (
                'current_complete_A_and_Atranspose_each_column',
                'fixed_global_SPD_for_one_complete_QP',
                'complete_original_QP_norm_penalty_and_C_preserved',
                'original_Phase_I_v3_unchanged',
                'original_v3_fallback_before_PCG_only',
                'mid_chain_application_failure_truncates_honestly',
                'performance_gain_not_predeclared'))
            or policy.get('previous_parent_Gram_used') is not False
            or policy.get('reduced_field_ansatz') is not False):
        raise ValueError('The full-space current A/A*, original norm and honest fixed-PCG policy changed')
    return dict(policy)


def _integer_count(value, name, maximum=None):
    if (not isinstance(value, int) or isinstance(value, bool) or value < 0
            or (maximum is not None and value > maximum)):
        raise ValueError('Invalid actually recorded count '+name)
    return value


def _small_matrix_diagonal(value, name):
    if (not isinstance(value, list) or len(value) != 8
            or any(not isinstance(row, list) or len(row) != 8 for row in value)
            or any(not _finite(item) for row in value for item in row)):
        raise ValueError('The actual recorded complete 8 by 8 '+name+' is missing or nonfinite')
    # Select existing scalar words only: no Gram, eigenvalue or factor is
    # recomputed. The full matrix remains only in the runner report.
    return [value[j][j] for j in range(8)]


def current_metric_preconditioner(value, profile, *, model, norm_identity, variables):
    prep = value.get('current_eight_column_preconditioner')
    dispatch = value.get('actual_metric_QP_dispatch')
    qp = value['qp']
    if value['phase'] == 'restoration':
        if (prep is not None or dispatch is not None
                or qp.get('schema') != 'fullspace-feasible-active-set-cg-reliable-update-v3'):
            raise ValueError('The complete original all-C Phase I must keep its original v3')
        return dict(phase='restoration', enabled=False,
            effective_solver_source_sha256=V3_SHA,
            original_Phase_I_preserved=True, current_frame_prepared=False)
    if not isinstance(prep, dict) or not isinstance(dispatch, dict):
        raise ValueError('Every metric QP must record its actual current preparation and solver dispatch')
    binding = prep['binding']
    quadratic = value['quadratic_model']
    damping = value['actual_damping']
    current_point = value['starting_geometry'].get('current_full_point_sha256')
    if (prep.get('schema') != 'complete-current-SO3-eight-column-SPD-preconditioner-v1'
            or prep.get('source_sha256') != FRAME_SHA
            or binding.get('field_source', {}).get('sha256') != FIELD_SHA
            or binding.get('hessian_source', {}).get('sha256') != HESSIAN_SHA
            or binding.get('spectral_source_sha256') != SPECTRAL_SHA
            or binding.get('model_identity_sha256') != model
            or binding.get('fixed_scalar_metric_identity_sha256') != profile
            or binding.get('coordinate_norm_identity_sha256') != norm_identity
            or not _digest(current_point)
            or binding.get('current_full_point_sha256') != current_point
            or binding.get('complete_variables') != variables
            or not _finite(damping) or damping <= 0
            or prep.get('actual_damping') != damping
            or prep.get('actual_damping_hex') != float(damping).hex()
            or quadratic.get('damping') != damping
            or qp.get('damping') != damping):
        raise ValueError('The current complete A, physical parent, source, norm or mu binding changed')
    factor = binding.get('external_factor')
    if (not _finite(factor) or factor <= 0
            or binding.get('external_factor_hex') != float(factor).hex()
            or quadratic.get('outer_half_Hessian_factor') != factor*factor
            or quadratic.get('gradient_and_Hessian_units_unchanged_from_declared_Phi') is not True):
        raise ValueError('Keep the original full positive-Hessian objective units')
    for key in ('p', 'epsilon', 'scale'):
        if binding['spectral_parameters'][key] != value['starting_statistics']['spectral'][key]:
            raise ValueError('The current frame used another spectral objective '+key)
    for key in ('mesh_sha256', 'radial_free_sha256', 'stage_weights_sha256',
            'orbit_weights_sha256', 'target_a_carrier_sha256'):
        if not _digest(binding.get(key)):
            raise ValueError('Missing actual complete carrier/positive-measure identity '+key)
    for key in ('immutable_original_objective_norm_rows_and_acceptance',
            'construction_before_any_PCG_chain'):
        if prep.get(key) is not True:
            raise ValueError('A complete immutable preparation responsibility was lost: '+key)
    for key in ('old_DI_frame_or_angular_moments_used', 'previous_parent_Gram_used',
            'original_QP_changed', 'physical_feasibility_conclusion',
            'performance_improvement_established', 'matrix_or_column_raw_published'):
        if prep.get(key) is not False:
            raise ValueError('A current preparation acquired an unsupported claim: '+key)
    completed = _integer_count(prep.get('columns_completed'), 'completed columns', 8)
    a_calls = _integer_count(prep.get('extra_A_calls'), 'A products', 8)
    at_calls = _integer_count(prep.get('extra_Atranspose_calls'), 'A transpose products', 8)
    history = prep.get('column_history')
    if (not completed <= at_calls <= a_calls <= completed+1
            or not isinstance(history, list) or len(history) != completed):
        raise ValueError('Keep the actual successful columns and paid partial product attempts distinct')
    for index, record in enumerate(history):
        if (record.get('column') != index
                or not _digest(record.get('full_coordinate_direction_sha256'))
                or any(not _finite(record.get(key)) for key in
                    ('seconds', 'data_energy', 'transpose_diagonal', 'diagonal_pair_absolute_defect'))):
            raise ValueError('The actual ordered complete current-column record changed')
    enabled = prep.get('enabled')
    if not isinstance(enabled, bool):
        raise ValueError('The actual optional preparation enabled flag must be explicit')
    expected_solver = V5_SHA if enabled else V3_SHA
    if (dispatch.get('wrapper_source_sha256') != V5_SHA
            or dispatch.get('effective_solver_source_sha256') != expected_solver
            or dispatch.get('fixed_global_preconditioner_used') is not enabled
            or dispatch.get('unavailable_preparation_delegates_to_original_v3_before_any_PCG_chain') is not (not enabled)
            or dispatch.get('mid_PCG_failure_never_restarts_with_identity') is not True):
        raise ValueError('Do not disguise an unavailable setup or mid-chain failure as another solver')
    result = dict(phase='metric', enabled=enabled, preparation_schema=prep['schema'],
        preparation_source_sha256=FRAME_SHA, preparation_status=prep['status'],
        preparation_seconds=prep.get('preparation_seconds'),
        preparation_field_operator_count_deltas=prep.get('actual_field_operator_count_deltas'),
        actual_extra_A_calls=a_calls, actual_extra_Atranspose_calls=at_calls,
        actual_columns_completed=completed,
        column_records=history, column_records_canonical_sha256=canonical(history),
        current_full_point_sha256=current_point, model_identity_sha256=model,
        fixed_scalar_metric_identity_sha256=profile,
        coordinate_norm_identity_sha256=norm_identity,
        actual_norm_arrays=binding['actual_norm_arrays'],
        complete_variables=variables, all_original_metric_rows=binding['all_original_metric_rows'],
        actual_quarter_rows=binding['actual_quarter_rows'],
        full_A_column_bytes=prep['full_A_column_bytes'],
        full_H_column_bytes=prep['full_H_column_bytes'],
        maximum_simultaneously_retained_full_A_columns=prep['maximum_simultaneously_retained_full_A_columns'],
        full_field_temporary_arrays_are_additional=prep['full_field_temporary_arrays_are_additional'],
        total_peak_memory_inferred_from_column_size=False,
        external_factor=factor, external_factor_hex=binding['external_factor_hex'],
        actual_damping=damping, actual_damping_hex=prep['actual_damping_hex'],
        effective_solver_source_sha256=expected_solver, dispatch=dispatch,
        preparation_matrices_recomputed=False, raw_small_matrices_in_readout=False,
        complete_QP_subspace_restricted=False, performance_improvement_claimed=False)
    if enabled:
        # ac03 stores beta together with its explicit fixed-scale policy.
        # The original 0d65 reader incorrectly treated this complete dict as
        # a scalar. Validate its real shape and retain the whole object.
        background = prep.get('fixed_background_inverse')
        common = {'policy', 'explicit_algorithm_choice', 'value', 'value_hex',
            'optimal_scale_claimed', 'unchanged_until_QP_returns'}
        if (not isinstance(background, dict)
                or not _finite(background.get('value')) or background['value'] <= 0
                or background.get('value_hex') != float(background['value']).hex()
                or background.get('explicit_algorithm_choice') is not True
                or background.get('optimal_scale_claimed') is not False
                or background.get('unchanged_until_QP_returns') is not True):
            raise ValueError('Keep the actual positive beta and its entire fixed-for-one-QP policy')
        if background['policy'] == 'reciprocal-current-coarse-average-Rayleigh':
            if (set(background) != common | {'numerator', 'denominator', 'formula'}
                    or background.get('formula') != 'trace(WT W)/trace(current compressed H)'
                    or any(not _finite(background.get(key)) or background[key] <= 0
                        for key in ('numerator', 'denominator'))
                    or float(background['numerator']/background['denominator']).hex()
                        != background['value_hex']):
                raise ValueError('The complete current coarse-Rayleigh scale record changed')
        elif background['policy'] == 'explicit-positive-literal-background':
            if set(background) != common:
                raise ValueError('Keep the complete explicitly supplied fixed scale policy')
        else:
            raise ValueError('The actual ac03 producer has only its two declared scale policies')
        frame = prep['frame']
        fixed = qp.get('fixed_preconditioner', {})
        face = fixed.get('face_metric', {})
        applications = fixed.get('applications', {})
        if (prep.get('status') != 'prepared_optional_fixed_SPD'
                or completed != 8 or a_calls != 8 or at_calls != 8
                or frame.get('schema') != 'complete-SO3-eight-column-frame-v1'
                or frame.get('actual_column_count') != 8
                or frame.get('full_coordinate_dimension') != variables
                or frame.get('complete_QP_subspace_restricted') is not False
                or frame.get('original_norm_changed') is not False
                or frame.get('all_original_variables_retained') is not True
                or qp.get('schema') != 'fullspace-feasible-active-set-face-metric-PCG-v5'
                or qp.get('implementation_source_sha256') != V5_SHA
                or qp.get('frozen_v3_source', {}).get('sha256') != V3_SHA
                or fixed.get('enabled') is not True
                or fixed.get('source_and_scale_metadata') != prep
                or fixed.get('solver_replaced_preconditioner') is not False
                or fixed.get('caller_required_to_freeze_operator') is not True
                or face.get('global_preconditioner_changed') is not False
                or face.get('original_QP_norm_constraints_and_stopping_unchanged') is not True
                or not _finite(prep.get('positive_small_factor_diagonal_min'))
                or prep['positive_small_factor_diagonal_min'] <= 0):
            raise ValueError('The actual fixed current SPD/face-PCG consumer does not match the complete preparation')
        for key in ('literal_frame_Gram_sha256',):
            if not _digest(frame.get(key)):
                raise ValueError('Missing complete literal current frame identity')
        for key in ('actual_data_Gram_sha256', 'symmetric_small_H_sha256', 'actual_small_factor_sha256'):
            if not _digest(prep.get(key)):
                raise ValueError('Missing actual current small-array identity '+key)
        data_diagonal = _small_matrix_diagonal(prep['actual_data_Gram'], 'data Gram')
        small_diagonal = _small_matrix_diagonal(prep['symmetric_small_H'], 'small damped Hessian')
        literal_diagonal = _small_matrix_diagonal(frame['literal_frame_Gram'], 'literal W transpose W')
        failures = applications.get('failures', [])
        if not isinstance(failures, list) or any(item.get('fallback_to_identity_performed') is not False for item in failures):
            raise ValueError('A fixed-PCG application failure must never silently replace its B')
        result.update(frame_schema=frame['schema'], actual_coarse_columns=8,
            compact_frame_bytes=frame['compact_frame_bytes'],
            inverse_coordinate_formula=frame['inverse_coordinate_formula'],
            literal_frame_Gram_sha256=frame['literal_frame_Gram_sha256'],
            actual_data_Gram_sha256=prep['actual_data_Gram_sha256'],
            symmetric_small_H_sha256=prep['symmetric_small_H_sha256'],
            actual_small_factor_sha256=prep['actual_small_factor_sha256'],
            maximum_data_Gram_skew=prep['maximum_data_Gram_skew'],
            positive_small_factor_diagonal_min=prep['positive_small_factor_diagonal_min'],
            fixed_background_inverse=background,
            fixed_background_inverse_value=background['value'],
            fixed_background_inverse_value_hex=background['value_hex'],
            fixed_background_inverse_policy=background['policy'],
            complete_background_scale_policy_retained=True,
            data_Gram_diagonal_json=json.dumps(data_diagonal, separators=(',', ':')),
            damped_H_diagonal_json=json.dumps(small_diagonal, separators=(',', ':')),
            literal_frame_diagonal_json=json.dumps(literal_diagonal, separators=(',', ':')),
            face_mode=face.get('current_mode'),
            face_QR_rebuilds=face.get('current_QR_rebuild_count'),
            face_applications=face.get('applications'),
            global_B_applications=face.get('global_B_applications'),
            global_B_seconds=face.get('global_B_seconds'),
            face_preparation_seconds=face.get('preparation_seconds'),
            maximum_face_cached_vectors=face.get('maximum_cached_vectors'),
            maximum_face_cached_vector_bytes=face.get('maximum_cached_vector_bytes'),
            maximum_observed_Schur_skew=face.get('maximum_observed_Schur_skew'),
            fallback_face_count=face.get('fallback_faces'),
            face_history_canonical_sha256=canonical(face),
            projected_preconditioner_applications=applications.get('applications'),
            projected_preconditioner_seconds=applications.get('seconds'),
            failed_preconditioner_application_count=len(failures),
            preconditioner_failures=failures,
            euclidean_release_starters_completed=applications.get('euclidean_release_starters_completed'),
            longest_same_face_advances=qp.get('longest_same_face_advances'),
            final_actual_linear_residual_relative_defect=qp.get('final_actual_linear_residual_relative_defect'),
            preconditioner_application_failure_is_honest_truncation=bool(failures),
            preparation_fallback=False)
    else:
        if (prep.get('status') != 'optional_numeric_preparation_unavailable'
                or qp.get('schema') != 'fullspace-feasible-active-set-cg-reliable-update-v3'
                or prep.get('no_coarse_column_dropped_to_force_success') is not True
                or prep.get('mathematical_infeasibility_claimed') is not False):
            raise ValueError('Only a reported pre-QP numeric preparation failure may delegate to original v3')
        result.update(preparation_fallback=True, preparation_error_type=prep.get('exception_type'),
            preparation_error=prep.get('message'), fallback=prep.get('fallback'),
            effective_original_v3_before_PCG=True,
            small_SPD_failure_is_not_mathematical_infeasibility=True)
    return result


def direction(value, profile, *, model, norm_identity, variables, soc_policy, restoration_interior_margin):
    phase = value['phase']
    if phase not in ('metric', 'restoration'):
        raise ValueError('The complete report used an undeclared scientific phase')
    rows = value['complete_selected_inequalities']
    added = rows.get('appended_pre_QP_separation_rows', 0)
    if (rows.get('no_original_row_removed') is not True
            or rows['original_prefix_rows']+rows['appended_amplitude_rows']+added != rows['selected_rows']
            or len(rows['rows']) != rows['selected_rows']
            or rows['row_cache_bytes'] != rows['selected_rows']*variables*8):
        raise ValueError('A full original, amplitude or pre-QP separated row was dropped or miscounted')
    for index, row in enumerate(rows['rows']):
        if row['index'] != index or not _finite(row['physical_g']) or not _finite(row['normalized_bound']):
            raise ValueError('Keep the actual full row order and every finite physical bound')
    if phase == 'metric':
        if (rows.get('schema') != 'complete-SO3-selected-amplitude-and-prior-rejection-QP-rows-v1'
                or rows.get('source_of_prior_separation_rows_sha256') != HELPER_SHA
                or rows.get('original_prefix_rewritten') is not False
                or not _digest(rows.get('literal_original_prefix_sha256'))
                or not _digest(rows.get('frozen_complete_QP_prefix_sha256'))):
            raise ValueError('This metric QP must bind its entire real original prefix and prior-separation helper')
        seed = value.get('prior_rejection_separation')
        if (seed is None or seed.get('extension_available') is not True
                or seed.get('added_rows', 0) != added
                or seed.get('prior_physical_values_or_covectors_inherited') is not False
                or seed.get('original_selector_and_amplitude_prefix_unchanged') is not True):
            raise ValueError('Every prior rejected address must be freshly linearized before the actual NEW QP')
        quadratic = value['quadratic_model']
        if (quadratic['physical_coordinate_norm']['norm_identity_sha256'] != norm_identity
                or quadratic.get('all_metric_mean_constraints_retained') is not True):
            raise ValueError('The complete parent H2 norm or any original metric mean was changed')
    else:
        quadratic = value['quadratic_model']
        if (added or value.get('soc_trials') or value.get('prior_rejection_separation') is not None
                or quadratic.get('all_original_rows_retained') is not True
                or quadratic.get('physical_feasibility_inferred_from_slack') is not False
                or quadratic['original_rows'] != rows['selected_rows']
                or quadratic.get('schema') != 'complete-all-typed-C-interior-common-slack-phase-I-v1'
                or quadratic.get('search_interior_margin') != restoration_interior_margin
                or quadratic.get('original_physical_g_changed') is not False
                or quadratic.get('original_nonlinear_acceptance_relaxed') is not False
                or quadratic.get('stricter_search_target') is not True):
            raise ValueError('The original complete all-C Phase I must not lose rows or interpret tau as feasibility')
    baseline = statistic(value['starting_statistics'], profile)
    starting_geometry = _actual_geometry(value['starting_geometry'], model)
    if phase == 'metric' and not starting_geometry['true_finite_geometry_feasible']:
        raise ValueError('A metric QP needs the actually reread feasible current parent')
    qp = value['qp']
    result = dict(index=value['index'], serial=value['serial'], phase=phase,
        accepted=value['accepted'], accepted_alpha=value.get('accepted_alpha'),
        accepted_step_kind=value.get('accepted_step_kind'),
        accepted_SOC_round=value.get('accepted_SOC_round'),
        accepted_SOC_anchor_alpha=value.get('accepted_SOC_anchor_alpha'),
        damping=value['actual_damping'], damping_after=value.get('damping_after_direction'),
        qp_status=qp['status'], actual_advances=qp['advances'],
        qp_termination_is_iteration_limit=qp['status'] == 'iteration_limit',
        final_face_projected_gradient_norm=qp.get('final_face_projected_gradient_norm'),
        qp_tolerance=qp.get('gradient_tolerance'),
        active_face_rows=qp.get('active_face', {}).get('active_rows'),
        active_face_indices=qp.get('active_face', {}).get('active_indices'),
        actual_operator_products=qp.get('operator_products'),
        maximum_linear_violation=qp.get('maximum_linear_violation'),
        original_geometry_rows=rows['original_prefix_rows'],
        amplitude_rows=rows['appended_amplitude_rows'], pre_QP_separation_rows=added,
        total_rows=rows['selected_rows'], row_cache_bytes=rows['row_cache_bytes'],
        row_cache_capacity_bytes=rows.get('row_cache_capacity_bytes'),
        duplicate_prefix_cache_bytes=rows.get('duplicate_prefix_cache_bytes'),
        original_literal_prefix_sha256=rows.get('literal_original_prefix_sha256'),
        frozen_complete_QP_prefix_sha256=rows.get('frozen_complete_QP_prefix_sha256'),
        prior_rejection_separation=value.get('prior_rejection_separation'),
        actual_QP_seconds=value.get('actual_QP_seconds'),
        actual_complete_direction_seconds=value['seconds'],
        actual_QP_operator_counts=value.get('actual_QP_operator_counts'),
        actual_complete_direction_operator_counts=value.get('actual_complete_direction_operator_counts'),
        starting_statistics=baseline, starting_geometry=starting_geometry,
        accepted_statistics=statistic(value.get('accepted_statistics'), profile),
        accepted_geometry=_actual_geometry(value.get('accepted_geometry'), model),
        maximum_selected_linear_physical_g=value.get('maximum_selected_linear_physical_g'),
        old_actual_positive_physical_g=value['old_actual_maximum_positive_physical_g'],
        computed_common_slack=value.get('computed_common_slack'),
        common_slack_is_true_feasibility=False, trial_count=len(value['trials']),
        phase_I_search_interior_margin=restoration_interior_margin if phase == 'restoration' else None,
        original_nonlinear_acceptance_relaxed=False,
        coordinate_step_norm=value.get('coordinate_step_norm'),
        half_objective_slope=value.get('half_objective_slope'),
        predicted_full_ray_Phi_change=value.get('predicted_actual_Phi_change'),
        actual_to_original_full_ray_prediction_ratio=value.get('actual_to_full_prediction_ratio'),
        actual_to_accepted_SOC_prediction_ratio=value.get('actual_to_accepted_SOC_prediction_ratio'),
        original_full_ray_ratio_is_same_alpha_ratio=False,
        SOC_anchor=value.get('SOC_anchor'),
        SOC_unavailable_error=value.get('SOC_unavailable_error'),
        SOC_unavailability_is_geometric_infeasibility=False,
        final_complete_SOC_cache=value.get('final_complete_SOC_cache'))
    result['current_preconditioner'] = current_metric_preconditioner(value, profile,
        model=model, norm_identity=norm_identity, variables=variables)
    _same_measure(result['accepted_statistics'], baseline)
    if value.get('accepted_bundle') is not None:
        result['accepted_bundle_sha256'] = value['accepted_bundle']['sha256']
    trials, accepted_candidates = [], []
    for trial in value['trials']:
        if trial.get('accepted'):
            if phase == 'metric':
                _check_actual_metric_acceptance(trial, baseline, model)
            elif not (trial.get('full_true_geometry_read') is True
                    and trial.get('domain_feasible') is True
                    and _finite(trial.get('actual_positive_physical_g'))
                    and trial['actual_positive_physical_g'] < value['old_actual_maximum_positive_physical_g']):
                raise ValueError('A restored accepted ray needs real nonlinear violation decrease independently of tau')
            accepted_candidates.append(('original_ray', trial))
        trials.append(_trial(trial, profile, baseline, model))
    soc_trials, anchor_identity, immutable_identity = [], None, None
    current_row_count = rows['selected_rows']
    projection_calls = 0
    tolerance = soc_policy['numerical_readback_tolerance']
    if len(value.get('soc_trials', [])) > soc_policy['maximum_rounds']:
        raise ValueError('The complete same-parent correction exceeded its explicitly declared round budget')
    for index, trial in enumerate(value.get('soc_trials', [])):
        if trial['index'] != index or trial.get('same_original_parent_and_anchor') is not True:
            raise ValueError('Every SOC round must retain its original complete parent and anchor')
        extension = trial.get('separation', {})
        if extension.get('extension_available') is True:
            n = extension.get('added_rows', 0)
            if n:
                if (extension.get('previous_rows') != current_row_count
                        or extension.get('current_rows') != current_row_count+n
                        or len(extension.get('rows', [])) != n
                        or extension.get('no_QP_reselection_or_original_row_rewrite') is not True
                        or extension.get('original_prefix_bytes_directly_checked') is not True):
                    raise ValueError('Every new correction row must be appended after the entire literal prior prefix')
                current_row_count += n
        proposal = trial.get('proposal')
        if proposal is not None:
            identity = proposal['identity']
            if (proposal.get('source_sha256') != HELPER_SHA
                    or identity.get('source_sha256') != HELPER_SHA
                    or identity['model_identity_sha256'] != model
                    or identity['coordinate_norm']['norm_identity_sha256'] != norm_identity
                    or identity['ambient_coordinates'] != variables
                    or identity['original_QP_rows'] != rows['selected_rows']
                    or identity['complete_QP_prefix_sha256'] != rows['frozen_complete_QP_prefix_sha256']
                    or identity['original_prefix_sha256'] != rows['literal_original_prefix_sha256']
                    or proposal['current_rows'] != current_row_count
                    or proposal['original_QP_rows'] != rows['selected_rows']
                    or proposal.get('original_QP_prefix_reselected') is not False
                    or proposal.get('same_parent_and_anchor_every_round') is not True):
                raise ValueError('A correction changed the complete original QP prefix, full variables, norm or model')
            pair = (proposal['original_anchor_step_sha256'], proposal['original_anchor_point_sha256'], proposal['anchor_alpha'])
            if anchor_identity is None:
                anchor_identity, immutable_identity = pair, canonical(identity)
            elif pair != anchor_identity or canonical(identity) != immutable_identity:
                raise ValueError('A later correction silently changed its original x or d anchor')
            if proposal.get('projection') is not None:
                projection_calls += 1
            if proposal.get('proposal_available'):
                projection = proposal.get('projection', {})
                fixed_rows = proposal.get('corrected_fixed_rows', {})
                anchor_rows = proposal.get('actual_anchor_fixed_rows', {})
                if (proposal.get('complete') is not True
                        or projection.get('numerical_feasible') is not True
                        or projection.get('rows_removed') is not False
                        or projection.get('rows') != current_row_count
                        or fixed_rows.get('complete') is not True
                        or fixed_rows.get('all_original_and_separated_rows_read') is not True
                        or len(fixed_rows.get('rows', [])) != current_row_count
                        or anchor_rows.get('complete') is not True
                        or len(anchor_rows.get('rows', [])) != current_row_count
                        or proposal['corrected_linear_violation'] > tolerance
                        or proposal['corrected_target_linear_violation'] > tolerance
                        or proposal['original_prefix_sha256_after'] != rows['literal_original_prefix_sha256']
                        or proposal['complete_QP_prefix_sha256_after'] != rows['frozen_complete_QP_prefix_sha256']):
                    raise ValueError('A proposed correction needs all-row direct linear and true fixed-row readback')
                if trial.get('independent_Az_and_model_reread') is True:
                    if (trial['corrected_coordinate_step_sha256'] != proposal['corrected_step_sha256']
                            or trial['corrected_candidate_sha256'] != proposal['candidate_coordinate_sha256']
                            or trial['old_actual_Phi'] != baseline['Phi']):
                        raise ValueError('The corrected A*z or same-Phi read belongs to another candidate')
        if trial.get('accepted'):
            if (proposal is None or proposal.get('proposal_available') is not True
                    or trial.get('independent_Az_and_model_reread') is not True):
                raise ValueError('An accepted SOC needs its complete proposal and independently reread full A*z')
            _check_actual_metric_acceptance(trial, baseline, model)
            accepted_candidates.append(('complete_separation_SOC', trial))
        summary = _trial(trial, profile, baseline, model)
        projection = {} if proposal is None else proposal.get('projection', {})
        summary.update(anchor_alpha=trial.get('anchor_alpha'), anchor_ray_index=trial.get('anchor_ray_index'),
            same_original_parent_and_anchor=trial.get('same_original_parent_and_anchor'),
            stop_reason=trial.get('stop_reason'),
            separation_added_rows=extension.get('added_rows'),
            separation_available=extension.get('extension_available'),
            separation_reason=extension.get('reason'),
            separation_current_rows=current_row_count,
            separation=extension,
            proposal_available=None if proposal is None else proposal.get('proposal_available'),
            proposal_reason=None if proposal is None else proposal.get('reason'),
            projection_status=projection.get('status'),
            projection_sweeps=projection.get('sweeps'),
            projection_seconds=projection.get('seconds'),
            projection_Gram_preparation_seconds=projection.get('preparation_seconds'),
            projection_numerical_feasible=projection.get('numerical_feasible'),
            minimum_norm_convergence_claimed=projection.get('minimum_norm_convergence_claimed'),
            independent_Az_and_model_reread=trial.get('independent_Az_and_model_reread'),
            corrected_half_objective_slope=trial.get('corrected_half_objective_slope'),
            corrected_predicted_actual_Phi_change=trial.get('corrected_predicted_actual_Phi_change'),
            old_actual_Phi=trial.get('old_actual_Phi'))
        if proposal is not None:
            summary.update({key: proposal.get(key) for key in (
                'original_QP_rows', 'current_rows', 'original_prefix_linear_violation',
                'all_current_anchor_linear_violation', 'inward_normalized_offset',
                'anchor_coordinate_norm', 'correction_norm', 'correction_over_anchor_norm',
                'corrected_coordinate_norm', 'corrected_linear_violation',
                'corrected_target_linear_violation', 'direct_Cz_minus_Cd_minus_Ce',
                'original_anchor_step_sha256', 'original_anchor_point_sha256',
                'original_prefix_sha256_after', 'complete_QP_prefix_sha256_after', 'cache')})
            fixed_rows = proposal.get('corrected_fixed_rows', {})
            summary['corrected_fixed_rows_complete'] = fixed_rows.get('complete')
            summary['corrected_fixed_rows_maximum_normalized_constraint'] = fixed_rows.get('maximum_normalized_constraint')
        soc_trials.append(summary)
    result['backtracked_anchor_and_selection'] = backtracked_anchor_and_selection(value, profile, baseline, model)
    result['actual_final_candidate_readback_count'] = result['backtracked_anchor_and_selection']['actual_final_candidate_readback_count']
    if bool(value['accepted']) != bool(accepted_candidates) or len(accepted_candidates) > 1:
        raise ValueError('Only one real accepted ray or corrected point may define this returned direction')
    if accepted_candidates:
        kind, actual = accepted_candidates[0]
        if (value.get('accepted_step_kind') != kind
                or value['accepted_statistics'] != actual['statistics']
                or value['accepted_geometry'] != actual['full_geometry']):
            raise ValueError('The reported accepted field differs from its actual accepted trial')
        if kind == 'complete_separation_SOC':
            if (value.get('accepted_alpha') is not None
                    or value.get('accepted_SOC_round') != actual['index']+1
                    or value.get('accepted_SOC_anchor_alpha') != actual['anchor_alpha']):
                raise ValueError('Do not label a corrected complete z as an original ray alpha')
        elif value.get('accepted_alpha') != actual['alpha']:
            raise ValueError('The actual accepted original ray alpha changed')
    result.update(trials=trials, soc_trials=soc_trials,
        actual_original_ray_trial_count=len(trials), actual_SOC_trial_count=len(soc_trials),
        actual_SOC_projection_calls=projection_calls,
        accepted_original_ray_count=sum(kind == 'original_ray' for kind, _ in accepted_candidates),
        accepted_SOC_count=sum(kind == 'complete_separation_SOC' for kind, _ in accepted_candidates),
        final_complete_row_count=current_row_count,
        all_original_and_prior_QP_rows_retained=True,
        finite_projection_or_QP_limit_is_convergence=False)
    compact_soc = []
    for item in soc_trials:
        geometry = item.get('geometry') or {}
        stats = item.get('statistics') or {}
        compact_soc.append(dict(index=item['index'], accepted=item['accepted'],
            anchor_alpha=item['anchor_alpha'], rows=item['separation_current_rows'],
            added_rows=item['separation_added_rows'], proposal=item['proposal_available'],
            projection_status=item['projection_status'], sweeps=item['projection_sweeps'],
            Phi=stats.get('Phi'), max_relative_gram=stats.get('max_relative_gram'),
            positive_g=item.get('actual_positive_physical_g'),
            reach_product=geometry.get('necessary_reach_product'), worst=geometry.get('worst'),
            failure_classes=item['failure_classes'], missing_checks=item['unperformed_or_missing_checks'],
            stop_reason=item['stop_reason'], proposal_reason=item['proposal_reason']))
    result['SOC_rounds_compact_json'] = json.dumps(compact_soc, separators=(',', ':'), allow_nan=False)
    compact_rays = [dict(index=item['index'], alpha=item['alpha'], accepted=item['accepted'],
        Phi=(item.get('statistics') or {}).get('Phi'),
        positive_g=item.get('actual_positive_physical_g'),
        reach_product=(item.get('geometry') or {}).get('necessary_reach_product'),
        worst=(item.get('geometry') or {}).get('worst'),
        failure_classes=item['failure_classes'], missing_checks=item['unperformed_or_missing_checks'])
        for item in trials]
    result['original_rays_compact_json'] = json.dumps(compact_rays, separators=(',', ':'), allow_nan=False)
    return result


def cache_record(report, report_path, *, verify_files):
    value = report['reference_meridian_cache']
    manifest_record = value['manifest']
    manifest_path = Path(manifest_record['path']).resolve()
    outdir = Path(report_path).resolve().parent
    directory = Path(value['cache_directory']).resolve()
    if (value.get('schema') != 'same-actual-frozen-parent-numerical-meridian-cache-v1'
            or value.get('source_sha256') != CACHE_SHA
            or manifest_path != outdir/'reference-meridian-cache-manifest.json'
            or directory != outdir/'frozen-parent-meridian-cache'
            or sha(manifest_path) != manifest_record['sha256']
            or manifest_path.stat().st_size != manifest_record['bytes']
            or value.get('operator_methods_replaced') is not False
            or value.get('unknown_entries_call_original_provider') is not True
            or value.get('no_metric_geometry_or_convergence_certificate_inherited') is not True
            or report.get('original_operator_and_provider_methods_unchanged') is not True
            or report.get('reference_cache_adoption_finished_before_first_field_read') is not True):
        raise ValueError('The exact explicit cache-adoption record changed')
    manifest = json.loads(manifest_path.read_text())
    identity = canonical({key: item for key, item in manifest.items() if key != 'manifest_identity_sha256'})
    binding = manifest['binding']
    if (manifest.get('source_sha256') != CACHE_SHA
            or manifest.get('producer_source_sha256') != DRIVER_SHA
            or identity != manifest.get('manifest_identity_sha256')
            or identity != value.get('manifest_identity_sha256')
            or canonical(binding) != manifest.get('binding_identity_sha256')
            or canonical(binding) != value.get('binding_identity_sha256')
            or binding.get('complete_field_model') != report['representation']
            or binding.get('model_identity_sha256') != report['model_identity_sha256']
            or binding.get('original_parent_report_sha256') != report['original_parent_report']['sha256']
            or binding.get('complete_input_sha256s') != dict(parent_bundle=report['bundle_sha256'],
                observation_carrier=report['observation_carrier_sha256'],
                node_report=report['exact_tail_node_report_sha256'],
                scalar_input=report['exact_tail_scalar_input_sha256'])
            or len(manifest['entries']) != value['complete_manifest_entries']
            or (report.get('complete') is True and manifest.get('completed_run_snapshot') is not True)):
        raise ValueError('The raw complete cache manifest belongs to different actual input words')
    seen, verified, byte_count = set(), 0, 0
    for entry in manifest['entries']:
        key = (entry['label'], tuple(entry['phi_hex']))
        if key in seen or entry['label'] not in ('integration', 'grid'):
            raise ValueError('Invalid duplicate or unknown complete cache address')
        seen.add(key)
        phi = [float.fromhex(word) for word in entry['phi_hex']]
        if not phi or any(not math.isfinite(x) or x.hex() != word for x, word in zip(phi, entry['phi_hex'])):
            raise ValueError('Keep every complete literal angular address')
        filename = canonical(dict(label=entry['label'], phi=entry['phi_hex']))+'.npz'
        if entry['filename'] != filename or entry['query'] != binding['queries'][entry['label']]:
            raise ValueError('Changed complete radial/angle cache address')
        shape = [entry['query']['rows'], len(phi), 3]
        if set(entry['arrays']) != {'T0', 'T0_s', 'T0_phi', 'T0_phiphi'}:
            raise ValueError('A complete normalized parent jet is missing')
        for item in entry['arrays'].values():
            if item.get('shape') != shape or item.get('dtype') != 'float64':
                raise ValueError('The cache manifest changed a complete array shape/type')
        byte_count += entry['bytes']
        if verify_files:
            path = directory/filename
            if path.is_symlink() or path.stat().st_size != entry['bytes'] or sha(path) != entry['sha256']:
                raise ValueError('An actual retained cache byte differs from the completed manifest')
            verified += 1
    result = dict(value)
    result.update(actual_raw_cache_files_rehashed=verified,
        complete_manifest_bytes_of_NPZ_files=byte_count,
        cache_arrays_recomputed_by_reader=False,
        original_provider_normalization_error_certified=False,
        cache_adoption_is_not_a_new_field_or_geometry_certificate=True)
    return result


def read_report(repo, report_path, *, verify_final_bundle=False, verify_cache_files=False):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    driver = topic/'scripts/resume_20261126/fullclosed_so3_cached_current_pcg_soc.py'
    deriver_path = topic/'scripts/resume_20261126/derive_so3_cached_current_pcg_soc.py'
    if sha(deriver_path) != DERIVER_SHA:
        raise ValueError('Bind the complete pure full-body derivation')
    spec = importlib.util.spec_from_file_location('_normalized_current_eight_column_PCQ_pure_deriver', deriver_path)
    deriver = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = deriver
    spec.loader.exec_module(deriver)
    source_derivation = deriver.bind_report(repo, report_path)
    if sha(driver) != DRIVER_SHA:
        raise ValueError('The complete actual driver body differs from the bound source')
    report = json.loads(Path(report_path).read_text())
    if report.get('schema') != REPORT_SCHEMA or report.get('source_sha256') != DRIVER_SHA:
        raise ValueError('This reader accepts only its complete actual SO3 report; no old schema relabeling')
    for role, (relative, expected) in load_pins(driver).items():
        if report['source_sha256_by_role'].get(role) != expected or sha(topic/relative) != expected:
            raise ValueError('The actual complete source role changed: '+role)
    binding_relative, binding_sha = load_pins(driver)['actual_parent_binding']
    binding_path = topic/binding_relative
    spec = importlib.util.spec_from_file_location('_SO3_pure_actual_profile_binding', binding_path)
    binder = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = binder
    spec.loader.exec_module(binder)
    fixed_profile = binder.verify_saved_binding(report, expected_binding_source_sha256=binding_sha)
    model = report['representation']
    fixed = report['fixed_scalar_metric']
    if (canonical(model) != report['model_identity_sha256']
            or model['frozen_parent_bundle_sha256'] != report['bundle_sha256']
            or fixed['identity_sha256'] != fixed_profile
            or canonical(fixed['exact_profile_definition']) != fixed_profile
            or fixed.get('target_fixed_before_first_direction') is not True
            or fixed.get('moving_mean_projection') is not False
            or fixed.get('all_metric_mean_constraints_retained') is not True
            or model['fixed_scalar_metric_identity_sha256'] != fixed_profile
            or report.get('radial_metric_error_identically_zero') is not False
            or report.get('radial_Gram_uses_complete_hprime_Delta') is not True):
        raise ValueError('Keep the one real scalar target and the actual corrected-field metric')
    norm = report['coordinate_norm']
    if canonical({key: value for key, value in norm.items() if key != 'norm_identity_sha256'}) != norm['norm_identity_sha256']:
        raise ValueError('The actual full new coordinate norm identity changed')
    initial, final = statistic(report.get('initial'), fixed_profile), statistic(report.get('final_statistics'), fixed_profile)
    if initial is not None and final is not None:
        for key in ('p', 'epsilon', 'scale', 'normalization'):
            if initial[key] != final[key]:
                raise ValueError('Never subtract Phi from different target definitions or positive measures')
    margin = report.get('restoration_interior_margin')
    if (not isinstance(margin, (int, float)) or not math.isfinite(margin) or margin <= 0
            or report.get('restoration_interior_margin_is_only_a_stricter_search_target') is not True
            or report.get('original_physical_g_and_nonlinear_acceptance_unchanged') is not True):
        raise ValueError('A strictly positive search margin must never relax the physical acceptance rule')
    preconditioner_policy = current_preconditioner_policy(report)
    soc_policy = report['complete_same_parent_SOC']
    required = ('whole_current_QP_prefix_preserved_through_every_correction',
        'same_parent_same_ray_anchor_every_round', 'no_prior_physical_covectors_or_values_inherited',
        'true_same_Phi_domain_and_full_geometry_required', 'all_original_ray_backtracking_precedes_SOC',
        'true_feasible_original_ray_fallback_required_before_SOC',
        'fallback_never_accepted_before_final_memory_readback', 'one_immutable_anchor_per_original_parent_direction',
        'failed_post_SOC_candidates_resume_remaining_original_ray_budget')
    if (any(soc_policy.get(key) is not True for key in required)
            or soc_policy.get('anchor_policy') != 'closest-eligible-larger-ray-after-first-true-feasible-ray'
            or soc_policy.get('candidate_choice_policy') != 'ascending previously-read same-Phi, then complete current-memory revalidation'
            or not isinstance(soc_policy.get('maximum_rounds'), int)
            or not 1 <= soc_policy['maximum_rounds'] <= 8
            or any(not _finite(soc_policy.get(key)) or soc_policy[key] < 0 for key in
                ('tau', 'observed_violation_inward_fraction', 'numerical_readback_tolerance'))):
        raise ValueError('Keep the entire declared post-backtracking same-parent correction and true fallback policy')
    arguments = dict(model=report['model_identity_sha256'],
        norm_identity=norm['norm_identity_sha256'], variables=report['original_variables'],
        soc_policy=soc_policy, restoration_interior_margin=margin)
    metrics = [direction(value, fixed_profile, **arguments) for value in report.get('metric_directions', [])]
    restoration = [direction(value, fixed_profile, **arguments) for value in report.get('restoration_directions', [])]
    final_geometry = geometric(report.get('final_geometry'))
    if report.get('complete') is True:
        if final is None or final_geometry is None:
            raise ValueError('A complete actual budget needs the final full field read')
        if bool(report.get('final_true_sampled_geometry_feasible')) != final_geometry['true_finite_geometry_feasible']:
            raise ValueError('A common slack or partial screen was mistaken for final physical feasibility')
        if report['actual_metric_directions'] != len(metrics) or report['actual_restoration_directions'] != len(restoration):
            raise ValueError('Only actual complete recorded directions count')
        if verify_final_bundle:
            path = Path(report['final_bundle'])
            if sha(path) != report['final_bundle_sha256']:
                raise ValueError('The actual returned full SO3 bundle differs from the source report')
    cache = cache_record(report, report_path, verify_files=verify_cache_files)
    metadata = report.get('latest_operator_metadata', {})
    return dict(schema='actual-complete-normalized-parent-current-eight-column-PCG-SOC-readout-v2',
        full_body_source_derivation=source_derivation, complete_same_parent_SOC=soc_policy,
        current_full_QP_preconditioner_policy=preconditioner_policy,
        metric_directions_using_current_PCG=sum(v['current_preconditioner']['enabled'] for v in metrics),
        metric_preparation_fallback_directions=sum(v['current_preconditioner'].get('preparation_fallback', False) for v in metrics),
        total_preparation_A_calls=sum(v['current_preconditioner']['actual_extra_A_calls'] for v in metrics),
        total_preparation_Atranspose_calls=sum(v['current_preconditioner']['actual_extra_Atranspose_calls'] for v in metrics),
        raw_small_preconditioner_matrices_published=False,
        performance_improvement_claimed=False,
        prior_separation_requires_actual_parent_restoration=report.get('prior_separation_requires_actual_parent_restoration'),
        reader_sha256=sha(__file__), report_path=str(Path(report_path).resolve()),
        report_sha256=sha(report_path), report_bytes=Path(report_path).stat().st_size,
        actual_driver_sha256=DRIVER_SHA, actual_source_commit=report['source_commit'],
        workflow_trigger_commit=report.get('workflow_trigger_commit'),
        github_run_id=report.get('github_run_id'), complete=report.get('complete') is True,
        original_parent_bundle_sha256=report['bundle_sha256'],
        model_identity_sha256=report['model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=fixed_profile,
        original_parent_source_binding=report['frozen_parent_binding'],
        actual_new_initial_bundle_sha256=report.get('initial_new_bundle', {}).get('sha256'),
        actual_final_bundle_sha256=report.get('final_bundle_sha256'),
        initial=initial, final=final,
        actual_same_objective_change=None if initial is None or final is None else final['Phi']-initial['Phi'],
        old_parent_Phi_subtracted_from_new_field=False,
        initial_geometry=geometric(report.get('initial_geometry')), final_geometry=final_geometry,
        actual_metric_directions=metrics, actual_restoration_directions=restoration,
        actual_metric_direction_count=len(metrics), actual_restoration_direction_count=len(restoration),
        accepted_original_ray_metric_directions=sum(v['accepted_original_ray_count'] for v in metrics),
        accepted_SOC_metric_directions=sum(v['accepted_SOC_count'] for v in metrics),
        actual_SOC_trial_count=sum(v['actual_SOC_trial_count'] for v in metrics),
        actual_SOC_projection_calls=sum(v['actual_SOC_projection_calls'] for v in metrics),
        actual_final_candidate_readback_count=sum(v['actual_final_candidate_readback_count'] for v in metrics),
        final_damping=report.get('final_damping'), final_restoration_damping=report.get('final_restoration_damping'),
        coordinate_norm=norm, working_evaluation=report['working_evaluation'],
        restoration_interior_margin=margin, reference_meridian_cache=cache,
        total_actual_seconds_including_cache_manifest=report.get('total_actual_seconds_including_cache_manifest'),
        maximum_requested_parent_norm_deviation_scope='fresh parent provider evaluations only; donor diagnostic separate',
        original_physical_g_and_nonlinear_acceptance_unchanged=True,
        actual_operator_counts=metadata.get('actual_counts'),
        maximum_actual_inverse_chart_residual=metadata.get('maximum_actual_inverse_chart_residual'),
        minimum_actual_inverse_root_rho=metadata.get('minimum_actual_inverse_root_rho'),
        maximum_requested_parent_norm_deviation=metadata.get('maximum_requested_parent_norm_deviation'),
        initial_position_counts=report['initial_permanent_position_counts'],
        final_position_counts=report.get('final_permanent_position_counts'),
        history=report['history'], stop_reason=report.get('stop_reason'),
        total_actual_seconds=report.get('total_actual_seconds'),
        initial_actual_setup_and_full_read_seconds=report.get('initial_actual_setup_and_full_read_seconds'),
        peak_rss_KiB=report.get('peak_rss_KiB'),
        sample_target_reached=report.get('sample_target_reached'),
        raw_scientific_arrays_recomputed=False, J_calls_by_reader=0, Jtranspose_calls_by_reader=0,
        continuous_metric_or_geometry_certified=False,
        refinement_convergence_claimed=False, closed_isometry_accepted=False,
        common_slack_residual_is_geometric_feasibility=False,
        quadrature_normalization_inverse_root_errors_certified=False,
        limitations=report.get('limitations', 'Actual incomplete numerical budget; no scientific success inferred'))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--verify-final-bundle', action='store_true')
    p.add_argument('--verify-cache-files', action='store_true')
    a = p.parse_args()
    result = read_report(a.repo, a.report, verify_final_bundle=a.verify_final_bundle,
        verify_cache_files=a.verify_cache_files)
    if a.output.exists():
        raise FileExistsError('Do not overwrite an actual previously bound readout')
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(result, separators=(',', ':'), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

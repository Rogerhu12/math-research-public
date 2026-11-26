#!/usr/bin/env python3
"""Bind the actual complete SO3 prior-separation and all-rows SOC report.

Only stdlib JSON/source/byte attribution is performed. No F/J or scientific
arrays are recomputed. Common-slack values and real nonlinear violations
remain separate. An incomplete or failed actual budget is never promoted
to a complete direction, a feasible field, or fixed-g refinement success.
"""
import argparse
import ast
import hashlib
import importlib.util
import sys
import json
import math
from pathlib import Path


DRIVER_SHA = '359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d'
HELPER_SHA = '02875e4a150644f8addb6073b346e2de3b0f3cf50498e9cf6efe8fe0333d7c97'
DERIVER_SHA = 'fea20e0b00fc55bc00d450947154a3f17de5a9ee4a71b0ea4b0aec7082ba1aa4'
REPORT_SCHEMA = 'complete-independent-axisymmetric-fixed-deep-so3-prior-separation-and-SOC-v1'


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
        unperformed_or_missing_checks_json=json.dumps(missing, separators=(',', ':')))


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


def direction(value, profile, *, model, norm_identity, variables, soc_policy):
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
                or quadratic['original_rows'] != rows['selected_rows']):
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


def read_report(repo, report_path, *, verify_final_bundle=False):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    driver = topic/'scripts/resume_20261126/fullclosed_axisymmetric_so3_separation_soc.py'
    deriver_path = topic/'scripts/resume_20261126/derive_axisymmetric_so3_soc.py'
    if sha(deriver_path) != DERIVER_SHA:
        raise ValueError('Bind the complete pure full-body source deriver')
    spec = importlib.util.spec_from_file_location('_actual_SO3_complete_source_deriver', deriver_path)
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
    model = report['representation']
    fixed = report['fixed_scalar_metric']
    reference = model['complete_axisymmetric_reference_model']
    profile = reference['fixed_scalar_metric_identity_sha256']
    if (canonical(model) != report['model_identity_sha256']
            or model['initial_reference_bundle_sha256'] != report['bundle_sha256']
            or canonical(reference) != model['initial_reference_model_identity_sha256']
            or canonical(reference['fixed_scalar_profile_definition']) != profile
            or fixed['exact_profile_definition'] != reference['fixed_scalar_profile_definition']
            or report['independent_reference_binding']['reference_model_identity_sha256'] != canonical(reference)
            or report['independent_reference_binding']['fixed_scalar_metric_identity_sha256'] != profile
            or reference['source_sha256'] != report['source_sha256_by_role']['reference']
            or fixed['identity_sha256'] != profile
            or canonical(fixed['exact_profile_definition']) != profile
            or fixed.get('target_fixed_before_first_direction') is not True
            or fixed.get('moving_mean_projection') is not False
            or fixed.get('all_metric_mean_constraints_retained') is not True
            or model['fixed_scalar_metric_identity_sha256'] != profile
            or report.get('radial_metric_error_identically_zero') is not False
            or report.get('radial_Gram_uses_complete_hprime_Delta') is not True):
        raise ValueError('Keep the one real scalar target and the actual corrected-field metric')
    norm = report['coordinate_norm']
    if canonical({key: value for key, value in norm.items() if key != 'norm_identity_sha256'}) != norm['norm_identity_sha256']:
        raise ValueError('The actual full new coordinate norm identity changed')
    initial, final = statistic(report.get('initial'),profile), statistic(report.get('final_statistics'),profile)
    if initial is not None and final is not None:
        for key in ('p', 'epsilon', 'scale', 'normalization'):
            if initial[key] != final[key]:
                raise ValueError('Never subtract Phi from different target definitions or positive measures')
    soc_policy = report['complete_same_parent_SOC']
    if (soc_policy.get('whole_current_QP_prefix_preserved_through_every_correction') is not True
            or soc_policy.get('same_parent_same_ray_anchor_every_round') is not True
            or soc_policy.get('no_prior_physical_covectors_or_values_inherited') is not True
            or soc_policy.get('true_same_Phi_domain_and_full_geometry_required') is not True):
        raise ValueError('The complete source report must retain all stated same-parent correction responsibilities')
    arguments = dict(model=report['model_identity_sha256'],
        norm_identity=norm['norm_identity_sha256'], variables=report['original_variables'],
        soc_policy=soc_policy)
    metrics = [direction(value,profile,**arguments) for value in report.get('metric_directions', [])]
    restoration = [direction(value,profile,**arguments) for value in report.get('restoration_directions', [])]
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
    metadata = report.get('latest_operator_metadata', {})
    return dict(schema='actual-complete-independent-axisymmetric-SO3-separation-SOC-scalar-readout-v1',
        full_body_source_derivation=source_derivation, complete_same_parent_SOC=soc_policy,
        prior_separation_requires_actual_parent_restoration=report.get('prior_separation_requires_actual_parent_restoration'),
        reader_sha256=sha(__file__), report_path=str(Path(report_path).resolve()),
        report_sha256=sha(report_path), report_bytes=Path(report_path).stat().st_size,
        actual_driver_sha256=DRIVER_SHA, actual_source_commit=report['source_commit'],
        workflow_trigger_commit=report.get('workflow_trigger_commit'),
        github_run_id=report.get('github_run_id'), complete=report.get('complete') is True,
        initial_reference_bundle_sha256=report['bundle_sha256'],
        model_identity_sha256=report['model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=profile,
        independent_reference_binding=report['independent_reference_binding'],
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
        final_damping=report.get('final_damping'), final_restoration_damping=report.get('final_restoration_damping'),
        coordinate_norm=norm, working_evaluation=report['working_evaluation'],
        actual_operator_counts=metadata.get('actual_counts'),
        maximum_actual_inverse_chart_residual=metadata.get('maximum_actual_inverse_chart_residual'),
        minimum_actual_inverse_root_rho=metadata.get('minimum_actual_inverse_root_rho'),
        maximum_requested_reference_norm_deviation=metadata.get('maximum_requested_reference_norm_deviation'),
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
    a = p.parse_args()
    result = read_report(a.repo, a.report, verify_final_bundle=a.verify_final_bundle)
    if a.output.exists():
        raise FileExistsError('Do not overwrite an actual previously bound readout')
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(result, separators=(',', ':'), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

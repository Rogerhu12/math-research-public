#!/usr/bin/env python3
"""Bind the complete actual R696 angular-unit fixed-scalar report.

Only stdlib JSON/source/byte attribution is performed. No F/J or scientific
arrays are recomputed. Common-slack values and real nonlinear violations
remain separate. An incomplete or failed actual budget is never promoted
to a complete direction, a feasible field, or fixed-g refinement success.
"""
import argparse
import ast
import hashlib
import json
import math
from pathlib import Path


DRIVER_SHA = '7b7cc0c9b27a0339debab0319c6854323dfc6c21f3e92c64946cbffc70824c7d'
REPORT_SCHEMA = 'complete-R696-angular-unit-fixed-deep-QP-v1'


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


def direction(value, profile):
    phase = value['phase']
    if phase not in ('metric', 'restoration'):
        raise ValueError('The complete report used an undeclared scientific phase')
    rows = value['complete_selected_inequalities']
    if (rows.get('no_original_row_removed') is not True
            or rows['original_prefix_rows']+rows['appended_amplitude_rows'] != rows['selected_rows']
            or len(rows['rows']) != rows['selected_rows']):
        raise ValueError('A full selected geometry/amplitude prefix was dropped or miscounted')
    if phase == 'restoration':
        quadratic = value['quadratic_model']
        if (quadratic.get('all_original_rows_retained') is not True
                or quadratic.get('physical_feasibility_inferred_from_slack') is not False
                or quadratic['original_rows'] != rows['selected_rows']):
            raise ValueError('Do not drop any typed row or interpret slack as physical feasibility')
    qp = value['qp']
    result = dict(index=value['index'], serial=value['serial'], phase=phase,
        accepted=value['accepted'], accepted_alpha=value.get('accepted_alpha'),
        damping=value['actual_damping'], damping_after=value.get('damping_after_direction'),
        qp_status=qp['status'], actual_advances=qp['advances'],
        final_face_projected_gradient_norm=qp.get('final_face_projected_gradient_norm'),
        qp_tolerance=qp.get('gradient_tolerance'),
        active_face_rows=qp.get('active_face', {}).get('active_rows'),
        active_face_indices=qp.get('active_face', {}).get('active_indices'),
        actual_operator_products=qp.get('operator_products'),
        maximum_linear_violation=qp.get('maximum_linear_violation'),
        original_geometry_rows=rows['original_prefix_rows'],
        amplitude_rows=rows['appended_amplitude_rows'], total_rows=rows['selected_rows'],
        row_cache_bytes=rows['row_cache_bytes'],
        duplicate_prefix_cache_bytes=rows.get('duplicate_prefix_cache_bytes'),
        actual_QP_seconds=value.get('actual_QP_seconds'),
        actual_complete_direction_seconds=value['seconds'],
        actual_QP_operator_counts=value.get('actual_QP_operator_counts'),
        actual_complete_direction_operator_counts=value.get('actual_complete_direction_operator_counts'),
        starting_statistics=statistic(value['starting_statistics'],profile),
        starting_geometry=geometric(value['starting_geometry']),
        accepted_statistics=statistic(value.get('accepted_statistics'),profile),
        accepted_geometry=geometric(value.get('accepted_geometry')),
        maximum_selected_linear_physical_g=value.get('maximum_selected_linear_physical_g'),
        old_actual_positive_physical_g=value['old_actual_maximum_positive_physical_g'],
        computed_common_slack=value.get('computed_common_slack'),
        common_slack_is_true_feasibility=False,
        trial_count=len(value['trials']))
    if value.get('accepted_bundle') is not None:
        result['accepted_bundle_sha256'] = value['accepted_bundle']['sha256']
    trials = []
    for trial in value['trials']:
        if trial.get('accepted') and trial.get('full_true_geometry_read') is not True:
            raise ValueError('No numerical trial may be accepted without its complete true-field geometry')
        if phase == 'metric' and trial.get('accepted') and (
                trial.get('actual_Phi_descent') is not True
                or not geometric(trial.get('full_geometry'))['true_finite_geometry_feasible']):
            raise ValueError('A metric direction must have actual same-objective descent and true geometry')
        if phase == 'restoration' and trial.get('accepted') and not (
                isinstance(trial.get('actual_positive_physical_g'), (int, float))
                and trial['actual_positive_physical_g'] < value['old_actual_maximum_positive_physical_g']):
            raise ValueError('A restored trial needs real physical violation decrease, independently of tau')
        trials.append(dict(index=trial['index'], alpha=trial['alpha'], accepted=trial['accepted'],
            actual_Phi_descent=trial.get('actual_Phi_descent'),
            actual_positive_physical_g=trial.get('actual_positive_physical_g'),
            full_true_geometry_read=trial.get('full_true_geometry_read'),
            true_finite_geometry_feasible=trial.get('physically_feasible'),
            actual_seconds=trial.get('actual_seconds'), actual_read_error=trial.get('actual_read_error')))
    result['trials'] = trials
    return result


def read_report(repo, report_path, *, verify_final_bundle=False):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    driver = topic/'scripts/resume_20261126/fullclosed_angular_unit_qp.py'
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
            or report.get('angular_metric_error_identically_zero') is not True
            or report.get('actual_all_three_working_Gram_entries_read') is not True
            or report.get('centered_primitive_s_and_ss_derivatives_complete') is not True
            or model.get('schema') != 'complete-R696-angular-unit-centered-field-v1'
            or model.get('angular_Gram_error_identically_zero') is not True
            or model.get('all_free_radial_profile_jets_retained') is not True
            or model.get('closed_angular_sections_identically') is not True
            or model.get('vertical_profile', {}).get('r_independent_of_angle') is not True):
        raise ValueError('Keep the same fixed scalar and the full actual R696 angular field')
    norm = report['coordinate_norm']
    free = report['all_new_free_variables']
    if (norm.get('schema') != 'complete-R696-positive-node-jet-H2-type-norm-v1'
            or free['core']+free['rotation']+free['radial_profile']+free['height'] != free['total']
            or free['radial_profile'] != 3*int(report['J'])-6
            or free['total'] != report['original_variables']
            or free['total'] != norm['free_variables']):
        raise ValueError('The complete new radial-profile, core, rotation, and height norm must be retained')
    if canonical({key: value for key, value in norm.items() if key != 'norm_identity_sha256'}) != norm['norm_identity_sha256']:
        raise ValueError('The actual full new coordinate norm identity changed')
    initial, final = statistic(report.get('initial'),profile), statistic(report.get('final_statistics'),profile)
    if initial is not None and final is not None:
        for key in ('p', 'epsilon', 'scale', 'normalization'):
            if initial[key] != final[key]:
                raise ValueError('Never subtract Phi from different target definitions or positive measures')
    metrics = [direction(value,profile) for value in report.get('metric_directions', [])]
    restoration = [direction(value,profile) for value in report.get('restoration_directions', [])]
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
    return dict(schema='actual-complete-R696-angular-unit-scalar-readout-v1',
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
        final_damping=report.get('final_damping'), final_restoration_damping=report.get('final_restoration_damping'),
        coordinate_norm=norm, working_evaluation=report['working_evaluation'],
        actual_operator_counts=metadata.get('actual_counts'),
        maximum_actual_inverse_chart_residual=metadata.get('maximum_actual_inverse_chart_residual'),
        minimum_actual_inverse_root_rho=metadata.get('minimum_actual_inverse_root_rho'),
        all_new_free_variables=free,
        maximum_scalar_a_carrier_error_upper=metadata.get('scalar_a_carrier_error_upper'),
        maximum_four_scalar_jet_error_carriers=metadata.get('maximum_four_scalar_jet_error_carriers'),
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

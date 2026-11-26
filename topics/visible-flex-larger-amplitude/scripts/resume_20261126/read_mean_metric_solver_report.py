#!/usr/bin/env python3
"""Source-bound R684/R688 solver attribution from already returned JSON.

This reader imports only byte-bound stdlib report/derivation helpers.  It
does not import the scientific driver, load a bundle, evaluate a field,
apply J/J*, assemble a coarse matrix, or run another numerical fixture.
The scalar arithmetic is an ordinary floating diagnostic, not an outward
optimality or continuous geometry certificate.  Public Actions only.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys


BASE_SCHEMA = 'R684-fullclosed-rotational-mean-metric-design-QP-v1'
FACE_SCHEMA = 'R688-fullclosed-rotational-mean-metric-face-PCG-v1'
BASE_SHA = '2d44a097e614f917fa133b1042e0fc7c6cdcb32a10b72d1bc2ac6362d54a94c3'
DERIVER_SHA = 'b57ab303682f708c6d205cf0d527df2ec16aa2cfa1762a59070599abcade6d75'
SCALAR_SHA = '9124229786200659f1c9dc73620eecd75dda6493990f684149471d7003263b9d'
BASE_RUNTIME = dict(
    mean_transform='b7eb35d5e7c1d32baf8d4e94c0c9651d46d5cbfea65a6c1c098ae24d42f0b624',
    spectral='e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91',
    spectral_hessian='29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4',
    qp='fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4',
    point='fe8e926c3239d707d6af48efbc48c1755bbac84c3d5722bdbf40f7be7bb53cad',
    exact_tail='2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_bound(name, path, digest):
    if sha(path) != digest:
        raise ValueError('A required complete stdlib source differs: '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def divide(numerator, denominator):
    return numerator/denominator if finite(numerator) and finite(denominator) and denominator > 0 else None


def choose(value, keys):
    value = value or {}
    return {key: value.get(key) for key in keys}


def stats(value):
    value = value or {}
    return dict(**choose(value, ('max_relative_gram', 'legacy_max_relative_gram',
        'rho_sample_min', 'min_relative_E', 'min_relative_determinant',
        'radial_weighted_mean_sse', 'old_fixed_metric_max_diagnostic')),
        spectral=choose(value.get('spectral'), ('p', 'epsilon', 'scale',
            'phi_normalized', 'centered_phi_normalized', 'phi_zero', 'max_gram')))


def bind_report(report, driver, repo):
    """Bind the entire accepted base body or exact complete R688 derivation."""
    if report.get('objective') != 'spectral':
        raise ValueError('This reader describes the declared spectral mean-metric runs')
    schema = report.get('schema')
    actual = Path(driver).resolve()
    if not actual.is_file() or sha(actual) != report.get('source_sha256'):
        raise ValueError('Need source bytes matching the actual complete report driver SHA')
    if report.get('diameter_diagnostic_sha256') != report.get('source_sha256'):
        raise ValueError('The report geometry reader is not bound to this same whole driver')
    roles = report.get('source_sha256_by_role') or {}
    if schema == BASE_SCHEMA:
        if sha(actual) != BASE_SHA:
            raise ValueError('The complete R684 body differs from its published v3/exact-memory source')
        for role, digest in BASE_RUNTIME.items():
            if roles.get(role) != digest:
                raise ValueError('The actual R684 component identity differs: '+role)
        binding = dict(kind='complete_published_R684_body', complete_driver_sha256=BASE_SHA,
            complete_report_and_source_binding=True, runtime_sources=BASE_RUNTIME)
        objective_key = 'phi_normalized'
    elif schema == FACE_SCHEMA:
        source = Path(repo)/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/derive_mean_metric_face_pcg.py'
        deriver = load_bound('actual_R688_complete_report_binder', source, DERIVER_SHA)
        binding = deriver.bind_report(report, actual, repo)
        binding['kind'] = 'complete_frozen_body_R688_derivation'
        objective_key = report.get('selected_scalar_objective_key')
        if objective_key not in ('phi_normalized', 'centered_phi_normalized'):
            raise ValueError('The actual R688 scalar objective selection is missing or unsupported')
        for role in ('point', 'exact_tail'):
            if roles.get(role) != BASE_RUNTIME[role]:
                raise ValueError('The same canonical actual physical point source is required: '+role)
        selected = (report.get('mean_coarse_source_binding') or {}).get('selected_scalar_objective_key')
        if selected != objective_key:
            raise ValueError('The whole report has conflicting selected scalar objective keys')
    else:
        raise ValueError('Only source-bound R684 and R688 design reports are accepted')
    design = report.get('mean_metric_design') or {}
    if design.get('averaging') not in ('physical', 'material') or design.get('final_metric_frozen') is not False:
        raise ValueError('Keep moving-mean design separate from later fixed-target refinement')
    binding.update(actual_source_read=str(actual), actual_source_read_sha256=sha(actual),
        recorded_runtime_driver=report.get('diameter_diagnostic_source'),
        source_path_relocated=str(actual) != report.get('diameter_diagnostic_source'),
        scientific_driver_imported=False)
    return binding, objective_key


def compact_geometry(value):
    return choose(value, ('complete', 'maximum_absolute_principal_curvature',
        'closed_body_diameter_point_lower', 'worst', 'maximum_radius_point',
        'min_area', 'evaluated_points', 'additional_witness_point_count'))


def trial_view(trial, direction, objective_key):
    """Report tested failure conditions; an unperformed geometry read is unknown."""
    old = direction.get('old_merit')
    merit, alpha, slope = (trial.get('merit'), trial.get('alpha'),
                           direction.get('half_objective_slope'))
    gain = old-merit if finite(old) and finite(merit) else None
    predicted_change = direction.get('quadratic_predicted_actual_change')
    data_energy = (predicted_change-2*slope
        if finite(predicted_change) and finite(slope) else None)
    predicted_gain = (-(2*alpha*slope+alpha*alpha*data_energy)
        if all(finite(v) for v in (alpha, slope, data_energy)) else None)
    armijo = (old+2e-4*alpha*slope if slope < 0 else old
        ) if all(finite(v) for v in (old, alpha, slope)) else None
    filter_value = trial.get('curvature_filter')
    geometry_evaluated = filter_value is not None and trial.get('curvature_points') is not None
    failures = []
    unknown = []
    if trial.get('finite') is False:
        failures.append('nonfinite_metric_or_reported_arithmetic_failure')
    elif trial.get('finite') is not True:
        unknown.append('finite_metric_flag_missing')
    if trial.get('feasible') is False and trial.get('finite') is True:
        failures.append('sampled_rho_or_relative_metric_regularity_failed')
    elif trial.get('feasible') is not True and trial.get('finite') is True:
        unknown.append('sampled_regularity_flag_missing')
    if trial.get('descent') is False:
        if gain is not None and gain <= 0:
            failures.append('same_objective_not_strictly_decreased')
        elif gain is not None and gain > 0:
            failures.append('same_objective_decreased_but_declared_Armijo_test_failed')
        else:
            failures.append('true_objective_descent_failed_without_finite_gain')
    elif trial.get('descent') is not True:
        unknown.append('true_objective_descent_flag_missing')
    if geometry_evaluated:
        if filter_value.get('passed') is False:
            failures.append('actual_sampled_curvature_filter_failed')
        elif filter_value.get('passed') is not True:
            unknown.append('actual_geometry_filter_pass_missing')
    else:
        unknown.append('geometry_not_evaluated_on_this_trial')
    accepted_flags = all(trial.get(key) is True for key in ('finite', 'feasible', 'descent', 'curvature_feasible'))
    accepted_record = bool(direction.get('accepted') and alpha == direction.get('accepted_alpha'))
    if accepted_record and (not accepted_flags or not geometry_evaluated or not filter_value.get('passed')):
        raise ValueError('The claimed accepted R684/R688 ray lacks its required actual nonlinear reads')
    peak = (trial.get('statistics') or {}).get('spectral') or {}
    scalar_in_stats = peak.get(objective_key)
    return dict(**choose(trial, ('index', 'alpha', 'finite', 'feasible', 'descent',
        'curvature_feasible', 'arithmetic_error', 'merit')),
        accepted_actual_ray=accepted_record, failure_classes=failures,
        failure_classes_json=json.dumps(failures, separators=(',', ':')),
        unperformed_or_missing_checks_json=json.dumps(unknown, separators=(',', ':')),
        unperformed_or_missing_checks=unknown,
        geometry_actually_evaluated=geometry_evaluated,
        default_true_geometry_flag_is_not_a_pass_when_not_evaluated=True,
        selected_scalar_objective_key=objective_key,
        selected_scalar_in_statistics=scalar_in_stats,
        merit_equals_selected_returned_statistic=(merit == scalar_in_stats) if finite(merit) else None,
        actual_same_objective_gain=gain,
        unregularized_model_gain_at_THIS_alpha=predicted_gain,
        actual_to_THIS_alpha_model_gain=divide(gain, predicted_gain),
        Armijo_upper_threshold=armijo,
        curvature_filter=filter_value, curvature=compact_geometry(trial.get('curvature_points')),
        statistics=stats(trial.get('statistics')),
        new_permanent_curvature_locations=trial.get('new_permanent_curvature_locations', []),
        new_permanent_radius_locations=trial.get('new_permanent_radius_locations', []))


def final_face(qp):
    transitions = qp.get('transitions') or []
    changes = [item for item in transitions
        if item.get('kind', '').startswith('release_negative_multiplier')
        or (item.get('kind') in ('blocking_step', 'zero_length_blocker') and item.get('added') is True)]
    last = changes[-1] if changes else None
    boundary = last.get('advances', 0) if last is not None else 0
    history = qp.get('history') or []
    tail = [item for item in history if finite(item.get('iteration')) and item['iteration'] > boundary]
    pg = qp.get('final_face_projected_gradient_norm')
    start_pg = tail[0].get('projected_gradient_norm_before') if tail else None
    tail_keys = ('iteration', 'objective', 'data_objective', 'projected_gradient_norm_before',
        'projected_gradient_norm_after', 'preconditioned_projected_gradient_energy_before',
        'preconditioned_projected_gradient_energy_after', 'same_face_advances_through_step',
        'active_rows', 'blocker', 'restart_reason', 'direction_kind', 'residual_replacement')
    return dict(active_face=qp.get('active_face'), last_recorded_face_change=last,
        last_face_change_after_advance=boundary, advances_recorded_on_final_face=len(tail),
        final_face_history_first=choose(tail[0], tail_keys) if tail else None,
        final_face_history_last_up_to_eight=[choose(item, tail_keys) for item in tail[-8:]],
        final_actual_Pg=pg, initial_recorded_Pg_on_final_face=start_pg,
        final_actual_to_initial_same_face_Pg_ratio=divide(pg, start_pg),
        final_normalized_release_diagnostics=qp.get('final_normalized_release_diagnostics'),
        face_bound_is_not_a_bound_after_releasing_rows=True,
        changes=dict(additions=sum(item.get('kind') in ('blocking_step', 'zero_length_blocker')
            and item.get('added') is True for item in transitions),
            releases=sum(item.get('kind', '').startswith('release_negative_multiplier') for item in transitions)),
        last_transitions=transitions[-8:], last_restarts=(qp.get('restarts') or [])[-8:],
        last_actual_residual_replacements=(qp.get('residual_replacements') or [])[-4:])


def preconditioner_view(direction, qp, face_schema):
    detail = direction.get('mean_coarse_preconditioner')
    if not face_schema:
        return dict(coarse_preparation_in_complete_driver=False,
            actual_preconditioner_counts=None, source_proved_original_v3_path=True)
    if not isinstance(detail, dict):
        raise ValueError('An R688 direction must retain its actual preparation record')
    fixed = qp.get('fixed_preconditioner') or {}
    face = fixed.get('face_metric') or {}
    gram = detail.get('current_mean_coarse_data_Gram') or {}
    return dict(coarse_preparation_in_complete_driver=True,
        preparation=choose(detail, ('status', 'construction_seconds', 'failure',
            'fallback_to_frozen_v3', 'actual_direction_damping', 'background_inverse_scale',
            'actual_operator_entry_calls', 'actual_operator_call_scope',
            'operator_instrumentation_complete', 'actual_additional_J_calls',
            'actual_additional_Jstar_calls', 'all_observed_J_and_Jstar_entries_zero',
            'all_observed_residual_entries_zero', 'outer_A_entry_counts_during_preparation',
            'temporary_method_wrappers_restored', 'actual_QP_schema', 'actual_QP_status',
            'frame_and_factor_released_after_solve', 'automatic_retry_or_changed_target')),
        Gram=choose(gram, ('schema', 'status', 'elapsed_seconds', 'coarse_variables', 'full_field_M',
            'rows', 'stages', 'evaluated_angles', 'p', 'epsilon', 'spectral_scale',
            'raw_coarse_diagonal_minimum', 'raw_negative_diagonal_count',
            'raw_coarse_maximum_absolute_entry', 'signed_low_rank_cancellation',
            'eigenvalue_clipping', 'jitter_added', 'actual_x_sha256',
            'actual_NEW_relative_residual_sha256', 'actual_mean_E_sha256', 'actual_mean_C_sha256')),
        actual_fixed_preconditioner_enabled=fixed.get('enabled'),
        actual_PCG_application_counts=fixed.get('applications'),
        constrained_face_metric=choose(face, ('schema', 'current_mode',
            'current_active_indices', 'current_QR_rebuild_count', 'applications',
            'global_B_applications', 'global_B_seconds', 'preparation_seconds',
            'maximum_cached_vectors', 'maximum_cached_vector_bytes',
            'maximum_observed_Schur_skew', 'fallback_faces', 'preparation_history')),
        independent_operator_product_counts_must_not_sum_nested_wrapper_and_base_entries=True,
        speedup_claimed=False)


def analyze(report, scalar, objective_key):
    parent = report.get('initial') or {}
    directions = []
    for direction in report.get('directions', []):
        qp = direction.get('qp') or {}
        parent_phi = (parent.get('spectral') or {}).get(objective_key)
        if direction.get('old_merit') != parent_phi:
            raise ValueError('The next ray old objective does not match its actual accepted same-functional parent')
        view = scalar.analyze_direction(direction, parent, report)
        view.pop('scalar_followup', None)
        view['ray_bound_scope'] = ('Only this parent and selected first-order C rows. '
            'The same declared moving-mean functional and every permanent geometry point are reread on each actual trial.')
        trials = [trial_view(item, direction, objective_key) for item in direction.get('trials', [])]
        accepted = [item for item in trials if item['accepted_actual_ray']]
        if bool(direction.get('accepted')) != (len(accepted) == 1):
            raise ValueError('The actual accepted ray must be uniquely identified')
        q0, qz = qp.get('initial_data_objective'), qp.get('final_regularized_objective')
        pg, tolerance = qp.get('final_face_projected_gradient_norm'), qp.get('gradient_tolerance')
        item = dict(**choose(direction, ('index', 'accepted', 'accepted_alpha',
            'accepted_bundle_sha256', 'old_merit', 'new_merit', 'damping',
            'damping_after_direction', 'seconds', 'preparation_and_linear_seconds',
            'coordinate_norm', 'height_step', 'actual_to_full_step_predicted_decrease')),
            selected_scalar_objective_key=objective_key,
            actual_gain=accepted[0]['actual_same_objective_gain'] if accepted else 0.0,
            actual_to_accepted_alpha_model_gain=accepted[0]['actual_to_THIS_alpha_model_gain'] if accepted else None,
            QP=dict(**choose(qp, ('schema', 'status', 'advances', 'maxiter', 'seconds',
                'initial_gradient_norm', 'gradient_tolerance', 'final_face_projected_gradient_norm',
                'maximum_linear_violation', 'maximum_complementarity_residual',
                'minimum_multiplier', 'longest_same_face_advances', 'maximum_active_face_rank',
                'operator_products', 'row_matvec_calls', 'row_load_calls',
                'final_actual_linear_residual_relative_defect', 'reliable_update')),
                q0=q0, qz_regularized=qz, qz_data=qp.get('final_data_objective'),
                achieved_regularized_model_gain=q0-qz if finite(q0) and finite(qz) else None,
                Pg_over_reported_tolerance=divide(pg, tolerance),
                reported_gradient_threshold_satisfied=(pg <= tolerance)
                    if finite(pg) and finite(tolerance) else None,
                virtual_q0_is_not_actual_Phi=True,
                iteration_limit_is_not_convergence=True),
            actual_full_J_entry_counts=direction.get('inner_counts'),
            explicit_outside_inner_calls=direction.get('outside_inner_calls'),
            spectral_model_blocks=(direction.get('quadratic_model') or {}).get('bridge', {}).get('blocks'),
            original_QP_scalar_attribution=view, final_face=final_face(qp),
            preconditioner=preconditioner_view(direction, qp, report['schema'] == FACE_SCHEMA),
            actual_trials=trials, actual_trial_count=len(trials),
            geometry_failure_with_true_Phi_descent=any(
                item['descent'] is True and 'actual_sampled_curvature_filter_failed' in item['failure_classes']
                for item in trials),
            amplitude_inequalities_implemented_in_these_bound_bodies=False,
            finite_Phi_drop_does_not_pay_held_amplitude_or_continuous_geometry=True)
        directions.append(item)
        if accepted:
            raw = [trial for trial in direction['trials'] if trial.get('alpha') == direction.get('accepted_alpha')]
            if len(raw) != 1:
                raise ValueError('Ambiguous actual accepted parent statistics')
            parent = raw[0]['statistics']
    return directions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--driver', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('Returned-scalar attribution is executed in the public repository Actions')
    if args.out.exists():
        raise FileExistsError('Use a new report-attribution output')
    report = json.loads(args.report.read_text())
    driver = args.driver or Path(report['diameter_diagnostic_source'])
    if not driver.is_file() and report.get('schema') == BASE_SCHEMA and args.driver is None:
        driver = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_mean_metric_design_qp.py'
    binding, objective_key = bind_report(report, driver, args.repo)
    source = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/full_phi_qp_scalar_diagnostics.py'
    scalar = load_bound('actual_mean_QP_returned_scalar_algebra', source, SCALAR_SHA)
    directions = analyze(report, scalar, objective_key)
    final_stats = report.get('final_statistics', report.get('current', report.get('initial', {})))
    result = scalar.sanitize(dict(schema='actual-R684-R688-mean-QP-source-bound-attribution-v1',
        source_sha256=sha(__file__), scalar_source_sha256=SCALAR_SHA,
        report=str(args.report.resolve()), report_sha256=sha(args.report),
        report_schema=report.get('schema'), report_complete=report.get('complete'),
        actual_complete_driver=binding, returned_report_run_id=report.get('github_run_id'),
        reader_run_id=os.environ.get('GITHUB_RUN_ID'),
        input_bundle_sha256=report.get('bundle_sha256'),
        final_bundle_sha256=report.get('final_bundle_sha256'),
        observation_carrier_sha256=report.get('observation_carrier_sha256'),
        mean_metric_design=report.get('mean_metric_design'), radial_weights=report.get('radial_weights'),
        selected_scalar_objective_key=objective_key,
        initial=stats(report.get('initial')), final=stats(final_stats),
        initial_damping=report.get('initial_damping'), final_damping=report.get('final_damping'),
        initial_known_point_filter=report.get('initial_curvature_filter'),
        final_known_point_filter=report.get('final_curvature_filter'),
        final_permanent_position_counts=report.get('final_permanent_position_counts'),
        sampled_target_reached=report.get('sample_target_reached'), directions=directions,
        scientific_arrays_read=0, field_evaluations=0, J_calls=0, Jtranspose_calls=0,
        new_fixtures=0, strict_arithmetic=False, speedup_claimed=False,
        fixed_g_refinement_claimed=False, continuous_metric_or_geometry_claimed=False,
        interpretation='Actual returned same-functional scalars only. Inner QP stationarity, selected linear feasibility, nonlinear Phi acceptance, held amplitude and continuous geometry are separate. No causal speed comparison across different parents is inferred.'))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, separators=(',', ':'), allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(args.out.resolve()), sha256=sha(args.out),
        bytes=args.out.stat().st_size, source_binding=binding,
        final=result['final'], final_filter=result['final_known_point_filter'],
        directions=[dict(index=item['index'], accepted=item['accepted'],
            accepted_alpha=item['accepted_alpha'], actual_gain=item['actual_gain'],
            QP=item['QP'], final_face=item['final_face'],
            preconditioner=item['preconditioner'], trials=item['actual_trials'])
            for item in result['directions']]), separators=(',', ':'), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

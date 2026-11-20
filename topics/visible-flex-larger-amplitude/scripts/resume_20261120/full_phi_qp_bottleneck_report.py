#!/usr/bin/env python3
"""Actions-only scalar diagnosis of returned full-Phi QP directions.

Reads existing JSON only. Reuses R673 scalar energies and adds literal
CG-history/face-transition accounting and every recorded nonlinear trial.
No arrays, field functions, J/J* products, new searches, or fixtures.
The complete analysis stays in work; direction_table is a compact public
selection and never substitutes for the actual returned report.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys


SCALAR_SHA = '9124229786200659f1c9dc73620eecd75dda6493990f684149471d7003263b9d'
V2_SHA = 'c131b45649e87be2e7f71088d817edb6402a74a4cb50a6b13018e252217f88f7'
V2_SCHEMA = 'fullspace-feasible-active-set-cg-early-release-v2'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def quotient(a, b):
    return a/b if number(a) and number(b) and b > 0 else None


def linear_history(qp, report):
    history, transitions = qp.get('history', []), qp.get('transitions', [])
    advances = qp.get('advances', 0)
    transition_counts = Counter(item.get('kind', 'missing_kind') for item in transitions)
    changes = []
    for item in transitions:
        kind = item.get('kind', '')
        changed = ((kind in ('blocking_step', 'zero_length_blocker') and item.get('added') is True)
                   or kind.startswith('release_negative_multiplier'))
        if changed:
            changes.append(int(item.get('advances', 0)))
    changes = sorted(set(v for v in changes if 0 <= v <= advances))
    boundaries = sorted(set([0, advances, *changes]))
    segments = []
    for left, right in zip(boundaries, boundaries[1:]):
        rows = [r for r in history if left < r.get('iteration', -1) <= right]
        segments.append(dict(after_advance=left, through_advance=right,
            advances=right-left, unblocked_advances=sum(r.get('blocker') is None for r in rows),
            last_step_clipped=bool(rows and rows[-1].get('blocker') is not None)))
    exact_v2 = (qp.get('schema') == V2_SCHEMA
                and report.get('source_sha256_by_role', {}).get('qp') == V2_SHA)
    known_interval = 32 if exact_v2 else qp.get('reliable_update', {}).get('interval')
    refreshes = []
    if isinstance(known_interval, int) and known_interval > 0:
        by_iteration = {row.get('iteration'): row for row in history}
        for iteration in range(known_interval, advances+1, known_interval):
            row = by_iteration.get(iteration)
            refreshes.append(dict(advance=iteration,
                recorded_history_present=row is not None,
                active_rows_before_step=None if row is None else row.get('active_rows'),
                blocking_row=None if row is None else row.get('blocker'),
                face_change_at_same_advance=iteration in changes,
                subsequent_advance_exists=iteration < advances,
                v2_unconditional_restart_on_unblocked_step=bool(exact_v2 and row is not None
                                                              and row.get('blocker') is None),
                regularized_objective=None if row is None else row.get('objective'),
                data_objective=None if row is None else row.get('data_objective')))
    actual_products = qp.get('operator_products', {})
    expected_v2 = (dict(matvec=advances, rmatvec=advances+2+advances//32)
                   if exact_v2 else None)
    changed_set = set(changes)
    forced_same_face = [r['advance'] for r in refreshes
        if r['v2_unconditional_restart_on_unblocked_step']
        and r['subsequent_advance_exists'] and r['advance'] not in changed_set]
    small_steps = [r for r in history if r.get('blocker') is not None]
    release_records = [{key: item.get(key) for key in (
        'kind', 'advances', 'row', 'normalized_descent_gain', 'gain_threshold',
        'face_gradient_norm_before', 'actual_unit_slope', 'actual_unit_inward',
        'new_projected_direction_slope', 'released_row_new_direction_derivative')}
        for item in transitions if item.get('kind', '').startswith('release_negative_multiplier')]
    gradient = qp.get('final_face_projected_gradient_norm')
    return dict(qp_status=qp.get('status'), advances=advances, maxiter=qp.get('maxiter'),
        history_length=len(history), history_complete=len(history) == advances,
        initial_gradient_norm=qp.get('initial_gradient_norm'),
        final_face_projected_gradient_norm=gradient,
        gradient_tolerance=qp.get('gradient_tolerance'),
        projected_gradient_over_tolerance=quotient(gradient, qp.get('gradient_tolerance')),
        projected_gradient_over_initial_gradient=quotient(gradient, qp.get('initial_gradient_norm')),
        transition_kind_counts=dict(transition_counts),
        successful_face_additions=sum(item.get('added') is True for item in transitions),
        release_count=len(release_records), release_records=release_records,
        zero_length_transition_count=transition_counts.get('zero_length_blocker', 0),
        clipped_positive_advance_count=len(small_steps),
        full_unblocked_advance_count=advances-len(small_steps),
        final_active_rows=qp.get('active_face', {}).get('active_rows'),
        maximum_active_rows=qp.get('maximum_active_face_rank'),
        fixed_face_segments=segments,
        longest_fixed_face_advances=max((s['advances'] for s in segments), default=0),
        longest_fixed_face_unblocked_advances=max((s['unblocked_advances'] for s in segments), default=0),
        known_refresh_interval=known_interval,
        refresh_accounting_source='frozen v2 source and actual advance count/history' if exact_v2 else 'reported successor metadata or unknown',
        refreshes=refreshes, refresh_count=len(refreshes),
        v2_effective_forced_same_face_restart_advances=forced_same_face,
        v2_effective_forced_same_face_restart_count=len(forced_same_face),
        actual_operator_products=actual_products, expected_v2_operator_products=expected_v2,
        v2_product_accounting_matches=(actual_products == expected_v2) if exact_v2 else None,
        maximum_linear_violation=qp.get('maximum_linear_violation'),
        minimum_raw_multiplier=qp.get('minimum_multiplier'),
        maximum_complementarity_residual=qp.get('maximum_complementarity_residual'),
        final_normalized_release_diagnostics=qp.get('final_normalized_release_diagnostics'),
        raw_negative_multiplier_alone_does_not_identify_a_release_bottleneck=True,
        fixed_face_scope='Temporary affine face of the same complete finite QP; it is not a frozen physical-field subspace')


def trial_analysis(direction, scalar):
    trials, counts = [], Counter()
    old = direction.get('old_merit')
    slope = direction.get('half_objective_slope')
    energy = scalar.get('data_Hessian_ray_energy')
    for trial in direction.get('trials', []):
        alpha, merit = trial.get('alpha'), trial.get('merit')
        evaluated = isinstance(trial.get('curvature_filter'), dict)
        point_filter = trial.get('curvature_filter') or {}
        if trial.get('finite') is not True:
            category = 'nonfinite_metric_or_arithmetic'
        elif trial.get('feasible') is not True:
            category = 'sampled_field_domain'
        elif trial.get('descent') is not True:
            category = 'true_Phi_descent_or_Armijo'
        elif evaluated and point_filter.get('passed') is not True:
            category = 'true_known_point_geometry'
        elif direction.get('accepted') and alpha == direction.get('accepted_alpha'):
            category = 'accepted'
        else:
            category = 'no_recorded_acceptance_reason'
        counts[category] += 1
        predicted = (old+2*alpha*slope+alpha*alpha*energy
            if all(number(x) for x in (old, alpha, slope, energy)) else None)
        model_drop = old-predicted if number(old) and number(predicted) else None
        actual_drop = old-merit if number(old) and number(merit) else None
        geometry = trial.get('curvature_points') or {}
        stats = trial.get('statistics') or {}
        trials.append(dict(index=trial.get('index'), alpha=alpha, Phi=merit,
            finite=trial.get('finite'), feasible=trial.get('feasible'), descent=trial.get('descent'),
            curvature_feasible_raw=trial.get('curvature_feasible'),
            curvature_evaluated=evaluated,
            curvature_failed=(point_filter.get('passed') is not True) if evaluated else None,
            true_known_point_product=point_filter.get('necessary_reach_product'),
            maximum_sampled_curvature=point_filter.get('sampled_curvature'),
            actual_radius_diameter_lower=point_filter.get('reference_diameter_lower_bound'),
            worst_geometry_location=geometry.get('worst'),
            max_gram=stats.get('max_relative_gram'),
            original_weighted_sse=stats.get('radial_weighted_frobenius_sse'),
            rejection_or_acceptance=category, same_alpha_model_Phi=predicted,
            actual_Phi_drop=actual_drop, same_alpha_predicted_Phi_drop=model_drop,
            actual_to_same_alpha_predicted_drop=quotient(actual_drop, model_drop),
            additional_permanent_curvature_points=len(trial.get('new_permanent_curvature_locations', [])),
            additional_permanent_radius_points=len(trial.get('new_permanent_radius_locations', []))))
    return dict(trials=trials, trial_status_counts=dict(counts), trial_count=len(trials),
        all_recorded_trials_retained=True,
        geometry_not_evaluated_is_not_geometry_pass=True,
        curvature_scope='True evaluations at all declared grid/permanent points; neither continuous K nor reach')


def analyze(path, scalar_module):
    value = json.loads(path.read_text())
    parent = value.get('initial', {})
    directions, table = [], []
    for direction in value.get('directions', []):
        scalars = scalar_module.analyze_direction(direction, parent, value)
        linear, nonlinear = linear_history(direction.get('qp', {}), value), trial_analysis(direction, scalars)
        entry = dict(index=direction.get('index'), damping=direction.get('damping'),
            accepted=direction.get('accepted'), accepted_alpha=direction.get('accepted_alpha'),
            old_merit=direction.get('old_merit'),
            full_step_predicted_merit=direction.get('quadratic_predicted_actual_objective'),
            new_merit=direction.get('new_merit'),
            accepted_bundle_sha256=direction.get('accepted_bundle_sha256'),
            linear=linear, nonlinear=nonlinear, Hessian_and_ray_scalars=scalars)
        directions.append(entry)
        table.append([entry['index'], entry['damping'], linear['advances'], linear['qp_status'],
            linear['final_face_projected_gradient_norm'], linear['refresh_count'],
            linear['v2_effective_forced_same_face_restart_count'], linear['successful_face_additions'],
            linear['release_count'], linear['longest_fixed_face_advances'],
            entry['old_merit'], entry['full_step_predicted_merit'], entry['new_merit'],
            entry['accepted_alpha'], scalars.get('damping_to_data_ray_energy_ratio'),
            nonlinear['trial_status_counts']])
        if direction.get('accepted'):
            for trial in direction.get('trials', []):
                if trial.get('alpha') == direction.get('accepted_alpha'):
                    parent = trial.get('statistics', parent)
                    break
    return dict(report=str(path), report_sha256=sha(path),
        input_bundle_sha256=value.get('bundle_sha256'), final_bundle_sha256=value.get('final_bundle_sha256'),
        original_driver_sha256=value.get('source_sha256'),
        original_QP_sha256=value.get('source_sha256_by_role', {}).get('qp'),
        numerical_safety=value.get('numerical_reach_safety_factor'),
        report_complete=value.get('complete'), actual_direction_count=len(directions),
        observed_QP_status_counts=dict(Counter(item['linear']['qp_status'] for item in directions)),
        direction_table_columns=['index', 'mu', 'advances', 'QP_status', 'final_Pg_norm',
            'refresh_count', 'effective_CG32_restart_count', 'face_additions', 'face_releases',
            'longest_fixed_face_advances', 'old_Phi', 'full_step_model_Phi', 'new_Phi',
            'accepted_alpha', 'mu_energy_over_data_energy', 'trial_status_counts'],
        direction_table=table, directions=directions,
        decision_scope='Distinguish repeated fixed-face truncation, changing faces, damping energy, and actual nonlinear rejection; no automatic causal winner or new solver budget')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, action='append', required=True)
    parser.add_argument('--scalar-source', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('Read these returned scientific reports in this public repository Actions.')
    source = (args.scalar_source or Path(__file__).with_name('full_phi_qp_scalar_diagnostics.py')).resolve()
    if sha(source) != SCALAR_SHA:
        raise ValueError('Use the published corrected R673 scalar source')
    if args.out.exists():
        raise FileExistsError(args.out)
    spec = importlib.util.spec_from_file_location('r673_returned_scalar_diagnostics', source)
    scalar_module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = scalar_module
    spec.loader.exec_module(scalar_module)
    result = scalar_module.sanitize(dict(schema='returned-full-Phi-QP-bottleneck-report-v1',
        source_sha256=sha(__file__), scalar_source=str(source), scalar_source_sha256=sha(source),
        github_run_id=os.environ.get('GITHUB_RUN_ID'), github_sha=os.environ.get('GITHUB_SHA'),
        reports=[analyze(path.resolve(), scalar_module) for path in args.report],
        field_evaluations=0, J_or_Jtranspose_calls=0, new_fixtures=0,
        input='Already returned report JSON; no raw direction or field arrays are loaded',
        numerical_scalar_diagnostics_only=True, outward_certification=False,
        continuous_reach_claimed=False))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, separators=(',', ':'), allow_nan=False)+'\n')
    print(json.dumps(dict(schema=result['schema'], report=str(args.out.resolve()),
        report_sha256=sha(args.out), reports=len(result['reports']),
        directions=sum(item['actual_direction_count'] for item in result['reports']),
        field_evaluations=0, J_or_Jtranspose_calls=0)), flush=True)


if __name__ == '__main__':
    main()

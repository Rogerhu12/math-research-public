#!/usr/bin/env python3
"""Summarize the completed pooled-feasibility curvature run without reevaluation.

Only reads the exact published JSON bytes. No geometry, quadrature, Jacobian,
SciPy or optimizer is imported or called. Original scientific files are untouched.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import tempfile

REPOSITORY = 'Rogerhu12/math-research-public'
ORIGINAL_RUN = '43648433010'
ORIGINAL_SOURCE = 'df535c0c42d76040903b1e89c6d08d13ea360ad2'
FULL_BYTES = 2739477
FULL_SHA256 = '87945a59c206618ca2da5fe0b31f8a5961c1bef085704aa5bf27494c7daecf32'
SOURCES = {
    'frame_curvature_epigraph_exchange.py': '8c26353df012ca61f37149b2e2ab52acaec4ca22fde68017261c0bd68992ebf5',
    'frame_curvature_epigraph_exchange_audit.py': '7162b7c56bb865591316b1ca576c7b0929d55619353567ccd4f3df789543802a',
    'frame_curvature_feasible_exchange.py': 'ed77abc30e6d4b5fa53e558c316e7479f91cbf674c2686e8ff69908b57e101e5',
    'frame_curvature_feasible_exchange_audit.py': '60a3bd66a1e0636c0796a102b900aa04099f5341008a9262e0f31b1090088b14',
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def trial_row(record, groups):
    d = record['decision']
    c = record['whole_grid_and_pool_separation_at_this_same_trial']['group_counts']
    omitted = [int(c[g]['omitted']) for g in groups]
    enforced = [int(c[g]['whole_grid']) - n for g, n in zip(groups, omitted)]
    cap = d['cap_and_box']
    return {
        'evaluation': record['epigraph_evaluation'],
        'physical_evaluation': record['physical_geometry_evaluation'],
        'optimization_seconds': record['optimization_elapsed_seconds'],
        'kappa': d['direct_maximum_absolute_principal_curvature'],
        'lambda': d['curvature_auxiliary_lambda'],
        'eta': d['direct_max_eta'],
        'fixed_metric_excess': d['direct_eta_minus_fixed_budget'],
        'metric_and_physical_ok': d['eligible_under_fixed_metric_and_physical_gates'],
        'physical_excluding_metric_ok': d['physical_gate_pass_excluding_fixed_metric'],
        'auxiliary_and_all_ok': d['eligible_under_all_declared_sampled_constraints'],
        'cap_margin': min(cap['affine_height_margin'], cap['reconstructed_height_margin']),
        'box_violation': cap['box_violation'],
        'signed_z_min': d['minimum_signed_height'],
        'ball_squared_normalized_max': d['ball_radius_squared_normalized_max'],
        'absolute_y_max': d['maximum_absolute_y'],
        'inner_strip_margin': d['inner_strip_absolute_margin'],
        'mirror_radius_min': d['direct_mirror_radius_min_finite'],
        'normal_area_over_a_min': d['first_order_normal_area_over_a_min_sample'],
        'metric_row_min': d['divided_metric_row_min'],
        'curvature_PSD_min': min(d['curvature_scaled_row_minima'].values()),
        'enforced_pool_violations_by_group': enforced,
        'omitted_violations_by_group': omitted,
    }


def callback_row(rd, c, groups):
    p = c['enforced_pool']
    return {
        'round': rd['round'],
        'major_in_round': c['major_in_round'],
        'epigraph_evaluation': c['epigraph_evaluation'],
        'pool_ready': p['ready_for_exchange'],
        'cap_and_box_pass': p['cap_and_box_pass'],
        'regularity_pass': p['independent_regularity_pass'],
        'enforced_violations_by_group': [p['groups'][g]['violating_count'] for g in groups],
        'enforced_minimum_rows_by_group': [p['groups'][g]['minimum_row'] for g in groups],
        'omitted_violations': c['omitted_violating_count'],
        'same_call_continues': c['same_SLSQP_continues_to_restore_pool'],
        'exchange_requested': c['exchange_requested'],
    }


def table(rows):
    columns = list(rows[0]) if rows else []
    return {'columns': columns, 'rows': [[r[k] for k in columns] for r in rows]}


def summarize(full, raw, path):
    if (full.get('schema') != 'same-g-pooled-feasibility-curvature-exchange-audit-v1'
            or full.get('status') != 'complete-pooled-feasibility-actual-curvature-exchange-audit'
            or str(full.get('github_run_id')) != ORIGINAL_RUN
            or full.get('github_sha') != ORIGINAL_SOURCE
            or full.get('artificial_inputs_only') is not False):
        raise ValueError('exact completed requested actual source/run required')
    for name, expected in SOURCES.items():
        if full.get('source_files_sha256', {}).get(name) != expected:
            raise ValueError('source differs: ' + name)
    stage = full['curvature_exchange_stage']
    checkpoint = stage['checkpoint']
    pool_history = checkpoint['active_row_pool_history']
    groups = pool_history[0]['group_order']
    if len(groups) != 11 or any(p['group_order'] != groups for p in pool_history):
        raise ValueError('eleven-group order mismatch')
    records = checkpoint['history']
    rows = [trial_row(r, groups) for r in records]
    if not rows:
        raise ValueError('no saved actual trial history')
    callbacks = [callback_row(rd, c, groups)
                 for rd in stage['solver']['rounds']
                 for c in rd.get('callback_observations', [])]
    by_evaluation = {r['evaluation']: r for r in rows}
    if len(by_evaluation) != len(rows):
        raise ValueError('duplicate epigraph evaluation identity')
    record_by_evaluation = {r['epigraph_evaluation']: r for r in records}

    def select(name, predicate, key):
        candidates = [r for r in rows if predicate(r)]
        if not candidates:
            return name, None
        row = min(candidates, key=key)
        original = record_by_evaluation[row['evaluation']]
        decision = original['decision']
        result = dict(row)
        result.update(kappa_location=decision['direct_max_curvature_location'],
                      eta_location=decision['direct_max_eta_location'],
                      regular=decision['regularity_screen_pass'],
                      pool_rows=original['pool_rows'],
                      pool_version=original['pool_version'])
        return name, result

    noninitial = lambda r: r['physical_evaluation'] != rows[0]['physical_evaluation']
    kappa_key = lambda r: (r['kappa'], r['eta'], r['evaluation'])
    selected = dict([
        select('minimum_kappa_any', lambda r: True, kappa_key),
        select('minimum_kappa_other_physical_gates', lambda r: r['physical_excluding_metric_ok'], kappa_key),
        select('minimum_kappa_all_physical_gates', lambda r: r['metric_and_physical_ok'], kappa_key),
        select('smallest_eta_noninitial_other_physical_gates',
               lambda r: noninitial(r) and r['physical_excluding_metric_ok'],
               lambda r: (r['eta'], r['kappa'], r['evaluation'])),
        select('fewest_enforced_violations_noninitial',
               noninitial,
               lambda r: (sum(r['enforced_pool_violations_by_group']), r['eta'], r['kappa'])),
        select('last_saved_trial', lambda r: True, lambda r: -r['evaluation']),
    ])
    counters = {k: checkpoint.get(k) for k in [
        'physical_geometry_evaluations', 'epigraph_vector_evaluations',
        'jacobian_geometry_batches', 'jacobian_refreshes',
        'initialization_elapsed_seconds', 'optimization_elapsed_seconds',
        'deferred_exchange_callbacks', 'pooled_feasible_exchange_callbacks',
        'maximum_batch_query_radial_rows', 'maximum_same_state_batch_ordinary_jet_difference',
    ]}
    thresholds = None
    if callbacks:
        first = stage['solver']['rounds'][0]['callback_observations'][0]['enforced_pool']['groups']
        thresholds = [first[g]['actual_tolerance'] for g in groups]
    saved = {}
    reference = checkpoint.get('best_physical_curvature_point')
    reference_coefficients = None if reference is None else reference['physical_parameter_coefficients_binary64']
    for name in ['best_physical_curvature_point', 'best_auxiliary_feasible_lambda_point',
                 'best_auxiliary_feasible_curvature_point', 'lowest_lambda_trial_may_be_ineligible']:
        point = checkpoint.get(name)
        if point is None:
            saved[name] = None
            continue
        coeff = point['physical_parameter_coefficients_binary64']
        delta = None if reference_coefficients is None else [
            float(x) - float(y) for x, y in zip(coeff, reference_coefficients)]
        if reference_coefficients is not None and len(coeff) != len(reference_coefficients):
            raise ValueError('saved point coefficient dimension mismatch')
        saved[name] = {
            'physical_state_sha256': point['physical_state_sha256'],
            'epigraph_evaluation': point['record']['epigraph_evaluation'],
            'physical_evaluation': point['record']['physical_geometry_evaluation'],
            'auxiliary_lambda_evaluated': point['auxiliary_lambda_evaluated'],
            'maximum_absolute_coefficient_difference_from_preserved_physical_best':
                None if delta is None else max(abs(x) for x in delta),
            'coefficient_l2_difference_from_preserved_physical_best':
                None if delta is None else sum(x*x for x in delta)**0.5,
            'coefficient_difference_is_output_arithmetic_not_geometry_reevaluation': True,
        }
    summaries = []
    for rd in stage['solver']['rounds']:
        summaries.append({k: rd.get(k) for k in [
            'round', 'pool_version', 'pool_rows', 'major_iterations', 'exit_reason',
            'library_result', 'pooled_feasibility_at_library_return',
        ]})
    return {
        'schema': 'pooled-feasibility-preserved-curvature-trial-diagnostics-v1',
        'source_full_report': {
            'path': str(path), 'raw_bytes': len(raw), 'raw_sha256': digest(raw),
            'original_run': ORIGINAL_RUN, 'original_source_commit': ORIGINAL_SOURCE,
        },
        'extractor_source_sha256': digest(Path(__file__).read_bytes()),
        'extraction_run_id': os.environ.get('GITHUB_RUN_ID'),
        'extraction_source_commit': os.environ.get('GITHUB_SHA'),
        'research_geometry_evaluated': False, 'optimizer_called': False,
        'original_scientific_output_modified': False,
        'group_order': groups, 'original_actual_group_tolerances': thresholds,
        'initial_physical_sha256': full['initial_state']['canonical_physical_state_sha256'],
        'final_physical_sha256': full['final_state']['canonical_physical_state_sha256'],
        'stage_status': stage['status'], 'budget_message': stage.get('budget_message'),
        'stage_error': stage.get('error'),
        'solver': {k: v for k, v in stage['solver'].items() if k != 'rounds'},
        'rounds': summaries, 'counters': counters,
        'complete_saved_history': len(rows) == checkpoint['epigraph_vector_evaluations'],
        'eligible_distinct_physical_evaluations': sorted({
            r['physical_evaluation'] for r in rows if r['metric_and_physical_ok']}),
        'other_physical_gates_passing_evaluations': sum(
            bool(r['physical_excluding_metric_ok']) for r in rows),
        'selected_diagnostics': selected, 'saved_full_coefficient_points': saved,
        'trial_history': table(rows), 'callback_pool_history': table(callbacks),
        'whole_group_counts_equal_enforced_plus_omitted': True,
        'no_new_convergence_or_continuous_certificate_claim': True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY):
        raise SystemExit('only the authorized public Actions may extract this report')
    opener = gzip.open if args.report.suffix == '.gz' else open
    with opener(args.report, 'rb') as handle:
        raw = handle.read(FULL_BYTES + 1)
    if len(raw) != FULL_BYTES or digest(raw) != FULL_SHA256:
        raise ValueError('exact original full report bytes differ')
    result = summarize(json.loads(raw), raw, args.report)
    encoded = (json.dumps(result, ensure_ascii=False, separators=(',', ':'),
                          allow_nan=False) + '\n').encode('utf-8')
    if len(encoded) > 95000:
        raise ValueError('semantic diagnosis exceeds its declared 95 KB bound')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.curvature-feasible-diag-', dir=str(args.out.parent))
    try:
        with os.fdopen(fd, 'wb') as handle:
            handle.write(encoded)
        os.replace(name, args.out)
    finally:
        if os.path.exists(name):
            os.unlink(name)
    print(json.dumps({'status': 'complete-existing-report-only-diagnosis',
        'out': str(args.out), 'bytes': len(encoded), 'sha256': digest(encoded),
        'geometry_recomputed': False}), flush=True)


if __name__ == '__main__':
    main()

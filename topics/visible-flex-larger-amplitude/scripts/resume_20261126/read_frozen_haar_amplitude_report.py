#!/usr/bin/env python3
"""Read only a real complete fixed accurate-Haar/amplitude solve.

All original f119 direction, true acceptance, row-count and amplitude
checks remain. The distinct actual target/source identities, working
moment carrier and initial/final/every finite trial target are checked.
No arrays, F/J, fixture or scientific solve runs in this reader.
"""
HAAR_SOURCE_DERIVATION = {'schema': 'R691-independent-complete-Haar-actual-report-reader-v1', 'complete_fixed_target_reader_parent_sha256': 'f119d9960a0e6de381b6a7ab93581a1dd785db258a6b7cd2a72546ea62c979af', 'complete_driver_sha256': 'b70bdcd7c9b0e0a8cf101d9a59b229d048359318f8b5289e3513fc96ce79d61f', 'complete_coarse_sha256': 'ee172fd58ec6ad589bb9cc8f7e9980eded83cc9d051bec7329d07bf474bbc80f', 'accurate_target_source_sha256': 'c5a717dbca55311060207672c703293403c16c6e5142b84cc522e660afc67a64', 'accurate_moment_source_sha256': '1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010', 'original_actual_direction_and_amplitude_checks_retained': True, 'scientific_evaluation': False}
R671_FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
HAAR_TARGET_SHA = 'c5a717dbca55311060207672c703293403c16c6e5142b84cc522e660afc67a64'
HAAR_MOMENTS_SHA = '1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010'
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
SCHEMA = 'complete-fixed-true-material-Haar-with-held-amplitude-budgets-v1'
EXPECTED = {'driver': ('fullclosed_frozen_haar_amplitude_qp.py', 'b70bdcd7c9b0e0a8cf101d9a59b229d048359318f8b5289e3513fc96ce79d61f'), 'amplitude_rows': ('held_amplitude_inequalities_v2.py', 'd494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'), 'amplitude_screen': ('held_amplitude_screen_v2.py', 'e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f'), 'frozen_coarse': ('frozen_material_haar_coarse_moments.py', 'ee172fd58ec6ad589bb9cc8f7e9980eded83cc9d051bec7329d07bf474bbc80f'), 'frozen_target': ('frozen_material_haar_metric.py', 'c5a717dbca55311060207672c703293403c16c6e5142b84cc522e660afc67a64'), 'qp': ('fullspace_feasible_active_pcg_v5.py', '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8')}
CENTERED_SHA = '5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01'

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

def finite(value, label):
    if isinstance(value, bool) or not isinstance(value, (float, int)) or (not math.isfinite(value)):
        raise ValueError('A finite actual scalar is required: ' + label)
    return float(value)

def metric(value):
    s = value['spectral']
    return dict(max_relative_gram=finite(value['max_relative_gram'], 'metric max'), old_fixed_metric_max_diagnostic=value.get('old_fixed_metric_max_diagnostic'), phi=finite(s['phi_normalized'], 'Phi'), centered_phi=s.get('centered_phi_normalized'), p=s['p'], epsilon=s['epsilon'], scale=s['scale'], normalization=s['normalization'])

def amplitude(value):
    if not value.get('complete'):
        return dict(complete=False, passed=False, actual_read_error=value.get('reason'))
    return dict(complete=True, passed=bool(value['passed']), maximum_inequality_value=value['maximum_inequality_value'], maximum_by_kind={key: item['value'] for key, item in value['maximum_inequality_by_kind'].items()}, scalar_inequalities=value['scalar_inequalities'], current_witness_radius=value['current_witness_radius'], height=value['height'], grid_points=value['grid_quarter_points_read'], permanent_points=value['distinct_arbitrary_points_read'], required_permanent_points=value['required_distinct_arbitrary_points'], exact_permanent_set_complete=value['exact_arbitrary_location_set_equals_required_set'], sampled_minimum_witness_distance_squared=value['minimum_witness_distance_squared'], sampled_minimum_is_not_a_global_distance_lower_bound=True, proposed_appended_rows=value['proposed_appended_rows_including_cap_and_height'], continuous_amplitude_certified=False)

def validate_accurate_Haar_report(r):
    value = r['haar_target_contract']
    target = r['frozen_metric_target']
    if value.get('schema') != 'R691-complete-fixed-Haar-full-solver-contract-v1' or value.get('exact_full_circle_material_integral') is not True or value.get('working_quadrature_is_target_definition') is not False or (value.get('old_target_Phi_improvement_claimed') is not False) or (value.get('all_original_variables_mean_rows_and_H2_norm_retained') is not True) or (value.get('all_original_geometry_and_both_amplitude_branches_retained') is not True) or (value.get('original_physical_R671_model_preserved') is not True) or (value.get('current_scalar_constraints_and_geometry_preserved') is not True) or (target.get('averaging') != 'exact-material-Haar') or (target.get('exact_material_Haar') is not True) or (target.get('frozen_full_angles') is not None) or (target.get('finite_quadrature_nodes_define_target') is not False) or (target.get('all_original_mean_constraints_retained') is not True) or (target.get('moving_mean_projection') is not False) or (target.get('target_mean_recomputed_from_current_field') is not False) or (target.get('target_identity_sha256') != value['target_identity_sha256']) or (target.get('angular_identity_sha256') != value['angular_identity_sha256']) or (target.get('working_moment_carrier') != value['working_moment_carrier']) or (target.get('working_moment_full_angles') != value['working_moment_full_angles']):
        raise ValueError('The actual solve must retain one complete exact Haar target and all original rows')
    if value['target_sources']['evaluator']['sha256'] != HAAR_TARGET_SHA or value['target_sources']['moments']['sha256'] != HAAR_MOMENTS_SHA or value['target_sources']['factory']['sha256'] != R671_FACTORY_SHA or (r['source_sha256_by_role']['exact_tail'] != R671_FACTORY_SHA) or (r['exact_tail_lambda'] != 1):
        raise ValueError('Do not relabel a finite-target or another physical-model report as accurate Haar')
    stats = [r['initial'], r['final_statistics']]
    if r.get('current') is not None:
        stats.append(r['current'])
    for direction in r['directions']:
        for trial in direction['trials']:
            if trial.get('finite'):
                if not isinstance(trial.get('statistics'), dict):
                    raise ValueError('Every finite trial needs its actual full target read')
                stats.append(trial['statistics'])
    if any((item.get('frozen_target_identity') != value['target_identity_sha256'] or item.get('mean_averaging') != 'exact-material-Haar' or item.get('final_metric_frozen') is not True for item in stats)):
        raise ValueError('Initial, final and all finite actual trials must read the same exact target')
    return value

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise SystemExit('Actual scientific report attribution belongs in this public repository Actions')
    source = a.repo.resolve() / 'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    r = json.loads(a.report.read_text())
    if r.get('schema') != SCHEMA or r.get('complete') is not True:
        raise ValueError('Need a naturally completed actual complete amplitude-design report')
    accurate = validate_accurate_Haar_report(r)
    binding = {}
    for role, (name, digest) in EXPECTED.items():
        path = source / name
        if sha(path) != digest:
            raise ValueError('Changed complete published source: ' + role)
        recorded = r.get('source_sha256') if role == 'driver' else r['source_sha256_by_role'].get(role)
        if recorded != digest:
            raise ValueError('The actual report is not bound to this complete source: ' + role)
        binding[role] = dict(path=str(path), sha256=digest)
    objective = r['selected_scalar_objective_key']
    if objective == 'centered_phi_normalized':
        if r['source_sha256_by_role'].get('centered_loss') != CENTERED_SHA or sha(source / 'centered_spectral_statistics.py') != CENTERED_SHA:
            raise ValueError('The actual centered scalar definition changed')
    elif objective != 'phi_normalized':
        raise ValueError('Unknown actual spectral scalar objective')
    direction_records = []
    for index, d in enumerate(r['directions']):
        if d['index'] != index or not isinstance(d['accepted'], bool):
            raise ValueError('Use the complete actual ordered direction history')
        trial_acceptance = []
        for t in d['trials']:
            potential = bool(t['feasible'] and t['descent'])
            full_pass = bool(potential and t['curvature_feasible'] and t['amplitude_feasible'])
            if full_pass:
                amp = t['amplitude_filter']
                if not (amp['complete'] and amp['passed'] and amp['complete_grid_coverage'] and amp['exact_arbitrary_location_set_equals_required_set']):
                    raise ValueError('An accepted candidate lacks its actual complete true amplitude read')
            trial_acceptance.append(full_pass)
        if sum(trial_acceptance) != int(d['accepted']):
            raise ValueError('The actual true line-search acceptance disagrees with the saved direction')
        rows = d['active_geometry']
        extra = rows['amplitude']
        if extra['original_prefix_rows'] != d['original_geometry_rows_retained'] or rows['selected_rows'] != extra['original_prefix_rows'] + extra['appended_rows'] or extra['appended_rows'] != d['appended_amplitude_rows']:
            raise ValueError('The complete old/new row counts disagree')
        direction_records.append(dict(index=index, accepted=d['accepted'], accepted_alpha=d.get('accepted_alpha'), qp_schema=d['qp'].get('schema'), qp_status=d['qp']['status'], qp_advances=d['qp']['advances'], actual_old_geometry_rows=extra['original_prefix_rows'], actual_amplitude_rows=extra['appended_rows'], total_working_rows=rows['selected_rows'], combined_row_cache_bytes=rows['row_cache_bytes'], original_geometry_row_cache_bytes=d['original_geometry_row_cache_bytes'], total_scratch_row_cache_bytes=d['total_scratch_row_cache_bytes'], maximum_linear_reach_product=d['maximum_selected_linear_product'], maximum_linear_amplitude_g=d['maximum_selected_linear_amplitude_value'], true_trials=len(d['trials']), true_amplitude_failed_trials=sum((t['amplitude_filter'] is not None and (not t['amplitude_feasible']) for t in d['trials'])), current_fixed_target_coarse={key: d['fixed_target_preconditioner'].get(key) for key in ('status', 'construction_seconds', 'actual_operator_entry_calls', 'actual_QP_schema', 'fallback_to_frozen_v3')}))
    initial = metric(r['initial'])
    final = metric(r['final_statistics'])
    for key in ('p', 'epsilon', 'scale', 'normalization'):
        if initial[key] != final[key]:
            raise ValueError('Cannot compare different spectral definitions/measures')
    summary = dict(schema='complete-fixed-true-material-Haar-held-amplitude-actual-summary-v1', reader_source_sha256=sha(__file__), report_sha256=sha(a.report), actual_solver_source_commit=r['source_commit'], actual_github_run_id=r.get('github_run_id'), reader_source_commit=subprocess.check_output(['git', '-C', str(a.repo), 'rev-parse', 'HEAD'], text=True).strip(), complete_source_binding=binding, actual_parent_bundle_sha256=r['bundle_sha256'], actual_final_bundle_sha256=r['final_bundle_sha256'], mean_averaging=r['frozen_metric_target']['averaging'], frozen_target_identity_sha256=r['frozen_metric_target']['target_identity_sha256'], frozen_target_manifest_sha256=r['frozen_metric_target']['manifest_sha256'], target_full_angles=None, accurate_material_Haar=True, angular_identity_sha256=accurate['angular_identity_sha256'], working_moment_carrier=accurate['working_moment_carrier'], working_moment_full_angles=accurate['working_moment_full_angles'], working_quadrature_is_target_definition=False, old_target_Phi_improvement_claimed=False, source_derivation=HAAR_SOURCE_DERIVATION, common_parent_measure=r['final_statistics'].get('common_parent_measure'), actual_M=r['M'], actual_N=r['N'], actual_J=r['J'], original_free_variables=r['original_variables'], all_full_rows=r['all_full_rows'], selected_scalar_objective_key=objective, initial_metric=initial, final_metric=final, actual_same_measure_Phi_change=final['phi'] - initial['phi'], actual_same_measure_centered_Phi_change=final['centered_phi'] - initial['centered_phi'] if final['centered_phi'] is not None and initial['centered_phi'] is not None else None, amplitude_budgets=r['amplitude_design_constraints']['budgets'], initial_amplitude=amplitude(r['initial_amplitude_filter']), final_amplitude=amplitude(r['final_amplitude_filter']), final_necessary_curvature_filter=r['final_curvature_filter'], directions=direction_records, actual_direction_count=r['actual_direction_count'], actual_accepted_direction_count=r['actual_accepted_direction_count'], actual_final_damping=r['final_damping'], final_permanent_counts=r['final_permanent_position_counts'], process_peak_rss_KiB=r['process_peak_rss_KiB'], actual_stop_before_linear=r.get('stopped_before_linear_iteration'), final_metric_frozen=True, all_fixed_target_mean_constraints_retained=True, common_parent_measure_present='common_parent_measure' in r['final_statistics'], declared_numerical_target=r['target'], zero_direction_exit=r['zero_direction_exit'], fixed_g_refinement_convergence_certified=False, continuous_amplitude_certified=False, reach_certified=False, topic_completion_claimed=False)
    if a.out.exists():
        raise FileExistsError(a.out)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(summary, indent=2, allow_nan=False) + '\n')
    print(json.dumps(dict(summary=str(a.out.resolve()), summary_sha256=sha(a.out), final_bundle_sha256=r['final_bundle_sha256'], final_metric=final['max_relative_gram'], frozen_target_identity_sha256=r['frozen_metric_target']['target_identity_sha256'], final_amplitude_passed=summary['final_amplitude']['passed'], actual_accepted_directions=summary['actual_accepted_direction_count'], continuous_amplitude_certified=False, reach_certified=False)), flush=True)
if __name__ == '__main__':
    main()

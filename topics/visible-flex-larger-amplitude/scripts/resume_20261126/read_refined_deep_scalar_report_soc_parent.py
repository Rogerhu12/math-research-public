#!/usr/bin/env python3
"""Read only an actual byte-bound complete fixed-deep-scalar/amplitude report.

No raw arrays, scientific operators, derivatives, or numerical fixtures are
loaded. Complete source identities and every actual direction/acceptance
record are checked before extracting a compact, honestly scoped summary.
This schema is distinct from R684/R688 and cannot use their old report binder.
"""
import argparse
import hashlib
import importlib.util
import sys
import json
import math
import os
from pathlib import Path
import subprocess
SCHEMA = 'complete-refined-fixed-deep-scalar-with-held-amplitude-budgets-soc-parent-v1'
EXPECTED = {'refinement_parent_binding': ('fixed_deep_refinement_parent_binding.py', 'b3e391847c6e1367ca43b3bc83f4f570aafd48e87eafe93f4d049d85b288cdbf'), 'driver': ('fullclosed_refined_deep_scalar_amplitude_qp_soc_parent.py', 'a616e88c1f1bd256d298f167f05f0030488a7842ca4af42d53ba3f41d70dff85'), 'amplitude_rows': ('held_amplitude_inequalities_v2.py', 'd494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'), 'amplitude_screen': ('held_amplitude_screen_v2.py', 'e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f'), 'scalar_coarse': ('deep_scalar_coarse_moments.py', 'dcfa30b688104b27efeddfbe6921af25ba33ba6202be43f815d5b8d8bfc69395'), 'exact_tail': ('deep_valley_reference_factory.py', '4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'), 'deep_scalar': ('deep_valley_tail_input.py', 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'), 'qp': ('fullspace_feasible_active_pcg_v5.py', '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8')}
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
    return dict(max_relative_gram=finite(value['max_relative_gram'], 'metric max'), phi=finite(s['phi_normalized'], 'Phi'), centered_phi=s.get('centered_phi_normalized'), p=s['p'], epsilon=s['epsilon'], scale=s['scale'], normalization=s['normalization'])

def amplitude(value):
    if not value.get('complete'):
        return dict(complete=False, passed=False, actual_read_error=value.get('reason'))
    return dict(complete=True, passed=bool(value['passed']), maximum_inequality_value=value['maximum_inequality_value'], maximum_by_kind={key: item['value'] for key, item in value['maximum_inequality_by_kind'].items()}, scalar_inequalities=value['scalar_inequalities'], current_witness_radius=value['current_witness_radius'], height=value['height'], grid_points=value['grid_quarter_points_read'], permanent_points=value['distinct_arbitrary_points_read'], required_permanent_points=value['required_distinct_arbitrary_points'], exact_permanent_set_complete=value['exact_arbitrary_location_set_equals_required_set'], sampled_minimum_witness_distance_squared=value['minimum_witness_distance_squared'], sampled_minimum_is_not_a_global_distance_lower_bound=True, proposed_appended_rows=value['proposed_appended_rows_including_cap_and_height'], continuous_amplitude_certified=False)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--comparison-parent-report', type=Path)
    a = p.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise SystemExit('Actual scientific report attribution belongs in this public repository Actions')
    source = a.repo.resolve() / 'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    r = json.loads(a.report.read_text())
    if r.get('schema') != SCHEMA or r.get('complete') is not True:
        raise ValueError('Need a naturally completed actual complete amplitude-design report')
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
        direction_records.append(dict(index=index, accepted=d['accepted'], accepted_alpha=d.get('accepted_alpha'), qp_schema=d['qp'].get('schema'), qp_status=d['qp']['status'], qp_advances=d['qp']['advances'], actual_old_geometry_rows=extra['original_prefix_rows'], actual_amplitude_rows=extra['appended_rows'], total_working_rows=rows['selected_rows'], combined_row_cache_bytes=rows['row_cache_bytes'], original_geometry_row_cache_bytes=d['original_geometry_row_cache_bytes'], total_scratch_row_cache_bytes=d['total_scratch_row_cache_bytes'], maximum_linear_reach_product=d['maximum_selected_linear_product'], maximum_linear_amplitude_g=d['maximum_selected_linear_amplitude_value'], true_trials=len(d['trials']), true_amplitude_failed_trials=sum((t['amplitude_filter'] is not None and (not t['amplitude_feasible']) for t in d['trials'])), current_fixed_scalar_coarse={key: d['scalar_coarse_preconditioner'].get(key) for key in ('status', 'construction_seconds', 'actual_operator_entry_calls', 'actual_QP_schema', 'fallback_to_frozen_v3')}))
    fixed=r['fixed_scalar_metric'];identity=fixed['identity_sha256']
    context=r['exact_tail_context'];final_context=r['exact_tail_context_final']
    definition=context['definition'];profile=fixed['exact_profile_definition']
    canonical=lambda value:hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
    if (fixed.get('target_fixed_before_first_direction') is not True
            or fixed.get('target_recomputed_from_current_field') is not False
            or fixed.get('moving_mean_projection') is not False
            or fixed.get('all_metric_mean_constraints_retained') is not True
            or canonical(profile)!=identity
            or definition.get('profile_definition')!=profile
            or definition.get('profile_identity_sha256')!=identity
            or canonical(definition)!=context['model_identity_sha256']
            or final_context['definition']!=definition
            or r['initial']['fixed_scalar_metric_identity_sha256']!=identity
            or r['final_statistics']['fixed_scalar_metric_identity_sha256']!=identity):
        raise ValueError('The actual full run must keep ONE independently identified exact scalar target')
    initial = metric(r['initial'])
    final = metric(r['final_statistics'])
    for key in ('p', 'epsilon', 'scale', 'normalization'):
        if initial[key] != final[key]:
            raise ValueError('Cannot compare different spectral definitions/measures')
    summary = dict(schema='complete-refined-fixed-deep-scalar-amplitude-soc-parent-actual-summary-v1', reader_source_sha256=sha(__file__), report_sha256=sha(a.report), actual_solver_source_commit=r['source_commit'], actual_github_run_id=r.get('github_run_id'), reader_source_commit=subprocess.check_output(['git', '-C', str(a.repo), 'rev-parse', 'HEAD'], text=True).strip(), complete_source_binding=binding, actual_parent_bundle_sha256=r['bundle_sha256'], actual_final_bundle_sha256=r['final_bundle_sha256'], fixed_scalar_metric_identity_sha256=identity, fixed_scalar_target=r['fixed_scalar_metric'], actual_current_model_identity_sha256=r['exact_tail_context']['model_identity_sha256'], actual_M=r['M'], actual_N=r['N'], actual_J=r['J'], original_free_variables=r['original_variables'], all_full_rows=r['all_full_rows'], selected_scalar_objective_key=objective, initial_metric=initial, final_metric=final, actual_same_measure_Phi_change=final['phi'] - initial['phi'], actual_same_measure_centered_Phi_change=final['centered_phi'] - initial['centered_phi'] if final['centered_phi'] is not None and initial['centered_phi'] is not None else None, amplitude_budgets=r['amplitude_design_constraints']['budgets'], initial_amplitude=amplitude(r['initial_amplitude_filter']), final_amplitude=amplitude(r['final_amplitude_filter']), final_necessary_curvature_filter=r['final_curvature_filter'], directions=direction_records, actual_direction_count=r['actual_direction_count'], actual_accepted_direction_count=r['actual_accepted_direction_count'], actual_final_damping=r['final_damping'], final_permanent_counts=r['final_permanent_position_counts'], process_peak_rss_KiB=r['process_peak_rss_KiB'], actual_stop_before_linear=r.get('stopped_before_linear_iteration'), final_metric_frozen=True, moving_mean_projection=False, all_metric_mean_constraints_retained=True, explicit_fixed_target_stopping_threshold=r['explicit_fixed_target_stopping_threshold'], zero_direction_exit=len(r['directions'])==0, actual_maximum_gram_change=final['max_relative_gram']-initial['max_relative_gram'], stopping_threshold_is_not_README_original_solver_floor=True, fixed_g_refinement_convergence_claimed=False, continuous_amplitude_certified=False, reach_certified=False, topic_completion_claimed=False)
    metadata=r['common_parent_measure_comparison']
    parent_path=a.comparison_parent_report or Path(metadata['parent_report_path'])
    if sha(parent_path)!=metadata['parent_report_sha256']:
        raise ValueError('The actual common-measure parent report differs from the saved comparison')
    parent=json.loads(parent_path.read_text())
    binding_path=source/'fixed_deep_refinement_parent_binding.py'
    if sha(binding_path)!='b3e391847c6e1367ca43b3bc83f4f570aafd48e87eafe93f4d049d85b288cdbf':
        raise ValueError('Changed complete parent-binding source')
    spec=importlib.util.spec_from_file_location('_actual_deep_refinement_parent_binding',binding_path)
    parent_binder=importlib.util.module_from_spec(spec);sys.modules[spec.name]=parent_binder
    spec.loader.exec_module(parent_binder)
    parent_binding=parent_binder.bind_parent(parent,a.repo,current_fine_schema=SCHEMA,
        current_fine_source=source/EXPECTED['driver'][0], current_fine_sha256=EXPECTED['driver'][1])
    if metadata.get('actual_complete_parent_source_binding')!=parent_binding:
        raise ValueError('The actual full parent binding differs from the fine solver record')
    if (parent.get('complete') is not True
            or parent['fixed_scalar_metric']['identity_sha256']!=identity
            or parent['final_bundle_sha256']!=metadata['parent_final_bundle_sha256']
            or parent['observation_carrier_sha256']!=metadata['parent_carrier_sha256']
            or parent['selected_scalar_objective_key']!=objective):
        raise ValueError('A complete same-target, same-objective actual parent is required')
    parent_metric=metric(parent['final_statistics'])
    for key in ('p','epsilon','scale'):
        if parent_metric[key]!=initial[key]:
            raise ValueError('No comparison across spectral parameters')
    if (metadata['parent_Phi']!=parent_metric['phi']
            or metadata['parent_centered_Phi']!=parent_metric['centered_phi']
            or metadata['parent_max_relative_Gram']!=parent_metric['max_relative_gram']):
        raise ValueError('The recorded parent scalars differ from their actual final report')
    common_records={}
    for label,stat in (('initial',r['initial']),('final',r['final_statistics'])):
        common=stat['common_parent_measure'];cs=common['spectral']
        if (common['parent_report_sha256']!=sha(parent_path)
                or common['fixed_scalar_metric_identity_sha256']!=identity
                or common.get('same_literal_parent_observation_measure') is not True
                or common.get('parent_literal_a_carriers_used') is not True
                or common.get('old_field_or_J_reevaluated') is not False
                or common.get('additional_field_or_J_calls')!=0
                or cs['normalization']!=parent_metric['normalization']):
            raise ValueError('The fine readout must use the actual same parent numerical measure and carriers')
        common_records[label]=dict(max_relative_gram=finite(cs['max_gram'],'same-parent metric'),
            phi=finite(cs['phi_normalized'],'same-parent Phi'),
            centered_phi=cs.get('centered_phi_normalized'),
            actual_Phi_minus_parent=common['actual_fine_minus_parent_Phi'],
            actual_centered_Phi_minus_parent=common['actual_fine_minus_parent_centered_Phi'],
            a_ratio_minimum=common['a_ratio_minimum'],a_ratio_maximum=common['a_ratio_maximum'],
            target_carriers_bitwise_identical=common['target_carriers_bitwise_identical'],
            original_parent_a_renormalization=common['residual_renormalization'])
    summary.update(actual_complete_parent_source_binding=parent_binding, actual_parent_comparison_report_sha256=sha(parent_path),
        actual_parent_metric=parent_metric,common_parent_measure=metadata,
        initial_on_common_parent=common_records['initial'],final_on_common_parent=common_records['final'],
        actual_common_parent_metric_change=common_records['final']['max_relative_gram']-parent_metric['max_relative_gram'],
        actual_common_parent_Phi_change=common_records['final']['phi']-parent_metric['phi'],
        actual_common_parent_centered_Phi_change=(common_records['final']['centered_phi']-parent_metric['centered_phi']
            if common_records['final']['centered_phi'] is not None and parent_metric['centered_phi'] is not None else None),
        ordinary_floating_comparison_not_outward=True,additional_parent_field_or_J_calls=0,
        zero_step_or_threshold_success_is_not_refinement_convergence=True,
        stopped_before_linear_iteration=r.get('stopped_before_linear_iteration'),
        fixed_g_refinement_convergence_claimed=False,topic_completion_claimed=False)
    if a.out.exists():
        raise FileExistsError(a.out)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(summary, indent=2, allow_nan=False) + '\n')
    print(json.dumps(dict(summary=str(a.out.resolve()), summary_sha256=sha(a.out), final_bundle_sha256=r['final_bundle_sha256'], final_metric=final['max_relative_gram'], final_amplitude_passed=summary['final_amplitude']['passed'], actual_accepted_directions=summary['actual_accepted_direction_count'], continuous_amplitude_certified=False, reach_certified=False)), flush=True)
if __name__ == '__main__':
    main()

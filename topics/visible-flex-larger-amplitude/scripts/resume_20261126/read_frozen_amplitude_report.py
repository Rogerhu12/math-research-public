#!/usr/bin/env python3
"""Read only an actual byte-bound complete frozen-target/amplitude report.

No raw arrays, scientific operators, derivatives, or numerical fixtures are
loaded. Complete source identities and every actual direction/acceptance
record are checked before extracting a compact, honestly scoped summary.
This schema is distinct from R684/R688 and cannot use their old report binder.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess

SCHEMA='complete-fixed-frozen-target-with-held-amplitude-budgets-v1'
EXPECTED={
 'driver':('fullclosed_frozen_metric_amplitude_qp.py','859ceb836378c3140a0d27877987f3d06546aae2baee0ef316403d3f332d911b'),
 'amplitude_rows':('held_amplitude_inequalities_v2.py','d494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'),
 'amplitude_screen':('held_amplitude_screen_v2.py','e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f'),
 'frozen_coarse':('frozen_metric_coarse_moments.py','a531818d75040ff571ad1249eecb3c18f7341284d1cdd86d2032b0f8f4ef9f63'),
 'frozen_target':('frozen_mean_metric.py','9d6440ab9f86cfe5312b78643e704a3ec861f2c5b6fd45047461af92eca81d28'),
 'qp':('fullspace_feasible_active_pcg_v5.py','76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8')}
CENTERED_SHA='5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01'


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def finite(value,label):
    if isinstance(value,bool) or not isinstance(value,(float,int)) or not math.isfinite(value):
        raise ValueError('A finite actual scalar is required: '+label)
    return float(value)


def metric(value):
    s=value['spectral']
    return dict(max_relative_gram=finite(value['max_relative_gram'],'metric max'),
        old_fixed_metric_max_diagnostic=value.get('old_fixed_metric_max_diagnostic'),
        phi=finite(s['phi_normalized'],'Phi'),centered_phi=s.get('centered_phi_normalized'),
        p=s['p'],epsilon=s['epsilon'],scale=s['scale'],normalization=s['normalization'])


def amplitude(value):
    if not value.get('complete'):
        return dict(complete=False,passed=False,actual_read_error=value.get('reason'))
    return dict(complete=True,passed=bool(value['passed']),
        maximum_inequality_value=value['maximum_inequality_value'],
        maximum_by_kind={key:item['value'] for key,item in value['maximum_inequality_by_kind'].items()},
        scalar_inequalities=value['scalar_inequalities'],current_witness_radius=value['current_witness_radius'],
        height=value['height'],grid_points=value['grid_quarter_points_read'],
        permanent_points=value['distinct_arbitrary_points_read'],
        required_permanent_points=value['required_distinct_arbitrary_points'],
        exact_permanent_set_complete=value['exact_arbitrary_location_set_equals_required_set'],
        sampled_minimum_witness_distance_squared=value['minimum_witness_distance_squared'],
        sampled_minimum_is_not_a_global_distance_lower_bound=True,
        proposed_appended_rows=value['proposed_appended_rows_including_cap_and_height'],
        continuous_amplitude_certified=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Actual scientific report attribution belongs in this public repository Actions')
    source=a.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    r=json.loads(a.report.read_text())
    if r.get('schema')!=SCHEMA or r.get('complete') is not True:
        raise ValueError('Need a naturally completed actual complete amplitude-design report')
    binding={}
    for role,(name,digest) in EXPECTED.items():
        path=source/name
        if sha(path)!=digest:raise ValueError('Changed complete published source: '+role)
        recorded=r.get('source_sha256') if role=='driver' else r['source_sha256_by_role'].get(role)
        if recorded!=digest:raise ValueError('The actual report is not bound to this complete source: '+role)
        binding[role]=dict(path=str(path),sha256=digest)
    objective=r['selected_scalar_objective_key']
    if objective=='centered_phi_normalized':
        if (r['source_sha256_by_role'].get('centered_loss')!=CENTERED_SHA
                or sha(source/'centered_spectral_statistics.py')!=CENTERED_SHA):
            raise ValueError('The actual centered scalar definition changed')
    elif objective!='phi_normalized':raise ValueError('Unknown actual spectral scalar objective')
    direction_records=[]
    for index,d in enumerate(r['directions']):
        if d['index']!=index or not isinstance(d['accepted'],bool):
            raise ValueError('Use the complete actual ordered direction history')
        trial_acceptance=[]
        for t in d['trials']:
            potential=bool(t['feasible'] and t['descent'])
            full_pass=bool(potential and t['curvature_feasible'] and t['amplitude_feasible'])
            if full_pass:
                amp=t['amplitude_filter']
                if not (amp['complete'] and amp['passed'] and amp['complete_grid_coverage']
                        and amp['exact_arbitrary_location_set_equals_required_set']):
                    raise ValueError('An accepted candidate lacks its actual complete true amplitude read')
            trial_acceptance.append(full_pass)
        if sum(trial_acceptance)!=int(d['accepted']):
            raise ValueError('The actual true line-search acceptance disagrees with the saved direction')
        rows=d['active_geometry'];extra=rows['amplitude']
        if (extra['original_prefix_rows']!=d['original_geometry_rows_retained']
                or rows['selected_rows']!=extra['original_prefix_rows']+extra['appended_rows']
                or extra['appended_rows']!=d['appended_amplitude_rows']):
            raise ValueError('The complete old/new row counts disagree')
        direction_records.append(dict(index=index,accepted=d['accepted'],accepted_alpha=d.get('accepted_alpha'),
            qp_schema=d['qp'].get('schema'),qp_status=d['qp']['status'],qp_advances=d['qp']['advances'],
            actual_old_geometry_rows=extra['original_prefix_rows'],actual_amplitude_rows=extra['appended_rows'],
            total_working_rows=rows['selected_rows'],combined_row_cache_bytes=rows['row_cache_bytes'],
            original_geometry_row_cache_bytes=d['original_geometry_row_cache_bytes'],
            total_scratch_row_cache_bytes=d['total_scratch_row_cache_bytes'],
            maximum_linear_reach_product=d['maximum_selected_linear_product'],
            maximum_linear_amplitude_g=d['maximum_selected_linear_amplitude_value'],
            true_trials=len(d['trials']),true_amplitude_failed_trials=sum(
                t['amplitude_filter'] is not None and not t['amplitude_feasible'] for t in d['trials']),
            current_fixed_target_coarse={key:d['fixed_target_preconditioner'].get(key) for key in
                ('status','construction_seconds','actual_operator_entry_calls','actual_QP_schema','fallback_to_frozen_v3')}))
    initial=metric(r['initial']);final=metric(r['final_statistics'])
    for key in ('p','epsilon','scale','normalization'):
        if initial[key]!=final[key]:raise ValueError('Cannot compare different spectral definitions/measures')
    summary=dict(schema='complete-fixed-target-held-amplitude-actual-summary-v1',
        reader_source_sha256=sha(__file__),report_sha256=sha(a.report),
        actual_solver_source_commit=r['source_commit'],actual_github_run_id=r.get('github_run_id'),
        reader_source_commit=subprocess.check_output(['git','-C',str(a.repo),'rev-parse','HEAD'],text=True).strip(),
        complete_source_binding=binding,actual_parent_bundle_sha256=r['bundle_sha256'],
        actual_final_bundle_sha256=r['final_bundle_sha256'],mean_averaging=r['frozen_metric_target']['averaging'],
        frozen_target_identity_sha256=r['frozen_metric_target']['target_identity_sha256'],
        frozen_target_manifest_sha256=r['frozen_metric_target']['manifest_sha256'],
        target_full_angles=r['frozen_metric_target']['frozen_full_angles'],
        common_parent_measure=r['final_statistics'].get('common_parent_measure'),
        actual_M=r['M'],actual_N=r['N'],actual_J=r['J'],
        original_free_variables=r['original_variables'],all_full_rows=r['all_full_rows'],
        selected_scalar_objective_key=objective,initial_metric=initial,final_metric=final,
        actual_same_measure_Phi_change=final['phi']-initial['phi'],
        actual_same_measure_centered_Phi_change=(final['centered_phi']-initial['centered_phi']
            if final['centered_phi'] is not None and initial['centered_phi'] is not None else None),
        amplitude_budgets=r['amplitude_design_constraints']['budgets'],
        initial_amplitude=amplitude(r['initial_amplitude_filter']),
        final_amplitude=amplitude(r['final_amplitude_filter']),
        final_necessary_curvature_filter=r['final_curvature_filter'],directions=direction_records,
        actual_direction_count=r['actual_direction_count'],
        actual_accepted_direction_count=r['actual_accepted_direction_count'],
        actual_final_damping=r['final_damping'],final_permanent_counts=r['final_permanent_position_counts'],
        process_peak_rss_KiB=r['process_peak_rss_KiB'],
        actual_stop_before_linear=r.get('stopped_before_linear_iteration'),
        final_metric_frozen=True,all_fixed_target_mean_constraints_retained=True,
        common_parent_measure_present='common_parent_measure' in r['final_statistics'],
        declared_numerical_target=r['target'],zero_direction_exit=r['zero_direction_exit'],
        fixed_g_refinement_convergence_certified=False,
        continuous_amplitude_certified=False,reach_certified=False,topic_completion_claimed=False)
    if a.out.exists():raise FileExistsError(a.out)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(summary=str(a.out.resolve()),summary_sha256=sha(a.out),
        final_bundle_sha256=r['final_bundle_sha256'],final_metric=final['max_relative_gram'],
        frozen_target_identity_sha256=r['frozen_metric_target']['target_identity_sha256'],
        final_amplitude_passed=summary['final_amplitude']['passed'],
        actual_accepted_directions=summary['actual_accepted_direction_count'],
        continuous_amplitude_certified=False,reach_certified=False)),flush=True)


if __name__=='__main__':main()

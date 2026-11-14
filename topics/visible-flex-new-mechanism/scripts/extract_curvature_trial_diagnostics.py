#!/usr/bin/env python3
"""Read preserved curvature outputs and summarize trial rejection causes.

This is an Actions-only JSON transformation, with no geometry, derivative,
quadrature or optimization call. The original full report is never modified.
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
ORIGINAL_RUN = '43645177423'
ORIGINAL_SOURCE = '2f1b809c0b0abb7a26303d36940edc203815f872'
FULL_SHA256 = '5b04d6a7c85870687b979bbda87bbf8bd4d429d3b36c918d83cebde59b4dcaa0'
FULL_BYTES = 5220015
SOURCE_SHA256 = {
    'frame_curvature_epigraph_exchange.py': '8c26353df012ca61f37149b2e2ab52acaec4ca22fde68017261c0bd68992ebf5',
    'frame_curvature_epigraph_exchange_audit.py': '7162b7c56bb865591316b1ca576c7b0929d55619353567ccd4f3df789543802a',
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def record_row(record, groups):
    d = record['decision']
    separation = record['whole_grid_and_pool_separation_at_this_same_trial']
    counts = separation['group_counts']
    whole = [int(counts[g]['whole_grid']) for g in groups]
    omitted = [int(counts[g]['omitted']) for g in groups]
    cap = d['cap_and_box']
    return {
        'evaluation':record['epigraph_evaluation'],
        'physical_evaluation':record['physical_geometry_evaluation'],
        'phase':record['phase'],
        'elapsed_seconds':record['elapsed_seconds'],
        'optimization_seconds':record['optimization_elapsed_seconds'],
        'pool_version':record['pool_version'],
        'pool_rows':record['pool_rows'],
        'kappa':d['direct_maximum_absolute_principal_curvature'],
        'kappa_location':d['direct_max_curvature_location'],
        'lambda':d['curvature_auxiliary_lambda'],
        'eta':d['direct_max_eta'],
        'eta_location':d['direct_max_eta_location'],
        'fixed_metric_excess':d['direct_eta_minus_fixed_budget'],
        'physical_excluding_metric_ok':d['physical_gate_pass_excluding_fixed_metric'],
        'metric_and_physical_ok':d['eligible_under_fixed_metric_and_physical_gates'],
        'auxiliary_and_all_ok':d['eligible_under_all_declared_sampled_constraints'],
        'cap_margin':min(cap['affine_height_margin'],cap['reconstructed_height_margin']),
        'box_violation':cap['box_violation'],
        'signed_z_min':d['minimum_signed_height'],
        'ball_squared_normalized_max':d['ball_radius_squared_normalized_max'],
        'absolute_y_max':d['maximum_absolute_y'],
        'inner_strip_margin':d['inner_strip_absolute_margin'],
        'mirror_radius_min':d['direct_mirror_radius_min_finite'],
        'normal_area_over_a_min':d['first_order_normal_area_over_a_min_sample'],
        'regular':d['regularity_screen_pass'],
        'metric_row_min':d['divided_metric_row_min'],
        'curvature_PSD_min':min(d['curvature_scaled_row_minima'].values()),
        'whole_violations_by_group':whole,
        'omitted_violations_by_group':omitted,
        'enforced_pool_violations_by_group':[a-b for a,b in zip(whole,omitted)],
        'whole_violations':sum(whole),
        'omitted_violations':sum(omitted),
        'enforced_pool_violations':sum(whole)-sum(omitted),
    }


def summarize(full, raw, path):
    if (full.get('schema')!='same-g-fixed-metric-budget-curvature-row-exchange-audit-v1'
            or full.get('status')!='complete-shared-budget-actual-curvature-exchange-audit'
            or str(full.get('github_run_id'))!=ORIGINAL_RUN
            or full.get('github_sha')!=ORIGINAL_SOURCE
            or full.get('artificial_inputs_only') is not False):
        raise ValueError('the requested completed original actual report is required')
    for name, sha in SOURCE_SHA256.items():
        if full.get('source_files_sha256',{}).get(name)!=sha:
            raise ValueError('original curvature source hash differs: '+name)
    stage=full['curvature_exchange_stage']
    checkpoint=stage['checkpoint']
    pool_history=checkpoint['active_row_pool_history']
    groups=pool_history[0]['group_order']
    if len(groups)!=11 or any(x['group_order']!=groups for x in pool_history):
        raise ValueError('the eleven-group order changed within the original run')
    rows=[record_row(r,groups) for r in checkpoint['history']]
    if len(rows)!=checkpoint['epigraph_vector_evaluations']:
        raise ValueError('the saved trial history is incomplete')
    def minimum(predicate):
        candidates=[r for r in rows if predicate(r)]
        return None if not candidates else min(candidates,key=lambda r:(r['kappa'],r['eta'],r['evaluation']))
    best={}
    for name in ['best_physical_curvature_point','best_auxiliary_feasible_lambda_point',
                 'best_auxiliary_feasible_curvature_point','lowest_lambda_trial_may_be_ineligible']:
        point=checkpoint.get(name)
        best[name]=None if point is None else {
            'physical_state_sha256':point['physical_state_sha256'],
            'auxiliary_zeta_evaluated':point['auxiliary_zeta_evaluated'],
            'auxiliary_lambda_evaluated':point['auxiliary_lambda_evaluated'],
            'history_evaluation':point['record']['epigraph_evaluation'],
        }
    rounds=[]
    for rd in stage['solver']['rounds']:
        separation=rd.get('full_grid_separation',{})
        bygroup=separation.get('groups',{})
        rounds.append({
            'round':rd['round'],'pool_version':rd['pool_version'],'pool_rows':rd['pool_rows'],
            'major_iterations':rd['major_iterations'],'exit_reason':rd['exit_reason'],
            'library_result':rd.get('library_result'),
            'omitted_violations':separation.get('omitted_violating_count'),
            'omitted_violations_by_group':[bygroup.get(g,{}).get('omitted_violating_count') for g in groups],
            'minimum_rows_by_group':[bygroup.get(g,{}).get('whole_grid_minimum_row') for g in groups],
            'callback_trigger_tolerances':[bygroup.get(g,{}).get('trigger_tolerance') for g in groups],
            'actual_eligibility_tolerances':[bygroup.get(g,{}).get('actual_eligibility_tolerance') for g in groups],
            'added_rows':len((rd.get('pool_addition') or {}).get('added_row_indices',[])),
            'omitted_after_addition':(rd.get('pool_addition') or {}).get('omitted_violations_after_this_addition'),
            'next_auxiliary_initialization':rd.get('next_auxiliary_initialization'),
        })
    return {
        'schema':'preserved-curvature-trial-rejection-diagnostics-v1',
        'source_full_report':{'path':str(path),'raw_bytes':len(raw),'raw_sha256':digest(raw),
            'original_run_id':ORIGINAL_RUN,'original_source_commit':ORIGINAL_SOURCE},
        'extractor_source_sha256':digest(Path(__file__).read_bytes()),
        'extraction_run_id':os.environ.get('GITHUB_RUN_ID'),
        'extraction_source_commit':os.environ.get('GITHUB_SHA'),
        'research_geometry_evaluated':False,'optimizer_called':False,
        'original_scientific_output_modified':False,
        'group_order_for_all_count_and_minimum_arrays':groups,
        'counts_use_the_original_actual_eligibility_tolerances':True,
        'round_callback_tolerance_may_differ_and_is_preserved_separately':True,
        'solver':{k:v for k,v in stage['solver'].items() if k!='rounds'},
        'original_stage_status':stage['status'],
        'original_stage_error':stage.get('error'),
        'initial_physical_sha256':full['initial_state']['canonical_physical_state_sha256'],
        'final_physical_sha256':full['final_state']['canonical_physical_state_sha256'],
        'final_equals_initial_physical_sha':full['initial_state']['canonical_physical_state_sha256']==full['final_state']['canonical_physical_state_sha256'],
        'minimum_kappa_any_saved_trial':minimum(lambda r:True),
        'minimum_kappa_physical_gates_excluding_fixed_metric':minimum(lambda r:r['physical_excluding_metric_ok']),
        'minimum_kappa_fixed_metric_and_physical_gates':minimum(lambda r:r['metric_and_physical_ok']),
        'eligible_distinct_physical_evaluation_numbers':sorted({r['physical_evaluation'] for r in rows if r['metric_and_physical_ok']}),
        'best_saved_points':best,'rounds':rounds,'trial_history':rows,
        'not_a_new_convergence_claim_or_continuous_geometric_certificate':True,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS','').lower()!='true' or os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY:
        raise SystemExit('this report-only extraction is restricted to the authorized public Actions')
    opener=gzip.open if a.report.suffix=='.gz' else open
    with opener(a.report,'rb') as handle:
        raw=handle.read(FULL_BYTES+1)
    if len(raw)!=FULL_BYTES or digest(raw)!=FULL_SHA256:
        raise ValueError('the exact preserved original full-report bytes differ')
    full=json.loads(raw)
    result=summarize(full,raw,a.report)
    data=(json.dumps(result,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode('utf-8')
    if len(data)>95000:
        raise ValueError('semantic trial diagnostic exceeds its declared 95 KB bound')
    a.out.parent.mkdir(parents=True,exist_ok=True)
    fd,name=tempfile.mkstemp(prefix='.trial-diagnostic-',dir=str(a.out.parent))
    try:
        with os.fdopen(fd,'wb') as handle: handle.write(data)
        os.replace(name,a.out)
    finally:
        if os.path.exists(name): os.unlink(name)
    print(json.dumps({'status':'complete-preserved-report-only-extraction',
        'out':str(a.out),'bytes':len(data),'sha256':digest(data),'geometry_recomputed':False}),flush=True)


if __name__=='__main__':
    main()

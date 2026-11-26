#!/usr/bin/env python3
"""Attribute one actual complete mean/amplitude/inward-SOC report, scalars only.

This reader binds the whole new source body with its own source deriver.
It never presents the new schema as R684, R688, or the old curvature-only
R683 driver. The old pure reader supplies only final-face/preconditioner
formatting functions after this new report has been independently bound.
No NumPy, raw field arrays, scientific operators or fixtures are loaded.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys

DERIVER_SHA='e731954fa5e62ec7b6bb7098f993fcc00ba03e9e924e15f7ea1d64472419d0a4'
PURE_MEAN_READER_SHA='3489a041559a17be2975b8f7c5c39a27b4ab974976a9e0610dcbe153e3e0a98e'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_bound(name,path,digest):
    if sha(path)!=digest:raise ValueError('Changed complete pure reader dependency '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def finite(value):
    return isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value)


def divide(a,b):
    return a/b if finite(a) and finite(b) and b!=0 else None


def choose(record,keys):
    return {key:record.get(key) for key in keys}


def sanitize(value):
    if isinstance(value,float) and not math.isfinite(value):return None
    if isinstance(value,dict):return {str(key):sanitize(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)):return [sanitize(item) for item in value]
    return value


def amplitude(screen):
    if not isinstance(screen,dict):return dict(read=False,complete=False,passed=None)
    maxima=screen.get('maximum_inequality_by_kind') or {}
    return dict(read=True,complete=screen.get('complete'),passed=screen.get('passed'),
        maximum_inequality_value=screen.get('maximum_inequality_value'),
        maximum_inequality_by_kind=maxima,scalar_inequalities=screen.get('scalar_inequalities'),
        all_grid_points_read=screen.get('complete_grid_coverage'),
        exact_arbitrary_set_complete=screen.get('exact_arbitrary_location_set_equals_required_set'),
        grid_quarter_points_read=screen.get('grid_quarter_points_read'),
        distinct_arbitrary_points_read=screen.get('distinct_arbitrary_points_read'),
        required_distinct_arbitrary_points=screen.get('required_distinct_arbitrary_points'),
        current_witness_radius=screen.get('current_witness_radius'),height=screen.get('height'),
        actual_read_error=screen.get('reason'),continuous_amplitude_certified=False)


def trial_view(t,d,objective_key):
    kind=t.get('update_kind')
    if kind=='original_ray':
        model=dict(half_objective_slope=d['half_objective_slope'],
            squared_model_step_norm=d['original_model_step_squared_norm'])
    elif kind=='complete_rows_soc':
        model=d['complete_rows_SOC'].get('corrected_same_parent_model')
        if model is None:raise ValueError('A true corrected trial needs its own actual A*z model')
    else:raise ValueError('Unknown actual accepted-update type')
    if t.get('half_objective_slope_used')!=model['half_objective_slope']:
        raise ValueError('The true trial used a different direction objective slope')
    alpha=t['alpha'];old=d['old_merit'];merit=t['merit']
    if not finite(alpha) or alpha<=0:raise ValueError('A real trial needs its literal positive alpha')
    predicted_gain=-(2*alpha*model['half_objective_slope']+alpha*alpha*model['squared_model_step_norm'])
    actual_gain=old-merit if finite(old) and finite(merit) else None
    failures=[];missing=[]
    if t.get('finite') is not True:failures.append('actual_objective_read_nonfinite_or_failed')
    if t.get('finite') is True and t.get('feasible') is not True:
        failures.append('actual_positive_metric_density_domain_failed')
    if t.get('finite') is True and t.get('descent') is not True:
        failures.append('actual_same_Phi_strict_or_Armijo_descent_failed')
    geometry=t.get('curvature_points');filt=t.get('curvature_filter');amp=t.get('amplitude_filter')
    if geometry is None:
        missing.append('full_actual_geometry_not_read_after_objective_or_domain_rejection')
    else:
        if geometry.get('complete') is not True:failures.append('actual_full_geometry_read_incomplete')
        if filt is None:missing.append('actual_curvature_filter_missing')
        elif filt.get('passed') is not True:failures.append('actual_curvature_filter_failed')
    if amp is None:missing.append('actual_amplitude_filter_not_read')
    else:
        if amp.get('complete') is not True:failures.append('actual_amplitude_read_incomplete')
        elif amp.get('passed') is not True:failures.append('actual_amplitude_budget_failed')
    accepted=bool(t.get('finite') and t.get('feasible') and t.get('descent')
        and t.get('curvature_feasible') and t.get('amplitude_feasible'))
    if accepted:
        if (not geometry or geometry.get('complete') is not True or not filt or filt.get('passed') is not True
                or not amp or amp.get('complete') is not True or amp.get('passed') is not True
                or amp.get('complete_grid_coverage') is not True
                or amp.get('exact_arbitrary_location_set_equals_required_set') is not True):
            raise ValueError('Accepted field lacks its literal full curvature/amplitude/memory read')
        if failures or missing:raise ValueError('Accepted trial has actual failures or missing reads')
        scalar=(t.get('statistics') or {}).get('spectral',{}).get(objective_key)
        if scalar!=merit:raise ValueError('Accepted Phi is not the selected actual scalar')
    return dict(index=t['index'],update_kind=kind,original_ray_trial_index=t.get('original_ray_trial_index'),
        alpha=alpha,accepted_actual_trial=accepted,actual_same_Phi=merit,
        actual_same_objective_gain=actual_gain,model_prediction_for_THIS_actual_step=-predicted_gain,
        actual_to_THIS_step_model_gain=divide(actual_gain,predicted_gain),
        same_parent_model_half_slope=model['half_objective_slope'],
        finite=t.get('finite'),feasible=t.get('feasible'),descent=t.get('descent'),
        curvature_feasible=t.get('curvature_feasible'),amplitude_feasible=t.get('amplitude_feasible'),
        failure_classes=failures,failure_classes_json=json.dumps(failures,separators=(',',':')),
        unperformed_or_missing_checks=missing,
        unperformed_or_missing_checks_json=json.dumps(missing,separators=(',',':')),
        actual_curvature_filter=filt,
        actual_curvature_worst=None if geometry is None else geometry.get('worst'),
        actual_grid_curvature_worst=None if geometry is None else geometry.get('observation_grid_worst'),
        actual_radius_worst=None if geometry is None else geometry.get('maximum_radius_point'),
        actual_amplitude=amplitude(amp),arithmetic_error=t.get('arithmetic_error'),
        new_permanent_locations=dict(curvature=t.get('new_permanent_curvature_locations'),
            radius=t.get('new_permanent_radius_locations'),amplitude=t.get('new_permanent_amplitude_locations')),
        no_step_prediction_borrowed_from_another_direction=True,
        finite_geometry_is_not_continuous_certification=True)


def typed_rows_view(read):
    if not isinstance(read,dict):return None
    rows=read.get('rows') or []
    positive=[item for item in rows if finite(item.get('normalized_constraint_value'))
        and item['normalized_constraint_value']>0]
    worst=max(rows,key=lambda item:item.get('normalized_constraint_value',-math.inf)) if rows else None
    return dict(complete=read.get('complete'),current_total_rows=read.get('current_total_rows'),
        maximum_normalized_constraint=read.get('maximum_normalized_constraint'),
        positive_row_count=len(positive),positive_rows=positive,worst_row=worst,
        failed_row=read.get('failed_row'),reason=read.get('reason'),
        fixed_parent_scales=read.get('fixed_parent_scales'))


def soc_view(d,trials):
    soc=d.get('complete_rows_SOC') or {};projection=soc.get('constrained_projection') or {}
    index=soc.get('corrected_actual_trial_index')
    corrected=None
    if index is not None:
        selected=[item for item in trials if item['index']==index]
        if len(selected)!=1 or selected[0]['update_kind']!='complete_rows_soc':
            raise ValueError('SOC corrected trial index does not identify its actual corrected candidate')
        corrected=selected[0]
        if soc.get('corrected_actual_trial_accepted')!=corrected['accepted_actual_trial']:
            raise ValueError('SOC actual acceptance flag disagrees with its complete true trial')
    return dict(**choose(soc,('attempted','complete','proposal_available','reason','seconds',
            'original_QP_rows','current_complete_rows','appended_separation_rows',
            'all_original_rows_retained','tau','inward_fraction','inward_normalized_offset',
            'inward_policy','coordinate_norm','correction_norm','correction_over_original_norm',
            'corrected_coordinate_norm','original_QP_maximum_linear_violation',
            'all_current_linear_violation','corrected_maximum_linear_violation',
            'corrected_all_nonlinear_target_linear_violation','direct_Cd_plus_Ce_discrepancy',
            'corrected_candidate_A_entry_counts','whole_SOC_outer_A_entry_counts',
            'corrected_model_or_trial_numeric_error','arithmetic_error')),
        separation=soc.get('separation'),corrected_same_parent_model=soc.get('corrected_same_parent_model'),
        constrained_projection=choose(projection,('schema','status','numerical_feasible','sweeps',
            'rows','ambient_coordinates','actual_maximum_violation',
            'direct_projected_dual_gradient_inf','minimum_norm_convergence_claimed',
            'primal_objective','dual_objective',
            'floating_primal_dual_gap','complementarity_max_abs','preparation_seconds','seconds',
            'infeasibility_proved','note')),
        full_rejected_trial_fixed_parent_rows=typed_rows_view(soc.get('full_trial_fixed_parent_rows')),
        corrected_fixed_parent_rows=typed_rows_view(soc.get('corrected_fixed_parent_rows')),
        corrected_actual_trial=corrected,
        numerical_inward_policy_is_not_a_local_MFCQ_certificate=True,
        every_finite_C_row_passing_does_not_imply_full_geometry_acceptance=True)


def analyze(r,old_reader):
    key=r['selected_scalar_objective_key'];parent=r['initial'];directions=[]
    for index,d in enumerate(r['directions']):
        if d['index']!=index or d['old_merit']!=parent['spectral'][key]:
            raise ValueError('Direction and actual same-functional parent order changed')
        trials=[trial_view(t,d,key) for t in d['trials']]
        if [t['index'] for t in trials]!=list(range(len(trials))):
            raise ValueError('Use the complete true trial order')
        accepted=[t for t in trials if t['accepted_actual_trial']]
        if len(accepted)!=int(d['accepted']):raise ValueError('Actual acceptance is not unique')
        if accepted:
            actual=accepted[0]
            if (d.get('accepted_trial_index')!=actual['index']
                    or d.get('accepted_update_kind')!=actual['update_kind']
                    or d.get('accepted_alpha')!=actual['alpha']):
                raise ValueError('The saved field does not identify the actual accepted original/corrected trial')
            parent=d['trials'][actual['index']]['statistics']
        rows=d['active_geometry'];amp_rows=rows['amplitude'];qp=d['qp']
        if (amp_rows['original_prefix_rows']!=d['original_geometry_rows_retained']
                or amp_rows['appended_rows']!=d['appended_amplitude_rows']
                or amp_rows['original_prefix_rows']+amp_rows['appended_rows']!=rows['selected_rows']):
            raise ValueError('Original C prefix or amplitude rows were lost')
        pg=qp.get('final_face_projected_gradient_norm');tol=qp.get('gradient_tolerance')
        q0=qp.get('initial_data_objective');qz=qp.get('final_regularized_objective')
        directions.append(dict(**choose(d,('index','accepted','accepted_alpha','accepted_update_kind',
                'accepted_trial_index','accepted_bundle_sha256','old_merit','new_merit','damping',
                'damping_after_direction','seconds','preparation_and_linear_seconds','coordinate_norm',
                'accepted_augmented_full_direction_norm','accepted_model_prediction',
                'accepted_actual_to_same_step_predicted_decrease','inner_counts','outside_inner_calls',
                'total_A_entry_counts_after_line_search','total_scratch_row_cache_bytes')),
            QP=dict(**choose(qp,('schema','status','advances','maxiter','seconds','initial_gradient_norm',
                    'gradient_tolerance','final_face_projected_gradient_norm','maximum_linear_violation',
                    'minimum_multiplier','longest_same_face_advances','maximum_active_face_rank',
                    'operator_products','row_matvec_calls','row_load_calls','reliable_update')),
                q0=q0,qz_regularized=qz,
                regularized_model_gain=q0-qz if finite(q0) and finite(qz) else None,
                Pg_over_reported_tolerance=divide(pg,tol),
                actual_gradient_threshold_satisfied=pg<=tol if finite(pg) and finite(tol) else None,
                iteration_limit_is_not_convergence=True,virtual_rhs_norm_is_not_actual_Phi=True),
            original_C_rows=amp_rows['original_prefix_rows'],amplitude_rows=amp_rows['appended_rows'],
            total_QP_rows=rows['selected_rows'],combined_QP_row_cache_bytes=rows['row_cache_bytes'],
            final_face=old_reader.final_face(qp),
            preconditioner=old_reader.preconditioner_view(d,qp,True),
            complete_rows_SOC=soc_view(d,trials),actual_trials=trials,actual_trial_count=len(trials),
            actual_accepted_gain=accepted[0]['actual_same_objective_gain'] if accepted else 0.))
    return directions


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True);p.add_argument('--report',type=Path,required=True)
    p.add_argument('--driver',type=Path);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Actual returned-scalar attribution runs in this public repository Actions')
    if a.out.exists():raise FileExistsError(a.out)
    source=a.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    deriver=load_bound('complete_typed_SOC_report_body_binder',source/'derive_mean_amplitude_complete_soc.py',DERIVER_SHA)
    old=load_bound('complete_typed_SOC_only_scalar_formatters',source/'read_mean_metric_solver_report.py',PURE_MEAN_READER_SHA)
    r=json.loads(a.report.read_text())
    if r.get('complete') is not True:raise ValueError('Use a naturally completed actual report')
    driver=a.driver or Path(r['diameter_diagnostic_source'])
    if not driver.is_file() and a.driver is None:driver=source/'fullclosed_mean_amplitude_complete_soc.py'
    binding=deriver.bind_report(r,driver,a.repo)
    directions=analyze(r,old)
    result=sanitize(dict(schema='actual-complete-mean-amplitude-inward-SOC-attribution-v1',
        reader_sha256=sha(__file__),report_sha256=sha(a.report),complete_source_binding=binding,
        source_commit=subprocess.check_output(['git','-C',str(a.repo),'rev-parse','HEAD'],text=True).strip(),
        actual_run_id=r.get('github_run_id'),actual_parent_bundle_sha256=r['bundle_sha256'],
        actual_final_bundle_sha256=r['final_bundle_sha256'],
        selected_scalar_objective_key=r['selected_scalar_objective_key'],
        initial=old.stats(r['initial']),final=old.stats(r['final_statistics']),
        initial_damping=r['initial_damping'],final_damping=r['final_damping'],
        amplitude_budgets=r['amplitude_design_constraints']['budgets'],SOC_policy=r['complete_rows_SOC_policy'],
        initial_amplitude=amplitude(r['initial_amplitude_filter']),final_amplitude=amplitude(r['final_amplitude_filter']),
        initial_curvature_filter=r['initial_curvature_filter'],final_curvature_filter=r['final_curvature_filter'],
        final_permanent_position_counts=r['final_permanent_position_counts'],directions=directions,
        actual_direction_count=len(directions),actual_accepted_direction_count=sum(d['accepted'] for d in directions),
        scientific_arrays_read=0,field_evaluations=0,J_calls=0,Jtranspose_calls=0,new_fixtures=0,
        fixed_g_refinement_claimed=False,continuous_metric_or_amplitude_or_reach_claimed=False,
        speedup_claimed=False,strict_arithmetic=False))
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(a.out.resolve()),output_sha256=sha(a.out),
        actual_final_bundle_sha256=r['final_bundle_sha256'],actual_direction_count=len(directions),
        accepted_SOC_directions=sum(d.get('accepted_update_kind')=='complete_rows_soc' for d in directions),
        scientific_arrays_read=0,field_evaluations=0,J_calls=0,Jtranspose_calls=0)),flush=True)


if __name__=='__main__':main()

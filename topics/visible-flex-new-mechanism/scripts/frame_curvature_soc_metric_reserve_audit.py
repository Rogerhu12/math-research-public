#!/usr/bin/env python3
"""Consume the saved arc success; reserve 1e-6 only in SOC metric-row RHS.

The complete g, b0, 163 parameters, all actual gates, old pools and shared
budgets are unchanged. No stored failed point is relabelled as accepted.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import tempfile
import time
import traceback

import numpy as np

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_entry_paired_repair_audit import require_public_actions
from frame_entry_short_bounded_audit import read_input, audit_data, compare_data
from frame_independent_height_solve import state_record
from frame_curvature_epigraph_exchange import GROUPS, candidate_decision
from frame_curvature_mixed_grid_steps import FINE_GROUPS, fine_row_coordinates
from frame_curvature_feasible_steps import linear_proposal
from frame_curvature_soc_metric_reserve import (run_soc_metric_reserve_steps,
    configuration as reserve_configuration,implementation_hashes as reserve_hashes,
    developer_check as reserve_developer_check,RESERVE_POLICY,FLOOR)
import frame_curvature_soc_arc_audit as previous

SCHEMA='same-g-SOC-metric-row-reserve-curvature-audit-v1'
POLICY=RESERVE_POLICY
PRIOR_RUN='43663914259'
PRIOR_SOURCE='e4f7cdd7f57a5127e22890d722b959657a416e07'
PRIOR_FINAL_PHYSICAL_SHA='6ba089c693bba96381a3b41860ce65098ea81d63ace6e3467eb2d10eb33f4bb5'
TARGETS=('55','50','45','40','35','30','25','20','16')
TRUST='1/1000'
INPUTS=previous.INPUTS+['soc_arc_audit']
SHA_NAMES=previous.SHA_NAMES+['soc-arc']
coefficients=previous.coefficients
curvature_grid=previous.curvature_grid
summary_path=previous.summary_path


def implementation_hashes():
    result=previous.implementation_hashes(); result.update(reserve_hashes())
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def configuration(base):
    cfg=reserve_configuration(base)
    if cfg['initial_trust_box_fraction_exact']!=TRUST:
        raise ValueError('this change preserves the published initial primary trust 1/1000')
    return cfg


class MetricReserveObjective(previous.ArcObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.evaluation_definition.update(SOC_metric_row_reserve_policy=POLICY,SOC_metric_row_floor_exact=FLOOR,
            implementation_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)
    def accepted_point(self,state,coarse,fine,reason):
        if not self.accepted_iterates and reason.get('kind')=='saved-d1ca5f-both-grid-accepted-SOC-start':
            reason={'kind':'saved-6ba089-arc-two-grid-success-metric-reserve-start',
                'source_run':PRIOR_RUN,'primary_trust_exact':TRUST}
        return super().accepted_point(state,coarse,fine,reason)


def exact_vector(values,n):
    if not isinstance(values,list) or len(values)!=n:
        raise ValueError('complete exact binary64 vector required')
    result=np.asarray([float(Q(x)) for x in values],float)
    if not np.all(np.isfinite(result)) or coefficients(result)!=values:
        raise ValueError('stored exact coefficients are not their declared binary64 values')
    return result


def replay_arc_success(prepared,prior,*,artificial=False):
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prior.get('schema')!=previous.SCHEMA
            or prior.get('status')!='complete-two-grid-SOC-parabolic-backtracking-curvature-audit'
            or bool(prior.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('the matching completed eighteenth SOC report is required')
    if prior.get('source_files_sha256')!=previous.implementation_hashes() or prior.get('configuration')!=old_cfg:
        raise ValueError('eighteenth frozen implementation/configuration differs')
    if not artificial and (str(prior.get('github_run_id'))!=PRIOR_RUN or prior.get('github_sha')!=PRIOR_SOURCE):
        raise ValueError('eighteenth source or run differs')
    for name,binding in bindings.items():
        recorded=prior.get('exact_input_storage',{}).get(name,{})
        if any(recorded.get(key)!=binding.get(key) for key in
                ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']):
            raise ValueError('eighteenth preceding input byte binding differs: '+name)
    if (prior.get('initial_state')!=state_record(problem,old_initial) or prior.get('input_replay')!=old_replay
            or prior.get('old_optimizer_calls_this_run')!=0 or not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_failed_metric_auxiliary_delta')!=tenth['selected_raw_auxiliary_delta']):
        raise ValueError('eighteenth original state/history binding differs')
    stage=prior['mixed_grid_short_step_stage']; snap=stage['checkpoint']; point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('eighteenth complete accepted physical point missing')
    state=exact_vector(point.get('exact_binary64_physical_coefficients'),problem.nunknown)
    if (state.tolist()!=point.get('physical_parameter_coefficients_binary64')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prior.get('final_state')!=state_record(problem,state)):
        raise ValueError('eighteenth full coefficients or canonical state differs')
    if not artificial and point['physical_state_sha256']!=PRIOR_FINAL_PHYSICAL_SHA:
        raise ValueError('the real continuation must consume the saved 6ba089 point')
    accepted=snap.get('accepted_iterates',[])
    if not accepted or accepted[-1]!=point or problem.metric_model(state)!=problem.metric_model(old_initial):
        raise ValueError('selected SOC point or complete fixed metric differs')
    validation=prior.get('final_selection_validation',{})
    if not validation.get('both_value_grids_physical_gate_pass'):
        raise ValueError('eighteenth final two-grid physical validation failed')
    if not artificial and (stage.get('completed_targets_exact')!=[] or stage.get('active_stage_target_exact')!='55'
            or validation.get('last_active_target_reached') is not False
            or point.get('reason',{}).get('kind')!='SOC-parabolic-backtrack'):
        raise ValueError('preserve actual parabolic success and unfinished55 history')
    for key in ['final_full_grid_constraints','final_doubled_constraints']:
        d=prior.get(key,{})
        if not d.get('eligible_under_fixed_metric_and_physical_gates'):
            raise ValueError('eighteenth original final physical gate failed')
        if any(d.get(field)!=old_cfg[field] for field in
                ['fixed_metric_budget_exact','hard_strip_half_width_exact','mirror_target_exact']):
            raise ValueError('eighteenth physical gate was changed')
    radial,theta,grid=curvature_grid(tenth)
    if prior.get('full_value_sampling_definition')!=grid:
        raise ValueError('eighteenth complete value grid differs')
    history=snap.get('active_row_pool_history',[]); fhistory=snap.get('fine_physical_row_pool_history',[])
    if not history or not fhistory:raise ValueError('eighteenth learned pools missing')
    coarse,fine=history[-1],fhistory[-1]; ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,names,total,rule,cap in [
        (coarse,ci,list(GROUPS),len(GROUPS)*len(radial)*len(theta),
         'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows']),
        (fine,fi,list(FINE_GROUPS),len(FINE_GROUPS)*len(radial)*2*len(theta),
         'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'])]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=names
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap):
            raise ValueError('eighteenth original pool index/group/hash differs')
    if not set(old_coarse).issubset(ci) or not set(old_fine).issubset(fi):
        raise ValueError('eighteenth discarded an already learned coarse or fine row')
    added=fine.get('added_row_indices'); ft=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added) or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=fine_row_coordinates(added,radial,ft)):
        raise ValueError('eighteenth fine original coordinates differ')
    evidence={'policy':POLICY,'floor_exact':FLOOR,'only_selected_metric_group_indices':[0,1],
        'only_selected_metric_group_names':list(GROUPS[:2]),
        'target_formula':'max(gamma*max(c_i(x),0),1/1000000) for metric rows; original target otherwise',
        'floor_units':'original c_plus/c_minus Schur metric rows, not eta tolerance',
        'actual_same_trial_c_y_not_shifted_or_relabelled':True,
        'same_primary_LP_arc_path_other_rows_box_cap_and_curvature_retention':True,
        'same_total_LP_value_and_active_time_limits':True,
        'actual_acceptance_metric_budget_and_all_tolerances_unchanged':True,
        'not_already_an_actual_metric_improvement_or_target55_success':True,
        'original_failed_points_not_promoted_or_relabelled':True}
    locations={}
    for d in [prior['final_doubled_constraints']]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('eighteenth fine metric location not finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    learned={'schema':'eighteenth-SOC-complete-retained-two-pools-v1','source_run':prior.get('github_run_id'),
        'source_commit':prior.get('github_sha'),'source_coarse_rows':len(ci),'source_coarse_row_indices_sha256':digest(ci),
        'source_fine_rows':len(fi),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'all_preceding_coarse_and_fine_rows_retained':True}
    retained={'source_run':prior.get('github_run_id'),'source_commit':prior.get('github_sha'),'status':stage['status'],
        'completed_targets_exact':stage.get('completed_targets_exact'),'unfinished_active_target_exact':stage.get('active_stage_target_exact'),
        'published_final_coarse_decision':copy.deepcopy(prior['final_full_grid_constraints']),
        'published_final_fine_decision':copy.deepcopy(prior['final_doubled_constraints']),
        'old_arc_success_and_rejected_trials_not_recomputed_or_relabelled':True}
    replay={'schema':'eighteen-input-SOC-metric-row-reserve-replay-v1','seventeen_input_replay':old_replay,
        'canonical_physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),'physical_parameter_count':problem.nunknown,
        'same_full_saved_accepted_coefficients':True,'same_complete_g_b0_space_and_two_value_grids':True,
        'learned_pool':learned,'completed_arc_attempt_retained':retained,
        'primary_scale_inheritance':copy.deepcopy(prior['primary_scale_inheritance']),
        'SOC_metric_row_reserve':evidence,
        'SOC_parabolic_backtracking':copy.deepcopy(prior['SOC_parabolic_backtracking']),
        'known_fine_metric_locations':list(locations.values()),'new_SOC_metric_row_reserve_policy':POLICY,
        'old_optimizer_calls_replayed':0,'no_research_geometry_during_structural_replay':True}
    return (problem,state,gate,lower,upper,source_cfg,configuration(old_cfg)),replay,np.asarray(ci,np.int64),np.asarray(fi,np.int64)


def prepare_run(args,*,artificial=False,process_started=None):
    start=time.monotonic(); process_started=start if process_started is None else process_started
    phase='seventeen-input-prior-SOC-start-replay'; bindings={}
    try:
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),[getattr(args,x) for x in INPUTS])
        old=previous.prepare_run(args,artificial=artificial,process_started=process_started)
        bindings=copy.deepcopy(old[1]); phase='eighteenth-SOC-arc-byte-binding'
        if args.soc_arc_audit is None or args.expected_soc_arc_sha256 is None:
            raise ValueError('eighteenth complete SOC arc report and expected SHA are required')
        prior,raw,binding=read_input(args.soc_arc_audit,args.expected_soc_arc_sha256)
        phase='eighteenth-SOC-arc-accepted-state-and-full-pool-replay'
        restored,replay,coarse,fine=replay_arc_success(old,prior,artificial=artificial)
        bindings['completed_soc_arc']=binding
        return restored,bindings,old[2],replay,coarse,fine
    except Exception as error:
        failure={'schema':SCHEMA,'status':'input-replay-failed-before-metric-reserve-geometry','phase':phase,
            'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,'artificial_inputs_only':bool(artificial),
            'old_optimizer_calls_this_run':0,'new_solver_calls':0,'prepare_elapsed_seconds':time.monotonic()-start,
            'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out,failure); raise


def small_summary(report,out):
    result=previous.small_summary(report,out)
    for key in ['completed_arc_attempt_retained','SOC_metric_row_reserve']:
        if key in report:
            result[key]={k:copy.deepcopy(v) for k,v in report[key].items() if not k.startswith('published_final_')}
    stage=report.get('mixed_grid_short_step_stage',{})
    table=result.get('mixed_grid_short_step_stage',{}).get('correction_table')
    if table is not None:
        extra=['metric_selected_row_count','metric_selected_rows_lifted_to_floor',
            'minimum_metric_target_evaluated','maximum_metric_target_increment_evaluated',
            'minimum_corrected_linear_metric_margin','minimum_corrected_linear_metric_margin_minus_floor']
        table['columns'].extend(extra)
        corrections=[c for m in stage.get('solver',{}).get('models',[]) for c in m.get('corrections',[])]
        for row,correction in zip(table['rows'],corrections,strict=True):
            reserve=correction.get('linear_program',{}).get('metric_row_reserve',{})
            row.extend(reserve.get(k) for k in extra)
    return result


def save_report(out,report):
    atomic_save(out,report); path=summary_path(out); tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


def run_audit(prepared,out,*,artificial=False,evaluate_only=False,process_started=None,prepare_seconds=0.):
    restored,bindings,tenth,replay,learned_coarse,learned_fine=prepared
    problem,initial,gate,lower,upper,source_cfg,cfg=restored
    started=time.monotonic(); process_started=started if process_started is None else process_started
    metric=copy.deepcopy(problem.metric_model(initial)); b0=copy.deepcopy(problem.height_base_definition)
    scale=float(Q(cfg['curvature_scale_exact'])); initial_target=float(Q(cfg['curvature_target_schedule_exact'][0]))
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,'github_sha':os.environ.get('GITHUB_SHA'),
        'github_run_id':os.environ.get('GITHUB_RUN_ID'),'github_repository':os.environ.get('GITHUB_REPOSITORY'),
        'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,
        'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':state_record(problem,initial),'unchanged_complete_metric_and_height_reference':True,
        'process_clock_scope':'main includes eighteen-input loader; initialization and active metric-reserve SOC separately recorded',
        'prepare_elapsed_seconds':prepare_seconds,'learned_pool_replay':replay['learned_pool'],
        'completed_arc_attempt_retained':replay['completed_arc_attempt_retained'],
        'primary_scale_inheritance':replay['primary_scale_inheritance'],
        'SOC_parabolic_backtracking':replay['SOC_parabolic_backtracking'],
        'SOC_metric_row_reserve':replay['SOC_metric_row_reserve'],
        'curvature_target_ladder_definition':{'targets_exact':list(TARGETS),'success_only_advance':True,
            'one_shared_LP_limit':cfg['max_linear_models'],'one_shared_value_limit':cfg['max_physical_evaluations'],
            'one_shared_active_seconds':cfg['max_seconds'],'targets_not_physical_coefficients':True,
            'prior_target60_and_unfinished55_kept_as_history':True,
            'final16_is_sampled_local_curvature_only':True,'reach_design_tau_exact':cfg['curvature_target_radius_exact']},
        'SOC_definition':{'policy':cfg['SOC_policy'],'parabolic_backtracking_policy':cfg['SOC_parabolic_backtracking_policy'],
            'metric_row_reserve_policy':POLICY,'metric_row_floor_exact':FLOOR,'at_most_one_correction_LP_per_primary_model':True,
            'objective':'minimize normalized correction L1 norm inside half actual primary infinity-norm radius',
            'physical_margin_retention_exact':cfg['SOC_physical_margin_retention_exact'],
            'predicted_descent_retention_exact':cfg['SOC_predicted_descent_retention_exact'],
            'maximum_relative_correction_exact':cfg['SOC_maximum_correction_relative_to_proposed_step_exact'],
            'trial_residuals_must_be_actual_same_state_on_both_complete_grids':True,
            'all_original_physical_gates_and_true_curvature_decrease_required_after_correction':True,
            'no_new_free_physical_parameters_or_metric_design':True}}
    def save(status):
        now=time.monotonic()
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=report.get('mixed_grid_short_step_stage',{}).get('checkpoint',{}).get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('eighteen-inputs-replayed-before-metric-reserve-SOC-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth); order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid; report['phase']='one-two-grid-SOC-initialization'
        def checkpoint(snapshot):
            report['mixed_grid_short_step_stage']={'status':'current-SOC-two-grid-checkpoint','checkpoint':snapshot,'solver':{}}
            save('SOC-two-grid-physical-checkpoint')
        objective=MetricReserveObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            eighteenth_report_decoded_sha256=bindings['completed_soc_arc']['decoded_sha256'],
            primary_scale_inheritance=replay['primary_scale_inheritance'],
            SOC_parabolic_backtracking=replay['SOC_parabolic_backtracking'],
            SOC_metric_row_reserve=replay['SOC_metric_row_reserve'],
            learned_pool_replay=replay['learned_pool'],old_metric_delta_and_old_curvature_targets_are_preserved_history=True)
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(learned_coarse,{'kind':'all-eighteenth-learned-coarse-rows-retained','source':replay['learned_pool']})
        objective.set_fine_pool(learned_fine,{'kind':'all-eighteenth-learned-fine-rows-retained','source':replay['learned_pool']})
        first=objective.evaluate(np.r_[initial,initial_target/scale])
        report['initial_current_constraints']=copy.deepcopy(first['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        save('complete-metric-reserve-initial-two-grid-diagnostics-target55-not-assumed-feasible')
        report['phase']='shared-budget-primary-and-SOC-LPs-with-two-grid-acceptance'
        stage=run_soc_metric_reserve_steps(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['mixed_grid_short_step_stage']=stage
        point=stage['checkpoint'].get('selected_two_grid_physical_point')
        if point is None:
            save('no-two-grid-physical-baseline-eligible'); return report
        final=np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if coefficients(final)!=point['exact_binary64_physical_coefficients'] or digest(problem.identity(final))!=point['physical_state_sha256']:
            raise ValueError('SOC selected full coefficients or physical identity differs')
        identity=problem.identity(final); frozen,fc=problem.frozen_metric_copy(final)
        if (fc.tobytes()!=final.tobytes() or frozen.identity(fc)!=identity or frozen.metric_model(fc)!=metric
                or frozen.height_base_definition!=b0):
            raise ArithmeticError('SOC final freeze changed g/b0/coefficients or the physical field')
        problem,final=frozen,fc; report['final_state']=state_record(problem,final)
        final_target=float(Q(stage['active_stage_target_exact'])); zeta=final_target/scale
        report['phase']='independent-final-same-state-original-two-grid-values'
        work=problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit']=audit_data(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints']=candidate_decision(problem,gate,final,zeta,work,lower,upper,cfg)
        save('last-SOC-accepted-state-recomputed-on-original-coarse-grid')
        del objective
        fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
        fine=problem.geometry(final,radial,fine_theta,order)
        report['final_doubled_angle_audit']=audit_data(problem,final,fine,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints']=candidate_decision(problem,gate,final,zeta,fine,lower,upper,cfg)
        report['same_parameter_Pi_refinement']=compare_data(problem,work,problem,fine,final,
            name='one SOC-accepted physical field, unchanged parameters and target between final angle grids',theta_stride=2)
        if problem.identity(final)!=identity:
            raise ArithmeticError('SOC independent final refinement changed physical identity')
        cd,fd=report['final_full_grid_constraints'],report['final_doubled_constraints']
        eligible=bool(cd['eligible_under_fixed_metric_and_physical_gates'] and fd['eligible_under_fixed_metric_and_physical_gates'])
        maximum=max(cd['direct_maximum_absolute_principal_curvature'],fd['direct_maximum_absolute_principal_curvature'])
        start_max=max(report['initial_current_constraints']['direct_maximum_absolute_principal_curvature'],
            report['initial_doubled_constraints']['direct_maximum_absolute_principal_curvature'])
        achieved=[x for x in TARGETS if eligible and maximum<=float(Q(x))+cfg['direct_curvature_tolerance']]
        report['final_selection_validation']={'both_value_grids_physical_gate_pass':eligible,
            'both_grid_maximum_curvature':maximum,'initial_both_grid_maximum_curvature':start_max,
            'actual_curvature_decrease':start_max-maximum,'last_active_target_exact':stage['active_stage_target_exact'],
            'last_active_target_reached':bool(eligible and maximum<=final_target+cfg['direct_curvature_tolerance']),
            'targets_reached_by_independent_final_values_exact':achieved,'all_schedule_targets_reached':len(achieved)==len(TARGETS),
            'whole_surface_reach_not_certified':True,'new_failure_not_promoted_to_accepted_physical_state':True}
        count=stage['checkpoint']['total_full_value_physical_evaluations']
        report['value_evaluation_counts']={'initialization_primary_and_corrected_coarse_plus_fine_within_shared_cap':count,
            'shared_cap':cfg['max_physical_evaluations'],'independent_final_same_state_value_calls':2,
            'total_counted_full_value_calls_in_this_driver':count+2,
            'fine_at_coarse_ineligible_trial_for_SOC_consumes_shared_cap':True,
            'failed_fine_attempts_consume_shared_cap':True,'Jacobian_batch_calls_recorded_separately':True,
            'exact_same_state_saved_cache_restores_do_not_repeat_geometry':True,'no_final_optimizer_or_step':True}
        report['limitations']={'all_value_gates_and_curvature_diagnostics_sampled_only':True,
            'metric_budget_167_over_625_is_not_exact_isometry':True,
            'target16_below_1000_over_61_does_not_pay_nonlocal_reach':True,
            'SOC_linear_model_and_curve_not_true_feasibility_or_true_curvature_descent':True,
            'partial_target_progress_not_all_targets_completed':True,'rejected_trials_not_warm_starts':True,
            'curvature_and_mirror_pairs_not_all_surface_pairs':True,'no_complete_embedding_or_reach_certificate':True,
            'no_old_optimizer_replayed':True}
        save('complete-two-grid-SOC-metric-reserve-curvature-audit' if eligible
             else 'final-same-state-value-recheck-failed-do-not-use-as-new-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('SOC-metric-reserve-audit-error-checkpoints-preserved'); return report


def artificial_eighteen_inputs(directory):
    """Small declared artificial predecessor IO only; no old checks/solve."""
    args,unused,unused_prior=previous.artificial_seventeen_inputs(directory)
    args.out=directory/'completed-artificial-soc-arc.json'
    prepared=previous.prepare_run(args,artificial=True)
    report=previous.run_audit(prepared,args.out,artificial=True,evaluate_only=True)
    if report['status']!='complete-two-grid-SOC-parabolic-backtracking-curvature-audit':
        raise ArithmeticError('artificial arc predecessor failed')
    args.soc_arc_audit=args.out
    args.expected_soc_arc_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    return args,prepared,report


def developer_check():
    targeted=reserve_developer_check()
    with tempfile.TemporaryDirectory(prefix='SOC-metric-reserve-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder); args,old_prepared,prior=artificial_eighteen_inputs(directory)
        args.out=directory/'metric-reserve-artificial.json'; start=time.monotonic()
        prepared=prepare_run(args,artificial=True,process_started=start)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=start,prepare_seconds=time.monotonic()-start)
        stage=report.get('mixed_grid_short_step_stage',{}); snap=stage.get('checkpoint',{})
        old=prior['mixed_grid_short_step_stage']['checkpoint']
        pools_kept=all(set(old[name][-1]['row_indices']).issubset(snap.get(name,[{}])[0].get('row_indices',[]))
            for name in ['active_row_pool_history','fine_physical_row_pool_history'])
        same=report.get('final_state')==prior['final_state']
        no_lp=stage.get('solver',{}).get('linear_program_invocation_count')==0
        label=snap.get('selected_two_grid_physical_point',{}).get('reason',{}).get('kind')==\
            'saved-6ba089-arc-two-grid-success-metric-reserve-start'
        summary=json.loads(summary_path(args.out).read_text()); summary_bytes=summary_path(args.out).stat().st_size
        bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args); wrong.out=directory/'wrong-eighteenth-SHA.json'; wrong.expected_soc_arc_sha256='0'*64
        try:
            prepare_run(wrong,artificial=True); wrong_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text())
            wrong_sha=failure['phase']=='eighteenth-SOC-arc-byte-binding' and failure['new_solver_calls']==0
        bad=copy.deepcopy(prior)
        bad['mixed_grid_short_step_stage']['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
        try:replay_arc_success(old_prepared,bad,artificial=True); wrong_state=False
        except ValueError:wrong_state=True
        bad=copy.deepcopy(prior)
        fp=bad['mixed_grid_short_step_stage']['checkpoint']['fine_physical_row_pool_history'][-1]
        first=fp['row_indices'][0]; rr,tt,unused=curvature_grid(old_prepared[2])
        fp['added_row_indices']=[first]
        fp['added_original_grid_coordinates']=fine_row_coordinates([first],rr,np.arange(2*len(tt))*np.pi/len(tt))
        fp['added_original_grid_coordinates'][0]['theta']=123.
        try:replay_arc_success(old_prepared,bad,artificial=True); wrong_coordinate=False
        except ValueError:wrong_coordinate=True

        # Output-only stress, deliberately above the joint LP budget. No extra
        # geometry or optimizer: preserve the new exact curve metadata too.
        worst=copy.deepcopy(report); ws=worst['mixed_grid_short_step_stage']; wc=ws['checkpoint']
        sample=copy.deepcopy(wc['selected_two_grid_physical_point'])
        ws['solver']['models']=[]; ws['solver'].update(primary_LP_invocation_count=12,correction_LP_invocation_count=12)
        expected=[]
        lp=targeted['toy_correction_report']
        for mi in range(12):
            target=TARGETS[min(mi,len(TARGETS)-1)]
            model={'number':mi+1,'stage_index':min(mi,len(TARGETS)-1),'fixed_stage_target_exact':target,
                'linearized_at_accepted_index':mi,'coarse_pool_rows':4208+mi,'fine_pool_rows':1176+mi,
                'linear_program':copy.deepcopy(lp),'result':'artificial-metric-reserve-output-fixture','trials':[],
                'corrections':[{'primary_trial_index':0,'primary_trial_physical_sha256':sample['physical_state_sha256'],
                    'coarse_residual_evaluation':mi+2,'fine_residual_evaluation':mi+3,
                    'coarse_pool_version':mi+1,'fine_pool_version':mi+2,'linear_program':copy.deepcopy(lp),
                    'exact_binary64_correction':['1/16','-1/32']} ]}
            for ti in range(7):
                alpha=Q(1,2**max(0,ti-1)); curve=None
                kind='primary-short-step' if ti==0 else 'SOC-corrected-short-step' if ti==1 else 'SOC-parabolic-backtrack'
                if ti>=2:
                    curve={'reference_primary_alpha_exact':'1','curve_fraction_exact':str(alpha),
                        'correction_weight_exact':str(alpha**2),'linear_curvature_slack_upper_bound':.02/(1+ti)}
                trial={'kind':kind,'stage_index':min(mi,len(TARGETS)-1),'target_exact':target,'alpha_exact':str(alpha),
                    'attempt_status':'coarse-value-call-complete','accepted_as_next_iterate':ti==6,
                    'accepted_index':mi+1 if ti==6 else None,'coarse_physical_evaluation':2+7*mi+ti,
                    'fine_value_evaluation':2+7*mi+ti,'coarse_decision':copy.deepcopy(sample['coarse']),
                    'fine_decision':copy.deepcopy(sample['fine']),'coarse_omitted_rows':mi,'new_coarse_rows':mi,
                    'fine_omitted_rows':ti,'new_fine_rows':ti,'fine_violation_groups':{n:mi+ti+j for j,n in enumerate(FINE_GROUPS)},
                    'actual_fine_residual_was_evaluated_even_if_coarse_ineligible':ti==0,
                    'exact_binary64_physical_coefficients':sample['exact_binary64_physical_coefficients']}
                if curve is not None:trial['parabolic_curve']=curve
                model['trials'].append(trial)
                expected.append((mi+1,ti,kind,str(alpha),None if curve is None else curve['correction_weight_exact']))
            ws['solver']['models'].append(model)
        wc['stage_events']=[]
        for i,target in enumerate(TARGETS):
            for kind in ['stage-start','stage-complete']:
                wc['stage_events'].append({'kind':kind,'stage_index':i,'target_exact':target,
                    'physical_state_sha256':sample['physical_state_sha256'],'total_LPs_so_far':i+1,
                    'combined_value_evaluations':2+2*i,'optimization_elapsed_seconds':3.+i,
                    'coarse':copy.deepcopy(sample['coarse']),'fine':copy.deepcopy(sample['fine'])})
        wc['accepted_iterates']=[]
        for i in range(13):
            point=copy.deepcopy(sample); point['accepted_index']=i
            point['reason']={'kind':'artificial-metric-reserve-output-fixture','model':i}; wc['accepted_iterates'].append(point)
        sp=directory/'metric-reserve-maximum-summary-artificial.json'; save_report(sp,worst)
        stress=json.loads(summary_path(sp).read_text()); stress_bytes=summary_path(sp).stat().st_size
        table=stress['mixed_grid_short_step_stage']['trial_table']
        rows=[dict(zip(table['columns'],row,strict=True)) for row in table['rows']]
        actual=[(r['model_number'],r['trial_index'],r['kind'],r['alpha_exact'],r['correction_weight_exact']) for r in rows]
        tables=actual==expected
        reserve_table=stress['mixed_grid_short_step_stage']['correction_table']
        reserve_rows=[dict(zip(reserve_table['columns'],r,strict=True)) for r in reserve_table['rows']]
        reserve_roundtrip=all(r['minimum_metric_target_evaluated']==1e-6 and
            r['metric_selected_rows_lifted_to_floor']==1 for r in reserve_rows) and len(reserve_rows)==12
        stress_bound=stress['full_report']['sha256']==hashlib.sha256(sp.read_bytes()).hexdigest() and json.loads(sp.read_text())==worst
        status=report['status']; error=report.get('error'); refinement=report.get('same_parameter_Pi_refinement')
        sources=report.get('source_files_sha256')==implementation_hashes()
    passed=bool(targeted['passed'] and pools_kept and same and no_lp and label and bound and summary_bytes<95000
        and wrong_sha and wrong_state and wrong_coordinate and tables and stress_bound and stress_bytes<95000
        and reserve_roundtrip and sources and status=='complete-two-grid-SOC-metric-reserve-curvature-audit')
    return {'schema':'SOC-metric-reserve-eighteen-input-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,'no_Actions_environment_forged':True,
        'new_RHS_targeted_check':targeted,'full_main_status':status,'full_main_error':error,
        'same_complete_state_g_b0_and_freeze':same,'all_prior_coarse_and_fine_rows_retained':pools_kept,
        'artificial_full_main_has_no_LP':no_lp,'initial_provenance_names_saved_source':label,
        'summary_binds_complete_report':bound,'summary_bytes':summary_bytes,'source_hashes_match':sources,
        'wrong_eighteenth_SHA_saves_failure':wrong_sha,'changed_full_coefficients_rejected':wrong_state,
        'changed_original_fine_coordinate_rejected':wrong_coordinate,
        'conservative_output_stress_counts':{'primary_models':12,'correction_LPs':12,'trials':84,'events':18,'accepted_points':13},
        'stress_summary_bytes':stress_bytes,'all_new_curve_trial_fields_roundtrip':tables,'all_new_metric_reserve_fields_roundtrip':reserve_roundtrip,
        'stress_complete_report_unchanged_and_byte_bound':stress_bound,'same_state_angle_refinement':refinement,'passed':passed}


def main():
    process_started=time.monotonic(); parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true'); parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'SOC-metric-reserve-development-error-v1','passed':False,'artificial_inputs_only':True,
                'source_files_sha256':implementation_hashes(),'process_total_elapsed_seconds':time.monotonic()-process_started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(),process_total_elapsed_seconds=time.monotonic()-process_started)
        atomic_save(args.out,result); print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    before=time.monotonic()
    try:prepared=prepare_run(args,process_started=process_started)
    except Exception:raise SystemExit(1)
    report=run_audit(prepared,args.out,process_started=process_started,prepare_seconds=time.monotonic()-before)
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)
    if report['status']!='complete-two-grid-SOC-metric-reserve-curvature-audit':raise SystemExit(1)


if __name__=='__main__':main()


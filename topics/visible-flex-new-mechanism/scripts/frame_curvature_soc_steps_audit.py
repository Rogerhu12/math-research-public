#!/usr/bin/env python3
"""One bounded-SOC continuation from the published two-grid target-65 state.

Fifteen reports are byte-bound; no old optimizer is replayed. Both primary and
correction LPs share the original budget. Actual geometry remains Actions-only.
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
import frame_curvature_target_ladder_audit as previous
from frame_curvature_soc_steps import (SOCObjective, configuration, run_soc_steps,
    developer_check as soc_check, implementation_hashes as soc_hashes, POLICY, TARGETS)

SCHEMA='same-g-two-grid-bounded-SOC-curvature-audit-v1'
PRIOR_RUN='43658064177'
PRIOR_SOURCE='bf3497f2333127f93bd5150c3fe7279dad3225f3'
PRIOR_FINAL_PHYSICAL_SHA='d1ca5fa0be2942c7f1537ac72fc6d20c42944443059ed5e237361c0d334abf13'
coefficients=previous.coefficients
curvature_grid=previous.curvature_grid
summary_path=previous.summary_path


def implementation_hashes():
    result=previous.implementation_hashes(); result.update(soc_hashes())
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def replay_ladder_success(prepared,prior,*,artificial=False):
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prior.get('schema')!=previous.SCHEMA
            or prior.get('status')!='complete-two-grid-curvature-target-ladder-audit'
            or bool(prior.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('a matching completed fifteenth target-ladder report is required')
    if prior.get('source_files_sha256')!=previous.implementation_hashes() or prior.get('configuration')!=old_cfg:
        raise ValueError('fifteenth frozen source/configuration binding differs')
    if not artificial and (str(prior.get('github_run_id'))!=PRIOR_RUN or prior.get('github_sha')!=PRIOR_SOURCE):
        raise ValueError('fifteenth source/run differs')
    for name,binding in bindings.items():
        recorded=prior.get('exact_input_storage',{}).get(name,{})
        for key in ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']:
            if recorded.get(key)!=binding.get(key):
                raise ValueError('fifteenth input byte binding differs: '+name+'/'+key)
    if (prior.get('initial_state')!=state_record(problem,old_initial)
            or prior.get('input_replay')!=old_replay or prior.get('old_optimizer_calls_this_run')!=0
            or not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_failed_metric_auxiliary_delta')!=tenth['selected_raw_auxiliary_delta']):
        raise ValueError('fifteenth original physical state, replay or preserved history differs')
    stage=prior['mixed_grid_short_step_stage']; snap=stage['checkpoint']
    point=snap.get('selected_two_grid_physical_point')
    if not point:
        raise ValueError('fifteenth complete two-grid accepted coefficients are missing')
    state=np.asarray(point.get('physical_parameter_coefficients_binary64'),float)
    if (state.shape!=(problem.nunknown,) or not np.all(np.isfinite(state))
            or coefficients(state)!=point.get('exact_binary64_physical_coefficients')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prior.get('final_state')!=state_record(problem,state)):
        raise ValueError('fifteenth full coefficients, exact rationals or canonical state differ')
    if not artificial and point['physical_state_sha256']!=PRIOR_FINAL_PHYSICAL_SHA:
        raise ValueError('real SOC continuation must start from the saved d1ca5f state')
    accepted=snap.get('accepted_iterates',[])
    if not accepted or accepted[-1]!=point or problem.metric_model(state)!=problem.metric_model(old_initial):
        raise ValueError('fifteenth selected state is not the last accepted fixed-g point')
    validation=prior.get('final_selection_validation',{})
    if not validation.get('both_value_grids_physical_gate_pass'):
        raise ValueError('fifteenth independent final two-grid validation failed')
    if not artificial and (stage.get('completed_targets_exact')!=['65']
            or stage.get('active_stage_target_exact')!='60'
            or validation.get('last_active_target_reached') is not False):
        raise ValueError('the saved history must retain target65 success and target60 not yet attained')
    for key in ['final_full_grid_constraints','final_doubled_constraints']:
        decision=prior.get(key,{})
        if not decision.get('eligible_under_fixed_metric_and_physical_gates'):
            raise ValueError('fifteenth physical decision failed')
        for field in ['fixed_metric_budget_exact','hard_strip_half_width_exact','mirror_target_exact']:
            if decision.get(field)!=old_cfg[field]:
                raise ValueError('fifteenth physical gate definition differs: '+field)
    radial,theta,grid=curvature_grid(tenth)
    if prior.get('full_value_sampling_definition')!=grid:
        raise ValueError('fifteenth original complete value grid differs')
    history=snap.get('active_row_pool_history',[]); fhistory=snap.get('fine_physical_row_pool_history',[])
    if not history or not fhistory:
        raise ValueError('fifteenth complete learned coarse and fine pools are required')
    coarse,fine=history[-1],fhistory[-1]; ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,groups,total,rule,cap in [
        (coarse,ci,list(GROUPS),len(GROUPS)*len(radial)*len(theta),
         'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows']),
        (fine,fi,list(FINE_GROUPS),len(FINE_GROUPS)*len(radial)*2*len(theta),
         'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'])]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=groups
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap):
            raise ValueError('fifteenth learned original row indices/shape/hash differ')
    if not set(old_coarse).issubset(ci) or not set(old_fine).issubset(fi):
        raise ValueError('fifteenth learned pool lost a preceding row')
    added=fine.get('added_row_indices'); ft=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added)
            or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=fine_row_coordinates(added,radial,ft)):
        raise ValueError('fifteenth fine-row original angular/radial pairing differs')
    locations={}
    for d in [prior['final_doubled_constraints']]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):
                raise ValueError('fifteenth fine peak location is not finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    learned={'schema':'fifteenth-target-ladder-retained-two-pools-v1','source_run':prior.get('github_run_id'),
        'source_commit':prior.get('github_sha'),'source_coarse_rows':len(ci),'source_coarse_row_indices_sha256':digest(ci),
        'source_fine_rows':len(fi),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'all_preceding_coarse_and_fine_rows_retained':True}
    retained={'source_run':prior.get('github_run_id'),'source_commit':prior.get('github_sha'),
        'status':stage['status'],'completed_targets_exact':stage.get('completed_targets_exact'),
        'unfinished_active_target_exact':stage.get('active_stage_target_exact'),
        'published_final_coarse_decision':copy.deepcopy(prior['final_full_grid_constraints']),
        'published_final_fine_decision':copy.deepcopy(prior['final_doubled_constraints']),
        'old_target_ladder_not_recomputed_or_relabelled':True}
    replay={'schema':'fifteen-input-SOC-complete-accepted-replay-v1','fourteen_input_replay':old_replay,
        'canonical_physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),'physical_parameter_count':problem.nunknown,
        'same_full_saved_accepted_coefficients':True,'same_complete_g_b0_space_and_two_value_grids':True,
        'learned_pool':learned,'completed_target_ladder_attempt_retained':retained,
        'known_fine_metric_locations':list(locations.values()),'new_SOC_policy':POLICY,
        'old_optimizer_calls_replayed':0,'no_research_geometry_during_structural_replay':True}
    return (problem,state,gate,lower,upper,source_cfg,configuration(old_cfg)),replay,np.asarray(ci,np.int64),np.asarray(fi,np.int64)


def prepare_run(args,*,artificial=False,process_started=None):
    start=time.monotonic(); process_started=start if process_started is None else process_started
    phase='fourteen-input-prior-accepted-replay'; bindings={}
    try:
        if not artificial:
            paths=[getattr(args,name) for name in INPUTS]
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        old=previous.prepare_run(args,artificial=artificial,process_started=process_started)
        bindings=copy.deepcopy(old[1]); phase='fifteenth-target-ladder-byte-binding'
        if args.target_ladder_audit is None or args.expected_target_ladder_sha256 is None:
            raise ValueError('fifteenth completed report and expected decoded SHA are required')
        prior,raw,binding=read_input(args.target_ladder_audit,args.expected_target_ladder_sha256)
        phase='fifteenth-complete-accepted-state-and-retained-pool-replay'
        restored,replay,coarse,fine=replay_ladder_success(old,prior,artificial=artificial)
        bindings['completed_target_ladder']=binding
        return restored,bindings,old[2],replay,coarse,fine
    except Exception as error:
        failure={'schema':SCHEMA,'status':'input-replay-failed-before-SOC-geometry','phase':phase,
            'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-start,'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out,failure)
        raise


def small_summary(report,out):
    result=previous.small_summary(report,out)
    for key in ['SOC_definition','completed_target_ladder_attempt_retained']:
        if key in report:
            result[key]={k:copy.deepcopy(v) for k,v in report[key].items() if not k.startswith('published_final_')}
    stage=report.get('mixed_grid_short_step_stage')
    if not stage:return result
    output=result['mixed_grid_short_step_stage']; snap=stage['checkpoint']; item=output['checkpoint']
    for key in ['primary_LP_invocation_count','correction_LP_invocation_count',
                'max_linear_programs_total','shared_max_physical_evaluations',
                'no_budget_reset_between_stages_or_corrections']:
        output[key]=stage.get('solver',{}).get(key)
    table=output['trial_table']; table['columns']+=['kind','fine_read_even_if_coarse_ineligible']
    trials=[r for m in stage.get('solver',{}).get('models',[]) for r in m.get('trials',[])]
    for row,trial in zip(table['rows'],trials,strict=True):
        row.extend([trial.get('kind'),trial.get('actual_fine_residual_was_evaluated_even_if_coarse_ineligible')])
    columns=['model_number','correction_index','primary_trial_index','primary_trial_physical_sha256',
        'coarse_residual_evaluation','fine_residual_evaluation','coarse_pool_version','fine_pool_version',
        'LP_invoked','success','status','message','nit','seconds','rows','variables','matrix_bytes',
        'primary_norm','correction_radius','correction_norm','correction_l1','maximum_absolute_correction',
        'initial_slack','primary_predicted_slack','primary_improvement','retained_fraction',
        'slack_budget','corrected_predicted_slack','corrected_predicted_improvement',
        'physical_linearization_error_min','linear_row_violation','linear_bound_violation','affine_cap_margin',
        'rejected_before_LP','rejected_before_geometry']
    rows=[]
    for model in stage.get('solver',{}).get('models',[]):
        for i,correction in enumerate(model.get('corrections',[])):
            lp=correction['linear_program']
            rows.append([model['number'],i,correction.get('primary_trial_index'),correction.get('primary_trial_physical_sha256'),
                correction.get('coarse_residual_evaluation'),correction.get('fine_residual_evaluation'),
                correction.get('coarse_pool_version'),correction.get('fine_pool_version'),
                lp.get('LP_invoked'),lp.get('success'),lp.get('status'),lp.get('message'),lp.get('nit'),lp.get('elapsed_seconds'),
                lp.get('rows'),lp.get('variables'),lp.get('matrix_bytes'),lp.get('primary_box_normalized_step_infinity_norm'),
                lp.get('maximum_box_normalized_correction_infinity_norm'),lp.get('correction_box_normalized_infinity_norm'),
                lp.get('correction_box_normalized_l1_norm'),lp.get('maximum_absolute_correction'),
                lp.get('initial_curvature_slack'),lp.get('primary_predicted_curvature_slack'),
                lp.get('primary_predicted_slack_improvement'),lp.get('retained_fraction_of_primary_predicted_descent'),
                lp.get('curvature_slack_budget'),lp.get('corrected_predicted_curvature_slack'),
                lp.get('corrected_predicted_slack_improvement'),lp.get('selected_physical_linearization_error_minimum'),
                lp.get('maximum_linear_row_violation'),lp.get('maximum_linear_bound_violation'),lp.get('corrected_affine_cap_margin'),
                lp.get('proposal_rejected_before_LP'),lp.get('proposal_rejected_before_geometry')])
    output['correction_table']={'columns':columns,'rows':rows}
    et=item['stage_event_table']; et['columns'].append('total_LPs_so_far')
    for row,event in zip(et['rows'],snap.get('stage_events',[]),strict=True):
        row.append(event.get('total_LPs_so_far'))
    for key in ['accepted_coarse_cache_restores_without_new_geometry',
                'accepted_fine_cache_restores_without_new_geometry','maximum_retained_accepted_cache_array_bytes']:
        item[key]=snap.get(key)
    output['compact_table_semantics']='all primary/SOC model, trial and event rows; full coefficients and omitted details remain in the byte-bound full report'
    return result


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out); tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


INPUTS=['input','anchor_input','short_audit','height_audit','prior_joint_audit','resume_audit',
    'epigraph_audit','trial_audit','dense_audit','exchange_audit','curvature_audit',
    'feasible_curvature_audit','fixed_target_audit','mixed_grid_audit','target_ladder_audit']
SHA_NAMES=['input','anchor','short','height','prior-joint','resume','epigraph','trial','dense',
    'exchange','curvature','feasible-curvature','fixed-target','mixed-grid','target-ladder']


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
        'process_clock_scope':'main includes fifteen-input loader; initialization and active shared-budget SOC separately recorded',
        'prepare_elapsed_seconds':prepare_seconds,'learned_pool_replay':replay['learned_pool'],
        'completed_target_ladder_attempt_retained':replay['completed_target_ladder_attempt_retained'],
        'curvature_target_ladder_definition':{'targets_exact':list(TARGETS),'success_only_advance':True,
            'one_shared_LP_limit':cfg['max_linear_models'],'one_shared_value_limit':cfg['max_physical_evaluations'],
            'one_shared_active_seconds':cfg['max_seconds'],'targets_not_physical_coefficients':True,
            'old_target65_kept_as_completed_history':True,
            'final16_is_sampled_local_curvature_only':True,'reach_design_tau_exact':cfg['curvature_target_radius_exact']},
        'SOC_definition':{'policy':POLICY,'at_most_one_correction_LP_per_primary_model':True,
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
    save('fifteen-inputs-replayed-before-SOC-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth); order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid; report['phase']='one-two-grid-SOC-initialization'
        def checkpoint(snapshot):
            report['mixed_grid_short_step_stage']={'status':'current-SOC-two-grid-checkpoint','checkpoint':snapshot,'solver':{}}
            save('SOC-two-grid-physical-checkpoint')
        objective=SOCObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            fifteenth_report_decoded_sha256=bindings['completed_target_ladder']['decoded_sha256'],
            learned_pool_replay=replay['learned_pool'],old_metric_delta_and_old_curvature_targets_are_preserved_history=True)
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(learned_coarse,{'kind':'all-fifteenth-learned-coarse-rows-retained','source':replay['learned_pool']})
        objective.set_fine_pool(learned_fine,{'kind':'all-fifteenth-learned-fine-rows-retained','source':replay['learned_pool']})
        first=objective.evaluate(np.r_[initial,initial_target/scale])
        report['initial_current_constraints']=copy.deepcopy(first['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        save('complete-SOC-initial-two-grid-diagnostics-target60-not-assumed-feasible')
        report['phase']='shared-budget-primary-and-SOC-LPs-with-two-grid-acceptance'
        stage=run_soc_steps(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
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
            'SOC_linear_model_not_true_feasibility_or_true_curvature_descent':True,
            'partial_target_progress_not_all_targets_completed':True,'rejected_trials_not_warm_starts':True,
            'curvature_and_mirror_pairs_not_all_surface_pairs':True,'no_complete_embedding_or_reach_certificate':True,
            'no_old_optimizer_replayed':True}
        save('complete-two-grid-bounded-SOC-curvature-audit' if eligible
             else 'final-same-state-value-recheck-failed-do-not-use-as-new-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('SOC-curvature-audit-error-checkpoints-preserved'); return report


def developer_check():
    targeted=soc_check()
    with tempfile.TemporaryDirectory(prefix='curvature-SOC-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder); mixed=previous.previous
        args,unused,unused_prior=mixed.artificial_thirteen_inputs(directory)
        args.out=directory/'completed-mixed-artificial.json'
        thirteen=mixed.prepare_run(args,artificial=True)
        mixed_report=mixed.run_audit(thirteen,args.out,artificial=True,evaluate_only=True)
        if mixed_report['status']!='complete-mixed-grid-fixed-target-short-step-audit':
            raise ArithmeticError('artificial fourteenth fixture failed')
        args.mixed_grid_audit=args.out; args.expected_mixed_grid_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'completed-ladder-artificial.json'
        fourteen=previous.prepare_run(args,artificial=True)
        prior=previous.run_audit(fourteen,args.out,artificial=True,evaluate_only=True)
        if prior['status']!='complete-two-grid-curvature-target-ladder-audit':
            raise ArithmeticError('artificial fifteenth fixture failed')
        args.target_ladder_audit=args.out; args.expected_target_ladder_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'SOC-artificial.json'
        before=time.monotonic(); prepared=prepare_run(args,artificial=True,process_started=before)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=before,prepare_seconds=time.monotonic()-before)
        stage=report.get('mixed_grid_short_step_stage',{}); snap=stage.get('checkpoint',{})
        old_snap=prior['mixed_grid_short_step_stage']['checkpoint']
        pools_kept=all(set(old_snap[name][-1]['row_indices']).issubset(snap.get(name,[{}])[0].get('row_indices',[]))
            for name in ['active_row_pool_history','fine_physical_row_pool_history'])
        same=report.get('final_state')==prior['final_state']
        no_lp=stage.get('solver',{}).get('linear_program_invocation_count')==0
        compact=json.loads(summary_path(args.out).read_text()); summary_bytes=summary_path(args.out).stat().st_size
        summary_ok=compact['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args); wrong.out=directory/'wrong-fifteenth-SHA.json'; wrong.expected_target_ladder_sha256='0'*64
        try:
            prepare_run(wrong,artificial=True); bad_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text())
            bad_sha=failure['phase']=='fifteenth-target-ladder-byte-binding' and failure['new_solver_calls']==0
        broken=copy.deepcopy(prior)
        broken['mixed_grid_short_step_stage']['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
        try:
            replay_ladder_success(fourteen,broken,artificial=True); bad_state=False
        except ValueError:
            bad_state=True
        broken=copy.deepcopy(prior)
        fake_pool=broken['mixed_grid_short_step_stage']['checkpoint']['fine_physical_row_pool_history'][-1]
        first_index=fake_pool['row_indices'][0]
        rr,tt,unused_grid=curvature_grid(fourteen[2])
        fake_pool['added_row_indices']=[first_index]
        fake_pool['added_original_grid_coordinates']=fine_row_coordinates([first_index],rr,np.arange(2*len(tt))*np.pi/len(tt))
        fake_pool['added_original_grid_coordinates'][0]['theta']=123.
        try:
            replay_ladder_success(fourteen,broken,artificial=True); bad_coord=False
        except ValueError:
            bad_coord=True
        broken=copy.deepcopy(prior); broken['source_files_sha256'][Path(previous.__file__).name]='0'*64
        try:
            replay_ladder_success(fourteen,broken,artificial=True); bad_source=False
        except ValueError:
            bad_source=True
        # Semantic-output stress only, not extra geometry or optimization. This
        # deliberately exceeds jointly possible LP/trial/event maxima.
        worst=copy.deepcopy(report); ws=worst['mixed_grid_short_step_stage']; wc=ws['checkpoint']
        sample=copy.deepcopy(wc['selected_two_grid_physical_point']); expected_trials=[]; expected_corrections=[]
        ws['solver']['models']=[]; ws['solver'].update(primary_LP_invocation_count=12,correction_LP_invocation_count=12)
        for mi in range(12):
            target=TARGETS[min(mi,len(TARGETS)-1)]; lp=copy.deepcopy(targeted['correction_LP_report'])
            lp.update(elapsed_seconds=.02+mi/100,nit=4+mi,matrix_bytes=14000000+mi)
            model={'number':mi+1,'stage_index':min(mi,9),'fixed_stage_target_exact':target,
                'linearized_at_accepted_index':mi,'coarse_pool_rows':4000+mi,'fine_pool_rows':134+mi,
                'linear_program':lp,'result':'artificial-complete-SOC-output-fixture','trials':[],
                'corrections':[{'primary_trial_index':0,'primary_trial_physical_sha256':sample['physical_state_sha256'],
                    'coarse_residual_evaluation':mi+2,'fine_residual_evaluation':mi+3,
                    'coarse_pool_version':mi+1,'fine_pool_version':mi+2,'linear_program':lp,
                    'exact_binary64_correction':['1/100','-1/200']}]}
            expected_corrections.append((mi+1,0,mi+2,mi+3,lp['matrix_bytes'],lp['curvature_slack_budget']))
            for ti in range(7):
                cd,fd=copy.deepcopy(sample['coarse']),copy.deepcopy(sample['fine'])
                cd.update(direct_max_eta=.267-mi*1e-6-ti*1e-7,direct_maximum_absolute_principal_curvature=63-mi-ti/100)
                fd.update(direct_max_eta=.2671-mi*1e-6-ti*1e-7,direct_maximum_absolute_principal_curvature=63.01-mi-ti/100)
                kind='SOC-corrected-short-step' if ti==1 else 'primary-short-step'
                trial={'kind':kind,'stage_index':min(mi,9),'target_exact':target,'alpha_exact':str(Q(1,2**ti)),
                    'attempt_status':'coarse-value-call-complete','accepted_as_next_iterate':ti==6,
                    'accepted_index':mi+1 if ti==6 else None,'coarse_physical_evaluation':2+7*mi+ti,
                    'fine_value_evaluation':2+7*mi+ti,'coarse_decision':cd,'fine_decision':fd,
                    'coarse_omitted_rows':mi,'new_coarse_rows':mi,'fine_omitted_rows':ti,'new_fine_rows':ti,
                    'fine_violation_groups':{n:mi+ti+j for j,n in enumerate(FINE_GROUPS)},
                    'actual_fine_residual_was_evaluated_even_if_coarse_ineligible':ti==0,
                    'exact_binary64_physical_coefficients':sample['exact_binary64_physical_coefficients']}
                model['trials'].append(trial)
                expected_trials.append((mi+1,ti,kind,trial['alpha_exact'],cd['direct_max_eta'],fd['direct_max_eta'],ti==0))
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
            point['reason']={'kind':'artificial-SOC-output-fixture','model':i}
            wc['accepted_iterates'].append(point)
        stress_path=directory/'SOC-maximum-output-artificial.json'; save_report(stress_path,worst)
        stress=json.loads(summary_path(stress_path).read_text()); stress_bytes=summary_path(stress_path).stat().st_size
        ss=stress['mixed_grid_short_step_stage']; sc=ss['checkpoint']
        def decode(table):return [dict(zip(table['columns'],row,strict=True)) for row in table['rows']]
        actual_trials=[(r['model_number'],r['trial_index'],r['kind'],r['alpha_exact'],r['coarse_max_eta'],r['fine_max_eta'],
            r['fine_read_even_if_coarse_ineligible']) for r in decode(ss['trial_table'])]
        actual_corrections=[(r['model_number'],r['correction_index'],r['coarse_residual_evaluation'],r['fine_residual_evaluation'],
            r['matrix_bytes'],r['slack_budget']) for r in decode(ss['correction_table'])]
        actual_events=[r['total_LPs_so_far'] for r in decode(sc['stage_event_table'])]
        tables=(actual_trials==expected_trials and actual_corrections==expected_corrections
            and actual_events==[i+1 for i in range(len(TARGETS)) for unused in range(2)])
        bound=(stress['full_report']['sha256']==hashlib.sha256(stress_path.read_bytes()).hexdigest()
            and json.loads(stress_path.read_text())==worst)
        status=report['status']; error=report.get('error'); refinement=report.get('same_parameter_Pi_refinement')
        frozen_sources=report.get('source_files_sha256')==implementation_hashes()
    passed=bool(targeted['passed'] and pools_kept and same and no_lp and summary_ok and summary_bytes<95000
        and bad_sha and bad_state and bad_coord and bad_source and stress_bytes<95000 and tables and bound
        and frozen_sources and status=='complete-two-grid-bounded-SOC-curvature-audit')
    return {'schema':'curvature-SOC-fifteen-input-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,'no_Actions_environment_forged':True,
        'targeted_curved_boundary_budget_cache_checks':targeted,'full_main_status':status,'full_main_error':error,
        'same_complete_physical_state_g_b0_and_freeze':same,'both_old_original_row_pools_retained':pools_kept,
        'artificial_full_main_has_no_LP':no_lp,'summary_binds_complete_report':summary_ok,'summary_bytes':summary_bytes,
        'source_hashes_match':frozen_sources,'wrong_fifteenth_SHA_saves_failure':bad_sha,
        'changed_full_coefficients_rejected':bad_state,'changed_fine_original_coordinate_rejected':bad_coord,
        'changed_fifteenth_implementation_rejected':bad_source,
        'conservative_summary_stress_counts':{'primary_models':12,'correction_LPs':12,'trials':84,'events':20,'accepted_points':13},
        'stress_summary_bytes':stress_bytes,'all_SOC_trial_correction_and_event_scalars_roundtrip':tables,
        'stress_complete_report_unchanged_and_byte_bound':bound,'same_state_angle_refinement':refinement,'passed':passed}


def main():
    process_started=time.monotonic(); parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true'); parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:
            result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'curvature-SOC-development-error-v1','passed':False,'artificial_inputs_only':True,
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
    if report['status']!='complete-two-grid-bounded-SOC-curvature-audit':raise SystemExit(1)


if __name__=='__main__':main()

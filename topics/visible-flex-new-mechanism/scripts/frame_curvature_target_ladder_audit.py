#!/usr/bin/env python3
"""One shared-budget curvature target ladder from the saved two-grid 70 success.

Fourteen reports are byte-bound. No previous optimizer is replayed. The new
controller retains every learned coarse/fine row, the same 163-dimensional
physical family, fixed g/b0, and the original two complete acceptance grids.
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
import frame_curvature_mixed_grid_steps_audit as previous
from frame_curvature_target_ladder import (TargetLadderObjective, configuration, run_ladder,
    developer_check as ladder_check, implementation_hashes as ladder_hashes, POLICY, TARGETS)

SCHEMA = 'same-g-two-grid-curvature-target-ladder-audit-v1'
PRIOR_RUN = '43655713308'
PRIOR_SOURCE = 'd21c87a4d9341369a3dee35598ed88fb666cb99d'
PRIOR_FINAL_PHYSICAL_SHA = 'd0d635e1b3f25816951c99ec49042d5d219ba300fe088da747a8e3e0a5fdba58'
coefficients = previous.coefficients
curvature_grid = previous.curvature_grid
summary_path = previous.summary_path


def implementation_hashes():
    result = previous.implementation_hashes()
    result.update(ladder_hashes())
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def replay_mixed_success(prepared, prior, *, artificial=False):
    restored, bindings, tenth, old_replay, old_pool = prepared
    problem, old_initial, gate, lower, upper, source_cfg, old_cfg = restored
    if (prior.get('schema') != previous.SCHEMA
            or prior.get('status') != 'complete-mixed-grid-fixed-target-short-step-audit'
            or bool(prior.get('artificial_inputs_only')) != bool(artificial)):
        raise ValueError('a completed matching mixed-grid two-grid report is required')
    if prior.get('source_files_sha256') != previous.implementation_hashes() or prior.get('configuration') != old_cfg:
        raise ValueError('fourteenth source or configuration differs from the frozen implementation')
    if not artificial and (str(prior.get('github_run_id')) != PRIOR_RUN or prior.get('github_sha') != PRIOR_SOURCE):
        raise ValueError('fourteenth source/run differs')
    for name, binding in bindings.items():
        recorded = prior.get('exact_input_storage', {}).get(name, {})
        for key in ['decoded_sha256', 'decoded_bytes', 'stored_sha256', 'stored_bytes', 'gzip_storage']:
            if recorded.get(key) != binding.get(key):
                raise ValueError('fourteenth preceding input binding differs: '+name+'/'+key)
    if (prior.get('initial_state') != state_record(problem, old_initial)
            or prior.get('input_replay') != old_replay
            or not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_optimizer_calls_this_run') != 0
            or prior.get('old_failed_metric_auxiliary_delta') != tenth['selected_raw_auxiliary_delta']):
        raise ValueError('the original physical family, initial state or old history differs')
    stage = prior['mixed_grid_short_step_stage']; checkpoint = stage['checkpoint']
    point = checkpoint.get('selected_two_grid_physical_point')
    if not point:
        raise ValueError('the fourteenth report has no complete two-grid accepted point')
    state = np.asarray(point.get('physical_parameter_coefficients_binary64'), float)
    if (state.shape != (problem.nunknown,) or not np.all(np.isfinite(state))
            or coefficients(state) != point.get('exact_binary64_physical_coefficients')
            or digest(problem.identity(state)) != point.get('physical_state_sha256')):
        raise ValueError('saved selected full binary64 coefficients, exact rationals or physical identity differs')
    if not artificial and point['physical_state_sha256'] != PRIOR_FINAL_PHYSICAL_SHA:
        raise ValueError('the real ladder must start from the accepted d0d635 point')
    if prior.get('final_state') != state_record(problem, state):
        raise ValueError('fourteenth final canonical state differs from all saved selected coefficients')
    if (problem.metric_model(state) != problem.metric_model(old_initial)
            or not prior.get('final_selection_validation', {}).get('both_value_grids_physical_gate_pass')):
        raise ValueError('fourteenth final state changed g or failed a physical value grid')
    accepted = checkpoint.get('accepted_iterates', [])
    if not accepted or accepted[-1] != point:
        raise ValueError('fourteenth selected point is not its final accepted physical iterate')
    for key in ['final_full_grid_constraints', 'final_doubled_constraints']:
        decision = prior.get(key, {})
        if not decision.get('eligible_under_fixed_metric_and_physical_gates'):
            raise ValueError('fourteenth saved physical decision failed')
        for field in ['fixed_metric_budget_exact', 'hard_strip_half_width_exact', 'mirror_target_exact']:
            if decision.get(field) != old_cfg[field]:
                raise ValueError('a fourteenth physical gate changed: '+field)
    old_target = prior['fixed_curvature_target_definition']['exact']
    if old_target != '70':
        raise ValueError('the preceding declared target must still be 70')
    if not artificial and (not stage.get('fixed_target_reached')
            or not prior.get('final_selection_validation', {}).get('fixed_target_70_reached')):
        raise ValueError('real target 70 success must be recorded without relabeling the old run')
    radial, theta, grid = curvature_grid(tenth)
    if prior.get('full_value_sampling_definition') != grid:
        raise ValueError('fourteenth full value grid differs')
    coarse_history = checkpoint.get('active_row_pool_history', [])
    fine_history = checkpoint.get('fine_physical_row_pool_history', [])
    if not coarse_history or not fine_history:
        raise ValueError('both learned row pools must be present')
    coarse = coarse_history[-1]; ci = coarse.get('row_indices')
    fine = fine_history[-1]; fi = fine.get('row_indices')
    for record, ids, groups, total, rule, capacity in [
        (coarse,ci,list(GROUPS),len(GROUPS)*len(radial)*len(theta),
         'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows']),
        (fine,fi,list(FINE_GROUPS),len(FINE_GROUPS)*len(radial)*2*len(theta),
         'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'])]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or record.get('row_count')!=len(ids)
                or record.get('row_indices_sha256')!=digest(ids) or record.get('group_order')!=groups
                or record.get('total_full_grid_rows')!=total or record.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>capacity):
            raise ValueError('fourteenth coarse/fine pool indices, groups or original coordinates differ')
    if not set(old_pool).issubset(ci):
        raise ValueError('fourteenth coarse pool discarded previously learned rows')
    fine_theta = np.arange(2*len(theta))*np.pi/len(theta)
    added = fine.get('added_row_indices')
    if (not isinstance(added,list) or any(type(i) is not int for i in added)
            or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=fine_row_coordinates(added,radial,fine_theta)):
        raise ValueError('fourteenth fine-pool original radial/angle coordinate binding differs')
    locations = {}
    decisions = [prior['final_doubled_constraints']]
    decisions += [r.get('decision',{}) for r in checkpoint.get('saved_fine_trials',[])
                  if r.get('status')=='complete-doubled-angle-value-call']
    for decision in decisions:
        location = decision.get('direct_max_eta_location')
        if location is not None:
            pair = (float(location['t']),float(location['theta']))
            if not all(np.isfinite(pair)):
                raise ValueError('saved fine metric peak must be finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    learned = {'schema':'fourteenth-mixed-grid-learned-two-pool-v1',
        'source_run':prior.get('github_run_id'),'source_commit':prior.get('github_sha'),
        'source_coarse_rows':len(ci),'source_coarse_row_indices_sha256':digest(ci),
        'source_fine_rows':len(fi),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],
        'all_preceding_coarse_and_fine_rows_retained':True}
    retained = {'source_run':prior.get('github_run_id'),'source_commit':prior.get('github_sha'),
        'status':stage['status'],'old_fixed_target_lambda_exact':old_target,
        'old_fixed_target_reached':bool(stage.get('fixed_target_reached')),
        'published_final_coarse_decision':copy.deepcopy(prior['final_full_grid_constraints']),
        'published_final_fine_decision':copy.deepcopy(prior['final_doubled_constraints']),
        'completed_70_success_is_not_recomputed_or_relabeled':True}
    replay = {'schema':'fourteen-input-target-ladder-complete-accepted-replay-v1',
        'thirteen_input_replay':old_replay,'canonical_physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),'physical_parameter_count':problem.nunknown,
        'same_full_saved_accepted_coefficients':True,'same_complete_g_b0_space_and_two_value_grids':True,
        'learned_pool':learned,'completed_mixed_target_attempt_retained':retained,
        'known_fine_metric_locations':list(locations.values()),'new_target_ladder_policy':POLICY,
        'old_optimizer_calls_replayed':0,'no_research_geometry_during_structural_replay':True}
    return (problem,state,gate,lower,upper,source_cfg,configuration(old_cfg)),replay,np.asarray(ci,np.int64),np.asarray(fi,np.int64)


def prepare_run(args, *, artificial=False, process_started=None):
    start=time.monotonic(); process_started=start if process_started is None else process_started
    phase='thirteen-input-prior-accepted-replay'; bindings={}
    try:
        if not artificial:
            paths=[args.input,args.anchor_input,args.short_audit,args.height_audit,args.prior_joint_audit,
                args.resume_audit,args.epigraph_audit,args.trial_audit,args.dense_audit,args.exchange_audit,
                args.curvature_audit,args.feasible_curvature_audit,args.fixed_target_audit,args.mixed_grid_audit]
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        old=previous.prepare_run(args,artificial=artificial,process_started=process_started)
        bindings=copy.deepcopy(old[1]); phase='fourteenth-mixed-grid-byte-binding'
        if args.mixed_grid_audit is None or args.expected_mixed_grid_sha256 is None:
            raise ValueError('the fourteenth complete report and expected decoded SHA are required')
        prior,raw,binding=read_input(args.mixed_grid_audit,args.expected_mixed_grid_sha256)
        phase='fourteenth-complete-accepted-state-and-both-pool-replay'
        restored,replay,coarse,fine=replay_mixed_success(old,prior,artificial=artificial)
        bindings['completed_mixed_grid_target70']=binding
        return restored,bindings,old[2],replay,coarse,fine
    except Exception as error:
        failure={'schema':SCHEMA,'status':'input-replay-failed-before-target-ladder-geometry','phase':phase,
            'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-start,'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out,failure)
        raise


def small_summary(report,out):
    # The inherited compact representation already preserves all trial outcomes
    # without duplicating full coefficient vectors or complete pool arrays.
    result=previous.small_summary(report,out)
    for key in ['curvature_target_ladder_definition','completed_mixed_target_attempt_retained']:
        if key in report:
            result[key]={k:copy.deepcopy(v) for k,v in report[key].items() if not k.startswith('published_final_')}
    stage=report.get('mixed_grid_short_step_stage')
    if stage:
        snap=stage['checkpoint']; output=result['mixed_grid_short_step_stage']; item=output['checkpoint']
        # All models/trials remain present. Column tables avoid repeating long
        # field names and nested decision dictionaries up to 72 times.
        model_columns=['number','stage_index','target_exact','linearized_at_accepted_index',
            'coarse_pool_rows','fine_pool_rows','result','lp_success','lp_status','lp_message','lp_nit',
            'lp_seconds','lp_rows','lp_variables','lp_matrix_bytes','trust_fraction',
            'initial_slack','predicted_slack','predicted_slack_improvement','maximum_linear_row_violation',
            'maximum_linear_bound_violation','maximum_absolute_step','step_l2']
        trial_columns=['model_number','trial_index','stage_index','target_exact','alpha_exact','attempt_status',
            'accepted','accepted_index','coarse_evaluation','fine_evaluation','coarse_eligible','fine_eligible',
            'coarse_max_eta','fine_max_eta','coarse_max_curvature','fine_max_curvature',
            'coarse_omitted_rows','new_coarse_rows','fine_omitted_rows','new_fine_rows','fine_violation_groups']
        models=[]; trials=[]
        for model in stage.get('solver',{}).get('models',[]):
            lp=model.get('linear_program',{})
            models.append([model.get('number'),model.get('stage_index'),model.get('fixed_stage_target_exact'),
                model.get('linearized_at_accepted_index'),model.get('coarse_pool_rows'),model.get('fine_pool_rows'),
                model.get('result'),lp.get('success'),lp.get('status'),lp.get('message'),lp.get('nit'),
                lp.get('elapsed_seconds'),lp.get('rows'),lp.get('variables'),lp.get('matrix_bytes'),
                lp.get('trust_fraction'),lp.get('initial_curvature_slack'),lp.get('predicted_curvature_slack'),
                lp.get('predicted_slack_improvement'),lp.get('maximum_linear_row_violation'),
                lp.get('maximum_linear_bound_violation'),lp.get('maximum_absolute_physical_step'),lp.get('physical_step_l2')])
            for ti,trial in enumerate(model.get('trials',[])):
                coarse=trial.get('coarse_decision',{}); fine=trial.get('fine_decision',{})
                trials.append([model.get('number'),ti,trial.get('stage_index'),trial.get('target_exact'),
                    trial.get('alpha_exact'),trial.get('attempt_status'),trial.get('accepted_as_next_iterate'),
                    trial.get('accepted_index'),trial.get('coarse_physical_evaluation'),trial.get('fine_value_evaluation'),
                    coarse.get('eligible_under_fixed_metric_and_physical_gates'),fine.get('eligible_under_fixed_metric_and_physical_gates'),
                    coarse.get('direct_max_eta'),fine.get('direct_max_eta'),
                    coarse.get('direct_maximum_absolute_principal_curvature'),fine.get('direct_maximum_absolute_principal_curvature'),
                    trial.get('coarse_omitted_rows'),trial.get('new_coarse_rows'),trial.get('fine_omitted_rows'),
                    trial.get('new_fine_rows'),trial.get('fine_violation_groups')])
        output.pop('models',None)
        output['model_table']={'columns':model_columns,'rows':models}
        output['trial_table']={'columns':trial_columns,'rows':trials}
        accepted_columns=['accepted_index','physical_state_sha256','maximum_curvature_on_both_grids',
            'reason','coarse_eligible','fine_eligible','coarse_max_eta','fine_max_eta','coarse_max_curvature','fine_max_curvature']
        accepted=[]
        for point in snap.get('accepted_iterates',[]):
            coarse=point.get('coarse',{}); fine=point.get('fine',{})
            accepted.append([point.get('accepted_index'),point.get('physical_state_sha256'),
                point.get('maximum_curvature_on_both_grids'),point.get('reason'),
                coarse.get('eligible_under_fixed_metric_and_physical_gates'),fine.get('eligible_under_fixed_metric_and_physical_gates'),
                coarse.get('direct_max_eta'),fine.get('direct_max_eta'),
                coarse.get('direct_maximum_absolute_principal_curvature'),fine.get('direct_maximum_absolute_principal_curvature')])
        item.pop('accepted_iterates',None)
        item['accepted_iterate_table']={'columns':accepted_columns,'rows':accepted}
        for key in ['active_stage_index','active_stage_target_exact','curvature_target_schedule_exact',
                    'cached_fine_target_rescorings_without_geometry','no_clock_counter_or_pool_reset_at_target_changes']:
            if key in snap:
                item[key]=copy.deepcopy(snap[key])
        event_columns=['kind','stage_index','target_exact','physical_state_sha256','total_models_so_far',
            'combined_value_evaluations','optimization_elapsed_seconds','coarse_eligible','fine_eligible',
            'coarse_max_curvature','fine_max_curvature','coarse_max_eta','fine_max_eta',
            'derived_from_saved_two_grid_acceptance_without_another_value_call']
        events=[]
        for event in snap.get('stage_events',[]):
            coarse=event.get('coarse',{}); fine=event.get('fine',{})
            events.append([event.get('kind'),event.get('stage_index'),event.get('target_exact'),
                event.get('physical_state_sha256'),event.get('total_models_so_far'),event.get('combined_value_evaluations'),
                event.get('optimization_elapsed_seconds'),coarse.get('eligible_under_fixed_metric_and_physical_gates'),
                fine.get('eligible_under_fixed_metric_and_physical_gates'),
                coarse.get('direct_maximum_absolute_principal_curvature'),fine.get('direct_maximum_absolute_principal_curvature'),
                coarse.get('direct_max_eta'),fine.get('direct_max_eta'),
                event.get('derived_from_saved_two_grid_acceptance_without_another_value_call')])
        item['stage_event_table']={'columns':event_columns,'rows':events}
        output['compact_table_semantics']='all model/trial/event indices and listed scalar values; exact coefficients and every original field remain in the full report'
    return result


def save_report(out,report):
    atomic_save(out,report)
    # The semantic column tables are ordinary UTF-8 JSON. Compact whitespace
    # prevents up to 72 numeric rows from spending the small-file allowance on
    # repeated indentation; no scientific field is split or encoded elsewhere.
    path=summary_path(out); temporary=path.with_suffix('.tmp')
    temporary.write_text(json.dumps(small_summary(report,out),separators=(',',':'),allow_nan=False)+'\n')
    temporary.replace(path)


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
        'process_clock_scope':'main entrance includes fourteen-input loader; run_audit and active optimization separately recorded',
        'prepare_elapsed_seconds':prepare_seconds,'learned_pool_replay':replay['learned_pool'],
        'completed_mixed_target_attempt_retained':replay['completed_mixed_target_attempt_retained'],
        'curvature_target_ladder_definition':{'targets_exact':list(TARGETS),'success_only_advance':True,
            'one_shared_LP_limit':cfg['max_linear_models'],'one_shared_value_limit':cfg['max_physical_evaluations'],
            'one_shared_active_seconds':cfg['max_seconds'],'targets_not_physical_coefficients':True,
            'old_target70_kept_as_completed_history':True,
            'final16_is_sampled_local_curvature_only':True,'reach_design_tau_exact':cfg['curvature_target_radius_exact']}}
    def save(status):
        now=time.monotonic()
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=report.get('mixed_grid_short_step_stage',{}).get('checkpoint',{}).get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('fourteen-inputs-replayed-before-target-ladder-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth); order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid
        report['phase']='one-two-grid-initialization-before-shared-active-clock'
        def checkpoint(snapshot):
            report['mixed_grid_short_step_stage']={'status':'current-target-ladder-checkpoint','checkpoint':snapshot,'solver':{}}
            save('target-ladder-two-grid-physical-checkpoint')
        objective=TargetLadderObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            fourteenth_report_decoded_sha256=bindings['completed_mixed_grid_target70']['decoded_sha256'],
            learned_pool_replay=replay['learned_pool'],old_metric_delta_and_old_curvature_targets_are_preserved_history=True)
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(learned_coarse,{'kind':'all-fourteenth-learned-coarse-rows-retained','source':replay['learned_pool']})
        objective.set_fine_pool(learned_fine,{'kind':'all-fourteenth-learned-fine-rows-retained','source':replay['learned_pool']})
        first=objective.evaluate(np.r_[initial,initial_target/scale])
        report['initial_current_constraints']=copy.deepcopy(first['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        save('complete-initial-two-grid-diagnostics-with-target65-not-assumed-feasible')
        report['phase']='shared-budget-fixed-target-ladder-with-both-grid-physical-acceptance'
        stage=run_ladder(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['mixed_grid_short_step_stage']=stage
        point=stage['checkpoint'].get('selected_two_grid_physical_point')
        if point is None:
            save('no-two-grid-physical-baseline-eligible')
            return report
        final=np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if coefficients(final)!=point['exact_binary64_physical_coefficients'] or digest(problem.identity(final))!=point['physical_state_sha256']:
            raise ValueError('selected complete coefficients or physical identity differs')
        identity=problem.identity(final); frozen,fc=problem.frozen_metric_copy(final)
        if (fc.tobytes()!=final.tobytes() or frozen.identity(fc)!=identity or frozen.metric_model(fc)!=metric
                or frozen.height_base_definition!=b0):
            raise ArithmeticError('freeze changed g, b0, physical coefficients or field')
        problem,final=frozen,fc
        report['final_state']=state_record(problem,final)
        final_target=float(Q(stage['active_stage_target_exact'])); zeta=final_target/scale
        report['phase']='same-state-independent-final-original-two-grid-values'
        work=problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit']=audit_data(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints']=candidate_decision(problem,gate,final,zeta,work,lower,upper,cfg)
        save('last-accepted-ladder-state-recomputed-on-original-coarse-grid')
        del objective
        fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
        fine=problem.geometry(final,radial,fine_theta,order)
        report['final_doubled_angle_audit']=audit_data(problem,final,fine,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints']=candidate_decision(problem,gate,final,zeta,fine,lower,upper,cfg)
        report['same_parameter_Pi_refinement']=compare_data(problem,work,problem,fine,final,
            name='one accepted ladder physical field, no parameter or target change between final angle grids',theta_stride=2)
        if problem.identity(final)!=identity:
            raise ArithmeticError('final angle refinement changed physical state')
        coarse_dec,fine_dec=report['final_full_grid_constraints'],report['final_doubled_constraints']
        eligible=bool(coarse_dec['eligible_under_fixed_metric_and_physical_gates'] and fine_dec['eligible_under_fixed_metric_and_physical_gates'])
        maximum=max(coarse_dec['direct_maximum_absolute_principal_curvature'],fine_dec['direct_maximum_absolute_principal_curvature'])
        initial_maximum=max(report['initial_current_constraints']['direct_maximum_absolute_principal_curvature'],
            report['initial_doubled_constraints']['direct_maximum_absolute_principal_curvature'])
        achieved=[x for x in TARGETS if eligible and maximum<=float(Q(x))+cfg['direct_curvature_tolerance']]
        report['final_selection_validation']={'both_value_grids_physical_gate_pass':eligible,
            'both_grid_maximum_curvature':maximum,'initial_both_grid_maximum_curvature':initial_maximum,
            'actual_curvature_decrease':initial_maximum-maximum,'last_active_target_exact':stage['active_stage_target_exact'],
            'last_active_target_reached':bool(eligible and maximum<=final_target+cfg['direct_curvature_tolerance']),
            'targets_reached_by_independent_final_values_exact':achieved,
            'all_schedule_targets_reached':len(achieved)==len(TARGETS),
            'whole_surface_reach_not_certified':True,
            'new_failure_not_promoted_to_accepted_physical_state':True}
        count=stage['checkpoint']['total_full_value_physical_evaluations']
        report['value_evaluation_counts']={'initialization_and_all_stages_coarse_plus_fine_within_shared_cap':count,
            'shared_cap':cfg['max_physical_evaluations'],'independent_final_same_state_value_calls':2,
            'total_counted_full_value_calls_in_this_driver':count+2,
            'failed_fine_attempts_consume_shared_cap':True,'Jacobian_batch_calls_recorded_separately':True,
            'target_rescoring_without_geometry_not_a_physical_value_call':True,'no_final_optimizer_or_step':True}
        report['limitations']={'all_value_gates_and_curvature_diagnostics_sampled_only':True,
            'metric_budget_167_over_625_is_not_exact_isometry':True,
            'target16_below_1000_over_61_does_not_pay_nonlocal_reach':True,
            'partial_target_progress_and_all_targets_achieved_are_different':True,
            'LP_feasibility_is_not_true_geometry_feasibility':True,'rejected_trials_not_warm_starts':True,
            'curvature_and_mirror_pairs_not_all_surface_pairs':True,'no_complete_embedding_or_reach_certificate':True,
            'no_old_optimizer_replayed':True}
        save('complete-two-grid-curvature-target-ladder-audit' if eligible
             else 'final-same-state-value-recheck-failed-do-not-use-as-new-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('curvature-target-ladder-audit-error-checkpoints-preserved')
        return report


def developer_check():
    targeted=ladder_check()
    with tempfile.TemporaryDirectory(prefix='curvature-ladder-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder)
        args,unused,unused_prior=previous.artificial_thirteen_inputs(directory)
        args.out=directory/'completed-mixed-grid-artificial.json'
        thirteen=previous.prepare_run(args,artificial=True)
        prior=previous.run_audit(thirteen,args.out,artificial=True,evaluate_only=True)
        if prior['status']!='complete-mixed-grid-fixed-target-short-step-audit':
            raise ArithmeticError('artificial fourteenth source fixture failed')
        args.mixed_grid_audit=args.out
        args.expected_mixed_grid_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'target-ladder-artificial.json'
        start=time.monotonic(); prepared=prepare_run(args,artificial=True,process_started=start)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=start,prepare_seconds=time.monotonic()-start)
        stage=report.get('mixed_grid_short_step_stage',{}); snap=stage.get('checkpoint',{})
        old_snap=prior['mixed_grid_short_step_stage']['checkpoint']
        old_coarse=old_snap['active_row_pool_history'][-1]['row_indices']
        old_fine=old_snap['fine_physical_row_pool_history'][-1]['row_indices']
        coarse_kept=set(old_coarse).issubset(snap.get('active_row_pool_history',[{}])[0].get('row_indices',[]))
        fine_kept=set(old_fine).issubset(snap.get('fine_physical_row_pool_history',[{}])[0].get('row_indices',[]))
        same=report.get('final_state')==prior['final_state']
        no_lp=stage.get('solver',{}).get('linear_program_invocation_count')==0
        summary=json.loads(summary_path(args.out).read_text())
        summary_ok=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        summary_bytes=summary_path(args.out).stat().st_size
        wrong=copy.copy(args); wrong.out=directory/'wrong-fourteenth-sha.json'; wrong.expected_mixed_grid_sha256='0'*64
        try:
            prepare_run(wrong,artificial=True); bad_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text())
            bad_sha=failure['phase']=='fourteenth-mixed-grid-byte-binding' and failure['new_solver_calls']==0
        broken=copy.deepcopy(prior)
        broken['mixed_grid_short_step_stage']['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
        try:
            replay_mixed_success(thirteen,broken,artificial=True); bad_state=False
        except ValueError:
            bad_state=True
        broken=copy.deepcopy(prior)
        broken['mixed_grid_short_step_stage']['checkpoint']['fine_physical_row_pool_history'][-1]['added_original_grid_coordinates'][0]['theta']=123.
        try:
            replay_mixed_success(thirteen,broken,artificial=True); bad_coord=False
        except ValueError:
            bad_coord=True
        frozen_sources=report.get('source_files_sha256')==implementation_hashes()
        status=report['status']; error=report.get('error')
        refinement=report.get('same_parameter_Pi_refinement')
        # Output-only stress fixture: the maximum declared 12 models / 72
        # backtracks / 22 stage events, plus 13 accepted points. It does not
        # evaluate any extra geometry or apply a parameter step.
        worst=copy.deepcopy(report); ws=worst['mixed_grid_short_step_stage']; wc=ws['checkpoint']
        sample=copy.deepcopy(wc['selected_two_grid_physical_point'])
        expected_trials=[]; expected_models=[]; expected_events=[]
        ws['solver']['models']=[]
        for mi in range(12):
            target=TARGETS[min(mi,len(TARGETS)-1)]
            lp={'success':True,'status':0,'message':'Artificial maximum-size output fixture; no research evaluation.',
                'nit':2000+mi,'elapsed_seconds':.71+mi/100,'rows':4308+mi,'variables':165,
                'matrix_bytes':5686560+mi,'trust_fraction':.01,'initial_curvature_slack':.003+mi/10000,
                'predicted_curvature_slack':.0001,'predicted_slack_improvement':.0029+mi/10000,
                'maximum_linear_row_violation':1e-10,'maximum_linear_bound_violation':0.,
                'maximum_absolute_physical_step':.0003,'physical_step_l2':.004}
            model={'number':mi+1,'stage_index':min(mi,10),'fixed_stage_target_exact':target,
                'linearized_at_accepted_index':mi,'coarse_pool_rows':3887+mi,'fine_pool_rows':94+mi,
                'result':'accepted-two-grid-physical-ladder-step','linear_program':lp,'trials':[]}
            expected_models.append((mi+1,target,lp['nit'],lp['matrix_bytes'],lp['predicted_slack_improvement']))
            for ti in range(6):
                coarse=copy.deepcopy(sample['coarse']); fine=copy.deepcopy(sample['fine'])
                coarse.update(eligible_under_fixed_metric_and_physical_gates=True,
                    direct_max_eta=.267-mi*1e-5-ti*1e-6,direct_maximum_absolute_principal_curvature=69-mi-ti/100)
                fine.update(eligible_under_fixed_metric_and_physical_gates=ti==5,
                    direct_max_eta=.2671-mi*1e-5-ti*1e-6,direct_maximum_absolute_principal_curvature=69.01-mi-ti/100)
                trial={'stage_index':min(mi,10),'target_exact':target,'alpha_exact':str(Q(1,2**ti)),
                    'attempt_status':'coarse-value-call-complete','accepted_as_next_iterate':ti==5,
                    'accepted_index':mi+1 if ti==5 else None,'coarse_physical_evaluation':2+6*mi+ti,
                    'fine_value_evaluation':2+6*mi+ti,'coarse_decision':coarse,'fine_decision':fine,
                    'coarse_omitted_rows':mi,'new_coarse_rows':mi,'fine_omitted_rows':ti,
                    'new_fine_rows':ti,'fine_violation_groups':{name:ti+mi+j for j,name in enumerate(FINE_GROUPS)}}
                model['trials'].append(trial)
                expected_trials.append((mi+1,ti,target,trial['alpha_exact'],ti==5,
                    coarse['direct_max_eta'],fine['direct_max_eta'],coarse['direct_maximum_absolute_principal_curvature'],
                    fine['direct_maximum_absolute_principal_curvature'],mi,ti,trial['fine_violation_groups']))
            ws['solver']['models'].append(model)
        wc['accepted_iterates']=[]
        for i in range(13):
            point=copy.deepcopy(sample); point['accepted_index']=i
            point['physical_state_sha256']=hashlib.sha256(('artificial-snapshot-'+str(i)).encode()).hexdigest()
            point['reason']={'kind':'artificial-maximum-output-fixture','stage_index':min(i,10)}
            wc['accepted_iterates'].append(point)
        wc['stage_events']=[]
        for i,target in enumerate(TARGETS):
            for kind in ['stage-start','stage-complete']:
                event={'kind':kind,'stage_index':i,'target_exact':target,'physical_state_sha256':sample['physical_state_sha256'],
                    'total_models_so_far':i+1,'combined_value_evaluations':2+2*i,
                    'optimization_elapsed_seconds':3.+i,'coarse':copy.deepcopy(sample['coarse']),
                    'fine':copy.deepcopy(sample['fine']),
                    'derived_from_saved_two_grid_acceptance_without_another_value_call':kind=='stage-complete'}
                wc['stage_events'].append(event)
                expected_events.append((kind,i,target,2+2*i,event['coarse']['direct_maximum_absolute_principal_curvature'],
                    event['fine']['direct_maximum_absolute_principal_curvature']))
        worst_path=directory/'maximum-output-artificial.json'
        save_report(worst_path,worst)
        compact=json.loads(summary_path(worst_path).read_text())
        cs=compact['mixed_grid_short_step_stage']; cc=cs['checkpoint']
        def decoded(table):
            return [dict(zip(table['columns'],row,strict=True)) for row in table['rows']]
        model_rows=decoded(cs['model_table']); trial_rows=decoded(cs['trial_table']); event_rows=decoded(cc['stage_event_table'])
        actual_models=[(r['number'],r['target_exact'],r['lp_nit'],r['lp_matrix_bytes'],r['predicted_slack_improvement']) for r in model_rows]
        actual_trials=[(r['model_number'],r['trial_index'],r['target_exact'],r['alpha_exact'],r['accepted'],
            r['coarse_max_eta'],r['fine_max_eta'],r['coarse_max_curvature'],r['fine_max_curvature'],
            r['coarse_omitted_rows'],r['fine_omitted_rows'],r['fine_violation_groups']) for r in trial_rows]
        actual_events=[(r['kind'],r['stage_index'],r['target_exact'],r['combined_value_evaluations'],
            r['coarse_max_curvature'],r['fine_max_curvature']) for r in event_rows]
        accepted_rows=decoded(cc['accepted_iterate_table'])
        # Also compare every listed value before/after JSON serialization, not
        # only the scientific projections checked directly against the fixture.
        expected_compact=small_summary(worst,worst_path)['mixed_grid_short_step_stage']
        full_tables_roundtrip=all(cs[key]==expected_compact[key] for key in ['model_table','trial_table'])
        full_tables_roundtrip=full_tables_roundtrip and all(cc[key]==expected_compact['checkpoint'][key]
            for key in ['accepted_iterate_table','stage_event_table'])
        table_values=(actual_models==expected_models and actual_trials==expected_trials and actual_events==expected_events
            and [r['accepted_index'] for r in accepted_rows]==list(range(13)) and full_tables_roundtrip)
        worst_bytes=summary_path(worst_path).stat().st_size
        full_unchanged=json.loads(worst_path.read_text())==worst
        worst_bound=compact['full_report']['sha256']==hashlib.sha256(worst_path.read_bytes()).hexdigest()
    passed=bool(targeted['passed'] and coarse_kept and fine_kept and same and no_lp and summary_ok
        and summary_bytes<95000 and bad_sha and bad_state and bad_coord and frozen_sources
        and worst_bytes<95000 and table_values and full_unchanged and worst_bound
        and status=='complete-two-grid-curvature-target-ladder-audit')
    return {'schema':'curvature-target-ladder-fourteen-input-artificial-check-v1','artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,'no_Actions_environment_forged':True,
        'targeted_new_stage_and_budget_branches':targeted,'full_main_status':status,'full_main_error':error,
        'same_complete_physical_coefficients_g_b0_and_freeze':same,'all_old_coarse_rows_retained':coarse_kept,
        'all_old_fine_rows_and_original_coordinates_retained':fine_kept,'artificial_full_main_has_no_LP':no_lp,
        'summary_binds_complete_report_bytes':summary_ok,'summary_bytes':summary_bytes,
        'source_hashes_match':frozen_sources,'wrong_fourteenth_SHA_saves_failure':bad_sha,
        'altered_complete_state_rejected':bad_state,'altered_original_fine_coordinate_rejected':bad_coord,
        'maximum_summary_fixture_counts':{'models':12,'trials':72,'stage_events':22,'accepted_points':13},
        'maximum_summary_bytes':worst_bytes,'maximum_summary_all_indices_and_scientific_table_values_roundtrip':table_values,
        'maximum_summary_full_report_unchanged_and_byte_bound':full_unchanged and worst_bound,
        'same_state_angle_refinement':refinement,'passed':passed}


def main():
    process_started=time.monotonic(); parser=argparse.ArgumentParser(description=__doc__)
    for name in ['input','anchor-input','short-audit','height-audit','prior-joint-audit','resume-audit',
                 'epigraph-audit','trial-audit','dense-audit','exchange-audit','curvature-audit',
                 'feasible-curvature-audit','fixed-target-audit','mixed-grid-audit']:
        parser.add_argument('--'+name,type=Path)
    for name in ['input','anchor','short','height','prior-joint','resume','epigraph','trial','dense',
                 'exchange','curvature','feasible-curvature','fixed-target','mixed-grid']:
        parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true'); parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:
            result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'curvature-target-ladder-development-error-v1','passed':False,
                'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-process_started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(),process_total_elapsed_seconds=time.monotonic()-process_started)
        atomic_save(args.out,result); print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:
            raise SystemExit(1)
        return
    start=time.monotonic()
    try:
        prepared=prepare_run(args,process_started=process_started)
    except Exception:
        raise SystemExit(1)
    report=run_audit(prepared,args.out,process_started=process_started,prepare_seconds=time.monotonic()-start)
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)
    if report['status']!='complete-two-grid-curvature-target-ladder-audit':
        raise SystemExit(1)


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Temporary growth-prefix restoration followed by one strip-reserve stage.

The twenty-four legacy inputs remain exact. A fresh same-job growth prefix
restores an eligible state and all pools without persisting a new payload.
The new stage changes only the normalized strip proposal targets.
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
from frame_entry_short_bounded_audit import audit_data,compare_data
from frame_independent_height_solve import state_record
from frame_curvature_epigraph_exchange import GROUPS
from frame_metric_budget_recovery import recovery_decision
from frame_metric_spectral_recovery import EPSILON_EXACT,PROPOSAL_BRANCHES
from frame_curvature_soc_metric_reserve_audit import exact_vector
import frame_metric_budget_restoration_rows as rows_api
import frame_metric_spectral_trust_growth_audit as growth
from frame_metric_spectral_strip_reserve import (
    StripReserveSpectralMetricObjective,run_strip_reserve_recovery,
    configuration as strip_configuration,implementation_hashes as strip_hashes,
    developer_check as strip_check,strip_floor_definition,
    penalty_definition,floor_definition,growth_definition,adaptive_definition)

SCHEMA='same-g-spectral-metric-strip-reserve-after-temporary-growth-audit-v1'
STAGE='metric_spectral_strip_reserve_stage'
PREFIX_STAGE='metric_spectral_trust_growth_stage'
OBSERVED_GROWTH_RUN='43681388902'
OBSERVED_GROWTH_SOURCE='7872857e7750e1b5091560b6362e52dd952bc6fa'
OBSERVED_GROWTH_STATE='f2bb6c35a10467d37d1c964c0135086b7451d469ab6548420ec76355b3207902'
OBSERVED_GROWTH_REPORT_SHA='2f9d65f5faf7d94637a34144af9ff8a5938d1891b6558bb7f0f816c3e944d875'
METRIC_TARGET='13/50'
CURVATURE_CAP='58'
INPUTS=growth.INPUTS
SHA_NAMES=growth.SHA_NAMES
coefficients=growth.coefficients
curvature_grid=growth.curvature_grid
summary_path=growth.summary_path


def implementation_hashes():
    result=growth.implementation_hashes();result.update(strip_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def configuration(base,*,artificial=False):
    if not artificial and any(Q(base[k])!=Q(value) for k,value in [
            ('previous_qualified_metric_budget_exact','167/625'),
            ('fixed_metric_budget_exact',METRIC_TARGET),
            ('fixed_hard_curvature_cap_exact',CURVATURE_CAP),
            ('hard_strip_half_width_exact','38999/100000')]):
        raise ValueError('preserve all actual metric/curvature/strip gates')
    return strip_configuration(base)


def restored_controller_state(stage,cfg):
    """Use completed updates; an interrupted last model contributes no success."""
    radius=float(Q(cfg['initial_trust_box_fraction_exact']));streak=0
    last_completed=0;origin='unchanged original seed: no model was started'
    models=stage.get('solver',{}).get('models',[])
    for index,model in enumerate(models):
        before=model.get('trust_before_model')
        if before is None or not np.isfinite(before) or float(before)!=radius:
            raise ValueError('temporary model radius does not follow the recorded previous controller')
        update=model.get('scale_feedback_update')
        if update is None:
            if index!=len(models)-1:
                raise ValueError('only the last temporary model may lack a completed controller update')
            origin='last model incomplete: its trust_before_model and previous completed streak'
            continue
        growth_record=update.get('conservative_growth',{})
        if growth_record.get('streak_before')!=streak:
            raise ValueError('temporary growth streak does not follow completed model history')
        next_radius=update.get('next_trust');next_streak=growth_record.get('streak_after')
        if (next_radius is None or not np.isfinite(next_radius) or next_radius<=0
                or type(next_streak) is not int
                or not 0<=next_streak<cfg['trust_growth_required_consecutive_models']):
            raise ValueError('temporary completed controller update is malformed')
        radius=float(next_radius);streak=next_streak;last_completed=index+1
        origin='last completed scale_feedback_update.next_trust and conservative_growth.streak_after'
    if stage.get('final_consecutive_growth_qualifying_models')!=streak:
        raise ValueError('temporary final controller streak disagrees with completed history')
    if radius>float(Q(cfg['trust_growth_maximum_box_fraction_exact'])):
        raise ValueError('temporary inherited radius exceeds unchanged growth cap')
    return {'schema':'restored-growth-controller-continuation-v1',
        'trust_binary64_exact':str(Q.from_float(radius)),'trust_evaluated':radius,
        'success_streak':streak,'origin':origin,'models_started':len(models),
        'last_completed_controller_model_position':last_completed,
        'unfinished_last_model_not_counted_as_success':bool(models and models[-1].get('scale_feedback_update') is None),
        'initial_growth_rule_and_actual_feedback_policy_unchanged':True}


def handoff_restored_growth(prepared,prefix,raw_binding,*,artificial=False):
    """Structural in-memory handoff; no geometry, optimizer, or fake old SHA."""
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prefix.get('schema')!=growth.SCHEMA
            or prefix.get('status')!='complete-two-grid-fixed-curvature-spectral-trust-growth-audit'
            or bool(prefix.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed current temporary growth result required')
    if (prefix.get('source_files_sha256')!=growth.implementation_hashes()
            or prefix.get('configuration')!=old_cfg or prefix.get('exact_input_storage')!=bindings
            or prefix.get('input_replay')!=old_replay
            or prefix.get('initial_state')!=state_record(problem,old_initial)
            or prefix.get('old_optimizer_calls_this_run')!=0
            or prefix.get('unchanged_complete_metric_and_height_reference') is not True):
        raise ValueError('temporary growth source/configuration/legacy inputs/initial identity differ')
    if not artificial and (prefix.get('github_sha')!=os.environ.get('GITHUB_SHA')
            or str(prefix.get('github_run_id'))!=os.environ.get('GITHUB_RUN_ID')
            or prefix.get('github_repository')!='Rogerhu12/math-research-public'
            or problem.nunknown!=163):
        raise ValueError('prefix must be the current public job and same163 family')
    stage=prefix[PREFIX_STAGE]
    if stage.get('error') is not None or 'error' in stage.get('status',''):
        raise ValueError('prefix implementation failure is not a qualified restoration')
    snap=stage['checkpoint'];point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('temporary growth accepted state missing')
    state=exact_vector(point.get('exact_binary64_physical_coefficients'),problem.nunknown)
    if (state.tolist()!=point.get('physical_parameter_coefficients_binary64')
            or coefficients(state)!=point.get('exact_binary64_physical_coefficients')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prefix.get('final_state')!=state_record(problem,state)):
        raise ValueError('temporary final exact coefficients or canonical identity differ')
    accepted=snap.get('accepted_iterates',[])
    if (not accepted or accepted[-1]!=point
            or problem.metric_model(state)!=problem.metric_model(old_initial)
            or old_replay.get('fixed_b0_definition_sha256')!=digest(problem.height_base_definition)):
        raise ValueError('temporary accepted state, fixed g or fixed b0 differ')
    validation=prefix.get('final_selection_validation',{})
    if not validation.get('both_value_grids_hard_and_old_metric_pass'):
        raise ValueError('temporary final two-grid actual gate failed')
    decisions=[prefix.get(k,{}) for k in ['final_full_grid_constraints','final_doubled_constraints']]
    for decision in decisions:
        if not decision.get('single_grid_admissible_recovery_point'):
            raise ValueError('temporary final decision was not independently admissible')
        for key in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
                'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']:
            if decision.get(key)!=old_cfg[key]:raise ValueError('temporary actual gate identity differs: '+key)
    if validation.get('both_grid_maximum_eta')!=max(d['direct_max_eta'] for d in decisions):
        raise ValueError('temporary final maximum does not agree with both decisions')
    radial,theta,grid=curvature_grid(tenth)
    if prefix.get('full_value_sampling_definition')!=grid:
        raise ValueError('temporary original full value sampling definition differs')
    histories=[snap.get(k,[]) for k in ['active_row_pool_history','fine_physical_row_pool_history']]
    if not all(histories):raise ValueError('temporary complete pool histories missing')
    coarse,fine=(h[-1] for h in histories);ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,total,rule,cap,previous in [
        (coarse,ci,11*len(radial)*len(theta),'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',
            old_cfg['max_pool_rows'],old_coarse),
        (fine,fi,22*len(radial)*len(theta),'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',
            old_cfg['max_fine_physical_pool_rows'],old_fine)]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=list(GROUPS)
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap or not set(previous).issubset(ids)):
            raise ValueError('temporary pool IDs/hash/group/layout/cap or inherited rows differ')
    added=fine.get('added_row_indices');fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added)
            or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=rows_api.fine_coordinates(added,radial,fine_theta)):
        raise ValueError('temporary fine original coordinate binding differs')
    locations={}
    for decision in [decisions[-1]]+[v.get('decision',{}) for v in snap.get('saved_fine_trials',[])
            if v.get('status')=='complete-doubled-angle-value-call']:
        loc=decision.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('temporary metric peak is not finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    continuation=restored_controller_state(stage,old_cfg)
    observed={'run':OBSERVED_GROWTH_RUN,'source':OBSERVED_GROWTH_SOURCE,
        'canonical_physical_state_sha256':OBSERVED_GROWTH_STATE,
        'temporary_complete_report_sha256':OBSERVED_GROWTH_REPORT_SHA,
        'raw_report_not_available_or_used_as_a_new_input':True}
    restoration={'schema':'same-job-temporary-growth-prefix-restoration-v1',
        'purpose':'restore necessary runtime state under metadata-only output policy, not a new scientific comparison',
        'prefix_scientific_implementation_sha256':growth.implementation_hashes(),
        'prefix_configuration':copy.deepcopy(old_cfg),'prefix_current_run':prefix.get('github_run_id'),
        'prefix_current_source':prefix.get('github_sha'),
        'prefix_temporary_raw_file':copy.deepcopy(raw_binding),
        'prefix_status':stage.get('status'),'prefix_budget_message':stage.get('budget_message'),
        'controller_continuation':continuation,
        'prefix_source_initial_physical_sha256':digest(problem.identity(old_initial)),
        'prefix_regenerated_final_physical_sha256':point['physical_state_sha256'],
        'observed_reference':observed,
        'regenerated_final_equals_observed_f2bb':point['physical_state_sha256']==OBSERVED_GROWTH_STATE,
        'old_raw_report_SHA_equality_not_required_or_claimed':True,
        'no_budget_extension_or_repeat_until_an_old_hash_matches':True,
        'different_wall_selected_state_may_continue_only_after_actual_two_grid_gates':True,
        'prefix_final_selection_validation':copy.deepcopy(validation),
        'prefix_final_gate_values':{name:{k:d.get(k) for k in [
            'single_grid_admissible_recovery_point','previous_metric_budget_pass','hard_strip_pass',
            'hard_ball_pass','signed_height_pass','independent_direct_curvature_pass',
            'direct_max_eta','direct_maximum_absolute_principal_curvature','maximum_absolute_y',
            'inner_strip_absolute_margin','minimum_signed_height','direct_mirror_radius_min_finite']}
            for name,d in zip(['coarse','fine'],decisions)},
        'prefix_accepted_count':len(accepted),
        'prefix_linear_program_count':stage.get('solver',{}).get('linear_program_invocation_count'),
        'prefix_shared_full_values':snap.get('total_full_value_physical_evaluations'),
        'prefix_optimization_active_seconds':prefix.get('optimization_active_seconds'),
        'prefix_run_audit_elapsed_seconds':prefix.get('run_audit_elapsed_seconds'),
        'prefix_preparation_elapsed_seconds':prefix.get('prepare_elapsed_seconds'),
        'prefix_failed_trials_remain_in_the_temporary_report_until_consumed':True,
        'prefix_report_and_summary_not_published_or_retained_after_this_job':True}
    learned={'schema':'temporary-growth-complete-learned-pool-handoff-v1',
        'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'all_previous_coarse_and_fine_integer_IDs_retained':True,
        'groups2_to10_have_original_actual_values_and_derivatives':True}
    cfg=configuration(old_cfg,artificial=artificial)
    replay={'schema':'temporary-growth-to-strip-reserve-in-memory-handoff-v1',
        'canonical_physical_state_sha256':point['physical_state_sha256'],
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'physical_parameter_count':problem.nunknown,'learned_pool':learned,
        'known_fine_metric_locations':list(locations.values()),'temporary_input_restoration':restoration,
        'controller_continuation':continuation,
        'explicit_new_constraint_definition':{
            'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
            'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
            'metric_restoration_target_exact':cfg['fixed_metric_budget_exact'],
            'proposal_epsilon_exact':EPSILON_EXACT,'proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
            'strip_proposal_floor_definition':strip_floor_definition(cfg),
            'curvature_proposal_floor_definition':floor_definition(cfg),
            'primary_physical_step_cost_definition':penalty_definition(cfg),
            'adaptive_scale_definition':adaptive_definition(cfg),
            'conservative_trust_growth_definition':growth_definition(cfg),
            'all_actual_gates_and163_physical_family_unchanged':True,
            'actual_new_stage_progress_is_measured_from_this_regenerated_initial_state':True,
            'no_initial_match_to_the_observed_f2bb_is_assumed':True}}
    return ((problem,state,gate,lower,upper,source_cfg,cfg),bindings,tenth,replay,
        np.asarray(ci,np.int64),np.asarray(fi,np.int64))


def small_summary(report,out):
    legacy=copy.copy(report);stage=legacy.pop(STAGE,None)
    if stage is not None:legacy[PREFIX_STAGE]=stage
    result=growth.resolve_summary_definition_references(growth.small_summary(legacy,out))
    if PREFIX_STAGE in result:result[STAGE]=result.pop(PREFIX_STAGE)
    result['temporary_input_restoration']=copy.deepcopy(report.get('temporary_input_restoration'))
    if STAGE in result:
        result[STAGE]['strip_proposal_floor']=strip_floor_definition(report['configuration'])
        result[STAGE].get('complete_group8_selected_row_source',{})['full_report_path']=STAGE+'.solver.models'
    return result


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


def print_prefix_outcomes(restoration):
    print('TEMPORARY INPUT RESTORATION -- one necessary frozen-growth prefix, no persistent payload',flush=True)
    for key in ['prefix_current_run','prefix_current_source','prefix_status','prefix_budget_message',
            'prefix_source_initial_physical_sha256','prefix_regenerated_final_physical_sha256',
            'regenerated_final_equals_observed_f2bb','prefix_accepted_count','prefix_linear_program_count',
            'prefix_shared_full_values','prefix_optimization_active_seconds','prefix_run_audit_elapsed_seconds',
            'prefix_preparation_elapsed_seconds']:
        print(key+': '+str(restoration.get(key)),flush=True)
    print('temporary raw bytes/SHA: '+str(restoration['prefix_temporary_raw_file']['bytes'])+' / '+
        restoration['prefix_temporary_raw_file']['sha256'],flush=True)
    print('prefix source-file-map SHA: '+digest(restoration['prefix_scientific_implementation_sha256']),flush=True)
    print('prefix exact configuration SHA: '+digest(restoration['prefix_configuration']),flush=True)
    for grid,decision in restoration['prefix_final_gate_values'].items():
        print(grid+' restored gates: '+'; '.join(k+'='+str(v) for k,v in decision.items()),flush=True)
    print('inherited controller: '+str(restoration['controller_continuation']),flush=True)
    print('Reference f2bb identity is an observation, not a forced replay condition. New progress starts at the actual restored state.',flush=True)


def print_strip_proposal_outcomes(report):
    print('STRIP PROPOSAL RESERVE -- original normalized row units, no true gate changed',flush=True)
    print('m | proposal | group | count | old target min | new target min | linear achieved min | max floor shortfall | max row violation | status',flush=True)
    for model in report.get(STAGE,{}).get('solver',{}).get('models',[]):
        proposals=[('primary',model.get('linear_program',{}))]
        proposals += [('SOC'+str(j),r.get('linear_program',{})) for j,r in enumerate(model.get('corrections',[]))]
        for name,record in proposals:
            for row in record.get('strip_proposal_diagnostics',{}).get('group_statistics',[]):
                def f(x):return '-' if x is None else format(x,'.17g') if isinstance(x,float) else str(x)
                values=[model['number'],name,row['group'],row['selected_count'],
                    row['old_target_minimum'],row['new_target_minimum'],row['linear_achieved_minimum'],
                    row['maximum_linear_floor_shortfall'],record.get('maximum_linear_row_violation'),record.get('status')]
                print(' | '.join(map(f,values)),flush=True)
    print('Positive requested linear margin is not a nonlinear shape or continuous enclosure.',flush=True)


def run_audit(prepared,out,*,artificial=False,evaluate_only=False,process_started=None,prepare_seconds=0.):
    restored,bindings,tenth,replay,coarse_pool,fine_pool=prepared
    problem,initial,gate,lower,upper,source_cfg,cfg=restored
    started=time.monotonic();process_started=started if process_started is None else process_started
    metric=copy.deepcopy(problem.metric_model(initial));b0=copy.deepcopy(problem.height_base_definition)
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':1,
        'necessary_growth_prefix_restoration_calls':1,'new_scientific_solver_calls':0,'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':state_record(problem,initial),'unchanged_complete_metric_and_height_reference':True,
        'prepare_elapsed_seconds':prepare_seconds,
        'learned_pool_replay':replay['learned_pool'],
        'temporary_input_restoration':replay['temporary_input_restoration'],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'process_clock_scope':'main includes one necessary temporary growth restoration and one new shared-budget strip stage; their clocks are separately reported'}
    def save(status):
        now=time.monotonic();snapshot=report.get('metric_spectral_strip_reserve_stage',{}).get('checkpoint',{})
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=snapshot.get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('twenty-four-inputs-replayed-before-new-spectral-metric-recovery-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='fixed-cap58-new-target026-initialization'
        def checkpoint(snapshot):
            report['metric_spectral_strip_reserve_stage']={'status':'current-two-grid-spectral-metric-recovery-checkpoint',
                'checkpoint':snapshot,'solver':{}}
            save('spectral-metric-recovery-last-accepted-physical-checkpoint')
        objective=StripReserveSpectralMetricObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            temporary_restored_prefix_raw_sha256=replay['temporary_input_restoration']['prefix_temporary_raw_file']['sha256'],
            learned_pool_replay=replay['learned_pool'],
            temporary_input_restoration=replay['temporary_input_restoration'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-current-temporary-prefix-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-current-temporary-prefix-eleven-group-fine-original-IDs',
            'source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        save('complete-two-grid-hard-cap-preflight-new-metric-target-not-assumed-feasible')
        report['phase']='one-shared-budget-metric-restoration-with-hard-curvature'
        report['new_scientific_solver_calls']=1
        stage=run_strip_reserve_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            continuation_state=replay['controller_continuation'],
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['metric_spectral_strip_reserve_stage']=stage
        point=stage['checkpoint'].get('selected_two_grid_physical_point')
        if point is None:
            save('no-original-two-grid-hard-qualified-baseline');return report
        final=np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if coefficients(final)!=point['exact_binary64_physical_coefficients'] or digest(problem.identity(final))!=point['physical_state_sha256']:
            raise ValueError('selected spectral-metric-recovery full coefficients/physical identity differ')
        identity=problem.identity(final);frozen,fc=problem.frozen_metric_copy(final)
        if (fc.tobytes()!=final.tobytes() or frozen.identity(fc)!=identity or frozen.metric_model(fc)!=metric
                or frozen.height_base_definition!=b0):
            raise ArithmeticError('final freezing changed g/b0/coefficients or physical field')
        problem,final=frozen,fc;report['final_state']=state_record(problem,final)
        report['phase']='independent-final-same-state-original384-and768-values'
        work=problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit']=audit_data(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints']=recovery_decision(problem,gate,final,work,lower,upper,cfg)
        save('last-accepted-metric-point-recomputed-on-original-coarse-grid')
        del objective
        fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
        fine=problem.geometry(final,radial,fine_theta,order)
        report['final_doubled_angle_audit']=audit_data(problem,final,fine,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints']=recovery_decision(problem,gate,final,fine,lower,upper,cfg)
        report['same_parameter_Pi_refinement']=compare_data(problem,work,problem,fine,final,
            name='same spectral-metric-recovery state and fixed hard cap; original angular grids',theta_stride=2)
        if problem.identity(final)!=identity:raise ArithmeticError('final angular refinement changed physical identity')
        c,f=report['final_full_grid_constraints'],report['final_doubled_constraints']
        eligible=bool(c['single_grid_admissible_recovery_point'] and f['single_grid_admissible_recovery_point'])
        maximum=max(c['direct_max_eta'],f['direct_max_eta'])
        start=max(report['initial_current_constraints']['direct_max_eta'],report['initial_doubled_constraints']['direct_max_eta'])
        new_target=bool(c['single_grid_new_target_qualified'] and f['single_grid_new_target_qualified'])
        report['final_selection_validation']={'both_value_grids_hard_and_old_metric_pass':eligible,
            'both_grid_maximum_eta':maximum,'initial_both_grid_maximum_eta':start,'actual_eta_decrease':start-maximum,
            'both_grid_maximum_curvature':max(c['direct_maximum_absolute_principal_curvature'],f['direct_maximum_absolute_principal_curvature']),
            'fixed_hard_curvature_cap_exact':CURVATURE_CAP,'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
            'new_metric_target_qualified_on_both_grids':new_target,
            'previous_qualified_budget_exact':cfg['previous_qualified_metric_budget_exact'],
            'qualification_not_assumed_from_LP_slack':True,'whole_surface_reach_not_certified':True}
        count=stage['checkpoint']['total_full_value_physical_evaluations']
        report['value_evaluation_counts']={'shared_initialization_and_trial_full_values':count,
            'shared_cap':cfg['max_physical_evaluations'],'independent_final_same_state_value_calls':2,
            'total_counted_full_value_calls_in_this_driver':count+2,
            'failed_fine_calls_and_actual_fine_SOC_residuals_count':True,
            'Jacobian_batches_recorded_separately':True,'no_final_optimizer':True}
        report['limitations']={'all_gates_and_curvatures_sampled_only':True,'new_target026_not_exact_isometry':True,
            'hard_cap58_above_1000_over61_is_not_reach_success':True,'full_nonlocal_reach_not_paid':True,
            'finite_evaluation_differences_not_error_enclosures':True,'same_g_b0_and163_not_expanded':True,
            'old_failed_delta_and_unfinished55_preserved':True,'necessary_frozen_growth_prefix_recreated_once':True,'no_other_old_optimizer_replayed':True}
        print_strip_proposal_outcomes(report)
        save('complete-two-grid-fixed-curvature-spectral-strip-reserve-audit' if eligible
            else 'final-recheck-failed-do-not-use-as-new-physical-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('spectral-strip-reserve-audit-error-last-checkpoint-preserved');return report



def run_pipeline(args,*,artificial=False,evaluate_only=False,process_started=None):
    """One temporary prefix, then one new stage; never persist prefix payload."""
    started=time.monotonic() if process_started is None else process_started
    phase='public-environment-and-legacy-input-contract';raw_binding=None;restoration=None
    prefix_invoked=0;new_invoked=0
    try:
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        parent=os.environ.get('RUNNER_TEMP')
        if artificial and Path('/dev/shm').is_dir():parent='/dev/shm'
        with tempfile.TemporaryDirectory(prefix='visible-strip-prefix-',dir=parent) as folder:
            prefix_out=Path(folder)/'restored-growth.json'
            prefix_args=copy.copy(args);prefix_args.out=prefix_out
            phase='strict-original-twenty-four-input-preparation';before=time.monotonic()
            prepared=growth.prepare_run(prefix_args,artificial=artificial,process_started=started)
            preparation=time.monotonic()-before
            phase='one-necessary-frozen-growth-prefix-restoration';prefix_invoked=1
            prefix=growth.run_audit(prepared,prefix_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=preparation)
            raw=prefix_out.read_bytes()
            raw_binding={'filename':prefix_out.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                'temporary_current_job_file_only':True,'not_an_observed_old_report_SHA_replay':True}
            del raw
            phase='current-temporary-prefix-state-gates-pools-controller-handoff'
            continued=handoff_restored_growth(prepared,prefix,raw_binding,artificial=artificial)
            restoration=continued[3]['temporary_input_restoration']
            print_prefix_outcomes(restoration)
            # The complete prefix is no longer needed. Its file remains only
            # inside this temporary directory until the pipeline leaves it.
            del prefix,prepared
            phase='new-normalized-strip-reserve-stage';new_invoked=1
            result=run_audit(continued,args.out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            return result
    except Exception as error:
        failure={'schema':SCHEMA,'status':'strip-reserve-pipeline-failed-last-written-scientific-checkpoint-preserved',
            'phase':phase,'source_files_sha256':implementation_hashes(),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'artificial_inputs_only':bool(artificial),'necessary_growth_prefix_restoration_calls':prefix_invoked,
            'new_scientific_solver_calls':new_invoked,'temporary_prefix_raw_binding':raw_binding,
            'temporary_input_restoration':restoration,
            'process_total_elapsed_seconds':time.monotonic()-started,
            'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
        # A failure after a new stage checkpoint must not destroy that best.
        if new_invoked and Path(args.out).exists():
            try:
                existing=json.loads(Path(args.out).read_text())
                existing['scientific_status_before_pipeline_failure']=existing.get('status')
                existing['status']='strip-reserve-pipeline-error-last-checkpoint-preserved'
                existing['pipeline_failure']=failure
                save_report(args.out,existing);return existing
            except (OSError,ValueError,TypeError,KeyError):
                pass
        save_report(args.out,failure);return failure


def developer_check():
    """Only the new rows and temporary handoff/IO; no old growth development."""
    from types import SimpleNamespace
    from unittest.mock import patch
    import sys
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    targeted=strip_check()
    class ToyProblem:
        nunknown=3
        slices={'u':slice(0,1),'v':slice(1,2),'height':slice(2,3),'metric':slice(3,3)}
        height_base_definition={'schema':'pure-artificial-handoff-fixed-b0'}
        def identity(self,x):
            return {'family':'pure-artificial-handoff-only','coefficients':coefficients(x)}
        def metric_model(self,x):
            return {'schema':'pure-artificial-handoff-metric','mathematical_definition_sha256':digest({'metric':'toy'})}
        def evaluation_definition(self):
            return {'schema':'pure-artificial-handoff-no-geometry-method'}
    problem=ToyProblem();old_state=np.array([.2,.3,.4]);new_state=np.array([.21,.31,.41])
    r=np.array([0.,.5,1.]);theta=np.arange(4)*np.pi/2
    grid={'schema':'tiny-artificial-handoff-grid','definition_sha256':digest({'r':r.tolist(),'theta':theta.tolist()})}
    cfg=growth.configuration(recovery_configuration(start_configuration(),target=METRIC_TARGET,curvature_cap=CURVATURE_CAP),
        artificial=True)
    bindings={'fixture':{'decoded_sha256':'f'*64,'decoded_bytes':1,'stored_sha256':'f'*64,'stored_bytes':1,'gzip_storage':False}}
    replay={'schema':'artificial-current-prepared-prefix','fixed_b0_definition_sha256':digest(problem.height_base_definition)}
    prepared=((problem,old_state,None,np.full(3,-1.),np.ones(3),{'primitive_order':3,'tau':'61/1000'},cfg),
        bindings,{'schema':'artificial-grid-input'},replay,np.array([0,48]),np.array([0,96]))
    def pool(ids,fine=False):
        nt=2*len(theta) if fine else len(theta)
        record={'row_indices':ids,'row_count':len(ids),'row_indices_sha256':digest(ids),
            'group_order':list(GROUPS),'total_full_grid_rows':11*len(r)*nt,
            'flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index' if fine
                else 'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'}
        if fine:
            record.update(added_row_indices=ids,added_original_grid_coordinates=rows_api.fine_coordinates(
                ids,r,np.arange(nt)*2*np.pi/nt))
        return record
    point={'exact_binary64_physical_coefficients':coefficients(new_state),
        'physical_parameter_coefficients_binary64':new_state.tolist(),
        'physical_state_sha256':digest(problem.identity(new_state))}
    decision={k:cfg[k] for k in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
        'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']}
    decision.update(single_grid_admissible_recovery_point=True,direct_max_eta=.2,
        direct_max_eta_location={'t':.5,'theta':0.},direct_maximum_absolute_principal_curvature=2.,
        hard_strip_pass=True,hard_ball_pass=True,signed_height_pass=True,independent_direct_curvature_pass=True,
        previous_metric_budget_pass=True,maximum_absolute_y=.1,inner_strip_absolute_margin=.28999,
        minimum_signed_height=.05,direct_mirror_radius_min_finite=.1)
    seed=float(Q(cfg['initial_trust_box_fraction_exact']));double=2*seed
    models=[
        {'number':1,'trust_before_model':seed,'scale_feedback_update':{'next_trust':double,
            'conservative_growth':{'streak_before':0,'streak_after':0}}},
        {'number':2,'trust_before_model':double,'trials':[{'attempt_status':'coarse-value-call-complete'}]}]
    prefix={'schema':growth.SCHEMA,'status':'complete-two-grid-fixed-curvature-spectral-trust-growth-audit',
        'artificial_inputs_only':True,'source_files_sha256':growth.implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,'initial_state':state_record(problem,old_state),
        'old_optimizer_calls_this_run':0,'unchanged_complete_metric_and_height_reference':True,
        'final_state':state_record(problem,new_state),'github_run_id':'pure-artificial',
        'github_sha':'pure-artificial-no-research','github_repository':'Rogerhu12/math-research-public',
        'full_value_sampling_definition':grid,'final_full_grid_constraints':decision,
        'final_doubled_constraints':copy.deepcopy(decision),
        'final_selection_validation':{'both_value_grids_hard_and_old_metric_pass':True,'both_grid_maximum_eta':.2},
        PREFIX_STAGE:{'status':'shared-value-time-or-pool-budget-exit','error':None,
            'final_consecutive_growth_qualifying_models':0,
            'solver':{'models':models,'linear_program_invocation_count':2},
            'checkpoint':{'selected_two_grid_physical_point':point,'accepted_iterates':[point],
                'active_row_pool_history':[pool([0,1,48])],
                'fine_physical_row_pool_history':[pool([0,1,96],True)],
                'saved_fine_trials':[],'total_full_value_physical_evaluations':4}}}
    raw_binding={'filename':'artificial-prefix.json','bytes':1,'sha256':'e'*64}
    with patch.object(sys.modules[__name__],'curvature_grid',return_value=(r,theta,grid)):
        restored=handoff_restored_growth(prepared,prefix,raw_binding,artificial=True)
        rc=restored[3]['controller_continuation']
        different_allowed=bool(not restored[3]['temporary_input_restoration']['regenerated_final_equals_observed_f2bb']
            and np.array_equal(restored[0][1],new_state))
        inherited=bool(rc['trust_evaluated']==double and rc['success_streak']==0
            and rc['unfinished_last_model_not_counted_as_success'])
        before=copy.deepcopy(prefix);handoff_restored_growth(prepared,prefix,raw_binding,artificial=True)
        immutable=prefix==before
        rejects={}
        for name in ['coefficient','gate','pool','controller','implementation-error']:
            wrong=copy.deepcopy(prefix)
            if name=='coefficient':
                wrong[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
            elif name=='gate':wrong['final_doubled_constraints']['single_grid_admissible_recovery_point']=False
            elif name=='pool':wrong[PREFIX_STAGE]['checkpoint']['fine_physical_row_pool_history'][-1]['row_indices']=[0]
            elif name=='controller':wrong[PREFIX_STAGE]['final_consecutive_growth_qualifying_models']=1
            else:wrong[PREFIX_STAGE]['error']={'message':'injected failure'}
            try:handoff_restored_growth(prepared,wrong,raw_binding,artificial=True);rejects[name]=False
            except (ValueError,KeyError):rejects[name]=True
        complete=copy.deepcopy(prefix[PREFIX_STAGE])
        complete['solver']['models'][-1]['scale_feedback_update']={'next_trust':double,
            'conservative_growth':{'streak_before':0,'streak_after':1}}
        complete['final_consecutive_growth_qualifying_models']=1
        c=restored_controller_state(complete,cfg)
        completed=bool(c['trust_evaluated']==double and c['success_streak']==1
            and not c['unfinished_last_model_not_counted_as_success'])
        empty={'solver':{'models':[]},'final_consecutive_growth_qualifying_models':0}
        e=restored_controller_state(empty,cfg)
        zero=bool(e['trust_evaluated']==seed and e['success_streak']==0)
        calls={'prepare':0,'prefix':0,'new':0};temporary=[]
        def prepare_stub(args,**kwargs):
            calls['prepare']+=1;return prepared
        def prefix_stub(p,out,**kwargs):
            calls['prefix']+=1;temporary.append(Path(out))
            atomic_save(out,prefix);return copy.deepcopy(prefix)
        def new_stub(p,out,**kwargs):
            calls['new']+=1
            if p[3]['controller_continuation']['trust_evaluated']!=double:raise AssertionError('controller reset')
            report={'schema':SCHEMA,'status':'pure-artificial-pipeline-new-stage-stub',
                'temporary_input_restoration':p[3]['temporary_input_restoration'],
                STAGE:{'solver':{'linear_program_invocation_count':0},'checkpoint':{}}}
            atomic_save(out,report);return report
        with tempfile.TemporaryDirectory(prefix='strip-new-IO-only-',dir='/dev/shm') as d:
            out=Path(d)/'new-audit.json';args=SimpleNamespace(out=out)
            with patch.object(growth,'prepare_run',side_effect=prepare_stub),patch.object(growth,'run_audit',side_effect=prefix_stub), \
                    patch.object(sys.modules[__name__],'run_audit',side_effect=new_stub):
                result=run_pipeline(args,artificial=True,evaluate_only=True)
            unique=bool([p.name for p in Path(d).glob('*-audit.json')]==['new-audit.json']
                and all(not p.exists() for p in temporary)
                and [k for k,v in result.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
            one_each=calls=={'prepare':1,'prefix':1,'new':1}
            failargs=SimpleNamespace(out=Path(d)/'failure-audit.json')
            with patch.object(growth,'prepare_run',side_effect=ValueError('injected new pipeline loader failure')):
                failure=run_pipeline(failargs,artificial=True,evaluate_only=True)
            fail=json.loads(failargs.out.read_text())
            failure_saved=bool(fail['phase']=='strict-original-twenty-four-input-preparation'
                and fail['necessary_growth_prefix_restoration_calls']==0 and fail['new_scientific_solver_calls']==0
                and fail['error']['type']=='ValueError')
    # Execute the new run_audit path on the existing explicit small jet family.
    # This is no saved candidate, and no old prefix or old development is solved.
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    class AuditArrayProblem(_CurvatureArrayProblem):
        ball_radius=1.01;strip_half_width=.38999;shape_weight=2.
        port=SimpleNamespace(side=1,width=.02)
        slices={'u':slice(0,1),'v':slice(1,2),'height':slice(2,3),'metric':slice(3,3)}
        height_base_definition={'schema':'artificial-strip-audit-b0'}
        def metric_model(self,state):
            return {'schema':'artificial-strip-audit-g','mathematical_definition_sha256':digest({'g':'array'})}
        def evaluation_definition(self):
            return {'schema':'artificial-strip-audit-evaluation'}
        def frozen_metric_copy(self,state):
            return copy.copy(self),np.asarray(state).copy()
        def geometry(self,*args,**kwargs):
            data=super().geometry(*args,**kwargs)
            nr=len(data['radial'])
            data['height']={'b':np.zeros(nr),'b_s':np.zeros(nr),'b_ss':np.zeros(nr)}
            return data
    ap=AuditArrayProblem();ax=np.array([.3,.6,.6])
    ag=HeightAffineGate.from_artificial_array_problem(ap)
    ar=np.array([0.,.2,.4,.7,1.]);at=np.arange(12)*np.pi/6
    acfg=configuration(recovery_configuration(start_configuration(),target='1/100',curvature_cap='3'),artificial=True)
    acfg.update(radial_Jacobian_batch_owned_rows=2,fine_Jacobian_owned_radial_rows=2,max_linear_models=1)
    areplay=copy.deepcopy(restored[3]);areplay['known_fine_metric_locations']=[]
    areplay['canonical_physical_state_sha256']=digest(ap.identity(ax))
    areplay['complete_metric_sha256']=ap.metric_model(ax)['mathematical_definition_sha256']
    areplay['fixed_b0_definition_sha256']=digest(ap.height_base_definition)
    aprepared=((ap,ax,ag,np.array([-.8,-1.,-1.]),np.array([2.,1.,1.]),
        {'primitive_order':3,'tau':'1/1000'},acfg),bindings,{'fixture':'array','selected_raw_auxiliary_delta':.5},areplay,np.array([0]),np.array([0]))
    agrid={'schema':'artificial-strip-audit-grid','definition_sha256':digest({'r':ar.tolist(),'t':at.tolist()})}
    with tempfile.TemporaryDirectory(prefix='strip-new-audit-only-',dir='/dev/shm') as d:
        out=Path(d)/'strip-audit.json'
        with patch.object(sys.modules[__name__],'curvature_grid',return_value=(ar,at,agrid)), \
                patch.object(sys.modules[__name__],'audit_data',side_effect=lambda *a,**k:
                    {'artificial_existing_jet_array_only':True,'no_research_surface':True}):
            full=run_audit(aprepared,out,artificial=True,evaluate_only=True)
        native=json.loads(summary_path(out).read_text())
        full_new_path=bool(full['status']=='complete-two-grid-fixed-curvature-spectral-strip-reserve-audit'
            and full[STAGE]['solver']['linear_program_invocation_count']==0
            and full['final_selection_validation']['both_value_grids_hard_and_old_metric_pass']
            and full['initial_state']==full['final_state']
            and full[STAGE]['solver']['restored_controller_continuation']==areplay['controller_continuation']
            and native['full_report']['sha256']==hashlib.sha256(out.read_bytes()).hexdigest()
            and [k for k,v in native.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        # The actual new-stage checkpoint is retained if a later pipeline error occurs.
        def checkpoint_then_fail(p,out,**kwargs):
            save_report(out,full)
            raise RuntimeError('injected error after a valid new-stage checkpoint')
        args=SimpleNamespace(out=Path(d)/'failure-after-checkpoint-audit.json')
        with patch.object(sys.modules[__name__],'curvature_grid',return_value=(r,theta,grid)), \
                patch.object(growth,'prepare_run',side_effect=prepare_stub), \
                patch.object(growth,'run_audit',side_effect=prefix_stub), \
                patch.object(sys.modules[__name__],'run_audit',side_effect=checkpoint_then_fail):
            preserved=run_pipeline(args,artificial=True,evaluate_only=True)
        failure_preserves=bool(preserved.get('status')=='strip-reserve-pipeline-error-last-checkpoint-preserved'
            and preserved.get('scientific_status_before_pipeline_failure')==full.get('status')
            and preserved.get('final_state')==full['final_state']
            and preserved.get(STAGE)==full[STAGE]
            and preserved.get('pipeline_failure',{}).get('error',{}).get('type')=='RuntimeError')
    checks={'new_initial_final_audit_summary_paths_executed_on_small_array_family':full_new_path,
        'later_pipeline_error_preserves_written_scientific_checkpoint':failure_preserves,
        'different_regenerated_canonical_explicitly_allowed_after_gates':different_allowed,
        'partial_last_model_inherits_true_radius_and_previous_streak':inherited,
        'completed_controller_update_and_nonzero_streak_retained':completed,
        'zero_models_use_only_the_original_seed':zero,'original_prefix_object_not_mutated':immutable,
        'bad_temporary_handoffs_rejected':all(rejects.values()),
        'one_prefix_and_one_new_stage_without_old_development':one_each,
        'single_top_level_audit_and_stage_and_prefix_cleanup':unique,
        'preparation_failure_still_writes_small_diagnostic':failure_saved}
    return {'schema':SCHEMA+'-artificial-check','artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,
        'old_growth_development_not_repeated':True,'new_library_checks':targeted,
        'checks':checks,'handoff_rejection_cases':rejects,
        'artificial_new_audit_status':full.get('status'),'artificial_new_audit_error':full.get('error'),
        'artificial_new_stage_error':full.get(STAGE,{}).get('error'),
        'passed':bool(targeted['passed'] and all(checks.values()))}


def main():
    started=time.monotonic();parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    if args.check_only:
        try:result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':SCHEMA+'-development-error','passed':False,
                'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(),
            process_total_elapsed_seconds=time.monotonic()-started)
        atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    report=run_pipeline(args,process_started=started)
    print(json.dumps({'out':str(args.out),'status':report.get('status')}),flush=True)
    if report.get('status')!='complete-two-grid-fixed-curvature-spectral-strip-reserve-audit':
        raise SystemExit(1)


if __name__=='__main__':main()

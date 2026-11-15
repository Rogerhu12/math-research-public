#!/usr/bin/env python3
"""Nineteen-input continuation: fixed hard curvature 58, metric target 13/50.

The previously qualified metric budget remains 167/625 until both complete
value grids pass the new target. No old optimizer is rerun. Actual geometry
and proposal steps require this repository's public Actions environment.
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
from frame_curvature_epigraph_exchange import GROUPS
from frame_curvature_mixed_grid_steps import FINE_GROUPS, fine_row_coordinates
from frame_metric_budget_recovery import (POLICY, MetricRecoveryObjective, run_recovery,
    configuration as recovery_configuration, implementation_hashes as recovery_hashes,
    recovery_decision, compact, developer_check as recovery_check)
import frame_curvature_soc_metric_reserve_audit as previous

SCHEMA='same-g-fixed-curvature-lower-metric-budget-audit-v1'
PRIOR_RUN='43665345551'
PRIOR_SOURCE='0aae9a6a85583a9f87415e586d8db2c9c7fea6a7'
PRIOR_FINAL='512de71f983e86521dda4250e387ed1449ce29626763f49accde94bdc89666a9'
METRIC_TARGET='13/50'
CURVATURE_CAP='58'
INPUTS=previous.INPUTS+['soc_metric_reserve_audit']
SHA_NAMES=previous.SHA_NAMES+['soc-metric-reserve']
coefficients=previous.coefficients
curvature_grid=previous.curvature_grid
summary_path=previous.summary_path


def implementation_hashes():
    result=previous.implementation_hashes();result.update(recovery_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def configuration(base,*,artificial=False):
    if not artificial and Q(base['fixed_metric_budget_exact'])!=Q('167/625'):
        raise ValueError('the old qualified metric budget must be exactly 167/625')
    return recovery_configuration(base,target=METRIC_TARGET,curvature_cap=CURVATURE_CAP,artificial_io=artificial)


def replay_reserve_success(prepared,prior,*,artificial=False):
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prior.get('schema')!=previous.SCHEMA
            or prior.get('status')!='complete-two-grid-SOC-metric-reserve-curvature-audit'
            or bool(prior.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('the completed nineteenth reserve report is required')
    if prior.get('source_files_sha256')!=previous.implementation_hashes() or prior.get('configuration')!=old_cfg:
        raise ValueError('nineteenth source/configuration differs')
    if not artificial and (str(prior.get('github_run_id'))!=PRIOR_RUN or prior.get('github_sha')!=PRIOR_SOURCE):
        raise ValueError('nineteenth source/run differs')
    for name,binding in bindings.items():
        recorded=prior.get('exact_input_storage',{}).get(name,{})
        if any(recorded.get(k)!=binding.get(k) for k in
                ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']):
            raise ValueError('nineteenth preceding input byte binding differs: '+name)
    if (prior.get('initial_state')!=state_record(problem,old_initial) or prior.get('input_replay')!=old_replay
            or prior.get('old_optimizer_calls_this_run')!=0
            or not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_failed_metric_auxiliary_delta')!=tenth['selected_raw_auxiliary_delta']):
        raise ValueError('nineteenth full original state/history binding differs')
    stage=prior['mixed_grid_short_step_stage'];snap=stage['checkpoint']
    point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('nineteenth complete two-grid accepted point missing')
    state=previous.exact_vector(point.get('exact_binary64_physical_coefficients'),problem.nunknown)
    if (state.tolist()!=point.get('physical_parameter_coefficients_binary64')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prior.get('final_state')!=state_record(problem,state)):
        raise ValueError('nineteenth full exact coefficients/canonical state differ')
    if not artificial and point['physical_state_sha256']!=PRIOR_FINAL:
        raise ValueError('this recovery stage starts only from the saved 512de71f reserve point')
    accepted=snap.get('accepted_iterates',[])
    if not accepted or accepted[-1]!=point or problem.metric_model(state)!=problem.metric_model(old_initial):
        raise ValueError('nineteenth selected accepted point/fixed complete metric differs')
    validation=prior.get('final_selection_validation',{})
    if not validation.get('both_value_grids_physical_gate_pass'):
        raise ValueError('nineteenth full final physical gates failed')
    if not artificial and (stage.get('completed_targets_exact')!=[] or stage.get('active_stage_target_exact')!='55'
            or validation.get('last_active_target_reached') is not False
            or point.get('reason',{}).get('kind')!='SOC-corrected-short-step'):
        raise ValueError('preserve actual full SOC success and unfinished55 history')
    for key in ['final_full_grid_constraints','final_doubled_constraints']:
        d=prior.get(key,{})
        if not d.get('eligible_under_fixed_metric_and_physical_gates'):
            raise ValueError('nineteenth original final physical gate failed')
        if any(d.get(k)!=old_cfg[k] for k in
                ['fixed_metric_budget_exact','hard_strip_half_width_exact','mirror_target_exact']):
            raise ValueError('nineteenth original physical gate definition differs')
        if d.get('direct_maximum_absolute_principal_curvature',float('inf'))>float(Q(CURVATURE_CAP)):
            raise ValueError('new fixed cap must already exceed both published actual curvatures')
    radial,theta,grid=curvature_grid(tenth)
    if prior.get('full_value_sampling_definition')!=grid:
        raise ValueError('nineteenth complete original value grid differs')
    h=snap.get('active_row_pool_history',[]);fh=snap.get('fine_physical_row_pool_history',[])
    if not h or not fh:raise ValueError('nineteenth two saved pools missing')
    coarse,fine=h[-1],fh[-1];ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,names,total,rule,cap in [
        (coarse,ci,list(GROUPS),11*len(radial)*len(theta),
         'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows']),
        (fine,fi,list(FINE_GROUPS),7*len(radial)*2*len(theta),
         'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'])]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=names
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap):
            raise ValueError('nineteenth exact learned pool index/group/hash differs')
    if not set(old_coarse).issubset(ci) or not set(old_fine).issubset(fi):
        raise ValueError('nineteenth dropped previously learned rows')
    added=fine.get('added_row_indices');fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added) or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=fine_row_coordinates(added,radial,fine_theta)):
        raise ValueError('nineteenth fine original-coordinate binding differs')
    if not artificial and (len(ci)!=4240 or len(fi)!=1310):
        raise ValueError('real saved reserve pools must contain all 4240/1310 rows')
    locations={}
    for d in [prior['final_doubled_constraints']]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('nineteenth peak is not finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    retained={'source_run':prior.get('github_run_id'),'source_commit':prior.get('github_sha'),
        'status':stage['status'],'old_target55_was_not_reached':not bool(validation.get('last_active_target_reached')),
        'completed_targets_exact':stage.get('completed_targets_exact'),
        'old_curvature_final':validation.get('both_grid_maximum_curvature'),
        'old_curvature_drop':validation.get('actual_curvature_decrease'),
        'old_actual_reports_and_failed_trials_not_relabelled':True,
        'new_cap58_is_a_new_constraint_role_not_old55_success':True}
    learned={'schema':'nineteenth-reserve-original-two-pools-v1','source_run':prior.get('github_run_id'),
        'source_commit':prior.get('github_sha'),'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],
        'fine_original_group_order':list(FINE_GROUPS),'fine_new_group_order':list(GROUPS),
        'all_preceding_integer_row_ids_and_coordinates_preserved':True}
    cfg=configuration(old_cfg,artificial=artificial)
    replay={'schema':'nineteen-input-fixed-curvature-metric-recovery-replay-v1','eighteen_input_replay':old_replay,
        'canonical_physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),'physical_parameter_count':problem.nunknown,
        'same_full_saved_coefficients_g_b0_space_and_value_grids':True,
        'learned_pool':learned,'completed_reserve_attempt_retained':retained,
        'known_fine_metric_locations':list(locations.values()),
        'explicit_new_constraint_definition':{'fixed_hard_curvature_cap_exact':CURVATURE_CAP,
            'previous_qualified_metric_budget_exact':old_cfg['fixed_metric_budget_exact'],
            'metric_restoration_target_exact':cfg['fixed_metric_budget_exact'],
            'artificial_large_metric_budget_for_IO_only':bool(cfg.get('artificial_large_metric_budget_for_IO_only')),
            'physical_model_unchanged':True,'new_target_not_assumed_feasible':True,
            'original12LP40value120seconds_shared_budget':True},
        'old_optimizer_calls_replayed':0,'no_research_geometry_in_structural_replay':True}
    return (problem,state,gate,lower,upper,source_cfg,cfg),replay,np.asarray(ci,np.int64),np.asarray(fi,np.int64)


def prepare_run(args,*,artificial=False,process_started=None):
    start=time.monotonic();process_started=start if process_started is None else process_started
    phase='eighteen-input-prior-reserve-start-replay';bindings={}
    try:
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        old=previous.prepare_run(args,artificial=artificial,process_started=process_started)
        bindings=copy.deepcopy(old[1]);phase='nineteenth-reserve-byte-binding'
        if args.soc_metric_reserve_audit is None or args.expected_soc_metric_reserve_sha256 is None:
            raise ValueError('nineteenth full reserve report and decoded SHA required')
        prior,raw,binding=read_input(args.soc_metric_reserve_audit,args.expected_soc_metric_reserve_sha256)
        phase='nineteenth-full-accepted-state-and-old-index-pools'
        restored,replay,coarse,fine=replay_reserve_success(old,prior,artificial=artificial)
        bindings['completed_soc_metric_reserve']=binding
        return restored,bindings,old[2],replay,coarse,fine
    except Exception as error:
        save_report(args.out,{'schema':SCHEMA,'status':'input-replay-failed-before-metric-recovery-geometry',
            'phase':phase,'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-start,
            'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__,'message':str(error)}})
        raise


def _table(columns,records):
    return {'columns':columns,'rows':[[r.get(k) for k in columns] for r in records]}


def small_summary(report,out):
    names=['schema','status','phase','source_files_sha256','configuration','github_sha','github_run_id',
        'github_repository','artificial_inputs_only','old_optimizer_calls_this_run',
        'old_failed_metric_auxiliary_delta','elapsed_seconds','run_audit_elapsed_seconds',
        'prepare_elapsed_seconds','process_total_elapsed_seconds','optimization_active_seconds',
        'peak_rss_kib_linux','learned_pool_replay','completed_reserve_attempt_retained',
        'new_constraint_role_definition','initial_current_constraints','initial_doubled_constraints',
        'final_full_grid_constraints','final_doubled_constraints','final_selection_validation',
        'same_parameter_Pi_refinement','value_evaluation_counts','limitations','error']
    result={k:copy.deepcopy(report[k]) for k in names if k in report}
    result['exact_input_storage']={k:{n:v.get(n) for n in
        ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']}
        for k,v in report.get('exact_input_storage',{}).items()}
    for name in ['initial_state','final_state']:
        p=report.get(name)
        if p:
            result[name]={'canonical_physical_state_sha256':p['canonical_physical_state_sha256'],
                'parameter_count':len(p['parameter_coefficients_binary64']),
                'complete_metric_sha256':p['metric_model']['mathematical_definition_sha256'],
                'evaluation_sha256':digest(p['evaluation_definition'])}
    stage=report.get('metric_budget_recovery_stage')
    if stage:
        s=stage.get('solver',{});snap=stage.get('checkpoint',{})
        sr={k:copy.deepcopy(stage[k]) for k in ['status','error','budget_message','new_metric_target_reached_on_both_grids'] if k in stage}
        sr['solver']={k:copy.deepcopy(v) for k,v in s.items() if k!='models'}
        counters=['physical_geometry_evaluations','doubled_angle_full_value_evaluations',
            'total_full_value_physical_evaluations','initialization_elapsed_seconds','optimization_elapsed_seconds',
            'jacobian_geometry_batches','jacobian_refreshes','fine_selected_Jacobian_batches','fine_selected_Jacobian_refreshes',
            'fine_selected_Jacobian_seconds','maximum_returned_batch_Jacobian_bytes',
            'fine_selected_Jacobian_maximum_returned_bytes','fine_selected_Jacobian_maximum_retained_bytes',
            'fine_selected_Jacobian_maximum_query_radial_rows','fine_batch_ordinary_replay_maxima',
            'maximum_same_state_batch_ordinary_jet_difference','same_state_batch_ordinary_jet_differences_by_field',
            'accepted_coarse_cache_restores_without_new_geometry','accepted_fine_cache_restores_without_new_geometry',
            'maximum_retained_accepted_cache_array_bytes','objective_evaluation_sha256']
        sr['checkpoint']={k:copy.deepcopy(snap[k]) for k in counters if k in snap}
        sr['pool_history']={name:[[r['version'],r['row_count'],len(r['added_row_indices']),r['row_indices_sha256']]
            for r in snap.get(name,[])] for name in ['active_row_pool_history','fine_physical_row_pool_history']}
        models=[];trials=[];corrections=[]
        for m in s.get('models',[]):
            lp=m.get('linear_program',{})
            row={k:m.get(k) for k in ['number','linearized_at_accepted_index','linearized_at_physical_sha256',
                'coarse_pool_rows','fine_pool_rows','result']}
            row.update(lp);models.append(row)
            for ti,t in enumerate(m.get('trials',[])):
                c,f=t.get('coarse_decision',{}),t.get('fine_decision',{})
                r={k:t.get(k) for k in ['kind','alpha_exact','attempt_status','accepted_as_next_iterate','accepted_index',
                    'coarse_physical_evaluation','fine_value_evaluation','coarse_omitted_rows','coarse_omitted_hard_rows',
                    'new_coarse_rows','fine_omitted_rows','fine_omitted_hard_rows','new_fine_rows']}
                r.update(model=m['number'],trial=ti,
                    physical_coefficients_sha256=digest(t.get('exact_binary64_physical_coefficients',[])),
                    coarse_eta=c.get('direct_max_eta'),fine_eta=f.get('direct_max_eta'),
                    coarse_curvature=c.get('direct_maximum_absolute_principal_curvature'),
                    fine_curvature=f.get('direct_maximum_absolute_principal_curvature'),
                    coarse_hard=c.get('single_grid_hard_gate_pass'),fine_hard=f.get('single_grid_hard_gate_pass'),
                    coarse_old_metric=c.get('previous_metric_budget_pass'),fine_old_metric=f.get('previous_metric_budget_pass'),
                    coarse_new_target=c.get('single_grid_new_target_qualified'),fine_new_target=f.get('single_grid_new_target_qualified'),
                    fine_group_omitted=[t.get('fine_violation_groups',{}).get(g,{}).get('omitted') for g in GROUPS],
                    correction_weight=t.get('parabolic_curve',{}).get('correction_weight_exact'),
                    linear_metric_slack_upper_bound=t.get('parabolic_curve',{}).get('linear_metric_slack_upper_bound'))
                trials.append(r)
            for j,c in enumerate(m.get('corrections',[])):
                r={k:c.get(k) for k in ['primary_trial_index','primary_trial_physical_sha256','coarse_residual_evaluation',
                    'fine_residual_evaluation','coarse_pool_version','fine_pool_version']}
                r.update(c.get('linear_program',{}));r.update(model=m['number'],correction=j);corrections.append(r)
        sr['model_table']=_table(['number','linearized_at_accepted_index','linearized_at_physical_sha256',
            'coarse_pool_rows','fine_pool_rows','result','success','status','nit','elapsed_seconds','rows','variables',
            'matrix_bytes','trust_fraction','initial_metric_slack','predicted_metric_slack','predicted_slack_improvement',
            'normalized_step_norm','maximum_linear_row_violation','maximum_linear_bound_violation',
            'maximum_absolute_physical_step','physical_step_l2'],models)
        sr['trial_table']=_table(['model','trial','kind','alpha_exact','attempt_status','physical_coefficients_sha256',
            'accepted_as_next_iterate','accepted_index','coarse_physical_evaluation','fine_value_evaluation',
            'coarse_eta','fine_eta','coarse_curvature','fine_curvature','coarse_hard','fine_hard',
            'coarse_old_metric','fine_old_metric','coarse_new_target','fine_new_target',
            'coarse_omitted_rows','coarse_omitted_hard_rows','new_coarse_rows',
            'fine_omitted_rows','fine_omitted_hard_rows','new_fine_rows','fine_group_omitted',
            'correction_weight','linear_metric_slack_upper_bound'],trials)
        sr['correction_table']=_table(['model','correction','primary_trial_index','primary_trial_physical_sha256',
            'coarse_residual_evaluation','fine_residual_evaluation','coarse_pool_version','fine_pool_version',
            'LP_invoked','success','status','nit','elapsed_seconds','initial_metric_slack','primary_predicted_metric_slack',
            'primary_predicted_slack_improvement','metric_slack_budget','corrected_predicted_metric_slack',
            'corrected_actual_trial_linear_metric_slack',
            'primary_box_normalized_step_infinity_norm','maximum_box_normalized_correction_infinity_norm',
            'correction_box_normalized_infinity_norm','maximum_absolute_correction','correction_l2',
            'maximum_linear_row_violation','maximum_linear_bound_violation',
            'minimum_corrected_linear_hard_margin','corrected_affine_cap_margin','proposal_rejected_before_LP',
            'proposal_rejected_before_geometry'],corrections)
        sr['accepted_table']=_table(['accepted_index','physical_state_sha256','maximum_eta_on_both_grids',
            'maximum_curvature_on_both_grids','new_metric_target_qualified_on_both_grids','reason'],
            snap.get('accepted_iterates',[]))
        result['metric_budget_recovery_stage']=sr
    raw=Path(out).read_bytes()
    result['full_report']={'filename':Path(out).name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
        'complete_exact_states_rows_and_all_trial_coefficients_remain_in_full_report':True}
    return result


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


def run_audit(prepared,out,*,artificial=False,evaluate_only=False,process_started=None,prepare_seconds=0.):
    restored,bindings,tenth,replay,coarse_pool,fine_pool=prepared
    problem,initial,gate,lower,upper,source_cfg,cfg=restored
    started=time.monotonic();process_started=started if process_started is None else process_started
    metric=copy.deepcopy(problem.metric_model(initial));b0=copy.deepcopy(problem.height_base_definition)
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':0,'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':state_record(problem,initial),'unchanged_complete_metric_and_height_reference':True,
        'prepare_elapsed_seconds':prepare_seconds,
        'learned_pool_replay':replay['learned_pool'],
        'completed_reserve_attempt_retained':replay['completed_reserve_attempt_retained'],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'process_clock_scope':'main includes nineteen-input replay; one initialization and one shared optimization clock'}
    def save(status):
        now=time.monotonic();snapshot=report.get('metric_budget_recovery_stage',{}).get('checkpoint',{})
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=snapshot.get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('nineteen-inputs-replayed-before-new-metric-recovery-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='fixed-cap58-new-target026-initialization'
        def checkpoint(snapshot):
            report['metric_budget_recovery_stage']={'status':'current-two-grid-metric-recovery-checkpoint',
                'checkpoint':snapshot,'solver':{}}
            save('metric-recovery-last-accepted-physical-checkpoint')
        objective=MetricRecoveryObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            nineteenth_report_decoded_sha256=bindings['completed_soc_metric_reserve']['decoded_sha256'],
            learned_pool_replay=replay['learned_pool'],
            completed_reserve_attempt_retained=replay['completed_reserve_attempt_retained'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-nineteenth-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-nineteenth-seven-group-fine-IDs-in-new-eleven-group-layout',
            'source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        save('complete-two-grid-hard-cap-preflight-new-metric-target-not-assumed-feasible')
        report['phase']='one-shared-budget-metric-restoration-with-hard-curvature'
        stage=run_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['metric_budget_recovery_stage']=stage
        point=stage['checkpoint'].get('selected_two_grid_physical_point')
        if point is None:
            save('no-original-two-grid-hard-qualified-baseline');return report
        final=np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if coefficients(final)!=point['exact_binary64_physical_coefficients'] or digest(problem.identity(final))!=point['physical_state_sha256']:
            raise ValueError('selected metric-recovery full coefficients/physical identity differ')
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
            name='same metric-recovery state and fixed hard cap; original angular grids',theta_stride=2)
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
            'old_failed_delta_and_unfinished55_preserved':True,'no_old_optimizer_replayed':True}
        save('complete-two-grid-fixed-curvature-metric-recovery-audit' if eligible
            else 'final-recheck-failed-do-not-use-as-new-physical-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('metric-recovery-audit-error-last-checkpoint-preserved');return report


def artificial_nineteen_inputs(directory):
    args,unused,unused_prior=previous.artificial_eighteen_inputs(directory)
    args.out=directory/'completed-artificial-metric-reserve.json'
    prepared=previous.prepare_run(args,artificial=True)
    report=previous.run_audit(prepared,args.out,artificial=True,evaluate_only=True)
    if report['status']!='complete-two-grid-SOC-metric-reserve-curvature-audit':
        raise ArithmeticError('small artificial reserve predecessor failed')
    args.soc_metric_reserve_audit=args.out
    args.expected_soc_metric_reserve_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    return args,prepared,report


def developer_check():
    targeted=recovery_check()
    with tempfile.TemporaryDirectory(prefix='metric-recovery-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder);args,old_prepared,prior=artificial_nineteen_inputs(directory)
        args.out=directory/'metric-recovery-artificial.json';start=time.monotonic()
        prepared=prepare_run(args,artificial=True,process_started=start)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=start,prepare_seconds=time.monotonic()-start)
        stage=report.get('metric_budget_recovery_stage',{});snap=stage.get('checkpoint',{})
        old=prior['mixed_grid_short_step_stage']['checkpoint']
        retained=all(set(old[name][-1]['row_indices']).issubset(snap.get(name,[{}])[0].get('row_indices',[]))
            for name in ['active_row_pool_history','fine_physical_row_pool_history'])
        same=report.get('final_state')==prior['final_state']
        complete_fine=snap.get('fine_physical_row_pool_history',[{}])[-1].get('group_order')==list(GROUPS)
        no_lp=stage.get('solver',{}).get('linear_program_invocation_count')==0
        summary=json.loads(summary_path(args.out).read_text());size=summary_path(args.out).stat().st_size
        bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args);wrong.out=directory/'wrong-nineteenth-SHA.json';wrong.expected_soc_metric_reserve_sha256='0'*64
        try:prepare_run(wrong,artificial=True);wrong_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text())
            wrong_sha=failure['phase']=='nineteenth-reserve-byte-binding' and failure['new_solver_calls']==0
        bad=copy.deepcopy(prior)
        bad['mixed_grid_short_step_stage']['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
        try:replay_reserve_success(old_prepared,bad,artificial=True);wrong_state=False
        except ValueError:wrong_state=True
        bad=copy.deepcopy(prior);fp=bad['mixed_grid_short_step_stage']['checkpoint']['fine_physical_row_pool_history'][-1]
        first=fp['row_indices'][0];r,t,unused=curvature_grid(old_prepared[2])
        fp['added_row_indices']=[first]
        fp['added_original_grid_coordinates']=fine_row_coordinates([first],r,np.arange(2*len(t))*np.pi/len(t))
        fp['added_original_grid_coordinates'][0]['theta']=123.
        try:replay_reserve_success(old_prepared,bad,artificial=True);wrong_coordinate=False
        except ValueError:wrong_coordinate=True
        # Output stress only. No geometry, LP, or new research parameter use.
        stress=copy.deepcopy(report);s=stress['metric_budget_recovery_stage'];cp=s['checkpoint']
        sample=copy.deepcopy(cp['selected_two_grid_physical_point'])
        s['solver']['models']=[];expected=[]
        for mi in range(12):
            model={'number':mi+1,'linearized_at_accepted_index':mi,'linearized_at_physical_sha256':sample['physical_state_sha256'],
                'coarse_pool_rows':4240+mi,'fine_pool_rows':1310+mi,'result':'artificial-table-stress',
                'linear_program':{'success':True,'initial_metric_slack':.01,'predicted_metric_slack':.005,'trust_fraction':.001},
                'trials':[],'corrections':[]}
            for ti in range(7):
                t={'kind':['primary-metric-short-step','metric-SOC-corrected-short-step','metric-SOC-parabolic-backtrack'][min(ti,2)],
                    'alpha_exact':str(Q(1,2**max(ti-1,0))),'attempt_status':'coarse-value-call-complete',
                    'accepted_as_next_iterate':ti==6,'accepted_index':mi+1 if ti==6 else None,
                    'coarse_decision':copy.deepcopy(sample['coarse']),'fine_decision':copy.deepcopy(sample['fine']),
                    'exact_binary64_physical_coefficients':sample['exact_binary64_physical_coefficients'],
                    'fine_violation_groups':{g:{'whole_grid':mi+j,'omitted':ti+j} for j,g in enumerate(GROUPS)}}
                if ti>=2:t['parabolic_curve']={'correction_weight_exact':str(Q(1,2**(2*(ti-1)))),
                    'linear_metric_slack_upper_bound':.01/(ti+1)}
                model['trials'].append(t);expected.append((mi+1,ti,t['kind'],t['alpha_exact']))
            model['corrections']=[{'primary_trial_index':0,'primary_trial_physical_sha256':sample['physical_state_sha256'],
                'linear_program':copy.deepcopy(targeted['SOC_toy_report'])}]
            s['solver']['models'].append(model)
        cp['accepted_iterates']=[]
        for i in range(13):
            point=copy.deepcopy(sample);point['accepted_index']=i;point['reason']={'kind':'artificial-stress','model':i}
            cp['accepted_iterates'].append(point)
        sp=directory/'stress-metric-recovery.json';save_report(sp,stress)
        st=json.loads(summary_path(sp).read_text());stress_size=summary_path(sp).stat().st_size
        tb=st['metric_budget_recovery_stage']['trial_table']
        values=[dict(zip(tb['columns'],row,strict=True)) for row in tb['rows']]
        tables=[(r['model'],r['trial'],r['kind'],r['alpha_exact']) for r in values]==expected
        full_unchanged=json.loads(sp.read_text())==stress and st['full_report']['sha256']==hashlib.sha256(sp.read_bytes()).hexdigest()
        status=report['status'];error=report.get('error');refinement=report.get('same_parameter_Pi_refinement')
    passed=bool(targeted['passed'] and same and retained and complete_fine and no_lp and bound and size<95000
        and wrong_sha and wrong_state and wrong_coordinate and tables and full_unchanged and stress_size<95000
        and status=='complete-two-grid-fixed-curvature-metric-recovery-audit')
    return {'schema':SCHEMA+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,'no_Actions_environment_forged':True,
        'new_roles_and_full_fine_geometry_check':targeted,
        'full_main_status':status,'full_main_error':error,'same_state_g_b0_and_freeze':same,
        'all_old_pools_retained':retained,'fine_four_curvature_groups_enabled':complete_fine,
        'full_IO_artificial_path_has_no_LP':no_lp,'summary_byte_bound':bound,'summary_bytes':size,
        'wrong_nineteenth_SHA_saves_failure':wrong_sha,'changed_coefficients_rejected':wrong_state,
        'changed_fine_coordinates_rejected':wrong_coordinate,
        'stress_counts':{'models':12,'trials':84,'corrections':12,'accepted':13},
        'stress_summary_bytes':stress_size,'all_trial_rows_roundtrip':tables,'full_report_unchanged':full_unchanged,
        'same_state_angular_refinement':refinement,'passed':passed}


def main():
    started=time.monotonic();parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':SCHEMA+'-development-error','passed':False,'artificial_inputs_only':True,
                'source_files_sha256':implementation_hashes(),'process_total_elapsed_seconds':time.monotonic()-started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(),process_total_elapsed_seconds=time.monotonic()-started)
        atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    before=time.monotonic()
    try:prepared=prepare_run(args,process_started=started)
    except Exception:raise SystemExit(1)
    report=run_audit(prepared,args.out,process_started=started,prepare_seconds=time.monotonic()-before)
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)
    if report['status']!='complete-two-grid-fixed-curvature-metric-recovery-audit':raise SystemExit(1)


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Twenty-two-input continuation with a curvature-only proposal floor.

The preceding three accepted adaptive steps and all learned rows are retained.
Only groups7..10 primary/SOC linear targets receive the exact floor1e-7.
The actual gates, g/b0/163, target026, curvature58 and budgets remain unchanged.
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
from frame_metric_budget_recovery import recovery_decision, compact
from frame_metric_spectral_recovery import EPSILON_EXACT, PROPOSAL_BRANCHES
from frame_metric_spectral_curvature_reserve import (POLICY, FLOOR,
    CurvatureReserveSpectralMetricObjective,run_curvature_reserve_recovery,
    configuration as reserve_configuration,implementation_hashes as reserve_hashes,
    developer_check as reserve_check,floor_definition)
from frame_metric_spectral_adaptive import adaptive_definition
from frame_curvature_soc_metric_reserve_audit import exact_vector
import frame_metric_spectral_adaptive_audit as previous
import frame_metric_budget_restoration_rows as rows_api

SCHEMA='same-g-spectral-metric-curvature-reserve-audit-v1'
PRIOR_RUN='43671924759'
PRIOR_SOURCE='67319aea213353ac444a5a2ce905fef6068804fd'
PRIOR_FINAL='a9eda7ed42ae3f45d369c136f924488cd36562076723536141f5b913c804652d'
METRIC_TARGET='13/50'
CURVATURE_CAP='58'
INPUTS=previous.INPUTS+['spectral_adaptive_audit']
SHA_NAMES=previous.SHA_NAMES+['spectral-adaptive']
coefficients=previous.coefficients
curvature_grid=previous.curvature_grid
summary_path=previous.summary_path


def implementation_hashes():
    result=previous.implementation_hashes();result.update(reserve_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def configuration(base,*,artificial=False):
    if not artificial and any(Q(base[k])!=Q(value) for k,value in [
        ('previous_qualified_metric_budget_exact','167/625'),('fixed_metric_budget_exact',METRIC_TARGET),
        ('fixed_hard_curvature_cap_exact',CURVATURE_CAP)]):
        raise ValueError('preserve the actual old/new metric budgets and curvature58')
    return reserve_configuration(base)


def replay_adaptive_progress(prepared,prior,*,artificial=False):
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prior.get('schema')!=previous.SCHEMA
            or prior.get('status')!='complete-two-grid-fixed-curvature-spectral-adaptive-recovery-audit'
            or bool(prior.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed twenty-second metric-recovery report required')
    if prior.get('source_files_sha256')!=previous.implementation_hashes() or prior.get('configuration')!=old_cfg:
        raise ValueError('twenty-second implementation/configuration differs')
    if not artificial and (str(prior.get('github_run_id'))!=PRIOR_RUN or prior.get('github_sha')!=PRIOR_SOURCE):
        raise ValueError('twenty-second actual source/run differs')
    for name,binding in bindings.items():
        recorded=prior.get('exact_input_storage',{}).get(name,{})
        if any(recorded.get(k)!=binding.get(k) for k in
                ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']):
            raise ValueError('twenty-second predecessor byte binding differs: '+name)
    if (prior.get('initial_state')!=state_record(problem,old_initial) or prior.get('input_replay')!=old_replay
            or prior.get('old_optimizer_calls_this_run')!=0
            or not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_failed_metric_auxiliary_delta')!=tenth['selected_raw_auxiliary_delta']):
        raise ValueError('twenty-second complete original state/history differs')
    stage=prior['metric_spectral_adaptive_stage'];snap=stage['checkpoint']
    point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('twenty-second complete accepted point missing')
    state=exact_vector(point.get('exact_binary64_physical_coefficients'),problem.nunknown)
    if (state.tolist()!=point.get('physical_parameter_coefficients_binary64')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prior.get('final_state')!=state_record(problem,state)):
        raise ValueError('twenty-second exact coefficient/canonical state mismatch')
    if not artificial and point['physical_state_sha256']!=PRIOR_FINAL:
        raise ValueError('start only from the qualified saveda9eda physical point')
    accepted=snap.get('accepted_iterates',[])
    if (not accepted or accepted[-1]!=point or problem.metric_model(state)!=problem.metric_model(old_initial)
            or old_replay.get('fixed_b0_definition_sha256')!=digest(problem.height_base_definition)):
        raise ValueError('twenty-second selected accepted point or complete metric mismatch')
    validation=prior.get('final_selection_validation',{})
    if not validation.get('both_value_grids_hard_and_old_metric_pass'):
        raise ValueError('twenty-second true two-grid hard/old-metric gates failed')
    if not artificial and (np.array_equal(state,old_initial) or len(accepted)!=4
            or validation.get('actual_eta_decrease',0)<=0 or validation.get('new_metric_target_qualified_on_both_grids') is not False):
        raise ValueError('preserve all three actual accepted steps and unfinished026, not an unsaved trial')
    for key in ['final_full_grid_constraints','final_doubled_constraints']:
        d=prior.get(key,{})
        if not d.get('single_grid_admissible_recovery_point'):
            raise ValueError('twenty-second final actual hard or old metric failed')
        if any(d.get(k)!=old_cfg[k] for k in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
                'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']):
            raise ValueError('twenty-second original gate definition differs')
    radial,theta,grid=curvature_grid(tenth)
    if prior.get('full_value_sampling_definition')!=grid:
        raise ValueError('twenty-second complete value grid differs')
    h=snap.get('active_row_pool_history',[]);fh=snap.get('fine_physical_row_pool_history',[])
    if not h or not fh:raise ValueError('twenty-second learned pool histories missing')
    coarse,fine=h[-1],fh[-1];ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,total,rule,cap in [
        (coarse,ci,11*len(radial)*len(theta),'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows']),
        (fine,fi,22*len(radial)*len(theta),'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'])]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=list(GROUPS)
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap):
            raise ValueError('twenty-second complete learned ID/group/hash/layout mismatch')
    if not set(old_coarse).issubset(ci) or not set(old_fine).issubset(fi):
        raise ValueError('twenty-second dropped earlier learned rows')
    added=fine.get('added_row_indices');fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added) or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=rows_api.fine_coordinates(added,radial,fine_theta)):
        raise ValueError('twenty-second added fine row original coordinates differ')
    if not artificial and (len(ci)!=4402 or len(fi)!=3489):
        raise ValueError('retain exactly all4402/all3489 published learned rows before adding new witnesses')
    locations={}
    for d in [prior['final_doubled_constraints']]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('twenty-second recorded peak is not finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    retained={'source_run':prior.get('github_run_id'),'source_commit':prior.get('github_sha'),
        'status':stage['status'],'old_newtarget026_was_not_reached':not bool(validation.get('new_metric_target_qualified_on_both_grids')),
        'old_actual_eta_decrease':validation.get('actual_eta_decrease'),
        'old_accepted_count':len(accepted),'old_linear_programs':stage.get('solver',{}).get('linear_program_invocation_count'),
        'completed_attempt_and_all_failed_trials_not_relabelled':True,
        'new_curvature_floor_changes_no_old_report_spectral_rows_or_actual_gates':True,
        'old_minimum_trust_exit_not_relabelled_as_budget_exhaustion':True,
        'old_SOC_time_limit_not_relabelled_as_infeasibility':True}
    learned={'schema':'twenty-second-metric-recovery-learned-pools-v1','source_run':prior.get('github_run_id'),
        'source_commit':prior.get('github_sha'),'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'all_preceding_integer_row_ids_and_coordinates_preserved':True,
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'groups2_to10_have_original_values_and_derivatives':True}
    cfg=configuration(old_cfg,artificial=artificial)
    replay={'schema':'twenty-two-input-spectral-adaptive-replay-v1','twenty_one_input_replay':old_replay,
        'canonical_physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),'physical_parameter_count':problem.nunknown,
        'same_saved_final_coefficients_g_b0_space_and_value_grids':True,
        'learned_pool':learned,'completed_adaptive_progress_retained':retained,
        'known_fine_metric_locations':list(locations.values()),
        'explicit_new_constraint_definition':{'fixed_hard_curvature_cap_exact':CURVATURE_CAP,
            'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
            'metric_restoration_target_exact':cfg['fixed_metric_budget_exact'],
            'curvature_reserve_policy':POLICY,'proposal_epsilon_exact':EPSILON_EXACT,
            'adaptive_scale_definition':adaptive_definition(cfg),
            'curvature_proposal_floor_definition':floor_definition(cfg),
            'proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
            'actual_two_grid_eta_Schur_curvature_and_all_physical_gates_unchanged':True,
            'artificial_large_metric_budget_for_IO_only':bool(cfg.get('artificial_large_metric_budget_for_IO_only')),
            'physical_model_unchanged':True,'new_target_not_assumed_feasible':True,
            'original12LP40value120seconds_shared_budget':True},
        'old_optimizer_calls_replayed':0,'no_research_geometry_in_structural_replay':True}
    return (problem,state,gate,lower,upper,source_cfg,cfg),replay,np.asarray(ci,np.int64),np.asarray(fi,np.int64)


def prepare_run(args,*,artificial=False,process_started=None):
    start=time.monotonic();process_started=start if process_started is None else process_started
    phase='twenty-one-input-prior-start-replay';bindings={}
    try:
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        old=previous.prepare_run(args,artificial=artificial,process_started=process_started)
        bindings=copy.deepcopy(old[1]);phase='twenty-second-metric-recovery-byte-binding'
        if args.spectral_adaptive_audit is None or args.expected_spectral_adaptive_sha256 is None:
            raise ValueError('twenty-second complete report and decoded SHA required')
        prior,raw,binding=read_input(args.spectral_adaptive_audit,args.expected_spectral_adaptive_sha256)
        phase='twenty-second-saved-qualified-state-and-all-learned-pools'
        restored,replay,coarse,fine=replay_adaptive_progress(old,prior,artificial=artificial)
        bindings['completed_spectral_adaptive']=binding
        return restored,bindings,old[2],replay,coarse,fine
    except Exception as error:
        save_report(args.out,{'schema':SCHEMA,'status':'input-replay-failed-before-spectral-recovery-geometry',
            'phase':phase,'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-start,
            'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__,'message':str(error)}})
        raise


def _table(columns,records):
    return {'columns':columns,'rows':[[r.get(k) for k in columns] for r in records]}


def small_summary(report,out):
    """Keep all value/quality tables; group8 selected rows stay in the full file."""
    legacy=copy.copy(report)
    stage=report.get('metric_spectral_curvature_reserve_stage')
    if stage is not None:legacy['metric_spectral_adaptive_stage']=stage
    result=previous.small_summary(legacy,out)
    if 'completed_adaptive_progress_retained' in report:
        result['completed_adaptive_progress_retained']=copy.deepcopy(report['completed_adaptive_progress_retained'])
    # These four dictionaries have identical keys. A column table is lossless
    # and avoids repeating long gate definitions four times in the brief.
    decision_names=[k for k in ['initial_current_constraints','initial_doubled_constraints',
        'final_full_grid_constraints','final_doubled_constraints'] if k in result]
    if decision_names:
        columns=list(dict.fromkeys(k for name in decision_names for k in result[name]))
        result['constraint_decision_table']={'names':decision_names,'columns':columns,
            'rows':[[result[name].get(k) for k in columns] for name in decision_names],
            'present_column_indices':[None if len(result[name])==len(columns)
                else [i for i,k in enumerate(columns) if k in result[name]] for name in decision_names]}
        for name in decision_names:result.pop(name)
    if stage is not None:
        sr=result.pop('metric_spectral_adaptive_stage')
        sr['curvature_proposal_floor']=floor_definition(report['configuration'])
        floors=[]
        for model in stage.get('solver',{}).get('models',[]):
            calls=[('primary',None,model.get('linear_program',{}))]+[
                ('SOC',i,item.get('linear_program',{})) for i,item in enumerate(model.get('corrections',[]))]
            for kind,index,lp in calls:
                diag=lp.get('curvature_proposal_diagnostics',{})
                for stat in diag.get('group_statistics',[]):
                    if stat['group']!=8:continue
                    row=copy.deepcopy(stat)
                    row.update(model=model['number'],kind=kind,correction=index,
                        coarse_pool_version=model.get('coarse_pool_version'),
                        fine_pool_version=model.get('fine_pool_version'))
                    floors.append(row)
        sr['group8_proposal_table']=_table(['model','kind','correction','coarse_pool_version','fine_pool_version',
            'selected_count','base_minimum','actual_point_minimum','legacy_target_minimum',
            'requested_target_minimum','floor_active_count','linear_achieved_minimum',
            'linear_legacy_target_margin_minimum','linear_target_margin_minimum','maximum_linear_floor_shortfall'],floors)
        values=[];snap=stage.get('checkpoint',{})
        for grid,records,key in [('coarse',snap.get('saved_coarse_trials',[]),'coarse_physical_evaluation'),
                ('fine',snap.get('saved_fine_trials',[]),'fine_value_evaluation')]:
            for record in records:
                d=record.get('decision',{})
                values.append({'grid':grid,'evaluation':record.get(key),
                    'physical_state_sha256':record.get('physical_state_sha256'),
                    'group8_minimum':d.get('curvature_scaled_row_minima',{}).get('curvature_plus_determinant'),
                    'direct_curvature':d.get('direct_maximum_absolute_principal_curvature'),
                    'direct_curvature_pass':d.get('independent_direct_curvature_pass'),
                    'hard_gate_pass':d.get('single_grid_hard_gate_pass')})
        sr['group8_value_table']=_table(['grid','evaluation','physical_state_sha256','group8_minimum',
            'direct_curvature','direct_curvature_pass','hard_gate_pass'],values)
        # One shared exact string dictionary; only repeated SHA text is encoded.
        hash_columns=[['model_table','linearized_at_physical_sha256'],
            ['correction_table','primary_trial_physical_sha256'],
            ['accepted_table','physical_state_sha256'],['group8_value_table','physical_state_sha256']]
        hashes=sorted({row[sr[name]['columns'].index(column)] for name,column in hash_columns
            for row in sr[name]['rows'] if row[sr[name]['columns'].index(column)] is not None})
        indices={value:i for i,value in enumerate(hashes)}
        for name,column in hash_columns:
            index=sr[name]['columns'].index(column)
            for row in sr[name]['rows']:
                if row[index] is not None:row[index]=indices[row[index]]
        sr['physical_state_sha256_dictionary']=hashes
        sr['physical_state_sha256_dictionary_columns']=hash_columns
        sr['complete_group8_selected_row_source']={
            'full_report_path':'metric_spectral_curvature_reserve_stage.solver.models',
            'primary_key':'linear_program.curvature_proposal_diagnostics.group8_selected_rows',
            'SOC_key':'corrections[].linear_program.curvature_proposal_diagnostics.group8_selected_rows',
            'integer_stack_ids_bound_to_the_recorded_coarse_and_fine_pool_versions':True,
            'all_four_groups_full_original_new_linear_margins_and_floor_shortfalls_retained':True}
        result['metric_spectral_curvature_reserve_stage']=sr
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
        'completed_adaptive_progress_retained':replay['completed_adaptive_progress_retained'],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'process_clock_scope':'main includes twenty-two-input replay; one initialization and one shared optimization clock'}
    def save(status):
        now=time.monotonic();snapshot=report.get('metric_spectral_curvature_reserve_stage',{}).get('checkpoint',{})
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=snapshot.get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('twenty-two-inputs-replayed-before-new-spectral-metric-recovery-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='fixed-cap58-new-target026-initialization'
        def checkpoint(snapshot):
            report['metric_spectral_curvature_reserve_stage']={'status':'current-two-grid-spectral-metric-recovery-checkpoint',
                'checkpoint':snapshot,'solver':{}}
            save('spectral-metric-recovery-last-accepted-physical-checkpoint')
        objective=CurvatureReserveSpectralMetricObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            twentysecond_report_decoded_sha256=bindings['completed_spectral_adaptive']['decoded_sha256'],
            learned_pool_replay=replay['learned_pool'],
            completed_adaptive_progress_retained=replay['completed_adaptive_progress_retained'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-twenty-second-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-twenty-second-eleven-group-fine-original-IDs',
            'source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        save('complete-two-grid-hard-cap-preflight-new-metric-target-not-assumed-feasible')
        report['phase']='one-shared-budget-metric-restoration-with-hard-curvature'
        stage=run_curvature_reserve_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['metric_spectral_curvature_reserve_stage']=stage
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
            'old_failed_delta_and_unfinished55_preserved':True,'no_old_optimizer_replayed':True}
        save('complete-two-grid-fixed-curvature-spectral-curvature-reserve-audit' if eligible
            else 'final-recheck-failed-do-not-use-as-new-physical-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('spectral-curvature-reserve-audit-error-last-checkpoint-preserved');return report


def artificial_twentytwo_inputs(directory):
    args,unused,unused_prior=previous.artificial_twentyone_inputs(directory)
    args.out=directory/'completed-artificial-spectral-adaptive.json'
    prepared=previous.prepare_run(args,artificial=True)
    report=previous.run_audit(prepared,args.out,artificial=True,evaluate_only=True)
    if report['status']!='complete-two-grid-fixed-curvature-spectral-adaptive-recovery-audit':
        raise ArithmeticError('small artificial twenty-second predecessor failed')
    args.spectral_adaptive_audit=args.out
    args.expected_spectral_adaptive_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    return args,prepared,report


def developer_check():
    targeted=reserve_check()
    with tempfile.TemporaryDirectory(prefix='metric-curvature-reserve-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder);args,old_prepared,prior=artificial_twentytwo_inputs(directory)
        args.out=directory/'curvature-reserve-artificial.json';start=time.monotonic()
        prepared=prepare_run(args,artificial=True,process_started=start)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=start,prepare_seconds=time.monotonic()-start)
        stage=report.get('metric_spectral_curvature_reserve_stage',{});snap=stage.get('checkpoint',{})
        old=prior['metric_spectral_adaptive_stage']['checkpoint']
        retained=all(set(old[name][-1]['row_indices']).issubset(snap.get(name,[{}])[0].get('row_indices',[]))
            for name in ['active_row_pool_history','fine_physical_row_pool_history'])
        same=report.get('final_state')==prior['final_state']
        complete_fine=snap.get('fine_physical_row_pool_history',[{}])[-1].get('group_order')==list(GROUPS)
        semantic=all(snap.get(name,[{}])[0].get('proposal_metric_branch_mapping')==PROPOSAL_BRANCHES
            for name in ['active_row_pool_history','fine_physical_row_pool_history'])
        no_lp=stage.get('solver',{}).get('linear_program_invocation_count')==0
        summary=json.loads(summary_path(args.out).read_text());size=summary_path(args.out).stat().st_size
        bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args);wrong.out=directory/'wrong-twenty-second-SHA.json'
        wrong.expected_spectral_adaptive_sha256='0'*64
        try:prepare_run(wrong,artificial=True);wrong_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text())
            wrong_sha=failure['phase']=='twenty-second-metric-recovery-byte-binding' and failure['new_solver_calls']==0
        bad=copy.deepcopy(prior)
        bad['metric_spectral_adaptive_stage']['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
        try:replay_adaptive_progress(old_prepared,bad,artificial=True);wrong_state=False
        except ValueError:wrong_state=True
        bad=copy.deepcopy(prior)
        fp=bad['metric_spectral_adaptive_stage']['checkpoint']['fine_physical_row_pool_history'][-1]
        first=fp['row_indices'][0];r,t,unused=curvature_grid(old_prepared[2])
        fp['added_row_indices']=[first]
        fp['added_original_grid_coordinates']=rows_api.fine_coordinates([first],r,np.arange(2*len(t))*np.pi/len(t))
        fp['added_original_grid_coordinates'][0]['theta']=123.
        try:replay_adaptive_progress(old_prepared,bad,artificial=True);wrong_coordinate=False
        except ValueError:wrong_coordinate=True
        # No geometry in this worst-case output test: 12 models / 84 trials,
        # 12 SOC records and 40 full-value records intentionally overfill the
        # simultaneous 12-LP/40-value budget to stress serialization only.
        stress=copy.deepcopy(report);s=stress['metric_spectral_curvature_reserve_stage'];cp=s['checkpoint']
        sample=copy.deepcopy(cp['selected_two_grid_physical_point'])
        s['solver']['models']=[];expected=[];expected_quality=[];expected_floor=[]
        for mi in range(12):
            model={'number':mi+1,'linearized_at_accepted_index':mi,
                'linearized_at_physical_sha256':sample['physical_state_sha256'],
                'coarse_pool_rows':4402+mi,'fine_pool_rows':3489+mi,
                'coarse_pool_version':mi+1,'fine_pool_version':mi+2,
                'result':'artificial-table-stress','linear_program':copy.deepcopy(targeted['primary']),
                'trials':[],'corrections':[]}
            for ti in range(7):
                trial={'kind':['primary-metric-short-step','metric-SOC-corrected-short-step',
                        'metric-SOC-parabolic-backtrack'][min(ti,2)],
                    'alpha_exact':str(Q(1,2**max(ti-1,0))),'attempt_status':'coarse-value-call-complete',
                    'accepted_as_next_iterate':ti==6,'accepted_index':mi+1 if ti==6 else None,
                    'coarse_decision':copy.deepcopy(sample['coarse']),'fine_decision':copy.deepcopy(sample['fine']),
                    'exact_binary64_physical_coefficients':sample['exact_binary64_physical_coefficients'],
                    'fine_violation_groups':{g:{'whole_grid':mi+j,'omitted':ti+j} for j,g in enumerate(GROUPS)}}
                if ti>=2:
                    trial['parabolic_curve']={'correction_weight_exact':str(Q(1,2**(2*(ti-1)))),
                        'linear_metric_slack_upper_bound':.01/(ti+1)}
                prediction=['basepoint-plus-J-step','same-actual-y-rows-plus-J-correction',
                    'parabolic-basepoint-linear-bound'][min(ti,2)]
                quality={'full_two_grid_actual_available':ti%2==0,'prediction':{'model_kind':prediction},
                    'predicted_metric_improvement':1e-5/(ti+1),
                    'actual_two_grid_eta_improvement':5e-6/(ti+1) if ti%2==0 else None,
                    'actual_to_predicted_ratio':.5 if ti%2==0 else None,
                    'coarse_only_upper_bound_on_actual_two_grid_ratio':.2 if ti%2 else None,
                    'actual_curvature_failure_grids':['fine'] if ti%3 else [],'request_shrink':ti%3==1}
                trial['scale_feedback']=quality
                expected_quality.append([mi+1,ti,quality['full_two_grid_actual_available'],prediction,
                    quality['predicted_metric_improvement'],quality['actual_two_grid_eta_improvement'],
                    quality['actual_to_predicted_ratio'],quality['coarse_only_upper_bound_on_actual_two_grid_ratio'],
                    quality['actual_curvature_failure_grids'],quality['request_shrink']])
                model['trials'].append(trial);expected.append((mi+1,ti,trial['kind'],trial['alpha_exact']))
            model['corrections']=[{'primary_trial_index':0,'primary_trial_physical_sha256':sample['physical_state_sha256'],
                'coarse_pool_version':mi+1,'fine_pool_version':mi+2,
                'linear_program':copy.deepcopy(targeted['correction'])}]
            model['trust_before_model']=float(Q('1/32000'))
            model['scale_feedback_update']={'trust_after_original_controller':float(Q('1/32000')),
                'next_trust':float(Q('1/64000')),'trigger_trial_indices':[1,4],
                'original_rejection_shrink_not_applied_twice':True}
            for kind,ci,lp in [('primary',None,model['linear_program']),('SOC',0,model['corrections'][0]['linear_program'])]:
                stat=next(v for v in lp['curvature_proposal_diagnostics']['group_statistics'] if v['group']==8)
                expected_floor.append([mi+1,kind,ci,mi+1,mi+2]+[stat[k] for k in [
                    'selected_count','base_minimum','actual_point_minimum','legacy_target_minimum',
                    'requested_target_minimum','floor_active_count','linear_achieved_minimum',
                    'linear_legacy_target_margin_minimum','linear_target_margin_minimum','maximum_linear_floor_shortfall']])
            s['solver']['models'].append(model)
        cp['accepted_iterates']=[]
        for i in range(13):
            point=copy.deepcopy(sample);point['accepted_index']=i;point['reason']={'kind':'artificial-stress','model':i}
            cp['accepted_iterates'].append(point)
        cp['saved_coarse_trials']=[];cp['saved_fine_trials']=[]
        expected_proposal=[];expected_group8=[]
        for grid,records,key in [('coarse',cp['saved_coarse_trials'],'coarse_physical_evaluation'),
                ('fine',cp['saved_fine_trials'],'fine_value_evaluation')]:
            for i in range(20):
                detail={'actual_full_spectral_proposal_slack':.007+i*1e-6,
                    'actual_full_old_Schur_slack':.014+i*1e-6,'actual_true_eta_maximum':.267+i*1e-6}
                d=copy.deepcopy(report['initial_current_constraints' if grid=='coarse' else 'initial_doubled_constraints'])
                records.append({key:i+1,'metric_proposal_diagnostic':detail,'decision':d,
                    'physical_state_sha256':sample['physical_state_sha256']})
                expected_proposal.append([grid,i+1,detail['actual_full_spectral_proposal_slack'],
                    detail['actual_full_old_Schur_slack'],detail['actual_true_eta_maximum']])
                expected_group8.append([grid,i+1,sample['physical_state_sha256'],
                    d['curvature_scaled_row_minima']['curvature_plus_determinant'],
                    d['direct_maximum_absolute_principal_curvature'],d['independent_direct_curvature_pass'],
                    d['single_grid_hard_gate_pass']])
        sp=directory/'stress-curvature-reserve.json';save_report(sp,stress)
        st=json.loads(summary_path(sp).read_text());stress_size=summary_path(sp).stat().st_size
        ss=st['metric_spectral_curvature_reserve_stage'];tb=ss['trial_table']
        for name,column in ss['physical_state_sha256_dictionary_columns']:
            index=ss[name]['columns'].index(column)
            for row in ss[name]['rows']:
                if row[index] is not None:row[index]=ss['physical_state_sha256_dictionary'][row[index]]
        values=[dict(zip(tb['columns'],row,strict=True)) for row in tb['rows']]
        dictionaries=ss['string_dictionaries']
        for value in values:
            if value['kind'] is not None:value['kind']=dictionaries['trial_table.kind'][value['kind']]
        tables=[(v['model'],v['trial'],v['kind'],v['alpha_exact']) for v in values]==expected
        proposal_table=ss['proposal_values_table']['rows']==expected_proposal
        decoded_quality=copy.deepcopy(ss['quality_table']['rows']);qi=ss['quality_table']['columns'].index('prediction')
        for row in decoded_quality:
            if row[qi] is not None:row[qi]=dictionaries['quality_table.prediction'][row[qi]]
        quality_table=decoded_quality==expected_quality
        floor_table=ss['group8_proposal_table']['rows']==expected_floor
        group8_values=ss['group8_value_table']['rows']==expected_group8
        decision_table=st['constraint_decision_table'];decisions_roundtrip=True
        for name,row,indices in zip(decision_table['names'],decision_table['rows'],decision_table['present_column_indices'],strict=True):
            use=range(len(decision_table['columns'])) if indices is None else indices
            restored={decision_table['columns'][i]:row[i] for i in use}
            decisions_roundtrip &= restored==stress[name]
        full_unchanged=json.loads(sp.read_text())==stress and st['full_report']['sha256']==hashlib.sha256(sp.read_bytes()).hexdigest()
        status=report['status'];error=report.get('error');refinement=report.get('same_parameter_Pi_refinement')
    passed=bool(targeted['passed'] and same and retained and complete_fine and semantic and no_lp and bound and size<95000
        and wrong_sha and wrong_state and wrong_coordinate and tables and proposal_table and quality_table
        and floor_table and group8_values and decisions_roundtrip and full_unchanged and stress_size<95000
        and status=='complete-two-grid-fixed-curvature-spectral-curvature-reserve-audit')
    return {'schema':SCHEMA+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,'no_Actions_environment_forged':True,
        'new_curvature_RHS_target_check':targeted,'full_main_status':status,'full_main_error':error,
        'same_state_g_b0_and_freeze':same,'all_old_pools_retained':retained,
        'fine_four_curvature_groups_enabled':complete_fine,'old_row_IDs_and_semantics_retained':semantic,
        'full_IO_artificial_path_has_no_LP':no_lp,'summary_byte_bound':bound,'summary_bytes':size,
        'wrong_twenty-second_SHA_saves_failure':wrong_sha,'changed_coefficients_rejected':wrong_state,
        'changed_fine_coordinates_rejected':wrong_coordinate,
        'stress_counts':{'models':12,'trials':84,'corrections':12,'accepted':13,'proposal_values':40,'group8_proposals':24},
        'stress_summary_bytes':stress_size,'all_trial_rows_roundtrip':tables,
        'all_proposal_diagnostic_rows_roundtrip':proposal_table,'full_report_unchanged':full_unchanged,
        'all_feedback_rows_roundtrip':quality_table,'all_group8_proposal_rows_roundtrip':floor_table,
        'all_group8_value_rows_roundtrip':group8_values,'all_four_complete_decisions_roundtrip':decisions_roundtrip,
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
    if report['status']!='complete-two-grid-fixed-curvature-spectral-curvature-reserve-audit':raise SystemExit(1)



if __name__=='__main__':main()

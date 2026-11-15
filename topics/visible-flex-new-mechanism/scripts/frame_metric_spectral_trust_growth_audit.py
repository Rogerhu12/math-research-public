#!/usr/bin/env python3
"""Twenty-four-input recovery with conservative next-model proposal growth.

Only the radius controller gains a conditional growth rule. The saved c010
state, fixed physical primary cost, all rows, floor, SOC and true gates remain. No old optimizer or candidate geometry is replayed locally.
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
from frame_metric_spectral_trust_growth import (POLICY,
    GrowingTrustSpectralMetricObjective,run_growing_trust_recovery,
    configuration as growth_configuration,implementation_hashes as growth_hashes,
    developer_check as growth_check,penalty_definition,growth_definition,adaptive_definition)
from frame_metric_spectral_curvature_reserve import floor_definition
from frame_curvature_soc_metric_reserve_audit import exact_vector
import frame_metric_spectral_physical_penalty_audit as previous
import frame_metric_budget_restoration_rows as rows_api

SCHEMA='same-g-spectral-metric-conservative-trust-growth-audit-v1'
PRIOR_RUN='43676765171'
PRIOR_SOURCE='ca4e52869123fa97df4560232a03f9529cf05332'
PRIOR_FINAL='c01081847002993c71ca7545b4baae6a1bd94422457b21871fb45cd01d072071'
METRIC_TARGET='13/50'
CURVATURE_CAP='58'
INPUTS=previous.INPUTS+['spectral_physical_penalty_audit']
SHA_NAMES=previous.SHA_NAMES+['spectral-physical-penalty']
coefficients=previous.coefficients
curvature_grid=previous.curvature_grid
summary_path=previous.summary_path



def implementation_hashes():
    result=previous.implementation_hashes();result.update(growth_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result



def configuration(base,*,artificial=False):
    if not artificial and any(Q(base[k])!=Q(value) for k,value in [
        ('previous_qualified_metric_budget_exact','167/625'),('fixed_metric_budget_exact',METRIC_TARGET),
        ('fixed_hard_curvature_cap_exact',CURVATURE_CAP)]):
        raise ValueError('preserve the actual old/new metric budgets and curvature58')
    return growth_configuration(base)



def replay_completed_progress(prepared,prior,*,artificial=False):
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prior.get('schema')!=previous.SCHEMA
            or prior.get('status')!='complete-two-grid-fixed-curvature-spectral-physical-penalty-audit'
            or bool(prior.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed twenty-fourth metric-recovery report required')
    if prior.get('source_files_sha256')!=previous.implementation_hashes() or prior.get('configuration')!=old_cfg:
        raise ValueError('twenty-fourth implementation/configuration differs')
    if not artificial and (str(prior.get('github_run_id'))!=PRIOR_RUN or prior.get('github_sha')!=PRIOR_SOURCE):
        raise ValueError('twenty-fourth actual source/run differs')
    for name,binding in bindings.items():
        recorded=prior.get('exact_input_storage',{}).get(name,{})
        if any(recorded.get(k)!=binding.get(k) for k in
                ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']):
            raise ValueError('twenty-fourth predecessor byte binding differs: '+name)
    if (prior.get('initial_state')!=state_record(problem,old_initial) or prior.get('input_replay')!=old_replay
            or prior.get('old_optimizer_calls_this_run')!=0
            or not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_failed_metric_auxiliary_delta')!=tenth['selected_raw_auxiliary_delta']):
        raise ValueError('twenty-fourth complete original state/history differs')
    stage=prior['metric_spectral_physical_penalty_stage'];snap=stage['checkpoint']
    point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('twenty-fourth complete accepted point missing')
    state=exact_vector(point.get('exact_binary64_physical_coefficients'),problem.nunknown)
    if (state.tolist()!=point.get('physical_parameter_coefficients_binary64')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prior.get('final_state')!=state_record(problem,state)):
        raise ValueError('twenty-fourth exact coefficient/canonical state mismatch')
    if not artificial and point['physical_state_sha256']!=PRIOR_FINAL:
        raise ValueError('start only from the qualified savedc010 physical point')
    accepted=snap.get('accepted_iterates',[])
    if (not accepted or accepted[-1]!=point or problem.metric_model(state)!=problem.metric_model(old_initial)
            or old_replay.get('fixed_b0_definition_sha256')!=digest(problem.height_base_definition)):
        raise ValueError('twenty-fourth selected accepted point or complete metric mismatch')
    validation=prior.get('final_selection_validation',{})
    if not validation.get('both_value_grids_hard_and_old_metric_pass'):
        raise ValueError('twenty-fourth true two-grid hard/old-metric gates failed')
    if not artificial and (np.array_equal(state,old_initial) or len(accepted)!=12
            or validation.get('actual_eta_decrease',0)<=0 or validation.get('new_metric_target_qualified_on_both_grids') is not False):
        raise ValueError('preserve all eleven actual accepted steps and unfinished026, not an unsaved trial')
    for key in ['final_full_grid_constraints','final_doubled_constraints']:
        d=prior.get(key,{})
        if not d.get('single_grid_admissible_recovery_point'):
            raise ValueError('twenty-fourth final actual hard or old metric failed')
        if any(d.get(k)!=old_cfg[k] for k in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
                'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']):
            raise ValueError('twenty-fourth original gate definition differs')
    radial,theta,grid=curvature_grid(tenth)
    if prior.get('full_value_sampling_definition')!=grid:
        raise ValueError('twenty-fourth complete value grid differs')
    h=snap.get('active_row_pool_history',[]);fh=snap.get('fine_physical_row_pool_history',[])
    if not h or not fh:raise ValueError('twenty-fourth learned pool histories missing')
    coarse,fine=h[-1],fh[-1];ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,total,rule,cap in [
        (coarse,ci,11*len(radial)*len(theta),'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows']),
        (fine,fi,22*len(radial)*len(theta),'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'])]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=list(GROUPS)
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap):
            raise ValueError('twenty-fourth complete learned ID/group/hash/layout mismatch')
    if not set(old_coarse).issubset(ci) or not set(old_fine).issubset(fi):
        raise ValueError('twenty-fourth dropped earlier learned rows')
    added=fine.get('added_row_indices');fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added) or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=rows_api.fine_coordinates(added,radial,fine_theta)):
        raise ValueError('twenty-fourth added fine row original coordinates differ')
    if not artificial and (len(ci)!=4414 or len(fi)!=3790):
        raise ValueError('retain exactly all4414/all3790 published learned rows before adding new witnesses')
    locations={}
    for d in [prior['final_doubled_constraints']]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('twenty-fourth recorded peak is not finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    retained={'source_run':prior.get('github_run_id'),'source_commit':prior.get('github_sha'),
        'status':stage['status'],'old_newtarget026_was_not_reached':not bool(validation.get('new_metric_target_qualified_on_both_grids')),
        'old_actual_eta_decrease':validation.get('actual_eta_decrease'),
        'old_accepted_count':len(accepted),'old_linear_programs':stage.get('solver',{}).get('linear_program_invocation_count'),
        'completed_attempt_and_all_failed_trials_not_relabelled':True,
        'new_growth_controller_changes_no_old_report_rows_cost_or_actual_gates':True,
        'original_twelve_LP_exit_not_relabelled_as_target_success':True,
        'old_SOC_time_limit_not_relabelled_as_infeasibility':True}
    learned={'schema':'twenty-fourth-metric-recovery-learned-pools-v1','source_run':prior.get('github_run_id'),
        'source_commit':prior.get('github_sha'),'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'all_preceding_integer_row_ids_and_coordinates_preserved':True,
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'groups2_to10_have_original_values_and_derivatives':True}
    cfg=configuration(old_cfg,artificial=artificial)
    replay={'schema':'twenty-four-input-spectral-physical-penalty-replay-v1','twenty_three_input_replay':old_replay,
        'canonical_physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),'physical_parameter_count':problem.nunknown,
        'same_saved_final_coefficients_g_b0_space_and_value_grids':True,
        'learned_pool':learned,'completed_physical_penalty_progress_retained':retained,
        'known_fine_metric_locations':list(locations.values()),
        'explicit_new_constraint_definition':{'fixed_hard_curvature_cap_exact':CURVATURE_CAP,
            'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
            'metric_restoration_target_exact':cfg['fixed_metric_budget_exact'],
            'next_model_trust_growth_policy':POLICY,'proposal_epsilon_exact':EPSILON_EXACT,
            'adaptive_scale_definition':adaptive_definition(cfg),
            'curvature_proposal_floor_definition':floor_definition(cfg),
            'primary_physical_step_cost_definition':penalty_definition(cfg),
            'conservative_trust_growth_definition':growth_definition(cfg),
            'proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
            'actual_two_grid_eta_Schur_curvature_and_all_physical_gates_unchanged':True,
            'artificial_large_metric_budget_for_IO_only':bool(cfg.get('artificial_large_metric_budget_for_IO_only')),
            'physical_model_unchanged':True,'new_target_not_assumed_feasible':True,
            'original12LP40value120seconds_shared_budget':True},
        'old_optimizer_calls_replayed':0,'no_research_geometry_in_structural_replay':True}
    return (problem,state,gate,lower,upper,source_cfg,cfg),replay,np.asarray(ci,np.int64),np.asarray(fi,np.int64)



def prepare_run(args,*,artificial=False,process_started=None):
    start=time.monotonic();process_started=start if process_started is None else process_started
    phase='twenty-three-input-prior-start-replay';bindings={}
    try:
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        old=previous.prepare_run(args,artificial=artificial,process_started=process_started)
        bindings=copy.deepcopy(old[1]);phase='twenty-fourth-metric-recovery-byte-binding'
        if args.spectral_physical_penalty_audit is None or args.expected_spectral_physical_penalty_sha256 is None:
            raise ValueError('twenty-fourth complete report and decoded SHA required')
        prior,raw,binding=read_input(args.spectral_physical_penalty_audit,args.expected_spectral_physical_penalty_sha256)
        phase='twenty-fourth-saved-qualified-state-and-all-learned-pools'
        restored,replay,coarse,fine=replay_completed_progress(old,prior,artificial=artificial)
        bindings['completed_spectral_physical_penalty']=binding
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
    """Keep the prior lossless native tables and add compact growth records."""
    legacy=copy.copy(report);stage=report.get('metric_spectral_trust_growth_stage')
    if stage is not None:legacy['metric_spectral_physical_penalty_stage']=stage
    result=copy.deepcopy(previous.small_summary(legacy,out))
    if 'completed_physical_penalty_progress_retained' in report:
        result['completed_physical_penalty_progress_retained']=copy.deepcopy(report['completed_physical_penalty_progress_retained'])
    if stage is not None:
        sr=result.pop('metric_spectral_physical_penalty_stage')
        sr['conservative_trust_growth']=growth_definition(report['configuration'])
        sr['adaptive_trust_policy']=adaptive_definition(report['configuration'])
        records=[];names=[]
        for model in stage.get('solver',{}).get('models',[]):
            update=model.get('scale_feedback_update',{});d=update.get('conservative_growth',{})
            if d:
                if not names:names=list(d['checks'])
                if list(d['checks'])!=names:raise ValueError('growth condition order changed within report')
            records.append(dict(d,model=model['number'],
                condition_values=[d['checks'][k] for k in names] if d else None,
                trust_after_unchanged_shrink_rule=update.get('trust_after_unchanged_shrink_rule'),
                next_trust=update.get('next_trust')))
        sr['growth_condition_columns']=names
        sr['growth_table']=_table(['model','streak_before','streak_after','qualifying_model',
            'condition_values','complete_ratio','actual_step_norm_over_radius',
            'new_coarse_rows','new_fine_rows','grew_for_next_model','qualified_pair_at_cap',
            'trust_after_unchanged_shrink_rule','next_trust'],records)
        sr['growth_definition_applies_to_every_model_row']=True
        sr['complete_group8_selected_row_source']['full_report_path']='metric_spectral_trust_growth_stage.solver.models'
        result['metric_spectral_trust_growth_stage']=sr
        # These are identical definitions, not trial data. Keep each full
        # definition in the same JSON and use explicit lossless local paths.
        for key,source in [
            ('adaptive_scale_definition','adaptive_trust_policy'),
            ('curvature_proposal_floor_definition','curvature_proposal_floor'),
            ('primary_physical_step_cost_definition','primary_physical_step_cost'),
            ('conservative_trust_growth_definition','conservative_trust_growth')]:
            target=result.get('new_constraint_role_definition',{})
            if target.get(key)==sr.get(source) and source in sr:
                target[key]={'same_value_as_summary_path':['metric_spectral_trust_growth_stage',source]}
        policy=sr['adaptive_trust_policy']
        if policy.get('next_model_growth')==sr['conservative_trust_growth']:
            policy['next_model_growth']={'same_value_as_summary_path':
                ['metric_spectral_trust_growth_stage','conservative_trust_growth']}
        result['identical_definition_reference_format']='a sole same_value_as_summary_path object resolves recursively inside this JSON; no external data and no trial rows removed'
    return result


def resolve_summary_definition_references(summary):
    def value_at(path):
        value=summary
        for key in path:value=value[key]
        return value
    def resolve(value,active=()):
        if isinstance(value,dict) and set(value)=={'same_value_as_summary_path'}:
            path=tuple(value['same_value_as_summary_path'])
            if path in active:raise ValueError('cyclic summary definition reference')
            return resolve(value_at(path),active+(path,))
        if isinstance(value,dict):return {k:resolve(v,active) for k,v in value.items()}
        if isinstance(value,list):return [resolve(v,active) for v in value]
        return value
    return resolve(summary)


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
        'completed_physical_penalty_progress_retained':replay['completed_physical_penalty_progress_retained'],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'process_clock_scope':'main includes twenty-four-input replay; one initialization and one shared optimization clock'}
    def save(status):
        now=time.monotonic();snapshot=report.get('metric_spectral_trust_growth_stage',{}).get('checkpoint',{})
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
            report['metric_spectral_trust_growth_stage']={'status':'current-two-grid-spectral-metric-recovery-checkpoint',
                'checkpoint':snapshot,'solver':{}}
            save('spectral-metric-recovery-last-accepted-physical-checkpoint')
        objective=GrowingTrustSpectralMetricObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            twentyfourth_report_decoded_sha256=bindings['completed_spectral_physical_penalty']['decoded_sha256'],
            learned_pool_replay=replay['learned_pool'],
            completed_physical_penalty_progress_retained=replay['completed_physical_penalty_progress_retained'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-twenty-fourth-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-twenty-fourth-eleven-group-fine-original-IDs',
            'source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        save('complete-two-grid-hard-cap-preflight-new-metric-target-not-assumed-feasible')
        report['phase']='one-shared-budget-metric-restoration-with-hard-curvature'
        stage=run_growing_trust_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['metric_spectral_trust_growth_stage']=stage
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
        save('complete-two-grid-fixed-curvature-spectral-trust-growth-audit' if eligible
            else 'final-recheck-failed-do-not-use-as-new-physical-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('spectral-trust-growth-audit-error-last-checkpoint-preserved');return report



def artificial_twentyfour_inputs(directory):
    args,unused,unused_prior=previous.artificial_twentythree_inputs(directory)
    args.out=directory/'completed-artificial-spectral-physical-penalty.json'
    prepared=previous.prepare_run(args,artificial=True)
    report=previous.run_audit(prepared,args.out,artificial=True,evaluate_only=True)
    if report['status']!='complete-two-grid-fixed-curvature-spectral-physical-penalty-audit':
        raise ArithmeticError('small artificial twenty-fourth predecessor failed')
    args.spectral_physical_penalty_audit=args.out
    args.expected_spectral_physical_penalty_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    return args,prepared,report



def developer_check():
    targeted=growth_check()
    with tempfile.TemporaryDirectory(prefix='metric-trust-growth-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder);args,old_prepared,prior=artificial_twentyfour_inputs(directory)
        args.out=directory/'trust-growth-artificial.json';start=time.monotonic()
        prepared=prepare_run(args,artificial=True,process_started=start)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=start,prepare_seconds=time.monotonic()-start)
        stage=report.get('metric_spectral_trust_growth_stage',{});snap=stage.get('checkpoint',{})
        old=prior['metric_spectral_physical_penalty_stage']['checkpoint']
        retained=all(set(old[name][-1]['row_indices']).issubset(snap.get(name,[{}])[0].get('row_indices',[]))
            for name in ['active_row_pool_history','fine_physical_row_pool_history'])
        same=report.get('final_state')==prior['final_state']
        complete_fine=snap.get('fine_physical_row_pool_history',[{}])[-1].get('group_order')==list(GROUPS)
        semantic=all(snap.get(name,[{}])[0].get('proposal_metric_branch_mapping')==PROPOSAL_BRANCHES
            for name in ['active_row_pool_history','fine_physical_row_pool_history'])
        no_lp=stage.get('solver',{}).get('linear_program_invocation_count')==0
        summary=json.loads(summary_path(args.out).read_text());size=summary_path(args.out).stat().st_size
        bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args);wrong.out=directory/'wrong-twenty-fourth-SHA.json'
        wrong.expected_spectral_physical_penalty_sha256='0'*64
        try:prepare_run(wrong,artificial=True);wrong_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text())
            wrong_sha=failure['phase']=='twenty-fourth-metric-recovery-byte-binding' and failure['new_solver_calls']==0
        bad=copy.deepcopy(prior)
        bad['metric_spectral_physical_penalty_stage']['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
        try:replay_completed_progress(old_prepared,bad,artificial=True);wrong_state=False
        except ValueError:wrong_state=True
        bad=copy.deepcopy(prior)
        fp=bad['metric_spectral_physical_penalty_stage']['checkpoint']['fine_physical_row_pool_history'][-1]
        first=fp['row_indices'][0];r,t,unused=curvature_grid(old_prepared[2])
        fp['added_row_indices']=[first]
        fp['added_original_grid_coordinates']=rows_api.fine_coordinates([first],r,np.arange(2*len(t))*np.pi/len(t))
        fp['added_original_grid_coordinates'][0]['theta']=123.
        try:replay_completed_progress(old_prepared,bad,artificial=True);wrong_coordinate=False
        except ValueError:wrong_coordinate=True
        # No geometry in this worst-case output test: 12 models / 84 trials,
        # 12 SOC records and 40 full-value records intentionally overfill the
        # simultaneous 12-LP/40-value budget to stress serialization only.
        stress=copy.deepcopy(report);s=stress['metric_spectral_trust_growth_stage'];cp=s['checkpoint']
        sample=copy.deepcopy(cp['selected_two_grid_physical_point'])
        s['solver']['models']=[];expected=[];expected_quality=[];expected_floor=[];expected_penalty=[];expected_growth=[]
        for mi in range(12):
            model={'number':mi+1,'linearized_at_accepted_index':mi,
                'linearized_at_physical_sha256':sample['physical_state_sha256'],
                'coarse_pool_rows':4407+mi,'fine_pool_rows':3711+mi,
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
            model['trust_before_model']=float(Q('1/64000'))
            model['scale_feedback_update']={'trust_after_original_controller':float(Q('1/64000')),
                'next_trust':float(Q('1/128000')),'trigger_trial_indices':[1,4],
                'original_rejection_shrink_not_applied_twice':True}
            growth=copy.deepcopy(targeted['second_feedback']['conservative_growth'])
            growth.update(streak_before=mi%2,streak_after=1-mi%2,qualifying_model=mi%3==0,
                complete_ratio=.8+mi/1000,actual_step_norm_over_radius=1.,
                new_coarse_rows=mi,new_fine_rows=mi+1,grew_for_next_model=mi%2==0,
                qualified_pair_at_cap=False)
            model['scale_feedback_update'].update(conservative_growth=growth,
                trust_after_unchanged_shrink_rule=float(Q('1/64000')))
            expected_growth.append([mi+1]+[growth.get(k) for k in ['streak_before','streak_after','qualifying_model']]
                +[list(growth['checks'].values())]+[growth.get(k) for k in ['complete_ratio',
                'actual_step_norm_over_radius','new_coarse_rows','new_fine_rows','grew_for_next_model','qualified_pair_at_cap']]
                +[float(Q('1/64000')),float(Q('1/128000'))])
            for kind,ci,lp in [('primary',None,model['linear_program']),('SOC',0,model['corrections'][0]['linear_program'])]:
                stat=next(v for v in lp['curvature_proposal_diagnostics']['group_statistics'] if v['group']==8)
                expected_floor.append([mi+1,kind,ci,mi+1,mi+2]+[stat[k] for k in [
                    'selected_count','base_minimum','actual_point_minimum','legacy_target_minimum',
                    'requested_target_minimum','floor_active_count','linear_achieved_minimum',
                    'linear_legacy_target_margin_minimum','linear_target_margin_minimum','maximum_linear_floor_shortfall']])
            d=model['linear_program']['primary_step_cost_diagnostic']
            expected_penalty.append([mi+1]+[d.get(k) for k in ['current_trust_evaluated',
                'effective_normalized_weight_evaluated','rho_bias_bound_if_exact_weighted_optimum_evaluated',
                'returned_LP_norm_auxiliary','actual_physical_box_normalized_step_norm',
                'returned_primary_step_cost','old_constant_normalized_cost_at_the_same_returned_auxiliary',
                'returned_weighted_objective']])
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
        sp=directory/'stress-trust-growth.json';save_report(sp,stress)
        st=json.loads(summary_path(sp).read_text());stress_size=summary_path(sp).stat().st_size
        expanded=resolve_summary_definition_references(st)
        definition_references=bool(expanded['new_constraint_role_definition']==stress['new_constraint_role_definition']
            and expanded['metric_spectral_trust_growth_stage']['adaptive_trust_policy']==adaptive_definition(stress['configuration']))
        ss=st['metric_spectral_trust_growth_stage'];tb=ss['trial_table']
        for name,column in ss['physical_state_sha256_dictionary_columns']:
            index=ss[name]['columns'].index(column)
            for row in ss[name]['rows']:
                if row[index] is not None:row[index]=ss['physical_state_sha256_dictionary'][row[index]]
        values=[dict(zip(tb['columns'],row,strict=True)) for row in tb['rows']]
        dictionaries=ss['string_dictionaries']
        for value in values:
            if value['kind'] is not None:value['kind']=dictionaries['trial_table.kind'][value['kind']]
            if value['physical_coefficients_sha256'] is not None:
                value['physical_coefficients_sha256']=dictionaries['trial_table.physical_coefficients_sha256'][value['physical_coefficients_sha256']]
        tables=[(v['model'],v['trial'],v['kind'],v['alpha_exact']) for v in values]==expected
        coefficient_hashes=all(v['physical_coefficients_sha256']==digest(sample['exact_binary64_physical_coefficients']) for v in values)
        proposal_table=ss['proposal_values_table']['rows']==expected_proposal
        decoded_quality=copy.deepcopy(ss['quality_table']['rows']);qi=ss['quality_table']['columns'].index('prediction')
        for row in decoded_quality:
            if row[qi] is not None:row[qi]=dictionaries['quality_table.prediction'][row[qi]]
        quality_table=decoded_quality==expected_quality
        floor_table=ss['group8_proposal_table']['rows']==expected_floor
        penalty_table=ss['primary_step_cost_table']['rows']==expected_penalty
        growth_table=ss['growth_table']['rows']==expected_growth
        group8_values=ss['group8_value_table']['rows']==expected_group8
        decision_table=st['constraint_decision_table'];decisions_roundtrip=True
        for name,row,indices in zip(decision_table['names'],decision_table['rows'],decision_table['present_column_indices'],strict=True):
            use=range(len(decision_table['columns'])) if indices is None else indices
            restored={decision_table['columns'][i]:row[i] for i in use}
            decisions_roundtrip &= restored==stress[name]
        full_unchanged=json.loads(sp.read_text())==stress and st['full_report']['sha256']==hashlib.sha256(sp.read_bytes()).hexdigest()
        status=report['status'];error=report.get('error');refinement=report.get('same_parameter_Pi_refinement')
    passed=bool(targeted['passed'] and same and retained and complete_fine and semantic and no_lp and bound and size<95000
        and wrong_sha and wrong_state and wrong_coordinate and tables and coefficient_hashes and proposal_table and quality_table
        and floor_table and penalty_table and growth_table and definition_references and group8_values and decisions_roundtrip and full_unchanged and stress_size<95000
        and status=='complete-two-grid-fixed-curvature-spectral-trust-growth-audit')
    return {'schema':SCHEMA+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,'no_Actions_environment_forged':True,
        'new_conservative_growth_check':targeted,'full_main_status':status,'full_main_error':error,
        'same_state_g_b0_and_freeze':same,'all_old_pools_retained':retained,
        'fine_four_curvature_groups_enabled':complete_fine,'old_row_IDs_and_semantics_retained':semantic,
        'full_IO_artificial_path_has_no_LP':no_lp,'summary_byte_bound':bound,'summary_bytes':size,
        'wrong_twenty-fourth_SHA_saves_failure':wrong_sha,'changed_coefficients_rejected':wrong_state,
        'changed_fine_coordinates_rejected':wrong_coordinate,
        'stress_counts':{'models':12,'trials':84,'corrections':12,'accepted':13,'proposal_values':40,'group8_proposals':24},
        'stress_summary_bytes':stress_size,'all_trial_rows_roundtrip':tables,
        'all_trial_exact_coefficient_hashes_roundtrip':coefficient_hashes,
        'all_proposal_diagnostic_rows_roundtrip':proposal_table,'full_report_unchanged':full_unchanged,
        'all_feedback_rows_roundtrip':quality_table,'all_group8_proposal_rows_roundtrip':floor_table,
        'all_definition_references_roundtrip':definition_references,'all_growth_feedback_rows_roundtrip':growth_table,'all_primary_cost_rows_roundtrip':penalty_table,'all_group8_value_rows_roundtrip':group8_values,'all_four_complete_decisions_roundtrip':decisions_roundtrip,
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
    if report['status']!='complete-two-grid-fixed-curvature-spectral-trust-growth-audit':raise SystemExit(1)



if __name__=='__main__':main()

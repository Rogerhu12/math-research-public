#!/usr/bin/env python3
"""Consume the saved target60 SOC success with a smaller inherited step scale.

The frozen SOC controller, geometry, 163 parameters and all original gates are
unchanged. Only the declared initial primary trust is 1/1000 instead of 1/100.
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
from frame_curvature_soc_steps import SOCObjective, run_soc_steps
import frame_curvature_soc_steps_audit as previous

SCHEMA='same-g-inherited-primary-scale-SOC-curvature-audit-v1'
POLICY='exact-one-thousandth-primary-scale-preserved-between-SOC-targets-v1'
PRIOR_RUN='43660745541'
PRIOR_SOURCE='3fd3bbe8b281cd729b047984bbe46645507b0b0d'
PRIOR_FINAL_PHYSICAL_SHA='b03c522ade58ec0c7a5a4bfb3af971a430adabf080cf0d8cdeabab4c0c3b4cb5'
TARGETS=('55','50','45','40','35','30','25','20','16')
TRUST='1/1000'
INPUTS=previous.INPUTS+['soc_audit']
SHA_NAMES=previous.SHA_NAMES+['soc']
coefficients=previous.coefficients
curvature_grid=previous.curvature_grid
summary_path=previous.summary_path


def implementation_hashes():
    result=previous.implementation_hashes()
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def configuration(base):
    cfg=copy.deepcopy(base)
    cfg.update(fixed_curvature_target_exact=TARGETS[0],curvature_target_schedule_exact=list(TARGETS),
        initial_trust_box_fraction_exact=TRUST,primary_step_scale_policy=POLICY,
        primary_scale_not_reset_when_target_changes=True,
        old_successful_SOC_controller_and_all_original_gates_unchanged=True)
    return cfg


class InheritedScaleObjective(SOCObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.evaluation_definition.update(primary_step_scale_policy=POLICY,
            inherited_primary_trust_exact=TRUST,implementation_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)
    def accepted_point(self,state,coarse,fine,reason):
        if not self.accepted_iterates and reason.get('kind')=='saved-d1ca5f-both-grid-accepted-SOC-start':
            reason={'kind':'saved-b03c-target60-SOC-success-inherited-scale-start',
                'source_run':PRIOR_RUN,'primary_trust_exact':TRUST}
        return super().accepted_point(state,coarse,fine,reason)


def exact_vector(values,n):
    if not isinstance(values,list) or len(values)!=n:
        raise ValueError('complete exact binary64 vector required')
    result=np.asarray([float(Q(x)) for x in values],float)
    if not np.all(np.isfinite(result)) or coefficients(result)!=values:
        raise ValueError('stored exact coefficients are not their declared binary64 values')
    return result


def successful_primary_scale(stage,point,lower,upper,n):
    """Read saved primary coefficients only; no geometry or optimization."""
    model_number=point['reason']['model']
    model=stage['solver']['models'][model_number-1]
    if model.get('number')!=model_number or model.get('result')!='accepted-SOC-corrected-two-grid-step':
        raise ValueError('successful source primary/SOC model is not present')
    p=exact_vector(model.get('exact_binary64_proposed_step'),n)
    alpha=Q(point['reason']['alpha_exact']); step=float(alpha)*p
    width=np.asarray(upper)-np.asarray(lower)
    norm=float(np.max(abs(step)/np.where(width>0,width,1.)))
    correction=model['corrections'][-1]; lp=correction['linear_program']
    if (not lp.get('LP_invoked') or not lp.get('success')
            or lp.get('primary_box_normalized_step_infinity_norm')!=norm
            or not Q(TRUST)<Q.from_float(norm)):
        raise ValueError('fixed new primary scale must be tied to the saved successful primary norm')
    return dict(source_successful_model_number=model_number,source_alpha_exact=str(alpha),
        source_primary_norm_exact_binary64=str(Q.from_float(norm)),source_primary_norm_evaluated=norm,
        source_primary_maximum_absolute_step=float(np.max(abs(step))),
        source_primary_step_exact_coefficients_sha256=digest(model['exact_binary64_proposed_step']),
        chosen_scale_smaller_than_saved_successful_primary_norm=True,
        chosen_scale_to_saved_norm_exact=str(Q(TRUST)/Q.from_float(norm)),
        source_SOC_maximum_absolute_correction=lp['maximum_absolute_correction'])


def replay_soc_success(prepared,prior,*,artificial=False):
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prior.get('schema')!=previous.SCHEMA
            or prior.get('status')!='complete-two-grid-bounded-SOC-curvature-audit'
            or bool(prior.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('the matching completed sixteenth SOC report is required')
    if prior.get('source_files_sha256')!=previous.implementation_hashes() or prior.get('configuration')!=old_cfg:
        raise ValueError('sixteenth frozen implementation/configuration differs')
    if not artificial and (str(prior.get('github_run_id'))!=PRIOR_RUN or prior.get('github_sha')!=PRIOR_SOURCE):
        raise ValueError('sixteenth source or run differs')
    for name,binding in bindings.items():
        recorded=prior.get('exact_input_storage',{}).get(name,{})
        if any(recorded.get(key)!=binding.get(key) for key in
                ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']):
            raise ValueError('sixteenth preceding input byte binding differs: '+name)
    if (prior.get('initial_state')!=state_record(problem,old_initial) or prior.get('input_replay')!=old_replay
            or prior.get('old_optimizer_calls_this_run')!=0 or not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_failed_metric_auxiliary_delta')!=tenth['selected_raw_auxiliary_delta']):
        raise ValueError('sixteenth original state/history binding differs')
    stage=prior['mixed_grid_short_step_stage']; snap=stage['checkpoint']; point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('sixteenth complete accepted physical point missing')
    state=exact_vector(point.get('exact_binary64_physical_coefficients'),problem.nunknown)
    if (state.tolist()!=point.get('physical_parameter_coefficients_binary64')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prior.get('final_state')!=state_record(problem,state)):
        raise ValueError('sixteenth full coefficients or canonical state differs')
    if not artificial and point['physical_state_sha256']!=PRIOR_FINAL_PHYSICAL_SHA:
        raise ValueError('the real continuation must consume the saved b03c point')
    accepted=snap.get('accepted_iterates',[])
    if not accepted or accepted[-1]!=point or problem.metric_model(state)!=problem.metric_model(old_initial):
        raise ValueError('selected SOC point or complete fixed metric differs')
    validation=prior.get('final_selection_validation',{})
    if not validation.get('both_value_grids_physical_gate_pass'):
        raise ValueError('sixteenth final two-grid physical validation failed')
    if not artificial and (stage.get('completed_targets_exact')!=['60'] or stage.get('active_stage_target_exact')!='55'
            or validation.get('last_active_target_reached') is not False
            or point.get('reason',{}).get('kind')!='SOC-corrected-short-step'):
        raise ValueError('preserve actual target60 SOC success and unfinished55 history')
    for key in ['final_full_grid_constraints','final_doubled_constraints']:
        d=prior.get(key,{})
        if not d.get('eligible_under_fixed_metric_and_physical_gates'):
            raise ValueError('sixteenth original final physical gate failed')
        if any(d.get(field)!=old_cfg[field] for field in
                ['fixed_metric_budget_exact','hard_strip_half_width_exact','mirror_target_exact']):
            raise ValueError('sixteenth physical gate was changed')
    radial,theta,grid=curvature_grid(tenth)
    if prior.get('full_value_sampling_definition')!=grid:
        raise ValueError('sixteenth complete value grid differs')
    history=snap.get('active_row_pool_history',[]); fhistory=snap.get('fine_physical_row_pool_history',[])
    if not history or not fhistory:raise ValueError('sixteenth learned pools missing')
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
            raise ValueError('sixteenth original pool index/group/hash differs')
    if not set(old_coarse).issubset(ci) or not set(old_fine).issubset(fi):
        raise ValueError('sixteenth discarded an already learned coarse or fine row')
    added=fine.get('added_row_indices'); ft=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added) or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=fine_row_coordinates(added,radial,ft)):
        raise ValueError('sixteenth fine original coordinates differ')
    evidence={'chosen_new_primary_trust_exact':TRUST,'old_initial_primary_trust_exact':old_cfg['initial_trust_box_fraction_exact'],
        'source_has_an_actual_SOC_accepted_step':not artificial,'physical_state_not_changed_by_scale_choice':True,
        'the_scale_is_a_fixed_design_constant_not_reoptimized_on_current_geometry':True}
    if not artificial:
        evidence.update(successful_primary_scale(stage,point,lower,upper,problem.nunknown))
    locations={}
    for d in [prior['final_doubled_constraints']]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('sixteenth fine metric location not finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    learned={'schema':'sixteenth-SOC-complete-retained-two-pools-v1','source_run':prior.get('github_run_id'),
        'source_commit':prior.get('github_sha'),'source_coarse_rows':len(ci),'source_coarse_row_indices_sha256':digest(ci),
        'source_fine_rows':len(fi),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'all_preceding_coarse_and_fine_rows_retained':True}
    retained={'source_run':prior.get('github_run_id'),'source_commit':prior.get('github_sha'),'status':stage['status'],
        'completed_targets_exact':stage.get('completed_targets_exact'),'unfinished_active_target_exact':stage.get('active_stage_target_exact'),
        'published_final_coarse_decision':copy.deepcopy(prior['final_full_grid_constraints']),
        'published_final_fine_decision':copy.deepcopy(prior['final_doubled_constraints']),
        'old_SOC_success_and_rejected_trials_not_recomputed_or_relabelled':True}
    replay={'schema':'sixteen-input-inherited-primary-scale-SOC-replay-v1','fifteen_input_replay':old_replay,
        'canonical_physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),'physical_parameter_count':problem.nunknown,
        'same_full_saved_accepted_coefficients':True,'same_complete_g_b0_space_and_two_value_grids':True,
        'learned_pool':learned,'completed_SOC_attempt_retained':retained,'primary_scale_inheritance':evidence,
        'known_fine_metric_locations':list(locations.values()),'new_primary_scale_policy':POLICY,
        'old_optimizer_calls_replayed':0,'no_research_geometry_during_structural_replay':True}
    return (problem,state,gate,lower,upper,source_cfg,configuration(old_cfg)),replay,np.asarray(ci,np.int64),np.asarray(fi,np.int64)


def prepare_run(args,*,artificial=False,process_started=None):
    start=time.monotonic(); process_started=start if process_started is None else process_started
    phase='fifteen-input-prior-SOC-start-replay'; bindings={}
    try:
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),[getattr(args,x) for x in INPUTS])
        old=previous.prepare_run(args,artificial=artificial,process_started=process_started)
        bindings=copy.deepcopy(old[1]); phase='sixteenth-SOC-byte-binding'
        if args.soc_audit is None or args.expected_soc_sha256 is None:
            raise ValueError('sixteenth complete SOC report and expected SHA are required')
        prior,raw,binding=read_input(args.soc_audit,args.expected_soc_sha256)
        phase='sixteenth-SOC-accepted-state-pool-and-primary-scale-replay'
        restored,replay,coarse,fine=replay_soc_success(old,prior,artificial=artificial)
        bindings['completed_SOC_target60']=binding
        return restored,bindings,old[2],replay,coarse,fine
    except Exception as error:
        failure={'schema':SCHEMA,'status':'input-replay-failed-before-inherited-scale-geometry','phase':phase,
            'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,'artificial_inputs_only':bool(artificial),
            'old_optimizer_calls_this_run':0,'new_solver_calls':0,'prepare_elapsed_seconds':time.monotonic()-start,
            'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out,failure); raise


def small_summary(report,out):
    result=previous.small_summary(report,out)
    for key in ['primary_scale_inheritance','completed_SOC_attempt_retained']:
        if key in report:
            result[key]={k:copy.deepcopy(v) for k,v in report[key].items() if not k.startswith('published_final_')}
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
        'process_clock_scope':'main includes sixteen-input loader; initialization and active inherited-scale SOC separately recorded',
        'prepare_elapsed_seconds':prepare_seconds,'learned_pool_replay':replay['learned_pool'],
        'completed_SOC_attempt_retained':replay['completed_SOC_attempt_retained'],
        'primary_scale_inheritance':replay['primary_scale_inheritance'],
        'curvature_target_ladder_definition':{'targets_exact':list(TARGETS),'success_only_advance':True,
            'one_shared_LP_limit':cfg['max_linear_models'],'one_shared_value_limit':cfg['max_physical_evaluations'],
            'one_shared_active_seconds':cfg['max_seconds'],'targets_not_physical_coefficients':True,
            'old_target60_kept_as_completed_history':True,
            'final16_is_sampled_local_curvature_only':True,'reach_design_tau_exact':cfg['curvature_target_radius_exact']},
        'SOC_definition':{'policy':cfg['SOC_policy'],'primary_scale_policy':POLICY,'at_most_one_correction_LP_per_primary_model':True,
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
    save('sixteen-inputs-replayed-before-inherited-scale-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth); order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid; report['phase']='one-two-grid-SOC-initialization'
        def checkpoint(snapshot):
            report['mixed_grid_short_step_stage']={'status':'current-SOC-two-grid-checkpoint','checkpoint':snapshot,'solver':{}}
            save('SOC-two-grid-physical-checkpoint')
        objective=InheritedScaleObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            sixteenth_report_decoded_sha256=bindings['completed_SOC_target60']['decoded_sha256'],
            primary_scale_inheritance=replay['primary_scale_inheritance'],
            learned_pool_replay=replay['learned_pool'],old_metric_delta_and_old_curvature_targets_are_preserved_history=True)
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(learned_coarse,{'kind':'all-sixteenth-learned-coarse-rows-retained','source':replay['learned_pool']})
        objective.set_fine_pool(learned_fine,{'kind':'all-sixteenth-learned-fine-rows-retained','source':replay['learned_pool']})
        first=objective.evaluate(np.r_[initial,initial_target/scale])
        report['initial_current_constraints']=copy.deepcopy(first['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        save('complete-inherited-scale-initial-two-grid-diagnostics-target55-not-assumed-feasible')
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
        save('complete-two-grid-inherited-scale-SOC-curvature-audit' if eligible
             else 'final-same-state-value-recheck-failed-do-not-use-as-new-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('inherited-scale-SOC-audit-error-checkpoints-preserved'); return report


def developer_check():
    # An explicit array LP shows the changed, genuinely binding scale. No
    # candidate geometry is constructed for this comparison.
    cfg=configuration(previous.configuration()); cfg['linear_program_seconds']=2.
    state=np.zeros(2); lower=np.full(2,-8.); upper=-lower
    base=np.array([1.,-1.]); J=np.array([[0.,0.],[1.,0.]])
    groups=np.array([0,7]); tolerances=np.full(2,1e-9); cap=np.zeros(2)
    p,lp=linear_proposal(base,J,groups,tolerances,state,lower,upper,cap,1.,float(Q(TRUST)),cfg)
    wide,wlp=linear_proposal(base,J,groups,tolerances,state,lower,upper,cap,1.,.01,cfg)
    new_norm=float(np.max(abs(p)/(upper-lower))); old_norm=float(np.max(abs(wide)/(upper-lower)))
    binding_scale=bool(lp['success'] and wlp['success'] and abs(new_norm-.001)<1e-12
        and abs(old_norm-.01)<1e-12 and abs(np.max(abs(p))-.016)<1e-12)
    fake_step=np.array([.017,.001]); norm=float(np.max(abs(fake_step)/(upper-lower)))
    fake_stage={'solver':{'models':[{'number':1,'result':'accepted-SOC-corrected-two-grid-step',
        'exact_binary64_proposed_step':coefficients(fake_step),'corrections':[{'linear_program':{
            'LP_invoked':True,'success':True,'primary_box_normalized_step_infinity_norm':norm,
            'maximum_absolute_correction':.0008}}]}]}}
    fake_point={'reason':{'model':1,'alpha_exact':'1'}}
    ev=successful_primary_scale(fake_stage,fake_point,lower,upper,2)
    evidence_ok=(ev['source_primary_norm_exact_binary64']==str(Q.from_float(norm))
        and ev['source_primary_step_exact_coefficients_sha256']==digest(coefficients(fake_step))
        and Q(ev['chosen_scale_to_saved_norm_exact'])==Q(TRUST)/Q.from_float(norm))
    broken=copy.deepcopy(fake_stage)
    broken['solver']['models'][0]['corrections'][0]['linear_program']['primary_box_normalized_step_infinity_norm']=0.
    try:
        successful_primary_scale(broken,fake_point,lower,upper,2); wrong_norm=False
    except ValueError:wrong_norm=True

    with tempfile.TemporaryDirectory(prefix='curvature-inherited-scale-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder); ladder=previous.previous; mixed=ladder.previous
        args,unused,unused_prior=mixed.artificial_thirteen_inputs(directory)
        args.out=directory/'completed-mixed-artificial.json'
        thirteen=mixed.prepare_run(args,artificial=True)
        r14=mixed.run_audit(thirteen,args.out,artificial=True,evaluate_only=True)
        if r14['status']!='complete-mixed-grid-fixed-target-short-step-audit':
            raise ArithmeticError('artificial fourteenth fixture failed')
        args.mixed_grid_audit=args.out; args.expected_mixed_grid_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'completed-ladder-artificial.json'
        fourteen=ladder.prepare_run(args,artificial=True)
        r15=ladder.run_audit(fourteen,args.out,artificial=True,evaluate_only=True)
        if r15['status']!='complete-two-grid-curvature-target-ladder-audit':
            raise ArithmeticError('artificial fifteenth fixture failed')
        args.target_ladder_audit=args.out; args.expected_target_ladder_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'completed-SOC-artificial.json'
        fifteen=previous.prepare_run(args,artificial=True)
        prior=previous.run_audit(fifteen,args.out,artificial=True,evaluate_only=True)
        if prior['status']!='complete-two-grid-bounded-SOC-curvature-audit':
            raise ArithmeticError('artificial sixteenth fixture failed')
        args.soc_audit=args.out; args.expected_soc_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'inherited-scale-artificial.json'
        before=time.monotonic(); prepared=prepare_run(args,artificial=True,process_started=before)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=before,prepare_seconds=time.monotonic()-before)
        st=report.get('mixed_grid_short_step_stage',{}); snap=st.get('checkpoint',{})
        old=prior['mixed_grid_short_step_stage']['checkpoint']
        pools_kept=all(set(old[name][-1]['row_indices']).issubset(snap.get(name,[{}])[0].get('row_indices',[]))
            for name in ['active_row_pool_history','fine_physical_row_pool_history'])
        same=report.get('final_state')==prior['final_state']; no_lp=st.get('solver',{}).get('linear_program_invocation_count')==0
        provenance_label=snap.get('selected_two_grid_physical_point',{}).get('reason',{}).get('kind')==\
            'saved-b03c-target60-SOC-success-inherited-scale-start'
        summary=json.loads(summary_path(args.out).read_text()); summary_bytes=summary_path(args.out).stat().st_size
        bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args); wrong.out=directory/'wrong-sixteenth-SHA.json'; wrong.expected_soc_sha256='0'*64
        try:
            prepare_run(wrong,artificial=True); bad_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text())
            bad_sha=failure['phase']=='sixteenth-SOC-byte-binding' and failure['new_solver_calls']==0
        changed=copy.deepcopy(prior)
        changed['mixed_grid_short_step_stage']['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
        try:
            replay_soc_success(fifteen,changed,artificial=True); bad_state=False
        except ValueError:bad_state=True
        changed=copy.deepcopy(prior)
        fake_pool=changed['mixed_grid_short_step_stage']['checkpoint']['fine_physical_row_pool_history'][-1]
        first=fake_pool['row_indices'][0]; rr,tt,unused_grid=curvature_grid(fifteen[2])
        fake_pool['added_row_indices']=[first]
        fake_pool['added_original_grid_coordinates']=fine_row_coordinates([first],rr,np.arange(2*len(tt))*np.pi/len(tt))
        fake_pool['added_original_grid_coordinates'][0]['theta']=123.
        try:
            replay_soc_success(fifteen,changed,artificial=True); bad_coord=False
        except ValueError:bad_coord=True
        # Stage changes use the same frozen controller and config object.
        pr,ss,ga,ll,uu,source_cfg,newcfg=prepared[0]
        radial,theta,unused_grid=curvature_grid(prepared[2])
        ob=InheritedScaleObjective(pr,ga,radial,theta,int(source_cfg['primitive_order']),ll,uu,cfg=newcfg)
        cb=copy.deepcopy(ob.cfg); ob.set_stage(1)
        stage_scale_preserved=(ob.active_target_exact==TARGETS[1] and ob.cfg==cb
            and ob.cfg['initial_trust_box_fraction_exact']==TRUST and ob.geometry_evaluations==0 and ob.fine_evaluations==0)
        frozen_sources=report.get('source_files_sha256')==implementation_hashes()
        status=report['status']; error=report.get('error'); refinement=report.get('same_parameter_Pi_refinement')
    passed=bool(binding_scale and evidence_ok and wrong_norm and pools_kept and same and no_lp and provenance_label
        and bound and summary_bytes<95000 and bad_sha and bad_state and bad_coord and stage_scale_preserved
        and frozen_sources and status=='complete-two-grid-inherited-scale-SOC-curvature-audit')
    return {'schema':'inherited-primary-scale-sixteen-input-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,'no_Actions_environment_forged':True,
        'new_exact_primary_scale_binds_large_pressure_array_LP':binding_scale,
        'array_old_normalized_step':old_norm,'array_new_normalized_step':new_norm,
        'saved_successful_primary_scale_reconstructed_from_exact_coefficients':evidence_ok,
        'altered_reported_successful_norm_rejected':wrong_norm,
        'full_main_status':status,'full_main_error':error,'same_complete_state_g_b0_and_freeze':same,
        'all_prior_coarse_and_fine_pool_rows_retained':pools_kept,'artificial_full_main_has_no_LP':no_lp,
        'initial_provenance_label_names_new_source':provenance_label,
        'target_switch_does_not_reset_primary_scale_or_evaluate_geometry':stage_scale_preserved,
        'summary_binds_complete_report':bound,'summary_bytes':summary_bytes,'source_hashes_match':frozen_sources,
        'wrong_sixteenth_SHA_saves_failure':bad_sha,'changed_full_coefficients_rejected':bad_state,
        'changed_fine_original_coordinate_rejected':bad_coord,'same_state_angle_refinement':refinement,'passed':passed}


def main():
    process_started=time.monotonic(); parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true'); parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'inherited-scale-development-error-v1','passed':False,'artificial_inputs_only':True,
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
    if report['status']!='complete-two-grid-inherited-scale-SOC-curvature-audit':raise SystemExit(1)


if __name__=='__main__':main()


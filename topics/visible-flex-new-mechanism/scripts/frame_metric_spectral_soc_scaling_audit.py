#!/usr/bin/env python3
"""Two temporary input restorations followed by one equivalent SOC-scaling stage.

The twenty-four legacy inputs remain exact. One growth and one strip-reserve
prefix restore the necessary state, pools and controller within this job.
The new scientific stage changes only the SOC linear program representation;
all existing targets, actual gates and budgets are retained.
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
import frame_metric_spectral_strip_reserve_audit as strip
from frame_metric_spectral_soc_scaling import (
    SOCScaledSpectralMetricObjective,run_soc_scaled_recovery,
    configuration as soc_configuration,implementation_hashes as soc_hashes,
    developer_check as soc_check,scaling_definition,
    strip_floor_definition,penalty_definition,floor_definition,growth_definition,adaptive_definition)


SCHEMA='same-g-spectral-metric-SOC-scaling-after-temporary-growth-and-strip-audit-v1'
STAGE='metric_spectral_soc_scaling_stage'
PREFIX_STAGE=strip.STAGE
GROWTH_STAGE='metric_spectral_trust_growth_stage'
OBSERVED_STRIP_RUN='43684152565'
OBSERVED_STRIP_SOURCE='c594eeb060f25dbc9c48911b4ec6511497692c0f'
OBSERVED_STRIP_STATE='267c41ff9cfe565cb859531ab505b3cab85069ff0ad77955fccb5e00354e824e'
OBSERVED_STRIP_REPORT_SHA='eba499be5bfbf9e74e0cf9af4a62e2799cafadbb0b33378deba797c41dbd4f25'
FROZEN_PREFIX_SOURCE_SHA256={
    'frame_metric_spectral_strip_reserve.py':'0d653e66947b95efe56e518e8bf4705076bc9ef687e5a596a1884b8367d22ae3',
    'frame_metric_spectral_strip_reserve_audit.py':'4347bdc3afc2504b2a6546d41176e0e3a9e340533ee1eee16ff831257e149e38'}
METRIC_TARGET='13/50'
CURVATURE_CAP='58'
INPUTS=growth.INPUTS
SHA_NAMES=growth.SHA_NAMES
coefficients=growth.coefficients
curvature_grid=growth.curvature_grid
summary_path=growth.summary_path


def implementation_hashes():
    result=strip.implementation_hashes();result.update(soc_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def require_frozen_prefix_sources():
    actual=strip.implementation_hashes()
    for name,expected in FROZEN_PREFIX_SOURCE_SHA256.items():
        if actual.get(name)!=expected:
            raise ValueError('the necessary temporary prefix implementation differs: '+name)


def configuration(base,*,artificial=False):
    return soc_configuration(strip.configuration(base,artificial=artificial))


def restored_controller_state(stage,cfg,expected_initial):
    """Use completed updates; an interrupted last model contributes no success."""
    inherited=stage.get('solver',{}).get('restored_controller_continuation')
    if inherited!=expected_initial:
        raise ValueError('strip stage initial controller must be its actual restored growth continuation')
    from frame_metric_spectral_strip_reserve import controller_continuation
    radius,streak,validated=controller_continuation(cfg,inherited,artificial=True)
    last_completed=0;origin='inherited strip-stage initial controller: no new model was started'
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
        'initial_growth_rule_and_actual_feedback_policy_unchanged':True,
        'previous_stage_initial_controller':copy.deepcopy(validated)}


def handoff_restored_strip(prepared,prefix,raw_binding,*,artificial=False):
    """Structural in-memory handoff; no geometry, optimizer, or fake old SHA."""
    require_frozen_prefix_sources()
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prefix.get('schema')!=strip.SCHEMA
            or prefix.get('status')!='complete-two-grid-fixed-curvature-spectral-strip-reserve-audit'
            or bool(prefix.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed current temporary strip result required')
    if (prefix.get('source_files_sha256')!=strip.implementation_hashes()
            or prefix.get('configuration')!=old_cfg or prefix.get('exact_input_storage')!=bindings
            or prefix.get('input_replay')!=old_replay
            or prefix.get('initial_state')!=state_record(problem,old_initial)
            or prefix.get('old_optimizer_calls_this_run')!=1
            or prefix.get('necessary_growth_prefix_restoration_calls')!=1
            or prefix.get('new_scientific_solver_calls')!=1
            or prefix.get('unchanged_complete_metric_and_height_reference') is not True):
        raise ValueError('temporary strip source/configuration/legacy inputs/initial identity differ')
    if not artificial and (prefix.get('github_sha')!=os.environ.get('GITHUB_SHA')
            or str(prefix.get('github_run_id'))!=os.environ.get('GITHUB_RUN_ID')
            or prefix.get('github_repository')!='Rogerhu12/math-research-public'
            or problem.nunknown!=163):
        raise ValueError('prefix must be the current public job and same163 family')
    stage=prefix[PREFIX_STAGE]
    if stage.get('error') is not None or 'error' in stage.get('status',''):
        raise ValueError('prefix implementation failure is not a qualified restoration')
    snap=stage['checkpoint'];point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('temporary strip accepted state missing')
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
    continuation=restored_controller_state(stage,old_cfg,old_replay['controller_continuation'])
    observed={'run':OBSERVED_STRIP_RUN,'source':OBSERVED_STRIP_SOURCE,
        'canonical_physical_state_sha256':OBSERVED_STRIP_STATE,
        'temporary_complete_report_sha256':OBSERVED_STRIP_REPORT_SHA,
        'raw_report_not_available_or_used_as_a_new_input':True}
    restoration={'schema':'same-job-temporary-strip-prefix-restoration-v1',
        'purpose':'restore necessary runtime state under metadata-only output policy, not a new scientific comparison',
        'prefix_scientific_implementation_sha256':strip.implementation_hashes(),
        'prefix_configuration':copy.deepcopy(old_cfg),'prefix_current_run':prefix.get('github_run_id'),
        'prefix_current_source':prefix.get('github_sha'),
        'prefix_temporary_raw_file':copy.deepcopy(raw_binding),
        'prefix_status':stage.get('status'),'prefix_budget_message':stage.get('budget_message'),
        'controller_continuation':continuation,
        'prefix_source_initial_physical_sha256':digest(problem.identity(old_initial)),
        'prefix_regenerated_final_physical_sha256':point['physical_state_sha256'],
        'observed_reference':observed,
        'regenerated_final_equals_observed_strip267':point['physical_state_sha256']==OBSERVED_STRIP_STATE,
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
    learned={'schema':'temporary-strip-complete-learned-pool-handoff-v1',
        'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'all_previous_coarse_and_fine_integer_IDs_retained':True,
        'groups2_to10_have_original_actual_values_and_derivatives':True}
    cfg=configuration(old_cfg,artificial=artificial)
    replay={'schema':'temporary-strip-to-scaled-SOC-in-memory-handoff-v1',
        'canonical_physical_state_sha256':point['physical_state_sha256'],
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'physical_parameter_count':problem.nunknown,'learned_pool':learned,
        'known_fine_metric_locations':list(locations.values()),'temporary_input_restoration':restoration,
        'controller_continuation':continuation,
        'temporary_input_restorations':[copy.deepcopy(old_replay['temporary_input_restoration']),restoration],
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
            'SOC_reversible_scaling':scaling_definition(cfg),
            'all_actual_gates_and163_physical_family_unchanged':True,
            'actual_new_stage_progress_is_measured_from_this_regenerated_initial_state':True,
            'no_initial_match_to_observed_strip267_is_assumed':True}}
    return ((problem,state,gate,lower,upper,source_cfg,cfg),bindings,tenth,replay,
        np.asarray(ci,np.int64),np.asarray(fi,np.int64))


def small_summary(report,out):
    legacy=copy.copy(report);stage=legacy.pop(STAGE,None)
    if stage is not None:legacy[GROWTH_STAGE]=stage
    result=growth.resolve_summary_definition_references(growth.small_summary(legacy,out))
    if GROWTH_STAGE in result:result[STAGE]=result.pop(GROWTH_STAGE)
    result['temporary_input_restorations']=copy.deepcopy(report.get('temporary_input_restorations',[]))
    if STAGE in result:
        result[STAGE]['strip_proposal_floor']=strip_floor_definition(report['configuration'])
        result[STAGE]['SOC_reversible_scaling']=scaling_definition(report['configuration'])
        result[STAGE].get('complete_group8_selected_row_source',{})['full_report_path']=STAGE+'.solver.models'
    return result


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


def _scalar(value,*,digits=12):
    if value is None:return 'NA'
    if isinstance(value,(bool,np.bool_)):return 'true' if value else 'false'
    if isinstance(value,(float,np.floating)):return format(float(value),'.'+str(digits)+'g')
    return str(value)


GATE_ORDER=('regularity_screen_pass','previous_metric_budget_pass','single_grid_hard_gate_pass',
    'hard_ball_pass','hard_strip_pass','outer_strip_pass','signed_height_pass','mirror_polynomial_pass',
    'independent_direct_mirror_radius_pass','curvature_lambda_bound_pass','curvature_scaled_PSD_row_pass',
    'independent_direct_curvature_pass','single_grid_admissible_recovery_point','cap_and_box_eligible')
GATE_NUMBERS=('direct_max_eta','direct_maximum_absolute_principal_curvature','inner_strip_absolute_margin',
    'maximum_absolute_y','minimum_signed_height','direct_mirror_radius_min_finite')


def _gate_codes(decision):
    actual=decision.get('actual_gate_booleans')
    if actual is None:
        actual=dict(decision)
        actual['cap_and_box_eligible']=decision.get('cap_and_box',{}).get(
            'eligible_under_declared_numerical_gate_tolerances')
    return ''.join('1' if actual.get(k) is True else '0' if actual.get(k) is False else '?' for k in GATE_ORDER)


def prefix_outcome_text(prefix,restoration,label):
    """Only finite scalar conclusions, not a JSON report or coefficient payload."""
    lines=['TEMPORARY INPUT RESTORATION '+label+' -- not new scientific progress',
        'gate code order (1=true,0=false,?=unavailable): '+', '.join(GATE_ORDER)]
    for key in ['prefix_current_run','prefix_current_source','prefix_status','prefix_budget_message',
            'prefix_source_initial_physical_sha256','prefix_regenerated_final_physical_sha256',
            'regenerated_final_equals_observed_f2bb','regenerated_final_equals_observed_strip267',
            'prefix_accepted_count','prefix_linear_program_count','prefix_shared_full_values',
            'prefix_optimization_active_seconds','prefix_run_audit_elapsed_seconds','prefix_preparation_elapsed_seconds']:
        if key in restoration:lines.append(key+': '+_scalar(restoration[key],digits=17))
    raw=restoration['prefix_temporary_raw_file']
    lines.append('temporary original bytes/SHA: '+str(raw['bytes'])+' / '+raw['sha256'])
    lines.append('prefix source-map SHA: '+digest(restoration['prefix_scientific_implementation_sha256']))
    lines.append('prefix exact configuration SHA: '+digest(restoration['prefix_configuration']))
    c=restoration['controller_continuation']
    lines.append('continued controller: radius='+c['trust_binary64_exact']+'; streak='+str(c['success_streak'])+
        '; origin='+c['origin']+'; incomplete last model='+_scalar(c['unfinished_last_model_not_counted_as_success']))
    lines.append('case | all-gate codes | '+ ' | '.join(GATE_NUMBERS))
    for key in ['initial_current_constraints','initial_doubled_constraints',
            'final_full_grid_constraints','final_doubled_constraints']:
        d=prefix.get(key,{})
        lines.append(key+' | '+_gate_codes(d)+' | '+' | '.join(_scalar(d.get(k),digits=17) for k in GATE_NUMBERS))
    lines.append('The observed historical hash is not a forced replay condition; all later progress starts from this actual qualified state.')
    return '\n'.join(lines)+'\n'


def supplementary_outcome_text(report):
    """Read computed state only. Every reported row is a human diagnostic summary."""
    lines=['SOC EQUIVALENT SCALING -- original gates and original-unit LP residual limit retained',
        'New solver tolerances act on new units; numerical trajectories need not match the old LP.',
        'Actual gates codes (1=true,0=false,?=unavailable): '+', '.join(GATE_ORDER)]
    models=report.get(STAGE,{}).get('solver',{}).get('models',[])
    lines.append('TRIAL GATES: model | trial | grid | codes | new metric target')
    for model in models:
        for ti,trial in enumerate(model.get('trials',[])):
            for name in ['coarse','fine']:
                d=trial.get(name+'_decision')
                if d is not None:lines.append(' | '.join(map(_scalar,[model['number'],ti,name,_gate_codes(d),d.get('new_metric_target_qualified')])))
    lines.append('PROPOSAL ROW UNITS: model | kind | group | n | old target min | requested min | linear achieved min | maximum floor shortfall | original row violation')
    for model in models:
        proposals=[('primary',model.get('linear_program',{}))]+[
            ('SOC'+str(j),record.get('linear_program',{})) for j,record in enumerate(model.get('corrections',[]))]
        for kind,lp in proposals:
            for name,oldkey,newkey in [('curvature_proposal_diagnostics','legacy_target_minimum','requested_target_minimum'),
                    ('strip_proposal_diagnostics','old_target_minimum','new_target_minimum')]:
                for d in lp.get(name,{}).get('group_statistics',[]):
                    row=[model['number'],kind,d['group'],d['selected_count'],d.get(oldkey),d.get(newkey),
                        d.get('linear_achieved_minimum'),d.get('maximum_linear_floor_shortfall'),lp.get('maximum_linear_row_violation')]
                    lines.append(' | '.join(_scalar(x,digits=9) for x in row))
    lines.append('SOC SOLVER: model | correction | status | success | primal | r_c | divisor min | divisor max | scale seconds | LP seconds | original row residual | original bound residual | scaled row residual | scaled bound residual')
    duals=[]
    for model in models:
        for j,record in enumerate(model.get('corrections',[])):
            lp=record.get('linear_program',{});scale=lp.get('SOC_reversible_scaling',{})
            res=lp.get('SOC_original_and_scaled_residuals',{})
            row=[model['number'],j,lp.get('status'),lp.get('success'),lp.get('SOC_solver_returned_finite_primal'),
                scale.get('positive_radius_evaluated'),scale.get('row_divisor_minimum'),scale.get('row_divisor_maximum'),
                lp.get('SOC_scaling_prepare_seconds'),lp.get('elapsed_seconds'),
                res.get('maximum_original_linear_row_violation'),res.get('maximum_original_linear_bound_violation'),
                res.get('maximum_scaled_linear_row_violation'),res.get('maximum_scaled_linear_bound_violation')]
            lines.append(' | '.join(_scalar(x,digits=12) for x in row))
            if lp.get('message'):lines.append('SOC message '+str(model['number'])+'/'+str(j)+': '+str(lp['message']))
            if lp.get('proposal_rejected_before_LP'):lines.append('SOC pre-LP rejection: '+str(lp['proposal_rejected_before_LP']))
            if lp.get('proposal_rejected_before_geometry'):lines.append('SOC original-unit rejection: '+str(lp['proposal_rejected_before_geometry']))
            duals.append((model['number'],j,lp.get('SOC_original_unit_dual_diagnostics',{})))
    lines.append('ORIGINAL UNIT DUAL: model | correction | available | primal objective | dual objective | gap | stationarity residual | complementarity | sign violation')
    for m,j,d in duals:
        lines.append(' | '.join(_scalar(x,digits=12) for x in [m,j,d.get('available'),
            d.get('original_primal_objective'),d.get('original_dual_objective_evaluated'),d.get('original_primal_minus_dual'),
            d.get('maximum_original_stationarity_residual'),d.get('maximum_original_complementarity_product'),d.get('dual_sign_violation')]))
        if not d.get('available'):lines.append('dual unavailable: '+str(d.get('reason','no solver result')))
    lines.append('DUAL GROUPS (nonunique decomposition): model | correction | group | rows | multiplier sum | max multiplier | stationarity contribution infinity norm')
    for m,j,d in duals:
        for row in d.get('original_unit_inequality_group_summaries',[]):
            lines.append(' | '.join(_scalar(x,digits=9) for x in [m,j,row['group'],row['rows'],
                row['nonnegative_multiplier_sum'],row['maximum_multiplier_magnitude'],row['stationarity_contribution_infinity_norm']]))
    lines.append('CURVATURE NONLINEAR DEFECT: model | trial | reference | grid | group | n | minimum predicted | minimum actual | max abs defect | critical original row | t | theta | q | kappa1 | kappa2 | critical predicted | critical actual | critical actual-predicted | determinant identity difference')
    lines.append('reference B=accepted base+J total displacement; Y=same primary-y actual rows+old J correction; no additional value calls')
    for model in models:
        for ti,trial in enumerate(model.get('trials',[])):
            diagnostic=trial.get('curvature_nonlinear_defect_diagnostic',{})
            ref='Y' if diagnostic.get('reference_kind')=='same-primary-y-actual-rows-plus-old-J-correction' else 'B'
            for grid,data in diagnostic.get('grids',{}).items():
                for d in data.get('groups',[]):
                    c=d['actual_minimum_selected_row'];ks=c['principal_curvatures']
                    row=[model['number'],ti,ref,grid,d['group'],d['selected_count'],d['selected_predicted_minimum'],
                        d['selected_actual_minimum'],d['maximum_absolute_actual_minus_prediction'],c['flat_row_id'],
                        c['t'],c['theta'],c['q'],ks[0],ks[1],c['predicted_row'],c['actual_row'],
                        c['actual_minus_predicted'],c.get('floating_identity_difference')]
                    lines.append(' | '.join(_scalar(x,digits=9) for x in row))
    lines.append('These floating LP diagnostics and sampled gates are not validated optimality, exact isometry or whole-surface reach certificates.')
    return '\n'.join(lines)+'\n'


def print_new_stage_outcomes(report):
    print(supplementary_outcome_text(report),end='',flush=True)


def run_pipeline(args,*,artificial=False,evaluate_only=False,process_started=None):
    """Growth -> strip input restoration -> one new stage, with no persisted prefix."""
    started=time.monotonic() if process_started is None else process_started
    phase='public-environment-and-legacy-input-contract';restorations=[];raw_bindings=[]
    growth_invoked=strip_invoked=new_invoked=0
    try:
        require_frozen_prefix_sources()
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        parent=os.environ.get('RUNNER_TEMP')
        if artificial and Path('/dev/shm').is_dir():parent='/dev/shm'
        with tempfile.TemporaryDirectory(prefix='visible-SOC-input-restorations-',dir=parent) as folder:
            growth_out=Path(folder)/'restored-growth.json';strip_out=Path(folder)/'restored-strip.json'
            prefix_args=copy.copy(args);prefix_args.out=growth_out
            phase='strict-original-twenty-four-input-preparation';before=time.monotonic()
            prepared=growth.prepare_run(prefix_args,artificial=artificial,process_started=started)
            preparation=time.monotonic()-before
            phase='one-necessary-frozen-growth-input-restoration';growth_invoked=1
            previous=growth.run_audit(prepared,growth_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=preparation)
            raw=growth_out.read_bytes()
            binding={'filename':growth_out.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                'temporary_current_job_file_only':True,'not_an_observed_old_report_SHA_replay':True}
            raw_bindings.append(binding);del raw
            phase='temporary-growth-state-gates-pools-controller-handoff'
            continued=strip.handoff_restored_growth(prepared,previous,binding,artificial=artificial)
            restorations.append(continued[3]['temporary_input_restoration'])
            print(prefix_outcome_text(previous,restorations[-1],'growth'),end='',flush=True)
            del previous,prepared
            phase='one-necessary-frozen-strip-input-restoration';strip_invoked=1
            previous=strip.run_audit(continued,strip_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            raw=strip_out.read_bytes()
            binding={'filename':strip_out.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                'temporary_current_job_file_only':True,'not_an_observed_old_report_SHA_replay':True}
            raw_bindings.append(binding);del raw
            phase='temporary-strip-state-gates-pools-controller-handoff'
            new_prepared=handoff_restored_strip(continued,previous,binding,artificial=artificial)
            restorations=list(new_prepared[3]['temporary_input_restorations'])
            print(prefix_outcome_text(previous,restorations[-1],'strip-reserve'),end='',flush=True)
            del previous,continued
            phase='new-equivalent-SOC-LP-representation-stage';new_invoked=1
            return run_audit(new_prepared,args.out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
    except Exception as error:
        failure={'schema':SCHEMA,'status':'SOC-scaling-pipeline-failed-last-written-scientific-checkpoint-preserved',
            'phase':phase,'source_files_sha256':implementation_hashes(),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
            'necessary_growth_prefix_restoration_calls':growth_invoked,
            'necessary_strip_prefix_restoration_calls':strip_invoked,'new_scientific_solver_calls':new_invoked,
            'temporary_prefix_raw_bindings':raw_bindings,'temporary_input_restorations':restorations,
            'process_total_elapsed_seconds':time.monotonic()-started,
            'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
        if new_invoked and Path(args.out).exists():
            try:
                existing=json.loads(Path(args.out).read_text())
                existing['scientific_status_before_pipeline_failure']=existing.get('status')
                existing['status']='SOC-scaling-pipeline-error-last-checkpoint-preserved'
                existing['pipeline_failure']=failure
                save_report(args.out,existing);return existing
            except (OSError,ValueError,TypeError,KeyError):pass
        save_report(args.out,failure);return failure



def run_audit(prepared,out,*,artificial=False,evaluate_only=False,process_started=None,prepare_seconds=0.):
    restored,bindings,tenth,replay,coarse_pool,fine_pool=prepared
    problem,initial,gate,lower,upper,source_cfg,cfg=restored
    started=time.monotonic();process_started=started if process_started is None else process_started
    metric=copy.deepcopy(problem.metric_model(initial));b0=copy.deepcopy(problem.height_base_definition)
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':2,
        'necessary_growth_prefix_restoration_calls':1,'necessary_strip_prefix_restoration_calls':1,'new_scientific_solver_calls':0,'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':state_record(problem,initial),'unchanged_complete_metric_and_height_reference':True,
        'prepare_elapsed_seconds':prepare_seconds,
        'learned_pool_replay':replay['learned_pool'],
        'temporary_input_restorations':replay['temporary_input_restorations'],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'process_clock_scope':'main includes two necessary temporary input restorations and one new shared-budget SOC-scaling stage; their clocks are separately reported'}
    def save(status):
        now=time.monotonic();snapshot=report.get('metric_spectral_soc_scaling_stage',{}).get('checkpoint',{})
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
            report['metric_spectral_soc_scaling_stage']={'status':'current-two-grid-spectral-metric-recovery-checkpoint',
                'checkpoint':snapshot,'solver':{}}
            save('spectral-metric-recovery-last-accepted-physical-checkpoint')
        objective=SOCScaledSpectralMetricObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
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
        stage=run_soc_scaled_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            continuation_state=replay['controller_continuation'],
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['metric_spectral_soc_scaling_stage']=stage
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
            'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
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
            'old_failed_delta_and_unfinished55_preserved':True,'necessary_frozen_growth_and_strip_prefixes_each_recreated_once':True,
            'neither_prefix_is_new_scientific_progress':True,'no_other_old_optimizer_replayed':True}
        print_new_stage_outcomes(report)
        save('complete-two-grid-fixed-curvature-spectral-SOC-scaling-audit' if eligible
            else 'final-recheck-failed-do-not-use-as-new-physical-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        print_new_stage_outcomes(report)
        save('spectral-SOC-scaling-audit-error-last-checkpoint-preserved');return report



def developer_check():
    """Only new SOC mapping, strip-to-new handoff, printing and small-array IO."""
    import contextlib
    import io
    import sys
    from types import SimpleNamespace
    from unittest.mock import patch
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    targeted=soc_check()
    class ToyProblem:
        nunknown=3
        slices={'u':slice(0,1),'v':slice(1,2),'height':slice(2,3),'metric':slice(3,3)}
        height_base_definition={'schema':'pure-artificial-SOC-handoff-fixed-b0'}
        def identity(self,x):return {'family':'pure-artificial-SOC-handoff','coefficients':coefficients(x)}
        def metric_model(self,x):
            return {'schema':'pure-artificial-SOC-g','mathematical_definition_sha256':digest({'metric':'toy'})}
        def evaluation_definition(self):return {'schema':'pure-artificial-SOC-handoff-no-geometry'}
    problem=ToyProblem();old_state=np.array([.2,.3,.4]);new_state=np.array([.21,.31,.41])
    r=np.array([0.,.5,1.]);theta=np.arange(4)*np.pi/2
    grid={'schema':'tiny-artificial-SOC-handoff-grid','definition_sha256':digest({'r':r.tolist(),'theta':theta.tolist()})}
    cfg=strip.configuration(recovery_configuration(start_configuration(),target=METRIC_TARGET,curvature_cap=CURVATURE_CAP),artificial=True)
    seed=float(Q(cfg['initial_trust_box_fraction_exact']));inherited=2*seed
    initial_controller={'schema':'restored-growth-controller-continuation-v1',
        'trust_binary64_exact':str(Q.from_float(inherited)),'trust_evaluated':inherited,
        'success_streak':1,'origin':'artificial completed growth continuation'}
    bindings={'fixture':{'decoded_sha256':'f'*64,'decoded_bytes':1,'stored_sha256':'f'*64,'stored_bytes':1,'gzip_storage':False}}
    decision={k:cfg[k] for k in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
        'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']}
    decision.update(single_grid_admissible_recovery_point=True,direct_max_eta=.2,
        direct_max_eta_location={'t':.5,'theta':0.},direct_maximum_absolute_principal_curvature=2.,
        hard_strip_pass=True,hard_ball_pass=True,signed_height_pass=True,independent_direct_curvature_pass=True,
        previous_metric_budget_pass=True,maximum_absolute_y=.1,inner_strip_absolute_margin=.28999,
        minimum_signed_height=.05,direct_mirror_radius_min_finite=.1)
    first_restoration={'prefix_current_run':'artificial','prefix_current_source':'artificial-source',
        'prefix_status':'artificial-completed','prefix_budget_message':None,
        'prefix_source_initial_physical_sha256':'0'*64,'prefix_regenerated_final_physical_sha256':digest(problem.identity(old_state)),
        'regenerated_final_equals_observed_f2bb':False,'prefix_accepted_count':1,'prefix_linear_program_count':1,
        'prefix_shared_full_values':2,'prefix_optimization_active_seconds':.01,'prefix_run_audit_elapsed_seconds':.02,
        'prefix_preparation_elapsed_seconds':.01,'prefix_temporary_raw_file':{'bytes':1,'sha256':'e'*64},
        'prefix_scientific_implementation_sha256':growth.implementation_hashes(),
        'prefix_configuration':cfg,'controller_continuation':dict(initial_controller,
            unfinished_last_model_not_counted_as_success=False)}
    replay={'schema':'artificial-current-prepared-strip','fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'controller_continuation':initial_controller,'temporary_input_restoration':first_restoration}
    prepared=((problem,old_state,None,np.full(3,-1.),np.ones(3),{'primitive_order':3,'tau':'61/1000'},cfg),
        bindings,{'schema':'artificial-grid-input'},replay,np.array([0,48]),np.array([0,96]))
    def pool(ids,fine=False):
        nt=2*len(theta) if fine else len(theta)
        record={'row_indices':ids,'row_count':len(ids),'row_indices_sha256':digest(ids),
            'group_order':list(GROUPS),'total_full_grid_rows':11*len(r)*nt,
            'flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index' if fine
                else 'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'}
        if fine:record.update(added_row_indices=ids,added_original_grid_coordinates=rows_api.fine_coordinates(
            ids,r,np.arange(nt)*2*np.pi/nt))
        return record
    point={'exact_binary64_physical_coefficients':coefficients(new_state),
        'physical_parameter_coefficients_binary64':new_state.tolist(),'physical_state_sha256':digest(problem.identity(new_state))}
    models=[{'number':1,'trust_before_model':inherited,'scale_feedback_update':{'next_trust':seed,
        'conservative_growth':{'streak_before':1,'streak_after':0}}},
        {'number':2,'trust_before_model':seed,'trials':[{'attempt_status':'coarse-value-call-complete'}]}]
    prefix={'schema':strip.SCHEMA,'status':'complete-two-grid-fixed-curvature-spectral-strip-reserve-audit',
        'artificial_inputs_only':True,'source_files_sha256':strip.implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,'initial_state':state_record(problem,old_state),
        'old_optimizer_calls_this_run':1,'necessary_growth_prefix_restoration_calls':1,'new_scientific_solver_calls':1,
        'unchanged_complete_metric_and_height_reference':True,'final_state':state_record(problem,new_state),
        'github_run_id':'pure-artificial','github_sha':'pure-artificial-no-research',
        'github_repository':'Rogerhu12/math-research-public','full_value_sampling_definition':grid,
        'initial_current_constraints':decision,'initial_doubled_constraints':copy.deepcopy(decision),
        'final_full_grid_constraints':copy.deepcopy(decision),'final_doubled_constraints':copy.deepcopy(decision),
        'final_selection_validation':{'both_value_grids_hard_and_old_metric_pass':True,'both_grid_maximum_eta':.2},
        PREFIX_STAGE:{'status':'shared-value-time-or-pool-budget-exit','error':None,'final_consecutive_growth_qualifying_models':0,
            'solver':{'models':models,'linear_program_invocation_count':2,'restored_controller_continuation':initial_controller},
            'checkpoint':{'selected_two_grid_physical_point':point,'accepted_iterates':[point],
                'active_row_pool_history':[pool([0,1,48])],
                'fine_physical_row_pool_history':[pool([0,1,96],True)],
                'saved_fine_trials':[],'total_full_value_physical_evaluations':4}}}
    binding={'filename':'artificial-strip.json','bytes':1,'sha256':'e'*64}
    module=sys.modules[__name__]
    with patch.object(module,'curvature_grid',return_value=(r,theta,grid)):
        restored=handoff_restored_strip(prepared,prefix,binding,artificial=True)
        rc=restored[3]['controller_continuation'];before=copy.deepcopy(prefix)
        handoff_restored_strip(prepared,prefix,binding,artificial=True)
        immutable=prefix==before
        inherited_ok=bool(rc['trust_evaluated']==seed and rc['success_streak']==0
            and rc['unfinished_last_model_not_counted_as_success'] and rc['previous_stage_initial_controller']==initial_controller)
        different_ok=not restored[3]['temporary_input_restoration']['regenerated_final_equals_observed_strip267']
        rejects={}
        for name in ['coefficient','gate','pool','initial-controller','final-controller','implementation-error']:
            bad=copy.deepcopy(prefix)
            if name=='coefficient':bad[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
            elif name=='gate':bad['final_doubled_constraints']['single_grid_admissible_recovery_point']=False
            elif name=='pool':bad[PREFIX_STAGE]['checkpoint']['fine_physical_row_pool_history'][-1]['row_indices']=[0]
            elif name=='initial-controller':bad[PREFIX_STAGE]['solver']['restored_controller_continuation']['success_streak']=0
            elif name=='final-controller':bad[PREFIX_STAGE]['final_consecutive_growth_qualifying_models']=1
            else:bad[PREFIX_STAGE]['error']={'message':'injected failure'}
            try:handoff_restored_strip(prepared,bad,binding,artificial=True);rejects[name]=False
            except (ValueError,KeyError):rejects[name]=True
        no_models=copy.deepcopy(prefix[PREFIX_STAGE]);no_models['solver']['models']=[]
        no_models['final_consecutive_growth_qualifying_models']=1
        zero=restored_controller_state(no_models,cfg,initial_controller)
        zero_ok=zero['trust_evaluated']==inherited and zero['success_streak']==1
        complete=copy.deepcopy(prefix[PREFIX_STAGE])
        complete['solver']['models'][-1]['scale_feedback_update']={'next_trust':seed,
            'conservative_growth':{'streak_before':0,'streak_after':1}}
        complete['final_consecutive_growth_qualifying_models']=1
        completed=restored_controller_state(complete,cfg,initial_controller)
        completed_ok=completed['success_streak']==1 and not completed['unfinished_last_model_not_counted_as_success']
    calls={'prepare':0,'growth':0,'strip':0,'new':0};temporary=[]
    growth_prefix={'initial_current_constraints':decision,'initial_doubled_constraints':decision,
        'final_full_grid_constraints':decision,'final_doubled_constraints':decision}
    def prepare_stub(args,**kwargs):calls['prepare']+=1;return ('opaque-old-preparation',)
    def growth_stub(p,out,**kwargs):
        calls['growth']+=1;temporary.append(Path(out));atomic_save(out,growth_prefix);return copy.deepcopy(growth_prefix)
    def strip_stub(p,out,**kwargs):
        calls['strip']+=1;temporary.append(Path(out));atomic_save(out,prefix);return copy.deepcopy(prefix)
    def new_stub(p,out,**kwargs):
        calls['new']+=1
        if p[3]['controller_continuation']['trust_evaluated']!=seed:raise AssertionError('controller reset')
        result={'schema':SCHEMA,'status':'pure-artificial-new-stage-stub',
            'temporary_input_restorations':p[3]['temporary_input_restorations'],STAGE:{'solver':{},'checkpoint':{}}}
        atomic_save(out,result);return result
    with tempfile.TemporaryDirectory(prefix='SOC-new-pipeline-',dir='/dev/shm') as folder:
        out=Path(folder)/'new-audit.json';args=SimpleNamespace(out=out);captured=io.StringIO()
        with patch.object(module,'curvature_grid',return_value=(r,theta,grid)), \
                patch.object(growth,'prepare_run',side_effect=prepare_stub),patch.object(growth,'run_audit',side_effect=growth_stub), \
                patch.object(strip,'handoff_restored_growth',return_value=prepared),patch.object(strip,'run_audit',side_effect=strip_stub), \
                patch.object(module,'run_audit',side_effect=new_stub),contextlib.redirect_stdout(captured):
            result=run_pipeline(args,artificial=True,evaluate_only=True)
        one_each=calls=={'prepare':1,'growth':1,'strip':1,'new':1}
        unique=bool([p.name for p in Path(folder).glob('*-audit.json')]==['new-audit.json']
            and all(not p.exists() for p in temporary)
            and [k for k,v in result.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        both_printed=all(x in captured.getvalue() for x in ['RESTORATION growth','RESTORATION strip-reserve','initial_doubled_constraints','final_doubled_constraints'])
        args_fail=SimpleNamespace(out=Path(folder)/'failure-audit.json')
        with patch.object(growth,'prepare_run',side_effect=ValueError('injected new pipeline loader failure')):
            failure=run_pipeline(args_fail,artificial=True,evaluate_only=True)
        failure_saved=(failure['phase']=='strict-original-twenty-four-input-preparation'
            and failure['necessary_growth_prefix_restoration_calls']==0 and failure['necessary_strip_prefix_restoration_calls']==0
            and failure['new_scientific_solver_calls']==0 and json.loads(args_fail.out.read_text())['error']['type']=='ValueError')
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    class AuditArrayProblem(_CurvatureArrayProblem):
        ball_radius=1.01;strip_half_width=.38999;shape_weight=2.
        port=SimpleNamespace(side=1,width=.02)
        slices={'u':slice(0,1),'v':slice(1,2),'height':slice(2,3),'metric':slice(3,3)}
        height_base_definition={'schema':'artificial-SOC-audit-b0'}
        def metric_model(self,state):
            return {'schema':'artificial-SOC-audit-g','mathematical_definition_sha256':digest({'g':'array'})}
        def evaluation_definition(self):return {'schema':'artificial-SOC-audit-evaluation'}
        def frozen_metric_copy(self,state):return copy.copy(self),np.asarray(state).copy()
        def geometry(self,*args,**kwargs):
            data=super().geometry(*args,**kwargs);nr=len(data['radial'])
            data['height']={'b':np.zeros(nr),'b_s':np.zeros(nr),'b_ss':np.zeros(nr)};return data
    ap=AuditArrayProblem();ax=np.array([.3,.6,.6]);gate=HeightAffineGate.from_artificial_array_problem(ap)
    ar=np.array([0.,.2,.4,.7,1.]);at=np.arange(12)*np.pi/6
    acfg=configuration(recovery_configuration(start_configuration(),target='1/100',curvature_cap='3'),artificial=True)
    acfg.update(radial_Jacobian_batch_owned_rows=2,fine_Jacobian_owned_radial_rows=2,max_linear_models=1)
    areplay=copy.deepcopy(restored[3]);areplay['known_fine_metric_locations']=[]
    areplay['canonical_physical_state_sha256']=digest(ap.identity(ax))
    areplay['complete_metric_sha256']=ap.metric_model(ax)['mathematical_definition_sha256']
    areplay['fixed_b0_definition_sha256']=digest(ap.height_base_definition)
    aprepared=((ap,ax,gate,np.array([-.8,-1.,-1.]),np.array([2.,1.,1.]),
        {'primitive_order':3,'tau':'1/1000'},acfg),bindings,{'fixture':'array','selected_raw_auxiliary_delta':.5},areplay,np.array([0]),np.array([0]))
    agrid={'schema':'artificial-SOC-audit-grid','definition_sha256':digest({'r':ar.tolist(),'t':at.tolist()})}
    with tempfile.TemporaryDirectory(prefix='SOC-new-array-audit-',dir='/dev/shm') as folder:
        out=Path(folder)/'new-audit.json';printed=io.StringIO()
        with patch.object(module,'curvature_grid',return_value=(ar,at,agrid)), \
                patch.object(module,'audit_data',side_effect=lambda *a,**k:{'artificial_existing_jet_array_only':True}), \
                contextlib.redirect_stdout(printed):
            full=run_audit(aprepared,out,artificial=True,evaluate_only=True)
        native=json.loads(summary_path(out).read_text())
        full_ok=bool(full['status']=='complete-two-grid-fixed-curvature-spectral-SOC-scaling-audit'
            and full[STAGE]['solver']['linear_program_invocation_count']==0
            and full['final_selection_validation']['both_value_grids_hard_and_old_metric_pass']
            and full['initial_state']==full['final_state']
            and full[STAGE]['solver']['restored_controller_continuation']==areplay['controller_continuation']
            and native['full_report']['sha256']==hashlib.sha256(out.read_bytes()).hexdigest()
            and [k for k,v in native.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        def checkpoint_then_fail(p,out,**kwargs):save_report(out,full);raise RuntimeError('injected post-checkpoint failure')
        args=SimpleNamespace(out=Path(folder)/'preserved-audit.json')
        with patch.object(module,'curvature_grid',return_value=(r,theta,grid)), \
                patch.object(growth,'prepare_run',side_effect=prepare_stub),patch.object(growth,'run_audit',side_effect=growth_stub), \
                patch.object(strip,'handoff_restored_growth',return_value=prepared),patch.object(strip,'run_audit',side_effect=strip_stub), \
                patch.object(module,'run_audit',side_effect=checkpoint_then_fail),contextlib.redirect_stdout(io.StringIO()):
            preserved=run_pipeline(args,artificial=True,evaluate_only=True)
        retained=(preserved.get('status')=='SOC-scaling-pipeline-error-last-checkpoint-preserved'
            and preserved.get('final_state')==full.get('final_state') and preserved.get(STAGE)==full.get(STAGE)
            and preserved.get('pipeline_failure',{}).get('error',{}).get('type')=='RuntimeError')
    # Exercise all new printed columns without any research geometry or LP.
    gate={k:True for k in GATE_ORDER};gate['independent_direct_curvature_pass']=False
    trial={'coarse_decision':{'actual_gate_booleans':gate,'new_metric_target_qualified':False},
        'fine_decision':{'actual_gate_booleans':gate,'new_metric_target_qualified':False},
        'curvature_nonlinear_defect_diagnostic':{'reference_kind':'same-primary-y-actual-rows-plus-old-J-correction','grids':{}}}
    for name in ['coarse','fine']:
        gs=[]
        for g in range(7,11):
            gs.append({'group':g,'selected_count':1234,'selected_predicted_minimum':1e-7,
                'selected_actual_minimum':-2.3456789e-8,'maximum_absolute_actual_minus_prediction':1.23456789e-7,
                'actual_minimum_selected_row':{'flat_row_id':123456,'t':.78,'theta':4.8,'q':.9,
                    'principal_curvatures':[-58.0000034,2.3456789],'predicted_row':1e-7,'actual_row':-2.3456789e-8,
                    'actual_minus_predicted':-1.23456789e-7,'floating_identity_difference':1e-16}})
        trial['curvature_nonlinear_defect_diagnostic']['grids'][name]={'groups':gs}
    diagnostics={'available':True,'original_primal_objective':.1,'original_dual_objective_evaluated':.1,
        'original_primal_minus_dual':0.,'maximum_original_stationarity_residual':1e-9,
        'maximum_original_complementarity_product':1e-14,'dual_sign_violation':0.,
        'original_unit_inequality_group_summaries':[{'group':g,'rows':500,'nonnegative_multiplier_sum':.123456789,
            'maximum_multiplier_magnitude':.0123456789,'stationarity_contribution_infinity_norm':.23456789} for g in range(-2,11)]}
    lp={'status':0,'success':True,'message':'artificial complete scaled LP','SOC_solver_returned_finite_primal':True,
        'SOC_reversible_scaling':{'positive_radius_evaluated':1/128000,'row_divisor_minimum':2.**-40,'row_divisor_maximum':2.**9},
        'SOC_scaling_prepare_seconds':.0123456789,'elapsed_seconds':.123456789,
        'SOC_original_and_scaled_residuals':{'maximum_original_linear_row_violation':1e-9,
            'maximum_original_linear_bound_violation':1e-12,'maximum_scaled_linear_row_violation':1e-9,
            'maximum_scaled_linear_bound_violation':1e-12},'SOC_original_unit_dual_diagnostics':diagnostics,
        'curvature_proposal_diagnostics':{'group_statistics':[{'group':g,'selected_count':1234,
            'legacy_target_minimum':1e-9,'requested_target_minimum':1e-7,'linear_achieved_minimum':.999e-7,
            'maximum_linear_floor_shortfall':1e-10} for g in range(7,11)]},
        'strip_proposal_diagnostics':{'group_statistics':[{'group':g,'selected_count':234,
            'old_target_minimum':1e-9,'new_target_minimum':1e-7,'linear_achieved_minimum':.999e-7,
            'maximum_linear_floor_shortfall':1e-10} for g in [4,5]]},'maximum_linear_row_violation':1e-9}
    # A conservative rectangular stress fixture: 12 LP model slots and 20 full
    # coarse+fine trial pairs. The real shared 12 LP/40 value limits are smaller.
    stress_models=[]
    for m in range(12):
        stress_models.append({'number':m+1,'linear_program':copy.deepcopy(lp),
            'trials':[copy.deepcopy(trial) for _ in range(2 if m<8 else 1)],
            'corrections':[{'linear_program':copy.deepcopy(lp)}] if m<6 else []})
    text=supplementary_outcome_text({STAGE:{'solver':{'models':stress_models}}})
    print_size=len(text.encode());complete_print=('11111111111011' in text and 'ORIGINAL UNIT DUAL' in text
        and 'CURVATURE NONLINEAR DEFECT' in text and 'Y | fine | 10' in text and 'SOC message 6/0' in text)
    checks={'only_new_small_array_SOC_development':targeted['passed'],
        'strip_initial_controller_not_reset_to_growth_seed':inherited_ok,
        'zero_strip_models_retain_its_inherited_radius_and_streak':zero_ok,
        'completed_strip_update_nonzero_streak_retained':completed_ok,
        'observed_old267_hash_not_forced':different_ok,'prefix_original_dictionary_unchanged':immutable,
        'all_bad_new_handoffs_rejected':all(rejects.values()),
        'one_growth_one_strip_one_new_stage':one_each,'one_top_level_audit_and_stage_and_temporary_cleanup':unique,
        'both_prefix_full_initial_final_gates_printed':both_printed,'loader_failure_small_report':failure_saved,
        'new_real_api_small_array_initial_final_summary_path':full_ok,'post_checkpoint_failure_keeps_best':retained,
        'new_printed_all_gate_and_dual_and_defect_fields':complete_print,
        'conservative_extra_diagnostics_below_64KiB':print_size<65536}
    return {'schema':SCHEMA+'-new-interface-artificial-check','artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,'old_development_suites_not_repeated':True,
        'new_library_checks':targeted,'checks':checks,'new_handoff_rejections':rejects,
        'artificial_new_audit_status':full.get('status'),'artificial_new_audit_error':full.get('error'),
        'artificial_new_stage_error':full.get(STAGE,{}).get('error'),
        'conservative_extra_stdout_stress_bytes':print_size,
        'passed':bool(all(checks.values()))}


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
    if report.get('status')!='complete-two-grid-fixed-curvature-spectral-SOC-scaling-audit':
        raise SystemExit(1)


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Six necessary temporary restorations, then one conditional-SOC-radius stage.

Same physical163 family and exact159 coordinates. The sixth frozen prefix is
the original five-null-height159 algorithm. Only the new next-radius rule is
changed; no old development suite is repeated. All development and research
run on public Actions. Payloads are temporary; only metadata is published.
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
from frame_height_null_coordinates import digest
from frame_entry_paired_repair_audit import require_public_actions
from frame_curvature_epigraph_exchange import GROUPS
from frame_curvature_soc_metric_reserve_audit import exact_vector
from frame_metric_budget_recovery import recovery_decision
from frame_metric_spectral_recovery import EPSILON_EXACT,PROPOSAL_BRANCHES
import frame_metric_budget_restoration_rows as rows_api
import frame_metric_entry_tail_height159_audit as height159
import frame_metric_entry_tail_height159 as height159_library
import frame_metric_height159_soc_hold as hold_library
from frame_metric_height159_soc_hold import (
    SOCHold159Objective,run_soc_hold_recovery,configuration,retention_definition,
    implementation_hashes as library_hashes,developer_check as hold_check)
from frame_metric_entry_tail_height159 import (
    restriction_definition,growth_definition,layout_from_problem,POSITION_JETS,
    strip_floor_definition,penalty_definition,floor_definition,scaling_definition)
from frame_five_height_field import FiveHeightField
from frame_height_null_gate import FiveNullHeightGate
from frame_entry_tail_height_blocks import EntryTailHeight159Subspace,RationalRowGrid

growth=height159.growth
strip=height159.strip
soc=height159.soc
body103=height159.body103
tail154=height159.tail154
INPUTS=height159.INPUTS
SHA_NAMES=height159.SHA_NAMES
coefficients=height159.coefficients
curvature_grid=height159.curvature_grid
summary_path=height159.summary_path
GATE_ORDER=height159.GATE_ORDER
GATE_NUMBERS=height159.GATE_NUMBERS
_scalar=height159._scalar
_gate_codes=height159._gate_codes
audit_computed_field=height159.audit_computed_field
compare_computed_fields=height159.compare_computed_fields
field_diagnostics=height159.field_diagnostics
exact_height_diagnostic=height159.exact_height_diagnostic
outside_replay=height159.outside_replay
compact_refinement=height159.compact_refinement
_temporary_binding=height159._temporary_binding

SCHEMA='same159-SOC-conditional-radius-after-six-temporary-prefixes-audit-v1'
STAGE='metric_height159_soc_hold_stage'
PREFIX_STAGE=height159.STAGE
OBSERVED_HEIGHT159_RUN='43701558227'
OBSERVED_HEIGHT159_SOURCE='ef8c1cdb6f83fd96e24215c63d246adb0cbc0121'
OBSERVED_HEIGHT159_STATE='b42911eca31bb1b2e7609dc606e2f56db0783e7f99ea760a7450d7f433b7e805'
OBSERVED_HEIGHT159_REPORT_SHA='567acea708acf18a2fd5641487765c6c7f3071fad0a40b477a256c850d4c32d1'
FROZEN_HEIGHT159_SOURCE_SHA256={
    'frame_height_null_coordinates.py':'5ebfde0a3322bd119704fda517b2f15db48964fad7a3a344b1e863ec4c2f2f22',
    'frame_five_height_field.py':'549e61db392f318260d636d41a090bd56e8c96b2eab580075707b5e25a24f656',
    'frame_height_null_gate.py':'2b79490f44ab4bfc3d70324850c5b71949a5a7dfaf4a9f0948d52394f0be734b',
    'frame_entry_tail_height_blocks.py':'6aa3e08be5504b11d2fe14b07ee812b37ae064dd7033ec96673f027b6877d6b1',
    'frame_metric_entry_tail_height159.py':'670c9314558441fb15fd572e5f853475aced4d1bdbbe8fa7f67024609b8ab86a',
    'frame_metric_entry_tail_height159_audit.py':'ff0b8cfb3f8052d77dba7153abe8f1151a371469c5fba589a0e2c2f82e8a265b'}


def implementation_hashes():
    result=height159.implementation_hashes();result.update(library_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def require_frozen_prefix_sources():
    height159.require_frozen_prefix_sources()
    actual=height159.implementation_hashes()
    for name,expected in FROZEN_HEIGHT159_SOURCE_SHA256.items():
        if actual.get(name)!=expected:raise ValueError('frozen sixth-prefix source differs: '+name)


def restored_height159_controller(stage,cfg,expected_source_controller):
    """Replay scalar updates only, not the LP or geometry that produced them."""
    height159_library.restriction_definition(cfg)
    init=stage.get('solver',{}).get('inherited154_plus_new_height_controller',{})
    if init.get('restored_entry_tail154_controller_inherited')!=expected_source_controller:
        raise ValueError('sixth-prefix actual154 controller origin differs')
    radius=float(Q(init['inherited_body_radius_exact_binary64']));streak=init['inherited_success_streak']
    if (not np.isfinite(radius) or radius<=0 or type(streak) is not int or not 0<=streak<2
            or radius!=expected_source_controller['trust_evaluated']
            or streak!=expected_source_controller['success_streak']
            or Q(init['inherited_tail_radius_exact_binary64'])!=Q.from_float(radius)/8
            or Q(init['new_height_radius_exact_binary64'])!=4*Q.from_float(radius)):
        raise ValueError('sixth-prefix initial block radius or streak differs')
    models=stage.get('solver',{}).get('models',[]);without_update=False
    for i,m in enumerate(models):
        if m.get('number')!=i+1 or m.get('trust_before_model')!=radius:
            raise ValueError('sixth-prefix sequential model radius differs')
        update=m.get('scale_feedback_update')
        if update is None:
            if i!=len(models)-1:raise ValueError('only the final model may have incomplete control')
            without_update=True;continue
        r,s,expected=height159_library.next_mapped_trust(m,
            update['trust_after_original_controller'],streak,cfg)
        if expected!=update:raise ValueError('sixth-prefix update differs from its frozen159 rule')
        radius,streak=r,s
    if stage.get('last_restricted_trust')!=radius or stage.get('final_consecutive_growth_qualifying_models')!=streak:
        raise ValueError('sixth-prefix reported terminal controller differs')
    return {'schema':'recorded-frozen159-controller-inherited-by-SOC-hold-v1',
        'trust_evaluated':radius,'trust_binary64_exact':str(Q.from_float(radius)),
        'success_streak':streak,'last_model_without_completed_scale_feedback':without_update,
        'origin':'same-job frozen159 actual154 initialization followed only by completed original159 updates',
        'unfinished_last_model_not_counted_as_success':without_update,
        'new_stage_inherits_this_B_radius_and_streak_without_reset':True}



def prefix_handoff_diagnostic(prefix,raw_binding):
    """Read existing sixth-prefix metadata before any successful-status check.

    This neither validates a restoration nor evaluates geometry. Missing fields
    remain unavailable; no exception cause or attempted pool size is inferred.
    """
    def mapping(value):
        return value if isinstance(value,dict) else {}
    def pick(value,keys):
        value=mapping(value)
        return {key:copy.deepcopy(value[key]) for key in keys if key in value}
    stage=mapping(prefix.get(PREFIX_STAGE));solver=mapping(stage.get('solver'))
    snap=mapping(stage.get('checkpoint'));cfg=mapping(prefix.get('configuration'))
    histories={}
    for label,key,cap in [
            ('coarse','active_row_pool_history','max_pool_rows'),
            ('fine','fine_physical_row_pool_history','max_fine_physical_pool_rows')]:
        history=snap.get(key);last=mapping(history[-1]) if isinstance(history,list) and history else {}
        histories[label]=pick(last,['version','row_count','row_indices_sha256','total_full_grid_rows'])
        histories[label].update(capacity=copy.deepcopy(cfg.get(cap)),
            history_records=len(history) if isinstance(history,list) else None,
            reason=pick(last.get('reason'),['kind','pool_capacity_would_be_exceeded','proposed_pool_rows']))
    selected=mapping(snap.get('selected_two_grid_physical_point'))
    return {'schema':'frozen-height159-handoff-existing-diagnostic-v1',
        'temporary_raw_file':copy.deepcopy(raw_binding),
        'prefix':pick(prefix,['schema','status','phase','github_sha','github_run_id','github_repository',
            'artificial_inputs_only','optimization_active_seconds','run_audit_elapsed_seconds']),
        'prefix_error':pick(prefix.get('error'),['type','message','traceback']),
        'stage_status':copy.deepcopy(stage.get('status')),
        'stage_error':pick(stage.get('error'),['type','message','traceback']),
        'stage_budget_message':copy.deepcopy(stage.get('budget_message')),
        'solver':pick(solver,['linear_program_invocation_count','primary_LP_invocation_count',
            'correction_LP_invocation_count','shared_max_LPs','shared_max_values','shared_active_seconds']),
        'completed_model_records':len(solver.get('models',[])) if isinstance(solver.get('models',[]),list) else None,
        'checkpoint_counters':pick(snap,['physical_geometry_evaluations','total_full_value_physical_evaluations',
            'jacobian_geometry_batches','jacobian_refreshes',
            'fine_selected_Jacobian_refreshes','fine_selected_Jacobian_batches',
            'jacobian_geometry_seconds','fine_selected_Jacobian_seconds',
            'same_state_batch_ordinary_jet_differences_by_field','fine_batch_ordinary_replay_maxima',
            'optimization_elapsed_seconds','initialization_elapsed_seconds']),
        'initial_pre_LP_decision':copy.deepcopy(solver.get('initial_pre_LP_decision')),
        'last_pre_LP_decision':copy.deepcopy(stage.get('last_pre_LP_decision')),
        'pool_metadata':histories,
        'selected_point':pick(selected,['physical_state_sha256','maximum_eta_on_both_grids',
            'maximum_curvature_on_both_grids','new_metric_target_qualified_on_both_grids']),
        'original_rejection_and_all_source_state_pool_and_gate_checks_unchanged':True,
        'original_error_is_reported_not_replaced_by_a_guessed_cause':True,
        'attempted_pool_size_unavailable_if_the_frozen_setter_raised_before_recording':True,
        'no_coefficients_grid_arrays_row_ids_or_new_geometry_in_this_diagnostic':True}


def print_prefix_handoff_diagnostic(diagnostic):
    print('FROZEN159 PRE-HANDOFF DIAGNOSTIC: '+json.dumps(
        diagnostic,ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)


def handoff_restored_height159(prepared,prefix,raw_binding,*,artificial=False):
    """Validate and reuse the SAME exact height reference/H; no field is rebuilt."""
    require_frozen_prefix_sources()
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if not isinstance(problem,FiveHeightField) or not isinstance(gate,FiveNullHeightGate):
        raise ValueError('the original159 runtime field and exact null gate must survive restoration')
    if (prefix.get('schema')!=height159.SCHEMA
            or prefix.get('status')!='complete-two-grid-entry-tail-height159-audit'
            or bool(prefix.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed current temporary159 result required')
    count_keys=['growth','strip','SOC','body103','tail154']
    if (prefix.get('source_files_sha256')!=height159.implementation_hashes()
            or prefix.get('configuration')!=old_cfg or prefix.get('exact_input_storage')!=bindings
            or prefix.get('input_replay')!=old_replay
            or prefix.get('initial_state')!=problem.state_record(old_initial)
            or prefix.get('old_optimizer_calls_this_run')!=5
            or any(prefix.get('necessary_'+k+'_prefix_restoration_calls')!=1 for k in count_keys)
            or prefix.get('new_scientific_solver_calls')!=1
            or prefix.get('unchanged_complete_metric_immutable_b0_and_permanent_anchor') is not True
            or prefix.get('independent_coordinate_definition')!=problem.coordinate_definition):
        raise ValueError('sixth-prefix source/configuration/inputs/initial or exact reference identity differs')
    if not artificial and (prefix.get('github_sha')!=os.environ.get('GITHUB_SHA')
            or str(prefix.get('github_run_id'))!=os.environ.get('GITHUB_RUN_ID')
            or prefix.get('github_repository')!='Rogerhu12/math-research-public'
            or problem.nunknown!=159 or problem.physical_parameter_count!=163):
        raise ValueError('sixth prefix must be the current public job and same159/163 family')
    stage=prefix[PREFIX_STAGE]
    if stage.get('error') is not None or 'error' in stage.get('status',''):
        raise ValueError('sixth-prefix implementation failure is not a usable restoration')
    snap=stage['checkpoint'];point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('sixth-prefix selected exact159 state missing')
    checked=exact_vector(point.get('exact_binary64_independent_coordinates'),159)
    state=np.asarray(point.get('independent_coordinates_binary64'),float)
    if state.shape!=checked.shape or not np.array_equal(state,checked):
        raise ValueError('sixth-prefix numerical159 coordinates differ from exact rationals')
    state=state.copy()
    if (coefficients(state)!=point.get('exact_binary64_independent_coordinates')
            or [str(q) for q in problem.coordinates.physical_exact(state)]!=point.get('exact_original_physical_coefficients')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or point.get('coordinate_definition_sha256')!=problem.coordinate_definition_sha256
            or prefix.get('final_state')!=problem.state_record(state)
            or snap.get('independent_coordinate_definition')!=problem.coordinate_definition):
        raise ValueError('sixth-prefix canonical physical/rational-coordinate identity differs')
    accepted=snap.get('accepted_iterates',[])
    if not accepted or accepted[-1]!=point:
        raise ValueError('sixth-prefix selected state is not its last accepted state')
    if (problem.metric_model(state)!=problem.metric_model(old_initial)
            or old_replay.get('fixed_b0_definition_sha256')!=digest(problem.height_base_definition)
            or old_replay.get('exact_coordinate_definition_sha256')!=problem.coordinate_definition_sha256
            or old_replay.get('restored_original_reference_state')!=height159.state_record(
                problem.original_problem,problem.coordinates.reference_state)):
        raise ValueError('same g/b0/original binary64 reference/H must remain unchanged')
    heights=problem.coordinates.exact_heights(state);reference=problem.coordinates.reference_exact
    if (any(heights[j]!=reference[j] for j in [4,5])
            or sum(problem.null_basis.integrals[j]*(heights[j]-reference[j]) for j in range(9))!=0
            or not problem.coordinates.exact_box_decision(state,gate.original_lower,gate.original_upper)['exact_original_box_pass']):
        raise ValueError('sixth-prefix exact null sum, fixed heights or coupled original box failed')
    validation=prefix.get('final_selection_validation',{})
    if not validation.get('both_value_grids_hard_and_old_metric_pass'):
        raise ValueError('sixth-prefix independent final two-grid gates failed')
    decisions=[prefix.get(k,{}) for k in ['final_full_grid_constraints','final_doubled_constraints']]
    for d in decisions:
        if not d.get('single_grid_admissible_recovery_point'):
            raise ValueError('sixth-prefix complete-grid admissibility missing')
        for key in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
                'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']:
            if d.get(key)!=old_cfg[key]:raise ValueError('sixth-prefix gate definition differs: '+key)
    if validation.get('both_grid_maximum_eta')!=max(d['direct_max_eta'] for d in decisions):
        raise ValueError('sixth-prefix complete-grid maximum differs')
    radial,theta,grid=curvature_grid(tenth)
    if prefix.get('full_value_sampling_definition')!=grid:
        raise ValueError('sixth-prefix full sampling coordinates/structure differ')
    histories=[snap.get(k,[]) for k in ['active_row_pool_history','fine_physical_row_pool_history']]
    if not all(histories):raise ValueError('sixth-prefix full pool histories missing')
    coarse,fine=(h[-1] for h in histories);ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,total,rule,cap,previous in [
        (coarse,ci,11*len(radial)*len(theta),'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows'],old_coarse),
        (fine,fi,22*len(radial)*len(theta),'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'],old_fine)]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=list(GROUPS)
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap or not set(previous).issubset(ids)):
            raise ValueError('sixth-prefix pool IDs/order/layout/cap or inherited rows differ')
    added=fine.get('added_row_indices');fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added) or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=rows_api.fine_coordinates(added,radial,fine_theta)):
        raise ValueError('sixth-prefix fine original row coordinates differ')
    locations={}
    for d in [decisions[-1]]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('sixth-prefix metric peak is nonfinite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    continuation=restored_height159_controller(stage,old_cfg,old_replay['controller_continuation'])
    observed={'run':OBSERVED_HEIGHT159_RUN,'source':OBSERVED_HEIGHT159_SOURCE,
        'canonical_physical_state_sha256':OBSERVED_HEIGHT159_STATE,
        'temporary_complete_report_sha256':OBSERVED_HEIGHT159_REPORT_SHA,
        'raw_report_not_available_or_used_as_new_input':True}
    restoration={'schema':'same-job-temporary-frozen159-prefix-restoration-v1',
        'purpose':'necessary input restoration under metadata-only policy, not another scientific comparison',
        'prefix_scientific_implementation_sha256':height159.implementation_hashes(),
        'prefix_configuration':copy.deepcopy(old_cfg),'prefix_current_run':prefix.get('github_run_id'),
        'prefix_current_source':prefix.get('github_sha'),'prefix_temporary_raw_file':copy.deepcopy(raw_binding),
        'prefix_status':stage.get('status'),'prefix_budget_message':stage.get('budget_message'),
        'controller_continuation':continuation,'prefix_source_initial_physical_sha256':digest(problem.identity(old_initial)),
        'prefix_regenerated_final_physical_sha256':point['physical_state_sha256'],'observed_reference':observed,
        'regenerated_final_equals_observed_height159_b429':point['physical_state_sha256']==OBSERVED_HEIGHT159_STATE,
        'same_runtime_field_exact_height_reference_and_H_reused':True,
        'no_rounding_reanchoring_retry_or_forced_historical_canonical':True,
        'prefix_final_selection_validation':copy.deepcopy(validation),
        'prefix_final_gate_values':{label:{k:d.get(k) for k in ['single_grid_admissible_recovery_point',
            'previous_metric_budget_pass','hard_strip_pass','hard_ball_pass','signed_height_pass',
            'independent_direct_curvature_pass','direct_max_eta','direct_maximum_absolute_principal_curvature',
            'maximum_absolute_y','inner_strip_absolute_margin','minimum_signed_height','direct_mirror_radius_min_finite']}
            for label,d in zip(['coarse','fine'],decisions)},
        'prefix_accepted_count':len(accepted),'prefix_linear_program_count':stage.get('solver',{}).get('linear_program_invocation_count'),
        'prefix_shared_full_values':snap.get('total_full_value_physical_evaluations'),
        'prefix_optimization_active_seconds':prefix.get('optimization_active_seconds'),
        'prefix_run_audit_elapsed_seconds':prefix.get('run_audit_elapsed_seconds'),
        'prefix_preparation_elapsed_seconds':prefix.get('prepare_elapsed_seconds'),
        'prefix_failed_trials_remain_in_temporary_report_until_consumed':True,
        'prefix_report_and_summary_not_published_or_retained_after_this_job':True}
    learned={'schema':'temporary-height159-complete-learned-pool-handoff-v1',
        'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'all_previous_coarse_and_fine_integer_IDs_retained':True,
        'groups2_to10_have_original_actual_values_and_derivatives':True}
    cfg=configuration(old_cfg);replay=copy.deepcopy(old_replay)
    replay.update(schema='temporary-frozen159-to-SOC-radius-hold-in-memory-handoff-v1',
        canonical_physical_state_sha256=point['physical_state_sha256'],learned_pool=learned,
        known_fine_metric_locations=list(locations.values()),temporary_input_restoration=restoration,
        controller_continuation=continuation,
        temporary_input_restorations=copy.deepcopy(old_replay['temporary_input_restorations'])+[restoration],
        same_runtime_field_reference_and_coordinate_map_reused=True,
        source159_initial_independent_coordinate_definition_sha256=problem.coordinate_definition_sha256)
    replay['explicit_new_constraint_definition'].update(
        successful_SOC_radius_retention=retention_definition(cfg),
        original_actual_gate_and_LP_definitions_unchanged=True,
        prior159_independent_coordinate_map_and_reference_unchanged=True,
        new_height_to_body_radius_exact_is_inherited_not_new_here='4',
        no_initial_match_to_observed_height159_b429_is_assumed=True)
    return ((problem,state,gate,lower,upper,source_cfg,cfg),bindings,tenth,replay,
        np.asarray(ci,np.int64),np.asarray(fi,np.int64))



def _old_format_view(report):
    """A shallow printing adapter only; neither source report nor arrays mutate."""
    view=dict(report)
    if STAGE in view:view[height159.STAGE]=view.pop(STAGE)
    return view


def small_summary(report,out):
    answer=height159.small_summary(_old_format_view(report),out)
    if height159.STAGE in answer:
        result=answer.pop(height159.STAGE)
        result['successful_SOC_radius_retention']=retention_definition(report['configuration'])
        result['complete_original_row_floor_and_nonlinear_defect_records']['source']='temporary full report '+STAGE+'.solver.models'
        diagnostics=[]
        for m in report[STAGE].get('solver',{}).get('models',[]):
            d=m.get('accepted_SOC_base_total_step_diagnostic',{})
            u=m.get('scale_feedback_update',{}).get('successful_SOC_radius_retention',{})
            diagnostics.append({'model':m['number'],'model_result':m.get('result'),
                'diagnostic_available':d.get('available',False),'diagnostic_unavailable_reason':d.get('unavailable_reason'),
                'model_binding':copy.deepcopy(m.get('SOC_hold_model_binding')),
                'old_eta':d.get('old_true_maximum_eta'),'new_eta':d.get('accepted_true_two_grid_maximum_eta'),
                'base_total_rho':d.get('base_total_predicted_slack'),
                'base_total_predicted_drop':d.get('base_total_predicted_eta_improvement'),
                'true_drop':d.get('actual_two_grid_eta_improvement'),
                'base_total_ratio':d.get('base_total_actual_to_predicted_ratio'),
                'denominator_usable':d.get('base_total_ratio_denominator_usable'),
                'correction_norms':copy.deepcopy(d.get('actual_correction_physical_norms')),
                'total_norms':copy.deepcopy(d.get('actual_total_physical_norms')),
                'binding_checks':copy.deepcopy(d.get('binding_checks')),
                'guard_checks':copy.deepcopy(u.get('checks')),'failed_conditions':copy.deepcopy(u.get('failed_conditions')),
                'held':u.get('retained_without_growth',False),'old_radius':u.get('old_controller_next_radius'),
                'new_radius':u.get('new_next_radius'),'new_streak':u.get('new_next_success_streak')})
        result['SOC_hold_diagnostic_table']=height159._table([
            'model','model_result','diagnostic_available','diagnostic_unavailable_reason','model_binding',
            'old_eta','new_eta','base_total_rho','base_total_predicted_drop','true_drop','base_total_ratio',
            'denominator_usable','correction_norms','total_norms','binding_checks','guard_checks','failed_conditions',
            'held','old_radius','new_radius','new_streak'],diagnostics)
        answer[STAGE]=result
    answer['necessary_height159_prefix_restoration_calls']=report.get('necessary_height159_prefix_restoration_calls',0)
    if report.get('last_temporary_prefix_diagnostic') is not None:
        answer['last_temporary_prefix_diagnostic']=copy.deepcopy(report['last_temporary_prefix_diagnostic'])
    answer['successful_SOC_radius_retention_definition']=copy.deepcopy(report.get('successful_SOC_radius_retention_definition'))
    for a,r in zip(answer.get('input_restoration_conclusions',[]),report.get('temporary_input_restorations',[])):
        if 'regenerated_final_equals_observed_height159_b429' in r:
            a['regenerated_final_equals_observed_height159_b429']=r['regenerated_final_equals_observed_height159_b429']
    return answer


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


def supplementary_outcome_text(report):
    """All new controller reasons are printed; no machine coefficient payload."""
    stage=report.get(STAGE,{})
    view=_old_format_view(report)
    if stage:
        formatted_stage=dict(stage);formatted_solver=dict(stage.get('solver',{}));models=[]
        for m in formatted_solver.get('models',[]):
            item=dict(m)
            if 'scale_feedback_update' in item:
                u=item['scale_feedback_update'];h=u.get('successful_SOC_radius_retention',{})
                item['scale_feedback_update']={'next_trust':u.get('next_trust'),
                    'old_next_trust':h.get('old_controller_next_radius'),
                    'held_without_growth':h.get('retained_without_growth'),
                    'complete_new_guard_and_old_reasons_printed_in_SOC_HOLD_section_below':True}
            models.append(item)
        formatted_solver['models']=models;formatted_stage['solver']=formatted_solver;view[height159.STAGE]=formatted_stage
    text=height159.supplementary_outcome_text(view)
    text=text.replace('ENTRY/TAIL + FIVE NULL HEIGHTS:159 INDEPENDENT COORDINATES IN THE SAME163 PHYSICAL FAMILY',
        'CONDITIONAL SUCCESSFUL-SOC RADIUS RETENTION: SAME159 COORDINATES AND SAME163 PHYSICAL FAMILY')
    text=text.replace('B103/T51 retain the actual regenerated154 radius and streak. H physical radius=4B; T=B/8.',
        'B103/T51/H5 retain the actual regenerated159 radius and streak. Physical block radii remain H=4B and T=B/8.')
    text=text.replace('All five necessary prefixes are input restoration, not new scientific progress or forced historical hashes.',
        'All six necessary prefixes are input restoration, not new scientific progress or forced historical hashes.')
    lines=[text.rstrip(),'SOC HOLD POLICY: '+json.dumps(retention_definition(report['configuration']),sort_keys=True)
        if 'configuration' in report else 'SOC HOLD POLICY unavailable before initialization']
    init=stage.get('solver',{}).get('inherited159_controller_without_reset')
    if init:lines.append('ACTUAL SIXTH-PREFIX CONTROLLER: '+json.dumps(init,sort_keys=True))
    lines.append('SOC HOLD -- original primary/y-linear ratios remain in TRIAL PROGRESS; the following ratio uses actual z-x from accepted base.')
    for m in stage.get('solver',{}).get('models',[]):
        number=str(m['number']);d=m.get('accepted_SOC_base_total_step_diagnostic')
        update=m.get('scale_feedback_update');guard=None if update is None else update.get('successful_SOC_radius_retention')
        lines.append('SOC HOLD MODEL '+number+': result='+str(m.get('result'))+'; control update completed='+str(update is not None))
        lines.append('SOC HOLD MODEL BINDING '+number+': '+json.dumps(m.get('SOC_hold_model_binding'),sort_keys=True))
        for i,t in enumerate(m.get('trials',[])):
            q=t.get('scale_feedback',{})
            reason={k:q.get(k) for k in ['full_two_grid_actual_available','ratio_denominator_usable',
                'predicted_metric_improvement','actual_two_grid_eta_improvement','actual_to_predicted_ratio',
                'poor_complete_two_grid_ratio','poor_coarse_upper_bound_without_fine',
                'actual_curvature_failure_grids','request_shrink']}
            reason.update(new_coarse_rows=t.get('new_coarse_rows'),new_fine_rows=t.get('new_fine_rows'),
                coarse_omitted_hard_rows=t.get('coarse_omitted_hard_rows'),fine_omitted_hard_rows=t.get('fine_omitted_hard_rows'),
                kind=t.get('kind'),alpha=t.get('alpha_exact'),accepted=t.get('accepted_as_next_iterate'))
            lines.append('SOC HOLD OLD REASONS '+number+'/'+str(i)+': '+json.dumps(reason,sort_keys=True))
        if d is None:
            lines.append('SOC HOLD BASE TOTAL '+number+': unavailable -- no accepted full SOC diagnostic; no inferred ratio or norm.')
        else:
            lines.append('SOC HOLD BASE TOTAL '+number+': '+json.dumps(d,sort_keys=True))
        if guard is None:
            lines.append('SOC HOLD DECISION '+number+': no completed radius update; no hold or streak success inferred.')
        else:
            lines.append('SOC HOLD DECISION '+number+': '+json.dumps(guard,sort_keys=True))
    lines.append('A held radius is only the next proposal box. The original actual two-grid gates and true eta descent remain independent.')
    return '\n'.join(lines)+'\n'


def print_new_stage_outcomes(report):
    print(supplementary_outcome_text(report),end='',flush=True)

def run_pipeline(args,*,artificial=False,evaluate_only=False,process_started=None):
    started=time.monotonic() if process_started is None else process_started
    phase='public-environment-and-original24-input-contract';restorations=[];raw_bindings=[]
    last_prefix_diagnostic=None
    invoked={'growth':0,'strip':0,'SOC':0,'body103':0,'tail154':0,'height159':0,'hold':0}
    try:
        require_frozen_prefix_sources()
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        parent='/dev/shm' if artificial and Path('/dev/shm').is_dir() else os.environ.get('RUNNER_TEMP')
        with tempfile.TemporaryDirectory(prefix='visible-SOC-hold-six-inputs-',dir=parent) as folder:
            growth_out=Path(folder)/'restored-growth.json';strip_out=Path(folder)/'restored-strip.json'
            soc_out=Path(folder)/'restored-scaled-SOC.json';body_out=Path(folder)/'restored-body103.json'
            tail_out=Path(folder)/'restored-tail154.json';height_out=Path(folder)/'restored-height159.json'
            prefix_args=copy.copy(args);prefix_args.out=growth_out
            phase='strict-original24-input-preparation';before=time.monotonic()
            prepared=growth.prepare_run(prefix_args,artificial=artificial,process_started=started)
            prepare_seconds=time.monotonic()-before
            phase='one-necessary-frozen-growth-restoration';invoked['growth']=1
            previous=growth.run_audit(prepared,growth_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=prepare_seconds)
            binding=_temporary_binding(growth_out);raw_bindings.append(binding)
            phase='growth-qualified-state-and-all-pools-handoff'
            continued=strip.handoff_restored_growth(prepared,previous,binding,artificial=artificial)
            restorations.append(continued[3]['temporary_input_restoration'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'growth'),end='',flush=True)
            del previous,prepared
            phase='one-necessary-frozen-strip-restoration';invoked['strip']=1
            previous=strip.run_audit(continued,strip_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(strip_out);raw_bindings.append(binding)
            phase='strip-qualified-state-and-all-pools-controller-handoff'
            prepared_soc=soc.handoff_restored_strip(continued,previous,binding,artificial=artificial)
            restorations=list(prepared_soc[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'strip-reserve'),end='',flush=True)
            del previous,continued
            phase='one-necessary-frozen-scaled-SOC-restoration';invoked['SOC']=1
            previous=soc.run_audit(prepared_soc,soc_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(soc_out);raw_bindings.append(binding)
            phase='SOC-qualified-state-complete-pools-and-explicit-new-subspace-handoff'
            prepared_body=body103.handoff_restored_soc(prepared_soc,previous,binding,artificial=artificial)
            restorations=list(prepared_body[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'scaled-SOC'),end='',flush=True)
            print('Regenerated scaled-SOC equals observed ec76: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_SOC_ec76'])+'; never a forced replay condition.',flush=True)
            del previous,prepared_soc
            phase='one-necessary-frozen-body103-restoration';invoked['body103']=1
            previous=body103.run_audit(prepared_body,body_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(body_out);raw_bindings.append(binding)
            phase='body103-qualified-full-state-complete-pools-handoff'
            prepared_tail=tail154.handoff_restored_body103(prepared_body,previous,binding,artificial=artificial)
            restorations=list(prepared_tail[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'entry-body103'),end='',flush=True)
            print('Regenerated body103 equals observed bfbd: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_body103_bfbd'])+'; never a forced replay condition.',flush=True)
            del previous,prepared_body
            phase='one-necessary-frozen-entry-tail154-restoration';invoked['tail154']=1
            previous=tail154.run_audit(prepared_tail,tail_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(tail_out);raw_bindings.append(binding)
            phase='tail154-qualified-state-pools-controller-and-exact-height-map-handoff'
            prepared_height=height159.handoff_restored_tail154(prepared_tail,previous,binding,artificial=artificial)
            restorations=list(prepared_height[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'entry-tail154'),end='',flush=True)
            print('Regenerated tail154 equals observed2ee6: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_tail154_2ee6'])+
                '; no retry or forced canonical. This is the sixth-prefix initial state.',flush=True)
            del previous,prepared_tail
            phase='one-necessary-frozen-five-null-height159-restoration';invoked['height159']=1
            previous=height159.run_audit(prepared_height,height_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(height_out);raw_bindings.append(binding)
            phase='height159-qualified-state-full-pools-reference-and-controller-handoff'
            last_prefix_diagnostic=prefix_handoff_diagnostic(previous,binding)
            print_prefix_handoff_diagnostic(last_prefix_diagnostic)
            new_prepared=handoff_restored_height159(prepared_height,previous,binding,artificial=artificial)
            restorations=list(new_prepared[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'entry-tail-height159'),end='',flush=True)
            print('Regenerated height159 equals observed b429: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_height159_b429'])+
                '; no retry, rounding, reanchoring or forced canonical. New progress starts only here.',flush=True)
            del previous,prepared_height
            phase='one-new-conditional-successful-SOC-radius-stage';invoked['hold']=1
            return run_audit(new_prepared,args.out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
    except Exception as error:
        failure={'schema':SCHEMA,'status':'height159-SOC-hold-pipeline-failed-last-written-checkpoint-preserved',
            'phase':phase,'source_files_sha256':implementation_hashes(),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
            'necessary_growth_prefix_restoration_calls':invoked['growth'],
            'necessary_strip_prefix_restoration_calls':invoked['strip'],
            'necessary_SOC_prefix_restoration_calls':invoked['SOC'],
            'necessary_body103_prefix_restoration_calls':invoked['body103'],
            'necessary_tail154_prefix_restoration_calls':invoked['tail154'],
            'necessary_height159_prefix_restoration_calls':invoked['height159'],
            'new_scientific_solver_calls':invoked['hold'],
            'temporary_prefix_raw_bindings':raw_bindings,'temporary_input_restorations':restorations,
            'last_temporary_prefix_diagnostic':copy.deepcopy(last_prefix_diagnostic),
            'process_total_elapsed_seconds':time.monotonic()-started,
            'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
        if invoked['hold'] and Path(args.out).exists():
            try:
                existing=json.loads(Path(args.out).read_text())
                existing['scientific_status_before_pipeline_failure']=existing.get('status')
                existing['status']='height159-SOC-hold-pipeline-error-last-checkpoint-preserved';existing['pipeline_failure']=failure
                save_report(args.out,existing);return existing
            except (OSError,ValueError,TypeError,KeyError):pass
        save_report(args.out,failure);return failure


def run_audit(prepared,out,*,artificial=False,evaluate_only=False,process_started=None,prepare_seconds=0.):
    restored,bindings,tenth,replay,coarse_pool,fine_pool=prepared
    problem,initial,gate,lower,upper,source_cfg,cfg=restored
    if not isinstance(problem,FiveHeightField) or not isinstance(gate,FiveNullHeightGate):
        raise ValueError('explicit original163-to-independent159 field and gate required')
    started=time.monotonic();process_started=started if process_started is None else process_started
    metric=copy.deepcopy(problem.metric_model(initial));b0=copy.deepcopy(problem.height_base_definition)
    coord=copy.deepcopy(problem.coordinate_definition)
    actual_layout=layout_from_problem(problem.original_problem)
    subspace=EntryTailHeight159Subspace(actual_layout,problem.coordinates)
    if actual_layout!=replay['layout_derived_from_actual_problem']:
        raise ValueError('original tangent/basis layout changed after handoff')
    if digest(problem.identity(initial))!=replay['canonical_physical_state_sha256']:
        raise ValueError('same actual159 coordinates do not match the sixth-prefix state')
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':6,'necessary_growth_prefix_restoration_calls':1,
        'necessary_strip_prefix_restoration_calls':1,'necessary_SOC_prefix_restoration_calls':1,
        'necessary_body103_prefix_restoration_calls':1,'necessary_tail154_prefix_restoration_calls':1,
        'necessary_height159_prefix_restoration_calls':1,
        'new_scientific_solver_calls':0,'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':problem.state_record(initial),
        'unchanged_complete_metric_immutable_b0_and_permanent_anchor':True,
        'current_height_is_allowed_to_change_with_exact_zero_total_integral':True,
        'prepare_elapsed_seconds':prepare_seconds,'learned_pool_replay':replay['learned_pool'],
        'temporary_input_restorations':replay['temporary_input_restorations'],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'restricted_proposal_definition':restriction_definition(cfg),
        'independent_coordinate_definition':coord,
        'successful_SOC_radius_retention_definition':retention_definition(cfg),
        'initial_exact_height_diagnostic':exact_height_diagnostic(problem,initial),
        'process_clock_scope':'main includes six one-time necessary temporary prefixes plus the newSOC-hold budget; all clocks separate'}
    def save(status):
        now=time.monotonic();snapshot=report.get(STAGE,{}).get('checkpoint',{})
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=snapshot.get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('original24-inputs-six-prefixes-and-exact-height-reference-replayed-before-new-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='height159-SOC-hold-complete-initialization'
        def checkpoint(snapshot):
            report[STAGE]={'status':'current159-last-qualified-checkpoint','checkpoint':snapshot,'solver':{}}
            save('SOC-hold-last-accepted-physical-checkpoint')
        objective=SOCHold159Objective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint,
            radial_nodes_exact=grid['radial_nodes_exact'])
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            temporary_restored_height159_raw_sha256=replay['temporary_input_restoration']['prefix_temporary_raw_file']['sha256'],
            learned_pool_replay=replay['learned_pool'],temporary_input_restoration=replay['temporary_input_restoration'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-temporary-height159-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-temporary-height159-eleven-group-fine-original-IDs','source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_computed_field(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        report['initial_field_diagnostics']={g.label:field_diagnostics(d,g,subspace,cfg) for g,d in
            [(objective.row_grids[0],objective.geometry_cache),(objective.row_grids[1],objective.fine_cache['data'])]}
        save('complete-initial-original-gates-exact-height-map-and-current-height-diagnostics')
        report['phase']='one-shared-budget-height159-SOC-hold-stage';report['new_scientific_solver_calls']=1
        stage=run_soc_hold_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            restored_controller=replay['controller_continuation'],artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report[STAGE]=stage;point=stage['checkpoint'].get('selected_two_grid_physical_point')
        if point is None:
            save('no-original-two-grid-qualified159-baseline');print_new_stage_outcomes(report);return report
        checked=exact_vector(point.get('exact_binary64_independent_coordinates'),159)
        final=np.asarray(point.get('independent_coordinates_binary64'),float)
        if (final.shape!=checked.shape or not np.array_equal(final,checked)
                or coefficients(final)!=point.get('exact_binary64_independent_coordinates')
                or [str(x) for x in problem.coordinates.physical_exact(final)]!=point.get('exact_original_physical_coefficients')
                or digest(problem.identity(final))!=point['physical_state_sha256']):
            raise ValueError('selected159 independent numbers or exact163 physical state differ')
        if not problem.coordinates.exact_box_decision(final,gate.original_lower,gate.original_upper)['exact_original_box_pass']:
            raise ArithmeticError('selected exact coupled original physical box failed')
        identity=problem.identity(final);frozen,fc=problem.frozen_metric_copy(final)
        if (fc.tobytes()!=final.tobytes() or frozen.identity(fc)!=identity or frozen.metric_model(fc)!=metric
                or frozen.height_base_definition!=b0 or frozen.coordinate_definition!=coord):
            raise ArithmeticError('final freezing changed g/b0/exact physical state or coordinate map')
        problem,final=frozen,fc;report['final_state']=problem.state_record(final)
        report['final_exact_height_diagnostic']=exact_height_diagnostic(problem,final)
        reference=objective.restricted_reference;grids=objective.row_grids
        report['phase']='independent-final-same-exact-state-original384-and768-values'
        work=problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit']=audit_computed_field(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints']=recovery_decision(problem,gate,final,work,lower,upper,cfg)
        report['final_field_diagnostics']={'coarse':field_diagnostics(work,grids[0],subspace,cfg)}
        report['final_fixed_support_replay']={
            'exact_total_cap_integral_change':report['final_exact_height_diagnostic']['exact_total_cap_integral_change'],
            'physical_height_c4_c5_exactly_unchanged':report['final_exact_height_diagnostic']['physical_c4_c5_exactly_unchanged'],
            'coarse':outside_replay(reference,subspace,grids[0],work)}
        save('last159-qualified-point-recomputed-on-original-coarse-grid')
        del objective
        fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
        fine=problem.geometry(final,radial,fine_theta,order)
        report['final_doubled_angle_audit']=audit_computed_field(problem,final,fine,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints']=recovery_decision(problem,gate,final,fine,lower,upper,cfg)
        report['final_field_diagnostics']['fine']=field_diagnostics(fine,grids[1],subspace,cfg)
        report['final_fixed_support_replay']['fine']=outside_replay(reference,subspace,grids[1],fine)
        report['same_parameter_Pi_refinement']=compare_computed_fields(problem,work,fine,final)
        if problem.identity(final)!=identity:raise ArithmeticError('final Pi evaluation changed exact physical identity')
        c,f=report['final_full_grid_constraints'],report['final_doubled_constraints']
        eligible=bool(c['single_grid_admissible_recovery_point'] and f['single_grid_admissible_recovery_point'])
        maximum=max(c['direct_max_eta'],f['direct_max_eta'])
        start=max(report['initial_current_constraints']['direct_max_eta'],report['initial_doubled_constraints']['direct_max_eta'])
        new_target=bool(c['single_grid_new_target_qualified'] and f['single_grid_new_target_qualified'])
        report['final_selection_validation']={'both_value_grids_hard_and_old_metric_pass':eligible,
            'both_grid_maximum_eta':maximum,'initial_both_grid_maximum_eta':start,'actual_eta_decrease':start-maximum,
            'both_grid_maximum_curvature':max(c['direct_maximum_absolute_principal_curvature'],f['direct_maximum_absolute_principal_curvature']),
            'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
            'new_metric_target_exact':cfg['fixed_metric_budget_exact'],'new_metric_target_qualified_on_both_grids':new_target,
            'previous_qualified_budget_exact':cfg['previous_qualified_metric_budget_exact'],
            'qualification_not_assumed_from_LP_null_cap_or_constant_support':True,
            'exact_original_physical_box_checked_without_clipping':True,'whole_surface_reach_not_certified':True}
        reference_drop=float(Q(cfg['entry_tail159_effective_total_eta_drop_reference_exact']))
        report['total_drop_reference']={'reference_exact':cfg['entry_tail159_effective_total_eta_drop_reference_exact'],
            'actual_total_two_grid_eta_drop':start-maximum,'reference_met':bool(start-maximum>=reference_drop),
            'not_an_acceptance_gate_or_continuous_bound':True,
            'progress_compared_only_to_this_actual_restored_initial_state':True,
            'no_historical_best_claim_from_drifting_temporary_prefixes':True}
        count=stage['checkpoint']['total_full_value_physical_evaluations']
        report['value_evaluation_counts']={'shared_initialization_and_trial_full_values':count,
            'shared_cap':cfg['max_physical_evaluations'],'independent_final_same_state_value_calls':2,
            'total_counted_full_value_calls_in_this_new_driver':count+2,
            'six_necessary_prefix_counts_are_separate':True,
            'failed_fine_and_actual_fine_SOC_residuals_count':True,
            'old163_J_batches_are_still_computed_before_new159_mapping':True,'no_final_optimizer':True}
        report['limitations']={'all_geometric_gates_sampled_only':True,'new_target026_not_exact_isometry':True,
            'hard_cap58_not_final_reach_target':True,'full_nonlocal_reach_not_paid':True,
            'same_g_b0_and_original163_physical_family_not_expanded':True,
            'exact_null_five_coordinate_subfamily_is_not_all_nine_height_variables':True,
            'six_prefixes_each_once_not_new_scientific_progress':True,'no_forced_observed_prefix_hash':True}
        save('height159-SOC-hold-controller-error-last-qualified-preserved' if stage.get('error') else
            'complete-two-grid-height159-SOC-hold-audit' if eligible else 'final-recheck-failed-do-not-use-as-new-warm-start')
        print_new_stage_outcomes(report)
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('height159-SOC-hold-audit-error-last-checkpoint-preserved');print_new_stage_outcomes(report);return report


def _new_io_fixture():
    """New structural159 handoff fixture; no research report or surface is used."""
    from types import SimpleNamespace
    from frame_entry_tail_blocks import expected_layout
    from frame_entry_tail_height_blocks import artificial_arrays
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    layout=expected_layout();sub,_,_,_,lo,hi,_=artificial_arrays()
    cfg=height159_library.configuration(recovery_configuration(start_configuration(),target='13/50',curvature_cap='58'))
    class ToyOriginal:
        nunknown=163;metric_free=0;q_index=153
        slices={**{k:slice(*v) for k,v in layout['slices'].items()},'metric':slice(163,163)}
        height_base_definition={'schema':'new-SOC-hold-IO-immutable-b0-not-a-surface'}
        height_basis=SimpleNamespace(identity=sub.coordinates.basis.source_definition,count=9)
        source=SimpleNamespace(space_definition=lambda:{'schema':'new-SOC-hold-IO-tangent-space'})
        port=SimpleNamespace(side=1);seed=SimpleNamespace(length=.9);tail=SimpleNamespace()
        def identity(self,q):
            return {'schema':'new-SOC-hold-IO-original163',
                'height_basis_definition':copy.deepcopy(self.height_basis.identity),
                'exact_coefficients':{k:coefficients(np.asarray(q)[v]) for k,v in self.slices.items() if k!='metric'},
                'immutable_b0':copy.deepcopy(self.height_base_definition)}
        def metric_model(self,q):
            return {'schema':'new-SOC-hold-IO-fixed-g','mathematical_definition_sha256':digest({'g':'new-SOC-hold-array'})}
        def evaluation_definition(self):return {'schema':'new-SOC-hold-IO-no-surface'}
    class ToyOriginalGate:
        nunknown=163;kind='frozen-frame';side=1;length=.9;target=0.
        row=np.zeros(163);family={'schema':'new-SOC-hold-array-cap-family'}
        physical_definition={'schema':'new-SOC-hold-array-cap'};physical_sha256=digest(physical_definition)
        numerical_sha256=digest({'numerical':'new-SOC-hold-array-cap'})
        reference_provenance={'pure_artificial_arrays':True}
        def assert_context(self,p,q):
            if not isinstance(p,ToyOriginal) or np.shape(q)!=(163,):raise ValueError('array original context differs')
        def height(self,q):return 0.
        def reconstructed_height(self,d):return float(d['center'][-1])
    nodes=['0','9/250','9/100','117/1000','33/50','153/200','309/400','423/500','9/10']
    radial=np.array([float(Q(x)) for x in nodes]);theta=np.arange(4)*np.pi/2
    grid={'schema':'new-SOC-hold-small-IO-grid','radial_nodes_exact':nodes,
        'definition_sha256':digest({'nodes':nodes,'nt':4})}
    class ArrayField(FiveHeightField):
        def geometry(self,state,r,t,order,**kwargs):
            obj=height159_library._MappedArrayObjective(cfg);obj.problem=self
            obj.subspace=EntryTailHeight159Subspace(layout,self.coordinates)
            g=RationalRowGrid('coarse' if len(t)==4 else 'fine',nodes,len(t))
            data,rows,d=obj._data(state,g);data['IO_mock_decision']=d;return data
    original=ToyOriginal();reference=np.zeros(163);reference[60]=-0.;reference[154]=.125
    field=ArrayField(original,reference);initial=field.initial_state()
    selected=initial.copy();selected[0]=.0001;selected[154:]=np.array([.00002,-.00001,.00001,.00002,-.00001])
    gate=FiveNullHeightGate.from_original(ToyOriginalGate(),field,lo,hi)
    r=float(Q(1,8000));source_controller={'schema':'new-array-source154-controller',
        'trust_binary64_exact':str(Q.from_float(r)),'trust_evaluated':r,'success_streak':0,
        'origin':'new labelled array154 predecessor','unfinished_last_model_not_counted_as_success':False}
    previous={'prefix_current_run':'artificial','prefix_current_source':'artificial-no-research',
        'prefix_status':'artificial-complete','prefix_budget_message':None,
        'prefix_source_initial_physical_sha256':digest(field.identity(initial)),
        'prefix_regenerated_final_physical_sha256':digest(field.identity(initial)),
        'prefix_accepted_count':1,'prefix_linear_program_count':0,'prefix_shared_full_values':2,
        'prefix_optimization_active_seconds':0.,'prefix_run_audit_elapsed_seconds':0.,'prefix_preparation_elapsed_seconds':0.,
        'prefix_temporary_raw_file':{'filename':'artificial.json','bytes':1,'sha256':'a'*64},
        'prefix_scientific_implementation_sha256':height159.implementation_hashes(),
        'prefix_configuration':cfg,'controller_continuation':source_controller,
        'regenerated_final_equals_observed_f2bb':False,'regenerated_final_equals_observed_strip267':False,
        'regenerated_final_equals_observed_SOC_ec76':False,'regenerated_final_equals_observed_body103_bfbd':False,
        'regenerated_final_equals_observed_tail154_2ee6':False}
    replay={'schema':'new-array-prepared-frozen159','fixed_b0_definition_sha256':digest(field.height_base_definition),
        'exact_coordinate_definition_sha256':field.coordinate_definition_sha256,
        'restored_original_reference_state':height159.state_record(original,reference),
        'controller_continuation':source_controller,'temporary_input_restoration':previous,
        'temporary_input_restorations':[copy.deepcopy(previous) for _ in range(5)],
        'layout_derived_from_actual_problem':layout,'explicit_new_constraint_definition':{},
        'canonical_physical_state_sha256':digest(field.identity(initial)),
        'complete_metric_sha256':field.metric_model(initial)['mathematical_definition_sha256'],
        'physical_parameter_count':163,'independent_coordinate_count':159}
    binding={'filename':'artificial-frozen159.json','bytes':1,'sha256':'e'*64}
    bindings={'fixture':{'decoded_sha256':'f'*64,'decoded_bytes':1,'stored_sha256':'f'*64,
        'stored_bytes':1,'gzip_storage':False}}
    tenth={'fixture':'new-SOC-hold-grid','selected_raw_auxiliary_delta':.2}
    prepared=((field,initial,gate,gate.coordinate_lower,gate.coordinate_upper,{'primitive_order':2,'tau':'61/1000'},cfg),
        bindings,tenth,replay,np.array([0,128]),np.array([0,256]))
    d={k:cfg[k] for k in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
        'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']}
    d.update(single_grid_admissible_recovery_point=True,direct_max_eta=.2665,
        direct_max_eta_location={'t':.66,'theta':0.},direct_maximum_absolute_principal_curvature=2.,
        hard_strip_pass=True,hard_ball_pass=True,signed_height_pass=True,independent_direct_curvature_pass=True,
        previous_metric_budget_pass=True,maximum_absolute_y=.1,inner_strip_absolute_margin=.28999,
        minimum_signed_height=.05,direct_mirror_radius_min_finite=.1)
    def pool(ids,fine=False):
        nt=8 if fine else 4
        record={'version':1,'row_indices':ids,'added_row_indices':ids,'row_count':len(ids),
            'row_indices_sha256':digest(ids),'group_order':list(GROUPS),'total_full_grid_rows':11*len(radial)*nt,
            'flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index' if fine
                else 'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'}
        if fine:record['added_original_grid_coordinates']=rows_api.fine_coordinates(ids,radial,np.arange(nt)*2*np.pi/nt)
        return record
    point={'independent_coordinates_binary64':selected.tolist(),
        'exact_binary64_independent_coordinates':coefficients(selected),
        'exact_original_physical_coefficients':[str(x) for x in field.coordinates.physical_exact(selected)],
        'physical_state_sha256':digest(field.identity(selected)),
        'coordinate_definition_sha256':field.coordinate_definition_sha256}
    quality={'full_two_grid_actual_available':True,'ratio_denominator_usable':True,
        'actual_to_predicted_ratio':.9,'request_shrink':False}
    model={'number':1,'trust_before_model':r,'scale_feedback_trials':[quality],
        'linear_program':{'primary_step_cost_diagnostic':{'actual_trust_normalized_step_norm':1.}},
        'corrections':[],'result':'accepted-two-grid-true-metric-descent',
        'trials':[{'kind':'primary-metric-short-step','alpha_exact':'1','accepted_as_next_iterate':True,
            'new_coarse_rows':0,'new_fine_rows':0,'coarse_decision':d,'fine_decision':d,'scale_feedback':quality}]}
    next_radius,next_streak,feedback=height159_library.next_mapped_trust(model,r,0,cfg)
    model['scale_feedback_update']=feedback
    init={'restored_entry_tail154_controller_inherited':source_controller,
        'inherited_body_radius_exact_binary64':str(Q.from_float(r)),
        'inherited_tail_radius_exact_binary64':str(Q.from_float(r)/8),
        'new_height_radius_exact_binary64':str(4*Q.from_float(r)),
        'inherited_success_streak':0,'height_to_body_radius_is_new_parameter_exact':'4',
        'no_reset_when_restoration_is_below_original_minimum':True}
    prefix={'schema':height159.SCHEMA,'status':'complete-two-grid-entry-tail-height159-audit',
        'source_files_sha256':height159.implementation_hashes(),'configuration':cfg,'artificial_inputs_only':True,
        'exact_input_storage':bindings,'input_replay':replay,'initial_state':field.state_record(initial),
        'final_state':field.state_record(selected),'old_optimizer_calls_this_run':5,
        **{'necessary_'+k+'_prefix_restoration_calls':1 for k in ['growth','strip','SOC','body103','tail154']},
        'new_scientific_solver_calls':1,'unchanged_complete_metric_immutable_b0_and_permanent_anchor':True,
        'independent_coordinate_definition':field.coordinate_definition,
        'github_sha':'artificial-no-science','github_run_id':'artificial','github_repository':'Rogerhu12/math-research-public',
        'full_value_sampling_definition':grid,'initial_current_constraints':d,'initial_doubled_constraints':copy.deepcopy(d),
        'final_full_grid_constraints':copy.deepcopy(d),'final_doubled_constraints':copy.deepcopy(d),
        'final_selection_validation':{'both_value_grids_hard_and_old_metric_pass':True,'both_grid_maximum_eta':.2665},
        PREFIX_STAGE:{'status':'shared-value-time-or-pool-budget-exit','error':None,
            'last_restricted_trust':next_radius,'final_consecutive_growth_qualifying_models':next_streak,
            'solver':{'inherited154_plus_new_height_controller':init,'linear_program_invocation_count':1,
                'models':[model,{'number':2,'trust_before_model':next_radius,'trials':[{'attempt_status':'not-completed'}]}]},
            'checkpoint':{'selected_two_grid_physical_point':point,'accepted_iterates':[point],
                'independent_coordinate_definition':field.coordinate_definition,
                'active_row_pool_history':[pool([0,1,128])],
                'fine_physical_row_pool_history':[pool([0,1,256],True)],
                'saved_fine_trials':[],'total_full_value_physical_evaluations':4}}}
    return {'prepared':prepared,'prefix':prefix,'binding':binding,'layout':layout,'nodes':nodes,
        'radial':radial,'theta':theta,'grid':grid,'selected':selected,'pool_builder':pool}


def developer_check():
    """Only new rule, sixth-handoff, IO and dispatch; old suites are never called."""
    import contextlib
    import io
    import sys
    from types import SimpleNamespace
    from unittest.mock import patch
    library=hold_check();fixture=_new_io_fixture();module=sys.modules[__name__]
    prepared,prefix,binding=(fixture[k] for k in ['prepared','prefix','binding'])
    nodes,radial,theta,grid=(fixture[k] for k in ['nodes','radial','theta','grid'])
    layout=fixture['layout'];before=copy.deepcopy(prefix)
    with patch.object(module,'curvature_grid',return_value=(radial,theta,grid)):
        continued=handoff_restored_height159(prepared,prefix,binding,artificial=True)
        field,state,gate,lo,hi,source_cfg,cfg=continued[0]
        handoff_ok=bool(field is prepared[0][0] and gate is prepared[0][2]
            and state.tobytes()==fixture['selected'].tobytes()
            and field.coordinates.reference_state.tobytes()==prepared[0][0].coordinates.reference_state.tobytes()
            and field.identity(state)==prefix['final_state']['complete_physical_definition']
            and continued[3]['restored_original_reference_state']==prepared[3]['restored_original_reference_state']
            and len(continued[3]['temporary_input_restorations'])==6
            and continued[3]['controller_continuation']['success_streak']==1
            and continued[3]['controller_continuation']['unfinished_last_model_not_counted_as_success'])
        rejected={}
        for name in ['independent-coefficient','derived-rational-height','coordinate-reference','source','pool',
                'controller','sampling','fine-gate','implementation-error']:
            bad=copy.deepcopy(prefix)
            point=bad[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']
            if name=='independent-coefficient':point['exact_binary64_independent_coordinates'][0]='123'
            elif name=='derived-rational-height':point['exact_original_physical_coefficients'][157]='0'
            elif name=='coordinate-reference':bad['independent_coordinate_definition']['schema']='different-map'
            elif name=='source':bad['source_files_sha256']['frame_metric_entry_tail_height159.py']='0'*64
            elif name=='pool':bad[PREFIX_STAGE]['checkpoint']['fine_physical_row_pool_history'][-1]['row_indices']=[0]
            elif name=='controller':bad[PREFIX_STAGE]['final_consecutive_growth_qualifying_models']=0
            elif name=='sampling':bad['full_value_sampling_definition']['radial_nodes_exact'][2]='1/10'
            elif name=='fine-gate':bad['final_doubled_constraints']['single_grid_admissible_recovery_point']=False
            else:bad[PREFIX_STAGE]['error']={'type':'RuntimeError','message':'new injected implementation failure'}
            try:handoff_restored_height159(prepared,bad,binding,artificial=True);rejected[name]=False
            except (ValueError,KeyError):rejected[name]=True
    immutable=prefix==before
    # Every necessary old run is stubbed at its boundary. No old controller,
    # geometry, or development suite runs merely to cover the new pipeline IO.
    calls={k:0 for k in ['prepare','growth','strip','SOC','body103','tail154','height159','new']};temporary=[]
    shallow={k:copy.deepcopy(prefix[k]) for k in ['initial_current_constraints','initial_doubled_constraints',
        'final_full_grid_constraints','final_doubled_constraints']}
    def prepare_stub(args,**kwargs):calls['prepare']+=1;return ('opaque-original24-preparation',)
    def run_stub(label,data):
        def run(p,out,**kwargs):
            calls[label]+=1;temporary.append(Path(out));atomic_save(out,data);return copy.deepcopy(data)
        return run
    def new_stub(p,out,**kwargs):
        calls['new']+=1
        if len(p[3]['temporary_input_restorations'])!=6:raise AssertionError('six restoration records required')
        result={'schema':SCHEMA,'status':'new-SOC-hold-pure-array-stage-stub',
            'temporary_input_restorations':p[3]['temporary_input_restorations'],STAGE:{'solver':{},'checkpoint':{}}}
        atomic_save(out,result);return result
    def patch_pipeline(stack,runner):
        stack.enter_context(patch.object(module,'curvature_grid',return_value=(radial,theta,grid)))
        stack.enter_context(patch.object(growth,'prepare_run',side_effect=prepare_stub))
        for mod,label,data in [(growth,'growth',shallow),(strip,'strip',shallow),(soc,'SOC',shallow),
                (body103,'body103',shallow),(tail154,'tail154',shallow),(height159,'height159',prefix)]:
            stack.enter_context(patch.object(mod,'run_audit',side_effect=run_stub(label,data)))
        for mod,name in [(strip,'handoff_restored_growth'),(soc,'handoff_restored_strip'),
                (body103,'handoff_restored_soc'),(tail154,'handoff_restored_body103'),
                (height159,'handoff_restored_tail154')]:
            stack.enter_context(patch.object(mod,name,return_value=prepared))
        stack.enter_context(patch.object(module,'run_audit',side_effect=runner))
    directory='/dev/shm' if Path('/dev/shm').is_dir() else None
    with tempfile.TemporaryDirectory(prefix='SOC-hold-new-IO-',dir=directory) as folder:
        args=SimpleNamespace(out=Path(folder)/'new-audit.json');printed=io.StringIO()
        with contextlib.ExitStack() as stack:
            patch_pipeline(stack,new_stub);stack.enter_context(contextlib.redirect_stdout(printed))
            result=run_pipeline(args,artificial=True,evaluate_only=True)
        once=all(v==1 for v in calls.values())
        unique=bool([p.name for p in Path(folder).glob('*-audit.json')]==['new-audit.json']
            and all(not p.exists() for p in temporary)
            and [k for k,v in result.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        prefix_print=all(s in printed.getvalue() for s in ['RESTORATION growth','RESTORATION strip-reserve',
            'RESTORATION scaled-SOC','RESTORATION entry-body103','RESTORATION entry-tail154',
            'RESTORATION entry-tail-height159','Regenerated height159 equals observed b429:',
            'initial_doubled_constraints','final_doubled_constraints'])
        bad_args=SimpleNamespace(out=Path(folder)/'failure.json')
        with patch.object(growth,'prepare_run',side_effect=ValueError('new SOC-hold loader exception')):
            bad=run_pipeline(bad_args,artificial=True,evaluate_only=True)
        failure_ok=bool(bad['phase']=='strict-original24-input-preparation'
            and bad['necessary_growth_prefix_restoration_calls']==0 and bad['new_scientific_solver_calls']==0
            and json.loads(bad_args.out.read_text())['error']['type']=='ValueError')
    class DriverArrayObjective(height159_library._MappedArrayObjective):
        def __init__(self,problem,gate,radial,theta,order,lower,upper,*,cfg,checkpoint,radial_nodes_exact):
            super().__init__(cfg);self.problem=problem;self.gate=gate
            self.subspace=EntryTailHeight159Subspace(layout,problem.coordinates)
            if list(radial_nodes_exact)!=nodes or not np.array_equal(radial,self.radial):raise ValueError('new array grid differs')
            self.lower=np.asarray(lower).copy();self.upper=np.asarray(upper).copy()
            self.physical_lower=gate.original_lower;self.physical_upper=gate.original_upper
            self.checkpoint=checkpoint;self.pool_history=[];self.fine_history=[]
        def set_pool(self,ids,reason):
            self.pool=np.asarray(ids,np.int64).copy();self.pool_history.append(fixture['pool_builder'](self.pool.tolist()))
        def set_fine_pool(self,ids,reason):
            self.fine_pool=np.asarray(ids,np.int64).copy();self.fine_history.append(fixture['pool_builder'](self.fine_pool.tolist(),True))
        def snapshot(self):
            value=super().snapshot();value['active_row_pool_history']=copy.deepcopy(self.pool_history)
            value['fine_physical_row_pool_history']=copy.deepcopy(self.fine_history)
            return value
    def compare_arrays(p,a,b,state):
        return {'same_artificial_exact_state':True,'physical_identity_sha256':digest(p.identity(state)),
            'position_jet_differences':{k:float(np.max(abs(a[k]-b[k][:,::2]))) for k in POSITION_JETS}}
    with tempfile.TemporaryDirectory(prefix='SOC-hold-new-main-',dir=directory) as folder:
        out=Path(folder)/'new-audit.json';printed=io.StringIO()
        with patch.object(module,'curvature_grid',return_value=(radial,theta,grid)), \
                patch.object(module,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)), \
                patch.object(module,'SOCHold159Objective',DriverArrayObjective), \
                patch.object(module,'audit_computed_field',side_effect=lambda *a,**k:{'new_artificial_arrays_not_surface':True}), \
                patch.object(module,'compare_computed_fields',side_effect=compare_arrays), \
                patch.object(module,'recovery_decision',side_effect=lambda p,g,s,d,*a,**k:d['IO_mock_decision']), \
                patch.object(tail154,'geometry_values',side_effect=lambda d:{'eta':d['eta'],'e':d['e'],'f':d['f']}), \
                contextlib.redirect_stdout(printed):
            full=run_audit(continued,out,artificial=True,evaluate_only=True)
        raw=out.read_bytes();native=json.loads(summary_path(out).read_text())
        full_ok=bool(full.get('status')=='complete-two-grid-height159-SOC-hold-audit'
            and full[STAGE]['solver']['linear_program_invocation_count']==0
            and full['initial_state']==full['final_state']
            and full['final_selection_validation']['both_value_grids_hard_and_old_metric_pass']
            and full['final_exact_height_diagnostic']['exact_total_cap_integral_change']=='0'
            and full[STAGE]['solver']['inherited159_controller_without_reset']['inherited_success_streak']==1
            and native['full_report']['sha256']==hashlib.sha256(raw).hexdigest()
            and [k for k,v in native.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        scientific_print=all(s in printed.getvalue() for s in ['SOC HOLD POLICY','ACTUAL SIXTH-PREFIX CONTROLLER',
            'MAPPED MODELS','CURRENT HEIGHT','final_selection_validation','ORIGINAL UNIT DUAL'])
        # Insert a newly constructed array guard record for printer coverage;
        # never evaluate or reconstruct an old scientific model6.
        fixture_cfg,_,_,_,_,newmodel=hold_library._new_array_fixture()
        _,_,feedback=hold_library.next_soc_hold_trust(newmodel,newmodel['trust_before_model'],1,fixture_cfg)
        newmodel['scale_feedback_update']=feedback
        logged=copy.deepcopy(full);logged[STAGE]['solver']['models']=[newmodel]
        text=supplementary_outcome_text(logged)
        guard_print=all(s in text for s in ['SOC HOLD MODEL BINDING','SOC HOLD OLD REASONS',
            'SOC HOLD BASE TOTAL','SOC HOLD DECISION','base_total_predicted_eta_improvement',
            'actual_correction_physical_norms','actual_total_physical_norms','old_controller_result',
            'qualified_to_retain_model_radius'])
        guard_summary=small_summary(logged,out)
        guard_table=guard_summary[STAGE]['SOC_hold_diagnostic_table']
        summary_ok=bool(len(guard_table['rows'])==1 and 'base_total_ratio' in guard_table['columns'])
        def save_then_fail(p,out,**kwargs):
            save_report(out,full);raise RuntimeError('new SOC-hold failure after checkpoint')
        args=SimpleNamespace(out=Path(folder)/'preserved-audit.json')
        with contextlib.ExitStack() as stack:
            patch_pipeline(stack,save_then_fail);stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            kept=run_pipeline(args,artificial=True,evaluate_only=True)
        keep_ok=bool(kept.get('status')=='height159-SOC-hold-pipeline-error-last-checkpoint-preserved'
            and kept.get('final_state')==full.get('final_state') and kept.get(STAGE)==full.get(STAGE)
            and kept.get('pipeline_failure',{}).get('error',{}).get('type')=='RuntimeError')
        marker={'schema':'new-SOC-hold-main-branch-only','passed':True,'artificial_inputs_only':True}
        devout=Path(folder)/'development.json'
        with patch.object(module,'developer_check',return_value=marker), \
                patch.object(sys,'argv',[__file__,'--check-only','--out',str(devout)]), \
                contextlib.redirect_stdout(io.StringIO()):main()
        cli_ok=json.loads(devout.read_text()).get('passed') is True
    try:require_public_actions('true','WrongOwner/OtherRepository',[]);guard=False
    except (ValueError,PermissionError,RuntimeError):guard=True
    checks={
        'new_array_radius_retention_branches':library['passed'],
        'sixth_handoff_reuses_exact_runtime_reference_H_and_real159_controller':handoff_ok,
        'source_prefix_dictionary_is_not_modified':immutable,
        'all_new_handoff_corruptions_rejected':all(rejected.values()),
        'six_old_prefix_boundaries_called_once_and_one_new_stage':once,
        'one_top_level_audit_and_stage_and_temporary_prefix_cleanup':unique,
        'six_prefix_gates_costs_and_actual_hash_relation_printed':prefix_print,
        'input_failure_writes_small_JSON':failure_ok,
        'new_evaluation_only_driver_complete_IO_finalfreeze_and_summary_binding':full_ok,
        'ordinary_geometry_and_original_unit_diagnostics_printed':scientific_print,
        'all_new_guard_quality_norm_reason_and_identity_fields_printed':guard_print,
        'new_native_summary_retains_guard_table':summary_ok,
        'post_checkpoint_failure_preserves_state_and_stage':keep_ok,
        'new_check_only_dispatch_does_not_repeat_development':cli_ok,
        'wrong_public_repository_rejected':guard}
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema':SCHEMA+'-new-development-only','passed':bool(all(checks.values())),
        'artificial_inputs_only':True,'checks':checks,'new_library_checks':library,
        'new_handoff_rejections':rejected,'new_pipeline_call_counts_across_success_and_failure_paths':calls,
        'new_pipeline_status':result.get('status'),'new_pipeline_error':result.get('error'),
        'new_artificial_audit_status':full.get('status'),'new_artificial_audit_error':full.get('error'),
        'new_artificial_stage_error':full.get(STAGE,{}).get('error'),
        'old_development_suites_and_scientific_prefixes_not_executed':True,
        'research_candidate_constructed_evaluated_or_optimized':False}



def prefix_diagnostic_developer_check():
    """Only the new missing-error branch; no old suite, geometry or solver."""
    import contextlib
    import io
    import sys
    from types import SimpleNamespace
    from unittest.mock import patch
    module=sys.modules[__name__]
    sentinel='new artificial frozen-prefix initialization exception'
    fixture={'schema':height159.SCHEMA,
        'status':'entry-tail-height159-controller-error-last-qualified-preserved',
        'phase':'independent-final-same-exact-state-original384-and768-values',
        'artificial_inputs_only':True,'github_sha':'new-array-source',
        'configuration':{'max_pool_rows':100,'max_fine_physical_pool_rows':4096},
        PREFIX_STAGE:{'status':'entry-tail-height159-recovery-error',
            'error':{'type':'ValueError','message':sentinel},'budget_message':None,
            'solver':{'linear_program_invocation_count':0,'primary_LP_invocation_count':0,
                'correction_LP_invocation_count':0,'models':[],
                'initial_pre_LP_decision':{'status':'new-array-preflight','may_call_LP':True}},
            'last_pre_LP_decision':{'status':'new-array-preflight','may_call_LP':True},
            'checkpoint':{'total_full_value_physical_evaluations':2,'jacobian_refreshes':0,
                'optimization_elapsed_seconds':None,
                'active_row_pool_history':[{'version':1,'row_count':3,'row_indices':[1,2,3],
                    'row_indices_sha256':'artificial-coarse-pool'}],
                'fine_physical_row_pool_history':[{'version':2,'row_count':4,'row_indices':[1,2,3,4],
                    'row_indices_sha256':'artificial-fine-pool'}],
                'selected_two_grid_physical_point':{'physical_state_sha256':'artificial-qualified-point',
                    'maximum_eta_on_both_grids':.2,
                    'physical_parameter_coefficients_binary64':['MUST_NOT_PRINT_MACHINE_COEFFICIENTS']}}}}
    before=copy.deepcopy(fixture)
    binding={'name':'artificial-frozen159.json','bytes':1,'sha256':'artificial-raw-binding'}
    diagnostic=prefix_handoff_diagnostic(fixture,binding)
    text=json.dumps(diagnostic,allow_nan=False)
    direct=bool(diagnostic['stage_error']==fixture[PREFIX_STAGE]['error']
        and diagnostic['prefix']['status']==fixture['status']
        and diagnostic['stage_status']==fixture[PREFIX_STAGE]['status']
        and diagnostic['pool_metadata']['fine']['capacity']==4096
        and diagnostic['pool_metadata']['fine']['row_count']==4
        and diagnostic['last_pre_LP_decision']==fixture[PREFIX_STAGE]['last_pre_LP_decision'])
    omitted=bool('MUST_NOT_PRINT_MACHINE_COEFFICIENTS' not in text
        and '"row_indices":' not in text and fixture==before)
    missing=prefix_handoff_diagnostic({'schema':'artificial-without-stage'},binding)
    no_guess=bool(missing['stage_status'] is None and missing['stage_error']=={}
        and missing['last_pre_LP_decision'] is None
        and missing['pool_metadata']['fine']['capacity'] is None)
    class Problem:pass
    class Gate:pass
    restoration={'regenerated_final_equals_observed_SOC_ec76':False,
        'regenerated_final_equals_observed_body103_bfbd':False,
        'regenerated_final_equals_observed_tail154_2ee6':False}
    prepared=((Problem(),None,Gate(),None,None,{},{}),{}, {},
        {'temporary_input_restoration':restoration,'temporary_input_restorations':[restoration]},None,None)
    counters={k:0 for k in ['growth','strip','SOC','body103','tail154','height159','new']}
    temporary=[]
    def stub(label):
        def run(p,out,**kwargs):
            counters[label]+=1;temporary.append(Path(out))
            result=copy.deepcopy(fixture) if label=='height159' else {'schema':'prior-prefix-array-stub'}
            atomic_save(out,result);return result
        return run
    def forbidden_new(*args,**kwargs):
        counters['new']+=1;raise AssertionError('new scientific stage must not run after prefix error')
    def forbidden_development(*args,**kwargs):
        raise AssertionError('already completed development suites must not run')
    directory='/dev/shm' if Path('/dev/shm').is_dir() else None
    with tempfile.TemporaryDirectory(prefix='SOC-hold-prefix-diagnostic-only-',dir=directory) as folder:
        args=SimpleNamespace(out=Path(folder)/'diagnostic-failure.json');printed=io.StringIO()
        with contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(module,'require_frozen_prefix_sources',return_value=None))
            stack.enter_context(patch.object(module,'FiveHeightField',Problem))
            stack.enter_context(patch.object(module,'FiveNullHeightGate',Gate))
            stack.enter_context(patch.object(module,'developer_check',side_effect=forbidden_development))
            stack.enter_context(patch.object(module,'hold_check',side_effect=forbidden_development))
            stack.enter_context(patch.object(growth,'prepare_run',return_value=prepared))
            stack.enter_context(patch.object(soc,'prefix_outcome_text',return_value='new artificial prior prefix stub\n'))
            for mod,label in [(growth,'growth'),(strip,'strip'),(soc,'SOC'),(body103,'body103'),
                    (tail154,'tail154'),(height159,'height159')]:
                stack.enter_context(patch.object(mod,'run_audit',side_effect=stub(label)))
            for mod,name in [(strip,'handoff_restored_growth'),(soc,'handoff_restored_strip'),
                    (body103,'handoff_restored_soc'),(tail154,'handoff_restored_body103'),
                    (height159,'handoff_restored_tail154')]:
                stack.enter_context(patch.object(mod,name,return_value=prepared))
            stack.enter_context(patch.object(module,'run_audit',side_effect=forbidden_new))
            # Only serialization is simplified; real run_pipeline and the real
            # unsuccessful-status check in handoff_restored_height159 execute.
            stack.enter_context(patch.object(module,'save_report',side_effect=atomic_save))
            stack.enter_context(contextlib.redirect_stdout(printed))
            result=run_pipeline(args,artificial=True,evaluate_only=True)
        written=json.loads(args.out.read_text())
        failure_kept=bool(result['error']['message']=='completed current temporary159 result required'
            and written['last_temporary_prefix_diagnostic']['stage_error']==fixture[PREFIX_STAGE]['error']
            and result['new_scientific_solver_calls']==0 and counters['new']==0
            and all(counters[k]==1 for k in counters if k!='new'))
        output_ok=bool(sentinel in printed.getvalue()
            and 'FROZEN159 PRE-HANDOFF DIAGNOSTIC:' in printed.getvalue()
            and 'entry-tail-height159-controller-error-last-qualified-preserved' in printed.getvalue())
        cleaned=bool(temporary and all(not p.exists() for p in temporary))
        with patch.object(height159,'small_summary',return_value={}):
            summary=small_summary(result,args.out)
        summary_ok=bool(summary['last_temporary_prefix_diagnostic']==written['last_temporary_prefix_diagnostic'])
        marker={'schema':'new-prefix-diagnostic-dispatch-only','passed':True,'artificial_inputs_only':True}
        devout=Path(folder)/'diagnostic-development.json'
        with patch.object(module,'prefix_diagnostic_developer_check',return_value=marker), \
                patch.object(module,'developer_check',side_effect=forbidden_development), \
                patch.object(sys,'argv',[__file__,'--check-prefix-diagnostic-only','--out',str(devout)]), \
                contextlib.redirect_stdout(io.StringIO()):
            main()
        dispatch=json.loads(devout.read_text()).get('passed') is True
    checks={k:bool(v) for k,v in {
        'original_status_error_budget_and_available_metadata_preserved':direct,
        'machine_arrays_omitted_and_prefix_unchanged':omitted,
        'unavailable_original_error_not_invented':no_guess,
        'real_original_unsuccessful_status_check_still_rejects_before_new_science':failure_kept,
        'original_inner_exception_printed_before_cleanup':output_ok,
        'failure_native_summary_preserves_same_diagnostic':summary_ok,
        'temporary_prefixes_cleaned_after_diagnostic_is_retained':cleaned,
        'targeted_new_CLI_does_not_dispatch_old_development':dispatch}.items()}
    return {'schema':SCHEMA+'-prefix-diagnostic-development-only',
        'passed':bool(all(checks.values())),'checks':checks,'artificial_inputs_only':True,
        'fixture_prefix_calls_are_dictionary_stubs_only':True,
        'old_completed_development_suites_not_executed':True,
        'geometry_solver_or_scientific_prefix_not_executed':True}


def main():
    started=time.monotonic();parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--check-prefix-diagnostic-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    if args.check_only and args.check_prefix_diagnostic_only:
        parser.error('choose one development branch')
    if args.check_only or args.check_prefix_diagnostic_only:
        try:result=prefix_diagnostic_developer_check() if args.check_prefix_diagnostic_only else developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':SCHEMA+'-development-error','passed':False,'artificial_inputs_only':True,
                'source_files_sha256':implementation_hashes(),'process_total_elapsed_seconds':time.monotonic()-started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(),process_total_elapsed_seconds=time.monotonic()-started)
        atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    report=run_pipeline(args,process_started=started)
    print(json.dumps({'out':str(args.out),'status':report.get('status')}),flush=True)
    if report.get('status')!='complete-two-grid-height159-SOC-hold-audit':raise SystemExit(1)


if __name__=='__main__':main()


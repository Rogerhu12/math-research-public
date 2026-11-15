#!/usr/bin/env python3
"""Five necessary temporary prefixes, then one same-g five-null-height159 stage.

All research geometry and optimization require public Actions. The original
24 input byte streams restore growth/strip/scaled-SOC/body103/tail154 once each.
The new stage inherits the actual154 state, pools, B/T trust and success streak;
it adds five exact zero-total-integral height directions with H radius4*B.
Only ephemeral reports are written. The publisher retains metadata, not payload.
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
from frame_entry_short_bounded_audit import audit_data
from frame_independent_height_solve import point_values,objective_cost
from frame_independent_height_solve import state_record
from frame_curvature_epigraph_exchange import GROUPS
from frame_metric_budget_recovery import recovery_decision
from frame_metric_epigraph import geometry_values
from frame_metric_spectral_recovery import EPSILON_EXACT,PROPOSAL_BRANCHES,spectral_proposal_rows
from frame_curvature_soc_metric_reserve_audit import exact_vector
import frame_metric_budget_restoration_rows as rows_api
import frame_metric_spectral_trust_growth_audit as growth
import frame_metric_spectral_strip_reserve_audit as strip
import frame_metric_spectral_soc_scaling_audit as soc
import frame_metric_entry_body103_audit as body103
import frame_metric_entry_tail154_audit as tail154
import frame_metric_entry_tail154 as tail154_library
from frame_entry_tail_blocks import EntryTail154Subspace,RationalRowGrid
from frame_metric_entry_tail_height159 import (
    EntryTailHeight159Objective,run_mapped_recovery,
    configuration,implementation_hashes as library_hashes,developer_check as mapped_check,
    restriction_definition,growth_definition,layout_from_problem,POSITION_JETS,
    strip_floor_definition,penalty_definition,floor_definition,scaling_definition)
from frame_five_height_field import FiveHeightField
from frame_height_null_gate import FiveNullHeightGate
from frame_entry_tail_height_blocks import EntryTailHeight159Subspace

SCHEMA='same-g-entry-tail-height159-after-five-temporary-prefixes-audit-v1'
STAGE='metric_entry_tail_height159_stage'
PREFIX_STAGE=tail154.STAGE
OBSERVED_TAIL154_RUN='43694686825'
OBSERVED_TAIL154_SOURCE='71744524b9001226332866870515281d35f49910'
OBSERVED_TAIL154_STATE='2ee6e90e17527b18345b9a72003507391aa77bf152981b08d331ce18921808c2'
OBSERVED_TAIL154_REPORT_SHA='58335c549aa84d15b9cb3886d75ffb8bbfa3f5d8a359b1350d3996a9b09aaeee'
FROZEN_PREFIX_SOURCE_SHA256={
    'frame_metric_spectral_trust_growth.py':'19394bea4779c4497851c169a15dddad5839469067d550f64bef7af3bb88dcc6',
    'frame_metric_spectral_strip_reserve.py':'0d653e66947b95efe56e518e8bf4705076bc9ef687e5a596a1884b8367d22ae3',
    'frame_metric_spectral_strip_reserve_audit.py':'4347bdc3afc2504b2a6546d41176e0e3a9e340533ee1eee16ff831257e149e38',
    'frame_second_order_correction_scaling.py':'3b74cc8cc840aaece3aaf4c188728fffff4a7409289d65d1aba6aeb9e70ef98f',
    'frame_metric_spectral_soc_scaling.py':'6e3ef11a7ee232436d609573de970a55be58858dac9364323383c37313a44958',
    'frame_metric_spectral_soc_scaling_audit.py':'d09cd8b4e435d252aaa56b0a14f13dce69b6904597b8c4e4c75753d1fe670966',
    'frame_entry_body_subspace.py':'09f91a1d53c807ff58bb8862c7e7765cb21d09ca93bc0ccfc100f19ef446d022',
    'frame_metric_entry_body103.py':'7054eaa6466f5f5b8bdc8f595bbdd2b1747b2063908cfaecd506d74084a08fd3',
    'frame_metric_entry_body103_audit.py':'90a03cea625d73822183019df269c1bd8713a9c66aacb4adf54644719939413c',
    'frame_entry_tail_blocks.py':'796d6498de093d2a8ccc4090c3b9ff67205f8e652b93ad7427b37b96b08b6bf1',
    'frame_metric_entry_tail154.py':'650b4b0d65bda69be6ee672e79054466bdaeb7bdebdf830e4b9449c78a6a7c22',
    'frame_metric_entry_tail154_audit.py':'5d10b3b3ecc33c5dd97b7417705e02697710bde0ec51d64ff9ee0edb907e0345'}
INPUTS=growth.INPUTS
SHA_NAMES=growth.SHA_NAMES
coefficients=growth.coefficients
curvature_grid=growth.curvature_grid
summary_path=growth.summary_path
GATE_ORDER=soc.GATE_ORDER
GATE_NUMBERS=soc.GATE_NUMBERS
_scalar=soc._scalar
_gate_codes=soc._gate_codes


def implementation_hashes():
    result=tail154.implementation_hashes();result.update(library_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def require_frozen_prefix_sources():
    actual=tail154.implementation_hashes()
    for name,expected in FROZEN_PREFIX_SOURCE_SHA256.items():
        if actual.get(name)!=expected:raise ValueError('necessary temporary prefix source differs: '+name)


def restored_tail154_controller(stage,cfg):
    tail154_library.restriction_definition(cfg)
    radius=float(Q(cfg['entry_tail154_initial_trust_exact']));streak=0
    models=stage.get('solver',{}).get('models',[]);without_update=False
    for i,model in enumerate(models):
        if model.get('number')!=i+1 or model.get('trust_before_model')!=radius:
            raise ValueError('restored154 sequential model/controller radius differs')
        feedback=model.get('scale_feedback_update')
        if feedback is None:
            if i!=len(models)-1:raise ValueError('only final154 model may lack completed scale update')
            without_update=True;continue
        updated,count,expected=tail154_library.next_restricted_trust(model,
            feedback['trust_after_original_controller'],streak,cfg)
        if feedback!=expected:raise ValueError('restored154 completed scale feedback differs from its frozen source')
        radius,streak=updated,count
    if (stage.get('last_restricted_trust')!=radius
            or stage.get('final_consecutive_growth_qualifying_models')!=streak):
        raise ValueError('restored154 final actual controller differs')
    return {'schema':'recorded-restored154-controller-inherited-by-five-null-height-stage-v1',
        'trust_evaluated':radius,'trust_binary64_exact':str(Q.from_float(radius)),
        'success_streak':streak,'last_model_without_completed_scale_feedback':without_update,
        'origin':'old154 explicit initial scale followed by its completed scale_feedback_update records',
        'unfinished_last_model_not_counted_as_success':without_update,
        'new_stage_inherits_this_B_radius_and_streak_without_reset':True}



def handoff_restored_tail154(prepared,prefix,raw_binding,*,artificial=False):
    """Structural in-memory handoff; no geometry, optimizer, or fake old SHA."""
    require_frozen_prefix_sources()
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prefix.get('schema')!=tail154.SCHEMA
            or prefix.get('status')!='complete-two-grid-entry-tail154-audit'
            or bool(prefix.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed current temporary entry/tail154 result required')
    if (prefix.get('source_files_sha256')!=tail154.implementation_hashes()
            or prefix.get('configuration')!=old_cfg or prefix.get('exact_input_storage')!=bindings
            or prefix.get('input_replay')!=old_replay
            or prefix.get('initial_state')!=state_record(problem,old_initial)
            or prefix.get('old_optimizer_calls_this_run')!=4
            or prefix.get('necessary_growth_prefix_restoration_calls')!=1
            or prefix.get('necessary_strip_prefix_restoration_calls')!=1
            or prefix.get('necessary_SOC_prefix_restoration_calls')!=1
            or prefix.get('necessary_body103_prefix_restoration_calls')!=1
            or prefix.get('new_scientific_solver_calls')!=1
            or prefix.get('unchanged_complete_metric_and_height_reference') is not True):
        raise ValueError('temporary entry/tail154 source/configuration/legacy inputs/initial identity differ')
    if not artificial and (prefix.get('github_sha')!=os.environ.get('GITHUB_SHA')
            or str(prefix.get('github_run_id'))!=os.environ.get('GITHUB_RUN_ID')
            or prefix.get('github_repository')!='Rogerhu12/math-research-public'
            or problem.nunknown!=163):
        raise ValueError('prefix must be the current public job and same163 family')
    stage=prefix[PREFIX_STAGE]
    if stage.get('error') is not None or 'error' in stage.get('status',''):
        raise ValueError('prefix implementation failure is not a qualified restoration')
    snap=stage['checkpoint'];point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('temporary entry/tail154 accepted state missing')
    checked=exact_vector(point.get('exact_binary64_physical_coefficients'),problem.nunknown)
    state=np.asarray(point.get('physical_parameter_coefficients_binary64'),float)
    if state.shape!=checked.shape or not np.array_equal(state,checked):
        raise ValueError('temporary numeric coefficients differ from their exact rational record')
    state=state.copy()  # retain any explicit binary64 signed zeros from the actual prefix
    if (state.tolist()!=point.get('physical_parameter_coefficients_binary64')
            or coefficients(state)!=point.get('exact_binary64_physical_coefficients')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prefix.get('final_state')!=state_record(problem,state)):
        raise ValueError('temporary final exact coefficients or canonical identity differ')
    accepted=snap.get('accepted_iterates',[])
    old_subspace=EntryTail154Subspace(layout_from_problem(problem))
    if state[old_subspace.fixed_columns].tobytes()!=np.asarray(old_initial)[old_subspace.fixed_columns].tobytes():
        raise ValueError('restored154 changed its declared fixed9 height coefficients')
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
    continuation=restored_tail154_controller(stage,old_cfg)
    observed={'run':OBSERVED_TAIL154_RUN,'source':OBSERVED_TAIL154_SOURCE,
        'canonical_physical_state_sha256':OBSERVED_TAIL154_STATE,
        'temporary_complete_report_sha256':OBSERVED_TAIL154_REPORT_SHA,
        'raw_report_not_available_or_used_as_a_new_input':True}
    restoration={'schema':'same-job-temporary-entry/tail154-prefix-restoration-v1',
        'purpose':'restore necessary runtime state under metadata-only output policy, not a new scientific comparison',
        'prefix_scientific_implementation_sha256':tail154.implementation_hashes(),
        'prefix_configuration':copy.deepcopy(old_cfg),'prefix_current_run':prefix.get('github_run_id'),
        'prefix_current_source':prefix.get('github_sha'),
        'prefix_temporary_raw_file':copy.deepcopy(raw_binding),
        'prefix_status':stage.get('status'),'prefix_budget_message':stage.get('budget_message'),
        'controller_continuation':continuation,
        'prefix_source_initial_physical_sha256':digest(problem.identity(old_initial)),
        'prefix_regenerated_final_physical_sha256':point['physical_state_sha256'],
        'observed_reference':observed,
        'regenerated_final_equals_observed_tail154_2ee6':point['physical_state_sha256']==OBSERVED_TAIL154_STATE,
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
    learned={'schema':'temporary-tail154-complete-learned-pool-handoff-v1',
        'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'all_previous_coarse_and_fine_integer_IDs_retained':True,
        'groups2_to10_have_original_actual_values_and_derivatives':True}
    cfg=configuration(old_cfg)
    actual_layout=layout_from_problem(problem)
    old_problem,old_state=problem,state.copy()
    problem=FiveHeightField(old_problem,old_state)
    state=problem.initial_state()
    if problem.identity(state)!=old_problem.identity(old_state):
        raise ArithmeticError('zero new height coordinates changed the original physical state')
    gate=FiveNullHeightGate.from_original(gate,problem,lower,upper)
    lower,upper=gate.coordinate_lower,gate.coordinate_upper
    replay={'schema':'temporary-tail154-to-five-height159-in-memory-handoff-v1',
        'canonical_physical_state_sha256':point['physical_state_sha256'],
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'physical_parameter_count':163,'independent_coordinate_count':159,'learned_pool':learned,
        'exact_coordinate_definition_sha256':problem.coordinate_definition_sha256,
        'restored_original_reference_state':state_record(old_problem,old_state),
        'known_fine_metric_locations':list(locations.values()),'temporary_input_restoration':restoration,
        'controller_continuation':continuation,
        'temporary_input_restorations':copy.deepcopy(old_replay['temporary_input_restorations'])+[restoration],
        'layout_derived_from_actual_problem':actual_layout,
        'explicit_new_constraint_definition':{
            'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
            'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
            'metric_restoration_target_exact':cfg['fixed_metric_budget_exact'],
            'proposal_epsilon_exact':EPSILON_EXACT,'proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
            'strip_proposal_floor_definition':strip_floor_definition(cfg),
            'curvature_proposal_floor_definition':floor_definition(cfg),
            'primary_physical_step_cost_definition':penalty_definition(cfg),
            'new_restricted_proposal_definition':restriction_definition(cfg),
            'new_restricted_scale_definition':growth_definition(cfg),
            'SOC_reversible_scaling':scaling_definition(cfg),
            'all_actual_gates_and163_physical_family_unchanged':True,
            'new159_independent_coordinate_definition':problem.coordinate_definition,
            'new_height_to_body_radius_exact':'4',
            'actual_new_stage_progress_is_measured_from_this_regenerated_initial_state':True,
            'no_initial_match_to_observed_tail154_2ee6_is_assumed':True}}
    return ((problem,state,gate,lower,upper,source_cfg,cfg),bindings,tenth,replay,
        np.asarray(ci,np.int64),np.asarray(fi,np.int64))



def _table(columns,records):
    return {'columns':list(columns),'rows':[[row.get(k) for k in columns] for row in records]}


def compact_decision(d):
    if not d:return None
    return {'actual_gate_booleans':{
        k:(d.get('actual_gate_booleans',{}).get(k) if 'actual_gate_booleans' in d else
           d.get('cap_and_box',{}).get('eligible_under_declared_numerical_gate_tolerances') if k=='cap_and_box_eligible' else d.get(k))
        for k in GATE_ORDER},**{k:d.get(k) for k in GATE_NUMBERS},
        'single_grid_new_target_qualified':d.get('single_grid_new_target_qualified',d.get('new_metric_target_qualified')),
        'direct_max_eta_location':d.get('direct_max_eta_location'),
        'actual_minimum_scaled_PSD_rows':d.get('curvature_scaled_PSD_row_minima'),
        'cap_and_box':copy.deepcopy(d.get('cap_and_box'))}


DECISION_COLUMNS=['actual_gate_codes','direct_max_eta','direct_maximum_absolute_principal_curvature',
    'inner_strip_absolute_margin','maximum_absolute_y','minimum_signed_height','direct_mirror_radius_min_finite',
    'new_metric_target_qualified','eta_peak_t','eta_peak_theta','affine_height_margin','reconstructed_height_margin',
    'box_violation']


def decision_values(d):
    if not d:return None
    c=d.get('cap_and_box',{});loc=d.get('direct_max_eta_location',{})
    return [_gate_codes(d),*[d.get(k) for k in GATE_NUMBERS],
        d.get('single_grid_new_target_qualified',d.get('new_metric_target_qualified')),
        loc.get('t'),loc.get('theta'),c.get('affine_height_margin'),c.get('reconstructed_height_margin'),c.get('box_violation')]


def compact_refinement(record):
    keys=['name','same_canonical_state_and_exact_coefficients','physical_identity_sha256',
        'coordinate_definition_sha256','angular_nodes','position_jet_differences','direct_metric_differences',
        'center_height_difference','center_speed_differences','same_state_objective_costs',
        'no_parameter_step_or_reoptimization_in_this_comparison','finite_evaluation_differences_are_not_error_enclosures']
    result={k:copy.deepcopy(record[k]) for k in keys if k in record}
    for key in ['evaluation_before','evaluation_after']:
        if key in record:result[key+'_sha256']=digest(record[key])
    return result


def small_summary(report,out):
    """A semantic native summary; exact states/full row records stay in the temporary full report."""
    raw=Path(out).read_bytes()
    keep=['schema','status','github_sha','github_run_id','github_repository','artificial_inputs_only',
        'source_files_sha256','configuration','prepare_elapsed_seconds','run_audit_elapsed_seconds',
        'process_total_elapsed_seconds','optimization_active_seconds','peak_rss_kib_linux',
        'old_optimizer_calls_this_run','necessary_growth_prefix_restoration_calls',
        'necessary_strip_prefix_restoration_calls','necessary_SOC_prefix_restoration_calls',
        'necessary_body103_prefix_restoration_calls','necessary_tail154_prefix_restoration_calls',
        'new_scientific_solver_calls','old_failed_metric_auxiliary_delta','final_selection_validation',
        'total_drop_reference','value_evaluation_counts','final_fixed_support_replay',
        'initial_field_diagnostics','final_field_diagnostics','initial_exact_height_diagnostic',
        'final_exact_height_diagnostic','same_parameter_Pi_refinement','limitations','error','phase',
        'pipeline_failure','scientific_status_before_pipeline_failure']
    answer={k:copy.deepcopy(report[k]) for k in keep if k in report}
    if 'same_parameter_Pi_refinement' in answer:
        answer['same_parameter_Pi_refinement']=compact_refinement(answer['same_parameter_Pi_refinement'])
    answer['full_report']={'filename':Path(out).name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
        'temporary_only_not_published_or_saved_as_an_artifact':True}
    answer['input_byte_streams']={k:{name:v.get(name) for name in ['decoded_sha256','decoded_bytes',
        'stored_sha256','stored_bytes','gzip_storage','path']} for k,v in report.get('exact_input_storage',{}).items()
        if isinstance(v,dict)}
    answer['state_identities']={label:{k:report.get(label,{}).get(k) for k in [
        'canonical_physical_state_sha256','independent_coordinate_definition_sha256',
        'complete_metric_sha256','b0_definition_sha256','physical_count','independent_count']}
        for label in ['initial_state','final_state']}
    answer['input_restoration_conclusions']=[{k:r.get(k) for k in [
        'prefix_current_run','prefix_current_source','prefix_status','prefix_budget_message',
        'prefix_regenerated_final_physical_sha256','regenerated_final_equals_observed_f2bb',
        'regenerated_final_equals_observed_strip267','regenerated_final_equals_observed_SOC_ec76',
        'regenerated_final_equals_observed_body103_bfbd','regenerated_final_equals_observed_tail154_2ee6',
        'prefix_accepted_count','prefix_linear_program_count','prefix_shared_full_values',
        'prefix_optimization_active_seconds','prefix_run_audit_elapsed_seconds','prefix_preparation_elapsed_seconds',
        'controller_continuation','prefix_final_gate_values','prefix_temporary_raw_file']}
        for r in report.get('temporary_input_restorations',[])]
    for k in ['initial_current_constraints','initial_doubled_constraints',
            'final_full_grid_constraints','final_doubled_constraints']:
        if k in report:answer[k]=compact_decision(report[k])
    stage=report.get(STAGE)
    if stage is None:return answer
    solver=stage.get('solver',{});snap=stage.get('checkpoint',{})
    result={k:copy.deepcopy(stage[k]) for k in [
        'status','error','budget_message','new_metric_target_reached_on_both_grids',
        'last_restricted_trust','final_consecutive_growth_qualifying_models','entry_tail_height159',
        'initial_fixed_domain_and_height_diagnostic','last_pre_LP_decision'] if k in stage}
    result['solver']={k:v for k,v in solver.items() if k not in ['models']}
    result['checkpoint']={k:snap.get(k) for k in ['total_full_value_physical_evaluations',
        'optimization_elapsed_seconds','original_physical_coefficient_count','independent_coordinate_count']}
    for key in ['active_row_pool_history','fine_physical_row_pool_history']:
        rows=snap.get(key,[])
        result[key+'_final']=None if not rows else {k:rows[-1].get(k) for k in [
            'version','row_count','row_indices_sha256','total_full_grid_rows','flat_index_rule','group_order']}
    models=[];trials=[];corrections=[];updates=[];accepted=[]
    for m in solver.get('models',[]):
        lp=m.get('linear_program',{});p=lp.get('projection',{});cost=lp.get('primary_step_cost_diagnostic',{})
        models.append(dict(number=m['number'],result=m.get('result'),trust=m.get('trust_before_model'),
            LP_status=lp.get('status'),LP_success=lp.get('success'),LP_message=lp.get('message'),
            LP_seconds=lp.get('elapsed_seconds'),LP_variables=lp.get('variables'),
            LP_matrix_bytes=lp.get('matrix_bytes'),row_violation=lp.get('maximum_linear_row_violation'),
            bound_violation=lp.get('maximum_linear_bound_violation'),
            projection=copy.deepcopy(p),physical_step_cost=copy.deepcopy(cost)))
        if 'scale_feedback_update' in m:updates.append({'number':m['number'],**copy.deepcopy(m['scale_feedback_update'])})
        for i,t in enumerate(m.get('trials',[])):
            trials.append({'model':m['number'],'trial':i,**{k:copy.deepcopy(t.get(k)) for k in [
                'kind','alpha_exact','attempt_status','physical_state_sha256','accepted_as_next_iterate',
                'new_coarse_rows','new_fine_rows','coarse_omitted_hard_rows','fine_omitted_hard_rows',
                'coarse_physical_evaluation','fine_value_evaluation','scale_feedback','curvature_step_prediction']},
                'coarse_decision':decision_values(t.get('coarse_decision')),
                'fine_decision':decision_values(t.get('fine_decision'))})
        for j,c in enumerate(m.get('corrections',[])):
            lp=c.get('linear_program',{})
            corrections.append({'model':m['number'],'correction':j,
                'primary_trial_index':c.get('primary_trial_index'),
                'linear_program':{k:copy.deepcopy(lp.get(k)) for k in [
                    'LP_invoked','status','success','message','elapsed_seconds','SOC_solver_returned_finite_primal',
                    'variables','matrix_bytes','body_correction_radius','tail_correction_radius',
                    'height_correction_radius','maximum_linear_row_violation','maximum_linear_bound_violation',
                    'SOC_reversible_scaling','SOC_original_and_scaled_residuals',
                    'SOC_original_unit_dual_diagnostics','initial_metric_slack',
                    'primary_predicted_metric_slack','corrected_predicted_metric_slack',
                    'corrected_actual_trial_linear_metric_slack','proposal_rejected_before_LP',
                    'proposal_rejected_before_geometry']}})
    for a in snap.get('accepted_iterates',[]):
        accepted.append({k:copy.deepcopy(a.get(k)) for k in [
            'accepted_index','physical_state_sha256','coordinate_definition_sha256',
            'maximum_eta_on_both_grids','new_metric_target_qualified_on_both_grids','reason']})
    result['trial_decision_columns']=DECISION_COLUMNS
    result['trial_decision_gate_code_order']=list(GATE_ORDER)
    result['model_table']=_table(['number','result','trust','LP_status','LP_success','LP_message',
        'LP_seconds','LP_variables','LP_matrix_bytes','row_violation','bound_violation','projection','physical_step_cost'],models)
    result['trial_table']=_table(['model','trial','kind','alpha_exact','attempt_status','physical_state_sha256',
        'accepted_as_next_iterate','new_coarse_rows','new_fine_rows','coarse_omitted_hard_rows','fine_omitted_hard_rows',
        'coarse_physical_evaluation','fine_value_evaluation','scale_feedback','curvature_step_prediction',
        'coarse_decision','fine_decision'],trials)
    result['correction_table']=_table(['model','correction','primary_trial_index','linear_program'],corrections)
    result['scale_feedback_updates']=updates
    result['accepted_table']=_table(['accepted_index','physical_state_sha256','coordinate_definition_sha256',
        'maximum_eta_on_both_grids','new_metric_target_qualified_on_both_grids','reason'],accepted)
    result['complete_original_row_floor_and_nonlinear_defect_records']={
        'source':'temporary full report '+STAGE+'.solver.models',
        'stdout':'complete group summaries printed from the same computed records',
        'no_additional_geometry_or_optimizer':True}
    answer[STAGE]=result
    return answer


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


def audit_computed_field(problem,state,data,tau,with_rows=True):
    # Existing audit routines need only unchanged core/tail/shape metadata and
    # the same fixed g. Their numeric inputs are the authoritative NEW jets.
    # The reference-height vector is never used to recompute this geometry.
    reference=problem.coordinates.reference_evaluation_state(state)
    result=audit_data(problem.original_problem,reference,data,tau,with_rows=with_rows)
    result.update(schema='exact-null-height159-already-computed-position-audit-v1',
        canonical_physical_state_sha256=digest(problem.identity(state)),
        independent_coordinate_definition_sha256=problem.coordinate_definition_sha256,
        all_numeric_audit_values_use_actual_null_incremented_jets=True,
        original_context_used_only_for_unchanged_core_tail_shape_and_metric_metadata=True)
    return result


def compare_computed_fields(problem,before,after,state):
    if not np.array_equal(before['radial'],after['radial']):
        raise ValueError('same-state angular refinement requires identical radial points')
    original=problem.original_problem
    values0,values1=point_values(original,before),point_values(original,after)
    return {'name':'same exact159 state and full fixed g/b0; original384/768 evaluation',
        'same_canonical_state_and_exact_coefficients':True,'physical_identity_sha256':digest(problem.identity(state)),
        'coordinate_definition_sha256':problem.coordinate_definition_sha256,
        'evaluation_before':problem.evaluation_definition(),'evaluation_after':problem.evaluation_definition(),
        'angular_nodes':[len(before['theta']),len(after['theta'])],
        'position_jet_differences':{k:float(np.max(np.linalg.norm(before[k]-after[k][:,::2],axis=-1)))
            for k in POSITION_JETS},
        'direct_metric_differences':{k:float(np.max(abs(values0[k]-values1[k][:,::2])))
            for k in ['E_minus_one','F_over_a','metric_operator_error']},
        'center_height_difference':float(after['center'][-1]-before['center'][-1]),
        'center_speed_differences':{k:float(np.max(abs(before['height'][k]-after['height'][k])))
            for k in ['b','b_s','b_ss']},
        'same_state_objective_costs':[objective_cost(original,before),objective_cost(original,after)],
        'no_parameter_step_or_reoptimization_in_this_comparison':True,
        'finite_evaluation_differences_are_not_error_enclosures':True}


def field_diagnostics(data,grid,subspace,cfg):
    # Identical scalar geometry formulas to the old reader, but b is now variable.
    result=tail154.field_diagnostics(data,grid,subspace,cfg)
    result['current_height_diagnostic']=result.pop('fixed_height_diagnostic')
    result['current_height_diagnostic']['not_a_fixed_global_obstruction_in_this_new_stage']=True
    return result


def exact_height_diagnostic(problem,state):
    c=problem.coordinates;heights=c.exact_heights(state);ref=c.reference_exact
    total=sum(c.basis.integrals[j]*(heights[j]-ref[j]) for j in range(9))
    if total!=0:raise ArithmeticError('exact five-height parameterization lost its null integral')
    return {'reference_nine_coefficients_exact':[str(x) for x in ref],
        'current_nine_coefficients_exact':[str(x) for x in heights],
        'five_independent_coordinates_binary64_exact':[str(Q.from_float(float(x))) for x in np.asarray(state)[154:]],
        'exact_total_cap_integral_change':str(total),
        'physical_c4_c5_exactly_unchanged':all(heights[j]==ref[j] for j in [4,5]),
        'coordinate_definition_sha256':problem.coordinate_definition_sha256,
        'current_height_is_not_the_immutable_b0':True,
        'no_rounding_of_nine_dependent_coefficients_is_used_as_the_model':True}


def outside_replay(reference,subspace,grid,data):
    outside=np.array([not(subspace.left<t<subspace.right) for t in grid.nodes])
    ref=reference['grids'][grid.label]
    return {'outside_six_jet_difference_max':{k:float(np.max(abs(np.asarray(data[k])[outside]-ref[k]))) for k in POSITION_JETS},
        'full_frozen_metric_jet_difference_max':{k:float(np.max(abs(np.asarray(data['metric'][k])-ref['metric'][k])))
            for k in ['a','a_s','a_ss']},
        'outside_common_center_difference_max':float(np.max(abs(np.asarray(data['center'])[outside]-ref['center']))),
        'outside_height_jet_difference_max':{k:float(np.max(abs(np.asarray(data['height'][k])[outside]-ref['height'][k])))
            for k in ['b','b_s','b_ss']},
        'same_existing_complete_evaluation_no_extra_call':True,
        'whole_inside_center_and_b_are_allowed_to_change':True,
        'floating_replay_is_not_a_continuous_certificate':True}


def supplementary_outcome_text(report):
    lines=['ENTRY/TAIL + FIVE NULL HEIGHTS:159 INDEPENDENT COORDINATES IN THE SAME163 PHYSICAL FAMILY',
        'B103/T51 retain the actual regenerated154 radius and streak. H physical radius=4B; T=B/8.',
        'All9 original height boxes are coupled exact affine rows. Mathematical total cap integral is exactly zero.',
        'The immutable b0/permanent c0/fixed g remain; current b and center may change inside (9/250,423/500).',
        'Complete original384/768 actual gates remain. The old163 geometry J is still computed before mapping159 columns.',
        'All five necessary prefixes are input restoration, not new scientific progress or forced historical hashes.']
    stage=report.get(STAGE,{})
    init=stage.get('solver',{}).get('inherited154_plus_new_height_controller')
    if init:lines.append('ACTUAL CONTROLLER HANDOFF: '+json.dumps(init,sort_keys=True))
    for phase,key in [('initial','initial_field_diagnostics'),('final','final_field_diagnostics')]:
        for grid,d in report.get(key,{}).items():
            lines.append('DOMAIN METRIC '+phase+' '+grid+': region | n | eta | t exact | theta/pi | e | f')
            for name,value in d['regions'].items():
                loc=value.get('location',{})
                row=[name,value.get('sample_count'),value.get('maximum_actual_eta'),loc.get('t_exact'),
                    loc.get('theta_over_pi_exact'),value.get('E_minus_one'),value.get('F_over_a')]
                lines.append(' | '.join(_scalar(x,digits=17) for x in row))
            lines.append('outside rho '+phase+' '+grid+': '+_scalar(d['rho_out'],digits=17)+
                '; attainer '+json.dumps(d['rho_out_attainer'],sort_keys=True))
            lines.append('CURRENT HEIGHT '+phase+' '+grid+': '+json.dumps(d['current_height_diagnostic'],sort_keys=True))
    for key in ['initial_exact_height_diagnostic','final_exact_height_diagnostic']:
        if key in report:lines.append(key+': '+json.dumps(report[key],sort_keys=True))
    lines.append('INITIAL/FINAL COMPLETE GATES: case | codes in declared order | '+ ' | '.join(GATE_NUMBERS))
    lines.append('gate code order: '+', '.join(GATE_ORDER))
    for key in ['initial_current_constraints','initial_doubled_constraints','final_full_grid_constraints','final_doubled_constraints']:
        if key in report:
            d=report[key]
            lines.append(key+' | '+_gate_codes(d)+' | '+' | '.join(_scalar(d.get(k),digits=17) for k in GATE_NUMBERS))
            lines.append(key+' cap/exact coupled box: '+json.dumps(d.get('cap_and_box',{}),sort_keys=True))
    lines.append('MAPPED MODELS: number | result | trustB | status | success | LP s | rows residual | bounds residual | variables | bytes')
    for m in stage.get('solver',{}).get('models',[]):
        lp=m.get('linear_program',{})
        row=[m['number'],m.get('result'),m.get('trust_before_model'),lp.get('status'),lp.get('success'),
            lp.get('elapsed_seconds'),lp.get('maximum_linear_row_violation'),lp.get('maximum_linear_bound_violation'),
            lp.get('variables'),lp.get('matrix_bytes')]
        lines.append(' | '.join(_scalar(x,digits=17) for x in row))
        if lp.get('message'):lines.append('LP message '+str(m['number'])+': '+lp['message'])
        lines.append('projection '+str(m['number'])+': '+json.dumps(lp.get('projection',{}),sort_keys=True))
        lines.append('B/T/H PHYSICAL UTILIZATION '+str(m['number'])+': '+
            json.dumps(lp.get('primary_step_cost_diagnostic',{}),sort_keys=True))
        lines.append('scale feedback '+str(m['number'])+': '+json.dumps(m.get('scale_feedback_update'),sort_keys=True))
    lines.append('TRIAL PROGRESS: model | i | kind | alpha | accepted | newcoarse | newfine | complete ratio | predicted drop | true drop | reason')
    for m in stage.get('solver',{}).get('models',[]):
        for i,t in enumerate(m.get('trials',[])):
            q=t.get('scale_feedback',{})
            row=[m['number'],i,t.get('kind'),t.get('alpha_exact'),t.get('accepted_as_next_iterate'),
                t.get('new_coarse_rows'),t.get('new_fine_rows'),q.get('actual_to_predicted_ratio'),
                q.get('predicted_metric_improvement'),q.get('actual_two_grid_eta_improvement'),
                q.get('ratio_unavailable_reason',t.get('attempt_status'))]
            lines.append(' | '.join(_scalar(x,digits=17) for x in row))
    lines.append('ACCEPTED EXACT PHYSICAL STATES: index | sha256 | maximum eta on both grids | target qualified')
    for a in stage.get('checkpoint',{}).get('accepted_iterates',[]):
        lines.append(' | '.join(_scalar(a.get(k),digits=17) for k in [
            'accepted_index','physical_state_sha256','maximum_eta_on_both_grids','new_metric_target_qualified_on_both_grids']))
    for key in ['final_fixed_support_replay','total_drop_reference','final_selection_validation',
            'value_evaluation_counts','same_parameter_Pi_refinement']:
        if key in report:
            value=compact_refinement(report[key]) if key=='same_parameter_Pi_refinement' else report[key]
            lines.append(key+': '+json.dumps(value,sort_keys=True))
    lines.append('NEW STAGE COUNTS/CLOCK: '+json.dumps({k:report.get(k) for k in [
        'prepare_elapsed_seconds','run_audit_elapsed_seconds','process_total_elapsed_seconds',
        'optimization_active_seconds','peak_rss_kib_linux']},sort_keys=True))
    alias=copy.copy(report);alias[soc.STAGE]=stage
    lines.append(soc.supplementary_outcome_text(alias).replace(
        'SOC EQUIVALENT SCALING -- original gates and original-unit LP residual limit retained',
        'MAPPED159 SOC/FLOOR/DUAL/DEFECT -- all original geometry gates and original-unit LP residuals retained').rstrip())
    lines.append('No continuous gate, exact isometry or whole-surface reach certificate follows from these finite tests.')
    return '\n'.join(lines)+'\n'


def print_new_stage_outcomes(report):
    print(supplementary_outcome_text(report),end='',flush=True)


def _temporary_binding(path):
    raw=Path(path).read_bytes()
    return {'filename':Path(path).name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
        'temporary_current_job_file_only':True,'not_an_observed_old_report_SHA_replay':True}

def run_pipeline(args,*,artificial=False,evaluate_only=False,process_started=None):
    started=time.monotonic() if process_started is None else process_started
    phase='public-environment-and-original24-input-contract';restorations=[];raw_bindings=[]
    invoked={'growth':0,'strip':0,'SOC':0,'body103':0,'tail154':0,'height159':0}
    try:
        require_frozen_prefix_sources()
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        parent='/dev/shm' if artificial and Path('/dev/shm').is_dir() else os.environ.get('RUNNER_TEMP')
        with tempfile.TemporaryDirectory(prefix='visible-height159-inputs-',dir=parent) as folder:
            growth_out=Path(folder)/'restored-growth.json';strip_out=Path(folder)/'restored-strip.json'
            soc_out=Path(folder)/'restored-scaled-SOC.json';body_out=Path(folder)/'restored-body103.json'
            tail_out=Path(folder)/'restored-tail154.json'
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
            new_prepared=handoff_restored_tail154(prepared_tail,previous,binding,artificial=artificial)
            restorations=list(new_prepared[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'entry-tail154'),end='',flush=True)
            print('Regenerated tail154 equals observed2ee6: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_tail154_2ee6'])+
                '; no retry or forced canonical. This is the actual new-stage initial state.',flush=True)
            del previous,prepared_tail
            phase='one-new-entry-tail-five-null-height159-stage';invoked['height159']=1
            return run_audit(new_prepared,args.out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
    except Exception as error:
        failure={'schema':SCHEMA,'status':'entry-tail-height159-pipeline-failed-last-written-checkpoint-preserved',
            'phase':phase,'source_files_sha256':implementation_hashes(),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
            'necessary_growth_prefix_restoration_calls':invoked['growth'],
            'necessary_strip_prefix_restoration_calls':invoked['strip'],
            'necessary_SOC_prefix_restoration_calls':invoked['SOC'],
            'necessary_body103_prefix_restoration_calls':invoked['body103'],
            'necessary_tail154_prefix_restoration_calls':invoked['tail154'],
            'new_scientific_solver_calls':invoked['height159'],
            'temporary_prefix_raw_bindings':raw_bindings,'temporary_input_restorations':restorations,
            'process_total_elapsed_seconds':time.monotonic()-started,
            'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
        if invoked['height159'] and Path(args.out).exists():
            try:
                existing=json.loads(Path(args.out).read_text())
                existing['scientific_status_before_pipeline_failure']=existing.get('status')
                existing['status']='entry-tail-height159-pipeline-error-last-checkpoint-preserved';existing['pipeline_failure']=failure
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
        raise ValueError('zero height-null coordinates do not match the actual prefix state')
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':5,'necessary_growth_prefix_restoration_calls':1,
        'necessary_strip_prefix_restoration_calls':1,'necessary_SOC_prefix_restoration_calls':1,
        'necessary_body103_prefix_restoration_calls':1,'necessary_tail154_prefix_restoration_calls':1,
        'new_scientific_solver_calls':0,'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':problem.state_record(initial),
        'unchanged_complete_metric_immutable_b0_and_permanent_anchor':True,
        'current_height_is_allowed_to_change_with_exact_zero_total_integral':True,
        'prepare_elapsed_seconds':prepare_seconds,'learned_pool_replay':replay['learned_pool'],
        'temporary_input_restorations':replay['temporary_input_restorations'],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'restricted_proposal_definition':restriction_definition(cfg),
        'independent_coordinate_definition':coord,
        'initial_exact_height_diagnostic':exact_height_diagnostic(problem,initial),
        'process_clock_scope':'main includes five one-time necessary temporary prefixes plus the new159 budget; all clocks separate'}
    def save(status):
        now=time.monotonic();snapshot=report.get(STAGE,{}).get('checkpoint',{})
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=snapshot.get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('original24-inputs-five-prefixes-and-exact-height-map-replayed-before-new-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='entry-tail-height159-complete-initialization'
        def checkpoint(snapshot):
            report[STAGE]={'status':'current159-last-qualified-checkpoint','checkpoint':snapshot,'solver':{}}
            save('five-null-height159-last-accepted-physical-checkpoint')
        objective=EntryTailHeight159Objective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint,
            radial_nodes_exact=grid['radial_nodes_exact'])
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            temporary_restored_tail154_raw_sha256=replay['temporary_input_restoration']['prefix_temporary_raw_file']['sha256'],
            learned_pool_replay=replay['learned_pool'],temporary_input_restoration=replay['temporary_input_restoration'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-temporary-tail154-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-temporary-tail154-eleven-group-fine-original-IDs','source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_computed_field(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        report['initial_field_diagnostics']={g.label:field_diagnostics(d,g,subspace,cfg) for g,d in
            [(objective.row_grids[0],objective.geometry_cache),(objective.row_grids[1],objective.fine_cache['data'])]}
        save('complete-initial-original-gates-exact-height-map-and-current-height-diagnostics')
        report['phase']='one-shared-budget-entry-tail-height159-stage';report['new_scientific_solver_calls']=1
        stage=run_mapped_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
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
            'five_necessary_prefix_counts_are_separate':True,
            'failed_fine_and_actual_fine_SOC_residuals_count':True,
            'old163_J_batches_are_still_computed_before_new159_mapping':True,'no_final_optimizer':True}
        report['limitations']={'all_geometric_gates_sampled_only':True,'new_target026_not_exact_isometry':True,
            'hard_cap58_not_final_reach_target':True,'full_nonlocal_reach_not_paid':True,
            'same_g_b0_and_original163_physical_family_not_expanded':True,
            'exact_null_five_coordinate_subfamily_is_not_all_nine_height_variables':True,
            'five_prefixes_each_once_not_new_scientific_progress':True,'no_forced_observed_prefix_hash':True}
        save('entry-tail-height159-controller-error-last-qualified-preserved' if stage.get('error') else
            'complete-two-grid-entry-tail-height159-audit' if eligible else 'final-recheck-failed-do-not-use-as-new-warm-start')
        print_new_stage_outcomes(report)
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('entry-tail-height159-audit-error-last-checkpoint-preserved');print_new_stage_outcomes(report);return report



def developer_check():
    """New159 interfaces only; all five scientific prefix solvers are stubbed.

    The library separately checks real SingleQ APIs on a newly specified small
    artificial ellipse. This driver fixture checks structural restoration,
    exact-coordinate handoff, complete IO and failure preservation, not geometry.
    """
    import contextlib
    import io
    import sys
    from types import SimpleNamespace
    from unittest.mock import patch
    from frame_entry_tail_blocks import expected_layout
    from frame_entry_tail_height_blocks import artificial_arrays
    from frame_metric_entry_tail_height159 import _MappedArrayObjective
    from frame_height_null_coordinates import developer_check as exact_check
    from frame_five_height_field import developer_check as field_check
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    targeted=mapped_check();arithmetic=exact_check();field=field_check()
    module=sys.modules[__name__]
    layout=expected_layout()
    fixture_sub,_,_,_,physical_lower,physical_upper,_=artificial_arrays()
    class ToyOriginal:
        nunknown=163;metric_free=0;q_index=153
        slices={**{k:slice(*v) for k,v in layout['slices'].items()},'metric':slice(163,163)}
        height_base_definition={'schema':'new159-artificial-IO-immutable-b0-no-surface'}
        height_basis=SimpleNamespace(identity=fixture_sub.coordinates.basis.source_definition,count=9)
        source=SimpleNamespace(space_definition=lambda:{'schema':'artificial-IO-tangent-space'})
        port=SimpleNamespace(side=1);seed=SimpleNamespace(length=.9);tail=SimpleNamespace()
        def identity(self,x):
            return {'schema':'new159-artificial-IO-original163-family',
                'height_basis_definition':copy.deepcopy(self.height_basis.identity),
                'exact_coefficients':{k:coefficients(np.asarray(x)[v]) for k,v in self.slices.items() if k!='metric'},
                'immutable_b0':copy.deepcopy(self.height_base_definition)}
        def metric_model(self,x):
            return {'schema':'new159-artificial-IO-g','mathematical_definition_sha256':digest({'g':'new159-toy'})}
        def evaluation_definition(self):return {'schema':'new159-artificial-no-geometry-IO-evaluation'}
    class ToyOriginalGate:
        nunknown=163;kind='frozen-frame';side=1;length=.9;target=0.
        row=np.zeros(163);family={'schema':'new159-artificial-IO-cap-family'}
        physical_definition={'schema':'new159-artificial-IO-physical-cap'}
        physical_sha256=digest(physical_definition)
        numerical_sha256=digest({'numerical':'new159-artificial-IO-cap'})
        reference_provenance={'artificial_no_geometry':True}
        def assert_context(self,p,s):
            if not isinstance(p,ToyOriginal) or np.shape(s)!=(163,):raise ValueError('toy gate context differs')
        def height(self,s):return 0.
        def reconstructed_height(self,d):return float(d['center'][-1])
    problem=ToyOriginal();old_state=np.zeros(163);old_state[60]=-0.;old_state[154]=.125
    new_state=old_state.copy();new_state[0]=1e-4
    old_gate=ToyOriginalGate()
    nodes=['0','9/250','9/100','117/1000','33/50','153/200','309/400','423/500','9/10']
    radial=np.array([float(Q(x)) for x in nodes]);theta=np.arange(4)*np.pi/2
    grid={'schema':'tiny-artificial159-IO-grid','radial_nodes_exact':nodes,
        'definition_sha256':digest({'r':nodes,'nt':4})}
    cfg=tail154_library.configuration(soc.configuration(recovery_configuration(start_configuration(),
        target='13/50',curvature_cap='58'),artificial=True))
    binding={'filename':'artificial-tail154.json','bytes':1,'sha256':'e'*64}
    bindings={'fixture':{'decoded_sha256':'f'*64,'decoded_bytes':1,'stored_sha256':'f'*64,
        'stored_bytes':1,'gzip_storage':False}}
    decision={k:cfg[k] for k in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
        'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']}
    decision.update(single_grid_admissible_recovery_point=True,direct_max_eta=.2665,
        direct_max_eta_location={'t':.66,'theta':0.},direct_maximum_absolute_principal_curvature=2.,
        hard_strip_pass=True,hard_ball_pass=True,signed_height_pass=True,independent_direct_curvature_pass=True,
        previous_metric_budget_pass=True,maximum_absolute_y=.1,inner_strip_absolute_margin=.28999,
        minimum_signed_height=.05,direct_mirror_radius_min_finite=.1)
    old_continuation={'trust_binary64_exact':str(Q.from_float(float(Q(1,32000)))),
        'trust_evaluated':float(Q(1,32000)),'success_streak':0,'origin':'artificial older prefix',
        'unfinished_last_model_not_counted_as_success':False}
    previous_restoration={
        'regenerated_final_equals_observed_SOC_ec76':False,'regenerated_final_equals_observed_body103_bfbd':False,
        'regenerated_final_equals_observed_f2bb':False,'regenerated_final_equals_observed_strip267':False,
        'prefix_current_run':'artificial','prefix_current_source':'artificial-source',
        'prefix_status':'artificial-completed','prefix_budget_message':None,
        'prefix_source_initial_physical_sha256':'0'*64,
        'prefix_regenerated_final_physical_sha256':digest(problem.identity(old_state)),
        'prefix_accepted_count':1,'prefix_linear_program_count':1,'prefix_shared_full_values':2,
        'prefix_optimization_active_seconds':.01,'prefix_run_audit_elapsed_seconds':.02,
        'prefix_preparation_elapsed_seconds':.01,'prefix_temporary_raw_file':binding,
        'prefix_scientific_implementation_sha256':growth.implementation_hashes(),
        'prefix_configuration':cfg,'controller_continuation':old_continuation}
    replay={'schema':'pure-artificial-current-prepared154','fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'controller_continuation':old_continuation,'temporary_input_restoration':previous_restoration,
        'temporary_input_restorations':[copy.deepcopy(previous_restoration) for _ in range(4)]}
    prepared=((problem,old_state,old_gate,physical_lower,physical_upper,
        {'primitive_order':2,'tau':'61/1000'},cfg),bindings,{'fixture':'grid','selected_raw_auxiliary_delta':.2},
        replay,np.array([0,128]),np.array([0,256]))
    def pool(ids,fine=False):
        nt=2*len(theta) if fine else len(theta)
        record={'version':1,'row_indices':ids,'added_row_indices':ids,'row_count':len(ids),'row_indices_sha256':digest(ids),
            'group_order':list(GROUPS),'total_full_grid_rows':11*len(radial)*nt,
            'flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index' if fine
                else 'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'}
        if fine:record.update(added_row_indices=ids,added_original_grid_coordinates=rows_api.fine_coordinates(
            ids,radial,np.arange(nt)*2*np.pi/nt))
        return record
    point={'exact_binary64_physical_coefficients':coefficients(new_state),
        'physical_parameter_coefficients_binary64':new_state.tolist(),
        'physical_state_sha256':digest(problem.identity(new_state))}
    radius=float(Q(1,4000));smaller=float(Q(1,8000))
    models=[{'number':1,'trust_before_model':radius,
        'trials':[],'scale_feedback_trials':[],'result':'artificial-primary-failed'}]
    _,count,feedback=tail154_library.next_restricted_trust(models[0],smaller,0,cfg)
    models[0]['scale_feedback_update']=feedback
    quality={'full_two_grid_actual_available':True,'ratio_denominator_usable':True,'actual_to_predicted_ratio':.9}
    good={'number':2,'trust_before_model':smaller,'scale_feedback_trials':[],
        'linear_program':{'primary_step_cost_diagnostic':{'actual_trust_normalized_step_norm':1.}},
        'corrections':[],'result':'accepted-two-grid-true-metric-descent',
        'trials':[{'kind':'primary-metric-short-step','alpha_exact':'1','accepted_as_next_iterate':True,
            'new_coarse_rows':0,'new_fine_rows':0,'coarse_decision':decision,'fine_decision':decision,'scale_feedback':quality}]}
    _,count,feedback=tail154_library.next_restricted_trust(good,smaller,count,cfg)
    good['scale_feedback_update']=feedback;models.append(good)
    models.append({'number':3,'trust_before_model':smaller,
        'trials':[{'attempt_status':'coarse-value-call-complete'}]})
    prefix={'schema':tail154.SCHEMA,'status':'complete-two-grid-entry-tail154-audit',
        'artificial_inputs_only':True,'source_files_sha256':tail154.implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,'initial_state':state_record(problem,old_state),
        'old_optimizer_calls_this_run':4,'necessary_growth_prefix_restoration_calls':1,
        'necessary_strip_prefix_restoration_calls':1,'necessary_SOC_prefix_restoration_calls':1,
        'necessary_body103_prefix_restoration_calls':1,'new_scientific_solver_calls':1,
        'unchanged_complete_metric_and_height_reference':True,'final_state':state_record(problem,new_state),
        'github_run_id':'pure-artificial','github_sha':'pure-artificial-no-research',
        'github_repository':'Rogerhu12/math-research-public','full_value_sampling_definition':grid,
        'initial_current_constraints':decision,'initial_doubled_constraints':copy.deepcopy(decision),
        'final_full_grid_constraints':copy.deepcopy(decision),'final_doubled_constraints':copy.deepcopy(decision),
        'final_selection_validation':{'both_value_grids_hard_and_old_metric_pass':True,'both_grid_maximum_eta':.2665},
        PREFIX_STAGE:{'status':'shared-value-time-or-pool-budget-exit','error':None,
            'final_consecutive_growth_qualifying_models':count,'last_restricted_trust':smaller,
            'solver':{'models':models,'linear_program_invocation_count':2,'restored_controller_continuation':old_continuation},
            'checkpoint':{'selected_two_grid_physical_point':point,'accepted_iterates':[point],
                'active_row_pool_history':[pool([0,1,128])],
                'fine_physical_row_pool_history':[pool([0,1,256],True)],
                'saved_fine_trials':[],'total_full_value_physical_evaluations':4}}}
    with patch.object(module,'curvature_grid',return_value=(radial,theta,grid)), \
            patch.object(module,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)):
        before=copy.deepcopy(prefix)
        restored=handoff_restored_tail154(prepared,prefix,binding,artificial=True)
        immutable=prefix==before
        rp,q0,new_gate,lo,hi,_,newcfg=restored[0]
        controller=restored[3]['controller_continuation']
        handoff_ok=bool(rp.identity(q0)==problem.identity(new_state)
            and q0[:154].tobytes()==new_state[:154].tobytes()
            and all(Q(x)==0 for x in q0[154:])
            and rp.coordinates.reference_state.tobytes()==new_state.tobytes()
            and controller['trust_evaluated']==smaller and controller['success_streak']==1
            and controller['unfinished_last_model_not_counted_as_success']
            and len(restored[3]['temporary_input_restorations'])==5
            and not restored[3]['temporary_input_restoration']['regenerated_final_equals_observed_tail154_2ee6'])
        rejects={}
        for name in ['coefficient','fixed-height','gate','pool','controller','source','sampling','implementation-error']:
            bad=copy.deepcopy(prefix)
            if name=='coefficient':bad[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
            elif name=='fixed-height':
                changed=new_state.copy();changed[154]+=.001;newpoint=copy.deepcopy(point)
                newpoint.update(exact_binary64_physical_coefficients=coefficients(changed),
                    physical_parameter_coefficients_binary64=changed.tolist(),physical_state_sha256=digest(problem.identity(changed)))
                bad[PREFIX_STAGE]['checkpoint'].update(selected_two_grid_physical_point=newpoint,accepted_iterates=[newpoint])
                bad['final_state']=state_record(problem,changed)
            elif name=='gate':bad['final_doubled_constraints']['single_grid_admissible_recovery_point']=False
            elif name=='pool':bad[PREFIX_STAGE]['checkpoint']['fine_physical_row_pool_history'][-1]['row_indices']=[0]
            elif name=='controller':bad[PREFIX_STAGE]['final_consecutive_growth_qualifying_models']=0
            elif name=='source':bad['source_files_sha256']['frame_metric_entry_tail154.py']='0'*64
            elif name=='sampling':bad['full_value_sampling_definition']['radial_nodes_exact'][2]='1/10'
            else:bad[PREFIX_STAGE]['error']={'type':'RuntimeError','message':'injected implementation failure'}
            try:handoff_restored_tail154(prepared,bad,binding,artificial=True);rejects[name]=False
            except (ValueError,KeyError):rejects[name]=True

    calls={'prepare':0,'growth':0,'strip':0,'SOC':0,'body103':0,'tail154':0,'new':0};temporary=[]
    shallow={k:copy.deepcopy(prefix[k]) for k in ['initial_current_constraints','initial_doubled_constraints',
        'final_full_grid_constraints','final_doubled_constraints']}
    def prepare_stub(args,**kwargs):calls['prepare']+=1;return ('opaque-original24-preparation',)
    def prefix_stub(label,data):
        def run(p,out,**kwargs):
            calls[label]+=1;temporary.append(Path(out));atomic_save(out,data);return copy.deepcopy(data)
        return run
    def new_stub(p,out,**kwargs):
        calls['new']+=1
        if len(p[3]['temporary_input_restorations'])!=5:raise AssertionError('five prefix records required')
        result={'schema':SCHEMA,'status':'pure-artificial159-new-stage-stub',
            'temporary_input_restorations':p[3]['temporary_input_restorations'],STAGE:{'solver':{},'checkpoint':{}}}
        atomic_save(out,result);return result
    def patch_pipeline(stack,runner):
        stack.enter_context(patch.object(module,'curvature_grid',return_value=(radial,theta,grid)))
        stack.enter_context(patch.object(module,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)))
        stack.enter_context(patch.object(growth,'prepare_run',side_effect=prepare_stub))
        stack.enter_context(patch.object(growth,'run_audit',side_effect=prefix_stub('growth',shallow)))
        stack.enter_context(patch.object(strip,'handoff_restored_growth',return_value=prepared))
        stack.enter_context(patch.object(strip,'run_audit',side_effect=prefix_stub('strip',shallow)))
        stack.enter_context(patch.object(soc,'handoff_restored_strip',return_value=prepared))
        stack.enter_context(patch.object(soc,'run_audit',side_effect=prefix_stub('SOC',shallow)))
        stack.enter_context(patch.object(body103,'handoff_restored_soc',return_value=prepared))
        stack.enter_context(patch.object(body103,'run_audit',side_effect=prefix_stub('body103',shallow)))
        stack.enter_context(patch.object(tail154,'handoff_restored_body103',return_value=prepared))
        stack.enter_context(patch.object(tail154,'run_audit',side_effect=prefix_stub('tail154',prefix)))
        stack.enter_context(patch.object(module,'run_audit',side_effect=runner))
    directory='/dev/shm' if Path('/dev/shm').is_dir() else None
    with tempfile.TemporaryDirectory(prefix='height159-new-IO-',dir=directory) as folder:
        args=SimpleNamespace(out=Path(folder)/'new-audit.json');printed=io.StringIO()
        with contextlib.ExitStack() as stack:
            patch_pipeline(stack,new_stub);stack.enter_context(contextlib.redirect_stdout(printed))
            result=run_pipeline(args,artificial=True,evaluate_only=True)
        once=calls=={'prepare':1,'growth':1,'strip':1,'SOC':1,'body103':1,'tail154':1,'new':1}
        unique=bool([p.name for p in Path(folder).glob('*-audit.json')]==['new-audit.json']
            and all(not p.exists() for p in temporary)
            and [k for k,v in result.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        prefix_print=all(s in printed.getvalue() for s in ['RESTORATION growth','RESTORATION strip-reserve',
            'RESTORATION scaled-SOC','RESTORATION entry-body103','RESTORATION entry-tail154',
            'initial_doubled_constraints','final_doubled_constraints','Regenerated tail154 equals observed2ee6:'])
        args_bad=SimpleNamespace(out=Path(folder)/'failure.json')
        with patch.object(growth,'prepare_run',side_effect=ValueError('new artificial inputloader failure')):
            bad=run_pipeline(args_bad,artificial=True,evaluate_only=True)
        failure_ok=bool(bad['phase']=='strict-original24-input-preparation'
            and bad['necessary_growth_prefix_restoration_calls']==0 and bad['new_scientific_solver_calls']==0
            and json.loads(args_bad.out.read_text())['error']['type']=='ValueError')

    class DriverArrayObjective(_MappedArrayObjective):
        def __init__(self,problem,gate,radial,theta,order,lower,upper,*,cfg,checkpoint,radial_nodes_exact):
            super().__init__(cfg);self.problem=problem;self.gate=gate
            self.subspace=EntryTailHeight159Subspace(layout,problem.coordinates)
            if list(radial_nodes_exact)!=nodes or not np.array_equal(radial,self.radial):raise ValueError('toy grid differs')
            self.lower=np.asarray(lower).copy();self.upper=np.asarray(upper).copy()
            self.physical_lower=gate.original_lower;self.physical_upper=gate.original_upper
            self.checkpoint=checkpoint;self.pool_history=[];self.fine_history=[]
        def set_pool(self,ids,reason):
            self.pool=np.asarray(ids,np.int64).copy();self.pool_history.append(pool(self.pool.tolist()))
        def set_fine_pool(self,ids,reason):
            self.fine_pool=np.asarray(ids,np.int64).copy();self.fine_history.append(pool(self.fine_pool.tolist(),True))
        def snapshot(self):
            r=super().snapshot();r['active_row_pool_history']=copy.deepcopy(self.pool_history)
            r['fine_physical_row_pool_history']=copy.deepcopy(self.fine_history);return r
    class ArrayField(FiveHeightField):
        def geometry(self,state,r,t,order,**kwargs):
            obj=_MappedArrayObjective(newcfg);obj.problem=self
            obj.subspace=EntryTailHeight159Subspace(layout,self.coordinates)
            g=RationalRowGrid('coarse' if len(t)==4 else 'fine',nodes,len(t))
            data,rr,decision=obj._data(state,g);data['IO_mock_decision']=decision;return data
    af=ArrayField(problem,new_state);ax=af.initial_state()
    ag=FiveNullHeightGate.from_original(old_gate,af,physical_lower,physical_upper)
    areplay=copy.deepcopy(restored[3]);areplay['known_fine_metric_locations']=[]
    aprepared=((af,ax,ag,ag.coordinate_lower,ag.coordinate_upper,{'primitive_order':2,'tau':'61/1000'},newcfg),
        bindings,prepared[2],areplay,restored[4],restored[5])
    def compare_arrays(p,a,b,state):
        return {'same_artificial_exact_state':True,'physical_identity_sha256':digest(p.identity(state)),
            'position_jet_differences':{k:float(np.max(abs(a[k]-b[k][:,::2]))) for k in POSITION_JETS}}
    with tempfile.TemporaryDirectory(prefix='height159-new-main-',dir=directory) as folder:
        out=Path(folder)/'new-audit.json';printed=io.StringIO()
        with patch.object(module,'curvature_grid',return_value=(radial,theta,grid)), \
                patch.object(module,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)), \
                patch.object(module,'EntryTailHeight159Objective',DriverArrayObjective), \
                patch.object(module,'audit_computed_field',side_effect=lambda *a,**k:{'artificial_labelled_arrays_no_surface':True}), \
                patch.object(module,'compare_computed_fields',side_effect=compare_arrays), \
                patch.object(module,'recovery_decision',side_effect=lambda p,g,s,d,*a,**k:d['IO_mock_decision']), \
                patch.object(tail154,'geometry_values',side_effect=lambda d:{'eta':d['eta'],'e':d['e'],'f':d['f']}), \
                contextlib.redirect_stdout(printed):
            full=run_audit(aprepared,out,artificial=True,evaluate_only=True)
        native=json.loads(summary_path(out).read_text());raw=out.read_bytes()
        full_ok=bool(full['status']=='complete-two-grid-entry-tail-height159-audit'
            and full[STAGE]['solver']['linear_program_invocation_count']==0
            and full['initial_state']==full['final_state']
            and full['final_selection_validation']['both_value_grids_hard_and_old_metric_pass']
            and full['final_exact_height_diagnostic']['exact_total_cap_integral_change']=='0'
            and full[STAGE]['solver']['inherited154_plus_new_height_controller']['inherited_success_streak']==1
            and native['full_report']['sha256']==hashlib.sha256(raw).hexdigest()
            and [k for k,v in native.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        scientific_print=all(s in printed.getvalue() for s in ['MAPPED MODELS','CURRENT HEIGHT',
            'final_exact_height_diagnostic','final_selection_validation','value_evaluation_counts','ORIGINAL UNIT DUAL'])
        def save_then_fail(p,out,**kwargs):
            save_report(out,full);raise RuntimeError('injected new post-checkpoint exception')
        args=SimpleNamespace(out=Path(folder)/'preserved-audit.json')
        with contextlib.ExitStack() as stack:
            patch_pipeline(stack,save_then_fail);stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            kept=run_pipeline(args,artificial=True,evaluate_only=True)
        keep_ok=bool(kept.get('status')=='entry-tail-height159-pipeline-error-last-checkpoint-preserved'
            and kept.get('final_state')==full.get('final_state') and kept.get(STAGE)==full.get(STAGE)
            and kept.get('pipeline_failure',{}).get('error',{}).get('type')=='RuntimeError')
        # Full CLI parser enters the new development branch only; do not execute
        # this same artificial suite twice merely to cover its dispatch.
        marker={'schema':'new159-explicit-main-branch-fixture','passed':True,'artificial_inputs_only':True}
        devout=Path(folder)/'development.json'
        with patch.object(module,'developer_check',return_value=marker), \
                patch.object(sys,'argv',[__file__,'--check-only','--out',str(devout)]), \
                contextlib.redirect_stdout(io.StringIO()):
            main()
        cli_ok=json.loads(devout.read_text()).get('passed') is True
    try:require_public_actions('true','WrongOwner/OtherRepository',[]);guard=False
    except (ValueError,PermissionError,RuntimeError):guard=True
    checks={
        'new_exact_height_arithmetic':arithmetic['passed'],
        'new_field_twojet_and_parameter_Jacobian':field['passed'],
        'new_mapped_arrays_controller_and_real_small_geometry_API':targeted['passed'],
        'restored154_state_signed_zero_fullpools_and_actual_controller':handoff_ok,
        'prefix_dictionary_not_mutated':immutable,'all_new_bad_handoffs_rejected':all(rejects.values()),
        'exactly_one_each_five_prefixes_and_one_new_stage':once,
        'one_top_level_audit_and_stage_temporary_prefix_cleanup':unique,
        'all_five_prefix_initial_final_gates_and_actual_hash_relation_printed':prefix_print,
        'input_failure_preserves_small_JSON':failure_ok,
        'complete159_run_audit_IO_exactfreeze_and_summary_binding':full_ok,
        'post_checkpoint_failure_preserves_last_complete_state_and_stage':keep_ok,
        'current_height_and_exact_nine_coefficients_science_printed':scientific_print,
        'new_main_check_only_dispatch_does_not_repeat_the_suite':cli_ok,
        'wrong_public_repository_rejected':guard}
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema':SCHEMA+'-new-artificial-interface-check','artificial_inputs_only':True,
        'research_candidate_constructed_evaluated_or_optimized':False,
        'old_development_suites_and_scientific_prefixes_not_repeated':True,
        'exact_height_checks':arithmetic,'field_checks':field,'new_library_checks':targeted,
        'checks':checks,'new_handoff_rejections':rejects,
        'new_pipeline_call_counts_across_success_and_injected_failure_paths':calls,
        'new_pipeline_status':result.get('status'),'new_pipeline_error':result.get('error'),
        'new_post_checkpoint_status':kept.get('status'),'new_post_checkpoint_error':kept.get('error'),
        'new_artificial_audit_status':full.get('status'),'new_artificial_audit_error':full.get('error'),
        'new_artificial_stage_error':full.get(STAGE,{}).get('error'),
        'passed':all(checks.values())}


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
        result.update(source_files_sha256=implementation_hashes(),process_total_elapsed_seconds=time.monotonic()-started)
        atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    report=run_pipeline(args,process_started=started)
    print(json.dumps({'out':str(args.out),'status':report.get('status')}),flush=True)
    if report.get('status')!='complete-two-grid-entry-tail-height159-audit':raise SystemExit(1)


if __name__=='__main__':main()

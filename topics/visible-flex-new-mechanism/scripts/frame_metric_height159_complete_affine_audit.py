#!/usr/bin/env python3
"""One new complete-grid affine-e/f primary after nine necessary restorations.

The same runtime Field, exact H/reference, full163 family, independent159
coordinates, all original IDs and actual successful-SOC controller survive.
Only complete-grid separation of the affine metric model is new here.
Each supporting-cut LP shares the original12 LP/120 second stage budget.
All new artificial and scientific execution is public GitHub Actions only.
"""
from __future__ import annotations
import argparse
import copy
from contextlib import redirect_stdout
from fractions import Fraction as Q
import hashlib
import io
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
from frame_metric_spectral_recovery import PROPOSAL_BRANCHES
from frame_five_height_field import FiveHeightField
from frame_height_null_gate import FiveNullHeightGate
from frame_entry_tail_height_blocks import EntryTailHeight159Subspace
from frame_metric_entry_tail_height159 import (
    restriction_definition,layout_from_problem)
from frame_metric_height159_complete_affine import (
    run_complete_affine_recovery,retention_definition)
from frame_metric_height159_complete_affine import (
    CompleteAffineHeight159Objective,configuration as complete_configuration,
    implementation_hashes as complete_hashes)
from frame_complete_affine_metric_oracle import POLICY, definition as model_definition
from frame_metric_affine_spectral_model import POLICY as SELECTED_POLICY
from frame_selected_row_radial_jacobian import POLICY as FACTORIZATION_POLICY
import frame_complete_affine_metric_development as new_development
import frame_metric_height159_affine_spectral_audit as selected_driver
import frame_metric_height159_factorized_rows_audit as previous_driver
import frame_metric_budget_restoration_rows as rows_api
import frame_metric_height159_capacity_soc_hold_audit as capacity_driver
import frame_height159_fine_capacity as capacity
import frame_metric_height159_soc_hold_audit as frozen
import frame_metric_height159_soc_hold as hold_library

height159=frozen.height159
growth=frozen.growth;strip=frozen.strip;soc=frozen.soc
body103=frozen.body103;tail154=frozen.tail154
INPUTS=frozen.INPUTS;SHA_NAMES=frozen.SHA_NAMES
coefficients=frozen.coefficients
curvature_grid=frozen.curvature_grid
summary_path=frozen.summary_path
audit_computed_field=frozen.audit_computed_field
compare_computed_fields=frozen.compare_computed_fields
field_diagnostics=frozen.field_diagnostics
exact_height_diagnostic=frozen.exact_height_diagnostic
outside_replay=frozen.outside_replay
_temporary_binding=frozen._temporary_binding
_scalar=frozen._scalar
SCHEMA='same159-complete-grid-affine-ef-after-nine-restorations-v1'
STAGE='metric_height159_complete_affine_stage'
COMPLETE='complete-two-grid-height159-complete-affine-audit'
PREFIX_STAGE=selected_driver.STAGE
FROZEN_AND_NEW_DEPENDENCIES={
    "frame_metric_height159_affine_spectral_audit.py": "a62c20944a66a04679a5ae4a156e2e64b4e9331d976125a3f23a1a2356a2df4c",
    "frame_complete_affine_metric_oracle.py": "ab81812f596cf3fc4f1c8d188aec785b289db2fb2c6959e32c2d69250faa91e9",
    "frame_metric_height159_complete_affine.py": "4b64858cec01566e17c2530c8b95c5855d57820454c13dde3cc5aec215217346",
    "frame_complete_affine_metric_development.py": "b40f6724261a8af8e6531b13a2694866e07c92b47651654f3f3549243b5ce2e8"
}


def implementation_hashes():
    result=selected_driver.implementation_hashes()
    result.update(complete_hashes())
    result.update(new_development.implementation_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def require_frozen_prefix_sources():
    selected_driver.require_frozen_prefix_sources()
    actual=implementation_hashes()
    for name,expected in FROZEN_AND_NEW_DEPENDENCIES.items():
        if actual.get(name)!=expected:
            raise ValueError('complete-affine exact source dependency differs: '+name)


def restored_affine_SOC_controller(stage,cfg,expected_source_controller):
    # Frozen scalar replay already covers every original hold reason. No new
    # LP, geometry, controller default, or historical terminal value is used.
    result=previous_driver.restored_successful_SOC_controller(stage,cfg,expected_source_controller)
    result.update(schema='recorded-selected-affine-successful-SOC-controller-for-complete-grid-v1',
        origin='same-job completed affine159 stage and all its recorded successful-SOC updates',
        inherited_complete_scalar_replay_from_frozen_controller_validator=True)
    return result


def handoff_restored_affine_spectral(prepared,prefix,raw_binding,*,artificial=False):
    """Validate and reuse the SAME exact height reference/H; no field is rebuilt."""
    require_frozen_prefix_sources()
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if not isinstance(problem,FiveHeightField) or not isinstance(gate,FiveNullHeightGate):
        raise ValueError('the original159 runtime field and exact null gate must survive restoration')
    if (prefix.get('schema')!=selected_driver.SCHEMA
            or prefix.get('status')!=selected_driver.COMPLETE
            or bool(prefix.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed current temporary affine159 result required')
    count_keys=['growth','strip','SOC','body103','tail154','height159','capacity_SOC_hold','factorized_selected_J']
    if (prefix.get('source_files_sha256')!=selected_driver.implementation_hashes()
            or prefix.get('configuration')!=old_cfg or prefix.get('exact_input_storage')!=bindings
            or prefix.get('input_replay')!=old_replay
            or prefix.get('initial_state')!=problem.state_record(old_initial)
            or prefix.get('old_optimizer_calls_this_run')!=8
            or any(prefix.get('necessary_'+k+'_prefix_restoration_calls')!=1 for k in count_keys)
            or prefix.get('new_scientific_solver_calls')!=1
            or prefix.get('unchanged_complete_metric_immutable_b0_and_permanent_anchor') is not True
            or prefix.get('independent_coordinate_definition')!=problem.coordinate_definition):
        raise ValueError('ninth-prefix source/configuration/inputs/initial or exact reference identity differs')
    if not artificial and (prefix.get('github_sha')!=os.environ.get('GITHUB_SHA')
            or str(prefix.get('github_run_id'))!=os.environ.get('GITHUB_RUN_ID')
            or prefix.get('github_repository')!='Rogerhu12/math-research-public'
            or problem.nunknown!=159 or problem.physical_parameter_count!=163):
        raise ValueError('ninth prefix must be the current public job and same159/163 family')
    if prefix.get('error') is not None or prefix.get('pipeline_failure') is not None:
        raise ValueError('completed affine stage has an implementation/pipeline error')
    if (prefix.get('affine_spectral_policy')!=SELECTED_POLICY
            or old_cfg.get('affine_ef_spectral_primary_policy')!=SELECTED_POLICY
            or 'complete_grid_affine_metric_policy' in old_cfg):
        raise ValueError('ninth prefix must be the original selected affine model before complete-grid separation')
    capacity_records=prefix.get('capacity_input_restoration_reservations',[])
    if (not capacity_records or capacity_records!=old_cfg.get(capacity.HISTORY_KEY)
            or old_cfg.get(capacity.CAP_KEY)!=capacity_records[-1].get('new_fine_capacity')):
        raise ValueError('affine prefix changed the inherited capacity declarations')
    source_reservation=old_replay.get('current_fine_initialization_capacity_reservation',{})
    if {k:v for k,v in source_reservation.items() if k!='executed_configuration_sha256'}!=capacity_records[-1]:
        raise ValueError('affine prefix last input reservation differs from its original declaration')
    stage=prefix[PREFIX_STAGE]
    if stage.get('error') is not None or 'error' in stage.get('status',''):
        raise ValueError('ninth-prefix implementation failure is not a usable restoration')
    snap=stage['checkpoint'];point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('ninth-prefix selected exact159 state missing')
    checked=exact_vector(point.get('exact_binary64_independent_coordinates'),159)
    state=np.asarray(point.get('independent_coordinates_binary64'),float)
    if state.shape!=checked.shape or not np.array_equal(state,checked):
        raise ValueError('ninth-prefix numerical159 coordinates differ from exact rationals')
    state=state.copy()
    if (coefficients(state)!=point.get('exact_binary64_independent_coordinates')
            or [str(q) for q in problem.coordinates.physical_exact(state)]!=point.get('exact_original_physical_coefficients')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or point.get('coordinate_definition_sha256')!=problem.coordinate_definition_sha256
            or prefix.get('final_state')!=problem.state_record(state)
            or snap.get('independent_coordinate_definition')!=problem.coordinate_definition):
        raise ValueError('ninth-prefix canonical physical/rational-coordinate identity differs')
    accepted=snap.get('accepted_iterates',[])
    if not accepted or accepted[-1]!=point:
        raise ValueError('ninth-prefix selected state is not its last accepted state')
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
        raise ValueError('ninth-prefix exact null sum, fixed heights or coupled original box failed')
    validation=prefix.get('final_selection_validation',{})
    if not validation.get('both_value_grids_hard_and_old_metric_pass'):
        raise ValueError('ninth-prefix independent final two-grid gates failed')
    decisions=[prefix.get(k,{}) for k in ['final_full_grid_constraints','final_doubled_constraints']]
    for d in decisions:
        if not d.get('single_grid_admissible_recovery_point'):
            raise ValueError('ninth-prefix complete-grid admissibility missing')
        for key in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
                'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']:
            if d.get(key)!=old_cfg[key]:raise ValueError('ninth-prefix gate definition differs: '+key)
    if validation.get('both_grid_maximum_eta')!=max(d['direct_max_eta'] for d in decisions):
        raise ValueError('ninth-prefix complete-grid maximum differs')
    radial,theta,grid=curvature_grid(tenth)
    if prefix.get('full_value_sampling_definition')!=grid:
        raise ValueError('ninth-prefix full sampling coordinates/structure differ')
    histories=[snap.get(k,[]) for k in ['active_row_pool_history','fine_physical_row_pool_history']]
    if not all(histories):raise ValueError('ninth-prefix full pool histories missing')
    coarse,fine=(h[-1] for h in histories);ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,total,rule,cap,previous in [
        (coarse,ci,11*len(radial)*len(theta),'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows'],old_coarse),
        (fine,fi,22*len(radial)*len(theta),'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'],old_fine)]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=list(GROUPS)
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap or not set(previous).issubset(ids)):
            raise ValueError('ninth-prefix pool IDs/order/layout/cap or inherited rows differ')
    added=fine.get('added_row_indices');fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added) or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=rows_api.fine_coordinates(added,radial,fine_theta)):
        raise ValueError('ninth-prefix fine original row coordinates differ')
    locations={}
    for d in [decisions[-1]]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('ninth-prefix metric peak is nonfinite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    continuation=restored_affine_SOC_controller(stage,old_cfg,old_replay['controller_continuation'])
    restoration={'schema':'same-job-temporary-selected-affine159-restoration-for-complete-grid-v1',
        'purpose':'necessary input restoration under metadata-only policy, not another scientific comparison',
        'prefix_scientific_implementation_sha256':selected_driver.implementation_hashes(),
        'prefix_configuration':copy.deepcopy(old_cfg),'prefix_current_run':prefix.get('github_run_id'),
        'prefix_current_source':prefix.get('github_sha'),'prefix_temporary_raw_file':copy.deepcopy(raw_binding),
        'prefix_status':stage.get('status'),'prefix_budget_message':stage.get('budget_message'),
        'controller_continuation':continuation,'prefix_source_initial_physical_sha256':digest(problem.identity(old_initial)),
        'prefix_regenerated_final_physical_sha256':point['physical_state_sha256'],
        'historical_canonical_hash_is_not_a_handoff_condition':True,
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
    learned={'schema':'temporary-affine159-complete-learned-pool-handoff-v1',
        'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'all_previous_coarse_and_fine_integer_IDs_retained':True,
        'groups2_to10_have_original_actual_values_and_derivatives':True}
    cfg=complete_configuration(old_cfg);replay=copy.deepcopy(old_replay)
    replay.update(schema='temporary-selected-affine159-to-complete-affine-handoff-v1',
        canonical_physical_state_sha256=point['physical_state_sha256'],learned_pool=learned,
        known_fine_metric_locations=list(locations.values()),temporary_input_restoration=restoration,
        controller_continuation=continuation,
        temporary_input_restorations=copy.deepcopy(old_replay['temporary_input_restorations'])+[restoration],
        same_runtime_field_reference_and_coordinate_map_reused=True,
        source_selected_affine_independent_coordinate_definition_sha256=problem.coordinate_definition_sha256)
    replay['explicit_new_constraint_definition'].update(
        successful_SOC_radius_retention=retention_definition(cfg),
        original_actual_gate_definitions_unchanged=True,
        complete_original_grid_affine_metric_model=model_definition(),
        original_hard_box_norm_rows_and_SOC_correction_RHS_unchanged=True,
        prior159_independent_coordinate_map_and_reference_unchanged=True,
        new_height_to_body_radius_exact_is_inherited_not_new_here='4',
        no_historical_canonical_state_is_assumed_or_forced=True,
        selected_row_radial_factorization_policy=FACTORIZATION_POLICY,
        current_reference_H_g_b0_physical_family_and_all_acceptance_gates_preserved=True,
        full_successful_SOC_controller_and_capacities_inherited_without_reset=True,
        selected_affine_policy_retained_as_frozen_input=SELECTED_POLICY,
        predicted_attainer_rows_do_not_mutate_actual_learning_pools=True,
        new_complete_grid_oracle_is_charged_to_original_active_clock=True,
        same_original_shared12LP_40value_120second_caps=True)
    return ((problem,state,gate,lower,upper,source_cfg,cfg),bindings,tenth,replay,
        np.asarray(ci,np.int64),np.asarray(fi,np.int64))



def _selected_format_view(report):
    """Formatting adapter only; the frozen selected driver never executes here."""
    view=dict(report)
    if STAGE in view:view[selected_driver.STAGE]=view.pop(STAGE)
    return view


def small_summary(report,out):
    if not isinstance(report.get('configuration'),dict):
        keys=['schema','status','phase','source_files_sha256','github_sha','github_run_id',
            'github_repository','artificial_inputs_only','old_optimizer_calls_this_run',
            'new_scientific_solver_calls','new_stage_call_counter_semantics',
            'temporary_prefix_raw_bindings','temporary_input_restorations',
            'last_temporary_prefix_diagnostic','capacity_input_restoration_reservations',
            'capacity_input_restoration_diagnostics','process_total_elapsed_seconds','error']
        keys += [k for k in report if k.startswith('necessary_') and k.endswith('_calls')]
        return {k:copy.deepcopy(report[k]) for k in keys if k in report}
    summary=selected_driver.small_summary(_selected_format_view(report),out)
    if selected_driver.STAGE in summary:summary[STAGE]=summary.pop(selected_driver.STAGE)
    for key in ['complete_affine_policy','complete_affine_model_definition','algorithm_stage_scope',
            'ninth_handoff_summary','new_stage_call_counter_semantics',
            'necessary_selected_affine_prefix_restoration_calls',
            'complete_original_grid_oracle_progress','error','pipeline_failure']:
        if key in report:summary[key]=copy.deepcopy(report[key])
    stage=report.get(STAGE,{})
    if STAGE in summary:
        summary[STAGE]['inherited_selected_affine_model_definition']=summary[STAGE].pop(
            'affine_spectral_model_definition',None)
        summary[STAGE]['complete_affine_model_definition']=model_definition()
        summary[STAGE]['complete_original_grid_oracle_progress']=copy.deepcopy(
            stage.get('complete_original_grid_oracle_progress',
                stage.get('checkpoint',{}).get('complete_original_grid_oracle_progress',[])))
        for output,source in zip(
                summary[STAGE].get('complete_new_affine_model_and_error_records',[]),
                stage.get('solver',{}).get('models',[])):
            output['complete_original_grid_model']=copy.deepcopy(
                source.get('linear_program',{}).get('complete_original_grid_model'))
            output['physical_values_or_Jacobians_inside_inner_solver']=copy.deepcopy(
                source.get('linear_program',{}).get('physical_values_or_Jacobians_inside_inner_solver'))
            output['full_and_selected_rho0_are_distinct_bound_metadata']=True
    return summary


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),
        allow_nan=False)+'\n')
    os.replace(tmp,path)


def print_new_stage_outcomes(report):
    # The two adapters map only stage keys for the complete old numeric printer.
    view=previous_driver._frozen_format_view(
        selected_driver._frozen_format_view(_selected_format_view(report)))
    text=frozen.supplementary_outcome_text(view)
    text=text.replace(
        'CONDITIONAL SUCCESSFUL-SOC RADIUS RETENTION: SAME159 COORDINATES AND SAME163 PHYSICAL FAMILY',
        'COMPLETE TWO-GRID AFFINE E/F SEPARATION: SAME159/SAME163 AND ORIGINAL ACTUAL GATES')
    text=text.replace(
        'All six necessary prefixes are input restoration, not new scientific progress or forced historical hashes.',
        'All nine prior invocations are one-time input restoration; only complete affine-grid separation is new here.')
    print(text,end='',flush=True)
    stage=report.get(STAGE,{})
    for model in stage.get('solver',{}).get('models',[]):
        payload={k:copy.deepcopy(model.get(k)) for k in [
            'number','trust_before_model','linear_program','SOC_hold_model_binding',
            'primary_step_cost_diagnostic','trials','corrections',
            'accepted_SOC_base_total_step_diagnostic','scale_feedback_update','error',
            'affine_spectral_observable_model'] if k in model}
        print('COMPLETE AFFINE OUTER MODEL '+json.dumps(payload,ensure_ascii=False,
            sort_keys=True,separators=(',',':'),allow_nan=False),flush=True)
    extra={k:copy.deepcopy(report.get(k)) for k in [
        'schema','status','phase','complete_affine_policy','complete_affine_model_definition',
        'factorized_selected_J_execution','complete_original_grid_oracle_progress',
        'algorithm_stage_scope','ninth_handoff_summary','value_evaluation_counts',
        'new_stage_call_counter_semantics','error','pipeline_failure']}
    print('COMPLETE AFFINE ACTUAL '+json.dumps(extra,ensure_ascii=False,sort_keys=True,
        separators=(',',':'),allow_nan=False),flush=True)


def print_existing_prefix(label,report,receipt):
    print(soc.prefix_outcome_text(report,receipt,label),end='',flush=True)


def affine_input_diagnostic(report,binding):
    stage=report.get(PREFIX_STAGE,{})
    snap=stage.get('checkpoint',{})
    point=snap.get('selected_two_grid_physical_point') or {}
    return {'schema':'selected-affine159-current-input-diagnostic-for-complete-grid-v1',
        'raw_binding':copy.deepcopy(binding),'status':report.get('status'),'phase':report.get('phase'),
        'error':copy.deepcopy(report.get('error')),'stage_error':copy.deepcopy(stage.get('error')),
        'stage_status':stage.get('status'),'stage_budget_message':stage.get('budget_message'),
        'selected_physical_state_sha256':point.get('physical_state_sha256'),
        'last_restricted_trust':stage.get('last_restricted_trust'),
        'success_streak':stage.get('final_consecutive_growth_qualifying_models'),
        'solver_call_counts':{k:stage.get('solver',{}).get(k) for k in [
            'linear_program_invocation_count','primary_LP_invocation_count','correction_LP_invocation_count']},
        'no_missing_point_or_original_error_inferred':True}


def run_pipeline(args,*,artificial=False,evaluate_only=False,process_started=None):
    started=time.monotonic() if process_started is None else process_started
    phase='public-environment-and-original24-input-contract';restorations=[];raw_bindings=[]
    last_prefix_diagnostic=None;reservations=[];capacity_diagnostics=[]
    invoked={'growth':0,'strip':0,'SOC':0,'body103':0,'tail154':0,'height159':0,'hold':0,'factorized':0,'affine':0,'complete':0}
    try:
        require_frozen_prefix_sources()
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        parent='/dev/shm' if artificial and Path('/dev/shm').is_dir() else os.environ.get('RUNNER_TEMP')
        with tempfile.TemporaryDirectory(prefix='visible-complete-affine-nine-inputs-',dir=parent) as folder:
            growth_out=Path(folder)/'restored-growth.json';strip_out=Path(folder)/'restored-strip.json'
            soc_out=Path(folder)/'restored-scaled-SOC.json';body_out=Path(folder)/'restored-body103.json'
            tail_out=Path(folder)/'restored-tail154.json';height_out=Path(folder)/'restored-height159.json'
            hold_out=Path(folder)/'restored-capacity-SOC-hold.json'
            factorized_out=Path(folder)/'restored-factorized-selected-J.json'
            affine_out=Path(folder)/'restored-selected-affine-spectral.json'
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
            phase='declare-once-capacity159-input-production-reserve'
            prepared_height,reservation=capacity_driver.reserve_prepared_stage(prepared_height,capacity_driver.CAPACITY_INPUT_STAGE)
            reservations.append(reservation);capacity_driver.print_capacity('INPUT PRODUCTION DECLARED',reservation)
            phase='one-necessary-exact-capacity159-producer-restoration';invoked['height159']=1
            captured=io.StringIO()
            try:
                with redirect_stdout(captured):
                    previous=height159.run_audit(prepared_height,height_out,artificial=artificial,evaluate_only=evaluate_only,
                        process_started=started,prepare_seconds=time.monotonic()-started)
            finally:
                if captured.getvalue():print(capacity_driver._output_scope(captured.getvalue()),end='',flush=True)
            binding=_temporary_binding(height_out);raw_bindings.append(binding)
            phase='height159-qualified-state-full-pools-reference-and-controller-handoff'
            last_prefix_diagnostic=frozen.prefix_handoff_diagnostic(previous,binding)
            print('CAPACITY159 PRE-HANDOFF DIAGNOSTIC: '+json.dumps(last_prefix_diagnostic,
                ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)
            capacity_result=capacity.initialization_diagnostic(previous.get(height159.STAGE),
                prepared_height[0][-1],reservation)
            capacity_diagnostics.append(capacity_result);capacity_driver.print_capacity('INPUT PRODUCTION INITIALIZER ACTUAL',capacity_result)
            new_prepared=frozen.handoff_restored_height159(prepared_height,previous,binding,artificial=artificial)
            if capacity_result.get('contract_pass') is False:
                raise ValueError('recorded capacity159 initialization violates its declared structural allowance')
            new_prepared=capacity_driver.annotate_validated_input_handoff(new_prepared,reservation,capacity_result)
            restorations=list(new_prepared[3]['temporary_input_restorations'])
            print(capacity_driver.input_production_outcome_text(previous,restorations[-1]),end='',flush=True)
            print('Regenerated height159 equals observed b429: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_height159_b429'])+
                '; historical comparison only: this is the sixth necessary restoration with the original declared capacity. No retry or forced canonical; the seventh input restoration follows.',flush=True)
            del previous,prepared_height
            phase='declare-once-hold-initialization-reserve'
            new_prepared,reservation=capacity_driver.reserve_prepared_stage(new_prepared,capacity_driver.CAPACITY_HOLD_STAGE)
            reservations.append(reservation);capacity_driver.print_capacity('HOLD DECLARED',reservation)
            phase='one-necessary-exact-capacity-SOC-hold-restoration';invoked['hold']=1
            # Keep this exact prepared tuple alive.  Its runtime Field/H is
            # the source of the final handoff; JSON alone never rebuilds it.
            previous=capacity_driver.run_audit(new_prepared,hold_out,artificial=artificial,
                evaluate_only=evaluate_only,process_started=started,
                prepare_seconds=time.monotonic()-started,
                capacity_reservations=reservations,capacity_diagnostics=capacity_diagnostics)
            binding=_temporary_binding(hold_out);raw_bindings.append(binding)
            phase='capacity-SOC-hold-complete-state-pools-and-controller-handoff'
            last_prefix_diagnostic=previous_driver.capacity_hold_diagnostic(previous,binding)
            print('SEVENTH PREFIX HANDOFF DIAGNOSTIC '+json.dumps(last_prefix_diagnostic,
                ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)
            prepared_factorized=previous_driver.handoff_restored_capacity_hold(
                new_prepared,previous,binding,artificial=artificial)
            restorations=list(prepared_factorized[3]['temporary_input_restorations'])
            print_existing_prefix('capacity-SOC-hold-complete-parameters',previous,restorations[-1])
            del previous,new_prepared
            phase='one-necessary-frozen-factorized-selected-J-restoration';invoked['factorized']=1
            captured=io.StringIO()
            try:
                with redirect_stdout(captured):
                    previous=previous_driver.run_audit(prepared_factorized,factorized_out,
                        artificial=artificial,evaluate_only=evaluate_only,process_started=started,
                        prepare_seconds=time.monotonic()-started)
            finally:
                if captured.getvalue():
                    print('EIGHTH INPUT RESTORATION ONLY -- following frozen selected-J outcomes are not new complete-grid separation results.',flush=True)
                    print(captured.getvalue(),end='',flush=True)
            binding=_temporary_binding(factorized_out);raw_bindings.append(binding)
            phase='factorized159-complete-state-pools-controller-and-model-handoff'
            last_prefix_diagnostic=selected_driver.factorized_input_diagnostic(previous,binding)
            print('EIGHTH PREFIX HANDOFF DIAGNOSTIC '+json.dumps(last_prefix_diagnostic,
                ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)
            prepared_affine=selected_driver.handoff_restored_factorized_rows(
                prepared_factorized,previous,binding,artificial=artificial)
            restorations=list(prepared_affine[3]['temporary_input_restorations'])
            print_existing_prefix('factorized-selected-J-input-restoration',previous,restorations[-1])
            del previous,prepared_factorized
            phase='one-necessary-frozen-selected-affine-restoration';invoked['affine']=1
            captured=io.StringIO()
            try:
                with redirect_stdout(captured):
                    previous=selected_driver.run_audit(prepared_affine,affine_out,
                        artificial=artificial,evaluate_only=evaluate_only,process_started=started,
                        prepare_seconds=time.monotonic()-started)
            finally:
                if captured.getvalue():
                    print('NINTH INPUT RESTORATION ONLY -- the following selected affine outcomes are not new complete-grid separation results.',flush=True)
                    print(captured.getvalue(),end='',flush=True)
            binding=_temporary_binding(affine_out);raw_bindings.append(binding)
            phase='selected-affine159-complete-state-pools-controller-and-full-grid-model-handoff'
            last_prefix_diagnostic=affine_input_diagnostic(previous,binding)
            print('NINTH PREFIX HANDOFF DIAGNOSTIC '+json.dumps(last_prefix_diagnostic,
                ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)
            final_prepared=handoff_restored_affine_spectral(
                prepared_affine,previous,binding,artificial=artificial)
            restorations=list(final_prepared[3]['temporary_input_restorations'])
            print_existing_prefix('selected-affine-input-restoration',previous,restorations[-1])
            print('All nine prior invocations are necessary input restoration. The new stage keeps '
                'the same runtime Field/H, full original pools, actual terminal controller and original '
                'LP/value/time caps. Only complete-grid affine separation starts next.',flush=True)
            del previous,prepared_affine
            phase='one-new-complete-grid-affine-primary-stage';invoked['complete']=1
            return run_audit(final_prepared,args.out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
    except Exception as error:
        failure={'schema':SCHEMA,'status':'complete-affine-pipeline-failed-last-written-checkpoint-preserved',
            'phase':phase,'source_files_sha256':implementation_hashes(),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
            'necessary_growth_prefix_restoration_calls':invoked['growth'],
            'necessary_strip_prefix_restoration_calls':invoked['strip'],
            'necessary_SOC_prefix_restoration_calls':invoked['SOC'],
            'necessary_body103_prefix_restoration_calls':invoked['body103'],
            'necessary_tail154_prefix_restoration_calls':invoked['tail154'],
            'necessary_height159_prefix_restoration_calls':invoked['height159'],
            'necessary_capacity_SOC_hold_prefix_restoration_calls':invoked['hold'],
            'necessary_factorized_selected_J_prefix_restoration_calls':invoked['factorized'],
            'necessary_selected_affine_prefix_restoration_calls':invoked['affine'],
            'old_optimizer_calls_this_run':sum(invoked[k] for k in invoked if k!='complete'),
            'new_scientific_solver_calls':invoked['complete'],
            'new_stage_call_counter_semantics':'only complete-grid affine separation is new; nine prior stage invocations are restoration',
            'capacity_input_restoration_reservations':copy.deepcopy(reservations),
            'capacity_input_restoration_diagnostics':copy.deepcopy(capacity_diagnostics),
            'temporary_prefix_raw_bindings':raw_bindings,'temporary_input_restorations':restorations,
            'last_temporary_prefix_diagnostic':copy.deepcopy(last_prefix_diagnostic),
            'process_total_elapsed_seconds':time.monotonic()-started,
            'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
        if invoked['complete'] and Path(args.out).exists():
            try:
                existing=json.loads(Path(args.out).read_text())
                if existing.get('schema')==SCHEMA:
                    existing['scientific_status_before_pipeline_failure']=existing.get('status')
                    existing['status']='complete-affine-pipeline-error-last-checkpoint-preserved'
                    existing['pipeline_failure']=failure
                    save_report(args.out,existing)
                    print('COMPLETE AFFINE PIPELINE FAILURE '+json.dumps(failure['error'],allow_nan=False),flush=True)
                    return existing
            except (OSError,ValueError,TypeError,KeyError):
                pass
        save_report(args.out,failure)
        print('COMPLETE AFFINE PIPELINE FAILURE '+json.dumps(failure['error'],
            ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)
        if last_prefix_diagnostic is not None:
            print('LAST PREFIX DIAGNOSTIC '+json.dumps(last_prefix_diagnostic,
                ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)
        return failure


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
        raise ValueError('same actual159 coordinates do not match the ninth-prefix state')
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':9,'necessary_growth_prefix_restoration_calls':1,
        'necessary_strip_prefix_restoration_calls':1,'necessary_SOC_prefix_restoration_calls':1,
        'necessary_body103_prefix_restoration_calls':1,'necessary_tail154_prefix_restoration_calls':1,
        'necessary_height159_prefix_restoration_calls':1,
        'necessary_capacity_SOC_hold_prefix_restoration_calls':1,
        'necessary_factorized_selected_J_prefix_restoration_calls':1,
        'necessary_selected_affine_prefix_restoration_calls':1,
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
        'process_clock_scope':'nine one-time necessary restorations, then one same-budget complete-grid affine stage; clocks separate'}
    report.update(
        factorization_policy=FACTORIZATION_POLICY,
        complete_affine_policy=POLICY,
        complete_affine_model_definition=model_definition(),
        algorithm_stage_scope={
            'nine_prior_scientific_stage_implementations_and_complete_parameters_reused_once':True,
            'capacity159_producer_and_hold_are_now_input_restoration_not_new_comparisons':True,
            'only_complete_original_grid_separation_of_the_affine_primary_changes':True,
            'full_grid_JVP_is_analytic_one_direction_with_original_complete_theta_Pi':True,
            'new_attainer_derivatives_use_inherited_selected_radial_contraction':True,
            'all_existing_selected_soft_functions_remain_in_each_primary':True,
            'no_predicted_learning_rows_or_new_pool_capacity':True,
            'new_JVP_and_row_J_seconds_count_in_original_active_time':True,
            'all_inner_supporting_cut_LPs_charge_the_original_shared_ledger':True,
            'original_hard_box_norm_and_SOC_correction_rhs_unchanged':True,
            'same159_coordinates_same163_family_same_g_b0_reference_and_H':True,
            'all_original_pool_IDs_and_actual_successful_SOC_terminal_controller_inherited':True,
            'no_new_capacity_reservation_or_LP_value_active_time_extension':True,
            'all_ordinary_values_actual_gates_and_final_two_grids_unchanged':True,
            'floating_reassociation_can_change_rows_LP_choices_and_trajectory':True},
        new_stage_call_counter_semantics='nine necessary prior driver invocations; one complete-grid affine driver, never inner LP counts',
        ninth_handoff_summary=copy.deepcopy(replay['temporary_input_restoration']),
        capacity_input_restoration_reservations=copy.deepcopy(cfg.get(capacity.HISTORY_KEY,[])))
    def save(status):
        now=time.monotonic();snapshot=report.get(STAGE,{}).get('checkpoint',{})
        report['factorized_selected_J_execution']=copy.deepcopy(
            snapshot.get('selected_row_factorization_statistics'))
        report['complete_original_grid_oracle_progress']=copy.deepcopy(
            report.get(STAGE,{}).get('complete_original_grid_oracle_progress',
                snapshot.get('complete_original_grid_oracle_progress',[])))
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=snapshot.get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('original24-inputs-nine-prefixes-and-exact-height-reference-replayed-before-new-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='height159-complete-affine-complete-initialization'
        def checkpoint(snapshot):
            report[STAGE]={'status':'current159-last-qualified-checkpoint','checkpoint':snapshot,'solver':{}}
            save('complete-affine-last-accepted-physical-checkpoint')
        objective=CompleteAffineHeight159Objective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint,
            radial_nodes_exact=grid['radial_nodes_exact'])
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            temporary_restored_selected_affine159_raw_sha256=replay['temporary_input_restoration']['prefix_temporary_raw_file']['sha256'],
            learned_pool_replay=replay['learned_pool'],temporary_input_restoration=replay['temporary_input_restoration'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-temporary-selected-affine159-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-temporary-selected-affine159-eleven-group-fine-original-IDs','source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_computed_field(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        report['initial_field_diagnostics']={g.label:field_diagnostics(d,g,subspace,cfg) for g,d in
            [(objective.row_grids[0],objective.geometry_cache),(objective.row_grids[1],objective.fine_cache['data'])]}
        save('complete-initial-original-gates-exact-height-map-and-current-height-diagnostics')
        report['phase']='one-shared-budget-height159-complete-affine-stage';report['new_scientific_solver_calls']=1
        # The original selected-affine recovery loop is called unchanged through
        # the explicit subclass. Only complete-grid separation/prediction is new.
        stage=run_complete_affine_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
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
            'nine_necessary_prefix_counts_are_separate':True,
            'failed_fine_and_actual_fine_SOC_residuals_count':True,
            'original_full163_geometry_J_batches_in_new_selected_paths':0,
            'selected_scalar_J_contracted_before_radial_expansion':True,
            'new_directional_scans_are_not_ordinary_geometry_values':True,
            'new_directional_and_added_metric_row_J_costs_reported_separately':True,
            'no_final_optimizer':True}
        report['limitations']={'all_geometric_gates_sampled_only':True,'new_target026_not_exact_isometry':True,
            'hard_cap58_not_final_reach_target':True,'full_nonlocal_reach_not_paid':True,
            'same_g_b0_and_original163_physical_family_not_expanded':True,
            'exact_null_five_coordinate_subfamily_is_not_all_nine_height_variables':True,
            'nine_prior_declared_stages_are_input_restoration_for_this_experiment':True,'no_forced_observed_prefix_hash':True}
        save('height159-complete-affine-controller-error-last-qualified-preserved' if stage.get('error') else
            COMPLETE if eligible else 'final-recheck-failed-do-not-use-as-new-warm-start')
        print_new_stage_outcomes(report)
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('height159-complete-affine-audit-error-last-checkpoint-preserved');print_new_stage_outcomes(report);return report



def _new_ninth_handoff_fixture():
    """Extend frozen labelled metadata, without running any old developer suite."""
    from unittest.mock import patch
    fixture=selected_driver._new_eighth_handoff_fixture()
    with patch.object(selected_driver,'curvature_grid',return_value=(
            fixture['radial'],fixture['theta'],fixture['grid'])):
        prepared=selected_driver.handoff_restored_factorized_rows(
            fixture['prepared_factorized'],fixture['factorized_report'],
            fixture['binding'],artificial=True)
    field,initial,gate,lo,hi,source_cfg,cfg=prepared[0]
    prefix=copy.deepcopy(fixture['factorized_report'])
    stage=prefix.pop(previous_driver.STAGE)
    controller=copy.deepcopy(prepared[3]['controller_continuation'])
    radius=controller['trust_evaluated'];streak=controller['success_streak']
    stage['solver']['models']=[]
    stage['solver']['inherited159_controller_without_reset']={
        'restored_height159_controller_inherited':controller,
        'inherited_body_radius_exact_binary64':str(Q.from_float(radius)),
        'inherited_tail_radius_exact_binary64':str(Q.from_float(radius)/8),
        'inherited_height_radius_exact_binary64':str(4*Q.from_float(radius)),
        'inherited_success_streak':streak}
    stage['last_restricted_trust']=radius
    stage['final_consecutive_growth_qualifying_models']=streak
    prefix.update(schema=selected_driver.SCHEMA,status=selected_driver.COMPLETE,
        source_files_sha256=selected_driver.implementation_hashes(),
        configuration=cfg,input_replay=prepared[3],
        initial_state=field.state_record(initial),final_state=field.state_record(initial),
        old_optimizer_calls_this_run=8,new_scientific_solver_calls=1,
        necessary_factorized_selected_J_prefix_restoration_calls=1,
        affine_spectral_policy=SELECTED_POLICY,
        capacity_input_restoration_reservations=copy.deepcopy(cfg[capacity.HISTORY_KEY]))
    prefix[PREFIX_STAGE]=stage
    return dict(fixture,prepared_affine=prepared,affine_report=prefix)


def _handoff_development():
    import sys
    from unittest.mock import patch
    module=sys.modules[__name__]
    fixture=_new_ninth_handoff_fixture()
    prepared=fixture['prepared_affine'];prefix=fixture['affine_report']
    raw={'filename':'new-labelled-selected-affine-input.json','bytes':1,'sha256':'e'*64}
    with patch.object(module,'curvature_grid',return_value=(
            fixture['radial'],fixture['theta'],fixture['grid'])):
        result=handoff_restored_affine_spectral(prepared,prefix,raw,artificial=True)
        field=prepared[0][0];old_cfg=prepared[0][-1];cfg=result[0][-1]
        checks={
            'same_runtime_field_gate_reference_H_and_exact159_state':bool(
                result[0][0] is field and result[0][2] is prepared[0][2]
                and result[0][0].coordinates is field.coordinates
                and result[0][1].tobytes()==prepared[0][1].tobytes()),
            'only_complete_model_policy_and_ninth_history_added':bool(
                cfg==complete_configuration(old_cfg)
                and len(result[3]['temporary_input_restorations'])==9
                and cfg['affine_ef_spectral_primary_policy']==SELECTED_POLICY
                and all(cfg[k]==old_cfg[k] for k in ['max_linear_models','max_physical_evaluations',
                    'max_seconds',capacity.CAP_KEY,capacity.HISTORY_KEY])
                and np.array_equal(result[4],prepared[4]) and np.array_equal(result[5],prepared[5])),
            'actual_selected_affine_terminal_controller_inherited':bool(
                result[3]['controller_continuation']['trust_evaluated']==prefix[PREFIX_STAGE]['last_restricted_trust']
                and result[3]['controller_continuation']['success_streak']==
                    prefix[PREFIX_STAGE]['final_consecutive_growth_qualifying_models'])}
        mutations={}
        bad=copy.deepcopy(prefix);bad['source_files_sha256']={}
        mutations['wrong_ninth_source_rejected']=bad
        bad=copy.deepcopy(prefix);bad['configuration']['max_linear_models']+=1
        mutations['different_prefix_budget_rejected']=bad
        bad=copy.deepcopy(prefix);bad[PREFIX_STAGE]['last_restricted_trust']/=2
        mutations['different_actual_terminal_controller_rejected']=bad
        bad=copy.deepcopy(prefix)
        bad[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']['exact_original_physical_coefficients'][0]='1'
        mutations['different_exact_physical163_state_rejected']=bad
        bad=copy.deepcopy(prefix);pool=bad[PREFIX_STAGE]['checkpoint']['active_row_pool_history'][-1]
        pool['row_indices']=[0,2,128];pool['row_count']=3;pool['row_indices_sha256']=digest(pool['row_indices'])
        mutations['removed_inherited_original_row_rejected']=bad
        bad=copy.deepcopy(prefix);bad[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']=None
        mutations['missing_selected_point_rejected']=bad
        bad=copy.deepcopy(prefix);bad['affine_spectral_policy']='wrong-selected-input-policy'
        mutations['different_selected_affine_policy_rejected']=bad
        for label,changed in mutations.items():
            try:handoff_restored_affine_spectral(prepared,changed,raw,artificial=True)
            except (ValueError,ArithmeticError,KeyError):checks[label]=True
            else:checks[label]=False
    return {'checks':checks,'all_passed':bool(all(checks.values())),
        'only_new_ninth_handoff_metadata_is_tested':True,
        'old_developer_suites_geometry_J_LP_or_research_not_executed':True,
        'labelled_metadata_is_not_a_new_scientific_surface':True}


def _pipeline_io_development():
    """New dictionary dispatch only; every old scientific call is a stub."""
    from contextlib import ExitStack
    from types import SimpleNamespace
    from unittest.mock import patch
    import sys
    module=sys.modules[__name__]
    fixture=_new_ninth_handoff_fixture();prepared=fixture['prepared_affine']
    restoration=copy.deepcopy(prepared[3]['temporary_input_restoration'])
    restoration.update(regenerated_final_equals_observed_SOC_ec76=False,
        regenerated_final_equals_observed_body103_bfbd=False,
        regenerated_final_equals_observed_tail154_2ee6=False,
        regenerated_final_equals_observed_height159_b429=False)
    replay=copy.deepcopy(prepared[3]);replay['temporary_input_restoration']=restoration
    replay['temporary_input_restorations']=[copy.deepcopy(restoration) for _ in range(8)]
    shared=(prepared[0],prepared[1],prepared[2],replay,prepared[4],prepared[5])
    expected_field=prepared[0][0]
    labels=['growth','strip','SOC','body103','tail154','height159','hold','factorized','affine','new']
    def one_case(fail_ninth):
        counts={name:0 for name in labels};paths=[];handoffs=[];identities=[]
        def stub(label):
            def call(p,out,**kwargs):
                counts[label]+=1;paths.append(Path(out));identities.append(p[0][0] is expected_field)
                report={'schema':'new-complete-affine-dictionary-pipeline-fixture','status':'complete','label':label}
                if label=='hold':report=copy.deepcopy(fixture['hold_report'])
                if label=='factorized':report=copy.deepcopy(fixture['factorized_report'])
                if label=='affine':
                    report=copy.deepcopy(fixture['affine_report'])
                    if fail_ninth:
                        report['status']='original-selected-affine-stage-error'
                        report['error']={'type':'ValueError','message':'NEW_NINTH_PREFIX_ORIGINAL_ERROR'}
                        report[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']=None
                atomic_save(out,report)
                return report
            return call
        def final_handoff(p,report,binding,**kwargs):
            handoffs.append((p,report,binding))
            if report.get('status')!=selected_driver.COMPLETE:
                raise ValueError('completed current temporary affine159 result required')
            return p
        def new_stage(p,out,**kwargs):
            counts['new']+=1;identities.append(p[0][0] is expected_field)
            report={'schema':SCHEMA,'status':COMPLETE,'new_scientific_solver_calls':1,
                'artificial_dictionary_dispatch_only':True}
            atomic_save(out,report);return report
        parent='/dev/shm' if Path('/dev/shm').is_dir() else None
        with tempfile.TemporaryDirectory(prefix='new-complete-affine-IO-only-',dir=parent) as folder:
            args=SimpleNamespace(out=Path(folder)/'metric-height159-complete-affine-audit.json')
            printed=io.StringIO()
            with ExitStack() as stack:
                stack.enter_context(patch.object(module,'require_frozen_prefix_sources',return_value=None))
                stack.enter_context(patch.object(growth,'prepare_run',return_value=shared))
                stack.enter_context(patch.object(soc,'prefix_outcome_text',return_value='existing dictionary stub numeric output\n'))
                stack.enter_context(patch.object(capacity_driver,'input_production_outcome_text',return_value='existing dictionary stub numeric output\n'))
                for mod,label in [(growth,'growth'),(strip,'strip'),(soc,'SOC'),(body103,'body103'),
                        (tail154,'tail154'),(height159,'height159'),(capacity_driver,'hold'),
                        (previous_driver,'factorized'),(selected_driver,'affine')]:
                    stack.enter_context(patch.object(mod,'run_audit',side_effect=stub(label)))
                for mod,name in [(strip,'handoff_restored_growth'),(soc,'handoff_restored_strip'),
                        (body103,'handoff_restored_soc'),(tail154,'handoff_restored_body103'),
                        (height159,'handoff_restored_tail154'),(frozen,'handoff_restored_height159'),
                        (previous_driver,'handoff_restored_capacity_hold'),
                        (selected_driver,'handoff_restored_factorized_rows')]:
                    stack.enter_context(patch.object(mod,name,return_value=shared))
                stack.enter_context(patch.object(capacity_driver,'reserve_prepared_stage',
                    side_effect=lambda p,key:(p,{'stage_key':key,'fixture_only':True})))
                stack.enter_context(patch.object(capacity_driver,'annotate_validated_input_handoff',side_effect=lambda p,*a:p))
                stack.enter_context(patch.object(capacity,'initialization_diagnostic',return_value={'contract_pass':None}))
                stack.enter_context(patch.object(module,'handoff_restored_affine_spectral',side_effect=final_handoff))
                stack.enter_context(patch.object(module,'run_audit',side_effect=new_stage))
                stack.enter_context(patch.object(module,'save_report',side_effect=atomic_save))
                stack.enter_context(redirect_stdout(printed))
                run_pipeline(args,artificial=True,evaluate_only=True)
            written=json.loads(args.out.read_text())
            return {'counts':counts,'same_field':all(identities),
                'one_new_handoff_same_prepared':len(handoffs)==1 and handoffs[0][0] is shared,
                'temporary_inputs_removed':bool(paths and all(not p.exists() for p in paths)),
                'result':written,'original_error_printed':'NEW_NINTH_PREFIX_ORIGINAL_ERROR' in printed.getvalue()}
    good=one_case(False);bad=one_case(True)
    checks={
        'nine_inputs_once_then_only_one_new_stage':bool(
            all(good['counts'][k]==1 for k in labels) and good['result']['status']==COMPLETE),
        'same_runtime_field_reaches_new_handoff_and_stage':bool(
            good['same_field'] and good['one_new_handoff_same_prepared']),
        'original_ninth_failure_prevents_science_and_preserves_none_point_and_error':bool(
            all(bad['counts'][k]==1 for k in labels if k!='new') and bad['counts']['new']==0
            and bad['original_error_printed']
            and bad['result']['last_temporary_prefix_diagnostic']['selected_physical_state_sha256'] is None
            and bad['result']['last_temporary_prefix_diagnostic']['error']['message']=='NEW_NINTH_PREFIX_ORIGINAL_ERROR'),
        'temporary_prefix_payloads_removed_in_both_paths':bool(
            good['temporary_inputs_removed'] and bad['temporary_inputs_removed'])}
    return {'checks':checks,'all_passed':bool(all(checks.values())),
        'dictionary_stubs_are_not_optimizers_or_scientific_reexecutions':True,
        'old_developer_suites_not_called':True}


def _print_development_part(name,result):
    p=Path(__file__)
    record={'schema':SCHEMA+'-development-part','part':name,'result':result,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'driver_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'artificial_inputs_only':True}
    print('DEVELOPMENT_PART '+json.dumps(record,ensure_ascii=False,sort_keys=True,
        separators=(',',':'),allow_nan=False),flush=True)


def developer_check():
    hold_library.require_public_research_environment()
    started=time.monotonic()
    kernels=new_development.run_development()
    _print_development_part('new-complete-grid-direction-and-four-maxima',kernels)
    handoff=_handoff_development();_print_development_part('new-ninth-handoff',handoff)
    dispatch=_pipeline_io_development();_print_development_part('new-nine-input-pipeline-IO',dispatch)
    passed=bool(kernels['all_passed'] and handoff['all_passed'] and dispatch['all_passed'])
    return {'schema':SCHEMA+'-development','completion':'complete','passed':passed,
        'development':{'all_passed':passed},'new_complete_grid_checks':kernels,
        'new_ninth_handoff_checks':handoff,'new_pipeline_IO_checks':dispatch,
        'artificial_inputs_only':True,'old_developer_suites_executed':False,
        'research_prefixes_or_scientific_geometry_not_executed':True,
        'source_files_sha256':implementation_hashes(),'elapsed_seconds':time.monotonic()-started,
        'maximum_RSS_MiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024}


def main():
    started=time.monotonic();parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-complete-affine-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_complete_affine_only:
        try:
            result=developer_check()
        except Exception as error:
            result={'schema':SCHEMA+'-development-error','completion':'implementation_check_failed',
                'passed':False,'development':{'all_passed':False},'artificial_inputs_only':True,
                'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
            atomic_save(args.out,result)
            print('COMPLETE_REPORT '+json.dumps(result,ensure_ascii=False,sort_keys=True,
                separators=(',',':'),allow_nan=False),flush=True)
            raise
        atomic_save(args.out,result)
        print('COMPLETE_REPORT '+json.dumps(result,ensure_ascii=False,sort_keys=True,
            separators=(',',':'),allow_nan=False),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    report=run_pipeline(args,process_started=started)
    # The full temporary solver payload stays on the runner only. Existing
    # detailed numeric outcome printers plus this native compact summary give
    # the result and errors directly in the public log.
    compact=small_summary(report,args.out)
    print('COMPLETE_REPORT '+json.dumps(compact,ensure_ascii=False,sort_keys=True,
        separators=(',',':'),allow_nan=False),flush=True)
    print(json.dumps({'out':str(args.out),'status':report.get('status')}),flush=True)
    if report.get('status')!=COMPLETE:raise SystemExit(1)


if __name__=='__main__':main()

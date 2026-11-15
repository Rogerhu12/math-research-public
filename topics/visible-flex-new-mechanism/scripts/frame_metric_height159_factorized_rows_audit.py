#!/usr/bin/env python3
"""One new selected-J evaluation stage after seven necessary frozen restorations.

The physical163 family, independent159 map, exact H/reference, immutable g/b0,
all original coarse/fine IDs and the completed successful-SOC controller state
survive the final handoff. Only selected Jacobian contraction is changed.
No capacity, LP, value or active-time limit is enlarged here. All new checks
and scientific work run only in this repository's public GitHub Actions.
Recomputable payloads are temporary; the publisher retains metadata only.
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
from frame_metric_height159_soc_hold import (
    run_soc_hold_recovery,retention_definition)
from frame_metric_height159_factorized_rows import (
    FactorizedHeight159Objective,configuration as factorized_configuration,
    implementation_hashes as factorized_hashes)
from frame_selected_row_radial_jacobian import POLICY as FACTORIZATION_POLICY
import frame_selected_row_radial_jacobian_development as new_development
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
SCHEMA='same159-selected-row-radial-factorization-after-seven-restorations-v1'
STAGE='metric_height159_factorized_rows_stage'
COMPLETE='complete-two-grid-height159-factorized-selected-J-audit'
PREFIX_STAGE=capacity_driver.STAGE
FROZEN_DEPENDENCIES={
    'frame_metric_height159_capacity_soc_hold_audit.py':'82a3b0f221f16a746e92d63208ad95a6a11374176c4c23e40d7f4315c83895f4',
    'frame_height159_fine_capacity.py':'b1e37f22e46845bea2d4ed44a61ae5ca0a1940b3f60285c339eaaf6a7d80b6bd',
    'frame_metric_height159_soc_hold_audit.py':'172567136e6cfd9373cdd41556555a3cb92938dc2ee8c6e238f42dcb13ab927e',
    'frame_metric_height159_soc_hold.py':'c6fb9d46840c64f9b6a43146ebbece8928e78f9efe609a624cf8ee4cc1da47de'}
NEW_DEPENDENCIES={
    'frame_selected_row_radial_jacobian.py':'e487cdfe3e508e572850217230ebd406736d360fd7e9d8e33b60ad50ba3e2632',
    'frame_metric_height159_factorized_rows.py':'b6c9fff497c0f22c5a12546c47349cc0274ed493f895547fc5c65cf99ba3d403',
    'frame_selected_row_radial_jacobian_development.py':'46aeefbbd7549150d8d03018b0038ec4389a7392a9efc2d7f25299c7575c8d39'}


def implementation_hashes():
    result=capacity_driver.implementation_hashes()
    result.update(factorized_hashes())
    result.update(new_development.implementation_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def require_frozen_prefix_sources():
    capacity_driver.require_frozen_prefix_sources()
    actual=implementation_hashes()
    for name,expected in {**FROZEN_DEPENDENCIES,**NEW_DEPENDENCIES}.items():
        if actual.get(name)!=expected:
            raise ValueError('selected-J source dependency differs: '+name)


def restored_successful_SOC_controller(stage,cfg,expected_source_controller):
    """Replay complete recorded scalar updates, without any geometry or LP."""
    retention_definition(cfg)
    init=stage.get('solver',{}).get('inherited159_controller_without_reset',{})
    if init.get('restored_height159_controller_inherited')!=expected_source_controller:
        raise ValueError('seventh-prefix original159 controller provenance differs')
    radius=float(Q(init['inherited_body_radius_exact_binary64']))
    streak=init['inherited_success_streak']
    if (not np.isfinite(radius) or radius<=0 or type(streak) is not int or not 0<=streak<2
            or radius!=expected_source_controller['trust_evaluated']
            or streak!=expected_source_controller['success_streak']
            or Q(init['inherited_tail_radius_exact_binary64'])!=Q.from_float(radius)/8
            or Q(init['inherited_height_radius_exact_binary64'])!=4*Q.from_float(radius)):
        raise ValueError('seventh-prefix initial block radius or streak differs')
    models=stage.get('solver',{}).get('models',[]);without_update=False;held=[]
    for i,model in enumerate(models):
        if model.get('number')!=i+1 or model.get('trust_before_model')!=radius:
            raise ValueError('seventh-prefix sequential model radius differs')
        update=model.get('scale_feedback_update')
        if update is None:
            if i!=len(models)-1:
                raise ValueError('only the final model may have incomplete control')
            without_update=True;continue
        radius_next,streak_next,expected=hold_library.next_soc_hold_trust(
            model,update['trust_after_original_controller'],streak,cfg)
        if expected!=update:
            raise ValueError('seventh-prefix update differs from full successful-SOC rule')
        if update['successful_SOC_radius_retention']['retained_without_growth']:
            held.append(i+1)
        radius,streak=radius_next,streak_next
    if (stage.get('last_restricted_trust')!=radius
            or stage.get('final_consecutive_growth_qualifying_models')!=streak):
        raise ValueError('seventh-prefix terminal controller differs')
    return {'schema':'recorded-successful-SOC-controller-inherited-by-factorized-J-v1',
        'trust_evaluated':radius,'trust_binary64_exact':str(Q.from_float(radius)),
        'success_streak':streak,'last_model_without_completed_scale_feedback':without_update,
        'origin':'same-job capacity-SOC-hold initialization and all completed original successful-SOC updates',
        'successful_SOC_model_numbers_that_really_retained_radius':held,
        'unfinished_last_model_not_counted_as_success':without_update,
        'new_stage_inherits_actual_terminal_radius_and_streak_without_reset':True,
        'old_mapped_controller_is_not_substituted_for_successful_SOC_controller':True}


def handoff_restored_capacity_hold(prepared,prefix,raw_binding,*,artificial=False):
    """Validate and reuse the SAME exact height reference/H; no field is rebuilt."""
    require_frozen_prefix_sources()
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if not isinstance(problem,FiveHeightField) or not isinstance(gate,FiveNullHeightGate):
        raise ValueError('the original159 runtime field and exact null gate must survive restoration')
    if (prefix.get('schema')!=capacity_driver.SCHEMA
            or prefix.get('status')!='complete-two-grid-height159-capacity-SOC-hold-audit'
            or bool(prefix.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed current temporary capacity-SOC-hold result required')
    count_keys=['growth','strip','SOC','body103','tail154']
    if (prefix.get('source_files_sha256')!=capacity_driver.implementation_hashes()
            or prefix.get('configuration')!=old_cfg or prefix.get('exact_input_storage')!=bindings
            or prefix.get('input_replay')!=old_replay
            or prefix.get('initial_state')!=problem.state_record(old_initial)
            or prefix.get('old_optimizer_calls_this_run')!=5
            or any(prefix.get('necessary_'+k+'_prefix_restoration_calls')!=1 for k in count_keys)
            or prefix.get('new_scientific_solver_calls')!=2
            or prefix.get('capacity_height159_input_production_calls')!=1
            or prefix.get('capacity_SOC_hold_calls')!=1
            or prefix.get('capacity_SOC_hold_solver_calls')!=1
            or prefix.get('unchanged_complete_metric_immutable_b0_and_permanent_anchor') is not True
            or prefix.get('independent_coordinate_definition')!=problem.coordinate_definition):
        raise ValueError('seventh-prefix source/configuration/inputs/initial or exact reference identity differs')
    if not artificial and (prefix.get('github_sha')!=os.environ.get('GITHUB_SHA')
            or str(prefix.get('github_run_id'))!=os.environ.get('GITHUB_RUN_ID')
            or prefix.get('github_repository')!='Rogerhu12/math-research-public'
            or problem.nunknown!=159 or problem.physical_parameter_count!=163):
        raise ValueError('seventh prefix must be the current public job and same159/163 family')
    if prefix.get('capacity_diagnostic_error') is not None:
        raise ValueError('capacity initialization diagnostic failed before factorized-J handoff')
    capacity_records=prefix.get('fine_initialization_capacity_reservations',[])
    history_records=[{k:v for k,v in item.items() if k!='executed_configuration_sha256'}
        for item in capacity_records]
    if history_records!=old_cfg.get(capacity.HISTORY_KEY):
        raise ValueError('capacity hold full reservation history differs from current configuration')
    if (not capacity_records or old_replay.get('current_fine_initialization_capacity_reservation')!=capacity_records[-1]
            or old_cfg.get(capacity.CAP_KEY)!=capacity_records[-1].get('new_fine_capacity')):
        raise ValueError('capacity hold current declaration differs from inherited final resource limit')
    if capacity_records[-1].get('executed_configuration_sha256')!=capacity.digest(old_cfg):
        raise ValueError('capacity hold actual executed configuration hash differs')
    stage=prefix[PREFIX_STAGE]
    if stage.get('error') is not None or 'error' in stage.get('status',''):
        raise ValueError('seventh-prefix implementation failure is not a usable restoration')
    snap=stage['checkpoint'];point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('seventh-prefix selected exact159 state missing')
    checked=exact_vector(point.get('exact_binary64_independent_coordinates'),159)
    state=np.asarray(point.get('independent_coordinates_binary64'),float)
    if state.shape!=checked.shape or not np.array_equal(state,checked):
        raise ValueError('seventh-prefix numerical159 coordinates differ from exact rationals')
    state=state.copy()
    if (coefficients(state)!=point.get('exact_binary64_independent_coordinates')
            or [str(q) for q in problem.coordinates.physical_exact(state)]!=point.get('exact_original_physical_coefficients')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or point.get('coordinate_definition_sha256')!=problem.coordinate_definition_sha256
            or prefix.get('final_state')!=problem.state_record(state)
            or snap.get('independent_coordinate_definition')!=problem.coordinate_definition):
        raise ValueError('seventh-prefix canonical physical/rational-coordinate identity differs')
    accepted=snap.get('accepted_iterates',[])
    if not accepted or accepted[-1]!=point:
        raise ValueError('seventh-prefix selected state is not its last accepted state')
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
        raise ValueError('seventh-prefix exact null sum, fixed heights or coupled original box failed')
    validation=prefix.get('final_selection_validation',{})
    if not validation.get('both_value_grids_hard_and_old_metric_pass'):
        raise ValueError('seventh-prefix independent final two-grid gates failed')
    decisions=[prefix.get(k,{}) for k in ['final_full_grid_constraints','final_doubled_constraints']]
    for d in decisions:
        if not d.get('single_grid_admissible_recovery_point'):
            raise ValueError('seventh-prefix complete-grid admissibility missing')
        for key in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
                'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']:
            if d.get(key)!=old_cfg[key]:raise ValueError('seventh-prefix gate definition differs: '+key)
    if validation.get('both_grid_maximum_eta')!=max(d['direct_max_eta'] for d in decisions):
        raise ValueError('seventh-prefix complete-grid maximum differs')
    radial,theta,grid=curvature_grid(tenth)
    if prefix.get('full_value_sampling_definition')!=grid:
        raise ValueError('seventh-prefix full sampling coordinates/structure differ')
    histories=[snap.get(k,[]) for k in ['active_row_pool_history','fine_physical_row_pool_history']]
    if not all(histories):raise ValueError('seventh-prefix full pool histories missing')
    coarse,fine=(h[-1] for h in histories);ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,total,rule,cap,previous in [
        (coarse,ci,11*len(radial)*len(theta),'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',old_cfg['max_pool_rows'],old_coarse),
        (fine,fi,22*len(radial)*len(theta),'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',old_cfg['max_fine_physical_pool_rows'],old_fine)]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=list(GROUPS)
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap or not set(previous).issubset(ids)):
            raise ValueError('seventh-prefix pool IDs/order/layout/cap or inherited rows differ')
    added=fine.get('added_row_indices');fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added) or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=rows_api.fine_coordinates(added,radial,fine_theta)):
        raise ValueError('seventh-prefix fine original row coordinates differ')
    locations={}
    for d in [decisions[-1]]+[r.get('decision',{}) for r in snap.get('saved_fine_trials',[])
            if r.get('status')=='complete-doubled-angle-value-call']:
        loc=d.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('seventh-prefix metric peak is nonfinite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    continuation=restored_successful_SOC_controller(stage,old_cfg,old_replay['controller_continuation'])
    restoration={'schema':'same-job-temporary-capacity-SOC-hold-restoration-for-factorized-J-v1',
        'purpose':'necessary input restoration under metadata-only policy, not another scientific comparison',
        'prefix_scientific_implementation_sha256':capacity_driver.implementation_hashes(),
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
    learned={'schema':'temporary-capacity-SOC-hold-complete-learned-pool-handoff-v1',
        'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'all_previous_coarse_and_fine_integer_IDs_retained':True,
        'groups2_to10_have_original_actual_values_and_derivatives':True}
    cfg=factorized_configuration(old_cfg);replay=copy.deepcopy(old_replay)
    replay.update(schema='temporary-capacity-SOC-hold-to-factorized-selected-J-handoff-v1',
        canonical_physical_state_sha256=point['physical_state_sha256'],learned_pool=learned,
        known_fine_metric_locations=list(locations.values()),temporary_input_restoration=restoration,
        controller_continuation=continuation,
        temporary_input_restorations=copy.deepcopy(old_replay['temporary_input_restorations'])+[restoration],
        same_runtime_field_reference_and_coordinate_map_reused=True,
        source_capacity_hold_independent_coordinate_definition_sha256=problem.coordinate_definition_sha256)
    replay['explicit_new_constraint_definition'].update(
        successful_SOC_radius_retention=retention_definition(cfg),
        original_actual_gate_and_LP_definitions_unchanged=True,
        prior159_independent_coordinate_map_and_reference_unchanged=True,
        new_height_to_body_radius_exact_is_inherited_not_new_here='4',
        no_historical_canonical_state_is_assumed_or_forced=True,
        selected_row_radial_factorization_policy=FACTORIZATION_POLICY,
        current_reference_H_g_b0_physical_family_and_all_acceptance_gates_preserved=True,
        full_successful_SOC_controller_and_capacities_inherited_without_reset=True)
    return ((problem,state,gate,lower,upper,source_cfg,cfg),bindings,tenth,replay,
        np.asarray(ci,np.int64),np.asarray(fi,np.int64))



def _frozen_format_view(report):
    """Printing only: the actual new stage dictionary is never modified."""
    view=dict(report)
    if STAGE in view:view[frozen.STAGE]=view.pop(STAGE)
    return view


def small_summary(report,out):
    if not isinstance(report.get('configuration'),dict):
        # A prefix can fail before there is any new objective/configuration.
        # Keep the exact original error and available identities; do not ask
        # an old scientific summary printer to invent a missing stage.
        keys=['schema','status','phase','source_files_sha256','github_sha','github_run_id',
            'github_repository','artificial_inputs_only','old_optimizer_calls_this_run',
            'new_scientific_solver_calls','new_stage_call_counter_semantics',
            'temporary_prefix_raw_bindings','temporary_input_restorations',
            'last_temporary_prefix_diagnostic','capacity_input_restoration_reservations',
            'capacity_input_restoration_diagnostics','process_total_elapsed_seconds','error']
        keys += [k for k in report if k.startswith('necessary_') and k.endswith('_calls')]
        return {k:copy.deepcopy(report[k]) for k in keys if k in report}
    view=_frozen_format_view(report)
    summary=frozen.small_summary(view,out)
    if frozen.STAGE in summary:summary[STAGE]=summary.pop(frozen.STAGE)
    for key in ['schema','source_files_sha256','necessary_capacity_SOC_hold_prefix_restoration_calls',
            'factorization_policy','factorized_selected_J_execution','algorithm_stage_scope',
            'last_temporary_prefix_diagnostic','capacity_input_restoration_reservations',
            'capacity_input_restoration_diagnostics','seventh_handoff_summary',
            'new_stage_call_counter_semantics','error','pipeline_failure']:
        if key in report:summary[key]=copy.deepcopy(report[key])
    stage=report.get(STAGE,{})
    snapshot=stage.get('checkpoint',{})
    if STAGE in summary:
        summary[STAGE]['factorized_selected_J_execution']=copy.deepcopy(
            snapshot.get('selected_row_factorization_statistics'))
        summary[STAGE]['actual_inherited_successful_SOC_controller']=copy.deepcopy(
            stage.get('solver',{}).get('inherited159_controller_without_reset'))
    return summary


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),
        allow_nan=False)+'\n')
    os.replace(tmp,path)


def print_new_stage_outcomes(report):
    view=_frozen_format_view(report)
    text=frozen.supplementary_outcome_text(view)
    text=text.replace(
        'CONDITIONAL SUCCESSFUL-SOC RADIUS RETENTION: SAME159 COORDINATES AND SAME163 PHYSICAL FAMILY',
        'SELECTED-ROW RADIAL JACOBIAN FACTORIZATION: SAME159/SAME163 AND SUCCESSFUL-SOC RULE')
    text=text.replace(
        'All six necessary prefixes are input restoration, not new scientific progress or forced historical hashes.',
        'All seven declared prior stages are one-time necessary input restoration for this experiment; no historical state is forced.')
    print(text,end='',flush=True)
    extra={k:copy.deepcopy(report.get(k)) for k in [
        'schema','status','phase','factorization_policy','factorized_selected_J_execution',
        'algorithm_stage_scope','seventh_handoff_summary','value_evaluation_counts',
        'new_stage_call_counter_semantics','error','pipeline_failure']}
    print('FACTORIZED SELECTED-J ACTUAL '+json.dumps(extra,ensure_ascii=False,sort_keys=True,
        separators=(',',':'),allow_nan=False),flush=True)


def print_existing_prefix(label,report,receipt):
    """Keep every old value while stating its current restoration purpose."""
    text=soc.prefix_outcome_text(report,receipt,label)
    print(text,end='',flush=True)


def capacity_hold_diagnostic(report,binding):
    """Available failure/context metadata only, before any successful handoff."""
    stage=report.get(PREFIX_STAGE,{})
    snapshot=stage.get('checkpoint',{})
    point=snapshot.get('selected_two_grid_physical_point') or {}
    return {'schema':'capacity-SOC-hold-current-temporary-handoff-diagnostic-v1',
        'raw_binding':copy.deepcopy(binding),'status':report.get('status'),
        'phase':report.get('phase'),'error':copy.deepcopy(report.get('error')),
        'stage_status':stage.get('status'),'stage_error':copy.deepcopy(stage.get('error')),
        'stage_budget_message':stage.get('budget_message'),
        'selected_physical_state_sha256':point.get('physical_state_sha256'),
        'last_restricted_trust':stage.get('last_restricted_trust'),
        'success_streak':stage.get('final_consecutive_growth_qualifying_models'),
        'solver_call_counts':{k:stage.get('solver',{}).get(k) for k in [
            'linear_program_invocation_count','primary_LP_invocation_count','correction_LP_invocation_count']},
        'available_factorization_input_capacity':report.get('configuration',{}).get(capacity.CAP_KEY),
        'no_missing_error_or_history_or_pool_size_is_inferred':True}


def run_pipeline(args,*,artificial=False,evaluate_only=False,process_started=None):
    started=time.monotonic() if process_started is None else process_started
    phase='public-environment-and-original24-input-contract';restorations=[];raw_bindings=[]
    last_prefix_diagnostic=None;reservations=[];capacity_diagnostics=[]
    invoked={'growth':0,'strip':0,'SOC':0,'body103':0,'tail154':0,'height159':0,'hold':0,'factorized':0}
    try:
        require_frozen_prefix_sources()
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        parent='/dev/shm' if artificial and Path('/dev/shm').is_dir() else os.environ.get('RUNNER_TEMP')
        with tempfile.TemporaryDirectory(prefix='visible-factorized-J-seven-inputs-',dir=parent) as folder:
            growth_out=Path(folder)/'restored-growth.json';strip_out=Path(folder)/'restored-strip.json'
            soc_out=Path(folder)/'restored-scaled-SOC.json';body_out=Path(folder)/'restored-body103.json'
            tail_out=Path(folder)/'restored-tail154.json';height_out=Path(folder)/'restored-height159.json'
            hold_out=Path(folder)/'restored-capacity-SOC-hold.json'
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
            last_prefix_diagnostic=capacity_hold_diagnostic(previous,binding)
            print('SEVENTH PREFIX HANDOFF DIAGNOSTIC '+json.dumps(last_prefix_diagnostic,
                ensure_ascii=False,sort_keys=True,allow_nan=False),flush=True)
            final_prepared=handoff_restored_capacity_hold(
                new_prepared,previous,binding,artificial=artificial)
            restorations=list(final_prepared[3]['temporary_input_restorations'])
            print_existing_prefix('capacity-SOC-hold-complete-parameters',previous,restorations[-1])
            print('All seven prior invocations are necessary input restoration for this new selected-J experiment. '
                'The same runtime Field/H and actual terminal successful-SOC controller continue. '
                'No new capacity, retry, budget extension or historical canonical target.',flush=True)
            del previous,new_prepared
            phase='one-new-factorized-selected-J-stage';invoked['factorized']=1
            return run_audit(final_prepared,args.out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
    except Exception as error:
        failure={'schema':SCHEMA,'status':'factorized-J-pipeline-failed-last-written-checkpoint-preserved',
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
            'old_optimizer_calls_this_run':sum(invoked[k] for k in invoked if k!='factorized'),
            'new_scientific_solver_calls':invoked['factorized'],
            'new_stage_call_counter_semantics':'only factorized selected-J is new; seven exact prior stage invocations are restoration',
            'capacity_input_restoration_reservations':copy.deepcopy(reservations),
            'capacity_input_restoration_diagnostics':copy.deepcopy(capacity_diagnostics),
            'temporary_prefix_raw_bindings':raw_bindings,'temporary_input_restorations':restorations,
            'last_temporary_prefix_diagnostic':copy.deepcopy(last_prefix_diagnostic),
            'process_total_elapsed_seconds':time.monotonic()-started,
            'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
        if invoked['factorized'] and Path(args.out).exists():
            try:
                existing=json.loads(Path(args.out).read_text())
                if existing.get('schema')==SCHEMA:
                    existing['scientific_status_before_pipeline_failure']=existing.get('status')
                    existing['status']='factorized-J-pipeline-error-last-checkpoint-preserved'
                    existing['pipeline_failure']=failure
                    save_report(args.out,existing)
                    print('FACTORIZED-J PIPELINE FAILURE '+json.dumps(failure['error'],allow_nan=False),flush=True)
                    return existing
            except (OSError,ValueError,TypeError,KeyError):
                pass
        save_report(args.out,failure)
        print('FACTORIZED-J PIPELINE FAILURE '+json.dumps(failure['error'],
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
        raise ValueError('same actual159 coordinates do not match the seventh-prefix state')
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':7,'necessary_growth_prefix_restoration_calls':1,
        'necessary_strip_prefix_restoration_calls':1,'necessary_SOC_prefix_restoration_calls':1,
        'necessary_body103_prefix_restoration_calls':1,'necessary_tail154_prefix_restoration_calls':1,
        'necessary_height159_prefix_restoration_calls':1,
        'necessary_capacity_SOC_hold_prefix_restoration_calls':1,
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
        'process_clock_scope':'seven one-time necessary restorations, then one same-budget selected-J stage; clocks separate'}
    report.update(
        factorization_policy=FACTORIZATION_POLICY,
        algorithm_stage_scope={
            'seven_prior_scientific_stage_implementations_and_complete_parameters_reused_once':True,
            'capacity159_producer_and_hold_are_now_input_restoration_not_new_comparisons':True,
            'only_selected_parameter_J_evaluation_changes_in_this_stage':True,
            'same159_coordinates_same163_family_same_g_b0_reference_and_H':True,
            'all_original_pool_IDs_and_actual_successful_SOC_terminal_controller_inherited':True,
            'no_new_capacity_reservation_or_LP_value_active_time_extension':True,
            'all_ordinary_values_actual_gates_and_final_two_grids_unchanged':True,
            'floating_reassociation_can_change_rows_LP_choices_and_trajectory':True},
        new_stage_call_counter_semantics='seven necessary prior driver invocations; one new factorized-J driver, never LP counts',
        seventh_handoff_summary=copy.deepcopy(replay['temporary_input_restoration']),
        capacity_input_restoration_reservations=copy.deepcopy(cfg.get(capacity.HISTORY_KEY,[])))
    def save(status):
        now=time.monotonic();snapshot=report.get(STAGE,{}).get('checkpoint',{})
        report['factorized_selected_J_execution']=copy.deepcopy(
            snapshot.get('selected_row_factorization_statistics'))
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=snapshot.get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('original24-inputs-seven-prefixes-and-exact-height-reference-replayed-before-new-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='height159-factorized-selected-J-complete-initialization'
        def checkpoint(snapshot):
            report[STAGE]={'status':'current159-last-qualified-checkpoint','checkpoint':snapshot,'solver':{}}
            save('factorized-selected-J-last-accepted-physical-checkpoint')
        objective=FactorizedHeight159Objective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint,
            radial_nodes_exact=grid['radial_nodes_exact'])
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            temporary_restored_capacity_SOC_hold_raw_sha256=replay['temporary_input_restoration']['prefix_temporary_raw_file']['sha256'],
            learned_pool_replay=replay['learned_pool'],temporary_input_restoration=replay['temporary_input_restoration'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-temporary-capacity-SOC-hold-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-temporary-capacity-SOC-hold-eleven-group-fine-original-IDs','source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_computed_field(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        report['initial_field_diagnostics']={g.label:field_diagnostics(d,g,subspace,cfg) for g,d in
            [(objective.row_grids[0],objective.geometry_cache),(objective.row_grids[1],objective.fine_cache['data'])]}
        save('complete-initial-original-gates-exact-height-map-and-current-height-diagnostics')
        report['phase']='one-shared-budget-height159-factorized-selected-J-stage';report['new_scientific_solver_calls']=1
        # This is the frozen successful-SOC loop, not the older mapped loop.
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
            'seven_necessary_prefix_counts_are_separate':True,
            'failed_fine_and_actual_fine_SOC_residuals_count':True,
            'original_full163_geometry_J_batches_in_new_selected_paths':0,
            'selected_scalar_J_contracted_before_radial_expansion':True,'no_final_optimizer':True}
        report['limitations']={'all_geometric_gates_sampled_only':True,'new_target026_not_exact_isometry':True,
            'hard_cap58_not_final_reach_target':True,'full_nonlocal_reach_not_paid':True,
            'same_g_b0_and_original163_physical_family_not_expanded':True,
            'exact_null_five_coordinate_subfamily_is_not_all_nine_height_variables':True,
            'seven_prior_declared_stages_are_input_restoration_for_this_experiment':True,'no_forced_observed_prefix_hash':True}
        save('height159-factorized-selected-J-controller-error-last-qualified-preserved' if stage.get('error') else
            COMPLETE if eligible else 'final-recheck-failed-do-not-use-as-new-warm-start')
        print_new_stage_outcomes(report)
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('height159-factorized-selected-J-audit-error-last-checkpoint-preserved');print_new_stage_outcomes(report);return report


def _new_handoff_fixture():
    """New metadata fixture built from labelled arrays, never a research point.

    Existing fixture builders supply exact coordinate/box shapes only. No old
    developer suite, geometry evaluator, value decision, Jacobian or LP runs.
    """
    from unittest.mock import patch
    f=frozen._new_io_fixture()
    # This labelled metadata fixture has no previously recorded fine peaks.
    # The real capacity adapter requires the field even when the list is empty.
    f['prepared'][3]['known_fine_metric_locations']=[]
    with patch.object(frozen,'curvature_grid',return_value=(f['radial'],f['theta'],f['grid'])):
        with patch.object(capacity_driver.frozen,'curvature_grid',
                return_value=(f['radial'],f['theta'],f['grid'])):
            producer,reservation1=capacity_driver.reserve_prepared_stage(
                f['prepared'],capacity_driver.CAPACITY_INPUT_STAGE)
            original_prefix=copy.deepcopy(f['prefix'])
            original_prefix['configuration']=producer[0][-1]
            original_prefix['input_replay']=producer[3]
            continued=frozen.handoff_restored_height159(
                producer,original_prefix,f['binding'],artificial=True)
            continued=capacity_driver.annotate_validated_input_handoff(
                continued,reservation1,{'contract_pass':None,'artificial_metadata_fixture':True})
            prepared,reservation2=capacity_driver.reserve_prepared_stage(
                continued,capacity_driver.CAPACITY_HOLD_STAGE)
    field,initial,gate,lo,hi,source_cfg,cfg=prepared[0]
    point=copy.deepcopy(f['prefix'][frozen.PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point'])
    controller=copy.deepcopy(prepared[3]['controller_continuation'])
    radius=controller['trust_evaluated'];streak=controller['success_streak']
    init={'restored_height159_controller_inherited':controller,
        'inherited_body_radius_exact_binary64':str(Q.from_float(radius)),
        'inherited_tail_radius_exact_binary64':str(Q.from_float(radius)/8),
        'inherited_height_radius_exact_binary64':str(4*Q.from_float(radius)),
        'inherited_success_streak':streak}
    snapshot=copy.deepcopy(f['prefix'][frozen.PREFIX_STAGE]['checkpoint'])
    snapshot['selected_two_grid_physical_point']=point
    snapshot['accepted_iterates']=[point]
    snapshot['active_row_pool_history']=[f['pool_builder']([0,1,2,128])]
    snapshot['fine_physical_row_pool_history']=[f['pool_builder']([0,1,2,256],True)]
    stage={'status':'new-labelled-metadata-only-initial-point','error':None,
        'checkpoint':snapshot,'last_restricted_trust':radius,
        'final_consecutive_growth_qualifying_models':streak,
        'solver':{'inherited159_controller_without_reset':init,'models':[],
            'linear_program_invocation_count':0}}
    prefix=copy.deepcopy(f['prefix']);prefix.pop(frozen.PREFIX_STAGE)
    prefix.update(schema=capacity_driver.SCHEMA,
        status='complete-two-grid-height159-capacity-SOC-hold-audit',
        source_files_sha256=capacity_driver.implementation_hashes(),
        configuration=cfg,input_replay=prepared[3],initial_state=field.state_record(initial),
        final_state=field.state_record(initial),
        old_optimizer_calls_this_run=5,new_scientific_solver_calls=2,
        capacity_height159_input_production_calls=1,capacity_SOC_hold_calls=1,
        capacity_SOC_hold_solver_calls=1,necessary_height159_prefix_restoration_calls=0,
        fine_initialization_capacity_reservations=[reservation1,reservation2],
        fine_initialization_capacity_diagnostics=[
            {'contract_pass':None,'artificial_metadata_fixture':True},
            {'contract_pass':None,'artificial_metadata_fixture':True}])
    prefix[PREFIX_STAGE]=stage
    return dict(f,prepared_hold=prepared,hold_report=prefix)


def _handoff_development():
    from unittest.mock import patch
    import sys
    module=sys.modules[__name__]
    fixture=_new_handoff_fixture()
    prepared=fixture['prepared_hold'];prefix=fixture['hold_report']
    field=prepared[0][0]
    raw={'filename':'new-array-capacity-hold-report.json','bytes':1,'sha256':'c'*64}
    with patch.object(module,'curvature_grid',return_value=(
            fixture['radial'],fixture['theta'],fixture['grid'])):
        got=handoff_restored_capacity_hold(prepared,prefix,raw,artificial=True)
        exact_identity=bool(got[0][0] is field and got[0][2] is prepared[0][2]
            and got[0][0].coordinates is field.coordinates
            and got[0][0].coordinates.reference_state.tobytes()==field.coordinates.reference_state.tobytes()
            and got[0][1].tobytes()==prepared[0][1].tobytes())
        old_cfg=prepared[0][-1];new_cfg=got[0][-1]
        budget_keys=['max_linear_models','max_physical_evaluations','max_seconds',
            capacity.CAP_KEY,capacity.HISTORY_KEY]
        parameters=bool(all(new_cfg[k]==old_cfg[k] for k in budget_keys)
            and new_cfg==factorized_configuration(old_cfg)
            and np.array_equal(got[4],np.array([0,1,2,128]))
            and np.array_equal(got[5],np.array([0,1,2,256]))
            and len(got[3]['temporary_input_restorations'])==7)
        failures={}
        bad=copy.deepcopy(prefix)
        bad[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']['exact_original_physical_coefficients'][0]='1'
        mutations={'different_physical163_state':bad}
        bad=copy.deepcopy(prefix);bad['independent_coordinate_definition']={'wrong_reference':True}
        mutations['different_reference_H']=bad
        bad=copy.deepcopy(prefix)
        record=bad[PREFIX_STAGE]['checkpoint']['active_row_pool_history'][-1]
        record['row_indices']=[0,2,128];record['row_count']=3
        record['row_indices_sha256']=digest(record['row_indices'])
        mutations['removed_inherited_original_row']=bad
        bad=copy.deepcopy(prefix);bad[PREFIX_STAGE]['last_restricted_trust']/=2
        mutations['changed_completed_controller_radius']=bad
        bad=copy.deepcopy(prefix);bad['status']='incomplete-original-prefix'
        mutations['incomplete_input_not_usable']=bad
        for name,bad in mutations.items():
            try:handoff_restored_capacity_hold(prepared,bad,raw,artificial=True)
            except (ValueError,ArithmeticError):failures[name]=True
            else:failures[name]=False
    cfg,unused,x,y,z,model=hold_library._new_array_fixture(actual_ratio=.75)
    radius=model['trust_before_model']
    source={'trust_evaluated':radius,'trust_binary64_exact':str(Q.from_float(radius)),
        'success_streak':0,'origin':'new-controller-handoff-array-fixture'}
    init={'restored_height159_controller_inherited':source,
        'inherited_body_radius_exact_binary64':str(Q.from_float(radius)),
        'inherited_tail_radius_exact_binary64':str(Q.from_float(radius)/8),
        'inherited_height_radius_exact_binary64':str(4*Q.from_float(radius)),
        'inherited_success_streak':0}
    next_radius,next_streak,update=hold_library.next_soc_hold_trust(model,radius,0,cfg)
    model['scale_feedback_update']=update
    stage={'solver':{'inherited159_controller_without_reset':init,
        'models':[model,{'number':2,'trust_before_model':next_radius}]},
        'last_restricted_trust':next_radius,
        'final_consecutive_growth_qualifying_models':next_streak}
    continuation=restored_successful_SOC_controller(stage,cfg,source)
    held=bool(update['successful_SOC_radius_retention']['retained_without_growth']
        and next_radius==radius and continuation['trust_evaluated']==radius
        and continuation['successful_SOC_model_numbers_that_really_retained_radius']==[1]
        and continuation['last_model_without_completed_scale_feedback'])
    bad=copy.deepcopy(stage)
    bad['solver']['models'][0]['scale_feedback_update']=copy.deepcopy(
        update['successful_SOC_radius_retention']['old_controller_result'])
    try:restored_successful_SOC_controller(bad,cfg,source)
    except (ValueError,KeyError):old_rule_rejected=True
    else:old_rule_rejected=False
    checks={'same_runtime_H_reference_exact159_and_gate_are_reused':exact_identity,
        'all_old_pools_capacities_and_solver_limits_retained':parameters,
        'completed_actual_SOC_hold_survives_next_stage_handoff':held,
        'substitution_of_old_halving_controller_is_rejected':old_rule_rejected,**failures}
    return {'checks':{k:bool(v) for k,v in checks.items()},
        'all_passed':bool(all(checks.values())),
        'new_replay_used_only_recorded_model_metadata_and_array_fixture_builders':True,
        'old_developer_suites_geometry_J_LP_and_scientific_candidates_not_executed':True,
        'metadata_fixture_not_a_new_surface_or_admissibility_certificate':True}


def _pipeline_io_development():
    """Exercise only the new production dispatch boundary with dictionary stubs."""
    from contextlib import ExitStack
    from types import SimpleNamespace
    from unittest.mock import patch
    import sys
    module=sys.modules[__name__]
    fixture=_new_handoff_fixture();prepared=fixture['prepared_hold']
    restoration=copy.deepcopy(prepared[3]['temporary_input_restoration'])
    restoration.update(regenerated_final_equals_observed_SOC_ec76=False,
        regenerated_final_equals_observed_body103_bfbd=False,
        regenerated_final_equals_observed_tail154_2ee6=False,
        regenerated_final_equals_observed_height159_b429=False)
    replay=copy.deepcopy(prepared[3]);replay['temporary_input_restoration']=restoration
    replay['temporary_input_restorations']=[copy.deepcopy(restoration) for _ in range(6)]
    shared=(prepared[0],prepared[1],prepared[2],replay,prepared[4],prepared[5])
    expected_field=prepared[0][0]
    labels=['growth','strip','SOC','body103','tail154','height159','hold','new']
    def one_case(fail_hold):
        counters={k:0 for k in labels};paths=[];handoff=[];same_runtime=[]
        def stub(label):
            def call(p,out,**kwargs):
                counters[label]+=1;paths.append(Path(out))
                same_runtime.append(p[0][0] is expected_field)
                report={'schema':'new-dictionary-pipeline-fixture','status':'complete',
                    'scientific_stage_label':label}
                if label=='hold':
                    report=copy.deepcopy(fixture['hold_report'])
                    if fail_hold:
                        report['status']='original-capacity-hold-error'
                        report['error']={'type':'ValueError','message':'NEW_HANDOFF_FIXTURE_ORIGINAL_ERROR'}
                        report[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']=None
                atomic_save(out,report)
                return report
            return call
        def reservation(p,stage_key):
            return p,{'stage_key':stage_key,'fixture_only':True}
        def handoff_hold(p,report,binding,**kwargs):
            handoff.append((p,report,binding))
            if report.get('status')!='complete-two-grid-height159-capacity-SOC-hold-audit':
                raise ValueError('completed current temporary capacity-SOC-hold result required')
            return p
        def new_stage(p,out,**kwargs):
            counters['new']+=1;same_runtime.append(p[0][0] is expected_field)
            result={'schema':SCHEMA,'status':COMPLETE,'new_scientific_solver_calls':1,
                'artificial_dictionary_dispatch_only':True}
            atomic_save(out,result);return result
        directory='/dev/shm' if Path('/dev/shm').is_dir() else None
        with tempfile.TemporaryDirectory(prefix='new-factorized-J-IO-only-',dir=directory) as folder:
            args=SimpleNamespace(out=Path(folder)/'new-factorized-audit.json')
            printed=io.StringIO()
            with ExitStack() as stack:
                stack.enter_context(patch.object(module,'require_frozen_prefix_sources',return_value=None))
                stack.enter_context(patch.object(growth,'prepare_run',return_value=shared))
                stack.enter_context(patch.object(soc,'prefix_outcome_text',return_value='existing numeric dictionary stub\n'))
                stack.enter_context(patch.object(capacity_driver,'input_production_outcome_text',
                    return_value='existing numeric dictionary stub\n'))
                for mod,label in [(growth,'growth'),(strip,'strip'),(soc,'SOC'),(body103,'body103'),
                        (tail154,'tail154'),(height159,'height159'),(capacity_driver,'hold')]:
                    stack.enter_context(patch.object(mod,'run_audit',side_effect=stub(label)))
                for mod,name in [(strip,'handoff_restored_growth'),(soc,'handoff_restored_strip'),
                        (body103,'handoff_restored_soc'),(tail154,'handoff_restored_body103'),
                        (height159,'handoff_restored_tail154'),(frozen,'handoff_restored_height159')]:
                    stack.enter_context(patch.object(mod,name,return_value=shared))
                stack.enter_context(patch.object(capacity_driver,'reserve_prepared_stage',side_effect=reservation))
                stack.enter_context(patch.object(capacity_driver,'annotate_validated_input_handoff',side_effect=lambda p,*a:p))
                stack.enter_context(patch.object(capacity,'initialization_diagnostic',return_value={'contract_pass':None}))
                stack.enter_context(patch.object(module,'handoff_restored_capacity_hold',side_effect=handoff_hold))
                stack.enter_context(patch.object(module,'run_audit',side_effect=new_stage))
                stack.enter_context(patch.object(module,'save_report',side_effect=atomic_save))
                stack.enter_context(redirect_stdout(printed))
                result=run_pipeline(args,artificial=True,evaluate_only=True)
            written=json.loads(args.out.read_text())
            cleaned=bool(paths and all(not path.exists() for path in paths))
            error_kept=('NEW_HANDOFF_FIXTURE_ORIGINAL_ERROR' in printed.getvalue())
            return {'counts':counters,'all_same_runtime':all(same_runtime),
                'one_new_handoff_with_same_prepared_hold':len(handoff)==1 and handoff[0][0] is shared,
                'temporary_prefix_files_deleted':cleaned,'result':written,
                'original_error_printed':error_kept}
    good=one_case(False);bad=one_case(True)
    checks={
        'seven_necessary_prefix_dispatches_once_then_one_new_stage':
            all(good['counts'][k]==1 for k in labels) and good['result']['status']==COMPLETE,
        'same_runtime_tuple_reaches_new_handoff_and_stage':
            good['all_same_runtime'] and good['one_new_handoff_with_same_prepared_hold'],
        'original_seventh_failure_prevents_new_stage_and_survives_cleanup':
            all(bad['counts'][k]==1 for k in labels if k!='new') and bad['counts']['new']==0
            and bad['original_error_printed']
            and bad['result']['last_temporary_prefix_diagnostic']['selected_physical_state_sha256'] is None
            and bad['result']['last_temporary_prefix_diagnostic']['error']['message']=='NEW_HANDOFF_FIXTURE_ORIGINAL_ERROR',
        'temporary_payloads_deleted_after_success_and_failure':
            good['temporary_prefix_files_deleted'] and bad['temporary_prefix_files_deleted']}
    return {'checks':{k:bool(v) for k,v in checks.items()},
        'all_passed':bool(all(checks.values())),
        'dictionary_stub_invocations_are_not_scientific_or_optimizer_calls':True,
        'old_developer_suites_not_called':True}


def _print_development_part(name,result):
    # A later fixture error must not erase an already completed new component.
    # These public log records contain actual results, never inferred passes.
    p=Path(__file__)
    record={'schema':SCHEMA+'-development-part','part':name,'result':result,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'driver_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'artificial_inputs_only':True}
    print('DEVELOPMENT_PART '+json.dumps(record,ensure_ascii=False,sort_keys=True,
        separators=(',',':'),allow_nan=False),flush=True)


def developer_check():
    hold_library.require_public_research_environment()
    started=time.monotonic()
    kernels=new_development.developer_check()
    _print_development_part('factorization-kernels-and-parent-cache',kernels)
    handoff=_handoff_development()
    _print_development_part('seventh-handoff-and-full-SOC-controller',handoff)
    dispatch=_pipeline_io_development()
    _print_development_part('new-pipeline-IO',dispatch)
    passed=bool(kernels['development']['all_passed'] and handoff['all_passed'] and dispatch['all_passed'])
    return {'schema':SCHEMA+'-development','completion':'complete','passed':passed,
        'development':{'all_passed':passed},
        'new_factorization_and_actual_parent_cache_checks':kernels,
        'new_seventh_handoff_and_full_SOC_controller_checks':handoff,
        'new_pipeline_IO_checks':dispatch,
        'artificial_inputs_only':True,'old_developer_suites_executed':False,
        'research_prefixes_and_geometry_candidates_not_executed':True,
        'source_files_sha256':implementation_hashes(),
        'elapsed_seconds':time.monotonic()-started,
        'maximum_RSS_MiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024}


def main():
    started=time.monotonic();parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-factorization-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_factorization_only:
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

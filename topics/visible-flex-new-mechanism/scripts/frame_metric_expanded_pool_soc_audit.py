#!/usr/bin/env python3
"""One same-trial expanded-pool SOC stage from the complete source checkpoint.

The full reference, physical coordinates, row pools, controller and original
norm bank are preserved. No old optimizer or developer suite is executed.
Only the new binding/SOC interfaces are checked before the new public run.
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
import sys
import time
import traceback
import numpy as np
from frame_collar_bvp import atomic_save
from frame_height_null_coordinates import digest
from frame_five_height_field import FiveHeightField
from frame_height_null_gate import FiveNullHeightGate
from frame_entry_tail_height_blocks import EntryTailHeight159Subspace
from frame_metric_entry_tail_height159 import restriction_definition, layout_from_problem
from frame_metric_height159_complete_affine import retention_definition
from frame_curvature_soc_metric_reserve_audit import exact_vector
from frame_metric_budget_recovery import recovery_decision
from frame_complete_affine_metric_oracle import definition as model_definition
from frame_selected_row_radial_jacobian import POLICY as FACTORIZATION_POLICY
from frame_metric_expanded_pool_soc import POLICY, ExpandedPoolSOCObjective
from frame_metric_expanded_pool_soc_recovery import run_expanded_pool_soc_recovery
import frame_metric_expanded_pool_soc_transfer as transfer
import frame_metric_norm_memory_audit as previous_audit
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader

SCHEMA = "same159-complete-checkpoint-expanded-pool-SOC-v1"
STAGE = "expanded_pool_SOC_stage"
COMPLETE = "complete-two-grid-expanded-pool-SOC-checkpoint-audit"
curvature_grid = baseline.curvature_grid
audit_computed_field = baseline.audit_computed_field
compare_computed_fields = baseline.compare_computed_fields
field_diagnostics = baseline.field_diagnostics
exact_height_diagnostic = baseline.exact_height_diagnostic
outside_replay = baseline.outside_replay
coefficients = baseline.coefficients


def implementation_hashes():
    result = previous_audit.implementation_hashes()
    folder = Path(__file__).parent
    for name in ("frame_metric_expanded_pool_soc.py",
                 "frame_metric_expanded_pool_soc_recovery.py",
                 "frame_metric_expanded_pool_soc_transfer.py",
                 "frame_metric_expanded_pool_soc_development.py", Path(__file__).name):
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def small_summary(report, out=None):
    omitted = {STAGE, "initial_full_grid_audit", "final_full_grid_audit",
               "final_doubled_angle_audit", "input_replay", "exact_input_storage"}
    result = {key: copy.deepcopy(value) for key, value in report.items() if key not in omitted}
    replay = report.get("input_replay", {})
    result["direct_transfer_source_and_scope"] = copy.deepcopy(replay.get("source_completed_log_transfer"))
    stage = report.get(STAGE, {})
    snap = stage.get("checkpoint", {})
    solver = stage.get("solver", {})
    result[STAGE] = {
        key: copy.deepcopy(stage.get(key)) for key in ("status", "error", "budget_message",
            "new_metric_target_reached_on_both_grids", "last_restricted_trust",
            "final_consecutive_growth_qualifying_models", "cross_center_norm_memory",
            "expanded_pool_same_trial_SOC_definition", "original_bank_replay",
            "expanded_pool_rebound_records", "primary_and_rebound_report_mapping_is_explicit")}
    result[STAGE]["solver"] = {
        key: copy.deepcopy(value) for key, value in solver.items() if key != "models"}
    result[STAGE]["model_count"] = len(solver.get("models", []))
    result[STAGE]["snapshot_scalar_counters"] = {
        key: copy.deepcopy(snap.get(key)) for key in (
            "initialization_elapsed_seconds", "optimization_elapsed_seconds",
            "value_geometry_seconds", "total_full_value_physical_evaluations",
            "coarse_physical_evaluations", "fine_physical_evaluations") if key in snap}
    result[STAGE]["selected_two_grid_physical_point"] = copy.deepcopy(snap.get("selected_two_grid_physical_point"))
    result[STAGE]["accepted_iterates"] = copy.deepcopy(snap.get("accepted_iterates", []))
    result[STAGE]["current_pool_metadata"] = {}
    for name in ("active_row_pool_history", "fine_physical_row_pool_history"):
        history = snap.get(name, [])
        last = history[-1] if history else {}
        result[STAGE]["current_pool_metadata"][name] = {
            key: copy.deepcopy(value) for key, value in last.items()
            if key not in ("row_indices", "added_row_indices", "added_original_grid_coordinates")}
    return result


def save_report(out, report):
    atomic_save(out, report)
    summary = Path(out).with_name(Path(out).stem+"-summary.json")
    atomic_save(summary, small_summary(report, out))


def emit(kind, value):
    print(kind+" "+reader.encoded(value).decode("utf-8"), flush=True)


def print_new_stage_outcomes(report):
    for model in report.get(STAGE, {}).get("solver", {}).get("models", []):
        emit("EXPANDED_SOC_MODEL", model)
    emit("EXPANDED_SOC_COMPLETE", small_summary(report))


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
        raise ValueError('transferred exact159 coordinates differ from pinned physical state')
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':0,'necessary_growth_prefix_restoration_calls':0,
        'necessary_strip_prefix_restoration_calls':0,'necessary_SOC_prefix_restoration_calls':0,
        'necessary_body103_prefix_restoration_calls':0,'necessary_tail154_prefix_restoration_calls':0,
        'necessary_height159_prefix_restoration_calls':0,
        'necessary_capacity_SOC_hold_prefix_restoration_calls':0,
        'necessary_factorized_selected_J_prefix_restoration_calls':0,
        'necessary_selected_affine_prefix_restoration_calls':0,
        'new_scientific_solver_calls':0,'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':problem.state_record(initial),'timing_segments':{},
        'unchanged_complete_metric_immutable_b0_and_permanent_anchor':True,
        'current_height_is_allowed_to_change_with_exact_zero_total_integral':True,
        'prepare_elapsed_seconds':prepare_seconds,'learned_pool_replay':replay['learned_pool'],
        'temporary_input_restorations':[],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'restricted_proposal_definition':restriction_definition(cfg),
        'independent_coordinate_definition':coord,
        'successful_SOC_radius_retention_definition':retention_definition(cfg),
        'initial_exact_height_diagnostic':exact_height_diagnostic(problem,initial),
        'process_clock_scope':'read24 completed reports and two immutable completed logs; exact checkpoint and bank input replay; one expanded-pool SOC stage; no old optimizer'}
    report.update(
        factorization_policy=FACTORIZATION_POLICY,
        complete_affine_policy=POLICY,
        complete_affine_model_definition=model_definition(),
        algorithm_stage_scope={
            'original_primary_rebuilds_restored_unit_normals_at_current_center':True,
            'new_same_failed_y_SOC_rebinds_expanded_original_pool_at_same_x':True,
            'old_numeric_cut_A_b_are_never_carried':True,
            'same_exact159_physical_coordinates_same163_state_g_b0_and_height_H':True,
            'full_reference163_and_coordinate_metadata_preserved':True,
            'full_source_terminal_coarse_and_fine_pool_ID_lists_preserved':True,
            'source_configuration_preserved_for_exact_factorization_and_bank_hash':True,
            'inherited_source_configuration_scope_labels_are_historical_metadata':True,
            'source_bank_replay_requires_exact_first_binding_hash':True,
            'all_original_complete_value_gates_and_thresholds_unchanged':True,
            'source_controller_radius_and_streak_read_without_reset':True,
            'all_new_work_uses_original12_LP40_value120_second_active_caps':True,
            'no_old_optimizer_or_old_developer_suite_executed':True},
        new_stage_call_counter_semantics='zero old optimizer calls; one new expanded-pool same-trial SOC driver',
        direct_transfer=copy.deepcopy(replay['source_completed_log_transfer']))
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
    save('complete-exact-checkpoint-transfer-before-new-geometry')
    try:
        initial_audit_started=time.monotonic()
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='height159-complete-affine-complete-initialization'
        def checkpoint(snapshot):
            report[STAGE]={'status':'current159-last-qualified-checkpoint','checkpoint':snapshot,'solver':{}}
            save('complete-affine-last-accepted-physical-checkpoint')
        objective=ExpandedPoolSOCObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint,
            radial_nodes_exact=grid['radial_nodes_exact'],initial_direction_records=replay['initial_direction_records'],
            expected_initial_bank_state_sha256=replay['expected_initial_bank_state_sha256'],
            expected_initial_bank_entries=replay['expected_initial_bank_entries'],
            expanded_pool_policy=POLICY)
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            direct_completed_source_transfer=replay['source_completed_log_transfer'],
            complete_checkpoint_pool_transfer=replay['learned_pool'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'complete-source-checkpoint-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'complete-source-checkpoint-fine-original-IDs','source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_computed_field(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        report['initial_field_diagnostics']={g.label:field_diagnostics(d,g,subspace,cfg) for g,d in
            [(objective.row_grids[0],objective.geometry_cache),(objective.row_grids[1],objective.fine_cache['data'])]}
        old_decisions = replay["original_report"]
        report["same_exact_state_initial_value_comparison"] = {}
        for label, old_key, new_key in (
                ("coarse","final_full_grid_constraints","initial_current_constraints"),
                ("fine","final_doubled_constraints","initial_doubled_constraints")):
            old, new = old_decisions[old_key], report[new_key]
            fields = ("direct_max_eta", "direct_maximum_absolute_principal_curvature")
            differences = {key: float(new[key])-float(old[key]) for key in fields}
            if max(abs(x) for x in differences.values()) > 5e-10:
                raise ArithmeticError("exact physical transfer changed original complete-grid values")
            if not new["single_grid_admissible_recovery_point"]:
                raise ArithmeticError("transferred original exact point lost original actual eligibility")
            report["same_exact_state_initial_value_comparison"][label] = differences
        save('complete-initial-original-gates-exact-height-map-and-current-height-diagnostics')
        report['timing_segments']['initial_ordinary_audit_before_recovery_wall_seconds']=time.monotonic()-initial_audit_started
        report['phase']='one-shared-budget-expanded-pool-same-trial-SOC-stage';report['new_scientific_solver_calls']=1
        recovery_started=time.monotonic()
        # Explicit new outer changes the failed full-primary expansion branch only.
        stage=run_expanded_pool_soc_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            restored_controller=replay['controller_continuation'],artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['timing_segments']['recovery_wall_seconds_including_pre_active_first_J']=time.monotonic()-recovery_started
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
        report["future_direct_checkpoint"] = {
            "reference_complete163_binary64_exact": [
                str(Q.from_float(float(x))) for x in problem.coordinates.reference_state],
            "coordinate_definition": copy.deepcopy(problem.coordinate_definition),
            "selected_final159_binary64_exact": coefficients(final),
            "selected_final163_physical_exact": [str(x) for x in problem.coordinates.physical_exact(final)],
            "selected_physical_state_sha256": digest(problem.identity(final)),
            "coarse_pool": copy.deepcopy(stage["checkpoint"]["active_row_pool_history"][-1]["row_indices"]),
            "fine_pool": copy.deepcopy(stage["checkpoint"]["fine_physical_row_pool_history"][-1]["row_indices"]),
            "terminal_trust": stage["last_restricted_trust"],
            "terminal_success_streak": stage["final_consecutive_growth_qualifying_models"],
            "norm_direction_bank_context": copy.deepcopy(objective.direction_bank.context),
            "norm_direction_bank_entries": copy.deepcopy(list(objective.direction_bank.entries.values())),
            "norm_direction_bank_state_sha256": objective.direction_bank.state_digest(),
            "all_values_are_original_completed_runner_output_not_committed_payload": True}
        reference=objective.restricted_reference;grids=objective.row_grids
        report['phase']='independent-final-same-exact-state-original384-and768-values'
        final_coarse_started=time.monotonic()
        work=problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit']=audit_computed_field(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints']=recovery_decision(problem,gate,final,work,lower,upper,cfg)
        report['final_field_diagnostics']={'coarse':field_diagnostics(work,grids[0],subspace,cfg)}
        report['final_fixed_support_replay']={
            'exact_total_cap_integral_change':report['final_exact_height_diagnostic']['exact_total_cap_integral_change'],
            'physical_height_c4_c5_exactly_unchanged':report['final_exact_height_diagnostic']['physical_c4_c5_exactly_unchanged'],
            'coarse':outside_replay(reference,subspace,grids[0],work)}
        report['timing_segments']['final_coarse_geometry_audit_and_support_seconds']=time.monotonic()-final_coarse_started
        save('last159-qualified-point-recomputed-on-original-coarse-grid')
        del objective
        fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
        final_fine_started=time.monotonic()
        fine=problem.geometry(final,radial,fine_theta,order)
        report['final_doubled_angle_audit']=audit_computed_field(problem,final,fine,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints']=recovery_decision(problem,gate,final,fine,lower,upper,cfg)
        report['final_field_diagnostics']['fine']=field_diagnostics(fine,grids[1],subspace,cfg)
        report['final_fixed_support_replay']['fine']=outside_replay(reference,subspace,grids[1],fine)
        report['timing_segments']['final_fine_geometry_audit_and_support_seconds']=time.monotonic()-final_fine_started
        final_comparison_started=time.monotonic()
        report['same_parameter_Pi_refinement']=compare_computed_fields(problem,work,fine,final)
        report['timing_segments']['final_two_grid_comparison_seconds']=time.monotonic()-final_comparison_started
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
            'old_optimizer_calls_this_run':0,
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
            'nine_old_optimizers_are_not_rerun':True,'no_forced_observed_prefix_hash':True}
        save('height159-complete-affine-controller-error-last-qualified-preserved' if stage.get('error') else
            COMPLETE if eligible else 'final-recheck-failed-do-not-use-as-new-warm-start')
        print_new_stage_outcomes(report)
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('height159-complete-affine-audit-error-last-checkpoint-preserved');print_new_stage_outcomes(report);return report




def main():
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    request = json.loads(args.request.read_text())
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != transfer.REPO:
        raise RuntimeError("all new checks and research require the public repository Actions")
    for path, expected in request["source_sha256"].items():
        if hashlib.sha256(Path(path).read_bytes()).hexdigest() != expected:
            raise RuntimeError("requested source differs: "+path)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    previous = request["reuse_completed_norm_memory"]
    current = previous_audit.implementation_hashes()
    if current != previous["source_files_sha256"]:
        raise RuntimeError("a completed norm-memory dependency changed")
    emit("EXPANDED_SOC_PRIOR_WORK_REUSED", {
        "original_run_id": previous["run_id"], "original_job_id": previous["job_id"],
        "original_source_commit": previous["source_commit"],
        "unchanged_dependencies": len(current),
        "previous_norm_development_passed_checks": 12,
        "previous_completed_scientific_stage_not_reexecuted": True,
        "old_development_executions": 0, "old_optimizer_executions": 0})
    import frame_metric_expanded_pool_soc_development as development
    check = development.developer_check()
    check["source_files_sha256"] = implementation_hashes()
    emit("EXPANDED_SOC_DEVELOPMENT", check)
    if not check.get("passed"):
        raise RuntimeError("new expanded-pool same-trial interface checks failed")
    try:
        prepared = transfer.prepare_transfer(request,
            args.out.parent/"original24-input-preparation-failure.json", started)
        report = run_audit(prepared, args.out, process_started=started,
                           prepare_seconds=time.monotonic()-started)
    except Exception as error:
        report = {"schema":SCHEMA, "status":"complete-checkpoint-transfer-failed-before-new-driver-completion",
            "source_files_sha256":implementation_hashes(), "old_optimizer_calls_this_run":0,
            "error":{"type":type(error).__name__, "message":str(error), "traceback":traceback.format_exc()},
            "process_total_elapsed_seconds":time.monotonic()-started}
        atomic_save(args.out, report)
        emit("EXPANDED_SOC_TRANSFER_ERROR", report)
        raise
    if report.get("status") != COMPLETE:
        raise RuntimeError("expanded-pool SOC run did not finish with both original value grids eligible")


if __name__ == "__main__":
    main()

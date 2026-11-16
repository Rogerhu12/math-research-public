#!/usr/bin/env python3
"""Public finite-cone task: one latest source read, new interfaces, real new method."""
from __future__ import annotations
import time
PROCESS_STARTED = time.monotonic()
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import traceback
import numpy as np
from frame_collar_bvp import atomic_save
from frame_height_null_coordinates import digest
from frame_curvature_soc_metric_reserve_audit import exact_vector
from frame_metric_budget_recovery import require_public_research_environment
import frame_metric_terminal_paid_slot_audit as paid_audit
import frame_metric_direct_reference_audit as original_audit
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader
from frame_metric_finite_cone_primary import POLICY
from frame_metric_finite_cone_epoch import (
    FiniteConeObjective, LIMITS, MAX_CONES_PER_MODEL, SETTINGS, CANDIDATE_STATUSES,
    SOURCE_SCIENCE_SECONDS, SOURCE_VALUES, SOURCE_LEGACY_COUNTS, definition)
from frame_metric_finite_cone_recovery import run_finite_cone_recovery
import frame_metric_finite_cone_transfer as transfer

SCHEMA = POLICY+"-audit"
STAGE = "finite_cone_primary_stage"
COMPLETE = "complete-two-grid-finite-cone-primary-audit"
TAG = "FINITE_CONE_"
NEW_SOURCES = (
    "frame_metric_finite_cone_primary.py", "frame_metric_finite_cone_epoch.py",
    "frame_metric_finite_cone_recovery.py", "frame_metric_finite_cone_transfer.py",
    "frame_metric_finite_cone_development.py", "frame_metric_finite_cone_audit.py")


def implementation_hashes():
    result = paid_audit.implementation_hashes()
    folder = Path(__file__).parent
    for name in NEW_SOURCES:
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def emit(suffix, value):
    print(TAG+suffix+" "+reader.encoded(value).decode("utf-8"), flush=True)


def metadata(value):
    raw = reader.encoded(value)
    return {"canonical_JSON_bytes": len(raw), "canonical_JSON_sha256": reader.digest(raw),
            "count": len(value) if isinstance(value, (list, dict)) else None}


def support_receipt(value):
    result = copy.deepcopy(value)
    for key in ("inherited_bank_record", "supplemental_original_rows",
                "source_manifest", "terminal_prepared_support_provenance"):
        if key in result:
            result[key+"_metadata"] = metadata(result.pop(key))
    return result


def oracle_semantic(value):
    result = copy.deepcopy(value)
    if "binding" in result:
        result["binding_metadata"] = metadata(result.pop("binding"))
    # Direction events, all actual four attainers, timing and original-row/J
    # events are new evidence. No whole-tree scalar compaction is applied.
    return result


def cone_call_semantic(value):
    result = copy.deepcopy(value)
    assembly = result.get("assembly")
    if isinstance(assembly, dict):
        for key in ("original_cone_tags", "row_sources"):
            if key in assembly:
                assembly[key+"_metadata"] = metadata(assembly.pop(key))
        if "retained_support_receipt" in assembly:
            assembly["retained_support_receipt"] = support_receipt(assembly["retained_support_receipt"])
    # In particular: new_candidate_step_record exact159 stays byte-for-byte
    # as stored by the adapter, including rejected-status and raised calls.
    return result


def capture_evidence(models):
    """Only inspect original records; never infer a saved vector from a status."""
    events = [event for model in models
              for event in model.get("linear_program", {}).get("cone_calls", [])]
    finite = [event for event in events if event.get("finite_original161_vector") is True]
    def actual_exact159(event):
        record = event.get("new_candidate_step_record")
        vector = record.get("exact_binary64_independent_step") if isinstance(record, dict) else None
        return isinstance(vector, list) and len(vector) == 159 and all(isinstance(x, str) for x in vector)
    trials = [trial for model in models for trial in model.get("trials", [])]
    def actual_trial_vectors(trial):
        independent = trial.get("exact_binary64_independent_coordinates")
        physical = trial.get("exact_original_physical_coefficients")
        return (isinstance(independent, list) and len(independent) == 159
                and isinstance(physical, list) and len(physical) == 163
                and all(isinstance(x, str) for x in independent+physical))
    return {
        "started_cone_event_records": len(events),
        "actual_finite_return_records": len(finite),
        "finite_returns_with_exact159_list": sum(actual_exact159(e) for e in finite),
        "all_finite_return_exact159_lists_present": (
            all(actual_exact159(e) for e in finite) if finite else None),
        "actual_trial_records": len(trials),
        "trials_with_exact159_and_physical163_lists": sum(actual_trial_vectors(t) for t in trials),
        "all_actual_trial_coordinate_lists_present": (
            all(actual_trial_vectors(t) for t in trials) if trials else None),
        "none_means_no_actual_return_or_trial_not_a_claim_of_saved_execution": True,
        "record_existence_and_length_only_no_vector_reconstruction": True}


def semantic_model(model):
    result = {k: copy.deepcopy(v) for k, v in model.items()
              if k not in ("linear_program", "complete_model")}
    lp = model.get("linear_program", {})
    result["finite_cone_primary"] = {
        k: copy.deepcopy(v) for k, v in lp.items()
        if k not in ("model", "cone_calls", "retained_support_bundle",
                     "complete_original_grid_model")}
    result["finite_cone_primary"]["cone_calls"] = [
        cone_call_semantic(v) for v in lp.get("cone_calls", [])]
    if "model" in lp:
        summary = copy.deepcopy(lp["model"])
        if "binding" in summary:
            summary["binding_metadata"] = metadata(summary.pop("binding"))
        result["finite_cone_primary"]["model_summary"] = summary
    if "retained_support_bundle" in lp:
        result["finite_cone_primary"]["retained_support_bundle"] = support_receipt(lp["retained_support_bundle"])
    complete = model.get("complete_model", {})
    result["complete_oracle"] = oracle_semantic(complete.get("oracle", {}))
    result["complete_model_metadata"] = metadata(complete)
    # Full new trial159/163, fourteen gates, learning and actual quality remain.
    evidence = capture_evidence([model])
    result["actual_capture_evidence"] = evidence
    result["serialization_scope"] = {
        "all_actual_solver_finite_exact159_vectors_retained": evidence["all_finite_return_exact159_lists_present"],
        "all_actual_trial159_and_physical163_vectors_retained": evidence["all_actual_trial_coordinate_lists_present"],
        "new_original_cone_expansion_tags_retained": True,
        "repeated_initial_cone_tags_and_bank_rebuild_details_are_metadata_only": True,
        "current_full_pools_and_all_retained_supports_in_COMPLETE_future_checkpoint": True,
        "no_dense_numeric_A_or_J_output": True}
    return result


def summary(report):
    result = {k: copy.deepcopy(v) for k, v in report.items() if k not in (
        STAGE, "exact_input_storage", "scientific_started_monotonic")}
    result["exact_input_storage_metadata"] = metadata(report.get("exact_input_storage", {}))
    stage = report.get(STAGE, {})
    result[STAGE] = {k: copy.deepcopy(v) for k, v in stage.items()
                    if k not in ("checkpoint", "solver", "complete_original_grid_oracle_progress",
                                 "curvature_defect_guard_learning_checkpoint",
                                 "inherited_guard_observation_full_history",
                                 "cross_center_norm_memory")}
    solver = stage.get("solver", {})
    result[STAGE]["solver"] = {k: copy.deepcopy(v) for k, v in solver.items() if k != "models"}
    result[STAGE]["model_count"] = len(solver.get("models", []))
    result[STAGE]["MODEL_record_metadata"] = [
        dict(number=m["number"], **metadata(semantic_model(m)))
        for m in solver.get("models", [])]
    snapshot = stage.get("checkpoint", {})
    result[STAGE]["selected_two_grid_physical_point"] = copy.deepcopy(
        snapshot.get("selected_two_grid_physical_point"))
    result[STAGE]["snapshot_scalar_counters"] = {
        k: copy.deepcopy(snapshot[k]) for k in (
            "initialization_elapsed_seconds", "optimization_elapsed_seconds",
            "value_geometry_seconds", "total_full_value_physical_evaluations",
            "coarse_physical_evaluations", "fine_physical_evaluations",
            "doubled_angle_value_seconds") if k in snapshot}
    result["factorized_selected_J_execution"] = copy.deepcopy(
        snapshot.get("selected_row_factorization_statistics"))
    result["complete_original_grid_oracle_progress"] = [
        {k: (metadata(v) if k in ("binding", "direction_events", "new_original_row_J_events")
             else copy.deepcopy(v)) for k, v in item.items()}
        for item in stage.get("complete_original_grid_oracle_progress", [])]
    bank = stage.get("cross_center_norm_memory", {})
    result["terminal_bank_scalar_report"] = {
        k: (metadata(v) if k == "rebuild_events" else copy.deepcopy(v)) for k, v in bank.items()}
    evidence = capture_evidence(solver.get("models", []))
    result["actual_capture_evidence"] = evidence
    result["serialization_scope"] = {
        "models_emitted_once_under_FINITE_CONE_MODEL": True,
        "every_finite_cone_return_exact159_is_in_its_MODEL_including_filtered_returns":
            evidence["all_finite_return_exact159_lists_present"],
        "COMPLETE_keeps_full_recoverable_checkpoint_without_repeating_models": True,
        "no_global_length_filter_is_applied_to_any_step_or_trial_vector": True,
        "all_scientific_payloads_stay_in_runner_stdout_or_temporary_files": True}
    return result


def save_report(output, report):
    now = time.monotonic()
    report["process_total_elapsed_seconds"] = now-PROCESS_STARTED
    start = report.get("scientific_started_monotonic")
    if start is not None:
        report["new_scientific_elapsed_seconds_including_input_prepare"] = now-start
        report["cumulative_original_scientific_seconds"] = SOURCE_SCIENCE_SECONDS+(now-start)
    report["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    atomic_save(output, report)
    atomic_save(Path(output).with_name("finite-cone-primary-audit-summary.json"), summary(report))


def final_receipts(stage, point, replay):
    if point["accepted_index"] == 27:
        transfer.require(point["physical_state_sha256"] == transfer.IDENTITIES["physical"],
                         "unchanged paid index27 has another physical identity")
        return (copy.deepcopy(replay["source_final_gate_receipts"]["coarse"]),
                copy.deepcopy(replay["source_final_gate_receipts"]["fine"]),
                {"kind": "unchanged-exact-source-point-original-complete14-gate-receipts",
                 "accepted_index": 27, "new_initial_restoration_receipts_recorded_separately": True,
                 "not_a_new_independent_final_audit": True})
    matches = [(m, i, t) for m in stage["solver"]["models"]
               for i, t in enumerate(m.get("trials", []))
               if t.get("accepted_as_next_iterate") is True
               and t.get("accepted_index") == point["accepted_index"]
               and t.get("physical_state_sha256") == point["physical_state_sha256"]]
    transfer.require(len(matches) == 1 and point["accepted_index"] > 27,
                     "one actual new trial must own the selected acceptance")
    model, index, trial = matches[0]
    return (copy.deepcopy(trial["coarse_decision"]), copy.deepcopy(trial["fine_decision"]),
            {"kind": "new-finite-cone-ordinary-full-two-grid-accepted-trial",
             "accepted_index": point["accepted_index"], "model_number": model["number"],
             "trial_index": index, "physical_state_sha256": point["physical_state_sha256"]})


def future_checkpoint(objective, problem, point, stage):
    replay = objective.finite_cone_replay
    return {
        "schema": POLICY+"-future-checkpoint",
        "reference_complete163_binary64_exact": [
            str(Q.from_float(float(x))) for x in problem.coordinates.reference_state],
        "coordinate_definition": copy.deepcopy(problem.coordinate_definition),
        "selected_accepted_index": point["accepted_index"],
        "selected_final159_binary64_exact": copy.deepcopy(point["exact_binary64_independent_coordinates"]),
        "selected_final163_physical_exact": copy.deepcopy(point["exact_original_physical_coefficients"]),
        "selected_physical_state_sha256": point["physical_state_sha256"],
        "selected_two_grid_physical_point": copy.deepcopy(point),
        "coarse_pool": objective.pool.tolist(), "fine_pool": objective.fine_pool.tolist(),
        "coarse_pool_version": objective.pool_version, "fine_pool_version": objective.fine_pool_version,
        "coarse_pool_history": copy.deepcopy(objective.pool_history),
        "fine_pool_history": copy.deepcopy(objective.fine_pool_history),
        "terminal_trust": stage["last_restricted_trust"],
        "terminal_success_streak": stage["final_consecutive_growth_qualifying_models"],
        "terminal_covered_ordinary_growth_streak": stage["final_covered_ordinary_growth_streak"],
        "configuration": copy.deepcopy(objective.cfg),
        "objective_evaluation_definition": copy.deepcopy(objective.evaluation_definition),
        "objective_evaluation_sha256": objective.evaluation_sha256,
        "ordinary_field_evaluation_definition": copy.deepcopy(problem.evaluation_definition()),
        "ordinary_field_evaluation_sha256": objective.factorized.ordinary_evaluation_sha256,
        "factorization_definition": copy.deepcopy(objective.factorized.definition),
        "factorization_definition_sha256": objective.factorized.definition_sha256,
        "norm_direction_bank_context": copy.deepcopy(objective.direction_bank.context),
        "norm_direction_bank_entries": copy.deepcopy(list(objective.direction_bank.entries.values())),
        "norm_direction_bank_state_sha256": objective.direction_bank.state_digest(),
        "norm_direction_bank_counters": {
            "insertions": objective.direction_bank.insertions,
            "evictions": objective.direction_bank.evictions,
            "normal_inward_binary64_adjustments": objective.direction_bank.rounding_adjustments},
        "all_retained_supplemental_normals": copy.deepcopy(objective.supplemental_normals),
        "retained_support_source_manifest": copy.deepcopy(objective.support_source_manifest),
        "curvature_defect_guard_learning_checkpoint": objective.curvature_defect_memory.checkpoint(),
        "closed_original_HiGHS_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
        "finite_cone_new_task_account": objective.cone_ledger.report(),
        "cumulative_original_actual_values": objective.full_value_evaluations,
        "new_finite_cone_actual_values": objective.full_value_evaluations-SOURCE_VALUES,
        "new_finite_cone_scientific_elapsed_seconds_at_checkpoint":
            time.monotonic()-objective.scientific_started,
        "cumulative_original_scientific_elapsed_seconds_at_checkpoint":
            time.monotonic()-objective.global_scientific_started,
        "final_COMPLETE_clock_is_later_and_authoritative_for_next_resume": True,
        "ancestor_cost_receipt": copy.deepcopy(replay["ancestor_cost_receipt"]),
        "current_source_point27_plus_new_acceptances_scope": True,
        "no_claim_of_recovering_unpublished_old_rejected_step": True,
        "actual_solver_and_trial_capture_evidence": capture_evidence(stage["solver"].get("models", [])),
        "all_finite_solver_exact159_records_are_in_the_native_MODEL_records":
            capture_evidence(stage["solver"].get("models", []))["all_finite_return_exact159_lists_present"],
        "arrays_only_in_runner_stdout_or_temporary_files": True}


def run_audit(prepared, output, *, scientific_started, segments, development_receipt, report_sink):
    # The caller keeps this same object if a final save/emit raises after science.
    report = report_sink
    restored, bindings, tenth, replay, coarse_pool, fine_pool = prepared
    problem, initial, gate, lower, upper, cfg = restored
    report.update({
        "schema": SCHEMA, "status": "finite-cone-not-yet-constructed",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "source_files_sha256": implementation_hashes(),
        "configuration": copy.deepcopy(cfg), "policy_definition": definition(),
        "scientific_started_monotonic": scientific_started,
        "timing_segments": copy.deepcopy(segments),
        "development_receipt": copy.deepcopy(development_receipt),
        "paid_source_receipt": copy.deepcopy(replay["paid_evidence"]),
        "source_transfer": copy.deepcopy(replay["source_completed_log_transfer"]),
        "exact_input_storage": bindings,
        "ancestor_cost_receipt": copy.deepcopy(replay["ancestor_cost_receipt"]),
        "source_current_physical_state_sha256": transfer.IDENTITIES["physical"],
        "source_current_accepted_index": 27,
        "closed_original_HiGHS_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
        "source_original_actual_values": SOURCE_VALUES,
        "source_final_original_scientific_seconds": SOURCE_SCIENCE_SECONDS,
        "new_limits": copy.deepcopy(LIMITS),
        "original_global_caps": {"science_seconds": 1800, "actual_values": 160},
        "new_recovery_entries": 0, "new_independent_final_geometry_calls": 0,
        "old_developer_optimizer_LP_geometry_JVP_or_trial_replays": 0,
        "new_legacy_LP_and_SOC_calls_authorized": 0,
        "limitations": {
            "backend_status_is_not_actual_feasibility_or_stationarity": True,
            "finite_grid_pass_not_continuous_isometry_or_reach_certificate": True,
            "empirical_curvature_guard_is_not_a_proved_cross_center_error_bound": True,
            "old64_calls_closed_not_relabelled_or_repeated": True,
            "new_budget_does_not_promise_improvement": True}})
    objective = None
    constructor_started = time.monotonic()
    try:
        transfer.check_clock(scientific_started)
        radial, theta, grid = baseline.curvature_grid(tenth)
        report["full_value_sampling_definition"] = copy.deepcopy(grid)
        bounded = problem.original_problem.base
        order = int(bounded.primitive_order)
        transfer.require(order == 8 and order == int(bounded.fixed_primitive.order),
                         "the authoritative original query/fixed primitive order differs")
        gate, gate_receipt = original_audit.fresh_adapter_gate(gate, problem, initial, lower, upper)
        report["fresh_adapter_original_physical_gate_binding"] = gate_receipt
        report["original_query_quadrature_order"] = {
            "value": order, "source": "problem.original_problem.base.primitive_order",
            "same_fixed_primitive_order": True}
        def checkpoint(snapshot):
            report[STAGE] = {"status": "last-actual-qualified-checkpoint",
                             "checkpoint": snapshot, "solver": {}}
            save_report(output, report)
        objective = FiniteConeObjective(
            problem, gate, radial, theta, order, lower, upper,
            cfg=cfg, checkpoint=checkpoint, radial_nodes_exact=grid["radial_nodes_exact"],
            replay=replay, scientific_started=scientific_started,
            finite_cone_policy=POLICY, limits=requested_limits(report),
            coarse_pool=coarse_pool, fine_pool=fine_pool)
        report["timing_segments"]["finite_cone_constructor_seconds"] = time.monotonic()-constructor_started
        report["actual_new_and_source_definition_hashes"] = {
            "source_objective": transfer.IDENTITIES["objective"],
            "new_objective": objective.evaluation_sha256,
            "same_ordinary_field": objective.factorized.ordinary_evaluation_sha256,
            "same_factorization": objective.factorized.definition_sha256,
            "same_configuration": digest(objective.cfg)}
        report["new_recovery_entries"] = 1
        started = time.monotonic()
        stage = run_finite_cone_recovery(
            objective, initial, restored_controller=replay["controller_continuation"])
        report[STAGE] = stage
        report["timing_segments"]["finite_cone_restoration_and_outer_seconds"] = time.monotonic()-started
        point = stage["checkpoint"].get("selected_two_grid_physical_point")
        transfer.require(point is not None, "the paid exact accepted point must remain available")
        final = exact_vector(point["exact_binary64_independent_coordinates"], 159)
        transfer.require(np.array_equal(final, np.asarray(point["independent_coordinates_binary64"], float))
            and [str(x) for x in problem.coordinates.physical_exact(final)] ==
                point["exact_original_physical_coefficients"]
            and digest(problem.identity(final)) == point["physical_state_sha256"],
            "selected exact159/physical163/identity differs")
        box = problem.coordinates.exact_box_decision(final, gate.original_lower, gate.original_upper)
        transfer.require(box["exact_original_box_pass"] is True, "the exact original163 box failed")
        copied, copied_state = problem.frozen_metric_copy(final)
        transfer.require(copied is problem and copied_state.tobytes() == final.tobytes()
                         and copied.identity(copied_state) == problem.identity(final)
                         and copied.metric_model(copied_state) == problem.metric_model(initial)
                         and copied.height_base_definition == problem.height_base_definition,
                         "the frozen g/b0/reference/map changed")
        coarse, fine, owner = final_receipts(stage, point, replay)
        flags = {label: value["actual_gate_booleans"]
                 for label, value in (("coarse", coarse), ("fine", fine))}
        transfer.require(all(len(v) == 14 and all(x is True for x in v.values()) for v in flags.values()),
                         "selected point lacks a complete original fourteen-gate receipt")
        transfer.require(all(value["direct_max_eta"] == point[label]["direct_max_eta"]
                             for label, value in (("coarse", coarse), ("fine", fine))),
                         "final gate receipts and selected scalar identity differ")
        maximum = max(coarse["direct_max_eta"], fine["direct_max_eta"])
        report["final_selection_validation"] = {
            "both_value_grids_hard_and_old_metric_pass": True,
            "exact_original_box_pass": True,
            "source_both_grid_maximum_eta": replay["source_current_point"]["maximum_eta_on_both_grids"],
            "both_grid_maximum_eta": maximum,
            "both_grid_maximum_curvature": max(coarse["direct_maximum_absolute_principal_curvature"],
                                               fine["direct_maximum_absolute_principal_curvature"]),
            "actual_eta_decrease": replay["source_current_point"]["maximum_eta_on_both_grids"]-maximum,
            "new_metric_target_qualified_on_both_grids": point["new_metric_target_qualified_on_both_grids"],
            "accepted_index": point["accepted_index"],
            "not_a_new_independent_final_geometry_audit": True}
        report["final_full_grid_constraints"], report["final_doubled_constraints"] = coarse, fine
        report["final_actual_gate_booleans"], report["selected_gate_receipt_source"] = flags, owner
        report["final_exact_box"] = box
        report["future_finite_cone_checkpoint"] = future_checkpoint(objective, problem, point, stage)
        report["terminal_bank_pools_and_learning"] = {
            "bank_entries": len(objective.direction_bank.entries),
            "bank_state_sha256": objective.direction_bank.state_digest(),
            "supplemental_rows": len(objective.supplemental_normals),
            "pool_counts": [len(objective.pool), len(objective.fine_pool)],
            "pool_versions": [objective.pool_version, objective.fine_pool_version],
            "learning_state_sha256": objective.curvature_defect_memory.state_record()["state_sha256"],
            "learning_events": len(objective.curvature_defect_memory.events),
            "learning_commits": len(objective.curvature_defect_memory.commits),
            "learning_pending": len(objective.curvature_defect_memory.pending),
            "last_trust": stage["last_restricted_trust"],
            "last_legacy_streak": stage["final_consecutive_growth_qualifying_models"],
            "last_covered_streak": stage["final_covered_ordinary_growth_streak"]}
        report["status"] = COMPLETE if not stage.get("error") else "finite-cone-stage-error-best-retained"
    except Exception as error:
        report["status"] = "finite-cone-audit-error"
        report["error"] = {"type": type(error).__name__, "message": str(error),
                           "traceback": traceback.format_exc()}
        if objective is not None:
            report.setdefault(STAGE, {"solver": {}})
            report[STAGE]["checkpoint"] = objective.snapshot()
    if objective is not None:
        report["direct_reference_geometry_timing"] = objective.problem.timing_snapshot()
        report["final_new_task_solver_account"] = objective.cone_ledger.report()
        report["final_value_account"] = {
            "source_values": SOURCE_VALUES,
            "new_values": objective.full_value_evaluations-SOURCE_VALUES,
            "cumulative_original_values": objective.full_value_evaluations,
            "coarse_cumulative": objective.geometry_evaluations,
            "fine_cumulative": objective.fine_evaluations,
            "new_limit": LIMITS["max_new_actual_values"], "original_global_limit": 160,
            "new_independent_final_values": 0}
    save_report(output, report)
    emit_result(report)
    return report


def requested_limits(report):
    transfer.require(report["new_limits"] == LIMITS, "reviewed new limits differ")
    return copy.deepcopy(report["new_limits"])


def emit_result(report):
    for model in report.get(STAGE, {}).get("solver", {}).get("models", []):
        emit("MODEL", semantic_model(model))
    emit("COMPLETE", summary(report))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    require_public_research_environment()
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    raw_request = Path(args.request).read_bytes()
    request = json.loads(raw_request)
    scientific_started = None
    development_receipt = None
    development_started = development_seconds = None
    audit_entered = False
    audit_report_sink = {}
    try:
        parameters = request["parameters"]
        transfer.require(parameters["policy"] == POLICY
            and parameters["new_scientific_seconds_limit"] == parameters["limits"]["max_scientific_seconds"]
            and parameters["limits"] == LIMITS
            and parameters["max_cone_calls_per_model"] == MAX_CONES_PER_MODEL
            and parameters["settings"] == SETTINGS
            and parameters["allowed_candidate_statuses"] == list(CANDIDATE_STATUSES)
            and parameters["SOC_reservation_policy"] == "none; no legacy/SOC calls authorized",
            "the explicit new finite-cone resource/status/settings contract differs")
        transfer.require(all(type(parameters["limits"][k]) is int for k in (
            "max_new_solver_calls", "max_new_cone_calls",
            "max_new_legacy_LP_calls", "max_new_actual_values"))
            and transfer.finite_number(parameters["new_scientific_seconds_limit"])
            and transfer.finite_number(parameters["limits"]["max_single_solver_seconds"]),
            "new integer count limits and finite budget aliases required")
        for path, expected in request["source_sha256"].items():
            transfer.require(reader.digest(Path(path).read_bytes()) == expected,
                             "requested source changed: "+path)
        requested_python = {Path(p).name: sha for p, sha in request["source_sha256"].items() if p.endswith(".py")}
        transfer.require(requested_python == implementation_hashes() and len(requested_python) == 164,
                         "old158 plus exactly six new Python sources required")
        emit("REQUEST", {"source_commit": os.environ.get("GITHUB_SHA"),
            "request_bytes": len(raw_request), "request_sha256": reader.digest(raw_request),
            "source_sha256": request["source_sha256"], "parameters": parameters})
        # Only the three new interfaces run. The old eleven/nine receipts are
        # read transitively from the one latest source log after this phase.
        development_started = time.monotonic()
        from frame_metric_finite_cone_development import developer_check
        development_receipt = developer_check()
        development_seconds = time.monotonic()-development_started
        emit("DEVELOPMENT", development_receipt)
        transfer.require(development_receipt["all_passed"] is True
                         and development_receipt["executed_check_count"] == 12,
                         "new finite-cone interface development did not all pass")
        scientific_started = time.monotonic()
        source_started = time.monotonic()
        completed = transfer.read_completed(request, scientific_started=scientific_started)
        source_seconds = time.monotonic()-source_started
        emit("PRIOR_WORK_REUSED", completed["receipt"])
        input_started = time.monotonic()
        prepared = transfer.prepare_transfer(
            request, output, PROCESS_STARTED, completed=completed,
            scientific_started=scientific_started)
        segments = {
            "source_latest_log_read_and_validation_seconds": source_seconds,
            "necessary24_original_inputs_and_immutable_prepare_seconds": time.monotonic()-input_started,
            "new_scientific_input_prepare_seconds": time.monotonic()-scientific_started,
            "new_development_elapsed_seconds_separate_from_science": development_seconds,
            "new_development_groups": 3, "new_development_checks": 12,
            "old11_and9_development_executions": 0,
            "process_import_and_development_before_science_seconds": scientific_started-PROCESS_STARTED,
            "paid_source356_seconds_not_replayed_and_added_once_only": True}
        audit_entered = True
        result = run_audit(prepared, output, scientific_started=scientific_started,
                           segments=segments, development_receipt=development_receipt,
                           report_sink=audit_report_sink)
    except Exception as error:
        if development_started is not None and development_seconds is None:
            development_seconds = time.monotonic()-development_started
        failure = {"type": type(error).__name__, "message": str(error),
                   "traceback": traceback.format_exc()}
        if audit_entered:
            # No zero-call claim or new empty stage may overwrite real work.
            result = audit_report_sink
            result.setdefault("schema", SCHEMA)
            result.setdefault("scientific_started_monotonic", scientific_started)
            result["status"] = "finite-cone-post-entry-reporting-error"
            result["post_entry_reporting_error"] = failure
            result["actual_stage_and_solver_accounts_preserved_from_shared_report"] = True
        else:
            result = {
                "schema": SCHEMA, "status": "finite-cone-input-or-development-error",
                "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
                "github_repository": os.environ.get("GITHUB_REPOSITORY"),
                "source_files_sha256": implementation_hashes(),
                "development_receipt": copy.deepcopy(development_receipt),
                "scientific_started_monotonic": scientific_started,
                "source_final_original_scientific_seconds": SOURCE_SCIENCE_SECONDS,
                "closed_original_HiGHS_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
                "source_actual_values": SOURCE_VALUES,
                "new_scientific_cone_calls_before_input_ready": 0, "error": failure}
        result.setdefault("timing_segments", {})[
            "new_development_elapsed_seconds_separate_from_science"] = development_seconds
        result["development_started"] = development_started is not None
        save_report(output, result)
        emit_result(result)
    for path in sorted(output.parent.glob("*.json")):
        raw = path.read_bytes()
        emit("OUTPUT_METADATA", {"filename": path.name, "bytes": len(raw),
             "sha256": reader.digest(raw), "payload_repository_artifact_cache_upload": False})
    return 0 if result.get("status") == COMPLETE else 1


if __name__ == "__main__":
    raise SystemExit(main())

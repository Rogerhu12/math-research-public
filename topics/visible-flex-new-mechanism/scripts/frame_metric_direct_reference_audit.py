#!/usr/bin/env python3
"""Public Actions entry for the independent direct-reference scientific task."""
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
from frame_metric_height159_soc_hold import compact_with_all_actual_gates
from frame_metric_direct_reference_epoch import (
    POLICY, RESOURCE_LIMITS, DirectReferenceGuardObjective, definition)
from frame_metric_direct_reference_recovery import run_direct_reference_recovery
import frame_direct_reference_geometry159_development as development
import frame_metric_direct_reference_transfer as transfer
import frame_metric_curvature_defect_guard_audit as original_audit
import frame_metric_paid_attainer_audit as paid_audit
import read_original_actions_log as reader

SCHEMA = POLICY+"-audit"
STAGE = "direct_reference_guarded_task_stage"
COMPLETE = "complete-two-grid-direct-reference-new-task-audit"
NEW_SOURCES = (
    "frame_direct_reference_geometry159.py",
    "frame_direct_reference_geometry159_development.py",
    "frame_metric_direct_reference_epoch.py",
    "frame_metric_direct_reference_recovery.py",
    "frame_metric_direct_reference_transfer.py",
    "frame_metric_direct_reference_audit.py")
TAG = "DIRECT_REFERENCE_"


def implementation_hashes():
    result = paid_audit.implementation_hashes()
    folder = Path(__file__).parent
    for name in NEW_SOURCES:
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def emit(suffix, value):
    print(TAG+suffix+" "+reader.encoded(value).decode("utf-8"), flush=True)


def omitted(value, reason):
    encoded = reader.encoded(value)
    return {"omitted_from_human_log": reason, "canonical_JSON_bytes": len(encoded),
            "canonical_JSON_sha256": reader.digest(encoded),
            "count": len(value) if isinstance(value, (list, dict)) else None}


def compact_metadata(value, key=""):
    """Copy original small values; never reconstruct geometry or a model."""
    if isinstance(value, dict):
        if "source" in key.lower() and "sha256" in key.lower() and len(value) > 12:
            return omitted(value, "repeated complete source map; the REQUEST carries the full binding")
        return {k: compact_metadata(v, k) for k, v in value.items()}
    if isinstance(value, list):
        if len(value) > 32:
            return omitted(value, "long original list; exact future state is carried once in COMPLETE")
        return [compact_metadata(v, key) for v in value]
    return copy.deepcopy(value)


def semantic_model(model):
    """No denseJ/A and no duplicated bank/pool/history; retain actual decisions."""
    result = {k: compact_metadata(v, k) for k, v in model.items()
              if k not in ("linear_program", "exact_binary64_independent_proposed_step")}
    step = model.get("exact_binary64_independent_proposed_step")
    if step is not None:
        result["proposed_step_fingerprint"] = omitted(step, "old trials are not new input checkpoints")
    lp = model.get("linear_program", {})
    result["linear_program"] = {
        k: compact_metadata(v, k) for k, v in lp.items()
        if k not in ("model", "complete_original_grid_model")}
    complete = lp.get("complete_original_grid_model", {})
    result["complete_model"] = {
        k: compact_metadata(complete[k], k) for k in (
            "schema", "summary", "supplemental_paid_normals",
            "new_support_requests", "new_task_resource_limits")
        if k in complete}
    oracle = complete.get("oracle", {})
    # Exact original paid attainers are small observations needed if a later
    # method uses a rejected/inexact final direction without replaying it.
    result["complete_model"]["oracle"] = {
        k: copy.deepcopy(oracle[k]) for k in (
            "schema", "statistics", "binding", "binding_sha256",
            "direction_events", "new_original_row_J_events")
        if k in oracle}
    bank = complete.get("norm_direction_memory", {})
    result["complete_model"]["norm_direction_memory"] = {
        k: copy.deepcopy(v) for k, v in bank.items() if k != "rebuild_events"}
    result["original_model_fingerprint"] = {
        "canonical_JSON_bytes": len(reader.encoded(model)),
        "canonical_JSON_sha256": reader.digest(reader.encoded(model))}
    return result


def small_summary(report):
    result = {k: copy.deepcopy(v) for k, v in report.items()
              if k not in (STAGE, "exact_input_storage")}
    result["exact_input_storage_metadata"] = compact_metadata(report.get("exact_input_storage", {}))
    stage = report.get(STAGE, {})
    result[STAGE] = {k: compact_metadata(v, k) for k, v in stage.items()
                     if k not in ("checkpoint", "solver",
                                  "cross_center_norm_memory",
                                  "curvature_defect_guard_learning_checkpoint",
                                  "curvature_defect_guard_observation")}
    solver = stage.get("solver", {})
    result[STAGE]["solver"] = {
        k: compact_metadata(v, k) for k, v in solver.items()
        if k not in ("models", "initial_actual_two_grid_decisions")}
    result[STAGE]["initial_actual_two_grid_decisions"] = copy.deepcopy(
        solver.get("initial_actual_two_grid_decisions"))
    result[STAGE]["model_count"] = len(solver.get("models", []))
    snap = stage.get("checkpoint", {})
    result[STAGE]["selected_two_grid_physical_point"] = copy.deepcopy(
        snap.get("selected_two_grid_physical_point"))
    result[STAGE]["snapshot_scalar_counters"] = {
        k: copy.deepcopy(snap[k]) for k in (
            "initialization_elapsed_seconds", "optimization_elapsed_seconds",
            "value_geometry_seconds", "total_full_value_physical_evaluations",
            "coarse_physical_evaluations", "fine_physical_evaluations",
            "doubled_angle_value_seconds") if k in snap}
    result["factorized_selected_J_execution"] = copy.deepcopy(
        snap.get("selected_row_factorization_statistics"))
    progress = stage.get("complete_original_grid_oracle_progress",
                         snap.get("complete_original_grid_oracle_progress", []))
    result["complete_original_grid_oracle_progress"] = [
        {k: (omitted(v, "original direction observations are in the one MODEL record")
             if k in ("direction_events", "new_original_row_J_events") else compact_metadata(v, k))
         for k, v in p.items()} for p in progress]
    learning = stage.get("curvature_defect_guard_observation", {})
    result["curvature_defect_guard_observation"] = {
        k: compact_metadata(v, k) for k, v in learning.items()
        if k not in ("paid_initial_samples",)}
    result["final_bank_scalar_report"] = {
        k: copy.deepcopy(v) for k, v in stage.get("cross_center_norm_memory", {}).items()
        if k != "rebuild_events"}
    # The complete final159/reference/pools/normals/learning history appears once.
    # It is runner output only, never committed/uploaded as an artifact.
    return result


def save_report(output, report):
    now = time.monotonic()
    report["process_total_elapsed_seconds"] = now-PROCESS_STARTED
    if report.get("scientific_started_monotonic") is not None:
        report["new_scientific_elapsed_seconds_including_input_prepare"] = (
            now-report["scientific_started_monotonic"])
    report["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    atomic_save(output, report)
    atomic_save(Path(output).with_name("direct-reference-audit-summary.json"), small_summary(report))


def emit_result(report):
    for model in report.get(STAGE, {}).get("solver", {}).get("models", []):
        emit("MODEL", semantic_model(model))
    emit("COMPLETE", small_summary(report))


def new_checkpoint(objective, problem, point, stage):
    return {
        "schema": POLICY+"-future-direct-checkpoint",
        "reference_complete163_binary64_exact": [
            str(Q.from_float(float(x))) for x in problem.coordinates.reference_state],
        "coordinate_definition": copy.deepcopy(problem.coordinate_definition),
        "selected_final159_binary64_exact": copy.deepcopy(
            point["exact_binary64_independent_coordinates"]),
        "selected_final163_physical_exact": copy.deepcopy(
            point["exact_original_physical_coefficients"]),
        "selected_physical_state_sha256": point["physical_state_sha256"],
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
        "supplemental_paid_normals": copy.deepcopy(objective.supplemental_normals),
        "curvature_defect_guard_learning_checkpoint": objective.curvature_defect_memory.checkpoint(),
        "information_migration_receipts": {
            "bank": copy.deepcopy(objective.checkpoint_bank_input),
            "learning": copy.deepcopy(objective.curvature_defect_memory.migration_lineage)},
        "new_task_started_LPs": stage["solver"]["linear_program_invocation_count"],
        "new_task_shared_values": objective.full_value_evaluations,
        "new_task_scientific_elapsed_seconds": time.monotonic()-objective.scientific_started,
        "ancestor_costs": copy.deepcopy(objective.direct_task_metadata["ancestor_costs"]),
        "closed_old_epoch_is_not_resumed": True,
        "new_context_hashes_are_not_old_context_hashes": True,
        "arrays_only_in_this_runner_output_not_saved_to_repository_or_release": True}


def accepted_receipts(stage, point):
    if point["accepted_index"] == 0:
        decisions = stage["solver"]["initial_actual_two_grid_decisions"]
        return (copy.deepcopy(decisions["coarse"]), copy.deepcopy(decisions["fine"]),
                {"kind": "this-new-adapter-initial-two-required-values",
                 "accepted_index": 0, "physical_state_sha256": point["physical_state_sha256"]})
    hits = [(m["number"], i, t) for m in stage["solver"]["models"]
            for i, t in enumerate(m["trials"])
            if t.get("accepted_as_next_iterate") is True
            and t.get("accepted_index") == point["accepted_index"]
            and t.get("physical_state_sha256") == point["physical_state_sha256"]]
    transfer.require(len(hits) == 1, "one actual accepted trial must own final two-grid gates")
    number, index, trial = hits[0]
    return (copy.deepcopy(trial["coarse_decision"]), copy.deepcopy(trial["fine_decision"]),
            {"kind": "this-new-adapter-complete-two-grid-accepted-trial",
             "model_number": number, "trial_index": index, "accepted_index": point["accepted_index"],
             "physical_state_sha256": point["physical_state_sha256"]})


def run_audit(prepared, output, *, scientific_started, preparation_segments, development_receipt):
    restored, bindings, tenth, replay, coarse_pool, fine_pool = prepared
    problem, initial, gate, lower, upper, source_cfg, cfg = restored
    real, source_cp = replay["original_report"], replay["source_checkpoint"]
    report = {
        "schema": SCHEMA, "status": "new-direct-reference-task-not-yet-started",
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "source_files_sha256": implementation_hashes(),
        "configuration": copy.deepcopy(cfg), "source_configuration_sha256": digest(source_cfg),
        "policy_definition": definition(), "exact_input_storage": bindings,
        "scientific_started_monotonic": scientific_started,
        "new_scientific_resource_limits": dict(RESOURCE_LIMITS, per_LP_seconds=10),
        "development_receipt": copy.deepcopy(development_receipt),
        "source_transfer": copy.deepcopy(replay["source_completed_log_transfer"]),
        "ancestor_costs": copy.deepcopy(replay["ancestor_costs"]),
        "old_developer_suite_optimizer_LP_JVP_trial_replays": 0,
        "new_scientific_recovery_entries": 0,
        "new_independent_final_full_grid_geometry_calls": 0,
        "same_immutable_g_b0_reference163_and_exact159_input": True,
        "new_field_and_objective_identity_not_old_hash_impersonation": True,
        "timing_segments": copy.deepcopy(preparation_segments),
        "source_initial_physical_state_sha256": replay["canonical_physical_state_sha256"],
        "source_final_selection_validation": copy.deepcopy(replay["source_final_selection_validation"]),
        "limitations": {
            "new_metric026_is_not_an_isometry_1e_6_claim": True,
            "hard_curvature58_is_not_the_continuous_reach_target": True,
            "finite_grid_actual_gates_not_a_global_embedding_certificate": True,
            "empirical_gamma_not_a_proved_nonlinear_error_bound": True,
            "inexact_cut_model_stop_not_convex_stationarity": True,
            "speedup_not_claimed_before_measuring_actual_new_subcalls": True}}
    objective = None
    constructor_started = time.monotonic()
    try:
        transfer.check_clock(scientific_started)
        radial, theta, grid = original_audit.curvature_grid(tenth)
        def checkpoint(snapshot):
            report[STAGE] = {"status": "new-task-last-qualified-checkpoint",
                             "checkpoint": snapshot, "solver": {}}
            save_report(output, report)
        objective = DirectReferenceGuardObjective(
            problem, gate, radial, theta, int(source_cfg["primitive_order"]), lower, upper,
            cfg=cfg, checkpoint=checkpoint, radial_nodes_exact=grid["radial_nodes_exact"],
            replay=replay, source_cfg=source_cfg, scientific_started=scientific_started,
            direct_reference_policy=POLICY)
        report["timing_segments"]["new_constructor_and_information_migration_seconds"] = (
            time.monotonic()-constructor_started)
        report["new_evaluation_identities"] = {
            "ordinary_field": objective.factorized.ordinary_evaluation_sha256,
            "factorization": objective.factorized.definition_sha256,
            "objective_before_controller_initialization": objective.evaluation_sha256,
            "source_ordinary_field": problem.implementation_definition()["original_ordinary_evaluation_sha256"],
            "physical_coordinate": problem.coordinate_definition_sha256}
        report["phase"] = "same-process-new-ordinary-caches-selected-J-factories-and-actual-steps"
        report["new_scientific_recovery_entries"] = 1
        recovery_started = time.monotonic()
        stage = run_direct_reference_recovery(
            objective, initial, restored_controller=replay["controller_continuation"])
        report[STAGE] = stage
        report["timing_segments"]["new_recovery_path_seconds"] = time.monotonic()-recovery_started
        snap = stage["checkpoint"]
        point = snap.get("selected_two_grid_physical_point")
        if point is None:
            report["status"] = "new-task-stopped-before-two-grid-initial-point"
            report["source_paid_point_remains_available_as_ancestral_input"] = {
                "physical_state_sha256": source_cp["selected_physical_state_sha256"],
                "not_relabelled_as_new_adapter_value_receipt": True}
            save_report(output, report); emit_result(report)
            return report
        final = exact_vector(point["exact_binary64_independent_coordinates"], 159)
        transfer.require(
            np.array_equal(final, np.asarray(point["independent_coordinates_binary64"], float))
            and [str(x) for x in problem.coordinates.physical_exact(final)] ==
                point["exact_original_physical_coefficients"]
            and digest(problem.identity(final)) == point["physical_state_sha256"],
            "selected exact159 and mapped physical163 identities differ")
        exact_box = problem.coordinates.exact_box_decision(final, gate.original_lower, gate.original_upper)
        transfer.require(exact_box["exact_original_box_pass"] is True,
                         "selected physical163 exact coupled box failed")
        original_metric = problem.metric_model(initial)
        copied, copied_state = problem.frozen_metric_copy(final)
        transfer.require(
            copied is problem and copied_state.tobytes() == final.tobytes()
            and copied.identity(copied_state) == problem.identity(final)
            and copied.metric_model(copied_state) == original_metric
            and copied.height_base_definition == problem.height_base_definition
            and copied.coordinate_definition == problem.coordinate_definition,
            "same-process frozen-state copy changed g/b0/reference/map")
        coarse, fine, source = accepted_receipts(stage, point)
        flags = {label: d["actual_gate_booleans"] for label, d in (("coarse", coarse), ("fine", fine))}
        transfer.require(all(len(f) == 14 and all(v is True for v in f.values())
                             for f in flags.values()), "one original actual gate did not pass")
        transfer.require(all(d["direct_max_eta"] == point[label]["direct_max_eta"]
                             for label, d in (("coarse", coarse), ("fine", fine))),
                         "complete gate receipts and selected maxima disagree")
        maximum = max(coarse["direct_max_eta"], fine["direct_max_eta"])
        maximum_curvature = max(coarse["direct_maximum_absolute_principal_curvature"],
                                fine["direct_maximum_absolute_principal_curvature"])
        source_maximum = real["final_selection_validation"]["both_grid_maximum_eta"]
        report["final_actual_gate_booleans"] = flags
        report["selected_gate_receipt_source"] = source
        report["final_full_grid_constraints"] = coarse
        report["final_doubled_constraints"] = fine
        report["final_selection_validation"] = {
            "both_value_grids_hard_and_old_metric_pass": True,
            "initial_both_grid_maximum_eta_paid": source_maximum,
            "initial_both_grid_maximum_eta_new_method":
                stage["checkpoint"]["accepted_iterates"][0]["maximum_eta_on_both_grids"],
            "both_grid_maximum_eta": maximum, "both_grid_maximum_curvature": maximum_curvature,
            "eta_change_from_paid_scalar": source_maximum-maximum,
            "actual_new_task_eta_decrease":
                stage["checkpoint"]["accepted_iterates"][0]["maximum_eta_on_both_grids"]-maximum,
            "new_metric_target_qualified_on_both_grids":
                point["new_metric_target_qualified_on_both_grids"],
            "source_state_unchanged": point["physical_state_sha256"] == source_cp["selected_physical_state_sha256"],
            "exact_original_box_pass": True,
            "not_a_new_independent_final_geometry_audit": True}
        report["final_exact_box"] = exact_box
        report["future_direct_checkpoint"] = new_checkpoint(objective, problem, point, stage)
        report["value_evaluation_counts"] = {
            "new_shared_values": objective.full_value_evaluations,
            "new_shared_value_cap": 160,
            "new_coarse_values": objective.geometry_evaluations,
            "new_fine_values": objective.fine_evaluations,
            "old_shared_values15_are_only_ancestor_history": True,
            "new_independent_final_value_calls": 0,
            "accepted_complete_two_grid_receipts_are_the_final_gates": True,
            "adapter_started_and_failed_calls_reported_separately": True}
        report["bank_migration_and_new_activity"] = {
            "source_entries": 438, "source_cumulative_insertions": replay["inherited_bank_report"]["insertions"],
            "fresh_initial_state_sha256": objective.expected_initial_bank_state_sha256,
            "current_entries": len(objective.direction_bank.entries),
            "current_state_sha256": objective.direction_bank.state_digest(),
            "new_remember_calls": objective.direction_bank.insertions-replay["inherited_bank_report"]["insertions"],
            "supplemental_normals_count_not_bank_entries": 4,
            "supplements_did_not_replace_source_same_ID_normals": True,
            "first_actual_model_bound": objective.initial_bank_replay.get("passed") is True}
        report["status"] = COMPLETE if not stage.get("error") else "new-direct-task-error-best-preserved"
    except Exception as error:
        report["status"] = "new-direct-reference-task-audit-error"
        report["error"] = {"type": type(error).__name__, "message": str(error),
                           "traceback": traceback.format_exc()}
        report["timing_segments"]["constructor_recovery_or_report_until_error_seconds"] = (
            time.monotonic()-constructor_started)
        if objective is not None:
            report["actual_counters_at_error"] = {
                "new_shared_values": objective.full_value_evaluations,
                "new_scientific_elapsed_seconds": time.monotonic()-scientific_started}
            report["new_adapter_timing_at_error"] = problem.timing_snapshot()
            if STAGE not in report:
                report[STAGE] = {"status": "new-task-error-current-checkpoint",
                                 "checkpoint": objective.snapshot(), "solver": {}}
    save_report(output, report)
    emit_result(report)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    require_public_research_environment()
    output = Path(args.out); output.parent.mkdir(parents=True, exist_ok=True)
    raw_request = Path(args.request).read_bytes()
    request = json.loads(raw_request)
    scientific_started = None
    try:
        transfer.require(request.get("parameters", {}).get("new_policy") == POLICY,
                         "explicit new direct-reference request required")
        for path, expected in request["source_sha256"].items():
            transfer.require(reader.digest(Path(path).read_bytes()) == expected,
                             "new task requested source bytes differ: "+path)
        current = implementation_hashes()
        requested_python = {Path(p).name: h for p, h in request["source_sha256"].items() if p.endswith(".py")}
        transfer.require(requested_python == current, "complete requested Python dependency closure differs")
        emit("REQUEST", {
            "source_commit": os.environ.get("GITHUB_SHA"),
            "request_bytes": len(raw_request), "request_sha256": reader.digest(raw_request),
            "source_sha256": request["source_sha256"], "parameters": request["parameters"]})
        dev_started = time.monotonic()
        dev = development.developer_check()
        dev["source_files_sha256"] = current
        dev["actual_development_entry_wall_seconds"] = time.monotonic()-dev_started
        emit("DEVELOPMENT", dev)
        atomic_save(output.with_name("direct-reference-development.json"), dev)
        transfer.require(dev["all_passed"] is True and dev["new_group_count"] == 3
                         and dev["new_case_count"] == dev["executed_check_count"] == 9,
                         "the new three-group nine-check interface did not pass")
        dev_payload = reader.encoded(dev)
        dev_receipt = {
            "new_groups": 3, "new_cases": 9, "all_passed": True,
            "canonical_JSON_plus_LF_bytes": len(dev_payload)+1,
            "canonical_JSON_plus_LF_sha256": reader.digest(dev_payload+b"\n"),
            "elapsed_seconds": dev["actual_development_entry_wall_seconds"],
            "execution": copy.deepcopy(dev["execution"]),
            "development_before_scientific_start_not_charged_as_research": True}
        # The sole new scientific clock starts BEFORE the first necessary paid
        # log / input read. It is never reset at constructor, first J or model1.
        scientific_started = time.monotonic()
        completed = transfer.read_completed(request, scientific_started=scientific_started)
        source_read_seconds = time.monotonic()-scientific_started
        emit("PRIOR_WORK_REUSED", completed[-1])
        input_started = time.monotonic()
        prepared = transfer.prepare_transfer(
            request, output, PROCESS_STARTED, completed=completed,
            scientific_started=scientific_started)
        segments = {
            "paid_source_log_read_and_receipt_validation_seconds": source_read_seconds,
            "necessary24_input_and_immutable_prepare_seconds": time.monotonic()-input_started,
            "all_scientific_input_prepare_seconds": time.monotonic()-scientific_started,
            "process_before_scientific_start_including_imports_newdev_source_hashes_seconds":
                scientific_started-PROCESS_STARTED}
        result = run_audit(prepared, output, scientific_started=scientific_started,
                           preparation_segments=segments, development_receipt=dev_receipt)
        raw = output.read_bytes()
        emit("OUTPUT_METADATA", {"name": output.name, "bytes": len(raw), "sha256": reader.digest(raw),
                                 "only_runner_temporary_output_no_payload_upload": True})
        return 0 if result["status"] == COMPLETE else 1
    except Exception as error:
        report = {
            "schema": SCHEMA, "status": "new-development-or-input-error-no-science-replay",
            "scientific_started_monotonic": scientific_started,
            "error": {"type": type(error).__name__, "message": str(error),
                      "traceback": traceback.format_exc()},
            "source_files_sha256": implementation_hashes(),
            "old_developer_LP_optimizer_replays": 0}
        save_report(output, report)
        emit("ENTRY_ERROR", report)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

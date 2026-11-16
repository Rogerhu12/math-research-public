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
from frame_height_null_gate import FiveNullHeightGate
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




PAID_PREVIOUS_ATTEMPT = {
    "run_id": "43778983026", "job_id": "133011642024",
    "source_commit": "439fe8b9b8fc9cffdfdb9d8cf01acc6687e0a48c",
    "log_bytes": 208955,
    "log_sha256": "68d723fd4132084e61f20b96fa3012e00e44b325a83c797b266be0046063e86c",
    "request_record_bytes": 26904,
    "request_record_sha256": "8029a35a421d93d57a90ea575fd10062e9d66fd69c64602c2a8870f664165881",
    "original_request_bytes": 40389,
    "original_request_sha256": "52645511b072a72ba2d8498094893dfe9a4dd4c87255c252ba416577987800e5",
    "development_reuse_bytes": 2298,
    "development_reuse_sha256": "ac54fae177ec63e7e232048731c651b5a306420e28d4080728dc7e99c37127f6",
    "complete_payload_bytes": 99050,
    "complete_payload_sha256": "8731e263ea059b0069260cd1e1774ddedb321226ab6cd29f4ca5d2084d7fb989",
    "prior_reuse_payload_bytes": 1135,
    "prior_reuse_payload_sha256": "46480623a3a683dd1a202c9b1f2f47f7105ca43580c5e64d85aa1546a1944661",
    "paid_scientific_seconds": 28.690336299000023,
}
PREVIOUS_ALLOWED_CHANGED = {
    "topics/visible-flex-new-mechanism/scripts/frame_metric_direct_reference_audit.py":
        "8008a7f92024bd745107784647fd1502a78ab3c5978dba3221abbebc66fc4eee",
    ".github/workflows/visible-direct-reference-new-task.yml":
        "24c9dba46d1213ef385d6b6916edf8c5f6e2aab46021700a904b7b7695f8fd25",
}


def read_paid_nine_checks(request, *, scientific_started):
    """Consume the second failure and its authenticated nine-check reuse chain."""
    transfer.check_clock(scientific_started)
    source = request["paid_previous_attempt"]
    transfer.require(all(source.get(k) == v for k, v in PAID_PREVIOUS_ATTEMPT.items()),
                     "only the pinned second direct-reference attempt can be consumed")
    api = reader.GitHubReader(transfer.REPO)
    run = api.api_json("/actions/runs/"+source["run_id"])
    job = api.api_json("/actions/jobs/"+source["job_id"])
    transfer.require(
        str(run["id"]) == source["run_id"] and str(job["id"]) == source["job_id"]
        and str(job["run_id"]) == source["run_id"]
        and run["head_sha"] == job["head_sha"] == source["source_commit"]
        and run["status"] == job["status"] == "completed"
        and run["conclusion"] == job["conclusion"] == "failure",
        "previous run/job/head/conclusion link differs")
    raw, redirects = api.job_log(source["job_id"])
    transfer.check_clock(scientific_started)
    transfer.require(len(raw) == source["log_bytes"] and reader.digest(raw) == source["log_sha256"],
                     "paid previous original log bytes differ")
    tags = tuple(TAG+x for x in ("REQUEST", "DEVELOPMENT", "DEVELOPMENT_REUSED",
                                "PRIOR_WORK_REUSED", "COMPLETE", "MODEL", "ENTRY_ERROR"))
    records = transfer.paid.inherited.tagged_records(raw, tags)
    transfer.require(not records[TAG+"DEVELOPMENT"] and not records[TAG+"MODEL"]
                     and not records[TAG+"ENTRY_ERROR"],
                     "the second attempt must have reused development and stopped without models")
    one = transfer.paid._one
    old_request = one(records, TAG+"REQUEST", source, "request_record_bytes", "request_record_sha256")
    reused = one(records, TAG+"DEVELOPMENT_REUSED", source,
                 "development_reuse_bytes", "development_reuse_sha256")
    complete = one(records, TAG+"COMPLETE", source, "complete_payload_bytes", "complete_payload_sha256")
    prior = one(records, TAG+"PRIOR_WORK_REUSED", source,
                "prior_reuse_payload_bytes", "prior_reuse_payload_sha256")
    transfer.require(
        old_request["source_commit"] == source["source_commit"]
        and old_request["request_bytes"] == source["original_request_bytes"]
        and old_request["request_sha256"] == source["original_request_sha256"],
        "previous161-file request identity differs")
    old_files, current_files = old_request["source_sha256"], request["source_sha256"]
    transfer.require(
        len(old_files) == len(current_files) == 161 and set(old_files) == set(current_files)
        and set(PREVIOUS_ALLOWED_CHANGED).issubset(old_files),
        "the same complete161-file binding is required")
    for path, expected in old_files.items():
        if path in PREVIOUS_ALLOWED_CHANGED:
            transfer.require(expected == PREVIOUS_ALLOWED_CHANGED[path],
                             "unexpected old identity of an allowed changed file: "+path)
        else:
            transfer.require(current_files[path] == expected, "an already-paid source changed: "+path)
        transfer.require(reader.digest(Path(path).read_bytes()) == current_files[path],
                         "current requested file bytes differ: "+path)
    old_python = {Path(p).name: h for p, h in old_files.items() if p.endswith(".py")}
    transfer.require(
        len(old_python) == 152 and sum(p.endswith(".py") for p in old_files) == 152
        and sum(p.endswith(".py") and p not in PREVIOUS_ALLOWED_CHANGED for p in old_files) == 151
        and complete["source_files_sha256"] == old_python,
        "previous152-Python closure or unchanged151-source identities differ")
    transfer.require(
        reused["schema"] == POLICY+"-paid-nine-check-reuse"
        and reused["passed"] is True and reused["all_paid_cases_passed"] is True
        and reused["source_run_id"] == "43777844163"
        and reused["source_job_id"] == "133008102089"
        and reused["source_commit"] == "ad3b104606347c345020d229b6fbc1c648dabacc"
        and reused["log_bytes"] == 185504
        and reused["log_sha256"] == "1890cc27b6f6ca3ff28cf2d821c73e9c4e78b8912822452cd6ec17c52a61b0cf"
        and reused["development_JSON_plus_LF_bytes"] == 25953
        and reused["development_JSON_plus_LF_sha256"] ==
            "717719da39d867b3206c12250ccc1df92e5276245cc48d8d9e4e6ba76b4accae"
        and (reused["bound_files"], reused["Python_files"], reused["unchanged_Python_files"]) == (161, 152, 151)
        and (reused["paid_groups"], reused["paid_cases"]) == (3, 9)
        and reused["new_development_groups_executed"] == reused["new_development_cases_executed"] == 0
        and reused["old_scientific_replays"] == 0
        and reused["adapter_core_and_development_and_epoch_outer_transfer_unchanged"] is True,
        "the source-pinned transitive original nine-check receipt differs")
    first_cost = reused["first_failure_cost"]
    transfer.require(first_cost["paid_scientific_seconds_including_source_read_and_prepare"] ==
                     13.756976061000046
                     and first_cost["paid_process_seconds"] == 17.244257307999987
                     and first_cost["paid_development_seconds_separate_from_science"] ==
                     1.5606790740000633
                     and all(first_cost[k] == 0 for k in (
                         "new_J_batches", "new_LPs", "new_accepted_iterates",
                         "new_models", "new_ordinary_values")),
                     "first-attempt paid clock or zero-science counters differ")
    stage = complete[STAGE]
    timing = stage["direct_reference_geometry_timing"]
    solver = stage["solver"]
    transfer.require(
        complete["schema"] == SCHEMA
        and complete["status"] == "new-task-stopped-before-two-grid-initial-point"
        and complete["github_sha"] == source["source_commit"]
        and str(complete["github_run_id"]) == source["run_id"]
        and complete["github_repository"] == transfer.REPO
        and complete["new_scientific_recovery_entries"] == 1
        and complete["old_developer_suite_optimizer_LP_JVP_trial_replays"] == 0
        and stage["status"] == "direct-reference-guarded-recovery-error"
        and stage["error"] == {"type": "ValueError",
            "message": "height primitive or exact-polynomial evaluation changed during this stage"}
        and stage["model_count"] == 0 and stage["selected_two_grid_physical_point"] is None
        and stage["snapshot_scalar_counters"]["total_full_value_physical_evaluations"] == 0
        and stage["snapshot_scalar_counters"]["value_geometry_seconds"] == 0
        and all(solver[k] == 0 for k in ("linear_program_invocation_count",
                "primary_LP_invocation_count", "correction_LP_invocation_count"))
        and all(timing[k] == 0 for k in (
            "geometry_calls_started", "geometry_calls_completed", "geometry_calls_failed"))
        and complete["complete_original_grid_oracle_progress"] == []
        and all(complete["factorized_selected_J_execution"][g][k] == 0
                for g in ("coarse", "fine") for k in ("batches", "refreshes"))
        and "future_direct_checkpoint" not in complete
        and complete["source_initial_physical_state_sha256"] == request["source"]["final_physical_sha256"]
        and complete["original_query_quadrature_order"]["value"] == 8,
        "only the exact pre-ordinary gate-identity failure with zero values/J/LPs is reusable")
    transfer.require(
        stage["direct_reference_bank_migration"]["passed_input_validation"] is True
        and stage["direct_reference_bank_migration"]["first_actual_complete_factory_bound"] is False
        and stage["direct_reference_bank_migration"]["source_state_sha256"] ==
            request["source"]["terminal_norm_bank_state_sha256"]
        and stage["curvature_learning_context_migration"]["old_event_retraining_calls"] == 0,
        "previous migration or pending-current-model boundary differs")
    transfer.require(prior["passed"] is True and prior["original_source_python_files"] == 140
                     and prior["original_request_bound_files"] == 146
                     and prior["original_guard_development_checks"] == 18
                     and prior["old_development_executions"] == 0
                     and prior["old_optimizer_LP_JVP_trial_replays"] == 0
                     and prior["transitive_old20_19_26_and_cache_receipts_checked"] is True,
                     "original paid source and transitive development receipt differs")
    science = complete["new_scientific_elapsed_seconds_including_input_prepare"]
    process = complete["process_total_elapsed_seconds"]
    first_science = first_cost["paid_scientific_seconds_including_source_read_and_prepare"]
    transfer.require(type(science) in (int, float) and np.isfinite(science)
                     and science == source["paid_scientific_seconds"] and science >= first_science
                     and type(process) in (int, float) and np.isfinite(process)
                     and process == 16.883830578999948
                     and complete["timing_segments"]["already_paid_first_attempt_scientific_seconds"]
                         == first_science,
                     "previous cumulative scientific/process clock differs")
    cost = {
        "cumulative_paid_scientific_seconds": science,
        "previous_attempt_scientific_increment_seconds": science-first_science,
        "previous_attempt_process_seconds": process,
        "first_attempt_cost": copy.deepcopy(first_cost),
        "previous_attempt_timing_segments": copy.deepcopy(complete["timing_segments"]),
        "paid_development_seconds_separate_from_science":
            first_cost["paid_development_seconds_separate_from_science"],
        "new_LPs": 0, "new_ordinary_values": 0, "new_J_batches": 0,
        "new_models": 0, "new_accepted_iterates": 0,
        "latest_cumulative28_seconds_inherited_once_not_added_to_first13_again": True,
        "process_import_and_development_seconds_not_added_again": True}
    receipt = {
        "schema": POLICY+"-paid-nine-check-chain-reuse", "passed": True,
        "source_run_id": source["run_id"], "source_job_id": source["job_id"],
        "source_commit": source["source_commit"], "original_conclusion": "failure",
        "log_bytes": len(raw), "log_sha256": reader.digest(raw),
        "request_JSON_plus_LF_bytes": source["request_record_bytes"],
        "request_JSON_plus_LF_sha256": source["request_record_sha256"],
        "development_reuse_JSON_plus_LF_bytes": source["development_reuse_bytes"],
        "development_reuse_JSON_plus_LF_sha256": source["development_reuse_sha256"],
        "complete_JSON_plus_LF_bytes": source["complete_payload_bytes"],
        "complete_JSON_plus_LF_sha256": source["complete_payload_sha256"],
        "original_nine_check_evidence": {
            "run_id": reused["source_run_id"], "source_commit": reused["source_commit"],
            "development_JSON_plus_LF_bytes": reused["development_JSON_plus_LF_bytes"],
            "development_JSON_plus_LF_sha256": reused["development_JSON_plus_LF_sha256"]},
        "bound_files": 161, "Python_files": 152, "unchanged_Python_files": 151,
        "paid_groups": 3, "paid_cases": 9, "all_paid_cases_passed": True,
        "new_development_groups_executed": 0, "new_development_cases_executed": 0,
        "old_scientific_replays": 0, "first_failed_log_downloads_this_attempt": 0,
        "previous_failed_log_downloads_this_attempt": 1,
        "allowed_changed_paths": list(PREVIOUS_ALLOWED_CHANGED),
        "adapter_core_and_development_and_epoch_outer_transfer_unchanged": True,
        "paid_cost": cost, "redirects_without_authorization": redirects,
        "payload_only_in_runner_memory_no_repository_or_artifact_upload": True}
    transfer.check_clock(scientific_started)
    return receipt, cost


def fresh_adapter_gate(original_gate, problem, state, lower, upper):
    """Rebuild only the numerical gate identity through its original constructor."""
    # Keep the original physical163 cap gate, exact H/reference and box.  Its
    # strict context check remains inside from_original and assert_context.
    gate = FiveNullHeightGate.from_original(
        original_gate.original_gate, problem,
        original_gate.original_lower, original_gate.original_upper)
    expected = copy.deepcopy(original_gate.numerical_definition)
    expected["problem_evaluation"] = copy.deepcopy(problem.evaluation_definition())
    transfer.require(
        gate.original_gate is original_gate.original_gate
        and gate.coordinates is original_gate.coordinates is problem.coordinates
        and gate.physical_definition == original_gate.physical_definition
        and gate.physical_sha256 == original_gate.physical_sha256
        and gate.coordinate_definition_sha256 == original_gate.coordinate_definition_sha256
        and gate.reference_provenance == original_gate.reference_provenance
        and gate.numerical_definition == expected
        and gate.numerical_sha256 == digest(expected)
        and gate.problem_evaluation_sha256 == digest(problem.evaluation_definition())
        and gate.numerical_sha256 != original_gate.numerical_sha256,
        "fresh gate may change only the declared ordinary evaluation identity")
    for name in ("kind", "nunknown", "side", "length", "target",
                 "reference_height", "intercept", "height_slice", "family"):
        transfer.require(getattr(gate, name) == getattr(original_gate, name),
                         "physical null-cap gate scalar changed: "+name)
    for name in ("row", "weights", "original_lower", "original_upper",
                 "coordinate_lower", "coordinate_upper"):
        a, b = np.asarray(getattr(gate, name)), np.asarray(getattr(original_gate, name))
        transfer.require(a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes(),
                         "physical/null gate array changed: "+name)
    transfer.require(gate.coordinate_lower.tobytes() == np.asarray(lower).tobytes()
                     and gate.coordinate_upper.tobytes() == np.asarray(upper).tobytes(),
                     "caller159 pivot envelope changed")
    gate.assert_context(problem, state)
    return gate, {
        "original_physical_gate_sha256": gate.physical_sha256,
        "coordinate_definition_sha256": gate.coordinate_definition_sha256,
        "old_numerical_gate_sha256": original_gate.numerical_sha256,
        "new_numerical_gate_sha256": gate.numerical_sha256,
        "old_ordinary_evaluation_sha256": original_gate.problem_evaluation_sha256,
        "new_ordinary_evaluation_sha256": gate.problem_evaluation_sha256,
        "original_physical_gate_and_exact_H_objects_shared": True,
        "only_numerical_definition_problem_evaluation_field_changed": True,
        "original_assert_context_executed_without_bypass": True,
        "all_physical_rows_height_target_boxes_and159_bounds_bitwise_unchanged": True,
        "no_geometry_J_LP_or_value_call": True}



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


def run_audit(prepared, output, *, scientific_started, preparation_segments, development_receipt,
              paid_previous_attempt):
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
        "paid_previous_attempt_receipt": copy.deepcopy(paid_previous_attempt),
        "same_new_task_scientific_clock_inherits_both_failed_attempts_once": True,
        "current_development_group_and_case_executions": 0,
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
        # The old audit's source_cfg was the input/field configuration.  This
        # task's source_cfg is the solver configuration, which has no order key.
        # Read the same unchanged authoritative BoundEntryHeightProblem value.
        bounded = problem.original_problem.base
        order = int(bounded.primitive_order)
        transfer.require(order > 0 and order == int(bounded.fixed_primitive.order),
                         "original bounded/query primitive-order provenance differs")
        report["original_query_quadrature_order"] = {
            "value": order, "source": "problem.original_problem.base.primitive_order",
            "same_fixed_primitive_order": True, "no_default_or_solver_cfg_mutation": True}
        gate, gate_receipt = fresh_adapter_gate(gate, problem, initial, lower, upper)
        report["fresh_adapter_cap_gate_binding"] = gate_receipt
        def checkpoint(snapshot):
            report[STAGE] = {"status": "new-task-last-qualified-checkpoint",
                             "checkpoint": snapshot, "solver": {}}
            save_report(output, report)
        objective = DirectReferenceGuardObjective(
            problem, gate, radial, theta, order, lower, upper,
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
        report["future_direct_checkpoint"]["paid_attempts_of_this_new_task"] = [
            copy.deepcopy(paid_previous_attempt)]
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
        transfer.require(
            all(request.get("paid_previous_attempt", {}).get(k) == v
                for k, v in PAID_PREVIOUS_ATTEMPT.items()),
            "explicit pinned transitive nine-check reuse and cumulative failed cost required")
        # This is the SAME independent1800s task.  Both failed attempts used
        # zero values/J/LPs, but their cumulative28.690336299s remains spent.
        # It already includes the first13.756976061s: never add them twice.
        # Prior process/import/development costs remain separate receipts.
        current_scientific_started = time.monotonic()
        scientific_started = current_scientific_started-PAID_PREVIOUS_ATTEMPT["paid_scientific_seconds"]
        reuse_started = time.monotonic()
        paid_previous, paid_cost = read_paid_nine_checks(
            request, scientific_started=scientific_started)
        paid_failure_read_seconds = time.monotonic()-reuse_started
        emit("DEVELOPMENT_REUSED", paid_previous)
        dev_receipt = {
            "paid_groups": 3, "paid_cases": 9, "all_paid_cases_passed": True,
            "current_new_groups_executed": 0, "current_new_cases_executed": 0,
            "canonical_JSON_plus_LF_bytes":
                paid_previous["original_nine_check_evidence"]["development_JSON_plus_LF_bytes"],
            "canonical_JSON_plus_LF_sha256":
                paid_previous["original_nine_check_evidence"]["development_JSON_plus_LF_sha256"],
            "paid_development_seconds_separate_from_science":
                paid_cost["paid_development_seconds_separate_from_science"],
            "current_development_execution_seconds": 0,
            "receipt_verified_without_running_developer_check": True}
        source_read_started = time.monotonic()
        completed = transfer.read_completed(request, scientific_started=scientific_started)
        source_read_seconds = time.monotonic()-source_read_started
        emit("PRIOR_WORK_REUSED", completed[-1])
        input_started = time.monotonic()
        prepared = transfer.prepare_transfer(
            request, output, PROCESS_STARTED, completed=completed,
            scientific_started=scientific_started)
        segments = {
            "already_paid_cumulative_scientific_seconds":
                paid_cost["cumulative_paid_scientific_seconds"],
            "previous_attempt_scientific_increment_seconds":
                paid_cost["previous_attempt_scientific_increment_seconds"],
            "paid_second_failed_log_read_and_transitive_reuse_validation_seconds": paid_failure_read_seconds,
            "paid_source_log_read_and_receipt_validation_seconds": source_read_seconds,
            "necessary24_input_and_immutable_prepare_seconds": time.monotonic()-input_started,
            "current_attempt_scientific_input_prepare_seconds":
                time.monotonic()-current_scientific_started,
            "cumulative_scientific_seconds_after_current_input_prepare":
                time.monotonic()-scientific_started,
            "current_process_before_scientific_read_including_imports_and_hashes_seconds":
                current_scientific_started-PROCESS_STARTED,
            "prior_process_import_development_not_added_to_scientific_clock": True}
        result = run_audit(prepared, output, scientific_started=scientific_started,
                           preparation_segments=segments, development_receipt=dev_receipt,
                           paid_previous_attempt=paid_previous)
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

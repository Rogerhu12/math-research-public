#!/usr/bin/env python3
"""Public entry: one new paid-support primary using the last original LP slot."""
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
from frame_metric_terminal_paid_slot import POLICY, SOURCE_SCIENCE_SECONDS, definition
from frame_metric_terminal_paid_slot_resume import TerminalPaidSlotObjective
from frame_metric_terminal_paid_slot_recovery import run_terminal_paid_slot_recovery
import frame_metric_terminal_paid_slot_transfer as transfer
import frame_metric_direct_reference_audit as original_audit
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader

SCHEMA = POLICY+"-audit"
STAGE = "terminal_paid_slot_stage"
COMPLETE = "complete-two-grid-terminal-paid-slot-audit"
TAG = "TERMINAL_SLOT_"
NEW_SOURCES = (
    "frame_metric_terminal_paid_slot.py",
    "frame_metric_terminal_paid_slot_development.py",
    "frame_metric_terminal_paid_slot_transfer.py",
    "frame_metric_terminal_paid_slot_resume.py",
    "frame_metric_terminal_paid_slot_recovery.py",
    "frame_metric_terminal_paid_slot_audit.py")


def implementation_hashes():
    result = original_audit.implementation_hashes()
    folder = Path(__file__).parent
    for name in NEW_SOURCES:
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def emit(suffix, value):
    print(TAG+suffix+" "+reader.encoded(value).decode("utf-8"), flush=True)


def metadata(value):
    raw = reader.encoded(value)
    return {"canonical_JSON_bytes": len(raw), "canonical_JSON_sha256": reader.digest(raw),
            "count": len(value) if isinstance(value, (dict, list)) else None}


def summary(report):
    result = {k: copy.deepcopy(v) for k, v in report.items()
              if k not in (STAGE, "exact_input_storage")}
    result["exact_input_storage_metadata"] = metadata(report.get("exact_input_storage", {}))
    stage = report.get(STAGE, {})
    result[STAGE] = {k: original_audit.compact_metadata(v, k) for k, v in stage.items()
                    if k not in ("checkpoint", "solver", "cross_center_norm_memory",
                                 "curvature_defect_guard_learning_checkpoint",
                                 "terminal_paid_slot_resume",
                                 "complete_original_grid_oracle_progress", "new_candidate_step_record")}
    solver = stage.get("solver", {})
    result[STAGE]["solver"] = {
        k: original_audit.compact_metadata(v, k) for k, v in solver.items() if k != "models"}
    result[STAGE]["model_count"] = len(solver.get("models", []))
    candidate = report.get("new_candidate_step_record", stage.get("new_candidate_step_record"))
    result["new_candidate_step_record"] = copy.deepcopy(candidate)
    result[STAGE]["new_candidate_step_metadata"] = metadata(candidate)
    snap = stage.get("checkpoint", {})
    result[STAGE]["selected_two_grid_physical_point"] = copy.deepcopy(
        snap.get("selected_two_grid_physical_point"))
    result[STAGE]["snapshot_scalar_counters"] = {
        k: copy.deepcopy(snap[k]) for k in (
            "initialization_elapsed_seconds", "optimization_elapsed_seconds",
            "value_geometry_seconds", "total_full_value_physical_evaluations",
            "coarse_physical_evaluations", "fine_physical_evaluations",
            "doubled_angle_value_seconds") if k in snap}
    resume = stage.get("terminal_paid_slot_resume", snap.get("terminal_paid_slot_resume", {}))
    result[STAGE]["resume"] = {
        k: (metadata(v) if k == "source_scalar_trace" else copy.deepcopy(v))
        for k, v in resume.items()}
    result["factorized_selected_J_execution"] = copy.deepcopy(
        snap.get("selected_row_factorization_statistics"))
    result["complete_original_grid_oracle_progress"] = [
        {k: (metadata(v) if k in ("direction_events", "new_original_row_J_events")
             else original_audit.compact_metadata(v, k)) for k, v in item.items()}
        for item in stage.get("complete_original_grid_oracle_progress", [])]
    result["final_bank_scalar_report"] = {
        k: copy.deepcopy(v) for k, v in stage.get("cross_center_norm_memory", {}).items()
        if k != "rebuild_events"}
    result["new_stage_learning_observation"] = original_audit.compact_metadata(
        stage.get("curvature_defect_guard_observation", {}))
    result["selection_scope"] = {
        "one_new_terminal_model_record_emitted_separately": True,
        "all_new_candidate_exact159_is_retained_once_even_if_not_returned": True,
        "final_exact_checkpoint_entries_context_and_learning_retained": True,
        "no_dense_J_A_or_old_model_rerun_payload": True,
        "only_unavailable_old_arrays_are_left_as_their_source_metadata": True}
    return result


def save_report(output, report):
    now = time.monotonic()
    report["process_total_elapsed_seconds"] = now-PROCESS_STARTED
    if report.get("scientific_started_monotonic") is not None:
        cumulative = now-report["scientific_started_monotonic"]
        report["cumulative_same_task_scientific_seconds"] = cumulative
        report["new_scientific_seconds_this_attempt"] = (
            cumulative-report["same_task_inherited_science_seconds"])
    report["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    atomic_save(output, report)
    atomic_save(Path(output).with_name("terminal-paid-slot-audit-summary.json"), summary(report))


def emit_result(report):
    for model in report.get(STAGE, {}).get("solver", {}).get("models", []):
        value = original_audit.semantic_model(model)
        value["source_model_number"] = 28
        value["is_new_terminal_continuation_not_source_MODEL28_republication"] = True
        value["prepared_support_provenance_reference"] = (
            "COMPLETE.future_direct_checkpoint.terminal_paid_slot_continuation.prepared_support_provenance"
            if "future_direct_checkpoint" in report
            else "COMPLETE.prepared_support_provenance")
        emit("MODEL", value)
    emit("COMPLETE", summary(report))


def final_receipts(stage, point, replay):
    if point["accepted_index"] == 27:
        transfer.require(point["physical_state_sha256"] == transfer.IDENTITIES["physical"],
                         "unchanged paid accepted index27 has another physical identity")
        return (copy.deepcopy(replay["source_final_gate_receipts"]["coarse"]),
                copy.deepcopy(replay["source_final_gate_receipts"]["fine"]),
                {"kind": "unchanged-source-exact-point-original-complete14-gate-receipt",
                 "accepted_index": 27, "source_model_number": 27,
                 "not_relabelled_as_a_new_independent_final_audit": True})
    matches = [(m, i, t) for m in stage["solver"]["models"]
               for i, t in enumerate(m.get("trials", []))
               if t.get("accepted_as_next_iterate") is True
               and t.get("accepted_index") == point["accepted_index"]
               and t.get("physical_state_sha256") == point["physical_state_sha256"]]
    transfer.require(len(matches) == 1 and point["accepted_index"] == 28,
                     "one actual new ordinary trial must own acceptance28")
    model, index, trial = matches[0]
    return (copy.deepcopy(trial["coarse_decision"]), copy.deepcopy(trial["fine_decision"]),
            {"kind": "new-terminal-slot-original-complete-two-grid-accepted-trial",
             "accepted_index": 28, "source_model_number": 28,
             "continuation_record_ordinal": 1, "trial_index": index,
             "physical_state_sha256": point["physical_state_sha256"]})


def run_audit(prepared, output, *, scientific_started, segments, development_receipt):
    restored, bindings, tenth, replay, coarse_pool, fine_pool = prepared
    problem, initial, gate, lower, upper, cfg = restored
    cp = replay["source_checkpoint"]
    report = {
        "schema": SCHEMA, "status": "terminal-slot-not-yet-restored",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "source_files_sha256": implementation_hashes(),
        "configuration": copy.deepcopy(cfg), "policy_definition": definition(),
        "scientific_started_monotonic": scientific_started,
        "timing_segments": copy.deepcopy(segments),
        "development_receipt": copy.deepcopy(development_receipt),
        "paid_source_receipt": copy.deepcopy(replay["paid_evidence"]),
        "source_transfer": copy.deepcopy(replay["source_completed_log_transfer"]),
        "exact_input_storage": bindings, "ancestor_costs": copy.deepcopy(replay["ancestor_costs"]),
        "original_source_model_status_unchanged": replay["source_model"]["result"],
        "source_final_selection_validation": copy.deepcopy(replay["source_final_selection_validation"]),
        "source_current_physical_state_sha256": transfer.IDENTITIES["physical"],
        "source_current_accepted_index": 27,
        "same_task_limits": {"LP": 64, "value": 160, "science_seconds": 1800, "single_LP_seconds": 10},
        "same_task_inherited_ledger": copy.deepcopy(replay["inherited_ledger"]),
        "same_task_inherited_values": 58,
        "same_task_inherited_science_seconds": replay["inherited_science_seconds"],
        "original_source_scientific_seconds": SOURCE_SCIENCE_SECONDS,
        "paid_first_attempt_receipt": copy.deepcopy(replay["paid_first_attempt"]),
        "new_recovery_entries": 0, "new_independent_final_geometry_calls": 0,
        "old_developer_optimizer_LP_geometry_or_direction_replays": 0,
        "new_SOC_calls_authorized": 0,
        "limitations": {
            "allocation_stop_is_not_stationarity": True,
            "new_support_does_not_guarantee_descent": True,
            "paid_attainer_not_claimed_to_touch_unknown_old_vector": True,
            "finite_grid_gates_not_continuous_metric_or_reach_certificate": True,
            "lastslot_fail_does_not_justify_identical_stage_restart": True}}
    objective = None
    constructor_started = time.monotonic()
    try:
        transfer.check_clock(scientific_started)
        radial, theta, grid = baseline.curvature_grid(tenth)
        report["full_value_sampling_definition"] = copy.deepcopy(grid)
        bounded = problem.original_problem.base
        order = int(bounded.primitive_order)
        transfer.require(order == 8 and order == int(bounded.fixed_primitive.order),
                         "same authoritative query/fixed primitive order required")
        gate, gate_receipt = original_audit.fresh_adapter_gate(
            gate, problem, initial, lower, upper)
        report["fresh_adapter_original_physical_gate_binding"] = gate_receipt
        report["original_query_quadrature_order"] = {
            "value": order, "source": "problem.original_problem.base.primitive_order",
            "same_fixed_primitive_order": True}
        def checkpoint(snapshot):
            report[STAGE] = {"status": "last-actual-qualified-checkpoint",
                             "checkpoint": snapshot, "solver": {}}
            save_report(output, report)
        objective = TerminalPaidSlotObjective(
            problem, gate, radial, theta, order, lower, upper,
            cfg=cfg, checkpoint=checkpoint, radial_nodes_exact=grid["radial_nodes_exact"],
            replay=replay, scientific_started=scientific_started,
            terminal_paid_slot_policy=POLICY, coarse_pool=coarse_pool, fine_pool=fine_pool)
        report["timing_segments"]["terminal_constructor_seconds"] = time.monotonic()-constructor_started
        report["restored_original_definition_hashes"] = {
            "objective": objective.evaluation_sha256,
            "ordinary_field": objective.factorized.ordinary_evaluation_sha256,
            "factorization": objective.factorized.definition_sha256,
            "configuration": digest(objective.cfg)}
        report["new_recovery_entries"] = 1
        started = time.monotonic()
        stage = run_terminal_paid_slot_recovery(
            objective, initial, restored_controller=replay["controller_continuation"])
        report[STAGE] = stage
        report["timing_segments"]["terminal_restore_model_and_trial_seconds"] = time.monotonic()-started
        point = stage["checkpoint"].get("selected_two_grid_physical_point")
        transfer.require(point is not None, "original exact accepted point must remain available")
        final = exact_vector(point["exact_binary64_independent_coordinates"], 159)
        transfer.require(
            np.array_equal(final, np.asarray(point["independent_coordinates_binary64"], float))
            and [str(x) for x in problem.coordinates.physical_exact(final)] ==
                point["exact_original_physical_coefficients"]
            and digest(problem.identity(final)) == point["physical_state_sha256"],
            "selected exact159/mapped163/physical identity differs")
        exact_box = problem.coordinates.exact_box_decision(final, gate.original_lower, gate.original_upper)
        transfer.require(exact_box["exact_original_box_pass"] is True,
                         "selected exact original163 coupled box failed")
        copied, copied_state = problem.frozen_metric_copy(final)
        transfer.require(copied is problem and copied_state.tobytes() == final.tobytes()
                         and copied.identity(copied_state) == problem.identity(final)
                         and copied.metric_model(copied_state) == problem.metric_model(initial)
                         and copied.height_base_definition == problem.height_base_definition,
                         "fixed g/b0/live reference/map changed")
        coarse, fine, owner = final_receipts(stage, point, replay)
        flags = {label: d["actual_gate_booleans"] for label, d in (("coarse", coarse), ("fine", fine))}
        transfer.require(all(len(v) == 14 and all(x is True for x in v.values()) for v in flags.values()),
                         "final two-grid14 original actual gates required")
        transfer.require(all(d["direct_max_eta"] == point[label]["direct_max_eta"]
                             for label, d in (("coarse", coarse), ("fine", fine))),
                         "final full gate receipt and selected scalar differ")
        maximum = max(coarse["direct_max_eta"], fine["direct_max_eta"])
        source_maximum = replay["original_current_point"]["maximum_eta_on_both_grids"]
        report["final_selection_validation"] = {
            "both_value_grids_hard_and_old_metric_pass": True, "exact_original_box_pass": True,
            "source_current_both_grid_maximum_eta": source_maximum,
            "both_grid_maximum_eta": maximum,
            "both_grid_maximum_curvature": max(coarse["direct_maximum_absolute_principal_curvature"],
                                               fine["direct_maximum_absolute_principal_curvature"]),
            "new_actual_eta_decrease": source_maximum-maximum,
            "new_metric_target_qualified_on_both_grids": point["new_metric_target_qualified_on_both_grids"],
            "source_current_state_unchanged": point["physical_state_sha256"] == transfer.IDENTITIES["physical"],
            "accepted_index": point["accepted_index"], "not_a_new_independent_final_geometry_audit": True}
        report["final_full_grid_constraints"], report["final_doubled_constraints"] = coarse, fine
        report["final_actual_gate_booleans"] = flags
        report["selected_gate_receipt_source"], report["final_exact_box"] = owner, exact_box
        report["future_direct_checkpoint"] = original_audit.new_checkpoint(objective, problem, point, stage)
        report["future_direct_checkpoint"]["selected_accepted_index"] = point["accepted_index"]
        report["future_direct_checkpoint"]["terminal_paid_slot_continuation"] = {
            "policy": POLICY, "source": copy.deepcopy(transfer.PINS),
            "old63_calls_not_reexecuted": True,
            "new_calls_started": stage["new_LPs_started_this_attempt"],
            "same_task_cumulative_counts_not_new_epoch": True,
            "original_source_accepted_index": 27,
            "new_candidate_exact_step_saved_separately": True}
        report["new_candidate_step_record"] = copy.deepcopy(stage.get("new_candidate_step_record"))
        report["final_value_ledger"] = {
            "source_shared_values": 58, "cumulative_shared_values": objective.full_value_evaluations,
            "new_shared_values": objective.full_value_evaluations-58,
            "cumulative_coarse_values": objective.geometry_evaluations,
            "cumulative_fine_values": objective.fine_evaluations,
            "new_coarse_values": objective.geometry_evaluations-29,
            "new_fine_values": objective.fine_evaluations-29,
            "unchanged_shared_cap": 160, "new_independent_final_calls": 0}
        report["terminal_bank_and_pools"] = {
            "source_entries": 512, "terminal_entries": len(objective.direction_bank.entries),
            "source_state_sha256": transfer.IDENTITIES["bank"],
            "terminal_state_sha256": objective.direction_bank.state_digest(),
            "old_four_supplements_still_separate": len(objective.supplemental_normals) == 4,
            "pool_counts": [len(objective.pool), len(objective.fine_pool)],
            "pool_versions": [objective.pool_version, objective.fine_pool_version],
            "source_learning_state_sha256": transfer.IDENTITIES["learning"],
            "terminal_learning_state_sha256": objective.curvature_defect_memory.state_record()["state_sha256"],
            "pending_learning_events": len(objective.curvature_defect_memory.pending)}
        report["status"] = COMPLETE if not stage.get("error") else "terminal-slot-error-best-retained"
    except Exception as error:
        report["status"] = "terminal-paid-slot-audit-error"
        report["error"] = {"type": type(error).__name__, "message": str(error),
                           "traceback": traceback.format_exc()}
        if objective is not None:
            report.setdefault(STAGE, {"solver": {}})
            report[STAGE]["checkpoint"] = objective.snapshot()
    if objective is not None:
        models = objective.complete_models
        support_record = (getattr(models[-1], "terminal_paid_support_record", None)
                          if models else None)
        provenance = (None if support_record is None else {
            key: copy.deepcopy(support_record[key]) for key in (
                "schema", "rows", "binding", "append", "paid_direction_sha256",
                "paid_attainers_sha256", "witnesses",
                "same_original_affine_objective_and_frozen_guard",
                "no_old_direction_or_old_primary_reexecution",
                "no_old_numeric_A_b_restored_without_current_rebuild",
                "floating_assembly_is_not_an_interval_certificate")})
        if "future_direct_checkpoint" in report:
            report["future_direct_checkpoint"]["terminal_paid_slot_continuation"][
                "prepared_support_provenance"] = provenance
        else:
            report["prepared_support_provenance"] = provenance
        report["direct_reference_geometry_timing"] = objective.problem.timing_snapshot()
    save_report(output, report)
    emit_result(report)
    return report


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
    paid_first_attempt = None
    try:
        transfer.require(request["parameters"]["policy"] == POLICY, "explicit terminal-slot request required")
        for path, expected in request["source_sha256"].items():
            transfer.require(reader.digest(Path(path).read_bytes()) == expected,
                             "requested source changed: "+path)
        requested_python = {Path(path).name: sha for path, sha in request["source_sha256"].items()
                            if path.endswith(".py")}
        transfer.require(requested_python == implementation_hashes() and len(requested_python) == 158,
                         "old152 plus exactly six new Python files required")
        emit("REQUEST", {
            "source_commit": os.environ.get("GITHUB_SHA"),
            "request_bytes": len(raw_request), "request_sha256": reader.digest(raw_request),
            "source_sha256": request["source_sha256"], "parameters": request["parameters"]})
        # Start before either paid failure or original source is read.
        # The old eleven verdicts are consumed, never executed again.
        current_scientific_started = time.monotonic()
        scientific_started = current_scientific_started-transfer.INHERITED_SCIENCE_SECONDS
        reuse_read_started = time.monotonic()
        paid_first_attempt = transfer.read_paid_first_attempt(
            request, scientific_started=scientific_started)
        reuse_read_seconds = time.monotonic()-reuse_read_started
        development_receipt = copy.deepcopy(paid_first_attempt)
        emit("DEVELOPMENT_REUSED", development_receipt)
        source_read_started = time.monotonic()
        completed = transfer.read_completed(request, scientific_started=scientific_started)
        source_read_seconds = time.monotonic()-source_read_started
        emit("PRIOR_WORK_REUSED", completed[3])
        input_started = time.monotonic()
        prepared = transfer.prepare_transfer(
            request, output, PROCESS_STARTED, completed=completed,
            scientific_started=scientific_started, paid_first_attempt=paid_first_attempt)
        segments = {
            "original_source_cumulative_scientific_seconds": SOURCE_SCIENCE_SECONDS,
            "already_paid_cumulative_scientific_seconds": transfer.INHERITED_SCIENCE_SECONDS,
            "current_failed_attempt_receipt_read_and_validation_seconds": reuse_read_seconds,
            "current_source_log_read_and_validation_seconds": source_read_seconds,
            "current_necessary24_input_and_immutable_prepare_seconds": time.monotonic()-input_started,
            "current_scientific_input_prepare_seconds": time.monotonic()-current_scientific_started,
            "new_development_seconds_separate_from_science": 0,
            "new_development_group_and_case_executions": 0,
            "first_failure_process_and_development_cost_only_in_paid_receipt": True,
            "current_process_before_scientific_start_including_import":
                current_scientific_started-PROCESS_STARTED,
            "old_failed_attempt_costs_already_inside257_seconds_not_added_twice": True,
            "closed_old_m7_epoch_costs_remain_separate_ancestor_history": True}
        result = run_audit(
            prepared, output, scientific_started=scientific_started,
            segments=segments, development_receipt=development_receipt)
    except Exception as error:
        result = {
            "schema": SCHEMA, "status": "terminal-paid-slot-input-or-development-error",
            "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
            "github_repository": os.environ.get("GITHUB_REPOSITORY"),
            "source_files_sha256": implementation_hashes(),
            "development_receipt": copy.deepcopy(development_receipt),
            "scientific_started_monotonic": scientific_started,
            "same_task_inherited_science_seconds": transfer.INHERITED_SCIENCE_SECONDS,
            "original_source_scientific_seconds": SOURCE_SCIENCE_SECONDS,
            "paid_first_attempt_receipt": copy.deepcopy(paid_first_attempt),
            "same_task_inherited_ledger": {"linear_program_invocation_count": 63,
                "primary_LP_invocation_count": 62, "correction_LP_invocation_count": 1},
            "same_task_inherited_values": 58,
            "new_values_J_LPs_or_accepted_points_before_input_ready": 0,
            "error": {"type": type(error).__name__, "message": str(error),
                      "traceback": traceback.format_exc()}}
        save_report(output, result)
        emit_result(result)
    for path in sorted(output.parent.glob("*.json")):
        data = path.read_bytes()
        emit("OUTPUT_METADATA", {"filename": path.name, "bytes": len(data),
             "sha256": reader.digest(data), "payload_repository_artifact_upload": False})
    return 0 if result.get("status") == COMPLETE else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Public Actions entry: paid checks reused, then at most LP11 and original SOC12.

The source guard epoch is never restarted. All paid counters, current438 bank,
both pools, frozen seventh-model guard, exact159/reference163 and immutable g/b0
are retained. A current-cache restoration is charged as new work. Existing
accepted-value receipts suffice for this continuation report; no extra final
geometry audit or already-paid development is mechanically repeated.
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
from frame_curvature_soc_metric_reserve_audit import exact_vector
from frame_metric_budget_recovery import require_public_research_environment
from frame_metric_height159_soc_hold import compact_with_all_actual_gates
from frame_metric_paid_attainer_refinement import POLICY, definition
from frame_metric_paid_attainer_resume import PaidAttainerResumeObjective
from frame_metric_paid_attainer_recovery import run_paid_attainer_resume_recovery
import frame_metric_paid_attainer_transfer as transfer
import frame_metric_curvature_defect_guard_audit as original_audit
import read_original_actions_log as reader

SCHEMA = POLICY+"-audit"
STAGE = "paid_attainer_refinement_stage"
COMPLETE = "complete-paid-attainer-mid-epoch-refinement-audit"
NEW_SOURCES = (
    "frame_metric_paid_attainer_refinement.py",
    "frame_metric_paid_attainer_refinement_development.py",
    "frame_metric_paid_attainer_resume.py",
    "frame_metric_paid_attainer_transfer.py",
    "frame_metric_paid_attainer_recovery.py",
    "frame_metric_paid_attainer_audit.py")


def implementation_hashes():
    result = original_audit.implementation_hashes()
    folder = Path(__file__).parent
    for name in NEW_SOURCES:
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def emit(tag, value):
    print(tag+" "+reader.encoded(value).decode("utf-8"), flush=True)


def small_summary(report):
    result = {k: copy.deepcopy(v) for k, v in report.items()
              if k not in (STAGE, "exact_input_storage")}
    stage = report.get(STAGE, {})
    result[STAGE] = {k: copy.deepcopy(v) for k, v in stage.items()
                     if k not in ("checkpoint", "solver")}
    result[STAGE]["solver"] = {
        k: copy.deepcopy(v) for k, v in stage.get("solver", {}).items() if k != "models"}
    result[STAGE]["model_count"] = len(stage.get("solver", {}).get("models", []))
    snap = stage.get("checkpoint", {})
    result[STAGE]["selected_two_grid_physical_point"] = copy.deepcopy(
        snap.get("selected_two_grid_physical_point"))
    result[STAGE]["new_accepted_iterates"] = copy.deepcopy(
        snap.get("accepted_iterates", [])[7:])
    result[STAGE]["snapshot_scalar_counters"] = {
        k: copy.deepcopy(snap[k]) for k in (
            "initialization_elapsed_seconds", "optimization_elapsed_seconds",
            "value_geometry_seconds", "total_full_value_physical_evaluations",
            "coarse_physical_evaluations", "fine_physical_evaluations") if k in snap}
    result["complete_original_grid_oracle_progress"] = copy.deepcopy(
        stage.get("complete_original_grid_oracle_progress",
                  snap.get("complete_original_grid_oracle_progress", [])))
    result["factorized_selected_J_execution"] = copy.deepcopy(
        snap.get("selected_row_factorization_statistics"))
    return result


def save_report(output, report):
    now = time.monotonic()
    report["process_total_elapsed_seconds"] = now-report["process_started_monotonic"]
    report["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    atomic_save(output, report)
    atomic_save(Path(output).with_name("audit-summary.json"), small_summary(report))


def emit_result(report):
    for model in report.get(STAGE, {}).get("solver", {}).get("models", []):
        emit("PAID_ATTAINER_MODEL", model)
    emit("PAID_ATTAINER_COMPLETE", small_summary(report))


def run_audit(prepared, output, *, process_started, prepare_seconds):
    restored, bindings, tenth, replay, coarse_pool, fine_pool = prepared
    problem, initial, gate, lower, upper, source_cfg, cfg = restored
    real, source_cp = replay["original_report"], replay["source_checkpoint"]
    inherited_before_current_preparation = copy.deepcopy(replay["inherited_counters"])
    transfer.require(prepare_seconds >= 0, "current preparation duration must be nonnegative")
    replay["inherited_counters"]["initialization_elapsed_seconds"] += prepare_seconds
    report = {
        "schema": SCHEMA, "status": "mid-epoch-restoration-not-yet-started",
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "source_files_sha256": implementation_hashes(), "configuration": copy.deepcopy(cfg),
        "policy_definition": definition(), "exact_input_storage": bindings,
        "process_started_monotonic": process_started, "prepare_elapsed_seconds": prepare_seconds,
        "source_transfer": copy.deepcopy(replay["source_completed_log_transfer"]),
        "source_paid_ledger": copy.deepcopy(replay["inherited_ledger"]),
        "source_paid_value_and_clock_counters": copy.deepcopy(replay["source_snapshot_scalar_counters"]),
        "inherited_combined_counters_before_this_preparation": inherited_before_current_preparation,
        "first_failed_attempt_paid_receipt": copy.deepcopy(replay["paid_first_attempt"]["receipt"]),
        "first_failed_attempt_paid_cost": copy.deepcopy(replay["paid_first_attempt"]["paid_cost"]),
        "this_preparation_charged_to_same_epoch_initialization": True,
        "old_sixteen_development_checks_executed_this_run": 0,
        "old_optimizer_calls_this_run": 0, "old_LP10_or_old_direction_replays": 0,
        "old_development_group_executions": 0, "new_scientific_solver_entry_calls": 0,
        "same_immutable_g_b0_full_reference163_and_current_exact159": True,
        "current438_and_historical_initial375_are_different_epoch_facts": True,
        "same_model_old_rows_frozen_guard_and_two_original_pools_required": True,
        "source_model7_has_no_serialized159_candidate": True,
        "source_final_selection_validation": copy.deepcopy(real["final_selection_validation"]),
        "future_direct_checkpoint": copy.deepcopy(source_cp),
        "timing_segments": {}, "limitations": {
            "finite_original_grid_model_and_actual_gates_only": True,
            "new_metric_target026_is_not_isometry_tolerance1e_6": True,
            "hard_curvature58_is_not_continuous_reach_target": True,
            "no_whole_surface_embedding_or_reach_certificate": True,
            "no_complete_convex_stationarity_claim_on_unclosed_gap": True,
            "no_replayed_old159_candidate_or_old_LP": True}}
    objective = None
    active_restoration_started = time.monotonic()
    try:
        radial, theta, grid = original_audit.curvature_grid(tenth)
        def checkpoint(snapshot):
            report[STAGE] = {"status": "last-qualified-mid-epoch-checkpoint",
                             "checkpoint": snapshot, "solver": {}}
            save_report(output, report)
        objective = PaidAttainerResumeObjective(
            problem, gate, radial, theta, int(source_cfg["primitive_order"]), lower, upper,
            cfg=cfg, checkpoint=checkpoint, radial_nodes_exact=grid["radial_nodes_exact"],
            replay=replay, coarse_pool=coarse_pool, fine_pool=fine_pool,
            active_restoration_started=active_restoration_started)
        report["timing_segments"]["direct_metadata_and_counter_restore_seconds"] = (
            time.monotonic()-active_restoration_started)
        report["restored_evaluation_identities"] = {
            "original_objective_from_both_paid_cache_bindings": replay["epoch_evaluation_sha256"],
            "restored_objective_evaluation_sha256": objective.evaluation_sha256,
            "original_ordinary_field_definition": replay["ordinary_field_evaluation_sha256"],
            "restored_ordinary_field_definition": objective.factorized.ordinary_evaluation_sha256,
            "two_different_hash_domains_each_checked_against_its_original": True}
        report["phase"] = "same-original-model7-on-inherited-shared-ledger"
        report["new_scientific_solver_entry_calls"] = 1
        stage = run_paid_attainer_resume_recovery(
            objective, initial, restored_controller=replay["controller_continuation"])
        report[STAGE] = stage
        report["timing_segments"]["new_restoration_and_original_recovery_path_seconds"] = (
            time.monotonic()-active_restoration_started)
        snap = stage["checkpoint"]
        point = snap.get("selected_two_grid_physical_point")
        if point is None:
            raise ValueError("the inherited actual two-grid qualified point was lost")
        final = exact_vector(point["exact_binary64_independent_coordinates"], 159)
        if (not np.array_equal(final, np.asarray(point["independent_coordinates_binary64"], float))
                or [str(x) for x in problem.coordinates.physical_exact(final)] !=
                    point["exact_original_physical_coefficients"]
                or digest(problem.identity(final)) != point["physical_state_sha256"]):
            raise ValueError("selected exact159 and mapped163 physical identity differ")
        exact_box = problem.coordinates.exact_box_decision(final, gate.original_lower, gate.original_upper)
        if not exact_box["exact_original_box_pass"]:
            raise ArithmeticError("original exact coupled physical box failed")
        metric_before = problem.metric_model(initial)
        frozen, frozen_state = problem.frozen_metric_copy(final)
        if (frozen_state.tobytes() != final.tobytes()
                or frozen.identity(frozen_state) != problem.identity(final)
                or frozen.metric_model(frozen_state) != metric_before
                or frozen.height_base_definition != problem.height_base_definition
                or frozen.coordinate_definition != problem.coordinate_definition):
            raise ArithmeticError("selected-state copy changed permanent g/b0/reference/map")
        unchanged = point["physical_state_sha256"] == source_cp["selected_physical_state_sha256"]
        if unchanged:
            c, f = (copy.deepcopy(real["final_full_grid_constraints"]),
                    copy.deepcopy(real["final_doubled_constraints"]))
            report["selected_gate_receipt_source"] = {
                "kind": "paid-independent-final-original-two-grid-records",
                "source_run_id": transfer.SOURCE_RUN,
                "source_physical_state_sha256": point["physical_state_sha256"]}
            gate_flags = {label: compact_with_all_actual_gates(d)["actual_gate_booleans"]
                          for label, d in (("coarse", c), ("fine", f))}
        else:
            hits = [(model["number"], i, trial)
                    for model in stage["solver"]["models"]
                    for i, trial in enumerate(model["trials"])
                    if trial.get("accepted_as_next_iterate") is True
                    and trial.get("accepted_index") == point["accepted_index"]
                    and trial.get("physical_state_sha256") == point["physical_state_sha256"]]
            if len(hits) != 1:
                raise ValueError("one exact new accepted trial must own final full gate receipts")
            model_number, trial_index, trial = hits[0]
            c, f = copy.deepcopy(trial["coarse_decision"]), copy.deepcopy(trial["fine_decision"])
            gate_flags = {"coarse": c["actual_gate_booleans"], "fine": f["actual_gate_booleans"]}
            report["selected_gate_receipt_source"] = {
                "kind": "new-complete-original-two-grid-accepted-trial",
                "model_number": model_number, "trial_index": trial_index,
                "accepted_index": point["accepted_index"],
                "physical_state_sha256": point["physical_state_sha256"]}
        if any(len(flags) != 14 or not all(v is True for v in flags.values())
               for flags in gate_flags.values()):
            raise ArithmeticError("one of the fourteen original actual gate receipts failed")
        report["final_actual_gate_booleans"] = copy.deepcopy(gate_flags)
        if any(d["direct_max_eta"] != point[label]["direct_max_eta"]
               for label, d in (("coarse", c), ("fine", f))):
            raise ArithmeticError("full gate receipts disagree with selected accepted-point maxima")
        eligible = bool(c["single_grid_admissible_recovery_point"]
                        and f["single_grid_admissible_recovery_point"])
        if not eligible:
            raise ArithmeticError("selected accepted-value receipts lost an original gate")
        maximum = max(c["direct_max_eta"], f["direct_max_eta"])
        report["final_selection_validation"] = {
            "both_value_grids_hard_and_old_metric_pass": eligible,
            "both_grid_maximum_eta": maximum,
            "initial_both_grid_maximum_eta": real["final_selection_validation"]["both_grid_maximum_eta"],
            "actual_eta_decrease": real["final_selection_validation"]["both_grid_maximum_eta"]-maximum,
            "both_grid_maximum_curvature": max(c["direct_maximum_absolute_principal_curvature"],
                                               f["direct_maximum_absolute_principal_curvature"]),
            "new_metric_target_qualified_on_both_grids":
                bool(c["single_grid_new_target_qualified"] and f["single_grid_new_target_qualified"]),
            "exact_original_physical_box_checked_without_clipping": True,
            "actual_complete_value_receipts_retained_from_each_accepted_point": True,
            "extra_independent_final_geometry_or_optimizer_calls": 0,
            "unchanged_source_best_uses_its_paid_final_independent_two_grid_receipt":
                point["physical_state_sha256"] == source_cp["selected_physical_state_sha256"],
            "whole_surface_reach_not_certified": True}
        report["final_full_grid_constraints"] = copy.deepcopy(c)
        report["final_doubled_constraints"] = copy.deepcopy(f)
        report["final_exact_height_diagnostic"] = original_audit.exact_height_diagnostic(problem, final)
        report["future_direct_checkpoint"] = {
            "reference_complete163_binary64_exact": [
                str(Q.from_float(float(x))) for x in problem.coordinates.reference_state],
            "coordinate_definition": copy.deepcopy(problem.coordinate_definition),
            "selected_final159_binary64_exact": point["exact_binary64_independent_coordinates"],
            "selected_final163_physical_exact": point["exact_original_physical_coefficients"],
            "selected_physical_state_sha256": point["physical_state_sha256"],
            "coarse_pool": objective.pool.tolist(), "fine_pool": objective.fine_pool.tolist(),
            "coarse_pool_version": objective.pool_version, "fine_pool_version": objective.fine_pool_version,
            "terminal_trust": stage["last_restricted_trust"],
            "terminal_success_streak": stage["final_consecutive_growth_qualifying_models"],
            "terminal_covered_ordinary_growth_streak": stage["final_covered_ordinary_growth_streak"],
            "curvature_defect_guard_learning_checkpoint": copy.deepcopy(
                stage["curvature_defect_guard_learning_checkpoint"]),
            "norm_direction_bank_context": copy.deepcopy(objective.direction_bank.context),
            "norm_direction_bank_entries": copy.deepcopy(list(objective.direction_bank.entries.values())),
            "norm_direction_bank_state_sha256": objective.direction_bank.state_digest(),
            "same_original_epoch_ledger": copy.deepcopy(stage["actual_ledger_after"]),
            "same_original_epoch_active_seconds": time.monotonic()-objective.optimization_started,
            "same_original_epoch_shared_values": objective.full_value_evaluations,
            "all_values_are_original_runner_output_not_committed_payload": True}
        report["value_evaluation_counts"] = {
            "inherited_shared_values": 14, "new_shared_values": objective.full_value_evaluations-14,
            "current_shared_values": objective.full_value_evaluations, "shared_cap": 40,
            "inherited_independent_final_value_calls": 2,
            "new_independent_final_value_calls": 0,
            "new_directional_scans_and_selected_J_reported_separately": True,
            "restoration_values_are_new_paid_calls_not_cache_hits": True}
        report["status"] = (COMPLETE if not stage.get("error") else
                            "paid-attainer-recovery-error-paid-best-preserved")
    except Exception as error:
        report["error"] = {"type": type(error).__name__, "message": str(error),
                           "traceback": traceback.format_exc()}
        report["status"] = "paid-attainer-audit-error-paid-best-preserved"
        report["timing_segments"]["restoration_or_recovery_wall_until_error_seconds"] = (
            time.monotonic()-active_restoration_started)
        if objective is not None:
            report["actual_counters_at_error"] = {
                "new_shared_values": objective.full_value_evaluations-14,
                "current_shared_values": objective.full_value_evaluations,
                "combined_active_seconds": time.monotonic()-objective.optimization_started}
    save_report(output, report)
    emit_result(report)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    require_public_research_environment()
    process_started = time.monotonic()
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    request = json.loads(Path(args.request).read_text(encoding="utf-8"))
    try:
        paid_first_attempt = transfer.read_paid_first_attempt(request)
        emit("PAID_ATTAINER_DEVELOPMENT_REUSE", paid_first_attempt["receipt"])
        completed = transfer.read_completed(request)
        emit("PAID_ATTAINER_PRIOR_WORK_REUSED", completed[-1])
        prepare_started = time.monotonic()
        prepared = transfer.prepare_transfer(
            request, output, process_started, completed=completed,
            paid_first_attempt=paid_first_attempt)
        prepare_seconds = time.monotonic()-prepare_started
        result = run_audit(prepared, output, process_started=process_started,
                           prepare_seconds=prepare_seconds)
        return 0 if result["status"] == COMPLETE else 1
    except Exception as error:
        report = {"schema": SCHEMA, "status": "source-transfer-or-entry-error-no-repeat",
                  "process_started_monotonic": process_started,
                  "error": {"type": type(error).__name__, "message": str(error),
                            "traceback": traceback.format_exc()},
                  "source_files_sha256": implementation_hashes()}
        save_report(output, report)
        emit("PAID_ATTAINER_ENTRY_ERROR", report)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

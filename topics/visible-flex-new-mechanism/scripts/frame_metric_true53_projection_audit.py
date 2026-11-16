#!/usr/bin/env python3
"""One new accepted53 complete-grid projected direction; all cost begins here."""
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
import sys
import traceback
import numpy as np
from frame_collar_bvp import atomic_save
from frame_height_null_coordinates import digest
from frame_curvature_soc_metric_reserve_audit import exact_vector
from frame_metric_budget_recovery import EvaluationBudgetReached, require_public_research_environment
import read_original_actions_log as reader
import frame_metric_p32_line_audit as inherited_audit
import frame_metric_final_cone32_audit as original_audit
from frame_metric_complete_maximin_projection import (
    ProjectionLedger, ProjectionLimit, LIMITS, ALGORITHM, require, solve_complete_projection)
from frame_metric_true53_projection_model import (
    build_from_current_objective, model_build_report, partial_model_record)
from frame_metric_true53_projection_line import run_guarded_line
from frame_metric_true53_projection_actual import (
    True53ProjectionObjective, run_projected_actual_trials)
from frame_metric_true53_projection_transfer import (
    TOPIC, REPO, POLICY, PINS, SOURCE_REQUEST, PUBLISHED_NOTE, read_source, prepare,
    SOURCE_PHYSICAL_SHA, SOURCE_ACCEPTED_INDEX, SOURCE_GLOBAL_SECONDS,
    SOURCE_CLOSED_CONE_SECONDS, SOURCE_ORIGINAL_VALUES)


SCHEMA = POLICY+"-audit"
STAGE = "projection_actual_stage"
COMPLETE = "complete-current53-projected-direction-and-original-gate-audit"
TAG = "TRUE53_PROJECTION_"
NEW_SOURCES = (
    "frame_metric_complete_maximin_projection.py", "frame_metric_true53_projection_model.py",
    "frame_metric_true53_projection_line.py", "frame_metric_true53_projection_development.py",
    "frame_metric_true53_projection_actual.py", "frame_metric_true53_projection_transfer.py",
    "frame_metric_true53_projection_audit.py", "frame_metric_true53_projection_report.py")


def implementation_hashes():
    result = inherited_audit.implementation_hashes()
    folder = Path(__file__).parent
    for name in NEW_SOURCES:
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def emit(suffix, value):
    raw = reader.encoded(value)
    sys.stdout.write(TAG+suffix+" ")
    sys.stdout.write(raw.decode("utf-8"))
    sys.stdout.write("\n")
    sys.stdout.flush()
    return {"tag": TAG+suffix, "JSON_plus_LF_bytes": len(raw)+1,
            "JSON_plus_LF_sha256": reader.digest(raw+b"\n")}


def emit_unique_cache(payload, report, *, complete, binding_sha256=None):
    require(not report.get("cache_emission_attempted"), "exactly one line-cache emission allowed")
    report["cache_emission_attempted"] = True
    started = time.monotonic()
    try:
        receipt = emit("CACHE", payload)
        receipt.update(complete=bool(complete), binding_sha256=binding_sha256,
                       only_original_plaintext_stdout_not_API_encoding_or_chunking=True,
                       log_retention_to_be_verified_by_the_read_only_report_job=True)
        report["line_cache_stdout_receipt"] = receipt
        return receipt
    except Exception as error:
        report["cache_emission_error"] = {
            "type": type(error).__name__, "message": str(error),
            "partial_stdout_is_not_claimed_a_recoverable_complete_cache": True}
        raise
    finally:
        report["timing_segments"]["cache_serialization_and_stdout_seconds"] = time.monotonic()-started


def selected_receipts(point, stage, completed):
    if point["accepted_index"] == SOURCE_ACCEPTED_INDEX:
        require(point["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
                "unchanged source53 has another physical identity")
        return (copy.deepcopy(completed["gates"]["coarse"]), copy.deepcopy(completed["gates"]["fine"]),
                {"kind": "source53-paid-original-two-grid-gates", "new_geometry_replays": 0})
    found = [trial for trial in stage.get("trials", [])
             if trial.get("accepted_as_next_iterate") is True
             and trial.get("accepted_index") == point["accepted_index"]
             and trial.get("physical_state_sha256") == point["physical_state_sha256"]]
    require(point["accepted_index"] == 54 and len(found) == 1,
            "only one actually accepted new54 can replace source53")
    trial = found[0]
    return (copy.deepcopy(trial["coarse_decision"]), copy.deepcopy(trial["fine_decision"]),
            {"kind": "new-projected-direction-actual-two-grid-trial", "trial_number": trial["number"],
             "model_query_number": trial["model_query_number"]})


def future_checkpoint(prepared, completed, objective, point, report, ledger):
    cp = copy.deepcopy(completed["checkpoint"])
    cp.update(
        schema=POLICY+"-future-direct-checkpoint",
        selected_accepted_index=point["accepted_index"],
        selected_physical_state_sha256=point["physical_state_sha256"],
        selected_two_grid_physical_point=copy.deepcopy(point),
        selected_final159_binary64_exact=copy.deepcopy(point["exact_binary64_independent_coordinates"]),
        selected_final163_physical_exact=copy.deepcopy(point["exact_original_physical_coefficients"]),
        coarse_pool=objective.pool.tolist(), fine_pool=objective.fine_pool.tolist(),
        coarse_pool_version=objective.pool_version, fine_pool_version=objective.fine_pool_version,
        coarse_pool_history=copy.deepcopy(objective.pool_history),
        fine_pool_history=copy.deepcopy(objective.fine_pool_history),
        objective_evaluation_definition=copy.deepcopy(objective.evaluation_definition),
        objective_evaluation_sha256=objective.evaluation_sha256,
        source_scalar_objective_evaluation_sha256=completed["checkpoint"]["objective_evaluation_sha256"],
        cumulative_original_actual_values=objective.value_account()["total_source_plus_new_started_values"],
        cumulative_original_scientific_elapsed_seconds_at_checkpoint=SOURCE_GLOBAL_SECONDS+ledger.elapsed(),
        projection_method_scientific_elapsed_seconds_at_checkpoint=ledger.elapsed(),
        final_FINAL_CLOCK_record_is_later_and_authoritative_for_future_cost=True)
    cp["projection_direction_method"] = {
        "policy": POLICY, "source": copy.deepcopy(PINS),
        "current_model_stdout_receipt": copy.deepcopy(report.get("model_stdout_receipt")),
        "line_cache_receipt": copy.deepcopy(report.get("line_cache_stdout_receipt")),
        "source_model_base_physical_state_sha256": SOURCE_PHYSICAL_SHA,
        "projection_original_record": copy.deepcopy(report.get("projection_result_stdout_receipt")),
        "scalar_optimization_original_record": copy.deepcopy(report.get("scalar_result_stdout_receipt")),
        "full_projection_and_scalar_records_are_in_same_original_stdout": True,
        "source32_and64_permanently_closed": True,
        "ancestor_original_scientific_seconds": SOURCE_GLOBAL_SECONDS,
        "current_ledger_at_checkpoint": ledger.report(),
        "new_method_is_not_source52_affine_or_scalar53_identity": True,
        "passive_bank_gamma_supplemental_and_controller_records_not_retrained": True,
        "future_model_must_explicitly_rebind_its_context": True}
    original = completed["checkpoint"]
    passive = ("norm_direction_bank_context", "norm_direction_bank_counters",
               "norm_direction_bank_entries", "norm_direction_bank_state_sha256",
               "curvature_defect_guard_learning_checkpoint", "all_retained_supplemental_normals",
               "terminal_trust", "terminal_success_streak", "terminal_covered_ordinary_growth_streak")
    require(all(cp[key] == original[key] for key in passive),
            "a passive source bank/learning/controller record changed")
    return cp


def finish_physical_report(prepared, completed, objective, report, ledger):
    problem, gate = prepared["problem"], prepared["gate"]
    stage = report.get(STAGE) or {
        "status": "no-actual-trial-started", "trials": [], "new_acceptances": 0,
        "selected_two_grid_physical_point": copy.deepcopy(objective.accepted_iterates[-1])}
    report[STAGE] = stage
    point = copy.deepcopy(objective.accepted_iterates[-1])
    state = exact_vector(point["exact_binary64_independent_coordinates"], 159)
    require(np.array_equal(state, np.asarray(point["independent_coordinates_binary64"], float))
            and digest(problem.identity(state)) == point["physical_state_sha256"]
            and [str(v) for v in problem.coordinates.physical_exact(state)]
                == point["exact_original_physical_coefficients"],
            "final exact159/physical163 identities differ")
    box = problem.coordinates.exact_box_decision(state, gate.original_lower, gate.original_upper)
    require(box["exact_original_box_pass"] is True, "final original exact163 box failed")
    copied, same = problem.frozen_metric_copy(state)
    require(copied is problem and same.tobytes() == state.tobytes()
            and copied.metric_model(state) == problem.metric_model(prepared["initial"])
            and copied.height_base_definition == problem.height_base_definition,
            "original g/b0/permanent anchor changed")
    coarse, fine, owner = selected_receipts(point, stage, completed)
    flags = {label: value["actual_gate_booleans"]
             for label, value in (("coarse", coarse), ("fine", fine))}
    require(all(len(v) == 14 and all(x is True for x in v.values()) for v in flags.values())
            and all(value["direct_max_eta"] == point[label]["direct_max_eta"]
                    for label, value in (("coarse", coarse), ("fine", fine))),
            "final14 actual gates and their true physical point must agree")
    report.update(
        selected_two_grid_physical_point=point,
        final_full_grid_constraints=coarse, final_doubled_constraints=fine,
        final_actual_gate_booleans=flags, final_exact_box=box,
        selected_gate_receipt_source=owner,
        final_selection_validation={
            "accepted_index": point["accepted_index"],
            "physical_state_sha256": point["physical_state_sha256"],
            "both_grid_maximum_eta": point["maximum_eta_on_both_grids"],
            "both_grid_maximum_curvature": point["maximum_curvature_on_both_grids"],
            "source_eta": completed["point"]["maximum_eta_on_both_grids"],
            "actual_eta_decrease": completed["point"]["maximum_eta_on_both_grids"]-point["maximum_eta_on_both_grids"],
            "all_original14_gates_and_exact_box_pass": True,
            "new_target_qualified_on_both_grids": point["new_metric_target_qualified_on_both_grids"],
            "new_independent_initial_or_final_geometry_calls": 0},
        actual_value_account=objective.value_account(),
        actual_value_events=copy.deepcopy(objective.actual_value_events),
        execution_receipt=objective.execution_receipt(),
        direct_reference_geometry_timing=problem.timing_snapshot())
    report["future_projection_checkpoint"] = future_checkpoint(
        prepared, completed, objective, point, report, ledger)
    old = completed["checkpoint"]
    report["terminal_information_state"] = {
        "pool_counts": [len(objective.pool), len(objective.fine_pool)],
        "pool_versions": [objective.pool_version, objective.fine_pool_version],
        "bank_entries": len(old["norm_direction_bank_entries"]),
        "bank_state_sha256": old["norm_direction_bank_state_sha256"],
        "learning_state_sha256": old["curvature_defect_guard_learning_checkpoint"]["state_sha256"],
        "learning_events": len(old["curvature_defect_guard_learning_checkpoint"]["events"]),
        "learning_commits": len(old["curvature_defect_guard_learning_checkpoint"]["commits"]),
        "learning_pending": len(old["curvature_defect_guard_learning_checkpoint"]["pending_event_indices"]),
        "passive_state_unchanged": True, "trust": old["terminal_trust"],
        "legacy_streak": old["terminal_success_streak"],
        "covered_streak": old["terminal_covered_ordinary_growth_streak"]}



def emit_unique_model(payload, report, *, complete):
    require(not report.get("model_emission_attempted"), "only one full or partial model record allowed")
    report["model_emission_attempted"] = True
    started = time.monotonic()
    try:
        receipt = emit("MODEL", payload)
        receipt.update(complete=bool(complete),
                       binding_sha256=payload.get("binding_sha256"),
                       original_unencoded_plaintext_stdout_only=True,
                       all_large_arrays_omitted_from_COMPLETE=True)
        report["model_stdout_receipt"] = receipt
        return receipt
    except Exception as error:
        report["model_emission_error"] = {
            "type": type(error).__name__, "message": str(error),
            "incomplete_stdout_not_claimed_a_recoverable_model": True}
        raise
    finally:
        report["timing_segments"]["model_serialization_and_stdout_seconds"] = time.monotonic()-started


def cost_snapshot(ledger, objective, development):
    cost = ledger.report()
    values = objective.value_account() if objective is not None else {
        "new_adapter_geometry_calls_started": 0,
        "necessary_model_geometry_calls_started": 0,
        "new_actual_geometry_calls_started": 0,
        "total_source_plus_new_started_values": SOURCE_ORIGINAL_VALUES}
    cost.update(
        ancestor_original_scientific_seconds=SOURCE_GLOBAL_SECONDS,
        total_ancestor_plus_new_scientific_seconds=
            SOURCE_GLOBAL_SECONDS+cost["scientific_seconds"],
        closed_cone_task_scientific_seconds_separate_not_added_twice=SOURCE_CLOSED_CONE_SECONDS,
        source_original_full_values=SOURCE_ORIGINAL_VALUES,
        total_source_plus_new_full_values=values["total_source_plus_new_started_values"],
        necessary_new_model_full_values=values["necessary_model_geometry_calls_started"],
        new_actual_full_values=values["new_actual_geometry_calls_started"],
        old_HiGHS_calls_closed=64, old_cone_calls_closed=32,
        new_ordinary_values_include_necessary_current_model_geometry=True,
        development_phase=copy.deepcopy(development),
        development_time_is_inside_science_not_added_twice=True,
        new_development_solver_counts_are_separate_from_production_counts=True,
        all_started_failed_calls_and_serialization_use_this_clock=True,
        nonpreemptive_elapsed_is_not_clipped_to600=True)
    return cost


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    require_public_research_environment()
    ledger = ProjectionLedger(PROCESS_STARTED)
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": SCHEMA, "status": "new-current53-projection-not-yet-started",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "source_files_sha256": implementation_hashes(),
        "source32_and64_permanently_closed": True, "old_checks_executed": 0,
        "timing_segments": {}, "projection": None, "scalar_optimization": None,
        "model_emission_attempted": False, "cache_emission_attempted": False,
        "full_model_and_line_cache_only_in_original_stdout_not_repeated_in_COMPLETE": True}
    completed = prepared = objective = model = handle = envelope = None
    build_capture = {}
    development = {"started": False, "completed": False, "seconds": 0.}
    try:
        ledger.check()
        raw_request = Path(args.request).read_bytes()
        request = json.loads(raw_request)
        parameters = request["parameters"]
        require(parameters["policy"] == POLICY and parameters["limits"] == LIMITS
                and parameters["algorithm"] == ALGORITHM
                and parameters["development_case_count"] == 3
                and parameters["development_seconds_within_science"] == 30
                and parameters["old_checks_executed"] == 0
                and parameters["ancestor_final_original_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
                and parameters["source_original_actual_values"] == SOURCE_ORIGINAL_VALUES
                and parameters["new_science_includes_development"] is True,
                "the new independent600/12prox/24separation/96row/64query/3pair scope differs")
        for path, expected in request["source_sha256"].items():
            require(reader.digest(Path(path).read_bytes()) == expected,
                    "requested source changed: "+path)
        py = {Path(path).name: expected for path, expected in request["source_sha256"].items()
              if path.endswith(".py")}
        require(py == implementation_hashes() and len(py) == 184
                and len(request["source_sha256"]) == 212,
                "all paid200 sources plus eight new Python/four provenance bindings required")
        require(request["new_python_sources"] == [TOPIC+"/scripts/"+name for name in NEW_SOURCES],
                "new module declaration differs")
        emit("REQUEST", {
            "source_commit": os.environ.get("GITHUB_SHA"),
            "request_bytes": len(raw_request), "request_sha256": reader.digest(raw_request),
            "source_sha256": request["source_sha256"], "parameters": parameters})
        tick = time.monotonic()
        development["started"] = True
        try:
            from frame_metric_true53_projection_development import developer_check
            dev = developer_check()
            report["new_development"] = dev
            development["completed"] = bool(dev["all_passed"])
            development["new_case_count"] = dev["executed_case_count"]
        finally:
            development["seconds"] = time.monotonic()-tick
            report["timing_segments"]["new_development_seconds_inside600"] = development["seconds"]
        emit("DEVELOPMENT", dev)
        require(development["completed"] is True and development["new_case_count"] == 3
                and development["seconds"] <= 30, "new three-case development did not complete")
        ledger.check()
        tick = time.monotonic()
        try:
            completed = read_source(request, ledger)
        finally:
            report["timing_segments"]["paid53_source_read_seconds"] = time.monotonic()-tick
        report["paid_source_receipt"] = copy.deepcopy(completed["receipt"])
        emit("PRIOR_WORK_REUSED", completed["receipt"])
        tick = time.monotonic()
        try:
            prepared = prepare(request, output, completed, ledger, process_started=PROCESS_STARTED)
        finally:
            report["timing_segments"]["necessary24_input_prepare_seconds"] = time.monotonic()-tick
        report.update(
            configuration=copy.deepcopy(prepared["cfg"]),
            exact_input_storage_metadata=original_audit.frozen.metadata(prepared["bindings"]),
            source_transfer=copy.deepcopy(prepared["replay"]["source_input_restoration"]),
            full_value_sampling_definition=copy.deepcopy(prepared["grid"]),
            source_current_point=copy.deepcopy(completed["point"]))
        tick = time.monotonic()
        try:
            objective = True53ProjectionObjective(
                prepared["problem"], prepared["gate"], prepared["radial"], prepared["theta"],
                prepared["order"], prepared["lower"], prepared["upper"],
                cfg=prepared["cfg"], checkpoint=None,
                radial_nodes_exact=prepared["grid"]["radial_nodes_exact"],
                replay=prepared["replay"], ledger=ledger,
                coarse_pool=prepared["coarse_pool"], fine_pool=prepared["fine_pool"])
        finally:
            report["timing_segments"]["new_objective_constructor_seconds"] = time.monotonic()-tick
        # These are the one necessary current model's two ordinary caches.
        # No independent repeat of the paid53 acceptance or final audit occurs.
        tick = time.monotonic()
        try:
            coarse = objective.evaluate(objective.vector(prepared["initial"]))
            fine = objective.fine_decision(prepared["initial"])
        finally:
            report["timing_segments"]["necessary_current53_model_values_seconds"] = time.monotonic()-tick
        from frame_metric_height159_soc_hold import compact_with_all_actual_gates
        base_values = {
            "purpose": "necessary-new-current53-hard-model-cache",
            "physical_state_sha256": SOURCE_PHYSICAL_SHA, "accepted_index": SOURCE_ACCEPTED_INDEX,
            "coarse": compact_with_all_actual_gates(coarse["decision"]),
            "fine": compact_with_all_actual_gates(fine),
            "value_account": objective.value_account(),
            "not_an_independent_replay_of_paid53_acceptance": True}
        report["necessary_current_model_values"] = base_values
        emit("BASE_VALUES", base_values)
        source_binding = {
            "source": copy.deepcopy(PINS), "physical_state_sha256": SOURCE_PHYSICAL_SHA,
            "accepted_index": SOURCE_ACCEPTED_INDEX,
            "ordinary_field_evaluation_sha256": completed["checkpoint"]["ordinary_field_evaluation_sha256"],
            "source_factorization_definition_sha256": completed["checkpoint"]["factorization_definition_sha256"],
            "source_objective_evaluation_sha256": completed["checkpoint"]["objective_evaluation_sha256"],
            "same_current159_reference163_and_actual53_pool_versions": True}
        memory = completed["checkpoint"]["curvature_defect_guard_learning_checkpoint"]
        frozen = {"coefficients": copy.deepcopy(memory["coefficients"]),
                  "state_sha256": memory["state_sha256"]}
        tick = time.monotonic()
        try:
            model = build_from_current_objective(
                objective, prepared, ledger, frozen_learning=frozen,
                source_binding=source_binding, capture=build_capture)
        finally:
            report["timing_segments"]["new_complete53_model_build_seconds"] = time.monotonic()-tick
        projection = {}
        report["projection"] = projection
        tick = time.monotonic()
        try:
            handle, _ = solve_complete_projection(
                model, ledger, result_sink=projection,
                emit=lambda record: emit("PROJECTION_EVENT", record))
        finally:
            report["timing_segments"]["one_new_projection_session_seconds"] = time.monotonic()-tick
        report["projection_result_stdout_receipt"] = emit("PROJECTION_RESULT", projection)
        # Include every newly added gradient and the retained selected J exactly
        # once after this session; the later scalar line reuses its final scan.
        emit_unique_model(model.full_record(), report, complete=True)
        ledger.check()
        if handle is not None:
            scalar = {}
            report["scalar_optimization"] = scalar
            best, _, envelope = run_guarded_line(
                model, handle, ledger,
                publish_cache=lambda payload: emit_unique_cache(
                    payload, report, complete=True, binding_sha256=payload["binding_sha256"]),
                emit_query=lambda record: emit("QUERY", record), progress=scalar)
            report["scalar_result_stdout_receipt"] = emit("SCALAR_RESULT", scalar)
            stage = run_projected_actual_trials(
                objective, prepared["initial"], model, handle, envelope, best,
                query_emitter=lambda record: emit("QUERY", record),
                trial_emitter=lambda record: emit("TRIAL", record))
            report[STAGE] = stage
        else:
            report[STAGE] = {
                "status": "no-qualified-direction-no-scalar-or-actual-trial",
                "trials": [], "new_acceptances": 0,
                "source_accepted_index": SOURCE_ACCEPTED_INDEX}
        stage = report[STAGE]
        report["status"] = (COMPLETE if "error" not in projection and stage.get("error") is None
                            else "new-projection-direction-or-actual-error")
    except (ProjectionLimit, EvaluationBudgetReached) as error:
        report.update(status="new-projection-science-or-operation-budget-exit",
                      budget_message=str(error),
                      budget_counter=getattr(error, "kind", "inherited-value-guard"))
    except Exception as error:
        report.update(status="new-projection-input-development-model-or-report-error",
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
    finally:
        if build_capture:
            report["model_build"] = model_build_report(build_capture)
        if model is not None:
            report["model_progress"] = model.report()
        if (model is not None or build_capture) and not report.get("model_emission_attempted"):
            try:
                payload = model.full_record() if model is not None else partial_model_record(build_capture)
                emit_unique_model(payload, report, complete=model is not None)
            except Exception as error:
                report["partial_model_reporting_error"] = {
                    "type": type(error).__name__, "message": str(error)}
        if envelope is not None:
            report["all_queries"] = copy.deepcopy(envelope.records)
        else:
            scalar = report.get("scalar_optimization")
            report["all_queries"] = copy.deepcopy(
                scalar.get("all_query_records", []) if isinstance(scalar, dict) else [])
        if objective is not None:
            if objective.validation_trace is not None:
                report[STAGE] = objective.validation_trace
            try:
                finish_physical_report(prepared, completed, objective, report, ledger)
            except Exception as error:
                report["final_receipt_error"] = {
                    "type": type(error).__name__, "message": str(error),
                    "traceback": traceback.format_exc()}
                report["status"] = "new-projection-final-receipt-error"
                report["partial_true_accepted_records"] = copy.deepcopy(objective.accepted_iterates)
                report["actual_value_account"] = objective.value_account()
                report["actual_value_events"] = copy.deepcopy(objective.actual_value_events)
    report["ledger_before_final_report"] = cost_snapshot(ledger, objective, development)
    report["process_elapsed_before_final_report"] = time.monotonic()-PROCESS_STARTED
    report["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["final_FINAL_CLOCK_tag_is_authoritative_and_later_than_checkpoint"] = True
    try:
        atomic_save(output, report)
        emit("COMPLETE", report)
    except Exception as error:
        report["status"] = "new-projection-final-serialization-error"
        report["final_serialization_error"] = {
            "type": type(error).__name__, "message": str(error), "no_blank_report_overwrite": True}
        emit("REPORTING_ERROR", {
            "error": report["final_serialization_error"], "status": report["status"],
            "ledger": cost_snapshot(ledger, objective, development),
            "model_receipt": report.get("model_stdout_receipt"),
            "cache_receipt": report.get("line_cache_stdout_receipt"),
            "actual_stage": report.get(STAGE),
            "selected_point": report.get("selected_two_grid_physical_point")})
    if output.exists():
        raw = output.read_bytes()
        emit("OUTPUT_METADATA", {"filename": output.name, "bytes": len(raw),
             "sha256": reader.digest(raw), "payload_Git_artifact_release_or_cache_uploads": 0})
    earlier_status, exhausted = report["status"], False
    try:
        ledger.check()
    except (ProjectionLimit, EvaluationBudgetReached) as error:
        exhausted = True
        report["status"] = "new-projection-science-scope-exhausted-at-final-report"
        report["final_budget_message"] = str(error)
    final_clock = {
        "schema": POLICY+"-final-clock", "status_at_final_emit": report["status"],
        "earlier_COMPLETE_status": earlier_status, "scope_exhausted": exhausted,
        "scope_check_after_all_large_output": True,
        "budget_message": report.get("final_budget_message"),
        "this_status_supersedes_earlier_COMPLETE_scope_status": True,
        "ledger": cost_snapshot(ledger, objective, development),
        "process_seconds": time.monotonic()-PROCESS_STARTED,
        "development_is_inside_science_and_reported_as_a_phase_not_added_twice": True,
        "sampled_after_all_large_model_cache_and_complete_serialization_and_emit": True,
        "only_this_final_cost_record_follows_its_time_sample": True}
    emit("FINAL_CLOCK", final_clock)
    return 0 if report.get("status") == COMPLETE else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""One independent first-jet/scalar-line method, with one full stdout cache."""
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
import frame_metric_final_cone32_audit as original_audit
from frame_metric_p32_line_envelope import (
    POLICY, LIMITS, SCALAR_RULE, SOURCE_GLOBAL_SECONDS,
    LineMethodLedger, build_original_first_jet_line, partial_line_record,
    validate_paid_endpoints_and_rows, optimize_scalar_envelope, require)
from frame_metric_p32_line_actual import (
    SOURCE_PHYSICAL_SHA, SOURCE_ACCEPTED_INDEX, ScalarLineActualObjective,
    run_scalar_line_actual_trials)
from frame_metric_p32_line_transfer import (
    TOPIC, REPO, PINS, SOURCE_REQUEST, PUBLISHED_NOTE, read_source, prepare)

SCHEMA = POLICY+"-audit"
STAGE = "p32_scalar_line_stage"
COMPLETE = "complete-two-grid-paid-p32-first-jet-scalar-line-audit"
TAG = "P32_LINE_"
NEW_SOURCES = (
    "frame_metric_p32_line_envelope.py", "frame_metric_p32_line_development.py",
    "frame_metric_p32_line_actual.py", "frame_metric_p32_line_transfer.py",
    "frame_metric_p32_line_audit.py", "frame_metric_p32_line_report.py")


def implementation_hashes():
    result = original_audit.implementation_hashes()
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
                "unchanged source52 has another physical identity")
        return (copy.deepcopy(completed["gates"]["coarse"]), copy.deepcopy(completed["gates"]["fine"]),
                {"kind": "source52-paid-original-two-grid-gates", "new_geometry_replays": 0})
    found = [trial for trial in stage.get("trials", [])
             if trial.get("accepted_as_next_iterate") is True
             and trial.get("accepted_index") == point["accepted_index"]
             and trial.get("physical_state_sha256") == point["physical_state_sha256"]]
    require(point["accepted_index"] == 53 and len(found) == 1,
            "only one actually accepted new53 can replace source52")
    trial = found[0]
    return (copy.deepcopy(trial["coarse_decision"]), copy.deepcopy(trial["fine_decision"]),
            {"kind": "new-scalar-line-actual-two-grid-trial", "trial_number": trial["number"],
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
        source_affine_objective_evaluation_definition=copy.deepcopy(
            completed["checkpoint"]["objective_evaluation_definition"]),
        source_affine_objective_evaluation_sha256=completed["checkpoint"]["objective_evaluation_sha256"],
        cumulative_original_actual_values=ledger.report()["total_source_plus_new_full_values"],
        cumulative_original_scientific_elapsed_seconds_at_checkpoint=
            ledger.report()["total_ancestor_plus_new_scientific_seconds"],
        line_method_scientific_elapsed_seconds_at_checkpoint=ledger.elapsed(),
        final_FINAL_CLOCK_record_is_later_and_authoritative_for_future_cost=True)
    cp["scalar_line_method"] = {
        "policy": POLICY, "source": copy.deepcopy(PINS),
        "source_paid32_raw161_record": copy.deepcopy(completed["raw161_record"]),
        "cache_receipt": copy.deepcopy(report.get("line_cache_stdout_receipt")),
        "cache_base_physical_state_sha256": SOURCE_PHYSICAL_SHA,
        "query_records_are_in_original_QUERY_and_COMPLETE_stdout": True,
        "optimization_result": copy.deepcopy(report.get("scalar_optimization")),
        "source32_and64_permanently_closed": True,
        "ancestor_original_scientific_seconds": SOURCE_GLOBAL_SECONDS,
        "current_ledger_at_checkpoint": ledger.report(),
        "new_line_cache_identity_is_not_an_old_primary_or_ordinary_cache_identity": True,
        "passive_bank_gamma_supplemental_and_controller_records_not_retrained": True,
        "future_model_must_explicitly_rebind_its_context": True,
        "closed_cone_ledger_and_history_carried_as_ancestor_metadata_only": True}
    original = completed["checkpoint"]
    passive = ("norm_direction_bank_context", "norm_direction_bank_counters",
               "norm_direction_bank_entries", "norm_direction_bank_state_sha256",
               "curvature_defect_guard_learning_checkpoint", "all_retained_supplemental_normals",
               "terminal_trust", "terminal_success_streak", "terminal_covered_ordinary_growth_streak")
    require(all(cp[key] == original[key] for key in passive),
            "a passive bank/learning/controller record changed")
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
        zero_selected_J_primary_factory_or_old_solver_execution=objective.zero_derivative_receipt(),
        direct_reference_geometry_timing=problem.timing_snapshot())
    report["future_scalar_line_checkpoint"] = future_checkpoint(
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    require_public_research_environment()
    ledger = LineMethodLedger(PROCESS_STARTED)
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": SCHEMA, "status": "new-line-method-not-yet-started",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "source_files_sha256": implementation_hashes(),
        "source32_and64_permanently_closed": True,
        "old_checks_executed": 0, "timing_segments": {},
        "coefficient_build": None, "scalar_optimization": None,
        "all_queries": [], "cache_emission_attempted": False,
        "full_cache_only_in_original_stdout_not_repeated_in_COMPLETE": True}
    completed = prepared = objective = envelope = None
    build_capture = {}
    try:
        ledger.check()
        raw_request = Path(args.request).read_bytes()
        request = json.loads(raw_request)
        p = request["parameters"]
        require(p["policy"] == POLICY and p["limits"] == LIMITS
                and p["scalar_rule"] == SCALAR_RULE
                and p["development_case_count"] == 3 and p["old_checks_executed"] == 0
                and p["ancestor_final_original_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
                and p["new_science_includes_development"] is True,
                "explicit independent600/64query/3trial/3case contract differs")
        for path, sha in request["source_sha256"].items():
            require(reader.digest(Path(path).read_bytes()) == sha, "requested source changed: "+path)
        py = {Path(path).name: sha for path, sha in request["source_sha256"].items() if path.endswith(".py")}
        require(py == implementation_hashes() and len(py) == 176
                and len(request["source_sha256"]) == 200,
                "old170 plus exactly six new Python sources and complete200 closure required")
        emit("REQUEST", {
            "source_commit": os.environ.get("GITHUB_SHA"),
            "request_bytes": len(raw_request), "request_sha256": reader.digest(raw_request),
            "source_sha256": request["source_sha256"], "parameters": p})
        tick = time.monotonic()
        try:
            from frame_metric_p32_line_development import developer_check
            dev = developer_check()
            report["new_development"] = dev
            ledger.development_completed = bool(dev["all_passed"])
        finally:
            ledger.development_seconds = time.monotonic()-tick
            report["timing_segments"]["development_seconds_inside600"] = ledger.development_seconds
        emit("DEVELOPMENT", dev)
        require(dev["all_passed"] is True and dev["executed_case_count"] == 3
                and ledger.development_seconds <= 30, "new scalar development did not complete")
        ledger.check()
        tick = time.monotonic()
        try:
            completed = read_source(request, ledger)
        finally:
            report["timing_segments"]["paid_source_read_seconds"] = time.monotonic()-tick
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
            source_current_point=copy.deepcopy(completed["point"]),
            source_raw161_and_scaled159_record=copy.deepcopy(completed["raw161_record"]),
            source_paid_endpoint_and_attainer_records=copy.deepcopy(completed["paid_adapter_check"]))
        tick = time.monotonic()
        try:
            objective = ScalarLineActualObjective(
                prepared["problem"], prepared["gate"], prepared["radial"], prepared["theta"],
                prepared["order"], prepared["lower"], prepared["upper"],
                cfg=prepared["cfg"], checkpoint=None,
                radial_nodes_exact=prepared["grid"]["radial_nodes_exact"],
                replay=prepared["replay"], ledger=ledger,
                coarse_pool=prepared["coarse_pool"], fine_pool=prepared["fine_pool"])
        finally:
            report["timing_segments"]["value_only_constructor_seconds"] = time.monotonic()-tick
        source_binding = {
            "source": copy.deepcopy(PINS), "source_physical_state_sha256": SOURCE_PHYSICAL_SHA,
            "source_accepted_index": SOURCE_ACCEPTED_INDEX,
            "source_original_field_evaluation_sha256": completed["checkpoint"]["ordinary_field_evaluation_sha256"],
            "source_factorization_definition_sha256": completed["checkpoint"]["factorization_definition_sha256"],
            "paid_independent_direction_body_array_sha256": completed["receipt"]["source_direction_body_array_digest"],
            "source_raw161_model_binding": copy.deepcopy(completed["raw161_record"]["current_model_binding"]),
            "same_current159_and_reference163_from_the_only_paid_checkpoint": True}
        envelope, event = build_original_first_jet_line(
            prepared["problem"], prepared["initial"], completed["direction"],
            prepared["radial"], prepared["theta"], prepared["row_grids"], prepared["cfg"],
            ledger=ledger, source_binding=source_binding, capture=build_capture)
        report["coefficient_build"] = event
        require(envelope.binding["original_factorization_definition_sha256"]
                    == completed["checkpoint"]["factorization_definition_sha256"]
                and envelope.binding["ordinary_field_evaluation_sha256"]
                    == completed["checkpoint"]["ordinary_field_evaluation_sha256"],
                "first-jet original field/factorizer provenance differs")
        # Serialize the one complete cache before querying or making a true trial.
        receipt = emit_unique_cache(envelope.full_record(), report, complete=True,
                                    binding_sha256=envelope.binding_sha256)
        envelope.mark_full_cache_published(receipt)
        ledger.check()
        scalar = {}
        report["scalar_optimization"] = scalar
        def endpoint_check(zero, one):
            result = validate_paid_endpoints_and_rows(
                envelope, zero, one, completed["paid_adapter_check"], prepared["cfg"])
            emit("ADAPTER_REPLAY", result)
            return result
        best, _ = optimize_scalar_envelope(
            envelope, improvement_floor=float(prepared["cfg"]["linear_model_improvement_floor"]),
            endpoint_validator=endpoint_check, query_emitter=lambda row: emit("QUERY", row),
            progress=scalar)
        emit("SCALAR_RESULT", scalar)
        stage = run_scalar_line_actual_trials(
            objective, prepared["initial"], completed["direction"], envelope, best,
            query_emitter=lambda row: emit("QUERY", row), trial_emitter=lambda row: emit("TRIAL", row))
        report[STAGE] = stage
        report["status"] = COMPLETE if stage.get("error") is None else "scalar-line-actual-stage-error"
    except EvaluationBudgetReached as error:
        report.update(status="scalar-line-new-science-or-query-budget-exit", budget_message=str(error))
    except Exception as error:
        report.update(status="scalar-line-input-development-build-or-report-error",
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
    finally:
        if build_capture:
            report["coefficient_build"] = copy.deepcopy(build_capture.get("event"))
        if envelope is not None:
            report["all_queries"] = copy.deepcopy(ledger.query_events)
            if hasattr(envelope, "paid_validation_receipt"):
                report["paid_adapter_replay"] = copy.deepcopy(envelope.paid_validation_receipt)
        if build_capture and not report.get("cache_emission_attempted"):
            try:
                emit_unique_cache(partial_line_record(build_capture), report, complete=False)
            except Exception as error:
                report["partial_cache_reporting_error"] = {
                    "type": type(error).__name__, "message": str(error)}
        if objective is not None:
            if objective.validation_trace is not None:
                report[STAGE] = objective.validation_trace
            try:
                finish_physical_report(prepared, completed, objective, report, ledger)
            except Exception as error:
                report["final_receipt_error"] = {
                    "type": type(error).__name__, "message": str(error),
                    "traceback": traceback.format_exc()}
                report["status"] = "scalar-line-final-receipt-error"
                report["partial_true_accepted_records"] = copy.deepcopy(objective.accepted_iterates)
                report["actual_value_account"] = objective.value_account()
                report["actual_value_events"] = copy.deepcopy(objective.actual_value_events)
    report["ledger_before_final_report"] = ledger.report()
    report["process_elapsed_before_final_report"] = time.monotonic()-PROCESS_STARTED
    report["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["final_FINAL_CLOCK_tag_is_authoritative_and_later_than_checkpoint"] = True
    try:
        atomic_save(output, report)
        emit("COMPLETE", report)
    except Exception as error:
        report["status"] = "scalar-line-final-serialization-error"
        report["final_serialization_error"] = {
            "type": type(error).__name__, "message": str(error), "no_blank_report_overwrite": True}
        # No second CACHE. Preserve all surviving scalar/trial/cost evidence.
        emit("REPORTING_ERROR", {
            "error": report["final_serialization_error"], "status": report["status"],
            "ledger": ledger.report(), "cache_receipt": report.get("line_cache_stdout_receipt"),
            "scalar_optimization": report.get("scalar_optimization"),
            "actual_stage": report.get(STAGE), "selected_point": report.get("selected_two_grid_physical_point")})
    if output.exists():
        raw = output.read_bytes()
        emit("OUTPUT_METADATA", {"filename": output.name, "bytes": len(raw),
             "sha256": reader.digest(raw), "payload_Git_artifact_release_or_cache_uploads": 0})
    earlier_status = report["status"]
    exhausted = False
    try:
        ledger.check()
    except EvaluationBudgetReached as error:
        exhausted = True
        report["status"] = "scalar-line-science-scope-exhausted-at-final-report"
        report["final_budget_message"] = str(error)
    final_clock = {
        "schema": POLICY+"-final-clock", "status_at_final_emit": report["status"],
        "earlier_COMPLETE_status": earlier_status,
        "scope_exhausted": exhausted,
        "scope_check_after_all_large_output": True,
        "budget_message": report.get("final_budget_message"),
        "this_status_supersedes_earlier_COMPLETE_scope_status": True,
        "ledger": ledger.report(), "process_seconds": time.monotonic()-PROCESS_STARTED,
        "development_is_inside_science_and_reported_as_a_phase_not_added_twice": True,
        "sampled_after_all_large_cache_and_complete_serialization_and_emit": True,
        "only_this_tiny_clock_record_follows_its_time_sample": True}
    emit("FINAL_CLOCK", final_clock)
    return 0 if report.get("status") == COMPLETE else 1


if __name__ == "__main__":
    raise SystemExit(main())

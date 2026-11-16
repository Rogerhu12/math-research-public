#!/usr/bin/env python3
"""Read only this workflow's completed research stdout; no scientific imports.

The full plain coefficient cache stays in the original research log. This
reader emits fingerprints and semantic observations, never an encoded or
chunked substitute for coefficient arrays.
"""
from __future__ import annotations
import time
STARTED = time.monotonic()
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import traceback
import read_original_actions_log as reader

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
POLICY = "same159-paid-p32-first-jet-scalar-envelope-v1"
TAG = "P32_LINE_"
KNOWN = {
    "PUBLIC_PULL", "PRIVATE_PULL", "REQUEST", "DEVELOPMENT", "PRIOR_WORK_REUSED",
    "CACHE", "ADAPTER_REPLAY", "QUERY", "SCALAR_RESULT", "TRIAL", "COMPLETE",
    "REPORTING_ERROR", "FINAL_CLOCK", "OUTPUT_METADATA"}
PATTERN = re.compile(r"\b(P32_LINE_[A-Z_]+)\s+(\{.*\})\s*$")
SEMANTIC_CAP = 480000


def metadata(value):
    raw = reader.encoded(value)
    result = {"JSON_bytes": len(raw), "JSON_sha256": reader.digest(raw)}
    if isinstance(value, (dict, list, tuple, str)):
        result["count"] = len(value)
    return result


def select(value, names):
    if not isinstance(value, dict):
        return value
    return {name: copy.deepcopy(value[name]) for name in names if name in value}


def parse_records(raw):
    rows = []
    for line in raw.decode("utf-8-sig", errors="strict").splitlines():
        match = PATTERN.search(line)
        if match is None:
            continue
        name = match.group(1)[len(TAG):]
        if name not in KNOWN:
            continue
        payload = match.group(2).encode("utf-8")
        value = reader.decode_json(payload)
        rows.append({
            "tag": name, "timestamp_prefix": line[:match.start()].strip(),
            "data": value, "JSON_bytes": len(payload),
            "JSON_sha256": reader.digest(payload),
            "JSON_plus_LF_bytes": len(payload)+1,
            "JSON_plus_LF_sha256": reader.digest(payload+b"\n")})
    return rows


def unique(rows, name, *, required=False):
    matches = [row for row in rows if row["tag"] == name]
    reader.require(len(matches) <= 1, "duplicate original record: "+name)
    reader.require(not required or len(matches) == 1, "missing original record: "+name)
    return matches[0] if matches else None


def small_query(row):
    result = select(row, (
        "query_number", "status", "alpha", "alpha_exact_binary64", "alpha_hex",
        "phi", "positive_slack", "floating_left_slope", "floating_right_slope",
        "cache_binding_sha256", "charged_before_evaluation", "seconds", "error",
        "exact_analytic_active_set_certified", "finite_precision_values_not_an_interval_certificate"))
    if isinstance(row, dict) and "branches" in row:
        result["branches"] = [select(branch, (
            "grid", "group", "maximum", "original_row", "original_point_flat_index",
            "floating_max_equal_count", "floating_active_min_slope", "floating_active_max_slope",
            "attainer_slope")) for branch in row["branches"]]
    return result


def small_trial(row):
    names = (
        "number", "kind", "alpha", "alpha_exact_binary64", "relative_to_first_alpha",
        "model_query_number", "model_gain_at_ideal_alpha_p",
        "actual_rounding_delta_not_substituted_for_ideal_cached_direction",
        "exact_binary64_scaled_paid_direction", "exact_binary64_actual_total_step",
        "exact_binary64_independent_coordinates", "exact_original_physical_coefficients",
        "physical_state_sha256", "accepted_as_next_iterate", "accepted_index",
        "attempt_status", "charged_actual_point",
        "actual_total_step_physical_norms", "restricted_support_invariants",
        "original_exact163_box", "coarse_physical_evaluation", "fine_value_evaluation",
        "coarse_decision", "fine_decision", "actual_acceptance",
        "coarse_omitted_rows", "fine_omitted_rows", "coarse_omitted_hard_rows",
        "fine_omitted_hard_rows", "new_coarse_rows", "new_fine_rows",
        "pool_versions_after_learning", "new_row_or_capacity_stop",
        "learning_used_only_current_actual_value_caches",
        "no_unavailable_J_curvature_gamma_bank_or_growth_feedback")
    result = select(row, names)
    for key in ("added_coarse_rows", "added_fine_rows"):
        if key in row:
            value = row[key]
            result[key] = (select(value, ("added_row_indices", "pool_size", "pool_version", "reason"))
                           if isinstance(value, dict) else value)
            result[key+"_complete_source_metadata"] = metadata(value)
    for key in ("coarse_learning_detail", "fine_learning_detail"):
        if key in row:
            result[key+"_source_metadata"] = metadata(row[key])
    return result


def checkpoint_view(cp):
    if not isinstance(cp, dict):
        return cp
    result = select(cp, (
        "schema", "selected_accepted_index", "selected_physical_state_sha256",
        "selected_final159_binary64_exact", "selected_final163_physical_exact",
        "selected_two_grid_physical_point", "coarse_pool_version", "fine_pool_version",
        "norm_direction_bank_state_sha256", "ordinary_field_evaluation_sha256",
        "objective_evaluation_sha256", "source_affine_objective_evaluation_sha256",
        "factorization_definition_sha256", "terminal_trust", "terminal_success_streak",
        "terminal_covered_ordinary_growth_streak", "cumulative_original_actual_values",
        "cumulative_original_scientific_elapsed_seconds_at_checkpoint",
        "line_method_scientific_elapsed_seconds_at_checkpoint",
        "final_FINAL_CLOCK_record_is_later_and_authoritative_for_future_cost"))
    for key in ("reference_complete163_binary64_exact", "configuration", "coordinate_definition",
                "coarse_pool", "fine_pool", "coarse_pool_history", "fine_pool_history",
                "norm_direction_bank_entries", "norm_direction_bank_context",
                "all_retained_supplemental_normals", "curvature_defect_guard_learning_checkpoint"):
        if key in cp:
            result[key+"_source_metadata"] = metadata(cp[key])
    memory = cp.get("curvature_defect_guard_learning_checkpoint", {})
    result["learning_exact_scalar_state"] = select(memory, (
        "state_sha256", "coefficients", "pending_event_indices", "schema"))
    if isinstance(cp.get("scalar_line_method"), dict):
        result["scalar_line_method"] = select(cp["scalar_line_method"], (
            "policy", "source", "cache_receipt", "cache_base_physical_state_sha256",
            "query_records_are_in_original_QUERY_and_COMPLETE_stdout",
            "source32_and64_permanently_closed", "ancestor_original_scientific_seconds",
            "current_ledger_at_checkpoint",
            "new_line_cache_identity_is_not_an_old_primary_or_ordinary_cache_identity",
            "passive_bank_gamma_supplemental_and_controller_records_not_retrained",
            "future_model_must_explicitly_rebind_its_context",
            "closed_cone_ledger_and_history_carried_as_ancestor_metadata_only"))
    return result


def complete_view(report):
    names = (
        "schema", "status", "github_repository", "github_sha", "github_run_id",
        "source32_and64_permanently_closed", "old_checks_executed", "timing_segments",
        "coefficient_build", "scalar_optimization", "cache_emission_attempted",
        "cache_emission_error", "partial_cache_reporting_error", "line_cache_stdout_receipt",
        "paid_adapter_replay", "final_selection_validation", "selected_two_grid_physical_point",
        "final_full_grid_constraints", "final_doubled_constraints", "final_actual_gate_booleans",
        "final_exact_box", "selected_gate_receipt_source", "terminal_information_state",
        "actual_value_account", "actual_value_events", "direct_reference_geometry_timing",
        "zero_selected_J_primary_factory_or_old_solver_execution",
        "ledger_before_final_report", "process_elapsed_before_final_report", "peak_rss_kib_linux",
        "final_FINAL_CLOCK_tag_is_authoritative_and_later_than_checkpoint",
        "error", "budget_message", "final_receipt_error", "partial_true_accepted_records",
        "source_paid_endpoint_and_attainer_records")
    result = select(report, names)
    for key in ("source_files_sha256", "configuration", "source_raw161_and_scaled159_record",
                "paid_source_receipt", "source_transfer", "full_value_sampling_definition",
                "exact_input_storage_metadata"):
        if key in report:
            result[key+"_original_metadata"] = metadata(report[key])
    stage = report.get("p32_scalar_line_stage")
    if isinstance(stage, dict):
        result["p32_scalar_line_stage"] = select(stage, (
            "schema", "status", "error", "budget_message", "new_acceptances",
            "source_accepted_index", "source_backend_status_preserved",
            "source32_complete_model_did_not_return_a_candidate",
            "new_scalar_model_and_actual_gates_are_separate", "pool_policy",
            "initial_actual_geometry_replays", "value_account", "ledger_at_trial_finish",
            "zero_derivative_or_old_solver_execution", "terminal_trust",
            "terminal_legacy_streak", "terminal_covered_streak",
            "bank_gamma_and_controller_carried_passively_without_unavailable_model_feedback"))
        result["p32_scalar_line_stage"]["trials"] = [small_trial(x) for x in stage.get("trials", [])]
    result["all_queries"] = [small_query(x) for x in report.get("all_queries", [])]
    result["future_checkpoint"] = checkpoint_view(report.get("future_scalar_line_checkpoint"))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    args = parser.parse_args()
    report = {"schema": POLICY+"-read-only-same-workflow-report", "status": "started",
              "scientific_imports_or_recomputations": 0,
              "whole_coefficient_arrays_not_printed_encoded_or_chunked": True}
    try:
        raw_request = Path(args.request).read_bytes()
        request = json.loads(raw_request)
        source, run_id = os.environ["GITHUB_SHA"], os.environ["GITHUB_RUN_ID"]
        reader.require(request["repository"] == REPO, "unexpected repository")
        for path in (TOPIC+"/scripts/frame_metric_p32_line_report.py",
                     TOPIC+"/scripts/read_original_actions_log.py",
                     ".github/workflows/visible-p32-line-envelope.yml"):
            reader.require(reader.digest(Path(path).read_bytes()) == request["source_sha256"][path],
                           "read-only helper/workflow self-binding differs: "+path)
        api = reader.GitHubReader(REPO)
        run = api.api_json("/actions/runs/"+run_id)
        jobs = api.api_json("/actions/runs/"+run_id+"/jobs?per_page=100")
        selected = [job for job in jobs["jobs"] if job["name"] == "research"]
        reader.require(str(run["id"]) == run_id and run["head_sha"] == source
                       and len(selected) == 1, "unique same-source research job required")
        job = selected[0]
        reader.require(str(job["run_id"]) == run_id and job["head_sha"] == source
                       and job["status"] == "completed",
                       "the research job must be complete; its success is not assumed")
        # The workflow itself can still be in_progress because this report is running.
        raw, redirects = api.job_log(str(job["id"]))
        report["source"] = {
            "run_id": run_id, "job_id": str(job["id"]), "source_commit": source,
            "research_status": job["status"], "research_conclusion": job["conclusion"],
            "workflow_status_observed": run["status"],
            "raw_log_bytes": len(raw), "raw_log_sha256": reader.digest(raw),
            "redirects_without_authorization": redirects,
            "read_once_and_not_written_to_Git_artifacts_or_cache": True}
        rows = parse_records(raw)
        report["record_fingerprints"] = [
            {k: v for k, v in row.items() if k != "data"} for row in rows]
        requested = unique(rows, "REQUEST")
        complete = unique(rows, "COMPLETE")
        cache = unique(rows, "CACHE")
        final_clock = unique(rows, "FINAL_CLOCK")
        if requested is not None:
            value = requested["data"]
            reader.require(value["source_commit"] == source
                           and value["request_bytes"] == len(raw_request)
                           and value["request_sha256"] == reader.digest(raw_request)
                           and value["source_sha256"] == request["source_sha256"],
                           "actual source request closure differs")
            report["request"] = {
                "parameters": copy.deepcopy(value["parameters"]),
                "request_bytes": value["request_bytes"], "request_sha256": value["request_sha256"],
                "source_manifest": metadata(value["source_sha256"]),
                "actual_and_current_source_manifest_equal": True}
        else:
            report["request_record_missing"] = True
        for name, target in (("PUBLIC_PULL", "scientific_public_pull"),
                             ("PRIVATE_PULL", "scientific_private_pull"),
                             ("ADAPTER_REPLAY", "paid_adapter_replay"),
                             ("SCALAR_RESULT", "scalar_result"),
                             ("REPORTING_ERROR", "scientific_reporting_error")):
            row = unique(rows, name)
            if row is not None:
                report[target] = copy.deepcopy(row["data"])
        dev = unique(rows, "DEVELOPMENT")
        if dev is not None:
            report["development"] = {k: copy.deepcopy(v) for k, v in dev["data"].items()
                                     if k != "source_files_sha256"}
            report["development"]["source_files_metadata"] = metadata(
                dev["data"].get("source_files_sha256", {}))
        prior = unique(rows, "PRIOR_WORK_REUSED")
        if prior is not None:
            report["prior_work_reused"] = copy.deepcopy(prior["data"])
        if complete is not None:
            value = complete["data"]
            reader.require(value["schema"] == POLICY+"-audit"
                           and value["github_sha"] == source and str(value["github_run_id"]) == run_id,
                           "original COMPLETE identity differs")
            expected_py = {Path(p).name: sha for p, sha in request["source_sha256"].items() if p.endswith(".py")}
            reader.require(value["source_files_sha256"] == expected_py,
                           "actual COMPLETE Python source closure differs")
            report["complete"] = complete_view(value)
        if cache is not None:
            value = cache["data"]
            arrays = value.get("binary64_round_trip_JSON_arrays", {})
            report["line_cache"] = {
                "original_record": {k: v for k, v in cache.items() if k != "data"},
                "schema": value.get("schema"), "status": value.get("status", "complete"),
                "binding_sha256": value.get("binding_sha256"),
                "binding": metadata(value.get("binding", value.get("binding_if_completed_before_error"))),
                "array_metadata": copy.deepcopy(value.get("array_metadata")),
                "available_grids": list(arrays),
                "plain_JSON_array_lengths": {
                    label: {name: len(data) for name, data in items.items()}
                    for label, items in arrays.items()},
                "entire_emitted_cache_record_retained_in_research_stdout": True,
                "cache_values_not_recomputed_or_forwarded_by_this_report": True}
            if complete is not None:
                receipt = complete["data"].get("line_cache_stdout_receipt")
                reader.require(isinstance(receipt, dict)
                               and receipt["JSON_plus_LF_bytes"] == cache["JSON_plus_LF_bytes"]
                               and receipt["JSON_plus_LF_sha256"] == cache["JSON_plus_LF_sha256"],
                               "actual single cache stdout fingerprint differs from its receipt")
                report["line_cache"]["producer_receipt_matches_full_original_record"] = True
        if final_clock is not None:
            report["final_authoritative_clock"] = copy.deepcopy(final_clock["data"])
            report["scientific_scope_status"] = final_clock["data"]["status_at_final_emit"]
        else:
            report["final_authoritative_clock_missing"] = True
            report["scientific_scope_status"] = "unknown-without-final-clock"
        report["native_trial_records"] = [small_trial(row["data"]) for row in rows if row["tag"] == "TRIAL"]
        report["status"] = "read-only-observation-complete"
        report["source_scientific_pass_not_inferred_from_job_conclusion"] = True
    except Exception as error:
        report.update(status="read-only-observation-error",
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
    report["read_only_report_seconds_separate_from_science"] = time.monotonic()-STARTED
    output = reader.encoded(report)
    if len(output) > SEMANTIC_CAP:
        omitted = {}
        # Remove only secondary duplicated query/trial views, never terminal gates,
        # the FINAL_CLOCK, raw-cache fingerprint or actual trial159/163 vectors.
        if isinstance(report.get("complete"), dict):
            old = report["complete"].pop("all_queries", None)
            if old is not None:
                omitted["complete.all_queries"] = metadata(old)
                report["query_table"] = [
                    select(x, ("query_number", "status", "alpha", "phi", "positive_slack",
                               "floating_left_slope", "floating_right_slope", "seconds", "error"))
                    for x in old]
            stage = report["complete"].get("p32_scalar_line_stage", {})
            duplicated = stage.get("trials")
            if duplicated is not None and duplicated == report.get("native_trial_records"):
                stage.pop("trials")
                omitted["complete.p32_scalar_line_stage.trials"] = metadata(duplicated)
        report["priority_output_omissions"] = omitted
        output = reader.encoded(report)
    # If a rare large original error/receipt remains, emit the paid terminal facts
    # rather than replacing them with a content-free LIMIT record.
    report["semantic_output_bytes_before_final_size_field"] = len(output)
    report["semantic_cap_exceeded_after_only_secondary_omissions"] = len(output) > SEMANTIC_CAP
    print("P32_LINE_REPORT_COMPLETE "+reader.encoded(report).decode("utf-8"), flush=True)
    return 0 if report["status"] == "read-only-observation-complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Read the completed direct-reference job once, without scientific imports.

Only bounded original observations and administrative fingerprints reach stdout.
Raw logs, numeric checkpoints, exact states and all arrays remain in memory.
"""
from __future__ import annotations
import argparse
import io
import os
from pathlib import Path
import re
import sys
import time

import read_original_actions_log as reader

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
MODE = "read-only-completed-direct-reference-log-v1"
SOURCE = "a0d71ea94446f0fcf64d1f69e4dbadd5910204ba"
RUN, JOB = "43780594182", "133016656592"
POLICY = "same159-direct-reference-new-task-information-migration-v1"
SCHEMA = POLICY+"-audit"
STAGE = "direct_reference_guarded_task_stage"
STDOUT_CAP = 660000
TEXT_CAP = 1800
TAGS = tuple("DIRECT_REFERENCE_"+x for x in (
    "REQUEST", "PUBLIC_PULL", "PRIVATE_PULL", "DEVELOPMENT",
    "DEVELOPMENT_REUSED", "PRIOR_WORK_REUSED", "MODEL", "COMPLETE",
    "ENTRY_ERROR", "OUTPUT_METADATA", "WORKFLOW_OUTPUT_METADATA"))
STATE_KEYS = {
    "exact_binary64_independent_coordinates", "independent_coordinates_binary64",
    "exact_original_physical_coefficients", "exact_binary64_independent_correction",
    "exact_binary64_actual_y_minus_x", "reference_complete163_binary64_exact",
    "selected_final159_binary64_exact", "selected_final163_physical_exact",
    "coarse_pool", "fine_pool", "row_indices", "added_row_indices",
    "added_original_grid_coordinates", "norm_direction_bank_entries",
    "source_files_sha256", "source_sha256", "modified_original_rows",
    "active_original_rows", "invariant_original_rows", "original_rows",
    "complete_original_soft_row_tags", "selected_tags", "coordinate_definition",
    "reference_state", "reference_exact", "initial_direction_records",
    "source_files", "exact_input_storage", "reference_complete163",
}
require = reader.require


def scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))


def omitted(value, reason):
    return {"explicit_omission": True, "reason": reason,
            "type": type(value).__name__,
            "length": len(value) if isinstance(value, (list, dict, str)) else None,
            **reader.fingerprint(value)}


def compact(value, depth=3, key=""):
    if (key in STATE_KEYS or ("source" in key.lower() and "sha256" in key.lower())) and isinstance(value, (dict, list)):
        return omitted(value, "original numeric/state/source container; metadata only")
    if isinstance(value, str):
        return value if len(value) <= TEXT_CAP else omitted(value, "long original text")
    if scalar(value):
        return value
    if isinstance(value, list):
        if len(value) > 16 or (len(value) > 8 and all(scalar(v) for v in value)):
            return omitted(value, "large original list; no payload emitted")
        return [compact(v, depth-1, key) for v in value] if depth >= 0 else omitted(value, "depth")
    if isinstance(value, dict):
        if depth < 0:
            result = {k: compact(v, 0, k) for k, v in value.items() if scalar(v)}
            result["unexpanded_field_names"] = [k for k, v in value.items() if not scalar(v)]
            return result
        return {k: compact(v, depth-1, k) for k, v in value.items()}
    raise reader.ObservationError("non-JSON value in original record")


def scalars(value):
    if not isinstance(value, dict):
        return compact(value, 0)
    return {k: compact(v, 0, k) for k, v in value.items() if scalar(v)}


def selected(value, keys, depth=3):
    if not isinstance(value, dict):
        return compact(value, 0)
    out = scalars(value)
    for key in keys:
        if key in value:
            out[key] = compact(value[key], depth, key)
    out["unexpanded_original_field_names"] = [k for k in value if k not in out]
    return out


def record_identity(row):
    return {key: row[key] for key in (
        "tag", "original_line", "timestamp", "payload_bytes",
        "payload_sha256", "payload_plus_LF_bytes", "payload_plus_LF_sha256")}


def parse_records(raw):
    found = {tag: [] for tag in TAGS}
    for number, line in enumerate(io.BytesIO(raw), 1):
        text = reader.ANSI.sub("", line.decode("utf-8").rstrip("\r\n")).lstrip("\ufeff")
        match = reader.TIME_PREFIX.match(text)
        timestamp, body = (match.group(1), match.group(2)) if match else (None, text)
        body = body.lstrip("\ufeff")
        for tag in TAGS:
            if not body.startswith(tag+" "):
                continue
            require(timestamp is not None, "target original record lacks its timestamp: "+tag)
            payload = body[len(tag)+1:]
            value = reader.decode_json(payload)
            require(isinstance(value, dict), "target original tag must contain one JSON object")
            data = payload.encode("utf-8")
            found[tag].append({
                "tag": tag, "original_line": number, "timestamp": timestamp,
                "payload_bytes": len(data), "payload_sha256": reader.digest(data),
                "payload_plus_LF_bytes": len(data)+1,
                "payload_plus_LF_sha256": reader.digest(data+b"\n"),
                "value": value})
            break
    return found


def one(records, tag):
    require(len(records[tag]) == 1, "one exact original record required: "+tag)
    return records[tag][0]


def event_view(event):
    if not isinstance(event, dict):
        return compact(event)
    out = selected(event, (
        "coefficients_observed", "actual_physical_norm_record",
        "original_signed_group_summaries"), 3)
    source = event.get("source")
    if isinstance(source, dict):
        out["source"] = selected(source, (
            "source", "final_model_binding", "old_final_model_binding",
            "original_selected_IDs_sha256"), 2)
    return out


def learning_view(value):
    if not isinstance(value, dict):
        return compact(value)
    out = selected(value, ("coefficients", "coefficient_binary64_exact",
                          "maximizing_event_indices", "pending_event_indices", "context"), 2)
    if isinstance(value.get("events"), list):
        out["events"] = [event_view(e) for e in value["events"]]
    if isinstance(value.get("commits"), list):
        out["commits"] = compact(value["commits"], 4)
    return out


def guard_view(value):
    return selected(value, (
        "frozen_coefficients", "per_grid", "pending_commit_before_model",
        "final_model_binding", "unchanged_array_sha256"), 4)


def lp_view(lp):
    out = selected(lp, (
        "primary_SOC_pair_allocation", "original_and_scaled_residuals",
        "SOC_original_and_scaled_residuals", "same_step_scalar_and_affine_budget_comparison",
        "physical_values_or_Jacobians_inside_inner_solver",
        "final_repaired_original_residuals", "original_residuals"), 3)
    if not isinstance(lp, dict):
        return out
    for key in ("inner_LPs", "cut_rounds"):
        if isinstance(lp.get(key), list):
            out[key] = [selected(item, (
                "source_primary_allocation", "residuals", "final_residual",
                "objective", "limits"), 2) for item in lp[key]]
    complete = lp.get("complete_original_grid_model")
    if isinstance(complete, dict):
        out["complete_original_grid_model"] = selected(complete, ("summary",), 2)
        oracle = complete.get("oracle", {})
        out["complete_original_grid_model"]["oracle"] = selected(
            oracle, ("statistics", "initial_four_maxima"), 2)
    return out


def trial_view(trial):
    out = selected(trial, (
        "coarse_decision", "fine_decision", "scale_feedback",
        "restricted_support_invariants", "fine_violation_groups",
        "curvature_nonlinear_defect_diagnostic", "SOC_LP_opportunity_allocation",
        "rebound_model_binding"), 4)
    if not isinstance(trial, dict):
        return out
    if "curvature_defect_guard_sample" in trial:
        sample = trial["curvature_defect_guard_sample"]
        out["curvature_defect_guard_sample"] = selected(
            sample, ("coefficients_observed",), 1)
    error = trial.get("affine_metric_error_decomposition")
    if isinstance(error, dict):
        out["affine_metric_error_decomposition"] = selected(error, (
            "difference_terms", "complete_model_difference_terms",
            "maximum_slack_difference_terms", "complete_affine_four_maxima"), 3)
    return out


def model_view(model):
    out = selected(model, (
        "SOC_hold_model_binding", "primary_step_cost_diagnostic",
        "primary_allocation_before_factory", "original_model_fingerprint",
        "scale_feedback_update", "expanded_pool_rebound_eligibility",
        "expanded_pool_rebound_budget", "accepted_SOC_base_total_step_diagnostic",
        "accepted_rebound_SOC_base_total_step_diagnostic",
        "failed_y_post_learning_cache_restore", "error"), 4)
    if "curvature_defect_guard" in model:
        out["curvature_defect_guard"] = guard_view(model["curvature_defect_guard"])
    if "curvature_defect_sample_final_record" in model:
        out["curvature_defect_sample_final_record"] = selected(
            model["curvature_defect_sample_final_record"], ("coefficients_observed",), 1)
    if "ordinary_covered_context" in model:
        out["ordinary_covered_context"] = selected(model["ordinary_covered_context"], (
            "final_model_binding", "old_pool_versions", "old_ID_counts",
            "old_ID_sha256"), 2)
    out["linear_program"] = lp_view(model.get("linear_program", {}))
    if "complete_model" in model:
        out["complete_model"] = complete_model_view(model["complete_model"])
    out["trials"] = [trial_view(v) for v in model.get("trials", [])]
    out["corrections"] = []
    for correction in model.get("corrections", []):
        part = selected(correction, (
            "rebound_model_binding", "original_primary_model_binding", "corrected_trial_added_rows"), 2)
        part["linear_program"] = lp_view(correction.get("linear_program", {}))
        out["corrections"].append(part)
    return out



def complete_model_view(value):
    out = selected(value, ("summary", "supplemental_paid_normals",
                          "new_task_resource_limits", "new_support_requests"), 3)
    oracle = value.get("oracle", {})
    out["oracle"] = selected(oracle, ("statistics", "binding", "initial_four_maxima"), 2)
    out["oracle"]["direction_events"] = [
        selected(x, ("attainers", "four_maxima", "maxima", "grids"), 2)
        for x in oracle.get("direction_events", [])]
    out["oracle"]["new_original_row_J_events"] = [
        selected(x, ("original_row",), 1) for x in oracle.get("new_original_row_J_events", [])]
    out["norm_direction_memory"] = selected(
        value.get("norm_direction_memory", {}), ("statistics", "context"), 2)
    return out


def geometry_timing_view(value):
    if not isinstance(value, dict):
        return compact(value)
    out = selected(value, ("components",), 4)
    out["last_call"] = selected(value.get("last_call"), ("components",), 4)
    out["implementation"] = selected(value.get("implementation"), (), 0)
    return out


def complete_view(report):
    out = selected(report, (
        "configuration", "new_scientific_resource_limits", "timing_segments",
        "new_evaluation_identities", "fresh_adapter_cap_gate_binding",
        "original_query_quadrature_order", "development_receipt",
        "final_actual_gate_booleans", "selected_gate_receipt_source",
        "final_full_grid_constraints", "final_doubled_constraints",
        "final_exact_box", "final_selection_validation", "value_evaluation_counts",
        "bank_migration_and_new_activity", "final_bank_scalar_report",
        "factorized_selected_J_execution", "complete_original_grid_oracle_progress",
        "source_final_selection_validation", "source_paid_point_remains_available_as_ancestral_input",
        "actual_counters_at_error", "limitations", "ancestor_costs", "error"), 3)
    if "new_adapter_timing_at_error" in report:
        out["new_adapter_timing_at_error"] = geometry_timing_view(report["new_adapter_timing_at_error"])
    stage = report.get(STAGE, {})
    sv = selected(stage, (
        "snapshot_scalar_counters", "original_bank_replay",
        "initial_complete_checkpoint_bank_input", "initial_fixed_domain_and_height_diagnostic",
        "last_pre_LP_decision", "new_task_resource_limits", "new_task_total_limits",
        "direct_reference_initial_scalar_comparison", "direct_reference_bank_migration",
        "curvature_learning_context_migration", "direct_reference_task_metadata",
        "covered_soft_ordinary_growth_observation", "error"), 3)
    solver = stage.get("solver", {})
    sv["solver"] = selected(solver, (
        "final_shared_LP_allocation", "unpaired_primary_stop", "initial_pre_LP_decision",
        "last_pre_LP_decision", "initial_paid_scalar_comparison", "initial_pool_handling",
        "error"), 3)
    sv["solver"]["initial_ordinary_timing"] = {
        k: geometry_timing_view(v) for k, v in solver.get("initial_ordinary_timing", {}).items()}
    sv["initial_actual_two_grid_decisions"] = compact(
        stage.get("initial_actual_two_grid_decisions"), 4)
    sv["selected_two_grid_physical_point"] = selected(
        stage.get("selected_two_grid_physical_point"), ("coarse", "fine", "reason"), 3)
    sv["direct_reference_geometry_timing"] = geometry_timing_view(
        stage.get("direct_reference_geometry_timing"))
    sv["expanded_pool_rebound_records"] = [
        selected(x, ("rebound_model_binding", "frozen_current_budget", "error"), 2)
        for x in stage.get("expanded_pool_rebound_records", [])]
    out[STAGE] = sv
    obs = report.get("curvature_defect_guard_observation",
                     stage.get("curvature_defect_guard_observation", {}))
    out["curvature_defect_guard_observation"] = selected(
        obs, ("initial_learning_state", "final_learning_state", "bookkeeping"), 3)
    out["paid_previous_attempt_receipt"] = selected(
        report.get("paid_previous_attempt_receipt"),
        ("original_nine_check_evidence", "paid_cost"), 4)
    cp = report.get("future_direct_checkpoint")
    if isinstance(cp, dict):
        out["future_direct_checkpoint"] = selected(
            cp, ("norm_direction_bank_counters", "information_migration_receipts",
                 "ancestor_costs"), 3)
        for k in ("coarse_pool", "fine_pool", "norm_direction_bank_entries",
                  "selected_final159_binary64_exact", "selected_final163_physical_exact",
                  "reference_complete163_binary64_exact", "coordinate_definition",
                  "norm_direction_bank_context", "configuration",
                  "objective_evaluation_definition", "ordinary_field_evaluation_definition",
                  "factorization_definition", "supplemental_paid_normals"):
            if k in cp:
                out["future_direct_checkpoint"][k] = omitted(
                    cp[k], "exact reusable input remains solely in the original log")
        out["future_direct_checkpoint"]["curvature_defect_guard_learning_checkpoint"] = learning_view(
            cp.get("curvature_defect_guard_learning_checkpoint", {}))
    return out


def run(args, context):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "readback runs only in the original public repository Actions")
    source = os.environ.get("GITHUB_SHA", "")
    require(reader.SHA40.fullmatch(source) is not None, "observer source SHA required")
    root = Path(reader.git_ok(Path.cwd(), ["rev-parse", "--show-toplevel"]).decode().strip())
    script = reader.repo_path(args.source_path)
    helper = TOPIC+"/scripts/read_original_actions_log.py"
    request_path = reader.repo_path(args.request)
    require(Path(__file__).resolve() == (root/script).resolve(), "observer source path differs")
    require(Path(reader.__file__).resolve() == (root/helper).resolve(), "read-only helper path differs")
    api = reader.GitHubReader(REPO)
    source_bytes = api.content(script, source, 100000)
    helper_bytes = api.content(helper, source, 100000)
    request_bytes = api.content(request_path, source, 64000)
    require((root/script).read_bytes() == source_bytes
            and (root/helper).read_bytes() == helper_bytes
            and (root/request_path).read_bytes() == request_bytes,
            "observer/helper/request checkout differs from pinned observer source")
    req = reader.decode_json(request_bytes)
    require(req.get("mode") == MODE and req.get("repository") == REPO,
            "exact read-only direct-reference request required")
    require(req.get("source_sha256") == reader.digest(source_bytes)
            and req.get("helper_source_sha256") == reader.digest(helper_bytes),
            "observer/read-only helper source hash differs")
    workflow_path = reader.repo_path(req["workflow_path"])
    workflow_bytes = api.content(workflow_path, source, 20000)
    require(reader.digest(workflow_bytes) == req["workflow_sha256"],
            "observer workflow hash differs")
    require(str(req.get("original_run_id")) == RUN
            and str(req.get("original_job_id")) == JOB
            and req.get("original_source_commit") == SOURCE,
            "only the one completed third direct-reference attempt can be observed")
    require(req.get("stdout_byte_limit") == STDOUT_CAP, "declared660000-byte readback bound required")
    context["observer_binding"] = {
        "repository": REPO, "source_commit": source, "source_path": script,
        "source_sha256": reader.digest(source_bytes), "source_bytes": len(source_bytes),
        "helper_source_sha256": reader.digest(helper_bytes),
        "workflow_path": workflow_path, "workflow_sha256": reader.digest(workflow_bytes),
        "request_path": request_path, "request_bytes": len(request_bytes),
        "request_sha256": reader.digest(request_bytes),
        "observer_run_id": os.environ.get("GITHUB_RUN_ID"),
        "observer_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT")}
    context["observer_actual_git_pull"] = reader.actual_pull(root, req, source)
    require(context["observer_actual_git_pull"]["passed"], "public pull/README identity failed")
    reader.private_rule_pull(req, context)

    old_req_path = TOPIC+"/computations/request-direct-reference-new-task.json"
    old_req_bytes = api.content(old_req_path, SOURCE, 64000)
    require(len(old_req_bytes) == req["original_request_bytes"]
            and reader.digest(old_req_bytes) == req["original_request_sha256"],
            "pinned original direct-reference request differs")
    original_request = reader.decode_json(old_req_bytes)
    run_obj = api.api_json("/actions/runs/"+RUN)
    job_obj = api.api_json("/actions/jobs/"+JOB)
    require(str(run_obj.get("id")) == RUN and str(job_obj.get("id")) == JOB
            and str(job_obj.get("run_id")) == RUN
            and run_obj.get("head_sha") == job_obj.get("head_sha") == SOURCE,
            "original run/job/source identity differs")
    require(run_obj.get("status") == job_obj.get("status") == "completed"
            and run_obj.get("conclusion") == job_obj.get("conclusion")
            == req.get("expected_original_conclusion") == "success",
            "original completed run/job conclusion differs from observed metadata")
    context["original_run"] = scalars(run_obj)
    context["original_job"] = scalars(job_obj)
    context["original_job_steps"] = [scalars(x) for x in job_obj.get("steps", [])]
    raw, redirects = api.job_log(JOB)
    raw_hash = reader.digest(raw)
    if "original_log_sha256" in req:
        require(len(raw) == req["original_log_bytes"] and raw_hash == req["original_log_sha256"],
                "original log differs from a previously observed byte digest")
        hash_status = "matches supplied previously observed bytes"
    else:
        require(req.get("original_log_identity_unobserved") is True,
                "first observation must explicitly declare that no raw digest is yet known")
        hash_status = "first successful original-byte observation; no guessed expected hash"
    context["original_log"] = {
        "run_id": RUN, "job_id": JOB, "source_commit": SOURCE,
        "bytes": len(raw), "sha256": raw_hash, "hash_status": hash_status,
        "downloaded_at": reader.utc_now(), "redirects_without_authorization": redirects,
        "original_log_download_count": 1, "only_in_memory": True,
        "written_uploaded_split_or_committed": False}
    records = parse_records(raw)
    context["original_record_directory"] = {
        tag: [record_identity(row) for row in rows] for tag, rows in records.items()}
    request_row = one(records, "DIRECT_REFERENCE_REQUEST")
    reuse_row = one(records, "DIRECT_REFERENCE_DEVELOPMENT_REUSED")
    prior_row = one(records, "DIRECT_REFERENCE_PRIOR_WORK_REUSED")
    complete_row = one(records, "DIRECT_REFERENCE_COMPLETE")
    require(not records["DIRECT_REFERENCE_DEVELOPMENT"] and not records["DIRECT_REFERENCE_ENTRY_ERROR"],
            "third run must consume its original nine-check receipt without new checks")
    request_value, reused, real = request_row["value"], reuse_row["value"], complete_row["value"]
    require(request_value.get("source_commit") == SOURCE
            and request_value.get("request_bytes") == len(old_req_bytes)
            and request_value.get("request_sha256") == reader.digest(old_req_bytes)
            and request_value.get("source_sha256") == original_request.get("source_sha256"),
            "original REQUEST does not reproduce the pinned161-source closure")
    expected = original_request["source_sha256"]
    expected_py = {Path(p).name: h for p, h in expected.items() if p.endswith(".py")}
    require(len(expected) == 161 and len(expected_py) == 152
            and sum(p.endswith(".py") for p in expected) == 152
            and sum(p.startswith(".github/workflows/") for p in expected) == 8,
            "original161 closure and152 unique Python basenames required")
    require(real.get("source_files_sha256") == expected_py,
            "original COMPLETE Python bindings disagree with original request")
    require(real.get("schema") == SCHEMA and real.get("github_sha") == SOURCE
            and str(real.get("github_run_id")) == RUN and real.get("github_repository") == REPO,
            "original COMPLETE schema/run/source differs")
    require(reused.get("schema") == POLICY+"-paid-nine-check-chain-reuse"
            and reused.get("passed") is True and reused.get("all_paid_cases_passed") is True
            and reused.get("paid_groups") == 3 and reused.get("paid_cases") == 9
            and reused.get("new_development_groups_executed") == 0
            and reused.get("new_development_cases_executed") == 0,
            "original third-run paid-nine-check evidence differs")
    require(request_row["original_line"] < reuse_row["original_line"]
            < prior_row["original_line"] < complete_row["original_line"],
            "original request/reuse/source/complete chronology differs")
    models = records["DIRECT_REFERENCE_MODEL"]
    require([r["value"].get("number") for r in models] == list(range(1, len(models)+1))
            and len(models) == real[STAGE]["model_count"]
            and len(models) <= real["configuration"]["max_linear_models"],
            "original model chronology/count differs from completed stage")
    context["source_bindings"] = {
        "original_request_path": old_req_path, "read_at_commit": SOURCE,
        "original_request_bytes": len(old_req_bytes),
        "original_request_sha256": reader.digest(old_req_bytes),
        "request_source_count": len(expected), "Python_source_count": len(expected_py),
        "all_original_COMPLETE_sources_match_original_request": True,
        "source_closure_fingerprint": reader.fingerprint(expected),
        "original_development_was_reused_not_reexecuted": True}
    context["scope"] = {
        "scientific_module_imports": 0, "science_or_developer_execution": False,
        "only_original_values_are_copied_no_numerical_recomputation": True,
        "hashing_and_container_counts_are_administrative_metadata": True,
        "old_runner_payloads_stay_only_in_memory": True,
        "output_is_a_nonreconstructible_bounded_semantic_view": True,
        "workflow_success_is_not_substituted_for_original_records": True}

    outputs = [("DIRECT_REFERENCE_READBACK_IDENTITY", context)]
    outputs.append(("DIRECT_REFERENCE_READBACK_REUSE", {
        "original_reuse_record": record_identity(reuse_row),
        "development_reuse": compact(reused, 5),
        "original_prior_record": record_identity(prior_row),
        "prior_work_reused": compact(prior_row["value"], 2)}))
    for row in models:
        outputs.append(("DIRECT_REFERENCE_READBACK_MODEL", {
            "original_record": record_identity(row), "model": model_view(row["value"])}))
    outputs.append(("DIRECT_REFERENCE_READBACK_COMPLETE", {
        "original_record": record_identity(complete_row), "report": complete_view(real)}))
    outputs.append(("DIRECT_REFERENCE_READBACK_ORIGINAL_PULLS", {
        tag: [{"original_record": record_identity(row), "record": compact(row["value"], 5)}
              for row in records[tag]]
        for tag in ("DIRECT_REFERENCE_PUBLIC_PULL", "DIRECT_REFERENCE_PRIVATE_PULL",
                    "DIRECT_REFERENCE_OUTPUT_METADATA", "DIRECT_REFERENCE_WORKFLOW_OUTPUT_METADATA")}))
    return outputs


def main():
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", required=True)
    parser.add_argument("--source-path", default=TOPIC+"/scripts/read_direct_reference_completed_log.py")
    args = parser.parse_args()
    context = {"schema": MODE, "started_at": reader.utc_now(), "stdout_byte_limit": STDOUT_CAP}
    try:
        records = run(args, context)
        context["observer_elapsed_seconds"] = time.monotonic()-started
        context["completed_at"] = reader.utc_now()
        def encode(rows):
            return b"".join(label.encode("ascii")+b" "+reader.encoded(value)+b"\n"
                            for label, value in rows)
        output = encode(records)
        if len(output) > STDOUT_CAP:
            # Only duplicate ancestral receipts and long old histories are
            # suppressed. Every MODEL/trial/gate/current cost remains present.
            for tag, value in records:
                if tag == "DIRECT_REFERENCE_READBACK_REUSE":
                    value["development_reuse"] = selected(value["development_reuse"], (), 0)
                    value["prior_work_reused"] = selected(value["prior_work_reused"], (), 0)
                if tag == "DIRECT_REFERENCE_READBACK_COMPLETE":
                    report = value["report"]
                    report["paid_previous_attempt_receipt"] = selected(
                        report.get("paid_previous_attempt_receipt"), (), 0)
                    cp = report.get("future_direct_checkpoint", {})
                    learning = cp.get("curvature_defect_guard_learning_checkpoint", {})
                    for key in ("events", "commits"):
                        if key in learning:
                            learning[key] = omitted(learning[key], "per-model live observations already retained")
            context["only_repeated_ancestral_history_details_shortened"] = True
            output = encode(records)
        if len(output) > STDOUT_CAP:
            complete = next(value for tag, value in records
                            if tag == "DIRECT_REFERENCE_READBACK_COMPLETE")
            minimal = {"context": context, "status": "semantic-output-bound-requires-narrower-selection",
                       "proposed_stdout_bytes": len(output),
                       "original_complete_record": complete["original_record"],
                       "original_status": complete["report"].get("status"),
                       "original_final_selection_validation": complete["report"].get("final_selection_validation"),
                       "original_stage_status": complete["report"].get(STAGE, {}).get("status"),
                       "original_timing_segments": complete["report"].get("timing_segments"),
                       "no_science_or_developer_execution": True,
                       "no_original_payload_written_split_uploaded_or_committed": True}
            output = b"DIRECT_REFERENCE_READBACK_LIMIT "+reader.encoded(minimal)+b"\n"
            require(len(output) <= STDOUT_CAP, "minimal provenance exceeds stdout bound")
            sys.stdout.buffer.write(output)
            return 2
        sys.stdout.buffer.write(output)
        return 0
    except Exception as error:
        context["observer_elapsed_seconds"] = time.monotonic()-started
        failure = {"schema": MODE+"-error", "error_type": type(error).__name__,
                   "error": str(error)[:TEXT_CAP], "context": context,
                   "no_science_or_developer_execution": True,
                   "no_original_payload_written_split_uploaded_or_committed": True}
        output = b"DIRECT_REFERENCE_READBACK_ERROR "+reader.encoded(failure)+b"\n"
        if len(output) > STDOUT_CAP:
            failure["context"] = {k: context[k] for k in (
                "observer_binding", "observer_actual_git_pull",
                "observer_private_actual_git_pull", "original_log") if k in context}
            output = b"DIRECT_REFERENCE_READBACK_ERROR "+reader.encoded(failure)+b"\n"
        require(len(output) <= STDOUT_CAP, "error provenance exceeds stdout bound")
        sys.stdout.buffer.write(output)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

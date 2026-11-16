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


def short_scalars(value):
    """Original scalar values only; long narrative strings are not repeated."""
    if not isinstance(value, dict):
        return value if scalar(value) else omitted(value, "non-scalar original")
    return {k: v for k, v in value.items()
            if scalar(v) and (not isinstance(v, str) or len(v) <= 200)}


def fields(value, names):
    if not isinstance(value, dict):
        return {}
    return {name: value[name] for name in names if name in value and scalar(value[name])}


def source_note(original, output, reason):
    if isinstance(original, dict):
        output["unselected_original_field_names"] = [k for k in original if k not in output]
    output["selection_scope"] = reason
    return output


def decision_view(value):
    if not isinstance(value, dict):
        return value if scalar(value) else omitted(value, "original decision not an object")
    out = short_scalars(value)
    if "actual_gate_booleans" in value:
        out["actual_gate_booleans"] = value["actual_gate_booleans"]
    # Original scalar decision names are retained, including every eta/kappa,
    # gate flag, tolerance and margin. Dense coordinate diagnostics are omitted.
    return source_note(value, out, "original scalar decision and all actual gate booleans")


LP_KEYS = (
    "status", "success", "message", "nit", "elapsed_seconds", "seconds",
    "time_limit_seconds", "inner_call_count", "best_candidate_inner_index",
    "returned_candidate", "returned_inner_index", "returned_epigraph_gap_met",
    "returned_inexact_cut_model", "predicted_metric_slack",
    "predicted_slack_from_rows_and_outside", "predicted_slack_improvement",
    "normalized_step_norm", "returned_repaired_objective", "repaired_rho_auxiliary",
    "returned_LP_status", "returned_LP_success",
    "maximum_linear_row_violation", "maximum_linear_bound_violation",
    "initial_rebuilt_memory_rows", "total_new_cut_rows",
    "inherited_primary_solver_stop_status", "new_task_shared_LP_limit_exhausted",
    "proposal_rejected_before_geometry", "exact_convex_optimality_claim",
    "all_started_inner_LPs_charged_to_original_ledger",
    "physical_values_or_Jacobians_inside_inner_solver",
    "LP_rows", "LP_variables", "LP_matrix_bytes", "shared_LP_ordinal",
    "corrected_actual_trial_linear_metric_slack", "corrected_trial_linear_eta_bound")


def lp_view(lp):
    if not isinstance(lp, dict):
        return {}
    out = fields(lp, LP_KEYS)
    for key in ("primary_SOC_pair_allocation", "same_step_scalar_and_affine_budget_comparison",
                "final_repaired_original_residuals", "original_residuals"):
        if isinstance(lp.get(key), dict):
            out[key] = short_scalars(lp[key])
    out["inner_LPs"] = []
    for item in lp.get("inner_LPs", []):
        record = short_scalars(item)
        for key in ("inherited_scalar_LP_report", "repaired_residual"):
            if isinstance(item.get(key), dict):
                record[key] = short_scalars(item[key])
        out["inner_LPs"].append(record)
    out["cut_rounds"] = [short_scalars(x) for x in lp.get("cut_rounds", [])]
    return source_note(lp, out, "fixed LP fields; original inner status/gap/gain/residual/cost scalars")


def trial_view(trial):
    out = fields(trial, (
        "kind", "alpha_exact", "accepted_as_next_iterate", "accepted_index",
        "attempt_status", "physical_state_sha256",
        "coarse_physical_evaluation", "fine_value_evaluation",
        "actual_fine_evaluated_even_if_coarse_ineligible",
        "coarse_omitted_rows", "coarse_omitted_hard_rows", "new_coarse_rows",
        "fine_omitted_rows", "fine_omitted_hard_rows", "new_fine_rows",
        "expanded_pool_rebound_revision"))
    for key in ("coarse_decision", "fine_decision"):
        if key in trial:
            out[key] = decision_view(trial[key])
    if "scale_feedback" in trial:
        out["scale_feedback"] = short_scalars(trial["scale_feedback"])
    sample = trial.get("curvature_defect_guard_sample")
    if isinstance(sample, dict):
        out["curvature_defect_guard_sample"] = short_scalars(sample)
        for key in ("coefficients_observed", "actual_physical_norm_record"):
            if isinstance(sample.get(key), dict):
                out["curvature_defect_guard_sample"][key] = short_scalars(sample[key])
    return source_note(trial, out, "actual trial identity, eta/kappa, all original gates and learning counts")


def controller_view(value):
    """Only the actual policy proof nodes; no recursive legacy copies."""
    if not isinstance(value, dict):
        return {}
    out = fields(value, ("next_trust", "next_tail_radius", "next_height_radius", "schema"))
    proofs, seen = [], set()
    def walk(node, path):
        if not isinstance(node, dict):
            return
        if isinstance(node.get("checks"), dict):
            signature = reader.fingerprint(node)["canonical_json_sha256"]
            if signature not in seen:
                seen.add(signature)
                record = fields(node, (
                    "schema", "model_number", "decision", "qualified",
                    "qualified_covered_ordinary_model", "qualified_new_pair_at_cap",
                    "legacy_streak_before", "frozen_controller_returned_streak",
                    "legacy_streak_after", "covered_streak_before", "covered_streak_after",
                    "old_pair_consumed", "new_pair_consumed", "any_pair_consumed",
                    "grew_for_next_model_by_new_rule", "any_actual_radius_growth",
                    "grew_for_next_model", "qualified_pair_at_cap",
                    "old_controller_next_radius", "model_radius", "new_next_radius",
                    "next_radius_used_by_model_number", "next_model_factory_used_radius",
                    "next_model_started_primary_LPs", "held_radius", "old_next_radius",
                    "bookkeeping_elapsed_seconds"))
                record["checks"] = {k: v for k, v in node["checks"].items() if scalar(v)}
                if "failed_conditions" in node:
                    record["failed_conditions"] = node["failed_conditions"]
                proofs.append({"original_path": path, "original_node_sha256": signature,
                               "original_values": record})
        for key, item in node.items():
            if isinstance(item, dict):
                walk(item, path+"."+key)
    walk(value, "$")
    out["unique_original_proofs"] = proofs
    return out


def guard_view(value):
    out = fields(value, (
        "status", "B", "B_binary64_exact", "original_floor_exact",
        "modified_row_count", "frozen_learning_state_sha256",
        "complete_model_binding_sha256", "original_SOC_RHS_unchanged",
        "before_targets_sha256", "guarded_targets_sha256",
        "before_rhs_sha256", "guarded_rhs_sha256"))
    if isinstance(value.get("frozen_coefficients"), dict):
        out["frozen_coefficients"] = value["frozen_coefficients"]
    if isinstance(value.get("per_grid"), dict):
        out["per_grid"] = {label: short_scalars(record)
                           for label, record in value["per_grid"].items()}
    return out


def oracle_cost_view(value):
    if not isinstance(value, dict):
        return {}
    out = fields(value, ("schema", "binding_sha256"))
    out["statistics"] = short_scalars(value.get("statistics", {}))
    out["direction_events"] = [
        fields(x, ("status", "phase", "ordinal", "elapsed_seconds",
                   "direction_sha256", "cache_hit", "original_grid_evaluations"))
        for x in value.get("direction_events", [])]
    out["new_original_row_J_events"] = [
        short_scalars(x) for x in value.get("new_original_row_J_events", [])]
    return out


def model_view(model):
    out = fields(model, (
        "number", "linearized_at_accepted_index", "linearized_at_physical_sha256",
        "linearized_at_true_two_grid_max_eta", "coarse_pool_rows", "fine_pool_rows",
        "coarse_pool_version", "fine_pool_version", "trust_before_model", "result",
        "accepted_expanded_pool_same_trial_SOC", "curvature_defect_sample_event_index"))
    out["linear_program"] = lp_view(model.get("linear_program", {}))
    out["primary_allocation_before_factory"] = short_scalars(
        model.get("primary_allocation_before_factory", {}))
    out["curvature_defect_guard"] = guard_view(model.get("curvature_defect_guard", {}))
    out["scale_feedback_update"] = controller_view(model.get("scale_feedback_update", {}))
    out["trials"] = [trial_view(v) for v in model.get("trials", [])]
    out["corrections"] = [
        {"original_scalar_fields": fields(x, (
            "primary_trial_index", "primary_trial_physical_sha256",
            "coarse_pool_version", "fine_pool_version",
            "same_layout_original_SOC_charged_before_call", "expanded_pool_rebound_revision")),
         "linear_program": lp_view(x.get("linear_program", {}))}
        for x in model.get("corrections", [])]
    cm = model.get("complete_model", {})
    out["complete_model"] = {
        "summary": short_scalars(cm.get("summary", {})),
        "oracle": oracle_cost_view(cm.get("oracle", {})),
        "norm_direction_memory": short_scalars(cm.get("norm_direction_memory", {}))}
    sample = model.get("curvature_defect_sample_final_record", {})
    out["curvature_defect_sample_final_record"] = {
        **fields(sample, ("event_index", "committed", "status", "first_consuming_model_number")),
        "coefficients_observed": sample.get("coefficients_observed")}
    return source_note(model, out, "fixed per-model audit columns; complete model28 is emitted separately")


def bounded_metadata(value, depth=2):
    """Scalar administrative metadata only, with bounded nesting and no long lists."""
    if scalar(value):
        return value if not isinstance(value, str) or len(value) <= 200 else omitted(value, "long text")
    if isinstance(value, list):
        if len(value) <= 6 and all(scalar(x) for x in value):
            return value
        return omitted(value, "original list retained only by fingerprint")
    if not isinstance(value, dict):
        return omitted(value, "non-JSON metadata")
    out = short_scalars(value)
    if depth:
        for key, item in value.items():
            if isinstance(item, dict) and key not in STATE_KEYS:
                out[key] = bounded_metadata(item, depth-1)
    return out


def geometry_timing_view(value):
    if not isinstance(value, dict):
        return value if scalar(value) else omitted(value, "timing value")
    out = short_scalars(value)
    for key in ("components", "last_call"):
        if key in value:
            out[key] = bounded_metadata(value[key], 3)
    return out


def complete_view(report):
    out = short_scalars(report)
    for key in ("new_scientific_resource_limits", "timing_segments",
                "new_evaluation_identities", "original_query_quadrature_order",
                "final_selection_validation", "value_evaluation_counts",
                "final_bank_scalar_report", "limitations"):
        if key in report:
            out[key] = short_scalars(report[key])
    for key in ("final_actual_gate_booleans",):
        if key in report:
            out[key] = report[key]
    for key in ("fresh_adapter_cap_gate_binding", "selected_gate_receipt_source",
                "final_exact_box", "bank_migration_and_new_activity",
                "factorized_selected_J_execution", "ancestor_costs"):
        if key in report:
            out[key] = bounded_metadata(report[key], 2)
    for key in ("final_full_grid_constraints", "final_doubled_constraints"):
        if key in report:
            out[key] = decision_view(report[key])
    stage = report.get(STAGE, {})
    sv = short_scalars(stage)
    for key in ("snapshot_scalar_counters", "initial_complete_checkpoint_bank_input",
                "last_pre_LP_decision", "new_task_resource_limits", "new_task_total_limits",
                "direct_reference_initial_scalar_comparison"):
        if key in stage:
            sv[key] = short_scalars(stage[key])
    for key in ("direct_reference_bank_migration", "curvature_learning_context_migration"):
        if key in stage:
            sv[key] = bounded_metadata(stage[key], 1)
    sv["direct_reference_geometry_timing"] = geometry_timing_view(
        stage.get("direct_reference_geometry_timing"))
    solver = stage.get("solver", {})
    sv["solver"] = short_scalars(solver)
    for key in ("final_shared_LP_allocation", "unpaired_primary_stop",
                "initial_pre_LP_decision", "last_pre_LP_decision",
                "initial_paid_scalar_comparison", "initial_pool_handling"):
        if key in solver:
            sv["solver"][key] = bounded_metadata(solver[key], 1)
    sv["solver"]["initial_ordinary_timing"] = {
        k: geometry_timing_view(v) for k, v in solver.get("initial_ordinary_timing", {}).items()}
    sv["initial_actual_two_grid_decisions"] = {
        k: decision_view(v) for k, v in (stage.get("initial_actual_two_grid_decisions") or {}).items()}
    point = stage.get("selected_two_grid_physical_point", {})
    sv["selected_two_grid_physical_point"] = short_scalars(point)
    for key in ("coarse", "fine", "reason"):
        if isinstance(point.get(key), dict):
            sv["selected_two_grid_physical_point"][key] = decision_view(point[key])
    out[STAGE] = sv
    obs = report.get("curvature_defect_guard_observation", {})
    out["curvature_defect_guard_observation"] = short_scalars(obs)
    for key in ("initial_learning_state", "final_learning_state", "bookkeeping"):
        if isinstance(obs.get(key), dict):
            out["curvature_defect_guard_observation"][key] = bounded_metadata(obs[key], 1)
    cp = report.get("future_direct_checkpoint")
    if isinstance(cp, dict):
        out["future_direct_checkpoint"] = short_scalars(cp)
        for key in ("norm_direction_bank_counters", "information_migration_receipts",
                    "ancestor_costs"):
            if key in cp:
                out["future_direct_checkpoint"][key] = bounded_metadata(cp[key], 1)
        for key in ("coarse_pool", "fine_pool", "norm_direction_bank_entries",
                    "selected_final159_binary64_exact", "selected_final163_physical_exact",
                    "reference_complete163_binary64_exact", "norm_direction_bank_context",
                    "configuration", "coordinate_definition"):
            if key in cp:
                out["future_direct_checkpoint"][key] = omitted(
                    cp[key], "exact checkpoint stays only in original runner log")
        learning = cp.get("curvature_defect_guard_learning_checkpoint", {})
        lv = short_scalars(learning)
        for key in ("coefficients", "coefficient_binary64_exact",
                    "maximizing_event_indices", "pending_event_indices"):
            if key in learning:
                lv[key] = learning[key]
        lv["events"] = []
        for event in learning.get("events", []):
            v = fields(event, ("event_index", "committed", "status", "first_consuming_model_number"))
            if "coefficients_observed" in event:
                v["coefficients_observed"] = event["coefficients_observed"]
            lv["events"].append(v)
        for key in ("commits", "context"):
            if key in learning:
                lv[key+"_fingerprint"] = reader.fingerprint(learning[key])
        out["future_direct_checkpoint"]["curvature_defect_guard_learning_checkpoint"] = lv
    return source_note(report, out, "fixed final gates, costs, migration and terminal checkpoint metadata")


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
    if models:
        outputs.append(("DIRECT_REFERENCE_READBACK_TERMINAL_MODEL", {
            "original_record": record_identity(models[-1]),
            "selection_scope": "complete original terminal MODEL; no fields omitted",
            "model": models[-1]["value"]}))
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
            # Keep the complete original terminal model and all mandatory
            # per-model LP/trial gates. Only secondary repeated metadata shrinks.
            for tag, value in records:
                if tag == "DIRECT_REFERENCE_READBACK_REUSE":
                    value["development_reuse"] = short_scalars(value["development_reuse"])
                    value["prior_work_reused"] = short_scalars(value["prior_work_reused"])
                if tag == "DIRECT_REFERENCE_READBACK_MODEL":
                    model = value["model"]
                    model.pop("unselected_original_field_names", None)
                    for trial in model.get("trials", []):
                        trial.pop("unselected_original_field_names", None)
                        for grid in ("coarse_decision", "fine_decision"):
                            if isinstance(trial.get(grid), dict):
                                trial[grid].pop("unselected_original_field_names", None)
                    lp = model.get("linear_program", {})
                    lp.pop("unselected_original_field_names", None)
                    cm = model.get("complete_model", {})
                    oracle = cm.get("oracle", {})
                    for key in ("direction_events", "new_original_row_J_events"):
                        if key in oracle:
                            oracle[key] = omitted(oracle[key], "original per-model aggregate costs retained")
                    model["secondary_metadata_shortened"] = True
                if tag == "DIRECT_REFERENCE_READBACK_COMPLETE":
                    report = value["report"]
                    report.pop("unselected_original_field_names", None)
                    for key in ("ancestor_costs", "bank_migration_and_new_activity"):
                        if key in report:
                            report[key] = omitted(report[key], "source fingerprint; migration state and costs retained elsewhere")
            context["secondary_metadata_only_shortened_for_bound"] = True
            output = encode(records)
        if len(output) > STDOUT_CAP:
            # A successful read must not conceal the terminal stopping evidence
            # behind a LIMIT-only record. Emit the complete terminal MODEL,
            # costs/final gates, then the full minimum 28-model table.
            essential = []
            for tag, value in records:
                if tag in ("DIRECT_REFERENCE_READBACK_IDENTITY",
                           "DIRECT_REFERENCE_READBACK_TERMINAL_MODEL",
                           "DIRECT_REFERENCE_READBACK_ORIGINAL_PULLS"):
                    essential.append((tag, value))
                elif tag == "DIRECT_REFERENCE_READBACK_COMPLETE":
                    report = value["report"]
                    stage = report.get(STAGE, {})
                    final = {k: report[k] for k in (
                        "schema", "status", "timing_segments", "value_evaluation_counts",
                        "final_actual_gate_booleans", "final_selection_validation",
                        "final_full_grid_constraints", "final_doubled_constraints",
                        "final_exact_box", "factorized_selected_J_execution",
                        "final_bank_scalar_report", "future_direct_checkpoint")
                        if k in report}
                    final.update(short_scalars(report))
                    final[STAGE] = short_scalars(stage)
                    for key in ("snapshot_scalar_counters", "solver",
                                "direct_reference_geometry_timing", "selected_two_grid_physical_point"):
                        if key in stage:
                            final[STAGE][key] = stage[key]
                    essential.append((tag, {"original_record": value["original_record"],
                        "selection_scope": "priority costs/final gates/checkpoint; secondary metadata omitted",
                        "report": final}))
                elif tag == "DIRECT_REFERENCE_READBACK_MODEL":
                    model = value["model"]
                    mini = {k: model[k] for k in (
                        "number", "result", "linearized_at_accepted_index",
                        "linearized_at_true_two_grid_max_eta", "trust_before_model",
                        "coarse_pool_rows", "fine_pool_rows", "coarse_pool_version", "fine_pool_version",
                        "linear_program", "primary_allocation_before_factory",
                        "curvature_defect_guard", "trials", "corrections")
                        if k in model}
                    mini["controller_next"] = fields(model.get("scale_feedback_update", {}),
                        ("next_trust", "next_tail_radius", "next_height_radius"))
                    mini["selection_scope"] = "minimum all-model table; full original record fingerprint retained"
                    essential.append((tag, {"original_record": value["original_record"], "model": mini}))
            context["priority_output_is_partial"] = True
            context["complete_terminal_MODEL_and_all_minimum_model_gates_preserved"] = True
            output = encode(essential)
        if len(output) > STDOUT_CAP:
            terminal = [(tag, value) for tag, value in records
                        if tag in ("DIRECT_REFERENCE_READBACK_IDENTITY",
                                   "DIRECT_REFERENCE_READBACK_TERMINAL_MODEL",
                                   "DIRECT_REFERENCE_READBACK_ORIGINAL_PULLS")]
            complete = next(value for tag, value in records if tag == "DIRECT_REFERENCE_READBACK_COMPLETE")
            report = complete["report"]
            minimum_models = []
            for tag, value in records:
                if tag != "DIRECT_REFERENCE_READBACK_MODEL":
                    continue
                model = value["model"]
                row = fields(model, ("number", "result", "trust_before_model",
                    "linearized_at_accepted_index", "linearized_at_true_two_grid_max_eta",
                    "coarse_pool_rows", "fine_pool_rows", "coarse_pool_version", "fine_pool_version"))
                row["original_record"] = value["original_record"]
                row["linear_program"] = fields(model.get("linear_program", {}), LP_KEYS)
                row["inner_LPs"] = model.get("linear_program", {}).get("inner_LPs", [])
                row["guard"] = model.get("curvature_defect_guard", {})
                row["trials"] = []
                for trial in model.get("trials", []):
                    tv = fields(trial, ("kind", "alpha_exact", "accepted_as_next_iterate",
                        "accepted_index", "new_coarse_rows", "new_fine_rows",
                        "coarse_omitted_hard_rows", "fine_omitted_hard_rows"))
                    for grid in ("coarse_decision", "fine_decision"):
                        if isinstance(trial.get(grid), dict):
                            tv[grid] = short_scalars(trial[grid])
                            if "actual_gate_booleans" in trial[grid]:
                                tv[grid]["actual_gate_booleans"] = trial[grid]["actual_gate_booleans"]
                    row["trials"].append(tv)
                minimum_models.append(row)
            terminal.append(("DIRECT_REFERENCE_READBACK_PRIORITY_FINAL", {
                "original_record": complete["original_record"],
                "minimum_all_models": minimum_models,
                "timing_segments": report.get("timing_segments"),
                "final_actual_gate_booleans": report.get("final_actual_gate_booleans"),
                "final_selection_validation": report.get("final_selection_validation"),
                "value_evaluation_counts": report.get("value_evaluation_counts"),
                "stage_scalar_counters": report.get(STAGE, {}).get("snapshot_scalar_counters"),
                "stage_solver_scalars": short_scalars(report.get(STAGE, {}).get("solver", {})),
                "all_other_models_original_record_directory_is_in_IDENTITY": True,
                "scope": "complete terminal model plus mandatory all-model scalar/trial-gate table and final costs; secondary controller/oracle details omitted"}))
            context["priority_secondary_details_not_emitted_due_to_bound"] = True
            output = encode(terminal)
            require(len(output) <= STDOUT_CAP, "complete terminal and provenance exceed hard stdout bound")
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

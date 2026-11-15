#!/usr/bin/env python3
"""Consume the paid seventh guard model and its exact terminal checkpoint once.

Only the fixed successful source log is read. No old LP, development group,
whole-grid direction, trial or optimizer is replayed. Recomputable arrays remain
in runner memory or transient output, never committed or uploaded.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
from pathlib import Path

from frame_height_null_coordinates import digest
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader
from frame_metric_paid_attainer_refinement import POLICY, PINS, fingerprint

REPO, ROOT = inherited.REPO, inherited.ROOT
require, json_bytes = inherited.require, inherited.json_bytes
SOURCE_RUN = "43767357527"
SOURCE_JOB = "132975354666"
SOURCE_COMMIT = "6f886c385bdc12c8963d451369c9250fa19a45a0"
SOURCE_SCHEMA = "same159-current-best-observed-curvature-defect-primary-guard-v1"
SOURCE_STAGE = "curvature_defect_guard_stage"
SOURCE_COMPLETE = "complete-two-grid-curvature-defect-guard-audit"


def _one(records, tag, source, bytes_key, sha_key):
    require(len(records[tag]) == 1, "one original record required: "+tag)
    payload, value = records[tag][0]
    raw = (payload+"\n").encode("utf-8")
    require(len(raw) == source[bytes_key] and reader.digest(raw) == source[sha_key],
            "original JSON plus LF differs: "+tag)
    return value



FIRST_ATTEMPT = {
    "run_id": "43771970034", "job_id": "132989648048",
    "source_commit": "68f92b9cb16677278dfbc7f8e13bdf7189e41d9c",
    "log_bytes": 430490,
    "log_sha256": "ba23313fae7855266456502ea1b5ac1f6b8d3799d5a833c6adbc749a1b3bd69d",
    "request_record_bytes": 22686,
    "request_record_sha256": "e69001f12ed703299ffa4224f29fbf926f6581c06b5eab89c45763159f1ddd77",
    "development_bytes": 17680,
    "development_sha256": "ab0755d597c2c626144e823b92d30f887bae96eac2173973179baaf9b218701c",
    "complete_payload_bytes": 305143,
    "complete_payload_sha256": "b2a6f4f62684c3d820cb81a6b0bc5a8311957d47a12749d45fb7657948f24515",
    "prior_reuse_payload_bytes": 1135,
    "prior_reuse_payload_sha256": "46480623a3a683dd1a202c9b1f2f47f7105ca43580c5e64d85aa1546a1944661",
    "original_request_bytes": 36744,
    "original_request_sha256": "fee29f3f625974f907376c09b1e6fdc98843a2ae6511a93af069194f58b36b01",
}
FIRST_ALLOWED_CHANGED = {
    "topics/visible-flex-new-mechanism/scripts/frame_metric_paid_attainer_transfer.py":
        "e6f959d90b1e351794fedecb10d5f6f3f19230b7f5cc4485a2628e8aedf3bb3e",
    "topics/visible-flex-new-mechanism/scripts/frame_metric_paid_attainer_resume.py":
        "70efdee2191fe5da8e1327f2c244dc8dc7d87d028e8f387fbb91e2d24abe9cbf",
    "topics/visible-flex-new-mechanism/scripts/frame_metric_paid_attainer_audit.py":
        "922e163abce193a60b871ec951bcec50e4b5135ea00f11dda40ec7af4f75eea1",
    ".github/workflows/visible-paid-attainer-refinement.yml":
        "474e942e53b0f5cfdebea94601e23332ce03beb4a04d5049c10b56f8ced3fbcc",
}
ORDINARY_FIELD_SHA256 = "047cefae968152d170387cf64a9f7b0f132089685472c10868de9379967d93e9"


def _nonnegative_seconds(value, label):
    require(type(value) in (int, float) and math.isfinite(value) and value >= 0,
            "finite nonnegative recorded seconds required: "+label)
    return float(value)


def read_paid_first_attempt(request):
    """Read the fixed failed constructor receipt; execute none of its16 checks."""
    source = request["paid_first_attempt"]
    require(all(source.get(key) == value for key, value in FIRST_ATTEMPT.items()),
            "only the pinned first paid-attainer constructor failure can be consumed")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+source["run_id"])
    job = api.api_json("/actions/jobs/"+source["job_id"])
    require(str(run["id"]) == source["run_id"] and str(job["id"]) == source["job_id"]
            and str(job["run_id"]) == source["run_id"]
            and run["head_sha"] == job["head_sha"] == source["source_commit"],
            "first-attempt run/job/head link differs")
    require(run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "failure",
            "the paid first attempt must be the completed constructor failure")
    raw, redirects = api.job_log(source["job_id"])
    require(len(raw) == source["log_bytes"] and reader.digest(raw) == source["log_sha256"],
            "first-attempt original log bytes differ")
    records = inherited.tagged_records(raw, (
        "PAID_ATTAINER_REQUEST", "PAID_ATTAINER_DEVELOPMENT",
        "PAID_ATTAINER_PRIOR_WORK_REUSED", "PAID_ATTAINER_COMPLETE",
        "PAID_ATTAINER_MODEL", "PAID_ATTAINER_ENTRY_ERROR"))
    require(not records["PAID_ATTAINER_MODEL"] and not records["PAID_ATTAINER_ENTRY_ERROR"],
            "the pinned constructor failure cannot contain a new model or a different entry error")
    old_request = _one(records, "PAID_ATTAINER_REQUEST", source,
                       "request_record_bytes", "request_record_sha256")
    development = _one(records, "PAID_ATTAINER_DEVELOPMENT", source,
                       "development_bytes", "development_sha256")
    prior = _one(records, "PAID_ATTAINER_PRIOR_WORK_REUSED", source,
                 "prior_reuse_payload_bytes", "prior_reuse_payload_sha256")
    complete = _one(records, "PAID_ATTAINER_COMPLETE", source,
                    "complete_payload_bytes", "complete_payload_sha256")
    require(old_request["source_commit"] == source["source_commit"]
            and old_request["request_bytes"] == source["original_request_bytes"]
            and old_request["request_sha256"] == source["original_request_sha256"],
            "first-attempt153-source request identity differs")
    old_files, current_files = old_request["source_sha256"], request["source_sha256"]
    require(len(old_files) == len(current_files) == 153
            and set(old_files) == set(current_files)
            and set(FIRST_ALLOWED_CHANGED).issubset(old_files),
            "the same complete153-file source/workflow closure is required")
    for path, expected in old_files.items():
        if path in FIRST_ALLOWED_CHANGED:
            require(expected == FIRST_ALLOWED_CHANGED[path],
                    "unexpected original identity of an allowed changed file: "+path)
        else:
            require(current_files[path] == expected,
                    "an already-paid source changed: "+path)
        require(reader.digest(Path(path).read_bytes()) == current_files[path],
                "current requested file bytes differ: "+path)
    old_python = {Path(path).name: value for path, value in old_files.items()
                  if path.endswith(".py")}
    require(len(old_python) == 146
            and sum(path.endswith(".py") for path in old_files) == 146
            and sum(path.endswith(".py") and path not in FIRST_ALLOWED_CHANGED
                    for path in old_files) == 143
            and development["source_files_sha256"] == old_python
            and complete["source_files_sha256"] == old_python,
            "paid146 Python closure,143 unchanged sources or receipt binding differs")
    expected_development_sources = {
        name: old_python[name] for name in (
            "frame_metric_paid_attainer_refinement.py",
            "frame_metric_paid_attainer_refinement_development.py")}
    require(development["schema"] == POLICY+"-development"
            and development["source_sha256"] == expected_development_sources
            and development["all_passed"] is True
            and development["new_group_count"] == 4
            and development["new_check_count"] == development["executed_check_count"] == 16,
            "all sixteen original new-interface checks must have passed")
    groups = development["groups"]
    require([g["name"] for g in groups] == [
                "paid_witness_and_same_model_binding",
                "valid_supports_and_original_memory_retention",
                "single_new_call_and_inherited_budget",
                "repaired_candidate_and_original_return_gates"]
            and all(g["planned_checks"] == g["completed_checks"] == len(g["checks"]) == 4
                    and g["passed"] is True and all(v is True for v in g["checks"].values())
                    for g in groups)
            and development["execution"] == {
                "new_stub_solver_calls": 5, "real_LP_calls": 0,
                "ordinary_geometry_calls": 0, "full_directional_JVP_calls": 0,
                "original_developer_suites_executed": 0}
            and development["old_science_and_old_developer_execution_count"] == 0,
            "original4x4 check verdicts or execution scope differ")
    require(prior["passed"] is True
            and prior["original_source_python_files"] == 140
            and prior["original_request_bound_files"] == 146
            and prior["original_guard_development_checks"] == 18
            and prior["old_development_executions"] == 0
            and prior["old_optimizer_LP_JVP_trial_replays"] == 0
            and prior["transitive_old20_19_26_and_cache_receipts_checked"] is True,
            "first-attempt prior-work receipt differs")
    stage = complete["paid_attainer_refinement_stage"]
    require(complete["schema"] == POLICY+"-audit"
            and complete["status"] == "paid-attainer-audit-error-paid-best-preserved"
            and complete["github_sha"] == source["source_commit"]
            and str(complete["github_run_id"]) == source["run_id"]
            and complete["github_repository"] == REPO
            and complete["error"]["type"] == "ValueError"
            and complete["error"]["message"] ==
                "same epoch ordinary evaluation definition could not be restored exactly"
            and "frame_metric_paid_attainer_resume.py" in complete["error"]["traceback"]
            and complete["new_scientific_solver_entry_calls"] == 0
            and complete["old_optimizer_calls_this_run"] == 0
            and complete["old_LP10_or_old_direction_replays"] == 0
            and complete["old_development_group_executions"] == 0
            and stage["model_count"] == 0 and stage["new_accepted_iterates"] == []
            and stage["solver"] == {}
            and stage["selected_two_grid_physical_point"] is None
            and stage["snapshot_scalar_counters"] == {},
            "only the exact pre-recovery identity failure with no model or new acceptance is reusable")
    require(complete["source_paid_ledger"] == {
                "linear_program_invocation_count": 10,
                "primary_LP_invocation_count": 10,
                "correction_LP_invocation_count": 0}
            and complete["future_direct_checkpoint"]["selected_physical_state_sha256"] ==
                request["source"]["final_physical_sha256"]
            and complete["future_direct_checkpoint"]["norm_direction_bank_state_sha256"] ==
                request["source"]["terminal_norm_bank_state_sha256"],
            "paid failure advanced the original ledger or checkpoint")
    active = _nonnegative_seconds(
        complete["timing_segments"]["restoration_or_recovery_wall_until_error_seconds"],
        "first failed constructor active cost")
    prepare = _nonnegative_seconds(complete["prepare_elapsed_seconds"], "first failed preparation")
    total = _nonnegative_seconds(complete["process_total_elapsed_seconds"], "first failed total")
    require(active == 0.08626015199990889 and prepare == 14.667315975000065
            and total >= prepare+active, "pinned first-attempt paid cost differs")
    counters = copy.deepcopy(complete["source_paid_value_and_clock_counters"])
    for key in ("initialization_elapsed_seconds", "optimization_elapsed_seconds",
                "value_geometry_seconds"):
        _nonnegative_seconds(counters[key], "source "+key)
    require(counters["total_full_value_physical_evaluations"] == 14,
            "first-attempt source value ledger differs")
    receipt = {
        "schema": POLICY+"-paid-first-attempt-reuse", "passed": True,
        "source_run_id": source["run_id"], "source_job_id": source["job_id"],
        "source_commit": source["source_commit"], "original_conclusion": "failure",
        "original_log_bytes": len(raw), "original_log_sha256": reader.digest(raw),
        "request_JSON_plus_LF_bytes": source["request_record_bytes"],
        "request_JSON_plus_LF_sha256": source["request_record_sha256"],
        "development_JSON_plus_LF_bytes": source["development_bytes"],
        "development_JSON_plus_LF_sha256": source["development_sha256"],
        "complete_JSON_plus_LF_bytes": source["complete_payload_bytes"],
        "complete_JSON_plus_LF_sha256": source["complete_payload_sha256"],
        "prior_JSON_plus_LF_bytes": source["prior_reuse_payload_bytes"],
        "prior_JSON_plus_LF_sha256": source["prior_reuse_payload_sha256"],
        "source_bound_files": 153, "source_python_files": 146,
        "unchanged_python_sources": 143, "unchanged_workflows": 6,
        "allowed_changed_paths": list(FIRST_ALLOWED_CHANGED),
        "core_development_recovery_sources_unchanged": True,
        "paid_development_groups": 4, "paid_development_checks": 16,
        "new_development_group_executions": 0, "new_development_check_executions": 0,
        "old_optimizer_or_failed_scientific_attempt_replays": 0,
        "first_attempt_new_solver_entries": 0, "first_attempt_new_models": 0,
        "first_attempt_new_accepted_iterates": 0,
        "failure_was_objective_vs_field_hash_domain_mismatch": True,
        "redirects_without_authorization": redirects,
        "payload_stays_in_runner_memory_not_Git_artifact_or_Release": True}
    paid_cost = {
        "failed_resume_active_seconds": active, "prepare_elapsed_seconds": prepare,
        "process_total_elapsed_seconds": total,
        "source_snapshot_scalar_counters": counters,
        "new_primary_LPs": 0, "new_SOC_LPs": 0, "new_shared_values": 0,
        "total_elapsed_is_retained_separately_not_all_charged_as_active": True,
        "already_paid_development_and_metadata_overhead_not_reclassified_as_science": True}
    return {"receipt": receipt, "paid_cost": paid_cost}


def _same_epoch_evaluation_domains(source_model):
    binding = source_model["linear_program"]["complete_original_grid_model"]["summary"]["binding"]
    caches = binding["selected_observable_binding"]["external_current_cache_binding"]
    require(isinstance(caches, list) and len(caches) == 2
            and [item["grid"] for item in caches] == ["coarse", "fine"],
            "paid coarse/fine selected-cache order is required")
    hashes = [item["evaluation_sha256"] for item in caches]
    require(hashes[0] == hashes[1] and isinstance(hashes[0], str)
            and len(hashes[0]) == 64
            and all(c in "0123456789abcdef" for c in hashes[0]),
            "both selected caches must bind one complete objective definition")
    ordinary = binding["full_grid_oracle_binding"]["ordinary_evaluation_definition_sha256"]
    require(ordinary == ORDINARY_FIELD_SHA256,
            "paid ordinary field evaluation definition differs")
    return hashes[0], ordinary


def read_completed(request):
    source = request["source"]
    require(str(source["run_id"]) == SOURCE_RUN and str(source["job_id"]) == SOURCE_JOB
            and source["source_commit"] == SOURCE_COMMIT, "fixed seventh-model source required")
    raw, redirects = inherited.completed_log(source)
    records = inherited.tagged_records(raw, (
        "CURVATURE_GUARD_REQUEST", "CURVATURE_GUARD_MODEL",
        "CURVATURE_GUARD_COMPLETE", "CURVATURE_GUARD_DEVELOPMENT",
        "CURVATURE_GUARD_DEVELOPMENT_REUSE", "CURVATURE_GUARD_PRIOR_WORK_REUSED"))
    real = _one(records, "CURVATURE_GUARD_COMPLETE", source,
                "complete_payload_bytes", "complete_payload_sha256")
    development = _one(records, "CURVATURE_GUARD_DEVELOPMENT", source,
                       "development_bytes", "development_sha256")
    prior = _one(records, "CURVATURE_GUARD_PRIOR_WORK_REUSED", source,
                 "prior_reuse_payload_bytes", "prior_reuse_payload_sha256")
    reuse = _one(records, "CURVATURE_GUARD_DEVELOPMENT_REUSE", source,
                 "development_reuse_bytes", "development_reuse_sha256")
    original_request = _one(records, "CURVATURE_GUARD_REQUEST", source,
                            "request_record_bytes", "request_record_sha256")
    require(real["schema"] == SOURCE_SCHEMA and real["status"] == SOURCE_COMPLETE
            and real["github_sha"] == SOURCE_COMMIT
            and str(real["github_run_id"]) == SOURCE_RUN
            and real["github_repository"] == REPO, "completed original provenance differs")
    count = inherited.check_current_sources(real["source_files_sha256"], 140)
    require(original_request["source_commit"] == SOURCE_COMMIT
            and len(original_request["source_sha256"]) == 146
            and original_request["request_bytes"] == 36687
            and original_request["request_sha256"] ==
                "f85013ec1af5d3e14881412708f14228252d160953f9eddebd78cca281164cc4",
            "original146-file request binding differs")
    for name, expected in original_request["source_sha256"].items():
        require(reader.digest(Path(name).read_bytes()) == expected,
                "frozen requested source differs: "+name)
    require(development["source_files_sha256"] == real["source_files_sha256"]
            and development["passed"] is True and development["all_passed"] is True
            and [(g["name"], len(g["checks"])) for g in development["groups"]] == [
                ("original_RHS_scope_and_final_factory_binding", 5),
                ("actual_step_and_delayed_defect_learning", 5),
                ("original_SOC_and_infeasible_proposal_scope", 4),
                ("three_seventy_five_entry_and_paid_sample_linkage", 4)]
            and all(g["passed"] is True and all(v is True for v in g["checks"].values())
                    for g in development["groups"])
            and development["reused_development_checks"] == 14
            and development["reused_development_groups"] == 3
            and development["new_development_checks_evaluated"] == 4
            and development["new_development_checks_passed"] == 4
            and development["new_development_groups_executed"] == 1
            and all(development[k] == 0 for k in (
                "first_three_development_group_executions_this_run",
                "old_developer_suite_executions", "scientific_inputs",
                "scientific_JVP_calls", "geometry_calls", "LP_calls", "optimizer_calls")),
            "paid18-check receipt or original reuse boundary differs")
    require(prior["paid_cache_evidence"]["passed"] is True
            and prior["original_source"]["all135_frozen_sources_match_current_files"] is True
            and prior["original_source"]["paid_cache_evidence_from_source_log"]
                == prior["paid_cache_evidence"]
            and all(prior[k] == 0 for k in prior
                    if k not in ("original_source", "paid_cache_evidence")),
            "transitive paid20/19/26/cache evidence or zero replay counters differ")
    models = [item[1] for item in records["CURVATURE_GUARD_MODEL"]]
    require([m["number"] for m in models] == list(range(1, 8)), "all seven native models required")
    m7 = models[-1]
    payload7 = (records["CURVATURE_GUARD_MODEL"][-1][0]+"\n").encode("utf-8")
    require(len(payload7) == source["model7_bytes"]
            and reader.digest(payload7) == source["model7_sha256"], "native model7 bytes differ")
    cp, stage = real["future_direct_checkpoint"], real[SOURCE_STAGE]
    for key, expected in source["checkpoint_list_sha256"].items():
        require(reader.digest(json_bytes(cp[key])) == expected, "checkpoint list differs: "+key)
    require(cp["selected_physical_state_sha256"] == source["final_physical_sha256"]
            and cp["norm_direction_bank_state_sha256"] == source["terminal_norm_bank_state_sha256"]
            and len(cp["norm_direction_bank_entries"]) == 438
            and [len(cp["coarse_pool"]), len(cp["fine_pool"])] == [4432, 4525],
            "exact current physical point, bank or row pools differ")
    require(digest({"context": cp["norm_direction_bank_context"],
                    "entries": cp["norm_direction_bank_entries"]})
            == cp["norm_direction_bank_state_sha256"], "ordered bank digest differs")
    accepted = [(m["number"], j, t) for m in models for j, t in enumerate(m.get("trials", []))
                if t.get("accepted_as_next_iterate") is True]
    require(len(accepted) == 6, "six original accepted ordinary trials required")
    number, trial_index, last = max(accepted, key=lambda t: t[2]["accepted_index"])
    require((number, trial_index, last["accepted_index"]) == (6, 0, 6)
            and last["kind"] == "primary-metric-short-step"
            and last["alpha_exact"] == "1"
            and last["physical_state_sha256"] == cp["selected_physical_state_sha256"]
            and last["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and last["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"],
            "source accepted exact point is not the seventh-model center")
    require(real["final_selection_validation"]["both_value_grids_hard_and_old_metric_pass"] is True
            and real["final_selection_validation"]["both_grid_maximum_eta"] ==
                source["final_both_grid_maximum_eta"], "paid final two-grid selection differs")
    require(m7["linearized_at_physical_sha256"] == cp["selected_physical_state_sha256"]
            and m7["linearized_at_accepted_index"] == 6
            and m7["trials"] == [] and m7["corrections"] == []
            and "exact_binary64_independent_proposed_step" not in m7,
            "this is not the paid unevaluated missing-step seventh model")
    events = m7["linear_program"]["complete_original_grid_model"]["oracle"]["direction_events"]
    events = [e for e in events if e.get("ordinal") == 1
              and e.get("phase") == "primary-inner" and e.get("status") == "complete"]
    require(len(events) == 1, "one paid completed nonzero direction required")
    event = copy.deepcopy(events[0])
    duplicate = real["complete_original_grid_oracle_progress"][6]["direction_events"]
    require(event in duplicate, "native and COMPLETE directional receipts disagree")
    for name in ("center_binding_sha256", "direction_sha256"):
        require(event[name] == PINS[name], "source witness identity differs: "+name)
    for name in ("attainers", "grid_scans", "maxima"):
        got = fingerprint(event[name])
        require((got["canonical_json_bytes"], got["canonical_json_sha256"]) == PINS[name],
                "source witness payload differs: "+name)
    solver = stage["solver"]
    require(tuple(solver[k] for k in ("linear_program_invocation_count",
            "primary_LP_invocation_count", "correction_LP_invocation_count")) == (10, 10, 0)
            and stage["model_count"] == 7, "original paid ledger differs")
    counts = stage["snapshot_scalar_counters"]
    require(counts["total_full_value_physical_evaluations"] == 14
            and (last["coarse_physical_evaluation"], last["fine_value_evaluation"]) == (7, 7)
            and math.isfinite(counts["optimization_elapsed_seconds"])
            and 0 < counts["optimization_elapsed_seconds"] < 120,
            "paid actual-value or active-time counters differ")
    learning = cp["curvature_defect_guard_learning_checkpoint"]
    require(learning == stage["curvature_defect_guard_learning_checkpoint"]
            and learning["pending_event_indices"] == [] and len(learning["events"]) == 8
            and all(e.get("committed") is True for e in learning["events"])
            and learning["state_sha256"] == source["learning_state_sha256"]
            and m7["curvature_defect_guard"]["frozen_learning_state_sha256"] ==
                learning["state_sha256"], "committed m7 learning state differs")
    paid = {
        "passed": True, "original_source_python_files": count, "original_request_bound_files": 146,
        "original_guard_development_groups": 4, "original_guard_development_checks": 18,
        "old_development_executions": 0, "old_optimizer_LP_JVP_trial_replays": 0,
        "transitive_old20_19_26_and_cache_receipts_checked": True,
        "additional_previous_scientific_or_failed_development_log_downloads": 0,
        "original_log_bytes": len(raw), "original_log_sha256": reader.digest(raw),
        "complete_json_plus_LF_sha256": source["complete_payload_sha256"],
        "development_json_plus_LF_sha256": source["development_sha256"],
        "development_reuse_json_plus_LF_sha256": source["development_reuse_sha256"],
        "prior_reuse_json_plus_LF_sha256": source["prior_reuse_payload_sha256"],
        "model7_json_plus_LF_sha256": source["model7_sha256"],
        "redirects_without_authorization": redirects,
        "unknown_old159_step_not_reconstructed": True,
        "only_paid_witness_observables_used_for_new_global_lower_supports": True}
    return real, models, cp, event, paid


def prepare_transfer(request, output, process_started, *, completed, paid_first_attempt):
    real, models, cp, event, paid = completed
    require(isinstance(paid_first_attempt, dict)
            and paid_first_attempt["receipt"]["passed"] is True
            and paid_first_attempt["receipt"]["source_run_id"] == FIRST_ATTEMPT["run_id"]
            and paid_first_attempt["receipt"]["source_job_id"] == FIRST_ATTEMPT["job_id"],
            "validated first-attempt receipt is required before necessary input recovery")
    first_cost = copy.deepcopy(paid_first_attempt["paid_cost"])
    source_counters = copy.deepcopy(real[SOURCE_STAGE]["snapshot_scalar_counters"])
    require(first_cost["source_snapshot_scalar_counters"] == source_counters,
            "first failed attempt and paid source epoch counters differ")
    inherited_counters = copy.deepcopy(source_counters)
    for name, delta_name in (
            ("optimization_elapsed_seconds", "failed_resume_active_seconds"),
            ("initialization_elapsed_seconds", "prepare_elapsed_seconds")):
        before = _nonnegative_seconds(source_counters[name], "source "+name)
        delta = _nonnegative_seconds(first_cost[delta_name], "first-attempt "+delta_name)
        combined = before+delta
        require(math.isfinite(combined), "combined inherited time is nonfinite: "+name)
        inherited_counters[name] = combined
    objective_sha, ordinary_field_sha = _same_epoch_evaluation_domains(models[-1])
    args = inherited.previous.old_input_namespace(request, output)
    prepared = baseline.growth.prepare_run(args, process_started=process_started)
    restored, bindings, tenth, old_replay, coarse24, fine24 = prepared
    original, _, original_gate, lower, upper, source_cfg, _ = restored
    field, initial, gate, field_transfer = inherited.reconstruct_checkpoint_field(
        original, original_gate, lower, upper, cp, request)
    cfg = copy.deepcopy(real["configuration"])
    require(digest(cfg) == request["source"]["configuration_sha256"]
            and (cfg["max_linear_models"], cfg["max_physical_evaluations"],
                 cfg["max_seconds"], cfg["linear_program_seconds"]) == (12, 40, 120, 10),
            "unchanged original configuration and limits required")
    radial, theta, grid = baseline.curvature_grid(tenth)
    counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    coarse = inherited.checked_pool(cp["coarse_pool"], counts["coarse"],
                                    cfg["max_pool_rows"], "coarse")
    fine = inherited.checked_pool(cp["fine_pool"], counts["fine"],
                                  cfg["max_fine_physical_pool_rows"], "fine")
    require(cp["norm_direction_bank_context"]["original_point_counts"] == counts,
            "saved bank is not on the original complete grids")
    stage = real[SOURCE_STAGE]
    require(cp["terminal_trust"] == .00025
            and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0
            and cp["terminal_trust"] == stage["last_restricted_trust"]
            and models[-1]["trust_before_model"] == cp["terminal_trust"]
            and [models[-1]["coarse_pool_version"], models[-1]["fine_pool_version"]] == [1, 2],
            "seventh-model radius, streaks or pool versions differ")
    controller = {
        "schema": "paid-seventh-model-mid-epoch-controller-v1",
        "origin": "fixed guard epoch model7 before an unevaluated refinement",
        "trust_binary64_exact": str(Q.from_float(float(cp["terminal_trust"]))),
        "trust_evaluated": cp["terminal_trust"],
        "success_streak": cp["terminal_success_streak"],
        "covered_ordinary_success_streak": cp["terminal_covered_ordinary_growth_streak"],
        "source_last_accepted_model": 6, "source_resumed_model": 7,
        "radius_or_success_streak_reset": False}
    replay = {
        "policy": POLICY, "original_report": real, "source_model": copy.deepcopy(models[-1]),
        "source_event": event, "source_checkpoint": cp, "paid_evidence": paid,
        "source_completed_log_transfer": {"source_run_id": SOURCE_RUN, "source_job_id": SOURCE_JOB,
            "source_commit": SOURCE_COMMIT, "field_transfer": field_transfer,
            "paid_evidence": copy.deepcopy(paid), "unknown_old159_step_not_serialized": True},
        "canonical_physical_state_sha256": digest(field.identity(initial)),
        "layout_derived_from_actual_problem": baseline.layout_from_problem(original),
        "controller_continuation": controller, "pool_versions": [1, 2],
        "initial_bank_context": copy.deepcopy(cp["norm_direction_bank_context"]),
        "initial_bank_entries": copy.deepcopy(cp["norm_direction_bank_entries"]),
        "expected_initial_bank_state_sha256": cp["norm_direction_bank_state_sha256"],
        "expected_initial_bank_entries": 438,
        "curvature_learning_checkpoint": copy.deepcopy(cp["curvature_defect_guard_learning_checkpoint"]),
        "epoch_original_metadata": {
            "expected_initial_bank": {
                "state_sha256": stage["initial_complete_checkpoint_bank_input"]["expected_state_sha256"],
                "entries": 375, "source": "complete ordered375 current-best checkpoint, no event replay"},
            "complete_value_sampling_definition": copy.deepcopy(real["full_value_sampling_definition"]),
            "direct_completed_source_transfer": copy.deepcopy(real["direct_transfer_source_and_scope"]),
            "complete_checkpoint_pool_transfer": copy.deepcopy(real["learned_pool_replay"]),
            "new_constraint_role_definition": copy.deepcopy(real["new_constraint_role_definition"]),
            "height159_SOC_hold_controller_initialization":
                copy.deepcopy(stage["solver"]["inherited159_controller_without_reset"])},
        "epoch_evaluation_sha256": objective_sha,
        "ordinary_field_evaluation_sha256": ordinary_field_sha,
        "inherited_ledger": {key: stage["solver"][key] for key in (
            "linear_program_invocation_count", "primary_LP_invocation_count",
            "correction_LP_invocation_count")},
        "source_snapshot_scalar_counters": source_counters,
        "inherited_counters": inherited_counters,
        "paid_first_attempt": {
            "receipt": copy.deepcopy(paid_first_attempt["receipt"]), "paid_cost": first_cost},
        "inherited_coarse_values": 7, "inherited_fine_values": 7,
        "inherited_accepted_iterates": copy.deepcopy(stage["accepted_iterates"]),
        "inherited_bank_report": copy.deepcopy(stage["cross_center_norm_memory"]),
        "paid_initial_sample_receipts": copy.deepcopy(
            real["curvature_defect_guard_observation"]["paid_initial_samples"]),
        "source_final_gate_and_value_report_consumed_without_old_optimizer": True,
        "no_source_pool_initialization_or_paid_sample_retraining": True}
    require(grid == replay["epoch_original_metadata"]["complete_value_sampling_definition"],
            "original full-value grid definition changed")
    return ((field, initial, gate, gate.coordinate_lower, gate.coordinate_upper,
             source_cfg, cfg), bindings, tenth, replay, coarse, fine)

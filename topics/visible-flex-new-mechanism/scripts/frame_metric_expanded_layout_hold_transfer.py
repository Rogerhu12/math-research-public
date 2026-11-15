#!/usr/bin/env python3
"""Direct current-best checkpoint and paid-evidence input for the new radius policy.

Only immutable completed output is read. No predecessor optimizer, developer
suite, original direction event, or historical m10 trial is executed again.
All new execution belongs to this public repository's GitHub Actions.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import json
import os
from pathlib import Path

from frame_height_null_coordinates import digest
import frame_metric_height159_complete_affine_audit as baseline
import frame_metric_norm_memory_transfer as previous
import frame_metric_expanded_pool_soc_transfer as frozen_transfer
import read_original_actions_log as reader

REPO = previous.REPO
ROOT = previous.ROOT
POLICY = "same159-covered-expanded-pool-small-SOC-retains-model-radius-v1"
SOURCE_SCHEMA = "same159-complete-checkpoint-expanded-pool-SOC-v1"
SOURCE_STAGE = "expanded_pool_SOC_stage"
require = previous.require
json_bytes = previous.json_bytes
file_sha = previous.file_sha
reconstruct_checkpoint_field = frozen_transfer.reconstruct_checkpoint_field
checked_pool = frozen_transfer.checked_pool


def tagged_records(raw, tags):
    """Keep each original JSON spelling plus LF; tolerate BOM in the log prefix."""
    found = {tag: [] for tag in tags}
    for line in raw.decode("utf-8").splitlines():
        for tag in tags:
            marker = tag+" "
            pos = line.find(marker)
            if pos < 0:
                continue
            payload = line[pos+len(marker):]
            require(payload.startswith("{"), "original tagged record must be an object")
            found[tag].append((payload, json.loads(payload)))
    return found


def completed_log(source):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "public repository Actions required")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+str(source["run_id"]))
    job = api.api_json("/actions/jobs/"+str(source["job_id"]))
    require(run["head_sha"] == job["head_sha"] == source["source_commit"],
            "completed run/job/source identity differs")
    require(run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "success",
            "completed successful original output required")
    require(int(job["run_id"]) == int(run["id"]), "original run/job linkage differs")
    raw, redirects = api.job_log(str(source["job_id"]))
    require(len(raw) == source["log_bytes"]
            and reader.digest(raw) == source["log_sha256"],
            "immutable original log bytes differ")
    return raw, redirects


def check_current_sources(manifest, expected_count):
    require(isinstance(manifest, dict) and len(manifest) == expected_count,
            "original dependency count differs")
    folder = Path(__file__).parent
    for name, expected in manifest.items():
        require(Path(name).name == name and file_sha(folder/name) == expected,
                "frozen original source changed: "+name)
    return len(manifest)


def read_completed(request):
    source = request["source"]
    raw, redirects = completed_log(source)
    records = tagged_records(raw, ("EXPANDED_SOC_MODEL", "EXPANDED_SOC_COMPLETE",
                                  "EXPANDED_SOC_DEVELOPMENT"))
    require(len(records["EXPANDED_SOC_COMPLETE"]) == 1
            and len(records["EXPANDED_SOC_DEVELOPMENT"]) == 1,
            "unique original complete/development record required")
    payload, real = records["EXPANDED_SOC_COMPLETE"][0]
    complete_bytes = (payload+"\n").encode("utf-8")
    require(len(complete_bytes) == source["complete_payload_bytes"]
            and reader.digest(complete_bytes) == source["complete_payload_sha256"],
            "original COMPLETE JSON plus LF differs")
    require(real["schema"] == SOURCE_SCHEMA
            and real["status"] == "complete-two-grid-expanded-pool-SOC-checkpoint-audit",
            "original expanded stage schema/status differs")
    require(real["github_sha"] == source["source_commit"]
            and str(real["github_run_id"]) == str(source["run_id"])
            and real["github_repository"] == REPO, "original report provenance differs")
    count = check_current_sources(real["source_files_sha256"], 117)
    development_payload, development = records["EXPANDED_SOC_DEVELOPMENT"][0]
    development_bytes = (development_payload+"\n").encode("utf-8")
    require(len(development_bytes) == source["development_bytes"]
            and reader.digest(development_bytes) == source["development_sha256"],
            "paid expanded development receipt differs")
    require(development.get("passed") is True and development.get("all_passed") is True
            and len(development.get("checks", {})) == 10
            and all(value is True for value in development["checks"].values())
            and development["source_files_sha256"] == real["source_files_sha256"],
            "paid ten-check evidence or unchanged source closure differs")
    models = [item[1] for item in records["EXPANDED_SOC_MODEL"]]
    require([m["number"] for m in models] == list(range(1, 8)),
            "all seven native completed models required, including BOM-prefixed records")
    cp = real["future_direct_checkpoint"]
    for key, expected in source["checkpoint_list_sha256"].items():
        require(reader.digest(json_bytes(cp[key])) == expected,
                "original exact checkpoint list differs: "+key)
    require(cp["selected_physical_state_sha256"] == source["final_physical_sha256"]
            and cp["norm_direction_bank_state_sha256"] == source["terminal_norm_bank_state_sha256"]
            and len(cp["norm_direction_bank_entries"]) == 11,
            "original best point or complete eleven-entry bank differs")
    accepted = [(m["number"], j, t) for m in models
                for j, t in enumerate(m.get("trials", []))
                if t.get("accepted_as_next_iterate") is True]
    require(len(accepted) == 7, "seven original accepted iterates required")
    number, trial, final = max(accepted, key=lambda item: item[2]["accepted_index"])
    require(number == 7 and final["accepted_index"] == 7
            and final["physical_state_sha256"] == cp["selected_physical_state_sha256"],
            "native final model7 and checkpoint differ")
    require(final["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and final["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"],
            "native exact independent159/physical163 differs from checkpoint")
    require(real["final_selection_validation"]["both_value_grids_hard_and_old_metric_pass"] is True,
            "source independent final original gates failed")
    require(real["final_selection_validation"]["both_grid_maximum_eta"]
            == source["final_both_grid_maximum_eta"],
            "source selected best eta differs")
    metadata = {
        "original_run_id": source["run_id"], "original_job_id": source["job_id"],
        "original_source_commit": source["source_commit"],
        "original_log_bytes": len(raw), "original_log_sha256": reader.digest(raw),
        "original_complete_payload_bytes": len(complete_bytes),
        "original_complete_payload_sha256": reader.digest(complete_bytes),
        "all117_frozen_sources_match_current_files": count == 117,
        "final_native_model": number, "final_native_trial": trial,
        "original_exact159_reference163_and_physical163_read_without_rounding": True,
        "full_completed_coarse_and_fine_row_lists_present": True,
        "complete_ordered_norm_bank_read_without_event_replay": True,
        "old_optimizer_calls": 0, "old_development_executions": 0,
        "redirects_without_authorization": redirects,
        "payloads_only_in_runner_memory_and_semantic_stdout": True,
        "paid_expanded_development_reused": {
            "passed": True, "checks": 10, "new_executions": 0,
            "bytes": len(development_bytes), "sha256": reader.digest(development_bytes)}}
    return real, models, cp, metadata


def reuse_paid_cache_evidence(request):
    """Consume the successful new positive and already-reused negative receipt."""
    source = request["reuse_completed_cache"]
    raw, redirects = completed_log(source)
    records = tagged_records(raw, ("M10_SOC_CACHE_DEVELOPMENT", "M10_SOC_COMPLETE"))
    require(len(records["M10_SOC_CACHE_DEVELOPMENT"]) == 1
            and len(records["M10_SOC_COMPLETE"]) == 1,
            "unique completed cache and actual science receipts required")
    payload, receipt = records["M10_SOC_CACHE_DEVELOPMENT"][0]
    data = (payload+"\n").encode("utf-8")
    require(len(data) == source["development_bytes"]
            and reader.digest(data) == source["development_sha256"],
            "paid cache receipt bytes differ")
    require(receipt.get("passed") is True and receipt.get("all_passed") is True
            and len(receipt.get("checks", {})) == 2
            and all(v is True for v in receipt["checks"].values())
            and receipt["new_positive_cache_executions"] == 1
            and receipt["old_charged_miss_executions"] == 0
            and receipt["old_m10_seven_executions"] == 0
            and receipt["old_expanded_ten_executions"] == 0,
            "successful original cache receipt scope differs")
    count = check_current_sources(receipt["source_files_sha256"], 120)
    complete_payload, complete = records["M10_SOC_COMPLETE"][0]
    complete_data = (complete_payload+"\n").encode("utf-8")
    require(len(complete_data) == source["complete_payload_bytes"]
            and reader.digest(complete_data) == source["complete_payload_sha256"],
            "completed historical SOC evidence differs")
    require(complete["status"] == "complete-historical-m10-expanded-SOC-accepted"
            and complete["github_sha"] == source["source_commit"]
            and str(complete["github_run_id"]) == str(source["run_id"])
            and complete["github_repository"] == REPO,
            "successful actual cached-y capture evidence differs")
    return {
        "schema": POLICY+"-paid-cache-evidence", "passed": True,
        "original_run_id": source["run_id"], "original_job_id": source["job_id"],
        "original_source_commit": source["source_commit"],
        "original_log_bytes": len(raw), "original_log_sha256": reader.digest(raw),
        "original_development_bytes": len(data), "original_development_sha256": reader.digest(data),
        "original_complete_bytes": len(complete_data),
        "original_complete_sha256": reader.digest(complete_data),
        "unchanged_source_count": count,
        "same_y_helper_positive_and_charged_miss_evidence_reused": True,
        "old_expanded_ten_m10_seven_and_cache_two_new_executions": 0,
        "historical_m10_trial_primary_or_SOC_replays": 0,
        "redirects_without_authorization": redirects}


def prepare_transfer(request, output, process_started, *, completed=None):
    real, models, cp, source = read_completed(request) if completed is None else completed
    args = previous.old_input_namespace(request, output)
    prepared = baseline.growth.prepare_run(args, process_started=process_started)
    restored, bindings, tenth, old_replay, coarse24, fine24 = prepared
    original, _, original_gate, lower, upper, source_cfg, _ = restored
    field, initial, gate, field_transfer = reconstruct_checkpoint_field(
        original, original_gate, lower, upper, cp, request)
    cfg = copy.deepcopy(real["configuration"])
    require(digest(cfg) == request["source"]["configuration_sha256"],
            "original current-best configuration hash differs")
    require((cfg["max_linear_models"], cfg["max_physical_evaluations"],
             cfg["max_seconds"], cfg["linear_program_seconds"]) == (12, 40, 120, 10),
            "original shared limits changed")
    radial, theta, grid = baseline.curvature_grid(tenth)
    counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    coarse = checked_pool(cp["coarse_pool"], counts["coarse"], cfg["max_pool_rows"], "coarse")
    fine = checked_pool(cp["fine_pool"], counts["fine"], cfg["max_fine_physical_pool_rows"], "fine")
    require(len(coarse) == 4418 and len(fine) == 4188,
            "current-best complete terminal pool sizes differ")
    require(cp["norm_direction_bank_context"]["original_point_counts"] == counts,
            "checkpoint bank and original full grid sizes differ")
    context = copy.deepcopy(cp["norm_direction_bank_context"])
    entries = copy.deepcopy(cp["norm_direction_bank_entries"])
    bank_sha = cp["norm_direction_bank_state_sha256"]
    require(digest({"context": context, "entries": entries}) == bank_sha
            == request["source"]["terminal_norm_bank_state_sha256"],
            "complete ordered bank context/entries hash differs")
    trust, streak = cp["terminal_trust"], cp["terminal_success_streak"]
    require(trust == .000125 and type(streak) is int and streak == 0,
            "original current-best terminal radius/streak differs")
    stage = real[SOURCE_STAGE]
    require(trust == stage["last_restricted_trust"]
            and streak == stage["final_consecutive_growth_qualifying_models"],
            "checkpoint and native controller differ")
    controller = {
        "schema": "complete-checkpoint-terminal-controller-v1",
        "origin": "immutable expanded run43744903357 final model7 and exact checkpoint",
        "trust_binary64_exact": str(Q.from_float(float(trust))),
        "trust_evaluated": trust, "success_streak": streak,
        "source_last_completed_model": 7, "radius_or_success_streak_reset": False}
    pools = {
        "policy": "both complete current-best terminal row lists; subsequent learning unchanged",
        "full_original_checkpoint_pools_retained": True,
        "seed_counts": {"coarse": len(coarse), "fine": len(fine)},
        "coarse_seed_sha256": digest(coarse), "fine_seed_sha256": digest(fine),
        "source_last_model_primary_pool_versions": [
            models[-1]["coarse_pool_version"], models[-1]["fine_pool_version"]],
        "source_terminal_pool_versions": [
            stage["current_pool_metadata"]["active_row_pool_history"]["version"],
            stage["current_pool_metadata"]["fine_physical_row_pool_history"]["version"]],
        "new_objective_versions_start_with_its_actual_set_pool_calls": True,
        "capacity_and_actual_gates_unchanged": True}
    memory = {
        "policy": "exact complete ordered eleven-entry checkpoint, no original event replay",
        "expected_distinct_bank_entries": 11, "expected_terminal_bank_state_sha256": bank_sha,
        "restored_entries": len(entries), "event_replay_calls": 0,
        "normal_recomputation_calls": 0, "old_numeric_A_b_carried": False,
        "first_current_complete_model_binding_still_required": True}
    source = copy.deepcopy(source)
    source.update(field_transfer=field_transfer, completed_pool_transfer=pools,
                  complete_bank_input=memory, original_controller=controller)
    replay = {
        "source_completed_log_transfer": source,
        "canonical_physical_state_sha256": digest(field.identity(initial)),
        "layout_derived_from_actual_problem": baseline.layout_from_problem(original),
        "learned_pool": pools,
        "explicit_new_constraint_definition": {
            "physical_gates_and_thresholds_unchanged": True, "new_proposal_algorithm": POLICY,
            "source_configuration_and_complete_bank_context_preserved": True,
            "original_SOC_and_acceptance_unchanged_only_next_radius_policy_is_new": True},
        "known_fine_metric_locations": [], "controller_continuation": controller,
        "initial_direction_records": [], "initial_bank_context": context,
        "initial_bank_entries": entries, "original_report": real,
        "expected_initial_bank_state_sha256": bank_sha, "expected_initial_bank_entries": 11,
        "source_final_gate_and_value_report_consumed_without_new_optimizer": True}
    return ((field, initial, gate, gate.coordinate_lower, gate.coordinate_upper,
             source_cfg, cfg), bindings, tenth, replay, coarse, fine)

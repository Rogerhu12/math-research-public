#!/usr/bin/env python3
"""Read the completed current-best checkpoint and paid evidence for LP reservation.

Only run43753280651 output is read. Its previous cache/developer evidence is
consumed transitively inside the byte-pinned successful log and unchanged125
source closure. No prior optimizer, developer, event or historical trial runs.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import json

from frame_height_null_coordinates import digest
import frame_metric_height159_complete_affine_audit as baseline
import frame_metric_expanded_layout_hold_transfer as inherited
import read_original_actions_log as reader
from frame_metric_soc_pair_reservation import POLICY

REPO, ROOT = inherited.REPO, inherited.ROOT
previous = inherited.previous
require, json_bytes = inherited.require, inherited.json_bytes
# Already-paid parser, run/job/log-byte validator and source-file reader.
tagged_records = inherited.tagged_records
completed_log = inherited.completed_log
check_current_sources = inherited.check_current_sources
reconstruct_checkpoint_field = inherited.reconstruct_checkpoint_field
checked_pool = inherited.checked_pool

SOURCE_SCHEMA = "same159-current-best-covered-expanded-layout-SOC-hold-v1"
SOURCE_STAGE = "expanded_layout_SOC_hold_stage"
SOURCE_COMPLETE = "complete-two-grid-covered-expanded-layout-SOC-hold-audit"
SOURCE_RUN = "43753280651"
SOURCE_JOB = "132931742484"
SOURCE_COMMIT = "52a48854e30ddc3d2351ec24274dbe222ef05d9a"


def read_completed(request):
    source = request["source"]
    require(str(source["run_id"]) == SOURCE_RUN
            and str(source["job_id"]) == SOURCE_JOB
            and source["source_commit"] == SOURCE_COMMIT,
            "this new stage starts only from the completed current-best checkpoint")
    raw, redirects = completed_log(source)
    records = tagged_records(raw, (
        "EXPANDED_HOLD_MODEL", "EXPANDED_HOLD_COMPLETE",
        "EXPANDED_HOLD_DEVELOPMENT", "EXPANDED_HOLD_PRIOR_WORK_REUSED"))
    for tag in ("EXPANDED_HOLD_COMPLETE", "EXPANDED_HOLD_DEVELOPMENT",
                "EXPANDED_HOLD_PRIOR_WORK_REUSED"):
        require(len(records[tag]) == 1, "unique original record required: "+tag)
    payload, real = records["EXPANDED_HOLD_COMPLETE"][0]
    complete_bytes = (payload+"\n").encode("utf-8")
    require(len(complete_bytes) == source["complete_payload_bytes"]
            and reader.digest(complete_bytes) == source["complete_payload_sha256"],
            "current-best COMPLETE JSON plus LF differs")
    require(real["schema"] == SOURCE_SCHEMA and real["status"] == SOURCE_COMPLETE,
            "original completed covered-layout schema/status differs")
    require(real["github_sha"] == SOURCE_COMMIT
            and str(real["github_run_id"]) == SOURCE_RUN
            and real["github_repository"] == REPO,
            "current-best report provenance differs")
    count = check_current_sources(real["source_files_sha256"], 125)

    development_payload, development = records["EXPANDED_HOLD_DEVELOPMENT"][0]
    development_bytes = (development_payload+"\n").encode("utf-8")
    require(len(development_bytes) == source["development_bytes"]
            and reader.digest(development_bytes) == source["development_sha256"],
            "paid four-group development receipt differs")
    groups = development.get("groups", [])
    expected_groups = (
        ("covered_expanded_context_and_radius", 6),
        ("new_policy_rejects_incomplete_evidence", 9),
        ("exact_checkpoint_bank_and_first_model", 8),
        ("ordinary_fallback_and_public_entry", 3))
    require(development.get("passed") is True and development.get("all_passed") is True
            and len(groups) == 4
            and [(g.get("name"), len(g.get("checks", {}))) for g in groups]
                == list(expected_groups)
            and all(g.get("passed") is True and
                    all(v is True for v in g["checks"].values()) for g in groups)
            and development["source_files_sha256"] == real["source_files_sha256"]
            and development.get("old_developer_suite_executions") == 0
            and development.get("scientific_inputs") == 0,
            "paid four groups/twenty-six checks or unchanged source closure differs")

    prior_payload, prior = records["EXPANDED_HOLD_PRIOR_WORK_REUSED"][0]
    prior_bytes = (prior_payload+"\n").encode("utf-8")
    require(len(prior_bytes) == source["prior_reuse_payload_bytes"]
            and reader.digest(prior_bytes) == source["prior_reuse_payload_sha256"],
            "byte-pinned previous paid-evidence receipt differs")
    cache = prior["paid_cache_evidence"]
    require(cache.get("passed") is True
            and cache.get("same_y_helper_positive_and_charged_miss_evidence_reused") is True
            and cache.get("unchanged_source_count") == 120
            and cache.get("old_expanded_ten_m10_seven_and_cache_two_new_executions") == 0
            and cache.get("historical_m10_trial_primary_or_SOC_replays") == 0
            and all(prior.get(k) == 0 for k in (
                "old_expanded_ten_executions", "old_m10_seven_executions",
                "old_positive_or_negative_cache_executions", "old_optimizer_calls",
                "historical_m10_trial_replays")),
            "previous paid-cache evidence or no-rerun boundary differs")

    models = [item[1] for item in records["EXPANDED_HOLD_MODEL"]]
    require([m["number"] for m in models] == list(range(1, 8)),
            "all seven original native models required")
    cp = real["future_direct_checkpoint"]
    for key, expected in source["checkpoint_list_sha256"].items():
        require(reader.digest(json_bytes(cp[key])) == expected,
                "current-best exact checkpoint list differs: "+key)
    require(cp["selected_physical_state_sha256"] == source["final_physical_sha256"]
            and cp["norm_direction_bank_state_sha256"] == source["terminal_norm_bank_state_sha256"]
            and len(cp["norm_direction_bank_entries"]) == 22,
            "current-best point or complete twenty-two-entry bank differs")
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
    require(real["final_selection_validation"]["both_value_grids_hard_and_old_metric_pass"] is True
            and real["final_selection_validation"]["both_grid_maximum_eta"]
                == source["final_both_grid_maximum_eta"],
            "current-best final gates or selected eta differs")
    metadata = {
        "original_run_id": SOURCE_RUN, "original_job_id": SOURCE_JOB,
        "original_source_commit": SOURCE_COMMIT,
        "original_log_bytes": len(raw), "original_log_sha256": reader.digest(raw),
        "original_complete_payload_bytes": len(complete_bytes),
        "original_complete_payload_sha256": reader.digest(complete_bytes),
        "all125_frozen_sources_match_current_files": count == 125,
        "final_native_model": number, "final_native_trial": trial,
        "original_exact159_reference163_and_physical163_read_without_rounding": True,
        "full_completed_coarse_and_fine_row_lists_present": True,
        "complete_ordered_norm_bank_read_without_event_replay": True,
        "old_optimizer_calls": 0, "old_development_executions": 0,
        "redirects_without_authorization": redirects,
        "payloads_only_in_runner_memory_and_semantic_stdout": True,
        "paid_previous_hold_development_reused": {
            "passed": True, "groups": 4, "checks": 26, "new_executions": 0,
            "bytes": len(development_bytes), "sha256": reader.digest(development_bytes)},
        "paid_cache_evidence_from_source_log": {
            "passed": True,
            "evidence_mode": "prior successful receipt inside this byte-pinned log and unchanged125 closure",
            "source_prior_reuse_payload_bytes": len(prior_bytes),
            "source_prior_reuse_payload_sha256": reader.digest(prior_bytes),
            "original_paid_cache_receipt": copy.deepcopy(cache),
            "original_prior_work_reused_record": copy.deepcopy(prior),
            "old_cache_or_developer_executions": 0,
            "historical_m10_trial_primary_or_SOC_replays": 0,
            "additional_old_m10_log_downloads": 0},
        "original_hold_policy_observation": copy.deepcopy(real["new_radius_policy_observation"])}
    return real, models, cp, metadata


def reuse_paid_cache_evidence(request, *, completed):
    """Return the evidence already verified while reading the one source log."""
    require(str(request["source"]["run_id"]) == SOURCE_RUN,
            "completed current-best source required for transitive evidence")
    result = copy.deepcopy(completed[3]["paid_cache_evidence_from_source_log"])
    require(result.get("passed") is True, "paid source cache evidence missing")
    return result


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
    require(len(coarse) == 4419 and len(fine) == 4277,
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
        "origin": "immutable covered-layout run43753280651 final model7 and exact checkpoint",
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
        "policy": "exact complete ordered twenty-two-entry checkpoint, no original event replay",
        "expected_distinct_bank_entries": 22, "expected_terminal_bank_state_sha256": bank_sha,
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
            "original_SOC_acceptance_and_radius_controllers_retained": True,
            "new_primary_inner_allocation_inside_original_twelve_LP_total": True,
            "reserved_LP_does_not_imply_SOC_or_retention_success": True},
        "known_fine_metric_locations": [], "controller_continuation": controller,
        "initial_direction_records": [], "initial_bank_context": context,
        "initial_bank_entries": entries, "original_report": real,
        "expected_initial_bank_state_sha256": bank_sha, "expected_initial_bank_entries": 22,
        "source_final_gate_and_value_report_consumed_without_new_optimizer": True}
    return ((field, initial, gate, gate.coordinate_lower, gate.coordinate_upper,
             source_cfg, cfg), bindings, tenth, replay, coarse, fine)

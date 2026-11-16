#!/usr/bin/env python3
"""One read of the latest paid terminal log; no old geometry or solver replay."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
from pathlib import Path
import time
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid
from frame_height_affine_gate import EvaluationBudgetReached
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_metric_direct_reference_epoch import POLICY as DIRECT_POLICY
from frame_metric_terminal_paid_slot import POLICY as TERMINAL_POLICY
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader
from frame_metric_finite_cone_primary import POLICY, require, finite_number
from frame_metric_finite_cone_epoch import LIMITS, SOURCE_SCIENCE_SECONDS, SOURCE_VALUES, SOURCE_LEGACY_COUNTS

REPO, ROOT = inherited.REPO, inherited.ROOT
SOURCE_STAGE = "terminal_paid_slot_stage"
PINS = {
    "run_id": "43789033043", "job_id": "133043031523",
    "source_commit": "a08ed9fb3bd44ece17befa23651b281e67f6bb1b",
    "log_bytes": 2957208,
    "log_sha256": "a465b5f6b09de317c8b9b541953171968543e91f3de3ad52ae4bac9e6dc5f8c0",
    "model_payload_bytes": 146427,
    "model_payload_sha256": "1d449ca76a8706ab0481b51b91c21d23d01cd2645124036dba205755ba638609",
    "complete_payload_bytes": 2682421,
    "complete_payload_sha256": "af48ff341b831df4ce24038b33aa2153161fa8f5da7a2d0387f29b042123c45b"}
IDENTITIES = {
    "physical": "bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c",
    "coordinate": "b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580",
    "configuration": "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19",
    "objective": "49c5f2e8a40c076b716c314bd9a3b41f4a0b8cd1ed40b51e0e83c87ce8266888",
    "field": "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1",
    "factorization": "b6cc198b6b58ec0484438c910a1e05a1273bc0cec81715415b8f538d31661963",
    "bank": "3d674785e4f46a8a5489ab49e6ff7de20d889eec92e4c7a6776ece452acf1611",
    "learning": "44eb8308c6ee5b2c1ab3b73951f6f111a5a5a7423636ea7a132b19b53003b00d",
    "old_supplemental": "42105a88c557e705c0f0b731d91ef42f2e5374ebab06da52dd870f254f508efd"}


def check_clock(scientific_started):
    require(finite_number(scientific_started) and scientific_started <= time.monotonic(),
            "one finite new pre-input scientific start required")
    elapsed = time.monotonic()-scientific_started
    if elapsed >= LIMITS["max_scientific_seconds"] or SOURCE_SCIENCE_SECONDS+elapsed >= 1800:
        raise EvaluationBudgetReached("new1200/original1800 scientific clock exhausted during source restoration")


def unique(records, tag, bytes_value=None, sha_value=None):
    require(len(records[tag]) == 1, "one paid original record required: "+tag)
    text, value = records[tag][0]
    raw = (text+"\n").encode("utf-8")
    if bytes_value is not None:
        require(len(raw) == bytes_value and reader.digest(raw) == sha_value,
                "paid JSON plus LF fingerprint differs: "+tag)
    return value, {"tag": tag, "JSON_plus_LF_bytes": len(raw),
                   "JSON_plus_LF_sha256": reader.digest(raw)}


def retained_supplements(cp):
    old = copy.deepcopy(cp["supplemental_paid_normals"])
    require(len(old) == 4 and digest(old) == IDENTITIES["old_supplemental"],
            "all four pre-terminal independent supports are required")
    record = cp["terminal_paid_slot_continuation"]["prepared_support_provenance"]
    require(isinstance(record, dict) and len(record["witnesses"]) == 4,
            "the actually recorded terminal four-witness provenance is required")
    appended = record["append"]
    kept, duplicates = appended["kept_new_indices"], appended["duplicate_new_indices"]
    require(all(type(x) is int for x in kept+duplicates)
            and sorted(kept+duplicates) == [0, 1, 2, 3]
            and len(set(kept)) == len(kept)
            and appended["original_rows_retained_in_order"] == 516
            and appended["distinct_new_rows"] == len(kept)
            and appended["combined_rows"] == 516+len(kept),
            "terminal support append identity differs")
    extra = []
    for index in kept:
        witness = record["witnesses"][index]
        exact = [Q(x) for x in witness["normal_exact_binary64"]]
        normal = [float(x) for x in exact]
        require(len(exact) == 3 and all(math.isfinite(v) for v in normal)
                and [Q.from_float(v) for v in normal] == exact
                and sum((x*x for x in exact), Q()) <= 1
                and str(sum((x*x for x in exact), Q())) == witness["normal_squared_norm_exact"]
                and witness["paid_attainer_index"] == index,
                "terminal unit-ball witness or exact binary64 normal changed")
        extra.append({
            "original_row": copy.deepcopy(witness["original_row"]), "normal": normal,
            "source": "actually appended terminal paid-affine support",
            "source_terminal_witness": copy.deepcopy(witness)})
    all_records = old+extra
    return all_records, {
        "schema": POLICY+"-retained-support-provenance",
        "bank_entries": 512, "pre_terminal_independent_supports": 4,
        "actual_appended_terminal_supports": len(extra),
        "terminal_prepared_support_provenance": copy.deepcopy(record),
        "all_supplemental_records_sha256": digest(all_records),
        "old_supplemental_sha256": IDENTITIES["old_supplemental"],
        "same_ID_normals_never_replace_retained_bank_rows": True,
        "unknown_old_proposed_step_not_reconstructed": True}


def read_completed(request, *, scientific_started):
    check_clock(scientific_started)
    require(request["source"] == PINS, "the latest terminal success is the only source")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+PINS["run_id"])
    job = api.api_json("/actions/jobs/"+PINS["job_id"])
    require(str(run["id"]) == PINS["run_id"] and str(job["id"]) == PINS["job_id"]
            and str(job["run_id"]) == PINS["run_id"]
            and run["head_sha"] == job["head_sha"] == PINS["source_commit"]
            and run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "success",
            "paid terminal run/job/source/link differs")
    raw, redirects = api.job_log(PINS["job_id"])
    require(len(raw) == PINS["log_bytes"] and reader.digest(raw) == PINS["log_sha256"],
            "paid latest raw log differs")
    tags = tuple("TERMINAL_SLOT_"+x for x in (
        "REQUEST", "DEVELOPMENT_REUSED", "PRIOR_WORK_REUSED", "MODEL", "COMPLETE"))
    records = inherited.tagged_records(raw, tags)
    requested, request_meta = unique(records, tags[0])
    dev, dev_meta = unique(records, tags[1])
    prior, prior_meta = unique(records, tags[2])
    model, model_meta = unique(records, tags[3], PINS["model_payload_bytes"], PINS["model_payload_sha256"])
    real, complete_meta = unique(records, tags[4], PINS["complete_payload_bytes"], PINS["complete_payload_sha256"])
    require(requested["source_commit"] == PINS["source_commit"], "paid request source differs")
    old_manifest = requested["source_sha256"]
    require(len(old_manifest) == 168
            and len([p for p in old_manifest if p.endswith(".py")]) == 158,
            "all paid168/158 source bindings required")
    for path, sha in old_manifest.items():
        require(request["source_sha256"].get(path) == sha
                and reader.digest(Path(path).read_bytes()) == sha,
                "a frozen terminal dependency changed: "+path)
    old_python = {Path(p).name: sha for p, sha in old_manifest.items() if p.endswith(".py")}
    require(real["source_files_sha256"] == old_python,
            "paid COMPLETE and REQUEST Python closures differ")
    require(dev["passed"] is True and dev["paid_source_group_count"] == 3
            and dev["paid_source_check_count"] == 11 and dev["all_paid_source_checks_passed"] is True
            and dev["current_development_groups_executed"] == 0
            and dev["current_development_checks_executed"] == 0
            and dev["current_stub_solver_calls"] == 0
            and dev["current_old_developer_or_science_replays"] == 0,
            "paid eleven-check reuse boundary differs")
    groups = dev["passed_source_groups"]
    require([len(g["checks"]) for g in groups] == [4, 3, 4]
            and all(g["passed"] is True and all(v is True for v in g["checks"].values()) for g in groups),
            "actual original eleven verdicts differ")
    require(prior["passed"] is True and prior["old_nine_check_groups"] == 3
            and prior["old_nine_checks"] == 9 and prior["old_development_executions"] == 0
            and prior["old_optimizer_LP_geometry_JVP_replays"] == 0
            and prior["whole_original_source_request_current_file_hashes_match"] is True,
            "the transitive paid nine-check/source receipt differs")
    require(real["schema"] == TERMINAL_POLICY+"-audit"
            and real["status"] == "complete-two-grid-terminal-paid-slot-audit"
            and real["github_sha"] == PINS["source_commit"]
            and str(real["github_run_id"]) == PINS["run_id"]
            and real["github_repository"] == REPO,
            "paid final audit provenance differs")
    stage, cp, cfg = real[SOURCE_STAGE], real["future_direct_checkpoint"], real["configuration"]
    require(stage["error"] is None and stage["model_count"] == 1
            and all(stage["solver"][k] == v for k, v in SOURCE_LEGACY_COUNTS.items())
            and stage["solver"]["nonlinear_minimize_invocation_count"] == 0
            and model["source_model_number"] == 28
            and model["result"] == "new-rows-return-to-last-accepted-before-SOC",
            "the final original LP64 outcome differs")
    require(cp["schema"] == DIRECT_POLICY+"-future-direct-checkpoint"
            and cp["configuration"] == cfg and digest(cfg) == IDENTITIES["configuration"]
            and cp["selected_physical_state_sha256"] == IDENTITIES["physical"]
            and cp["selected_accepted_index"] == 27
            and cp["new_task_started_LPs"] == 64 and cp["new_task_shared_values"] == SOURCE_VALUES
            and real["cumulative_same_task_scientific_seconds"] == SOURCE_SCIENCE_SECONDS,
            "paid current point, complete cfg, 64/62 or final scientific cost differs")
    for definition_key, sha_key, kind in (
            ("objective_evaluation_definition", "objective_evaluation_sha256", "objective"),
            ("ordinary_field_evaluation_definition", "ordinary_field_evaluation_sha256", "field"),
            ("factorization_definition", "factorization_definition_sha256", "factorization")):
        require(cp[sha_key] == IDENTITIES[kind] and digest(cp[definition_key]) == cp[sha_key],
                "paid complete identity changed: "+kind)
    require(cp["norm_direction_bank_state_sha256"] == IDENTITIES["bank"]
            and len(cp["norm_direction_bank_entries"]) == 512
            and digest(cp["coordinate_definition"]) == IDENTITIES["coordinate"],
            "complete source bank or coordinate identity differs")
    learning = cp["curvature_defect_guard_learning_checkpoint"]
    require(learning["state_sha256"] == IDENTITIES["learning"]
            and learning["pending_event_indices"] == []
            and len(learning["events"]) == 36 and len(learning["commits"]) == 35
            and learning["coefficients"] == {
                "coarse": 43.39425351670855, "fine": 44.0738041005123},
            "paid committed terminal learning state differs")
    require([len(cp["coarse_pool"]), len(cp["fine_pool"])] == [4439, 4533]
            and [cp["coarse_pool_version"], cp["fine_pool_version"]] == [8, 6]
            and cp["terminal_trust"] == .000125
            and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
            "paid source pools or controller differ")
    point = stage["selected_two_grid_physical_point"]
    require(point["accepted_index"] == 27
            and point["physical_state_sha256"] == IDENTITIES["physical"]
            and point["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and point["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"],
            "the exact accepted current point is not preserved")
    require(real["final_selection_validation"]["both_value_grids_hard_and_old_metric_pass"] is True
            and real["final_selection_validation"]["exact_original_box_pass"] is True
            and real["final_selection_validation"]["both_grid_maximum_eta"] == point["maximum_eta_on_both_grids"],
            "paid final gate/box/eta receipt differs")
    for key in ("final_full_grid_constraints", "final_doubled_constraints"):
        flags = real[key]["actual_gate_booleans"]
        require(len(flags) == 14 and all(v is True for v in flags.values()),
                "paid final fourteen actual gate flags required")
    counters = copy.deepcopy(stage["snapshot_scalar_counters"])
    require(counters["total_full_value_physical_evaluations"] == SOURCE_VALUES,
            "paid value count differs")
    supplements, manifest = retained_supplements(cp)
    receipt = {
        "schema": POLICY+"-paid-latest-source-receipt", "passed": True,
        "source": copy.deepcopy(PINS), "original_record_fingerprints": [
            request_meta, dev_meta, prior_meta, model_meta, complete_meta],
        "old_source_total_bindings": 168, "old_Python_sources": 158,
        "all_old_sources_match_current_bytes": True,
        "paid_eleven_checks": 11, "paid_nine_geometry_checks": 9,
        "old_development_executions": 0, "old_solver_trial_JVP_geometry_replays": 0,
        "one_latest_original_log_read": True,
        "earlier_failed_or_direct_original_logs_redownloaded": 0,
        "redirects_without_authorization": redirects,
        "source_legacy_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
        "source_actual_values": SOURCE_VALUES, "source_final_science_seconds": SOURCE_SCIENCE_SECONDS,
        "source_checkpoint_earlier_clock_not_used_as_final_total": True,
        "terminal_unknown_rejected_step_remains_unknown": True,
        "payload_repository_release_cache_uploads": 0}
    check_clock(scientific_started)
    return {"report": real, "checkpoint": cp, "terminal_model": model,
            "receipt": receipt, "current_point": point, "snapshot_counters": counters,
            "supplements": supplements, "support_manifest": manifest}


def prepare_transfer(request, output, process_started, *, completed, scientific_started):
    check_clock(scientific_started)
    real, cp = completed["report"], completed["checkpoint"]
    args = inherited.previous.old_input_namespace(request, output)
    prepared = baseline.growth.prepare_run(args, process_started=process_started)
    check_clock(scientific_started)
    restored, bindings, tenth, old_replay, coarse24, fine24 = prepared
    original, _, original_gate, lower, upper, historical_cfg, _ = restored
    coordinate_sha = digest(cp["coordinate_definition"])
    require(coordinate_sha == IDENTITIES["coordinate"], "source exact coordinate definition differs")
    field_request = {
        "source": {"coordinate_definition_sha256": coordinate_sha},
        "fixed_complete_metric_sha256": request["fixed_complete_metric_sha256"],
        "fixed_b0_definition_sha256": request["fixed_b0_definition_sha256"]}
    field, initial, gate, field_receipt = inherited.reconstruct_checkpoint_field(
        original, original_gate, lower, upper, cp, field_request)
    adapter, cfg = DirectReferenceFiveHeightField(field), copy.deepcopy(cp["configuration"])
    require(digest(adapter.identity(initial)) == IDENTITIES["physical"]
            and digest(adapter.evaluation_definition()) == IDENTITIES["field"]
            and digest(cfg) == IDENTITIES["configuration"],
            "same exact current159/physical163/reference/cfg/direct field required")
    radial, theta, grid = baseline.curvature_grid(tenth)
    original_grids = completed["terminal_model"]["complete_model"]["oracle"]["binding"]["grids"]
    for label, angular in (("coarse", len(theta)), ("fine", 2*len(theta))):
        current_grid = RationalRowGrid(label, grid["radial_nodes_exact"], angular)
        require(current_grid.definition == original_grids[label]["rational_grid_definition"]
                and current_grid.definition_sha256 == original_grids[label]["rational_grid_definition_sha256"],
                "paid original rational grid differs: "+label)
    counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    coarse = inherited.checked_pool(cp["coarse_pool"], counts["coarse"], cfg["max_pool_rows"], "coarse")
    fine = inherited.checked_pool(cp["fine_pool"], counts["fine"], cfg["max_fine_physical_pool_rows"], "fine")
    require(cp["norm_direction_bank_context"]["original_point_counts"] == counts,
            "source bank does not use these same complete original grids")
    controller = {
        "schema": POLICY+"-actual-source-controller",
        "trust_binary64_exact": str(Q.from_float(cp["terminal_trust"])),
        "trust_evaluated": cp["terminal_trust"],
        "success_streak": cp["terminal_success_streak"],
        "covered_ordinary_success_streak": cp["terminal_covered_ordinary_growth_streak"],
        "radius_or_streak_reset": False}
    ancestor = {
        "source": copy.deepcopy(PINS), "final_source_scientific_seconds": SOURCE_SCIENCE_SECONDS,
        "final_source_actual_values": SOURCE_VALUES, "closed_source_legacy_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
        "source_process_seconds": real["process_total_elapsed_seconds"],
        "source_peak_rss_kib_linux": real["peak_rss_kib_linux"],
        "source_snapshot_scalar_counters": copy.deepcopy(completed["snapshot_counters"]),
        "earlier_closed_epoch_costs": copy.deepcopy(cp["ancestor_costs"]),
        "all_source_attempt_science_already_in_final356_seconds_not_added_twice": True}
    replay = {
        "policy": POLICY, "identities": copy.deepcopy(IDENTITIES),
        "source_checkpoint": cp, "source_current_point": copy.deepcopy(completed["current_point"]),
        "paid_evidence": copy.deepcopy(completed["receipt"]),
        "source_snapshot_scalar_counters": copy.deepcopy(completed["snapshot_counters"]),
        "ancestor_cost_receipt": ancestor,
        "pool_versions": [8, 6], "controller_continuation": controller,
        "all_retained_supplemental_normals": copy.deepcopy(completed["supplements"]),
        "retained_support_manifest": copy.deepcopy(completed["support_manifest"]),
        "paid_initial_decisions": {
            "coarse": copy.deepcopy(completed["current_point"]["coarse"]),
            "fine": copy.deepcopy(completed["current_point"]["fine"])},
        "source_final_gate_receipts": {
            "coarse": copy.deepcopy(real["final_full_grid_constraints"]),
            "fine": copy.deepcopy(real["final_doubled_constraints"])},
        "source_final_selection_validation": copy.deepcopy(real["final_selection_validation"]),
        "source_completed_log_transfer": {
            "source": copy.deepcopy(PINS), "field_transfer": field_receipt,
            "necessary24_original_reports_loaded_once": True,
            "no_old_developer_optimizer_geometry_or_solver_execution": True,
            "no_pool_initialize_or_automatic_expand": True,
            "current_physical_value_caches_not_yet_computed": True},
        "historical24_configuration_sha256": digest(historical_cfg)}
    check_clock(scientific_started)
    return ((adapter, initial, gate, gate.coordinate_lower, gate.coordinate_upper, cfg),
            bindings, tenth, replay, coarse, fine)

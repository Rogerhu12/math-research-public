#!/usr/bin/env python3
"""Read one paid guard log and the24 necessary inputs for a NEW direct task.

The old source reader only validates already-published evidence. No old suite,
optimizer, LP, direction or whole-value call is replayed. Every new necessary
input/prepare second belongs to the caller's new1800s scientific clock.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
from pathlib import Path
import time

from frame_height_null_coordinates import digest
from frame_height_affine_gate import EvaluationBudgetReached
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_metric_direct_reference_epoch import (
    POLICY, configuration, SOURCE_PHYSICAL_SHA, SOURCE_BANK_SHA, RESOURCE_LIMITS)
import frame_metric_paid_attainer_transfer as paid
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader

REPO, ROOT = paid.REPO, paid.ROOT
require, json_bytes = paid.require, paid.json_bytes
SOURCE_RUN, SOURCE_JOB, SOURCE_COMMIT = paid.SOURCE_RUN, paid.SOURCE_JOB, paid.SOURCE_COMMIT
SOURCE_STAGE = paid.SOURCE_STAGE


def check_clock(scientific_started):
    require(type(scientific_started) in (int, float)
            and math.isfinite(scientific_started) and 0 < scientific_started <= time.monotonic(),
            "one pre-input scientific start required")
    if time.monotonic()-scientific_started >= RESOURCE_LIMITS["max_seconds"]:
        raise EvaluationBudgetReached("new1800s scientific task exhausted during necessary input/prepare")


def read_completed(request, *, scientific_started):
    check_clock(scientific_started)
    completed = paid.read_completed(request)
    check_clock(scientific_started)
    return completed


def ancestor_costs(request, source_counters):
    """Small source-pinned human receipt; never import its exhausted clock."""
    record = copy.deepcopy(request["ancestor_costs"])
    closed = record["closed_paid_attainer_epoch"]
    require(str(closed["run_id"]) == "43773136836"
            and str(closed["job_id"]) == "132993290386"
            and closed["source_commit"] == "403a2fcf430f0ed98b5731256befe36bb833eadf"
            and closed["status"] == "shared-value-time-or-pool-budget-exit",
            "closed cold-restoration source differs")
    expected = {
        "cumulative_active_seconds": 241.3142038439999,
        "cumulative_initialization_seconds": 293.5427817930001,
        "cumulative_shared_values": 15, "cumulative_LPs": 10,
        "new_coarse_values": 1, "new_fine_values": 0,
        "new_LPs": 0, "new_J_batches": 0,
        "cold_coarse_value_seconds": 205.448292651,
        "process_seconds": 224.820478542,
        "prepare_seconds": 14.011384722,
        "recovery_seconds": 205.785849204}
    require(all(closed.get(k) == value for k, value in expected.items()),
            "the authenticated closed-epoch scalar cost pins differ")
    evidence = record["published_human_note"]
    path = Path(evidence["path"])
    raw = path.read_bytes()
    require(len(raw) == evidence["bytes"] and reader.digest(raw) == evidence["sha256"],
            "ancestor human-result note bytes differ")
    record["source_guard_snapshot_counters"] = copy.deepcopy(source_counters)
    record["source_guard_independent_final_values_outside_shared_ledger"] = 2
    record["ancestor_costs_not_added_to_new_resource_counters"] = True
    record["closed_m7_not_reopened"] = True
    record["no_additional_old_log_download_for_human_cost_receipt"] = True
    return record


def prepare_transfer(request, output, process_started, *, completed, scientific_started):
    """Construct immutable input objects once; do not evaluate their full geometry."""
    check_clock(scientific_started)
    real, models, cp, event, evidence = completed
    require(cp["selected_physical_state_sha256"] == SOURCE_PHYSICAL_SHA
            and cp["norm_direction_bank_state_sha256"] == SOURCE_BANK_SHA,
            "the current best438 checkpoint is required")
    source_counters = real[SOURCE_STAGE]["snapshot_scalar_counters"]
    costs = ancestor_costs(request, source_counters)
    args = inherited.previous.old_input_namespace(request, output)
    prepared = baseline.growth.prepare_run(args, process_started=process_started)
    check_clock(scientific_started)
    restored, bindings, tenth, old_replay, coarse24, fine24 = prepared
    original, _, original_gate, lower, upper, historical_input_cfg, _ = restored
    field, initial, gate, field_transfer = inherited.reconstruct_checkpoint_field(
        original, original_gate, lower, upper, cp, request)
    require(digest(field.identity(initial)) == SOURCE_PHYSICAL_SHA,
            "exact current159/reference163 recovery changed physical identity")
    source_cfg = copy.deepcopy(real["configuration"])
    cfg = configuration(source_cfg)
    adapter = DirectReferenceFiveHeightField(field)
    radial, theta, grid = baseline.curvature_grid(tenth)
    require(grid == real["full_value_sampling_definition"],
            "the original complete full-value grid changed")
    point_counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    coarse = inherited.checked_pool(cp["coarse_pool"], point_counts["coarse"],
                                     cfg["max_pool_rows"], "coarse")
    fine = inherited.checked_pool(cp["fine_pool"], point_counts["fine"],
                                   cfg["max_fine_physical_pool_rows"], "fine")
    require(cp["norm_direction_bank_context"]["original_point_counts"] == point_counts
            and [len(coarse), len(fine)] == [4432, 4525],
            "current pools/bank do not use the original two grids")
    stage = real[SOURCE_STAGE]
    require(cp["terminal_trust"] == .00025
            and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0
            and [models[-1]["coarse_pool_version"], models[-1]["fine_pool_version"]] == [1, 2],
            "original current-best controller or pool versions differ")
    selected = stage["selected_two_grid_physical_point"]
    require(selected["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
            "paid initial scalar receipts belong to another state")
    controller = {
        "schema": POLICY+"-source-controller",
        "origin": "new independent task starting at paid guard best; closed m7 is not resumed",
        "trust_binary64_exact": str(Q.from_float(cp["terminal_trust"])),
        "trust_evaluated": cp["terminal_trust"],
        "success_streak": cp["terminal_success_streak"],
        "covered_ordinary_success_streak": cp["terminal_covered_ordinary_growth_streak"],
        "source_last_accepted_model": 6, "source_closed_unevaluated_model": 7,
        "radius_or_success_streak_reset": False}
    replay = {
        "policy": POLICY,
        "original_report": real,
        "source_checkpoint": cp,
        "paid_evidence": copy.deepcopy(evidence),
        "canonical_physical_state_sha256": SOURCE_PHYSICAL_SHA,
        "layout_derived_from_actual_problem": baseline.layout_from_problem(original),
        "source_completed_log_transfer": {
            "source_run_id": SOURCE_RUN, "source_job_id": SOURCE_JOB, "source_commit": SOURCE_COMMIT,
            "field_transfer": copy.deepcopy(field_transfer),
            "original_guard18_and_transitive20_19_26_cache_receipts_checked": True,
            "old_developer_LP_optimizer_direction_replays": 0,
            "source24_input_reports_loaded_once": True,
            "adapter_and_original_field_share_the_same_live_immutable_objects": True,
            "new_initial_full_value_evaluations_not_yet_started": True},
        "controller_continuation": controller, "pool_versions": [1, 2],
        "initial_bank_context": copy.deepcopy(cp["norm_direction_bank_context"]),
        "initial_bank_entries": copy.deepcopy(cp["norm_direction_bank_entries"]),
        "expected_initial_bank_state_sha256": cp["norm_direction_bank_state_sha256"],
        "expected_initial_bank_entries": 438,
        "curvature_learning_checkpoint": copy.deepcopy(cp["curvature_defect_guard_learning_checkpoint"]),
        "inherited_bank_report": copy.deepcopy(stage["cross_center_norm_memory"]),
        "paid_attainers": copy.deepcopy(event["attainers"]),
        "paid_initial_decisions": {
            "coarse": copy.deepcopy(selected["coarse"]), "fine": copy.deepcopy(selected["fine"])},
        "paid_initial_full_actual_gate_receipts": {
            "coarse": copy.deepcopy(real["final_full_grid_constraints"]),
            "fine": copy.deepcopy(real["final_doubled_constraints"])},
        "ancestor_costs": costs,
        "source_configuration": source_cfg,
        "historical24_input_configuration_sha256": digest(historical_input_cfg),
        "source_final_selection_validation": copy.deepcopy(real["final_selection_validation"]),
        "source_reference_exact": copy.deepcopy(cp["reference_complete163_binary64_exact"]),
        "no_source_pool_initialization_or_old_sample_retraining": True}
    check_clock(scientific_started)
    return ((adapter, initial, gate, gate.coordinate_lower, gate.coordinate_upper,
             source_cfg, cfg), bindings, tenth, replay, coarse, fine)

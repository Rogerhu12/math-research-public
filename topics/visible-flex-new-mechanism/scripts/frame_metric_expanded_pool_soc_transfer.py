#!/usr/bin/env python3
"""Read a completed exact physical checkpoint and its original norm-memory bank.

All execution belongs to the public repository Actions. The final159, full163
reference, physical163, complete two row pools, and terminal controller come
from run43741276060. The nine bank entries are reconstructed from the original
nineteen seeds and the two actually added supports, then checked against the
completed bank hash on first binding. No optimizer or old developer suite runs.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import numpy as np
from frame_height_null_coordinates import digest
from frame_five_height_field import FiveHeightField
from frame_height_null_gate import FiveNullHeightGate
import frame_metric_height159_complete_affine_audit as baseline
import frame_metric_norm_memory_transfer as previous
import read_original_actions_log as reader

REPO = previous.REPO
ROOT = previous.ROOT
POLICY = "same159-expanded-pool-rebound-SOC-v1"
SOURCE_SCHEMA = "same159-direct-physical-transfer-norm-direction-memory-v1"
SOURCE_STAGE = "norm_direction_memory_stage"
require = previous.require
json_bytes = previous.json_bytes
file_sha = previous.file_sha
exact_binary_vector = previous.exact_binary_vector


def parse_records(raw):
    """Preserve original JSON bytes for the payload binding; BOM is prefix only."""
    found = {"NORM_MEMORY_MODEL": [], "NORM_MEMORY_COMPLETE": []}
    for line in raw.decode("utf-8").splitlines():
        clean = line.lstrip("\ufeff")
        for tag in found:
            marker = tag+" "
            pos = clean.find(marker)
            if pos < 0:
                continue
            payload = clean[pos+len(marker):]
            require(payload.startswith("{"), "completed record is not an object")
            found[tag].append((payload, json.loads(payload)))
    require(len(found["NORM_MEMORY_COMPLETE"]) == 1, "unique original COMPLETE record required")
    models = [item[1] for item in found["NORM_MEMORY_MODEL"]]
    require([m["number"] for m in models] == list(range(1, 12)),
            "all eleven completed primary models required")
    payload, real = found["NORM_MEMORY_COMPLETE"][0]
    return real, models, (payload+"\n").encode("utf-8")


def read_completed(request):
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == REPO, "public Actions required")
    source = request["source"]
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+str(source["run_id"]))
    job = api.api_json("/actions/jobs/"+str(source["job_id"]))
    require(run["head_sha"] == job["head_sha"] == source["source_commit"],
            "completed source/run/job differs")
    require(run["status"] == job["status"] == "completed" and
            run["conclusion"] == job["conclusion"] == "success",
            "completed successful source required")
    require(int(job["run_id"]) == int(run["id"]), "source run/job binding differs")
    raw, redirects = api.job_log(str(source["job_id"]))
    require(len(raw) == source["log_bytes"] and reader.digest(raw) == source["log_sha256"],
            "original completed log bytes differ")
    real, models, payload = parse_records(raw)
    require(len(payload) == source["complete_payload_bytes"] and
            reader.digest(payload) == source["complete_payload_sha256"],
            "original COMPLETE JSON plus LF differs")
    require(real["schema"] == SOURCE_SCHEMA and
            real["status"] == "complete-two-grid-norm-direction-memory-transfer-audit",
            "source schema/status differs")
    require(real["github_sha"] == source["source_commit"] and
            str(real["github_run_id"]) == str(source["run_id"]) and
            real["github_repository"] == REPO, "source report provenance differs")
    scripts = Path(__file__).parent
    require(len(real["source_files_sha256"]) == 112, "completed dependency count differs")
    for name, expected in real["source_files_sha256"].items():
        require(file_sha(scripts/name) == expected, "frozen source changed: "+name)
    cp = real["future_direct_checkpoint"]
    for key, expected in source["checkpoint_list_sha256"].items():
        require(reader.digest(json_bytes(cp[key])) == expected, "exact checkpoint list differs: "+key)
    require(cp["selected_physical_state_sha256"] == source["final_physical_sha256"],
            "checkpoint physical identity differs")
    accepted = [(m["number"], j, t) for m in models for j, t in enumerate(m.get("trials", []))
                if t.get("accepted_as_next_iterate") is True]
    require(len(accepted) == 8, "eight source accepts required")
    number, trial, final = max(accepted, key=lambda item: item[2]["accepted_index"])
    require(number == 11 and final["accepted_index"] == 8 and
            final["physical_state_sha256"] == cp["selected_physical_state_sha256"],
            "native final trial and checkpoint differ")
    require(final["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"] and
            final["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"],
            "native exact lists and checkpoint differ")
    require(real["final_selection_validation"]["both_value_grids_hard_and_old_metric_pass"],
            "source final original gates not passed")
    metadata = {
        "original_run_id": source["run_id"], "original_job_id": source["job_id"],
        "original_source_commit": source["source_commit"],
        "original_log_bytes": len(raw), "original_log_sha256": reader.digest(raw),
        "original_complete_payload_bytes": len(payload),
        "original_complete_payload_sha256": reader.digest(payload),
        "all112_frozen_sources_match_current_files": True,
        "final_native_model": number, "final_native_trial": trial,
        "original_exact159_reference163_and_physical163_read_without_rounding": True,
        "full_completed_coarse_and_fine_row_lists_present": True,
        "new_old_optimizer_calls": 0, "new_old_developer_calls": 0,
        "redirects_without_authorization": redirects,
        "payloads_only_in_runner_memory_and_semantic_stdout": True}
    return real, models, cp, metadata


def reconstruct_checkpoint_field(original, original_gate, lower, upper, cp, request):
    q = exact_binary_vector(cp["selected_final159_binary64_exact"], 159)
    reference = exact_binary_vector(cp["reference_complete163_binary64_exact"], 163)
    physical = tuple(Q(x) for x in cp["selected_final163_physical_exact"])
    require(len(physical) == 163, "physical checkpoint dimension differs")
    field = FiveHeightField(original, reference)
    require(field.coordinates.physical_exact(q) == physical, "checkpoint affine map changed physical163")
    require(digest(field.identity(q)) == cp["selected_physical_state_sha256"],
            "checkpoint canonical physical identity differs")
    require(field.coordinate_definition == cp["coordinate_definition"] and
            field.coordinate_definition_sha256 == request["source"]["coordinate_definition_sha256"],
            "complete reference/height map/coordinate metadata changed")
    metric = field.metric_model(q)
    require(digest(metric["mathematical_definition"]) ==
            metric["mathematical_definition_sha256"] == request["fixed_complete_metric_sha256"],
            "permanent mathematical metric changed")
    require(digest(field.height_base_definition) == request["fixed_b0_definition_sha256"],
            "permanent b0 changed")
    gate = FiveNullHeightGate(original_gate, field, lower, upper)
    require(field.coordinates.exact_box_decision(q, lower, upper)["exact_original_box_pass"],
            "transferred exact original physical box fails")
    metadata = {
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "full_runtime_reference_preserved_including_tangent_entries": True,
        "reference_physical_tag": field.coordinate_definition["reference_physical_sha256"],
        "same_exact_reference163_height_H_physical163_and_independent159": True,
        "same_original_metric_and_b0": True,
        "no_coordinate_metadata_change_this_transfer": True,
        "no_physical_rounding_projection_or_clipping": True}
    return field, q, gate, metadata


def checked_pool(values, point_count, capacity, name):
    require(isinstance(values, list) and all(type(x) is int for x in values),
            name+" pool must retain integer original row IDs")
    require(values == sorted(set(values)) and
            all(0 <= x < 11*point_count for x in values) and len(values) <= capacity,
            name+" complete source pool is malformed or exceeds the original capacity")
    return list(values)


def reconstruct_source_direction_records(request, models, coarse24, fine24, counts, cfg):
    """Replay only the completed direction inputs, without evaluating geometry."""
    path = Path(request["ancestor_transfer_request_path"])
    raw = path.read_bytes()
    require(reader.digest(raw) == request["ancestor_transfer_request_sha256"],
            "ancestor transfer request changed")
    ancestor_request = json.loads(raw)
    old, old_models, _, old_source = previous.read_completed(ancestor_request)
    _, _, records, old_pool_meta = previous.current_pool_seed(
        old, old_models, coarse24, fine24, counts["coarse"], counts["fine"], cfg)
    require(len(records) == 19, "original nineteen direction records differ")
    source_cut_count = 0
    for model in models:
        lp = model["linear_program"]
        for round_record in lp.get("cut_rounds", []):
            if "direction_memory_after_this_cut_sha256" not in round_record:
                continue
            for row in round_record["per_row"]:
                value = row.get("directional_oracle_attainer")
                require(isinstance(value, dict), "completed support lacks its original e/f attainer")
                records.append({
                    "original_row": copy.deepcopy(value["original_row"]),
                    "affine_e": value["affine_e"], "affine_f": value["affine_f"],
                    "source_center_binding_sha256": lp["model"]["binding_sha256"]})
                source_cut_count += 1
    require(source_cut_count == 2 and len(records) == 21, "completed added support count differs")
    expected = request["source"]["terminal_norm_bank_state_sha256"]
    require(models[-1]["linear_program"]["complete_original_grid_model"]["norm_direction_memory"]
            ["state_sha256"] == expected, "native terminal bank hash differs")
    return records, {
        "policy": "original nineteen observed seeds plus exactly two source cut-round supports in original order",
        "ancestor_run_id": old_source["original_run_id"],
        "ancestor_log_sha256": old_source["original_log_sha256"],
        "ancestor_seed_records": 19, "new_source_support_records": 2,
        "replayed_direction_input_records": 21,
        "expected_distinct_bank_entries": 9,
        "expected_terminal_bank_state_sha256": expected,
        "hash_must_match_after_first_original_model_binding": True,
        "old_numeric_A_b_carried": False,
        "no_geometry_or_optimizer_executed_by_direction_input_replay": True}


def prepare_transfer(request, output, process_started):
    real, models, cp, source = read_completed(request)
    args = previous.old_input_namespace(request, output)
    prepared = baseline.growth.prepare_run(args, process_started=process_started)
    restored, bindings, tenth, old_replay, coarse24, fine24 = prepared
    original, _, original_gate, lower, upper, source_cfg, _ = restored
    field, initial, gate, transfer = reconstruct_checkpoint_field(
        original, original_gate, lower, upper, cp, request)
    cfg = copy.deepcopy(real["configuration"])
    require(digest(cfg) == request["source"]["configuration_sha256"],
            "completed original configuration hash differs")
    require((cfg["max_linear_models"], cfg["max_physical_evaluations"],
             cfg["max_seconds"], cfg["linear_program_seconds"]) == (12, 40, 120, 10),
            "original shared limits changed")
    # Preserve the complete original configuration: it is part of the exact
    # factorization and norm-bank context hash. New algorithm metadata lives
    # in the explicit objective class/request, never in this frozen cfg.
    radial, theta, grid = baseline.curvature_grid(tenth)
    counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    coarse = checked_pool(cp["coarse_pool"], counts["coarse"], cfg["max_pool_rows"], "coarse")
    fine = checked_pool(cp["fine_pool"], counts["fine"], cfg["max_fine_physical_pool_rows"], "fine")
    require(len(coarse) == 4418 and len(fine) == 4092, "source final complete pool sizes differ")
    normals, memory = reconstruct_source_direction_records(
        request, models, coarse24, fine24, counts, cfg)
    trust, streak = cp["terminal_trust"], cp["terminal_success_streak"]
    require(trust == .0000625 and streak == 1 and type(streak) is int,
            "completed terminal radius/streak differs")
    stage = real[SOURCE_STAGE]
    require(trust == stage["last_restricted_trust"] and
            streak == stage["final_consecutive_growth_qualifying_models"],
            "checkpoint controller and native final state differ")
    controller = {
        "schema": "complete-checkpoint-terminal-controller-v1",
        "origin": "immutable norm-memory run43741276060 final model11 and exact checkpoint",
        "trust_binary64_exact": str(Q.from_float(float(trust))),
        "trust_evaluated": trust, "success_streak": streak,
        "source_last_completed_model": 11, "radius_or_success_streak_reset": False}
    pools = {
        "policy": "both complete terminal source row lists, followed by unchanged current-state learning",
        "full_original_checkpoint_pools_retained": True,
        "seed_counts": {"coarse": len(coarse), "fine": len(fine)},
        "coarse_seed_sha256": digest(coarse), "fine_seed_sha256": digest(fine),
        "no_invented_absent_history_or_new_pool_union": True,
        "capacity_and_actual_gates_unchanged": True}
    source.update(field_transfer=transfer, completed_pool_transfer=pools,
                  direction_input_replay=memory, original_controller=controller)
    replay = {
        "source_completed_log_transfer": source,
        "canonical_physical_state_sha256": digest(field.identity(initial)),
        "layout_derived_from_actual_problem": baseline.layout_from_problem(original),
        "learned_pool": pools,
        "explicit_new_constraint_definition": {
            "physical_gates_and_thresholds_unchanged": True,
            "new_proposal_algorithm": POLICY,
            "full_source_row_pool_and_original_memory_preserved": True,
            "complete_source_configuration_preserved_for_original_bank_binding": True,
            "same_failed_trial_rebinds_expanded_original_row_layout_before_SOC": True},
        "known_fine_metric_locations": [], "controller_continuation": controller,
        "initial_direction_records": normals, "original_report": real,
        "expected_initial_bank_state_sha256": memory["expected_terminal_bank_state_sha256"],
        "expected_initial_bank_entries": 9,
        "source_final_gate_and_value_report_consumed_without_new_optimizer": True}
    return ((field, initial, gate, gate.coordinate_lower, gate.coordinate_upper,
             source_cfg, cfg), bindings, tenth, replay, coarse, fine)

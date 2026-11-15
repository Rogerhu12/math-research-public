#!/usr/bin/env python3
"""Direct exact-state transfer from an immutable completed public Actions log.

No old optimization is rerun. The original nine height reference values and H
are recovered exactly. Their old full-reference tag is checked, but the new
runtime reference uses current tangent values; its metadata hash is reported
as new. Original physical identity and field do not change. Later historical
row lists absent from the log are not invented: all24-input rows and observed
original row tags seed a declared new pool initialization.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
import time
import numpy as np
from frame_height_null_coordinates import ExactFiveHeightBasis, digest
from frame_five_height_field import FiveHeightField
from frame_height_null_gate import FiveNullHeightGate
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader

REPO = "Rogerhu12/math-research-public"
ROOT = "topics/visible-flex-new-mechanism"
OLD_SCHEMA = "same159-complete-grid-affine-ef-after-nine-restorations-v1"
OLD_STAGE = "metric_height159_complete_affine_stage"


def require(value, text):
    if not value:
        raise ValueError(text)


def json_bytes(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_binary_vector(strings, size):
    require(isinstance(strings, list) and len(strings) == size, "exact vector dimension differs")
    rational = [Q(s) for s in strings]
    values = np.array([float(x) for x in rational], float)
    require(np.all(np.isfinite(values)), "nonfinite exact input")
    require(all(Q.from_float(float(y)) == x for x, y in zip(rational, values)),
            "input independent/reference vector is not exact binary64")
    return values


def old_input_namespace(request, output):
    parser = argparse.ArgumentParser(add_help=False)
    for name in baseline.INPUTS:
        parser.add_argument("--"+name.replace("_", "-"), type=Path)
    for name in baseline.SHA_NAMES:
        parser.add_argument("--expected-"+name+"-sha256")
    parser.add_argument("--out", type=Path, required=True)
    args = list(request["original_input_arguments"])
    position = args.index("--out")
    args[position+1] = str(output)
    require("@OUT@" not in " ".join(args), "unexpanded output path")
    return parser.parse_args(args)


def walk_dicts(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from walk_dicts(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_dicts(item)


def read_completed(request):
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == REPO, "public repository Actions required")
    original = request["original"]
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+str(original["run_id"]))
    job = api.api_json("/actions/jobs/"+str(original["job_id"]))
    require(run["head_sha"] == job["head_sha"] == original["source_commit"], "old source/run/job differs")
    require(run["conclusion"] == job["conclusion"] == "success" and
            run["status"] == job["status"] == "completed", "completed successful original job required")
    require(int(job["run_id"]) == int(run["id"]), "old run/job binding differs")
    raw, redirects = api.job_log(str(original["job_id"]))
    require(len(raw) == original["log_bytes"] and
            reader.digest(raw) == original["log_sha256"], "immutable original log differs")
    dev, actual, _, models, _, _, _ = reader.parse_log(raw, job)
    real = actual["report"]
    require(real["schema"] == OLD_SCHEMA and real["status"] ==
            "complete-two-grid-height159-complete-affine-audit", "old actual schema/status differs")
    require(real["github_sha"] == original["source_commit"] and
            str(real["github_run_id"]) == str(original["run_id"]), "old actual provenance differs")
    require(actual["payload_sha256"] == original["actual_payload_sha256"], "old report substring differs")
    require(dev["report"].get("passed") is True, "old development receipt does not say passed")
    receipt_path = Path(original["receipt_path"])
    receipt_raw = receipt_path.read_bytes()
    require(len(receipt_raw) == original["receipt_bytes"] and
            reader.digest(receipt_raw) == original["receipt_sha256"], "old receipt differs")
    receipt = json.loads(receipt_raw)
    require(str(receipt["run_id"]) == str(original["run_id"]) and
            receipt["source_commit"] == original["source_commit"], "old receipt identity differs")
    reader.source_bindings(real, receipt)
    scripts = Path(__file__).parent
    for name, expected in real["source_files_sha256"].items():
        require(file_sha(scripts/name) == expected, "frozen physical/numerical source changed: "+name)
    require([x["model"]["number"] for x in models] == list(range(1, 7)), "all six original models required")
    accepted = [(x["model"]["number"], j, trial) for x in models
                for j, trial in enumerate(x["model"].get("trials", []))
                if trial.get("accepted_as_next_iterate") is True]
    require(bool(accepted), "old native accepted coordinates absent")
    model_number, trial_number, final = max(accepted, key=lambda x: x[2]["accepted_index"])
    require((model_number, trial_number, final["accepted_index"]) == (5, 1, 5),
            "unexpected selected exact native final trial")
    require(final["physical_state_sha256"] == original["final_physical_sha256"],
            "old selected physical identity differs")
    require(reader.digest(json_bytes(final["exact_binary64_independent_coordinates"])) ==
            original["final_independent_list_sha256"], "old exact159 list differs")
    require(reader.digest(json_bytes(final["exact_original_physical_coefficients"])) ==
            original["final_physical_list_sha256"], "old exact163 list differs")
    metadata = {
        "original_run_id": original["run_id"], "original_job_id": original["job_id"],
        "original_source_commit": original["source_commit"],
        "original_log_bytes": len(raw), "original_log_sha256": reader.digest(raw),
        "original_actual_payload_sha256": actual["payload_sha256"],
        "original106_sources_match_receipt_and_current_files": True,
        "final_native_model": model_number, "final_native_trial": trial_number,
        "original_exact159_and163_arrays_read_not_rounded": True,
        "original_payloads_kept_only_in_runner_memory": True,
        "new_old_optimizer_calls": 0, "new_old_developer_calls": 0,
        "redirects_without_authorization": redirects}
    return real, models, final, metadata



def recover_reference_heights(exact159, exact163, height_map):
    q = exact_binary_vector(exact159, 159)
    physical = tuple(Q(x) for x in exact163)
    require(len(physical) == 163 and all(physical[i] == Q.from_float(float(q[i]))
            for i in range(154)), "old physical/tangent coefficients disagree")
    require(len(height_map) == 9 and all(len(row) == 5 for row in height_map), "exact H shape differs")
    tau = [Q.from_float(float(x)) for x in q[154:]]
    reference = tuple(physical[154+j]-sum((Q(height_map[j][k])*tau[k]
                      for k in range(5)), Q()) for j in range(9))
    href = exact_binary_vector([str(x) for x in reference], 9)
    return q, physical, reference, href


def reconstruct_same_field(original, initial24, original_gate, lower, upper,
                           exact159, exact163, request):
    """Exact reconstruction, not a legacy-object identity claim."""
    basis = ExactFiveHeightBasis(original.height_basis.identity)
    q, physical, reference, href = recover_reference_heights(exact159, exact163, basis.H)
    # Current tangent reference is explicit. Only its metadata tag changes.
    complete_reference = np.r_[q[:154], href]
    field = FiveHeightField(original, complete_reference)
    require(field.coordinates.physical_exact(q) == physical, "new affine map changes exact physical point")
    require(digest(field.identity(q)) == request["original"]["final_physical_sha256"],
            "reconstructed canonical physical identity differs")
    metric = field.metric_model(q)
    require(digest(metric["mathematical_definition"]) ==
            metric["mathematical_definition_sha256"] == request["fixed_complete_metric_sha256"],
            "permanent mathematical target metric definition changed")
    require(digest(field.height_base_definition) == request["fixed_b0_definition_sha256"],
            "permanent b0 definition changed")
    definition = copy.deepcopy(field.coordinate_definition)
    new_reference_tag = definition["reference_physical_sha256"]
    definition["reference_physical_sha256"] = request["original_height_reference_physical_sha256"]
    require(digest(definition) == request["original_coordinate_definition_sha256"],
            "recovered exact nine heights/H/layout differ from the original coordinate definition")
    gate = FiveNullHeightGate(original_gate, field, lower, upper)
    require(field.coordinates.exact_box_decision(q, lower, upper)["exact_original_box_pass"],
            "original exact physical box failed at transferred state")
    metadata = {
        "old_coordinate_definition_sha256": request["original_coordinate_definition_sha256"],
        "new_coordinate_definition_sha256": field.coordinate_definition_sha256,
        "original_full_reference_physical_tag": request["original_height_reference_physical_sha256"],
        "new_runtime_reference_physical_tag": new_reference_tag,
        "only_coordinate_metadata_change": "full reference tangent values replaced by current transferred tangent values",
        "same_exact_nine_height_reference": True, "same_exact_five_height_map_H": True,
        "same_exact163_physical_final_state": True,
        "same_original_metric_and_b0": True,
        "all_other_coordinate_definition_fields_match_old_hash": True,
        "old_full_reference_tangent_vector_not_claimed_recovered": True,
        "old_runtime_object_identity_not_claimed": True,
        "reference_height_sha256": digest([str(x) for x in reference])}
    return field, q, gate, metadata


def current_pool_seed(real, models, initial_coarse, initial_fine, coarse_count, fine_count, cfg):
    pools = {"coarse": set(map(int, initial_coarse)), "fine": set(map(int, initial_fine))}
    counts = {"coarse": int(coarse_count), "fine": int(fine_count)}
    initial = {key: len(value) for key, value in pools.items()}
    source_ids = {"coarse": set(), "fine": set()}
    normals = []
    for record in models:
        model = record["model"]
        binding = model["linear_program"].get("model", {}).get("binding_sha256")
        require(isinstance(binding, str) and len(binding) == 64, "old model norm binding missing")
        for item in walk_dicts(model):
            if "grid" in item and "flat_row_id" in item and item["grid"] in counts:
                label = item["grid"]
                flat = item["flat_row_id"]
                require(type(flat) is int and 0 <= flat < 11*counts[label], "old original row ID malformed")
                source_ids[label].add(flat)
            value = item.get("directional_oracle_attainer")
            if isinstance(value, dict):
                tag = value["original_row"]
                require(tag["grid"] in counts and int(tag["flat_row_id"])//counts[tag["grid"]] ==
                        int(tag["group"]) in (0, 1), "old norm attainer row/branch differs")
                e, f = float(value["affine_e"]), float(value["affine_f"])
                require(math.isfinite(e) and math.isfinite(f), "nonfinite old norm attainer")
                normals.append({"original_row": copy.deepcopy(tag), "affine_e": e, "affine_f": f,
                                "source_center_binding_sha256": binding})
    for key in pools:
        pools[key].update(source_ids[key])
    coarse, fine = sorted(pools["coarse"]), sorted(pools["fine"])
    require(len(coarse) <= cfg["max_pool_rows"] and len(fine) <= cfg["max_fine_physical_pool_rows"],
            "declared new seed union exceeds unchanged original pool capacity")
    metadata = {
        "policy": "all24-input learned IDs plus every original row tag retained in source six models, then unchanged current-state initialization",
        "all24_input_coarse_and_fine_rows_retained": True,
        "later_complete_historical_row_lists_present_in_source_log": False,
        "not_claimed_to_restore_all_later_historical_pools": True,
        "seed_counts": {"coarse": len(coarse), "fine": len(fine)},
        "original24_counts": initial,
        "source_observed_row_counts": {k: len(v) for k, v in source_ids.items()},
        "coarse_seed_sha256": digest(coarse), "fine_seed_sha256": digest(fine),
        "source_norm_attainer_records": len(normals),
        "capacity_and_actual_gates_unchanged": True,
        "predicted_new_attainer_rows_will_not_mutate_actual_learning_pools": True}
    return coarse, fine, normals, metadata


def prepare_transfer(request, output, process_started):
    real, models, final, source = read_completed(request)
    args = old_input_namespace(request, output)
    prepared = baseline.growth.prepare_run(args, process_started=process_started)
    restored, bindings, tenth, old_replay, coarse24, fine24 = prepared
    original, old_initial, original_gate, lower, upper, source_cfg, _ = restored
    field, initial, gate, transfer = reconstruct_same_field(
        original, old_initial, original_gate, lower, upper,
        final["exact_binary64_independent_coordinates"],
        final["exact_original_physical_coefficients"], request)
    cfg = copy.deepcopy(real["configuration"])
    inherited_flags = {}
    for key in ("all_coarse_learned_rows_retained",
                "entry_tail159_body_and_tail_controller_inherited_from_this_run154"):
        if key in cfg:
            inherited_flags[key] = cfg[key]
            cfg[key] = False
    cfg["direct_transfer_inherited_scope_labels"] = inherited_flags
    cfg["cross_center_norm_memory_policy"] = "same159-complete-affine-cross-center-unit-normal-memory-v1"
    cfg["direct_exact_physical_state_transfer_with_explicit_new_pool_initialization"] = True
    require((cfg["max_linear_models"], cfg["max_physical_evaluations"],
             cfg["max_seconds"], cfg["linear_program_seconds"]) == (12, 40, 120, 10),
            "original shared caps changed")
    radial, theta, grid = baseline.curvature_grid(tenth)
    coarse, fine, normals, pools = current_pool_seed(
        real, models, coarse24, fine24, len(radial)*len(theta),
        2*len(radial)*len(theta), cfg)
    stage = real[OLD_STAGE]
    trust = stage["last_restricted_trust"]
    streak = stage["final_consecutive_growth_qualifying_models"]
    require(trust == .000125 and streak == 0, "actual terminal source controller differs")
    # Model6 used its last LP without a candidate/feedback. Keep model5's completed state.
    require(not models[-1]["model"].get("trials") and
            not models[-1]["model"].get("scale_feedback_update"), "unfinished source model6 gained fabricated feedback")
    controller = {
        "schema": "completed-log-terminal-controller-direct-transfer-v1",
        "origin": "immutable complete-affine run43728280256 summary and native completed feedback",
        "trust_binary64_exact": str(Q.from_float(float(trust))),
        "trust_evaluated": trust, "success_streak": streak,
        "unfinished_last_model_not_counted_as_success": True,
        "original_last_model_number": 6, "original_last_completed_feedback_model": 5}
    source.update(field_transfer=transfer, new_pool_initialization=pools,
                  original_controller=controller)
    replay = {
        "source_completed_log_transfer": source,
        "canonical_physical_state_sha256": digest(field.identity(initial)),
        "layout_derived_from_actual_problem": baseline.layout_from_problem(original),
        "learned_pool": pools,
        "explicit_new_constraint_definition": {
            "physical_gates_and_thresholds_unchanged": True,
            "new_proposal_algorithm": cfg["cross_center_norm_memory_policy"],
            "new_pool_initialization_is_declared_not_old_history_replay": True},
        "known_fine_metric_locations": [], "controller_continuation": controller,
        "initial_direction_records": normals, "original_report": real}
    return ((field, initial, gate, gate.coordinate_lower, gate.coordinate_upper,
             source_cfg, cfg), bindings, tenth, replay, coarse, fine)

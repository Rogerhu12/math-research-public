#!/usr/bin/env python3
"""One paid MaxTime direction, original actual two-grid gates, zero new solvers."""
from __future__ import annotations
import time
PROCESS_STARTED = time.monotonic()
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import traceback
import numpy as np
from frame_collar_bvp import atomic_save
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_curvature_soc_metric_reserve_audit import exact_vector
from frame_metric_budget_recovery import require_public_research_environment
import frame_metric_finite_cone_audit as frozen_audit
import frame_metric_finite_cone_transfer as frozen_transfer
import frame_metric_direct_reference_audit as direct_audit
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader
from frame_metric_paid_cone_vector import (
    POLICY, POOL_POLICY, SOURCE_NEW_SCIENCE, SOURCE_GLOBAL_SCIENCE,
    SOURCE_VALUES, SOURCE_CONE_VALUES, SOURCE_ACCEPTED_INDEX, SOURCE_STEP_SHA,
    SOURCE_PHYSICAL_SHA, SOURCE_CFG_SHA, SOURCE_FIELD_SHA, CLOSED_HIGHS,
    ContinuationClock, PaidConeVectorObjective, decode_paid_step,
    definition, run_actual_validation, require)

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
SCHEMA = POLICY+"-audit"
STAGE = "paid_cone_vector_validation_stage"
COMPLETE = "complete-two-grid-paid-cone-vector-actual-validation-audit"
TAG = "PAID_CONE_VECTOR_"
NEW_SOURCES = ("frame_metric_paid_cone_vector.py",
               "frame_metric_paid_cone_vector_development.py",
               "frame_metric_paid_cone_vector_audit.py")
PINS = {
    "run_id": "43792959676", "job_id": "133055320913",
    "source_commit": "c0e7336c28b8d1b1f83306e3a0781069f57c0f48",
    "log_bytes": 7416045,
    "log_sha256": "a4a20c9f481fc5d8f1fcce7f279c9c8361e5c84d2da7edd324bd9180b97024c0",
    "request_payload_bytes": 30464,
    "request_payload_sha256": "071fa607bf2fb70a7300876a4b53c669ea520faeb8cfe0a0ad7f6532ec474899",
    "development_payload_bytes": 2464,
    "development_payload_sha256": "3e3f8828d6340932c7661f2c35d6aa8da972b45609fcc80759db5e82a9292e75",
    "prior_payload_bytes": 2069,
    "prior_payload_sha256": "1cd1679d023e03a470570c4bf5f35b5d7514fd07db43a19a46048afefe48a271",
    "model26_payload_bytes": 158563,
    "model26_payload_sha256": "eff56b61616700dd0a1cc4aadff7b717329d930d3e86d36e814a2b4c8021dfee",
    "model27_payload_bytes": 84126,
    "model27_payload_sha256": "046520467133e26d2449bfcf1a7aedb7e85b16da3b00e480727706daa567cbb9",
    "complete_payload_bytes": 3202149,
    "complete_payload_sha256": "8a67d74a139e06c50c6f19e6b265a0c7e5788bd7e6681259712fb8d70a3b189e"}
SOURCE_REQUEST = {
    "path": TOPIC+"/computations/request-finite-cone-primary.json",
    "bytes": 41315, "sha256": "340d6f063831331cfa56f9da64785a05f74a60c7d76c9a858be6c63c5563df64"}
PUBLISHED_NOTE = {
    "path": TOPIC+"/notes/finite-cone-first-actual-and-backend-time-limit-20261116.md",
    "commit": "0442b0fbf8704790756f2e4c957f72777fcb5911",
    "bytes": 23477, "sha256": "65cf357809821976103129c39726103e74c3d4dc96b92bc9de0099acf1bffc34"}
BANK_SHA = "b240dfd9aad4ea6052eec24590b7147102d1f180be1e9c364f5ba996ed1a47cb"
LEARNING_SHA = "b076a3436d0b5c2ae4738013314e9b806f7cf90d74712b28fafd2b791ce1ca76"
COORDINATE_SHA = "b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580"


def implementation_hashes():
    result = frozen_audit.implementation_hashes()
    folder = Path(__file__).parent
    for name in NEW_SOURCES:
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def emit(suffix, value):
    print(TAG+suffix+" "+reader.encoded(value).decode("utf-8"), flush=True)


def tagged_value(records, tag, byte_count, sha):
    require(len(records[tag]) == 1, "one paid original record required: "+tag)
    text, value = records[tag][0]
    encoded = (text+"\n").encode("utf-8")
    require(len(encoded) == byte_count and reader.digest(encoded) == sha,
            "paid original JSON plus LF changed: "+tag)
    return value, {"tag": tag, "JSON_plus_LF_bytes": byte_count, "JSON_plus_LF_sha256": sha}


def model_value(records, number, byte_count, sha):
    found = [(text, value) for text, value in records["FINITE_CONE_MODEL"]
             if value.get("number") == number]
    return tagged_value({"model": found}, "model", byte_count, sha)


def read_source(request, clock):
    clock.check()
    require(request["source"] == PINS and request["source_request"] == SOURCE_REQUEST
            and request["published_actual_note"] == PUBLISHED_NOTE,
            "only the published paid finite-cone source is authorized")
    for meta in (SOURCE_REQUEST, PUBLISHED_NOTE):
        raw = Path(meta["path"]).read_bytes()
        require(len(raw) == meta["bytes"] and reader.digest(raw) == meta["sha256"],
                "published request or human-note identity differs")
    previous_request = json.loads(Path(SOURCE_REQUEST["path"]).read_bytes())
    require(request["original_input_arguments"] == previous_request["original_input_arguments"]
            and len(request["original_input_arguments"]) == 98,
            "all original 24-input CLI arguments must remain unchanged")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+PINS["run_id"])
    job = api.api_json("/actions/jobs/"+PINS["job_id"])
    require(str(run["id"]) == PINS["run_id"] and str(job["id"]) == PINS["job_id"]
            and str(job["run_id"]) == PINS["run_id"]
            and run["head_sha"] == job["head_sha"] == PINS["source_commit"]
            and run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "success",
            "paid source run/job/head/link differs")
    raw, redirects = api.job_log(PINS["job_id"])
    require(len(raw) == PINS["log_bytes"] and reader.digest(raw) == PINS["log_sha256"],
            "paid finite-cone original raw log changed")
    tags = tuple("FINITE_CONE_"+x for x in ("REQUEST", "DEVELOPMENT", "PRIOR_WORK_REUSED", "MODEL", "COMPLETE"))
    records = inherited.tagged_records(raw, tags)
    requested, rm = tagged_value(records, tags[0], PINS["request_payload_bytes"], PINS["request_payload_sha256"])
    dev, dm = tagged_value(records, tags[1], PINS["development_payload_bytes"], PINS["development_payload_sha256"])
    prior, pm = tagged_value(records, tags[2], PINS["prior_payload_bytes"], PINS["prior_payload_sha256"])
    model26, m26m = model_value(records, 26, PINS["model26_payload_bytes"], PINS["model26_payload_sha256"])
    model27, m27m = model_value(records, 27, PINS["model27_payload_bytes"], PINS["model27_payload_sha256"])
    real, cm = tagged_value(records, tags[4], PINS["complete_payload_bytes"], PINS["complete_payload_sha256"])
    old_manifest = requested["source_sha256"]
    require(requested["source_commit"] == PINS["source_commit"]
            and requested["request_bytes"] == SOURCE_REQUEST["bytes"]
            and requested["request_sha256"] == SOURCE_REQUEST["sha256"]
            and old_manifest == previous_request["source_sha256"]
            and len(old_manifest) == 175,
            "paid request175 or original request-file fingerprint differs")
    old_python = {Path(p).name: sha for p, sha in old_manifest.items() if p.endswith(".py")}
    require(len(old_python) == 164 and real["source_files_sha256"] == old_python,
            "paid complete and request164 Python closures differ")
    for path, sha in old_manifest.items():
        require(request["source_sha256"].get(path) == sha
                and reader.digest(Path(path).read_bytes()) == sha,
                "a frozen paid dependency changed: "+path)
    require(dev["all_passed"] is True and dev["executed_check_count"] == 12
            and dev["group_count"] == 3 and [len(g["checks"]) for g in dev["groups"]] == [3, 4, 5]
            and all(g["passed"] is True and all(v is True for v in g["checks"].values()) for g in dev["groups"])
            and dev["execution"] == {
                "actual_geometry_calls": 0, "actual_research_LP_or_cone_calls": 0,
                "new_stub_backend_constructors": 4, "new_tiny_real_Clarabel_calls": 1,
                "original_developer_suites_executed": 0,
                "original_parameter_J_or_directional_JVP_calls": 0},
            "actual paid twelve-check verdict or scope differs")
    require(prior["passed"] is True and prior["paid_eleven_checks"] == 11
            and prior["paid_nine_geometry_checks"] == 9 and prior["old_development_executions"] == 0
            and prior["all_old_sources_match_current_bytes"] is True,
            "the transitive paid eleven/nine receipts differ")
    require(real["schema"] == "same159-finite-lorentz-affine-primary-v1-audit"
            and real["status"] == "complete-two-grid-finite-cone-primary-audit"
            and real["github_sha"] == PINS["source_commit"]
            and str(real["github_run_id"]) == PINS["run_id"] and real["github_repository"] == REPO,
            "paid completed audit provenance differs")
    stage, cp = real["finite_cone_primary_stage"], real["future_finite_cone_checkpoint"]
    require(stage["error"] is None and stage["model_count"] == 27
            and len(records["FINITE_CONE_MODEL"]) == 27
            and [value["number"] for _, value in records["FINITE_CONE_MODEL"]] == list(range(1, 28)),
            "all actual original model identities required")
    require(real["new_scientific_elapsed_seconds_including_input_prepare"] == SOURCE_NEW_SCIENCE
            and real["cumulative_original_scientific_seconds"] == SOURCE_GLOBAL_SCIENCE
            and real["final_value_account"]["cumulative_original_values"] == SOURCE_VALUES
            and real["final_value_account"]["new_values"] == SOURCE_CONE_VALUES
            and real["final_value_account"]["coarse_cumulative"] == real["final_value_account"]["fine_cumulative"] == 58,
            "authoritative final clock or values differ; earlier cp clock is not substituted")
    require(real["final_new_task_solver_account"]["new_cone_calls_started"] == 31
            and real["final_new_task_solver_account"]["new_solver_calls_started"] == 31
            and real["final_new_task_solver_account"]["new_legacy_LP_calls_started"] == 0
            and real["closed_original_HiGHS_counts"] == CLOSED_HIGHS,
            "paid31 and closed64 ledgers differ")
    point = stage["selected_two_grid_physical_point"]
    require(point == cp["selected_two_grid_physical_point"]
            and point["accepted_index"] == cp["selected_accepted_index"] == SOURCE_ACCEPTED_INDEX
            and point["physical_state_sha256"] == cp["selected_physical_state_sha256"] == SOURCE_PHYSICAL_SHA
            and point["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and point["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"]
            and cp["configuration"] == real["configuration"] and digest(cp["configuration"]) == SOURCE_CFG_SHA,
            "full source52 state/configuration was not preserved")
    require(model27["number"] == 27 and model27["linearized_at_accepted_index"] == SOURCE_ACCEPTED_INDEX
            and model27["linearized_at_physical_sha256"] == SOURCE_PHYSICAL_SHA
            and model27["trials"] == [] and model27["corrections"] == []
            and model27["finite_cone_primary"]["returned_candidate"] is False
            and len(model27["finite_cone_primary"]["cone_calls"]) == 1,
            "source final vector must be genuinely untried at this same accepted base")
    call = model27["finite_cone_primary"]["cone_calls"][0]
    require(call["new_cone_solver_ordinal"] == call["new_total_solver_ordinal"] == 31
            and call["backend_status"] == "MaxTime"
            and call["status"] == "backend-status-or-finite-vector-not-eligible"
            and call["charged_before_backend_constructor"] is True
            and call["finite_original161_vector"] is True,
            "original MaxTime filter boundary differs")
    require(call["new_candidate_step_record"]["source"]
            == "this new cone solver vector before any return filter",
            "paid step was not the actual solver return captured before its filter")
    paid_step = decode_paid_step(call["new_candidate_step_record"])
    require("rho" not in call["new_candidate_step_record"]
            and "norm_auxiliary" not in call["new_candidate_step_record"],
            "entry scope requires the actual saved159 record, not invented auxiliaries")
    trial = model26["trials"][0]
    require(model26["number"] == 26 and len(model26["trials"]) == 1
            and trial["accepted_as_next_iterate"] is True and trial["accepted_index"] == 52
            and trial["physical_state_sha256"] == SOURCE_PHYSICAL_SHA
            and trial["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and trial["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"],
            "source m26 must own both original actual receipts at accepted52")
    for label, key in (("coarse", "final_full_grid_constraints"), ("fine", "final_doubled_constraints")):
        value = trial[label+"_decision"]
        require(value == real[key] and len(value["actual_gate_booleans"]) == 14
                and all(v is True for v in value["actual_gate_booleans"].values())
                and value["direct_max_eta"] == point[label]["direct_max_eta"],
                "source initial fourteen-gate receipt differs: "+label)
    require(cp["norm_direction_bank_state_sha256"] == BANK_SHA
            and len(cp["norm_direction_bank_entries"]) == 512
            and len(cp["all_retained_supplemental_normals"]) == 8,
            "complete passive bank/support source differs")
    memory = cp["curvature_defect_guard_learning_checkpoint"]
    require(memory["state_sha256"] == LEARNING_SHA and memory["pending_event_indices"] == []
            and len(memory["events"]) == 62 and len(memory["commits"]) == 61
            and memory["coefficients"] == {
                "coarse": 57.187653029922444, "fine": 67.42701956990882},
            "actual fully committed learning source differs")
    require([len(cp["coarse_pool"]), len(cp["fine_pool"])] == [4448, 4543]
            and [cp["coarse_pool_version"], cp["fine_pool_version"]] == [13, 12]
            and cp["terminal_trust"] == .00025
            and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
            "actual pools/controller source differs")
    for definition_key, sha_key in (
            ("objective_evaluation_definition", "objective_evaluation_sha256"),
            ("ordinary_field_evaluation_definition", "ordinary_field_evaluation_sha256"),
            ("factorization_definition", "factorization_definition_sha256")):
        require(digest(cp[definition_key]) == cp[sha_key],
                "paid complete definition fingerprint differs: "+definition_key)
    require(cp["ordinary_field_evaluation_sha256"] == SOURCE_FIELD_SHA,
            "original direct ordinary evaluator differs")
    receipt = {
        "schema": POLICY+"-paid-source-receipt", "passed": True, "source": copy.deepcopy(PINS),
        "original_record_fingerprints": [rm, dm, pm, m26m, m27m, cm],
        "frozen_source_bindings": 175, "frozen_Python_sources": 164,
        "all_frozen_sources_match_current_bytes": True,
        "paid12_cone_development_checks": 12, "transitive_paid11_and9": [11, 9],
        "all_old_developer_solver_geometry_J_JVP_trial_replays": 0,
        "one_latest_original_log_read": True, "earlier_original_logs_downloaded": 0,
        "redirects_without_authorization": redirects,
        "source_MaxTime_status_unchanged": True, "source_model27_had_no_actual_trial": True,
        "source_model26_owns_actual_initial_point52_two_grid_receipts": True,
        "saved159_step_sha256": SOURCE_STEP_SHA, "missing_rho_and_norm_not_reconstructed": True,
        "source_final_clocks_used_not_earlier_checkpoint_clocks": True,
        "published_actual_note": copy.deepcopy(PUBLISHED_NOTE),
        "payload_repository_artifact_cache_uploads": 0}
    clock.check()
    return {"report": real, "checkpoint": cp, "point": point, "paid_step": paid_step,
            "paid_step_record": copy.deepcopy(call["new_candidate_step_record"]),
            "receipt": receipt, "gate_receipts": {
                "coarse": copy.deepcopy(trial["coarse_decision"]),
                "fine": copy.deepcopy(trial["fine_decision"])},
            "backend_receipt": {
                "backend_status": call["backend_status"], "source_call_ordinal": 31,
                "source_complete_call_seconds": call["complete_call_and_repair_elapsed_seconds"],
                "source_solve_seconds": call["backend_reported_solve_seconds"],
                "original_state_filter_not_promoted": True}}


def prepare(request, output, completed, clock):
    clock.check()
    cp = completed["checkpoint"]
    args = inherited.previous.old_input_namespace(request, output)
    prepared = baseline.growth.prepare_run(args, process_started=PROCESS_STARTED)
    clock.check()
    restored, bindings, tenth, unused_old_replay, unused_coarse24, unused_fine24 = prepared
    original, _, original_gate, lower, upper, historical_cfg, _ = restored
    coordinate_sha = digest(cp["coordinate_definition"])
    require(coordinate_sha == COORDINATE_SHA, "exact original coordinate map differs")
    field_request = {
        "source": {"coordinate_definition_sha256": coordinate_sha},
        "fixed_complete_metric_sha256": request["fixed_complete_metric_sha256"],
        "fixed_b0_definition_sha256": request["fixed_b0_definition_sha256"]}
    field, initial, gate, field_receipt = inherited.reconstruct_checkpoint_field(
        original, original_gate, lower, upper, cp, field_request)
    adapter = DirectReferenceFiveHeightField(field)
    cfg = copy.deepcopy(cp["configuration"])
    require(digest(adapter.identity(initial)) == SOURCE_PHYSICAL_SHA
            and digest(adapter.evaluation_definition()) == SOURCE_FIELD_SHA
            and digest(cfg) == SOURCE_CFG_SHA, "physical52/g/b0/cfg/direct field differs")
    radial, theta, grid = baseline.curvature_grid(tenth)
    require(grid == completed["report"]["full_value_sampling_definition"],
            "complete original ordinary sampling grid differs")
    for label, nt in (("coarse", len(theta)), ("fine", 2*len(theta))):
        rg = RationalRowGrid(label, grid["radial_nodes_exact"], nt)
        require(rg.definition_sha256 == cp["norm_direction_bank_context"]["original_grids"][label],
                "same rational original row-ID grid required: "+label)
    counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    require(counts == cp["norm_direction_bank_context"]["original_point_counts"],
            "same original point counts required")
    coarse = inherited.checked_pool(cp["coarse_pool"], counts["coarse"], cfg["max_pool_rows"], "coarse")
    fine = inherited.checked_pool(cp["fine_pool"], counts["fine"], cfg["max_fine_physical_pool_rows"], "fine")
    gate, gate_receipt = direct_audit.fresh_adapter_gate(
        gate, adapter, initial, gate.coordinate_lower, gate.coordinate_upper)
    bounded = adapter.original_problem.base
    order = int(bounded.primitive_order)
    require(order == int(bounded.fixed_primitive.order) == 8, "original query/fixed primitive order changed")
    replay = {
        "source_checkpoint": cp, "source_current_point": copy.deepcopy(completed["point"]),
        "source_snapshot_scalar_counters": copy.deepcopy(
            completed["report"]["finite_cone_primary_stage"]["snapshot_scalar_counters"]),
        "source_final_gate_receipts": copy.deepcopy(completed["gate_receipts"]),
        "paid_source_receipt": copy.deepcopy(completed["receipt"]),
        "source_backend_receipt": copy.deepcopy(completed["backend_receipt"]),
        "source_completed_log_transfer": {
            "same_exact_reference163_current159_physical163": True,
            "same_original_g_b0_coordinate_and_two_grid_definitions": True,
            "original_24_input_reports_loaded_once": True,
            "old_source_ordinary_or_solver_replays": 0,
            "field_transfer": field_receipt, "fresh_adapter_gate": gate_receipt,
            "original_order_from_bounded_primitive_order": order,
            "source_configuration_unchanged": True,
            "historical24_configuration_sha256": digest(historical_cfg),
            "no_pool_initialize_or_automatic_expand": True}}
    clock.check()
    return {
        "problem": adapter, "initial": initial, "gate": gate, "cfg": cfg,
        "radial": radial, "theta": theta, "grid": grid, "order": order,
        "lower": gate.coordinate_lower, "upper": gate.coordinate_upper,
        "bindings": bindings, "replay": replay, "coarse_pool": coarse, "fine_pool": fine,
        "paid_step": completed["paid_step"]}


def final_receipts(stage, replay):
    point = stage["selected_two_grid_physical_point"]
    if point["accepted_index"] == SOURCE_ACCEPTED_INDEX:
        require(point["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
                "unchanged accepted52 has another physical identity")
        return (copy.deepcopy(replay["source_final_gate_receipts"]["coarse"]),
                copy.deepcopy(replay["source_final_gate_receipts"]["fine"]),
                {"kind": "paid-model26-original-two-grid-receipts-at-the-same-physical52",
                 "accepted_index": 52, "new_geometry_replays": 0})
    matches = [t for t in stage["trials"] if t.get("accepted_as_next_iterate") is True
               and t.get("accepted_index") == point["accepted_index"]
               and t.get("physical_state_sha256") == point["physical_state_sha256"]]
    require(point["accepted_index"] == 53 and len(matches) == 1,
            "one actual accepted trial must own new point53")
    t = matches[0]
    return (copy.deepcopy(t["coarse_decision"]), copy.deepcopy(t["fine_decision"]),
            {"kind": "new-actual-only-paid-vector-two-grid-trial",
             "trial_number": t["number"], "alpha_exact": t["alpha_exact"],
             "accepted_index": 53, "new_independent_final_geometry_calls": 0})


def future_checkpoint(objective, stage, paid_step_record):
    source = objective.validation_replay["source_checkpoint"]
    result = copy.deepcopy(source)
    point = stage["selected_two_grid_physical_point"]
    result.update(
        schema=POLICY+"-future-checkpoint",
        selected_accepted_index=point["accepted_index"],
        selected_physical_state_sha256=point["physical_state_sha256"],
        selected_final159_binary64_exact=copy.deepcopy(point["exact_binary64_independent_coordinates"]),
        selected_final163_physical_exact=copy.deepcopy(point["exact_original_physical_coefficients"]),
        selected_two_grid_physical_point=copy.deepcopy(point),
        coarse_pool=objective.pool.tolist(), fine_pool=objective.fine_pool.tolist(),
        coarse_pool_version=objective.pool_version, fine_pool_version=objective.fine_pool_version,
        coarse_pool_history=copy.deepcopy(objective.pool_history),
        fine_pool_history=copy.deepcopy(objective.fine_pool_history),
        source_affine_objective_evaluation_definition=copy.deepcopy(source["objective_evaluation_definition"]),
        source_affine_objective_evaluation_sha256=source["objective_evaluation_sha256"],
        objective_evaluation_definition=copy.deepcopy(objective.evaluation_definition),
        objective_evaluation_sha256=objective.evaluation_sha256,
        cumulative_original_actual_values=objective.full_value_evaluations,
        new_finite_cone_actual_values=SOURCE_CONE_VALUES+objective.full_value_evaluations-SOURCE_VALUES,
        value_only_validation={
            "policy": POLICY, "source": copy.deepcopy(PINS),
            "source_backend_status": "MaxTime", "source_model_number": 27, "source_cone_ordinal": 31,
            "saved_source_exact159_step_record": copy.deepcopy(paid_step_record),
            "rho_and_norm_auxiliaries_remain_unavailable": True,
            "tried_fractions_exact": [t["alpha_exact"] for t in stage["trials"]],
            "each_trial_full159_and_physical163_is_in_native_TRIAL_records": all(
                len(t.get("exact_binary64_independent_coordinates", [])) == 159
                and len(t.get("exact_original_physical_coefficients", [])) == 163 for t in stage["trials"]),
            "source_bank_and_learning_passively_retained_without_replay_or_rebinding": True,
            "no_affine_model_or_selected_J_is_claimed_for_new_or_old_point": True,
            "ordinary_value_only_pool_learning_policy": POOL_POLICY,
            "controller_without_model_quality_feedback_unchanged": True,
            "source_final_authoritative_science": {
                "cone_task": SOURCE_NEW_SCIENCE, "original_global": SOURCE_GLOBAL_SCIENCE},
            "clock_at_checkpoint": objective.continuation_clock.report(),
            "final_COMPLETE_clock_is_later_and_authoritative": True},
        cumulative_original_scientific_elapsed_seconds_at_checkpoint=
            objective.continuation_clock.report()["cumulative_original_scientific_seconds"],
        new_finite_cone_scientific_elapsed_seconds_at_checkpoint=
            objective.continuation_clock.report()["cumulative_cone_task_scientific_seconds"])
    # No inherited phrase may pretend this new entry captured a solver vector.
    result["source_finite_cone_capture_evidence"] = result.pop("actual_solver_and_trial_capture_evidence", None)
    result.pop("all_finite_solver_exact159_records_are_in_the_native_MODEL_records", None)
    result["source_finite_cone_new_task_account"] = copy.deepcopy(source["finite_cone_new_task_account"])
    result["finite_cone_new_task_account"] = copy.deepcopy(source["finite_cone_new_task_account"])
    continued = objective.continuation_clock.report()
    result["finite_cone_new_task_account"].update(
        new_scientific_seconds=continued["cumulative_cone_task_scientific_seconds"],
        remaining_scientific_seconds_in_intersection=continued["remaining_scientific_seconds_in_intersection"],
        current_continued_science_clock=continued,
        no_additional_cone_calls_during_actual_only_validation=True)
    result["source_current_point27_plus_new_acceptances_scope"] = result.pop(
        "current_source_point27_plus_new_acceptances_scope", None)
    require(result["norm_direction_bank_state_sha256"] == BANK_SHA
            and result["curvature_defect_guard_learning_checkpoint"]["state_sha256"] == LEARNING_SHA
            and result["curvature_defect_guard_learning_checkpoint"]["pending_event_indices"] == []
            and result["terminal_trust"] == .00025
            and result["terminal_success_streak"] == result["terminal_covered_ordinary_growth_streak"] == 0,
            "passive bank/learning/controller checkpoint was changed")
    return result


def summary(report):
    stage = report.get(STAGE, {})
    point = stage.get("selected_two_grid_physical_point") or {}
    return {
        "schema": SCHEMA+"-summary", "status": report.get("status"),
        "stage_status": stage.get("status"), "error": report.get("error") or stage.get("error"),
        "budget_message": stage.get("budget_message"),
        "new_actual_trial_records": len(stage.get("trials", [])),
        "new_acceptances": stage.get("new_acceptances", 0),
        "selected_accepted_index": point.get("accepted_index"),
        "selected_physical_state_sha256": point.get("physical_state_sha256"),
        "maximum_eta_on_both_grids": point.get("maximum_eta_on_both_grids"),
        "new_metric_target_qualified_on_both_grids": point.get("new_metric_target_qualified_on_both_grids"),
        "final_selection_validation": report.get("final_selection_validation"),
        "final_value_account": report.get("final_value_account"),
        "continued_science_account": report.get("continued_science_account"),
        "new_development_receipt": report.get("new_development_receipt"),
        "source_cone31_and_HiGHS64_preserved": True,
        "new_solver_LP_SOC_J_JVP_calls": 0,
        "source_MaxTime_status_not_promoted": True,
        "new_independent_final_geometry_calls": 0,
        "process_total_elapsed_seconds": report.get("process_total_elapsed_seconds"),
        "peak_rss_kib_linux": report.get("peak_rss_kib_linux"),
        "payload_only_in_runner_and_original_stdout": True}


def save_report(output, report, clock):
    report["process_total_elapsed_seconds"] = time.monotonic()-PROCESS_STARTED
    report["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if clock is not None:
        report["continued_science_account"] = clock.report()
    atomic_save(output, report)
    atomic_save(Path(output).with_name("paid-cone-vector-actual-summary.json"), summary(report))


def run_audit(prepared, completed, output, clock, report):
    problem, initial, gate, cfg = (prepared[k] for k in ("problem", "initial", "gate", "cfg"))
    replay = prepared["replay"]
    report.update({
        "schema": SCHEMA, "status": "paid-vector-objective-not-yet-constructed",
        "configuration": copy.deepcopy(cfg), "policy_definition": definition(),
        "exact_original_input_storage": prepared["bindings"],
        "source_transfer": copy.deepcopy(replay["source_completed_log_transfer"]),
        "source_selected_physical_point": copy.deepcopy(replay["source_current_point"]),
        "initial_actual_two_grid_gate_source": {
            "source_model_number": 26, "source_accepted_index": 52,
            "source_physical_sha256": SOURCE_PHYSICAL_SHA,
            "new_initial_ordinary_value_calls": 0},
        "closed_original_HiGHS_counts": copy.deepcopy(CLOSED_HIGHS),
        "paid_finite_cone_calls_unchanged": 31,
        "remaining_cone_slot_unconsumed": 1,
        "source_solver_MaxTime_status": "MaxTime",
        "source_no_trial_and_missing_auxiliary_scope": copy.deepcopy(completed["backend_receipt"]),
        "source_saved_exact159_step_record": copy.deepcopy(completed["paid_step_record"]),
        "source_snapshot_scalar_counters": copy.deepcopy(replay["source_snapshot_scalar_counters"]),
        "full_value_sampling_definition": copy.deepcopy(prepared["grid"]),
        "source_bank_learning_and_controller_are_passive": True})
    objective = None
    constructor_started = time.monotonic()
    try:
        objective = PaidConeVectorObjective(
            problem, gate, prepared["radial"], prepared["theta"], prepared["order"],
            prepared["lower"], prepared["upper"], cfg=cfg, checkpoint=None,
            radial_nodes_exact=prepared["grid"]["radial_nodes_exact"],
            replay=replay, continuation_clock=clock,
            coarse_pool=prepared["coarse_pool"], fine_pool=prepared["fine_pool"])
        report["timing_segments"]["value_only_constructor_seconds"] = time.monotonic()-constructor_started
        report["actual_definition_hashes"] = {
            "source_objective": replay["source_checkpoint"]["objective_evaluation_sha256"],
            "new_value_only_objective": objective.evaluation_sha256,
            "same_ordinary_field": digest(problem.evaluation_definition()),
            "same_coordinate": problem.coordinate_definition_sha256,
            "same_configuration": digest(cfg),
            "factorization_not_instantiated_or_rebound": True}
        started = time.monotonic()
        stage = run_actual_validation(objective, initial, completed["paid_step"])
        report[STAGE] = stage
        report["timing_segments"]["actual_validation_seconds"] = time.monotonic()-started
        point = stage["selected_two_grid_physical_point"]
        final = exact_vector(point["exact_binary64_independent_coordinates"], 159)
        require(np.array_equal(final, np.asarray(point["independent_coordinates_binary64"], float))
                and digest(problem.identity(final)) == point["physical_state_sha256"]
                and [str(x) for x in problem.coordinates.physical_exact(final)]
                    == point["exact_original_physical_coefficients"], "final exact physical identity differs")
        box = problem.coordinates.exact_box_decision(final, gate.original_lower, gate.original_upper)
        require(box["exact_original_box_pass"] is True, "selected physical163 box failed")
        copied, copied_state = problem.frozen_metric_copy(final)
        require(copied is problem and copied_state.tobytes() == final.tobytes()
                and copied.metric_model(copied_state) == problem.metric_model(initial)
                and copied.height_base_definition == problem.height_base_definition,
                "original g/b0 or selected exact field changed")
        coarse, fine, owner = final_receipts(stage, replay)
        flags = {label: d["actual_gate_booleans"] for label, d in (("coarse", coarse), ("fine", fine))}
        require(all(len(v) == 14 and all(x is True for x in v.values()) for v in flags.values()),
                "selected point lacks complete original fourteen-gate receipts")
        require(all(d["direct_max_eta"] == point[label]["direct_max_eta"]
                    for label, d in (("coarse", coarse), ("fine", fine))),
                "selected scalar and actual two-grid receipt differ")
        report["final_selection_validation"] = {
            "both_value_grids_hard_and_old_metric_pass": True,
            "exact_original_box_pass": True,
            "source_eta": replay["source_current_point"]["maximum_eta_on_both_grids"],
            "both_grid_maximum_eta": point["maximum_eta_on_both_grids"],
            "actual_eta_decrease": replay["source_current_point"]["maximum_eta_on_both_grids"]-point["maximum_eta_on_both_grids"],
            "both_grid_maximum_curvature": point["maximum_curvature_on_both_grids"],
            "new_metric_target_qualified_on_both_grids": point["new_metric_target_qualified_on_both_grids"],
            "accepted_index": point["accepted_index"], "not_a_new_independent_final_audit": True}
        report["final_full_grid_constraints"], report["final_doubled_constraints"] = coarse, fine
        report["final_actual_gate_booleans"], report["selected_gate_receipt_source"] = flags, owner
        report["final_exact_box"] = box
        report["future_value_only_checkpoint"] = future_checkpoint(objective, stage, completed["paid_step_record"])
        report["status"] = COMPLETE if stage.get("error") is None else "paid-vector-stage-error-best-retained"
    except Exception as error:
        report["status"] = "paid-vector-audit-error"
        report["error"] = {"type": type(error).__name__, "message": str(error), "traceback": traceback.format_exc()}
        if objective is not None and objective.validation_trace is not None:
            report.setdefault(STAGE, objective.validation_trace)
    finally:
        report["timing_segments"].setdefault("value_only_constructor_seconds", time.monotonic()-constructor_started)
        if objective is not None:
            report["direct_reference_geometry_timing"] = problem.timing_snapshot()
            report["final_value_account"] = objective.value_account()
            report["value_call_events"] = copy.deepcopy(objective.value_call_events)
            report["failed_coarse_value_receipts"] = copy.deepcopy(objective.failed_coarse_value_receipts)
            report["zero_derivative_or_solver_execution"] = objective.zero_derivative_receipt()
            report["terminal_pool_counts"] = [len(objective.pool), len(objective.fine_pool)]
            report["terminal_pool_versions"] = [objective.pool_version, objective.fine_pool_version]
            report["passive_state_identity"] = {
                "bank_entries": 512, "bank_state_sha256": BANK_SHA, "supplemental_rows": 8,
                "learning_state_sha256": LEARNING_SHA, "events": 62, "commits": 61, "pending": 0,
                "trust": .00025, "legacy_streak": 0, "covered_streak": 0,
                "new_curvature_training_model_feedback_or_bank_replay": 0}
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    require_public_research_environment()
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    raw_request = Path(args.request).read_bytes()
    request = json.loads(raw_request)
    clock = None
    completed = None
    dev_started = dev_seconds = None
    report = {
        "schema": SCHEMA, "status": "paid-vector-input-not-yet-read",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "source_files_sha256": implementation_hashes(), "source": copy.deepcopy(PINS),
        "source_final_cone_science_seconds": SOURCE_NEW_SCIENCE,
        "source_final_original_science_seconds": SOURCE_GLOBAL_SCIENCE,
        "source_actual_values": SOURCE_VALUES, "new_actual_values_before_objective": 0,
        "timing_segments": {}, "new_scientific_solver_J_JVP_calls": 0}
    try:
        require(request["parameters"] == {
            **definition(), "new_development_groups": 2, "new_development_checks": 6,
            "new_group_check_counts": [3, 3],
            "old12_11_9_checks_reexecuted": 0, "source_log_reads": 1,
            "original_input_reports": 24}, "approved actual-only parameter contract differs")
        for path, sha in request["source_sha256"].items():
            require(reader.digest(Path(path).read_bytes()) == sha, "requested source changed: "+path)
        requested_python = {Path(p).name: sha for p, sha in request["source_sha256"].items() if p.endswith(".py")}
        require(requested_python == implementation_hashes() and len(requested_python) == 167,
                "all old164 plus exactly three new Python sources required")
        emit("REQUEST", {
            "source_commit": os.environ.get("GITHUB_SHA"), "request_bytes": len(raw_request),
            "request_sha256": reader.digest(raw_request), "parameters": request["parameters"],
            "source_sha256": request["source_sha256"]})
        dev_started = time.monotonic()
        from frame_metric_paid_cone_vector_development import developer_check
        dev = developer_check()
        dev_seconds = time.monotonic()-dev_started
        report["new_development_receipt"] = dev
        emit("DEVELOPMENT", dev)
        require(dev["all_passed"] is True and dev["executed_check_count"] == 6,
                "new value-only interfaces did not all pass")
        clock = ContinuationClock(time.monotonic())
        before = time.monotonic()
        completed = read_source(request, clock)
        report["timing_segments"]["latest_paid_log_read_and_validation_seconds"] = time.monotonic()-before
        report["paid_source_receipt"] = completed["receipt"]
        emit("PRIOR_WORK_REUSED", completed["receipt"])
        before = time.monotonic()
        prepared = prepare(request, output, completed, clock)
        report["timing_segments"]["necessary24_input_prepare_seconds"] = time.monotonic()-before
        run_audit(prepared, completed, output, clock, report)
    except Exception as error:
        if dev_started is not None and dev_seconds is None:
            dev_seconds = time.monotonic()-dev_started
        report["status"] = "paid-vector-input-or-reporting-error"
        report["error"] = {"type": type(error).__name__, "message": str(error), "traceback": traceback.format_exc()}
        if completed is not None and STAGE not in report:
            report["source_unchanged_complete_checkpoint_after_input_failure"] = copy.deepcopy(completed["checkpoint"])
            report["source_checkpoint_unchanged_no_objective_or_new_actual_trial"] = True
    report["timing_segments"]["new_development_seconds_separate_from_science"] = dev_seconds
    report["new_development_started"] = dev_started is not None
    try:
        save_report(output, report, clock)
    except Exception as error:
        report["status"] = "paid-vector-report-save-error-actual-stage-retained"
        report["report_save_error"] = {"type": type(error).__name__, "message": str(error)}
        report["process_total_elapsed_seconds"] = time.monotonic()-PROCESS_STARTED
        if clock is not None:
            report["continued_science_account"] = clock.report()
    for trial in report.get(STAGE, {}).get("trials", []):
        emit("TRIAL", trial)
    # No global semantic filter may delete the paid or new physical vectors.
    emit("COMPLETE", report)
    for path in sorted(output.parent.glob("*.json")):
        raw = path.read_bytes()
        emit("OUTPUT_METADATA", {"filename": path.name, "bytes": len(raw), "sha256": reader.digest(raw),
                                 "payload_repository_artifact_cache_upload": False})
    return 0 if report.get("status") == COMPLETE else 1


if __name__ == "__main__":
    raise SystemExit(main())

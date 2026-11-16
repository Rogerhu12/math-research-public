#!/usr/bin/env python3
"""Read exactly the paid cone32 log and restore inputs without old science."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid, array_digest
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_curvature_soc_metric_reserve_audit import exact_vector
import read_original_actions_log as reader
import frame_metric_final_cone32_audit as source_audit
import frame_metric_paid_cone_vector_audit as paid
import frame_metric_direct_reference_audit as direct_audit
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
from frame_metric_p32_line_envelope import (
    POLICY, SOURCE_GLOBAL_SECONDS, SOURCE_CLOSED_CONE_SECONDS,
    SOURCE_ORIGINAL_VALUES, require)
from frame_metric_p32_line_actual import (
    SOURCE_CFG_SHA, SOURCE_FIELD_SHA, SOURCE_PHYSICAL_SHA, SOURCE_ACCEPTED_INDEX)

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
PINS = {
    "run_id": "43800505444", "job_id": "133079366251",
    "source_commit": "8dfe5272b6d4f4fb752c8962689b22a95c61f78a",
    "log_bytes": 3503842,
    "log_sha256": "445108ab5e8b15822331bcf080388969a51dc3021d0eda6937759fedae20306f",
    "request_payload_bytes": 29716,
    "request_payload_sha256": "f8e22d359d911ee1075e08041f19a1ca966e75707cb93711c7f4f6d22acaf13f",
    "prior_payload_bytes": 5185,
    "prior_payload_sha256": "641f4b9933fd82c0587d75fe00c473254aed58b357222d2b409640ad8028d083",
    "model_payload_bytes": 122226,
    "model_payload_sha256": "c10a67934b49edeb0b87b1612cb281f59b26449470b4fb54eb8e85ceac9e6d8b",
    "complete_payload_bytes": 3251685,
    "complete_payload_sha256": "1f029b442de75b27baec55352d0dee72d3d4fc753f8202f2291f99a18da08e1f"}
SOURCE_REQUEST = {
    "path": TOPIC+"/computations/request-final-cone32.json", "bytes": 40422,
    "sha256": "39458fd2dff42510a5719491e2402ce37ef69663986eecf11896b10a21c2e332"}
PUBLISHED_NOTE = {
    "path": TOPIC+"/notes/final-cone32-first-actual-and-complete-grid-separation-20261116.md",
    "commit": "482dce395cd037559aa4c43cb6133e1bec1d8fd7", "bytes": 19117,
    "sha256": "d0c7bc22ad1fbf5a9f3a380048aaea7e6b53bd8143c7e4c43f06f70768709ab9"}
SOURCE_BANK_SHA = "233b2e81fdd0ab36f3306d2d901e8708bb103ea34c9c20ef006537d371634527"
SOURCE_LEARNING_SHA = "b076a3436d0b5c2ae4738013314e9b806f7cf90d74712b28fafd2b791ce1ca76"
SOURCE_DIRECTION_BODY_HASH = "451be7b6aae16793e85727ac19295ac0138a750a8710267ad44608f6676a72dd"


def _exact_binary64(values, length):
    require(isinstance(values, list) and len(values) == length
            and all(isinstance(v, str) for v in values), "actual exact-vector strings required")
    rational = [Q(v) for v in values]
    array = np.asarray([float(v) for v in rational], float)
    require(np.all(np.isfinite(array)) and all(
        Q.from_float(float(v)) == q for v, q in zip(array, rational)),
        "source vector is not exactly binary64 recoverable")
    return array


def read_source(request, ledger):
    ledger.check()
    require(request["source"] == PINS and request["source_request"] == SOURCE_REQUEST
            and request["published_actual_note"] == PUBLISHED_NOTE,
            "only the completed and published cone32 source is authorized")
    for meta in (SOURCE_REQUEST, PUBLISHED_NOTE):
        raw = Path(meta["path"]).read_bytes()
        require(len(raw) == meta["bytes"] and reader.digest(raw) == meta["sha256"],
                "source request or published actual-note fingerprint differs")
    old_request = json.loads(Path(SOURCE_REQUEST["path"]).read_bytes())
    require(request["original_input_arguments"] == old_request["original_input_arguments"]
            and len(request["original_input_arguments"]) == 98,
            "all original24-input CLI values must remain unchanged")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+PINS["run_id"])
    job = api.api_json("/actions/jobs/"+PINS["job_id"])
    require(str(run["id"]) == str(job["run_id"]) == PINS["run_id"]
            and str(job["id"]) == PINS["job_id"]
            and run["head_sha"] == job["head_sha"] == PINS["source_commit"]
            and run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "success",
            "original run/job/link/source/conclusion differs")
    raw, redirects = api.job_log(PINS["job_id"])
    require(len(raw) == PINS["log_bytes"] and reader.digest(raw) == PINS["log_sha256"],
            "paid cone32 original log differs")
    fields = (("REQUEST", "request"), ("PRIOR_WORK_REUSED", "prior"),
              ("MODEL", "model"), ("COMPLETE", "complete"))
    records = inherited.tagged_records(raw, tuple("FINAL_CONE32_"+name for name, _ in fields))
    values, fingerprints = {}, []
    for name, field in fields:
        value, receipt = paid.tagged_value(
            records, "FINAL_CONE32_"+name,
            PINS[field+"_payload_bytes"], PINS[field+"_payload_sha256"])
        values[name] = value
        fingerprints.append(receipt)
    actual_request, prior, model, real = (
        values[name] for name in ("REQUEST", "PRIOR_WORK_REUSED", "MODEL", "COMPLETE"))
    manifest = actual_request["source_sha256"]
    old_py = {Path(path).name: sha for path, sha in manifest.items() if path.endswith(".py")}
    require(actual_request["source_commit"] == PINS["source_commit"]
            and actual_request["request_bytes"] == SOURCE_REQUEST["bytes"]
            and actual_request["request_sha256"] == SOURCE_REQUEST["sha256"]
            and manifest == old_request["source_sha256"] and len(manifest) == 189
            and len(old_py) == 170 and real["source_files_sha256"] == old_py,
            "paid189/170 actual source closure differs")
    for path, sha in manifest.items():
        require(request["source_sha256"].get(path) == sha
                and reader.digest(Path(path).read_bytes()) == sha,
                "a paid source or source parameter file changed: "+path)
    require(prior["passed"] is True and prior["all_frozen_sources_match_current_bytes"] is True
            and prior["paid_check_counts"] == [6, 12, 11, 9]
            and prior["new_checks_executed"] == 0
            and prior["old_developer_solver_geometry_J_JVP_trial_replays"] == 0,
            "transitive paid6/12/11/9 receipt differs")
    require(real["schema"] == source_audit.SCHEMA and real["status"] == source_audit.COMPLETE
            and real["github_sha"] == PINS["source_commit"]
            and str(real["github_run_id"]) == PINS["run_id"]
            and real["github_repository"] == REPO
            and real["new_developer_or_tiny_solver_executions"] == 0,
            "completed cone32 audit identity differs")
    stage, cp = real[source_audit.STAGE], real["future_final_cone32_checkpoint"]
    require(stage["status"] == "finite-cone-model-no-returnable-step-not-stationarity"
            and stage["error"] is None and stage["model_count"] == 1
            and not model["trials"]
            and model["result"] == "no-returnable-finite-cone-affine-step",
            "only the previously untried p32 direction is authorized")
    events = model["finite_cone_primary"]["cone_calls"]
    require(len(events) == len(real["all_current_cone_events"]) == 1
            and events[0] == real["all_current_cone_events"][0],
            "one native full cone32 event must agree with COMPLETE")
    event = events[0]
    require(event["new_cone_solver_ordinal"] == 32 and event["backend_status"] == "AlmostSolved"
            and event["status"] == "complete-affine-candidate-repaired"
            and event["finite_original161_vector"] is True
            and event["gap_met"] is False and event["candidate_positive_above_original_floor"] is False,
            "source status and unreturned/nonimproving full-step boundary differ")
    vector = event["actual_complete_solver_vector_record"]
    step = _exact_binary64(vector["exact_binary64_independent_step159"], 159)
    raw161 = _exact_binary64(vector["exact_binary64_original_solver_variables161"], 161)
    scale = _exact_binary64(vector["exact_binary64_primary_step_scale"], 159)
    require(vector["captured_before_status_or_original_candidate_filters"] is True
            and np.array_equal(step, scale*raw161[:159])
            and array_digest(raw161) == vector["solver_variables_array_sha256"]
            and array_digest(step) == event["new_candidate_step_record"]["array_sha256"]
                == SOURCE_DIRECTION_BODY_HASH
            and vector["exact_binary64_independent_step159"]
                == event["new_candidate_step_record"]["exact_binary64_independent_step"]
            and vector["exact_binary64_original_solver_rho"] == str(Q.from_float(float(raw161[159])))
            and vector["exact_binary64_original_solver_norm_auxiliary"] == str(Q.from_float(float(raw161[160]))),
            "actual saved161/scaled159/auxiliary identities differ")
    require(real["continued_science_account"]["cumulative_original_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
            and real["continued_science_account"]["cumulative_cone_task_scientific_seconds"]
                == SOURCE_CLOSED_CONE_SECONDS
            and real["final_value_account"]["cumulative_original_values"] == SOURCE_ORIGINAL_VALUES
            and real["final_value_account"]["coarse_cumulative"]
                == real["final_value_account"]["fine_cumulative"] == 62
            and real["final_solver_account"]["new_cone_calls_started"] == 32
            and real["old_HiGHS_counts"]["linear_program_invocation_count"] == 64,
            "final authoritative clocks/closed32/64/source124 values differ")
    point = cp["selected_two_grid_physical_point"]
    require(point == stage["selected_two_grid_physical_point"] == real["source_current_point"]
            and point["accepted_index"] == cp["selected_accepted_index"] == SOURCE_ACCEPTED_INDEX
            and point["physical_state_sha256"] == cp["selected_physical_state_sha256"] == SOURCE_PHYSICAL_SHA
            and point["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and point["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"]
            and cp["configuration"] == real["configuration"] and digest(cp["configuration"]) == SOURCE_CFG_SHA,
            "true current52/reference/physical/unchanged configuration differs")
    for key, sha_key in (
            ("objective_evaluation_definition", "objective_evaluation_sha256"),
            ("ordinary_field_evaluation_definition", "ordinary_field_evaluation_sha256"),
            ("factorization_definition", "factorization_definition_sha256")):
        require(digest(cp[key]) == cp[sha_key], "source definition fingerprint differs: "+key)
    require(cp["ordinary_field_evaluation_sha256"] == SOURCE_FIELD_SHA
            and cp["norm_direction_bank_state_sha256"] == SOURCE_BANK_SHA
            and len(cp["norm_direction_bank_entries"]) == 512
            and len(cp["all_retained_supplemental_normals"]) == 8
            and (len(cp["coarse_pool"]), len(cp["fine_pool"]),
                 cp["coarse_pool_version"], cp["fine_pool_version"]) == (4448, 4544, 13, 13)
            and 159001 in cp["fine_pool"] and cp["terminal_trust"] == .00025
            and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
            "latest actual pools/controller/passive information state differs")
    learning = cp["curvature_defect_guard_learning_checkpoint"]
    require(learning["state_sha256"] == SOURCE_LEARNING_SHA
            and learning["pending_event_indices"] == []
            and len(learning["events"]) == 62 and len(learning["commits"]) == 61,
            "source committed learning history differs")
    gates = {}
    for label, key in (("coarse", "final_full_grid_constraints"), ("fine", "final_doubled_constraints")):
        decision = real[key]
        require(len(decision["actual_gate_booleans"]) == 14
                and all(v is True for v in decision["actual_gate_booleans"].values())
                and decision["direct_max_eta"] == point[label]["direct_max_eta"],
                "source current52 full14-gate receipt differs: "+label)
        gates[label] = copy.deepcopy(decision)
    oracle = real["complete_original_grid_oracle_progress"]
    require(len(oracle) == 1 and len(oracle[0]["initial_four_maxima"]) == 4
            and len(event["complete_original_grid_maxima"]) == 4
            and len(event["complete_original_grid_attainers"]) == 4,
            "paid complete endpoint/attainer data missing")
    check = {
        "source": copy.deepcopy(PINS),
        "initial_four_maxima": copy.deepcopy(oracle[0]["initial_four_maxima"]),
        "direction_four_maxima": copy.deepcopy(event["complete_original_grid_maxima"]),
        "attainers": copy.deepcopy(event["complete_original_grid_attainers"])}
    cost = {
        "ancestor_final_original_scientific_seconds": SOURCE_GLOBAL_SECONDS,
        "closed_cone_task_scientific_seconds_not_added_twice": SOURCE_CLOSED_CONE_SECONDS,
        "closed_HiGHS_calls": 64, "closed_cone_calls": 32,
        "source_original_full_values": SOURCE_ORIGINAL_VALUES,
        "source_process_seconds": real["process_total_elapsed_seconds"],
        "source_timing_segments": copy.deepcopy(real["timing_segments"]),
        "source_cost_already_contains_all_older_ancestors": True}
    receipt = {
        "schema": POLICY+"-paid-source-receipt", "passed": True,
        "source": copy.deepcopy(PINS), "fingerprints": fingerprints,
        "all189_frozen_dependencies_and170_python_sources_match_current_bytes": True,
        "paid_check_counts": [6, 12, 11, 9], "old_checks_executed": 0,
        "old_geometry_J_JVP_scalar_LP_SOC_cone_or_trial_replays": 0,
        "source32_and64_permanently_closed": True,
        "only_latest_original_log_read": True, "earlier_source_log_reads": 0,
        "redirects_without_authorization": redirects,
        "published_actual_note": copy.deepcopy(PUBLISHED_NOTE),
        "paid_final_cost": cost,
        "exact_saved159_retained_from_actual_raw161": True,
        "source_direction_body_array_digest": array_digest(step)}
    ledger.check()
    return {"report": real, "checkpoint": cp, "point": point, "gates": gates,
            "direction": step, "raw161_record": copy.deepcopy(vector),
            "paid_adapter_check": check, "receipt": receipt, "ancestor_cost_receipt": cost}


def prepare(request, output, completed, ledger, *, process_started):
    ledger.check()
    cp, real = completed["checkpoint"], completed["report"]
    args = inherited.previous.old_input_namespace(request, output)
    restored, bindings, tenth, _, _, _ = baseline.growth.prepare_run(
        args, process_started=process_started)
    ledger.check()
    original, _, original_gate, lower, upper, historical_cfg, _ = restored
    coordinate_sha = digest(cp["coordinate_definition"])
    require(coordinate_sha == paid.COORDINATE_SHA, "original coordinate map differs")
    field_request = {
        "source": {"coordinate_definition_sha256": coordinate_sha},
        "fixed_complete_metric_sha256": request["fixed_complete_metric_sha256"],
        "fixed_b0_definition_sha256": request["fixed_b0_definition_sha256"]}
    field, initial, gate, field_receipt = inherited.reconstruct_checkpoint_field(
        original, original_gate, lower, upper, cp, field_request)
    problem = DirectReferenceFiveHeightField(field)
    cfg = copy.deepcopy(cp["configuration"])
    require(digest(problem.identity(initial)) == SOURCE_PHYSICAL_SHA
            and digest(problem.evaluation_definition()) == SOURCE_FIELD_SHA
            and digest(cfg) == SOURCE_CFG_SHA,
            "physical current52/g/b0/direct evaluator/configuration changed")
    radial, theta, grid = baseline.curvature_grid(tenth)
    require(grid == real["full_value_sampling_definition"],
            "original complete sampling definition changed")
    grids = {}
    for label, nt in (("coarse", len(theta)), ("fine", 2*len(theta))):
        rg = RationalRowGrid(label, grid["radial_nodes_exact"], nt)
        require(rg.definition_sha256 == cp["norm_direction_bank_context"]["original_grids"][label]
                and rg.point_count == cp["norm_direction_bank_context"]["original_point_counts"][label],
                "original rational row-ID grid changed: "+label)
        grids[label] = rg
    coarse = inherited.checked_pool(cp["coarse_pool"], grids["coarse"].point_count,
                                    cfg["max_pool_rows"], "coarse")
    fine = inherited.checked_pool(cp["fine_pool"], grids["fine"].point_count,
                                  cfg["max_fine_physical_pool_rows"], "fine")
    gate, gate_receipt = direct_audit.fresh_adapter_gate(
        gate, problem, initial, gate.coordinate_lower, gate.coordinate_upper)
    bounded = problem.original_problem.base
    order = int(bounded.primitive_order)
    require(order == int(bounded.fixed_primitive.order) == 8,
            "original primitive/quadrature identity changed")
    replay = {
        "source_checkpoint": cp, "source_current_point": copy.deepcopy(completed["point"]),
        "source_final_gate_receipts": copy.deepcopy(completed["gates"]),
        "source_paid_receipt": copy.deepcopy(completed["receipt"]),
        "ancestor_cost_receipt": copy.deepcopy(completed["ancestor_cost_receipt"]),
        "source_input_restoration": {
            "all24_original_inputs_loaded_once": True,
            "no_old_developer_geometry_J_JVP_model_solver_or_trial_replay": True,
            "source_configuration_unchanged": True,
            "historical24_configuration_sha256": digest(historical_cfg),
            "field_transfer": field_receipt, "fresh_adapter_gate": gate_receipt,
            "original_primitive_order": order,
            "pool_restoration_without_initialize_or_automatic_expand": True}}
    ledger.check()
    return {"problem": problem, "initial": initial, "gate": gate, "cfg": cfg,
            "radial": radial, "theta": theta, "grid": grid, "row_grids": grids, "order": order,
            "lower": gate.coordinate_lower, "upper": gate.coordinate_upper,
            "coarse_pool": coarse, "fine_pool": fine, "bindings": bindings, "replay": replay}

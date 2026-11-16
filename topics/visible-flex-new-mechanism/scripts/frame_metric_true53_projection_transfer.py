#!/usr/bin/env python3
"""Restore the uniquely paid accepted53 checkpoint; execute no old science."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import json
from pathlib import Path
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
import read_original_actions_log as reader
import frame_metric_paid_cone_vector_audit as paid
import frame_metric_direct_reference_audit as direct_audit
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
POLICY = "same159-true53-complete-grid-maximin-projection-v1"
SOURCE_ACCEPTED_INDEX = 53
SOURCE_PHYSICAL_SHA = "9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e"
SOURCE_CFG_SHA = "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA = "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"
SOURCE_OBJECTIVE_SHA = "fa4757cdc16c284e47cec422bbccea6abfa379e36c456d7bec453559c93b8e77"
SOURCE_BANK_SHA = "233b2e81fdd0ab36f3306d2d901e8708bb103ea34c9c20ef006537d371634527"
SOURCE_LEARNING_SHA = "b076a3436d0b5c2ae4738013314e9b806f7cf90d74712b28fafd2b791ce1ca76"
SOURCE_GLOBAL_SECONDS = 1406.2512530919998
SOURCE_CLOSED_CONE_SECONDS = 968.6757049859999
SOURCE_ORIGINAL_VALUES = 126
PINS = {
    "run_id": "43804573954", "job_id": "133092260804",
    "source_commit": "ab1ba331a1d376d61e6e9f9b7f29f2bb9221a1e2",
    "log_bytes": 19369550,
    "log_sha256": "12cab583514612fa08da7988b4f71aaf9478d019ec313ae5f2a4d06d70b15392",
    "request_payload_bytes": 32512,
    "request_payload_sha256": "4b75275d37b3710f83c885e38d3187e1e4548c7e27e0f77a7ce2906a4e370b5d",
    "prior_payload_bytes": 2777,
    "prior_payload_sha256": "342913c8dea3512af31b92122f5c5ac09b12ce2b204769d797c558dcae25106c",
    "complete_payload_bytes": 3717687,
    "complete_payload_sha256": "9302b47c2845c83707992aad2bcd91cf32dc07b1105a771337c17c9cf23e5023",
    "clock_payload_bytes": 1849,
    "clock_payload_sha256": "9e72ed720c8b05c38647a6da07e1ffb3caf56636ce814ee7eaf58708672e2b95"}
SOURCE_REQUEST = {
    "path": TOPIC+"/computations/request-p32-line-envelope.json",
    "bytes": 44738,
    "sha256": "7b300c90eeb4c4b7c1fefc5b449fd8c80ec8aa836b10324b2e34c9942d3936a4"}
PUBLISHED_NOTE = {
    "path": TOPIC+"/notes/paid-p32-line-envelope-first-actual-and-accepted53-20261116.md",
    "commit": "4efa7511d4501dde25e89a74661226cbf6f129c6",
    "bytes": 28403,
    "sha256": "e9e02036b5ad77f9b755a8184a9301358259fe8e0fc0c09b0f1780ef80ad6b8a"}

def require(value, message):
    if not bool(value):
        raise ValueError(message)


def exact_binary64(values, length):
    require(isinstance(values, list) and len(values) == length
            and all(isinstance(v, str) for v in values), "full exact-vector strings required")
    exact = [Q(v) for v in values]
    array = np.asarray([float(v) for v in exact], float)
    require(np.all(np.isfinite(array)) and all(
        Q.from_float(float(v)) == q for v, q in zip(array, exact)),
        "selected vector is not exactly binary64 recoverable")
    return array


def read_source(request, ledger):
    ledger.check()
    require(request["source"] == PINS and request["source_request"] == SOURCE_REQUEST
            and request["published_actual_note"] == PUBLISHED_NOTE,
            "the published accepted53 source is the only authorized checkpoint")
    for meta in (SOURCE_REQUEST, PUBLISHED_NOTE):
        raw = Path(meta["path"]).read_bytes()
        require(len(raw) == meta["bytes"] and reader.digest(raw) == meta["sha256"],
                "source request or actual-note fingerprint changed")
    old_request = json.loads(Path(SOURCE_REQUEST["path"]).read_bytes())
    require(request["original_input_arguments"] == old_request["original_input_arguments"]
            and len(request["original_input_arguments"]) == 98,
            "all original24-input arguments must remain unchanged")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+PINS["run_id"])
    job = api.api_json("/actions/jobs/"+PINS["job_id"])
    require(str(run["id"]) == str(job["run_id"]) == PINS["run_id"]
            and str(job["id"]) == PINS["job_id"]
            and run["head_sha"] == job["head_sha"] == PINS["source_commit"]
            and run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "success",
            "paid run/job/source/completion differs")
    raw, redirects = api.job_log(PINS["job_id"])
    require(len(raw) == PINS["log_bytes"] and reader.digest(raw) == PINS["log_sha256"],
            "paid53 original research log differs")
    # Do not parse or reuse the old52 direction cache. Only these four paid tags
    # are needed to restore53 and its final authoritative ancestor cost.
    fields = (("REQUEST", "request"), ("PRIOR_WORK_REUSED", "prior"),
              ("COMPLETE", "complete"), ("FINAL_CLOCK", "clock"))
    records = inherited.tagged_records(raw, tuple("P32_LINE_"+name for name, _ in fields))
    values, fingerprints = {}, []
    for name, field in fields:
        value, receipt = paid.tagged_value(
            records, "P32_LINE_"+name,
            PINS[field+"_payload_bytes"], PINS[field+"_payload_sha256"])
        values[name] = value
        fingerprints.append(receipt)
    actual_request, prior, real, clock = (
        values[name] for name in ("REQUEST", "PRIOR_WORK_REUSED", "COMPLETE", "FINAL_CLOCK"))
    manifest = actual_request["source_sha256"]
    old_py = {Path(path).name: sha for path, sha in manifest.items() if path.endswith(".py")}
    require(actual_request["source_commit"] == PINS["source_commit"]
            and actual_request["request_bytes"] == SOURCE_REQUEST["bytes"]
            and actual_request["request_sha256"] == SOURCE_REQUEST["sha256"]
            and manifest == old_request["source_sha256"] and len(manifest) == 200
            and len(old_py) == 176 and real["source_files_sha256"] == old_py,
            "paid200-source/176-Python closure differs")
    for path, sha in manifest.items():
        require(request["source_sha256"].get(path) == sha
                and reader.digest(Path(path).read_bytes()) == sha,
                "a paid source changed: "+path)
    require(prior["passed"] is True
            and prior["paid_check_counts"] == [6, 12, 11, 9]
            and prior["old_checks_executed"] == 0
            and prior["old_geometry_J_JVP_scalar_LP_SOC_cone_or_trial_replays"] == 0
            and prior["source32_and64_permanently_closed"] is True,
            "transitive paid source receipt differs")
    expected_status = "complete-two-grid-paid-p32-first-jet-scalar-line-audit"
    require(real["schema"] == "same159-paid-p32-first-jet-scalar-envelope-v1-audit"
            and real["status"] == expected_status
            and clock["status_at_final_emit"] == expected_status
            and clock["scope_exhausted"] is False
            and clock["sampled_after_all_large_cache_and_complete_serialization_and_emit"] is True
            and real["github_sha"] == PINS["source_commit"]
            and str(real["github_run_id"]) == PINS["run_id"]
            and real["github_repository"] == REPO and real["old_checks_executed"] == 0,
            "completed accepted53 audit or final clock differs")
    final = clock["ledger"]
    require(final["total_ancestor_plus_new_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
            and final["total_source_plus_new_full_values"] == SOURCE_ORIGINAL_VALUES
            and final["closed_cone_task_scientific_seconds_separate_not_added_twice"]
                == SOURCE_CLOSED_CONE_SECONDS
            and final["new_actual_full_values"] == 2
            and final["new_actual_trial_points"] == 1
            and final["new_complete_envelope_queries"] == 62
            and final["old_HiGHS_calls_closed"] == 64
            and final["old_cone_calls_closed"] == 32,
            "final paid53 clocks/126values/closed solver counts differ")
    cp = real["future_scalar_line_checkpoint"]
    point = real["selected_two_grid_physical_point"]
    require(point == cp["selected_two_grid_physical_point"]
            and point["accepted_index"] == cp["selected_accepted_index"] == SOURCE_ACCEPTED_INDEX
            and point["physical_state_sha256"] == cp["selected_physical_state_sha256"]
                == SOURCE_PHYSICAL_SHA
            and point["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and point["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"]
            and digest(cp["configuration"]) == SOURCE_CFG_SHA
            and cp["configuration"] == real["configuration"],
            "actual53 vectors/configuration/point differ")
    exact_binary64(cp["selected_final159_binary64_exact"], 159)
    require(len(cp["selected_final163_physical_exact"]) == 163
            and all(isinstance(s, str) for s in cp["selected_final163_physical_exact"]),
            "full original physical163 exact vector missing")
    for key, sha_key in (
            ("objective_evaluation_definition", "objective_evaluation_sha256"),
            ("ordinary_field_evaluation_definition", "ordinary_field_evaluation_sha256"),
            ("factorization_definition", "factorization_definition_sha256")):
        require(digest(cp[key]) == cp[sha_key], "paid definition hash differs: "+key)
    require(cp["objective_evaluation_sha256"] == SOURCE_OBJECTIVE_SHA
            and cp["ordinary_field_evaluation_sha256"] == SOURCE_FIELD_SHA
            and cp["norm_direction_bank_state_sha256"] == SOURCE_BANK_SHA
            and len(cp["norm_direction_bank_entries"]) == 512
            and len(cp["all_retained_supplemental_normals"]) == 8
            and (len(cp["coarse_pool"]), len(cp["fine_pool"]),
                 cp["coarse_pool_version"], cp["fine_pool_version"]) == (4448, 4549, 13, 14)
            and all(row in cp["fine_pool"] for row in
                    (86919, 87033, 87303, 87417, 159001, 210297))
            and cp["terminal_trust"] == .00025
            and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
            "actual53 pools/information state differs")
    learning = cp["curvature_defect_guard_learning_checkpoint"]
    require(learning["state_sha256"] == SOURCE_LEARNING_SHA
            and learning["pending_event_indices"] == []
            and len(learning["events"]) == 62 and len(learning["commits"]) == 61,
            "paid curvature-learning state differs")
    gates = {}
    for label, key in (("coarse", "final_full_grid_constraints"),
                       ("fine", "final_doubled_constraints")):
        decision = real[key]
        require(len(decision["actual_gate_booleans"]) == 14
                and all(v is True for v in decision["actual_gate_booleans"].values())
                and decision["direct_max_eta"] == point[label]["direct_max_eta"],
                "paid53 full14-gate receipt differs: "+label)
        gates[label] = copy.deepcopy(decision)
    stage = real["p32_scalar_line_stage"]
    accepted = [t for t in stage["trials"] if t.get("accepted_as_next_iterate") is True]
    require(stage["new_acceptances"] == 1 and len(accepted) == 1
            and accepted[0]["accepted_index"] == SOURCE_ACCEPTED_INDEX
            and accepted[0]["physical_state_sha256"] == SOURCE_PHYSICAL_SHA
            and accepted[0]["exact_binary64_independent_coordinates"]
                == cp["selected_final159_binary64_exact"]
            and accepted[0]["exact_original_physical_coefficients"]
                == cp["selected_final163_physical_exact"]
            and accepted[0]["original_exact163_box"]["exact_original_box_pass"] is True,
            "one native accepted53 trial must match the checkpoint")
    cost = {
        "ancestor_final_original_scientific_seconds": SOURCE_GLOBAL_SECONDS,
        "source_original_full_values": SOURCE_ORIGINAL_VALUES,
        "closed_cone_task_scientific_seconds_not_added_twice": SOURCE_CLOSED_CONE_SECONDS,
        "closed_HiGHS_calls": 64, "closed_cone_calls": 32,
        "paid_p32_new_scientific_seconds": final["new_scientific_seconds"],
        "paid_p32_UTC_job_seconds_separate_from_monotonic_science": 530,
        "paid_p32_clock": copy.deepcopy(clock),
        "earlier_checkpoint_clocks_not_used_as_final_ancestor_cost": True,
        "source_cost_already_contains_all_older_ancestors": True}
    receipt = {
        "schema": POLICY+"-paid-source-receipt", "passed": True,
        "source": copy.deepcopy(PINS), "fingerprints": fingerprints,
        "all200_paid_dependencies_and176_python_sources_match_current_bytes": True,
        "paid_check_counts": [6, 12, 11, 9], "paid_scalar_case_count": 3,
        "old_checks_executed": 0,
        "old_geometry_J_JVP_scalar_LP_SOC_cone_or_trial_replays": 0,
        "source32_and64_permanently_closed": True,
        "only_latest_original_research_log_read": True, "earlier_source_log_reads": 0,
        "old52_line_cache_not_decoded_or_reused": True,
        "redirects_without_authorization": redirects,
        "published_actual_note": copy.deepcopy(PUBLISHED_NOTE),
        "paid_final_cost": cost,
        "complete_current53_vectors_pools_bank_learning_from_original_checkpoint": True}
    ledger.check()
    return {"report": real, "checkpoint": cp, "point": point, "gates": gates,
            "receipt": receipt, "ancestor_cost_receipt": cost,
            "source_final_clock": clock}


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
            "physical current53/g/b0/direct evaluator/configuration changed")
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
    return {"problem": problem, "initial": initial, "initial159": initial, "gate": gate, "cfg": cfg,
            "radial": radial, "theta": theta, "grid": grid, "row_grids": grids, "order": order,
            "lower": gate.coordinate_lower, "upper": gate.coordinate_upper,
            "coarse_pool": coarse, "fine_pool": fine, "bindings": bindings, "replay": replay}

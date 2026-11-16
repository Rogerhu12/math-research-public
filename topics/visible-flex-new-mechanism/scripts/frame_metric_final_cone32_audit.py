#!/usr/bin/env python3
"""One current-model cone32 continuation; all old checks/solves are receipts."""
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
import frame_metric_paid_cone_vector_audit as paid
import frame_metric_finite_cone_audit as frozen
import frame_metric_direct_reference_audit as direct_audit
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
import read_original_actions_log as reader
from frame_metric_finite_cone_epoch import (
    POLICY, LIMITS, SETTINGS, CANDIDATE_STATUSES, SOURCE_VALUES, SOURCE_LEGACY_COUNTS)
from frame_metric_final_cone32 import (
    CONTINUATION_POLICY, SOURCE_CONE_SECONDS, SOURCE_GLOBAL_SECONDS,
    SOURCE_TOTAL_VALUES, SOURCE_CONE_CALLS, SOURCE_ACCEPTED_INDEX,
    SOURCE_PHYSICAL_SHA, SOURCE_AFFINE_SHA, SOURCE_VALUE_ONLY_SHA,
    SOURCE_BANK_SHA, SOURCE_LEARNING_SHA,
    ContinuedCone32Clock, FinalCone32Objective, continuation_definition,
    require, finite_number)
from frame_metric_final_cone32_recovery import run_final_cone32_recovery

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
SCHEMA = CONTINUATION_POLICY+"-audit"
STAGE = "final_cone32_stage"
COMPLETE = "complete-two-grid-final-cone32-audit"
TAG = "FINAL_CONE32_"
NEW_SOURCES = ("frame_metric_final_cone32.py",
               "frame_metric_final_cone32_recovery.py",
               "frame_metric_final_cone32_audit.py")
PINS = {
    "run_id": "43798128882", "job_id": "133071559203",
    "source_commit": "b8577eaaa8d8327495db13bd1f684348ede6cb06",
    "log_bytes": 3765299,
    "log_sha256": "9170360919ba81f563ef5a441069c6d65863c55591a9ab218193bf2833a42f51",
    "request_payload_bytes": 28557,
    "request_payload_sha256": "51c1e9a40fc66bc65e760effbae577c14dc34fcf3af3535b290444694e4c4b3b",
    "development_payload_bytes": 1356,
    "development_payload_sha256": "5ebc93d61bff48ea592a612d1f34fc2b7e4c89eb8cb9f74c3dc5302a3de9b4fc",
    "prior_payload_bytes": 2962,
    "prior_payload_sha256": "4d19b31896278f1984ee1a2d39ef12c460fd4d1ba8fa17a4c14c65dec36eefa1",
    "complete_payload_bytes": 3505269,
    "complete_payload_sha256": "df20419f4e3051848d1b6dbb63ff3f0b2b31ea1f4de528108176f951b0f76731"}
SOURCE_REQUEST = {
    "path": TOPIC+"/computations/request-paid-cone-vector.json", "bytes": 39813,
    "sha256": "2a75f7668fba356feb300fe618a08adabe9973f36e90504f56208211eb3cf69e"}
PUBLISHED_NOTE = {
    "path": TOPIC+"/notes/paid-MaxTime-vector-first-actual-and-new-soft-row-20261116.md",
    "commit": "c99a38e230759d407c5eb2b1afb9ed62cf9d5a06", "bytes": 16823,
    "sha256": "4280b80ca63bd55d4476a0082ae43321b4ea5139ce6aef94c25929da29cbbe31"}


def implementation_hashes():
    result = paid.implementation_hashes()
    folder = Path(__file__).parent
    for name in NEW_SOURCES:
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def emit(suffix, value):
    print(TAG+suffix+" "+reader.encoded(value).decode("utf-8"), flush=True)


def read_source(request, clock):
    clock.check()
    require(request["source"] == PINS and request["source_request"] == SOURCE_REQUEST
            and request["published_actual_note"] == PUBLISHED_NOTE,
            "only the completed paid-vector source is authorized")
    for meta in (SOURCE_REQUEST, PUBLISHED_NOTE):
        raw = Path(meta["path"]).read_bytes()
        require(len(raw) == meta["bytes"] and reader.digest(raw) == meta["sha256"],
                "published source request or human-note fingerprint differs")
    old_request = json.loads(Path(SOURCE_REQUEST["path"]).read_bytes())
    require(request["original_input_arguments"] == old_request["original_input_arguments"]
            and len(request["original_input_arguments"]) == 98,
            "all original 24-input CLI parameters must stay unchanged")
    api = reader.GitHubReader(REPO)
    run, job = api.api_json("/actions/runs/"+PINS["run_id"]), api.api_json("/actions/jobs/"+PINS["job_id"])
    require(str(run["id"]) == PINS["run_id"] and str(job["id"]) == PINS["job_id"]
            and str(job["run_id"]) == PINS["run_id"]
            and run["head_sha"] == job["head_sha"] == PINS["source_commit"]
            and run["status"] == job["status"] == "completed"
            and run["conclusion"] == job["conclusion"] == "success",
            "source run/job/head/link/conclusion differs")
    raw, redirects = api.job_log(PINS["job_id"])
    require(len(raw) == PINS["log_bytes"] and reader.digest(raw) == PINS["log_sha256"],
            "paid-vector original log differs")
    names = ("REQUEST", "DEVELOPMENT", "PRIOR_WORK_REUSED", "COMPLETE")
    tags = tuple("PAID_CONE_VECTOR_"+x for x in names)
    records = inherited.tagged_records(raw, tags)
    fields = ("request", "development", "prior", "complete")
    values, fingerprints = {}, []
    for name, field in zip(names, fields):
        value, receipt = paid.tagged_value(
            records, "PAID_CONE_VECTOR_"+name,
            PINS[field+"_payload_bytes"], PINS[field+"_payload_sha256"])
        values[name] = value
        fingerprints.append(receipt)
    requested, dev, prior, real = (values[x] for x in names)
    manifest = requested["source_sha256"]
    old_python = {Path(path).name: sha for path, sha in manifest.items() if path.endswith(".py")}
    require(requested["source_commit"] == PINS["source_commit"]
            and requested["request_bytes"] == SOURCE_REQUEST["bytes"]
            and requested["request_sha256"] == SOURCE_REQUEST["sha256"]
            and manifest == old_request["source_sha256"] and len(manifest) == 182
            and len(old_python) == 167 and real["source_files_sha256"] == old_python,
            "actual paid182/167 source closure differs")
    for path, sha in manifest.items():
        require(request["source_sha256"].get(path) == sha
                and reader.digest(Path(path).read_bytes()) == sha,
                "a frozen paid dependency changed: "+path)
    require(dev["all_passed"] is True and dev["executed_check_count"] == 6
            and dev["group_count"] == 2 and [len(g["checks"]) for g in dev["groups"]] == [3, 3]
            and all(g["passed"] is True and all(v is True for v in g["checks"].values()) for g in dev["groups"])
            and dev["execution"] == {
                "actual_geometry_calls": 0, "new_stub_value_calls": 6,
                "original_developer_suites_executed": 0,
                "parameter_J_or_directional_JVP_calls": 0, "research_or_tiny_solver_calls": 0}
            and dev["paid12_cone_11_terminal_and9_geometry_checks_are_receipts_only"] is True,
            "paid six checks or transitive execution boundary differs")
    require(prior["passed"] is True and prior["all_frozen_sources_match_current_bytes"] is True
            and prior["paid12_cone_development_checks"] == 12
            and prior["transitive_paid11_and9"] == [11, 9]
            and prior["all_old_developer_solver_geometry_J_JVP_trial_replays"] == 0,
            "paid twelve/eleven/nine transitive receipt differs")
    require(real["schema"] == paid.SCHEMA and real["status"] == paid.COMPLETE
            and real["github_sha"] == PINS["source_commit"]
            and str(real["github_run_id"]) == PINS["run_id"]
            and real["github_repository"] == REPO,
            "latest completed audit identity differs")
    stage, cp = real[paid.STAGE], real["future_value_only_checkpoint"]
    require(stage["status"] == "paid-vector-new-rows-stop-fixed-direction-last-accepted-retained"
            and stage["error"] is None and stage["new_acceptances"] == 0
            and len(stage["trials"]) == 3
            and [t["alpha_exact"] for t in stage["trials"]] == ["1", "1/2", "1/4"]
            and all(t["accepted_as_next_iterate"] is False for t in stage["trials"])
            and stage["trials"][-1]["new_fine_rows"] == 1
            and stage["trials"][-1]["added_fine_rows"]["added_row_indices"] == [159001],
            "actual failed-direction learning boundary differs")
    require(real["continued_science_account"]["cumulative_cone_task_scientific_seconds"] == SOURCE_CONE_SECONDS
            and real["continued_science_account"]["cumulative_original_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
            and real["final_value_account"]["cumulative_original_values"] == SOURCE_TOTAL_VALUES
            and real["final_value_account"]["cumulative_cone_task_values"] == 60
            and real["final_value_account"]["coarse_cumulative"] == real["final_value_account"]["fine_cumulative"] == 61
            and real["paid_finite_cone_calls_unchanged"] == SOURCE_CONE_CALLS
            and real["remaining_cone_slot_unconsumed"] == 1
            and real["closed_original_HiGHS_counts"] == SOURCE_LEGACY_COUNTS,
            "authoritative latest source clocks/values/solver accounts differ")
    require(real["zero_derivative_or_solver_execution"] == {
        "affine_factories": 0, "full_directional_JVP": 0,
        "new_LP_SOC_or_cone_calls": 0, "new_solver_return_vectors": 0,
        "selected_J_batches": 0, "selected_J_refreshes": 0},
        "source actual-only scope differs")
    point = stage["selected_two_grid_physical_point"]
    require(point == cp["selected_two_grid_physical_point"]
            and point["accepted_index"] == cp["selected_accepted_index"] == SOURCE_ACCEPTED_INDEX
            and point["physical_state_sha256"] == cp["selected_physical_state_sha256"] == SOURCE_PHYSICAL_SHA
            and point["exact_binary64_independent_coordinates"] == cp["selected_final159_binary64_exact"]
            and point["exact_original_physical_coefficients"] == cp["selected_final163_physical_exact"]
            and cp["configuration"] == real["configuration"]
            and digest(cp["configuration"]) == paid.SOURCE_CFG_SHA,
            "exact current52/configuration differs")
    for key, sha_key in (
        ("objective_evaluation_definition", "objective_evaluation_sha256"),
        ("source_affine_objective_evaluation_definition", "source_affine_objective_evaluation_sha256"),
        ("ordinary_field_evaluation_definition", "ordinary_field_evaluation_sha256"),
        ("factorization_definition", "factorization_definition_sha256")):
        require(digest(cp[key]) == cp[sha_key], "source definition fingerprint differs: "+key)
    require(cp["objective_evaluation_sha256"] == SOURCE_VALUE_ONLY_SHA
            and cp["source_affine_objective_evaluation_sha256"] == SOURCE_AFFINE_SHA
            and cp["ordinary_field_evaluation_sha256"] == paid.SOURCE_FIELD_SHA
            and cp["norm_direction_bank_state_sha256"] == SOURCE_BANK_SHA
            and len(cp["norm_direction_bank_entries"]) == 512
            and len(cp["all_retained_supplemental_normals"]) == 8,
            "same field/affine method/passive information state required")
    memory = cp["curvature_defect_guard_learning_checkpoint"]
    require(memory["state_sha256"] == SOURCE_LEARNING_SHA and memory["pending_event_indices"] == []
            and len(memory["events"]) == 62 and len(memory["commits"]) == 61
            and memory["coefficients"] == {"coarse": 57.187653029922444, "fine": 67.42701956990882}
            and [len(cp["coarse_pool"]), len(cp["fine_pool"])] == [4448, 4544]
            and [cp["coarse_pool_version"], cp["fine_pool_version"]] == [13, 13]
            and 159001 in cp["fine_pool"] and cp["terminal_trust"] == .00025
            and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
            "complete latest learning/pools/controller differ")
    gates = {}
    for label, key in (("coarse", "final_full_grid_constraints"), ("fine", "final_doubled_constraints")):
        value = real[key]
        require(len(value["actual_gate_booleans"]) == 14
                and all(x is True for x in value["actual_gate_booleans"].values())
                and value["direct_max_eta"] == point[label]["direct_max_eta"],
                "same point52 paid complete gates required: "+label)
        gates[label] = copy.deepcopy(value)
    cost = {
        "final_authoritative_cone_science_seconds": SOURCE_CONE_SECONDS,
        "final_authoritative_global_science_seconds": SOURCE_GLOBAL_SECONDS,
        "latest_actual_values": SOURCE_TOTAL_VALUES,
        "closed_HiGHS_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
        "paid_cone_calls": SOURCE_CONE_CALLS,
        "latest_process_seconds": real["process_total_elapsed_seconds"],
        "latest_timing_segments": copy.deepcopy(real["timing_segments"]),
        "earlier_ancestor_receipt": copy.deepcopy(cp["ancestor_cost_receipt"]),
        "source_clock_offsets_are_cumulative_not_resummed": True}
    receipt = {
        "schema": CONTINUATION_POLICY+"-paid-source-receipt", "passed": True,
        "source": copy.deepcopy(PINS), "fingerprints": fingerprints,
        "frozen_source_bindings": 182, "frozen_Python_sources": 167,
        "all_frozen_sources_match_current_bytes": True,
        "paid_check_counts": [6, 12, 11, 9], "new_checks_executed": 0,
        "old_developer_solver_geometry_J_JVP_trial_replays": 0,
        "only_latest_original_log_read": True, "earlier_logs_downloaded": 0,
        "source_MaxTime31_and_three_failed_real_trials_not_reexecuted": True,
        "redirects_without_authorization": redirects,
        "published_actual_note": copy.deepcopy(PUBLISHED_NOTE),
        "paid_final_cost": cost}
    clock.check()
    return {"report": real, "checkpoint": cp, "point": point,
            "gates": gates, "receipt": receipt, "ancestor_cost_receipt": cost}


def prepare(request, output, completed, clock):
    clock.check()
    cp, real = completed["checkpoint"], completed["report"]
    args = inherited.previous.old_input_namespace(request, output)
    restored, bindings, tenth, _, _, _ = baseline.growth.prepare_run(
        args, process_started=PROCESS_STARTED)
    clock.check()
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
            and digest(problem.evaluation_definition()) == paid.SOURCE_FIELD_SHA
            and digest(cfg) == paid.SOURCE_CFG_SHA,
            "physical52/original g/b0/direct evaluator/cfg changed")
    radial, theta, grid = baseline.curvature_grid(tenth)
    require(grid == real["full_value_sampling_definition"], "original complete sampling grid changed")
    for label, nt in (("coarse", len(theta)), ("fine", 2*len(theta))):
        rg = RationalRowGrid(label, grid["radial_nodes_exact"], nt)
        require(rg.definition_sha256 == cp["norm_direction_bank_context"]["original_grids"][label],
                "original rational row-ID grid changed: "+label)
    counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    require(counts == cp["norm_direction_bank_context"]["original_point_counts"],
            "original grid point counts differ")
    coarse = inherited.checked_pool(cp["coarse_pool"], counts["coarse"], cfg["max_pool_rows"], "coarse")
    fine = inherited.checked_pool(cp["fine_pool"], counts["fine"], cfg["max_fine_physical_pool_rows"], "fine")
    gate, gate_receipt = direct_audit.fresh_adapter_gate(
        gate, problem, initial, gate.coordinate_lower, gate.coordinate_upper)
    bounded = problem.original_problem.base
    order = int(bounded.primitive_order)
    require(order == int(bounded.fixed_primitive.order) == 8, "original primitive orders changed")
    latest_value_cost = {
        "component_timer_totals_not_exported_by_the_value_only_objective": True,
        "value_call_events": [
            {k: copy.deepcopy(v) for k, v in event.items() if k != "direct_reference_timing_after_call"}
            for event in real["value_call_events"]],
        "adapter_geometry_seconds": real["direct_reference_geometry_timing"]["geometry_seconds"],
        "science_and_process_fees": copy.deepcopy(completed["ancestor_cost_receipt"]),
        "wrapper_elapsed_not_substituted_for_old_internal_component_counters": True}
    replay = {
        "source_checkpoint": cp, "source_current_point": copy.deepcopy(completed["point"]),
        "identities": {"field": cp["ordinary_field_evaluation_sha256"],
                      "factorization": cp["factorization_definition_sha256"],
                      "configuration": digest(cfg), "physical": SOURCE_PHYSICAL_SHA},
        "source_snapshot_scalar_counters": copy.deepcopy(real["source_snapshot_scalar_counters"]),
        "source_value_only_cost_receipt": latest_value_cost,
        "source_final_gate_receipts": copy.deepcopy(completed["gates"]),
        "paid_initial_decisions": copy.deepcopy(completed["gates"]),
        "ancestor_cost_receipt": copy.deepcopy(completed["ancestor_cost_receipt"]),
        "paid_source_receipt": copy.deepcopy(completed["receipt"]),
        "controller_continuation": {
            "trust_binary64_exact": str(Q.from_float(cp["terminal_trust"])),
            "trust_evaluated": cp["terminal_trust"],
            "success_streak": cp["terminal_success_streak"],
            "covered_ordinary_success_streak": cp["terminal_covered_ordinary_growth_streak"]},
        "source_completed_log_transfer": {
            "same_exact_reference163_current159_physical163": True,
            "same_original_g_b0_coordinate_and_two_grids": True,
            "all24_inputs_loaded_once": True, "old_values_J_JVP_models_or_solver_replays": 0,
            "field_transfer": field_receipt, "fresh_adapter_gate": gate_receipt,
            "original_order": order, "source_configuration_unchanged": True,
            "historical24_configuration_sha256": digest(historical_cfg),
            "source_pool_counts": [4448, 4544], "source_pool_versions": [13, 13],
            "no_pool_initialize_or_automatic_expand": True}}
    clock.check()
    return {"problem": problem, "initial": initial, "gate": gate, "cfg": cfg,
            "radial": radial, "theta": theta, "grid": grid, "order": order,
            "lower": gate.coordinate_lower, "upper": gate.coordinate_upper,
            "coarse_pool": coarse, "fine_pool": fine, "bindings": bindings, "replay": replay}


def complete_capture_evidence(models):
    finite = [e for m in models for e in m.get("linear_program", {}).get("cone_calls", [])
              if e.get("finite_original161_vector") is True]
    def present(event):
        rec = event.get("actual_complete_solver_vector_record", {})
        x, p = rec.get("exact_binary64_original_solver_variables161"), rec.get("exact_binary64_independent_step159")
        return (isinstance(x, list) and len(x) == 161 and isinstance(p, list) and len(p) == 159
                and all(isinstance(v, str) for v in x+p)
                and rec.get("exact_binary64_original_solver_rho") == x[159]
                and rec.get("exact_binary64_original_solver_norm_auxiliary") == x[160])
    return {"finite_return_count": len(finite),
            "full161_and_scaled159_present_count": sum(present(e) for e in finite),
            "all_finite_returns_saved_in_full": all(present(e) for e in finite) if finite else None}


def semantic_model(model):
    result = frozen.semantic_model(model)
    evidence = complete_capture_evidence([model])
    result["complete161_capture_evidence"] = evidence
    result["serialization_scope"]["all_actual_finite_solver161_vectors_retained"] = evidence["all_finite_returns_saved_in_full"]
    return result


def summary(report):
    result = {k: copy.deepcopy(v) for k, v in report.items()
              if k not in (STAGE, "exact_input_storage")}
    result["exact_input_storage_metadata"] = frozen.metadata(report.get("exact_input_storage", {}))
    stage = report.get(STAGE, {})
    result[STAGE] = {k: copy.deepcopy(v) for k, v in stage.items()
                    if k not in ("checkpoint", "solver", "complete_original_grid_oracle_progress",
                                 "curvature_defect_guard_learning_checkpoint",
                                 "inherited_guard_observation_full_history", "cross_center_norm_memory")}
    solver, snapshot = stage.get("solver", {}), stage.get("checkpoint", {})
    result[STAGE]["solver"] = {k: copy.deepcopy(v) for k, v in solver.items() if k != "models"}
    models = solver.get("models", [])
    result[STAGE]["model_count"] = len(models)
    result[STAGE]["MODEL_record_metadata"] = [
        dict(number=m["number"], **frozen.metadata(semantic_model(m))) for m in models]
    result[STAGE]["selected_two_grid_physical_point"] = copy.deepcopy(
        snapshot.get("selected_two_grid_physical_point"))
    result[STAGE]["snapshot_scalar_counters"] = {
        k: copy.deepcopy(snapshot[k]) for k in (
            "initialization_elapsed_seconds", "optimization_elapsed_seconds",
            "value_geometry_seconds", "total_full_value_physical_evaluations",
            "coarse_physical_evaluations", "fine_physical_evaluations",
            "doubled_angle_value_seconds", "component_timer_scope") if k in snapshot}
    result["factorized_selected_J_execution"] = copy.deepcopy(
        snapshot.get("selected_row_factorization_statistics"))
    result["complete_original_grid_oracle_progress"] = [
        {k: (frozen.metadata(v) if k in ("binding", "direction_events", "new_original_row_J_events")
             else copy.deepcopy(v)) for k, v in item.items()}
        for item in stage.get("complete_original_grid_oracle_progress", [])]
    result["complete161_capture_evidence"] = complete_capture_evidence(models)
    result["serialization_scope"] = {
        "MODEL_policy": "retain actual161, p159, rho, norm and actual trial159/163 without filtering",
        "actual_vector_presence": copy.deepcopy(result["complete161_capture_evidence"]),
        "no_global_vector_length_filter": True,
        "no_dense_A_J_or_repository_payload_output": True}
    return result


def save_report(output, report, clock):
    report["process_total_elapsed_seconds"] = time.monotonic()-PROCESS_STARTED
    report["continued_science_account"] = clock.report()
    report["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    atomic_save(output, report)
    atomic_save(Path(output).with_name("final-cone32-audit-summary.json"), summary(report))


def final_receipts(stage, point, replay):
    if point["accepted_index"] == 52:
        require(point["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
                "unchanged accepted52 has another physical identity")
        return (copy.deepcopy(replay["source_final_gate_receipts"]["coarse"]),
                copy.deepcopy(replay["source_final_gate_receipts"]["fine"]),
                {"kind": "unchanged52-original-two-grid-actual-receipts",
                 "accepted_index": 52, "new_restoration_receipts_separately_recorded": True})
    found = [(m, t) for m in stage["solver"]["models"] for t in m.get("trials", [])
             if t.get("accepted_as_next_iterate") is True and t.get("accepted_index") == point["accepted_index"]
             and t.get("physical_state_sha256") == point["physical_state_sha256"]]
    require(len(found) == 1 and point["accepted_index"] == 53, "one actual new accepted trial required")
    model, trial = found[0]
    return (copy.deepcopy(trial["coarse_decision"]), copy.deepcopy(trial["fine_decision"]),
            {"kind": "cone32-new-actual-two-grid-trial", "accepted_index": 53, "model_number": model["number"]})


def run_audit(prepared, completed, output, clock, report):
    problem, initial, gate, cfg = (prepared[k] for k in ("problem", "initial", "gate", "cfg"))
    replay = prepared["replay"]
    report.update(
        status="cone32-objective-not-yet-constructed",
        configuration=copy.deepcopy(cfg), exact_input_storage=prepared["bindings"],
        source_transfer=copy.deepcopy(replay["source_completed_log_transfer"]),
        source_snapshot_component_counters=copy.deepcopy(replay["source_snapshot_scalar_counters"]),
        latest_value_only_cost_receipt=copy.deepcopy(replay["source_value_only_cost_receipt"]),
        full_value_sampling_definition=copy.deepcopy(prepared["grid"]),
        source_current_point=copy.deepcopy(replay["source_current_point"]),
        original_method_policy=POLICY, continuation_definition=continuation_definition())
    objective = None
    ctor_started = time.monotonic()
    try:
        objective = FinalCone32Objective(
            problem, gate, prepared["radial"], prepared["theta"], prepared["order"],
            prepared["lower"], prepared["upper"], cfg=cfg, checkpoint=None,
            radial_nodes_exact=prepared["grid"]["radial_nodes_exact"], replay=replay,
            continuation_clock=clock, continuation_policy=CONTINUATION_POLICY,
            coarse_pool=prepared["coarse_pool"], fine_pool=prepared["fine_pool"])
        report["timing_segments"]["constructor_seconds"] = time.monotonic()-ctor_started
        report["actual_definition_hashes"] = {
            "source_value_only_objective": SOURCE_VALUE_ONLY_SHA,
            "restored_same_affine_objective": objective.evaluation_sha256,
            "same_ordinary_field": objective.factorized.ordinary_evaluation_sha256,
            "same_factorizer": objective.factorized.definition_sha256,
            "same_configuration": digest(cfg)}
        began = time.monotonic()
        stage = run_final_cone32_recovery(
            objective, initial, restored_controller=replay["controller_continuation"])
        report[STAGE] = stage
        report["timing_segments"]["same_process_restore_J_cone32_and_actual_trials_seconds"] = time.monotonic()-began
        point = stage["checkpoint"]["selected_two_grid_physical_point"]
        final = exact_vector(point["exact_binary64_independent_coordinates"], 159)
        require(np.array_equal(final, np.asarray(point["independent_coordinates_binary64"], float))
                and [str(x) for x in problem.coordinates.physical_exact(final)] ==
                    point["exact_original_physical_coefficients"]
                and digest(problem.identity(final)) == point["physical_state_sha256"],
                "final exact159/physical163 identity changed")
        box = problem.coordinates.exact_box_decision(final, gate.original_lower, gate.original_upper)
        require(box["exact_original_box_pass"] is True, "final exact original163 box failed")
        copied, copied_state = problem.frozen_metric_copy(final)
        require(copied is problem and copied_state.tobytes() == final.tobytes()
                and copied.identity(copied_state) == problem.identity(final)
                and copied.metric_model(copied_state) == problem.metric_model(initial)
                and copied.height_base_definition == problem.height_base_definition,
                "frozen original g/b0/anchor/map changed")
        coarse, fine, owner = final_receipts(stage, point, replay)
        flags = {label: d["actual_gate_booleans"] for label, d in (("coarse", coarse), ("fine", fine))}
        require(all(len(v) == 14 and all(x is True for x in v.values()) for v in flags.values())
                and all(d["direct_max_eta"] == point[label]["direct_max_eta"]
                        for label, d in (("coarse", coarse), ("fine", fine))),
                "all final14 gates and true scalar identity required")
        report["final_selection_validation"] = {
            "accepted_index": point["accepted_index"],
            "both_grid_maximum_eta": max(coarse["direct_max_eta"], fine["direct_max_eta"]),
            "both_grid_maximum_curvature": max(coarse["direct_maximum_absolute_principal_curvature"],
                                                fine["direct_maximum_absolute_principal_curvature"]),
            "source_eta": replay["source_current_point"]["maximum_eta_on_both_grids"],
            "actual_eta_decrease": replay["source_current_point"]["maximum_eta_on_both_grids"]-point["maximum_eta_on_both_grids"],
            "original14_gates_and_exact_box_pass": True,
            "new_target_qualified_on_both_grids": point["new_metric_target_qualified_on_both_grids"],
            "new_independent_final_value_calls": 0}
        report["final_full_grid_constraints"], report["final_doubled_constraints"] = coarse, fine
        report["final_actual_gate_booleans"], report["selected_gate_receipt_source"] = flags, owner
        report["final_exact_box"] = box
        cp = frozen.future_checkpoint(objective, problem, point, stage)
        cp.pop("current_source_point27_plus_new_acceptances_scope", None)
        cp["current_source52_plus_at_most_one_true_cone32_acceptance"] = True
        cp["cone32_continuation"] = {
            "source": copy.deepcopy(PINS), "source_value_only_objective": SOURCE_VALUE_ONLY_SHA,
            "current_complete161_capture_evidence": complete_capture_evidence(stage["solver"]["models"]),
            "source_failed_MaxTime_direction_not_replayed": True,
            "component_timer_scope": "this attempt only; final COMPLETE dual clocks authoritative"}
        report["future_final_cone32_checkpoint"] = cp
        report["terminal_information_state"] = {
            "bank_entries": len(objective.direction_bank.entries),
            "bank_state_sha256": objective.direction_bank.state_digest(),
            "supplemental_normals": len(objective.supplemental_normals),
            "pool_counts": [len(objective.pool), len(objective.fine_pool)],
            "pool_versions": [objective.pool_version, objective.fine_pool_version],
            "learning_events": len(objective.curvature_defect_memory.events),
            "learning_commits": len(objective.curvature_defect_memory.commits),
            "learning_pending": len(objective.curvature_defect_memory.pending),
            "learning_state_sha256": objective.curvature_defect_memory.state_record()["state_sha256"],
            "trust": stage["last_restricted_trust"],
            "legacy_streak": stage["final_consecutive_growth_qualifying_models"],
            "covered_streak": stage["final_covered_ordinary_growth_streak"]}
        report["status"] = COMPLETE if stage.get("error") is None else "cone32-stage-error-best-retained"
    except Exception as error:
        report["status"] = "cone32-audit-error"
        report["error"] = {"type": type(error).__name__, "message": str(error), "traceback": traceback.format_exc()}
        if objective is not None:
            report.setdefault(STAGE, {"solver": {}})["checkpoint"] = objective.snapshot()
    finally:
        report["timing_segments"].setdefault("constructor_seconds", time.monotonic()-ctor_started)
        if objective is not None:
            report["direct_reference_geometry_timing"] = problem.timing_snapshot()
            report["final_solver_account"] = objective.cone_ledger.report()
            report["all_current_cone_events"] = [
                frozen.cone_call_semantic(e) for e in objective.cone_ledger.events]
            report["final_value_account"] = {
                "source_original_values": SOURCE_TOTAL_VALUES,
                "current_attempt_values": objective.full_value_evaluations-SOURCE_TOTAL_VALUES,
                "cumulative_original_values": objective.full_value_evaluations,
                "cumulative_cone_task_values": objective.full_value_evaluations-SOURCE_VALUES,
                "coarse_cumulative": objective.geometry_evaluations,
                "fine_cumulative": objective.fine_evaluations,
                "original_cap": 160, "cone_task_cap": 96,
                "no_new_independent_final_audit": True}
    return report


def emit_result(report):
    for model in report.get(STAGE, {}).get("solver", {}).get("models", []):
        emit("MODEL", semantic_model(model))
    emit("COMPLETE", summary(report))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    require_public_research_environment()
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    clock = ContinuedCone32Clock(time.monotonic())
    report = {
        "schema": SCHEMA, "status": "cone32-not-yet-read",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "source_files_sha256": implementation_hashes(),
        "new_developer_or_tiny_solver_executions": 0,
        "old_HiGHS_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
        "source_cone_calls": 31, "source_actual_values": SOURCE_TOTAL_VALUES,
        "timing_segments": {}}
    try:
        raw_request = Path(args.request).read_bytes()
        request = json.loads(raw_request)
        p = request["parameters"]
        require(p["policy"] == CONTINUATION_POLICY and p["source_cone_calls"] == 31
                and p["maximum_additional_cone_calls"] == 1 and p["new_legacy_LP_SOC_calls"] == 0
                and p["source_cone_science_seconds"] == SOURCE_CONE_SECONDS
                and p["source_global_science_seconds"] == SOURCE_GLOBAL_SECONDS
                and p["source_actual_values"] == SOURCE_TOTAL_VALUES
                and p["unchanged_limits"] == LIMITS and p["unchanged_settings"] == SETTINGS
                and p["allowed_candidate_statuses"] == list(CANDIDATE_STATUSES)
                and p["new_development_checks"] == 0 and p["old_checks_executed"] == 0,
                "the exact unchanged final-slot resource/status contract differs")
        for path, expected in request["source_sha256"].items():
            require(reader.digest(Path(path).read_bytes()) == expected, "requested source changed: "+path)
        py = {Path(path).name: sha for path, sha in request["source_sha256"].items() if path.endswith(".py")}
        require(py == implementation_hashes() and len(py) == 170 and len(request["source_sha256"]) == 189,
                "paid167 plus exactly three new Python sources and reviewed189 closure required")
        emit("REQUEST", {"source_commit": os.environ.get("GITHUB_SHA"),
            "request_bytes": len(raw_request), "request_sha256": reader.digest(raw_request),
            "source_sha256": request["source_sha256"], "parameters": p})
        started = time.monotonic()
        completed = read_source(request, clock)
        report["timing_segments"]["latest_paid_log_read_and_validation_seconds"] = time.monotonic()-started
        report["paid_source_receipt"] = copy.deepcopy(completed["receipt"])
        emit("PRIOR_WORK_REUSED", completed["receipt"])
        started = time.monotonic()
        prepared = prepare(request, output, completed, clock)
        report["timing_segments"]["necessary24_input_prepare_seconds"] = time.monotonic()-started
        run_audit(prepared, completed, output, clock, report)
    except Exception as error:
        report["status"] = "cone32-input-or-reporting-error"
        report["error"] = {"type": type(error).__name__, "message": str(error), "traceback": traceback.format_exc()}
        report["actual_stage_and_solver_accounts_preserved"] = True
    try:
        save_report(output, report, clock)
        emit_result(report)
    except Exception as error:
        # Keep the same sink: never overwrite real events/values with a blank report.
        report["status"] = "cone32-final-reporting-error"
        report["post_entry_reporting_error"] = {
            "type": type(error).__name__, "message": str(error), "traceback": traceback.format_exc()}
        report["continued_science_account"] = clock.report()
        report["process_total_elapsed_seconds"] = time.monotonic()-PROCESS_STARTED
        emit_result(report)
    for path in sorted(output.parent.glob("*.json")):
        raw = path.read_bytes()
        emit("OUTPUT_METADATA", {"filename": path.name, "bytes": len(raw),
             "sha256": reader.digest(raw), "payload_repository_artifact_cache_uploads": 0})
    return 0 if report.get("status") == COMPLETE else 1


if __name__ == "__main__":
    raise SystemExit(main())

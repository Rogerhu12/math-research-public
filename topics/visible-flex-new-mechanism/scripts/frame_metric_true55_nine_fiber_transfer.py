#!/usr/bin/env python3
"""Restore the one actually accepted55 source; do not replay any old model.

Import-only. The caller starts NineFiberLedger before imports and all I/O.
One original research log supplies COMPLETE, accepted CACHE ordinal2 and the
 authoritative FINAL_CLOCK. Only the exact original selected row pools are
 inherited. Old159 gradients, finite problems and directions are not reused.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import io
from pathlib import Path
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid, array_digest
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
import read_original_actions_log as reader
import frame_metric_paid_cone_vector_audit as paid
import frame_metric_direct_reference_audit as direct_audit
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
from frame_metric_true55_nine_fiber_scope import POLICY, NineFiberLedger, require

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
SOURCE_ACCEPTED_INDEX = 55
SOURCE_PHYSICAL_SHA = "39e71805432d8e1814032200b8cb70973e95475b4ec02696233a7bb37e57746e"
SOURCE_STATE_SHA = "a66f9708cb878b5d700de8ca072017daa39ff3913f061315fe070f8b54bb7fc2"
SOURCE_COORDINATE_SHA = "b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580"
SOURCE_CFG_SHA = "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA = "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"
SOURCE_OBJECTIVE_SHA = "5407778b5d8290ee1ad257259e0bcfe378147e805a8fc90eb12b4db230d183d1"
SOURCE_GLOBAL_SECONDS = 2073.56241112
SOURCE_ORIGINAL_VALUES = 134
SOURCE_ACCEPTED_CACHE_BINDING = "697ee3cbaa48d26e0d6b0e230524523732c3cd96e572711ebf2044e9c5a3a2b6"
SOURCE_STATUS = "complete-fresh54-model-exchange-and-original-actual-observation"
PREFIX = "TRUE54_FRESH_"
GRID_SHAPES = {"coarse": (160, 384), "fine": (160, 768)}

PINS = {
    "run_id": "43832870561",
    "job_id": "133182173190",
    "source_commit": "23b37e90cbc1ac33ca6ff8ac1f91fa7a95c903db",
    "workflow": ".github/workflows/visible-true54-fresh-model.yml",
    "log_bytes": 81300477,
    "log_sha256": "36bfb2269d5a85c52116066e521c9ffdce4f9c99dc35866a11d31e0830928ce2"
}
RECORDS = [
    {
        "tag": "COMPLETE",
        "ordinal": 1,
        "JSON_plus_LF_bytes": 5388242,
        "JSON_plus_LF_sha256": "a7819f1e04a97c5003e4058fb3c1df17a9841c5b6006790875a98cee27622b4b"
    },
    {
        "tag": "CACHE",
        "ordinal": 2,
        "JSON_plus_LF_bytes": 29873051,
        "JSON_plus_LF_sha256": "9e2d8986f82674d5fef27b530b177798419a203bfbef4782c632c23a8ed5870f"
    },
    {
        "tag": "FINAL_CLOCK",
        "ordinal": 1,
        "JSON_plus_LF_bytes": 95650,
        "JSON_plus_LF_sha256": "61ac9c3d62f869307d8f2ab1357c438466395997cd31189a2d3e225fea8369bb"
    }
]
SOURCE_REQUEST = {
    "path": "topics/visible-flex-new-mechanism/computations/request-true54-fresh-model.json",
    "bytes": 54065,
    "sha256": "ee73f17aa45584743306d7d49a16118f3d087a611d4f583590fa825e7f641c76"
}


def exact_binary64(values, length):
    require(isinstance(values, list) and len(values) == length
            and all(isinstance(v, str) for v in values),
            "full exact-vector strings are required")
    exact = [Q(v) for v in values]
    array = np.asarray([float(v) for v in exact], dtype=np.float64)
    require(np.all(np.isfinite(array)) and all(
        Q.from_float(float(v)) == q for v, q in zip(array, exact)),
        "the source vector is not exactly binary64 recoverable")
    return array


def _source_records(raw, ledger):
    expected = {(r["tag"], r["ordinal"]): r for r in RECORDS}
    found, counts, receipts = {}, {}, []
    # Decode only this log, and only the three required payloads. In particular
    # CACHE1 contains a source54 direction, not accepted55 ordinary geometry.
    for line in io.StringIO(raw.decode("utf-8-sig")):
        clean = reader.ANSI.sub("", line.rstrip("\r\n")).lstrip("\ufeff")
        match = reader.TIME_PREFIX.match(clean)
        if match is None:
            continue
        body = match.group(2).lstrip("\ufeff")
        if not body.startswith(PREFIX):
            continue
        tag, separator, payload = body[len(PREFIX):].partition(" ")
        if not separator:
            continue
        counts[tag] = counts.get(tag, 0) + 1
        key = (tag, counts[tag])
        if key not in expected:
            continue
        ledger.check()
        literal = payload.encode("utf-8") + b"\n"
        pin = expected[key]
        require(len(literal) == pin["JSON_plus_LF_bytes"]
                and reader.digest(literal) == pin["JSON_plus_LF_sha256"],
                "the original JSON+LF payload changed: " + str(key))
        found[key] = reader.decode_json(literal)
        receipts.append(copy.deepcopy(pin))
        ledger.check()
    require(set(found) == set(expected)
            and counts.get("COMPLETE") == 1
            and counts.get("CACHE") == 2
            and counts.get("FINAL_CLOCK") == 1,
            "the complete source55 record ordinals differ")
    return found, receipts


def _accepted_cache(cache, cp, point, real, state):
    require(cache.get("kind") == "accepted-point-paid-geometry"
            and cache.get("available") is True and cache.get("status") == "complete"
            and cache["binding_sha256"] == SOURCE_ACCEPTED_CACHE_BINDING
            and digest(cache["binding"]) == SOURCE_ACCEPTED_CACHE_BINDING,
            "CACHE2 must be the paid accepted55 ordinary first-jet cache")
    binding = cache["binding"]
    require(binding["accepted_index"] == SOURCE_ACCEPTED_INDEX
            and binding["physical_state_sha256"] == SOURCE_PHYSICAL_SHA
            and binding["independent159_array_sha256"] == SOURCE_STATE_SHA
            and binding["coordinate_definition_sha256"] == SOURCE_COORDINATE_SHA
            and binding["original_cfg_sha256"] == SOURCE_CFG_SHA
            and binding["ordinary_field_evaluation_sha256"] == SOURCE_FIELD_SHA
            and binding["objective_evaluation_sha256"] == cp["objective_evaluation_sha256"],
            "accepted55 cache source/field/configuration identity changed")
    saved = cache["accepted_independent159"]
    require(saved["shape"] == [159] and saved["dtype"] == "float64"
            and saved["array_sha256"] == SOURCE_STATE_SHA
            and np.asarray(saved["values"], dtype=np.float64).tobytes() == state.tobytes(),
            "the cache has a different accepted159 coefficient vector")
    require(point["physical_state_sha256"] == cache["metadata"]["physical_state_sha256"],
            "accepted cache metadata belongs to another actual point")
    receipt = real["accepted_cache_stdout_receipt"]
    pin = next(r for r in RECORDS if r["tag"] == "CACHE")
    require(receipt["tag"] == PREFIX+"CACHE"
            and receipt["JSON_plus_LF_bytes"] == pin["JSON_plus_LF_bytes"]
            and receipt["JSON_plus_LF_sha256"] == pin["JSON_plus_LF_sha256"]
            and receipt["binding_sha256"] == SOURCE_ACCEPTED_CACHE_BINDING
            and receipt["accepted_index"] == SOURCE_ACCEPTED_INDEX
            and cp["fresh54_model_exchange_method"]["new_accepted_first_jet_cache_receipt"] == receipt,
            "COMPLETE/checkpoint must point to this exact accepted CACHE2")
    require(set(cache["grids"]) == set(GRID_SHAPES),
            "both accepted complete grids are required")
    # The complete literal payload hash already authenticates every value.
    # Do not decode/copy large arrays into a second model or compare new
    # geometry against old values as an extra scientific observation.
    for label, (nr, nt) in GRID_SHAPES.items():
        rows = cache["grids"][label]
        expected = {"U": [nr, nt, 3], "T": [nr, nt, 3],
                    "e": [nr*nt], "f": [nr*nt], "radial": [nr], "theta": [nt]}
        require(set(rows) == set(expected), "unexpected accepted cache arrays")
        for name, shape in expected.items():
            row = rows[name]
            require(row["shape"] == shape and row["dtype"] == "float64"
                    and row["array_sha256"] == binding["grid_array_sha256"][label][name],
                    "accepted cache array metadata differs: " + label + "/" + name)
    return cache


def read_source(request, ledger, *, capture=None):
    """Read the single source55 log; never call old MODEL/finite/geometry code."""
    require(isinstance(ledger, NineFiberLedger), "the new shared NineFiberLedger is required")
    ledger.check()
    progress = {} if capture is None else capture
    require(isinstance(progress, dict) and not progress, "fresh source capture required")
    tick = time.monotonic()
    progress.update(status="started", source=copy.deepcopy(PINS),
                    original_logs_requested=0, source54_models_or_J_reexecuted=0,
                    ordinary_geometry_calls=0)
    try:
        require(request["source"] == PINS and request["source_records"] == RECORDS
                and request["source_request"] == SOURCE_REQUEST,
                "only the completed accepted55 original source is allowed")
        old_bytes = Path(SOURCE_REQUEST["path"]).read_bytes()
        require(len(old_bytes) == SOURCE_REQUEST["bytes"]
                and reader.digest(old_bytes) == SOURCE_REQUEST["sha256"],
                "the original source request changed")
        old_request = reader.decode_json(old_bytes)
        require(len(request["original_input_arguments"]) == 98
                and request["original_input_arguments"] == old_request["original_input_arguments"]
                and request["fixed_complete_metric_sha256"] == old_request["fixed_complete_metric_sha256"]
                and request["fixed_b0_definition_sha256"] == old_request["fixed_b0_definition_sha256"],
                "all original24 inputs and fixed g/b0 bindings must be retained")
        ledger.check()
        api = reader.GitHubReader(REPO)
        run = api.api_json("/actions/runs/" + PINS["run_id"])
        job = api.api_json("/actions/jobs/" + PINS["job_id"])
        require(str(run["id"]) == str(job["run_id"]) == PINS["run_id"]
                and str(job["id"]) == PINS["job_id"]
                and run["head_sha"] == job["head_sha"] == PINS["source_commit"]
                and run["status"] == job["status"] == "completed"
                and run["conclusion"] == job["conclusion"] == "success"
                and run["path"] == PINS["workflow"],
                "the original accepted55 run/job/source/workflow is not complete")
        ledger.check()
        progress["original_logs_requested"] = 1
        raw, redirects = api.job_log(PINS["job_id"])
        require(len(raw) == PINS["log_bytes"]
                and reader.digest(raw) == PINS["log_sha256"],
                "the original accepted55 research stdout changed")
        records, fingerprints = _source_records(raw, ledger)
        del raw
        real, cache, clock = (records[("COMPLETE", 1)], records[("CACHE", 2)],
                              records[("FINAL_CLOCK", 1)])
        require(real["status"] == clock["status_at_final_emit"] == SOURCE_STATUS
                and clock["scope_exhausted"] is False
                and clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
                and real["github_sha"] == PINS["source_commit"]
                and str(real["github_run_id"]) == PINS["run_id"]
                and real["github_repository"] == REPO
                and real["old_checks_executed"] == real["new_development_executed"] == 0
                and real["source_files_sha256"] == old_request["source_sha256"],
                "the accepted55 scientific source/outcome contract differs")
        final = clock["ledger"]
        require(final["total_ancestor_plus_new_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
                and final["total_source_plus_new_started_values"] == SOURCE_ORIGINAL_VALUES
                and final["total_source_plus_new_full_value_debits"] == SOURCE_ORIGINAL_VALUES
                and final["started_counts"]["actual_trial_pairs"] == 1
                and final["started_counts"]["actual_grid_values"] == 2,
                "the final source55 clock/value account differs")
        cp = real["future_fresh54_checkpoint"]
        point = real["selected_two_grid_physical_point"]
        require(point == cp["selected_two_grid_physical_point"]
                and point["accepted_index"] == cp["selected_accepted_index"] == SOURCE_ACCEPTED_INDEX
                and point["physical_state_sha256"] == cp["selected_physical_state_sha256"]
                    == SOURCE_PHYSICAL_SHA
                and point["exact_binary64_independent_coordinates"]
                    == cp["selected_final159_binary64_exact"]
                and point["exact_original_physical_coefficients"]
                    == cp["selected_final163_physical_exact"]
                and digest(cp["configuration"]) == SOURCE_CFG_SHA
                and cp["configuration"] == real["configuration"],
                "accepted55 point/vectors/configuration disagree")
        state = exact_binary64(cp["selected_final159_binary64_exact"], 159)
        require(array_digest(state) == SOURCE_STATE_SHA
                and np.asarray(point["independent_coordinates_binary64"], dtype=np.float64).tobytes()
                    == state.tobytes()
                and len(cp["selected_final163_physical_exact"]) == 163
                and all(isinstance(v, str) for v in cp["selected_final163_physical_exact"]),
                "the complete accepted55 independent159/physical163 data are required")
        require(digest(cp["coordinate_definition"]) == SOURCE_COORDINATE_SHA,
                "the inherited independent159/reference163 map differs")
        for key, sha_key in (
                ("objective_evaluation_definition", "objective_evaluation_sha256"),
                ("ordinary_field_evaluation_definition", "ordinary_field_evaluation_sha256"),
                ("factorization_definition", "factorization_definition_sha256")):
            require(digest(cp[key]) == cp[sha_key], "source definition hash differs: " + key)
        require(cp["objective_evaluation_sha256"] == SOURCE_OBJECTIVE_SHA
                and cp["ordinary_field_evaluation_sha256"] == SOURCE_FIELD_SHA
                and (len(cp["coarse_pool"]), len(cp["fine_pool"]),
                     cp["coarse_pool_version"], cp["fine_pool_version"]) == (4453, 4549, 14, 14)
                and cp["terminal_trust"] == .00025
                and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
                "the accepted55 pools/controller state differ")
        require(cp["configuration"]["max_physical_evaluations"] == 160
                and cp["configuration"]["max_seconds"] == 1800,
                "original closed-scope configuration metadata may not be overwritten")
        gates = {}
        for label, key in (("coarse", "final_full_grid_constraints"),
                           ("fine", "final_doubled_constraints")):
            decision = real[key]
            require(len(decision["actual_gate_booleans"]) == 14
                    and all(v is True for v in decision["actual_gate_booleans"].values())
                    and decision["direct_max_eta"] == point[label]["direct_max_eta"],
                    "the paid55 original14 gates differ: " + label)
            gates[label] = copy.deepcopy(decision)
        stage = real["fresh54_direction_actual_stage"]
        accepted = [t for t in stage["trials"] if t.get("accepted_as_next_iterate") is True]
        require(stage["new_acceptances"] == 1 and len(accepted) == 1
                and accepted[0]["accepted_index"] == SOURCE_ACCEPTED_INDEX
                and accepted[0]["physical_state_sha256"] == SOURCE_PHYSICAL_SHA
                and accepted[0]["exact_binary64_independent_coordinates"]
                    == cp["selected_final159_binary64_exact"]
                and accepted[0]["exact_original_physical_coefficients"]
                    == cp["selected_final163_physical_exact"],
                "one original actually accepted55 trial must match the checkpoint")
        _accepted_cache(cache, cp, point, real, state)
        seeds, seed_provenance = [], []  # New nine-column model starts with exact selected pools.
        cost = {
            "ancestor_final_original_scientific_seconds": SOURCE_GLOBAL_SECONDS,
            "source_global_scientific_seconds": SOURCE_GLOBAL_SECONDS,
            "source_original_full_values": SOURCE_ORIGINAL_VALUES,
            "source_original_values": SOURCE_ORIGINAL_VALUES,
            "source_final_clock": copy.deepcopy(clock),
            "source_cost_already_contains_all_older_ancestors_and_failed_inputs": True,
            "earlier_checkpoint_samples_not_added_to_final_clock": True,
            "old_HiGHS_cone_projection_finite_and_direction_epochs_closed": True}
        receipt = {
            "schema": POLICY+"-accepted55-source-receipt", "passed": True,
            "source": copy.deepcopy(PINS), "source_records": fingerprints,
            "source_request": copy.deepcopy(SOURCE_REQUEST),
            "accepted_cache_binding_sha256": SOURCE_ACCEPTED_CACHE_BINDING,
            "accepted_physical_state_sha256": SOURCE_PHYSICAL_SHA,
            "accepted_independent159_array_sha256": SOURCE_STATE_SHA,
            "source_objective_evaluation_sha256": cp["objective_evaluation_sha256"],
            "source_coordinate_definition_sha256": SOURCE_COORDINATE_SHA,
            "paid_ancestor_scientific_seconds": SOURCE_GLOBAL_SECONDS,
            "paid_ancestor_ordinary_values": SOURCE_ORIGINAL_VALUES,
            "seed_original_metric_row_count": len(seeds),
            "old54_extra_seed_gradients_not_reused_as_new9": True,
            "seed_original_metric_row_tags": copy.deepcopy(seeds),
            "seed_provenance": seed_provenance,
            "source54_gradient_values_not_inherited": True,
            "source54_MODEL_J_finite_directions_or_source_actual_not_reexecuted": True,
            "one_original_log_read_no_old_log_reads": True,
            "source_CACHE1_line_predictions_not_decoded": True,
            "accepted_CACHE2_contains_no_positions_curvature_two_jets_or_J": True,
            "large_accepted_array_values_authenticated_by_literal_payload_hash": True,
            "redirect_count_without_forwarding_authorization": redirects,
            "all_input_copy_hash_and_failure_seconds_in_new_shared_clock": True}
        progress.update(status="complete", records=fingerprints,
                        accepted_index=SOURCE_ACCEPTED_INDEX,
                        seed_tag_count=len(seeds),
                        accepted_cache_binding_sha256=SOURCE_ACCEPTED_CACHE_BINDING)
        ledger.check()
        return {
            "report": real, "checkpoint": cp, "point": point, "gates": gates,
            "receipt": receipt, "ancestor_cost_receipt": cost,
            "source_final_clock": clock, "accepted_cache": cache,
            "seed_metric_tags": seeds}
    except Exception as error:
        progress.update(status="raised",
                        error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        progress["elapsed_source_input_seconds"] = time.monotonic()-tick


def prepare(request, output, completed, ledger, *, process_started):
    require(isinstance(ledger, NineFiberLedger), "one shared NineFiberLedger required")
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
            "physical current55/g/b0/direct evaluator/configuration changed")
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
        "source_accepted_cache_binding_sha256": SOURCE_ACCEPTED_CACHE_BINDING,
        "source_seed_metric_tags": copy.deepcopy(completed["seed_metric_tags"]),
        "source_input_restoration": {
            "all24_original_inputs_loaded_once": True,
            "new9_scope_policy": POLICY,
            "source_accepted55_cache_restored_but_no_geometry_constructed": True,
            "necessary_new_model_values_are_owned_by_new9_geometry_helper": True,
            "closed_ancestor_scientific_seconds": SOURCE_GLOBAL_SECONDS,
            "closed_ancestor_ordinary_values": SOURCE_ORIGINAL_VALUES,
            "no_old_developer_geometry_J_JVP_model_solver_or_trial_replay": True,
            "source_configuration_unchanged": True,
            "historical24_configuration_sha256": digest(historical_cfg),
            "field_transfer": field_receipt, "fresh_adapter_gate": gate_receipt,
            "original_primitive_order": order,
            "pool_restoration_without_initialize_or_automatic_expand": True}}
    require(problem.timing_snapshot()["geometry_calls_started"] == 0,
            "input preparation may not construct ordinary geometry")
    ledger.check()
    return {"accepted_cache": completed["accepted_cache"],
            "fine_theta": np.asarray(completed["accepted_cache"]["grids"]["fine"]["theta"]["values"], dtype=np.float64),
            "source_binding": {"source": copy.deepcopy(PINS), "accepted_index": SOURCE_ACCEPTED_INDEX,
                "physical_state_sha256": SOURCE_PHYSICAL_SHA, "independent159_array_sha256": SOURCE_STATE_SHA,
                "source_original_cfg_sha256": SOURCE_CFG_SHA, "source_original_field_sha256": SOURCE_FIELD_SHA,
                "source_original_objective_sha256": SOURCE_OBJECTIVE_SHA},
            "seed_metric_tags": copy.deepcopy(completed["seed_metric_tags"]),
            "problem": problem, "initial": initial, "initial159": initial, "gate": gate, "cfg": cfg,
            "radial": radial, "theta": theta, "grid": grid, "row_grids": grids, "order": order,
            "lower": gate.coordinate_lower, "upper": gate.coordinate_upper,
            "coarse_pool": coarse, "fine_pool": fine, "bindings": bindings, "replay": replay}

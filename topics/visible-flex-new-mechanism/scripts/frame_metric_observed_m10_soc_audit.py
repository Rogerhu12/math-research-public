#!/usr/bin/env python3
"""One first expanded-pool SOC on the already observed norm-memory model10.

Read-only historical recovery; no old primary LP, optimization, or developer
suite. All new interface checks, ordinary values, Jacobians, and the one SOC
are executed only in the public repository Actions. No source cfg is changed.
"""
from __future__ import annotations
import argparse
import ast
import base64
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import time
import traceback
import numpy as np
from frame_collar_bvp import atomic_save
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_affine_spectral_model import definition as selected_definition
from frame_complete_affine_metric_oracle import definition as complete_definition
from frame_metric_height159_complete_affine import attach_complete_model_reports
import frame_metric_expanded_pool_soc as core
import frame_metric_expanded_pool_soc_recovery as frozen_outer
import frame_metric_expanded_pool_soc_audit as frozen_audit
import frame_metric_expanded_pool_soc_transfer as transfer
import read_original_actions_log as reader

SCHEMA = "same159-observed-m10-first-expanded-pool-SOC-v1"
STAGE = "observed_m10_SOC_stage"
REPO = transfer.REPO
require = transfer.require


def implementation_hashes():
    result = frozen_audit.implementation_hashes()
    for name in (Path(__file__).name, "frame_metric_observed_m10_soc_development.py",
                 "frame_metric_observed_m10_cache_development.py"):
        p = Path(__file__).parent/name
        result[name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def emit(tag, value):
    print(tag+" "+reader.encoded(value).decode("utf-8"), flush=True)


def select_case(real, models, cp, expected):
    """Only original JSON fields and integer-list operations; no geometry."""
    require([m.get("number") for m in models] == list(range(1, 12)),
            "all eleven source models required")
    m = models[9]
    require(m["result"] == "new-rows-return-to-last-accepted-before-SOC"
            and len(m["trials"]) == 1 and not m.get("corrections"),
            "the original failed model10 must not have any SOC or backtrack")
    t = m["trials"][0]
    require(t["kind"] == "primary-metric-short-step" and t["alpha_exact"] == "1"
            and t["accepted_as_next_iterate"] is False
            and t["new_coarse_rows"] == t["new_fine_rows"] == 1,
            "one unaccepted complete primary with exactly two learned IDs required")
    points = real[transfer.SOURCE_STAGE]["accepted_iterates"]
    matches = [a for a in points if a.get("accepted_index") == m["linearized_at_accepted_index"]]
    require(len(matches) == 1 and matches[0]["accepted_index"] == 7,
            "unique original accepted index7 required")
    x = matches[0]
    native_x = [(a["number"], v) for a in models for v in a.get("trials", [])
                if v.get("accepted_as_next_iterate") is True and v.get("accepted_index") == 7]
    require(len(native_x) == 1 and native_x[0][0] == 9,
            "unique native model9 acceptance of x required")
    x_trial = native_x[0][1]
    for key in ("physical_state_sha256", "exact_binary64_independent_coordinates",
                "exact_original_physical_coefficients"):
        require(x_trial[key] == x[key], "native accepted x and checkpoint differ: "+key)
    require(x["physical_state_sha256"] == m["linearized_at_physical_sha256"]
            == expected["x_physical_sha256"] and
            t["physical_state_sha256"] == expected["y_physical_sha256"],
            "original x/y canonical identities differ")
    for name, item in (("x", x), ("y", t)):
        require(len(item["exact_binary64_independent_coordinates"]) == 159
                and len(item["exact_original_physical_coefficients"]) == 163,
                "complete exact159 and physical163 source lists required")
        require(digest(item["exact_binary64_independent_coordinates"]) ==
                expected[name+"159_compact_json_sha256"], name+" exact list differs")
        require(item["coarse_decision" if name == "y" else "coarse"]
                ["regularity_screen_pass"] and
                item["fine_decision" if name == "y" else "fine"]["regularity_screen_pass"],
                "both source grids must be regular")
    later = models[10]
    require(later["linearized_at_accepted_index"] == 7 and
            all(t0.get("new_coarse_rows") == t0.get("new_fine_rows") == 0
                for t0 in later.get("trials", [])) and not later.get("corrections"),
            "model11 must not change either pool")
    history = real[transfer.SOURCE_STAGE]["current_pool_metadata"]
    old_pools, new_pools, pool_proof = [], [], []
    for label, hkey, dkey in (
            ("coarse", "active_row_pool_history", "whole_coarse_separation"),
            ("fine", "fine_physical_row_pool_history", "whole_fine_separation")):
        last = history[hkey]
        detail = last["reason"][dkey]
        groups = detail["group_counts"]
        require(detail["omitted_violating_count"] == 1 and
                detail["omitted_hard_violating_count"] == 0 and
                groups["metric_minus"] == {"omitted": 0, "whole_grid": 0} and
                groups["metric_plus"] == {"omitted": 1, "whole_grid": 0} and
                all(v["omitted"] == 0 for k, v in groups.items()
                    if k not in ("metric_minus", "metric_plus")),
                "source separation does not uniquely identify a soft peak slot")
        count = m["linear_program"]["model"]["binding"]["full_grid_oracle_binding"][
            "grids"][label]["original_point_count"]
        peak = detail["true_eta_peak_point_index"]
        require(type(count) is int and type(peak) is int and 0 <= peak < count,
                "original full-grid point metadata differs")
        new_id = count+peak
        require(new_id == expected["new_row_ids"][label], "unique original new ID differs")
        values = cp[label+"_pool"]
        require(values == sorted(set(values)) and values.count(new_id) == 1,
                "complete sorted final pool lacks the unique inserted ID")
        require(len(values) == later[label+"_pool_rows"] == last["row_count"] and
                later[label+"_pool_version"] == last["version"] ==
                m[label+"_pool_version"]+1 and
                len(values) == m[label+"_pool_rows"]+1,
                "last complete pool is not the post-model10 pool")
        require(digest(values) == last["row_indices_sha256"],
                "complete post-model10 pool digest differs")
        old = [i for i in values if i != new_id]
        require(digest(old) == expected["old_pool_compact_json_sha256"][label],
                "recovered original pre-model10 pool differs")
        old_pools.append(old); new_pools.append(list(values))
        pool_proof.append({"grid": label, "old_version": m[label+"_pool_version"],
            "new_version": last["version"], "old_count": len(old), "new_count": len(values),
            "only_new_original_ID": new_id, "true_eta_peak_point_index": peak,
            "old_compact_json_sha256": digest(old), "new_compact_json_sha256": digest(values),
            "both_source_soft_whole_grid_violation_counts_zero": True,
            "no_later_pool_mutation": True})
    inherited = sum(int(a["linear_program"]["inner_call_count"]) for a in models[:10])
    require(inherited == 11 and all(not a.get("corrections") for a in models[:10]),
            "the unique historical12th LP slot is not available")
    require(t["coarse_physical_evaluation"] == t["fine_value_evaluation"] == 11,
            "original observed value counters differ")
    for a in models[9:]:
        require(not any("direction_memory_after_this_cut_sha256" in z
                        for z in a["linear_program"].get("cut_rounds", [])),
                "bank changed at or after model10")
    require(m["linear_program"]["initial_rebuilt_memory_rows"] == 9,
            "model10 did not have the original nine-entry bank")
    prior = models[8]["scale_feedback_update"]
    streak = prior["successful_SOC_radius_retention"]["new_next_success_streak"]
    require(m["trust_before_model"] == prior["next_trust"] == .000125 and streak == 0,
            "original model10 radius/streak differs")
    proof = {
        "schema": SCHEMA+"-historical-case", "source_model": 10, "source_primary_trial": 0,
        "source_accepted_index": 7, "x_physical_sha256": x["physical_state_sha256"],
        "y_physical_sha256": t["physical_state_sha256"], "pool_proof": pool_proof,
        "body_radius_evaluated": m["trust_before_model"],
        "body_radius_exact_binary64": str(Q.from_float(m["trust_before_model"])),
        "source_success_streak_before_model": streak,
        "inherited_primary_LP_calls": inherited, "inherited_correction_LP_calls": 0,
        "inherited_ordinary_value_calls_through_failed_y": 22,
        "source_primary_optimization_is_not_reexecuted": True,
        "source_whole_J_and_ordinary_caches_not_available": True,
        "historical_active_clock_checkpoint_not_available": True,
        "only_one_new_SOC_allowed": True}
    return {"model": copy.deepcopy(m), "x_record": copy.deepcopy(x),
            "x_trial": copy.deepcopy(x_trial), "trial": copy.deepcopy(t), "old_pools": old_pools, "new_pools": new_pools,
            "proof": proof, "streak": streak}


def prepare_case(request, out, started):
    real, models, cp, source = transfer.read_completed(request)
    case = select_case(real, models, cp, request["historical_m10"])
    args = transfer.previous.old_input_namespace(request, out)
    prepared = transfer.baseline.growth.prepare_run(args, process_started=started)
    restored, bindings, tenth, _, coarse24, fine24 = prepared
    original, _, old_gate, lower, upper, source_cfg, _ = restored
    field, _, gate, field_meta = transfer.reconstruct_checkpoint_field(
        original, old_gate, lower, upper, cp, request)
    x = transfer.exact_binary_vector(case["x_record"]["exact_binary64_independent_coordinates"], 159)
    y = transfer.exact_binary_vector(case["trial"]["exact_binary64_independent_coordinates"], 159)
    for q, record in ((x, case["x_record"]), (y, case["trial"])):
        require(field.coordinates.physical_exact(q) ==
                tuple(Q(s) for s in record["exact_original_physical_coefficients"]),
                "historical exact159/163 map differs")
        require(digest(field.identity(q)) == record["physical_state_sha256"],
                "historical canonical physical identity differs")
    cfg = copy.deepcopy(real["configuration"])
    require(digest(cfg) == request["source"]["configuration_sha256"] and
            (cfg["max_linear_models"], cfg["max_physical_evaluations"],
             cfg["max_seconds"], cfg["linear_program_seconds"]) == (12, 40, 120, 10),
            "source cfg or original limits changed")
    radial, theta, grid = frozen_audit.curvature_grid(tenth)
    counts = {"coarse": len(radial)*len(theta), "fine": 2*len(radial)*len(theta)}
    for i, label in enumerate(("coarse", "fine")):
        cap = cfg["max_pool_rows" if label == "coarse" else "max_fine_physical_pool_rows"]
        for pools in (case["old_pools"], case["new_pools"]):
            transfer.checked_pool(pools[i], counts[label], cap, label)
    normals, bank_meta = transfer.reconstruct_source_direction_records(
        request, models, coarse24, fine24, counts, cfg)
    source.update(field_transfer=field_meta, historical_case=case["proof"],
                  direction_input_replay=bank_meta)
    return {"field": field, "x": x, "y": y, "gate": gate, "source_cfg": source_cfg,
            "cfg": cfg, "bindings": bindings, "radial": radial, "theta": theta,
            "grid": grid, "case": case, "directions": normals, "source": source,
            "expected_bank_sha256": bank_meta["expected_terminal_bank_state_sha256"],
            "source_configuration_preserved": True}


def _leaves(v, path=()):
    if isinstance(v, dict):
        result = {}
        for k in sorted(v):
            result.update(_leaves(v[k], path+(str(k),)))
        return result
    if isinstance(v, list):
        result = {}
        for i, w in enumerate(v):
            result.update(_leaves(w, path+(str(i),)))
        return result
    return {path: v}


def compare_observable_binding(current, historical):
    """Only two explicit evaluation metadata leaves may differ."""
    new, old = _leaves(current), _leaves(historical)
    require(new.keys() == old.keys(), "historical selected observable field set differs")
    differences = []
    for path in old:
        if new[path] == old[path]:
            continue
        allowed = (len(path) == 3 and path[0] == "external_current_cache_binding"
                   and path[1] in ("0", "1") and path[2] == "evaluation_sha256")
        require(allowed, "historical physical/array observable changed: "+".".join(path))
        differences.append({"path": ".".join(path), "historical": old[path], "current": new[path],
                            "scope": "new explicit policy/evaluation metadata only"})
    return differences


def verify_historical_model(primary, affine, new_binding, historical):
    old = historical["linear_program"]["model"]
    old_binding = old["binding"]
    selected = old_binding["selected_observable_binding"]
    require(digest(selected) == old_binding["selected_observable_binding_sha256"] and
            digest(old_binding["full_grid_oracle_binding"]) ==
            old_binding["full_grid_oracle_binding_sha256"] and
            digest(old_binding) == old["binding_sha256"],
            "historical complete model bindings are internally inconsistent")
    changes = compare_observable_binding(affine.selected_model.binding, selected)
    require(affine.oracle.binding == old_binding["full_grid_oracle_binding"],
            "original full-grid state/field/config/Pi/declaration arrays differ")
    for key in ("selected_scalar_function_count", "additional_complete_maximum_function_count",
                "complete_initial_slack", "inherited_selected_initial_slack",
                "base_slack_difference_retained_not_assumed_zero", "schema"):
        require(affine.binding[key] == old_binding[key], "complete model scalar differs: "+key)
    scalar = primary.information["inherited_scalar_radius_independent_model_sha256"]
    old_selected_signature = digest({
        "inherited_scalar_model_sha256": scalar,
        "affine_spectral_observables_sha256": old_binding["selected_observable_binding_sha256"],
        "policy": selected_definition()})
    old_final_signature = digest({
        "inherited_selected_affine_model_sha256": old_selected_signature,
        "complete_affine_binding_sha256": old["binding_sha256"],
        "policy": complete_definition()})
    source_hold = historical["SOC_hold_model_binding"]
    require(old_final_signature == source_hold["radius_independent_model_sha256"],
            "original scalar full-J/values/tolerances/boxes signature did not replay")
    require(new_binding.keys() == source_hold.keys(), "hold binding field set changed")
    for key in source_hold:
        if key != "radius_independent_model_sha256":
            require(new_binding[key] == source_hold[key],
                    "original physical hold binding differs: "+key)
    return {"schema": SCHEMA+"-historical-model-identity",
        "original_historical_binding": copy.deepcopy(source_hold),
        "new_two_factory_final_binding": copy.deepcopy(new_binding),
        "new_scalar_signature": scalar,
        "historical_selected_signature_replayed": old_selected_signature,
        "historical_final_signature_replayed": old_final_signature,
        "full_original_active_J_values_and_tolerances_bound_by_scalar_signature": True,
        "whole_original_grid_oracle_binding_equal": True,
        "selected_e_f_de_df_hashes_and_original_ID_order_equal": True,
        "allowed_evaluation_metadata_differences": changes,
        "historical_whole_final_hash_not_falsely_used_as_new_capture_binding": True}


def check_decisions(new_coarse, new_fine, old_coarse, old_fine):
    result = {}
    for label, new, old in (("coarse", new_coarse, old_coarse), ("fine", new_fine, old_fine)):
        actual = frozen_outer.compact_with_all_actual_gates(new)
        require(actual["actual_gate_booleans"] == old["actual_gate_booleans"],
                "historical original actual gates changed on "+label)
        values = {k: float(new[k])-float(old[k]) for k in
                  ("direct_max_eta", "direct_maximum_absolute_principal_curvature")}
        require(max(abs(v) for v in values.values()) <= 5e-10,
                "historical complete-grid value changed on "+label)
        result[label] = {"direct_value_differences": values,
                         "all_original_fourteen_gate_flags_equal": True}
    return result


def restore_failed_y_layout(objective, y, record):
    """Reinstall selected-layout caches at the same already-evaluated y.

    Pool learning clears epigraph_cache. The original complete ordinary
    geometry/fine values must still be reusable; this function never grants
    an unobserved zero charge. A miss is retained in record and rejects this
    eight-value replay before any capture/rebound/SOC.
    """
    started = time.monotonic()
    state = np.asarray(y, float)
    before = [int(objective.geometry_evaluations), int(objective.fine_evaluations)]
    versions = [int(objective.pool_version), int(objective.fine_pool_version)]
    ids = [array_digest(objective.pool), array_digest(objective.fine_pool)]
    physical = digest(objective.problem.identity(state))
    state_sha = array_digest(state)
    record.update(schema=SCHEMA+"-post-learning-y-cache-reinstall",
        status="started", new_ordinary_counts_before=before,
        pool_versions_before=versions, pool_ids_sha256_before=ids,
        failed_independent_array_sha256=state_sha,
        failed_physical_state_sha256=physical,
        methods=["original evaluate(vector(y))", "original fine_decision(y)"],
        no_selected_J_or_primary_LP_requested=True)
    try:
        objective.evaluate(objective.vector(state))
        objective.fine_decision(state)
        after = [int(objective.geometry_evaluations), int(objective.fine_evaluations)]
        require(after == before,
                "post-learning y cache reinstallation charged ordinary geometry; "
                "declared eight-value replay stopped")
        require([int(objective.pool_version), int(objective.fine_pool_version)] == versions
                and [array_digest(objective.pool), array_digest(objective.fine_pool)] == ids,
                "post-learning y cache reinstallation changed the expanded layout")
        require(array_digest(state) == state_sha
                and digest(objective.problem.identity(state)) == physical,
                "post-learning y cache reinstallation changed the failed physical state")
        # Use the original strict cache contract; there is no implicit value call.
        views = objective.full_views(state)
        require(len(views) == 2 and [v.grid.label for v in views] == ["coarse", "fine"],
                "both original complete same-y views were not restored")
        record.update(status="complete-no-new-ordinary-value",
                      original_full_views_same_state_contract_passed=True)
        return record
    except Exception as error:
        record.update(status="error",
            error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        after = [int(objective.geometry_evaluations), int(objective.fine_evaluations)]
        record.update(new_ordinary_counts_after=after,
            new_ordinary_calls=[b-a for a, b in zip(before, after)],
            zero_extra_ordinary_calls_observed=before == after,
            elapsed_seconds=time.monotonic()-started)


def reuse_completed_checks(request):
    original = request["reuse_completed_expanded"]
    current = frozen_audit.implementation_hashes()
    require(len(current) == 117 and current == original["source_files_sha256"],
            "one of the117 previously checked frozen dependencies changed")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+str(original["run_id"]))
    job = api.api_json("/actions/jobs/"+str(original["job_id"]))
    require(run["head_sha"] == job["head_sha"] == original["source_commit"] and
            int(job["run_id"]) == int(run["id"]) and
            run["status"] == job["status"] == "completed" and
            run["conclusion"] == job["conclusion"] == "success",
            "completed expanded interface source/run/job differs")
    raw, redirects = api.job_log(str(original["job_id"]))
    require(len(raw) == original["log_bytes"] and reader.digest(raw) == original["log_sha256"],
            "original checked expanded log differs")
    records = []
    for line in raw.decode("utf-8").splitlines():
        marker = "EXPANDED_SOC_DEVELOPMENT "
        if marker in line:
            payload = line.split(marker, 1)[1]
            records.append(((payload+"\n").encode("utf-8"), json.loads(payload)))
    require(len(records) == 1, "unique completed interface record required")
    payload, result = records[0]
    require(len(payload) == original["development_bytes"] and
            reader.digest(payload) == original["development_sha256"] and
            result["all_passed"] is True and result["passed"] is True and
            len(result["checks"]) == 10 and all(v is True for v in result["checks"].values())
            and result["source_files_sha256"] == current,
            "completed ten-interface proof differs")
    return {"original_run_id": original["run_id"], "original_job_id": original["job_id"],
            "original_source_commit": original["source_commit"], "frozen_dependencies": 117,
            "completed_interface_checks": 10, "old_interface_executions_this_run": 0,
            "old_primary_or_optimizer_executions_this_run": 0,
            "development_payload_sha256": reader.digest(payload),
            "redirects_without_authorization": redirects}


def reuse_completed_m10_checks(request):
    """Consume seven paid checks from the original failed scientific job.

    The successful DEV is bound independently of the later scientific status.
    Its original driver is read as source text, never imported or executed.
    Every helper used by those seven groups must remain text-identical.
    """
    original = request["reuse_completed_m10_interfaces"]
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+str(original["run_id"]))
    job = api.api_json("/actions/jobs/"+str(original["job_id"]))
    require(run["head_sha"] == job["head_sha"] == original["source_commit"] and
            int(job["run_id"]) == int(run["id"]) and
            run["status"] == job["status"] == "completed" and
            run["conclusion"] == job["conclusion"] == original["conclusion"] == "failure",
            "original paid m10 DEV run/job/source identity differs")
    raw, redirects = api.job_log(str(original["job_id"]))
    require(len(raw) == original["log_bytes"] and reader.digest(raw) == original["log_sha256"],
            "original completed m10 DEV log differs")
    records = []
    marker = "M10_SOC_DEVELOPMENT "
    for line in raw.decode("utf-8").splitlines():
        if marker in line:
            payload = line.split(marker, 1)[1]
            records.append(((payload+"\n").encode("utf-8"), json.loads(payload)))
    require(len(records) == 1, "one original seven-check DEV payload required")
    payload, result = records[0]
    require(len(payload) == original["development_bytes"] and
            reader.digest(payload) == original["development_sha256"] and
            result["all_passed"] is True and result["passed"] is True and
            len(result["checks"]) == 7 and all(v is True for v in result["checks"].values())
            and not result["errors"] and result["old_developer_calls"] == 0
            and result["geometry_calls"] == result["primary_LP_calls"] == result["SOC_LP_calls"] == 0,
            "original seven-check DEV was not fully completed")
    current = implementation_hashes()
    driver_name = Path(__file__).name
    cache_name = "frame_metric_observed_m10_cache_development.py"
    previous_sources = result["source_files_sha256"]
    require(len(previous_sources) == 119 and len(current) == 120 and
            {k: v for k, v in current.items() if k not in (driver_name, cache_name)} ==
            {k: v for k, v in previous_sources.items() if k != driver_name},
            "one paid dependency or the unchanged seven-check source differs")
    path = original["driver_path"]
    require(path == "topics/visible-flex-new-mechanism/scripts/"+driver_name,
            "original m10 driver source path differs")
    data = api.api_json("/contents/"+path+"?ref="+original["source_commit"])
    require(data.get("encoding") == "base64", "original small driver is not base64 source")
    source_raw = base64.b64decode(data["content"])
    require(len(source_raw) == original["driver_bytes"] and
            reader.digest(source_raw) == original["driver_sha256"] ==
                previous_sources[driver_name],
            "original driver bytes do not bind the paid DEV")
    old_source = source_raw.decode("utf-8")
    new_source = Path(__file__).read_text(encoding="utf-8")
    helper_names = ("select_case", "_leaves", "compare_observable_binding",
                    "verify_historical_model", "check_decisions")
    def helpers(source):
        tree = ast.parse(source)
        found = {name: [n for n in tree.body
                 if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name]
                 for name in helper_names}
        require(all(len(v) == 1 for v in found.values()),
                "each paid helper must have one top-level definition")
        return {name: ast.get_source_segment(source, nodes[0])
                for name, nodes in found.items()}
    before, after = helpers(old_source), helpers(new_source)
    require(before == after and all(isinstance(v, str) and v for v in before.values()),
            "a helper covered by the original seven groups changed")
    return {
        "original_run_id": original["run_id"], "original_job_id": original["job_id"],
        "original_source_commit": original["source_commit"],
        "original_scientific_conclusion": original["conclusion"],
        "original_DEV_all_passed": True, "completed_interface_checks": 7,
        "seven_interface_executions_this_run": 0, "old_optimizer_calls_this_run": 0,
        "development_payload_sha256": reader.digest(payload),
        "original_driver_sha256": reader.digest(source_raw),
        "unchanged_paid_helper_source_sha256": {
            k: reader.digest(v.encode("utf-8")) for k, v in before.items()},
        "unchanged_old_seven_development_source_sha256":
            previous_sources["frame_metric_observed_m10_soc_development.py"],
        "all117_frozen_dependencies_and_old_seven_source_equal": True,
        "redirects_without_authorization": redirects}


def reuse_completed_cache_miss_check(request):
    """Reuse the one successful group from the partial cache DEV, not its failure."""
    original = request["reuse_completed_cache_miss"]
    name_paid = "charged_cache_miss_is_reported_and_rejected_before_capture_not_declared_zero"
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+str(original["run_id"]))
    job = api.api_json("/actions/jobs/"+str(original["job_id"]))
    require(run["head_sha"] == job["head_sha"] == original["source_commit"] and
            int(job["run_id"]) == int(run["id"]) and
            run["status"] == job["status"] == "completed" and
            run["conclusion"] == job["conclusion"] == "failure",
            "original partial cache DEV run/job/source differs")
    raw, redirects = api.job_log(str(original["job_id"]))
    require(len(raw) == original["log_bytes"] and reader.digest(raw) == original["log_sha256"],
            "original partial cache DEV log differs")
    records = []
    marker = "M10_SOC_CACHE_DEVELOPMENT "
    for line in raw.decode("utf-8").splitlines():
        if marker in line:
            payload = line.split(marker, 1)[1]
            records.append(((payload+"\n").encode("utf-8"), json.loads(payload)))
    require(len(records) == 1, "unique original partial cache DEV required")
    payload, result = records[0]
    require(len(payload) == original["development_bytes"] and
            reader.digest(payload) == original["development_sha256"] and
            result["passed"] is False and result["all_passed"] is False and
            len(result["checks"]) == 2 and result["checks"].get(name_paid) is True and
            name_paid not in result["errors"] and
            result["details"][name_paid]["passed"] is True and
            result["geometry_calls"] == result["primary_LP_calls"] == result["SOC_LP_calls"] == 0,
            "charged-miss group was not actually paid in the partial DEV")
    current = implementation_hashes()
    driver_name = Path(__file__).name
    cache_name = "frame_metric_observed_m10_cache_development.py"
    previous = result["source_files_sha256"]
    require(len(previous) == len(current) == 120 and
            {k: v for k, v in current.items() if k not in (driver_name, cache_name)} ==
            {k: v for k, v in previous.items() if k not in (driver_name, cache_name)},
            "a dependency of the paid charged-miss closure changed")
    unchanged = {}
    for filename, names in (
            (driver_name, ("restore_failed_y_layout",)),
            (cache_name, ("_fixture", "_charged_restore_rejected"))):
        data = api.api_json("/contents/topics/visible-flex-new-mechanism/scripts/"+
                            filename+"?ref="+original["source_commit"])
        require(data.get("encoding") == "base64", "original small source encoding differs")
        source_raw = base64.b64decode(data["content"])
        expected = original["sources"][filename]
        require(len(source_raw) == expected["bytes"] and
                reader.digest(source_raw) == expected["sha256"] == previous[filename],
                "source of the paid charged-miss group differs")
        sources = (source_raw.decode("utf-8"),
                   Path(__file__).with_name(filename).read_text(encoding="utf-8"))
        trees = [ast.parse(s) for s in sources]
        for name in names:
            nodes = [[n for n in t.body if isinstance(n, ast.FunctionDef) and n.name == name]
                     for t in trees]
            require(all(len(v) == 1 for v in nodes), "paid cache closure must be uniquely defined")
            pieces = [ast.get_source_segment(s, ns[0]) for s, ns in zip(sources, nodes)]
            require(isinstance(pieces[0], str) and pieces[0] == pieces[1],
                    "paid charged-miss closure source changed: "+name)
            unchanged[filename+":"+name] = reader.digest(pieces[0].encode("utf-8"))
    return {"passed": True, "original_check_name": name_paid,
        "original_run_id": original["run_id"], "original_job_id": original["job_id"],
        "original_source_commit": original["source_commit"],
        "original_whole_cache_DEV_passed": False,
        "original_detail": copy.deepcopy(result["details"][name_paid]),
        "original_development_payload_sha256": reader.digest(payload),
        "unchanged_charged_miss_closure_sha256": unchanged,
        "charged_miss_executions_this_run": 0,
        "redirects_without_authorization": redirects}


def compact_report(report):
    result = {k: copy.deepcopy(v) for k, v in report.items()
              if k not in ("exact_input_storage", STAGE)}
    stage = report.get(STAGE, {})
    snap = stage.get("checkpoint", {})
    result[STAGE] = {k: copy.deepcopy(v) for k, v in stage.items()
                     if k not in ("checkpoint", "solver")}
    result[STAGE]["solver"] = {k: copy.deepcopy(v)
        for k, v in stage.get("solver", {}).items() if k != "models"}
    result[STAGE]["new_replay_model_records"] = len(stage.get("solver", {}).get("models", []))
    result[STAGE]["selected_two_grid_physical_point"] = copy.deepcopy(
        snap.get("selected_two_grid_physical_point"))
    result[STAGE]["accepted_iterates"] = copy.deepcopy(snap.get("accepted_iterates", []))
    result[STAGE]["scalar_counts"] = {k: snap[k] for k in (
        "initialization_elapsed_seconds", "optimization_elapsed_seconds",
        "value_geometry_seconds", "total_full_value_physical_evaluations") if k in snap}
    result[STAGE]["current_pool_metadata"] = {}
    for key in ("active_row_pool_history", "fine_physical_row_pool_history"):
        history = snap.get(key, [])
        if history:
            result[STAGE]["current_pool_metadata"][key] = {
                k: copy.deepcopy(v) for k, v in history[-1].items()
                if k not in ("row_indices", "added_row_indices", "added_original_grid_coordinates")}
    return result


def save_report(out, report):
    atomic_save(out, report)
    atomic_save(Path(out).with_name(Path(out).stem+"-summary.json"), compact_report(report))


def run_case(prepared, out, *, process_started, prepare_seconds):
    field, gate = prepared["field"], prepared["gate"]
    cfg, source_cfg = prepared["cfg"], prepared["source_cfg"]
    x, y, case = prepared["x"], prepared["y"], prepared["case"]
    radial, theta, grid = prepared["radial"], prepared["theta"], prepared["grid"]
    source_model, source_trial = case["model"], case["trial"]
    trust = float(source_model["trust_before_model"])
    objective = None
    model = None
    correction = None
    active_started = None
    independent_final_calls = 0
    result_status = "not-started"
    started = time.monotonic()
    ledger = {"method": SCHEMA, "linear_program_invocation_count": 11,
        "primary_LP_invocation_count": 11, "correction_LP_invocation_count": 0,
        "inherited_primary_LP_calls_not_executed_here": 11,
        "new_primary_LP_calls": 0, "nonlinear_minimize_invocation_count": 0,
        "counter_scope": "historical11 primary calls plus at most one newly started SOC",
        "shared_max_LPs": 12, "shared_max_values": 40, "shared_active_seconds": 120,
        "models": []}
    report = {"schema": SCHEMA, "status": "read-only-historical-input-ready",
        "github_sha": os.environ.get("GITHUB_SHA"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "source_files_sha256": implementation_hashes(), "configuration": copy.deepcopy(cfg),
        "exact_input_storage": prepared["bindings"],
        "direct_source": copy.deepcopy(prepared["source"]),
        "historical_case": copy.deepcopy(case["proof"]),
        "source_configuration_sha256": digest(cfg),
        "old_primary_LP_calls_this_run": 0, "old_optimizer_calls_this_run": 0,
        "old_developer_calls_this_run": 0,
        "prepare_elapsed_seconds": prepare_seconds,
        "same_original_reference163_coordinate_map_metric_b0_and_physical_box": True,
        "initial_historical_x": field.state_record(x),
        "fixed_historical_y": field.state_record(y),
        "full_value_sampling_definition": grid, "timing_segments": {},
        "scope": {
            "one_predeclared_historical_m10_failure_not_waiting_for_new_failures": True,
            "no_new_primary_solver_no_backtrack_no_recursive_SOC": True,
            "not_a_successor_of_latest_selected_best": True,
            "only_the_original_m10_center_is_the_acceptance_baseline": True,
            "new_ordinary_values_and_J_are_counted_not_claimed_as_saved_arrays": True,
            "x_initial_values_are_initialization_cost": True,
            "active_clock_starts_before_the_first_recovered_old_layout_J": True,
            "old_historical_active_clock_remaining_seconds_not_invented": True,
            "new_ordinary_calls_control_flow_bound_including_final_is_eight": True}}
    stage = {"status": "not-started", "error": None, "solver": ledger, "checkpoint": {}}
    report[STAGE] = stage

    def new_value_count():
        return 0 if objective is None else (
            int(objective.geometry_evaluations)+int(objective.fine_evaluations))

    def check_value_account():
        count = new_value_count()+independent_final_calls
        require(count <= 8 and 22+count <= int(cfg["max_physical_evaluations"]),
                "predeclared historical replay ordinary-value budget exceeded")
        return count

    def save(status):
        report["status"] = status
        report.update(elapsed_seconds=time.monotonic()-started,
            process_total_elapsed_seconds=time.monotonic()-process_started,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out, report)

    def snapshot_and_attach(status, error=None, budget=None):
        stage.update(status=status, error=error, budget_message=budget)
        if objective is not None:
            stage["checkpoint"] = objective.snapshot()
            stage["cross_center_norm_memory"] = objective.direction_bank.report()
            attach_complete_model_reports(stage, objective)
            stage.setdefault("inherited_scope_labels", {})[
                "frozen_outer_recovery_function_was_called_without_monkeypatch"] = stage.pop(
                    "frozen_outer_recovery_function_was_called_without_monkeypatch")
            stage["frozen_outer_recovery_function_was_called_without_monkeypatch"] = False
            stage["only_original_core_capture_rebuild_and_SOC_math_called"] = True
            core.attach_rebound_reports(stage, objective)
            for record in ledger["models"]:
                lp = record["linear_program"]
                lp.setdefault("inherited_scope_labels", {})["returned_prediction_source"] = lp.get(
                    "returned_prediction_source")
                lp.update(returned_prediction_source="not-applicable-no-new-primary-solver",
                          new_primary_LP_invocation_count=0)
        ledger["new_correction_LP_calls"] = ledger["correction_LP_invocation_count"]
        ledger["new_total_LP_calls"] = ledger["linear_program_invocation_count"]-11
        report["value_evaluation_counts"] = {
            "historical_values_through_original_failed_y_not_executed_again_as_optimizer": 22,
            "new_ordinary_objective_calls": new_value_count(),
            "new_independent_final_calls": independent_final_calls,
            "new_total_ordinary_calls": new_value_count()+independent_final_calls,
            "new_predeclared_bound": 8, "historical_plus_new_bound": 40,
            "directional_JVPs_and_selected_J_are_separately_accounted": True}
        report["optimization_active_seconds"] = (
            time.monotonic()-active_started if active_started is not None else 0.)
        save(status)

    save("historical-input-ready-before-new-geometry")
    try:
        objective = core.ExpandedPoolSOCObjective(
            field, gate, radial, theta, int(source_cfg["primitive_order"]),
            gate.coordinate_lower, gate.coordinate_upper, cfg=cfg, checkpoint=None,
            radial_nodes_exact=grid["radial_nodes_exact"],
            initial_direction_records=prepared["directions"], expanded_pool_policy=core.POLICY,
            expected_initial_bank_state_sha256=prepared["expected_bank_sha256"],
            expected_initial_bank_entries=9)
        # Restore the original published version offset before installing IDs.
        # No absent earlier row lists or evaluations are claimed to have run.
        objective.pool_version = source_model["coarse_pool_version"]-1
        objective.fine_pool_version = source_model["fine_pool_version"]-1
        objective.set_pool(case["old_pools"][0],
            {"kind": "published-m10-pretrial-complete-ID-list-restore",
             "historical_version": source_model["coarse_pool_version"]})
        objective.set_fine_pool(case["old_pools"][1],
            {"kind": "published-m10-pretrial-complete-ID-list-restore",
             "historical_version": source_model["fine_pool_version"]})
        old_versions = (objective.pool_version, objective.fine_pool_version)
        require(old_versions == (4, 7), "historical pool versions did not restore")
        init = time.monotonic()
        xc = objective.evaluate(objective.vector(x))["decision"]
        xf = objective.fine_decision(x)
        check_value_account()
        report["x_original_value_comparison"] = check_decisions(
            xc, xf, case["x_trial"]["coarse_decision"], case["x_trial"]["fine_decision"])
        require(xc["single_grid_admissible_recovery_point"] and
                xf["single_grid_admissible_recovery_point"], "historical x lost its original hard gates")
        point = objective.accepted_point(x, xc, xf,
            {"kind": "exact-published-model10-base-no-new-primary-solve",
             "original_accepted_index": 7})
        objective.install_reference(x)
        old_eta = float(point["maximum_eta_on_both_grids"])
        report["initial_current_constraints"] = copy.deepcopy(xc)
        report["initial_doubled_constraints"] = copy.deepcopy(xf)
        report["timing_segments"]["x_ordinary_initialization_seconds"] = time.monotonic()-init
        stage["checkpoint"] = objective.snapshot()
        save("historical-x-original-two-grid-gates-recovered")
        objective.begin_optimization()
        active_started = objective.optimization_started
        wall = objective._wall
        remaining = lambda: float(cfg["max_seconds"])-(time.monotonic()-active_started)
        wall()
        tick = time.monotonic()
        base, J, groups, tols = objective.linear_rows(objective.vector(x))
        primary = frozen_outer.selected_model(objective, x, base, J, groups, tols, trust, cfg)
        affine = objective.primary_observable_model(primary)
        affine.oracle.set_post_primary_phase()
        binding = frozen_outer.model_binding(
            primary, x, case["proof"]["x_physical_sha256"], old_versions)
        report["historical_model_identity"] = verify_historical_model(
            primary, affine, binding, source_model)
        report["original_bank_replay"] = copy.deepcopy(objective.initial_bank_replay)
        report["timing_segments"]["old_layout_J_and_two_factory_restore_seconds"] = time.monotonic()-tick
        require(objective.initial_bank_replay["passed"], "nine-entry bank recovery not passed")
        wall()
        model = {"number": 10, "source_model_number": 10,
            "linearized_at_accepted_index": point["accepted_index"],
            "source_linearized_at_accepted_index": 7,
            "linearized_at_physical_sha256": point["physical_state_sha256"],
            "coarse_pool_rows": len(objective.pool), "fine_pool_rows": len(objective.fine_pool),
            "coarse_pool_version": old_versions[0], "fine_pool_version": old_versions[1],
            "trust_before_model": trust, "SOC_hold_model_binding": copy.deepcopy(binding),
            "original_historical_SOC_hold_model_binding": copy.deepcopy(source_model["SOC_hold_model_binding"]),
            "linear_program": {"status": "historical-primary-read-not-solved",
                "LP_invoked": False, "new_primary_LP_invocation_count": 0},
            "trials": [], "corrections": [], "scale_feedback_trials": [],
            "result": "fixed-failed-y-not-yet-recovered"}
        ledger["models"].append(model)
        tick = time.monotonic()
        yr = objective.evaluate(objective.vector(y)); yc = yr["decision"]
        yf = objective.fine_decision(y)
        check_value_account()
        report["y_original_value_comparison"] = check_decisions(
            yc, yf, source_trial["coarse_decision"], source_trial["fine_decision"])
        require(not (yc["single_grid_admissible_recovery_point"] and
                     yf["single_grid_admissible_recovery_point"]),
                "the old failed trial is no longer a rejected original-gate point")
        trial = copy.deepcopy(source_trial)
        trial["historical_coarse_residual_evaluation"] = trial["coarse_physical_evaluation"]
        trial["historical_fine_residual_evaluation"] = trial["fine_value_evaluation"]
        trial.update(coarse_physical_evaluation=yr["physical_geometry_evaluation"],
            fine_value_evaluation=objective.fine_evaluations,
            coarse_decision=frozen_outer.compact_with_all_actual_gates(yc),
            fine_decision=frozen_outer.compact_with_all_actual_gates(yf),
            historical_trial_recovered_without_primary_optimization=True)
        addc, dc = objective.expand_pool(objective.vector(y),
            "recovered-original-m10-failed-y-coarse-separation")
        addf, df = objective.learn_fine_violations(y,
            "recovered-original-m10-failed-y-fine-separation")
        require(addc is not None and addf is not None and
                addc["added_row_indices"] == [72480] and
                addf["added_row_indices"] == [144960],
                "new actual separation did not recover the two original learned IDs")
        require(objective.pool.tolist() == case["new_pools"][0] and
                objective.fine_pool.tolist() == case["new_pools"][1] and
                (objective.pool_version, objective.fine_pool_version) == (5, 8),
                "actual post-y complete pools differ from the historical arrays")
        for label, detail in (("coarse", dc), ("fine", df)):
            require(detail["omitted_violating_count"] == trial[label+"_omitted_rows"] and
                    detail["omitted_hard_violating_count"] == trial[label+"_omitted_hard_rows"],
                    "historical learning counts changed")
        trial["new_coarse_rows"] = len(addc["added_row_indices"])
        trial["new_fine_rows"] = len(addf["added_row_indices"])
        model["trials"].append(trial)
        model["scale_feedback_trials"].append(copy.deepcopy(trial["scale_feedback"]))
        model["exact_binary64_independent_proposed_step"] = copy.deepcopy(
            source_model["exact_binary64_independent_proposed_step"])
        cache_restore = model.setdefault("failed_y_post_learning_cache_restore", {})
        restore_failed_y_layout(objective, y, cache_restore)
        check_value_account()
        failed = core.capture_failed_trial(objective, primary, x, y, old_versions,
                                          binding, 10, 0, trial, cfg)
        model["expanded_pool_same_failed_trial"] = copy.deepcopy(failed.report)
        model["actual_full_step_vs_original_proposal"] = {
            "exact_binary64_actual_y_minus_x": frozen_audit.coefficients(failed.step),
            "no_nominal_step_substitution": True}
        report["timing_segments"]["y_value_recovery_and_original_separation_seconds"] = time.monotonic()-tick
        stage["checkpoint"] = objective.snapshot()
        save("historical-y-and-both-exact-expanded-pools-recovered")
        wall()
        rebind_before = [objective.geometry_evaluations, objective.fine_evaluations]
        cache_before = [objective.accepted_coarse_cache_restores, objective.accepted_fine_cache_restores]
        try:
            ctx = objective.rebuild_failed_context(failed, trust, cfg)
        finally:
            rebind_after = [objective.geometry_evaluations, objective.fine_evaluations]
            cache_after = [objective.accepted_coarse_cache_restores, objective.accepted_fine_cache_restores]
            report["rebound_accepted_value_cache_reuse"] = {
                "new_ordinary_counts_before": rebind_before,
                "new_ordinary_counts_after": rebind_after,
                "new_ordinary_calls_during_rebind":
                    [b-a for a, b in zip(rebind_before, rebind_after)],
                "accepted_cache_restore_counter_increments":
                    [b-a for a, b in zip(cache_before, cache_after)],
                "zero_extra_ordinary_calls_observed": rebind_before == rebind_after,
                "pool_version_change_invalidates_selected_J_not_saved_ordinary_values": True}
        require(rebind_before == rebind_after,
                "saved exact-x ordinary caches did not restore; declared eight-value replay stopped")
        check_value_account()
        model["expanded_pool_rebound_registry_index"] = ctx.record["rebound_context_index"]
        budget = core.rebound_budget(ctx, cfg)
        model["expanded_pool_rebound_budget"] = copy.deepcopy(budget)
        wall()
        if not budget["finite_and_both_original_positive_gain_gates"]:
            model["result"] = "historical-rebound-has-no-original-positive-scalar-and-complete-gain"
            result_status = "complete-historical-m10-rebound-stopped-before-SOC"
        else:
            core.require_current_layout(objective, failed)
            soc = {}
            correction = {"primary_trial_index": 0,
                "primary_trial_physical_sha256": trial["physical_state_sha256"],
                "coarse_residual_evaluation": trial["coarse_physical_evaluation"],
                "fine_residual_evaluation": trial["fine_value_evaluation"],
                "coarse_pool_version": ctx.versions[0], "fine_pool_version": ctx.versions[1],
                "expanded_pool_rebound_revision": 1,
                "rebound_model_binding": copy.deepcopy(ctx.binding),
                "rebound_complete_model_binding_sha256": ctx.affine.binding_sha256,
                "original_primary_model_binding": copy.deepcopy(binding),
                "same_failed_y_and_original_learning_preserved": True, "linear_program": soc}
            model["corrections"].append(correction)
            w, soc = core.solve_rebound_correction(ctx.primary, failed.views, failed.step,
                cfg, ledger, progress=soc, wall=wall, remaining_seconds=remaining)
            require(ledger["linear_program_invocation_count"] <= 12 and
                    ledger["correction_LP_invocation_count"] <= 1,
                    "more than the unique historical remaining SOC slot was consumed")
            soc["same_step_scalar_and_affine_budget_comparison"] = {
                "scalar_rho_source": "new selected minimum at actual y-x in frozen build_correction",
                "minimum_scalar_slack_at_same_step": budget["new_scalar_slack_at_actual_d"],
                "evaluated_affine_spectral_slack_at_same_step": budget["new_full_slack_at_actual_d"],
                "original_SOC_rhs_if_built": soc.get("metric_slack_budget"),
                "hypothetical_affine_rhs_not_used": budget["hypothetical_full_SOC_rhs_not_used"],
                "selected_initial_slack_retained": budget["new_scalar_initial_slack"],
                "full_initial_slack_retained": budget["new_full_initial_slack"],
                "rebound_complete_model_binding_sha256": ctx.affine.binding_sha256,
                "primary_LP_auxiliary_not_substituted": True,
                "original_rhs_and_original_unit_primal_residual_gate_unchanged": True}
            ctx.record.update(status="historical-rebound-correction-returned",
                correction_index=0, correction_LP_invoked=bool(soc.get("LP_invoked")))
            stage["checkpoint"] = objective.snapshot()
            save("unique-historical-m10-SOC-returned")
            wall()
            if w is None:
                model["result"] = "historical-rebound-no-qualified-correction-x-retained"
                result_status = "complete-historical-m10-SOC-rejected-before-z"
            else:
                correction["exact_binary64_independent_correction"] = frozen_audit.coefficients(w)
                core.require_current_layout(objective, failed)
                z = objective.subspace.apply(y, w[objective.subspace.columns])
                zc, zf, corrected, accepted = assess_corrected(
                    objective, z, ctx, model, old_eta, cfg)
                check_value_account()
                correction["corrected_trial_index"] = len(model["trials"])-1
                correction["corrected_trial_physical_sha256"] = corrected["physical_state_sha256"]
                correction["corrected_trial_added_rows"] = {
                    "coarse": corrected.get("new_coarse_rows", 0),
                    "fine": corrected.get("new_fine_rows", 0)}
                model["original_failed_trial_learning_not_erased_for_SOC_hold"] = True
                if accepted:
                    model["result"] = "accepted-historical-m10-expanded-SOC-two-grid-descent"
                    model["accepted_expanded_pool_same_trial_SOC"] = True
                    model["accepted_rebound_SOC_base_total_step_diagnostic"] = frozen_outer.actual_total_step_diagnostic(
                        ctx.primary, x, y, z, old_eta, zc, zf, cfg=cfg,
                        model_context=ctx.binding,
                        base_physical_sha256=case["proof"]["x_physical_sha256"],
                        primary_physical_sha256=case["proof"]["y_physical_sha256"],
                        accepted_physical_sha256=corrected["physical_state_sha256"],
                        current_pool_versions=(objective.pool_version, objective.fine_pool_version))
                    result_status = "complete-historical-m10-expanded-SOC-accepted"
                else:
                    model["result"] = "historical-m10-corrected-point-rejected-x-retained"
                    result_status = "complete-historical-m10-expanded-SOC-z-rejected"
        next_trust, next_streak, feedback = frozen_outer.next_soc_hold_trust(
            model, trust, case["streak"], cfg)
        model["scale_feedback_update"] = feedback
        objective.trust_updates.append(copy.deepcopy(feedback))
        require(not feedback["successful_SOC_radius_retention"]["qualified_to_retain_model_radius"],
                "original nonzero learning cannot become an unchanged-layout hold witness")
        stage["last_restricted_trust"] = next_trust
        stage["final_consecutive_growth_qualifying_models"] = next_streak
        point = objective.accepted_iterates[-1]
        selected = transfer.exact_binary_vector(point["exact_binary64_independent_coordinates"], 159)
        require(field.coordinates.physical_exact(selected) ==
                tuple(Q(v) for v in point["exact_original_physical_coefficients"]) and
                digest(field.identity(selected)) == point["physical_state_sha256"],
                "last genuinely accepted exact physical point changed")
        require(field.coordinates.exact_box_decision(
            selected, gate.original_lower, gate.original_upper)["exact_original_box_pass"],
            "final exact original physical box failed")
        wall()
        require(check_value_account()+2 <= 8, "no room for declared independent final values")
        final_decisions = []
        final_started = time.monotonic()
        for th in (theta, objective.fine_theta):
            wall()
            independent_final_calls += 1
            data = field.geometry(selected, radial, th, int(source_cfg["primitive_order"]))
            dec = frozen_audit.recovery_decision(
                field, gate, selected, data, gate.coordinate_lower, gate.coordinate_upper, cfg)
            final_decisions.append(dec)
            check_value_account()
        report["timing_segments"]["independent_final_two_grid_seconds"] = time.monotonic()-final_started
        fc, ff = final_decisions
        require(fc["single_grid_admissible_recovery_point"] and
                ff["single_grid_admissible_recovery_point"],
                "independent final original hard gates did not confirm the accepted point")
        maximum = max(fc["direct_max_eta"], ff["direct_max_eta"])
        require(abs(maximum-point["maximum_eta_on_both_grids"]) <= 5e-10,
                "independent same-state final eta changed")
        report["final_full_grid_constraints"] = fc
        report["final_doubled_constraints"] = ff
        report["final_state"] = field.state_record(selected)
        report["final_selection_validation"] = {
            "both_value_grids_hard_and_old_metric_pass": True,
            "exact_original_physical_box_checked_without_clipping": True,
            "historical_x_both_grid_eta": old_eta, "selected_both_grid_eta": maximum,
            "decrease_relative_to_historical_x_only": old_eta-maximum,
            "new_SOC_point_accepted": bool(model.get("accepted_expanded_pool_same_trial_SOC")),
            "new_target_qualified_on_both_grids":
                bool(fc["single_grid_new_target_qualified"] and ff["single_grid_new_target_qualified"]),
            "maximum_curvature_on_both_grids": max(
                fc["direct_maximum_absolute_principal_curvature"],
                ff["direct_maximum_absolute_principal_curvature"]),
            "not_claimed_better_than_the_later_current_global_best": True,
            "finite_two_grid_gates_not_continuous_embedding_or_whole_reach": True}
        report["future_direct_checkpoint"] = {
            "reference_complete163_binary64_exact":
                [str(Q.from_float(float(v))) for v in field.coordinates.reference_state],
            "coordinate_definition": copy.deepcopy(field.coordinate_definition),
            "selected_final159_binary64_exact": frozen_audit.coefficients(selected),
            "selected_final163_physical_exact": [str(v) for v in field.coordinates.physical_exact(selected)],
            "selected_physical_state_sha256": digest(field.identity(selected)),
            "coarse_pool": objective.pool.tolist(), "fine_pool": objective.fine_pool.tolist(),
            "terminal_trust": next_trust, "terminal_success_streak": next_streak,
            "norm_direction_bank_context": copy.deepcopy(objective.direction_bank.context),
            "norm_direction_bank_entries": copy.deepcopy(list(objective.direction_bank.entries.values())),
            "norm_direction_bank_state_sha256": objective.direction_bank.state_digest(),
            "historical_branch_not_automatically_the_current_warm_start": True}
        wall()
        snapshot_and_attach(result_status)
    except frozen_outer.EvaluationBudgetReached as error:
        snapshot_and_attach("partial-historical-m10-budget-exit", budget=str(error))
    except Exception as error:
        detail = {"type": type(error).__name__, "message": str(error),
                  "traceback": traceback.format_exc()}
        try:
            snapshot_and_attach("historical-m10-error-last-valid-point-preserved", error=detail)
        except Exception as report_error:
            stage["error"] = detail
            report["secondary_report_error"] = {
                "type": type(report_error).__name__, "message": str(report_error)}
            save("historical-m10-original-error-with-secondary-report-failure")
    return report


def assess_corrected(objective, z, ctx, model, old_eta, cfg):
    """The frozen outer's original two-grid acceptance, exactly one new z."""
    core.require_current_layout(objective, ctx.failed)
    objective.problem.coordinates.validate(z)
    heights = objective.problem.coordinates.exact_heights(z)
    require(all(heights[j] == objective.problem.coordinates.reference_exact[j]
                for j in (4, 5)), "correction changed fixed physical height slots4 or5")
    record = {"kind": "metric-SOC-corrected-short-step", "alpha_exact": "1",
        "accepted_as_next_iterate": False, "attempt_status": "coarse-value-call-started",
        "physical_state_sha256": digest(objective.problem.identity(z)),
        "exact_binary64_independent_coordinates": frozen_audit.coefficients(z),
        "exact_original_physical_coefficients":
            [str(v) for v in objective.problem.coordinates.physical_exact(z)],
        "expanded_pool_rebound_revision": 1,
        "rebound_complete_model_binding_sha256": ctx.affine.binding_sha256,
        "rebound_model_binding": copy.deepcopy(ctx.binding)}
    model["trials"].append(record)
    rv = objective.evaluate(objective.vector(z))
    coarse = rv["decision"]
    record.update(attempt_status="coarse-value-call-complete",
        coarse_physical_evaluation=rv["physical_geometry_evaluation"],
        coarse_decision=frozen_outer.compact_with_all_actual_gates(coarse))
    fine = None
    accepted = False
    # This sole corrected point receives the full fine decision whenever regular.
    # No gate is relaxed because it is historical or because the SOC LP succeeded.
    if coarse.get("regularity_screen_pass", False):
        fine = objective.fine_decision(z)
        record.update(fine_value_evaluation=objective.fine_evaluations,
            fine_decision=frozen_outer.compact_with_all_actual_gates(fine),
            actual_fine_evaluated_even_if_coarse_ineligible=
                not coarse["single_grid_admissible_recovery_point"])
        maximum = max(coarse["direct_max_eta"], fine["direct_max_eta"])
        qualified = coarse["single_grid_new_target_qualified"] and fine["single_grid_new_target_qualified"]
        drop = float(Q(cfg["minimum_accepted_eta_decrease_exact"]))
        if (coarse["single_grid_admissible_recovery_point"] and
                fine["single_grid_admissible_recovery_point"] and maximum < old_eta and
                (old_eta-maximum >= drop or qualified)):
            point = objective.accepted_point(z, coarse, fine,
                {"kind": record["kind"], "model": 10, "alpha_exact": "1",
                 "previous_two_grid_maximum_eta": old_eta,
                 "historical_base_original_accepted_index": 7})
            record.update(accepted_as_next_iterate=True, accepted_index=point["accepted_index"])
            accepted = True
    record["restricted_support_invariants"] = objective.invariant_diagnostic(
        z, fine_present=fine is not None)
    record["curvature_nonlinear_defect_diagnostic"] = frozen_outer.curvature_trial_diagnostics(
        objective, z, ctx.trial_rows, ctx.J, ctx.groups, ctx.failed.y,
        "same-primary-y-actual-new-pool-rows-plus-rebuilt-x-J-correction",
        fine_present=fine is not None)
    record["affine_metric_error_decomposition"] = objective.actual_metric_error(
        ctx.affine, z, fine_present=fine is not None)
    added, detail = objective.expand_pool(objective.vector(z),
        "single-historical-m10-correction-original-coarse-separation")
    record.update(coarse_omitted_rows=detail["omitted_violating_count"],
        coarse_omitted_hard_rows=detail["omitted_hard_violating_count"],
        new_coarse_rows=len(added["added_row_indices"]) if added else 0)
    if detail.get("pool_capacity_would_be_exceeded"):
        raise frozen_outer.EvaluationBudgetReached("coarse capacity after sole corrected value; last accepted retained")
    if fine is not None:
        added_f, detail_f = objective.learn_fine_violations(z,
            "single-historical-m10-correction-original-fine-separation")
        record.update(fine_omitted_rows=detail_f["omitted_violating_count"],
            fine_omitted_hard_rows=detail_f["omitted_hard_violating_count"],
            fine_violation_groups=detail_f["group_counts"],
            new_fine_rows=len(added_f["added_row_indices"]) if added_f else 0)
        if detail_f.get("pool_capacity_would_be_exceeded"):
            raise frozen_outer.EvaluationBudgetReached("fine capacity after sole corrected value; last accepted retained")
    # Rejected new-row z has no further correction. An accepted z keeps the
    # original acceptance rule; its learning still prevents a radius hold.
    prediction = {"predicted_slack": ctx.affine.slack(z-ctx.failed.x),
        "model_kind": "accepted-base-affine-e-f-spectral-norm-at-actual-total-step",
        "observable_binding_sha256": ctx.affine.binding_sha256,
        "pool_versions": list(ctx.versions), "full_fine_actual_required_for_eta_ratio": True,
        "expanded_pool_rebound_revision": 1}
    record["scale_feedback"] = frozen_outer.trial_quality(
        old_eta, coarse, fine, prediction, record["kind"], cfg)
    model["scale_feedback_trials"].append(copy.deepcopy(record["scale_feedback"]))
    return coarse, fine, record, accepted


def print_result(report):
    stage = report.get(STAGE, {})
    for model in stage.get("solver", {}).get("models", []):
        emit("M10_SOC_MODEL", model)
    summary = compact_report(report)
    emit("M10_SOC_SUMMARY", summary)
    # Full exact coordinates, IDs and all mathematical reports remain only in
    # this public job log and runner temporary files, never a repository blob.
    emit("M10_SOC_COMPLETE", report)
    payload = reader.encoded(report)
    emit("M10_SOC_REPORT_METADATA", {"schema": SCHEMA, "bytes": len(payload),
        "sha256": reader.digest(payload), "payload_storage": "runner-temporary-and-job-stdout-only"})


def main():
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == REPO,
            "new developer and scientific execution only in the public repository Actions")
    request = json.loads(args.request.read_text(encoding="utf-8"))
    require(request["request"] == SCHEMA, "explicit observed-m10-only request required")
    for path, expected in request["source_sha256"].items():
        require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected,
                "new requested source differs: "+path)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    reused = reuse_completed_checks(request)
    emit("M10_SOC_PRIOR_CHECKS_REUSED", reused)
    reused_seven = reuse_completed_m10_checks(request)
    emit("M10_SOC_PRIOR_EXTRACTION_REUSED", reused_seven)
    reused_negative = reuse_completed_cache_miss_check(request)
    emit("M10_SOC_CACHE_NEGATIVE_REUSED", reused_negative)
    import frame_metric_observed_m10_cache_development as development
    check = development.developer_check(reused_negative)
    check["source_files_sha256"] = implementation_hashes()
    emit("M10_SOC_CACHE_DEVELOPMENT", check)
    require(check.get("passed") is True and check.get("all_passed") is True,
            "new post-learning cache reinstallation/capture checks failed")
    try:
        prepared = prepare_case(request,
            args.out.parent/"original24-read-only-preparation.json", started)
        emit("M10_SOC_HISTORICAL_CASE", prepared["case"]["proof"])
        report = run_case(prepared, args.out, process_started=started,
                          prepare_seconds=time.monotonic()-started)
    except Exception as error:
        report = {"schema": SCHEMA, "status": "historical-m10-input-recovery-error",
            "source_files_sha256": implementation_hashes(),
            "old_optimizer_calls_this_run": 0, "old_primary_LP_calls_this_run": 0,
            "error": {"type": type(error).__name__, "message": str(error),
                      "traceback": traceback.format_exc()},
            "process_total_elapsed_seconds": time.monotonic()-started}
        save_report(args.out, report)
        print_result(report)
        raise
    print_result(report)
    require(report["status"].startswith("complete-historical-m10-") and
            report.get("final_selection_validation", {}).get(
                "both_value_grids_hard_and_old_metric_pass") is True,
            "historical one-shot SOC did not complete with independently rechecked original gates")


if __name__ == "__main__":
    main()

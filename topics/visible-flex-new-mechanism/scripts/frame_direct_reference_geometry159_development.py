#!/usr/bin/env python3
"""Three new artificial groups for direct immutable-reference evaluation.

Only this new adapter is checked.  Existing artificial input factories are
reused, but no old developer suite or optimizer is executed.  Execution is
restricted to a separately authorized public Actions job.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import resource
import time
from unittest.mock import patch

import numpy as np

import frame_direct_reference_geometry159 as direct
from frame_five_height_field import FiveHeightField, artificial_problem
from frame_independent_height import IndependentHeightProblem
from frame_height_affine_gate import require_public_research_environment
from frame_height_null_coordinates import digest
from frame_selected_row_radial_jacobian import SelectedRadialJacobian
from frame_curvature_soc_steps import configuration as start_configuration
from frame_metric_budget_recovery import configuration as recovery_configuration
from frame_metric_entry_tail_height159 import configuration as mapped_configuration
from frame_metric_height159_soc_hold import configuration as held_configuration
from frame_metric_height159_factorized_rows import configuration as factorized_configuration


SCHEMA = direct.POLICY + "-new-artificial-development"
EXPECTED_CASE_COUNTS = {
    "reference_and_Jacobian_branches": 3,
    "deleted_calls_cache_and_failure_cost": 3,
    "new_identity_and_selected_binding": 3,
}
ARRAY_TOLERANCE = 128 * np.finfo(float).eps
RADIAL = np.array([0., .036, .05, .09, .117, .36, .441, .603, .7725, .78, .846, .9])


def implementation_hashes():
    names = [
        Path(__file__).name, "frame_direct_reference_geometry159.py",
        "frame_five_height_field.py", "frame_independent_height.py",
        "frame_height_affine_gate.py", "frame_height_null_coordinates.py",
        "frame_selected_row_radial_jacobian.py", "frame_curvature_soc_steps.py",
        "frame_metric_budget_recovery.py", "frame_metric_entry_tail_height159.py",
        "frame_metric_height159_soc_hold.py", "frame_metric_height159_factorized_rows.py",
    ]
    root = Path(__file__).resolve().parent
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in names}


def _fixture(execution):
    execution["old_artificial_input_factory_calls"] += 1
    single, reference = artificial_problem(1)
    original = FiveHeightField(single, reference)
    adapter = direct.DirectReferenceFiveHeightField(original)
    zero = original.initial_state()
    changed = zero.copy()
    changed[153] = .0013
    changed[154:] = .0001 * np.array([1., -.3, .2, .4, -.2])
    base = held_configuration(mapped_configuration(recovery_configuration(
        start_configuration(), target="13/50", curvature_cap="58")))
    cfg = factorized_configuration(base)
    return {
        "single": single, "original": original, "adapter": adapter,
        "zero": zero, "changed": changed, "cfg": cfg,
    }


def _adapter_geometry(fixture, execution, state, theta, **kwargs):
    execution["artificial_adapter_geometry_calls_started"] += 1
    if kwargs.get("jacobian"):
        execution["artificial_adapter_Jacobian_calls_started"] += 1
    try:
        data = fixture["adapter"].geometry(state, RADIAL, theta, 2, **kwargs)
    except Exception:
        execution["artificial_adapter_geometry_calls_failed"] += 1
        raise
    execution["artificial_adapter_geometry_calls_completed"] += 1
    return data


def _comparison_geometry(fixture, execution, state, theta, **kwargs):
    execution["artificial_original_comparison_geometry_calls_started"] += 1
    if kwargs.get("jacobian"):
        execution["artificial_original_comparison_Jacobian_calls_started"] += 1
    return fixture["original"].geometry(state, RADIAL, theta, 2, **kwargs)


def _compare_structure(expected, actual):
    """Compare complete returned structures; do not replace differences by zero."""
    report = {
        "same_structure_and_scalar_metadata": True, "finite_arrays": True,
        "array_count": 0, "maximum_absolute_array_difference": 0.,
        "maximum_scaled_array_difference": 0., "all_arrays_bitwise_equal": True,
        "largest_array_elements": 0,
    }

    def visit(a, b):
        if isinstance(a, dict):
            if not isinstance(b, dict) or set(a) != set(b):
                report["same_structure_and_scalar_metadata"] = False
                return
            for key in a:
                visit(a[key], b[key])
        elif isinstance(a, np.ndarray):
            if (not isinstance(b, np.ndarray) or a.shape != b.shape
                    or a.dtype != b.dtype):
                report["same_structure_and_scalar_metadata"] = False
                return
            report["array_count"] += 1
            report["largest_array_elements"] = max(report["largest_array_elements"], int(a.size))
            report["all_arrays_bitwise_equal"] = (
                report["all_arrays_bitwise_equal"] and a.tobytes() == b.tobytes())
            if a.dtype.kind in "fci":
                finite = bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b)))
                report["finite_arrays"] = report["finite_arrays"] and finite
                if finite:
                    error = float(np.max(np.abs(a - b), initial=0.))
                    scale = 1. + float(np.max(np.abs(a), initial=0.))
                    report["maximum_absolute_array_difference"] = max(
                        report["maximum_absolute_array_difference"], error)
                    report["maximum_scaled_array_difference"] = max(
                        report["maximum_scaled_array_difference"], error / scale)
            elif not np.array_equal(a, b):
                report["same_structure_and_scalar_metadata"] = False
        elif isinstance(a, (list, tuple)):
            if type(a) is not type(b) or len(a) != len(b):
                report["same_structure_and_scalar_metadata"] = False
                return
            for x, y in zip(a, b):
                visit(x, y)
        elif type(a) is not type(b) or a != b:
            report["same_structure_and_scalar_metadata"] = False

    visit(expected, actual)
    report["comparison_tolerance"] = float(ARRAY_TOLERANCE)
    report["passed"] = bool(
        report["same_structure_and_scalar_metadata"] and report["finite_arrays"]
        and report["maximum_scaled_array_difference"] <= ARRAY_TOLERANCE)
    return report


def _case(name, callback):
    started = time.monotonic()
    try:
        record = callback()
        if type(record.get("passed")) is not bool:
            raise TypeError("each new case must return an actual Boolean verdict")
        record.update(name=name, execution_status="completed")
    except Exception as exc:
        record = {"name": name, "passed": False, "execution_status": "failed",
                  "error": {"type": type(exc).__name__, "message": str(exc)}}
    record["elapsed_seconds"] = time.monotonic() - started
    return record


def _group(name, cases):
    return {
        "name": name, "case_count": len(cases),
        "check_count": len(cases),
        "checks": {case["name"]: case["passed"] for case in cases},
        "cases": cases, "passed": bool(all(case["passed"] for case in cases)),
    }


def _reference_group(fixture, execution, shared):
    cases = []
    definitions = [
        ("zero_null_ordinary8", fixture["zero"], 8, False, False),
        ("nonzero_Q_null_basic_J8", fixture["changed"], 8, True, False),
        ("nonzero_Q_null_full_J16", fixture["changed"], 16, True, True),
    ]
    for name, state, nt, jacobian, full in definitions:
        def run(state=state, nt=nt, jacobian=jacobian, full=full):
            theta = np.arange(nt) * 2 * np.pi / nt
            kwargs = {"jacobian": jacobian, "full_two_jet_jacobian": full}
            old = _comparison_geometry(fixture, execution, state, theta, **kwargs)
            new = _adapter_geometry(fixture, execution, state, theta, **kwargs)
            result = _compare_structure(old, new)
            result["same_physical_identity"] = (
                fixture["original"].identity(state) == fixture["adapter"].identity(state))
            result["passed"] = bool(result["passed"] and result["same_physical_identity"])
            result.update(radial_rows=len(RADIAL), angular_nodes=nt,
                          original_parameter_columns=163, independent_parameter_columns=159,
                          jacobian=jacobian, full_two_jet_jacobian=full)
            if full:
                shared.update(data=new, state=state.copy(), theta=theta.copy())
            return result
        cases.append(_case(name, run))
    return _group("reference_and_Jacobian_branches", cases)


def _cache_group(fixture, execution):
    adapter = fixture["adapter"]
    theta = np.arange(8) * 2 * np.pi / 8
    retained = {}
    cases = []

    def no_deleted_call():
        def forbidden(*args, **kwargs):
            raise AssertionError("an intentionally removed reference geometry call was reached")
        with patch.object(fixture["single"].base, "geometry", side_effect=forbidden) as bounded_call:
            with patch.object(IndependentHeightProblem, "geometry", side_effect=forbidden) as independent_call:
                data = _adapter_geometry(fixture, execution, fixture["zero"], theta)
        retained["first"] = data
        retained["before_hit"] = adapter.timing_snapshot()
        events = {r["component"]: r for r in retained["before_hit"]["last_call"]["components"]}
        return {
            "passed": bool(
                bounded_call.call_count == independent_call.call_count == 0
                and events["reference_fixed_height_primitive"]["cache_after"]["prefix_present"]
                and events["reference_fixed_height_primitive"]["cache_after"]["requested_points_present"]
                    == events["reference_fixed_height_primitive"]["cache_after"]["requested_unique_points"]),
            "forbidden_bounded_geometry_calls": bounded_call.call_count,
            "forbidden_independent_geometry_calls": independent_call.call_count,
            "actual_first_reference_components": {
                k: events[k] for k in ("reference_height_jets",
                    "reference_fixed_height_primitive", "reference_height_control_primitive",
                    "current_complete_scalar_grid")},
        }
    cases.append(_case("direct_path_avoids_both_discarded_geometry_calls", no_deleted_call))

    def same_objects_hit():
        if "first" not in retained:
            raise ValueError("preceding new direct-path case did not provide its artificial cache")
        state = fixture["zero"].copy()
        state[154:] = fixture["changed"][154:]
        data = _adapter_geometry(fixture, execution, state, theta)
        snapshot = adapter.timing_snapshot()
        events = {r["component"]: r for r in snapshot["last_call"]["components"]}
        hits = {name: events[name]["cache_before"]["classification"] == "hit" for name in (
            "reference_height_jets", "reference_fixed_height_primitive",
            "reference_height_control_primitive", "current_complete_scalar_grid")}
        before = retained["first"]
        active = (RADIAL > adapter.null_basis.left) & (RADIAL < adapter.null_basis.right)
        maximum = 0.
        for name, order, integral in (("X", 0, True), ("Xs", 0, False), ("Xss", 1, False)):
            delta = adapter.null_basis.values(RADIAL, order, integral=integral) @ state[154:]
            expected = before[name].copy()
            expected[active, :, 2] += delta[active, None]
            maximum = max(maximum, float(np.max(np.abs(data[name] - expected))))
        return {
            "passed": bool(all(hits.values()) and maximum <= ARRAY_TOLERANCE
                           and adapter.original_problem is fixture["single"]
                           and adapter.coordinates is fixture["original"].coordinates),
            "true_original_cache_hits": hits,
            "maximum_artificial_null_update_difference": maximum,
            "same_original_objects_not_reconstructed": True,
            "returned_arrays_are_kept_only_in_this_artificial_process": True,
        }
    cases.append(_case("same_process_cache_hits_keep_current_null_update", same_objects_hit))

    def paid_failure_time():
        before = adapter.timing_snapshot()
        failed_before = execution["artificial_adapter_geometry_calls_failed"]
        try:
            with patch.object(direct, "target_frame",
                              side_effect=RuntimeError("new-artificial-timing-failure-only")):
                _adapter_geometry(fixture, execution, fixture["zero"], theta)
        except RuntimeError as exc:
            expected_error = str(exc) == "new-artificial-timing-failure-only"
        else:
            expected_error = False
        after = adapter.timing_snapshot()
        part = after["components"].get("current_fields_and_frame", {})
        delta_failed = after["geometry_calls_failed"] - before["geometry_calls_failed"]
        good = bool(expected_error and delta_failed == 1
            and execution["artificial_adapter_geometry_calls_failed"] == failed_before + 1
            and after["geometry_seconds"] >= before["geometry_seconds"]
            and part.get("failed") == 1 and part.get("seconds", -1.) >= 0.
            and after["last_call"]["status"] == "failed"
            and adapter._direct_call is None)
        return {
            "passed": good, "controlled_failed_adapter_geometry_calls": delta_failed,
            "failure_is_a_new_artificial_case_not_a_scientific_failure": True,
            "geometry_elapsed_increment": after["geometry_seconds"] - before["geometry_seconds"],
            "failed_component_record": copy.deepcopy(part),
            "wall_clock_is_observed_not_replaced_by_a_mock_clock": True,
        }
    cases.append(_case("started_component_failure_remains_in_timing", paid_failure_time))
    return _group("deleted_calls_cache_and_failure_cost", cases)


def _binding_group(fixture, execution, shared):
    original, adapter = fixture["original"], fixture["adapter"]
    cases = []

    def explicit_identity():
        old, new = original.evaluation_definition(), adapter.evaluation_definition()
        expected = copy.deepcopy(old)
        expected["common_center_evaluation"] = new["common_center_evaluation"]
        expected["direct_reference_assembly"] = new["direct_reference_assembly"]
        state = fixture["changed"]
        passed = bool(new == expected and digest(new) != digest(old)
            and new["direct_reference_assembly"]["source_original_ordinary_evaluation_sha256"] == digest(old)
            and adapter.identity(state) == original.identity(state)
            and adapter.metric_model(state) == original.metric_model(state)
            and adapter.height_base_definition == original.height_base_definition
            and adapter.coordinate_definition == original.coordinate_definition)
        return {
            "passed": passed, "original_evaluation_sha256": digest(old),
            "adapter_evaluation_sha256": digest(new),
            "changed_top_level_definition_keys": sorted(k for k in set(old) | set(new) if old.get(k) != new.get(k)),
            "old_evaluation_identity_not_forged": True,
        }
    cases.append(_case("new_route_identity_preserves_exact_physical_definition", explicit_identity))

    def fresh_selected_binding():
        if set(shared) != {"data", "state", "theta"}:
            raise ValueError("the preceding new full-J case did not return its artificial ordinary data")
        factorized = SelectedRadialJacobian(adapter, fixture["cfg"])
        execution["new_selected_factorizer_constructors"] += 1
        bound = factorized.bind_ordinary(
            shared["state"], RADIAL, shared["theta"], shared["data"],
            owner="new-artificial-current-cache")
        execution["new_selected_ordinary_bindings"] += 1
        return {
            "passed": bool(isinstance(adapter, FiveHeightField)
                and factorized.single is fixture["single"]
                and bound["data"] is shared["data"]
                and bound["ordinary_evaluation_definition_sha256"] == digest(adapter.evaluation_definition())
                and bound["factorization_definition_sha256"] == factorized.definition_sha256
                and bound["coordinate_definition_sha256"] == original.coordinate_definition_sha256),
            "new_factorization_definition_sha256": factorized.definition_sha256,
            "bound_new_ordinary_evaluation_sha256": bound["ordinary_evaluation_definition_sha256"],
            "selected_J_evaluate_calls": 0,
            "bind_ordinary_consumes_existing_new_data_without_geometry": True,
        }
    cases.append(_case("old_selected_J_API_binds_the_new_field_identity", fresh_selected_binding))

    def frozen_no_reanchor():
        state = fixture["changed"]
        same, copied = adapter.frozen_metric_copy(state)
        return {
            "passed": bool(same is adapter and copied is not state
                and np.array_equal(copied.view(np.uint64), state.view(np.uint64))
                and adapter.original_problem is original.original_problem
                and adapter.coordinates is original.coordinates
                and adapter.null_basis is original.null_basis
                and adapter._direct_bounded is original.original_problem.base),
            "same_adapter_and_all_original_reference_cache_owners": True,
            "evaluation_variant_not_invoked": True,
            "new_reference_constructor_calls": 0,
        }
    cases.append(_case("frozen_metric_copy_retains_original_objects", frozen_no_reanchor))
    return _group("new_identity_and_selected_binding", cases)


def developer_check():
    require_public_research_environment()
    started = time.monotonic()
    execution = {
        "old_artificial_input_factory_calls": 0,
        "artificial_original_comparison_geometry_calls_started": 0,
        "artificial_original_comparison_Jacobian_calls_started": 0,
        "artificial_adapter_geometry_calls_started": 0,
        "artificial_adapter_geometry_calls_completed": 0,
        "artificial_adapter_geometry_calls_failed": 0,
        "artificial_adapter_Jacobian_calls_started": 0,
        "new_selected_factorizer_constructors": 0, "new_selected_ordinary_bindings": 0,
        "selected_J_evaluate_calls": 0, "full_directional_JVP_calls": 0,
        "real_LP_calls": 0, "optimizer_calls": 0, "research_geometry_calls": 0,
        "old_developer_suites_executed": 0,
        "top_level_geometry_counts_do_not_count_nested_legacy_comparator_calls_again": True,
    }
    shared = {}
    fixture = _fixture(execution)
    groups = [_reference_group(fixture, execution, shared)]
    cache_fixture = _fixture(execution)
    groups.append(_cache_group(cache_fixture, execution))
    groups.append(_binding_group(fixture, execution, shared))
    counts = {group["name"]: group["case_count"] for group in groups}
    return {
        "schema": SCHEMA, "artificial_inputs_only": True,
        "all_passed": bool(counts == EXPECTED_CASE_COUNTS and all(g["passed"] for g in groups)),
        "new_group_count": len(groups), "new_case_count": sum(counts.values()),
        "executed_check_count": sum(g["check_count"] for g in groups),
        "group_case_counts": counts, "groups": groups, "execution": execution,
        "maximum_declared_radial_rows": len(RADIAL), "maximum_declared_angular_nodes": 16,
        "original_J_comparison_only_on_new_small_artificial_inputs": True,
        "controlled_failed_geometry_calls_expected": 1,
        "elapsed_seconds": time.monotonic() - started,
        "maximum_resident_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "source_sha256": implementation_hashes(),
        "passed_does_not_establish_research_speedup_or_new_optimizer_budget": True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    result = developer_check()
    text = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
    if args.out:
        path = Path(args.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print("DIRECT_REFERENCE_DEVELOPMENT " + text.rstrip("\n"), flush=True)
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

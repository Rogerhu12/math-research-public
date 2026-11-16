#!/usr/bin/env python3
"""Only new final-slot eligibility, support append and ledger boundaries.

These fixtures do not construct geometry, call a real LP or run an old suite.
Their first execution is reserved for public Actions.
"""
from __future__ import annotations
import copy
import hashlib
from pathlib import Path
import time
import numpy as np

from frame_metric_terminal_paid_slot import (
    POLICY, validate_release, append_distinct_supports, _call_final_slot)


def _inputs():
    cfg = {"max_linear_models": 64, "max_physical_evaluations": 160,
           "max_seconds": 1800, "linear_program_seconds": 10,
           "linear_model_improvement_floor": 1e-12}
    ledger = {"linear_program_invocation_count": 63,
              "primary_LP_invocation_count": 62, "correction_LP_invocation_count": 1,
              "nonlinear_minimize_invocation_count": 0}
    model = {
        "number": 28, "result": "no-evaluated-affine-spectral-improvement",
        "trials": [], "corrections": [],
        "linear_program": {
            "returned_candidate": False, "returned_epigraph_gap_met": False,
            "returned_inexact_cut_model": True,
            "proposal_rejected_before_geometry":
                "no-evaluated-affine-model-improvement-above-original-floor",
            "status": "new-task-pair-allocation-primary-ceiling-reached",
            "new_task_shared_LP_limit_exhausted": False,
            "inner_call_count": 1, "predicted_slack_improvement": -1e-5,
            "inner_LPs": [{"shared_LP_ordinal": 63, "status": "evaluated-affine-candidate",
                          "gap_met": False, "raw_epigraph_gap": 2e-5,
                          "gap_tolerance": 1e-9, "evaluated_model_improvement": -1e-5}],
            "cut_rounds": [{"rows": 516}], "initial_rebuilt_memory_rows": 516,
            "total_new_cut_rows": 516,
            "primary_SOC_pair_allocation": {
                "shared_LP_limit": 64, "started_shared_LPs_before_primary": 62,
                "remaining_shared_LPs_before_primary": 2, "primary_inner_calls_granted": 1,
                "scoped_primary_absolute_ceiling": 63, "charged_primary_LPs": 1,
                "remaining_shared_LPs_after_primary": 1, "source_cfg_unchanged": True}}}
    return cfg, ledger, model


def _rejected(call):
    try:
        call()
    except ValueError:
        return True
    return False


def _group_release():
    checks = {}
    cfg, ledger, source = _inputs()
    frozen = copy.deepcopy((cfg, ledger, source))
    decision = validate_release(source, cfg, ledger)
    checks["same_paid_nonimproving_inexact_terminal_releases_only_slot64"] = (
        decision["eligible"] and decision["released_shared_LP_ordinal"] == 64
        and decision["maximum_new_primary_LPs"] == 1
        and decision["new_candidate_has_no_SOC_budget"]
        and (cfg, ledger, source) == frozen)
    changed = copy.deepcopy(source)
    changed["trials"] = [{"accepted_as_next_iterate": False}]
    checks["any_source_physical_trial_refuses_the_terminal_release"] = _rejected(
        lambda: validate_release(changed, cfg, ledger))
    changed = copy.deepcopy(source)
    changed["linear_program"]["returned_epigraph_gap_met"] = True
    checks["completed_gap_cannot_use_the_inexact_terminal_rule"] = _rejected(
        lambda: validate_release(changed, cfg, ledger))
    changed_ledger = dict(ledger, linear_program_invocation_count=64)
    checks["already_spent_slot64_is_never_reset_or_reassigned"] = _rejected(
        lambda: validate_release(source, cfg, changed_ledger))
    return checks


def _ready_progress(distinct=1):
    return {"terminal_slot_release": {
        "eligible": True, "status": "new-supports-prepared",
        "append": {"distinct_new_rows": distinct}}}


def _group_supports():
    checks = {}
    old_A = np.array([[1., -1., 0.], [1., -1., 0.]])
    old_b = np.array([.1, .1])
    new_A = np.array([[1., -1., 0.], [2., -1., 0.], [2., -1., 0.]])
    new_b = np.array([.1, .2, .2])
    A, b, r = append_distinct_supports(old_A, old_b, new_A, new_b)
    checks["old_duplicates_retained_and_new_distinct_support_appended_once"] = (
        np.array_equal(A[:2], old_A) and np.array_equal(b[:2], old_b)
        and r["kept_new_indices"] == [1] and r["duplicate_new_indices"] == [0, 2]
        and r["distinct_new_rows"] == 1 and r["combined_rows"] == 3)
    A, b, r = append_distinct_supports(old_A, old_b, old_A, old_b)
    cfg, ledger, _ = _inputs()
    called = []
    checks["duplicate_only_bundle_keeps_the_last_slot_unstarted"] = (
        r["distinct_new_rows"] == 0
        and np.array_equal(A, old_A) and np.array_equal(b, old_b)
        and _rejected(lambda: _call_final_slot(
            cfg, ledger, _ready_progress(0), lambda: called.append(True)))
        and called == [] and ledger["linear_program_invocation_count"] == 63)
    broken = new_A.copy()
    broken[0, 0] = float("nan")
    checks["nonfinite_new_support_is_refused_before_any_call"] = _rejected(
        lambda: append_distinct_supports(old_A, old_b, broken, new_b))
    return checks


def _group_accounting(execution):
    checks = {}
    cfg, ledger, _ = _inputs()
    progress = _ready_progress()
    saved_cfg = copy.deepcopy(cfg)

    def charged_return():
        execution["new_stub_callbacks_started"] += 1
        ledger["linear_program_invocation_count"] += 1
        ledger["primary_LP_invocation_count"] += 1
        return "stub-candidate"
    result = _call_final_slot(cfg, ledger, progress, charged_return)
    r = progress["terminal_slot_release"]
    checks["one_started_primary_is64_and_SOC_budget_is_zero"] = (
        result == "stub-candidate" and ledger["linear_program_invocation_count"] == 64
        and ledger["primary_LP_invocation_count"] == 63
        and ledger["correction_LP_invocation_count"] == 1
        and r["new_started_primary_LPs"] == 1 and r["new_started_SOC_LPs"] == 0
        and r["original_shared_slots_left"] == 0 and cfg == saved_cfg)

    second = []
    checks["same_final_slot_cannot_be_invoked_twice"] = _rejected(
        lambda: _call_final_slot(cfg, ledger, progress, lambda: second.append(True))) and second == []

    cfg, ledger, _ = _inputs()
    progress = _ready_progress()

    def charged_raise():
        execution["new_stub_callbacks_started"] += 1
        ledger["linear_program_invocation_count"] += 1
        ledger["primary_LP_invocation_count"] += 1
        raise RuntimeError("new stub: after-start failure")
    message = None
    try:
        _call_final_slot(cfg, ledger, progress, charged_raise)
    except RuntimeError as error:
        message = str(error)
    r = progress["terminal_slot_release"]
    checks["after_start_exception_keeps_the_paid64_ledger_and_original_error"] = (
        message == "new stub: after-start failure"
        and ledger["linear_program_invocation_count"] == 64
        and r["new_started_primary_LPs"] == 1
        and r["error"]["message"] == message and r["source_cfg_unchanged"])

    cfg, ledger, _ = _inputs()
    progress = _ready_progress()

    def uncharged_raise():
        execution["new_stub_callbacks_started"] += 1
        raise RuntimeError("new stub: before-start budget failure")
    message = None
    try:
        _call_final_slot(cfg, ledger, progress, uncharged_raise)
    except RuntimeError as error:
        message = str(error)
    r = progress["terminal_slot_release"]
    checks["before_start_budget_failure_does_not_invent_a_charge"] = (
        message == "new stub: before-start budget failure"
        and ledger["linear_program_invocation_count"] == 63
        and r["new_started_primary_LPs"] == 0
        and r["original_shared_slots_left"] == 1 and r["source_cfg_unchanged"])
    return checks


def developer_check():
    started = time.monotonic()
    execution = {"new_stub_callbacks_started": 0, "real_LP_calls": 0,
                 "ordinary_geometry_calls": 0, "full_directional_JVP_calls": 0,
                 "old_developer_suites_executed": 0, "scientific_optimization_calls": 0}
    groups = []
    for name, operation in (
        ("terminal_release_eligibility", _group_release),
        ("support_bundle_nonreplacement", _group_supports),
        ("single_slot_ledger_and_failure", lambda: _group_accounting(execution))):
        event = {"name": name, "checks": {}, "passed": False}
        groups.append(event)
        try:
            event["checks"] = operation()
            event["passed"] = all(event["checks"].values())
        except Exception as error:
            event["error"] = {"type": type(error).__name__, "message": str(error)}
    expected_counts = [4, 3, 4]
    actual_counts = [len(g["checks"]) for g in groups]
    passed = actual_counts == expected_counts and all(g["passed"] for g in groups)
    sources = {}
    for name in ("frame_metric_terminal_paid_slot.py", Path(__file__).name):
        raw = Path(__file__).with_name(name).read_bytes()
        sources[name] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    return {
        "schema": POLICY+"-development", "all_passed": passed,
        "groups": groups, "new_group_count": 3,
        "executed_check_count": sum(actual_counts), "expected_check_count": 11,
        "expected_group_check_counts": expected_counts,
        "execution": execution, "source_files": sources,
        "elapsed_seconds": time.monotonic()-started,
        "old9_direct_geometry_receipt_must_be_consumed_without_execution": True,
        "no_new_geometry_or_frozen_solver_suite_is_hidden_in_these_fixtures": True,
    }

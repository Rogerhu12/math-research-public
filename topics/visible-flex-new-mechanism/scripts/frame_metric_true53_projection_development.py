#!/usr/bin/env python3
"""Exactly three new projection/glue cases, called only by the public audit.

These are small artificial arrays with hand-derived answers.  They do not
restore a research point, call a geometry/J/JVP backend, or execute an old
developer suite.  Their real elapsed time remains inside the caller's one
600-second scientific clock; their artificial solver counters are separate
from the single production projection and line sessions.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import time
import traceback

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_budget_recovery import require_public_research_environment
from frame_metric_complete_maximin_projection import (
    POLICY, ProjectionLedger, ProjectionLimit, PhysicalMetric,
    HalfspaceProjection, guard_compatible_interval, require)
from frame_metric_true53_projection_line import GuardedLineEnvelope, run_guarded_line

CASE_NAMES = (
    "weighted_dual_projection_on_a_guard_domain_excluding_zero",
    "current_gap_separation_constant_conflict_and_started_budget_exit",
    "positive_lower_endpoint_keeps_physical_zero_and_query_debits",
)


def implementation_hashes():
    names = ("frame_metric_complete_maximin_projection.py",
             "frame_metric_true53_projection_line.py", Path(__file__).name)
    return {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in names}


def _row(A, b, *, name, kind="hard", tolerance=0.):
    return {"A": np.array(A, dtype=float), "b": float(b),
            "tolerance": float(tolerance), "kind": kind,
            "tag": {"artificial_case_row": name}}


def _near(actual, expected, tolerance=2e-13):
    a, b = np.asarray(actual, float), np.asarray(expected, float)
    require(a.shape == b.shape and np.all(np.isfinite(a))
            and np.max(abs(a-b), initial=0.) <= tolerance,
            "hand-derived artificial identity differs")


def _case_one(record):
    ledger = ProjectionLedger(time.monotonic())
    record["_ledger"] = ledger
    record["_session"] = ledger.begin("projection_sessions", artificial_case=CASE_NAMES[0])
    metric = PhysicalMetric(np.array([[2.]]), artificial=True)
    rows = [
        _row([-1, 0, 0], -.25, name="z-lower"),
        _row([1, 0, 0], .75, name="z-upper"),
        _row([0, -1, 0], 0, name="h-lower"),
        _row([0, 1, 0], 1, name="h-upper"),
        _row([0, 0, 1], .5, name="s-upper"),
        _row([0, 0, -1], .5, name="s-lower"),
    ]
    master = HalfspaceProjection(metric, rows, ledger)
    require(not master.residual(np.zeros(3))["all_installed_rows_within_original_tolerance"],
            "this real artificial guard domain must exclude zero")
    prox = ledger.begin("prox_steps", artificial_case=CASE_NAMES[0], center=1)
    master.rebind_center(np.array([0., 0., 1.]))
    master.sweep()
    first = master.diagnostic()
    _near(master.w, [.25, 0., .5])
    _near([first["projection_primal_value_if_full_primal_feasible"],
           first["projection_dual_lower_value"], first["projection_gap"]], [.25, .25, 0.])
    require(first["all_installed_rows_within_original_tolerance"],
            "first hand solution must satisfy every row")
    ledger.end(prox)
    first_vector = master.w.copy()
    # Reuse the same dual variables, but restore stationarity for the new y.
    prox = ledger.begin("prox_steps", artificial_case=CASE_NAMES[0], center=2)
    master.rebind_center(np.array([1., 0., .2]))
    _near(master.w, master.y-master.multipliers@master.inverse_rows)
    master.sweep()
    second = master.diagnostic()
    _near(master.w, [.75, 0., .2])
    _near(second["projection_gap"], 0.)
    require(second["all_installed_rows_within_original_tolerance"]
            and second["negative_dual_multiplier_count"] == 0
            and second["dual_stationarity_maximum_error"] <= 2e-13,
            "warm dual rebinding changed the same-center identity")
    ledger.end(prox)
    record.update(
        physical_map=[[2.]], weighted_metric_diagonal=[4., 1., 1.],
        guard_domain_nonempty_but_zero_not_in_domain=True,
        first_actual_vector=first_vector.tolist(), first_diagnostic=first,
        second_actual_vector=master.w.tolist(), second_diagnostic=second,
        artificial_coordinate_updates_executed=ledger.counts["coordinate_updates"],
        artificial_projection_sessions_executed=1)


def _case_two(record):
    ledger = ProjectionLedger(time.monotonic())
    record["_ledger"] = ledger
    record["_session"] = ledger.begin("projection_sessions", artificial_case=CASE_NAMES[1])
    metric = PhysicalMetric(np.array([[1.]]), artificial=True)
    hard = [
        _row([-1, 0, 0], -.02, name="old-hard-z-lower"),
        _row([1, 0, 0], 1, name="old-hard-z-upper"),
    ]
    current = _row([-1, .1, .1], 0., name="base-active-phi", kind="metric", tolerance=1e-9)
    omitted = _row([1, .1, .1], .1, name="near-active-gap-point-one",
                   kind="metric", tolerance=1e-9)
    master = HalfspaceProjection(metric, hard+[current], ledger)
    old_A, old_b = master.A.copy(), master.b.copy()
    wrong = np.array([.2, .2, 1.])
    require(master.residual(wrong)["all_installed_rows_within_original_tolerance"],
            "the omitted-row example must pass its original finite master")
    base_phi0 = 1.
    # These two rows have actual current values 1 and .9: the .1 gap is not dropped.
    complete_values = [1.-wrong[0], .9+wrong[0]]
    full_residual = max(complete_values)+.1*(wrong[1]+wrong[2])-base_phi0
    _near(full_residual, .22)
    require(full_residual > 1e-9 and omitted["b"] == .1,
            "the near-active full row must reject this wrong direction")
    installed = master.add([omitted, copy.deepcopy(omitted)])
    require(installed == 1 and np.array_equal(master.A[:len(old_A)], old_A)
            and np.array_equal(master.b[:len(old_b)], old_b),
            "separation must append one original row without dropping old hard rows")
    require(not master.residual(wrong)["all_installed_rows_within_original_tolerance"],
            "the newly installed actual-gap row must remain effective")
    zero = _row([0, 0, 0], -2.**-30, name="literal-zero-negative-RHS", tolerance=1e-7)
    master.add([zero])
    require(len(master.zero_conflicts) == 1
            and master.zero_conflicts[0]["strict_model_inconsistent"]
            and master.zero_conflicts[0]["within_original_numeric_tolerance"],
            "a literal zero row cannot be silently divided or have its RHS clipped")

    # A fixture-only inherited debit places the real production ledger one visit
    # below its fixed cap.  It is explicitly not one million executed updates.
    budget_master = HalfspaceProjection(metric, hard, ledger)
    simulated = ledger.limits["coordinate_updates"]-1
    ledger.counts["coordinate_updates"] = simulated
    record["simulated_inherited_coordinate_debits_not_executed"] = simulated
    prox = ledger.begin("prox_steps", artificial_case=CASE_NAMES[1])
    budget_master.rebind_center(np.zeros(3))
    try:
        budget_master.sweep()
    except ProjectionLimit as error:
        require(error.kind == "coordinate_updates"
                and error.used == ledger.limits["coordinate_updates"],
                "the real boundary debit reported the wrong counter")
        record["expected_budget_exception"] = {
            "type": type(error).__name__, "counter": error.kind,
            "used_including_simulated_inheritance": error.used, "limit": error.limit}
    else:
        raise AssertionError("the second coordinate visit must be refused before work")
    _near(budget_master.w, [.02, 0., 0.])
    saved = budget_master.w.copy()
    before = ledger.counts["coordinate_updates"]
    try:
        ledger.charge("coordinate_updates")
    except ProjectionLimit:
        pass
    else:
        raise AssertionError("an exhausted coordinate scope must not reset itself")
    require(before == ledger.counts["coordinate_updates"]
            and np.array_equal(saved, budget_master.w),
            "refused work must preserve the already paid finite iterate")
    ledger.end(prox)
    record.update(
        current_phi_gap_kept=.1, complete_wrong_direction_residual=full_residual,
        added_original_metric_rows=installed,
        literal_zero_conflict=copy.deepcopy(master.zero_conflicts[0]),
        retained_partial_vector_after_budget_exit=saved.tolist(),
        artificial_coordinate_updates_executed=ledger.counts["coordinate_updates"]-simulated,
        artificial_projection_sessions_executed=1,
        simulated_debits_excluded_from_executed_update_count=True)


def _case_three(record):
    ledger = ProjectionLedger(time.monotonic())
    record["_ledger"] = ledger
    interval = guard_compatible_interval(
        np.array([0.]), np.array([1.]), np.array([.25]),
        residual_tolerance=0., physical_bounds=[(.75, -1., 0.)])
    legal = interval["original_numeric_tolerance_interval"]
    require(legal["nonempty"] and legal["lower"] == .25 and legal["upper"] == .75
            and not legal["zero_in_interval"],
            "the physical interval must have a genuinely positive lower endpoint")
    arrays = {label: {"e": np.array([1.]), "f": np.array([0.]),
                      "de": np.array([-1.]), "df": np.array([0.])}
              for label in ("coarse", "fine")}
    direction = np.array([1.])
    binding_sha = digest({"artificial_current": "positive-left-original-alpha"})
    model = SimpleNamespace(
        binding_sha256=binding_sha,
        binding={"physical_state_sha256": digest({"artificial": "same-source"})},
        phi0=1., target=.26, epsilon=1e-8,
        cfg_sha256=digest({"artificial": "frozen-cfg"}), grids={},
        cfg={"value_Jacobian_replay_relative_tolerance": 5e-12,
             "linear_model_improvement_floor": 1e-10})
    handle = {
        "qualified": True, "direction": direction, "interval": interval,
        "scan": {"model_binding_sha256": binding_sha,
                 "direction_sha256": array_digest(direction), "arrays": arrays}}
    envelope = GuardedLineEnvelope(model, handle, ledger)
    payload = envelope.full_record()
    raw = (json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False)+"\n").encode()
    receipt = {"binding_sha256": envelope.binding_sha256,
               "JSON_plus_LF_bytes": len(raw), "JSON_plus_LF_sha256": hashlib.sha256(raw).hexdigest(),
               "artificial_in_memory_publication_protocol_only": True}
    envelope.mark_full_cache_published(receipt)
    envelope.ledger.charge_session()
    baseline = envelope.query(0., purpose="physical-zero-baseline")
    lower = envelope.query(.25)
    middle = envelope.query(.5)
    target = envelope.query(.75)
    duplicate = envelope.query(.5, purpose="untried-actual-fallback")
    _near([baseline["phi"], lower["phi"], middle["phi"], target["phi"]], [1., .75, .5, .26])
    require(target["constant_original_target_is_active"]
            and target["floating_left_slope"] == target["floating_right_slope"] == 0.,
            "the constant original metric target is a real envelope branch")
    require(all(x["original_alpha_zero_baseline"] == 1. for x in envelope.records),
            "the legal lower endpoint may not replace the original physical baseline")
    _near(lower["observed_model_gain_from_true_zero"], .25)
    require(duplicate["query_number"] == 5 and ledger.counts["scalar_queries"] == 5,
            "a repeated complete value/derivative recomputation must be charged")
    before = ledger.counts["scalar_queries"]
    try:
        envelope.query(0.)
    except ValueError:
        pass
    else:
        raise AssertionError("physical zero outside the legal interval is only a baseline query")
    require(ledger.counts["scalar_queries"] == before,
            "an out-of-domain request must fail before a complete query starts")
    empty = guard_compatible_interval(
        np.array([0.]), np.array([0.]), np.array([1.]), residual_tolerance=0.)
    empty_ledger = ProjectionLedger(time.monotonic())
    forbidden_publications = []
    def should_not_publish(payload):
        forbidden_publications.append(payload)
        raise AssertionError("an empty interval must not start line-cache publication")
    empty_handle = dict(handle, qualified=False, interval=empty)
    answer, progress, empty_envelope = run_guarded_line(
        model, empty_handle, empty_ledger, publish_cache=should_not_publish)
    require(answer is None and empty_envelope is None and not forbidden_publications
            and empty_ledger.counts["scalar_sessions"] == 0
            and empty_ledger.counts["scalar_queries"] == 0,
            "an empty interval must not start a scalar or actual session")
    record.update(
        legal_interval=copy.deepcopy(interval), artificial_cache_receipt=receipt,
        actual_artificial_queries=copy.deepcopy(envelope.records),
        empty_interval_progress=progress,
        artificial_scalar_sessions_executed=ledger.counts["scalar_sessions"],
        artificial_complete_queries_executed=ledger.counts["scalar_queries"],
        old_golden_search_suite_executed=0, production_cache_published=False,
        artificial_coordinate_updates_executed=0,
        artificial_projection_sessions_executed=0)


def developer_check():
    """No parameters: exactly the three new cases, once per authorized first run."""
    require_public_research_environment()
    started = time.monotonic()
    records = []
    functions = (_case_one, _case_two, _case_three)
    for name, function in zip(CASE_NAMES, functions):
        record = {"name": name, "status": "started", "passed": False}
        records.append(record)
        tick = time.monotonic()
        error = None
        try:
            function(record)
            record.update(status="complete", passed=True)
        except Exception as caught:
            error = caught
            record.update(status="raised", error={"type": type(caught).__name__,
                          "message": str(caught), "traceback": traceback.format_exc()})
        finally:
            ledger, session = record.pop("_ledger", None), record.pop("_session", None)
            if ledger is not None:
                if session is not None:
                    ledger.end(session, error)
                record["artificial_ledger"] = ledger.report()
            record["elapsed_seconds"] = time.monotonic()-tick
    return {
        "schema": POLICY+"-new-three-case-development",
        "all_passed": all(row["passed"] for row in records),
        "passed": all(row["passed"] for row in records),
        "new_case_count": 3, "executed_case_count": len(records),
        "records": records, "elapsed_seconds": time.monotonic()-started,
        "source_sha256": implementation_hashes(),
        "execution": {
            "new_artificial_projection_sessions": sum(
                row.get("artificial_ledger", {}).get("started_counts", {}).get(
                    "projection_sessions", 0) for row in records),
            "new_artificial_prox_steps_started": sum(
                row.get("artificial_ledger", {}).get("started_counts", {}).get(
                    "prox_steps", 0) for row in records),
            "new_artificial_sweeps_started": sum(
                row.get("artificial_ledger", {}).get("started_counts", {}).get(
                    "sweeps", 0) for row in records),
            "new_artificial_coordinate_updates_executed": sum(
                row.get("artificial_ledger", {}).get("started_counts", {}).get(
                    "coordinate_updates", 0)
                -row.get("simulated_inherited_coordinate_debits_not_executed", 0)
                for row in records),
            "new_artificial_scalar_sessions": sum(
                row.get("artificial_ledger", {}).get("started_counts", {}).get(
                    "scalar_sessions", 0) for row in records),
            "new_artificial_complete_envelope_queries": sum(
                row.get("artificial_ledger", {}).get("started_counts", {}).get(
                    "scalar_queries", 0) for row in records),
            "production_projection_sessions": 0, "production_full_grid_separations": 0,
            "actual_geometry_calls": 0, "selected159_J_calls": 0,
            "directional_JVP_calls": 0, "legacy_LP_SOC_cone_calls": 0,
            "original_developer_suites_executed": 0,
            "old_scalar_optimizer_or_tiny_cone_tests_executed": 0,
            "simulated_inherited_debits_are_not_counted_as_executed_updates": True,
        },
        "artificial_solver_work_is_not_reported_as_zero_solver_work": True,
        "all_development_elapsed_is_inside_the_audit_600_second_science_clock": True,
        "no_surface_or_original_input_restoration_in_development": True,
    }


if __name__ == "__main__":
    raise SystemExit("No standalone scope; the public true53 audit calls developer_check once.")

#!/usr/bin/env python3
"""Six new interface checks only; no original geometry, J, or solver suite."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import time
from types import SimpleNamespace
import numpy as np
from frame_entry_body_subspace import array_digest
from frame_height_null_coordinates import digest
from frame_metric_budget_recovery import EvaluationBudgetReached, require_public_research_environment
from frame_metric_paid_cone_vector import (
    POLICY, SOURCE_NEW_SCIENCE, SOURCE_GLOBAL_SCIENCE, ContinuationClock,
    decode_paid_step, actual_acceptance, _validate_direction)


def rejected(function, exception):
    try:
        function()
    except exception:
        return True
    return False


def saved_vector_and_clock():
    p = np.zeros(159)
    p[0], p[158] = .125, -.25
    raw = {"exact_binary64_independent_step": [str(Q.from_float(float(x))) for x in p],
           "array_sha256": array_digest(p)}
    actual = decode_paid_step(raw, expected_sha=raw["array_sha256"])
    short = copy.deepcopy(raw)
    short["exact_binary64_independent_step"] = short["exact_binary64_independent_step"][:-1]
    wrong = copy.deepcopy(raw)
    wrong["array_sha256"] = "0"*64
    now = [100.]
    clock = ContinuationClock(100., clock=lambda: now[0])
    first = clock.report()
    now[0] += 1200-SOURCE_NEW_SCIENCE+.25
    over = clock.report()
    checks = {
        "paid_exact159_is_recovered_without_missing_solver_auxiliaries":
            np.array_equal(actual, p) and set(raw) == {"exact_binary64_independent_step", "array_sha256"},
        "short_or_wrong_fingerprint_record_is_rejected_before_any_value":
            rejected(lambda: decode_paid_step(short, expected_sha=raw["array_sha256"]), ValueError)
            and rejected(lambda: decode_paid_step(wrong, expected_sha=raw["array_sha256"]), ValueError),
        "both_source_clocks_continue_and_post_call_overrun_is_not_clipped":
            first["cumulative_cone_task_scientific_seconds"] == SOURCE_NEW_SCIENCE
            and first["cumulative_original_scientific_seconds"] == SOURCE_GLOBAL_SCIENCE
            and over["cumulative_cone_task_scientific_seconds"] > 1200
            and over["remaining_scientific_seconds_in_intersection"] < 0
            and rejected(clock.check, EvaluationBudgetReached)}
    return {k: bool(v) for k, v in checks.items()}, {"new_solver_or_actual_value_calls": 0}


class ArrayCoordinates:
    def validate(self, state):
        q = np.asarray(state, float)
        if q.shape != (159,) or not np.all(np.isfinite(q)):
            raise ValueError("fixture requires finite159")
        return q

    def physical_exact(self, state):
        return tuple(Q.from_float(float(x)) for x in np.r_[self.validate(state), np.zeros(4)])

    def exact_box_decision(self, state, lower, upper):
        self.validate(state)
        return {"exact_original_box_pass": True, "fixture_only_not_a_physical_box_certificate": True}


class ArrayOnlyObjective:
    """Just the new outer contract; values are declared arrays, never geometry."""
    def __init__(self, *, failed_eta=False, new_row=False, fail_fine=False):
        self.cfg = {"minimum_accepted_eta_decrease_exact": "1/10000000"}
        self.physical_lower, self.physical_upper = -np.ones(163), np.ones(163)
        coordinates = ArrayCoordinates()
        self.problem = SimpleNamespace(
            coordinates=coordinates,
            identity=lambda state: {"artificial_array": True, "exact159": [
                str(Q.from_float(float(x))) for x in state]})
        self.subspace = SimpleNamespace(
            columns=np.arange(159, dtype=np.int64),
            apply=lambda state, step: np.asarray(state, float)+np.asarray(step, float),
            step_norms=lambda step, width: {"fixture_actual_delta_infinity": float(np.max(abs(step)))})
        self.initial = np.zeros(159)
        self.accepted_iterates = [{
            "accepted_index": 52, "maximum_eta_on_both_grids": 1.,
            "physical_state_sha256": digest(self.problem.identity(self.initial))}]
        self.geometry_evaluations = self.fine_evaluations = 0
        self.pool_version, self.fine_pool_version = 13, 12
        self.failed_eta, self.new_row, self.fail_fine = failed_eta, new_row, fail_fine

    @property
    def full_value_evaluations(self):
        return self.geometry_evaluations+self.fine_evaluations

    def _wall(self):
        return None

    def vector(self, state):
        return np.r_[state, 1.]

    def exact_support_invariants(self, state):
        return {"fixture_no_physical_support_claim": True}

    def decision(self):
        return {
            "direct_max_eta": 1.1 if self.failed_eta else .9,
            "single_grid_admissible_recovery_point": True,
            "single_grid_new_target_qualified": False, "regularity_screen_pass": True,
            "single_grid_hard_gate_pass": True, "previous_metric_budget_pass": True,
            "cap_and_box": {"eligible_under_declared_numerical_gate_tolerances": True}}

    def evaluate(self, vector):
        self.geometry_evaluations += 1
        return {"physical_geometry_evaluation": self.geometry_evaluations, "decision": self.decision()}

    def fine_decision(self, state):
        self.fine_evaluations += 1
        if self.fail_fine:
            raise EvaluationBudgetReached("new fixture declared charged fine failure")
        return self.decision()

    def accepted_point(self, state, coarse, fine, reason):
        value = {"accepted_index": 53, "maximum_eta_on_both_grids": max(coarse["direct_max_eta"], fine["direct_max_eta"]),
                 "physical_state_sha256": digest(self.problem.identity(state))}
        self.accepted_iterates.append(value)
        return value

    def expand_pool(self, vector, reason):
        detail = {"omitted_violating_count": int(self.new_row),
                  "omitted_hard_violating_count": 0}
        if self.new_row:
            self.pool_version += 1
            return {"added_row_indices": [17]}, detail
        return None, detail

    def learn_fine_violations(self, state, reason):
        return None, {"omitted_violating_count": 0, "omitted_hard_violating_count": 0}


def actual_branch_and_capture():
    p = np.zeros(159)
    p[0] = .125
    accepted = ArrayOnlyObjective()
    result = {"trials": [], "status": "fixture-start"}
    _validate_direction(accepted, accepted.initial, p, result)
    c = accepted.decision()
    equal = actual_acceptance(c["direct_max_eta"], c, c, 1e-7)
    qualified = dict(c, direct_max_eta=.99999999, single_grid_new_target_qualified=True)
    tiny_target = actual_acceptance(1., qualified, qualified, 1e-7)
    failed = ArrayOnlyObjective(failed_eta=True, new_row=True)
    stopped = {"trials": [], "status": "fixture-start"}
    _validate_direction(failed, failed.initial, p, stopped)
    fault = ArrayOnlyObjective(fail_fine=True)
    partial = {"trials": [], "status": "fixture-start"}
    caught = rejected(lambda: _validate_direction(fault, fault.initial, p, partial), EvaluationBudgetReached)
    trial = partial["trials"][0]
    checks = {
        "actual_only_acceptance_uses_two_grid_strict_drop_and_original_target_exception":
            result["status"] == "paid-vector-new-two-grid-strict-descent-accepted"
            and len(result["trials"]) == 1 and result["trials"][0]["alpha_exact"] == "1"
            and accepted.accepted_iterates[-1]["accepted_index"] == 53
            and accepted.full_value_evaluations == 2
            and equal["accepted"] is False and tiny_target["accepted"] is True,
        "failed_trial_new_actual_row_stops_the_same_direction_before_second_fraction":
            stopped["status"] == "paid-vector-new-rows-stop-fixed-direction-last-accepted-retained"
            and len(stopped["trials"]) == 1 and failed.full_value_evaluations == 2
            and len(failed.accepted_iterates) == 1
            and failed.pool_version == 14 and failed.fine_pool_version == 12,
        "charged_fine_failure_keeps_full_candidate159_and_physical163_before_acceptance":
            caught and fault.full_value_evaluations == 2 and len(fault.accepted_iterates) == 1
            and trial["attempt_status"] == "fine-value-call-started"
            and len(trial["exact_binary64_independent_coordinates"]) == 159
            and len(trial["exact_original_physical_coefficients"]) == 163
            and trial["accepted_as_next_iterate"] is False}
    return {k: bool(v) for k, v in checks.items()}, {
        "new_stub_value_calls": accepted.full_value_evaluations+failed.full_value_evaluations+fault.full_value_evaluations,
        "actual_geometry_J_JVP_solver_calls": 0,
        "original_physical_geometry_and_gate_suites_not_reexecuted": True}


def developer_check():
    require_public_research_environment()
    groups = []
    for name, function in (
            ("saved_vector_and_continued_clock", saved_vector_and_clock),
            ("actual_only_branch_and_failure_capture", actual_branch_and_capture)):
        before = time.monotonic()
        try:
            checks, details = function()
            group = {"name": name, "expected_checks": 3, "checks": checks,
                     "details": details, "passed": len(checks) == 3 and all(checks.values())}
        except Exception as error:
            group = {"name": name, "expected_checks": 3, "checks": {},
                     "passed": False, "error": {"type": type(error).__name__, "message": str(error)}}
        group["elapsed_seconds"] = time.monotonic()-before
        groups.append(group)
    return {
        "schema": POLICY+"-new-interface-development", "group_count": 2,
        "expected_check_count": 6, "executed_check_count": sum(len(g["checks"]) for g in groups),
        "all_passed": all(g["passed"] for g in groups), "groups": groups,
        "execution": {"actual_geometry_calls": 0, "parameter_J_or_directional_JVP_calls": 0,
                      "research_or_tiny_solver_calls": 0, "original_developer_suites_executed": 0,
                      "new_stub_value_calls": sum(g.get("details", {}).get("new_stub_value_calls", 0) for g in groups)},
        "paid12_cone_11_terminal_and9_geometry_checks_are_receipts_only": True}

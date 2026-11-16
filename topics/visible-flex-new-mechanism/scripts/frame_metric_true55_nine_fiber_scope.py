#!/usr/bin/env python3
"""Shared, newly authorized true55 fixed159/new9 task scope; import-only."""
from __future__ import annotations
import copy
import math
import time
from frame_metric_true53_paid_master_central_path import NewMasterLimitReached

POLICY = "fixed159-true55-new9-affine-fiber-v1"
VARIABLES = 11
NINE = 9
RHO_INDEX = 9
H_INDEX = 10
STEP_SCALE = .25
NORM_WEIGHT = 1.e-6
LIMITS = {
    "science_seconds": 600,
    "necessary_model_grid_values": 2,
    "hard_J_grid_builds": 2,
    "metric9_grid_builds": 2,
    "full_separations": 16,
    "new_metric_rows": 64,
    "finite_master_calls": 16,
    "finite_master_iterations": 1536,
    "finite_master_newton_systems": 3072,
    "scalar_sessions": 1,
    "scalar_queries": 64,
    "actual_trial_pairs": 3,
    "actual_grid_values": 6,
}
PER_PROBLEM_ITERATIONS = 96
PER_PROBLEM_SYSTEMS = 192

def require(condition, message):
    if not bool(condition):
        raise ValueError(message)

class NineFiberLimit(NewMasterLimitReached):
    def __init__(self, kind, used, limit, *, stage="", elapsed=0.):
        self.kind, self.used, self.limit = str(kind), used, limit
        reason = "time_limit" if kind == "science_seconds" else "nine_fiber_scope_limit"
        super().__init__(reason, stage or str(kind), elapsed)
        self.args = ("nine-fiber limit %s: %s / %s at %s" %
                     (kind, used, limit, self.stage),)

class NineFiberLedger:
    """One new 600-second clock; ancestor costs are retained, never debited anew."""
    def __init__(self, started_monotonic, *, ancestor_receipt, limits=None):
        now = time.monotonic()
        require(type(started_monotonic) in (int, float)
                and math.isfinite(started_monotonic)
                and 0 <= started_monotonic <= now,
                "a real pre-import, pre-input monotonic origin is required")
        selected = dict(LIMITS if limits is None else limits)
        require(selected == LIMITS, "the declared new nine-fiber scope is immutable")
        require(isinstance(ancestor_receipt, dict),
                "the original ancestor cost and source receipt is required")
        self.started = float(started_monotonic)
        self.limits = selected
        self.ancestor_receipt = copy.deepcopy(ancestor_receipt)
        self.counts = {key: 0 for key in LIMITS if key != "science_seconds"}
        self.events = []
        self.problem_bindings = set()
        self.last_problem_added_count = None
        self.check("ledger.entry")
    def elapsed(self):
        return float(time.monotonic()-self.started)
    def check(self, stage=""):
        elapsed = self.elapsed()
        if not math.isfinite(elapsed) or elapsed >= self.limits["science_seconds"]:
            raise NineFiberLimit("science_seconds", elapsed,
                                 self.limits["science_seconds"],
                                 stage=stage, elapsed=elapsed)
        return elapsed
    def charge(self, key, count=1):
        self.check(key)
        require(key in self.counts and type(count) is int and count > 0,
                "a known started-work counter and positive integer debit are required")
        if self.counts[key]+count > self.limits[key]:
            raise NineFiberLimit(key, self.counts[key]+count, self.limits[key],
                                 stage=key, elapsed=self.elapsed())
        self.counts[key] += count
        return self.counts[key]
    def begin(self, key, **metadata):
        ordinal = self.charge(key)
        event = copy.deepcopy(metadata)
        event.update(counter=key, ordinal=ordinal, status="started",
                     started_scientific_seconds=self.elapsed(),
                     _started=time.monotonic())
        self.events.append(event)
        return event
    def end(self, event, error=None, **metadata):
        require(any(item is event for item in self.events) and event.get("status") == "started",
                "exactly one finish of the original started event is required")
        tick = event.pop("_started")
        event.update(copy.deepcopy(metadata))
        event["elapsed_seconds"] = float(time.monotonic()-tick)
        event["finished_scientific_seconds"] = self.elapsed()
        event["status"] = "complete" if error is None else "raised"
        if error is not None:
            event["error"] = copy.deepcopy(error) if isinstance(error, dict) else {
                "type": type(error).__name__, "message": str(error)}
    def note(self, stage, **metadata):
        self.events.append({"stage": str(stage), "status": "metadata",
                            "scientific_seconds": self.elapsed(),
                            **copy.deepcopy(metadata)})
    def claim_problem(self, binding, added_row_count):
        require(isinstance(binding, str) and len(binding) == 64
                and all(c in "0123456789abcdef" for c in binding),
                "a SHA256 of the complete new eleven-variable problem is required")
        require(type(added_row_count) is int and added_row_count >= 0,
                "the actual cumulative number of added original rows is required")
        require(binding not in self.problem_bindings,
                "an already attempted finite row set cannot be solved again")
        require(self.last_problem_added_count is None
                or added_row_count > self.last_problem_added_count,
                "each later master must retain all old rows and add a new source row")
        event = self.begin("finite_master_calls", problem_binding_sha256=binding,
                           additional_original_metric_rows=added_row_count,
                           variable_order="z9,rho,h", source_accepted_index=55)
        self.problem_bindings.add(binding)
        self.last_problem_added_count = added_row_count
        return event
    def report(self):
        elapsed = self.elapsed()
        events = copy.deepcopy(self.events)
        for event in events:
            tick = event.pop("_started", None)
            if tick is not None:
                event["elapsed_seconds_so_far"] = float(time.monotonic()-tick)
        return {
            "schema": POLICY+"-ledger", "limits": dict(self.limits),
            "started_counts": dict(self.counts), "scientific_seconds": elapsed,
            "remaining_scientific_seconds": max(0., self.limits["science_seconds"]-elapsed),
            "deadline_observed_exceeded": elapsed >= self.limits["science_seconds"],
            "observed_overrun_seconds": max(0., elapsed-self.limits["science_seconds"]),
            "new_full_value_debits": self.counts["necessary_model_grid_values"]
                                      +self.counts["actual_grid_values"],
            "ancestor_receipt_unchanged": copy.deepcopy(self.ancestor_receipt),
            "events": events,
            "attempted_problem_bindings": sorted(self.problem_bindings),
            "old_HiGHS_cone_projection_finite_tasks_resumed": False,
            "old_159_derivatives_or_developer_suites_requested": False,
            "all_inputs_imports_failures_serialization_share_this_clock": True,
            "nested_phase_seconds_are_not_added_to_scientific_seconds": True,
            "indivisible_call_overrun_is_reported_not_hidden": True}


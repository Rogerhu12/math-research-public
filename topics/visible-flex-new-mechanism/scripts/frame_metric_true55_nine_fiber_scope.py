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
    """One task account across processes; closed ancestor costs stay separate.

    started is the current process's real pre-import monotonic origin.
    elapsed() adds authenticated-by-caller prior task time to that process
    duration.  No prior monotonic tick is meaningful in the new process.
    """
    def __init__(self, started_monotonic, *, ancestor_receipt, limits=None,
                 prior_scope_receipt=None):
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
        empty_counts = {key: 0 for key in LIMITS if key != "science_seconds"}
        self.prior_scientific_seconds = 0.
        self.prior_started_counts = dict(empty_counts)
        self.prior_scope_receipt = None
        self.events = []
        self.problem_bindings = set()
        self.last_problem_added_count = None
        if prior_scope_receipt is not None:
            require(isinstance(prior_scope_receipt, dict),
                    "a prior same-task receipt must be a mapping")
            prior = copy.deepcopy(prior_scope_receipt)
            seconds = prior.get("scientific_seconds")
            require(type(seconds) in (int, float) and math.isfinite(seconds)
                    and seconds >= 0.,
                    "prior same-task scientific time must be finite and nonnegative")
            counts = prior.get("started_counts")
            require(isinstance(counts, dict) and set(counts) == set(empty_counts),
                    "the complete original started-counter set is required")
            for key, value in counts.items():
                require(type(value) is int and 0 <= value <= self.limits[key],
                        "a prior started count is outside its original task limit")
            source = prior.get("source")
            require(isinstance(source, dict) and bool(source),
                    "the original failed output and clock receipt source is required")
            if "schema" in prior:
                require(prior["schema"] == POLICY+"-ledger",
                        "the prior receipt belongs to a different task schema")
            if "limits" in prior:
                require(prior["limits"] == LIMITS,
                        "the prior task limits must be unchanged")
            prior_events = prior.get("events", [])
            require(isinstance(prior_events, list)
                    and all(isinstance(event, dict) and "_started" not in event
                            for event in prior_events),
                    "prior events must be original serialized receipts, not live ticks")
            bindings = prior.get("attempted_problem_bindings", [])
            require(isinstance(bindings, list)
                    and all(isinstance(item, str) and len(item) == 64
                            and all(c in "0123456789abcdef" for c in item)
                            for item in bindings)
                    and len(set(bindings)) == len(bindings)
                    and len(bindings) == counts["finite_master_calls"],
                    "every previously attempted finite row set must remain recorded")
            last_added = prior.get("last_problem_added_count")
            require((not bindings and last_added is None)
                    or (bool(bindings) and type(last_added) is int and last_added >= 0),
                    "a prior finite problem requires its last cumulative added-row count")
            self.prior_scientific_seconds = float(seconds)
            self.prior_started_counts = dict(counts)
            self.prior_scope_receipt = prior
            self.problem_bindings = set(bindings)
            self.last_problem_added_count = last_added
        self.counts = dict(self.prior_started_counts)
        self.check("ledger.entry")
    def current_process_elapsed(self):
        return float(time.monotonic()-self.started)
    def elapsed(self):
        return float(self.prior_scientific_seconds+self.current_process_elapsed())
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
        current_elapsed = self.current_process_elapsed()
        elapsed = float(self.prior_scientific_seconds+current_elapsed)
        events = copy.deepcopy(self.events)
        for event in events:
            tick = event.pop("_started", None)
            if tick is not None:
                event["elapsed_seconds_so_far"] = float(time.monotonic()-tick)
        return {
            "schema": POLICY+"-ledger", "limits": dict(self.limits),
            "started_counts": dict(self.counts), "scientific_seconds": elapsed,
            "same_task_scientific_seconds": elapsed,
            "prior_same_task_scientific_seconds": self.prior_scientific_seconds,
            "current_process_scientific_seconds": current_elapsed,
            "prior_started_counts": dict(self.prior_started_counts),
            "current_process_started_counts": {
                key: self.counts[key]-self.prior_started_counts[key]
                for key in self.counts},
            "prior_scope_receipt_unchanged": copy.deepcopy(self.prior_scope_receipt),
            "prior_receipt_validation_scope":
                "structure and original limits only; caller authenticates source stdout",
            "events_scope": "this process; prior events remain in their original receipt",
            "remaining_scientific_seconds": max(0., self.limits["science_seconds"]-elapsed),
            "deadline_observed_exceeded": elapsed >= self.limits["science_seconds"],
            "observed_overrun_seconds": max(0., elapsed-self.limits["science_seconds"]),
            "new_full_value_debits": self.counts["necessary_model_grid_values"]
                                      +self.counts["actual_grid_values"],
            "ancestor_receipt_unchanged": copy.deepcopy(self.ancestor_receipt),
            "events": events,
            "attempted_problem_bindings": sorted(self.problem_bindings),
            "last_problem_added_count": self.last_problem_added_count,
            "counts_are_cumulative_for_the_same_task": True,
            "prior_counts_are_loaded_without_new_begin_events": True,
            "old_HiGHS_cone_projection_finite_tasks_resumed": False,
            "old_159_derivatives_or_developer_suites_requested": False,
            "all_inputs_imports_failures_serialization_share_this_clock": True,
            "nested_phase_seconds_are_not_added_to_scientific_seconds": True,
            "indivisible_call_overrun_is_reported_not_hidden": True}


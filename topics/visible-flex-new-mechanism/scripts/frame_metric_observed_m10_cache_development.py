#!/usr/bin/env python3
"""Only the new post-learning y-cache reinstall/capture interface.

Public Actions is the sole execution venue. Use source-defined artificial
array DATA, never an old developer_check. The original full_views and
capture_failed_trial functions are real; evaluate/fine_decision below are
explicit cache-only stubs, not a geometric surface or nonlinear validation.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import resource
import time
import traceback
from types import SimpleNamespace
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_entry_tail_height_blocks import N, artificial_arrays, build_primary
from frame_metric_entry_tail154 import EntryTail154Objective
from frame_metric_height159_soc_hold import model_binding
import frame_metric_expanded_pool_soc as core
import frame_metric_observed_m10_soc_audit as audit


def _fixture(*, charged_miss=False):
    cfg = {
        "linear_fraction_to_boundary_exact": "1/2",
        "step_cost_physical_box_norm_coefficient_exact": "1/1000",
        "strip_proposal_floor_exact": "1/10000000",
        "curvature_proposal_floor_exact": "1/10000000",
        "SOC_physical_margin_retention_exact": "1/4",
        "SOC_predicted_descent_retention_exact": "1/2",
        "SOC_maximum_correction_relative_to_proposed_step_exact": "1/2",
        "linear_model_improvement_floor": 1e-10,
        "max_linear_models": 2, "linear_program_seconds": 1.}
    sub, full, selected, x, lower, upper, cap = artificial_arrays()
    x = np.asarray(x, float).copy()
    primary = build_primary(sub, full, selected, x, lower, upper, cap,
        trust_exact=str(Q.from_float(1/4000)))
    # A labelled array signature only, with no observable or geometric factory.
    primary.information["radius_independent_model_sha256"] = digest({
        "cache_fixture_original_complete_array":
            primary.information["radius_independent_model_sha256"]})
    step = np.zeros(N)
    step[0], step[154] = 1/1024, -1/1024
    y = sub.apply(x, step)
    new_ids = [np.asarray(sorted(set(selection.ids.tolist()+[
        view.grid.nt+1, 8*view.grid.point_count+2*view.grid.nt+1])), np.int64)
        for view, selection in zip(full, selected)]

    class CacheHarness:
        def __init__(self):
            self.subspace = sub
            self.problem = SimpleNamespace(identity=sub.coordinates.physical_identity)
            self.pool, self.fine_pool = (v.copy() for v in new_ids)
            self.pool_version, self.fine_pool_version = 3, 4
            self.row_grids = [v.grid for v in full]
            self.geometry_evaluations, self.fine_evaluations = 2, 2
            self.calls = {"evaluate_cache_stub": 0, "fine_cache_stub": 0,
                          "original_full_views": 0}
            self.geometry_cache = self._data(full[0])
            self.fine_cache = {
                "state": y.copy(), "rows": full[1].rows.copy(),
                "data": self._data(full[1]),
                "decision": {"regularity_screen_pass": True}}
            self.epigraph_cache = None  # Exact lifecycle state missed by the first m10 driver.

        def _data(self, view):
            return {"state": y.copy(), "rows": view.rows.copy(),
                "eta": view.eta.copy(), "height": {"b": view.b.copy()},
                "Xs": np.zeros((view.grid.nr, view.grid.nt, 3))}

        def vector(self, state):
            return np.r_[np.asarray(state, float), 0.]

        def evaluate(self, vector):
            self.calls["evaluate_cache_stub"] += 1
            if not np.array_equal(np.asarray(vector[:-1], float), self.geometry_cache["state"]):
                raise ValueError("cache stub only owns its one source-defined y")
            if charged_miss:
                self.geometry_evaluations += 1  # Deliberately detectable artificial miss.
            result = {"decision": {"regularity_screen_pass": True}}
            self.epigraph_cache = {
                "vector": np.asarray(vector, float).copy(),
                "rows": self.geometry_cache["rows"].copy(), "record": result}
            return result

        def fine_decision(self, state):
            self.calls["fine_cache_stub"] += 1
            if not np.array_equal(np.asarray(state, float), self.fine_cache["state"]):
                raise ValueError("fine cache stub only owns its one y")
            return self.fine_cache["decision"]

        def row_tolerances(self):
            return full[0].tolerances

        def full_views(self, state):
            self.calls["original_full_views"] += 1
            return EntryTail154Objective.full_views(self, state)

    objective = CacheHarness()
    old_versions = (2, 3)
    binding = model_binding(primary, x, digest(objective.problem.identity(x)), old_versions)
    trial = {
        "kind": "primary-metric-short-step", "alpha_exact": "1",
        "accepted_as_next_iterate": False,
        "physical_state_sha256": digest(objective.problem.identity(y)),
        "coarse_decision": {"regularity_screen_pass": True},
        "fine_decision": {"regularity_screen_pass": True},
        "new_coarse_rows": 2, "new_fine_rows": 2,
        "coarse_omitted_hard_rows": 1, "fine_omitted_hard_rows": 1}
    return objective, primary, x, y, old_versions, binding, trial, cfg


def _capture(fixture):
    objective, primary, x, y, versions, binding, trial, cfg = fixture
    return core.capture_failed_trial(objective, primary, x, y, versions, binding, 10, 0, trial, cfg)


def _restore_and_capture():
    fixture = _fixture()
    objective, primary, x, y, versions, binding, trial, cfg = fixture
    original = {"trial": copy.deepcopy(trial), "cfg": copy.deepcopy(cfg),
                "binding": copy.deepcopy(binding),
                "ids": [array_digest(objective.pool), array_digest(objective.fine_pool)],
                "state": array_digest(y)}
    # Reproduce the exact original None-cache boundary with the real capture.
    rejected_before_restore = False
    try:
        _capture(fixture)
    except TypeError as error:
        rejected_before_restore = ("NoneType" in str(error) and
                                   objective.epigraph_cache is None)
    if not rejected_before_restore:
        raise AssertionError("original full_views did not reproduce the published None-cache boundary")
    record = {}
    audit.restore_failed_y_layout(objective, y, record)
    failed = _capture(fixture)
    frozen_rows = failed.views[0].rows.copy()
    objective.geometry_cache["rows"] = objective.geometry_cache["rows"].copy()
    objective.geometry_cache["rows"].reshape(-1)[0] += 3.
    good = bool(
        record["status"] == "complete-no-new-ordinary-value" and
        record["new_ordinary_counts_before"] == record["new_ordinary_counts_after"] == [2, 2] and
        record["new_ordinary_calls"] == [0, 0] and
        record["original_full_views_same_state_contract_passed"] is True and
        objective.calls == {"evaluate_cache_stub": 1, "fine_cache_stub": 1,
                            "original_full_views": 3} and
        np.array_equal(failed.x, x) and np.array_equal(failed.y, y) and
        np.array_equal(failed.step, y-x) and failed.new_versions == (3, 4) and
        np.array_equal(failed.views[0].rows, frozen_rows) and
        all(not a.flags.writeable for v in failed.views
            for a in (v.rows, v.eta, v.b, v.tolerances, v.mean_Xs)) and
        failed.original_binding == binding == original["binding"] and
        trial == original["trial"] and cfg == original["cfg"] and
        original["ids"] == [array_digest(objective.pool), array_digest(objective.fine_pool)] and
        original["state"] == array_digest(y))
    if not good:
        raise AssertionError("real full_views/capture did not retain the complete cache-only contract")
    return {"passed": True, "restore": record, "calls": objective.calls,
            "real_capture_before_and_after": True, "real_inherited_full_views": True,
            "cache_methods_are_explicit_array_stubs": True}


def _charged_restore_rejected():
    fixture = _fixture(charged_miss=True)
    objective, _, _, y, _, _, _, _ = fixture
    record = {}
    rejected = False
    try:
        audit.restore_failed_y_layout(objective, y, record)
    except Exception as error:
        rejected = "charged ordinary geometry" in str(error)
    if not (rejected and record.get("status") == "error" and
            record["new_ordinary_counts_before"] == [2, 2] and
            record["new_ordinary_counts_after"] == [3, 2] and
            record["new_ordinary_calls"] == [1, 0] and
            record["zero_extra_ordinary_calls_observed"] is False and
            objective.calls["original_full_views"] == 0):
        raise AssertionError("charged cache miss was not recorded and rejected before capture")
    return {"passed": True, "restore": record, "calls": objective.calls,
            "deliberate_array_counter_increment_is_not_a_real_geometry_call": True}


def developer_check():
    started = time.monotonic()
    checks, details, errors = {}, {}, {}
    for name, operation in (
        ("post_learning_cache_reinstall_allows_real_full_views_and_same_y_capture_without_new_values",
         _restore_and_capture),
        ("charged_cache_miss_is_reported_and_rejected_before_capture_not_declared_zero",
         _charged_restore_rejected)):
        try:
            detail = operation()
            if detail["passed"] is not True:
                raise AssertionError("new cache interface did not return exact True")
            checks[name], details[name] = True, detail
        except Exception as error:
            checks[name] = False
            errors[name] = {"type": type(error).__name__, "message": str(error),
                            "traceback": traceback.format_exc()}
    passed = bool(checks) and all(checks.values())
    return {"schema": audit.SCHEMA+"-post-learning-cache-development",
        "passed": passed, "all_passed": passed, "checks": checks,
        "details": details, "errors": errors,
        "scope": "only new cache-reinstall/original-full_views/capture lifecycle",
        "source_defined_artificial_arrays_not_original_research_input": True,
        "geometry_calls": 0, "primary_LP_calls": 0, "SOC_LP_calls": 0,
        "old_expanded_ten_executions": 0, "old_m10_seven_executions": 0,
        "no_original_suite_or_optimizer_called": True,
        "elapsed_seconds": time.monotonic()-started,
        "peak_rss_kib_linux": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}

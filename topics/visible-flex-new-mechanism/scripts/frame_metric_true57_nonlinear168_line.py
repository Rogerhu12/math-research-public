#!/usr/bin/env python3
"""Seven fixed actual-coordinate nonlinear predictions for a true57 direction.

Import-only.  No golden section, adaptive alpha, midpoint, restart or hidden
solver is present.  Each of the seven declared slots is charged once before
its actual binary64 coordinate application and domain checks.  A rejected
domain uses no metric/curvature prediction.  All scientific work, nested
calls, failures and output share the caller's one new scope.

Only genuinely eligible nonlinear metric/curvature predictions are ranked.
The actual owner independently evaluates the original fourteen gates and
original acceptance rule.  Predictor values never become actual receipts.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import math

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_complete_body_extension168 import array_binding
from frame_complete_body_extension168_joint_selected import bind_current_168_first_jets
from frame_complete_body_extension168_nonlinear_metric_line import (
    ActualCandidateMetricPredictor168, POLICY as METRIC_POLICY)
from frame_complete_body_extension168_curvature_prediction import (
    bind_current_168_curvature_metric, predict_current_168_curvature,
    POLICY as CURVATURE_POLICY)


POLICY = "true57-full168-seven-fixed-candidate-nonlinear-prediction-line-v1"
ALPHAS_EXACT = ("1", "3/4", "1/2", "1/4", "1/8", "1/16", "1/32")
ALPHAS = tuple(float(Q(value)) for value in ALPHAS_EXACT)
NORM_WEIGHT = 1.e-6
MAXIMUM_H_EXACT = "1/128"
MAXIMUM_ACTUAL_PAIRS = 3


def definition():
    return {
        "schema": POLICY,
        "source_accepted_index": 57,
        "fixed_alphas_exact_in_evaluation_order": list(ALPHAS_EXACT),
        "candidate_application":
            "literal numpy model.state + float(alpha)*handle.direction, then original exact172 domain",
        "candidate_coordinates_are_saved_once_and_used_verbatim_for_actual": True,
        "scalar_sessions": 1, "scalar_queries": 7,
        "query_slot_includes_domain_rejection_or_same-point_semantic_reuse": True,
        "maximum_actual_trial_pairs": MAXIMUM_ACTUAL_PAIRS,
        "metric_prediction_policy": METRIC_POLICY,
        "curvature_prediction_policy": CURVATURE_POLICY,
        "predicted_descent":
            "source57 actual two-grid eta minus predicted nonlinear two-grid eta >= original cfg minimum",
        "strict_positive_predicted_eta_drop_required_even_if_target_already_qualified": True,
        "curvature_filter": "both original scaled PSD and direct-kappa tolerance predicates on both predictor grids",
        "ranking": "predicted eta + 1e-6 * original handle.report.new_physical_norm_h * alpha",
        "ranking_tie_break": "smaller alpha, then original query number",
        "h_for_score_is_the_frozen_complete_direction_report_value": True,
        "actual_exact172_h_limit": MAXIMUM_H_EXACT,
        "original_model_numeric_hard_interval_and_exact_candidate_domain_both_retained": True,
        "no_zero_alpha_replay_of_source57": True,
        "no_convexity_or_global_or_continuous_optimality_claim": True,
        "no_golden_search_midpoint_restart_or_new_alpha": True,
        "new_rows_or_capacity_from_actual_close_this_direction": True,
        "predictor_curvature_failure_is_not_a_complete_actual_gate_result": True,
        "raw_array_retention":
            "only current best eligible successful prediction plus current/most recent partial",
        "other_successful_queries":
            "full semantic coordinates/domain/results/counts/array hashes; values discarded",
        "same_candidate_reuse":
            "only identical binary64 state168; preserve original predictor source receipt and charge no second predictor",
        "actual_trial_does_not_read_prediction_arrays_as_ordinary": True,
        "caller_owns_600_second_clock_and_all_nested_work_output_and_failures": True}


def _require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def _array(value, shape, name):
    a = np.asarray(value, dtype=np.float64)
    _require(a.shape == tuple(shape) and np.all(np.isfinite(a)),
             "finite literal shape required: "+name)
    a = a.copy()
    a.setflags(write=False)
    return a


def _same(left, right):
    a, b = np.asarray(left), np.asarray(right)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def _vector(value):
    a = np.asarray(value, dtype=np.float64)
    return {
        "shape": list(a.shape), "dtype": str(a.dtype),
        "array_sha256": array_digest(a), "values": a.tolist(),
        "exact_binary64": [str(Q.from_float(float(v))) for v in a]}


def _error(error):
    return {"type": type(error).__name__, "message": str(error)}


def _public_capture(value):
    """Known predictor captures keep arrays ONLY under their _arrays key."""
    return {key: copy.deepcopy(item) for key, item in value.items() if key != "_arrays"}


def _rank(row):
    return (row["objective"], row["alpha"], row["number"])


class NonlinearCandidateLine168:
    """A new seven-slot scalar session, with the old actual.trial call shape.

    Required objects:
      prepared: field168, center168, radial, theta, fine_theta, cfg;
      model: state, field, cfg, binding_sha256, input_binding_sha256,
             validate_actual_candidate(candidate168);
      handle: qualified,direction,interval,report from the complete current model;
      ledger: begin/end/check, counts/limits using the new 1/7/3/6 allowance;
      first_jet_bounds: current57 coarse/fine bindings already paid in this scope;
      fixed_metric: already available a/a_s/a_ss from the same fixed field;
      source_point: authenticated original actual57 point, including physical
                    hash and maximum_eta_on_both_grids;
      source_receipt: the caller's input/output provenance.

    emit(suffix, semantic_dict) is optional and returns an original-stdout
    receipt.  run() emits LINE_QUERY only.  actual_candidates(actual,emit=...)
    calls actual.trial(saved_q,alpha,prediction,emit=...) without new predictor
    work.  The actual owner alone charges actual pairs/geometry and checks
    all fourteen gates.  Public report() never contains large raw arrays.
    """
    def __init__(
            self, prepared, model, handle, ledger, *,
            first_jet_bounds, fixed_metric, source_point, source_receipt,
            emit=None, capture=None):
        self.prepared, self.model, self.handle, self.ledger = prepared, model, handle, ledger
        self.emit = emit
        self.capture = {} if capture is None else capture
        _require(isinstance(self.capture, dict) and not self.capture,
                 "one empty line capture is required")
        self.capture.update(
            schema=POLICY+"-capture", status="constructing", queries=[],
            best_raw_source_query=None, latest_partial_source_query=None,
            _best_qualified_prediction_raw=None, _latest_partial_raw=None)
        self.records, self.by_alpha, self.by_candidate = [], {}, {}
        self.candidates = {}
        self.event, self.summary, self.actual_summary = None, None, None
        self._run_started = False
        self._actual_started = False
        self._best = None
        ledger.check("nonlinear-line.constructor")
        _require(isinstance(prepared, dict) and isinstance(handle, dict)
                 and handle.get("qualified") is True,
                 "one complete original-domain-qualified current direction is required")
        _require(ledger.limits["scalar_sessions"] == 1
                 and ledger.limits["scalar_queries"] == len(ALPHAS)
                 and ledger.limits["actual_trial_pairs"] == MAXIMUM_ACTUAL_PAIRS
                 and ledger.limits["actual_grid_values"] == 2*MAXIMUM_ACTUAL_PAIRS,
                 "the new one-session/seven-query/three-actual-pair scope is required")
        self.field, self.cfg = prepared["field168"], prepared["cfg"]
        self.configuration_sha256 = digest(self.cfg)
        self.center = _array(model.state, (168,), "model current168")
        self.direction = _array(handle["direction"], (168,), "complete direction168")
        _require(model.field is self.field
                 and digest(model.cfg) == digest(self.cfg)
                 and _same(self.center, np.asarray(prepared["center168"], dtype=np.float64)),
                 "same current field/cfg/center required by line and model")
        self.field.validate_state(self.center)
        self.model_binding_sha256 = model.binding_sha256
        self.input_binding_sha256 = model.input_binding_sha256
        self.direction_sha256 = array_digest(self.direction)
        self.interval = copy.deepcopy(
            handle["interval"]["original_numeric_tolerance_interval"])
        _require(self.interval.get("nonempty") is True,
                 "the original hard/physical numerical line interval is required")
        self.lower, self.upper = float(self.interval["lower"]), float(self.interval["upper"])
        _require(math.isfinite(self.lower) and math.isfinite(self.upper)
                 and 0. <= self.lower <= self.upper <= 1.,
                 "one declared subinterval inside [0,1] is required")
        direction_report = handle["report"]
        _require(direction_report.get("model_binding_sha256") == self.model_binding_sha256
                 and direction_report.get("input_binding_sha256") == self.input_binding_sha256,
                 "the complete direction report belongs to a different current model")
        self.h = float(direction_report["new_physical_norm_h"])
        _require(math.isfinite(self.h) and self.h >= 0.,
                 "the frozen complete-direction physical norm must be finite")
        self.source_point = copy.deepcopy(source_point)
        self.source_receipt = copy.deepcopy(source_receipt)
        _require(isinstance(source_point, dict) and source_point.get("accepted_index") == 57
                 and isinstance(source_receipt, dict) and bool(source_receipt),
                 "authenticated actual57 source point and receipt required")
        self.source_physical_sha256 = digest(self.field.identity(self.center))
        _require(source_point.get("physical_state_sha256") == self.source_physical_sha256,
                 "actual57 and the current complete model are different physical points")
        self.baseline_eta = float(source_point["maximum_eta_on_both_grids"])
        self.minimum_exact = Q(self.cfg["minimum_accepted_eta_decrease_exact"])
        self.minimum = float(self.minimum_exact)
        _require(math.isfinite(self.baseline_eta) and self.baseline_eta >= 0.
                 and self.minimum_exact > 0 and math.isfinite(self.minimum),
                 "the original source eta and positive acceptance decrease are required")
        self.radial = np.asarray(prepared["radial"], dtype=np.float64)
        self.thetas = {
            "coarse": np.asarray(prepared["theta"], dtype=np.float64),
            "fine": np.asarray(prepared["fine_theta"], dtype=np.float64)}
        input_receipt = {
            "schema": POLICY+"-paid-current-input",
            "source_accepted_index": 57,
            "source_physical_state_sha256": self.source_physical_sha256,
            "source_two_grid_actual_eta": self.baseline_eta,
            "model_binding_sha256": self.model_binding_sha256,
            "input_binding_sha256": self.input_binding_sha256,
            "caller_source_receipt": copy.deepcopy(source_receipt)}
        self.metric_bound = bind_current_168_curvature_metric(
            self.field, self.radial, fixed_metric, input_receipt)
        self.metric_predictor = ActualCandidateMetricPredictor168(
            self.field, self.center, self.radial, self.thetas, first_jet_bounds,
            input_receipt, wall=ledger.check)
        for key in ("a", "a_s"):
            _require(_same(self.metric_predictor.metric[key], self.metric_bound["data"][key]),
                     "metric and curvature predictors must retain the same fixed radial metric")
        self.identity = {
            "schema": POLICY+"-line-identity",
            "definition": definition(),
            "source_physical_state_sha256": self.source_physical_sha256,
            "center168": _vector(self.center),
            "direction168": _vector(self.direction),
            "model_binding_sha256": self.model_binding_sha256,
            "input_binding_sha256": self.input_binding_sha256,
            "original_direction_report": copy.deepcopy(direction_report),
            "original_numeric_tolerance_interval": copy.deepcopy(self.interval),
            "configuration_sha256": self.configuration_sha256,
            "minimum_predicted_eta_drop_exact": str(self.minimum_exact),
            "source57_actual_two_grid_eta": self.baseline_eta,
            "norm_h_for_ranking": self.h,
            "norm_h_for_ranking_binary64_exact": str(Q.from_float(self.h)),
            "norm_h_source": "original complete handle.report.new_physical_norm_h",
            "curvature_metric_binding_sha256": self.metric_bound["binding_sha256"],
            "nonlinear_metric_source_binding_sha256": self.metric_predictor.source_binding_sha256,
            "source_receipt": copy.deepcopy(source_receipt)}
        self.binding_sha256 = digest(self.identity)
        self.capture.update(
            status="ready", identity=copy.deepcopy(self.identity),
            binding_sha256=self.binding_sha256,
            raw_retention_policy=definition()["raw_array_retention"])
        ledger.check("nonlinear-line.constructor.complete")

    def _assert_current(self):
        self.ledger.check("nonlinear-line.same-current-model")
        _require(self.model.binding_sha256 == self.model_binding_sha256
                 and self.model.input_binding_sha256 == self.input_binding_sha256
                 and _same(self.model.state, self.center)
                 and digest(self.field.identity(self.center)) == self.source_physical_sha256
                 and digest(self.cfg) == self.configuration_sha256
                 and digest(self.model.cfg) == self.configuration_sha256,
                 "the fixed direction's physical/model/cfg context changed")

    def _publish(self, row):
        if self.emit is not None and "stdout_receipt" not in row:
            row["stdout_receipt"] = self.emit("LINE_QUERY", row)

    def _end_query(self, event, row):
        if event.get("status") == "started":
            self.ledger.end(
                event, query_status=row["status"],
                nonlinear_prediction_evaluated=row.get("new_metric_predictor_calls", 0) == 1,
                qualified_for_actual=row.get("qualified_for_actual", False),
                objective=row.get("objective"))
        self._publish(row)
        self.ledger.check("nonlinear-line.query.complete")

    def _domain(self, candidate, alpha):
        domain = self.model.validate_actual_candidate(candidate)
        norm = domain["joint_physical_domain"]
        exact_norm = Q(norm["actual_exact172_step_norm_exact"])
        required = bool(
            domain["eligible"]
            and domain["exact172_box"]["exact_full_box_pass"]
            and norm["all_selected_hard_targets_pass"]
            and norm["literal_mapped_direction_norm_pass"]
            and norm["literal_actual_physical_step_pass"]
            and exact_norm <= Q(MAXIMUM_H_EXACT))
        return domain, bool(required and self.lower <= alpha <= self.upper)

    def _retain_best(self, row, raw):
        if not row.get("qualified_for_actual", False):
            return
        if self._best is not None and _rank(row) >= _rank(self._best):
            return
        self._best = row
        if raw is None:
            # An identical binary64 point may have an earlier semantic receipt
            # whose values were already discarded.  Never invent its arrays.
            current = self.capture.get("_best_qualified_prediction_raw")
            if current is not None and current["candidate_array_sha256"] == row["candidate_array_sha256"]:
                raw = current
        self.capture["_best_qualified_prediction_raw"] = raw
        self.capture["best_raw_source_query"] = (
            None if raw is None else raw["source_query_number"])
        self.capture["best_semantic_query"] = row["number"]
        self.capture["best_raw_available"] = raw is not None
        if raw is None:
            self.capture["best_raw_unavailable_reason"] = (
                "same actual point reused by identity; original successful values were not retained")
        else:
            self.capture.pop("best_raw_unavailable_reason", None)

    def _qualify(self, row):
        eta = float(row["predicted_two_grid_eta"])
        gain = self.baseline_eta-eta
        curv = row["predicted_curvature_by_grid"]
        curvature_pass = all(
            curv[label]["predictor_PSD_with_original_tolerance"] is True
            and curv[label]["predictor_direct_cap_with_original_tolerance"] is True
            for label in ("coarse", "fine"))
        strict = bool(math.isfinite(eta) and gain > 0. and gain >= self.minimum)
        norm_cost = NORM_WEIGHT*self.h*row["alpha"]
        row.update(
            predicted_eta_drop=gain,
            minimum_predicted_eta_drop_exact=str(self.minimum_exact),
            predicted_eta_drop_is_strict_and_at_least_original_minimum=strict,
            predicted_curvature_pass_on_both_grids=curvature_pass,
            norm_cost=norm_cost, objective=eta+norm_cost,
            qualified_for_actual=bool(row["original_domain_eligible"]
                                      and strict and curvature_pass),
            nonlinear_floating_predictions_are_not_actual_fourteen_gate_receipts=True)

    def query(self, alpha, purpose="one-fixed-scale"):
        alpha = float(alpha)
        _require(math.isfinite(alpha) and alpha in ALPHAS,
                 "only the seven originally declared exact binary64 scales are allowed")
        key = alpha.hex()
        if key in self.by_alpha:
            return self.by_alpha[key]
        _require(self.event is not None and self.event.get("status") == "started",
                 "a fixed query must belong to the single active declared session")
        self._assert_current()
        event = self.ledger.begin("scalar_queries", alpha=alpha, purpose=purpose,
                                  line_binding_sha256=self.binding_sha256)
        row = {
            "number": len(self.records)+1, "alpha": alpha,
            "alpha_exact": str(Q.from_float(alpha)), "purpose": purpose,
            "status": "started", "line_binding_sha256": self.binding_sha256,
            "direction_sha256": self.direction_sha256,
            "qualified_for_actual": False,
            "new_metric_predictor_calls": 0, "new_curvature_predictor_calls": 0,
            "new_candidate_first_jet_bindings": 0,
            "ordinary_geometry_calls_in_prediction": 0,
            "large_values_not_in_semantic_LINE_QUERY": True}
        self.records.append(row)
        self.by_alpha[key] = row
        self.capture["queries"].append(row)
        working = {
            "source_query_number": row["number"], "alpha": alpha,
            "line_binding_sha256": self.binding_sha256,
            "metric_capture": {}, "curvature_capture": {}}
        self.capture["_latest_partial_raw"] = working
        self.capture["latest_partial_source_query"] = row["number"]
        try:
            # Exactly the old actual application, with both operations in
            # binary64.  No later candidate reconstruction is permitted.
            candidate = self.center+alpha*self.direction
            candidate = _array(candidate, (168,), "actual rounded candidate168")
            candidate_sha = array_digest(candidate)
            self.candidates[row["number"]] = candidate
            working.update(candidate_array_sha256=candidate_sha, candidate168=candidate)
            row.update(
                actual_candidate168=_vector(candidate),
                candidate_array_sha256=candidate_sha,
                actual_application="literal current168 + float(alpha)*direction168",
                same_coordinates_are_passed_to_predictors_and_actual=True)
            # Keep every finite returned coordinate before any field/domain
            # operation can reject it; do not reconstruct it after failure.
            self.field.validate_state(candidate)
            physical_sha = digest(self.field.identity(candidate))
            working["physical_state_sha256"] = physical_sha
            row.update(
                actual_physical172_exact=[str(value) for value in self.field.full_coefficients(candidate, exact=True)],
                candidate_physical_state_sha256=physical_sha)
            domain, eligible = self._domain(candidate, alpha)
            row.update(
                candidate_domain=copy.deepcopy(domain),
                inside_original_numeric_tolerance_interval=bool(self.lower <= alpha <= self.upper),
                original_domain_eligible=eligible)
            if _same(candidate, self.center):
                row.update(status="unchanged-actual-binary64-point-no-prediction",
                           original_domain_eligible=False)
                self._end_query(event, row)
                self.capture["_latest_partial_raw"] = None
                self.capture["latest_partial_source_query"] = None
                return row
            if not eligible:
                row["status"] = "original-rounded-domain-or-interval-rejected-no-prediction"
                self._end_query(event, row)
                self.capture["_latest_partial_raw"] = None
                self.capture["latest_partial_source_query"] = None
                return row
            previous = self.by_candidate.get(candidate_sha)
            if previous is not None:
                _require(_same(self.candidates[previous["number"]], candidate),
                         "equal candidate hash must retain exact coordinate equality")
                for name in ("metric_prediction", "candidate_first_jet_bindings",
                             "curvature_prediction", "predicted_two_grid_eta",
                             "predicted_curvature_by_grid"):
                    row[name] = copy.deepcopy(previous[name])
                row.update(
                    status="complete-same-actual-point-semantic-reuse",
                    reused_source_query_number=previous["number"],
                    reused_source_stdout_receipt=copy.deepcopy(previous.get("stdout_receipt")),
                    original_predictor_diagnostics_are_reused_provenance_not_new_cost=True,
                    new_nested_metric_counts={}, new_nested_curvature_counts={},
                    reused_values_not_claimed_as_a_new_complete_cache=True)
                self._qualify(row)
                self._retain_best(row, None)
                self._end_query(event, row)
                self.capture["_latest_partial_raw"] = None
                self.capture["latest_partial_source_query"] = None
                return row

            candidate_receipt = {
                "schema": POLICY+"-actual-candidate-source",
                "line_binding_sha256": self.binding_sha256,
                "query_number": row["number"], "alpha_exact": row["alpha_exact"],
                "candidate_array_sha256": candidate_sha,
                "candidate_physical_state_sha256": physical_sha,
                "model_binding_sha256": self.model_binding_sha256,
                "input_binding_sha256": self.input_binding_sha256,
                "exact172_box_and_domain_receipt": copy.deepcopy(domain),
                "candidate_has_not_been_ordinary_evaluated_by_this_line": True}
            row["new_metric_predictor_calls"] = 1
            metric_result = self.metric_predictor.predict(
                candidate, candidate_receipt=candidate_receipt,
                capture=working["metric_capture"])
            working["metric_result"] = metric_result
            row["metric_prediction"] = {
                "binding": copy.deepcopy(metric_result["binding"]),
                "binding_sha256": metric_result["binding_sha256"],
                "diagnostics": copy.deepcopy(metric_result["diagnostics"])}
            row["new_nested_metric_counts"] = copy.deepcopy(
                metric_result["diagnostics"]["counts_during_call"])
            row["predicted_two_grid_eta"] = float(
                metric_result["diagnostics"]["two_grid_predicted_eta"])
            candidate_bounds = {}
            binding_records = {}
            for label in ("coarse", "fine"):
                self.ledger.check("nonlinear-line.candidate-first-jet."+label)
                arrays = metric_result["grids"][label]
                data = {name: arrays[name] for name in ("U", "T", "e", "f")}
                data["metric"] = self.metric_bound["data"]
                provenance = {
                    "schema": POLICY+"-nonlinear-predicted-first-jet-source",
                    "grid": label, "query_number": row["number"],
                    "line_binding_sha256": self.binding_sha256,
                    "actual_candidate168_array_sha256": candidate_sha,
                    "nonlinear_metric_policy": METRIC_POLICY,
                    "nonlinear_metric_prediction_binding_sha256": metric_result["binding_sha256"],
                    "nonlinear_metric_grid_binding_sha256":
                        metric_result["diagnostics"]["grid_receipts"][label]["binding_sha256"],
                    "original_ordinary_was_not_evaluated": True,
                    "not_an_actual_gate_receipt": True}
                row["new_candidate_first_jet_bindings"] += 1
                bound = bind_current_168_first_jets(
                    self.field, candidate, self.radial, self.thetas[label], data,
                    provenance, wall=self.ledger.check)
                candidate_bounds[label] = bound
                binding_records[label] = {
                    "binding_sha256": bound["binding_sha256"],
                    "identity": copy.deepcopy(bound["identity"]),
                    "binding_seconds": bound["binding_seconds"]}
                working.setdefault("completed_candidate_first_jet_bindings", {})[label] = bound
                row["candidate_first_jet_bindings"] = copy.deepcopy(binding_records)
            row["new_curvature_predictor_calls"] = 1
            curvature_result = predict_current_168_curvature(
                self.field, candidate, self.radial, self.thetas, candidate_bounds,
                self.metric_bound, self.cfg,
                source_receipt={
                    "schema": POLICY+"-candidate-curvature-source",
                    "line_binding_sha256": self.binding_sha256,
                    "query_number": row["number"],
                    "candidate_array_sha256": candidate_sha,
                    "candidate_physical_state_sha256": physical_sha,
                    "upstream_metric_prediction_binding_sha256": metric_result["binding_sha256"],
                    "upstream_first_jets_are_nonlinear_predictions_not_original_ordinary": True},
                wall=self.ledger.check, capture=working["curvature_capture"])
            working["curvature_result"] = curvature_result
            row["curvature_prediction"] = {
                "binding": copy.deepcopy(curvature_result["binding"]),
                "binding_sha256": curvature_result["binding_sha256"],
                "diagnostics": copy.deepcopy(curvature_result["diagnostics"]),
                "grid_receipts": {
                    label: {
                        "binding_sha256": curvature_result["grids"][label]["binding_sha256"],
                        "identity": copy.deepcopy(curvature_result["grids"][label]["identity"]),
                        "summary": copy.deepcopy(curvature_result["grids"][label]["summary"])}
                    for label in ("coarse", "fine")}}
            row["new_nested_curvature_counts"] = copy.deepcopy(curvature_result["diagnostics"]["counts"])
            row["predicted_curvature_by_grid"] = {
                label: copy.deepcopy(curvature_result["grids"][label]["summary"])
                for label in ("coarse", "fine")}
            row["status"] = "complete-nonlinear-metric-and-curvature-prediction"
            self._qualify(row)
            self.by_candidate[candidate_sha] = row
            self._retain_best(row, working)
            row["raw_array_storage_scope"] = (
                "temporary; only the currently best eligible query and latest partial are retained")
            self._end_query(event, row)
            self.capture["_latest_partial_raw"] = None
            self.capture["latest_partial_source_query"] = None
            return row
        except Exception as error:
            previous_status = row["status"]
            row.update(status="raised", error=_error(error),
                       status_before_exception=previous_status,
                       partial_metric_capture=_public_capture(working["metric_capture"]),
                       partial_curvature_capture=_public_capture(working["curvature_capture"]))
            if event.get("status") == "started":
                self.ledger.end(event, error)
            else:
                row["query_work_completed_but_post_completion_failed"] = True
            self.capture.update(status="raised", latest_partial_source_query=row["number"])
            self._publish(row)
            raise

    def run(self):
        _require(not self._run_started, "this fixed seven-slot session cannot restart")
        self._run_started = True
        self._assert_current()
        self.event = self.ledger.begin(
            "scalar_sessions", direction_sha256=self.direction_sha256,
            line_binding_sha256=self.binding_sha256,
            fixed_alphas_exact=list(ALPHAS_EXACT))
        self.capture["status"] = "running"
        try:
            for index, alpha in enumerate(ALPHAS, 1):
                self.query(alpha, "fixed-alpha-slot-"+str(index))
            ranked = sorted((row for row in self.records if row.get("qualified_for_actual")), key=_rank)
            best = ranked[0] if ranked else None
            self.summary = {
                "schema": POLICY+"-fixed-candidate-selection",
                "status": ("complete-fixed-seven-with-qualified-candidates" if best is not None
                           else "complete-fixed-seven-no-qualified-candidate"),
                "line_binding_sha256": self.binding_sha256,
                "fixed_alphas_exact": list(ALPHAS_EXACT),
                "source57_actual_two_grid_eta": self.baseline_eta,
                "minimum_predicted_eta_drop_exact": str(self.minimum_exact),
                "legal_interval": copy.deepcopy(self.interval),
                "best_query": copy.deepcopy(best),
                "qualified_predicted_descent": best is not None,
                "ranked_qualified_query_numbers": [row["number"] for row in ranked],
                "qualified_candidate_count_before_exact-point_deduplication": len(ranked),
                "maximum_actual_pairs": MAXIMUM_ACTUAL_PAIRS,
                "scalar_slots_started_this_session": len(self.records),
                "shared_scalar_queries": self.ledger.counts["scalar_queries"],
                "new_metric_prediction_calls": sum(row["new_metric_predictor_calls"] for row in self.records),
                "new_curvature_prediction_calls": sum(row["new_curvature_predictor_calls"] for row in self.records),
                "no_convexity_or_global_minimum_is_inferred": True,
                "no_source57_zero_replay_or_adaptive_alpha": True,
                "normal_and_PSD_predictions_do_not_replace_actual14": True,
                "raw_best_source_query": self.capture.get("best_raw_source_query"),
                "other_successful_query_values_are_not_a_future_free_cache": True}
            self.ledger.end(
                self.event, qualified_predicted_descent=best is not None,
                scalar_queries=len(self.records), eligible_count=len(ranked))
            self.capture.update(status="complete", summary=copy.deepcopy(self.summary))
            self.ledger.check("nonlinear-line.session.complete")
            return self.summary
        except Exception as error:
            if self.event.get("status") == "started":
                self.ledger.end(self.event, error)
            self.capture.update(status="raised", error=_error(error),
                                partial_query_records=copy.deepcopy(self.records))
            raise

    def actual_candidates(self, actual, *, emit=None):
        """At most three already predicted distinct actual coordinate vectors."""
        _require(self.summary is not None and self.capture.get("status") == "complete",
                 "a complete fixed nonlinear prediction session is required")
        _require(not self._actual_started, "the same predicted direction cannot restart actual trials")
        self._actual_started = True
        self._assert_current()
        _require(actual.field is self.field
                 and actual.source_point.get("accepted_index") == 57
                 and actual.source_point.get("physical_state_sha256") == self.source_physical_sha256
                 and float(actual.source_point["maximum_eta_on_both_grids"]) == self.baseline_eta,
                 "actual owner must use the identical original accepted57 baseline")
        trace = {
            "schema": POLICY+"-actual-candidate-selection", "trials": [],
            "policy": "ranked eligible fixed candidates; no new alpha or prediction",
            "new_acceptances": 0, "maximum_actual_pairs": MAXIMUM_ACTUAL_PAIRS,
            "all_ordinary_and_trial_pair_charges_are_owned_by_actual_trial": True}
        self.actual_summary = trace
        if not self.summary["qualified_predicted_descent"]:
            trace["status"] = "no-fixed-scale-qualified-nonlinear-prediction"
            return trace
        ranked = sorted((row for row in self.records if row.get("qualified_for_actual")), key=_rank)
        seen = set()
        selected = []
        for row in ranked:
            if row["candidate_array_sha256"] not in seen:
                seen.add(row["candidate_array_sha256"])
                selected.append(row)
            if len(selected) == MAXIMUM_ACTUAL_PAIRS:
                break
        trace["preselected_distinct_query_numbers"] = [row["number"] for row in selected]
        for number, prediction in enumerate(selected, 1):
            self._assert_current()
            self.ledger.check("nonlinear-line.actual-selected-candidate")
            q = self.candidates[prediction["number"]]
            _require(array_digest(q) == prediction["candidate_array_sha256"]
                     and digest(self.field.identity(q)) == prediction["candidate_physical_state_sha256"],
                     "actual must use the exact saved already-predicted coordinate bytes")
            _require(prediction["candidate_domain"]["model_binding_sha256"] == self.model_binding_sha256
                     and prediction["candidate_domain"]["eligible"] is True
                     and prediction["qualified_for_actual"] is True,
                     "the original candidate domain and new prediction qualification must remain bound")
            item = {
                "number": number, "source_query_number": prediction["number"],
                "alpha": prediction["alpha"],
                "candidate_array_sha256": prediction["candidate_array_sha256"],
                "candidate_physical_state_sha256": prediction["candidate_physical_state_sha256"],
                "candidate_domain": copy.deepcopy(prediction["candidate_domain"]),
                "actual_coordinate_application_was_not_repeated": True,
                "new_predictor_calls_here": 0}
            trace["trials"].append(item)
            try:
                result = actual.trial(q, prediction["alpha"], prediction, emit=emit)
                item.update(
                    actual_trial_receipt=copy.deepcopy(result.get("stdout_receipt")),
                    status=result["status"],
                    accepted_as_next_iterate=result["accepted_as_next_iterate"],
                    new_row_or_capacity_stop=result["new_row_or_capacity_stop"])
                if result["accepted_as_next_iterate"]:
                    trace.update(status="new-original-fourteen-gate-actual-acceptance",
                                 new_acceptances=1,
                                 accepted_source_query_number=prediction["number"])
                    break
                if result["new_row_or_capacity_stop"]:
                    trace["status"] = "actual-new-row-or-capacity-closes-fixed-direction"
                    break
            except Exception as error:
                item.update(status="raised", error=_error(error))
                trace.update(status="raised", error=_error(error))
                raise
        else:
            trace["status"] = "preselected-actual-candidates-completed-without-acceptance"
        trace.setdefault("status", "no-new-actual-acceptance")
        return trace

    def report(self):
        return {
            "schema": POLICY+"-report", "identity": copy.deepcopy(self.identity),
            "binding_sha256": self.binding_sha256,
            "summary": copy.deepcopy(self.summary), "all_queries": copy.deepcopy(self.records),
            "actual_selection": copy.deepcopy(self.actual_summary),
            "interval": copy.deepcopy(self.interval), "direction168": _vector(self.direction),
            "metric_predictor_cumulative_report": self.metric_predictor.report(),
            "shared_scalar_queries": self.ledger.counts["scalar_queries"],
            "raw_retention": {
                "best_semantic_query": self.capture.get("best_semantic_query"),
                "best_raw_source_query": self.capture.get("best_raw_source_query"),
                "best_raw_available": self.capture.get("best_raw_available", False),
                "best_raw_unavailable_reason": self.capture.get("best_raw_unavailable_reason"),
                "latest_partial_source_query": self.capture.get("latest_partial_source_query"),
                "only_capture_private_entries_contain_large_arrays": True,
                "other_successful_values_discarded_and_not_recoverable_from_hashes": True},
            "report_has_no_large_prediction_array_values": True,
            "all_original_actual_gates_remain_with_the_actual_owner": True}

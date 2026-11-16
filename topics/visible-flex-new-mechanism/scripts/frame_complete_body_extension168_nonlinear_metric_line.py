#!/usr/bin/env python3
"""Metric-only predictions at explicit actual complete168 candidate coordinates.

Import-only; no search, ordinary geometry, center/height primitive, hard-row
Jacobian, curvature gate or solver is invoked.  This is a new predictor
identity for a future separately budgeted task, not the small168 task.

The actual binary64 candidate is supplied directly.  No alpha or nominal
q0+alpha*delta is used to reconstruct it.  Fixed a/a_s and current U/T are
read from the paid first-jet bindings.  Current and candidate scalar_frame
calls preserve the original phase, c(v), and whole-circle Pi operator.

Height coefficient differences are exact Fractions of the two supplied
binary64 states.  Each height-speed increment is float(exact rational dot)
against the ORIGINAL binary64 null-density/P8-prime samples.  This is exact
coefficient/sample algebra before the final conversion, not an exact
transcendental or continuous-profile certificate.

All clocks and query limits belong to the future caller.  Local counters
record started/completed/failed preparation attempts and actual call entry;
they grant no resource budget.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import periodic_operator
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_complete_body_extension168 import (
    CompleteBody168Field, radial_columns, array_binding)
from frame_complete_body_extension168_joint_selected import _validate_first_jets


POLICY = "complete168-actual-candidate-nonlinear-metric-only-predictor-v1"
LABELS = ("coarse", "fine")
TANGENT_INDICES = tuple(range(154))+tuple(range(159, 167))
HEIGHT_INDICES = tuple(range(154, 159))+(167,)


def definition():
    return {
        "schema": POLICY,
        "proof": "R504-complete-168-parameter-line-second-metric-jets-and-curvature-PSD-remainders",
        "candidate_input": "literal already-applied binary64 candidate168",
        "no_alpha_argument_or_reconstruction": True,
        "same_complete_field_fixed_g_b0_reference_and_coordinate_map": True,
        "state_parameter_count": 168, "physical_parameter_count": 172,
        "current_inputs": "paid current U,T,e,f plus bound fixed a,a_s",
        "frame": "T=c(v)H(theta+u)+v*c(v)*e3; c=(1+v*v)^(-1/2)",
        "candidate_frame": "original field.scalar_frame at the actual candidate168",
        "periodic_operator": "original complete-circle periodic_operator(...,-1)",
        "floating_assembly_order": [
            "P=Pi(T_candidate-T_current_recomputed)",
            "Ps=Pi(Ts_candidate-Ts_current_recomputed)",
            "U=paid_U+a_s*P",
            "U=U+a*Ps",
            "U_z=U_z+height_speed_difference",
            "e=sum(U*U)-1;f=sum(U*T_candidate)",
            "eta=(abs(e)+sqrt(e*e+4*f*f))/2"],
        "height_only_path":
            "exact equality of all tangent coordinate bytes permits paid T and no scalar_frame/Pi",
        "height_coefficients":
            "exact Fraction(candidate binary64)-Fraction(current binary64) at 154..158,167",
        "height_density_basis":
            "original null_basis.values(radial) and original radial_columns(radial)['height']['b']",
        "height_increment":
            "each row float(sum(exact coefficient difference * exact rational of binary64 basis value))",
        "basis_samples_are_not_claimed_exact_transcendental_values": True,
        "mathematical_map_is_the_same_complete168_field": True,
        "floating_addition_and_FFT_path_differs_from_original_ordinary": True,
        "not_bitwise_equivalent_to_original_ordinary": True,
        "candidate_values_are_predictor_outputs_not_actual14_gate_receipts": True,
        "no_ordinary_geometry_or_position_jet_assembly": True,
        "no_center_or_height_primitive_query": True,
        "no_old_or_new_parameter_Jacobian": True,
        "no_curvature_or_hard_row_evaluation": True,
        "no_search_or_solver_or_developer_suite": True,
        "baseline_scalar_frames_prepared_lazily_and_shared_in_process": True,
        "scalar_frame_may_form_its_original_unused_Tss_and_auxiliary_fields": True,
        "all_new_calls_and_partial_outputs_are_owned_by_external_scope": True,
        "counter_semantics":
            "started counts preparation attempts; work_call_entered marks original frame/Pi/basis entry"}


def implementation_hashes():
    files = [Path(__file__)]
    for name in ("frame_collar_bvp.py", "frame_complete_body_extension168.py",
                 "frame_complete_body_extension168_joint_selected.py",
                 "frame_height_null_coordinates.py", "frame_entry_body_subspace.py"):
        files.append(Path(__file__).with_name(name))
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def _require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def _array(value, shape, name, *, owned=True):
    raw = np.asarray(value, dtype=np.float64)
    _require(raw.shape == tuple(shape) and np.all(np.isfinite(raw)),
             "finite "+name+" with the declared shape is required")
    result = raw.copy() if owned else raw.view()
    result.setflags(write=False)
    return result


def _same(left, right):
    a, b = np.asarray(left), np.asarray(right)
    return a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes()


def _vector(value):
    a = np.asarray(value, dtype=np.float64)
    return {"shape": list(a.shape), "dtype": a.dtype.str,
            "array_sha256": array_digest(a), "binary64": a.tolist(),
            "binary64_exact": [str(Q.from_float(float(v))) for v in a]}


def _error(error):
    return {"type": type(error).__name__, "message": str(error)}


class ActualCandidateMetricPredictor168:
    """One fixed current168 source, two paid grids, no internally granted budget.

    wall, when supplied, is called as wall(stage_string).  The enclosing task
    must debit a predictor query BEFORE calling predict and include imports,
    construction, partial failures and serialization in its scientific clock.

    predict returns necessary predicted first-jet arrays U,T,e,f,eta on each
    complete grid.  These are not actual gate receipts.  The caller owns their
    in-process lifetime and any declared original-stdout serialization.
    """

    def __init__(self, field, current168, radial, thetas, first_jet_bounds,
                 source_receipt, *, wall=None):
        self.wall = wall
        self._check("nonlinear-metric.constructor")
        _require(isinstance(field, CompleteBody168Field) and field.metric_free == 0,
                 "the frozen-metric complete168 field is required")
        _require(isinstance(thetas, dict) and set(thetas) == set(LABELS)
                 and isinstance(first_jet_bounds, dict)
                 and set(first_jet_bounds) == set(LABELS),
                 "both original coarse/fine grids and first-jet bindings are required")
        _require(isinstance(source_receipt, dict) and bool(source_receipt),
                 "the paid first-jet/source receipt is required")
        self.field = field
        self.current168 = _array(current168, (168,), "current168")
        field.validate_state(self.current168)
        rr = np.asarray(radial, dtype=np.float64)
        _require(rr.ndim == 1 and len(rr) >= 2, "one complete original radial grid is required")
        self.radial = _array(rr, rr.shape, "original radial")
        self.thetas, self.bounds, self.base = {}, {}, {}
        self.source_receipt = copy.deepcopy(source_receipt)
        for label in LABELS:
            th = np.asarray(thetas[label], dtype=np.float64)
            _require(th.ndim == 1, "one complete original angular grid is required")
            self.thetas[label] = _array(th, th.shape, label+" theta")
            bound = first_jet_bounds[label]
            q, r, theta, data = _validate_first_jets(
                field, self.current168, self.radial, self.thetas[label], bound)
            _require(_same(q, self.current168) and _same(r, self.radial)
                     and _same(theta, self.thetas[label]),
                     "paid first-jet state/grid bytes differ")
            self.bounds[label] = bound
            self.base[label] = data
        _require(len(self.thetas["fine"]) == 2*len(self.thetas["coarse"]),
                 "the original coarse/fine angular grids are required")
        for name in ("a", "a_s"):
            _require(_same(self.base["coarse"]["metric"][name],
                          self.base["fine"]["metric"][name]),
                     "both grids must use the same original fixed radial metric")
        self.metric = self.base["coarse"]["metric"]
        self.field_sha256 = field.definition_sha256
        self.coordinate_sha256 = field.coordinate_definition_sha256
        self.current_physical_sha256 = digest(field.identity(self.current168))
        self.source_identity = {
            "schema": POLICY+"-current-source",
            "definition_sha256": digest(definition()),
            "field_definition_sha256": self.field_sha256,
            "coordinate_definition_sha256": self.coordinate_sha256,
            "current_physical_state_sha256": self.current_physical_sha256,
            "current168_array_sha256": array_digest(self.current168),
            "source_receipt": copy.deepcopy(source_receipt),
            "radial": array_binding(self.radial),
            "grids": {label: {
                "theta": array_binding(self.thetas[label]),
                "paid_first_jet_binding_sha256": self.bounds[label]["binding_sha256"],
                "paid_first_jet_arrays": {name: array_binding(self.base[label][name])
                                         for name in ("U", "T", "e", "f")}}
                for label in LABELS},
            "fixed_metric": {name: array_binding(self.metric[name]) for name in ("a", "a_s")}}
        self.source_binding_sha256 = digest(self.source_identity)
        self._baseline_frames = {}
        self._height_basis = self._height_basis_rationals = None
        self._height_basis_receipt = None
        self.events = []
        self.counts = {kind+suffix: 0
                      for kind in ("candidate_predictions", "baseline_scalar_frames",
                                   "candidate_scalar_frames", "periodic_operator_calls",
                                   "height_density_basis_reads", "completed_grid_predictions")
                      for suffix in ("_started", "_completed", "_failed")}
        self._check("nonlinear-metric.constructor.complete")

    def _check(self, stage):
        if self.wall is not None:
            _require(callable(self.wall), "wall must accept one stage string")
            self.wall(str(stage))

    def _assert_source(self):
        self.field._assert_context()
        _require(self.field.definition_sha256 == self.field_sha256
                 and self.field.coordinate_definition_sha256 == self.coordinate_sha256
                 and digest(self.field.identity(self.current168)) == self.current_physical_sha256,
                 "the frozen physical field/current point changed")
        for label in LABELS:
            _validate_first_jets(self.field, self.current168, self.radial,
                                 self.thetas[label], self.bounds[label])

    def _start(self, kind, **metadata):
        self.counts[kind+"_started"] += 1
        event = {"kind": kind, "ordinal": self.counts[kind+"_started"],
                 "status": "started", "work_call_entered": False,
                 **copy.deepcopy(metadata)}
        self.events.append(event)
        return event, time.monotonic()

    def _finish(self, kind, event, started, error=None, **metadata):
        event.update(copy.deepcopy(metadata))
        event["elapsed_seconds"] = float(time.monotonic()-started)
        event["status"] = "complete" if error is None else "raised"
        self.counts[kind+("_completed" if error is None else "_failed")] += 1
        if error is not None:
            event["error"] = _error(error)

    def _failed_or_blocked(self, kind, event, started, error):
        if event["status"] == "started":
            self._finish(kind, event, started, error)
        else:
            # Completed work remains completed and available in capture/cache.
            # A subsequent wall/metadata exception must not double-debit it.
            event["post_completion_exception"] = _error(error)
            event["elapsed_seconds_at_exception"] = float(time.monotonic()-started)
            event["completed_work_retained_but_return_blocked"] = True

    def _frame(self, state, label, role, capture):
        kind = "baseline_scalar_frames" if role == "baseline" else "candidate_scalar_frames"
        event, started = self._start(
            kind, grid=label, state168_array_sha256=array_digest(state),
            source_binding_sha256=self.source_binding_sha256)
        public = capture.setdefault(role+"_frame_preparations", [])
        public.append(event)
        try:
            self._check("nonlinear-metric."+role+"-frame."+label)
            event["work_call_entered"] = True
            grid, fields, frame = self.field.scalar_frame(state, self.radial, self.thetas[label])
            # Preserve returned paid work before shape/finiteness/hash/check
            # failures.  The caller decides how to serialize a failed product.
            raw = {"T": frame.get("T"), "Ts": frame.get("Ts")}
            capture["_arrays"].setdefault(role+"_frames", {})[label] = raw
            shape = (len(self.radial), len(self.thetas[label]), 3)
            T = _array(raw["T"], shape, role+"/"+label+"/T")
            Ts = _array(raw["Ts"], shape, role+"/"+label+"/Ts")
            record = {
                "schema": POLICY+"-raw-scalar-frame",
                "role": role, "grid": label,
                "field_definition_sha256": self.field_sha256,
                "state168_array_sha256": array_digest(state),
                "radial": array_binding(self.radial),
                "theta": array_binding(self.thetas[label]),
                "scalar_arrays": {
                    name+"/"+jet: array_binding(np.asarray(fields[name][jet], dtype=np.float64))
                    for name in ("u", "v") for jet in ("value", "s")},
                "T": array_binding(T), "Ts": array_binding(Ts),
                "original_scalar_frame_called_at_actual_state": True,
                "phase": "theta+u", "normalizer": "(1+v*v)^(-1/2)",
                "unused_original_scalar_frame_outputs_not_ordinary_geometry": True}
            if role == "baseline":
                difference = T-np.asarray(self.base[label]["T"])
                record.update(
                    recomputed_T_bitwise_equal_paid_T=_same(T, self.base[label]["T"]),
                    recomputed_T_minus_paid_T_maximum_absolute=float(np.max(abs(difference))),
                    numerical_difference_is_reported_not_a_new_acceptance_tolerance=True)
            result = {"T": T, "Ts": Ts, "identity": record,
                      "binding_sha256": digest(record)}
            capture["_arrays"][role+"_frames"][label] = {"T": T, "Ts": Ts}
            if role == "baseline":
                self._baseline_frames[label] = result
            self._finish(kind, event, started, raw_frame_identity=record,
                         raw_frame_binding_sha256=result["binding_sha256"])
            self._check("nonlinear-metric."+role+"-frame."+label+".complete")
            return result
        except Exception as error:
            self._failed_or_blocked(kind, event, started, error)
            raise

    def _baseline_frame(self, label, capture):
        if label not in self._baseline_frames:
            value = self._frame(self.current168, label, "baseline", capture)
            self._baseline_frames[label] = value
        else:
            capture.setdefault("baseline_frame_cache_hits", []).append({
                "grid": label,
                "raw_frame_binding_sha256": self._baseline_frames[label]["binding_sha256"],
                "new_scalar_frame_calls": 0})
        return self._baseline_frames[label]

    def _height_difference(self, candidate, capture):
        differences = tuple(Q.from_float(float(candidate[i]))
                            -Q.from_float(float(self.current168[i])) for i in HEIGHT_INDICES)
        coefficient_record = {
            "indices": list(HEIGHT_INDICES),
            "current_binary64_exact": [str(Q.from_float(float(self.current168[i])))
                                      for i in HEIGHT_INDICES],
            "candidate_binary64_exact": [str(Q.from_float(float(candidate[i])))
                                        for i in HEIGHT_INDICES],
            "coefficient_differences_exact": [str(value) for value in differences],
            "not_float_candidate_minus_current_then_fraction": True}
        capture["height_coefficient_difference"] = coefficient_record
        if not any(differences):
            result = np.zeros(len(self.radial), dtype=np.float64)
            result.setflags(write=False)
            receipt = {**coefficient_record, "zero_height_direction": True,
                       "height_density_basis_read_required": False,
                       "height_speed_difference": array_binding(result)}
            capture["height_speed_difference"] = receipt
            return result, receipt
        if self._height_basis is None:
            event, started = self._start("height_density_basis_reads",
                                        source_binding_sha256=self.source_binding_sha256)
            capture["height_density_basis_preparation"] = event
            try:
                self._check("nonlinear-metric.height-basis")
                event["work_call_entered"] = True
                old = self.field.original_field.null_basis.values(self.radial)
                new = radial_columns(self.radial)["height"]["b"]
                raw = np.column_stack((
                    _array(old, (len(self.radial), 5), "original five null densities"),
                    _array(new, (len(self.radial),), "original gamma P8prime density")))
                capture["_arrays"]["new_height_density_basis"] = raw
                basis = _array(raw, (len(self.radial), 6), "same original six height densities")
                exact = tuple(tuple(Q.from_float(float(v)) for v in row) for row in basis)
                record = {
                    "schema": POLICY+"-height-density-samples",
                    "radial": array_binding(self.radial), "basis": array_binding(basis),
                    "column_order": list(HEIGHT_INDICES),
                    "old_density_source": "original_field.null_basis.values(radial)",
                    "new_density_source": "radial_columns(radial)['height']['b']",
                    "new_density_is_P8_xi_prime_without_an_extra_1_over_length": True,
                    "no_reference_b0_or_center_primitive_evaluation": True,
                    "sampled_binary64_basis_not_exact_transcendental_values": True}
                self._height_basis, self._height_basis_rationals = basis, exact
                self._height_basis_receipt = record
                capture["_arrays"]["new_height_density_basis"] = basis
                self._finish("height_density_basis_reads", event, started, receipt=record)
                self._check("nonlinear-metric.height-basis.complete")
            except Exception as error:
                self._failed_or_blocked("height_density_basis_reads", event, started, error)
                raise
        self._check("nonlinear-metric.exact-height-difference")
        values = []
        for row in self._height_basis_rationals:
            values.append(float(sum((d*b for d, b in zip(differences, row)), Q(0))))
        result = _array(values, (len(self.radial),), "actual-coordinate height-speed difference")
        receipt = {
            **coefficient_record,
            "zero_height_direction": False,
            "height_density_basis": copy.deepcopy(self._height_basis_receipt),
            "height_density_basis_cache_is_current_process_only": True,
            "height_speed_difference": array_binding(result),
            "algebra": "float(exact rational coefficient/sample dot) at each original radial point",
            "basis_evaluation_and_final_float_conversion_are_not_exact_real_geometry": True}
        capture["_arrays"]["height_speed_difference"] = result
        capture["height_speed_difference"] = receipt
        self._check("nonlinear-metric.exact-height-difference.complete")
        return result, receipt

    def _pi(self, values, label, name, capture):
        event, started = self._start(
            "periodic_operator_calls", grid=label, argument=name,
            original_order=-1, source_binding_sha256=self.source_binding_sha256)
        try:
            self._check("nonlinear-metric.Pi."+label+"."+name)
            event["work_call_entered"] = True
            result = periodic_operator(values, -1)
            capture["_arrays"].setdefault("pending_periodic_increments", {}).setdefault(label, {})[name] = result
            result = _array(result, values.shape, "complete Pi/"+name)
            self._finish("periodic_operator_calls", event, started,
                         input_array=array_binding(values), output_array=array_binding(result))
            self._check("nonlinear-metric.Pi."+label+"."+name+".complete")
            return result
        except Exception as error:
            self._failed_or_blocked("periodic_operator_calls", event, started, error)
            raise

    def predict(self, actual_candidate168, *, candidate_receipt, capture=None):
        """Predict one explicit actual candidate, retaining any completed grid.

        No acceptance, box, curvature, line search or budget grant occurs.
        capture is optional but, when supplied, must be empty.  On failure it
        retains the actual candidate, first-frame failures and all completed
        new grid arrays.  A later run must not silently recompute that work.
        """
        sink = {} if capture is None else capture
        _require(isinstance(sink, dict) and not sink, "an empty per-candidate capture is required")
        sink.update(schema=POLICY+"-candidate-capture", status="started",
                    completed_grids={}, _arrays={})
        before = dict(self.counts)
        event, started = self._start(
            "candidate_predictions", source_binding_sha256=self.source_binding_sha256)
        sink["prediction_event"] = event
        try:
            self._check("nonlinear-metric.predict.entry")
            self._assert_source()
            event["work_call_entered"] = True
            _require(isinstance(candidate_receipt, dict) and bool(candidate_receipt),
                     "the caller's actual-candidate provenance is required")
            candidate = _array(actual_candidate168, (168,), "actual candidate168")
            self.field.validate_state(candidate)
            candidate_record = _vector(candidate)
            sink["actual_candidate168"] = candidate_record
            sink["candidate_receipt"] = copy.deepcopy(candidate_receipt)
            candidate_physical = digest(self.field.identity(candidate))
            tangent = np.asarray(TANGENT_INDICES, dtype=np.int64)
            same_tangent = _same(candidate[tangent], self.current168[tangent])
            height, height_receipt = self._height_difference(candidate, sink)
            grids, identities = {}, {}
            for label in LABELS:
                item, tick = self._start(
                    "completed_grid_predictions", grid=label,
                    candidate168_array_sha256=array_digest(candidate),
                    source_binding_sha256=self.source_binding_sha256)
                sink.setdefault("grid_prediction_events", []).append(item)
                try:
                    self._check("nonlinear-metric.predict."+label)
                    item["work_call_entered"] = True
                    base = self.base[label]
                    nr, nt = len(self.radial), len(self.thetas[label])
                    if same_tangent:
                        T = _array(base["T"], (nr, nt, 3), "paid unchanged T", owned=False)
                        U = np.asarray(base["U"], dtype=np.float64).copy()
                        baseline_frame_identity = None
                        candidate_frame_identity = {
                            "schema": POLICY+"-unchanged-tangent-frame",
                            "all_original154_and_new8_tangent_coordinate_bytes_identical": True,
                            "paid_T": array_binding(T),
                            "new_scalar_frame_and_Pi_calls": 0}
                    else:
                        baseline = self._baseline_frame(label, sink)
                        actual = self._frame(candidate, label, "candidate", sink)
                        dT = actual["T"]-baseline["T"]
                        dTs = actual["Ts"]-baseline["Ts"]
                        P = self._pi(dT, label, "delta_T", sink)
                        Ps = self._pi(dTs, label, "delta_Ts", sink)
                        T = actual["T"]
                        U = np.asarray(base["U"])+np.asarray(self.metric["a_s"])[:, None, None]*P
                        U = U+np.asarray(self.metric["a"])[:, None, None]*Ps
                        baseline_frame_identity = copy.deepcopy(baseline["identity"])
                        candidate_frame_identity = copy.deepcopy(actual["identity"])
                    U[..., 2] += height[:, None]
                    # This is the declared new assembly, not an ordinary call.
                    raw = {
                        "U": U, "T": T,
                        "e": np.sum(U*U, axis=2)-1.,
                        "f": np.sum(U*T, axis=2)}
                    raw["eta"] = .5*(abs(raw["e"])
                                    +np.sqrt(raw["e"]*raw["e"]+4*raw["f"]*raw["f"]))
                    sink["_arrays"].setdefault("candidate_grids", {})[label] = raw
                    values = {
                        name: _array(value, (nr, nt, 3) if name in ("U", "T") else (nr, nt),
                                     label+"/"+name, owned=False)
                        for name, value in raw.items()}
                    index = np.unravel_index(int(np.argmax(values["eta"])), (nr, nt))
                    identity = {
                        "schema": POLICY+"-predicted-grid",
                        "grid": label,
                        "source_binding_sha256": self.source_binding_sha256,
                        "paid_first_jet_binding_sha256": self.bounds[label]["binding_sha256"],
                        "actual_candidate168_array_sha256": array_digest(candidate),
                        "candidate_physical_state_sha256": candidate_physical,
                        "radial": array_binding(self.radial),
                        "theta": array_binding(self.thetas[label]),
                        "baseline_raw_frame_identity": baseline_frame_identity,
                        "candidate_raw_frame_identity": candidate_frame_identity,
                        "height_speed_difference_receipt": copy.deepcopy(height_receipt),
                        "predicted_arrays": {name: array_binding(value) for name, value in values.items()},
                        "floating_assembly_definition_sha256": digest(definition()),
                        "same_tangent_coordinate_path": bool(same_tangent),
                        "original_ordinary_was_not_evaluated": True,
                        "not_an_actual14_gate_receipt": True}
                    record = {
                        "binding_sha256": digest(identity), "identity": identity,
                        "eta_maximum": float(values["eta"][index]),
                        "eta_maximum_location": {
                            "radial_index": int(index[0]), "theta_index": int(index[1]),
                            "s": float(self.radial[index[0]]),
                            "theta": float(self.thetas[label][index[1]]),
                            "e": float(values["e"][index]), "f": float(values["f"][index])},
                        "point_count": nr*nt}
                    grids[label], identities[label] = values, record
                    sink["_arrays"]["candidate_grids"][label] = values
                    sink["completed_grids"][label] = copy.deepcopy(record)
                    self._finish("completed_grid_predictions", item, tick, receipt=record)
                    # Completed U/T/e/f/eta and raw frame inputs are retained.
                    # Intermediate Pi outputs need not be duplicated on success.
                    sink["_arrays"].get("pending_periodic_increments", {}).pop(label, None)
                    self._check("nonlinear-metric.predict."+label+".complete")
                except Exception as error:
                    self._failed_or_blocked("completed_grid_predictions", item, tick, error)
                    raise
            identity = {
                "schema": POLICY+"-complete-candidate-pair",
                "definition": definition(),
                "source_binding_sha256": self.source_binding_sha256,
                "actual_candidate168": candidate_record,
                "candidate_physical_state_sha256": candidate_physical,
                "candidate_receipt": copy.deepcopy(candidate_receipt),
                "grid_binding_sha256": {label: identities[label]["binding_sha256"] for label in LABELS},
                "no_alpha_or_unrounded_line_point_was_substituted": True,
                "original_two_grid_actual_gates_remain_required": True,
                "new_solver_or_search_calls": 0}
            result = {
                "grids": grids, "binding": identity, "binding_sha256": digest(identity),
                "diagnostics": {
                    "schema": POLICY+"-candidate-diagnostics",
                    "grid_receipts": identities,
                    "two_grid_predicted_eta": max(identities[label]["eta_maximum"] for label in LABELS),
                    "elapsed_seconds_before_return": float(time.monotonic()-started),
                    "counts_during_call": {key: self.counts[key]-before[key] for key in self.counts},
                    "height_speed_difference": copy.deepcopy(height_receipt),
                    "ordinary_calls": 0, "center_or_height_primitive_calls": 0,
                    "parameter_J_calls": 0, "hard_row_or_curvature_calls": 0,
                    "not_a_strict_interval_or_roundoff_error_certificate": True}}
            sink.update(status="complete", result_binding_sha256=result["binding_sha256"],
                        diagnostics=copy.deepcopy(result["diagnostics"]))
            self._finish("candidate_predictions", event, started,
                         result_binding_sha256=result["binding_sha256"],
                         two_grid_predicted_eta=result["diagnostics"]["two_grid_predicted_eta"])
            result["diagnostics"]["counts_during_call"] = {
                key: self.counts[key]-before[key] for key in self.counts}
            sink["diagnostics"] = copy.deepcopy(result["diagnostics"])
            self._check("nonlinear-metric.predict.complete")
            return result
        except Exception as error:
            sink.update(status="raised", error=_error(error),
                        elapsed_seconds_before_raise=float(time.monotonic()-started))
            self._failed_or_blocked("candidate_predictions", event, started, error)
            sink["counts_during_call"] = {
                key: self.counts[key]-before[key] for key in self.counts}
            raise

    def report(self):
        """Small metadata only; actual arrays remain in returns/capture."""
        return {
            "schema": POLICY+"-predictor-report",
            "source_identity": copy.deepcopy(self.source_identity),
            "source_binding_sha256": self.source_binding_sha256,
            "counts": dict(self.counts), "events": copy.deepcopy(self.events),
            "entered_original_call_counts": {
                kind: sum(event["kind"] == kind and event["work_call_entered"]
                          for event in self.events)
                for kind in ("baseline_scalar_frames", "candidate_scalar_frames",
                             "periodic_operator_calls", "height_density_basis_reads")},
            "prepared_baseline_frames": {
                label: {"binding_sha256": value["binding_sha256"],
                        "identity": copy.deepcopy(value["identity"])}
                for label, value in self._baseline_frames.items()},
            "height_density_basis": copy.deepcopy(self._height_basis_receipt),
            "no_budget_was_granted_or_reset_by_this_module": True,
            "no_original_ordinary_or_acceptance_gate_called": True,
            "current_task_import_does_not_invoke_prediction": True}

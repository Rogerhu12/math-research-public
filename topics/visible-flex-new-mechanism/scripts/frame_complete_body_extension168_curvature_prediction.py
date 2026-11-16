#!/usr/bin/env python3
"""Current complete168 curvature prediction without X, center or ordinary.

Import-only.  The caller supplies paid current U/T first-jet bindings and
bound fixed a/a_s/a_ss on the original radial grid.  One original scalar
frame on each complete theta grid and one current height_jets call provide
the missing inputs.  All three whole-circle primitives Pi(T), Pi(Ts),
Pi(Tss) are retained.  This is not a Tss-only shortcut.

The module constructs only Xs/Xt/Xss/Xst/Xtt.  It invokes the original
curvature_values and independent_principal_curvatures formulas on these
concrete predictor arrays, including their actual first fundamental form.
It never substitutes the target metric or G=1.  No X, center integral,
fixed height primitive, ordinary geometry, parameter J, search, optimization solver or
all-fourteen actual gate decision is evaluated.

This is the same mathematical current surface with an explicitly new
floating assembly.  In particular current height_jets groups the height
terms differently from the ordinary's staged null/gamma additions.  No
bitwise replay, interval bound or actual acceptance certificate is claimed.
All costs and failures belong to a future separately authorized caller.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import periodic_operator
from frame_curvature_psd import curvature_values, independent_principal_curvatures
from frame_height_null_coordinates import digest
from frame_complete_body_extension168 import (
    CompleteBody168Field, array_binding, _validate_grid)
from frame_complete_body_extension168_joint_selected import _context, _validate_first_jets


POLICY = "complete168-current-firstjet-curvature-only-predictor-v1"
LABELS = ("coarse", "fine")
METRIC_KEYS = ("a", "a_s", "a_ss")
FRAME_KEYS = ("T", "Ts", "Tss", "Ttheta")
POSITION_KEYS_WITHOUT_X = ("Xs", "Xt", "Xss", "Xst", "Xtt")
CURVATURE_ROW_GROUPS = (7, 8, 9, 10)
CURVATURE_ROW_NAMES = (
    "plus_trace", "plus_determinant", "minus_trace", "minus_determinant")


def definition():
    return {
        "schema": POLICY,
        "proof": "R504-complete-168-parameter-line-second-metric-jets-and-curvature-PSD-remainders",
        "state": "literal current binary64 state168 bound to supplied paid first jets",
        "physical_parameter_count": 172, "independent_parameter_count": 168,
        "no_alpha_or_nominal_direction_reconstruction": True,
        "fixed_g_b0_reference_and_all_original_coordinates_retained": True,
        "required_paid_inputs": ["U", "T", "e", "f", "a", "a_s", "a_ss"],
        "new_source_inputs": ["original scalar_frame Ts/Tss/Ttheta",
                              "original current height_jets b_s"],
        "complete_periodic_primitives": [
            "P=Pi(paid T)", "Ps=Pi(current scalar_frame Ts)",
            "Pss=Pi(current scalar_frame Tss)"],
        "assembly": [
            "Xs=paid U", "Xt=a*paid T",
            "Xss=a_ss*P+2*a_s*Ps+a*Pss; Xss_z+=current b_s",
            "Xst=a_s*paid T+a*current Ts",
            "Xtt=a*current Ttheta"],
        "normalized_second_jets": [
            "B=Xss", "C=Xst/a", "D=Xtt/a^2"],
        "curvature":
            "original curvature_values: w=Xs cross (Xt/a), q=|w|, actual I and K",
        "direct_kappa": "original independent_principal_curvatures via actual-I Cholesky",
        "scaled_rows": "original factors cap/scale,(cap/scale)^2 repeated for signs",
        "height_call_path": [
            "CompleteBody168Field.height_jets(current168,radial)",
            "FiveHeightField.height_jets(current159,radial)",
            "SingleQ.height_jets(reference_evaluation_state,radial)",
            "IndependentHeight.height_baseline plus original height basis derivatives",
            "five original null columns plus current gamma density jets"],
        "height_path_has_no_position_or_fixed_height_primitive_call": True,
        "height_baseline_or_scalar_frame_cold_cost_is_not_assumed_zero": True,
        "paid_T_is_authoritative_and_recomputed_T_difference_is_reported": True,
        "actual_I_not_target_g_and_no_unit_T_shortcut": True,
        "not_bitwise_original_ordinary_replay": True,
        "not_a_continuous_interval_or_roundoff_certificate": True,
        "only_curvature_predictor_not_actual_fourteen_gate_receipt": True,
        "no_X_or_center_or_ordinary_geometry": True,
        "no_parameter_Jacobian_or_search_or_optimization_solver": True,
        "no_budget_granted_or_reset": True,
        "external_scope_must_charge_all_calls_failures_and_output": True}


def implementation_hashes():
    names = (
        Path(__file__).name, "frame_complete_body_extension168.py",
        "frame_complete_body_extension168_joint_selected.py",
        "frame_collar_bvp.py", "frame_curvature_psd.py",
        "frame_metric_budget_restoration_rows.py",
        "frame_five_height_field.py", "frame_entry_single_q.py",
        "frame_independent_height.py", "frame_height_null_coordinates.py")
    root = Path(__file__).parent
    return {name: hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names}


def _require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def _same(left, right):
    a, b = np.asarray(left), np.asarray(right)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def _array(value, shape, name, *, owned=True):
    a = np.asarray(value, dtype=np.float64)
    _require(a.shape == tuple(shape) and np.all(np.isfinite(a)),
             "finite original-shape array required: "+name)
    a = a.copy() if owned else a.view()
    a.setflags(write=False)
    return a


def _error(error):
    return {"type": type(error).__name__, "message": str(error)}


def _wall(wall, stage):
    if wall is not None:
        wall(str(stage))


def _metric_identity(field, radial, arrays, source_receipt):
    return {
        "schema": POLICY+"-fixed-metric",
        "field_definition_sha256": field.definition_sha256,
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "original_field_coordinate_definition_sha256":
            field.original_field.coordinate_definition_sha256,
        "ordinary_evaluation_definition_sha256": digest(field.evaluation_definition()),
        "metric_free": int(field.metric_free),
        "radial": array_binding(radial),
        "arrays": {key: array_binding(arrays[key]) for key in METRIC_KEYS},
        "source_receipt": copy.deepcopy(source_receipt),
        "same_frozen_g_for_all_state168_not_a_refit": True}


def bind_current_168_curvature_metric(field, radial, metric, source_receipt):
    """Bind existing fixed a/a_s/a_ss; no metric/geometry query is performed.

    The caller must supply a source receipt for these actual arrays.  This
    helper is metadata/array selection, not a mathematical verification of
    caller provenance.  No zero a_ss surrogate or numerical derivative is
    created.  A future request must pin the source/binding independently.
    """
    _context(field)
    rr = np.asarray(radial, dtype=np.float64)
    _require(rr.ndim == 1 and len(rr) >= 2 and rr[0] == 0.
             and np.all(np.isfinite(rr)) and np.all(np.diff(rr) > 0),
             "original zero-anchored increasing radial grid required")
    r = _array(rr, rr.shape, "radial")
    _require(isinstance(metric, dict) and isinstance(source_receipt, dict)
             and bool(source_receipt), "existing metric arrays and source receipt required")
    arrays = {key: _array(metric.get(key), (len(r),), key) for key in METRIC_KEYS}
    _require(np.all(arrays["a"] > 0), "the original fixed positive a is required")
    identity = _metric_identity(field, r, arrays, source_receipt)
    return {
        "schema": POLICY+"-bound-fixed-metric",
        "radial": r, "data": arrays, "identity": identity,
        "binding_sha256": digest(identity),
        "metric_geometry_and_J_calls": 0}


def _validate_metric(field, radial, bound):
    _require(isinstance(bound, dict)
             and bound.get("schema") == POLICY+"-bound-fixed-metric",
             "explicit bound fixed a/a_s/a_ss required")
    identity, arrays = bound.get("identity"), bound.get("data")
    _require(isinstance(identity, dict) and isinstance(arrays, dict),
             "fixed metric identity/data required")
    r = np.asarray(radial, dtype=np.float64)
    _require(_same(bound.get("radial"), r)
             and bound.get("binding_sha256") == digest(identity)
             and identity == _metric_identity(
                 field, r, arrays, identity.get("source_receipt")),
             "fixed metric field/grid/reference/content binding changed")
    for key in METRIC_KEYS:
        _array(arrays.get(key), (len(r),), "bound-"+key, owned=False)
    _require(np.all(arrays["a"] > 0), "fixed a must remain positive")
    return arrays


class _Trace:
    """Local accounting only; external wall/ledger owns every resource limit."""
    def __init__(self, wall, capture):
        self.wall, self.capture = wall, capture
        self.events = capture.setdefault("events", [])
        self.counts = {}

    def run(self, kind, operation, retain, **metadata):
        event = {
            "kind": kind, "status": "started", "work_call_entered": False,
            **copy.deepcopy(metadata)}
        counts = self.counts.setdefault(kind, {"started": 0, "entered": 0,
                                               "completed": 0, "failed": 0})
        counts["started"] += 1
        event["ordinal"] = counts["started"]
        self.events.append(event)
        tick = time.monotonic()
        try:
            _wall(self.wall, "curvature-predictor."+kind)
            event["work_call_entered"] = True
            counts["entered"] += 1
            value = operation()
            # Retain real returned work before post-call scope checks.
            retain(value)
            counts["completed"] += 1
            event.update(status="complete", seconds=float(time.monotonic()-tick))
            _wall(self.wall, "curvature-predictor."+kind+".complete")
            return value, event
        except Exception as error:
            if event["status"] == "started":
                counts["failed"] += 1
                event.update(status="raised", error=_error(error),
                             seconds=float(time.monotonic()-tick))
            else:
                event.update(post_completion_error=_error(error),
                             completed_work_retained_but_return_blocked=True,
                             seconds_at_exception=float(time.monotonic()-tick))
            raise


def _current_frame(field, q, radial, theta, label, trace, capture):
    def retain(value):
        grid, fields, frame = value
        capture["_arrays"].setdefault("returned_raw_frames", {})[label] = {
            key: frame.get(key) for key in FRAME_KEYS}
    raw, event = trace.run(
        "scalar_frame", lambda: field.scalar_frame(q, radial, theta), retain,
        grid=label, state168=array_binding(q))
    grid, fields, frame = raw
    shape = (len(radial), len(theta), 3)
    arrays = {key: _array(frame.get(key), shape, label+"/"+key, owned=False)
              for key in FRAME_KEYS}
    identity = {
        "schema": POLICY+"-current-scalar-frame", "grid": label,
        "field_definition_sha256": field.definition_sha256,
        "state168": array_binding(q), "radial": array_binding(radial),
        "theta": array_binding(theta),
        "scalar_arrays": {
            name+"/"+jet: array_binding(np.asarray(fields[name][jet], dtype=np.float64))
            for name in ("u", "v") for jet in ("value", "s", "ss", "theta")},
        "frame_arrays": {key: array_binding(value) for key, value in arrays.items()},
        "same_actual_phase_theta_plus_u_and_c_of_v": True}
    event.update(raw_frame_identity=identity, raw_frame_binding_sha256=digest(identity))
    capture["_arrays"]["returned_raw_frames"][label] = arrays
    return arrays, identity


def _current_height(field, q, radial, trace, capture):
    def retain(value):
        capture["_arrays"]["returned_current_height_jets"] = value
    raw, event = trace.run(
        "height_jets", lambda: field.height_jets(q, radial), retain,
        state168=array_binding(q), radial=array_binding(radial))
    _require(isinstance(raw, dict), "original current height_jets dictionary required")
    arrays = {key: _array(raw.get(key), (len(radial),), "height/"+key, owned=False)
              for key in ("b", "b_s", "b_ss")}
    old = field.original_field
    identity = {
        "schema": POLICY+"-current-height-jets",
        "state168": array_binding(q), "radial": array_binding(radial),
        "field_definition_sha256": field.definition_sha256,
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "old_null_basis_identity_sha256": old.null_basis.identity_sha256,
        "old_null_basis_evaluation_definition_sha256":
            digest(old.null_basis.evaluation_definition()),
        "fixed_height_base_definition_sha256": digest(field.height_base_definition),
        "current_arrays": {key: array_binding(value) for key, value in arrays.items()},
        "source": "original field.height_jets at literal current168",
        "current_null_and_gamma_height_terms_retained": True,
        "no_center_or_fixed_height_primitive_query": True,
        "only_b_s_is_used_in_curvature_assembly": True}
    capture["_arrays"]["returned_current_height_jets"] = arrays
    capture["height_identity"] = identity
    event.update(height_identity=identity, height_binding_sha256=digest(identity))
    return arrays, identity


def _pi(value, key, label, trace, capture):
    def retain(result):
        capture["_arrays"].setdefault("periodic_primitives", {}).setdefault(label, {})[key] = result
    answer, event = trace.run(
        "periodic_primitive", lambda: periodic_operator(value, -1), retain,
        grid=label, source_key=key, order=-1, input_array=array_binding(value))
    out = _array(answer, value.shape, label+"/Pi"+key, owned=False)
    event["output_array"] = array_binding(out)
    return out


def predict_current_168_curvature(
        field, state168, radial, thetas, first_jet_bounds, metric_bound, cfg, *,
        source_receipt, wall=None, capture=None):
    """Return full two-grid curvature predictions at one explicit current q.

    first_jet_bounds use bind_current_168_first_jets and may name original
    paid ordinary or explicitly new metric-predictor provenance.  The source
    is never relabeled as actual ordinary.  metric_bound comes from the
    pure binding helper above and includes a_ss, absent from a basic first
    jet record.  cfg is the unmodified original physical-row configuration.

    Only this function performs new curvature predictor work.  The caller
    must debit its own new query/call ledger before entry; there is no
    internally granted clock, quota, search, retry or automatic continuation.
    Supply capture to retain completed grids and all partial raw work.
    """
    started = time.monotonic()
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty per-query capture required")
    sink.update(schema=POLICY+"-capture", status="started", completed_grids={},
                _arrays={}, events=[])
    trace = _Trace(wall, sink)
    try:
        _wall(wall, "curvature-predictor.entry")
        _context(field)
        _require(isinstance(field, CompleteBody168Field) and field.metric_free == 0,
                 "the actual fixed-g complete168 field is required")
        q = _array(field.validate_state(state168), (168,), "state168")
        rr = np.asarray(radial, dtype=np.float64)
        _require(rr.ndim == 1, "original radial vector required")
        r = _array(rr, rr.shape, "radial")
        _require(isinstance(thetas, dict) and set(thetas) == set(LABELS)
                 and isinstance(first_jet_bounds, dict)
                 and set(first_jet_bounds) == set(LABELS),
                 "both original coarse/fine complete grids and first jets required")
        _require(isinstance(cfg, dict) and isinstance(source_receipt, dict)
                 and bool(source_receipt), "original cfg and source provenance required")
        metric = _validate_metric(field, r, metric_bound)
        theta, paid = {}, {}
        for label in LABELS:
            q0, r0, th, data = _validate_first_jets(
                field, q, r, thetas[label], first_jet_bounds[label])
            _require(_same(q0, q) and _same(r0, r), "first-jet current state/radial differs")
            theta[label] = _array(th, th.shape, label+"/theta")
            for key in ("a", "a_s"):
                _require(_same(data["metric"][key], metric[key]),
                         "paid first-jet metric differs from bound curvature metric")
            paid[label] = data
        _require(len(theta["fine"]) == 2*len(theta["coarse"]),
                 "original coarse/fine circle association required")
        cap = float(Q(cfg["fixed_hard_curvature_cap_exact"]))
        scale = float(Q(cfg["curvature_scale_exact"]))
        area_floor = float(cfg["normal_area_numerical_floor"])
        row_tolerance = float(cfg["curvature_row_tolerance"])
        direct_tolerance = float(cfg["direct_curvature_tolerance"])
        _require(all(np.isfinite(x) for x in
                     (cap, scale, area_floor, row_tolerance, direct_tolerance))
                 and cap > 0 and scale > 0 and area_floor >= 0
                 and row_tolerance >= 0 and direct_tolerance >= 0,
                 "original finite curvature cap/scale/floor/tolerances required")
        factors = np.array([cap/scale, (cap/scale)**2, cap/scale, (cap/scale)**2])
        state_record = {
            **array_binding(q), "binary64": q.tolist(),
            "binary64_exact": [str(Q.from_float(float(v))) for v in q]}
        source = {
            "schema": POLICY+"-query-source", "definition": definition(),
            "field_definition_sha256": field.definition_sha256,
            "coordinate_definition_sha256": field.coordinate_definition_sha256,
            "physical_identity_sha256": digest(field.identity(q)),
            "state168": state_record, "configuration_sha256": digest(cfg),
            "source_receipt": copy.deepcopy(source_receipt),
            "fixed_metric_binding_sha256": metric_bound["binding_sha256"],
            "first_jet_binding_sha256": {
                label: first_jet_bounds[label]["binding_sha256"] for label in LABELS},
            "first_jet_source_identities": {
                label: copy.deepcopy(first_jet_bounds[label]["identity"]) for label in LABELS},
            "upstream_nonlinear_metric_prediction_is_not_relabelled_as_original_ordinary": True,
            "original_grid": {
                label: {"radial": array_binding(r), "theta": array_binding(theta[label])}
                for label in LABELS}}
        source_sha = digest(source)
        sink.update(source_identity=copy.deepcopy(source), source_binding_sha256=source_sha)
        height, height_identity = _current_height(field, q, r, trace, sink)
        results = {}
        a = metric["a"][:, None, None]
        ap = metric["a_s"][:, None, None]
        app = metric["a_ss"][:, None, None]
        for label in LABELS:
            _wall(wall, "curvature-predictor."+label)
            frame, frame_identity = _current_frame(
                field, q, r, theta[label], label, trace, sink)
            nr, nt = len(r), len(theta[label])
            U = _array(paid[label]["U"], (nr, nt, 3), label+"/paid-U", owned=False)
            T = _array(paid[label]["T"], (nr, nt, 3), label+"/paid-T", owned=False)
            frame_comparison = {
                "recomputed_T_bitwise_equal_paid_T": _same(frame["T"], T),
                "recomputed_T_minus_paid_T_maximum_absolute": float(np.max(abs(frame["T"]-T))),
                "discrepancy_is_a_report_not_a_new_acceptance_tolerance": True}
            P = _pi(T, "T", label, trace, sink)
            Ps = _pi(frame["Ts"], "Ts", label, trace, sink)
            Pss = _pi(frame["Tss"], "Tss", label, trace, sink)

            def assemble():
                B = app*P+2*ap*Ps+a*Pss
                B[..., 2] += height["b_s"][:, None]
                return {"Xs": U, "Xt": a*T, "Xss": B,
                        "Xst": ap*T+a*frame["Ts"], "Xtt": a*frame["Ttheta"]}

            def retain_jets(value):
                sink["_arrays"].setdefault("position_jets_without_X", {})[label] = value
            jets, assembly_event = trace.run(
                "position_derivative_assembly_without_X", assemble, retain_jets,
                grid=label, source_binding_sha256=source_sha)
            jets = {key: _array(jets[key], (nr, nt, 3), label+"/"+key, owned=False)
                    for key in POSITION_KEYS_WITHOUT_X}
            sink["_arrays"]["position_jets_without_X"][label] = jets
            assembly_event["position_arrays"] = {
                key: array_binding(value) for key, value in jets.items()}

            def retain_curvature(value):
                sink["_arrays"].setdefault("returned_curvature_values", {})[label] = value
            values, curvature_event = trace.run(
                "original_curvature_values",
                lambda: curvature_values(
                    jets, metric["a"][:, None], 1/cap, area_floor=area_floor),
                retain_curvature, grid=label, source_binding_sha256=source_sha,
                original_cap=cfg["fixed_hard_curvature_cap_exact"],
                original_scale=cfg["curvature_scale_exact"])

            def retain_principal(value):
                sink["_arrays"].setdefault("principal_curvatures", {})[label] = value
            principal, principal_event = trace.run(
                "original_independent_principal_curvatures",
                lambda: independent_principal_curvatures(values),
                retain_principal, grid=label, source_binding_sha256=source_sha)
            principal = _array(principal, (nr, nt, 2), label+"/principal-curvatures", owned=False)
            arrays = {
                "psd_rows_unscaled": _array(values["rows"], (nr, nt, 4), label+"/unscaled-PSD", owned=False),
                "psd_rows_scaled": _array(
                    values["rows"]*factors, (nr, nt, 4), label+"/original-scaled-PSD"),
                "principal_curvatures": principal,
                "normal_area": _array(values["q"], (nr, nt), label+"/normal-area", owned=False),
                "actual_I": _array(values["actual_I"], (nr, nt, 2, 2), label+"/actual-I", owned=False),
                "actual_II": _array(values["actual_II"], (nr, nt, 2, 2), label+"/actual-II", owned=False),
                "numerator_K": _array(values["numerator_K"], (nr, nt, 2, 2), label+"/K", owned=False)}
            absolute = abs(principal)
            at = np.unravel_index(int(np.argmax(absolute)), absolute.shape)
            minima = np.min(arrays["psd_rows_scaled"], axis=(0, 1))
            identity = {
                "schema": POLICY+"-predicted-grid", "grid": label,
                "source_binding_sha256": source_sha,
                "raw_frame_identity": frame_identity,
                "raw_frame_binding_sha256": digest(frame_identity),
                "paid_T_comparison": frame_comparison,
                "height_identity": copy.deepcopy(height_identity),
                "assembly": definition()["assembly"],
                "position_arrays_without_X": {key: array_binding(value) for key, value in jets.items()},
                "curvature_arrays": {key: array_binding(value) for key, value in arrays.items()},
                "groups": list(CURVATURE_ROW_GROUPS), "row_names": list(CURVATURE_ROW_NAMES),
                "original_scaled_row_factors": factors.tolist(),
                "normal_I_and_II_from_original_array_evaluator": True,
                "no_G_equals_one_or_target_metric_substitution": True,
                "not_an_original_ordinary_actual_gate_receipt": True}
            summary = {
                "maximum_absolute_principal_curvature": float(absolute[at]),
                "curvature_attainer": {
                    "radial_index": int(at[0]), "theta_index": int(at[1]),
                    "principal_index": int(at[2]),
                    "s": float(r[at[0]]), "theta": float(theta[label][at[1]]),
                    "principal_curvatures": principal[at[0], at[1]].tolist()},
                "scaled_curvature_row_minima": {
                    name: float(value) for name, value in zip(CURVATURE_ROW_NAMES, minima)},
                "minimum_normal_area": float(np.min(arrays["normal_area"])),
                "predictor_PSD_with_original_tolerance": bool(np.all(minima >= -row_tolerance)),
                "predictor_direct_cap_with_original_tolerance":
                    bool(float(absolute[at]) <= cap+direct_tolerance),
                "original_row_tolerance": row_tolerance,
                "original_direct_tolerance": direct_tolerance,
                "only_curvature_prediction_and_not_actual14": True}
            results[label] = {
                "position_two_jets_without_X": jets, "arrays": arrays,
                "identity": identity, "binding_sha256": digest(identity), "summary": summary}
            sink["completed_grids"][label] = {
                "identity": copy.deepcopy(identity), "binding_sha256": digest(identity),
                "summary": copy.deepcopy(summary)}
            sink["_arrays"].setdefault("completed_curvature_predictions", {})[label] = {
                "position_two_jets_without_X": jets, "arrays": arrays}
            curvature_event["completed_output_bindings"] = {
                key: array_binding(value) for key, value in arrays.items()}
            principal_event["principal_curvatures"] = array_binding(principal)
            # The complete result already keeps the only needed ordinary-like
            # position derivatives; duplicated evaluator views need not remain.
            sink["_arrays"]["returned_curvature_values"].pop(label, None)
            sink["_arrays"]["periodic_primitives"].pop(label, None)
            _wall(wall, "curvature-predictor."+label+".complete")
        identity = {
            "schema": POLICY+"-complete-pair",
            "source": source,
            "grid_binding_sha256": {label: results[label]["binding_sha256"] for label in LABELS},
            "only_new_curvature_predictor_work_not_old_ordinary_replay": True}
        diagnostics = {
            "counts": copy.deepcopy(trace.counts),
            "events": copy.deepcopy(trace.events),
            "total_seconds_before_return": float(time.monotonic()-started),
            "maximum_two_grid_absolute_curvature": max(
                results[label]["summary"]["maximum_absolute_principal_curvature"] for label in LABELS),
            "ordinary_geometry_calls": 0, "center_or_fixed_primitive_calls": 0,
            "parameter_Jacobian_calls": 0, "optimization_solver_calls": 0,
            "actual_fourteen_gate_calls": 0,
            "future_caller_owns_all_value_predictor_cost_and_output": True}
        sink.update(status="complete", result_binding_sha256=digest(identity),
                    diagnostics=copy.deepcopy(diagnostics))
        _wall(wall, "curvature-predictor.complete")
        return {
            "grids": results, "binding": identity, "binding_sha256": digest(identity),
            "diagnostics": diagnostics}
    except Exception as error:
        sink.update(status="raised", error=_error(error),
                    counts=copy.deepcopy(trace.counts),
                    elapsed_seconds_before_raise=float(time.monotonic()-started))
        raise

#!/usr/bin/env python3
"""R510/R511 current-point ring17 curvature problem; import-only.

No CLI, automatic calculation, old solver instance, ordinary geometry,
development check, repeated LP or actual acceptance is installed.  The caller
owns a new pre-import scientific clock, all component charges and one new LP.

The exact real/rational R2 embedding is distinct from its binary64 candidate.
The numerical shape retains actual G=dot(T,T), including its floating error.
Any candidate still needs full nonlinear prediction and original actual gates.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import math
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import periodic_operator
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_complete_body_extension168 import (
    CompleteBody168Field, array_binding, _validate_grid)
from frame_complete_body_extension168_joint_selected import (
    _context, _validate_first_jets, bind_current_168_first_jets)
from frame_complete_body_extension168_curvature_prediction import (
    bind_current_168_curvature_metric, predict_current_168_curvature,
    POLICY as CURVATURE_POLICY)
from frame_curvature_psd import curvature_values


POLICY = "same-fixed-g-current168-ring17-finite-curvature-v1"
LABELS = ("coarse", "fine")
JETS = ("Xs", "Xt", "Xss", "Xst", "Xtt")
PARAMETERS = 17
VARIABLES = 18
TARGET_EXACT = "1000/61"
REFERENCE_SMALL_H_EXACT = "1/128"
# This is a new floating LP residual diagnostic, not any actual gate.
LP_ROW_TOLERANCE = 1.e-9


def definition():
    return {
        "schema": POLICY,
        "source_point_is_selected_by_caller_not_hardcoded_57_or_58": True,
        "full_field_columns": 168, "physical_columns": 172,
        "ring_control_columns": 17, "LP_columns": 18,
        "variable_order": "original u9, original v8, h",
        "radial_free_full_spline_indices": [9, 10, 11],
        "exact_R2_jets_at_selected_sigma": ["0", "0", "1"],
        "whole_original_three_spline_extension_not_a_truncated_last_piece": True,
        "angular_columns": "original u9/v8 in their published order; Q not changed",
        "new9_and_null_height_increments": "exactly zero, current nonzero values retained",
        "math_ring_shape": "S=S0+sum(ell_j*xi_j)*diag(1,0)",
        "numerical_shape": "actual-G Gram-Schmidt; never substitute G=1",
        "objective": "min h",
        "normalization": "h >= 4*||exact original physical172 increment||infinity",
        "maximum_h": "caller exact value, or a sufficient bound derived from the original box",
        "original_small_h": "1/128 is comparison-only unless explicitly requested as maximum_h_exact",
        "target_exact_default": TARGET_EXACT,
        "source_curvature": "complete paid ring twojets or one published curvature-predictor pair",
        "missing_twojets_are_never_zero_filled": True,
        "fixed_column_test": "sqrt(B^2+C^2) at both complete original angular grids",
        "LP_backend": "one new scipy.optimize.linprog(method='highs') call",
        "closed_ancestor_LP_and_cone_instances_are_not_called": True,
        "infeasibility_status_is_not_a_continuous_or_exact_mathematical_certificate": True,
        "timeout_or_failure_is_no_decision_and_never_restarted": True,
        "LP_row_tolerance": LP_ROW_TOLERANCE,
        "returned_candidate":
            "one final rounding of exact(binary64 base)+exact R2 embedding of binary64 xi",
        "rounded_candidate_not_claimed_exactly_metric_neutral": True,
        "ordinary_geometry_calls_inside_module": 0,
        "hard_or_selected_parameter_J_calls_inside_module": 0,
        "actual_fourteen_gate_calls_inside_module": 0,
        "all_new_frames_Pi_curvature_exact_basis_work_solver_output_and_failures_are_charged": True}


def implementation_hashes():
    names = (
        Path(__file__).name,
        "frame_complete_body_extension168.py",
        "frame_complete_body_extension168_joint_selected.py",
        "frame_complete_body_extension168_curvature_prediction.py",
        "frame_collar_bvp.py", "frame_collar_enriched.py",
        "frame_entry_single_q.py", "frame_entry_paired_repair.py",
        "frame_five_height_field.py",
        "frame_curvature_psd.py", "frame_height_null_coordinates.py")
    root = Path(__file__).parent
    return {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
            for name in names}


def _require(value, message):
    if not bool(value):
        raise ValueError(message)


def _error(error):
    return {"type": type(error).__name__, "message": str(error)}


def _wall(wall, stage):
    _require(callable(wall), "an external new-task scientific-clock callback is required")
    return wall(stage)


def _array(value, shape, name, *, own=True):
    a = np.asarray(value, dtype=np.float64)
    _require(a.shape == tuple(shape) and np.all(np.isfinite(a)),
             "finite literal shape required: "+name)
    a = a.copy() if own else a.view()
    a.setflags(write=False)
    return a


def _same(left, right):
    a, b = np.asarray(left), np.asarray(right)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def _q(value):
    _require(not isinstance(value, (bool, np.bool_)), "boolean is not a physical rational")
    if isinstance(value, Q):
        return value
    if isinstance(value, (float, np.floating)):
        _require(math.isfinite(float(value)), "finite physical bound required")
        return Q.from_float(float(value))
    if isinstance(value, (int, np.integer)):
        return Q(int(value))
    if isinstance(value, str):
        return Q(value)
    raise ValueError("literal rational string, integer or finite binary64 required")


def _vector(value):
    a = np.asarray(value, dtype=np.float64)
    _require(a.ndim == 1 and np.all(np.isfinite(a)), "finite vector required")
    return {**array_binding(a), "values": a.tolist(),
            "exact_binary64": [str(Q.from_float(float(x))) for x in a]}


def _payload(value):
    a = np.asarray(value)
    _require(np.all(np.isfinite(a)), "finite original scientific payload required")
    return {**array_binding(a), "values": a.tolist()}


def _public(value):
    return {key: copy.deepcopy(item) for key, item in value.items() if key != "_arrays"}


def _bounds(value, name):
    _require(len(value) == 172, "all 172 "+name+" values are required")
    return tuple(_q(item) for item in value)


class _Trace:
    def __init__(self, wall, capture):
        self.wall, self.capture = wall, capture
        self.events = capture.setdefault("events", [])
        self.counts = capture.setdefault("component_counts", {})

    def run(self, kind, operation, retain, **metadata):
        counter = self.counts.setdefault(kind, {"started": 0, "entered": 0,
                                               "completed": 0, "failed": 0})
        counter["started"] += 1
        event = {"kind": kind, "ordinal": counter["started"], "status": "started",
                 "work_call_entered": False, **copy.deepcopy(metadata)}
        self.events.append(event)
        tick = time.monotonic()
        try:
            _wall(self.wall, "ring17."+kind)
            event["work_call_entered"] = True
            counter["entered"] += 1
            answer = operation()
            retain(answer)
            counter["completed"] += 1
            event.update(status="complete", seconds=float(time.monotonic()-tick))
            _wall(self.wall, "ring17."+kind+".complete")
            return answer, event
        except Exception as error:
            if event["status"] == "started":
                counter["failed"] += 1
                event.update(status="raised", error=_error(error),
                             seconds=float(time.monotonic()-tick))
            else:
                event.update(post_completion_error=_error(error),
                             completed_work_retained_but_return_blocked=True)
            raise


def _grid_context(field, state168, radial, thetas, ring_index):
    _context(field)
    q = _array(field.validate_state(state168), (168,), "current168")
    _require(isinstance(thetas, dict) and set(thetas) == set(LABELS),
             "both complete original angular grids are required")
    r = None
    th = {}
    for label in LABELS:
        rr, tt = _validate_grid(radial, thetas[label])
        rr = _array(rr, rr.shape, "radial")
        if r is None:
            r = rr
        else:
            _require(_same(r, rr), "both grids must retain one original radial vector")
        th[label] = _array(tt, tt.shape, label+"/theta")
    _require(len(th["fine"]) == 2*len(th["coarse"]),
             "original doubled fine angular grid required")
    _require(type(ring_index) is int and 0 < ring_index < len(r)-1,
             "one literal interior original radial index required")
    return q, r, th


def _ring_source_identity(field, q, r, th, ring_index):
    return {
        "field_definition_sha256": field.definition_sha256,
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "physical_state_sha256": digest(field.identity(q)),
        "state168": array_binding(q), "radial": array_binding(r),
        "ring_radial_index": ring_index,
        "sigma_binary64_exact": str(Q.from_float(float(r[ring_index]))),
        "theta": {label: array_binding(th[label]) for label in LABELS}}


def bind_paid_ring_twojets(
        field, state168, radial, thetas, ring_index, positions_by_grid,
        point_ids_by_grid, source_receipt):
    """Bind already paid complete-circle positions; no geometry is evaluated.

    The external producer must select each source point in literal theta order.
    A partial selected pool is not accepted as a complete ring.  This function
    binds supplied values/provenance; it does not retroactively prove their cost.
    """
    q, r, th = _grid_context(field, state168, radial, thetas, ring_index)
    _require(isinstance(source_receipt, dict) and bool(source_receipt),
             "the actual paid source of the original ring twojets is required")
    _require(set(positions_by_grid) == set(LABELS)
             and set(point_ids_by_grid) == set(LABELS),
             "both complete rings and their actual selected point IDs are required")
    arrays, ids = {}, {}
    for label in LABELS:
        nt = len(th[label])
        raw = np.asarray(point_ids_by_grid[label])
        _require(raw.dtype.kind in "iu" and raw.shape == (nt,),
                 "integer complete-ring source point IDs required")
        expected = ring_index*nt+np.arange(nt, dtype=np.int64)
        _require(np.array_equal(raw, expected),
                 "the selected twojets do not cover the complete circle in source order")
        ids[label] = np.asarray(raw, dtype=np.int64).copy()
        ids[label].setflags(write=False)
        arrays[label] = {
            name: _array(positions_by_grid[label].get(name), (nt, 3),
                         label+"/paid-"+name, own=False)
            for name in JETS}
    identity = {
        "schema": POLICY+"-paid-ring-twojet-identity",
        "source": _ring_source_identity(field, q, r, th, ring_index),
        "point_ids": {label: array_binding(ids[label]) for label in LABELS},
        "position_arrays": {
            label: {name: array_binding(value) for name, value in arrays[label].items()}
            for label in LABELS},
        "source_receipt": copy.deepcopy(source_receipt),
        "all_complete_ring_points_supplied_no_fullgrid_zero_surrogate": True}
    return {
        "schema": POLICY+"-paid-ring-twojets", "state168": q, "radial": r,
        "thetas": th, "ring_index": ring_index, "point_ids": ids,
        "data": arrays, "identity": identity, "binding_sha256": digest(identity),
        "ordinary_and_parameter_J_calls": 0}


def _validated_paid_ring(field, q, r, th, ring_index, bound):
    _require(isinstance(bound, dict) and bound.get("schema") == POLICY+"-paid-ring-twojets",
             "an explicit paid complete-ring twojet binding is required")
    rebuilt = bind_paid_ring_twojets(
        field, q, r, th, ring_index, bound["data"], bound["point_ids"],
        bound["identity"]["source_receipt"])
    _require(bound["binding_sha256"] == digest(bound["identity"])
             and rebuilt["identity"] == bound["identity"],
             "paid ring state/grid/positions or source binding changed")
    return bound["data"]


def _exact_R2(single, sigma):
    """Exact 3-by-3 basis-jet elimination; new mathematical build work."""
    knots = tuple(Q(value) for value in single.radial_knots)
    _require(len(knots) == 21 and all(a <= b for a, b in zip(knots, knots[1:]))
             and knots[:6] == (knots[0],)*6 and knots[-6:] == (knots[-1],)*6,
             "the published nine-free-column clamped quintic knot list is required")
    _require(knots[0] == Q("9/250") and knots[-1] == Q("423/500")
             and knots[-7] == Q("153/200"),
             "the original last span is a mathematical identity, not a fitted knot")
    entry_end = Q(single.entry.left_exact)+Q(single.entry.length_exact)
    _require(entry_end <= knots[9],
             "all three original spline supports must lie beyond the entry weights")
    _require(knots[-7] < sigma < knots[-1],
             "the R2 ring must lie strictly in the original final knot span")

    @lru_cache(None)
    def basis(i, degree, derivative):
        if derivative < 0 or derivative > degree:
            return Q(0)
        if degree == 0:
            return Q(int(derivative == 0 and knots[i] <= sigma < knots[i+1]))
        left = knots[i+degree]-knots[i]
        right = knots[i+degree+1]-knots[i+1]
        if derivative:
            return ((Q(degree)/left*basis(i, degree-1, derivative-1) if left else Q(0))
                    -(Q(degree)/right*basis(i+1, degree-1, derivative-1) if right else Q(0)))
        return (((sigma-knots[i])/left*basis(i, degree-1, 0) if left else Q(0))
                +((knots[i+degree+1]-sigma)/right*basis(i+1, degree-1, 0) if right else Q(0)))

    columns = (9, 10, 11)
    matrix = [[basis(i, 5, derivative) for i in columns] for derivative in range(3)]
    work = [row+[Q(int(j == 2))] for j, row in enumerate(matrix)]
    operations = []
    for col in range(3):
        pivot = next((j for j in range(col, 3) if work[j][col]), None)
        _require(pivot is not None, "original exact three-jet matrix is singular")
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            operations.append({"swap": [col, pivot]})
        scale = work[col][col]
        work[col] = [value/scale for value in work[col]]
        operations.append({"normalize_row": col, "pivot_exact": str(scale)})
        for j in range(3):
            if j != col and work[j][col]:
                factor = work[j][col]
                work[j] = [a-factor*b for a, b in zip(work[j], work[col])]
                operations.append({"eliminate_row": j, "using": col,
                                   "factor_exact": str(factor)})
    weights = tuple(work[j][-1] for j in range(3))
    jets = tuple(sum(matrix[j][i]*weights[i] for i in range(3)) for j in range(3))
    _require(jets == (Q(0), Q(0), Q(1)), "exact original R2 embedding failed")
    return {
        "knots_exact": [str(value) for value in knots],
        "entry_weight_end_exact": str(entry_end),
        "entry_u_and_v_weights_are_one_on_all_three_supports": True,
        "full_spline_indices": list(columns), "free_radial_indices": [6, 7, 8],
        "sigma_exact": str(sigma),
        "basis_jet_matrix_exact": [[str(value) for value in row] for row in matrix],
        "weights_exact": [str(value) for value in weights],
        "resulting_radial_jets_exact": [str(value) for value in jets],
        "exact_elimination_operations": operations,
        "global_extension": "same original B9/B10/B11 on their whole support",
        "not_truncated_at_last_span_left": True,
        "binary64_evaluation_is_not_claimed_exactly_zero": True}, weights


def _embedding(weights):
    entries = []
    E = np.zeros((168, PARAMETERS), dtype=np.float64)
    for offset, modes, start in ((0, 9, 0), (9, 8, 81)):
        for j in range(modes):
            for local, weight in enumerate(weights):
                independent = start+(6+local)*modes+j
                E[independent, offset+j] = float(weight)
                entries.append({
                    "parameter_column": offset+j,
                    "independent168_row": independent,
                    "physical172_row": independent,
                    "full_spline_index": 9+local,
                    "weight_exact": str(weight), "weight_binary64": float(weight)})
    E.setflags(write=False)
    P = np.zeros((172, PARAMETERS), dtype=np.float64)
    P[:154] = E[:154]
    P.setflags(write=False)
    return E, P, entries


def _normal_shape(jets, actual_I, actual_II, original_q, a):
    """Actual-G orthonormalization, preserving the R2 changing first slot."""
    U = np.asarray(jets["Xs"], dtype=np.float64)
    T = np.asarray(jets["Xt"], dtype=np.float64)/float(a)
    I, II = np.asarray(actual_I), np.asarray(actual_II)
    E, F, G = I[:, 0, 0], I[:, 0, 1], I[:, 1, 1]
    _require(np.all(G > 0), "actual G must remain positive")
    eta = F/G
    q_perp2 = E-F*eta
    _require(np.all(q_perp2 > 0) and np.all(np.isfinite(q_perp2)),
             "the actual tangent Gram-Schmidt denominator must be positive")
    n = np.cross(U, T)/np.asarray(original_q)[:, None]
    _require(np.all(np.isfinite(n)), "finite original actual normal required")
    A = (II[:, 0, 0]-2*eta*II[:, 0, 1]+eta*eta*II[:, 1, 1])/q_perp2
    B = (II[:, 0, 1]-eta*II[:, 1, 1])/np.sqrt(q_perp2*G)
    C = II[:, 1, 1]/G
    for value in (A, B, C):
        _require(np.all(np.isfinite(value)), "finite actual-G shape components required")
    return {
        "A": A, "B": B, "C": C, "normal": n, "actual_I": I, "actual_II": II,
        "actual_G": G, "q_perp_squared": q_perp2,
        "actual_normal_area": np.asarray(original_q),
        "G_minus_one": G-1.,
        "q_perp2_minus_original_cross_q2_over_G": q_perp2-np.asarray(original_q)**2/G}


def _operator_norm(A, B, C):
    return .5*(abs(A+C)+np.sqrt((A-C)**2+4*B*B))


def _validate_inputs_firstjets(field, q, r, th, firstjets, fixed_metric):
    _require(isinstance(firstjets, dict) and set(firstjets) == set(LABELS),
             "both actual current first-jet bindings are required")
    _require(isinstance(fixed_metric, dict)
             and fixed_metric.get("schema") == CURVATURE_POLICY+"-bound-fixed-metric",
             "bound actual fixed a/a_s/a_ss is required")
    rebuilt = bind_current_168_curvature_metric(
        field, r, fixed_metric["data"], fixed_metric["identity"]["source_receipt"])
    _require(fixed_metric.get("binding_sha256") == digest(fixed_metric["identity"])
             and rebuilt["identity"] == fixed_metric["identity"],
             "fixed metric source/grid/arrays changed")
    metric, paid = fixed_metric["data"], {}
    for label in LABELS:
        _, _, _, data = _validate_first_jets(field, q, r, th[label], firstjets[label])
        for key in ("U", "T", "e", "f"):
            _require(array_binding(data[key]) == firstjets[label]["identity"]["arrays"][key],
                     "paid first-jet array changed after its binding: "+label+"/"+key)
        for key in ("a", "a_s"):
            _require(_same(data["metric"][key], metric[key])
                     and array_binding(data["metric"][key])
                     == firstjets[label]["identity"]["metric_arrays"][key],
                     "fixed metric and paid first-jet metric disagree")
        paid[label] = data
    return paid, metric


def _acquire_ring_curvature(
        field, q, r, th, ring_index, firstjets, paid, metric, fixed_metric,
        cfg, source, paid_ring_geometry, trace, sink):
    """Only array curvature evaluation or the declared new predictor route."""
    area_floor = float(cfg["normal_area_numerical_floor"])
    cap = float(Q(cfg["fixed_hard_curvature_cap_exact"]))
    _require(math.isfinite(area_floor) and area_floor >= 0
             and math.isfinite(cap) and cap > 0,
             "original curvature configuration is required")
    answer = {}
    if paid_ring_geometry is not None:
        data = _validated_paid_ring(field, q, r, th, ring_index, paid_ring_geometry)
        sink["curvature_input_route"] = {
            "kind": "already-paid-complete-ring-twojets",
            "binding_sha256": paid_ring_geometry["binding_sha256"],
            "source_identity": copy.deepcopy(paid_ring_geometry["identity"]),
            "new_ordinary_calls": 0,
            "new_original_array_curvature_evaluations": 2}
        for label in LABELS:
            jets = data[label]
            aa = float(metric["a"][ring_index])
            _require(_same(jets["Xs"], paid[label]["U"][ring_index])
                     and _same(jets["Xt"], aa*paid[label]["T"][ring_index]),
                     "paid complete ring twojets and paid first jets do not agree")
            def retain(value, label=label):
                sink["_arrays"].setdefault("paid_ring_array_curvature", {})[label] = value
            values, event = trace.run(
                "original_ring_curvature_array_evaluation",
                lambda jets=jets, aa=aa: curvature_values(
                    jets, aa, 1/cap, area_floor=area_floor),
                retain, grid=label,
                original_twojet_binding_sha256=paid_ring_geometry["binding_sha256"])
            answer[label] = {
                "jets": jets, "actual_I": values["actual_I"],
                "actual_II": values["actual_II"], "q": values["q"],
                "input_source": {"kind": "original-paid-complete-ring-twojets",
                                 "binding_sha256": paid_ring_geometry["binding_sha256"]}}
            event["actual_I"] = array_binding(values["actual_I"])
            event["actual_II"] = array_binding(values["actual_II"])
        return answer

    # The published predictor requires an anchored increasing radial grid.
    # Retain real first/last rows as anchors; no fake zero or omitted circle.
    take = np.array([0, ring_index, len(r)-1], dtype=np.int64)
    sub_r = r[take].copy()
    sub_first = {}
    sub_metric = {key: metric[key][take].copy() for key in ("a", "a_s", "a_ss")}
    sub_source = {
        "schema": POLICY+"-ring-predictor-subgrid",
        "source": copy.deepcopy(source),
        "original_radial_indices": take.tolist(),
        "original_radial": array_binding(r), "selected_radial": array_binding(sub_r),
        "whole_original_theta_retained": True,
        "all_three_radial_rows_are_real_paid_inputs": True,
        "new_predictor_computes_all_three_rows_and_charges_them": True}
    for label in LABELS:
        selected = {
            "U": paid[label]["U"][take].copy(),
            "T": paid[label]["T"][take].copy(),
            "e": paid[label]["e"][take].copy(),
            "f": paid[label]["f"][take].copy(),
            "metric": {key: sub_metric[key] for key in ("a", "a_s")}}
        def retain(value, label=label):
            sink["_arrays"].setdefault("subgrid_firstjet_bindings", {})[label] = value
        bound, _ = trace.run(
            "firstjet_subgrid_binding",
            lambda label=label, selected=selected: bind_current_168_first_jets(
                field, q, sub_r, th[label], selected,
                {**sub_source, "grid": label,
                 "parent_firstjet_binding_sha256": firstjets[label]["binding_sha256"]}),
            retain, grid=label, ordinary_calls=0, parameter_J_calls=0)
        sub_first[label] = bound
    bound_metric = bind_current_168_curvature_metric(field, sub_r, sub_metric, sub_source)
    partial = {}
    sink["_arrays"]["curvature_predictor_partial"] = partial
    def retain_prediction(value):
        sink["_arrays"]["curvature_predictor_returned"] = value
    prediction, event = trace.run(
        "new_curvature_predictor_pair",
        lambda: predict_current_168_curvature(
            field, q, sub_r, th, sub_first, bound_metric, cfg,
            source_receipt=sub_source, wall=trace.wall, capture=partial),
        retain_prediction, radial_count=3,
        original_radial_indices=take.tolist(), ordinary_calls=0, parameter_J_calls=0)
    sink["curvature_input_route"] = {
        "kind": "published-current-curvature-predictor-on-actual-three-row-subgrid",
        "prediction_binding_sha256": prediction["binding_sha256"],
        "source": sub_source, "diagnostics": copy.deepcopy(prediction["diagnostics"]),
        "current_height_and_whole_theta_primitives_are_actual_new_work": True,
        "not_bitwise_ordinary_or_original_actual14": True}
    event["nested_diagnostics"] = copy.deepcopy(prediction["diagnostics"])
    for label in LABELS:
        grid = prediction["grids"][label]
        answer[label] = {
            "jets": {name: grid["position_two_jets_without_X"][name][1]
                     for name in JETS},
            "actual_I": grid["arrays"]["actual_I"][1],
            "actual_II": grid["arrays"]["actual_II"][1],
            "q": grid["arrays"]["normal_area"][1],
            "input_source": {
                "kind": "new-curvature-predictor",
                "binding_sha256": grid["binding_sha256"],
                "selected_subgrid_radial_index": 1,
                "original_radial_index": ring_index}}
    return answer


def _ring_ell(field, q, sigma, theta, shape, aa, weights, label, trace, sink):
    query = np.array([sigma], dtype=np.float64)
    def retain_frame(value):
        grid, fields, frame = value
        sink["_arrays"].setdefault("ring_frames", {})[label] = {
            "grid": grid, "fields": fields, "frame": frame}
    result, event = trace.run(
        "current_ring_scalar_frame",
        lambda: field.scalar_frame(q, query, theta), retain_frame,
        grid=label, state168=array_binding(q), radial=array_binding(query))
    grid, fields, frame = result
    nt = len(theta)
    Tu = _array(frame["Tpart"]["u"], (1, nt, 3), label+"/Tu", own=False)
    Tv = _array(frame["Tpart"]["v"], (1, nt, 3), label+"/Tv", own=False)
    angular_u = _array(grid.original_grid.angular["u"], (nt, 9),
                       label+"/original-u9", own=False)
    angular_v = _array(grid.original_grid.angular["v"], (nt, 8),
                       label+"/original-v8", own=False)
    # R2''=1, R2=R2'=0 in the exact embedding: no second-order
    # frame-partial terms remain, and every full-angle Pi is retained.
    changed_Tss = np.concatenate((
        Tu[..., None]*angular_u[None, :, None, :],
        Tv[..., None]*angular_v[None, :, None, :]), axis=-1)
    _require(changed_Tss.shape == (1, nt, 3, PARAMETERS)
             and np.all(np.isfinite(changed_Tss)),
             "complete seventeen original angular Tss columns are required")
    sink["_arrays"].setdefault("ring_Tss_columns", {})[label] = changed_Tss
    def retain_pi(value):
        sink["_arrays"].setdefault("ring_Tss_primitives", {})[label] = value
    primitive, pi_event = trace.run(
        "whole_circle_seventeen_column_primitive",
        lambda: periodic_operator(changed_Tss, -1), retain_pi,
        grid=label, order=-1, source_array=array_binding(changed_Tss))
    primitive = _array(primitive, changed_Tss.shape, label+"/Pi-Tss", own=False)
    ell = aa*np.einsum("tc,tck->tk", shape["normal"], primitive[0])
    ell /= shape["q_perp_squared"][:, None]
    ell = _array(ell, (nt, PARAMETERS), label+"/ell")
    actual_basis = []
    for order in range(3):
        basis = np.asarray(grid.original_grid.bases[order], dtype=np.float64)
        _require(basis.shape == (1, 9), "original nine radial spline columns required")
        actual_basis.append(float(basis[0, 6:9] @ np.array(list(map(float, weights)))))
    identity = {
        "schema": POLICY+"-current-seventeen-ring-columns", "grid": label,
        "field_definition_sha256": field.definition_sha256,
        "state168": array_binding(q), "radial": array_binding(query),
        "theta": array_binding(theta),
        "scalar_arrays": {
            name+"/"+jet: array_binding(np.asarray(fields[name][jet], dtype=np.float64))
            for name in ("u", "v") for jet in ("value", "s", "ss", "theta")},
        "frame_partials": {"Tu": array_binding(Tu), "Tv": array_binding(Tv)},
        "original_angular_columns": {
            "u9": array_binding(angular_u), "v8": array_binding(angular_v)},
        "Tss_columns": array_binding(changed_Tss),
        "whole_periodic_primitive": array_binding(primitive),
        "ell": array_binding(ell),
        "ell_formula": "a*normal dot Pi(Tu*u9,Tv*v8)/(E-F^2/G)",
        "actual_G_retained": True,
        "binary64_R2_jets_diagnostic": actual_basis,
        "binary64_R2_jets_are_not_an_exact_neutrality_claim": True}
    event["current_frame_identity"] = copy.deepcopy(identity)
    pi_event["output_array"] = array_binding(primitive)
    return ell, identity


def build_ring17_model(
        field, state168, radial, thetas, paid_firstjets, fixed_metric, cfg,
        lower172, upper172, *, source_receipt, ring_index,
        target_exact=TARGET_EXACT, maximum_h_exact=None, wall, capture=None,
        paid_ring_geometry=None):
    """Build one new ring problem.  This function grants no resource budget.

    source_receipt must name the current accepted point (currently 58 in the
    intended caller) and all original U/T/grid/metric provenance.  There is
    no old-point fallback.  Maximum h is caller-specified or box-derived,
    never silently inherited from the old small-domain optimization.
    """
    started = time.monotonic()
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty ring-build capture required")
    sink.update(schema=POLICY+"-build-capture", status="started", events=[],
                component_counts={}, _arrays={})
    trace = _Trace(wall, sink)
    try:
        _wall(wall, "ring17.build.entry")
        q, r, th = _grid_context(field, state168, radial, thetas, ring_index)
        _require(isinstance(source_receipt, dict) and bool(source_receipt)
                 and isinstance(cfg, dict), "current source receipt and original cfg required")
        old, single = _context(field)
        target = _q(target_exact)
        _require(target > 0, "positive exact curvature target required")
        low, high = _bounds(lower172, "lower bounds"), _bounds(upper172, "upper bounds")
        _require(all(a <= b for a, b in zip(low, high)), "ordered original physical172 box required")
        # The original actual field compares to exact binary64 box endpoints.
        # Do not silently replace an externally exact bound by its rounding.
        _require(all(Q.from_float(float(v)) == v for v in low+high),
                 "original actual physical172 bounds must have exact binary64 endpoints")
        physical = tuple(field.full_coefficients(q, exact=True))
        _require(all(lo <= value <= hi for lo, value, hi in zip(low, physical, high)),
                 "the supplied current point is outside its original exact172 box")
        paid, metric = _validate_inputs_firstjets(
            field, q, r, th, paid_firstjets, fixed_metric)
        sigma = Q.from_float(float(r[ring_index]))
        source = {
            "schema": POLICY+"-current-source",
            **_ring_source_identity(field, q, r, th, ring_index),
            "source_receipt": copy.deepcopy(source_receipt),
            "configuration_sha256": digest(cfg),
            "physical172_exact": [str(v) for v in physical],
            "lower172_exact": [str(v) for v in low],
            "upper172_exact": [str(v) for v in high],
            "fixed_metric_binding_sha256": fixed_metric["binding_sha256"],
            "firstjet_binding_sha256": {
                label: paid_firstjets[label]["binding_sha256"] for label in LABELS},
            "target_exact": str(target)}
        sink["source"] = copy.deepcopy(source)
        def retain_basis(value):
            sink["exact_radial_embedding"] = copy.deepcopy(value[0])
        radial_result, _ = trace.run(
            "exact_three_spline_jet_elimination",
            lambda: _exact_R2(single, sigma), retain_basis, sigma_exact=str(sigma))
        radial_definition, weights = radial_result
        E, P, entries = _embedding(weights)
        active = sorted({entry["physical172_row"] for entry in entries})
        derived_h = 4*max(max(abs(low[j]-physical[j]), abs(high[j]-physical[j]))
                         for j in active)
        hmax = derived_h if maximum_h_exact is None else _q(maximum_h_exact)
        _require(hmax >= 0 and math.isfinite(float(hmax)), "finite nonnegative h bound required")
        maximum = {
            "requested_maximum_h_exact": None if maximum_h_exact is None else str(hmax),
            "effective_maximum_h_exact": str(hmax),
            "box_sufficient_maximum_h_exact": str(derived_h),
            "source": "original172-box-derived" if maximum_h_exact is None else "explicit-caller-cap",
            "reference_small_h_exact": REFERENCE_SMALL_H_EXACT,
            "reference_small_h_is_not_an_implicit_constraint": maximum_h_exact is None,
            "active_physical_indices": active,
            "all_172_original_box_constraints_retained": True}
        sink["maximum_h"] = copy.deepcopy(maximum)
        ring_data = _acquire_ring_curvature(
            field, q, r, th, ring_index, paid_firstjets, paid, metric, fixed_metric,
            cfg, source, paid_ring_geometry, trace, sink)
        grids = {}
        for label in LABELS:
            data = ring_data[label]
            shape = _normal_shape(
                data["jets"], data["actual_I"], data["actual_II"], data["q"],
                metric["a"][ring_index])
            ell, ell_identity = _ring_ell(
                field, q, float(r[ring_index]), th[label], shape,
                float(metric["a"][ring_index]), weights, label, trace, sink)
            lower_bound = np.sqrt(shape["B"]**2+shape["C"]**2)
            current_norm = _operator_norm(shape["A"], shape["B"], shape["C"])
            at = int(np.argmax(lower_bound))
            grid = {
                **shape, "ell": ell, "theta": th[label],
                "position_two_jets_without_X": data["jets"],
                "invariant_column_lower_bound": lower_bound,
                "current_operator_norm": current_norm,
                "input_source": copy.deepcopy(data["input_source"]),
                "ell_identity": ell_identity,
                "summary": {
                    "maximum_invariant_column_lower_bound": float(lower_bound[at]),
                    "lower_bound_attainer": {"theta_index": at, "theta": float(th[label][at])},
                    "maximum_current_ring_operator_norm": float(np.max(current_norm)),
                    "maximum_absolute_G_minus_one": float(np.max(abs(shape["G_minus_one"]))),
                    "target_exact": str(target),
                    "floating_invariant_column_excludes_target":
                        bool(np.any(lower_bound > float(target))),
                    "finite_float_inputs_not_interval_certificate": True}}
            grids[label] = grid
            sink["_arrays"].setdefault("completed_ring_grids", {})[label] = grid
            sink.setdefault("completed_grids", {})[label] = copy.deepcopy(grid["summary"])
            _wall(wall, "ring17.build."+label+".complete")
        model = Ring17Model(
            field, q, r, th, ring_index, cfg, source, radial_definition, weights,
            E, P, entries, physical, low, high, target, hmax, maximum, grids, sink)
        sink.update(status="complete", model_binding_sha256=model.binding_sha256,
                    build_seconds_before_return=float(time.monotonic()-started))
        _wall(wall, "ring17.build.complete")
        return model
    except Exception as error:
        sink.update(status="raised", error=_error(error),
                    build_seconds_before_raise=float(time.monotonic()-started),
                    completed_work_not_retried=True)
        raise


class Ring17Model:
    """One same-current-state finite ring LP, never a full-body acceptance."""
    def __init__(self, field, q, radial, thetas, ring_index, cfg, source,
                 radial_definition, weights, E, P, entries, physical,
                 lower, upper, target, hmax, maximum, grids, capture):
        self.field, self.state168, self.radial, self.thetas = field, q, radial, thetas
        self.ring_index, self.cfg = ring_index, cfg
        self.source = copy.deepcopy(source)
        self.weights, self.E, self.P = tuple(weights), E, P
        self.embedding_entries = copy.deepcopy(entries)
        self.radial_definition = copy.deepcopy(radial_definition)
        self.base_physical172 = tuple(physical)
        self.lower172, self.upper172 = tuple(lower), tuple(upper)
        self.target_exact, self.maximum_h_exact = target, hmax
        self.maximum_h = copy.deepcopy(maximum)
        self.grids = grids
        self.build_capture = capture
        self.solve_attempted = False
        self.solve_record = None
        self._assembled = None
        self.binding = {
            "schema": POLICY+"-model-binding", "source": self.source,
            "definition": definition(), "source_hashes": implementation_hashes(),
            "exact_radial_embedding": self.radial_definition,
            "embedding_entries": self.embedding_entries,
            "binary64_embedding168": array_binding(E),
            "binary64_physical_embedding172": array_binding(P),
            "maximum_h": self.maximum_h,
            "grid_arrays": {
                label: {name: array_binding(grids[label][name])
                        for name in ("A", "B", "C", "ell", "normal", "actual_I",
                                     "actual_II", "actual_G", "q_perp_squared",
                                     "actual_normal_area", "invariant_column_lower_bound")}
                for label in LABELS},
            "grid_position_arrays": {
                label: {name: array_binding(value) for name, value in
                        grids[label]["position_two_jets_without_X"].items()}
                for label in LABELS},
            "curvature_input_route": copy.deepcopy(capture["curvature_input_route"]),
            "grid_ell_binding_sha256": {
                label: digest(grids[label]["ell_identity"]) for label in LABELS}}
        self.binding_sha256 = digest(self.binding)

    def assert_context(self):
        self.field._assert_context()
        _require(digest(self.cfg) == self.source["configuration_sha256"]
                 and digest(self.field.identity(self.state168))
                 == self.source["physical_state_sha256"]
                 and array_binding(self.state168) == self.source["state168"],
                 "current field/state/physical configuration changed")
        _require(digest(self.binding) == self.binding_sha256
                 and array_binding(self.radial) == self.source["radial"]
                 and all(array_binding(self.thetas[label]) == self.source["theta"][label]
                         for label in LABELS),
                 "ring model or original grid identity changed")
        for label in LABELS:
            for name, expected in self.binding["grid_arrays"][label].items():
                _require(array_binding(self.grids[label][name]) == expected,
                         "current ring model array changed: "+label+"/"+name)
            for name, expected in self.binding["grid_position_arrays"][label].items():
                _require(array_binding(self.grids[label]["position_two_jets_without_X"][name])
                         == expected, "current ring twojet changed: "+label+"/"+name)
        _require(array_binding(self.E) == self.binding["binary64_embedding168"]
                 and array_binding(self.P) == self.binding["binary64_physical_embedding172"],
                 "physical ring embedding changed")

    def summary(self):
        return {
            "schema": POLICY+"-model-summary", "model_binding_sha256": self.binding_sha256,
            "source": copy.deepcopy(self.source), "target_exact": str(self.target_exact),
            "maximum_h": copy.deepcopy(self.maximum_h),
            "grids": {label: copy.deepcopy(self.grids[label]["summary"]) for label in LABELS},
            "floating_invariant_column_obstruction": any(
                self.grids[label]["summary"]["floating_invariant_column_excludes_target"]
                for label in LABELS),
            "obstruction_is_not_a_continuous_or_interval_certificate": True,
            "finite_LP_attempted": bool(self.solve_attempted),
            "actual_body_geometry_or_actual14_calls": 0}

    def assemble(self):
        """Four trace/determinant rows at every angle, plus the true box/norm.

        Trace plus determinant retains |C|=K without division.  These are
        affine rows because only the (1,1) shape entry varies.  All quantities
        here are floating model coefficients, not an exact LP certificate.
        """
        self.assert_context()
        if self._assembled is not None:
            return self._assembled
        rows, rhs, tags = [], [], []
        def add(row, bound, tag):
            row = np.asarray(row, dtype=np.float64)
            _require(row.shape == (VARIABLES,) and np.all(np.isfinite(row))
                     and math.isfinite(float(bound)), "finite original-unit LP row required")
            rows.append(row.copy())
            rhs.append(float(bound))
            tags.append(tag)
        K = float(self.target_exact)
        for label in LABELS:
            grid = self.grids[label]
            for j, theta in enumerate(grid["theta"]):
                A, B, C, ell = (grid[name][j] for name in ("A", "B", "C", "ell"))
                for name, coeff, bound in (
                    ("plus_trace", -ell, 2*K+A+C),
                    ("plus_determinant", -(K+C)*ell, (K+C)*(K+A)-B*B),
                    ("minus_trace", ell, 2*K-A-C),
                    ("minus_determinant", (K-C)*ell, (K-C)*(K-A)-B*B)):
                    add(np.r_[coeff, 0.], bound, {
                        "kind": "ring_PSD", "grid": label, "theta_index": j,
                        "theta": float(theta), "component": name})
        for j in range(172):
            p = self.P[j]
            add(np.r_[p, 0.], float(self.upper172[j]-self.base_physical172[j]),
                {"kind": "physical172_box", "physical_index": j, "side": "upper"})
            add(np.r_[-p, 0.], float(self.base_physical172[j]-self.lower172[j]),
                {"kind": "physical172_box", "physical_index": j, "side": "lower"})
            if np.any(p != 0.):
                add(np.r_[4*p, -1.], 0.,
                    {"kind": "physical_step_norm", "physical_index": j, "side": "plus"})
                add(np.r_[-4*p, -1.], 0.,
                    {"kind": "physical_step_norm", "physical_index": j, "side": "minus"})
        add(np.r_[np.zeros(PARAMETERS), -1.], 0., {"kind": "h_lower"})
        add(np.r_[np.zeros(PARAMETERS), 1.], float(self.maximum_h_exact),
            {"kind": "h_upper"})
        A, b = np.stack(rows), np.asarray(rhs, dtype=np.float64)
        c = np.r_[np.zeros(PARAMETERS), 1.]
        for array in (A, b, c):
            array.setflags(write=False)
        metadata = {
            "rows": len(b), "columns": VARIABLES, "A": array_binding(A),
            "b": array_binding(b), "c": array_binding(c),
            "row_tags_sha256": digest(tags),
            "row_counts": {kind: sum(tag["kind"] == kind for tag in tags)
                           for kind in sorted({tag["kind"] for tag in tags})},
            "all_variables_explicitly_free_before_declared_rows": True,
            "PSD_rows_keep_boundary_cases_without_dividing_by_K_plus_or_minus_C": True}
        self._assembled = (A, b, c, tags, metadata)
        return self._assembled

    def full_record(self):
        """One original stdout record; no duplicated dense LP A is necessary."""
        self.assert_context()
        return {
            "schema": POLICY+"-full-ring-model", "binding": copy.deepcopy(self.binding),
            "binding_sha256": self.binding_sha256, "summary": self.summary(),
            "state168": _vector(self.state168),
            "physical172_exact": [str(value) for value in self.base_physical172],
            "exact_radial_embedding": copy.deepcopy(self.radial_definition),
            "exact_embedding_entries": copy.deepcopy(self.embedding_entries),
            "grids": {
                label: {
                    "arrays": {name: _payload(self.grids[label][name])
                               for name in ("A", "B", "C", "ell", "normal", "actual_I",
                                            "actual_II", "actual_G", "q_perp_squared",
                                            "actual_normal_area", "G_minus_one",
                                            "q_perp2_minus_original_cross_q2_over_G",
                                            "theta", "current_operator_norm",
                                            "invariant_column_lower_bound")},
                    "position_two_jets_without_X": {
                        name: _payload(value) for name, value in
                        self.grids[label]["position_two_jets_without_X"].items()},
                    "input_source": copy.deepcopy(self.grids[label]["input_source"]),
                    "ell_identity": copy.deepcopy(self.grids[label]["ell_identity"])}
                for label in LABELS},
            "build_cost": _public(self.build_capture),
            "LP_matrix_reconstructible_from_saved_ring_rows_and_exact_embedding": True,
            "no_fullgrid_position_or_dense_parameter_J_payload": True}

    def candidate_from_raw(self, x18):
        """Retain exact ideal embedding and the actually rounded q separately."""
        self.assert_context()
        x = _array(x18, (VARIABLES,), "finite raw18")
        xi = tuple(Q.from_float(float(v)) for v in x[:PARAMETERS])
        base = tuple(Q.from_float(float(v)) for v in self.state168)
        delta = [Q(0) for _ in range(168)]
        for entry in self.embedding_entries:
            delta[entry["independent168_row"]] += (
                Q(entry["weight_exact"])*xi[entry["parameter_column"]])
        ideal = tuple(a+d for a, d in zip(base, delta))
        physical_delta = tuple(delta[:154])+tuple(Q(0) for _ in range(18))
        ideal_physical = tuple(a+d for a, d in zip(self.base_physical172, physical_delta))
        ideal_h = 4*max(map(abs, physical_delta))
        candidate = self.state168.copy()
        changed = sorted({entry["independent168_row"] for entry in self.embedding_entries})
        for j in changed:
            candidate[j] = float(ideal[j])
        _require(np.all(np.isfinite(candidate)), "exact embedded solution overflowed binary64")
        candidate = _array(self.field.validate_state(candidate), (168,), "rounded168")
        rounded_exact = tuple(Q.from_float(float(v)) for v in candidate)
        actual_physical = tuple(self.field.full_coefficients(candidate, exact=True))
        actual_delta = tuple(a-b for a, b in zip(actual_physical, self.base_physical172))
        actual_h = 4*max(map(abs, actual_delta))
        bad_box = [j for j, (lo, value, hi) in enumerate(
            zip(self.lower172, actual_physical, self.upper172)) if value < lo or value > hi]
        ideal_bad_box = [j for j, (lo, value, hi) in enumerate(
            zip(self.lower172, ideal_physical, self.upper172)) if value < lo or value > hi]
        rounding = tuple(a-b for a, b in zip(rounded_exact, ideal))
        # Original actual implementation uses these same binary64 endpoints.
        actual_box = self.field.exact_full_box_decision(
            candidate, np.array(list(map(float, self.lower172))),
            np.array(list(map(float, self.upper172))))
        _require(actual_box["exact_full_box_pass"] == (not bad_box),
                 "canonical and original exact172 box decisions disagree")
        actual_h_pass = actual_h <= self.maximum_h_exact
        record = {
            "schema": POLICY+"-exact-embedding-and-rounded-candidate",
            "model_binding_sha256": self.binding_sha256,
            "raw18": _vector(x), "xi17_exact_binary64": [str(v) for v in xi],
            "unrounded_exact_independent168_increment": [str(v) for v in delta],
            "unrounded_exact_independent168": [str(v) for v in ideal],
            "unrounded_exact_physical172_increment": [str(v) for v in physical_delta],
            "unrounded_exact_physical172": [str(v) for v in ideal_physical],
            "unrounded_exact_h": str(ideal_h),
            "unrounded_exact_box_pass": not ideal_bad_box,
            "unrounded_exact_box_violating_indices": ideal_bad_box,
            "unrounded_exact_h_bound_pass": bool(ideal_h <= self.maximum_h_exact),
            "rounded_independent168": _vector(candidate),
            "rounded_physical172_exact": [str(v) for v in actual_physical],
            "rounded_physical172_binary64": _vector(np.array(list(map(float, actual_physical)))),
            "rounded_exact_physical172_increment": [str(v) for v in actual_delta],
            "rounded_exact_h": str(actual_h),
            "rounded_exact_box_decision": actual_box,
            "rounded_exact_h_bound_pass": bool(actual_h_pass),
            "rounded_exact_h_at_most_original_small_1_over_128":
                bool(actual_h <= Q(REFERENCE_SMALL_H_EXACT)),
            "independent_rounding_error_exact": [str(v) for v in rounding],
            "physical_rounding_error_exact": [
                str(a-b) for a, b in zip(actual_physical, ideal_physical)],
            "maximum_absolute_independent_rounding_error_exact": str(max(map(abs, rounding))),
            "rounding": "each touched exact current+R2*binary64-xi coordinate rounded once",
            "untouched168_coordinates_keep_the_original_literal_binary64": True,
            "exact_ring_identity_applies_to_unrounded_rational_embedding_only": True,
            "rounded_candidate_claimed_exactly_ring_metric_neutral": False,
            "actual14_or_fullbody_feasibility_claimed": False,
            "original_actual_box_and_new_explicit_h_pass":
                bool(not bad_box and actual_h_pass),
            "candidate_physical_identity_sha256": digest(self.field.identity(candidate))}
        return candidate, record


def _raw_numeric(value):
    """Keep true backend arrays before any status/finite/candidate filter."""
    if value is None:
        return None
    a = np.asarray(value)
    if a.dtype.kind not in "fiu":
        raise ValueError("backend numeric output has a nonnumeric dtype")
    x = np.asarray(a, dtype=np.float64)
    finite = np.isfinite(x)
    flat = x.ravel()
    values = [float(v) if math.isfinite(float(v)) else
              ("NaN" if math.isnan(float(v)) else ("+Infinity" if float(v) > 0 else "-Infinity"))
              for v in flat]
    return {
        **array_binding(x), "all_finite": bool(np.all(finite)),
        "values_flat": values,
        "exact_binary64_flat": [
            str(Q.from_float(float(v))) if math.isfinite(float(v)) else values[j]
            for j, v in enumerate(flat)],
        "literal_shape_is_retained_above": True}


def _backend_snapshot(result, model, assembly_metadata, elapsed, version, options):
    """No candidate decision is made here; a finite/nonfinite raw18 is retained."""
    out = {
        "schema": POLICY+"-original-backend-return",
        "model_binding_sha256": model.binding_sha256,
        "assembly": copy.deepcopy(assembly_metadata),
        "backend": "scipy.optimize.linprog(method='highs')",
        "scipy_version": str(version), "options": copy.deepcopy(options),
        "status": None if result.get("status") is None else int(result.get("status")),
        "success": bool(result.get("success", False)),
        "message": str(result.get("message", "")),
        "nit": None if result.get("nit") is None else int(result.get("nit")),
        "crossover_nit": None if result.get("crossover_nit") is None
                         else int(result.get("crossover_nit")),
        "fun": _raw_numeric(result.get("fun")),
        "raw18": _raw_numeric(result.get("x")),
        "slack": _raw_numeric(result.get("slack")),
        "con": _raw_numeric(result.get("con")),
        "backend_elapsed_seconds": float(elapsed),
        "raw_captured_before_status_or_candidate_filter": True,
        "configured_time_limit_is_not_claimed_strict_backend_wall_time": True}
    for name in ("ineqlin", "eqlin", "lower", "upper"):
        block = result.get(name)
        out[name] = None if block is None else {
            key: _raw_numeric(block.get(key)) for key in ("residual", "marginals")}
    raw = out["raw18"]
    out["all18_finite_values_actually_saved"] = bool(
        raw is not None and raw["shape"] == [VARIABLES] and raw["all_finite"]
        and len(raw["values_flat"]) == VARIABLES)
    return out


def _row_residual(A, b, x, tags):
    residual = A@x-b
    _require(np.all(np.isfinite(residual)), "nonfinite original-unit LP residual")
    violation = np.maximum(residual, 0.)
    by_kind = {}
    for kind in sorted({tag["kind"] for tag in tags}):
        take = np.array([tag["kind"] == kind for tag in tags], dtype=bool)
        by_kind[kind] = {
            "row_count": int(np.count_nonzero(take)),
            "maximum_signed_residual": float(np.max(residual[take])),
            "maximum_violation": float(np.max(violation[take])),
            "within_declared_floating_row_tolerance":
                bool(np.all(residual[take] <= LP_ROW_TOLERANCE))}
    index = int(np.argmax(violation))
    return {
        "schema": POLICY+"-original-unit-row-residual",
        "tolerance": LP_ROW_TOLERANCE,
        "all_rows_pass": bool(np.all(residual <= LP_ROW_TOLERANCE)),
        "maximum_violation": float(violation[index]),
        "maximum_violation_original_row": copy.deepcopy(tags[index]),
        "by_kind": by_kind, "residual_array": _payload(residual),
        "not_an_exact_or_fullbody_certificate": True}


def _predicted_ring(model, xi):
    answer = {}
    for label in LABELS:
        grid = model.grids[label]
        change = grid["ell"]@xi
        A, B, C = grid["A"]+change, grid["B"], grid["C"]
        norm = _operator_norm(A, B, C)
        at = int(np.argmax(norm))
        K = float(model.target_exact)
        psd = np.stack((
            2*K+A+C, (K+A)*(K+C)-B*B,
            2*K-A-C, (K-A)*(K-C)-B*B), axis=-1)
        answer[label] = {
            "change_of_S11": _payload(change),
            "ring_operator_norm": _payload(norm),
            "four_PSD_rows": _payload(psd),
            "maximum_operator_norm": float(norm[at]),
            "attainer": {"theta_index": at, "theta": float(grid["theta"][at])},
            "target_exact": str(model.target_exact),
            "floating_exact_sign_PSD_pass": bool(np.all(psd >= 0.)),
            "floating_PSD_with_declared_row_tolerance":
                bool(np.all(psd >= -LP_ROW_TOLERANCE)),
            "model_only_for_exact_R2_embedding_not_rounded_actual_or_fullbody": True}
    return answer


def solve_ring17_once(
        model, *, charge_call, wall, time_limit_seconds, emit=None, capture=None):
    """Attempt at most one newly charged LP on this model.

    charge_call(metadata) is invoked before importing/entering the backend
    and must debit the external new-task solver account.  wall(stage) is
    checked before and after each potentially costly phase.  The caller
    supplies min(authorized single-call limit, true remaining task time).

    A timeout or non-success backend return is an undecided result even
    when it contains a vector.  Every actual returned numeric value is
    captured first.  There is no free retry, rerounding search or repair LP.
    Full nonlinear prediction and original body gates belong to the caller.
    """
    started = time.monotonic()
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty one-solve capture required")
    sink.update(schema=POLICY+"-one-solve-capture", status="entered",
                charged_new_solver_calls=0, actual_backend_calls=0,
                backend_result=None, candidate_record=None,
                candidate_qualified_for_external_prediction=False, events=[],
                no_restart=True, _arrays={})
    trace = _Trace(wall, sink)
    candidate = None
    try:
        _wall(wall, "ring17.solve.entry")
        _require(isinstance(model, Ring17Model), "the bound current ring17 model is required")
        model.assert_context()
        _require(not model.solve_attempted, "this ring17 instance has already been considered")
        _require(callable(charge_call), "external solver-account charge callback required")
        limit = float(time_limit_seconds)
        _require(math.isfinite(limit) and limit > 0,
                 "an explicit positive externally bounded single-solver limit is required")
        _require(emit is None or callable(emit), "optional original stdout emitter must be callable")
        model.solve_attempted = True
        model.solve_record = sink
        sink["model_binding_sha256"] = model.binding_sha256
        sink["target_exact"] = str(model.target_exact)
        summary = model.summary()
        if summary["floating_invariant_column_obstruction"]:
            sink.update(
                status="floating-invariant-column-bound-blocks-this-ring-family",
                decision="no LP; target excluded in the supplied floating ring model",
                invariant_column_report=summary["grids"],
                exact_continuous_infeasibility_claimed=False,
                elapsed_seconds_before_return=float(time.monotonic()-started))
            _wall(wall, "ring17.solve.no-LP.complete")
            return {"status": sink["status"], "qualified": False,
                    "candidate168": None, "candidate_record": None,
                    "report": _public(sink)}

        def retain_assembly(value):
            sink["_arrays"]["LP_arrays_and_tags"] = value
            sink["assembly"] = copy.deepcopy(value[-1])
        assembled, _ = trace.run(
            "finite_ring_LP_assembly", model.assemble, retain_assembly,
            model_binding_sha256=model.binding_sha256)
        A, b, c, tags, metadata = assembled
        charge_metadata = {
            "kind": "one-new-current-ring17-HiGHS-LP",
            "model_binding_sha256": model.binding_sha256,
            "variables": VARIABLES, "rows": len(b),
            "time_limit_seconds": limit,
            "objective": "min h", "maximum_h_exact": str(model.maximum_h_exact),
            "old_LP_and_cone_instances_reopened": False}
        event = {
            "kind": "new_solver_call", "status": "charging",
            "charge_attempted": True, "charge_completed": False,
            "backend_entered": False, "model_binding_sha256": model.binding_sha256}
        sink["events"].append(event)
        call_phase_started = time.monotonic()
        backend_started = call_phase_started
        try:
            # The external callback must atomically enforce/debit the quota.
            # Its own failure receipt stays with the caller and this event.
            charge_receipt = charge_call(copy.deepcopy(charge_metadata))
            sink["charged_new_solver_calls"] = 1
            event.update(charge_completed=True, charge_receipt=copy.deepcopy(charge_receipt),
                         status="charged")
            _wall(wall, "ring17.solve.after-charge-before-backend")
            import scipy
            from scipy.optimize import linprog

            # Subtract work since the caller supplied its remaining-time
            # allowance.  The backend may still return late; the actual wall
            # time and post-call external deadline check remain authoritative.
            effective_limit = limit-float(time.monotonic()-started)
            _require(effective_limit > 0.,
                     "externally supplied solve-time allowance ended before backend entry")
            options = {
                "time_limit": effective_limit, "presolve": True,
                "primal_feasibility_tolerance": LP_ROW_TOLERANCE,
                "dual_feasibility_tolerance": LP_ROW_TOLERANCE}
            sink["solver_options"] = copy.deepcopy(options)
            sink["requested_remaining_time_allowance_seconds"] = limit
            sink["scipy_version"] = scipy.__version__
            # A scoped new caller, not this import-only module, decides the
            # maximum permitted time.  Import/metadata cost is still in its
            # total clock and is checked before the actual solve.
            _wall(wall, "ring17.solve.before-backend")
            backend_started = time.monotonic()
            event.update(backend_entered=True, status="backend-started")
            sink["actual_backend_calls"] = 1
            result = linprog(
                c, A_ub=A, b_ub=b,
                bounds=[(None, None)]*VARIABLES,
                method="highs", options=options)
            backend_elapsed = float(time.monotonic()-backend_started)
            # Preserve the actual OptimizeResult first, including pathological
            # nonfinite data, so a later serialization/status/clock failure
            # cannot pretend no vector had been returned.
            sink["_arrays"]["actual_backend_result_before_filter"] = result
            event.update(status="backend-returned", backend_elapsed_seconds=backend_elapsed,
                         total_call_phase_seconds=float(time.monotonic()-call_phase_started))
            backend = _backend_snapshot(
                result, model, metadata, backend_elapsed, scipy.__version__, options)
            sink["backend_result"] = backend
            event["all18_finite_values_actually_saved"] = backend["all18_finite_values_actually_saved"]
            if emit is not None:
                output_start = time.monotonic()
                receipt = emit("FINITE_RESULT", copy.deepcopy(backend))
                sink["finite_result_original_stdout_receipt"] = copy.deepcopy(receipt)
                sink["finite_result_emit_seconds"] = float(time.monotonic()-output_start)
            event["total_call_phase_seconds"] = float(time.monotonic()-call_phase_started)
            _wall(wall, "ring17.solve.backend-return-and-raw-output")
        except Exception as error:
            event.update(error=_error(error),
                         total_call_phase_seconds=float(time.monotonic()-call_phase_started))
            if event["status"] != "backend-returned":
                event["status"] = "raised"
            raise

        _require(sink["backend_result"] is not None, "missing retained backend return")
        backend = sink["backend_result"]
        eligible = bool(backend["status"] == 0 and backend["success"]
                        and backend["all18_finite_values_actually_saved"])
        if not eligible:
            sink.update(status="backend-status-or-vector-ineligible-no-decision",
                        decision="no candidate; original backend status retained",
                        backend_failure_or_timeout_not_infeasibility_certificate=True)
        else:
            x = np.asarray(result["x"], dtype=np.float64)
            def retain_residual(value):
                sink["original_unit_row_residual"] = value
            residual, _ = trace.run(
                "returned_original_unit_row_residual",
                lambda: _row_residual(A, b, x, tags), retain_residual)
            def retain_exact(value):
                sink["_arrays"]["actually_rounded_candidate168"] = value[0]
                sink["candidate_record"] = value[1]
            embedded, _ = trace.run(
                "exact_embedding_and_actual_binary64_rounding",
                lambda: model.candidate_from_raw(x), retain_exact)
            candidate = embedded[0]
            def retain_prediction(value):
                sink["unrounded_R2_ring_model_prediction"] = value
            _, _ = trace.run(
                "saved_R2_ring_model_prediction",
                lambda: _predicted_ring(model, x[:PARAMETERS]), retain_prediction)
            exact_gate = sink["candidate_record"]["original_actual_box_and_new_explicit_h_pass"]
            qualified = bool(residual["all_rows_pass"] and exact_gate)
            sink["candidate_qualified_for_external_prediction"] = qualified
            sink["exact_minimum_h_or_actual_ring_neutrality_claimed"] = False
            sink["raw_h_minus_unrounded_exact_physical_h"] = str(
                Q.from_float(float(x[-1]))-Q(sink["candidate_record"]["unrounded_exact_h"]))
            sink["raw_h_minus_rounded_exact_physical_h"] = str(
                Q.from_float(float(x[-1]))-Q(sink["candidate_record"]["rounded_exact_h"]))
            sink["status"] = (
                "one-ring-proposal-awaits-fullbody-prediction-and-original-actual-gates"
                if qualified else "returned-solution-failed-row-or-exact-box-norm-eligibility")
            if not qualified:
                candidate = None
        sink["elapsed_seconds_before_return"] = float(time.monotonic()-started)
        _wall(wall, "ring17.solve.complete")
        return {
            "status": sink["status"],
            "qualified": bool(sink["candidate_qualified_for_external_prediction"]),
            "candidate168": candidate,
            "candidate_record": copy.deepcopy(sink["candidate_record"]),
            "report": _public(sink)}
    except Exception as error:
        sink.update(status="raised", error=_error(error),
                    candidate_qualified_for_external_prediction=False,
                    elapsed_seconds_before_raise=float(time.monotonic()-started))
        # No made-up empty scientific arrays, no solver retry and no recovered
        # candidate qualification after a scope/serialization failure.
        raise


def ring17_capture_record(capture, *, include_arrays=False):
    """Serialize only genuinely retained work, including incomplete failures.

    This is an output helper, not a scientific re-evaluation.  Use
    include_arrays=True only when the future scope chooses to preserve
    partial returned arrays in original stdout.  Runtime grid objects are
    identified as not serialized; they are never replaced by zero arrays.
    Successful models have the smaller, explicit full_record() format.
    """
    _require(isinstance(capture, dict), "actual ring capture dictionary required")
    def convert(value):
        if isinstance(value, np.ndarray):
            if value.dtype.kind in "fiu":
                if np.all(np.isfinite(value)):
                    return _payload(value)
                return _raw_numeric(value)
            return {"unserialized_array_dtype": str(value.dtype),
                    "shape": list(value.shape), "values_saved": False}
        if isinstance(value, dict):
            return {str(key): convert(item) for key, item in value.items()
                    if include_arrays or key != "_arrays"}
        if isinstance(value, (list, tuple)):
            return [convert(item) for item in value]
        if isinstance(value, Q):
            return str(value)
        if isinstance(value, (np.bool_, bool)):
            return bool(value)
        if isinstance(value, (np.integer, int)):
            return int(value)
        if isinstance(value, (np.floating, float)):
            return float(value) if math.isfinite(float(value)) else (
                "NaN" if math.isnan(float(value)) else
                ("+Infinity" if float(value) > 0 else "-Infinity"))
        if value is None or isinstance(value, str):
            return value
        return {
            "runtime_object_type_not_serialized":
                type(value).__module__+"."+type(value).__name__,
            "values_saved": False,
            "reason": "not a returned scientific array or JSON metadata"}
    return {
        "schema": POLICY+"-capture-output",
        "raw_arrays_included": bool(include_arrays),
        "actual_capture": convert(capture),
        "only_actually_retained_values_no_empty_scientific_surrogates": True,
        "output_cost_belongs_to_external_new_scientific_clock": True}

#!/usr/bin/env python3
"""R516/R519 common reflected R1 ray and one conditional R2 fiber; import-only.

The caller owns a new scientific clock and separate one-LS/one-LP accounts.
Only the complete already-paid current ring record is consumed.  No ordinary
geometry, selected J, old LP instance, scalar search, or actual gate is run here.
The R1 model point is never made an accepted point.  Its exact increment and the
new R2 solution are added to the original current point before one final rounding.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import periodic_operator
from frame_height_null_coordinates import digest
from frame_complete_body_extension168 import array_binding
from frame_complete_body_extension168_joint_selected import _context
from frame_complete_body_extension168_curvature_prediction import _validate_metric
from frame_metric_current168_ring17 import (
    Ring17Model, POLICY as RING_POLICY, LABELS, JETS, PARAMETERS, VARIABLES,
    LP_ROW_TOLERANCE, REFERENCE_SMALL_H_EXACT,
    _require, _error, _wall, _array, _same, _q, _vector, _payload, _bounds,
    _grid_context, _ring_source_identity, _embedding, _normal_shape, _operator_norm,
    _raw_numeric, solve_ring17_once, ring17_capture_record)


POLICY = "true58-original-box-reflected-R1-ray-and-one-R2-fiber-v1"
TARGET_EXACT = "1000/61"
ALPHA_EXACT = ("1/2", "3/8", "1/4", "1/8", "1/16", "1/32", "1/64")
LS_TOLERANCE = 1.e-10
LS_MAX_ITERATIONS = 68


def definition():
    return {
        "schema": POLICY,
        "source": "one fixed actual current168 point and its complete paid ring MODEL",
        "new_family": "original R1 u9/v8 followed by one original R2 u9/v8 fiber",
        "base_point_never_replaced_by_unaccepted_R1_point": True,
        "source_G": "actual dot(T,T); never substitute one",
        "reflection": "-2*(U dot (T cross Ttheta))/|T cross Ttheta|^2*(T cross Ttheta)",
        "reflection_mean": "retained in the target and residual; no height compensation",
        "common_coefficients": 17,
        "LS_domain": "R516 exact projected original172 box J1; inward binary64 endpoints",
        "LS_grid_weights": "1/(2*n_grid) per three-vector angular sample",
        "LS_backend": "one scipy.optimize.lsq_linear(method='bvls')",
        "LS_tol": LS_TOLERANCE, "LS_max_iter": LS_MAX_ITERATIONS,
        "zero_width_coordinates": "eliminated at their exact value zero",
        "LS_timeout": "no backend time-limit API; external before/after clock is authoritative",
        "fixed_alpha_exact": list(ALPHA_EXACT),
        "all_seven_scales_evaluated_once": True,
        "selection": "first nonzero scale passing metric, positive Q, column quartic and remaining box",
        "metric_budget": "required current-point receipt argument, never cfg target .26",
        "column_target_exact_default": TARGET_EXACT,
        "R1_table": "U=U0+alpha*Vx; Xst=Xst0+a*alpha*Zx; Xss=Xss0+alpha*Lx+alpha^2*Hxx",
        "R2_table": "only Xss changes by V17*y at the selected unrounded R1 model point",
        "LP": "one new min-h 18-variable original-box conditional R2 problem",
        "physical_norm": "h >= 4*||exact combined R1+R2 physical172 increment||infinity",
        "candidate": "exact original binary64 base + exact R1 increment + exact R2*y, rounded once",
        "rounded_candidate_claimed_ring_isometric": False,
        "ordinary_calls": 0, "selected_J_calls": 0, "old_instance_calls": 0,
        "actual_gate_calls": 0, "global_optimality_or_infeasibility_certificate": False}


def implementation_hashes():
    names = (
        Path(__file__).name, "frame_metric_current168_ring17.py",
        "frame_complete_body_extension168.py",
        "frame_complete_body_extension168_joint_selected.py",
        "frame_complete_body_extension168_curvature_prediction.py",
        "frame_collar_bvp.py", "frame_collar_enriched.py",
        "frame_entry_single_q.py", "frame_entry_paired_repair.py",
        "frame_five_height_field.py", "frame_height_null_coordinates.py")
    root = Path(__file__).parent
    return {name: hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names}


def _public(record):
    return {key: copy.deepcopy(value) for key, value in record.items()
            if key not in ("_arrays", "_objects")}


class _Trace:
    """Nested real work receipts; the external wall and debit callbacks own limits."""
    def __init__(self, wall, capture):
        self.wall = wall
        self.events = capture.setdefault("events", [])
        self.counts = capture.setdefault("component_counts", {})

    def run(self, kind, operation, retain, **metadata):
        count = self.counts.setdefault(
            kind, {"started": 0, "entered": 0, "completed": 0, "failed": 0})
        count["started"] += 1
        event = {"kind": kind, "ordinal": count["started"], "status": "started",
                 "work_call_entered": False, **copy.deepcopy(metadata)}
        self.events.append(event)
        tick = time.monotonic()
        try:
            _wall(self.wall, "reflected-R1."+kind)
            event["work_call_entered"] = True
            count["entered"] += 1
            result = operation()
            retain(result)
            count["completed"] += 1
            event.update(status="complete", seconds=float(time.monotonic()-tick))
            _wall(self.wall, "reflected-R1."+kind+".complete")
            return result, event
        except Exception as error:
            if event["status"] == "started":
                count["failed"] += 1
                event.update(status="raised", error=_error(error),
                             seconds=float(time.monotonic()-tick))
            else:
                event.update(post_completion_error=_error(error),
                             completed_work_retained_but_return_blocked=True,
                             seconds_at_exception=float(time.monotonic()-tick))
            raise


def _decode_payload(value, shape, name):
    _require(isinstance(value, dict) and "values" in value,
             "complete paid array payload required: "+name)
    dtype = np.dtype(value.get("dtype"))
    _require(dtype.kind == "f" and dtype.itemsize == 8,
             "paid binary64 array required: "+name)
    array = np.asarray(value["values"], dtype=dtype)
    _require(array.shape == tuple(shape) and np.all(np.isfinite(array)),
             "paid finite array shape mismatch: "+name)
    expected = array_binding(array)
    _require(all(value.get(key) == item for key, item in expected.items()),
             "paid array fingerprint mismatch: "+name)
    array = array.copy()
    array.setflags(write=False)
    return array


def _load_paid_ring(field, q, radial, thetas, paid, metric_bound, cfg, low, high):
    _require(isinstance(paid, dict)
             and paid.get("schema") == RING_POLICY+"-full-ring-model",
             "the complete original ring MODEL, not a report projection, is required")
    binding = paid.get("binding")
    _require(isinstance(binding, dict)
             and paid.get("binding_sha256") == digest(binding),
             "original paid ring binding fingerprint mismatch")
    source = binding.get("source")
    _require(isinstance(source, dict), "paid ring current-source identity missing")
    ring_index = source.get("ring_radial_index")
    q, r, th = _grid_context(field, q, radial, thetas, ring_index)
    current_identity = _ring_source_identity(field, q, r, th, ring_index)
    _require(all(source.get(key) == value for key, value in current_identity.items()),
             "paid ring belongs to another field/state/grid/ring")
    _require(source.get("configuration_sha256") == digest(cfg),
             "paid ring original configuration differs")
    metric = _validate_metric(field, r, metric_bound)
    _require(source.get("fixed_metric_binding_sha256") == metric_bound["binding_sha256"],
             "paid ring fixed-metric binding differs")
    physical = tuple(field.full_coefficients(q, exact=True))
    _require(source.get("physical172_exact") == [str(v) for v in physical]
             and paid.get("physical172_exact") == [str(v) for v in physical],
             "paid ring physical172 identity differs")
    _require(source.get("lower172_exact") == [str(v) for v in low]
             and source.get("upper172_exact") == [str(v) for v in high],
             "original172 box was changed")
    _require(_same(_decode_payload(paid.get("state168"), (168,), "paid/state168"), q),
             "paid ring state168 changed")
    _require(all(lo <= value <= hi for lo, value, hi in zip(low, physical, high)),
             "the current point is outside its original physical172 box")
    grids = {}
    for label in LABELS:
        data = paid.get("grids", {}).get(label)
        _require(isinstance(data, dict), "both complete paid ring grids required")
        n = len(th[label])
        arrays = data.get("arrays", {})
        needed = {
            "A": (n,), "B": (n,), "C": (n,), "ell": (n, 17),
            "normal": (n, 3), "actual_I": (n, 2, 2), "actual_II": (n, 2, 2),
            "actual_G": (n,), "q_perp_squared": (n,), "actual_normal_area": (n,),
            "theta": (n,), "G_minus_one": (n,),
            "q_perp2_minus_original_cross_q2_over_G": (n,),
            "current_operator_norm": (n,), "invariant_column_lower_bound": (n,)}
        restored = {key: _decode_payload(arrays.get(key), shape, label+"/"+key)
                    for key, shape in needed.items()}
        _require(_same(restored["theta"], th[label]), "paid theta ordering changed")
        for key, expected in binding["grid_arrays"][label].items():
            _require(key in restored and array_binding(restored[key]) == expected,
                     "paid ring model array not bound: "+label+"/"+key)
        positions = data.get("position_two_jets_without_X", {})
        jets = {key: _decode_payload(positions.get(key), (n, 3), label+"/"+key)
                for key in JETS}
        for key, expected in binding["grid_position_arrays"][label].items():
            _require(key in jets and array_binding(jets[key]) == expected,
                     "paid position twojet not bound: "+label+"/"+key)
        _require(digest(data["ell_identity"])
                 == binding["grid_ell_binding_sha256"][label],
                 "original ell provenance changed")
        grids[label] = {
            **restored, "position_two_jets_without_X": jets,
            "input_source": copy.deepcopy(data.get("input_source")),
            "paid_ell_identity": copy.deepcopy(data["ell_identity"])}
    return q, r, th, ring_index, physical, metric, grids, current_identity


def _exact_three_jet_basis(single, sigma, paid_definition):
    """Consume the paid literal basis jets; solve the new full inverse once."""
    _require(isinstance(paid_definition, dict), "paid exact radial definition missing")
    knots = tuple(Q(v) for v in single.radial_knots)
    _require([str(v) for v in knots] == paid_definition.get("knots_exact")
             and len(knots) == 21 and knots[0] == Q("9/250")
             and knots[-1] == Q("423/500") and knots[-7] == Q("153/200"),
             "published complete original quintic knot descriptor changed")
    _require(knots[-7] < sigma < knots[-1]
             and paid_definition.get("sigma_exact") == str(sigma)
             and paid_definition.get("full_spline_indices") == [9, 10, 11],
             "paid last-span ring identity changed")
    entry_end = Q(single.entry.left_exact)+Q(single.entry.length_exact)
    _require(entry_end <= knots[9]
             and paid_definition.get("entry_weight_end_exact") == str(entry_end),
             "entry weights must already be one on all three original supports")
    matrix = [[Q(v) for v in row]
              for row in paid_definition["basis_jet_matrix_exact"]]
    _require(len(matrix) == 3 and all(len(row) == 3 for row in matrix),
             "the paid exact three-jet matrix must be 3 by 3")
    work = [row+[Q(int(i == j)) for j in range(3)]
            for i, row in enumerate(matrix)]
    operations = []
    for column in range(3):
        pivot = next((i for i in range(column, 3) if work[i][column]), None)
        _require(pivot is not None, "the exact original three-jet matrix is singular")
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            operations.append({"swap": [column, pivot]})
        denominator = work[column][column]
        work[column] = [v/denominator for v in work[column]]
        operations.append({"row": column, "divide_exact": str(denominator)})
        for i in range(3):
            if i != column and work[i][column]:
                coefficient = work[i][column]
                work[i] = [a-coefficient*b for a, b in zip(work[i], work[column])]
                operations.append({"row": i, "subtract_row": column,
                                   "coefficient_exact": str(coefficient)})
    inverse = tuple(tuple(work[i][3+j] for j in range(3)) for i in range(3))
    _require(all(sum(matrix[i][k]*inverse[k][j] for k in range(3))
                 == Q(int(i == j)) for i in range(3) for j in range(3)),
             "exact R0/R1/R2 elimination did not give the identity")
    weights = tuple(tuple(inverse[i][j] for i in range(3)) for j in range(3))
    _require([str(v) for v in weights[2]] == paid_definition["weights_exact"],
             "new full inverse disagrees with the original paid R2 column")
    record = {
        "schema": POLICY+"-exact-R0-R1-R2",
        "source": "original paid ring basis-jet array; no spline jet reevaluation",
        "original_paid_R2_definition": copy.deepcopy(paid_definition),
        "sigma_exact": str(sigma), "basis_jet_matrix_exact":
            [[str(v) for v in row] for row in matrix],
        "inverse_by_spline_row_and_radial_jet_column":
            [[str(v) for v in row] for row in inverse],
        "R0_weights_exact": [str(v) for v in weights[0]],
        "R1_weights_exact": [str(v) for v in weights[1]],
        "R2_weights_exact": [str(v) for v in weights[2]],
        "exact_elimination_operations": operations,
        "full_original_supports_retained": True,
        "front_102_middle_body_coupling_not_deleted": True}
    return matrix, inverse, weights, record


def _mode_physical_rows(j):
    _require(type(j) is int and 0 <= j < 17, "original angular mode required")
    if j < 9:
        return tuple((6+k)*9+j for k in range(3))
    return tuple(81+(6+k)*8+(j-9) for k in range(3))


def _project_original_box(matrix, inverse, low, high, physical):
    """Exact R516 J1 projection, with all zero-width and empty cases explicit."""
    intervals, modes = [], []
    for j in range(17):
        indices = _mode_physical_rows(j)
        lower = tuple(low[i]-physical[i] for i in indices)
        upper = tuple(high[i]-physical[i] for i in indices)
        vertices = {}
        for free in range(3):
            if not matrix[0][free]:
                continue
            fixed = [i for i in range(3) if i != free]
            for bits in ((0, 0), (0, 1), (1, 0), (1, 1)):
                point = [Q(0)]*3
                for k, bit in zip(fixed, bits):
                    point[k] = (upper if bit else lower)[k]
                point[free] = -sum(matrix[0][k]*point[k] for k in fixed)/matrix[0][free]
                if all(a <= c <= b for a, c, b in zip(lower, point, upper)):
                    vertices[tuple(point)] = {
                        "original_three_coefficient_increment_exact": [str(v) for v in point],
                        "R1_exact": str(sum(matrix[1][k]*point[k] for k in range(3))),
                        "R2_exact": str(sum(matrix[2][k]*point[k] for k in range(3)))}
        _require(bool(vertices), "empty exact original-box R0=0 slice for angular mode "+str(j))
        values = [Q(v["R1_exact"]) for v in vertices.values()]
        lo, hi = min(values), max(values)
        _require(lo <= 0 <= hi, "current feasible base must lie in every projected J1 interval")
        intervals.append((lo, hi))
        modes.append({
            "mode": j, "kind": "u" if j < 9 else "v",
            "physical172_rows": list(indices),
            "original_increment_lower_exact": [str(v) for v in lower],
            "original_increment_upper_exact": [str(v) for v in upper],
            "R1_lower_exact": str(lo), "R1_upper_exact": str(hi),
            "exact_zero_width": lo == hi,
            "vertices": list(vertices.values()),
            "projection_guarantees_some_box_R2_not_a_curvature_R2": True})
    record = {
        "schema": POLICY+"-exact-J1-projected-box", "modes": modes,
        "all_seventeen_bounds_from_one_original172_box": True,
        "not_a_product_box_assumption_on_the_fifty_one_physical_coefficients": True}
    return tuple(intervals), record


def _inward_float(value, side):
    out = float(value)
    _require(math.isfinite(out), "finite projected box endpoint required")
    if side == "lower" and Q.from_float(out) < value:
        out = math.nextafter(out, math.inf)
    if side == "upper" and Q.from_float(out) > value:
        out = math.nextafter(out, -math.inf)
    return out


def _remaining_R2_intervals(x_exact, inverse, low, high, physical, hmax):
    intervals, modes = [], []
    feasible = True
    for j, x in enumerate(x_exact):
        lo_y = None
        hi_y = None
        constraints = []
        for k, index in enumerate(_mode_physical_rows(j)):
            fixed = inverse[k][1]*x
            coefficient = inverse[k][2]
            lo = max(low[index]-physical[index], -hmax/4)
            hi = min(high[index]-physical[index], hmax/4)
            entry = {"physical172_index": index, "fixed_R1_exact": str(fixed),
                     "R2_coefficient_exact": str(coefficient),
                     "allowed_combined_increment_lower_exact": str(lo),
                     "allowed_combined_increment_upper_exact": str(hi)}
            if lo > hi:
                feasible = False
                entry["empty"] = True
            elif coefficient == 0:
                okay = lo <= fixed <= hi
                entry.update(zero_R2_coefficient=True, passed=okay)
                feasible = feasible and okay
            else:
                a, b = (lo-fixed)/coefficient, (hi-fixed)/coefficient
                if a > b:
                    a, b = b, a
                lo_y = a if lo_y is None else max(lo_y, a)
                hi_y = b if hi_y is None else min(hi_y, b)
                entry.update(lower_R2_exact=str(a), upper_R2_exact=str(b))
            constraints.append(entry)
        _require(lo_y is not None and hi_y is not None,
                 "injective exact R2 column must give bounded remaining interval")
        okay = lo_y <= hi_y
        feasible = feasible and okay
        intervals.append((lo_y, hi_y))
        modes.append({"mode": j, "lower_exact": str(lo_y), "upper_exact": str(hi_y),
                      "nonempty": okay, "constraints": constraints})
    return tuple(intervals), {
        "all_modes_nonempty": bool(feasible), "modes": modes,
        "maximum_h_exact": str(hmax),
        "only_box_and_combined_norm_existence_not_curvature_feasibility": True}


def _reflection_target(paid_grid, a):
    jets = paid_grid["position_two_jets_without_X"]
    U = jets["Xs"]
    T = jets["Xt"]/float(a)
    Ttheta = jets["Xtt"]/float(a)
    cross = np.cross(T, Ttheta)
    denominator = np.einsum("ij,ij->i", cross, cross)
    result = {"T_from_paid_Xt_over_a": T, "Ttheta_from_paid_Xtt_over_a": Ttheta,
              "cross": cross, "cross_squared": denominator}
    if not np.all(np.isfinite(denominator)) or np.any(denominator <= 0.):
        result.update(
            status="zero-or-nonfinite-reflection-denominator",
            valid=False,
            zero_or_nonfinite_indices=np.flatnonzero(
                ~np.isfinite(denominator) | (denominator <= 0.)).tolist(),
            analytic_extension_not_fabricated=True)
        return result
    scalar = -2*np.einsum("ij,ij->i", U, cross)/denominator
    D = scalar[:, None]*cross
    _require(np.all(np.isfinite(D)), "nonfinite general-G reflection target")
    mean = np.mean(D, axis=0)
    result.update(status="complete", valid=True, target=D, mean=mean,
                  mean_subtracted_for_LS=False,
                  discrete_mean_not_a_continuous_zero_mean_certificate=True,
                  actual_G_retained=paid_grid["actual_G"])
    return result


def _build_frame_columns(field, q, sigma, theta, a, label, trace, sink):
    completed = sink["_arrays"].setdefault("new_grids", {}).setdefault(label, {})
    def retain_frame(value):
        grid, fields, frame = value
        sink["_objects"].setdefault("scalar_grids", {})[label] = grid
        completed["scalar_fields"] = fields
        completed["scalar_frame"] = frame
    made, event = trace.run(
        "current_scalar_frame", lambda: field.scalar_frame(
            q, np.asarray([sigma], dtype=np.float64), theta),
        retain_frame, grid=label, radial_count=1, angular_count=len(theta),
        ordinary_calls=0, selected_J_calls=0)
    grid, fields, frame = made
    au = _array(grid.original_grid.angular["u"], (len(theta), 9), label+"/u9")
    av = _array(grid.original_grid.angular["v"], (len(theta), 8), label+"/v8")
    Tu = _array(frame["Tpart"]["u"], (1, len(theta), 3), label+"/Tu")
    Tv = _array(frame["Tpart"]["v"], (1, len(theta), 3), label+"/Tv")
    Z = np.concatenate((
        Tu[..., None]*au[None, :, None, :],
        Tv[..., None]*av[None, :, None, :]), axis=-1)
    _require(Z.shape == (1, len(theta), 3, 17) and np.all(np.isfinite(Z)),
             "complete original seventeen tangent columns required")
    completed.update(original_u9=au, original_v8=av, tangent_columns17=Z)
    def retain_primitive(value):
        completed["primitive_tangent_columns17"] = value
        completed["V17"] = float(a)*value[0]
    primitive, pi_event = trace.run(
        "complete_theta_Pi_seventeen_columns", lambda: periodic_operator(Z, -1),
        retain_primitive, grid=label, input=array_binding(Z),
        original_theta_count=len(theta), parameters=17, axis=1, order=-1)
    _require(primitive.shape == Z.shape and np.all(np.isfinite(primitive)),
             "finite full-angle primitive columns required")
    event["Tpart_u_binding"] = array_binding(Tu)
    event["Tpart_v_binding"] = array_binding(Tv)
    pi_event["output"] = array_binding(primitive)
    return completed


def _raw_all_fields(value):
    """Preserve every actual backend return, including nested lstsq tuples."""
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, (np.bool_,)):
        return bool(value)
    if isinstance(value, dict):
        return {str(key): _raw_all_fields(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return {"sequence_type": type(value).__name__,
                "items": [_raw_all_fields(item) for item in value]}
    if isinstance(value, (int, float, np.integer, np.floating, np.ndarray)):
        return _raw_numeric(value)
    return {"unsupported_type": type(value).__name__, "literal_repr": repr(value),
            "full_numeric_recoverability_claimed": False}


def _least_squares_once(intervals, new_grids, targets, charge, wall, emit, sink):
    _require(callable(charge), "external one-LS debit callback required")
    _require(emit is None or callable(emit), "optional stdout emitter must be callable")
    lower = np.asarray([_inward_float(v[0], "lower") for v in intervals])
    upper = np.asarray([_inward_float(v[1], "upper") for v in intervals])
    _require(np.all(lower <= 0.) and np.all(upper >= 0.),
             "zero must survive inward conversion of the original projected box")
    free = np.flatnonzero(lower < upper)
    eliminated = np.flatnonzero(lower == upper)
    _require(np.all(lower[eliminated] == 0.),
             "a zero-width projected increment must be exactly zero")
    matrices, vectors, weight_records = [], [], []
    for label in LABELS:
        n = len(targets[label]["target"])
        weight = 1./(2*n)
        factor = math.sqrt(weight)
        matrices.append((factor*new_grids[label]["V17"]).reshape(3*n, 17))
        vectors.append((factor*targets[label]["target"]).reshape(3*n))
        weight_records.append({"grid": label, "angle_count": n,
                               "weight_exact": str(Q(1, 2*n)),
                               "weight_binary64": weight, "sqrt_weight_binary64": factor})
    A_full = np.concatenate(matrices, axis=0)
    rhs = np.concatenate(vectors)
    A = A_full[:, free]
    lower_free, upper_free = lower[free], upper[free]
    ls_arrays = sink["_arrays"].setdefault("least_squares", {})
    ls_arrays.update(
        design_matrix17=A_full, target=rhs, reduced_design_matrix=A,
        lower17=lower, upper17=upper, free_indices=free,
        eliminated_indices=eliminated)
    sink["least_squares_domain"] = {
        "free_indices": free.tolist(), "eliminated_zero_indices": eliminated.tolist(),
        "original_exact_zero_width_indices": [
            j for j, (lo, hi) in enumerate(intervals) if lo == hi],
        "binary64_interval_collapsed_to_zero_indices": [
            int(j) for j in eliminated if intervals[int(j)][0] != intervals[int(j)][1]],
        "bounds_converted_inward_not_outward": True,
        "lower17": _vector(lower), "upper17": _vector(upper),
        "weights": weight_records, "design_matrix17": array_binding(A_full),
        "reduced_design_matrix": array_binding(A), "target": array_binding(rhs),
        "raw_reflection_mean_is_retained_in_the_target": True}
    if not len(free):
        sink["least_squares_status"] = "all-projected-coordinates-fixed-to-zero"
        sink["least_squares_backend_entered"] = False
        return None

    event = {
        "kind": "bounded_common_two_grid_least_squares",
        "status": "charging", "charge_attempted": True, "charge_completed": False,
        "backend_entered": False}
    sink["events"].append(event)
    start = time.monotonic()
    try:
        metadata = {
            "schema": POLICY+"-LS-charge", "backend": "scipy.optimize.lsq_linear",
            "method": "bvls", "common_variables": 17, "free_variables": len(free),
            "scalar_residual_rows": len(rhs), "max_iter": LS_MAX_ITERATIONS,
            "tol": LS_TOLERANCE, "one_attempt_no_retry": True,
            "design_matrix": array_binding(A), "target": array_binding(rhs)}
        event["charge_receipt"] = copy.deepcopy(charge(metadata))
        event.update(charge_completed=True, status="charged")
        sink["charged_new_least_squares_calls"] = 1
        _wall(wall, "reflected-R1.LS.after-charge")
        import scipy
        from scipy.optimize import lsq_linear
        options = {"method": "bvls", "tol": LS_TOLERANCE,
                   "max_iter": LS_MAX_ITERATIONS}
        sink["least_squares_options"] = copy.deepcopy(options)
        _wall(wall, "reflected-R1.LS.before-backend")
        backend_start = time.monotonic()
        event.update(status="backend-entered", backend_entered=True)
        sink["least_squares_backend_entered"] = True
        result = lsq_linear(A, rhs, bounds=(lower_free, upper_free), **options)
        backend_seconds = float(time.monotonic()-backend_start)
        ls_arrays["actual_backend_result_before_filter"] = result
        event.update(status="backend-returned", backend_elapsed_seconds=backend_seconds)
        raw = {
            "schema": POLICY+"-original-bounded-LS-return",
            "backend": "scipy.optimize.lsq_linear(method='bvls')",
            "scipy_version": str(scipy.__version__), "options": options,
            "status": None if result.get("status") is None else int(result.get("status")),
            "success": bool(result.get("success", False)),
            "message": str(result.get("message", "")),
            "nit": None if result.get("nit") is None else int(result.get("nit")),
            "backend_elapsed_seconds": backend_seconds,
            "entire_OptimizeResult_fields": _raw_all_fields(dict(result)),
            "free_indices": free.tolist(), "eliminated_zero_indices": eliminated.tolist(),
            "domain": copy.deepcopy(sink["least_squares_domain"]),
            "raw_capture_precedes_status_vector_and_scope_filters": True,
            "max_iter_is_not_a_strict_wall_time_limit": True,
            "continuous_exact_bounded_LS_optimality_claimed": False}
        sink["least_squares_raw_record"] = raw
        if emit is not None:
            tick = time.monotonic()
            receipt = emit("LEAST_SQUARES", copy.deepcopy(raw))
            sink["least_squares_original_stdout_receipt"] = copy.deepcopy(receipt)
            sink["least_squares_emit_seconds"] = float(time.monotonic()-tick)
        event["phase_elapsed_seconds"] = float(time.monotonic()-start)
        _wall(wall, "reflected-R1.LS.after-raw-output")
        vector = result.get("x")
        eligible = bool(raw["success"] and vector is not None)
        if eligible:
            vector = np.asarray(vector, dtype=np.float64)
            eligible = bool(vector.shape == (len(free),) and np.all(np.isfinite(vector)))
        if not eligible:
            sink["least_squares_status"] = "backend-status-or-vector-ineligible"
            return None
        xstar = np.zeros(17, dtype=np.float64)
        xstar[free] = vector
        exact = tuple(Q.from_float(float(v)) for v in xstar)
        box_pass = all(lo <= x <= hi for (lo, hi), x in zip(intervals, exact))
        residual = A_full @ xstar-rhs
        ls_arrays.update(full_xstar17=xstar, saved_weighted_residual=residual)
        per_grid = {}
        offset = 0
        for label in LABELS:
            n = len(targets[label]["target"])
            fitted = np.einsum("icj,j->ic", new_grids[label]["V17"], xstar)
            unweighted = fitted-targets[label]["target"]
            new_grids[label]["LS_fitted_vector"] = fitted
            new_grids[label]["LS_unweighted_residual"] = unweighted
            per_grid[label] = {
                "fitted_vector": array_binding(fitted),
                "residual": array_binding(unweighted),
                "mean_residual": np.mean(unweighted, axis=0).tolist(),
                "weighted_squared_residual": float(np.dot(
                    residual[offset:offset+3*n], residual[offset:offset+3*n])),
                "reflection_mean": targets[label]["mean"].tolist()}
            offset += 3*n
        sink["common_xstar"] = {
            "xstar17": _vector(xstar),
            "exact_J1_pass": bool(box_pass),
            "exact_nonzero": any(v != 0 for v in exact),
            "weighted_squared_residual": float(np.dot(residual, residual)),
            "per_grid": per_grid,
            "no_clipping_repair_or_second_LS": True,
            "projected_direction_not_claimed_exact_reflection_or_isometry": True}
        if not box_pass:
            sink["least_squares_status"] = "returned-common-vector-outside-exact-projected-box"
            return None
        if not any(exact):
            sink["least_squares_status"] = "returned-common-vector-is-exactly-zero"
            return None
        sink["least_squares_status"] = "one-nonzero-common-bounded-LS-ray"
        return xstar, exact
    except Exception as error:
        event.update(error=_error(error), phase_elapsed_seconds=float(time.monotonic()-start))
        if event["status"] != "backend-returned":
            event["status"] = "raised"
        raise


def _contract_R1_ray(new, xstar, a, a_s, label, trace):
    fields, frame = new["scalar_fields"], new["scalar_frame"]
    A = np.asarray(new["original_u9"]) @ xstar[:9]
    D = np.asarray(new["original_v8"]) @ xstar[9:]
    Tu = np.asarray(frame["Tpart"]["u"])[0]
    Tv = np.asarray(frame["Tpart"]["v"])[0]
    Z = A[:, None]*Tu+D[:, None]*Tv
    linear = 2*(A[:, None]*np.asarray(frame["Ts_value_part"]["u"])[0]
                +D[:, None]*np.asarray(frame["Ts_value_part"]["v"])[0])
    u = np.asarray(fields["u"]["value"])[0]
    v = np.asarray(fields["v"]["value"])[0]
    theta = np.asarray(fields["_theta"])
    theta = np.broadcast_to(theta, np.asarray(fields["u"]["value"]).shape)[0]
    phase = theta+u
    zero = np.zeros_like(u)
    N = np.stack((np.cos(phase), np.sin(phase), zero), axis=-1)
    H = np.stack((-np.sin(phase), np.cos(phase), zero), axis=-1)
    ez = np.stack((zero, zero, np.ones_like(zero)), axis=-1)
    c = 1/np.sqrt(1+v*v)
    Tuu = -c[:, None]*H
    Tuv = (v*c**3)[:, None]*N
    Tvv = ((2*v*v-1)*c**5)[:, None]*H-(3*v*c**5)[:, None]*ez
    quadratic = (A*A)[:, None]*Tuu+(2*A*D)[:, None]*Tuv+(D*D)[:, None]*Tvv
    new.update(R1_angular_u=A, R1_angular_v=D, R1_Zxstar=Z,
               R1_linear_Tss_xstar=linear, R1_quadratic_Tss_xstar=quadratic)
    _require(all(np.all(np.isfinite(value)) for value in (Z, linear, quadratic)),
             "finite contracted true scalar-frame second direction required")
    primitive = {}
    for name, value in (("Zxstar", Z), ("linear_Tss_xstar", linear),
                        ("quadratic_Tss_xstar", quadratic)):
        def retain(answer, name=name):
            primitive[name] = answer[0]
            new["R1_Pi_"+name] = answer[0]
        answer, event = trace.run(
            "complete_theta_Pi_contracted_R1", lambda value=value:
                periodic_operator(value[None, ...], -1),
            retain, grid=label, component=name, axis=1, order=-1,
            input=array_binding(value))
        _require(answer.shape == (1, len(A), 3) and np.all(np.isfinite(answer)),
                 "finite contracted complete-angle primitive required")
        event["output"] = array_binding(answer)
    V = float(a)*primitive["Zxstar"]
    L = 2*float(a_s)*primitive["Zxstar"]+float(a)*primitive["linear_Tss_xstar"]
    Hxx = float(a)*primitive["quadratic_Tss_xstar"]
    fitted = np.einsum("icj,j->ic", new["V17"], xstar)
    new.update(R1_Vxstar=V, R1_Lxstar=L, R1_Hxxstar=Hxx,
               R1_contracted_Pi_minus_LS_column_contraction=V-fitted)
    return {
        "Vxstar": array_binding(V), "Lxstar": array_binding(L),
        "Hxxstar": array_binding(Hxx), "Zxstar": array_binding(Z),
        "maximum_absolute_contracted_Pi_vs_LS_contraction_difference":
            float(np.max(abs(V-fitted))),
        "floating_regrouping_is_recorded_not_claimed_bitwise_identical": True,
        "no_full_seventeen_by_seventeen_quadratic_tensor_formed": True,
        "fixed_height_and_new_nine_coefficients_not_varied": True}


def _r1_scale_grid(paid, new, target, a, alpha, metric_budget):
    """New finite R1 circle table, with actual G and no original alpha=0 replay."""
    old = paid["position_two_jets_without_X"]
    T = old["Xt"]/float(a)
    Z22 = old["Xtt"]/(float(a)**2)
    U = old["Xs"]+alpha*new["R1_Vxstar"]
    Xst = old["Xst"]+float(a)*alpha*new["R1_Zxstar"]
    Z12 = Xst/float(a)
    cross = np.cross(U, T)
    area2 = np.einsum("ij,ij->i", cross, cross)
    E = np.einsum("ij,ij->i", U, U)
    F = np.einsum("ij,ij->i", U, T)
    G = paid["actual_G"]
    mixed_numerator = np.einsum("ij,ij->i", cross, Z12)
    angular_numerator = np.einsum("ij,ij->i", cross, Z22)
    b = G*mixed_numerator-F*angular_numerator
    c = angular_numerator
    quartic = G*G*target*target*area2*area2-b*b-c*c*area2
    eps = metric_budget
    plus = eps*(1+eps-E)-F*F
    minus = eps*(E-1+eps)-F*F
    phi = .5*(np.sqrt((E-1)**2+4*F*F)+abs(E-1))
    finite = all(np.all(np.isfinite(value)) for value in (
        U, Xst, cross, area2, E, F, G, b, c, quartic, plus, minus, phi))
    positive = bool(finite and np.all(area2 > 0.) and np.all(G > 0.))
    metric_pass = bool(finite and np.all(plus >= 0.) and np.all(minus >= 0.)
                       and np.all(phi <= eps))
    quartic_pass = bool(finite and np.all(quartic >= 0.))
    arrays = {
        "E": E, "F": F, "actual_G": G, "normal_area_squared_Q": area2,
        "original_metric_phi": phi, "metric_plus_quadratic": plus,
        "metric_minus_quadratic": minus, "column_b_numerator": b,
        "column_c_numerator": c, "column_quartic": quartic}
    maximum_column = None
    if positive:
        B = b/(G*area2)
        C = c/(G*np.sqrt(area2))
        lower = np.sqrt(B*B+C*C)
        arrays.update(column_B_coordinate_formula=B, column_C_coordinate_formula=C,
                      invariant_column_lower_bound=lower)
        maximum_column = float(np.max(lower))
    summary = {
        "finite": bool(finite), "positive_Q_and_actual_G": positive,
        "metric_budget": eps, "metric_budget_source": "required paid-current-point argument",
        "maximum_original_metric_phi": float(np.max(phi)) if finite else None,
        "minimum_metric_plus_quadratic": float(np.min(plus)) if finite else None,
        "minimum_metric_minus_quadratic": float(np.min(minus)) if finite else None,
        "metric_quadratics_and_direct_phi_pass": metric_pass,
        "minimum_Q": float(np.min(area2)) if finite else None,
        "minimum_column_quartic": float(np.min(quartic)) if finite else None,
        "column_quartic_pass": quartic_pass,
        "maximum_invariant_column_lower_bound": maximum_column,
        "column_target": target,
        "comparison_tolerance": 0.,
        "finite_float_circle_table_not_interval_or_actual14": True,
        "passed": bool(positive and metric_pass and quartic_pass)}
    return {"summary": summary, "arrays": arrays,
            "U": U, "Xst": Xst, "cross": cross,
            "mixed_numerator": mixed_numerator,
            "angular_numerator": angular_numerator}


def _fixed_R1_increment(weights, x_exact):
    delta = [Q(0)]*168
    entries = []
    for j, x in enumerate(x_exact):
        for k, row in enumerate(_mode_physical_rows(j)):
            value = weights[k]*x
            delta[row] = value
            entries.append({
                "parameter_column": j, "independent168_row": row,
                "physical172_row": row, "full_spline_index": 9+k,
                "R1_weight_exact": str(weights[k]),
                "fixed_R1_coefficient_exact": str(x),
                "increment_exact": str(value)})
    return tuple(delta), tuple(delta[:154])+tuple(Q(0) for _ in range(18)), entries


def _conditional_grid(paid, new, scale, alpha, a, theta, target, label):
    original = paid["position_two_jets_without_X"]
    Xss = (original["Xss"]+alpha*new["R1_Lxstar"]
           +alpha*alpha*new["R1_Hxxstar"])
    jets = {key: original[key] for key in ("Xt", "Xtt")}
    jets.update(Xs=scale["U"], Xst=scale["Xst"], Xss=Xss)
    arrays = scale["arrays"]
    E, F, G = arrays["E"], arrays["F"], arrays["actual_G"]
    q = np.sqrt(arrays["normal_area_squared_Q"])
    numerator11 = np.einsum("ij,ij->i", scale["cross"], Xss)
    numerator12 = scale["mixed_numerator"]
    numerator22 = scale["angular_numerator"]
    I = np.stack((E, F, F, G), axis=-1).reshape(len(theta), 2, 2)
    II = np.stack((numerator11, numerator12, numerator12, numerator22),
                  axis=-1).reshape(len(theta), 2, 2)/q[:, None, None]
    shape = _normal_shape(jets, I, II, q, a)
    ell = np.einsum("ic,icj->ij", shape["normal"], new["V17"])/(
        shape["q_perp_squared"][:, None])
    _require(np.all(np.isfinite(ell)), "nonfinite conditional R2 response")
    lower = np.sqrt(shape["B"]**2+shape["C"]**2)
    current_norm = _operator_norm(shape["A"], shape["B"], shape["C"])
    at = int(np.argmax(lower))
    return {
        **shape, "ell": ell, "theta": theta,
        "position_two_jets_without_X": jets,
        "invariant_column_lower_bound": lower,
        "current_operator_norm": current_norm,
        "input_source": {
            "kind": "new-floating-R1-table-at-unaccepted-unrounded-state",
            "paid_current_ring_source": copy.deepcopy(paid["input_source"]),
            "alpha": alpha,
            "ordinary_geometry_or_accepted_point_construction": False},
        "ell_identity": {
            "schema": POLICY+"-conditional-R2-ell",
            "V17": array_binding(new["V17"]), "normal": array_binding(shape["normal"]),
            "q_perp_squared": array_binding(shape["q_perp_squared"]),
            "ell": array_binding(ell), "same_original_full_theta_columns": True},
        "summary": {
            "maximum_invariant_column_lower_bound": float(lower[at]),
            "lower_bound_attainer": {"theta_index": at, "theta": float(theta[at])},
            "maximum_current_ring_operator_norm": float(np.max(current_norm)),
            "maximum_absolute_G_minus_one": float(np.max(abs(shape["G_minus_one"]))),
            "target_exact": str(target),
            "floating_invariant_column_excludes_target": bool(np.any(lower > float(target))),
            "finite_float_inputs_not_interval_certificate": True,
            "this_is_not_an_accepted_R1_point": True}}


def _scientific_payload(value):
    """Lossless arrays/ordinary containers only, with no scientific recomputation."""
    if isinstance(value, np.ndarray):
        if value.dtype.kind in "iu":
            return {**array_binding(value), "values": value.tolist()}
        return _payload(value) if np.all(np.isfinite(value)) else _raw_numeric(value)
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _scientific_payload(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_scientific_payload(item) for item in value]
    if isinstance(value, (np.floating, float)):
        return float(value) if math.isfinite(float(value)) else (
            "NaN" if math.isnan(float(value)) else
            ("+Infinity" if float(value) > 0 else "-Infinity"))
    if isinstance(value, (np.integer, np.bool_)):
        return value.item()
    if value is None or isinstance(value, (str, int, bool)):
        return value
    raise TypeError("not a stored array/container payload: "+type(value).__name__)


class ReflectedR1Ray:
    def __init__(self, capture):
        self.capture = capture
        self.model = None
        self.solve_considered = False

    @property
    def status(self):
        return str(self.capture.get("status", "entered"))

    def summary(self):
        result = _public(self.capture)
        if "least_squares_raw_record" in result:
            raw = result["least_squares_raw_record"]
            result["least_squares_return_summary"] = {
                key: copy.deepcopy(raw.get(key)) for key in (
                    "status", "success", "message", "nit", "backend_elapsed_seconds")}
            result.pop("least_squares_raw_record")
        result.update(
            schema=POLICY+"-ray-summary",
            conditional_R2_model_created=self.model is not None,
            conditional_R2_model_binding_sha256=(
                None if self.model is None else self.model.binding_sha256),
            one_R2_solve_considered=bool(self.solve_considered))
        return result

    def full_record(self):
        arrays = self.capture.get("_arrays", {})
        ls = arrays.get("least_squares", {})
        ls_payload = {key: value for key, value in ls.items()
                      if key != "actual_backend_result_before_filter"}
        raw = self.capture.get("least_squares_raw_record")
        emitted = self.capture.get("least_squares_original_stdout_receipt")
        return {
            "schema": POLICY+"-full-reflected-R1-ray",
            "summary": self.summary(),
            "source": copy.deepcopy(self.capture.get("source")),
            "exact_radial_embedding": copy.deepcopy(
                self.capture.get("exact_radial_embedding")),
            "exact_projected_J1_domain": copy.deepcopy(
                self.capture.get("exact_projected_J1_domain")),
            "reflection_targets": _scientific_payload(arrays.get("reflection_targets", {})),
            "new_complete_frame_and_vector_tables":
                _scientific_payload(arrays.get("new_grids", {})),
            "original_weighted_LS_inputs_and_residuals": _scientific_payload(ls_payload),
            "least_squares_original_stdout_receipt": copy.deepcopy(emitted),
            "unemitted_original_least_squares_return":
                copy.deepcopy(raw) if emitted is None else None,
            "all_seven_fixed_R1_scale_records": copy.deepcopy(
                self.capture.get("alpha_records", [])),
            "completed_scale_original_arrays":
                _scientific_payload(arrays.get("alpha_gate_arrays", {})),
            "conditional_R2_model": None if self.model is None else self.model.full_record(),
            "paid_baseline_ring_arrays_not_duplicated": True,
            "no_future_ordinary_or_actual_gate_receipt_claimed": True}


def build_reflected_R1_ray(
        field, state168, radial, thetas, paid_ring_record, fixed_metric, cfg,
        lower172, upper172, source_receipt, wall, capture=None, *,
        metric_budget, charge_least_squares, emit=None,
        target_exact=TARGET_EXACT, maximum_h_exact=None):
    """One common bounded-LS ray, seven fixed tables, and at most one new R2 model.

    charge_least_squares(metadata) debits the caller's one-LS account immediately
    before the sole backend attempt.  No LP occurs in this function.  All phases,
    including input validation, arrays, LS import/failure and stdout, lie inside
    the caller's already-running clock.  The selected R1 point is only a model.
    """
    started = time.monotonic()
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty one-build capture required")
    sink.update(
        schema=POLICY+"-build-capture", status="entered",
        definition=definition(), events=[], component_counts={}, alpha_records=[],
        charged_new_least_squares_calls=0, least_squares_backend_entered=False,
        actual_ordinary_calls=0, actual_selected_J_calls=0, actual_gate_calls=0,
        old_instance_reopened=False, _arrays={}, _objects={})
    trace = _Trace(wall, sink)
    ray = ReflectedR1Ray(sink)
    try:
        _wall(wall, "reflected-R1.build.entry")
        _require(isinstance(cfg, dict) and isinstance(source_receipt, dict)
                 and bool(source_receipt), "original cfg and paid source receipt required")
        _require(callable(charge_least_squares), "one-LS external debit callback required")
        eps = float(metric_budget)
        _require(math.isfinite(eps) and eps > 0.,
                 "literal positive paid-current metric budget required")
        target = _q(target_exact)
        _require(target > 0 and math.isfinite(float(target)), "finite positive curvature target")
        low, high = _bounds(lower172, "lower"), _bounds(upper172, "upper")
        _require(all(lo <= hi for lo, hi in zip(low, high)), "ordered original172 bounds required")
        _require(all(Q.from_float(float(v)) == v for v in low+high),
                 "original actual172 box endpoints must remain exact binary64")
        q, r, th, ring_index, physical, metric, paid_grids, identity = _load_paid_ring(
            field, state168, radial, thetas, paid_ring_record, fixed_metric, cfg, low, high)
        _old, single = _context(field)
        sigma = Q.from_float(float(r[ring_index]))
        source = {
            "schema": POLICY+"-current-source", **identity,
            "configuration_sha256": digest(cfg),
            "source_receipt": copy.deepcopy(source_receipt),
            "paid_ring_model_binding_sha256": paid_ring_record["binding_sha256"],
            "paid_ring_MODEL_canonical_sha256": digest(paid_ring_record),
            "canonical_hash_is_not_the_original_JSON_plus_LF_receipt": True,
            "fixed_metric_binding_sha256": fixed_metric["binding_sha256"],
            "physical172_exact": [str(v) for v in physical],
            "lower172_exact": [str(v) for v in low], "upper172_exact": [str(v) for v in high],
            "metric_budget_binary64": eps,
            "metric_budget_exact_binary64": str(Q.from_float(eps)),
            "target_exact": str(target)}
        sink["source"] = copy.deepcopy(source)
        sink["curvature_input_route"] = {
            "kind": "complete-paid-ring-MODEL-array-reuse",
            "paid_model_binding_sha256": paid_ring_record["binding_sha256"],
            "new_original_alpha_zero_curvature_evaluations": 0,
            "new_ordinary_calls": 0, "new_selected_J_calls": 0}
        sink["_objects"].update(field=field, state168=q, radial=r, thetas=th,
                                paid_grids=paid_grids, fixed_metric=metric)
        def retain_basis(value):
            sink["exact_radial_embedding"] = copy.deepcopy(value[3])
        basis_result, _ = trace.run(
            "new_exact_R0_R1_R2_elimination",
            lambda: _exact_three_jet_basis(
                single, sigma, paid_ring_record["exact_radial_embedding"]),
            retain_basis, sigma_exact=str(sigma), paid_basis_reused=True)
        matrix, inverse, weights, radial_definition = basis_result
        def retain_box(value):
            sink["exact_projected_J1_domain"] = copy.deepcopy(value[1])
        box_result, _ = trace.run(
            "exact_projected_original172_R1_box",
            lambda: _project_original_box(matrix, inverse, low, high, physical),
            retain_box)
        intervals, _box_record = box_result
        E2, P2, entries2 = _embedding(weights[2])
        active = sorted({entry["physical172_row"] for entry in entries2})
        derived_h = 4*max(max(abs(low[j]-physical[j]), abs(high[j]-physical[j]))
                         for j in active)
        hmax = derived_h if maximum_h_exact is None else _q(maximum_h_exact)
        _require(hmax >= 0 and math.isfinite(float(hmax)), "finite nonnegative maximum h")
        maximum = {
            "requested_maximum_h_exact": None if maximum_h_exact is None else str(hmax),
            "effective_maximum_h_exact": str(hmax),
            "box_sufficient_maximum_h_exact": str(derived_h),
            "source": "original172-box-derived" if maximum_h_exact is None else "explicit-caller-cap",
            "reference_small_h_exact": REFERENCE_SMALL_H_EXACT,
            "reference_small_h_is_not_an_implicit_constraint": maximum_h_exact is None,
            "active_physical_indices": active, "all_172_original_box_constraints_retained": True,
            "norm_applies_to_complete_R1_plus_R2_increment": True}
        sink["maximum_h"] = copy.deepcopy(maximum)
        a, a_s = float(metric["a"][ring_index]), float(metric["a_s"][ring_index])
        targets = sink["_arrays"].setdefault("reflection_targets", {})
        for label in LABELS:
            def retain_target(value, label=label):
                targets[label] = value
                sink.setdefault("reflection_target_summary", {})[label] = {
                    "status": value["status"], "valid": value["valid"],
                    "mean": None if not value["valid"] else value["mean"].tolist(),
                    "zero_or_nonfinite_indices": value.get("zero_or_nonfinite_indices", []),
                    "mean_not_silently_removed": True}
            trace.run(
                "general_G_reflection_target",
                lambda label=label: _reflection_target(paid_grids[label], a),
                retain_target, grid=label, original_ring_arrays_reused=True)
        if not all(targets[label]["valid"] for label in LABELS):
            sink.update(status="reflection-degenerate-no-LS-no-LP",
                        build_seconds_before_return=float(time.monotonic()-started))
            _wall(wall, "reflected-R1.build.degenerate.complete")
            return ray
        if not any(np.any(targets[label]["target"] != 0.) for label in LABELS):
            sink.update(status="reflection-target-zero-no-LS-no-LP",
                        build_seconds_before_return=float(time.monotonic()-started))
            _wall(wall, "reflected-R1.build.zero-target.complete")
            return ray
        new_grids = sink["_arrays"].setdefault("new_grids", {})
        for label in LABELS:
            _build_frame_columns(field, q, float(r[ring_index]), th[label],
                                 a, label, trace, sink)
        ls_result = _least_squares_once(
            intervals, new_grids, targets, charge_least_squares, wall, emit, sink)
        if ls_result is None:
            sink.update(status="no-qualified-nonzero-common-R1-ray",
                        build_seconds_before_return=float(time.monotonic()-started))
            _wall(wall, "reflected-R1.build.no-ray.complete")
            return ray
        xstar, xstar_exact = ls_result
        for label in LABELS:
            def retain_contract(value, label=label):
                sink.setdefault("contracted_R1_vector_summary", {})[label] = value
            trace.run(
                "one_contracted_R1_second_direction_table",
                lambda label=label: _contract_R1_ray(
                    new_grids[label], xstar, a, a_s, label, trace),
                retain_contract, grid=label, no_full_quadratic_parameter_tensor=True)

        first = None
        for ordinal, alpha_literal in enumerate(ALPHA_EXACT, 1):
            alpha_exact = Q(alpha_literal)
            alpha = float(alpha_exact)
            x_exact = tuple(alpha_exact*v for v in xstar_exact)
            scales = {}
            for label in LABELS:
                def retain_scale(value, label=label, alpha_literal=alpha_literal):
                    scales[label] = value
                    sink["_arrays"].setdefault("alpha_gate_arrays", {}).setdefault(
                        alpha_literal, {})[label] = value["arrays"]
                trace.run(
                    "fixed_R1_metric_and_column_query",
                    lambda label=label: _r1_scale_grid(
                        paid_grids[label], new_grids[label], float(target), a, alpha, eps),
                    retain_scale, grid=label, fixed_alpha_exact=alpha_literal, ordinal=ordinal)
            remaining_capture = {}
            def retain_remaining(value):
                remaining_capture["record"] = value[1]
                sink.setdefault("completed_remaining_R2_box_records", {})[
                    alpha_literal] = copy.deepcopy(value[1])
            remaining_result, _ = trace.run(
                "exact_remaining_R2_original_box",
                lambda: _remaining_R2_intervals(
                    x_exact, inverse, low, high, physical, hmax),
                retain_remaining, fixed_alpha_exact=alpha_literal, ordinal=ordinal)
            remaining, box_record = remaining_result
            passed = bool(any(x_exact) and box_record["all_modes_nonempty"]
                          and all(scales[label]["summary"]["passed"] for label in LABELS))
            record = {
                "ordinal": ordinal, "alpha_exact": alpha_literal, "alpha_binary64": alpha,
                "R1_common_coefficients17_exact": [str(v) for v in x_exact],
                "nonzero": any(x_exact), "grids": {
                    label: copy.deepcopy(scales[label]["summary"]) for label in LABELS},
                "remaining_original_box_and_norm_R2": box_record,
                "qualified_for_one_new_conditional_R2_model": passed,
                "first_qualified_scale_in_declared_order": bool(passed and first is None),
                "not_an_actual_trial_or_accepted_point": True}
            sink["alpha_records"].append(record)
            if passed and first is None:
                first = (alpha_exact, x_exact, scales, remaining, record)
            _wall(wall, "reflected-R1.fixed-scale."+alpha_literal+".complete")
        sink["all_seven_fixed_scales_actually_recorded"] = (
            len(sink["alpha_records"]) == len(ALPHA_EXACT))
        if first is None:
            sink.update(status="seven-fixed-R1-scales-have-no-qualified-fiber",
                        build_seconds_before_return=float(time.monotonic()-started))
            _wall(wall, "reflected-R1.build.no-fiber.complete")
            return ray

        alpha_exact, x_exact, scales, remaining, selected_record = first
        fixed_delta, fixed_physical, fixed_entries = _fixed_R1_increment(weights[1], x_exact)
        grids = {}
        for label in LABELS:
            def retain_conditional(value, label=label):
                grids[label] = value
                sink["_arrays"].setdefault("conditional_R2_grids", {})[label] = value
            trace.run(
                "one_conditional_R2_circle_model",
                lambda label=label: _conditional_grid(
                    paid_grids[label], new_grids[label], scales[label], float(alpha_exact),
                    a, th[label], target, label),
                retain_conditional, grid=label, selected_alpha_exact=str(alpha_exact),
                original_point_still_unmodified=True)
        model = ConditionalR1Ring17Model(
            field, q, r, th, ring_index, cfg, source,
            radial_definition, weights[2], E2, P2, entries2, physical,
            low, high, target, hmax, maximum, grids, sink,
            fixed_delta=fixed_delta, fixed_physical=fixed_physical,
            fixed_entries=fixed_entries, x_exact=x_exact,
            selected_record=selected_record, remaining=remaining)
        ray.model = model
        sink.update(
            status="one-new-R1-fiber-ready-for-at-most-one-R2-LP",
            selected_alpha_exact=str(alpha_exact),
            selected_R1_coefficients17_exact=[str(v) for v in x_exact],
            conditional_model_binding_sha256=model.binding_sha256,
            all_seven_fixed_scales_actually_recorded=len(sink["alpha_records"]) == len(ALPHA_EXACT),
            build_seconds_before_return=float(time.monotonic()-started))
        _wall(wall, "reflected-R1.build.complete")
        return ray
    except Exception as error:
        sink.update(status="raised", error=_error(error),
                    build_seconds_before_raise=float(time.monotonic()-started),
                    completed_work_not_retried=True)
        raise


class ConditionalR1Ring17Model(Ring17Model):
    """A new R2 LP at a fixed unaccepted R1 state, based at the original q58."""
    def __init__(self, *args, fixed_delta, fixed_physical, fixed_entries,
                 x_exact, selected_record, remaining, **kwargs):
        super().__init__(*args, **kwargs)
        self.fixed_independent168_delta = tuple(fixed_delta)
        self.fixed_physical172_delta = tuple(fixed_physical)
        self.fixed_R1_entries = copy.deepcopy(fixed_entries)
        self.fixed_R1_coefficients17 = tuple(x_exact)
        self.selected_R1_record = copy.deepcopy(selected_record)
        self.remaining_R2_exact = tuple(tuple(v) for v in remaining)
        self.binding.update(
            schema=POLICY+"-conditional-R2-model-binding",
            definition=definition(), source_hashes=implementation_hashes(),
            fixed_R1_independent168_increment_exact=[str(v) for v in fixed_delta],
            fixed_R1_physical172_increment_exact=[str(v) for v in fixed_physical],
            fixed_R1_embedding_entries=copy.deepcopy(fixed_entries),
            fixed_R1_coefficients17_exact=[str(v) for v in x_exact],
            selected_R1_record_sha256=digest(selected_record),
            remaining_R2_exact=[[str(v) for v in pair] for pair in remaining],
            original_current_point_remains_base=True,
            combined_R1_R2_norm_and_single_rounding=True)
        self.binding_sha256 = digest(self.binding)

    def assert_context(self):
        super().assert_context()
        _require(
            self.binding["fixed_R1_independent168_increment_exact"]
            == [str(v) for v in self.fixed_independent168_delta]
            and self.binding["fixed_R1_physical172_increment_exact"]
            == [str(v) for v in self.fixed_physical172_delta]
            and self.binding["fixed_R1_embedding_entries"] == self.fixed_R1_entries
            and self.binding["fixed_R1_coefficients17_exact"]
            == [str(v) for v in self.fixed_R1_coefficients17]
            and self.binding["selected_R1_record_sha256"] == digest(self.selected_R1_record),
            "the selected fixed R1 state or its original-point binding changed")

    def summary(self):
        record = super().summary()
        record.update(
            schema=POLICY+"-conditional-R2-model-summary",
            selected_alpha_exact=self.selected_R1_record["alpha_exact"],
            fixed_R1_coefficients17_exact=[str(v) for v in self.fixed_R1_coefficients17],
            selected_R1_metric_and_column_record=copy.deepcopy(self.selected_R1_record),
            original_state168_is_the_only_accepted_base=True,
            no_q1_rounding_or_q1_actual_acceptance=True,
            objective="min h of complete exact R1+R2 original172 increment")
        return record

    def assemble(self):
        self.assert_context()
        if self._assembled is not None:
            return self._assembled
        rows, rhs, tags = [], [], []
        def add(row, bound, tag):
            row = np.asarray(row, dtype=np.float64)
            _require(row.shape == (18,) and np.all(np.isfinite(row))
                     and math.isfinite(float(bound)), "finite original-unit conditional LP row")
            rows.append(row.copy())
            rhs.append(float(bound))
            tags.append(tag)
        K = float(self.target_exact)
        for label in LABELS:
            grid = self.grids[label]
            for j, theta in enumerate(grid["theta"]):
                A, B, C, ell = (grid[name][j] for name in ("A", "B", "C", "ell"))
                for component, coefficient, bound in (
                    ("plus_trace", -ell, 2*K+A+C),
                    ("plus_determinant", -(K+C)*ell, (K+C)*(K+A)-B*B),
                    ("minus_trace", ell, 2*K-A-C),
                    ("minus_determinant", (K-C)*ell, (K-C)*(K-A)-B*B)):
                    add(np.r_[coefficient, 0.], bound, {
                        "kind": "ring_PSD", "grid": label, "theta_index": j,
                        "theta": float(theta), "component": component,
                        "selected_R1_alpha_exact": self.selected_R1_record["alpha_exact"]})
        for j in range(172):
            p = self.P[j]
            fixed = self.fixed_physical172_delta[j]
            add(np.r_[p, 0.], self.upper172[j]-self.base_physical172[j]-fixed,
                {"kind": "physical172_box", "physical_index": j, "side": "upper"})
            add(np.r_[-p, 0.], self.base_physical172[j]+fixed-self.lower172[j],
                {"kind": "physical172_box", "physical_index": j, "side": "lower"})
            if np.any(p != 0.) or fixed != 0:
                add(np.r_[4*p, -1.], -4*fixed,
                    {"kind": "physical_step_norm", "physical_index": j, "side": "plus"})
                add(np.r_[-4*p, -1.], 4*fixed,
                    {"kind": "physical_step_norm", "physical_index": j, "side": "minus"})
        add(np.r_[np.zeros(17), -1.], 0., {"kind": "h_lower"})
        add(np.r_[np.zeros(17), 1.], self.maximum_h_exact, {"kind": "h_upper"})
        A = np.stack(rows)
        b = np.asarray(rhs, dtype=np.float64)
        c = np.r_[np.zeros(17), 1.]
        for value in (A, b, c):
            value.setflags(write=False)
        metadata = {
            "schema": POLICY+"-conditional-R2-assembly",
            "rows": len(b), "columns": 18, "A": array_binding(A),
            "b": array_binding(b), "c": array_binding(c),
            "row_tags_sha256": digest(tags),
            "row_counts": {kind: sum(tag["kind"] == kind for tag in tags)
                           for kind in sorted({tag["kind"] for tag in tags})},
            "selected_R1_alpha_exact": self.selected_R1_record["alpha_exact"],
            "fixed_R1_physical_increment_exact": [str(v) for v in self.fixed_physical172_delta],
            "box_RHS_uses_original_base_plus_exact_fixed_R1": True,
            "norm_RHS_includes_exact_fixed_R1_shift": True,
            "four_PSD_rows_keep_K_plus_or_minus_C_zero_cases": True,
            "all_18_variables_explicitly_free_before_rows": True,
            "floating_matrix_not_a_rational_feasibility_certificate": True}
        self._assembled = (A, b, c, tags, metadata)
        return self._assembled

    def candidate_from_raw(self, x18):
        self.assert_context()
        raw = _array(x18, (18,), "actual conditional R2 raw18")
        y = tuple(Q.from_float(float(v)) for v in raw[:17])
        base = tuple(Q.from_float(float(v)) for v in self.state168)
        delta = list(self.fixed_independent168_delta)
        R2_delta = [Q(0)]*168
        for entry in self.embedding_entries:
            row = entry["independent168_row"]
            change = Q(entry["weight_exact"])*y[entry["parameter_column"]]
            R2_delta[row] += change
            delta[row] += change
        ideal = tuple(q+d for q, d in zip(base, delta))
        physical_delta = tuple(delta[:154])+tuple(Q(0) for _ in range(18))
        ideal_physical = tuple(q+d for q, d in zip(self.base_physical172, physical_delta))
        ideal_h = 4*max(map(abs, physical_delta))
        candidate = self.state168.copy()
        touched = sorted(
            {entry["independent168_row"] for entry in self.embedding_entries}
            | {entry["independent168_row"] for entry in self.fixed_R1_entries})
        for row in touched:
            candidate[row] = float(ideal[row])
        _require(np.all(np.isfinite(candidate)), "combined exact increment overflowed binary64")
        candidate = _array(self.field.validate_state(candidate), (168,), "rounded combined168")
        actual_physical = tuple(self.field.full_coefficients(candidate, exact=True))
        actual_delta = tuple(q-b for q, b in zip(actual_physical, self.base_physical172))
        actual_h = 4*max(map(abs, actual_delta))
        rounded_exact = tuple(Q.from_float(float(v)) for v in candidate)
        rounding = tuple(q-b for q, b in zip(rounded_exact, ideal))
        bad_box = [j for j, (lo, value, hi) in enumerate(
            zip(self.lower172, actual_physical, self.upper172)) if value < lo or value > hi]
        ideal_bad_box = [j for j, (lo, value, hi) in enumerate(
            zip(self.lower172, ideal_physical, self.upper172)) if value < lo or value > hi]
        actual_box = self.field.exact_full_box_decision(
            candidate, np.asarray(list(map(float, self.lower172))),
            np.asarray(list(map(float, self.upper172))))
        _require(actual_box["exact_full_box_pass"] == (not bad_box),
                 "canonical original172 box and actual field box disagree")
        actual_h_pass = actual_h <= self.maximum_h_exact
        record = {
            "schema": POLICY+"-combined-exact-R1-R2-and-once-rounded-candidate",
            "model_binding_sha256": self.binding_sha256,
            "raw18": _vector(raw),
            "xi17_exact_binary64": [str(v) for v in y],
            "R2_y17_exact_binary64": [str(v) for v in y],
            "selected_R1_alpha_exact": self.selected_R1_record["alpha_exact"],
            "fixed_R1_coefficients17_exact": [str(v) for v in self.fixed_R1_coefficients17],
            "fixed_R1_independent168_increment_exact":
                [str(v) for v in self.fixed_independent168_delta],
            "R2_independent168_increment_exact": [str(v) for v in R2_delta],
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
            "rounded_physical172_binary64": _vector(np.asarray(list(map(float, actual_physical)))),
            "rounded_exact_physical172_increment": [str(v) for v in actual_delta],
            "rounded_exact_h": str(actual_h), "rounded_exact_box_decision": actual_box,
            "rounded_exact_h_bound_pass": bool(actual_h_pass),
            "rounded_exact_h_at_most_original_small_1_over_128":
                bool(actual_h <= Q(REFERENCE_SMALL_H_EXACT)),
            "independent_rounding_error_exact": [str(v) for v in rounding],
            "physical_rounding_error_exact": [
                str(q-b) for q, b in zip(actual_physical, ideal_physical)],
            "maximum_absolute_independent_rounding_error_exact": str(max(map(abs, rounding))),
            "rounding": "each touched exact(q58)+exact(R1*x)+exact(R2*y) coordinate rounded once",
            "no_intermediate_q1_binary64_point_constructed": True,
            "untouched168_coordinates_keep_original_literal_binary64": True,
            "exact_ring_identity_applies_to_unrounded_rational_embedding_only": True,
            "rounded_candidate_claimed_exactly_ring_metric_neutral": False,
            "projected_R1_was_never_claimed_exactly_isometric": True,
            "actual14_or_fullbody_feasibility_claimed": False,
            "original_actual_box_and_new_explicit_h_pass":
                bool(not bad_box and actual_h_pass),
            "candidate_physical_identity_sha256": digest(self.field.identity(candidate))}
        return candidate, record

    def full_record(self):
        """Save only the new conditional model, not another paid baseline payload."""
        self.assert_context()
        return {
            "schema": POLICY+"-full-conditional-R2-model",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "summary": self.summary(),
            "original_base_state168": _vector(self.state168),
            "original_base_physical172_exact": [str(v) for v in self.base_physical172],
            "exact_R0_R1_R2_definition": copy.deepcopy(self.radial_definition),
            "fixed_R1_embedding_entries": copy.deepcopy(self.fixed_R1_entries),
            "R2_embedding_entries": copy.deepcopy(self.embedding_entries),
            "remaining_box_R2_intervals_exact": [
                [str(v) for v in pair] for pair in self.remaining_R2_exact],
            "grids": {
                label: {
                    "arrays": {name: _payload(self.grids[label][name]) for name in (
                        "A", "B", "C", "ell", "normal", "actual_I", "actual_II", "actual_G",
                        "q_perp_squared", "actual_normal_area", "G_minus_one",
                        "q_perp2_minus_original_cross_q2_over_G", "theta",
                        "current_operator_norm", "invariant_column_lower_bound")},
                    "position_two_jets_without_X": {
                        name: _payload(value) for name, value in
                        self.grids[label]["position_two_jets_without_X"].items()},
                    "input_source": copy.deepcopy(self.grids[label]["input_source"]),
                    "ell_identity": copy.deepcopy(self.grids[label]["ell_identity"])}
                for label in LABELS},
            "assembly_metadata": None if self._assembled is None
                else copy.deepcopy(self._assembled[-1]),
            "build_component_counts": copy.deepcopy(self.build_capture.get("component_counts", {})),
            "unaccepted_R1_point_not_saved_as_an_actual_checkpoint": True,
            "new_vector_tables_and_LS_input_are_in_the_parent_ray_record": True}


def _conditional_solver_report(report):
    result = copy.deepcopy(report)
    result["schema"] = POLICY+"-one-conditional-R2-solve-report"
    if "unrounded_R2_ring_model_prediction" in result:
        result["unrounded_combined_R1_R2_ring_model_prediction"] = result.pop(
            "unrounded_R2_ring_model_prediction")
    if isinstance(result.get("backend_result"), dict):
        result["backend_result"]["schema"] = POLICY+"-original-conditional-R2-backend-return"
    result.update(
        base_is_original_current_point_not_q1=True,
        physical_norm_and_box_include_fixed_R1_offset=True,
        inherited_helper_is_a_new_model_solve_not_an_old_instance_restart=True)
    return result


def solve_reflected_R1_once(
        ray, *, charge_call, wall, time_limit_seconds, emit=None, capture=None):
    """At most one new LP on ray.model; no model means an explicit zero-LP result."""
    started = time.monotonic()
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty reflected-R1 solve capture required")
    sink.update(schema=POLICY+"-one-solve-capture", status="entered",
                _arrays={}, new_LP_account_debits_returned=0)
    try:
        _wall(wall, "reflected-R1.solve.entry")
        _require(isinstance(ray, ReflectedR1Ray), "actual ReflectedR1Ray object required")
        _require(not ray.solve_considered, "this ray has already been considered for its one LP")
        _require(callable(charge_call), "external one-new-LP debit callback required")
        _require(emit is None or callable(emit), "stdout emitter must be callable")
        ray.solve_considered = True
        sink["ray_status"] = ray.status
        if ray.model is None:
            sink.update(status="no-qualified-R1-fiber-zero-LP",
                        elapsed_seconds_before_return=float(time.monotonic()-started))
            _wall(wall, "reflected-R1.solve.no-model.complete")
            return {"status": sink["status"], "qualified": False,
                    "candidate168": None, "candidate_record": None, "report": _public(sink)}
        model = ray.model
        model.assert_context()
        sink["model_binding_sha256"] = model.binding_sha256
        sink["selected_R1_alpha_exact"] = model.selected_R1_record["alpha_exact"]
        inner = {}
        sink["_arrays"]["conditional_R2_solver_capture"] = inner
        def charge(metadata):
            new_metadata = copy.deepcopy(metadata)
            new_metadata.update(
                schema=POLICY+"-new-R2-LP-charge",
                kind="one-new-selected-R1-fiber-original-box-R2-LP",
                selected_R1_alpha_exact=model.selected_R1_record["alpha_exact"],
                complete_combined_R1_R2_physical_norm=True,
                original_state_remains_base=True)
            receipt = charge_call(new_metadata)
            sink["new_LP_account_debits_returned"] += 1
            return receipt
        def relay(suffix, record):
            delivered = copy.deepcopy(record)
            if suffix == "FINITE_RESULT":
                delivered.update(
                    schema=POLICY+"-original-conditional-R2-backend-return",
                    selected_R1_alpha_exact=model.selected_R1_record["alpha_exact"],
                    complete_combined_R1_R2_physical_norm=True)
            return emit(suffix, delivered)
        result = solve_ring17_once(
            model, charge_call=charge, wall=wall, time_limit_seconds=time_limit_seconds,
            emit=None if emit is None else relay, capture=inner)
        report = _conditional_solver_report(result["report"])
        sink.update(status=result["status"], conditional_R2_solver_report=report,
                    elapsed_seconds_before_return=float(time.monotonic()-started))
        _wall(wall, "reflected-R1.solve.complete")
        return {
            "status": result["status"], "qualified": bool(result["qualified"]),
            "candidate168": result["candidate168"],
            "candidate_record": copy.deepcopy(result["candidate_record"]),
            "report": _public(sink)}
    except Exception as error:
        sink.update(status="raised", error=_error(error),
                    elapsed_seconds_before_raise=float(time.monotonic()-started),
                    no_new_solver_retry=True)
        raise


def reflected_R1_capture_record(capture, *, include_arrays=False):
    """Serialize actual retained partial work; no fake empty scientific buffers."""
    _require(isinstance(capture, dict), "actual reflected-R1 capture dictionary required")
    def convert(value):
        if isinstance(value, np.ndarray):
            if value.dtype.kind in "fiu":
                return _payload(value) if np.all(np.isfinite(value)) else _raw_numeric(value)
            return {"unserialized_array_dtype": str(value.dtype), "shape": list(value.shape),
                    "values_saved": False}
        if isinstance(value, dict):
            return {str(key): convert(item) for key, item in value.items()
                    if key != "_objects" and (include_arrays or key != "_arrays")}
        if isinstance(value, (tuple, list)):
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
        return {"runtime_object_type_not_serialized":
                    type(value).__module__+"."+type(value).__name__, "values_saved": False}
    return {
        "schema": POLICY+"-capture-output", "raw_arrays_included": bool(include_arrays),
        "actual_capture": convert(capture),
        "only_actually_returned_values_no_zero_scientific_surrogates": True,
        "output_time_belongs_to_external_current_scientific_clock": True}

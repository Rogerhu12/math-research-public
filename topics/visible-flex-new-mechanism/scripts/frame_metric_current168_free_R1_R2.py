#!/usr/bin/env python3
"""One new free-R1/R2 minimax ring model using the paid actual58 tables.

Import-only.  The caller owns the entire scientific clock and debits.  This
module does not rerun ordinary geometry, a scalar frame, an old geometric J,
the reflected-ray least-squares fit, or any closed fixed-alpha/ray problem.
The only new angular primitives are the 17 missing linear and 125 quadratic
columns, in one complete batch per original angular grid.
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
from frame_metric_current168_ring17 import (
    POLICY as PAID_RING_POLICY, LABELS, JETS, LP_ROW_TOLERANCE,
    REFERENCE_SMALL_H_EXACT, _require, _error, _wall, _array, _same, _q,
    _vector, _payload, _bounds, _normal_shape, _operator_norm, _raw_numeric)
from frame_metric_current168_reflected_R1_ray import (
    POLICY as PAID_RAY_POLICY, _decode_payload, _mode_physical_rows,
    _raw_all_fields)
from frame_metric_current168_joint_alpha_R2 import _numeric_record


POLICY = "true58-free-R1-R2-original-box-curvature-minimax-v1"
TARGET_EXACT = "1000/61"
INITIAL_K_EXACT = "58"
NPHYSICAL_FREE = 34
MODES = 17
VARIABLES = 36
K_COLUMN = 34
H_COLUMN = 35
SLSQP_OPTIONS = {"maxiter": 200, "ftol": 1.e-9, "disp": False}
MAX_EVALUATIONS = 600
SOLVER_SECONDS = 180.
NORM_WEIGHT = 1.e-6
GRID_CONSTRAINTS = (
    "metric_plus", "metric_minus", "positive_Q_lower_bound",
    "spectral_trace_square", "spectral_determinant_sign",
    "spectral_determinant_square")


class FreeR1R2Limit(RuntimeError):
    """A real new-session limit, without a substitute backend result."""


def definition():
    return {
        "schema": POLICY,
        "problem": "34 free original R1/R2 controls plus common K and physical h",
        "fixed_R0": "zero; original radial value and all angular jets remain fixed on the ring",
        "physical_variables": "x_R1[17],y_R2[17],K,h",
        "backend_variables": "z[34],K,h; each z is four times one free physical coefficient increment",
        "R0_elimination": "largest-absolute nonzero literal row0 coefficient; first index on ties",
        "physical_decode": "two free increments z/4; third from the exact original R0 plane",
        "exact_and_float_decode": "callback matrices are rounded once; final rational decode is separate",
        "objective": "K+1e-6*h",
        "target_lower_exact_default": TARGET_EXACT,
        "backend_K_lower": "least binary64 not below the exact lower target; recorded separately",
        "K_upper_and_initial_exact": INITIAL_K_EXACT,
        "initial_point": "original actual58: z=0,K=58,h=0; one seed, no restart",
        "physical_norm": "h >= 4*max absolute increment over all original172 physical coefficients",
        "maximum_h": "the paid original-box sufficient bound; no implicit 1/128",
        "metric_budget": "literal current58 global eta receipt, not the .26 completion target",
        "current_frame": "read paid scalar_fields/scalar_frame from the complete R1 MODEL",
        "paid_columns": "read original_u9/v8,tangent_columns17,primitive_tangent_columns17,V17",
        "new_linear_columns": 17,
        "new_quadratic_columns": {"uu": 45, "uv": 44, "vv": 36, "total": 125},
        "quadratic_basis_is_a_generating_list_not_a_rank_claim": True,
        "new_primitive_batch": "one complete theta batch of 142 columns on each original grid",
        "old_V17_primitive_recomputed": False,
        "second_partials": "original target_frame Tuu/Tuv/Tvv formulas at paid u/v/theta",
        "ring_jets": "U=U0+Vx; Z12=Z12_0+Zx; Z11=Z11_0+Lx+H(x,x)+Vy",
        "floating_primitive_regrouping_not_bitwise_old_ray_identity": True,
        "Q": "|(U0+Vx) cross T|^2, never a Schur quantity renamed without G",
        "actual_G": "paid G kept literally; no replacement by one",
        "spectrum": "4*K^2*G^2*Q^3-t^2>=0, R>=0, R^2-K^2*G^2*Q*t^2>=0",
        "spectrum_numerators": "t=a+cQ; R=K^2*G^2*Q^2+ac-b^2",
        "row_scales": "fixed at the first counted full evaluation: max(1,abs(value),max abs Jrow)",
        "backend": "one scipy.optimize.minimize(method='SLSQP')",
        "backend_options": copy.deepcopy(SLSQP_OPTIONS),
        "full_evaluation_cap": MAX_EVALUATIONS,
        "solver_seconds_cap": SOLVER_SECONDS,
        "original_row_tolerance": LP_ROW_TOLERANCE,
        "original_unit_filter": "same returned parameters, original unsquared four PSD rows and metric",
        "candidate": "exact original58 plus exact decoded physical increments, once rounded",
        "K_above_target_may_be_a_finite_candidate_but_is_not_reach": True,
        "whole_body_prediction_and_original14_acceptance_are_external": True,
        "ordinary_calls": 0, "metric_calls": 0, "new_frame_calls": 0,
        "geometric_J_calls": 0, "old_optimization_calls": 0,
        "global_infeasibility_or_optimality_certificate": False,
        "API_source": "https://docs.scipy.org/doc/scipy-1.17.0/reference/optimize.minimize-slsqp.html"}


def implementation_hashes():
    names = (
        Path(__file__).name, "frame_metric_current168_joint_alpha_R2.py",
        "frame_metric_current168_reflected_R1_ray.py", "frame_metric_current168_ring17.py",
        "frame_complete_body_extension168.py", "frame_complete_body_extension168_joint_selected.py",
        "frame_collar_bvp.py", "frame_collar_enriched.py", "frame_height_null_coordinates.py")
    root = Path(__file__).parent
    return {name: hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names}


def _public(value):
    return {key: copy.deepcopy(item) for key, item in value.items()
            if not str(key).startswith("_")}


def _dot(left, right):
    return np.einsum("ic,ic->i", left, right)


def _dot_columns(vector, columns):
    return np.einsum("ic,icj->ij", vector, columns)


def _freeze(arrays):
    for value in arrays.values():
        if isinstance(value, np.ndarray):
            _require(np.all(np.isfinite(value)), "finite model array required")
            value.setflags(write=False)


def _restore_paid(field, state168, ring, ray, cfg, lower, upper, receipt, wall, sink):
    _wall(wall, "free-R1R2.source.entry")
    _context(field)
    q = _array(field.validate_state(state168), (168,), "actual58 state")
    _require(isinstance(cfg, dict) and isinstance(receipt, dict) and receipt,
             "original cfg and authenticated source receipts required")
    low, high = _bounds(lower, "lower"), _bounds(upper, "upper")
    _require(all(lo <= hi for lo, hi in zip(low, high)),
             "ordered original172 box required")
    _require(all(Q.from_float(float(v)) == v for v in low+high),
             "literal original binary64 box endpoints required")
    physical = tuple(field.full_coefficients(q, exact=True))
    _require(len(physical) == 172 and all(
        lo <= v <= hi for lo, v, hi in zip(low, physical, high)),
        "actual58 must retain the exact original172 box")
    _require(isinstance(ring, dict) and ring.get("schema") == PAID_RING_POLICY+"-full-ring-model",
             "the full paid original ring MODEL is required")
    rb = ring.get("binding")
    _require(isinstance(rb, dict) and ring.get("binding_sha256") == digest(rb),
             "original ring binding changed")
    source = rb.get("source")
    _require(isinstance(source, dict), "paid ring source missing")
    expected = {
        "field_definition_sha256": field.definition_sha256,
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "physical_state_sha256": digest(field.identity(q)),
        "state168": array_binding(q), "configuration_sha256": digest(cfg),
        "physical172_exact": [str(v) for v in physical],
        "lower172_exact": [str(v) for v in low],
        "upper172_exact": [str(v) for v in high]}
    _require(all(source.get(key) == value for key, value in expected.items())
             and source.get("ring_radial_index") == 141,
             "paid ring current state, grid, field, cfg or box differs")
    _require(_same(_decode_payload(ring.get("state168"), (168,), "ring/state168"), q)
             and ring.get("physical172_exact") == expected["physical172_exact"],
             "literal paid ring state differs")
    _require(isinstance(ray, dict)
             and ray.get("schema") == PAID_RAY_POLICY+"-full-reflected-R1-ray",
             "complete reflected-R1 MODEL required")
    rs = ray.get("source")
    _require(isinstance(rs, dict)
             and rs.get("paid_ring_model_binding_sha256") == ring["binding_sha256"]
             and rs.get("paid_ring_MODEL_canonical_sha256") == digest(ring)
             and all(rs.get(key) == value for key, value in expected.items())
             and all(rs.get(key) == source.get(key) for key in (
                 "ring_radial_index", "sigma_binary64_exact", "radial", "theta",
                 "fixed_metric_binding_sha256")),
             "the two paid models do not share the original actual58 definition")
    metric = receipt.get("paid_ring_metric")
    _require(isinstance(metric, dict) and isinstance(metric.get("source"), dict)
             and metric["source"], "authenticated original a and a_s receipt required")
    metric_values = {}
    for key in ("a", "a_s"):
        v = metric.get(key+"_binary64")
        _require(not isinstance(v, (bool, np.bool_))
                 and isinstance(v, (int, float, np.integer, np.floating))
                 and math.isfinite(float(v)), "literal finite paid metric "+key+" required")
        metric_values[key] = float(v)
        if key+"_exact_binary64" in metric:
            _require(Q(metric[key+"_exact_binary64"]) == Q.from_float(float(v)),
                     "paid metric exact and binary64 differ: "+key)
    _require(metric_values["a"] > 0, "positive original a required")
    if "radial_index" in metric:
        _require(metric["radial_index"] == 141, "paid metric radial index differs")
    exact = ray.get("exact_radial_embedding")
    _require(isinstance(exact, dict)
             and exact.get("original_paid_R2_definition") == ring.get("exact_radial_embedding")
             and exact.get("sigma_exact") == source["sigma_binary64_exact"],
             "literal paid complete three-jet embedding differs")
    matrix = tuple(tuple(Q(v) for v in row) for row in exact["basis_jet_matrix_exact"])
    inverse = tuple(tuple(Q(v) for v in row) for row in
                    exact["inverse_by_spline_row_and_radial_jet_column"])
    _require(len(matrix) == len(inverse) == 3
             and all(len(row) == 3 for row in matrix+inverse)
             and tuple(row[1] for row in inverse) == tuple(map(Q, exact["R1_weights_exact"]))
             and tuple(row[2] for row in inverse) == tuple(map(Q, exact["R2_weights_exact"])),
             "paid three-jet columns changed")
    # The paid inverse identity is consumed as source, not recomputed here.
    maximum = ray.get("summary", {}).get("maximum_h")
    _require(isinstance(maximum, dict)
             and maximum.get("source") == "original172-box-derived"
             and maximum.get("requested_maximum_h_exact") is None,
             "complete paid original-box h domain required")
    hmax = Q(maximum["effective_maximum_h_exact"])
    _require(hmax == Q(maximum["box_sufficient_maximum_h_exact"]) and hmax > 0,
             "positive paid original-box h bound required")
    new_source = {
        "schema": POLICY+"-authenticated-input", **expected,
        "ring_radial_index": 141, "sigma_binary64_exact": source["sigma_binary64_exact"],
        "radial": copy.deepcopy(source["radial"]), "theta": copy.deepcopy(source["theta"]),
        "paid_ring_binding_sha256": ring["binding_sha256"],
        "paid_ray_source": copy.deepcopy(rs), "source_receipt": copy.deepcopy(receipt),
        "paid_ring_metric": copy.deepcopy(metric),
        "fixed_metric_binding_sha256": source["fixed_metric_binding_sha256"],
        "exact_radial_embedding_sha256": digest(exact),
        "original_R1_ray_and_its_alpha_are_not_parameters_of_this_problem": True}
    sink["source"] = copy.deepcopy(new_source)
    grids = {}
    sink["_paid_grids"] = grids
    for label in LABELS:
        _wall(wall, "free-R1R2.source."+label)
        old = ring["grids"][label]
        n = int(old["arrays"]["theta"]["shape"][0])
        theta = _decode_payload(old["arrays"]["theta"], (n,), label+"/theta")
        _require(array_binding(theta) == source["theta"][label], "paid full theta grid differs")
        base = {key: _decode_payload(old["position_two_jets_without_X"][key],
                                    (n, 3), label+"/"+key) for key in JETS}
        for key, value in base.items():
            _require(array_binding(value) == rb["grid_position_arrays"][label][key],
                     "unbound original position jet: "+label+"/"+key)
        G = _decode_payload(old["arrays"]["actual_G"], (n,), label+"/G")
        _require(array_binding(G) == rb["grid_arrays"][label]["actual_G"], "unbound paid G")
        saved = ray["new_complete_frame_and_vector_tables"][label]
        au = _decode_payload(saved["original_u9"], (n, 9), label+"/u9")
        av = _decode_payload(saved["original_v8"], (n, 8), label+"/v8")
        _require(_same(au[:, :8], av), "the original shared eight angular columns differ")
        V17 = _decode_payload(saved["V17"], (n, 3, 17), label+"/V17")
        Z17 = _decode_payload(saved["tangent_columns17"], (1, n, 3, 17), label+"/Z17")[0]
        PiZ17 = _decode_payload(saved["primitive_tangent_columns17"],
                               (1, n, 3, 17), label+"/paid-PiZ17")[0]
        fields, frame = saved.get("scalar_fields"), saved.get("scalar_frame")
        _require(isinstance(fields, dict) and isinstance(frame, dict),
                 "literal paid scalar fields and frame are missing")
        u = _decode_payload(fields["u"]["value"], (1, n), label+"/u")[0]
        v = _decode_payload(fields["v"]["value"], (1, n), label+"/v")[0]
        LTu = _decode_payload(frame["Ts_value_part"]["u"], (1, n, 3), label+"/Ts-value-u")[0]
        LTv = _decode_payload(frame["Ts_value_part"]["v"], (1, n, 3), label+"/Ts-value-v")[0]
        grids[label] = {
            "theta": theta, "base": base, "G": G, "au": au, "av": av,
            "u": u, "v": v, "V17": V17, "Z17": Z17, "PiZ17": PiZ17,
            "Ts_value_u": LTu, "Ts_value_v": LTv}
        grids[label]["source_arrays"] = {
            key: array_binding(value) for key, value in grids[label].items()
            if isinstance(value, np.ndarray)}
        grids[label]["source_arrays"]["base_twojets"] = {
            key: array_binding(value) for key, value in base.items()}
        sink.setdefault("restored_grid_receipts", {})[label] = {
            "complete_angle_count": n, "source_arrays": copy.deepcopy(grids[label]["source_arrays"]),
            "original_scalar_frame_and_old_Pi_recomputed": False}
    _wall(wall, "free-R1R2.source.complete")
    return (q, physical, low, high, metric_values["a"], metric_values["a_s"],
            hmax, matrix, copy.deepcopy(exact), new_source, grids)


def _quadratic_descriptors():
    """125 exact generators; no rank determination or angular refit."""
    out = []
    for i in range(9):
        for j in range(i, 9):
            out.append({"sector": "uu", "angular_indices": [i, j],
                        "terms": [[i, j, 1 if i == j else 2]]})
    for i in range(8):
        for j in range(i, 8):
            terms = [[i, 9+j, 1]]
            if i != j:
                terms.append([j, 9+i, 1])
            out.append({"sector": "uv_shared", "angular_indices": [i, j],
                        "terms": terms, "factor_two_is_in_the_primitive_column": True})
    for j in range(8):
        out.append({"sector": "uv_core", "angular_indices": [8, j],
                    "terms": [[8, 9+j, 1]], "factor_two_is_in_the_primitive_column": True})
    for i in range(8):
        for j in range(i, 8):
            out.append({"sector": "vv", "angular_indices": [i, j],
                        "terms": [[9+i, 9+j, 1 if i == j else 2]]})
    _require(len(out) == 125, "literal quadratic generation count")
    return out


def _new_primitive_batch(grid, aa, a_s, label, descriptors, wall, charge, sink):
    event = {"grid": label, "status": "entered", "primitive_columns": 142,
             "new_linear_columns": 17, "new_quadratic_columns": 125,
             "charged": False, "primitive_call_entered": False,
             "old_V17_Pi_calls": 0, "new_frame_calls": 0}
    sink.setdefault("new_primitive_events", []).append(event)
    tick = time.monotonic()
    started_call = None
    actual = {}
    sink.setdefault("_new_primitive_arrays", {})[label] = actual
    try:
        _wall(wall, "free-R1R2.primitive.prepare."+label)
        theta, u, v = grid["theta"], grid["u"], grid["v"]
        phase = theta+u
        zero = np.zeros_like(u)
        N = np.stack((np.cos(phase), np.sin(phase), zero), axis=-1)
        H = np.stack((-np.sin(phase), np.cos(phase), zero), axis=-1)
        ez = np.stack((zero, zero, np.ones_like(zero)), axis=-1)
        c = 1/np.sqrt(1+v*v)
        Tuu = -c[:, None]*H
        Tuv = (v*c**3)[:, None]*N
        Tvv = ((2*v*v-1)*c**5)[:, None]*H-(3*v*c**5)[:, None]*ez
        actual.update(Tuu=Tuu, Tuv=Tuv, Tvv=Tvv)
        au, av = grid["au"], grid["av"]
        linear = 2*np.concatenate((
            grid["Ts_value_u"][:, :, None]*au[:, None, :],
            grid["Ts_value_v"][:, :, None]*av[:, None, :]), axis=-1)
        columns = []
        for item in descriptors:
            i, j = item["angular_indices"]
            if item["sector"] == "uu":
                column = Tuu*(au[:, i]*au[:, j])[:, None]
            elif item["sector"] == "uv_shared":
                column = 2*Tuv*(av[:, i]*av[:, j])[:, None]
            elif item["sector"] == "uv_core":
                column = 2*Tuv*(au[:, 8]*av[:, j])[:, None]
            else:
                column = Tvv*(av[:, i]*av[:, j])[:, None]
            columns.append(column)
        quadratic = np.stack(columns, axis=-1)
        batch = np.concatenate((linear, quadratic), axis=-1)[None, ...]
        _require(batch.shape == (1, len(theta), 3, 142) and np.all(np.isfinite(batch)),
                 "finite complete new142-column angular input required")
        actual["new_primitive_input142"] = batch
        event["input"] = array_binding(batch)
        _wall(wall, "free-R1R2.primitive.before-charge."+label)
        event["charge_receipt"] = copy.deepcopy(charge({
            "schema": POLICY+"-primitive-charge", "grid": label, "columns": 142,
            "new_linear_columns": 17, "new_quadratic_columns": 125,
            "complete_theta_count": len(theta), "axis": 1, "order": -1,
            "input": array_binding(batch), "new_frame_calls": 0, "old_V17_Pi_calls": 0}))
        event["charged"] = True
        _wall(wall, "free-R1R2.primitive.before-call."+label)
        started_call = time.monotonic()
        event["primitive_call_entered"] = True
        primitive = periodic_operator(batch, -1)
        actual["original_new_primitive_output142"] = primitive
        event["primitive_call_seconds"] = time.monotonic()-started_call
        _require(primitive.shape == batch.shape and np.all(np.isfinite(primitive)),
                 "finite complete new angular primitive required")
        L17 = 2*a_s*grid["PiZ17"]+aa*primitive[0, :, :, :17]
        H125 = aa*primitive[0, :, :, 17:]
        actual.update(L17=L17, H125=H125)
        _freeze(actual)
        event.update(status="complete", phase_seconds=time.monotonic()-tick,
                     output=array_binding(primitive), L17=array_binding(L17), H125=array_binding(H125),
                     floating_reassembly_has_its_own_identity=True)
        _wall(wall, "free-R1R2.primitive.complete."+label)
        return L17, H125
    except Exception as error:
        event["error"] = _error(error)
        event["phase_seconds"] = time.monotonic()-tick
        if started_call is not None and "primitive_call_seconds" not in event:
            event["primitive_call_seconds_at_exception"] = time.monotonic()-started_call
        if event["status"] != "complete":
            event["status"] = "raised"
        else:
            event["completed_arrays_retained_before_post_call_stop"] = True
        raise


def _physical_coordinates(matrix, physical, low, high, hmax):
    nu0, nu1, nu2 = matrix
    pivot = max(range(3), key=lambda k: abs(nu0[k]))
    _require(nu0[pivot] != 0, "literal R0 row must contain a nonzero coefficient")
    free = tuple(k for k in range(3) if k != pivot)
    P = [[Q(0) for _ in range(34)] for _ in range(172)]
    X = [[Q(0) for _ in range(34)] for _ in range(17)]
    Y = [[Q(0) for _ in range(34)] for _ in range(17)]
    entries = []
    for j in range(17):
        rows = _mode_physical_rows(j)
        for local, k in enumerate(free):
            col = 2*j+local
            P[rows[k]][col] = Q(1, 4)
            P[rows[pivot]][col] = -nu0[k]/(4*nu0[pivot])
            for l in range(3):
                X[j][col] += nu1[l]*P[rows[l]][col]
                Y[j][col] += nu2[l]*P[rows[l]][col]
            entries.append({
                "backend_column": col, "mode": j, "free_local_spline": k,
                "free_physical172_row": rows[k], "eliminated_local_spline": pivot,
                "eliminated_physical172_row": rows[pivot],
                "free_increment_exact": "backend_z/4",
                "eliminated_increment_coefficient_exact": str(P[rows[pivot]][col]),
                "decoded_R1_coefficient_exact": str(X[j][col]),
                "decoded_R2_coefficient_exact": str(Y[j][col])})
    active = tuple(sorted({row for j in range(17) for row in _mode_physical_rows(j)}))
    _require(all(hmax >= 4*max(abs(low[j]-physical[j]), abs(high[j]-physical[j]))
                 for j in active), "paid h bound must cover the original physical box")
    exact = {"P": tuple(tuple(row) for row in P),
             "X": tuple(tuple(row) for row in X), "Y": tuple(tuple(row) for row in Y)}
    arrays = {key: np.asarray([[float(v) for v in row] for row in value], dtype=np.float64)
              for key, value in exact.items()}
    _freeze(arrays)
    record = {
        "schema": POLICY+"-fixed-physical-coordinate-map",
        "pivot_local_spline": pivot, "free_local_splines": list(free),
        "R0_row_exact": [str(v) for v in nu0],
        "source_R1_row_exact": [str(v) for v in nu1],
        "source_R2_row_exact": [str(v) for v in nu2],
        "free_increment_scale_exact": "1/4",
        "entries": copy.deepcopy(entries),
        "float_maps": {key: array_binding(value) for key, value in arrays.items()},
        "exact_maps_sha256": digest({key: [[str(v) for v in row] for row in value]
                                     for key, value in exact.items()}),
        "zero_width_original_box_rows_retained_as_constraints": True,
        "no_new_inverse_or_old_threejet_identity_check": True}
    return exact, arrays, active, record


def _linear_rows(P, physical, low, high, hmax, target):
    rows, rhs, tags = [], [], []
    def add(coeff, K, h, bound, tag):
        row = np.r_[np.asarray(coeff, dtype=np.float64), float(K), float(h)]
        _require(row.shape == (36,) and np.all(np.isfinite(row)) and math.isfinite(float(bound)),
                 "finite complete physical row required")
        rows.append(row); rhs.append(float(bound)); tags.append(tag)
    for j in range(172):
        add(P[j], 0., 0., high[j]-physical[j],
            {"kind": "physical172_box", "physical_index": j, "side": "upper"})
        add(-P[j], 0., 0., physical[j]-low[j],
            {"kind": "physical172_box", "physical_index": j, "side": "lower"})
        if np.any(P[j] != 0.):
            add(4*P[j], 0., -1., 0.,
                {"kind": "complete_physical_norm", "physical_index": j, "side": "plus"})
            add(-4*P[j], 0., -1., 0.,
                {"kind": "complete_physical_norm", "physical_index": j, "side": "minus"})
    zero = np.zeros(34)
    add(zero, -1., 0., -target, {"kind": "K_lower_target"})
    add(zero, 1., 0., Q(INITIAL_K_EXACT), {"kind": "K_upper_original58"})
    add(zero, 0., -1., 0., {"kind": "h_lower"})
    add(zero, 0., 1., hmax, {"kind": "h_upper"})
    A, b = np.stack(rows), np.asarray(rhs, dtype=np.float64)
    _freeze({"A": A, "b": b})
    return A, b, tags


def build_free_R1_R2_model(
        field, state168, paid_ring_model, paid_ray_model, cfg, lower172, upper172,
        source_receipt, wall, capture=None, *, metric_budget,
        target_exact=TARGET_EXACT, charge_primitive_batch):
    """Build the new34-control model; exactly two new complete primitive batches."""
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty new-model capture required")
    _require(callable(wall) and callable(charge_primitive_batch),
             "shared wall and new primitive debit callback required")
    sink.update(schema=POLICY+"-build-capture", status="entered", definition=definition(),
                ordinary_calls=0, new_frame_calls=0, metric_calls=0,
                old_V17_Pi_calls=0, old_optimization_calls=0, geometric_J_calls=0)
    started = time.monotonic()
    try:
        eps, target = float(metric_budget), _q(target_exact)
        _require(math.isfinite(eps) and 0 < eps < 1 and 0 < target < Q(INITIAL_K_EXACT),
                 "literal metric budget and target below original58 upper curvature required")
        target_lower = float(target)
        if Q.from_float(target_lower) < target:
            target_lower = math.nextafter(target_lower, math.inf)
        _require(Q.from_float(target_lower) >= target and target_lower < 58.,
                 "inward binary64 lower bound must preserve the exact target interval")
        source_data = _restore_paid(
            field, state168, paid_ring_model, paid_ray_model, cfg,
            lower172, upper172, source_receipt, wall, sink)
        q, physical, low, high, aa, a_s, hmax, matrix, exact_basis, source, grids = source_data
        _require(Q.from_float(eps) == Q(paid_ray_model["source"]["metric_budget_exact_binary64"])
                 and target == Q(paid_ray_model["source"]["target_exact"]),
                 "the new free problem must retain the declared original metric and reach targets")
        descriptors = _quadratic_descriptors()
        sink["quadratic_generators"] = copy.deepcopy(descriptors)
        for label in LABELS:
            L17, H125 = _new_primitive_batch(
                grids[label], aa, a_s, label, descriptors, wall, charge_primitive_batch, sink)
            grid = grids[label]
            grid["L17"], grid["H125"] = L17, H125
            T = grid["base"]["Xt"]/aa
            C0 = grid["base"]["Xst"]/aa
            D0 = grid["base"]["Xtt"]/(aa*aa)
            W17 = np.cross(np.moveaxis(grid["V17"], -1, -2), T[:, None, :])
            W17 = np.moveaxis(W17, -2, -1)
            _require(W17.shape == grid["V17"].shape, "complete cross-column shape")
            grid.update(T=T, C0=C0, D0=D0, W17=W17)
            _require(np.all(grid["G"] >= eps), "paid G>=metric budget is needed for the Q lower bound")
            _freeze({key: grid[key] for key in ("T", "C0", "D0", "W17", "L17", "H125")})
            sink.setdefault("derived_grid_receipts", {})[label] = {
                key: array_binding(grid[key]) for key in ("T", "C0", "D0", "W17", "L17", "H125")}
            _wall(wall, "free-R1R2.grid-model.complete."+label)
        exact_map, maps, active, coordinate_record = _physical_coordinates(
            matrix, physical, low, high, hmax)
        sink["physical_coordinates"] = coordinate_record
        sink["_new_coordinate_arrays"] = maps
        A, b, tags = _linear_rows(maps["P"], physical, low, high, hmax, target_lower)
        sink["_new_linear_arrays"] = {"A": A, "b": b}
        x0 = np.r_[np.zeros(34), float(Q(INITIAL_K_EXACT)), 0.]
        x0.setflags(write=False)
        seed = {
            "backend_seed36": _vector(x0),
            "decoded_R1_R2_seed36": _vector(np.r_[np.zeros(34), 58., 0.]),
            "base": "the same accepted58, with zero physical increment",
            "source_actual58_fourteen_gates_are_not_rerun": True,
            "first_new_model_evaluation_is_still_charged": True,
            "new_floating_model_feasibility_not_assumed_without_its_evaluation": True,
            "one_seed_no_restart_or_old_optimizer_replay": True}
        sink["initial_point"] = copy.deepcopy(seed)
        model = FreeR1R2Model(
            field, q, cfg, source, exact_basis, physical, low, high, aa, a_s,
            hmax, eps, target, target_lower, descriptors, grids, exact_map, maps, active,
            coordinate_record, A, b, tags, x0, seed, sink)
        sink.update(status="complete", model_binding_sha256=model.binding_sha256,
                    elapsed_seconds=time.monotonic()-started)
        _wall(wall, "free-R1R2.build.complete")
        return model
    except Exception as error:
        sink.update(status="raised", error=_error(error),
                    elapsed_seconds=time.monotonic()-started,
                    completed_new_primitives_retained_without_rebuilding=True)
        raise


class FreeR1R2Model:
    def __init__(
            self, field, q, cfg, source, exact_basis, physical, low, high, aa, a_s,
            hmax, eps, target, target_lower, descriptors, grids, exact_map, maps, active,
            coordinate_record, A, b, tags, x0, seed, capture):
        self.field, self.state168, self.cfg = field, q, copy.deepcopy(cfg)
        self.source, self.exact_basis = copy.deepcopy(source), copy.deepcopy(exact_basis)
        self.base_physical172, self.lower172, self.upper172 = physical, low, high
        self.radius, self.radius_s = aa, a_s
        self.maximum_h_exact, self.eps, self.target_exact = hmax, eps, target
        self.target_binary64_lower_bound = target_lower
        self.descriptors, self.grids = copy.deepcopy(descriptors), grids
        self.exact_map, self.maps, self.active = exact_map, maps, active
        self.coordinate_record = copy.deepcopy(coordinate_record)
        self.linear_A, self.linear_b, self.linear_tags = A, b, tags
        self.x0, self.seed, self.capture = x0, seed, capture
        self.row_scales = None
        self.solve_attempted = False
        self.solver_sink = None
        self.row_layout = []
        offset = 0
        for label in LABELS:
            n = len(grids[label]["theta"])
            for component in GRID_CONSTRAINTS:
                self.row_layout.append({
                    "grid": label, "component": component, "offset": offset, "count": n,
                    "theta_array": array_binding(grids[label]["theta"]),
                    "original_angle_order": True})
                offset += n
        self.row_layout.append({
            "component": "original172_box_complete_norm_K_h",
            "offset": offset, "count": len(b), "tags_sha256": digest(tags)})
        self.constraint_count = offset+len(b)
        self.binding = {
            "schema": POLICY+"-model-binding", "definition": definition(),
            "source": copy.deepcopy(source), "implementation_hashes": implementation_hashes(),
            "metric_budget_binary64": eps, "metric_budget_exact_binary64": str(Q.from_float(eps)),
            "curvature_lower_target_exact": str(target), "curvature_upper_exact": INITIAL_K_EXACT,
            "backend_curvature_lower_bound_binary64": target_lower,
            "backend_curvature_lower_bound_exact_binary64": str(Q.from_float(target_lower)),
            "backend_lower_is_not_below_exact_target": True,
            "original_box_sufficient_hmax_exact": str(hmax),
            "literal_paid_threejet_embedding": copy.deepcopy(exact_basis),
            "physical_coordinates": copy.deepcopy(coordinate_record),
            "quadratic_generators": copy.deepcopy(descriptors),
            "source_grid_arrays": {label: copy.deepcopy(grids[label]["source_arrays"])
                                   for label in LABELS},
            "new_grid_arrays": {
                label: {key: array_binding(grids[label][key])
                        for key in ("L17", "H125", "T", "C0", "D0", "W17")}
                for label in LABELS},
            "new_primitive_output142": {
                label: array_binding(capture["_new_primitive_arrays"][label][
                    "original_new_primitive_output142"]) for label in LABELS},
            "linear_A": array_binding(A), "linear_b": array_binding(b),
            "linear_row_tags_sha256": digest(tags),
            "constraint_layout": copy.deepcopy(self.row_layout),
            "initial_backend_seed36": array_binding(x0),
            "original_actual58_not_a_returned_or_unaccepted_old_ray_point": True}
        self.binding_sha256 = digest(self.binding)

    def assert_context(self):
        self.field._assert_context()
        _require(digest(self.binding) == self.binding_sha256
                 and digest(self.cfg) == self.source["configuration_sha256"]
                 and array_binding(self.state168) == self.source["state168"]
                 and digest(self.field.identity(self.state168)) == self.source["physical_state_sha256"],
                 "new free model/current field/state/cfg changed")
        for label in LABELS:
            for key, expected in self.binding["new_grid_arrays"][label].items():
                _require(array_binding(self.grids[label][key]) == expected,
                         "new grid model coefficient changed: "+label+"/"+key)
        _require(array_binding(self.linear_A) == self.binding["linear_A"]
                 and array_binding(self.linear_b) == self.binding["linear_b"]
                 and all(array_binding(value) == self.coordinate_record["float_maps"][key]
                         for key, value in self.maps.items()),
                 "original physical mapping/rows changed")

    def decode_backend(self, backend36):
        raw = _array(backend36, (36,), "literal new backend36")
        values = np.r_[self.maps["X"] @ raw[:34], self.maps["Y"] @ raw[:34], raw[34:]]
        return _array(values, (36,), "floating decoded R1/R2/K/h")

    def exact_decode(self, backend36):
        raw = _array(backend36, (36,), "literal backend36 for exact decode")
        z = tuple(Q.from_float(float(v)) for v in raw[:34])
        physical_delta = tuple(sum(c*v for c, v in zip(row, z))
                               for row in self.exact_map["P"])
        x = tuple(sum(c*v for c, v in zip(row, z)) for row in self.exact_map["X"])
        y = tuple(sum(c*v for c, v in zip(row, z)) for row in self.exact_map["Y"])
        return physical_delta, x, y, Q.from_float(float(raw[34])), Q.from_float(float(raw[35]))

    def quadratic_weights(self, x):
        x = _array(x, (17,), "common R1 coefficients")
        values = np.zeros(125)
        jac = np.zeros((125, 17))
        for row, descriptor in enumerate(self.descriptors):
            for i, j, coefficient in descriptor["terms"]:
                values[row] += coefficient*x[i]*x[j]
                jac[row, i] += coefficient*x[j]
                jac[row, j] += coefficient*x[i]
        return values, jac

    def _full_value_jacobian(self, backend36, partial):
        backend = _array(backend36, (36,), "new full-evaluation backend36")
        decoded = self.decode_backend(backend)
        x, y, K = decoded[:17], decoded[17:34], float(decoded[34])
        weights, weights_x = self.quadratic_weights(x)
        partial.update(status="entered", backend36=_vector(backend),
                       decoded_R1_R2_K_h36=_vector(decoded), completed_grids={})
        values, jacobians, diagnostics = [], [], {}
        Xmap, Ymap = self.maps["X"], self.maps["Y"]
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            for label in LABELS:
                g = self.grids[label]
                V, Z, L, H = g["V17"], g["Z17"], g["L17"], g["H125"]
                U = g["base"]["Xs"]+np.einsum("icj,j->ic", V, x)
                Z12 = g["C0"]+np.einsum("icj,j->ic", Z, x)
                Z11 = (g["base"]["Xss"]+np.einsum("icj,j->ic", L, x)
                       +np.einsum("icm,m->ic", H, weights)
                       +np.einsum("icj,j->ic", V, y))
                Z11_x = L+np.einsum("icm,mj->icj", H, weights_x)
                w = np.cross(U, g["T"])
                G = g["G"]
                E, F, QQ = _dot(U, U), _dot(U, g["T"]), _dot(w, w)
                E_x = 2*_dot_columns(U, V)
                F_x = _dot_columns(g["T"], V)
                Q_x = 2*_dot_columns(w, g["W17"])
                pp, rr, cc = _dot(w, Z11), _dot(w, Z12), _dot(w, g["D0"])
                p_x = _dot_columns(Z11, g["W17"])+_dot_columns(w, Z11_x)
                p_y = _dot_columns(w, V)
                r_x = _dot_columns(Z12, g["W17"])+_dot_columns(w, Z)
                c_x = _dot_columns(g["D0"], g["W17"])
                aa = G*G*pp-2*G*F*rr+F*F*cc
                a_x = (G[:, None]**2*p_x
                       -2*G[:, None]*(F_x*rr[:, None]+F[:, None]*r_x)
                       +2*(F*cc)[:, None]*F_x+(F*F)[:, None]*c_x)
                a_y = G[:, None]**2*p_y
                bb = G*rr-F*cc
                b_x = G[:, None]*r_x-cc[:, None]*F_x-F[:, None]*c_x
                tt = aa+cc*QQ
                t_x = a_x+QQ[:, None]*c_x+cc[:, None]*Q_x
                t_y = a_y
                RR = K*K*G*G*QQ*QQ+aa*cc-bb*bb
                R_x = (2*K*K*(G*G*QQ)[:, None]*Q_x
                       +cc[:, None]*a_x+aa[:, None]*c_x-2*bb[:, None]*b_x)
                R_y = cc[:, None]*a_y
                R_K = 2*K*G*G*QQ*QQ
                raw = (
                    self.eps*(1+self.eps-E)-F*F,
                    self.eps*(E-1+self.eps)-F*F,
                    QQ-G*(1-self.eps),
                    4*K*K*G*G*QQ**3-tt*tt,
                    RR,
                    RR*RR-K*K*G*G*QQ*tt*tt)
                dx = (
                    -self.eps*E_x-2*F[:, None]*F_x,
                    self.eps*E_x-2*F[:, None]*F_x,
                    Q_x,
                    12*K*K*(G*G*QQ*QQ)[:, None]*Q_x-2*tt[:, None]*t_x,
                    R_x,
                    2*RR[:, None]*R_x-K*K*G[:, None]**2*(
                        (tt*tt)[:, None]*Q_x+2*(QQ*tt)[:, None]*t_x))
                dy = (
                    None, None, None, -2*tt[:, None]*t_y, R_y,
                    2*RR[:, None]*R_y-2*K*K*(G*G*QQ*tt)[:, None]*t_y)
                dk = (
                    None, None, None, 8*K*G*G*QQ**3, R_K,
                    2*RR*R_K-2*K*G*G*QQ*tt*tt)
                n = len(E)
                for row, d_x, d_y, d_K in zip(raw, dx, dy, dk):
                    derivative = np.zeros((n, 36))
                    derivative[:, :34] = d_x @ Xmap
                    if d_y is not None:
                        derivative[:, :34] += d_y @ Ymap
                    if d_K is not None:
                        derivative[:, K_COLUMN] = d_K
                    values.append(row)
                    jacobians.append(derivative)
                arrays = {
                    "E": E, "F": F, "actual_G": G, "Q_cross": QQ,
                    "a_numerator": aa, "b_numerator": bb, "c_numerator": cc,
                    "t_trace_numerator": tt, "R_determinant_numerator": RR,
                    **dict(zip(GRID_CONSTRAINTS, raw))}
                _require(all(np.all(np.isfinite(v)) for v in arrays.values()),
                         "nonfinite complete free-ring contraction: "+label)
                partial["completed_grids"][label] = arrays
                diagnostics[label] = {
                    "constraint_minima_in_original_polynomial_units": {
                        name: float(np.min(value)) for name, value in zip(GRID_CONSTRAINTS, raw)},
                    "Q_cross_minimum": float(np.min(QQ)),
                    "actual_G_minimum": float(np.min(G)), "K": K,
                    "no_actual_fourteen_gate_receipt": True}
            linear = self.linear_b-self.linear_A @ backend
            values.append(linear); jacobians.append(-self.linear_A)
            vals, jac = np.concatenate(values), np.concatenate(jacobians, axis=0)
            _require(vals.shape == (self.constraint_count,)
                     and jac.shape == (self.constraint_count, 36)
                     and np.all(np.isfinite(vals)) and np.all(np.isfinite(jac)),
                     "finite complete free-ring value/analytic-Jacobian required")
            partial.update(status="complete", linear_values=linear,
                           full_values=vals, full_jacobian_backend=jac)
            diagnostics["linear_original_units"] = {
                "minimum": float(np.min(linear)),
                "maximum_violation": float(max(0., -np.min(linear)))}
            return vals, jac, decoded, diagnostics

    def summary(self):
        result = {
            "schema": POLICY+"-model-summary", "binding_sha256": self.binding_sha256,
            "backend_variables": 36, "physical_R1_and_R2_variables": 34,
            "backend_order": "z34,K,h", "decoded_order": "x17,y17,K,h",
            "objective": "K+1e-6*h", "K_interval_exact": [str(self.target_exact), INITIAL_K_EXACT],
            "backend_K_lower_bound_binary64": self.target_binary64_lower_bound,
            "backend_K_lower_bound_exact_binary64": str(Q.from_float(self.target_binary64_lower_bound)),
            "maximum_h_exact": str(self.maximum_h_exact), "metric_budget": self.eps,
            "initial_backend_seed36": _vector(self.x0), "initial_point": copy.deepcopy(self.seed),
            "complete_grid_angle_counts": {label: len(self.grids[label]["theta"]) for label in LABELS},
            "constraint_count": self.constraint_count,
            "constraint_layout": copy.deepcopy(self.row_layout),
            "linear_row_counts": {kind: sum(row["kind"] == kind for row in self.linear_tags)
                                  for kind in sorted({row["kind"] for row in self.linear_tags})},
            "source_physical_state_sha256": self.source["physical_state_sha256"],
            "row_scales_established": self.row_scales is not None,
            "row_scales_binding": None if self.row_scales is None else array_binding(self.row_scales),
            "one_solver_attempted": self.solve_attempted,
            "new_primitive_batches": copy.deepcopy(self.capture.get("new_primitive_events", [])),
            "no_new_ordinary_geometry_metric_frame_or_geometric_J": True,
            "backend_success_is_not_actual_fourteen_gate_acceptance": True}
        if self.solver_sink is not None:
            s = self.solver_sink
            result["solver"] = {
                key: copy.deepcopy(s.get(key)) for key in (
                    "status", "backend_entered", "error", "stop_reason", "local_elapsed_seconds",
                    "full_evaluation_counts", "callback_counts", "original_result_stdout_receipt",
                    "qualified_candidate", "candidate_filter")}
            raw = s.get("original_backend_return")
            result["solver"]["original_backend_return_summary"] = None if raw is None else {
                key: copy.deepcopy(raw.get(key)) for key in (
                    "status", "success", "message", "nit", "nfev", "njev",
                    "backend_elapsed_seconds", "scipy_version")}
        return result

    def full_record(self):
        self.assert_context()
        s = self.solver_sink
        emitted = None if s is None else s.get("original_result_stdout_receipt")
        return {
            "schema": POLICY+"-full-new-model", "binding": copy.deepcopy(self.binding),
            "binding_sha256": self.binding_sha256, "summary": self.summary(),
            "original_actual58_state168": _vector(self.state168),
            "original_actual58_physical172_exact": [str(v) for v in self.base_physical172],
            "physical_coordinate_definition": copy.deepcopy(self.coordinate_record),
            "exact_physical_coordinate_maps": {
                key: [[str(v) for v in row] for row in value] for key, value in self.exact_map.items()},
            "actual_float_coordinate_maps": {key: _payload(value) for key, value in self.maps.items()},
            "quadratic_generator_descriptors": copy.deepcopy(self.descriptors),
            "new_primitive_batches": {
                label: {key: _payload(value) for key, value in values.items()}
                for label, values in self.capture["_new_primitive_arrays"].items()},
            "linear_row_tags": copy.deepcopy(self.linear_tags),
            "new_linear_A": _payload(self.linear_A), "new_linear_b": _payload(self.linear_b),
            "initial_point": copy.deepcopy(self.seed), "build_receipt": _public(self.capture),
            "solver_original_stdout_receipt": copy.deepcopy(emitted),
            "unemitted_original_backend_return": (
                None if s is None or emitted is not None else copy.deepcopy(s.get("original_backend_return"))),
            "solver_trace_location": "separate free_R1_R2_capture_record(include_arrays=True) after solve",
            "old_paid_scalar_fields_frame_V17_and_ring_jets_not_duplicated": True,
            "new_values_are_only_in_original_stdout_and_current_process": True}

    def candidate_from_backend(self, backend36):
        backend = _array(backend36, (36,), "actual returned backend36")
        delta, x, y, K, h = self.exact_decode(backend)
        base = tuple(Q.from_float(float(v)) for v in self.state168)
        independent_delta = tuple(delta[:154])+tuple(Q(0) for _ in range(14))
        ideal = tuple(q+d for q, d in zip(base, independent_delta))
        ideal_physical = tuple(q+d for q, d in zip(self.base_physical172, delta))
        candidate = self.state168.copy()
        for row in self.active:
            candidate[row] = float(ideal[row])
        _require(np.all(np.isfinite(candidate)), "one-round exact candidate overflowed")
        candidate = _array(self.field.validate_state(candidate), (168,), "rounded candidate168")
        actual_physical = tuple(self.field.full_coefficients(candidate, exact=True))
        actual_delta = tuple(v-b for v, b in zip(actual_physical, self.base_physical172))
        ideal_h, actual_h = 4*max(map(abs, delta)), 4*max(map(abs, actual_delta))
        ideal_bad = [j for j, (lo, v, hi) in enumerate(
            zip(self.lower172, ideal_physical, self.upper172)) if not lo <= v <= hi]
        actual_bad = [j for j, (lo, v, hi) in enumerate(
            zip(self.lower172, actual_physical, self.upper172)) if not lo <= v <= hi]
        exact_box = self.field.exact_full_box_decision(
            candidate, np.asarray(list(map(float, self.lower172))),
            np.asarray(list(map(float, self.upper172))))
        _require(bool(exact_box["exact_full_box_pass"]) == (not actual_bad),
                 "canonical original field box disagrees with exact physical embedding")
        model_decoded = self.decode_backend(backend)
        exact_decoded_float = np.asarray([float(v) for v in x+y+(K, h)])
        _require(np.all(np.isfinite(exact_decoded_float)), "finite exact-decoded R1/R2 controls")
        K_pass = self.target_exact <= K <= Q(INITIAL_K_EXACT)
        record = {
            "schema": POLICY+"-exact-physical-plane-and-once-rounded-candidate",
            "model_binding_sha256": self.binding_sha256,
            "actual_backend_raw36": _vector(backend),
            "backend_order": "z34,K,h", "decoded_order": "x17,y17,K,h",
            "floating_callback_decoded36": _vector(model_decoded),
            "exact_decoded_R1_17": [str(v) for v in x],
            "exact_decoded_R2_17": [str(v) for v in y],
            "exact_decoded_K": str(K), "exact_decoded_h_backend": str(h),
            "exact_decoded36_rounded_for_original_unit_filter": _vector(exact_decoded_float),
            "float_callback_minus_rounded_exact_decode": _vector(model_decoded-exact_decoded_float),
            "unrounded_exact_independent168_increment": [str(v) for v in independent_delta],
            "unrounded_exact_independent168": [str(v) for v in ideal],
            "unrounded_exact_physical172_increment": [str(v) for v in delta],
            "unrounded_exact_physical172": [str(v) for v in ideal_physical],
            "unrounded_exact_h": str(ideal_h),
            "unrounded_exact_box_pass": not ideal_bad,
            "unrounded_exact_box_violating_indices": ideal_bad,
            "unrounded_exact_h_bound_pass": bool(ideal_h <= self.maximum_h_exact),
            "backend_norm_epigraph_exact_pass": bool(ideal_h <= h),
            "backend_h_minus_ideal_physical_h_exact": str(h-ideal_h),
            "rounded_independent168": _vector(candidate),
            "rounded_physical172_exact": [str(v) for v in actual_physical],
            "rounded_physical172_binary64": _vector(np.asarray(list(map(float, actual_physical)))),
            "rounded_exact_physical172_increment": [str(v) for v in actual_delta],
            "rounded_exact_h": str(actual_h),
            "rounded_exact_box_decision": exact_box,
            "rounded_exact_h_bound_pass": bool(actual_h <= self.maximum_h_exact),
            "rounded_exact_h_at_most_original_small_1_over_128":
                bool(actual_h <= Q(REFERENCE_SMALL_H_EXACT)),
            "independent_rounding_error_exact": [
                str(Q.from_float(float(v))-u) for v, u in zip(candidate, ideal)],
            "physical_rounding_error_exact": [str(v-u) for v, u in zip(actual_physical, ideal_physical)],
            "K_exact_interval_pass": bool(K_pass),
            "K_is_above_requested_reach_target": bool(K > self.target_exact),
            "candidate_physical_identity_sha256": digest(self.field.identity(candidate)),
            "original_current_base_physical_identity_sha256": self.source["physical_state_sha256"],
            "original_actual_box_and_new_explicit_h_pass": bool(
                K_pass and not ideal_bad and not actual_bad and 0 <= h <= self.maximum_h_exact
                and ideal_h <= self.maximum_h_exact and actual_h <= self.maximum_h_exact),
            "exact_R0_plane_preserved_in_unrounded_physical_increment": True,
            "rounded_candidate_not_claimed_exactly_in_that_plane": True,
            "raw_backend_h_is_not_silently_repaired": True,
            "no_intermediate_unaccepted_R1_point": True, "actual14_feasibility_claimed": False}
        return candidate, record, exact_decoded_float

    def original_unit_filter(self, decoded36, partial):
        raw = _array(decoded36, (36,), "actual exact-decoded control values for original-unit rows")
        x, y, K = raw[:17], raw[17:34], float(raw[34])
        weights, unused_derivative = self.quadratic_weights(x)
        all_pass, summaries = True, {}
        partial.update(schema=POLICY+"-returned-original-unit-filter", status="entered", grids={})
        for label in LABELS:
            g, aa = self.grids[label], self.radius
            old, G = g["base"], g["G"]
            U = old["Xs"]+np.einsum("icj,j->ic", g["V17"], x)
            Xst = old["Xst"]+aa*np.einsum("icj,j->ic", g["Z17"], x)
            Xss = (old["Xss"]+np.einsum("icj,j->ic", g["L17"], x)
                   +np.einsum("icm,m->ic", g["H125"], weights)
                   +np.einsum("icj,j->ic", g["V17"], y))
            T = old["Xt"]/aa
            Z12, Z22 = Xst/aa, old["Xtt"]/(aa*aa)
            w = np.cross(U, T)
            QQ = _dot(w, w)
            E, F = _dot(U, U), _dot(U, T)
            _require(np.all(QQ > 0) and np.all(G > 0),
                     "returned controls have no positive original normal area")
            qarea = np.sqrt(QQ)
            I = np.stack((E, F, F, G), axis=-1).reshape(len(E), 2, 2)
            II = np.stack((_dot(w, Xss), _dot(w, Z12), _dot(w, Z12), _dot(w, Z22)),
                          axis=-1).reshape(len(E), 2, 2)/qarea[:, None, None]
            jets = {"Xs": U, "Xt": old["Xt"], "Xss": Xss, "Xst": Xst, "Xtt": old["Xtt"]}
            shape = _normal_shape(jets, I, II, qarea, aa)
            A, B, C = shape["A"], shape["B"], shape["C"]
            rows = np.stack((2*K+A+C, (K+C)*(K+A)-B*B,
                             2*K-A-C, (K-C)*(K-A)-B*B), axis=1)
            phi = .5*(np.sqrt((E-1)**2+4*F*F)+abs(E-1))
            plus = self.eps*(1+self.eps-E)-F*F
            minus = self.eps*(E-1+self.eps)-F*F
            norm = _operator_norm(A, B, C)
            finite = all(np.all(np.isfinite(v)) for v in (
                rows, phi, plus, minus, norm, QQ, shape["q_perp_squared"]))
            metric_pass = bool(finite and np.all(plus >= 0.) and np.all(minus >= 0.)
                               and np.all(phi <= self.eps))
            psd_pass = bool(finite and np.min(rows) >= -LP_ROW_TOLERANCE)
            Q_pass = bool(finite and np.all(QQ-G*(1-self.eps) >= -LP_ROW_TOLERANCE))
            passed = metric_pass and psd_pass and Q_pass
            all_pass = bool(all_pass and passed)
            summary = {
                "passed": passed, "returned_K": K,
                "metric_quadratics_and_direct_phi_pass": metric_pass,
                "original_unsquared_four_PSD_rows_pass": psd_pass,
                "new_redundant_Q_row_pass": Q_pass,
                "maximum_original_metric_phi": float(np.max(phi)),
                "maximum_operator_norm": float(np.max(norm)),
                "minimum_unsquared_PSD_by_component": np.min(rows, axis=0).tolist(),
                "maximum_original_PSD_violation": float(max(0., -np.min(rows))),
                "original_PSD_row_tolerance": LP_ROW_TOLERANCE,
                "minimum_Q_cross_direct": float(np.min(QQ)),
                "minimum_Schur_q_perp_squared": float(np.min(shape["q_perp_squared"])),
                "maximum_abs_Q_direct_minus_G_Schur": float(np.max(abs(QQ-G*shape["q_perp_squared"]))),
                "maximum_abs_actual_G_minus_one": float(np.max(abs(G-1))),
                "new_floating_prediction_not_continuous_or_actual14_certificate": True}
            summaries[label] = summary
            partial["grids"][label] = {
                "summary": copy.deepcopy(summary), "original_unsquared_PSD_rows": rows,
                "original_metric_phi": phi, "metric_plus": plus, "metric_minus": minus,
                "A": A, "B": B, "C": C, "Q_cross_direct": QQ,
                "q_perp_squared": shape["q_perp_squared"], "actual_G": G,
                "normal": shape["normal"], "actual_I": I, "actual_II": II}
        partial.update(status="complete", passed=bool(all_pass))
        return bool(all_pass), summaries


class _CompleteEvaluationCache:
    """One shared full value/J evaluation per literal backend input."""
    def __init__(self, model, wall, started, seconds, maximum, sink):
        self.model, self.wall = model, wall
        self.started, self.seconds, self.maximum, self.sink = started, seconds, maximum, sink
        self.cache = {}
        self.counts = {"started": 0, "completed": 0, "failed": 0, "cache_hits": 0}
        self.callbacks = {"objective": 0, "objective_jacobian": 0,
                          "constraint_value": 0, "constraint_jacobian": 0,
                          "iteration": 0, "initial_full": 0, "returned_vector": 0}
        sink["full_evaluation_records"] = []
        sink["iteration_records"] = []
        sink["_callback_cache"] = self.cache

    def check(self, phase):
        _wall(self.wall, "free-R1R2.solver."+str(phase))
        elapsed = time.monotonic()-self.started
        if elapsed >= self.seconds:
            raise FreeR1R2Limit("the one new solver clock is exhausted: %.17g seconds" % elapsed)

    def touch(self, x, role):
        self.callbacks[role] = self.callbacks.get(role, 0)+1
        self.sink["callback_counts"] = copy.deepcopy(self.callbacks)
        self.sink["_last_backend_input"] = np.asarray(x, dtype=np.float64).copy()
        self.check(role)
        return _array(x, (36,), "backend callback input")

    def get(self, x, role):
        array = self.touch(x, role)
        key = array.tobytes()
        if key in self.cache:
            self.counts["cache_hits"] += 1
            self.sink["full_evaluation_counts"] = copy.deepcopy(self.counts)
            entry = self.cache[key]
            self.sink["_last_evaluation_partial"] = entry["partial"]
            return entry
        if self.counts["started"] >= self.maximum:
            raise FreeR1R2Limit("the one new full value/analytic-Jacobian budget is exhausted")
        self.counts["started"] += 1
        ordinal = self.counts["started"]
        tick = time.monotonic()
        record = {"ordinal": ordinal, "status": "started", "first_callback_role": role,
                  "backend36": _vector(array), "input_sha256": array_binding(array)["sha256"]}
        self.sink["full_evaluation_records"].append(record)
        partial = {"evaluation_ordinal": ordinal, "status": "entered"}
        self.sink["_last_evaluation_partial"] = partial
        self.sink["full_evaluation_counts"] = copy.deepcopy(self.counts)
        try:
            values, jacobian, physical, diagnostics = self.model._full_value_jacobian(array, partial)
            if ordinal == 1 and role == "initial_full":
                self.sink["_initial_full_evaluation"] = {
                    "status": "original-value-and-Jacobian-returned",
                    "evaluation_ordinal": ordinal, "backend36": array,
                    "decoded_R1_R2_K_h36": physical,
                    "original_unit_constraint_values": values,
                    "analytic_backend_Jacobian": jacobian,
                    "complete_grid_diagnostics": diagnostics,
                    "scaled_copies_not_duplicated": True}
            if self.model.row_scales is None:
                _require(ordinal == 1 and role == "initial_full"
                         and _same(array, self.model.x0),
                         "row scales must be established at the one declared initial input")
                scales = np.maximum(1., np.maximum(abs(values), np.max(abs(jacobian), axis=1)))
                _require(np.all(np.isfinite(scales)) and np.all(scales > 0),
                         "finite positive fixed initial row scales required")
                scales.setflags(write=False)
                self.model.row_scales = scales
                self.sink["_fixed_row_scales"] = scales
                self.sink["fixed_row_scale_receipt"] = {
                    "formula": "max(1,abs(initial raw residual),max(abs(initial backend-J row)))",
                    "evaluation_ordinal": ordinal, "initial_input_sha256": record["input_sha256"],
                    "row_scales": array_binding(scales), "never_updated_after_this_evaluation": True}
            scales = self.model.row_scales
            scaled_values = values/scales
            _require(np.all(np.isfinite(scaled_values)),
                     "finite scaled complete model required")
            # Retain one raw Jacobian per unique input; scale only when the backend requests it.
            for value in (values, jacobian, scaled_values):
                value.setflags(write=False)
            entry = {
                "ordinal": ordinal, "backend": array, "physical": physical,
                "values": values, "jacobian": jacobian,
                "scaled_values": scaled_values,
                "diagnostics": diagnostics, "partial": partial}
            self.cache[key] = entry
            self.counts["completed"] += 1
            if ordinal == 1 and role == "initial_full":
                self.sink["_initial_full_evaluation"]["status"] = "complete"
            record.update(
                status="complete", decoded_R1_R2_K_h36=_vector(physical),
                objective_K_plus_weight_h=float(array[34]+NORM_WEIGHT*array[35]),
                K=float(array[34]), h=float(array[35]), elapsed_seconds=time.monotonic()-tick,
                minimum_scaled_constraint=float(np.min(scaled_values)),
                maximum_scaled_violation=float(max(0., -np.min(scaled_values))),
                full_unscaled_values=array_binding(values),
                full_analytic_backend_Jacobian=array_binding(jacobian),
                complete_grid_diagnostics=copy.deepcopy(diagnostics),
                original_actual_gate_evaluations=0)
            self.sink["full_evaluation_counts"] = copy.deepcopy(self.counts)
            self.check("full-evaluation-complete")
            return entry
        except Exception as error:
            if record["status"] == "started":
                self.counts["failed"] += 1
                record["status"] = "raised"
            else:
                record["completed_work_retained_before_post_call_stop"] = True
            record.update(error=_error(error), elapsed_seconds=time.monotonic()-tick)
            self.sink["full_evaluation_counts"] = copy.deepcopy(self.counts)
            raise

    def objective(self, x):
        value = self.touch(x, "objective")
        return float(value[K_COLUMN]+NORM_WEIGHT*value[H_COLUMN])

    def objective_jacobian(self, x):
        self.touch(x, "objective_jacobian")
        value = np.zeros(36, dtype=np.float64)
        value[K_COLUMN] = 1.
        value[H_COLUMN] = NORM_WEIGHT
        return value

    def constraint_value(self, x):
        return self.get(x, "constraint_value")["scaled_values"].copy()

    def constraint_jacobian(self, x):
        entry = self.get(x, "constraint_jacobian")
        return entry["jacobian"]/self.model.row_scales[:, None]

    def iteration(self, xk):
        # A callback never creates an unrequested scientific evaluation.
        x = self.touch(xk, "iteration")
        entry = self.cache.get(x.tobytes())
        self.sink["iteration_records"].append({
            "ordinal": len(self.sink["iteration_records"])+1,
            "backend36": _vector(x), "objective_K_plus_weight_h": float(x[34]+NORM_WEIGHT*x[35]),
            "K": float(x[34]), "h": float(x[35]),
            "local_elapsed_seconds": time.monotonic()-self.started,
            "cached_full_evaluation_ordinal": None if entry is None else entry["ordinal"],
            "cached_maximum_scaled_violation": None if entry is None else float(
                max(0., -np.min(entry["scaled_values"]))),
            "callback_did_not_run_an_extra_full_evaluation": True})


def _solver_public(sink):
    public = _public(sink)
    raw = public.pop("original_backend_return", None)
    emitted = public.get("original_result_stdout_receipt")
    public["original_backend_return_summary"] = None if raw is None else {
        key: copy.deepcopy(raw.get(key)) for key in (
            "schema", "status", "success", "message", "nit", "nfev", "njev",
            "backend_elapsed_seconds", "scipy_version", "raw_return_captured_before_filter",
            "actual_finite_raw36_saved", "raw_K", "raw_h")}
    public["unemitted_original_backend_return"] = raw if emitted is None else None
    public["evaluation_and_iteration_records_location"] = (
        "solver capture; caller emits free_R1_R2_capture_record(include_arrays=True) "
        "as SOLVE_TRACE after this attempt, including on failure")
    public.pop("full_evaluation_records", None)
    public.pop("iteration_records", None)
    return public


def solve_free_R1_R2_once(
        model, *, wall, charge_solve, emit=None, capture=None,
        solver_time_limit_seconds=SOLVER_SECONDS, maxiter=200, max_evaluations=MAX_EVALUATIONS):
    """One new free34 minimax problem; no continuation of the closed19-vector run."""
    _require(isinstance(model, FreeR1R2Model), "one new FreeR1R2Model required")
    _require(not model.solve_attempted, "the one new solve cannot be restarted")
    _require(callable(charge_solve) and callable(wall), "shared solver debit and clock required")
    _require(emit is None or callable(emit), "optional emitter must be callable")
    _require(type(maxiter) is int and 0 < maxiter <= SLSQP_OPTIONS["maxiter"]
             and type(max_evaluations) is int and 0 < max_evaluations <= MAX_EVALUATIONS,
             "new iteration and full-evaluation ceilings may not be enlarged")
    seconds = float(solver_time_limit_seconds)
    _require(not isinstance(solver_time_limit_seconds, (bool, np.bool_))
             and math.isfinite(seconds) and 0 < seconds <= SOLVER_SECONDS,
             "finite solver time limit no larger than180 required")
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty one-solver capture required")
    sink.update(schema=POLICY+"-one-solver-attempt", status="entered",
                model_binding_sha256=model.binding_sha256, backend_entered=False,
                charged=False, qualified_candidate=False,
                options={"maxiter": maxiter, "ftol": SLSQP_OPTIONS["ftol"], "disp": False},
                maximum_full_evaluations=max_evaluations, solver_time_limit_seconds=seconds,
                initial_point="original58 zero increment, K58,h0",
                no_restart_or_closed_optimizer_replay=True,
                no_unreturned_callback_point_promoted=True,
                original_backend_return=None, original_result_stdout_receipt=None)
    model.solve_attempted = True
    model.solver_sink = sink
    started = time.monotonic()
    cache = None
    candidate, candidate_record = None, None
    try:
        model.assert_context()
        _wall(wall, "free-R1R2.solver.before-charge")
        metadata = {
            "schema": POLICY+"-solver-charge",
            "backend": "scipy.optimize.minimize(method='SLSQP')",
            "model_binding_sha256": model.binding_sha256,
            "backend_variables": 36, "physical_R1_R2_controls": 34,
            "backend_order": "z34,K,h", "decoded_order": "x17,y17,K,h",
            "objective": "K+1e-6*h", "constraint_count": model.constraint_count,
            "options": copy.deepcopy(sink["options"]),
            "max_full_value_and_analytic_Jacobian_evaluations": max_evaluations,
            "solver_time_limit_seconds": seconds,
            "one_new_model_not_a_restart_of_the_closed_ray_problem": True}
        sink["charge_receipt"] = copy.deepcopy(charge_solve(metadata))
        sink["charged"] = True
        cache = _CompleteEvaluationCache(model, wall, started, seconds, max_evaluations, sink)
        cache.check("after-charge-before-import")
        import scipy
        from scipy.optimize import minimize
        sink["scipy_version"] = str(scipy.__version__)
        cache.check("after-import")
        initial_entry = cache.get(model.x0, "initial_full")
        sink["initial_actual_model_receipt"] = {
            "evaluation_ordinal": initial_entry["ordinal"],
            "maximum_scaled_violation": float(max(0., -np.min(initial_entry["scaled_values"]))),
            "original_unit_grid_diagnostics": copy.deepcopy(initial_entry["diagnostics"]),
            "actual_original_geometry_or_fourteen_gates_not_replayed": True}
        sink["backend_bounds"] = [
            *[[None, None] for _ in range(34)],
            [model.target_binary64_lower_bound, float(Q(INITIAL_K_EXACT))],
            [0., float(model.maximum_h_exact)]]
        bounds = [tuple(row) for row in sink["backend_bounds"]]
        cache.check("before-backend")
        backend_started = time.monotonic()
        sink.update(status="backend-entered", backend_entered=True)
        result = minimize(
            cache.objective, model.x0.copy(), method="SLSQP",
            jac=cache.objective_jacobian, bounds=bounds,
            constraints=[{"type": "ineq", "fun": cache.constraint_value,
                          "jac": cache.constraint_jacobian}],
            callback=cache.iteration, options=copy.deepcopy(sink["options"]))
        elapsed_backend = time.monotonic()-backend_started
        sink["_original_return_object"] = result
        raw_x = result.get("x")
        raw = {
            "schema": POLICY+"-original-nonlinear-backend-return",
            "backend": "scipy.optimize.minimize(method='SLSQP')",
            "scipy_version": str(scipy.__version__),
            "model_binding_sha256": model.binding_sha256,
            "options": copy.deepcopy(sink["options"]),
            "backend_variable_order": "z34,K,h", "decoded_variable_order": "x17,y17,K,h",
            "physical_coordinate_definition": copy.deepcopy(model.coordinate_record),
            "actual_raw_backend36": None if raw_x is None else _raw_numeric(raw_x),
            "entire_OptimizeResult_fields": _raw_all_fields(dict(result)),
            "status": None if result.get("status") is None else int(result.get("status")),
            "success": bool(result.get("success", False)),
            "message": str(result.get("message", "")),
            "nit": None if result.get("nit") is None else int(result.get("nit")),
            "nfev": None if result.get("nfev") is None else int(result.get("nfev")),
            "njev": None if result.get("njev") is None else int(result.get("njev")),
            "backend_elapsed_seconds": float(elapsed_backend),
            "raw_return_captured_before_filter": True,
            "returned_multipliers_scope": (
                "SciPy internal-QP approximate KKT multipliers, not a strict nonlinear certificate"),
            "unreturned_bounds_multipliers_or_slacks_not_fabricated": True}
        sink["original_backend_return"] = raw
        sink.update(status="backend-returned", backend_elapsed_seconds=float(elapsed_backend))
        finite_vector = False
        if raw_x is not None:
            arr = np.asarray(raw_x, dtype=np.float64)
            finite_vector = bool(arr.shape == (36,) and np.all(np.isfinite(arr)))
        raw["actual_finite_raw36_saved"] = bool(
            finite_vector and raw["actual_raw_backend36"] is not None
            and raw["actual_raw_backend36"].get("shape") == [36]
            and len(raw["actual_raw_backend36"].get("exact_binary64_flat", [])) == 36)
        if finite_vector:
            raw["raw_K"], raw["raw_h"] = float(arr[K_COLUMN]), float(arr[H_COLUMN])
            raw["floating_decoded_R1_R2_K_h36"] = _vector(model.decode_backend(arr))
        else:
            raw["raw_K"], raw["raw_h"] = None, None
            raw["floating_decoded_R1_R2_K_h36"] = None
        if emit is not None:
            tick = time.monotonic()
            try:
                sink["original_result_stdout_receipt"] = copy.deepcopy(
                    emit("NONLINEAR_RESULT", copy.deepcopy(raw)))
            except Exception as error:
                sink["raw_result_reporting_error"] = _error(error)
                raise
            finally:
                sink["raw_result_emit_seconds"] = time.monotonic()-tick
        cache.check("after-raw-result-output")
        status_eligible = bool(raw["success"] and raw["status"] == 0 and finite_vector)
        sink["backend_candidate_status_eligible"] = status_eligible
        if not status_eligible:
            sink["status"] = "no-qualified-backend-return"
        else:
            entry = cache.get(arr, "returned_vector")
            linear_start = model.row_layout[-1]["offset"]
            linear_violation = float(max(0., -np.min(entry["values"][linear_start:])))
            scaled_violation = float(max(0., -np.min(entry["scaled_values"])))
            candidate_filter = {
                "returned_evaluation_ordinal": entry["ordinal"],
                "maximum_scaled_model_violation": scaled_violation,
                "scaled_model_tolerance": SLSQP_OPTIONS["ftol"],
                "maximum_unscaled_original_linear_violation": linear_violation,
                "original_linear_row_tolerance": LP_ROW_TOLERANCE,
                "scaled_model_pass": bool(scaled_violation <= SLSQP_OPTIONS["ftol"]),
                "original_linear_pass": bool(linear_violation <= LP_ROW_TOLERANCE)}
            sink["candidate_filter"] = candidate_filter
            cache.check("before-exact-candidate")
            proposed, candidate_record, exact_decoded_float = model.candidate_from_backend(arr)
            sink["returned_candidate_record"] = copy.deepcopy(candidate_record)
            sink["_returned_candidate168"] = proposed
            cache.check("after-exact-candidate")
            if not (candidate_filter["scaled_model_pass"] and candidate_filter["original_linear_pass"]
                    and candidate_record["original_actual_box_and_new_explicit_h_pass"]):
                sink["status"] = "returned-vector-fails-new-model-or-exact-original-box"
            else:
                tick = time.monotonic()
                units = {}
                sink["_returned_original_units"] = units
                try:
                    passed, summaries = model.original_unit_filter(exact_decoded_float, units)
                    candidate_filter["original_unsquared_grid_summaries"] = summaries
                    candidate_filter["original_unsquared_and_metric_pass"] = bool(passed)
                except Exception as error:
                    units.update(status="returned-domain-error", error=_error(error))
                    candidate_filter["original_unit_error"] = _error(error)
                    candidate_filter["original_unsquared_and_metric_pass"] = False
                    passed = False
                finally:
                    sink["returned_original_unit_filter_seconds"] = time.monotonic()-tick
                cache.check("after-original-unit-filter")
                if passed:
                    candidate = proposed
                    sink.update(status="new-free-ring-candidate-needs-whole-body-validation",
                                qualified_candidate=True,
                                ring_K_above_reach_target=bool(float(arr[K_COLUMN]) > float(model.target_exact)),
                                original_actual14_or_main_reach_not_claimed=True)
                else:
                    sink["status"] = "returned-vector-fails-original-unsquared-ring-rows"
        cache.check("complete")
    except FreeR1R2Limit as error:
        sink.update(status="stopped-at-declared-new-solver-limit",
                    stop_reason=str(error), error=_error(error), qualified_candidate=False,
                    no_backend_status_relabelled=True)
        candidate = None
    except Exception as error:
        sink.update(status="raised", error=_error(error), qualified_candidate=False,
                    completed_and_returned_work_retained=True)
        candidate = None
        raise
    finally:
        if cache is not None:
            sink["full_evaluation_counts"] = copy.deepcopy(cache.counts)
            sink["callback_counts"] = copy.deepcopy(cache.callbacks)
            sink["cached_complete_literal_inputs"] = len(cache.cache)
        sink["local_elapsed_seconds"] = time.monotonic()-started
        sink["observed_solver_clock_overrun_seconds"] = max(0., sink["local_elapsed_seconds"]-seconds)
        sink["nonpreemptive_solver_clock_checks_not_a_strict_backend_wall_guarantee"] = True
        record = sink.get("returned_candidate_record")
        sink["actual_rounded_candidate168_saved"] = bool(
            isinstance(record, dict)
            and len(record.get("rounded_independent168", {}).get("values", [])) == 168
            and len(record.get("rounded_independent168", {}).get("exact_binary64", [])) == 168)
        sink["actual_physical172_exact_saved"] = bool(
            isinstance(record, dict) and len(record.get("rounded_physical172_exact", [])) == 172)
    return {
        "status": sink["status"], "qualified_candidate": bool(sink["qualified_candidate"]),
        "qualified": bool(sink["qualified_candidate"]),
        "candidate168": candidate, "candidate": candidate,
        "candidate_record": copy.deepcopy(candidate_record),
        "report": _solver_public(sink)}


def free_R1_R2_capture_record(capture, *, include_arrays=False):
    """Actual public partials and retained arrays only; no source/science regeneration."""
    _require(isinstance(capture, dict), "capture dictionary required")
    result = _public(capture)
    if result.get("original_result_stdout_receipt") is not None and "original_backend_return" in result:
        raw = result.pop("original_backend_return")
        result["emitted_original_backend_return_summary"] = None if raw is None else {
            key: copy.deepcopy(raw.get(key)) for key in (
                "schema", "status", "success", "message", "nit", "nfev", "njev",
                "actual_finite_raw36_saved", "backend_elapsed_seconds", "raw_K", "raw_h")}
    if include_arrays:
        if isinstance(capture.get("_new_primitive_arrays"), dict):
            result["actually_completed_new_primitive_arrays"] = {
                label: {key: _payload(value) if np.all(np.isfinite(value)) else _raw_numeric(value)
                        for key, value in arrays.items()}
                for label, arrays in capture["_new_primitive_arrays"].items()}
        for private, public in (
                ("_new_coordinate_arrays", "actual_new_coordinate_maps"),
                ("_new_linear_arrays", "actual_new_linear_rows")):
            if isinstance(capture.get(private), dict):
                result[public] = _numeric_record(capture[private])
        if capture.get("_fixed_row_scales") is not None:
            result["actual_fixed_row_scales_values"] = _payload(capture["_fixed_row_scales"])
        if isinstance(capture.get("_initial_full_evaluation"), dict):
            result["actual_initial_full_evaluation"] = _numeric_record(capture["_initial_full_evaluation"])
        if isinstance(capture.get("_last_evaluation_partial"), dict):
            result["actual_last_completed_or_partial_evaluation"] = _numeric_record(
                capture["_last_evaluation_partial"])
        if isinstance(capture.get("_returned_original_units"), dict):
            result["actual_returned_original_unit_rows"] = _numeric_record(capture["_returned_original_units"])
        if capture.get("_last_backend_input") is not None:
            result["actual_last_backend_callback_input"] = _raw_numeric(capture["_last_backend_input"])
        if capture.get("_returned_candidate168") is not None:
            result["actual_constructed_rounded_candidate168"] = _vector(capture["_returned_candidate168"])
    result["values_not_present_in_capture_are_not_filled_or_recomputed"] = True
    result["other_complete_cached_evaluation_arrays_not_promised_as_future_free_input"] = True
    return result


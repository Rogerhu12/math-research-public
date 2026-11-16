#!/usr/bin/env python3
"""R525 paid common R1 ray / joint alpha-R2 model and one new SLSQP call.

Import-only.  The caller owns the scientific clock, source-log authentication,
and one new nonlinear-solver debit.  This module never evaluates field.metric,
scalar_frame, Pi, ordinary geometry, a selected geometric Jacobian, an old
least-squares problem, or an old fixed-alpha LP.  A finite model is not an
actual fourteen-gate receipt.  No function runs at import time.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import time

import numpy as np

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


POLICY = "true58-paid-reflection-ray-joint-alpha-R2-v1"
TARGET_EXACT = "1000/61"
ALPHA_INTERVAL_EXACT = ("1/64", "1/2")
INITIAL_ALPHA_EXACT = "1/4"
VARIABLES = 19
MODES = 17
SLSQP_OPTIONS = {"maxiter": 160, "ftol": 1.e-9, "disp": False}
MAX_EVALUATIONS = 400
SOLVER_SECONDS = 120.
GRID_CONSTRAINTS = (
    "metric_plus", "metric_minus", "positive_Q_lower_bound",
    "spectral_trace_square", "spectral_determinant_sign",
    "spectral_determinant_square")


class JointAlphaR2Limit(RuntimeError):
    """A real local time/evaluation limit; no replacement backend result."""


def definition():
    return {
        "schema": POLICY,
        "problem": "one joint alpha+y17+h nonlinear original172-box problem",
        "accepted_base": "the unchanged actual58 supplied with both paid MODEL records",
        "alpha_interval_exact": list(ALPHA_INTERVAL_EXACT),
        "initial_alpha_exact": INITIAL_ALPHA_EXACT,
        "initial_y": "midpoint of the already-paid alpha=1/4 remaining exact R2 box",
        "target_exact_default": TARGET_EXACT,
        "physical_variables": "alpha,y[0:17],h",
        "backend_variables": "alpha,z[0:17],h; y=s*z in binary64",
        "fixed_y_scale": "s=1/(4*max(abs(exact original R2 spline weights)))",
        "decoded_y_is_not_the_literal_backend_z": True,
        "candidate_y": "exact binary64 decoded y; no hidden higher-precision z*s substitution",
        "physical_norm": "h >= 4*||alpha*P1*xstar+P2*y||infinity",
        "maximum_h": "reuse the original box-sufficient exact bound; no implicit 1/128",
        "metric_budget": "required literal current58 receipt; not the .26 target",
        "metric_rows": "eps*(1+eps-E)-F^2 and eps*(E-1+eps)-F^2",
        "Q": "Horner polynomial for |(U0+alpha*paid_Vxstar) cross T|^2",
        "Schur_quantity": "q_perp^2=E-F^2/G; mathematically Q=G*q_perp^2",
        "G": "unchanged paid actual_G, never replaced by one",
        "floating_Q_and_Schur_are_not_forced_bitwise_equal": True,
        "full_spectrum_rows": "4*K^2*G^2*Q^3-t^2, R, R^2-K^2*G^2*Q*t^2",
        "t_R": "t=a+c*Q; R=K^2*G^2*Q^2+a*c-b^2; R>=0 retained",
        "positive_Q": "Q-G*(1-eps)>=0; mathematically redundant when paid G>=eps",
        "curvature_alpha_degrees": [6, 4, 8],
        "R1_data": "paid Vxstar/Zxstar/Lxstar/Hxxstar, not a full 17x17 quadratic tensor",
        "row_scaling": "positive fixed max(1,abs(initial residual),max abs(initial backend-J row))",
        "row_scales_are_fixed_after_the_first_counted_full_evaluation": True,
        "backend": "one scipy.optimize.minimize(method='SLSQP')",
        "backend_options": copy.deepcopy(SLSQP_OPTIONS),
        "full_evaluation_cap": MAX_EVALUATIONS,
        "solver_seconds_cap": SOLVER_SECONDS,
        "solver_clock": "pre-import charge through raw return and qualification; nonpreemptive checks",
        "same_literal_backend_input_cache": "all completed full value/J evaluations kept in process",
        "original_unit_candidate_filter": "paid-path unsquared four PSD rows with original row tolerance",
        "original_row_tolerance": LP_ROW_TOLERANCE,
        "candidate": "exact base+exact(alpha*xstar*R1)+exact(decoded_y*R2), once rounded",
        "backend_success_is_not_actual_acceptance": True,
        "unreturned_callback_points_are_not_promoted_to_candidates": True,
        "ordinary_calls": 0, "geometric_J_calls": 0, "new_metric_calls": 0,
        "new_frame_calls": 0, "new_Pi_calls": 0, "old_LS_or_LP_calls": 0,
        "actual_gate_calls": 0, "global_infeasibility_or_optimality_certificate": False,
        "API_source": "https://docs.scipy.org/doc/scipy-1.17.0/reference/optimize.minimize-slsqp.html"}


def implementation_hashes():
    names = (
        Path(__file__).name, "frame_metric_current168_reflected_R1_ray.py",
        "frame_metric_current168_ring17.py", "frame_complete_body_extension168.py",
        "frame_complete_body_extension168_joint_selected.py",
        "frame_height_null_coordinates.py")
    root = Path(__file__).parent
    return {name: hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names}


def _public(value):
    return {key: copy.deepcopy(item) for key, item in value.items()
            if not str(key).startswith("_")}


def _numeric_record(value):
    if isinstance(value, np.ndarray):
        return _payload(value) if np.all(np.isfinite(value)) else _raw_numeric(value)
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _numeric_record(item) for key, item in value.items()
                if not str(key).startswith("_")}
    if isinstance(value, (list, tuple)):
        return [_numeric_record(item) for item in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.bool_,)):
        return bool(value)
    if isinstance(value, (float, np.floating)):
        x = float(value)
        return x if math.isfinite(x) else ("NaN" if math.isnan(x) else
                                          ("+Infinity" if x > 0 else "-Infinity"))
    if value is None or isinstance(value, (str, int, bool)):
        return value
    return {"unserialized_type": type(value).__name__, "not_a_recoverable_numeric_value": True}


def _event(sink, kind, **metadata):
    row = {"kind": kind, "status": "started", **copy.deepcopy(metadata)}
    sink.setdefault("events", []).append(row)
    return row


def _dot(x, y):
    return np.einsum("ij,ij->i", x, y)


def _freeze_arrays(value):
    for item in value.values():
        if isinstance(item, np.ndarray):
            _require(np.all(np.isfinite(item)), "finite derived model coefficient required")
            item.setflags(write=False)


def _read_sources(field, state168, ring, ray, cfg, lower, upper, receipt, wall, sink):
    _wall(wall, "joint-alpha.source.entry")
    _context(field)
    q = _array(field.validate_state(state168), (168,), "actual58 state168")
    _require(isinstance(cfg, dict) and isinstance(receipt, dict) and receipt,
             "original cfg and authenticated paid-source receipt required")
    low, high = _bounds(lower, "lower"), _bounds(upper, "upper")
    _require(all(lo <= hi for lo, hi in zip(low, high)), "ordered original172 box")
    _require(all(Q.from_float(float(v)) == v for v in low+high),
             "the actual original box endpoints must remain binary64 rationals")
    physical = tuple(field.full_coefficients(q, exact=True))
    _require(len(physical) == 172 and all(
        lo <= value <= hi for lo, value, hi in zip(low, physical, high)),
        "the actual accepted base must satisfy its original exact172 box")
    _require(isinstance(ring, dict) and ring.get("schema") == PAID_RING_POLICY+"-full-ring-model",
             "complete original paid ring MODEL required")
    rb = ring.get("binding")
    _require(isinstance(rb, dict) and ring.get("binding_sha256") == digest(rb),
             "paid ring binding mismatch")
    source = rb.get("source")
    _require(isinstance(source, dict), "paid original ring source missing")
    expected = {
        "field_definition_sha256": field.definition_sha256,
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "physical_state_sha256": digest(field.identity(q)),
        "state168": array_binding(q), "configuration_sha256": digest(cfg),
        "physical172_exact": [str(x) for x in physical],
        "lower172_exact": [str(x) for x in low],
        "upper172_exact": [str(x) for x in high]}
    _require(all(source.get(key) == value for key, value in expected.items()),
             "paid ring current field/state/configuration/box differs")
    _require(source.get("ring_radial_index") == 141,
             "this paid ray belongs to the original actual58 radial row141")
    _require(_same(_decode_payload(ring.get("state168"), (168,), "ring/state168"), q)
             and ring.get("physical172_exact") == expected["physical172_exact"],
             "paid ring literal independent or physical state changed")
    _require(isinstance(ray, dict) and ray.get("schema") == PAID_RAY_POLICY+"-full-reflected-R1-ray",
             "complete paid reflected-ray MODEL required")
    rs = ray.get("source")
    _require(isinstance(rs, dict)
             and rs.get("paid_ring_model_binding_sha256") == ring["binding_sha256"]
             and rs.get("paid_ring_MODEL_canonical_sha256") == digest(ring),
             "ray must bind this complete original ring MODEL")
    _require(all(rs.get(key) == value for key, value in expected.items())
             and rs.get("ring_radial_index") == source["ring_radial_index"]
             and rs.get("sigma_binary64_exact") == source["sigma_binary64_exact"]
             and rs.get("radial") == source["radial"]
             and rs.get("theta") == source["theta"]
             and rs.get("fixed_metric_binding_sha256") == source["fixed_metric_binding_sha256"],
             "paid ray and original ring use different current definitions")
    metric = receipt.get("paid_ring_metric")
    _require(isinstance(metric, dict) and isinstance(metric.get("source"), dict)
             and metric["source"], "authenticated literal paid ring metric a required")
    aa = metric.get("a_binary64")
    _require(not isinstance(aa, (bool, np.bool_)) and isinstance(
        aa, (int, float, np.integer, np.floating)), "literal finite metric a required")
    aa = float(aa)
    _require(math.isfinite(aa) and aa > 0, "original ring radius must be positive")
    if "a_exact_binary64" in metric:
        _require(Q(metric["a_exact_binary64"]) == Q.from_float(aa),
                 "paid ring a exact and binary64 values disagree")
    if "radial_index" in metric:
        _require(metric["radial_index"] == 141, "paid metric radial index differs")
    summary = ray.get("summary")
    common = summary.get("common_xstar") if isinstance(summary, dict) else None
    _require(isinstance(common, dict) and common.get("exact_J1_pass") is True
             and common.get("exact_nonzero") is True,
             "paid nonzero common J1-qualified ray required")
    xstar = _decode_payload(common.get("xstar17"), (17,), "ray/common-xstar")
    xstar2 = _decode_payload(ray.get("original_weighted_LS_inputs_and_residuals", {}).get(
        "full_xstar17"), (17,), "ray/full-xstar")
    _require(_same(xstar, xstar2) and np.any(xstar != 0),
             "the two original stored ray vectors differ")
    exact = ray.get("exact_radial_embedding")
    _require(isinstance(exact, dict)
             and exact.get("original_paid_R2_definition") == ring.get("exact_radial_embedding")
             and exact.get("sigma_exact") == source["sigma_binary64_exact"],
             "paid complete R0/R1/R2 source differs")
    w1 = tuple(Q(v) for v in exact["R1_weights_exact"])
    w2 = tuple(Q(v) for v in exact["R2_weights_exact"])
    _require(len(w1) == len(w2) == 3 and any(w2), "three literal original spline weights")
    inv = tuple(tuple(Q(v) for v in row) for row in
                exact["inverse_by_spline_row_and_radial_jet_column"])
    mat = tuple(tuple(Q(v) for v in row) for row in exact["basis_jet_matrix_exact"])
    _require(len(inv) == len(mat) == 3 and all(len(row) == 3 for row in inv+mat)
             and tuple(row[1] for row in inv) == w1
             and tuple(row[2] for row in inv) == w2,
             "paid exact inverse columns differ")
    maximum = summary.get("maximum_h")
    _require(isinstance(maximum, dict) and maximum.get("source") == "original172-box-derived"
             and maximum.get("requested_maximum_h_exact") is None,
             "the paid source must retain the complete original-box domain")
    hmax = Q(maximum["effective_maximum_h_exact"])
    _require(hmax == Q(maximum["box_sufficient_maximum_h_exact"]) and hmax > 0,
             "a sufficient positive exact original-box h bound is required")
    seed_rows = [row for row in ray.get("all_seven_fixed_R1_scale_records", [])
                 if row.get("alpha_exact") == INITIAL_ALPHA_EXACT]
    _require(len(seed_rows) == 1, "unique paid alpha=1/4 seed-domain record required")
    seed_domain = seed_rows[0].get("remaining_original_box_and_norm_R2")
    _require(isinstance(seed_domain, dict) and seed_domain.get("all_modes_nonempty") is True
             and Q(seed_domain["maximum_h_exact"]) == hmax
             and len(seed_domain.get("modes", [])) == 17,
             "complete paid alpha=1/4 R2 seed box required")
    seed_intervals = []
    for j, row in enumerate(seed_domain["modes"]):
        _require(row.get("mode") == j and row.get("nonempty") is True,
                 "paid seed modes must retain literal order")
        lo, hi = Q(row["lower_exact"]), Q(row["upper_exact"])
        _require(lo <= hi, "paid seed interval is empty")
        seed_intervals.append((lo, hi))
    source_meta = {
        "schema": POLICY+"-authenticated-input",
        **expected, "ring_radial_index": 141,
        "sigma_binary64_exact": source["sigma_binary64_exact"],
        "radial": copy.deepcopy(source["radial"]),
        "theta": copy.deepcopy(source["theta"]),
        "paid_ring_binding_sha256": ring["binding_sha256"],
        "paid_ray_source": copy.deepcopy(rs),
        "source_receipt": copy.deepcopy(receipt),
        "paid_ring_metric": copy.deepcopy(metric),
        "fixed_metric_binding_sha256": source["fixed_metric_binding_sha256"],
        "ray_xstar17": array_binding(xstar),
        "exact_radial_embedding_sha256": digest(exact),
        "paid_seed_domain_sha256": digest(seed_domain),
        "source_current_point_never_replaced_by_R1_only_state": True}
    sink["source"] = copy.deepcopy(source_meta)
    sink["paid_input_restoration"] = {
        "radius": "literal selected metric_a from the authenticated actual58 CACHE2",
        "base_twojets": "original paid ring MODEL",
        "ray_tables": "original reflected-R1 MODEL",
        "old_LS_Pi_frame_J_metric_or_geometry_calls": 0}
    grids = {}
    sink["_paid_grids"] = grids
    for label in LABELS:
        _wall(wall, "joint-alpha.source."+label)
        old = ring["grids"][label]
        n = int(old["arrays"]["theta"]["shape"][0])
        theta = _decode_payload(old["arrays"]["theta"], (n,), label+"/theta")
        _require(array_binding(theta) == source["theta"][label],
                 "the original full angular grid differs")
        base = {key: _decode_payload(old["position_two_jets_without_X"][key],
                                    (n, 3), label+"/"+key) for key in JETS}
        for key, value in base.items():
            _require(array_binding(value) == rb["grid_position_arrays"][label][key],
                     "paid base twojet is not bound: "+label+"/"+key)
        G = _decode_payload(old["arrays"]["actual_G"], (n,), label+"/actual-G")
        _require(array_binding(G) == rb["grid_arrays"][label]["actual_G"],
                 "paid actual G is not bound")
        new = ray["new_complete_frame_and_vector_tables"][label]
        vectors = {key: _decode_payload(new[key], (n, 3), label+"/"+key)
                   for key in ("R1_Vxstar", "R1_Zxstar", "R1_Lxstar", "R1_Hxxstar")}
        V17 = _decode_payload(new["V17"], (n, 3, 17), label+"/V17")
        grids[label] = {
            "theta": theta, "base": base, "G": G, "V17": V17,
            "V": vectors["R1_Vxstar"], "Z": vectors["R1_Zxstar"],
            "L": vectors["R1_Lxstar"], "H": vectors["R1_Hxxstar"],
            "source_arrays": {
                "theta": array_binding(theta), "actual_G": array_binding(G),
                "V17": array_binding(V17),
                **{key: array_binding(value) for key, value in vectors.items()},
                "base_twojets": {key: array_binding(value) for key, value in base.items()}}}
        sink.setdefault("restored_grid_receipts", {})[label] = {
            "complete_angle_count": n, "source_arrays": copy.deepcopy(grids[label]["source_arrays"])}
    _wall(wall, "joint-alpha.source.complete")
    return (q, physical, low, high, aa, xstar, w1, w2, hmax,
            tuple(seed_intervals), copy.deepcopy(exact), source_meta, grids)


def _polynomial_coefficients(grid, aa, eps):
    base = grid["base"]
    U0, T = base["Xs"], base["Xt"]/aa
    C0, D0 = base["Xst"]/aa, base["Xtt"]/(aa*aa)
    V, Z, L, H, G, V17 = (grid[key] for key in ("V", "Z", "L", "H", "G", "V17"))
    _require(np.all(G >= eps), "the declared metric-implied Q lower bound needs paid G>=eps")
    w0, w1 = np.cross(U0, T), np.cross(V, T)
    coeff = {
        "E": np.stack((_dot(U0, U0), 2*_dot(U0, V), _dot(V, V)), axis=1),
        "F": np.stack((_dot(U0, T), _dot(V, T)), axis=1),
        "Q_cross": np.stack((_dot(w0, w0), 2*_dot(w0, w1), _dot(w1, w1)), axis=1),
        "p_without_y": np.stack((
            _dot(w0, base["Xss"]),
            _dot(w1, base["Xss"])+_dot(w0, L),
            _dot(w1, L)+_dot(w0, H), _dot(w1, H)), axis=1),
        "p_y_constant": np.einsum("ic,icj->ij", w0, V17),
        "p_y_linear": np.einsum("ic,icj->ij", w1, V17),
        "r": np.stack((_dot(w0, C0), _dot(w1, C0)+_dot(w0, Z), _dot(w1, Z)), axis=1),
        "c": np.stack((_dot(w0, D0), _dot(w1, D0)), axis=1),
        "G": G, "Q_redundant_lower_bound": G*(1.-eps)}
    _require(np.all(coeff["Q_cross"][:, 0] > 0), "paid base cross-area must be positive")
    _freeze_arrays(coeff)
    return coeff


def _embedding_from_paid(xstar, w1, w2, physical, low, high, hmax):
    xq = tuple(Q.from_float(float(x)) for x in xstar)
    fixed = [Q(0)]*172
    exact_P2 = [[Q(0) for _ in range(17)] for _ in range(172)]
    entries = []
    for j in range(17):
        for k, row in enumerate(_mode_physical_rows(j)):
            fixed[row] = w1[k]*xq[j]
            exact_P2[row][j] = w2[k]
            entries.append({
                "parameter_column": j, "independent168_row": row, "physical172_row": row,
                "full_spline_index": 9+k, "R1_weight_exact": str(w1[k]),
                "R2_weight_exact": str(w2[k]), "ray_coefficient_exact": str(xq[j]),
                "R1_ray_increment_exact": str(fixed[row])})
    active = tuple(sorted({row["physical172_row"] for row in entries}))
    _require(all(hmax >= 4*max(abs(low[j]-physical[j]), abs(high[j]-physical[j]))
                 for j in active), "paid h upper bound is not sufficient for the original box")
    scale_exact = Q(1)/(4*max(map(abs, w2)))
    scale = float(scale_exact)
    _require(math.isfinite(scale) and scale > 0, "finite positive fixed R2 coordinate scale")
    P1 = np.asarray(list(map(float, fixed)), dtype=np.float64)
    P2 = np.asarray([[float(x) for x in row] for row in exact_P2], dtype=np.float64)
    scales = np.full(17, scale, dtype=np.float64)
    _freeze_arrays({"P1": P1, "P2": P2, "scales": scales})
    return tuple(fixed), tuple(tuple(row) for row in exact_P2), P1, P2, scales, active, entries, {
        "schema": POLICY+"-fixed-backend-coordinate-scale",
        "formula": "1/(4*max(abs(original exact R2 weights)))",
        "intended_scale_exact": str(scale_exact),
        "actual_scale_binary64": scale,
        "actual_scale_exact_binary64": str(Q.from_float(scale)),
        "all_seventeen_scale_values": scales.tolist(),
        "scale_does_not_change_original_physical_norm": True}


def _linear_rows(P1, P2, scales, physical, low, high, hmax):
    rows, rhs, tags = [], [], []
    def add(alpha, ys, h, bound, tag):
        row = np.r_[float(alpha), np.asarray(ys, dtype=np.float64)*scales, float(h)]
        _require(row.shape == (19,) and np.all(np.isfinite(row))
                 and math.isfinite(float(bound)), "finite original physical row")
        rows.append(row)
        rhs.append(float(bound))
        tags.append(tag)
    for j in range(172):
        add(P1[j], P2[j], 0., high[j]-physical[j],
            {"kind": "physical172_box", "physical_index": j, "side": "upper"})
        add(-P1[j], -P2[j], 0., physical[j]-low[j],
            {"kind": "physical172_box", "physical_index": j, "side": "lower"})
        if P1[j] != 0. or np.any(P2[j] != 0.):
            add(4*P1[j], 4*P2[j], -1., 0.,
                {"kind": "complete_physical_norm", "physical_index": j, "side": "plus"})
            add(-4*P1[j], -4*P2[j], -1., 0.,
                {"kind": "complete_physical_norm", "physical_index": j, "side": "minus"})
    zero = np.zeros(17)
    add(-1., zero, 0., -Q(ALPHA_INTERVAL_EXACT[0]), {"kind": "alpha_lower"})
    add(1., zero, 0., Q(ALPHA_INTERVAL_EXACT[1]), {"kind": "alpha_upper"})
    add(0., zero, -1., 0., {"kind": "h_lower"})
    add(0., zero, 1., hmax, {"kind": "h_upper"})
    A, b = np.stack(rows), np.asarray(rhs, dtype=np.float64)
    _freeze_arrays({"A": A, "b": b})
    return A, b, tags


def build_joint_alpha_R2_model(
        field, state168, paid_ring_model, paid_ray_model, cfg, lower172, upper172,
        source_receipt, wall, capture=None, *, metric_budget, target_exact=TARGET_EXACT):
    """Restore paid tables and assemble a genuinely new one-parameter model."""
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty new-model capture required")
    sink.update(schema=POLICY+"-build-capture", status="entered",
                definition=definition(), events=[], completed_new_coefficients={},
                ordinary_calls=0, metric_calls=0, frame_calls=0, Pi_calls=0,
                geometric_J_calls=0, old_solver_calls=0)
    started = time.monotonic()
    try:
        eps = float(metric_budget)
        target = _q(target_exact)
        _require(math.isfinite(eps) and 0. < eps < 1. and target > 0,
                 "finite current metric budget in (0,1) and positive target")
        data = _read_sources(field, state168, paid_ring_model, paid_ray_model, cfg,
                             lower172, upper172, source_receipt, wall, sink)
        (q, physical, low, high, aa, xstar, w1, w2, hmax,
         seed_intervals, radial_definition, source, grids) = data
        _require(Q.from_float(eps) == Q(paid_ray_model["source"]["metric_budget_exact_binary64"])
                 and target == Q(paid_ray_model["source"]["target_exact"]),
                 "new joint problem must retain the original paid metric and curvature targets")
        coefficients = {}
        sink["_new_coefficients"] = coefficients
        for label in LABELS:
            tick = time.monotonic()
            event = _event(sink, "paid-table-polynomial-and-analytic-derivative-coefficients",
                           grid=label)
            try:
                _wall(wall, "joint-alpha.coefficients."+label)
                coefficients[label] = _polynomial_coefficients(grids[label], aa, eps)
                sink["completed_new_coefficients"][label] = {
                    key: array_binding(value) for key, value in coefficients[label].items()}
                event.update(status="complete", elapsed_seconds=time.monotonic()-tick,
                             coefficients=copy.deepcopy(sink["completed_new_coefficients"][label]))
                _wall(wall, "joint-alpha.coefficients."+label+".complete")
            except Exception as error:
                event.update(error=_error(error), elapsed_seconds=time.monotonic()-tick)
                if event["status"] == "started":
                    event["status"] = "raised"
                raise
        embedding = _embedding_from_paid(xstar, w1, w2, physical, low, high, hmax)
        fixed, exact_P2, P1, P2, scales, active, entries, scale_record = embedding
        A, b, rowtags = _linear_rows(P1, P2, scales, physical, low, high, hmax)
        intended_y = tuple((lo+hi)/2 for lo, hi in seed_intervals)
        y_float = np.asarray(list(map(float, intended_y)), dtype=np.float64)
        z0 = y_float/scales
        decoded_y = z0*scales
        alpha0 = float(Q(INITIAL_ALPHA_EXACT))
        actual_seed_y = tuple(Q.from_float(float(v)) for v in decoded_y)
        physical_delta = tuple(Q(INITIAL_ALPHA_EXACT)*fixed[j]+sum(
            exact_P2[j][k]*actual_seed_y[k] for k in range(17)) for j in range(172))
        exact_h0 = 4*max(map(abs, physical_delta))
        h0 = float(exact_h0)
        if Q.from_float(h0) < exact_h0:
            h0 = math.nextafter(h0, math.inf)
        x0 = _array(np.r_[alpha0, z0, h0], (19,), "one literal backend seed")
        seed = {
            "alpha_exact": INITIAL_ALPHA_EXACT,
            "paid_seed_R2_intervals_exact": [[str(lo), str(hi)] for lo, hi in seed_intervals],
            "intended_midpoint_y17_exact": [str(v) for v in intended_y],
            "backend_seed19": _vector(x0),
            "decoded_seed_physical19": _vector(np.r_[alpha0, decoded_y, h0]),
            "decoded_seed_y17_exact_binary64": [str(v) for v in actual_seed_y],
            "decoded_seed_complete_physical_increment_exact": [str(v) for v in physical_delta],
            "decoded_seed_physical_h_exact": str(exact_h0),
            "decoded_seed_exact_box_pass": all(
                lo <= base+d <= hi for lo, base, d, hi in zip(low, physical, physical_delta, high)),
            "h_binary64_rounded_up_if_necessary": Q.from_float(h0) >= exact_h0,
            "seed_curvature_feasibility_claimed": False,
            "one_seed_no_restart_or_projection_solve": True}
        sink["coordinate_scale"] = scale_record
        sink["initial_point"] = copy.deepcopy(seed)
        model = JointAlphaR2Model(
            field, q, cfg, source, radial_definition, physical, low, high, aa,
            xstar, w1, w2, hmax, eps, target, grids, coefficients, fixed,
            exact_P2, P1, P2, scales, active, entries, A, b, rowtags, x0, seed, sink)
        sink.update(status="complete", model_binding_sha256=model.binding_sha256,
                    elapsed_seconds=time.monotonic()-started)
        _wall(wall, "joint-alpha.build.complete")
        return model
    except Exception as error:
        sink.update(status="raised", error=_error(error),
                    elapsed_seconds=time.monotonic()-started, completed_work_not_repeated=True)
        raise


class JointAlphaR2Model:
    """A paid-table finite prediction with one common nonlinear alpha."""
    def __init__(
            self, field, q, cfg, source, radial_definition, physical, low, high, aa,
            xstar, w1, w2, hmax, eps, target, grids, coefficients, fixed,
            exact_P2, P1, P2, scales, active, entries, linear_A, linear_b,
            linear_tags, x0, seed, capture):
        self.field, self.state168, self.cfg = field, q, copy.deepcopy(cfg)
        self.source, self.radial_definition = copy.deepcopy(source), copy.deepcopy(radial_definition)
        self.base_physical172, self.lower172, self.upper172 = physical, low, high
        self.radius, self.xstar, self.w1, self.w2 = aa, xstar, w1, w2
        self.maximum_h_exact, self.eps, self.target_exact = hmax, eps, target
        self.grids, self.coefficients = grids, coefficients
        self.fixed_physical_ray, self.exact_P2 = fixed, exact_P2
        self.P1, self.P2, self.y_scales, self.active, self.entries = P1, P2, scales, active, entries
        self.linear_A, self.linear_b, self.linear_tags = linear_A, linear_b, linear_tags
        self.x0, self.seed, self.capture = x0, seed, capture
        self.solve_attempted = False
        self.solver_sink = None
        self.row_scales = None
        self.row_layout = []
        offset = 0
        for label in LABELS:
            n = len(grids[label]["theta"])
            for component in GRID_CONSTRAINTS:
                self.row_layout.append({
                    "grid": label, "component": component, "offset": offset,
                    "count": n, "theta_array": array_binding(grids[label]["theta"]),
                    "original_angle_order": True})
                offset += n
        self.row_layout.append({
            "component": "original172_box_complete_norm_alpha_h",
            "offset": offset, "count": len(linear_b),
            "tags_sha256": digest(linear_tags)})
        self.constraint_count = offset+len(linear_b)
        self.binding = {
            "schema": POLICY+"-model-binding", "definition": definition(),
            "source": copy.deepcopy(source), "implementation_hashes": implementation_hashes(),
            "metric_budget_binary64": eps, "metric_budget_exact_binary64": str(Q.from_float(eps)),
            "curvature_target_exact": str(target),
            "alpha_interval_exact": list(ALPHA_INTERVAL_EXACT),
            "original_box_sufficient_hmax_exact": str(hmax),
            "paid_xstar17": array_binding(xstar),
            "exact_radial_embedding": copy.deepcopy(radial_definition),
            "physical_embedding_entries": copy.deepcopy(entries),
            "backend_y_scales": array_binding(scales),
            "backend_y_scale_receipt": copy.deepcopy(capture["coordinate_scale"]),
            "source_grid_arrays": {label: copy.deepcopy(grids[label]["source_arrays"])
                                   for label in LABELS},
            "new_polynomial_coefficients": {
                label: {key: array_binding(value) for key, value in coefficients[label].items()}
                for label in LABELS},
            "linear_A": array_binding(linear_A), "linear_b": array_binding(linear_b),
            "linear_row_tags_sha256": digest(linear_tags),
            "constraint_layout": copy.deepcopy(self.row_layout),
            "initial_backend_seed19": array_binding(x0),
            "original_current_point_not_an_unaccepted_R1_point": True}
        self.binding_sha256 = digest(self.binding)

    def assert_context(self):
        self.field._assert_context()
        _require(digest(self.binding) == self.binding_sha256
                 and digest(self.cfg) == self.source["configuration_sha256"]
                 and array_binding(self.state168) == self.source["state168"]
                 and digest(self.field.identity(self.state168)) == self.source["physical_state_sha256"],
                 "new joint model or current field/state/configuration changed")
        for label in LABELS:
            for key, expected in self.binding["new_polynomial_coefficients"][label].items():
                _require(array_binding(self.coefficients[label][key]) == expected,
                         "new polynomial array changed: "+label+"/"+key)
        _require(array_binding(self.linear_A) == self.binding["linear_A"]
                 and array_binding(self.linear_b) == self.binding["linear_b"]
                 and array_binding(self.y_scales) == self.binding["backend_y_scales"],
                 "physical rows or fixed backend coordinate scale changed")

    def decode_backend(self, backend19):
        x = _array(backend19, (19,), "literal backend19")
        decoded = np.r_[x[0], x[1:18]*self.y_scales, x[18]]
        return _array(decoded, (19,), "decoded physical19")

    def _full_value_jacobian(self, backend19, partial):
        """One actual complete new table contraction, no geometric J."""
        x = _array(backend19, (19,), "new evaluation backend19")
        physical = self.decode_backend(x)
        alpha, y = float(physical[0]), physical[1:18]
        K, eps = float(self.target_exact), self.eps
        values, derivatives = [], []
        diagnostics = {}
        partial.update(backend19=_vector(x), decoded_physical19=_vector(physical),
                       completed_grids={}, status="entered")
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            for label in LABELS:
                p = self.coefficients[label]
                G = p["G"]
                Ec, Fc, Qc = p["E"], p["F"], p["Q_cross"]
                E = Ec[:, 0]+alpha*(Ec[:, 1]+alpha*Ec[:, 2])
                E_a = Ec[:, 1]+2*alpha*Ec[:, 2]
                F = Fc[:, 0]+alpha*Fc[:, 1]
                F_a = Fc[:, 1]
                QQ = Qc[:, 0]+alpha*(Qc[:, 1]+alpha*Qc[:, 2])
                Q_a = Qc[:, 1]+2*alpha*Qc[:, 2]
                pc = p["p_without_y"]
                py = p["p_y_constant"]+alpha*p["p_y_linear"]
                pp = (pc[:, 0]+alpha*(pc[:, 1]+alpha*(pc[:, 2]+alpha*pc[:, 3]))
                      +py @ y)
                p_a = (pc[:, 1]+alpha*(2*pc[:, 2]+3*alpha*pc[:, 3])
                       +p["p_y_linear"] @ y)
                rc, cc = p["r"], p["c"]
                rr = rc[:, 0]+alpha*(rc[:, 1]+alpha*rc[:, 2])
                r_a = rc[:, 1]+2*alpha*rc[:, 2]
                cc0 = cc[:, 0]+alpha*cc[:, 1]
                c_a = cc[:, 1]
                aa = G*G*pp-2*G*F*rr+F*F*cc0
                a_a = (G*G*p_a-2*G*(F_a*rr+F*r_a)
                       +2*F*F_a*cc0+F*F*c_a)
                bb = G*rr-F*cc0
                b_a = G*r_a-F_a*cc0-F*c_a
                tt = aa+cc0*QQ
                t_a = a_a+c_a*QQ+cc0*Q_a
                RR = K*K*G*G*QQ*QQ+aa*cc0-bb*bb
                R_a = (2*K*K*G*G*QQ*Q_a+a_a*cc0+aa*c_a-2*bb*b_a)
                M = G[:, None]**2*py
                # Jacobians below are converted once to the fixed backend z coordinates.
                Mz = M*self.y_scales[None, :]
                raw = (
                    eps*(1+eps-E)-F*F,
                    eps*(E-1+eps)-F*F,
                    QQ-p["Q_redundant_lower_bound"],
                    4*K*K*G*G*QQ**3-tt*tt,
                    RR,
                    RR*RR-K*K*G*G*QQ*tt*tt)
                alpha_derivative = (
                    -eps*E_a-2*F*F_a,
                    eps*E_a-2*F*F_a,
                    Q_a,
                    12*K*K*G*G*QQ*QQ*Q_a-2*tt*t_a,
                    R_a,
                    2*RR*R_a-K*K*G*G*(Q_a*tt*tt+2*QQ*tt*t_a))
                y_derivative = (
                    None, None, None,
                    -2*tt[:, None]*Mz,
                    cc0[:, None]*Mz,
                    (2*RR*cc0-2*K*K*G*G*QQ*tt)[:, None]*Mz)
                n = len(E)
                for row, da, dy in zip(raw, alpha_derivative, y_derivative):
                    jac = np.zeros((n, 19), dtype=np.float64)
                    jac[:, 0] = da
                    if dy is not None:
                        jac[:, 1:18] = dy
                    values.append(row)
                    derivatives.append(jac)
                arrays = {
                    "E": E, "F": F, "actual_G": G, "Q_cross_polynomial": QQ,
                    "a_numerator": aa, "b_numerator": bb, "c_numerator": cc0,
                    "t_trace_numerator": tt, "R_determinant_numerator": RR,
                    **dict(zip(GRID_CONSTRAINTS, raw))}
                _require(all(np.all(np.isfinite(item)) for item in arrays.values()),
                         "nonfinite full new polynomial contraction: "+label)
                partial["completed_grids"][label] = arrays
                diagnostics[label] = {
                    "constraint_minima_in_original_polynomial_units": {
                        name: float(np.min(value)) for name, value in zip(GRID_CONSTRAINTS, raw)},
                    "Q_cross_minimum": float(np.min(QQ)),
                    "actual_G_minimum": float(np.min(G)),
                    "no_original_shape_or_actual_gate_receipt": True}
            lin = self.linear_b-self.linear_A @ x
            values.append(lin)
            derivatives.append(-self.linear_A)
            val, jac = np.concatenate(values), np.concatenate(derivatives, axis=0)
            _require(val.shape == (self.constraint_count,)
                     and jac.shape == (self.constraint_count, 19)
                     and np.all(np.isfinite(val)) and np.all(np.isfinite(jac)),
                     "finite complete new inequality vector and analytic Jacobian required")
            partial.update(status="complete", linear_values=lin,
                           full_values=val, full_jacobian_backend=jac)
            diagnostics["linear_original_units"] = {
                "minimum": float(np.min(lin)),
                "maximum_violation": float(max(0., -np.min(lin)))}
            return val, jac, physical, diagnostics

    def summary(self):
        result = {
            "schema": POLICY+"-model-summary", "binding_sha256": self.binding_sha256,
            "physical_variables": 19, "backend_variables": 19,
            "original_common_R2_modes": 17,
            "alpha_interval_exact": list(ALPHA_INTERVAL_EXACT),
            "target_exact": str(self.target_exact), "metric_budget": self.eps,
            "maximum_h_exact": str(self.maximum_h_exact),
            "initial_backend_seed19": _vector(self.x0),
            "initial_point": copy.deepcopy(self.seed),
            "complete_grid_angle_counts": {label: len(self.grids[label]["theta"]) for label in LABELS},
            "constraint_count": self.constraint_count,
            "constraint_layout": copy.deepcopy(self.row_layout),
            "linear_row_counts": {kind: sum(row["kind"] == kind for row in self.linear_tags)
                                  for kind in sorted({row["kind"] for row in self.linear_tags})},
            "source_physical_state_sha256": self.source["physical_state_sha256"],
            "row_scales_established": self.row_scales is not None,
            "row_scales_binding": None if self.row_scales is None else array_binding(self.row_scales),
            "one_solver_attempted": self.solve_attempted,
            "no_new_ordinary_geometry_metric_frame_Pi_or_geometric_J": True,
            "full_R1_quadratic_tensor_claimed": False,
            "backend_success_is_not_actual_fourteen_gate_acceptance": True}
        if self.solver_sink is not None:
            s = self.solver_sink
            raw = s.get("original_backend_return")
            result["solver"] = {
                key: copy.deepcopy(s.get(key)) for key in (
                    "status", "backend_entered", "error", "stop_reason",
                    "local_elapsed_seconds", "full_evaluation_counts",
                    "callback_counts", "original_result_stdout_receipt",
                    "qualified_candidate", "candidate_filter")}
            result["solver"]["original_backend_return_summary"] = None if raw is None else {
                key: copy.deepcopy(raw.get(key)) for key in (
                    "status", "success", "message", "nit", "nfev", "njev",
                    "backend_elapsed_seconds", "scipy_version")}
        return result

    def full_record(self):
        """New coefficients once; paid large vectors remain in their source MODELs."""
        self.assert_context()
        s = self.solver_sink
        raw = None if s is None else s.get("original_backend_return")
        emitted = None if s is None else s.get("original_result_stdout_receipt")
        return {
            "schema": POLICY+"-full-new-model",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "summary": self.summary(),
            "original_actual58_state168": _vector(self.state168),
            "original_actual58_physical172_exact": [str(v) for v in self.base_physical172],
            "new_polynomial_coefficients": {
                label: {key: _payload(value) for key, value in self.coefficients[label].items()}
                for label in LABELS},
            "fixed_backend_y_scales": _vector(self.y_scales),
            "fixed_constraint_row_scales": None if self.row_scales is None else _payload(self.row_scales),
            "linear_row_tags": copy.deepcopy(self.linear_tags),
            "physical_embedding_entries": copy.deepcopy(self.entries),
            "initial_point": copy.deepcopy(self.seed),
            "build_receipt": _public(self.capture),
            "solver_actual_full_evaluation_records": [] if s is None else copy.deepcopy(
                s.get("full_evaluation_records", [])),
            "solver_actual_iteration_records": [] if s is None else copy.deepcopy(
                s.get("iteration_records", [])),
            "solver_original_stdout_receipt": copy.deepcopy(emitted),
            "unemitted_original_backend_return": copy.deepcopy(raw) if emitted is None else None,
            "last_completed_or_partial_new_evaluation": None if s is None else _numeric_record(
                s.get("_last_evaluation_partial", {})),
            "returned_original_unit_filter": None if s is None else _numeric_record(
                s.get("_returned_original_units", {})),
            "paid_frame_Pi_V17_and_original_base_arrays_not_duplicated": True,
            "other_inprocess_callback_cache_arrays_not_saved_for_future_free_reuse": True}

    def candidate_from_physical(self, physical19, backend19):
        """Decode actual binary64 parameters, exact embedding, and one final rounding."""
        raw = _array(physical19, (19,), "actual decoded physical19")
        backend = _array(backend19, (19,), "actual backend19")
        alpha = Q.from_float(float(raw[0]))
        y = tuple(Q.from_float(float(v)) for v in raw[1:18])
        base = tuple(Q.from_float(float(v)) for v in self.state168)
        delta = [Q(0)]*168
        r1 = [Q(0)]*168
        r2 = [Q(0)]*168
        for entry in self.entries:
            row, j = entry["independent168_row"], entry["parameter_column"]
            r1[row] = alpha*Q(entry["R1_ray_increment_exact"])
            r2[row] = Q(entry["R2_weight_exact"])*y[j]
            delta[row] = r1[row]+r2[row]
        ideal = tuple(q+d for q, d in zip(base, delta))
        pd = tuple(delta[:154])+tuple(Q(0) for _ in range(18))
        ideal_physical = tuple(q+d for q, d in zip(self.base_physical172, pd))
        ideal_h = 4*max(map(abs, pd))
        candidate = self.state168.copy()
        for row in self.active:
            candidate[row] = float(ideal[row])
        _require(np.all(np.isfinite(candidate)), "combined exact candidate overflowed binary64")
        candidate = _array(self.field.validate_state(candidate), (168,), "rounded candidate168")
        actual_physical = tuple(self.field.full_coefficients(candidate, exact=True))
        actual_delta = tuple(v-b for v, b in zip(actual_physical, self.base_physical172))
        actual_h = 4*max(map(abs, actual_delta))
        actual_bad = [j for j, (lo, value, hi) in enumerate(
            zip(self.lower172, actual_physical, self.upper172)) if not lo <= value <= hi]
        ideal_bad = [j for j, (lo, value, hi) in enumerate(
            zip(self.lower172, ideal_physical, self.upper172)) if not lo <= value <= hi]
        exact_box = self.field.exact_full_box_decision(
            candidate, np.asarray(list(map(float, self.lower172))),
            np.asarray(list(map(float, self.upper172))))
        _require(bool(exact_box["exact_full_box_pass"]) == (not actual_bad),
                 "canonical exact field box and exact embedded physical box disagree")
        alpha_pass = Q(ALPHA_INTERVAL_EXACT[0]) <= alpha <= Q(ALPHA_INTERVAL_EXACT[1])
        record = {
            "schema": POLICY+"-exact-joint-and-once-rounded-candidate",
            "model_binding_sha256": self.binding_sha256,
            "backend_variable_order": "alpha,z17,h",
            "physical_variable_order": "alpha,decoded-binary64-y17,h",
            "actual_backend_raw19": _vector(backend),
            "decoded_physical_proposal19": _vector(raw),
            "selected_R1_alpha_exact": str(alpha),
            "selected_R1_alpha_binary64": float(alpha),
            "R2_y17_exact_binary64": [str(v) for v in y],
            "raw_backend_h": float(backend[18]),
            "fixed_backend_y_scales": _vector(self.y_scales),
            "decoded_y_uses_binary64_multiplication_before_exact_embedding": True,
            "fixed_R1_coefficients17_exact": [
                str(alpha*Q.from_float(float(v))) for v in self.xstar],
            "R1_independent168_increment_exact": [str(v) for v in r1],
            "R2_independent168_increment_exact": [str(v) for v in r2],
            "unrounded_exact_independent168_increment": [str(v) for v in delta],
            "unrounded_exact_independent168": [str(v) for v in ideal],
            "unrounded_exact_physical172_increment": [str(v) for v in pd],
            "unrounded_exact_physical172": [str(v) for v in ideal_physical],
            "unrounded_exact_h": str(ideal_h),
            "unrounded_exact_box_pass": not ideal_bad,
            "unrounded_exact_box_violating_indices": ideal_bad,
            "unrounded_exact_h_bound_pass": bool(ideal_h <= self.maximum_h_exact),
            "rounded_independent168": _vector(candidate),
            "rounded_physical172_exact": [str(v) for v in actual_physical],
            "rounded_physical172_binary64": _vector(np.asarray(list(map(float, actual_physical)))),
            "rounded_exact_physical172_increment": [str(v) for v in actual_delta],
            "rounded_exact_h": str(actual_h), "rounded_exact_box_decision": exact_box,
            "rounded_exact_h_bound_pass": bool(actual_h <= self.maximum_h_exact),
            "rounded_exact_h_at_most_original_small_1_over_128":
                bool(actual_h <= Q(REFERENCE_SMALL_H_EXACT)),
            "independent_rounding_error_exact": [
                str(Q.from_float(float(v))-u) for v, u in zip(candidate, ideal)],
            "physical_rounding_error_exact": [
                str(v-u) for v, u in zip(actual_physical, ideal_physical)],
            "alpha_original_exact_interval_pass": bool(alpha_pass),
            "candidate_physical_identity_sha256": digest(self.field.identity(candidate)),
            "original_current_base_physical_identity_sha256": self.source["physical_state_sha256"],
            "original_actual_box_and_new_explicit_h_pass":
                bool(alpha_pass and not actual_bad and not ideal_bad
                     and actual_h <= self.maximum_h_exact and ideal_h <= self.maximum_h_exact),
            "rounding": "exact q58 + exact alpha*xstar*R1 + exact decoded-y*R2, each touched row once",
            "no_intermediate_q1_binary64_or_actual_point": True,
            "exact_ring_identity_applies_to_the_unrounded_embedding_only": True,
            "rounded_candidate_claimed_exactly_ring_metric_neutral": False,
            "actual14_feasibility_claimed": False}
        return candidate, record

    def original_unit_filter(self, physical19, partial):
        """Same returned point, original unsquared Schur/normal path, no new field call."""
        raw = _array(physical19, (19,), "returned physical19 for original-unit rows")
        alpha, y, K = float(raw[0]), raw[1:18], float(self.target_exact)
        all_pass, summaries = True, {}
        partial.update(schema=POLICY+"-returned-original-unit-filter", status="entered", grids={})
        for label in LABELS:
            grid, aa = self.grids[label], self.radius
            old, G = grid["base"], grid["G"]
            U = old["Xs"]+alpha*grid["V"]
            Xst = old["Xst"]+aa*alpha*grid["Z"]
            Xss = (old["Xss"]+alpha*grid["L"]+alpha*alpha*grid["H"]
                   +np.einsum("icj,j->ic", grid["V17"], y))
            T = old["Xt"]/aa
            Z12, Z22 = Xst/aa, old["Xtt"]/(aa*aa)
            w = np.cross(U, T)
            QQ = _dot(w, w)
            E, F = _dot(U, U), _dot(U, T)
            _require(np.all(QQ > 0) and np.all(G > 0),
                     "returned candidate has no positive original normal area")
            qarea = np.sqrt(QQ)
            I = np.stack((E, F, F, G), axis=-1).reshape(len(E), 2, 2)
            II = np.stack((_dot(w, Xss), _dot(w, Z12), _dot(w, Z12),
                           _dot(w, Z22)), axis=-1).reshape(len(E), 2, 2)/qarea[:, None, None]
            jets = {"Xs": U, "Xt": old["Xt"], "Xss": Xss, "Xst": Xst, "Xtt": old["Xtt"]}
            shape = _normal_shape(jets, I, II, qarea, aa)
            A, B, C = shape["A"], shape["B"], shape["C"]
            rows = np.stack((2*K+A+C, (K+C)*(K+A)-B*B,
                             2*K-A-C, (K-C)*(K-A)-B*B), axis=1)
            phi = .5*(np.sqrt((E-1)**2+4*F*F)+abs(E-1))
            plus = self.eps*(1+self.eps-E)-F*F
            minus = self.eps*(E-1+self.eps)-F*F
            norm = _operator_norm(A, B, C)
            pc = self.coefficients[label]["Q_cross"]
            Qpoly = pc[:, 0]+alpha*(pc[:, 1]+alpha*pc[:, 2])
            finite = all(np.all(np.isfinite(v)) for v in (
                rows, phi, plus, minus, norm, Qpoly, shape["q_perp_squared"]))
            metric_pass = bool(finite and np.all(plus >= 0.) and np.all(minus >= 0.)
                               and np.all(phi <= self.eps))
            psd_pass = bool(finite and np.min(rows) >= -LP_ROW_TOLERANCE)
            # This is a new finite-model regularity condition, not a substitute actual gate.
            Q_pass = bool(finite and np.all(
                Qpoly-self.coefficients[label]["Q_redundant_lower_bound"] >= -LP_ROW_TOLERANCE))
            passed = metric_pass and psd_pass and Q_pass
            all_pass = bool(all_pass and passed)
            summary = {
                "passed": passed, "metric_quadratics_and_direct_phi_pass": metric_pass,
                "original_unsquared_four_PSD_rows_pass": psd_pass,
                "new_redundant_Q_row_pass": Q_pass,
                "maximum_original_metric_phi": float(np.max(phi)),
                "maximum_operator_norm": float(np.max(norm)),
                "minimum_unsquared_PSD_by_component": np.min(rows, axis=0).tolist(),
                "maximum_original_PSD_violation": float(max(0., -np.min(rows))),
                "original_PSD_row_tolerance": LP_ROW_TOLERANCE,
                "minimum_Q_cross_direct": float(np.min(QQ)),
                "minimum_Schur_q_perp_squared": float(np.min(shape["q_perp_squared"])),
                "maximum_abs_Q_direct_minus_Horner": float(np.max(abs(QQ-Qpoly))),
                "maximum_abs_Q_direct_minus_G_Schur": float(np.max(
                    abs(QQ-G*shape["q_perp_squared"]))),
                "maximum_abs_actual_G_minus_one": float(np.max(abs(G-1))),
                "new_floating_prediction_not_continuous_or_actual14_certificate": True}
            summaries[label] = summary
            partial["grids"][label] = {
                "summary": copy.deepcopy(summary), "original_unsquared_PSD_rows": rows,
                "original_metric_phi": phi, "metric_plus": plus, "metric_minus": minus,
                "A": A, "B": B, "C": C, "Q_cross_direct": QQ, "Q_cross_Horner": Qpoly,
                "q_perp_squared": shape["q_perp_squared"], "actual_G": G,
                "normal": shape["normal"], "actual_I": I, "actual_II": II}
        partial.update(status="complete", passed=bool(all_pass))
        return bool(all_pass), summaries


class _FullEvaluationCache:
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
        _wall(self.wall, "joint-alpha.solver."+str(phase))
        elapsed = time.monotonic()-self.started
        if elapsed >= self.seconds:
            raise JointAlphaR2Limit("the one new solver clock is exhausted: %.17g seconds" % elapsed)

    def touch(self, x, role):
        self.callbacks[role] = self.callbacks.get(role, 0)+1
        self.sink["callback_counts"] = copy.deepcopy(self.callbacks)
        self.sink["_last_backend_input"] = np.asarray(x, dtype=np.float64).copy()
        self.check(role)
        return _array(x, (19,), "backend callback input")

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
            raise JointAlphaR2Limit("the one new full value/analytic-Jacobian budget is exhausted")
        self.counts["started"] += 1
        ordinal = self.counts["started"]
        tick = time.monotonic()
        record = {"ordinal": ordinal, "status": "started", "first_callback_role": role,
                  "backend19": _vector(array), "input_sha256": array_binding(array)["sha256"]}
        self.sink["full_evaluation_records"].append(record)
        partial = {"evaluation_ordinal": ordinal, "status": "entered"}
        self.sink["_last_evaluation_partial"] = partial
        self.sink["full_evaluation_counts"] = copy.deepcopy(self.counts)
        try:
            values, jacobian, physical, diagnostics = self.model._full_value_jacobian(array, partial)
            if ordinal == 1 and role == "initial_full":
                self.sink["_initial_full_evaluation"] = {
                    "status": "original-value-and-Jacobian-returned",
                    "evaluation_ordinal": ordinal, "backend19": array,
                    "decoded_physical19": physical,
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
            scaled_jacobian = jacobian/scales[:, None]
            _require(np.all(np.isfinite(scaled_values)) and np.all(np.isfinite(scaled_jacobian)),
                     "finite scaled full model required")
            for value in (values, jacobian, scaled_values, scaled_jacobian):
                value.setflags(write=False)
            entry = {
                "ordinal": ordinal, "backend": array, "physical": physical,
                "values": values, "jacobian": jacobian,
                "scaled_values": scaled_values, "scaled_jacobian": scaled_jacobian,
                "diagnostics": diagnostics, "partial": partial}
            self.cache[key] = entry
            self.counts["completed"] += 1
            if ordinal == 1 and role == "initial_full":
                self.sink["_initial_full_evaluation"]["status"] = "complete"
            record.update(
                status="complete", decoded_physical19=_vector(physical),
                objective_h=float(array[18]), elapsed_seconds=time.monotonic()-tick,
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
        return float(value[18])

    def objective_jacobian(self, x):
        self.touch(x, "objective_jacobian")
        value = np.zeros(19, dtype=np.float64)
        value[18] = 1.
        return value

    def constraint_value(self, x):
        return self.get(x, "constraint_value")["scaled_values"].copy()

    def constraint_jacobian(self, x):
        return self.get(x, "constraint_jacobian")["scaled_jacobian"].copy()

    def iteration(self, xk):
        # A callback never creates an unrequested scientific evaluation.
        x = self.touch(xk, "iteration")
        entry = self.cache.get(x.tobytes())
        self.sink["iteration_records"].append({
            "ordinal": len(self.sink["iteration_records"])+1,
            "backend19": _vector(x), "objective_h": float(x[18]),
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
            "actual_finite_raw19_saved")}
    public["unemitted_original_backend_return"] = raw if emitted is None else None
    public["evaluation_and_iteration_records_location"] = (
        "solver capture; caller emits joint_alpha_R2_capture_record(include_arrays=True) "
        "as SOLVE_TRACE after this attempt, including on failure")
    public.pop("full_evaluation_records", None)
    public.pop("iteration_records", None)
    return public


def solve_joint_alpha_R2_once(
        model, *, wall, charge_solve, emit=None, capture=None,
        solver_time_limit_seconds=SOLVER_SECONDS, maxiter=160, max_evaluations=MAX_EVALUATIONS):
    """One new analytic-Jac SLSQP attempt.  No restart or hidden fixed-alpha LP."""
    _require(isinstance(model, JointAlphaR2Model), "one new JointAlphaR2Model required")
    _require(not model.solve_attempted, "the one new solver attempt cannot be repeated")
    _require(callable(charge_solve) and callable(wall), "shared charge and clock callbacks required")
    _require(emit is None or callable(emit), "optional emitter must be callable")
    _require(type(maxiter) is int and 0 < maxiter <= SLSQP_OPTIONS["maxiter"]
             and type(max_evaluations) is int and 0 < max_evaluations <= MAX_EVALUATIONS,
             "new iteration and full-evaluation ceilings may not be enlarged")
    seconds = float(solver_time_limit_seconds)
    _require(not isinstance(solver_time_limit_seconds, (bool, np.bool_))
             and math.isfinite(seconds) and 0 < seconds <= SOLVER_SECONDS,
             "new solver time limit must be finite and no greater than120")
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty one-solver capture required")
    sink.update(schema=POLICY+"-one-solver-attempt", status="entered",
                model_binding_sha256=model.binding_sha256,
                backend_entered=False, charged=False, qualified_candidate=False,
                options={"maxiter": maxiter, "ftol": SLSQP_OPTIONS["ftol"], "disp": False},
                maximum_full_evaluations=max_evaluations, solver_time_limit_seconds=seconds,
                no_restart_or_fixed_alpha_inner_LP=True,
                no_unreturned_callback_point_promoted=True,
                original_backend_return=None, original_result_stdout_receipt=None)
    model.solve_attempted = True
    model.solver_sink = sink
    started = time.monotonic()
    cache = None
    candidate, candidate_record = None, None
    try:
        model.assert_context()
        _wall(wall, "joint-alpha.solver.before-charge")
        metadata = {
            "schema": POLICY+"-solver-charge",
            "backend": "scipy.optimize.minimize(method='SLSQP')",
            "model_binding_sha256": model.binding_sha256,
            "backend_variables": 19, "physical_variables": 19,
            "backend_order": "alpha,z17,h", "physical_order": "alpha,decoded-y17,h",
            "constraint_count": model.constraint_count,
            "options": copy.deepcopy(sink["options"]),
            "max_full_value_and_analytic_Jacobian_evaluations": max_evaluations,
            "solver_time_limit_seconds": seconds,
            "one_new_joint_problem_not_a_restarted_old_LP": True}
        sink["charge_receipt"] = copy.deepcopy(charge_solve(metadata))
        sink["charged"] = True
        cache = _FullEvaluationCache(model, wall, started, seconds, max_evaluations, sink)
        cache.check("after-charge-before-import")
        import scipy
        from scipy.optimize import minimize
        sink["scipy_version"] = str(scipy.__version__)
        cache.check("after-import")
        # This is the first charged new full value/J call and fixes the row scales.
        cache.get(model.x0, "initial_full")
        sink["backend_bounds"] = [
            [float(Q(ALPHA_INTERVAL_EXACT[0])), float(Q(ALPHA_INTERVAL_EXACT[1]))],
            *[[None, None] for _ in range(17)], [0., float(model.maximum_h_exact)]]
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
        # Preserve the actual object before metadata conversion, deadlines, or status filters.
        sink["_original_return_object"] = result
        raw_x = result.get("x")
        raw = {
            "schema": POLICY+"-original-nonlinear-backend-return",
            "backend": "scipy.optimize.minimize(method='SLSQP')",
            "scipy_version": str(scipy.__version__),
            "model_binding_sha256": model.binding_sha256,
            "options": copy.deepcopy(sink["options"]),
            "backend_variable_order": "alpha,z17,h",
            "fixed_y_scales": _vector(model.y_scales),
            "actual_raw_backend19": None if raw_x is None else _raw_numeric(raw_x),
            "entire_OptimizeResult_fields": _raw_all_fields(dict(result)),
            "status": None if result.get("status") is None else int(result.get("status")),
            "success": bool(result.get("success", False)),
            "message": str(result.get("message", "")),
            "nit": None if result.get("nit") is None else int(result.get("nit")),
            "nfev": None if result.get("nfev") is None else int(result.get("nfev")),
            "njev": None if result.get("njev") is None else int(result.get("njev")),
            "backend_elapsed_seconds": float(elapsed_backend),
            "raw_return_captured_before_filter": True,
            "returned_QP_multipliers_are_not_a_global_nonlinear_certificate": True,
            "returned_multipliers_scope": (
                "SciPy SLSQP internal-QP approximate KKT multipliers; "
                "not a strict nonlinear separation certificate; bound multipliers not returned"),
            "bound_multipliers_or_unreturned_slacks_not_fabricated": True}
        sink["original_backend_return"] = raw
        sink.update(status="backend-returned", backend_elapsed_seconds=float(elapsed_backend))
        finite_vector = False
        if raw_x is not None:
            arr = np.asarray(raw_x, dtype=np.float64)
            finite_vector = bool(arr.shape == (19,) and np.all(np.isfinite(arr)))
        raw["actual_finite_raw19_saved"] = bool(
            finite_vector and raw["actual_raw_backend19"] is not None
            and raw["actual_raw_backend19"].get("shape") == [19]
            and len(raw["actual_raw_backend19"].get("exact_binary64_flat", [])) == 19)
        if finite_vector:
            decoded = model.decode_backend(arr)
            raw["decoded_physical19"] = _vector(decoded)
            raw["decoded_y17_exact_binary64"] = [
                str(Q.from_float(float(v))) for v in decoded[1:18]]
        else:
            decoded = None
            raw["decoded_physical19"] = None
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
            filter_record = {
                "returned_evaluation_ordinal": entry["ordinal"],
                "maximum_scaled_model_violation": scaled_violation,
                "scaled_model_tolerance": SLSQP_OPTIONS["ftol"],
                "maximum_unscaled_original_linear_violation": linear_violation,
                "original_linear_row_tolerance": LP_ROW_TOLERANCE,
                "scaled_model_pass": bool(scaled_violation <= SLSQP_OPTIONS["ftol"]),
                "original_linear_pass": bool(linear_violation <= LP_ROW_TOLERANCE)}
            sink["candidate_filter"] = filter_record
            cache.check("before-exact-candidate")
            proposed, candidate_record = model.candidate_from_physical(decoded, arr)
            sink["returned_candidate_record"] = copy.deepcopy(candidate_record)
            sink["_returned_candidate168"] = proposed
            cache.check("after-exact-candidate")
            if not (filter_record["scaled_model_pass"] and filter_record["original_linear_pass"]
                    and candidate_record["original_actual_box_and_new_explicit_h_pass"]):
                sink["status"] = "returned-vector-fails-new-model-or-exact-original-box"
            else:
                tick = time.monotonic()
                units = {}
                sink["_returned_original_units"] = units
                try:
                    passed, summaries = model.original_unit_filter(decoded, units)
                    filter_record["original_unsquared_grid_summaries"] = summaries
                    filter_record["original_unsquared_and_metric_pass"] = bool(passed)
                except Exception as error:
                    units.update(status="returned-domain-error", error=_error(error))
                    filter_record["original_unit_error"] = _error(error)
                    filter_record["original_unsquared_and_metric_pass"] = False
                    passed = False
                finally:
                    sink["returned_original_unit_filter_seconds"] = time.monotonic()-tick
                cache.check("after-original-unit-filter")
                if passed:
                    candidate = proposed
                    sink.update(status="new-joint-ring-candidate-needs-whole-body-validation",
                                qualified_candidate=True)
                else:
                    sink["status"] = "returned-vector-fails-original-unsquared-ring-rows"
        cache.check("complete")
    except JointAlphaR2Limit as error:
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
        sink["observed_solver_clock_overrun_seconds"] = max(
            0., sink["local_elapsed_seconds"]-seconds)
        sink["nonpreemptive_solver_clock_checks_not_a_strict_backend_wall_guarantee"] = True
        record = sink.get("returned_candidate_record")
        sink["actual_rounded_candidate168_saved"] = bool(
            isinstance(record, dict)
            and len(record.get("rounded_independent168", {}).get("values", [])) == 168
            and len(record.get("rounded_independent168", {}).get("exact_binary64", [])) == 168)
        sink["actual_physical172_exact_saved"] = bool(
            isinstance(record, dict)
            and len(record.get("rounded_physical172_exact", [])) == 172)
    return {
        "status": sink["status"], "qualified_candidate": bool(sink["qualified_candidate"]),
        "qualified": bool(sink["qualified_candidate"]),
        "candidate168": candidate, "candidate": candidate,
        "candidate_record": copy.deepcopy(candidate_record),
        "report": _solver_public(sink)}


def joint_alpha_R2_capture_record(capture, *, include_arrays=False):
    """Only actually retained source/partial work; never fabricate a missing result."""
    _require(isinstance(capture, dict), "capture dictionary required")
    result = _public(capture)
    for key in ("original_backend_return",):
        if key in result and result.get("original_result_stdout_receipt") is not None:
            raw = result.pop(key)
            result["emitted_original_backend_return_summary"] = None if raw is None else {
                name: copy.deepcopy(raw.get(name)) for name in (
                    "schema", "status", "success", "message", "nit", "nfev", "njev",
                    "actual_finite_raw19_saved", "backend_elapsed_seconds")}
    if include_arrays:
        if capture.get("_fixed_row_scales") is not None:
            result["actual_fixed_row_scales_values"] = _payload(capture["_fixed_row_scales"])
        if isinstance(capture.get("_initial_full_evaluation"), dict):
            result["actual_initial_full_evaluation"] = _numeric_record(
                capture["_initial_full_evaluation"])
        if isinstance(capture.get("_new_coefficients"), dict):
            result["actually_completed_new_polynomial_coefficients"] = {
                label: {key: _payload(value) for key, value in arrays.items()}
                for label, arrays in capture["_new_coefficients"].items()}
        if isinstance(capture.get("_last_evaluation_partial"), dict):
            result["actual_last_completed_or_partial_evaluation"] = _numeric_record(
                capture["_last_evaluation_partial"])
        if isinstance(capture.get("_returned_original_units"), dict):
            result["actual_returned_original_unit_rows"] = _numeric_record(
                capture["_returned_original_units"])
        if capture.get("_last_backend_input") is not None:
            result["actual_last_backend_callback_input"] = _raw_numeric(
                capture["_last_backend_input"])
        if capture.get("_returned_candidate168") is not None:
            result["actual_constructed_rounded_candidate168"] = _vector(
                capture["_returned_candidate168"])
    result["values_not_present_in_capture_are_not_filled_or_recomputed"] = True
    return result




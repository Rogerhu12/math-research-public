#!/usr/bin/env python3
"""One R0-preserving R1/R2 minimax problem on the complete paid suffix.

Import-only.  The external public Actions runner owns all clocks and debits.
The paid free36 ring fiber and fixed-ring prefix102 fiber are closed.  This
module changes the original last51 coefficients through their already paid
34-dimensional exact R0 kernel, and constrains both complete original angular
grids on every original radial row s>=153/200.  No old optimizer, ordinary
geometry, height primitive, old radial inverse, or paid suffix value is run.

New values use the literal paid q_R scalar fields plus the change in the
actual once-rounded coefficients.  This is the same mathematical field with
an explicitly different floating summation order.  A qualified return still
needs the external original whole-body prediction and original fourteen gates.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import tempfile
import time

import numpy as np

from frame_collar_bvp import periodic_operator
from frame_complete_body_extension168 import CompleteBody168Field, array_binding
from frame_complete_body_extension168_joint_selected import _context
from frame_selected_row_radial_jacobian import angular_kernels, virtual_selected_jets, expand_radial_rows
from frame_metric_spectral_recovery import spectral_proposal_rows, spectral_parameter_rows
from frame_curvature_psd import curvature_values, independent_principal_curvatures
from frame_height_null_coordinates import digest
from frame_metric_current168_ring17 import (
    LP_ROW_TOLERANCE, _require, _error, _wall, _q, _bounds, _vector, _payload, _raw_numeric)
from frame_metric_current168_reflected_R1_ray import _raw_all_fields
from frame_metric_current168_fixed_ring_prefix102 import (
    _finite, _same, _numeric, _slice_radial, _derivative_frame_parts, _inward_float)


POLICY = "true58-R1-R2-whole-suffix-v1"
PAID_FREE_POLICY = "true58-free-R1-R2-original-box-curvature-minimax-v1"
PAID_PREFIX_POLICY = "true58-fixed-ring-prefix102-body-repair-v1"
LABELS = ("coarse", "fine")
POSITION_KEYS = ("Xs", "Xt", "Xss", "Xst", "Xtt")
SCALAR_KEYS = ("value", "s", "ss", "theta")
ROW_NAMES = ("metric_plus", "metric_minus", "plus_trace", "plus_determinant", "minus_trace", "minus_determinant")
ACTIVE_ROWS = tuple(range(54, 81))+tuple(range(129, 153))
SUFFIX_LEFT_EXACT = "153/200"
TARGET_EXACT = "1000/61"
VARIABLES = 36
K_COLUMN = 34
H_COLUMN = 35
NORM_WEIGHT = 1.e-6
OWNED_WIDTH = 4
MAX_EVALUATIONS = 240
SOLVER_SECONDS = 180.
SLSQP_OPTIONS = {"maxiter": 120, "ftol": 1.e-9, "disp": False}


class WholeSuffixLimit(RuntimeError):
    """The actual one-solve clock/point limit, never a fabricated return."""


def definition():
    return {
        "schema": POLICY, "accepted_source_index": 58,
        "backend_order": "delta_z34,K,h", "physical_controls": 34,
        "decode": "RN(q58+P*(Q(z_R)+Q(delta_z))); one final coordinate rounding",
        "R0": "the literal paid exact plane relative to accepted58, not a new plane through rounded q_R",
        "initial_point": "delta_z=-z_R,K=58,h=0, exactly the accepted58",
        "objective": "K+1e-6*h", "K_interval_exact": [TARGET_EXACT, "58"],
        "physical_norm": "h>=4*norm_inf(P*(Q(z_R)+Q(delta_z))) over original172 physical coordinates",
        "physical_box": "the full original172 box before and after once rounding",
        "maximum_h": "the unchanged paid original-box sufficient bound",
        "suffix_left_exact": SUFFIX_LEFT_EXACT,
        "suffix_rows": "all21 original radial rows with s>=153/200, including the protected original ring",
        "angular_grids": "both complete original coarse384 and fine768, separately evaluated with their own Pi_N",
        "finite_rows": "all points times two original smooth metric rows plus four original unsquared PSD rows",
        "no_active_row_thinning_or_repair_restart": True,
        "PSD_matrix": "(K*q*I_actual +/- numerator_K)/original_curvature_scale",
        "actual_G_retained": True, "normal_area_is_a_separate_domain_and_qualification_gate": True,
        "original_unsmoothed_eta_and_direct_kappa_also_required": True,
        "value_arithmetic": "paid q_R u/v fields plus original last3 basis times actual rounded coefficient change",
        "same_mathematical_field_not_bitwise_canonical_field_scalar_frame": True,
        "q_R_value_reuse": "literal paid T,jets,e,f,eta,PSD,area,principal arrays; no repeated value call",
        "fixed_radial_rows": "same paid binary64 radial identity beyond both the original exact and stored binary64 support right endpoints",
        "fixed_row_values": "literal paid geometry at every q; current K PSD and K derivatives still assembled",
        "new_q_R_derivative_inputs": "only previously unsaved I/II and derivative-frame parts if requested",
        "basis": "original clamped quintic full columns9,10,11, original knots and zero extensions; no cutoff at.765",
        "new_geometric_J": "original full-angle angular_kernels and complete two-jet chain, only on requested inputs",
        "derivative_input_cache": "actual q/owned-radial-block/family; K-independent physical metric/I/II differentials",
        "final_J_cache": "actual q plus binary64 K; h has only fixed linear derivatives",
        "same_q_new_K_reuses_all_original_angular_and_position_derivative_inputs": True,
        "no_full_grid_by34_position_J_tensor": True,
        "row_scales": "fixed after first requested initial J: max(1,abs(initial values),max(abs(initial Jrow)))",
        "solver": "one scipy.optimize.minimize(method='SLSQP')",
        "options": copy.deepcopy(SLSQP_OPTIONS), "solver_seconds": SOLVER_SECONDS,
        "maximum_new_points": MAX_EVALUATIONS,
        "new_point_cap_counts": "distinct literal backend36 byte inputs, including same q with new K or h",
        "new_geometry_counts_track_actual_q_separately": True,
        "temporary_cache": "same-process public Actions temporary files, no artifact/cache upload or future reuse",
        "qualification": "only actual status0 successful backend return with exact box and all whole-suffix gates",
        "external_after_qualification": "one original whole-body prediction, then at most one original actual pair",
        "finite_success_is_not_reach_or_main_topic_completion": True}


def implementation_hashes():
    names = (Path(__file__).name, "frame_metric_current168_fixed_ring_prefix102.py",
             "frame_metric_current168_ring17.py", "frame_metric_current168_reflected_R1_ray.py",
             "frame_collar_bvp.py", "frame_complete_body_extension168.py",
             "frame_complete_body_extension168_joint_selected.py", "frame_selected_row_radial_jacobian.py",
             "frame_entry_single_q.py", "frame_metric_spectral_recovery.py", "frame_curvature_psd.py")
    return {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}


def _public(value):
    return {key: copy.deepcopy(item) for key, item in value.items() if not str(key).startswith("_")}


def _paid_array(value, shape, name, *, integer=False):
    _require(isinstance(value, dict) and "values" in value, "complete paid array missing: "+name)
    dtype = np.dtype(value.get("dtype"))
    _require((dtype.kind in "iu") if integer else (dtype.kind == "f" and dtype.itemsize == 8),
             "paid array dtype mismatch: "+name)
    a = np.asarray(value["values"], dtype=dtype)
    _require(a.shape == tuple(shape) and np.all(np.isfinite(a)), "paid array shape/finite mismatch: "+name)
    _require(all(value.get(k) == v for k, v in array_binding(a).items()), "paid array hash mismatch: "+name)
    if "exact_binary64" in value:
        _require(a.ndim == 1 and value["exact_binary64"] == [str(Q.from_float(float(x))) for x in a],
                 "paid exact binary64 vector mismatch: "+name)
    a = a.copy(); a.setflags(write=False)
    return a


class _Trace:
    def __init__(self, wall, sink):
        self.wall, self.sink = wall, sink
        self.events = sink.setdefault("component_events", [])
        self.counts = sink.setdefault("component_counts", {})

    def run(self, kind, operation, retain=None, **metadata):
        _wall(self.wall, POLICY+"."+kind+".before")
        count = self.counts.setdefault(kind, {"started": 0, "completed": 0, "failed": 0, "seconds": 0.})
        count["started"] += 1
        event = {"kind": kind, "ordinal": count["started"], "status": "started", **copy.deepcopy(metadata)}
        self.events.append(event); tick = time.monotonic()
        try:
            answer = operation()
            if retain is not None:
                retain(answer)
            event["status"] = "complete"; count["completed"] += 1
        except Exception as error:
            event.update(status="raised", error=_error(error)); count["failed"] += 1
            raise
        finally:
            event["seconds"] = time.monotonic()-tick
            count["seconds"] += event["seconds"]
        _wall(self.wall, POLICY+"."+kind+".after")
        return answer


class _TemporaryArrays:
    """Byte-preserving cache only in this public scientific process."""
    def __init__(self, wall, sink):
        self.wall, self.sink = wall, sink
        self.directory = tempfile.TemporaryDirectory(prefix="visible-whole-suffix-")
        self.index = 0
        sink["temporary_cache"] = {"writes": 0, "reads": 0, "bytes_written": 0,
            "io_seconds": 0., "only_this_process": True, "uploaded_or_future_free": False}

    def save(self, value, kind):
        _wall(self.wall, POLICY+".temporary-cache.before-save")
        tick = time.monotonic(); arrays = {}
        def flatten(item):
            if isinstance(item, np.ndarray):
                key = "a"+str(len(arrays)); arrays[key] = item
                return {"__array__": key}
            if isinstance(item, dict):
                return {key: flatten(v) for key, v in item.items()}
            if isinstance(item, (tuple, list)):
                return {"__list__": [flatten(v) for v in item]}
            return item
        structure = flatten(value)
        path = Path(self.directory.name)/(str(self.index)+"-"+kind+".npz")
        self.index += 1
        try:
            np.savez(path, **arrays)
            receipt = {"path": str(path), "structure": structure}
            log = self.sink["temporary_cache"]
            log["writes"] += 1; log["bytes_written"] += path.stat().st_size
        finally:
            self.sink["temporary_cache"]["io_seconds"] += time.monotonic()-tick
        _wall(self.wall, POLICY+".temporary-cache.after-save")
        return receipt

    def load(self, receipt):
        _wall(self.wall, POLICY+".temporary-cache.before-load")
        tick = time.monotonic()
        try:
            with np.load(receipt["path"], allow_pickle=False) as archive:
                def restore(item):
                    if isinstance(item, dict) and set(item) == {"__array__"}:
                        a = archive[item["__array__"]]; a.setflags(write=False); return a
                    if isinstance(item, dict) and set(item) == {"__list__"}:
                        return [restore(v) for v in item["__list__"]]
                    if isinstance(item, dict):
                        return {key: restore(v) for key, v in item.items()}
                    return item
                answer = restore(receipt["structure"])
            self.sink["temporary_cache"]["reads"] += 1
        finally:
            self.sink["temporary_cache"]["io_seconds"] += time.monotonic()-tick
        _wall(self.wall, POLICY+".temporary-cache.after-load")
        return answer


def _tangent_frame(fields):
    """The original target_frame T formulas without irrelevant beta/V work."""
    u, v = fields["u"]["value"], fields["v"]["value"]
    psi = fields["_theta"]+u; zero = np.zeros_like(u)
    N = np.stack((np.cos(psi), np.sin(psi), zero), axis=-1)
    H = np.stack((-np.sin(psi), np.cos(psi), zero), axis=-1)
    ez = np.stack((zero, zero, np.ones_like(u)), axis=-1)
    c = 1/np.sqrt(1+v*v)
    Tu, Tv = -c[..., None]*N, (c**3)[..., None]*(ez-v[..., None]*H)
    Tuu, Tuv = -c[..., None]*H, (v*c**3)[..., None]*N
    Tvv = ((2*v*v-1)*c**5)[..., None]*H-(3*v*c**5)[..., None]*ez
    us, vs = fields["u"]["s"], fields["v"]["s"]
    return {"T": c[..., None]*H+(v*c)[..., None]*ez,
        "Ts": us[..., None]*Tu+vs[..., None]*Tv,
        "Tss": ((us*us)[..., None]*Tuu+(2*us*vs)[..., None]*Tuv+(vs*vs)[..., None]*Tvv
                 +fields["u"]["ss"][..., None]*Tu+fields["v"]["ss"][..., None]*Tv),
        "Ttheta": (1+fields["u"]["theta"])[..., None]*Tu+fields["v"]["theta"][..., None]*Tv,
        "Tpart": {"u": Tu, "v": Tv},
        "Ts_value_part": {"u": us[..., None]*Tuu+vs[..., None]*Tuv,
                          "v": us[..., None]*Tuv+vs[..., None]*Tvv}}


def _new_last3_basis(field, radial):
    """Only missing original full B9,B10,B11 jets; no old inverse or first6."""
    from scipy.interpolate import BSpline
    source = field.original_field._direct_single.source
    basis = source.field_basis
    _require(basis.count == 9 and not basis.endpoint_weight and basis.full.k == 5,
             "literal original unweighted nine retained quintics required")
    entry = field.original_field._direct_single.entry
    _require(np.all(radial >= entry.left+entry.length), "all new suffix rows must be beyond entry weights")
    full = basis.full
    last = BSpline(full.t, full.c[:, 9:12], full.k, extrapolate=False, axis=full.axis)
    inside = ((radial > basis.left) & (radial < basis.right))[:, None]
    values = []
    for j in range(3):
        value = np.zeros((len(radial), 3))
        value[inside[:, 0]] = last(radial[inside[:, 0]], nu=j)
        values.append(_finite(value, (len(radial), 3), "last3 jet"+str(j)))
    return values, {"original_knots": _vector(np.asarray(full.t)),
        "original_support_right_binary64": float(basis.right),
        "original_support_right_exact_binary64": str(Q.from_float(float(basis.right))),
        "full_spline_indices": [9, 10, 11], "degree": 5,
        "original_zero_extensions": True, "entry_weights_exactly_one_on_this_suffix": True,
        "old_first6_radial_and_old_angular_arrays_not_recomputed": True}


def _linear_rows(P, base, seed_delta, lower, upper, hmax, target_lower):
    rows, rhs, tags = [], [], []
    def add(coeff, k, h, bound, tag):
        rows.append(np.r_[coeff, float(k), float(h)]); rhs.append(float(bound)); tags.append(tag)
    zero = np.zeros(34)
    for j in range(172):
        center = base[j]+seed_delta[j]
        add(P[j], 0, 0, upper[j]-center, {"kind": "physical172_box", "index": j, "side": "upper"})
        add(-P[j], 0, 0, center-lower[j], {"kind": "physical172_box", "index": j, "side": "lower"})
        if np.any(P[j] != 0.):
            add(4*P[j], 0, -1, -4*seed_delta[j], {"kind": "norm", "index": j, "side": "plus"})
            add(-4*P[j], 0, -1, 4*seed_delta[j], {"kind": "norm", "index": j, "side": "minus"})
    add(zero, -1, 0, -target_lower, {"kind": "K_lower"})
    add(zero, 1, 0, Q(58), {"kind": "K_upper"})
    add(zero, 0, -1, Q(0), {"kind": "h_lower"})
    add(zero, 0, 1, hmax, {"kind": "h_upper"})
    A = _finite(np.stack(rows), (len(rows), 36), "shifted linear A")
    b = _finite(rhs, (len(rows),), "shifted linear b")
    return A, b, tags


def _curvature_differentials(data, a, values):
    """K-independent portion of the original curvature_parameter_jacobian chain."""
    scale = np.broadcast_to(np.asarray(a, dtype=float), values["q"].shape)
    _require(np.array_equal(scale, values["scale"]), "original curvature derivative scale changed")
    dA = data["jac_Xs"]
    dT = data["jac_Xt"]/scale[..., None, None]
    dU = data["jac_Xss"]
    dV = data["jac_Xst"]/scale[..., None, None]
    dW = data["jac_Xtt"]/scale[..., None, None]**2
    dot = lambda left, right: np.einsum("...c,...cn->...n", left, right)
    dw = np.moveaxis(np.cross(np.moveaxis(dA, -1, -2), values["T"][..., None, :])
        +np.cross(values["A"][..., None, :], np.moveaxis(dT, -1, -2)), -2, -1)
    return {"dq": dot(values["w"], dw)/values["q"][..., None],
        "dE": 2*dot(values["A"], dA),
        "dF": dot(values["T"], dA)+dot(values["A"], dT),
        "dG": 2*dot(values["T"], dT),
        "de": dot(values["U"], dw)+dot(values["w"], dU),
        "df": dot(values["V"], dw)+dot(values["w"], dV),
        "dk": dot(values["W"], dw)+dot(values["w"], dW)}


def _curvature_rows_from_differentials(values, differentials, K, scale):
    """Only new K-dependent row assembly; all physical differentials are cached."""
    d = differentials; tau = 1/K
    def pair(metric, derivative, second):
        base = d["dq"]*values[metric][:, None]+values["q"][:, None]*d[derivative]
        return np.stack((base+tau*d[second], base-tau*d[second]), axis=1)
    dh11, dh12, dh22 = pair("E", "dE", "de"), pair("F", "dF", "df"), pair("G", "dG", "dk")
    dtrace = dh11+dh22
    ddet = values["h22"][..., None]*dh11+values["h11"][..., None]*dh22-2*values["h12"][..., None]*dh12
    four = np.stack((dtrace[:, 0], ddet[:, 0], dtrace[:, 1], ddet[:, 1]), axis=1)
    factor = K/scale
    return four*np.asarray((factor, factor*factor, factor, factor*factor))[None, :, None]


class R1R2WholeSuffixModel:
    def __init__(self):
        self.status = "not-built"; self.solve_attempted = False; self.solver_sink = None
        self.row_scales = None; self.initial_entry = None; self.last_entry = None
        self.geometry_cache = {}; self.jacobian_cache = {}
        self.derivative_input_cache = {}
        self.paid_curvature_part_cache = {}; self.paid_metric_part_cache = {}
        self.loaded_geometry = None; self.loaded_geometry_key = None
        self.loaded_J = None; self.loaded_J_key = None
        self.full_point_counts = {"started": 0, "completed": 0, "failed": 0, "paid_seed_hits": 0, "cache_hits": 0}
        self.jacobian_counts = {"started": 0, "completed": 0, "failed": 0, "cache_hits": 0}
        self.derivative_input_counts = {"started": 0, "completed": 0, "failed": 0, "cache_hits": 0}

    def assert_context(self):
        self.field._assert_context()
        _require(self.field.definition_sha256 == self.binding["field_definition_sha256"]
                 and self.field.coordinate_definition_sha256 == self.binding["coordinate_definition_sha256"]
                 and digest(self.cfg) == self.binding["configuration_sha256"], "original field/cfg changed")
        _wall(self.wall, POLICY+".context")

    def point_from_backend(self, backend, *, include_record=False):
        x = _finite(backend, (36,), "literal backend36")
        z = tuple(a+Q.from_float(float(b)) for a, b in zip(self.seed_z_exact, x[:34]))
        delta = tuple(sum(c*v for c, v in zip(row, z)) for row in self.exact_P)
        ideal = list(self.accepted_independent_exact)
        candidate = self.accepted_state168.copy()
        for j in ACTIVE_ROWS:
            ideal[j] += delta[j]; candidate[j] = float(ideal[j])
        _require(np.all(np.isfinite(candidate)), "finite once-rounded candidate required")
        if not include_record:
            return candidate
        physical = tuple(self.field.full_coefficients(candidate, exact=True))
        ideal_physical = tuple(a+b for a, b in zip(self.accepted_physical, delta))
        after_delta = tuple(a-b for a, b in zip(physical, self.accepted_physical))
        before_bad = [j for j, (lo, v, hi) in enumerate(zip(self.lower172, ideal_physical, self.upper172)) if not lo <= v <= hi]
        after_bad = [j for j, (lo, v, hi) in enumerate(zip(self.lower172, physical, self.upper172)) if not lo <= v <= hi]
        K, h = Q.from_float(float(x[34])), Q.from_float(float(x[35]))
        norm = 4*max(map(abs, delta)); rounded_norm = 4*max(map(abs, after_delta))
        interval = self.target_exact <= K <= Q(58) and 0 <= h <= self.maximum_h_exact
        record = {"schema": POLICY+"-exact-once-rounded-candidate", "model_binding_sha256": self.binding_sha256,
            "actual_backend_raw36": _vector(x), "backend_order": "delta_z34,K,h",
            "absolute_original_z34_exact": [str(v) for v in z],
            "unrounded_independent168_exact": [str(v) for v in ideal],
            "unrounded_physical172_exact": [str(v) for v in ideal_physical],
            "unrounded_physical172_increment_exact": [str(v) for v in delta],
            "rounded_independent168": _vector(candidate), "rounded_physical172_exact": [str(v) for v in physical],
            "rounding_difference_independent168_exact": [str(Q.from_float(float(v))-a) for v, a in zip(candidate, ideal)],
            "physical_increment_from_accepted58_exact": [str(v) for v in after_delta],
            "unrounded_original172_box_pass": not before_bad, "rounded_original172_box_pass": not after_bad,
            "unrounded_box_violating_indices": before_bad, "rounded_box_violating_indices": after_bad,
            "original_exact_box_pass": bool(not before_bad and not after_bad),
            "K_exact": str(K), "h_exact": str(h), "K_h_exact_interval_pass": bool(interval),
            "unrounded_exact_physical_norm": str(norm), "rounded_exact_physical_norm": str(rounded_norm),
            "backend_norm_epigraph_exact_pass": bool(norm <= h), "backend_h_minus_exact_norm": str(h-norm),
            "original_sufficient_hmax_pass": bool(norm <= self.maximum_h_exact and rounded_norm <= self.maximum_h_exact),
            "original_box_and_K_h_pass": bool(interval and not before_bad and not after_bad
                and norm <= self.maximum_h_exact and rounded_norm <= self.maximum_h_exact),
            "norm_acceptance_is_original_unscaled_linear_tolerance_not_a_claim_of_exact_h_coverage": True,
            "exact_R0_plane_preserved_in_unrounded_physical_increment": True,
            "rounded_candidate_not_claimed_exactly_in_that_plane": True,
            "same_original_full_support_and_frozen_height_metric": True,
            "physical_state_sha256": digest(self.field.identity(candidate)),
            "original_actual58_physical_state_sha256": self.binding["accepted_physical_state_sha256"],
            "whole_body_prediction_and_actual14_not_yet_evaluated": True}
        return candidate, record

    def _new_fields(self, q, label, indices):
        fields = {"_theta": self.thetas[label][None, :]}
        for name, columns, modes in (("u", range(54, 81), 9), ("v", range(129, 153), 8)):
            # Actual once-rounded coordinate difference; no ideal control is used as a substitute.
            delta = np.asarray([float(Q.from_float(float(q[i]))-Q.from_float(float(self.ring_candidate168[i])))
                                for i in columns]).reshape(3, modes)
            family = self.families[label][name]
            fields[name] = {}
            for order, key in enumerate(("value", "s", "ss")):
                fields[name][key] = self.seed_fields[label][name][key][indices]+np.einsum(
                    "ri,ik,tk->rt", self.last3_radial[order][indices], delta, family["angular"])
            fields[name]["theta"] = self.seed_fields[label][name]["theta"][indices]+np.einsum(
                "ri,ik,tk->rt", self.last3_radial[0][indices], delta, family["angular_first"])
        return fields

    def _grid_summary(self, label, grid, K, rows):
        eta, principal, area = grid["eta"], grid["principal"], grid["curvature"]["q"]
        e_at = np.unravel_index(int(np.argmax(eta)), eta.shape)
        k_at = np.unravel_index(int(np.argmax(abs(principal))), principal.shape)
        maximum_eta, maximum_k = float(eta[e_at]), float(abs(principal[k_at]))
        minima = np.min(rows, axis=(0, 1)); minimum_area = float(np.min(area))
        gates = {"strict_metric_decrease_budget": maximum_eta <= self.metric_budget,
            "original_unsquared_four_PSD_rows_at_returned_K": bool(np.min(minima) >= -self.curvature_row_tolerance),
            "original_direct_curvature_at_returned_K": maximum_k <= K+self.direct_curvature_tolerance,
            "original_hard58_curvature": maximum_k <= self.cap+self.direct_curvature_tolerance,
            "original_regular_normal_area": minimum_area > self.area_floor}
        return {"grid": label, "radial_count": len(self.radial), "theta_count": len(self.thetas[label]),
            "maximum_eta": maximum_eta, "metric_budget": self.metric_budget,
            "eta_attainer": {"radial_index": int(self.radial_ids[e_at[0]]), "theta_index": int(e_at[1]),
                "s": float(self.radial[e_at[0]]), "theta": float(self.thetas[label][e_at[1]])},
            "maximum_absolute_principal_curvature": maximum_k, "K": K,
            "curvature_attainer": {"radial_index": int(self.radial_ids[k_at[0]]), "theta_index": int(k_at[1]),
                "principal_index": int(k_at[2]), "s": float(self.radial[k_at[0]]),
                "theta": float(self.thetas[label][k_at[1]])},
            "scaled_PSD_minima": dict(zip(ROW_NAMES[2:], map(float, minima))),
            "minimum_normal_area": minimum_area, "gates": gates,
            "all_metric_curvature_area_gates_pass": bool(all(gates.values())),
            "finite_regrouped_predictor_not_canonical_wholebody_or_continuous_certificate": True}

    def _paid_seed_curvature_inputs(self, paid, indices):
        """Only previously unsaved algebraic I/II inputs; do not remake paid rows/q/kappa."""
        jets = paid["jets"]; a = self.metric["a"][indices, None]
        A, T = jets["Xs"], jets["Xt"]/a[..., None]
        U, V, W = jets["Xss"], jets["Xst"]/a[..., None], jets["Xtt"]/a[..., None]**2
        w = np.cross(A, T)
        dot = lambda p, r: np.einsum("...c,...c->...", p, r)
        E, F, G = dot(A, A), dot(A, T), dot(T, T)
        e, f, k = dot(w, U), dot(w, V), dot(w, W)
        q = paid["normal_area"]
        I = np.stack((E, F, F, G), axis=-1).reshape(E.shape+(2, 2))
        N = np.stack((e, f, f, k), axis=-1).reshape(E.shape+(2, 2))
        return {"A": A, "T": T, "U": U, "V": V, "W": W, "w": w, "q": q,
            "E": E, "F": F, "G": G, "e": e, "f": f, "k": k,
            "actual_I": I, "numerator_K": N, "actual_II": N/q[..., None, None],
            "scale": np.broadcast_to(a, q.shape), "area_floor": self.area_floor,
            "tau": 1/self.cap, "paid_q_rows_and_principal_were_not_recomputed": True}

    def _paid_curvature_part(self, label, part, indices, trace, work):
        key = (label, part)
        if key not in self.paid_curvature_part_cache:
            saved = _slice_radial(self.seed_grids[label], indices, len(self.radial))
            value = trace.run("new_unsaved_paid_seed_I_II_inputs",
                lambda: self._paid_seed_curvature_inputs(saved, indices),
                lambda v: work.__setitem__("new_paid_"+part+"_I_II_inputs", v),
                grid=label, part=part, original_radial_ids=self.radial_ids[indices].tolist())
            self.paid_curvature_part_cache[key] = value
        return self.paid_curvature_part_cache[key]

    def _paid_metric_part(self, label, part, indices, trace, work):
        key = (label, part)
        if key not in self.paid_metric_part_cache:
            saved = self.seed_grids[label]
            value = trace.run("new_rows_from_paid_metric_inputs", lambda: np.moveaxis(spectral_proposal_rows(
                saved["e"][indices], saved["f"][indices], self.metric_budget, self.epsilon), 0, -1),
                lambda v: work.__setitem__("new_paid_"+part+"_metric_proposal_rows", v),
                grid=label, part=part, original_radial_ids=self.radial_ids[indices].tolist())
            self.paid_metric_part_cache[key] = value
        return self.paid_metric_part_cache[key]

    def _join_radial_parts(self, mutable, fixed):
        # Both disjoint parts come from complete returned arrays.  No unfilled
        # buffer is published; their indices partition all literal21 rows.
        answer = np.empty((len(self.radial),)+mutable.shape[1:], dtype=mutable.dtype)
        answer[self.mutable_radial_indices] = mutable
        answer[self.fixed_radial_indices] = fixed
        return answer

    def _join_curvature_parts(self, mutable, fixed):
        keys = ("A", "T", "U", "V", "W", "w", "q", "E", "F", "G", "e", "f", "k",
                "actual_I", "numerator_K", "actual_II", "scale")
        answer = {key: self._join_radial_parts(mutable[key], fixed[key]) for key in keys}
        answer.update(area_floor=self.area_floor, tau=1/self.cap)
        return answer

    def _geometry(self, q, sink):
        key = q.tobytes()
        if key == self.loaded_geometry_key:
            self.full_point_counts["cache_hits"] += 1
            sink["_last_complete_geometry"] = self.loaded_geometry
            return self.loaded_geometry
        if key in self.geometry_cache:
            self.full_point_counts["cache_hits"] += 1
            result = self.temporary.load(self.geometry_cache[key])
            self.loaded_geometry_key, self.loaded_geometry = key, result
            sink["_last_complete_geometry"] = result
            return result
        trace = _Trace(self.wall, sink)
        is_paid = _same(q, self.ring_candidate168)
        if is_paid:
            self.full_point_counts["paid_seed_hits"] += 1
        else:
            self.full_point_counts["started"] += 1
        ordinal = self.full_point_counts["started"]
        partial = {"schema": POLICY+"-geometry-partial", "status": "entered", "state168": q,
            "new_geometry_ordinal": None if is_paid else ordinal, "paid_q_R_reuse": bool(is_paid),
            "completed_grids": {}, "working_grid": None}
        sink["_last_geometry_partial"] = partial
        tick = time.monotonic()
        try:
            grids = {}
            for label in LABELS:
                work = {"grid": label, "status": "entered"}; partial["working_grid"] = work
                mi, fi = self.mutable_radial_indices, self.fixed_radial_indices
                work.update(new_value_original_radial_ids=self.radial_ids[mi].tolist(),
                            literal_paid_fixed_original_radial_ids=self.radial_ids[fi].tolist())
                saved = self.seed_grids[label]
                fixed_curvature = self._paid_curvature_part(label, "fixed", fi, trace, work)
                fixed_metric_rows = self._paid_metric_part(label, "fixed", fi, trace, work)
                if is_paid:
                    fields = {"_theta": self.thetas[label][None, :], **self.seed_fields[label]}
                    mutable_curvature = self._paid_curvature_part(label, "mutable", mi, trace, work)
                    c = self._join_curvature_parts(mutable_curvature, fixed_curvature)
                    # No target_frame, Pi, metric norm, area, PSD, or principal call at q_R.
                    grid = {"fields": fields, "frame": None, "primitives": None,
                        "jets": saved["jets"], "T": saved["T"], "e": saved["e"], "f": saved["f"],
                        "eta": saved["eta"], "principal": saved["principal"], "curvature": c,
                        "scaled_PSD_cap": saved["scaled_PSD_cap"], "paid_original_arrays": True,
                        "frame_radial_indices": None,
                        "metric_rows": self._join_radial_parts(
                            self._paid_metric_part(label, "mutable", mi, trace, work), fixed_metric_rows)}
                    work["paid_original_value_arrays_reused_without_recalculation"] = True
                else:
                    fields = trace.run("new_scalar_increment_fields", lambda label=label: self._new_fields(q, label, mi),
                                       lambda v: work.__setitem__("scalar_fields_on_mutable_rows", v), grid=label,
                                       original_radial_ids=self.radial_ids[mi].tolist(), geometry_ordinal=ordinal)
                    frame = trace.run("new_tangent_frame", lambda: _tangent_frame(fields),
                                      lambda v: work.__setitem__("frame", v), grid=label, geometry_ordinal=ordinal)
                    primitives = {}; work["primitive_arrays"] = primitives
                    for name in ("T", "Ts", "Tss"):
                        trace.run("new_complete_theta_primitive", lambda name=name: periodic_operator(frame[name], -1),
                                  lambda v, name=name: primitives.__setitem__(name, v),
                                  grid=label, geometry_ordinal=ordinal, source_array=name)
                    a, ap, app = (self.metric[name][mi, None, None] for name in ("a", "a_s", "a_ss"))
                    def assemble():
                        U = ap*primitives["T"]+a*primitives["Ts"]
                        U[..., 2] += self.height["b"][mi, None]
                        B = app*primitives["T"]+2*ap*primitives["Ts"]+a*primitives["Tss"]
                        B[..., 2] += self.height["b_s"][mi, None]
                        return {"Xs": U, "Xt": a*frame["T"], "Xss": B,
                            "Xst": ap*frame["T"]+a*frame["Ts"], "Xtt": a*frame["Ttheta"]}
                    jets = trace.run("new_position_two_jets_without_X", assemble,
                                     lambda v: work.__setitem__("position_jets", v), grid=label, geometry_ordinal=ordinal)
                    T, U = frame["T"], jets["Xs"]
                    e, f = np.sum(U*U, axis=-1)-1., np.sum(U*T, axis=-1)
                    eta = (abs(e)+np.hypot(e, 2*f))/2
                    work.update(metric_e=e, metric_f=f, metric_eta=eta)
                    c = trace.run("new_original_curvature_values", lambda: curvature_values(
                        jets, self.metric["a"][mi, None], 1/self.cap, area_floor=self.area_floor),
                        lambda v: work.__setitem__("curvature_inputs", v), grid=label, geometry_ordinal=ordinal)
                    principal = trace.run("new_direct_principal_curvatures", lambda: independent_principal_curvatures(c),
                                          lambda v: work.__setitem__("principal_curvatures", v), grid=label, geometry_ordinal=ordinal)
                    factor = self.cap/self.curvature_scale
                    scaled = c["rows"]*np.asarray((factor, factor*factor, factor, factor*factor))
                    full_fields = {"_theta": self.thetas[label][None, :]}
                    for name in ("u", "v"):
                        full_fields[name] = {key: self._join_radial_parts(fields[name][key],
                            self.seed_fields[label][name][key][fi]) for key in SCALAR_KEYS}
                    grid = {"fields": full_fields, "frame": frame, "frame_radial_indices": mi,
                        "primitives": primitives, "primitive_radial_indices": mi,
                        "jets": {key: self._join_radial_parts(jets[key], saved["jets"][key][fi]) for key in POSITION_KEYS},
                        "T": self._join_radial_parts(T, saved["T"][fi]),
                        "e": self._join_radial_parts(e, saved["e"][fi]), "f": self._join_radial_parts(f, saved["f"][fi]),
                        "eta": self._join_radial_parts(eta, saved["eta"][fi]),
                        "principal": self._join_radial_parts(principal, saved["principal"][fi]),
                        "curvature": self._join_curvature_parts(c, fixed_curvature),
                        "scaled_PSD_cap": self._join_radial_parts(scaled, saved["scaled_PSD_cap"][fi]),
                        "metric_rows": self._join_radial_parts(np.moveaxis(spectral_proposal_rows(
                            e, f, self.metric_budget, self.epsilon), 0, -1), fixed_metric_rows),
                        "paid_original_arrays": False}
                grid["literal_fixed_geometry_radial_indices"] = fi
                grid["literal_fixed_geometry_original_radial_ids"] = self.radial_ids[fi]
                _require(all(np.all(np.isfinite(grid[k])) for k in ("T", "e", "f", "eta", "principal", "scaled_PSD_cap", "metric_rows")),
                         "finite complete suffix arrays required")
                grids[label] = grid; work.update(status="complete")
                partial["completed_grids"][label] = grid; partial["working_grid"] = None
            answer = {"state168": q, "grids": grids, "paid_q_R_reuse": bool(is_paid),
                "new_geometry_ordinal": None if is_paid else ordinal}
            # Commit complete scientific arrays before a potentially failing cache write.
            partial.update(status="complete", geometry=answer)
            self.loaded_geometry_key, self.loaded_geometry = key, answer
            sink["_last_complete_geometry"] = answer
            if not is_paid:
                self.full_point_counts["completed"] += 1
            self.geometry_cache[key] = self.temporary.save(answer, "geometry")
            return answer
        except Exception as error:
            partial["error"] = _error(error)
            if partial.get("status") != "complete":
                partial["status"] = "raised"
                if not is_paid:
                    self.full_point_counts["failed"] += 1
            else:
                partial["completed_arrays_retained_before_cache_or_clock_failure"] = True
            raise
        finally:
            partial["seconds"] = time.monotonic()-tick
            sink["new_geometry_counts"] = copy.deepcopy(self.full_point_counts)

    def _curvature_at_K(self, grid, K):
        c = grid["curvature"]
        tau = 1/K; q = c["q"]
        # q_R has no previously saved h11/h12/h22; only these new derivative inputs are formed.
        if K == self.cap and all(key in c for key in ("h11", "h12", "h22", "rows")):
            return c, grid["scaled_PSD_cap"]
        h11 = np.stack((q*c["E"]+tau*c["e"], q*c["E"]-tau*c["e"]), axis=-1)
        h12 = np.stack((q*c["F"]+tau*c["f"], q*c["F"]-tau*c["f"]), axis=-1)
        h22 = np.stack((q*c["G"]+tau*c["k"], q*c["G"]-tau*c["k"]), axis=-1)
        factor = K/self.curvature_scale
        factors = np.asarray((factor, factor*factor, factor, factor*factor))
        if K == self.cap:
            # Reuse both literal fixed rows and already computed mutable rows.
            scaled = grid["scaled_PSD_cap"]
            rows = scaled/factors
        else:
            trace = h11+h22; det = h11*h22-h12*h12
            rows = np.stack((trace[..., 0], det[..., 0], trace[..., 1], det[..., 1]), axis=-1)
            scaled = rows*factors
        answer = dict(c)
        answer.update(h11=h11, h12=h12, h22=h22, rows=rows, tau=tau)
        return answer, scaled

    def _value(self, backend, sink):
        x = _finite(backend, (36,), "new backend value input")
        _require(x[34] > 0, "positive actual backend K required")
        q = self.point_from_backend(x)
        geometry = self._geometry(q, sink)
        values, summaries = [], {}
        for label in LABELS:
            grid = geometry["grids"][label]
            _, scaled = self._curvature_at_K(grid, float(x[34]))
            values.append(np.concatenate((grid["metric_rows"], scaled), axis=-1).ravel())
            summaries[label] = self._grid_summary(label, grid, float(x[34]), scaled)
        values.append(self.linear_b-self.linear_A@x)
        raw = _finite(np.concatenate(values), (self.constraint_count,), "whole-suffix residual")
        return {"backend": x, "state168": q, "values": raw, "summaries": summaries,
            "whole_suffix_pass": bool(all(s["all_metric_curvature_area_gates_pass"] for s in summaries.values())),
            "geometry_key": q.tobytes(), "jacobian_key": q.tobytes()+np.asarray(x[34], dtype=np.float64).tobytes()}

    def _jacobian(self, entry, sink):
        key = entry["jacobian_key"]
        if key == self.loaded_J_key:
            self.jacobian_counts["cache_hits"] += 1
            return self.loaded_J
        if key in self.jacobian_cache:
            self.jacobian_counts["cache_hits"] += 1
            J = self.temporary.load(self.jacobian_cache[key])
            self.loaded_J_key, self.loaded_J = key, J
            return J
        self.assert_context()
        self.jacobian_counts["started"] += 1
        ordinal = self.jacobian_counts["started"]
        geometry = self._geometry(entry["state168"], sink)
        K = float(entry["backend"][34]); factor = K/self.curvature_scale
        J = np.empty((self.constraint_count, 36), dtype=np.float64)
        partial = {"status": "entered", "ordinal": ordinal, "backend36": entry["backend"],
            "matrix": J, "completed_column_blocks": [], "working_kernel_arrays": None}
        sink["_last_jacobian_partial"] = partial
        trace = _Trace(self.wall, sink); tick = time.monotonic()
        try:
            offset = 0
            for label in LABELS:
                grid = geometry["grids"][label]
                nr, nt = len(self.radial), len(self.thetas[label])
                cfull, _ = self._curvature_at_K(grid, K)
                # K changes every geometric row's PSD problem, including rows
                # whose exact original control two-jets vanish.  Never freeze
                # their K58 PSD or their K derivative at another K.
                E, F, G, q = (cfull[name] for name in ("E", "F", "G", "q"))
                h11, h12, h22 = (cfull[name]*factor for name in ("h11", "h12", "h22"))
                dtrace = q*(E+G)/self.curvature_scale
                ddet = (q/self.curvature_scale)[..., None]*(E[..., None]*h22+G[..., None]*h11-2*F[..., None]*h12)
                dk = np.stack((np.zeros_like(q), np.zeros_like(q), dtrace, ddet[..., 0], dtrace, ddet[..., 1]), axis=-1)
                J[offset:offset+nr*nt*6, 34] = dk.ravel(); J[offset:offset+nr*nt*6, 35] = 0.
                partial["completed_column_blocks"].append({"grid": label, "family": "K_h_all_original_rows",
                    "row_start": offset, "row_stop": offset+nr*nt*6, "column_start": 34, "column_stop": 36})
                for fixed_ri in self.fixed_radial_indices:
                    first_row, last_row = offset+int(fixed_ri)*nt*6, offset+(int(fixed_ri)+1)*nt*6
                    J[first_row:last_row, :34] = 0.
                    partial["completed_column_blocks"].append({"grid": label, "family": "exact_original_support_zero",
                        "row_start": first_row, "row_stop": last_row, "column_start": 0, "column_stop": 34,
                        "zero_is_the_proved_control_derivative_not_unfilled_memory": True,
                        "original_radial_id": int(self.radial_ids[fixed_ri])})
                for begin in range(0, len(self.mutable_radial_indices), OWNED_WIDTH):
                    _wall(self.wall, POLICY+".J.block")
                    owned = self.mutable_radial_indices[begin:begin+OWNED_WIDTH]
                    end = int(owned[-1])+1
                    count = len(owned)*nt; ri = np.repeat(np.arange(len(owned)), nt); ti = np.tile(np.arange(nt), len(owned))
                    global_ri = owned[ri]
                    row_start, row_stop = offset+int(owned[0])*nt*6, offset+end*nt*6
                    fields, frame = None, None
                    metric = {name: v[owned] for name, v in self.metric.items()}
                    small = {name: grid["jets"][name][global_ri, ti] for name in POSITION_KEYS}
                    small["T"] = grid["T"][global_ri, ti]
                    cv = {name: (v[global_ri, ti] if isinstance(v, np.ndarray) and v.shape[:2] == (nr, nt) else v)
                          for name, v in cfull.items()}
                    e, f = grid["e"][global_ri, ti], grid["f"][global_ri, ti]
                    for name, first, stop, physical_rows in (("u", 0, 18, list(range(54, 81))),
                                                           ("v", 18, 34, list(range(129, 153)))):
                        derivative_key = (entry["geometry_key"], label, begin, end, name)
                        if derivative_key in self.derivative_input_cache:
                            self.derivative_input_counts["cache_hits"] += 1
                            d = self.temporary.load(self.derivative_input_cache[derivative_key])
                        else:
                            self.derivative_input_counts["started"] += 1
                            try:
                                if fields is None:
                                    fields = _slice_radial(grid["fields"], owned, nr)
                                    if grid["frame"] is None:
                                        frame = trace.run("new_paid_seed_derivative_frame_parts", lambda: _derivative_frame_parts(fields),
                                            lambda v: partial.__setitem__("working_derivative_frame", v), grid=label,
                                            original_radial_ids=self.radial_ids[owned].tolist())
                                    else:
                                        frame_ids = np.asarray(grid["frame_radial_indices"], dtype=int)
                                        frame = _slice_radial(grid["frame"], np.searchsorted(frame_ids, owned), len(frame_ids))
                                family = self.families[label][name]
                                kernels = trace.run("new_full_angle_J_kernels", lambda name=name, family=family: angular_kernels(
                                    fields, frame, name, family["angular"], family["angular_first"], second=True),
                                    lambda v: partial.__setitem__("working_kernel_arrays", v), grid=label, family=name,
                                    original_radial_ids=self.radial_ids[owned].tolist(), jacobian_ordinal=ordinal)
                                virtual = trace.run("new_virtual_position_J_inputs", lambda: virtual_selected_jets(
                                    kernels, ri, ti, metric, second=True),
                                    lambda v: partial.__setitem__("working_virtual_position_J", v), grid=label, family=name)
                                data = dict(small); data.update({"jac_"+key: v for key, v in virtual.items()})
                                U, T = small["Xs"], small["T"]
                                de = 2*np.einsum("ic,icn->in", U, virtual["Xs"])
                                df = np.einsum("ic,icn->in", T, virtual["Xs"])+np.einsum("ic,icn->in", U, virtual["T"])
                                differentials = _curvature_differentials(data, self.metric["a"][global_ri], cv)
                                differentials["metric0"] = spectral_parameter_rows(e, f, de, df, np.zeros(count, dtype=int), self.epsilon)
                                differentials["metric1"] = spectral_parameter_rows(e, f, de, df, np.ones(count, dtype=int), self.epsilon)
                                d = {key: expand_radial_rows(value, self.last3_radial, global_ri)
                                    @self.P[np.asarray(physical_rows), first:stop] for key, value in differentials.items()}
                                _require(all(value.shape == (count, stop-first) and np.all(np.isfinite(value)) for value in d.values()),
                                         "complete finite K-independent physical differentials required")
                                partial["working_contracted_physical_differentials"] = d
                                self.derivative_input_cache[derivative_key] = self.temporary.save(d, "physical-differentials")
                                self.derivative_input_counts["completed"] += 1
                                partial["working_kernel_arrays"] = None
                                partial.pop("working_virtual_position_J", None)
                                del kernels, virtual, data, de, df, differentials
                            except Exception:
                                self.derivative_input_counts["failed"] += 1
                                raise
                        cj = trace.run("new_K_dependent_PSD_J_assembly", lambda: _curvature_rows_from_differentials(
                            cv, d, K, self.curvature_scale),
                            lambda v: partial.__setitem__("working_K_dependent_PSD_J", v), grid=label, family=name, K=K)
                        six = np.concatenate((d["metric0"][:, None, :], d["metric1"][:, None, :], cj), axis=1)
                        contracted = six.reshape(count*6, stop-first)
                        _require(contracted.shape == (count*6, stop-first) and np.all(np.isfinite(contracted)),
                                 "finite complete original R0-kernel J block required")
                        J[row_start:row_stop, first:stop] = contracted
                        partial["completed_column_blocks"].append({"grid": label, "family": name,
                            "row_start": row_start, "row_stop": row_stop, "column_start": first, "column_stop": stop})
                        partial["working_kernel_arrays"] = None
                        partial.pop("working_contracted_physical_differentials", None)
                        partial.pop("working_K_dependent_PSD_J", None)
                        del d, cj, six, contracted
                    partial.pop("working_derivative_frame", None)
                offset += nr*nt*6
            J[offset:] = -self.linear_A
            partial["completed_column_blocks"].append({"family": "original_linear_rows",
                "row_start": offset, "row_stop": self.constraint_count, "column_start": 0, "column_stop": 36})
            _require(offset == self.nonlinear_constraint_count and np.all(np.isfinite(J)), "complete finite36 Jacobian required")
            J.setflags(write=False); partial.update(status="complete", matrix_binding=array_binding(J))
            self.jacobian_counts["completed"] += 1
            self.loaded_J_key, self.loaded_J = key, J
            self.jacobian_cache[key] = self.temporary.save(J, "J")
            return J
        except Exception as error:
            partial["error"] = _error(error)
            if partial.get("status") != "complete":
                partial["status"] = "raised"; self.jacobian_counts["failed"] += 1
            else:
                partial["completed_J_retained_before_cache_or_clock_failure"] = True
            raise
        finally:
            partial["seconds"] = time.monotonic()-tick
            sink["new_J_counts"] = copy.deepcopy(self.jacobian_counts)
            sink["K_independent_derivative_input_counts"] = copy.deepcopy(self.derivative_input_counts)

    def summary(self):
        return {"schema": POLICY+"-model-summary", "status": self.status, "binding_sha256": self.binding_sha256,
            "variables": 36, "physical_R1_R2_controls": 34, "constraint_count": self.constraint_count,
            "nonlinear_constraint_count": self.nonlinear_constraint_count,
            "suffix_radial_ids": self.radial_ids.tolist(), "suffix_radial_count": len(self.radial),
            "new_value_and_physical_J_original_radial_ids": self.radial_ids[self.mutable_radial_indices].tolist(),
            "literal_paid_fixed_geometry_original_radial_ids": self.radial_ids[self.fixed_radial_indices].tolist(),
            "fixed_rows_still_have_current_K_PSD_and_K_derivatives": True,
            "theta_counts": {label: len(self.thetas[label]) for label in LABELS},
            "initial_backend_seed36": _vector(self.x0), "metric_budget": self.metric_budget,
            "maximum_h_exact": str(self.maximum_h_exact), "K_interval_exact": [str(self.target_exact), "58"],
            "backend_K_lower_binary64": self.target_lower, "backend_K_lower_exact_binary64": str(Q.from_float(self.target_lower)),
            "new_geometry_counts": copy.deepcopy(self.full_point_counts), "new_J_counts": copy.deepcopy(self.jacobian_counts),
            "K_independent_derivative_input_counts": copy.deepcopy(self.derivative_input_counts),
            "all_suffix_rows_enter_solver": True, "new_last3_radial_basis": copy.deepcopy(self.basis_receipt),
            "same_mathematical_original_field_different_floating_summation_order": True,
            "paid_q_R_T_jets_metric_PSD_area_principal_are_read_only": True,
            "qualified_return_only_authorizes_external_canonical_wholebody_prediction": True,
            "actual14_and_reach_not_claimed": True,
            "initial_summaries": None if self.initial_entry is None else copy.deepcopy(self.initial_entry["summaries"]),
            "last_summaries": None if self.last_entry is None else copy.deepcopy(self.last_entry["summaries"])}

    def full_record(self):
        return {"schema": POLICY+"-full-model", "definition": definition(), "summary": self.summary(),
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "build_receipt": _public(self.build_sink),
            "accepted_state168": _vector(self.accepted_state168), "paid_unaccepted_q_R168": _vector(self.ring_candidate168),
            "paid_original_z_R34": _vector(self.seed_z), "exact_physical_P172x34": [[str(v) for v in row] for row in self.exact_P],
            "original_lower172_exact": [str(v) for v in self.lower172], "original_upper172_exact": [str(v) for v in self.upper172],
            "new_original_last3_radial_jets": [_payload(v) for v in self.last3_radial],
            "new_shifted_linear_A": _payload(self.linear_A), "new_shifted_linear_b": _payload(self.linear_b),
            "linear_row_tags": copy.deepcopy(self.linear_tags),
            "paid_input_arrays_referenced_in_source_receipt_not_duplicated": True,
            "actual_initial_last_values_and_J_are_in_separate_SOLVE_TRACE": True,
            "temporary_intermediate_cache_is_not_published_or_future_free_input": True}


def build_R1_R2_whole_suffix_model(
        field, accepted_state168, ring_candidate168, paid_free_model, paid_free_solution, paid_prefix_model,
        cfg, lower172, upper172, source_receipt, wall, capture=None, *, metric_budget, charge_prepare):
    """Restore pinned full records, then pay once for only genuinely missing inputs."""
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty new whole-suffix build capture required")
    _require(callable(wall) and callable(charge_prepare), "external clock and one prepare charge required")
    sink.update(schema=POLICY+"-build-capture", status="entered", source_receipt=copy.deepcopy(source_receipt))
    model = R1R2WholeSuffixModel(); sink["_object_model"] = model
    model.field, model.wall, model.build_sink = field, wall, sink
    tick = time.monotonic()
    try:
        _wall(wall, POLICY+".build.entry"); _context(field)
        _require(isinstance(field, CompleteBody168Field) and field.metric_free == 0, "original fixed-g complete168 field required")
        _require(isinstance(cfg, dict) and isinstance(source_receipt, dict) and source_receipt, "original cfg and authenticated receipts required")
        _require(paid_free_model.get("schema") == PAID_FREE_POLICY+"-full-new-model"
                 and paid_prefix_model.get("schema") == PAID_PREFIX_POLICY+"-full-model", "both original complete MODEL records required")
        model.accepted_state168 = _finite(field.validate_state(accepted_state168), (168,), "accepted58")
        model.ring_candidate168 = _finite(field.validate_state(ring_candidate168), (168,), "paid unaccepted q_R")
        q58 = _paid_array(paid_free_model["original_actual58_state168"], (168,), "free MODEL q58")
        qr_record = paid_free_solution["candidate_record"]
        qr = _paid_array(qr_record["rounded_independent168"], (168,), "free solution q_R")
        _require(_same(q58, model.accepted_state168) and _same(qr, model.ring_candidate168), "source state vector disagreement")
        _require(_same(_paid_array(paid_prefix_model["accepted_state168"], (168,), "prefix q58"), q58)
                 and _same(_paid_array(paid_prefix_model["unaccepted_ring_seed168"], (168,), "prefix q_R"), qr), "prefix states disagree")
        model.lower172, model.upper172 = _bounds(lower172, "lower"), _bounds(upper172, "upper")
        _require(all(a <= b for a, b in zip(model.lower172, model.upper172)), "ordered original172 box required")
        _require([str(v) for v in model.lower172] == paid_prefix_model["lower172_exact"]
                 and [str(v) for v in model.upper172] == paid_prefix_model["upper172_exact"], "original172 box changed")
        model.accepted_physical = tuple(field.full_coefficients(q58, exact=True))
        _require([str(v) for v in model.accepted_physical] == paid_free_model["original_actual58_physical172_exact"], "original physical q58 changed")
        model.accepted_independent_exact = tuple(Q.from_float(float(v)) for v in q58)
        model.exact_P = tuple(tuple(Q(v) for v in row) for row in paid_free_model["exact_physical_coordinate_maps"]["P"])
        _require(len(model.exact_P) == 172 and all(len(row) == 34 for row in model.exact_P), "paid P172x34 layout required")
        model.P = _paid_array(paid_free_model["actual_float_coordinate_maps"]["P"], (172, 34), "paid float P")
        model.coordinate_record = copy.deepcopy(paid_free_model["physical_coordinate_definition"])
        raw_free = _paid_array(qr_record["actual_backend_raw36"], (36,), "paid original raw36")
        _require(qr_record.get("backend_order") == "z34,K,h"
                 and qr_record.get("exact_R0_plane_preserved_in_unrounded_physical_increment") is True,
                 "literal original exact R0 free36 record required")
        model.seed_z = _finite(raw_free[:34], (34,), "paid z_R34")
        model.seed_z_exact = tuple(Q.from_float(float(v)) for v in model.seed_z)
        seed_delta = tuple(sum(c*v for c, v in zip(row, model.seed_z_exact)) for row in model.exact_P)
        _require([str(v) for v in seed_delta] == qr_record["unrounded_exact_physical172_increment"], "paid exact affine source increment mismatch")
        model.cfg = copy.deepcopy(cfg)
        _require(digest(cfg) == paid_prefix_model["binding"]["configuration_sha256"], "original cfg digest changed")
        model.cap = float(Q(cfg["fixed_hard_curvature_cap_exact"]))
        model.curvature_scale = float(Q(cfg["curvature_scale_exact"]))
        model.area_floor = float(cfg["normal_area_numerical_floor"])
        model.curvature_row_tolerance = float(cfg["curvature_row_tolerance"])
        model.direct_curvature_tolerance = float(cfg["direct_curvature_tolerance"])
        model.epsilon = float(Q(cfg["metric_proposal_epsilon_exact"]))
        model.metric_budget = float(metric_budget)
        _require(model.cap == 58. and all(math.isfinite(v) and v > 0 for v in
                    (model.curvature_scale, model.epsilon, model.metric_budget))
                 and all(math.isfinite(v) and v >= 0 for v in
                    (model.area_floor, model.curvature_row_tolerance, model.direct_curvature_tolerance)), "original positive targets required")
        _require(Q.from_float(model.metric_budget) == Q(paid_prefix_model["binding"]["metric_budget_exact_binary64"]), "strict metric budget changed")
        model.target_exact = Q(TARGET_EXACT)
        _require(model.target_exact == Q(paid_free_model["binding"]["curvature_lower_target_exact"]), "original target changed")
        model.target_lower = _inward_float(model.target_exact, True)
        model.maximum_h_exact = Q(paid_free_model["binding"]["original_box_sufficient_hmax_exact"])
        _require(model.maximum_h_exact > 0, "paid sufficient positive h bound required")
        model.maximum_h_float = _inward_float(model.maximum_h_exact, False)
        inputs = paid_prefix_model["new_paid_input"]
        nr = int(inputs["radial"]["shape"][0])
        radial = _paid_array(inputs["radial"], (nr,), "prefix full radial")
        ids = np.asarray([i for i, s in enumerate(radial) if Q.from_float(float(s)) >= Q(SUFFIX_LEFT_EXACT)], dtype=np.int64)
        _require(len(ids) == 21 and 141 in ids, "the complete original21-row suffix required")
        model.radial_ids = ids; model.radial = _finite(radial[ids], (21,), "whole suffix radial")
        model.metric = {name: _finite(_paid_array(inputs["fixed_metric"][name], (nr,), name)[ids], (21,), "suffix "+name)
                        for name in ("a", "a_s", "a_ss")}
        model.height = {name: _finite(_paid_array(inputs["fixed_height_derivatives"][name], (nr,), name)[ids], (21,), "suffix "+name)
                        for name in ("b", "b_s")}
        _require(np.all(model.metric["a"] > 0), "original fixed positive metric scale required")
        model.thetas, model.seed_fields, model.families, model.seed_grids = {}, {}, {}, {}
        for label, nt in (("coarse", 384), ("fine", 768)):
            th = _paid_array(inputs["theta"][label], (nt,), label+" original theta")
            model.thetas[label] = th; model.seed_fields[label] = {}; model.families[label] = {}
            for name, modes in (("u", 9), ("v", 8)):
                model.seed_fields[label][name] = {key: _finite(_paid_array(
                    inputs["source_scalar_fields"][label][name][key], (nr, nt), label+"/"+name+"/"+key)[ids],
                    (21, nt), "suffix scalar "+key) for key in SCALAR_KEYS}
                family = inputs["original_families"][label][name]
                model.families[label][name] = {key: _paid_array(family[key], (nt, modes), label+"/"+name+"/"+key)
                                              for key in ("angular", "angular_first")}
            saved = paid_prefix_model["fixed_suffix_full_arrays"][label]
            saved_ids = _paid_array(saved["radial_ids"], (21,), label+" suffix ids", integer=True)
            _require(np.array_equal(saved_ids, ids) and _same(_paid_array(saved["theta"], (nt,), label+" suffix theta"), th), "paid suffix association mismatch")
            model.seed_grids[label] = {
                "jets": {key: _paid_array(saved["position_two_jets_without_X"][key], (21, nt, 3), label+"/"+key) for key in POSITION_KEYS},
                "T": _paid_array(saved["T"], (21, nt, 3), label+"/T"),
                "e": _paid_array(saved["metric_e"], (21, nt), label+"/e"),
                "f": _paid_array(saved["metric_f"], (21, nt), label+"/f"),
                "eta": _paid_array(saved["metric_eta"], (21, nt), label+"/eta"),
                "normal_area": _paid_array(saved["normal_area"], (21, nt), label+"/area"),
                "principal": _paid_array(saved["principal_curvatures"], (21, nt, 2), label+"/principal"),
                "scaled_PSD_cap": _paid_array(saved["scaled_PSD_rows"], (21, nt, 4), label+"/PSD")}
        sink["source_restore_complete"] = True
        sink["prepare_charge_receipt"] = copy.deepcopy(charge_prepare({"schema": POLICY+"-prepare-charge",
            "new_last3_radial_basis_through_order2": 1, "new_shifted_linear_model": 1,
            "old_angular_or_first6_basis_calls": 0, "new_old_rank_or_inverse_calls": 0,
            "new_initial_geometry_calls_in_builder": 0, "paid_suffix_value_recalculations": 0}))
        trace = _Trace(wall, sink)
        model.last3_radial, model.basis_receipt = trace.run("new_missing_last3_radial_basis",
            lambda: _new_last3_basis(field, model.radial), lambda v: sink.__setitem__("_new_last3_radial", v[0]))
        paid_radial_definition = paid_free_model["binding"]["literal_paid_threejet_embedding"]["original_paid_R2_definition"]
        model.support_right_exact = Q(paid_radial_definition["knots_exact"][-1])
        _require(model.support_right_exact == Q("423/500") and paid_radial_definition["full_spline_indices"] == [9, 10, 11],
                 "original exact last-three support identity required")
        binary_right = Q(model.basis_receipt["original_support_right_exact_binary64"])
        fixed_mask = np.asarray([Q.from_float(float(s)) >= model.support_right_exact
            and Q.from_float(float(s)) >= binary_right for s in model.radial], dtype=bool)
        model.fixed_radial_indices = np.flatnonzero(fixed_mask)
        model.mutable_radial_indices = np.flatnonzero(~fixed_mask)
        _require(len(model.mutable_radial_indices) > 0
                 and np.array_equal(model.mutable_radial_indices, np.arange(len(model.mutable_radial_indices))),
                 "same ordered original radial identities must give a mutable prefix and fixed terminal rows")
        model.fixed_row_receipt = {"original_support_right_exact": str(model.support_right_exact),
            "original_support_right_exact_binary64": str(binary_right),
            "classification": "Q(original binary64 s)>=both right endpoints; no sampled-near-zero test",
            "original_fixed_radial_ids": model.radial_ids[model.fixed_radial_indices].tolist(),
            "original_mutable_radial_ids": model.radial_ids[model.mutable_radial_indices].tolist(),
            "fixed_s_exact_binary64": [str(Q.from_float(float(model.radial[i]))) for i in model.fixed_radial_indices],
            "both_grids_keep_all21_rows_and_current_K_constraints": True}
        sink["fixed_radial_row_reuse"] = copy.deepcopy(model.fixed_row_receipt)
        model.linear_A, model.linear_b, model.linear_tags = trace.run("new_shifted_exact_physical_linear_rows",
            lambda: _linear_rows(model.P, model.accepted_physical, seed_delta, model.lower172, model.upper172,
                                 model.maximum_h_exact, model.target_lower),
            lambda v: sink.__setitem__("_new_linear_arrays", {"A": v[0], "b": v[1]}))
        model.x0 = _finite(np.r_[-model.seed_z, 58., 0.], (36,), "unique accepted58 initial backend")
        model.nonlinear_constraint_count = sum(21*len(model.thetas[label])*6 for label in LABELS)
        model.constraint_count = model.nonlinear_constraint_count+len(model.linear_b)
        model.binding = {"schema": POLICY+"-binding", "definition": definition(),
            "source_receipt": copy.deepcopy(source_receipt), "configuration_sha256": digest(cfg),
            "field_definition_sha256": field.definition_sha256, "coordinate_definition_sha256": field.coordinate_definition_sha256,
            "accepted_state168": array_binding(q58), "paid_unaccepted_q_R168": array_binding(qr),
            "accepted_physical_state_sha256": digest(field.identity(q58)),
            "paid_q_R_physical_state_sha256": digest(field.identity(qr)),
            "paid_free_model_binding_sha256": paid_free_model["binding_sha256"],
            "paid_prefix_model_binding_sha256": paid_prefix_model["binding_sha256"],
            "original_lower172_exact": [str(v) for v in model.lower172], "original_upper172_exact": [str(v) for v in model.upper172],
            "paid_exact_P_sha256": digest([[str(v) for v in row] for row in model.exact_P]),
            "physical_coordinate_definition": copy.deepcopy(model.coordinate_record),
            "paid_original_z_R34": _vector(model.seed_z), "initial_backend36": _vector(model.x0),
            "suffix_radial_ids": ids.tolist(), "radial": array_binding(model.radial),
            "theta": {label: array_binding(model.thetas[label]) for label in LABELS},
            "metric_budget_exact_binary64": str(Q.from_float(model.metric_budget)),
            "K_lower_exact": str(model.target_exact), "K_lower_binary64": model.target_lower,
            "K_lower_exact_binary64": str(Q.from_float(model.target_lower)),
            "maximum_h_exact": str(model.maximum_h_exact), "maximum_h_inward_binary64": model.maximum_h_float,
            "new_last3_radial_basis": copy.deepcopy(model.basis_receipt),
            "fixed_radial_row_reuse": copy.deepcopy(model.fixed_row_receipt),
            "new_last3_radial_jets": [array_binding(v) for v in model.last3_radial],
            "new_linear_A": array_binding(model.linear_A), "new_linear_b": array_binding(model.linear_b),
            "all_original_suffix_rows_preserved": True,
            "same_mathematical_original_field_different_floating_summation_order": True,
            "canonical_wholebody_prediction_and_actual14_remain_external": True,
            "implementation_hashes": implementation_hashes()}
        model.binding_sha256 = digest(model.binding)
        _require(_same(model.point_from_backend(model.x0), q58), "exact shifted initial point must reproduce accepted58")
        _require(_same(model.point_from_backend(np.r_[np.zeros(34), 58., 0.]), qr), "zero shift must reproduce literal paid q_R")
        model.temporary = _TemporaryArrays(wall, sink)
        model.status = "ready"
        sink.update(status="complete", model_binding_sha256=model.binding_sha256, binding=copy.deepcopy(model.binding),
                    no_paid_suffix_value_or_old_scientific_call_replayed=True)
        _wall(wall, POLICY+".build.complete")
        return model
    except Exception as error:
        sink.update(status="raised", error=_error(error)); model.status = "build-raised"
        raise
    finally:
        sink["local_elapsed_seconds"] = time.monotonic()-tick


class _EvaluationCache:
    def __init__(self, model, wall, started, seconds, maximum, sink):
        self.model, self.wall, self.started, self.seconds = model, wall, started, seconds
        self.maximum, self.sink = maximum, sink
        self.entries = {}
        self.counts = {"started": 0, "completed": 0, "failed": 0, "cache_hits": 0}
        self.callbacks = {"objective": 0, "objective_J": 0, "constraint_value": 0,
            "constraint_J": 0, "iteration": 0, "initial_value": 0, "initial_J": 0, "returned_vector": 0}
        sink["evaluation_records"] = []; sink["iteration_records"] = []

    def check(self, phase):
        _wall(self.wall, POLICY+".solver."+phase)
        elapsed = time.monotonic()-self.started
        if elapsed >= self.seconds:
            raise WholeSuffixLimit("the one new whole-suffix solver clock exhausted: %.17g seconds" % elapsed)

    def touch(self, x, role):
        self.callbacks[role] = self.callbacks.get(role, 0)+1
        self.sink["callback_counts"] = copy.deepcopy(self.callbacks)
        self.sink["_last_backend_input"] = np.asarray(x, dtype=np.float64).copy()
        self.check(role)
        return _finite(x, (36,), "literal backend callback")

    def get(self, x, role):
        vector = self.touch(x, role); key = vector.tobytes()
        if key in self.entries:
            self.counts["cache_hits"] += 1
            entry = self.entries[key]
            self.model.last_entry = entry
            self.sink["_last_complete_evaluation"] = entry
            self.sink["new_point_counts"] = copy.deepcopy(self.counts)
            return entry
        if self.counts["started"] >= self.maximum:
            raise WholeSuffixLimit("the declared240 new backend-point ceiling is exhausted")
        self.counts["started"] += 1; ordinal = self.counts["started"]
        record = {"ordinal": ordinal, "first_role": role, "status": "entered", "backend36": _vector(vector)}
        self.sink["evaluation_records"].append(record)
        self.sink["new_point_counts"] = copy.deepcopy(self.counts)
        tick = time.monotonic()
        try:
            entry = self.model._value(vector, self.sink); entry["ordinal"] = ordinal
            self.entries[key] = entry; self.model.last_entry = entry
            self.counts["completed"] += 1
            self.sink["_last_complete_evaluation"] = entry
            record.update(status="complete", state168=_vector(entry["state168"]),
                whole_suffix_pass=entry["whole_suffix_pass"], summaries=copy.deepcopy(entry["summaries"]),
                constraint_values=array_binding(entry["values"]), objective_K_plus_weight_h=float(vector[34]+NORM_WEIGHT*vector[35]))
            self.check("value-complete")
            return entry
        except Exception as error:
            record["error"] = _error(error)
            if record["status"] == "complete":
                record["complete_values_retained_before_post_call_stop"] = True
            else:
                record["status"] = "raised"; self.counts["failed"] += 1
            raise
        finally:
            record["seconds"] = time.monotonic()-tick
            self.sink["new_point_counts"] = copy.deepcopy(self.counts)

    def jacobian(self, entry, role):
        self.callbacks[role] = self.callbacks.get(role, 0)+1
        self.sink["callback_counts"] = copy.deepcopy(self.callbacks)
        self.check(role)
        J = self.model._jacobian(entry, self.sink)
        self.sink["_last_complete_J"] = {"backend36": entry["backend"], "value_ordinal": entry["ordinal"], "matrix": J}
        self.check(role+"-complete")
        return J

    def initialize(self):
        entry = self.get(self.model.x0, "initial_value")
        self.model.initial_entry = entry
        # Save the complete initial values before requesting any J which could fail.
        self.sink["_initial_evaluation"] = entry
        self.sink["_initial_geometry"] = self.sink.get("_last_complete_geometry")
        J = self.jacobian(entry, "initial_J")
        self.sink["_initial_J"] = J
        scales = np.maximum(1., np.maximum(abs(entry["values"]), np.max(abs(J), axis=1)))
        scales = _finite(scales, (self.model.constraint_count,), "fixed initial row scales")
        self.model.row_scales = scales; self.sink["_fixed_row_scales"] = scales
        self.sink["fixed_row_scales"] = {"formula": "max(1,abs(initial value),max(abs(initial Jrow)))",
            "binding": array_binding(scales), "never_updated": True, "initial_value_ordinal": entry["ordinal"]}
        self.sink["initial_model_receipt"] = {"value_ordinal": entry["ordinal"],
            "actual_strict_metric_margin_was_evaluated_not_inferred_from_peak_location": True,
            "maximum_scaled_violation": float(max(0., -np.min(entry["values"]/scales))),
            "whole_suffix_pass": entry["whole_suffix_pass"], "summaries": copy.deepcopy(entry["summaries"])}
        self.check("initial-scales-complete")

    def objective(self, x):
        x = self.touch(x, "objective")
        return float(x[34]+NORM_WEIGHT*x[35])

    def objective_J(self, x):
        self.touch(x, "objective_J")
        result = np.zeros(36); result[34] = 1.; result[35] = NORM_WEIGHT
        return result

    def constraint_value(self, x):
        entry = self.get(x, "constraint_value")
        return entry["values"]/self.model.row_scales

    def constraint_J(self, x):
        entry = self.get(x, "constraint_J")
        J = self.jacobian(entry, "requested_analytic_J")
        return J/self.model.row_scales[:, None]

    def iteration(self, x):
        vector = self.touch(x, "iteration")
        entry = self.entries.get(vector.tobytes())
        self.sink["iteration_records"].append({"ordinal": len(self.sink["iteration_records"])+1,
            "backend36": _vector(vector), "objective_K_plus_weight_h": float(vector[34]+NORM_WEIGHT*vector[35]),
            "elapsed_seconds": time.monotonic()-self.started,
            "cached_value_ordinal": None if entry is None else entry["ordinal"],
            "cached_scaled_violation": None if entry is None else float(max(0., -np.min(entry["values"]/self.model.row_scales))),
            "no_new_scientific_evaluation_in_iteration_callback": True})


def _solver_public(sink):
    result = _public(sink)
    raw = result.pop("original_backend_return", None)
    result["original_backend_return_summary"] = None if raw is None else {key: copy.deepcopy(raw.get(key)) for key in
        ("status", "success", "message", "nit", "nfev", "njev", "backend_elapsed_seconds", "actual_finite_raw36_saved", "raw_K", "raw_h")}
    result["unemitted_original_backend_return"] = raw if sink.get("original_result_stdout_receipt") is None else None
    result.pop("evaluation_records", None); result.pop("iteration_records", None)
    result.pop("component_events", None)
    result["all_evaluation_iteration_and_partial_records_are_in_caller_SOLVE_TRACE"] = True
    return result


def solve_R1_R2_whole_suffix_once(
        model, *, wall, charge_solve, emit=None, capture=None,
        solver_seconds=SOLVER_SECONDS, maxiter=120, max_evaluations=MAX_EVALUATIONS):
    """Exactly one new minimax call; emit only the actual original backend result."""
    _require(isinstance(model, R1R2WholeSuffixModel) and model.status == "ready" and not model.solve_attempted,
             "one ready unattempted new whole-suffix model required")
    _require(callable(wall) and callable(charge_solve) and (emit is None or callable(emit)), "external clock/charge/emitter required")
    _require(type(maxiter) is int and 0 < maxiter <= SLSQP_OPTIONS["maxiter"]
             and type(max_evaluations) is int and 0 < max_evaluations <= MAX_EVALUATIONS, "new caps may only be reduced")
    seconds = float(solver_seconds)
    _require(not isinstance(solver_seconds, (bool, np.bool_)) and math.isfinite(seconds) and 0 < seconds <= SOLVER_SECONDS,
             "finite solver limit at most180 seconds required")
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty one-solver capture required")
    sink.update(schema=POLICY+"-one-solver-attempt", status="entered", model_binding_sha256=model.binding_sha256,
        backend_entered=False, charged=False, qualified_candidate=False, original_backend_return=None,
        original_result_stdout_receipt=None, options={"maxiter": maxiter, "ftol": SLSQP_OPTIONS["ftol"], "disp": False},
        maximum_new_points=max_evaluations, solver_seconds_limit=seconds,
        new_point_cap_counts="distinct literal backend36 byte inputs, including same q with new K or h",
        one_new_problem_not_a_restart_of_free36_or_prefix102=True,
        no_unreturned_intermediate_callback_candidate_promoted=True)
    model.solve_attempted = True; model.solver_sink = sink
    started = time.monotonic(); cache = None; candidate = None; candidate_record = None; raw_vector = None
    try:
        model.assert_context()
        sink["charge_receipt"] = copy.deepcopy(charge_solve({"schema": POLICY+"-solve-charge",
            "backend": "scipy.optimize.minimize(method='SLSQP')", "backend_variables": 36,
            "backend_order": "delta_z34,K,h", "objective": "K+1e-6*h", "model_binding_sha256": model.binding_sha256,
            "whole_suffix_radial_rows": 21, "complete_angular_counts": [384, 768],
            "constraint_count": model.constraint_count, "options": copy.deepcopy(sink["options"]),
            "maximum_new_points": max_evaluations, "solver_seconds": seconds,
            "new_point_cap_counts": sink["new_point_cap_counts"],
            "new_geometric_J_only_when_requested_including_initial_scaling_request": True}))
        sink["charged"] = True
        cache = _EvaluationCache(model, wall, started, seconds, max_evaluations, sink)
        cache.check("before-import")
        import scipy
        from scipy.optimize import minimize
        sink["scipy_version"] = str(scipy.__version__)
        cache.check("after-import")
        cache.initialize()
        bounds = [(None, None)]*34+[(model.target_lower, 58.), (0., model.maximum_h_float)]
        sink["backend_bounds"] = [list(v) for v in bounds]
        cache.check("before-backend")
        backend_started = time.monotonic(); sink.update(status="backend-entered", backend_entered=True)
        result = minimize(cache.objective, model.x0.copy(), method="SLSQP", jac=cache.objective_J, bounds=bounds,
            constraints=[{"type": "ineq", "fun": cache.constraint_value, "jac": cache.constraint_J}],
            callback=cache.iteration, options=copy.deepcopy(sink["options"]))
        backend_elapsed = time.monotonic()-backend_started
        # Capture the complete real return before any decode, gate, clock, or external decision.
        sink["_original_return_object"] = result
        returned = result.get("x")
        raw = {"schema": POLICY+"-original-nonlinear-backend-return",
            "backend": "scipy.optimize.minimize(method='SLSQP')", "scipy_version": str(scipy.__version__),
            "model_binding_sha256": model.binding_sha256, "backend_variable_order": "delta_z34,K,h",
            "actual_raw_backend36": None if returned is None else _raw_numeric(returned),
            "entire_OptimizeResult_fields": _raw_all_fields(dict(result)),
            "status": None if result.get("status") is None else int(result.get("status")),
            "success": bool(result.get("success", False)), "message": str(result.get("message", "")),
            "nit": None if result.get("nit") is None else int(result.get("nit")),
            "nfev": None if result.get("nfev") is None else int(result.get("nfev")),
            "njev": None if result.get("njev") is None else int(result.get("njev")),
            "backend_elapsed_seconds": float(backend_elapsed), "raw_return_captured_before_filter": True,
            "returned_multipliers_are_internal_QP_approximations_not_strict_certificates": True,
            "unreturned_fields_not_fabricated": True}
        sink["original_backend_return"] = raw
        sink.update(status="backend-returned", backend_elapsed_seconds=float(backend_elapsed))
        finite = False
        if returned is not None:
            vector = np.asarray(returned, dtype=np.float64)
            finite = bool(vector.shape == (36,) and np.all(np.isfinite(vector)))
            if finite:
                raw_vector = _vector(vector)
                raw["raw_K"], raw["raw_h"] = float(vector[34]), float(vector[35])
        raw["actual_finite_raw36_saved"] = bool(finite and raw["actual_raw_backend36"] is not None
            and raw["actual_raw_backend36"].get("shape") == [36]
            and len(raw["actual_raw_backend36"].get("exact_binary64_flat", [])) == 36)
        if not finite:
            raw["raw_K"], raw["raw_h"] = None, None
        if emit is not None:
            tick = time.monotonic()
            try:
                sink["original_result_stdout_receipt"] = copy.deepcopy(emit("NONLINEAR_RESULT", copy.deepcopy(raw)))
            except Exception as error:
                sink["raw_result_reporting_error"] = _error(error)
                raise
            finally:
                sink["raw_result_emit_seconds"] = time.monotonic()-tick
        cache.check("after-original-backend-return-saved")
        eligible = bool(finite and raw["success"] and raw["status"] == 0)
        sink["backend_status_eligible"] = eligible
        if finite:
            proposed, candidate_record = model.point_from_backend(vector, include_record=True)
            sink["returned_candidate_record"] = copy.deepcopy(candidate_record)
            sink["_returned_candidate168"] = proposed
        if not eligible:
            sink["status"] = "no-qualified-backend-return"
        else:
            entry = cache.get(vector, "returned_vector")
            # Reuse the already computed geometry at the actual returned state.
            model._geometry(entry["state168"], sink)
            nonlinear_violation = float(max(0., -np.min(entry["values"][:model.nonlinear_constraint_count]/model.row_scales[:model.nonlinear_constraint_count])))
            scaled_violation = float(max(0., -np.min(entry["values"]/model.row_scales)))
            linear_violation = float(max(0., -np.min(entry["values"][model.nonlinear_constraint_count:])))
            passed = bool(scaled_violation <= SLSQP_OPTIONS["ftol"] and linear_violation <= LP_ROW_TOLERANCE
                          and candidate_record["original_box_and_K_h_pass"] and entry["whole_suffix_pass"])
            sink["candidate_filter"] = {"returned_value_ordinal": entry["ordinal"],
                "maximum_scaled_model_violation": scaled_violation, "maximum_scaled_nonlinear_violation": nonlinear_violation,
                "scaled_model_tolerance": SLSQP_OPTIONS["ftol"],
                "maximum_unscaled_original_linear_violation": linear_violation, "original_linear_tolerance": LP_ROW_TOLERANCE,
                "original_linear_pass": bool(linear_violation <= LP_ROW_TOLERANCE),
                "exact_box_K_h_pass": bool(candidate_record["original_box_and_K_h_pass"]),
                "backend_norm_epigraph_exact_pass": bool(candidate_record["backend_norm_epigraph_exact_pass"]),
                "whole_suffix_unsmoothed_and_unsquared_pass": bool(entry["whole_suffix_pass"]),
                "whole_suffix_summaries": copy.deepcopy(entry["summaries"]), "qualified": passed,
                "wholebody_canonical_prediction_and_actual14_remain_external": True}
            if passed:
                candidate = proposed
                sink.update(status="qualified-whole-suffix-return-needs-canonical-wholebody-prediction", qualified_candidate=True)
            else:
                sink["status"] = "returned-vector-fails-whole-suffix-or-original-exact-box"
        cache.check("complete")
        model.status = sink["status"]
    except WholeSuffixLimit as error:
        sink.update(status="stopped-at-declared-new-solver-limit", error=_error(error), stop_reason=str(error),
                    qualified_candidate=False, no_backend_status_relabelled=True)
        model.status = sink["status"]; candidate = None
    except Exception as error:
        sink.update(status="raised", error=_error(error), qualified_candidate=False,
                    complete_and_partial_scientific_work_retained=True)
        model.status = "solver-raised"; candidate = None
        raise
    finally:
        sink["local_elapsed_seconds"] = time.monotonic()-started
        sink["observed_nonpreemptive_solver_clock_overrun_seconds"] = max(0., sink["local_elapsed_seconds"]-seconds)
        sink["nonpreemptive_clock_checks_not_a_strict_backend_wall_guarantee"] = True
        sink["new_geometry_counts"] = copy.deepcopy(model.full_point_counts)
        sink["new_J_counts"] = copy.deepcopy(model.jacobian_counts)
        sink["K_independent_derivative_input_counts"] = copy.deepcopy(model.derivative_input_counts)
        sink["temporary_cache_receipt"] = copy.deepcopy(model.build_sink.get("temporary_cache"))
        if cache is not None:
            sink["new_point_counts"] = copy.deepcopy(cache.counts)
            sink["callback_counts"] = copy.deepcopy(cache.callbacks)
            sink["cached_complete_literal_backend_inputs"] = len(cache.entries)
        record = sink.get("returned_candidate_record")
        sink["actual_returned_candidate168_saved"] = bool(isinstance(record, dict)
            and len(record.get("rounded_independent168", {}).get("values", [])) == 168
            and len(record.get("rounded_independent168", {}).get("exact_binary64", [])) == 168)
        sink["actual_returned_physical172_saved"] = bool(isinstance(record, dict)
            and len(record.get("rounded_physical172_exact", [])) == 172)
    raw = sink.get("original_backend_return")
    return {"status": sink["status"], "qualified": bool(sink["qualified_candidate"]),
        "qualified_candidate": bool(sink["qualified_candidate"]), "candidate168": candidate,
        "candidate": candidate, "candidate_record": copy.deepcopy(candidate_record),
        "actual_backend_raw36": copy.deepcopy(raw_vector),
        "backend_success": None if raw is None else raw["success"],
        "backend_status": None if raw is None else raw["status"], "report": _solver_public(sink)}


def _entry_payload(entry):
    return {"value_ordinal": entry["ordinal"], "backend36": _vector(entry["backend"]),
        "state168": _vector(entry["state168"]), "original_constraint_values": _payload(entry["values"]),
        "whole_suffix_summaries": copy.deepcopy(entry["summaries"]), "whole_suffix_pass": entry["whole_suffix_pass"]}


def _geometry_payload(geometry):
    if geometry.get("paid_q_R_reuse"):
        # Do not emit a second copy of arrays already permanently bound by the source stdout.
        return {"paid_q_R_reuse": True, "state168": _vector(geometry["state168"]),
            "paid_value_arrays_reference": "paid_prefix_model.fixed_suffix_full_arrays",
            "new_unsaved_I_II_inputs": {label: _numeric({key: value for key, value in grid["curvature"].items()
                if key not in ("A", "U", "q")}) for label, grid in geometry["grids"].items()},
            "new_metric_proposal_rows": {label: _payload(grid["metric_rows"]) for label, grid in geometry["grids"].items()}}
    return _numeric(geometry)


def R1_R2_whole_suffix_capture_record(capture, *, include_arrays=False):
    """No geometry is regenerated and no unfilled np.empty memory is serialized."""
    _require(isinstance(capture, dict), "whole-suffix capture dictionary required")
    result = _public(capture)
    if result.get("original_result_stdout_receipt") is not None:
        raw = result.pop("original_backend_return", None)
        result["emitted_original_backend_return_summary"] = None if raw is None else {key: copy.deepcopy(raw.get(key)) for key in
            ("status", "success", "message", "nit", "nfev", "njev", "actual_finite_raw36_saved", "backend_elapsed_seconds", "raw_K", "raw_h")}
    if not include_arrays:
        return result
    for private, public in (("_new_last3_radial", "actually_completed_new_last3_radial"),
                            ("_new_linear_arrays", "actually_completed_new_linear_arrays"),
                            ("_fixed_row_scales", "actual_fixed_row_scales"),
                            ("_last_backend_input", "actual_last_backend_input"),
                            ("_returned_candidate168", "actual_returned_candidate168")):
        if private in capture:
            result[public] = _numeric(capture[private])
    initial = capture.get("_initial_evaluation"); latest = capture.get("_last_complete_evaluation")
    if isinstance(initial, dict):
        result["actual_initial_evaluation"] = _entry_payload(initial)
    if isinstance(latest, dict):
        if initial is not None and latest["ordinal"] == initial["ordinal"]:
            result["actual_last_evaluation"] = {"values_reference": "actual_initial_evaluation", "same_value_ordinal": True}
        else:
            result["actual_last_evaluation"] = _entry_payload(latest)
    first_geometry = capture.get("_initial_geometry"); last_geometry = capture.get("_last_complete_geometry")
    if isinstance(first_geometry, dict):
        result["actual_initial_geometry_arrays"] = _geometry_payload(first_geometry)
    if isinstance(last_geometry, dict):
        if isinstance(first_geometry, dict) and _same(last_geometry["state168"], first_geometry["state168"]):
            result["actual_last_geometry_arrays"] = {"values_reference": "actual_initial_geometry_arrays", "same_actual_state": True}
        else:
            result["actual_last_geometry_arrays"] = _geometry_payload(last_geometry)
    first_J = capture.get("_initial_J"); last_J_record = capture.get("_last_complete_J")
    if isinstance(first_J, np.ndarray):
        result["actual_initial_analytic_J36"] = _payload(first_J)
    last_J = last_J_record.get("matrix") if isinstance(last_J_record, dict) else None
    if isinstance(last_J, np.ndarray):
        same = isinstance(first_J, np.ndarray) and array_binding(last_J) == array_binding(first_J)
        result["actual_last_analytic_J36"] = {
            "backend36": _vector(last_J_record["backend36"]), "value_ordinal": last_J_record["value_ordinal"],
            "matrix": {**array_binding(last_J), "values_reference": "actual_initial_analytic_J36"} if same else _payload(last_J)}
    partial = capture.get("_last_geometry_partial")
    if isinstance(partial, dict) and partial.get("status") != "complete":
        result["actually_last_incomplete_geometry"] = _numeric(partial)
    partial_J = capture.get("_last_jacobian_partial")
    if isinstance(partial_J, dict):
        metadata = {key: value for key, value in partial_J.items() if key not in
            ("matrix", "working_kernel_arrays", "working_derivative_frame")}
        matrix = partial_J.get("matrix")
        if partial_J.get("status") == "complete" and isinstance(matrix, np.ndarray):
            if isinstance(last_J, np.ndarray) and array_binding(matrix) == array_binding(last_J):
                metadata["complete_J_values_reference"] = "actual_last_analytic_J36"
            elif isinstance(first_J, np.ndarray) and array_binding(matrix) == array_binding(first_J):
                metadata["complete_J_values_reference"] = "actual_initial_analytic_J36"
            else:
                metadata["complete_J_before_post_call_stop"] = _payload(matrix)
        else:
            metadata["actually_completed_column_values"] = []
            if isinstance(matrix, np.ndarray):
                for block in partial_J.get("completed_column_blocks", []):
                    values = matrix[block["row_start"]:block["row_stop"], block["column_start"]:block["column_stop"]]
                    metadata["actually_completed_column_values"].append({**copy.deepcopy(block), "values": _payload(values)})
            if partial_J.get("working_kernel_arrays") is not None:
                metadata["actually_completed_current_kernel_arrays"] = _numeric(partial_J["working_kernel_arrays"])
            if partial_J.get("working_derivative_frame") is not None:
                metadata["actually_completed_current_derivative_frame"] = _numeric(partial_J["working_derivative_frame"])
        result["last_J_completion_or_partial_receipt"] = _numeric(metadata)
    result["unsaved_values_are_not_filled_or_recomputed"] = True
    result["temporary_intermediate_cache_is_not_a_future_free_scientific_input"] = True
    return result


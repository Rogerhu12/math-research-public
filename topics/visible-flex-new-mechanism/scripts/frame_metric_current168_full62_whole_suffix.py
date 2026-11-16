#!/usr/bin/env python3
"""One full62 original-coefficient minimax on the complete paid suffix.

Import-only: all scientific execution belongs to the external public Actions
scope.  The closed whole34/full51 solves are not restarted and provide no
unavailable scientific arrays.  The new62 controls add two exact-null tail
heights and the original complete body9 to the old51 tail u/v directions.
All original172 box, physical norm, metric, area and unsquared PSD gates remain.

Values use paid q_R scalar fields plus the actual once-rounded coefficient
change.  The mathematical field is unchanged; floating summation order is
explicitly not the canonical full-body order.  Only a qualified actual return
may receive the external canonical prediction and original fourteen gates.
Large scientific arrays are temporary same-process cache only; public records
retain bindings/costs, never claim those bindings are future free inputs.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import math
import resource
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import periodic_operator
from frame_complete_body_extension168 import (
    CompleteBody168Field, array_binding, LEFT_EXACT as BODY_LEFT_EXACT,
    RIGHT_EXACT as BODY_RIGHT_EXACT, LENGTH_EXACT as BODY_LENGTH_EXACT)
from frame_complete_body_extension168_joint_selected import _context
from frame_selected_row_radial_jacobian import angular_kernels, virtual_selected_jets, expand_radial_rows
from frame_metric_spectral_recovery import spectral_proposal_rows, spectral_parameter_rows
from frame_curvature_psd import curvature_values, independent_principal_curvatures
from frame_height_null_coordinates import digest
from frame_metric_current168_ring17 import (
    LP_ROW_TOLERANCE, _require, _error, _wall, _bounds, _vector, _raw_numeric)
from frame_metric_current168_reflected_R1_ray import _raw_all_fields
from frame_metric_current168_fixed_ring_prefix102 import (
    _finite, _same, _slice_radial, _derivative_frame_parts, _inward_float)


POLICY = "true58-full62-whole-suffix-v1"
PAID_FREE_POLICY = "true58-free-R1-R2-original-box-curvature-minimax-v1"
PAID_PREFIX_POLICY = "true58-fixed-ring-prefix102-body-repair-v1"
LABELS = ("coarse", "fine")
POSITION_KEYS = ("Xs", "Xt", "Xss", "Xst", "Xtt")
SCALAR_KEYS = ("value", "s", "ss", "theta")
ROW_NAMES = ("metric_plus", "metric_minus", "plus_trace", "plus_determinant", "minus_trace", "minus_determinant")
TAIL_UV_ROWS = tuple(range(54, 81))+tuple(range(129, 153))
ACTIVE_ROWS = TAIL_UV_ROWS+(157, 158)+tuple(range(159, 168))
PRIMARY_PHYSICAL_ROWS = TAIL_UV_ROWS+(160, 161)+tuple(range(163, 172))
HEIGHT_STATE_ROWS = (157, 158, 167)
HEIGHT_BACKEND_COLUMNS = (51, 52, 61)
SUFFIX_LEFT_EXACT = "153/200"
TARGET_EXACT = "1000/61"
VARIABLES = 64
K_COLUMN = 62
H_COLUMN = 63
NORM_WEIGHT = 1.e-6
OWNED_WIDTH = 4
MAX_EVALUATIONS = 640
MAX_BACKEND_EVALUATIONS = 1280
SOLVER_SECONDS = 1200.
SLSQP_OPTIONS = {"maxiter": 320, "ftol": 1.e-9, "disp": False}


class WholeSuffixLimit(RuntimeError):
    """The actual one-solve clock/point limit, never a fabricated return."""


def definition():
    return {
        "schema": POLICY, "accepted_source_index": 58,
        "backend_order": "z62,K,h", "independent_controls": 62,
        "independent_rows": list(ACTIVE_ROWS),
        "old_full51_controls": list(TAIL_UV_ROWS),
        "new11_controls": [157, 158]+list(range(159, 168)),
        "excluded_exact_suffix_zero_rows": [153, 154, 155, 156],
        "excluded_reason": "normalized-Q uses old B3; first3 null heights end at .603",
        "independent_decode": "RN(q58+E168x62*Q(z62)), E has1/4 active entries; one exact sum and one independent rounding",
        "physical_decode": "original exact affine159-to163 null-height map, direct-sum identity9",
        "physical_height_160_161_162_increment": "z51/4,z52/4,-3*z51/8-5*z52/16",
        "no_rounded_nine_height_surrogate": True,
        "initial_point": "z62=0,K=58,h=0, exactly accepted58",
        "objective": "K+1e-6*h", "K_interval_exact": [TARGET_EXACT, "58"],
        "physical_norm": "h>=4*norm_inf(P172x62*z), including coupled physical height row162",
        "physical_box": "all original172 coordinates before and after independent once rounding",
        "backend_z_bounds": "inward independent endpoints induced by62 original physical anchor rows",
        "coupled_height_row162": "all original linear and exact final gates; not certified by independent bounds",
        "maximum_h_exact": "18014398507545773/281474976710656",
        "maximum_h_semantics": "explicit retained finite cap; paid derivation covered old51, not claimed full62-box sufficient",
        "suffix_left_exact": SUFFIX_LEFT_EXACT,
        "suffix_rows": "all21 original radial rows s>=153/200, including original ring141",
        "angular_grids": "both complete original coarse384 and fine768 with their own Pi_N",
        "finite_rows": "145152 nonlinear plus344 original box,126 physical norm and4 K/h",
        "same_fixed_g_and_permanent_c0_b0": True,
        "height_changes": "two original exact-null tail heights and one complete zero-total body height",
        "no_active_row_thinning_or_repair_restart": True,
        "PSD_matrix": "(K*q*I_actual +/- numerator_K)/original_curvature_scale",
        "actual_G_retained": True, "normal_area_is_a_separate_domain_and_qualification_gate": True,
        "original_unsmoothed_eta_and_direct_kappa_also_required": True,
        "value_arithmetic": "paid q_R scalars/b,b_s plus actual rounded tail/body/null-height coefficient changes",
        "same_mathematical_field_not_bitwise_canonical_field_scalar_frame": True,
        "q_R_value_reuse": "literal paid prefix T,jets,e,f,eta,PSD,area,principal",
        "closed_whole34_and_full51_missing_arrays_are_not_free_inputs": True,
        "fixed_radial_rows": "same binary64 radial beyond all original exact and stored spline/null/body support endpoints",
        "fixed_row_values": "paid geometry retained; current K PSD and K derivative still assembled",
        "new_basis": "original B9/B10/B11; two exact-null height columns; original P5/P8 body jets",
        "body_angular": "first4 paid original sin(2*j*theta) modes and derivatives, no duplicate trigonometry",
        "new_geometric_J": "original full angular/position chain: u27+4,v24+4,height2+1",
        "derivative_input_cache": "actual q/owned-radial-block/family, K-independent metric and I/II differentials",
        "final_J_cache": "actual q plus binary64 K; h has only fixed linear derivatives",
        "row_scales": "fixed after initial J: max(1,abs(initial values),max(abs(initial Jrow)))",
        "solver": "one scipy.optimize.minimize(method='SLSQP')",
        "options": copy.deepcopy(SLSQP_OPTIONS), "solver_seconds": SOLVER_SECONDS,
        "maximum_new_physical_points": MAX_EVALUATIONS,
        "maximum_distinct_backend64_inputs": MAX_BACKEND_EVALUATIONS,
        "physical_point_cap_counts": "distinct actual q168 needing new geometry; literal paid q_R hits separate",
        "backend_cap_counts": "distinct literal backend64 byte inputs, including new K or h",
        "temporary_cache": "bounded current-q RAM, current q+K J, initial/last receipts; zero disk writes",
        "evicted_revisits": "actual geometry/J/input recomputation separately counted and charged",
        "scientific_array_output": "shape/hash/completion/cost only; no large values or future free reuse",
        "qualification": "actual status0 return, exact original affine box and rounded norm to raw h, all suffix gates",
        "external_after_qualification": "one canonical whole-body prediction then at most one original actual pair",
        "finite_success_is_not_reach_or_main_topic_completion": True}

def implementation_hashes():
    names = (Path(__file__).name, "frame_metric_current168_full62_whole_suffix_solver.py",
             "frame_metric_current168_fixed_ring_prefix102.py",
             "frame_metric_current168_ring17.py", "frame_metric_current168_reflected_R1_ray.py",
             "frame_collar_bvp.py", "frame_complete_body_extension168.py",
             "frame_complete_body_extension168_joint_selected.py", "frame_selected_row_radial_jacobian.py",
             "frame_entry_single_q.py", "frame_height_null_coordinates.py",
             "frame_direct_reference_geometry159.py", "frame_metric_spectral_recovery.py", "frame_curvature_psd.py")
    return {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}


def _public(value):
    return {key: copy.deepcopy(item) for key, item in value.items() if not str(key).startswith("_")}


def _array_receipt(value):
    """Only call on an array that was actually filled by completed work."""
    a = np.asarray(value)
    return {**array_binding(a), "values_in_this_record": False,
        "hash_is_not_a_future_free_scientific_input": True}


def _compact(value):
    """Compact already-computed data; no scientific reconstruction or truncation."""
    if isinstance(value, np.ndarray):
        return _array_receipt(value)
    if isinstance(value, np.generic):
        return _compact(value.item())
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _compact(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_compact(v) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        return {"original_nonfinite_float": repr(value)}
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise TypeError("unsupported compact retained object: "+type(value).__name__)


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
            event["process_peak_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        _wall(self.wall, POLICY+"."+kind+".after")
        return answer


class _CurrentArrays:
    """Bounded current-q RAM cache; no scientific arrays are written to disk."""
    def __init__(self, wall, sink):
        self.wall, self.sink = wall, sink
        sink["temporary_cache"] = {"storage": "current-q RAM only", "writes": 0, "reads": 0,
            "bytes_written": 0, "io_seconds": 0., "cleanup_complete": False,
            "maximum_current_geometry_states": 1, "maximum_current_final_J": 1,
            "current_q_derivative_blocks_only": True,
            "initial_and_last_completed_arrays_retained_for_bindings_only": True,
            "value_vectors_bounded_by_backend64_input_cap": True,
            "evictions": {}, "process_peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
            "only_this_process": True, "uploaded_or_future_free": False}

    def evict(self, kind, count):
        if count:
            log = self.sink["temporary_cache"]["evictions"]
            log[kind] = log.get(kind, 0)+int(count)
        self.sink["temporary_cache"]["process_peak_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    def close(self):
        self.sink["temporary_cache"]["cleanup_complete"] = True
        self.sink["temporary_cache"]["no_disk_cleanup_IO_was_needed"] = True
        self.sink["temporary_cache"]["process_peak_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


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


def _new_body_and_tail_height_basis(field, radial):
    """Only the missing new62 inputs; no field/baseline geometry is re-evaluated."""
    r = np.asarray(radial, dtype=float)
    left, right, length = map(lambda v: float(Q(v)),
        (BODY_LEFT_EXACT, BODY_RIGHT_EXACT, BODY_LENGTH_EXACT))
    null = field.original_field.null_basis
    _require(Q(BODY_RIGHT_EXACT) == Q("423/500")
        and null.right_exact == Q(BODY_RIGHT_EXACT),
        "shared actual original null/body right endpoint required")
    active = (r > left) & (r < right)
    xi = (r[active]-left)/length
    inside = (xi > 0.) & (xi < 1.)
    ids = np.flatnonzero(active)[inside]; xi = xi[inside]
    body, xi_outputs = {}, {}
    for name, power in (("u", 5), ("v", 8)):
        out = [np.zeros_like(r) for _ in range(3)]
        distance = 1.-xi; exponential = np.exp(-xi/distance)
        inverse2 = distance**-2; inverse3 = distance**-3
        base = xi**power
        first = power*xi**(power-1)-inverse2*base
        second = (power*(power-1)*xi**(power-2)
            -2*power*inverse2*xi**(power-1)+(inverse2*inverse2-2*inverse3)*base)
        for j, local in enumerate((base, first, second)):
            out[j][ids] = exponential*local
            _require(np.all(np.isfinite(out[j])), "finite original body radial jet required")
        xi_outputs[name] = out
        body[name] = tuple(out[j][:, None]/length**j for j in range(3))
    # values() skips all first3 null columns by their exact compact supports
    # on this suffix; only the original tail6/tail7 columns are consumed.
    nb = _finite(null.values(r), (len(r), 5), "original null-height b")[:, 3:5]
    nbs = _finite(null.values(r, 1), (len(r), 5), "original null-height b_s")[:, 3:5]
    height = {"b": np.column_stack((nb, xi_outputs["v"][1])),
              "b_s": np.column_stack((nbs, xi_outputs["v"][2]/length))}
    receipt = {"schema": POLICY+"-new-body-and-tail-height-inputs",
        "body_definition": {"left_exact": BODY_LEFT_EXACT, "right_exact": BODY_RIGHT_EXACT,
            "length_exact": BODY_LENGTH_EXACT, "u_power": 5, "v_power": 8,
            "formula": "xi^m*exp(-xi/(1-xi)), original zero extensions",
            "derivative_orders_actually_formed": [0, 1, 2]},
        "old_exact_null_basis_sha256": null.identity_sha256,
        "old_null_directions_consumed": [3, 4],
        "old_null_direction_supports_exact": [[str(v) for v in null.supports[j]] for j in (3, 4)],
        "old_null_right_binary64": float(null.right),
        "body_right_binary64": right,
        "height_column_independent_rows": list(HEIGHT_STATE_ROWS),
        "height_column_meaning": ["tail6-compensate8", "tail7-compensate8", "complete body gamma"],
        "old_entry_height_and_Q_zero_columns_not_added_to_solver": True,
        "old_metric_height_baseline_and_source_scalar_fields_not_recomputed": True,
        "body_radial_bindings": {name: [array_binding(v) for v in values] for name, values in body.items()},
        "height_basis_bindings": {name: array_binding(v) for name, v in height.items()}}
    return body, height, receipt


def _linear_rows(P, base, lower, upper, hmax, target_lower):
    rows, rhs, tags = [], [], []
    def add(coeff, k, h, bound, tag):
        rows.append(np.r_[coeff, float(k), float(h)]); rhs.append(float(bound)); tags.append(tag)
    zero = np.zeros(62)
    for j in range(172):
        add(P[j], 0, 0, upper[j]-base[j], {"kind": "physical172_box", "index": j, "side": "upper"})
        add(-P[j], 0, 0, base[j]-lower[j], {"kind": "physical172_box", "index": j, "side": "lower"})
        if np.any(P[j] != 0.):
            add(4*P[j], 0, -1, Q(0), {"kind": "norm", "index": j, "side": "plus"})
            add(-4*P[j], 0, -1, Q(0), {"kind": "norm", "index": j, "side": "minus"})
    add(zero, -1, 0, -target_lower, {"kind": "K_lower"})
    add(zero, 1, 0, Q(58), {"kind": "K_upper"})
    add(zero, 0, -1, Q(0), {"kind": "h_lower"})
    add(zero, 0, 1, hmax, {"kind": "h_upper"})
    return (_finite(np.stack(rows), (474, 64), "full62 original linear A"),
            _finite(rhs, (474,), "full62 original linear b"), tags)


def _original_box_backend_bounds(independent, physical, lower, upper):
    """Inward62 anchor bounds; the coupled row162 keeps its original gates."""
    bounds, rows = [], []
    for column, (i, j) in enumerate(zip(ACTIVE_ROWS, PRIMARY_PHYSICAL_ROWS)):
        # Every chosen anchor has physical_j = fixed_offset + independent_i.
        offset = physical[j]-independent[i]
        exact_independent_lower, exact_independent_upper = lower[j]-offset, upper[j]-offset
        qlower = Q.from_float(_inward_float(exact_independent_lower, True))
        qupper = Q.from_float(_inward_float(exact_independent_upper, False))
        _require(exact_independent_lower <= qlower <= independent[i] <= qupper <= exact_independent_upper,
                 "accepted58 must lie in the inward independent anchor interval")
        exact_lower, exact_upper = 4*(qlower-independent[i]), 4*(qupper-independent[i])
        zlower, zupper = _inward_float(exact_lower, True), _inward_float(exact_upper, False)
        _require(exact_lower <= Q.from_float(zlower) <= 0 <= Q.from_float(zupper) <= exact_upper,
                 "inward anchor increment bounds must contain the true58 zero increment")
        bounds.append((zlower, zupper))
        rows.append({"backend_column": column, "independent_index": i, "physical_anchor_index": j,
            "physical_fixed_offset_exact": str(offset),
            "original_physical_interval_exact": [str(lower[j]), str(upper[j])],
            "independent_inward_endpoints_exact_binary64": [str(qlower), str(qupper)],
            "backend_interval_binary64": [zlower, zupper],
            "backend_interval_exact_binary64": [str(Q.from_float(zlower)), str(Q.from_float(zupper))]})
    return bounds, {"schema": POLICY+"-original-box-anchor-bounds", "rows": rows,
        "original_exact_box_is_unchanged": True,
        "independent_once_rounding_protects_each_listed_physical_anchor": True,
        "coupled_physical_height_row162_retains_original_linear_and_exact_final_gates": True,
        "coupled_row162_not_claimed_protected_by_independent_bounds": True,
        "no_rounding_or_linear_tolerance_failure_is_repaired": True}

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


class Full62WholeSuffixModel:
    def __init__(self):
        self.status = "not-built"; self.solve_attempted = False; self.solver_sink = None
        self.row_scales = None; self.initial_entry = None; self.last_entry = None
        self.seen_geometry_keys = set(); self.seen_J_keys = set(); self.seen_derivative_keys = set()
        self.derivative_input_cache = {}
        self.paid_curvature_part_cache = {}; self.paid_metric_part_cache = {}
        self.loaded_geometry = None; self.loaded_geometry_key = None
        self.loaded_J = None; self.loaded_J_key = None
        self.full_point_counts = {"started": 0, "completed": 0, "failed": 0, "paid_seed_hits": 0, "cache_hits": 0,
            "distinct_new_physical_points": 0, "recomputed_after_eviction": 0}
        self.jacobian_counts = {"started": 0, "completed": 0, "failed": 0, "cache_hits": 0,
            "distinct_q_K_keys": 0, "reassembled_after_eviction": 0}
        self.derivative_input_counts = {"started": 0, "completed": 0, "failed": 0, "cache_hits": 0,
            "distinct_input_keys": 0, "recomputed_after_eviction": 0}

    def assert_context(self):
        self.field._assert_context()
        _require(self.field.definition_sha256 == self.binding["field_definition_sha256"]
                 and self.field.coordinate_definition_sha256 == self.binding["coordinate_definition_sha256"]
                 and digest(self.cfg) == self.binding["configuration_sha256"], "original field/cfg changed")
        _wall(self.wall, POLICY+".context")

    def point_from_backend(self, backend, *, include_record=False):
        x = _finite(backend, (64,), "literal backend64")
        z = tuple(Q.from_float(float(v)) for v in x[:62])
        ideal = list(self.accepted_independent_exact)
        candidate = self.accepted_state168.copy()
        for column, i in enumerate(ACTIVE_ROWS):
            ideal[i] += z[column]/4
            candidate[i] = float(ideal[i])
        _require(np.all(np.isfinite(candidate)), "finite independent once-rounded candidate required")
        if not include_record:
            return candidate
        delta = [Q(0) for _ in range(172)]
        for column, j in enumerate(PRIMARY_PHYSICAL_ROWS):
            delta[j] = z[column]/4
        delta[162] = -3*z[51]/8-5*z[52]/16
        delta = tuple(delta)
        physical = tuple(self.field.full_coefficients(candidate, exact=True))
        ideal_physical = tuple(a+b for a, b in zip(self.accepted_physical, delta))
        after_delta = tuple(a-b for a, b in zip(physical, self.accepted_physical))
        before_bad = [j for j, (lo, v, hi) in enumerate(zip(self.lower172, ideal_physical, self.upper172)) if not lo <= v <= hi]
        after_bad = [j for j, (lo, v, hi) in enumerate(zip(self.lower172, physical, self.upper172)) if not lo <= v <= hi]
        K, h = Q.from_float(float(x[62])), Q.from_float(float(x[63]))
        norm = 4*max(map(abs, delta)); rounded_norm = 4*max(map(abs, after_delta))
        interval = self.target_exact <= K <= Q(58) and 0 <= h <= self.maximum_h_exact
        record = {"schema": POLICY+"-exact-once-rounded-candidate", "model_binding_sha256": self.binding_sha256,
            "actual_backend_raw64": _vector(x), "backend_order": "z62,K,h",
            "literal_z62_exact_binary64": [str(v) for v in z],
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
            "rounded_physical_norm_le_raw_h_exact_pass": bool(rounded_norm <= h),
            "raw_h_minus_rounded_physical_norm_exact": str(h-rounded_norm),
            "raw_h_is_never_repaired_after_return": True,
            "explicit_retained_hmax_pass": bool(norm <= self.maximum_h_exact and rounded_norm <= self.maximum_h_exact),
            "original_box_and_K_h_pass": bool(interval and not before_bad and not after_bad
                and norm <= self.maximum_h_exact and rounded_norm <= self.maximum_h_exact),
            "unrounded_backend_norm_rows_use_original_linear_tolerance": True,
            "rounded_physical_norm_to_raw_h_is_a_separate_exact_qualification_gate": True,
            "exact_original_null_height_map_used_after_independent_rounding": True,
            "physical_height_coefficients_were_not_separately_rounded": True,
            "original_total_height_and_body_height_null_identities_retained": True,
            "old_R0_equalities_are_not_imposed": True,
            "all62_actual_nonzero_suffix_control_directions_are_available": True,
            "four_original_exact_suffix_zero_independent_controls_are_fixed": [153, 154, 155, 156],
            "same_fixed_g_and_permanent_c0_b0": True,
            "physical_state_sha256": digest(self.field.identity(candidate)),
            "original_actual58_physical_state_sha256": self.binding["accepted_physical_state_sha256"],
            "whole_body_prediction_and_actual14_not_yet_evaluated": True}
        return candidate, record

    def _new_fields(self, q, label, indices):
        fields = {"_theta": self.thetas[label][None, :]}
        for name, columns, modes, body_columns in (
                ("u", range(54, 81), 9, range(159, 163)),
                ("v", range(129, 153), 8, range(163, 167))):
            delta = np.asarray([float(Q.from_float(float(q[i]))-Q.from_float(float(self.ring_candidate168[i])))
                                for i in columns]).reshape(3, modes)
            body_delta = np.asarray([float(Q.from_float(float(q[i]))-Q.from_float(float(self.ring_candidate168[i])))
                                     for i in body_columns])
            family = self.families[label][name]
            fields[name] = {}
            for order, key in enumerate(("value", "s", "ss")):
                fields[name][key] = self.seed_fields[label][name][key][indices]+np.einsum(
                    "ri,ik,tk->rt", self.last3_radial[order][indices], delta, family["angular"])
            fields[name]["theta"] = self.seed_fields[label][name]["theta"][indices]+np.einsum(
                "ri,ik,tk->rt", self.last3_radial[0][indices], delta, family["angular_first"])
            if np.any(body_delta != 0.):
                angle = family["angular"][:, :4]@body_delta
                first = family["angular_first"][:, :4]@body_delta
                for order, key in enumerate(("value", "s", "ss")):
                    fields[name][key] += self.body_radial[name][order][indices]*angle[None, :]
                fields[name]["theta"] += self.body_radial[name][0][indices]*first[None, :]
        return fields

    def _height_for(self, q):
        delta = np.asarray([float(Q.from_float(float(q[i]))-Q.from_float(float(self.ring_candidate168[i])))
                            for i in HEIGHT_STATE_ROWS])
        if not np.any(delta != 0.):
            return {**self.seed_height, "paid_baseline_only": True}
        return {name: _finite(self.seed_height[name]+self.height_basis[name]@delta,
                             (len(self.radial),), "actual incremented height "+name)
                for name in ("b", "b_s")} | {"paid_baseline_only": False}

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
        self.temporary.evict("geometry", int(self.loaded_geometry is not None))
        self.temporary.evict("physical_derivative_blocks", len(self.derivative_input_cache))
        self.temporary.evict("final_J", int(self.loaded_J is not None))
        self.loaded_geometry = None; self.loaded_geometry_key = None
        self.derivative_input_cache.clear()
        self.loaded_J = None; self.loaded_J_key = None
        trace = _Trace(self.wall, sink)
        is_paid = _same(q, self.ring_candidate168)
        if is_paid:
            self.full_point_counts["paid_seed_hits"] += 1
        else:
            self.full_point_counts["started"] += 1
            if key in self.seen_geometry_keys:
                self.full_point_counts["recomputed_after_eviction"] += 1
            else:
                self.seen_geometry_keys.add(key)
                self.full_point_counts["distinct_new_physical_points"] += 1
        ordinal = self.full_point_counts["started"]
        partial = {"schema": POLICY+"-geometry-partial", "status": "entered", "state168": q,
            "new_geometry_ordinal": None if is_paid else ordinal, "paid_q_R_reuse": bool(is_paid),
            "completed_grids": {}, "working_grid": None}
        sink["_last_geometry_partial"] = partial
        tick = time.monotonic()
        try:
            self.height = trace.run("height_inputs_for_actual_q",
                lambda: self._height_for(q),
                lambda v: partial.__setitem__("height_inputs", v),
                paid_height_baseline_identity_reused=True)
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
            answer = {"state168": q, "grids": grids, "height_inputs": self.height, "paid_q_R_reuse": bool(is_paid),
                "new_geometry_ordinal": None if is_paid else ordinal}
            # Keep only this current geometry; old arrays are not rebuilt for reporting.
            partial.update(status="complete", geometry=answer)
            self.loaded_geometry_key, self.loaded_geometry = key, answer
            sink["_last_complete_geometry"] = answer
            if not is_paid:
                self.full_point_counts["completed"] += 1
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

    def _value(self, backend, sink, *, state168=None):
        x = _finite(backend, (64,), "new backend value input")
        _require(x[62] > 0, "positive actual backend K required")
        q = self.point_from_backend(x) if state168 is None else state168
        geometry = self._geometry(q, sink)
        values, summaries = [], {}; trace = _Trace(self.wall, sink)
        for label in LABELS:
            grid = geometry["grids"][label]
            _, scaled = trace.run("current_K_suffix_PSD_value_read_or_assembly",
                lambda grid=grid: self._curvature_at_K(grid, float(x[62])), grid=label, K=float(x[62]))
            values.append(np.concatenate((grid["metric_rows"], scaled), axis=-1).ravel())
            summaries[label] = self._grid_summary(label, grid, float(x[62]), scaled)
        values.append(self.linear_b-self.linear_A@x)
        raw = _finite(np.concatenate(values), (self.constraint_count,), "whole-suffix residual")
        return {"backend": x, "state168": q, "values": raw, "summaries": summaries,
            "whole_suffix_pass": bool(all(s["all_metric_curvature_area_gates_pass"] for s in summaries.values())),
            "geometry_key": q.tobytes(), "jacobian_key": q.tobytes()+np.asarray(x[62], dtype=np.float64).tobytes()}

    def _jacobian(self, entry, sink):
        key = entry["jacobian_key"]
        if key == self.loaded_J_key:
            self.jacobian_counts["cache_hits"] += 1
            return self.loaded_J
        self.assert_context()
        self.jacobian_counts["started"] += 1
        if key in self.seen_J_keys:
            self.jacobian_counts["reassembled_after_eviction"] += 1
        else:
            self.seen_J_keys.add(key)
            self.jacobian_counts["distinct_q_K_keys"] += 1
        ordinal = self.jacobian_counts["started"]
        geometry = self._geometry(entry["state168"], sink)
        K = float(entry["backend"][62]); factor = K/self.curvature_scale
        J = np.empty((self.constraint_count, 64), dtype=np.float64)
        partial = {"status": "entered", "ordinal": ordinal, "backend64": entry["backend"],
            "matrix": J, "completed_column_blocks": [], "working_kernel_arrays": None}
        sink["_last_jacobian_partial"] = partial
        trace = _Trace(self.wall, sink); tick = time.monotonic()
        families = (
            ("u", list(range(0, 27))+list(range(53, 57)), 9, ((0, 27), (53, 57))),
            ("v", list(range(27, 51))+list(range(57, 61)), 8, ((27, 51), (57, 61))),
            ("height", list(HEIGHT_BACKEND_COLUMNS), 3, ((51, 53), (61, 62))))
        try:
            offset = 0
            for label in LABELS:
                grid = geometry["grids"][label]
                nr, nt = len(self.radial), len(self.thetas[label])
                cfull, _ = self._curvature_at_K(grid, K)
                E, F, G, q = (cfull[name] for name in ("E", "F", "G", "q"))
                h11, h12, h22 = (cfull[name]*factor for name in ("h11", "h12", "h22"))
                dtrace = q*(E+G)/self.curvature_scale
                ddet = (q/self.curvature_scale)[..., None]*(E[..., None]*h22+G[..., None]*h11-2*F[..., None]*h12)
                dk = np.stack((np.zeros_like(q), np.zeros_like(q), dtrace, ddet[..., 0], dtrace, ddet[..., 1]), axis=-1)
                J[offset:offset+nr*nt*6, 62] = dk.ravel(); J[offset:offset+nr*nt*6, 63] = 0.
                partial["completed_column_blocks"].append({"grid": label, "family": "K_h_all_original_rows",
                    "row_start": offset, "row_stop": offset+nr*nt*6, "column_start": 62, "column_stop": 64})
                for fixed_ri in self.fixed_radial_indices:
                    first_row, last_row = offset+int(fixed_ri)*nt*6, offset+(int(fixed_ri)+1)*nt*6
                    J[first_row:last_row, :62] = 0.
                    partial["completed_column_blocks"].append({"grid": label, "family": "exact_original_support_zero",
                        "row_start": first_row, "row_stop": last_row, "column_start": 0, "column_stop": 62,
                        "zero_is_the_proved_control_derivative_not_unfilled_memory": True,
                        "original_radial_id": int(self.radial_ids[fixed_ri])})
                for begin in range(0, len(self.mutable_radial_indices), OWNED_WIDTH):
                    _wall(self.wall, POLICY+".J.block")
                    owned = self.mutable_radial_indices[begin:begin+OWNED_WIDTH]
                    end = int(owned[-1])+1
                    count = len(owned)*nt
                    ri = np.repeat(np.arange(len(owned)), nt); ti = np.tile(np.arange(nt), len(owned))
                    global_ri = owned[ri]
                    row_start, row_stop = offset+int(owned[0])*nt*6, offset+end*nt*6
                    fields, frame = None, None
                    metric = {name: v[owned] for name, v in self.metric.items()}
                    small = {name: grid["jets"][name][global_ri, ti] for name in POSITION_KEYS}
                    small["T"] = grid["T"][global_ri, ti]
                    cv = {name: (v[global_ri, ti] if isinstance(v, np.ndarray) and v.shape[:2] == (nr, nt) else v)
                          for name, v in cfull.items()}
                    e, f = grid["e"][global_ri, ti], grid["f"][global_ri, ti]
                    for name, columns, modes, completed_ranges in families:
                        derivative_key = (entry["geometry_key"], label, begin, end, name)
                        if derivative_key in self.derivative_input_cache:
                            self.derivative_input_counts["cache_hits"] += 1
                            d = self.derivative_input_cache[derivative_key]
                        else:
                            self.derivative_input_counts["started"] += 1
                            if derivative_key in self.seen_derivative_keys:
                                self.derivative_input_counts["recomputed_after_eviction"] += 1
                            else:
                                self.seen_derivative_keys.add(derivative_key)
                                self.derivative_input_counts["distinct_input_keys"] += 1
                            try:
                                if name == "height":
                                    kernels = None
                                    def height_virtual():
                                        values = {jet: np.zeros((count, 3, 3), dtype=float)
                                                  for jet in POSITION_KEYS+("T",)}
                                        values["Xs"][:, 2, :] = self.height_basis["b"][global_ri]/4
                                        values["Xss"][:, 2, :] = self.height_basis["b_s"][global_ri]/4
                                        return values
                                    virtual = trace.run("new_height_position_J_inputs", height_virtual,
                                        lambda v: partial.__setitem__("working_virtual_position_J", v),
                                        grid=label, original_radial_ids=self.radial_ids[owned].tolist(),
                                        independent_height_rows=list(HEIGHT_STATE_ROWS))
                                else:
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
                                data = dict(small); data.update({"jac_"+jet: value for jet, value in virtual.items()})
                                U, T = small["Xs"], small["T"]
                                de = 2*np.einsum("ic,icn->in", U, virtual["Xs"])
                                df = np.einsum("ic,icn->in", T, virtual["Xs"])+np.einsum("ic,icn->in", U, virtual["T"])
                                differentials = _curvature_differentials(data, self.metric["a"][global_ri], cv)
                                differentials["metric0"] = spectral_parameter_rows(e, f, de, df, np.zeros(count, dtype=int), self.epsilon)
                                differentials["metric1"] = spectral_parameter_rows(e, f, de, df, np.ones(count, dtype=int), self.epsilon)
                                if name == "height":
                                    # The complete physical null-height direction is already in Xs/Xss.
                                    d = differentials
                                else:
                                    d = {}
                                    for quantity, value in differentials.items():
                                        old = expand_radial_rows(value, self.last3_radial, global_ri)/4
                                        first4 = value.reshape(count, 3, modes)[:, :, :4].reshape(count, 12)
                                        body = expand_radial_rows(first4, self.body_radial[name], global_ri)/4
                                        d[quantity] = np.concatenate((old, body), axis=1)
                                _require(all(value.shape == (count, len(columns)) and np.all(np.isfinite(value)) for value in d.values()),
                                         "complete finite full62 K-independent physical differentials required")
                                partial["working_contracted_physical_differentials"] = d
                                self.derivative_input_cache[derivative_key] = d
                                self.derivative_input_counts["completed"] += 1
                                partial["working_kernel_arrays"] = None
                                partial.pop("working_virtual_position_J", None)
                                del kernels, virtual, data, de, df, differentials
                            except Exception:
                                self.derivative_input_counts["failed"] += 1
                                raise
                        cj = trace.run("new_K_dependent_PSD_J_assembly", lambda: _curvature_rows_from_differentials(
                            cv, d, K, self.curvature_scale),
                            lambda v: partial.__setitem__("working_K_dependent_PSD_J", v),
                            grid=label, family=name, K=K)
                        six = np.concatenate((d["metric0"][:, None, :], d["metric1"][:, None, :], cj), axis=1)
                        contracted = six.reshape(count*6, len(columns))
                        _require(contracted.shape == (count*6, len(columns)) and np.all(np.isfinite(contracted)),
                                 "finite complete full62 physical J block required")
                        J[row_start:row_stop, np.asarray(columns, dtype=int)] = contracted
                        for first, stop in completed_ranges:
                            partial["completed_column_blocks"].append({"grid": label, "family": name,
                                "row_start": row_start, "row_stop": row_stop,
                                "column_start": first, "column_stop": stop})
                        partial["working_kernel_arrays"] = None
                        partial.pop("working_contracted_physical_differentials", None)
                        partial.pop("working_K_dependent_PSD_J", None)
                        del d, cj, six, contracted
                    partial.pop("working_derivative_frame", None)
                offset += nr*nt*6
            J[offset:] = -self.linear_A
            partial["completed_column_blocks"].append({"family": "original_linear_rows",
                "row_start": offset, "row_stop": self.constraint_count, "column_start": 0, "column_stop": 64})
            _require(offset == self.nonlinear_constraint_count and np.all(np.isfinite(J)), "complete finite64 Jacobian required")
            J.setflags(write=False); partial.update(status="complete", matrix_binding=array_binding(J))
            self.jacobian_counts["completed"] += 1
            self.temporary.evict("final_J", int(self.loaded_J is not None))
            self.loaded_J_key, self.loaded_J = key, J
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
            "variables": 64, "independent_nonzero_suffix_controls": 62,
            "new_controls_beyond_closed_full51": 11, "nonzero_physical_rows": 63,
            "excluded_exact_suffix_zero_controls": [153, 154, 155, 156],
            "constraint_count": self.constraint_count,
            "nonlinear_constraint_count": self.nonlinear_constraint_count,
            "suffix_radial_ids": self.radial_ids.tolist(), "suffix_radial_count": len(self.radial),
            "new_value_and_physical_J_original_radial_ids": self.radial_ids[self.mutable_radial_indices].tolist(),
            "literal_paid_fixed_geometry_original_radial_ids": self.radial_ids[self.fixed_radial_indices].tolist(),
            "fixed_rows_still_have_current_K_PSD_and_K_derivatives": True,
            "theta_counts": {label: len(self.thetas[label]) for label in LABELS},
            "initial_backend_seed64": _vector(self.x0), "metric_budget": self.metric_budget,
            "maximum_h_exact": str(self.maximum_h_exact),
            "maximum_h_is_explicit_retained_cap_not_claimed_full62_box_sufficient": True,
            "K_interval_exact": [str(self.target_exact), "58"],
            "backend_K_lower_binary64": self.target_lower, "backend_K_lower_exact_binary64": str(Q.from_float(self.target_lower)),
            "backend_z_bounds_are_inward_original_box_only": True,
            "new_scientific_arrays_are_not_published_or_future_free_inputs": True,
            "new_geometry_counts": copy.deepcopy(self.full_point_counts), "new_J_counts": copy.deepcopy(self.jacobian_counts),
            "K_independent_derivative_input_counts": copy.deepcopy(self.derivative_input_counts),
            "all_suffix_rows_enter_solver": True, "new_last3_radial_basis": copy.deepcopy(self.basis_receipt),
            "new_body_and_tail_height_basis": copy.deepcopy(self.body_height_receipt),
            "same_fixed_metric_and_permanent_c0_b0": True,
            "actual_height_is_allowed_to_change_in_three_exact_null_directions": True,
            "same_mathematical_original_field_different_floating_summation_order": True,
            "paid_q_R_T_jets_metric_PSD_area_principal_are_read_only": True,
            "qualified_return_only_authorizes_external_canonical_wholebody_prediction": True,
            "actual14_and_reach_not_claimed": True,
            "initial_summaries": None if self.initial_entry is None else copy.deepcopy(self.initial_entry["summaries"]),
            "last_summaries": None if self.last_entry is None else copy.deepcopy(self.last_entry["summaries"])}

    def full_record(self):
        return {"schema": POLICY+"-full-model", "definition": definition(), "summary": self.summary(),
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "build_receipt": _compact(_public(self.build_sink)),
            "accepted_state168": _vector(self.accepted_state168), "paid_unaccepted_q_R168": _vector(self.ring_candidate168),
            "exact_injection": copy.deepcopy(self.coordinate_record),
            "original_lower172_exact": [str(v) for v in self.lower172],
            "original_upper172_exact": [str(v) for v in self.upper172],
            "backend_z_bounds": copy.deepcopy(self.backend_bound_receipt),
            "new_original_last3_radial_jet_bindings": [_array_receipt(v) for v in self.last3_radial],
            "new_body_radial_bindings": {name: [_array_receipt(v) for v in values] for name, values in self.body_radial.items()},
            "new_height_basis_bindings": {name: _array_receipt(v) for name, v in self.height_basis.items()},
            "new_body_height_basis_receipt": copy.deepcopy(self.body_height_receipt),
            "new_linear_A_binding": _array_receipt(self.linear_A),
            "new_linear_b_binding": _array_receipt(self.linear_b),
            "linear_row_tags": copy.deepcopy(self.linear_tags),
            "paid_input_arrays_referenced_in_original_source_receipt_not_duplicated": True,
            "new_scientific_arrays_not_published_or_future_free_inputs": True,
            "SOLVE_TRACE_contains_only_compact_completion_and_cost_receipts": True,
            "temporary_intermediate_cache_is_not_published_or_future_free_input": True}


def build_full62_whole_suffix_model(
        field, accepted_state168, ring_candidate168, paid_free_model, paid_free_solution, paid_prefix_model,
        cfg, lower172, upper172, source_receipt, wall, capture=None, *, metric_budget, charge_prepare):
    """Restore pinned full records, then pay once for only genuinely missing inputs."""
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty new whole-suffix build capture required")
    _require(callable(wall) and callable(charge_prepare), "external clock and one prepare charge required")
    sink.update(schema=POLICY+"-build-capture", status="entered", source_receipt=copy.deepcopy(source_receipt))
    model = Full62WholeSuffixModel(); sink["_object_model"] = model
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
        sink["prepare_charge_receipt"] = copy.deepcopy(charge_prepare({"schema": POLICY+"-prepare-charge",
            "new_exact_P172x62_affine_height_injection": 1,
            "new_last3_radial_basis_through_order2": 1,
            "new_body_P5_P8_radial_jets_through_order2": 1,
            "new_two_tail_null_height_b_and_b_s": 1,
            "new_original_box_linear_model": 1, "new_original_anchor_bounds": 1,
            "old34_kernel_or_old_inverse_calls": 0, "duplicate_original_angular_calls": 0,
            "new_initial_geometry_calls_in_builder": 0, "paid_prefix_suffix_value_recalculations": 0,
            "closed_whole34_and_full51_missing_arrays_not_consumed": True}))
        height_map = field.original_field.coordinates.basis.H
        expected_tail = ((0, 0),)*6+((1, 0), (0, 1), (Q(-3, 2), Q(-5, 4)))
        _require(all(tuple(height_map[row][3:5]) == tuple(map(Q, expected_tail[row]))
                     for row in range(9)), "literal original exact tail height map required")
        P = [[Q(0) for _ in range(62)] for _ in range(172)]
        for column, j in enumerate(PRIMARY_PHYSICAL_ROWS):
            P[j][column] = Q(1, 4)
        P[162][51], P[162][52] = Q(-3, 8), Q(-5, 16)
        model.exact_P = tuple(tuple(row) for row in P)
        model.P = np.asarray([[float(v) for v in row] for row in model.exact_P], dtype=np.float64)
        model.coordinate_record = {"schema": POLICY+"-literal-original-full62-affine-injection",
            "independent168_rows": list(ACTIVE_ROWS), "primary_physical172_rows": list(PRIMARY_PHYSICAL_ROWS),
            "nonzero_physical172_rows": sorted(list(PRIMARY_PHYSICAL_ROWS)+[162]),
            "columns": 62, "independent_increment_scale_exact": "1/4",
            "old_tail_u_columns": [0, 27], "old_tail_v_columns": [27, 51],
            "old_tail_height_columns": [51, 53], "new_body_u_columns": [53, 57],
            "new_body_v_columns": [57, 61], "new_body_height_column": 61,
            "coupled_physical_row162": {"51": "-3/8", "52": "-5/16"},
            "original_full_height_H9x5_exact": [[str(v) for v in row] for row in height_map],
            "physical_map": "original exact affine159-to163 map direct-sum identity9",
            "physical_nine_height_vector_never_separately_rounded": True,
            "all_other_independent_coefficients_fixed_at_accepted58": True,
            "excluded_exact_suffix_zero_independent_rows": [153, 154, 155, 156],
            "original17_R0_directions_still_free": True,
            "new11_are_genuine_suffix_controls_not_added_zero_columns": True,
            "old34_kernel_used_or_reconstructed": False,
            "rank62_reason": "62 distinct independent coordinate directions; original affine map is injective"}
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
        _require(model.maximum_h_exact == Q("18014398507545773/281474976710656"),
                 "literal retained h cap from the paid old51 scope required")
        model.maximum_h_float = _inward_float(model.maximum_h_exact, False)
        inputs = paid_prefix_model["new_paid_input"]
        nr = int(inputs["radial"]["shape"][0])
        radial = _paid_array(inputs["radial"], (nr,), "prefix full radial")
        ids = np.asarray([i for i, s in enumerate(radial) if Q.from_float(float(s)) >= Q(SUFFIX_LEFT_EXACT)], dtype=np.int64)
        _require(len(ids) == 21 and 141 in ids, "the complete original21-row suffix required")
        model.radial_ids = ids; model.radial = _finite(radial[ids], (21,), "whole suffix radial")
        model.metric = {name: _finite(_paid_array(inputs["fixed_metric"][name], (nr,), name)[ids], (21,), "suffix "+name)
                        for name in ("a", "a_s", "a_ss")}
        model.seed_height = {name: _finite(_paid_array(inputs["fixed_height_derivatives"][name], (nr,), name)[ids], (21,), "suffix "+name)
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
        trace = _Trace(wall, sink)
        model.last3_radial, model.basis_receipt = trace.run("new_missing_last3_radial_basis",
            lambda: _new_last3_basis(field, model.radial), lambda v: sink.__setitem__("_new_last3_radial", v[0]))
        model.body_radial, model.height_basis, model.body_height_receipt = trace.run(
            "new_missing_body_and_tail_height_basis",
            lambda: _new_body_and_tail_height_basis(field, model.radial),
            lambda v: sink.__setitem__("_new_body_height_arrays", {"body": v[0], "height": v[1]}))
        paid_radial_definition = paid_free_model["binding"]["literal_paid_threejet_embedding"]["original_paid_R2_definition"]
        model.support_right_exact = Q(paid_radial_definition["knots_exact"][-1])
        _require(model.support_right_exact == Q("423/500") and paid_radial_definition["full_spline_indices"] == [9, 10, 11],
                 "original exact last-three support identity required")
        right_ends = {
            "original_spline_exact": model.support_right_exact,
            "original_spline_binary64": Q(model.basis_receipt["original_support_right_exact_binary64"]),
            "original_null_height_exact": field.original_field.null_basis.right_exact,
            "original_null_height_binary64": Q.from_float(float(field.original_field.null_basis.right)),
            "original_body_exact": Q(BODY_RIGHT_EXACT),
            "original_body_binary64": Q.from_float(float(Q(BODY_RIGHT_EXACT)))}
        fixed_mask = np.asarray([all(Q.from_float(float(value)) >= endpoint for endpoint in right_ends.values())
                                  for value in model.radial], dtype=bool)
        model.fixed_radial_indices = np.flatnonzero(fixed_mask)
        model.mutable_radial_indices = np.flatnonzero(~fixed_mask)
        _require(len(model.mutable_radial_indices) > 0
                 and np.array_equal(model.mutable_radial_indices, np.arange(len(model.mutable_radial_indices))),
                 "same ordered original radial identities must give a mutable prefix and fixed terminal rows")
        model.fixed_row_receipt = {"all_original_support_right_endpoints_exact": {key: str(value) for key, value in right_ends.items()},
            "classification": "same Q(original binary64 s)>=every original exact and stored binary64 right endpoint",
            "original_fixed_radial_ids": model.radial_ids[model.fixed_radial_indices].tolist(),
            "original_mutable_radial_ids": model.radial_ids[model.mutable_radial_indices].tolist(),
            "fixed_s_exact_binary64": [str(Q.from_float(float(model.radial[i]))) for i in model.fixed_radial_indices],
            "both_grids_keep_all21_rows_and_current_K_constraints": True}
        sink["fixed_radial_row_reuse"] = copy.deepcopy(model.fixed_row_receipt)
        model.linear_A, model.linear_b, model.linear_tags = trace.run("new_full62_original_physical_linear_rows",
            lambda: _linear_rows(model.P, model.accepted_physical, model.lower172, model.upper172,
                                 model.maximum_h_exact, model.target_lower),
            lambda v: sink.__setitem__("_new_linear_arrays", {"A": v[0], "b": v[1]}))
        model.backend_z_bounds, model.backend_bound_receipt = trace.run("new_original_box_backend_bounds",
            lambda: _original_box_backend_bounds(model.accepted_independent_exact, model.accepted_physical, model.lower172, model.upper172),
            lambda v: sink.__setitem__("_new_backend_bounds", v[1]))
        model.x0 = _finite(np.r_[np.zeros(62), 58., 0.], (64,), "unique accepted58 initial backend")
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
            "new_exact_P172x62_sha256": digest([[str(v) for v in row] for row in model.exact_P]),
            "physical_coordinate_definition": copy.deepcopy(model.coordinate_record),
            "initial_backend64": _vector(model.x0),
            "original_box_backend_bounds": copy.deepcopy(model.backend_bound_receipt),
            "suffix_radial_ids": ids.tolist(), "radial": array_binding(model.radial),
            "theta": {label: array_binding(model.thetas[label]) for label in LABELS},
            "metric_budget_exact_binary64": str(Q.from_float(model.metric_budget)),
            "K_lower_exact": str(model.target_exact), "K_lower_binary64": model.target_lower,
            "K_lower_exact_binary64": str(Q.from_float(model.target_lower)),
            "maximum_h_exact": str(model.maximum_h_exact), "maximum_h_inward_binary64": model.maximum_h_float,
            "maximum_h_semantics": "explicit retained cap from paid old51, not asserted sufficient for all62 box",
            "new_last3_radial_basis": copy.deepcopy(model.basis_receipt),
            "fixed_radial_row_reuse": copy.deepcopy(model.fixed_row_receipt),
            "new_last3_radial_jets": [array_binding(v) for v in model.last3_radial],
            "new_body_height_basis_receipt": copy.deepcopy(model.body_height_receipt),
            "new_linear_A": array_binding(model.linear_A), "new_linear_b": array_binding(model.linear_b),
            "all_original_suffix_rows_preserved": True,
            "same_mathematical_original_field_different_floating_summation_order": True,
            "canonical_wholebody_prediction_and_actual14_remain_external": True,
            "implementation_hashes": implementation_hashes()}
        model.binding_sha256 = digest(model.binding)
        _require(_same(model.point_from_backend(model.x0), q58), "exact zero-increment initial point must reproduce accepted58")
        model.temporary = _CurrentArrays(wall, sink)
        model.status = "ready"
        sink.update(status="complete", model_binding_sha256=model.binding_sha256, binding=copy.deepcopy(model.binding),
                    no_paid_prefix_suffix_value_or_old_kernel_replayed=True,
                    closed_whole34_and_full51_missing_arrays_not_free_or_consumed=True)
        _wall(wall, POLICY+".build.complete")
        return model
    except Exception as error:
        sink.update(status="raised", error=_error(error)); model.status = "build-raised"
        raise
    finally:
        sink["local_elapsed_seconds"] = time.monotonic()-tick




def solve_full62_whole_suffix_once(
        model, *, wall, charge_solve, emit=None, capture=None,
        solver_seconds=SOLVER_SECONDS, maxiter=320, max_evaluations=MAX_EVALUATIONS,
        max_backend_evaluations=MAX_BACKEND_EVALUATIONS):
    """Public lazy bridge; the dedicated solver source owns the one attempt."""
    from frame_metric_current168_full62_whole_suffix_solver import solve_full62_whole_suffix_once as run_once
    return run_once(model, wall=wall, charge_solve=charge_solve, emit=emit, capture=capture,
        solver_seconds=solver_seconds, maxiter=maxiter, max_evaluations=max_evaluations,
        max_backend_evaluations=max_backend_evaluations)


def full62_whole_suffix_capture_record(capture, *, include_arrays=False):
    """Compact existing records only; no scientific evaluation is requested."""
    from frame_metric_current168_full62_whole_suffix_solver import full62_whole_suffix_capture_record as record
    return record(capture, include_arrays=include_arrays)

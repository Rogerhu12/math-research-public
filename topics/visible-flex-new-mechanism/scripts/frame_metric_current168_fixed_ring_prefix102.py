#!/usr/bin/env python3
"""One new full-body restoration fiber with a paid feasible ring held fixed.

Import-only.  No research, source-log read, ordinary geometry, old optimizer,
developer check, import-time numerical experiment or automatic restart occurs.
The external task owns every clock, source receipt, original input and actual
fourteen-gate evaluation.  Only the first six original radial u/v coefficient
blocks vary.  Their complete original zero extensions vanish for s>=.765;
the paid, once-rounded ring candidate is never promoted to an accepted point.

The finite nonlinear problem has 102 physical increments and one phase-I
slack.  Its fixed rows are the original pools' metric/curvature rows plus both
complete bad circles 111/131.  Full-grid nonlinear values are also formed at
every new point.  The returned backend point, or the already complete initial
point if it passes all global gates, must also pass the exact original172 box.  Active rows alone,
backend success, or a small phase-I slack never certify a whole body.
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
from frame_complete_body_extension168 import CompleteBody168Field, array_binding
from frame_complete_body_extension168_joint_selected import _context, _families
from frame_complete_body_extension168_curvature_prediction import _validate_metric
from frame_selected_row_radial_jacobian import angular_kernels, virtual_selected_jets, expand_radial_rows
from frame_metric_spectral_recovery import spectral_proposal_rows, spectral_parameter_rows
from frame_curvature_psd import curvature_values, curvature_parameter_jacobian, independent_principal_curvatures
from frame_height_null_coordinates import digest
from frame_metric_current168_ring17 import _require, _error, _wall, _q, _bounds, _vector, _payload, _raw_numeric
from frame_metric_current168_reflected_R1_ray import _raw_all_fields


POLICY = "true58-fixed-ring-prefix102-body-repair-v1"
LABELS = ("coarse", "fine")
PREFIX_COLUMNS = tuple(range(54))+tuple(range(81, 129))
PAID_RING_COLUMNS = tuple(range(54, 81))+tuple(range(129, 153))
IMMUTABLE_COLUMNS = tuple(i for i in range(168) if i not in PREFIX_COLUMNS)
SUFFIX_LEFT_EXACT = "153/200"
BAD_RADIAL_INDICES = (111, 131)
BAD_RADIAL_LABELS = (0.585, 0.7125)
ORIGINAL_GROUPS = (0, 1, 7, 8, 9, 10)
ROW_NAMES = ("metric_plus", "metric_minus", "plus_trace", "plus_determinant", "minus_trace", "minus_determinant")
POSITION_KEYS = ("Xs", "Xt", "Xss", "Xst", "Xtt")
SCALAR_KEYS = ("value", "s", "ss", "theta")
VARIABLES = 103
OWNED_WIDTH = 4
MAX_EVALUATIONS = 240
SOLVER_SECONDS = 180.
SLSQP_OPTIONS = {"maxiter": 120, "ftol": 1.e-9, "disp": False}


class FixedRingPrefix102Limit(RuntimeError):
    """A real new-scope limit, without a substitute solver result."""


def definition():
    return {
        "schema": POLICY, "accepted_source_index": 58,
        "base": "paid free36 once-rounded unaccepted ring candidate",
        "accepted_state_is_not_replaced_by_the_ring_seed": True,
        "backend_order": "102 original physical coefficient increments, phase_I_slack",
        "prefix_columns168_and172": list(PREFIX_COLUMNS),
        "unchanged_columns168": list(IMMUTABLE_COLUMNS),
        "radial_basis": "original B3..B8 with their original entry weights and zero extensions",
        "fixed_suffix_left_exact": SUFFIX_LEFT_EXACT,
        "ring_fiber_proof": "R514 section11; no new rank or old three-jet identity check",
        "fixed_suffix": "same full scalar and position two-jets, fixed height and all original endpoints",
        "physical_box": "literal original172 box, restricted to 102 unit physical columns",
        "no_new_trust_radius_or_old_norm_guard_migration": True,
        "objective": "minimize one nonnegative common normalized phase-I slack",
        "finite_rows": "original metric/curvature pool rows plus complete two-grid circles111/131",
        "finite_constraints": "g_i(z)/s_i+slack>=0; s_i fixed after the first paid analytic Jacobian",
        "fixed_scales": "max(1,abs(initial g_i),max(abs(initial analytic J_i)))",
        "metric_budget": "literal accepted58 eta minus the original required actual decrease",
        "metric_rows": "original smooth two spectral rows with unchanged original epsilon",
        "curvature_rows": "original four scaled PSD rows at original actual I,II and normal area",
        "full_grid_values_at_each_new_point": True,
        "all_grid_metric_unsmoothed_PSD_direct_kappa_area_required_for_qualification": True,
        "body_positions_other_than_the_five_derivative_jets_not_constructed": True,
        "remaining_original_fourteen_gates_are_external_actual_only": True,
        "full_field": "original field.scalar_frame at the actual binary64 point, full theta Pi",
        "value_position_jets": "original a/as/ass and fixed b/bs, no center or X query",
        "analytic_J": "original angular_kernels/virtual_selected_jets, u54+v48, owned radial width4",
        "no_full_grid_by_102_position_J_tensor": True,
        "rounding": "exact rational ring_seed plus exact binary64 raw increment, once converted",
        "Jacobian_scope": "continuous original field derivative at that binary64 point; not a derivative of rounding",
        "solver": "one scipy.optimize.minimize(method='SLSQP')",
        "options": copy.deepcopy(SLSQP_OPTIONS),
        "max_new_complete_points": MAX_EVALUATIONS,
        "solver_seconds": SOLVER_SECONDS,
        "the_prepared_initial_full_value_is_reused_when_its_Jacobian_is_first_paid": True,
        "maxima_and_finite_nonlinear_success_are_not_continuous_certificates": True,
        "zero_old_solver_developer_ordinary_or_old_J_calls": True,
        "candidate_selection": "actual backend return, or prepared initial point if it already passes every full-grid gate",
        "an_unreturned_intermediate_solver_callback_point_cannot_be_promoted": True,
        "no_restart_or_rowset_resolve": True}


def implementation_hashes():
    names = (Path(__file__).name, "frame_collar_bvp.py", "frame_complete_body_extension168.py",
             "frame_complete_body_extension168_joint_selected.py",
             "frame_complete_body_extension168_curvature_prediction.py",
             "frame_selected_row_radial_jacobian.py", "frame_entry_single_q.py",
             "frame_metric_spectral_recovery.py", "frame_curvature_psd.py",
             "frame_metric_current168_ring17.py", "frame_metric_current168_reflected_R1_ray.py")
    return {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}


def _finite(value, shape, name, *, copy_array=True):
    a = np.asarray(value, dtype=np.float64)
    _require(a.shape == tuple(shape) and np.all(np.isfinite(a)), "finite "+name+" with original shape required")
    a = a.copy() if copy_array else a.view()
    a.setflags(write=False)
    return a


def _same(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def _public(value):
    return {key: copy.deepcopy(item) for key, item in value.items() if not str(key).startswith("_")}


def _numeric(value):
    if isinstance(value, np.ndarray):
        return _payload(value) if np.all(np.isfinite(value)) else _raw_numeric(value)
    if isinstance(value, dict):
        return {str(key): _numeric(item) for key, item in value.items() if not str(key).startswith("_object")}
    if isinstance(value, (list, tuple)):
        return [_numeric(item) for item in value]
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    if isinstance(value, (np.integer, int)):
        return int(value)
    if isinstance(value, (float, np.floating)):
        x = float(value)
        return x if math.isfinite(x) else ("NaN" if math.isnan(x) else ("+Infinity" if x > 0 else "-Infinity"))
    if value is None or isinstance(value, str):
        return value
    return {"unserialized_type": type(value).__name__, "numeric_value_not_saved": True}


def _slice_radial(value, indices, nr):
    if isinstance(value, dict):
        return {key: _slice_radial(item, indices, nr) for key, item in value.items()}
    if isinstance(value, np.ndarray) and value.ndim and value.shape[0] == nr:
        return value[indices]
    return value


def _selected_curvature(values, ri, ti, shape):
    return {key: (item[ri, ti] if isinstance(item, np.ndarray) and item.shape[:2] == shape else item)
            for key, item in values.items()}


def _derivative_frame_parts(fields):
    """Only the original two derivative parts; no paid T/U/value regenerated."""
    v = fields["v"]["value"]
    psi = fields["_theta"]+fields["u"]["value"]
    zero = np.zeros_like(v)
    H = np.stack((-np.sin(psi), np.cos(psi), zero), axis=-1)
    N = np.stack((np.cos(psi), np.sin(psi), zero), axis=-1)
    ez = np.zeros_like(H); ez[..., 2] = 1.
    c = 1/np.sqrt(1+v*v)
    Tu = -c[..., None]*N
    Tv = (c**3)[..., None]*(ez-v[..., None]*H)
    Tuu = -c[..., None]*H
    Tuv = (v*c**3)[..., None]*N
    Tvv = ((2*v*v-1)*c**5)[..., None]*H-(3*v*c**5)[..., None]*ez
    us, vs = fields["u"]["s"], fields["v"]["s"]
    return {"Tpart": {"u": Tu, "v": Tv}, "Ts_value_part": {
        "u": us[..., None]*Tuu+vs[..., None]*Tuv,
        "v": us[..., None]*Tuv+vs[..., None]*Tvv}}


def _inward_float(value, lower):
    x = float(value)
    _require(math.isfinite(x), "finite original remaining box required")
    if ((Q.from_float(x) < value) if lower else (Q.from_float(x) > value)):
        x = float(np.nextafter(x, np.inf if lower else -np.inf))
    return x


class _Trace:
    def __init__(self, wall, sink):
        self.wall, self.sink = wall, sink
        self.events = sink.setdefault("component_events", [])
        self.counts = sink.setdefault("component_counts", {})

    def run(self, kind, operation, retain=None, **metadata):
        _wall(self.wall, POLICY+"."+kind+".before")
        counter = self.counts.setdefault(kind, {"started": 0, "completed": 0, "failed": 0, "elapsed_seconds": 0.})
        counter["started"] += 1
        event = {"kind": kind, "ordinal": counter["started"], "status": "started", **copy.deepcopy(metadata)}
        self.events.append(event)
        tick = time.monotonic()
        try:
            result = operation()
            if retain is not None:
                retain(result)
            event["status"] = "complete"
            counter["completed"] += 1
        except Exception as error:
            event.update(status="raised", error=_error(error))
            counter["failed"] += 1
            raise
        finally:
            event["elapsed_seconds"] = time.monotonic()-tick
            counter["elapsed_seconds"] += event["elapsed_seconds"]
        _wall(self.wall, POLICY+"."+kind+".after")
        return result


class FixedRingPrefix102Model:
    def __init__(self):
        self.status = "not-built"
        self.solve_attempted = False
        self.binding = None
        self.binding_sha256 = None
        self.solver_sink = None
        self.row_scales = None
        self.full_point_counts = {"started": 0, "completed": 0, "failed": 0}
        self.jacobian_counts = {"started": 0, "completed": 0, "failed": 0}
        self.full_evaluation_records = []
        self.last_entry = None
        self.initial_entry = None

    def assert_context(self):
        self.field._assert_context()
        _require(self.field.definition_sha256 == self.binding["field_definition_sha256"]
                 and self.field.coordinate_definition_sha256 == self.binding["coordinate_definition_sha256"]
                 and digest(self.cfg) == self.binding["configuration_sha256"],
                 "fixed field/cfg identity changed during the new fiber")
        _wall(self.wall, "prefix102.context")

    def point_from_increment(self, z, *, include_record=False):
        z = _finite(z, (102,), "prefix102 increment")
        proposed = self.ring_candidate168.copy()
        exact_delta = tuple(Q.from_float(float(v)) for v in z)
        exact = [Q.from_float(float(v)) for v in proposed]
        for j, column in enumerate(PREFIX_COLUMNS):
            exact[column] += exact_delta[j]
            proposed[column] = float(exact[column])
        _require(np.all(np.isfinite(proposed)), "finite once-rounded complete168 candidate required")
        physical = tuple(self.field.full_coefficients(proposed, exact=True))
        exact_before_physical = list(self.seed_physical)
        for j, column in enumerate(PREFIX_COLUMNS):
            exact_before_physical[column] += exact_delta[j]
        before_ok = all(lo <= value <= hi for lo, value, hi in zip(self.lower172, exact_before_physical, self.upper172))
        after_ok = all(lo <= value <= hi for lo, value, hi in zip(self.lower172, physical, self.upper172))
        unchanged = _same(proposed[list(IMMUTABLE_COLUMNS)], self.ring_candidate168[list(IMMUTABLE_COLUMNS)])
        _require(unchanged, "immutable ring/suffix coefficients changed")
        if not include_record:
            return proposed
        source_physical = tuple(self.accepted_physical)
        increment_all = tuple(a-b for a, b in zip(physical, source_physical))
        record = {
            "schema": POLICY+"-actual-candidate",
            "accepted_source_index": 58,
            "ring_seed_was_not_accepted": True,
            "model_binding_sha256": self.binding_sha256,
            "raw_prefix102": _vector(z),
            "unrounded_independent168_exact": [str(value) for value in exact],
            "unrounded_physical172_exact": [str(value) for value in exact_before_physical],
            "rounded_independent168": _vector(proposed),
            "rounded_physical172_exact": [str(value) for value in physical],
            "rounding_difference_independent168_exact": [str(Q.from_float(float(v))-e) for v, e in zip(proposed, exact)],
            "physical_increment_from_accepted58_exact": [str(value) for value in increment_all],
            "four_times_actual_physical_step_infinity_exact": str(4*max(map(abs, increment_all))),
            "no_new_small_trust_or_old_h_cap_imposed": True,
            "unrounded_original172_box_pass": bool(before_ok),
            "rounded_original172_box_pass": bool(after_ok),
            "original_exact_box_pass": bool(before_ok and after_ok),
            "immutable_suffix_coordinates_unchanged": bool(unchanged),
            "physical_state_sha256": digest(self.field.identity(proposed)),
            "whole_body_original_fourteen_gates_not_yet_evaluated": True}
        return proposed, record

    def _grid_summary(self, label, data, *, radial_indices=None):
        rids = np.arange(len(self.radial), dtype=int) if radial_indices is None else np.asarray(radial_indices, dtype=int)
        _require(len(rids) > 0, "nonempty original grid subset required")
        eta = data["eta"][rids]
        principal = data["principal"][rids]
        psd = data["curvature_rows_scaled"][rids]
        area = data["curvature"]["q"][rids]
        e_at = np.unravel_index(int(np.argmax(eta)), eta.shape)
        k_at = np.unravel_index(int(np.argmax(abs(principal))), principal.shape)
        amin = np.unravel_index(int(np.argmin(area)), area.shape)
        maximum_eta = float(eta[e_at])
        maximum_k = float(abs(principal[k_at]))
        minima = np.min(psd, axis=(0, 1))
        gates = {
            "strict_metric_decrease_budget": bool(maximum_eta <= self.metric_budget),
            "original_scaled_four_PSD_rows": bool(np.min(minima) >= -self.curvature_row_tolerance),
            "original_direct_curvature": bool(maximum_k <= self.cap+self.direct_curvature_tolerance),
            "original_regular_normal_area": bool(float(np.min(area)) > self.area_floor)}
        return {
            "grid": label, "radial_count": len(rids), "theta_count": len(self.thetas[label]),
            "maximum_eta": maximum_eta,
            "eta_attainer": {"radial_index": int(rids[e_at[0]]), "theta_index": int(e_at[1]),
                             "s": float(self.radial[rids[e_at[0]]]), "theta": float(self.thetas[label][e_at[1]])},
            "maximum_absolute_principal_curvature": maximum_k,
            "curvature_attainer": {"radial_index": int(rids[k_at[0]]), "theta_index": int(k_at[1]),
                                   "principal_index": int(k_at[2]), "s": float(self.radial[rids[k_at[0]]]),
                                   "theta": float(self.thetas[label][k_at[1]]),
                                   "principal_curvatures": principal[k_at[0], k_at[1]].tolist()},
            "scaled_PSD_minima": {name: float(value) for name, value in zip(ROW_NAMES[2:], minima)},
            "minimum_normal_area": float(area[amin]),
            "normal_area_attainer": {"radial_index": int(rids[amin[0]]), "theta_index": int(amin[1])},
            "metric_budget": self.metric_budget, "original_curvature_cap": self.cap,
            "gates": gates, "all_metric_curvature_area_gates_pass": bool(all(gates.values())),
            "finite_grid_predictor_not_continuous_or_actual_fourteen_gate_certificate": True}

    def _value(self, z, reason, sink, *, prepared_frames=None):
        self.assert_context()
        _require(self.full_point_counts["started"] < MAX_EVALUATIONS, "new full-point cap exceeded")
        self.full_point_counts["started"] += 1
        ordinal = self.full_point_counts["started"]
        q = self.point_from_increment(z)
        partial = {"schema": POLICY+"-full-value-partial", "ordinal": ordinal, "reason": reason,
                   "state168": q, "increment102": np.asarray(z).copy(), "completed_grids": {}, "working_grid": None}
        sink["_last_full_value_partial"] = partial
        trace = _Trace(self.wall, sink)
        tick = time.monotonic()
        record = {"ordinal": ordinal, "reason": reason, "status": "started", "raw_increment102": _vector(z),
                  "actual_binary64_state168": _vector(q), "model_binding_sha256": self.binding_sha256}
        self.full_evaluation_records.append(record)
        try:
            grids = {}
            for label in LABELS:
                _wall(self.wall, "prefix102.full-value."+label)
                work = {"grid": label, "state168_sha256": array_binding(q)["sha256"], "status": "started"}
                partial["working_grid"] = work
                if prepared_frames is not None:
                    body_grid, fields, frame = prepared_frames[label]
                    work["frame_source"] = "same new preparation, no repeated scalar_frame call"
                else:
                    def retain_frame(value):
                        work["scalar_fields"] = {name: {key: value[1][name][key] for key in SCALAR_KEYS} for name in ("u", "v")}
                        work["current_frame_arrays"] = {key: value[2][key] for key in ("T", "Ts", "Tss", "Ttheta")}
                    body_grid, fields, frame = trace.run(
                        "current_scalar_frame", lambda label=label: self.field.scalar_frame(q, self.radial, self.thetas[label]),
                        retain_frame, grid=label, evaluation_ordinal=ordinal)
                work.setdefault("scalar_fields", {name: {key: fields[name][key] for key in SCALAR_KEYS} for name in ("u", "v")})
                work.setdefault("current_frame_arrays", {key: frame[key] for key in ("T", "Ts", "Tss", "Ttheta")})
                primitives = {}
                work["primitive_arrays"] = primitives
                for key in ("T", "Ts", "Tss"):
                    trace.run("complete_theta_primitive", lambda key=key: periodic_operator(frame[key], -1),
                              lambda value, key=key: primitives.__setitem__(key, value),
                              grid=label, source_array=key, evaluation_ordinal=ordinal)
                a = self.metric["a"][:, None, None]
                ap = self.metric["a_s"][:, None, None]
                app = self.metric["a_ss"][:, None, None]
                def assemble():
                    U = ap*primitives["T"]+a*primitives["Ts"]
                    U[..., 2] += self.height["b"][:, None]
                    B = app*primitives["T"]+2*ap*primitives["Ts"]+a*primitives["Tss"]
                    B[..., 2] += self.height["b_s"][:, None]
                    return {"Xs": U, "Xt": a*frame["T"], "Xss": B,
                            "Xst": ap*frame["T"]+a*frame["Ts"], "Xtt": a*frame["Ttheta"]}
                jets = trace.run("position_two_jets_without_X", assemble,
                                 lambda value: work.__setitem__("position_jets", value),
                                 grid=label, evaluation_ordinal=ordinal)
                T = np.asarray(frame["T"])
                U = jets["Xs"]
                e, f = np.sum(U*U, axis=-1)-1., np.sum(U*T, axis=-1)
                eta = (abs(e)+np.hypot(e, 2*f))/2
                metric_rows = np.moveaxis(spectral_proposal_rows(e, f, self.metric_budget, self.epsilon), 0, -1)
                curvature = trace.run("original_curvature_values", lambda: curvature_values(
                    jets, self.metric["a"][:, None], 1/self.cap, area_floor=self.area_floor),
                    lambda value: work.__setitem__("curvature_values", value), grid=label, evaluation_ordinal=ordinal)
                principal = trace.run("original_principal_curvatures", lambda: independent_principal_curvatures(curvature),
                                      lambda value: work.__setitem__("principal_curvatures", value),
                                      grid=label, evaluation_ordinal=ordinal)
                scaled = curvature["rows"]*self.curvature_factors
                all_six = np.concatenate((metric_rows, scaled), axis=-1)
                _require(np.all(np.isfinite(all_six)) and np.all(np.isfinite(eta)) and np.all(np.isfinite(principal)),
                         "finite full nonlinear grid rows required")
                grid = {"fields": fields, "frame": frame, "jets": jets, "T": T, "e": e, "f": f, "eta": eta,
                        "curvature": curvature, "principal": principal, "curvature_rows_scaled": scaled,
                        "all_six_rows": all_six}
                grids[label] = grid
                work.update(status="complete", metric_e=e, metric_f=f, metric_eta=eta,
                            all_six_rows=all_six, curvature_rows_scaled=scaled)
                partial["completed_grids"][label] = work
                partial["working_grid"] = None
            finite_values = []
            for label in LABELS:
                row = self.selected[label]
                finite_values.append(grids[label]["all_six_rows"][row["ri"], row["ti"], row["slot"]])
            values = np.concatenate(finite_values)
            _require(np.all(np.isfinite(values)), "finite selected body constraints required")
            summaries = {label: self._grid_summary(label, grids[label]) for label in LABELS}
            all_pass = all(item["all_metric_curvature_area_gates_pass"] for item in summaries.values())
            jac_inputs = {}
            for label in LABELS:
                selection = self.selected[label]
                points = np.unique(selection["point"])
                nr, nt = len(self.radial), len(self.thetas[label])
                ri, ti = points//nt, points % nt
                grid = grids[label]
                jac_inputs[label] = {"point_ids": points,
                    "position_jets": {key: value[ri, ti] for key, value in grid["jets"].items()},
                    "T": grid["T"][ri, ti], "e": grid["e"][ri, ti], "f": grid["f"][ri, ti],
                    "curvature": _selected_curvature(grid["curvature"], ri, ti, (nr, nt))}
            entry = {"ordinal": ordinal, "z": np.asarray(z).copy(), "state168": q, "grids": grids,
                     "values": values, "jacobian": None, "summaries": summaries,
                     "jac_inputs": jac_inputs, "all_grid_pass": bool(all_pass), "partial": partial}
            self.last_entry = entry
            partial.update(status="complete", selected_values=values, full_grid_summaries=summaries)
            self.full_point_counts["completed"] += 1
            record.update(status="complete", full_grid_summaries=copy.deepcopy(summaries),
                          all_grid_pass=bool(all_pass), selected_values=array_binding(values))
            return entry
        except Exception as error:
            self.full_point_counts["failed"] += 1
            record.update(status="raised", error=_error(error))
            partial.update(status="raised", error=_error(error))
            raise
        finally:
            record["elapsed_seconds"] = time.monotonic()-tick
            partial["elapsed_seconds"] = record["elapsed_seconds"]
            sink["full_point_counts"] = copy.deepcopy(self.full_point_counts)

    def _jacobian(self, entry, sink):
        if entry["jacobian"] is not None:
            return entry["jacobian"]
        self.assert_context()
        self.jacobian_counts["started"] += 1
        ordinal = self.jacobian_counts["started"]
        trace = _Trace(self.wall, sink)
        tick = time.monotonic()
        partial = {"status": "started", "ordinal": ordinal, "value_ordinal": entry["ordinal"],
                   "completed_blocks": [], "completed_column_blocks": []}
        sink["_last_jacobian_partial"] = partial
        J = np.empty((self.constraint_count, 102), dtype=np.float64)
        row_done = np.zeros(self.constraint_count, dtype=bool)
        partial["matrix"] = J
        partial["completed_rows_mask"] = row_done
        try:
            offset = 0
            for label in LABELS:
                selected = self.selected[label]
                grid = None if entry.get("grids") is None else entry["grids"][label]
                retained = entry["jac_inputs"][label]
                nr, nt = len(self.radial), len(self.thetas[label])
                radial_ids = np.unique(selected["ri"])
                for begin in range(0, len(radial_ids), OWNED_WIDTH):
                    _wall(self.wall, "prefix102.J."+label+".block")
                    owned = radial_ids[begin:begin+OWNED_WIDTH]
                    rows = np.flatnonzero(np.isin(selected["ri"], owned))
                    points, inverse = np.unique(selected["point"][rows], return_inverse=True)
                    gri, ti = points//nt, points % nt
                    ri = np.searchsorted(owned, gri)
                    if grid is not None:
                        fields = _slice_radial(grid["fields"], owned, nr)
                        frame = _slice_radial(grid["frame"], owned, nr)
                    else:
                        query = np.unique(np.r_[0, owned, nr-1])
                        local_owned = np.searchsorted(query, owned)
                        def restore_scalar_context():
                            body_grid = self.field.source.grid_for(self.radial[query], self.thetas[label])
                            full = body_grid.fields(entry["state168"])
                            full["_theta"] = self.thetas[label][None, :]
                            values = _slice_radial(full, local_owned, len(query))
                            return values, _derivative_frame_parts(values)
                        fields, frame = trace.run("new_J_scalar_context_only", restore_scalar_context,
                            None, grid=label, owned_radial_ids=owned.tolist(), value_ordinal=entry["ordinal"],
                            ordinary_U_T_and_full_values_recomputed=False)
                    metric = {key: value[owned] for key, value in self.metric.items()}
                    ip = np.searchsorted(retained["point_ids"], points)
                    small = {key: retained["position_jets"][key][ip] for key in POSITION_KEYS}
                    small["T"] = retained["T"][ip]
                    cvalues = {key: (value[ip] if isinstance(value, np.ndarray)
                                    and value.shape[:1] == (len(retained["point_ids"]),) else value)
                               for key, value in retained["curvature"].items()}
                    de0, f0 = retained["e"][ip], retained["f"][ip]
                    block_meta = {"grid": label, "owned_radial_ids": owned.tolist(),
                                  "selected_rows": len(rows), "unique_points": len(points), "value_ordinal": entry["ordinal"]}
                    for name, start, stop in (("u", 0, 54), ("v", 54, 102)):
                        family = self.families[label][name]
                        kernels = trace.run("new_angular_J_kernels", lambda name=name, family=family: angular_kernels(
                            fields, frame, name, family["angular"], family["angular_first"], second=True),
                            lambda value: partial.__setitem__("current_kernel_arrays", value), family=name, **block_meta)
                        virtual = virtual_selected_jets(kernels, ri, ti, metric, second=True)
                        data = dict(small)
                        data.update({"jac_"+key: value for key, value in virtual.items()})
                        U, T = small["Xs"], small["T"]
                        de = 2*np.einsum("ic,icn->in", U, virtual["Xs"])
                        df = np.einsum("ic,icn->in", T, virtual["Xs"])+np.einsum("ic,icn->in", U, virtual["T"])
                        m0 = spectral_parameter_rows(de0, f0, de, df, np.zeros(len(points), dtype=int), self.epsilon)
                        m1 = spectral_parameter_rows(de0, f0, de, df, np.ones(len(points), dtype=int), self.epsilon)
                        cj = curvature_parameter_jacobian(data, self.metric["a"][gri], 1/self.cap,
                                                          area_floor=self.area_floor, values=cvalues)
                        cj = cj*self.curvature_factors[None, :, None]
                        six = np.concatenate((m0[:, None, :], m1[:, None, :], cj), axis=1)
                        local = six[inverse, selected["slot"][rows]]
                        expanded = expand_radial_rows(local, family["radial"], selected["ri"][rows])
                        _require(expanded.shape == (len(rows), stop-start) and np.all(np.isfinite(expanded)),
                                 "finite exact prefix-column analytic block required")
                        J[offset+rows, start:stop] = expanded
                        partial["completed_column_blocks"].append({
                            "rows": (offset+rows).copy(), "column_start": start, "column_stop": stop,
                            "grid": label, "family": name, "value_ordinal": entry["ordinal"]})
                        partial.pop("current_kernel_arrays", None)
                        block_meta[name+"_maximum_temporary_virtual_bytes"] = sum(value.nbytes for value in virtual.values())
                        del kernels, virtual, data, six, local, expanded, cj, de, df, m0, m1
                    row_done[offset+rows] = True
                    partial["completed_blocks"].append(block_meta)
                offset += len(selected["ids"])
            _require(np.all(row_done) and np.all(np.isfinite(J)), "complete finite selected102 Jacobian required")
            J.setflags(write=False)
            entry["jacobian"] = J
            partial.update(status="complete", matrix_binding=array_binding(J))
            self.jacobian_counts["completed"] += 1
            return J
        except Exception as error:
            partial.update(status="raised", error=_error(error))
            self.jacobian_counts["failed"] += 1
            raise
        finally:
            partial["elapsed_seconds"] = time.monotonic()-tick
            sink["jacobian_counts"] = copy.deepcopy(self.jacobian_counts)

    def summary(self):
        return {"schema": POLICY+"-model-summary", "status": self.status,
                "binding_sha256": self.binding_sha256, "variables": VARIABLES,
                "mutable_physical_coefficients": 102, "owned_radial_J_width": OWNED_WIDTH,
                "constraint_count": getattr(self, "constraint_count", None),
                "finite_row_receipts": copy.deepcopy(getattr(self, "row_receipts", None)),
                "suffix_receipt": copy.deepcopy(getattr(self, "suffix_receipt", None)),
                "initial_full_grid_summaries": None if self.initial_entry is None else copy.deepcopy(self.initial_entry["summaries"]),
                "full_point_counts": copy.deepcopy(self.full_point_counts), "jacobian_counts": copy.deepcopy(self.jacobian_counts),
                "only_selected_metric_curvature_rows_enter_the_solver": True,
                "every_candidate_requires_full_grid_values_and_external_actual_fourteen_gates": True}

    def full_record(self):
        result = {"schema": POLICY+"-full-model", "definition": definition(), "summary": self.summary(),
                  "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
                  "build_receipt": _public(self.build_sink),
                  "accepted_state168": _vector(self.accepted_state168),
                  "unaccepted_ring_seed168": _vector(self.ring_candidate168),
                  "lower172_exact": [str(v) for v in self.lower172], "upper172_exact": [str(v) for v in self.upper172],
                  "backend_remaining_box102_exact": [[str(a), str(b)] for a, b in zip(self.remaining_lower_exact, self.remaining_upper_exact)],
                  "backend_remaining_box102_binary64_inward": [list(row) for row in self.backend_bounds102],
                  "new_paid_input": _numeric(self.model_input_arrays),
                  "fixed_finite_selected_original_row_ids": {label: _payload(self.selected[label]["ids"]) for label in LABELS},
                  "fixed_suffix_full_arrays": _numeric(getattr(self, "suffix_arrays", {})),
                  "initial_selected_original_values": None if self.initial_entry is None else _payload(self.initial_entry["values"]),
                  "all_initial_global_frame_primitive_and_curvature_arrays_not_duplicated": True,
                  "unsaved_derived_arrays_are_not_future_free_recoverable_inputs": True}
        return result


def _selected_rows(pool, nr, nt, label):
    raw = np.asarray(pool)
    _require(raw.ndim == 1 and raw.dtype.kind in "iu" and len(raw) > 0
             and np.all(raw >= 0) and np.all(raw < 11*nr*nt), "literal original "+label+" pool IDs required")
    ids = []
    seen = set()
    retained, discarded = 0, 0
    for value in raw:
        row = int(value)
        if row//(nr*nt) not in ORIGINAL_GROUPS:
            discarded += 1
            continue
        if row not in seen:
            seen.add(row); ids.append(row); retained += 1
    added = 0
    for radial_index in BAD_RADIAL_INDICES:
        for group in ORIGINAL_GROUPS:
            for theta_index in range(nt):
                row = group*nr*nt+radial_index*nt+theta_index
                if row not in seen:
                    seen.add(row); ids.append(row); added += 1
    ids = np.asarray(ids, dtype=np.int64)
    group, point = ids//(nr*nt), ids % (nr*nt)
    slot = np.where(group < 2, group, group-5)
    receipt = {"grid": label, "original_pool": array_binding(raw), "original_count": len(raw),
               "retained_distinct_original_metric_curvature_rows": retained,
               "other_original_group_rows_not_solver_constraints": discarded,
               "other_original_groups_not_claimed_invariant": True,
               "mandatory_complete_circle_radial_ids": list(BAD_RADIAL_INDICES),
               "genuinely_added_circle_rows": added, "fixed_total_rows": len(ids),
               "selected_row_binding": array_binding(ids), "first_occurrence_original_pool_order_preserved": True}
    return {"ids": ids, "group": group, "point": point, "ri": point//nt, "ti": point % nt, "slot": slot}, receipt


def build_fixed_ring_prefix102_model(
        field, accepted_state168, ring_candidate168, radial, thetas, fixed_metric,
        cfg, lower172, upper172, source_receipt, wall, capture=None, *,
        metric_budget, original_pools, charge_prepare, charge_suffix):
    """Build once from authenticated accepted58 and the actual free36 vector.

    fixed_metric is the COMPLETE bind_current_168_curvature_metric record.
    original_pools contains the literal current coarse/fine integer arrays.
    charge callbacks debit the external task and may return any receipt dict;
    local events retain true elapsed/complete/error and grant no new quota.
    No paid ring/ray model or old derivative is recomputed or read here.
    """
    started = time.monotonic()
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty new model capture required")
    sink.update(schema=POLICY+"-build-capture", status="entered", source_receipt=copy.deepcopy(source_receipt))
    model = FixedRingPrefix102Model()
    sink["_object_model"] = model
    model.build_sink = sink
    model.field, model.wall = field, wall
    try:
        _wall(wall, "prefix102.build.entry")
        _context(field)
        _require(isinstance(field, CompleteBody168Field) and field.metric_free == 0,
                 "the original fixed-g complete168 field required")
        _require(isinstance(cfg, dict) and isinstance(source_receipt, dict) and source_receipt,
                 "original cfg and independently authenticated paid source receipt required")
        _require(callable(charge_prepare) and callable(charge_suffix), "both new external accounting callbacks required")
        model.accepted_state168 = _finite(field.validate_state(accepted_state168), (168,), "accepted58")
        model.ring_candidate168 = _finite(field.validate_state(ring_candidate168), (168,), "unaccepted paid ring vector")
        outside_paid = [i for i in range(168) if i not in PAID_RING_COLUMNS]
        _require(_same(model.accepted_state168[outside_paid], model.ring_candidate168[outside_paid]),
                 "paid free36 vector changed coordinates outside its literal original last51")
        model.lower172, model.upper172 = _bounds(lower172, "lower"), _bounds(upper172, "upper")
        _require(all(a <= b for a, b in zip(model.lower172, model.upper172)), "ordered original172 box required")
        model.accepted_physical = tuple(field.full_coefficients(model.accepted_state168, exact=True))
        model.seed_physical = tuple(field.full_coefficients(model.ring_candidate168, exact=True))
        _require(all(a <= v <= b for a, v, b in zip(model.lower172, model.seed_physical, model.upper172))
                 and all(a <= v <= b for a, v, b in zip(model.lower172, model.accepted_physical, model.upper172)),
                 "both the real accepted source and the unaccepted seed need the original exact172 box")
        rr = np.asarray(radial, dtype=np.float64)
        _require(rr.ndim == 1 and len(rr) > 141 and rr[0] == 0 and np.all(np.diff(rr) > 0),
                 "the original increasing zero-anchored radial vector required")
        model.radial = _finite(rr, rr.shape, "radial")
        _require(all(abs(float(rr[i])-value) <= 8*np.spacing(value) for i, value in zip(BAD_RADIAL_INDICES, BAD_RADIAL_LABELS)),
                 "mandatory new bad-circle indices are not the original source grid")
        _require(isinstance(thetas, dict) and set(thetas) == set(LABELS)
                 and isinstance(original_pools, dict) and set(original_pools) == set(LABELS),
                 "both original grids and pools required")
        model.thetas = {}
        for label in LABELS:
            th = np.asarray(thetas[label], dtype=np.float64)
            _require(th.ndim == 1 and len(th) > 0 and np.all(np.isfinite(th)), "finite original full theta grid required")
            model.thetas[label] = _finite(th, th.shape, label+" theta")
        _require(len(model.thetas["fine"]) == 2*len(model.thetas["coarse"]), "original two-grid circle widths required")
        model.cfg = copy.deepcopy(cfg)
        model.metric = _validate_metric(field, model.radial, fixed_metric)
        model.metric_budget = float(metric_budget)
        _require(not isinstance(metric_budget, bool) and math.isfinite(model.metric_budget) and model.metric_budget > 0,
                 "literal strict-decrease metric budget required")
        model.epsilon = float(Q(cfg["metric_proposal_epsilon_exact"]))
        model.cap = float(Q(cfg["fixed_hard_curvature_cap_exact"]))
        model.area_floor = float(cfg["normal_area_numerical_floor"])
        model.curvature_row_tolerance = float(cfg["curvature_row_tolerance"])
        model.direct_curvature_tolerance = float(cfg["direct_curvature_tolerance"])
        scale = float(Q(cfg["curvature_scale_exact"]))
        _require(all(math.isfinite(v) and v > 0 for v in (model.epsilon, model.cap, scale))
                 and all(math.isfinite(v) and v >= 0 for v in (model.area_floor, model.curvature_row_tolerance, model.direct_curvature_tolerance)),
                 "original finite positive targets and nonnegative tolerances required")
        model.curvature_factors = np.asarray((model.cap/scale, (model.cap/scale)**2,
                                              model.cap/scale, (model.cap/scale)**2))
        model.remaining_lower_exact = tuple(model.lower172[i]-model.seed_physical[i] for i in PREFIX_COLUMNS)
        model.remaining_upper_exact = tuple(model.upper172[i]-model.seed_physical[i] for i in PREFIX_COLUMNS)
        model.backend_bounds102 = tuple((_inward_float(a, True), _inward_float(b, False))
                                      for a, b in zip(model.remaining_lower_exact, model.remaining_upper_exact))
        _require(all(a <= 0 <= b for a, b in model.backend_bounds102), "the paid ring seed must belong to the remaining box")
        model.selected, model.row_receipts = {}, {}
        for label in LABELS:
            model.selected[label], model.row_receipts[label] = _selected_rows(
                original_pools[label], len(rr), len(model.thetas[label]), label)
        model.constraint_count = sum(len(value["ids"]) for value in model.selected.values())
        model.suffix_indices = np.asarray([i for i, value in enumerate(rr) if Q.from_float(float(value)) >= Q(SUFFIX_LEFT_EXACT)], dtype=np.int64)
        _require(len(model.suffix_indices) > 0 and 141 in model.suffix_indices, "original fixed suffix and protected ring required")
        model.binding = {
            "schema": POLICY+"-binding", "definition": definition(),
            "field_definition_sha256": field.definition_sha256,
            "coordinate_definition_sha256": field.coordinate_definition_sha256,
            "configuration_sha256": digest(model.cfg),
            "accepted_state168": array_binding(model.accepted_state168),
            "accepted_physical_identity_sha256": digest(field.identity(model.accepted_state168)),
            "unaccepted_ring_candidate168": array_binding(model.ring_candidate168),
            "unaccepted_ring_physical_identity_sha256": digest(field.identity(model.ring_candidate168)),
            "original_lower172_exact": [str(v) for v in model.lower172],
            "original_upper172_exact": [str(v) for v in model.upper172],
            "radial": array_binding(model.radial), "theta": {k: array_binding(v) for k, v in model.thetas.items()},
            "fixed_metric_binding_sha256": fixed_metric["binding_sha256"],
            "metric_budget_binary64": model.metric_budget, "metric_budget_exact_binary64": str(Q.from_float(model.metric_budget)),
            "finite_original_rows": copy.deepcopy(model.row_receipts),
            "source_receipt": copy.deepcopy(source_receipt), "source_hashes": implementation_hashes()}
        model.binding_sha256 = digest(model.binding)
        sink.update(model_binding_sha256=model.binding_sha256, binding=copy.deepcopy(model.binding))
        _wall(wall, "prefix102.before-new-prepare")
        sink["prepare_charge_receipt"] = copy.deepcopy(charge_prepare({
            "schema": POLICY+"-prepare-charge", "model_binding_sha256": model.binding_sha256,
            "new_height_derivative_input": 1, "new_two_grid_scalar_frames": 2,
            "new_full_circle_primitive_calls": 6, "ordinary_or_center_calls": 0}))
        trace = _Trace(wall, sink)
        model.model_input_arrays = {"radial": model.radial, "theta": model.thetas,
                                    "fixed_metric": model.metric, "fixed_height_derivatives": {},
                                    "source_scalar_fields": {}, "original_families": {}}
        def retain_height(value):
            model.model_input_arrays["fixed_height_derivatives"] = {key: value[key] for key in ("b", "b_s")}
        height = trace.run("fixed_height_derivative_input", lambda: field.height_jets(model.ring_candidate168, model.radial), retain_height)
        model.height = {key: _finite(height[key], (len(rr),), key) for key in ("b", "b_s")}
        prepared_frames, model.families = {}, {}
        for label in LABELS:
            def retain_prepared(value, label=label):
                model.model_input_arrays["source_scalar_fields"][label] = {
                    name: {key: value[1][name][key] for key in SCALAR_KEYS} for name in ("u", "v")}
            triple = trace.run("current_scalar_frame", lambda label=label: field.scalar_frame(
                model.ring_candidate168, model.radial, model.thetas[label]), retain_prepared, grid=label, evaluation_ordinal=1)
            prepared_frames[label] = triple
            families = _families(triple[0], len(rr), len(model.thetas[label]), verify_shared_modes=False)
            model.families[label] = {
                family["name"]: {"angular": family["angular"], "angular_first": family["angular_first"],
                                 "radial": tuple(value[:, :6] for value in family["radial"])}
                for family in families[:2]}
            model.model_input_arrays["original_families"][label] = model.families[label]
        initial = model._value(np.zeros(102), "new_full_body_preparation", sink, prepared_frames=prepared_frames)
        model.initial_entry = initial
        _wall(wall, "prefix102.before-suffix-assessment")
        sink["suffix_charge_receipt"] = copy.deepcopy(charge_suffix({
            "schema": POLICY+"-fixed-suffix-charge", "model_binding_sha256": model.binding_sha256,
            "source_full_value_ordinal": initial["ordinal"], "radial_ids": model.suffix_indices.tolist(),
            "same_new_arrays_only_no_geometry_or_J_repeated": True}))
        model.suffix_receipt = {label: model._grid_summary(label, initial["grids"][label], radial_indices=model.suffix_indices) for label in LABELS}
        model.suffix_arrays = {}
        for label in LABELS:
            grid = initial["grids"][label]
            ids = model.suffix_indices
            model.suffix_arrays[label] = {
                "radial_ids": ids, "theta": model.thetas[label],
                "position_two_jets_without_X": {key: value[ids] for key, value in grid["jets"].items()},
                "T": grid["T"][ids], "metric_e": grid["e"][ids], "metric_f": grid["f"][ids],
                "metric_eta": grid["eta"][ids], "scaled_PSD_rows": grid["curvature_rows_scaled"][ids],
                "normal_area": grid["curvature"]["q"][ids], "principal_curvatures": grid["principal"][ids]}
        suffix_pass = all(item["all_metric_curvature_area_gates_pass"] for item in model.suffix_receipt.values())
        model.status = "ready" if suffix_pass else "fixed-suffix-excludes-this-numerical-fiber"
        sink.update(status=model.status, fixed_suffix=copy.deepcopy(model.suffix_receipt), suffix_pass=bool(suffix_pass),
                    suffix_failure_does_not_claim_a_directed_continuous_infeasibility_certificate=True,
                    new_solver_calls=0, new_selected_J_calls=0)
        _wall(wall, "prefix102.build.complete")
        return model
    except Exception as error:
        sink.update(status="raised", error=_error(error))
        model.status = "build-raised"
        raise
    finally:
        sink["local_elapsed_seconds"] = time.monotonic()-started
        sink["full_point_counts"] = copy.deepcopy(model.full_point_counts)


class _EvaluationCache:
    def __init__(self, model, wall, started, seconds, maximum, sink):
        self.model, self.wall, self.started = model, wall, started
        self.seconds, self.maximum, self.sink = seconds, maximum, sink
        initial = model.initial_entry
        self.entries = {initial["state168"].tobytes(): initial}
        self.callbacks = {"objective": 0, "objective_J": 0, "constraint_value": 0,
                          "constraint_J": 0, "iteration": 0, "paid_value_cache_hits": 0,
                          "paid_J_cache_hits": 0}
        sink["iteration_records"] = []
        sink["full_evaluation_records"] = model.full_evaluation_records

    def check(self, stage):
        _wall(self.wall, "prefix102.solver."+stage)
        elapsed = time.monotonic()-self.started
        if elapsed > self.seconds:
            raise FixedRingPrefix102Limit("new solver scientific clock exceeded after "+stage)

    def _input(self, x):
        x = np.asarray(x, dtype=np.float64)
        _require(x.shape == (103,) and np.all(np.isfinite(x)), "finite backend103 required")
        return x

    def _release_last_global_arrays(self):
        entry = self.model.last_entry
        if entry is None or entry.get("grids") is None:
            return
        entry["grids"] = None
        partial = entry.get("partial")
        if isinstance(partial, dict):
            partial.clear()
            partial.update(status="complete-full-arrays-released",
                           ordinal=entry["ordinal"], actual_state168=array_binding(entry["state168"]),
                           full_grid_summaries=copy.deepcopy(entry["summaries"]),
                           selected_value_and_derivative_inputs_retained=True,
                           full_grid_values_not_saved_for_free_future_reuse=True)
        entry["partial"] = None

    def get(self, z, reason, *, need_J=False):
        self.check(reason+".before")
        z = _finite(z, (102,), "literal prefix increment")
        candidate = self.model.point_from_increment(z)
        key = candidate.tobytes()
        entry = self.entries.get(key)
        if entry is None:
            if self.model.full_point_counts["started"] >= self.maximum:
                raise FixedRingPrefix102Limit("new point value limit reached; no old value replay")
            self._release_last_global_arrays()
            entry = self.model._value(z, reason, self.sink)
            self.entries[key] = entry
        else:
            self.callbacks["paid_value_cache_hits"] += 1
        _require(_same(entry["state168"], candidate), "cache candidate identity changed")
        if need_J:
            if entry["jacobian"] is None:
                self.model._jacobian(entry, self.sink)
            else:
                self.callbacks["paid_J_cache_hits"] += 1
        self.sink["_last_complete_selected_evaluation"] = {
            "value_ordinal": entry["ordinal"], "requested_increment102": z,
            "actual_state168": entry["state168"], "values": entry["values"],
            "analytic_J102": entry["jacobian"],
            "full_grid_summaries": entry["summaries"],
            "full_grid_arrays_still_available": bool(entry.get("grids") is not None)}
        self.check(reason+".after")
        return entry

    def objective(self, x):
        self.callbacks["objective"] += 1
        self.check("objective")
        return float(self._input(x)[102])

    def objective_J(self, x):
        self.callbacks["objective_J"] += 1
        self.check("objective-J")
        self._input(x)
        out = np.zeros(103)
        out[102] = 1.
        return out

    def constraints(self, x):
        self.callbacks["constraint_value"] += 1
        x = self._input(x)
        entry = self.get(x[:102], "constraint-value")
        return entry["values"]/self.model.row_scales+x[102]

    def constraints_J(self, x):
        self.callbacks["constraint_J"] += 1
        x = self._input(x)
        entry = self.get(x[:102], "constraint-J", need_J=True)
        return np.column_stack((entry["jacobian"]/self.model.row_scales[:, None],
                                np.ones(len(entry["values"]))))

    def iteration(self, x):
        self.callbacks["iteration"] += 1
        self.check("iteration")
        x = self._input(x)
        q = self.model.point_from_increment(x[:102])
        entry = self.entries.get(q.tobytes())
        record = {"iteration_callback_ordinal": self.callbacks["iteration"],
                  "raw_backend103": _vector(x), "elapsed_solver_seconds": time.monotonic()-self.started,
                  "actual_binary64_state168": _vector(q),
                  "paid_value_ordinal": None if entry is None else entry["ordinal"],
                  "callback_does_not_trigger_a_new_value_or_J": True}
        if entry is not None:
            record.update(phase_I_slack=float(x[102]),
                          maximum_scaled_phase_I_constraint_violation=float(max(0., -np.min(entry["values"]/self.model.row_scales+x[102]))),
                          full_grid_summaries=copy.deepcopy(entry["summaries"]))
        self.sink["iteration_records"].append(record)


def _solver_public(sink):
    result = _public(sink)
    for key in ("full_evaluation_records", "iteration_records"):
        if key in result:
            records = result.pop(key)
            result[key+"_count"] = len(records)
    result["all_actual_evaluation_and_iteration_records_are_in_capture_for_SOLVE_TRACE"] = True
    if result.get("original_result_stdout_receipt") is not None:
        raw = result.pop("original_backend_return", None)
        result["original_backend_return_was_emitted"] = True
        result["original_backend_return_summary"] = None if raw is None else {
            key: copy.deepcopy(raw.get(key)) for key in (
                "schema", "status", "success", "message", "nit", "nfev", "njev",
                "actual_finite_raw103_saved", "backend_elapsed_seconds", "raw_phase_I_slack")}
    return result


def solve_fixed_ring_prefix102_once(
        model, *, wall, charge_solve, emit=None, capture=None,
        solver_time_limit_seconds=180, maxiter=120, max_evaluations=240):
    """One new phase-I backend call; no suffix failure is sent to a solver.

    max_evaluations counts genuinely new complete TWO-GRID value points,
    including the initial point already prepared by build.  The original
    selected analytic Jacobian is paid only when actually requested and is
    cached separately.  No dense full-grid-by102 parameter tensor is formed.
    """
    _require(isinstance(model, FixedRingPrefix102Model) and not model.solve_attempted,
             "one fresh fixed-ring prefix model is required")
    _require(callable(wall) and callable(charge_solve) and (emit is None or callable(emit)),
             "external wall, one solve debit and optional emitter required")
    _require(type(maxiter) is int and 0 < maxiter <= SLSQP_OPTIONS["maxiter"]
             and type(max_evaluations) is int and 0 < max_evaluations <= MAX_EVALUATIONS,
             "new point/iteration caps may not be enlarged")
    seconds = float(solver_time_limit_seconds)
    _require(not isinstance(solver_time_limit_seconds, bool) and math.isfinite(seconds)
             and 0 < seconds <= SOLVER_SECONDS, "finite solver clock at most180 required")
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty per-solve capture required")
    sink.update(schema=POLICY+"-solver-capture", status="entered", model_binding_sha256=model.binding_sha256,
                charged=False, backend_entered=False, qualified_candidate=False,
                original_backend_return=None, original_result_stdout_receipt=None,
                maximum_new_two_grid_value_points=max_evaluations,
                maximum_iterations=maxiter, solver_time_limit_seconds=seconds,
                options={"maxiter": maxiter, "ftol": SLSQP_OPTIONS["ftol"], "disp": False},
                no_restart_or_extra_rowset_solve=True)
    model.solve_attempted = True
    model.solver_sink = sink
    started = time.monotonic()
    cache, candidate, candidate_record = None, None, None
    try:
        model.assert_context()
        if model.status == "fixed-suffix-excludes-this-numerical-fiber":
            sink.update(status=model.status, new_solver_calls=0,
                        suffix_receipt=copy.deepcopy(model.suffix_receipt),
                        no_candidate_created=True)
        elif model.status != "ready":
            raise ValueError("the new prefix model was not fully prepared")
        elif all(a == b for a, b in model.backend_bounds102) and not model.initial_entry["all_grid_pass"]:
            sink.update(status="original-prefix-box-singleton-fails-full-grid", new_solver_calls=0,
                        no_candidate_created=True)
        elif model.initial_entry["all_grid_pass"]:
            candidate, candidate_record = model.point_from_increment(np.zeros(102), include_record=True)
            _require(candidate_record["original_exact_box_pass"], "initial seed exact box changed")
            sink.update(status="initial-fixed-ring-seed-passes-full-grid-needs-actual",
                        qualified_candidate=True, new_solver_calls=0,
                        returned_candidate_record=copy.deepcopy(candidate_record),
                        candidate_source="prepared original seed; no backend was called",
                        original_actual_fourteen_gates_not_claimed=True)
        else:
            _wall(wall, "prefix102.before-solver-charge")
            sink["charge_receipt"] = copy.deepcopy(charge_solve({
                "schema": POLICY+"-solver-charge", "model_binding_sha256": model.binding_sha256,
                "variables": VARIABLES, "finite_constraint_rows": model.constraint_count,
                "backend": "scipy.optimize.minimize(method='SLSQP')", "objective": "phase_I_slack",
                "options": copy.deepcopy(sink["options"]),
                "maximum_new_two_grid_value_points": max_evaluations,
                "Jacobian_only_when_requested_and_charged_in_local_counts": True,
                "solver_time_limit_seconds": seconds}))
            sink.update(charged=True, new_solver_calls=1)
            cache = _EvaluationCache(model, wall, started, seconds, max_evaluations, sink)
            cache.check("after-charge")
            import scipy
            from scipy.optimize import minimize
            sink["scipy_version"] = str(scipy.__version__)
            cache.check("after-import")
            initial = cache.get(np.zeros(102), "initial-J-at-prepared-point", need_J=True)
            scales = np.maximum(1., np.maximum(abs(initial["values"]), np.max(abs(initial["jacobian"]), axis=1)))
            _require(np.all(np.isfinite(scales)) and np.all(scales > 0), "finite strictly positive fixed row scales required")
            scales.setflags(write=False)
            model.row_scales = scales
            sink["_fixed_row_scales"] = scales
            sink["_initial_full_evaluation"] = {
                "value_ordinal": initial["ordinal"], "actual_state168": initial["state168"],
                "selected_original_values": initial["values"], "selected_analytic_J102": initial["jacobian"],
                "full_grid_summaries": initial["summaries"]}
            sink["fixed_row_scale_receipt"] = {
                "formula": definition()["fixed_scales"], "source_value_ordinal": initial["ordinal"],
                "row_scales": array_binding(scales), "same_values_in_SOLVE_TRACE": True,
                "never_updated_after_initial_evaluation": True}
            slack0 = float(max(0., -np.min(initial["values"]/scales)))
            if slack0 > 0:
                slack0 = float(np.nextafter(slack0, np.inf))
            x0 = np.r_[np.zeros(102), slack0]
            bounds = [*model.backend_bounds102, (0., None)]
            sink["initial_raw103"] = _vector(x0)
            sink["backend_bounds103"] = [list(row) for row in bounds]
            sink["initial_source_value_was_not_recomputed"] = True
            cache.check("before-backend")
            backend_started = time.monotonic()
            sink.update(status="backend-entered", backend_entered=True)
            result = minimize(cache.objective, x0, method="SLSQP", jac=cache.objective_J,
                              bounds=bounds,
                              constraints=[{"type": "ineq", "fun": cache.constraints, "jac": cache.constraints_J}],
                              callback=cache.iteration, options=copy.deepcopy(sink["options"]))
            backend_seconds = time.monotonic()-backend_started
            sink["_object_original_result"] = result
            raw_x = result.get("x")
            finite_vector = bool(raw_x is not None and np.asarray(raw_x).shape == (103,)
                                 and np.all(np.isfinite(np.asarray(raw_x, dtype=float))))
            raw = {
                "schema": POLICY+"-original-nonlinear-return", "model_binding_sha256": model.binding_sha256,
                "backend": "scipy.optimize.minimize(method='SLSQP')", "scipy_version": str(scipy.__version__),
                "options": copy.deepcopy(sink["options"]), "variable_order": "physical_prefix102,phase_I_slack",
                "actual_raw_backend103": None if raw_x is None else _raw_numeric(raw_x),
                "entire_OptimizeResult_fields": _raw_all_fields(dict(result)),
                "status": None if result.get("status") is None else int(result.get("status")),
                "success": bool(result.get("success", False)), "message": str(result.get("message", "")),
                "nit": None if result.get("nit") is None else int(result.get("nit")),
                "nfev": None if result.get("nfev") is None else int(result.get("nfev")),
                "njev": None if result.get("njev") is None else int(result.get("njev")),
                "raw_phase_I_slack": float(raw_x[102]) if finite_vector else None,
                "backend_elapsed_seconds": float(backend_seconds),
                "all_actual_result_fields_saved_before_any_filter": True,
                "QP_multipliers_are_not_a_strict_nonlinear_or_global_certificate": True}
            raw["actual_finite_raw103_saved"] = bool(finite_vector and raw["actual_raw_backend103"] is not None
                    and raw["actual_raw_backend103"].get("shape") == [103]
                    and len(raw["actual_raw_backend103"].get("exact_binary64_flat", [])) == 103)
            sink.update(status="backend-returned", original_backend_return=raw, backend_elapsed_seconds=float(backend_seconds))
            if emit is not None:
                emit_started = time.monotonic()
                try:
                    sink["original_result_stdout_receipt"] = copy.deepcopy(emit("NONLINEAR_RESULT", copy.deepcopy(raw)))
                except Exception as error:
                    sink["raw_result_reporting_error"] = _error(error)
                    raise
                finally:
                    sink["raw_result_emit_seconds"] = time.monotonic()-emit_started
            cache.check("after-raw-return-preservation")
            eligible = bool(raw["success"] and raw["status"] == 0 and finite_vector)
            sink["backend_status_eligible"] = eligible
            if finite_vector:
                vector = np.asarray(raw_x, dtype=np.float64)
                proposed, candidate_record = model.point_from_increment(vector[:102], include_record=True)
                sink["returned_candidate_record"] = copy.deepcopy(candidate_record)
                sink["_returned_candidate168"] = proposed
                entry = cache.entries.get(proposed.tobytes())
                sink["returned_point_paid_full_summary_available"] = bool(entry is not None)
                if entry is not None:
                    same_state = _same(proposed, entry["state168"])
                    violation = float(max(0., -np.min(entry["values"]/scales+vector[102])))
                    filt = {
                        "value_ordinal": entry["ordinal"], "same_actual_binary64_state168": bool(same_state),
                        "phase_I_slack": float(vector[102]), "phase_I_slack_tolerance": SLSQP_OPTIONS["ftol"],
                        "phase_I_slack_pass": bool(-SLSQP_OPTIONS["ftol"] <= vector[102] <= SLSQP_OPTIONS["ftol"]),
                        "maximum_scaled_phase_I_constraint_violation": violation,
                        "scaled_phase_I_constraint_pass": bool(violation <= SLSQP_OPTIONS["ftol"]),
                        "exact_original172_box_pass": bool(candidate_record["original_exact_box_pass"]),
                        "full_grid_summaries": copy.deepcopy(entry["summaries"]),
                        "all_full_grid_metric_curvature_area_pass": bool(entry["all_grid_pass"]),
                        "full_grid_arrays_still_available": bool(entry.get("grids") is not None),
                        "no_full_value_repeated_for_final_report_or_filter": True,
                        "original_actual_fourteen_gates_not_claimed": True}
                    sink["candidate_filter"] = filt
                    passed = eligible and same_state and all(filt[key] for key in (
                        "phase_I_slack_pass", "scaled_phase_I_constraint_pass", "exact_original172_box_pass",
                        "all_full_grid_metric_curvature_area_pass"))
                    if passed:
                        candidate = proposed
                        sink.update(status="full-grid-prefix-candidate-needs-original-actual",
                                    qualified_candidate=True, candidate_source_value_ordinal=entry["ordinal"])
                    else:
                        sink["status"] = "returned-point-not-qualified-by-full-grid-and-original-box"
                else:
                    sink["status"] = "returned-point-has-no-authenticated-paid-full-grid-summary"
            else:
                sink["status"] = "backend-returned-no-finite103"
            if not eligible:
                sink["status"] = "backend-return-is-not-status0-success"
            cache.check("complete")
        model.status = sink["status"]
    except FixedRingPrefix102Limit as error:
        sink.update(status="stopped-at-new-declared-limit", error=_error(error),
                    qualified_candidate=False, no_backend_status_relabelled=True)
        model.status = sink["status"]
        candidate = None
    except Exception as error:
        sink.update(status="raised", error=_error(error), qualified_candidate=False,
                    all_completed_and_partial_costs_retained=True)
        model.status = "solver-raised"
        candidate = None
        raise
    finally:
        sink["local_elapsed_seconds"] = time.monotonic()-started
        sink["observed_nonpreemptive_solver_clock_overrun_seconds"] = max(0., sink["local_elapsed_seconds"]-seconds)
        sink["new_value_counts"] = copy.deepcopy(model.full_point_counts)
        sink["new_selected_J_counts"] = copy.deepcopy(model.jacobian_counts)
        if cache is not None:
            sink["callback_counts"] = copy.deepcopy(cache.callbacks)
            sink["distinct_actual_binary64_states_cached"] = len(cache.entries)
            sink["retained_selected_J_bytes"] = sum(entry["jacobian"].nbytes for entry in cache.entries.values() if entry["jacobian"] is not None)
        record = sink.get("returned_candidate_record")
        sink["actual_returned_candidate168_saved"] = bool(isinstance(record, dict)
            and len(record.get("rounded_independent168", {}).get("values", [])) == 168
            and len(record.get("rounded_independent168", {}).get("exact_binary64", [])) == 168)
        sink["actual_returned_physical172_exact_saved"] = bool(isinstance(record, dict)
            and len(record.get("rounded_physical172_exact", [])) == 172)
        sink["final_candidate_only_from_return_or_already_complete_initial_value"] = True
    return {"status": sink["status"], "qualified_candidate": bool(sink["qualified_candidate"]),
            "qualified": bool(sink["qualified_candidate"]), "candidate168": candidate,
            "candidate": candidate, "candidate_record": copy.deepcopy(candidate_record),
            "report": _solver_public(sink)}


def fixed_ring_prefix102_capture_record(capture, *, include_arrays=False):
    """Only actual retained values; unfilled J memory is NEVER serialized."""
    _require(isinstance(capture, dict), "capture dictionary required")
    result = _public(capture)
    if result.get("original_result_stdout_receipt") is not None:
        raw = result.pop("original_backend_return", None)
        result["emitted_original_backend_return_summary"] = None if raw is None else {
            key: copy.deepcopy(raw.get(key)) for key in (
                "schema", "status", "success", "message", "nit", "nfev", "njev",
                "actual_finite_raw103_saved", "backend_elapsed_seconds", "raw_phase_I_slack")}
    if not include_arrays:
        return result
    model = capture.get("_object_model")
    if isinstance(model, FixedRingPrefix102Model):
        if hasattr(model, "model_input_arrays"):
            result["actually_prepared_new_input_arrays"] = _numeric(model.model_input_arrays)
        if hasattr(model, "suffix_arrays"):
            result["actually_completed_fixed_suffix_arrays"] = _numeric(model.suffix_arrays)
    for private, public in (("_fixed_row_scales", "actual_fixed_row_scales"),
                            ("_initial_full_evaluation", "actual_initial_selected_value_and_J"),
                            ("_returned_candidate168", "actual_returned_candidate168")):
        if private in capture:
            result[public] = _numeric(capture[private])
    initial = capture.get("_initial_full_evaluation")
    initial_J = initial.get("selected_analytic_J102") if isinstance(initial, dict) else None
    latest = capture.get("_last_complete_selected_evaluation")
    if isinstance(latest, dict):
        result["actual_last_selected_value_receipt"] = _numeric({key: value for key, value in latest.items() if key != "analytic_J102"})
        last_J = latest.get("analytic_J102")
        result["actual_last_selected_value_receipt"]["analytic_J102"] = None if last_J is None else {
            **array_binding(last_J),
            "same_array_as_initial_J": bool(last_J is initial_J),
            "values_are_only_saved_in_initial_or_last_computed_J_sections": True}
    partial = capture.get("_last_full_value_partial")
    if isinstance(partial, dict):
        if partial.get("status") == "complete":
            result["last_full_value_arrays"] = {
                "status": partial["status"], "ordinal": partial["ordinal"],
                "state168": _vector(partial["state168"]),
                "grids": {label: {
                    "position_two_jets_without_X": _numeric(grid["position_jets"]),
                    "T": _payload(grid["current_frame_arrays"]["T"]),
                    "metric_e": _payload(grid["metric_e"]), "metric_f": _payload(grid["metric_f"]),
                    "metric_eta": _payload(grid["metric_eta"]),
                    "scaled_PSD_rows": _payload(grid["curvature_rows_scaled"]),
                    "principal_curvatures": _payload(grid["principal_curvatures"]),
                    "normal_area": _payload(grid["curvature_values"]["q"])}
                    for label, grid in partial["completed_grids"].items()},
                "no_duplicate_full_frame_or_Pi_or_I_II_copy": True}
        else:
            result["actually_last_incomplete_or_released_full_value"] = _numeric(partial)
    partial_J = capture.get("_last_jacobian_partial")
    if isinstance(partial_J, dict):
        meta = {key: value for key, value in partial_J.items() if key not in ("matrix", "current_kernel_arrays")}
        if partial_J.get("status") == "complete":
            if partial_J["matrix"] is initial_J:
                meta["complete_analytic_J102"] = {**array_binding(initial_J),
                    "values_reference": "actual_initial_selected_value_and_J.selected_analytic_J102"}
            else:
                meta["complete_analytic_J102"] = _payload(partial_J["matrix"])
        else:
            matrix = partial_J.get("matrix")
            meta["actually_completed_column_values"] = []
            if isinstance(matrix, np.ndarray):
                for block in partial_J.get("completed_column_blocks", []):
                    rows = block["rows"]
                    meta["actually_completed_column_values"].append({
                        **_numeric(block),
                        "values": _payload(matrix[rows, block["column_start"]:block["column_stop"]])})
            if "current_kernel_arrays" in partial_J:
                meta["actually_completed_current_angular_kernels"] = _numeric(partial_J["current_kernel_arrays"])
            meta["unfilled_matrix_storage_is_not_scientific_output"] = True
        result["actually_last_J_or_partial"] = _numeric(meta)
    result["all_other_successful_full_grid_arrays_not_saved_for_free_future_replay"] = True
    return result


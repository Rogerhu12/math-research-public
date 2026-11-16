#!/usr/bin/env python3
"""Original physical159 domain and complete metric first-order separator at true53.

This module builds no optimizer from the closed HiGHS/conic epochs. It reuses
the original scalar row formulas, direct ordinary caches, selected derivatives,
physical map, empirical group8 targets, and complete-angle directional formula.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_entry_tail_height_blocks import (
    N, P, SelectedMappedRows, build_primary, _physical_gaps)
from frame_selected_row_metric_observables import SelectedMetricObservables
from frame_metric_affine_spectral_model import phi, phi_gradient
from frame_complete_affine_metric_oracle import (
    direction_frame_jets)
from frame_selected_row_radial_jacobian import target_frame, periodic_operator
from frame_metric_curvature_defect_guard import apply_primary_guard
from frame_metric_complete_maximin_projection import (
    POLICY, LABELS, ALGORITHM, ProjectionLedger, ProjectionLimit,
    require, finite, owned, exact_vector, guard_compatible_interval)

SOURCE_ACCEPTED_INDEX = 53
SOURCE_PHYSICAL_SHA = "9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e"
SOURCE_CFG_SHA = "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA = "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"


def implementation_hashes():
    from frame_selected_row_metric_observables import implementation_hashes as selected_hashes
    out = selected_hashes()
    for name in ("frame_metric_complete_maximin_projection.py", Path(__file__).name):
        p = Path(__file__).with_name(name)
        out[name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def _integer_ids(values, count, label):
    a = np.asarray(values)
    require(a.ndim == 1 and a.dtype.kind in "iu" and len(a) > 0
            and np.all(a >= 0) and np.all(a < 11*count)
            and len(np.unique(a)) == len(a),
            "original ordered integer unique IDs required: "+label)
    return np.array(a, dtype=np.int64, copy=True)


def _row_tag_key(tag):
    require(tag.get("grid") in LABELS and type(tag.get("group")) is int
            and tag["group"] in (0, 1) and type(tag.get("flat_row_id")) is int,
            "literal original metric row tag required")
    return (tag["grid"], tag["flat_row_id"])


def _small_direction_record(direction):
    return {
        "independent_step_binary64": np.asarray(direction, float).tolist(),
        "exact_binary64_independent_step": exact_vector(direction),
        "independent_step_sha256": array_digest(np.asarray(direction, float)),
        "independent_step_length": len(direction),
    }


def _array_payload(value):
    a = np.asarray(value)
    return {"values": a.tolist(), "shape": list(a.shape), "dtype": str(a.dtype),
            "array_sha256": array_digest(a)}


def _original_domain_record(primary):
    """One unscaled J and one physical map, sufficient to recover the hard rows."""
    groups = np.asarray(primary.active_groups)
    hard, soft = np.flatnonzero(groups >= 2), np.flatnonzero(groups < 2)
    tags = primary.information["active_original_rows"]
    m = len(primary.active_values)
    return {
        "variables": ["z_159", "physical_norm_h", "normalized_gain_s"],
        "hard_original_selected_positions": hard.tolist(),
        "hard_original_row_tags": [copy.deepcopy(tags[int(i)]) for i in hard],
        "hard_groups": groups[hard].tolist(),
        "hard_base_values": _array_payload(primary.active_values[hard]),
        "hard_unscaled_physical159_J": _array_payload(primary.active_J[hard]),
        "hard_frozen_targets": _array_payload(primary.targets[hard]),
        "hard_original_h_column": _array_payload(primary.A[hard, -1]),
        "hard_margin_formula": "base + J @ actual_delta >= frozen_target",
        "selected_metric_original_positions": soft.tolist(),
        "selected_metric_original_row_tags": [copy.deepcopy(tags[int(i)]) for i in soft],
        "selected_metric_base_margins": _array_payload(primary.active_values[soft]),
        "selected_metric_gradients_of_phi": _array_payload(-primary.active_J[soft]),
        "physical_M": _array_payload(primary.subspace.M),
        "physical_width": _array_payload(primary.width),
        "original_qscale": _array_payload(primary.qscale),
        "actual_step_scale": _array_payload(primary.step_scale),
        "common_radius": float(primary.common_radius), "trust_B": float(primary.trust),
        "physical_original_lower163": _array_payload(primary.original_lower),
        "physical_original_upper163": _array_payload(primary.original_upper),
        "physical_and_norm_original_rhs": _array_payload(primary.b[m:m+4*P]),
        "outer_x_lower_z_then_h": _array_payload(np.r_[primary.lower[:N], 0.]),
        "outer_x_upper_z_then_h": _array_payload(np.r_[primary.upper[:N], 1.]),
        "normalized_K_sha256": array_digest(primary.K),
        "normalized_K_reconstruction": "diag(1 / width) @ M @ diag(qscale)",
        "scaled_delta_reconstruction": "actual_step_scale * z",
        "physical_norm_row_order": ["+K physical", "-K physical", "+K minus h", "-K minus h"],
        "scaled_A_K_G_and_inverse_not_duplicated_as_numeric_arrays": True,
        "original_guard": copy.deepcopy(primary.information.get("curvature_defect_guard")),
    }


def model_build_report(capture):
    """JSON-safe build progress; never accidentally duplicate the large arrays."""
    require(isinstance(capture, dict), "the original model-build capture required")
    out = copy.deepcopy({key: value for key, value in capture.items() if key != "_arrays"})
    arrays = capture.get("_arrays", {})
    out["available_selected_grid_arrays"] = sorted(arrays.get("selected_grids", {}))
    out["available_complete_base_grid_arrays"] = sorted(arrays.get("base_grids", {}))
    out["guarded_original_primary_is_available"] = arrays.get("primary") is not None
    out["large_array_payload_is_only_in_one_full_or_partial_original_stdout_record"] = True
    return out


def partial_model_record(capture):
    """Read already completed array work after any failed build; never rebuild."""
    require(isinstance(capture, dict), "the original model-build capture required")
    arrays = capture.get("_arrays", {})
    primary = arrays.get("primary")
    record = {
        "schema": POLICY+"-partial-original-model",
        "status": "incomplete-model-no-new-qualification",
        "build_report": model_build_report(capture),
        "available_base_e_f": {
            label: {key: _array_payload(value) for key, value in row.items()}
            for label, row in arrays.get("base_grids", {}).items()},
        "no_geometry_J_or_JVP_recomputed_for_output": True,
        "one_plaintext_stdout_record_not_API_chunking_or_Git_payload": True,
    }
    if primary is not None:
        record["original_domain"] = _original_domain_record(primary)
    else:
        record["already_completed_selected_grid_arrays"] = {
            label: {"ordered_row_ids": row["ids"].tolist(),
                    "unscaled_original_selected159_J": _array_payload(row["J"])}
            for label, row in arrays.get("selected_grids", {}).items()}
    return record


def build_from_current_objective(objective, prepared, ledger, *, frozen_learning,
                                 source_binding, capture=None):
    """Use exactly the two already charged same-state ordinary caches.

    Root's new recovery entry creates these caches once for the new hard model.
    No call to evaluate/fine_decision/linear_rows/old optimizer is made here.
    """
    require(isinstance(ledger, ProjectionLedger), "one new projection ledger required")
    ledger.check()
    capture = {} if capture is None else capture
    require(isinstance(capture, dict) and not capture, "fresh model-build report sink required")
    capture.update(status="building", source_binding=copy.deepcopy(source_binding),
                   _arrays={"selected_grids": {}, "base_grids": {}})
    state = finite(prepared["initial159"], (N,), "actual accepted53")
    field, cfg = prepared["problem"], prepared["cfg"]
    require(digest(field.identity(state)) == SOURCE_PHYSICAL_SHA
            and digest(field.evaluation_definition()) == SOURCE_FIELD_SHA
            and digest(cfg) == SOURCE_CFG_SHA,
            "source53 physical point/ordinary evaluator/configuration changed")
    require(source_binding["physical_state_sha256"] == SOURCE_PHYSICAL_SHA
            and source_binding["accepted_index"] == SOURCE_ACCEPTED_INDEX,
            "explicit real53 source binding required")
    require(objective.problem is field and np.array_equal(objective.radial, prepared["radial"])
            and np.array_equal(objective.theta, prepared["theta"]),
            "one shared field and original current grids required")
    require((objective.pool_version, objective.fine_pool_version) == (13, 14),
            "the paid53 pool versions must be restored without initialization")
    grids = prepared["row_grids"]
    require(set(grids) == set(LABELS), "the two original rational grids required")
    pools = {
        "coarse": _integer_ids(objective.pool, grids["coarse"].point_count, "coarse"),
        "fine": _integer_ids(objective.fine_pool, grids["fine"].point_count, "fine")}
    require((len(pools["coarse"]), len(pools["fine"])) == (4448, 4549),
            "the true53 learned row counts differ")
    require(np.array_equal(pools["coarse"], prepared["coarse_pool"])
            and np.array_equal(pools["fine"], prepared["fine_pool"]),
            "root-restored original row order changed")
    data = {"coarse": objective.geometry_cache, "fine": (
        objective.fine_cache["data"] if isinstance(objective.fine_cache, dict) else None)}
    require(all(isinstance(data[label], dict) for label in LABELS),
            "new same53 ordinary caches required before the selected-J build")
    require(np.array_equal(data["coarse"]["state"], state)
            and np.array_equal(objective.fine_cache["state"], state),
            "same current53 cache state required")
    factorized = SelectedMetricObservables(field, cfg)
    bounds, jacobians, reports = {}, {}, {}
    for label in LABELS:
        theta = prepared["theta"] if label == "coarse" else objective.fine_theta
        bounds[label] = factorized.bind_ordinary(
            state, prepared["radial"], theta, data[label],
            owner=label+"-current-cache")
        bounds[label]["objective_evaluation_sha256"] = objective.evaluation_sha256
        event = ledger.begin("hard_J_grid_builds", grid=label, original_row_count=len(pools[label]))
        capture.setdefault("selected_J_builds", []).append(event)
        try:
            width_key = ("radial_Jacobian_batch_owned_rows" if label == "coarse"
                         else "fine_Jacobian_owned_radial_rows")
            J, report, obs = factorized.evaluate(
                state, prepared["radial"], theta, pools[label], bounds[label],
                side=field.port.side, owned_width=cfg[width_key], wall=ledger.check)
            jacobians[label] = owned(finite(J, (len(pools[label]), N), "new selected159 "+label))
            capture["_arrays"]["selected_grids"][label] = {
                "ids": pools[label].copy(), "J": jacobians[label]}
            reports[label] = report
            ledger.end(event, returned_J_sha256=array_digest(J),
                       returned_metric_observable_binding_sha256=obs["binding_sha256"],
                       selected_factorization=copy.deepcopy(report))
            ledger.check()
        except Exception as error:
            ledger.end(event, error)
            raise
    # full_views reads those exact ordinary caches; it does not request geometry.
    value_count_before = objective.full_value_evaluations
    full = objective.full_views(state)
    require(objective.full_value_evaluations == value_count_before,
            "binding original full rows unexpectedly evaluated another physical point")
    selections = [SelectedMappedRows(objective.subspace, full[i], pools[label], jacobians[label])
                  for i, label in enumerate(LABELS)]
    cp = prepared["replay"]["source_checkpoint"]
    trust = float(cp["terminal_trust"])
    require(trust == .00025, "source53 actual B must be inherited exactly")
    primary = build_primary(
        objective.subspace, full, selections, state, objective.physical_lower,
        objective.physical_upper, objective.constant_cap(),
        trust_exact=str(Q.from_float(trust)),
        fraction_to_boundary_exact=cfg["linear_fraction_to_boundary_exact"],
        physical_norm_weight_exact=cfg["step_cost_physical_box_norm_coefficient_exact"],
        strip_floor_exact=cfg["strip_proposal_floor_exact"],
        curvature_floor_exact=cfg["curvature_proposal_floor_exact"])
    guard = apply_primary_guard(primary, frozen_learning, cfg)
    capture["_arrays"]["primary"] = primary
    capture.update(
        original_hard_scalar_model_sha256=primary.information["radius_independent_model_sha256"],
        original_guard=copy.deepcopy(guard), no_old_LP_or_affine_cone_factory_called=True,
        selected_J_reports=copy.deepcopy(reports),
        source_ordinary_value_count_did_not_change_inside_model_builder=True)
    model = CompleteFirstOrderModel(
        primary, factorized, bounds, grids, cfg, ledger,
        source_binding=source_binding, objective_evaluation_sha256=objective.evaluation_sha256,
        pool_versions={"coarse": objective.pool_version, "fine": objective.fine_pool_version},
        original_pool_ids=pools, build_capture=capture)
    capture["complete_model_binding_sha256"] = model.binding_sha256
    capture["status"] = "complete"
    ledger.check()
    return model


class CompleteFirstOrderModel:
    def __init__(self, primary, factorized, bounds, grids, cfg, ledger, *,
                 source_binding, objective_evaluation_sha256, pool_versions,
                 original_pool_ids, build_capture=None):
        require(isinstance(ledger, ProjectionLedger)
                and isinstance(factorized, SelectedMetricObservables),
                "true selected derivative implementation and new ledger required")
        self.primary, self.factorized, self.field = primary, factorized, factorized.field
        self.cfg, self.ledger = cfg, ledger
        self.state = owned(factorized.field.coordinates.validate(primary.state))
        self.reference163 = owned(self.field.coordinates.reference_evaluation_state(self.state))
        self.grids, self.bounds = dict(grids), dict(bounds)
        self.original_pool_ids = {label: np.asarray(ids, np.int64).copy()
                                  for label, ids in original_pool_ids.items()}
        for ids in self.original_pool_ids.values():
            ids.flags.writeable = False
        self._build_capture = build_capture
        self.K, self.step_scale = owned(primary.K), owned(primary.step_scale)
        self.mu = float(primary.c[-1])
        self.epsilon = float(Q(cfg["metric_proposal_epsilon_exact"]))
        self.target = float(Q(cfg["fixed_metric_budget_exact"]))
        require(self.K.shape == (P, N) and self.mu > 0 and np.isfinite(self.mu)
                and self.epsilon == 1e-8 and self.target == .26,
                "unchanged original physical norm/epsilon/target required")
        require(np.array_equal(self.step_scale, primary.common_radius*primary.qscale),
                "the one original physical step scaling changed")
        self.cfg_sha256 = digest(cfg)
        self.lower_x = owned(np.r_[primary.lower[:N], 0.])
        self.upper_x = owned(np.r_[primary.upper[:N], 1.])
        self._hard_positions = np.flatnonzero(np.asarray(primary.active_groups) >= 2)
        self.hard_base = owned(primary.active_values[self._hard_positions])
        self.hard_J = owned(primary.active_J[self._hard_positions])
        self.hard_targets = owned(primary.targets[self._hard_positions])
        self._selected_gradient = {}
        for i, tag in enumerate(primary.information["active_original_rows"]):
            if int(primary.active_groups[i]) < 2:
                self._selected_gradient[_row_tag_key(tag)] = {
                    "gradient": owned(-primary.active_J[i]),
                    "base_margin": float(primary.active_values[i]),
                    "source": "same-current53-already-built-selected-scalar-J"}
        self._metric_rows, self.row_events = {}, []
        self._hard_row_cache = None
        self.base, self.base_events, self.direction_events = {}, [], []
        self._last_scan, self._best_scan = None, None
        self.original_row_statistics = {"calls_started": 0, "calls_completed": 0,
                                        "seconds_including_failed_calls": 0.}
        self.original_value_binding = {
            "field": factorized.ordinary_evaluation_sha256,
            "factorization": factorized.definition_sha256,
            "state": array_digest(self.state),
            "grids": {label: {"grid": grids[label].definition_sha256,
                              "radial": array_digest(bounds[label]["radial"]),
                              "theta": array_digest(bounds[label]["theta"])} for label in LABELS}}
        for label in LABELS:
            event = ledger.begin("first_jet_grid_builds", grid=label)
            self.base_events.append(event)
            try:
                bound, grid = bounds[label], grids[label]
                require(bound["factorization_definition_sha256"] == factorized.definition_sha256
                        and bound["ordinary_evaluation_definition_sha256"] == factorized.ordinary_evaluation_sha256
                        and np.array_equal(bound["state"], self.state),
                        "same current ordinary field/factorization binding required")
                r, th, data = bound["radial"], bound["theta"], bound["data"]
                require(len(r) == grid.nr and len(th) == grid.nt
                        and np.array_equal(r, np.array([float(v) for v in grid.nodes])),
                        "original complete rational grid differs from its bound cache")
                old = {"U": finite(data["Xs"], (grid.nr, grid.nt, 3)),
                       "T": finite(data["T"], (grid.nr, grid.nt, 3)),
                       "a": finite(data["metric"]["a"], (grid.nr,)),
                       "a_s": finite(data["metric"]["a_s"], (grid.nr,))}
                old["e"] = np.sum(old["U"]*old["U"], axis=2)-1.
                old["f"] = np.sum(old["U"]*old["T"], axis=2)
                scalar_grid = factorized.single.source.grid_for(r, th)
                fields = scalar_grid.fields(self.reference163)
                fields["_theta"] = th[None, :]
                frame = target_frame(fields)
                T = finite(frame["T"], (len(r), len(th), 3), "new current T")
                error = float(np.max(abs(T-old["T"]), initial=0.))
                tolerance = float(cfg["value_Jacobian_replay_relative_tolerance"])*max(
                    1., float(np.max(abs(old["T"]), initial=0.)))
                require(error <= tolerance, "new first-jet frame differs from original current cache")
                U, T = owned(old["U"]), owned(old["T"])
                e, f = owned(old["e"].reshape(-1)), owned(old["f"].reshape(-1))
                if self._build_capture is not None:
                    self._build_capture["_arrays"]["base_grids"][label] = {"e": e, "f": f}
                C = owned(finite(self.field.null_basis.values(r), (len(r), 5), "original null density"))
                branches = []
                for group in (0, 1):
                    groups = np.full(len(e), group, dtype=np.int64)
                    value = owned(phi(e, f, groups, self.epsilon))
                    ge, gf = phi_gradient(e, f, groups, self.epsilon)
                    branches.append({"phi": value, "ge": owned(ge), "gf": owned(gf)})
                self.base[label] = {
                    "U": U, "T": T, "e": e, "f": f,
                    "a": owned(old["a"]), "a_s": owned(old["a_s"]), "null": C,
                    "scalar_grid": scalar_grid, "fields": fields, "frame": frame,
                    "radial": owned(r), "theta": owned(th), "branches": branches}
                ledger.end(event, current_U_sha256=array_digest(U), current_T_sha256=array_digest(T),
                           e_sha256=array_digest(e), f_sha256=array_digest(f),
                           original_frame_replay_max_error=error,
                           original_geometry_or_direction_calls=0,
                           point_count=grids[label].point_count)
                ledger.check()
            except Exception as error:
                ledger.end(event, error)
                raise
        self.phi0 = max(self.target, *(float(np.max(self.base[label]["branches"][group]["phi"]))
                                       for label in LABELS for group in (0, 1)))
        self.binding = {
            "schema": POLICY+"-complete-first-order-model",
            "source_binding": copy.deepcopy(source_binding),
            "state_sha256": array_digest(self.state),
            "physical_state_sha256": digest(self.field.identity(self.state)),
            "reference163_sha256": array_digest(self.reference163),
            "coordinate_definition_sha256": self.field.coordinate_definition_sha256,
            "ordinary_field_evaluation_sha256": factorized.ordinary_evaluation_sha256,
            "objective_evaluation_sha256": objective_evaluation_sha256,
            "original_factorization_definition_sha256": factorized.definition_sha256,
            "original_complete_value_binding_sha256": digest(self.original_value_binding),
            "configuration_sha256": self.cfg_sha256,
            "original_scalar_guarded_model_sha256": primary.information["radius_independent_model_sha256"],
            "original_guard": copy.deepcopy(primary.information["curvature_defect_guard"]),
            "pool_versions": copy.deepcopy(pool_versions),
            "pool_ids_sha256": {label: array_digest(original_pool_ids[label]) for label in LABELS},
            "original_grid_definitions": {label: copy.deepcopy(grids[label].definition) for label in LABELS},
            "B": float(primary.trust), "step_scale_sha256": array_digest(self.step_scale),
            "K_sha256": array_digest(self.K), "mu": self.mu, "complete_phi0": self.phi0,
            "full_metric_point_counts": {label: grids[label].point_count for label in LABELS},
            "target_constant_branch_included": True,
            "old_affine_factories_or_backends_called": 0}
        self.binding_sha256 = digest(self.binding)

    def _assert(self):
        self.ledger.check()
        self.factorized._assert_context()
        require(digest(self.cfg) == self.cfg_sha256
                and digest(self.binding) == self.binding_sha256
                and np.array_equal(self.primary.state, self.state),
                "frozen true53 complete first-order model changed")

    def hard_rows(self):
        """Reorder original (z,rho,h) rows to (z,h,s), remove only scalar soft rows."""
        if self._hard_row_cache is not None:
            return self._hard_row_cache
        primary = self.primary
        m = len(primary.active_values)
        rows = []
        for i in self._hard_positions:
            A = np.r_[primary.A[i, :N], primary.A[i, -1], 0.]
            rows.append({
                "A": A, "b": float(primary.b[i]),
                "tolerance": float(self.cfg["linear_model_residual_limit"]),
                "kind": "hard",
                "tag": copy.deepcopy(primary.information["active_original_rows"][int(i)])})
        for offset in range(4*P):
            i = m+offset
            kind = "physical" if offset < 2*P else "norm"
            rows.append({
                "A": np.r_[primary.A[i, :N], primary.A[i, -1], 0.],
                "b": float(primary.b[i]),
                "tolerance": float(self.cfg["linear_model_residual_limit"]),
                "kind": kind, "tag": {"original_primary_row": int(i), "physical_row_offset": offset}})
        for j, (lo, hi) in enumerate(zip(self.lower_x, self.upper_x)):
            A = np.zeros(N+2)
            A[j] = 1.
            rows.append({"A": A.copy(), "b": float(hi), "tolerance": float(self.cfg["linear_model_residual_limit"]),
                         "kind": "bound", "tag": {"coordinate": j, "side": "upper"}})
            rows.append({"A": -A, "b": -float(lo), "tolerance": float(self.cfg["linear_model_residual_limit"]),
                         "kind": "bound", "tag": {"coordinate": j, "side": "lower"}})
        self._hard_row_cache = rows
        return rows

    def _attainer(self, label, group, point, value, slope):
        grid = self.grids[label]
        return {
            "grid": label, "group": group, "point": int(point),
            "original_row": grid.coordinate(group*grid.point_count+int(point)),
            "base_phi": float(self.base[label]["branches"][group]["phi"][point]),
            "base_gap": self.phi0-float(self.base[label]["branches"][group]["phi"][point]),
            "directional_slope": float(slope), "linear_branch_value": float(value)}

    def initial_metric_rows(self):
        A = np.r_[np.zeros(N), self.mu, self.mu]
        rows = [{"A": A, "b": self.phi0-self.target,
                 "tolerance": float(self.cfg["metric_row_tolerance"]),
                 "kind": "metric", "tag": {"constant_original_target": self.target}}]
        for label in LABELS:
            for group in (0, 1):
                values = self.base[label]["branches"][group]["phi"]
                point = int(np.argmax(values))
                item = self._attainer(label, group, point, values[point], 0.)
                rows.append(self.metric_row(item, None))
        return rows

    def _direction(self, p, phase):
        self._assert()
        p = owned(finite(p, (N,), "actual one-direction input"))
        event = self.ledger.begin(
            "full_separations", phase=phase, direction_sha256=array_digest(p),
            model_binding_sha256=self.binding_sha256)
        self.direction_events.append(event)
        for previous in (self._last_scan, self._best_scan):
            if previous is not None and np.array_equal(previous["direction"], p):
                event.update(cache_hit=True, new_full_grid_JVP_calls=0)
                self.ledger.end(event, full_grid_coverage=copy.deepcopy(previous["coverage"]))
                self.ledger.check()
                return previous
        arrays, branches, coverage = {}, [], {}
        try:
            for label in LABELS:
                self.ledger.check()
                d, grid = self.base[label], self.grids[label]
                tick = time.monotonic()
                grid_event = {"grid": label, "status": "direction-started",
                              "new_full_grid_JVP_started": 1}
                event.setdefault("grids", []).append(grid_event)
                dT, dTs = direction_frame_jets(
                    self.factorized, d["scalar_grid"], d["fields"], d["frame"], p)
                dP0, dP1 = periodic_operator(dT, -1), periodic_operator(dTs, -1)
                dU = d["a_s"][:, None, None]*dP0+d["a"][:, None, None]*dP1
                dU[:, :, 2] += (d["null"]@p[154:])[:, None]
                de = owned((2*np.sum(d["U"]*dU, axis=2)).reshape(-1))
                df = owned(np.sum(d["T"]*dU+d["U"]*dT, axis=2).reshape(-1))
                require(len(de) == len(df) == grid.point_count,
                        "the complete original grid was not covered exactly once")
                arrays[label] = {"e": d["e"], "f": d["f"], "de": de, "df": df}
                coverage[label] = grid.point_count
                for group in (0, 1):
                    b = d["branches"][group]
                    slopes = b["ge"]*de+b["gf"]*df
                    values = b["phi"]+slopes
                    finite(values, (grid.point_count,), "complete first-order branch")
                    point = int(np.argmax(values))
                    branches.append(self._attainer(label, group, point, values[point], slopes[point]))
                grid_event.update(
                    status="complete", point_count=grid.point_count,
                    seconds=time.monotonic()-tick,
                    de_sha256=array_digest(de), df_sha256=array_digest(df),
                    no_selected_parameter_tensor_formed=True)
                self.ledger.check()
            scan = {
                "direction": p, "direction_sha256": array_digest(p),
                "model_binding_sha256": self.binding_sha256, "arrays": arrays,
                "branches": branches, "coverage": coverage,
                "linear_maximum": max(self.target, *(x["linear_branch_value"] for x in branches)),
                "base_phi": self.phi0, "target": self.target}
            self._last_scan = scan
            self.ledger.end(event, cache_hit=False, new_full_grid_JVP_calls=2,
                            full_grid_coverage=copy.deepcopy(coverage),
                            branches=copy.deepcopy(branches),
                            linear_maximum=scan["linear_maximum"])
            self.ledger.check()
            return scan
        except Exception as error:
            if event.get("grids") and event["grids"][-1]["status"] == "direction-started":
                event["grids"][-1].update(
                    status="raised", seconds=time.monotonic()-tick,
                    error={"type": type(error).__name__, "message": str(error)})
            self.ledger.end(event, error, completed_grid_coverage=copy.deepcopy(coverage),
                            completed_coefficient_sha256={
                                label: {key: array_digest(value) for key, value in row.items()}
                                for label, row in arrays.items()})
            raise

    def scan(self, w, *, phase):
        w = finite(w, (N+2,), "actual maximin iterate")
        return self._direction(self.step_scale*w[:N], phase)

    def scan_summary(self, scan):
        return {
            "direction_sha256": scan["direction_sha256"],
            "model_binding_sha256": scan["model_binding_sha256"],
            "linear_maximum": float(scan["linear_maximum"]),
            "base_phi": self.phi0, "coverage": copy.deepcopy(scan["coverage"]),
            "branches": copy.deepcopy(scan["branches"]),
            "array_sha256": {label: {key: array_digest(value) for key, value in row.items()}
                             for label, row in scan["arrays"].items()}}

    def pin_best(self, scan):
        require(scan["model_binding_sha256"] == self.binding_sha256,
                "best direction belongs to another current model")
        self._best_scan = scan

    def violating_attainers(self, w, scan):
        w = finite(w, (N+2,), "actual maximin iterate")
        addition = self.mu*(w[-2]+w[-1])
        tol = float(self.cfg["metric_row_tolerance"])
        return [item for item in scan["branches"]
                if item["linear_branch_value"]+addition-self.phi0 > tol]

    def metric_row(self, item, scan):
        self._assert()
        label, group, point = item["grid"], item["group"], item["point"]
        grid = self.grids[label]
        require(type(group) is int and group in (0, 1) and type(point) is int
                and 0 <= point < grid.point_count, "literal complete metric attainer identity required")
        flat = group*grid.point_count+point
        tag = grid.coordinate(flat)
        key = (label, flat)
        if key not in self._metric_rows:
            selected = self._selected_gradient.get(key)
            parts = grid.classify([flat], self.primary.subspace)
            if selected is not None:
                gradient = selected["gradient"]
                source = selected["source"]
                expected = self.target-self.base[label]["branches"][group]["phi"][point]
                err = abs(expected-selected["base_margin"])
                tol = float(self.cfg["value_Jacobian_replay_relative_tolerance"])*max(
                    1., abs(expected), abs(selected["base_margin"]))
                require(err <= tol, "selected original metric value differs from complete base")
            elif not bool(parts["variable"][0]):
                gradient = np.zeros(N)
                source = "proved-original-support-invariant-zero-directional-row"
            else:
                event = self.ledger.begin("new_metric_rows", original_row=copy.deepcopy(tag))
                self.row_events.append(event)
                try:
                    width_key = ("radial_Jacobian_batch_owned_rows" if label == "coarse"
                                 else "fine_Jacobian_owned_radial_rows")
                    self.original_row_statistics["calls_started"] += 1
                    tick = time.monotonic()
                    try:
                        J, report, obs = self.factorized.evaluate(
                            self.state, self.base[label]["radial"], self.base[label]["theta"],
                            [flat], self.bounds[label], side=self.field.port.side,
                            owned_width=self.cfg[width_key], wall=self.ledger.check)
                        require(J.shape == (1, N) and len(obs["e"]) == 1
                                and int(obs["row_ids"][0]) == flat
                                and int(obs["row_positions"][0]) == 0,
                                "new metric derivative lost its original row identity")
                        ge, gf = phi_gradient(obs["e"], obs["f"], obs["groups"], self.epsilon)
                        gradient = owned(ge[0]*obs["de"][0]+gf[0]*obs["df"][0])
                        source = "new-single-original-metric-row-at-current53"
                        self.original_row_statistics["calls_completed"] += 1
                        self.ledger.end(event, gradient_sha256=array_digest(gradient),
                                        selected_observable_binding_sha256=obs["binding_sha256"],
                                        selected_factorization=copy.deepcopy(report))
                    finally:
                        self.original_row_statistics["seconds_including_failed_calls"] += time.monotonic()-tick
                    self.ledger.check()
                except Exception as error:
                    self.ledger.end(event, error)
                    raise
            gradient = owned(finite(gradient, (N,), "metric physical159 derivative"))
            self._metric_rows[key] = {
                "A": np.r_[gradient*self.step_scale, self.mu, self.mu],
                "b": self.phi0-float(self.base[label]["branches"][group]["phi"][point]),
                "tolerance": float(self.cfg["metric_row_tolerance"]), "kind": "metric",
                "tag": tag, "gradient": gradient, "source": source}
        row = self._metric_rows[key]
        if scan is not None:
            require(scan["model_binding_sha256"] == self.binding_sha256, "row/direction context changed")
            direct = float(row["gradient"]@scan["direction"])
            observed = float(item["directional_slope"])
            error = abs(direct-observed)
            tolerance = float(self.cfg["value_Jacobian_replay_relative_tolerance"])*max(
                1., abs(direct), abs(observed))
            require(error <= tolerance, "new selected metric gradient and paid full JVP disagree")
            row["last_chain_rule_comparison"] = {
                "direction_sha256": scan["direction_sha256"],
                "selected_dot_actual_direction": direct, "complete_directional_slope": observed,
                "absolute_error": error, "original_relative_tolerance_limit": tolerance,
                "no_additional_JVP_or_geometry_for_comparison": True}
        return {key: copy.deepcopy(value) if key == "tag" else value
                for key, value in row.items() if key in ("A", "b", "tolerance", "kind", "tag")}

    def _residual(self, w):
        w = finite(w, (N+2,), "actual repaired maximin vector")
        rows = self.hard_rows()
        residual = np.array([float(row["A"]@w-row["b"]) for row in rows])
        tolerance = np.array([row["tolerance"] for row in rows])
        return {
            "all_original_hard_physical_norm_bound_rows_passed": bool(np.all(residual <= tolerance)),
            "maximum_original_row_residual": float(np.max(residual, initial=-np.inf)),
            "maximum_excess_over_original_tolerance": float(np.max(residual-tolerance, initial=-np.inf)),
            "strict_model_all_rows_nonpositive": bool(np.all(residual <= 0)),
            "original_residual_tolerance": float(self.cfg["linear_model_residual_limit"])}

    def ideal_candidate(self, w, scan):
        w = finite(w, (N+2,), "actual maximin vector")
        h = float(np.max(abs(self.K@w[:N]), initial=0.))
        gain = self.phi0-float(scan["linear_maximum"])-self.mu*h
        repaired = w.copy()
        repaired[-2], repaired[-1] = h, gain/self.mu
        residual = self._residual(repaired)
        full = residual["all_original_hard_physical_norm_bound_rows_passed"]
        positive = bool(full and gain > float(self.cfg["linear_model_improvement_floor"]))
        report = {
            "raw_norm_h": float(w[-2]), "raw_gain_d": self.mu*float(w[-1]),
            "actual_physical_norm_h": h, "complete_repaired_gain_d": gain,
            "complete_first_order_maximum": float(scan["linear_maximum"]),
            "complete_phi0": self.phi0, "physical_norm_cost": self.mu*h,
            "original_domain": residual, "qualified_positive_ideal_primal": positive,
            "exact163_box_and_actual_rounding_still_required": True,
            "repaired_binary64_vector": repaired.tolist(),
            "repaired_exact_binary64_vector": exact_vector(repaired),
            "full_current_gap_constraints_preserved": True}
        return {"qualified_primal": positive, "gain": gain, "repaired_w": repaired, "report": report}

    def finalize_direction(self, w, previous):
        self._assert()
        w = finite(w, (N+2,), "best actual recorded ideal vector")
        ideal_p = self.step_scale*w[:N]
        candidate = self.primary.subspace.apply(self.state, ideal_p)
        actual_p = finite(candidate-self.state, (N,), "rounded actual direction")
        if np.array_equal(actual_p, previous["direction"]):
            scan = previous
            used_cached = True
        else:
            scan = self._direction(actual_p, "final-actual-rounded-direction")
            used_cached = False
        actual_w = w.copy()
        actual_w[:N] = actual_p/self.step_scale
        checked = self.ideal_candidate(actual_w, scan)
        actual_w = checked["repaired_w"]
        box = self.field.coordinates.exact_box_decision(
            candidate, self.primary.original_lower, self.primary.original_upper)
        require(isinstance(box, dict) and "exact_original_box_pass" in box, "original exact163 box report required")
        qualified = bool(checked["qualified_primal"] and box["exact_original_box_pass"])
        upper_gap, lower_gap = _physical_gaps(
            self.field.coordinates, self.state, self.primary.original_lower, self.primary.original_upper)
        physical_step = self.primary.subspace.M@actual_p
        physical = [(float(gap), -float(delta), 0.) for gap, delta in zip(upper_gap, physical_step)]
        physical += [(float(gap), float(delta), 0.) for gap, delta in zip(lower_gap, physical_step)]
        interval = guard_compatible_interval(
            self.hard_base, self.hard_J@actual_p, self.hard_targets,
            residual_tolerance=float(self.cfg["linear_model_residual_limit"]),
            physical_bounds=physical)
        report = {
            "schema": POLICY+"-final-direction",
            "model_binding_sha256": self.binding_sha256,
            "raw_best_solver_vector": w.tolist(),
            "raw_best_solver_exact_binary64_vector": exact_vector(w),
            "actual_rounded_solver_vector": actual_w.tolist(),
            "actual_rounded_solver_exact_binary64_vector": exact_vector(actual_w),
            **_small_direction_record(actual_p),
            "untried_unit_step_state_exact159": exact_vector(candidate),
            "untried_unit_step_physical_exact163": [
                str(v) for v in self.field.coordinates.physical_exact(candidate)],
            "exact163_box": copy.deepcopy(box),
            "final_complete_original_domain": checked["report"],
            "actual_direction_used_existing_full_scan": used_cached,
            "full_scan": self.scan_summary(scan),
            "guard_compatible_alpha_interval": interval,
            "qualified_first_order_direction": qualified,
            "physical_unit_step_not_evaluated_or_accepted": True}
        return {"qualified": qualified, "direction": actual_p, "scan": scan,
                "candidate": candidate, "interval": interval, "report": report}

    def validate_actual_candidate(self, candidate):
        """Actual sameapply delta against every frozen original hard row; no JVP."""
        self._assert()
        candidate = finite(candidate, (N,), "genuinely untried actual candidate")
        delta = candidate-self.state
        z = delta/self.step_scale
        h = float(np.max(abs(self.K@z), initial=0.))
        w = np.r_[z, h, 0.]
        domain = self._residual(w)
        hard = self.hard_targets-(self.hard_base+self.hard_J@delta)
        box = self.field.coordinates.exact_box_decision(
            candidate, self.primary.original_lower, self.primary.original_upper)
        maximum = float(np.max(hard, initial=-np.inf))
        eligible = bool(box["exact_original_box_pass"]
                        and domain["all_original_hard_physical_norm_bound_rows_passed"]
                        and maximum <= float(self.cfg["linear_model_residual_limit"]))
        return {
            "eligible": eligible, "model_binding_sha256": self.binding_sha256,
            "actual_delta_record": _small_direction_record(delta),
            "actual_state_exact159": exact_vector(candidate),
            "actual_physical_exact163": [
                str(v) for v in self.field.coordinates.physical_exact(candidate)],
            "exact163_box": copy.deepcopy(box),
            "original_hard_margin_max_violation": maximum,
            "original_hard_tolerance": float(self.cfg["linear_model_residual_limit"]),
            "original_domain": domain,
            "no_current_geometry_JVP_or_derivative_recomputation": True,
            "affine_line_prediction_is_not_a_new_actual_geometry_certificate": True,
        }

    def full_record(self):
        """One original numeric model record; report() never repeats these arrays."""
        selected_source = "same-current53-already-built-selected-scalar-J"
        added = []
        installed = []
        for (label, flat), row in self._metric_rows.items():
            item = {"original_row": copy.deepcopy(row["tag"]), "grid": label,
                    "flat_row_id": int(flat), "source": row["source"],
                    "base_gap": float(row["b"]),
                    "original_tolerance": float(row["tolerance"]),
                    "gradient_sha256": array_digest(row["gradient"])}
            installed.append(copy.deepcopy(item))
            if row["source"] != selected_source:
                item["unscaled_physical159_gradient"] = _array_payload(row["gradient"])
                added.append(item)
        return {
            "schema": POLICY+"-complete-original-model",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "source_current_independent159": _array_payload(self.state),
            "source_current_independent_exact159": exact_vector(self.state),
            "source_current_physical_exact163": [
                str(x) for x in self.field.coordinates.physical_exact(self.state)],
            "ordered_original_pool_ids": {
                label: ids.tolist() for label, ids in self.original_pool_ids.items()},
            "original_domain": _original_domain_record(self.primary),
            "complete_base_e_f": {
                label: {key: _array_payload(self.base[label][key]) for key in ("e", "f")}
                for label in LABELS},
            "epsilon": self.epsilon, "constant_target": self.target,
            "complete_original_phi0": self.phi0, "physical_norm_cost_mu": self.mu,
            "installed_metric_rows": installed,
            "additional_metric_gradients_not_already_in_selected_J": added,
            "constant_target_row": {
                "h_coefficient": self.mu, "s_coefficient": self.mu,
                "rhs": self.phi0-self.target, "physical_gradient_is_literal_zero": True},
            "original_selected_soft_gradients_appear_once_in_original_domain": True,
            "new_metric_A_reconstruction": "[gradient * step_scale, mu, mu]",
            "ordinary_position_and_dense_scaled_A_G_not_serialized": True,
            "no_geometry_J_or_JVP_recomputed_for_output": True,
            "one_plaintext_stdout_record_not_API_chunking_or_Git_payload": True,
        }

    def report(self):
        return {
            "schema": POLICY+"-model-progress",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "base_events": copy.deepcopy(self.base_events),
            "direction_events": copy.deepcopy(self.direction_events),
            "new_metric_row_events": copy.deepcopy(self.row_events),
            "new_metric_row_count": len(self.row_events),
            "selected_or_proved_or_new_metric_rows": [
                {"tag": copy.deepcopy(row["tag"]), "source": row["source"],
                 "gradient_sha256": array_digest(row["gradient"]),
                 "base_gap": row["b"],
                 "last_chain_rule_comparison": copy.deepcopy(row.get("last_chain_rule_comparison"))}
                for row in self._metric_rows.values()],
            "original_selected_metric_gradient_cache_count": len(self._selected_gradient),
            "original_single_row_derivative_statistics": copy.deepcopy(self.original_row_statistics),
            "no_actual_pool_bank_gamma_or_controller_mutation_inside_model": True,
            "no_old_primary_LP_cone_or_SOC_called": True}

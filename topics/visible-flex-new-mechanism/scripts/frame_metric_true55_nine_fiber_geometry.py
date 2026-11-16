#!/usr/bin/env python3
"""New-nine input at accepted55, complete baseline-linear separation and caches.

Import-only.  No old159 derivative, old optimizer, trial, log loader or test is
called here.  The caller owns one pre-input/pre-import NineFiberLedger.

Two necessary ordinary values supply the complete current position two-jets.
Only variable hard pool rows enter the two selected J9 calls.  The two complete
metric9 calls supply every metric derivative, including selected soft rows and
later attainers.  A master scan means phi0 + grad(phi0).delta, not the nonlinear
affine-(e,f) scalar predictor.  The latter receives direction_cache() and is
charged by the separate scalar driver.

The exact accepted55 fine theta array must be supplied by transfer; this
module never reconstructs an algebraically equivalent angular array.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import time
from types import SimpleNamespace

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid, FullGridValues, array_digest
from frame_metric_budget_restoration_rows import row_values
from frame_metric_affine_spectral_model import phi, phi_gradient
from frame_complete_body_extension168 import (
    CompleteBody168Field, LEFT_EXACT, RIGHT_EXACT)
from frame_complete_body_extension168_selected import (
    new_nine_selected_rows, new_nine_metric_jets)

POLICY = "fixed159-true55-new9-affine-fiber-v1"
LABELS = ("coarse", "fine")
SOURCE_INDEX = 55
SOURCE_PHYSICAL_SHA = "39e71805432d8e1814032200b8cb70973e95475b4ec02696233a7bb37e57746e"
SOURCE_CFG_SHA = "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA = "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"
POSITION_KEYS = ("X", "Xs", "Xt", "Xss", "Xst", "Xtt", "T")


def require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def _finite(value, shape=None, name="array"):
    a = np.asarray(value, dtype=np.float64)
    require((shape is None or a.shape == shape) and np.all(np.isfinite(a)),
            "finite "+name+" with the declared shape is required")
    return a


def _owned(value, shape=None, name="array"):
    a = _finite(value, shape, name).copy()
    a.setflags(write=False)
    return a


def _ids(value, grid):
    raw = np.asarray(value)
    require(raw.ndim == 1 and raw.dtype.kind in "iu"
            and not raw.dtype.kind == "b",
            "literal original integer pool IDs are required")
    a = grid.ids(raw).astype(np.int64, copy=True)
    a.setflags(write=False)
    return a


def _same_bytes(a, b):
    aa, bb = np.asarray(a), np.asarray(b)
    return aa.dtype == bb.dtype and aa.shape == bb.shape and aa.tobytes() == bb.tobytes()


def _row_tolerances(cfg):
    # The exact original CurvatureEpigraphObjective.row_tolerances order.
    a = np.asarray(
        [cfg["metric_row_tolerance"]]*2
        + [cfg["signed_height_tolerance"]]
        + [cfg["shape_constraint_tolerance"]]*3
        + [cfg["mirror_polynomial_tolerance"]]
        + [cfg["curvature_row_tolerance"]]*4, dtype=float)
    require(a.shape == (11,) and np.all(np.isfinite(a)) and np.all(a >= 0.),
            "all eleven original group tolerances are required")
    a.setflags(write=False)
    return a


def _hard_targets(values, groups, tolerances, cfg):
    """Original fraction-to-boundary and original strip/curvature floors."""
    fraction = float(Q(cfg["linear_fraction_to_boundary_exact"]))
    strip = float(Q(cfg["strip_proposal_floor_exact"]))
    curvature = float(Q(cfg["curvature_proposal_floor_exact"]))
    require(0. < fraction <= 1. and np.isfinite(fraction)
            and min(strip, curvature) >= 0. and np.isfinite(strip+curvature),
            "the original hard-target constants are required")
    result = values-fraction*(values+tolerances)
    for selected, floor in (([4, 5], strip), ([7, 8, 9, 10], curvature)):
        mask = np.isin(groups, selected)
        result[mask] = np.maximum(result[mask], floor)
    return _owned(result, values.shape, "original hard targets")


def build_new_nine_geometry(prepared, ledger, capture=None, *, source_binding=None):
    """Construct exactly one new-nine input; never mutate original pools.

    Required prepared keys:
      problem, initial159, gate, cfg, radial, theta, fine_theta, row_grids,
      order, coarse_pool, fine_pool, source_binding, replay.
    gate.original_lower/original_upper are the true physical163 boxes.
    lower/upper159 pivot envelopes are never substituted for those boxes.

    Appends field168, q168, initial168, lower172, upper172 to prepared.
    capture receives small progress metadata and an _arrays entry containing
    references to completed inputs.  A reporting driver must serialize these
    intentionally, not print the opaque cache indiscriminately.
    """
    require(isinstance(prepared, dict), "the one restored accepted55 input is required")
    require(all(callable(getattr(ledger, name, None))
                for name in ("check", "elapsed", "begin", "end")),
            "one externally owned shared scientific ledger is required")
    ledger.check("nine-geometry.entry")
    sink = {} if capture is None else capture
    require(isinstance(sink, dict) and not sink, "an empty build capture is required")
    sink.update(schema=POLICY+"-new-input-build", status="started", grids={},
                _arrays={}, source_accepted_index=SOURCE_INDEX,
                old159_derivative_calls=0, repeated_old_model_calls=0)
    obj = NineFiberGeometry.__new__(NineFiberGeometry)
    try:
        obj._build(prepared, ledger, sink, source_binding)
        sink.update(status="complete", binding_sha256=obj.binding_sha256,
                    receipt=obj.receipt())
        ledger.check("nine-geometry.complete")
        return obj
    except Exception as error:
        sink.update(status="raised",
                    error={"type": type(error).__name__, "message": str(error)},
                    scientific_seconds=ledger.elapsed())
        raise


class NineFiberGeometry:
    """One immutable current55/new-nine baseline and its complete derivative caches."""

    def _build(self, prepared, ledger, capture, source_binding):
        self.ledger, self.capture = ledger, capture
        self.cfg = copy.deepcopy(prepared["cfg"])
        self.cfg_sha256 = digest(self.cfg)
        self.original_field = prepared["problem"]
        self.initial159 = _owned(prepared["initial159"], (159,), "accepted55 independent159")
        require(digest(self.original_field.identity(self.initial159)) == SOURCE_PHYSICAL_SHA
                and digest(self.original_field.evaluation_definition()) == SOURCE_FIELD_SHA
                and self.cfg_sha256 == SOURCE_CFG_SHA,
                "accepted55, its frozen g/b0/reference and original cfg must be unchanged")
        binding = prepared.get("source_binding") if source_binding is None else source_binding
        require(isinstance(binding, dict)
                and binding.get("accepted_index") == SOURCE_INDEX
                and binding.get("independent159_array_sha256") == array_digest(self.initial159),
                "explicit accepted55 source identity and exact independent vector are required")
        self.source_binding = copy.deepcopy(binding)
        prepared["source_binding"] = copy.deepcopy(binding)
        self.field = self.field168 = CompleteBody168Field(self.original_field)
        self.center168 = self.q168 = _owned(
            self.field.embed_state(self.initial159), (168,), "zero-nine168")
        require(np.array_equal(self.center168[:159], self.initial159)
                and np.array_equal(self.center168[159:], np.zeros(9)),
                "the old159 must remain fixed and all new coefficients start at exact zero")
        gate = prepared["gate"]
        lo = _finite(gate.original_lower, (163,), "original physical lower163")
        hi = _finite(gate.original_upper, (163,), "original physical upper163")
        self.lower172 = _owned(np.r_[lo, np.full(9, -.25)], (172,))
        self.upper172 = _owned(np.r_[hi, np.full(9, .25)], (172,))
        require(np.all(self.lower172 < self.upper172),
                "all true physical172 boxes must be strictly ordered")
        self.center_box = self.field.exact_full_box_decision(
            self.center168, self.lower172, self.upper172)
        require(self.center_box["exact_full_box_pass"],
                "the zero-nine true55 point must satisfy all exact172 boxes")
        prepared.update(field168=self.field, q168=self.center168,
                        initial168=self.center168, lower172=self.lower172,
                        upper172=self.upper172)

        self.radial = _owned(prepared["radial"], name="original radial grid")
        self.theta = _owned(prepared["theta"], name="original coarse theta")
        require("fine_theta" in prepared,
                "transfer must provide the paid source55 fine-theta binary64 array")
        self.fine_theta = _owned(prepared["fine_theta"], name="source55 fine theta")
        require(self.radial.ndim == self.theta.ndim == self.fine_theta.ndim == 1
                and len(self.fine_theta) == 2*len(self.theta),
                "the actual complete coarse/fine grids are required")
        self.grids = prepared["row_grids"]
        require(isinstance(self.grids, dict) and set(self.grids) == set(LABELS),
                "both original RationalRowGrid objects are required")
        require(all(isinstance(self.grids[label], RationalRowGrid)
                    and self.grids[label].label == label for label in LABELS),
                "the original grid/row-ID identities are required")
        require(self.grids["coarse"].nodes == self.grids["fine"].nodes,
                "both original grids must have the same exact radial nodes")
        self.order = int(prepared["order"])
        require(self.order == 8 and gate.side in (-1, 1),
                "the original quadrature order and signed cap side are required")
        self.side = int(gate.side)
        self.support = SimpleNamespace(left=Q(LEFT_EXACT), right=Q(RIGHT_EXACT))
        self.epsilon = float(Q(self.cfg["metric_proposal_epsilon_exact"]))
        self.target = float(Q(self.cfg["fixed_metric_budget_exact"]))
        require(self.epsilon == 1.e-8 and self.target == .26,
                "the original smoothed metric epsilon and current target must be retained")
        self.tolerances = _row_tolerances(self.cfg)
        self.pools = {label: _ids(prepared[label+"_pool"], self.grids[label])
                      for label in LABELS}
        cp = prepared.get("replay", {}).get("source_checkpoint")
        require(isinstance(cp, dict), "the literal accepted55 checkpoint is required")
        for label in LABELS:
            require(self.pools[label].tolist() == cp[label+"_pool"],
                    "the source55 pool IDs/order must not be expanded or reinitialized")
        self.pool_versions = {label: int(cp[label+"_pool_version"]) for label in LABELS}
        self.grid_records, self.base = {}, {}
        self._selected_tags, self._gradient_records = set(), {}
        self._last_scan, self._last_direction_cache = None, None
        self.scan_events, self.row_events = [], []

        hard_J, hard_values, hard_targets, hard_tags = [], [], [], []
        selected_gradients, selected_phi, selected_tags = [], [], []
        fixed_outside_phi = 0.
        domain_grids = {}
        for label, theta in (("coarse", self.theta), ("fine", self.fine_theta)):
            ledger.check("nine-geometry."+label+".entry")
            grid = self.grids[label]
            require(grid.nr == len(self.radial) and grid.nt == len(theta)
                    and _same_bytes(np.array([float(t) for t in grid.nodes]), self.radial),
                    "the exact original radial classification must bind the actual value grid")
            parts = grid.classify(self.pools[label], self.support)
            hard_mask = parts["variable"] & (parts["groups"] >= 2)
            soft_mask = parts["variable"] & (parts["groups"] < 2)
            hard_ids = self.pools[label][hard_mask].copy()
            soft_ids = self.pools[label][soft_mask].copy()
            require(len(hard_ids) > 0, "the original pool must contain variable hard rows")
            hard_ids.setflags(write=False)
            soft_ids.setflags(write=False)
            info = capture["grids"][label] = {
                "status": "ordinary-starting",
                "pool_rows": len(self.pools[label]),
                "variable_hard_rows": len(hard_ids),
                "variable_selected_metric_rows": len(soft_ids),
                "outside_selected_rows": int(np.count_nonzero(~parts["variable"])),
                "theta_array_sha256": array_digest(theta),
                "fine_theta_is_source55_array": label == "fine"}
            raw_cache = capture["_arrays"][label] = {"hard_ids":hard_ids}
            event = ledger.begin(
                "necessary_model_grid_values", grid=label, source_accepted_index=55,
                purpose="new-nine hard-model complete two-jet input",
                physical_state_sha256=SOURCE_PHYSICAL_SHA,
                old159_J_requested=False, fine_theta_regenerated=False)
            try:
                ordinary = dict(self.field.geometry(
                    self.center168, self.radial, theta, self.order,
                    jacobian=False, full_two_jet_jacobian=False))
                for key, value in (("radial", self.radial), ("theta", theta)):
                    if key in ordinary:
                        require(_same_bytes(_finite(ordinary[key]), value),
                                "the necessary ordinary changed "+key+" bytes")
                    ordinary[key] = value
                ordinary["state168"] = self.center168
                ordinary["source_accepted_index"] = SOURCE_INDEX
                raw_cache["ordinary"] = ordinary
                derived = row_values(
                    ordinary, np.asarray(ordinary["metric"]["a"]), self.side, self.cfg)
                ordinary["eta"] = np.asarray(derived["eta"])
                raw_rows = _finite(derived["rows"], (11, grid.nr, grid.nt),
                                   "complete original scalar values").copy()
                raw_cache["rows_with_original_hard_components"] = raw_rows
                bound = self.field.bind_ordinary(
                    self.center168, self.radial, theta, ordinary,
                    {"kind": "new-necessary-ordinary55-for-nine-derivative-input",
                     "grid": label, "source_accepted_index": SOURCE_INDEX,
                     "physical_state_sha256": SOURCE_PHYSICAL_SHA,
                     "source_binding": copy.deepcopy(self.source_binding),
                     "ordinary_value_ledger_ordinal": event["ordinal"],
                     "not_the_old55_UT_only_cache": True})
                raw_cache["bound"] = bound
                info.update(ordinary_bound_sha256=bound["binding_sha256"],
                            true_eta_maximum=float(np.max(ordinary["eta"])),
                            ordinary_two_jets_retained=True)
                ledger.end(event, ordinary_bound_sha256=bound["binding_sha256"],
                           true_eta_maximum=info["true_eta_maximum"],
                           point_count=grid.point_count, no_old159_J=True)
            except Exception as error:
                ledger.end(event, error)
                raise
            ledger.check("nine-geometry."+label+".after-ordinary")

            event = ledger.begin(
                "hard_J_grid_builds", grid=label, row_count=len(hard_ids),
                row_ids_sha256=array_digest(hard_ids),
                purpose="only original variable hard scalar rows, nine new columns",
                old159_columns_requested=0, soft_rows_requested=0)
            try:
                width_key = ("radial_Jacobian_batch_owned_rows" if label == "coarse"
                             else "fine_Jacobian_owned_radial_rows")
                J9, hard_diag, obs = new_nine_selected_rows(
                    self.field, self.center168, self.radial, theta, hard_ids, bound,
                    self.cfg, side=self.side, owned_width=int(self.cfg[width_key]),
                    wall=ledger.check, need_observables=False)
                J9 = _owned(J9, (len(hard_ids), 9), "new selected hard J9")
                require(obs is None, "no selected soft-observable derivatives may be repeated")
                raw_cache["hard_J9"], raw_cache["hard_ids"] = J9, hard_ids
                info["hard_J9"] = copy.deepcopy(hard_diag)
                ledger.end(event, J9_sha256=array_digest(J9),
                           diagnostics=copy.deepcopy(hard_diag), no_old159_J=True)
            except Exception as error:
                ledger.end(event, error)
                raise
            ledger.check("nine-geometry."+label+".after-hard-J9")

            event = ledger.begin(
                "metric9_grid_builds", grid=label, point_count=grid.point_count,
                new_column_count=9, purpose="complete baseline metric9, once",
                ordinary_values_reused=True, old159_columns_requested=0)
            try:
                metric, metric_diag = new_nine_metric_jets(
                    self.field, self.center168, self.radial, theta, bound,
                    owned_width=int(self.cfg[width_key]), wall=ledger.check)
                require(set(metric) == {"e", "f", "de", "df"},
                        "the complete metric9 contract must contain e/f/de/df only")
                e = _finite(metric["e"], (grid.nr, grid.nt), "metric9 base e").reshape(-1)
                f = _finite(metric["f"], (grid.nr, grid.nt), "metric9 base f").reshape(-1)
                de9 = _finite(metric["de"], (grid.nr, grid.nt, 9), "complete de9").reshape(-1, 9)
                df9 = _finite(metric["df"], (grid.nr, grid.nt, 9), "complete df9").reshape(-1, 9)
                variable_nodes = np.array(
                    [self.support.left < t < self.support.right for t in grid.nodes])
                outside_points = np.repeat(~variable_nodes, grid.nt)
                require(np.any(outside_points) and np.any(~outside_points),
                        "the exact support must have an interior and a fixed exterior")
                # These are input-domain contracts on the new derivative,
                # not a repeat of any old geometry/J scientific check.
                require(np.all(de9[outside_points] == 0.)
                        and np.all(df9[outside_points] == 0.),
                        "the new columns must be exactly inactive off their declared support")
                branch_phi = np.empty((2, grid.point_count))
                branch_gradients = np.empty((2, grid.point_count, 9))
                for group in (0, 1):
                    groups = np.full(grid.point_count, group, dtype=np.int64)
                    branch_phi[group] = phi(e, f, groups, self.epsilon)
                    ge, gf = phi_gradient(e, f, groups, self.epsilon)
                    branch_gradients[group] = ge[:, None]*de9+gf[:, None]*df9
                branch_phi = _owned(branch_phi, (2, grid.point_count), "complete baseline phi")
                branch_gradients = _owned(
                    branch_gradients, (2, grid.point_count, 9), "complete baseline gphi9")
                ordinary["e"], ordinary["f"] = metric["e"], metric["f"]
                raw_rows[:2] = self.target-branch_phi.reshape(2, grid.nr, grid.nt)
                raw_rows.setflags(write=False)
                raw_cache.update(metric9=metric, branch_phi=branch_phi,
                                 branch_gradients9=branch_gradients, rows=raw_rows)
                full = FullGridValues(
                    grid, raw_rows, ordinary["eta"], ordinary["height"]["b"],
                    self.tolerances, np.mean(ordinary["Xs"], axis=1))
                raw_cache["full"] = full
                info["metric9"] = copy.deepcopy(metric_diag)
                ledger.end(event,
                           e_sha256=array_digest(e), f_sha256=array_digest(f),
                           de9_sha256=array_digest(de9), df9_sha256=array_digest(df9),
                           branch_phi_sha256=array_digest(branch_phi),
                           branch_gradients9_sha256=array_digest(branch_gradients),
                           diagnostics=copy.deepcopy(metric_diag),
                           zero_derivative_outside_exact_support=True,
                           selected_soft_J_calls=0, old159_J_calls=0)
            except Exception as error:
                ledger.end(event, error)
                raise
            ledger.check("nine-geometry."+label+".after-metric9")

            hard_groups = hard_ids//grid.point_count
            values = _owned(raw_rows.reshape(-1)[hard_ids], (len(hard_ids),))
            tolerances = self.tolerances[hard_groups]
            require(np.all(values >= -tolerances),
                    "the accepted55 selected hard rows must pass their original tolerances")
            targets = _hard_targets(values, hard_groups, tolerances, self.cfg)
            # Exterior hard rows use their original tolerances, not the
            # interior proposal floors.  No exterior derivative is inferred
            # from a small floating-point gradient.
            outside_radial = ~variable_nodes
            margin = (raw_rows[2:, outside_radial, :]
                      + self.tolerances[2:, None, None])
            hloc = np.unravel_index(int(np.argmin(margin)), margin.shape)
            outside_ri = np.flatnonzero(outside_radial)
            worst_id = ((int(hloc[0])+2)*grid.point_count
                        +int(outside_ri[int(hloc[1])])*grid.nt+int(hloc[2]))
            outside_minimum = float(np.min(margin))
            require(outside_minimum >= 0.,
                    "an invariant exterior hard row fails its original tolerance")
            outside_phi = float(np.max(branch_phi[:, outside_points]))
            fixed_outside_phi = max(fixed_outside_phi, outside_phi)
            soft_groups, soft_points = soft_ids//grid.point_count, soft_ids % grid.point_count
            gradients = _owned(branch_gradients[soft_groups, soft_points], (len(soft_ids), 9))
            basephi = _owned(branch_phi[soft_groups, soft_points], (len(soft_ids),))
            htags = [grid.coordinate(int(value)) for value in hard_ids]
            stags = [grid.coordinate(int(value)) for value in soft_ids]
            hard_J.append(J9); hard_values.append(values); hard_targets.append(targets)
            hard_tags.extend(htags)
            selected_gradients.append(gradients); selected_phi.append(basephi)
            selected_tags.extend(stags)
            self._selected_tags.update((label, int(value)) for value in soft_ids)
            self.base[label] = {
                "e": e, "f": f, "de9": de9, "df9": df9,
                "branch_phi": branch_phi, "branch_gradients9": branch_gradients,
                "outside_points": outside_points,
                "variable_nodes": variable_nodes}
            self.grid_records[label] = {
                "grid": grid, "radial": self.radial, "theta": theta,
                "ordinary": ordinary, "bound": bound, "full": full,
                "pool_ids": self.pools[label], "ids": hard_ids, "J9": J9,
                "hard_ids": hard_ids, "hard_base_values": values,
                "hard_targets": targets, "hard_original_row_tags": htags,
                "selected_metric_ids": soft_ids,
                "selected_metric_gradients9_of_phi": gradients,
                "selected_metric_base_phi": basephi,
                "selected_metric_original_row_tags": stags,
                "metric9": metric,
                "hard_diagnostics": hard_diag, "metric9_diagnostics": metric_diag}
            domain_grids[label] = {
                "original_grid": copy.deepcopy(grid.definition),
                "grid_definition_sha256": grid.definition_sha256,
                "source_pool_version": self.pool_versions[label],
                "source_pool_rows": len(self.pools[label]),
                "source_pool_ids_sha256": array_digest(self.pools[label]),
                "variable_hard_rows": len(hard_ids),
                "variable_selected_metric_rows": len(soft_ids),
                "exterior_hard_original_tolerance_pass": True,
                "exterior_hard_minimum_original_tolerance_margin": outside_minimum,
                "exterior_hard_worst_original_row": grid.coordinate(worst_id),
                "fixed_outside_phi": outside_phi,
                "original_hard_targets_sha256": array_digest(targets),
                "hard_target_minimum": float(np.min(targets)),
                "zero_interior_J_rows_retained": int(np.sum(np.all(J9 == 0., axis=1))),
                "hard_J_only_used_for_variable_original_pool_rows": True,
                "selected_soft_gradients_are_slices_of_complete_metric9": True,
                "all_original_pool_rows_remain_classified": True}
            info.update(status="complete", domain=copy.deepcopy(domain_grids[label]))

        self.phi0 = self.complete_phi0 = max(
            self.target, *(float(np.max(self.base[label]["branch_phi"])) for label in LABELS))
        require(np.array_equal(self.grid_records["coarse"]["full"].b,
                               self.grid_records["fine"]["full"].b),
                "both complete grids must use the same current common height")
        self.domain_receipt = {
            "schema": POLICY+"-original-nine-domain",
            "source_accepted_index": SOURCE_INDEX,
            "support_exact": [LEFT_EXACT, RIGHT_EXACT],
            "classification_uses_exact_radial_nodes_not_gradient_size": True,
            "grids": domain_grids,
            "hard_target_rule": "value-fraction*(value+original_tolerance), then original floors",
            "fraction_to_boundary_exact": self.cfg["linear_fraction_to_boundary_exact"],
            "strip_floor_exact": self.cfg["strip_proposal_floor_exact"],
            "curvature_floor_exact": self.cfg["curvature_proposal_floor_exact"],
            "original_group_tolerances": self.tolerances.tolist(),
            "old159_empirical_defect_gamma_not_transferred_to_new_fiber": True,
            "constant_height_gate_unchanged_by_exact_zero_total_new_height_column": True,
            "actual_all14_gates_remain_the_separate_acceptance_test": True,
            "finite_model_does_not_certify_actual_geometry_or_reach": True}
        self.original_domain = {
            "hard_J9": _owned(np.vstack(hard_J), (sum(len(x) for x in hard_values), 9)),
            "hard_base_values": _owned(np.concatenate(hard_values)),
            "hard_targets": _owned(np.concatenate(hard_targets)),
            "hard_original_row_tags": hard_tags,
            "selected_metric_gradients9_of_phi": _owned(np.vstack(selected_gradients)),
            "selected_metric_base_phi": _owned(np.concatenate(selected_phi)),
            "selected_metric_original_row_tags": selected_tags,
            "fixed_outside_phi": float(fixed_outside_phi)}
        self.binding = {
            "schema": POLICY+"-geometry-metric9-input",
            "source_binding": copy.deepcopy(self.source_binding),
            "source_accepted_index": SOURCE_INDEX,
            "source_physical_state_sha256": SOURCE_PHYSICAL_SHA,
            "source_ordinary_evaluator_sha256": SOURCE_FIELD_SHA,
            "configuration_sha256": self.cfg_sha256,
            "new_field_definition_sha256": self.field.definition_sha256,
            "new_coordinate_definition_sha256": self.field.coordinate_definition_sha256,
            "new_physical_identity_sha256": digest(self.field.identity(self.center168)),
            "new_independent168_sha256": array_digest(self.center168),
            "lower172_sha256": array_digest(self.lower172),
            "upper172_sha256": array_digest(self.upper172),
            "target": self.target, "epsilon": self.epsilon,
            "support_exact": [LEFT_EXACT, RIGHT_EXACT],
            "new_coefficient_units": "literal alpha4,beta4,gamma; no hidden column normalization",
            "new9_box_exact": ["-1/4", "1/4"],
            "old159_are_fixed_not_reoptimized": True,
            "fine_theta_source": "the exact source55 accepted-cache array supplied by transfer",
            "grids": {
                label: {
                    "grid_definition_sha256": self.grids[label].definition_sha256,
                    "radial_sha256": array_digest(self.grid_records[label]["radial"]),
                    "theta_sha256": array_digest(self.grid_records[label]["theta"]),
                    "ordinary_bound_sha256": self.grid_records[label]["bound"]["binding_sha256"],
                    "hard_ids_sha256": array_digest(self.grid_records[label]["hard_ids"]),
                    "hard_J9_sha256": array_digest(self.grid_records[label]["J9"]),
                    "source_pool_sha256": array_digest(self.pools[label]),
                    "metric9_sha256": {
                        name: array_digest(value)
                        for name, value in self.grid_records[label]["metric9"].items()},
                    "branch_phi_sha256": array_digest(self.base[label]["branch_phi"]),
                    "branch_gradients9_sha256": array_digest(
                        self.base[label]["branch_gradients9"])}
                for label in LABELS},
            "hard_base_values_sha256": array_digest(self.original_domain["hard_base_values"]),
            "hard_targets_sha256": array_digest(self.original_domain["hard_targets"]),
            "hard_tags_sha256": digest(hard_tags),
            "selected_metric_tags_sha256": digest(selected_tags),
            "selected_metric_g9_sha256": array_digest(
                self.original_domain["selected_metric_gradients9_of_phi"]),
            "selected_metric_phi_sha256": array_digest(
                self.original_domain["selected_metric_base_phi"]),
            "complete_phi0": self.phi0,
            "fixed_outside_phi": float(fixed_outside_phi),
            "domain_receipt_sha256": digest(self.domain_receipt),
            "ordinary_grid_values": 2, "selected_hard_J9_grid_builds": 2,
            "complete_metric9_grid_builds": 2,
            "old159_J_and_selected_soft_J_builds": 0,
            "master_scan_is_baseline_linear_phi": True}
        self.binding_sha256 = digest(self.binding)
        self.source55 = SOURCE_INDEX
        ledger.check("nine-geometry.binding-complete")

    def model_input(self):
        """References to the one completed input; no geometry, J or full scan."""
        self.ledger.check("nine-geometry.model-input")
        return {
            "original_domain": self.original_domain,
            "complete_phi0": self.phi0, "target": self.target,
            "binding": copy.deepcopy(self.binding),
            "binding_sha256": self.binding_sha256,
            "center168": self.center168, "source55": SOURCE_INDEX,
            "domain_receipt": copy.deepcopy(self.domain_receipt)}

    def receipt(self):
        """Small JSON metadata, deliberately excluding ordinary/derivative arrays."""
        return {
            "schema": POLICY+"-geometry-receipt",
            "binding": copy.deepcopy(self.binding),
            "binding_sha256": self.binding_sha256,
            "source55": SOURCE_INDEX, "complete_phi0": self.phi0,
            "target": self.target, "epsilon": self.epsilon,
            "domain": copy.deepcopy(self.domain_receipt),
            "complete_grid_coverage": {label: self.grids[label].point_count for label in LABELS},
            "ordinary_cache_accessor": "grid_records[label]['ordinary']",
            "bound_cache_accessor": "grid_records[label]['bound']",
            "complete_metric9_accessor": "grid_records[label]['metric9']",
            "only_selected_hard_J9_and_complete_metric9_were_built": True,
            "actual_candidate_not_evaluated_by_this_helper": True}

    def _delta(self, delta9):
        self.ledger.check("nine-geometry.direction-input")
        return _owned(delta9, (9,), "actual new-nine coefficient displacement")

    def scan(self, delta9, *, phase="master"):
        """One complete pair scan of phi_i(0)+gphi_i(0).delta9, including target.

        This cache contraction calls no geometry/J/JVP and does not evaluate
        phi at perturbed e/f.  Repeated requests remain observed scan attempts,
        but exact same-direction cache hits do not repeat grid contraction.
        """
        delta = self._delta(delta9)
        event = self.ledger.begin(
            "full_separations", phase=str(phase),
            binding_sha256=self.binding_sha256,
            direction_sha256=array_digest(delta),
            oracle="complete-baseline-first-order-original-rows",
            geometry_calls=0, J_calls=0, JVP_calls=0)
        self.scan_events.append(event)
        started = time.monotonic()
        try:
            if self._last_scan is not None and _same_bytes(self._last_scan["direction"], delta):
                self.ledger.end(event, cache_hit=True,
                                coverage=copy.deepcopy(self._last_scan["coverage"]),
                                linear_maximum=self._last_scan["linear_maximum"])
                self.ledger.check("nine-geometry.scan-cache-hit")
                return self._last_scan
            branches, coverage = [], {}
            for label in LABELS:
                self.ledger.check("nine-geometry.scan."+label)
                grid, base = self.grids[label], self.base[label]
                slopes = np.einsum("gpj,j->gp", base["branch_gradients9"], delta)
                values = base["branch_phi"]+slopes
                _finite(values, (2, grid.point_count), "complete baseline-linear branch values")
                coverage[label] = grid.point_count
                for group in (0, 1):
                    point = int(np.argmax(values[group]))
                    flat = group*grid.point_count+point
                    branches.append({
                        "grid": label, "group": group, "point": point,
                        "flat_row_id": flat, "original_row": grid.coordinate(flat),
                        "base_phi": float(base["branch_phi"][group, point]),
                        "base_gap": float(base["branch_phi"][group, point]-self.target),
                        "directional_slope": float(slopes[group, point]),
                        "linear_branch_value": float(values[group, point])})
            maximum = max(self.target, *(row["linear_branch_value"] for row in branches))
            result = {
                "schema": POLICY+"-complete-first-order-scan",
                "binding_sha256": self.binding_sha256,
                "model_binding_sha256": self.binding_sha256,
                "direction": delta, "direction_sha256": array_digest(delta),
                "linear_maximum": float(maximum),
                "first_order_metric_maximum": float(maximum),
                "complete_linear_gain": float(self.phi0-maximum),
                "base_phi": self.phi0, "target": self.target,
                "branches": branches, "coverage": coverage,
                "scope": "all original grid points and both baseline spectral branches, plus target",
                "ordinal": event["ordinal"],
                "elapsed_seconds": float(time.monotonic()-started),
                "baseline_gradients_not_candidate_point_tangents": True,
                "nonlinear_affine_observable_phi_not_used_for_master": True,
                "actual_geometry_not_evaluated": True}
            self._last_scan = result
            self.ledger.end(event, cache_hit=False, coverage=copy.deepcopy(coverage),
                            branches=copy.deepcopy(branches), linear_maximum=float(maximum),
                            no_derivative_rebuild=True)
            self.ledger.check("nine-geometry.scan.complete")
            return result
        except Exception as error:
            if event.get("status") == "started":
                self.ledger.end(event, error)
            raise

    def attainer_gradient(self, label, flat_row_id, *, scan=None):
        """Materialize one already computed BASELINE metric gradient9.

        Only the first request for a new variable original tag debits
        new_metric_rows.  Selected tags and the invariant exterior are not
        new derivative calls.  No derivative is recomputed for any tag.
        """
        self.ledger.check("nine-geometry.attainer-entry")
        require(label in LABELS, "coarse or fine grid required")
        grid = self.grids[label]
        flat = int(grid.ids([flat_row_id])[0])
        group, point = divmod(flat, grid.point_count)
        require(group in (0, 1), "an original soft branch row is required")
        if scan is not None:
            require(scan["binding_sha256"] == self.binding_sha256
                    and any(item["grid"] == label and item["flat_row_id"] == flat
                            for item in scan["branches"]),
                    "a materialized cut must be an original attainer of this complete scan")
        key = (label, flat)
        if key in self._gradient_records:
            return copy.deepcopy(self._gradient_records[key])
        tag = grid.coordinate(flat)
        inside = self.support.left < Q(tag["t_exact"]) < self.support.right
        selected = key in self._selected_tags
        event = None
        if inside and not selected:
            event = self.ledger.begin(
                "new_metric_rows", original_row=copy.deepcopy(tag),
                binding_sha256=self.binding_sha256,
                source="slice of the once-built complete metric9",
                geometry_calls=0, J_calls=0, JVP_calls=0)
            self.row_events.append(event)
        try:
            gradient = _owned(self.base[label]["branch_gradients9"][group, point], (9,))
            if not inside:
                require(np.all(gradient == 0.),
                        "the invariant exterior cannot acquire a new derivative")
            result = {
                "schema": POLICY+"-baseline-original-row-gradient",
                "grid": label, "flat_row_id": flat, "original_row": tag,
                "gradient": gradient.tolist(), "gradient9": gradient.tolist(),
                "gradient_sha256": array_digest(gradient),
                "binding_sha256": self.binding_sha256,
                "base_phi": float(self.base[label]["branch_phi"][group, point]),
                "source": ("already selected baseline metric row" if selected else
                           "exact support-invariant exterior" if not inside else
                           "new original tag from complete metric9 baseline cache"),
                "new_original_tag_debit": bool(event is not None),
                "no_new_geometry_or_derivative_evaluation": True,
                "linearization_point": "accepted55 with all new9 coefficients zero",
                "not_a_candidate_point_tangent": True}
            self._gradient_records[key] = result
            if event is not None:
                self.ledger.end(event, gradient_sha256=result["gradient_sha256"],
                                base_phi=result["base_phi"])
            self.ledger.check("nine-geometry.attainer-complete")
            return copy.deepcopy(result)
        except Exception as error:
            if event is not None and event.get("status") == "started":
                self.ledger.end(event, error)
            raise

    def direction_cache(self, delta9):
        """Contract cached de9/df9 once for the separate scalar prediction.

        Returned e/f/de/df are one-dimensional, radial-major arrays.  This
        method has no scalar query or full_separations debit: it evaluates no
        scalar alpha and finds no grid maximum.  Its arithmetic and hashing
        still consume the same wall clock.  The scalar driver owns all
        scalar_sessions/scalar_queries counters and must use this exact cache.
        """
        delta = self._delta(delta9)
        if self._last_direction_cache is not None and _same_bytes(
                self._last_direction_cache["direction"], delta):
            return self._last_direction_cache
        arrays, hashes = {}, {}
        started = time.monotonic()
        for label in LABELS:
            self.ledger.check("nine-geometry.direction-cache."+label)
            base, grid = self.base[label], self.grids[label]
            de = _owned(np.einsum("pj,j->p", base["de9"], delta),
                        (grid.point_count,), "complete directional de")
            df = _owned(np.einsum("pj,j->p", base["df9"], delta),
                        (grid.point_count,), "complete directional df")
            arrays[label] = {"e": base["e"], "f": base["f"], "de": de, "df": df}
            hashes[label] = {name: array_digest(value) for name, value in arrays[label].items()}
        result = {
            "schema": POLICY+"-affine-observable-direction-cache",
            "grids": arrays, "direction": delta,
            "direction_sha256": array_digest(delta),
            "binding_sha256": self.binding_sha256,
            "model_binding_sha256": self.binding_sha256,
            "source_binding": copy.deepcopy(self.source_binding),
            "base_phi": self.phi0, "target": self.target, "epsilon": self.epsilon,
            "coverage": {label: self.grids[label].point_count for label in LABELS},
            "arrays_sha256": hashes,
            "elapsed_seconds": float(time.monotonic()-started),
            "only_e_f_de_df_returned_per_grid": True,
            "nonlinear_phi_alpha_queries_owned_by_scalar_driver": True,
            "master_linear_gain_is_not_a_scalar_or_actual_gain": True,
            "no_geometry_J_or_JVP_calls": True}
        self._last_direction_cache = result
        self.ledger.check("nine-geometry.direction-cache.complete")
        return result

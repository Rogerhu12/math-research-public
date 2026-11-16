#!/usr/bin/env python3
"""Current accepted56 full168 model input and complete first-order separation.

Import-only.  This module obtains two necessary complete current ordinary
inputs and builds the selected168 derivatives for every original pool row.
No old159 final Jacobian is reused and no new9 support filter is applied.

A separation evaluates phi_i(0) + Dphi_i(0)[delta168] on both complete grids.
Each new direction uses one current-frame metric JVP on each grid.  Its exact
e/f/de/df arrays are then retained for the separate scalar predictor, which
does not rebuild that direction.  No actual candidate is evaluated here.
All imports, input, calls, failures and output share the external ledger.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid, FullGridValues, array_digest
from frame_metric_budget_restoration_rows import row_values
from frame_metric_epigraph import geometry_values
from frame_metric_affine_spectral_model import phi, phi_gradient
from frame_complete_body_extension168 import CompleteBody168Field, POSITION_KEYS
from frame_complete_body_extension168_joint_selected import (
    current_168_selected_rows, bind_current_168_first_jets,
    current_168_metric_direction)

POLICY = "true56-full168-physical172-maximin-finite-exchange-v1"
LABELS = ("coarse", "fine")
SOURCE_INDEX = 56
SOURCE_PHYSICAL_SHA = "11c07425846f224c2d05997068b6442fa28a65383b5af5dce3eb2789da0593dd"
SOURCE_COORDINATE_SHA = "c69967fb9b864f3e95da411610b74d5477c58891352895b493aee6e482d960de"
SOURCE_FIELD_SHA = "81e6881cd1f36d87a865cd9cc8c51ee8480d2ac8278241d97fb19666486eba8d"
SOURCE_CFG_SHA = "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"


def require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def _finite(value, shape=None, name="array"):
    a = np.asarray(value, dtype=np.float64)
    require((shape is None or a.shape == tuple(shape)) and np.all(np.isfinite(a)),
            "finite "+name+" with the declared shape is required")
    return a


def _owned(value, shape=None, name="array"):
    a = _finite(value, shape, name).copy()
    a.setflags(write=False)
    return a


def _same_bytes(a, b):
    aa, bb = np.asarray(a), np.asarray(b)
    return aa.dtype == bb.dtype and aa.shape == bb.shape and aa.tobytes() == bb.tobytes()


def _ids(value, grid):
    raw = np.asarray(value)
    require(raw.ndim == 1 and raw.dtype.kind in "iu",
            "literal original integer pool IDs are required")
    a = grid.ids(raw).copy()
    a.setflags(write=False)
    return a


def _row_tolerances(cfg):
    answer = np.asarray(
        [cfg["metric_row_tolerance"]]*2 + [cfg["signed_height_tolerance"]]
        + [cfg["shape_constraint_tolerance"]]*3
        + [cfg["mirror_polynomial_tolerance"]]
        + [cfg["curvature_row_tolerance"]]*4, dtype=float)
    require(answer.shape == (11,) and np.all(np.isfinite(answer))
            and np.all(answer >= 0.), "the original eleven tolerances are required")
    answer.setflags(write=False)
    return answer


def _hard_targets(values, groups, tolerances, cfg):
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


def _array_payload(value):
    a = np.asarray(value)
    return {"shape": list(a.shape), "dtype": a.dtype.str,
            "array_sha256": array_digest(a), "values": a.tolist()}


def build_joint168_geometry(prepared, ledger, capture=None):
    """Build the one true56 input.  No pool expansion or actual trial.

    prepared supplies field168 (or problem=that field), a literal initial168,
    q168 or center168, cfg, gate.side, radial/theta/fine_theta, row_grids,
    order=8, lower172/upper172, coarse_pool/fine_pool, source_binding and
    replay.source_checkpoint with the actual56 pools and versions.

    If only the original DirectReference159 problem is supplied, its body168
    adapter may be constructed, but the actual nonzero168 vector is still
    mandatory.  There is no zero-extra embedding fallback.

    capture['_arrays'][label] retains references to completed ordinary,
    scalar values and derivative inputs/results for an explicit failure
    report.  full_payload() is the separate single success-input payload.
    Neither opaque capture nor a full ordinary cache is printed here.
    """
    require(isinstance(prepared, dict), "one restored accepted56 input is required")
    require(all(callable(getattr(ledger, name, None))
                for name in ("check", "elapsed", "begin", "end")),
            "the single externally owned scientific ledger is required")
    ledger.check("joint168-geometry.entry")
    sink = {} if capture is None else capture
    require(isinstance(sink, dict) and not sink, "an empty build capture is required")
    sink.update(schema=POLICY+"-input-build", status="started", grids={},
                _arrays={}, source_accepted_index=SOURCE_INDEX,
                old159_J_reuse_calls=0, actual_candidate_calls=0)
    answer = Joint168Geometry.__new__(Joint168Geometry)
    try:
        answer._build(prepared, ledger, sink)
        sink.update(status="complete", binding_sha256=answer.binding_sha256,
                    receipt=answer.receipt())
        ledger.check("joint168-geometry.complete")
        return answer
    except Exception as error:
        sink.update(status="raised",
                    error={"type": type(error).__name__, "message": str(error)},
                    scientific_seconds=ledger.elapsed())
        raise


class Joint168Geometry:
    """One immutable actual56/current168 baseline, selected J and directional caches."""

    def _build(self, prepared, ledger, capture):
        self.ledger, self.capture = ledger, capture
        self.cfg = copy.deepcopy(prepared["cfg"])
        self.cfg_sha256 = digest(self.cfg)
        field = prepared.get("field168")
        if field is None:
            problem = prepared["problem"]
            field = (problem if isinstance(problem, CompleteBody168Field)
                     else CompleteBody168Field(problem))
        require(isinstance(field, CompleteBody168Field),
                "the complete body168 field is required")
        states = [prepared[key] for key in ("initial168", "q168", "center168")
                  if key in prepared]
        require(bool(states), "the actual nonzero-new9 accepted56 vector is required")
        self.center168 = self.q168 = _owned(states[0], (168,), "accepted56 independent168")
        require(all(_same_bytes(np.asarray(value, dtype=float), self.center168)
                    for value in states[1:]),
                "all prepared names must identify the same accepted56 vector")
        self.field = self.field168 = field
        self.original_field = field.original_field
        field.validate_state(self.center168)
        require(digest(field.identity(self.center168)) == SOURCE_PHYSICAL_SHA
                and field.coordinate_definition_sha256 == SOURCE_COORDINATE_SHA
                and field.definition_sha256 == SOURCE_FIELD_SHA
                and self.cfg_sha256 == SOURCE_CFG_SHA,
                "accepted56, its complete field/reference and original cfg must be unchanged")
        require(np.any(self.center168[159:] != 0.),
                "this input is the actual56 nonzero-new9 field, not a zero-extra old point")
        binding = prepared.get("source_binding")
        require(isinstance(binding, dict)
                and binding.get("accepted_index") == SOURCE_INDEX
                and binding.get("independent168_array_sha256") == array_digest(self.center168),
                "explicit accepted56 source identity and exact independent vector are required")
        self.source_binding = copy.deepcopy(binding)
        self.lower172 = _owned(prepared["lower172"], (172,), "physical lower172")
        self.upper172 = _owned(prepared["upper172"], (172,), "physical upper172")
        require(np.all(self.lower172 < self.upper172),
                "all actual physical172 bounds must be strictly ordered")
        self.center_box = field.exact_full_box_decision(
            self.center168, self.lower172, self.upper172)
        require(self.center_box["exact_full_box_pass"],
                "accepted56 must satisfy its original exact172 coefficient box")
        self.physical_linear_map172x168 = np.zeros((172, 168), dtype=float)
        self.physical_linear_map172x168[:163, :159] = _finite(
            self.original_field.coordinates.M, (163, 159), "original physical163 map")
        self.physical_linear_map172x168[163:, 159:] = np.eye(9)
        self.physical_linear_map172x168.setflags(write=False)
        self.physical_map_source = {
            "schema": POLICY+"-physical172-linear-map",
            "old_exact_coordinate_definition":
                copy.deepcopy(self.original_field.coordinate_definition),
            "old_height_H_exact": [
                [str(value) for value in row]
                for row in self.original_field.coordinates.basis.H],
            "new9_block": "literal identity9",
            "float_matrix_is_for_the_finite_model":
                "exact physical coefficients and exact box decisions remain canonical",
            "norm": "h = 4*max(abs(M172x168 @ delta168)) <= 1",
            "old163_Gamma_not_used": True}
        prepared.update(field168=self.field, q168=self.center168,
                        center168=self.center168, initial168=self.center168,
                        lower172=self.lower172, upper172=self.upper172)

        self.radial = _owned(prepared["radial"], name="original radial grid")
        self.theta = _owned(prepared["theta"], name="original coarse theta")
        require("fine_theta" in prepared,
                "the exact accepted56 fine-theta binary64 array must be supplied")
        self.fine_theta = _owned(prepared["fine_theta"], name="source56 fine theta")
        require(self.radial.ndim == self.theta.ndim == self.fine_theta.ndim == 1
                and len(self.fine_theta) == 2*len(self.theta),
                "the complete original coarse and fine grids are required")
        self.grids = prepared["row_grids"]
        require(isinstance(self.grids, dict) and set(self.grids) == set(LABELS)
                and all(isinstance(self.grids[label], RationalRowGrid)
                        and self.grids[label].label == label for label in LABELS)
                and self.grids["coarse"].nodes == self.grids["fine"].nodes,
                "both original RationalRowGrid identities are required")
        gate = prepared["gate"]
        self.side = int(gate.side)
        self.order = int(prepared["order"])
        require(self.side in (-1, 1) and self.order == 8,
                "the original side and ordinary query order are required")
        self.epsilon = float(Q(self.cfg["metric_proposal_epsilon_exact"]))
        self.target = float(Q(self.cfg["fixed_metric_budget_exact"]))
        require(self.epsilon == 1.e-8 and self.target == .26,
                "the original spectral epsilon and target are retained")
        self.tolerances = _row_tolerances(self.cfg)
        self.pools = {label: _ids(prepared[label+"_pool"], self.grids[label])
                      for label in LABELS}
        cp = prepared.get("replay", {}).get("source_checkpoint")
        require(isinstance(cp, dict), "the actual56 pool checkpoint is required")
        for label in LABELS:
            require(self.pools[label].tolist() == cp[label+"_pool"],
                    "the source56 pool IDs/order must not be expanded or reinitialized")
        self.pool_versions = {label: int(cp[label+"_pool_version"]) for label in LABELS}
        self.input_record_original_stdout_receipt = copy.deepcopy(
            prepared.get("input_record_original_stdout_receipt"))
        self.grid_records, self.base = {}, {}
        self._selected_lookup, self._gradient_records = {}, {}
        self._last_scan, self._last_direction_cache = None, None
        self._scan_cache, self._direction_caches = {}, {}
        self.scan_events, self.row_events = [], []
        self.ordinary_input_receipts = {}
        hard_J, hard_values, hard_targets, hard_tags = [], [], [], []
        soft_gradients, soft_values, soft_tags = [], [], []
        domain_grids = {}

        for label, theta in (("coarse", self.theta), ("fine", self.fine_theta)):
            ledger.check("joint168-geometry."+label+".entry")
            grid = self.grids[label]
            require(grid.nr == len(self.radial) and grid.nt == len(theta)
                    and _same_bytes(np.asarray([float(t) for t in grid.nodes]), self.radial),
                    "the original rational row grid must bind the actual full value grid")
            ids = self.pools[label]
            groups = ids//grid.point_count
            hard_positions = np.flatnonzero(groups >= 2)
            soft_positions = np.flatnonzero(groups < 2)
            hard_ids, soft_ids = ids[hard_positions], ids[soft_positions]
            require(len(hard_ids) > 0 and len(soft_ids) > 0,
                    "both original hard and metric pool rows are required")
            info = capture["grids"][label] = {
                "stage": "ordinary-starting", "pool_rows": len(ids),
                "hard_rows": len(hard_ids), "metric_rows": len(soft_ids),
                "no_support_filter": True, "theta_sha256": array_digest(theta)}
            raw = capture["_arrays"][label] = {"all_pool_ids": ids}
            event = ledger.begin(
                "necessary_model_grid_values", grid=label,
                source_accepted_index=SOURCE_INDEX,
                purpose="current56 complete two-jet derivative input",
                physical_state_sha256=SOURCE_PHYSICAL_SHA,
                old159_J_reused=False, fine_theta_regenerated=False)
            try:
                ordinary = dict(field.geometry(
                    self.center168, self.radial, theta, self.order,
                    jacobian=False, full_two_jet_jacobian=False))
                raw["ordinary"] = ordinary
                for name, value in (("radial", self.radial), ("theta", theta)):
                    if name in ordinary:
                        require(_same_bytes(np.asarray(ordinary[name], dtype=float), value),
                                "the current ordinary changed "+name+" bytes")
                    ordinary[name] = value
                ordinary["state168"] = self.center168
                ordinary["source_accepted_index"] = SOURCE_INDEX
                ordinary_receipt = {
                    "kind": "new-necessary-complete-current56-ordinary",
                    "grid": label, "source_accepted_index": SOURCE_INDEX,
                    "physical_state_sha256": SOURCE_PHYSICAL_SHA,
                    "source_binding": copy.deepcopy(self.source_binding),
                    "ordinary_value_ledger_ordinal": event["ordinal"],
                    "not_the_previous_UT_only_cache": True,
                    "ordinary_geometry_called_in_this_build": True}
                self.ordinary_input_receipts[label] = copy.deepcopy(ordinary_receipt)
                ledger.check("joint168-geometry."+label+".before-derived-values")
                derived = row_values(
                    ordinary, np.asarray(ordinary["metric"]["a"])[:, None],
                    self.side, self.cfg)
                gv = geometry_values(ordinary)
                ordinary["e"], ordinary["f"], ordinary["eta"] = gv["e"], gv["f"], gv["eta"]
                e = _finite(gv["e"], (grid.nr, grid.nt), "current e").reshape(-1)
                f = _finite(gv["f"], (grid.nr, grid.nt), "current f").reshape(-1)
                branch_phi = np.empty((2, grid.point_count))
                branch_ge, branch_gf = np.empty_like(branch_phi), np.empty_like(branch_phi)
                for group in (0, 1):
                    gg = np.full(grid.point_count, group, dtype=np.int64)
                    branch_phi[group] = phi(e, f, gg, self.epsilon)
                    branch_ge[group], branch_gf[group] = phi_gradient(e, f, gg, self.epsilon)
                branch_phi = _owned(branch_phi, name="complete current phi")
                branch_ge, branch_gf = _owned(branch_ge), _owned(branch_gf)
                rows = _owned(derived["rows"], (11, grid.nr, grid.nt),
                              "original complete scalar rows").copy()
                rows[:2] = self.target-branch_phi.reshape(2, grid.nr, grid.nt)
                rows.setflags(write=False)
                ordinary_bound = field.bind_ordinary(
                    self.center168, self.radial, theta, ordinary, ordinary_receipt)
                first_bound = bind_current_168_first_jets(
                    field, self.center168, self.radial, theta, ordinary,
                    ordinary_receipt, wall=ledger.check)
                # One current ordinary is the baseline for all scalar rows,
                # selected observables, full first-order scans and scalar caches.
                full = FullGridValues(
                    grid, rows, gv["eta"], ordinary["height"]["b"],
                    self.tolerances, np.mean(ordinary["Xs"], axis=1))
                raw.update(rows=rows, full=full, bound=ordinary_bound,
                           first_jet_bound=first_bound,
                           branch_phi=branch_phi, branch_ge=branch_ge, branch_gf=branch_gf)
                info.update(
                    stage="ordinary-complete",
                    ordinary_receipt=copy.deepcopy(ordinary_receipt),
                    ordinary_bound_sha256=ordinary_bound["binding_sha256"],
                    first_jet_bound_sha256=first_bound["binding_sha256"],
                    true_eta_maximum=float(np.max(gv["eta"])))
                ledger.end(
                    event, ordinary_bound_sha256=ordinary_bound["binding_sha256"],
                    first_jet_bound_sha256=first_bound["binding_sha256"],
                    true_eta_maximum=info["true_eta_maximum"],
                    point_count=grid.point_count)
            except Exception as error:
                if event.get("status") == "started":
                    ledger.end(event, error)
                raise

            ledger.check("joint168-geometry."+label+".before-selected-J")
            event = ledger.begin(
                "selected_J_grid_builds", grid=label, row_count=len(ids),
                row_ids_sha256=array_digest(ids),
                purpose="all original hard and soft pool rows at the current168 field",
                support_filter=False, old_final159_J_reuse=False)
            try:
                width_key = ("radial_Jacobian_batch_owned_rows" if label == "coarse"
                             else "fine_Jacobian_owned_radial_rows")
                width = int(self.cfg[width_key])
                J, diag, obs = current_168_selected_rows(
                    field, self.center168, self.radial, theta, ids,
                    ordinary_bound, self.cfg, side=self.side, owned_width=width,
                    wall=ledger.check, need_observables=True)
                J = _finite(J, (len(ids), 168), "complete selected J168")
                require(isinstance(obs, dict)
                        and np.array_equal(obs["row_positions"], soft_positions)
                        and np.array_equal(obs["row_ids"], soft_ids)
                        and np.array_equal(obs["groups"], groups[soft_positions]),
                        "selected observables must preserve the original metric row order")
                soft_groups = soft_ids//grid.point_count
                soft_points = soft_ids % grid.point_count
                require(_same_bytes(obs["e"], e[soft_points])
                        and _same_bytes(obs["f"], f[soft_points]),
                        "selected observables must use the literal current ordinary baseline")
                de = _finite(obs["de"], (len(soft_ids), 168), "selected de168")
                df = _finite(obs["df"], (len(soft_ids), 168), "selected df168")
                gradients = _owned(
                    branch_ge[soft_groups, soft_points, None]*de
                    + branch_gf[soft_groups, soft_points, None]*df,
                    (len(soft_ids), 168), "selected baseline metric gradients168")
                selected_phi = _owned(branch_phi[soft_groups, soft_points])
                Jhard = _owned(J[hard_positions], (len(hard_ids), 168), "hard J168")
                raw.update(selected_J168=J, selected_observables=obs,
                           hard_J168=Jhard, soft_gradient168=gradients)
                info["selected_J168"] = copy.deepcopy(diag)
                ledger.end(event, J168_sha256=array_digest(J),
                           hard_J168_sha256=array_digest(Jhard),
                           soft_gradient168_sha256=array_digest(gradients),
                           diagnostics=copy.deepcopy(diag))
            except Exception as error:
                if event.get("status") == "started":
                    ledger.end(event, error)
                raise

            hard_groups = hard_ids//grid.point_count
            values = _owned(rows.reshape(-1)[hard_ids], (len(hard_ids),))
            htols = self.tolerances[hard_groups]
            require(np.all(values >= -htols),
                    "accepted56 selected hard rows must retain their original tolerances")
            targets = _hard_targets(values, hard_groups, htols, self.cfg)
            htags = [grid.coordinate(int(value)) for value in hard_ids]
            stags = [grid.coordinate(int(value)) for value in soft_ids]
            hard_J.append(Jhard); hard_values.append(values); hard_targets.append(targets)
            hard_tags.extend(htags)
            soft_gradients.append(gradients); soft_values.append(selected_phi); soft_tags.extend(stags)
            for j, value in enumerate(soft_ids):
                self._selected_lookup[(label, int(value))] = (gradients[j], float(selected_phi[j]))
            self.base[label] = {
                "e": first_bound["data"]["e"].reshape(-1),
                "f": first_bound["data"]["f"].reshape(-1),
                "branch_phi": branch_phi, "branch_ge": branch_ge, "branch_gf": branch_gf}
            self.grid_records[label] = {
                "grid": grid, "radial": self.radial, "theta": theta,
                "ordinary": ordinary, "bound": ordinary_bound, "first_jet_bound": first_bound,
                "full": full, "pool_ids": ids, "ids": ids, "J168": J,
                "hard_ids": hard_ids, "hard_J168": Jhard,
                "hard_base_values": values, "hard_targets": targets,
                "hard_original_row_tags": htags,
                "selected_metric_ids": soft_ids,
                "selected_metric_gradients168_of_phi": gradients,
                "selected_metric_base_phi": selected_phi,
                "selected_metric_original_row_tags": stags,
                "selected_observables": obs, "selected_diagnostics": diag,
                "owned_width": width}
            domain_grids[label] = {
                "original_grid": copy.deepcopy(grid.definition),
                "grid_definition_sha256": grid.definition_sha256,
                "source_pool_version": self.pool_versions[label],
                "source_pool_rows": len(ids), "source_pool_ids_sha256": array_digest(ids),
                "all_original_pool_rows_included": True, "support_filter": False,
                "hard_rows": len(hard_ids), "selected_metric_rows": len(soft_ids),
                "hard_targets_sha256": array_digest(targets),
                "hard_target_minimum": float(np.min(targets)),
                "literal_zero_hard_J_rows_retained": int(np.sum(np.all(Jhard == 0., axis=1))),
                "selected_soft_current168_observables_not_old_J": True,
                "fixed_outside_phi": 0.,
                "no_common_outside_invariance_was_assumed": True}
            info.update(stage="complete", domain=copy.deepcopy(domain_grids[label]))
            ledger.check("joint168-geometry."+label+".complete")

        self.complete_phi0 = self.phi0 = max(
            self.target, *(float(np.max(self.base[label]["branch_phi"])) for label in LABELS))
        require(_same_bytes(self.grid_records["coarse"]["full"].b,
                            self.grid_records["fine"]["full"].b),
                "both current grids must use the same common height")
        self.domain_receipt = {
            "schema": POLICY+"-original-full168-domain", "source_accepted_index": SOURCE_INDEX,
            "grids": domain_grids, "support_filter": False,
            "hard_target_rule": "value-fraction*(value+original_tolerance), then original floors",
            "fraction_to_boundary_exact": self.cfg["linear_fraction_to_boundary_exact"],
            "strip_floor_exact": self.cfg["strip_proposal_floor_exact"],
            "curvature_floor_exact": self.cfg["curvature_proposal_floor_exact"],
            "original_group_tolerances": self.tolerances.tolist(),
            "literal_zero_rows_are_retained_for_exact_finite_model_handling": True,
            "not_an_old159_plus_new9_final_J_splice": True,
            "actual_all14_gates_and_exact172_box_remain_separate": True,
            "finite_model_is_not_an_actual_geometry_or_reach_certificate": True}
        self.original_domain = {
            "hard_J168": _owned(np.vstack(hard_J)),
            "hard_base_values": _owned(np.concatenate(hard_values)),
            "hard_targets": _owned(np.concatenate(hard_targets)),
            "hard_original_row_tags": hard_tags,
            "selected_metric_gradients168_of_phi": _owned(np.vstack(soft_gradients)),
            "selected_metric_base_phi": _owned(np.concatenate(soft_values)),
            "selected_metric_original_row_tags": soft_tags,
            "fixed_outside_phi": 0.}
        self.binding = {
            "schema": POLICY+"-geometry-input",
            "source_binding": copy.deepcopy(self.source_binding),
            "source_accepted_index": SOURCE_INDEX,
            "source_physical_state_sha256": SOURCE_PHYSICAL_SHA,
            "source_field_definition_sha256": SOURCE_FIELD_SHA,
            "source_coordinate_definition_sha256": SOURCE_COORDINATE_SHA,
            "configuration_sha256": self.cfg_sha256,
            "current_independent168_sha256": array_digest(self.center168),
            "lower172_sha256": array_digest(self.lower172),
            "upper172_sha256": array_digest(self.upper172),
            "physical_linear_map172x168_sha256": array_digest(self.physical_linear_map172x168),
            "physical_map_source_sha256": digest(self.physical_map_source),
            "target": self.target, "epsilon": self.epsilon,
            "fine_theta_source": "literal accepted56 cache array supplied by transfer",
            "all168_columns_evaluated_at_the_current_nonzero_new9_frame": True,
            "support_filter": False, "old_final159_J_reuse_calls": 0,
            "grids": {
                label: {
                    "grid_definition_sha256": self.grids[label].definition_sha256,
                    "radial_sha256": array_digest(self.radial),
                    "theta_sha256": array_digest(self.grid_records[label]["theta"]),
                    "ordinary_bound_sha256": self.grid_records[label]["bound"]["binding_sha256"],
                    "first_jet_bound_sha256": self.grid_records[label]["first_jet_bound"]["binding_sha256"],
                    "source_pool_sha256": array_digest(self.pools[label]),
                    "selected_J168_sha256": array_digest(self.grid_records[label]["J168"]),
                    "baseline_e_sha256": array_digest(self.base[label]["e"]),
                    "baseline_f_sha256": array_digest(self.base[label]["f"]),
                    "branch_phi_sha256": array_digest(self.base[label]["branch_phi"])}
                for label in LABELS},
            "hard_J168_sha256": array_digest(self.original_domain["hard_J168"]),
            "hard_base_values_sha256": array_digest(self.original_domain["hard_base_values"]),
            "hard_targets_sha256": array_digest(self.original_domain["hard_targets"]),
            "hard_tags_sha256": digest(hard_tags),
            "selected_metric_tags_sha256": digest(soft_tags),
            "selected_metric_g168_sha256": array_digest(
                self.original_domain["selected_metric_gradients168_of_phi"]),
            "selected_metric_phi_sha256": array_digest(
                self.original_domain["selected_metric_base_phi"]),
            "complete_phi0": self.phi0,
            "fixed_outside_phi": 0.,
            "domain_receipt_sha256": digest(self.domain_receipt),
            "necessary_current_ordinary_grid_values": 2,
            "selected_current168_grid_builds": 2,
            "complete_metric168_parameter_tensor_builds": 0,
            "ordinary_input_receipts": copy.deepcopy(self.ordinary_input_receipts),
            "master_scan_uses_two_directional_first_jets_per_new_direction": True}
        self.binding_sha256 = digest(self.binding)
        self.source56 = SOURCE_INDEX
        capture["_arrays"]["original_domain"] = self.original_domain
        capture["_arrays"]["physical_linear_map172x168"] = self.physical_linear_map172x168
        ledger.check("joint168-geometry.binding-complete")

    def model_input(self):
        """One shared numpy input; no geometry, derivative or full scan."""
        self.ledger.check("joint168-geometry.model-input")
        result = {
            "original_domain": self.original_domain,
            "complete_phi0": self.phi0, "target": self.target,
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "center168": self.center168, "source56": SOURCE_INDEX,
            "lower172": self.lower172, "upper172": self.upper172,
            "physical_linear_map172x168": self.physical_linear_map172x168,
            "physical_linear_map_sha256": array_digest(self.physical_linear_map172x168),
            "physical_linear_map_exact_source": copy.deepcopy(self.physical_map_source),
            "domain_receipt": copy.deepcopy(self.domain_receipt)}
        if self.input_record_original_stdout_receipt is not None:
            result["input_record_original_stdout_receipt"] = copy.deepcopy(
                self.input_record_original_stdout_receipt)
        return result

    def full_payload(self, array_encoder=None):
        """Single JSON-safe success-input record, excluding ordinary/UT/raw-J duplicates.

        array_encoder is optional and takes exactly one numpy array.  The
        default emits shape, dtype, array_sha256 and literal binary64 values.
        Serialization still belongs to this same external scientific clock.
        """
        self.ledger.check("joint168-geometry.input-payload")
        encode = _array_payload if array_encoder is None else array_encoder
        require(callable(encode), "an array encoder is required")
        domain = {
            key: (encode(value) if isinstance(value, np.ndarray) else copy.deepcopy(value))
            for key, value in self.original_domain.items()}
        result = {
            "schema": POLICY+"-complete-input",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "source56": SOURCE_INDEX, "complete_phi0": self.phi0, "target": self.target,
            "epsilon": self.epsilon, "original_domain": domain,
            "center168": encode(self.center168),
            "lower172": encode(self.lower172), "upper172": encode(self.upper172),
            "physical_linear_map172x168": encode(self.physical_linear_map172x168),
            "physical_linear_map_exact_source": copy.deepcopy(self.physical_map_source),
            "domain_receipt": copy.deepcopy(self.domain_receipt),
            "source_pools": {
                label: {"ids": self.pools[label].tolist(), "version": self.pool_versions[label]}
                for label in LABELS},
            "ordinary_and_raw_selected_J_are_not_duplicated_in_this_payload": True}
        if self.input_record_original_stdout_receipt is not None:
            result["input_record_original_stdout_receipt"] = copy.deepcopy(
                self.input_record_original_stdout_receipt)
        self.ledger.check("joint168-geometry.input-payload-complete")
        return result

    def receipt(self):
        return {
            "schema": POLICY+"-geometry-receipt",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "source56": SOURCE_INDEX, "complete_phi0": self.phi0,
            "target": self.target, "epsilon": self.epsilon,
            "domain": copy.deepcopy(self.domain_receipt),
            "coverage": {label: self.grids[label].point_count for label in LABELS},
            "ordinary_cache_accessor": "grid_records[label]['ordinary']",
            "bound_cache_accessor": "grid_records[label]['bound']",
            "first_jet_cache_accessor": "grid_records[label]['first_jet_bound']",
            "ordinary_input_receipts": copy.deepcopy(self.ordinary_input_receipts),
            "selected_current168_J_built_for_all_original_pool_rows": True,
            "no_support_filter": True,
            "actual_candidate_not_evaluated_by_this_helper": True}

    def _delta(self, delta168):
        self.ledger.check("joint168-geometry.direction-input")
        return _owned(delta168, (168,), "actual independent168 displacement")

    def scan(self, delta168, phase="master"):
        """Complete baseline-linear phi separation, with two current-frame JVPs.

        Same-direction cache hits retain a scan-attempt debit but repeat no
        JVP.  A successful new scan retains its two complete directional
        e/f/de/df arrays for direction_cache(); no candidate ordinary is called.
        """
        delta = self._delta(delta168)
        event = self.ledger.begin(
            "full_separations", phase=str(phase),
            binding_sha256=self.binding_sha256, direction_sha256=array_digest(delta),
            oracle="complete-current168-baseline-first-order-original-rows",
            geometry_calls=0, directional_metric_grids_at_most=2)
        self.scan_events.append(event)
        started = time.monotonic()
        try:
            direction_key = array_digest(delta)
            cached_scan = self._scan_cache.get(direction_key)
            if cached_scan is not None:
                require(_same_bytes(cached_scan["direction"], delta),
                        "a direction hash collision cannot substitute a different vector")
                self._last_scan = cached_scan
                self._last_direction_cache = self._direction_caches[direction_key]
                self.ledger.end(event, cache_hit=True,
                                coverage=copy.deepcopy(cached_scan["coverage"]),
                                linear_maximum=cached_scan["linear_maximum"],
                                directional_metric_grid_calls=0)
                self.ledger.check("joint168-geometry.scan-cache-hit")
                return cached_scan
            branches, coverage, cache_arrays, cache_hashes, jvp_diags = [], {}, {}, {}, {}
            current_capture = self.capture.setdefault("_direction_arrays", {})
            current_capture.clear()
            for label in LABELS:
                self.ledger.check("joint168-geometry.scan."+label)
                rec, grid, base = self.grid_records[label], self.grids[label], self.base[label]
                arrays, diag = current_168_metric_direction(
                    self.field, self.center168, delta, self.radial, rec["theta"],
                    rec["first_jet_bound"], owned_width=rec["owned_width"],
                    wall=self.ledger.check)
                require(set(arrays) == {"e", "f", "de", "df"},
                        "the complete direction cache has exactly e/f/de/df")
                entry = {
                    name: _finite(value, (grid.nr, grid.nt), "direction/"+name).reshape(-1)
                    for name, value in arrays.items()}
                require(_same_bytes(entry["e"], base["e"])
                        and _same_bytes(entry["f"], base["f"]),
                        "a directional query cannot replace its current baseline")
                for value in entry.values():
                    value.setflags(write=False)
                current_capture[label] = entry
                cache_arrays[label] = entry
                cache_hashes[label] = {name: array_digest(value) for name, value in entry.items()}
                jvp_diags[label] = copy.deepcopy(diag)
                slopes = base["branch_ge"]*entry["de"][None, :] + base["branch_gf"]*entry["df"][None, :]
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
            elapsed = float(time.monotonic()-started)
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
                "scope": "all original points and both baseline spectral branches, plus target",
                "ordinal": event["ordinal"], "elapsed_seconds": elapsed,
                "directional_metric_grid_calls": 2,
                "directional_diagnostics": jvp_diags,
                "baseline_gradients_not_candidate_point_tangents": True,
                "nonlinear_affine_observable_phi_not_used_for_master": True,
                "actual_geometry_not_evaluated": True}
            self._last_direction_cache = {
                "schema": POLICY+"-affine-observable-direction-cache",
                "grids": cache_arrays, "direction": delta,
                "direction_sha256": array_digest(delta),
                "binding_sha256": self.binding_sha256,
                "model_binding_sha256": self.binding_sha256,
                "source_binding": copy.deepcopy(self.source_binding),
                "base_phi": self.phi0, "target": self.target, "epsilon": self.epsilon,
                "coverage": copy.deepcopy(coverage), "arrays_sha256": cache_hashes,
                "origin_scan_ordinal": event["ordinal"],
                "origin_scan_directional_grid_calls": 2,
                "only_e_f_de_df_returned_per_grid": True,
                "nonlinear_phi_alpha_queries_owned_by_scalar_driver": True,
                "master_linear_gain_is_not_a_scalar_or_actual_gain": True,
                "no_additional_geometry_J_or_JVP_calls_on_cache_access": True}
            self._last_scan = result
            self._scan_cache[direction_key] = result
            self._direction_caches[direction_key] = self._last_direction_cache
            self.ledger.end(
                event, cache_hit=False, coverage=copy.deepcopy(coverage),
                branches=copy.deepcopy(branches), linear_maximum=float(maximum),
                directional_metric_grid_calls=2, cache_array_sha256=copy.deepcopy(cache_hashes))
            self.ledger.check("joint168-geometry.scan.complete")
            return result
        except Exception as error:
            if event.get("status") == "started":
                self.ledger.end(event, error)
            raise

    def attainer_gradient(self, label, flat_row_id, *, scan=None):
        """Materialize one original metric-row gradient at the same true56 point.

        A selected pool tag uses its already built gradient.  A new tag debits
        new_metric_rows and calls the current selected168 adapter for that
        single row.  Repeated requests return the bound baseline cache.
        There is no assumed invariant exterior and no candidate-point tangent.
        """
        self.ledger.check("joint168-geometry.attainer-entry")
        require(label in LABELS, "coarse or fine grid required")
        grid = self.grids[label]
        flat = int(grid.ids([flat_row_id])[0])
        group, point = divmod(flat, grid.point_count)
        require(group in (0, 1), "an original metric branch row is required")
        if scan is not None:
            require(scan["binding_sha256"] == self.binding_sha256
                    and any(row["grid"] == label and row["flat_row_id"] == flat
                            for row in scan["branches"]),
                    "the new original tag must be an attainer of this input's complete scan")
        key = (label, flat)
        if key in self._gradient_records:
            return copy.deepcopy(self._gradient_records[key])
        tag = grid.coordinate(flat)
        event = None
        selected = key in self._selected_lookup
        if selected:
            gradient, basephi = self._selected_lookup[key]
            diagnostic = None
        else:
            event = self.ledger.begin(
                "new_metric_rows", original_row=copy.deepcopy(tag),
                binding_sha256=self.binding_sha256,
                source="new original baseline tag, complete-current168 selected derivative",
                geometry_calls=0, selected_row_count=1)
            self.row_events.append(event)
        try:
            if not selected:
                rec = self.grid_records[label]
                J, diagnostic, obs = current_168_selected_rows(
                    self.field, self.center168, self.radial, rec["theta"], [flat],
                    rec["bound"], self.cfg, side=self.side,
                    owned_width=rec["owned_width"], wall=self.ledger.check,
                    need_observables=True)
                require(isinstance(obs, dict) and obs["row_ids"].tolist() == [flat]
                        and obs["row_positions"].tolist() == [0]
                        and obs["groups"].tolist() == [group],
                        "the new selected row must retain its full original identity")
                base = self.base[label]
                require(_same_bytes(obs["e"], base["e"][point:point+1])
                        and _same_bytes(obs["f"], base["f"][point:point+1]),
                        "new metric-row observables cannot replace the baseline")
                gradient = _owned(
                    base["branch_ge"][group, point]*obs["de"][0]
                    + base["branch_gf"][group, point]*obs["df"][0], (168,),
                    "new baseline metric gradient168")
                basephi = float(base["branch_phi"][group, point])
            else:
                gradient = _owned(gradient, (168,), "already selected metric gradient168")
            result = {
                "schema": POLICY+"-baseline-original-row-gradient",
                "grid": label, "flat_row_id": flat, "original_row": tag,
                "gradient": gradient, "gradient168": gradient,
                "gradient_sha256": array_digest(gradient),
                "binding_sha256": self.binding_sha256, "base_phi": float(basephi),
                "source": ("already selected baseline metric row" if selected else
                           "new original tag evaluated at the same current168 baseline"),
                "new_original_tag_debit": not selected,
                "selected_diagnostics": copy.deepcopy(diagnostic),
                "linearization_point": "actual accepted56, including its nonzero new9",
                "not_a_candidate_point_tangent": True,
                "no_actual_geometry_evaluation": True}
            self._gradient_records[key] = result
            if event is not None:
                self.ledger.end(event, gradient_sha256=result["gradient_sha256"],
                                base_phi=result["base_phi"],
                                selected_diagnostics=copy.deepcopy(diagnostic))
            self.ledger.check("joint168-geometry.attainer-complete")
            return copy.deepcopy(result)
        except Exception as error:
            if event is not None and event.get("status") == "started":
                self.ledger.end(event, error)
            raise

    def direction_cache(self, delta168):
        """Return only a successful scan's identical direction, with zero new JVPs.

        The caller must first scan this exact binary64 direction.  All at
        most eight successful directional caches are retained, so choosing an
        earlier best direction does not repeat its JVP.  A different direction
        requires its own authorized full_separations debit through scan();
        this accessor never hides a new direction or a rescaling.
        """
        delta = self._delta(delta168)
        cached = self._direction_caches.get(array_digest(delta))
        require(cached is not None and _same_bytes(cached["direction"], delta),
                "an identical successful full scan is required before scalar cache access")
        self.ledger.check("joint168-geometry.direction-cache")
        return cached

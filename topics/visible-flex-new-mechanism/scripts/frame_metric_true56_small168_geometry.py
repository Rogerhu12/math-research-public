#!/usr/bin/env python3
"""Paid true56 input restoration for the new small physical168 domain.

Import-only.  The closed large-domain INPUT3 and MODEL supply every old
hard/soft derivative and their eight additional metric rows.  Accepted56
CACHE2 supplies the literal current U,T,e,f.  One fixed radial metric call
restores a,a_s; it does not call ordinary geometry or a height primitive.
Only missing coarse metric row 104448 and genuinely new future attainers
use the metric-only selected168 API.  All work and failures use the caller's
new 300-second ledger; the old task is not resumed.

The inherited complete scan is the original baseline first-order oracle.
The separate e/f/de/df direction cache serves the scalar predictor.  New
method metadata are explicit; old source records and their bindings remain
unchanged.  No large paid input matrix is serialized a second time.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid, array_digest
from frame_metric_affine_spectral_model import phi, phi_gradient
from frame_complete_body_extension168 import CompleteBody168Field
from frame_complete_body_extension168_joint_selected import bind_current_168_first_jets
from frame_complete_body_extension168_metric_selected import current_168_metric_selected_rows
from frame_metric_true56_joint168_geometry import (
    Joint168Geometry, LABELS, SOURCE_INDEX, SOURCE_PHYSICAL_SHA,
    SOURCE_COORDINATE_SHA, SOURCE_FIELD_SHA, SOURCE_CFG_SHA,
    POLICY as PAID_JOINT_POLICY, require, _finite, _owned, _same_bytes,
    _ids, _row_tolerances, _array_payload)
from frame_metric_true56_small168_scope import (
    POLICY, Joint168Ledger, MAXIMUM_H_EXACT, MAXIMUM_H)

MISSING_INITIAL_TAG = ("coarse", 104448)
PAID_ADDITIONAL_ROWS = 8
SOURCE_POOL_COUNTS = {"coarse": 4453, "fine": 4549}
CURRENT_POOL_COUNTS = {"coarse": 4454, "fine": 4549}
SOURCE_POOL_VERSIONS = {"coarse": 14, "fine": 14}
CURRENT_POOL_VERSIONS = {"coarse": 15, "fine": 14}


def _decode(payload, shape, name):
    """Decode a paid literal binary64 array, checking its original hash."""
    require(isinstance(payload, dict)
            and isinstance(payload.get("shape"), list)
            and isinstance(payload.get("values"), list)
            and isinstance(payload.get("array_sha256"), str),
            name+" must be an original array payload")
    require(payload["shape"] == list(shape)
            and payload.get("dtype") in ("float64", "<f8", "=f8"),
            name+" must retain its original binary64 shape/dtype")
    value = _owned(payload["values"], tuple(shape), name)
    require(array_digest(value) == payload["array_sha256"],
            name+" original array hash differs")
    return value


def _tag_key(tag, grids, *, metric=None):
    require(isinstance(tag, dict) and tag.get("grid") in LABELS,
            "an original grid-tag dictionary is required")
    raw = tag.get("flat_row_id")
    require(isinstance(raw, (int, np.integer))
            and not isinstance(raw, (bool, np.bool_)),
            "an original literal integer row ID is required")
    label, flat = tag["grid"], int(raw)
    original = grids[label].coordinate(int(grids[label].ids([flat])[0]))
    require(original == tag, "an original row tag changed")
    group = flat//grids[label].point_count
    if metric is not None:
        require((group < 2) == metric,
                "the original hard/metric row classification changed")
    return label, flat


def _metadata_array(value):
    a = np.asarray(value)
    return {"shape": list(a.shape), "dtype": a.dtype.str,
            "array_sha256": array_digest(a)}


def _new_row_payload(row, encode):
    out = {}
    for key, value in row.items():
        if key in ("gradient", "gradient168"):
            continue
        if key == "metric_observables":
            out[key] = {name: encode(a) for name, a in value.items()}
        else:
            out[key] = copy.deepcopy(value)
    out["gradient168"] = encode(row["gradient168"])
    return out


def partial_small168_payload(capture, array_encoder=None):
    """Retain completed new products on a failed build, without old J/UT."""
    encode = _array_payload if array_encoder is None else array_encoder
    require(isinstance(capture, dict) and callable(encode),
            "the actual build capture and an array encoder are required")
    result = {key: copy.deepcopy(value) for key, value in capture.items()
              if not key.startswith("_") and key != "completed_new_metric_gradients"}
    result["schema"] = POLICY+"-partial-restored-input"
    result["new_metric_rows_completed"] = [
        _new_row_payload(row, encode)
        for row in capture.get("_new_metric_rows", [])]
    metric = capture.get("_arrays", {}).get("fixed_metric")
    if metric is not None:
        result["new_fixed_radial_metric"] = {
            name: encode(value) for name, value in metric.items()}
    observations = capture.get("_arrays", {}).get("last_new_metric_observables")
    if observations is not None:
        result["last_completed_metric_only_observables"] = {
            name: encode(value) for name, value in observations.items()}
    result["paid_large_INPUT3_and_CACHE2_not_duplicated"] = True
    result["no_ordinary_or_old_selected_J_rebuild"] = True
    return result


def restore_paid56_first_jets(field, state168, radial, thetas, accepted_cache,
                             source_receipt, ledger, capture):
    """Restore fixed a/a_s once, then bind each paid U/T/e/f product grid.

    Actual fixed-metric path:
      CompleteBody168Field.metric
      -> FiveHeightField.metric(reference_evaluation_state)
      -> SingleQProblem.metric(to_old)
      -> BoundedEntryHeightProblem.__getattr__
      -> EntryRepairProblem / IndependentHeightProblem.metric
      -> body_metric.evaluate(fixed_metric, radial, jacobian=False).

    metric_free is zero along the published field chain.  That call returns
    a fixed one-dimensional metric table; only a/a_s are consumed here.
    No geometry, height_baseline, fixed_primitive, center, position two-jets,
    parameter Jacobian or current T/U evaluation is called by this helper.
    The published first-jet binder checks literal paid e/f against U/T once.
    """
    ledger.check("small168.restore-first-jets.entry")
    require(isinstance(field, CompleteBody168Field) and field.metric_free == 0,
            "the original frozen-metric complete168 field is required")
    require(isinstance(accepted_cache, dict)
            and accepted_cache.get("kind") == "accepted-point-paid-geometry"
            and accepted_cache.get("available") is True
            and accepted_cache.get("status") == "complete"
            and isinstance(accepted_cache.get("binding"), dict)
            and digest(accepted_cache["binding"]) == accepted_cache.get("binding_sha256"),
            "one complete original accepted56 CACHE2 is required")
    binding = accepted_cache["binding"]
    expected = {
        "accepted_index": 56,
        "physical_state_sha256": digest(field.identity(state168)),
        "independent168_array_sha256": array_digest(state168),
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "field_evaluation_sha256": field.definition_sha256}
    require(all(binding.get(key) == value for key, value in expected.items()),
            "accepted56 CACHE2 belongs to another physical field or point")
    saved_state = _decode(accepted_cache["accepted_independent168"], (168,), "CACHE2/state168")
    require(_same_bytes(saved_state, state168),
            "accepted56 CACHE2 has different independent coordinate bits")
    mathematical = field.metric_model(state168)
    require(isinstance(mathematical, dict)
            and "mathematical_definition" in mathematical
            and digest(mathematical["mathematical_definition"])
                == mathematical["mathematical_definition_sha256"],
            "the complete original frozen metric definition is required")
    event = {
        "schema": POLICY+"-fixed-radial-metric-restoration",
        "status": "started", "started_scientific_seconds": ledger.elapsed(),
        "radial_sha256": array_digest(radial),
        "fixed_metric_mathematical_definition_sha256":
            mathematical["mathematical_definition_sha256"],
        "fixed_radial_metric_calls_started": 1,
        "ordinary_geometry_calls": 0, "parameter_J_calls": 0,
        "height_or_center_primitive_calls": 0,
        "consumed_metric_arrays": ["a", "a_s"]}
    capture["fixed_radial_metric_restoration"] = event
    started = time.monotonic()
    try:
        raw = field.metric(state168, radial, jacobian=False)
        require(isinstance(raw, dict), "the original fixed metric must return its dictionary")
        metric = {name: _owned(raw[name], (len(radial),), "fixed metric/"+name)
                  for name in ("a", "a_s")}
        capture["_arrays"]["fixed_metric"] = metric
        require(np.all(metric["a"] > 0.), "the original radius is strictly positive")
        event.update(status="complete", arrays={
            name: _metadata_array(value) for name, value in metric.items()},
            fixed_radial_metric_calls_completed=1)
        ledger.check("small168.restore-fixed-metric.complete")
    except Exception as error:
        event.update(status="raised",
                     error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        event["elapsed_seconds"] = float(time.monotonic()-started)
        event["finished_scientific_seconds"] = ledger.elapsed()
        ledger.note("small168.fixed-radial-metric-restoration", receipt=copy.deepcopy(event))

    bounds = {}
    require(set(accepted_cache["grids"]) == set(LABELS), "both paid first-jet grids are required")
    for label in LABELS:
        ledger.check("small168.restore-first-jets."+label)
        rows, theta = accepted_cache["grids"][label], thetas[label]
        shape = (len(radial), len(theta))
        require(set(rows) == {"U", "T", "e", "f", "radial", "theta"},
                "the original CACHE2 first-jet fields must remain explicit")
        rr = _decode(rows["radial"], (shape[0],), "CACHE2/"+label+"/radial")
        th = _decode(rows["theta"], (shape[1],), "CACHE2/"+label+"/theta")
        require(_same_bytes(rr, radial) and _same_bytes(th, theta),
                "paid first-jet radial/theta bits changed")
        arrays = {name: _decode(rows[name],
                    shape+(3,) if name in ("U", "T") else (shape[0]*shape[1],),
                    "CACHE2/"+label+"/"+name) for name in ("U", "T", "e", "f")}
        for name in ("U", "T", "e", "f", "radial", "theta"):
            require(rows[name]["array_sha256"] == binding["grid_array_sha256"][label][name],
                    "accepted CACHE2 array metadata differs from its original binding")
        receipt = {
            "schema": POLICY+"-paid-current-first-jets",
            "source_accepted_index": 56, "grid": label,
            "accepted_CACHE2_binding_sha256": accepted_cache["binding_sha256"],
            "source_receipt": copy.deepcopy(source_receipt),
            "paid_U_T_e_f_array_metadata": {
                name: {key: rows[name][key] for key in ("shape", "dtype", "array_sha256")}
                for name in ("U", "T", "e", "f", "radial", "theta")},
            "fixed_radial_metric_restoration": copy.deepcopy(event),
            "old_U_T_e_f_recomputed": False,
            "published_binder_checks_paid_U_T_contractions_once": True}
        item = capture["grids"][label]
        item.update(stage="binding-paid-first-jets", first_jet_source=copy.deepcopy(receipt))
        tick = time.monotonic()
        try:
            bounds[label] = bind_current_168_first_jets(
                field, state168, radial, theta,
                {**arrays, "metric": metric, "radial": radial,
                 "theta": theta, "state168": state168},
                receipt, wall=ledger.check)
            item.update(stage="first-jets-bound",
                        first_jet_binding_sha256=bounds[label]["binding_sha256"])
        except Exception as error:
            item.update(stage="first-jet-bind-raised",
                        error={"type": type(error).__name__, "message": str(error)})
            raise
        finally:
            item["binding_seconds"] = float(time.monotonic()-tick)
    ledger.check("small168.restore-first-jets.complete")
    return bounds, metric, event


def build_small168_geometry(prepared, ledger, capture=None):
    require(isinstance(prepared, dict) and isinstance(ledger, Joint168Ledger),
            "one restored true56 input and the new small-domain ledger are required")
    ledger.check("small168-geometry.entry")
    sink = {} if capture is None else capture
    require(isinstance(sink, dict) and not sink, "an empty geometry capture is required")
    sink.update(schema=POLICY+"-paid-input-restoration", status="started",
                source_accepted_index=56, grids={label: {} for label in LABELS},
                _arrays={}, _new_metric_rows=[], new_ordinary_geometry_calls=0,
                selected_hard_or_allpool_J_builds=0, full_grid_parameter_tensors=0)
    result = Small168Geometry.__new__(Small168Geometry)
    try:
        result._build(prepared, ledger, sink)
        sink.update(status="complete", binding_sha256=result.binding_sha256,
                    receipt=result.receipt())
        ledger.check("small168-geometry.complete")
        return result
    except Exception as error:
        sink.update(status="raised",
                    error={"type": type(error).__name__, "message": str(error)},
                    scientific_seconds=ledger.elapsed())
        raise


class Small168Geometry(Joint168Geometry):
    """New small-domain identity, paid large-domain rows, fresh first-jet binds."""

    def _build(self, prepared, ledger, capture):
        self.ledger, self.capture = ledger, capture
        require(MAXIMUM_H_EXACT == "1/128" and MAXIMUM_H == 1./128.,
                "the independently authorized small physical domain is required")
        self.cfg = copy.deepcopy(prepared["cfg"])
        self.cfg_sha256 = digest(self.cfg)
        field = prepared.get("field168")
        if field is None:
            field = CompleteBody168Field(prepared["problem"])
        require(isinstance(field, CompleteBody168Field), "the original complete168 field is required")
        states = [prepared[key] for key in ("center168", "q168", "initial168") if key in prepared]
        require(bool(states), "the actual nonzero-new9 accepted56 state is required")
        self.center168 = self.q168 = _owned(states[0], (168,), "accepted56 independent168")
        require(all(_same_bytes(np.asarray(v, dtype=float), self.center168) for v in states[1:]),
                "the prepared current168 aliases must have identical bits")
        self.field = self.field168 = field
        self.original_field = field.original_field
        field.validate_state(self.center168)
        require(digest(field.identity(self.center168)) == SOURCE_PHYSICAL_SHA
                and field.coordinate_definition_sha256 == SOURCE_COORDINATE_SHA
                and field.definition_sha256 == SOURCE_FIELD_SHA
                and self.cfg_sha256 == SOURCE_CFG_SHA
                and np.any(self.center168[159:] != 0.),
                "the original accepted56 physical field/cfg/coordinates are fixed")
        self.source_binding = copy.deepcopy(prepared["source_binding"])
        require(self.source_binding.get("accepted_index") == 56
                and self.source_binding.get("independent168_array_sha256")
                    == array_digest(self.center168),
                "the exact accepted56 source binding is required")
        self.paid_joint_receipt = copy.deepcopy(prepared["paid_joint_receipt"])
        require(isinstance(self.paid_joint_receipt, dict)
                and self.paid_joint_receipt.get("source")
                and self.paid_joint_receipt.get("records"),
                "the root-authenticated paid joint log and record receipt are required")
        self.paid_input = prepared["paid_joint_input"]
        self.paid_model = prepared["paid_joint_model"]
        require(isinstance(self.paid_input, dict) and isinstance(self.paid_model, dict),
                "the literal paid INPUT3 and MODEL records are required")
        old_binding = self.paid_input["binding"]
        self.paid_input_binding_sha256 = digest(old_binding)
        require(self.paid_input["binding_sha256"] == self.paid_input_binding_sha256
                == self.paid_joint_receipt["input_binding_sha256"]
                == self.paid_model["input_binding_sha256"]
                and self.paid_model["model_binding_sha256"]
                    == self.paid_joint_receipt["model_binding_sha256"],
                "paid INPUT3/MODEL/source bindings differ")
        require(old_binding["schema"] == PAID_JOINT_POLICY+"-geometry-input"
                and old_binding["source_accepted_index"] == 56
                and old_binding["source_physical_state_sha256"] == SOURCE_PHYSICAL_SHA
                and old_binding["source_field_definition_sha256"] == SOURCE_FIELD_SHA
                and old_binding["source_coordinate_definition_sha256"] == SOURCE_COORDINATE_SHA
                and old_binding["configuration_sha256"] == self.cfg_sha256
                and old_binding["current_independent168_sha256"] == array_digest(self.center168),
                "paid derivatives must be at the same complete168 field and physical point")
        require(_same_bytes(_decode(self.paid_input["center168"], (168,), "INPUT3/center168"),
                            self.center168), "paid INPUT3 center bits changed")
        capture["paid_source_reference"] = copy.deepcopy(self.paid_joint_receipt)
        capture["paid_input_binding_sha256"] = self.paid_input_binding_sha256
        self.lower172 = _owned(prepared["lower172"], (172,), "physical lower172")
        self.upper172 = _owned(prepared["upper172"], (172,), "physical upper172")
        require(_same_bytes(_decode(self.paid_input["lower172"], (172,), "INPUT3/lower172"),
                            self.lower172)
                and _same_bytes(_decode(self.paid_input["upper172"], (172,), "INPUT3/upper172"),
                                self.upper172), "all exact physical172 box bounds are unchanged")
        self.center_box = field.exact_full_box_decision(
            self.center168, self.lower172, self.upper172)
        require(self.center_box["exact_full_box_pass"], "accepted56 must retain its exact172 box")
        self.physical_linear_map172x168 = _decode(
            self.paid_input["physical_linear_map172x168"], (172, 168), "INPUT3/M172x168")
        require(_same_bytes(self.physical_linear_map172x168,
                            np.asarray(prepared["physical_map172x168"], dtype=float))
                and array_digest(self.physical_linear_map172x168)
                    == old_binding["physical_linear_map172x168_sha256"],
                "the complete original physical172 map is unchanged")
        self.physical_map_source = {
            "schema": POLICY+"-same-physical-map-small-domain",
            "paid_exact_source_unchanged":
                copy.deepcopy(self.paid_input["physical_linear_map_exact_source"]),
            "source_INPUT3_binding_sha256": self.paid_input_binding_sha256,
            "matrix_sha256": array_digest(self.physical_linear_map172x168),
            "norm": "h=4*max(abs(M172x168@delta168));0<=h<=1/128",
            "maximum_h_exact": MAXIMUM_H_EXACT,
            "maximum_physical_displacement_exact": "1/512",
            "old_large_domain_is_closed": True}

        self.radial = _owned(prepared["radial"], name="source radial")
        self.theta = _owned(prepared["theta"], name="source coarse theta")
        self.fine_theta = _owned(prepared["fine_theta"], name="source fine theta")
        require(self.radial.ndim == self.theta.ndim == self.fine_theta.ndim == 1
                and len(self.fine_theta) == 2*len(self.theta), "both original complete grids are required")
        self.grids = prepared["row_grids"]
        require(set(self.grids) == set(LABELS)
                and all(isinstance(self.grids[x], RationalRowGrid)
                        and self.grids[x].label == x for x in LABELS),
                "the original rational row grids are required")
        self.side, self.order = int(prepared["gate"].side), int(prepared["order"])
        require(self.side in (-1, 1) and self.order == 8, "the original side and query order are fixed")
        self.epsilon = float(Q(self.cfg["metric_proposal_epsilon_exact"]))
        self.target = float(Q(self.cfg["fixed_metric_budget_exact"]))
        require(self.epsilon == 1.e-8 and self.target == .26
                and self.paid_input["epsilon"] == self.epsilon
                and self.paid_input["target"] == self.target,
                "the original spectral epsilon and metric target are fixed")
        self.tolerances = _row_tolerances(self.cfg)
        self.pools = {label: _ids(prepared[label+"_pool"], self.grids[label]) for label in LABELS}
        cp = prepared["replay"]["source_checkpoint"]
        self.pool_versions = {}
        source_pools, overlay = {}, []
        for label in LABELS:
            grid = self.grids[label]
            theta = self.theta if label == "coarse" else self.fine_theta
            require(grid.nr == len(self.radial) and grid.nt == len(theta)
                    and _same_bytes(np.asarray([float(t) for t in grid.nodes]), self.radial),
                    "the true rational grid and radial array differ")
            old_grid = old_binding["grids"][label]
            require(old_grid["grid_definition_sha256"] == grid.definition_sha256
                    and old_grid["radial_sha256"] == array_digest(self.radial)
                    and old_grid["theta_sha256"] == array_digest(theta),
                    "paid derivative row grid differs")
            src = self.paid_input["source_pools"][label]
            source_pools[label] = _ids(src["ids"], grid)
            version = cp[label+"_pool_version"]
            require(type(version) is int and version == CURRENT_POOL_VERSIONS[label]
                    and src["version"] == SOURCE_POOL_VERSIONS[label]
                    and len(source_pools[label]) == SOURCE_POOL_COUNTS[label]
                    and len(self.pools[label]) == CURRENT_POOL_COUNTS[label]
                    and self.pools[label].tolist() == cp[label+"_pool"]
                    and array_digest(source_pools[label]) == old_grid["source_pool_sha256"],
                    "the original source and post-failed-trial pool receipts differ")
            self.pool_versions[label] = version
            oldset = set(map(int, source_pools[label]))
            kept = [int(value) for value in self.pools[label] if int(value) in oldset]
            require(kept == source_pools[label].tolist(),
                    "a paid pool row or its original relative order was dropped")
            overlay.extend((label, int(value)) for value in self.pools[label]
                           if int(value) not in oldset)
        require(overlay == [MISSING_INITIAL_TAG],
                "only the actual new coarse metric row104448 may overlay the paid pool")
        self.source_pools = source_pools
        self.input_record_original_stdout_receipt = copy.deepcopy(
            prepared.get("input_record_original_stdout_receipt"))
        self.grid_records, self.base = {}, {}
        self._selected_lookup, self._gradient_records, self._selected_provenance = {}, {}, {}
        self._last_scan = self._last_direction_cache = None
        self._scan_cache, self._direction_caches = {}, {}
        self.scan_events, self.row_events, self.new_metric_records = [], [], []
        self.binding = None
        self.binding_sha256 = None
        thetas = {"coarse": self.theta, "fine": self.fine_theta}
        cache_receipt = {
            "source": copy.deepcopy(prepared["replay"]["source_paid_receipt"]),
            "new_task_paid_joint_receipt": copy.deepcopy(self.paid_joint_receipt),
            "accepted_CACHE2_binding_sha256": prepared["accepted_cache"]["binding_sha256"]}
        first, self.fixed_metric, self.fixed_metric_receipt = restore_paid56_first_jets(
            field, self.center168, self.radial, thetas, prepared["accepted_cache"],
            cache_receipt, ledger, capture)
        require(prepared["accepted_cache"]["binding"]["original_cfg_sha256"] == self.cfg_sha256,
                "the CACHE2 fixed cfg definition differs")
        for label in LABELS:
            grid, bound = self.grids[label], first[label]
            e, f = bound["data"]["e"].reshape(-1), bound["data"]["f"].reshape(-1)
            bp = np.empty((2, grid.point_count))
            ge, gf = np.empty_like(bp), np.empty_like(bp)
            for group in (0, 1):
                groups = np.full(grid.point_count, group, dtype=np.int64)
                bp[group] = phi(e, f, groups, self.epsilon)
                ge[group], gf[group] = phi_gradient(e, f, groups, self.epsilon)
            self.base[label] = {"e": e, "f": f, "branch_phi": _owned(bp),
                                "branch_ge": _owned(ge), "branch_gf": _owned(gf)}
            require(array_digest(e) == old_binding["grids"][label]["baseline_e_sha256"]
                    and array_digest(f) == old_binding["grids"][label]["baseline_f_sha256"]
                    and array_digest(self.base[label]["branch_phi"])
                        == old_binding["grids"][label]["branch_phi_sha256"],
                    "paid INPUT3 metric baseline must be identical to accepted56 CACHE2")
            key = ("radial_Jacobian_batch_owned_rows" if label == "coarse"
                   else "fine_Jacobian_owned_radial_rows")
            width = self.cfg[key]
            require(type(width) is int and 1 <= width <= 16, "the original bounded radial width is required")
            self.grid_records[label] = {
                "grid": grid, "radial": self.radial, "theta": thetas[label],
                "first_jet_bound": bound, "owned_width": width,
                "pool_ids": self.pools[label], "ids": self.pools[label],
                "no_ordinary_position_or_curvature_cache": True}
        self.phi0 = self.complete_phi0 = max(
            self.target, *(float(np.max(self.base[x]["branch_phi"])) for x in LABELS))
        require(self.phi0 == self.paid_input["complete_phi0"] == old_binding["complete_phi0"],
                "the paid full-grid baseline maximum changed")
        self.restoration_binding = {
            "schema": POLICY+"-first-jet-and-paid-row-restoration",
            "source56": copy.deepcopy(self.source_binding),
            "source_joint_receipt": copy.deepcopy(self.paid_joint_receipt),
            "paid_INPUT3_binding_sha256": self.paid_input_binding_sha256,
            "accepted_CACHE2_binding_sha256": prepared["accepted_cache"]["binding_sha256"],
            "fixed_metric_arrays": {k: _metadata_array(v) for k, v in self.fixed_metric.items()},
            "grids": {label: {
                "first_jet_binding_sha256": first[label]["binding_sha256"],
                "current_pool_sha256": array_digest(self.pools[label]),
                "current_pool_version": self.pool_versions[label]}
                for label in LABELS},
            "maximum_h_exact": MAXIMUM_H_EXACT}
        self.restoration_binding_sha256 = digest(self.restoration_binding)
        capture["restoration_binding_sha256"] = self.restoration_binding_sha256
        self._restore_domain_and_initial_rows(old_binding)
        prepared.update(field168=field, center168=self.center168,
                        q168=self.center168, initial168=self.center168)
        self.source56 = SOURCE_INDEX
        ledger.check("small168-geometry.binding-complete")

    def _restore_domain_and_initial_rows(self, old_binding):
        self.ledger.check("small168.restore-paid-domain.entry")
        source = self.paid_input["original_domain"]
        hard_tags = copy.deepcopy(source["hard_original_row_tags"])
        soft_tags = copy.deepcopy(source["selected_metric_original_row_tags"])
        require(isinstance(hard_tags, list) and isinstance(soft_tags, list)
                and len(hard_tags) == 3132 and len(soft_tags) == 5870
                and source["fixed_outside_phi"] == 0.,
                "the paid complete3132-hard/5870-soft input is required without filtering")
        hard_keys = [_tag_key(tag, self.grids, metric=False) for tag in hard_tags]
        soft_keys = [_tag_key(tag, self.grids, metric=True) for tag in soft_tags]
        require(len(set(hard_keys+soft_keys)) == len(hard_keys)+len(soft_keys),
                "every paid original domain row must remain unique")
        for label in LABELS:
            grid, pool = self.grids[label], self.source_pools[label]
            for keys, metric in ((hard_keys, False), (soft_keys, True)):
                wanted = [int(v) for v in pool if (int(v)//grid.point_count < 2) == metric]
                got = [flat for owner, flat in keys if owner == label]
                require(got == wanted, "the paid hard/soft pool order is incomplete")
        hard_J = _decode(source["hard_J168"], (len(hard_tags), 168), "INPUT3/hard-J168")
        hard_base = _decode(source["hard_base_values"], (len(hard_tags),), "INPUT3/hard-base")
        hard_targets = _decode(source["hard_targets"], (len(hard_tags),), "INPUT3/hard-target")
        soft_g = _decode(source["selected_metric_gradients168_of_phi"],
                         (len(soft_tags), 168), "INPUT3/selected-metric-g168")
        soft_phi = _decode(source["selected_metric_base_phi"], (len(soft_tags),),
                           "INPUT3/selected-metric-phi")
        pairs = (
            ("hard_J168_sha256", hard_J), ("hard_base_values_sha256", hard_base),
            ("hard_targets_sha256", hard_targets),
            ("selected_metric_g168_sha256", soft_g), ("selected_metric_phi_sha256", soft_phi))
        require(all(old_binding[key] == array_digest(value) for key, value in pairs)
                and old_binding["hard_tags_sha256"] == digest(hard_tags)
                and old_binding["selected_metric_tags_sha256"] == digest(soft_tags),
                "paid domain arrays or original tags differ from INPUT3's complete binding")
        for index, key in enumerate(soft_keys):
            label, flat = key
            group, point = divmod(flat, self.grids[label].point_count)
            require(float(soft_phi[index]) == float(self.base[label]["branch_phi"][group, point]),
                    "a paid selected metric row has a different current baseline")
            self._selected_lookup[key] = (soft_g[index], float(soft_phi[index]))
            self._selected_provenance[key] = {
                "kind": "paid-INPUT3-selected-metric-row",
                "source_INPUT3_binding_sha256": self.paid_input_binding_sha256,
                "source_row_index": index, "gradient_sha256": array_digest(soft_g[index])}
        self.paid_domain_metadata = {
            key: _metadata_array(value) for key, value in (
                ("hard_J168", hard_J), ("hard_base_values", hard_base),
                ("hard_targets", hard_targets),
                ("selected_metric_gradients168_of_phi", soft_g),
                ("selected_metric_base_phi", soft_phi))}
        self.paid_domain_metadata.update(
            hard_tags_sha256=digest(hard_tags), selected_metric_tags_sha256=digest(soft_tags))
        additions = self.paid_model["new_original_metric_rows_with_paid_gradients168"]
        require(isinstance(additions, list) and len(additions) == PAID_ADDITIONAL_ROWS,
                "all eight actual paid joint-model gradients are required")
        appended_g, appended_phi, appended_tags, paid_row_metadata = [], [], [], []
        for index, row in enumerate(additions):
            tag = copy.deepcopy(row["original_row"])
            key = _tag_key(tag, self.grids, metric=True)
            require(key == (row["grid"], row["flat_row_id"])
                    and key not in self._selected_lookup
                    and row["input_binding_sha256"] == self.paid_input_binding_sha256,
                    "a paid MODEL row is duplicated or bound to another input")
            gradient = _owned(row["gradient168"], (168,), "paid MODEL gradient168")
            require(array_digest(gradient) == row["gradient_sha256"],
                    "a paid MODEL gradient hash changed")
            label, flat = key
            group, point = divmod(flat, self.grids[label].point_count)
            value = float(row["base_phi"])
            require(np.isfinite(value) and value == float(self.base[label]["branch_phi"][group, point]),
                    "a paid MODEL gradient has a different baseline")
            self._selected_lookup[key] = (gradient, value)
            provenance = {
                "kind": "paid-closed-joint-MODEL-additional-row",
                "source_MODEL_binding_sha256": self.paid_joint_receipt["model_binding_sha256"],
                "source_INPUT3_binding_sha256": self.paid_input_binding_sha256,
                "source_record_index": index, "gradient_sha256": row["gradient_sha256"],
                "source_input_binding_sha256": row["input_binding_sha256"]}
            self._selected_provenance[key] = provenance
            appended_g.append(gradient); appended_phi.append(value); appended_tags.append(tag)
            paid_row_metadata.append({**copy.deepcopy(provenance),
                                      "grid": label, "flat_row_id": flat,
                                      "original_row": tag, "base_phi": value})
        require(MISSING_INITIAL_TAG not in self._selected_lookup,
                "the specifically unpaid104448 row may not be charged as an old row")
        first_new = self._materialize_metric_row(
            *MISSING_INITIAL_TAG, reason="actual failed large-domain trial's sole new soft pool row")
        appended_g.append(first_new["gradient168"])
        appended_phi.append(first_new["base_phi"])
        appended_tags.append(copy.deepcopy(first_new["original_row"]))
        self._selected_lookup[MISSING_INITIAL_TAG] = (
            first_new["gradient168"], first_new["base_phi"])
        self._selected_provenance[MISSING_INITIAL_TAG] = {
            "kind": "new-small-task-initial-missing-metric-row",
            "restoration_binding_sha256": self.restoration_binding_sha256,
            "charged_new_metric_rows_ordinal": first_new["charged_new_metric_rows_ordinal"]}
        complete_g = _owned(np.vstack((soft_g, np.asarray(appended_g))),
                            (5879, 168), "retained-paid-plus-nine-added-soft-gradients")
        complete_phi = _owned(np.r_[soft_phi, np.asarray(appended_phi)],
                              (5879,), "retained-paid-plus-nine-added-soft-values")
        all_soft_tags = soft_tags+appended_tags
        require(len(set(_tag_key(tag, self.grids, metric=True) for tag in all_soft_tags)) == 5879,
                "every retained or added original metric tag must be unique")
        for label in LABELS:
            wanted_hard = [int(v) for v in self.pools[label]
                           if int(v)//self.grids[label].point_count >= 2]
            require(wanted_hard == [flat for owner, flat in hard_keys if owner == label],
                    "a new hard pool row cannot be silently filled from old INPUT3")
            require(all((label, int(v)) in self._selected_lookup
                        for v in self.pools[label]
                        if int(v)//self.grids[label].point_count < 2),
                    "a current soft pool row is missing its real baseline gradient")
        self.original_domain = {
            "hard_J168": hard_J, "hard_base_values": hard_base,
            "hard_targets": hard_targets, "hard_original_row_tags": hard_tags,
            "selected_metric_gradients168_of_phi": complete_g,
            "selected_metric_base_phi": complete_phi,
            "selected_metric_original_row_tags": all_soft_tags, "fixed_outside_phi": 0.}
        self.paid_additional_row_metadata = paid_row_metadata
        self.domain_receipt = {
            "schema": POLICY+"-restored-hard-and-augmented-metric-domain",
            "source_INPUT3_binding_sha256": self.paid_input_binding_sha256,
            "source_MODEL_binding_sha256": self.paid_joint_receipt["model_binding_sha256"],
            "paid_original_hard_rows": len(hard_tags), "paid_original_soft_rows": len(soft_tags),
            "paid_MODEL_additional_rows": PAID_ADDITIONAL_ROWS,
            "new_initial_metric_rows": 1, "initial_metric_rows": len(all_soft_tags),
            "new_initial_original_row": copy.deepcopy(first_new["original_row"]),
            "all_paid_hard_values_targets_and_derivatives_retained_verbatim": True,
            "all_paid_soft_gradients_and_baselines_retained_verbatim": True,
            "all_current_pool_rows_covered": True, "support_filter": False,
            "hard_target_rule_unchanged_from_paid_INPUT3": True,
            "fraction_to_boundary_exact": self.cfg["linear_fraction_to_boundary_exact"],
            "strip_floor_exact": self.cfg["strip_proposal_floor_exact"],
            "curvature_floor_exact": self.cfg["curvature_proposal_floor_exact"],
            "original_group_tolerances": self.tolerances.tolist(),
            "fixed_outside_phi": 0.,
            "maximum_h_exact": MAXIMUM_H_EXACT,
            "maximum_physical_displacement_exact": "1/512",
            "ordinary_geometry_rebuild_calls": 0,
            "selected_hard_or_allpool_J_rebuild_calls": 0,
            "complete_grid_parameter_tensor_builds": 0,
            "actual14_gates_and_exact172_box_are_separate": True,
            "small_domain_is_new_method_not_large_domain_remaining_budget": True}
        self.binding = {
            "schema": POLICY+"-geometry-input",
            "source_binding": copy.deepcopy(self.source_binding),
            "source_accepted_index": 56,
            "source_physical_state_sha256": SOURCE_PHYSICAL_SHA,
            "source_field_definition_sha256": SOURCE_FIELD_SHA,
            "source_coordinate_definition_sha256": SOURCE_COORDINATE_SHA,
            "configuration_sha256": self.cfg_sha256,
            "current_independent168_sha256": array_digest(self.center168),
            "lower172_sha256": array_digest(self.lower172),
            "upper172_sha256": array_digest(self.upper172),
            "physical_linear_map172x168_sha256": array_digest(self.physical_linear_map172x168),
            "physical_map_source_sha256": digest(self.physical_map_source),
            "target": self.target, "epsilon": self.epsilon, "complete_phi0": self.phi0,
            "maximum_h_exact": MAXIMUM_H_EXACT,
            "source_INPUT3_binding_sha256": self.paid_input_binding_sha256,
            "source_MODEL_binding_sha256": self.paid_joint_receipt["model_binding_sha256"],
            "paid_joint_receipt_sha256": digest(self.paid_joint_receipt),
            "restoration_binding_sha256": self.restoration_binding_sha256,
            "hard_J168_sha256": array_digest(hard_J),
            "hard_base_values_sha256": array_digest(hard_base),
            "hard_targets_sha256": array_digest(hard_targets),
            "hard_tags_sha256": digest(hard_tags),
            "selected_metric_tags_sha256": digest(all_soft_tags),
            "selected_metric_g168_sha256": array_digest(complete_g),
            "selected_metric_phi_sha256": array_digest(complete_phi),
            "paid_additional_rows": copy.deepcopy(paid_row_metadata),
            "initial_new_gradient_sha256": first_new["gradient_sha256"],
            "grids": {label: {
                "grid_definition_sha256": self.grids[label].definition_sha256,
                "radial_sha256": array_digest(self.radial),
                "theta_sha256": array_digest(self.grid_records[label]["theta"]),
                "first_jet_bound_sha256": self.grid_records[label]["first_jet_bound"]["binding_sha256"],
                "source_pool_sha256": array_digest(self.source_pools[label]),
                "current_pool_sha256": array_digest(self.pools[label]),
                "current_pool_version": self.pool_versions[label],
                "baseline_e_sha256": array_digest(self.base[label]["e"]),
                "baseline_f_sha256": array_digest(self.base[label]["f"]),
                "branch_phi_sha256": array_digest(self.base[label]["branch_phi"])}
                for label in LABELS},
            "domain_receipt_sha256": digest(self.domain_receipt),
            "new_ordinary_geometry_calls": 0, "new_selected_hard_or_allpool_J_builds": 0,
            "paid_fixed_metric_and_current_field_math_not_changed": True,
            "fresh_method_and_first_jet_context_not_an_old_model_certificate": True}
        self.binding_sha256 = digest(self.binding)
        # First104448 was actually computed before the final complete binding.
        # Its real first-jet/restoration provenance is preserved, then explicitly
        # associated with the final input which now contains that same row.
        for row in self.new_metric_records:
            row["binding_sha256"] = self.binding_sha256
            row["final_complete_input_bound"] = True
        self._gradient_records[MISSING_INITIAL_TAG] = first_new
        self.ledger.check("small168.restore-paid-domain.complete")

    def _materialize_metric_row(self, label, flat, *, reason, scan=None):
        grid, rec = self.grids[label], self.grid_records[label]
        group, point = divmod(flat, grid.point_count)
        tag = grid.coordinate(flat)
        event = self.ledger.begin(
            "new_metric_rows", grid=label, flat_row_id=flat, original_row=copy.deepcopy(tag),
            reason=str(reason), source_accepted_index=56,
            restoration_binding_sha256=self.restoration_binding_sha256,
            first_jet_binding_sha256=rec["first_jet_bound"]["binding_sha256"],
            final_input_binding_sha256=self.binding_sha256,
            ordinary_geometry_calls=0, old_selected_J_calls=0,
            metric_only_selected_rows=1, selected_parameter_columns=168)
        self.row_events.append(event)
        try:
            obs, diag = current_168_metric_selected_rows(
                self.field, self.center168, self.radial, rec["theta"], [flat],
                rec["first_jet_bound"], owned_width=rec["owned_width"],
                wall=self.ledger.check)
            self.capture["_arrays"]["last_new_metric_observables"] = obs
            require(obs["row_ids"].tolist() == [flat]
                    and obs["row_positions"].tolist() == [0]
                    and obs["groups"].tolist() == [group],
                    "the metric-only API must preserve the literal original row")
            base = self.base[label]
            require(_same_bytes(obs["e"], base["e"][point:point+1])
                    and _same_bytes(obs["f"], base["f"][point:point+1]),
                    "a new derivative may not substitute its paid U/T baseline")
            gradient = _owned(base["branch_ge"][group, point]*obs["de"][0]
                              + base["branch_gf"][group, point]*obs["df"][0],
                              (168,), "new metric-only gradient168")
            result = {
                "schema": POLICY+"-baseline-original-row-gradient",
                "grid": label, "flat_row_id": flat, "original_row": tag,
                "gradient": gradient, "gradient168": gradient,
                "gradient_sha256": array_digest(gradient),
                "base_phi": float(base["branch_phi"][group, point]),
                "restoration_binding_sha256": self.restoration_binding_sha256,
                "first_jet_binding_sha256": rec["first_jet_bound"]["binding_sha256"],
                "final_complete_input_bound": self.binding_sha256 is not None,
                "new_original_tag_debit": True,
                "charged_new_metric_rows_ordinal": event["ordinal"],
                "source": str(reason),
                "selected_diagnostics": copy.deepcopy(diag),
                "metric_observables": {key: obs[key] for key in ("e", "f", "de", "df")},
                "linearization_point": "same actual accepted56 nonzero-new9 complete field",
                "not_a_candidate_point_tangent": True,
                "no_actual_geometry_evaluation": True}
            if self.binding_sha256 is not None:
                result["binding_sha256"] = self.binding_sha256
            if scan is not None:
                result["source_scan_ordinal"] = scan["ordinal"]
                result["source_scan_direction_sha256"] = scan["direction_sha256"]
            # Preserve the actual new arrays BEFORE end/check or later input
            # assembly can fail.  The public capture is intentionally visible
            # to the caller's failure serializer; no old large matrix is added.
            self.new_metric_records.append(result)
            self.capture["_new_metric_rows"].append(result)
            self.capture.setdefault("completed_new_metric_gradients", []).append(result)
            self.ledger.end(event, gradient_sha256=result["gradient_sha256"],
                            base_phi=result["base_phi"], selected_diagnostics=copy.deepcopy(diag))
            self.ledger.check("small168.metric-only-row.complete")
            return result
        except Exception as error:
            if event.get("status") == "started":
                self.ledger.end(event, error)
            raise

    def attainer_gradient(self, label, flat_row_id, *, scan=None):
        self.ledger.check("small168.attainer.entry")
        require(label in LABELS and isinstance(flat_row_id, (int, np.integer))
                and not isinstance(flat_row_id, (bool, np.bool_)),
                "one literal original coarse/fine metric row ID is required")
        grid = self.grids[label]
        flat = int(grid.ids([int(flat_row_id)])[0])
        group, point = divmod(flat, grid.point_count)
        require(group in (0, 1), "only original metric branch rows use this API")
        key = (label, flat)
        if scan is not None:
            require(scan["binding_sha256"] == self.binding_sha256
                    and any(row["grid"] == label and row["flat_row_id"] == flat
                            for row in scan["branches"]),
                    "a new row must be an actual complete-scan attainer of this input")
        if key in self._gradient_records:
            return copy.deepcopy(self._gradient_records[key])
        if key in self._selected_lookup:
            gradient, basephi = self._selected_lookup[key]
            result = {
                "schema": POLICY+"-baseline-original-row-gradient",
                "grid": label, "flat_row_id": flat, "original_row": grid.coordinate(flat),
                "gradient": gradient, "gradient168": gradient,
                "gradient_sha256": array_digest(gradient), "base_phi": basephi,
                "binding_sha256": self.binding_sha256,
                "source": "retained paid initial-domain row",
                "paid_source_provenance": copy.deepcopy(self._selected_provenance[key]),
                "new_original_tag_debit": False, "selected_diagnostics": None,
                "linearization_point": "same actual accepted56 nonzero-new9 complete field",
                "not_a_candidate_point_tangent": True, "no_actual_geometry_evaluation": True}
        else:
            result = self._materialize_metric_row(
                label, flat, reason="new original attainer of the complete small-domain scan",
                scan=scan)
        self._gradient_records[key] = result
        return copy.deepcopy(result)

    def _label_direction_records(self):
        # The inherited math/byte cache is unchanged.  Do not mutate the
        # frozen old module's POLICY or present its schema as this new task.
        for scan in self._scan_cache.values():
            scan["schema"] = POLICY+"-complete-first-order-scan"
            scan["inherited_oracle_algorithm_policy"] = PAID_JOINT_POLICY
            scan["maximum_h_exact"] = MAXIMUM_H_EXACT
        for cache in self._direction_caches.values():
            cache["schema"] = POLICY+"-affine-observable-direction-cache"
            cache["inherited_oracle_algorithm_policy"] = PAID_JOINT_POLICY
            cache["maximum_h_exact"] = MAXIMUM_H_EXACT

    def scan(self, delta168, phase="master"):
        try:
            return super().scan(delta168, phase=phase)
        finally:
            self._label_direction_records()

    def direction_cache(self, delta168):
        cache = super().direction_cache(delta168)
        self._label_direction_records()
        return cache

    def model_input(self):
        result = super().model_input()
        result["maximum_h_exact"] = MAXIMUM_H_EXACT
        return result

    def full_payload(self, array_encoder=None):
        """New input reference plus genuinely new outputs; no old J/UT copy."""
        self.ledger.check("small168.input-payload")
        encode = _array_payload if array_encoder is None else array_encoder
        require(callable(encode), "an array encoder is required")
        result = {
            "schema": POLICY+"-paid-input-with-new-metric-row",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "restoration_binding": copy.deepcopy(self.restoration_binding),
            "restoration_binding_sha256": self.restoration_binding_sha256,
            "source56": 56, "center168": encode(self.center168),
            "complete_phi0": self.phi0, "target": self.target, "epsilon": self.epsilon,
            "maximum_h_exact": MAXIMUM_H_EXACT,
            "maximum_physical_displacement_exact": "1/512",
            "paid_joint_original_stdout_reference": copy.deepcopy(self.paid_joint_receipt),
            "paid_INPUT3_binding_sha256": self.paid_input_binding_sha256,
            "paid_original_domain_metadata": copy.deepcopy(self.paid_domain_metadata),
            "paid_MODEL_additional_row_metadata": copy.deepcopy(self.paid_additional_row_metadata),
            "new_metric_gradients_computed_this_task": [
                _new_row_payload(row, encode) for row in self.new_metric_records],
            "new_fixed_radial_metric": {name: encode(value)
                                        for name, value in self.fixed_metric.items()},
            "fixed_radial_metric_restoration": copy.deepcopy(self.fixed_metric_receipt),
            "domain_receipt": copy.deepcopy(self.domain_receipt),
            "current_pools": {label: {
                "rows": len(self.pools[label]), "version": self.pool_versions[label],
                "ids_sha256": array_digest(self.pools[label]),
                "source_INPUT3_pool_sha256": array_digest(self.source_pools[label])}
                for label in LABELS},
            "sole_pool_overlay": {"grid": "coarse", "flat_row_id": 104448,
                                  "original_row": self.grids["coarse"].coordinate(104448)},
            "hard_J_soft_g_physical_map_and_paid_UT_not_duplicated": True,
            "original_paid_INPUT3_and_MODEL_remain_authoritative": True,
            "source_pool_overlay_ids_are_in_authenticated_paid_joint_COMPLETE": True}
        if self.input_record_original_stdout_receipt is not None:
            result["input_record_original_stdout_receipt"] = copy.deepcopy(
                self.input_record_original_stdout_receipt)
        self.ledger.check("small168.input-payload.complete")
        return result

    def receipt(self):
        return {
            "schema": POLICY+"-geometry-receipt",
            "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
            "source56": 56, "complete_phi0": self.phi0,
            "target": self.target, "epsilon": self.epsilon,
            "maximum_h_exact": MAXIMUM_H_EXACT,
            "domain": copy.deepcopy(self.domain_receipt),
            "coverage": {label: self.grids[label].point_count for label in LABELS},
            "first_jet_cache_accessor": "grid_records[label]['first_jet_bound']",
            "ordinary_cache_accessor": None, "full_scalar_or_curvature_cache_accessor": None,
            "paid_source_reference": copy.deepcopy(self.paid_joint_receipt),
            "fixed_radial_metric_restoration": copy.deepcopy(self.fixed_metric_receipt),
            "paid_hard_and_soft_inputs_reused": True,
            "paid_MODEL_additional_gradients_reused": PAID_ADDITIONAL_ROWS,
            "initial_new_metric_rows": 1,
            "new_metric_rows_completed_so_far": len(self.new_metric_records),
            "new_ordinary_geometry_calls": 0,
            "new_hard_or_allpool_selected_J_calls": 0,
            "no_support_filter": True, "no_new_full_grid_parameter_tensor": True,
            "actual_candidate_not_evaluated_by_this_helper": True,
            "all_actual14_gates_are_owned_by_the_caller": True,
            "old_geometry_receipt_two_new_ordinary_claim_not_inherited": True}

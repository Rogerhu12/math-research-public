#!/usr/bin/env python3
"""Export paid selected current168 ordinary jets; rebuild only a future J.

This module is import-only.  Export/bind select, copy, hash and serialize
existing arrays and metadata.  They never call geometry, scalar_frame,
height_jets, a primitive, a directional oracle, a solver, or a Jacobian.
The final selected derivative API does new, separately charged Jacobian
work through the original full-angle kernels and original contractions.

A selected cache is its own binding, not a fake full-grid ordinary record.
There are no fabricated zero entries for unsaved physical points.  An
out-of-scope original row is rejected even if another group at its point
happened to be exported.  Original pool order and requested row duplicates
are distinct from the sorted unique point/radial indices used for storage.

This saves a future ordinary input reconstruction; it is not a new actual
gate receipt or a free Jacobian.  All elapsed time, imports, export/output,
new derivative calls and failures remain owned by the enclosing task.
"""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_complete_body_extension168 import (
    CompleteBody168Field, INDEPENDENT_COUNT, POSITION_KEYS,
    POLICY as FIELD_POLICY, array_binding, _validate_grid)
from frame_complete_body_extension168_joint_selected import (
    _context, _width, _row_ids, _base_diagnostics, _families,
    _first_four_virtual, _height_six)
from frame_selected_row_radial_jacobian import (
    angular_kernels, virtual_selected_jets, expand_radial_rows,
    selected_spectral_parameter_jacobian)
from frame_metric_affine_spectral_model import observable_parameter_jacobians
from frame_metric_spectral_recovery import (
    POLICY as SPECTRAL_POLICY, EPSILON_EXACT)


POLICY = "complete168-paid-selected-ordinary-cache-and-current-J-v1"
N = INDEPENDENT_COUNT
METRIC_KEYS = ("a", "a_s", "a_ss")
HEIGHT_KEYS = ("b", "b_s", "b_ss")
GRID_LABELS = ("coarse", "fine")


def definition():
    return {
        "schema": POLICY,
        "source_derivative_module": "frame_complete_body_extension168_joint_selected.py",
        "source_derivative_function": "current_168_selected_rows",
        "export_scope": "one actual current pool on one original full grid",
        "physical_parameter_count": 172, "independent_parameter_count": 168,
        "position_arrays_at_sorted_unique_pool_points": list(POSITION_KEYS),
        "position_array_shape": ["number_of_saved_points", 3],
        "row_ids": "literal original pool order; not replaced by sorted point IDs",
        "point_ids": "sorted unique row_id % (Nr*Ntheta)",
        "metric_radial_ids": "sorted union of selected radial IDs with original first/last radial IDs",
        "metric_arrays_at_saved_radial_ids": list(METRIC_KEYS),
        "optional_paid_height_samples_at_same_radial_ids": list(HEIGHT_KEYS),
        "height_samples_are_provenance_not_an_extra_J_input": True,
        "height_J_source": "original _height_six; exact five null functions plus R490 gamma",
        "height_and_common_center_already_present_in_saved_position_jets": True,
        "no_center_value_or_primitive_is_required_by_the_selected_J_consumer": True,
        "all_seven_selected_position_arrays_retained":
            "the frozen contraction reads all seven at the batch; no new group-specific shortcut",
        "no_full_grid_position_array_reconstruction_or_zero_fill": True,
        "no_baseline_ordinary_replay_in_the_new_adapter": True,
        "no_old_parameter_J_reuse": True,
        "unmodified_three_current_angular_families_and_six_height_columns": True,
        "same_full_circle_before_selection_and_original_Nyquist_rules": True,
        "new_J_scope_and_method_identity": True,
        "different_new_point_cannot_reuse_this_selected_ordinary_binding": True,
        "new_pool_rows_not_in_the_exported_scope_require_new_paid_inputs": True,
        "new_metric_attainer_path":
            "use the separate current168 metric-only selected API with the existing full-grid first-jet binding",
        "new_hard_rows_outside_saved_scope_are_not_filled_or_replayed": True,
        "export_and_bind_do_not_evaluate_geometry_or_parameter_derivatives": True,
        "future_J_is_new_scientific_work_not_an_export_cost_waiver": True,
        "actual14_box_curvature_and_two_grid_descent_gates_are_not_evaluated": True}


def implementation_hashes():
    names = (
        Path(__file__).name, "frame_complete_body_extension168.py",
        "frame_complete_body_extension168_joint_selected.py",
        "frame_selected_row_radial_jacobian.py", "frame_collar_bvp.py",
        "frame_metric_spectral_recovery.py", "frame_metric_budget_restoration_rows.py",
        "frame_metric_affine_spectral_model.py", "frame_height_null_coordinates.py",
        "frame_curvature_psd.py")
    root = Path(__file__).parent
    return {name: hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names}


def _require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def _wall(wall):
    if wall is not None:
        wall()


def _error(error):
    return {"type": type(error).__name__, "message": str(error)}


def _same(left, right):
    a, b = np.asarray(left), np.asarray(right)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def _float_array(value, shape, name, *, copy_array=True):
    a = np.asarray(value, dtype=np.float64)
    _require(a.shape == tuple(shape) and np.all(np.isfinite(a)),
             "finite selected array with original shape required: "+name)
    a = a.copy() if copy_array else a.view()
    a.setflags(write=False)
    return a


def _integer_array(value, name):
    raw = np.asarray(value)
    _require(raw.ndim == 1 and raw.dtype.kind in "iu",
             "literal integer array, not float/bool coercion, required: "+name)
    _require(np.all(raw >= 0) and np.all(raw <= np.iinfo(np.int64).max),
             "nonnegative signed-int64 range required: "+name)
    a = np.asarray(raw, dtype=np.int64).copy()
    a.setflags(write=False)
    return a


def _pool_version(value):
    _require(not isinstance(value, (bool, np.bool_))
             and isinstance(value, (int, np.integer)) and value >= 0,
             "nonnegative literal current pool version required")
    return int(value)


def _config(cfg, side):
    _require(isinstance(cfg, dict)
             and cfg.get("metric_proposal_policy") == SPECTRAL_POLICY
             and cfg.get("metric_proposal_epsilon_exact") == EPSILON_EXACT,
             "the original scalar-row and spectral configuration is required")
    _require(not isinstance(side, (bool, np.bool_))
             and isinstance(side, (int, np.integer)) and side in (-1, 1),
             "the original signed physical side is required")


def _height_identity(field):
    old = field.original_field
    return {
        "old159_coordinate_definition_sha256": old.coordinate_definition_sha256,
        "old_five_null_basis_identity_sha256": old.null_basis.identity_sha256,
        "old_five_null_basis_evaluation_definition_sha256":
            digest(old.null_basis.evaluation_definition()),
        "original_fixed_height_base_definition_sha256":
            digest(field.height_base_definition),
        "complete168_coordinate_definition_sha256": field.coordinate_definition_sha256,
        "new_gamma_definition": "R490: center=L*P8, b=P8_xi_prime, b_s=P8_xi_second/L",
        "all_height_coordinates_are_the_original_current168_entries_154_to_158_and_167": True,
        "height_identity_reads_definitions_not_basis_values_or_primitives": True}


def _physical_context(field, q, r, theta, cfg, side):
    return {
        "field_definition_sha256": field.definition_sha256,
        "ordinary_evaluation_definition_sha256": digest(field.evaluation_definition()),
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "physical_identity_sha256": digest(field.identity(q)),
        "state168": array_binding(q),
        "radial": array_binding(r), "theta": array_binding(theta),
        "configuration_sha256": digest(cfg), "side": int(side),
        "height": _height_identity(field)}


def _source_ordinary_binding(bound, field, q, r, theta):
    """Check the original owner-made binding without evaluating an ordinary."""
    expected = {
        "schema": FIELD_POLICY+"-bound-ordinary",
        "field_definition_sha256": field.definition_sha256,
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "physical_identity_sha256": digest(field.identity(q)),
        "state": array_binding(q), "radial": array_binding(r),
        "theta": array_binding(theta), "source_receipt": bound.get("source_receipt")}
    _require(isinstance(bound.get("source_receipt"), dict)
             and bound.get("binding_sha256") == digest(expected),
             "the original field.bind_ordinary owner receipt/binding changed")
    return {
        "binding_sha256": bound["binding_sha256"],
        "identity": expected,
        "complete_six_position_jets_required": bound.get("complete_six_position_jets_required"),
        "no_ordinary_evaluation_in_binding": bound.get("no_ordinary_evaluation_in_binding")}


def _pack_array(value):
    a = np.ascontiguousarray(value)
    return {**array_binding(a), "values": a.tolist()}


def _manifest(arrays):
    return {name: array_binding(value) for name, value in arrays.items()}


def _read_array(payload, metadata, name, *, integer=False):
    _require(isinstance(payload, dict) and isinstance(metadata, dict),
             "selected array payload and identity required: "+name)
    if integer:
        a = _integer_array(payload.get("values"), name)
    else:
        raw = np.asarray(payload.get("values"), dtype=np.float64)
        a = _float_array(raw, raw.shape, name)
    actual = array_binding(a)
    _require(actual == metadata
             and {key: payload.get(key) for key in actual} == actual,
             "selected payload shape/dtype/bytes/SHA differs: "+name)
    return a


def export_selected_current168_geometry(
        field, state168, radial, theta, row_ids, ordinary_bound, cfg, *,
        grid_label, side, pool_version, source_receipt, wall=None, capture=None):
    """JSON-safe selected-only export from an ALREADY PAID current ordinary.

    The actual cache owner supplies ordinary_bound from field.bind_ordinary.
    source_receipt names the accepted point/pool/native output provenance.
    This function records that claim; it does not rerun or manufacture the
    actual gates.  Call after all actual value-only pool additions intended
    for the next model, so their literal rows are included in row_ids.

    No full U/T/first-jet cache is replaced: full-grid future direction scans
    still require their own existing paid first-jet record.  This export is
    precisely the additional selected position-two-jet input for a future J.
    A later soft attainer outside this pool uses the separate metric-only
    selected API and its full-grid first jets, not a fabricated hard cache.
    """
    started = time.monotonic()
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty export capture required")
    sink.update(schema=POLICY+"-export-capture", status="started",
                grid=grid_label, completed_array_names=[], _selected_arrays={})
    try:
        _wall(wall)
        _context(field)
        _config(cfg, side)
        _require(grid_label in GRID_LABELS, "original coarse or fine label required")
        version = _pool_version(pool_version)
        _require(isinstance(source_receipt, dict) and bool(source_receipt),
                 "the actual owner/source receipt is required")
        q, r, th, ordinary = field.validate_bound(
            state168, radial, theta, ordinary_bound)
        source_binding = _source_ordinary_binding(ordinary_bound, field, q, r, th)
        nr, nt = len(r), len(th)
        ids, groups, points = _row_ids(row_ids, nr, nt)
        _require(len(np.unique(ids)) == len(ids),
                 "an original current pool must not contain duplicate row IDs")
        point_ids = np.unique(points).astype(np.int64, copy=False)
        radial_ids = np.unique(np.r_[0, point_ids//nt, nr-1]).astype(np.int64, copy=False)
        ri, ti = point_ids//nt, point_ids % nt
        arrays = {
            "state168": _float_array(q, (168,), "state168"),
            "radial": _float_array(r, (nr,), "radial"),
            "theta": _float_array(th, (nt,), "theta"),
            "pool_row_ids": _integer_array(ids, "pool_row_ids"),
            "point_ids": _integer_array(point_ids, "point_ids"),
            "metric_radial_ids": _integer_array(radial_ids, "metric_radial_ids")}
        sink["_selected_arrays"].update(arrays)
        sink["completed_array_names"].extend(arrays)
        for key in POSITION_KEYS:
            _wall(wall)
            value = np.asarray(ordinary.get(key))
            _require(value.dtype == np.dtype(np.float64)
                     and value.shape == (nr, nt, 3),
                     "original paid full-grid position shape/dtype required: "+key)
            selected = _float_array(value[ri, ti], (len(point_ids), 3), key)
            name = "position_"+key
            arrays[name] = selected
            sink["_selected_arrays"][name] = selected
            sink["completed_array_names"].append(name)
        metric = ordinary.get("metric")
        _require(isinstance(metric, dict), "paid original metric arrays required")
        for key in METRIC_KEYS:
            _wall(wall)
            value = np.asarray(metric.get(key))
            _require(value.dtype == np.dtype(np.float64) and value.shape == (nr,),
                     "paid original full-radial metric shape/dtype required: "+key)
            name = "metric_"+key
            arrays[name] = _float_array(value[radial_ids], (len(radial_ids),), name)
            sink["_selected_arrays"][name] = arrays[name]
            sink["completed_array_names"].append(name)
        height = ordinary.get("height")
        height_available = isinstance(height, dict) and all(key in height for key in HEIGHT_KEYS)
        if isinstance(height, dict) and not height_available:
            raise ValueError("partial paid height dictionary cannot be silently completed")
        if height_available:
            for key in HEIGHT_KEYS:
                _wall(wall)
                value = np.asarray(height[key])
                _require(value.dtype == np.dtype(np.float64) and value.shape == (nr,),
                         "paid height sample shape/dtype differs: "+key)
                name = "height_"+key
                arrays[name] = _float_array(value[radial_ids], (len(radial_ids),), name)
                sink["_selected_arrays"][name] = arrays[name]
                sink["completed_array_names"].append(name)
        identity = {
            "schema": POLICY+"-selected-ordinary",
            "definition_sha256": digest(definition()),
            "context": _physical_context(field, q, r, th, cfg, side),
            "grid_label": grid_label, "pool_version": version,
            "source_ordinary_binding": source_binding,
            "source_receipt": copy.deepcopy(source_receipt),
            "arrays": _manifest(arrays),
            "row_count": len(ids), "saved_point_count": len(point_ids),
            "saved_metric_radial_count": len(radial_ids),
            "original_point_count": nr*nt,
            "pool_order_preserved": True,
            "height_samples_available": height_available,
            "height_samples_consumed_by_selected_J": False,
            "all_selected_position_values_copied_from_current_ordinary": True,
            "ordinary_geometry_calls": 0, "parameter_Jacobian_calls": 0,
            "no_fabricated_full_grid_arrays": True,
            "acceptance_is_the_original_owner_receipt_not_a_new_check": True}
        payload = {
            "schema": POLICY+"-payload",
            "identity": identity, "binding_sha256": digest(identity),
            "configuration": copy.deepcopy(cfg),
            "arrays": {name: _pack_array(value) for name, value in arrays.items()},
            "export_seconds_before_return": float(time.monotonic()-started)}
        sink.update(status="complete", binding_sha256=payload["binding_sha256"],
                    identity=copy.deepcopy(identity), payload=payload)
        _wall(wall)
        return payload
    except Exception as error:
        sink.update(status="raised", error=_error(error),
                    elapsed_seconds_before_raise=float(time.monotonic()-started))
        raise


def bind_selected_current168_geometry(
        field, state168, radial, theta, row_ids, payload, cfg, *,
        grid_label, side, pool_version, expected_binding_sha256,
        expected_source_receipt=None, wall=None):
    """Decode/validate selected bytes; never reconstruct full-grid ordinary.

    expected_binding_sha256 must come from the authenticated original-output
    record chosen by the caller.  Array SHA/shape/dtype and current physical,
    cfg, side, grid, original pool ORDER and version are all checked here.
    """
    _wall(wall)
    _context(field)
    _config(cfg, side)
    q = field.validate_state(state168)
    r, th = _validate_grid(radial, theta)
    ids, _, _ = _row_ids(row_ids, len(r), len(th))
    version = _pool_version(pool_version)
    _require(grid_label in GRID_LABELS, "original coarse or fine label required")
    _require(isinstance(payload, dict) and payload.get("schema") == POLICY+"-payload",
             "the explicit selected-only payload is required")
    identity = payload.get("identity")
    _require(isinstance(identity, dict) and identity.get("schema") == POLICY+"-selected-ordinary",
             "selected-only identity is missing")
    _require(isinstance(expected_binding_sha256, str)
             and len(expected_binding_sha256) == 64
             and expected_binding_sha256 == payload.get("binding_sha256") == digest(identity),
             "selected source binding differs from the original-output receipt")
    _require(identity.get("definition_sha256") == digest(definition())
             and identity.get("context") == _physical_context(field, q, r, th, cfg, side)
             and identity.get("grid_label") == grid_label
             and identity.get("pool_version") == version,
             "selected source physical/reference/cfg/grid/side/version changed")
    _require(payload.get("configuration") == cfg,
             "the literal original configuration changed")
    if expected_source_receipt is not None:
        _require(identity.get("source_receipt") == expected_source_receipt,
                 "selected owner/source receipt changed")
    data, manifest = payload.get("arrays"), identity.get("arrays")
    _require(isinstance(data, dict) and isinstance(manifest, dict)
             and set(data) == set(manifest), "selected payload array inventory differs")
    required = {"state168", "radial", "theta", "pool_row_ids", "point_ids", "metric_radial_ids"}
    required.update("position_"+key for key in POSITION_KEYS)
    required.update("metric_"+key for key in METRIC_KEYS)
    if identity.get("height_samples_available") is True:
        required.update("height_"+key for key in HEIGHT_KEYS)
    _require(set(data) == required, "selected payload has missing or undeclared arrays")
    integers = {"pool_row_ids", "point_ids", "metric_radial_ids"}
    arrays = {name: _read_array(data[name], manifest[name], name, integer=name in integers)
              for name in sorted(required)}
    _require(_same(arrays["state168"], q) and _same(arrays["radial"], r)
             and _same(arrays["theta"], th) and _same(arrays["pool_row_ids"], ids),
             "literal selected state/grid/pool bytes changed")
    expected_points = np.unique(ids % (len(r)*len(th)))
    expected_radial = np.unique(np.r_[0, expected_points//len(th), len(r)-1])
    _require(_same(arrays["point_ids"], expected_points)
             and _same(arrays["metric_radial_ids"], expected_radial)
             and len(np.unique(ids)) == len(ids),
             "saved point/radial index map is not the literal original pool map")
    mp, mr = len(expected_points), len(expected_radial)
    for key in POSITION_KEYS:
        _require(arrays["position_"+key].shape == (mp, 3),
                 "selected position rows do not match the unique original points")
    for key in METRIC_KEYS:
        _require(arrays["metric_"+key].shape == (mr,),
                 "saved radial metric shape differs")
    if identity.get("height_samples_available") is True:
        for key in HEIGHT_KEYS:
            _require(arrays["height_"+key].shape == (mr,),
                     "saved radial height provenance shape differs")
    _require(identity.get("row_count") == len(ids)
             and identity.get("saved_point_count") == mp
             and identity.get("saved_metric_radial_count") == mr
             and identity.get("original_point_count") == len(r)*len(th),
             "selected source counts differ from actual saved arrays")
    result = {
        "schema": POLICY+"-bound-selected-ordinary",
        "identity": copy.deepcopy(identity),
        "binding_sha256": expected_binding_sha256,
        "arrays": arrays,
        "source_configuration": copy.deepcopy(cfg),
        "field_definition_sha256": field.definition_sha256,
        "method_definition_sha256": digest(definition()),
        "selected_only_not_field_bind_ordinary": True}
    _wall(wall)
    return result


def _validate_selected_bound(field, state168, radial, theta, row_ids, bound, cfg, side):
    q = field.validate_state(state168)
    r, th = _validate_grid(radial, theta)
    _config(cfg, side)
    _require(isinstance(bound, dict)
             and bound.get("schema") == POLICY+"-bound-selected-ordinary",
             "the genuine selected-only runtime binding is required")
    identity, arrays = bound.get("identity"), bound.get("arrays")
    _require(isinstance(identity, dict) and isinstance(arrays, dict)
             and bound.get("binding_sha256") == digest(identity)
             and bound.get("method_definition_sha256") == digest(definition())
             and identity.get("context") == _physical_context(field, q, r, th, cfg, side)
             and bound.get("source_configuration") == cfg,
             "selected ordinary current-state or method binding changed")
    _require(_manifest(arrays) == identity.get("arrays"),
             "selected arrays changed after their owner-bound export")
    _require(_same(arrays["state168"], q) and _same(arrays["radial"], r)
             and _same(arrays["theta"], th),
             "selected current point or grid bytes changed")
    ids, groups, points = _row_ids(row_ids, len(r), len(th))
    _require(np.all(np.isin(ids, arrays["pool_row_ids"])),
             "requested original row was not saved in this actual pool; no zero fill is permitted")
    location = np.searchsorted(arrays["point_ids"], points)
    _require(np.all(location < len(arrays["point_ids"]))
             and np.array_equal(arrays["point_ids"][location], points),
             "selected original physical point is absent")
    return q, r, th, arrays


def current_168_selected_rows_from_selected_geometry(
        field, state168, radial, theta, row_ids, bound, cfg, *,
        side, owned_width=16, wall=None, need_observables=True):
    """Return a NEW J168 using only paid selected ordinary input arrays.

    bound is the explicit bind_selected_current168_geometry runtime record.
    It is not accepted by field.validate_bound and contains no full-grid
    position arrays.  This method does new, separately charged derivative
    work.  No ordinary geometry is evaluated and no old final J is reused.

    Original row IDs are group*(Nr*Ntheta)+ri*Ntheta+ti.  Caller order and
    duplicates are preserved, including endpoints and rows outside the new
    body support.  Every basis keeps its own original zero extension;
    there is no common new9 support filter.  observables, when requested, contains only
    input groups0/1 in their input order:
      row_positions, row_ids, groups, e, f, de, df
    with de/df shape (number_of_metric_rows,168).  It is None otherwise.
    """
    started = time.monotonic()
    _wall(wall)
    _context(field)
    q, r, th, ordinary = _validate_selected_bound(
        field, state168, radial, theta, row_ids, bound, cfg, side)
    width = _width(owned_width)
    if side not in (-1, 1) or not isinstance(cfg, dict):
        raise ValueError("original signed side and scalar configuration required")
    if (cfg.get("metric_proposal_policy") != SPECTRAL_POLICY
            or cfg.get("metric_proposal_epsilon_exact") != EPSILON_EXACT):
        raise ValueError("the original frozen spectral row policy is required")
    if not isinstance(need_observables, (bool, np.bool_)):
        raise ValueError("need_observables must be boolean")
    nr, nt = len(r), len(th)
    ids, groups, points = _row_ids(row_ids, nr, nt)
    positions = (np.flatnonzero(groups < 2) if need_observables
                 else np.zeros(0, dtype=np.int64))
    slots = np.full(len(ids), -1, dtype=np.int64)
    slots[positions] = np.arange(len(positions))
    obs_e = np.empty(len(positions), dtype=float)
    obs_f = np.empty(len(positions), dtype=float)
    obs_de = np.empty((len(positions), N), dtype=float)
    obs_df = np.empty((len(positions), N), dtype=float)
    J = np.empty((len(ids), N), dtype=float)
    covered = np.zeros(len(ids), dtype=bool)
    radial_ids = np.unique(points//nt)
    diagnostics = _base_diagnostics(field, q, r, th, bound["binding_sha256"])
    diagnostics.update(
        policy=POLICY,
        purpose="complete-current168-selected-original-scalar-J-from-paid-selected-ordinary",
        derivative_method_definition_sha256=digest(definition()),
        selected_only_input_binding_sha256=bound["binding_sha256"],
        original_ordinary_binding_sha256=
            bound["identity"]["source_ordinary_binding"]["binding_sha256"],
        exported_pool_version=bound["identity"]["pool_version"],
        exported_pool_row_ids=bound["identity"]["arrays"]["pool_row_ids"],
        saved_point_ids=bound["identity"]["arrays"]["point_ids"],
        saved_metric_radial_ids=bound["identity"]["arrays"]["metric_radial_ids"],
        new_paid_selected_J_not_a_reused_original_J=True,
        no_fabricated_full_grid_position_array=True,
        original_height_samples_are_provenance_only=True,
        rows=len(ids), row_ids=array_binding(ids),
        configuration_sha256=digest(cfg), side=int(side),
        need_observables=bool(need_observables),
        metric_row_count=len(positions),
        three_original_angular_families_per_batch=True,
        shared_new_modes_verified_once_per_call=False)

    for begin in range(0, len(radial_ids), width):
        _wall(wall)
        owned = radial_ids[begin:begin+width]
        selected = np.flatnonzero(np.isin(points//nt, owned))
        global_ri = points[selected]//nt
        ti = points[selected] % nt
        query = np.unique(np.r_[0, owned, nr-1])
        ri = np.searchsorted(query, global_ri)
        second = bool(np.any(groups[selected] >= 7))
        tick = time.monotonic()
        body_grid, fields, frame = field.scalar_frame(q, r[query], th)
        radial_slots = np.searchsorted(ordinary["metric_radial_ids"], query)
        if (np.any(radial_slots >= len(ordinary["metric_radial_ids"]))
                or not np.array_equal(ordinary["metric_radial_ids"][radial_slots], query)):
            raise ValueError("the saved selected metric misses an original query radial row")
        point_slots = np.searchsorted(ordinary["point_ids"], points[selected])
        metric = {key: ordinary["metric_"+key][radial_slots] for key in METRIC_KEYS}
        small = {key: ordinary["position_"+key][point_slots] for key in POSITION_KEYS}
        radius = metric["a"][ri]
        diagnostics["scalar_fields_seconds"] += time.monotonic()-tick
        tick = time.monotonic()
        families = _families(body_grid, len(query), nt, verify_shared_modes=(begin == 0))
        diagnostics["basis_seconds"] += time.monotonic()-tick
        diagnostics["shared_new_modes_verified_once_per_call"] = True
        local_metric = ((groups[selected] < 2) if need_observables
                        else np.zeros(len(selected), dtype=bool))
        metric_out = slots[selected[local_metric]]
        if np.any(local_metric):
            U, T = (small[key][local_metric] for key in ("Xs", "T"))
            obs_e[metric_out] = np.sum(U*U, axis=1)-1.
            obs_f[metric_out] = np.sum(U*T, axis=1)

        for family in families:
            name = family["name"]
            modes = family["angular"].shape[1]
            tick = time.monotonic()
            kernels = angular_kernels(
                fields, frame, name, family["angular"], family["angular_first"],
                second=second)
            diagnostics["angular_kernels_seconds"] += time.monotonic()-tick
            diagnostics["family_kernel_count"] += 1
            diagnostics["maximum_angular_modes"] = max(
                diagnostics["maximum_angular_modes"], modes)
            diagnostics["maximum_family_kernel_array_bytes"] = max(
                diagnostics["maximum_family_kernel_array_bytes"],
                sum(int(v.nbytes) for v in kernels.values()))
            tick = time.monotonic()
            virtual = virtual_selected_jets(kernels, ri, ti, metric, second=second)
            data = dict(small)
            data.update({"jac_"+key: value for key, value in virtual.items()})
            local = selected_spectral_parameter_jacobian(
                data, radius, groups[selected], side, cfg)
            diagnostics["scalar_contraction_seconds"] += time.monotonic()-tick
            tick = time.monotonic()
            start, stop = family["start"], family["stop"]
            J[selected, start:stop] = expand_radial_rows(local, family["radial"], ri)
            if family["new_radial"] is not None:
                ns, ne = family["new_start"], family["new_stop"]
                J[selected, ns:ne] = expand_radial_rows(
                    _first_four_virtual(local, modes), family["new_radial"], ri)
            diagnostics["radial_expansion_seconds"] += time.monotonic()-tick
            diagnostics["maximum_virtual_columns"] = max(
                diagnostics["maximum_virtual_columns"], local.shape[1])
            diagnostics["maximum_selected_virtual_jet_bytes"] = max(
                diagnostics["maximum_selected_virtual_jet_bytes"],
                sum(int(v.nbytes) for v in virtual.values()))
            if np.any(local_metric):
                tick = time.monotonic()
                observable = {key: small[key][local_metric] for key in ("Xs", "T")}
                observable.update({
                    "jac_"+key: virtual[key][local_metric] for key in ("Xs", "T")})
                de, df = observable_parameter_jacobians(observable)
                mri = ri[local_metric]
                obs_de[metric_out, start:stop] = expand_radial_rows(
                    de, family["radial"], mri)
                obs_df[metric_out, start:stop] = expand_radial_rows(
                    df, family["radial"], mri)
                if family["new_radial"] is not None:
                    ns, ne = family["new_start"], family["new_stop"]
                    obs_de[metric_out, ns:ne] = expand_radial_rows(
                        _first_four_virtual(de, modes), family["new_radial"], mri)
                    obs_df[metric_out, ns:ne] = expand_radial_rows(
                        _first_four_virtual(df, modes), family["new_radial"], mri)
                diagnostics["observable_contraction_seconds"] += time.monotonic()-tick
            del kernels, virtual, data, local

        tick = time.monotonic()
        height = _height_six(field, body_grid, r[query], ri, second=second)
        data = dict(small)
        data.update({"jac_"+key: value for key, value in height.items()})
        hrows = selected_spectral_parameter_jacobian(
            data, radius, groups[selected], side, cfg)
        J[selected, 154:159] = hrows[:, :5]
        J[selected, 167:168] = hrows[:, 5:6]
        if np.any(local_metric):
            observable = {key: small[key][local_metric] for key in ("Xs", "T")}
            observable.update({
                "jac_"+key: height[key][local_metric] for key in ("Xs", "T")})
            de, df = observable_parameter_jacobians(observable)
            obs_de[metric_out, 154:159] = de[:, :5]
            obs_df[metric_out, 154:159] = df[:, :5]
            obs_de[metric_out, 167:168] = de[:, 5:6]
            obs_df[metric_out, 167:168] = df[:, 5:6]
        diagnostics["height_columns_seconds"] += time.monotonic()-tick
        diagnostics["maximum_selected_virtual_jet_bytes"] = max(
            diagnostics["maximum_selected_virtual_jet_bytes"],
            sum(int(v.nbytes) for v in height.values()))
        diagnostics["batch_count"] += 1
        diagnostics["maximum_query_radial_rows"] = max(
            diagnostics["maximum_query_radial_rows"], len(query))
        covered[selected] = True
        del fields, frame, body_grid, small, families, height, data, hrows

    arrays = (J, obs_e, obs_f, obs_de, obs_df)
    if not np.all(covered) or any(not np.all(np.isfinite(v)) for v in arrays):
        raise FloatingPointError("incomplete or nonfinite complete-current168 selected derivatives")
    observables = None
    if need_observables:
        observables = {
            "row_positions": positions.copy(), "row_ids": ids[positions].copy(),
            "groups": groups[positions].copy(),
            "e": obs_e, "f": obs_f, "de": obs_de, "df": obs_df}
        for value in observables.values():
            value.setflags(write=False)
        diagnostics["observables_array_bindings"] = {
            key: array_binding(value) for key, value in observables.items()}
    J.setflags(write=False)
    diagnostics.update(
        J168=array_binding(J),
        returned_J_bytes=int(J.nbytes),
        total_seconds=time.monotonic()-started,
        complete=True)
    _wall(wall)
    return J, diagnostics, observables


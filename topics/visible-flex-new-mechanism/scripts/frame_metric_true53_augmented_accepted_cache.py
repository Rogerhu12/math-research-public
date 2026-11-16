#!/usr/bin/env python3
"""Export the newly accepted ordinary first-jet cache without reevaluation.

Import-only helper. It never calls geometry, physical_geometry, fine_decision,
an objective callback, a field/grid builder, target_frame, a periodic operator,
a JVP/Jacobian, or geometry_values. T is the original cached frame T, not Xt/a.
e/f are the original cached ordinary arrays, never reconstructed from U/T.

All extraction, copying, hashing and JSON-list conversion remain inside the
caller's already-running augmented-direction clock. There is no new scientific
value/JVP allowance, no file write, and no direct stdout emission.
"""
from __future__ import annotations

import copy
import time
from typing import Any

import numpy as np

from frame_entry_body_subspace import array_digest
from frame_height_null_coordinates import digest
from frame_metric_true53_augmented_scope import (
    POLICY, SOURCE_ACCEPTED_INDEX, SOURCE_CFG_SHA,
    SOURCE_FIELD_SHA, SOURCE_PHYSICAL_SHA, require)

SCHEMA = POLICY + "-new-accepted-ordinary-first-jet-cache-v1"
LABELS = ("coarse", "fine")
GRID_SHAPES = {"coarse": (160, 384), "fine": (160, 768)}
ARRAY_NAMES = ("U", "T", "e", "f", "radial", "theta")
MAX_SELECTED_RAW_BYTES = 13 * 1024 * 1024

SOURCE_OPERATIONS = {
    "frame": (
        "DirectReferenceFiveHeightField._single_geometry: "
        "T=frame['T']; _null_height_update retains that exact array"),
    "coarse": (
        "CurvatureExchangeObjective.physical_geometry: POSITION_JETS includes T; "
        "cache retains Xs/T and geometry_values e/f"),
    "fine": (
        "MetricRecoveryObjective.fine_decision: data retains Xs/T; "
        "data.update(e=val['e'],f=val['f'],eta=val['eta'])"),
    "accepted_owner": (
        "SOCObjective.accepted_point: accepted_cache['coarse']=geometry_cache; "
        "accepted_cache['fine']=fine_cache"),
    "physical_identity": (
        "FiveHeightField.identity delegates only to coordinates.physical_identity; "
        "no metric/field/geometry evaluation"),
}


def _check(ledger: Any) -> None:
    require(ledger is not None and callable(getattr(ledger, "check", None)),
            "the current augmented-direction clock is required")
    ledger.check()


def _same_array_bits(left: Any, right: Any) -> bool:
    a, b = np.asarray(left), np.asarray(right)
    return a.dtype.str == b.dtype.str and a.shape == b.shape and a.tobytes() == b.tobytes()


def _float64(value: Any, shape: tuple[int, ...], name: str) -> np.ndarray:
    a = np.asarray(value)
    require(a.dtype == np.dtype(np.float64) and a.shape == shape,
            "existing native binary64 cache shape differs: " + name)
    # Original actual acceptance already checked finite complete arrays.
    # No redundant all-grid scientific value calculation occurs here.
    return a


def _counter_snapshot(objective: Any, ledger: Any) -> dict[str, Any]:
    statistics = getattr(objective.problem, "_direct_statistics", None)
    require(isinstance(statistics, dict),
            "the existing direct-reference ordinary field is required")
    counts = getattr(ledger, "counts", {})
    return {
        "geometry_calls_started": statistics.get("geometry_calls_started"),
        "geometry_calls_completed": statistics.get("geometry_calls_completed"),
        "geometry_calls_failed": statistics.get("geometry_calls_failed"),
        "coarse_ordinary_values": getattr(objective, "geometry_evaluations", None),
        "fine_ordinary_values": getattr(objective, "fine_evaluations", None),
        "actual_grid_values": counts.get("actual_grid_values"),
        "pair_first_jet_jvps": counts.get("pair_first_jet_jvps"),
        "new_attainer_gradients": counts.get("new_attainer_gradients"),
    }


def _array_metadata(a: np.ndarray) -> dict[str, Any]:
    return {"shape": list(a.shape), "dtype": str(a.dtype),
            "dtype_str": a.dtype.str, "raw_bytes": int(a.nbytes),
            "array_sha256": array_digest(a),
            "array_hash_contract": "frame_entry_body_subspace.array_digest"}


def _owner_cache(objective: Any, state: np.ndarray) -> tuple[dict[str, Any],
                                                           dict[str, Any], dict[str, str]]:
    saved = getattr(objective, "accepted_cache", None)
    if isinstance(saved, dict):
        require("state" in saved and _same_array_bits(saved["state"], state),
                "accepted cache owner is not the new accepted physical state")
        coarse = saved.get("coarse")
        fine = saved.get("fine")
        require(isinstance(coarse, dict) and isinstance(fine, dict),
                "accepted owner must retain both complete ordinary value caches")
        paths = {"coarse": "objective.accepted_cache['coarse']",
                 "fine": "objective.accepted_cache['fine']['data']"}
    else:
        # A caller retaining the exact current accepted caches may use them,
        # without triggering the objective's restore-or-evaluate methods.
        coarse = getattr(objective, "geometry_cache", None)
        fine = getattr(objective, "fine_cache", None)
        require(isinstance(coarse, dict) and isinstance(fine, dict),
                "both existing accepted-state caches are required")
        paths = {"coarse": "objective.geometry_cache",
                 "fine": "objective.fine_cache['data']"}
    require("state" in coarse and _same_array_bits(coarse["state"], state),
            "coarse cache state differs from accepted state")
    require("state" in fine and _same_array_bits(fine["state"], state),
            "fine cache wrapper state differs from accepted state")
    require(isinstance(fine.get("data"), dict),
            "fine ordinary cache data is unavailable")
    return coarse, fine["data"], paths


def _extract_accepted_first_jet_snapshots(
        objective: Any, ledger: Any, *,
        source_identity: dict[str, Any] | None = None,
        capture: dict[str, Any] | None = None) -> dict[str, Any]:
    """Copy only existing new accepted54 U/T/e/f and grids, with exact bindings.

    Returns metadata plus ndarray snapshots. If no new point was accepted,
    available=False and no arrays are read/exported. Missing accepted caches
    raise; no implicit base/geometry reconstruction is possible.
    """
    started = time.monotonic()
    progress = capture if capture is not None else {}
    progress.update(schema=SCHEMA, status="started",
                    ordinary_geometry_calls=0, JVP_calls=0,
                    scientific_values_recomputed=0,
                    serialized_dense_two_jets_or_Jacobians=False)
    try:
        _check(ledger)
        points = getattr(objective, "accepted_iterates", None)
        require(isinstance(points, list) and bool(points),
                "the original accepted-point receipts are required")
        point = points[-1]
        require(isinstance(point, dict), "accepted-point receipt must be an object")
        index = point.get("accepted_index")
        if index == SOURCE_ACCEPTED_INDEX:
            progress.update(status="no-new-accepted-point",
                            elapsed_seconds=time.monotonic() - started)
            return {
                "available": False, "schema": SCHEMA,
                "status": "no-new-accepted-point",
                "source_accepted_index": SOURCE_ACCEPTED_INDEX,
                "arrays": {}, "metadata": copy.deepcopy(progress)}
        require(index == SOURCE_ACCEPTED_INDEX + 1 and len(points) == 2,
                "only the one newly accepted54 point may be exported")
        require(point.get("physical_state_sha256") != SOURCE_PHYSICAL_SHA,
                "the paid source53 point may not be rebuilt or relabeled")
        require("independent_coordinates_binary64" in point,
                "the new accepted record must contain all independent159 coefficients")
        state = np.asarray(point["independent_coordinates_binary64"], dtype=np.float64)
        require(state.shape == (159,), "new accepted159 state required")
        field = objective.problem
        require(getattr(field, "_direct_adapter_sha256", None) == SOURCE_FIELD_SHA,
                "ordinary direct-field binding changed")
        require(digest(objective.cfg) == SOURCE_CFG_SHA,
                "the original mathematical configuration changed")
        # This is only the exact-rational coefficient identity map.
        physical_identity = field.identity(state)
        physical_sha = digest(physical_identity)
        require(physical_sha == point["physical_state_sha256"],
                "accepted coefficient identity differs from its original receipt")
        before = _counter_snapshot(objective, ledger)
        coarse, fine, owner_paths = _owner_cache(objective, state)
        data_by_grid = {"coarse": coarse, "fine": fine}
        arrays: dict[str, dict[str, np.ndarray]] = {}
        grids: dict[str, dict[str, Any]] = {}
        raw_bytes = 0
        for label in LABELS:
            _check(ledger)
            data = data_by_grid[label]
            nr, nt = GRID_SHAPES[label]
            require(all(name in data for name in
                        ("Xs", "T", "e", "f", "radial", "theta")),
                    "an original required array is absent; no recovery is allowed: " + label)
            U = _float64(data["Xs"], (nr, nt, 3), label + ".Xs")
            T = _float64(data["T"], (nr, nt, 3), label + ".T")
            e = _float64(data["e"], (nr, nt), label + ".e")
            f = _float64(data["f"], (nr, nt), label + ".f")
            radial = _float64(data["radial"], (nr,), label + ".radial")
            theta = _float64(data["theta"], (nt,), label + ".theta")
            require(_same_array_bits(radial, objective.radial),
                    "the cached original radial chart differs")
            theta_owner = objective.theta if label == "coarse" else objective.fine_theta
            require(_same_array_bits(theta, theta_owner),
                    "the cached original angular array differs")
            candidates = {
                "U": U, "T": T,
                # View-only reshape keeps radial-major/angular-minor binary64
                # order and matches the original model's complete_base_e_f.
                "e": e.reshape(-1), "f": f.reshape(-1),
                "radial": radial, "theta": theta}
            arrays[label] = {}
            meta = {}
            for name in ARRAY_NAMES:
                _check(ledger)
                a = np.array(candidates[name], copy=True, order="C")
                a.setflags(write=False)
                raw_bytes += int(a.nbytes)
                require(raw_bytes <= MAX_SELECTED_RAW_BYTES,
                        "selected accepted cache exceeds declared raw-byte cap")
                arrays[label][name] = a
                meta[name] = _array_metadata(a)
            grids[label] = {
                "label": label, "Nr": nr, "Ntheta": nt,
                "complete_point_count": nr * nt,
                "flattening": "radial-major/angular-minor",
                "cache_owner": owner_paths[label],
                "U_source": "existing ordinary Xs including accepted null-height update",
                "T_source": "existing original frame T retained in ordinary cache",
                "e_f_source": "existing ordinary geometry_values arrays, without recomputation",
                "original_e_f_shapes": {"e": [nr, nt], "f": [nr, nt]},
                "exported_e_f_shapes": {"e": [nr * nt], "f": [nr * nt]},
                "theta_not_reconstructed_or_reassociated": True,
                "arrays": meta}
        require(_same_array_bits(arrays["coarse"]["radial"], arrays["fine"]["radial"]),
                "the two existing radial charts differ")
        _check(ledger)
        after = _counter_snapshot(objective, ledger)
        require(before == after,
                "accepted cache extraction changed a geometry/JVP/value counter")
        state_copy = state.copy()
        state_copy.setflags(write=False)
        binding = {
            "policy": POLICY, "accepted_index": index,
            "physical_state_sha256": physical_sha,
            "independent159_array_sha256": array_digest(state_copy),
            "coordinate_definition_sha256": field.coordinate_definition_sha256,
            "original_cfg_sha256": SOURCE_CFG_SHA,
            "ordinary_field_evaluation_sha256": SOURCE_FIELD_SHA,
            "objective_evaluation_sha256": getattr(objective, "evaluation_sha256", None),
            "source_identity": copy.deepcopy(source_identity or {}),
            "grid_array_sha256": {
                label: {name: grids[label]["arrays"][name]["array_sha256"]
                        for name in ARRAY_NAMES} for label in LABELS}}
        binding_sha = digest(binding)
        progress.update(
            status="complete", accepted_index=index,
            physical_state_sha256=physical_sha,
            binding_sha256=binding_sha,
            selected_array_raw_bytes=raw_bytes,
            state_array_raw_bytes=int(state_copy.nbytes),
            elapsed_seconds=time.monotonic() - started,
            counters_before=before, counters_after=after,
            zero_geometry_JVP_or_ordinary_value_recalculation=True)
        metadata = {
            "schema": SCHEMA, "status": "complete", "available": True,
            "binding": binding, "binding_sha256": binding_sha,
            "accepted_index": index, "physical_state_sha256": physical_sha,
            "grids": grids, "selected_array_raw_bytes": raw_bytes,
            "state_array_raw_bytes": int(state_copy.nbytes),
            "maximum_selected_array_raw_bytes": MAX_SELECTED_RAW_BYTES,
            "source_operations": copy.deepcopy(SOURCE_OPERATIONS),
            "e_f_are_paid_actual_values_not_directional_predictions": True,
            "T_is_not_recovered_by_dividing_Xt": True,
            "no_e_f_recomputed_from_U_T": True,
            "no_field_or_grid_or_height_primitive_restoration": True,
            "positions_curvature_two_jets_and_Jacobians_not_exported": True,
            "no_old_cache_or_p53_state_is_relabelled_as_accepted54": True,
            "shared_clock_charges_copy_hash_and_serialization": True,
            "new_value_or_JVP_allowance": 0,
            "progress": copy.deepcopy(progress)}
        return {"available": True, "schema": SCHEMA,
                "status": "complete", "state": state_copy,
                "arrays": arrays, "metadata": metadata}
    except Exception as error:
        progress.update(status="failed", elapsed_seconds=time.monotonic() - started,
                        error={"type": type(error).__name__, "message": str(error)})
        raise


def accepted_first_jet_cache_record(
        extracted: dict[str, Any], ledger: Any) -> dict[str, Any]:
    """JSON-safe stdout payload only; do not print/write it from this module.

    Uses the original _array_payload spelling (values/shape/dtype/array_sha256)
    without importing the legacy model. It serializes existing snapshots and
    hashes already computed at extraction. Root audit owns the single CACHE
    emission, exact JSON-byte/hash receipt, and whole-log size limit.
    """
    started = time.monotonic()
    _check(ledger)
    require(isinstance(extracted, dict) and extracted.get("schema") == SCHEMA,
            "the accepted-only extracted cache is required")
    if not extracted.get("available"):
        return {"schema": SCHEMA, "available": False,
                "status": extracted.get("status"),
                "metadata": copy.deepcopy(extracted.get("metadata", {}))}
    metadata = copy.deepcopy(extracted["metadata"])
    require(metadata.get("status") == "complete",
            "only complete accepted-cache extraction may be serialized")
    arrays = extracted["arrays"]
    grid_payload = {}
    for label in LABELS:
        require(set(arrays[label]) == set(ARRAY_NAMES),
                "unexpected accepted cache payload keys")
        grid_payload[label] = {}
        for name in ARRAY_NAMES:
            _check(ledger)
            a = arrays[label][name]
            m = metadata["grids"][label]["arrays"][name]
            require(isinstance(a, np.ndarray) and not a.flags.writeable
                    and list(a.shape) == m["shape"] and str(a.dtype) == m["dtype"],
                    "the original immutable accepted snapshot changed")
            grid_payload[label][name] = {
                "values": a.tolist(), "shape": m["shape"], "dtype": m["dtype"],
                "array_sha256": m["array_sha256"]}
    state = extracted["state"]
    require(isinstance(state, np.ndarray) and state.shape == (159,)
            and not state.flags.writeable, "immutable accepted159 state required")
    _check(ledger)
    return {
        "schema": SCHEMA, "available": True, "status": "complete",
        "binding": metadata["binding"],
        "binding_sha256": metadata["binding_sha256"],
        "accepted_independent159": {
            "values": state.tolist(), "shape": [159], "dtype": str(state.dtype),
            "array_sha256": metadata["binding"]["independent159_array_sha256"]},
        "grids": grid_payload, "metadata": metadata,
        "serialization_seconds_before_outer_JSON_encoding": time.monotonic() - started,
        "original_plain_stdout_only_no_artifact_or_cross_run_cache": True,
        "this_record_does_not_contain_any_selected_or_dense_Jacobian": True}


def extract_accepted_first_jet_cache(
        objective: Any, *, ledger: Any = None,
        source_identity: dict[str, Any] | None = None,
        capture: dict[str, Any] | None = None) -> dict[str, Any] | None:
    """The audit's one-call JSON-safe interface; None means no new acceptance.

    Root emits the return value once under the second CACHE record with
    kind='accepted-point-paid-geometry'. Its literal receipt is stored in
    COMPLETE/future checkpoint. The root emitter alone enforces the shared
    78 MiB mathematical-stdout ceiling; this helper never emits any output.
    """
    owner = ledger if ledger is not None else getattr(objective, "positive_ledger", None)
    snapshots = _extract_accepted_first_jet_snapshots(
        objective, owner, source_identity=source_identity, capture=capture)
    if not snapshots["available"]:
        return None
    return accepted_first_jet_cache_record(snapshots, owner)

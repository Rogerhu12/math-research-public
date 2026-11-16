#!/usr/bin/env python3
"""Selected current168 metric first jets from an already bound U/T cache.

Import-only.  This module computes only e,f and their requested parameter
rows.  It does not call ordinary geometry, selected scalar/curvature rows,
an old159 Jacobian, a solver, or any development suite.  The calling new task
owns all input restoration, started/failed counts and scientific wall time.

The first-jet binding is the published current168 binding, with the actual
state/grid/reference and paid U,T,e,f,a,a_s.  No X, Xss, Xst, Xtt, center or
a_ss is required.  Original metric row order, repetitions and branch IDs
are retained.  Only the requested m-by-168 de/df matrices are materialized;
there is no full-grid-by-168 derivative construction.
"""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_complete_body_extension168 import (
    INDEPENDENT_COUNT, POLICY as FIELD_POLICY, array_binding)
from frame_complete_body_extension168_joint_selected import (
    POLICY as CURRENT168_POLICY, _validate_first_jets, _width, _wall,
    _families, _first_four_virtual, _row_ids, _finite, _current_identity)
from frame_selected_row_radial_jacobian import angular_kernels, expand_radial_rows
from frame_metric_affine_spectral_model import observable_parameter_jacobians


POLICY = "same-fixed-g-complete-body168-metric-only-selected-v1"
N = INDEPENDENT_COUNT


def definition():
    return {
        "schema": POLICY,
        "field_policy": FIELD_POLICY,
        "accepted_first_jet_binding_policy": CURRENT168_POLICY,
        "independent_columns": 168,
        "physical_columns": 172,
        "column_layout": {
            "old_u": [0, 81], "old_v_without_Q": [81, 153],
            "original_normalized_Q": [153, 154],
            "old_exact_null_heights": [154, 159],
            "new_alpha": [159, 163], "new_beta": [163, 167],
            "new_gamma": [167, 168]},
        "input_metric_groups": [0, 1],
        "row_identity": "group*(Nr*Ntheta)+ri*Ntheta+ti",
        "original_row_order_and_repetitions_retained": True,
        "no_support_or_endpoint_filter": True,
        "baseline_fields": ["U", "T", "e", "f"],
        "required_fixed_metric_fields": ["a", "a_s"],
        "parameter_kernel_order": 1,
        "angular_families": ["current u:9", "current v:8", "current Q:1"],
        "maximum_full_angle_parameter_axis": 9,
        "maximum_selected_virtual_parameter_axis": 27,
        "virtual_Xs_coefficients": ["a_s*P0+a*P1", "a*P0", "0"],
        "virtual_T_coefficients": ["F0", "0", "0"],
        "metric_contraction":
            "de=2*U.dot(dU);df=T.dot(dU)+U.dot(dT)",
        "radial_expansion": "R and Rprime only; Rsecond coefficient is structurally zero",
        "structural_zero_is_not_a_second_order_geometry_formula": True,
        "height_six":
            "five original exact-null speed columns plus complete new gamma speed",
        "full_circle_primitive_before_angle_selection": True,
        "ordinary_geometry_calls_inside_module": 0,
        "old_final159_J_reuse_calls": 0,
        "selected_hard_or_curvature_row_calls": 0,
        "full_grid168_parameter_tensors": 0,
        "position_two_jets_read": 0,
        "caller_owns_all_started_failed_counts_and_wall_time": True,
        "not_a_metric_target_or_actual_acceptance_gate": True}


def implementation_hashes():
    root = Path(__file__).parent
    names = (
        Path(__file__).name,
        "frame_complete_body_extension168.py",
        "frame_complete_body_extension168_joint_selected.py",
        "frame_selected_row_radial_jacobian.py",
        "frame_metric_affine_spectral_model.py",
        "frame_height_null_coordinates.py")
    return {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
            for name in names}


def _virtual_metric_jets(kernels, ri, ti, a, a_s):
    """Only dU,dT at selected points; no location or second-order arrays.

    For one original angular family and a radial coefficient R:
      dT = R*F0,
      dU = R*(a_s*P0+a*P1) + Rprime*a*P0.
    The three virtual slots match the published radial expansion exactly;
    the third is zero because these observables contain no Rsecond.
    """
    ri = np.asarray(ri, dtype=np.int64)
    ti = np.asarray(ti, dtype=np.int64)
    f0, p0, p1 = (np.asarray(kernels[key], dtype=float)[ri, ti]
                   for key in ("F0", "P0", "P1"))
    if (f0.ndim != 3 or p0.shape != f0.shape or p1.shape != f0.shape
            or f0.shape[:2] != (len(ri), 3)):
        raise ValueError("the original selected full-circle first kernels are required")
    radius = _finite(a, (len(ri),), "selected fixed a")[:, None, None]
    first = _finite(a_s, (len(ri),), "selected fixed a_s")[:, None, None]
    zero = np.zeros_like(f0)
    dU0, dU1 = first*p0+radius*p1, radius*p0
    dU = np.concatenate((dU0, dU1, zero), axis=2)
    dT = np.concatenate((f0, zero, zero), axis=2)
    if not np.all(np.isfinite(dU)) or not np.all(np.isfinite(dT)):
        raise FloatingPointError("nonfinite selected metric first kernels")
    return dU, dT


def _height_observables(field, body_grid, radial, ri, U, T):
    """Original exact height speed only; no primitive or b_s is evaluated."""
    null_speed = _finite(
        field.original_field.null_basis.values(radial),
        (len(radial), 5), "five original exact-null speeds")
    gamma_speed = _finite(
        body_grid.radial_body["height"]["b"],
        (len(radial),), "complete new gamma speed")
    speed = np.column_stack((null_speed[ri], gamma_speed[ri]))
    de = 2.*U[:, 2, None]*speed
    df = T[:, 2, None]*speed
    if not np.all(np.isfinite(de)) or not np.all(np.isfinite(df)):
        raise FloatingPointError("nonfinite selected exact-null/gamma metric rows")
    return de, df


def current_168_metric_selected_rows(
        field, state168, radial, theta, original_metric_ids, first_jet_bound, *,
        owned_width=16, wall=None):
    """Return (observables, diagnostics), using only already bound first jets.

    observables contains row_positions,row_ids,groups,e,f,de,df; de/df have
    shape (m,168), and m is exactly the number of requested original IDs.
    Both groups0/1 are accepted, including endpoints and repetitions.  The
    raw e/f derivatives are the same geometric quantities for both groups;
    the caller applies the original phi branch only after preserving its ID.

    The first_jet_bound is produced by the already published
    bind_current_168_first_jets.  Its underlying owner must keep the paid
    arrays immutable.  This call validates the same field/state/grid identity
    without calling the ordinary-binding path that requires position2 jets.

    Scalar frame coefficients and the three angular first-kernel families
    are constructed on at most owned_width+2 radial rows.  Baseline U/T/e/f
    are always read from the supplied cache, never replaced by reconstructed
    positions or a newly evaluated ordinary.  The old nine-radial basis
    metadata includes its second jet, but that jet has zero coefficient in
    every returned metric row.
    """
    started = time.monotonic()
    _wall(wall)
    q, r, th, baseline = _validate_first_jets(
        field, state168, radial, theta, first_jet_bound)
    width = _width(owned_width)
    nr, nt = len(r), len(th)
    ids, groups, points = _row_ids(original_metric_ids, nr, nt)
    if np.any(groups >= 2):
        raise ValueError("only original metric groups0/1 are accepted by this API")
    m = len(ids)
    global_ri_all, ti_all = points//nt, points % nt
    # Retain the literal already-bound current e/f arrays at these source IDs.
    obs_e = np.asarray(baseline["e"])[global_ri_all, ti_all].copy()
    obs_f = np.asarray(baseline["f"])[global_ri_all, ti_all].copy()
    de, df = np.empty((m, N), dtype=float), np.empty((m, N), dtype=float)
    covered = np.zeros(m, dtype=bool)
    columns_written = np.zeros(N, dtype=bool)
    radial_ids = np.unique(global_ri_all)
    diagnostics = {
        "schema": POLICY+"-diagnostics",
        "policy": POLICY,
        "definition": definition(),
        "inherited_current_field_identity": _current_identity(field, q, r, th),
        "input_first_jet_binding_sha256": first_jet_bound["binding_sha256"],
        "input_source_receipt": copy.deepcopy(
            first_jet_bound["identity"].get("source_receipt")),
        "input_array_bindings": copy.deepcopy(first_jet_bound["identity"]["arrays"]),
        "input_metric_array_bindings": copy.deepcopy(
            first_jet_bound["identity"]["metric_arrays"]),
        "rows": m, "row_ids": array_binding(ids),
        "current_new9_nonzero": bool(np.any(q[159:] != 0.)),
        "row_order_and_repetitions_retained": True,
        "batch_count": 0, "family_kernel_count": 0,
        "maximum_query_radial_rows": 0,
        "maximum_angular_modes": 0,
        "maximum_virtual_columns": 0,
        "maximum_family_kernel_array_bytes": 0,
        "maximum_selected_metric_work_bytes": 0,
        "scalar_fields_seconds": 0.,
        "basis_seconds": 0.,
        "angular_kernels_seconds": 0.,
        "metric_contraction_seconds": 0.,
        "radial_expansion_seconds": 0.,
        "height_columns_seconds": 0.,
        "ordinary_geometry_calls_inside_module": 0,
        "old_final159_J_reuse_calls": 0,
        "hard_or_curvature_selected_calls": 0,
        "position_two_jets_read": 0,
        "full_grid168_parameter_tensors": 0,
        "a_ss_not_required": True,
        "caller_owns_all_scientific_costs": True}

    for begin in range(0, len(radial_ids), width):
        _wall(wall)
        owned = radial_ids[begin:begin+width]
        selected = np.flatnonzero(np.isin(global_ri_all, owned))
        global_ri = global_ri_all[selected]
        ti = ti_all[selected]
        query = np.unique(np.r_[0, owned, nr-1])
        ri = np.searchsorted(query, global_ri)
        U = np.asarray(baseline["U"])[global_ri, ti]
        T = np.asarray(baseline["T"])[global_ri, ti]
        a = np.asarray(baseline["metric"]["a"])[global_ri]
        a_s = np.asarray(baseline["metric"]["a_s"])[global_ri]
        tick = time.monotonic()
        body_grid, fields, frame = field.scalar_frame(q, r[query], th)
        diagnostics["scalar_fields_seconds"] += time.monotonic()-tick
        _wall(wall)
        tick = time.monotonic()
        families = _families(
            body_grid, len(query), nt, verify_shared_modes=(begin == 0))
        diagnostics["basis_seconds"] += time.monotonic()-tick

        for family in families:
            _wall(wall)
            modes = family["angular"].shape[1]
            tick = time.monotonic()
            kernels = angular_kernels(
                fields, frame, family["name"],
                family["angular"], family["angular_first"], second=False)
            diagnostics["angular_kernels_seconds"] += time.monotonic()-tick
            diagnostics["family_kernel_count"] += 1
            diagnostics["maximum_angular_modes"] = max(
                diagnostics["maximum_angular_modes"], modes)
            diagnostics["maximum_family_kernel_array_bytes"] = max(
                diagnostics["maximum_family_kernel_array_bytes"],
                sum(int(value.nbytes) for value in kernels.values()))
            _wall(wall)
            tick = time.monotonic()
            dU, dT = _virtual_metric_jets(kernels, ri, ti, a, a_s)
            local_de, local_df = observable_parameter_jacobians(
                {"Xs": U, "T": T, "jac_Xs": dU, "jac_T": dT})
            diagnostics["metric_contraction_seconds"] += time.monotonic()-tick
            diagnostics["maximum_virtual_columns"] = max(
                diagnostics["maximum_virtual_columns"], local_de.shape[1])
            diagnostics["maximum_selected_metric_work_bytes"] = max(
                diagnostics["maximum_selected_metric_work_bytes"],
                sum(int(value.nbytes) for value in (dU, dT, local_de, local_df)))
            tick = time.monotonic()
            start, stop = family["start"], family["stop"]
            de[selected, start:stop] = expand_radial_rows(
                local_de, family["radial"], ri)
            df[selected, start:stop] = expand_radial_rows(
                local_df, family["radial"], ri)
            columns_written[start:stop] = True
            if family["new_radial"] is not None:
                ns, ne = family["new_start"], family["new_stop"]
                de[selected, ns:ne] = expand_radial_rows(
                    _first_four_virtual(local_de, modes), family["new_radial"], ri)
                df[selected, ns:ne] = expand_radial_rows(
                    _first_four_virtual(local_df, modes), family["new_radial"], ri)
                columns_written[ns:ne] = True
            diagnostics["radial_expansion_seconds"] += time.monotonic()-tick
            del kernels, dU, dT, local_de, local_df
            _wall(wall)

        tick = time.monotonic()
        height_de, height_df = _height_observables(
            field, body_grid, r[query], ri, U, T)
        de[selected, 154:159] = height_de[:, :5]
        df[selected, 154:159] = height_df[:, :5]
        de[selected, 167:168] = height_de[:, 5:6]
        df[selected, 167:168] = height_df[:, 5:6]
        columns_written[154:159] = True
        columns_written[167] = True
        diagnostics["height_columns_seconds"] += time.monotonic()-tick
        diagnostics["batch_count"] += 1
        diagnostics["maximum_query_radial_rows"] = max(
            diagnostics["maximum_query_radial_rows"], len(query))
        covered[selected] = True
        del body_grid, fields, frame, families, height_de, height_df, U, T, a, a_s
        _wall(wall)

    if (not np.all(covered) or not np.all(columns_written)
            or any(not np.all(np.isfinite(value)) for value in (obs_e, obs_f, de, df))):
        raise FloatingPointError("incomplete or nonfinite selected current168 metric first jets")
    observables = {
        "row_positions": np.arange(m, dtype=np.int64),
        "row_ids": ids.copy(), "groups": groups.copy(),
        "e": obs_e, "f": obs_f, "de": de, "df": df}
    for value in observables.values():
        value.setflags(write=False)
    diagnostics.update(
        observables_array_bindings={key: array_binding(value)
                                   for key, value in observables.items()},
        returned_metric_derivative_bytes=int(de.nbytes+df.nbytes),
        actual_returned_row_count=len(observables["row_ids"]),
        actual_returned_column_count=de.shape[1],
        all_requested_rows_and_current168_columns_written=bool(
            np.all(covered) and np.all(columns_written)),
        total_seconds=time.monotonic()-started,
        complete=True)
    _wall(wall)
    return observables, diagnostics

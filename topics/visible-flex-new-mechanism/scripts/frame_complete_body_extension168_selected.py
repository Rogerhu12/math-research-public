#!/usr/bin/env python3
"""Only the nine genuinely new derivatives of the R490 body168 family.

Import-only.  Reuses the original scalar constraint contraction and complete
angular periodic primitive.  No old159 factorization, optimizer, ordinary
geometry call, tests, or CLI is present.  A caller supplies already bound
complete ordinary arrays and owns every scientific cost.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import time

import numpy as np

from frame_complete_body_extension168 import (
    CompleteBody168Field, EXTRA_COUNT, POSITION_KEYS, POLICY as FIELD_POLICY,
    array_binding)
from frame_selected_row_radial_jacobian import (
    angular_kernels, virtual_selected_jets, expand_radial_rows,
    selected_spectral_parameter_jacobian)
from frame_metric_affine_spectral_model import observable_parameter_jacobians
from frame_height_null_coordinates import digest


POLICY = "same-fixed-g-complete-body168-new-nine-selected-v1"
FIRST_KEYS = ("X", "Xs", "Xt", "T")


def definition():
    return {
        "schema": POLICY,
        "field_policy": FIELD_POLICY,
        "derivative_column_order": ["alpha1", "alpha2", "alpha3", "alpha4",
                                    "beta1", "beta2", "beta3", "beta4", "gamma"],
        "returned_column_count": 9,
        "original159_factorization_calls": 0,
        "ordinary_geometry_calls_inside_derivatives": 0,
        "complete_original_scalar_groups": 11,
        "original_row_order_and_duplicates_retained": True,
        "two_four_mode_angular_families_and_one_height_column": True,
        "original_spectral_scalar_contraction": True,
        "full_current_position_two_jets_used_for_curvature_rows": True,
        "metric_observables": ["e=|Xs|^2-1", "f=Xs dot T",
                               "de=2 Xs dot dXs", "df=T dot dXs+Xs dot dT"],
        "supplied_ordinary_is_not_automatically_a_paid_receipt": True,
        "no_new_reference_or_old159_jacobian_relabeling": True,
    }


def implementation_hashes():
    names = (
        Path(__file__).name, "frame_complete_body_extension168.py",
        "frame_selected_row_radial_jacobian.py",
        "frame_metric_affine_spectral_model.py",
        "frame_entry_single_q.py", "frame_collar_bvp.py")
    return {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in names}


def _width(value):
    if (isinstance(value, (bool, np.bool_))
            or not isinstance(value, (int, np.integer)) or not 1 <= value <= 16):
        raise ValueError("one through sixteen owned radial rows per batch required")
    return int(value)


def _new_height_selected(height, ri, *, second):
    keys = FIRST_KEYS + (("Xss", "Xst", "Xtt") if second else ())
    out = {key: np.zeros((len(ri), 3, 1)) for key in keys}
    for key, name in (("X", "center"), ("Xs", "b"), ("Xss", "b_s")):
        if key in out:
            out[key][:, 2, 0] = np.asarray(height[name])[ri]
    return out


def _diagnostics(bound, state, radial, theta):
    return {
        "policy": POLICY,
        "field_definition_sha256": bound["field_definition_sha256"],
        "coordinate_definition_sha256": bound["coordinate_definition_sha256"],
        "ordinary_binding_sha256": bound["binding_sha256"],
        "state": array_binding(state),
        "radial": array_binding(radial),
        "theta": array_binding(theta),
        "columns": EXTRA_COUNT,
        "batch_count": 0,
        "family_kernel_count": 0,
        "maximum_query_radial_rows": 0,
        "maximum_angular_modes": 4,
        "maximum_virtual_columns": 12,
        "maximum_family_kernel_array_bytes": 0,
        "ordinary_geometry_calls_inside_derivatives": 0,
        "old159_parameter_Jacobian_calls": 0,
        "old159_or163_full_angle_derivative_tensors": 0,
        "complete_current_reference_and_original_periodic_operator": True,
    }


def _metadata_arrays(data):
    return {key: array_binding(value) for key, value in data.items()
            if isinstance(value, np.ndarray)}


def new_nine_selected_rows(field, state, radial, theta, row_ids, bound, cfg, *,
                          side, owned_width=16, wall=None, need_observables=True):
    """Return (J9, diagnostics, observables) in exact caller row order.

    row_ids use the original eleven-group convention: id=group*(Nr*Ntheta)
    +radial_index*Ntheta+theta_index.  Repeated IDs remain repeated.  cfg and
    side have the original selected_spectral_parameter_jacobian semantics.

    observables contains only groups 0 and 1, in their original row positions:
    row_positions, row_ids, groups, e, f, de, df (last derivative axis 9).
    With need_observables=False it returns None.  No ordinary value, old
    derivative, original domain, or old optimizer is evaluated here.
    """
    started = time.monotonic()
    if not isinstance(field, CompleteBody168Field):
        raise ValueError("the explicitly new CompleteBody168Field is required")
    q, r, th, ordinary = field.validate_bound(state, radial, theta, bound)
    width = _width(owned_width)
    if side not in (-1, 1) or not isinstance(cfg, dict):
        raise ValueError("the original signed side and scalar-constraint config are required")
    raw = list(row_ids)
    if any(isinstance(v, (bool, np.bool_))
           or not isinstance(v, (int, np.integer)) for v in raw):
        raise ValueError("original integer row IDs required")
    ids = np.asarray(raw, dtype=np.int64)
    count, nt = len(r)*len(th), len(th)
    if not len(ids) or np.any(ids < 0) or np.any(ids >= 11*count):
        raise ValueError("nonempty original eleven-group row IDs required")
    groups, points = ids//count, ids % count
    positions = np.flatnonzero(groups < 2) if need_observables else np.zeros(0, dtype=np.int64)
    slots = np.full(len(ids), -1, dtype=np.int64)
    slots[positions] = np.arange(len(positions))
    obs_e = np.empty(len(positions))
    obs_f = np.empty(len(positions))
    obs_de = np.empty((len(positions), EXTRA_COUNT))
    obs_df = np.empty((len(positions), EXTRA_COUNT))
    J = np.empty((len(ids), EXTRA_COUNT))
    covered = np.zeros(len(ids), dtype=bool)
    radial_ids = np.unique(points//nt)
    diagnostics = _diagnostics(bound, q, r, th)
    diagnostics.update(
        rows=len(ids), row_ids=array_binding(ids),
        need_observables=bool(need_observables),
        metric_row_count=len(positions),
        scalar_fields_seconds=0., angular_kernels_seconds=0.,
        scalar_contraction_seconds=0., metric_contraction_seconds=0.,
        height_column_seconds=0.)

    for begin in range(0, len(radial_ids), width):
        if wall is not None:
            wall()
        owned = radial_ids[begin:begin+width]
        selected = np.flatnonzero(np.isin(points//nt, owned))
        global_ri = points[selected]//nt
        ti = points[selected] % nt
        query = np.unique(np.r_[0, owned, len(r)-1])
        ri = np.searchsorted(query, global_ri)
        second = bool(np.any(groups[selected] >= 7))
        tick = time.monotonic()
        grid, fields, frame = field.scalar_frame(q, r[query], th)
        metric = {key: np.asarray(ordinary["metric"][key])[query]
                  for key in ("a", "a_s", "a_ss")}
        small = {key: np.asarray(ordinary[key])[global_ri, ti] for key in POSITION_KEYS}
        radius = metric["a"][ri]
        diagnostics["scalar_fields_seconds"] += time.monotonic()-tick
        local_metric = (groups[selected] < 2) if need_observables else np.zeros(len(selected), dtype=bool)
        metric_out = slots[selected[local_metric]]
        if np.any(local_metric):
            U, T = (small[key][local_metric] for key in ("Xs", "T"))
            obs_e[metric_out] = np.sum(U*U, axis=1)-1.
            obs_f[metric_out] = np.sum(U*T, axis=1)

        for name, start, stop in (("u", 0, 4), ("v", 4, 8)):
            tick = time.monotonic()
            kernels = angular_kernels(
                fields, frame, name, grid.angular_body, grid.angular_body_first,
                second=second)
            diagnostics["angular_kernels_seconds"] += time.monotonic()-tick
            diagnostics["family_kernel_count"] += 1
            diagnostics["maximum_family_kernel_array_bytes"] = max(
                diagnostics["maximum_family_kernel_array_bytes"],
                sum(value.nbytes for value in kernels.values()))
            tick = time.monotonic()
            virtual = virtual_selected_jets(kernels, ri, ti, metric, second=second)
            data = dict(small)
            data.update({"jac_"+key: value for key, value in virtual.items()})
            local = selected_spectral_parameter_jacobian(
                data, radius, groups[selected], side, cfg)
            radial_jets = tuple(np.asarray(grid.radial_body[name][j])[:, None]
                                for j in range(3))
            J[selected, start:stop] = expand_radial_rows(local, radial_jets, ri)
            diagnostics["scalar_contraction_seconds"] += time.monotonic()-tick
            tick = time.monotonic()
            if np.any(local_metric):
                observable = {key: small[key][local_metric] for key in ("Xs", "T")}
                observable.update({
                    "jac_"+key: virtual[key][local_metric] for key in ("Xs", "T")})
                de, df = observable_parameter_jacobians(observable)
                obs_de[metric_out, start:stop] = expand_radial_rows(
                    de, radial_jets, ri[local_metric])
                obs_df[metric_out, start:stop] = expand_radial_rows(
                    df, radial_jets, ri[local_metric])
            diagnostics["metric_contraction_seconds"] += time.monotonic()-tick
            del kernels, virtual, data, local

        tick = time.monotonic()
        height = _new_height_selected(grid.radial_body["height"], ri, second=second)
        data = dict(small)
        data.update({"jac_"+key: value for key, value in height.items()})
        J[selected, 8:9] = selected_spectral_parameter_jacobian(
            data, radius, groups[selected], side, cfg)
        if np.any(local_metric):
            observable = {key: small[key][local_metric] for key in ("Xs", "T")}
            observable.update({"jac_"+key: height[key][local_metric] for key in ("Xs", "T")})
            de, df = observable_parameter_jacobians(observable)
            obs_de[metric_out, 8:9], obs_df[metric_out, 8:9] = de, df
        diagnostics["height_column_seconds"] += time.monotonic()-tick
        diagnostics["batch_count"] += 1
        diagnostics["maximum_query_radial_rows"] = max(
            diagnostics["maximum_query_radial_rows"], len(query))
        covered[selected] = True

    arrays = [J, obs_e, obs_f, obs_de, obs_df]
    if not np.all(covered) or any(not np.all(np.isfinite(value)) for value in arrays):
        raise FloatingPointError("incomplete or nonfinite new-nine selected derivatives")
    observables = None
    if need_observables:
        observables = {
            "schema": POLICY+"-metric-observables",
            "row_positions": positions, "row_ids": ids[positions].copy(),
            "groups": groups[positions].copy(),
            "e": obs_e, "f": obs_f, "de": obs_de, "df": obs_df,
            "ordinary_binding_sha256": bound["binding_sha256"],
            "complete_row_ids": array_binding(ids),
            "new_column_count": EXTRA_COUNT,
        }
        observables["arrays"] = _metadata_arrays(observables)
        observables["binding_sha256"] = digest({
            key: value for key, value in observables.items()
            if not isinstance(value, np.ndarray)})
        for value in observables.values():
            if isinstance(value, np.ndarray):
                value.setflags(write=False)
    diagnostics.update(total_seconds=time.monotonic()-started,
                       selected_J9_bytes=int(J.nbytes),
                       row_order_preserved_including_repetitions=True)
    if wall is not None:
        wall()
    return J, diagnostics, observables


def new_nine_metric_jets(field, state, radial, theta, bound, *,
                         owned_width=16, wall=None):
    """Return (arrays, diagnostics) for one complete grid and all new9 columns.

    arrays e,f have shape (Nr,Ntheta); de,df have shape (Nr,Ntheta,9).
    This is a new derivative input, not a repeat ordinary value or an old159
    first-jet build.  It contracts the supplied current U,T with only the two
    four-mode kernels and the exact new height column.
    """
    started = time.monotonic()
    if not isinstance(field, CompleteBody168Field):
        raise ValueError("the explicitly new CompleteBody168Field is required")
    q, r, th, ordinary = field.validate_bound(state, radial, theta, bound)
    width = _width(owned_width)
    nr, nt = len(r), len(th)
    U, T = np.asarray(ordinary["Xs"]), np.asarray(ordinary["T"])
    arrays = {
        "e": np.sum(U*U, axis=2)-1.,
        "f": np.sum(U*T, axis=2),
        "de": np.empty((nr, nt, EXTRA_COUNT)),
        "df": np.empty((nr, nt, EXTRA_COUNT)),
    }
    diagnostics = _diagnostics(bound, q, r, th)
    diagnostics.update(
        purpose="complete-new-nine-metric-jet-grid",
        metric_point_count=nr*nt, maximum_virtual_columns=4,
        scalar_fields_seconds=0., angular_kernels_seconds=0.,
        metric_contraction_seconds=0.)
    for begin in range(0, nr, width):
        if wall is not None:
            wall()
        owned = np.arange(begin, min(nr, begin+width))
        query = np.unique(np.r_[0, owned, nr-1])
        take = np.searchsorted(query, owned)
        tick = time.monotonic()
        grid, fields, frame = field.scalar_frame(q, r[query], th)
        a = np.asarray(ordinary["metric"]["a"])[owned, None, None, None]
        ap = np.asarray(ordinary["metric"]["a_s"])[owned, None, None, None]
        own_U, own_T = U[owned], T[owned]
        diagnostics["scalar_fields_seconds"] += time.monotonic()-tick
        for name, start, stop in (("u", 0, 4), ("v", 4, 8)):
            tick = time.monotonic()
            kernels = angular_kernels(
                fields, frame, name, grid.angular_body, grid.angular_body_first,
                second=False)
            diagnostics["angular_kernels_seconds"] += time.monotonic()-tick
            diagnostics["family_kernel_count"] += 1
            diagnostics["maximum_family_kernel_array_bytes"] = max(
                diagnostics["maximum_family_kernel_array_bytes"],
                sum(value.nbytes for value in kernels.values()))
            tick = time.monotonic()
            rr = grid.radial_body[name]
            r0 = np.asarray(rr[0])[take, None, None, None]
            r1 = np.asarray(rr[1])[take, None, None, None]
            dT = kernels["F0"][take]*r0
            dU = (ap*kernels["P0"][take]+a*kernels["P1"][take])*r0 + a*kernels["P0"][take]*r1
            arrays["de"][owned, :, start:stop] = 2*np.sum(own_U[..., None]*dU, axis=2)
            arrays["df"][owned, :, start:stop] = np.sum(
                own_T[..., None]*dU+own_U[..., None]*dT, axis=2)
            diagnostics["metric_contraction_seconds"] += time.monotonic()-tick
            del kernels, dT, dU
        hb = np.asarray(grid.radial_body["height"]["b"])[take, None]
        arrays["de"][owned, :, 8] = 2*own_U[..., 2]*hb
        arrays["df"][owned, :, 8] = own_T[..., 2]*hb
        diagnostics["batch_count"] += 1
        diagnostics["maximum_query_radial_rows"] = max(
            diagnostics["maximum_query_radial_rows"], len(query))
    if any(not np.all(np.isfinite(value)) for value in arrays.values()):
        raise FloatingPointError("nonfinite complete new-nine metric jets")
    diagnostics.update(
        array_bindings=_metadata_arrays(arrays),
        complete_metric_jet_bytes=sum(int(value.nbytes) for value in arrays.values()),
        total_seconds=time.monotonic()-started)
    for value in arrays.values():
        value.setflags(write=False)
    if wall is not None:
        wall()
    return arrays, diagnostics

#!/usr/bin/env python3
"""Complete current-state derivatives of the R490 body168 family.

Import-only.  The old154 tangent bases and the new8 body bases are evaluated
through ONE current nonzero-new9 scalar frame.  Old5 exact null heights and
the new gamma direction are contracted against the same current ordinary.

No old159 final Jacobian reuse branch, ordinary geometry call, solver,
development check, test, or CLI exists in this module.  The external driver
owns every scientific cost, import, input, output, and deadline.
"""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_complete_body_extension168 import (
    CompleteBody168Field, INDEPENDENT_COUNT, POSITION_KEYS,
    POLICY as FIELD_POLICY, array_binding, _validate_grid)
from frame_collar_bvp import periodic_operator
from frame_entry_single_q import SingleQGrid
from frame_entry_paired_repair import EntryRepairGrid
from frame_selected_row_radial_jacobian import (
    angular_kernels, virtual_selected_jets, expand_radial_rows,
    selected_null_height_jets, selected_spectral_parameter_jacobian)
from frame_metric_affine_spectral_model import observable_parameter_jacobians
from frame_metric_spectral_recovery import (
    POLICY as SPECTRAL_POLICY, EPSILON_EXACT)
from frame_height_null_coordinates import digest


POLICY = "same-fixed-g-complete-body168-current-joint-selected-v1"
N = INDEPENDENT_COUNT
FIRST_KEYS = ("X", "Xs", "Xt", "T")
HEIGHT_COLUMNS = (154, 155, 156, 157, 158, 167)


def definition():
    return {
        "schema": POLICY,
        "field_policy": FIELD_POLICY,
        "independent_columns": 168,
        "physical_columns": 172,
        "column_layout": {
            "old_u": [0, 81], "old_v_without_Q": [81, 153],
            "original_normalized_Q": [153, 154],
            "old_exact_null_heights": [154, 159],
            "new_alpha": [159, 163], "new_beta": [163, 167],
            "new_gamma": [167, 168]},
        "one_current_nonzero_new9_scalar_frame_for_all_tangent_columns": True,
        "angular_families": ["current u:9", "current v:8", "current Q:1"],
        "new_four_modes_share_first_four_original_theta_modes": True,
        "original_radial_major_mode_minor_order_retained": True,
        "current_original_eleven_scalar_groups": True,
        "original_row_order_and_duplicates_retained": True,
        "all_legal_original_rows_including_endpoints_and_outside_new_body_support": True,
        "new_body_support_is_not_an_original159_derivative_filter": True,
        "exact_five_height_basis_not_rounded_nine_height_surrogate": True,
        "new_gamma_uses_complete_R490_center_speed_and_derivatives": True,
        "old_final159_J_reuse_branch": False,
        "old_SelectedRadialJacobian_evaluate_calls": 0,
        "ordinary_geometry_calls_inside_this_module": 0,
        "full_angle168_position_derivative_tensors": 0,
        "maximum_selected_virtual_parameter_axis": 27,
        "caller_owns_scientific_ledger": True,
        "not_an_optimizer_or_an_actual_candidate_acceptance_gate": True,
    }


def implementation_hashes():
    names = (
        Path(__file__).name,
        "frame_complete_body_extension168.py",
        "frame_collar_bvp.py",
        "frame_entry_single_q.py",
        "frame_entry_paired_repair.py",
        "frame_selected_row_radial_jacobian.py",
        "frame_metric_spectral_recovery.py",
        "frame_metric_budget_restoration_rows.py",
        "frame_metric_affine_spectral_model.py",
        "frame_height_null_coordinates.py",
        "frame_curvature_psd.py",
    )
    root = Path(__file__).parent
    return {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
            for name in names}


def _wall(wall):
    if wall is not None:
        wall()


def _finite(value, shape, label):
    a = np.asarray(value, dtype=float)
    if a.shape != tuple(shape) or not np.all(np.isfinite(a)):
        raise ValueError("finite declared shape required: " + label)
    return a


def _same_bytes(left, right):
    a, b = np.asarray(left), np.asarray(right)
    return (a.shape == b.shape and a.dtype == b.dtype
            and a.tobytes() == b.tobytes())


def _slice_is(value, start, stop):
    return (isinstance(value, slice) and value.start == start
            and value.stop == stop and value.step in (None, 1))


def _width(value):
    if (isinstance(value, (bool, np.bool_))
            or not isinstance(value, (int, np.integer))
            or not 1 <= value <= 16):
        raise ValueError("one through sixteen owned radial rows required")
    return int(value)


def _context(field):
    if not isinstance(field, CompleteBody168Field):
        raise ValueError("the complete new CompleteBody168Field is required")
    field._assert_context()
    old = field.original_field
    single = old._direct_single
    if (field.nunknown != 168 or field.metric_free != 0
            or old.nunknown != 159 or old.metric_free != 0
            or single.nunknown != 163 or single.metric_free != 0
            or single.q_index != 153 or single.height_free != 9
            or single.source.radial_free != 9
            or single.source.angular_modes != 5
            or single.source.phi_modes != 3
            or not single.source.core_direction
            or int(single.port.fold) != 2
            or not _slice_is(single.slices.get("u"), 0, 81)
            or not _slice_is(single.slices.get("v"), 81, 154)
            or not _slice_is(single.slices.get("height"), 154, 163)
            or not _slice_is(old.slices.get("height_null"), 154, 159)):
        raise ValueError("the declared complete body168/original159 basis layout is required")
    return old, single


def _current_identity(field, state, radial, theta):
    return {
        "policy": POLICY,
        "field_definition_sha256": field.definition_sha256,
        "coordinate_definition_sha256": field.coordinate_definition_sha256,
        "physical_identity_sha256": digest(field.identity(state)),
        "original_reference_coordinate_sha256":
            field.original_field.coordinate_definition_sha256,
        "state": array_binding(state),
        "radial": array_binding(radial),
        "theta": array_binding(theta),
    }


def _base_diagnostics(field, state, radial, theta, binding_sha256):
    out = _current_identity(field, state, radial, theta)
    out.update(
        input_binding_sha256=binding_sha256,
        independent_columns=N,
        physical_columns=172,
        current_new9_nonzero=bool(np.any(state[159:] != 0.)),
        batch_count=0,
        family_kernel_count=0,
        maximum_query_radial_rows=0,
        maximum_angular_modes=0,
        maximum_virtual_columns=0,
        maximum_family_kernel_array_bytes=0,
        maximum_selected_virtual_jet_bytes=0,
        scalar_fields_seconds=0.,
        basis_seconds=0.,
        angular_kernels_seconds=0.,
        scalar_contraction_seconds=0.,
        observable_contraction_seconds=0.,
        radial_expansion_seconds=0.,
        height_columns_seconds=0.,
        ordinary_geometry_calls_inside_module=0,
        old_final159_J_reuse_calls=0,
        old_SelectedRadialJacobian_evaluate_calls=0,
        full_angle168_position_derivative_tensors=0,
        full_current_field_and_original_angular_primitive=True,
        all_costs_owned_by_external_ledger=True)
    return out


def _families(body_grid, nr, nt, *, verify_shared_modes):
    """Pure original linear bases, not a reconstruction of the old field."""
    grid = body_grid.original_grid
    if not isinstance(grid, SingleQGrid) or not isinstance(grid.original, EntryRepairGrid):
        raise ValueError("the original paired-entry SingleQ grid is required")
    bases = tuple(_finite(grid.bases[j], (nr, 9), "original B/"+str(j))
                  for j in range(3))
    out = []
    for name, modes, start, stop, new_start, new_stop in (
            ("u", 9, 0, 81, 159, 163),
            ("v", 8, 81, 153, 163, 167)):
        w, wp, wpp = (
            _finite(value, (nr,), name+"/entry-weight/"+str(j))
            for j, value in enumerate(grid.original.weights[name]))
        radial = (
            w[:, None]*bases[0],
            wp[:, None]*bases[0]+w[:, None]*bases[1],
            wpp[:, None]*bases[0]+2*wp[:, None]*bases[1]+w[:, None]*bases[2])
        angular = _finite(grid.angular[name], (nt, modes), name+"/angular")
        first = _finite(grid.angular_first[name], (nt, modes), name+"/angular-first")
        if verify_shared_modes:
            # These are the same frozen sin(2*j*theta) expressions.  This is
            # a basis/column-identity binding, not a numerical derivative test.
            if (not _same_bytes(angular[:, :4], body_grid.angular_body)
                    or not _same_bytes(first[:, :4], body_grid.angular_body_first)):
                raise ValueError("new modes are not the literal first four original theta modes")
        new_radial = tuple(
            _finite(body_grid.radial_body[name][j], (nr,), name+"/new-radial/"+str(j))[:, None]
            for j in range(3))
        out.append({
            "name": name, "angular": angular, "angular_first": first,
            "radial": radial, "start": start, "stop": stop,
            "new_radial": new_radial, "new_start": new_start, "new_stop": new_stop})
    qr = tuple(
        _finite(value, (nr,), "original Q/radial/"+str(j))[:, None]
        for j, value in enumerate(grid.radial_Q))
    if len(qr) != 3:
        raise ValueError("three original normalized-Q radial jets required")
    out.append({
        "name": "v",
        "angular": _finite(grid.angular_Q, (nt,), "original Q/angular")[:, None],
        "angular_first": _finite(grid.angular_Q_theta, (nt,), "original Q/angular-first")[:, None],
        "radial": qr, "start": 153, "stop": 154,
        "new_radial": None, "new_start": None, "new_stop": None})
    return out


def _first_four_virtual(local, modes):
    a = np.asarray(local, dtype=float)
    if a.ndim != 2 or a.shape[1] != 3*modes or modes < 4:
        raise ValueError("original (radial-jet,mode) selected row shape required")
    return a.reshape(len(a), 3, modes)[:, :, :4].reshape(len(a), 12)


def _height_six(field, body_grid, radial, ri, *, second):
    old = selected_null_height_jets(field.original_field, radial, ri, second=second)
    keys = POSITION_KEYS if second else FIRST_KEYS
    answer = {}
    for key in keys:
        gamma = np.zeros((len(ri), 3, 1), dtype=float)
        if key in ("X", "Xs", "Xss"):
            source = {"X": "center", "Xs": "b", "Xss": "b_s"}[key]
            gamma[:, 2, 0] = np.asarray(body_grid.radial_body["height"][source])[ri]
        answer[key] = np.concatenate((old[key], gamma), axis=2)
    return answer


def _row_ids(row_ids, nr, nt):
    raw = list(row_ids)
    if any(isinstance(v, (bool, np.bool_))
           or not isinstance(v, (int, np.integer)) for v in raw):
        raise ValueError("original integer row IDs required")
    ids = np.asarray(raw, dtype=np.int64)
    count = nr*nt
    if not len(ids) or np.any(ids < 0) or np.any(ids >= 11*count):
        raise ValueError("nonempty original eleven-group row IDs required")
    # Do not sort or deduplicate the requested rows.
    return ids, ids//count, ids % count


def current_168_selected_rows(
        field, state168, radial, theta, row_ids, bound, cfg, *,
        side, owned_width=16, wall=None, need_observables=True):
    """Return (J168, diagnostics, observables) at the same complete current field.

    bound is the existing field.bind_ordinary record for this exact q168/grid.
    No ordinary geometry is evaluated here, and no old final159 J is reused.

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
    q, r, th, ordinary = field.validate_bound(state168, radial, theta, bound)
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
        purpose="complete-current168-selected-original-scalar-J",
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
        metric = {key: np.asarray(ordinary["metric"][key])[query]
                  for key in ("a", "a_s", "a_ss")}
        small = {key: np.asarray(ordinary[key])[global_ri, ti]
                 for key in POSITION_KEYS}
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


def _readonly_view(value):
    out = np.asarray(value).view()
    out.setflags(write=False)
    return out


def bind_current_168_first_jets(
        field, state168, radial, theta, data, source_receipt, *, wall=None):
    """Bind current U/T plus fixed a,a_s; no ordinary or derivative is evaluated.

    data may be a complete current ordinary dictionary (Xs,T,metric), or a
    current first-jet dictionary (U,T,metric).  metric must contain a and a_s.
    Optional e/f are required to be the literal derived current arrays; flat
    e/f are allowed only by reshape to the bound product grid.

    Large U/T/metric arrays are shared read-only views.  Their external owner
    must keep the underlying source arrays immutable for this binding's life.
    The receipt must identify their actual source.  A binding is not a claim
    that an input was free or already paid in a different ledger.
    """
    started = time.monotonic()
    _wall(wall)
    _context(field)
    q = field.validate_state(state168)
    r, th = _validate_grid(radial, theta)
    if not isinstance(data, dict) or not isinstance(source_receipt, dict):
        raise ValueError("current first-jet data and its explicit source receipt are required")
    shape = (len(r), len(th), 3)
    key = "Xs" if "Xs" in data else "U"
    if key not in data or "T" not in data:
        raise ValueError("current U or Xs and current T are required")
    U = _finite(data[key], shape, "first-jet/U")
    if "Xs" in data and "U" in data and not _same_bytes(data["Xs"], data["U"]):
        raise ValueError("two different first-jet U inputs were supplied")
    T = _finite(data["T"], shape, "first-jet/T")
    metric = data.get("metric")
    if not isinstance(metric, dict):
        raise ValueError("the fixed current metric a/a_s arrays are required")
    aa = {name: _finite(metric.get(name), (len(r),), "first-jet/metric/"+name)
          for name in ("a", "a_s")}
    if np.any(aa["a"] <= 0):
        raise ValueError("positive fixed radius a is required")
    for name, expected in (("radial", r), ("theta", th), ("state168", q)):
        if name in data and not _same_bytes(data[name], expected):
            raise ValueError("first-jet "+name+" binding mismatch")
    e = np.sum(U*U, axis=2)-1.
    f = np.sum(U*T, axis=2)
    for name, expected in (("e", e), ("f", f)):
        if name in data:
            supplied = np.asarray(data[name], dtype=float)
            if supplied.shape == (len(r)*len(th),):
                supplied = supplied.reshape(len(r), len(th))
            if not _same_bytes(supplied, expected):
                raise ValueError("supplied "+name+" is not the literal current U/T contraction")
    if not np.all(np.isfinite(e)) or not np.all(np.isfinite(f)):
        raise FloatingPointError("nonfinite current first-jet metric values")
    content = {
        "U": _readonly_view(U), "T": _readonly_view(T),
        "e": _readonly_view(e), "f": _readonly_view(f),
        "metric": {name: _readonly_view(value) for name, value in aa.items()}}
    identity = _current_identity(field, q, r, th)
    identity.update(
        schema=POLICY+"-bound-first-jets",
        source_receipt=copy.deepcopy(source_receipt),
        arrays={name: array_binding(content[name]) for name in ("U", "T", "e", "f")},
        metric_arrays={name: array_binding(value) for name, value in content["metric"].items()},
        first_jet_values_derived_once_from_current_U_T=True,
        no_ordinary_or_parameter_derivative_evaluation_in_binding=True,
        underlying_array_owner_must_keep_inputs_immutable=True)
    result = {
        "schema": identity["schema"],
        "identity": identity,
        "binding_sha256": digest(identity),
        "state": q.copy(), "radial": r.copy(), "theta": th.copy(),
        "data": content,
        "binding_seconds": time.monotonic()-started}
    for name in ("state", "radial", "theta"):
        result[name].setflags(write=False)
    _wall(wall)
    return result


def _validate_first_jets(field, state168, radial, theta, bound):
    _context(field)
    q = field.validate_state(state168)
    r, th = _validate_grid(radial, theta)
    if (not isinstance(bound, dict)
            or bound.get("schema") != POLICY+"-bound-first-jets"
            or not isinstance(bound.get("identity"), dict)
            or bound.get("binding_sha256") != digest(bound["identity"])
            or not _same_bytes(bound.get("state"), q)
            or not _same_bytes(bound.get("radial"), r)
            or not _same_bytes(bound.get("theta"), th)):
        raise ValueError("current168 first-jet binding differs from exact state/grid")
    expected = _current_identity(field, q, r, th)
    if any(bound["identity"].get(key) != value for key, value in expected.items()):
        raise ValueError("current168 first-jet physical/reference identity changed")
    data = bound.get("data")
    if not isinstance(data, dict) or not isinstance(data.get("metric"), dict):
        raise ValueError("complete first-jet binding data required")
    for name in ("U", "T"):
        _finite(data.get(name), (len(r), len(th), 3), "bound-first-jet/"+name)
    for name in ("e", "f"):
        _finite(data.get(name), (len(r), len(th)), "bound-first-jet/"+name)
    for name in ("a", "a_s"):
        _finite(data["metric"].get(name), (len(r),), "bound-first-jet/"+name)
    return q, r, th, data


def _scalar_direction(families, direction, nr, nt):
    """Collapse original/new linear bases before any full-angle frame derivative."""
    du = np.zeros((nr, nt), dtype=float)
    dv = np.zeros_like(du)
    dus = np.zeros_like(du)
    dvs = np.zeros_like(du)
    for family in families:
        radial = family["radial"]
        modes = family["angular"].shape[1]
        coefficients = direction[family["start"]:family["stop"]].reshape(-1, modes)
        value = (radial[0] @ coefficients) @ family["angular"].T
        first = (radial[1] @ coefficients) @ family["angular"].T
        if family["new_radial"] is not None:
            ns, ne = family["new_start"], family["new_stop"]
            angular_value = family["angular"][:, :4] @ direction[ns:ne]
            value += family["new_radial"][0][:, :1] * angular_value[None, :]
            first += family["new_radial"][1][:, :1] * angular_value[None, :]
        if family["name"] == "u":
            du += value
            dus += first
        else:
            dv += value
            dvs += first
    if any(not np.all(np.isfinite(v)) for v in (du, dv, dus, dvs)):
        raise FloatingPointError("nonfinite complete-current168 scalar direction")
    return du, dv, dus, dvs


def current_168_metric_direction(
        field, state168, direction168, radial, theta, first_jet_bound, *,
        owned_width=16, wall=None):
    """Return (arrays,diagnostics) for one full original grid and one direction.

    arrays has e/f/de/df, each shape (Nr,Ntheta).  This is the true first jet
    of current e/f in direction168, not an ordinary candidate evaluation and
    not a nonlinear metric prediction.  All old154 and new8 tangent entries
    are collapsed into scalar variations before the full-circle primitive.
    """
    started = time.monotonic()
    _wall(wall)
    q, r, th, baseline = _validate_first_jets(
        field, state168, radial, theta, first_jet_bound)
    direction = _finite(direction168, (N,), "current168 direction")
    width = _width(owned_width)
    nr, nt = len(r), len(th)
    U, T = baseline["U"], baseline["T"]
    arrays = {
        "e": baseline["e"], "f": baseline["f"],
        "de": np.empty((nr, nt), dtype=float),
        "df": np.empty((nr, nt), dtype=float)}
    diagnostics = _base_diagnostics(
        field, q, r, th, first_jet_bound["binding_sha256"])
    diagnostics.update(
        purpose="complete-current168-one-direction-metric-first-jet",
        direction=array_binding(direction),
        metric_point_count=nr*nt,
        scalar_direction_seconds=0.,
        directional_frame_seconds=0.,
        directional_primitive_seconds=0.,
        metric_contraction_seconds=0.,
        full_angle_parameter_axis=None,
        collapsed_scalar_direction_only=True,
        original_fine_theta_bytes_retained=True,
        primitive_passes=0)

    for begin in range(0, nr, width):
        _wall(wall)
        owned = np.arange(begin, min(nr, begin+width))
        query = np.unique(np.r_[0, owned, nr-1])
        take = np.searchsorted(query, owned)
        tick = time.monotonic()
        body_grid, fields, frame = field.scalar_frame(q, r[query], th)
        diagnostics["scalar_fields_seconds"] += time.monotonic()-tick
        tick = time.monotonic()
        families = _families(body_grid, len(query), nt, verify_shared_modes=(begin == 0))
        diagnostics["basis_seconds"] += time.monotonic()-tick
        tick = time.monotonic()
        du, dv, dus, dvs = _scalar_direction(
            families, direction, len(query), nt)
        diagnostics["scalar_direction_seconds"] += time.monotonic()-tick
        tick = time.monotonic()
        tu, tv = frame["Tpart"]["u"], frame["Tpart"]["v"]
        t_us, t_vs = frame["Ts_value_part"]["u"], frame["Ts_value_part"]["v"]
        dT = du[..., None]*tu + dv[..., None]*tv
        dTs = (du[..., None]*t_us + dv[..., None]*t_vs
               + dus[..., None]*tu + dvs[..., None]*tv)
        diagnostics["directional_frame_seconds"] += time.monotonic()-tick
        tick = time.monotonic()
        p0 = periodic_operator(dT, -1)
        p1 = periodic_operator(dTs, -1)
        diagnostics["directional_primitive_seconds"] += time.monotonic()-tick
        diagnostics["primitive_passes"] += 2
        tick = time.monotonic()
        a = baseline["metric"]["a"][owned, None, None]
        ap = baseline["metric"]["a_s"][owned, None, None]
        dU = ap*p0[take] + a*p1[take]
        old_height = _finite(
            field.original_field.null_basis.values(r[query]),
            (len(query), 5), "current-direction/exact-null-height")
        db = old_height @ direction[154:159]
        db += np.asarray(body_grid.radial_body["height"]["b"])*direction[167]
        dU[..., 2] += db[take, None]
        own_U, own_T = U[owned], T[owned]
        arrays["de"][owned] = 2*np.sum(own_U*dU, axis=2)
        arrays["df"][owned] = np.sum(
            own_T*dU + own_U*dT[take], axis=2)
        diagnostics["metric_contraction_seconds"] += time.monotonic()-tick
        diagnostics["batch_count"] += 1
        diagnostics["maximum_query_radial_rows"] = max(
            diagnostics["maximum_query_radial_rows"], len(query))
        diagnostics["maximum_directional_work_array_bytes"] = max(
            diagnostics.get("maximum_directional_work_array_bytes", 0),
            sum(int(v.nbytes) for v in
                (du, dv, dus, dvs, dT, dTs, p0, p1, dU)))
        del body_grid, fields, frame, families, du, dv, dus, dvs, dT, dTs, p0, p1, dU

    if any(not np.all(np.isfinite(value)) for value in arrays.values()):
        raise FloatingPointError("nonfinite complete-current168 directional metric jets")
    for value in arrays.values():
        value.setflags(write=False)
    diagnostics.update(
        array_bindings={key: array_binding(value) for key, value in arrays.items()},
        returned_directional_bytes=sum(int(v.nbytes) for v in arrays.values()),
        total_seconds=time.monotonic()-started,
        complete=True)
    _wall(wall)
    return arrays, diagnostics

"""Finite cell-local residual queries for an explicitly saved bump P1 field.

The native reader owns the actual field definition. This module never builds
a solver mesh, interpolates to a new mesh, solves an equation, or evolves a
body frame. Two Gauss points are a finite quadrature diagnostic, not a bound
for the unsampled part of the cell. Angular projection is the stated discrete
projection on the specified computational-xi grid, with the full sampled
residual retained separately.
"""
from __future__ import annotations

import numpy as np
from fd2d_gc_three_field_residual import native_residuals

COMPONENTS = ('G', 'Rn', 'Rm')
RESIDUAL_KEYS = ('a', 'a_s', 'a_ss', 'l', 'm', 'n', 'J', 'U_x',
                 'U_xi', 'l_xi', 'm_xi', 'n_xi', 'm_x', 'n_x')
GAUSS_FRACTIONS = np.array([.5-.5/np.sqrt(3.), .5+.5/np.sqrt(3.)])


def select_cells(reader, *, cells=(), intervals=(), segment_labels=(), all_cells=False):
    """Union of actual saved cells selected by index or physical overlap.

    A positive-length interval selects every cell with positive interior
    overlap. Endpoints do not add an adjacent cell that only touches it.
    Segment labels refer to the actual base profile, not a hard-coded cell
    number. They select whole saved cells; the query does not clip or split a
    cell when a requested interval cuts through it.
    """
    mesh = np.asarray(reader.nodes, float)
    count = len(mesh)-1
    selected = set(range(count)) if all_cells else set()
    requests = []
    for raw in cells:
        index = int(raw)
        if index != raw or not 0 <= index < count:
            raise ValueError(f'Cell {raw!r} is not an index of the saved mesh')
        selected.add(index)
        requests.append(dict(kind='cell', index=index))

    def add_interval(left, right, origin):
        left, right = float(left), float(right)
        if not np.isfinite(left+right) or not mesh[0] <= left < right <= mesh[-1]:
            raise ValueError('A physical selection interval must have positive length inside the saved domain')
        indices = np.flatnonzero((mesh[:-1] < right) & (mesh[1:] > left))
        selected.update(int(i) for i in indices)
        requests.append(dict(kind=origin, interval=[left, right], actual_cells=indices.tolist()))

    for interval in intervals:
        if len(interval) != 2:
            raise ValueError('A physical interval needs exactly two endpoints')
        add_interval(*interval, 'physical_interval')
    for label in segment_labels:
        matches = [piece for piece in reader.profile.base.segments if piece.get('label') == label]
        if not matches:
            raise ValueError(f'No actual physical segment has label {label!r}')
        for piece in matches:
            add_interval(piece['s0'], piece['s1'], 'physical_segment:'+str(label))
    if not selected:
        raise ValueError('Select an actual cell, physical interval, segment label, or explicitly all cells')
    return np.array(sorted(selected), dtype=int), requests


def _projection(value, component, E, O, PE, PO):
    basis, projection = (O, PO) if component == 'Rm' else (E, PE)
    return (basis@(projection@value.T)).T


def _maxima(value):
    return {key: float(np.max(np.abs(value[..., j]), initial=0.))
            for j, key in enumerate(COMPONENTS)}


def probe_cell(reader, cell, *, angles=256, endpoints=False):
    """Return the full two-point samples and a small JSON-ready summary.

    The arithmetic mean holds xi fixed. For physical_bumps x=s, the returned
    Rn/Rm are also the complete native Codazzi residuals; no factor J is
    hidden in the mean. Both ends, when requested, use this cell's P1 slope.
    The actual material u is returned separately at every point.
    """
    if not isinstance(angles, (int, np.integer)) or angles < 64 or angles % 4:
        raise ValueError('Use an angular count divisible by four and at least 64')
    if angles <= 4*reader.K+2:
        raise ValueError('The angular grid must resolve the retained parity modes')
    index = int(cell)
    if index != cell or not 0 <= index < len(reader.nodes)-1:
        raise ValueError('Cell index is outside the actual saved P1 mesh')
    left, right = (float(v) for v in reader.nodes[index:index+2])
    fractions = np.r_[0., GAUSS_FRACTIONS, 1.] if endpoints else GAUSS_FRACTIONS.copy()
    gauss_indices = np.array([1, 2] if endpoints else [0, 1])
    s = left+(right-left)*fractions
    if endpoints:
        s[0], s[-1] = left, right
    xi = 2*np.pi*np.arange(angles)/angles
    q = reader.evaluate_native(s[:, None], xi[None, :], side='left')
    if endpoints:
        # Searchsorted(left) at a shared node would choose the preceding
        # interval. Replace the entire left jet by the right one-sided jet.
        first = reader.evaluate_native(left, xi, side='right')
        for key in q:
            q[key][0] = first[key]
    if not np.all(np.asarray(q['J']) == 1.):
        raise ValueError('This cell probe is for the explicit physical-s bump reader')
    residual = native_residuals(**{key: q[key] for key in RESIDUAL_KEYS})
    full = np.stack([residual[key] for key in COMPONENTS], axis=-1)
    E = np.cos(xi[:, None]*reader.frequencies)
    O = np.sin(xi[:, None]*reader.frequencies[1:])
    PE = 2*E.T/angles
    PE[0] *= .5
    PO = 2*O.T/angles
    retained = np.stack([_projection(full[..., j], key, E, O, PE, PO)
                         for j, key in enumerate(COMPONENTS)], axis=-1)
    omitted = full-retained
    mean = np.mean(full[gauss_indices], axis=0)
    mean_retained = np.mean(retained[gauss_indices], axis=0)
    mean_omitted = np.mean(omitted[gauss_indices], axis=0)
    spread = np.hypot(q['n']-q['l'], 2*q['m'])
    formal_curvature = .5*np.maximum(np.abs(q['n']+q['l']+spread),
                                    np.abs(q['n']+q['l']-spread))
    peaks = {}
    for j, key in enumerate(COMPONENTS):
        radial, angular = np.unravel_index(np.argmax(np.abs(full[..., j])), full.shape[:2])
        peaks[key] = dict(absolute_value=float(abs(full[radial, angular, j])),
            signed_value=float(full[radial, angular, j]),
            fraction=float(fractions[radial]), s=float(s[radial]), xi=float(xi[angular]),
            material_u=float(q['u'][radial, angular]),
            retained_at_same_point=float(retained[radial, angular, j]),
            omitted_at_same_point=float(omitted[radial, angular, j]))
    summary = dict(cell=index, endpoints=[left, right], length=right-left,
        sample_fractions=fractions.tolist(), physical_sample_s=s.tolist(),
        gauss_point_indices=gauss_indices.tolist(), gauss_weights=[.5, .5],
        sample_maxima=_maxima(full), retained_sample_maxima=_maxima(retained),
        omitted_sample_maxima=_maxima(omitted), peaks=peaks,
        gauss2_mean_maxima=_maxima(mean),
        gauss2_retained_mean_maxima=_maxima(mean_retained),
        gauss2_omitted_mean_maxima=_maxima(mean_omitted),
        gauss2_integral_maxima=_maxima((right-left)*mean),
        sampled_n_minimum=float(np.min(q['n'])),
        sampled_formal_curvature_maximum=float(np.max(formal_curvature)),
        sampled_connection_operator_norm_maximum=float(np.max(residual['connection_operator_norm'])),
        a_range=[float(np.min(q['a'])), float(np.max(q['a']))],
        a_s_range=[float(np.min(q['a_s'])), float(np.max(q['a_s']))],
        a_ss_range=[float(np.min(q['a_ss'])), float(np.max(q['a_ss']))])
    if endpoints:
        trapezoid = .5*(full[0]+full[-1])
        summary['trapezoid_mean_maxima'] = _maxima(trapezoid)
        summary['gauss2_minus_trapezoid_maxima'] = _maxima(mean-trapezoid)
    return dict(summary=summary, physical_s=s, xi=xi, material_u=q['u'],
        fractions=fractions, gauss_indices=gauss_indices, full=full,
        retained=retained, omitted=omitted, gauss2_mean=mean,
        gauss2_retained_mean=mean_retained, gauss2_omitted_mean=mean_omitted,
        fields=q)

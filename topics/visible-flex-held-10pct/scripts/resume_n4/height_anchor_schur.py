#!/usr/bin/env python3
"""Height-anchor Schur diagnostic for the existing finite collocation equations.

This module consumes an already assembled original Jacobian and residual.
It does not change a physical model, boundary acceptance gate, Newton rule,
or a running solve. The numerical helper has not been executed in the
2026-11-20 unavailable environment; its block identity is derived in the
associated note. Float LU/SVD outputs are diagnostics, not interval proofs.

Unknown order: [Y.ravel(order='F'), p]. Residual order:
[collocation.ravel(order='F'), inlet, terminal DN].
For the cylindrical prefix n_state=3*M+1, z starts at index 2*M+1.
The exact reference lift must vanish at the terminal cut.
"""
from __future__ import annotations

import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import splu


def _spectrum(matrix):
    values = np.linalg.svd(matrix, compute_uv=False)
    return dict(singular_values=values.tolist(),
                condition_2=None if values[-1] == 0 else float(values[0]/values[-1]),
                determinant=float(np.linalg.det(matrix)))


def height_anchor_schur(jacobian, residual, y_last, *, mesh_nodes, modes,
                     gauge_amplitude, bridge_sigma, boundary_weights,
                     target_heights, branch_parameters=(0, 1),
                     height_modes=(0, 1), branch_scales=None,
                     height_scales=None, operator_label):
    """Return exact block formulas evaluated by one float sparse factorization.

    branch_parameters and height_modes are zero-based parameter/mode indices.
    Defaults are log(q/q_gauge), c8/q_gauge and H4,H8 for the raw n4 model.
    Selected branch columns are removed with equally many terminal rows.
    For a single m3 branch, use branch_parameters=(0,), height_modes=(0,).
    For the n4 double branch, the default uses two columns and two rows.
    The remaining block retains every inlet/collocation equation and
    all other terminal DN equations, avoiding a pure forward-IVP elimination.

    Positive branch_scales and height_scales define the dimensionless matrix
    diag(1/height_scales) dH/dalpha diag(branch_scales). They affect only
    reporting, not the equations or computed step. Raw DN and height matrices
    have different physical units; do not compare their unscaled magnitudes.

    Returned steps have the full original unknown ordering and still require
    the original domain-aware backtracking. A small/singular response is not
    itself a nonexistence result. No returned quantity is an acceptance flag.
    """
    M = int(modes)
    K = int(mesh_nodes)
    n = 3*M+1
    if M < 1 or K < 2:
        raise ValueError('At least one mode and two mesh nodes are required')
    state_size = n*K
    size = state_size+M
    J = csc_matrix(jacobian, dtype=float)
    r = np.asarray(residual, dtype=float)
    yb = np.asarray(y_last, dtype=float)
    weights = np.asarray(boundary_weights, dtype=float)
    target = np.asarray(target_heights, dtype=float)
    branch = np.asarray(branch_parameters, dtype=int)
    hmodes = np.asarray(height_modes, dtype=int)
    k = len(branch)
    if (J.shape != (size, size) or r.shape != (size,) or
            yb.shape != (n,) or weights.shape != (M,) or target.shape != (k,)):
        raise ValueError('Declared finite-system dimensions do not match')
    if (k < 1 or branch.shape != (k,) or hmodes.shape != (k,) or
            len(set(branch.tolist())) != k or len(set(hmodes.tolist())) != k or
            np.any(branch < 0) or np.any(branch >= M) or
            np.any(hmodes < 0) or np.any(hmodes >= M)):
        raise ValueError('Choose equally many distinct existing parameter columns/modes')
    q = float(gauge_amplitude)
    sigma = float(bridge_sigma)
    if not np.isfinite(q) or q <= 0 or sigma not in (-1., 1.) or np.any(weights <= 0):
        raise ValueError('Positive fixed gauge/weights and the original sigma are required')
    if not all(np.isfinite(x).all() for x in (J.data, r, yb, weights, target)):
        raise FloatingPointError('Nonfinite original linearization')
    rows_low = state_size+hmodes
    cols_branch = state_size+branch
    rows_keep = np.delete(np.arange(size), rows_low)
    cols_keep = np.delete(np.arange(size), cols_branch)
    A = J[rows_keep, :][:, cols_keep].tocsc()
    B = J[rows_keep, :][:, cols_branch].toarray()
    C_dn = J[rows_low, :][:, cols_keep].toarray()
    D_dn = J[rows_low, :][:, cols_branch].toarray()
    try:
        factor = splu(A)
    except RuntimeError as exc:
        raise RuntimeError('Selected complement block is singular; this branch-coordinate choice failed') from exc
    # One factorization, then one residual and k parameter right-hand sides.
    solved = factor.solve(np.column_stack((r[rows_keep], B)))
    if not np.isfinite(solved).all():
        raise FloatingPointError('Nonfinite complement-block solve')
    v, Z = solved[:, 0], solved[:, 1:]
    C_height = np.zeros((k, len(cols_keep)))
    iz = 2*M+1
    for j, mode in enumerate(hmodes):
        state_column = (K-1)*n+iz+mode
        position = np.searchsorted(cols_keep, state_column)
        if position == len(cols_keep) or cols_keep[position] != state_column:
            raise ValueError('A terminal state column was removed as a parameter')
        C_height[j, position] = sigma*q/weights[mode]
    H = sigma*q*yb[iz+hmodes]
    r_height = (H-target)/weights[hmodes]
    S_dn = D_dn-C_dn@Z
    S_height = -C_height@Z
    b_dn = -r[rows_low]+C_dn@v
    b_height = -r_height+C_height@v

    def full_step(S, b):
        try:
            delta_branch = np.linalg.solve(S, b)
        except np.linalg.LinAlgError:
            return None
        delta = np.empty(size)
        delta[cols_branch] = delta_branch
        delta[cols_keep] = -v-Z@delta_branch
        return delta

    report = dict(scope='Finite float Schur response; no acceptance or existence certificate',
                  operator_label=str(operator_label), state_size=state_size,
                  parameter_count=M, branch_parameters=branch.tolist(),
                  height_modes=hmodes.tolist(), current_tail_heights=H.tolist(),
                  target_tail_heights=target.tolist(),
                  original_reduced_matrix=S_dn.tolist(),
                  height_reduced_matrix=S_height.tolist(),
                  original_reduced_rhs=b_dn.tolist(),
                  height_reduced_rhs=b_height.tolist(),
                  original_selected_residual=r[rows_low].tolist(),
                  height_selected_residual=r_height.tolist(),
                  original_interior_feedback=(C_dn@v).tolist(),
                  height_interior_feedback=(C_height@v).tolist(),
                  original_raw_spectrum=_spectrum(S_dn),
                  height_raw_spectrum=_spectrum(S_height))
    if branch_scales is not None or height_scales is not None:
        if branch_scales is None or height_scales is None:
            raise ValueError('Supply both scales to report a dimensionless response')
        ps = np.asarray(branch_scales, dtype=float)
        hs = np.asarray(height_scales, dtype=float)
        if (ps.shape != (k,) or hs.shape != (k,) or not np.isfinite(ps).all() or
                not np.isfinite(hs).all() or np.any(ps <= 0) or np.any(hs <= 0)):
            raise ValueError('One positive scale per selected coordinate is required')
        normalized = (weights[hmodes]/hs)[:, None]*S_height*ps[None, :]
        report['branch_scales'] = ps.tolist()
        report['height_scales'] = hs.tolist()
        report['dimensionless_height_matrix'] = normalized.tolist()
        report['dimensionless_height_spectrum'] = _spectrum(normalized)
    try:
        branch_response = np.linalg.solve(S_height, np.diag(1/weights[hmodes]))
    except np.linalg.LinAlgError:
        branch_response = None
    return dict(diagnostics=report,
                original_newton_step=full_step(S_dn, b_dn),
                height_newton_step=full_step(S_height, b_height),
                branch_response_to_physical_target_height=branch_response)

# Descriptive alias for the default n4 two-coordinate case.
two_height_schur = height_anchor_schur

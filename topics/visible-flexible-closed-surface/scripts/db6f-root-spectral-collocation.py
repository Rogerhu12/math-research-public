#!/usr/bin/env python3
"""Positive diagonal conjugacy for the finite prefix collocation problem.

This module does not load a candidate or run a solver on import. It returns
physical y/yp/PPoly values and re-evaluates the original physical RMS and BC.
No DN, metric, continuous enclosure or existence conclusion follows from it.
"""
import copy
import hashlib
import inspect
import numpy as np
from scipy.integrate import solve_bvp as scipy_solve_bvp
import scipy.integrate._bvp as scipy_bvp
from scipy.interpolate import PPoly


SCIPY_BVP_SHA256 = '59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2'


def power2_weights(modes):
    if not isinstance(modes, int) or modes < 1:
        raise ValueError('Positive integer mode count required')
    block = np.array([float(1 << (9*j*j).bit_length()) for j in range(1, modes+1)])
    weights = np.r_[1., np.tile(block, 3)]
    target = 1 + np.r_[0, np.tile(3*np.arange(1, modes+1), 3)]**2
    if not np.all((target <= weights) & (weights < 2*target)):
        raise RuntimeError('Power-of-two spectral weights do not enclose target')
    return weights


def make_solver(weights):
    """Return (callable, records); no source or engine is changed.

    Callbacks use the prefix three-argument signatures and a nonempty p.
    Singular S problems and complex-valued inputs are deliberately unsupported.
    """
    runtime_path = inspect.getfile(scipy_bvp)
    with open(runtime_path, 'rb') as f:
        runtime_sha = hashlib.sha256(f.read()).hexdigest()
    if runtime_sha != SCIPY_BVP_SHA256:
        raise RuntimeError('Installed SciPy BVP source is not the reviewed source')
    w = np.asarray(weights, dtype=float).copy()
    if w.ndim != 1 or not np.all(np.isfinite(w)) or not np.all(w >= 1):
        raise ValueError('Finite diagonal weights at least one required')
    if not np.all(np.frexp(w)[0] == .5):
        raise ValueError('This implementation is restricted to powers of two')
    w.setflags(write=False)
    n = len(w)
    records = []

    def scale_checked(value, factor):
        value = np.asarray(value)
        if not np.isrealobj(value) or not np.all(np.isfinite(value)):
            raise FloatingPointError('Nonfinite or complex coordinate data')
        with np.errstate(over='raise', under='raise', invalid='raise'):
            changed = value * factor
            restored = changed / factor
        if not np.array_equal(restored, value):
            raise FloatingPointError('Coordinate scaling round trip failed')
        return changed

    def solve(fun, bc, x, y, p=None, S=None, fun_jac=None, bc_jac=None,
              tol=2e-9, max_nodes=6500, verbose=0, bc_tol=None):
        if S is not None or p is None or np.asarray(p).ndim != 1 or len(p) == 0:
            raise ValueError('Only nonsingular prefix problems with parameters are supported')
        if fun_jac is None or bc_jac is None:
            raise ValueError('Reviewed analytic RHS and boundary Jacobians are required')
        y = np.asarray(y)
        if y.ndim != 2 or y.shape != (n, len(x)):
            raise ValueError('Physical state dimension does not match frozen weights')
        if not (np.isfinite(tol) and tol > 0):
            raise ValueError('Finite positive collocation tolerance required')
        physical_bc_tol = tol if bc_tol is None else bc_tol
        if not (np.isfinite(physical_bc_tol) and physical_bc_tol > 0):
            raise ValueError('Finite positive boundary tolerance required')
        u = scale_checked(y, w[:, None])
        parameters = np.asarray(p, float).copy()
        if not np.all(np.isfinite(parameters)):
            raise ValueError('Finite unchanged parameters required')
        k = len(parameters)

        def weighted_fun(xx, uu, pp):
            return w[:, None] * fun(xx, uu/w[:, None], pp)

        def weighted_jac(xx, uu, pp):
            fy, fp = fun_jac(xx, uu/w[:, None], pp)
            if np.shape(fy) != (n, n, len(xx)) or np.shape(fp) != (n, k, len(xx)):
                raise ValueError('Original RHS Jacobian shape differs')
            return (w[:, None, None]*fy/w[None, :, None], w[:, None, None]*fp)

        def physical_bc(ua, ub, pp):
            return bc(ua/w, ub/w, pp)

        def physical_bc_jac(ua, ub, pp):
            aa, bb, pp_jac = bc_jac(ua/w, ub/w, pp)
            if np.shape(aa) != (n+k, n) or np.shape(bb) != (n+k, n) or np.shape(pp_jac) != (n+k, k):
                raise ValueError('Original boundary Jacobian shape differs')
            return aa/w[None, :], bb/w[None, :], pp_jac

        entry = dict(call=len(records)+1, status='RUNNING_WEIGHTED_COLLOCATION',
                     initial_nodes=len(x), state_components=n, parameters=k,
                     original_tol=float(tol), original_bc_tol=float(physical_bc_tol),
                     maximum_nodes=int(max_nodes), weights=w.tolist(),
                     scipy_bvp_sha256=runtime_sha,
                     actual_nonlinear_tail_not_inferred=True)
        records.append(entry)
        try:
            raw = scipy_solve_bvp(weighted_fun, physical_bc, x, u, parameters,
                                 fun_jac=weighted_jac, bc_jac=physical_bc_jac,
                                 tol=tol, bc_tol=physical_bc_tol,
                                 max_nodes=max_nodes, verbose=verbose)
            result = copy.copy(raw)
            if not isinstance(raw.sol, PPoly) or raw.sol.axis != 1:
                raise RuntimeError('Unexpected collocation interpolant type or axis')
            if raw.sol.c.shape != (4, len(raw.x)-1, n):
                raise RuntimeError('Unexpected collocation polynomial coefficient layout')
            result.y = scale_checked(raw.y, (1/w)[:, None])
            result.yp = scale_checked(raw.yp, (1/w)[:, None])
            coefficients = scale_checked(raw.sol.c, (1/w)[None, None, :])
            result.sol = PPoly.construct_fast(coefficients, raw.sol.x.copy(),
                                             extrapolate=raw.sol.extrapolate, axis=1)
            hh = np.diff(result.x)
            mid = result.x[:-1] + .5*hh
            fm = fun(mid, result.sol(mid), result.p)
            rm = result.sol(mid, 1)-fm
            physical_rms = scipy_bvp.estimate_rms_residuals(
                fun, result.sol, result.x, hh, result.p, rm.copy(), fm)
            physical_boundary = np.asarray(bc(result.y[:, 0], result.y[:, -1], result.p))
            if not np.all(np.isfinite(physical_rms)) or not np.all(np.isfinite(physical_boundary)):
                raise FloatingPointError('Original physical residual is not finite')
            result.rms_residuals = physical_rms
            result.weighted_rms_residuals = np.asarray(raw.rms_residuals).copy()
            physical_max = float(np.max(physical_rms))
            boundary_max = float(np.max(np.abs(physical_boundary)))
            physical_pass = physical_max <= tol and boundary_max <= physical_bc_tol
            if raw.success and not physical_pass:
                result.success = False
                result.status = 4
                result.message = 'Weighted solve passed but original physical residual gate did not'
            entry.update(status='RETURNED_PHYSICAL_COORDINATES',
                         weighted_solver_success=bool(raw.success), success=bool(result.success),
                         final_nodes=len(result.x), weighted_rms_max=float(np.max(raw.rms_residuals)),
                         original_physical_rms_max=physical_max, original_physical_bc_max=boundary_max,
                         original_physical_residual_gate_passed=physical_pass,
                         ppoly_axis=1, coordinate_roundtrips_passed=True,
                         scope='Finite collocation diagnostics only; neither continuous metric nor true DN success.')
            result.spectral_coordinate_audit = copy.deepcopy(entry)
            return result
        except Exception as exc:
            entry.update(status='WEIGHTED_COLLOCATION_EXCEPTION', error=repr(exc))
            raise

    return solve, records

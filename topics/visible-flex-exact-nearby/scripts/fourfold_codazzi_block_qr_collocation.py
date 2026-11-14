#!/usr/bin/env python3
"""Full finite collocation solve by orthogonal propagation of boundary rows.

Every endpoint/midpoint Fourier coupling and the metric-parameter column
are retained.  QR eliminates one complete nodal block at a time; the
surviving left boundary row space is reorthonormalized, not shot through
an unstable fundamental matrix.  The original complete FFT action checks
each answer.  This is floating linear algebra, not a continuous PDE proof.
"""
from __future__ import annotations

import resource
import tempfile
import time
import warnings
from pathlib import Path

import numpy as np
import scipy.integrate._bvp as bvp
from scipy.linalg import LinAlgWarning, lu_factor, lu_solve, qr, solve_triangular
from scipy.linalg.lapack import dgeqrf, dormqr
from scipy.sparse.linalg import LinearOperator

from fourfold_codazzi_matrix_free_fft_collocation_v5 import state_action


def orthonormal_rows(rows):
    q, r = qr(rows.T, mode="economic", check_finite=False)
    if r.shape[0] != rows.shape[0] or not np.all(np.isfinite(r)):
        raise RuntimeError("invalid propagated boundary row space")
    if np.any(np.diag(r) == 0):
        raise RuntimeError("rank loss in propagated boundary rows")
    return q.T.copy(), r.copy()


def householder(matrix):
    packed, tau, work, info = dgeqrf(np.asfortranarray(matrix), overwrite_a=1)
    if info:
        raise RuntimeError(f"complete block dgeqrf returned {info}")
    return packed, tau


def apply_qt(packed, tau, value):
    c = np.array(value, dtype=float, order="F", copy=True)
    if c.ndim == 1:
        c = c[:, None]
    _, work, info = dormqr("L", "T", packed, tau, c, lwork=-1)
    if info:
        raise RuntimeError(f"complete block dormqr workspace returned {info}")
    out, _, info = dormqr("L", "T", packed, tau, c,
                         lwork=max(1, int(work[0])), overwrite_c=1)
    if info:
        raise RuntimeError(f"complete block dormqr returned {info}")
    return out


class FullBoundaryQR:
    """Factor a separated-boundary, adjacent-block system with one parameter."""

    def __init__(self, n, nodes, left, right, parameter, blocks, history,
                 storage="memory", scratch=None):
        tick = time.monotonic()
        self.n, self.nodes, self.history = n, nodes, history
        self.left_rows = np.flatnonzero(np.any(left != 0, axis=1))
        self.right_rows = np.flatnonzero(~np.any(left != 0, axis=1))
        if np.any(right[self.left_rows] != 0):
            raise RuntimeError("QR producer requires the actual separated boundary rows")
        p = self.left_rows.size
        if p == 0 or p > n or left.shape != (n + 1, n):
            raise RuntimeError("unsupported complete boundary dimensions")
        self.p = p
        c0 = np.column_stack((left[self.left_rows], parameter[self.left_rows, 0]))
        self.c0, self.initial_r = orthonormal_rows(c0)
        current = self.c0
        self.right_boundary = np.column_stack(
            (right[self.right_rows], parameter[self.right_rows, 0]))
        self.right_scale = 1 / np.maximum(
            1., np.max(abs(self.right_boundary), axis=1))
        self.right_boundary *= self.right_scale[:, None]
        self.shapes = ((n+p, n), (n,), (n, n), (n,), (p, p), (n,))
        self.counts = [int(np.prod(s)) for s in self.shapes]
        self.record_bytes = 8 * sum(self.counts)
        if storage not in ("memory", "file"):
            raise ValueError("unknown exact factor storage")
        self.records = [] if storage == "memory" else None
        self.file = (tempfile.TemporaryFile(prefix="codazzi-full-qr-",
                     dir=scratch) if storage == "file" else None)
        self.minimum_local_diagonal = float("inf")
        for i, (a, b, c) in enumerate(blocks):
            if i >= nodes-1:
                raise RuntimeError("too many complete collocation blocks")
            scale = 1 / np.maximum(1., np.maximum.reduce((
                np.max(abs(a), axis=1), np.max(abs(b), axis=1), abs(c))))
            packed, tau = householder(np.vstack((current[:, :n], scale[:, None]*a)))
            coefficients = np.zeros((n+p, n+1))
            coefficients[:p, n] = current[:, n]
            coefficients[p:, :n] = scale[:, None]*b
            coefficients[p:, n] = scale*c
            transformed = apply_qt(packed, tau, coefficients)
            current, norm_r = orthonormal_rows(transformed[n:])
            item = (packed, tau, transformed[:n, :n].copy(),
                    transformed[:n, n].copy(), norm_r, scale)
            self.minimum_local_diagonal = min(
                self.minimum_local_diagonal, float(np.min(abs(np.diag(packed[:n])))))
            if self.records is not None:
                self.records.append(item)
            else:
                for value in item:
                    self.file.write(np.asarray(value, order="F").tobytes(order="F"))
            if (i+1) % 32 == 0 or i == nodes-2:
                print(dict(full_QR_blocks=i+1, expected_blocks=nodes-1,
                    elapsed_seconds=time.monotonic()-tick,
                    factor_bytes=(i+1)*self.record_bytes,
                    factor_storage=storage,
                    peak_resident_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),
                    flush=True)
        if i != nodes-2:
            raise RuntimeError("incomplete collocation block stream")
        self.end = np.vstack((current, self.right_boundary))
        if self.end.shape != (n+1, n+1):
            raise RuntimeError("the complete final boundary Schur system is not square")
        self.end_condition = float(np.linalg.cond(self.end))
        with warnings.catch_warnings():
            warnings.simplefilter("error", LinAlgWarning)
            try:
                self.end_lu = lu_factor(self.end, check_finite=False)
            except (ValueError, LinAlgWarning) as error:
                raise RuntimeError(f"complete final boundary factor failed: {error}") from error
        if self.file:
            self.file.flush()
        item = dict(kind="full_boundary_row_QR_factorization", radial_nodes=nodes,
            state_dimension=n, parameter_dimension=1, left_rows=int(p),
            right_rows=int(len(self.right_rows)), complete_blocks=nodes-1,
            all_Fourier_couplings_retained=True, no_entry_drop=True,
            factor_storage=storage, factor_bytes=(nodes-1)*self.record_bytes,
            end_condition_2=self.end_condition,
            minimum_local_QR_diagonal=self.minimum_local_diagonal,
            seconds=time.monotonic()-tick)
        history.append(item)
        print(item, flush=True)

    def read(self, index):
        if self.records is not None:
            return self.records[index]
        self.file.seek(index*self.record_bytes)
        data = self.file.read(self.record_bytes)
        if len(data) != self.record_bytes:
            raise RuntimeError("incomplete temporary QR factor record")
        flat = np.frombuffer(data, dtype=np.float64)
        answer, start = [], 0
        for count, shape in zip(self.counts, self.shapes):
            answer.append(flat[start:start+count].reshape(shape, order="F"))
            start += count
        return answer

    def solve(self, residual):
        n, p, nodes = self.n, self.p, self.nodes
        if residual.shape != (n*nodes+1,):
            raise RuntimeError("wrong complete collocation residual dimension")
        body = residual[:n*(nodes-1)].reshape((n, nodes-1), order="F")
        boundary = residual[n*(nodes-1):]
        current = solve_triangular(self.initial_r.T, boundary[self.left_rows],
                                   lower=True, check_finite=False)
        top = np.empty((nodes-1, n))
        for i in range(nodes-1):
            packed, tau, _, _, norm_r, scale = self.read(i)
            result = apply_qt(packed, tau, np.r_[current, scale*body[:, i]])[:, 0]
            top[i] = result[:n]
            current = solve_triangular(norm_r.T, result[n:],
                                       lower=True, check_finite=False)
        end_rhs = np.r_[current, self.right_scale*boundary[self.right_rows]]
        end = lu_solve(self.end_lu, end_rhs, check_finite=False)
        parameter = float(end[-1])
        state = np.empty((n, nodes))
        state[:, -1] = end[:n]
        for i in range(nodes-2, -1, -1):
            packed, _, next_block, param, _, _ = self.read(i)
            state[:, i] = solve_triangular(packed[:n],
                top[i]-next_block@state[:, i+1]-param*parameter,
                lower=False, check_finite=False)
        answer = np.r_[state.ravel(order="F"), parameter]
        if not np.all(np.isfinite(answer)):
            raise RuntimeError("nonfinite full QR answer")
        return answer

    def __del__(self):
        if getattr(self, "file", None) is not None:
            self.file.close()


class CheckedFullQRSolve:
    def __init__(self, operator, factor, history):
        self.operator, self.factor, self.history = operator, factor, history

    def solve(self, residual):
        tick = time.monotonic()
        answer = self.factor.solve(residual)
        denom = max(float(np.linalg.norm(residual)), 1e-300)
        refinements = []
        for iteration in range(4):
            error = self.operator@answer-residual
            relative = float(np.linalg.norm(error)/denom)
            refinements.append(dict(iteration=iteration, full_relative_residual=relative,
                maximum_absolute_residual=float(np.max(abs(error)))))
            if relative <= 5e-8:
                break
            if iteration < 3:
                answer -= self.factor.solve(error)
        item = dict(kind="full_finite_collocation_QR_solve", refinements=refinements,
            full_relative_residual=relative, seconds=time.monotonic()-tick,
            all_finite_modes_and_parameter_column_retained=True,
            original_backward_residual_gate=5e-8, complete=bool(relative<=5e-8))
        self.history.append(item)
        print(item, flush=True)
        if not np.all(np.isfinite(answer)) or relative > 5e-8:
            raise RuntimeError("full collocation QR did not meet its backward-residual gate")
        return answer


def make_prepare_sys(mode_indices, *, system, band, drop, chunk, history,
                     storage="memory", scratch=None):
    # band and drop remain accepted CLI diagnostics; neither changes any entry.
    def prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
        if k != 1 or len(mode_indices) != n or m < 2:
            raise ValueError("this full branch has one metric parameter")
        system.current_mesh_x = x.copy()
        middle = x[:-1]+h/2

        def col_fun(y, p):
            return bvp.collocation_fun(fun, y, p, x, h)

        def jac(y, p, ym, f, fm, bc0):
            left, right, parameter = bc_jac(y[:, 0], y[:, -1], p)
            identity = np.eye(n)

            def blocks():
                for start in range(0, m-1, chunk):
                    stop = min(start+chunk, m-1)
                    df, dp = fun_jac(x[start:stop+1], y[:, start:stop+1], p)
                    dm, pm = fun_jac(middle[start:stop], ym[:, start:stop], p)
                    df, dm = np.moveaxis(df, 2, 0), np.moveaxis(dm, 2, 0)
                    dp, pm = np.moveaxis(dp, 2, 0), np.moveaxis(pm, 2, 0)
                    for j in range(stop-start):
                        hh = h[start+j]
                        a = -identity-hh*(df[j]+2*dm[j])/6-hh*hh*(dm[j]@df[j])/12
                        b = identity-hh*(df[j+1]+2*dm[j])/6+hh*hh*(dm[j]@df[j+1])/12
                        c = -hh*(dp[j]+dp[j+1]+4*pm[j])/6
                        c += hh*hh*(dm[j]@(dp[j+1]-dp[j]))/12
                        yield a, b, c[:, 0]
            factor = FullBoundaryQR(n, m, left, right, parameter, blocks(),
                                    history, storage=storage, scratch=scratch)
            endpoints = state_action(system, x, y, p)
            midpoints = state_action(system, middle, ym, p)

            def matvec(vector):
                v = vector[:n*m].reshape(n, m, order="F")
                dp = float(vector[-1])
                df = endpoints(v, dp)
                vm = (v[:, :-1]+v[:, 1:])/2-h*(df[:, 1:]-df[:, :-1])/8
                dm = midpoints(vm, dp)
                result = v[:, 1:]-v[:, :-1]-h*(df[:, :-1]+df[:, 1:]+4*dm)/6
                boundary = left@v[:, 0]+right@v[:, -1]+parameter[:, 0]*dp
                return np.r_[result.ravel(order="F"), boundary]

            operator = LinearOperator((n*m+1, n*m+1), matvec=matvec, dtype=float)
            return CheckedFullQRSolve(operator, factor, history)
        return col_fun, jac
    return prepare

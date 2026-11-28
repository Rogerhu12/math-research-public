"""Complete block QR with streaming absolute-matrix diagnostics.

All state variables, parameter columns and endpoint equations are retained.
No shooting propagation, rank truncation, damping, or change of BVP occurs.
The matrix has interval rows A_i y_i + B_i y_(i+1) + C_i p and endpoint rows.
Adjacent interval rows are orthogonally transformed to eliminate their shared
node, recursively.  Full-rank interior blocks follow from full-rank global J.
This is a finite numerical linear solver, not an inverse theorem for the PDE.
"""
from dataclasses import dataclass
import warnings

import numpy as np
from scipy.linalg import LinAlgWarning, get_lapack_funcs, lu_factor, lu_solve, qr, solve_triangular


@dataclass
class Edge:
    left: int
    right: int
    a: np.ndarray
    b: np.ndarray
    c: np.ndarray


@dataclass
class Elimination:
    left: int
    middle: int
    right: int
    householder: np.ndarray
    tau: np.ndarray
    pivot: np.ndarray
    top: np.ndarray


class BlockQR:
    def __init__(self, matrix, n, m, k, *, refinement=2):
        if n < 1 or m < 2 or k < 0 or matrix.shape != (n*m+k, n*m+k):
            raise ValueError('Collocation dimensions do not match')
        if np.iscomplexobj(matrix.data):
            raise ValueError('This implementation accepts real binary64 matrices')
        self.n, self.m, self.k = n, m, k
        self.matrix = matrix.tocsr()
        self.matrix.eliminate_zeros()
        if not np.all(np.isfinite(self.matrix.data)):
            raise FloatingPointError('Nonfinite collocation matrix')
        self.refinement = int(refinement)
        self.levels = []
        self.dormqr = get_lapack_funcs('ormqr', dtype=np.float64)
        self.work_sizes = {}
        self.stats = dict(equations=n*m+k, state_size=n, nodes=m, parameters=k,
                          internal_nodes_eliminated=0, levels=0,
                          minimum_relative_R_diagonal=1., solve_calls=0,
                          maximum_componentwise_backward_error=0.,
                          maximum_normwise_backward_error=0., refinement_steps=0)
        edges = []
        for i in range(m-1):
            row = self.matrix[i*n:(i+1)*n]
            valid = ((row.indices >= i*n) & (row.indices < (i+2)*n)) | (row.indices >= n*m)
            if not np.all(valid):
                raise ValueError('An interval row contains a nonlocal state column')
            edges.append(Edge(i, i+1,
                              row[:, i*n:(i+1)*n].toarray(),
                              row[:, (i+1)*n:(i+2)*n].toarray(),
                              row[:, n*m:].toarray()))
        endpoint = self.matrix[(m-1)*n:]
        valid = (endpoint.indices < n) | (endpoint.indices >= (m-1)*n)
        if not np.all(valid):
            raise ValueError('An endpoint row contains an interior state column')
        self.endpoint = np.hstack((endpoint[:, :n].toarray(),
                                   endpoint[:, (m-1)*n:m*n].toarray(),
                                   endpoint[:, m*n:].toarray()))
        while len(edges) > 1:
            level, remaining = [], []
            for i in range(0, len(edges)-1, 2):
                left, right = edges[i:i+2]
                assert left.right == right.left
                interior = np.asfortranarray(np.vstack((left.b, right.a)))
                (hh, tau), upper, pivot = qr(interior, mode='raw', pivoting=True,
                                            overwrite_a=True, check_finite=False)
                diag = np.abs(np.diag(upper))
                if not np.all(np.isfinite(diag)) or np.any(diag == 0):
                    raise RuntimeError('Singular interior block; no direction was removed')
                ratio = float(diag.min()/max(np.abs(upper).max(), np.finfo(float).tiny))
                self.stats['minimum_relative_R_diagonal'] = min(
                    self.stats['minimum_relative_R_diagonal'], ratio)
                boundary = np.zeros((2*n, 2*n+k), order='F')
                boundary[:n, :n], boundary[n:, n:2*n] = left.a, right.b
                boundary[:n, 2*n:], boundary[n:, 2*n:] = left.c, right.c
                transformed = self._apply(hh, tau, boundary)
                level.append(Elimination(left.left, left.right, right.right,
                                          hh, tau, pivot, transformed[:n].copy()))
                remaining.append(Edge(left.left, right.right,
                                       transformed[n:, :n].copy(),
                                       transformed[n:, n:2*n].copy(),
                                       transformed[n:, 2*n:].copy()))
                self.stats['internal_nodes_eliminated'] += 1
            if len(edges) % 2:
                level.append(None)
                remaining.append(edges[-1])
            self.levels.append(level)
            edges = remaining
        final = edges[0]
        assert final.left == 0 and final.right == m-1
        reduced = np.vstack((np.hstack((final.a, final.b, final.c)), self.endpoint))
        self.reduced = reduced
        self.row_scale = np.max(np.abs(reduced), axis=1)
        if np.any(self.row_scale == 0):
            raise RuntimeError('Singular complete endpoint system')
        normalized = reduced / self.row_scale[:, None]
        self.col_scale = np.max(np.abs(normalized), axis=0)
        if np.any(self.col_scale == 0):
            raise RuntimeError('Singular complete endpoint system')
        normalized = normalized / self.col_scale[None, :]
        with warnings.catch_warnings():
            warnings.simplefilter('error', LinAlgWarning)
            try:
                self.final_factor = lu_factor(normalized, check_finite=False)
            except (LinAlgWarning, ValueError) as exc:
                raise RuntimeError('Singular complete endpoint system') from exc
        self.stats['levels'] = len(self.levels)
        self.stats['stored_factor_bytes'] = sum(
            item.householder.nbytes + item.tau.nbytes + item.pivot.nbytes + item.top.nbytes
            for level in self.levels for item in level if item is not None)
        # Preserve the original per-row sparse summation and matvec order,
        # without retaining a second full CSR solely for diagnostics.
        self.diagnostic_rows = 2048
        self.matrix_inf = self._absolute_row_sum_max()

    def _absolute_blocks(self):
        for first in range(0, self.matrix.shape[0], self.diagnostic_rows):
            stop = min(self.matrix.shape[0], first + self.diagnostic_rows)
            block = self.matrix[first:stop]
            np.absolute(block.data, out=block.data)
            yield first, stop, block

    def _absolute_row_sum_max(self):
        maximum = 0.
        for first, stop, block in self._absolute_blocks():
            maximum = max(maximum, float(np.max(np.asarray(block.sum(axis=1)))))
        return maximum

    def _absolute_matvec(self, vector):
        result = np.empty(self.matrix.shape[0], dtype=float)
        for first, stop, block in self._absolute_blocks():
            result[first:stop] = block @ vector
        return result

    def _apply(self, hh, tau, values):
        values = np.asarray(values, dtype=float, order='F')
        shape = values.shape
        if shape not in self.work_sizes:
            _, work, info = self.dormqr('L', 'T', hh, tau, values, -1)
            if info:
                raise RuntimeError('LAPACK QR workspace query failed')
            self.work_sizes[shape] = max(1, int(work[0]))
        transformed, _, info = self.dormqr('L', 'T', hh, tau, values,
                                          self.work_sizes[shape], overwrite_c=True)
        if info:
            raise RuntimeError('LAPACK orthogonal transformation failed')
        return transformed

    def _solve(self, rhs):
        n, m, k = self.n, self.m, self.k
        intervals = [rhs[i*n:(i+1)*n] for i in range(m-1)]
        saved = []
        for level in self.levels:
            next_rhs, eliminated_rhs, cursor = [], [], 0
            for item in level:
                if item is None:
                    next_rhs.append(intervals[cursor])
                    eliminated_rhs.append(None)
                    cursor += 1
                else:
                    pair = np.concatenate(intervals[cursor:cursor+2])[:, None]
                    transformed = self._apply(item.householder, item.tau, pair)[:, 0]
                    eliminated_rhs.append(transformed[:n].copy())
                    next_rhs.append(transformed[n:].copy())
                    cursor += 2
            assert cursor == len(intervals)
            saved.append(eliminated_rhs)
            intervals = next_rhs
        final_rhs = np.r_[intervals[0], rhs[(m-1)*n:]]
        endpoints = lu_solve(self.final_factor, final_rhs/self.row_scale,
                             check_finite=False) / self.col_scale
        states = np.empty((m, n))
        states[0], states[-1] = endpoints[:n], endpoints[n:2*n]
        parameters = endpoints[2*n:]
        for level, rr in zip(reversed(self.levels), reversed(saved)):
            for item, interior_rhs in zip(level, rr):
                if item is None:
                    continue
                outer = np.r_[states[item.left], states[item.right], parameters]
                value = solve_triangular(item.householder[:n, :],
                                          interior_rhs-item.top@outer,
                                          lower=False, check_finite=False)
                states[item.middle, item.pivot] = value
        return np.r_[states.ravel(), parameters]

    def solve(self, rhs):
        rhs = np.asarray(rhs, dtype=float)
        if rhs.shape != (self.n*self.m+self.k,) or not np.all(np.isfinite(rhs)):
            raise ValueError('One complete finite real right hand side is required')
        answer = self._solve(rhs)
        for iteration in range(self.refinement+1):
            residual = rhs-self.matrix@answer
            normwise = float(np.max(np.abs(residual))/max(
                self.matrix_inf*np.max(np.abs(answer))+np.max(np.abs(rhs)),
                np.finfo(float).tiny))
            denominator = self._absolute_matvec(np.abs(answer))+np.abs(rhs)
            componentwise = float(np.max(np.abs(residual)/np.maximum(
                denominator, np.finfo(float).tiny)))
            # Pure homogeneous endpoint rows can have componentwise ratio one
            # at subnormal absolute errors.  Keep that diagnostic visible, and
            # stop by the actual residual relative to the requested RHS rather
            # than hiding it behind the (possibly large) global matrix norm.
            if (np.max(np.abs(residual)) <= 8*np.finfo(float).eps*max(
                    np.max(np.abs(rhs)), np.finfo(float).tiny)
                    or iteration == self.refinement):
                break
            correction = self._solve(residual)
            if not np.all(np.isfinite(correction)):
                raise FloatingPointError('Nonfinite complete-system residual correction')
            answer += correction
            self.stats['refinement_steps'] += 1
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError('Nonfinite complete collocation direction')
        self.stats['solve_calls'] += 1
        self.stats['maximum_componentwise_backward_error'] = max(
            self.stats['maximum_componentwise_backward_error'], componentwise)
        self.stats['maximum_normwise_backward_error'] = max(
            self.stats['maximum_normwise_backward_error'], normwise)
        return answer

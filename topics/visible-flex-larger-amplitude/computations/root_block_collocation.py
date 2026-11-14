"""The unchanged SciPy collocation Jacobian in adjacent dense blocks.

This optional storage backend avoids global COO/CSC/CSR arrays and their
indices. Pointwise analytic Jacobians are evaluated in independent radial
batches. The collocation, parameter and endpoint formulas are those in
scipy.integrate._bvp.construct_global_jac; acceptance is not changed.
"""
from __future__ import annotations
import inspect
import numpy as np
from scipy.integrate import _bvp
from scipy.linalg import lu_factor
from scipy.linalg.lapack import dgeqrf, dormqr
from strong_block_qr import BlockQRFactor, _Node


class BlockJacobian:
    def __init__(self, a, b, c, boundary_a, boundary_b, boundary_p):
        self.a, self.b, self.c = a, b, c
        self.boundary_a, self.boundary_b, self.boundary_p = boundary_a, boundary_b, boundary_p
        self.intervals, self.n = a.shape[:2]
        self.nodes = self.intervals + 1
        self.parameters = c.shape[2]
        self.shape = (self.n * self.nodes + self.parameters,) * 2

    def matvec(self, value):
        n, m = self.n, self.nodes
        v = np.asarray(value)
        y, p = v[:n*m].reshape(m, n), v[n*m:]
        interior = (np.einsum('mij,mj->mi', self.a, y[:-1])
                    + np.einsum('mij,mj->mi', self.b, y[1:])
                    + np.einsum('mik,k->mi', self.c, p))
        boundary = self.boundary_a @ y[0] + self.boundary_b @ y[-1] + self.boundary_p @ p
        return np.r_[interior.ravel(), boundary]

    def to_sparse(self):
        """Diagnostic only: materialize precisely the original sparse layout."""
        from scipy.sparse import coo_matrix, csc_matrix
        n, m, k = self.n, self.nodes, self.parameters
        i, j = _bvp.compute_jac_indices(n, m, k)
        values = np.hstack((self.a.ravel(), self.b.ravel(),
                            self.boundary_a.ravel(), self.boundary_b.ravel()))
        if k:
            values = np.hstack((values, self.c.ravel(), self.boundary_p.ravel()))
        return csc_matrix(coo_matrix((values, (i, j)), shape=self.shape))


def prepare_sys(n, m, k, fun, bc, fun_jac, bc_jac, x, h, batch_size=24):
    x_middle = x[:-1] + .5 * h

    def col_fun(y, p):
        return _bvp.collocation_fun(fun, y, p, x, h)

    def sys_jac(y, p, y_middle, f, f_middle, bc0):
        a = np.empty((m - 1, n, n), dtype=y.dtype)
        b = np.empty_like(a)
        c = np.empty((m - 1, n, k), dtype=y.dtype)
        identity = np.identity(n)
        for lo in range(0, m - 1, batch_size):
            hi = min(lo + batch_size, m - 1)
            nodes, mids = slice(lo, hi + 1), slice(lo, hi)
            if fun_jac is None:
                dy, dp = _bvp.estimate_fun_jac(fun, x[nodes], y[:, nodes], p, f[:, nodes])
                dym, dpm = _bvp.estimate_fun_jac(fun, x_middle[mids], y_middle[:, mids], p, f_middle[:, mids])
            else:
                dy, dp = fun_jac(x[nodes], y[:, nodes], p)
                dym, dpm = fun_jac(x_middle[mids], y_middle[:, mids], p)
            dy, dym = dy.transpose(2, 0, 1), dym.transpose(2, 0, 1)
            hh = h[mids, None, None]
            aa, bb = a[mids], b[mids]
            aa[:] = -identity
            aa -= hh / 6 * (dy[:-1] + 2 * dym)
            aa -= hh**2 / 12 * _bvp.stacked_matmul(dym, dy[:-1])
            bb[:] = identity
            bb -= hh / 6 * (dy[1:] + 2 * dym)
            bb += hh**2 / 12 * _bvp.stacked_matmul(dym, dy[1:])
            if k:
                dp, dpm = dp.transpose(2, 0, 1), dpm.transpose(2, 0, 1)
                # Do not retain a view of a caller-owned derivative array.
                dpm = dpm + .125 * hh * _bvp.stacked_matmul(dym, dp[:-1] - dp[1:])
                c[mids] = -hh / 6 * (dp[:-1] + dp[1:] + 4 * dpm)
        if bc_jac is None:
            ba, bb, bp = _bvp.estimate_bc_jac(bc, y[:, 0], y[:, -1], p, bc0)
        else:
            ba, bb, bp = bc_jac(y[:, 0], y[:, -1], p)
        return BlockJacobian(a, b, c, ba, bb, bp)

    return col_fun, sys_jac


class DirectBlockQRFactor(BlockQRFactor):
    """Same balanced orthogonal elimination, with no sparse matrix copy."""
    def __init__(self, matrix, n, nodes, parameters):
        if not isinstance(matrix, BlockJacobian):
            raise TypeError('Direct block QR requires the matching block Jacobian')
        n, m, k = int(n), int(nodes), int(parameters)
        if (n, m, k) != (matrix.n, matrix.nodes, matrix.parameters):
            raise ValueError('Block Jacobian dimensions differ')
        self.n, self.nodes, self.parameters = n, m, k
        self.dimension = n*m+k

        def build(lo, hi):
            node = _Node(lo, hi)
            if hi == lo + 1:
                node.a, node.b, node.c = matrix.a[lo], matrix.b[lo], matrix.c[lo]
                return node
            mid = (lo + hi) // 2
            node.left, node.right = build(lo, mid), build(mid, hi)
            left, right = node.left, node.right
            center = np.asfortranarray(np.vstack((left.b, right.a)))
            _, _, work, info = dgeqrf(center, lwork=-1, overwrite_a=False)
            if info:
                raise np.linalg.LinAlgError('dgeqrf workspace query failed')
            qr, tau, _, info = dgeqrf(center, lwork=max(n, int(work[0])), overwrite_a=True)
            if info:
                raise np.linalg.LinAlgError('dgeqrf failed')
            node.qr, node.tau = qr, tau
            sides = np.zeros((2*n, 2*n+k), order='F')
            sides[:n, :n], sides[n:, n:2*n] = left.a, right.b
            sides[:n, 2*n:], sides[n:, 2*n:] = left.c, right.c
            _, work, info = dormqr('L', 'T', qr, tau, sides, lwork=-1, overwrite_c=False)
            if info:
                raise np.linalg.LinAlgError('dormqr workspace query failed')
            node.work = max(2*n+k, int(work[0]))
            transformed = node.qt(sides)
            node.top_a, node.top_b, node.top_c = (transformed[:n, :n].copy(),
                transformed[:n, n:2*n].copy(), transformed[:n, 2*n:].copy())
            node.a, node.b, node.c = (transformed[n:, :n].copy(),
                transformed[n:, n:2*n].copy(), transformed[n:, 2*n:].copy())
            for child in (left, right):
                child.a = child.b = child.c = None
            return node

        try:
            self.root = build(0, m - 1)
        finally:
            build = None
        boundary = np.hstack((matrix.boundary_a, matrix.boundary_b, matrix.boundary_p))
        final = np.vstack((np.hstack((self.root.a, self.root.b, self.root.c)), boundary))
        self.final_lu = lu_factor(final, check_finite=True)
        self.root.a = self.root.b = self.root.c = None
        self.stats = dict(kind='direct-block-balanced-local-QR', n=n, nodes=m,
                         parameters=k, root_dimension=2*n+k, internal_nodes=m-2)


def install():
    wanted = ['n', 'm', 'k', 'fun', 'bc', 'fun_jac', 'bc_jac', 'x', 'h']
    if list(inspect.signature(_bvp.prepare_sys).parameters) not in (wanted, wanted + ['batch_size']):
        raise RuntimeError('Installed SciPy preparation signature differs')
    _bvp.prepare_sys = prepare_sys

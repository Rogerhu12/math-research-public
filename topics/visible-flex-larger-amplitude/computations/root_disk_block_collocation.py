"""Optional disk storage for the unchanged real collocation and balanced QR.

No equation, Newton rule or nonlinear acceptance is changed. Original dense
adjacent blocks and QR data are stored as exact float64 bytes in anonymous
temporary files. Only a radial batch, a logarithmic stack of coarse blocks
and solve vectors remain in process memory. This module is not installed by
importing it and is not connected to a production driver by default.
"""
from __future__ import annotations
from dataclasses import dataclass
import os
import tempfile
import numpy as np
from scipy.integrate import _bvp
from scipy.linalg import lu_factor
from scipy.linalg.lapack import dgeqrf, dormqr
from strong_block_qr import BlockQRFactor
from root_block_collocation import BlockJacobian


@dataclass(frozen=True)
class _Reference:
    offset: int
    shape: tuple
    order: str
    size: int


class _Arena:
    def __init__(self, directory=None):
        self.file = tempfile.TemporaryFile(prefix='visible-flex-blocks-', dir=directory)
        self.size = 0
        self.written = self.read_bytes = 0

    def reserve(self, shape, order='C'):
        shape = tuple(map(int, shape))
        if any(n < 0 for n in shape) or order not in ('C', 'F'):
            raise ValueError('Invalid stored array shape or order')
        count = int(np.prod(shape, dtype=np.int64))
        result = _Reference(self.size, shape, order, count*8)
        self.size += result.size
        self.file.truncate(self.size)
        return result

    def _write(self, offset, data):
        view = memoryview(data)
        while view:
            count = os.pwrite(self.file.fileno(), view, offset)
            if count <= 0:
                raise OSError('Short temporary block write')
            offset += count
            self.written += count
            view = view[count:]

    def _read(self, offset, size):
        pieces = []
        remaining = size
        while remaining:
            piece = os.pread(self.file.fileno(), remaining, offset)
            if not piece:
                raise OSError('Short temporary block read')
            pieces.append(piece)
            offset += len(piece)
            remaining -= len(piece)
            self.read_bytes += len(piece)
        return b''.join(pieces)

    def save(self, values, order='C'):
        values = np.asarray(values)
        if values.dtype != np.dtype('float64'):
            raise TypeError('Only original real float64 arrays are supported')
        ref = self.reserve(values.shape, order)
        self._write(ref.offset, values.tobytes(order=order))
        return ref

    def load(self, ref):
        data = self._read(ref.offset, ref.size)
        return np.frombuffer(data, dtype=np.float64).reshape(ref.shape, order=ref.order).copy(order=ref.order)

    def close(self):
        if not self.file.closed:
            self.file.close()

    def __del__(self):
        self.close()


class _Rows:
    def __init__(self, arena, shape):
        self.arena = arena
        self.reference = arena.reserve(shape)
        self.shape = self.reference.shape
        self.row_bytes = int(np.prod(self.shape[1:], dtype=np.int64))*8

    def __getitem__(self, key):
        if isinstance(key, (int, np.integer)):
            lo = int(key)
            if lo < 0:
                lo += self.shape[0]
            if not 0 <= lo < self.shape[0]:
                raise IndexError('Stored row index out of range')
            return self[slice(lo, lo+1)][0]
        if not isinstance(key, slice):
            raise TypeError('Stored block rows support only integer or contiguous slice access')
        lo, hi, step = key.indices(self.shape[0])
        if step != 1 or hi < lo:
            raise ValueError('Stored block rows require a forward contiguous slice')
        data = self.arena._read(self.reference.offset+lo*self.row_bytes, (hi-lo)*self.row_bytes)
        return np.frombuffer(data, dtype=np.float64).reshape((hi-lo, *self.shape[1:])).copy()

    def write(self, lo, values):
        values = np.asarray(values)
        if (values.dtype != np.dtype('float64') or values.shape[1:] != self.shape[1:] or
                lo < 0 or lo+values.shape[0] > self.shape[0]):
            raise ValueError('Stored block write has wrong shape, dtype or range')
        self.arena._write(self.reference.offset+lo*self.row_bytes, values.tobytes(order='C'))


class DiskBlockJacobian(BlockJacobian):
    def __init__(self, arena, a, b, c, boundary_a, boundary_b, boundary_p, batch_size):
        super().__init__(a, b, c, boundary_a, boundary_b, boundary_p)
        self.storage = arena
        self.batch_size = batch_size

    def matvec(self, value):
        n, m = self.n, self.nodes
        v = np.asarray(value)
        y, p = v[:n*m].reshape(m, n), v[n*m:]
        interior = np.empty((m-1, n), dtype=float)
        for lo in range(0, m-1, self.batch_size):
            hi = min(lo+self.batch_size, m-1)
            interior[lo:hi] = (np.einsum('mij,mj->mi', self.a[lo:hi], y[lo:hi])
                + np.einsum('mij,mj->mi', self.b[lo:hi], y[lo+1:hi+1])
                + np.einsum('mik,k->mi', self.c[lo:hi], p))
        boundary = self.boundary_a@y[0]+self.boundary_b@y[-1]+self.boundary_p@p
        return np.r_[interior.ravel(), boundary]

    def to_sparse(self):
        if self.storage.size > 32*1024**2:
            raise MemoryError('Diagnostic sparse materialization is limited to32MiB of original blocks')
        return BlockJacobian(self.a[:], self.b[:], self.c[:], self.boundary_a,
                             self.boundary_b, self.boundary_p).to_sparse()


def prepare_sys(n, m, k, fun, bc, fun_jac, bc_jac, x, h, batch_size=24, directory=None):
    """Same original preparation formulas, with explicit streamed block writes."""
    x_middle = x[:-1]+.5*h

    def col_fun(y, p):
        return _bvp.collocation_fun(fun, y, p, x, h)

    def sys_jac(y, p, y_middle, f, f_middle, bc0):
        if y.dtype != np.dtype('float64') or n < 1 or m < 2 or k < 0 or batch_size < 1:
            raise ValueError('Expected a nonempty real float64 collocation problem')
        arena = _Arena(directory)
        a, b = _Rows(arena, (m-1, n, n)), _Rows(arena, (m-1, n, n))
        c = _Rows(arena, (m-1, n, k))
        identity = np.identity(n)
        for lo in range(0, m-1, batch_size):
            hi = min(lo+batch_size, m-1)
            nodes, mids = slice(lo, hi+1), slice(lo, hi)
            if fun_jac is None:
                dy, dp = _bvp.estimate_fun_jac(fun, x[nodes], y[:, nodes], p, f[:, nodes])
                dym, dpm = _bvp.estimate_fun_jac(fun, x_middle[mids], y_middle[:, mids], p, f_middle[:, mids])
            else:
                dy, dp = fun_jac(x[nodes], y[:, nodes], p)
                dym, dpm = fun_jac(x_middle[mids], y_middle[:, mids], p)
            dy, dym = dy.transpose(2, 0, 1), dym.transpose(2, 0, 1)
            hh = h[mids, None, None]
            aa, bb = np.empty((hi-lo, n, n)), np.empty((hi-lo, n, n))
            aa[:] = -identity
            aa -= hh/6*(dy[:-1]+2*dym)
            aa -= hh**2/12*_bvp.stacked_matmul(dym, dy[:-1])
            bb[:] = identity
            bb -= hh/6*(dy[1:]+2*dym)
            bb += hh**2/12*_bvp.stacked_matmul(dym, dy[1:])
            a.write(lo, aa); b.write(lo, bb)
            if k:
                dp, dpm = dp.transpose(2, 0, 1), dpm.transpose(2, 0, 1)
                dpm = dpm+.125*hh*_bvp.stacked_matmul(dym, dp[:-1]-dp[1:])
                c.write(lo, -hh/6*(dp[:-1]+dp[1:]+4*dpm))
        if bc_jac is None:
            ba, bb, bp = _bvp.estimate_bc_jac(bc, y[:, 0], y[:, -1], p, bc0)
        else:
            ba, bb, bp = bc_jac(y[:, 0], y[:, -1], p)
        return DiskBlockJacobian(arena, a, b, c, ba, bb, bp, batch_size)

    return col_fun, sys_jac


class _DiskNode:
    def __init__(self, lo, hi, storage):
        self.lo, self.hi, self.storage = lo, hi, storage
        self.left = self.right = None
        self.a = self.b = self.c = None
        self.work = 1
        self.refs = {}

    def keep(self, name, value, order='C'):
        self.refs[name] = self.storage.save(value, order)

    def __getattr__(self, name):
        if name in ('qr', 'tau', 'top_a', 'top_b', 'top_c'):
            return self.storage.load(self.refs[name])
        raise AttributeError(name)

    def qt(self, values):
        values = np.array(values, dtype=float, order='F', copy=True)
        if values.ndim == 1:
            values = values[:, None]
        out, unused, info = dormqr('L', 'T', self.qr, self.tau, values,
                                   lwork=self.work, overwrite_c=True)
        if info:
            raise np.linalg.LinAlgError('Disk dormqr failed: '+str(info))
        return out


class DiskDirectBlockQRFactor(BlockQRFactor):
    """The same balanced elimination and inherited original solve traversal."""
    def __init__(self, matrix, n, nodes, parameters, directory=None):
        if not isinstance(matrix, BlockJacobian):
            raise TypeError('An original or disk BlockJacobian is required')
        n, m, k = int(n), int(nodes), int(parameters)
        if (n, m, k) != (matrix.n, matrix.nodes, matrix.parameters):
            raise ValueError('Block dimensions differ')
        self.n, self.nodes, self.parameters = n, m, k
        self.dimension = n*m+k
        self.storage = _Arena(directory)

        def build(lo, hi):
            node = _DiskNode(lo, hi, self.storage)
            if hi == lo+1:
                node.a, node.b, node.c = matrix.a[lo], matrix.b[lo], matrix.c[lo]
                return node
            mid = (lo+hi)//2
            node.left, node.right = build(lo, mid), build(mid, hi)
            left, right = node.left, node.right
            center = np.asfortranarray(np.vstack((left.b, right.a)))
            unused1, unused2, work, info = dgeqrf(center, lwork=-1, overwrite_a=False)
            if info:
                raise np.linalg.LinAlgError('dgeqrf workspace query failed')
            qr, tau, unused, info = dgeqrf(center, lwork=max(n, int(work[0])), overwrite_a=True)
            if info:
                raise np.linalg.LinAlgError('dgeqrf failed')
            node.keep('qr', qr, 'F'); node.keep('tau', tau)
            sides = np.zeros((2*n, 2*n+k), order='F')
            sides[:n, :n], sides[n:, n:2*n] = left.a, right.b
            sides[:n, 2*n:], sides[n:, 2*n:] = left.c, right.c
            unused, work, info = dormqr('L', 'T', qr, tau, sides, lwork=-1, overwrite_c=False)
            if info:
                raise np.linalg.LinAlgError('dormqr workspace query failed')
            node.work = max(2*n+k, int(work[0]))
            transformed = node.qt(sides)
            for name, part in (('top_a', transformed[:n, :n]),
                               ('top_b', transformed[:n, n:2*n]),
                               ('top_c', transformed[:n, 2*n:])):
                node.keep(name, part)
            node.a, node.b, node.c = (transformed[n:, :n].copy(),
                transformed[n:, n:2*n].copy(), transformed[n:, 2*n:].copy())
            for child in (left, right):
                child.a = child.b = child.c = None
            return node

        try:
            self.root = build(0, m-1)
        finally:
            build = None
        boundary = np.hstack((matrix.boundary_a, matrix.boundary_b, matrix.boundary_p))
        final = np.vstack((np.hstack((self.root.a, self.root.b, self.root.c)), boundary))
        self.final_lu = lu_factor(final, check_finite=True)
        self.root.a = self.root.b = self.root.c = None
        self.stats = dict(kind='disk-direct-block-balanced-local-QR', n=n, nodes=m,
            parameters=k, root_dimension=2*n+k, internal_nodes=m-2,
            stored_factor_bytes=self.storage.size, exact_original_float64_bytes=True,
            original_solve_traversal_inherited=True)

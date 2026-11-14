#!/usr/bin/env python3
"""Small real nonlinear collocation comparisons; no research BVP is solved."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gc
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np
from scipy.sparse.linalg import splu
import root_block_collocation as original
import root_disk_block_collocation as disk


def check(n, m, k, seed, analytic=True):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, n))*.07-np.eye(n)*.2
    B = rng.normal(size=(n, k))*.1
    x = np.linspace(0, 1, m)**1.4
    h = np.diff(x)
    y, p = rng.normal(size=(n, m))*.1, rng.normal(size=k)*.1
    extra = np.eye(n)[:k]

    def fun(t, v, q):
        return A@v+.02*v*v+(B@(q+q*q))[:, None]*(1+t)[None, :]

    def jac(t, v, q):
        dy = np.repeat(A[:, :, None], len(t), axis=2)
        dy[np.arange(n), np.arange(n), :] += .04*v
        dp = B[:, :, None]*(1+2*q)[None, :, None]*(1+t)[None, None, :]
        return dy, dp

    def bc(ya, yb, q):
        return np.r_[ya+.1*yb, q+.03*extra@yb]

    def bc_jac(ya, yb, q):
        return (np.vstack((np.eye(n), np.zeros((k, n)))),
                np.vstack((.1*np.eye(n), .03*extra)),
                np.vstack((np.zeros((n, k)), np.eye(k))))

    # The original block implementation requires an explicit empty boundary
    # parameter matrix when k=0; SciPy's estimator returns None in that case.
    args = n, m, k, fun, bc, jac if analytic else None, bc_jac if analytic or k == 0 else None, x, h
    col, prepare = original.prepare_sys(*args, batch_size=4)
    disk_col, disk_prepare = disk.prepare_sys(*args, batch_size=4)
    values = col(y, p)
    assert all(np.array_equal(a, b) for a, b in zip(values, disk_col(y, p)))
    cr, ym, ff, fm = values
    before_fd = len(os.listdir('/proc/self/fd')) if Path('/proc/self/fd').exists() else None
    J = prepare(y, p, ym, ff, fm, bc(y[:, 0], y[:, -1], p))
    D = disk_prepare(y, p, ym, ff, fm, bc(y[:, 0], y[:, -1], p))
    same_blocks = {key: bool(np.array_equal(getattr(J, key), getattr(D, key)[:]))
                   for key in ('a', 'b', 'c')}
    same_boundary = all(np.array_equal(getattr(J, key), getattr(D, key))
                        for key in ('boundary_a', 'boundary_b', 'boundary_p'))
    assert all(same_blocks.values()) and same_boundary
    v = rng.normal(size=n*m+k)
    same_matvec = np.array_equal(J.matvec(v), D.matvec(v))
    assert same_matvec
    factor = original.DirectBlockQRFactor(J, n, m, k)
    stored = disk.DiskDirectBlockQRFactor(D, n, m, k)
    rhs = rng.normal(size=(n*m+k, 3))
    a, b = factor.solve(rhs), stored.solve(rhs)
    vector_identical = np.array_equal(factor.solve(rhs[:, 0]), stored.solve(rhs[:, 0]))
    matrix_identical = np.array_equal(a, b)
    assert vector_identical and matrix_identical
    sparse = J.to_sparse()
    direct = splu(sparse).solve(rhs)
    residual = float(np.max(abs(sparse@b-rhs)))
    relative = float(np.max(abs(b-direct))/(1+np.max(abs(direct))))
    assert residual < 2e-11 and relative < 2e-11
    original_bytes = D.storage.size
    factor_bytes = stored.storage.size
    del D, stored
    gc.collect()
    after_fd = len(os.listdir('/proc/self/fd')) if before_fd is not None else None
    assert before_fd is None or before_fd == after_fd
    return dict(n=n, nodes=m, parameters=k, analytic_jacobian=analytic,
        explicit_empty_boundary_parameter_matrix_when_k_zero=True,
        all_original_blocks_bitwise_same=same_blocks, boundary_bitwise_same=same_boundary,
        original_matvec_bitwise_same=bool(same_matvec),
        original_vector_solve_bitwise_same=bool(vector_identical),
        original_multi_rhs_solve_bitwise_same=bool(matrix_identical),
        sparse_solve_relative_difference=relative, max_backward_residual=residual,
        stored_jacobian_bytes=original_bytes, stored_factor_bytes=factor_bytes,
        temporary_descriptors_closed=before_fd is None or before_fd == after_fd)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh check output')
    started = time.monotonic()
    rows = [check(5, 17, 0, 12345, False), check(7, 33, 3, 12346), check(9, 2, 2, 12347)]
    here = Path(__file__).parent
    record = dict(scope=__doc__, cases=rows, all_checks_passed=True,
        actual_research_jacobian_checked=False, production_connected=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        source_sha256={str(here/n): hashlib.sha256((here/n).read_bytes()).hexdigest()
                       for n in ('root_disk_block_storage_check.py', 'root_disk_block_collocation.py',
                                 'root_block_collocation.py', 'strong_block_qr.py')})
    args.out.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record))


if __name__ == '__main__':
    main()

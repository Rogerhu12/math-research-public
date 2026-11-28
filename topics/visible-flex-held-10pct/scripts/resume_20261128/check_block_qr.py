#!/usr/bin/env python3
"""Compare the complete QR solve on an actual saved collocation input.

Reconstructs the original portable problem and Jacobian, and compares a single
linear direction with SuperLU. No BVP step is applied or accepted. Generated
matrices, snapshots and states stay in scratch; only scalar records are needed
in the repository. A deterministic small-system check covers tree parities.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy.integrate import _bvp
from scipy.sparse import csc_matrix, save_npz
from scipy.sparse.linalg import splu
from block_qr import BlockQR


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def small_checks():
    rng = np.random.default_rng(20261128)
    reports = []
    for n, m, k in ((3, 2, 2), (3, 3, 2), (3, 4, 2), (3, 7, 2),
                    (3, 12, 2), (3, 65, 2), (2, 9, 0)):
        total = n*m+k
        J = np.zeros((total, total))
        for i in range(m-1):
            rr = slice(i*n, (i+1)*n)
            J[rr, i*n:(i+1)*n] = -np.eye(n)+.03*rng.normal(size=(n, n))
            J[rr, (i+1)*n:(i+2)*n] = np.eye(n)+.03*rng.normal(size=(n, n))
            J[rr, n*m:] = .03*rng.normal(size=(n, k))
        r = (m-1)*n
        J[r:r+n, :n] = np.eye(n)
        J[r:r+n, n*m:] = rng.normal(size=(n, k))
        J[r+n:, (m-1)*n:m*n] = rng.normal(size=(k, n))
        J[r+n:, n*m:] = np.eye(k)
        exact = rng.normal(size=total)
        factor = BlockQR(csc_matrix(J), n, m, k)
        actual = factor.solve(J@exact)
        error = float(np.max(np.abs(actual-exact)))
        if error > 2e-10:
            raise AssertionError((n, m, k, error))
        reports.append(dict(n=n, m=m, k=k, absolute_solution_error=error,
                            residual_max=float(np.max(np.abs(J@actual-J@exact)))))
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run', type=Path)
    parser.add_argument('--snapshot', type=Path)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=False)
    summary = dict(scope=__doc__, small_systems=small_checks(),
                   source_sha256=digest(__file__),
                   factor_sha256=digest(Path(__file__).with_name('block_qr.py')),
                   BVP_steps_applied=0, complete_surface=False)
    destination = args.outdir/'summary.json'
    destination.write_text(json.dumps(summary, indent=2)+'\n')
    if args.source_run is None:
        return
    if args.snapshot is None:
        raise ValueError('A saved actual Jacobian input is required')
    source = json.loads(args.source_run.read_text())
    command = list(source['command'][2:])
    scripts = Path(__file__).resolve().parents[1]
    portable = scripts/'resume_m3/portable_prefix_continue.py'
    original = load('_qr_check_original_problem', portable)
    captured = {}
    def capture(obj, x, y, p):
        captured.update(obj=obj, x=x, y=y, p=p)
    text = inspect.getsource(original.main)
    marker = '        rhs = o.fun(x,y,par)'
    assert text.count(marker) == 1
    modified = text.replace(marker, '        _qr_capture(o,x,y,par)\n        return')
    original.__dict__['_qr_capture'] = capture
    exec(compile(modified, str(portable)+'::capture_without_solver', 'exec'), original.__dict__)
    command[command.index('--outdir')+1] = str(args.outdir/'problem-construction')
    for name in ('--restart-checkpoint', '--raw-restart'):
        if name in command:
            idx = command.index(name)
            del command[idx:idx+2]
    command += ['--raw-restart', str(args.snapshot.resolve())]
    sys.argv = [str(portable), *command]
    original.main()
    obj, x, y, p = (captured[name] for name in ('obj', 'x', 'y', 'p'))
    batches = load('_qr_check_original_batches',
                   scripts/'resume_20261126/streamed_release_prefix_driver.py')
    wrapped = _bvp.wrap_functions(batches.split_rhs(obj.fun, 8), obj.bc,
                                  batches.split_jac(obj.fun_jac, 8), obj.bc_jac,
                                  len(p), x[0], None, None, np.float64)
    fun, bc, fun_jac, bc_jac = wrapped
    n, m, k = obj.n, len(x), len(p)
    col, jac = _bvp.prepare_sys(n, m, k, fun, bc, fun_jac, bc_jac, x, np.diff(x))
    cr, ym, ff, fm = col(y, p)
    br = bc(y[:, 0], y[:, -1], p)
    residual = np.r_[cr.ravel(order='F'), br]
    begin = time.monotonic()
    matrix = jac(y, p, ym, ff, fm, br)
    jac_seconds = time.monotonic()-begin
    save_npz(args.outdir/'actual_jacobian.npz', matrix)
    np.save(args.outdir/'actual_residual.npy', residual)
    begin = time.monotonic()
    lu = splu(matrix)
    lu_direction = lu.solve(residual)
    lu_seconds = time.monotonic()-begin
    lu_nnz = int(lu.L.nnz+lu.U.nnz)
    del lu
    begin = time.monotonic()
    factor = BlockQR(matrix, n, m, k)
    qr_factor_seconds = time.monotonic()-begin
    begin = time.monotonic()
    qr_direction = factor.solve(residual)
    qr_solve_seconds = time.monotonic()-begin
    difference = qr_direction-lu_direction
    linear_residual = matrix@qr_direction-residual
    summary['actual'] = dict(source_run=str(args.source_run.resolve()),
        source_run_sha256=digest(args.source_run), snapshot=str(args.snapshot.resolve()),
        snapshot_sha256=digest(args.snapshot), nodes=m, n=n, k=k,
        matrix_nnz=int(matrix.nnz), jac_seconds=jac_seconds,
        superlu_seconds=lu_seconds, superlu_LU_nnz=lu_nnz,
        qr_factor_seconds=qr_factor_seconds, qr_solve_seconds=qr_solve_seconds,
        direction_max=float(np.max(np.abs(qr_direction))),
        direction_relative_difference=float(np.linalg.norm(difference)/max(
            np.linalg.norm(lu_direction), np.finfo(float).tiny)),
        original_residual_max=float(np.max(np.abs(residual))),
        QR_linear_residual_max=float(np.max(np.abs(linear_residual))),
        LU_linear_residual_max=float(np.max(np.abs(matrix@lu_direction-residual))),
        QR_stats=factor.stats,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        actual_matrix_sha256=digest(args.outdir/'actual_jacobian.npz'))
    destination.write_text(json.dumps(summary, indent=2, allow_nan=False)+'\n')
    print(json.dumps(summary['actual'], indent=2), flush=True)


if __name__ == '__main__':
    main()

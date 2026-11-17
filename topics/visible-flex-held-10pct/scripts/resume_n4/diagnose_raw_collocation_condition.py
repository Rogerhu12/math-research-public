#!/usr/bin/env python3
"""Read-only estimate of the original complete finite collocation Jacobian.

One Jacobian and its original sparse LU are assembled at the saved complete
state. A proposed parameter-only coordinate change is compared using the
same LU and exact chain rule. This does not solve or change the BVP.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import inspect
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import _bvp
from scipy.sparse.linalg import LinearOperator, onenormest, splu


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('loader', 'source-topic', 'checkpoint', 'transform', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--modes', type=int, required=True)
    parser.add_argument('--angular', type=int, default=1280)
    args = parser.parse_args()
    sys.path.insert(0, str(args.loader.resolve()))
    from refine_fixed_raw_n4 import build_seed
    started = time.monotonic()
    seed = build_seed(args.source_topic, args.checkpoint, args.modes, args.angular)
    obj, par, x, y = (seed[key] for key in ('obj', 'par', 'x', 'y'))
    transform = np.load(args.transform)
    T, inverse = transform['transform'], transform['inverse']
    if not np.array_equal(par, transform['parameter_anchor']):
        raise ValueError('The proposed coordinate change has another anchor')
    col, jac = _bvp.prepare_sys(obj.n, len(x), obj.M, obj.fun, obj.bc,
                                obj.fun_jac, obj.bc_jac, x, np.diff(x))
    cr, ym, ff, fm = col(y, par)
    bc = obj.bc(y[:, 0], y[:, -1], par)
    residual = np.r_[cr.ravel(order='F'), bc]
    print(json.dumps(dict(event='original_collocation_ready',
                          nodes=len(x), n=obj.n, modes=obj.M,
                          residual_max=float(abs(residual).max()))), flush=True)
    A = jac(y, par, ym, ff, fm, bc)
    factor = splu(A)
    n, M = A.shape[0], obj.M
    print(json.dumps(dict(event='original_jacobian_factored', dimension=n,
                          nnz=A.nnz, seconds=time.monotonic() - started)), flush=True)
    def solve(rhs):
        return factor.solve(rhs)
    def solve_t(rhs):
        return factor.solve(rhs, 'T')
    def transformed_solve(rhs):
        value = solve(rhs)
        value[-M:] = inverse @ value[-M:]
        return value
    def transformed_solve_t(rhs):
        value = np.array(rhs, copy=True)
        value[-M:] = inverse.T @ value[-M:]
        return solve_t(value)
    inv_op = LinearOperator((n, n), matvec=solve, matmat=solve,
                            rmatvec=solve_t, rmatmat=solve_t, dtype=float)
    new_inv_op = LinearOperator((n, n), matvec=transformed_solve,
                                matmat=transformed_solve,
                                rmatvec=transformed_solve_t,
                                rmatmat=transformed_solve_t, dtype=float)
    np.random.seed(20261118)
    inverse_estimate = float(onenormest(inv_op, t=2, itmax=5))
    np.random.seed(20261118)
    new_inverse_estimate = float(onenormest(new_inv_op, t=2, itmax=5))
    colsum = np.asarray(abs(A).sum(axis=0)).ravel()
    new_parameter_block = np.asarray(A[:, -M:] @ T)
    norm = float(colsum.max())
    new_norm = max(float(colsum[:-M].max()),
                   float(abs(new_parameter_block).sum(axis=0).max()))
    step = solve(residual)
    new_step = step.copy()
    new_step[-M:] = inverse @ step[-M:]
    linear_error = A @ step - residual
    result = dict(scope=__doc__, command=sys.argv, source_sha256=sha(__file__),
                  input_checkpoint_sha256=sha(args.checkpoint),
                  transform_sha256=sha(args.transform),
                  driver_sha256=sha(args.loader / 'refine_fixed_raw_n4.py'),
                  scipy_prepare_sys_sha256=hashlib.sha256(inspect.getsource(_bvp.prepare_sys).encode()).hexdigest(),
                  scipy_construct_global_jac_sha256=hashlib.sha256(inspect.getsource(_bvp.construct_global_jac).encode()).hexdigest(),
                  physical_profile=obj.cfg, homotopy=seed['settings']['homotopy'],
                  raw_anchor_modes=seed['core_projection_order'],
                  modes=M, nodes=len(x), state_dimension=obj.n,
                  matrix_dimension=n, matrix_nnz=A.nnz,
                  matrix_one_norm=norm, inverse_one_norm_estimate=inverse_estimate,
                  condition_one_estimate=norm * inverse_estimate,
                  transformed_matrix_one_norm=new_norm,
                  transformed_inverse_one_norm_estimate=new_inverse_estimate,
                  transformed_condition_one_estimate=new_norm * new_inverse_estimate,
                  full_residual_max=float(abs(residual).max()),
                  original_boundary_residual_max=float(abs(bc).max()),
                  full_newton_step_norm=float(np.linalg.norm(step)),
                  state_step_max=float(abs(step[:-M]).max()),
                  original_parameter_step_max=float(abs(step[-M:]).max()),
                  physical_logq_step=float(step[-M]),
                  physical_correction_step_max=float(abs(obj.pscale * step[-M + 1:]).max()),
                  transformed_step_norm=float(np.linalg.norm(new_step)),
                  direct_lu_residual_max=float(abs(linear_error).max()),
                  direct_lu_relative_residual=float(abs(linear_error).max() / max(abs(residual).max(), np.finfo(float).tiny)),
                  parameter_only_change_in_physical_step=float(abs(T @ new_step[-M:] - step[-M:]).max()),
                  seconds=time.monotonic() - started,
                  interpretation='The inverse one-norm is an estimator/lower estimate, not a rigorous upper condition bound. Only the actual saved finite Jacobian is measured. A parameter coordinate change preserves the exact Newton direction, while changing its norm and floating factorization. No BVP trial has been accepted here.')
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()

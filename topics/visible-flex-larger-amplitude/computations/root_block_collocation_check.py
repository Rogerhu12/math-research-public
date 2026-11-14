#!/usr/bin/env python3
"""Check the direct blocks on one actual saved-neck collocation Jacobian.

Use --runner fixed or strong, --check-output PATH, then that runner's normal
arguments. This is a linear-algebra inspection, never a nonlinear solution.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy.integrate._bvp import prepare_sys as sparse_prepare
from scipy.sparse.linalg import splu
from strong_block_qr import BlockQRFactor
from root_block_collocation import prepare_sys, DirectBlockQRFactor

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--runner', choices=('fixed', 'strong'), required=True)
    parser.add_argument('--check-output', type=Path, required=True)
    parser.add_argument('--check-nodes', type=int, default=122)
    options, remaining = parser.parse_known_args()
    file = 'root_c2_polished_refinement.py' if options.runner == 'fixed' else 'strong_neck_bvp.py'
    spec = importlib.util.spec_from_file_location('root_direct_inspected_runner', HERE / file)
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)

    def inspect_solver(fun, bc, x, y, p, **kw):
        input_nodes = len(x)
        if options.check_nodes < 2:
            raise ValueError('At least two inspection nodes are needed')
        if input_nodes > options.check_nodes:
            selected = np.unique(np.linspace(0, input_nodes-1, options.check_nodes, dtype=int))
            x, y = x[selected], y[:, selected]
        n, m = y.shape
        k, h = len(p), np.diff(x)
        start = time.monotonic()
        col, jac = sparse_prepare(n, m, k, fun, bc, kw['fun_jac'], kw['bc_jac'], x, h)
        cr, ym, ff, fm = col(y, p)
        br = bc(y[:, 0], y[:, -1], p)
        rhs = np.r_[cr.ravel(order='F'), br]
        original = jac(y, p, ym, ff, fm, br)
        print(json.dumps(dict(event='original_actual_jacobian', n=n, nodes=m, parameters=k,
                              seconds=time.monotonic()-start)), flush=True)
        _, direct_jac = prepare_sys(n, m, k, fun, bc, kw['fun_jac'], kw['bc_jac'], x, h)
        direct = direct_jac(y, p, ym, ff, fm, br)
        sparse_direct = direct.to_sparse()
        difference = sparse_direct-original
        max_entry_difference = float(np.max(abs(difference.data), initial=0.))
        original_qr = BlockQRFactor(original, n, m, k)
        original_step = original_qr.solve(rhs)
        del original_qr
        gc.collect()
        block_qr = DirectBlockQRFactor(direct, n, m, k)
        direct_step = block_qr.solve(rhs)
        lu_step = splu(original).solve(rhs)
        scale = max(float(np.max(abs(original) @ abs(direct_step)+abs(rhs))), np.finfo(float).tiny)
        backward = float(np.max(abs(original @ direct_step-rhs))/scale)
        vs_qr = float(np.max(abs(direct_step-original_step))/max(1., np.max(abs(original_step))))
        vs_lu = float(np.max(abs(direct_step-lu_step))/max(1., np.max(abs(lu_step))))
        result = dict(scope=__doc__, runner=options.runner, inspection_only=True,
            nonlinear_solution=False, n=n, nodes=m, parameters=k,
            input_nodes=input_nodes, inspection_node_subset_only=m != input_nodes,
            original_nnz=int(original.nnz), exact_sparse_entries_equal=max_entry_difference == 0.,
            maximum_jacobian_entry_difference=max_entry_difference,
            qr_steps_bitwise_equal=bool(np.array_equal(direct_step, original_step)),
            direct_vs_original_qr_relative_difference=vs_qr,
            direct_vs_sparse_lu_relative_difference=vs_lu,
            relative_backward_error=backward,
            direct_matvec_relative_error=float(np.max(abs(direct.matvec(direct_step)-original@direct_step))/scale),
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            seconds=time.monotonic()-start,
            source_sha256={name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                           for name in ('root_block_collocation.py', 'root_block_collocation_check.py',
                                        'strong_block_qr.py', file)})
        options.check_output.write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps(result), flush=True)
        if not (backward < 1e-10 and vs_qr < 1e-8 and vs_lu < 1e-6):
            raise RuntimeError('Actual direct-block comparison outside required tolerance')
        raise SystemExit(0)

    if options.runner == 'strong':
        old = runner.module
        def module(name, path):
            value = old(name, path)
            if Path(path).name == 'root_dual_core_bvp.py':
                value.solve_bvp = inspect_solver
            return value
        runner.module = module
    else:
        old = runner.load
        def load(name, path):
            value = old(name, path)
            if Path(path).name == 'root_dual_core_bvp.py':
                value.solve_bvp = inspect_solver
            return value
        runner.load = load
    sys.argv = [sys.argv[0]] + remaining
    runner.main()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Run the existing prefix driver with recoverable Jacobian-input snapshots.

Every snapshot is only an initializer, never an accepted BVP solution. The
original collocation/Newton functions, arithmetic, domains and gates execute
unchanged. Logging before/after Jacobian and sparse LU records the location
and observed peak RSS if an execution environment kills a later operation.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import sys
import time

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
import scipy.integrate._bvp as bvp
import scipy.sparse.linalg as sparse_linalg


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--observer-dir', type=Path, required=True)
    parser.add_argument('--driver', type=Path, required=True)
    parser.add_argument('driver_args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    rest = args.driver_args
    if rest and rest[0] == '--':
        rest = rest[1:]
    output = args.observer_dir.resolve()
    output.mkdir(parents=True, exist_ok=False)
    solve_output = Path(rest[rest.index('--outdir')+1]).resolve()
    begin = time.monotonic()
    calls = 0

    def event(kind, **fields):
        row = dict(kind=kind, seconds=time.monotonic()-begin,
                   maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                   **fields)
        with (output/'resources.jsonl').open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False)+'\n')

    old_prepare = bvp.prepare_sys
    def prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
        col, jac = old_prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h)
        def observed(y, p, *extra):
            nonlocal calls
            calls += 1
            run = json.loads((solve_output/'run.json').read_text())
            temp = output/'last-jac-input.tmp.npz'
            np.savez_compressed(temp, x=x, y=y, p=p,
                                pscale=np.array(run['parameter_scales']))
            temp.replace(output/'last-jac-input.npz')
            event('jacobian_start', calls=calls, nodes=m, dimension=n, parameters=k)
            result = jac(y, p, *extra)
            event('jacobian_return', calls=calls, nodes=m, nnz=result.nnz)
            return result
        return col, observed
    bvp.prepare_sys = prepare
    old_lu = sparse_linalg.splu
    def lu(matrix, *a, **kw):
        event('sparse_lu_start', shape=list(matrix.shape), nnz=matrix.nnz)
        result = old_lu(matrix, *a, **kw)
        event('sparse_lu_return', L_nnz=result.L.nnz, U_nnz=result.U.nnz)
        return result
    sparse_linalg.splu = lu
    metadata = dict(scope=__doc__, command=sys.argv,
                    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    original_driver_sha256=hashlib.sha256(args.driver.read_bytes()).hexdigest(),
                    snapshot_status='unaccepted original Jacobian input; initializer only')
    (output/'observer.json').write_text(json.dumps(metadata, indent=2)+'\n')
    spec = importlib.util.spec_from_file_location('observed_original_prefix', args.driver)
    driver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(driver)
    sys.argv = [str(args.driver), *rest]
    event('driver_start')
    try:
        driver.main()
    finally:
        event('driver_return_or_exception')


if __name__ == '__main__':
    main()

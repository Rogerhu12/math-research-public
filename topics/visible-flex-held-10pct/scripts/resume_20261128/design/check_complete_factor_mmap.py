#!/usr/bin/env python3
"""One actual saved M16 complete-J check of factor-only scratch backing.

No new Jacobian or BVP is computed. The unchanged full QR and the mapped
factor solve receive the exact same saved complete matrix and residual.
Directions, every backward-error denominator, original-J residual arrays,
matrix norm, and every original factor/solve statistic must agree bitwise.
Automatic cyclic GC is disabled for the final factor/backing lifetime check.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '2'
import argparse
import gc
import hashlib
import inspect
import json
from pathlib import Path
import resource
import sys
import time
import weakref

import numpy as np
from scipy.sparse import load_npz

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import complete_factor_mmap as mapped
from complete_factor_mmap import BlockQR, MappedBlockQR


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def bits(a, b):
    return a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes()


def csr_hashes(matrix):
    return {name:hashlib.sha256(memoryview(getattr(matrix, name)).cast('B')).hexdigest()
            for name in ('data', 'indices', 'indptr')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prior-check', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    source = json.loads(args.prior_check.read_text())['actual']
    matrix_path = args.prior_check.parent/'actual_jacobian.npz'
    rhs_path = args.prior_check.parent/'actual_residual.npy'
    if sha(matrix_path) != source['actual_matrix_sha256']:
        raise ValueError('The saved original full M16 matrix changed')
    n, m, k = source['n'], source['nodes'], source['k']
    if (n, m, k) != (49, 879, 16):
        raise ValueError('This execution is bound to the actual saved M16 check')
    rhs = np.load(rhs_path, allow_pickle=False)
    if rhs.shape != (n*m+k,):
        raise ValueError('The saved complete original residual has changed shape')
    original = BlockQR(load_npz(matrix_path).tocsr(), n, m, k)
    direction = original.solve(rhs)
    denominator = original._absolute_matvec(np.abs(direction))+np.abs(rhs)
    residual = original.matrix@direction-rhs
    reference = dict(stats=dict(original.stats), matrix_inf=original.matrix_inf,
                     CSR_hashes=csr_hashes(original.matrix))
    del original
    mapped.collect_and_trim()
    before = mapped.memory()
    current = MappedBlockQR(load_npz(matrix_path).tocsr(), n, m, k,
        storage_directory=args.outdir/'temporary-factors', map_scope='factor-only')
    actual_direction = current.solve(rhs)
    actual_denominator = current._absolute_matvec(np.abs(actual_direction))+np.abs(rhs)
    actual_residual = current.matrix@actual_direction-rhs
    comparison = dict(complete_direction_bitwise=bits(direction, actual_direction),
        all_backward_denominators_bitwise=bits(denominator, actual_denominator),
        complete_original_matrix_residual_bitwise=bits(residual, actual_residual),
        full_CSR_data_indices_indptr_hashes_equal=reference['CSR_hashes'] == csr_hashes(current.matrix),
        matrix_inf_identical=reference['matrix_inf'] == current.matrix_inf,
        all_original_factor_and_solve_statistics_identical=reference['stats'] == current.stats,
        original_apply_implementation_retained=MappedBlockQR._apply is BlockQR._apply,
        original_triangular_solve_implementation_retained=MappedBlockQR._solve is BlockQR._solve,
        all_mapped_factor_arrays_readonly=all(not mapped._get(current, path).flags.writeable
            for path in mapped._paths(current, 'factor-only')))
    if not all(comparison.values()):
        raise AssertionError(comparison)
    current._complete_store.discard_after_solve()
    storage = json.loads(json.dumps(current._complete_store.stats))
    actual_stats = dict(current.stats)
    folder = current._complete_store.directory
    backing_file = current._complete_store.path
    factor_ref = weakref.ref(current)
    backing_ref = weakref.ref(current._complete_store._backing)
    automatic_gc = gc.isenabled()
    gc.disable()
    try:
        del current
        lifetime = dict(automatic_cyclic_GC_disabled=True,
            factor_weakref_immediately_released=factor_ref() is None,
            backing_weakref_immediately_released=backing_ref() is None,
            backing_file_immediately_unlinked=not backing_file.exists(),
            unique_factor_directory_immediately_removed=not folder.exists())
        if not all(lifetime.values()):
            raise AssertionError(lifetime)
    finally:
        if automatic_gc:
            gc.enable()
    report = dict(scope=__doc__, status='actual_complete_M16_factor_only_mmap_check_passed',
        map_scope='factor-only', untested_full_CSR_mapping_not_claimed=True,
        actual_prior_check=str(args.prior_check.resolve()), prior_check_sha256=sha(args.prior_check),
        original_matrix=str(matrix_path.resolve()), original_matrix_sha256=sha(matrix_path),
        original_residual=str(rhs_path.resolve()), original_residual_sha256=sha(rhs_path),
        source_dimensions=dict(n=n, nodes=m, parameters=k, equations=n*m+k),
        comparison=comparison, original_QR_statistics=reference['stats'],
        mapped_QR_statistics=actual_stats,
        original_absolute_J_direction_residual_max=float(np.max(np.abs(residual))),
        mapped_absolute_J_direction_residual_max=float(np.max(np.abs(actual_residual))),
        storage=storage, lifetime=lifetime,
        actual_before_new_factor=before,
        conservative_backing_upper_bound=mapped.backing_upper_bound(n,m,k,'factor-only'),
        inherited_original_function_sha256={name:hashlib.sha256(inspect.getsource(
            getattr(BlockQR, name)).encode()).hexdigest() for name in ('_apply', '_solve', 'solve')},
        source_hashes={str(path.resolve()):sha(path) for path in
            (Path(__file__), Path(mapped.__file__), HERE.parent/'block_qr_v2.py')},
        full_J_reassembled=False, BVP_steps_applied=0, accepted_field_produced=False,
        original_gates_relaxed=False, construction_peak_reduction_claimed=False,
        maximum_process_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        seconds=time.monotonic()-started)
    (args.outdir/'comparison.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key:report[key] for key in ('status','comparison','lifetime',
        'original_absolute_J_direction_residual_max','mapped_absolute_J_direction_residual_max',
        'maximum_process_RSS_KiB','seconds','storage')}, indent=2), flush=True)


if __name__ == '__main__':
    main()

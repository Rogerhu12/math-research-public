#!/usr/bin/env python3
"""One saved actual M16 full-J check of CSR mapping before original QR.

This checks a new storage layout, not a new mathematical input. No Jacobian is
assembled and no BVP step is applied. Complete directions, all backward-error
denominators, residual arrays, matrix bytes and original QR statistics must
match bitwise. Mapping lifetime is checked with automatic cyclic GC disabled.
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
import complete_factor_mmap as factors
import complete_csr_prefactor_mmap as mapped
from complete_csr_prefactor_mmap import BlockQR, BeforeQRMappedBlockQR


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def bits(a, b):
    return a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes()


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
        raise ValueError('The saved original complete M16 matrix changed')
    n, m, k = source['n'], source['nodes'], source['k']
    if (n, m, k) != (49, 879, 16):
        raise ValueError('This execution is bound to the actual saved M16 matrix')
    rhs = np.load(rhs_path, allow_pickle=False)
    if rhs.shape != (n*m+k,):
        raise ValueError('The saved complete original residual changed shape')
    original_input = load_npz(matrix_path).tocsr()
    initial_hashes = mapped._hash_arrays(original_input)
    initial_nnz = original_input.nnz
    original = BlockQR(original_input, n, m, k)
    direction = original.solve(rhs)
    denominator = original._absolute_matvec(np.abs(direction))+np.abs(rhs)
    residual = original.matrix@direction-rhs
    reference = dict(stats=dict(original.stats), matrix_inf=original.matrix_inf,
                     CSR_hashes=mapped._hash_arrays(original.matrix), nnz=original.matrix.nnz)
    del original, original_input
    factors.collect_and_trim()
    new_input = load_npz(matrix_path).tocsr()
    before = mapped.process_memory()
    current = BeforeQRMappedBlockQR(new_input, n, m, k,
        storage_directory=args.outdir/'temporary-complete-stores')
    actual_direction = current.solve(rhs)
    actual_denominator = current._absolute_matvec(np.abs(actual_direction))+np.abs(rhs)
    actual_residual = current.matrix@actual_direction-rhs
    comparison = dict(complete_direction_bitwise=bits(direction, actual_direction),
        all_backward_denominators_bitwise=bits(denominator, actual_denominator),
        complete_original_matrix_residual_bitwise=bits(residual, actual_residual),
        every_initial_stored_CSR_byte_hash_equal=(initial_hashes ==
            current._complete_csr_store.stats['initial_CSR_hashes']),
        post_original_zero_compaction_CSR_hashes_equal=(reference['CSR_hashes'] ==
            mapped._hash_arrays(current.matrix)),
        original_zero_compaction_nnz_equal=reference['nnz'] == current.matrix.nnz,
        original_zero_compaction_executed_once=(
            current._complete_csr_store.stats['original_zero_compactions'] == 1),
        complete_original_CSR_object_retained=current.matrix is new_input,
        original_instance_prune_restored='prune' not in new_input.__dict__,
        all_complete_CSR_arrays_share_mapping=all(np.shares_memory(getattr(new_input, name),
            current._complete_csr_store._backing) for name in ('data','indices','indptr')),
        all_complete_CSR_arrays_readonly=all(not getattr(new_input, name).flags.writeable
            for name in ('data','indices','indptr')),
        matrix_inf_identical=reference['matrix_inf'] == current.matrix_inf,
        all_original_factor_and_solve_statistics_identical=reference['stats'] == current.stats,
        original_apply_implementation_retained=BeforeQRMappedBlockQR._apply is BlockQR._apply,
        original_triangular_solve_implementation_retained=BeforeQRMappedBlockQR._solve is BlockQR._solve,
        all_mapped_factor_arrays_readonly=all(not factors._get(current, path).flags.writeable
            for path in factors._paths(current, 'factor-only')))
    if not all(comparison.values()):
        raise AssertionError(comparison)
    current._complete_csr_store.discard_after_solve()
    current._complete_store.discard_after_solve()
    csr_storage = json.loads(json.dumps(current._complete_csr_store.stats))
    factor_storage = json.loads(json.dumps(current._complete_store.stats))
    actual_stats = dict(current.stats)
    folders = [current._complete_csr_store.directory, current._complete_store.directory]
    files = [current._complete_csr_store.path, current._complete_store.path]
    factor_ref = weakref.ref(current)
    csr_backing_ref = weakref.ref(current._complete_csr_store._backing)
    factor_backing_ref = weakref.ref(current._complete_store._backing)
    del new_input
    automatic_gc = gc.isenabled()
    gc.disable()
    try:
        del current
        lifetime = dict(automatic_cyclic_GC_disabled=True,
            factor_weakref_immediately_released=factor_ref() is None,
            CSR_backing_weakref_immediately_released=csr_backing_ref() is None,
            QR_backing_weakref_immediately_released=factor_backing_ref() is None,
            both_backing_files_immediately_unlinked=all(not path.exists() for path in files),
            both_unique_store_directories_immediately_removed=all(not path.exists() for path in folders))
        if not all(lifetime.values()):
            raise AssertionError(lifetime)
    finally:
        if automatic_gc:
            gc.enable()
    report = dict(scope=__doc__, status='actual_complete_M16_CSR_before_QR_mapping_check_passed',
        actual_prior_check=str(args.prior_check.resolve()), prior_check_sha256=sha(args.prior_check),
        original_matrix=str(matrix_path.resolve()), original_matrix_sha256=sha(matrix_path),
        original_residual=str(rhs_path.resolve()), original_residual_sha256=sha(rhs_path),
        source_dimensions=dict(n=n, nodes=m, parameters=k, equations=n*m+k),
        original_stored_CSR_nnz_before_zero_compaction=initial_nnz,
        original_CSR_nnz_after_original_zero_compaction=reference['nnz'],
        comparison=comparison, original_QR_statistics=reference['stats'],
        mapped_QR_statistics=actual_stats, initial_CSR_hashes=initial_hashes,
        original_absolute_J_direction_residual_max=float(np.max(np.abs(residual))),
        mapped_absolute_J_direction_residual_max=float(np.max(np.abs(actual_residual))),
        CSR_storage=csr_storage, factor_storage=factor_storage, lifetime=lifetime,
        actual_before_new_factor=before,
        conservative_complete_backing_upper_bound=mapped.full_backing_upper_bound(n,m,k),
        inherited_original_function_sha256={name:hashlib.sha256(inspect.getsource(
            getattr(BlockQR, name)).encode()).hexdigest() for name in ('_apply', '_solve', 'solve')},
        source_hashes={str(path.resolve()):sha(path) for path in
            (Path(__file__), Path(mapped.__file__), Path(factors.__file__), HERE.parent/'block_qr_v2.py')},
        full_J_reassembled=False, BVP_steps_applied=0, accepted_field_produced=False,
        original_gates_relaxed=False, actual_M48_RAM_saving_claimed=False,
        original_CSR_assembly_peak_still_required=True,
        maximum_process_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        seconds=time.monotonic()-started)
    (args.outdir/'comparison.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key:report[key] for key in ('status','comparison','lifetime',
        'original_absolute_J_direction_residual_max','maximum_process_RSS_KiB','seconds')}, indent=2), flush=True)


if __name__ == '__main__':
    main()

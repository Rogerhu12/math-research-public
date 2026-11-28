#!/usr/bin/env python3
"""Compare streaming diagnostics on a saved complete actual collocation J."""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import argparse
import gc
import hashlib
import inspect
import json
from pathlib import Path
import resource
import time
import numpy as np
from scipy.sparse import load_npz
from block_qr import BlockQR as Old
from block_qr_v2 import BlockQR as New


def ref(path):
    p = Path(path).resolve()
    with p.open('rb') as stream:
        return dict(path=str(p), sha256=hashlib.file_digest(stream, 'sha256').hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--actual-directory', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    a = parser.parse_args()
    if a.out.exists():
        raise FileExistsError(a.out)
    b = a.actual_directory
    matrix_path, rhs_path = b/'actual_jacobian.npz', b/'actual_residual.npy'
    # Bind the already saved actual M16 system, not a random/synthetic matrix.
    if ref(matrix_path)['sha256'] != 'a9d655651b6170f1eb8097fe61606dc7a89b40fd181b042ef8e1af305fad4bef':
        raise ValueError('Unexpected actual saved M16 matrix')
    if ref(rhs_path)['sha256'] != '5adf39dd101f6adcd8ec57e7a89337bd6ce034e124fca887a2c3cfd22fafe423':
        raise ValueError('Unexpected actual saved M16 right hand side')
    started = time.monotonic()
    matrix = load_npz(matrix_path)
    rhs = np.load(rhs_path)
    same_core = all(inspect.getsource(getattr(Old,k)) == inspect.getsource(getattr(New,k))
                    for k in ('_apply','_solve'))
    if not same_core:
        raise ValueError('The QR solve core was changed')
    old = Old(matrix, 49, 879, 16)
    answer_old = old.solve(rhs)
    old_stats = dict(old.stats)
    old_inf = old.matrix_inf
    old_denominator = old.matrix_abs @ np.abs(answer_old) + np.abs(rhs)
    storage = sum(value.nbytes for value in
                  (old.matrix_abs.data, old.matrix_abs.indices, old.matrix_abs.indptr))
    del old
    gc.collect()
    new = New(matrix, 49, 879, 16)
    answer_new = new.solve(rhs)
    new_denominator = new._absolute_matvec(np.abs(answer_new)) + np.abs(rhs)
    checks = dict(core_methods_source_identical=same_core,
                  complete_direction_bitwise_identical=np.array_equal(answer_old, answer_new),
                  complete_backward_denominator_bitwise_identical=np.array_equal(old_denominator, new_denominator),
                  original_matrix_infinity_norm_bitwise_identical=old_inf == new.matrix_inf,
                  all_original_factor_and_solve_stats_identical=old_stats == new.stats,
                  no_full_absolute_matrix_retained=not hasattr(new, 'matrix_abs'))
    if not all(checks.values()):
        raise AssertionError(checks)
    out = dict(scope=__doc__, status='all_actual_complete_M16_checks_passed',
               source=ref(__file__),
               old_source=ref(inspect.getfile(Old)), new_source=ref(inspect.getfile(New)),
               wrapper_source=ref(Path(__file__).with_name('prefix_block_qr_driver_v3.py')),
               actual_matrix=ref(matrix_path), actual_residual=ref(rhs_path),
               actual_source_summary=ref(b/'summary.json'),
               shape=list(matrix.shape), n=49, nodes=879, k=16,
               all_original_entries_in_factor_retained=True, checks=checks,
               removed_persistent_absolute_matrix_bytes=int(storage),
               diagnostic_block_rows=new.diagnostic_rows,
               actual_original_matrix_residual_max=float(np.max(np.abs(rhs-matrix@answer_new))),
               original_stats=old_stats, new_stats=dict(new.stats),
               wall_seconds=time.monotonic()-started,
               maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               peak_scope='both original and new comparisons in one process; not a production peak bound',
               nonlinear_problem_or_gates_changed=False, new_BVP_invoked=False,
               complete_surface=False)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=ref(a.out), checks=checks,
                          removed_persistent_bytes=int(storage), seconds=out['wall_seconds'],
                          peak_kib=out['maximum_rss_kib']), indent=2))


if __name__ == '__main__':
    main()

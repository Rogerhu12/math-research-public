#!/usr/bin/env python3
"""Check lossless whole-field chunks and streaming LP against a full matrix.

The data fixture reuses the completed coarse baseline as bytes only.  It
does not compute any new physical field, solve a BVP, or run a tail worker.
"""
from __future__ import annotations
import argparse
import gzip
import json
import os
from pathlib import Path
import tempfile
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from scipy.optimize import linprog
from root_geometry_array_io import write_chunks, read_chunks, sha
from root_geometry_streaming_lp import solve_all_rows, GROUPS


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh fixture output')
    with gzip.open(args.field, 'rb') as stream:
        actual = np.load(stream, allow_pickle=False)
    data = np.concatenate([actual, actual], axis=0)
    with tempfile.TemporaryDirectory(prefix='owned-geometry-storage-check-') as temporary:
        target = Path(temporary)/'complete.json'
        record = write_chunks(target, data)
        recovered = read_chunks(target)
        if not np.array_equal(data, recovered) or len(record['chunks']) < 2:
            raise AssertionError('Complete multi-chunk reconstruction differs')
        destination = np.memmap(Path(temporary)/'mapped.bin', dtype='float64', mode='w+', shape=data.shape)
        read_chunks(target, destination)
        if not np.array_equal(data, destination):
            raise AssertionError('Direct disk destination differs')
        original = target.read_text()
        bad = json.loads(original); bad['chunks'][1]['start'] += 1
        target.write_text(json.dumps(bad))
        omitted_row_rejected = False
        try:
            read_chunks(target)
        except ValueError:
            omitted_row_rejected = True
        target.write_text(original)
        part = target.with_name(record['chunks'][0]['file'])
        part.write_bytes(part.read_bytes()+b'changed')
        changed_chunk_rejected = False
        try:
            read_chunks(target)
        except ValueError:
            changed_chunk_rejected = True
        if not omitted_row_rejected or not changed_chunk_rejected:
            raise AssertionError('An incomplete or changed field was not rejected')
        chunk_sizes = [item['bytes'] for item in record['chunks']]
        del destination
    del data, recovered, actual
    rng = np.random.default_rng(168521)
    count = 2200
    base = np.column_stack([rng.uniform(-8.28, -7.9, count),
                            rng.uniform(7.9, 8.28, count), rng.uniform(3.85, 3.99, count)])
    changes = rng.normal(0, .20, (count, 3, 5))
    diameter = 4.
    curvature_budget = 1/.03
    limits = [curvature_budget/diameter]*4+[diameter]
    A = np.vstack([sign*changes[:, component, :] for component, sign in GROUPS])
    B = np.hstack([limit-sign*base[:, component]
                   for (component, sign), limit in zip(GROUPS, limits)])
    dense = linprog([-1., 0., 0., 0., 0.], A_ub=A, b_ub=B,
                    bounds=[(0., 1.)]+[(-1., 1.)]*4, method='highs',
                    options=dict(primal_feasibility_tolerance=1e-9,
                                 dual_feasibility_tolerance=1e-9))
    streamed = solve_all_rows(base, changes, diameter, curvature_budget, batch=137)
    if not dense.success or not streamed['success']:
        raise AssertionError('The comparison fixture should be feasible')
    value = np.asarray(streamed['normalized_steps'])
    gap = abs(-value[0]-dense.fun)
    violation = float(np.max(A@value-B))
    if gap > 1e-9 or violation > 1e-9 or not streamed['all_finite_rows_checked']:
        raise AssertionError('The full finite LP comparison failed')
    impossible = solve_all_rows(base, np.zeros_like(changes), 3., curvature_budget, batch=137)
    if impossible['success'] or impossible.get('status') != 2:
        raise AssertionError('An infeasible full-row case was not reported')
    sources = {str(Path(__file__).with_name(name)): sha(Path(__file__).with_name(name))
        for name in ('root_geometry_array_io.py', 'root_geometry_streaming_lp.py',
                     'root_geometry_streaming_check.py')}
    args.out.write_text(json.dumps(dict(scope=__doc__, source_sha256=sources,
        original_field=str(args.field), original_field_sha256=sha(args.field),
        complete_field_bitwise_equal=True, direct_mapped_destination_equal=True,
        chunk_bytes=chunk_sizes, omitted_row_rejected=omitted_row_rejected,
        changed_chunk_rejected=changed_chunk_rejected, full_lp_rows=len(B),
        objective_gap_to_full_matrix=float(gap), max_full_row_violation=violation,
        history=streamed['history'], infeasible_case_status=impossible['status'],
        all_checks_passed=True, actual_geometry_executed=False),indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out), all_checks_passed=True)))


if __name__ == '__main__':
    main()

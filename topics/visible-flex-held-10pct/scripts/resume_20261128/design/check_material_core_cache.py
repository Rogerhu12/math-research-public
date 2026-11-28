#!/usr/bin/env python3
"""Compare the original R53 evaluator memo on an actual complete state block.

Every state and parameter column is retained at the selected genuine saved
nodes.  --points 0 selects the entire saved grid.  No BVP iteration, accepted
field or new collocation matrix is produced.  A final isolated-write check
verifies that mutating a returned array or original output-cache array cannot
change the next evaluation.  Actual arrays remain outside Git.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gc
import hashlib
import inspect
import json
from pathlib import Path
import resource
import shutil
import sys
import time

import numpy as np

from check_fourier_table_cache import load, sha
import cached_fourier_tables as fourier_cache
import material_core_evaluate_cache as core_cache


def array_sha(value):
    value = np.ascontiguousarray(value)
    digest = hashlib.sha256()
    digest.update(value.dtype.str.encode())
    digest.update(repr(value.shape).encode())
    digest.update(memoryview(value).cast('B'))
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-run', 'snapshot', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--points', type=int, default=32)
    parser.add_argument('--rhs-block', type=int, default=16)
    args = parser.parse_args()
    if args.points < 0 or args.rhs_block < 1:
        raise ValueError('Nonnegative points and a positive block are required')
    out = args.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    snapshot = out/'actual-snapshot.npz'
    shutil.copyfile(args.snapshot, snapshot)
    source_copy = out/'source-run-captured.json'
    source_copy.write_bytes(args.source_run.read_bytes())
    source = json.loads(source_copy.read_text())
    command = list(source['command'][2:])
    scripts = Path(__file__).resolve().parents[2]
    portable = scripts/'resume_m3/portable_prefix_continue.py'
    original = load('_material_cache_original_portable', portable)
    captured = {}

    def capture(obj, x, y, p):
        captured.update(obj=obj, x=x, y=y, p=p)

    before = inspect.getsource(original.main)
    marker = '        rhs = o.fun(x,y,par)'
    if before.count(marker) != 1:
        raise ValueError('The original initial-domain capture location changed')
    after = before.replace(marker, '        _memo_capture(o,x,y,par)\n        return')
    original.__dict__['_memo_capture'] = capture
    exec(compile(after, str(portable)+'::capture_without_solver', 'exec'), original.__dict__)
    command[command.index('--outdir')+1] = str(out/'problem-construction')
    for flag in ('--raw-restart', '--restart-checkpoint'):
        if flag in command:
            index = command.index(flag)
            del command[index:index+2]
    command.extend(['--raw-restart', str(snapshot)])
    sys.argv = [str(portable), *command]
    original.main()
    obj, full_x, full_y, p = (captured[name] for name in ('obj', 'x', 'y', 'p'))
    if args.points == 0:
        indices = np.arange(len(full_x))
    else:
        indices = np.unique(np.linspace(0, len(full_x)-1,
            min(args.points, len(full_x)), dtype=int))
    x, y = full_x[indices].copy(), full_y[:, indices].copy()
    batches = load('_material_cache_original_batches',
                   scripts/'resume_20261126/streamed_release_prefix_driver.py')
    table_stats = fourier_cache.install(sys.modules['portable_m3_fourier_jac'])
    # Warm the unchanged geometry-independent tables before either timed phase.
    sys.modules['portable_m3_fourier_jac'].build_tables(obj.flow(p[0]))
    cls = type(obj._core)
    if cls.__name__ != 'MaterialFlattenedSupportCore':
        raise ValueError('The actual input is not an original positive-lambda R53 core')
    memo_stats = core_cache.install(cls)
    times = {}

    def evaluate(label, enabled, reset):
        memo_stats['enabled'] = enabled
        if reset:
            for attribute in ('_flow', '_flow_key', '_core', '_core_key', '_initial',
                              '_initial_jac', '_adaptive_core_jac_key',
                              '_adaptive_core_jac_fields', '_lift_inlet_key'):
                setattr(obj, attribute, None)
            if hasattr(obj, 'unlifted_projection'):
                del obj.unlifted_projection
            gc.collect()
        begin = time.monotonic()
        rhs = batches.split_rhs(obj.fun, args.rhs_block)(x, y, p)
        dy, dp = batches.split_jac(obj.fun_jac, args.rhs_block)(x, y, p)
        times[label] = time.monotonic()-begin
        print(json.dumps(dict(phase=label, seconds=times[label],
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
        return rhs, dy, dp

    baseline = evaluate('original_core_evaluate', False, True)
    cached = evaluate('memo_cold', True, True)
    warm = evaluate('memo_warm', True, False)

    def difference(left, right):
        return {name: dict(bitwise_equal=bool(a.dtype == b.dtype and a.shape == b.shape
                                and a.tobytes() == b.tobytes()),
                          max_absolute_difference=float(np.max(np.abs(a-b))),
                          original_array_sha256=array_sha(a),
                          cached_array_sha256=array_sha(b))
                for name, a, b in zip(('rhs', 'dy', 'dp'), left, right)}

    core = obj._core
    theta = obj.flow(p[0]).angular(obj.nt)[1]
    value = core.evaluate(theta)
    expected = {name: item.copy() if isinstance(item, np.ndarray) else item
                for name, item in value.items()}
    expected_jets = tuple(item.copy() for item in core._cache_jets)
    value['F'].flat[0] += 1.
    core._cache_jets[0].flat[0] += 1.
    core._cache_theta.flat[0] += 1.
    again = core.evaluate(theta)
    restored = dict(
        returned_value_after_isolated_write=all(np.array_equal(expected[name], item)
            if isinstance(item, np.ndarray) else expected[name] == item
            for name, item in again.items()),
        original_jets_after_isolated_write=all(np.array_equal(a, b)
            for a, b in zip(expected_jets, core._cache_jets)),
        original_theta_after_isolated_write=np.array_equal(theta, core._cache_theta),
        returned_arrays_writable=all(item.flags.writeable for item in again.values()
                                     if isinstance(item, np.ndarray)))
    result = dict(scope=__doc__, source_run=str(args.source_run.resolve()),
        source_run_sha256=sha(source_copy), actual_snapshot=str(args.snapshot.resolve()),
        snapshot_sha256=sha(snapshot), original_nodes=len(full_x), evaluated_nodes=len(x),
        node_selection='all actual saved nodes' if args.points == 0 else
            'unique linspace integer indices across the actual saved grid',
        node_indices_sha256=array_sha(indices), dimension=obj.n, parameters=len(p),
        modes=obj.M, radial_block=args.rhs_block,
        complete_rows_and_parameter_columns_evaluated=True,
        original_vs_memo_cold=difference(baseline, cached),
        original_vs_memo_warm=difference(baseline, warm),
        isolated_write_check=restored, times_seconds=times,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        actual_memo_stats=memo_stats, actual_fourier_cache_stats=table_stats,
        source_hashes={str(file): sha(file) for file in
            (Path(__file__).resolve(), Path(core_cache.__file__).resolve(),
             Path(fourier_cache.__file__).resolve(), portable)},
        BVP_solver_invoked=False, global_collocation_matrix_assembled=False,
        accepted_field=False, original_acceptance_gates_changed=False)
    (out/'summary.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    if (not all(value['bitwise_equal'] for group in
            ('original_vs_memo_cold', 'original_vs_memo_warm')
            for value in result[group].values()) or not all(restored.values())
            or not memo_stats['hits'] or memo_stats['bypasses']):
        raise AssertionError('The actual core memo comparison or write isolation failed')
    print(json.dumps(dict(status='actual_state_block_bitwise_equal',
        evaluated_nodes=len(x), original_nodes=len(full_x), modes=obj.M,
        times_seconds=times, isolated_write_check=restored)), flush=True)


if __name__ == '__main__':
    main()

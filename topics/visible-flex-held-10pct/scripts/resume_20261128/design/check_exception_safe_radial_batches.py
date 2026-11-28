#!/usr/bin/env python3
"""Check one actual small original block and unreachable-Flow lifecycle.

Uses the saved true M16 original J input, without constructing its full J or
applying a Newton step.  Both batch paths must return bitwise identical RHS,
state columns, and all parameter columns.  An explicitly perturbed unaccepted
field then exercises the original Frenet exception; it is a resource probe,
not an actual solver event or a new mathematical failure.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '2'
import argparse
import gc
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import resource
import sys
import time
import weakref

import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path.insert(0, str(HERE))
import exception_safe_radial_batches as lifecycle
import cached_fourier_tables as fourier
import material_core_evaluate_cache as memo
import analytic_delta_jac_adapter as delta


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def same_bits(a, b):
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prior-check', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    binding = json.loads(args.prior_check.read_text())['actual']
    source_path, snapshot = Path(binding['source_run']), Path(binding['snapshot'])
    if sha(source_path) != binding['source_run_sha256'] or sha(snapshot) != binding['snapshot_sha256']:
        raise ValueError('The actual original small-block source changed')
    source = json.loads(source_path.read_text())
    for group in ('source_hashes', 'inputs'):
        for filename, expected in source[group].items():
            if sha(filename) != expected:
                raise ValueError('The original problem definition changed: '+filename)
    portable = SCRIPTS/'resume_m3/portable_prefix_continue.py'
    driver = load('_lifecycle_original_portable', portable)
    captured = {}

    def capture(obj, x, y, p):
        captured.update(obj=obj, x=x, y=y, p=p)

    before = inspect.getsource(driver.main)
    marker = '        rhs = o.fun(x,y,par)'
    if before.count(marker) != 1:
        raise ValueError('The original no-solve capture location changed')
    driver.__dict__['_lifecycle_capture'] = capture
    exec(compile(before.replace(marker, '        _lifecycle_capture(o,x,y,par)\n        return'),
                 str(portable)+'::lifecycle_capture_no_solver', 'exec'), driver.__dict__)
    command = list(source['command'][2:])
    command[command.index('--outdir')+1] = str(args.outdir/'problem-construction')
    for flag in ('--raw-restart', '--restart-checkpoint'):
        if flag in command:
            i = command.index(flag)
            del command[i:i+2]
    command += ['--raw-restart', str(snapshot)]
    sys.argv = [str(portable), *command]
    driver.main()
    obj = captured['obj']
    with np.load(snapshot, allow_pickle=False) as raw:
        x, y, p = (raw[key].copy() for key in ('x', 'y', 'p'))
    if (obj.n, len(x), len(p)) != (binding['n'], binding['nodes'], binding['k']):
        raise ValueError('The actual full source dimensions differ')
    obj.initial(p)
    fourier_stats = fourier.install(sys.modules['portable_m3_fourier_jac'])
    memo_stats = memo.install(type(obj._core))
    delta_stats = delta.install(type(obj))
    previous = load('_lifecycle_previous_batching', SCRIPTS/'resume_20261126/streamed_release_prefix_driver.py')
    indices = np.unique(np.linspace(0, len(x)-1, 7, dtype=int))
    t, Y = x[indices], y[:, indices]
    stats, events, comparisons = lifecycle.statistics(), [], []
    for block in (8, 4):
        old_rhs = previous.split_rhs(obj.fun, block)(t, Y, p)
        new_rhs = lifecycle.split_rhs(obj.fun, block, stats, events.append)(t, Y, p)
        old_dy, old_dp = previous.split_jac(obj.fun_jac, block)(t, Y, p)
        new_dy, new_dp = lifecycle.split_jac(obj.fun_jac, block, stats, events.append)(t, Y, p)
        row = dict(radial_block=block, sampled_nodes=len(t),
            RHS_bitwise=same_bits(old_rhs, new_rhs),
            complete_state_columns_bitwise=same_bits(old_dy, new_dy),
            complete_parameter_columns_bitwise=same_bits(old_dp, new_dp))
        if not all(row[key] for key in ('RHS_bitwise', 'complete_state_columns_bitwise', 'complete_parameter_columns_bitwise')):
            raise AssertionError(row)
        comparisons.append(row)
        del old_rhs, new_rhs, old_dy, old_dp, new_dy, new_dp
    obj.initial(p)
    gc.collect()
    automatic_gc = gc.isenabled()
    gc.disable()
    old_flow, old_core = weakref.ref(obj._flow), weakref.ref(obj._core)
    bad_y = Y.copy()
    bad_y[-1, :] += 1.e4
    trial_p = p.copy()
    trial_p[0] += 1.e-8
    trial_p[1] += 1.e-4

    def failure(call):
        try:
            call(t, bad_y, trial_p)
        except FloatingPointError as error:
            return dict(type=type(error).__module__+'.'+type(error).__qualname__, message=str(error))
        raise AssertionError('The explicitly perturbed field did not reach the original domain exception')

    try:
        original_error = failure(previous.split_rhs(obj.fun, 8))
        old_kept = dict(flow=old_flow() is not None, core=old_core() is not None)
        if not all(old_kept.values()):
            raise AssertionError('The actual old Flow/core retention was not observed')
        # Replay the exact same failed field and parameter vector. Collection
        # in finally now releases the already unreachable previous Flow/core.
        new_error = failure(lifecycle.split_rhs(obj.fun, 8, stats, events.append))
        new_released = dict(flow=old_flow() is None, core=old_core() is None)
        if original_error != new_error or not all(new_released.values()):
            raise AssertionError((original_error, new_error, new_released))
    finally:
        if automatic_gc:
            gc.enable()
        gc.collect()
    result = dict(scope=__doc__, status='actual_small_block_and_exception_lifecycle_check_passed',
        source_run=str(source_path), source_run_sha256=sha(source_path),
        snapshot=str(snapshot), snapshot_sha256=sha(snapshot),
        source_dimensions=dict(n=obj.n, nodes=len(x), parameters=len(p)),
        sampled_source_indices=indices.tolist(), comparisons=comparisons,
        lifecycle_probe=dict(automatic_cyclic_gc_disabled_during_probe=True,
            artificially_raised_exception=False,
            deliberately_perturbed_unaccepted_field=True,
            trial_parameter_changes=dict(additive_delta=1.e-8, first_scaled_support=1.e-4),
            trial_last_height_component_increment=1.e4,
            exception_is_actual_original_domain_guard=True,
            old_flow_and_core_retained_without_collection=old_kept,
            old_flow_and_core_released_by_finally_collection=new_released,
            exception_type_and_message_identical=original_error == new_error,
            original_exception=original_error, successor_exception=new_error,
            no_actual_solver_domain_event_inferred=True),
        lifecycle_statistics=stats, exception_release_events=events,
        fourier_cache=fourier_stats, core_memo=memo_stats, analytical_delta=delta_stats,
        source_hashes={str(file.resolve()):sha(file) for file in (
            Path(__file__), Path(lifecycle.__file__), Path(fourier.__file__),
            Path(memo.__file__), Path(delta.__file__), portable,
            SCRIPTS/'resume_20261126/streamed_release_prefix_driver.py')},
        full_J_assembled=False, BVP_steps_applied=0, accepted_field_produced=False,
        original_numerical_gates_changed=False,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        seconds=time.monotonic()-started)
    (args.outdir/'comparison.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key:result[key] for key in ('status', 'comparisons', 'lifecycle_probe', 'maximum_rss_kib', 'seconds')}, indent=2), flush=True)


if __name__ == '__main__':
    main()

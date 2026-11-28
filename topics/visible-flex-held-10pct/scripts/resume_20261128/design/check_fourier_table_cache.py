#!/usr/bin/env python3
"""Compare original and cached Jacobians on a genuine saved BVP iterate.

No BVP solver is called and no new field is accepted.  The original portable
problem constructor consumes a copied actual snapshot, then the same full
state is evaluated unbatched, with the existing block-eight grouping, and
with the new read-only CSR cache.  Generated arrays remain outside Git.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gc
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import resource
import shutil
import sys
import time
import numpy as np
import cached_fourier_tables as cache


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run', type=Path, required=True)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    out = args.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    snapshot = out / 'actual-snapshot.npz'
    shutil.copyfile(args.snapshot, snapshot)
    captured_source = out / 'source-run-captured.json'
    captured_source.write_bytes(args.source_run.read_bytes())
    source = json.loads(captured_source.read_text())
    command = list(source['command'][2:])
    scripts = Path(__file__).resolve().parents[2]
    portable = scripts / 'resume_m3/portable_prefix_continue.py'
    original = load('_cache_check_original_portable', portable)
    captured = {}

    def capture(obj, x, y, p):
        captured.update(obj=obj, x=x, y=y, p=p)

    before = inspect.getsource(original.main)
    marker = '        rhs = o.fun(x,y,par)'
    if before.count(marker) != 1:
        raise ValueError('Original initial-domain capture statement differs')
    after = before.replace(marker, '        _cache_capture(o,x,y,par)\n        return')
    original.__dict__['_cache_capture'] = capture
    exec(compile(after, str(portable) + '::capture_without_solver', 'exec'), original.__dict__)
    command[command.index('--outdir') + 1] = str(out / 'problem-construction')
    for flag in ('--restart-checkpoint', '--raw-restart'):
        if flag in command:
            at = command.index(flag)
            del command[at:at+2]
    command.extend(['--raw-restart', str(snapshot)])
    sys.argv = [str(portable), *command]
    original.main()
    obj, x, y, p = (captured[name] for name in ('obj', 'x', 'y', 'p'))
    batches = load('_cache_check_original_batches',
                   scripts / 'resume_20261126/streamed_release_prefix_driver.py')
    times = {}

    def evaluate(label, grouped):
        obj._flow = None
        obj._flow_key = None
        gc.collect()
        begin = time.monotonic()
        block = 8 if grouped is True else grouped
        rhs = batches.split_rhs(obj.fun, block) if grouped else obj.fun
        jac = batches.split_jac(obj.fun_jac, block) if grouped else obj.fun_jac
        value = rhs(x, y, p)
        dy, dp = jac(x, y, p)
        times[label] = time.monotonic() - begin
        return value, dy, dp

    full = evaluate('original_full', False)
    split = evaluate('original_block8', True)
    stats = cache.install(sys.modules['portable_m3_fourier_jac'])
    cached = evaluate('cached_block8_cold', True)
    warm = evaluate('cached_block8_warm', True)
    larger = evaluate('cached_block64', 64)

    def difference(left, right):
        return {name: dict(max_abs=float(np.max(np.abs(a-b))),
                          exact_equal=bool(np.array_equal(a, b)),
                          original_max_abs=float(np.max(np.abs(a))))
                for name, a, b in zip(('rhs', 'dy', 'dp'), left, right)}

    result = dict(scope=__doc__, source_run=str(args.source_run.resolve()),
        source_run_sha256=sha(captured_source), snapshot_sha256=sha(snapshot),
        source_sha256=sha(__file__), cache_sha256=sha(cache.__file__),
        portable_sha256=sha(portable), nodes=len(x), dimension=obj.n, modes=obj.M,
        original_vs_block8=difference(full, split),
        block8_vs_cached=difference(split, cached),
        cached_cold_vs_warm=difference(cached, warm), times_seconds=times,
        original_vs_cached_block64=difference(full, larger),
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        actual_cache_stats=stats, BVP_solver_invoked=False, accepted_field=False,
        original_acceptance_gates_changed=False)
    (out / 'summary.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    if not all(item['exact_equal'] for item in result['block8_vs_cached'].values()):
        raise AssertionError('The cache changed the actual original block-eight evaluation')
    if not all(item['exact_equal'] for item in result['original_vs_cached_block64'].values()):
        raise AssertionError('The block-64 evaluation differs from the same original actual state')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()

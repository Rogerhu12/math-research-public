#!/usr/bin/env python3
"""Compare angular RHS quadrature at the same complete saved A field.

This is a design-speed diagnostic, not a solve, a boundary audit or fixed-g
convergence of accepted solutions. All physical profile and full state data
are retained. Only the explicitly reported angular evaluation grid varies.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np
import root_20261114_radial_thread_benchmark as bench
import root_20261114_radial_threads as parallel


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'source-topic', 'port', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--angles', type=int, nargs='+', default=[640, 960])
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    # Record loaded sources before any lengthy evaluation. The repository may
    # be rebased for an independent completed result while this process runs.
    source_fingerprints = {Path(path).name:hashlib.sha256(Path(path).read_bytes()).hexdigest()
                           for path in (__file__, bench.__file__, parallel.__file__)}
    opener = gzip.open if args.input.suffix == '.gz' else open
    with opener(args.input, 'rt') as source:
        record = json.load(source)
    reference_angle = int(record['config']['angular'])
    namespace, provenance = bench.build('audit', bench.HERE / 'strong_anchor_interior_fullmean_audit.py')
    observation = dict(provider_loads=0, saved_fields=[])
    loader = namespace['install_audit_loader'](bench.module, observation)(
        'angular_comparison_saved_loader', bench.HERE / 'geometric-checkpoint-core-pullback.py')
    parallel.configure(args.workers)
    rows = []
    reference = reference_mesh = reference_parameters = reference_state = None
    for requested_angle in dict.fromkeys([reference_angle] + args.angles):
        saved, _ = loader.load_saved(args.input, args.source_topic, args.port, angular=requested_angle)
        grid = np.sort(np.r_[saved.sol.x, (saved.sol.x[:-1] + saved.sol.x[1:]) / 2])
        state = saved.sol.sol(grid)
        if reference is not None:
            if not (np.array_equal(grid, reference_mesh) and
                    np.array_equal(state, reference_state) and
                    np.array_equal(saved.sol.p, reference_parameters)):
                raise AssertionError('Physical input field changed between evaluations')
        start = time.perf_counter()
        result = parallel.value(saved.flow, grid, state, saved.sol.p, 24)
        seconds = time.perf_counter() - start
        if reference is None:
            reference = result.copy()
            reference_mesh = grid.copy()
            reference_state = state.copy()
            reference_parameters = saved.sol.p.copy()
        difference = result - reference
        scaled = abs(difference) / (1 + abs(reference))
        index = np.unravel_index(np.argmax(scaled), scaled.shape)
        row = dict(requested_angle=requested_angle, actual_angle=saved.flow.nt,
                   seconds=seconds, max_abs_difference=float(abs(difference).max()),
                   max_scaled_difference=float(scaled.max()),
                   rms_scaled_difference=float(np.sqrt(np.mean(scaled**2))),
                   worst_scaled_component=int(index[0]), worst_scaled_s=float(grid[index[1]]),
                   all_finite=bool(np.isfinite(result).all()),
                   input_state_bitwise_equal=True)
        if not row['all_finite']:
            raise FloatingPointError(row)
        rows.append(row)
        print(json.dumps(row), flush=True)
    parallel.close()
    report = dict(scope=__doc__, input=str(args.input),
                  input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  source_sha256=source_fingerprints,
                  reference_angular=reference_angle, modes=saved.flow.M,
                  radial_nodes_plus_midpoints=len(reference_mesh),
                  compared_values=int(reference.size), workers=args.workers, rows=rows,
                  loader_provenance=provenance, original_profile=observation,
                  original_scientific_config=record['config'],
                  boundary_evaluated=False, new_nonlinear_solution=False,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  parallel_stats=parallel.STATS)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + '\n')


if __name__ == '__main__':
    main()

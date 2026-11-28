#!/usr/bin/env python3
"""Run the same complete actual-matrix comparison with bounded cached assembly.

Only read-only Fourier CSR tables and the radial evaluation block size change.
The original check still reconstructs the whole original model, all state and
parameter columns, all boundary rows, and compares QR with SuperLU on that J.
No Newton or BVP step is applied. The old in-flight check source is unmodified.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import check_block_qr as original


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--rhs-block', type=int, default=32)
    args, rest = parser.parse_known_args()
    if args.rhs_block < 1:
        raise ValueError('A positive complete radial block is required')
    here = Path(__file__).resolve().parent
    cache_path = here/'design/cached_fourier_tables.py'
    base_load = original.load
    cache = base_load('_qr_cached_assembly_tables', cache_path)
    cache_stats = []

    def load(name, path):
        value = base_load(name, path)
        if Path(path).name == 'portable_prefix_continue.py':
            original_module = value.module
            def problem_module(key, file):
                problem = original_module(key, file)
                if Path(file).name == '78718-prefix-fourier-jacobian.py':
                    cache_stats.append(cache.install(problem))
                return problem
            value.module = problem_module
        elif Path(path).name == 'streamed_release_prefix_driver.py':
            split_rhs, split_jac = value.split_rhs, value.split_jac
            value.split_rhs = lambda fun, _old_block: split_rhs(fun, args.rhs_block)
            value.split_jac = lambda fun, _old_block: split_jac(fun, args.rhs_block)
        return value

    original.load = load
    out = Path(rest[rest.index('--outdir')+1]) if '--outdir' in rest else None
    sys.argv = [str(Path(original.__file__).resolve()), *rest]
    try:
        original.main()
    finally:
        if out is not None and out.is_dir():
            provenance = dict(scope=__doc__, actual_rhs_jac_block=args.rhs_block,
                source_hashes={str(file): sha(file) for file in
                    (Path(__file__).resolve(), Path(original.__file__).resolve(),
                     cache_path, here/'block_qr.py')},
                actual_cache_stats=cache_stats, complete_original_matrix=True,
                original_equations_changed=False, BVP_steps_applied=0,
                geometry_or_response_cached=False)
            (out/'cached-assembly.json').write_text(
                json.dumps(provenance, indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()

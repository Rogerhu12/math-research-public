#!/usr/bin/env python3
"""Run an explicit original entry with isolated parallel radial RHS batches."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import root_radial_batching as radial
import root_20261114_radial_threads as parallel


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--radial-workers', type=int, default=4)
    parser.add_argument('--target-entry', type=Path, required=True)
    parser.add_argument('--parallel-run-record', type=Path, required=True)
    options, remaining = parser.parse_known_args()
    if options.parallel_run_record.exists():
        raise FileExistsError(options.parallel_run_record)
    target = options.target_entry.resolve()
    source = Path(__file__).resolve()
    record = dict(target=str(target), target_sha256=sha(target),
                  adapter_sha256=sha(source), radial_adapter_sha256=sha(parallel.__file__),
                  original_radial_sha256=sha(radial.__file__), workers=options.radial_workers,
                  original_entry_argv=remaining, equations_or_acceptance_changed=False,
                  isolated_deepcopy_per_worker=True, process_fork_used=False)
    parallel.configure(options.radial_workers)
    previous, old_argv = radial.value, sys.argv
    radial.value = parallel.value
    started = time.perf_counter()
    try:
        spec = importlib.util.spec_from_file_location('root_threaded_explicit_target', target)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        sys.argv = [str(target), *remaining]
        module.main()
        record['entry_returned_normally'] = True
    except BaseException as error:
        record['entry_returned_normally'] = False
        record['error_type'] = type(error).__name__
        record['error'] = str(error)
        raise
    finally:
        radial.value, sys.argv = previous, old_argv
        parallel.close()
        record.update(seconds=time.perf_counter()-started, stats=parallel.STATS,
                      peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        options.parallel_run_record.parent.mkdir(parents=True, exist_ok=True)
        options.parallel_run_record.write_text(json.dumps(record, indent=2)+'\n')


if __name__ == '__main__':
    main()

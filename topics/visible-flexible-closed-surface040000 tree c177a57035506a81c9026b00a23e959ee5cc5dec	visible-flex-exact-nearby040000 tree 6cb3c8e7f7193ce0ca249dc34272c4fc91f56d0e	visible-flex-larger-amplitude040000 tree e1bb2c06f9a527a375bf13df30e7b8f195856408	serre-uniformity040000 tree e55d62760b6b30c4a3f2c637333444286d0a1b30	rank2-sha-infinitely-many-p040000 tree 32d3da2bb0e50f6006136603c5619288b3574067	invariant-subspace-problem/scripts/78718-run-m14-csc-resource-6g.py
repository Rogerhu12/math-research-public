#!/usr/bin/env python3
"""Apply an explicit per-process resource budget, then the original disk guard.

This new wrapper runs the separately bound direct-CSC M14 command.  It changes
no numerical argument, source callback, solver, or acceptance threshold.
RLIMIT_DATA is inherited per process and is not an aggregate RSS limit.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import resource

CAP = 6 * 1024 * 1024 * 1024
GUARD_SHA = 'cf1e2364300015c841b2070be51e948dc7ba37ef5b98eef0441819bca1e6aabd'


def main():
    path = Path(__file__).with_name('db6f-root-run-space-guarded.py')
    if hashlib.sha256(path.read_bytes()).hexdigest() != GUARD_SHA:
        raise ValueError('Original disk guard source changed')
    prior = resource.getrlimit(resource.RLIMIT_DATA)
    effective = min([CAP] + [v for v in prior if v != resource.RLIM_INFINITY])
    if effective <= 0:
        raise ValueError('No positive DATA budget')
    resource.setrlimit(resource.RLIMIT_DATA, (effective, effective))
    actual = resource.getrlimit(resource.RLIMIT_DATA)
    if actual != (effective, effective):
        raise RuntimeError('DATA limit was not applied')
    print(json.dumps({
        'event': 'new_environment_direct_CSC_M14_per_process_DATA_budget',
        'requested_bytes': CAP, 'effective_limits': actual, 'prior_limits': prior,
        'original_Node_heap_MiB': 1536, 'mathematical_arguments_unchanged': True,
        'scope': 'Per process only; no aggregate-memory or convergence guarantee.',
    }), flush=True)
    spec = importlib.util.spec_from_file_location('unchanged_M14_disk_guard', path)
    guard = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(guard)
    guard.main()


if __name__ == '__main__':
    main()

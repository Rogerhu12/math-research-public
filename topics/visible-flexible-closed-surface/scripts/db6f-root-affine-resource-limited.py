#!/usr/bin/env python3
"""Per-process data-memory cap around the unchanged affine disk supervisor.

Only for the no-tail-subprocess affine diagnostic. This is a resource budget,
not a numerical tolerance or a claim of sufficient memory. Never select this
wrapper for the true coupled/Node route without a separate resource review.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import resource

CAP = 1536 * 1024 * 1024
GUARD_SHA = 'cf1e2364300015c841b2070be51e948dc7ba37ef5b98eef0441819bca1e6aabd'


def main():
    path = Path(__file__).with_name('db6f-root-run-space-guarded.py')
    assert hashlib.sha256(path.read_bytes()).hexdigest() == GUARD_SHA
    prior = resource.getrlimit(resource.RLIMIT_DATA)
    finite = [v for v in prior if v != resource.RLIM_INFINITY]
    effective = min([CAP] + finite)
    assert effective > 0
    resource.setrlimit(resource.RLIMIT_DATA, (effective, effective))
    actual = resource.getrlimit(resource.RLIMIT_DATA)
    assert actual == (effective, effective)
    print(json.dumps({'event':'affine_only_per_process_RLIMIT_DATA_budget',
                      'requested_bytes':CAP,'effective_limits':actual,
                      'prior_limits':prior,'numerical_inputs_unchanged':True,
                      'scope':'Resource cap only, inherited by the one affine child; not total RSS/cgroup control or mathematical success.'}), flush=True)
    spec = importlib.util.spec_from_file_location('original_affine_disk_guard',path)
    guard = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(guard)
    guard.main()


if __name__ == '__main__':
    main()

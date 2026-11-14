#!/usr/bin/env python3
"""Independent full bitwise polynomial comparison for both finite-tail formats.

This verifies storage/operation equivalence only; it does not certify new
metric bounds or replace the independent mathematical adapter review.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('root_review_stream_adapter', HERE/'db6f-audit-tail-stream.py')
adapter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = adapter
spec.loader.exec_module(adapter)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def identical(a, b):
    return (a.lo.shape == b.lo.shape and
            np.array_equal(a.lo.view(np.uint64), b.lo.view(np.uint64)) and
            np.array_equal(a.hi.view(np.uint64), b.hi.view(np.uint64)))


def compare(path):
    start = time.time()
    old = adapter.frozen.ExactIntegratedTail(path)
    new = adapter.StreamingExactIntegratedTail(path)
    assert old.rq == new.rq and old.lq == new.lq
    assert old.cuff == new.cuff and old.collar_length == new.collar_length
    assert old.M == new.M and old.N == new.N and old.C == new.C
    assert identical(old.endpoint_value_enclosure, new.endpoint_value_enclosure)
    assert all(identical(a, b) for a, b in zip(old.collar, new.collar))
    checked = 0
    for index in range(old.N):
        for a, b in zip(old.polys, new.span_polys(index)):
            assert identical(a[index], b), ('polynomial difference', index)
            checked += a[index].lo.size
    assert new.expand.__func__ is old.expand.__func__
    assert new.interval_radius.__func__ is old.interval_radius.__func__
    result = {'manifest': str(path), 'manifest_sha256': sha(path),
              'format': old.meta['status'], 'spans': old.N,
              'coefficient_slots_per_endpoint': checked,
              'all_F_G_Gp_endpoints_bitwise_identical': True,
              'endpoint_value_and_collar_bitwise_identical': True,
              'exact_radial_nodes_lengths_cuff_identical': True,
              'same_inherited_expand_and_radius_functions': True,
              'seconds': time.time()-start}
    del old, new
    gc.collect()
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('manifests', type=Path, nargs='+')
    args = p.parse_args()
    reports = []
    for manifest in args.manifests:
        r = compare(manifest)
        reports.append(r)
        print(json.dumps({'checked': r['manifest'], 'spans': r['spans'],
                          'bitwise_identical': True, 'seconds': r['seconds']}), flush=True)
    out = {'status': 'independent-full-storage-adapter-equivalence-PASS',
           'reviewer': 'Astra-visible-flex-db6f0b0e/root', 'script_sha256': sha(__file__),
           'adapter_sha256': sha(HERE/'db6f-audit-tail-stream.py'),
           'frozen_backend_sha256': sha(HERE/'db6f-audit-tail-metric-curvature.py'),
           'reports': reports,
           'peak_process_rss_bytes': int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024,
           'scope': __doc__}
    args.out.write_text(json.dumps(out, indent=2)+'\n')


if __name__ == '__main__':
    main()

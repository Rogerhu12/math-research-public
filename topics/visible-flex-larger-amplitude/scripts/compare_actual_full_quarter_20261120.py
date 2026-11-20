#!/usr/bin/env python3
"""One actual-input comparison of new full-grid and quarter-grid batches.

This does not run the old dense operator, a geometric audit, or a solve.
Only the compact comparison is written; all field/residual arrays remain
process-local and the supplied bundle is read-only.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def relative(a, b):
    return float(np.linalg.norm((a-b).ravel())/
                 max(1., np.linalg.norm(a.ravel()), np.linalg.norm(b.ravel())))


def gram_max(values):
    e, f, g = values[..., 0], values[..., 1], values[..., 2]
    return float(np.max((np.abs(e+g)+np.sqrt((e-g)**2+4*f*f))/2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle', 'operator', 'implementation', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--stage-block', type=int, default=64)
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError('The requested actual comparison output already exists')
    module = load('actual_full_quarter_batched', args.implementation)
    data = np.load(args.bundle, allow_pickle=False)
    M = (data['qjets'].shape[-1]-2)//3
    construction = (args.operator, data['mesh'], data['a_stages'],
                    float(data['radius']), data['fixed_core_first3'])
    options = dict(M=M, N=args.angles, width=float(data['width']),
                   stage_block=args.stage_block)
    full = module.create(*construction, quarter=False, **options)
    quarter = module.create(*construction, quarter=True, **options)
    x, affine = full.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    xq, affineq = quarter.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    if not np.array_equal(x, xq):
        raise ValueError('Angular restriction must not alter the free vector')
    del xq
    timings = {}
    clock = time.perf_counter()
    cache_full = full.set_base(x)
    timings['full_cache_seconds'] = time.perf_counter()-clock
    clock = time.perf_counter()
    cache_quarter = quarter.set_base(x)
    timings['quarter_cache_seconds'] = time.perf_counter()-clock
    clock = time.perf_counter()
    rf = full.residual(x)
    timings['full_residual_seconds'] = time.perf_counter()-clock
    clock = time.perf_counter()
    rq = quarter.residual(x)
    timings['quarter_residual_seconds'] = time.perf_counter()-clock
    frobenius = np.array([1., 2., 1.])
    full_sse = float(np.sum(rf*rf*frobenius))
    quarter_sse = float(np.sum(rq*rq*frobenius))
    rawq = quarter.unweight(rq)
    angle_values_relative = relative(rf[:, :quarter.N], rawq)
    angle_values_max = float(np.max(np.abs(rf[:, :quarter.N]-rawq)))
    physical_full_max, physical_quarter_max = gram_max(rf), gram_max(rawq)
    del rawq
    clock = time.perf_counter()
    gf = full.vjp(x, rf*frobenius)
    timings['full_gradient_seconds'] = time.perf_counter()-clock
    clock = time.perf_counter()
    gq = quarter.vjp(x, rq*frobenius)
    timings['quarter_gradient_seconds'] = time.perf_counter()-clock
    gradient_relative = relative(gf, gq)
    norm_relative = abs(full_sse-quarter_sse)/max(1., full_sse, quarter_sse)
    report = dict(
        schema='actual-batched-full-quarter-Gram-comparison-20261120-v1',
        source_sha256=digest(__file__), operator_sha256=digest(args.operator),
        implementation_sha256=digest(args.implementation),
        bundle_sha256=digest(args.bundle), bundle=str(args.bundle),
        M=M, J=full.J, stages=full.P, full_N=full.N, quarter_N=quarter.N,
        full_rows=full.P*full.N*3, quarter_rows=quarter.P*quarter.N*3,
        free_size=full.free_size, stage_block=args.stage_block,
        affine_full=affine, affine_quarter=affineq,
        full_frobenius_sse=full_sse, quarter_frobenius_sse=quarter_sse,
        squared_norm_relative=norm_relative,
        quarter_physical_values_relative=angle_values_relative,
        quarter_physical_values_max_absolute=angle_values_max,
        full_physical_max_gram=physical_full_max,
        quarter_physical_max_gram=physical_quarter_max,
        full_quarter_frobenius_gradient_relative=gradient_relative,
        cache_full=cache_full, cache_quarter=cache_quarter, timings=timings,
        process_peak_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024),
        old_dense_evaluations=0, geometric_audits=0, nonlinear_solves=0,
        mathematical_scope='The same finite original angle-grid Gram objective and free affine space; no continuous metric or closed-flexibility assertion')
    report['comparison_passed'] = (norm_relative < 2e-11
                                  and angle_values_relative < 2e-11
                                  and gradient_relative < 2e-10)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    if not report['comparison_passed']:
        raise SystemExit('Actual full-quarter comparison failed')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Measure the actual endpoint collocation defect and its quintic lobe scale.

The cubic collocation midpoint is reconstructed in the recorded numerical
coordinate, not in physical arclength. The lobe scale (10/sqrt(3))*|e|/h_s^2
is the exact norm for an isolated endpoint-position correction e*S(u).
It is a diagnostic for one source of C2 error, not a bound for the whole map.
"""
import os
for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[k] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
import root_radial_batching as radial
from root_neck_chart import NeckChart

HERE = Path(__file__).resolve().parent
SOURCE_HASH = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'source-topic', 'port', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--angular', type=int, default=512)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('root_collocation_pullback',
                                                 HERE / 'geometric-checkpoint-core-pullback.py')
    pullback = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pullback)
    start = time.time()
    with gzip.open(args.input, 'rt') if args.input.suffix == '.gz' else args.input.open() as handle:
        metadata = json.load(handle)
    saved, _ = pullback.load_saved(args.input, args.source_topic, args.port,
                                   angular=metadata['config']['angular'])
    flow = saved.flow
    record = saved.rec['numerical_meridian_chart']
    chart = NeckChart(record['reference_t'], record['physical_s'])
    s = saved.sol.x
    t = chart.inverse(s)
    # Remove the ordinary inverse's user-facing stopping error before dividing
    # tiny endpoint defects by short radial lengths. No saved point is changed.
    for _ in range(6):
        sr, ds = chart.evaluate(t)
        t -= (sr - s) / ds
    sr, ds = chart.evaluate(t)
    h = np.diff(t)
    hs = np.diff(s)
    y = saved.sol.sol(s)
    v = radial.value(flow, s, y, saved.sol.p, batch_size=24) * ds[None, :]
    ym = (y[:, :-1] + y[:, 1:]) / 2 - h[None, :] * (v[:, 1:] - v[:, :-1]) / 8
    sm, dsm = chart.evaluate((t[:-1] + t[1:]) / 2)
    vm = radial.value(flow, sm, ym, saved.sol.p, batch_size=24) * dsm[None, :]
    defect = (y[:, 1:] - y[:, :-1]) - h[None, :] * (v[:, :-1] + v[:, 1:] + 4 * vm) / 6
    relative = np.max(np.abs(defect) / (h[None, :] * (1 + np.abs(vm))), axis=0)
    B, _, _ = flow.basis(args.angular)
    cart_norm = np.empty(len(h))
    for first in range(0, len(h), 24):
        sl = slice(first, first + 24)
        cart_norm[sl] = np.max(np.linalg.norm(flow.q * flow.values(defect[:, sl], B), axis=2), axis=1)
    scale = (10 / np.sqrt(3)) * cart_norm / hs**2
    indices = np.argsort(scale)[-12:][::-1]
    rows = [dict(interval=int(j), s_left=float(s[j]), s_right=float(s[j + 1]),
                 physical_width=float(hs[j]), numerical_width=float(h[j]),
                 relative_collocation_defect=float(relative[j]),
                 cartesian_endpoint_defect=float(cart_norm[j]),
                 isolated_quintic_second_lobe_scale=float(scale[j])) for j in indices]
    output = dict(scope=__doc__, input=str(args.input),
                  input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  source_sha256=SOURCE_HASH, modes=saved.M, quadrature=flow.nt,
                  angular=args.angular, numerical_coordinate_reconstruction_error=float(np.max(abs(sr-s))),
                  maximum_relative_collocation_defect=float(np.max(relative)),
                  worst_lobe_scales=rows, seconds=time.time()-start)
    args.out.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output))


if __name__ == '__main__':
    main()

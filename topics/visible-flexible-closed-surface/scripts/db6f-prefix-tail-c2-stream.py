#!/usr/bin/env python3
"""Finite C2 comparison using the reviewed low-memory exact-tail adapter.

The existing exact common-partition and Fourier/Bernstein comparison is
unchanged. Coefficient axes are transposed and extended by exact zeroes
on demand. No global F/G/Gp arrays are built.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
from types import SimpleNamespace
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('first')
    parser.add_argument('second')
    parser.add_argument('out')
    parser.add_argument('--batch', type=int, default=64)
    args = parser.parse_args()
    if args.batch <= 0:
        raise ValueError('Positive batch size required')
    out = Path(args.out)
    if out.exists():
        raise FileExistsError(out)
    paths = [str(Path(p).resolve()) for p in (args.first, args.second)]
    backend = module('db6f_prefix_c2_stream_backend', HERE/'db6f-tail-c2-compare.py')
    adapter = module('db6f_prefix_c2_stream_geometry', HERE/'db6f-audit-tail-stream.py')
    geoms = [adapter.StreamingExactIntegratedTail(p) for p in paths]
    planar = np.unique(np.concatenate([g.reader.planar_modes for g in geoms]))
    height = np.unique(np.concatenate([g.reader.height_modes for g in geoms]))
    P, C = len(planar), len(planar)+len(height)

    class BatchPolynomials:
        def __init__(self, geom):
            self.geom = geom
            self.slots = [int(np.flatnonzero(planar == m)[0]) for m in geom.reader.planar_modes]
            self.slots += [P+int(np.flatnonzero(height == m)[0]) for m in geom.reader.height_modes]
            self.key, self.values = None, None

        def obtain(self, indices, order):
            key = tuple(map(int, np.asarray(indices).ravel()))
            if key != self.key:
                arrays = [[np.zeros((len(key), C, 6-j)) for _ in range(2)] for j in range(3)]
                for row, index in enumerate(key):
                    for j, p in enumerate(self.geom.span_polys(index)):
                        arrays[j][0][row, self.slots, :] = p.lo.T
                        arrays[j][1][row, self.slots, :] = p.hi.T
                self.values = [backend.I(lo, hi) for lo, hi in arrays]
                self.key = key
            return self.values[order]

    class OrderView:
        def __init__(self, batch, order):
            self.batch, self.order = batch, order

        def __getitem__(self, indices):
            return self.batch.obtain(indices, self.order)

    views = {}
    for path, g in zip(paths, geoms):
        batch = BatchPolynomials(g)
        views[path] = SimpleNamespace(meta=g.meta, geom=g, planar_modes=planar,
                                     height_modes=height, P=P, C=C,
                                     polys=[OrderView(batch, j) for j in range(3)])
    backend.IntegratedTail = lambda p: views[str(Path(p).resolve())]
    backend.exact_nodes = lambda t: t.geom.rq
    backend.polynomials = lambda t, nodes: t.polys
    backend.main()
    report = json.loads(out.read_text())
    report['streaming_comparison_adapter'] = dict(
        file=str(Path(__file__).resolve()), sha256=sha(__file__),
        exact_geometry_adapter_sha256=sha(HERE/'db6f-audit-tail-stream.py'),
        exact_geometry_backend_sha256=sha(HERE/'db6f-audit-tail-metric-curvature.py'),
        reader_sha256=sha(HERE/'db6f_tail_integrated.py'),
        peak_process_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024,
        batch=args.batch, mathematical_change=False,
        operation='Reviewed exact F/G/Gp coefficients: transpose degree/coefficient axes and extend signed Fourier labels by exact zeros; original common-partition comparison unchanged.')
    report['mode_alignment'] = dict(
        original=[dict(planar=list(map(int, g.reader.planar_modes)),
                       height=list(map(int, g.reader.height_modes))) for g in geoms],
        common_planar=list(map(int, planar)), common_height=list(map(int, height)))
    report['source_checkpoint_hashes'] = [g.meta.get('inputSHA256') for g in geoms]
    report['same_source_checkpoint'] = report['source_checkpoint_hashes'][0] == report['source_checkpoint_hashes'][1]
    report['height_gauges'] = [g.meta.get('gauge') for g in geoms]
    report['exact_anchors'] = [[str(g.rq[0]), str(g.rq[-1])] for g in geoms]
    report['collars_compared'] = False
    report['scope_addendum'] = (
        'Only perturbations on the exact intersection of the exterior domains are compared. '
        'The fixed rotational background cancels. R6 collars, omitted end slivers and '
        'closed-map height normalization are not included. Equal source checkpoint hashes '
        'do not imply identical interior RK evaluators or stage-end compensation; inspect '
        'the two manifest settings and stageDefects separately.')
    out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(peak_rss=report['streaming_comparison_adapter']['peak_process_rss_bytes'],
                          same_checkpoint=report['same_source_checkpoint'],
                          collars_compared=False)), flush=True)


if __name__ == '__main__':
    main()

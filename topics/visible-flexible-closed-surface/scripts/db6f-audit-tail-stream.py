#!/usr/bin/env python3
"""Low-memory storage adapter for the frozen continuous finite-tail verifier.

The exact finite map, interval formulas and order of node-value accumulation
are unchanged. Only V0 is stored globally; F/G/Gp are rebuilt for the current
span and cached. This file does not replace or edit the frozen verifier.
Its SHA is recorded in addition to the original mathematical backend SHA.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import resource
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('db6f_frozen_tail_for_stream', HERE/'db6f-audit-tail-metric-curvature.py')
frozen = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = frozen
spec.loader.exec_module(frozen)
I, base, poly, qbounds = frozen.I, frozen.base, frozen.poly, frozen.qbounds
BLOCK_SIZE = 128


class StreamingExactIntegratedTail(frozen.ExactIntegratedTail):
    """Same geometry enclosure, with only node V0 stored for all spans."""

    def __init__(self, manifest, block_size=None):
        block_size = BLOCK_SIZE if block_size is None else block_size
        frozen.check(isinstance(block_size, int) and block_size > 0,
                     'Positive integral streaming block size required')
        self.block_size = block_size
        self.path = Path(manifest)
        self.reader = t = frozen.IntegratedTail(manifest)
        self.meta = t.meta
        self.N, self.C, self.P = len(t.nodes)-1, t.C, t.P
        frozen.check(np.isfinite(t.nodes).all(), 'Nonfinite finite-tail data')
        frozen.check(t.first.shape == (self.N+1, self.C), 'Unexpected derivative shape')
        frozen.check(self.C == len(t.planar_modes)+len(t.height_modes), 'Mode count mismatch')
        frozen.check(len(set(map(int, t.planar_modes))) == self.P, 'Duplicate planar mode')
        frozen.check(len(set(map(int, t.height_modes))) == len(t.height_modes), 'Duplicate height mode')
        frozen.check(np.all(t.planar_modes % 3 == 1), 'Planar modes must be 1 modulo 3')
        frozen.check(np.all(t.height_modes >= 0) and np.all(t.height_modes % 3 == 0),
                     'Height modes must be nonnegative multiples of 3')
        self.M = max(max(abs((int(m)-1)//3) for m in t.planar_modes),
                     max(int(m)//3 for m in t.height_modes))
        if t.unscaled_lengths is None:
            self.rq = [frozen.exact(r) for r in t.nodes[:, 0]]
            self.lq = [b-a for a, b in zip(self.rq[:-1], self.rq[1:])]
        else:
            radial = t.meta['radialGeometry']
            self.lq = [frozen.exact(d)*t.radial_scale for d in t.unscaled_lengths]
            self.rq = [frozen.exact(radial['innerAnchor'])]
            for d in self.lq:
                self.rq.append(self.rq[-1]+d)
            frozen.check(self.rq[-1] == frozen.exact(radial['outerAnchor']),
                         'Exact normalized increments do not reach the declared outer anchor')
        frozen.check(all(d > 0 for d in self.lq), 'Nonpositive exact physical span')
        self.cuff = frozen.exact(self.meta['parameters']['rCuff'])
        self.collar_length = self.rq[0]-self.cuff
        frozen.check(self.cuff > 0 and self.collar_length > 0, 'Invalid R6 collar')

        # Same exact length enclosure and same increment expression as the
        # frozen constructor. No reduction across nodes or reordered sum.
        self._lengths = frozen.intervals(self.lq)[:, None]
        self._v0lo = np.empty((self.N, self.C), dtype=np.float64)
        self._v0hi = np.empty((self.N, self.C), dtype=np.float64)
        node = I(t.source_values[0])
        for start in range(0, self.N, block_size):
            stop = min(self.N, start+block_size)
            L = self._lengths[start:stop]
            u0, u1 = I(t.first[start:stop]), I(t.first[start+1:stop+1])
            v0, v1 = L*I(t.second[start:stop]), L*I(t.second[start+1:stop+1])
            increment = L*(qbounds(Q(7, 30))*(u0+u1)
                           +qbounds(Q(8, 15))*I(t.midpoint[start:stop])
                           +qbounds(Q(1, 60))*(v0-v1))
            for local, index in enumerate(range(start, stop)):
                self._v0lo[index] = node.lo
                self._v0hi[index] = node.hi
                node = node+increment[local]
        self._v0 = I(self._v0lo, self._v0hi)
        self.endpoint_value_enclosure = node

        # The collar expressions and their operation order are unchanged.
        cl = qbounds(self.collar_length)
        a0, a1, a2 = I(t.source_values[0]), I(t.first[0]), I(t.second[0])
        zero = I(np.zeros(self.C))
        c3 = 10*a0-4*cl*a1+qbounds(Q(1, 2))*cl.square()*a2
        c4 = -15*a0+7*cl*a1-cl.square()*a2
        c5 = 6*a0-3*cl*a1+qbounds(Q(1, 2))*cl.square()*a2
        self.collar = [
            base.stack([zero, zero, zero, c3, c4, c5], 0),
            base.stack([zero, zero, 3*c3/cl, 4*c4/cl, 5*c5/cl], 0),
            base.stack([zero, 6*c3/cl.square(), 12*c4/cl.square(), 20*c5/cl.square()], 0)]
        self._cached_index = None
        self._cached_polys = None

    def span_polys(self, index):
        frozen.check(0 <= index < self.N, 'Invalid finite-tail span')
        if self._cached_index != index:
            t = self.reader
            L = self._lengths[index]
            u0, u1 = I(t.first[index]), I(t.first[index+1])
            v0, v1 = L*I(t.second[index]), L*I(t.second[index+1])
            bubble = 16*I(t.midpoint[index])-8*(u0+u1)-2*(v0-v1)
            G = base.stack([u0, v0, -3*u0+3*u1-2*v0-v1+bubble,
                            2*u0-2*u1+v0+v1-2*bubble, bubble], 0)
            F = base.stack([self._v0[index]]+
                           [L*G[j]*qbounds(Q(1, j+1)) for j in range(5)], 0)
            Gp = base.stack([G[j+1]*(j+1)/L for j in range(4)], 0)
            self._cached_index = index
            self._cached_polys = [F, G, Gp]
        return self._cached_polys

    def fields(self, index, a, b):
        result = []
        raw_polys = self.collar if index == -1 else self.span_polys(index)
        for raw in raw_polys:
            local = poly.compose(raw, qbounds(a), qbounds(b-a))
            result.append(self.expand(local))
        return result


def main():
    global BLOCK_SIZE
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest', type=Path, required=True)
    ap.add_argument('--packet', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--angular', type=int, default=128)
    ap.add_argument('--radial', type=int, default=1)
    ap.add_argument('--background-curvature', type=float, default=6.)
    ap.add_argument('--direct-threshold', type=float, default=6.35)
    ap.add_argument('--minimum-span', type=int, default=-1)
    ap.add_argument('--maximum-span-exclusive', type=int)
    ap.add_argument('--limit', type=int)
    ap.add_argument('--progress', type=int, default=100)
    ap.add_argument('--block-size', type=int, default=128)
    args = ap.parse_args()
    frozen.check(args.block_size > 0, 'Positive streaming block size required')
    BLOCK_SIZE = args.block_size
    adapter_hash = frozen.sha(__file__)
    backend_hash = frozen.sha(HERE/'db6f-audit-tail-metric-curvature.py')
    frozen.ExactIntegratedTail = StreamingExactIntegratedTail
    frozen.run(args)
    report = json.loads(args.out.read_text())
    report['streaming_geometry_adapter'] = dict(
        file=str(Path(__file__).resolve()), sha256=adapter_hash,
        frozen_backend_sha256=backend_hash, block_size=BLOCK_SIZE,
        peak_process_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024,
        storage='Global V0 interval endpoints; one cached F/G/Gp span. Original node addition order unchanged.',
        changes_to_map_or_bound_formulas=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(report['streaming_geometry_adapter'], separators=(',', ':')))


if __name__ == '__main__':
    main()

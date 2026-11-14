#!/usr/bin/env python3
"""Memory-bounded evaluation of the already reviewed tail first-jet bounds.

Only batching changes. The exact interval operations, their order along each
radial coefficient, the Fourier/Bernstein bounds and the R6 collar are inherited
from db6f-tail-first-bounds.py. This is not a new source-equation certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
REFERENCE = HERE/'db6f-tail-first-bounds.py'
spec = importlib.util.spec_from_file_location('tail_first_stream_reference', REFERENCE)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
I, stack, qbounds = base.I, base.stack, base.qbounds


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def merge_summary(total, new):
    if total is None:
        return dict(new)
    for key, value in new.items():
        if key == 'label':
            if total[key] != value:
                raise ValueError('summary label changed')
        elif key == 'spans':
            total[key] += value
        elif isinstance(value, bool):
            total[key] = total[key] and value
        elif key.endswith('Lower'):
            total[key] = min(total[key], value)
        else:
            total[key] = max(total[key], value)
    return total


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('manifest', type=Path)
    ap.add_argument('out', type=Path)
    ap.add_argument('--batch', type=int, default=128)
    args = ap.parse_args()
    if args.batch <= 0:
        raise ValueError('batch must be positive')
    t = base.IntegratedTail(args.manifest)
    N, C, P = len(t.L), t.C, t.P
    if N <= 0:
        raise ValueError('empty radial partition')
    modes = np.concatenate([t.planar_modes, t.height_modes])
    value_node = I(t.source_values[0])
    radial_node = None if t.unscaled_lengths is None else I(t.meta['radialGeometry']['innerAnchor'])
    finite = None
    for begin in range(0, N, args.batch):
        end = min(N, begin+args.batch)
        if t.unscaled_lengths is None:
            length = I(t.nodes[begin+1:end+1, 0]) - I(t.nodes[begin:end, 0])
            r_lower = t.nodes[begin:end, 0]
        else:
            length = I(t.unscaled_lengths[begin:end]) * qbounds(t.radial_scale)
            rr = []
            for j in range(end-begin):
                rr.append(float(radial_node.lo))
                radial_node = radial_node + length[j]
            r_lower = np.array(rr)
        L = I(length.lo[:, None], length.hi[:, None])
        u0, u1 = I(t.first[begin:end]), I(t.first[begin+1:end+1])
        v0, v1 = L*I(t.second[begin:end]), L*I(t.second[begin+1:end+1])
        middle = I(t.midpoint[begin:end])
        A = 16*middle - 8*(u0+u1) - 2*(v0-v1)
        G = stack([u0, v0, -3*u0+3*u1-2*v0-v1+A,
                   2*u0-2*u1+v0+v1-2*A, A], -1)
        increment = L*(qbounds(Q(7, 30))*(u0+u1) +
                       qbounds(Q(8, 15))*middle + (v0-v1)*qbounds(Q(1, 60)))
        vl, vh = [], []
        for j in range(end-begin):
            vl.append(value_node.lo.copy())
            vh.append(value_node.hi.copy())
            value_node = value_node + increment[j]
        V0 = I(np.asarray(vl), np.asarray(vh))
        F = stack([V0]+[L*G[..., j]*qbounds(Q(1, j+1)) for j in range(5)], -1)
        Gp = stack([G[..., j+1]*(j+1)/L for j in range(4)], -1)
        current = base.inspect([F, G, Gp], r_lower, modes, P,
                               'finite exterior, exact saved definition')
        finite = merge_summary(finite, current)

    cuff = t.meta['parameters']['rCuff']
    deep = t.meta.get('radialGeometry', {}).get('innerAnchor', float(t.nodes[0, 0]))
    collarL = I(deep) - I(cuff)
    a0 = I(t.source_values[0][None, :])
    a1 = I(t.first[0][None, :])
    a2 = I(t.second[0][None, :])
    zero = I(np.zeros((1, C)))
    c3 = 10*a0-4*collarL*a1+qbounds(Q(1, 2))*collarL.square()*a2
    c4 = -15*a0+7*collarL*a1-collarL.square()*a2
    c5 = 6*a0-3*collarL*a1+qbounds(Q(1, 2))*collarL.square()*a2
    CF = stack([zero, zero, zero, c3, c4, c5], -1)
    CG = stack([zero, zero, 3*c3/collarL, 4*c4/collarL, 5*c5/collarL], -1)
    CGp = stack([zero, 6*c3/collarL.square(), 12*c4/collarL.square(),
                 20*c5/collarL.square()], -1)
    collar = base.inspect([CF, CG, CGp], np.array([cuff]), modes, P,
                          'exact R6 endpoint collar')
    result = {
        'status': 'continuous-outward-rounded-finite-tail-first-jet-certificate',
        'scope': base.__doc__,
        'manifest': str(args.manifest.resolve()),
        'manifestSHA256': sha(args.manifest),
        'scriptSHA256': sha(__file__),
        'intervalBackendSHA256': sha(base.backend),
        'readerSHA256': sha(HERE/'db6f_tail_integrated.py'),
        'referenceScriptSHA256': sha(REFERENCE),
        'streaming': {'batch': args.batch, 'description': __doc__},
        'finite': finite, 'collar': collar,
        'entireTail': {
            'planarDisplacementUpper': max(finite['r0theta0Planar'], collar['r0theta0Planar']),
            'heightDisplacementUpper': max(finite['r0theta0Height'], collar['r0theta0Height']),
            'planarJacobianPositive': finite['positivePlanarJacobian'] and collar['positivePlanarJacobian'],
            'allCrossSectionsSimple': finite['starShapedSimpleCrossSections'] and collar['starShapedSimpleCrossSections'],
            'planarJacobianOverRLower': min(finite['planarRadialJacobianOverRLower'],
                                           collar['planarRadialJacobianOverRLower']),
        },
        'notCertified': ['target metric', 'curvature or reach', 'source ODE',
                         'infinite nonlinear stable graph', 'prefix interface',
                         'actual total volume moment', 'README completion'],
    }
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['entireTail']))


if __name__ == '__main__':
    main()

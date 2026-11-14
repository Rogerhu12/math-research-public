#!/usr/bin/env python3
"""Continuous Fourier/Bernstein first-jet bounds for the explicit finite tail.

Includes the exact R6 endpoint collar down to the original cuff. The result
certifies the saved finite C2 map, not an ODE solution or an infinite graph.
No angular sampling and no source PDE evaluator are used.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np
from db6f_tail_integrated import IntegratedTail

backend = Path(__file__).with_name('db6f-audit-continuous-hermite.py')
spec = importlib.util.spec_from_file_location('db6f_interval_backend', backend)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
I, stack, qbounds, up = mod.I, mod.stack, mod.qbounds, mod.up


def power_to_bernstein(poly):
    """poly[...,j] is the coefficient of t**j on [0,1]."""
    d = poly.lo.shape[-1] - 1
    rows = []
    for k in range(d + 1):
        row = I(np.zeros(poly.lo.shape[:-1]))
        for j in range(k + 1):
            row = row + poly[..., j] * qbounds(Q(math.comb(k, j), math.comb(d, j)))
        rows.append(row)
    return stack(rows, -1)


def fourier_bound(poly, modes, begin, end, order):
    b = power_to_bernstein(poly).abs().hi
    total = np.zeros((b.shape[0], b.shape[-1]))
    for k in range(begin, end):
        total = up(total + up(b[:, k, :] * int(abs(modes[k]) ** order)))
    return np.max(total, axis=1)


def inspect(polys, r_lower, modes, P, label):
    C = len(modes)
    bounds = {}
    for j in range(3):
        for k in range(3-j):
            bounds[f'r{j}theta{k}Planar'] = fourier_bound(polys[j], modes, 0, P, k)
            bounds[f'r{j}theta{k}Height'] = fourier_bound(polys[j], modes, P, C, k)
    v = bounds['r0theta0Planar']
    vr = bounds['r1theta0Planar']
    vt = bounds['r0theta1Planar']
    vv, tt = I(v) / I(r_lower), I(vt) / I(r_lower)
    jac = 1 - I(vr) - tt - I(vr)*tt
    star = 1 - vv - tt - vv*tt
    summary = {key: float(np.max(val)) for key, val in bounds.items()}
    summary.update(label=label, spans=int(len(r_lower)),
                   planarRadialJacobianOverRLower=float(np.min(jac.lo)),
                   polarAngleDerivativeNumeratorOverR2Lower=float(np.min(star.lo)),
                   relativePlanarDisplacementUpper=float(np.max(vv.hi)),
                   relativePlanarAngularDerivativeUpper=float(np.max(tt.hi)),
                   positivePlanarJacobian=bool(np.all(jac.lo > 0)),
                   starShapedSimpleCrossSections=bool(np.all(star.lo > 0) and np.all(vv.hi < 1)))
    return summary


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('manifest')
    ap.add_argument('out')
    args = ap.parse_args()
    t = IntegratedTail(args.manifest)
    N, C, P = len(t.L), t.C, t.P
    modes = np.concatenate([t.planar_modes, t.height_modes])
    if t.unscaled_lengths is None:
        length = I(t.nodes[1:, 0]) - I(t.nodes[:-1, 0])
        r_lower = t.nodes[:-1, 0]
    else:
        length = I(t.unscaled_lengths) * qbounds(t.radial_scale)
        node = I(t.meta['radialGeometry']['innerAnchor'])
        rr = []
        for j in range(N):
            rr.append(float(node.lo))
            node = node + length[j]
        r_lower = np.array(rr)
    L = I(length.lo[:, None], length.hi[:, None])
    u0, u1 = I(t.first[:-1]), I(t.first[1:])
    v0, v1 = L*I(t.second[:-1]), L*I(t.second[1:])
    A = 16*I(t.midpoint) - 8*(u0+u1) - 2*(v0-v1)
    G = stack([u0, v0, -3*u0+3*u1-2*v0-v1+A,
               2*u0-2*u1+v0+v1-2*A, A], -1)
    increment = L*(qbounds(Q(7, 30))*(u0+u1) + qbounds(Q(8, 15))*I(t.midpoint) +
                   (v0-v1)*qbounds(Q(1, 60)))
    node = I(t.source_values[0])
    vl, vh = [], []
    for j in range(N):
        vl.append(node.lo.copy()); vh.append(node.hi.copy())
        node = node + increment[j]
    V0 = I(np.asarray(vl), np.asarray(vh))
    F = stack([V0]+[L*G[..., j]*qbounds(Q(1, j+1)) for j in range(5)], -1)
    Gp = stack([G[..., j+1]*(j+1)/L for j in range(4)], -1)
    finite = inspect([F, G, Gp], r_lower, modes, P, 'finite exterior, exact saved definition')

    cuff = t.meta['parameters']['rCuff']
    deep = t.meta.get('radialGeometry', {}).get('innerAnchor', float(t.nodes[0, 0]))
    collarL = I(deep) - I(cuff)
    a0, a1, a2 = I(t.source_values[0][None, :]), I(t.first[0][None, :]), I(t.second[0][None, :])
    zero = I(np.zeros((1, C)))
    c3 = 10*a0-4*collarL*a1+qbounds(Q(1, 2))*collarL.square()*a2
    c4 = -15*a0+7*collarL*a1-collarL.square()*a2
    c5 = 6*a0-3*collarL*a1+qbounds(Q(1, 2))*collarL.square()*a2
    CF = stack([zero, zero, zero, c3, c4, c5], -1)
    CG = stack([zero, zero, 3*c3/collarL, 4*c4/collarL, 5*c5/collarL], -1)
    CGp = stack([zero, 6*c3/collarL.square(), 12*c4/collarL.square(), 20*c5/collarL.square()], -1)
    collar = inspect([CF, CG, CGp], np.array([cuff]), modes, P, 'exact R6 endpoint collar')
    result = {
        'status': 'continuous-outward-rounded-finite-tail-first-jet-certificate',
        'scope': __doc__,
        'manifest': str(Path(args.manifest).resolve()),
        'manifestSHA256': hashlib.sha256(Path(args.manifest).read_bytes()).hexdigest(),
        'scriptSHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'intervalBackendSHA256': hashlib.sha256(backend.read_bytes()).hexdigest(),
        'readerSHA256': hashlib.sha256(Path(__file__).with_name('db6f_tail_integrated.py').read_bytes()).hexdigest(),
        'finite': finite, 'collar': collar,
        'entireTail': {
            'planarDisplacementUpper': max(finite['r0theta0Planar'], collar['r0theta0Planar']),
            'heightDisplacementUpper': max(finite['r0theta0Height'], collar['r0theta0Height']),
            'planarJacobianPositive': finite['positivePlanarJacobian'] and collar['positivePlanarJacobian'],
            'allCrossSectionsSimple': finite['starShapedSimpleCrossSections'] and collar['starShapedSimpleCrossSections'],
            'planarJacobianOverRLower': min(finite['planarRadialJacobianOverRLower'], collar['planarRadialJacobianOverRLower']),
        },
        'notCertified': ['target metric', 'curvature or reach', 'source ODE', 'infinite nonlinear stable graph',
                         'prefix interface', 'actual total volume moment', 'README completion'],
    }
    Path(args.out).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['entireTail']))


if __name__ == '__main__':
    main()

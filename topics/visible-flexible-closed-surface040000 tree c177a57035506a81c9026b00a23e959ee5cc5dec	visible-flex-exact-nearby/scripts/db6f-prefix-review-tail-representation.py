#!/usr/bin/env python3
"""Independent signed-mode/restriction diagnostics for the tail backend."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
path = HERE/'db6f-audit-tail-metric-curvature.py'
spec = importlib.util.spec_from_file_location('tail_repr_review', path)
a = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = a
spec.loader.exec_module(a)


def boxed(q):
    lo = np.empty((len(q), len(q[0])))
    hi = lo.copy()
    for j, row in enumerate(q):
        for k, v in enumerate(row):
            z = a.qbounds(v)
            lo[j, k], hi[j, k] = z.lo, z.hi
    return a.I(lo, hi)


def derivatives(c, L):
    first = [[(j+1)*v/L for v in c[j+1]] for j in range(len(c)-1)]
    second = [[(j+1)*v/L for v in first[j+1]] for j in range(len(first)-1)]
    return [c, first, second]


def polynomial(c, u):
    return np.array([sum(float(c[j][k])*u**j for j in range(len(c))) for k in range(len(c[0]))])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    geom = object.__new__(a.ExactIntegratedTail)
    geom.reader = SimpleNamespace(planar_modes=np.array([-5, -2, 1, 4, 7]), height_modes=np.array([0, 3, 6]))
    geom.P, geom.C, geom.M = 5, 8, 2
    geom.rq, geom.lq = [Q(1, 5), Q(13, 40)], [Q(1, 8)]
    geom.cuff, geom.collar_length = Q(1, 10), Q(1, 10)
    c = [[Q((-1)**(j+k)*(j+1)*(k+2), 2**(12+j+k)) for k in range(geom.C)] for j in range(6)]
    collar = [[Q(0) if j < 3 else Q((-1)**k*(j+1)*(k+1), 2**(14+j+k)) for k in range(geom.C)] for j in range(6)]
    raw = {0: derivatives(c, geom.lq[0]), -1: derivatives(collar, geom.collar_length)}
    geom.polys = [boxed(q)[None, :, :] for q in raw[0]]
    geom.collar = [boxed(q) for q in raw[-1]]
    angular = 32
    trig = a.base.trigonometry(geom.M, angular)
    max_difference, violations, count = 0., 0, 0
    for index in (-1, 0):
        for left, right in [(Q(0), Q(1)), (Q(1, 5), Q(4, 5)), (Q(7, 8), Q(1))]:
            fields = geom.fields(index, left, right)
            radius, ra, rb = geom.interval_radius(index, left, right)
            expected_left = (geom.cuff if index == -1 else geom.rq[0])+(geom.collar_length if index == -1 else geom.lq[0])*left
            assert ra == expected_left and rb > ra
            for order in range(3):
                bounds = a.vector_range(fields[order], trig)
                for u in np.linspace(0, 1, 9):
                    old_u = float(left+(right-left)*Q.from_float(float(u)))
                    coeff = polynomial(raw[index][order], old_u)
                    for sector in range(angular):
                        for offset in (0., .5, 1.):
                            theta = 2*math.pi*(sector+offset)/(3*angular)
                            z = np.sum(coeff[:geom.P]*np.exp(1j*geom.reader.planar_modes*theta))*np.exp(-1j*theta)
                            expected = np.array([z.real, z.imag, np.sum(coeff[geom.P:]*np.cos(geom.reader.height_modes*theta))])
                            observed = []
                            for p in fields[order]:
                                cc = p.c.lo/2+p.c.hi/2
                                radial = np.array([u**j for j in range(cc.shape[0])])@cc
                                modes = np.arange(p.first, p.first+cc.shape[1])
                                observed.append(float(((1j**p.phase)*np.sum(radial*np.exp(3j*modes*theta))).real))
                            max_difference = max(max_difference, float(np.max(np.abs(expected-observed))))
                            violations += int(np.any(expected < bounds.lo[sector]-2e-13) or np.any(expected > bounds.hi[sector]+2e-13))
                            count += 1
    assert violations == 0 and max_difference < 2e-12
    report = dict(status='PASS signed-mode/restriction component diagnostics', scope=__doc__,
                  script_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  reviewer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  cartesian_complex_comparisons=count, max_absolute_difference=max_difference,
                  sampled_interval_violations=violations,
                  not_certified=['supplier packet validity', 'whole physical tail', 'README completion'])
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()

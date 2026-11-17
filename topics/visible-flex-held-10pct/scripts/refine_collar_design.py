#!/usr/bin/env python3
"""Enlarge a collar design space by exact knot insertion and Fourier embedding.

The initial represented surface and its two endpoint jets are preserved.
Subsequent optimization still designs a new angularly independent metric;
this is not fixed-metric refinement or an existence certificate.
Chunked sparse analytic Jacobians avoid a dense least-squares factorization.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import json
import time
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix, vstack
from general_analytic_collar_design import GeneralCollar


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--trace', type=Path, required=True)
    p.add_argument('--seed', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--subdivide', type=int, default=2)
    p.add_argument('--m', type=int, default=12)
    p.add_argument('--G-floor', type=float, default=.0005)
    p.add_argument('--chunk', type=int, default=2)
    p.add_argument('--nfev', type=int, default=100)
    p.add_argument('--lsmr-maxiter', type=int, default=500)
    a = p.parse_args()
    if a.subdivide < 1 or a.chunk < 1:
        p.error('subdivide and chunk must be positive')
    seed = json.loads(a.seed.read_text())
    oldp = seed['parameters']
    names = ('rise', 'radius', 'nc', 'm', 'bend', 'degree', 'r0',
             'slope', 'slope_r', 'curvature_limit')
    oldparams = {k: oldp[k] for k in names if k in oldp}
    trace = dict(np.load(a.trace))
    old = GeneralCollar(trace, **oldparams)
    if old.degree != 5:
        p.error('this exact embedding currently requires the quintic basis')
    if a.m < old.m:
        p.error('the new Fourier space must contain the old one')
    coeff = np.zeros((old.nc, 3*old.m))
    coeff[3:-3] = np.array(seed['q']).reshape(old.shape)
    spl = BSpline(old.spline.t, coeff, old.degree)
    for lo, hi in zip(old.intervals[:-1], old.intervals[1:]):
        for j in range(1, a.subdivide):
            spl = spl.insert_knot(lo + (hi-lo)*j/a.subdivide)
    new_nc = len(spl.t)-old.degree-1
    newparams = {**oldparams, 'nc': new_nc, 'm': a.m}
    obj = GeneralCollar(trace, **newparams)
    obj.G_floor = a.G_floor
    if np.max(abs(obj.spline.t-spl.t)) > 1e-14:
        raise ValueError('knot insertion and the target knot sequence disagree')
    q = np.zeros(obj.shape)
    for component in range(3):
        q[:, component*a.m:component*a.m+old.m] = \
            spl.c[3:new_nc-3, component*old.m:(component+1)*old.m]
    q = q.ravel()
    check_s = np.r_[0., .071, .177, .411, .653, .879, 1.]
    check_u = np.arange(48)*2*np.pi/48
    before = old.geometry(np.array(seed['q']), old.prepare(check_s, check_u), True)
    after = obj.geometry(q, obj.prepare(check_s, check_u), True)
    embedding_errors = [float(np.max(abs(x-y))) for x, y in zip(before, after)]
    if max(embedding_errors) > 1e-8:
        raise ValueError('the warm start did not preserve the represented two-jet')
    nodes, _ = np.polynomial.legendre.leggauss(7)
    s = np.concatenate([lo+(hi-lo)*(1+nodes)/2
                        for lo, hi in zip(obj.intervals[:-1], obj.intervals[1:])])
    nu = max(96, 12*a.m)
    u = np.arange(nu)*2*np.pi/nu
    grids = [obj.prepare(s[i:i+a.chunk], u) for i in range(0, len(s), a.chunk)]
    common = dict(parameters={**newparams, 'trace': str(a.trace),
                              'G_floor': a.G_floor},
                  refinement_arguments={k: str(v) if isinstance(v, Path) else v
                                        for k, v in vars(a).items()},
                  trace_sha256=hashlib.sha256(a.trace.read_bytes()).hexdigest(),
                  seed_sha256=hashlib.sha256(a.seed.read_bytes()).hexdigest(),
                  embedding_errors=embedding_errors,
                  optimization_grid=[len(s), nu])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    count = 0
    best = np.inf

    def fun(v):
        nonlocal count, best
        count += 1
        r = np.concatenate([obj.residual(v, g) for g in grids])
        norm = float(np.dot(r, r))
        if norm < best:
            best = norm
            if count % 10 == 1:
                warm = {**common, 'provisional': True, 'q': v.tolist(),
                        'eval': count, 'squared_residual_norm': norm}
                a.out.with_suffix('.warm.json').write_text(json.dumps(warm)+'\n')
        if count % 5 == 1:
            print(json.dumps(dict(eval=count, rms=float(np.sqrt(np.mean(r*r))),
                                  maximum=float(abs(r).max()),
                                  seconds=time.monotonic()-start)), flush=True)
        return r

    def jac(v):
        return vstack([csr_matrix(obj.residual(v, g, True)) for g in grids],
                      format='csr')

    res = least_squares(fun, q, jac=jac, method='trf', tr_solver='lsmr',
                        tr_options=dict(atol=1e-8, btol=1e-8,
                                        maxiter=a.lsmr_maxiter),
                        max_nfev=a.nfev, ftol=1e-11, xtol=1e-11,
                        gtol=1e-11, x_scale='jac')
    result = dict(**common, q=res.x.tolist(), success=bool(res.success),
                  message=res.message, nfev=res.nfev, njev=res.njev,
                  cost=res.cost, seconds=time.monotonic()-start,
                  audit=obj.audit(res.x, 601, max(384, 24*a.m)))
    a.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'q'}), flush=True)


if __name__ == '__main__':
    main()

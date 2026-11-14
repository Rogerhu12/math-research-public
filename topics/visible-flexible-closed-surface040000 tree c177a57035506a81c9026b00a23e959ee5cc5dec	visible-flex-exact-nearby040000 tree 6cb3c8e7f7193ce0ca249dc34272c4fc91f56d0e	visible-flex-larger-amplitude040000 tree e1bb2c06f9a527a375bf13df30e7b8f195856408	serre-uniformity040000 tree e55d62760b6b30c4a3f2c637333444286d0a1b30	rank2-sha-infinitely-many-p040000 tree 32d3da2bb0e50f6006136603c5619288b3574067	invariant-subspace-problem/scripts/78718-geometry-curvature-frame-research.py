#!/usr/bin/env python3
"""Small own-map interval comparison of principal-curvature bounds.

No source BVP, tail shooting, or ODE is called.  Each reported bound covers
the indicated whole radial span and angular arcs of the actual saved map.
Only the selected spans are covered; no global geometry claim is made.
"""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def midpoint(x):
    return x.lo+(x.hi-x.lo)/2


def nominal_data(v):
    Xs, Xp, Xss, Xsp, Xpp = map(midpoint, v)
    E = np.sum(Xs*Xs, axis=-1)
    F = np.sum(Xs*Xp, axis=-1)
    G = np.sum(Xp*Xp, axis=-1)
    a = 1/np.sqrt(E)
    c = 1/np.sqrt(G-F*F/E)
    b = -F/E*c
    V1, V2 = a[..., None]*Xs, b[..., None]*Xs+c[..., None]*Xp
    H11 = a[..., None]**2*Xss
    H12 = a[..., None]*(b[..., None]*Xss+c[..., None]*Xsp)
    H22 = b[..., None]**2*Xss+2*(b*c)[..., None]*Xsp+c[..., None]**2*Xpp
    gram = np.stack((np.stack((np.sum(V1*V1, -1), np.sum(V1*V2, -1)), -1),
                     np.stack((np.sum(V1*V2, -1), np.sum(V2*V2, -1)), -1)), -2)
    gammas = []
    for H in (H11, H12, H22):
        rhs = np.stack((np.sum(V1*H, -1), np.sum(V2*H, -1)), -1)
        gammas.append(np.linalg.solve(gram, rhs[..., None])[..., 0])
    # All these numbers are used only as exact, freely chosen binary64
    # frame/tangential-subtraction constants.  Their approximation error
    # requires no assumption: the interval Gram bound is recomputed below.
    return a, b, c, gammas


def frame_curvature(mod, v, nominal):
    I, dot = mod.I, mod.dot
    def sqrt_nonnegative(z):
        # Each use is a sum of squares.  Roundoff may put its interval's
        # lower endpoint one subnormal below zero; intersect with [0,inf).
        return I(np.maximum(0,z.lo),np.maximum(0,z.hi)).sqrt()
    def norm(z):
        return sqrt_nonnegative(z[...,0].square()+z[...,1].square()+z[...,2].square())
    Xs, Xp, Xss, Xsp, Xpp = v
    aa, bb, cc, gammas = nominal
    a, b, c = (I(z[..., None]) for z in (aa, bb, cc))
    V1, V2 = a*Xs, b*Xs+c*Xp
    e, f, g = dot(V1,V1)-1, dot(V1,V2), dot(V2,V2)-1
    delta = ((e+g).abs()+sqrt_nonnegative((e-g).square()+4*f.square()))/2
    denominator = 1-delta
    H = [a.square()*Xss, a*(b*Xss+c*Xsp),
         b.square()*Xss+2*b*c*Xsp+c.square()*Xpp]
    for j, gamma in enumerate(gammas):
        H[j] = H[j]-I(gamma[..., 0, None])*V1-I(gamma[..., 1, None])*V2
    numerator = norm(H[0]+H[2])+sqrt_nonnegative(norm(H[0]-H[2]).square()+4*norm(H[1]).square())
    if np.any(denominator.lo <= 0):
        return dict(resolved=False, gram_defect_upper=float(delta.hi.max()))
    curvature = numerator/(2*denominator)
    return dict(resolved=True, gram_defect_upper=float(delta.hi.max()),
                curvature_upper=float(curvature.hi.max()))


def original_curvature(mod, v):
    Xs, Xp, Xss, Xsp, Xpp = v
    area = mod.cross(Xp, Xs)
    length = mod.norm(area)
    if np.any(length.lo <= 0):
        return dict(resolved=False, area_lower=float(length.lo.min()))
    normal = area/length[..., None]
    E, F, G = mod.dot(Xs,Xs), mod.dot(Xs,Xp), mod.dot(Xp,Xp)
    L, M, N = mod.dot(Xss,normal), mod.dot(Xsp,normal), mod.dot(Xpp,normal)
    det = length.square()
    tr = (L*G-2*M*F+N*E)/det
    gauss = (L*N-M.square())/det
    discr = tr.square()-4*gauss
    discr = mod.I(np.maximum(0,discr.lo), np.maximum(0,discr.hi))
    curvature = (tr.abs()+discr.sqrt())/2
    return dict(resolved=True, area_lower=float(length.lo.min()),
                curvature_upper=float(curvature.hi.max()))


def jets(mod, ranges, cos, sin, M):
    _, Xp, Xpp = mod.cylindrical(ranges[0], cos, sin, M)
    Xs, Xsp, _ = mod.cylindrical(ranges[1], cos, sin, M)
    Xss, _, _ = mod.cylindrical(ranges[2], cos, sin, M)
    return Xs, Xp, Xss, Xsp, Xpp


def run(args):
    started = time.monotonic()
    mod = load('geometry_frame_intervals', HERE/'78718-prefix-continuous-hermite-storage-v1.py')
    meta = json.loads(args.geometry.read_text())
    if meta.get('representation') == 'exact-common-cut-prefix':
        common = load('geometry_frame_common', HERE/'78718-prefix-common-cut-storage-v1.py')
        common.install(mod)
    geom = mod.ExactHermite(args.geometry)
    indices = [int(z) for z in args.spans.split(',')]
    if any(j < 0 or j >= len(geom.x)-1 for j in indices):
        raise ValueError('Selected span is outside the actual saved mesh')
    part = copy.copy(geom)
    part.power = mod.I(geom.power.lo[indices], geom.power.hi[indices])
    part.h = mod.I(geom.h.lo[indices], geom.h.hi[indices])
    full = [part.ranges(d) for d in range(3)]
    center = [part.ranges(d,Q(1,2),Q(1,2)) for d in range(3)]
    rows = []
    for angular in [int(z) for z in args.angular.split(',')]:
        clock = time.monotonic()
        cos, sin = mod.trigonometry(geom.M, angular)
        pc = np.empty((geom.M, angular, 2)); ps = np.empty_like(pc)
        for j in range(1, geom.M+1):
            for k in range(angular):
                q = Q(j*(2*k+1), angular)
                pc[j-1,k] = mod.trig_point(q, True)
                ps[j-1,k] = mod.trig_point(q, False)
        ci, si = mod.I(pc[...,0],pc[...,1]), mod.I(ps[...,0],ps[...,1])
        values = jets(mod, full, cos, sin, geom.M)
        centers = jets(mod, center, ci, si, geom.M)
        nominal = nominal_data(centers)
        for k, span in enumerate(indices):
            row = dict(span=span, radial_interval=[float(geom.x[span]),float(geom.x[span+1])],
                       angular_intervals_per_threefold_period=angular)
            vv = tuple(x[k:k+1] for x in values)
            nom = tuple(x[k:k+1] for x in nominal[:3]) + ([x[k:k+1] for x in nominal[3]],)
            row['original'] = original_curvature(mod, vv)
            row['fixed_frame'] = frame_curvature(mod, vv, nom)
            rows.append(row)
        print(json.dumps(dict(angular=angular,spans=indices,
                              original_max=max((r['original'].get('curvature_upper',0.) for r in rows[-len(indices):])),
                              frame_max=max((r['fixed_frame'].get('curvature_upper',0.) for r in rows[-len(indices):])),
                              seconds=time.monotonic()-clock)), flush=True)
    report = dict(scope=__doc__, geometry=str(args.geometry), geometry_sha256=sha(args.geometry),
                  script_sha256=sha(__file__), interval_source_sha256=sha(mod.__file__),
                  modes=geom.M, selected_spans=indices, whole_prefix_covered=False,
                  rows=rows, seconds=time.monotonic()-started,
                  interpretation='Every resolved bound is outward rounded on its own complete selected span. '
                                 'Midpoint frame and tangential subtraction are arbitrary exact binary constants. '
                                 'No assertion is made for unselected spans, closed geometry, or reach.')
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True)
    p.add_argument('--spans',default='0,600,2500,4000,6124,6500')
    p.add_argument('--angular',default='64,128,256')
    p.add_argument('--out',type=Path,required=True)
    run(p.parse_args())

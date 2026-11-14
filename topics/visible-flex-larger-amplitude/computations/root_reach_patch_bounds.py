#!/usr/bin/env python3
"""Exact rational lower bounds for certified surface patch enclosures (R16).

This module does not certify the input position/normal radii. It does not
infer a continuous surface or reach from a mesh. All rational inequalities
and outward square roots below are exact for the supplied numeric inputs.
"""
from fractions import Fraction as F
from math import isqrt
import argparse
import json
from pathlib import Path


def q(x):
    return x if isinstance(x, F) else F(x)


def dot(a, b):
    return sum((q(x) * q(y) for x, y in zip(a, b)), F(0))


def sqrt_upper(x, bits=96):
    x = q(x)
    if x < 0:
        raise ValueError('Square root of a negative bound')
    if not x:
        return F(0)
    return F(isqrt((x.numerator << (2*bits)) // x.denominator) + 1, 1 << bits)


def static_margin(p, n, ep, vp, target, m, eq, vq, tau):
    ep, vp, eq, vq, tau = map(q, (ep, vp, eq, vq, tau))
    if min(ep, vp, eq, vq) < 0 or tau <= 0:
        raise ValueError('Nonnegative error radii and positive reach required')
    d = [q(b)-q(a) for a, b in zip(p, target)]
    d2 = dot(d, d)
    du = sqrt_upper(d2)
    error = ep + eq
    normal = max(abs(dot(n, d)) + vp*du + error,
                 abs(dot(m, d)) + vq*du + error)
    return d2 - 2*du*error - 2*tau*normal


def phase_margins(p, n, ep, vp, target, m, eq, vq, tau):
    ep, vp, eq, vq, tau = map(q, (ep, vp, eq, vq, tau))
    if min(ep, vp, eq, vq) < 0 or tau <= 0:
        raise ValueError('Nonnegative error radii and positive reach required')
    p, n, target, m = [[q(v) for v in z] for z in (p, n, target, m)]
    x, y = p[:2], target[:2]
    a, b = n[:2], m[:2]
    jx, ja = [-x[1], x[0]], [-a[1], a[0]]
    dz = target[2]-p[2]
    A, B, C = dot(x, x)+dot(y, y)+dz*dz, dot(y, x), dot(y, jx)
    dmax = sqrt_upper(A+2*sqrt_upper(B*B+C*C))
    error = ep+eq
    rows = [(dz*n[2]-dot(x, a), dot(y, a), dot(y, ja), vp),
            (dot(y, b)+dz*m[2], -dot(x, b), -dot(jx, b), vq)]
    bounds = []
    for d0, dc, ds, normal_error in rows:
        for sign in (-1, 1):
            center = A-2*tau*sign*d0-2*sqrt_upper((B+tau*sign*dc)**2+(C+tau*sign*ds)**2)
            bounds.append(center-2*dmax*error-2*tau*(normal_error*dmax+error))
    return bounds


def display(value):
    return dict(exact_lower=str(value), decimal_lower=float(value), nonnegative=value >= 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    example = static_margin([1, 0, 0], [1, 0, 0], F(1, 100), F(1, 100),
                            [-1, 0, 0], [-1, 0, 0], F(1, 100), F(1, 100), F(9, 10))
    phase = phase_margins([2, 0, 0], [1, 0, 0], F(1, 1000), F(1, 1000),
                          [0, 0, 4], [0, 0, 1], F(1, 1000), F(1, 1000), F(1, 10))
    result = dict(scope=__doc__, static_example=display(example),
                  all_phase_example=[display(v) for v in phase],
                  current_surface_certified=False,
                  missing='Certified continuous position/normal enclosures, curvature/path bounds and a closed embedded surface.')
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out), static_pass=example >= 0,
                          phase_pass=all(v >= 0 for v in phase), current_surface_certified=False)))


if __name__ == '__main__':
    main()

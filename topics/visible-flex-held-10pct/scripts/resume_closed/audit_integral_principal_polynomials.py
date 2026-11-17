#!/usr/bin/env python3
"""Exact interface audit of the R39 principal compiler, without metric boxes.

Selected center/lift/short-span locations compare two exact rational
evaluations.  A single finite Gram-polynomial evaluation checks the R31
consumer with a declared auxiliary radius 1; it is not a physical metric
estimate.  No original map, parameter, source checkpoint or BVP is changed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

from integral_principal_polynomials import IntegralPrincipalCompiler, HERMITE, ff, sha
from certify_integral_remainder_budget import quintic


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
II = (F(0), F(1))


def ca(x, y): return x[0]+y[0], x[1]+y[1]
def cm(x, y): return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]
def cs(x, a): return x[0]*a, x[1]*a
def cn(x): return -x[0], -x[1]
def cp(x, k):
    assert x[0]*x[0]+x[1]*x[1] == 1
    if k < 0: return cp((x[0], -x[1]), -k)
    out = ONE
    while k:
        if k % 2: out = cm(out, x)
        x, k = cm(x, x), k//2
    return out


def integer_i(k): return (ONE, II, cn(ONE), cn(II))[k % 4]


def pv(coefficients, t, order=0, scale=F(1)):
    return sum((value*F(math.factorial(j), math.factorial(j-order))*t**(j-order)/scale**order
                for j, value in enumerate(coefficients) if j >= order), F(0))


def laurent(coefficients, z, order=0):
    result = ZERO
    for k, value in coefficients.items():
        result = ca(result, cs(cm(cp(z, int(k)), integer_i(order)), value*int(k)**order))
    return result


def tensor(xy_coefficients, height_coefficients, z, order=0):
    xy = laurent(xy_coefficients, z, order)
    height = sum((value*cm(cp(z, int(k)), integer_i(order))[0]*int(k)**order
                  for k, value in height_coefficients.items()), F(0))
    return xy[0], xy[1], height


def source_projection(c, z, order):
    """Independent cylindrical formula, including rotating-basis derivatives."""
    raw = [ff(v) for v in c.data['reference_initial_projection']]
    M = (len(raw)-1)//3
    r, tangent, height = [], [], []
    for d in range(order+1):
        rr, tt, zz = raw[0] if d == 0 else F(0), F(0), F(0)
        for j in range(1, M+1):
            unit = cm(cp(z, 3*j), integer_i(d))
            factor = (3*j)**d
            rr += raw[j]*unit[0]*factor
            tt += raw[M+j]*unit[1]*factor
            zz += raw[2*M+j]*unit[0]*factor
        r.append(rr); tangent.append(tt); height.append(zz)
    xy = ZERO
    for d in range(order+1):
        xy = ca(xy, cs(cm(integer_i(order-d), (r[d], tangent[d])), math.comb(order, d)))
    xy = cm(z, xy)
    return xy[0], xy[1], height[order]


def circle_by_exponential(c, z, order):
    """Derivative of the finite exponential, independent of Laurent expansion."""
    z3 = cp(z, 3)
    v = (F(0), -c.er*z3[1]/3)
    vp = (F(0), -c.er*z3[0])
    vpp = (F(0), 3*c.er*z3[1])
    sums = [ZERO, ZERO, ZERO]
    term = ONE
    for r in range(c.circle_degree+1):
        if r: term = cs(cm(term, v), F(1, r))
        for d in range(3):
            if r <= c.circle_degree-d:
                sums[d] = ca(sums[d], term)
    if order == 0: value = sums[0]
    elif order == 1: value = ca(cm(II, sums[0]), cm(vp, sums[1]))
    else:
        value = ca(cn(sums[0]), ca(cs(cm(II, cm(vp, sums[1])), 2),
                   ca(cm(vpp, sums[1]), cm(cm(vp, vp), sums[2]))))
    value = cm(z, value)
    return value[0], value[1], F(0)


def direct_factor_value(c, index, t, z, radial, angular):
    h = ff(c.knots[index+1])-ff(c.knots[index])
    s = ff(c.knots[index])+h*t
    old = []
    for k in range(len(c.old_pm)+len(c.old_hm)):
        coefficients, _ = quintic(c.knots[index], c.knots[index+1], c.data['jets'][:, k, index:index+2])
        old.append(pv(coefficients, t, radial, h))
    C = tensor(dict(zip(map(int, c.old_pm), old[:c.old_P])),
               dict(zip(map(int, c.old_hm), old[c.old_P:])), z, angular)
    G = laurent(c.G, z, angular); G = (*G, F(0))
    E, V = circle_by_exponential(c, z, angular), source_projection(c, z, angular)
    f, _ = quintic(c.knots[index], c.knots[index+1], c.data['reference_radial_jets'][:, 0, index:index+2])
    fr = pv(f, t, radial, h)
    centers = [tensor(dict(zip(map(int, c.old_pm), map(ff, c.data['jets'][j, :c.old_P, 0]))),
                      dict(zip(map(int, c.old_hm), map(ff, c.data['jets'][j, c.old_P:, 0]))), z, angular)
               for j in range(3)]
    bT = ZERO
    z3 = cp(z, 3)
    for j in range(angular+1):
        b = -c.epp/3*cm(z3, integer_i(j))[1]*3**j
        tangent = cm(II, laurent(c.T_imag, z, angular-j))
        bT = ca(bT, cs(tangent, math.comb(angular, j)*b))
    target = [tuple(E[k]+c.q_gauge*V[k]-centers[0][k] for k in range(3)),
              tuple(F(k == 2 and angular == 0)-centers[1][k] for k in range(3)),
              (bT[0]-centers[2][0], bT[1]-centers[2][1], -centers[2][2])]
    weights = [pv(HERMITE[j], s/c.width, radial)*c.width**(j-radial) if s <= c.width else F(0)
               for j in range(3)]
    return tuple(C[k]+fr*(G[k]-E[k]-c.q_gauge*V[k])+sum(weights[j]*target[j][k] for j in range(3))
                 for k in range(3))


def compiled_value(c, rows, h, t, z, radial, angular):
    coefficients = [pv([row[k] for row in rows], t, radial, h) for k in range(c.C)]
    return tensor(dict(zip(map(int, c.planar_modes), coefficients[:c.P])),
                  dict(zip(map(int, c.height_modes), coefficients[c.P:])), z, angular)


def evaluate_real_numerator(box, t, z, imaginary=False):
    lo, hi = F(0), F(0)
    K = box[0].shape[1]//2
    for degree in range(box[0].shape[0]):
        for j in range(box[0].shape[1]):
            unit = cp(z, 3*(j-K))
            weight = t**degree*(-unit[1] if imaginary else unit[0])
            a, b = ff(box[0][degree, j])*weight, ff(box[1][degree, j])*weight
            lo += min(a, b); hi += max(a, b)
    return lo, hi


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('data', 'prefix-audit', 'checkpoint', 'angular-certificate', 'principal', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    args = p.parse_args()
    began = time.monotonic()
    c = IntegralPrincipalCompiler(args.data, args.prefix_audit, args.checkpoint,
                                  args.angular_certificate, args.principal)
    shortest = int(np.argmin(np.diff(c.knots)))
    center_knot = int(np.flatnonzero(c.knots == float(c.width))[0])
    indices = {0, len(c.knots)-2, shortest, max(0, shortest-1), min(len(c.knots)-2, shortest+1),
               center_knot-1, center_knot}
    for s in c.audit['definition']['radial_lift_window']:
        k = int(np.searchsorted(c.knots, s))
        indices |= {max(0, k-1), min(len(c.knots)-2, k)}
    selected = sorted(indices)
    # A rational point on the unit circle avoids all evaluation/libm error.
    z, t = (F(3, 5), F(4, 5)), F(2, 5)
    pairs = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 1))
    compared = 0
    for index in selected:
        rows, h = c.span_exact(index)
        for radial, angular in pairs:
            left = compiled_value(c, rows, h, t, z, radial, angular)
            right = direct_factor_value(c, index, t, z, radial, angular)
            assert left == right, (index, radial, angular)
            compared += 3
    # Literal C2 identity at the newly spliced center-width endpoint.
    left, hl = c.span_exact(center_knot-1)
    right, hr = c.span_exact(center_knot)
    for order in range(3):
        for k in range(c.C):
            assert pv([r[k] for r in left], F(1), order, hl) == pv([r[k] for r in right], F(0), order, hr)
    # One exact rational point checks all three complete R31 finite
    # convolution outputs.  Radius one is explicitly only a consumer probe.
    formal_radius = (np.zeros((6, 1)), np.zeros((6, 1)))
    formal_radius[0][0, 0] = formal_radius[1][0, 0] = 1.
    numerators, info = c.metric_numerators(0, formal_radius)
    t, z = F(1, 2), II
    rows, h = c.span_exact(0)
    Xs, Xp = (compiled_value(c, rows, h, t, z, *pair) for pair in ((1, 0), (0, 1)))
    e, _ = quintic(c.knots[0], c.knots[1], c.data['phase_jets'][:, 0, :2])
    rho = 1-pv(e, t)*cp(z, 3)[0]
    theta_s = -pv(e, t, 1, h)*cp(z, 3)[1]/3
    Y = tuple(rho*u-theta_s*v for u, v in zip(Xs, Xp))
    exact = (sum(v*v for v in Y)-rho*rho, sum(u*v for u, v in zip(Y, Xp)),
             sum(v*v for v in Xp)-rho*rho)
    widths = []
    for j, (box, value) in enumerate(zip(numerators, exact)):
        lo, hi = evaluate_real_numerator(box, t, z, imaginary=(j == 1))
        assert lo <= value <= hi, j
        widths.append(float(hi-lo))
    here = Path(__file__).resolve().parent
    sources = [Path(__file__), here/'integral_principal_polynomials.py',
               here/'certify_integral_remainder_budget.py', here/'interval_prefix_metric.py',
               here/'interval_tail_metric.py',
               here.parent/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py']
    result = dict(scope=__doc__, command=sys.argv, compiler=c.report(),
        source_sha256={str(p.resolve()): sha(p) for p in sources},
        exact_factor_comparison=dict(selected_span_count=len(selected), selected_span_indices=selected,
            rational_angular_point=['3/5', '4/5'], local_radial_fraction='2/5',
            radial_angular_jet_pairs=[list(pair) for pair in pairs],
            scalar_equalities=compared, every_difference_exactly_zero=True),
        center_width_common_C2_identity=dict(coefficient_equalities=3*c.C, all_exact=True),
        R31_consumer_probe=dict(single_span=0, local_radial_fraction='1/2', angular_point=['0', '1'],
            auxiliary_radius='1 (formal interface probe only, not the physical reference)',
            complete_exact_A_B_C_values_enclosed=True, outward_interval_widths_display_only=widths,
            **info),
        shortest_source_span=dict(index=shortest, width=str(ff(c.knots[shortest+1])-ff(c.knots[shortest]))),
        full_domain_metric_boxes=0, principal_metric_certificate=False, bvp_solves=0,
        seconds=time.monotonic()-began)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('exact_factor_comparison',
          'center_width_common_C2_identity', 'R31_consumer_probe', 'shortest_source_span', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()

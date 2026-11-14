#!/usr/bin/env python3
"""Continuous Fz/x and area gates for the explicitly symmetric R33 graph.

Only spline convex hulls and elementary outward arithmetic are used. No
angular sampling or finite primitive is needed for these particular gates.
The inputs are the same frozen physical coefficients used by the root proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_root_interval import Box
from fourfold_phase_uniform_tail import (
    local_hulls, derivative_coefficients, weighted_phase_bounds,
    weighted_sum_up, up, down, add_up, mul_up,
)


def coefficient_core_bounds(knots, degree, coefficients, radius, order=2):
    """Ranges of an exact even coefficient combination and its derivatives."""
    t, k = knots, degree
    low, high = coefficients.lo, coefficients.hi
    result = []
    for j in range(order+1):
        count = len(t)-k-1
        active = (t[:count] <= radius)&(t[k+1:k+1+count] >= -radius)
        result.append([float(low[:count][active].min()), float(high[:count][active].max())])
        if j < order:
            t, k, low, high = derivative_coefficients(t, k, low, high)
    return np.array(result)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--core', type=float, default=.25)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    with np.load(args.inputs, allow_pickle=False) as saved:
        f = {key: saved[key].copy() for key in saved.files}
    alpha = f['alpha']
    t, k = f['base_knots'], int(f['base_degree'])
    if not np.array_equal(t, -t[::-1]):
        raise ValueError('this scalar coefficient average requires exactly reflected mean knots')
    acoeff = Box(f['base_radius_coefficients'])
    for j, parameter in enumerate(alpha):
        if not np.array_equal(t, f[f'mean{j}_knots']):
            raise ValueError('mean knot vectors differ')
        acoeff = acoeff+parameter*Box(f[f'mean{j}_radius_coefficients'])
    if not np.array_equal(t, f['shift_knots']):
        raise ValueError('shift knot vector differs')
    acoeff = acoeff+Box(f['shift_coefficients'])
    acoeff = (acoeff+acoeff[::-1])*.5
    arange = coefficient_core_bounds(t, k, acoeff, args.core)
    ab = np.maximum(abs(arange[:, 0]), abs(arange[:, 1]))
    zt, zk = f['height0_slope_knots'], int(f['height0_slope_degree'])
    if not np.array_equal(zt, -zt[::-1]):
        raise ValueError('height knots are not exactly reflected')
    zcoeff = Box(f['height0_slope_coefficients'])
    for j, parameter in enumerate(alpha, 1):
        if not np.array_equal(zt, f[f'height{j}_slope_knots']):
            raise ValueError('height mean knots differ')
        zcoeff = zcoeff+parameter*Box(f[f'height{j}_slope_coefficients'])
    zcoeff = (zcoeff+zcoeff[::-1])*.5
    zrange = coefficient_core_bounds(zt, zk, zcoeff, args.core, order=1)
    cuts = np.unique(np.r_[-args.core, args.core, f['phase_knots'], t])
    cuts = cuts[(cuts >= -args.core)&(cuts <= args.core)]
    raw = local_hulls(f['phase_knots'], 5, f['phase_coefficients'], cuts[:-1], derivatives=2)
    base = local_hulls(t, k, f['base_radius_coefficients'], cuts[:-1], derivatives=2)
    phase = [weighted_phase_bounds(raw[..., c], base, p) for c, p in enumerate((3, 2))]
    phase_sums = []
    for values in phase:
        # Explicit averaging with x->-x cannot increase these global
        # per-mode derivative bounds on the symmetric radial interval.
        maxima = values.max(axis=1)
        phase_sums.append(weighted_sum_up(maxima, np.ones(maxima.shape[-1])))
    b, g = phase_sums
    pvertical, pvector = up(11/28), up(11/7)
    zmin, zmax = zrange[0]
    qloss = mul_up(pvertical, mul_up(ab[0], g[1]))
    quotient_lower = float(down(zmin-qloss))
    vertical_loss = mul_up(pvertical, add_up(mul_up(ab[1], g[0]), mul_up(ab[0], g[1])))
    vz_lower, vz_upper = float(down(zmin-vertical_loss)), float(up(zmax+vertical_loss))
    horizontal_upper = mul_up(pvector, add_up(ab[1], mul_up(ab[0], add_up(b[1], mul_up(g[0], g[1])))))
    horizontal_tangent_lower = float(down(1-mul_up(.5, mul_up(g[0], g[0]))))
    if vz_lower <= 0 or horizontal_tangent_lower <= 0:
        raise ValueError('positive factors needed for the transverse lower estimate')
    transverse_lower = float(down(down(vz_lower*horizontal_tangent_lower)
                                  -mul_up(g[0], horizontal_upper)))
    area_lower = float(down(arange[0, 0]*transverse_lower))
    area_upper = float(mul_up(ab[0], add_up(horizontal_upper, vz_upper)))
    zsecond = max(abs(zrange[1]))
    vertical_second = add_up(zsecond, mul_up(pvertical,
        add_up(add_up(mul_up(ab[2], g[0]), mul_up(2, mul_up(ab[1], g[1]))),
               mul_up(ab[0], add_up(g[2], mul_up(g[1], g[1]))))))
    report = dict(kind='continuous_scalar_and_area_gates_for_explicitly_symmetric_infinite_R33_graph',
        inputs=str(args.inputs), inputs_sha256=hashlib.sha256(args.inputs.read_bytes()).hexdigest(),
        source_checkpoint_sha256=json.loads(str(f['metadata']))['checkpoint_sha256'],
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
        radial_core=[-args.core,args.core], radial_cells=len(cuts)-1,
        circumference_radius_derivative_ranges=arange.tolist(), exact_height_slope_ranges=zrange.tolist(),
        beta_field_absolute_derivative_bounds=b.tolist(), gamma_field_absolute_derivative_bounds=g.tolist(),
        vertical_primitive_operator_bound=float(pvertical), full_vector_primitive_operator_bound=float(pvector),
        Fz_over_x_lower=quotient_lower, Fx_vertical_lower=vz_lower, Fx_vertical_upper=vz_upper,
        Fx_horizontal_norm_upper=float(horizontal_upper), tangent_horizontal_norm_lower=horizontal_tangent_lower,
        T_cross_Fx_norm_lower=transverse_lower, area_lower=area_lower, area_upper=area_upper,
        quotient_radial_Lipschitz_upper=float(mul_up(.5,vertical_second)),
        quotient_angular_Lipschitz_upper=float(mul_up(ab[0],g[1])),
        gate_passed=bool(quotient_lower>0 and vz_lower>0 and transverse_lower>0 and area_lower>0),
        exact_object='physical a,beta even and gamma,Z odd by explicit averaging; Z is the exact slope integral; no Gaussian smoothing',
        limitations=['No claim that N is negative or support zeta is positive from these gates alone',
                     'No angular sample is used as a proof bound; these conservative inequalities use full spline convex hulls',
                     'Only the stated core is covered; the original saved finite candidate and the new symmetric real object remain distinguished'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)
    if not report['gate_passed']:
        raise SystemExit('scalar gate failed; inspect the recorded conservative bounds')


if __name__=='__main__':
    main()

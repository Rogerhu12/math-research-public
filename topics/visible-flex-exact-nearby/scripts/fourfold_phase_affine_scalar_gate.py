#!/usr/bin/env python3
"""Uniform real Fz/r and scalar gates for the exact affine R57 family.

No DFT or angular samples are used. The original and direction raw spline
derivatives are bounded separately, then combined with max|delta| before
the unchanged physical weights and explicit parity operation. Height and
radius mean coefficients use the same exact affine alpha direction.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_core_scalar_gate import coefficient_core_bounds
from fourfold_phase_root_interval import Box
from fourfold_phase_uniform_tail import (
    local_hulls, weighted_phase_bounds, weighted_sum_up,
    up, down, add_up, mul_up,
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--frozen-direction', type=Path, required=True)
    ap.add_argument('--parameter-left', type=float, default=-.01)
    ap.add_argument('--parameter-right', type=float, default=.01)
    ap.add_argument('--core', type=float, default=.24)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if not 0 < args.core < 1 or args.parameter_left > args.parameter_right:
        raise ValueError('invalid real core or parameter interval')
    with np.load(args.inputs, allow_pickle=False) as stored:
        f = {key: stored[key].copy() for key in stored.files}
    with np.load(args.frozen_direction, allow_pickle=False) as stored:
        direction = {key: stored[key].copy() for key in stored.files}
    origin_sha, direction_sha = digest(args.inputs), digest(args.frozen_direction)
    metadata = json.loads(str(direction['metadata']))
    if metadata['origin_inputs_sha256'] != origin_sha:
        raise ValueError('affine direction uses a different origin')
    if (direction['phase_direction_coefficients'].shape != f['phase_coefficients'].shape
            or direction['alpha_direction'].shape != f['alpha'].shape):
        raise ValueError('affine direction dimensions differ')
    parameter = [args.parameter_left, args.parameter_right]
    delta = Box(*parameter)
    delta_abs = max(abs(v) for v in parameter)
    alpha = [Box(a)+delta*d for a, d in zip(f['alpha'], direction['alpha_direction'])]

    t, k = f['base_knots'], int(f['base_degree'])
    if not np.array_equal(t, -t[::-1]):
        raise ValueError('mean knot vector must be exactly reflected')
    acoeff = Box(f['base_radius_coefficients'])
    for j, value in enumerate(alpha):
        if not np.array_equal(t, f[f'mean{j}_knots']) or k != int(f[f'mean{j}_degree']):
            raise ValueError('mean knot vectors or degrees differ')
        acoeff = acoeff+value*Box(f[f'mean{j}_radius_coefficients'])
    if not np.array_equal(t, f['shift_knots']) or k != int(f['shift_degree']):
        raise ValueError('shift knot vector or degree differs')
    acoeff = acoeff+Box(f['shift_coefficients'])
    acoeff = (acoeff+acoeff[::-1])*.5
    arange = coefficient_core_bounds(t, k, acoeff, args.core)
    ab = np.maximum(abs(arange[:, 0]), abs(arange[:, 1]))

    zt, zk = f['height0_slope_knots'], int(f['height0_slope_degree'])
    if not np.array_equal(zt, -zt[::-1]):
        raise ValueError('height slope knot vector must be exactly reflected')
    zcoeff = Box(f['height0_slope_coefficients'])
    for j, value in enumerate(alpha, 1):
        if (not np.array_equal(zt, f[f'height{j}_slope_knots'])
                or zk != int(f[f'height{j}_slope_degree'])):
            raise ValueError('height slope knot vectors or degrees differ')
        zcoeff = zcoeff+value*Box(f[f'height{j}_slope_coefficients'])
    zcoeff = (zcoeff+zcoeff[::-1])*.5
    zrange = coefficient_core_bounds(zt, zk, zcoeff, args.core, order=1)

    cuts = np.unique(np.r_[-args.core, args.core, f['phase_knots'], t])
    cuts = cuts[(cuts >= -args.core)&(cuts <= args.core)]
    raw0 = local_hulls(f['phase_knots'], 5, f['phase_coefficients'], cuts[:-1], derivatives=2)
    raw1 = local_hulls(f['phase_knots'], 5, direction['phase_direction_coefficients'],
                       cuts[:-1], derivatives=2)
    raw = add_up(raw0, mul_up(delta_abs, raw1))
    base = local_hulls(t, k, f['base_radius_coefficients'], cuts[:-1], derivatives=2)
    physical = [weighted_phase_bounds(raw[..., c], base, power)
                for c, power in enumerate((3, 2))]
    phase_sums = []
    for values in physical:
        # Supremum over the symmetric interval also bounds the explicitly
        # reflected physical phase; no exact parity of raw knots is assumed.
        maxima = values.max(axis=1)
        phase_sums.append(weighted_sum_up(maxima, np.ones(maxima.shape[-1])))
    beta, gamma = phase_sums
    pvertical, pvector = up(11/28), up(11/7)
    zmin, zmax = zrange[0]
    quotient_lower = float(down(zmin-mul_up(pvertical, mul_up(ab[0], gamma[1]))))
    vertical_loss = mul_up(pvertical, add_up(mul_up(ab[1], gamma[0]), mul_up(ab[0], gamma[1])))
    vz_lower, vz_upper = float(down(zmin-vertical_loss)), float(up(zmax+vertical_loss))
    horizontal_upper = mul_up(pvector, add_up(ab[1],
        mul_up(ab[0], add_up(beta[1], mul_up(gamma[0], gamma[1])))))
    horizontal_tangent_lower = float(down(1-mul_up(.5, mul_up(gamma[0], gamma[0]))))
    if arange[0, 0] <= 0 or vz_lower <= 0 or horizontal_tangent_lower <= 0:
        raise ValueError('strictly positive factors required for the transverse estimate')
    transverse_lower = float(down(down(vz_lower*horizontal_tangent_lower)
                                  -mul_up(gamma[0], horizontal_upper)))
    area_lower = float(down(arange[0, 0]*transverse_lower)) if transverse_lower > 0 else None
    area_upper = float(mul_up(ab[0], add_up(horizontal_upper, vz_upper)))
    zsecond = max(abs(zrange[1]))
    vertical_second = add_up(zsecond, mul_up(pvertical,
        add_up(add_up(mul_up(ab[2], gamma[0]), mul_up(2, mul_up(ab[1], gamma[1]))),
               mul_up(ab[0], add_up(gamma[2], mul_up(gamma[1], gamma[1]))))))
    report = dict(kind='uniform_real_scalar_gates_for_exact_affine_R57_family',
        origin_inputs_sha256=origin_sha, frozen_direction_sha256=direction_sha,
        source_sha256=digest(Path(__file__)),
        dependency_sha256={name: digest(Path(__file__).with_name(name)) for name in [
            'fourfold_phase_core_scalar_gate.py', 'fourfold_phase_root_interval.py',
            'fourfold_phase_uniform_tail.py', 'fourfold_interval_scalar.py']},
        family=metadata['family'], exact_parameter_interval=parameter,
        exact_parameter_fractions=[str(Fraction.from_float(v)) for v in parameter],
        absolute_parameter_bound=delta_abs, radial_core=[-args.core, args.core],
        radial_cells=len(cuts)-1, circumference_radius_derivative_ranges=arange.tolist(),
        exact_height_slope_ranges=zrange.tolist(),
        beta_field_absolute_derivative_bounds=beta.tolist(),
        gamma_field_absolute_derivative_bounds=gamma.tolist(),
        vertical_primitive_operator_bound=float(pvertical),
        full_vector_primitive_operator_bound=float(pvector),
        Fz_over_x_lower=quotient_lower, Fx_vertical_lower=vz_lower, Fx_vertical_upper=vz_upper,
        Fx_horizontal_norm_upper=float(horizontal_upper),
        tangent_horizontal_norm_lower=horizontal_tangent_lower,
        T_cross_Fx_norm_lower=transverse_lower, area_lower=area_lower, area_upper=area_upper,
        quotient_radial_Lipschitz_upper=float(mul_up(.5, vertical_second)),
        quotient_angular_Lipschitz_upper=float(mul_up(ab[0], gamma[1])),
        gate_passed=bool(quotient_lower > 0 and transverse_lower > 0 and area_lower > 0),
        exact_object=('Physical a,beta even and gamma,Z odd by explicit averaging; '
                      'Z is the exact affine slope integral; infinite R33 primitive; no Gaussian'),
        limitations=['Exact real affine family only; not a rounded predictor or independent control box',
            'No angular sample or finite primitive is substituted for the exact graph',
            'N, support/zeta, complex tubes and actual target curvature require their own certificates',
            'No ODE residual, cap, full-frequency inverse or closed isometric-family claim'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)
    if not report['gate_passed']:
        raise SystemExit('the affine scalar gate did not pass')


if __name__ == '__main__':
    main()

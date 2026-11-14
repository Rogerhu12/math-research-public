#!/usr/bin/env python3
"""Real-core / complex-angle chart for the exact R57 affine family.

Combines continuous real Q/support/area certificates with exact finite phase
coefficient hulls and R59's complete G_theta_theta bound.  Q=F_z/x, H=F.F,
G=(F_theta cross F_x).(F_theta cross F_x), and J=F.(F_theta cross F_x)
stay in the right half-plane.  All dot products in the complex angle are
bilinear; vector norms used only for estimates are Hermitian norms.
No finite primitive or sampled geometry is substituted for the true graph.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from fourfold_phase_root_interval import Box
from fourfold_phase_uniform_tail import (
    local_hulls, weighted_phase_bounds, weighted_sum_up,
    add_up, mul_up, exp_up, exact_iv, endpoint_up,
)
from fourfold_interval_scalar import interval_exp


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    if str(path).endswith('.gz'):
        with gzip.open(path, 'rt') as handle:
            return json.load(handle)
    return json.loads(Path(path).read_text())


def upper(value):
    return float(Box.coerce(value).hi)


def lower(value):
    return float(Box.coerce(value).lo)


def square(value):
    return Box(value)*Box(value)


def sqrt_checked(value, upward):
    """libm proposes only; an exact binary-rational square proves the bound."""
    if value <= 0 or not math.isfinite(value):
        raise ValueError('positive finite square-root input required')
    answer = math.sqrt(value)
    exact = Fraction.from_float(value)
    while ((Fraction.from_float(answer)**2 < exact) if upward
           else (Fraction.from_float(answer)**2 > exact)):
        answer = math.nextafter(answer, math.inf if upward else -math.inf)
    return answer


def exact_coverage(cells, right):
    position = Fraction(0)
    for row in sorted(cells, key=lambda cell:cell['radial_interval'][0]):
        left, end = map(Fraction.from_float, row['radial_interval'])
        if left != position or end <= left or not row['passed']:
            return False
        position = end
    return position == Fraction.from_float(right)


def phase_mode_bounds(frozen, direction, parameter, core):
    """Physical derivative 0..2 bounds, after explicit parity averaging."""
    knots, degree = frozen['base_knots'], int(frozen['base_degree'])
    cuts = np.unique(np.r_[-core, core, frozen['phase_knots'], knots])
    cuts = cuts[(cuts >= -core)&(cuts <= core)]
    raw0 = local_hulls(frozen['phase_knots'], 5,
                      frozen['phase_coefficients'], cuts[:-1], derivatives=2)
    raw1 = local_hulls(frozen['phase_knots'], 5,
                      direction['phase_direction_coefficients'], cuts[:-1], derivatives=2)
    raw = add_up(raw0, mul_up(max(map(abs, parameter)), raw1))
    base = local_hulls(knots, degree, frozen['base_radius_coefficients'],
                       cuts[:-1], derivatives=2)
    # The whole symmetric real interval covers both physical values at +/-x;
    # each explicitly averaged coefficient is bounded by this same maximum.
    fields = [weighted_phase_bounds(raw[..., component], base, power).max(axis=1)
              for component, power in enumerate((3, 2))]
    return fields, len(cuts)-1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--frozen-direction', type=Path, required=True)
    parser.add_argument('--scalar-certificate', type=Path, required=True)
    parser.add_argument('--core-certificate', type=Path, required=True)
    parser.add_argument('--strip-certificate', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    origin_hash, direction_hash = digest(args.inputs), digest(args.frozen_direction)
    with np.load(args.inputs, allow_pickle=False) as saved:
        frozen = {key:saved[key].copy() for key in saved.files}
    with np.load(args.frozen_direction, allow_pickle=False) as saved:
        direction = {key:saved[key].copy() for key in saved.files}
    if json.loads(str(direction['metadata']))['origin_inputs_sha256'] != origin_hash:
        raise ValueError('direction/origin mismatch')
    if (direction['phase_direction_coefficients'].shape != frozen['phase_coefficients'].shape
            or direction['alpha_direction'].shape != frozen['alpha'].shape):
        raise ValueError('affine direction dimensions differ')
    scalar, core, strip = map(read_json, (args.scalar_certificate,
                                        args.core_certificate, args.strip_certificate))
    config = core['configuration']
    for certificate in (scalar, config, strip):
        if (certificate['origin_inputs_sha256'] != origin_hash
                or certificate['frozen_direction_sha256'] != direction_hash):
            raise ValueError('certificates refer to different affine inputs')
    parameter = scalar['exact_parameter_interval']
    if parameter != config['parameter_interval'] or parameter != strip['exact_parameter_interval']:
        raise ValueError('parameter ranges differ')
    radial = scalar['radial_core']
    if radial != core['radial_core'] or radial != strip['radial_core'] or radial != [-config['core'], config['core']]:
        raise ValueError('real core ranges differ')
    if not (scalar['gate_passed'] and core['complete']
            and core['proved_continuous_real_N_support_zeta']
            and core['exact_dyadic_radial_coverage']
            and strip['status'] == 'complete' and strip['all_passed']
            and strip['complete_radial_coverage']
            and strip['proved_uniform_denominator_nonzero']):
        raise ValueError('an input certificate is partial or unproved')
    if (not exact_coverage(core['cells'], radial[1])
            or not exact_coverage(strip['cells'], radial[1])
            or strip['cell_count'] != strip['total_real_cells']
            or len(strip['cells']) != strip['cell_count']
            or strip['requested_indices'] != list(range(strip['total_real_cells']))):
        raise ValueError('closed radial coverage failed exact rational replay')
    sigma = strip['angular_strip_width']
    if not 0 < sigma < 1:
        raise ValueError('invalid physical angular strip')

    (beta, gamma), phase_cells = phase_mode_bounds(frozen, direction, parameter, radial[1])
    for values, key in ((beta, 'beta_field_absolute_derivative_bounds'),
                        (gamma, 'gamma_field_absolute_derivative_bounds')):
        summed = weighted_sum_up(values, np.ones(values.shape[-1]))
        if summed.tolist() != scalar[key]:
            raise ValueError('recomputed phase coefficient hulls differ from the scalar certificate')
    frequencies = 4*np.arange(1, beta.shape[-1]+1)
    cosh, sinh = [], []
    for frequency in frequencies:
        argument = exact_iv(sigma)*int(frequency)
        ep, em = interval_exp(argument), interval_exp(-argument)
        cosh.append(endpoint_up((ep+em)/2))
        sinh.append(endpoint_up((ep-em)/2))
    cosh, sinh = np.asarray(cosh), np.asarray(sinh)
    first_weights = mul_up(frequencies, cosh)
    second_weights = mul_up(frequencies*frequencies, cosh)
    combined0, combined1 = add_up(beta[0], gamma[0]), add_up(beta[1], gamma[1])
    I = upper(Box(sigma)+weighted_sum_up(combined0, sinh))
    Igamma = float(weighted_sum_up(gamma[0], sinh))
    P1 = upper(1+Box(weighted_sum_up(combined0, first_weights)))
    P2 = float(weighted_sum_up(combined0, second_weights))
    X1 = float(weighted_sum_up(combined1, cosh))
    Xtheta = float(weighted_sum_up(combined1, first_weights))
    tangent = exp_up(I)
    tangent_theta = upper(Box(tangent)*P1)
    tangent_theta2 = upper(Box(tangent)*(Box(P2)+square(P1)))
    tangent_x = upper(Box(tangent)*X1)
    tangent_x_theta = upper(Box(tangent)*(Box(Xtheta)+Box(X1)*P1))
    arange = np.asarray(scalar['circumference_radius_derivative_ranges'])
    a, ap, _ = np.maximum(abs(arange[:, 0]), abs(arange[:, 1]))
    if arange[0, 0] <= 0:
        raise ValueError('actual radius positivity missing')
    F = upper(Box(core['F_norm_upper'])+Box(sigma)*a*tangent)
    X = upper(Box(core['Fx_norm_upper'])+Box(sigma)*(Box(ap)*tangent+Box(a)*tangent_x))

    # gamma and all its theta derivatives are exactly odd in x.  Dividing by
    # x is evaluated as an integral of a radial derivative, including x=0.
    Q1 = upper(Box(a)*exp_up(Igamma)*float(weighted_sum_up(gamma[1], cosh)))
    Q2 = upper(Box(a)*exp_up(Igamma)*float(weighted_sum_up(gamma[1], first_weights)))
    Q_real = scalar['Fz_over_x_lower']
    Q_lower = lower(Box(Q_real)-square(sigma)*Q2/2)
    Q_upper = upper(Box(scalar['Fx_vertical_upper'])+Box(sigma)*Q1)

    # H=F.F has H_thetatheta=2*a^2+2*a*F.T_theta since T.T=1.
    H2 = upper(2*(square(a)+Box(a)*F*tangent_theta))
    H_lower = lower(square(core['support_lower'])-square(sigma)*H2/2)

    # J_thetatheta=-Nraw+a F.(T_thetatheta x X+a' T_theta x T
    #                        +2 a T_theta x T_x+a T x T_xtheta).
    # Complex cross products satisfy ||u x v|| <= ||u|| ||v||.
    N_upper = upper(square(a)*X*tangent*tangent_theta)
    J2 = upper(Box(N_upper)+Box(a)*F*(Box(tangent_theta2)*X
               +Box(ap)*tangent_theta*tangent
               +2*Box(a)*tangent_theta*tangent_x
               +Box(a)*tangent*tangent_x_theta))
    J_lower = lower(Box(core['support_numerator_lower'])-square(sigma)*J2/2)

    # R59 gives an entire-strip bilinear area-squared second derivative bound
    # on the larger real control box, hence also on this exact affine family.
    Gbounds = [max(row['G_derivative_bounds'][j] for row in strip['cells']) for j in range(3)]
    G_lower = lower(square(core['area_lower_from_support'])-square(sigma)*Gbounds[2]/2)
    positive = dict(Q=Q_lower, F_dot_F=H_lower, area_squared=G_lower, support_numerator=J_lower)
    if min(positive.values()) <= 0:
        raise ValueError(f'the right-half-plane chart gate failed: {positive}')
    root_G_upper = sqrt_checked(Gbounds[0], True)
    root_H_lower = sqrt_checked(H_lower, False)
    ground_lower = lower(Box(Q_lower)/F)
    ground_upper = upper(Box(Q_upper)/root_H_lower)
    support_modulus_lower = lower(Box(J_lower)/root_G_upper)
    zeta_modulus_lower = lower(Box(J_lower)/(Box(root_G_upper)*F))
    ell_upper = upper(Box(Q1)/Q_lower+Box(F)*a*tangent/H_lower)
    report = dict(
        kind='directed_complex_angle_chart_for_exact_R57_affine_family', proved=True,
        origin_inputs_sha256=origin_hash, frozen_direction_sha256=direction_hash,
        source_sha256=digest(Path(__file__)),
        dependency_sha256={name:digest(Path(__file__).with_name(name)) for name in
                          ('fourfold_phase_root_interval.py', 'fourfold_phase_uniform_tail.py',
                           'fourfold_interval_scalar.py')},
        certificate_sha256={str(path):digest(path) for path in
                            (args.scalar_certificate, args.core_certificate, args.strip_certificate)},
        exact_parameter_interval=parameter,
        exact_parameter_fractions=[str(Fraction.from_float(v)) for v in parameter],
        radial_core=radial, angular_strip_width=sigma,
        angular_coordinate='physical theta; normalized angle 4theta has four times this width',
        exact_closed_radial_coverage_rechecked=True, phase_hull_cells=phase_cells,
        beta_mode_absolute_radial_derivative_bounds=beta.tolist(),
        gamma_mode_absolute_radial_derivative_bounds=gamma.tolist(),
        imaginary_angle_majorant=I, imaginary_gamma_majorant=Igamma,
        phase_theta_majorants=[P1, P2], phase_x_majorants=[X1, Xtheta],
        tangent_norm_bounds=dict(T=tangent, T_theta=tangent_theta, T_theta2=tangent_theta2,
                                 T_x=tangent_x, T_x_theta=tangent_x_theta),
        complex_F_norm_upper=F, complex_Fx_norm_upper=X,
        complex_Q_angular_derivative_bounds=[Q1, Q2], complex_Q_absolute_upper=Q_upper,
        complex_H_angular_second_upper=H2, complex_J_angular_second_upper=J2,
        imported_complex_G_angular_derivative_bounds=Gbounds,
        right_half_plane_lower=positive,
        Nraw_modulus_lower=strip['minimum_Nraw_modulus_lower'],
        ground_factor_modulus_lower=ground_lower, ground_factor_modulus_upper=ground_upper,
        support_modulus_lower=support_modulus_lower, zeta_modulus_lower=zeta_modulus_lower,
        ell_modulus_upper=ell_upper,
        exact_definitions=dict(Q='Fz/x by exact continuous extension', H='F dot F (bilinear)',
            G='(Ftheta cross Fx) dot (Ftheta cross Fx) (bilinear)',
            J='F dot (Ftheta cross Fx)',
            ground='Q/exp(Log(H)/2)', h='J/exp(Log(G)/2)',
            zeta='J/exp((Log(G)+Log(H))/2)',
            ell='dtheta(Log(Q)-Log(H)/2)'),
        branch_statement='All four logs use the right-half-plane branch, real on the real circle; '
                         'these are periodic holomorphic functions of theta throughout the strip',
        limitations=['Radial and affine parameters are real; only theta is complex',
                     'Exact affine family only; the stronger graph-chart claims do not apply to '
                     'the larger independent control box used as an R59 input',
                     'No new ODE flow error, Wiener residual, beta, cap, full-frequency inverse '
                     'or exact isometric-family claim'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('proved', 'right_half_plane_lower',
          'ground_factor_modulus_lower', 'ground_factor_modulus_upper',
          'support_modulus_lower', 'zeta_modulus_lower', 'ell_modulus_upper')}, indent=2), flush=True)


if __name__ == '__main__':
    main()

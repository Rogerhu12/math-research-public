#!/usr/bin/env python3
"""Design the necessary quartic support polynomial using exactly closed bases.

Research optimization runs only in this public repository's GitHub Actions.
Two real root variables and four coefficient equations represent the same two
quartic-square conditions without dividing by a possibly small leading term.
The nonzero leading amplitude, root separation, and physical half-strip are
explicitly controlled. A quartic design is not a constructed complex profile.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import least_squares

import literature_closed_codesign as closed


def c_polynomial(coefficients):
    p0, p1, p2, _, _, r0, r1, s0, s1, t0, t1 = coefficients
    return np.array([r0, r1+s0, s1+t0-p0/4, t1-p1/4, -p2/4])


def square_coefficients(amplitude, roots):
    a, b = roots
    return amplitude*np.polynomial.polynomial.polymul(
        np.array([a*a, -2*a, 1.]), np.array([b*b, -2*b, 1.]))


def square_invariants(poly, leading_floor):
    """Diagnostic two-equation reduction; never divide below the stated floor."""
    c0, c1, c2, c3, c4 = map(float, poly)
    if abs(c4) < leading_floor:
        return dict(eligible_nonzero_leading=False, monic_linear=None,
                    monic_constant=None, square_residuals=None,
                    quadratic_discriminant=None, candidate_quadratic_roots=None)
    linear = c3/(2*c4)
    constant = (c2/c4-linear*linear)/2
    discriminant = linear*linear-4*constant
    roots = None
    if discriminant > 0:
        half = np.sqrt(discriminant)/2
        roots = [float(-linear/2-half), float(-linear/2+half)]
    return dict(eligible_nonzero_leading=True, monic_linear=linear,
                monic_constant=constant,
                square_residuals=[c1-2*c4*linear*constant, c0-c4*constant*constant],
                quadratic_discriminant=discriminant,
                candidate_quadratic_roots=roots,
                candidate_roots_are_not_certified_roots_of_actual_quartic=True)


def target_roots(g, root_parameters, xi_scale, side):
    gap, width = xi_scale*np.exp(root_parameters)
    if side == 'positive':
        a = -float(np.min(g['omega']))+gap
        return np.array([a, a+width])
    b = -float(np.max(g['omega']))-gap
    return np.array([b-width, b])


def physical_strip(g, roots, side):
    denominators = g['omega'][:, None]+np.asarray(roots)[None, :]
    valid = bool(np.all(denominators > 0) if side == 'positive'
                 else np.all(denominators < 0))
    contains_pole = bool(np.any(denominators[:, 0]*denominators[:, 1] <= 0))
    result = dict(side=side, frozen_target_roots=list(map(float, roots)),
                  denominator_min=float(np.min(denominators)),
                  denominator_max=float(np.max(denominators)),
                  minimum_absolute_denominator=(0. if contains_pole else float(np.min(abs(denominators)))),
                  interval_contains_a_pole_at_a_validation_angle=contains_pole,
                  same_sign_at_all_validation_nodes=valid,
                  continuous_half_strip_certified=False,
                  physical_u_range=None, endpoint_u_ranges=None,
                  physical_u_width_min=None, physical_u_width_max=None)
    if valid:
        physical_u = np.sqrt(g['v'])[:, None]/denominators
        widths = abs(physical_u[:, 1]-physical_u[:, 0])
        result.update(physical_u_range=[float(np.min(physical_u)), float(np.max(physical_u))],
                      endpoint_u_ranges=[[float(np.min(physical_u[:, j])),
                                          float(np.max(physical_u[:, j]))] for j in (0, 1)],
                      physical_u_width_min=float(np.min(widths)),
                      physical_u_width_max=float(np.max(widths)))
    return result


def endpoint_rates(coefficients, roots, amplitude):
    a, b = map(float, roots)
    p0, p1, p2, _, _, r0, r1, s0, s1, t0, t1 = coefficients
    W = np.array([s0, s1+2*t0, 2*t1-p1/4, -p2/2])
    values = np.polynomial.polynomial.polyval(np.array([a, b]), W)
    second_order = amplitude*(b-a)**2
    rates = np.array([-3*values[0], 3*values[1]])/(2*second_order)
    normalized = rates/((b-a)/2)
    return dict(W_at_frozen_target_roots=values.tolist(),
                candidate_endpoint_quadratic_coefficient=float(second_order),
                candidate_exponential_rates_physical_xi=rates.tolist(),
                candidate_exponential_rates_normalized_interval=normalized.tolist(),
                both_standard_exponential_rates_positive=bool(np.all(rates > 0)),
                rates_are_conditional_on_quartic_shape=True,
                other_flat_asymptotics_not_excluded=True)


def warm_parameters(path, q, modes):
    if path is None:
        return None, None
    data = json.loads(path.read_text())
    rows = [row for row in data.get('designs', [])
            if row.get('q') == q and len(row.get('final_parameters', [])) == modes+4]
    if not rows:
        return None, dict(path=str(path), matching_design_found=False)
    row = rows[0]
    return np.array(row['final_parameters'], dtype=float), dict(
        path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        matching_design_found=True, q=q,
        source_schema=data.get('schema'), source_design_index=data['designs'].index(row))


def validation_record(g, n, independent_scales, roots, side, target,
                      polynomial_weights, leading_floor, leading_sign):
    record = closed.diagnostic(g, n, independent_scales)
    poly = c_polynomial(g['coefficients'])
    residual = (poly-target)*polynomial_weights
    target_size = max(float(np.linalg.norm(target*polynomial_weights)), np.finfo(float).tiny)
    record.update(square_target_frozen_ascending_coefficients=target.tolist(),
                  square_residual_vs_frozen_target=(poly-target).tolist(),
                  scaled_square_residual_vs_frozen_target=residual.tolist(),
                  scaled_square_residual_l2=float(np.linalg.norm(residual)),
                  scaled_square_residual_max=float(np.max(abs(residual))),
                  relative_square_coefficient_residual=float(np.linalg.norm(residual)/target_size),
                  frozen_leading_floor=float(leading_floor),
                  leading_sign=int(leading_sign),
                  nonzero_leading_guard_passed=bool(leading_sign*poly[4] >= leading_floor),
                  square_invariants=square_invariants(poly, leading_floor),
                  physical_strip=physical_strip(g, roots, side))
    if abs(poly[4]) >= leading_floor:
        record['candidate_endpoint_rates'] = endpoint_rates(g['coefficients'], roots, poly[4])
    else:
        record['candidate_endpoint_rates'] = None
    return record


def one_design(args, q, a, b, side):
    started = time.monotonic()
    initial, warm = warm_parameters(args.warm_start, q, args.modes)
    if initial is None:
        initial = closed.initial(q, a, b, args.modes, args.theta_n)
    g0 = closed.geometry(initial, q, args.modes, args.theta_n)
    independent_scales = np.maximum(1., abs(g0['coefficients'][closed.INDEPENDENT]))
    # Fixed units avoid a changing residual scale during the design.
    xi_scale = max(1., float(np.ptp(g0['omega'])))
    first_root_parameters = np.log([args.initial_root_gap, args.initial_root_width])
    roots0 = target_roots(g0, first_root_parameters, xi_scale, side)
    poly0 = c_polynomial(g0['coefficients'])
    sign = int(np.sign(poly0[4])) if args.leading_sign == 0 else args.leading_sign
    if sign == 0:
        sign = 1
    target0 = square_coefficients(poly0[4], roots0)
    powers = xi_scale**np.arange(5)
    polynomial_scale = max(1., float(np.max(abs(poly0)*powers)),
                           float(np.max(abs(target0)*powers)))
    polynomial_weights = powers/polynomial_scale
    leading_scale = max(abs(float(poly0[4])), .001*polynomial_scale/xi_scale**4)
    leading_floor = args.leading_floor_fraction*leading_scale
    sample = np.arange(96)*args.theta_n//96
    x0 = np.r_[initial, first_root_parameters]

    def residual(x):
        g = closed.geometry(x[:-2], q, args.modes, args.theta_n)
        roots = target_roots(g, x[-2:], xi_scale, side)
        poly = c_polynomial(g['coefficients'])
        target = square_coefficients(poly[4], roots)
        shape = (poly[:4]-target[:4])*polynomial_weights[:4]
        leading = max(leading_floor-sign*poly[4], 0)/leading_scale
        concentration = np.maximum(abs(.5*np.log(g['v'][sample]))-args.logh_bound, 0)
        regularity = np.maximum(args.speed_floor-g['data']['sphere_speed'][sample], 0)/args.speed_floor
        global_regularity = max(args.speed_floor-float(np.min(g['data']['sphere_speed'])), 0)/args.speed_floor
        answer = np.r_[shape, 10*leading, 10*concentration, 10*regularity, 10*global_regularity]
        if args.enforce_exponential_signs:
            safe_amplitude = sign*max(sign*poly[4], leading_floor)
            rates = endpoint_rates(g['coefficients'], roots, safe_amplitude)
            normalized = np.asarray(rates['candidate_exponential_rates_normalized_interval'])
            answer = np.r_[answer, np.maximum(args.exponential_rate_floor-normalized, 0)]
        if not np.all(np.isfinite(answer)):
            raise ValueError('nonfinite quartic design residual')
        return answer

    lo = np.r_[-.8, .05, -.6, -.5, .76, np.full(args.modes-1, -.4),
               np.log(args.root_gap_bounds[0]), np.log(args.root_width_bounds[0])]
    hi = np.r_[.8, 1.4, .6, .5, 1.55, np.full(args.modes-1, .4),
               np.log(args.root_gap_bounds[1]), np.log(args.root_width_bounds[1])]
    fit = least_squares(residual, x0, bounds=(lo, hi), max_nfev=args.max_nfev,
                        ftol=1e-11, xtol=1e-11, gtol=1e-10,
                        x_scale='jac',
                        jac=lambda x: closed.absolute_jacobian(residual, x))
    final = closed.geometry(fit.x[:-2], q, args.modes, args.theta_n)
    frozen = dict(tilt=final['tilt'], normalization=final['normalization'])
    roots = target_roots(final, fit.x[-2:], xi_scale, side)
    amplitude = float(c_polynomial(final['coefficients'])[4])
    target = square_coefficients(amplitude, roots)
    validation = [validation_record(
        closed.geometry(fit.x[:-2], q, args.modes, n, frozen), n,
        independent_scales, roots, side, target, polynomial_weights, leading_floor, sign)
        for n in args.validation_n]
    return dict(q=q, side=side, warm_start=warm,
                initial_parameters=initial.tolist(), final_parameters=fit.x[:-2].tolist(),
                parameter_order=['rho0', 'rho1', 'rho2', 'rho3', 'b']+
                                [f'c{j}' for j in range(1, args.modes+1) if j != 2],
                root_parameters_initial=first_root_parameters.tolist(),
                root_parameters_final=fit.x[-2:].tolist(),
                root_parameter_meaning='log gap from sampled pole half-band, log interval width; both in frozen xi units',
                frozen_xi_scale=xi_scale, frozen_polynomial_scale=polynomial_scale,
                frozen_polynomial_weights=polynomial_weights.tolist(),
                frozen_independent_scales=independent_scales.tolist(),
                frozen_leading_reference_scale=leading_scale,
                frozen_leading_floor=leading_floor, leading_sign=sign,
                frozen_target_roots=roots.tolist(), frozen_square_amplitude=amplitude,
                frozen_target_root_separation=float(roots[1]-roots[0]),
                frozen_square_coefficients=target.tolist(), frozen_validation_data=frozen,
                initial=validation_record(g0, args.theta_n, independent_scales, roots0,
                                          side, target0, polynomial_weights, leading_floor, sign),
                validation=validation,
                solver=dict(success=bool(fit.success), message=str(fit.message),
                            nfev=int(fit.nfev), optimality=float(fit.optimality),
                            jacobian_method='central absolute coordinate differences',
                            jacobian_step=2e-5,
                            jacobian_coordinate_step='2e-5 * max(1, abs(x[j]))',
                            final_jacobian_direction_check=closed.jacobian_direction_check(residual, fit.x),
                            initial_residual_l2=float(np.linalg.norm(residual(x0))),
                            final_residual_l2=float(np.linalg.norm(fit.fun)),
                            elapsed_seconds=time.monotonic()-started),
                exact_closure_mechanism_proved=True,
                stored_tilt_is_reference_quadrature_approximation=True,
                target_roots_and_amplitude_are_frozen_for_validation=True,
                actual_quartic_has_two_exact_double_real_roots_proved=False,
                continuous_physical_half_strip_proved=False,
                full_complex_period_equation_solved=False,
                three_complex_total_moments_solved=False,
                nonzero_profile_constructed=False,
                finite_isometric_path_proved=False, embedding_proved=False,
                reach_lower_certified=False, task_complete=False)


def developer_check():
    # Synthetic polynomial/coordinate fixtures only. No geometric design call.
    poly = square_coefficients(2., [3., 5.])
    inv = square_invariants(poly, .1)
    assert np.max(abs(np.asarray(inv['square_residuals']))) == 0
    assert np.max(abs(np.asarray(inv['candidate_quadratic_roots'])-[3., 5.])) == 0
    # A zero/vanishing quartic must not be accepted by cancellation of two residuals.
    assert not square_invariants(np.zeros(5), .1)['eligible_nonzero_leading']
    assert not square_invariants(poly*1e-14, .1)['eligible_nonzero_leading']
    assert square_invariants(np.array([1., 0., 2., 0., 1.]), .1)['candidate_quadratic_roots'] is None
    g = dict(omega=np.array([-1., 0., 1.]), v=np.array([1., 4., 9.]))
    positive = physical_strip(g, [3., 5.], 'positive')
    negative = physical_strip(g, [-5., -3.], 'negative')
    crossing = physical_strip(g, [-.5, .5], 'positive')
    assert positive['same_sign_at_all_validation_nodes']
    assert negative['same_sign_at_all_validation_nodes']
    assert not crossing['same_sign_at_all_validation_nodes']
    # Check the exact mapping from the existing eleven-entry coefficient interface.
    p0 = p1 = s0 = s1 = 0.
    p2, r0, r1, t0, t1 = -4*poly[4], poly[0], poly[1], poly[2], poly[3]
    coefficients = np.array([p0, p1, p2, r1, s1-p0/2, r0, r1, s0, s1, t0, t1])
    assert np.max(abs(c_polynomial(coefficients)-poly)) == 0
    # A changed leading coefficient is visible against a frozen full target.
    altered = poly.copy(); altered[4] *= 1.01
    assert np.max(abs(altered-poly)) > 0
    # Near-zero synthetic coordinates must retain an absolute finite-difference
    # step. This exercises the shared Jacobian helper, not the geometry.
    point = np.array([1e-16, -2.])
    def synthetic_residual(x):
        return np.array([x[0]+3*x[1], x[0]*x[1]+x[1]**2])
    exact_jacobian = np.array([[1., 3.], [point[1], point[0]+2*point[1]]])
    approximate_jacobian = closed.absolute_jacobian(synthetic_residual, point)
    jacobian_error = float(np.max(abs(approximate_jacobian-exact_jacobian)))
    assert jacobian_error < 1e-8
    result = dict(developer_check=True, no_geometry_evaluated=True, no_optimization=True,
                  square_mapping_max_error=float(np.max(abs(c_polynomial(coefficients)-poly))),
                  synthetic_square_invariants=inv, synthetic_positive_strip=positive,
                  synthetic_negative_strip=negative, pole_crossing_rejected=True,
                  vanishing_leading_rejected=True,
                  synthetic_absolute_jacobian_max_error=jacobian_error)
    print(json.dumps(result, allow_nan=False))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--modes', type=int, default=12)
    p.add_argument('--theta-n', type=int, default=768)
    p.add_argument('--validation-n', type=int, nargs='+', default=[768, 1536, 3072])
    p.add_argument('--q', type=int, nargs='+', choices=[2, 3, 4], default=[3, 2, 4])
    p.add_argument('--sides', nargs='+', choices=['positive', 'negative'], default=['positive', 'negative'])
    p.add_argument('--max-nfev', type=int, default=250)
    p.add_argument('--warm-start', type=Path)
    p.add_argument('--logh-bound', type=float, default=.8)
    p.add_argument('--speed-floor', type=float, default=.08)
    p.add_argument('--leading-sign', type=int, choices=[-1, 0, 1], default=0)
    p.add_argument('--leading-floor-fraction', type=float, default=.1)
    p.add_argument('--root-gap-bounds', type=float, nargs=2, default=[.05, 4.])
    p.add_argument('--root-width-bounds', type=float, nargs=2, default=[.1, 4.])
    p.add_argument('--initial-root-gap', type=float, default=.5)
    p.add_argument('--initial-root-width', type=float, default=1.)
    p.add_argument('--enforce-exponential-signs', action='store_true')
    p.add_argument('--exponential-rate-floor', type=float, default=.05)
    p.add_argument('--out', type=Path)
    p.add_argument('--developer-check', action='store_true')
    args = p.parse_args()
    if args.developer_check:
        developer_check()
        return
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        p.error('run research optimization in this public repository Actions')
    if args.out is None or args.modes < 4 or args.theta_n < 384:
        p.error('need output, at least four modes and at least 384 reference samples')
    if not 0 < args.leading_floor_fraction < 1 or args.speed_floor <= 0:
        p.error('invalid nonzero-leading or indicatrix-speed guard')
    for bounds, value in [(args.root_gap_bounds, args.initial_root_gap),
                          (args.root_width_bounds, args.initial_root_width)]:
        if not 0 < bounds[0] <= value <= bounds[1]:
            p.error('positive root bounds must contain their initial value')
    arguments = vars(args) | {'out': str(args.out),
                             'warm_start': None if args.warm_start is None else str(args.warm_start)}
    output = dict(schema='literature-quartic-closed-base-design-v1', arguments=arguments,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  closed_geometry_source_sha256=hashlib.sha256(Path(closed.__file__).read_bytes()).hexdigest(),
                  profile_existence_is_not_assumed=True,
                  root_and_amplitude_validation_are_frozen=True,
                  numerical_optimization_is_not_an_existence_proof=True,
                  task_complete=False, designs=[])
    defaults = {3: (.35, 1.1), 2: (.60, 1.2), 4: (.35, 1.1)}
    for q in args.q:
        for side in args.sides:
            row = one_design(args, q, *defaults[q], side)
            output['designs'].append(row)
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
            print(json.dumps(dict(q=q, side=side, solver=row['solver'],
                                  final=row['validation'][-1]), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

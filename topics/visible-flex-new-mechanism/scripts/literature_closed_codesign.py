#!/usr/bin/env python3
"""Design actual period coefficients with an exactly defined closure tilt.

Research optimization runs only in this public repository's GitHub Actions.
The reference quadrature approximation of the unique tilt is frozen before
validation. A finite solver result is not a closed-surface flex.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time
from fractions import Fraction

import numpy as np
from scipy.optimize import brentq, least_squares

import literature_band_seed as seed
from literature_band_second_order import polynomial_period_operator
from literature_base_codesign import NAMES, extract_coefficients, reconstruct_coefficients

INDEPENDENT = np.array([0, 1, 2, 5, 6, 7, 8, 9, 10])


def absolute_jacobian(function, x, step=2e-5):
    """Central differences with an absolute floor for near-zero parameters.

    A relative-only step at Fourier coefficients around 1e-16 can be 1e-21,
    which is unsuitable for coefficients formed by quadrature cancellation.
    These derivative probes do not change the reported geometric candidate.
    """
    x = np.asarray(x, dtype=float)
    columns = []
    for j in range(len(x)):
        h = step*max(1., abs(x[j]))
        plus, minus = x.copy(), x.copy()
        plus[j] += h
        minus[j] -= h
        columns.append((function(plus)-function(minus))/(2*h))
    return np.column_stack(columns)


def jacobian_direction_check(function, x):
    direction = np.random.default_rng(20261114).normal(size=len(x))
    direction /= np.linalg.norm(direction)
    predicted = absolute_jacobian(function, x) @ direction
    h = 2e-6
    observed = (function(x+h*direction)-function(x-h*direction))/(2*h)
    return dict(column_step_floor=2e-5, directional_step=h,
                relative_difference=float(np.linalg.norm(predicted-observed)/
                                          max(np.linalg.norm(observed), 1e-30)))


def radial_sphere(q, b, rho, n):
    theta = np.arange(n) * (2 * np.pi / n)
    x = q * theta
    js = np.arange(1, 4)
    cs, sn = np.cos(x[:, None] * js), np.sin(x[:, None] * js)
    ell = rho[0] + cs @ rho[1:]
    ep = -q * (sn * js) @ rho[1:]
    epp = -q*q * (cs * js**2) @ rho[1:]
    eppp = q**3 * (sn * js**3) @ rho[1:]
    r = np.exp(ell)
    rp, rpp, rppp = r*ep, r*(epp+ep*ep), r*(eppp+3*ep*epp+ep**3)
    phi = theta + b * np.sin(2*x) / q
    fp = 1 + 2*b*np.cos(2*x)
    fpp, fppp = -4*b*q*np.sin(2*x), -8*b*q*q*np.cos(2*x)
    S = 1+r*r
    f = np.column_stack((r*np.cos(phi), r*np.sin(phi), np.ones(n)))
    df = np.column_stack((rp*np.cos(phi)-r*fp*np.sin(phi),
                          rp*np.sin(phi)+r*fp*np.cos(phi), np.zeros(n)))
    B = f/np.sqrt(S)[:, None]
    Bp = df/np.sqrt(S)[:, None]-f*(r*rp/S**1.5)[:, None]
    Q = rp*rp+r*r*S*fp*fp
    Qp = 2*rp*rpp+2*r*rp*(1+2*r*r)*fp*fp+2*r*r*S*fp*fpp
    J = 2*rp*rp*fp+r*rp*fpp-r*rpp*fp+r*r*fp**3
    Jp = (3*rp*rpp*fp+3*rp*rp*fpp+r*rp*fppp-r*rppp*fp
          +2*r*rp*fp**3+3*r*r*fp*fp*fpp)
    speed = np.sqrt(Q)/S
    k = J*S**1.5/Q**1.5
    kp = (Jp+J*(3*r*rp/S-1.5*Qp/Q))*S**1.5/Q**1.5
    return dict(theta=theta, r=r, rp=rp, B=B, B_theta=Bp,
                sphere_speed=speed, kappa=k, kappa_theta=kp,
                raw=-np.cross(B, Bp))


def closing_tilt(ell, z, b):
    """Unique root of E_d[z]=-1/(2b); derivative is 2 Var_d(z)>0."""
    def equation(d):
        exponent = 2*(ell+d*z)
        weights = np.exp(exponent-np.max(exponent))
        return float(weights @ z / np.sum(weights) + 1/(2*b))
    lo, hi = -1., 1.
    while equation(lo) >= 0:
        lo *= 2
        if lo < -512:
            raise ValueError('closure tilt bracket did not resolve')
    while equation(hi) <= 0:
        hi *= 2
        if hi > 512:
            raise ValueError('closure tilt bracket did not resolve')
    return float(brentq(equation, lo, hi, xtol=2e-14, rtol=1e-14))


def geometry(parameters, q, modes, n, frozen=None):
    rho, b, free = np.asarray(parameters[:4]), float(parameters[4]), np.asarray(parameters[5:])
    data = radial_sphere(q, b, rho, n)
    x = q*data['theta']
    js = np.array([j for j in range(1, modes+1) if j != 2])
    ell = np.cos(x[:, None]*js) @ free
    ep = -q*(np.sin(x[:, None]*js)*js) @ free
    z = np.cos(2*x)
    tilt = closing_tilt(ell, z, b) if frozen is None else frozen['tilt']
    ell = ell+tilt*z
    ep = ep-2*q*tilt*np.sin(2*x)
    raw_v = (1+data['r']**-2)*np.exp(2*ell)
    normalization = (float(np.mean(raw_v*data['sphere_speed'])/np.mean(data['sphere_speed']))
                     if frozen is None else frozen['normalization'])
    v = raw_v/normalization
    vp = v*(2*ep-2*data['rp']/(data['r']*(1+data['r']**2)))
    om_prime = data['kappa_theta']/(2*np.sqrt(v))
    omega = seed.periodic_primitive(om_prime[:, None])[:, 0]
    closure = 2*np.pi*np.mean(v[:, None]*data['raw'], axis=0)
    values = np.array(polynomial_period_operator(data, v, vp, omega, np.array([-1., 0., 1., 2.])))
    coefficients = extract_coefficients(values)
    error = np.max(abs(values-reconstruct_coefficients(coefficients, np.array([-1., 0., 1., 2.]))))
    return dict(data=data, v=v, vp=vp, omega=omega, coefficients=coefficients,
                radial_parameters=rho.tolist(), angular_parameter=b,
                closure=closure, length=float(2*np.pi*np.mean(v*data['sphere_speed'])),
                tilt=tilt, normalization=normalization, polynomial_identity_error=float(error),
                asymptotic_half_period=float(2*np.pi*np.mean(om_prime)))


def initial(q, a, b, modes, n):
    x = 2*np.pi*np.arange(n)/n
    logr = np.log(1+a*np.cos(x))
    rho = np.r_[np.mean(logr), [2*np.mean(logr*np.cos(j*x)) for j in range(1, 4)]]
    lam = 1-np.cos(2*x)/b+np.cos(4*x)/(4*b*b)
    assert np.min(lam) > 0
    logh = .5*np.log(lam)
    free = [2*np.mean(logh*np.cos(j*x)) for j in range(1, modes+1) if j != 2]
    return np.r_[rho, b, np.clip(free, -.39, .39)]


def diagnostic(g, n, scales):
    c = g['coefficients']
    C = np.array([c[5], c[6]+c[7], -c[0]/4+c[8]+c[9], c[10]-c[1]/4, -c[2]/4])
    alpha = seed.periodic_primitive(g['v'][:, None]*g['data']['raw'])
    D = seed.sampled_diameter(alpha[::max(1, n//768)])
    # B' can vanish only when phi'=0 and (log r)'=0.  At phi'=0,
    # cos(x)^2=(1-1/(2b))/2 and the remaining factor is A+4 rho2 cos(x).
    # The following exact rational calculation certifies no simultaneous zero
    # for the stored binary64 parameters; it is not a quantitative speed bound.
    r0, r1, r2, r3 = map(Fraction.from_float, g['radial_parameters'])
    b = Fraction.from_float(g['angular_parameter'])
    c2 = (1-Fraction(1, 2)/b)/2
    A = r1+3*r3*(1-1/b)
    discriminant = A*A-16*r2*r2*c2
    return dict(theta_n=n, period_coefficients=dict(zip(NAMES, map(float, c))),
                independent_scaled_l2=float(np.linalg.norm(c[INDEPENDENT]/scales)),
                independent_scaled_max=float(np.max(abs(c[INDEPENDENT]/scales))),
                C_ascending_coefficients=C.tolist(), C_complex_roots=[[float(z.real), float(z.imag)]
                         for z in np.polynomial.polynomial.polyroots(C)],
                polynomial_identity_error=g['polynomial_identity_error'],
                additional_identity_errors=[float(c[3]-c[6]), float(c[4]-c[8]+c[0]/2)],
                actual_curve_closure_vector=g['closure'].tolist(),
                closure_over_length=float(np.linalg.norm(g['closure'])/g['length']),
                asymptotic_half_period=g['asymptotic_half_period'],
                speed_min=float(np.min(g['v'])), speed_max=float(np.max(g['v'])),
                speed_contrast=float(np.max(g['v'])/np.min(g['v'])),
                indicatrix_speed_min_sample=float(np.min(g['data']['sphere_speed'])),
                continuous_indicatrix_regular_by_exact_rational_nonvanishing=bool(discriminant != 0),
                regularity_discriminant_numerator=discriminant.numerator,
                regularity_discriminant_denominator=discriminant.denominator,
                omega_min_sample=float(np.min(g['omega'])), omega_max_sample=float(np.max(g['omega'])),
                projected_centerline_diameter_sample=D,
                projected_curve_is_diagnostic_until_closure_certified=True,
                formal_principal_radius_over_diameter_sample=float(np.min(g['v'])/D),
                reach_lower_certified=False, tilt=g['tilt'], normalization=g['normalization'])


def one_design(args, q, a, b):
    start = time.monotonic()
    x0 = initial(q, a, b, args.modes, args.theta_n)
    g0 = geometry(x0, q, args.modes, args.theta_n)
    scales = np.maximum(1, abs(g0['coefficients'][INDEPENDENT]))
    sample = np.arange(96)*args.theta_n//96
    def residual(x):
        g = geometry(x, q, args.modes, args.theta_n)
        concentration = np.maximum(abs(.5*np.log(g['v'][sample]))-args.logh_bound, 0)
        regularity = np.maximum(args.speed_floor-g['data']['sphere_speed'][sample], 0)/args.speed_floor
        return np.r_[g['coefficients'][INDEPENDENT]/scales, 10*concentration, 10*regularity]
    lo = np.r_[-.8, .05, -.6, -.5, .76, np.full(args.modes-1, -.4)]
    hi = np.r_[.8, 1.4, .6, .5, 1.55, np.full(args.modes-1, .4)]
    fit = least_squares(residual, x0, bounds=(lo, hi), max_nfev=args.max_nfev,
                        jac=lambda x: absolute_jacobian(residual, x),
                        ftol=1e-11, xtol=1e-11, gtol=1e-10, x_scale='jac')
    final = geometry(fit.x, q, args.modes, args.theta_n)
    frozen = dict(tilt=final['tilt'], normalization=final['normalization'])
    validations = [diagnostic(geometry(fit.x, q, args.modes, n, frozen), n, scales)
                   for n in args.validation_n]
    return dict(q=q, initial_parameters=x0.tolist(), final_parameters=fit.x.tolist(),
                parameter_order=['rho0', 'rho1', 'rho2', 'rho3', 'b']+
                                [f'c{j}' for j in range(1, args.modes+1) if j != 2],
                independent_names=[NAMES[j] for j in INDEPENDENT], scales=scales.tolist(),
                derivative_method='central differences; column step 2e-5*max(1,abs(parameter))',
                final_directional_derivative_check=jacobian_direction_check(residual, fit.x),
                frozen_validation_data=frozen, initial=diagnostic(g0, args.theta_n, scales),
                validation=validations, solver=dict(success=bool(fit.success), message=str(fit.message),
                    nfev=int(fit.nfev), optimality=float(fit.optimality),
                    initial_residual_l2=float(np.linalg.norm(residual(x0))),
                    final_residual_l2=float(np.linalg.norm(fit.fun)), elapsed_seconds=time.monotonic()-start),
                exact_closure_mechanism_proved=True,
                stored_tilt_is_reference_quadrature_approximation=True,
                all_period_coefficients_zero_proved=False, nonzero_profile_constructed=False,
                finite_isometric_path_proved=False, task_complete=False)


def developer_check():
    # Tiny formula checks only: no research candidate selection or optimizer.
    n = 32
    theta = np.arange(n)*2*np.pi/n
    b = 1.1
    ell = .07*np.cos(theta)-.03*np.cos(3*theta)
    tilt = closing_tilt(ell, np.cos(2*theta), b)
    w = np.exp(2*(ell+tilt*np.cos(2*theta)))
    closure = float(np.mean(w*(1+2*b*np.cos(2*theta))))
    data = radial_sphere(3, b, np.array([0., .3, .02, -.01]), n)
    raw_formula = -data['r']**2/(1+data['r']**2)*(1+2*b*np.cos(6*data['theta']))
    cross_error = float(np.max(abs(data['raw'][:, 2]-raw_formula)))
    unit_error = float(np.max(abs(np.sum(data['B']**2, axis=1)-1)))
    speed_error = float(np.max(abs(np.linalg.norm(data['B_theta'], axis=1)-data['sphere_speed'])))
    if max(abs(closure), cross_error, unit_error, speed_error) > 1e-12:
        raise AssertionError((closure, cross_error, unit_error, speed_error))
    point = np.array([1e-16, .3])
    synthetic = lambda x: np.array([np.sin(x[0])+x[1]**2, np.exp(x[1])+x[0]*x[1]])
    exact = np.array([[np.cos(point[0]), 2*point[1]], [point[1], np.exp(point[1])+point[0]]])
    jac_error = float(np.max(abs(absolute_jacobian(synthetic, point)-exact)))
    if jac_error > 2e-9:
        raise AssertionError(jac_error)
    print(json.dumps(dict(developer_check=True, no_optimization=True, closure_scalar=closure,
                          raw_z_identity=cross_error, sphere_unit=unit_error,
                          analytic_speed=speed_error, tiny_quadrature_tilt=tilt,
                          absolute_jacobian_synthetic_max_error=jac_error)))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--modes', type=int, default=12)
    p.add_argument('--theta-n', type=int, default=768)
    p.add_argument('--validation-n', type=int, nargs='+', default=[768, 1536, 3072])
    p.add_argument('--max-nfev', type=int, default=400)
    p.add_argument('--logh-bound', type=float, default=.8)
    p.add_argument('--speed-floor', type=float, default=.08)
    p.add_argument('--out', type=Path)
    p.add_argument('--developer-check', action='store_true')
    args = p.parse_args()
    if args.developer_check:
        developer_check()
        return
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        p.error('run research optimization in the public repository Actions')
    if args.out is None or args.modes < 4 or args.theta_n < 384:
        p.error('need output, at least four modes and at least 384 reference samples')
    output = dict(schema='literature-exact-closure-codesign-v1', arguments=vars(args)|{'out':str(args.out)},
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  zero_mean_omega_is_fixed_by_definition=True,
                  validation_does_not_resolve_tilt_or_normalization=True,
                  numerical_optimization_is_not_an_existence_proof=True, task_complete=False, designs=[])
    for q, a, b in [(3, .35, 1.1), (2, .60, 1.2), (4, .35, 1.1)]:
        row = one_design(args, q, a, b)
        output['designs'].append(row)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
        print(json.dumps(dict(q=q, solver=row['solver'], final=row['validation'][-1]), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

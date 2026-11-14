#!/usr/bin/env python3
"""Test whether an actually closed base can have a negative physical-root ratio.

This is a geometric C/W design, not a full profile or a finite flex.  The two
smooth equations are C(xi)=0 and W(xi)-target*C'(xi)=0.  A frozen nonzero
derivative scale and sampled physical-half-line guards prevent a vanishing
denominator from being mistaken for a target ratio.  Research runs only in
this public repository's Actions; --developer-check uses synthetic polynomials.
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


def polynomials(coefficients):
    p0, p1, p2, _, _, r0, r1, s0, s1, t0, t1 = coefficients
    C = np.array([r0, r1+s0, s1+t0-p0/4, t1-p1/4, -p2/4])
    W = np.array([s0, s1+2*t0, 2*t1-p1/4, -p2/2])
    return C, W, np.array([p0, p1, p2])


def value(poly, x, order=0):
    return float(np.polynomial.polynomial.polyval(
        x, np.polynomial.polynomial.polyder(poly, order)))


def local_root_quantities(coefficients, xi):
    C, W, A = polynomials(coefficients)
    Cp = np.polynomial.polynomial.polyder(C)
    B = np.polynomial.polynomial.polysub(Cp, W)
    gamma, ww = value(C, xi, 1), value(W, xi)
    answer = dict(xi=float(xi), C=value(C, xi), C_prime=gamma,
                  C_second=value(C, xi, 2), W=ww, W_prime=value(W, xi, 1),
                  W_over_C_prime=None, R26_exponent=None,
                  R26_jet=None, R26_K=None,
                  root_and_nonzero_jet_certified=False)
    if gamma != 0:
        ratio = ww/gamma
        answer['W_over_C_prime'] = float(ratio)
        if 9-32*ratio >= 0:
            answer['R26_exponent'] = float((1+np.sqrt(9-32*ratio))/2)
    bb = value(B, xi)
    if bb != 0 and ww != 0 and 2*ww+gamma != 0:
        a = -value(A, xi)/(2*bb)
        b = (value(A, xi, 1)+(value(A, xi)+2*value(B, xi, 1))*a)/(2*ww)
        K = (value(A, xi, 2)+(2*value(A, xi, 1)+2*value(B, xi, 2))*a
             +(value(A, xi)+2*value(B, xi, 1)-2*value(W, xi, 1))*b)
        c = K/(2*ww+gamma)
        answer.update(R26_jet=[1., float(a), float(b), float(c)], R26_K=float(K),
                      R26_L_quadratic_coefficient=float(-gamma*c/2))
    return answer


def physical_roots(g, imaginary_tolerance=1e-8):
    C, _, _ = polynomials(g['coefficients'])
    answer = []
    for z in np.polynomial.polynomial.polyroots(C):
        if abs(z.imag) > imaginary_tolerance*max(1., abs(z.real)):
            continue
        x = float(z.real)
        denominators = x+g['omega']
        side = ('positive' if np.min(denominators) > 0 else
                'negative' if np.max(denominators) < 0 else 'pole_band')
        row = local_root_quantities(g['coefficients'], x)
        row.update(side_by_validation_samples=side,
                   denominator_min_sample=float(np.min(denominators)),
                   denominator_max_sample=float(np.max(denominators)),
                   continuous_physical_half_line_certified=False)
        answer.append(row)
    return answer


def hinge_map(raw, n_guard, log_bound):
    """Differentiate smooth observables first, then the selected hinge branch."""
    raw = np.asarray(raw)
    # Two equations, one derivative floor, n pole gaps, n log h, n speed gaps.
    a, b, c = 3, 3+n_guard, 3+2*n_guard
    eq = raw[:2]
    derivative_gap = raw[2:3]
    physical_gap = raw[a:b]
    logh = raw[b:c]
    speed_gap = raw[c:]
    residual = np.r_[eq, 10*np.maximum(derivative_gap, 0),
                     10*np.maximum(physical_gap, 0),
                     10*np.maximum(abs(logh)-log_bound, 0),
                     10*np.maximum(speed_gap, 0)]
    derivative = np.r_[np.ones(2), 10*(derivative_gap > 0),
                       10*(physical_gap > 0),
                       10*np.sign(logh)*(abs(logh) > log_bound),
                       10*(speed_gap > 0)]
    return residual, derivative


def diagnostic(g, n, coefficient_scales, xi, side, target, xi_scale,
               derivative_scale, derivative_sign, derivative_floor, physical_gap):
    row = closed.diagnostic(g, n, coefficient_scales)
    local = local_root_quantities(g['coefficients'], xi)
    den = xi+g['omega']
    direction = 1 if side == 'positive' else -1
    same_sign = bool(np.all(direction*den > 0))
    raw_core = [local['C']/(derivative_scale*xi_scale),
                (local['W']-target*local['C_prime'])/derivative_scale]
    row.update(frozen_candidate_xi=float(xi), root_quantities_at_frozen_xi=local,
               smooth_core_residual=raw_core,
               smooth_core_residual_l2=float(np.linalg.norm(raw_core)),
               frozen_ratio_target=float(target), frozen_xi_scale=float(xi_scale),
               frozen_derivative_scale=float(derivative_scale),
               derivative_sign=int(derivative_sign),
               signed_derivative_in_reference_units=float(
                   derivative_sign*local['C_prime']/derivative_scale),
               derivative_guard_passed=bool(
                   derivative_sign*local['C_prime']/derivative_scale >= derivative_floor),
               physical_side=side, denominator_min_sample=float(np.min(den)),
               denominator_max_sample=float(np.max(den)),
               physical_gap_in_reference_units_min_sample=float(np.min(direction*den)/xi_scale),
               physical_gap_guard_passed_at_samples=bool(np.min(direction*den)/xi_scale >= physical_gap),
               physical_half_line_at_all_validation_nodes=same_sign,
               physical_u_range_sample=None,
               all_real_polynomial_roots_diagnostic=physical_roots(g),
               frozen_xi_is_not_replaced_by_recomputed_root=True,
               continuous_physical_half_line_certified=False,
               exact_simple_C_root_certified=False,
               exact_negative_root_ratio_certified=False,
               complete_profile_constructed=False,
               finite_isometric_family_constructed=False)
    if same_sign:
        uu = np.sqrt(g['v'])/den
        row['physical_u_range_sample'] = [float(np.min(uu)), float(np.max(uu))]
    return row


def solve_case(source, source_index, source_hash, args, side):
    started = time.monotonic()
    q = int(source['q'])
    initial = np.asarray(source[args.parameter_state+'_parameters'], dtype=float)
    if len(initial) != args.modes+4:
        raise ValueError('saved parameter vector does not match the requested mode count')
    g0 = closed.geometry(initial, q, args.modes, args.theta_n)
    possible = [row for row in physical_roots(g0)
                if row['side_by_validation_samples'] == side and row['C_prime'] != 0]
    if not possible:
        return dict(q=q, side=side, source_design_index=source_index,
                    skipped=True, reason='no sampled physical simple real C root in this saved seed',
                    all_real_roots=physical_roots(g0), task_complete=False)
    # A deterministic nearest-to-pole physical root; all roots remain reported.
    chosen = min(possible, key=lambda row: abs(row['xi']))
    xi0 = chosen['xi']
    xi_scale = max(1., float(np.ptp(g0['omega'])), abs(xi0))
    derivative_scale = abs(chosen['C_prime'])
    derivative_sign = 1 if chosen['C_prime'] > 0 else -1
    coefficient_scales = np.maximum(1., abs(g0['coefficients'][closed.INDEPENDENT]))
    sample = np.arange(args.guard_angles)*args.theta_n//args.guard_angles
    sign = 1 if side == 'positive' else -1
    x0 = np.r_[initial, xi0/xi_scale]

    def raw(x):
        g = closed.geometry(x[:-1], q, args.modes, args.theta_n)
        xi = x[-1]*xi_scale
        C, W, _ = polynomials(g['coefficients'])
        derivative = value(C, xi, 1)
        return np.r_[value(C, xi)/(derivative_scale*xi_scale),
                     (value(W, xi)-args.target_ratio*derivative)/derivative_scale,
                     args.derivative_floor-derivative_sign*derivative/derivative_scale,
                     args.physical_gap-sign*(xi+g['omega'][sample])/xi_scale,
                     .5*np.log(g['v'][sample]),
                     1-g['data']['sphere_speed'][sample]/args.speed_floor]

    evaluations = [0]
    best = [np.inf]
    checkpoint = args.out.with_name(args.out.stem+f'-q{q}-{side}-checkpoint.json')

    def residual(x):
        answer = hinge_map(raw(x), len(sample), args.logh_bound)[0]
        if not np.all(np.isfinite(answer)):
            raise ValueError('nonfinite physical-root design residual')
        evaluations[0] += 1
        score = float(np.linalg.norm(answer))
        if score < best[0]:
            best[0] = score
            if evaluations[0] == 1 or evaluations[0] % 20 == 0:
                checkpoint.parent.mkdir(parents=True, exist_ok=True)
                checkpoint.write_text(json.dumps(dict(
                    q=q, side=side, evaluation=evaluations[0], parameters=x[:-1].tolist(),
                    xi=float(x[-1]*xi_scale), residual_l2=score,
                    incomplete_solver_checkpoint=True, task_complete=False), indent=2,
                    allow_nan=False)+'\n')
        return answer

    def jacobian(x):
        derivative = hinge_map(raw(x), len(sample), args.logh_bound)[1]
        return derivative[:, None]*closed.absolute_jacobian(raw, x)

    # These are design bounds, not a claim that the fixed metric is preserved.
    lo = np.r_[-1.2, .05, -.8, -.7, .76, np.full(args.modes-1, -.7),
               1e-5 if side == 'positive' else -args.xi_bound]
    hi = np.r_[1.2, 1.8, .8, .7, 2.1, np.full(args.modes-1, .7),
               args.xi_bound if side == 'positive' else -1e-5]
    if not np.all((x0 >= lo) & (x0 <= hi)):
        raise ValueError('saved physical seed is outside the declared design box')
    fit = least_squares(residual, x0, jac=jacobian, bounds=(lo, hi),
                        max_nfev=args.max_nfev, ftol=1e-12, xtol=1e-12,
                        gtol=1e-10, x_scale='jac')
    final = closed.geometry(fit.x[:-1], q, args.modes, args.theta_n)
    xi = float(fit.x[-1]*xi_scale)
    frozen = dict(tilt=final['tilt'], normalization=final['normalization'])
    validations = [diagnostic(
        closed.geometry(fit.x[:-1], q, args.modes, n, frozen), n,
        coefficient_scales, xi, side, args.target_ratio, xi_scale,
        derivative_scale, derivative_sign, args.derivative_floor, args.physical_gap)
        for n in args.validation_n]

    direction = np.random.default_rng(20261114).normal(size=len(fit.x))
    direction /= np.linalg.norm(direction)
    smooth_jac = closed.absolute_jacobian(raw, fit.x)
    h = 2e-6
    rp, rm = raw(fit.x+h*direction), raw(fit.x-h*direction)
    observed = (rp-rm)/(2*h)
    predicted = smooth_jac@direction
    hp, dp = hinge_map(rp, len(sample), args.logh_bound)
    hm, dm = hinge_map(rm, len(sample), args.logh_bound)
    current = hinge_map(raw(fit.x), len(sample), args.logh_bound)[1]
    observed_hinge = (hp-hm)/(2*h)
    predicted_hinge = current*(smooth_jac@direction)

    def difference(a, b):
        return float(np.linalg.norm(a-b)/max(np.linalg.norm(b), 1e-30))

    return dict(q=q, side=side, skipped=False,
                source_report_sha256=source_hash, source_design_index=source_index,
                source_parameter_state=args.parameter_state,
                initial_parameters=initial.tolist(), final_parameters=fit.x[:-1].tolist(),
                initial_root=chosen, frozen_final_xi=xi,
                parameter_order=source.get('parameter_order'),
                design_variable_last='xi divided by the frozen xi scale',
                bounds_lower=lo.tolist(), bounds_upper=hi.tolist(),
                frozen_xi_scale=xi_scale, frozen_derivative_scale=derivative_scale,
                derivative_sign=derivative_sign,
                frozen_coefficient_scales=coefficient_scales.tolist(),
                frozen_validation_data=frozen,
                initial=diagnostic(g0, args.theta_n, coefficient_scales, xi0, side,
                    args.target_ratio, xi_scale, derivative_scale, derivative_sign,
                    args.derivative_floor, args.physical_gap),
                validation=validations,
                solver=dict(success=bool(fit.success), message=str(fit.message),
                    nfev=int(fit.nfev), residual_evaluations=evaluations[0],
                    optimality=float(fit.optimality),
                    initial_residual_l2=float(np.linalg.norm(hinge_map(raw(x0),len(sample),args.logh_bound)[0])),
                    final_residual_l2=float(np.linalg.norm(fit.fun)),
                    elapsed_seconds=float(time.monotonic()-started)),
                derivative_audit=dict(method='smooth central columns then exact current hinge branch',
                    column_step='2e-5*max(1,abs(x[j]))', directional_step=h,
                    core_direction_relative_difference=difference(predicted[:2], observed[:2]),
                    all_smooth_direction_relative_difference=difference(predicted, observed),
                    current_hinge_direction_relative_difference=difference(predicted_hinge,observed_hinge),
                    directional_probe_branch_switch_count=int(np.count_nonzero(dp != dm)),
                    smooth_core_jacobian_singular_values=np.linalg.svd(smooth_jac[:2],compute_uv=False).tolist()),
                actual_geometry_design_not_fixed_metric_refinement=True,
                no_simple_fourth_order_double_tail_profile_is_being_fitted=True,
                exact_negative_root_ratio_proved=False,
                complete_profile_constructed=False,
                finite_isometric_family_constructed=False,
                reach_lower_certified=False, task_complete=False)


def developer_check():
    # Synthetic R22 coefficients only; do not call any real geometry here.
    c = np.array([-8/3, 0., 0., 87/32, 2., 0., 87/32, -55/32, 2/3, -1/3, 0.])
    C, W, A = polynomials(c)
    assert np.allclose(C, [0., 1., 1., 0., 0.])
    assert np.allclose(W, [-55/32, 0., 0., 0.])
    assert np.allclose(A, [-8/3, 0., 0.])
    root = local_root_quantities(c, 0.)
    exact = [1., 128/261, -8192/43065, 524288/5038605]
    assert np.max(abs(np.array(root['R26_jet'])-exact)) < 2e-15
    assert root['W_over_C_prime'] == -55/32 and root['R26_exponent'] == 4.5
    raw = np.r_[.2, -.3, .1, [-.1, .2], [.9, -.9], [-1., .3]]
    res, branch = hinge_map(raw, 2, .8)
    assert np.allclose(res, [.2, -.3, 1., 0., 2., 1., 1., 0., 3.])
    assert np.array_equal(branch, [1., 1., 10., 0., 10., 10., -10., 0., 10.])
    fake = dict(coefficients=c, omega=np.array([1., 2.]))
    roots = physical_roots(fake)
    assert any(abs(row['xi']) < 1e-12 and row['side_by_validation_samples'] == 'positive' for row in roots)
    print(json.dumps(dict(developer_check=True, synthetic_polynomials_passed=True,
                          synthetic_hinge_branch_passed=True,
                          R26_jet_max_error=float(np.max(abs(np.array(root['R26_jet'])-exact))),
                          geometry_evaluated=False, optimizer_called=False), allow_nan=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--q', type=int, nargs='+', default=[2])
    parser.add_argument('--sides', choices=['positive','negative'], nargs='+', default=['positive','negative'])
    parser.add_argument('--parameter-state', choices=['initial','final'], default='initial')
    parser.add_argument('--modes', type=int, default=12)
    parser.add_argument('--theta-n', type=int, default=768)
    parser.add_argument('--validation-n', type=int, nargs='+', default=[768,1536,3072])
    parser.add_argument('--guard-angles', type=int, default=192)
    parser.add_argument('--max-nfev', type=int, default=180)
    parser.add_argument('--target-ratio', type=float, default=-1.75)
    parser.add_argument('--derivative-floor', type=float, default=.1)
    parser.add_argument('--physical-gap', type=float, default=.01)
    parser.add_argument('--logh-bound', type=float, default=1.)
    parser.add_argument('--speed-floor', type=float, default=.08)
    parser.add_argument('--xi-bound', type=float, default=4.)
    parser.add_argument('--developer-check', action='store_true')
    args = parser.parse_args()
    if args.developer_check:
        developer_check()
        return
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        parser.error('run research designs only in this public repository Actions')
    if args.input is None or args.out is None:
        parser.error('input and out are required')
    if not 16 <= args.guard_angles <= args.theta_n:
        parser.error('guard-angle count must lie between 16 and theta-n')
    if not args.derivative_floor > 0 or not args.physical_gap > 0:
        parser.error('nonzero derivative and physical gap guards are required')
    data = json.loads(args.input.read_text())
    source_hash = hashlib.sha256(args.input.read_bytes()).hexdigest()
    report = dict(schema='physical-C-root-ratio-design-v1',
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256=source_hash,
                  arguments=vars(args)|dict(input=str(args.input),out=str(args.out)),
                  designs=[], task_complete=False)
    for q in args.q:
        matching = [(j,row) for j,row in enumerate(data['designs']) if row['q']==q]
        if len(matching) != 1:
            raise ValueError('need exactly one saved design per requested q')
        index, source = matching[0]
        for side in args.sides:
            result = solve_case(source, index, source_hash, args, side)
            report['designs'].append(result)
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
            print(json.dumps(dict(q=q, side=side, skipped=result['skipped'],
                solver=result.get('solver'), final=(None if result['skipped'] else
                result['validation'][-1]['root_quantities_at_frozen_xi'])), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

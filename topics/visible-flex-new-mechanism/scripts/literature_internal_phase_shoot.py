#!/usr/bin/env python3
"""Public-Actions diagnostics for R13's abstract local complex phase branch.

The nine coefficients are the exact rational example in R13; they have NOT
been realized by a closed geometric base.  Local moments start at the stated
constants, not at a manufactured zero right tail.  Finite collocation and
shooting outputs do not prove compact support or a finite isometric family.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import chebyshev as ch
from scipy.fft import dct
from scipy.integrate import solve_ivp
from scipy.linalg import lu_factor, lu_solve

SIGMA = 4/17
YBAR = np.array([25/24, 25/6, 25/2, 25.])
JANCHOR = np.array([44/9, 3/4, -14/9])


def polynomial_multiply(a, b):
    """Small polynomials whose coefficients may be vectors over collocation nodes."""
    answer = [0]*(len(a)+len(b)-1)
    for j, u in enumerate(a):
        for k, v in enumerate(b):
            answer[j+k] = answer[j+k]+u*v
    return answer


def horner(coefficients, x):
    answer = coefficients[-1]
    for value in coefficients[-2::-1]:
        answer = answer*x+value
    return answer


def normal_terms(x, V):
    """Return ell and G in x^2 v'=sigma*v+G, without small-x division.

    V has four rows.  The discarded R polynomial coefficients 0 and 1 are
    exactly 0 and 8*V[3].  Only coefficients of degree >=2 form Rhat.
    """
    y0, y1, y2, y3 = [V[j]+YBAR[j] for j in range(4)]
    offset = (-2*V[2]-4*x/3+x*x*(2*y0-10*y1+4*y2)-4*x**3/3
              +x**4*(-4*y0+4*y1-2*y2))
    ell = -34+offset
    C = [1, 0, -2, 0, 1]
    s_square = [4, 4*y3, y3*y3]
    M = [16, -52, -40, -32*y1-4*y2, -16/3, -16*y0+16*y1-8*y2]
    first = polynomial_multiply(C, s_square)
    second = polynomial_multiply(M, [2, y3])
    third = polynomial_multiply([1, 2, y2], [1, 2, y2])
    R = [-2*first[j]+second[j]-(24*third[j] if j < len(third) else 0)
         for j in range(len(first))]
    Rhat = horner(R[2:], x)
    G = -x*y3-x*Rhat/ell-SIGMA*V[3]*offset/ell
    return ell, G


def coefficients(x):
    C = (1-x*x)**2
    W = x+2*x**3
    A1 = 2-4*x*x
    A2 = -5*x+2*x**3
    return C, W, A1, A2


def raw_expressions(x, q, p, r, s):
    C, W, A1, A2 = coefficients(x)
    L = A1*q+2*A2*p-2*C*r
    M = -16*x*q+(-32+16*x*x)*p-4*W*r
    R = -2*C*s*s+M*s-24*r*r
    scale = abs(A1*q)+2*abs(A2*p)+2*abs(C*r)
    return L, R, scale


def reconstruct(x, V):
    y0, y1, y2, y3 = [V[j]+YBAR[j] for j in range(4)]
    q = 1-x/2+x*x/2+x**3/3+x**4*y0
    p = -.5+x+x*x+x**3*y1
    r = 1+2*x+x*x*y2
    s = 2+x*y3
    return np.asarray([q, p, r, s])


def lobatto(n, length):
    j = np.arange(n+1)
    coordinate = -np.cos(np.pi*j/n)
    t = length*(coordinate+1)/2
    weights = (-1.)**j
    weights[[0, -1]] *= .5
    difference = t[:, None]-t[None, :]
    np.fill_diagonal(difference, 1.)
    D = weights[None, :]/weights[:, None]/difference
    np.fill_diagonal(D, 0.)
    D[np.diag_indices_from(D)] = -np.sum(D, axis=1)
    return coordinate, t, D


def cheb_coefficients(values):
    n = len(values)-1
    result = (dct(np.real(values[::-1]), type=1)
              +1j*dct(np.imag(values[::-1]), type=1))/n
    result[[0, -1]] *= .5
    return result


def cheb_anchor_integral(integrand, signed_length, initial=0.):
    answer = ch.chebint(integrand)*signed_length/2
    answer[0] += initial-ch.chebval(-1., answer)
    return answer


def field_coefficients(V_coefficients, signed_length):
    x = np.array([signed_length/2, signed_length/2])
    x2 = ch.chebmul(x, x)
    x3 = ch.chebmul(x2, x)
    x4 = ch.chebmul(x3, x)
    Y = [c.copy() for c in V_coefficients]
    for j in range(4):
        Y[j][0] += YBAR[j]
    P = ch.chebadd([1.], ch.chebadd(-x/2, ch.chebadd(x2/2, x3/3)))
    q = ch.chebadd(P, ch.chebmul(x4, Y[0]))
    p = ch.chebadd([-.5], ch.chebadd(x, ch.chebadd(x2, ch.chebmul(x3, Y[1]))))
    r = ch.chebadd([1.], ch.chebadd(2*x, ch.chebmul(x2, Y[2])))
    s = ch.chebadd([2.], ch.chebmul(x, Y[3]))
    r2, p2 = ch.chebmul(r, r), ch.chebmul(p, p)
    integrands = [r2, ch.chebmul(x, r2), ch.chebadd(ch.chebmul(x2, r2), 2*p2)]
    moments = [cheb_anchor_integral(-f, signed_length, JANCHOR[j])
               for j, f in enumerate(integrands)]
    return [q, p, r, s], moments


def period_value(x, state):
    q, p, r, s, J0, J1, J2 = state
    C, W, A1, A2 = coefficients(x)
    return (4*x*q*q+A1*q*p+A2*p*p+(1-x*x/2)*J0
            -4*x*J1+(2.5+x*x)*J2)


def complex_pairs(array):
    array = np.asarray(array)
    return np.stack([array.real, array.imag], axis=-1).tolist()


def local_design(n, length, side, eta, args):
    started = time.monotonic()
    coordinate, t, D = lobatto(n, length)
    identity = np.eye(n+1)
    euler = [np.linalg.solve(t[:, None]*D+m*identity, identity) for m in (2, 3, 4)]
    A2, A3, A4 = euler

    def regular_variables(v):
        v2 = A2 @ v
        v1 = A3 @ v2
        v0 = A4 @ v1
        return np.stack([v0, v1, v2, v])

    fast = t[:, None]**2*D-side*SIGMA*identity
    fast[0] = 0.; fast[0, 0] = 1.
    if side == 1:
        fast[-1] = 0.; fast[-1, -1] = 1.
    factorization = lu_factor(fast.astype(complex))
    v = np.zeros(n+1, dtype=complex)
    last_change = np.inf
    weighted_change = np.inf
    history = []
    failure = None
    converged = False
    for iteration in range(args.max_iterations):
        V = regular_variables(v)
        ell, G = normal_terms(side*t, V)
        if np.min(abs(ell)) < args.local_ell_floor or not np.all(np.isfinite(G)):
            failure = 'local ell guard or nonfinite residual'
            break
        rhs = side*G
        rhs[0] = 0.
        if side == 1:
            rhs[-1] = eta*length
        candidate = lu_solve(factorization, rhs)
        candidate[0] = 0.
        if not np.all(np.isfinite(candidate)):
            failure = 'nonfinite Picard iterate'
            break
        last_change = float(np.max(abs(candidate-v)))
        weighted_change = float(np.max(abs(candidate[1:]-v[1:])/t[1:]))
        v = candidate
        if iteration < 6 or iteration % 20 == 19:
            history.append(dict(iteration=iteration+1, maximum_change=last_change,
                                weighted_maximum_change=weighted_change))
        if last_change <= args.picard_tolerance*max(length, float(np.max(abs(v)))):
            converged = True
            break
        if np.max(abs(v)) > args.local_v_bound:
            failure = 'local v guard'
            break
    if failure is not None:
        return dict(n=n, length=length, side=side,
                    eta=[float(np.real(eta)), float(np.imag(eta))],
                    iterations=iteration+1, failure=failure, history=history,
                    picard_converged=False, numerical_local_gate_passed=False,
                    validation=[dict(skipped=True, reason=failure)],
                    elapsed_seconds=time.monotonic()-started), None
    V = regular_variables(v)
    V_coeff = [cheb_coefficients(row) for row in V]
    fields, moments = field_coefficients(V_coeff, side*length)
    validation = []
    for multiplier in (2, 4):
        cdense = np.linspace(-1., 1., multiplier*n+3)
        tdense = length*(cdense+1)/2
        xdense = side*tdense
        Vdense = np.array([ch.chebval(cdense, row) for row in V_coeff])
        Vprime = np.array([ch.chebval(cdense, ch.chebder(row))*2/length
                          for row in V_coeff])
        ell, G = normal_terms(xdense, Vdense)
        fast_residual = tdense**2*Vprime[3]-side*(SIGMA*Vdense[3]+G)
        euler_residuals = np.array([
            tdense*Vprime[0]-(Vdense[1]-4*Vdense[0]),
            tdense*Vprime[1]-(Vdense[2]-3*Vdense[1]),
            tdense*Vprime[2]-(Vdense[3]-2*Vdense[2])])
        state = np.array([ch.chebval(cdense, c) for c in fields+moments])
        L, R, scale = raw_expressions(xdense, *state[:4])
        fourth = YBAR[3]+Vdense[3]+tdense*Vprime[3]
        direct_Q = L*fourth+R
        factored_Q = side*xdense*ell*fast_residual
        validation.append(dict(points=len(cdense),
            fast_normal_form_max=float(np.max(abs(fast_residual))),
            fast_normal_form_over_length=float(np.max(abs(fast_residual))/length),
            three_euler_residual_max=float(np.max(abs(euler_residuals))),
            direct_Q_max=float(np.max(abs(direct_Q))),
            direct_vs_factored_Q_max=float(np.max(abs(direct_Q-factored_Q))),
            local_complete_O_max=float(np.max(abs(period_value(xdense, state)))),
            minimum_absolute_ell=float(np.min(abs(ell))),
            maximum_imaginary_q=float(np.max(abs(state[0].imag))),
            maximum_imaginary_third_derivative=float(np.max(abs(state[3].imag))),
            minimum_sampled_normalized_L_away_from_zero=float(np.min(
                abs(L[1:])/np.maximum(scale[1:], 1e-300))),
            evaluation_uses_frozen_collocation_coefficients=True))
    endpoint = np.array([ch.chebval(1., c) for c in fields+moments])
    gate = bool(converged and failure is None
                and validation[-1]['fast_normal_form_over_length'] < args.local_gate
                and validation[-1]['three_euler_residual_max'] < args.local_gate
                and validation[-1]['local_complete_O_max'] < args.local_gate)
    report = dict(n=n, length=length, side=side,
                  eta=[float(np.real(eta)), float(np.imag(eta))],
                  positive_terminal_v=[float(np.real(eta*length)), float(np.imag(eta*length))]
                                      if side == 1 else None,
                  negative_side_uses_bounded_condition_without_terminal_parameter=side == -1,
                  iterations=iteration+1, final_change=last_change,
                  final_weighted_change=weighted_change,
                  picard_converged=converged,
                  iteration_limit_reached=bool(not converged),
                  failure=failure, history=history, validation=validation,
                  numerical_local_gate_passed=gate,
                  endpoint_q_jets_and_local_J=complex_pairs(endpoint),
                  local_moments_are_anchored_at_x_zero=JANCHOR.tolist(),
                  local_moments_are_not_assumed_right_tail_integrals=True,
                  endpoint_x=side*length,
                  elapsed_seconds=time.monotonic()-started)
    return report, endpoint


def shoot(start, endpoint, side, args):
    gamma = float(np.max(abs(endpoint.imag)))
    if gamma == 0:
        gamma = 1.
    initial = np.r_[endpoint.real, endpoint.imag/gamma]
    initial_L, _, initial_scale = raw_expressions(start, *endpoint[:4])
    initial_gap = float(abs(initial_L)/max(float(initial_scale), 1e-300))
    if initial_gap <= args.shoot_L_floor or np.max(abs(endpoint[:4])) >= args.shoot_jet_bound:
        return dict(success=False, status=-2, message='initial shooting guard failed',
                    start_x=start, requested_end_x=side*args.outer_stop,
                    actual_end_x=start, reached_requested_end=False,
                    initial_normalized_L=initial_gap,
                    final_q_jets_and_local_J=complex_pairs(endpoint)), endpoint

    def unpack(y):
        return y[:7]+1j*gamma*y[7:]

    def rhs(x, y):
        q, p, r, s, J0, J1, J2 = unpack(y)
        L, R, _ = raw_expressions(x, q, p, r, s)
        derivative = np.array([p, r, s, -R/L, -r*r, -x*r*r, -x*x*r*r-2*p*p])
        return np.r_[derivative.real, derivative.imag/gamma]

    def small_L(x, y):
        L, R, scale = raw_expressions(x, *unpack(y)[:4])
        return float(abs(L)/max(float(scale), 1e-300)-args.shoot_L_floor)

    def large_jet(x, y):
        return float(args.shoot_jet_bound-np.max(abs(unpack(y)[:4])))

    small_L.terminal = large_jet.terminal = True
    small_L.direction = large_jet.direction = -1
    atol = np.r_[np.full(7, args.shoot_atol),
                 np.maximum(abs(initial[7:])*args.shoot_rtol*.01, 1e-28)]
    try:
        result = solve_ivp(rhs, [start, side*args.outer_stop], initial, method='DOP853',
                           rtol=args.shoot_rtol, atol=atol, max_step=args.max_step,
                           events=[small_L, large_jet], dense_output=True)
    except (ValueError, FloatingPointError, ZeroDivisionError) as error:
        return dict(success=False, status=-3,
                    message=f'{type(error).__name__}: {error}',
                    start_x=start, requested_end_x=side*args.outer_stop,
                    actual_end_x=start, reached_requested_end=False,
                    recovered_partial_integration=False,
                    final_q_jets_and_local_J=complex_pairs(endpoint)), endpoint
    xs = np.linspace(start, result.t[-1], args.shoot_samples)
    states = unpack(result.sol(xs))
    L, R, scale = raw_expressions(xs, *states[:4])
    periods = period_value(xs, states)
    terminal = states[:, -1]
    reached = bool(result.status == 0 and abs(result.t[-1]-side*args.outer_stop) < 1e-12)
    return dict(success=bool(result.success), status=int(result.status), message=str(result.message),
                start_x=start, requested_end_x=side*args.outer_stop,
                actual_end_x=float(result.t[-1]), reached_requested_end=reached,
                nfev=int(result.nfev), stored_dense_samples=len(xs),
                imaginary_state_scaling=gamma,
                normalized_L_floor=args.shoot_L_floor,
                events=dict(small_normalized_L=result.t_events[0].tolist(),
                            large_jet=result.t_events[1].tolist()),
                minimum_sampled_normalized_L=float(np.min(abs(L)/np.maximum(scale, 1e-300))),
                maximum_q_jet=float(np.max(abs(states[:4]))),
                maximum_imaginary_q=float(np.max(abs(states[0].imag))),
                complete_O_max=float(np.max(abs(periods))),
                initial_complete_O=complex_pairs(periods[0]),
                final_q_jets_and_local_J=complex_pairs(terminal),
                q_jets_at_truncated_outer_endpoint_max=float(np.max(abs(terminal[:4]))),
                outer_local_J_max=float(np.max(abs(terminal[4:]))),
                right_tail_zero_condition_imposed=False,
                endpoint_is_inside_target_interval_not_at_flat_boundary=True,
                sampled_path_and_events_are_not_continuous_certificates=True), terminal


def developer_check():
    # Fixed finite polynomial/interface checks only; no nonlinear solve or shot.
    coordinate, t, D = lobatto(16, .2)
    derivative_error = float(np.max(abs(D @ (1+2*t-3*t*t)-(2-6*t))))
    assert derivative_error < 1e-10
    c = cheb_coefficients((1+2j)+(3-1j)*coordinate+2*coordinate**2)
    assert np.max(abs(ch.chebval(coordinate, c)-((1+2j)+(3-1j)*coordinate+2*coordinate**2))) < 1e-12
    integral = cheb_anchor_integral(np.array([1., 0., 1.]), .2)
    assert abs(ch.chebval(-1., integral)) < 1e-14
    assert abs(ch.chebval(1., integral)-(.2*2/3)) < 1e-14
    errors = []
    for x in [.03, -.07]:
        V = np.array([.03, -.07, .05, .11], dtype=complex)*(1+.3j)
        ell, G = normal_terms(x, V)
        q, p, r, s = reconstruct(x, V)
        L, R, _ = raw_expressions(x, q, p, r, s)
        y3 = YBAR[3]+V[3]
        F = SIGMA*V[3]+G
        errors.append(max(abs(L-x*x*ell), abs(R+x*x*ell*y3+x*ell*F)))
    assert max(errors) < 1e-10
    v = np.array([0., 0., 0., 0.])
    eps = 1e-6
    v[3] = eps
    _, g = normal_terms(0., v)
    assert abs(g) < 1e-12
    print(json.dumps(dict(developer_check=True, no_profile_solve=True,
                          no_geometric_design=True, no_ode_integration=True,
                          synthetic_D_polynomial_error=derivative_error,
                          synthetic_normal_form_identity_errors=list(map(float, errors)))))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n', type=int, nargs='+', default=[96, 192])
    parser.add_argument('--length', type=float, nargs='+', default=[.003, .006])
    parser.add_argument('--eta-imag', type=float, nargs='+', default=[.001, .1])
    parser.add_argument('--max-iterations', type=int, default=300)
    parser.add_argument('--picard-tolerance', type=float, default=2e-12)
    parser.add_argument('--local-gate', type=float, default=2e-7)
    parser.add_argument('--local-ell-floor', type=float, default=1.)
    parser.add_argument('--local-v-bound', type=float, default=50.)
    parser.add_argument('--outer-stop', type=float, default=.995)
    parser.add_argument('--shoot-L-floor', type=float, default=1e-8)
    parser.add_argument('--shoot-jet-bound', type=float, default=1e6)
    parser.add_argument('--shoot-rtol', type=float, default=1e-9)
    parser.add_argument('--shoot-atol', type=float, default=1e-11)
    parser.add_argument('--max-step', type=float, default=.002)
    parser.add_argument('--shoot-samples', type=int, default=257)
    parser.add_argument('--skip-shoot', action='store_true')
    parser.add_argument('--out', type=Path)
    parser.add_argument('--developer-check', action='store_true')
    args = parser.parse_args()
    if args.developer_check:
        developer_check(); return
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        parser.error('run profile calculations in the authorized public repository Actions')
    if args.out is None or min(args.n) < 24 or not all(0 < x < args.outer_stop < 1 for x in args.length):
        parser.error('need an output, n >= 24, and 0 < local lengths < outer stop < 1')
    output = dict(schema='literature-internal-phase-volterra-shoot-v1',
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  arguments=vars(args) | {'out': str(args.out)},
                  exact_abstract_coefficients=[2, 0, -4, 1, 0, 0, -4, 2.5, 0],
                  coefficients_are_not_from_a_realized_geometric_base=True,
                  local_analytic_existence_reference='results/R13-local-smooth-complex-phase-opening.md',
                  endpoint_states_are_numerical_not_existence_certificates=True,
                  local_cases=[], shooting_pairs=[],
                  global_compact_profile_constructed=False,
                  three_complex_total_moments_solved=False,
                  finite_isometric_family_proved=False, task_complete=False)
    last = {}
    for length in args.length:
        for n in args.n:
            left, left_state = local_design(n, length, -1, 0j, args)
            output['local_cases'].append(left)
            last[(length, n, -1, 0.)] = (left, left_state)
            for imag in args.eta_imag:
                right, right_state = local_design(n, length, 1, 1j*imag, args)
                output['local_cases'].append(right)
                last[(length, n, 1, imag)] = (right, right_state)
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
            print(json.dumps(dict(length=length, n=n,
                recent=[dict(side=r['side'], eta=r['eta'], gate=r['numerical_local_gate_passed'],
                             validation=r['validation'][-1])
                        for r in output['local_cases'][-(1+len(args.eta_imag)):]])), flush=True)
        if args.skip_shoot:
            continue
        n = max(args.n)
        left, left_state = last[(length, n, -1, 0.)]
        left_shot = None
        left_end = None
        if left['numerical_local_gate_passed']:
            left_shot, left_end = shoot(-length, left_state, -1, args)
        for imag in args.eta_imag:
            right, right_state = last[(length, n, 1, imag)]
            if not right['numerical_local_gate_passed'] or left_shot is None:
                output['shooting_pairs'].append(dict(length=length, n=n, eta_imag=imag,
                    skipped=True, reason='a local numerical gate failed'))
                continue
            right_shot, right_end = shoot(length, right_state, 1, args)
            both = left_shot['reached_requested_end'] and right_shot['reached_requested_end']
            output['shooting_pairs'].append(dict(length=length, n=n, eta_imag=imag,
                left=left_shot, right=right_shot,
                both_reached_requested_inner_endpoints=bool(both),
                integral_across_computed_segments=complex_pairs(left_end[4:]-right_end[4:]),
                this_is_not_the_total_moment_on_minus_one_to_one=True,
                right_tail_integral_constants_match_zero=False))
            args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()

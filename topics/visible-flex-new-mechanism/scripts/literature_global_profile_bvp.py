#!/usr/bin/env python3
"""Global C2-profile BVP on [-1,1] with exact fourth-order endpoint factors.

The coefficient family is abstract and is not claimed to arise from a closed
geometric base.  Trial functions combine global polynomials and an interior
C-infinity window; a finite collocation fit is not an exact profile.  All
research optimization is restricted to the public repository Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import chebyshev as cheb, legendre as leg, polynomial as poly
from scipy.linalg import eigh
from scipy.optimize import least_squares

from literature_closed_codesign import absolute_jacobian, jacobian_direction_check
from literature_internal_phase_certificate import add, scale, multiply, derivative, trim


def divide_exact(numerator, denominator):
    remainder = trim(numerator)
    answer = [F(0)]*max(1, len(remainder)-len(denominator)+1)
    while len(remainder) >= len(denominator) and any(remainder):
        n = len(remainder)-len(denominator)
        value = remainder[-1]/denominator[-1]
        answer[n] = value
        subtract = [F(0)]*n+scale(denominator, -value)
        remainder = add(remainder, subtract)
    if any(remainder):
        raise ArithmeticError('endpoint factor did not divide an operator coefficient')
    return trim(answer)


def operator_tensor():
    """Exact coefficients of Q[(1-x^2)^4 P]/(1-x^2)^4.

    Parameter order is (1,b,c,d,D).  Each coefficient of P^(i)P^(j)
    is divided separately using Fraction; no sampled small-number division.
    """
    base = [F(1), F(0), F(-1)]
    weight = multiply(multiply(base, base), multiply(base, base))
    q_ops = [[scale(derivative(weight, k-j), math.comb(k, j))
              for j in range(k+1)] for k in range(5)]
    pairs = [(i, j) for i in range(5) for j in range(i, 5)]
    result = []
    for axis in range(5):
        z, b, c, d, D = [F(int(j == axis)) for j in range(5)]
        C = multiply(base, [z, b, c])
        W = [d, (16*z+30*c)/7, 16*b/7-d, -2*c]
        A1 = [(152*z+124*c+14*D)/21, 120*b/7-4*d, 4*c]
        A2 = add(derivative(C), scale(W, -1))
        H = add([2*D], scale(A1, 2), scale(derivative(A2), 4))
        accumulated = {pair: [F(0)] for pair in pairs}

        def product(coefficient, left, right):
            for i, a in enumerate(q_ops[left]):
                for j, bb in enumerate(q_ops[right]):
                    key = tuple(sorted((i, j)))
                    term = multiply(coefficient, multiply(a, bb))
                    accumulated[key] = add(accumulated[key], term)

        for coefficient, left, right in [
                (A1, 0, 4), (scale(A2, 2), 1, 4), (scale(C, -2), 2, 4),
                (scale(C, -2), 3, 3), (scale(derivative(A1), 2), 0, 3),
                (H, 1, 3), (scale(W, -4), 2, 3), ([3*D], 2, 2)]:
            product(coefficient, left, right)
        result.append([divide_exact(accumulated[pair], weight) for pair in pairs])
    return pairs, result


PAIRS, EXACT_TENSOR = operator_tensor()


def coefficient_vector(parameters):
    b, c, d, D = parameters
    p0 = (152+124*c+14*D)/21
    p1 = 120*b/7-4*d
    p2 = 4*c
    r0, r1, s0 = 1., b-d, d
    s1 = (2*c-2+D)/3
    t0 = (62+76*c-7*D)/42
    t1 = 23*b/7-d
    return np.array([p0, p1, p2, r0, r1, s0, s1, t0, t1])


def coefficient_report(parameters):
    p0, p1, p2, r0, r1, s0, s1, t0, t1 = coefficient_vector(parameters)
    B = np.array([[r0, s0, t0], [r1, s1, t1], [-p0/4, -p1/4, -p2/4]])
    return dict(parameter_order=['b', 'c', 'd', 'D'], parameters=list(map(float, parameters)),
                coefficient_order=['p0', 'p1', 'p2', 'r0', 'r1', 's0', 's1', 't0', 't1'],
                nine_coefficients=coefficient_vector(parameters).tolist(),
                B_determinant=float(np.linalg.det(B)),
                B_singular_values=np.linalg.svd(B, compute_uv=False).tolist(),
                endpoint_H_values=[float(1-parameters[0]+parameters[1]),
                                   float(1+parameters[0]+parameters[1])])


def profile_basis(x, outer_degree, core_degree, core_width, core_rate):
    """Values of P basis and its first four derivatives.

    P has a global polynomial block and a separate flat interior window block.
    The latter is zero on the open outer tails; no imaginary phase is forced
    to start at an outer endpoint by the trial space itself.
    """
    x = np.asarray(x)
    count = outer_degree+1+core_degree+1
    result = np.zeros((5, len(x), count))
    for k in range(outer_degree+1):
        a = np.zeros(k+1); a[-1] = 1
        for j in range(min(k, 4)+1):
            result[j, :, k] = cheb.chebval(x, cheb.chebder(a, j))
    active = abs(x) < core_width
    z = x[active]/core_width
    h = 1-z*z
    w0 = np.exp(core_rate-core_rate/h)
    l1 = -2*core_rate*z/h**2/core_width
    l2 = -2*core_rate*(1+3*z*z)/h**3/core_width**2
    l3 = -24*core_rate*z*(1+z*z)/h**4/core_width**3
    l4 = -24*core_rate*(1+10*z*z+5*z**4)/h**5/core_width**4
    window = [w0, w0*l1, w0*(l2+l1*l1),
              w0*(l3+3*l1*l2+l1**3),
              w0*(l4+4*l1*l3+3*l2*l2+6*l1*l1*l2+l1**4)]
    for k in range(core_degree+1):
        a = np.zeros(k+1); a[-1] = 1
        for j in range(5):
            value = np.zeros(len(z))
            for ell in range(j+1):
                d = j-ell
                if d <= k:
                    value += math.comb(j, ell)*window[ell]*cheb.chebval(z, cheb.chebder(a, d))/core_width**d
            result[j, active, outer_degree+1+k] = value
    return result


def field_jets(x, P_jets):
    weight = poly.polypow(np.array([1., 0., -1.]), 4)
    result = []
    for k in range(5):
        row = np.zeros_like(P_jets[0])
        for j in range(k+1):
            factor = math.comb(k, j)*poly.polyval(x, poly.polyder(weight, k-j))
            row = row+factor*P_jets[j]
        result.append(row)
    return np.asarray(result)


def tensor_values(x):
    return np.array([[poly.polyval(x, list(map(float, row))) for row in block]
                     for block in EXACT_TENSOR])


def reduced_Q(jets, parameters, tensor):
    products = np.array([jets[i]*jets[j] for i, j in PAIRS])
    weights = np.einsum('a,apn->pn', np.r_[1., parameters], tensor)
    return np.sum(weights*products, axis=0)


def raw_Q(x, q, parameters):
    b, c, d, D = parameters
    C = (1-x*x)*(1+b*x+c*x*x)
    Cp = b+2*(c-1)*x-3*b*x*x-4*c*x**3
    W = d+(16+30*c)*x/7+(16*b/7-d)*x*x-2*c*x**3
    A2 = Cp-W
    A2p = 2*(c-1)-6*b*x-12*c*x*x-((16+30*c)/7+2*(16*b/7-d)*x-6*c*x*x)
    p0, p1, p2 = coefficient_vector(parameters)[:3]
    A1 = p0+p1*x+p2*x*x
    A1p = p1+2*p2*x
    f, fp, fpp, fppp, f4 = q
    L = A1*f+2*A2*fp-2*C*fpp
    M = 2*A1p*f+(2*D+2*A1+4*A2p)*fp-4*W*fpp
    return L*f4-2*C*fppp*fppp+M*fppp+3*D*fpp*fpp


def polar_frame(raw):
    gram = raw.T @ raw
    rootdet = np.sqrt(np.linalg.det(gram))
    invroot = np.sqrt(np.trace(gram)+2*rootdet)*np.linalg.inv(gram+rootdet*np.eye(2))
    return raw @ invroot


def circle_initial(basis, weights, x):
    # Four even global modes, as in the proven three-moment construction.
    actual = np.array([field_jets(x, basis[:, :, j]) for j in [0, 2, 4, 6]])
    dp, ddp = actual[:, 1].T, actual[:, 2].T
    A = ddp.T @ (weights[:, None]*ddp)
    B = ddp.T @ ((weights*x*x)[:, None]*ddp)+2*dp.T @ (weights[:, None]*dp)
    values, vectors = eigh(B, A)
    mu = (values[1]+values[2])/2
    f = (np.sqrt((values[3]-mu)/(values[3]-values[0]))*vectors[:, 0]
         +np.sqrt((mu-values[0])/(values[3]-values[0]))*vectors[:, 3])
    g = (np.sqrt((values[2]-mu)/(values[2]-values[1]))*vectors[:, 1]
         +np.sqrt((mu-values[1])/(values[2]-values[1]))*vectors[:, 2])
    answer = np.zeros((basis.shape[-1], 2))
    answer[[0, 2, 4, 6], 0] = f
    answer[[0, 2, 4, 6], 1] = g
    return answer


def complex_pairs(a):
    return np.stack([np.real(a), np.imag(a)], axis=-1).tolist()


def right_integrals_gauss(x, w, values):
    """Right tails of the Legendre interpolant through the validation nodes."""
    n = len(x)
    V = leg.legvander(x, n)
    factors = (2*np.arange(n)+1)/2
    coefficients = factors[:, None]*(V[:, :n].T @ (w[:, None]*values.T))
    tails = np.empty((n, n))
    tails[:, 0] = 1-x
    for j in range(1, n):
        tails[:, j] = (V[:, j-1]-V[:, j+1])/(2*j+1)
    return (tails @ coefficients).T


def validation(coeff, parameters, outer, core, args, count):
    x, w = leg.leggauss(count)
    basis = profile_basis(x, outer, core, args.core_width, args.core_rate)
    P = np.einsum('jnk,k->jn', basis, coeff[:, 0]+1j*coeff[:, 1])
    q = field_jets(x, P)
    red = reduced_Q(P, parameters, tensor_values(x))
    direct = raw_Q(x, q, parameters)
    factored = (1-x*x)**4*red
    moments = np.array([np.sum(w*q[2]**2), np.sum(w*x*q[2]**2),
                        np.sum(w*(x*x*q[2]**2+2*q[1]**2))])
    gram = np.array([[np.sum(w*q[2].real**2), np.sum(w*q[2].real*q[2].imag)],
                     [np.sum(w*q[2].real*q[2].imag), np.sum(w*q[2].imag**2)]])
    left, right = profile_basis(np.array([-1., 1.]), outer, core, args.core_width, args.core_rate)[0] @ (coeff[:, 0]+1j*coeff[:, 1])
    # Exact zero endpoint jets are structural, not numerical near-end cutoffs.
    # Formula R15 gives a second independent check on the three total moments.
    p0, p1, p2, r0, r1, s0, s1, t0, t1 = coefficient_vector(parameters)
    J = right_integrals_gauss(x, w, np.array([q[2]**2, x*q[2]**2,
                                             x*x*q[2]**2+2*q[1]**2]))
    B0 = r0+r1*x-p0*x*x/4
    B1 = s0+s1*x-p1*x*x/4
    B2 = t0+t1*x-p2*x*x/4
    A0 = -p1/2-p2*x
    A1 = p0+p1*x+p2*x*x
    A2 = r1+(s1-p0/2)*x+(t1-p1/2)*x*x-p2*x**3/2
    O = A0*q[0]**2+A1*q[0]*q[1]+A2*q[1]**2+B0*J[0]+B1*J[1]+B2*J[2]
    B = np.array([[r0, s0, t0], [r1, s1, t1], [-p0/4, -p1/4, -p2/4]])
    Wleft = np.array([[1., -1., 1.], [0., 1., -2.], [0., 0., 2.]]) @ B
    transferred = np.array([-.5*np.sum(w*(x+1)**2*factored),
                             np.sum(w*(x+1)*factored), -np.sum(w*factored)])
    return dict(points=count, reduced_Q_l2=float(np.sqrt(np.sum(w*abs(red)**2))),
                reduced_Q_max=float(np.max(abs(red))),
                full_Q_max=float(np.max(abs(factored))),
                complete_O_from_true_right_tails_max=float(np.max(abs(O))),
                direct_vs_factored_Q_max=float(np.max(abs(direct-factored))),
                complex_total_moments=complex_pairs(moments),
                moment_max=float(np.max(abs(moments))), H2_real_imaginary_gram=gram.tolist(),
                exact_R15_residual_transfer_error=float(np.max(abs(Wleft @ moments-transferred))),
                P_at_endpoints=complex_pairs(np.array([left, right])),
                fourth_derivative_endpoint_values=complex_pairs(384*np.array([left, right])),
                sampled_profile_jet_maxima=np.max(abs(q), axis=1).tolist(),
                profile_coefficient_l2=float(np.linalg.norm(coeff)),
                profile_is_zero_extended_C3=True, induced_linear_field_is_C2=True,
                q_derivatives_zero_through_order_three_at_exact_endpoints=True,
                evaluation_uses_frozen_profile_and_operator=True)


def one_stage(args, outer, core, parameters, previous, design_coefficients, frozen_scale):
    started = time.monotonic()
    xr, wr = leg.leggauss(args.reference_n)
    reference = profile_basis(xr, outer, core, args.core_width, args.core_rate)
    q_second = np.column_stack([field_jets(xr, reference[:, :, j])[2]
                                for j in range(reference.shape[-1])])
    mass = q_second.T @ (wr[:, None]*q_second)
    eigenvalues, vectors = np.linalg.eigh(mass)
    keep = eigenvalues > args.mass_cutoff*eigenvalues[-1]
    U, ev = vectors[:, keep], eigenvalues[keep]
    whitening = U/np.sqrt(ev)[None, :]
    if len(ev) < 4:
        raise ArithmeticError('fewer than four resolved H2 trial directions')
    if previous is None:
        physical_initial = circle_initial(reference, wr, xr)
    else:
        old_outer, old_core, old = previous
        physical_initial = np.zeros((reference.shape[-1], 2))
        physical_initial[:old_outer+1] = old[:old_outer+1]
        physical_initial[outer+1:outer+old_core+2] = old[old_outer+1:]
    frame = polar_frame(np.sqrt(ev)[:, None]*(U.T @ physical_initial))
    complement = np.linalg.qr(frame, mode='complete')[0][:, 2:]
    chart_count = 2*(len(ev)-2)
    x, w = leg.leggauss(args.training_n)
    basis = profile_basis(x, outer, core, args.core_width, args.core_rate)
    tensor = tensor_values(x)
    endpoint_basis = profile_basis(np.array([-1., 1.]), outer, core,
                                   args.core_width, args.core_rate)[0]

    def decode(z):
        raw = frame+complement @ z[:chart_count].reshape(-1, 2)
        physical = whitening @ polar_frame(raw)
        par = z[chart_count:] if design_coefficients else parameters
        return physical, par

    initial = np.r_[np.zeros(chart_count), parameters] if design_coefficients else np.zeros(chart_count)
    initial_physical, _ = decode(initial)
    initial_jets = np.einsum('jnk,k->jn', basis, initial_physical[:, 0]+1j*initial_physical[:, 1])
    if frozen_scale is None:
        frozen_scale = max(1., float(np.sqrt(np.sum(w*abs(reduced_Q(initial_jets, parameters, tensor))**2))))

    def residual(z):
        physical, par = decode(z)
        comp = physical[:, 0]+1j*physical[:, 1]
        jets = np.einsum('jnk,k->jn', basis, comp)
        q = field_jets(x, jets)
        value = np.sqrt(w)*reduced_Q(jets, par, tensor)/frozen_scale
        M1 = np.sum(w*x*q[2]**2)
        M2 = np.sum(w*(x*x*q[2]**2+2*q[1]**2))
        moments = args.moment_weight*np.array([M1.real, M1.imag, M2.real, M2.imag])
        edges = endpoint_basis @ comp
        guard = np.maximum(args.endpoint_leading_floor-abs(edges), 0)/args.endpoint_leading_floor
        return np.r_[value.real, value.imag, moments, guard]

    lower = np.full(chart_count, -args.chart_bound)
    upper = np.full(chart_count, args.chart_bound)
    if design_coefficients:
        lower = np.r_[lower, -.4, -.4, -10., -20.]
        upper = np.r_[upper, .4, 2., 10., 20.]
    fit = least_squares(residual, initial, jac=lambda z: absolute_jacobian(residual, z),
                        bounds=(lower, upper), max_nfev=args.max_nfev, x_scale='jac',
                        ftol=1e-10, xtol=1e-10, gtol=1e-10)
    physical, par = decode(fit.x)
    reports = [validation(physical, par, outer, core, args, count) for count in args.validation_n]
    result = dict(outer_degree=outer, core_degree=core,
                  core_width=args.core_width, core_rate=args.core_rate,
                  abstract_coefficients=coefficient_report(par),
                  geometric_coefficients_realized=False,
                  operator_coefficients_were_optimized=design_coefficients,
                  operator_coefficients_frozen_for_next_stages=True,
                  frozen_residual_scale=frozen_scale,
                  full_trial_dimension=reference.shape[-1], retained_trial_dimension=len(ev),
                  mass_eigenvalues=eigenvalues.tolist(), mass_relative_cutoff=args.mass_cutoff,
                  discarded_mass_directions=int(np.sum(~keep)),
                  initial_projection_H2_error=float(np.linalg.norm(
                      q_second @ (initial_physical-physical_initial)*np.sqrt(wr)[:, None])),
                  final_physical_P_coefficients=physical.tolist(),
                  P_basis_order='global T0..Touter, interior_window*T0(x/rho)..Tcore(x/rho)',
                  solver=dict(success=bool(fit.success), message=str(fit.message),
                              nfev=int(fit.nfev), optimality=float(fit.optimality),
                              initial_residual_l2=float(np.linalg.norm(residual(initial))),
                              final_residual_l2=float(np.linalg.norm(fit.fun)),
                              final_jacobian_direction_check=jacobian_direction_check(residual, fit.x),
                              elapsed_seconds=time.monotonic()-started),
                  validation=reports, compact_exact_profile_proved=False,
                  global_complete_period_proved=False, finite_isometric_family_proved=False)
    return result, physical, np.asarray(par).copy(), frozen_scale


def developer_check():
    # This checks exact operator algebra with a single fixed low polynomial.
    # It does not solve the BVP or evaluate a geometric base.
    x = np.array([-.73, -.12, .31, .84])
    Pcoeff = np.array([1+.2j, -.3+.7j, .11-.09j])
    P = np.array([poly.polyval(x, poly.polyder(Pcoeff, j)) for j in range(5)])
    q = field_jets(x, P)
    par = np.array([.13, .27, -.21, 1.2])
    exact_factor = (1-x*x)**4*reduced_Q(P, par, tensor_values(x))
    direct = raw_Q(x, q, par)
    error = float(np.max(abs(exact_factor-direct)))
    assert error < 1e-8
    # Analytic interior-window derivatives compared only on a synthetic function.
    nodes = np.array([-.2, .07, .19])
    h = 1e-5
    plus = profile_basis(nodes+h, 6, 2, .5, 1.)
    minus = profile_basis(nodes-h, 6, 2, .5, 1.)
    center = profile_basis(nodes, 6, 2, .5, 1.)
    relative = []
    for j in range(4):
        observed = (plus[j]-minus[j])/(2*h)
        relative.append(float(np.max(abs(observed-center[j+1]))/max(1., np.max(abs(center[j+1])))))
    assert max(relative) < 2e-7
    gx, gw = leg.leggauss(8)
    integral_error = float(np.max(abs(right_integrals_gauss(gx, gw, np.array([gx*gx]))[0]
                                      -(1-gx**3)/3)))
    assert integral_error < 1e-12
    report = dict(developer_check=True, no_BVP_optimization=True, no_geometry=True,
                  exact_coefficient_factor_divisions=5*len(PAIRS),
                  direct_vs_exact_factor_error=error,
                  synthetic_window_derivative_relative_errors=relative,
                  synthetic_right_tail_integral_error=integral_error)
    print(json.dumps(report, allow_nan=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--outer-degrees', type=int, nargs='+', default=[8, 12, 16])
    parser.add_argument('--core-degrees', type=int, nargs='+', default=[6, 10, 14])
    parser.add_argument('--core-width', type=float, default=.5)
    parser.add_argument('--core-rate', type=float, default=1.)
    parser.add_argument('--initial-D', type=float, nargs='+', default=[-8., 1.])
    parser.add_argument('--initial-b', type=float, default=.05)
    parser.add_argument('--initial-c', type=float, default=0.)
    parser.add_argument('--initial-d', type=float, default=.1)
    parser.add_argument('--reference-n', type=int, default=512)
    parser.add_argument('--training-n', type=int, default=256)
    parser.add_argument('--validation-n', type=int, nargs='+', default=[512, 1024])
    parser.add_argument('--mass-cutoff', type=float, default=1e-12)
    parser.add_argument('--chart-bound', type=float, default=5.)
    parser.add_argument('--endpoint-leading-floor', type=float, default=1e-4)
    parser.add_argument('--moment-weight', type=float, default=1.)
    parser.add_argument('--max-nfev', type=int, default=150)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--developer-check', action='store_true')
    args = parser.parse_args()
    if args.developer_check:
        developer_check(); return
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        parser.error('run all profile research optimization in the public repository Actions')
    if args.out is None or len(args.outer_degrees) != len(args.core_degrees) or min(args.outer_degrees) < 6:
        parser.error('need output, matched degree lists, and outer degree >=6')
    if sorted(args.outer_degrees) != args.outer_degrees or sorted(args.core_degrees) != args.core_degrees:
        parser.error('refinement degrees must be nondecreasing')
    if min(args.core_degrees) < 0 or min(args.reference_n, args.training_n, *args.validation_n) < 32:
        parser.error('nonnegative core degrees and at least 32 quadrature nodes are required')
    if not 0 < args.mass_cutoff < 1 or args.endpoint_leading_floor <= 0:
        parser.error('invalid mass cutoff or endpoint leading guard')
    if not 0 < args.core_width < 1 or args.core_rate <= 0:
        parser.error('need an interior window and a positive flat rate')
    output = dict(schema='literature-global-C2-profile-BVP-v1',
                  arguments=vars(args) | {'out': str(args.out)},
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  coefficient_family_is_abstract_not_geometric=True,
                  exact_endpoint_relations='C(+/-1)=0, W(+/-1)=-(8/7)Cprime(+/-1)',
                  q_zero_extension_regular_class='C3', Y_zero_extension_regular_class='C2',
                  profile_trial_space_contains_a_flat_interior_window=True,
                  finite_collocation_fit_is_not_an_exact_profile=True,
                  designs=[], task_complete=False)
    for initial_D in args.initial_D:
        design = dict(initial_D=initial_D, stages=[])
        output['designs'].append(design)
        par = np.array([args.initial_b, args.initial_c, args.initial_d, initial_D])
        previous = None
        scale0 = None
        for stage, (outer, core) in enumerate(zip(args.outer_degrees, args.core_degrees)):
            report, physical, par, scale0 = one_stage(args, outer, core, par, previous, stage == 0, scale0)
            design['stages'].append(report)
            previous = (outer, core, physical)
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
            print(json.dumps(dict(initial_D=initial_D, stage=stage,
                                  solver=report['solver'], validation=report['validation'][-1]),
                             allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

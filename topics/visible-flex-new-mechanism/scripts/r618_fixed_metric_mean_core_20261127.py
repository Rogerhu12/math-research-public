#!/usr/bin/env python3
"""R618 pure fixed-metric mean/core and affine forced-mouth algebra.

No input, root solve, quadrature, tail integration, optimizer, request or
workflow is created here. E and E_r are evaluations of ONE independently
frozen complete function. A later declared public Actions scope must supply
its same continuous angular functional (with separately charged numerical
evaluation/errors), the actual scalar root and all original field jets.
Replacing E by a new grid-dependent turning root is not this interface.

The finite-array formulas below are observations until their quadrature,
root, radial, tail and floating errors are supplied. No return value claims
continuous or README completion. No scientific routine is executed locally.
"""
import numpy as np


def _geometry(r, E, p, q, t):
    b2 = r*r-q*q
    if np.any(b2 <= 0):
        raise ArithmeticError('fixed-metric angular graph domain failed')
    b = np.sqrt(b2)
    u2 = E-r*r*p*p/b2
    if np.any(u2 <= 0):
        raise ArithmeticError('fixed-metric positive velocity failed')
    u = np.sqrt(u2)
    N = r/b+r*r*p*t/b**3
    if np.any(N <= 0):
        raise ArithmeticError('fixed-metric positive turning failed')
    return b, u, N


def state_from_same_root(r, E, E_r, p0, jets, angular_mean):
    """Use the actual p0 root; never recompute or vary the supplied metric.

    One radial point, one common angle axis. ``jets`` has fr,frr,ft,ftt,frt.
    ``angular_mean`` acts on axis0 and must be the same functional in all
    expressions; for direction blocks it retains the direction axis.
    This function neither solves nor certifies the scalar root. Its residual
    is returned, and a caller must not hide a finite quadrature/root error.
    """
    if not (r > 0 and E > 0):
        raise ValueError('positive radius and same frozen metric required')
    fr, frr, q, t, frt = [np.asarray(jets[k]) for k in ('fr', 'frr', 'ft', 'ftt', 'frt')]
    if fr.ndim != 1 or any(x.shape != fr.shape for x in (frr, q, t, frt)):
        raise ValueError('one identical angular axis for every actual jet required')
    p = p0+fr
    b, u, N = _geometry(r, E, p, q, t)
    B = frt-q/r
    C = E*t+r*p
    M = r+p*t-q*q/r
    omega = r*r/(u**3*b**3)
    mean_derivative = angular_mean(omega*C)
    if not np.isfinite(mean_derivative) or mean_derivative == 0:
        raise ArithmeticError('same mean-root branch is not locally invertible')
    Q = E*B*B+E_r*M/2-C*frr
    p0_r = angular_mean(omega*Q)/mean_derivative
    D = C*(p0_r+frr)-E*B*B-E_r*M/2
    return {'r':r, 'E':E, 'E_r':E_r, 'p0':p0, 'p0_r':p0_r,
        'fr':fr, 'frr':frr, 'q':q, 't':t, 'frt':frt,
        'p':p, 'b':b, 'u':u, 'N':N, 'B':B, 'C':C, 'M':M,
        'omega':omega, 'Q':Q, 'mean_derivative':mean_derivative,
        'D':D, 'R':omega*D,
        'turning_root_residual_observation':angular_mean(N/u)-1,
        'mean_connection_residual_observation':angular_mean(omega*D),
        'same_frozen_metric_not_resolved_from_height':True,
        'continuous_errors_or_README_certified':False}


def _geometry_direction(r, p, q, t, b, u, dp, dq, dt):
    db = -q*dq/b
    du = -r*r*p*dp/(u*b*b)-r*r*p*p*q*dq/(u*b**4)
    dN = (r*q*dq/b**3+r*r*(t*dp+p*dt)/b**3
          +3*r*r*p*t*q*dq/b**5)
    return db, du, dN


def direction_from_same_root(state, direction_jets, angular_mean):
    """R618(34)--(37), complete off-solution derivative with dE=dE_r=0.

    The five direction jets have shape (angle,direction). All mean-root,
    mean-root-radial and off-solution weight terms are retained. The output
    dR,da,db can be consumed by the R613 two-primitive position chain.
    """
    H_r, H_rr, H_t, H_tt, H_rt = [np.asarray(direction_jets[k]) for k in
        ('fr', 'frr', 'ft', 'ftt', 'frt')]
    if H_r.ndim != 2 or H_r.shape[0] != len(state['p']):
        raise ValueError('complete same-angle direction blocks required')
    if any(x.shape != H_r.shape for x in (H_rr, H_t, H_tt, H_rt)):
        raise ValueError('inconsistent complete direction jets')
    r, E, E_r = state['r'], state['E'], state['E_r']
    p, q, t, b, u, N = [state[k][:,None] for k in ('p', 'q', 't', 'b', 'u', 'N')]
    _, du_free, dN_free = _geometry_direction(r, p, q, t, b, u, H_r, H_t, H_tt)
    dp0 = -angular_mean(dN_free/u-N*du_free/u**2)/state['mean_derivative']
    dp = H_r+dp0[None,:]
    db, du, dN = _geometry_direction(r, p, q, t, b, u, dp, H_t, H_tt)
    B, C, M, omega, Q, frr, D = [state[k][:,None] for k in
        ('B', 'C', 'M', 'omega', 'Q', 'frr', 'D')]
    dB = H_rt-H_t/r
    dC = E*H_tt+r*dp
    dM = t*dp+p*H_tt-2*q*H_t/r
    domega = -3*omega*(du/u+db/b)
    dc0 = angular_mean(domega*C+omega*dC)
    dQ = 2*E*B*dB+E_r*dM/2-dC*frr-C*H_rr
    dp0_r = (angular_mean(domega*Q+omega*dQ)-state['p0_r']*dc0)/state['mean_derivative']
    dD = dC*(state['p0_r']+frr)+C*(dp0_r[None,:]+H_rr)-2*E*B*dB-E_r*dM/2
    dR = domega*D+omega*dD
    return {'p0':dp0, 'p0_r':dp0_r, 'p':dp, 'b':db, 'u':du, 'N':dN,
        'C':dC, 'M':dM, 'B':dB, 'omega':domega, 'D':dD, 'R':dR,
        'a':dN/u-N*du/u**2, 'E':np.zeros_like(dp0), 'E_r':np.zeros_like(dp0),
        'turning_linearized_residual_observation':angular_mean(dN/u-N*du/u**2),
        'mean_connection_linearized_residual_observation':angular_mean(dR)}


def core_from_same_root(R, alpha, E_difference, E_difference_r,
                        P, P_t, P_tt, core_root, angular_mean):
    """Full-angle target including the forced fixed-g zeta and zeta_r.

    ``core_root`` is e(P), not the frozen metric difference E_difference.
    The former is obtained from the same continuous core root equation.
    This helper never overwrites the frozen E_difference or its derivative.
    """
    if not (R > 0 and .5 < alpha < 1):
        raise ValueError('declared regular core constants required')
    P, P_t, P_tt = [np.asarray(x) for x in (P, P_t, P_tt)]
    u2 = core_root+2*P
    if np.any(u2 <= 0):
        raise ArithmeticError('positive full-angle core root required')
    c = alpha/(1+alpha)
    S = angular_mean(P_t*P_t)
    target = (c*u2*P_tt-P_t*P_t+(2*c+1)*S)/R
    return {'R':R, 'alpha':alpha, 'c':c, 'P':P, 'P_t':P_t, 'P_tt':P_tt,
        'u':np.sqrt(u2), 'root':core_root, 'S':S, 'P1_target':target,
        'zeta':(core_root-E_difference)/2,
        'zeta_r':-(2*c+1)*S/R-E_difference_r/2,
        'effective_e_r':-2*(2*c+1)*S/R,
        'frozen_e':E_difference, 'frozen_e_r':E_difference_r,
        'turning_root_residual_observation':angular_mean(1/np.sqrt(u2))-1,
        'target_mean_roundoff_or_quadrature_observation':angular_mean(target),
        'continuous_core_certified':False}


def core_direction(state, H, H_t, H_tt, angular_mean):
    """Full R618 core parameter chain, retaining implicit root dependence."""
    H, H_t, H_tt = [np.asarray(x) for x in (H, H_t, H_tt)]
    P, P_t, P_tt, u = [state[k][:,None] for k in ('P', 'P_t', 'P_tt', 'u')]
    de = -2*angular_mean(H/u**3)/angular_mean(u**-3)
    cross = angular_mean(P_t*H_t)
    R, c = state['R'], state['c']
    target = (c*((de[None,:]+2*H)*P_tt+(state['root']+2*P)*H_tt)
              -2*P_t*H_t+2*(2*c+1)*cross[None,:])/R
    return {'root':de, 'zeta':de/2, 'zeta_r':-2*(2*c+1)*cross/R,
        'P1_target':target,
        'frozen_e':np.zeros_like(de), 'frozen_e_r':np.zeros_like(de)}


def forced_affine_cell_step(k_left, k_right, V, rho_next, tau_next, beta):
    """One R618 exact affine elimination; caller supplies paid true data.

    This is not a tail solve or a truncation bound. beta includes BOTH
    neighboring true forced flux integrals. Keeping only rho loses the
    inhomogeneous mouth. Previously paid homogeneous rho may be reused.
    """
    denominator = V-k_right*rho_next
    if np.any(denominator <= 0):
        raise ArithmeticError('true forced-cell denominator unresolved')
    return k_left/denominator, (beta-k_right*tau_next)/denominator


def forced_mouth(D_left_left, k, rho_next, tau_next, beta_left):
    """Return both coefficients of q_left = linear*y_left + affine."""
    return D_left_left+k*rho_next, beta_left-k*tau_next


def core_laurent_coefficients(cosine_coefficients, core_root, R, alpha):
    """Direct finite convolution, including every dependent mode through2J.

    This algebra uses the caller's same e(P) root; it never approximates that
    continuous root by a finite sum. The returned constant is retained as a
    floating expression observation, although its exact formula is zero.
    A caller must not interpret finite floating convolutions as certified.
    """
    if any(not isinstance(j, int) or j <= 0 or j % 2 for j in cosine_coefficients):
        raise ValueError('independent positive even cosine frequencies required')
    P = {0:0j}
    for j, value in cosine_coefficients.items():
        P[j] = P[-j] = complex(value)/2
    Pt = {j:1j*j*v for j,v in P.items()}
    Ptt = {j:-j*j*v for j,v in P.items()}
    U2 = {j:2*v for j,v in P.items()}
    U2[0] += core_root
    def product(a, b):
        result = {}
        for j, x in a.items():
            for k, y in b.items():
                result[j+k] = result.get(j+k,0j)+x*y
        return result
    first, square = product(U2,Ptt), product(Pt,Pt)
    c = alpha/(1+alpha)
    modes = set(first)|set(square)|{0}
    answer = {j:(c*first.get(j,0j)-square.get(j,0j))/R for j in modes}
    answer[0] += (2*c+1)*square.get(0,0j)/R
    return {'all_laurent_coefficients':answer,
        'highest_dependent_mode':2*max(cosine_coefficients,default=0),
        'constant_expression_observation':answer[0],
        'finite_convolution_without_angular_alias':True,
        'continuous_core_root_and_float_errors_certified':False}

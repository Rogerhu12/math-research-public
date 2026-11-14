"""Prepared complete connection-root certificate around an actual K candidate.

Uses the full finite residual polynomial and a Wiener inverse about the
specified positive V anchor. No universal eta<=1/32 assumption is made.
All positivity gates are retained. This source has not yet been executed
on the outer saved trajectory; it does not certify radial existence.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction

from flint import acb, arb
from closure_real_head_source_enclosure import ball_record
from tail_r41_connection_polynomial import (
    real, add, scale, product, derivative, norm, residual_polynomial)


def real_lower(term):
    """Valid for a real-valued Laurent polynomial with enclosed coefficients."""
    center = term.get(0, acb(0)).real
    radius = sum((abs(value) for mode, value in term.items() if mode), arb(0))
    return (center-radius).lower()


def certify_general(P, G, Khat, w, tau=Fraction(0), vstar=Fraction(1)):
    """The complete gates in tail-outer-general-connection-root.md.

All input fields must denote real-valued functions. They may be
coefficient enclosures over the same real radial panel, provided that
their construction retains this same-function interpretation.
"""
    tau, vstar = real(tau), real(vstar)
    one = {0: acb(1)}
    z, E = w*w, 1+w*w
    T = derivative(P)
    P2, T2 = product(P, P), product(T, T)
    S = add(one, scale(P2, -z))
    Gamma = add(one, scale(G, z))
    S2, Gamma2 = product(S, S), product(Gamma, Gamma)
    y = add(one, Khat)
    y2 = product(y, y)
    s, c = norm(scale(P2, z), tau), norm(scale(G, z), tau)
    result = dict(
        scope="Complete angular algebraic root around the specified candidate; no radial solution or discretization claim",
        universal_eta_smallness_used=False,
        complete_mean_and_nonlinear_frequencies_retained=True,
        S_Wiener_radius=ball_record(s),
        Gamma_Wiener_radius=ball_record(c),
        positive_w=bool(w > 0), positive_anchor=bool(vstar > 0),
        initial_gates=bool(w > 0 and vstar > 0 and s < 1 and c < 1))
    if not result["initial_gates"]:
        result.update(complete_root_gate=False, failure="S/Gamma/anchor gate failed")
        return result
    Anum = add(product(Gamma2, S2), scale(T2, z))
    Vnum = add(product(Anum, y), product(T, S))
    denom = (1-s)**2
    a = (norm(Anum, tau)/denom).upper()
    dv = (norm(add(Vnum, scale(S2, -vstar)), tau)/denom).upper()
    nu = (vstar-dv).lower()
    result.update(A_norm_upper=ball_record(a), V_anchor=ball_record(vstar),
                  V_difference_norm=ball_record(dv), V_inverse_denominator=ball_record(nu))
    if not nu > 0:
        result.update(complete_root_gate=False, failure="Candidate V inverse gate failed")
        return result
    poly = residual_polynomial(P, G, Khat, w)
    residual = norm(poly, tau)
    e = (residual/denom).upper()
    xi = (a*e/(nu*nu)).upper()
    result.update(complete_polynomial_degree=max(map(abs, poly), default=0),
                  residual_W1=ball_record(residual),
                  cleared_residual_W1=ball_record(e), quadratic_ratio=ball_record(xi))
    if not xi < 1:
        result.update(complete_root_gate=False, failure="Complete quadratic-root discriminant gate failed")
        return result
    delta = (e/(nu*(1+(1-xi).sqrt()))).upper()
    Y, B = norm(y, tau), (norm(T, tau)/(1-s)).upper()
    Dhat = add(scale(S, E), scale(y2, -z))
    Nnum = add(S, scale(product(T, y), z))
    Lhat = add(y, scale(T, E))
    y0, d0 = real_lower(y), real_lower(Dhat)
    numerator0 = real_lower(Nnum)
    n0 = (numerator0/(1+s if numerator0 >= 0 else 1-s)).lower()
    l0 = real_lower(Lhat)
    margins = dict(
        positive_radial_slope=(y0-delta).lower(),
        positive_D=(d0-z*delta*(2*Y+delta)).lower(),
        unsquared_positive_numerator=(n0-z*B*delta).lower(),
        positive_Darboux_leading=(l0-delta).lower())
    gate = all(value > 0 for value in margins.values())
    perpendicular = norm({m: value for m, value in Khat.items() if m}, tau)
    strong = (norm(P, tau)+perpendicular+delta).upper()
    result.update(
        candidate_y_lower=ball_record(y0), candidate_D_lower=ball_record(d0),
        candidate_N_lower=ball_record(n0), candidate_leading_lower=ball_record(l0),
        complete_K_correction_W1=ball_record(delta),
        complete_mean_K_error_upper=ball_record(delta),
        branch_margins={name: ball_record(value) for name, value in margins.items()},
        complete_root_gate=gate,
        failure=None if gate else "Real unsquared branch/leading margin failed",
        complete_nonmean_R33_norm_upper=ball_record(strong) if gate else None,
        R33_complete_mean_domain=bool(gate and strong <= arb(1)/32),
        R33_complete_working_domain=bool(gate and strong <= arb(1)/64),
        angular_quadrature_used=False, radial_flow_used=False)
    return result

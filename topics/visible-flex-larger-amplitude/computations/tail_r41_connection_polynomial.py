"""Exact full-angle connection-root gates from finite Laurent polynomials.

R41 supplies the infinite angular root. This module computes its input
norms and, optionally, the complete finite residual polynomial for a
specified finite K candidate. No angle sampling, radial flow or Node call
occurs. A point certificate is not a radial solution certificate.

Prepared by tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
Execution against the actual saved fields is separate from this source.
"""
from fractions import Fraction

from flint import acb, arb
from closure_real_head_source_enclosure import exact_q, ball_record


def real(value):
    return value if isinstance(value, arb) else exact_q(value)


def add(*terms):
    result = {}
    for term in terms:
        for mode, value in term.items():
            result[mode] = result.get(mode, acb(0)) + value
    return result


def scale(term, coefficient):
    coefficient = real(coefficient)
    return {mode: coefficient*value for mode, value in term.items()}


def product(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            m = a+b
            result[m] = result.get(m, acb(0)) + x*y
    return result


def derivative(term):
    return {mode: acb(0, mode)*value for mode, value in term.items()}


def norm(term, tau):
    tau = real(tau)
    return sum(((1+abs(mode))*(tau*abs(mode)).exp()*abs(value)
                for mode, value in term.items()), arb(0)).upper()


def fields(heights, momenta, modes, radius, w, mu, orientation=1):
    """Inputs are real amplitudes; the momentum gauge is already local.

The returned P and G have exact zero mean by definition of this
candidate. Any omitted input mode is a definition, not a theorem about
the exact radial solution.
"""
    if orientation not in (-1, 1):
        raise ValueError("A signed momentum orientation is required")
    if len(heights) != len(momenta) or len(heights) != len(modes):
        raise ValueError("Complete height and momentum spectra must match")
    P, G = {}, {}
    for height, momentum, mode in zip(heights, momenta, modes):
        mode = int(mode)
        if mode <= 0:
            raise ValueError("Only positive, nonmean input modes are listed")
        sine = -mode*real(height)/(radius*w)
        cosine = orientation*arb(12).sqrt()*mu*real(momentum)/(radius**4*w*w)
        # a*sin(m*theta) has signed coefficients -i*a/2, +i*a/2.
        P[mode], P[-mode] = acb(0, -sine/2), acb(0, sine/2)
        G[mode] = G[-mode] = acb(cosine/2)
    return P, G


def candidate_K(heights, L, modes, radius, w):
    """R41.57 using H=r^4 Q, including the complete finite candidate mean."""
    if len(L) != len(modes)+1 or len(heights) != len(modes):
        raise ValueError("The finite candidate root spectrum is incomplete")
    result = {0: acb(real(L[0]))}
    for height, ell, mode in zip(heights, L[1:], modes):
        coefficient = arb(2).sqrt()*real(ell)+int(mode)**2*real(height)/(radius*w)
        result[int(mode)] = result[-int(mode)] = acb(coefficient/2)
    return result


def residual_polynomial(P, G, Khat, w):
    """All coefficients of R41.49, without rational-series truncation."""
    one = {0: acb(1)}
    z = w*w
    E = 1+z
    T = derivative(P)
    P2, G2, T2 = (product(value, value) for value in (P, G, T))
    S = add(one, scale(P2, -z))
    Gamma = add(one, scale(G, z))
    Gamma2, S2 = product(Gamma, Gamma), product(S, S)
    y = add(one, Khat)
    y2 = product(y, y)
    R = add(product(Gamma2, add(one, scale(P2, -E))),
            scale(G, 2), scale(G2, z))
    return add(product(add(product(Gamma2, S2), scale(T2, z)), y2),
               scale(product(T, product(S, y)), 2),
               scale(product(R, S2), -1))


def certify(P, G, w, tau=Fraction(0), Khat=None):
    """Return a full-angle point certificate, or the actual failed gates."""
    tau = real(tau)
    pn, tn, gn = norm(P, tau), norm(derivative(P), tau), norm(G, tau)
    eta = (pn+tn+gn).upper()
    root_gate = bool(w > 0 and w <= arb(1)/2 and eta <= arb(1)/32)
    result = dict(
        scope="Complete angular root for these specified P/G fields at one real radial point; no radial existence or discretization claim",
        P_norm=ball_record(pn), Ptheta_norm=ball_record(tn),
        G_norm=ball_record(gn), eta=ball_record(eta),
        full_connection_root_gate=root_gate,
        mean_G_zero_by_candidate_definition=0 not in G or G[0] == 0,
        root_source="R41 Theorem41A; no finite projected-root assertion")
    if root_gate:
        result.update(
            K_norm_upper=ball_record((arb(9)/8*eta).upper()),
            D_lower=ball_record((1-arb(3)/5*eta).lower()),
            S_lower=ball_record((1-eta*eta/4).lower()),
            Gamma_lower=ball_record((1-eta/4).lower()),
            Darboux_leading_over_w_lower=ball_record((1-arb(19)/8*eta).lower()))
    if Khat is not None:
        khat = norm(Khat, tau)
        result["candidate_K_norm"] = ball_record(khat)
        residual_gate = bool(root_gate and khat <= arb(1)/16)
        result["full_polynomial_residual_gate"] = residual_gate
        if residual_gate:
            poly = residual_polynomial(P, G, Khat, w)
            residual = norm(poly, tau)
            correction = (arb(4)/7*residual).upper()
            perpendicular = norm({m: v for m, v in Khat.items() if m}, tau)
            strong = (pn+perpendicular+correction).upper()
            result.update(
                complete_polynomial_degree=max(map(abs, poly), default=0),
                residual_W1=ball_record(residual),
                complete_K_correction_W1=ball_record(correction),
                mean_K_correction_abs_upper=ball_record(correction),
                complete_nonmean_R33_norm_upper=ball_record(strong),
                R33_complete_mean_domain=bool(strong <= arb(1)/32),
                R33_complete_working_domain=bool(strong <= arb(1)/64),
                every_residual_frequency_retained=True,
                angular_quadrature_used=False,
                radial_flow_used=False)
    return result

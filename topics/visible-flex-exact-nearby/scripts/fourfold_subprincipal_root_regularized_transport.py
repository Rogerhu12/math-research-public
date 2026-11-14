#!/usr/bin/env python3
"""Complete finite Fourier source for the R106 root transport counterterm.

All finite convolutions retain every output frequency.  This file does not
produce geometric inputs: the caller must pay the actual G,q,k polynomials,
whole-disk errors, root identity and true-ray input separately.

Rows are finite mappings j -> acb coefficient of exp(4 i j theta); radial
row n is the coefficient of physical rho**n, not a scaled radial variable.
"""
from __future__ import annotations
from collections.abc import Mapping
from flint import acb, arb


def fourier_row(values):
    if not isinstance(values, Mapping):
        raise TypeError("a full finite Laurent mapping is required")
    out = {}
    for index, value in values.items():
        key = int(index)
        if key != index:
            raise ValueError("noninteger physical Fourier index")
        value = acb(value)
        if not value.is_finite():
            raise ValueError("nonfinite coefficient")
        out[key] = value
    return out


def fadd(*rows):
    out = {}
    for row in rows:
        for k, v in row.items():
            out[k] = out.get(k, acb(0))+v
    return out


def fscale(row, scalar):
    return {k: acb(scalar)*v for k, v in row.items()}


def fmul(left, right):
    out = {}
    for j, v in left.items():
        for k, w in right.items():
            out[j+k] = out.get(j+k, acb(0))+v*w
    return out


def ftheta(row):
    return {k: acb(0, 4*k)*v for k, v in row.items()}


def regularized_source(G, q, kstar, sigma):
    """Finite reference defined by (106RT.10), with no unknown true tails zeroed.

    G,q,kstar are chosen finite polynomials. Their coefficients need not satisfy
    kstar[0]*G[0] == -1/16 as interval arithmetic identities. The actual geometry
    must satisfy that exact identity; the difference between this reference and
    the true regularized source is paid by source_error_bound.
    """
    if sigma not in (-1, 1):
        raise ValueError("sigma must be one actual branch")
    if not G or not q or not kstar:
        raise ValueError("empty finite root polynomial")
    G, q, kstar = [list(map(fourier_row, rows)) for rows in (G, q, kstar)]
    row = lambda rows, n: rows[n] if n < len(rows) else {}
    G0, G1, q0 = G[0], row(G, 1), q[0]
    Bm3 = fscale(G0, -acb(1)/3)
    Bm1 = fadd(fscale(G1, -1),
                fscale(ftheta(fmul(q0, G0)), -acb(2)/3))
    count = max(len(G)-2, len(q), len(kstar), 1)
    even, odd = [], []
    for n in range(count):
        even.append(fadd(
            row(G, n+2),
            fscale(ftheta(fmul(row(q, n+1), G0)), acb(2)/3),
            fscale(ftheta(fmul(row(q, n), Bm1)), -2)))
        odd.append(fadd(
            fscale(ftheta(fmul(row(kstar, n+1), G0)), -acb(2*sigma)/3),
            fscale(ftheta(fmul(row(kstar, n), Bm1)), 2*sigma)))
    return {"even_rho_rows": even, "s_times_odd_rho_rows": odd,
            "boundary_s_minus3": Bm3, "boundary_s_minus1": Bm1,
            "physical_angular_multiplier": 4,
            "finite_formula_only": True, "all_convolution_frequencies_retained": True}


def full_polynomial_norm(rows, radial_radius, physical_strip, theta_order=0):
    """A rigorous finite bidisk Wiener upper bound; no sampling."""
    r, s = arb(radial_radius), arb(physical_strip)
    if not r >= 0 or not s >= 0 or theta_order not in (0, 1, 2, 3, 4):
        raise ValueError("invalid finite norm domain")
    total = arb(0)
    for n, row in enumerate(rows):
        for k, v in row.items():
            frequency = 4*abs(int(k))
            total += abs(acb(v))*r**n*(s*frequency).exp()*frequency**theta_order
    return total.upper()


def _positive(value, name, allow_zero=False):
    value = arb(value)
    if not value.is_finite() or not (value >= 0 if allow_zero else value > 0):
        raise ValueError("unpaid positive input "+name)
    return value


def source_error_bound(*, outer_radius, working_radius, s_radius,
                       first_angle_loss, second_angle_loss,
                       G_bound, q_bound, k_bound,
                       G_error, q_error, k_error,
                       finite_q_bound=None, finite_k_bound=None):
    """True uniform complex source error (106RT.12).

    Inputs are already complete sup bounds on one common outer (rho,theta)
    bidisk. The caller must check the true angular widths and exact identity.
    The s disk must satisfy s_radius**2 <= working_radius < outer_radius.
    """
    R = _positive(outer_radius, "outer rho radius")
    r = _positive(working_radius, "working rho radius")
    c = _positive(s_radius, "s radius")
    d1 = _positive(first_angle_loss, "first physical angle loss")
    d2 = _positive(second_angle_loss, "second physical angle loss")
    if not c*c <= r or not r < R:
        raise ValueError("root disks are not nested")
    MG = _positive(G_bound, "true G modulus", True)
    MQ = _positive(q_bound, "true q modulus", True)
    MK = _positive(k_bound, "true k modulus", True)
    eG = _positive(G_error, "complete G error", True)
    eq = _positive(q_error, "complete q error", True)
    ek = _positive(k_error, "complete k error", True)
    Qh = _positive(MQ+eq if finite_q_bound is None else finite_q_bound,
                   "finite q modulus", True)
    Kh = _positive(MK+ek if finite_k_bound is None else finite_k_bound,
                   "finite k modulus", True)
    d = 1-r/R
    B = MG/R+2*MQ*MG/(3*d1)
    eB = eG/R+2*(eq*MG+Qh*eG)/(3*d1)
    EG2 = eG/(R*R*d)
    EQG = (eq*MG+Qh*eG)/(R*d)
    EKG = (ek*MG+Kh*eG)/(R*d)
    EQB = eq*B+Qh*eB
    EKB = ek*B+Kh*eB
    error = EG2+2*(EQG+c*EKG)/(3*d2)+2*(EQB+c*EKB)/d2
    return {"regularized_source_sup_error": error.upper(),
            "B1_true_modulus": B.upper(), "B1_sup_error": eB.upper(),
            "G_shift2_error": EG2.upper(),
            "q_shift1_times_G0_error": EQG.upper(),
            "k_shift1_times_G0_error": EKG.upper(),
            "q_times_B1_error": EQB.upper(), "k_times_B1_error": EKB.upper(),
            "cut_boundary_error_at_s_radius": (eG/(3*c*c*c)+eB/c).upper()}


def pullback_error_bound(*, true_field_bound, true_theta_derivative_bound,
                         complete_field_error, true_angle_minus_reference,
                         true_J_minus_reference, reference_J_bound):
    """One-form true-ray error (106RT.14), before integration in actual ds."""
    M, Mt, e, et, eJ, Q = [
        _positive(v, name, True) for v, name in (
            (true_field_bound, "true field modulus"),
            (true_theta_derivative_bound, "true physical theta derivative"),
            (complete_field_error, "complete finite field error"),
            (true_angle_minus_reference, "true angle error"),
            (true_J_minus_reference, "true Jacobian error"),
            (reference_J_bound, "reference Jacobian modulus"))]
    return (M*eJ+Q*(Mt*et+e)).upper()

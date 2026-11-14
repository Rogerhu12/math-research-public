"""Explicit finite two-jet definition for the actual saved13-port candidate.

The saved binary Q/L and the fixed true endpoint background define one
nonmean H/K pair.  Its candidate second jet is a finite Fourier projection
of a finite inverse-polynomial PDE expression.  It is deliberately NOT
declared the exact radial derivative of the unknown true solution.

R48 subsequently interpolates these candidate jets by one actual height;
R44 restores the complete mean and measures its full continuous defect.
No angular quadrature, root solve, ODE or real-source integration occurs.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction
from flint import acb, arb

from closure_real_head_source_enclosure import ball_record
from tail_r41_connection_polynomial import real, add, scale, product, derivative, norm
from tail_outer_compatible_mean_defect import (
    ONE, constant, powers, linear_combination, algebra)
from tail_outer_weighted_compatible import intersection


def finite_saved_endpoint(Q, L, *, radius, radius_x, w, log_w_x,
                          spacing=2, tau=Fraction(1, 64), inverse_degree=8):
    """Return real cosine H,H_r,H_rr and source-chart K,K_x candidate fields.

The actual constants r,w,r_x,ell are the same exact source functions
whose supplied Arb enclosures are used throughout this evaluation.
The finite inverse degree is part of the candidate definition.
"""
    if len(L) != len(Q)+1 or not isinstance(spacing, int) or spacing <= 0 or spacing % 2:
        raise ValueError("The complete nonmean Q and mean+nonmean L spectra are required")
    if not isinstance(inverse_degree, int) or inverse_degree < 0:
        raise ValueError("A fixed nonnegative inverse-polynomial degree is required")
    radius, radius_x, w, ell, tau = map(real, (radius, radius_x, w, log_w_x, tau))
    if not radius > 0 or not radius_x > 0 or not w > 0 or not tau >= 0:
        raise ValueError("The true endpoint background and analytic width must be valid")
    modes = [spacing*(j+1) for j in range(len(Q))]
    H, Kbar = {}, {}
    for j, m in enumerate(modes):
        h = radius**4*real(Q[j])
        k = arb(2).sqrt()*real(L[j+1])+m*m*h/(radius*w)
        H[m] = H[-m] = acb(h/2)
        Kbar[m] = Kbar[-m] = acb(k/2)
    P = scale(derivative(H), 1/(radius*w))
    center = real(L[0])
    anchor = 1+center
    if not anchor > 0:
        raise ValueError("The finite candidate inverse anchor is not positive")
    z, s = w*w, radius_x/radius
    full = algebra(P, Kbar, center, z)
    # This is one fixed finite polynomial, not a separately rounded inverse
    # chosen at each angle.  Exact full inverse error is recorded below.
    W = scale(add(Kbar, scale(full["T"], full["E"])), 1/anchor)
    Wnorm = norm(W, tau)
    if not Wnorm < 1:
        raise ValueError("The complete angular inverse-polynomial remainder gate failed")
    inv = scale(linear_combination(powers(W, inverse_degree),
                                   [(-1)**j for j in range(inverse_degree+1)]),
                1/anchor)
    U = add(derivative(full["K"]), scale(P, -1))
    ell_poly = add(
        product(add(full["K"], full["T"]), add(full["K"], full["T"])),
        scale(add(scale(product(full["K"], full["T"]), 2),
                  product(full["T"], full["T"]), scale(full["P2"], -1)), z))
    numerator = add(scale(product(U, U), full["E"]*s), scale(ell_poly, ell))
    nonlinear_polynomial = product(numerator, inv)
    linear = scale(add(scale(Kbar, 2), full["T"]), -ell)
    projected = {
        m: nonlinear_polynomial.get(m, acb(0))
        for m in [sign*k for k in modes for sign in (-1, 1)]}
    Kbarx = add(linear, projected)
    tail = {m: value for m, value in nonlinear_polynomial.items()
            if m and abs(m) not in modes}
    inverse_error = (Wnorm**(inverse_degree+1)/(anchor*(1-Wnorm))).upper()
    full_source_projection_error = (
        norm(numerator, tau)*inverse_error+norm(tail, tau)).upper()
    Hcos, Hrcos, Hrrcos, Kcos, Kxcos = {}, {}, {}, {}, {}
    for m in modes:
        coefficients = {}
        for name, field in (("H", H), ("K", Kbar), ("Kx", Kbarx)):
            positive, negative = field.get(m, acb(0)), field.get(-m, acb(0))
            if not positive.imag.contains(0) or not negative.imag.contains(0):
                raise ArithmeticError("A real even candidate coefficient lost its reality")
            coefficients[name] = 2*intersection(positive.real, negative.real)
        Hcos[m], Kcos[m], Kxcos[m] = (
            coefficients["H"], coefficients["K"], coefficients["Kx"])
        Hrcos[m] = w*Kcos[m]
        Hrrcos[m] = (w/radius_x)*(Kxcos[m]+ell*Kcos[m])
    return dict(
        H=Hcos, Hr=Hrcos, Hrr=Hrrcos, K=Kcos, Kx=Kxcos,
        mean_candidate=center,
        report=dict(
            status="Explicit saved-Q/L finite candidate endpoint two-jet, not an exact radial-solution jet",
            modes=modes, all_saved_nonmean_modes_retained=True,
            candidate_mean=ball_record(center), inverse_degree=inverse_degree,
            inverse_nonconstant_W1=ball_record(Wnorm),
            complete_inverse_remainder_W1=ball_record(inverse_error),
            discarded_nonmean_polynomial_tail_W1=ball_record(norm(tail, tau)),
            source_derivative_error_at_fixed_candidate_mean_W1=ball_record(full_source_projection_error),
            source_error_scope="Only finite inverse/projection discrepancy at the saved candidate mean; R44 separately restores the true complete mean and computes the actual candidate defect",
            source_coordinate="The same original endpoint source x used by r_x and ell",
            mathematical_candidate_definition="All binary Q/L are exact stored constants; H=r^4Q and Kbar=sqrt2*L_nonmean-P_theta on the fixed real source. Kbar_x is the saved-mode projection of the stated finite inverse-polynomial PDE expression.",
            complete_mean_root_solved=False, exact_connection_momentum_matched=False,
            exact_radial_solution_derivative_claimed=False,
            new_angular_quadrature_or_radial_flow=False))

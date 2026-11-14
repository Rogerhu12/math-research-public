"""Prepared R44 certificate for a continuous compatible outer-height panel.

The physical-r wrapper uses an explicitly specified cosine polynomial.
The R48 wrapper supplies fields from the same weighted source integral.
The shared private core is only an evaluator: its callers must establish
the same-height derivative identities.  Background interval inputs must
enclose the same R26 source functions on the panel.  All mean evaluations use finite Laurent
convolutions plus explicit infinite-series remainder bounds.

No saved node value is silently promoted to a radial enclosure; this
module has not yet been run on the actual outer trajectory.  It starts
no ODE, BVP, Node worker, angular quadrature or new source integration.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction
from math import comb

from flint import acb, arb
from closure_real_head_source_enclosure import exact_q, ball_record
from tail_r41_connection_polynomial import (
    real, add, scale, product, derivative, norm)
from tail_r41_general_connection_polynomial import real_lower


ONE = {0: acb(1)}


def constant(value):
    return {0: acb(real(value))}


def real_upper(poly):
    center = poly.get(0, acb(0)).real
    radius = sum((abs(value) for mode, value in poly.items() if mode), arb(0))
    return (center + radius).upper()


def powers(poly, degree):
    out = [ONE]
    for unused in range(degree):
        out.append(product(out[-1], poly))
    return out


def linear_combination(polynomials, coefficients):
    return add(*(scale(poly, coefficient)
                 for poly, coefficient in zip(polynomials, coefficients)))


def scalar_polynomial(coefficients, t):
    """Horner evaluation; the coefficients denote one fixed polynomial."""
    value = arb(0)
    for coefficient in reversed(coefficients):
        value = value*t + real(coefficient)
    return value


def hermite_cosine_coefficients(left_h, left_hr, left_hrr,
                                right_h, right_hr, right_hrr, width):
    """R44.7 in powers of t=(r-left)/width, with physical-r jets."""
    width = real(width)
    if not width > 0:
        raise ValueError("The true physical radial width must be positive")
    fields = (left_h, left_hr, left_hrr, right_h, right_hr, right_hrr)
    modes = set(left_h)
    if any(set(field) != modes for field in fields):
        raise ValueError("All six endpoint spectra must contain the same modes")
    if any(not isinstance(m, int) or m <= 0 or m % 2 for m in modes):
        raise ValueError("Use the complete positive even cosine modes")
    half = Fraction(1, 2)
    bases = (
        [1, 0, 0, -10, 15, -6],
        [0, 1, 0, -6, 8, -3],
        [0, 0, half, -3*half, 3*half, -half],
        [0, 0, 0, 10, -15, 6],
        [0, 0, 0, -4, 7, -3],
        [0, 0, 0, half, -1, half],
    )
    factors = (arb(1), width, width*width, arb(1), width, width*width)
    return {
        m: [
            sum((real(field[m])*factor*exact_q(basis[j])
                 for field, factor, basis in zip(fields, factors, bases)), arb(0))
            for j in range(6)
        ]
        for m in sorted(modes)
    }


def height_jet(coefficients, radius, left, width):
    """Return signed Laurent H,H_r,H_rr from the identical radial polynomial."""
    radius, left, width = real(radius), real(left), real(width)
    if not width > 0:
        raise ValueError("The polynomial's true physical width must be positive")
    t = (radius-left)/width
    H, Hr, Hrr = {}, {}, {}
    for m, row in sorted(coefficients.items()):
        if not isinstance(m, int) or m <= 0 or m % 2:
            raise ValueError("A real pi-periodic cosine height is required")
        if not row or len(row) > 6:
            raise ValueError("Use a radial polynomial of degree at most five")
        first = [j*real(row[j]) for j in range(1, len(row))]
        second = [j*(j-1)*real(row[j]) for j in range(2, len(row))]
        for target, value in (
            (H, scalar_polynomial(row, t)),
            (Hr, scalar_polynomial(first, t)/width),
            (Hrr, scalar_polynomial(second, t)/(width*width)),
        ):
            target[m] = target[-m] = acb(value/2)
    return H, Hr, Hrr


def algebra(P, Kbar, c, z):
    K = add(Kbar, constant(c))
    y = add(ONE, K)
    E = 1+z
    T = derivative(P)
    P2 = product(P, P)
    v = scale(P2, z)
    S = add(ONE, scale(v, -1))
    A = add(scale(K, 2), product(K, K), scale(P2, E))
    u = scale(A, z)
    Y = product(y, T)
    L = add(y, scale(T, E))
    return dict(K=K, y=y, E=E, T=T, P2=P2, v=v, S=S,
                A=A, u=u, Y=Y, L=L)


def series_tail(q, degree):
    return (q**(degree+1)/(1-q)).upper()


def derivative_tail(q, degree):
    return (q**degree*((degree+1)-degree*q)/(1-q)**2).upper()


def mean_enclosure(P, Kbar, c, z, tau, N, J,
                   Px=None, Kbarx=None, zx=None):
    """The full mean, its c derivative, and optionally fixed-c x derivative.

Every returned interval encloses the exact angular integral.  The
imaginary coefficient-zero component is discarded only because input
reality is guaranteed by the cosine-height construction.
"""
    a = algebra(P, Kbar, c, z)
    un, vn = norm(a["u"], tau), norm(a["v"], tau)
    if not un < 1 or not vn < 1:
        raise ValueError("The full binomial/geometric Wiener gates failed")
    up = powers(a["u"], N)
    vp = powers(a["v"], J)
    aa = [Fraction(comb(2*n, n), 4**n) for n in range(N+2)]
    CN = linear_combination(up, aa[:N+1])
    C1N = linear_combination(up, aa[1:N+2])
    WN = linear_combination(up, [(2*n+1)*aa[n] for n in range(N+1)])
    geo = add(*vp)
    BJ = product(a["Y"], geo)
    F = add(product(a["A"], C1N), product(BJ, CN))
    An, Yn = norm(a["A"], tau), norm(a["Y"], tau)
    Bn = (Yn/(1-vn)).upper()
    tC, tB = series_tail(un, N), series_tail(vn, J)
    eB = (Yn*tB).upper()
    cn = (1/(1-un).sqrt()).upper()
    error = ((An+Bn)*tC+eB*cn).upper()
    M = F.get(0, acb(0)).real + (-error).union(error)
    # (1-u)^(-3/2) has coefficient (2n+1)*a_n <= 2n+1.
    wtail = (un**(N+1)*((2*N+3)-(2*N+1)*un)/(1-un)**2).upper()
    mc_error = (norm(a["L"], tau)*wtail).upper()
    Mc_poly = product(a["L"], WN)
    Mc = Mc_poly.get(0, acb(0)).real + (-mc_error).union(mc_error)
    result = dict(mean=M, mean_error=error, mean_c_derivative=Mc,
                  mean_c_derivative_error=mc_error, u_norm=un, v_norm=vn,
                  polynomial_degree=max(map(abs, F), default=0))
    if Px is None:
        return result
    if Kbarx is None or zx is None:
        raise ValueError("All fixed-c radial derivatives must be supplied together")
    Tx = derivative(Px)
    Ax = add(scale(product(a["y"], Kbarx), 2),
             scale(a["P2"], zx), scale(product(P, Px), 2*a["E"]))
    vx = add(scale(a["P2"], zx), scale(product(P, Px), 2*z))
    ux = add(scale(a["A"], zx), scale(Ax, z))
    Yx = add(product(Kbarx, a["T"]), product(a["y"], Tx))
    CNp = linear_combination(up[:N], [n*aa[n] for n in range(1, N+1)])
    C1Np = linear_combination(up[:N], [n*aa[n+1] for n in range(1, N+1)])
    geop = linear_combination(vp[:J], list(range(1, J+1)))
    BJx = add(product(Yx, geo), product(a["Y"], product(geop, vx)))
    Fx = add(product(Ax, C1N), product(a["A"], product(C1Np, ux)),
             product(BJx, CN), product(BJ, product(CNp, ux)))
    Axn, Yxn, uxn, vxn = (norm(p, tau) for p in (Ax, Yx, ux, vx))
    Bxn = (Yxn/(1-vn)+Yn*vxn/(1-vn)**2).upper()
    eBx = (Yxn*tB+Yn*derivative_tail(vn, J)*vxn).upper()
    cpn = (1/(2*(1-un)*(1-un).sqrt())).upper()
    xerror = ((Axn+Bxn)*tC
              +(An+Bn)*derivative_tail(un, N)*uxn
              +eBx*cn+eB*cpn*uxn).upper()
    Mx = Fx.get(0, acb(0)).real + (-xerror).union(xerror)
    result.update(mean_fixed_c_x_derivative=Mx,
                  mean_fixed_c_x_derivative_error=xerror)
    return result


def certify_height_panel(coefficients, *, radius, radius_x, left, width,
                         w, log_w_x, mean_candidate, mean_radius,
                         tau=Fraction(1, 64), binomial_degree=8,
                         geometric_degree=8):
    """Apply R44 to the supplied same-function background panel enclosures.

The returned result is conditional on those background enclosures.
It does not assert that the polynomial is the exact radial solution.
All identities connecting H,Hr,Hrr are enforced internally.
"""
    radius, radius_x, left, width, w, ell = map(
        real, (radius, radius_x, left, width, w, log_w_x))
    if not width > 0:
        raise ValueError("The polynomial's true physical width must be positive")
    H, Hr, Hrr = height_jet(coefficients, radius, left, width)
    Kbar = scale(Hr, 1/w)
    Kbarx = add(scale(Hrr, radius_x/w), scale(Kbar, -ell))
    return _certify_same_height_fields(
        H, Kbar, Kbarx, radius=radius, radius_x=radius_x, w=w,
        log_w_x=ell, mean_candidate=mean_candidate, mean_radius=mean_radius,
        tau=tau, binomial_degree=binomial_degree, geometric_degree=geometric_degree,
        construction="Identical physical-r cosine polynomial and its first two derivatives")


def _certify_same_height_fields(H, Kbar, Kbarx, *, radius, radius_x, w,
                                log_w_x, mean_candidate, mean_radius,
                                tau=Fraction(1, 64), binomial_degree=8,
                                geometric_degree=8, construction):
    """Internal R44 algebra for compatible fields supplied by a constructor.

The caller must prove H_x=r_x*w*Kbar and that Kbarx is its actual source
derivative.  Interval arithmetic alone cannot establish those identities.
Only the polynomial wrapper above and the R48 weighted-integral wrapper
use this entry.  The field coefficients must have conjugate symmetry.
"""
    radius, radius_x, w, ell = map(real, (radius, radius_x, w, log_w_x))
    tau, center, radius_c = map(real, (tau, mean_candidate, mean_radius))
    N, J = int(binomial_degree), int(geometric_degree)
    if N < 0 or J < 0 or not tau >= 0:
        raise ValueError("Nonnegative exact degrees and angular width are required")
    if not radius > 0 or not radius_x > 0 or not w > 0 or not radius_c > 0:
        raise ValueError("Positive real radius/source speed/w/mean radius are required")
    modes = set(H) | set(Kbar) | set(Kbarx)
    if any(not isinstance(m, int) or m == 0 or m % 2 for m in modes):
        raise ValueError("Nonmean even Fourier fields are required")
    maximum_mode = max(map(abs, modes), default=0)
    s, z = radius_x/radius, w*w
    E, zx = 1+z, 2*z*ell
    P = scale(derivative(H), 1/(radius*w))
    Px = add(scale(derivative(Kbar), s), scale(P, -(s+ell)))
    bracket = center + (-radius_c).union(radius_c)
    whole = algebra(P, Kbar, bracket, z)
    un, vn = norm(whole["u"], tau), norm(whole["v"], tau)
    ylo, Llo = real_lower(whole["y"]), real_lower(whole["L"])
    Nnumlo = real_lower(add(whole["S"], scale(whole["Y"], z)))
    gates = dict(
        D_Wiener=bool(un < 1), S_Wiener=bool(vn < 1),
        positive_y=bool(ylo > 0), positive_unsquared_numerator=bool(Nnumlo > 0),
        positive_leading=bool(Llo > 0))
    out = dict(
        status="Prepared R44 same-function panel calculation",
        scope="A compatible continuous height candidate, not existence of the exact outer radial solution",
        no_angular_quadrature=True, no_radial_flow=True,
        height_construction=construction,
        complete_mean_and_all_residual_frequencies=True,
        compatibility_residual_exactly_zero_by_construction=True,
        background_enclosure_obligation="The supplied r,r_x,w,ell boxes must enclose the same R26 functions over the entire panel",
        background_enclosure_certified_by_this_module=False,
        Darboux_tolerance_tested=False,
        maximum_height_mode=maximum_mode,
        mean_bracket=ball_record(bracket), tau=ball_record(tau),
        binomial_degree=N, geometric_degree=J,
        bracket_u_norm=ball_record(un), bracket_v_norm=ball_record(vn),
        bracket_y_lower=ball_record(ylo), bracket_leading_lower=ball_record(Llo),
        bracket_N_numerator_lower=ball_record(Nnumlo), gates=gates)
    if not all(gates.values()):
        out.update(complete_mean_and_branch_gate=False, failure="A whole-mean-bracket Wiener/branch gate failed")
        return out
    mu = (Llo/((1+un)*(1+un).sqrt())).lower()
    candidate = mean_enclosure(P, Kbar, center, z, tau, N, J)
    epsilon = abs(candidate["mean"]).upper()
    correction = (epsilon/mu).upper()
    gates["complete_mean_root"] = bool(correction < radius_c)
    out.update(
        mean_uniform_derivative_lower=ball_record(mu),
        complete_candidate_mean_residual=ball_record(candidate["mean"]),
        complete_mean_correction_upper=ball_record(correction),
        candidate_mean_series_remainder=ball_record(candidate["mean_error"]))
    if not gates["complete_mean_root"]:
        out.update(complete_mean_and_branch_gate=False, failure="The exact complete mean root is not enclosed")
        return out
    c = center + (-correction).union(correction)
    full = mean_enclosure(P, Kbar, c, z, tau, N, J, Px, Kbarx, zx)
    if not full["mean"].lower() <= 0 or not full["mean"].upper() >= 0:
        raise ArithmeticError("The proved root enclosure lost zero in the complete mean equation")
    derivative_lo = max(mu, full["mean_c_derivative"].lower())
    derivative_hi = full["mean_c_derivative"].upper()
    if not derivative_lo <= derivative_hi:
        raise ArithmeticError("Independent complete-mean derivative enclosures do not intersect")
    mc = derivative_lo.union(derivative_hi)
    cx = -full["mean_fixed_c_x_derivative"]/mc
    actual = algebra(P, Kbar, c, z)
    Kx = add(Kbarx, constant(cx))
    U = add(derivative(actual["K"]), scale(P, -1))
    linear_ell = add(scale(actual["K"], 2),
                     product(actual["K"], actual["K"]),
                     scale(actual["P2"], z), actual["Y"])
    residual = add(product(actual["L"], Kx),
                   scale(product(U, U), -E*s), scale(linear_ell, ell))
    degree = max(map(abs, residual), default=0)
    if degree > 2*maximum_mode:
        raise AssertionError("A frequency outside the proved finite residual support appeared")
    residual_norm = norm(residual, tau)
    residual_real_norm = norm(residual, arb(0))
    aL = (1+c.lower()-norm(add(Kbar, scale(actual["T"], E)), tau)).lower()
    darboux = (z*residual_real_norm/(radius*radius_x*E*E)).upper()
    source_norm = (residual_norm/aL).upper() if aL > 0 else None
    out.update(
        complete_mean_and_branch_gate=True, failure=None,
        actual_mean_c_enclosure=ball_record(c),
        actual_mean_c_x_enclosure=ball_record(cx),
        complete_mean_c_derivative_enclosure=ball_record(mc),
        complete_mean_fixed_c_x_derivative_enclosure=ball_record(full["mean_fixed_c_x_derivative"]),
        mean_derivative_series_remainder=ball_record(full["mean_fixed_c_x_derivative_error"]),
        residual_polynomial_degree=degree,
        residual_polynomial_W1=ball_record(residual_norm),
        residual_polynomial_zero_strip_W1=ball_record(residual_real_norm),
        actual_Darboux_defect_uniform_upper=ball_record(darboux),
        analytic_leading_inverse_margin=ball_record(aL),
        analytic_second_source_gate=bool(aL > 0),
        complete_second_source_W1=ball_record(source_norm) if source_norm is not None else None,
        second_source_coordinate="Original source x derivative of normalized K; no physical-r or R33-V conversion is implicit",
        residual_coefficients={
            str(m): dict(real=ball_record(value.real), imaginary=ball_record(value.imag))
            for m, value in sorted(residual.items())
        },
        exact_radial_solution_certified=False)
    return out

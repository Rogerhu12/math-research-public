#!/usr/bin/env python3
"""R624: one globally legal analytic input and its unique scalar paper branch.

This module is a source interface, not a completed BVP or a numerical proof.
All arithmetic execution is restricted to the named public Actions scope.
The exact rational reference moments use [4.01,5.99], not the wider [4,6]
support window. The sole scalar root is the one proved in [0,1/15] by R624.
The complete finite-width equations, potential and history remain elsewhere.
"""
from __future__ import annotations

from fractions import Fraction
import time

import mpmath as mp
import numpy as np

import r612_r614_reduced_function_map_agent as reduced


def _add(*polynomials):
    result = [Fraction(0)]*max(map(len, polynomials))
    for polynomial in polynomials:
        for degree, coefficient in enumerate(polynomial):
            result[degree] += coefficient
    return result


def _scale(polynomial, multiplier):
    return [multiplier*coefficient for coefficient in polynomial]


def _multiply(left, right):
    result = [Fraction(0)]*(len(left)+len(right)-1)
    for i, lhs in enumerate(left):
        for j, rhs in enumerate(right):
            result[i+j] += lhs*rhs
    return result


def _fraction_text(value):
    return f"{value.numerator}/{value.denominator}"


def _mp_fraction(value):
    return mp.mpf(value.numerator)/value.denominator


def exact_paper_constants(clock):
    """Evaluate rational identities, only in public science; no sampled rule."""
    reduced.require_public_science()
    clock.check("before_r624_exact_reference_moments")
    left, right = Fraction(401, 100), Fraction(599, 100)
    moments = [Fraction(50, 99)*(right**(degree+1)-left**(degree+1))/(degree+1)
               for degree in range(11)]

    def integral(polynomial):
        if len(polynomial) > len(moments):
            raise ValueError("R624 uses the proved common degree-ten moments only.")
        return sum((coefficient*moments[degree]
                    for degree, coefficient in enumerate(polynomial)), Fraction(0))

    one = Fraction(1)
    Q = [one, Fraction(0), one]
    W = [Fraction(19, 48), Fraction(0), -Fraction(41, 112), Fraction(0), Fraction(1, 2)]
    y, y2 = [Fraction(0), one], [Fraction(0), Fraction(0), one]
    W2, Q2 = _multiply(W, W), _multiply(Q, Q)
    T1 = integral(_multiply(y, W2))
    S1 = -integral(_multiply(y, _multiply(Q2, W)))
    r = T1/(-S1)
    a, beta = 1-r, 1-r-Fraction(1, 16)
    Bc = integral(_multiply(Q, W2))
    S0 = -integral(_multiply(Q2, W))
    Vss_at_j_zero = [(-Fraction(1, 2)+2*a)/8, Fraction(0),
                    (Fraction(3, 2)+a)/8, Fraction(0), Fraction(1, 8)]
    # N=B''-Bc/8. This includes Q'', 4 Q' V V', 2 Q(V')^2 and 2 Q V V''.
    N0 = integral(_add(
        _scale(_multiply(y2, W2), 2*a-Fraction(1, 8)),
        _scale(_multiply(_multiply(Q, y2), W), -r/2),
        _scale(_multiply(_multiply(Q2, Q), y2), r*r/8),
        _scale(_multiply(_multiply(Q, W), Vss_at_j_zero), -2)))
    if not (Fraction(9, 20) < r < Fraction(7, 15) and Bc > 0 and S0 < 0 and S1 < 0):
        raise ArithmeticError("The fixed R624 exact rational identity was misassembled.")
    clock.check("after_r624_exact_reference_moments")
    return {"r":r, "a":a, "beta":beta, "Bc":Bc, "S0":S0, "S1":S1,
            "T1":T1, "N_at_j_zero":N0}


class CompatibleFreeCenterInput:
    """The single m=41 R624 input; full history is never manufactured here."""
    def __init__(self, clock, progress=None):
        reduced.require_public_science()
        started = time.monotonic()
        self.clock, self.points = clock, 0
        self.integrand_evaluations = self.scalar_function_evaluations = 0
        self.progress = {} if progress is None else progress
        self.progress.update({"stage":"exact_reference_constants", "completed":False})
        try:
            self._initialize()
        finally:
            elapsed = time.monotonic()-started
            self.progress.update({"seconds":elapsed,
                                  "endpoint_integrand_evaluations":self.integrand_evaluations,
                                  "scalar_function_evaluations":self.scalar_function_evaluations,
                                  "analytic_shape_points":self.points})
            if hasattr(self, "input_receipt"):
                self.input_receipt["seconds"] = elapsed
                self.progress["receipt"] = self.input_receipt

    def _initialize(self):
        clock = self.clock
        self.length, self.mode = 3., 41
        constants = exact_paper_constants(clock)
        self.progress["stage"] = "unique_paper_branch"
        clock.check("before_r624_unique_input_branch")
        with mp.workdps(60):
            a = _mp_fraction(constants["a"])
            beta = _mp_fraction(constants["beta"])
            Bc, S0 = _mp_fraction(constants["Bc"]), _mp_fraction(constants["S0"])
            N0 = _mp_fraction(constants["N_at_j_zero"])
            A = 9*a/mp.pi**2
            h_end = 1+2*A
            alpha = 3/mp.pi
            third = (mp.mpf(8)/5-alpha)/3
            cubic = 4*third
            k_end_magnitude = alpha+cubic
            J0 = mp.atan(mp.sqrt(2*A))/mp.sqrt(2*A)
            J2 = (1-J0)/(2*A)
            eta_base_end = -(alpha*J0+3*cubic*J2)/2
            d_base = h_end*eta_base_end+k_end_magnitude
            j_base = mp.pi**2/8-8*mp.pi**3/135
            slope = 400*mp.pi**3/9
            C20 = (N0+j_base*S0/4)/(2*beta)
            kappa = -slope*S0/(8*beta)

            def integrand(x):
                self.integrand_evaluations += 1
                clock.check("during_r624_unique_input_endpoint_integral")
                u = mp.pi*x/2
                h = 1+A*(1-mp.cos(mp.pi*x))
                hx = A*mp.pi*mp.sin(mp.pi*x)
                minus_psi = 4*mp.sin(u)*mp.sin(20*u)**2
                return (h_end/2)*minus_psi*hx/h**2

            clock.check("before_r624_unique_input_endpoint_integral")
            self.progress["stage"] = "true_endpoint_increment_integral"
            cuts = [mp.mpf(i)/32 for i in range(33)]
            D, estimated_error = mp.quad(integrand, cuts, method="tanh-sinh",
                                         maxdegree=7, error=True)
            clock.check("after_r624_unique_input_endpoint_integral")

            def phi(q):
                self.scalar_function_evaluations += 1
                d = d_base+D*q
                G = h_end**2/(1+d*d)-1
                return Bc+(C20-kappa*q)*G

            lower, upper = mp.mpf(0), mp.mpf(1)/15
            self.progress["stage"] = "unique_scalar_bisection"
            f_lower, f_upper = phi(lower), phi(upper)
            if not (f_lower > 0 and f_upper < 0):
                raise ArithmeticError("Numerical evaluation lost the fixed R624 paper bracket.")
            endpoint_values = [mp.nstr(f_lower/Bc, 55), mp.nstr(f_upper/Bc, 55)]
            for _ in range(180):
                clock.check("during_r624_unique_scalar_branch_bisection")
                midpoint = (lower+upper)/2
                value = phi(midpoint)
                if value > 0:
                    lower = midpoint
                else:
                    upper = midpoint
            q_star = (lower+upper)/2
            d_star = d_base+D*q_star
            G_star = h_end**2/(1+d_star*d_star)-1
            G_prime = -2*h_end**2*d_star*D/(1+d_star*d_star)**2
            phi_prime = -kappa*G_star+(C20-kappa*q_star)*G_prime
            self.increment = float(q_star)
            self.a = float(a)
            self.input_receipt = {
                "definition":"R624, the unique root of Phi on [0,1/15], m=41",
                "full_finite_width_bvp_solved":False,
                "leading_energy_equations_along_trial_curve_solved":False,
                "initial_true_A_terminal_projection_performed":False,
                "reference_interval":["401/100", "599/100"],
                "reference_identity":"normalized continuous moments through degree 10",
                "exact_rational_constants":{key:_fraction_text(value)
                                              for key, value in constants.items()},
                "mpmath_decimal_digits":60,
                "endpoint_integral":{
                    "quantity":"D=(h_L/2) integral (-psi) h_x/h^2 dx",
                    "value":mp.nstr(D, 55),
                    "method":"tanh-sinh, 32 fixed panels, maxdegree 7",
                    "estimated_absolute_error":mp.nstr(estimated_error, 12),
                    "error_estimate_is_rigorous_bound":False,
                    "evaluations":self.integrand_evaluations},
                "eta_base_end_closed_form":mp.nstr(eta_base_end, 55),
                "original_d_base":mp.nstr(d_base, 55),
                "q_star_numerical_approximation":mp.nstr(q_star, 55),
                "evaluated_root_bracket":[mp.nstr(lower, 58), mp.nstr(upper, 58)],
                "root_bracket_includes_integration_error":False,
                "scalar_bisection_steps":180,
                "Phi_over_Bc_at_original_bracket":endpoint_values,
                "Phi_over_Bc_at_selected_approximation":mp.nstr(phi(q_star)/Bc, 20),
                "minus_Phi_prime_over_Bc":mp.nstr(-phi_prime/Bc, 30),
                "C2_over_Bc":mp.nstr((C20-kappa*q_star)/Bc, 30),
                "original_d_end":mp.nstr(d_star, 30),
                "R_end_squared_minus_one":mp.nstr(G_star, 30),
                "paper_full_domain_margins":{
                    "h":["1", "21/10"], "absolute_k_upper":"11/6",
                    "eta":["-11/12", "2/15"], "absolute_h_s_upper":"11/20",
                    "absolute_k_s_upper":"79/18", "kinetic_surplus_lower":"1/45",
                    "center_beta_lower":"113/240", "scalar_root_slope_over_Bc_lower":"8"},
                "numerical_input_is_rigorous_interval_certificate":False}
        # The actual binary64 curve and its physical center jets use one set
        # of stored constants. The subsequent full-history evaluation pays
        # its actual residuals; the mp scalar root is not a finite-width root.
        pi = np.pi
        self.third_amplitude = (8/5-3/pi)/3
        self.height_amplitude = 9*self.a/pi**2
        j = pi*pi/8-8*pi**3/135+(400*pi**3/9)*self.increment
        f = -self.a*pi*pi/9
        self.parameters = np.asarray([1., -.5, -7/5, -1., -1/7, 1/6,
                                      self.a, j, f, 3.])
        self.input_receipt["actual_binary64_increment"] = self.increment
        self.input_receipt["actual_binary64_parameters"] = self.parameters.tolist()
        self.input_receipt["scalar_function_evaluations"] = self.scalar_function_evaluations
        self.progress.update({"stage":"complete_analytic_input", "completed":True})
        clock.check("after_r624_unique_input_branch")

    def shape(self, x):
        reduced.require_public_science()
        self.clock.check("before_r624_analytic_shape")
        x = np.asarray(x, float).reshape(-1)
        self.points += len(x)
        pi, b, q = np.pi, self.third_amplitude, self.increment
        u = pi*x/2
        su, cu = np.sin(u), np.cos(u)
        sn, cn = np.sin(20*u), np.cos(20*u)
        h = 1+self.height_amplitude*(1-np.cos(pi*x))
        hx = 9*self.a/pi*np.sin(pi*x)
        hxx = 9*self.a*np.cos(pi*x)
        psi = -4*su*sn**2
        psi_u = -4*cu*sn**2-160*su*sn*cn
        psi_uu = 4*su*sn**2-320*cu*sn*cn-3200*su*(cn**2-sn**2)
        k = -8/5*su+b*np.sin(3*u)-q*psi
        kx = (pi/2)*(-8/5*cu+3*b*np.cos(3*u)-q*psi_u)
        kxx = (pi/2)**2*(8/5*su-9*b*np.sin(3*u)-q*psi_uu)
        hx[(x == 0.) | (x == 1.)] = 0.
        k[x == 0.] = 0.
        kx[x == 0.] = -1.5
        kx[x == 1.] = 0.
        kxx[x == 0.] = 0.
        self.clock.check("after_r624_analytic_shape")
        return np.column_stack((h, k, hx, kx, hxx, kxx))

    def center_jets(self):
        return self.parameters[[6, 7, 8]].tolist()

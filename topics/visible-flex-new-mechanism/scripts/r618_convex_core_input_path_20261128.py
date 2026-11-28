#!/usr/bin/env python3
"""Actual same-perimeter core input path from an accepted total P to R579.

phi is ALWAYS the outward normal angle.  In the old position convention
psi=phi+pi/2, so Y_theta=R*(-sin(phi),cos(phi)).  The right support point is
at theta=phi=0.  There is no extra planar rotation or phase adjustment.

This supplies a fixed continuous target and finite Fourier observations,
not a connection root or a source/angular error certificate.  In particular
R579's epsilon=.001 can require much more than J48.  It never selects mu.
All numerical work requires this repository's public Actions environment.
"""
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
HARD_TRACE_MODEL_SHA = 'a55832af74577a86e850905dc16c39997a4cd095aca23bcb5aa35e64e9798c62'
COUNTS = defaultdict(int)


def _sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def _scalar(value):
    return float(np.asarray(value))


class ConvexCoreInputPath:
    """One immutable exact seed function, evaluated by declared finite rules."""
    def __init__(self, actual_hard_trace_model, *, quadrature_epsabs,
            quadrature_epsrel, quadrature_limit, ode_atol, ode_rtol,
            ode_max_step, root_xtol, maximum_seed_positivity_nodes):
        model = actual_hard_trace_model
        module = sys.modules.get(type(model).__module__)
        path = HERE / 'r618_hard_total_trace_model_20261128.py'
        if (module is None or Path(module.__file__).resolve() != path.resolve()
                or type(model) is not module.HardTotalTraceHeight
                or hashlib.sha256(path.read_bytes()).hexdigest() != HARD_TRACE_MODEL_SHA):
            raise ValueError('the actual accepted-source hard-trace model is required')
        module.chain.public_only()
        self.model, self.source_provenance = model, model.guard()
        self.R = float(model.par.R)
        if self.R != .85:
            raise ValueError('the R579 target has the same fixed R=.85')
        self.modes = model.modes.copy()
        self.seed_pc = model.seed_pc.copy()
        self.seed_source_e = float(model.seed_trace['e'])
        if (not all(np.isfinite(value) and value > 0 for value in
                (quadrature_epsabs, quadrature_epsrel, ode_atol, ode_rtol, ode_max_step, root_xtol))
                or type(quadrature_limit) is not int or quadrature_limit < 2
                or type(maximum_seed_positivity_nodes) is not int
                or maximum_seed_positivity_nodes < 4 * int(self.modes[-1])):
            raise ValueError('complete positive finite numerical input rules are required')
        self.settings = {'quadrature_epsabs': float(quadrature_epsabs),
            'quadrature_epsrel': float(quadrature_epsrel), 'quadrature_limit': quadrature_limit,
            'ode_atol': float(ode_atol), 'ode_rtol': float(ode_rtol),
            'ode_max_step': float(ode_max_step), 'root_xtol': float(root_xtol),
            'maximum_seed_positivity_nodes': maximum_seed_positivity_nodes}
        self.quadrature_errors, self.root_receipt = [], None
        self.seed_e = self._continuous_seed_root()
        self.seed_normal_solution = solve_ivp(self._seed_theta_rhs, (0., np.pi/2), [0.],
            method='DOP853', dense_output=True, atol=ode_atol, rtol=ode_rtol, max_step=ode_max_step)
        if not self.seed_normal_solution.success:
            raise ArithmeticError('actual seed normal-angle inversion failed: ' + self.seed_normal_solution.message)
        COUNTS['seed_normal_angle_ODE_rhs'] += int(self.seed_normal_solution.nfev)
        self.seed_quarter_material_angle_error = abs(float(self.seed_normal_solution.y[0, -1]) - np.pi/2)
        self.epsilon = .001
        L = 4 * self._integral(lambda phi: np.sqrt(np.cos(phi)**2
            + self.epsilon**2*np.sin(phi)**2), 'R579_ellipse_support_quarter')
        c = L / (1 + self.epsilon)
        self.rounding = (c * (1. + .37) - 2*np.pi*self.R) / (2*c - 2*np.pi)
        self.p = (1-self.rounding-self.epsilon*(.37-self.rounding))/(1-self.epsilon**2)
        self.q = (.37-self.rounding-self.epsilon*(1-self.rounding))/(1-self.epsilon**2)
        if not (.075 < self.rounding < .09 and self.p > 0 and self.q > 0):
            raise ArithmeticError('numerical evaluation of the proved R579 constants left its strict bounds')
        self.seed_A = self._integral(lambda phi: self.rho0(phi)[0]*np.sin(phi), 'seed_right_support')
        self.seed_B = self._integral(lambda phi: self.rho0(phi)[0]*np.cos(phi), 'seed_upper_support')
        self.definition = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'actual_accepted_seed_source': model.accepted_source,
            'seed_positive_even_modes': self.modes.tolist(), 'seed_P0_coefficients': self.seed_pc.tolist(),
            'seed_e_definition': 'mean_theta((e+2P_seed)^(-1/2))=1',
            'R_exact': '17/20', 'R579_epsilon_exact': '1/1000',
            'R579_A_exact': '1', 'R579_B_exact': '37/100',
            'R579_r_p_q_definition': 'R579 equations (2),(3),(4)',
            'path': 'rho_mu=(1-mu)*rho_seed+mu*rho_R579; theta_phi=rho_mu/R',
            'normal_angle_convention': 'phi=0 at right support; psi=phi+pi/2; Y_theta=R*(-sin(phi),cos(phi))',
            'no_grid_dependent_target_or_extra_rotation': True}
        self.definition_sha256 = _sha(self.definition)
        COUNTS['actual_continuous_core_input_paths'] += 1

    def _check(self):
        self.model.driver.check(self.model.deadline)

    def _integral(self, function, label):
        def checked(phi):
            self._check()
            COUNTS['path_quadrature_integrand_evaluations'] += 1
            return _scalar(function(phi))
        value, error = quad(checked, 0., np.pi/2,
            epsabs=self.settings['quadrature_epsabs'], epsrel=self.settings['quadrature_epsrel'],
            limit=self.settings['quadrature_limit'])
        if not np.isfinite(value) or not np.isfinite(error):
            raise ArithmeticError('nonfinite actual core path quadrature: ' + label)
        self.quadrature_errors.append({'purpose': label, 'absolute_error_estimate_observation': float(error)})
        COUNTS['path_quadrature_calls'] += 1
        return float(value)

    def _seed_fields(self, theta):
        theta = np.asarray(theta, dtype=float)
        co, si = np.cos(self.modes[:, None] * theta.reshape(1, -1)), np.sin(self.modes[:, None] * theta.reshape(1, -1))
        P = self.seed_pc @ co
        Pt = -(self.modes * self.seed_pc) @ si
        Ptt = -(self.modes**2 * self.seed_pc) @ co
        return P.reshape(theta.shape), Pt.reshape(theta.shape), Ptt.reshape(theta.shape)

    def _continuous_seed_root(self):
        # For a grid with spacing h, P >= min_grid(P)-h*sum(j|pc_j|)/2.
        # This analytic inequality controls the bracket's domain; floating
        # evaluation/roundoff are still recorded as unproved errors.
        lipschitz = float(np.sum(self.modes * abs(self.seed_pc)))
        nodes = max(128, 4*int(self.modes[-1]))
        evaluations = []
        def turning(e):
            def integrand(theta):
                P = _scalar(self._seed_fields(theta)[0])
                u2 = e + 2*P
                if u2 <= 0:
                    raise ArithmeticError('continuous seed root evaluator left its positive domain')
                u = np.sqrt(u2)
                return (1-u2)/(u*(1+u))
            value = 2/np.pi*self._integral(integrand, 'seed_continuous_turning')
            evaluations.append([float(e), float(value)])
            return value
        while nodes <= self.settings['maximum_seed_positivity_nodes']:
            theta = np.linspace(0., np.pi/2, nodes+1)
            P = self._seed_fields(theta)[0]
            lower = float(np.min(P) - lipschitz*(np.pi/2/nodes)/2)
            scale = max(1., abs(self.seed_source_e), abs(2*lower))
            floor = -2*lower + 64*np.finfo(float).eps*scale
            left = max(floor, self.seed_source_e-.125*scale)
            fl = turning(left)
            if fl <= 0 and left > floor:
                left, fl = floor, turning(floor)
            if fl > 0:
                break
            nodes *= 2
        else:
            raise ArithmeticError('declared positivity-grid range did not bracket the same continuous seed root')
        right = max(self.seed_source_e+.125*scale, floor+1.)
        fr = turning(right)
        if fr >= 0:
            raise ArithmeticError('same continuous seed root right bracket not negative')
        root, receipt = brentq(turning, left, right, xtol=self.settings['root_xtol'],
            rtol=4*np.finfo(float).eps, full_output=True, disp=False)
        if not receipt.converged:
            raise ArithmeticError('same continuous seed root did not converge')
        COUNTS['continuous_seed_scalar_root_evaluations'] += len(evaluations)
        self.root_receipt = {'source_same_seed_e_from_original_rule': self.seed_source_e,
            'continuous_rule_e_observation': float(root), 'difference_observation': float(root-self.seed_source_e),
            'source_seed_P0_unchanged': True, 'positivity_grid_nodes': nodes,
            'P_lower_from_Lipschitz_grid_observation': lower,
            'same_continuous_root_bracket': [left, right],
            'iterations': int(receipt.iterations), 'scalar_evaluations': evaluations,
            'continuous_root_and_roundoff_error_enclosed': False}
        return float(root)

    def _seed_theta_rhs(self, phi, theta):
        self._check()
        P = _scalar(self._seed_fields(float(theta[0]))[0])
        u2 = self.seed_e+2*P
        if u2 <= 0:
            raise ArithmeticError('seed normal-angle ODE left positivity')
        return [np.sqrt(u2)]

    @staticmethod
    def _fold_quarter(value):
        remainder = np.mod(np.asarray(value, dtype=float), np.pi)
        first = remainder <= np.pi/2
        return np.where(first, remainder, np.pi-remainder), np.where(first, 1., -1.)

    def rho0(self, phi):
        """rho_seed and its true derivative with respect to NORMAL angle."""
        folded, sign = self._fold_quarter(phi)
        shape = folded.shape
        theta = self.seed_normal_solution.sol(folded.reshape(-1))[0].reshape(shape)
        P, Pt, _ = self._seed_fields(theta)
        u2 = self.seed_e+2*P
        if np.any(u2 <= 0):
            raise ArithmeticError('same seed curvature radius left positivity')
        return self.R*np.sqrt(u2), sign*self.R*Pt

    def rho1(self, phi):
        """R579 equation(7), same outward normal and same coordinate axes."""
        phi = np.asarray(phi, dtype=float)
        s, c, eps2 = np.sin(phi), np.cos(phi), self.epsilon**2
        a2, b2 = c*c+eps2*s*s, s*s+eps2*c*c
        rho = self.p*eps2/a2**1.5+self.q*eps2/b2**1.5+self.rounding
        derivative = 3*eps2*(1-eps2)*s*c*(self.p/a2**2.5-self.q/b2**2.5)
        return rho, derivative

    def input(self, mu_literal, *, maximum_mode, angular_points):
        """Generate one explicitly chosen input and its full path derivative.

        Refining J or N always uses the same definition and literal mu.
        No input is judged to meet connection or macro surface criteria here.
        """
        self._check()
        if not isinstance(mu_literal, str):
            raise TypeError('mu must be a literal exact rational/decimal input string')
        mu_rational = Fraction(mu_literal)
        if not 0 <= mu_rational <= 1:
            raise ValueError('the declared convex path has 0<=mu<=1')
        mu = float(mu_rational)
        if (type(maximum_mode) is not int or maximum_mode % 2
                or maximum_mode < int(self.modes[-1])
                or type(angular_points) is not int or angular_points % 4
                or angular_points <= 4*maximum_mode):
            raise ValueError('all seed modes and explicit complete Fourier observation grids required')
        retained = np.arange(2, maximum_mode+1, 2)
        A = (1-mu)*self.seed_A+mu
        B = (1-mu)*self.seed_B+mu*.37
        def rhs(theta, state):
            self._check()
            phi = float(state[0])
            rho0, _ = self.rho0(phi)
            rho1, _ = self.rho1(phi)
            delta = _scalar(rho1-rho0)
            rho = _scalar(rho0+mu*delta)
            if rho <= 0:
                raise ArithmeticError('the actual convex input interpolation left positivity')
            rate = self.R/rho
            return [rate, delta*rate, -self.R*np.sin(phi), self.R*np.cos(phi)]
        solution = solve_ivp(rhs, (0., np.pi/2), [0., 0., A, 0.], method='DOP853',
            dense_output=True, atol=self.settings['ode_atol'], rtol=self.settings['ode_rtol'],
            max_step=self.settings['ode_max_step'])
        if not solution.success:
            raise ArithmeticError('actual path normal-angle inversion failed: '+solution.message)
        COUNTS['path_material_to_normal_ODE_rhs'] += int(solution.nfev)
        def e_increment(phi):
            rho0, _ = self.rho0(phi)
            rho1, _ = self.rho1(phi)
            d = rho1-rho0
            return mu*d*(3*rho0*rho0+3*mu*rho0*d+mu*mu*d*d)
        e_delta = 0. if mu_rational == 0 else 2/(np.pi*self.R**3)*self._integral(e_increment, 'same_path_e_increment')
        e = self.seed_e+e_delta
        def e_derivative(phi):
            rho0, _ = self.rho0(phi)
            rho1, _ = self.rho1(phi)
            return (rho0+mu*(rho1-rho0))**2*(rho1-rho0)
        edot = 6/(np.pi*self.R**3)*self._integral(e_derivative, 'same_path_e_derivative')
        def sample(n):
            theta = 2*np.pi*np.arange(n)/n
            folded, _ = self._fold_quarter(theta)
            values = solution.sol(folded)
            phi, integral_delta, X, Y = values
            rho0, rho0p = self.rho0(phi)
            rho1, rho1p = self.rho1(phi)
            rho = rho0+mu*(rho1-rho0)
            rhop = rho0p+mu*(rho1p-rho0p)
            u = rho/self.R
            phidot = -integral_delta/rho
            udot = (rho1-rho0+rhop*phidot)/self.R
            Pseed = self._seed_fields(theta)[0]
            deltaP = .5*(u*u-(self.seed_e+2*Pseed)-e_delta)
            if mu_rational == 0:
                # Exact endpoint input, not a drifted reconstruction of it.
                deltaP = np.zeros_like(Pseed)
            P = Pseed+deltaP
            Pdot = u*udot-edot/2
            coefficients = 2*np.fft.rfft(deltaP).real/n
            derivative_coefficients = 2*np.fft.rfft(Pdot).real/n
            pc = coefficients[retained].copy()
            for column, mode in enumerate(self.modes):
                pc[mode//2-1] += self.seed_pc[column]
            dpc = derivative_coefficients[retained]
            approx = pc @ np.cos(retained[:, None]*theta)
            dapprox = dpc @ np.cos(retained[:, None]*theta)
            # Symmetries reconstruct the same canonical curve.  The ODE's
            # quarter endpoint mismatch remains explicit; no axis rotation,
            # period rescaling, or normalization hides it.
            quadrant = np.floor(theta/(np.pi/2)).astype(int)%4
            points = np.stack([np.where(np.isin(quadrant, (0, 3)), X, -X),
                               np.where(np.isin(quadrant, (0, 1)), Y, -Y)], axis=1)
            return {'pc': pc, 'dpc': dpc,
                'P_constant_mode_observation': float(np.mean(P)),
                'Pdot_constant_mode_observation': float(np.mean(Pdot)),
                'sampled_full_target_P_range': [float(np.min(P)), float(np.max(P))],
                'sampled_full_target_u_range': [float(np.min(u)), float(np.max(u))],
                'sampled_J_projection_error': float(np.max(abs(approx-P))),
                'sampled_J_projection_derivative_error': float(np.max(abs(dapprox-Pdot))),
                'sampled_high_even_coefficient_l1_after_J': float(np.sum(abs(coefficients[maximum_mode+2::2]))),
                'sampled_core_ball_radius': float(np.max(np.linalg.norm(points, axis=1))),
                'sampled_positive_curvature_radius_minimum': float(np.min(rho)),
                'sampled_path_normal_angle_range_on_quarter': [float(np.min(phi)), float(np.max(phi))]}
        coarse, fine = sample(angular_points), sample(2*angular_points)
        coarse_pc, coarse_dpc = coarse.pop('pc'), coarse.pop('dpc')
        pc, dpc = fine.pop('pc'), fine.pop('dpc')
        if self.model.guard() != self.source_provenance or _sha(self.definition) != self.definition_sha256:
            raise ValueError('the actual source core or fixed continuous path changed')
        COUNTS['actual_path_inputs_generated'] += 1
        COUNTS['path_angular_samples'] += 3*angular_points
        return {'schema': 'actual-R618-to-R579-canonical-convex-core-input-v1',
            'continuous_function_definition': self.definition,
            'continuous_function_definition_sha256': self.definition_sha256,
            'mu_literal': mu_literal, 'mu_rational': [mu_rational.numerator, mu_rational.denominator],
            'maximum_independent_mode': maximum_mode, 'retained_modes': retained.tolist(),
            'P0_coefficients': pc.tolist(), 'P0_path_derivative_coefficients': dpc.tolist(),
            'literal_seed_coefficients_returned_at_mu_zero': bool(mu_rational == 0),
            'continuous_e_observation': float(e), 'continuous_e_path_derivative_observation': float(edot),
            'canonical_right_upper_support_observations': [float(A), float(B)],
            'R579_constant_observations': {'epsilon': self.epsilon, 'r': self.rounding, 'p': self.p, 'q': self.q},
            'same_seed_continuous_root_receipt': self.root_receipt,
            'seed_normal_ODE_quarter_material_angle_error_observation': self.seed_quarter_material_angle_error,
            'path_ODE_endpoint_observations': {
                'normal_angle_minus_pi_over_two': float(solution.y[0, -1]-np.pi/2),
                'integral_rho_difference_expected_zero': float(solution.y[1, -1]),
                'right_coordinate_expected_zero': float(solution.y[2, -1]),
                'upper_coordinate_minus_expected_B': float(solution.y[3, -1]-B)},
            'angular_points': angular_points, 'coarse_observations': coarse, 'fine_observations': fine,
            'maximum_retained_coefficient_N_to_2N_difference': float(np.max(abs(pc-coarse_pc))),
            'maximum_retained_derivative_coefficient_N_to_2N_difference': float(np.max(abs(dpc-coarse_dpc))),
            'numerical_settings': self.settings,
            'quadrature_error_estimates_not_enclosures': list(self.quadrature_errors),
            'complete_cost_counts': dict(COUNTS),
            'finite_P_requires_its_own_same_root_T_P_in_actual_height': True,
            'same_fixed_target_under_J_N_refinement': True,
            'J48_sufficient_not_assumed': True,
            'global_Fourier_tail_source_root_ODE_and_roundoff_errors_certified': False,
            'connection_whole_surface_or_README_criteria_met': False}

#!/usr/bin/env python3
"""R631 canonical core input path from the ACTUAL new R=.8 design seed.

The normal-angle ODE, implicit path derivative and Fourier observation
formulas are reused from the unchanged R=.85 path implementation.  This
constructor supplies its own actual seed, R=.8 and epsilon=.05 constants.
No old core, old accepted response or old metric identity is relabelled.
"""
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
PATH_FORMULAS_SHA = 'd08f57118d5de4ac5b23d15292e31315c26429b68e0711133d61a98d22780c45'
DESIGN_MODEL_SHA = '5fc7b6cb112e9ef659b0a61e3adb8a7981a8c0f50ec2d8d38e208edb49b9efcb'


def _load(name, filename, digest):
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('new-radius canonical path source differs: '+filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


path_formulas = _load('r631_unchanged_canonical_path_formulas',
    'r618_convex_core_input_path_20261128.py', PATH_FORMULAS_SHA)


class Radius080ConvexCoreInputPath(path_formulas.ConvexCoreInputPath):
    """New constructor, same parameterized normal-angle/path equations."""
    def __init__(self, actual_new_design_model, *, quadrature_epsabs,
            quadrature_epsrel, quadrature_limit, ode_atol, ode_rtol,
            ode_max_step, root_xtol, maximum_seed_positivity_nodes):
        model = actual_new_design_model
        module = sys.modules.get(type(model).__module__)
        source = HERE/'r631_radius080_hard_trace_design_20261128.py'
        if (module is None or Path(module.__file__).resolve() != source.resolve()
                or type(model) is not module.Radius080HardTraceDesign
                or hashlib.sha256(source.read_bytes()).hexdigest() != DESIGN_MODEL_SHA):
            raise ValueError('the actual reconstructed new-radius hard-P model is required')
        module.formulas.chain.public_only()
        self.model, self.source_provenance = model, model.guard()
        self.R = float(model.par.R)
        if self.R != .8:
            raise ValueError('R631 requires its actual new R=.8 reference')
        self.modes, self.seed_pc = model.modes.copy(), model.seed_pc.copy()
        self.seed_source_e = float(model.seed_target['e'])
        if (not all(np.isfinite(value) and value > 0 for value in
                (quadrature_epsabs, quadrature_epsrel, ode_atol, ode_rtol, ode_max_step, root_xtol))
                or type(quadrature_limit) is not int or quadrature_limit < 2
                or type(maximum_seed_positivity_nodes) is not int
                or maximum_seed_positivity_nodes < 4*int(self.modes[-1])):
            raise ValueError('complete positive finite numerical path inputs are required')
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
            raise ArithmeticError('actual R=.8 seed normal-angle inversion failed: '+self.seed_normal_solution.message)
        path_formulas.COUNTS['new_R080_seed_normal_angle_ODE_rhs'] += int(self.seed_normal_solution.nfev)
        self.seed_quarter_material_angle_error = abs(float(self.seed_normal_solution.y[0, -1])-np.pi/2)
        self.epsilon = .05
        L = 4*self._integral(lambda phi: np.sqrt(np.cos(phi)**2
            +self.epsilon**2*np.sin(phi)**2), 'R631_ellipse_support_quarter')
        c = L/(1+self.epsilon)
        self.rounding = (c*(1.+.37)-2*np.pi*self.R)/(2*c-2*np.pi)
        self.p = (1-self.rounding-self.epsilon*(.37-self.rounding))/(1-self.epsilon**2)
        self.q = (.37-self.rounding-self.epsilon*(1-self.rounding))/(1-self.epsilon**2)
        if not (.14 < self.rounding < .27 and self.p > self.q > 0):
            raise ArithmeticError('actual R631 constants left their proved strict bounds')
        self.seed_A = self._integral(lambda phi: self.rho0(phi)[0]*np.sin(phi), 'new_R080_seed_right_support')
        self.seed_B = self._integral(lambda phi: self.rho0(phi)[0]*np.cos(phi), 'new_R080_seed_upper_support')
        self.seed_coefficient_l1_exact = sum((abs(Fraction(str(float(value)))) for value in self.seed_pc), Fraction(0))
        self.definition = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'unchanged_normal_angle_path_formulas_sha256': PATH_FORMULAS_SHA,
            'actual_new_design_source_definition': model.definition,
            'seed_positive_even_modes': self.modes.tolist(), 'seed_P0_coefficients': self.seed_pc.tolist(),
            'seed_e_definition': 'mean_theta((e+2P_seed)^(-1/2))=1',
            'R_exact': '4/5', 'R631_epsilon_exact': '1/20',
            'R631_A_exact': '1', 'R631_B_exact': '37/100',
            'R631_r_p_q_definition': 'R631 exact support integral formulas',
            'path': 'rho_mu=(1-mu)*rho_actual_new_seed+mu*rho_R631; theta_phi=rho_mu/R',
            'normal_angle_convention': 'phi=0 at right support; psi=phi+pi/2; Y_theta=R*(-sin(phi),cos(phi))',
            'design_path_can_change_W_H_E_and_is_not_final_isometry_time': True,
            'old_R085_seed_or_fixed_E_identity_used': False,
            'no_grid_dependent_target_or_extra_rotation': True}
        self.definition_sha256 = path_formulas._sha(self.definition)
        path_formulas.COUNTS['actual_new_R080_continuous_core_input_paths'] += 1

    def input(self, mu_literal, *, maximum_mode, angular_points):
        result = super().input(mu_literal, maximum_mode=maximum_mode, angular_points=angular_points)
        result['schema'] = 'actual-new-R080-to-R631-canonical-convex-core-input-v1'
        result['R631_constant_observations'] = result.pop('R579_constant_observations')
        result['actual_new_radius_design_seed_not_old_accepted_R085_core'] = True
        small = self.seed_coefficient_l1_exact <= Fraction(1, 5)
        result['literal_seed_coefficient_l1_exact_rational'] = [
            self.seed_coefficient_l1_exact.numerator, self.seed_coefficient_l1_exact.denominator]
        result['seed_L1_at_most_one_fifth'] = small
        result['paper_target_bound_consumer'] = {
            'condition': 'seed_P0_coefficient_l1<=1/5', 'condition_met_on_literal_input': small,
            'argument': '1-2a<=e_seed<=1+2a; 1-4a<=u_seed^2<=1+4a; interpolate positive rho with R631',
            'if_condition_holds_target_rho_strict_bounds': ['7/50', '17153/1000'],
            'if_condition_holds_target_u_upper': '17153/800',
            'if_condition_holds_target_e_upper': '460',
            'if_condition_holds_target_abs_P_upper': '230',
            'bounds_are_for_exact_continuous_core_input_not_its_finite_J_projection': True,
            'whole_connection_ball_reach_or_metric_claimed': False}
        return result

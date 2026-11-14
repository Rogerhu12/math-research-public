#!/usr/bin/env python3
"""Generic radial metric seed with open flat ports and a genuine negative-K band.

The historic filename identifies its development branch; no C3 or cosine
assumption occurs in the metric.  The same interface supports a twofold
ellipse core.  Length is independent: two slope levels are solved from the
endpoint radius drop and a prescribed positive downward slope jump.
Only artificial derivative checks are exposed by this CLI.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np


def exact_number(value):
    if isinstance(value, Q):
        return value
    if isinstance(value, (float, np.floating)):
        return Q.from_float(float(value))
    return Q(value)


def s5(x, order=0):
    x = np.asarray(x, float)
    if order == -1:
        return x**4 * (2.5 - 3*x + x*x)
    if order == 0:
        return x**3 * (10 - 15*x + 6*x*x)
    if order == 1:
        return 30*x*x*(1-x)**2
    if order == 2:
        return 60*x*(1-x)*(1-2*x)
    if order == 3:
        return 60-360*x+360*x*x
    raise ValueError('S5 orders are integral -1 and derivatives 0 through 3')


def s11(x, order=0):
    """Normalized integral of 2772*x^5*(1-x)^5, with stable endpoint symmetry."""
    x = np.asarray(x, float)
    if order in [-1, 0]:
        y = np.minimum(x, 1-x)
        if order == -1:
            lower = y**7*(66+y*(-247.5+y*(385+y*(-308+y*(126-21*y)))))
            return np.where(x <= .5, lower, x-.5+lower)
        lower = y**6*(462+y*(-1980+y*(3465+y*(-3080+y*(1386-252*y)))))
        return np.where(x <= .5, lower, 1-lower)
    if order == 1:
        return 2772*x**5*(1-x)**5
    if order == 2:
        return 13860*x**4*(1-x)**4*(1-2*x)
    if order == 3:
        return 13860*x**3*(1-x)**3*(4*(1-2*x)**2-2*x*(1-x))
    raise ValueError('S11 orders are integral -1 and derivatives 0 through 3')


class NegativeKRadialSeed:
    """a(t) on [0,L], with a=a0 initially and a=rc+L-t on an open tail.

    Config has normalized core_fraction, flat_fraction, active_fractions
    (three positive fractions summing to one), negative_curvature_drop, and
    tail_smoothstep_order (11 by default; 5 is an explicitly different model).
    negative_curvature_drop equals mu-nu and forces integral
    K dA=-2*pi*(mu-nu) on the middle active segment. Positive mu>nu ensure
    a>=rc>0 everywhere.

    parameter_jacobian returns derivatives with respect to
    (a0, cut_radius, length, negative_curvature_drop); callers must specify
    whether the physical t or normalized u=t/L is held fixed.
    """
    parameter_names = ('a0', 'cut_radius', 'length', 'negative_curvature_drop')

    def __init__(self, a0, length, cut_radius, config=None, *, a0_source=None):
        cfg = {} if config is None else dict(config)
        self.length_exact = exact_number(length); self.cut_radius_exact = exact_number(cut_radius)
        self.a0 = float(exact_number(a0))
        self.length = float(self.length_exact); self.cut_radius = float(self.cut_radius_exact)
        self.gap_exact = exact_number(cfg.get('negative_curvature_drop', '3/10'))
        self.core_fraction_exact = exact_number(cfg.get('core_fraction', '1/25'))
        self.flat_fraction_exact = exact_number(cfg.get('flat_fraction', '3/50'))
        self.fractions_exact = tuple(exact_number(x) for x in
                                    cfg.get('active_fractions', ['1/4', '7/20', '2/5']))
        tail_order = exact_number(cfg.get('tail_smoothstep_order', 11))
        if tail_order not in (Q(5), Q(11)):
            raise ValueError('tail_smoothstep_order must be exactly 5 or 11')
        self.tail_smoothstep_order = int(tail_order)
        self.transition_orders = (5, 5, self.tail_smoothstep_order)
        if (len(self.fractions_exact) != 3 or sum(self.fractions_exact) != 1
                or min(self.fractions_exact) <= 0):
            raise ValueError('three positive exact active fractions must sum to one')
        if (self.core_fraction_exact <= 0 or self.flat_fraction_exact <= 0
                or self.core_fraction_exact+self.flat_fraction_exact >= 1):
            raise ValueError('strictly positive open core and flat buffers are required')
        if not (self.a0 > self.cut_radius > 0 and self.length > 0 and self.gap_exact > 0):
            raise ValueError('need a0>cut_radius>0, length>0, and positive negative-K drop')

        self.core_fraction = float(self.core_fraction_exact)
        self.flat_fraction = float(self.flat_fraction_exact)
        self.active_fraction = 1-self.core_fraction-self.flat_fraction
        self.fractions = np.array([float(x) for x in self.fractions_exact])
        self.widths = self.active_fraction*self.fractions
        self.edges = np.r_[self.core_fraction, self.core_fraction+np.cumsum(self.widths)]
        self.edges[-1] = 1-self.flat_fraction
        self.gap = float(self.gap_exact)
        f1, f2, f3 = self.fractions
        self.A = (f1+f2)/2; self.B = (f2+f3)/2; self.C = f3/2
        self.mean_active = ((self.a0-self.cut_radius)/self.length-self.flat_fraction)/self.active_fraction
        self.nu = (self.mean_active-self.A*self.gap-self.C)/(self.A+self.B)
        self.mu = self.nu+self.gap
        if not self.mu > self.nu > 0:
            raise ValueError('the chosen L/radius/gap do not give positive mu>nu; redesign these parameters')
        self.slope_at_most_one = bool(max(self.mu, self.nu) <= 1)
        self.a0_source = ({'kind': 'literal_exact_a0', 'exact_value': str(exact_number(a0)),
                           'not_an_unstated_arclength_integral': True}
                          if a0_source is None else dict(a0_source))

        denom = self.active_fraction*(self.A+self.B)
        self.nu_jac = np.array([1/(self.length*denom), -1/(self.length*denom),
                                -(self.a0-self.cut_radius)/(self.length**2*denom),
                                -self.A/(self.A+self.B)])
        self.mu_jac = self.nu_jac.copy(); self.mu_jac[-1] += 1
        self.coefficient_jac = np.vstack((np.zeros(4), self.mu_jac, self.nu_jac))

    @classmethod
    def from_core(cls, core, length, cut_radius, config=None):
        """Bind a0 to one frozen core's exact perimeter definition.

        A generic core needs a0 and identity_sha256, and preferably identity.
        The numerical a0 is an evaluation of that fixed definition; it is not
        frozen as a replacement binary64 metric constant.
        """
        if not hasattr(core, 'identity_sha256'):
            raise ValueError('a true core needs an explicit frozen physical identity')
        source = {'kind': 'frozen_core_perimeter',
                  'physical_identity_sha256': core.identity_sha256,
                  'physical_identity': getattr(core, 'identity', None),
                  'exact_definition': 'perimeter of the frozen core curve divided by 2*pi'}
        return cls(core.a0, length, cut_radius, config, a0_source=source)

    def _profile_basis(self, u):
        """Arrays for integral d, d, d_u, d_uu, d_uuu, linear in (1,mu,nu)."""
        u = np.asarray(u, float)
        if np.any(u < 0) or np.any(u > 1):
            raise ValueError('the frozen radial seed is evaluated only on its physical interval')
        F = np.zeros(u.shape+(3,)); d = np.zeros_like(F)
        du = np.zeros_like(F); duu = np.zeros_like(F); duuu = np.zeros_like(F)
        l1, l2, l3 = self.widths
        for segment, width in enumerate(self.widths):
            lo, hi = self.edges[segment:segment+2]
            mask = (u >= lo) & (u < hi)
            x = (u[mask]-lo)/width
            transition = s11 if self.transition_orders[segment] == 11 else s5
            S, H = transition(x), transition(x, -1)
            if segment == 0:
                before = np.zeros(3); start = np.zeros(3); change = np.array([0., 1., 0.])
            elif segment == 1:
                before = np.array([0., l1/2, 0.]); start = np.array([0., 1., 0.])
                change = np.array([0., -1., 1.])
            else:
                before = np.array([0., (l1+l2)/2, l2/2]); start = np.array([0., 0., 1.])
                change = np.array([1., 0., -1.])
            F[mask] = before+width*(x[..., None]*start+H[..., None]*change)
            d[mask] = start+S[..., None]*change
            du[mask] = transition(x, 1)[..., None]*change/width
            duu[mask] = transition(x, 2)[..., None]*change/width**2
            duuu[mask] = transition(x, 3)[..., None]*change/width**3
        mask = u >= self.edges[-1]
        F[mask] = np.array([l3/2, (l1+l2)/2, (l2+l3)/2])
        F[mask, 0] += u[mask]-self.edges[-1]
        d[mask, 0] = 1
        return F, d, du, duu, duuu

    def evaluate(self, points, *, coordinate='physical'):
        if coordinate not in ['physical', 'normalized']:
            raise ValueError('coordinate must be physical t or normalized u=t/L')
        points = np.asarray(points, float)
        u = points/self.length if coordinate == 'physical' else points
        F, db, dub, duub, _ = self._profile_basis(u)
        coefficients = np.array([1., self.mu, self.nu])
        d = db@coefficients; du = dub@coefficients; duu = duub@coefficients
        a = self.a0-self.length*(F@coefficients)
        # This is the same mathematical formula on the open tail, with no
        # cancellation between numerical endpoint-radius terms.
        tail = u >= self.edges[-1]
        a = np.where(tail, self.cut_radius+self.length*(1-u), a)
        if np.any(a <= 0):
            raise ArithmeticError('a positive radial metric was expected')
        return {'a': a, 'a_s': -d, 'a_ss': -du/self.length,
                'a_sss': -duu/self.length**2, 'K': du/(self.length*a),
                'normalized_coordinate': u, 'physical_coordinate': self.length*u}

    def jet(self, points, order=0, *, coordinate='physical'):
        if order not in range(4):
            raise ValueError('physical radial jets 0 through 3 are available')
        return self.evaluate(points, coordinate=coordinate)[['a', 'a_s', 'a_ss', 'a_sss'][order]]

    def parameter_jacobian(self, points, order=0, *, coordinate='physical'):
        """Analytic parameter derivatives of physical a,a_s,a_ss.

        The coordinate argument is essential: the length column changes when
        the same normalized collocation node, instead of the same t, is held.
        At moving breakpoints the returned orders remain differentiable; a
        parameter derivative of a_sss is intentionally not claimed there.
        """
        if order not in range(3) or coordinate not in ['physical', 'normalized']:
            raise ValueError('need order 0..2 and an explicit physical/normalized coordinate convention')
        points = np.asarray(points, float)
        u = points/self.length if coordinate == 'physical' else points
        F, db, dub, duub, _ = self._profile_basis(u)
        coefficients = np.array([1., self.mu, self.nu])
        d, du, duu = db@coefficients, dub@coefficients, duub@coefficients
        if order == 0:
            answer = -self.length*(F@self.coefficient_jac)
            answer[..., 0] += 1
            answer[..., 2] -= F@coefficients
            if coordinate == 'physical': answer[..., 2] += u*d
        elif order == 1:
            answer = -(db@self.coefficient_jac)
            if coordinate == 'physical': answer[..., 2] += u*du/self.length
        else:
            answer = -(dub@self.coefficient_jac)/self.length
            answer[..., 2] += du/self.length**2
            if coordinate == 'physical': answer[..., 2] += u*duu/self.length**2
        tail = u >= self.edges[-1]
        if order == 0:
            replacement = np.zeros(u.shape+(4,)); replacement[..., 1] = 1
            replacement[..., 2] = 1 if coordinate == 'physical' else 1-u
            answer = np.where(tail[..., None], replacement, answer)
        else:
            answer = np.where(tail[..., None], 0., answer)
        return answer

    def frozen_definition(self):
        definition = {'schema': 'negative-K-open-port-radial-metric-v2',
                      'a0_source': self.a0_source,
                      'length': str(self.length_exact), 'cut_radius': str(self.cut_radius_exact),
                      'negative_curvature_drop': str(self.gap_exact),
                      'core_fraction': str(self.core_fraction_exact),
                      'flat_fraction': str(self.flat_fraction_exact),
                      'active_fractions': [str(x) for x in self.fractions_exact],
                      'tail_smoothstep_order': self.tail_smoothstep_order,
                      'transition_orders': list(self.transition_orders),
                      'slope_definition': 'd=-a_s: 0 -> mu -> nu -> 1 by the listed normalized smoothsteps',
                      'S5_definition': '10*x^3-15*x^4+6*x^5',
                      'S11_definition': '462*x^6-1980*x^7+3465*x^8-3080*x^9+1386*x^10-252*x^11',
                      'each_transition_integral_on_unit_interval': '1/2',
                      'nu_definition': '(((a0-rc)/L-flat_fraction)/active_fraction-A*gap-C)/(A+B)',
                      'mu_definition': 'nu+gap; A=(f1+f2)/2,B=(f2+f3)/2,C=f3/2',
                      'whole_radius_positive_by_monotonicity': True,
                      'core_and_tail_are_open_exact_metric_regions': True,
                      'middle_integrated_Gaussian_curvature': '-2*pi*negative_curvature_drop',
                      'changing_any_parameter_is_metric_design_not_fixed_g_refinement': True,
                      'numerical_evaluation': {'a0': self.a0, 'mu': self.mu, 'nu': self.nu,
                                               'maximum_abs_a_prime': max(1., self.mu, self.nu),
                                               'active_mean_slope': self.mean_active},
                      'a_surface_realizing_this_metric_has_not_been_constructed': True}
        exact_part = {k: v for k, v in definition.items() if k != 'numerical_evaluation'}
        # Accept an older explicit source descriptor without making a finer
        # evaluation of the same exact perimeter change the frozen metric.
        exact_part['a0_source'] = {k: v for k, v in self.a0_source.items()
                                   if k != 'numerical_a0_for_evaluation'}
        definition['definition_sha256'] = hashlib.sha256(
            json.dumps(exact_part, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        return definition


def developer_check():
    config = {'negative_curvature_drop': '3/10'}
    seed = NegativeKRadialSeed(.7, .9, .22, config)
    u = np.array([.01, .11, .23, .39, .57, .73, .91, .98])
    pars = np.array([seed.a0, seed.cut_radius, seed.length, seed.gap])
    checks = {}
    for coordinate in ['physical', 'normalized']:
        points = u*seed.length if coordinate == 'physical' else u
        for order in range(3):
            analytic = seed.parameter_jacobian(points, order, coordinate=coordinate)
            columns = []
            for j in range(4):
                h = 1e-6
                plus, minus = pars.copy(), pars.copy(); plus[j] += h; minus[j] -= h
                ps = NegativeKRadialSeed(plus[0], plus[2], plus[1],
                                         {'negative_curvature_drop': float(plus[3])})
                ms = NegativeKRadialSeed(minus[0], minus[2], minus[1],
                                         {'negative_curvature_drop': float(minus[3])})
                columns.append((ps.jet(points, order, coordinate=coordinate)
                                -ms.jet(points, order, coordinate=coordinate))/(2*h))
            finite = np.stack(columns, axis=-1)
            checks[f'{coordinate}_order_{order}'] = float(np.max(abs(analytic-finite)) /
                                                          max(1., float(np.max(abs(finite)))))
    ends = seed.evaluate(np.array([0., seed.length]))
    endpoint_error = max(abs(ends['a'][0]-seed.a0), abs(ends['a'][1]-seed.cut_radius),
                         abs(ends['a_s'][0]), abs(ends['a_s'][1]+1),
                         np.max(abs(ends['a_ss'])), np.max(abs(ends['a_sss'])))
    joins = seed.evaluate(seed.edges, coordinate='normalized')
    join_jet_error = float(max(np.max(abs(joins['a_ss'])), np.max(abs(joins['a_sss']))))
    middle = (seed.edges[1]+seed.edges[2])/2
    negative_k = float(seed.evaluate(middle, coordinate='normalized')['K'])
    # Exact integral of K a dt equals endpoint difference of d, not quadrature.
    negative_integral_over_2pi = seed.nu-seed.mu
    same_source = {'kind': 'frozen_core_perimeter', 'physical_identity_sha256': 'artificial-fixed-core',
                   'exact_definition': 'one fixed artificial exact perimeter divided by 2*pi'}
    metric0 = NegativeKRadialSeed(.7, .9, .22, config, a0_source=same_source).frozen_definition()
    metric1 = NegativeKRadialSeed(np.nextafter(.7, 1.), .9, .22, config,
                                  a0_source=same_source).frozen_definition()
    metric2 = NegativeKRadialSeed(.7, np.nextafter(.9, 1.), .22, config,
                                  a0_source=same_source).frozen_definition()
    fixed_identity_stable = metric0['definition_sha256'] == metric1['definition_sha256']
    changed_length_detected = metric0['definition_sha256'] != metric2['definition_sha256']
    rational_string_roundtrip = NegativeKRadialSeed('7/10', '9/10', '11/50', config)
    rational_string_supported = (rational_string_roundtrip.length_exact == Q(9, 10)
                                 and rational_string_roundtrip.cut_radius_exact == Q(11, 50))
    legacy = NegativeKRadialSeed(.7, .9, .22, {**config, 'tail_smoothstep_order': 5})
    tail_order_identity_detected = (legacy.frozen_definition()['definition_sha256']
                                   != seed.frozen_definition()['definition_sha256'])
    unchanged_levels = bool(seed.mu == legacy.mu and seed.nu == legacy.nu)
    # Exact polynomial checks are developer checks, not geometry sampling.
    polynomial = [Q(0)]*6+[Q(x) for x in [462, -1980, 3465, -3080, 1386, -252]]
    integral = sum(value/Q(i+1) for i, value in enumerate(polynomial))
    left_jets, right_jets = [], []
    derivative = polynomial
    for order in range(6):
        left_jets.append(derivative[0]); right_jets.append(sum(derivative))
        derivative = [Q(i)*value for i, value in enumerate(derivative)][1:]
    exact_tail_checks = (integral == Q(1, 2) and left_jets == [Q(0)]*6
                         and right_jets == [Q(1)]+[Q(0)]*5
                         and polynomial[6] == 462)
    artificial_x = np.array([0., .07, .31, .5, .73, .94, 1.])
    primitive_symmetry_error = float(np.max(abs(s11(artificial_x, -1)
                                                -artificial_x+.5-s11(1-artificial_x, -1))))
    passed = (max(checks.values()) < 2e-6 and endpoint_error < 1e-12
              and join_jet_error < 1e-10 and negative_k < 0
              and abs(negative_integral_over_2pi+seed.gap) < 1e-14
              and fixed_identity_stable and changed_length_detected and rational_string_supported
              and tail_order_identity_detected and unchanged_levels and exact_tail_checks
              and primitive_symmetry_error < 1e-14)
    return {'schema': 'generic-radial-seed-development-check-v2', 'passed': bool(passed),
            'artificial_parameters_only': True, 'no_research_candidate_evaluated': True,
            'parameter_jacobian_relative_errors': checks, 'endpoint_error': float(endpoint_error),
            'join_radial_2_3_jet_error': join_jet_error, 'middle_K': negative_k,
            'middle_integral_K_dA_over_2pi': negative_integral_over_2pi,
            'same_exact_a0_finer_evaluation_preserves_identity': fixed_identity_stable,
            'different_physical_length_changes_identity': changed_length_detected,
            'exact_rational_string_parameters_supported': rational_string_supported,
            'tail_order_change_changes_metric_identity': tail_order_identity_detected,
            'S11_preserves_mu_nu_of_same_design': unchanged_levels,
            'S11_exact_integral': str(integral),
            'S11_exact_endpoint_jets_0_through_5': {
                'left': [str(x) for x in left_jets], 'right': [str(x) for x in right_jets]},
            'S11_exact_left_leading_power': 6, 'S11_exact_left_leading_coefficient': '462',
            'S11_primitive_symmetry_error': primitive_symmetry_error,
            'definition': seed.frozen_definition()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(); report = developer_check()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'passed': report['passed'], 'out': str(args.out)}), flush=True)
    if not report['passed']: raise SystemExit(1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Three fixed-metric engines with a physical elliptic core and inward ports.

The circle reference determines a(s), not the actual cap height.  The latter
is a separate fixed BVP datum, screened by R4 before the run.  Optimization is
restricted to this public repository's Actions; local --smoke-only is for
small interface/derivative checks.  No finite residual is an isometry claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import least_squares
from scipy.special import ellipe

from core_to_tail_bvp import InwardMeridian
from eccentric_collar_search import TrialSpace, smoothstep
from folded_collar_search import (PinnedCartesianSpace, PinnedUnitSpace,
                                 ReferenceMetricProblem, SplitRadialSpace,
                                 core_curve)
from unit_tangent_collar_search import SignedFrenetSpace


class InwardPortProfile:
    """Fixed radius metric and a C2 trial center with independently fixed caps.

    The full s interval has a central cylinder of length 2*h0 and two
    connections of length Lc.  Lower and upper cap planes are -Cz and +Cz.
    The reference beta and a remain fixed when the trial z center is raised.
    Consequently a'^2+z_trial'^2 need not be one away from the pinned pieces.
    """
    def __init__(self, args):
        self.connection_length = L = float(args.connection_length)
        self.core_half_height = h = float(args.core_half_height)
        self.port_height = float(args.port_height)
        self.radius = float(args.cut_radius)
        self.a0 = float(2*args.ellipse_major*ellipe(
            1-(args.ellipse_minor/args.ellipse_major)**2)/np.pi)
        self.half = InwardMeridian(
            self.a0, 0., 0., L, self.radius, (0., 0., h), args.quadrature,
            overshoot=args.inward_overshoot,
            first_fraction=args.inward_first_fraction)
        self.active = float(self.half.u2*L)
        self.flat_length = L-self.active
        self.length = 2*(L+h)
        self.core_left, self.core_right = L, L+2*h
        self.start, self.end = self.flat_length, self.length-self.flat_length
        self.transition_width = self.active
        self.plateau = h/self.length
        self.collar = self.flat_length/self.length
        self.height = 2*self.port_height
        self.nodes, self.weights = self.half.gl, self.half.gw
        self.reference_port_height = float(self.half.evaluate(np.array([1.]))[1][0][0])
        self.height_shift = self.port_height-self.reference_port_height
        self.parameters = {
            key: getattr(args, key) for key in
            ['ellipse_major', 'ellipse_minor', 'connection_length',
             'core_half_height', 'cut_radius', 'port_height',
             'inward_overshoot', 'inward_first_fraction', 'quadrature']}

    def _coordinate(self, s):
        s = np.asarray(s, float)
        if np.any(s < -1e-13) or np.any(s > self.length+1e-13):
            raise ValueError('radial coordinate outside the prescribed band')
        mid = self.length/2
        t = np.clip(np.abs(s-mid)-self.core_half_height, 0., self.connection_length)
        return s, t, s < self.core_left, s > self.core_right

    def evaluate(self, s):
        s, t, left, right = self._coordinate(s)
        shape = s.shape
        a, z = self.half.evaluate(t.reshape(-1)/self.connection_length)
        a = [v.reshape(shape) for v in a]
        z = [v.reshape(shape) for v in z]
        b, bp, bpp = smoothstep(t/self.active)
        z[0] = z[0]+self.height_shift*b
        z[1] = z[1]+self.height_shift*bp/self.active
        z[2] = z[2]+self.height_shift*bpp/self.active**2
        active = left | right
        aa = np.where(active, a[0], self.a0)
        zz = np.where(left, -z[0], np.where(right, z[0], s-self.length/2))
        ap = np.where(left, -a[1], np.where(right, a[1], 0.))
        zp = np.where(active, z[1], 1.)
        app = np.where(active, a[2], 0.)
        zpp = np.where(left, -z[2], np.where(right, z[2], 0.))
        return aa, zz, ap, zp, app, zpp

    def beta(self, s):
        s, t, left, right = self._coordinate(s)
        u = t/self.connection_length
        b = self.half.beta(u)
        bp = self.half.beta(u, 1)/self.connection_length
        bpp = self.half.beta(u, 2)/self.connection_length**2
        return (np.where(left, np.pi-b, np.where(right, b, np.pi/2)),
                np.where(left | right, bp, 0.),
                np.where(left, -bpp, np.where(right, bpp, 0.)))

    def identity(self):
        return {
            'profile_family': 'fixed_inward_radius_independent_trial_cap_height',
            'parameters': self.parameters,
            'target_metric': 'ds^2+a_inward(s)^2 du^2, fixed throughout the run',
            'core_mean_radius': self.a0,
            'full_s_length': self.length,
            'core_s_interval': [self.core_left, self.core_right],
            'half_active_length': self.active,
            'half_open_flat_collar_length': self.flat_length,
            'reference_circle_upper_port_height': self.reference_port_height,
            'actual_upper_port_height': self.port_height,
            'trial_center_height_shift': self.height_shift,
            'height_bridge': 'S5(t/half_active_length), constant on the whole flat collar',
            'trial_base_is_not_assumed_isometric': True,
            'reference_geometry_is_not_a_nonaxisymmetric_certificate': True}


class InwardCartesianSpace(PinnedCartesianSpace):
    def __init__(self, args):
        self.args = args
        TrialSpace.__init__(self, InwardPortProfile(args), args.controls,
                            args.modes, 0., 0., 'fixed')
        self.split = SplitRadialSpace(self.metric, self.shape[0])


class InwardUnitSpace(PinnedUnitSpace):
    def __init__(self, args):
        self.args = args
        self.meridian = InwardPortProfile(args)
        self.radial = TrialSpace(self.meridian, args.controls, args.modes, 0., 0.)
        self.j, self.k = args.controls-6, 2*args.modes+1
        self.nangle = self.j*self.k
        self.size = 2*self.nangle+3*self.j
        self.split = SplitRadialSpace(self.meridian, self.j)


class InwardSignedSpace(SignedFrenetSpace, InwardUnitSpace):
    pass


def r4_screen(args):
    """Necessary conditions only; no reference-geometry substitution."""
    A, B, rc, L = (args.ellipse_major, args.ellipse_minor, args.cut_radius,
                   args.connection_length)
    tau = max(args.reach_budget, .06*A)  # D >= 2A and reach/D >= .03.
    x = L/tau
    horizontal_upper = tau*(1-np.cos(x)) if x <= np.pi/2 else L-(np.pi/2-1)*tau
    dx = max(A-rc, 0.)
    # For the coaxial full planar cap, Cy=0, rf=rc.  A single inward core
    # normal-ball center projects into it if rc >= B-tau.
    height_applies = 0 < tau < B and rc >= B-tau
    height_min = args.core_half_height+tau if height_applies else None
    length_ok = dx <= horizontal_upper+1e-13
    height_ok = height_min is None or args.port_height >= height_min-1e-13
    return {
        'absolute_reach_budget_used': tau,
        'task_necessary_absolute_reach_from_core_diameter': .06*A,
        'additional_reach_budget_is_a_design_condition': args.reach_budget > .06*A,
        'horizontal_displacement_required': dx,
        'horizontal_displacement_upper': float(horizontal_upper),
        'length_necessary_condition_passes': bool(length_ok),
        'flat_disk_normal_ball_height_condition_applies': bool(height_applies),
        'actual_flat_disk_radius': rc,
        'actual_cap_center_xy': [0., 0.],
        'upper_cap_height_minimum': height_min,
        'actual_upper_cap_height': args.port_height,
        'height_necessary_condition_passes': bool(height_ok),
        'sufficient_for_solution_or_reach': False}


def pinned_jet_audit(space, q, args, angular=64):
    """Cheap checks on open pinned pieces, including actual reconstructed X."""
    m = space.metric if args.engine == 'cartesian' else space.meridian
    s = np.array([0., m.start/2, m.core_left,
                  m.length/2, m.core_right, (m.end+m.length)/2, m.length])
    u = np.arange(angular)*2*np.pi/angular
    er = np.stack((np.cos(u), np.sin(u), np.zeros_like(u)), axis=-1)
    et = np.stack((-np.sin(u), np.cos(u), np.zeros_like(u)), axis=-1)
    curve = core_curve(u, args)
    gamma, gu, guu = [m.a0*curve[k] for k in ['gamma', 'du', 'duu']]
    a, z, ap, zp, app, zpp = m.evaluate(s)
    expected = [a[:,None,None]*er, ap[:,None,None]*er,
                a[:,None,None]*et, app[:,None,None]*er,
                ap[:,None,None]*et, -a[:,None,None]*er]
    expected[0][:,:,2] = z[:,None]
    expected[1][:,:,2] = zp[:,None]
    expected[3][:,:,2] = zpp[:,None]
    for i in [2, 3, 4]:
        expected[0][i] = gamma+np.array([0., 0., z[i]])
        expected[1][i] = np.array([0., 0., 1.])
        expected[2][i] = gu
        expected[3][i] = 0.
        expected[4][i] = 0.
        expected[5][i] = guu
    grid = space.prepare(s, u if args.engine == 'cartesian' else angular)
    actual = space.geometry(q, grid, True)
    if isinstance(actual, dict):
        actual = [actual[k] for k in ['x', 'xs', 'xu', 'xss', 'xsu', 'xuu']]
    errors = [float(np.max(np.abs(x-y))) for x,y in zip(actual, expected)]
    return {'radial_points': s.tolist(), 'angular_points': angular,
            'jet_component_order': ['X', 'Xs', 'Xu', 'Xss', 'Xsu', 'Xuu'],
            'maximum_error_each_jet': errors,
            'core_position_has_analytic_formula': args.engine == 'cartesian',
            'unit_and_signed_use_discrete_FFT_primitive': args.engine != 'cartesian',
            'continuous_certificate': False}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--engine', choices=['cartesian', 'unit', 'signed'], default='cartesian')
    p.add_argument('--ellipse-major', type=float, default=1.)
    p.add_argument('--ellipse-minor', type=float, default=.3)
    p.add_argument('--core-half-height', type=float, default=.23)
    p.add_argument('--connection-length', type=float, default=.8)
    p.add_argument('--cut-radius', type=float, default=.28)
    p.add_argument('--port-height', type=float, default=.30)
    p.add_argument('--inward-overshoot', type=float, default=1.53)
    p.add_argument('--inward-first-fraction', type=float, default=.67)
    p.add_argument('--reach-budget', type=float, default=.069)
    p.add_argument('--quadrature', type=int, default=96)
    p.add_argument('--controls', type=int, default=14)
    p.add_argument('--modes', type=int, default=6)
    p.add_argument('--radial-order', type=int, default=8)
    p.add_argument('--angles', type=int, default=128)
    p.add_argument('--curvature-limit', type=float, default=13.)
    p.add_argument('--curvature-weight', type=float, default=0.)
    p.add_argument('--closure-weight', type=float, default=2.)
    p.add_argument('--max-nfev', type=int, default=200)
    p.add_argument('--resume', type=Path)
    p.add_argument('--check-jacobian', action='store_true')
    p.add_argument('--smoke-only', action='store_true')
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if not (args.ellipse_major >= args.ellipse_minor > 0 and
            args.core_half_height > 0 and args.cut_radius > 0 and
            args.connection_length > 0 and args.reach_budget >= 0):
        p.error('positive physical axes, core height, cut radius and length are required')
    if args.controls < 10 or args.angles < 4*args.modes+4:
        p.error('need controls >= 10 and angles >= 4*modes+4')
    if args.engine != 'cartesian' and args.curvature_weight:
        p.error('true-curvature penalty is currently implemented for Cartesian only')
    if not args.smoke_only and (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        p.error('optimization belongs in the public repository Actions; use --smoke-only locally')
    screen = r4_screen(args)
    if not screen['length_necessary_condition_passes'] or not screen['height_necessary_condition_passes']:
        p.error('R4 necessary condition fails: '+json.dumps(screen))
    args.core_shape = 'ellipse'
    args.seed2 = args.seed3 = args.seed_asymmetry = args.offset = 0.
    args.fixed_radius = args.pin_core = True
    args.radius_floor, args.radius_ceiling, args.radius_weight = .7, 1.3, 10.
    started = time.monotonic()
    if args.engine == 'cartesian':
        space = InwardCartesianSpace(args)
        problem = ReferenceMetricProblem(space, args.curvature_limit, args.curvature_weight)
        m = space.metric
        grid = problem.prepare(space.collocation(args.radial_order),
                               np.arange(args.angles)*2*np.pi/args.angles)
        residual = lambda q: problem.residual(q, grid)
        jacobian = lambda q: problem.jacobian(q, grid)
        audit = lambda q,n: problem.audit(q, n, max(128, 2*args.angles))
    else:
        space = (InwardSignedSpace if args.engine == 'signed' else InwardUnitSpace)(args)
        m = space.meridian
        grid = space.prepare(space.split.collocation(args.radial_order), args.angles)
        residual = lambda q: space.residual(q, grid)
        jacobian = lambda q: space.jacobian(q, grid)
        audit = lambda q,n: space.audit(q, n, max(128, 2*args.angles))
    q0 = np.zeros(space.size)
    if args.resume:
        old = json.loads(args.resume.read_text())
        if old['definition']['engine'] != args.engine or len(old['coefficients']) != space.size:
            raise ValueError('resume changes representation; project explicitly')
        for key, value in m.parameters.items():
            if old['definition'][key] != value:
                raise ValueError('resume changes a fixed metric or boundary datum: '+key)
        if old['definition']['controls'] != args.controls or old['definition']['modes'] != args.modes:
            raise ValueError('resume changes basis; project explicitly')
        q0 = np.asarray(old['coefficients'], float)
    derivative = None
    if args.check_jacobian:
        direction = np.random.default_rng(20261114).normal(size=space.size)
        direction /= np.linalg.norm(direction)
        eps = 2e-7
        numeric = (residual(q0+eps*direction)-residual(q0-eps*direction))/(2*eps)
        analytic = jacobian(q0)@direction
        derivative = float(np.linalg.norm(numeric-analytic)/max(np.linalg.norm(numeric), 1e-30))
        print(json.dumps({'jacobian_relative_error': derivative}), flush=True)
    initial = audit(q0, 33 if args.smoke_only else 257)
    count = [0]
    def fun(q):
        value = residual(q)
        count[0] += 1
        if count[0]%10 == 1:
            print(json.dumps({'evaluation': count[0], 'rms': float(np.sqrt(np.mean(value*value))),
                              'maximum': float(np.max(abs(value))),
                              'seconds': time.monotonic()-started}), flush=True)
        return value
    if args.smoke_only:
        rr = residual(q0)
        result = argparse.Namespace(x=q0, success=False,
            message='development smoke only; no optimization', nfev=0,
            cost=float(rr@rr)/2, optimality=None)
    else:
        result = least_squares(fun, q0, jac=jacobian, method='lm', x_scale='jac',
            max_nfev=args.max_nfev, ftol=1e-11, gtol=1e-11, xtol=1e-11)
    audits = [audit(result.x,n) for n in ([33] if args.smoke_only else [257, 1025])]
    source_names = ['inward_collar_search.py', 'folded_collar_search.py',
        'core_to_tail_bvp.py', 'eccentric_collar_search.py',
        'eccentric_curvature_search.py', 'unit_tangent_collar_search.py']
    report = {
        'schema': 'inward-pinned-collar-v1',
        'status': 'development_smoke_only' if args.smoke_only else 'finite_fixed_metric_search',
        'definition': {k: str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
        'fixed_profile_and_actual_boundary': m.identity(),
        'r4_necessary_screen_for_exact_target_problem': screen,
        'prescribed_physical_core_semiaxes': [args.ellipse_major, args.ellipse_minor],
        'target_metric_is_fixed': True, 'circle_reference_height_is_not_used_as_actual_height': True,
        'open_core_dofs_and_open_flat_circular_collars_pinned': True,
        'core_tangent_field_is_analytically_pinned': True,
        'position_core_analytic_only_in_cartesian_engine': True,
        'initial_audit': initial, 'final_audits': audits,
        'pinned_piece_jet_audit': pinned_jet_audit(space, result.x, args, max(128,2*args.angles)),
        'jacobian_relative_error': derivative,
        'solver': {'success': bool(result.success), 'message': result.message,
                   'nfev': int(result.nfev), 'cost': float(result.cost),
                   'optimality': None if result.optimality is None else float(result.optimality)},
        'coefficients': result.x.tolist(), 'elapsed_seconds': time.monotonic()-started,
        'source_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                          for name in source_names},
        'claim': {'exact_isometry': False, 'fixed_metric_refinement_demonstrated': False,
                  'closed_embedded_family': False, 'held_displacement_certified': False,
                  'reach_certified': False, 'task_complete': False}}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'out': str(args.out), 'engine': args.engine, 'final_audit': audits[-1]}), flush=True)


if __name__ == '__main__':
    main()

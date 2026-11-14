#!/usr/bin/env python3
"""Cartesian inward BVP with an analytic Gauss--Codazzi fourth-jet seed.

This independent entry point preserves the frozen inward baseline.  Both
seed choices solve the same fixed metric and boundary problem.  Optional
ellipse-angle trial functions are differentiated in the original material u;
they do not change the metric or add unknowns.  Optimization runs in the
public repository Actions only; --smoke-only is a development check.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import polynomial as poly
from scipy.optimize import least_squares

from eccentric_collar_search import TrialSpace, fourier, smoothstep
from folded_collar_search import ReferenceMetricProblem, SplitRadialSpace, core_curve
from inward_collar_search import (InwardCartesianSpace, InwardPortProfile,
                                 pinned_jet_audit, r4_screen)


S9 = np.array([0.,0.,0.,0.,0.,126.,-420.,540.,-315.,70.])


def step9(x):
    x = np.asarray(x)
    y = np.clip(x, 0., 1.)
    output = [poly.polyval(y, poly.polyder(S9, d)) for d in range(3)]
    output[0] = np.where(x <= 0., 0., np.where(x >= 1., 1., output[0]))
    for d in [1, 2]:
        output[d] = np.where((x > 0.) & (x < 1.), output[d], 0.)
    return output


def ellipse_geometry(u, args, curve=None):
    """Exact material derivatives of phase and h=gamma+N/kappa_normalized."""
    curve = core_curve(u, args) if curve is None else curve
    A, B = args.ellipse_major, args.ellipse_minor
    from scipy.special import ellipe
    a0 = 2*A*ellipe(1-(B/A)**2)/np.pi
    co = a0*curve['gamma'][:,0]/A
    si = a0*curve['gamma'][:,1]/B
    phase = np.mod(np.arctan2(si, co), 2*np.pi)
    speed = np.sqrt(A*A*si*si+B*B*co*co)
    delta = A*A-B*B
    phase_u = a0/speed
    phase_uu = -a0*a0*delta*si*co/speed**4
    zero = np.zeros_like(u)
    h = np.stack((delta*co**3/(A*a0), -delta*si**3/(B*a0), zero), axis=-1)
    hp = np.stack((-3*delta*co*co*si/(A*a0),
                   -3*delta*si*si*co/(B*a0), zero), axis=-1)
    hpp = np.stack((delta*(6*co*si*si-3*co**3)/(A*a0),
                    delta*(-6*si*co*co+3*si**3)/(B*a0), zero), axis=-1)
    hu = hp*phase_u[:,None]
    huu = hpp*phase_u[:,None]**2+hp*phase_uu[:,None]
    return phase, phase_u, phase_uu, (h, hu, huu)


class GC4Profile(InwardPortProfile):
    def evaluate(self, s):
        value = list(super().evaluate(s))
        s, t, left, right = self._coordinate(s)
        old, new = smoothstep(t/self.active), step9(t/self.active)
        sign = np.where(left, -1., np.where(right, 1., 0.))
        active = left | right
        value[1] += sign*self.height_shift*(new[0]-old[0])
        value[3] += active*self.height_shift*(new[1]-old[1])/self.active
        value[5] += sign*self.height_shift*(new[2]-old[2])/self.active**2
        return value

    @property
    def cubic_beta(self):
        first_length = self.half.u1*self.connection_length
        return 10*(self.half.minimum-np.pi/2)/first_length**3

    def identity(self):
        out = super().identity()
        out.update(height_bridge='S9(t/half_active_length), zero derivatives through order 4 at each join',
                   seed_family='analytic_GC_fourth_jet',
                   beta_minus_pi_over_two_cubic_coefficient=self.cubic_beta,
                   target_metric_unchanged_from_inward_baseline=True)
        return out


def apply_angular_basis(grid, args, curve=None):
    if args.angular_basis == 'material':
        return
    phi, pu, puu, _ = ellipse_geometry(grid['u'], args, curve)
    f, fp, fpp = fourier(phi, args.modes)
    grid['angular'] = [f, fp*pu[:,None], fpp*pu[:,None]**2+fp*puu[:,None]]


class EllipseAngleSpace(InwardCartesianSpace):
    def prepare(self, s, u):
        grid = super().prepare(s, u)
        apply_angular_basis(grid, self.args)
        return grid


class GC4Space(EllipseAngleSpace):
    def __init__(self, args):
        self.args = args
        TrialSpace.__init__(self, GC4Profile(args), args.controls, args.modes, 0., 0., 'fixed')
        self.split = SplitRadialSpace(self.metric, self.shape[0])
        self.jet_window = args.gc_jet_fraction*self.metric.half.u1*self.metric.connection_length

    def prepare(self, s, u):
        # Build from the unblended circular trial, not the legacy S5 core blend.
        grid = TrialSpace.prepare(self, s, u)
        s, t, left, right = self.metric._coordinate(s)
        a, _, ap, _, app, _ = self.metric.evaluate(s)
        direction = np.where(left, -1., np.where(right, 1., 0.))
        step, step_p, step_pp = step9(t/self.metric.active)
        B = 1-step
        Bs = -step_p*direction/self.metric.active
        Bss = -step_pp*(left | right)/self.metric.active**2
        curve = core_curve(np.asarray(u), self.args)
        er = np.stack((np.cos(u), np.sin(u), np.zeros_like(u)), axis=-1)
        et = np.stack((-np.sin(u), np.cos(u), np.zeros_like(u)), axis=-1)
        diff = [curve['gamma']-er, curve['du']-et, curve['duu']+er]
        f0, f1, f2 = a*B, ap*B+a*Bs, app*B+2*ap*Bs+a*Bss
        orders = [(f0,0), (f1,0), (f0,1), (f2,0), (f1,1), (f0,2)]
        for i, (factor, d) in enumerate(orders):
            grid['base'][i] += factor[:,None,None]*diff[d][None,:,:]
        # a(t)=a0-c*t^4/4+O(t^5).  The base a*gamma_normalized has
        # coefficient -c*gamma_normalized/4; the exact GC coefficient is
        # c*N/(4*kappa_normalized).  Their difference is c*h/4.
        _, _, _, h = ellipse_geometry(np.asarray(u), self.args, curve)
        # The fourth jet is local information; do not extrapolate its t^4
        # polynomial over the entire connection.  This compact window affects
        # the trial seed only and leaves the target metric and boundary fixed.
        cut, cutp, cutpp = step9(t/self.jet_window)
        J = 1-cut
        Js = -cutp*direction/self.jet_window
        Jss = -cutpp*(left | right)/self.jet_window**2
        w = t**4*J
        ws = 4*t**3*direction*J+t**4*Js
        wss = 12*t*t*(left | right)*J+8*t**3*direction*Js+t**4*Jss
        orders = [(w,0), (ws,0), (w,1), (wss,0), (ws,1), (w,2)]
        for i, (factor, d) in enumerate(orders):
            grid['base'][i] += (self.metric.cubic_beta/4)*factor[:,None,None]*h[d][None,:,:]
        apply_angular_basis(grid, self.args, curve)
        return grid


def local_jet_check(space, args):
    """Check the analytic coefficient and one-sided scaling, without solving."""
    m = space.metric
    u = np.arange(32)*2*np.pi/32
    curve = core_curve(u, args)
    _, _, _, h = ellipse_geometry(u, args, curve)
    c = m.cubic_beta if isinstance(m, GC4Profile) else (
        10*(m.half.minimum-np.pi/2)/(m.half.u1*m.connection_length)**3)
    normal = curve['duu']/curve['curvature'][:,None]
    required = c*normal/(4*curve['curvature'][:,None])
    inserted = -c*curve['gamma']/4+c*h[0]/4
    coefficient_error = float(np.max(np.abs(required-inserted)))
    rows = []
    for t in [.002, .001, .0005]:
        s = np.array([m.core_right+t])
        x = space.geometry(np.zeros(space.size), space.prepare(s,u))[0][0]
        core = m.a0*curve['gamma']+np.array([0.,0.,args.core_half_height+t])
        rows.append({'t': t,
            'horizontal_fourth_coefficient_error': float(np.max(np.abs((x-core)[:,:2]/t**4-required[:,:2]))),
            'maximum_vertical_displacement_over_t4': float(np.max(np.abs((x-core)[:,2]/t**4)))})
    return {'gc_fourth_coefficient_applied': args.seed_family == 'gc4',
            'analytic_fourth_coefficient_identity_error': coefficient_error,
            'one_sided_scaling_samples': rows,
            'samples_are_not_a_validated_remainder_bound': True}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--seed-family', choices=['legacy','gc4'], default='gc4')
    p.add_argument('--angular-basis', choices=['material','ellipse'], default='material')
    p.add_argument('--gc-jet-fraction', type=float, default=.25)
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
    p.add_argument('--max-nfev', type=int, default=200)
    p.add_argument('--resume', type=Path)
    p.add_argument('--check-jacobian', action='store_true')
    p.add_argument('--smoke-only', action='store_true')
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if not (args.ellipse_major >= args.ellipse_minor > 0 and args.core_half_height > 0 and
            args.cut_radius > 0 and args.connection_length > 0 and args.reach_budget >= 0):
        p.error('invalid physical geometry')
    if not 0 < args.gc_jet_fraction <= 1:
        p.error('need 0 < gc-jet-fraction <= 1')
    if args.controls < 10 or args.angles < 4*args.modes+4:
        p.error('need controls >= 10 and angles >= 4*modes+4')
    if not args.smoke_only and (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        p.error('optimization belongs in the public repository Actions; use --smoke-only locally')
    screen = r4_screen(args)
    if not screen['length_necessary_condition_passes'] or not screen['height_necessary_condition_passes']:
        p.error('R4 necessary condition fails: '+json.dumps(screen))
    args.engine, args.core_shape = 'cartesian', 'ellipse'
    args.seed2 = args.seed3 = args.offset = 0.
    started = time.monotonic()
    space = (GC4Space if args.seed_family == 'gc4' else EllipseAngleSpace)(args)
    m = space.metric
    problem = ReferenceMetricProblem(space, args.curvature_limit, args.curvature_weight)
    grid = problem.prepare(space.collocation(args.radial_order), np.arange(args.angles)*2*np.pi/args.angles)
    fun = lambda q: problem.residual(q, grid)
    jac = lambda q: problem.jacobian(q, grid)
    q0 = np.zeros(space.size)
    if args.resume:
        old = json.loads(args.resume.read_text())
        keys = [*m.parameters, 'controls', 'modes', 'seed_family', 'angular_basis','gc_jet_fraction']
        if any(old['definition'][k] != getattr(args,k) for k in keys) or len(old['coefficients']) != space.size:
            raise ValueError('resume changes fixed data, seed or basis; project explicitly')
        q0 = np.asarray(old['coefficients'],float)
    derivative = None
    if args.check_jacobian:
        v = np.random.default_rng(20261114).normal(size=space.size)
        v /= np.linalg.norm(v)
        eps = 2e-7
        numeric = (fun(q0+eps*v)-fun(q0-eps*v))/(2*eps)
        derivative = float(np.linalg.norm(numeric-jac(q0)@v)/max(np.linalg.norm(numeric),1e-30))
        print(json.dumps({'jacobian_relative_error': derivative}), flush=True)
    audit = lambda q,n: problem.audit(q,n,max(128,2*args.angles))
    initial = audit(q0,33 if args.smoke_only else 257)
    evaluations = [0]
    def progress(q):
        r = fun(q)
        evaluations[0] += 1
        if evaluations[0]%10 == 1:
            print(json.dumps({'evaluation':evaluations[0],'rms':float(np.sqrt(np.mean(r*r))),
                              'maximum':float(np.max(abs(r))),'seconds':time.monotonic()-started}),flush=True)
        return r
    if args.smoke_only:
        r = fun(q0)
        result = argparse.Namespace(x=q0,success=False,message='development smoke only; no optimization',
                                    nfev=0,cost=float(r@r)/2,optimality=None)
    else:
        result = least_squares(progress,q0,jac=jac,method='lm',x_scale='jac',
                               max_nfev=args.max_nfev,ftol=1e-11,gtol=1e-11,xtol=1e-11)
    audits = [audit(result.x,n) for n in ([33] if args.smoke_only else [257,1025])]
    sources = ['inward_gc4_collar_search.py','inward_collar_search.py','folded_collar_search.py',
               'core_to_tail_bvp.py','eccentric_collar_search.py','eccentric_curvature_search.py']
    report = {
        'schema':'inward-gc4-cartesian-v1',
        'status':'development_smoke_only' if args.smoke_only else 'finite_fixed_metric_search',
        'definition':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
        'fixed_profile_and_actual_boundary':m.identity(),
        'r4_necessary_screen_for_exact_target_problem':screen,
        'target_metric_is_fixed':True,
        'ellipse_angle_basis_changes_trial_functions_not_material_coordinate':True,
        'radial_unknown_count_unchanged':args.controls-6,
        'coefficient_shape':list(space.shape),
        'gc_jet_window_physical_length':getattr(space,'jet_window',None),
        'local_gc_fourth_jet_check':local_jet_check(space,args),
        'pinned_piece_jet_audit':pinned_jet_audit(space,result.x,args,max(128,2*args.angles)),
        'jacobian_relative_error':derivative,'initial_audit':initial,'final_audits':audits,
        'solver':{'success':bool(result.success),'message':result.message,'nfev':int(result.nfev),
                  'cost':float(result.cost),'optimality':None if result.optimality is None else float(result.optimality)},
        'coefficients':result.x.tolist(),'elapsed_seconds':time.monotonic()-started,
        'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in sources},
        'claim':{'exact_isometry':False,'fixed_metric_refinement_demonstrated':False,
                  'closed_embedded_family':False,'reach_certified':False,'task_complete':False}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'final_audit':audits[-1]}),flush=True)


if __name__ == '__main__':
    main()

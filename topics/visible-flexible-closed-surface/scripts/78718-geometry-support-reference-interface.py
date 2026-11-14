#!/usr/bin/env python3
"""Optional R93 support-reference chart and anchored background.

This module mutates only an explicitly supplied, newly constructed flow/BVP.
It does not install a global patch, run a solver, or change the physical metric.
The existing production driver and its checkpoint schema are not modified.
"""
from __future__ import annotations

import math
import types
import numpy as np


def coefficients_from_checkpoint(record):
    c = np.r_[float(record['actual_primary_amplitude']),
              np.asarray(record['parameters'][1:], float)
              * np.asarray(record['central_correction_scales'], float)]
    if len(c) != record['config']['modes']:
        raise ValueError('Incomplete support reference')
    return c


def _vec(z):
    return np.stack((z.real, z.imag, np.zeros_like(z.real)), axis=-1)


def _shape(flow, s):
    """The original scalar spline/cutoff and a quintic anchor blend."""
    s = np.atleast_1d(np.asarray(s, float))
    x = s/flow.end
    h0 = flow.spline(x)
    h1 = flow.spline(x, 1)/flow.end
    h2 = flow.spline(x, 2)/flow.end**2
    u = np.clip(4*x-3, 0., 1.)
    fac = 4/flow.end
    cut = 1-u**3*(10-15*u+6*u*u)
    cut1 = -30*u*u*(1-u)**2*fac
    cut2 = -60*u*(1-u)*(1-2*u)*fac**2
    chi = h0*cut
    chi1 = h1*cut+h0*cut1
    chi2 = h2*cut+2*h1*cut1+h0*cut2
    # The caller uses the physical prefix [0,end]. No extrapolated formula
    # is asserted for the compactly supported coordinate change.
    eta = 1-x**3*(10-15*x+6*x*x)
    eta1 = -30*x*x*(1-x)**2/flow.end
    eta2 = -60*x*(1-x)*(1-2*x)/flow.end**2
    return chi, chi1, chi2, eta, eta1, eta2


class ReferenceGeometry:
    """The complete coordinate/background jets, including mixed s,psi,psi."""
    def __init__(self, flow, coefficients, anchor=True):
        self.flow = flow
        self.c = np.asarray(coefficients, float).copy()
        self.c.setflags(write=False)
        self.k = 3*np.arange(1, len(self.c)+1)
        self.arc = (1-self.k*self.k)*self.c/self.k
        self.radius_lower = float(1-np.sum(abs((1-self.k*self.k)*self.c)))
        if not len(self.c) or self.radius_lower <= 0:
            raise ValueError('This interface requires a positive triangle bound for rho')
        if len(self.c) > flow.M:
            raise ValueError('Reference support is outside the represented linear space')
        self.anchor = bool(anchor)
        self.cache = {}

    def angular_parts(self, psi):
        psi = np.asarray(psi, float)
        phase = psi[..., None]*self.k
        co, si = np.cos(phase), np.sin(phase)
        h = 1+co@self.c
        hp = -si@(self.k*self.c)
        rho = 1+co@((1-self.k*self.k)*self.c)
        rhop = -si@(self.k*(1-self.k*self.k)*self.c)
        unit = np.exp(1j*psi)
        return dict(P=si@self.arc, P1=rho-1, P2=rhop,
                    gamma=(h+1j*hp)*unit,
                    gamma1=1j*rho*unit, gamma2=(-rho+1j*rhop)*unit)

    def uniform_parts(self, N):
        if N not in self.cache:
            psi = 2*np.pi*np.arange(N)/N
            self.cache[N] = (psi, self.angular_parts(psi))
        return self.cache[N]

    def evaluate(self, s, psi, parts=None):
        s = np.atleast_1d(np.asarray(s, float))
        psi = np.asarray(psi, float)
        if psi.ndim == 1:
            psi = psi[None, :]
        if psi.shape[0] not in (1, len(s)):
            raise ValueError('Angular rows must match radial rows')
        parts = self.angular_parts(psi) if parts is None else parts
        chi, chi1, chi2, eta, eta1, eta2 = _shape(self.flow, s)
        chi, chi1, chi2 = (v[:, None] for v in (chi, chi1, chi2))
        eta, eta1, eta2 = (v[:, None] for v in (eta, eta1, eta2))
        if not self.anchor:
            eta = np.zeros_like(eta); eta1 = np.zeros_like(eta1); eta2 = np.zeros_like(eta2)
        theta = psi+chi*parts['P']
        ts, tss = chi1*parts['P'], chi2*parts['P']
        rho, rhop = 1+chi*parts['P1'], chi*parts['P2']
        rhos, rhops = chi1*parts['P1'], chi1*parts['P2']
        if np.min(rho) <= 0:
            raise FloatingPointError('Support-reference material angle is not invertible')
        v = ts/rho
        vs = (tss*rho-ts*rhos)/rho**2
        vp = (rhos*rho-ts*rhop)/rho**2
        unit = np.exp(1j*theta)
        up = 1j*rho*unit
        upp = (1j*rhop-rho*rho)*unit
        us = 1j*ts*unit
        uss = (1j*tss-ts*ts)*unit
        usp = (1j*rhos-rho*ts)*unit
        uspp = (1j*rhops-2*rho*rhos+1j*ts*(1j*rhop-rho*rho))*unit
        C = (1-eta)*unit+eta*parts['gamma']
        Cp = (1-eta)*up+eta*parts['gamma1']
        Cpp = (1-eta)*upp+eta*parts['gamma2']
        Cs = (1-eta)*us+eta1*(parts['gamma']-unit)
        Css = (1-eta)*uss-2*eta1*us+eta2*(parts['gamma']-unit)
        Csp = (1-eta)*usp+eta1*(parts['gamma1']-up)
        Cspp = (1-eta)*uspp+eta1*(parts['gamma2']-upp)
        a, ap, app = (np.asarray(x)[:, None] for x in self.flow.profile(s))
        return dict(theta=theta, theta_s=ts, theta_ss=tss,
                    rho=rho, rhop=rhop, rhos=rhos, rhops=rhops,
                    v=v, vs=vs, vp=vp,
                    pos=_vec(a*C), p1=_vec(a*Cp), p2=_vec(a*Cpp),
                    s1=_vec(ap*C+a*Cs), s2=_vec(app*C+2*ap*Cs+a*Css),
                    sp=_vec(ap*Cp+a*Csp), spp=_vec(ap*Cpp+a*Cspp),
                    # e is only the old scalar fade diagnostic, NOT a formula
                    # for this multi-harmonic chart. Transport uses theta.
                    e=self.flow.warp_e*chi[:, 0], chi=chi[:, 0])

    def uniform(self, s, N):
        psi, parts = self.uniform_parts(N)
        return self.evaluate(s, psi, parts)

    def inlet_displacement(self, coefficients, psi):
        """Stable Gamma_c(A_cstar(psi))-gamma_cstar(psi).

        Solve for delta=phi-psi using sin differences, then evaluate the
        position difference without subtracting two order-one positions.
        At c=cstar both delta and the displacement are exactly zero.
        """
        c = np.asarray(coefficients, float)
        if len(c) != len(self.c):
            raise ValueError('Support coefficient dimensions differ')
        d = c-self.c
        psi = np.asarray(psi, float)
        base = psi[:, None]*self.k
        co, si = np.cos(base), np.sin(base)
        ad = (1-self.k*self.k)*d/self.k
        radius = 1+co@((1-self.k*self.k)*c)
        delta = -(si@ad)/radius
        period = 2*np.pi/3
        target = psi+si@self.arc
        lower = np.floor(target/period)*period-psi
        upper = lower+period
        eps = np.finfo(float).eps
        for iteration in range(80):
            half = delta[:, None]*self.k/2
            midpoint = base+half
            sindiff = 2*np.cos(midpoint)*np.sin(half)
            shifted = base+2*half
            sc, cc = np.sin(shifted), np.cos(shifted)
            residual = delta+sindiff@self.arc+sc@ad
            scale = (abs(delta)+abs(sindiff)@abs(self.arc)+abs(sc)@abs(ad))
            done = abs(residual) <= 64*eps*np.maximum(scale, np.finfo(float).tiny)
            if np.all(done):
                break
            lower = np.where((residual < 0) & ~done, delta, lower)
            upper = np.where((residual > 0) & ~done, delta, upper)
            rho = 1+cc@((1-self.k*self.k)*c)
            proposed = delta-residual/rho
            bad = (proposed <= lower) | (proposed >= upper) | ~np.isfinite(proposed)
            proposed = np.where(bad, (lower+upper)/2, proposed)
            delta = np.where(done, delta, proposed)
        if not np.all(done):
            raise FloatingPointError('Stable support-angle difference failed to converge')
        half = delta[:, None]*self.k/2
        midpoint = base+half
        sindiff = 2*np.cos(midpoint)*np.sin(half)
        cosdiff = -2*np.sin(midpoint)*np.sin(half)
        shifted = base+2*half
        cc, sc = np.cos(shifted), np.sin(shifted)
        dh = cosdiff@self.c+cc@d
        dhp = -sindiff@(self.k*self.c)-sc@(self.k*d)
        h = 1+cc@c
        hp = -sc@(self.k*c)
        expm1 = -2*np.sin(delta/2)**2+1j*np.sin(delta)
        displacement = np.exp(1j*psi)*(dh+1j*dhp+(h+1j*hp)*expm1)
        return dict(displacement=_vec(displacement), phi=psi+delta,
                    rho=1+cc@((1-self.k*self.k)*c),
                    arc_residual=float(np.max(abs(residual))),
                    arc_iterations=iteration+1)


def attach_flow(flow, coefficients):
    existing = getattr(flow, '_support_reference_geometry', None)
    if existing is not None:
        if not np.array_equal(existing.c, coefficients):
            raise ValueError('A running flow cannot change its fixed reference')
        return existing
    geometry = ReferenceGeometry(flow, coefficients, anchor=True)
    def geo(self, s, N):
        return geometry.uniform(s, N)
    def angular(self, N):
        psi, unused_parts = geometry.uniform_parts(N)
        g = geometry.uniform(np.array([0.]), N)
        return (psi, g['theta'][0], g['rho'][0], g['rhop'][0],
                g['pos'][0], g['p1'][0], g['p2'][0])
    def physical_base(self, s, N, derivative=0):
        return geometry.uniform(s, N)[('pos', 's1', 's2')[derivative]]
    flow.geo = types.MethodType(geo, flow)
    flow.angular = types.MethodType(angular, flow)
    flow.physical_base = types.MethodType(physical_base, flow)
    flow._support_reference_geometry = geometry
    flow._support_reference_record = dict(
        kind='fixed-support-reference-anchor-v1', coefficients=geometry.c.tolist(),
        scalar_fade='original adaptive spline times original cut-off',
        anchor_blend='1-10x^3+15x^4-6x^5, x=s/end',
        physical_metric_changed=False)
    return geometry


def attach_bvp(obj, coefficients):
    """Attach fixed reference geometry and its stable initial callback.

    Use transport_state_jets for a new warm start. The original restart and
    exporter routines do not by themselves understand this new background.
    """
    if not obj.fixed or obj.base_mode != 3:
        raise ValueError('This implementation is for the current fixed-g threefold BVP')
    if getattr(obj, '_support_reference_attached', False):
        raise ValueError('Reference is installed once per newly constructed BVP')
    reference = np.asarray(coefficients, float).copy()
    if len(reference) != obj.M:
        raise ValueError('Reference and state must have the same support dimension')
    original_factory = obj.Flow
    def factory(*args, **kwargs):
        flow = original_factory(*args, **kwargs)
        attach_flow(flow, reference)
        return flow
    obj.Flow = factory
    if obj.fixed_flow is not None:
        attach_flow(obj.fixed_flow, reference)
    if obj._flow is not None:
        attach_flow(obj._flow, reference)
    def initial(self, p):
        key = tuple(np.asarray(p, float))
        if key != self._core_key:
            from fixed_metric_mode3_core import PlanarSupportCore
            amplitude = self.seed_support_amplitude*math.exp(float(p[0]))
            if not 1e-7 < amplitude < .124:
                raise FloatingPointError('Support amplitude left the original search domain')
            core = PlanarSupportCore(amplitude, np.asarray(p[1:])*self.pscale, 3)
            flow = self.flow(p[0]); geometry = flow._support_reference_geometry
            N = max(2048, 128*self.M)
            angular = flow.angular(N); B, B1, B2 = flow.basis(N)
            exact = geometry.inlet_displacement(core.coefficients, angular[0])
            self._initial = flow.project(exact['displacement'][None, :, :], B)[:, 0]/self.q
            phi = exact['phi']; er = _vec(np.exp(1j*phi)); et = _vec(1j*np.exp(1j*phi))
            modes = core.frequencies[:, None]
            deriv = (np.cos(modes*phi[None, :])[:, :, None]*er[None, :, :]
                     -(np.sin(modes*phi[None, :])/modes)[:, :, None]*et[None, :, :])
            J = flow.project(deriv, B)
            self._initial_jac = np.zeros((self.n, self.M))
            self._initial_jac[:, 0] = amplitude*J[:, 0]/self.q
            self._initial_jac[:, 1:] = J[:, 1:]*self.pscale[None, :]/self.q
            pos_delta = flow.values((self.q*self._initial)[:, None], B)[0]
            first = flow.values((self.q*self._initial)[:, None], B1)[0]+angular[5]
            second = flow.values((self.q*self._initial)[:, None], B2)[0]+angular[6]
            exactfirst = et*angular[2][:, None]
            exactsecond = (-er/exact['rho'][:, None]*angular[2][:, None]**2
                           +et*angular[3][:, None])
            metric = np.sum(first*first, axis=1)/angular[2]**2-1
            self._inlet_metrics = dict(
                position=float(np.linalg.norm(pos_delta-exact['displacement'], axis=1).max()),
                first=float(np.linalg.norm(first-exactfirst, axis=1).max()),
                second=float(np.linalg.norm(second-exactsecond, axis=1).max()),
                metric_l1=float(np.sum(abs(np.fft.fft(metric)/N))),
                stable_arc_residual=exact['arc_residual'],
                stable_arc_iterations=exact['arc_iterations'],
                reference_equal=bool(np.array_equal(core.coefficients, reference)),
                scope='Finite angular diagnostic of the anchored inlet, not a continuous bound')
            self._core = core; self._core_key = key; self.support_amplitude = amplitude
        return self._initial
    obj.initial = types.MethodType(initial, obj)
    obj._core_key = None
    obj._support_reference_attached = True
    return obj


def _cylindrical_jet(coefficients, psi, order):
    """Physical Cartesian angular derivative of a cylindrical Fourier vector."""
    coefficients = np.asarray(coefficients)
    M = (coefficients.shape[0]-1)//3
    k = 3*np.arange(1, M+1)
    phase = psi[:, :, None]*k
    co, si = np.cos(phase), np.sin(phase)
    r, t, z = (coefficients[lo:hi].T for lo, hi in
               ((1, M+1), (M+1, 2*M+1), (2*M+1, 3*M+1)))
    dot = lambda table, values: np.einsum('snj,sj->sn', table, values)
    R = coefficients[0, :, None]+dot(co, r)
    T = dot(si, t)
    Z = dot(co, z)
    if order == 1:
        R, T, Z = -dot(si, k*r)-T, R+dot(co, k*t), -dot(si, k*z)
    elif order == 2:
        R, T, Z = (-dot(co, k*k*r)-R-2*dot(co, k*t),
                   -2*dot(si, k*r)-dot(si, k*k*t)-T, -dot(co, k*k*z))
    elif order != 0:
        raise ValueError('Only angular orders zero through two are used')
    value = _vec((R+1j*T)*np.exp(1j*psi))
    value[:, :, 2] = Z
    return value


def transport_state_jets(oldflow, old_pp, newflow, s, N=2048):
    """Pull back old raw PP values/two-jets, then project a new warm state.

    The omitted old vertical mean H(s) must be added to mean[0], and H',H''
    to mean[1:3], for an exact full-map transport. Angular derivatives and
    projected nonmean state jets are independent of those unknown constants.
    This function creates no checkpoint and does not call the BVP or DN.
    """
    s = np.atleast_1d(np.asarray(s, float))
    if oldflow.end != newflow.end:
        raise ValueError('Transport here preserves the same physical radial interval')
    new = newflow._support_reference_geometry
    old = getattr(oldflow, '_support_reference_geometry', None)
    if old is None:
        old = ReferenceGeometry(oldflow, [oldflow.warp_e/8], anchor=False)
    ng = new.uniform(s, N)
    phi = ng['theta'].copy()
    chi = _shape(oldflow, s)[0][:, None]
    for iteration in range(40):
        parts = old.angular_parts(phi)
        residual = phi+chi*parts['P']-ng['theta']
        update = residual/(1+chi*parts['P1'])
        phi -= update
        if np.max(abs(update)) < 4e-15:
            break
    og = old.evaluate(s, phi)
    if np.max(abs(og['theta']-ng['theta'])) > 3e-13:
        raise FloatingPointError('Material pullback failed')
    pp = ng['rho']/og['rho']
    ps = (ng['theta_s']-og['theta_s'])/og['rho']
    ppp = (ng['rhop']-og['rhop']*pp*pp)/og['rho']
    psp = (ng['rhos']-og['rhos']*pp-og['rhop']*ps*pp)/og['rho']
    pss = (ng['theta_ss']-og['theta_ss']-2*og['rhos']*ps-og['rhop']*ps*ps)/og['rho']
    y, dy, ddy = (old_pp(s, j) for j in range(3))
    X = og['pos']+oldflow.q*_cylindrical_jet(y, phi, 0)
    Xs = og['s1']+oldflow.q*_cylindrical_jet(dy, phi, 0)
    Xss = og['s2']+oldflow.q*_cylindrical_jet(ddy, phi, 0)
    Xp = og['p1']+oldflow.q*_cylindrical_jet(y, phi, 1)
    Xpp = og['p2']+oldflow.q*_cylindrical_jet(y, phi, 2)
    Xsp = og['sp']+oldflow.q*_cylindrical_jet(dy, phi, 1)
    scalar = lambda x: x[:, :, None]
    transported = dict(
        pos=X, p1=Xp*scalar(pp),
        s1=Xs+Xp*scalar(ps),
        p2=Xpp*scalar(pp*pp)+Xp*scalar(ppp),
        sp=Xsp*scalar(pp)+Xpp*scalar(ps*pp)+Xp*scalar(psp),
        s2=Xss+2*Xsp*scalar(ps)+Xpp*scalar(ps*ps)+Xp*scalar(pss))
    B, unused_B1, unused_B2 = newflow.basis(N)
    state = [newflow.project(transported[k]-ng[k], B)/newflow.q
             for k in ('pos', 's1', 's2')]
    means = np.stack([np.mean(transported[k][:, :, 2], axis=1)
                      for k in ('pos', 's1', 's2')])
    return dict(jets=transported, state_jets=state, mean_shift_jets=means,
                old_angle=phi, new_geometry=ng,
                coordinate_residual=float(np.max(abs(og['theta']-ng['theta']))),
                inverse_iterations=iteration+1,
                new_warm_only=True, omitted_original_height_mean=True)

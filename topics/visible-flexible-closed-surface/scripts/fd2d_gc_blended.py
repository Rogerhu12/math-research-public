#!/usr/bin/env python3
"""Fixed-material Codazzi equations in a radially changing angular chart.

u=U(s,xi)=(1-beta(s))*U_seed(xi)+beta(s)*xi.  This is a coordinate
change of the SAME g, not a different metric.  Its nonorthogonal coordinate
metric is recorded explicitly.  Only intrinsic n,m are evolved here.

For the eventual actual surface we select reconstruction along FIXED
MATERIAL u with xi(s,u) inverted in these fields, followed by the original
skew radial frame ODE.  Integrating the moving connection with nonzero
finite Codazzi residual would define a different approximate map; it is
not substituted silently for that selected reconstruction.
"""
from __future__ import annotations
import numpy as np
from fd2d_gc_intrinsic import IntrinsicGC, LD


class BlendedIntrinsicGC(IntrinsicGC):
    def __init__(self, *args, blend_interval=(.58, 1.40), **kwargs):
        super().__init__(*args, **kwargs)
        self.blend_interval = tuple(float(x) for x in blend_interval)
        if not (0 <= self.blend_interval[0] < self.blend_interval[1] <= self.candidate.end):
            raise ValueError('The chart transition must lie in the physical prefix interval')

    def blend(self, s):
        left, right = self.blend_interval
        t = np.clip((np.atleast_1d(np.asarray(s, dtype=LD))-left)/(right-left), 0, 1)
        value = t**3*(10-15*t+6*t*t)
        first = 30*t*t*(1-t)**2/(right-left)
        second = 60*t*(1-t)*(1-2*t)/(right-left)**2
        return value, first, second

    def coordinates(self, s, coordinate=None):
        if coordinate is None:
            xi, u0, v0, vv0 = self.theta, self.u, self.u_theta, self.u_theta_theta
        else:
            xi = np.atleast_1d(np.asarray(coordinate, dtype=LD))
            initial = self.reference.reference_coordinate(xi)
            u0, v0, vv0 = (np.asarray(initial[k], dtype=LD) for k in ('u', 'u_theta', 'u_theta_theta'))
        beta, beta_s, beta_ss = self.blend(s)
        displacement = u0-xi
        U = xi[:, None]+(1-beta[None, :])*displacement[:, None]
        Ux = 1+(1-beta[None, :])*(v0[:, None]-1)
        Uxx = (1-beta[None, :])*vv0[:, None]
        Us = -beta_s[None, :]*displacement[:, None]
        Usx = -beta_s[None, :]*(v0[:, None]-1)
        Uss = -beta_ss[None, :]*displacement[:, None]
        if np.any(Ux <= 0):
            raise FloatingPointError('The common angular chart is not a diffeomorphism')
        return dict(u=U, u_xi=Ux, u_xixi=Uxx, u_s=Us, u_sxi=Usx, u_ss=Uss,
                    advection=Us/Ux, beta=beta, beta_s=beta_s, beta_ss=beta_ss)

    def fields(self, s, state):
        try:
            f = super().fields(s, state)
        except ArithmeticError as exc:
            raise FloatingPointError(str(exc)) from exc
        coordinates = self.coordinates(s)
        f['inverse_b'] = 1/(coordinates['u_xi']*f['a'])
        f['advection'] = coordinates['advection']
        f['coordinates'] = coordinates
        return f

    def rhs(self, s, state):
        f = self.fields(s, state)
        n, m, l = f['n'], f['m'], f['l']
        derivatives = self.derivative(np.stack((n, m, l), axis=1))
        velocity = np.stack((derivatives[:, 1]*f['inverse_b']+f['c']*(l-n)+f['advection']*derivatives[:, 0],
                             derivatives[:, 2]*f['inverse_b']-2*f['c']*m+f['advection']*derivatives[:, 1]), axis=1)
        self.calls += 1
        answer = self.encode(velocity)
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError('Nonfinite finite Codazzi velocity')
        return answer[:, 0] if f['single'] else answer

    def jvp(self, s, state, direction):
        state, direction = np.asarray(state), np.asarray(direction)
        if state.ndim != 1:
            raise ValueError('JVP accepts a single radial base state')
        single = direction.ndim == 1
        if single:
            direction = direction[:, None]
        f = self.fields(s, state)
        values = self.decode(direction)
        dn, dm = values[:, 0], values[:, 1]
        dl = (2*f['m']*dm-f['l']*dn)/f['n']
        derivatives = self.derivative(np.stack((dn, dm, dl), axis=1))
        velocity = np.stack((derivatives[:, 1]*f['inverse_b']+f['c']*(dl-dn)+f['advection']*derivatives[:, 0],
                             derivatives[:, 2]*f['inverse_b']-2*f['c']*dm+f['advection']*derivatives[:, 1]), axis=1)
        self.jvp_calls += 1
        answer = self.encode(velocity)
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError('Nonfinite finite Codazzi tangent')
        return answer[:, 0] if single else answer

    def coordinate_metric(self, s):
        a, _, _ = self.profile(s)
        c = self.coordinates(s)
        return dict(E=1+(a*c['u_s'])**2, F=a*a*c['u_s']*c['u_xi'],
                    G=(a*c['u_xi'])**2, determinant=(a*c['u_xi'])**2,
                    scope='Exact coordinate expression of the unchanged ds^2+a(s)^2 du^2 target.')

    def chart_definition(self):
        return dict(kind='fixed-seed-normal-to-material-quintic', blend_interval=list(self.blend_interval),
                    beta='10*t^3-15*t^4+6*t^5, t=clip((s-left)/(right-left),0,1)',
                    U='(1-beta)*arc_seed(xi)/a0+beta*xi',
                    target_metric='(1+a^2*U_s^2) ds^2+2*a^2*U_s*U_xi ds dxi+a^2*U_xi^2 dxi^2',
                    material_metric_changed=False,
                    intended_actual_map='Reconstruct at fixed material u after inverting xi(s,u); use the original skew radial frame ODE.')

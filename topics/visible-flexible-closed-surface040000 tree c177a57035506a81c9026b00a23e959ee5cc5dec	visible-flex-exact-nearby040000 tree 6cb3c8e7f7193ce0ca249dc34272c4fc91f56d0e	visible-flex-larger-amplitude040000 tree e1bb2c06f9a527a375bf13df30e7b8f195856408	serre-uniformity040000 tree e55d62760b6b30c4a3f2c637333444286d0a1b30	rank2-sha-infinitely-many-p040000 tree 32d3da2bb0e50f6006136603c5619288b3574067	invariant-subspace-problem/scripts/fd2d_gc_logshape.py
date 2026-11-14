#!/usr/bin/env python3
"""Positive-normal Codazzi coordinates on the unchanged candidate metric.

n=n_ref*exp(eta), m=n_ref*zeta, n_ref=sqrt(1-a_s^2)/a.
This is an exact dependent-variable change wherever |a_s|<1 and n>0;
no n value is clipped.  The Fourier unknowns are eta (even) and zeta (odd).
The zero state is the actual rotational background for every candidate.
The radial angular chart remains the explicitly recorded U(s,xi).
"""
from __future__ import annotations
import numpy as np
from fd2d_gc_blended import BlendedIntrinsicGC
from fd2d_gc_intrinsic import LD


class LogShapeGC(BlendedIntrinsicGC):
    state_representation = 'eta=log(n/n_ref), zeta=m/n_ref; real cosine/sine amplitudes'

    def fields(self, s, state):
        state = np.asarray(state)
        single = state.ndim == 1
        if single:
            state = state[:, None]
        if state.ndim != 2:
            raise ValueError('Expected one state or a radial array')
        values = self.decode(state)
        eta, zeta = values[:, 0], values[:, 1]
        a, ap, app = self.profile(s)
        b2 = 1-ap*ap
        if np.any(b2 <= 0):
            raise FloatingPointError('Rotational normalization requires |a_prime|<1')
        nr = np.sqrt(b2)/a
        K, c = -app/a, ap/a
        beta = K/(nr*nr)
        with np.errstate(over='ignore', under='ignore', invalid='ignore'):
            positive = np.exp(eta)
            inverse = np.exp(-eta)
        n, m = nr*positive, nr*zeta
        l = nr*inverse*(zeta*zeta+beta)
        if np.any(n <= 0) or not all(np.all(np.isfinite(x)) for x in (n, m, l)):
            raise FloatingPointError('Nonfinite positive-normal coordinate trial')
        coordinates = self.coordinates(s)
        return dict(eta=eta, zeta=zeta, exponential=positive, inverse_exponential=inverse,
                    n=n, m=m, l=l, n_reference=nr, beta=beta, c=c, K=K,
                    a=a, ap=ap, app=app, dlog_n_reference=c*(beta-1),
                    inverse_b=1/(coordinates['u_xi']*a), advection=coordinates['advection'],
                    coordinates=coordinates, single=single)

    def rhs(self, s, state):
        f = self.fields(s, state)
        eta, zeta, q = f['eta'], f['zeta'], f['inverse_exponential']
        dx = self.derivative(np.stack((eta, zeta), axis=1))
        ex, zx = dx[:, 0], dx[:, 1]
        B = zeta*zeta+f['beta']
        Lx = q*(2*zeta*zx-B*ex)
        velocity = np.stack((q*zx*f['inverse_b']+f['c']*(q*q*B-f['beta'])+f['advection']*ex,
                             Lx*f['inverse_b']-f['c']*(1+f['beta'])*zeta+f['advection']*zx), axis=1)
        answer = self.encode(velocity)
        self.calls += 1
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError('Nonfinite normalized Codazzi velocity')
        return answer[:, 0] if f['single'] else answer

    def jvp(self, s, state, direction):
        state, direction = np.asarray(state), np.asarray(direction)
        if state.ndim != 1:
            raise ValueError('JVP accepts a single radial base state')
        single = direction.ndim == 1
        if single:
            direction = direction[:, None]
        f = self.fields(s, state)
        eta, zeta, q = f['eta'], f['zeta'], f['inverse_exponential']
        dx = self.derivative(np.stack((eta, zeta), axis=1))
        ex, zx = dx[:, 0], dx[:, 1]
        delta = self.decode(direction)
        de, dz = delta[:, 0], delta[:, 1]
        delta_dx = self.derivative(delta)
        dex, dzx = delta_dx[:, 0], delta_dx[:, 1]
        B = zeta*zeta+f['beta']
        dQ = 2*zeta*dz-B*de
        dQx = 2*zx*dz+2*zeta*dzx-2*zeta*zx*de-B*dex
        dLx = q*(dQx-ex*dQ)
        velocity = np.stack((q*(dzx-de*zx)*f['inverse_b']+2*f['c']*q*q*(zeta*dz-B*de)+f['advection']*dex,
                             dLx*f['inverse_b']-f['c']*(1+f['beta'])*dz+f['advection']*dzx), axis=1)
        answer = self.encode(velocity)
        self.jvp_calls += 1
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError('Nonfinite normalized Codazzi JVP')
        return answer[:, 0] if single else answer

    def physical_values_and_derivatives(self, s, state, first):
        """Use the actual native interpolant derivative, never substitute RHS."""
        f = self.fields(s, state)
        native_first = self.decode(first)
        if native_first.ndim == 2:
            native_first = native_first[:, :, None]
        n_s = f['n']*(native_first[:, 0]+f['dlog_n_reference'])
        m_s = f['n_reference']*(native_first[:, 1]+f['dlog_n_reference']*f['zeta'])
        dx = self.derivative(np.stack((f['eta'], f['zeta']), axis=1))
        n_x = f['n']*dx[:, 0]
        m_x = f['n_reference']*dx[:, 1]
        l_x = f['n_reference']*f['inverse_exponential']*(
            2*f['zeta']*dx[:, 1]-(f['zeta']**2+f['beta'])*dx[:, 0])
        return dict(fields=f, values=np.stack((f['n'], f['m']), axis=1),
                    first=np.stack((n_s, m_s), axis=1),
                    angular=np.stack((n_x, m_x, l_x), axis=1))

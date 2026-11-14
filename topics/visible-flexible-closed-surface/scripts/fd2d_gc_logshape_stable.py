#!/usr/bin/env python3
"""The same positive-normal equations with an expm1 background subtraction.

Only evaluation of exp(-2 eta)*(zeta^2+chi)-chi is changed to the equal
zeta^2*exp(-2 eta)+chi*expm1(-2 eta).  The inherited analytic JVP and
physical reconstruction formulas are unchanged.
"""
import numpy as np
from fd2d_gc_logshape import LogShapeGC as OriginalLogShapeGC


class LogShapeGC(OriginalLogShapeGC):
    def rhs(self, s, state):
        f = self.fields(s, state)
        eta, zeta, q = f['eta'], f['zeta'], f['inverse_exponential']
        dx = self.derivative(np.stack((eta, zeta), axis=1))
        ex, zx = dx[:, 0], dx[:, 1]
        B = zeta*zeta+f['beta']
        Lx = q*(2*zeta*zx-B*ex)
        reaction = zeta*zeta*q*q+f['beta']*np.expm1(-2*eta)
        velocity = np.stack((q*zx*f['inverse_b']+f['c']*reaction+f['advection']*ex,
                             Lx*f['inverse_b']-f['c']*(1+f['beta'])*zeta+f['advection']*zx), axis=1)
        answer = self.encode(velocity)
        self.calls += 1
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError('Nonfinite normalized Codazzi velocity')
        return answer[:, 0] if f['single'] else answer

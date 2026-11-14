#!/usr/bin/env python3
"""Exact flat tail with nonnegative Bernstein curvature controls.

For degree K, alpha_q = 630 q^4(1-q)^4 sum p_i B_i^K(q).
The angle is its exact integral.  If 0<=p_i<=6/5, then
0<=alpha<=6/5, 0<=kappa<=4725/736 for width .46, and
alpha(q)<=6*S9(q)/5.  Thus convexity, the fixed collar and the
same deflection/normal-ball budgets are preserved throughout this box.
These are a selected constructive family, not necessary conditions for
every possible flat annulus. Position integrals are evaluated numerically.
"""
from functools import lru_cache
from fractions import Fraction
from math import comb, factorial
import numpy as np
from scipy.special import betainc
from fd2d_flat_developable_family import FlatDevelopableFamily


@lru_cache(maxsize=16)
def primitive_weights(degree):
    exact = [Fraction(630*comb(degree, i)*factorial(i+4)*factorial(degree-i+4),
                      factorial(degree+9)) for i in range(degree+1)]
    assert sum(exact) == 1
    return np.array([float(v) for v in exact]), tuple(str(v) for v in exact)


@lru_cache(maxsize=8)
def gauss(order):
    return np.polynomial.legendre.leggauss(order)


class PositiveFlatDevelopableFamily(FlatDevelopableFamily):
    @staticmethod
    def initial_coefficients(amplitude, count):
        return np.full(count, float(amplitude))

    def angle_basis(self, q):
        q = np.asarray(q, float)
        t = np.clip(q, 0., 1.)
        degree = self.parameter_count-1
        weights, _ = primitive_weights(degree)
        values, first, second = [], [], []
        inside = (q > 0.) & (q < 1.)
        for i in range(degree+1):
            j = degree-i
            scale = 630*comb(degree, i)
            values.append(weights[i]*betainc(i+5, j+5, t))
            first.append(np.where(inside, scale*t**(i+4)*(1-t)**(j+4), 0.))
            second.append(np.where(inside, scale*((i+4)*t**(i+3)*(1-t)**(j+4)-
                                                   (j+4)*t**(i+4)*(1-t)**(j+3)), 0.))
        return tuple(np.stack(rows, axis=-1) for rows in (values, first, second))

    def angle_jets(self, y):
        y = np.asarray(y, float)
        sign = np.sign(y)
        value, first, second = self.angle_basis((np.abs(y)-self.flat_radius)/self.width)
        aJ = sign[..., None]*value
        kJ = first/self.width
        kyJ = sign[..., None]*second/self.width**2
        alpha, kappa, kappa_y = [v@self.coefficients for v in (aJ, kJ, kyJ)]
        return dict(alpha=alpha, kappa=kappa, kappa_y=kappa_y,
            alpha_jacobian=aJ, kappa_jacobian=kJ, kappa_y_jacobian=kyJ,
            cos_alpha=np.cos(alpha), sin_alpha=np.sin(alpha))

    def curve(self, y, *, integrate=True):
        y = np.asarray(y, float)
        result = self.angle_jets(y)
        if not integrate:
            return result
        flat = y.ravel()
        X, Z = flat.copy(), np.zeros_like(flat)
        XJ = np.zeros((len(flat), self.parameter_count)); ZJ = np.zeros_like(XJ)
        nodes, weights = gauss(self.quadrature_order)
        endpoint, _ = primitive_weights(self.parameter_count-1)
        A = endpoint@self.coefficients
        for start in range(0, len(flat), self.quadrature_chunk):
            end = min(len(flat), start+self.quadrature_chunk)
            yf = flat[start:end]; sign = np.sign(yf)
            v = np.maximum(np.abs(yf)-self.flat_radius, 0.)/self.width
            vmax = np.minimum(v, 1.)
            basis = self.angle_basis(vmax[:, None]*(nodes+1)/2)[0]
            angle = basis@self.coefficients
            sn, cs = np.sin(angle), np.cos(angle)
            scale = self.width*vmax/2
            X[start:end] += sign*scale*np.sum(-2*np.sin(angle/2)**2*weights, axis=1)
            Z[start:end] = scale*np.sum(sn*weights, axis=1)
            XJ[start:end] = -sign[:, None]*scale[:, None]*np.einsum('no,nop,o->np', sn, basis, weights)
            ZJ[start:end] = scale[:, None]*np.einsum('no,nop,o->np', cs, basis, weights)
            beyond = self.width*np.maximum(v-1, 0.)
            X[start:end] += sign*beyond*(np.cos(A)-1)
            Z[start:end] += beyond*np.sin(A)
            XJ[start:end] -= (sign*beyond*np.sin(A))[:, None]*endpoint
            ZJ[start:end] += (beyond*np.cos(A))[:, None]*endpoint
        result.update(X=X.reshape(y.shape), Z=Z.reshape(y.shape),
            X_jacobian=XJ.reshape(y.shape+(self.parameter_count,)),
            Z_jacobian=ZJ.reshape(y.shape+(self.parameter_count,)))
        return result

    def sufficient_bounds(self):
        lower, upper = float(self.coefficients.min()), float(self.coefficients.max())
        weights, exact = primitive_weights(self.parameter_count-1)
        absolute = max(abs(lower), abs(upper))
        A = float(weights@self.coefficients)
        return dict(degree=self.parameter_count-1, controls_lower=lower, controls_upper=upper,
            endpoint_angle=A, endpoint_weights_exact=list(exact),
            selected_box_0_to_6_over_5=lower >= 0 and upper <= 1.2,
            curvature_nonnegative_sufficient=lower >= 0,
            absolute_curvature_upper=absolute*315/(128*self.width),
            absolute_angle_upper=absolute,
            positive_projection_sufficient=absolute < np.pi/2,
            absolute_deflection_upper=absolute*self.width/2,
            scope='Exact Bernstein partition-of-unity bounds, not sampled maxima. Cuff and phase fixed exactly.')

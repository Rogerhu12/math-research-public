"""One finite M8 path from all seven cosine columns to B2..B6,T,U.

C_j(lambda)=(1-lambda)*cos(3*j*phi)+lambda*E_j(phi), j=2..8,
where E=(B2,...,B6,SA-SB,SB) is the already defined R44 endpoint.
This changes the physical finite space; it is not fixed-g refinement or a
reparametrization of the earlier infinite-dimensional raw-control homotopy.
The defining mean and primary moments vanish; production rounded projection
coefficients still have the inherited separate evaluation-error budget.
"""
from fractions import Fraction as F
import math
import numpy as np
from circle_trace_replacement_basis import CircleTraceReplacementBasis
from moment_interval_bounds import upper_float


class CircleTraceHomotopyBasis:
    def __init__(self, base_mode=3, modes=8, halfwidth=.21, transition=.4,
                 center=math.pi/3, precision=80, quadrature_order=64,
                 lock_fundamental=True):
        if base_mode != 3 or modes != 8 or not lock_fundamental:
            raise ValueError('This declared finite path has n3 and all seven M8 controls')
        if float(center).hex() != float(math.pi/3).hex():
            raise ValueError('This path uses the literal reflection axis pi/3')
        self.endpoint = CircleTraceReplacementBasis(base_mode=base_mode, modes=modes,
            halfwidth=halfwidth, transition=transition, center=center,
            precision=precision, quadrature_order=quadrature_order,
            lock_fundamental=lock_fundamental)
        self.n, self.M = 3, 8
        self.frequencies = 3*np.arange(2, 9, dtype=float)
        # The original core multiplies coefficient errors by lambda itself.
        # These are therefore the endpoint bounds, without a second lambda.
        self.coefficient_evaluation_error_bounds = self.endpoint.coefficient_evaluation_error_bounds.copy()
        self.fundamental_evaluation_error = np.zeros(7)
        self.fundamental_absolute_upper = np.zeros(7)
        self.fundamental_leakage = np.zeros(7)

    @staticmethod
    def checked_lambda(homotopy):
        lam = float(homotopy)
        if not math.isfinite(lam) or not 0 <= lam <= 1:
            raise ValueError('Finite circle-trace path requires 0<=lambda<=1')
        return lam

    def cosine_support_jets(self, phi, order):
        flat = np.asarray(phi, float).ravel()
        m = self.frequencies[:, None]
        angle = m*flat[None, :]
        return tuple(m**k*np.cos(angle+k*np.pi/2) for k in range(order+1))

    def support_jets(self, phi, order=4, homotopy=1.):
        lam = self.checked_lambda(homotopy)
        if not 0 <= order <= 4:
            raise ValueError('Support derivatives zero through four only')
        if lam == 1.:
            return self.endpoint.support_jets(phi, order, 1.)
        old = self.cosine_support_jets(phi, order)
        if lam == 0.:
            return old
        endpoint = self.endpoint.support_jets(phi, order, 1.)
        return tuple((1-lam)*a+lam*b for a,b in zip(old,endpoint))

    def primitive_jets(self, phi, order=5, homotopy=1.):
        lam = self.checked_lambda(homotopy)
        if not 0 <= order <= 5:
            raise ValueError('Primitive derivatives zero through five only')
        if lam == 1.:
            return self.endpoint.primitive_jets(phi, order, 1.)
        flat = np.asarray(phi, float).ravel()
        m = self.frequencies[:, None]
        primitive = np.sin(m*flat[None, :])/m
        old = (primitive,) if order == 0 else (primitive,)+self.cosine_support_jets(phi,order-1)
        if lam == 0.:
            return old
        endpoint = self.endpoint.primitive_jets(phi,order,1.)
        return tuple((1-lam)*a+lam*b for a,b in zip(old,endpoint))

    def homotopy_rho_bounds(self, homotopy=1.):
        lam = self.checked_lambda(homotopy)
        endpoint = self.endpoint.homotopy_rho_bounds(1.)
        if lam == 1.:
            return endpoint
        lf = F.from_float(lam)
        out = []
        for k in range(3):
            values=[]
            for j,m in enumerate(range(6,25,3)):
                old=F(m*m-1)*m**k
                values.append(upper_float((1-lf)*old+lf*F.from_float(float(endpoint[k][j]))))
            out.append(np.asarray(values))
        return tuple(out)

    def combined_control_rho_bounds(self, coefficients, homotopy=1.):
        lam = self.checked_lambda(homotopy)
        c = np.asarray(coefficients,float)
        if c.shape!=(7,) or not np.all(np.isfinite(c)):
            raise ValueError('Use all seven finite physical controls')
        endpoint = self.endpoint.combined_control_rho_bounds(c,1.)
        if lam == 1.:
            return endpoint
        lf=F.from_float(lam)
        out=[]
        for k in range(3):
            cosine=sum(abs(F.from_float(float(c[j])))*F(m*m-1)*m**k
                       for j,m in enumerate(range(6,25,3)))
            out.append(upper_float((1-lf)*cosine+lf*F.from_float(float(endpoint[k]))))
        return tuple(out)

    def summary(self):
        return dict(base_mode=3,modes=8,controls=7,
            columns_at_zero=['cos6','cos9','cos12','cos15','cos18','cos21','cos24'],
            columns_at_one=['B2','B3','B4','B5','B6','T=SA-SB','U=SB'],
            homotopy='C_j=(1-lambda)*cos(3*j*phi)+lambda*E_j, j=2..8',
            endpoint=self.endpoint.summary(),
            positivity_budget='Convex sum of whole-domain cosine rho-jet bounds and the already combined endpoint trace bound; no sampled derivative maxima.',
            scope=__doc__)

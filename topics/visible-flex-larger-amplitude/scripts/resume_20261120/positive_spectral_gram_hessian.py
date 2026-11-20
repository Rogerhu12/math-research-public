#!/usr/bin/env python3
"""Exact positive spectral residual Hessian, with the original true gradient.

E=[[e,f],[f,g]], phi(E)=tr(((E^2+eps^2 I)/scale^2)^k).
h(t)=t*((t^2+eps^2)/scale^2)^(k-1). The unscaled positive
block is L=T* Dh(E) T; half the point Hessian is (k/scale^2)L.
The unscaled half gradient remains T*h(E), NOT L times (e,f,g).

All arithmetic here is ordinary floating point, not outward certification.
The exact formulas and the positive Gauss divided difference are proved
in R664. This is a residual Hessian pullback, not the full x-Hessian.
"""
from functools import lru_cache
import numpy as np


SQRT2 = np.sqrt(2.)


@lru_cache(maxsize=None)
def positive_gauss(k):
    """k positive Gauss nodes/weights on [0,1], exact through degree 2k-1."""
    x, w = np.polynomial.legendre.leggauss(k)
    t, w = .5*(x+1.), .5*w
    if np.any(t <= 0) or np.any(t >= 1) or np.any(w <= 0):
        raise ArithmeticError('Positive Gauss rule was not obtained')
    t.setflags(write=False); w.setflags(write=False)
    return t, w


def hprime(value, parameters):
    p = parameters
    value = np.asarray(value)
    if p.k == 1:
        return np.ones_like(value)
    z2 = (value/p.scale)**2
    ep2 = (p.epsilon/p.scale)**2
    return (z2+ep2)**(p.k-2)*(ep2+(2*p.k-1)*z2)


def symmetric_power(a, b, d, exponent):
    """Polynomial power of [[a,b],[b,d]], also holomorphic for CS checks."""
    u, v, w = np.ones_like(a), np.zeros_like(b), np.ones_like(d)
    for _ in range(exponent):
        # The exact matrices commute; average the two off-diagonal formulas.
        u, v, w = u*a+v*b, .5*(u*b+v*d+v*a+w*b), v*b+w*d
    return u, v, w


def primitive_gradient(residual, parameters):
    """T* h(E); multiply by 2k/scale^2 for the true point gradient.

    This is the same polynomial as the R660 K(E)r. It is independently
    evaluated and never replaced by the Hessian block times the base r.
    Complex inputs are allowed for a holomorphic differentiation check.
    """
    r, p = np.asarray(residual), parameters
    e, f, g = r[..., 0], r[..., 1], r[..., 2]
    q00 = (e*e+f*f+p.epsilon*p.epsilon)/(p.scale*p.scale)
    q01 = f*(e+g)/(p.scale*p.scale)
    q11 = (g*g+f*f+p.epsilon*p.epsilon)/(p.scale*p.scale)
    u, v, w = symmetric_power(q00, q01, q11, p.k-1)
    return np.stack((u*e+v*f, v*e+(u+w)*f+v*g, v*f+w*g), axis=-1)


class HessianBlocks:
    """L=T*Dh(E)T, stored through an everywhere positive square-root factor.

    .whiten(r)=B r, .whiten(r,transpose=True)=B^T r, L=B^T B.
    No eigenvector angle or division by a small eigenvalue gap is needed.
    The divided difference is the positive k-point integral of hprime.
    .normal_and_gradient retains the R660 true half-gradient convention.
    """
    def __init__(self, residual, parameters):
        self.parameters = p = parameters
        r = np.asarray(residual)
        if r.shape[-1] != 3 or np.iscomplexobj(r) or not np.isfinite(r).all():
            raise ValueError('Freeze the residual Hessian at a finite real Gram state')
        if p.p < 2 or p.p % 2 or p.epsilon <= 0 or p.scale <= 0:
            raise ValueError('Use even p>=2 and strictly positive epsilon/scale')
        e, f, g = r[..., 0], r[..., 1], r[..., 2]
        gap = np.hypot(e-g, 2*f)
        plus, minus = .5*(e+g+gap), .5*(e+g-gap)
        self.axis = np.divide(e-g, gap, out=np.ones_like(gap), where=gap != 0)
        self.offaxis = np.divide(2*f, gap, out=np.zeros_like(gap), where=gap != 0)
        wp, wm = hprime(plus, p), hprime(minus, p)
        divided = np.zeros_like(gap)
        t, weights = positive_gauss(p.k)
        for theta, weight in zip(t, weights):
            divided += weight*hprime((1-theta)*minus+theta*plus, p)
        # The repeated eigenvalue has an exact continuous formula.
        divided = np.where(gap == 0, wp, divided)
        self.minimum_eigenweight = float(min(wp.min(), wm.min(), divided.min()))
        self.maximum_eigenweight = float(max(wp.max(), wm.max(), divided.max()))
        if not self.minimum_eigenweight > 0 or not np.isfinite(self.maximum_eigenweight):
            raise ArithmeticError('Finite arithmetic lost a positive derivative eigenweight')
        self.root_plus, self.root_off, self.root_minus = np.sqrt(wp), np.sqrt(divided), np.sqrt(wm)

    def whiten(self, residual, transpose=False):
        r = np.asarray(residual)
        n, s = self.axis, self.offaxis
        a, b, d = self.root_plus, self.root_off, self.root_minus
        e, f, g = r[..., 0], r[..., 1], r[..., 2]
        if transpose:
            plus, off, minus = a*e, b*f, d*g
            mean, difference = .5*(plus+minus), .5*(plus-minus)
            return np.stack((mean+n*difference-s*off/SQRT2,
                2*s*difference+SQRT2*n*off,
                mean-n*difference+s*off/SQRT2), axis=-1)
        mean, difference = .5*(e+g), .5*(e-g)
        return np.stack((a*(mean+n*difference+s*f),
            b*SQRT2*(-s*difference+n*f),
            d*(mean-n*difference-s*f)), axis=-1)

    def inverse_transpose(self, cotangent):
        """Solve B^T y=cotangent. Used for the true-gradient LSMR RHS.

        The spectral-coordinate transform T satisfies T^T T=diag(1,2,1),
        so T^{-T}=T diag(1,1/2,1). This is an explicit inverse, not a fit.
        """
        g = np.asarray(cotangent)
        n, s = self.axis, self.offaxis
        e, f, z = g[..., 0], .5*g[..., 1], g[..., 2]
        mean, difference = .5*(e+z), .5*(e-z)
        return np.stack(((mean+n*difference+s*f)/self.root_plus,
            SQRT2*(-s*difference+n*f)/self.root_off,
            (mean-n*difference-s*f)/self.root_minus), axis=-1)

    def whiten_columns(self, jacobian, transpose=False):
        """Apply B or B^T to columns (...,3,d), preserving every column."""
        J = np.asarray(jacobian)
        n, s = self.axis[..., None], self.offaxis[..., None]
        a, b, d = self.root_plus[..., None], self.root_off[..., None], self.root_minus[..., None]
        e, f, g = J[..., 0, :], J[..., 1, :], J[..., 2, :]
        if transpose:
            plus, off, minus = a*e, b*f, d*g
            mean, difference = .5*(plus+minus), .5*(plus-minus)
            return np.stack((mean+n*difference-s*off/SQRT2,
                2*s*difference+SQRT2*n*off,
                mean-n*difference+s*off/SQRT2), axis=-2)
        mean, difference = .5*(e+g), .5*(e-g)
        return np.stack((a*(mean+n*difference+s*f),
            b*SQRT2*(-s*difference+n*f),
            d*(mean-n*difference-s*f)), axis=-2)

    def apply(self, residual):
        return self.whiten(self.whiten(residual), transpose=True)

    def apply_columns(self, jacobian):
        return self.whiten_columns(self.whiten_columns(jacobian), transpose=True)

    def normal_and_gradient(self, jacobian, residual, point_weights):
        """Return J^T w L J and J^T w K(r)r; both unscaled by k/scale^2.

        residual is the current raw Gram residual, normally the base used
        to construct this block. The normal uses the frozen exact residual
        Hessian; the gradient always uses the actual supplied residual.
        External normalization and k/scale^2 match the R660 coarse API.
        """
        J = np.asarray(jacobian); dim = J.shape[-1]
        weights = np.asarray(point_weights)
        if np.any(weights <= 0):
            raise ValueError('Every original observation keeps a positive weight')
        BJ = self.whiten_columns(J)
        weighted_BJ = BJ*weights[..., None, None]
        gradient = primitive_gradient(residual, self.parameters)*weights[..., None]
        return (BJ.reshape(-1, dim).T@weighted_BJ.reshape(-1, dim),
                J.reshape(-1, dim).T@gradient.reshape(-1))

    def metadata(self):
        p = self.parameters
        return dict(p=p.p, epsilon=p.epsilon, scale=p.scale,
            hessian_block='L=T*Dh(E)T; half point Hessian=(k/scale^2)L',
            gradient='T*h(E)=R660 K(E)r; never L*r',
            minimum_eigenweight=self.minimum_eigenweight,
            maximum_eigenweight=self.maximum_eigenweight,
            eigenweight_coordinates='orthonormal Frobenius eigenbasis, not raw (e,f,g)',
            raw_L_minimum_eigenvalue_lower=self.minimum_eigenweight,
            raw_L_maximum_eigenvalue_upper=2*self.maximum_eigenweight,
            analytic_positive_floor=(p.epsilon/p.scale)**(p.p-2),
            divided_difference='positive k-point Gauss integral of hprime; exact polynomial degree 2k-2',
            square_root_factor='B=diag(sqrt(hprime+),sqrt(hdiv),sqrt(hprime-))*spectral_Frobenius_transform',
            half_gradient_and_normal_external_factor=p.k/(p.scale*p.scale),
            frobenius_cross_factor_already_inside_block=True,
            full_x_hessian_claimed=False, MM_majorant_claimed=bool(p.p == 2),
            numeric_evaluation_outward=False, permanent_scalar_arrays_per_point=5)


class NativeLinearization:
    """Complete-space bridge with the correct non-residual RHS for LSMR.

    A=sqrt(radial)*B*J_native. Virtual RHS v=sqrt(radial*orbit)*B^{-T}g0,
    where g0=T*h(E). Thus A^T v is the true unscaled half-gradient and
    A^T A the exact residual-Hessian pullback. Solve A d approximately -v.
    ||v||^2 is NOT the actual Phi. Read actual_trial during line search.
    """
    def __init__(self, original, x, radial_weights, parameters, *, spectral_module):
        from scipy.sparse.linalg import LinearOperator
        self.original, self.x = original, np.asarray(x).copy()
        self.spectral_module, self.parameters = spectral_module, parameters
        self.radial = np.asarray(radial_weights).copy()
        if self.radial.shape != (original.P,) or np.any(self.radial <= 0):
            raise ValueError('Need positive weight on every original stage')
        native = original.residual(self.x).reshape(original.P, original.N, 3)
        raw = original.unweight(native).reshape(native.shape)
        self.blocks = HessianBlocks(raw, parameters)
        self.sqrt_radial = np.sqrt(self.radial)[:, None, None]
        sqrt_orbit = np.sqrt(original.multiplicity)[None, :, None]
        self.residual = (self.sqrt_radial*sqrt_orbit*self.blocks.inverse_transpose(
            primitive_gradient(raw, parameters))).ravel()
        self.shape = (original.P*original.N*3, original.free_size)
        self.operator = LinearOperator(self.shape, matvec=self.matvec, rmatvec=self.rmatvec, dtype=float)
        self.gradient = self.rmatvec(self.residual)
        self.true_gradient_factor = 2*parameters.k/(parameters.scale**2*float(self.radial.sum()*original.full_N))
        self.base_statistics = spectral_module.statistics(raw, self.radial, original.multiplicity, parameters)

    def matvec(self, direction):
        value = self.original.jvp(self.x, direction).reshape(self.original.P, self.original.N, 3)
        return (self.sqrt_radial*self.blocks.whiten(value)).ravel()

    def rmatvec(self, value):
        value = np.asarray(value).reshape(self.original.P, self.original.N, 3)
        cotangent = self.blocks.whiten(self.sqrt_radial*value, transpose=True)
        return self.original.vjp(self.x, cotangent)

    def normal(self, direction): return self.rmatvec(self.matvec(direction))

    def actual_trial(self, candidate):
        raw = self.original.unweight(self.original.residual(candidate)).reshape(self.original.P, self.original.N, 3)
        return self.spectral_module.statistics(raw, self.radial, self.original.multiplicity, self.parameters)

    def metadata(self):
        return dict(blocks=self.blocks.metadata(), native_rows=self.shape[0], original_free_variables=self.shape[1],
            true_normalized_gradient_factor=self.true_gradient_factor,
            normal='J_native^T diag(radial) L J_native; external k/(scale^2*C0)',
            virtual_rhs='sqrt(radial*orbit) B^{-T} T*h(E); NOT sqrt(radial)*B*r_native',
            gradient='A^T virtual_rhs; multiply true_normalized_gradient_factor for actual Phi',
            row_sqrt_orbit_applied_exactly_once_each_side=True,
            virtual_rhs_squared_norm_is_actual_objective=False,
            additional_cross_sqrt2_weight_needed=False,
            actual_phi_and_original_Jw_max_required_in_line_search=True)

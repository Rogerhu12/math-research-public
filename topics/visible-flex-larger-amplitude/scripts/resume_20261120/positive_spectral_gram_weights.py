#!/usr/bin/env python3
"""Positive 3x3 Gram residual blocks for a smoothed even spectral Lp.

For E=[[e,f],[f,g]], p=2k, freeze W=((E0^2+eps^2 I)/scale^2)^(k-1).
The exact positive quadratic is tr(W E^2)=r^T K r, r=(e,f,g), with
K=[[u,v,0],[v,u+w,v],[0,v,w]] and W=[[u,v],[v,w]].
All original residual rows remain present. Frozen weights are not an MM
majorant for p>2; accept against the actual fixed-epsilon spectral target.
"""
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Parameters:
    p: int = 8
    epsilon: float = .001
    scale: float = .05

    def __post_init__(self):
        if self.p < 2 or self.p % 2 or self.epsilon <= 0 or self.scale <= 0:
            raise ValueError('Use even p>=2 and positive epsilon/scale')

    @property
    def k(self): return self.p//2

    def as_dict(self):
        return dict(p=self.p, epsilon=self.epsilon, scale=self.scale,
                    target='sum normalized positive weights * tr(((E^2+epsilon^2 I)/scale^2)^(p/2))',
                    epsilon_and_scale_fixed_during_line_search=True)


def eigenvalues(residual):
    e, f, g = residual[..., 0], residual[..., 1], residual[..., 2]
    gap = np.sqrt((e-g)**2+4*f*f)
    return .5*(e+g+gap), .5*(e+g-gap), gap


def point_loss(residual, parameters):
    plus, minus, _ = eigenvalues(np.asarray(residual))
    a = (plus*plus+parameters.epsilon**2)/parameters.scale**2
    b = (minus*minus+parameters.epsilon**2)/parameters.scale**2
    return a**parameters.k+b**parameters.k


class Blocks:
    """A positive residual block on every original (stage,quarter-angle)."""
    def __init__(self, residual, parameters=Parameters()):
        self.parameters = parameters
        residual = np.asarray(residual)
        if residual.shape[-1] != 3 or np.iscomplexobj(residual):
            raise ValueError('Freeze weights at a real complete Gram state')
        plus, minus, gap = eigenvalues(residual)
        p = parameters
        wp = ((plus*plus+p.epsilon**2)/p.scale**2)**(p.k-1)
        wm = ((minus*minus+p.epsilon**2)/p.scale**2)**(p.k-1)
        average, half_difference = .5*(wp+wm), .5*(wp-wm)
        axis = np.divide(residual[..., 0]-residual[..., 2], gap, out=np.zeros_like(gap), where=gap != 0)
        offaxis = np.divide(2*residual[..., 1], gap, out=np.zeros_like(gap), where=gap != 0)
        self.u = average+half_difference*axis
        self.v = half_difference*offaxis
        self.w = average-half_difference*axis
        self.minimum_eigenweight = float(min(wp.min(), wm.min()))
        self.maximum_eigenweight = float(max(wp.max(), wm.max()))
        if not self.minimum_eigenweight > 0 or not np.isfinite(self.maximum_eigenweight):
            raise ValueError('Finite arithmetic lost a strictly positive block weight')
        self._cholesky = None

    def apply(self, residual):
        """K times the raw/native-orbit three-vector, without radial weights."""
        r = np.asarray(residual); e, f, g = r[..., 0], r[..., 1], r[..., 2]
        return np.stack((self.u*e+self.v*f,
            self.v*e+(self.u+self.w)*f+self.v*g,
            self.v*f+self.w*g), axis=-1)

    def apply_columns(self, jacobian):
        """K times arbitrary original/coarse Jacobian columns (...,3,d)."""
        J = np.asarray(jacobian); e, f, g = J[..., 0, :], J[..., 1, :], J[..., 2, :]
        u, v, w = self.u[..., None], self.v[..., None], self.w[..., None]
        return np.stack((u*e+v*f, v*e+(u+w)*f+v*g, v*f+w*g), axis=-2)

    def cholesky(self):
        """K=L L^T. No clipping or dropping small original residual rows."""
        if self._cholesky is None:
            a = np.sqrt(self.u)
            b = self.v/a
            cc = self.u+self.w-b*b
            if np.any(cc <= 0):
                raise ArithmeticError('The declared epsilon is too small for stable block factorization')
            c = np.sqrt(cc); d = self.v/c
            ee = self.w-d*d
            if np.any(ee <= 0):
                raise ArithmeticError('The declared epsilon is too small for stable block factorization')
            self._cholesky = a, b, c, d, np.sqrt(ee)
        return self._cholesky

    def whiten(self, residual, transpose=False):
        """Forward is L^T r; transpose is L r, so forward^T forward=K."""
        a, b, c, d, h = self.cholesky()
        r = np.asarray(residual); e, f, g = r[..., 0], r[..., 1], r[..., 2]
        if transpose:
            return np.stack((a*e, b*e+c*f, d*f+h*g), axis=-1)
        return np.stack((a*e+b*f, c*f+d*g, h*g), axis=-1)

    def contractions(self, residual, first, second, point_weights):
        """Stream two physical families, e.g. radial xi / xi' columns.

        The final two axes are (angle,three residuals). Returns five stage
        moments before assembly with any radial basis. point_weights has
        shape (...,angle) and includes radial and/or angular weights once.
        """
        Kfirst, Ksecond, Kr = self.apply(first), self.apply(second), self.apply(residual)
        reduce = lambda x: np.sum(np.sum(x, axis=-1)*point_weights, axis=-1)
        return (reduce(first*Kfirst), reduce(first*Ksecond), reduce(second*Ksecond),
                reduce(first*Kr), reduce(second*Kr))

    def normal_and_gradient(self, jacobian, residual, point_weights):
        """Exact J^T diag(point_weights) K J and J^T ... K r assembly.

        Jacobian columns may span the original complete affine space or
        any existing coarse space. No column/row truncation is performed.
        """
        J = np.asarray(jacobian); dim = J.shape[-1]
        weighted_J = self.apply_columns(J)*np.asarray(point_weights)[..., None, None]
        weighted_r = self.apply(residual)*np.asarray(point_weights)[..., None]
        return J.reshape(-1, dim).T@weighted_J.reshape(-1, dim), J.reshape(-1, dim).T@weighted_r.reshape(-1)

    def metadata(self):
        p = self.parameters
        return dict(**p.as_dict(), minimum_eigenweight=self.minimum_eigenweight,
            maximum_eigenweight=self.maximum_eigenweight,
            analytic_positive_floor=(p.epsilon*p.epsilon/(p.scale*p.scale))**(p.k-1),
            original_component_order=['ss', 'sphi', 'phiphi'],
            frobenius_cross_factor_is_inside_K=True,
            quadratic_is_MM_upper_bound=bool(p.p == 2),
            true_unnormalized_gradient_factor=2*p.k/(p.scale*p.scale))


def statistics(residual, radial_weights, multiplicity, parameters=Parameters()):
    """Actual fixed-parameter spectral objective and original Jw/max.

    The mathematical inequalities are exact; these displayed numbers use
    ordinary binary arithmetic and are not outward numerical certificates.
    """
    r = np.asarray(residual); radial = np.asarray(radial_weights); orbit = np.asarray(multiplicity)
    if np.any(radial <= 0) or np.any(orbit <= 0):
        raise ValueError('Every original row orbit must retain positive weight')
    normalizer = float(radial.sum()*orbit.sum())
    phi = float(radial@(point_loss(r, parameters)@orbit)/normalizer)
    w_min = float(radial.min()*orbit.min()/normalizer)
    plus, minus, _ = eigenvalues(r)
    maximum = float(np.maximum(np.abs(plus), np.abs(minus)).max())
    q = r[..., 0]**2+2*r[..., 1]**2+r[..., 2]**2
    norm_lower = np.sqrt(max(0., parameters.scale**2*(phi/2)**(1/parameters.k)-parameters.epsilon**2))
    norm_upper = np.sqrt(max(0., parameters.scale**2*(phi/w_min)**(1/parameters.k)-parameters.epsilon**2))
    return dict(**parameters.as_dict(), phi_normalized=phi,
        phi_zero=2*(parameters.epsilon**2/parameters.scale**2)**parameters.k,
        positive_weight_sum=1., minimum_normalized_orbit_weight=w_min,
        normalization=normalizer, smoothed_spectral_lp=parameters.scale*phi**(1/parameters.p),
        finite_max_formula_lower=float(norm_lower), finite_max_formula_upper=float(norm_upper),
        formula_evaluation_outward=False, max_gram=maximum,
        original_weighted_sse=float(radial@(q@orbit)),
        original_weighted_mean_sse=float(radial@(q@orbit)/normalizer),
        all_original_rows_retained=True)


class NativeLinearization:
    """Full original operator bridge, preserving its native sqrt-orbit rows.

    .operator is the weighted LinearOperator for LSMR/LSQR.
    .residual is the consistently weighted base residual.
    .gradient is J^T(radial * K)r in native orbit convention.
    .true_gradient_factor rescales it to the actual normalized Phi gradient.
    Existing full-space preconditioners/coarse columns can wrap this bridge.
    """
    def __init__(self, original, x, radial_weights, parameters=Parameters()):
        from scipy.sparse.linalg import LinearOperator
        self.original, self.x = original, np.asarray(x).copy()
        self.radial = np.asarray(radial_weights).copy()
        if self.radial.shape != (original.P,) or np.any(self.radial <= 0):
            raise ValueError('Need one positive weight for every original stage')
        native = original.residual(self.x).reshape(original.P, original.N, 3)
        raw = original.unweight(native).reshape(native.shape)
        self.blocks = Blocks(raw, parameters)
        self.sqrt_radial = np.sqrt(self.radial)[:, None, None]
        self.residual = (self.sqrt_radial*self.blocks.whiten(native)).ravel()
        self.shape = (original.P*original.N*3, original.free_size)
        self.operator = LinearOperator(self.shape, matvec=self.matvec, rmatvec=self.rmatvec, dtype=float)
        self.gradient = self.rmatvec(self.residual)
        self.true_gradient_factor = 2*parameters.k/(parameters.scale**2*float(self.radial.sum()*original.full_N))
        self.base_statistics = statistics(raw, self.radial, original.multiplicity, parameters)

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
        return statistics(raw, self.radial, self.original.multiplicity, self.blocks.parameters)

    def metadata(self):
        return dict(blocks=self.blocks.metadata(), native_rows=self.shape[0], original_free_variables=self.shape[1],
            minimum_normalized_orbit_weight=self.base_statistics['minimum_normalized_orbit_weight'],
            true_normalized_gradient_factor=self.true_gradient_factor,
            normal='J_native^T diag(radial) K J_native',
            gradient='J_native^T diag(radial) K r_native; multiply true_normalized_gradient_factor for actual Phi',
            row_sqrt_orbit_applied_exactly_once_each_side=True,
            additional_cross_sqrt2_weight_needed=False,
            model_target_and_affine_space_unchanged=True,
            actual_phi_and_original_Jw_max_required_in_line_search=True)

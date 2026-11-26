#!/usr/bin/env python3
"""R684: NEW rotational-metric design using material-angle Gram averages.

The original physical field and all free coordinates stay unchanged.
Only the design objective changes: two diagonal material-angle means
provide E(s), C(s), while every angular fluctuation/cross row remains.
This is NOT fixed-old-g refinement and does not freeze a final metric.

Material theta=Theta(phi) has density rho>0. The material variant uses
omega_j=m_j*rho_j/sum(m*rho), including its core derivative. The separate
physical variant uses FIXED omega_j=m_j/sum(m); it does not claim to be
a material Haar average, but still defines a legitimate invariant metric.
Exact parity makes the full-circle cross mean zero even with rho weights;
never take a positive quarter-domain mean of that odd cross component.

There is no scientific execution on import or numerical acceptance claim.
"""
import numpy as np


class MeanMetricTransform:
    """Full derivative/transpose of the finite material-mean metric map.

    raw[...,j,:]=(e,f,d) is relative Gram in the ORIGINAL normalization.
    multiplicity is the exact orbit count and density is actual rho_j.
    Keeping sum(m*rho) in every formula also pays finite normalization.
    """
    def __init__(self, raw, multiplicity, density, averaging="material"):
        self.raw = np.asarray(raw)
        m = np.asarray(multiplicity, dtype=float)
        rho = np.asarray(density)
        if (self.raw.ndim < 2 or self.raw.shape[-1] != 3
                or m.shape != (self.raw.shape[-2],) or rho.shape != m.shape
                or not np.isfinite(m).all() or np.any(m <= 0)
                or not np.isfinite(rho).all() or np.any(rho.real <= 0)
                or not np.isfinite(self.raw).all()):
            raise ValueError('Need all finite Gram rows, positive multiplicities and actual positive rho')
        if averaging not in ("material", "physical"):
            raise ValueError("Explicitly choose material or physical averaging")
        self.averaging = averaging
        self.multiplicity, self.density = m, rho
        self.mass = np.sum(m*rho) if averaging == "material" else np.sum(m)
        self.density_factor = m/self.mass if averaging == "material" else np.zeros_like(m)
        self.omega = m*rho/self.mass if averaging == "material" else m/self.mass
        self.mean_e = np.sum(self.raw[..., 0]*self.omega, axis=-1)
        self.mean_d = np.sum(self.raw[..., 2]*self.omega, axis=-1)
        self.radial, self.angular = 1+self.mean_e, 1+self.mean_d
        if (np.any(self.radial.real <= 0) or np.any(self.angular.real <= 0)
                or not np.isfinite(self.radial).all()
                or not np.isfinite(self.angular).all()):
            raise ValueError('The new diagonal mean metric is not positive')
        self.cross_scale = np.sqrt(self.radial*self.angular)
        A, C, S = self.radial[..., None], self.angular[..., None], self.cross_scale[..., None]
        self.result = np.stack(((1+self.raw[..., 0])/A-1,
            self.raw[..., 1]/S, (1+self.raw[..., 2])/C-1), axis=-1)

    def apply(self, direction, density_direction=None):
        """Derivative in BOTH raw Gram and rho, including normalizer chain."""
        h = np.asarray(direction)
        if h.shape != self.raw.shape:
            raise ValueError('All original angle/component directions are required')
        drho = np.zeros_like(self.density) if density_direction is None else np.asarray(density_direction)
        if drho.shape != self.density.shape:
            raise ValueError('The actual core-induced density direction is required')
        dm = np.sum(self.multiplicity*drho) if self.averaging == "material" else 0.
        domega = self.density_factor*drho-self.omega*dm/self.mass
        de = np.sum(h[..., 0]*self.omega+self.raw[..., 0]*domega, axis=-1)
        dd = np.sum(h[..., 2]*self.omega+self.raw[..., 2]*domega, axis=-1)
        A, C, S = self.radial[..., None], self.angular[..., None], self.cross_scale[..., None]
        qe = (h[..., 0]-(1+self.result[..., 0])*de[..., None])/A
        qd = (h[..., 2]-(1+self.result[..., 2])*dd[..., None])/C
        qf = (h[..., 1]/S-.5*self.result[..., 1]
            *(de[..., None]/A+dd[..., None]/C))
        return np.stack((qe, qf, qd), axis=-1)

    def transpose(self, cotangent):
        """Return (raw-Gram cotangent, stagewise density cotangent).

        Ordinary bilinear Euclidean transpose, with no implicit row
        weights. Since one rho is shared by all stages, callers must SUM
        the second output over the stage axis before its core pullback.
        """
        y = np.asarray(cotangent)
        if y.shape != self.raw.shape:
            raise ValueError('All output angle/component cotangents are required')
        A, C, S = self.radial[..., None], self.angular[..., None], self.cross_scale[..., None]
        shared = .5*np.sum(y[..., 1]*self.result[..., 1], axis=-1)
        ce = (np.sum(y[..., 0]*(1+self.result[..., 0]), axis=-1)+shared)/self.radial
        cd = (np.sum(y[..., 2]*(1+self.result[..., 2]), axis=-1)+shared)/self.angular
        qe = y[..., 0]/A-ce[..., None]*self.omega
        qd = y[..., 2]/C-cd[..., None]*self.omega
        qf = y[..., 1]/S
        qrho = -self.density_factor*(
            ce[..., None]*(self.raw[..., 0]-self.mean_e[..., None])
            + cd[..., None]*(self.raw[..., 2]-self.mean_d[..., None]))
        return np.stack((qe, qf, qd), axis=-1), qrho


class MeanMetricOperator:
    """Complete J/J* adapter retaining every original free core coefficient.

    Geometry and affine conditions remain on original_operator. Consumers
    assembling old J directly from Fs/Fphi must be adapted separately.
    Final refinement must instead use frozen continuum E_star,C_star.
    """
    def __init__(self, original_operator, averaging="material"):
        if averaging not in ("material", "physical"):
            raise ValueError("Explicitly choose material or physical averaging")
        self.averaging = averaging
        self.original_operator = original_operator
        self._design_x = self._design_transform = None

    def __getattr__(self, name):
        return getattr(self.original_operator, name)

    def _state(self, x):
        x = np.asarray(x)
        if (self._design_x is not None and x.dtype == self._design_x.dtype
                and x.shape == self._design_x.shape
                and np.array_equal(x, self._design_x)):
            return self._design_transform
        raw = self.original_operator.raw_residual(x)
        rho = self.original_operator.prepare(x).rho
        return MeanMetricTransform(raw, self.multiplicity, rho, self.averaging)

    def set_base(self, x):
        record = self.original_operator.set_base(x)
        self._design_x = np.array(x, copy=True)
        self._design_x.setflags(write=False)
        self._design_transform = MeanMetricTransform(
            self.original_operator.raw_residual(x), self.multiplicity,
            self.original_operator.prepare(x).rho, self.averaging)
        return dict(record, objective='R684 moving '+self.averaging+'-angle mean metric design',
                    fixed_old_metric=False, original_physical_field_unchanged=True)

    def clear_base(self):
        self.original_operator.clear_base()
        self._design_x = self._design_transform = None

    def raw_residual(self, x):
        return self._state(x).result.copy()

    def residual(self, x):
        return self.raw_residual(x)*self.sqrt_multiplicity[None, :, None]

    def jvp(self, x, direction):
        old = self.original_operator
        raw_jvp = old.unweight(old.jvp(x, direction))
        _, _, dc = old.unpack(direction, tangent=True)
        drho = old.cos[:, 1:]@(old.qfreq*dc)
        return self._state(x).apply(raw_jvp, drho)*self.sqrt_multiplicity[None, :, None]

    def vjp(self, x, weights):
        old = self.original_operator
        y = np.asarray(weights).reshape((self.P, self.N, 3))
        raw_cotangent = y*self.sqrt_multiplicity[None, :, None]
        old_raw, rho_cotangent = self._state(x).transpose(raw_cotangent)
        old_cotangent = old_raw/self.sqrt_multiplicity[None, :, None]
        result = old.vjp(x, old_cotangent)
        gc = old.qfreq*(old.cos[:, 1:].T@np.sum(rho_cotangent, axis=0))
        # Original packed block is core[K:M], then core acceleration,
        # every interior jet, and cap height. The mean weights add only
        # this direct rho-to-core branch; old.vjp already pays all other
        # rho/Theta/analytic-lift/physical-field dependencies.
        result[:old.M-old.K] += gc[old.K:]
        return result

    def observation_metadata(self):
        record = self.original_operator.observation_metadata()
        return dict(record, objective='R684 moving '+self.averaging+'-angle mean metric design',
                    fixed_old_metric=False, fixed_final_metric=False,
                    every_angular_fluctuation_and_cross_row_retained=True,
                    material_density_weight_derivative_retained=self.averaging == "material",
                    explicit_averaging_variant=self.averaging,
                    omitted_scalar_constraints='The prescribed old radial/azimuthal means are explicitly released during NEW metric design only')

#!/usr/bin/env python3
"""R53: unit-speed material-curvature flattening of a true support core.

This source was preserved while the execution environment was unavailable.
It has NOT yet passed an execution, finite-difference, or BVP check.
The homotopy is a core design change, not fixed-metric BVP convergence.

Factory: make_factory(reference_class, settings) -> Core(q, corrections, base_mode).
At homotopy=0 the factory returns the original reference instance literally.
Only the default field provider assumes finite support Fourier coefficients.
"""
import math
import numpy as np
from numpy.polynomial import Polynomial

_STEP = Polynomial([0., 0., 0., 0., 0., 126., -420., 540., -315., 70.])
_STEP_INT = _STEP.integ()


def _xyz(z):
    z = np.asarray(z)
    return np.stack((z.real, z.imag, np.zeros_like(z.real)), axis=-1)


def _support_fields(original, theta):
    """True fixed-material derivatives for h=1+sum a_j cos(m_j phi)."""
    theta = np.asarray(theta, dtype=float).reshape(-1)
    g = original.evaluate(theta)
    phi = np.asarray(g["phi"], dtype=float).reshape(-1)
    kappa = np.asarray(g["kappa"], dtype=float).reshape(-1)
    rho = 1. / kappa
    m = np.asarray(original.frequencies, dtype=float).reshape(-1)
    a = np.asarray(original.coefficients, dtype=float).reshape(-1)
    angle = m[:, None] * phi[None, :]
    co, si = np.cos(angle), np.sin(angle)
    weight = 1. - m * m
    rho_phi = -(m * weight * a) @ si
    rho_phiphi = -(m * m * weight * a) @ co
    phi_p = -(weight / m)[:, None] * si / rho[None, :]
    kappa_p = -(weight[:, None] * co +
                rho_phi[None, :] * phi_p) / rho[None, :]**2
    return dict(phi=phi, kappa=kappa, phi_p=phi_p, kappa_p=kappa_p,
                kappa_u=-rho_phi / rho**3,
                kappa_uu=-rho_phiphi / rho**4 + 3. * rho_phi**2 / rho**5,
                original_geometry=g)


def _support_curvature_derivative_bounds(original):
    """Bounds for material kappa_u and kappa_uu, not normal-angle derivatives."""
    m = np.asarray(original.frequencies, dtype=float)
    a = np.asarray(original.coefficients, dtype=float)
    r = float(original.rho_lower)
    d1 = float(np.sum(np.abs(m * (1. - m * m) * a)))
    d2 = float(np.sum(np.abs(m * m * (1. - m * m) * a)))
    return d1 / r**3, d2 / r**4 + 3. * d1*d1 / r**5


def parameter_jets(core, theta):
    """Return dF/dp, dFt/dp, dFtt/dp in original physical parameter units."""
    if hasattr(core, "jet_parameter_derivatives"):
        return core.jet_parameter_derivatives(theta)
    f = _support_fields(core, theta)
    nu = np.exp(1j * f["phi"])[None, :]
    return (core.parameter_derivatives(np.asarray(theta, float).reshape(-1)),
            _xyz(-nu * f["phi_p"]),
            _xyz(-nu * (f["kappa_p"] + 1j*f["kappa"][None, :]*f["phi_p"])))


class MaterialFlattenedSupportCore:
    def __init__(self, original, *, homotopy, halfwidth=.20, transition=.25,
                 target_curvature=.20, curvature_blend=0., arc_nodes=1024,
                 quadrature_order=12, integration_cells=64, transition_cells=24,
                 _fields_provider=None, _curvature_derivative_bounds_provider=None,
                 _parameter_count=None, _parameter_values=None):
        self.original = original
        self.base_mode = int(original.base_mode)
        if self.base_mode < 3:
            raise ValueError("R53 adapter requires base_mode >= 3")
        self.period = 2.*math.pi/self.base_mode
        self.halfperiod = self.period/2.
        self.homotopy = float(homotopy)
        self.curvature_blend = float(curvature_blend)
        self.halfwidth, self.transition = float(halfwidth), float(transition)
        if not (0. < self.homotopy <= 1. and 0. <= self.curvature_blend <= 1.):
            raise ValueError("Need homotopy in (0,1] and curvature_blend in [0,1]")
        if not (0. < self.halfwidth and 0. < self.transition and
                self.halfwidth+self.transition < self.halfperiod):
            raise ValueError("Material arc plus transition must fit in half a sector")
        self.target_curvature = float(target_curvature)
        if not (np.isfinite(self.target_curvature) and self.target_curvature > 0.):
            raise ValueError("Target curvature must be finite and positive")
        self.arc_nodes = max(128, int(arc_nodes))
        self.quadrature_order = max(4, int(quadrature_order))
        self.integration_cells = max(8, int(integration_cells))
        self.transition_cells = max(4, int(transition_cells))
        self._fields_provider = _fields_provider or _support_fields
        if _fields_provider is None:
            self._bound_provider = (_curvature_derivative_bounds_provider or
                                    _support_curvature_derivative_bounds)
        else:
            self._bound_provider = _curvature_derivative_bounds_provider
        if _parameter_count is None:
            _parameter_count = len(np.asarray(original.coefficients).reshape(-1))
        self._p = int(_parameter_count)
        if self._p < 1:
            raise ValueError("At least one physical core parameter is required")
        if _parameter_values is None:
            _parameter_values = np.asarray(original.coefficients, float)
        self.coefficients = np.asarray(_parameter_values, float).reshape(-1)
        if len(self.coefficients) != self._p:
            raise ValueError("Physical parameter values and provider dimension disagree")
        self.support_amplitude = float(self.coefficients[0])
        self.q = self.support_amplitude
        self.corrections = tuple(float(x) for x in self.coefficients[1:])
        # Labels only for a generic provider; no generic formula reads these.
        self.frequencies = self.base_mode*np.arange(1, self._p+1)
        self.a0 = 1.
        self._gx, self._gw = np.polynomial.legendre.leggauss(self.quadrature_order)

        center = self._fields(np.array([self.halfperiod]))
        self.k = ((1.-self.curvature_blend)*float(center["kappa"][0]) +
                  self.curvature_blend*self.target_curvature)
        self._kp = (1.-self.curvature_blend)*center["kappa_p"][:, 0]
        if self.k <= 0.:
            raise FloatingPointError("Nonpositive target circle curvature")
        S, b = self.halfwidth, self.transition
        edge = self._fields(np.array([self.halfperiod+S]))
        omega_S = np.r_[self.k*S-(float(edge["phi"][0])-self.halfperiod),
                        self._kp*S-edge["phi_p"][:, 0]]
        self._transition_grid = np.linspace(S, S+b, self.transition_cells+1)
        increments = self._weighted_integral(
            self._transition_grid[:-1], self._transition_grid[1:])
        self._omega_grid = np.vstack(
            (omega_S, omega_S[None, :]+np.cumsum(increments, axis=0)))
        self._omega_end = self._omega_grid[-1]
        self._beta_all = -self._omega_end/(self.halfperiod-S-b/2.)
        self.beta = float(self._beta_all[0])
        self._set_curvature_guard()

        breaks = np.r_[np.linspace(0., self.period, self.integration_cells+1),
                       self.halfperiod-S-b, self.halfperiod-S, self.halfperiod,
                       self.halfperiod+S, self.halfperiod+S+b]
        self._integration_grid = np.unique(breaks)
        increments = self._position_integral(
            self._integration_grid[:-1], self._integration_grid[1:])
        self._position_grid = np.vstack(
            (np.zeros(self._p+1, dtype=complex), np.cumsum(increments, axis=0)))
        origin = self._position_grid[-1]/np.expm1(1j*self.period)
        self.reflection_roundoff = float(np.max(np.abs(origin.imag)))
        self._origin = origin.real.astype(complex)
        self._cache_theta = None
        self._cache_jets = None

    def _fields(self, theta):
        theta = np.asarray(theta, dtype=float).reshape(-1)
        f = self._fields_provider(self.original, theta)
        for key in ("phi", "kappa", "kappa_u", "kappa_uu"):
            f[key] = np.asarray(f[key], float).reshape(-1)
            if f[key].shape != theta.shape or not np.all(np.isfinite(f[key])):
                raise FloatingPointError("Invalid old-core field: "+key)
        for key in ("phi_p", "kappa_p"):
            f[key] = np.asarray(f[key], float)
            if f[key].shape != (self._p, len(theta)) or not np.all(np.isfinite(f[key])):
                raise FloatingPointError("Invalid old-core parameter field: "+key)
        return f

    def _window(self, theta):
        x = np.asarray(theta, float).reshape(-1)-self.halfperiod
        z, sign = np.abs(x), np.sign(x)
        W, W1, W2 = np.ones_like(z), np.zeros_like(z), np.zeros_like(z)
        C = np.full_like(z, self.halfwidth+self.transition/2.)
        inner = z <= self.halfwidth
        trans = (z > self.halfwidth) & (z < self.halfwidth+self.transition)
        W[inner], C[inner] = 0., z[inner]
        t = (z[trans]-self.halfwidth)/self.transition
        small = np.minimum(t, 1.-t)
        step_small = _STEP(small)
        W[trans] = np.where(t <= .5, step_small, 1.-step_small)
        W1[trans] = sign[trans]*630.*t**4*(1.-t)**4/self.transition
        W2[trans] = 2520.*t**3*(1.-t)**3*(1.-2.*t)/self.transition**2
        primitive = np.where(t <= .5, t-_STEP_INT(t),
                             .5-_STEP_INT(1.-t))
        C[trans] = self.halfwidth+self.transition*primitive
        return x, W, W1, W2, sign*C

    def _weighted_integral(self, a, b):
        a, b = np.asarray(a, float).reshape(-1), np.asarray(b, float).reshape(-1)
        z = (a[:, None]+b[:, None])/2. + (b-a)[:, None]*self._gx[None, :]/2.
        u = self.halfperiod+z.reshape(-1)
        f = self._fields(u)
        chi = 1.-self._window(u)[1]
        values = np.column_stack((self.k-f["kappa"],
                                  (self._kp[:, None]-f["kappa_p"]).T))
        values *= chi[:, None]
        values = values.reshape(len(a), self.quadrature_order, self._p+1)
        return np.einsum("q,nqp->np", self._gw, values)*(b-a)[:, None]/2.

    def _omega(self, theta):
        x = np.asarray(theta, float).reshape(-1)-self.halfperiod
        z, sign = np.abs(x), np.sign(x)
        result = np.empty((len(z), self._p+1), dtype=float)
        inner = z <= self.halfwidth
        trans = (z > self.halfwidth) & (z < self.halfwidth+self.transition)
        outer = ~(inner | trans)
        if np.any(inner):
            zz = z[inner]
            f = self._fields(self.halfperiod+zz)
            result[inner, 0] = self.k*zz-(f["phi"]-self.halfperiod)
            result[inner, 1:] = zz[:, None]*self._kp[None, :]-f["phi_p"].T
        if np.any(trans):
            zz = z[trans]
            index = np.searchsorted(self._transition_grid, zz, side="right")-1
            index = np.clip(index, 0, self.transition_cells-1)
            result[trans] = (self._omega_grid[index] +
                            self._weighted_integral(self._transition_grid[index], zz))
        result[outer] = self._omega_end
        return result*sign[:, None]

    def _phase_fields(self, theta):
        theta = np.asarray(theta, float).reshape(-1)
        f = self._fields(theta)
        x, W, W1, W2, C = self._window(theta)
        chi, lam = 1.-W, self.homotopy
        correction = self._omega(theta)+(x-C)[:, None]*self._beta_all[None, :]
        phi = f["phi"]+lam*correction[:, 0]
        phi_p = f["phi_p"]+lam*correction[:, 1:].T
        kappa = f["kappa"]+lam*(chi*(self.k-f["kappa"])+self.beta*W)
        kappa_p = f["kappa_p"]+lam*(
            chi[None, :]*(self._kp[:, None]-f["kappa_p"]) +
            W[None, :]*self._beta_all[1:, None])
        gap = f["kappa"]-self.k+self.beta
        kappa_u = (1.-lam*chi)*f["kappa_u"]+lam*W1*gap
        kappa_uu = ((1.-lam*chi)*f["kappa_uu"] +
                    2.*lam*W1*f["kappa_u"]+lam*W2*gap)
        return dict(phi=phi, phi_p=phi_p, kappa=kappa, kappa_p=kappa_p,
                    kappa_u=kappa_u, kappa_uu=kappa_uu)

    def _set_curvature_guard(self):
        a = 1./float(self.original.rho_upper)
        b = 1./float(self.original.rho_lower)
        if not (0. < a <= b and np.isfinite(b)):
            raise FloatingPointError("Original provider lacks valid positive rho bounds")
        lam, floor = self.homotopy, 1.e-5
        lower = (1.-lam)*a+lam*min(self.k, a+self.beta)
        upper = (1.-lam)*b+lam*max(self.k, b+self.beta)
        details = dict(method="R53-convex-mixture", lower=lower, upper=upper)
        if lower <= floor:
            if self._bound_provider is None:
                raise FloatingPointError(
                    "Coarse R53 guard insufficient; true material curvature derivative bounds required")
            K1, K2 = (float(v) for v in self._bound_provider(self.original))
            if min(K1, K2) < 0. or not np.isfinite(K1+K2):
                raise FloatingPointError("Invalid true material curvature derivative bounds")
            D1 = 630./(256.*self.transition)
            D2 = 2520./(64.*self.transition**2)
            gap = max(abs(a-self.k+self.beta), abs(b-self.k+self.beta))
            second_bound = K2+2.*lam*D1*K1+lam*D2*gap
            for nodes in (512, 1024, 2048, 4096, 8192, 16384, 32768):
                theta = self.period*np.arange(nodes)/nodes
                values = self._phase_fields(theta)["kappa"]
                slack = (second_bound*(self.period/nodes)**2/8. +
                         1.e-12*(1.+b+abs(self.beta)+self.k))
                improved_lower = max(lower, float(values.min())-slack)
                improved_upper = min(upper, float(values.max())+slack)
                details = dict(method="R53-periodic-interpolation", nodes=nodes,
                               lower=improved_lower, upper=improved_upper,
                               second_derivative_bound=second_bound, slack=slack)
                if improved_lower > floor:
                    lower, upper = improved_lower, improved_upper
                    break
                if float(values.min()) <= floor:
                    raise FloatingPointError("R53 curvature sample crossed physical floor")
            else:
                raise FloatingPointError("R53 curvature positivity not resolved at node ceiling")
        self.curvature_lower_bound, self.curvature_upper_bound = lower, upper
        self.rho_lower, self.rho_upper = 1./upper, 1./lower
        self.curvature_guard = details

    def _position_integral(self, a, b):
        a, b = np.asarray(a, float).reshape(-1), np.asarray(b, float).reshape(-1)
        theta = (a[:, None]+b[:, None])/2. + (b-a)[:, None]*self._gx[None, :]/2.
        f = self._phase_fields(theta.reshape(-1))
        nu = np.exp(1j*f["phi"])
        values = np.column_stack((1j*nu, -nu[:, None]*f["phi_p"].T))
        values = values.reshape(len(a), self.quadrature_order, self._p+1)
        return np.einsum("q,nqp->np", self._gw, values)*(b-a)[:, None]/2.

    def evaluate(self, theta):
        theta = np.asarray(theta, float).reshape(-1)
        sector = np.floor(theta/self.period)
        local = theta-sector*self.period
        f = self._phase_fields(local)
        index = np.searchsorted(self._integration_grid, local, side="right")-1
        index = np.clip(index, 0, len(self._integration_grid)-2)
        integral = (self._position_grid[index] +
                    self._position_integral(self._integration_grid[index], local))
        rotation = np.exp(1j*sector*self.period)
        z = (self._origin[None, :]+integral)*rotation[:, None]
        phi = f["phi"]+sector*self.period
        nu = np.exp(1j*phi)
        self._cache_theta = theta.copy()
        self._cache_jets = (
            _xyz(z[:, 1:].T),
            _xyz(-nu[None, :]*f["phi_p"]),
            _xyz(-nu[None, :]*(f["kappa_p"] +
                 1j*f["kappa"][None, :]*f["phi_p"])))
        return dict(F=_xyz(z[:, 0]), Ft=_xyz(1j*nu),
                    Ftt=_xyz(-f["kappa"]*nu), phi=phi, kappa=f["kappa"],
                    kappa_u=f["kappa_u"], kappa_uu=f["kappa_uu"],
                    arc_residual=np.zeros_like(theta), arc_iterations=0)

    def jet_parameter_derivatives(self, theta):
        theta = np.asarray(theta, float).reshape(-1)
        if self._cache_theta is None or not np.array_equal(theta, self._cache_theta):
            self.evaluate(theta)
        return self._cache_jets

    def parameter_derivatives(self, theta):
        return self.jet_parameter_derivatives(theta)[0]

    def rho_material_jets(self, theta):
        f = self.evaluate(theta)
        k, ku, kuu = f["kappa"], f["kappa_u"], f["kappa_uu"]
        return 1./k, -ku/k**2, 2.*ku**2/k**3-kuu/k**2

    def summary(self):
        result = dict(core_kind="material-curvature-flattening",
                      base_mode=self.base_mode, support_amplitude=self.support_amplitude,
                      physical_parameters=self.coefficients.tolist(),
                      homotopy=self.homotopy, curvature_blend=self.curvature_blend,
                      target_curvature=self.target_curvature, circle_curvature=self.k,
                      halfwidth=self.halfwidth, halfwidth_coordinate="material-arclength",
                      transition=self.transition, compensation_beta=self.beta,
                      exact_perimeter=2.*math.pi, curvature_radius_lower=self.rho_lower,
                      curvature_radius_upper=self.rho_upper,
                      curvature_lower_bound=self.curvature_lower_bound,
                      curvature_upper_bound=self.curvature_upper_bound,
                      curvature_guard=self.curvature_guard,
                      quadrature_order=self.quadrature_order,
                      integration_cells=self.integration_cells,
                      transition_cells=self.transition_cells,
                      reflection_roundoff=self.reflection_roundoff,
                      original_kind=type(self.original).__name__,
                      implementation_validation="not yet executed when source was saved",
                      scope="core design only; no full metric, tail, or closed-surface claim")
        if self.homotopy == 1.:
            g = self.evaluate(np.array([self.halfperiod]))
            center = g["F"][0, :2]-np.array(
                [math.cos(self.halfperiod), math.sin(self.halfperiod)])/self.k
            result["circle_center"] = center.tolist()
        return result


def make_factory(reference, settings=None):
    """Return a physical-support-parameter Core factory.

    reference must be the genuine original PlanarSupportCore class/factory.
    lambda=0 returns it literally and does not add or mutate its methods.
    """
    options = dict(settings or {})
    homotopy = float(options.pop("homotopy", 0.))
    if not (0. <= homotopy <= 1.):
        raise ValueError("homotopy must lie in [0,1]")
    original_arc_nodes = options.pop("original_arc_nodes", None)

    def factory(q, corrections=(), base_mode=3):
        original_options = dict(base_mode=base_mode)
        if original_arc_nodes is not None:
            original_options["arc_nodes"] = int(original_arc_nodes)
        original = reference(q, corrections, **original_options)
        if homotopy == 0.:
            return original
        return MaterialFlattenedSupportCore(original, homotopy=homotopy, **options)

    factory.parameter_jets = parameter_jets
    factory.flattening_settings = dict(settings or {})
    return factory

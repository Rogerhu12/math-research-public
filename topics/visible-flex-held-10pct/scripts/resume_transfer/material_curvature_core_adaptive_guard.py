"""Version 2: same material core with a sharper positive-curvature domain guard.

This is a new physical family, not a reparameterization of the normal-angle
raw/support core.  q and corrections below are curvature controls.  No BVP,
closed-surface or reach claim is made by this module.  All construction
integrals are evaluated by piecewise Gauss quadrature, with an explicit
quadrature order/refinement parameter; no interpolant is called exact.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.polynomial import Polynomial


_STEP = Polynomial([0, 0, 0, 0, 0, 126, -420, 540, -315, 70])
_STEP_INT = _STEP.integ()


def _xyz(z):
    z = np.asarray(z)
    return np.stack((z.real, z.imag, np.zeros_like(z.real)), axis=-1)


class MaterialCurvatureCore:
    """Even n-fold convex core in circumference-2pi material coordinate.

    The protected material halfwidth is ``halfwidth``.  On that interval
    kappa = 1 - amplitude_scale*q exactly in the defining functions.  All
    correction controls vanish there and have zero integral on each sector.
    ``amplitude_scale`` defaults to n*n-1 solely for convenient input size;
    q is NOT the true normal-angle support Fourier coefficient.
    """

    def __init__(self, q=.02, corrections=(), base_mode=3, *, halfwidth=.20,
                 transition=.30, amplitude_scale=None, arc_nodes=1024,
                 quadrature_order=16, integration_cells=64, **unused):
        if unused:
            raise TypeError("Undeclared material-core settings: " + repr(unused))
        self.base_mode = int(base_mode)
        if self.base_mode != base_mode or self.base_mode < 2:
            raise ValueError("base_mode must be an integer >=2")
        self.T = 2*np.pi/self.base_mode
        self.center = self.T/2
        self.a = float(halfwidth)
        self.transition = float(transition)
        if not 0 < self.a < self.a+self.transition < self.T/2:
            raise ValueError("Require 0 < halfwidth < halfwidth+transition < pi/n")
        self.q = float(q)
        self.factor = float(self.base_mode**2-1 if amplitude_scale is None else amplitude_scale)
        self.support_amplitude = self.q  # legacy input label; see summary.
        self.corrections = tuple(float(c) for c in corrections)
        self.c = np.asarray(self.corrections)
        self.coefficients = np.r_[self.q, self.c]
        self.frequencies = self.base_mode*np.arange(1, len(self.c)+2)
        self.omega = self.base_mode*np.arange(1, len(self.c)+1)
        self.mean_chi = (2*self.a+self.transition)/self.T
        self.norms = 1 + (630/256)/(self.transition*self.omega)
        self.circle_curvature = 1-self.factor*self.q
        # W*cos + W'*sin/omega is bounded by the declared normalization.
        pmin = min(-self.factor, self.factor*self.mean_chi/(1-self.mean_chi))
        pmax = max(-self.factor, self.factor*self.mean_chi/(1-self.mean_chi))
        lo, hi = sorted((self.q*pmin, self.q*pmax))
        radius = float(np.sum(abs(self.c)))
        self.curvature_lower_bound = 1+lo-radius
        self.curvature_upper_bound = 1+hi+radius
        self.curvature_triangle_lower = self.curvature_lower_bound
        self.curvature_triangle_upper = self.curvature_upper_bound
        self.curvature_guard_grid = 0
        self.curvature_guard_method = 'triangle'
        self.curvature_second_derivative_bound = 0.
        if self.curvature_lower_bound <= 1e-5:
            self._refine_curvature_guard()
        self.rho_lower = 1/self.curvature_upper_bound
        self.rho_upper = 1/self.curvature_lower_bound
        self.rho_triangle_lower = self.rho_lower
        self.control_rho_bounds = np.ones(len(self.c)) / self.curvature_lower_bound**2
        self.positivity_grid_per_sector = 0
        self._last_theta = None
        self._last_evaluation = None
        self._last_parameter_jets = None
        self.quadrature_order = int(quadrature_order)
        self.integration_cells = int(integration_cells)
        if self.quadrature_order < 8 or self.integration_cells < 8:
            raise ValueError("Use at least order8 and 8 integration cells")
        self.gx, self.gw = np.polynomial.legendre.leggauss(self.quadrature_order)
        marks = np.r_[np.linspace(0, self.T, self.integration_cells+1),
                      self.center-self.a-self.transition, self.center-self.a,
                      self.center, self.center+self.a, self.center+self.a+self.transition]
        self.breaks = np.unique(marks)
        self._cumulative = np.zeros((len(self.breaks), len(self.coefficients)+1), dtype=complex)
        for j, (left, right) in enumerate(zip(self.breaks[:-1], self.breaks[1:])):
            self._cumulative[j+1] = self._cumulative[j] + self._integrate(left, np.array([right]))[0]
        self._origins = self._cumulative[-1] / np.expm1(1j*self.T)
        self.period_reflection_roundoff = float(np.max(abs(self._origins.imag)))
        # Reflection implies these imaginary parts vanish in the defining integrals.
        self._origins = self._origins.real.astype(complex)
        theta = 2*np.pi*np.arange(int(arc_nodes))/int(arc_nodes)
        g = self.evaluate(theta)
        rr = np.linalg.norm(g['F'], axis=-1)
        self.radius_max_sample = float(rr.max())
        self.radius_min_sample = float(rr.min())
        self.radius_upper_bound = self.radius_max_sample + np.pi/int(arc_nodes)
        self.radius_lower_bound = max(0., self.radius_min_sample - np.pi/int(arc_nodes))
        self.minimum_sampled_curvature = float(g['kappa'].min())
        self.maximum_sampled_curvature = float(g['kappa'].max())
        self.rho_min_sample = 1/self.maximum_sampled_curvature
        self.rho_max_sample = 1/self.minimum_sampled_curvature
        self.constant_width_exact = False
        self.width_defect_bound = math.nan
        self.support_monotone = False

    def _refine_curvature_guard(self):
        """Same positive-curvature floor, sharper continuous interpolation bound.

        The analytic error formula is h^2*||kappa''||_inf/8. Node values use
        binary64 and the declared evaluation allowance, not outward interval
        arithmetic; this numerical domain guard is not a certified theorem
        about a complete curve/surface's floating-point evaluation.
        """
        b = self.transition
        D1 = 630/(256*b)
        D2 = 2520/(64*b*b)
        D3 = (7560/16+5040/64)/(b**3)
        w = self.omega
        columns = (3*D2+w*w+D3/w+3*w*D1)/self.norms
        M2 = abs(self.factor*self.q)*D2/(1-self.mean_chi)+float(np.sum(abs(self.c)*columns))
        self.curvature_second_derivative_bound = float(np.nextafter(M2, np.inf))
        allowance = 1e-12*(1+abs(self.factor*self.q)/(1-self.mean_chi)+float(np.sum(abs(self.c))))
        count = 512
        while True:
            theta = self.T*np.arange(count)/count
            kb = self._angle_basis(theta)[1]
            value = 1+self.coefficients@kb
            slack = (self.T/count)**2*self.curvature_second_derivative_bound/8+allowance
            lower = max(self.curvature_triangle_lower, float(np.min(value)-slack))
            upper = min(self.curvature_triangle_upper, float(np.max(value)+slack))
            self.curvature_guard_grid = count
            self.curvature_guard_sample_min = float(np.min(value))
            self.curvature_guard_sample_max = float(np.max(value))
            self.curvature_guard_slack = float(slack)
            if lower > 1e-5:
                self.curvature_lower_bound = lower
                self.curvature_upper_bound = upper
                self.curvature_guard_method = 'periodic-linear-interpolation-second-derivative'
                return
            if np.min(value) <= 1e-5:
                raise FloatingPointError('Material core actual sampled curvature failed: '+repr((float(np.min(value)), count)))
            if count >= 32768:
                raise FloatingPointError('Material core curvature guard cannot certify at ceiling: '+repr((lower, float(np.min(value)), count)))
            count *= 2

    def _window(self, local):
        d = np.asarray(local)-self.center
        t = np.clip((abs(d)-self.a)/self.transition, 0., 1.)
        W = _STEP(t)
        W1 = 630*t**4*(1-t)**4*np.sign(d)/self.transition
        W2 = 2520*t**3*(1-t)**3*(1-2*t)/self.transition**2
        W3 = (7560*t**2*(1-t)**2*(1-2*t)**2-5040*t**3*(1-t)**3)*np.sign(d)/self.transition**3
        # Integral of chi from the middle of the material arc, not from a
        # normal-angle coordinate.  Its exact endpoint value is a+b/2.
        z = abs(d)
        C = np.where(z <= self.a, z,
                     np.where(z >= self.a+self.transition, self.a+self.transition/2,
                              self.a+self.transition*(t-_STEP_INT(t))))
        return d, W, W1, W2, W3, np.sign(d)*C

    def _angle_basis(self, local):
        x = np.asarray(local, dtype=float).ravel()
        d, W, W1, W2, W3, C = self._window(x)
        phase0 = self.factor*(self.mean_chi*d-C)/(1-self.mean_chi)
        k0 = self.factor*(W-(1-self.mean_chi))/(1-self.mean_chi)
        k01 = self.factor*W1/(1-self.mean_chi)
        k02 = self.factor*W2/(1-self.mean_chi)
        if not len(self.c):
            return phase0[None, :], k0[None, :], k01[None, :], k02[None, :]
        w = self.omega[:, None]
        sin = np.sin(w*x[None, :]); cos = np.cos(w*x[None, :])
        scale = self.norms[:, None]
        phase = W[None, :]*sin/w/scale
        k = (W[None, :]*cos+W1[None, :]*sin/w)/scale
        k1 = (2*W1[None, :]*cos+(W2[None, :]/w-W[None, :]*w)*sin)/scale
        k2 = ((3*W2[None, :]-W[None, :]*w*w)*cos+
              (W3[None, :]/w-3*W1[None, :]*w)*sin)/scale
        return tuple(np.concatenate((a[None, :], b), axis=0)
                     for a, b in ((phase0, phase), (k0, k), (k01, k1), (k02, k2)))

    def _integrate(self, left, right):
        right = np.asarray(right)
        nodes = (right[..., None]+left)/2 + (right[..., None]-left)/2*self.gx
        basis = self._angle_basis(nodes.ravel())[0]
        phi = nodes.ravel()+self.coefficients@basis
        normal = np.exp(1j*phi)
        values = np.concatenate(((1j*normal)[None, :], -basis*normal[None, :]), axis=0)
        values = values.reshape((len(self.coefficients)+1, len(right), self.quadrature_order))
        return ((right-left)/2)[:, None]*np.einsum('pni,i->np', values, self.gw)

    def _position_and_parameter_derivatives(self, theta):
        flat = np.asarray(theta, dtype=float).ravel()
        sector = np.floor(flat/self.T)
        local = flat-sector*self.T
        index = np.clip(np.searchsorted(self.breaks, local, side='right')-1, 0, len(self.breaks)-2)
        result = np.empty((len(flat), len(self.coefficients)+1), dtype=complex)
        for j in np.unique(index):
            mask = index == j
            result[mask] = self._origins+self._cumulative[j]+self._integrate(self.breaks[j], local[mask])
        return result*np.exp(1j*sector*self.T)[:, None]

    def evaluate(self, theta):
        theta = np.asarray(theta, dtype=float)
        if self._last_theta is not None and np.array_equal(theta, self._last_theta):
            return self._last_evaluation
        flat = theta.ravel()
        sector = np.floor(flat/self.T)
        local = flat-sector*self.T
        phase, kb, k1b, k2b = self._angle_basis(local)
        phi = flat+self.coefficients@phase
        kappa = 1+self.coefficients@kb
        kp = self.coefficients@k1b
        kpp = self.coefficients@k2b
        normal = np.exp(1j*phi)
        positions = self._position_and_parameter_derivatives(theta)
        F = _xyz(positions[:, 0]).reshape(theta.shape+(3,))
        Ft = _xyz(1j*normal).reshape(theta.shape+(3,))
        Ftt = _xyz(-kappa*normal).reshape(theta.shape+(3,))
        Fttt = _xyz((-kp-1j*kappa*kappa)*normal).reshape(theta.shape+(3,))
        ans = dict(F=F, Ft=Ft, Ftt=Ftt, Fttt=Fttt, phi=phi.reshape(theta.shape),
                   kappa=kappa.reshape(theta.shape), kappa_u=kp.reshape(theta.shape),
                   kappa_uu=kpp.reshape(theta.shape), arc_residual=np.zeros_like(theta),
                   arc_iterations=0)
        d0 = _xyz(positions[:, 1:].T)
        d1 = _xyz(-phase*normal[None, :])
        d2 = _xyz(-(kb+1j*kappa[None, :]*phase)*normal[None, :])
        self._last_theta = theta.copy()
        self._last_evaluation = ans
        self._last_parameter_jets = (d0, d1, d2)
        return ans

    def parameter_derivatives(self, theta):
        self.evaluate(theta)
        return self._last_parameter_jets[0]

    def jet_parameter_derivatives(self, theta):
        self.evaluate(theta)
        return self._last_parameter_jets

    def rho_material_jets(self, theta):
        g = self.evaluate(theta)
        k, kp, kpp = g['kappa'], g['kappa_u'], g['kappa_uu']
        return dict(**g, rho=1/k, rho_u=-kp/k**2, rho_uu=2*kp**2/k**3-kpp/k**2,
                    rho_phi=-kp/k**3, rho_phiphi=3*kp**2/k**5-kpp/k**4,
                    normal=_xyz(np.exp(1j*g['phi'])))

    def summary(self):
        g = self.evaluate(np.array([self.center]))
        R = 1/self.circle_curvature
        circle_center = g['F'][0]-R*_xyz(np.exp(1j*self.center))
        return dict(core_kind='material_curvature_integral', base_mode=self.base_mode,
                    q_parameter=self.q, q_meaning='curvature decrement / amplitude_scale; not support Fourier Q',
                    amplitude_scale=self.factor, corrections=list(self.corrections),
                    correction_meaning='normalized material curvature derivative controls',
                    halfwidth=self.a, halfwidth_coordinate='material arclength',
                    transition=self.transition, center=self.center,
                    plateau_curvature=self.circle_curvature, plateau_radius=R,
                    plateau_normal_halfwidth=self.a*self.circle_curvature,
                    plateau_material_endpoints=[self.center-self.a, self.center+self.a],
                    plateau_material_length=2*self.a, circle_center=circle_center.tolist(),
                    circle_center_norm=float(np.linalg.norm(circle_center)),
                    exact_perimeter=2*np.pi, curvature_lower=self.curvature_lower_bound,
                    curvature_upper=self.curvature_upper_bound, rho_lower=self.rho_lower,
                    rho_upper=self.rho_upper, radius_max_sample=self.radius_max_sample,
                    quadrature_order=self.quadrature_order, integration_cells=self.integration_cells,
                    reflection_roundoff=self.period_reflection_roundoff,
                    curvature_guard_method=self.curvature_guard_method,
                    curvature_guard_grid=self.curvature_guard_grid,
                    curvature_triangle_lower=self.curvature_triangle_lower,
                    curvature_guard_second_derivative_bound=self.curvature_second_derivative_bound,
                    scope='Integral-defined closed convex core; no complete surface or BVP claimed')


def parameter_jets(core, theta):
    """Adapter for the lift module's analytic parameter-jets entry point."""
    return core.jet_parameter_derivatives(theta)

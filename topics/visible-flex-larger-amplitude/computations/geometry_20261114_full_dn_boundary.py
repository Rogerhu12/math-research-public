#!/usr/bin/env python3
"""All nonmean material-angle DN rows for the normal-angle Frenet state.

This module supplies an actual finite boundary map and its chain-rule
Jacobian. It is not a solved BVP. A caller must supply the original true tail
DN evaluator, the complete controlled scalar profile, and the finite Frenet
RHS/Jacobians at the physical cut. In particular, a principal normal
projector is not accepted as a replacement for the tail DN evaluator.

State ordering is r[0:M+1], t[1:M+1], z[0:M+1]. If K support
coefficients are fixed and T material tail modes are imposed on M field
modes, dimensional squareness requires T-M+K scalar controls. Initial
design uses K=3. Canonical-material fixed-metric refinement uses K=0,
T=M and an already frozen scalar profile with no controls. Independence,
the remaining angular spectral error, the mean radial height jets and full
Cartesian closure still need actual calculation. Continuous mean uniqueness
under the original positive branch is a separate statement; a finite DFT
does not by itself establish its hypotheses.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from geometry_20261114_material_quintic_readout import material_angles


@dataclass
class Trace:
    height: np.ndarray
    derivative_s: np.ndarray
    projection: np.ndarray
    height_core_jacobian: np.ndarray
    derivative_core_jacobian: np.ndarray
    angle_info: dict


class MaterialTrace:
    """Actual normal-to-material pullback and all core-angle derivatives.

    Quadrature is finite. A separate angular-grid and tail-mode refinement
    must bound its error; this class never calls a finite DFT exact Fourier
    coefficients of the composed smooth function.
    """
    def __init__(self, field_modes, tail_modes, angular=4096):
        self.M, self.T, self.N = map(int, (field_modes, tail_modes, angular))
        if self.M < 3 or self.T < self.M or self.N <= 4 * max(self.M, self.T) or self.N % 2:
            raise ValueError("Keep the full field, all requested tail modes and a resolved even grid")
        self.frequency = 2 * np.arange(1, self.M + 1)
        theta = 2 * np.pi * np.arange(self.N) / self.N
        self.project = (2 / self.N) * np.cos(2 * np.arange(1, self.T + 1)[:, None] * theta)

    def __call__(self, core, z, zs):
        core, z, zs = (np.asarray(value, dtype=float) for value in (core, z, zs))
        if core.shape != (self.M,) or z.shape != (self.M + 1,) or zs.shape != z.shape:
            raise ValueError("Material trace must consume the complete core and height jets")
        phi, rho, _, angle_info = material_angles(core, self.N)
        if np.any(rho <= 0):
            raise FloatingPointError("The normal-to-material map is not orientation preserving")
        argument = self.frequency[:, None] * phi
        cosphi = np.r_[np.ones((1, self.N)), np.cos(argument)]
        projection = self.project @ cosphi.T
        # The constant phi mode is exactly constant in theta. Its nonmean
        # projection is zero independently of floating quadrature roundoff.
        projection[:, 0] = 0
        dphi_dc = -((1 - self.frequency ** 2) / self.frequency)[:, None] * np.sin(argument) / rho
        zphi = -(self.frequency * z[1:]) @ np.sin(argument)
        zsphi = -(self.frequency * zs[1:]) @ np.sin(argument)
        return Trace(height=projection @ z, derivative_s=projection @ zs,
                     projection=projection,
                     height_core_jacobian=self.project @ (dphi_dc * zphi).T,
                     derivative_core_jacobian=self.project @ (dphi_dc * zsphi).T,
                     angle_info=angle_info)


class FullDNBoundary:
    """Square coupled system, retaining all requested nonmean tail rows.

    rhs(s, y, p) is the physical-s Frenet RHS. rhs_jac(s,y,p) returns
    (d_rhs/d_y, d_rhs/d_p). The controlled scalar profile preserves the
    complete tail metric/cut for all p.

    tail_map(H) returns {slope, jacobian, actual_nonlinear_solve, ...}, where
    slope=dH/dr and jacobian=d(slope)/dH have all T modes. It may be a clearly
    labeled affine inner map during outer Newton iteration; final acceptance
    must separately call the true nonlinear tail with full audit.
    """
    def __init__(self, profile, target_core, rhs, rhs_jac, tail_map,
                 height_sign=-1, radial_sign=-1, angular=4096):
        self.profile = profile
        self.M, self.T = profile.M, profile.tail_modes
        self.n = 3 * self.M + 2
        self.target = np.asarray(target_core, dtype=float)
        if self.target.ndim != 1 or len(self.target) > self.M:
            raise ValueError("Supply a vector of the explicitly fixed low-core coefficients")
        self.K = len(self.target)
        self.k = self.T - self.M + self.K
        self.left_count = 2 * self.M + self.K + 2
        if profile.parameter_count != self.k or self.left_count + self.T != self.n + self.k:
            raise ValueError("The full DN boundary problem is not dimensionally square")
        if height_sign not in (-1, 1) or radial_sign not in (-1, 1):
            raise ValueError("Both physical orientation signs must be explicit")
        self.eh, self.er = height_sign, radial_sign
        self.rhs, self.rhs_jac, self.tail_map = rhs, rhs_jac, tail_map
        self.trace = MaterialTrace(self.M, self.T, angular)
        self.iz = 2 * self.M + 1
        self.cut_scale = self.eh * self.er / np.sqrt(float(profile.cut["E"]))

    def _inputs(self, ya, yb, p):
        ya, yb, p = (np.asarray(value, dtype=float) for value in (ya, yb, p))
        if ya.shape != (self.n,) or yb.shape != ya.shape or p.shape != (self.k,):
            raise ValueError("Full boundary state or scalar-control dimensions differ")
        jet = np.array(self.profile.profile(self.profile.end, p))
        E, Ep = float(self.profile.cut["E"]), float(self.profile.cut["Ep"])
        target = np.array([self.profile.cut["radius"], self.er / np.sqrt(E), -Ep / (2 * E ** 2)])
        if np.max(np.abs(jet - target)) > 5e-12:
            raise ValueError("The scalar controls changed the physical tail cut")
        return ya, yb, p

    def data(self, ya, yb, p):
        ya, yb, p = self._inputs(ya, yb, p)
        derivative = np.asarray(self.rhs(self.profile.end, yb, p))
        if derivative.shape != (self.n,):
            raise ValueError("A complete physical Frenet endpoint derivative is required")
        trace = self.trace(ya[1:self.M + 1], yb[self.iz:], derivative[self.iz:])
        native_height = self.eh * trace.height
        tail = self.tail_map(native_height)
        slope, J = np.asarray(tail["slope"], dtype=float), np.asarray(tail["jacobian"], dtype=float)
        if slope.shape != (self.T,) or J.shape != (self.T, self.T):
            raise ValueError("The tail response lost a height mode or DN Jacobian row")
        if "actual_nonlinear_solve" not in tail:
            raise ValueError("The tail evaluator must label true versus affine evaluation")
        if not np.all(np.isfinite(slope)) or not np.all(np.isfinite(J)):
            raise FloatingPointError("Nonfinite complete tail response")
        return ya, yb, p, trace, tail, slope, J

    def __call__(self, ya, yb, p):
        ya, yb, p, trace, tail, slope, J = self.data(ya, yb, p)
        frequency = 2 * np.arange(1, self.M + 1)
        left = np.r_[ya[0] - 1, ya[1:self.K + 1] - self.target,
                     ya[self.M + 1:self.iz] + frequency * ya[1:self.M + 1], ya[self.iz:]]
        right = trace.derivative_s - self.cut_scale * slope
        return np.r_[left, right]

    def jacobian(self, ya, yb, p):
        ya, yb, p, trace, tail, slope, J = self.data(ya, yb, p)
        Jy, Jp = self.rhs_jac(self.profile.end, yb, p)
        Jy, Jp = np.asarray(Jy), np.asarray(Jp)
        if Jy.shape != (self.n, self.n) or Jp.shape != (self.n, self.k):
            raise ValueError("Complete state and all scalar-control Jacobians are required")
        rows = self.n + self.k
        A = np.zeros((rows, self.n)); B = np.zeros_like(A); P = np.zeros((rows, self.k))
        A[:self.K + 1, :self.K + 1] = np.eye(self.K + 1)
        j = np.arange(self.M)
        A[self.K + 1 + j, 1 + j] = 2 * (j + 1)
        A[self.K + 1 + j, self.M + 1 + j] = 1
        j = np.arange(self.M + 1)
        A[self.K + 1 + self.M + j, self.iz + j] = 1
        last = slice(self.left_count, None)
        A[last, 1:self.M + 1] = (trace.derivative_core_jacobian
            - self.cut_scale * J @ (self.eh * trace.height_core_jacobian))
        B[last] = trace.projection @ Jy[self.iz:]
        B[last, self.iz:] -= self.cut_scale * J @ (self.eh * trace.projection)
        P[last] = trace.projection @ Jp[self.iz:]
        return A, B, P


def directional_check(boundary, ya, yb, parameters, directions, steps=(2e-6, 1e-6)):
    """Run actual centered FD responses against the complete analytic BC J.

    directions contains dictionaries with name and full ya/yb/p vectors.
    Call only at a real cut with the real tail evaluator, or explicitly mark
    a complete affine-inner DN map as such. This returns measurements; it
    never turns a proxy DN, a direction check, or a prepared state into a
    nonlinear accepted closed surface.
    """
    ya, yb, parameters = map(np.asarray, (ya, yb, parameters))
    A, B, P = boundary.jacobian(ya, yb, parameters)
    rows = []
    for direction in directions:
        da, db, dp = [np.asarray(direction[name]) for name in ("ya", "yb", "p")]
        analytic = A @ da + B @ db + P @ dp
        levels = []
        for step in steps:
            plus = boundary(ya + step * da, yb + step * db, parameters + step * dp)
            minus = boundary(ya - step * da, yb - step * db, parameters - step * dp)
            finite = (plus - minus) / (2 * step)
            error = float(np.max(np.abs(finite - analytic)))
            scale = max(1., float(np.max(np.abs(analytic))))
            levels.append(dict(step=float(step), absolute_error=error, relative_error=error / scale,
                               finite_response_max=float(np.max(np.abs(finite)))))
        rows.append(dict(direction=direction["name"], analytic_response_max=float(np.max(np.abs(analytic))),
                         levels=levels))
    return dict(scope="Actual complete boundary directional checks only; no global BVP solve.",
                field_modes=boundary.M, tail_modes=boundary.T, state_dimension=boundary.n,
                fixed_core_modes=boundary.K,
                parameter_count=boundary.k, boundary_rows=boundary.n + boundary.k,
                directions=rows, closed_surface_certified=False)

#!/usr/bin/env python3
"""R252 complete physical-angle Galerkin DN boundary.

This is an explicitly different finite boundary test, not P^{-1} times
the old material-angle residual.  The complete physical field, full core,
native height H=epsilon_h P z, true tail map and all scalar controls are
unchanged.  Only the nonmean slope test changes from P v-gamma D(H) to
v-gamma S D(H).  Old material residuals and the finite projection defects
must be reported separately; success of this map does not certify them.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path

import numpy as np

from geometry_20261114_full_dn_boundary import FullDNBoundary


SCHEMA = "complete-physical-angle-Galerkin-DN-test-v1"


def source_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


@dataclass
class Pullback:
    projection: np.ndarray
    derivative_core_jacobian: np.ndarray
    mean_coefficients: np.ndarray
    angular: int
    rho_sample_min: float


class PhysicalTestBoundary(FullDNBoundary):
    """All M physical nonmean rows and their full exact-chain Jacobian.

    Both quadratures are fixed, explicitly recorded finite cosine rules.
    The original material rule is used unchanged for native height input.
    The physical rule synthesizes every requested native slope mode before
    projection.  No S inverse, SVD truncation or principal slope is used.
    """
    def __init__(self, *args, physical_angles=4096, **kwargs):
        super().__init__(*args, **kwargs)
        if self.T != self.M:
            raise ValueError("This separately counted R252 implementation uses full T=M")
        self.physical_angles = int(physical_angles)
        if self.physical_angles <= 4 * max(self.M, self.T) or self.physical_angles % 2:
            raise ValueError("Use a fixed resolved even physical boundary quadrature")
        self.physical_phi = 2 * np.pi * np.arange(self.physical_angles) / self.physical_angles
        self.physical_frequency = 2 * np.arange(1, self.M + 1)
        argument = self.physical_frequency[:, None] * self.physical_phi
        self.physical_cosine = np.cos(argument)
        self.physical_sine = np.sin(argument)
        self.physical_project = (2 / self.physical_angles) * self.physical_cosine
        self.material_core_argument_derivative = (
            ((1 - self.physical_frequency ** 2) / self.physical_frequency)[:, None]
            * self.physical_sine)

    def description(self):
        return dict(schema=SCHEMA, source_sha256=source_sha256(),
            formula="R_phi = Z_nonmean f - cut_scale S(c) D(epsilon_h P(c) z_nonmean)",
            native_height_formula="H=epsilon_h P(c) z_nonmean; unchanged full material trace",
            material_angles=self.trace.N, physical_angles=self.physical_angles,
            field_modes=self.M, tail_modes=self.T, right_rows=self.M,
            height_sign=self.eh, radial_sign=self.er, cut_scale=float(self.cut_scale),
            quadrature="Independent fixed uniform theta and phi cosine sums; no quadrature-error certificate",
            original_material_test_equivalent_at_finite_modes=False,
            all_physical_core_scalar_columns_retained=True,
            original_true_tail_and_complete_native_J_retained=True)

    def pullback(self, core, slope):
        core, slope = np.asarray(core, float), np.asarray(slope, float)
        if core.shape != (self.M,) or slope.shape != (self.T,):
            raise ValueError("The pullback consumes all core and native slope modes")
        theta = self.physical_phi + core @ self.material_core_argument_derivative
        native_frequency = 2 * np.arange(1, self.T + 1)
        argument = native_frequency[:, None] * theta
        cosine, sine = np.cos(argument), np.sin(argument)
        S = self.physical_project @ cosine.T
        slope_theta = -(native_frequency * slope) @ sine
        # Column j is Q_phi[(d/dtheta C_theta slope)(Phi_c) d_cj Phi_c].
        # Its sign and the derivative of Phi itself are both included.
        Sj_slope = self.physical_project @ (
            self.material_core_argument_derivative * slope_theta).T
        rho = 1 + ((1 - self.physical_frequency ** 2) * core) @ self.physical_cosine
        return Pullback(projection=S, derivative_core_jacobian=Sj_slope,
                        mean_coefficients=cosine.mean(axis=1),
                        angular=self.physical_angles, rho_sample_min=float(rho.min()))

    def __call__(self, ya, yb, p):
        ya, yb, p, trace, tail, slope, J = self.data(ya, yb, p)
        derivative = np.asarray(self.rhs(self.profile.end, yb, p))
        pullback = self.pullback(ya[1:self.M + 1], slope)
        left = np.r_[ya[0] - 1, ya[1:self.K + 1] - self.target,
                     ya[self.M + 1:self.iz] + self.physical_frequency * ya[1:self.M + 1],
                     ya[self.iz:]]
        right = derivative[self.iz + 1:] - self.cut_scale * pullback.projection @ slope
        return np.r_[left, right]

    def jacobian(self, ya, yb, p):
        ya, yb, p, trace, tail, slope, J = self.data(ya, yb, p)
        Jy, Jp = self.rhs_jac(self.profile.end, yb, p)
        Jy, Jp = np.asarray(Jy), np.asarray(Jp)
        if Jy.shape != (self.n, self.n) or Jp.shape != (self.n, self.k):
            raise ValueError("The full endpoint state and scalar Jacobians are required")
        pullback = self.pullback(ya[1:self.M + 1], slope)
        rows = self.n + self.k
        A = np.zeros((rows, self.n)); B = np.zeros_like(A)
        parameters = np.zeros((rows, self.k))
        A[:self.K + 1, :self.K + 1] = np.eye(self.K + 1)
        j = np.arange(self.M)
        A[self.K + 1 + j, 1 + j] = self.physical_frequency
        A[self.K + 1 + j, self.M + 1 + j] = 1
        j = np.arange(self.M + 1)
        A[self.K + 1 + self.M + j, self.iz + j] = 1
        last = slice(self.left_count, None)
        SJ = pullback.projection @ J
        A[last, 1:self.M + 1] = -self.cut_scale * (
            pullback.derivative_core_jacobian + SJ @ (self.eh * trace.height_core_jacobian))
        B[last] = Jy[self.iz + 1:]
        B[last, self.iz:] -= self.cut_scale * SJ @ (self.eh * trace.projection)
        parameters[last] = Jp[self.iz + 1:]
        return A, B, parameters

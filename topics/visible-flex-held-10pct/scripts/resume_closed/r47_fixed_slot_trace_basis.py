"""R47 fixed-slot finite circle-trace controls, with an unchanged M8 branch.

Physical columns are B2..B6,T,U,B7,...,B(M-2) at lambda one and
cos(6 phi),...,cos(3 M phi) at lambda zero.  T/U stay at zero-based
physical-control indices 5/6.  The canonical endpoint implementation is
reused through an exact coordinate permutation, including its combined
trace bound and primitive normalization.  No new moment integral is defined.

This is low-level source preparation.  Appending zero controls preserves
the defining core in exact mathematics; it does not preserve a finite
partial-lift inlet, a radial interpolant, or a computed mean height.  R48
describes the separate full-reference state compensation.  This module
does not construct a BVP, change a gate, or assert floating bit identity
between different mode counts.
"""
from fractions import Fraction as F
import hashlib
import math
from pathlib import Path
import sys

import numpy as np


M3 = Path(__file__).resolve().parent.parent/'resume_m3'
DEPENDENCY_SHA256 = {
    'circle_trace_homotopy_basis.py': '6689d08c9c86e842bf9f77922801dc357567ec14861012f20a2868ce7f6d7184',
    'circle_trace_replacement_basis.py': '43a1ae54a55f2c7fd6ca224250124d4f6cd6b917591209d1fea91a81057cef6f',
    'circle_trace_controls.py': '8c83f201b19fc60d19aae63b173128cc9bd32b56aee64032009fd342bee63a02',
    'round_raw_lib/complementary_moment_basis.py': 'aa48a458a5146deda566588d4d19a408be4a9d45306469a788f7b9d9071af35c',
    'round_raw_lib/moment_interval_bounds.py': 'ca77a9f8cfba9f88defa37993644dc5bd66c29dbdf737bae7d69243d97f85257',
}
for _name, _expected in DEPENDENCY_SHA256.items():
    if hashlib.sha256((M3/_name).read_bytes()).hexdigest() != _expected:
        raise RuntimeError('A frozen defining basis source changed: '+_name)
for _directory in (M3, M3/'round_raw_lib'):
    if str(_directory) not in sys.path:
        sys.path.insert(0, str(_directory))

from circle_trace_homotopy_basis import CircleTraceHomotopyBasis
from circle_trace_replacement_basis import CircleTraceReplacementBasis
from moment_interval_bounds import upper_float


def checked_modes(modes):
    if isinstance(modes, (bool, np.bool_)) or not isinstance(modes, (int, np.integer)) or modes < 8:
        raise ValueError('R47 retains the original M8 controls and permits integer M>=8')
    return int(modes)


def fixed_to_canonical_indices(modes):
    """E_fixed[i] = E_canonical[permutation[i]], without numerical algebra."""
    M = checked_modes(modes)
    permutation = (*range(5), M-3, M-2, *range(5, M-3))
    if sorted(permutation) != list(range(M-1)):
        raise AssertionError('The fixed-slot map must be a full permutation')
    return permutation


def endpoint_labels(modes):
    M = checked_modes(modes)
    return [*(f'B{j}' for j in range(2, 7)), 'T=SA-SB', 'U=SB',
            *(f'B{j}' for j in range(7, M-1))]


def make_fixed_slot_basis(base_mode=3, modes=8, halfwidth=.21, transition=.4,
                          center=math.pi/3, precision=80, quadrature_order=64,
                          lock_fundamental=True):
    """M8 returns the original class, rather than re-evaluating it differently."""
    M = checked_modes(modes)
    cls = CircleTraceHomotopyBasis if M == 8 else FixedSlotCircleTraceBasis
    return cls(base_mode=base_mode, modes=M, halfwidth=halfwidth,
               transition=transition, center=center, precision=precision,
               quadrature_order=quadrature_order, lock_fundamental=lock_fundamental)


class FixedSlotCircleTraceBasis:
    """The M>8 branch; use make_fixed_slot_basis for the literal M8 branch."""
    def __init__(self, base_mode=3, modes=9, halfwidth=.21, transition=.4,
                 center=math.pi/3, precision=80, quadrature_order=64,
                 lock_fundamental=True):
        self.M = checked_modes(modes)
        if self.M == 8 or base_mode != 3 or not lock_fundamental:
            raise ValueError('The new implementation is n3, M>8 with both low moments locked')
        if float(center).hex() != float(math.pi/3).hex():
            raise ValueError('R47 retains the literal reflection axis pi/3')
        self.n = 3
        self.permutation = np.asarray(fixed_to_canonical_indices(self.M), dtype=int)
        self.endpoint = CircleTraceReplacementBasis(base_mode=3, modes=self.M,
            halfwidth=halfwidth, transition=transition, center=center,
            precision=precision, quadrature_order=quadrature_order,
            lock_fundamental=True)
        self.frequencies = 3*np.arange(2, self.M+1, dtype=float)
        self.derivative_bounds = self.endpoint.derivative_bounds[:, self.permutation].copy()
        # The original integral core multiplies this endpoint error by lambda.
        self.coefficient_evaluation_error_bounds = (
            self.endpoint.coefficient_evaluation_error_bounds[:, self.permutation].copy())
        self.fundamental_evaluation_error = np.zeros(self.M-1)
        self.fundamental_absolute_upper = np.zeros(self.M-1)
        self.fundamental_leakage = np.zeros(self.M-1)

    checked_lambda = staticmethod(CircleTraceHomotopyBasis.checked_lambda)

    def to_canonical(self, coefficients):
        c = np.asarray(coefficients, float)
        if c.shape != (self.M-1,) or not np.all(np.isfinite(c)):
            raise ValueError('All M-1 finite physical controls are required')
        canonical = np.empty_like(c)
        canonical[self.permutation] = c
        return canonical

    def endpoint_support_jets(self, phi, order):
        return tuple(v[self.permutation] for v in self.endpoint.support_jets(phi, order, 1.))

    def endpoint_primitive_jets(self, phi, order):
        return tuple(v[self.permutation] for v in self.endpoint.primitive_jets(phi, order, 1.))

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
            return self.endpoint_support_jets(phi, order)
        old = self.cosine_support_jets(phi, order)
        if lam == 0.:
            return old
        endpoint = self.endpoint_support_jets(phi, order)
        return tuple((1-lam)*a+lam*b for a, b in zip(old, endpoint))

    def primitive_jets(self, phi, order=5, homotopy=1.):
        lam = self.checked_lambda(homotopy)
        if not 0 <= order <= 5:
            raise ValueError('Primitive derivatives zero through five only')
        if lam == 1.:
            return self.endpoint_primitive_jets(phi, order)
        flat = np.asarray(phi, float).ravel()
        m = self.frequencies[:, None]
        primitive = np.sin(m*flat[None, :])/m
        old = (primitive,) if order == 0 else (primitive,)+self.cosine_support_jets(phi, order-1)
        if lam == 0.:
            return old
        endpoint = self.endpoint_primitive_jets(phi, order)
        return tuple((1-lam)*a+lam*b for a, b in zip(old, endpoint))

    def homotopy_rho_bounds(self, homotopy=1.):
        lam = self.checked_lambda(homotopy)
        endpoint = tuple(v[self.permutation] for v in self.endpoint.homotopy_rho_bounds(1.))
        if lam == 1.:
            return endpoint
        lf = F.from_float(lam)
        result = []
        for k in range(3):
            values = []
            for j, m in enumerate(range(6, 3*self.M+1, 3)):
                old = F(m*m-1)*m**k
                values.append(upper_float((1-lf)*old+lf*F.from_float(float(endpoint[k][j]))))
            result.append(np.asarray(values))
        return tuple(result)

    def combined_control_rho_bounds(self, coefficients, homotopy=1.):
        lam = self.checked_lambda(homotopy)
        canonical = self.to_canonical(coefficients)
        endpoint = self.endpoint.combined_control_rho_bounds(canonical, 1.)
        if lam == 1.:
            return endpoint
        c = np.asarray(coefficients, float)
        lf = F.from_float(lam)
        result = []
        for k in range(3):
            cosine = sum(abs(F.from_float(float(c[j])))*F(m*m-1)*m**k
                         for j, m in enumerate(range(6, 3*self.M+1, 3)))
            result.append(upper_float((1-lf)*cosine+lf*F.from_float(float(endpoint[k]))))
        return tuple(result)

    def summary(self):
        return dict(base_mode=3, modes=self.M, controls=self.M-1,
            coordinate_scheme='R47-fixed-trace-slots-5-and-6-v1',
            physical_trace_indices=[5, 6], parameter_indices_if_delta_first=[6, 7],
            columns_at_zero=[f'cos{3*j}' for j in range(2, self.M+1)],
            columns_at_one=endpoint_labels(self.M),
            fixed_to_canonical_indices=self.permutation.tolist(),
            homotopy='C_j=(1-lambda)*cos(3*j*phi)+lambda*E_j; j=2..M',
            endpoint_backend=self.endpoint.summary(),
            endpoint_backend_coordinate_scope='Canonical B2..B(M-2),T,U, used only after the declared exact permutation',
            physical_control_scope='Complete physical c; no q or pscale rescaling and no ignored first control',
            positivity_budget='The same combined endpoint trace bound, plus the whole-domain cosine bound; the original numerical guard is not a surface certificate',
            scope=__doc__)

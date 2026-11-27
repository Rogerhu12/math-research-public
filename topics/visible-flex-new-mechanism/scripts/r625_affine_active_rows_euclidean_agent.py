#!/usr/bin/env python3
"""All-row Euclidean damping under actual affine active constraints C d=g.

The caller has already eliminated its original known end increments and any
fixed length increment.  This helper neither changes those equations nor
adds physical rows.  It receives the caller's complete row-weighted A,b and
all active physical height equations C,g in the same remaining coordinates.

For full row rank C, complete QR of C.T gives orthonormal Q1,N and triangular
R.  d0=Q1 solve(R.T,g), d=d0+N y; d0 is perpendicular to N.  Consequently
||d||^2=||d0||^2+||y||^2 and the original Euclidean damped problem is solved
with every original row of (A@N,b-A@d0), using the frozen full QR/SVD helper.
No coordinate scaling, objective-spectrum truncation, normal equations,
new model derivative, omitted active equation, or physics gate is introduced.

The declared QR diagonal guard rejects an entire numerically dependent
constraint parameterization; it never drops a row or pretends to certify
rank.  All residual observations are records, never added acceptance gates.
Scientific execution belongs only to the declared public Actions scope.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np

BASE_SHA = '56a089e6d5348fdf9d55f78138f76775de66f686976269ad08c1f2636a1d8555'
if hashlib.sha256(Path(__file__).with_name('r625_complete_rows_euclidean_qr_svd_agent.py').read_bytes()).hexdigest() != BASE_SHA:
    raise RuntimeError('The published original Euclidean full-row factor changed.')
import r625_complete_rows_euclidean_qr_svd_agent as base_factor

_FACTOR_RECEIPTS = []


def _public_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Affine complete-row factorization requires the declared public Actions scope.')


def _norm(value):
    with np.errstate(over='ignore', invalid='ignore'):
        return float(np.hypot.reduce(np.ravel(value), initial=0.))


def _finite_or_none(value):
    value = float(value)
    return value if math.isfinite(value) else None


def _maximum(value):
    return float(np.max(np.abs(value))) if np.size(value) else 0.


def factor_receipts():
    """Small actual records, including failed/clock-interrupted constructors.

    Inner-factor records are referenced inside successful wrappers; a failed
    inner constructor is copied from its own public partial-receipt API.
    No original or transformed matrix, Q, N, d0, spectrum or direction is
    written to disk or returned by this metadata interface.
    """
    return json.loads(json.dumps(_FACTOR_RECEIPTS, allow_nan=False))


class AffineActiveRowEuclideanFactor:
    def __init__(self, A, b, C, g, clock, counts, label):
        _public_only()
        if not isinstance(counts, dict) or not isinstance(label, str):
            raise TypeError('Shared cumulative counters and explicit active-set label are required.')
        self.clock, self.counts, self.label = clock, counts, label
        self.ready, self.inner = False, None
        self.receipt = {
            'factor_id': len(_FACTOR_RECEIPTS), 'label': label,
            'phase': 'before_actual_affine_input_capture', 'complete': False,
            'solve_requests': 0,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'base_complete_row_factor_sha256': BASE_SHA,
            'original_row_weights_already_present_and_unchanged': True,
            'all_original_objective_rows_retained': True,
            'all_active_constraint_equations_retained': True,
            'new_coordinate_scaling': False,
            'objective_singular_value_truncation': False,
            'dependent_constraint_rows_removed': False,
            'normal_equation_matrix_formed': False,
            'penalty': 'Euclidean increment on original remaining coordinates',
            'finite_precision_constraint_rank_certified': False,
            'raw_inputs_or_factors_saved_to_files': False,
        }
        _FACTOR_RECEIPTS.append(self.receipt)
        self._count('affine_euclidean_factor_construction_attempts')
        started = time.monotonic()
        inner_label = label+':affine-'+str(self.receipt['factor_id'])+':orthogonal-nullspace'
        self.receipt['inner_factor_label'] = inner_label
        try:
            clock.check('before_affine_complete_row_input_capture')
            raw_A = A.toarray() if hasattr(A, 'toarray') else A
            raw_C = C.toarray() if hasattr(C, 'toarray') else C
            self.A = np.array(raw_A, dtype=np.float64, order='C', copy=True)
            self.b = np.array(b, dtype=np.float64, copy=True)
            self.C = np.array(raw_C, dtype=np.float64, order='C', copy=True)
            self.g = np.array(g, dtype=np.float64, copy=True)
            del raw_A, raw_C
            if (self.A.ndim != 2 or self.b.ndim != 1 or self.C.ndim != 2
                    or self.g.ndim != 1 or self.A.shape[0] != len(self.b)
                    or self.C.shape[0] != len(self.g)
                    or self.C.shape[1] != self.A.shape[1]
                    or self.A.shape[1] == 0 or self.A.shape[0] < self.A.shape[1]):
                raise ValueError('Complete square/tall A,b and matching complete affine C,g are required.')
            self.rows, self.n = self.A.shape
            self.active = self.C.shape[0]
            if self.active > self.n:
                raise np.linalg.LinAlgError('More active equations than free coordinates: no rows are removed.')
            for value in (self.A, self.b, self.C, self.g):
                if not np.all(np.isfinite(value)):
                    raise FloatingPointError('Nonfinite original objective or affine constraint input.')
                value.flags.writeable = False
            identity = hashlib.sha256(json.dumps(
                [self.rows, self.n, self.active], separators=(',', ':')).encode()+b'\n')
            for value in (self.A, self.b, self.C, self.g):
                identity.update(value.tobytes(order='C'))
            self._count('affine_original_A_entries_captured', self.rows*self.n)
            self._count('affine_original_b_entries_captured', self.rows)
            self._count('affine_constraint_entries_captured', self.active*self.n)
            self._count('affine_constraint_target_entries_captured', self.active)
            self.receipt.update(matrix_shape=[self.rows, self.n],
                constraint_shape=[self.active, self.n],
                original_A_b_C_g_float64_sha256=identity.hexdigest(),
                input_bytes=sum(int(x.nbytes) for x in (self.A, self.b, self.C, self.g)),
                phase='before_complete_constraint_transpose_QR')
            clock.check('before_complete_constraint_transpose_QR')
            if self.active:
                qr_started = time.monotonic()
                self._count('affine_constraint_complete_QR_attempts')
                try:
                    Q, R = np.linalg.qr(self.C.T, mode='complete')
                    if (Q.shape != (self.n, self.n) or R.shape != (self.n, self.active)
                            or not np.all(np.isfinite(Q)) or not np.all(np.isfinite(R))):
                        raise FloatingPointError('Incomplete or nonfinite constraint transpose QR.')
                    core = R[:self.active, :]
                    diagonal = np.abs(np.diag(core))
                    threshold = float(np.finfo(float).eps*max(self.n, self.active)*_norm(self.C))
                    self.receipt.update(
                        constraint_QR_absolute_diagonal_min=float(np.min(diagonal)),
                        constraint_QR_absolute_diagonal_max=float(np.max(diagonal)),
                        constraint_dependency_threshold=_finite_or_none(threshold),
                        constraint_dependency_formula='eps64*max(n,active_count)*Frobenius_norm(C)',
                        dependency_guard_rejects_whole_factor_never_drops_equations=True)
                    self._count('affine_constraint_complete_QRs_completed')
                    if not math.isfinite(threshold) or np.any(diagonal <= threshold):
                        self._count('affine_constraint_parameterization_dependency_failures')
                        raise np.linalg.LinAlgError(
                            'All-row affine parameterization is numerically dependent under declared QR guard; no constraint is removed.')
                    self.receipt['phase'] = 'complete_constraint_QR_before_affine_particular_solution'
                finally:
                    elapsed = time.monotonic()-qr_started
                    self._count('affine_constraint_complete_QR_seconds', elapsed)
                    self.receipt['constraint_QR_seconds'] = elapsed
                clock.check('after_constraint_QR_before_affine_particular_solve')
                particular_started = time.monotonic()
                self._count('affine_particular_solve_attempts')
                try:
                    # The actual triangular matrix is solved directly; no
                    # C C.T, normal equations or pseudoinverse is formed.
                    coordinates = np.linalg.solve(core.T, self.g)
                    self.d0 = Q[:, :self.active]@coordinates
                    self.N = Q[:, self.active:].copy(order='C')
                    if (not np.all(np.isfinite(coordinates))
                            or not np.all(np.isfinite(self.d0))
                            or not np.all(np.isfinite(self.N))):
                        raise FloatingPointError('Nonfinite affine particular solution or nullspace basis.')
                    self._count('affine_particular_solves_completed')
                    self._count('affine_particular_product_entries', self.n*self.active)
                    self._count('affine_nullspace_basis_entries', self.n*(self.n-self.active))
                    self.receipt['phase'] = 'affine_particular_and_full_nullspace_ready'
                finally:
                    elapsed = time.monotonic()-particular_started
                    self._count('affine_particular_solve_seconds', elapsed)
                    self.receipt['particular_solve_seconds'] = elapsed
                del Q, R, core, coordinates, diagonal
            else:
                # The zero-constraint identity map does not need a dense I.
                self.d0, self.N = np.zeros(self.n, dtype=np.float64), None
                self.receipt['phase'] = 'no_active_constraints_identity_coordinates'
            self.nullity = self.n-self.active
            self.d0.flags.writeable = False
            if self.N is not None:
                self.N.flags.writeable = False
            self.receipt.update(nullspace_columns=self.nullity,
                particular_Euclidean_norm=_finite_or_none(_norm(self.d0)),
                orthogonal_decomposition_preserves_original_penalty_in_exact_arithmetic=True,
                particular_penalty_constant_not_discarded_from_full_direction=True)
            clock.check('before_original_all_rows_affine_reduction')
            product_started = time.monotonic()
            try:
                if self.active == 0:
                    reduced_A, reduced_b = self.A, self.b
                elif self.nullity:
                    reduced_A = self.A@self.N
                    reduced_b = self.b-self.A@self.d0
                    self._count('affine_original_A_nullspace_product_scalar_terms', self.rows*self.n*self.nullity)
                    self._count('affine_original_A_particular_product_entries', self.rows*self.n)
                    if not np.all(np.isfinite(reduced_A)) or not np.all(np.isfinite(reduced_b)):
                        raise FloatingPointError('Nonfinite complete original-row nullspace problem.')
                else:
                    reduced_A = reduced_b = None
                self.receipt['phase'] = 'original_complete_rows_reduced_without_row_selection'
            finally:
                elapsed = time.monotonic()-product_started
                self._count('affine_all_rows_reduction_seconds', elapsed)
                self.receipt['all_rows_reduction_seconds'] = elapsed
            clock.check('after_affine_reduction_before_full_reduced_QR_SVD')
            if self.nullity:
                self.inner = base_factor.EuclideanCompleteRowFactor(
                    reduced_A, reduced_b, clock, counts, inner_label)
                self.receipt['inner_complete_row_factor'] = self.inner.receipt
            else:
                self.receipt['unique_affine_direction_no_remaining_free_coordinates'] = True
            del reduced_A, reduced_b
            self.ready = True
            self.receipt.update(phase='complete_affine_factor_ready', complete=True)
            self._count('affine_euclidean_factor_constructions_completed')
            clock.check('after_complete_affine_Euclidean_factorization')
        except Exception as exc:
            if self.inner is None:
                for item in reversed(base_factor.factor_receipts()):
                    if item.get('label') == inner_label:
                        self.receipt['inner_interrupted_or_failed_factor'] = item
                        break
            self.receipt.update(phase='affine_factorization_interrupted_or_failed',
                complete=self.ready, exception={'type': type(exc).__name__, 'message': str(exc)})
            self._count('affine_euclidean_factor_failures_or_interruptions')
            raise
        finally:
            elapsed = time.monotonic()-started
            self._count('affine_euclidean_factor_construction_seconds', elapsed)
            self.receipt['factor_construction_seconds_including_inner'] = elapsed

    def _count(self, name, value=1):
        self.counts[name] = self.counts.get(name, 0)+value

    def solve(self, positive_lambda):
        _public_only()
        regularization = float(positive_lambda)
        if not self.ready or not math.isfinite(regularization) or regularization <= 0:
            raise ValueError('A completed affine factor and positive finite lambda are required.')
        self.receipt['solve_requests'] += 1
        self._count('affine_cached_solve_attempts')
        report = {
            'affine_factor_id': self.receipt['factor_id'], 'label': self.label,
            'matrix_shape': [self.rows, self.n], 'active_constraints': self.active,
            'nullspace_columns': self.nullity, 'regularization_lambda': regularization,
            'phase': 'before_cached_affine_damped_solve',
            'factor_recomputed_for_this_lambda': False,
            'all_original_rows_and_all_active_equations_retained': True,
            'penalty': 'Euclidean increment on original remaining coordinates',
            'new_coordinate_scaling': False, 'objective_rank_truncation': False,
            'linear_readouts_are_observations_not_new_physical_gates': True,
        }
        self.receipt['last_solve'] = report
        started = time.monotonic()
        try:
            self.clock.check('before_cached_affine_nullspace_solve')
            if self.nullity:
                reduced, inner_report = self.inner.solve(regularization)
                report['inner_original_all_rows_solve'] = inner_report
                self.clock.check('after_inner_solve_before_affine_original_coordinate_lift')
                if self.active:
                    solution = self.d0+self.N@reduced
                    self._count('affine_nullspace_direction_lift_scalar_terms', self.n*self.nullity)
                else:
                    solution = reduced.copy()
            else:
                solution = self.d0.copy()
                report['zero_nullity_unique_affine_direction_independent_of_lambda'] = True
            if not np.all(np.isfinite(solution)):
                raise FloatingPointError('Nonfinite original-coordinate affine direction.')
            self.clock.check('after_affine_lift_before_complete_original_row_readout')
            # Readouts never discard an otherwise finite direction. The
            # caller still uses its original unscaled prediction, step rules
            # and complete nonlinear curve/physical acceptance conditions.
            with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
                constraint_residual = self.C@solution-self.g
                residual = self.A@solution-self.b
                gradient = self.A.T@residual+regularization*solution
                if self.active == 0:
                    projected = gradient
                elif self.nullity:
                    projected = self.N.T@gradient
                else:
                    projected = np.empty(0, dtype=np.float64)
            self._count('affine_original_constraint_readout_entries', self.active*self.n)
            self._count('affine_original_row_residual_matvec_entries', self.rows*self.n)
            self._count('affine_original_gradient_matvec_entries', self.rows*self.n)
            if self.active and self.nullity:
                self._count('affine_projected_gradient_product_entries', self.n*self.nullity)
            report.update(
                phase='completed_cached_affine_Euclidean_solve',
                original_scaled_row_residual_norm=_finite_or_none(_norm(residual)),
                original_scaled_row_residual_max=_finite_or_none(_maximum(residual)),
                original_affine_constraint_residual_norm=_finite_or_none(_norm(constraint_residual)),
                original_affine_constraint_residual_max=_finite_or_none(_maximum(constraint_residual)),
                original_Euclidean_direction_norm=_finite_or_none(_norm(solution)),
                original_direction_infinity_norm=_finite_or_none(_maximum(solution)),
                original_projected_regularized_stationarity_norm=_finite_or_none(_norm(projected)),
                original_projected_regularized_stationarity_max=_finite_or_none(_maximum(projected)),
                original_constraint_formula='C@d-g',
                original_row_residual_formula='A@d-b',
                original_constrained_stationarity_formula='N.T@(A.T@(A@d-b)+lambda*d)',
                full_gradient_need_not_vanish_under_affine_constraints=True,
                nonfinite_constraint_observation_entries=int(np.sum(~np.isfinite(constraint_residual))),
                nonfinite_row_residual_observation_entries=int(np.sum(~np.isfinite(residual))),
                nonfinite_full_gradient_observation_entries=int(np.sum(~np.isfinite(gradient))),
                nonfinite_projected_stationarity_observation_entries=int(np.sum(~np.isfinite(projected))),
                diagnostic_overflow_does_not_reject_finite_direction=True,
                floating_affine_solution_error_or_global_physical_feasibility_certified=False,
            )
            self._count('affine_cached_solves_completed')
            self.clock.check('after_complete_original_affine_direction_readout')
            return solution, report
        except Exception as exc:
            report.update(phase='cached_affine_solve_interrupted_or_failed',
                exception={'type': type(exc).__name__, 'message': str(exc)})
            self._count('affine_cached_solve_failures_or_interruptions')
            raise
        finally:
            elapsed = time.monotonic()-started
            self._count('affine_cached_solve_seconds_including_inner', elapsed)
            report['seconds_including_inner_solve'] = elapsed

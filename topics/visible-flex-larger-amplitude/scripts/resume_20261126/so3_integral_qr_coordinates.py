#!/usr/bin/env python3
"""Complete SO3 integral-norm coordinates through local banded square-root QR.

This is an explicit alternative numerical factorization of the full original
radial integral norm in the frozen 234ac and 7f operators. No Gram matrix,
ridge, jitter, rank truncation, removed free variable or changed damping is
used. The ordinary working factor/solve errors are NOT enclosed. No actual
failure of the original integral branch is assumed or claimed.

All construction and vector actions are scientific work and require the
public repository Actions environment. Source/AST review does not construct
an instance or execute a numerical fixture.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

import numpy as np
import scipy
from scipy.linalg import solve_banded
from scipy.linalg.lapack import dlartg


SCHEMA = 'complete-original-SO3-integral-norm-streamed-banded-QR-v1'
OBSERVED_SHA = '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d'
ORIGINAL_SOURCES = {
    '234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42':
        'complete-closed-so3-unit-meridian-with-core-lift-v1',
    '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf':
        'complete-independent-axisymmetric-so3-meridian-with-core-lift-v1',
}
BANDWIDTH = 5
GAUSS_ORDER = 6


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Complete integral QR coordinates belong in public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


class IntegralQRFactorizationError(ArithmeticError):
    """Actual numerical failure with a truthful finite diagnostic, no fallback."""
    def __init__(self, message, diagnostic):
        super().__init__(message)
        self.diagnostic = dict(diagnostic, complete=False,
            original_integral_failure_claimed=False,
            geometric_infeasibility_or_nonexistence_claimed=False,
            no_ridge_jitter_truncation_or_norm_substitution=True)


class RotationH2IntegralQRCoordinates:
    """API-compatible full free-variable lift and its exact algebraic transpose.

    For the same positive cell-width carrier h, six-point positive Gauss
    rows A define G=A.T@A in exact arithmetic. Column equilibration D is
    computed from A, and local Givens insertion factors A D = Q R without
    forming G. The declared maps are D R^-1(z/sigma) and
    R^-T(D v)/sigma, with original core and H scales unchanged.

    Only the original core + complete rotation + H layout is accepted.
    R696's additional radial profile and every other wrapper need their own
    complete source/layout contract; this class never relabels them.
    """
    def __init__(self, problem, *, radial_length=.05, angular_transition=24.,
                 original_coordinate_source=None, progress=None):
        require_actions()
        started = time.monotonic()
        for name, value in (('radial_length', radial_length), ('angular_transition', angular_transition)):
            if isinstance(value, bool) or not math.isfinite(float(value)) or value <= 0:
                raise ValueError('Use a finite positive explicit full integral-norm parameter: '+name)
        self.problem = q = problem
        self.size = q.free_size
        self.radial_length = float(radial_length)
        self.angular_transition = float(angular_transition)
        self.norm_kind = 'integral'
        self.counts = dict(lift_calls=0, transpose_calls=0)
        module = sys.modules.get(q.__class__.__module__)
        if module is None or not hasattr(module, '__file__'):
            raise ValueError('The complete actual original physical module is unavailable')
        actual_source = Path(module.__file__).resolve()
        requested_source = actual_source if original_coordinate_source is None else Path(original_coordinate_source).resolve()
        original_sha = sha(actual_source)
        if (original_sha not in ORIGINAL_SOURCES or sha(requested_source) != original_sha
                or q.model.get('source_sha256') != original_sha
                or q.model.get('schema') != ORIGINAL_SOURCES[original_sha]
                or canonical(q.model) != q.identity):
            raise ValueError('Bind one complete actual original 234ac/7f model; no wrapper source relabeling')
        original_class = getattr(module, 'RotationH2Coordinates', None)
        if (original_class is None
                or sha(original_class.__init__.__code__.co_filename) != original_sha
                or sha(original_class.lift.__code__.co_filename) != original_sha
                or sha(original_class.transpose.__code__.co_filename) != original_sha):
            raise ValueError('The complete original integral-coordinate definition is unavailable')
        if (not hasattr(q.context, 'observed')
                or sha(q.context.observed.__file__) != OBSERVED_SHA
                or q._hermite is not q.context.observed.hermite_weights
                or sha(q._hermite.__code__.co_filename) != OBSERVED_SHA):
            raise ValueError('Keep the complete original six-slot physical Hermite evaluation')
        if (not isinstance(q.J, (int, np.integer)) or q.J < 2
                or not isinstance(q.M, (int, np.integer)) or q.M < 1
                or not isinstance(q.K, (int, np.integer)) or not 0 <= q.K <= q.M):
            raise ValueError('Invalid complete original radial/angular/free-core dimensions')
        mesh = np.asarray(q.mesh)
        if (mesh.dtype != np.dtype('float64') or mesh.shape != (q.J,)
                or not np.isfinite(mesh).all()
                or q.model.get('mesh_sha256') != array_sha(mesh)):
            raise ValueError('Bind the actual complete literal mesh carrier')
        self.mesh = np.array(mesh, copy=True)
        self.widths = np.diff(self.mesh)
        if not np.isfinite(self.widths).all() or np.any(self.widths <= 0):
            raise ValueError('Every complete original cell must have a positive finite width carrier')
        expected_free = np.array([i for i in range(3*q.J)
            if i not in (0, 3*(q.J-1), 3*(q.J-1)+1)], dtype=np.int64)
        free = np.asarray(q.radial_free)
        if (free.dtype != np.dtype('int64') or not np.array_equal(free, expected_free)
                or q.core_size != q.M-q.K or q.n != 3*q.M+2
                or q.rotation_size != len(free)*q.n
                or q.free_size != q.core_size+q.rotation_size+1):
            raise ValueError('Preserve every original free core, rotation jet and final H slot; no extra-profile layout')
        self.free = np.array(free, copy=True)
        self.radial_count = count = len(free)
        # The structural half-bandwidth is at most five. A smaller complete
        # space still keeps every free slot and uses its actual matrix size.
        self.bandwidth = bandwidth = min(BANDWIDTH, count-1)
        self.lookup = np.full(3*q.J, -1, dtype=np.int64)
        self.lookup[self.free] = np.arange(count, dtype=np.int64)
        frequencies = 2*np.arange(1, q.M+1, dtype=float)
        if (not np.array_equal(q.freq, frequencies)
                or not np.array_equal(q.qfreq, 1-frequencies**2)):
            raise ValueError('The complete original angular/core frequencies changed')
        odd = 2*np.arange(q.M+1)+1
        modes = np.r_[odd, odd, q.freq]
        self.sigma = np.sqrt(1+(modes/self.angular_transition)**2)
        self.core_scale = 1/np.maximum(1., np.abs(q.qfreq[q.K:]))
        if (self.sigma.shape != (q.n,) or self.core_scale.shape != (q.core_size,)
                or not np.isfinite(self.sigma).all() or np.any(self.sigma <= 0)
                or not np.isfinite(self.core_scale).all() or np.any(self.core_scale <= 0)):
            raise ValueError('Keep all original finite positive angular/core scales')
        roots, weights = np.polynomial.legendre.leggauss(GAUSS_ORDER)
        self.gauss_u, self.gauss_w = (roots+1)/2, weights/2
        if (not np.isfinite(self.gauss_u).all() or not np.isfinite(self.gauss_w).all()
                or np.any(self.gauss_u <= 0) or np.any(self.gauss_u >= 1)
                or np.any(self.gauss_w <= 0)):
            raise ArithmeticError('The complete six-point working Gauss rule must remain positive and interior')
        self.derivative_scales = np.array([1., self.radial_length, self.radial_length**2])
        if not np.isfinite(self.derivative_scales).all() or np.any(self.derivative_scales <= 0):
            raise ArithmeticError('The literal derivative-scale carrier is not finite positive')
        self._progress = progress
        column_norms = np.zeros(count)
        input_rows = 0
        first_started = time.monotonic()
        for cell in range(q.J-1):
            for _, _, indices, row in self._cell_rows(cell):
                input_rows += 1
                for index, value in zip(indices, row):
                    # Streaming nrm2 through hypot avoids squaring the large
                    # derivatives of a short quintic cell to form a Gram.
                    column_norms[index] = math.hypot(float(column_norms[index]), float(value))
            self._notify('complete_column_norms', cell, first_started)
        expected_rows = (q.J-1)*GAUSS_ORDER*3
        if (input_rows != expected_rows or not np.isfinite(column_norms).all()
                or np.any(column_norms <= 0)):
            raise IntegralQRFactorizationError('Every original radial column needs a finite strictly positive actual norm',
                dict(phase='column_norms', input_rows=input_rows, expected_rows=expected_rows,
                    finite=bool(np.isfinite(column_norms).all()),
                    nonpositive_columns=int(np.count_nonzero(column_norms <= 0))))
        with np.errstate(over='raise', divide='raise', invalid='raise', under='ignore'):
            self.equilibration = 1/column_norms
        if not np.isfinite(self.equilibration).all() or np.any(self.equilibration <= 0):
            raise IntegralQRFactorizationError('No representable positive complete column scaling',
                dict(phase='column_scaling', radial_columns=count))
        self.column_norms = column_norms
        first_seconds = time.monotonic()-first_started
        row_band = np.zeros((bandwidth+1, count))
        rotations, zero_input_entries, processed_rows = 0, 0, 0
        maximum_inserted_column = -1
        second_started = time.monotonic()
        for cell in range(q.J-1):
            for gauss_index, derivative_order, indices, values in self._cell_rows(cell):
                if not len(indices):
                    raise ValueError('No original cell may silently lose all free Hermite columns')
                start, last = int(indices[0]), int(indices[-1])
                if last-start > bandwidth or last < maximum_inserted_column:
                    raise ValueError('The complete original cell/slot order cannot be represented by this local band proof')
                maximum_inserted_column = last
                row = np.zeros(last-start+1)
                row[indices-start] = values*self.equilibration[indices]
                if not np.isfinite(row).all():
                    raise IntegralQRFactorizationError('Nonfinite actual scaled complete Hermite row',
                        dict(phase='row_scaling', cell=cell, gauss_index=gauss_index,
                            derivative_order=derivative_order))
                for j in range(start, last+1):
                    offset = j-start
                    # Earlier cells have not introduced columns beyond last.
                    # Check rather than silently trim any unexpected nonzero
                    # existing R entry outside the current local front.
                    if last-j < bandwidth and np.any(row_band[last-j+1:, j] != 0):
                        raise IntegralQRFactorizationError('An existing nonzero factor entry lies outside the complete current front',
                            dict(phase='band_support', cell=cell, column=j, current_last=last))
                    g = float(row[offset])
                    if g == 0.:
                        zero_input_entries += 1
                        continue
                    cs, sn, r = dlartg(float(row_band[0, j]), g)
                    if not all(math.isfinite(float(v)) for v in (cs, sn, r)):
                        raise IntegralQRFactorizationError('DLARTG returned a nonfinite complete plane rotation',
                            dict(phase='givens', cell=cell, gauss_index=gauss_index,
                                derivative_order=derivative_order, column=j))
                    length = last-j+1
                    old_factor = row_band[:length, j].copy()
                    old_row = row[offset:].copy()
                    row_band[:length, j] = cs*old_factor+sn*old_row
                    row[offset:] = -sn*old_factor+cs*old_row
                    # DLARTG owns the scaled diagonal computation. This exact
                    # eliminated slot is not a rank/entry truncation rule.
                    row_band[0, j] = r
                    row[offset] = 0.
                    if (not np.isfinite(row_band[:length, j]).all()
                            or not np.isfinite(row[offset:]).all()):
                        raise IntegralQRFactorizationError('Nonfinite ordinary complete local QR update',
                            dict(phase='givens_update', cell=cell, column=j))
                    rotations += 1
                if np.any(row != 0):
                    raise IntegralQRFactorizationError('A complete actual inserted row was not fully eliminated',
                        dict(phase='row_elimination', cell=cell, gauss_index=gauss_index,
                            derivative_order=derivative_order))
                processed_rows += 1
            self._notify('complete_banded_QR', cell, second_started)
        if processed_rows != expected_rows or not np.isfinite(row_band).all():
            raise IntegralQRFactorizationError('The actual complete QR did not process every positive evaluation row',
                dict(phase='complete_factor', processed_rows=processed_rows, expected_rows=expected_rows))
        signs = np.ones(count)
        negative = row_band[0] < 0
        signs[negative] = -1.
        row_band[:, negative] *= -1.
        if np.any(row_band[0] <= 0):
            raise IntegralQRFactorizationError('The complete working upper factor has a zero diagonal; no rank truncation or ridge is substituted',
                dict(phase='factor_diagonal', nonpositive_diagonals=int(np.count_nonzero(row_band[0] <= 0))))
        # row_band[k,j] = R[j,j+k]. This same layout is the lower-band
        # representation of R.T. The upper-band conversion uses SciPy's
        # ab[u+i-j,j] = A[i,j] convention, with u=bandwidth (at most five).
        self.lower = row_band
        self.upper = np.zeros_like(row_band)
        for offset in range(bandwidth+1):
            self.upper[bandwidth-offset, offset:] = row_band[offset, :count-offset]
        second_seconds = time.monotonic()-second_started
        definition = dict(schema='complete-original-SO3-radial-integral-norm-definition-v1',
            norm='sum_modes sigma_k^2 integral(omega_k^2+ell^2 omega_ks^2+ell^4 omega_kss^2) ds + sum_free_core((1-nu^2)dc)^2+dH^2',
            radial_length_hex=self.radial_length.hex(), angular_transition_hex=self.angular_transition.hex(),
            M=int(q.M), J=int(q.J), K=int(q.K), angular_channels=int(q.n),
            free_original_variables=int(q.free_size), radial_free_slots_sha256=array_sha(self.free),
            mesh_carrier_sha256=array_sha(self.mesh), width_carrier_sha256=array_sha(self.widths),
            angular_frequencies_sha256=array_sha(modes),
            positive_width_parameters='literal positive words np.diff(q.mesh); subtraction error relative to exact symbolic nodes is not certified',
            polynomial='complete shared quintic endpoint value/physical-first/physical-second jets on every positive width parameter',
            angular_weight='sigma(k)^2 = 1+(k/angular_transition)^2; x/y odd, z even',
            every_original_free_core_rotation_and_H_retained=True,
            radial_profile_extra_variables_supported=False,
            exact_positive_Gauss_order=GAUSS_ORDER, maximum_polynomial_product_degree=10,
            full_mass_first_and_second_derivative_terms=True,
            symbolic_physical_mesh_equivalence_or_error_certified=False)
        self.record = dict(schema=SCHEMA, source_sha256=sha(__file__), norm_kind='integral',
            radial_length=self.radial_length, angular_transition=self.angular_transition,
            norm=definition['norm'], mathematical_norm_definition=definition,
            mathematical_norm_definition_sha256=canonical(definition),
            original_coordinate_source_sha256=original_sha,
            original_complete_field_model_identity_sha256=q.identity,
            complete_Hermite_source_sha256=OBSERVED_SHA,
            same_original_integral_norm_in_exact_arithmetic=True,
            original_band_Gram_or_normal_equations_formed=False,
            numerical_factorization='streamed local real Givens QR of complete A D; row signs fixed to positive R diagonal',
            radial_gauss_order=GAUSS_ORDER, radial_bandwidth=bandwidth,
            maximum_structural_radial_bandwidth=BANDWIDTH,
            complete_evaluation_rows=expected_rows, radial_columns=count,
            row_order='cell, Gauss node, derivative order 0/1/2; every original row processed',
            coefficient_row='sqrt(h)*sqrt(w)*ell^r*Hermite_r, restricted only to originally free slots',
            column_scaling='D_j = 1 / streaming_hypot_norm(A[:,j]); no squared Gram diagonal',
            row_band_storage='lower[k,j]=R[j,j+k]; upper[bandwidth-k,j+k]=lower[k,j]',
            lift_formula='core_scale*zcore; D*solve(R,zrot/sigma); zH',
            transpose_formula='core_scale*vcore; solve(R.T,D*vrot)/sigma; vH',
            all_original_free_core_and_height_retained=True,
            all_complete_rotation_jets_retained=True,
            rotation_gauge_removed=False, positive_damping_controls_redundant_directions=True,
            damping_rescaled_or_selected_by_this_factor=False,
            original_q_physical_mother_norm_claimed_unchanged=False,
            no_ridge_jitter_pseudoinverse_rank_truncation_or_norm_fallback=True,
            original_integral_failure_observed_or_claimed=False,
            exact_radial_integral_is_the_declared_norm=True,
            actual_working_factor_or_solve_error_enclosed=False,
            working_quadrature_Hermite_width_and_scale_errors_enclosed=False,
            numpy_version=np.__version__, scipy_version=scipy.__version__,
            gauss_node_sha256=array_sha(self.gauss_u), gauss_weight_sha256=array_sha(self.gauss_w),
            column_norm_sha256=array_sha(column_norms),
            diagonal_equilibration_sha256=array_sha(self.equilibration),
            lower_factor_sha256=array_sha(self.lower), upper_factor_sha256=array_sha(self.upper),
            positive_diagonal_signs_sha256=array_sha(signs),
            angular_scale_sha256=array_sha(self.sigma), core_scale_sha256=array_sha(self.core_scale))
        self.record['norm_identity_sha256'] = canonical(self.record)
        self.factorization = dict(complete=True, processed_rows=processed_rows,
            full_radial_columns=count, actual_Givens_rotations=rotations,
            exact_zero_eliminand_skips=zero_input_entries,
            negative_diagonal_row_sign_changes=int(np.count_nonzero(negative)),
            column_norm_preparation_seconds=first_seconds, actual_QR_seconds=second_seconds,
            complete_preparation_seconds=time.monotonic()-started,
            minimum_positive_factor_diagonal=float(np.min(self.lower[0])),
            maximum_factor_diagonal=float(np.max(self.lower[0])),
            factor_bytes=int(self.lower.nbytes+self.upper.nbytes),
            dense_or_rectangular_evaluation_matrix_bytes=0,
            original_Gram_matrix_bytes=0, transient_front_maximum_entries=bandwidth+1,
            actual_factor_condition_number_not_estimated=True,
            numerical_rank_failure_does_not_prove_exact_singular_norm=True,
            rigorous_factor_or_inverse_errors_certified=False)
        for value in (self.mesh, self.widths, self.free, self.lookup, self.sigma, self.core_scale,
                self.gauss_u, self.gauss_w, self.derivative_scales, self.equilibration,
                self.column_norms, self.lower, self.upper):
            value.setflags(write=False)

    def _notify(self, phase, cell, started):
        if self._progress is not None and ((cell+1)%128 == 0 or cell+1 == self.problem.J-1):
            self._progress(dict(phase=phase, completed_cells=cell+1,
                total_cells=self.problem.J-1, actual_seconds=time.monotonic()-started))

    def _cell_rows(self, cell):
        width = float(self.widths[cell])
        slots = np.arange(3*cell, 3*cell+6, dtype=np.int64)
        local_indices = self.lookup[slots]
        keep = local_indices >= 0
        indices = local_indices[keep]
        for gauss_index, (u, weight) in enumerate(zip(self.gauss_u, self.gauss_w)):
            W = np.asarray(self.problem._hermite(width, float(u)), dtype=np.float64)
            if W.shape != (3, 6) or not np.isfinite(W).all():
                raise IntegralQRFactorizationError('The actual complete physical Hermite row is undefined',
                    dict(phase='Hermite_rows', cell=cell, gauss_index=gauss_index))
            scalar = math.sqrt(width)*math.sqrt(float(weight))
            for derivative_order in range(3):
                values = (scalar*self.derivative_scales[derivative_order])*W[derivative_order, keep]
                if not np.isfinite(values).all():
                    raise IntegralQRFactorizationError('The actual positive complete evaluation row is nonfinite',
                        dict(phase='evaluation_rows', cell=cell, gauss_index=gauss_index,
                            derivative_order=derivative_order))
                yield gauss_index, derivative_order, indices, values

    def _vector(self, value):
        value = np.asarray(value, dtype=np.float64)
        if value.shape != (self.size,) or not np.isfinite(value).all():
            raise ValueError('Every action consumes the complete finite original free-variable vector')
        return value

    def lift(self, value):
        require_actions()
        value = self._vector(value)
        q = self.problem
        result = np.empty_like(value)
        result[:q.core_size] = value[:q.core_size]*self.core_scale
        rhs = value[q.core_size:-1].reshape(self.radial_count, q.n)/self.sigma[None]
        result[q.core_size:-1] = (self.equilibration[:, None]*solve_banded(
            (0, self.bandwidth), self.upper, rhs, check_finite=False)).ravel()
        result[-1] = value[-1]
        self.counts['lift_calls'] += 1
        if not np.isfinite(result).all():
            raise FloatingPointError('The complete ordinary upper-band QR coordinate solve is nonfinite')
        return result

    def transpose(self, value):
        require_actions()
        value = self._vector(value)
        q = self.problem
        result = np.empty_like(value)
        result[:q.core_size] = value[:q.core_size]*self.core_scale
        rhs = value[q.core_size:-1].reshape(self.radial_count, q.n)
        result[q.core_size:-1] = (solve_banded((self.bandwidth, 0), self.lower,
            self.equilibration[:, None]*rhs, check_finite=False)/self.sigma[None]).ravel()
        result[-1] = value[-1]
        self.counts['transpose_calls'] += 1
        if not np.isfinite(result).all():
            raise FloatingPointError('The complete ordinary transpose-band QR coordinate solve is nonfinite')
        return result

    def metadata(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__),
            coordinate_norm=dict(self.record), factorization=dict(self.factorization),
            actual_coordinate_actions=dict(self.counts),
            source_guard_for_a_later_complete_driver_must_explicitly_allow_this_new_coordinate_module=True,
            inherited_physical_solver_or_geometry_acceptance=False,
            raw_F_J_or_scientific_fixture_evaluated_by_this_module=False)

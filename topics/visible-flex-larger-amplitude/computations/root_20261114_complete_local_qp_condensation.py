#!/usr/bin/env python3
"""Condense one complete damped square-root model to its exact local support.

Actions only. Consume a completed frozen RegularizedBlockQR without rebuilding
J or closing the borrowed factor. Reverse physical fronts retain every affine
and global column; core columns are then eliminated before local QR.
The actual recovered full vector is rechecked by the original factor.solve_H.
No normal Schur subtraction, outside-zero constraint, or QP acceptance is used.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import os
from pathlib import Path
import resource
import sys
import time

import numpy as np
import scipy
from scipy.linalg.lapack import dgeqrf, dormqr, dtrtrs

HERE = Path(__file__).resolve().parent
FACTOR_NAME = 'exact_20261114_regularized_block_qr.py'
FACTOR_SHA = '596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722'
SCHEMA = 'complete-original-H-local-support-square-root-condensation-v1'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific condensation is only authorized in the public repository Actions')
    if sys.byteorder != 'little':
        raise RuntimeError('Explicit original little-endian binary64 storage is required')


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for raw in iter(lambda: stream.read(1 << 20), b''):
            h.update(raw)
    return h.hexdigest()


def byte_chunks(value):
    a = np.asarray(value)
    if not a.size:
        return
    if a.flags.c_contiguous:
        raw = memoryview(a).cast('B')
        for start in range(0, len(raw), 1 << 20):
            yield raw[start:start+(1 << 20)]
    else:
        for row in a:
            yield np.ascontiguousarray(row).tobytes(order='C')


def identity(value):
    a = np.asarray(value)
    h = hashlib.sha256()
    for raw in byte_chunks(a):
        h.update(raw)
    return dict(shape=list(a.shape), dtype=a.dtype.str, order='C',
                bytes=int(a.size*a.dtype.itemsize), raw_sha256=h.hexdigest())


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def norm(value):
    a = np.asarray(value)
    maximum = float(np.max(np.abs(a))) if a.size else 0.
    if maximum == 0. or not np.isfinite(maximum):
        return maximum
    with np.errstate(over='ignore', invalid='ignore'):
        return float(maximum*np.sqrt(np.sum((a/maximum)**2)))


def half_square(value):
    with np.errstate(over='ignore', invalid='ignore'):
        return float(np.float64(value)*np.float64(value)*np.float64(0.5))


def maximum_abs(value):
    a = np.asarray(value)
    return float(np.max(np.abs(a))) if a.size else 0.


def json_safe(value):
    if isinstance(value, dict):
        return {str(k):json_safe(v) for k,v in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_safe(v) for v in value]
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else dict(nonfinite_display=repr(float(value)))
    return value


class CondensationDeadline(RuntimeError):
    pass


class CondensationFailure(RuntimeError):
    def __init__(self, message, report):
        super().__init__(message)
        self.report = report


class CondensedModel:
    """The support is a contiguous run of whole physical nodes plus all controls.

    local_indices use original scaled-z coordinates, in ascending order.
    All free-core coordinates are exterior and are conditionally minimized.
    A completed live frozen factor is borrowed, never re-factorized or closed.

    Public methods return numpy arrays, including multi-RHS local H actions and
    solves. recover() returns the actual original full vector; its local block
    is not overwritten. Original readback diagnostics are in last_recovery.
    """

    def __init__(self, factor, original_g, local_indices, *,
                 deadline, output_directory=None):
        require_actions()
        self.factor = factor
        self.complete = False
        self.closed = False
        self._lwork = {}
        self._arrays = {}
        self._report = dict(schema=SCHEMA, source_sha256=file_sha(__file__),
            frozen_factor_source_sha256=FACTOR_SHA, status='binding',
            no_new_J=True, no_new_ODE_or_boundary=True,
            normal_Schur_matrix_not_formed=True,
            exterior_variables_not_fixed_to_zero=True,
            full_affine_column_retained=True, pure_global_root_retained=True,
            no_QP_optimality_claim=True, nonlinear_accepted=False,
            local_hessian_is_rounded_square_root_model=True,
            exact_original_H_identity_claimed_only_in_exact_arithmetic=True,
            all_final_constraints_must_use_actual_recovered_full_vector=True,
            borrowed_factor_is_never_closed=True, arrays_artifact_only=True,
            local_H_action_calls=0, local_H_action_rhs_columns=0,
            local_H_solve_calls=0, local_H_solve_rhs_columns=0,
            local_H_action_seconds=0., local_H_solve_seconds=0.,
            local_H_solve_mandatory_residual_actions=0,
            recover_calls=0, original_complete_recovery_solves=0,
            completed_reverse_fronts=0, NumPy=np.__version__, SciPy=scipy.__version__)
        self.last_recovery = None
        self.last_local_solve = None
        self.storage = None
        self._sequence = 0
        started = time.monotonic()
        try:
            source = HERE/FACTOR_NAME
            if file_sha(source) != FACTOR_SHA:
                raise ValueError('The frozen complete square-root source changed')
            base = None
            for cls in type(factor).__mro__:
                if cls.__name__ == 'RegularizedBlockQR' and file_sha(inspect.getfile(cls)) == FACTOR_SHA:
                    base = cls
                    break
            if base is None:
                raise ValueError('Borrow an actual frozen complete RegularizedBlockQR instance')
            if getattr(factor.solve_H, '__func__', None) is not base.solve_H:
                raise ValueError('Keep the frozen complete solve_H and its original readback')
            if not factor.complete or factor.closed:
                raise ValueError('The borrowed factor must already be complete and open')
            self.deadline = float(deadline)
            if not np.isfinite(self.deadline):
                raise ValueError('Supply an explicit finite absolute monotonic deadline')
            self.deadline = min(self.deadline, float(factor.deadline))
            self.n, self.N = int(factor.n), int(factor.N)
            self.free, self.k, self.d = int(factor.free), int(factor.k), int(factor.d)
            self.physical, self.size = int(factor.physical), int(factor.size)
            self.lambda_ = float(factor.lambda_)
            self.lambda_squared = float(factor.lambda_squared)
            if self.d != self.free+self.k or self.size != self.N*self.n+self.d:
                raise ValueError('Complete physical/global factor dimensions are inconsistent')
            self._check_deadline()
            self.g = self._full_vector(original_g, 'original complete g', copy=True)
            self.g.flags.writeable = False
            self.C = self._full_vector(factor.C, 'actual factor column scale', copy=True)
            if np.any(self.C <= 0):
                raise ValueError('The factor column scale must remain finite and positive')
            self.C.flags.writeable = False
            self._bind_support(local_indices)
            if output_directory is not None:
                self.storage = Path(output_directory).resolve()
                self.storage.mkdir(parents=True, exist_ok=False)
            factor_report = factor.report
            self._report.update(
                dimension=self.size, physical_nodes=self.N, physical_block=self.n,
                free_core=self.free, scalar_controls=self.k, global_border=self.d,
                first_retained_physical_node=self.left+1,
                last_retained_physical_node=self.right+1,
                retained_physical_nodes=self.retained,
                local_dimension=self.local_size,
                left_exterior_physical_nodes=self.left,
                right_exterior_physical_nodes=self.N-self.right-1,
                exterior_core_dimension=self.free,
                complete_B_support_is_callers_verified_contract=True,
                no_B_row_is_truncated_or_evaluated_by_this_library=True,
                original_gradient=identity(self.g),
                original_gradient_is_callers_same_A_transpose_b_contract=True,
                original_g_is_not_replaced_by_a_computed_center=True,
                factor_column_scale=identity(self.C),
                original_local_indices=identity(self.local_indices),
                damping=self.lambda_, damping_squared=self.lambda_squared,
                original_factor_input_arrays=factor.input_hashes,
                original_factor_input_identity_sha256=canonical_sha(factor.input_identity),
                original_factor_array_identities=factor_report['factor_arrays'],
                factor_source_sha256=factor_report['source_sha256'],
                deadline=self.deadline,
                memory_budget=dict(
                    borrowed_factor_bytes=sum(a.nbytes for a in factor.factor_arrays.values()),
                    complete_affine_column_bytes=self.size*8,
                    reverse_front_bytes=2*self.n*(2*self.n+self.d+1)*8,
                    central_with_affine_bytes=self.central_size*(self.central_size+1)*8,
                    local_root_bytes=self.local_size*self.local_size*8,
                    QR_workspace_and_transient_copies_are_additional=True,
                    no_dense_full_H_or_dual_Gram=True))
            self._event('binding-complete')
            self._report['original_input_recheck_before_seconds'] = factor._check_inputs()
            self._factor_snapshot = self._check_factor_arrays()
            if identity(self.C) != factor_report['column_preconditioner']:
                raise ValueError('The current factor C differs from its completed producer identity')
            self._save_array('original-g', self.g, 'Complete caller-supplied original g=A.T b')
            self._save_array('local-indices', self.local_indices, 'Complete original-coordinate inequality support')
            self._check_deadline()
            affine = self._complete_affine()
            self._save_array('complete-affine-column', affine,
                             'Full R_C.T h=g/C solution; left and pure-global contributions retained')
            reverse_start = time.monotonic()
            U = self._D(self.N-1)
            V = self._T(self.N-1)
            a = affine[(self.N-1)*self.n:self.N*self.n].copy()
            for i in range(self.N-1, self.right, -1):
                self._check_deadline()
                n, d = self.n, self.d
                front = np.zeros((2*n, 2*n+d+1), dtype='<f8', order='F')
                front[:n, :n] = self._S(i-1)
                front[n:, :n] = U
                front[:n, n:2*n] = self._D(i-1)
                front[:n, 2*n:2*n+d] = self._T(i-1)
                front[n:, 2*n:2*n+d] = V
                front[:n, -1] = affine[(i-1)*n:i*n]
                front[n:, -1] = a
                rotated = self._qr_prefix(front, n, 'right-node-'+str(i+1))
                # The upper n rows are the conditionally minimized square.
                # Every remaining variable and the affine column undergoes Q.T.
                U = np.array(rotated[n:, n:2*n], dtype='<f8', order='C', copy=True)
                V = np.array(rotated[n:, 2*n:2*n+d], dtype='<f8', order='C', copy=True)
                a = rotated[n:, -1].copy()
                self._report['completed_reverse_fronts'] += 1
                if self._report['completed_reverse_fronts'] % 16 == 0 or i == self.right+1:
                    self._event('right-exterior', remaining_node=i,
                                seconds=time.monotonic()-reverse_start)
            self._report['reverse_front_seconds'] = time.monotonic()-reverse_start
            self._check_deadline()
            central = self._central_front(affine, U, V, a)
            self._report['central_affine_front'] = identity(central)
            core_start = time.monotonic()
            if self.free:
                core_rotated = self._qr_prefix(central, self.free, 'complete-core109')
                remainder = np.array(core_rotated[self.free:, self.free:],
                                     dtype='<f8', order='F', copy=True)
            else:
                remainder = central
            del central
            if self.free:
                del core_rotated
            self._report['core_elimination_seconds'] = time.monotonic()-core_start
            self._check_deadline()
            local_start = time.monotonic()
            rotated = self._qr_prefix(remainder, self.local_size, 'complete-local-root')
            del remainder
            self.root = np.asarray(np.triu(rotated[:, :self.local_size]), dtype='<f8', order='C')
            self.affine = np.array(rotated[:, -1], dtype='<f8', order='C', copy=True)
            del rotated
            self._report['local_QR_seconds'] = time.monotonic()-local_start
            self.local_gradient = self.root.T @ self.affine
            self.local_center = self._triangular(self.root, -self.affine, transpose=False)
            if (not np.isfinite(self.local_gradient).all() or
                    not np.isfinite(self.local_center).all()):
                raise FloatingPointError('The complete condensed affine model is nonfinite')
            local_center_residual = self._local_H(self.local_center)+self.local_gradient
            self._report.update(
                local_root=identity(self.root), local_affine=identity(self.affine),
                local_gradient=identity(self.local_gradient), local_center=identity(self.local_center),
                local_root_diagonal_min_abs=float(np.min(np.abs(np.diag(self.root)))),
                local_root_diagonal_max_abs=maximum_abs(np.diag(self.root)),
                local_center_condensed_gradient_L2=norm(local_center_residual),
                local_center_condensed_gradient_Linf=maximum_abs(local_center_residual),
                local_center_not_claimed_exact_original_H_center=True,
                affine_constant_components=dict(
                    original_f0_is_not_supplied=True,
                    full_affine_half_norm_squared=half_square(norm(affine)),
                    retained_local_affine_half_norm_squared=half_square(norm(self.affine)),
                    original_f0_minus_full_affine_half_norm_is_preserved_constant=True,
                    absolute_constant_difference_not_required_for_model_comparisons=True,
                    floating_constants_are_diagnostics_not_validated_bounds=True))
            self._save_array('local-root', self.root, 'Upper square root of the complete condensed finite model')
            self._save_array('local-affine', self.affine, 'Affine column after all physical/core orthogonal eliminations')
            self._save_array('local-gradient', self.local_gradient, 'Rhat.T hhat from the original complete g')
            self._save_array('local-center', self.local_center, 'Local finite root center; not an exact original-H assertion')
            self.root.flags.writeable = False
            self.affine.flags.writeable = False
            self.local_gradient.flags.writeable = False
            self.local_center.flags.writeable = False
            self._report['original_input_recheck_after_seconds'] = factor._check_inputs()
            if self._check_factor_arrays() != self._factor_snapshot:
                raise ValueError('The borrowed complete factor changed during condensation')
            if identity(factor.C) != identity(self.C):
                raise ValueError('The borrowed factor column scale changed during condensation')
            self._report['model_identity_sha256'] = canonical_sha(dict(
                source_sha256=self._report['source_sha256'], factor_source_sha256=FACTOR_SHA,
                original_factor_input_arrays=factor.input_hashes,
                actual_complete_factor_arrays=self._factor_snapshot,
                original_g=identity(self.g), column_scale=identity(self.C),
                original_local_indices=identity(self.local_indices),
                local_root=identity(self.root), local_affine=identity(self.affine),
                local_gradient=identity(self.local_gradient), damping=self.lambda_))
            self.complete = True
            self._report.update(status='complete', complete=True,
                elapsed_seconds=time.monotonic()-started,
                maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                completed_after_declared_deadline=bool(time.monotonic() >= self.deadline))
            self._event('complete')
            self._write_status()
        except Exception as error:
            self._report.update(status='failed', complete=False, actual_error=repr(error),
                elapsed_seconds=time.monotonic()-started,
                maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            self._write_status()
            raise CondensationFailure(str(error), self.report) from error

    def _full_vector(self, value, label, copy=False):
        a = np.asarray(value)
        if a.dtype != np.dtype('<f8') or a.shape != (self.size,) or not np.isfinite(a).all():
            raise ValueError(label+' must preserve all original finite binary64 coordinates')
        return np.array(a, dtype='<f8', copy=True) if copy else a

    def _bind_support(self, local_indices):
        source = np.asarray(local_indices)
        if source.ndim != 1 or source.dtype.kind not in ('i', 'u'):
            raise ValueError('Original local coordinate indices must be a complete integer vector')
        idx = np.asarray(source, dtype=np.int64)
        if (idx.size == 0 or np.any(idx < 0) or np.any(idx >= self.size) or
                np.any(idx[1:] <= idx[:-1])):
            raise ValueError('Use unique ascending original-coordinate local indices')
        physical = idx[idx < self.physical]
        global_part = idx[idx >= self.physical]
        if physical.size == 0 or physical.size % self.n:
            raise ValueError('Retain a nonempty run of whole physical nodes')
        first, last = int(physical[0]), int(physical[-1])
        if first % self.n or (last+1) % self.n:
            raise ValueError('The local physical support must have full node boundaries')
        if not np.array_equal(physical, np.arange(first, last+1, dtype=np.int64)):
            raise ValueError('The physical support must be one complete contiguous chain run')
        expected_controls = np.arange(self.physical+self.free, self.size, dtype=np.int64)
        if not np.array_equal(global_part, expected_controls):
            raise ValueError('Retain every scalar control and eliminate every free-core coordinate')
        self.left, self.right = first//self.n, last//self.n
        self.retained = self.right-self.left+1
        self.local_size = physical.size+self.k
        self.central_size = self.retained*self.n+self.d
        self.local_indices = idx.copy()
        self.local_indices.flags.writeable = False
        expected = np.concatenate((np.arange(first, last+1, dtype=np.int64), expected_controls))
        if not np.array_equal(self.local_indices, expected):
            raise ValueError('The original support ordering changed')

    def _check_factor_arrays(self):
        expected = self.factor.report['factor_arrays']
        result = {}
        started = time.monotonic()
        names = {'diagonal':self.factor.diagonal, 'next-physical':self.factor.upper,
                 'global-border':self.factor.border, 'global-diagonal':self.factor.global_diagonal}
        for name, value in names.items():
            actual = identity(value)
            for key in ('shape', 'dtype', 'order', 'bytes', 'raw_sha256'):
                if actual[key] != expected[name][key]:
                    raise ValueError('The completed borrowed factor byte identity changed: '+name)
            result[name] = actual
        self._report['factor_byte_rechecks'] = self._report.get('factor_byte_rechecks', 0)+1
        self._report['factor_byte_recheck_seconds'] = self._report.get('factor_byte_recheck_seconds', 0.)+time.monotonic()-started
        return result

    def _check_deadline(self):
        if time.monotonic() >= min(self.deadline, float(self.factor.deadline)):
            raise CondensationDeadline('Condensation discretionary work deadline reached between complete operations')
        if self.factor.closed or not self.factor.complete:
            raise RuntimeError('The borrowed factor is no longer complete and open')

    def _check_open(self):
        require_actions()
        if not self.complete or self.closed:
            raise RuntimeError('A complete open condensed model is required')
        self._check_deadline()

    def _D(self, i):
        a = self.factor.diagonal[i]*self.C[i*self.n:(i+1)*self.n][None, :]
        if not np.isfinite(a).all():
            raise FloatingPointError('Folding C into a complete physical diagonal is nonfinite')
        return a

    def _S(self, i):
        a = self.factor.upper[i]*self.C[(i+1)*self.n:(i+2)*self.n][None, :]
        if not np.isfinite(a).all():
            raise FloatingPointError('Folding C into a complete physical connection is nonfinite')
        return a

    def _T(self, i):
        a = self.factor.border[i]*self.C[self.physical:][None, :]
        if not np.isfinite(a).all():
            raise FloatingPointError('Folding C into a complete global border is nonfinite')
        return a

    def _complete_affine(self):
        before = time.monotonic()
        n, N = self.n, self.N
        with np.errstate(over='ignore', under='ignore', divide='ignore', invalid='ignore'):
            scaled_g = self.g/self.C
        if not np.isfinite(scaled_g).all():
            raise FloatingPointError('The complete original g/C is nonfinite')
        h = np.empty(self.size, dtype='<f8')
        hp = h[:self.physical].reshape(N, n)
        source = scaled_g[:self.physical].reshape(N, n)
        global_rhs = scaled_g[self.physical:].copy()
        for i in range(N):
            self._check_deadline()
            value = source[i].copy()
            if i:
                value -= self.factor.upper[i-1].T @ hp[i-1]
            hp[i] = self._triangular(self.factor.diagonal[i], value, transpose=True)
            global_rhs -= self.factor.border[i].T @ hp[i]
        h[self.physical:] = self._triangular(self.factor.global_diagonal, global_rhs, transpose=True)
        # Read back the finite affine relation in original z coordinates.
        recovered = np.empty(self.size, dtype='<f8')
        physical = recovered[:self.physical].reshape(N, n)
        border_value = self.factor.global_diagonal.T @ h[self.physical:]
        for i in range(N):
            physical[i] = self.factor.diagonal[i].T @ hp[i]
            if i:
                physical[i] += self.factor.upper[i-1].T @ hp[i-1]
            border_value += self.factor.border[i].T @ hp[i]
        recovered[self.physical:] = border_value
        recovered *= self.C
        error = recovered-self.g
        if not np.isfinite(h).all() or not np.isfinite(error).all():
            raise FloatingPointError('The full affine construction/readback is nonfinite')
        self._report['complete_affine_construction'] = dict(
            equation='R_C.T h = original_g/C; Rbar=R_C C',
            full_affine_identity=identity(h), recovered_linear_term=identity(recovered),
            original_linear_term_error=identity(error),
            original_linear_term_error_L2=norm(error), original_linear_term_error_Linf=maximum_abs(error),
            full_original_g_L2=norm(self.g), seconds=time.monotonic()-before,
            no_computed_center_used_to_delete_original_gradient=True,
            finite_factor_linear_term_readback_not_exact_original_H_certificate=True)
        self._save_array('affine-original-linear-term-error', error,
                         'Actual (R_C C).T h minus supplied original g')
        return h

    def _central_front(self, affine, U, V, last_affine):
        n, d, free = self.n, self.d, self.free
        length = self.retained*n
        front = np.zeros((self.central_size, self.central_size+1), dtype='<f8', order='F')
        for j, i in enumerate(range(self.left, self.right)):
            rows = slice(j*n, (j+1)*n)
            physical = slice(free+j*n, free+(j+1)*n)
            following = slice(free+(j+1)*n, free+(j+2)*n)
            T = self._T(i)
            front[rows, :free] = T[:, :free]
            front[rows, physical] = self._D(i)
            front[rows, following] = self._S(i)
            front[rows, free+length:free+length+self.k] = T[:, free:]
            front[rows, -1] = affine[i*n:(i+1)*n]
        j = self.retained-1
        rows = slice(j*n, (j+1)*n)
        front[rows, :free] = V[:, :free]
        front[rows, free+j*n:free+(j+1)*n] = U
        front[rows, free+length:free+length+self.k] = V[:, free:]
        front[rows, -1] = last_affine
        global_root = self.factor.global_diagonal*self.C[self.physical:][None, :]
        front[length:, :free] = global_root[:, :free]
        front[length:, free+length:free+length+self.k] = global_root[:, free:]
        front[length:, -1] = affine[self.physical:]
        if not np.isfinite(front).all():
            raise FloatingPointError('The full central affine root is nonfinite')
        self._report['central_order'] = dict(
            rows='retained physical chain, compressed right endpoint, full pure-global root',
            columns='all free core first, all retained physical nodes in original order, all controls, affine',
            pure_global_rows=d, pure_global_affine_kept=True,
            core_eliminated=free, local_retained=self.local_size,
            no_exterior_coordinate_was_set_to_zero=True)
        return front

    def _qr_prefix(self, matrix, columns, label):
        a = np.array(matrix, dtype='<f8', order='F', copy=True)
        rows, total = a.shape
        if not 0 < columns <= min(rows, total) or not np.isfinite(a).all():
            raise ValueError('Invalid complete affine QR front '+label)
        left = a[:, :columns]
        key = ('geqrf', rows, columns)
        if key not in self._lwork:
            _, _, work, info = dgeqrf(left, lwork=-1, overwrite_a=0)
            if info or not np.isfinite(work[0]):
                raise RuntimeError('dgeqrf workspace query failed at '+label)
            self._lwork[key] = max(1, int(work[0]))
        qr, tau, _, info = dgeqrf(left, lwork=self._lwork[key], overwrite_a=1)
        if info:
            raise RuntimeError('dgeqrf failed at '+label+': '+str(info))
        if np.any(np.diag(qr[:columns, :columns]) == 0):
            raise FloatingPointError('A required eliminated QR diagonal is exactly zero at '+label+'; no ridge or clipping is used')
        if total > columns:
            trailing = a[:, columns:]
            key = ('ormqr', rows, columns, total-columns)
            if key not in self._lwork:
                _, work, info = dormqr(b'L', b'T', qr, tau, trailing, -1, overwrite_c=0)
                if info or not np.isfinite(work[0]):
                    raise RuntimeError('dormqr workspace query failed at '+label)
                self._lwork[key] = max(1, int(work[0]))
            rotated, _, info = dormqr(b'L', b'T', qr, tau, trailing,
                                      self._lwork[key], overwrite_c=1)
            if info:
                raise RuntimeError('dormqr failed at '+label+': '+str(info))
            a[:, columns:] = rotated
        a[:, :columns] = qr
        if not np.isfinite(a).all():
            raise FloatingPointError('The completed affine QR front is nonfinite at '+label)
        return a

    @staticmethod
    def _triangular(upper, rhs, transpose):
        lower = np.asarray(upper.T, dtype='<f8', order='F')
        r = np.asarray(rhs)
        vector = r.ndim == 1
        if r.ndim not in (1, 2) or r.shape[0] != upper.shape[0] or r.dtype != np.dtype('<f8'):
            raise ValueError('Triangular RHS must retain its full binary64 row dimension')
        b = np.array(r[:, None] if vector else r, dtype='<f8', order='F', copy=True)
        if not vector and b.shape[1] == 0:
            return b
        solved, info = dtrtrs(lower, b, lower=1, trans=0 if transpose else 1,
                             unitdiag=0, overwrite_b=1)
        if info:
            raise RuntimeError('Complete condensed triangular solve failed: '+str(info))
        if not np.isfinite(solved).all():
            raise FloatingPointError('A complete condensed triangular solution is nonfinite')
        return solved[:, 0] if vector else solved

    def _local_rhs(self, value, name):
        a = np.asarray(value)
        if (a.dtype != np.dtype('<f8') or a.ndim not in (1, 2) or
                a.shape[0] != self.local_size or not np.isfinite(a).all()):
            raise ValueError(name+' must be a complete finite local binary64 vector or column matrix')
        return a

    def _local_H(self, value):
        return self.root.T @ (self.root @ value)

    def hessian_action(self, value):
        self._check_open()
        a = self._local_rhs(value, 'Local H input')
        before = time.monotonic()
        result = self._local_H(a)
        if not np.isfinite(result).all():
            raise FloatingPointError('The complete local H action is nonfinite')
        self._report['local_H_action_calls'] += 1
        self._report['local_H_action_rhs_columns'] += 1 if a.ndim == 1 else a.shape[1]
        self._report['local_H_action_seconds'] += time.monotonic()-before
        return result

    def solve_local_H(self, rhs):
        self._check_open()
        r = self._local_rhs(rhs, 'Local H right-hand side')
        before = time.monotonic()
        y = self._triangular(self.root, r, transpose=True)
        result = self._triangular(self.root, y, transpose=False)
        defect = self._local_H(result)-r
        if not np.isfinite(defect).all():
            raise FloatingPointError('The complete local inverse diagnostic is nonfinite')
        rhs_norm = norm(r)
        record = dict(
            solve_index=self._report['local_H_solve_calls']+1,
            right_hand_sides=1 if r.ndim == 1 else int(r.shape[1]),
            rhs=identity(r), candidate=identity(result), condensed_residual=identity(defect),
            condensed_residual_L2=norm(defect), condensed_residual_Linf=maximum_abs(defect),
            relative_condensed_residual_L2=None if rhs_norm == 0 else norm(defect)/rhs_norm,
            seconds=time.monotonic()-before,
            crossed_deadline_for_started_solve=bool(time.monotonic() >= self.deadline),
            original_full_H_inverse_not_claimed=True, local_solver_diagnostic_not_scientific_gate=True)
        self.last_local_solve = json_safe(record)
        self._report['local_H_solve_calls'] += 1
        self._report['local_H_solve_rhs_columns'] += record['right_hand_sides']
        self._report['local_H_solve_seconds'] += record['seconds']
        self._report['local_H_solve_mandatory_residual_actions'] += 1
        self._report['last_local_solve'] = self.last_local_solve
        self._append_event(dict(event='local-H-solve', **self.last_local_solve))
        return result

    def recover(self, local, *, label='complete-local-QP-recovery'):
        self._check_open()
        u = self._local_rhs(local, 'Requested local candidate')
        if u.ndim != 1:
            raise ValueError('Recover one final local vector at a time through the original full readback')
        before = time.monotonic()
        u = u.copy()
        local_force = self._local_H(u)+self.local_gradient
        if not np.isfinite(local_force).all():
            raise FloatingPointError('The complete condensed recovery force is nonfinite')
        rhs = -self.g.copy()
        rhs[self.local_indices] += local_force
        if not np.isfinite(rhs).all():
            raise FloatingPointError('The complete original recovery RHS is nonfinite')
        # solve_H keeps its own unchanged deadline-at-start rule and mandatory
        # complete original A/AT readback after an initiated solve.
        self._check_deadline()
        if identity(self.factor.C) != identity(self.C):
            raise ValueError('The borrowed factor column scale changed before recovery')
        if self._check_factor_arrays() != self._factor_snapshot:
            raise ValueError('The borrowed factor changed before original full recovery')
        solved = self.factor.solve_H(rhs, label=label)
        full = self._full_vector(solved['candidate'], 'Actual recovered full candidate', copy=True)
        residual = self._full_vector(solved['original_residual'], 'Original full H recovery residual')
        mismatch = full[self.local_indices]-u
        exterior = residual.copy()
        exterior[self.local_indices] = 0.
        # At exterior coordinates rhs=-g exactly. The frozen original H-rhs
        # residual is therefore the actually read-back exterior gradient.
        exterior_norm = norm(exterior)
        rhs_embed_error = (rhs[self.local_indices]+self.g[self.local_indices])-local_force
        counter = self._report['recover_calls']
        receipts = dict(
            requested_local=self._save_array(f'recovery-{counter:03d}-requested-local', u,
                                            'Requested local candidate, never forcibly copied over recovered full values'),
            actual_full=self._save_array(f'recovery-{counter:03d}-actual-full', full,
                                        'Actual frozen solve_H candidate in complete original scaled-z coordinates'),
            original_full_residual=self._save_array(f'recovery-{counter:03d}-original-H-residual', residual,
                                                   'Original A.T A plus lambda2 readback minus the actual complete RHS'),
            local_mismatch=self._save_array(f'recovery-{counter:03d}-local-mismatch', mismatch,
                                           'Actual recovered local coordinates minus the requested vector'),
            rhs=self._save_array(f'recovery-{counter:03d}-rhs', rhs,
                                 'Actual full RHS -g+embed(Hhat u+ghat) including its floating addition'),
            rhs_local_embedding_error=self._save_array(f'recovery-{counter:03d}-rhs-embedding-error', rhs_embed_error,
                                                      'Diagnostic cancellation in the saved full RHS local addition'))
        record = dict(
            schema='complete-local-condensation-original-H-recovery-v1',
            source_sha256=self._report['source_sha256'], label=label, recovery_index=counter,
            model_identity_sha256=self._report.get('model_identity_sha256'),
            original_gradient=identity(self.g), local_indices=identity(self.local_indices),
            requested_local=identity(u), actual_full=identity(full),
            actual_local=identity(full[self.local_indices]), actual_rhs=identity(rhs),
            actual_local_force=identity(local_force), original_full_H_residual=identity(residual),
            local_mismatch_L2=norm(mismatch), local_mismatch_Linf=maximum_abs(mismatch),
            exterior_gradient_L2=exterior_norm, exterior_gradient_Linf=maximum_abs(exterior),
            exterior_gradient_from_original_H_residual_not_local_root=True,
            local_rhs_embedding_error_L2=norm(rhs_embed_error),
            local_rhs_embedding_error_Linf=maximum_abs(rhs_embed_error),
            exterior_response_distance_bound_diagnostic=exterior_norm/self.lambda_squared,
            exterior_energy_excess_bound_diagnostic=half_square(exterior_norm)/self.lambda_squared,
            posterior_bounds_apply_at_actual_recovered_local_coordinates=True,
            floating_posterior_numbers_not_validated_enclosures=True,
            factor_solve_report=solved['report'], arrays=receipts,
            original_A_calls_in_this_recovery=solved['report']['original_A_calls'],
            original_AT_calls_in_this_recovery=solved['report']['original_AT_calls'],
            frozen_reference_extra_A_calls=solved['report']['frozen_reference_extra_A_calls'],
            frozen_reference_extra_AT_calls=solved['report']['frozen_reference_extra_AT_calls'],
            no_additional_complete_H_action_in_this_wrapper=True,
            no_local_coordinate_overwrite=True,
            constraints_and_merit_must_be_recomputed_on_actual_full_candidate=True,
            seconds=time.monotonic()-before,
            crossed_deadline_after_started_complete_recovery=bool(time.monotonic() >= self.deadline),
            nonlinear_accepted=False, QP_optimality_claimed=False)
        self.last_recovery = json_safe(record)
        self._report['recover_calls'] += 1
        self._report['original_complete_recovery_solves'] += 1
        self._report['last_recovery'] = self.last_recovery
        self._append_event(dict(event='complete-recovery', report=self.last_recovery))
        if self.storage is not None:
            self._write_json(self.storage/f'recovery-{counter:03d}.json', self.last_recovery)
        self._write_status()
        return full

    def _save_array(self, name, value, role):
        entry = identity(value)
        entry.update(name=name, role=role, file=None)
        if self.storage is not None:
            extension = '.i64le' if np.asarray(value).dtype == np.dtype('<i8') else '.f64le'
            path = self.storage/(name+extension)
            with path.open('xb') as stream:
                for raw in byte_chunks(value):
                    stream.write(raw)
            entry['file'] = path.name
            if path.stat().st_size != entry['bytes'] or file_sha(path) != entry['raw_sha256']:
                raise IOError('An independently written condensed artifact changed bytes')
        self._arrays[name] = entry
        return entry

    def _write_json(self, path, value):
        raw = (json.dumps(json_safe(value), ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
        with Path(path).open('xb') as stream:
            stream.write(raw)

    def _append_event(self, event):
        if self.storage is not None:
            with (self.storage/'events.jsonl').open('ab') as stream:
                stream.write((json.dumps(json_safe(event), ensure_ascii=False, allow_nan=False)+'\n').encode())

    def _event(self, phase, **details):
        event = dict(event='complete_local_square_root_condensation', phase=phase,
                     completed_reverse_fronts=self._report['completed_reverse_fronts'],
                     maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, **details)
        print(json.dumps(json_safe(event), allow_nan=False), flush=True)
        self._append_event(event)

    @property
    def report(self):
        return json_safe(dict(self._report, output_arrays=self._arrays))

    def _write_status(self):
        if self.storage is None:
            return
        temp = self.storage/'status.json.tmp'
        temp.write_text(json.dumps(self.report, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
        temp.replace(self.storage/'status.json')

    def close(self):
        if self.closed:
            return
        self._report['status_before_close'] = self._report['status']
        self._report['closed'] = True
        self._report['borrowed_factor_closed_by_this_model'] = False
        self.closed = True
        self._write_status()
        self.root = self.affine = self.g = self.C = None
        self.local_gradient = self.local_center = None
        self._lwork.clear()
        # Intentionally never call self.factor.close().

    def __enter__(self):
        return self

    def __exit__(self, *unused):
        self.close()

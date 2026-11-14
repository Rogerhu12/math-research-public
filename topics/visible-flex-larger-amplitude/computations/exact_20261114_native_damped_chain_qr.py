#!/usr/bin/env python3
"""R273 complete native chain: an explicitly damped square-root direction.

This independent fallback is not scheduled by its existence.  Eta is a
required positive finite input, never an inferred acceptance tolerance.
The target is the bound direct-LD/f64 J1372 matrix, with every original
sigma, cut, stage, far and mode. T_n is exactly the original sigma_n I.
No native RHS, root, ODE, J, nonlinear trial, normal matrix or Riccati inverse
is evaluated. All scientific execution is confined to public Actions.
"""
from __future__ import annotations

import argparse
from collections import deque
from concurrent.futures import ProcessPoolExecutor
import gzip
import hashlib
import importlib
import json
import math
import multiprocessing
import os
from pathlib import Path
import resource
import struct
import sys
import time
import traceback

import numpy as np
import scipy
from scipy.linalg.lapack import dgeqrf, dormqr, dtrtrs


HERE = Path(__file__).resolve().parent
SYSTEM_NAME = 'exact_20261114_rawcell0_direct_ld_system.py'
SYSTEM_SHA = 'b64b6ed8b387834b5cc9332675127a1dcbb15a317c3400f5b768d18cdbdf5a8e'
KERNEL_NAME = 'exact_20261114_native_allrows_dyadic_residual.py'
KERNEL_SHA = '0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
SCHEMA = 'complete-native-direct-LD-J1372-damped-square-root-direction-v1'
MODEL_SCOPE = 'R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates'
_KERNEL = None


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public'):
        raise RuntimeError('Scientific native-chain QR belongs only to this public repository Actions')


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for raw in iter(lambda: stream.read(1 << 20), b''):
            h.update(raw)
    return h.hexdigest()


def load_pinned(name, digest):
    path = HERE / name
    if file_sha(path) != digest:
        raise ValueError('Frozen source changed: ' + name)
    module = importlib.import_module(Path(name).stem)
    if Path(module.__file__).resolve() != path.resolve():
        raise ValueError('Unexpected frozen helper import path: ' + name)
    return module


def exact_kernel():
    global _KERNEL
    if _KERNEL is None:
        _KERNEL = load_pinned(KERNEL_NAME, KERNEL_SHA)
    return _KERNEL


def exact_stage_job(task):
    return exact_kernel().stage_job(task)


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def precision_record():
    info = np.finfo(np.longdouble)
    return dict(dtype=str(np.dtype(np.longdouble)), itemsize=np.dtype(np.longdouble).itemsize,
        significand_bits=int(info.nmant)+1, minexp=int(info.minexp), maxexp=int(info.maxexp),
        byteorder=sys.byteorder, exact_rational_arithmetic_claimed=False)


def ld_record(value):
    value = np.longdouble(value)
    return dict(decimal_display=str(value), finite=bool(np.isfinite(value)),
        zero=bool(value == 0), negative=bool(np.signbit(value)),
        arithmetic='Recorded longdouble numerical readout, not an exact rational bound')


def ld_norm(value):
    v = np.asarray(value, dtype=np.longdouble)
    return np.sqrt(np.sum(v*v, dtype=np.longdouble))


class ChainDeadline(RuntimeError):
    pass


class NativeDampedChainQR:
    """Borrow one complete system; store all factors and pure constants.

    The front coefficients are explicitly formed f64 arrays. Their
    source expression is the exact R273 model, but their longdouble
    formation followed by f64 cast is not asserted exact. The final
    original-coordinate dyadic residual never uses these rounded weights.
    """

    def __init__(self, system, eta, eta_text, output, deadline=None, max_factor_bytes=2*1024**3):
        require_actions()
        self.system, self.B, self.output = system, system.B, output
        self.eta, self.eta_text = float(eta), str(eta_text)
        if not math.isfinite(self.eta) or self.eta <= 0:
            raise ValueError('Supply an explicit positive finite binary64 eta')
        self.D, self.K, self.M = system.depth, system.K, system.M
        self.scales = system.all('original-scales').reshape(-1)
        self.residuals = system.all('stage-residuals')
        self.cut = system.all('cut-residual').reshape(-1)
        self.far = system.all('end-residual').reshape(-1)
        self.graph = system.all('original-far-graph').reshape(-1)
        self.deadline = deadline
        self.started = time.monotonic()
        self.workspaces = {}
        self.factors = []
        self.pure_constants = []
        self.constant_rows = 0
        self.formed_stage_rows = []
        self.complete = False
        self.kappa = np.longdouble(0)
        self.qr_calls = 0
        self.formation_calls = 0
        self.formation_underflow = 0
        self.minimum_triangular_diagonal = math.inf
        N = (self.D+1)*self.K
        factor_bytes = (self.D*self.K*(2*self.K+1)+self.K*(self.K+1)+N)*8
        self.report = dict(schema='R273-complete-chain-square-root-factor-v1',
            source_sha256=file_sha(__file__), input_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
            model_scope=MODEL_SCOPE, original_scales_raw_sha256=system.arrays['original-scales']['raw_sha256'],
            eta_cli_text=self.eta_text, eta_binary64=self.B.scalar(self.eta),
            T_rule='T_n equals the complete original sigma_n times I; no nearest-power substitute',
            target_model='0.5||W(A_original T z+r)||2^2+0.5 eta^2||z||2^2',
            formed_coefficient_rule='longdouble(J)*longdouble(sigma_next)/longdouble(sigma_current), then one f64 cast; r/sigma likewise',
            exact_symbolic_cancellations='L=-I, cut=[I,0], far=[-G,I] when T_n=sigma_n I',
            working_precision=precision_record(), formation_is_not_exact_rational_RN_certification=True,
            original_unscaled_matrix_remains_the_exact_readback_target=True,
            original_cut_far_H_and_all_sigma_unchanged=True,
            rows=N, columns=N, augmented_rows=2*N, modes=self.M, block_width=self.K,
            stage_count=self.D, node_count=self.D+1, complete=False,
            node_penalty_blocks=0, cut_rows=self.M, far_rows=self.M, stage_rows=self.D*self.K,
            expected_factor_and_constant_bytes=factor_bytes,
            maximum_declared_factor_bytes=max_factor_bytes,
            maximum_front_shape=[3*self.K, 2*self.K+1],
            factors_streamed_to_artifact_not_held_as_full_dense_matrix=True,
            no_normal_matrix_formed=True, no_Riccati_or_explicit_inverse=True,
            no_rank_truncation_or_additional_ridge=True,
            no_linear_residual_threshold_added_to_native_trials=True,
            floating_QR_not_certified_by_exact_R273_rank_bound=True,
            native_accepted=False, task_completed=False)

    def check_deadline(self):
        if self.deadline is not None and time.monotonic() >= self.deadline:
            raise ChainDeadline('Explicit factor budget reached before a new complete front')

    def finite(self, value, label):
        if not np.isfinite(value).all():
            descriptor = self.output.save('failed-'+label.replace(' ', '-'), value,
                'Actual nonfinite numerical array retained; no replacement/clipping')
            self.report['nonfinite_array'] = descriptor
            raise FloatingPointError('Nonfinite complete chain array: ' + label)

    def form_stage(self, stage, J, remember=False):
        before = time.monotonic()
        with np.errstate(over='ignore', under='ignore', invalid='ignore', divide='ignore'):
            working = (np.asarray(J, dtype=np.longdouble)*np.longdouble(self.scales[stage+1]))/np.longdouble(self.scales[stage])
            V = np.asarray(working, dtype='<f8', order='C')
            rho_work = np.asarray(self.residuals[stage], dtype=np.longdouble)/np.longdouble(self.scales[stage])
            rho = np.asarray(rho_work, dtype='<f8', order='C')
        self.finite(V, 'formed-stage-'+str(stage)+'-V')
        self.finite(rho, 'formed-stage-'+str(stage)+'-rho')
        digest = hashlib.sha256(self.B.float_bytes(V)+self.B.float_bytes(rho)).hexdigest()
        if remember:
            item = dict(stage=stage, original_J_raw_sha256=self.system.J_rows[stage]['raw_sha256'],
                formed_V_raw_sha256=hashlib.sha256(self.B.float_bytes(V)).hexdigest(),
                formed_rho_raw_sha256=hashlib.sha256(self.B.float_bytes(rho)).hexdigest(),
                combined_formed_bytes_sha256=digest,
                original_sigma_current=self.B.scalar(self.scales[stage]),
                original_sigma_next=self.B.scalar(self.scales[stage+1]),
                working_nonzero_V_to_f64_zero=int(np.count_nonzero((working != 0) & (V == 0))),
                working_nonzero_rho_to_f64_zero=int(np.count_nonzero((rho_work != 0) & (rho == 0))),
                finite_source_nonzero_V_to_zero=int(np.count_nonzero((J != 0) & (V == 0))),
                negative_zero_V_entries=int(np.count_nonzero((V == 0) & np.signbit(V))),
                formation_seconds=time.monotonic()-before)
            self.formed_stage_rows.append(item)
            self.formation_underflow += item['working_nonzero_V_to_f64_zero']+item['working_nonzero_rho_to_f64_zero']
        else:
            self.B.same(digest, self.formed_stage_rows[stage]['combined_formed_bytes_sha256'],
                        'repeated formed-model byte identity, without a new J/RHS')
        self.formation_calls += 1
        return V, rho

    def boundary_rho(self, residual, sigma, label):
        with np.errstate(over='ignore', under='ignore', invalid='ignore', divide='ignore'):
            working = np.asarray(residual, dtype=np.longdouble)/np.longdouble(sigma)
            value = np.asarray(working, dtype='<f8', order='C')
        self.finite(value, label)
        self.report[label] = dict(array=self.output.save(label, value,
            'Explicitly formed boundary residual; original r/sigma exact readback remains separate'),
            working_nonzero_to_f64_zero=int(np.count_nonzero((working != 0) & (value == 0))))
        return value

    def qr_prefix(self, matrix, columns):
        # LAPACK usage follows the already executed full-prefix square-root
        # implementation. Reflector storage is never copied into a retained R.
        a = np.array(matrix, dtype='<f8', order='F', copy=True)
        rows, total = a.shape
        if not 0 < columns <= min(rows, total):
            raise ValueError('Invalid complete QR front dimensions')
        self.finite(a, 'qr-input-'+str(self.qr_calls))
        left = a[:, :columns]
        key = ('geqrf', rows, columns)
        if key not in self.workspaces:
            _, _, work, info = dgeqrf(left, lwork=-1, overwrite_a=0)
            if info or not np.isfinite(work[0]):
                raise RuntimeError('dgeqrf workspace query returned '+str(info))
            self.workspaces[key] = max(1, int(work[0]))
        qr, tau, _, info = dgeqrf(left, lwork=self.workspaces[key], overwrite_a=1)
        if info:
            raise RuntimeError('dgeqrf returned '+str(info))
        if total > columns:
            trailing = a[:, columns:]
            key = ('ormqr', rows, columns, total-columns)
            if key not in self.workspaces:
                _, work, info = dormqr(b'L', b'T', qr, tau, trailing, -1, overwrite_c=0)
                if info or not np.isfinite(work[0]):
                    raise RuntimeError('dormqr workspace query returned '+str(info))
                self.workspaces[key] = max(1, int(work[0]))
            rotated, _, info = dormqr(b'L', b'T', qr, tau, trailing,
                                     self.workspaces[key], overwrite_c=1)
            if info:
                raise RuntimeError('dormqr returned '+str(info))
            a[:, columns:] = rotated
        a[:, :columns] = qr
        self.finite(a, 'qr-output-'+str(self.qr_calls))
        self.qr_calls += 1
        return a

    def save_factor(self, node, R, S, affine, constant):
        combined = np.concatenate((R, S, affine[:, None]), axis=1) if S is not None else np.column_stack((R, affine))
        desc = self.output.save(f'chain-factor-{node:04d}', combined,
            '[upper R, S, affine] or final [upper R, affine]; mathematical lower triangle of R is zero')
        dc = self.output.save(f'chain-pure-constant-{node:04d}', constant,
            'Complete pure affine residual left by orthogonal compression; never discarded')
        self.factors.append(dict(node=node, factor=desc, constant=dc, final=S is None,
            R_columns=[0, self.K], S_columns=None if S is None else [self.K, 2*self.K],
            affine_column=self.K if S is None else 2*self.K))
        self.pure_constants.append(dc)
        self.constant_rows += int(np.size(constant))
        diagonal = np.abs(np.diag(R))
        self.minimum_triangular_diagonal = min(self.minimum_triangular_diagonal, float(np.min(diagonal)))
        ld = np.asarray(constant, dtype=np.longdouble)
        self.kappa += np.sum(ld*ld, dtype=np.longdouble)

    def factorize(self):
        require_actions()
        if self.factors or self.complete:
            raise RuntimeError('One bound factor object has only one factorization attempt')
        if self.report['expected_factor_and_constant_bytes'] > self.report['maximum_declared_factor_bytes']:
            raise MemoryError('Complete factor storage exceeds declared resource budget; no node or row is dropped')
        K, M, D = self.K, self.M, self.D
        I = np.eye(K, dtype='<f8')
        penalty = self.eta*I
        self.finite(penalty, 'explicit-eta-I')
        self.rho_cut = self.boundary_rho(self.cut, self.scales[0], 'formed-cut-rho')
        self.rho_far = self.boundary_rho(self.far, self.scales[D], 'formed-far-rho')
        carry = np.concatenate((I[:M], self.rho_cut[:, None]), axis=1)
        expected = 0
        for n, J in self.system.stages():
            self.check_deadline()
            self.B.same(n, expected, 'complete factor stage order')
            V, rho = self.form_stage(n, J, remember=True)
            crows = carry.shape[0]
            front = np.zeros((crows+2*K, 2*K+1), dtype='<f8', order='F')
            front[:crows, :K] = carry[:, :K]
            front[:crows, -1] = carry[:, K]
            front[crows:crows+K, :K] = penalty
            front[crows+K:, :K] = -I
            front[crows+K:, K:2*K] = V
            front[crows+K:, -1] = rho
            first = self.qr_prefix(front, K)
            R = np.triu(first[:K, :K]).copy()
            S = first[:K, K:2*K].copy()
            affine = first[:K, -1].copy()
            # All remaining next-node rows must be compressed, even when
            # their next-column block is rank deficient. No inverse is taken.
            second = self.qr_prefix(first[K:, K:], K)
            carry = np.column_stack((np.triu(second[:K, :K]), second[:K, K]))
            constant = second[K:, K].copy()
            self.save_factor(n, R, S, affine, constant)
            self.report['node_penalty_blocks'] += 1
            expected += 1
            if expected % 32 == 0 or expected == D:
                print(json.dumps(dict(event='native_damped_chain_factor', completed_stages=expected,
                    expected_stages=D, elapsed_seconds=time.monotonic()-self.started)), flush=True)
        self.B.same(expected, D, 'all complete shooting stages included')
        self.check_deadline()
        far_matrix = np.column_stack((-np.diag(self.graph), np.eye(M, dtype='<f8')))
        final = np.zeros((2*K+M, K+1), dtype='<f8', order='F')
        final[:K] = carry
        final[K:2*K, :K] = penalty
        final[2*K:, :K] = far_matrix
        final[2*K:, -1] = self.rho_far
        last = self.qr_prefix(final, K)
        self.save_factor(D, np.triu(last[:K, :K]).copy(), None, last[:K, K].copy(), last[K:, K].copy())
        self.report['node_penalty_blocks'] += 1
        self.B.same(self.report['node_penalty_blocks'], D+1, 'every node has exactly one eta I block')
        self.B.same(len(self.factors), D+1, 'all square-root blocks retained')
        self.B.same(self.constant_rows, (D+1)*K, 'all pure constant residual rows retained')
        actual_factor_bytes = sum(row['factor']['bytes']+row['constant']['bytes'] for row in self.factors)
        self.B.same(actual_factor_bytes, self.report['expected_factor_and_constant_bytes'],
                    'complete factor and constant storage, without dropped entries')
        self.complete = True
        self.report.update(complete=True, qr_calls=self.qr_calls, formation_calls=self.formation_calls,
            formation_underflow_to_binary64_zero=self.formation_underflow,
            pure_constant_energy_longdouble=ld_record(self.kappa),
            pure_constant_rows=self.constant_rows, actual_factor_and_constant_bytes=actual_factor_bytes,
            minimum_absolute_triangular_diagonal=self.B.scalar(self.minimum_triangular_diagonal),
            small_diagonal_is_a_readout_not_a_truncation_threshold=True,
            elapsed_seconds=time.monotonic()-self.started,
            maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        self.report['formed_model_identity_sha256'] = canonical_sha(dict(
            original_matrix=self.system.binding['new_matrix_identity_sha256'],
            sigma=self.system.arrays['original-scales']['raw_sha256'],
            eta_bits=struct.pack('<d', self.eta).hex(),
            source_sha256=file_sha(__file__), precision=precision_record(),
            stages=[{key:row[key] for key in ('stage','original_J_raw_sha256','formed_V_raw_sha256',
                'formed_rho_raw_sha256','combined_formed_bytes_sha256','original_sigma_current',
                'original_sigma_next')} for row in self.formed_stage_rows],
            cut=self.report['formed-cut-rho']['array'], far=self.report['formed-far-rho']['array']))
        return self.report

    def load_factor(self, node):
        row = self.factors[node]
        desc = row['factor']
        path = self.B.safe_file(self.output.directory, desc['file'])
        raw = path.read_bytes()
        self.B.same(len(raw), desc['bytes'], 'complete retained factor bytes')
        self.B.same(hashlib.sha256(raw).hexdigest(), desc['sha256'], 'retained factor hash')
        value = np.frombuffer(raw, dtype='<f8').reshape(desc['shape'])
        return value[:, :self.K], (None if row['final'] else value[:, self.K:2*self.K]), value[:, row['affine_column']]

    def solve(self):
        require_actions()
        if not self.complete:
            raise RuntimeError('An incomplete chain cannot produce a full direction')
        z = np.empty((self.D+1, self.K), dtype='<f8')
        started = time.monotonic()
        for n in range(self.D, -1, -1):
            R, S, a = self.load_factor(n)
            rhs = -a.copy()
            if S is not None:
                rhs -= S @ z[n+1]
            self.finite(rhs, 'backward-rhs-'+str(n))
            lower_storage = np.asarray(R.T, dtype='<f8', order='F')
            column = np.array(rhs[:, None], dtype='<f8', order='F', copy=True)
            solved, info = dtrtrs(lower_storage, column, lower=1, trans=1, unitdiag=0, overwrite_b=1)
            if info:
                self.report['triangular_failure'] = dict(node=n, info=int(info))
                raise RuntimeError('Complete chain triangular solve returned '+str(info))
            z[n] = solved[:, 0]
            self.finite(z[n], 'backward-node-'+str(n))
        z_desc = self.output.save('complete-scaled-z', z, 'Complete model coordinates before T_n=sigma_n I recovery')
        with np.errstate(over='ignore', under='ignore', invalid='ignore'):
            delta = np.multiply(z, self.scales[:, None], dtype=np.float64)
        delta_desc = self.output.save('complete-original-coordinate-delta', delta,
            'Actual full binary64 sigma*z product, no threshold or removed mode; original exact readback follows')
        self.finite(delta, 'recovered-delta')
        mask = (z != 0) & (delta == 0)
        sites = np.argwhere(mask)
        self.report['solve'] = dict(seconds=time.monotonic()-started, scaled_z=z_desc, delta=delta_desc,
            triangular_solves=self.D+1, all_native_nodes_and_modes_retained=True,
            recovery='One actual binary64 multiplication delta_nj=sigma_n*z_nj; not an exact real product claim',
            nonzero_recovery_to_zero=int(np.count_nonzero(mask)),
            negative_zero_delta=int(np.count_nonzero((delta == 0) & np.signbit(delta))),
            recovery_underflow_examples=[dict(node=int(n), column=int(j), z=self.B.scalar(z[n,j]),
                sigma=self.B.scalar(self.scales[n]), delta=self.B.scalar(delta[n,j])) for n,j in sites[:16]],
            no_recovered_local_coordinate_overwrite=True, native_accepted=False)
        return z, delta

    def model_readback(self, z):
        """Same formed arrays and eta; full A/AT actions, no normal matrix.

        These numerical diagnostics use longdouble accumulation and z before
        coordinate recovery. They are distinct from exact unscaled-row readback.
        """
        require_actions()
        K, M, D = self.K, self.M, self.D
        zld = np.asarray(z, dtype=np.longdouble)
        gradient = np.longdouble(self.eta)*(np.longdouble(self.eta)*zld)
        weighted = np.empty(((D+1)*K,), dtype=np.longdouble)
        cut = zld[0, :M]+np.asarray(self.rho_cut, dtype=np.longdouble)
        weighted[:M] = cut
        gradient[0, :M] += cut
        base_square = np.sum(np.asarray(self.rho_cut, dtype=np.longdouble)**2, dtype=np.longdouble)
        for n, J in self.system.stages():
            V, rho = self.form_stage(n, J, remember=False)
            Vld, rld = np.asarray(V, dtype=np.longdouble), np.asarray(rho, dtype=np.longdouble)
            residual = -zld[n]+Vld @ zld[n+1]+rld
            weighted[M+n*K:M+(n+1)*K] = residual
            gradient[n] -= residual
            gradient[n+1] += Vld.T @ residual
            base_square += np.sum(rld*rld, dtype=np.longdouble)
        graph = np.asarray(self.graph, dtype=np.longdouble)
        far = zld[D, M:]-graph*zld[D, :M]+np.asarray(self.rho_far, dtype=np.longdouble)
        weighted[M+D*K:] = far
        gradient[D, :M] -= graph*far
        gradient[D, M:] += far
        base_square += np.sum(np.asarray(self.rho_far, dtype=np.longdouble)**2, dtype=np.longdouble)
        residual_square = np.sum(weighted*weighted, dtype=np.longdouble)
        penalty = np.longdouble(self.eta)*zld
        penalty_square = np.sum(penalty*penalty, dtype=np.longdouble)
        factor_square = np.longdouble(0)
        factor_row_max = np.longdouble(0)
        for n in range(D+1):
            R, S, affine = self.load_factor(n)
            residual = np.asarray(R, dtype=np.longdouble) @ zld[n]+np.asarray(affine, dtype=np.longdouble)
            if S is not None:
                residual += np.asarray(S, dtype=np.longdouble) @ zld[n+1]
            factor_square += np.sum(residual*residual, dtype=np.longdouble)
            factor_row_max = max(factor_row_max, np.max(np.abs(residual)))
        model_square = residual_square+penalty_square
        return dict(arithmetic='Longdouble numerical actions of exactly the same formed f64 coefficients; no exact certificate',
            model_identity_sha256=self.report['formed_model_identity_sha256'],
            scope='Scaled z before actual sigma*z recovery; exact final delta rows are reported separately',
            base_objective=ld_record(base_square/2), objective=ld_record(model_square/2),
            model_drop=ld_record((base_square-model_square)/2),
            formed_residual_two_norm=ld_record(np.sqrt(residual_square)),
            formed_residual_infinity_norm=ld_record(np.max(np.abs(weighted))),
            full_unpreconditioned_model_gradient_two_norm=ld_record(ld_norm(gradient)),
            gradient_dimension=(D+1)*K,
            factor_variable_square=ld_record(factor_square), constant_square=ld_record(self.kappa),
            formed_energy_minus_factor_energy=ld_record(model_square-factor_square-self.kappa),
            factor_triangular_residual_infinity=ld_record(factor_row_max),
            model_gradient_is_not_native_acceptance=True, no_R273_posterior_certification_from_rounded_norms=True)


def exact_original_readback(system, delta, output, workers, source_sha):
    """All original-coordinate dyadic rows, with no unnecessary float RHS.

    Reuse only the pinned integer row kernels. Preserve the exact residual
    even when a conversion to a refinement RHS would overflow. Eta is not
    part of these original cut/stage/far equations.
    """
    require_actions()
    B = system.B
    kernel = exact_kernel()
    S = load_pinned(SYSTEM_NAME, SYSTEM_SHA)
    E = S.DynamicExactContext(system, kernel)
    M, K, D = system.M, system.K, system.depth
    inputs = {name: system.raw(name) for name in ('stage-residuals', 'cut-residual',
        'end-residual', 'original-scales', 'original-far-graph')}
    raw = B.float_bytes(delta)
    digest = hashlib.sha256(raw).hexdigest()
    decoded = E.decoded_array(raw, (D+1)*K, 'every complete original-coordinate damping direction')
    residuals = E.decoded_array(inputs['stage-residuals'], D*K, 'all original stored stage residuals')
    cut = E.decoded_array(inputs['cut-residual'], M, 'complete original cut residual')
    far = E.decoded_array(inputs['end-residual'], M, 'complete original far residual')
    graph = E.decoded_array(inputs['original-far-graph'], M, 'complete original far graph')
    sigma_words = [row[0] for row in struct.iter_unpack('<Q', inputs['original-scales'])]
    relative = 'large-arrays/damped-direction-all-exact-rows.jsonl.gz'
    path = output.directory / relative
    start = time.monotonic()
    state = dict(rows=0, products=0, stages=0, worst=None, base_worst=None)
    maxima = []
    handle = path.open('xb')
    ledger = gzip.GzipFile(fileobj=handle, mode='wb', mtime=0)
    pool = None

    def consume(kind, node, data, jhash=None):
        result = data['directions']['candidate']
        count = K if kind == 'stage' else M
        B.same(len(result['rows']), count, 'complete exact row block')
        record = E.max_record(kind, node, result['maximum_row'], result['maximum_integer'], sigma_words[node])
        if E.better(record, state['worst']):
            state['worst'] = record
        base_value, base_row = data['base_maximum']
        base = E.max_record(kind, node, base_row, base_value, sigma_words[node])
        if E.better(base, state['base_worst']):
            state['base_worst'] = base
        maxima.append(kernel.public_record(record))
        ledger.write(E.json_bytes(dict(kind=kind, node=node,
            first_global_equation_row=E.row_order(kind, node, 0),
            all_exact_unscaled_rows=result['rows'], original_J_stage_sha256=jhash,
            exact_original_sigma_maximum=kernel.public_record(record),
            direction_float64le_sha256=digest,
            new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'])))
        state['rows'] += count
        state['products'] += result['original_product_positions']

    def tasks():
        for n, J in E.stage_bytes(system):
            yield dict(stage=n, J=J, residuals=residuals[n*K:(n+1)*K],
                directions={'candidate': (decoded[n*K:(n+1)*K], decoded[(n+1)*K:(n+2)*K])})

    def take(result):
        B.same(result['stage'], state['stages'], 'all original exact stage rows in order')
        consume('stage', state['stages'], result, result['J_stage_raw_sha256'])
        state['stages'] += 1
        if state['stages'] % 32 == 0 or state['stages'] == D:
            print(json.dumps(dict(event='native_damped_exact_readback', completed_stages=state['stages'],
                expected_stages=D, elapsed_seconds=time.monotonic()-start)), flush=True)

    try:
        consume('cut', 0, E.boundary_job('cut', cut, {'candidate': decoded[:K]}, graph))
        if workers == 1:
            for task in tasks():
                take(E.stage_job(task))
        else:
            pool = ProcessPoolExecutor(max_workers=workers, mp_context=multiprocessing.get_context('spawn'))
            pending = deque()
            source = iter(tasks())
            for _ in range(2*workers):
                task = next(source, None)
                if task is None:
                    break
                pending.append(pool.submit(exact_stage_job, task))
            while pending:
                take(pending.popleft().result())
                task = next(source, None)
                if task is not None:
                    pending.append(pool.submit(exact_stage_job, task))
            pool.shutdown(wait=True)
            pool = None
        consume('far', D, E.boundary_job('far', far, {'candidate': decoded[D*K:(D+1)*K]}, graph))
        B.same(state['stages'], D, 'complete exact stage count')
        B.same(state['rows'], (D+1)*K, 'all original cut/stage/far rows')
        B.same(state['products'], D*K*K+M, 'all original product positions')
    finally:
        if pool is not None:
            pool.shutdown(wait=True, cancel_futures=True)
        ledger.close()
        handle.close()
    descriptor = dict(name='damped-direction-all-exact-rows', file=relative,
        dtype='exact-dyadic-jsonl-gzip', shape=[state['rows']], bytes=path.stat().st_size,
        sha256=file_sha(path), role='Every original unscaled e row, then exact division by original sigma; no eta rows')
    output.entries.append(descriptor)
    maximum = kernel.public_record(state['worst'])
    witness = B.write(output.directory/'exact-original-worst-witness.json', dict(
        source_sha256=source_sha, kernel_sha256=KERNEL_SHA,
        new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
        exact_original_sigma_maximum=maximum,
        operands=E.worst_witness(system, state['worst'], raw, inputs),
        complete_direction_float64le_sha256=digest,
        saved_finite_arrays_only=True, exact_nonlinear_derivative_not_claimed=True))
    detail = dict(schema='native-damped-complete-original-exact-row-readback-v1',
        source_sha256=source_sha, kernel_sha256=KERNEL_SHA,
        new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
        direction_float64le_sha256=digest, exact_rows=state['rows'], completed_stages=state['stages'],
        original_product_positions=state['products'], exact_global_original_sigma_norm=maximum,
        exact_stored_base_sigma_norm=kernel.public_record(state['base_worst']),
        typed_block_maxima=maxima, all_exact_residual_rows=descriptor, worst_witness=witness,
        no_float_refinement_RHS_formed=True, eta_not_in_original_equations=True,
        readback_uses_unscaled_J_and_r_before_exact_sigma_division=True,
        used_as_new_nonlinear_acceptance_gate=False, native_accepted=False,
        elapsed_seconds=time.monotonic()-start)
    full = B.write(output.directory/'exact-original-readback.json.gz', detail, compressed=True)
    return dict(full_report=full, exact_global_original_sigma_norm=maximum,
        exact_stored_base_sigma_norm=detail['exact_stored_base_sigma_norm'],
        exact_rows=state['rows'], completed_stages=state['stages'],
        all_exact_residual_rows=descriptor, worst_witness=witness,
        no_float_refinement_RHS_formed=True, used_as_new_nonlinear_acceptance_gate=False)


def checkpoint(B, output, system, delta, source_sha, eta, name, restricted=False):
    rows = [dict(node=n, state=row.tolist(),
        negative_zero_columns=np.flatnonzero((row == 0) & np.signbit(row)).tolist())
        for n, row in enumerate(delta)]
    return B.write(output.directory/name, dict(
        schema=('complete-original-node-restriction-of-damped-chain-direction-v1' if restricted
                else 'complete-native-damped-chain-direction-v1'),
        source_sha256=source_sha, input_binding=system.binding,
        M=system.M, K=system.K, depth=system.original_depth if restricted else system.depth,
        original_depth=system.original_depth, step_depth=system.depth, old_to_new=system.old_to_new,
        eta_binary64=B.scalar(eta), model_scope=MODEL_SCOPE,
        delta_float64le_sha256=hashlib.sha256(B.float_bytes(delta)).hexdigest(), rows=rows,
        restricted_to_original_nodes=restricted,
        complete_damped_direction_not_an_exact_Newton_claim=True,
        original_nonlinear_readback_required=True, no_nonlinear_trial=True,
        native_accepted=False, task_completed=False), compressed=True)


def small_summary(report, full_result):
    keys=('source_sha256','system_source_sha256','kernel_source_sha256','eta_cli_text','eta_binary64',
        'diagnostic_completed','linear_direction_computed','native_accepted','task_completed',
        'new_matrix_identity_sha256','actual_direct_result_sha256','input_binding',
        'factor_report','factor_summary','factor_index','formed_stage_inventory','formed_model_diagnostic',
        'original_exact_readback','step_delta','step_direction_checkpoint','restricted_old_node_delta',
        'restricted_direction_checkpoint','array_manifest','actual_error','elapsed_seconds','maximum_RSS_kib')
    result={key:report[key] for key in keys if key in report}
    result.update(schema='native-damped-chain-direction-small-summary-v1',full_result=full_result,
        scientific_execution_requires_public_repository_Actions=True,
        no_linear_norm_threshold_is_a_native_trial_gate=True,
        L2_model_descent_does_not_imply_original_infinity_descent=True)
    if len((json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode())>=95000:
        result={key:report[key] for key in ('diagnostic_completed','linear_direction_computed',
            'new_matrix_identity_sha256','actual_error','elapsed_seconds') if key in report}
        result.update(schema='native-damped-chain-direction-small-summary-v1',full_result=full_result,
            compact_transport_fallback=True,native_accepted=False,task_completed=False)
    return result


def main():
    require_actions()
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('capture-directory','step-directory','direct-directory','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--step-result-sha256',required=True)
    parser.add_argument('--direct-result-sha256',required=True)
    parser.add_argument('--eta',required=True,help='Explicit positive finite damping for direction selection, not a native tolerance')
    parser.add_argument('--factor-budget-seconds',type=float,default=None)
    parser.add_argument('--max-factor-bytes',type=int,default=2*1024**3)
    parser.add_argument('--exact-workers',type=int,default=2)
    args=parser.parse_args()
    eta=float(args.eta)
    if not math.isfinite(eta) or eta<=0:
        raise ValueError('Eta must be explicitly positive and finite in actual binary64')
    if (args.factor_budget_seconds is not None and
            (not math.isfinite(args.factor_budget_seconds) or args.factor_budget_seconds<=0)):
        raise ValueError('An explicit factor time budget must be positive and finite')
    if args.max_factor_bytes<=0 or not 1<=args.exact_workers<=4:
        raise ValueError('Use complete-factor resource storage and one to four exact workers')
    out=args.out.resolve()
    if out.exists() or any(out.is_relative_to(p.resolve()) for p in
            (args.capture_directory,args.step_directory,args.direct_directory)):
        raise ValueError('Use one new independent output directory')
    out.mkdir(parents=True)
    started=time.monotonic()
    source_sha=file_sha(__file__)
    S=load_pinned(SYSTEM_NAME,SYSTEM_SHA)
    B=S.load_binding()
    output=B.OutputArrays(out)
    factor=None
    report=dict(schema=SCHEMA,source_sha256=source_sha,system_source_sha256=SYSTEM_SHA,
        kernel_source_sha256=KERNEL_SHA,eta_cli_text=args.eta,eta_binary64=B.scalar(eta),
        actual_direct_result_sha256=args.direct_result_sha256,
        original_native_calls=0,new_RHS_calls=0,new_J_calls=0,new_ODE_steps=0,nonlinear_trials=0,
        diagnostic_completed=False,linear_direction_computed=False,native_accepted=False,task_completed=False,
        original_cut_H_far_and_sigma_not_changed=True,
        no_normal_matrix_Riccati_inverse_rank_truncation_or_extra_ridge=True,
        damping_is_not_a_new_final_equation_or_acceptance_tolerance=True,
        exact_linear_defect_not_used_as_new_native_trial_gate=True,
        factor_budget_seconds=args.factor_budget_seconds,maximum_factor_bytes=args.max_factor_bytes,
        exact_workers=args.exact_workers,NumPy=np.__version__,SciPy=scipy.__version__,
        BLAS_threads={key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')})
    try:
        system=S.RawCell0DirectLDSystem(args.capture_directory,args.step_directory,args.step_result_sha256,
            args.direct_directory,args.direct_result_sha256,B)
        report['new_matrix_identity_sha256']=system.binding['new_matrix_identity_sha256']
        report['input_binding']=B.write(out/'input-binding.json.gz',system.binding,compressed=True)
        report['original_arrays']=system.export_inputs(output)
        deadline=None if args.factor_budget_seconds is None else time.monotonic()+args.factor_budget_seconds
        factor=NativeDampedChainQR(system,eta,args.eta,output,deadline,args.max_factor_bytes)
        factor.factorize()
        report['factor_index']=B.write(out/'factor-index.json.gz',dict(
            new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
            source_sha256=source_sha,factors=factor.factors,complete=True),compressed=True)
        report['formed_stage_inventory']=B.write(out/'formed-stage-inventory.json.gz',dict(
            source_sha256=source_sha,new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
            formed_model_identity_sha256=factor.report['formed_model_identity_sha256'],
            stages=factor.formed_stage_rows),compressed=True)
        z,delta=factor.solve()
        report['linear_direction_computed']=True
        report['step_delta']=factor.report['solve']['delta']
        report['step_direction_checkpoint']=checkpoint(B,output,system,delta,source_sha,eta,'step-direction-checkpoint.json.gz')
        restricted=np.array(delta[np.asarray(system.old_to_new)],copy=True)
        report['restricted_old_node_delta']=output.save('complete-old-node-restricted-delta',restricted,
            'Exact old577-node byte restriction of this new complete damped direction, not a new target H')
        report['restricted_direction_checkpoint']=checkpoint(B,output,system,restricted,source_sha,eta,
            'restricted-original-node-direction.json.gz',restricted=True)
        # Once a complete direction exists, this mandatory original-row
        # diagnostic/serialization is not abandoned by the factor deadline.
        report['original_exact_readback']=exact_original_readback(system,delta,output,args.exact_workers,source_sha)
        report['formed_model_diagnostic']=factor.model_readback(z)
        report['diagnostic_completed']=True
    except Exception as error:
        report['actual_error']=repr(error)
        report['actual_traceback']=traceback.format_exc()
    finally:
        if factor is not None:
            factor.report.update(qr_calls=factor.qr_calls,formation_calls=factor.formation_calls,
                formation_underflow_to_binary64_zero=factor.formation_underflow,
                elapsed_seconds=time.monotonic()-factor.started,
                maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            report['factor_summary']={key:factor.report[key] for key in (
                'complete','rows','columns','augmented_rows','stage_count','node_count','block_width',
                'node_penalty_blocks','qr_calls','formation_calls','formation_underflow_to_binary64_zero',
                'pure_constant_rows','actual_factor_and_constant_bytes',
                'formed_model_identity_sha256','pure_constant_energy_longdouble',
                'minimum_absolute_triangular_diagonal','expected_factor_and_constant_bytes',
                'maximum_declared_factor_bytes','working_precision','elapsed_seconds','maximum_RSS_kib')
                if key in factor.report}
            report['factor_report']=B.write(out/'factor-report.json.gz',factor.report,compressed=True)
            if 'factor_index' not in report:
                report['factor_index']=B.write(out/'partial-factor-index.json.gz',dict(
                    source_sha256=source_sha,complete=False,factors=factor.factors,
                    partial_factors_not_a_complete_direction=True),compressed=True)
            if 'formed_stage_inventory' not in report:
                report['formed_stage_inventory']=B.write(out/'partial-formed-stage-inventory.json.gz',dict(
                    source_sha256=source_sha,complete=False,stages=factor.formed_stage_rows,
                    partial_inventory_not_a_complete_formed_model=True),compressed=True)
        report['array_manifest']=B.write(out/'output-array-manifest.json.gz',dict(
            schema='complete-native-damped-chain-direction-arrays-v1',source_sha256=source_sha,
            new_matrix_identity_sha256=report.get('new_matrix_identity_sha256'),
            arrays=output.entries,all_arrays_artifact_only=True,native_accepted=False),compressed=True)
        report['elapsed_seconds']=time.monotonic()-started
        report['maximum_RSS_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        full=B.write(out/'result.json.gz',report,compressed=True)
        B.write(out/'summary.json',small_summary(report,full))
    print(json.dumps(dict(event='native_damped_chain_finished',diagnostic_completed=report['diagnostic_completed'],
        linear_direction_computed=report['linear_direction_computed'],native_accepted=False)),flush=True)
    return 0 if report['diagnostic_completed'] else 2


if __name__=='__main__':
    raise SystemExit(main())

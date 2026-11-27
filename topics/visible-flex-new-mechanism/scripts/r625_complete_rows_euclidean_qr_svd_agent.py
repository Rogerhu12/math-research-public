#!/usr/bin/env python3
"""Complete-row QR/SVD for the original Euclidean damped increment.

For an already constructed A,b, solve min ||A x-b||^2+lambda||x||^2.
A already contains the caller's original row weights and all its retained
rows. This helper introduces NO column scaling, rank truncation, normal
equation matrix, new Jacobian, mesh, physical direction gate or ODE call.
The same factor serves every positive lambda at that exact input/active set.

Scientific execution belongs only to a declared public Actions scope.
Floating residual/stationarity observations below describe the necessary
linear solve. They are not inverse certificates or new acceptance gates.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np

_FACTOR_RECEIPTS = []


def _public_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Euclidean complete-row factorization requires the declared public Actions scope')


def _norm(vector):
    with np.errstate(over='ignore',invalid='ignore'):
        return float(np.hypot.reduce(np.ravel(vector),initial=0.))


def _finite_or_none(value):
    value = float(value)
    return value if math.isfinite(value) else None


def factor_receipts():
    """Small records, including constructor failures and partial work.

    The driver may include this in its FINAL even if an exception prevented
    a just-created factor from being installed in its cache. No raw A,Q,R,
    U,V or response arrays are returned by this function.
    """
    return json.loads(json.dumps(_FACTOR_RECEIPTS,allow_nan=False))


class EuclideanCompleteRowFactor:
    def __init__(self,A,b,clock,counts,label):
        _public_only()
        if not isinstance(counts,dict) or not isinstance(label,str):
            raise TypeError('shared cumulative dict and explicit active-set label required')
        self.clock,self.counts,self.label = clock,counts,label
        self.ready = False
        self.receipt = {'factor_id':len(_FACTOR_RECEIPTS),'label':label,
            'phase':'before_actual_matrix_capture','complete':False,'solve_requests':0,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_already_has_original_row_scaling':True,'new_column_scaling':False,
            'all_rows_and_remaining_columns_retained':True,
            'penalty':'Euclidean increment on the original remaining mixed coordinates',
            'rank_or_singular_value_truncation':False,'normal_equation_matrix_formed':False,
            'raw_matrix_or_factors_saved_to_files':False}
        _FACTOR_RECEIPTS.append(self.receipt)
        self._count('euclidean_factor_construction_attempts')
        started = time.monotonic()
        try:
            clock.check('before_complete_Euclidean_matrix_capture')
            raw = A.toarray() if hasattr(A,'toarray') else A
            dense = np.array(raw,dtype=np.float64,order='C',copy=True)
            target = np.array(b,dtype=np.float64,copy=True)
            if (dense.ndim != 2 or target.ndim != 1 or dense.shape[0] != len(target)
                    or dense.shape[0] < dense.shape[1] or dense.shape[1] == 0):
                raise ValueError('complete square or tall A and its full target b required')
            if not np.all(np.isfinite(dense)) or not np.all(np.isfinite(target)):
                raise FloatingPointError('nonfinite original Euclidean least-squares input')
            self.A,self.b = dense,target
            self.m,self.n = dense.shape
            dense.flags.writeable = False;target.flags.writeable = False
            digest = hashlib.sha256(json.dumps([self.m,self.n],separators=(',',':')).encode()+b'\n')
            digest.update(dense.tobytes(order='C'));digest.update(target.tobytes(order='C'))
            self.receipt.update(phase='before_complete_reduced_QR',matrix_shape=[self.m,self.n],
                dense_matrix_bytes=int(dense.nbytes),original_A_b_float64_sha256=digest.hexdigest(),
                original_b_norm=_finite_or_none(_norm(target)))
            self._count('euclidean_original_matrix_entries_captured',self.m*self.n)
            self._count('euclidean_original_target_entries_captured',self.m)
            del raw
            clock.check('before_complete_original_rows_reduced_QR')
            qr_started = time.monotonic()
            self._count('euclidean_full_reduced_QR_attempts')
            try:
                Q,R = np.linalg.qr(dense,mode='reduced')
                if Q.shape != (self.m,self.n) or R.shape != (self.n,self.n):
                    raise ArithmeticError('complete reduced QR returned a different dimension')
                if not np.all(np.isfinite(Q)) or not np.all(np.isfinite(R)):
                    raise FloatingPointError('nonfinite complete reduced QR factors')
                c = Q.T@target
                if not np.all(np.isfinite(c)):
                    raise FloatingPointError('nonfinite full Q-transpose-b target')
                self._count('euclidean_full_reduced_QRs_completed')
                self._count('euclidean_Q_transpose_b_entries',self.m*self.n)
                self.receipt['phase'] = 'complete_reduced_QR_before_R_SVD'
            finally:
                elapsed = time.monotonic()-qr_started
                self._count('euclidean_full_QR_seconds',elapsed)
                self.receipt['QR_seconds'] = elapsed
            del Q
            clock.check('after_complete_QR_before_full_R_SVD')
            svd_started = time.monotonic()
            self._count('euclidean_full_R_SVD_attempts')
            try:
                U,s,Vt = np.linalg.svd(R,full_matrices=False)
                if (s.shape != (self.n,) or U.shape != (self.n,self.n)
                        or Vt.shape != (self.n,self.n) or not np.all(np.isfinite(s))
                        or not np.all(np.isfinite(U)) or not np.all(np.isfinite(Vt))):
                    raise FloatingPointError('nonfinite or incomplete full R SVD')
                Utc = U.T@c
                if not np.all(np.isfinite(Utc)):
                    raise FloatingPointError('nonfinite full singular-coordinate target')
                self.s,self.Vt,self.Utc = s,Vt,Utc
                for value in (self.s,self.Vt,self.Utc):
                    value.flags.writeable = False
                self._count('euclidean_full_R_SVDs_completed')
                self._count('euclidean_all_singular_values_retained',self.n)
                self.receipt['phase'] = 'full_R_SVD_completed'
            finally:
                elapsed = time.monotonic()-svd_started
                self._count('euclidean_full_R_SVD_seconds',elapsed)
                self.receipt['R_SVD_seconds'] = elapsed
            del U,R,c
            threshold = max(self.m,self.n)*np.finfo(float).eps*float(s[0])
            self.matrix_frobenius_norm_observation = _norm(s)
            self.receipt.update(singular_values_used=self.n,
                singular_max=float(s[0]),singular_min=float(s[-1]),
                numerical_rank_observation=int(np.sum(s>threshold)),rank_observation_threshold=float(threshold),
                rank_threshold_only_reported_never_used_in_solution=True,
                matrix_frobenius_norm_observation=_finite_or_none(self.matrix_frobenius_norm_observation),
                finite_precision_factorization_not_an_inverse_certificate=True)
            self.ready = True
            self.receipt.update(phase='complete_factor_ready',complete=True)
            self._count('euclidean_factor_constructions_completed')
            clock.check('after_complete_Euclidean_QR_SVD_factorization')
        except Exception as exc:
            self.receipt.update(phase='factorization_interrupted_or_failed',
                exception={'type':type(exc).__name__,'message':str(exc)},
                complete=self.ready)
            self._count('euclidean_factor_construction_failures_or_interruptions')
            raise
        finally:
            elapsed = time.monotonic()-started
            self._count('euclidean_factor_construction_seconds',elapsed)
            self.receipt['factor_construction_seconds'] = elapsed

    def _count(self,key,amount=1):
        self.counts[key] = self.counts.get(key,0)+amount

    def solve(self,positive_lambda):
        _public_only()
        regularization = float(positive_lambda)
        if not self.ready or not math.isfinite(regularization) or regularization <= 0:
            raise ValueError('one completed factor and strictly positive finite lambda required')
        self._count('euclidean_cached_factor_solve_attempts')
        self.receipt['solve_requests'] += 1
        report = {'factor_id':self.receipt['factor_id'],'label':self.label,
            'matrix_shape':[self.m,self.n],'regularization_lambda':regularization,
            'phase':'before_cached_full_singular_filter',
            'factor_recomputed_for_this_lambda':False,'all_singular_values_used':self.n,
            'penalty':'Euclidean increment on the original remaining mixed coordinates',
            'new_column_scaling':False,'rank_truncation':False,
            'residual_and_stationarity_observations_are_not_acceptance_gates':True}
        self.receipt['last_solve'] = report
        started = time.monotonic()
        try:
            self.clock.check('before_cached_complete_Euclidean_damped_solve')
            # Equivalent to sigma/(sigma^2+lambda), avoiding squaring a
            # possibly large singular value. No threshold mask is applied.
            hypotenuse = np.hypot(self.s,math.sqrt(regularization))
            weights = (self.s/hypotenuse)/hypotenuse
            solution = self.Vt.T@(weights*self.Utc)
            self._count('euclidean_full_spectral_filter_values',self.n)
            if not np.all(np.isfinite(solution)):
                raise FloatingPointError('nonfinite original-coordinate damped solution')
            self.clock.check('after_full_filter_before_original_residual_readout')
            # These observations do not reject an otherwise finite direction.
            # If their arithmetic overflows, report the unresolved fields;
            # the driver's unchanged original prediction decides usability.
            with np.errstate(over='ignore',invalid='ignore',divide='ignore'):
                residual = self.A@solution-self.b
                self._count('euclidean_original_residual_matvec_entries',self.m*self.n)
                stationarity = self.A.T@residual+regularization*solution
                self._count('euclidean_stationarity_transpose_matvec_entries',self.m*self.n)
            rn,xn,gn = _norm(residual),_norm(solution),_norm(stationarity)
            balance = self.matrix_frobenius_norm_observation*rn+regularization*xn
            relative = gn/balance if math.isfinite(balance) and balance > 0 else (0. if gn == 0 else None)
            report.update(phase='completed_cached_Euclidean_solve',
                original_scaled_residual_norm=_finite_or_none(rn),
                original_scaled_residual_max=_finite_or_none(np.max(abs(residual))),
                Euclidean_solution_norm=_finite_or_none(xn),
                original_coordinate_direction_infinity_norm=float(np.max(abs(solution))),
                original_regularized_stationarity_norm=_finite_or_none(gn),
                original_regularized_stationarity_max=_finite_or_none(np.max(abs(stationarity))),
                relative_stationarity_observation=_finite_or_none(relative) if relative is not None else None,
                original_stationarity_formula='A.T@(A@x-b)+lambda*x',
                nonfinite_residual_observation_entries=int(np.sum(~np.isfinite(residual))),
                nonfinite_stationarity_observation_entries=int(np.sum(~np.isfinite(stationarity))),
                diagnostic_overflow_does_not_reject_finite_direction=True,
                exact_zero_singular_values=int(np.sum(self.s == 0)),
                nonzero_singular_filter_float_underflows=int(np.sum((self.s != 0)&(weights == 0))),
                zero_singular_directions_use_the_same_damped_filter_not_rank_truncation=True,
                mathematical_damped_problem_has_unique_solution_for_positive_lambda=True,
                floating_solution_error_or_global_physical_feasibility_certified=False)
            self._count('euclidean_cached_factor_solves_completed')
            self.clock.check('after_original_Euclidean_residual_and_stationarity_readout')
            return solution,report
        except Exception as exc:
            report.update(phase='cached_solve_interrupted_or_failed',
                exception={'type':type(exc).__name__,'message':str(exc)})
            self._count('euclidean_cached_factor_solve_failures_or_interruptions')
            raise
        finally:
            elapsed = time.monotonic()-started
            self._count('euclidean_cached_factor_solve_seconds',elapsed)
            report['seconds'] = elapsed

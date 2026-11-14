#!/usr/bin/env python3
"""Finite physical-angle cap Jacobi proposal at the explicit continuous repair.

Only proposal arithmetic is floating. The exact derived definition, all
mean/regular rows, the physical angle inversion, and every centre piece
are retained. True angular tails and continuous residuals are separate
inputs to the proved all-mode cap Green operator, never inferred from FFT.
"""
from __future__ import annotations
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from fourfold_codazzi_final_regular_head_model import FinalHead
from fourfold_codazzi_final_head_trial_model import ALPHA, NU, RIGHT, sha
from fourfold_codazzi_final_continuous_value_repair import iter_repair

REPAIR = '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'


class PhysicalCapHead(FinalHead):
    def __init__(self, *args, repair_report, left=Fraction(9, 10), **kwargs):
        super().__init__(*args, **kwargs)
        self.left_cut = Fraction(left)
        if not Fraction(9, 10) <= self.left_cut < RIGHT:
            raise ValueError('this new stable cap proposal uses the proved physical cap interval')
        path = Path(repair_report)
        report = json.loads(gzip.decompress(path.read_bytes()))
        if (report.get('derived_definition_sha256') != REPAIR
                or report.get('candidate_sha256') != self.identity['candidate_sha256']
                or not report.get('complete') or report.get('exact_interface_count') != 6143):
            raise ValueError('the exact full continuous value repair is required')
        definition_bytes = (json.dumps(report['definition'], sort_keys=True,
                            separators=(',', ':'))+'\n').encode()
        if hashlib.sha256(definition_bytes).hexdigest() != REPAIR:
            raise ValueError('the true derived centre definition changed')
        digest = hashlib.sha256()
        offsets = np.zeros((len(self.nodes)-1, 2*self.mc+1))
        maximum_float_fee = Fraction(0)
        for piece, exact, previous in iter_repair(self.saved, ALPHA):
            digest.update((json.dumps(dict(piece=piece, physical_offset=list(map(str, exact))),
                          sort_keys=True, separators=(',', ':'))+'\n').encode())
            offsets[piece] = list(map(float, exact))
            maximum_float_fee = max(maximum_float_fee,
                max(abs(Fraction(float(x))-e) for x, e in zip(offsets[piece], exact)))
        if digest.hexdigest() != report['definition']['offset_sequence_sha256']:
            raise ValueError('all exact cumulative offsets must match the derived definition')
        self.offsets = offsets
        self.theta = np.arange(self.angles)*np.pi/(2*self.angles)
        self.frequency = 4*np.arange(1, self.m+1)
        self.physical_fft = 4*np.fft.fftfreq(self.angles, 1/self.angles)
        self.sines = np.sin(self.theta[:, None]*self.frequency[None, :])
        self.cosines = np.column_stack((np.ones(self.angles),
                          np.cos(self.theta[:, None]*self.frequency[None, :])))
        self.basis_b = np.column_stack((self.sines, np.zeros((self.angles, self.m+1))))
        self.basis_c = np.column_stack((np.zeros((self.angles, self.m)), self.cosines))
        self.basis_bp = np.column_stack((self.cosines[:, 1:]*self.frequency,
                                        np.zeros((self.angles, self.m+1))))
        self.basis_cp = np.column_stack((np.zeros((self.angles, self.m+1)),
                                        -self.sines*self.frequency))
        self.max_inverse_residual = 0.
        self.minimum_observed_angle_jacobian = float('inf')
        self.identity.update(
            finite_state_coordinates='physical B sine and C cosine amplitudes, complete C mean',
            physical_cap_model_sha256=sha(__file__),
            derived_centre_definition_sha256=REPAIR,
            continuous_repair_report_sha256=sha(path),
            exact_repair_float_coefficient_maximum_error=str(maximum_float_fee),
            exact_requested_left=str(self.left_cut),
            exact_proposal_left_float=str(Fraction(float(self.left_cut))),
            direct_physical_rows=True, implicit_angle_inversion_is_diagnostic_only=True,
            right_DN_is_original_model_with_true_error_not_yet_paid=True)

    def fields(self, radius, piece):
        radius = float(radius)
        piece = int(piece)
        y = self.background([radius], [piece])[:, 0]
        target = self.system.controlled(np.array([radius]), float(NU))
        gamma, beta, K, ell, cr = [float(target[j][0]) for j in (1, 2, 3, 4, 5)]
        s = 1/cr
        odd = float(ALPHA)*y[:self.mc] + self.offsets[piece, :self.mc]
        even = float(ALPHA)*y[self.m:self.m+self.mc+1] + self.offsets[piece, self.mc:]
        mean = s + even[0]
        if not mean < 0:
            raise ValueError('the physical-angle proposal lost the true mean sign')
        modes = 4*np.arange(1, self.mc+1)
        phi = self.theta.copy()
        for iteration in range(20):
            phase = phi[:, None]*modes
            sine, cosine = np.sin(phase), np.cos(phase)
            psi = sine @ (even[1:]/modes)/mean
            jacobian = 1 + cosine @ even[1:]/mean
            if not np.all(jacobian > 0):
                raise ValueError('floating inverse-angle iterate is not monotone')
            residual = phi+psi-self.theta
            phi -= residual/jacobian
            if np.max(abs(residual)) < 2e-15:
                break
        phase = phi[:, None]*modes
        sine, cosine = np.sin(phase), np.cos(phase)
        psi = sine @ (even[1:]/modes)/mean
        jacobian = 1 + cosine @ even[1:]/mean
        residual = float(np.max(abs(phi+psi-self.theta)))
        if residual > 2e-13 or not np.all(np.isfinite(phi)):
            raise ValueError('complete physical-angle Newton proposal did not converge')
        self.max_inverse_residual = max(self.max_inverse_residual, residual)
        self.minimum_observed_angle_jacobian = min(self.minimum_observed_angle_jacobian,
                                                   float(np.min(jacobian)))
        u = sine @ odd
        dv = even[0] + cosine @ even[1:]
        # This exact algebraic cancellation is essential on the small cap.
        qb = 2*u
        qc = -u*u-K*(2*s*dv+dv*dv)
        return gamma, beta, K, ell, qb, qc

    def derivative(self, value):
        return (np.fft.ifft(1j*self.physical_fft[:, None]
                *np.fft.fft(value, axis=0), axis=0)).real

    def matrix(self, r, pieces=None, role='response'):
        if role != 'response':
            raise ValueError('the cap Dirichlet graph uses the physical response operator')
        r = np.atleast_1d(r)
        if pieces is None:
            pieces = self.piece_indices(r)
        answer = np.empty((self.n, self.n, len(r)))
        for k, (radius, piece) in enumerate(zip(r, pieces)):
            gamma, beta, K, ell, qb, qc = self.fields(radius, piece)
            F = qb[:, None]*self.basis_b + qc[:, None]*self.basis_c
            B = -gamma*ell*self.basis_cp-2*beta*self.basis_b+gamma*self.derivative(F)
            C = gamma*self.basis_bp-beta*(ell+1)*self.basis_c+beta*F
            answer[:, :, k] = self.project(B, C)
        return answer

    def action_at(self, radius, delta, piece):
        """Independent FFT synthesis of every supplied physical column."""
        delta = np.asarray(delta)
        if delta.ndim == 1:
            delta = delta[:, None]
        b, c, bp, cp = self.synthesize(delta, self.m)
        gamma, beta, K, ell, qb, qc = self.fields(radius, piece)
        F = qb[:, None]*b+qc[:, None]*c
        return self.project(-gamma*ell*cp-2*beta*b+gamma*self.derivative(F),
                            gamma*bp-beta*(ell+1)*c+beta*F)

    def boundary_problem(self, role='response'):
        if role != 'response':
            raise ValueError('only the physical Dirichlet graph is requested')
        left = np.zeros((self.n+1, self.n))
        right = np.zeros_like(left)
        parameter = np.zeros((self.n+1, 1))
        left[:self.m, self.m+1:] = np.eye(self.m)
        right[self.m, self.m] = 1.
        right[self.m+1:2*self.m+1, :self.m] = np.eye(self.m)
        right[self.m+1:2*self.m+1, self.m+1:] = np.diag(self.system.q_vector)
        parameter[-1, 0] = 1.
        return left, right, parameter, np.zeros(self.n+1), dict(
            left_input='all physical nonmean C cosine amplitudes j=1..96',
            right_rows='complete physical C mean and all B_j+q_j*C_j, j=1..96',
            no_fourth_row_removed=True, no_mean_removed=True,
            independent_dummy='its own zero row only',
            true_regular_DN_and_source_fees_not_yet_paid=True)

    def diagnostics(self):
        radius = float(self.left_cut)
        piece = int(self.piece_indices([radius])[0])
        z = np.sin(np.arange(self.n*3).reshape(self.n, 3)/17)/(1+np.arange(self.n)[:, None])
        A = self.matrix([radius], [piece])[:, :, 0]
        difference = A@z-self.action_at(radius, z, piece)
        error = float(np.max(abs(difference)))
        if error > 1e-9:
            raise ValueError('complete physical coefficient/FFT action identity failed')
        return dict(independent_full_column_action_maximum_difference=error,
                    physical_angle_inverse_maximum_observed_residual=self.max_inverse_residual,
                    complete_C_mean_and_original_m4_retained=True,
                    diagnostic_only=True)

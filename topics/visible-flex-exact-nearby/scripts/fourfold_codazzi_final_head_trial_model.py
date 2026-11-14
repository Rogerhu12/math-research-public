#!/usr/bin/env python3
"""Complete 193-state Galerkin Jacobi data at the exact final ac1 background.

This is a floating trial factory, not an interval inverse certificate.
The background is never enlarged: its M32 coefficients are embedded into
the requested head.  Every drift/nonlocal intermediate is kept.  All
physical boundary rows use the original theta moments.  The parameter
source differentiates F at fixed physical moving (u,v), not at fixed
normalized (U,V).  Background PPoly one-sided values are explicit.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.linalg import svd

from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_moving_polynomial_system import COORDINATES
from fourfold_codazzi_moving_regular_endpoint_system import MovingRegularEndpoint
from fourfold_codazzi_compact_metric_return_probe import bumps
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget

CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT = '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
ALPHA = Fraction(6890507429876859, 9007199254740992)
NU = Fraction(-2572625729470897, 72057594037927936)
QNUM = Fraction(562949953420957, 562949953421312)
WAIST_ROW_SHA = 'c99e3f6c7fd4975ee8fd1de26fadad7f4e42c6c379a861830d6fa419046b052e'
WAIST_ROW_SOURCE_SHA = 'dc8d3d4183cacc36e617620ca28e7e238564a80a3e53010a39577fe31632d4ae'
RIGHT = Fraction(25, 8)
TRIAL_COORDINATES = (
    'physical moving nonmean variation; h1 sine(4j phi), h2 cosine(4j phi); '
    'mean supplied by exact scalar Green')
FULL_COORDINATES = (
    'physical unnormalized moving variation; h1 sine(4j phi), '
    'h2 cosine(4j phi) including its true mean')
DUAL_COORDINATES = (
    'physical cosine-amplitude dual; original physical m=4 output omitted; '
    'no alpha normalization')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_float(value):
    return str(Fraction(float(value)))


def reflection_weights(modes):
    value = np.full(2*modes+1, .5)
    value[modes] = 1.
    return value


def kernel_rows(matrix):
    """Return an actual full nullspace only after a diagnostic rank check."""
    u, s, vh = svd(matrix, full_matrices=True, check_finite=True)
    if len(s) != matrix.shape[0] or not np.all(np.isfinite(s)):
        raise RuntimeError('invalid complete physical boundary SVD')
    relative = float(s[-1]/s[0])
    if relative <= 1e-12:
        raise RuntimeError('physical boundary rows need a better numerical factorization')
    return vh[matrix.shape[0]:].copy(), dict(
        singular_values=s.tolist(), minimum_to_maximum=relative,
        diagnostic_only=True)


class FinalHead:
    def __init__(self, candidate, object_path, q_vector, waist_row, *, modes=96,
                 angles=1024, boundary_angles=8192):
        self.candidate_path = Path(candidate)
        self.object_path = Path(object_path)
        self.q_path = Path(q_vector)
        self.waist_row_path = Path(waist_row)
        if sha(candidate) != CANDIDATE or sha(object_path) != OBJECT:
            raise ValueError('restore the complete exact ac1 background and original object')
        saved = load_candidate(candidate)
        meta = json.loads(str(saved['metadata']))
        self.saved, self.meta = saved, meta
        self.nodes = np.asarray(saved['radial_nodes'], dtype=float)
        self.coeff = np.asarray(saved['piece_coefficients'], dtype=float)
        self.mc = int(meta['modes'])
        if (meta.get('coordinates') != COORDINATES or self.mc != 32
                or Fraction(meta['exact_float_amplitude']) != ALPHA
                or Fraction(meta['exact_float_nu']) != NU
                or meta.get('exact_cap_cut') != '25/8'
                or self.nodes[0] != 0 or self.nodes[-1] != float(RIGHT)
                or self.coeff.shape != (4, len(self.nodes)-1, 65)):
            raise ValueError('the actual centre, coordinates or all cubic pieces changed')
        if any(Fraction(x) != QNUM for x in meta['exact_float_q_values']):
            raise ValueError('the original physical regular proposal changed')
        if not np.all(np.diff(self.nodes) > 0):
            raise ValueError('candidate nodes must be strictly increasing')
        self.m, self.n = int(modes), 2*int(modes)+1
        self.angles, self.boundary_angles = int(angles), int(boundary_angles)
        if self.m != 96 or angles <= 6*self.m or boundary_angles < angles:
            raise ValueError('the complete M96 head, cubic grid and physical quadrature are required')
        if angles <= 2*(self.m+2*self.mc):
            raise ValueError('the full head-to-shell operator output would alias')
        if sha(waist_row) != WAIST_ROW_SHA:
            raise ValueError('the actual complete 96-column whole-eta waist row is required')
        waist = json.loads(Path(waist_row).read_text())
        if (waist.get('kind') != 'actual_final_complete_96_physical_waist_amplitude_Jacobi_row'
                or not waist.get('complete') or not waist.get('executed')
                or not waist.get('whole_original_eta')
                or waist.get('candidate_sha256') != CANDIDATE
                or waist.get('producer_sha256') != WAIST_ROW_SOURCE_SHA
                or waist.get('complete_odd_u_derivative_columns') != 'all exactly zero'
                or len(waist['rows']) != self.m):
            raise ValueError('actual physical waist identity or complete columns changed')
        denominator = int(waist['exact_interval_denominator'])
        if denominator != 2**384:
            raise ValueError('use the exact published interval scale')
        intervals = [waist['exact_mean_interval_numerator_at_scale']]
        for j,row in enumerate(waist['rows'],1):
            if row['moving_index'] != j or row['physical_frequency'] != 4*j:
                raise ValueError('a complete waist column is missing or reordered')
            intervals.append(row['exact_interval_numerator_at_scale'])
        self.waist_proposal = np.empty(self.m+1)
        self.waist_intervals, self.waist_proposal_fees = [], []
        for j,(lo,hi) in enumerate(intervals):
            lo,hi = Fraction(int(lo),denominator),Fraction(int(hi),denominator)
            if lo > hi:
                raise ValueError('an actual waist interval was reversed')
            midpoint = (lo+hi)/2
            proposal = float(midpoint)
            exact_proposal = Fraction(proposal)
            if abs(exact_proposal-midpoint) > Fraction(1,2**52):
                raise ValueError('the physical waist midpoint conversion exceeded its explicit fee')
            self.waist_proposal[j] = proposal
            self.waist_intervals.append([str(lo),str(hi)])
            self.waist_proposal_fees.append(str(max(abs(exact_proposal-lo),abs(exact_proposal-hi))))
        squared_fee = Fraction(self.waist_proposal_fees[0])**2 \
            +2*sum((Fraction(x)**2 for x in self.waist_proposal_fees[1:]),Fraction(0)) \
            +Fraction(1,10**84)
        if not squared_fee < Fraction(3,50000000)**2:
            raise ValueError('the complete true physical waist proposal fee did not close')
        self.waist_full_L2_dual_proposal_fee = '3/50000000'
        geometry, definition = load_exact_object(object_path, 512)
        body = RotationalBodyTarget(geometry)
        graft = RotationalGraftTarget(geometry, object_path)
        self.system = MovingRegularEndpoint(geometry, self.m, angles, body, graft,
            q_path=q_vector, mean_boundary='outer')
        self.boundary_system = MovingRegularEndpoint(
            geometry, self.m, boundary_angles, body, graft,
            q_path=q_vector, mean_boundary='outer')
        for system in (self.system, self.boundary_system):
            system.alpha = float(ALPHA)
            if any(Fraction(float(x)) != QNUM for x in system.q_vector):
                raise ValueError('every head Robin proposal must be the recorded actual endpoint proposal')
        self.p = np.array([float(NU)])
        self.weights = reflection_weights(self.m)
        self.identity = dict(
            candidate_sha256=sha(candidate), object_sha256=sha(object_path),
            q_vector_sha256=sha(q_vector), actual_waist_row_sha256=sha(waist_row),
            modes=self.m, centre_modes=self.mc,
            exact_alpha=str(ALPHA), exact_nu=str(NU),
            angular_grid=angles, physical_boundary_grid=boundary_angles,
            state_coordinates=FULL_COORDINATES, background_coordinates=COORDINATES,
            source_sha256=sha(__file__),
            dependencies={name: sha(Path(__file__).with_name(name)) for name in (
                'fourfold_codazzi_candidate_shards.py',
                'fourfold_codazzi_moving_polynomial_system.py',
                'fourfold_codazzi_moving_regular_endpoint_system.py',
                'fourfold_codazzi_reciprocal_polynomial_system.py',
                'fourfold_codazzi_compact_metric_branch_probe.py',
                'fourfold_codazzi_compact_metric_return_probe.py',
                'fourfold_phase_symmetric_geometry.py',
                'fourfold_phase_codazzi_rotational_reference_probe.py',
                'fourfold_codazzi_rotational_cap_jacobi_probe.py')})

    def piece_indices(self, r):
        r = np.atleast_1d(np.asarray(r, dtype=float))
        if np.any(r < self.nodes[0]) or np.any(r > self.nodes[-1]):
            raise ValueError('no radial PPoly extrapolation')
        return np.minimum(np.searchsorted(self.nodes, r, side='right')-1,
                          len(self.nodes)-2)

    def background(self, r, pieces=None, derivative=0):
        r = np.atleast_1d(np.asarray(r, dtype=float))
        if pieces is None:
            pieces = self.piece_indices(r)
        pieces = np.broadcast_to(np.asarray(pieces, dtype=int), r.shape)
        if (np.any(pieces < 0) or np.any(pieces >= len(self.nodes)-1)
                or np.any(r < self.nodes[pieces]) or np.any(r > self.nodes[pieces+1])):
            raise ValueError('one-sided background evaluation left its actual cubic piece')
        h = r-self.nodes[pieces]
        c = self.coeff[:, pieces, :]
        if derivative == 0:
            y = ((c[0]*h[:, None]+c[1])*h[:, None]+c[2])*h[:, None]+c[3]
        elif derivative == 1:
            y = (3*c[0]*h[:, None]+2*c[1])*h[:, None]+c[2]
        else:
            raise ValueError('only actual value and first radial derivative are requested')
        out = np.zeros((self.n, len(r)))
        out[:self.mc] = y[:, :self.mc].T
        out[self.m:self.m+self.mc+1] = y[:, self.mc:].T
        return out

    def data(self, r, pieces=None):
        y = self.background(r, pieces)
        return self.system.moving_linear_fields(r, y, self.p)

    def matrix(self, r, pieces=None, role='response'):
        y = self.background(r, pieces)
        A, ignored_normalized_parameter = self.system.jacobian(r, y, self.p)
        if role == 'response':
            return A
        if role == 'adjoint':
            w = self.weights
            return -np.swapaxes(A, 0, 1)*w[None, :, None]/w[:, None, None]
        raise ValueError('unknown physical finite role')

    def project(self, odd, even, modes=None):
        modes = self.m if modes is None else int(modes)
        N = self.angles
        if 2*modes >= N:
            raise ValueError('the requested full output exceeds the original dealiased grid')
        fo = np.fft.fft(odd, axis=0)/N
        fe = np.fft.fft(even, axis=0)/N
        out = np.concatenate((-2*fo.imag[1:modes+1], 2*fe.real[:modes+1]), axis=0)
        out[modes] *= .5
        return out

    def synthesize(self, delta, modes):
        """Complete Fourier synthesis for a head or its genuine adjacent shell."""
        delta = np.asarray(delta, dtype=float)
        if delta.ndim == 1:
            delta = delta[:, None]
        if delta.shape[0] != 2*modes+1 or self.angles <= 2*(modes+2*self.mc):
            raise ValueError('full input/output support is required for this shell action')
        odd = np.zeros((self.angles, delta.shape[1]), dtype=complex)
        even = np.zeros_like(odd)
        odd[1:modes+1] = -.5j*delta[:modes]
        odd[-modes:] = .5j*delta[:modes][::-1]
        even[0] = delta[modes]
        even[1:modes+1] = .5*delta[modes+1:]
        even[-modes:] = .5*delta[modes+1:][::-1]
        frequency = 1j*self.system.physical_fft_frequency[:, None]
        return tuple(np.fft.ifft(q, axis=0).real*self.angles
                     for q in (odd,even,frequency*odd,frequency*even))

    def full_action(self, r, delta, pieces=None, role='response', output_modes=None,
                    input_modes=None):
        """Independent complete sampled polynomial action, before any head cut."""
        z = self.data(r, pieces)
        input_modes = self.m if input_modes is None else int(input_modes)
        h1, h2, h1p, h2p = self.synthesize(delta, input_modes)
        a, gamma, beta, K = z['target'][:4]
        u, v = float(ALPHA)*z['U'], z['v']
        up, vp = float(ALPHA)*z['Ut'], float(ALPHA)*z['Vt']
        m, d = z['mean'], z['drift']
        L11, L12, L21, L22 = (z[k] for k in ('b11','b12','b21','b22'))
        if role == 'response':
            primitive = self.system.primitive(u*h1+K*v*h2)
            mean = np.asarray(delta)[input_modes]
            f1 = d*h1p+gamma*m*K*h2p+L11*h1+L12*h2 \
                -2*beta*up*primitive+gamma*K*vp*mean
            f2 = d*h2p-gamma*m*h1p+L21*h1+L22*h2 \
                -2*beta*vp*primitive-gamma*up*mean
        elif role == 'adjoint':
            dphi = -beta*(z['S']-np.mean(z['S'], axis=0))
            primitive = self.system.primitive(up*h1+vp*h2)
            rank_mean = np.mean(K*vp*h1-up*h2, axis=0)
            f1 = d*h1p-gamma*m*h2p+dphi*h1-L11*h1-L21*h2 \
                -2*beta*u*primitive
            f2 = d*h2p+gamma*m*K*h1p+dphi*h2-L12*h1-L22*h2 \
                -2*beta*K*v*primitive-gamma*rank_mean
        else:
            raise ValueError('unknown physical complete action')
        return self.project(f1, f2, output_modes)

    def head_shell_blocks(self, radius, *, piece=None, columns=8, role='response'):
        """Every finite-centre body head/high entry, before any Schur estimate.

        The shell is N+1..N+64 in both fields.  Only these direct body
        couplings are finite; the high evolution and physical boundary
        operators remain genuinely infinite.
        """
        if columns < 1:
            raise ValueError('positive full column batch required')
        shell_modes = self.m+2*self.mc
        shell_indices = np.r_[np.arange(self.m,shell_modes),
            shell_modes+np.arange(self.m+1,shell_modes+1)]
        high_dimension = len(shell_indices)
        AHL = np.empty((high_dimension,self.n))
        ALH = np.empty((self.n,high_dimension))
        piece = int(self.piece_indices([radius])[0]) if piece is None else int(piece)
        for first in range(0,self.n,columns):
            last = min(first+columns,self.n);count = last-first
            delta = np.zeros((self.n,count))
            delta[np.arange(first,last),np.arange(count)] = 1.
            full = self.full_action(np.full(count,radius),delta,
                np.full(count,piece),role,output_modes=shell_modes)
            AHL[:,first:last] = full[shell_indices]
        for first in range(0,high_dimension,columns):
            last = min(first+columns,high_dimension);count = last-first
            delta = np.zeros((2*shell_modes+1,count))
            delta[shell_indices[first:last],np.arange(count)] = 1.
            ALH[:,first:last] = self.full_action(np.full(count,radius),delta,
                np.full(count,piece),role,output_modes=self.m,input_modes=shell_modes)
        return dict(head_to_shell=AHL,shell_to_head=ALH,
            shell_positive_indices=list(range(self.m+1,shell_modes+1)),
            direct_body_couplings_only=True,
            high_evolution_or_boundary_projection_not_performed=True,
            background_is_the_frozen_finite_M32_centre=True)

    def parameter_source(self, r, pieces=None, output_modes=None):
        """True partial_nu F at fixed physical Q; complete mean included."""
        z = self.data(r, pieces)
        a, gamma, beta, K = z['target'][:4]
        u, v = float(ALPHA)*z['U'], z['v']
        up, vp = float(ALPHA)*z['Ut'], float(ALPHA)*z['Vt']
        m = z['mean']
        w, wp = bumps(np.atleast_1d(np.asarray(r, dtype=float)))
        w, wp = w[0], wp[0]
        Knu = -K*w+beta*wp/(2*a*a*gamma*gamma)
        primitive = self.system.primitive(v*v)
        F1 = -beta*Knu*(primitive*up+v*v*u) \
             +gamma*m*(K*w/2+Knu)*vp
        F2 = -beta*Knu*(primitive*vp+v*v*v)-gamma*m*w*up/2
        return self.project(F1, F2, output_modes)

    def physical_boundary(self):
        """Original real amplitude rows, with no alpha or factor-two ambiguity."""
        y0 = self.background([0.], [0])[:, 0]
        yR = self.background([float(RIGHT)], [len(self.nodes)-2])[:, 0]
        _, _, jb0, jc0, _, _ = self.boundary_system.boundary_jet(0., y0, self.p)
        _, _, jbR, jcR, _, _ = self.boundary_system.boundary_jet(float(RIGHT), yR, self.p)
        amplitude = np.r_[np.zeros(self.m), self.waist_proposal]
        B0 = np.vstack((np.eye(self.n)[:self.m], amplitude))
        robin = jbR+self.boundary_system.q_vector[:, None]*jcR[1:]
        BR = np.vstack((jcR[0], robin[1:]))
        output = robin[0].copy()
        if B0.shape != (self.m+1, self.n) or BR.shape != (self.m, self.n):
            raise RuntimeError('the full fixed-nu physical complement is not square')
        return B0, BR, output, dict(
            waist_rows='u sine amplitudes, then physical C4 amplitude',
            outer_rows='physical C mean, then physical Robin amplitudes j=2..N',
            original_output='physical Robin amplitude j=1 (m=4)',
            row_units='physical unnormalized amplitudes',
            outer_rows_are_floating_complete_physical_quadrature=True,
            waist_row_from_executed_complete_interval_certificate=True,
            waist_exact_intervals=self.waist_intervals,
            waist_exact_proposal_error_bounds=self.waist_proposal_fees,
            full_waist_L2_dual_proposal_error_upper=self.waist_full_L2_dual_proposal_fee,
            waist_quadrature_vs_proposal_maximum=float(np.max(abs(jc0[1]-amplitude))),
            true_nonlinear_DN_and_physical_tail_fees_unpaid=True)

    def boundary_problem(self, role):
        B0, BR, output, description = self.physical_boundary()
        n = self.n
        left = np.zeros((n+1, n)); right = np.zeros_like(left)
        parameter = np.zeros((n+1, 1)); rhs = np.zeros(n+1)
        if role == 'response':
            p = len(B0)
            left[:p] = B0
            right[p:p+len(BR)] = BR
            right[-1] = output
            parameter[-1, 0] = 1.
            return left, right, parameter, rhs, dict(
                description=description, artificial_parameter='lambda_b4 = -b4[h]',
                no_metric_parameter_unknown=True)
        if role != 'adjoint':
            raise ValueError('unknown boundary role')
        amplitude = B0[-1, self.m:]
        if np.any(B0[-1, :self.m] != 0) or not -1. < amplitude[1] < -.5:
            raise RuntimeError('the actual physical C4 amplitude pivot needs inspection')
        # Exact reflection/Gram elimination: mean weight 1, nonmean weight 1/2.
        # No numerical left nullspace and no omitted mean column.
        L0 = np.zeros((self.m, self.n))
        L0[0, self.m] = 1.
        L0[0, self.m+1] = -amplitude[0]/(2*amplitude[1])
        for j in range(2, self.m+1):
            L0[j-1, self.m+j] = 1.
            L0[j-1, self.m+1] = -amplitude[j]/amplitude[1]
        check0 = dict(explicit_full_Gram_elimination=True,
            physical_C4_pivot=float(amplitude[1]),
            mean_factor_two_retained=True, diagnostic_only=True)
        ZR, checkR = kernel_rows(BR)
        p = len(L0)
        left[:p] = L0
        right[p:p+len(ZR)] = ZR*self.weights[None, :]
        rhs[p:p+len(ZR)] = ZR@output
        # This scalar is identically zero. It only preserves the established
        # n+1-row QR storage protocol and has no physical parameter meaning.
        parameter[-1, 0] = 1.
        return left, right, parameter, rhs, dict(
            description=description, left_rank=check0, right_rank=checkR,
            artificial_parameter='zero dummy in its own right boundary row',
            source_output_functional=output.tolist(),
            complete_L2_Gram=self.weights.tolist())

    def recover_dual(self, psi0, psiR):
        B0, BR, output, description = self.physical_boundary()
        lhs0 = self.weights*np.asarray(psi0)
        lhsR = output-self.weights*np.asarray(psiR)
        pivot = B0[-1, self.m+1]
        if not -1. < pivot < -.5:
            raise RuntimeError('the actual physical amplitude pivot changed')
        lambda0 = np.r_[lhs0[:self.m], np.asarray(psi0)[self.m+1]/(2*pivot)]
        lambdaR, _, rankR, _ = np.linalg.lstsq(BR.T, lhsR, rcond=None)
        if rankR != len(BR):
            raise RuntimeError('complete physical boundary multiplier recovery lost rank')
        robin = np.r_[0., lambdaR[1:]]
        meta = dict(
            kind='actual_final_physical_retained_Robin_dual_v1',
            coordinates=DUAL_COORDINATES,
            background_candidate_sha256=CANDIDATE,
            background_exact_alpha=str(ALPHA), background_exact_nu=str(NU),
            physical_frequency_factor=4, omitted_physical_mode=4, modes=self.m,
            cosine_amplitude_multipliers=[exact_float(x) for x in robin],
            exactly_zero_fourth_retained_multiplier=True,
            exact_amp_multiplier=exact_float(lambda0[-1]),
            exact_model_mean_multiplier=exact_float(lambdaR[0]),
            exact_waist_Dirichlet_multipliers=[exact_float(x) for x in lambda0[:-1]],
            recovery_residual_left=float(np.max(abs(B0.T@lambda0-lhs0))),
            recovery_residual_right=float(np.max(abs(BR.T@lambdaR-lhsR))),
            model_physical_boundary_only=True,
            true_mean_and_true_DN_are_reconstructed_by_the_complete_consumers=True,
            mathematical_certificate=False)
        return meta

    def trial_metadata(self, role, *, projected):
        if role not in ('response', 'adjoint'):
            raise ValueError('unknown trial role')
        return dict(
            kind=('actual_final_mean_eliminated_trial_v1' if projected
                  else 'actual_final_full_finite_head_trial_v1'),
            role=(('response' if role == 'response' else 'adjoint_nonmean')
                  if projected else role+'_full'),
            coordinates=TRIAL_COORDINATES if projected else FULL_COORDINATES,
            background_candidate_sha256=CANDIDATE,
            background_exact_alpha=str(ALPHA), background_exact_nu=str(NU),
            modes=self.m, physical_frequency_factor=4,
            exact_interval=['0', '25/8'],
            mathematical_certificate=False, full_BVP_inverse_proved=False,
            Galerkin_head_only=True,
            finite_head_mean_was_not_removed_from_the_solve=True,
            exact_zero_mean_projection_for_separate_scalar_completion=projected,
            full_operator_output_support=self.m+2*self.mc,
            no_original_background_mode_was_discarded=True)

    def diagnostic_actions(self):
        """Actual coefficient/action checks; not an interval or inverse gate."""
        r = np.array([0., .08, .16, .23839, .23841, .5, 1.5, 3.125])
        pieces = self.piece_indices(r)
        j = np.arange(1, self.n+1, dtype=float)[:, None]
        k = np.arange(1, len(r)+1, dtype=float)[None, :]
        h = np.sin(j*k/7)/(1+j)
        v = np.cos(j*(k+1)/11)/(1+j)
        rows = []
        for role in ('response', 'adjoint'):
            matrix = self.matrix(r, pieces, role)
            dense = np.einsum('ijr,jr->ir', matrix, h)
            independent = self.full_action(r, h, pieces, role)
            error = float(np.linalg.norm(dense-independent)/max(1., np.linalg.norm(independent)))
            if not np.isfinite(error) or error > 5e-11:
                raise RuntimeError('actual full Fourier matrix/action discrepancy: '+role)
            rows.append(dict(role=role, full_relative_discrepancy=error))
        A = self.full_action(r, h, pieces, 'response')
        minus_astar = self.full_action(r, v, pieces, 'adjoint')
        pairing = np.sum(self.weights[:, None]*(v*A+minus_astar*h), axis=0)
        duality = float(np.max(abs(pairing))/max(1., np.linalg.norm(A)*np.linalg.norm(v)))
        if duality > 5e-11:
            raise RuntimeError('the physical mean-weighted full adjoint identity failed')
        F = self.parameter_source(r, pieces)
        z = self.data(r, pieces)
        a, gamma, beta, K = z['target'][:4]
        w, wp = bumps(r); w, wp = w[0], wp[0]
        Knu = -K*w+beta*wp/(2*a*a*gamma*gamma)
        expected_mean = -beta*z['mean']*Knu*np.mean(z['v']**2, axis=0)
        mean_error = float(np.max(abs(F[self.m]-expected_mean)))
        if mean_error > 5e-11*max(1., float(np.max(abs(expected_mean)))):
            raise RuntimeError('the full physical parameter mean source failed')
        return dict(rows=rows, full_adjoint_duality_discrepancy=duality,
            physical_parameter_mean_discrepancy=mean_error,
            actual_radial_points=r.tolist(), diagnostic_only=True,
            rigorous_whole_eta_or_radial_certificate=False)

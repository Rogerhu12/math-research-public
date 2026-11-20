#!/usr/bin/env python3
"""R681 implicit coarse frame and fixed SPD preconditioner components.

No full/PCG driver and no angular-moment assembler are supplied here.
Construction and every standalone numerical entry belong to the public
repository Actions. Import defines functions/classes only.

The basis contract is the published ThreeJetSpace: every leading free
core-c coefficient is zero; a pair selects one radial nodal three-jet and
one R/T/Z coefficient channel; only the final column changes H, by one.
The actual DI, physical-height map, basis and whitening are retained.
No integrated_variables by coarse_variables array is materialized.
"""
import os
import time

import numpy as np
from scipy.linalg import cho_solve, solve_triangular


SCHEMA = 'R681-implicit-complete-coarse-frame-v1'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Construct or apply this numerical interface only in the public repository Actions')


class SmallSPDUnavailable(ArithmeticError):
    """An explicit optional-preconditioner failure; the original QP is intact."""

    def __init__(self, role, reason):
        self.role = str(role)
        self.reason = str(reason)
        super().__init__(self.role+': '+self.reason)

    def record(self):
        return dict(status='optional_preconditioner_unavailable', role=self.role,
            reason=self.reason, original_QP_unchanged=True,
            fallback='Caller may retain the original solver; a change during PCG requires an explicit restart',
            silent_jitter_or_clipping=False, physical_infeasibility_claimed=False)


def _vector(value, size, role):
    result = np.asarray(value)
    if result.shape != (size,) or not np.all(np.isfinite(result)):
        raise ValueError('Need a finite vector of the declared shape: '+role)
    return result


def _real_vector(value, size, role):
    result = _vector(value, size, role)
    if np.iscomplexobj(result):
        raise ValueError('The retained literal coarse basis is a real QP map: '+role)
    return result


def _real_square(value, size, role):
    result = np.asarray(value)
    if (result.shape != (size, size) or np.iscomplexobj(result)
            or not np.all(np.isfinite(result))):
        raise ValueError('Need a finite real square matrix: '+role)
    return np.array(result, dtype=float, copy=True)


def _symmetric(value, role):
    if not np.all(np.isfinite(value)):
        raise SmallSPDUnavailable(role, 'Nonfinite small-matrix arithmetic')
    skew = float(np.max(np.abs(value-value.T), initial=0.))
    result = .5*value+.5*value.T
    if not np.all(np.isfinite(result)):
        raise SmallSPDUnavailable(role, 'Nonfinite symmetrized small matrix')
    return result, skew


def _cholesky(value, role):
    try:
        result = np.linalg.cholesky(value)
    except np.linalg.LinAlgError as error:
        raise SmallSPDUnavailable(role, str(error)) from error
    if not np.all(np.isfinite(result)):
        raise SmallSPDUnavailable(role, 'Nonfinite Cholesky factor')
    return result


def integrated_inverse_transpose(coordinates, covector):
    """Transpose of DI.inverse(free, affine=False), WITHOUT scale or height.

    This is not DI.raw_transpose and not DI.pullback.  The nodal difference
    transpose is followed by the literal free-slot/core R/T restriction.
    All E/D channels, every free core mode and the H slot are retained.
    Real coefficients also permit complex input for an explicitly chosen
    future actual-map check; this function performs no such check itself.
    """
    require_actions()
    c = coordinates
    value = _vector(covector, c.size, 'DI inverse covector')
    core, accel, e, d, height = c._parts(value)
    dtype = np.result_type(value.dtype, float)
    gy = np.zeros((c.J, c.n), dtype=dtype)
    gu = np.zeros_like(gy)
    ga = np.array(accel, dtype=dtype, copy=True)
    eh, dh = e/c.h[:, None], d/c.h[:, None]
    ga[:-1] -= .5*e
    ga[1:] -= .5*e
    gu[:-1] -= eh+.5*d
    gu[1:] += eh-.5*d
    gy[:-1] -= dh
    gy[1:] += dh
    gc = (core+gy[0, 1+c.K:c.M+1]
          -c.problem.freq[c.K:]*gy[0, c.M+1+c.K:2*c.M+1])
    interior = np.stack((gy[1:-1], gu[1:-1], ga[1:-1]), axis=1)
    result = np.concatenate((gc, ga[0, :c.na0], interior.ravel(), np.asarray([height])))
    if result.shape != (c.problem.free_size,):
        raise ValueError('The original complete free layout changed')
    return result


def literal_mother_gram(coordinates, basis):
    """G_N=(S^-1 DI.inverse(A_H^-1 B))^T times itself, separated by channel.

    Uses the ACTUAL scale entries, not a presumed nu_c or an inverse
    reconstruction of the supplied coarse Cholesky.  The final physical
    height compensation cancels exactly against A_H^-1.  The caller must
    have bound that same B_H to its actual PhysicalHeight object.
    """
    require_actions()
    c = coordinates
    size = int(basis.dimension)
    pairs = np.asarray(basis.pairs)
    nodes = np.asarray(basis.node_jets)
    channels = list(basis.channels)
    if (pairs.shape != (size, 2) or not np.issubdtype(pairs.dtype, np.integer)
            or nodes.ndim != 3 or nodes.shape[1:] != (c.J, 3)
            or np.iscomplexobj(nodes) or not np.all(np.isfinite(nodes))):
        raise ValueError('Need the declared literal separable ThreeJetSpace')
    if len({tuple(v) for v in pairs.tolist()}) != size:
        raise ValueError('Literal coarse pairs must be distinct')
    radial, channel = pairs.T
    if (np.any(radial < 0) or np.any(radial >= len(nodes))
            or np.any(channel < 0) or np.any(channel >= len(channels))
            or tuple(pairs[-1]) != (basis.height_radial, 1)
            or np.count_nonzero(radial == basis.height_radial) != 1):
        raise ValueError('Only the final declared coarse column may change H')
    slots = []
    for kind, mode, slot in channels:
        if not isinstance(mode, (int, np.integer)) or not 0 <= mode <= c.M:
            raise ValueError('Invalid literal coarse Fourier mode')
        expected = (mode if kind == 'R' else c.M+mode if kind == 'T'
                    else 2*c.M+1+mode if kind == 'Z' else -1)
        if slot != expected or (kind == 'T' and mode == 0):
            raise ValueError('The original R/T/Z coefficient order changed')
        slots.append(int(slot))
    if len(set(slots)) != len(slots) or channels[1][:2] != ('Z', 0):
        raise ValueError('Need independent literal channels and the declared Z0 height slot')
    _, sa, se, sd, sh = c._parts(c.scale)
    if not np.isfinite(sh) or sh <= 0:
        raise ValueError('The actual H coordinate scale must stay positive')
    gram = np.zeros((size, size))
    last = size-1
    for j, slot in enumerate(slots):
        indices = np.flatnonzero((channel == j) & (np.arange(size) != last))
        if not len(indices):
            continue
        nodal = np.array(nodes[radial[indices]], copy=True)
        # Exactly the slots discarded by original free_direction/unpack:
        # no coarse core-c variation, fixed U0, fixed end, fixed A0_Z.
        nodal[:, 0, :2] = 0.
        nodal[:, -1, :] = 0.
        if slot >= c.na0:
            nodal[:, 0, 2] = 0.
        y, u, a = nodal[:, :, 0], nodal[:, :, 1], nodal[:, :, 2]
        e = np.diff(u, axis=1)/c.h[None]-.5*(a[:, :-1]+a[:, 1:])
        d = np.diff(y, axis=1)/c.h[None]-.5*(u[:, :-1]+u[:, 1:])
        free_a = sa[:, slot] > 0
        if np.any(a[:, ~free_a] != 0):
            raise ValueError('A discarded literal acceleration slot was retained')
        aa = a[:, free_a]/sa[free_a, slot][None]
        ee = e/se[:, slot][None]
        dd = d/sd[:, slot][None]
        gram[np.ix_(indices, indices)] = aa@aa.T+ee@ee.T+dd@dd.T
    gram[-1, -1] = 1./(sh*sh)
    if not np.all(np.isfinite(gram)):
        raise SmallSPDUnavailable('literal mother Gram', 'Nonfinite inverse-scale accumulation')
    return gram


class CoarseFrame:
    """Implicit Q/QT and corrected W/WT for the current full augmented map.

    Q=DI.inverse(A_H^-1 B R)/scale, R=diag(diagonal)^-1 chol^-T.
    Literal K=R^T G_N R; V=(Q,K); E=K+K^2=L L^T; W=V L^-T.
    Keep the supplied coordinates/basis immutable for this QP.  Their
    physical state cache may be read; this object never evaluates a field.
    """

    def __init__(self, coordinates, height_map, basis, diagonal, chol, *, provenance=None):
        require_actions()
        started = time.monotonic()
        self.coordinates, self.basis = coordinates, basis
        self.integrated_size = int(coordinates.size)
        self.coarse_size = int(basis.dimension)
        self.size = self.integrated_size+self.coarse_size
        self.provenance = dict(provenance or {})
        if height_map.coordinates is not coordinates:
            raise ValueError('Retain this exact physical-height/DI composition')
        if any(getattr(basis.o, key) != getattr(coordinates.problem, key)
               for key in ('J', 'n', 'M', 'K', 'free_size')):
            raise ValueError('Basis and full operator have different free layouts')
        if not np.array_equal(basis.o.mesh, coordinates.problem.mesh):
            raise ValueError('Retain the original radial mesh')
        self.scale = np.array(_vector(coordinates.scale, self.integrated_size, 'actual DI scale'), copy=True)
        if np.iscomplexobj(self.scale) or np.any(self.scale <= 0):
            raise ValueError('Retain every actual positive coordinate scale')
        self.compensation = np.array(_vector(height_map.compensation,
            coordinates.problem.free_size, 'actual height compensation'), copy=True)
        if np.iscomplexobj(self.compensation) or self.compensation[-1] != 0:
            raise ValueError('The original height map must be its declared triangular shear')
        selector = np.zeros(self.coarse_size)
        selector[-1] = 1.
        literal_height = basis.free_direction(selector)
        if (literal_height.shape != self.compensation.shape or literal_height[-1] != 1.
                or not np.array_equal(literal_height[:-1], self.compensation[:-1])):
            raise ValueError('The current height shear must use this same literal final B column')
        self.diagonal = np.array(_vector(diagonal, self.coarse_size, 'actual coarse diagonal'), copy=True)
        self.chol = _real_square(chol, self.coarse_size, 'actual coarse whitening factor')
        if (np.iscomplexobj(self.diagonal) or np.any(self.diagonal <= 0)
                or np.any(np.diag(self.chol) <= 0) or np.any(np.triu(self.chol, 1) != 0)):
            raise ValueError('Use the actual positive diagonal and lower Cholesky, without changing whitening')
        gram = literal_mother_gram(coordinates, basis)
        scaled = gram/self.diagonal[:, None]/self.diagonal[None, :]
        left = solve_triangular(self.chol, scaled, lower=True, check_finite=False)
        literal_k = solve_triangular(self.chol, left.T, lower=True, check_finite=False).T
        self.K, k_skew = _symmetric(literal_k, 'literal K')
        # No ridge/eigenvalue clipping: a failed small SPD factor is explicit.
        k_chol = _cholesky(self.K, 'literal K')
        endpoint, e_skew = _symmetric(self.K+self.K@self.K, 'K+K^2')
        self.frame_chol = _cholesky(endpoint, 'K+K^2')
        self._metadata = dict(schema=SCHEMA, integrated_variables=self.integrated_size,
            coarse_variables=self.coarse_size, augmented_variables=self.size,
            mother_gram='literal inverse/scale Gram from actual coefficient slots and scales',
            whitening='R=diag(diagonal)^-1 chol^-T; original caller factor retained',
            K='R^T G_N R, independently of any reconstruction from the supplied Cholesky',
            corrected_frame='W=(Q,K) chol(K+K^2)^-T',
            Q_transpose='R^T B^T A_H^-T DI.inverse^T scale^-1; no raw/lift transpose substitution',
            K_float_skew_maximum=k_skew, frame_gram_float_skew_maximum=e_skew,
            K_float_maximum_difference_from_identity=float(np.max(np.abs(self.K-np.eye(self.coarse_size)))),
            K_cholesky_diagonal_minimum=float(np.min(np.diag(k_chol))),
            frame_cholesky_diagonal_minimum=float(np.min(np.diag(self.frame_chol))),
            full_Q_materialized=False, every_original_free_coordinate_retained=True,
            coarse_free_core_c_variations=False, original_core_A0_columns_retained=True,
            same_literal_height_column_bound=True, data_Gram_assembled_here=False,
            mathematical_orthogonality_is_not_a_float_outward_certificate=True,
            source_and_input_provenance=self.provenance,
            field_evaluations=0, J_or_Jtranspose_calls=0, fixtures=0,
            setup_seconds=time.monotonic()-started)

    def q(self, coefficients):
        require_actions()
        value = _real_vector(coefficients, self.coarse_size, 'Q input')
        raw = solve_triangular(self.chol.T, value, lower=False, check_finite=False)/self.diagonal
        physical = self.basis.free_direction(raw)
        inverse_height = physical-physical[-1]*self.compensation
        return self.coordinates.inverse(inverse_height, affine=False)/self.scale

    def qt(self, covector):
        require_actions()
        value = _real_vector(covector, self.integrated_size, 'QT input')
        free = integrated_inverse_transpose(self.coordinates, value/self.scale)
        # A_H^-T, not A_H^T.  compensation has zero H slot.
        free[-1] -= self.compensation@free
        coarse = self.basis.transpose_free(free)/self.diagonal
        return solve_triangular(self.chol, coarse, lower=True, check_finite=False)

    def w(self, coefficients):
        require_actions()
        value = _real_vector(coefficients, self.coarse_size, 'W input')
        raw = solve_triangular(self.frame_chol.T, value, lower=False, check_finite=False)
        return np.concatenate((self.q(raw), self.K@raw))

    def wt(self, covector):
        require_actions()
        value = _real_vector(covector, self.size, 'WT input')
        raw = self.qt(value[:self.integrated_size])+self.K.T@value[self.integrated_size:]
        return solve_triangular(self.frame_chol, raw, lower=True, check_finite=False)

    def small_hessian(self, data_gram, damping):
        """Input G_c=A_c^T A_c already has the FULL mean-Phi external scale.

        G_c is in current U=B R coefficients, contains no damping, and is
        not the raw B-coefficient matrix or the earlier Jw normal matrix.
        No full Jacobian, field or angular-moment assembly is done here.
        """
        require_actions()
        mu = float(damping)
        if not np.isfinite(mu) or mu <= 0:
            raise ValueError('Keep the actual positive QP damping')
        mu_squared = mu*mu
        if not np.isfinite(mu_squared) or mu_squared <= 0:
            raise SmallSPDUnavailable('small Hc damping', 'The actual damping squared is not representable as finite positive float')
        data = _real_square(data_gram, self.coarse_size, 'current normalized coarse data Gram')
        data, skew = _symmetric(data, 'current normalized coarse data Gram')
        plus = np.eye(self.coarse_size)+self.K
        middle = plus@data@plus
        left = solve_triangular(self.frame_chol, middle, lower=True, check_finite=False)
        projected = solve_triangular(self.frame_chol, left.T, lower=True, check_finite=False).T
        small, final_skew = _symmetric(projected, 'coarse data compression')
        small.flat[::self.coarse_size+1] += mu_squared
        return small, dict(damping=mu, damping_squared=mu_squared,
            formula='mu^2 I + L^-1 (I+K) G_c (I+K) L^-T, L L^T=K+K^2',
            data_float_skew_maximum=skew, compressed_float_skew_maximum=final_skew,
            original_QP_regularization_changed=False, target_Gram_assembled_here=False)

    def metadata(self):
        return dict(self._metadata)


class FixedSPDPreconditioner:
    """Apply beta*(I-W WT)^2 + W*Hc^-1*WT in ORIGINAL QP coordinates.

    beta is an explicit, fixed inverse background scale. This never replaces
    mu^2 ||z||^2, changes rows/constraints, or chooses a different objective.
    The two projection passes deliberately implement P_W^2. Even for a
    nonexactly orthogonal declared W the same mutually transposed maps give
    an SPD algebraic operator when the small solve is SPD.
    """

    def __init__(self, frame, data_gram, damping, background_inverse_scale, *, data_provenance=None):
        require_actions()
        started = time.monotonic()
        self.frame = frame
        self.size = frame.size
        self.beta = float(background_inverse_scale)
        if not np.isfinite(self.beta) or self.beta <= 0:
            raise ValueError('Choose and record an explicit positive background inverse scale')
        small, construction = frame.small_hessian(data_gram, damping)
        self.factor = _cholesky(small, 'current small Hc')
        self._metadata = dict(schema='R681-fixed-original-QP-SPD-application-v1',
            frame=frame.metadata(), small_hessian=construction,
            background_inverse_scale=self.beta,
            data_provenance=dict(data_provenance or {}),
            current_data_identity_checked_by_this_helper=False,
            current_data_binding_scope='Caller must bind G_c to its actual parent, full bridge, all original rows/weights and current U; this helper neither reads nor fabricates that evidence',
            apply='beta*(I-W WT)^2 + W*Hc^-1*WT',
            active_face_usage='P B P in the original Euclidean coordinates; caller retains literal feasible steps and R668 release handling',
            small_Hc_cholesky_diagonal_minimum=float(np.min(np.diag(self.factor))),
            all_original_variables_retained=True, original_QP_changed=False,
            automatic_beta_or_damping_selection=False, PCG_driver_implemented=False,
            field_evaluations=0, J_or_Jtranspose_calls=0, fixtures=0,
            setup_seconds=time.monotonic()-started)

    def apply(self, vector):
        require_actions()
        value = _real_vector(vector, self.size, 'original augmented preconditioner input')
        coefficient = self.frame.wt(value)
        remainder = value-self.frame.w(coefficient)
        twice = remainder-self.frame.w(self.frame.wt(remainder))
        try:
            solved = cho_solve((self.factor, True), coefficient, check_finite=False)
        except np.linalg.LinAlgError as error:
            raise SmallSPDUnavailable('small Hc solve', str(error)) from error
        if not np.all(np.isfinite(solved)):
            raise SmallSPDUnavailable('small Hc solve', 'Nonfinite solved coefficients')
        result = self.beta*twice+self.frame.w(solved)
        if not np.all(np.isfinite(result)):
            raise SmallSPDUnavailable('SPD application', 'Nonfinite returned direction')
        return result

    def metadata(self):
        return dict(self._metadata)


def try_prepare(coordinates, height_map, basis, diagonal, chol, data_gram,
                damping, background_inverse_scale, *, frame_provenance=None, data_provenance=None):
    """Optional construction only. An unavailable small SPD solve is explicit.

    Return (preconditioner, report), or (None, failure_report). A caller may
    then keep its original solver without changing q or requiring a fixture.
    Layout/source misuse is not swallowed. An application-time failure is
    also never silently replaced by identity inside an ongoing PCG chain.
    """
    require_actions()
    try:
        frame = CoarseFrame(coordinates, height_map, basis, diagonal, chol,
                            provenance=frame_provenance)
        preconditioner = FixedSPDPreconditioner(frame, data_gram, damping,
            background_inverse_scale, data_provenance=data_provenance)
    except SmallSPDUnavailable as error:
        return None, error.record()
    return preconditioner, dict(status='prepared_optional_SPD_preconditioner',
        metadata=preconditioner.metadata(), scientific_solver_started=False)

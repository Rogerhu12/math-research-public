#!/usr/bin/env python3
"""Same-current full SO(3) A/A* and an optional eight-column SPD apply.

This is a new source for the actual 234ac/7f SO(3) coordinate layouts.
It does not import the old non-SO(3) DI coarse frame or its angle moments.
The fixed-SPD algebra is R681 and its active-face consumer is R685/v5.
Every scientific call requires the public repository Actions. No fixture
or numerical computation is performed by importing this file.

The eight columns only define a preconditioner. The original full QP,
Euclidean coordinate penalty, positive damping, all rows, all current
variables and all true nonlinear acceptance conditions remain in place.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from scipy.linalg import cho_solve
from scipy.sparse.linalg import LinearOperator


SCHEMA = 'complete-current-SO3-eight-column-SPD-preconditioner-v1'
MERIDIANS = {
    '234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42':
        'complete-closed-so3-unit-meridian-with-core-lift-v1',
    '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf':
        'complete-independent-axisymmetric-so3-meridian-with-core-lift-v1',
}
HESSIAN_SHA = '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4'
SPECTRAL_SHA = 'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91'
V3_SHA = 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'
V5_SHA = '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Run scientific preconditioner construction only in public Actions')


def sha(path):
    path = Path(path).resolve()
    if not path.is_file() or path.stat().st_size > 100000:
        raise ValueError('Bind a complete small source, not an arbitrary large input')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def array_sha(value):
    a = np.ascontiguousarray(value)
    h = hashlib.sha256(str(a.dtype).encode())
    h.update(json.dumps(list(a.shape)).encode())
    h.update(a.tobytes())
    return h.hexdigest()


def _source(method):
    function = getattr(method, '__func__', method)
    code = getattr(function, '__code__', None)
    if code is None:
        raise ValueError('Need the actual declared Python implementation')
    path = Path(code.co_filename).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def _finite(value):
    a = np.asarray(value)
    if np.iscomplexobj(a):
        return False
    flat = a.reshape(-1)
    # The complete A output is large: do not make an equally large mask.
    return all(np.isfinite(flat[i:i+(1 << 20)]).all()
        for i in range(0, flat.size, 1 << 20))


class NumericPreparationUnavailable(ArithmeticError):
    """A truthful optional-setup failure, never mathematical infeasibility."""


def _vector(value, size, role):
    a = np.asarray(value)
    if a.shape != (size,) or a.dtype != np.dtype('float64') or not _finite(a):
        raise NumericPreparationUnavailable('Invalid complete binary64 '+role)
    return a


def _norm_arrays(coordinates):
    names = ['sigma', 'core_scale']
    names += (['diagonal_scale'] if coordinates.norm_kind == 'jet-sum'
        else ['equilibration', 'lower', 'upper'])
    return {name: array_sha(getattr(coordinates, name)) for name in names}


def _bind(q, coordinates, bridge, x):
    implementation = _source(q.jvp)
    selected = implementation['sha256']
    if selected not in MERIDIANS or q.model.get('schema') != MERIDIANS[selected]:
        raise ValueError('Need one of the two explicitly bound complete SO3 fields')
    if (q.model.get('source_sha256') != selected or canonical(q.model) != q.identity
            or any(_source(method)['sha256'] != selected for method in
                (q.vjp, q.fields_torch, coordinates.lift, coordinates.transpose))):
        raise ValueError('The actual field and mother-coordinate sources do not match')
    if coordinates.problem is not q or bridge.original is not q:
        raise ValueError('The bridge, coordinates and current field must be the same objects')
    if (any(_source(method)['sha256'] != HESSIAN_SHA for method in
                (bridge.matvec, bridge.rmatvec, bridge.blocks.whiten))
            or sha(bridge.spectral_module.__file__) != SPECTRAL_SHA):
        raise ValueError('Retain the complete original R664 positive spectral bridge')
    x = _vector(x, q.free_size, 'current point')
    if (not np.array_equal(x, bridge.x) or x.dtype != bridge.x.dtype
            or array_sha(x) != array_sha(bridge.x)):
        raise ValueError('The complete bridge is not based at the current full point')
    norm = dict(coordinates.record)
    norm_identity = norm.pop('norm_identity_sha256', None)
    if (norm_identity != canonical(norm) or coordinates.norm_kind not in ('jet-sum', 'integral')
            or coordinates.size != q.free_size
            or norm.get('norm_kind') != coordinates.norm_kind
            or norm.get('radial_length') != coordinates.radial_length
            or norm.get('angular_transition') != coordinates.angular_transition
            or norm.get('angular_scale_sha256') != array_sha(coordinates.sigma)
            or norm.get('core_scale_sha256') != array_sha(coordinates.core_scale)):
        raise ValueError('Use the actual unchanged complete mother norm')
    expected_slots = np.array([j for j in range(3*q.J)
        if j not in (0, 3*(q.J-1), 3*(q.J-1)+1)], dtype=np.int64)
    if (q.K != 3 or q.M <= q.K or q.J < 3 or q.n != 3*q.M+2
            or q.core_size != q.M-q.K
            or not np.array_equal(q.radial_free, expected_slots)
            or q.rotation_size != len(expected_slots)*q.n
            or q.free_size != q.core_size+q.rotation_size+1):
        raise ValueError('Do not interpret another representation as the full SO3 layout')
    if (q.mesh.shape != (q.J,) or q.mesh[0] != 0 or q.S != q.mesh[-1]
            or not _finite(q.mesh) or np.any(np.diff(q.mesh) <= 0)
            or not math.isfinite(q.S) or q.S <= 0
            or q.model.get('mesh_sha256') != array_sha(q.mesh)):
        raise ValueError('Need the complete current numerical radial carrier')
    if coordinates.norm_kind == 'jet-sum':
        widths = np.diff(q.mesh)
        mass = np.r_[widths[0]/2, (widths[:-1]+widths[1:])/2, widths[-1]/2]
        diagonal = (mass[:, None]*np.array([1., coordinates.radial_length**2,
            coordinates.radial_length**4])[None]).ravel()[q.radial_free]
        if (norm.get('node_mass_sha256') != array_sha(mass)
                or norm.get('diagonal_sha256') != array_sha(diagonal)
                or not np.array_equal(coordinates.diagonal_scale, 1/np.sqrt(diagonal))):
            raise ValueError('The actual node-jet factors differ from the declared norm')
    else:
        if (norm.get('lower_factor_sha256') != array_sha(coordinates.lower)
                or norm.get('diagonal_equilibration_sha256') != array_sha(coordinates.equilibration)):
            raise ValueError('The actual integral whitening differs from its declared factors')
        upper = np.zeros_like(coordinates.lower)
        for offset in range(6):
            upper[5-offset, offset:] = coordinates.lower[offset, :len(expected_slots)-offset]
        if not np.array_equal(upper, coordinates.upper):
            raise ValueError('The upper factor is not the transpose of the actual same lower factor')
    if (bridge.radial.shape != (q.P,) or not _finite(bridge.radial)
            or np.any(bridge.radial <= 0) or q.N != q.full_N//4+1
            or q.full_N % 4 or q.multiplicity.sum() != q.full_N
            or np.any(q.multiplicity <= 0)
            or bridge.shape != (q.P*q.N*3, q.free_size)):
        raise ValueError('Keep every original stage and the complete original quarter orbit')
    if not _finite(coordinates.sigma) or np.any(coordinates.sigma <= 0):
        raise ValueError('The original angular mother scales must stay positive')
    normalizer = float(bridge.radial.sum()*q.full_N)
    p = bridge.parameters
    factor = math.sqrt(p.k/(p.scale**2*normalizer))
    if not math.isfinite(factor) or factor <= 0:
        raise NumericPreparationUnavailable('The original positive external factor is unavailable')
    return dict(field_source=implementation, model_identity_sha256=q.identity,
        current_full_point_sha256=array_sha(x), coordinate_norm_identity_sha256=norm_identity,
        actual_norm_arrays=_norm_arrays(coordinates), mesh_sha256=array_sha(q.mesh),
        radial_free_sha256=array_sha(q.radial_free),
        stage_weights_sha256=array_sha(bridge.radial),
        orbit_weights_sha256=array_sha(q.multiplicity),
        target_a_carrier_sha256=array_sha(q.a),
        fixed_scalar_metric_identity_sha256=q.model['fixed_scalar_metric_identity_sha256'],
        spectral_parameters=p.as_dict(), normalizer=normalizer,
        external_factor=factor, external_factor_hex=factor.hex(),
        hessian_source=_source(bridge.matvec), spectral_source_sha256=SPECTRAL_SHA,
        all_original_metric_rows=int(q.P*q.full_N*3),
        actual_quarter_rows=int(bridge.shape[0]), complete_variables=int(q.free_size))


class EightColumnFrame:
    """Compact W/WT in the unchanged complete SO3 QP coordinates.

    Each angular slot has two radial vectors. Core/H supports are separate.
    No full n-by-8 array is stored. QR is only an eight-column frame choice,
    not a reduction of the QP variable space or a change of its norm.
    """
    coarse_size = 8

    def __init__(self, q, coordinates):
        require_actions()
        self.size, self.core_size, self.radial_size, self.n = (
            q.free_size, q.core_size, len(q.radial_free), q.n)
        self.slots = (0, q.M+1, 2*(q.M+1))
        self.radial = []
        self.preparation = []
        t = q.mesh/q.S
        values = np.stack((t-2*t*t+t*t*t, t*t-2*t*t*t+t*t*t*t), axis=1)
        slopes = np.stack((1-4*t+3*t*t, 2*t-6*t*t+4*t*t*t), axis=1)/q.S
        accelerations = np.stack((-4+6*t, 2-12*t+12*t*t), axis=1)/(q.S*q.S)
        physical = np.stack((values, slopes, accelerations), axis=1).reshape(3*q.J, 2)
        physical = physical[q.radial_free]
        if coordinates.norm_kind == 'jet-sum':
            scale = np.asarray(coordinates.diagonal_scale)
            if scale.shape != (self.radial_size,) or not _finite(scale) or np.any(scale <= 0):
                raise ValueError('Invalid actual node-jet whitening scale')
            common = physical/scale[:, None]
            inverse_formula = 'z_rad=sigma_m*x_rad/diagonal_scale'
        else:
            scale, upper = np.asarray(coordinates.equilibration), np.asarray(coordinates.upper)
            if (scale.shape != (self.radial_size,) or upper.shape != (6, self.radial_size)
                    or not _finite(scale) or not _finite(upper) or np.any(scale <= 0)):
                raise ValueError('Invalid actual complete band whitening factors')
            raw = physical/scale[:, None]
            common = np.zeros_like(raw)
            # U[i,i+k] = upper[5-k,i+k], exactly the current lift's band convention.
            for offset in range(6):
                common[:self.radial_size-offset] += (
                    upper[5-offset, offset:, None]*raw[offset:])
            inverse_formula = 'z_rad=sigma_m*U*(x_rad/equilibration); U is the current upper band factor'
        for slot in self.slots:
            original = common*coordinates.sigma[slot]
            qr, triangular = np.linalg.qr(original, mode='reduced')
            if (qr.shape != (self.radial_size, 2) or triangular.shape != (2, 2)
                    or not _finite(qr) or not _finite(triangular)
                    or np.any(np.diag(triangular) == 0)):
                raise NumericPreparationUnavailable('The declared two full radial columns have no available QR')
            signs = np.where(np.diag(triangular) < 0., -1., 1.)
            qr = np.asarray(qr*signs[None, :], dtype=np.float64)
            triangular = signs[:, None]*triangular
            qr.setflags(write=False)
            self.radial.append(qr)
            self.preparation.append(dict(actual_angular_slot=int(slot),
                mother_coordinate_columns_sha256=array_sha(original),
                radial_Q_sha256=array_sha(qr), radial_R_sha256=array_sha(triangular),
                literal_QtQ=(qr.T@qr).tolist(),
                QR_residual_max=float(np.max(np.abs(original-qr@triangular)))))
        gram = np.zeros((8, 8), dtype=np.float64)
        gram[0, 0] = gram[1, 1] = 1.
        for j, radial in enumerate(self.radial):
            gram[2+2*j:4+2*j, 2+2*j:4+2*j] = radial.T@radial
        gram.setflags(write=False)
        self.literal_gram = gram
        self.record = dict(schema='complete-SO3-eight-column-frame-v1',
            column_descriptions=['H', 'first original free core coefficient (nu=8)',
                'omega_x sin(phi): p0,p1', 'omega_y cos(phi): p0,p1',
                'omega_z sin(2phi): p0,p1'],
            actual_column_count=8, full_coordinate_dimension=int(self.size),
            radial_physical_polynomials=['t*(1-t)^2', 't^2*(1-t)^2'],
            t='actual numerical mesh/S', physical_jet_orders=[0, 1, 2],
            inverse_coordinate_formula=inverse_formula, radial_preparation=self.preparation,
            compact_frame_bytes=sum(a.nbytes for a in self.radial),
            literal_frame_Gram_sha256=array_sha(gram), literal_frame_Gram=gram.tolist(),
            full_n_by_8_frame_stored=False, complete_QP_subspace_restricted=False,
            exact_working_orthogonality_claimed=False,
            original_norm_changed=False, all_original_variables_retained=True,
            quadrature_or_continuous_geometry_certificate=False)

    def w(self, coefficients):
        require_actions()
        c = _vector(coefficients, 8, 'coarse coefficient')
        result = np.zeros(self.size, dtype=np.float64)
        result[-1], result[0] = c[0], c[1]
        rotation = result[self.core_size:-1].reshape(self.radial_size, self.n)
        for j, (slot, radial) in enumerate(zip(self.slots, self.radial)):
            rotation[:, slot] = radial@c[2+2*j:4+2*j]
        return result

    def wt(self, value):
        require_actions()
        value = _vector(value, self.size, 'full frame transpose input')
        result = np.empty(8, dtype=np.float64)
        result[0], result[1] = value[-1], value[0]
        rotation = value[self.core_size:-1].reshape(self.radial_size, self.n)
        for j, (slot, radial) in enumerate(zip(self.slots, self.radial)):
            result[2+2*j:4+2*j] = radial.T@rotation[:, slot]
        return result


class FixedEightColumnSPD:
    """R681 beta*(I-W WT)^2 + W*(L L^T)^-1*WT, fixed for one QP."""
    def __init__(self, frame, small, *, background_inverse_scale=None):
        require_actions()
        self.frame, self.size = frame, frame.size
        self.factor = np.linalg.cholesky(small)
        if not _finite(self.factor) or np.any(np.diag(self.factor) <= 0):
            raise NumericPreparationUnavailable('The complete current small factor is not available')
        if background_inverse_scale is None:
            numerator, denominator = float(np.trace(frame.literal_gram)), float(np.trace(small))
            self.beta = numerator/denominator
            self.background = dict(policy='reciprocal-current-coarse-average-Rayleigh',
                numerator=numerator, denominator=denominator,
                formula='trace(WT W)/trace(current compressed H)', explicit_algorithm_choice=True)
        else:
            self.beta = float(background_inverse_scale)
            self.background = dict(policy='explicit-positive-literal-background', explicit_algorithm_choice=True)
        if not math.isfinite(self.beta) or self.beta <= 0:
            raise NumericPreparationUnavailable('The explicit fixed background inverse scale is unavailable')
        self.factor.setflags(write=False)
        self.background.update(value=self.beta, value_hex=self.beta.hex(),
            optimal_scale_claimed=False, unchanged_until_QP_returns=True)

    def apply(self, value):
        require_actions()
        value = _vector(value, self.size, 'preconditioner input')
        c = self.frame.wt(value)
        remainder = value-self.frame.w(c)
        twice = remainder-self.frame.w(self.frame.wt(remainder))
        coarse = cho_solve((self.factor, True), c, check_finite=False)
        result = self.beta*twice+self.frame.w(coarse)
        return _vector(result, self.size, 'preconditioner output')


def prepare(q, coordinates, bridge, x, *, damping, background_inverse_scale=None,
            callback=None):
    """Return (A, original_virtual_rhs, optional_fixed_B, complete_setup_record).

    Call only in a metric phase, before beginning its QP. A is constructed
    here from the byte-bound original full bridge and unchanged norm, using
    exactly the existing driver factor. Eight A/A* products are explicit.
    At most one full A-column is retained at once; no full rows-by-8 matrix
    or raw column artifact is written. The original bridge's own temporary
    arrays and caches remain part of actual resource usage.

    A source/layout/point mismatch raises. An arithmetic preparation failure
    is reported with B=None, so the caller may use the original frozen v3
    QP before any PCG chain. No running chain silently changes its B.
    """
    require_actions()
    began = time.monotonic()
    mu = float(damping)
    if not math.isfinite(mu) or mu <= 0 or not math.isfinite(mu*mu) or mu*mu <= 0:
        raise ValueError('Keep the original finite positive damping')
    binding = _bind(q, coordinates, bridge, x)
    factor = binding['external_factor']
    A = LinearOperator(bridge.shape, dtype=np.float64,
        matvec=lambda z: factor*bridge.operator.matvec(coordinates.lift(z)),
        rmatvec=lambda v: factor*coordinates.transpose(bridge.operator.rmatvec(v)))
    residual = factor*bridge.residual
    report = dict(schema=SCHEMA, source_sha256=sha(__file__), binding=binding,
        actual_damping=mu, actual_damping_hex=mu.hex(),
        current_H='A^T A+mu^2 I in the original complete QP coordinates',
        immutable_original_objective_norm_rows_and_acceptance=True,
        old_DI_frame_or_angular_moments_used=False, previous_parent_Gram_used=False,
        extra_A_calls=0, extra_Atranspose_calls=0, columns_completed=0,
        maximum_simultaneously_retained_full_A_columns=1,
        full_A_column_bytes=int(A.shape[0])*8,
        full_H_column_bytes=int(A.shape[1])*8,
        full_field_temporary_arrays_are_additional=True,
        total_peak_memory_inferred_from_column_size=False,
        matrix_or_column_raw_published=False, column_history=[],
        construction_before_any_PCG_chain=True,
        original_QP_changed=False, physical_feasibility_conclusion=False,
        performance_improvement_established=False, fixtures=0)
    counts_before = dict(q.counts)
    try:
        frame = EightColumnFrame(q, coordinates)
        data = np.empty((8, 8), dtype=np.float64)
        for j in range(8):
            started = time.monotonic()
            coefficient = np.zeros(8, dtype=np.float64)
            coefficient[j] = 1.
            direction = frame.w(coefficient)
            ad = adjoint = None
            try:
                report['extra_A_calls'] += 1
                ad = _vector(A.matvec(direction), A.shape[0], 'current full A column')
                energy = float(ad@ad)
                report['extra_Atranspose_calls'] += 1
                adjoint = _vector(A.rmatvec(ad), A.shape[1], 'current full A*A column')
                column = frame.wt(adjoint)
                if not math.isfinite(energy) or not _finite(column):
                    raise NumericPreparationUnavailable('The current complete data compression is nonfinite')
                data[:, j] = column
                details = dict(column=j, seconds=time.monotonic()-started,
                    full_coordinate_direction_sha256=array_sha(direction),
                    data_energy=energy, transpose_diagonal=float(column[j]),
                    diagonal_pair_absolute_defect=abs(energy-float(column[j])))
                report['column_history'].append(details)
                report['columns_completed'] = j+1
                if callback is not None:
                    callback(dict(event='same_current_SO3_coarse_column_complete', **details))
            finally:
                # Release the actual quarter-orbit A output before the next column.
                del ad, adjoint, direction
        skew = float(np.max(np.abs(data-data.T)))
        symmetric = .5*(data+data.T)
        small = symmetric+(mu*mu)*frame.literal_gram
        if not _finite(small):
            raise NumericPreparationUnavailable('The same-current complete small Hessian is nonfinite')
        preconditioner = FixedEightColumnSPD(frame, small,
            background_inverse_scale=background_inverse_scale)
        report.update(status='prepared_optional_fixed_SPD', enabled=True,
            frame=frame.record, actual_data_Gram_sha256=array_sha(data),
            actual_data_Gram=data.tolist(), maximum_data_Gram_skew=skew,
            symmetric_small_H_sha256=array_sha(small), symmetric_small_H=small.tolist(),
            compressed_damping='mu^2 times literal WT W; the full QP still uses mu^2 I',
            actual_small_factor_sha256=array_sha(preconditioner.factor),
            positive_small_factor_diagonal_min=float(np.min(np.diag(preconditioner.factor))),
            fixed_background_inverse=preconditioner.background,
            apply='beta*(I-W WT)^2 + W*(L L^T)^-1*WT',
            actual_small_solve_uses='literal successful Cholesky L, no inverse, ridge, jitter, clipping or column removal',
            active_face_consumer=dict(source_sha256=V5_SHA,
                formula='R685 B-BQ^T(QBQ^T)^-1QB',
                original_v3_source_sha256=V3_SHA),
            global_SPD_is_the_R681_algebra_for_declared_maps=True,
            floating_operator_or_continuous_certificate=False)
    except (NumericPreparationUnavailable, FloatingPointError, OverflowError,
            MemoryError, np.linalg.LinAlgError) as error:
        preconditioner = None
        report.update(status='optional_numeric_preparation_unavailable', enabled=False,
            exception_type=type(error).__name__, message=str(error),
            fallback='Original byte-bound v3 on the same A/residual/C/b/mu before a PCG chain',
            no_coarse_column_dropped_to_force_success=True,
            mathematical_infeasibility_claimed=False)
    finally:
        report['preparation_seconds'] = time.monotonic()-began
        report['actual_field_operator_count_deltas'] = {
            key: q.counts[key]-counts_before[key] for key in q.counts}
    if (array_sha(bridge.x) != binding['current_full_point_sha256']
            or canonical(q.model) != binding['model_identity_sha256']
            or coordinates.record['norm_identity_sha256'] != binding['coordinate_norm_identity_sha256']
            or _norm_arrays(coordinates) != binding['actual_norm_arrays']):
        raise ValueError('Current point, full model or mother norm changed during preparation')
    return A, residual, preconditioner, report

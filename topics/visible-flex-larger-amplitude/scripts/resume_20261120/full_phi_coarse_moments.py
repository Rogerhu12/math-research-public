#!/usr/bin/env python3
"""R681 current normalized-Phi coarse Gram from moving-frame angular moments.

Consume the existing frozen R664 bridge, actual field cache, literal B and
CoarseFrame R. No field/J/JT evaluations, unit-column sweep, PCG/full driver,
fixture or scientific execution occurs on import. Numerical construction is
restricted to this repository's public Actions. Floating algebra only.
"""
import copy
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.linalg import solve_triangular


SCHEMA = 'R681-current-normalized-Phi-coarse-moments-v1'
SOURCE_SHA256 = {
    'frame': '324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da',
    'hessian': '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4',
    'batch': '02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a',
    'observed': '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d',
    'dense': 'e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d',
    'basis': '118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8',
    'basis_base': '1da3fac6c2050f9615c9c023e87e58a67e1d36cb578e791abb8903a771d2bfc7',
    'reference_tail': '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216',
}
V7_EQUIVALENT_SOURCE_SHA256 = '702c9e13db661d39771aa673dca7c19120c695da16556919e63918705b038ec8'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Assemble current scientific matrices only in the public repository Actions')


def _source(function, role):
    function = getattr(function, '__func__', function)
    code = getattr(function, '__code__', None)
    if code is None:
        raise ValueError('Need the actual published Python implementation: '+role)
    path = Path(code.co_filename).resolve()
    if not path.is_file() or path.stat().st_size > 100000:
        raise ValueError('Missing or unexpected source file: '+role)
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != SOURCE_SHA256[role]:
        raise ValueError('The declared frozen implementation changed: '+role)
    return dict(path=str(path), bytes=len(raw), sha256=digest,
                symbol=function.__qualname__)


def _array_sha(value):
    value = np.ascontiguousarray(value)
    digest = hashlib.sha256()
    digest.update(str(value.dtype).encode())
    digest.update(json.dumps(list(value.shape)).encode())
    digest.update(memoryview(value).cast('B'))
    return digest.hexdigest()


def _real(value, shape, role, *, positive=False):
    value = np.asarray(value)
    if (value.shape != tuple(shape) or np.iscomplexobj(value)
            or not np.all(np.isfinite(value)) or (positive and np.any(value <= 0))):
        raise ValueError('Need the actual finite '+('positive ' if positive else '')+role)
    return value


class _AngularMoments:
    """Pointwise product-to-sum in the already moving R/T/Z six-frame.

    Coarse channel pairs are finite trigonometric tests. The current field
    and spectral tensor are NOT band limited or truncated by this object.
    """

    def __init__(self, channels, phi, multiplicity):
        require_actions()
        self.channels = list(channels)
        self.nc = len(channels)
        self.dimension = 2*self.nc
        self.max_mode = max(int(channel[1]) for channel in channels)
        self.span = 2*self.max_mode+1
        self.ii, self.jj = np.triu_indices(6)
        self.component = {(int(i), int(j)): k for k, (i, j) in enumerate(zip(self.ii, self.jj))}
        frequencies = 2*np.arange(self.span)
        arguments = phi[:, None]*frequencies[None]
        self.tests = np.concatenate((np.cos(arguments), np.sin(arguments)), axis=1)
        self.tests *= multiplicity[:, None]
        velocity, position = [], []
        for kind, mode, _ in channels:
            mode, nu = int(mode), 2*int(mode)
            # Terms: six-component index, cos=0/sin=1, mode, coefficient.
            if kind == 'R':
                velocity.append([(0, 0, mode, 1.)])
                position.append([(3, 1, mode, -float(nu)), (4, 0, mode, 1.)])
            elif kind == 'T':
                velocity.append([(1, 1, mode, 1.)])
                position.append([(3, 1, mode, -1.), (4, 0, mode, float(nu))])
            elif kind == 'Z':
                velocity.append([(2, 0, mode, 1.)])
                position.append([(5, 1, mode, -float(nu))])
            else:
                raise ValueError('Unknown literal moving coefficient channel')
        terms = velocity+position
        destination, component, tone, coefficient = [], [], [], []
        for left in range(self.dimension):
            for right in range(left, self.dimension):
                for i, ti, m, ci in terms[left]:
                    for j, tj, n, cj in terms[right]:
                        factor = .5*ci*cj
                        if factor == 0:
                            continue
                        piece = self.component[(min(i, j), max(i, j))]
                        difference, total = abs(m-n), m+n
                        if ti == tj == 0:
                            entries = ((difference, 1.), (total, 1.))
                        elif ti == tj == 1:
                            entries = ((difference, 1.), (total, -1.))
                        else:
                            sign = (n > m)-(n < m) if ti == 0 else (m > n)-(m < n)
                            entries = ((self.span+total, 1.), (self.span+difference, float(sign)))
                        for frequency, weight in entries:
                            if weight == 0:
                                continue
                            destination.append(left*self.dimension+right)
                            component.append(piece)
                            tone.append(frequency)
                            coefficient.append(factor*weight)
        self.destination = np.asarray(destination, dtype=np.int64)
        self.component_index = np.asarray(component, dtype=np.int64)
        self.tone = np.asarray(tone, dtype=np.int64)
        self.coefficient = np.asarray(coefficient)
        self.diagonal = np.arange(self.dimension)

    def contract(self, moving_tensor):
        """All original angle rows enter; no rotation is applied here."""
        tensor = np.asarray(moving_tensor)
        components = tensor[:, :, self.ii, self.jj]
        moments = components.transpose(0, 2, 1)@self.tests
        contributions = (moments[:, self.component_index, self.tone]
                         *self.coefficient[None])
        result = np.empty((len(tensor), self.dimension, self.dimension))
        for block in range(len(tensor)):
            upper = np.bincount(self.destination, weights=contributions[block],
                minlength=self.dimension*self.dimension).reshape(self.dimension, self.dimension)
            result[block] = upper+upper.T
            result[block, self.diagonal, self.diagonal] = upper[self.diagonal, self.diagonal]
        return result


def _block_view(blocks, start, stop):
    """Reuse the literal R664 factor methods with views of the same five arrays."""
    view = copy.copy(blocks)
    for key in ('axis', 'offaxis', 'root_plus', 'root_off', 'root_minus'):
        setattr(view, key, getattr(blocks, key)[start:stop])
    return view


def _radial_pair(problem, nodes, height_radial, start, stop):
    """Literal nodal Hermite three jets plus actual analytic h/h' on B_H."""
    cells = problem.observation_cells[start:stop]
    endpoint = np.stack((nodes[cells], nodes[cells+1]), axis=1).reshape(-1, 6, nodes.shape[-1])
    stages = np.einsum('bqc,bck->bqk', problem.observation_weights[start:stop, :2], endpoint)
    stages[:, :, height_radial] += problem.lift_scalar[start:stop, :2]
    return stages[:, 0], stages[:, 1]


def _apply_original_whitening(normal, frame, channel_indices):
    """Apply the SAME actual R on both sides; exploit only literal zero blocks."""
    d, factor = frame.diagonal, frame.chol
    size = len(d)
    groups = [np.flatnonzero(channel_indices == j) for j in np.unique(channel_indices)]
    # The final height column has its own mother-norm block.
    groups = [group[group != size-1] for group in groups]
    groups = [group for group in groups if len(group)]+[np.asarray([size-1])]
    exact_blocks = True
    for group in groups:
        off = np.array(factor[group], copy=True)
        off[:, group] = 0.
        if np.any(off != 0):
            exact_blocks = False
            break
    scaled = normal/d[:, None]/d[None]
    if exact_blocks:
        left = np.empty_like(scaled)
        for group in groups:
            local = factor[np.ix_(group, group)]
            left[group] = solve_triangular(local, scaled[group], lower=True, check_finite=False)
        result = np.empty_like(scaled)
        for group in groups:
            local = factor[np.ix_(group, group)]
            result[:, group] = solve_triangular(local, left[:, group].T, lower=True, check_finite=False).T
    else:
        left = solve_triangular(factor, scaled, lower=True, check_finite=False)
        result = solve_triangular(factor, left.T, lower=True, check_finite=False).T
    if not np.all(np.isfinite(result)):
        raise ArithmeticError('Nonfinite current coarse data Gram after the retained whitening')
    skew = float(np.max(np.abs(result-result.T), initial=0.))
    result = .5*result+.5*result.T
    return result, dict(actual_original_R_retained=True,
        whitening='G_c=L_N^-1 D^-1 N D^-1 L_N^-T; no new R',
        exact_channel_and_height_blocks=exact_blocks,
        maximum_exact_block_size=max(map(len, groups)) if exact_blocks else size,
        block_count=len(groups) if exact_blocks else 1,
        cross_block_threshold=0., float_skew_before_symmetrization=skew,
        source_changes_or_rewhitening=False)


def assemble_current_coarse_gram(bridge, frame, *, stage_block=8, provenance=None, progress=None):
    """Return (G_c, report), ready for frame.small_hessian/FixedSPDPreconditioner.

    bridge is the actual current frozen R664 NativeLinearization. The
    original operator must already cache its identical x via set_base.
    frame is the current original augmented basis/coordinate frame; its
    underlying arrays and the bridge must remain frozen during assembly.
    No objective, regularization, constraint, state or cache is changed.
    """
    require_actions()
    started = time.monotonic()
    source_path = Path(__file__).resolve()
    source_bytes = source_path.read_bytes()
    own_source = dict(path=str(source_path), bytes=len(source_bytes),
                      sha256=hashlib.sha256(source_bytes).hexdigest())
    o, b, parameters = bridge.original, frame.basis, bridge.parameters
    stage_block = int(stage_block)
    if stage_block < 1:
        raise ValueError('The explicit stage block must be positive')
    if frame.coordinates.problem is not o or frame.coarse_size != b.dimension:
        raise ValueError('Retain this actual complete bridge and coordinate frame')
    sources = {
        'frame': _source(type(frame).__init__, 'frame'),
        'bridge': _source(type(bridge).__init__, 'hessian'),
        'R664_blocks': _source(type(bridge.blocks).whiten_columns, 'hessian'),
        'cached_first_jet_access': _source(o._first_batch, 'batch'),
        'actual_cache_builder': _source(o.set_base, 'batch'),
        'observation_pair': _source(o._stage_pair, 'observed'),
        'unpack': _source(o.unpack, 'dense'),
        'literal_B': _source(b.free_direction, 'basis'),
        'literal_BT': _source(b.transpose_free, 'basis'),
        'literal_B_candidate': _source(b.candidate, 'basis_base'),
    }
    tail = getattr(o, 'reference_tail_context', None)
    native_tail = getattr(b.o, 'reference_tail_context', None)
    if tail is not native_tail:
        raise ValueError('The literal nodal height and full field must use the same actual lift context')
    if tail is None:
        sources['first_jet_builder'] = _source(o._first_batch_uncached, 'batch')
        model = dict(representation='original analytic lift', reference_tail_lambda=0.)
    else:
        sources['first_jet_builder'] = _source(o._first_batch_uncached, 'reference_tail')
        sources['reference_definition'] = _source(tail.definition, 'reference_tail')
        definition = tail.definition()
        identity = hashlib.sha256(json.dumps(definition, sort_keys=True,
            separators=(',', ':'), allow_nan=False).encode()).hexdigest()
        model = dict(representation='R671 exact reference tail lift',
            reference_tail_lambda=float(tail.lambda_value), model_definition=definition,
            model_identity_sha256=identity)
    if (o._base_x is None or o._base_p is None or o._base_first is None
            or not np.array_equal(o._base_x, bridge.x)):
        raise ValueError('Supply the existing complete cache at the actual bridge.x; no new field is evaluated here')
    if any(getattr(b.o, key) != getattr(o, key) for key in ('J', 'n', 'M', 'K', 'free_size')):
        raise ValueError('The original native B and complete field have different layouts')
    if (not np.array_equal(b.o.mesh, o.mesh) or not np.array_equal(b.o.phi, o.phi)
            or not np.array_equal(b.o.freq, o.freq)):
        raise ValueError('Retain all actual nodes, angular rows and modes in B')
    P, N, dimension = int(o.P), int(o.N), int(b.dimension)
    first = o._base_first
    if first.shape != (2, P, N, 3) or np.iscomplexobj(first):
        raise ValueError('Need the complete cached moving-frame first jets')
    rho = np.array(_real(o._base_p.rho, (N,), 'current full-M rho'), copy=True)
    a = np.array(_real(o.a, (P,), 'original target a'), copy=True)
    radial = np.array(_real(bridge.radial, (P,), 'full radial weights', positive=True), copy=True)
    orbit = np.array(_real(o.multiplicity, (N,), 'original angular orbit multiplicities', positive=True), copy=True)
    phi = np.array(_real(o.phi, (N,), 'original angular grid'), copy=True)
    if float(np.sum(orbit)) != int(o.full_N):
        raise ValueError('Original angular orbit weights must cover the declared full grid exactly')
    if bridge.blocks.parameters is not parameters:
        raise ValueError('Use the same frozen R664 parameters as the actual bridge')
    for key in ('axis', 'offaxis', 'root_plus', 'root_off', 'root_minus'):
        if np.shape(getattr(bridge.blocks, key)) != (P, N):
            raise ValueError('R664 blocks must retain every actual stage and angle')
    cells = np.asarray(o.observation_cells)
    weights = _real(o.observation_weights, (P, 3, 6), 'complete observation weights')
    if (cells.shape != (P,) or not np.issubdtype(cells.dtype, np.integer)
            or np.any(cells < 0) or np.any(cells >= o.J-1)
            or o.lift_scalar.shape != (P, 6)):
        raise ValueError('Use the actual complete observation plan and six physical h/f scalars')
    pairs = np.asarray(b.pairs)
    if pairs.shape != (dimension, 2):
        raise ValueError('Literal coarse pairs changed')
    ri, cj = pairs.T
    nodes = np.array(_real(b.node_jets, (b.nb, o.J, 3), 'literal nodal coarse three jets'), copy=True)
    # These are precisely the original free_direction/unpack fixed slots.
    nodes[:, 0, :2] = 0.
    nodes[:, -1, :] = 0.
    for radial_index, channel_index in pairs:
        if b.channels[channel_index][0] == 'Z' and nodes[radial_index, 0, 2] != 0:
            raise ValueError('Published Z coarse columns have zero fixed A0_Z; an altered basis needs its own literal expansion')
    if tuple(pairs[-1]) != (b.height_radial, 1):
        raise ValueError('Use the actual final physical-height coarse column')
    nodal = nodes.transpose(1, 2, 0)
    angular = _AngularMoments(b.channels, phi, orbit)
    normalizer = float(np.sum(radial))*int(o.full_N)
    gamma = float(parameters.k)/(float(parameters.scale)**2*normalizer)
    if not np.isfinite(gamma) or gamma <= 0:
        raise ValueError('The original normalized-Phi external half-Hessian factor must be positive')
    normal = np.zeros((dimension, dimension))
    maximum_active = 0
    zero_column_stages = 0
    assembled_stages = 0
    for start in range(0, P, stage_block):
        stop = min(start+stage_block, P)
        V, d = first[0, start:stop], first[1, start:stop]
        ar = a[start:stop, None]*rho[None]
        if (not np.all(np.isfinite(V)) or not np.all(np.isfinite(d))
                or not np.all(np.isfinite(ar)) or np.any(ar == 0)):
            raise ArithmeticError('Nonfinite current cached geometry or zero target Gram denominator')
        # Cache components ALREADY use rotating-phi R/T/Z. No second O.
        derivative = np.zeros((stop-start, N, 3, 6))
        derivative[:, :, 0, :3] = 2*V
        derivative[:, :, 1, :3] = d/ar[:, :, None]
        derivative[:, :, 1, 3:] = V/ar[:, :, None]
        derivative[:, :, 2, 3:] = 2*d/(ar*ar)[:, :, None]
        block = _block_view(bridge.blocks, start, stop)
        weighted = block.whiten_columns(derivative)
        # Sloc = Dloc^T L Dloc, including the full current R664 block.
        tensor = weighted.transpose(0, 1, 3, 2)@weighted
        kernels = angular.contract(tensor)
        y, u = _radial_pair(o, nodal, b.height_radial, start, stop)
        c = angular.nc
        for local, stage in enumerate(range(start, stop)):
            by, bu = y[local, ri], u[local, ri]
            active = np.flatnonzero((by != 0)|(bu != 0))
            maximum_active = max(maximum_active, len(active))
            if not len(active):
                zero_column_stages += 1
                continue
            channel = cj[active]
            ix = np.ix_(channel, channel)
            ku = kernels[local, :c, :c][ix]
            kuy = kernels[local, :c, c:][ix]
            ky = kernels[local, c:, c:][ix]
            v, z = bu[active], by[active]
            increment = (np.outer(v, v)*ku+np.outer(v, z)*kuy
                +np.outer(z, v)*kuy.T+np.outer(z, z)*ky)
            normal[np.ix_(active, active)] += radial[stage]*increment
        assembled_stages = stop
        if progress is not None:
            progress(dict(event='current_coarse_moments_block', stages_done=stop,
                total_stages=P, maximum_active_coarse_columns=maximum_active,
                elapsed_seconds=time.monotonic()-started))
    normal *= gamma
    if not np.all(np.isfinite(normal)):
        raise ArithmeticError('Nonfinite accumulated current coarse data Gram')
    raw_skew = float(np.max(np.abs(normal-normal.T), initial=0.))
    normal = .5*normal+.5*normal.T
    result, whitening = _apply_original_whitening(normal, frame, cj)
    report = dict(schema=SCHEMA, status='assembled_current_normalized_coarse_data_Gram',
        assembly_source=own_source,
        sources=sources, v7_algebraically_equivalent_normal_source_sha256=V7_EQUIVALENT_SOURCE_SHA256,
        caller_provenance=dict(provenance or {}), model=model,
        actual_x_sha256=_array_sha(bridge.x), actual_scale_sha256=_array_sha(frame.scale),
        actual_coarse_diagonal_sha256=_array_sha(frame.diagonal),
        actual_coarse_cholesky_sha256=_array_sha(frame.chol),
        literal_nodal_basis_sha256=_array_sha(b.node_jets),
        original_mesh_sha256=_array_sha(o.mesh), original_angles_sha256=_array_sha(phi),
        actual_target_a_sha256=_array_sha(a), actual_rho_sha256=_array_sha(rho),
        actual_radial_weights_sha256=_array_sha(radial), actual_orbit_weights_sha256=_array_sha(orbit),
        p=int(parameters.p), epsilon=float(parameters.epsilon), spectral_scale=float(parameters.scale),
        normalization=normalizer, outer_half_hessian_factor=gamma,
        actual_bridge_true_gradient_factor=float(bridge.true_gradient_factor),
        units='G_c=A_c^T A_c with complete normalized-Phi factor k/(scale^2*C0); no damping',
        rows=P*N*3, full_rows=P*int(o.full_N)*3,
        stages=P, evaluated_angles=N, full_angles=int(o.full_N),
        full_field_M=int(o.M), coarse_maximum_mode=angular.max_mode,
        coarse_variables=dimension, angular_channels=angular.nc,
        angular_moment_orders=angular.span, cosine_and_sine_columns=2*angular.span,
        symmetric_six_tensor_components=21, stage_block=stage_block,
        assembled_stages=assembled_stages, zero_column_stages=zero_column_stages,
        maximum_active_coarse_columns=maximum_active,
        radial_weight_minimum=float(radial.min()), radial_weight_sum=float(radial.sum()),
        orbit_weight_minimum=float(orbit.min()), orbit_weight_sum=float(orbit.sum()),
        representation='Already-moving R/T/Z cache; Dloc and Sloc use the same frame; no repeated Cartesian rotation',
        physical_height='Hermite_mesh(literal nodal b-h)+actual h, with its actual first derivative',
        reference_fixed_kprime_in_current_cache=tail is not None,
        coarse_core_c_variation=False, original_core_A0_columns_retained=True,
        all_current_field_modes_retained=True, every_original_positive_weight_row_retained=True,
        angular_tensor_bandlimit_assumed=False, orbit_weight_applied_once=True,
        extra_Frobenius_sqrt2_applied=False, actual_R664_Hessian_used=True,
        finite_frequency_reconstruction='Pointwise cos/sin product identities; current Sloc remains full',
        raw_coarse_float_skew=raw_skew, whitening=whitening,
        output_bytes=int(result.nbytes),
        memory_scope='One coarse dense output and several same-size whitening temporaries; block six-tensors only; existing current cache/bridge arrays are shared',
        angular_work_order='P*N*21*(4*m_c+2) plus finite channel algebra; no coarse or free unit-J sweep',
        radial_work_order='sum_s active_coarse_columns(s)^2',
        physical_fields_or_cache_rebuilt=False, J_calls=0, JT_calls=0,
        unit_column_probes=0, fixtures=0, objective_or_regularization_changed=False,
        original_B_or_R_mutated=False, PCG_or_full_driver_implemented=False,
        full_x_Hessian_claimed=False, floating_outward_certificate=False,
        elapsed_seconds=time.monotonic()-started)
    return result, report

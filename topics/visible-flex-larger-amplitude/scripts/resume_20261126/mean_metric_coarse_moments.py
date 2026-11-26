#!/usr/bin/env python3
"""R688 complete NEW mean-metric coarse Gram by exact two-mean corrections.

Use the actual R684 wrapper, its cached current mean state and current R664
blocks. Every frozen literal coarse B column has zero core-c variation, so
rho and the normalized material averaging weights have zero derivative on
this coarse space. The two normalization derivatives are retained exactly.
The full solver still uses the complete mean/rho J/J* on all variables.

The two-mean derivative expansion is ordinary floating algebra, not a PSD or
outward certificate. Record cancellation and do not clip negative spectra.
A small-Hessian Cholesky failure must select an explicit original-QP
fallback. Import defines code only. Scientific execution is public Actions.
Actual extra operator-call counts belong to the caller's runtime counters.
"""
import copy
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.linalg import solve_triangular


SCHEMA = 'R688-current-mean-metric-complete-coarse-moments-v1'
SOURCE_SHA256 = {
    'mean_transform': 'b7eb35d5e7c1d32baf8d4e94c0c9651d46d5cbfea65a6c1c098ae24d42f0b624',
    'frame': '324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da',
    'hessian': '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4',
    'batch': '02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a',
    'observed': '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d',
    'dense': 'e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d',
    'basis': '118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8',
    'basis_base': '1da3fac6c2050f9615c9c023e87e58a67e1d36cb578e791abb8903a771d2bfc7',
    'reference_tail': '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216',
}
ORIGINAL_MOMENTS_SOURCE_SHA256 = 'da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719'


class CoarseLayoutUnavailable(ValueError):
    """This shortcut cannot establish zero core variation for every column.

    The caller may explicitly retain the full mean-metric v3 solve. Do not
    replace missing material-weight derivatives by zero for another basis.
    """



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
        self.linear_terms = terms
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

    def contract_linear(self, moving_covectors):
        """All orbit-weighted first moments in the same velocity/position channels.

        Input [block, angle, six_component, output_component]; return
        [block, 2*channel, output_component]. Multiplicity occurs once.
        """
        value = np.asarray(moving_covectors)
        if value.ndim != 4 or value.shape[1] != self.tests.shape[0] or value.shape[2] != 6:
            raise ValueError('Need the full-angle six-frame linear covectors')
        moments = value.transpose(0, 2, 3, 1)@self.tests
        result = np.zeros((len(value), self.dimension, value.shape[-1]), dtype=value.dtype)
        for channel, terms in enumerate(self.linear_terms):
            for component, sine, mode, coefficient in terms:
                tone = self.span+mode if sine else mode
                result[:, channel] += coefficient*moments[:, component, :, tone]
        return result

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

    bridge is R664 NativeLinearization on the actual R684 mean wrapper.
    Both wrapper and physical base must cache the identical current x.
    The actual original frame and whitening stay fixed. The exact source
    contract establishes zero core variation on every literal B column;
    without that contract this function explicitly declines the shortcut.
    No objective, regularization, constraint, state or cache is changed.
    """
    require_actions()
    started = time.monotonic()
    source_path = Path(__file__).resolve()
    source_bytes = source_path.read_bytes()
    own_source = dict(path=str(source_path), bytes=len(source_bytes),
                      sha256=hashlib.sha256(source_bytes).hexdigest())
    mean, b, parameters = bridge.original, frame.basis, bridge.parameters
    _source(type(mean).__init__, 'mean_transform')
    _source(type(mean).jvp, 'mean_transform')
    _source(type(mean).vjp, 'mean_transform')
    o = mean.original_operator
    if (mean._design_x is None or mean._design_transform is None
            or not np.array_equal(mean._design_x, bridge.x)):
        raise ValueError('Use the existing actual cached mean state, without a new residual read')
    mean_state = mean._design_transform
    stage_block = int(stage_block)
    if stage_block < 1:
        raise ValueError('The explicit stage block must be positive')
    if frame.coordinates.problem is not mean or frame.coarse_size != b.dimension:
        raise ValueError('Retain this actual complete bridge and coordinate frame')
    try:
        literal_sources = {
            'literal_B': _source(b.free_direction, 'basis'),
            'literal_BT': _source(b.transpose_free, 'basis'),
            'literal_B_candidate': _source(b.candidate, 'basis_base'),
        }
    except ValueError as error:
        raise CoarseLayoutUnavailable(
            'The complete published B source establishing an identically zero core block is unavailable: '+str(error)) from error
    sources = {
        'mean_wrapper': _source(type(mean).__init__, 'mean_transform'),
        'mean_complete_J': _source(type(mean).jvp, 'mean_transform'),
        'mean_complete_Jstar': _source(type(mean).vjp, 'mean_transform'),
        'frame': _source(type(frame).__init__, 'frame'),
        'bridge': _source(type(bridge).__init__, 'hessian'),
        'R664_blocks': _source(type(bridge.blocks).whiten_columns, 'hessian'),
        'cached_first_jet_access': _source(o._first_batch, 'batch'),
        'actual_cache_builder': _source(o.set_base, 'batch'),
        'observation_pair': _source(o._stage_pair, 'observed'),
        'unpack': _source(o.unpack, 'dense'),
        **literal_sources,
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
    if (mean_state.averaging != mean.averaging
            or not np.array_equal(mean_state.multiplicity, orbit)
            or not np.array_equal(mean_state.density, rho)):
        raise ValueError('The actual mean transform and physical cache have different angular weights or rho')
    mean_E = _real(mean_state.radial, (P,), 'actual current mean radial target', positive=True)
    mean_C = _real(mean_state.angular, (P,), 'actual current mean angular target', positive=True)
    mean_cross = _real(mean_state.cross_scale, (P,), 'actual current cross normalization', positive=True)
    mean_raw = _real(mean_state.result, (P, N, 3), 'actual current new-target residual')
    mean_weights = _real(mean_state.omega, (N,), 'actual normalized mean angular weights', positive=True)
    # contract_linear already multiplies by orbit, so this supplies the
    # different normalized mean measure exactly once, including rho.
    mean_weight_over_orbit = mean_weights/orbit
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
    cancellation = dict(maximum_local_K00_entry=0., maximum_local_cross_entry=0.,
        maximum_local_restore_entry=0., maximum_local_corrected_entry=0.,
        maximum_local_correction_skew=0., maximum_finite_scale_ratio=0.,
        nonzero_terms_with_zero_corrected_scale=0, exact_zero_term_stages=0)
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
        E, C, S = mean_E[start:stop], mean_C[start:stop], mean_cross[start:stop]
        row_scale = np.stack((1/E, 1/S, 1/C), axis=1)
        weighted = block.whiten_columns(derivative*row_scale[:, None, :, None])
        # K00 includes NEW residual Hessian blocks and local normalization.
        tensor = weighted.transpose(0, 1, 3, 2)@weighted
        kernels = angular.contract(tensor)
        current = mean_raw[start:stop]
        target_columns = np.zeros((stop-start, N, 3, 2))
        target_columns[:, :, 0, 0] = (1+current[:, :, 0])/E[:, None]
        target_columns[:, :, 1, 0] = .5*current[:, :, 1]/E[:, None]
        target_columns[:, :, 1, 1] = .5*current[:, :, 1]/C[:, None]
        target_columns[:, :, 2, 1] = (1+current[:, :, 2])/C[:, None]
        weighted_target = block.whiten_columns(target_columns)
        cross_tensor = weighted.transpose(0, 1, 3, 2)@weighted_target
        K0U = angular.contract_linear(cross_tensor)
        KUU = np.sum((weighted_target.transpose(0, 1, 3, 2)@weighted_target)
            *orbit[None, :, None, None], axis=1)
        # Every coarse column has dc=0, hence drho=domega=0. The two
        # derivative means still depend on the complete raw Gram variation.
        mean_covectors = derivative[:, :, [0, 2], :].transpose(0, 1, 3, 2)
        mean_covectors = mean_covectors*mean_weight_over_orbit[None, :, None, None]
        mean_columns = angular.contract_linear(mean_covectors)
        cross = K0U@mean_columns.transpose(0, 2, 1)
        restore = mean_columns@KUU@mean_columns.transpose(0, 2, 1)
        for local in range(stop-start):
            a0 = float(np.max(np.abs(kernels[local]), initial=0.))
            a1 = float(np.max(np.abs(cross[local]), initial=0.))
            a2 = float(np.max(np.abs(restore[local]), initial=0.))
            kernels[local] -= cross[local]+cross[local].T
            kernels[local] += restore[local]
            corrected = float(np.max(np.abs(kernels[local]), initial=0.))
            skew = float(np.max(np.abs(kernels[local]-kernels[local].T), initial=0.))
            for key, value in (('maximum_local_K00_entry', a0),
                    ('maximum_local_cross_entry', a1), ('maximum_local_restore_entry', a2),
                    ('maximum_local_corrected_entry', corrected),
                    ('maximum_local_correction_skew', skew)):
                cancellation[key] = max(cancellation[key], value)
            numerator = a0+2*a1+a2
            if corrected > 0:
                ratio = numerator/corrected
                if np.isfinite(ratio):
                    cancellation['maximum_finite_scale_ratio'] = max(
                        cancellation['maximum_finite_scale_ratio'], ratio)
                else:
                    raise ArithmeticError('Nonfinite low-rank cancellation scale ratio')
            elif numerator > 0:
                cancellation['nonzero_terms_with_zero_corrected_scale'] += 1
            else:
                cancellation['exact_zero_term_stages'] += 1
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
            progress(dict(event='mean_metric_coarse_moments_block', stages_done=stop,
                total_stages=P, maximum_active_coarse_columns=maximum_active,
                elapsed_seconds=time.monotonic()-started))
    normal *= gamma
    if not np.all(np.isfinite(normal)):
        raise ArithmeticError('Nonfinite accumulated current coarse data Gram')
    raw_skew = float(np.max(np.abs(normal-normal.T), initial=0.))
    raw_diagonal = np.diag(normal)
    raw_diagonal_min = float(np.min(raw_diagonal))
    raw_negative_diagonal_count = int(np.count_nonzero(raw_diagonal < 0))
    raw_maximum_entry = float(np.max(np.abs(normal), initial=0.))
    normal = .5*normal+.5*normal.T
    result, whitening = _apply_original_whitening(normal, frame, cj)
    report = dict(schema=SCHEMA, status='assembled_current_NEW_mean_normalized_coarse_data_Gram',
        assembly_source=own_source,
        sources=sources, original_moment_assembly_source_sha256=ORIGINAL_MOMENTS_SOURCE_SHA256,
        old_untransformed_coarse_Gram_used=False,
        mean_target_averaging=mean.averaging,
        actual_mean_E_sha256=_array_sha(mean_E), actual_mean_C_sha256=_array_sha(mean_C),
        actual_mean_weights_sha256=_array_sha(mean_weights),
        actual_NEW_relative_residual_sha256=_array_sha(mean_raw),
        exact_coarse_derivative='Jmean_B = D Jold_B - U M; M has both complete angular derivative means',
        low_rank_update='Knew=K00-K0U M-M^T K0U^T+M^T KUU M; M here is 2 by channel',
        material_weight_derivative_on_coarse_space='Identically zero: bound free_direction starts with np.zeros(M-K) for every coefficient vector',
        zero_core_contract_scope='All literal B columns, including core acceleration and H; not the full free space',
        full_free_core_mean_weight_derivatives_still_required=True,
        signed_low_rank_cancellation=cancellation,
        raw_coarse_diagonal_minimum=raw_diagonal_min,
        raw_negative_diagonal_count=raw_negative_diagonal_count,
        raw_coarse_maximum_absolute_entry=raw_maximum_entry,
        eigenvalue_clipping=False, jitter_added=False,
        small_SPD_failure_scope='Caller adds the actual damping/mother-norm contribution and tries Cholesky; arithmetic failure may select unchanged full-mean v3 QP, not false geometry infeasibility',
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
        units='G_c=A_mean_coarse^T A_mean_coarse for the actual moving mean target and its current normalized Phi; factor k/(scale^2*C0), no damping',
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
        angular_work_order='Original full-angle 21 tensor moments plus full-angle 6x2 first moments for each of the two-mean derivative and cross term; no coarse or free unit-J sweep',
        radial_work_order='sum_s active_coarse_columns(s)^2',
        assembly_uses_existing_cache_only=True,
        expected_extra_J_calls_by_formula=0, expected_extra_JT_calls_by_formula=0,
        actual_operator_call_counts_must_be_recorded_by_caller=True,
        unit_column_probes=0, fixtures=0, current_design_objective_or_regularization_changed=False,
        old_fixed_metric_inherited=False, frozen_final_target_claimed=False,
        original_B_or_R_mutated=False, PCG_or_full_driver_implemented=False,
        full_x_Hessian_claimed=False, floating_outward_certificate=False,
        elapsed_seconds=time.monotonic()-started)
    return result, report


class _ActualOperatorCounts:
    """Count actual wrapper/base entry calls only while preparing this metric.

    Nested calls are reported by role, not falsely summed as independent
    scientific products. Every patched instance attribute is restored.
    The assembler binds the class source, so counting does not change its
    declared implementation identity or the physical state.
    """

    def __init__(self, mean):
        self.counts = {}
        self.saved = []
        self.objects = [('wrapper', mean), ('physical_base', mean.original_operator)]

    def __enter__(self):
        try:
            for role, obj in self.objects:
                for name in ('jvp', 'vjp', 'residual', 'raw_residual'):
                    method = getattr(obj, name)
                    key = role+'.'+name
                    self.counts[key] = 0
                    present = name in vars(obj)
                    old_value = vars(obj).get(name)
                    def counted(*args, _method=method, _key=key, **kwargs):
                        self.counts[_key] += 1
                        return _method(*args, **kwargs)
                    self.saved.append((obj, name, present, old_value))
                    setattr(obj, name, counted)
        except BaseException:
            self.__exit__(None, None, None)
            raise
        return self

    def __exit__(self, exc_type, exc, traceback):
        for obj, name, present, old_value in reversed(self.saved):
            if present:
                setattr(obj, name, old_value)
            else:
                delattr(obj, name)
        self.saved.clear()
        return False


def prepare_current_mean_preconditioner(frame_module, coordinates, height_map,
        basis, diagonal, chol, bridge, damping, *, stage_block=8,
        provenance=None, progress=None):
    """Prepare the unchanged-QP SPD map, or explicitly select original v3.

    Every success and handled arithmetic/layout failure returns actual
    call counters. Source/state/model misuse other than the declared
    zero-core shortcut limitation propagates. An externally killed process
    cannot return a fallback and must never be reported as doing so.
    """
    require_actions()
    started = time.monotonic()
    detail = dict(enabled=True, status='construction_started',
        actual_direction_damping=float(damping),
        unchanged_current_mean_QP=True, old_fixed_target_used=False,
        current_complete_mean_bridge_reused=True,
        original_coarse_diagonal_and_cholesky_reused=True,
        planned_operator_calls_from_formula=0,
        numerical_execution_returned=False)
    counter = _ActualOperatorCounts(bridge.original)
    frame = gram = None
    try:
        with counter:
            mu = float(damping)
            if not np.isfinite(mu) or mu <= 0:
                raise ValueError('Use the actual positive finite damping')
            mu_squared = mu*mu
            if not np.isfinite(mu_squared) or mu_squared <= 0:
                raise frame_module.SmallSPDUnavailable('actual damping squared',
                    'Not representable as a finite positive float')
            beta = 1./mu_squared
            if not np.isfinite(beta) or beta <= 0:
                raise frame_module.SmallSPDUnavailable('background inverse scale',
                    'The explicit beta=1/mu^2 is not finite positive')
            detail['background_inverse_scale'] = beta
            # Establish the all-column zero-core contract BEFORE even the
            # original frame's specialized literal-mother construction.
            try:
                _source(basis.free_direction, 'basis')
                _source(basis.transpose_free, 'basis')
                _source(basis.candidate, 'basis_base')
            except ValueError as error:
                raise CoarseLayoutUnavailable(
                    'The all-column zero-core source contract is not established: '+str(error)) from error
            frame = frame_module.CoarseFrame(coordinates, height_map, basis,
                diagonal, chol, provenance=provenance)
            detail['frame'] = frame.metadata()
            gram, data_report = assemble_current_coarse_gram(bridge, frame,
                stage_block=stage_block, provenance=provenance, progress=progress)
            detail['current_mean_coarse_data_Gram'] = data_report
            preconditioner = frame_module.FixedSPDPreconditioner(frame, gram,
                mu, beta, data_provenance=data_report)
            fixed_metadata = preconditioner.metadata()
            fixed_metadata['original_source_active_face_note'] = fixed_metadata.get('active_face_usage')
            fixed_metadata['active_face_usage'] = 'R685: B-BQ^T(QBQ^T)^-1QB; actual v5 face cache/fallback diagnostics remain authoritative'
            detail.update(status='prepared_current_mean_fixed_SPD',
                fixed_metadata=fixed_metadata, fallback_to_frozen_v3=False)
            return preconditioner, detail
    except CoarseLayoutUnavailable as error:
        detail.update(status='zero_core_coarse_contract_unavailable_frozen_v3_selected',
            failure=dict(kind=type(error).__name__, reason=str(error)),
            fallback_to_frozen_v3=True,
            unproved_material_weight_derivative_omitted=False,
            full_mean_J_and_Jstar_retained=True)
        return None, detail
    except frame_module.SmallSPDUnavailable as error:
        detail.update(status='small_SPD_unavailable_frozen_v3_selected',
            failure=error.record(), fallback_to_frozen_v3=True,
            numerical_failure_is_not_physical_infeasibility=True,
            no_jitter_no_clipping_no_changed_damping=True)
        return None, detail
    except (ArithmeticError, MemoryError) as error:
        detail.update(status='arithmetic_or_resource_unavailable_frozen_v3_selected',
            failure=dict(kind=type(error).__name__, reason=str(error)),
            fallback_to_frozen_v3=True,
            numerical_failure_is_not_physical_infeasibility=True,
            no_jitter_no_clipping_no_changed_damping=True)
        return None, detail
    finally:
        observed = dict(counter.counts)
        detail.update(construction_seconds=time.monotonic()-started,
            actual_operator_entry_calls=observed,
            operator_instrumentation_complete=len(observed)==8,
            actual_operator_call_scope='Separate wrapper and physical-base entries; nested calls are not independent products',
            actual_additional_J_calls=observed.get('physical_base.jvp'),
            actual_additional_Jstar_calls=observed.get('physical_base.vjp'),
            all_observed_J_and_Jstar_entries_zero=bool(len(observed)==8 and all(
                value == 0 for key, value in observed.items()
                if key.endswith('.jvp') or key.endswith('.vjp'))),
            all_observed_residual_entries_zero=bool(len(observed)==8 and all(
                value == 0 for key, value in observed.items()
                if key.endswith('.residual') or key.endswith('.raw_residual'))),
            temporary_method_wrappers_restored=not counter.saved,
            numerical_execution_returned=True,
            dense_Gram_reference_released_before_solve=True,
            no_unit_column_probe_or_fixture=True)
        del gram, frame

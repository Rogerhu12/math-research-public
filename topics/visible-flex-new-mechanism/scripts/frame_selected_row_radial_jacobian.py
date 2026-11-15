#!/usr/bin/env python3
"""Selected scalar rows of the existing 159-coordinate field, factored radially.

This module changes no ordinary geometry or physical gate.  It never builds the
original 163-parameter position-Jacobian tensor.  Complete angular kernels are
formed on the old uniform circle; only then are points selected and the three
radial jet directions contracted by the frozen eleven-row derivative API.

No research or development entry point is executed by importing this module.
New development and actual use are owned by the public Actions driver.
"""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import periodic_operator, target_frame
from frame_entry_single_q import SingleQProblem, SingleQGrid, complete_tangent_parameter_jets
from frame_entry_paired_repair import EntryRepairGrid
from frame_five_height_field import FiveHeightField
from frame_height_null_coordinates import digest
from frame_metric_spectral_recovery import (
    POLICY as SPECTRAL_POLICY, EPSILON_EXACT,
    selected_spectral_parameter_jacobian)
import frame_metric_budget_restoration_rows as rows_api

POLICY = 'same159-selected-row-radial-factorization-v1'
POSITION_KEYS = ('X', 'Xs', 'Xt', 'Xss', 'Xst', 'Xtt', 'T')
FIRST_KEYS = ('X', 'Xs', 'Xt', 'T')
N = 159
SOURCE_BINDINGS = {
    'frame_entry_single_q.py': 'b0744e42b00854b85ac6828afc4520c0505b5d4800c47ab4d8bb96c84d04e286',
    'frame_entry_paired_repair.py': '8f09d96a4377175e0242a37f1450960f0914e28a787699565d437058e7625ac1',
    'frame_five_height_field.py': '549e61db392f318260d636d41a090bd56e8c96b2eab580075707b5e25a24f656',
    'frame_metric_spectral_recovery.py': '27fcdbc71a6d9d07e0cba962067e61d7f8439ef06d47cdbdf9c669ce1ea2c428',
    'frame_metric_budget_restoration_rows.py': 'eff06d6c2136b8b13fa86afe915352ee54e5aaae2c4c80551a08355cea2e1d4f',
    'frame_curvature_epigraph_exchange.py': '8c26353df012ca61f37149b2e2ab52acaec4ca22fde68017261c0bd68992ebf5',
    'frame_collar_bvp.py': '64dffdbfc6456fe022105d264442d307c8f88022cdf755ec0a41ea97fff93d00',
}


def implementation_hashes():
    root = Path(__file__).parent
    result = {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
              for name in SOURCE_BINDINGS}
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def verify_sources():
    result = implementation_hashes()
    changed = [name for name, expected in SOURCE_BINDINGS.items()
               if result[name] != expected]
    if changed:
        raise ValueError('frozen radial-factorization source changed: ' + ','.join(changed))
    return result


def array_hash(value):
    value = np.ascontiguousarray(np.asarray(value))
    h = hashlib.sha256()
    h.update(str(value.dtype).encode('ascii'))
    h.update(str(tuple(value.shape)).encode('ascii'))
    h.update(value.tobytes())
    return h.hexdigest()


def _same_bytes(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def _slice_equal(value, start, stop):
    return (isinstance(value, slice) and value.start == start
            and value.stop == stop and value.step in (None, 1))


def _finite(value, shape, label):
    value = np.asarray(value, float)
    if value.shape != shape or not np.all(np.isfinite(value)):
        raise ValueError('finite original layout required: ' + label)
    return value


class _AngularOnlyGrid:
    """The old analytic tangent formula, with R=1, R'=R''=0.

    This is a derivative-array adapter, not a physical geometry evaluator.
    No old 81/73-column basis_jacobian method is called.
    """
    def __init__(self, name, nr, angular, angular_first):
        self.name = name
        self.angular = np.asarray(angular, float)
        self.first = np.asarray(angular_first, float)
        if (self.angular.ndim != 2 or self.first.shape != self.angular.shape
                or not np.all(np.isfinite(self.angular))
                or not np.all(np.isfinite(self.first))):
            raise ValueError('finite same-layout original angular modes required')
        self.shape = (nr,) + self.angular.shape
        self.zero = np.zeros(self.shape, float)

    def basis_jacobian(self, name, kind='value'):
        if name != self.name:
            raise ValueError('angular adapter used with a different field')
        if kind == 'value':
            return np.broadcast_to(self.angular[None, :, :], self.shape)
        if kind == 'theta':
            return np.broadcast_to(self.first[None, :, :], self.shape)
        if kind in ('s', 'ss'):
            return self.zero
        raise ValueError('unsupported derivative kind')


def angular_kernels(fields, frame, name, angular, angular_first, *, second):
    """Return true F0/F1/F2/Ftheta and the SAME full-circle Pi_N kernels."""
    nr = fields[name]['value'].shape[0]
    adapter = _AngularOnlyGrid(name, nr, angular, angular_first)
    jets = complete_tangent_parameter_jets(
        adapter, fields, frame, name, order=2 if second else 1)
    result = {
        'F0': jets['T'], 'F1': jets['Ts'], 'Ftheta': jets['Ttheta'],
        'P0': periodic_operator(jets['T'], -1),
        'P1': periodic_operator(jets['Ts'], -1)}
    if second:
        result['F2'] = jets['Tss']
        result['P2'] = periodic_operator(jets['Tss'], -1)
    if any(not np.all(np.isfinite(v)) for v in result.values()):
        raise FloatingPointError('nonfinite full-angle kernel')
    return result


def virtual_selected_jets(kernels, ri, ti, metric, *, second):
    """Selected physical variation arrays; parameter ordering is (jet, mode).

    The last axis is at most 3*9.  It contains algebraic virtual directions,
    not newly optimized parameters.  Angular position jets use the parent
    definitions, never D_theta Pi_N=id.
    """
    ri, ti = np.asarray(ri, int), np.asarray(ti, int)
    selected = {k: np.asarray(v)[ri, ti] for k, v in kernels.items()}
    f0, f1, ft = (selected[k] for k in ('F0', 'F1', 'Ftheta'))
    p0, p1 = (selected[k] for k in ('P0', 'P1'))
    radius, first, second_a = (
        np.asarray(metric[k], float)[ri, None, None]
        for k in ('a', 'a_s', 'a_ss'))
    zero = np.zeros_like(f0)
    values = {
        'T': (f0, zero, zero),
        'X': (radius*p0, zero, zero),
        'Xs': (first*p0 + radius*p1, radius*p0, zero),
        'Xt': (radius*f0, zero, zero)}
    if second:
        p2 = selected['P2']
        values.update(
            Xss=(second_a*p0 + 2*first*p1 + radius*p2,
                 2*first*p0 + 2*radius*p1, radius*p0),
            Xst=(first*f0 + radius*f1, radius*f0, zero),
            Xtt=(radius*ft, zero, zero))
    answer = {key: np.stack(parts, axis=-2).reshape(
        len(ri), 3, 3*f0.shape[-1]) for key, parts in values.items()}
    if any(not np.all(np.isfinite(v)) for v in answer.values()):
        raise FloatingPointError('nonfinite selected virtual geometry jet')
    return answer


def expand_radial_rows(local, radial, ri):
    """L0*R + L1*R' + L2*R'', with original radial-major/mode-minor columns."""
    ri = np.asarray(ri, int)
    local = np.asarray(local, float)
    if local.ndim != 2 or local.shape[0] != len(ri) or local.shape[1] % 3:
        raise ValueError('selected (radial jet, angular mode) row shape required')
    modes = local.shape[1] // 3
    coeff = local.reshape(len(ri), 3, modes)
    rr = [np.asarray(x, float)[ri] for x in radial]
    if any(v.ndim != 2 or v.shape != rr[0].shape for v in rr):
        raise ValueError('three equally shaped original radial jets required')
    result = sum(coeff[:, k, None, :]*rr[k][:, :, None] for k in range(3))
    return result.reshape(len(ri), rr[0].shape[1]*modes)


def selected_null_height_jets(field, radial, ri, *, second):
    """Five exact-null columns; no rounded nine-height physical surrogate."""
    t = np.asarray(radial, float)
    z = np.asarray(field.null_basis.values(t, integral=True), float)
    d = np.asarray(field.null_basis.values(t), float)
    dp = np.asarray(field.null_basis.values(t, 1), float)
    if any(v.shape != (len(t), 5) or not np.all(np.isfinite(v))
           for v in (z, d, dp)):
        raise ValueError('the declared five original null-height functions are required')
    answer = {}
    for key in POSITION_KEYS if second else FIRST_KEYS:
        value = np.zeros((len(ri), 3, 5))
        if key in ('X', 'Xs', 'Xss'):
            source = {'X': z, 'Xs': d, 'Xss': dp}[key]
            value[:, 2, :] = source[ri]
        answer[key] = value
    return answer


class SelectedRadialJacobian:
    """Fixed-family evaluator; its caller owns ordinary-cache provenance.

    A binding record must describe the actual current159 ordinary cache.  This
    evaluator verifies exact state/grid/reference identities, rebuilds current
    scalar fields, and checks the resulting tangent and position jets against
    that cache.  The common center and height are taken from that bound cache,
    not recomputed with a different primitive or reference.
    """
    def __init__(self, field, cfg):
        if not isinstance(field, FiveHeightField):
            raise ValueError('the declared exact FiveHeightField is required')
        old = field.original_problem
        if not isinstance(old, SingleQProblem):
            raise ValueError('the declared SingleQProblem is required')
        if (field.nunknown != N or old.nunknown != 163
                or field.metric_free != 0 or old.metric_free != 0
                or old.q_index != 153 or old.height_free != 9
                or old.source.radial_free != 9
                or not _slice_equal(old.slices.get('u'), 0, 81)
                or not _slice_equal(old.slices.get('v'), 81, 154)
                or not _slice_equal(old.slices.get('height'), 154, 163)
                or not _slice_equal(field.slices.get('height_null'), 154, 159)):
            raise ValueError('unsupported physical163/independent159 column layout')
        if (cfg.get('metric_proposal_policy') != SPECTRAL_POLICY
                or cfg.get('metric_proposal_epsilon_exact') != EPSILON_EXACT):
            raise ValueError('the frozen spectral proposal, not a different row model, is required')
        self.field, self.single, self.cfg = field, old, cfg
        self.coordinate_sha256 = field.coordinate_definition_sha256
        self.ordinary_evaluation = copy.deepcopy(field.evaluation_definition())
        self.ordinary_evaluation_sha256 = digest(self.ordinary_evaluation)
        self.configuration_sha256 = digest(cfg)
        self.fixed_source = copy.deepcopy(old.source.space_definition())
        self.fixed_source_sha256 = digest(self.fixed_source)
        self.height_reference_sha256 = digest(field.coordinates.definition)
        self.sources = verify_sources()
        self.definition = {
            'schema': POLICY,
            'coordinate_definition_sha256': self.coordinate_sha256,
            'ordinary_evaluation_definition_sha256': self.ordinary_evaluation_sha256,
            'configuration_sha256': self.configuration_sha256,
            'tangent_space_definition_sha256': self.fixed_source_sha256,
            'height_reference_definition_sha256': self.height_reference_sha256,
            'source_files_sha256': self.sources,
            'family_order': ['u:9 angular x9 radial', 'v:8 angular x9 radial',
                             'Q:1 angular x1 radial', 'height:5 exact-null columns'],
            'complete_uniform_circle_before_any_point_selection': True,
            'same_periodic_operator_order_minus_one_including_zero_and_Nyquist': True,
            'parent_angular_position_jets_used_without_Dtheta_Pi_identity': True,
            'ordinary_geometry_values_and_all_actual_gates_unchanged': True,
            'virtual_directions_are_not_new_parameters': True,
            'maximum_selected_virtual_parameter_axis': 27,
            'original163_or159_full_angle_position_Jacobian_is_not_formed': True,
            'floating_reassociation_is_not_bitwise_replay': True}
        self.definition_sha256 = digest(self.definition)

    def _assert_context(self):
        if (self.field.coordinate_definition_sha256 != self.coordinate_sha256
                or digest(self.field.coordinates.definition) != self.height_reference_sha256
                or digest(self.field.evaluation_definition()) != self.ordinary_evaluation_sha256
                or digest(self.single.source.space_definition()) != self.fixed_source_sha256
                or digest(self.cfg) != self.configuration_sha256):
            raise ValueError('selected-J context, reference, source or configuration changed')

    def bind_ordinary(self, state, radial, theta, data, *, owner):
        """Attach explicit provenance at the ordinary-cache owner, not in a loader."""
        self._assert_context()
        state = self.field.coordinates.validate(state)
        r, th = rows_api._grid(radial, theta)
        if len(th) % 4:
            raise ValueError('the supported complete circle has a multiple of four angles')
        if owner not in ('coarse-current-cache', 'fine-current-cache', 'new-artificial-current-cache'):
            raise ValueError('explicit authoritative cache owner required')
        # The frozen coarse physical_geometry copies only ordinary arrays and
        # state/radial/theta; it deliberately drops FiveHeightField metadata.
        # Its explicit owner binds this trimmed cache to the already checked
        # fixed field.  Fine and standalone field data retain their identity.
        trimmed_coarse = (owner == 'coarse-current-cache'
                          and 'coordinate_definition_sha256' not in data
                          and 'state' in data)
        if (not _same_bytes(np.asarray(data.get('radial'), float), r)
                or not _same_bytes(np.asarray(data.get('theta'), float), th)
                or (not trimmed_coarse
                    and data.get('coordinate_definition_sha256') != self.coordinate_sha256)):
            raise ValueError('ordinary cache uses a different full grid or coordinate definition')
        if 'state' in data and not _same_bytes(np.asarray(data['state'], float), state):
            raise ValueError('ordinary cache belongs to another exact state')
        for key in POSITION_KEYS:
            _finite(data[key], (len(r), len(th), 3), 'ordinary/' + key)
        _finite(data['center'], (len(r),), 'ordinary/center')
        for group, keys in [('metric', ('a', 'a_s', 'a_ss')),
                            ('height', ('b', 'b_s', 'b_ss'))]:
            for key in keys:
                _finite(data[group][key], (len(r),), group + '/' + key)
        return {
            'schema': POLICY + '-bound-ordinary',
            'state': np.asarray(state, float).copy(),
            'radial': r.copy(), 'theta': th.copy(), 'data': data,
            'owner': owner, 'factorization_definition_sha256': self.definition_sha256,
            'ordinary_evaluation_definition_sha256': self.ordinary_evaluation_sha256,
            'coordinate_definition_sha256': self.coordinate_sha256}

    def _ordinary_slice_and_replay(self, state, radial, theta, query, bound, grid, fields, frame):
        """No ordinary geometry call: compare the exact current scalar reconstruction.

        Center/height retain the authoritative current159 cache's common
        primitive.  They are never borrowed from a reference163 geometry.
        Height density jets are additionally checked against height_jets.
        """
        target = bound['data']
        local = {key: np.asarray(target[key])[query] for key in POSITION_KEYS}
        metric = {key: np.asarray(value)[query] for key, value in target['metric'].items()}
        height = {key: np.asarray(value)[query] for key, value in target['height'].items()}
        center = np.asarray(target['center'])[query]
        a, ap, app = (metric[k][:, None, None] for k in ('a', 'a_s', 'a_ss'))
        p0, p1, p2 = (periodic_operator(frame[k], -1) for k in ('T', 'Ts', 'Tss'))
        x = a*p0
        x[:, :, 2] += center[:, None]
        xs = ap*p0 + a*p1
        xs[:, :, 2] += height['b'][:, None]
        xss = app*p0 + 2*ap*p1 + a*p2
        xss[:, :, 2] += height['b_s'][:, None]
        replay = {'X': x, 'Xs': xs, 'Xss': xss, 'T': frame['T'],
                  'Xt': a*frame['T'], 'Xst': ap*frame['T']+a*frame['Ts'],
                  'Xtt': a*frame['Ttheta']}
        errors, scale = {}, 1.
        for key in POSITION_KEYS:
            if replay[key].shape != local[key].shape or not np.all(np.isfinite(replay[key])):
                raise FloatingPointError('invalid scalar reconstruction: ' + key)
            errors[key] = float(np.max(abs(replay[key]-local[key])))
            scale = max(scale, float(np.max(abs(local[key]))))
        current_height = self.field.height_jets(state, radial[query])
        for key in ('b', 'b_s', 'b_ss'):
            value = _finite(current_height[key], (len(query),), 'current-height/' + key)
            errors['height/' + key] = float(np.max(abs(value-height[key])))
            scale = max(scale, float(np.max(abs(height[key]))))
        if max(errors.values(), default=0.) > float(self.cfg['value_Jacobian_replay_relative_tolerance'])*scale:
            raise ArithmeticError('selected-J current scalar/null-height reconstruction differs from ordinary cache')
        return local, metric, errors

    def _families(self, grid, nr, nt):
        if not isinstance(grid, SingleQGrid) or not isinstance(grid.original, EntryRepairGrid):
            raise ValueError('only the frozen paired-entry SingleQ grid is supported')
        bases = [_finite(grid.bases[j], (nr, 9), 'retained B jet ' + str(j)) for j in range(3)]
        families = []
        for name, modes, start, stop in [('u', 9, 0, 81), ('v', 8, 81, 153)]:
            weight = [_finite(v, (nr,), name + '/weight') for v in grid.original.weights[name]]
            w, wp, wpp = weight
            radial = (w[:, None]*bases[0],
                      wp[:, None]*bases[0]+w[:, None]*bases[1],
                      wpp[:, None]*bases[0]+2*wp[:, None]*bases[1]+w[:, None]*bases[2])
            angular = _finite(grid.angular[name], (nt, modes), name + '/angular')
            first = _finite(grid.angular_first[name], (nt, modes), name + '/angular_first')
            families.append((name, angular, first, radial, start, stop))
        qr = tuple(_finite(v, (nr,), 'Q/radial')[:, None] for v in grid.radial_Q)
        q = _finite(grid.angular_Q, (nt,), 'Q/angular')[:, None]
        qt = _finite(grid.angular_Q_theta, (nt,), 'Q/angular_first')[:, None]
        families.append(('v', q, qt, qr, 153, 154))
        return families

    def evaluate(self, state, radial, theta, row_ids, bound, *, side, owned_width, wall=None,
                 development_direction=None):
        """Return (selected159 J, diagnostics, optional new-development six-jet direction).

        Production passes development_direction=None.  The optional output is
        a direct directional contraction of the same new virtual jets, for a
        public artificial comparison; no full parameter geometry tensor is made.
        """
        self._assert_context()
        q = self.field.coordinates.validate(state)
        r, th = rows_api._grid(radial, theta)
        if len(th) % 4 or side not in (-1, 1):
            raise ValueError('same complete angle grid and signed physical side required')
        if isinstance(owned_width, bool) or not isinstance(owned_width, (int, np.integer)) or not 1 <= owned_width <= 16:
            raise ValueError('one through sixteen owned radial rows per batch required')
        if (bound.get('schema') != POLICY + '-bound-ordinary'
                or bound.get('factorization_definition_sha256') != self.definition_sha256
                or bound.get('ordinary_evaluation_definition_sha256') != self.ordinary_evaluation_sha256
                or bound.get('coordinate_definition_sha256') != self.coordinate_sha256
                or not _same_bytes(bound['state'], q)
                or not _same_bytes(bound['radial'], r)
                or not _same_bytes(bound['theta'], th)):
            raise ValueError('selected-J ordinary binding differs from current state/grid/reference')
        raw = list(row_ids)
        if any(isinstance(v, (bool, np.bool_)) or not isinstance(v, (int, np.integer)) for v in raw):
            raise ValueError('original integer row IDs required')
        ids = np.asarray(raw, np.int64)
        count, nt = len(r)*len(th), len(th)
        if not len(ids) or np.any(ids < 0) or np.any(ids >= 11*count):
            raise ValueError('nonempty row IDs inside the original eleven-group grid required')
        # Do not sort or de-duplicate: a repeated point in distinct groups is a
        # distinct row, and caller order is the output order.
        groups, points = ids//count, ids % count
        radial_ids = np.unique(points//nt)
        result = np.empty((len(ids), N))
        covered = np.zeros(len(ids), bool)
        direct = None
        if development_direction is not None:
            direction = _finite(development_direction, (N,), 'new-development direction')
            direct = {key: np.zeros((len(ids), 3)) for key in POSITION_KEYS}
        diagnostics = {
            'policy': POLICY, 'rows': len(ids), 'columns': N,
            'row_ids_sha256': array_hash(ids), 'state_array_sha256': array_hash(q),
            'full_radial_sha256': array_hash(r), 'full_theta_sha256': array_hash(th),
            'factorization_definition_sha256': self.definition_sha256,
            'batch_count': 0, 'family_kernel_count': 0,
            'maximum_query_radial_rows': 0, 'maximum_angular_modes': 0,
            'maximum_selected_virtual_parameter_axis': 0,
            'maximum_family_kernel_array_bytes': 0,
            'maximum_selected_virtual_jet_bytes': 0,
            'full_angle_163_or159_parameter_tensors_formed': 0,
            'ordinary_geometry_calls_inside_factorization': 0,
            'timing_scope': 'nonoverlapping per-batch scalar, replay, kernels, contraction; total includes bindings',
            'scalar_fields_seconds': 0., 'ordinary_replay_seconds': 0.,
            'angular_kernels_seconds': 0., 'selected_contraction_seconds': 0.,
            'null_height_seconds': 0.,
            'ordinary_replay_maxima': {key: 0. for key in POSITION_KEYS},
            'development_directional_output_requested': direct is not None}
        started = time.monotonic()
        reference163 = self.field.coordinates.reference_evaluation_state(q)
        for begin in range(0, len(radial_ids), int(owned_width)):
            if wall is not None:
                wall()
            owned = radial_ids[begin:begin+int(owned_width)]
            selected = np.flatnonzero(np.isin(points//nt, owned))
            query = np.unique(np.r_[0, owned, len(r)-1])
            ri = np.searchsorted(query, points[selected]//nt)
            ti = points[selected] % nt
            second = bool(np.any(groups[selected] >= 7) or direct is not None)
            tick = time.monotonic()
            grid = self.single.source.grid_for(r[query], th)
            fields = grid.fields(reference163)
            fields['_theta'] = th[None, :]
            frame = target_frame(fields)
            diagnostics['scalar_fields_seconds'] += time.monotonic()-tick
            tick = time.monotonic()
            ordinary, metric, errors = self._ordinary_slice_and_replay(
                q, r, th, query, bound, grid, fields, frame)
            diagnostics['ordinary_replay_seconds'] += time.monotonic()-tick
            for key, error in errors.items():
                diagnostics['ordinary_replay_maxima'][key] = max(
                    diagnostics['ordinary_replay_maxima'].get(key, 0.), error)
            small = {key: ordinary[key][ri, ti] for key in POSITION_KEYS}
            radius = np.asarray(metric['a'])[ri]
            for name, angular, angular_first, radial_jets, start, stop in self._families(grid, len(query), nt):
                tick = time.monotonic()
                kernels = angular_kernels(fields, frame, name, angular, angular_first, second=second)
                diagnostics['angular_kernels_seconds'] += time.monotonic()-tick
                diagnostics['family_kernel_count'] += 1
                diagnostics['maximum_angular_modes'] = max(diagnostics['maximum_angular_modes'], angular.shape[1])
                diagnostics['maximum_family_kernel_array_bytes'] = max(
                    diagnostics['maximum_family_kernel_array_bytes'], sum(v.nbytes for v in kernels.values()))
                tick = time.monotonic()
                virtual = virtual_selected_jets(kernels, ri, ti, metric, second=second)
                data = dict(small)
                data.update({'jac_'+key: value for key, value in virtual.items()})
                local = selected_spectral_parameter_jacobian(
                    data, radius, groups[selected], side, self.cfg)
                result[selected, start:stop] = expand_radial_rows(local, radial_jets, ri)
                diagnostics['maximum_selected_virtual_parameter_axis'] = max(
                    diagnostics['maximum_selected_virtual_parameter_axis'], local.shape[1])
                diagnostics['maximum_selected_virtual_jet_bytes'] = max(
                    diagnostics['maximum_selected_virtual_jet_bytes'], sum(v.nbytes for v in virtual.values()))
                if direct is not None:
                    nmode = angular.shape[1]
                    coefficients = direction[start:stop].reshape(-1, nmode)
                    weights = np.stack([v[ri] @ coefficients for v in radial_jets], axis=1)
                    for key in POSITION_KEYS:
                        values = virtual[key].reshape(len(selected), 3, 3, nmode)
                        direct[key][selected] += np.einsum('nckm,nkm->nc', values, weights)
                diagnostics['selected_contraction_seconds'] += time.monotonic()-tick
                del kernels, virtual, data, local
            tick = time.monotonic()
            height = selected_null_height_jets(self.field, r[query], ri, second=second)
            data = dict(small)
            data.update({'jac_'+key: value for key, value in height.items()})
            result[selected, 154:] = selected_spectral_parameter_jacobian(
                data, radius, groups[selected], side, self.cfg)
            if direct is not None:
                for key in POSITION_KEYS:
                    direct[key][selected] += np.einsum('nck,k->nc', height[key], direction[154:])
            diagnostics['null_height_seconds'] += time.monotonic()-tick
            diagnostics['maximum_selected_virtual_jet_bytes'] = max(
                diagnostics['maximum_selected_virtual_jet_bytes'], sum(v.nbytes for v in height.values()))
            diagnostics['batch_count'] += 1
            diagnostics['maximum_query_radial_rows'] = max(diagnostics['maximum_query_radial_rows'], len(query))
            covered[selected] = True
            del fields, frame, ordinary, small, grid, height, data
        if not np.all(covered) or not np.all(np.isfinite(result)):
            raise ArithmeticError('selected factorized rows not completely covered')
        if direct is not None and any(not np.all(np.isfinite(v)) for v in direct.values()):
            raise FloatingPointError('nonfinite new-development directional output')
        diagnostics['total_seconds'] = time.monotonic()-started
        diagnostics['returned_selected_matrix_bytes'] = result.nbytes
        diagnostics['row_order_preserved_including_repetitions'] = True
        if wall is not None:
            wall()
        return result, diagnostics, direct

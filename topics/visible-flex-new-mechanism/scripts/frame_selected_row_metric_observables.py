#!/usr/bin/env python3
"""True selected de/df alongside the already-paid factorized scalar Jacobian.

The same complete-angle virtual kernels are used once per family and batch.
No full163/159 parameter geometry tensor is formed. New outputs are the two
observable scalar derivative rows needed by the affine spectral norm model.
"""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_height_null_coordinates import digest
import frame_selected_row_radial_jacobian as frozen
from frame_selected_row_radial_jacobian import (
    SelectedRadialJacobian, N, POSITION_KEYS, array_hash, _same_bytes, _finite,
    angular_kernels, virtual_selected_jets, expand_radial_rows,
    selected_null_height_jets, target_frame, selected_spectral_parameter_jacobian)
from frame_metric_affine_spectral_model import observable_parameter_jacobians

POLICY = 'same159-selected-radial-J-with-true-metric-observables-v1'


def implementation_hashes():
    result = frozen.implementation_hashes()
    from frame_metric_affine_spectral_model import implementation_hashes as model_hashes
    result.update(model_hashes())
    p = Path(__file__)
    result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


class SelectedMetricObservables(SelectedRadialJacobian):
    def __init__(self, field, cfg):
        super().__init__(field, cfg)
        self.definition = copy.deepcopy(self.definition)
        self.definition.update(
            metric_observables_policy=POLICY,
            additional_scalar_outputs=['e', 'f', 'de159', 'df159'],
            derivative_formulas=['2*Xs dot dXs', 'T dot dXs + Xs dot dT'],
            observable_rows_only_at_existing_selected_metric_IDs=True,
            both_branches_keep_the_original_row_order=True,
            no_recovery_by_dividing_spectral_J_by_f=True,
            common_virtual_kernel_pass_for_original_J_and_observables=True)
        self.definition_sha256 = digest(self.definition)

    def evaluate(self, state, radial, theta, row_ids, bound, *, side, owned_width,
                 wall=None):
        self._assert_context()
        q = self.field.coordinates.validate(state)
        r, th = frozen.rows_api._grid(radial, theta)
        if len(th) % 4 or side not in (-1, 1):
            raise ValueError('same complete angle grid and signed physical side required')
        if (isinstance(owned_width, bool)
                or not isinstance(owned_width, (int, np.integer))
                or not 1 <= owned_width <= 16):
            raise ValueError('one through sixteen owned radial rows per batch required')
        if (bound.get('schema') != frozen.POLICY+'-bound-ordinary'
                or bound.get('factorization_definition_sha256') != self.definition_sha256
                or bound.get('ordinary_evaluation_definition_sha256') != self.ordinary_evaluation_sha256
                or bound.get('coordinate_definition_sha256') != self.coordinate_sha256
                or not _same_bytes(bound['state'], q)
                or not _same_bytes(bound['radial'], r)
                or not _same_bytes(bound['theta'], th)):
            raise ValueError('observable binding differs from exact current state/grid/reference')
        raw = list(row_ids)
        if any(isinstance(v, (bool, np.bool_)) or not isinstance(v, (int, np.integer)) for v in raw):
            raise ValueError('original integer row IDs required')
        ids = np.asarray(raw, np.int64)
        count, nt = len(r)*len(th), len(th)
        if not len(ids) or np.any(ids < 0) or np.any(ids >= 11*count):
            raise ValueError('nonempty original eleven-group row IDs required')
        groups, points = ids//count, ids % count
        metric_positions = np.flatnonzero(groups < 2)
        metric_slots = np.full(len(ids), -1, np.int64)
        metric_slots[metric_positions] = np.arange(len(metric_positions))
        metric_e = np.empty(len(metric_positions))
        metric_f = np.empty(len(metric_positions))
        metric_de = np.empty((len(metric_positions), N))
        metric_df = np.empty((len(metric_positions), N))
        radial_ids = np.unique(points//nt)
        result = np.empty((len(ids), N))
        covered = np.zeros(len(ids), bool)
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
            'timing_scope': 'nonoverlapping scalar,replay,kernel,J contraction,observable,height; total includes identities',
            'scalar_fields_seconds': 0., 'ordinary_replay_seconds': 0.,
            'angular_kernels_seconds': 0., 'selected_contraction_seconds': 0.,
            'metric_observable_seconds': 0., 'null_height_seconds': 0.,
            'ordinary_replay_maxima': {key: 0. for key in POSITION_KEYS},
            'development_directional_output_requested': False,
            'existing_metric_row_count': len(metric_positions),
            'extra_field_J_or_ordinary_value_calls': 0}
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
            local_metric = groups[selected] < 2
            metric_output = metric_slots[selected[local_metric]]
            second = bool(np.any(groups[selected] >= 7))
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
            if np.any(local_metric):
                U = small['Xs'][local_metric]
                T = small['T'][local_metric]
                metric_e[metric_output] = np.sum(U*U, axis=1)-1.
                metric_f[metric_output] = np.sum(U*T, axis=1)
            for name, angular, angular_first, radial_jets, start, stop in self._families(
                    grid, len(query), nt):
                tick = time.monotonic()
                kernels = angular_kernels(
                    fields, frame, name, angular, angular_first, second=second)
                diagnostics['angular_kernels_seconds'] += time.monotonic()-tick
                diagnostics['family_kernel_count'] += 1
                diagnostics['maximum_angular_modes'] = max(
                    diagnostics['maximum_angular_modes'], angular.shape[1])
                diagnostics['maximum_family_kernel_array_bytes'] = max(
                    diagnostics['maximum_family_kernel_array_bytes'],
                    sum(v.nbytes for v in kernels.values()))
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
                    diagnostics['maximum_selected_virtual_jet_bytes'],
                    sum(v.nbytes for v in virtual.values()))
                diagnostics['selected_contraction_seconds'] += time.monotonic()-tick
                tick = time.monotonic()
                if np.any(local_metric):
                    obs = {key: small[key][local_metric] for key in ('Xs', 'T')}
                    obs.update({'jac_'+key: virtual[key][local_metric] for key in ('Xs', 'T')})
                    de, df = observable_parameter_jacobians(obs)
                    metric_de[metric_output, start:stop] = expand_radial_rows(
                        de, radial_jets, ri[local_metric])
                    metric_df[metric_output, start:stop] = expand_radial_rows(
                        df, radial_jets, ri[local_metric])
                diagnostics['metric_observable_seconds'] += time.monotonic()-tick
                del kernels, virtual, data, local
            tick = time.monotonic()
            height = selected_null_height_jets(self.field, r[query], ri, second=second)
            data = dict(small)
            data.update({'jac_'+key: value for key, value in height.items()})
            result[selected, 154:] = selected_spectral_parameter_jacobian(
                data, radius, groups[selected], side, self.cfg)
            diagnostics['null_height_seconds'] += time.monotonic()-tick
            tick = time.monotonic()
            if np.any(local_metric):
                obs = {key: small[key][local_metric] for key in ('Xs', 'T')}
                obs.update({'jac_'+key: height[key][local_metric] for key in ('Xs', 'T')})
                metric_de[metric_output, 154:], metric_df[metric_output, 154:] = (
                    observable_parameter_jacobians(obs))
            diagnostics['metric_observable_seconds'] += time.monotonic()-tick
            diagnostics['maximum_selected_virtual_jet_bytes'] = max(
                diagnostics['maximum_selected_virtual_jet_bytes'],
                sum(v.nbytes for v in height.values()))
            diagnostics['batch_count'] += 1
            diagnostics['maximum_query_radial_rows'] = max(
                diagnostics['maximum_query_radial_rows'], len(query))
            covered[selected] = True
            del fields, frame, ordinary, small, grid, height, data
        arrays = [result, metric_e, metric_f, metric_de, metric_df]
        if not np.all(covered) or any(not np.all(np.isfinite(a)) for a in arrays):
            raise ArithmeticError('selected scalar/observable rows not completely covered')
        observables = {
            'schema': POLICY+'-selected-observables',
            'row_positions': metric_positions, 'row_ids': ids[metric_positions].copy(),
            'groups': groups[metric_positions].copy(),
            'e': metric_e, 'f': metric_f, 'de': metric_de, 'df': metric_df,
            'state_array_sha256': array_hash(q),
            'complete_row_ids_sha256': array_hash(ids),
            'full_radial_sha256': array_hash(r), 'full_theta_sha256': array_hash(th),
            'coordinate_definition_sha256': self.coordinate_sha256,
            'factorization_definition_sha256': self.definition_sha256}
        observables['array_sha256'] = {
            key: array_hash(observables[key]) for key in
            ('row_positions', 'row_ids', 'groups', 'e', 'f', 'de', 'df')}
        observables['binding_sha256'] = digest({
            key: value for key, value in observables.items()
            if key not in ('row_positions', 'row_ids', 'groups', 'e', 'f', 'de', 'df')})
        for key in ('row_positions', 'row_ids', 'groups', 'e', 'f', 'de', 'df'):
            observables[key].setflags(write=False)
        diagnostics['total_seconds'] = time.monotonic()-started
        diagnostics['returned_selected_matrix_bytes'] = result.nbytes
        diagnostics['returned_metric_observable_bytes'] = sum(
            observables[key].nbytes for key in ('row_positions', 'row_ids', 'groups', 'e', 'f', 'de', 'df'))
        diagnostics['metric_observable_binding_sha256'] = observables['binding_sha256']
        diagnostics['row_order_preserved_including_repetitions'] = True
        if wall is not None:
            wall()
        return result, diagnostics, observables


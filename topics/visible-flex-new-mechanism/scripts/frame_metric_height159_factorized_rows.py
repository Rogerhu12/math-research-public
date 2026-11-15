#!/usr/bin/env python3
"""Only the selected Jacobian path changes in the existing159 SOC-hold objective.

Ordinary geometry, current exact-null heights, all original row IDs and
two-grid decisions, pool learning, LPs, model radii and controller rules retain
their frozen implementations.  New floating evaluation identity is explicit.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_metric_height159_soc_hold import (
    SOCHold159Objective, retention_definition,
    implementation_hashes as inherited_hashes)
from frame_selected_row_radial_jacobian import (
    POLICY, N, SelectedRadialJacobian, array_hash, _same_bytes,
    implementation_hashes as factorization_hashes)

CACHE_SCHEMA = POLICY + '-selected-cache'


def implementation_hashes():
    result = inherited_hashes()
    result.update(factorization_hashes())
    p = Path(__file__)
    result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def configuration(base):
    """Add only evaluation metadata; all numerical controller/gate values stay."""
    retention_definition(base)
    if 'selected_row_radial_factorization_policy' in base:
        raise ValueError('the new selected-J representation must be installed exactly once')
    result = copy.deepcopy(base)
    result.update(
        selected_row_radial_factorization_policy=POLICY,
        inherited_original163_J_reporting_flag=base.get(
            'original_geometry_163_J_still_computed_before_new159_columns_are_returned'),
        original_geometry_163_J_still_computed_before_new159_columns_are_returned=False,
        selected_J_change_is_floating_evaluation_not_new_physical_parameters=True,
        actual_full_value_and_gate_paths_are_unmodified=True)
    return result


class FactorizedHeight159Objective(SOCHold159Objective):
    """Keep the frozen accepted-cache protocol and replace only coarse/fine J.

    derivative_cache and fine_derivative_cache still have state/pool_version.
    The unchanged SOC parent therefore restores these exact same selected
    matrices on accepted-state rollback.  No cache survives a different row
    order, full grid, exact state bytes or new evaluation identity.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.cfg.get('selected_row_radial_factorization_policy') != POLICY:
            raise ValueError('explicit selected-row evaluation configuration required')
        self.factorized = SelectedRadialJacobian(self.problem, self.cfg)
        self.factorized_statistics = {
            name: {
                'refreshes': 0, 'cache_hits': 0, 'batches': 0,
                'total_seconds': 0., 'scalar_fields_seconds': 0.,
                'ordinary_replay_seconds': 0., 'angular_kernels_seconds': 0.,
                'selected_contraction_seconds': 0., 'null_height_seconds': 0.,
                'maximum_family_kernel_array_bytes': 0,
                'maximum_selected_virtual_jet_bytes': 0,
                'maximum_selected_matrix_bytes': 0,
                'maximum_query_radial_rows': 0,
                'maximum_selected_virtual_parameter_axis': 0,
                'maximum_original_row_count': 0,
                'ordinary_replay_maxima': {}, 'last_refresh': None}
            for name in ('coarse', 'fine')}
        previous = self.evaluation_sha256
        self.evaluation_definition.update(
            selected_row_radial_factorization=copy.deepcopy(self.factorized.definition),
            inherited_objective_evaluation_sha256=previous,
            selected_row_parameter_Jacobian_source_sha256=implementation_hashes(),
            ordinary_geometry_and_all_decisions_use_unchanged_parent=True,
            legacy_163_geometry_Jacobian_is_not_called_by_new_selected_paths=True,
            selected_cache_protocol='same accepted-state state/pool_version, plus exact rows/grids/identity',
            new_floating_reassociation_not_bitwise_historical_trajectory=True)
        self.evaluation_sha256 = digest(self.evaluation_definition)

    def _cache_matches(self, cache, state, ids, pool_version, theta):
        return bool(cache is not None
            and cache.get('schema') == CACHE_SCHEMA
            and cache.get('pool_version') == pool_version
            and cache.get('evaluation_sha256') == self.evaluation_sha256
            and cache.get('factorization_definition_sha256') == self.factorized.definition_sha256
            and _same_bytes(cache['state'], np.asarray(state, float))
            and _same_bytes(cache['row_ids'], np.asarray(ids, np.int64))
            and cache.get('radial_sha256') == array_hash(self.radial)
            and cache.get('theta_sha256') == array_hash(theta))

    def _record_refresh(self, label, report):
        target = self.factorized_statistics[label]
        target['refreshes'] += 1
        target['batches'] += report['batch_count']
        for name in ('total_seconds', 'scalar_fields_seconds', 'ordinary_replay_seconds',
                     'angular_kernels_seconds', 'selected_contraction_seconds', 'null_height_seconds'):
            target[name] += report[name]
        for name in ('maximum_family_kernel_array_bytes', 'maximum_selected_virtual_jet_bytes',
                     'maximum_query_radial_rows', 'maximum_selected_virtual_parameter_axis'):
            target[name] = max(target[name], report[name])
        target['maximum_selected_matrix_bytes'] = max(
            target['maximum_selected_matrix_bytes'], report['returned_selected_matrix_bytes'])
        target['maximum_original_row_count'] = max(target['maximum_original_row_count'], report['rows'])
        for name, value in report['ordinary_replay_maxima'].items():
            target['ordinary_replay_maxima'][name] = max(target['ordinary_replay_maxima'].get(name, 0.), value)
        # Every LP/model already binds the actual selected matrix.  Do not
        # retain all diagnostic arrays or create another trajectory artifact.
        target['last_refresh'] = copy.deepcopy(report)

    def _evaluate_selected(self, label, state, ids, theta, data, pool_version):
        width_key = ('radial_Jacobian_batch_owned_rows' if label == 'coarse'
                     else 'fine_Jacobian_owned_radial_rows')
        width = int(self.cfg[width_key])
        bound = self.factorized.bind_ordinary(
            state, self.radial, theta, data,
            owner='coarse-current-cache' if label == 'coarse' else 'fine-current-cache')
        J, report, unused = self.factorized.evaluate(
            state, self.radial, theta, ids, bound, side=self.gate.side,
            owned_width=width, wall=self._wall)
        if unused is not None or J.shape != (len(ids), self.n) or self.n != N:
            raise ArithmeticError('exact selected159 derivative layout required')
        J.setflags(write=False)
        cache = {
            'schema': CACHE_SCHEMA, 'state': np.asarray(state, float).copy(),
            'pool_version': pool_version, 'row_ids': np.asarray(ids, np.int64).copy(),
            'radial_sha256': array_hash(self.radial), 'theta_sha256': array_hash(theta),
            'evaluation_sha256': self.evaluation_sha256,
            'factorization_definition_sha256': self.factorized.definition_sha256,
            'J': J}
        cache['state'].setflags(write=False)
        cache['row_ids'].setflags(write=False)
        self._record_refresh(label, report)
        return cache, report

    def active_derivatives(self, vector):
        raise NotImplementedError(
            'this objective owns selected scalar rows, not the legacy per-point primitive-J cache; '
            'use its unchanged linear_rows/constraint_jac interface')

    def constraint_jac(self, vector):
        """Same (rows,n+1) API, including the unchanged fixed-zeta derivative."""
        started = time.monotonic()
        self.evaluate(vector)
        vector = np.asarray(vector, float)
        state = vector[:-1]
        if not len(self.pool):
            raise ValueError('initialize the original coarse row pool first')
        cache = self.derivative_cache
        if not self._cache_matches(cache, state, self.pool, self.pool_version, self.theta):
            cache, report = self._evaluate_selected(
                'coarse', state, self.pool, self.theta, self.geometry_cache, self.pool_version)
            self.derivative_cache = cache
            # These retained counters now mean selected-row refreshes, not old
            # full geometry-J requests.  The new snapshot states that distinction.
            self.jacobian_refreshes += 1
            self.maximum_retained_derivative_bytes = max(
                self.maximum_retained_derivative_bytes,
                cache['J'].nbytes + cache['state'].nbytes + cache['row_ids'].nbytes)
            self.maximum_value_Jacobian_replay_difference = max(
                self.maximum_value_Jacobian_replay_difference,
                max(report['ordinary_replay_maxima'].values(), default=0.))
        else:
            self.factorized_statistics['coarse']['cache_hits'] += 1
        result = np.zeros((len(self.pool), self.n+1))
        result[:, :self.n] = cache['J']
        # Preserve the old auxiliary-column contract.  The physical recovery
        # and its unchanged linear_rows use only [:self.n]; zeta is never optimized.
        data = self.geometry_cache
        count = data['e'].size
        groups, points = self.pool//count, self.pool % count
        forms = data['curvature']
        q, E, F, G, e, f, k = (
            np.asarray(forms[name]).ravel()[points]
            for name in ('q', 'E', 'F', 'G', 'e', 'f', 'k'))
        zeta = float(vector[-1])
        scale = float(Q(self.cfg['curvature_scale_exact']))
        for group in (7, 8, 9, 10):
            mask = groups == group
            if not np.any(mask):
                continue
            sign = 1 if group < 9 else -1
            if group in (7, 9):
                result[mask, -1] = q[mask]*(E[mask]+G[mask])
            else:
                h0 = zeta*q[mask]*E[mask] + sign*e[mask]/scale
                h1 = zeta*q[mask]*F[mask] + sign*f[mask]/scale
                h2 = zeta*q[mask]*G[mask] + sign*k[mask]/scale
                result[mask, -1] = q[mask]*(
                    G[mask]*h0 + E[mask]*h2 - 2*F[mask]*h1)
        if not np.all(np.isfinite(result)):
            raise FloatingPointError('nonfinite factorized selected coarse derivative')
        self.maximum_constraint_Jacobian_bytes = max(
            self.maximum_constraint_Jacobian_bytes, result.nbytes)
        self.pool_jacobian_seconds += time.monotonic()-started
        self._wall()
        return result

    def fine_derivatives(self, state):
        self.fine_decision(state)
        if not len(self.fine_pool):
            raise ValueError('initialize the original complete fine pool first')
        cache = self.fine_derivative_cache
        if self._cache_matches(cache, state, self.fine_pool, self.fine_pool_version, self.fine_theta):
            self.factorized_statistics['fine']['cache_hits'] += 1
            return cache['J']
        if not _same_bytes(np.asarray(self.fine_cache['state'], float), np.asarray(state, float)):
            raise ValueError('the full fine ordinary cache must own this exact state')
        started = time.monotonic()
        cache, report = self._evaluate_selected(
            'fine', state, self.fine_pool, self.fine_theta,
            self.fine_cache['data'], self.fine_pool_version)
        self.fine_derivative_cache = cache
        self.fine_Jacobian_refreshes += 1
        self.fine_Jacobian_batches += report['batch_count']
        self.fine_Jacobian_maximum_query_radial_rows = max(
            self.fine_Jacobian_maximum_query_radial_rows, report['maximum_query_radial_rows'])
        self.fine_Jacobian_maximum_retained_bytes = max(
            self.fine_Jacobian_maximum_retained_bytes, cache['J'].nbytes)
        # This is the new small virtual tensor, explicitly labelled in snapshot.
        self.fine_Jacobian_maximum_returned_bytes = max(
            self.fine_Jacobian_maximum_returned_bytes, report['maximum_selected_virtual_jet_bytes'])
        for name, value in report['ordinary_replay_maxima'].items():
            key = 'height' if name.startswith('height/') else name
            if key in self.fine_batch_replay_maxima:
                self.fine_batch_replay_maxima[key] = max(self.fine_batch_replay_maxima[key], value)
        self.fine_Jacobian_seconds += time.monotonic()-started
        self._wall()
        return cache['J']

    def snapshot(self):
        result = super().snapshot()
        if not hasattr(self, 'factorized_statistics'):
            return result
        result.update(
            selected_row_radial_factorization_policy=POLICY,
            selected_row_radial_factorization_definition=copy.deepcopy(self.factorized.definition),
            selected_row_factorization_statistics=copy.deepcopy(self.factorized_statistics),
            original_full163_parameter_geometry_Jacobian_requests_in_new_paths=0,
            original_full159_parameter_geometry_Jacobian_requests_in_new_paths=0,
            ordinary_full_value_path_and_all_controller_gates_inherited=True,
            fine_selected_returned_bytes_now_measure_small_virtual_geometry_arrays=True,
            coarse_jacobian_geometry_batches_counter_retains_old_full_geometry_scope=True,
            coarse_jacobian_refreshes_counter_means_selected_matrix_refreshes=True,
            exact_same_state_pool_and_row_order_cache_protocol_preserved=True,
            floating_reassociation_can_change_LP_and_acceptance_trajectory=True)
        return result

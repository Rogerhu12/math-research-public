#!/usr/bin/env python3
"""Complete original-grid affine-e/f norms by a single parameter-direction JVP.

This is a new model oracle, not an ordinary physical geometry evaluator.
All scientific and new artificial execution belongs to public Actions.
No frozen source is patched and no full-grid159 parameter tensor is formed.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import periodic_operator, target_frame
from frame_height_null_coordinates import digest
from frame_selected_row_radial_jacobian import (
    N, array_hash, _same_bytes, POLICY as FACTORIZATION_POLICY)
from frame_selected_row_metric_observables import (
    SelectedMetricObservables, implementation_hashes as observable_hashes)
from frame_metric_affine_spectral_model import (
    AffineSpectralModel, phi, phi_gradient,
    implementation_hashes as affine_hashes)

POLICY = 'same159-complete-two-grid-affine-ef-directional-separation-v1'
GRID_BRANCHES = (('coarse', 0), ('coarse', 1), ('fine', 0), ('fine', 1))


def implementation_hashes():
    result = observable_hashes()
    result.update(affine_hashes())
    p = Path(__file__)
    result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def definition():
    return {
        'schema': POLICY+'-definition',
        'independent_coordinates': N,
        'grid_maximum_functions': [
            {'grid': label, 'original_group': group} for label, group in GRID_BRANCHES],
        'complete_original_uniform_theta_before_Pi': True,
        'directional_formulas': [
            'deltaT=sum_q Tpart[q]*deltaq',
            'deltaTs=sum_q Ts_value_part[q]*deltaq+Tpart[q]*deltaq_s',
            'deltaXs=a_s*Pi(deltaT)+a*Pi(deltaTs)+ez*Dnull*pheight',
            'de=2*current_Xs dot deltaXs',
            'df=current_T dot deltaXs+current_Xs dot deltaT'],
        'fixed_complete_metric_and_exact_height_reference': True,
        'original_selected_phi_functions_are_retained': True,
        'four_global_max_functions_are_additional_convex_functions': True,
        'attainer_cut_uses_true_original_row_de_df': True,
        'deterministic_equal_value_tie_is_smallest_original_flat_ID': True,
        'whole_grid_JVP_has_one_direction_not159_parameter_axes': True,
        'ordinary_geometry_calls_inside_oracle': 0,
        'predicted_rows_do_not_mutate_actual_pools_or_reserve_capacity': True,
        'no_continuous_surface_or_interval_optimality_claim': True}


def _finite(value, shape=None, name='array'):
    a = np.asarray(value, float)
    if (shape is not None and a.shape != shape) or not np.all(np.isfinite(a)):
        raise ValueError('finite same-shape '+name+' required')
    return a


def _readonly(value):
    a = np.asarray(value).copy()
    a.setflags(write=False)
    return a


def _key(label, flat_id, point_count):
    return str(label), int(flat_id) % int(point_count)


def direction_frame_jets(factorized, grid, fields, frame, direction):
    """New analytic directional contraction; no old basis_jacobian is called.

    Current fields and frame are the exact frozen-grid functions already used
    by complete_tangent_parameter_jets. The two coefficients are its B/B_s
    contract, with all original radial and angular factors retained.
    """
    p = _finite(direction, (N,), 'independent159 direction')
    nr, nt = fields['u']['value'].shape
    delta = {name: [np.zeros((nr, nt)), np.zeros((nr, nt))]
             for name in ('u', 'v')}
    for name, angular, _, radial, start, stop in factorized._families(grid, nr, nt):
        nrad, nmodes = radial[0].shape[1], angular.shape[1]
        if stop-start != nrad*nmodes:
            raise ValueError('original radial-major/mode-minor layout changed')
        coeff = p[start:stop].reshape(nrad, nmodes)
        for order in (0, 1):
            delta[name][order] += (np.asarray(radial[order])@coeff)@angular.T
    dT = np.zeros((nr, nt, 3))
    dTs = np.zeros_like(dT)
    for name in ('u', 'v'):
        dq, dqs = delta[name]
        part = _finite(frame['Tpart'][name], dT.shape, 'original Tpart/'+name)
        first = _finite(frame['Ts_value_part'][name], dT.shape,
                        'original Ts_value_part/'+name)
        dT += part*dq[..., None]
        dTs += first*dq[..., None] + part*dqs[..., None]
    return _finite(dT), _finite(dTs)


class CompleteDirectionalMetricOracle:
    """Frozen accepted-center data and four complete-grid branch maxima.

    The object holds its own readonly first-jet ordinary values. Bound full
    ordinary references are retained only for same-center scalar replay and
    the few new selected derivative rows; later candidate caches are never
    read in place of this accepted center.
    """
    def __init__(self, factorized, state, bounds, grids, cfg, *, wall):
        if not isinstance(factorized, SelectedMetricObservables):
            raise ValueError('the frozen true selected e/f evaluator is required')
        if not callable(wall) or set(bounds) != {'coarse', 'fine'} or set(grids) != set(bounds):
            raise ValueError('both bound original grids and original wall callback required')
        self.factorized, self.field, self.cfg, self.wall = (
            factorized, factorized.field, cfg, wall)
        factorized._assert_context()
        self.state = _readonly(self.field.coordinates.validate(state))
        self.reference163 = _readonly(
            self.field.coordinates.reference_evaluation_state(self.state))
        self.bounds, self.grids = dict(bounds), dict(grids)
        self.epsilon = float(Q(cfg['metric_proposal_epsilon_exact']))
        self.target = float(Q(cfg['fixed_metric_budget_exact']))
        if self.epsilon <= 0 or self.target <= 0:
            raise ValueError('positive frozen epsilon and target required')
        self.config_sha256 = digest(cfg)
        self.center = {}
        self.grid_binding = {}
        self.events = []
        self.phase = 'primary-inner'
        self.cache = {}
        self.extra_rows = {}
        self.extra_row_events = []
        self.statistics = {
            'new_full_direction_evaluations': 0, 'full_grid_scans': 0,
            'cached_direction_reuses': 0, 'total_directional_seconds': 0.,
            'total_scalar_replay_seconds': 0., 'total_parameter_contraction_seconds': 0.,
            'total_complete_Pi_seconds': 0., 'total_branch_reduction_seconds': 0.,
            'original_owned_radial_batches': 0, 'complete_Pi_calls': 0,
            'new_selected_metric_row_calls': 0, 'new_selected_metric_rows': 0,
            'new_selected_metric_J_seconds': 0., 'new_selected_metric_J_bytes': 0,
            'ordinary_geometry_calls_inside_oracle': 0,
            'full_angle_159_or163_parameter_tensors_formed': 0,
            'largest_direction_array_bytes': 0,
            'maximum_current_scalar_replay_error': 0.,
            'maximum_attainer_direction_vs_selected_J_error': 0.,
            'zero_direction_returns_from_frozen_values': 0}
        for label in ('coarse', 'fine'):
            b, g = self.bounds[label], self.grids[label]
            if (b.get('schema') != FACTORIZATION_POLICY+'-bound-ordinary'
                    or b.get('factorization_definition_sha256') != factorized.definition_sha256
                    or b.get('ordinary_evaluation_definition_sha256') != factorized.ordinary_evaluation_sha256
                    or b.get('coordinate_definition_sha256') != factorized.coordinate_sha256
                    or not _same_bytes(b['state'], self.state)
                    or g.label != label):
                raise ValueError('exact center/field/grid/reference binding differs')
            r, th = np.asarray(b['radial']), np.asarray(b['theta'])
            if (r.shape != (g.nr,) or len(th) != g.nt
                    or not np.array_equal(r, np.array([float(x) for x in g.nodes]))):
                raise ValueError('original rational grid and ordinary grid differ')
            data = b['data']
            U = _readonly(_finite(data['Xs'], (g.nr, g.nt, 3), label+'/current Xs'))
            T = _readonly(_finite(data['T'], U.shape, label+'/current T'))
            e, f = np.sum(U*U, axis=2)-1., np.sum(U*T, axis=2)
            item = {
                'U': U, 'T': T, 'e': _readonly(e), 'f': _readonly(f),
                'radial': _readonly(r), 'theta': _readonly(th),
                'a': _readonly(_finite(data['metric']['a'], (g.nr,), label+'/a')),
                'a_s': _readonly(_finite(data['metric']['a_s'], (g.nr,), label+'/a_s'))}
            self.center[label] = item
            self.grid_binding[label] = {
                'rational_grid_definition': copy.deepcopy(g.definition),
                'rational_grid_definition_sha256': g.definition_sha256,
                'radial_sha256': array_hash(r), 'theta_sha256': array_hash(th),
                'current_Xs_sha256': array_hash(U), 'current_T_sha256': array_hash(T),
                'e_sha256': array_hash(e), 'f_sha256': array_hash(f),
                'original_point_count': g.point_count,
                'original_soft_row_count': 2*g.point_count}
        self.binding = {
            'schema': POLICY+'-center',
            'state_array_sha256': array_hash(self.state),
            'reference163_array_sha256': array_hash(self.reference163),
            'coordinate_definition_sha256': factorized.coordinate_sha256,
            'height_reference_definition_sha256': factorized.height_reference_sha256,
            'factorization_definition_sha256': factorized.definition_sha256,
            'ordinary_evaluation_definition_sha256': factorized.ordinary_evaluation_sha256,
            'configuration_sha256': self.config_sha256,
            'grids': copy.deepcopy(self.grid_binding),
            'definition': definition()}
        self.binding_sha256 = digest(self.binding)
        zero = np.zeros(N)
        baseline = self._zero_direction(zero)
        self.base_maxima = _readonly(baseline['phi'])
        self.base_slack = max(0., float(np.max(self.base_maxima))-self.target)
        self.cache[array_hash(zero)] = (zero.copy(), baseline)

    def _assert_context(self):
        self.factorized._assert_context()
        if digest(self.cfg) != self.config_sha256:
            raise ValueError('complete oracle configuration changed after accepted-center binding')
        for label in ('coarse', 'fine'):
            if (self.grids[label].definition_sha256 !=
                    self.grid_binding[label]['rational_grid_definition_sha256']
                    or not _same_bytes(self.bounds[label]['state'], self.state)):
                raise ValueError('complete oracle original grid/center changed')

    def _record(self, label, group, point, values):
        grid = self.grids[label]
        ri, ti = divmod(int(point), grid.nt)
        result = dict(values)
        result.update(
            original_row=grid.coordinate(group*grid.point_count+int(point)),
            original_point_flat_index=int(point), radial_index=ri, theta_index=ti)
        return result

    def _zero_direction(self, p):
        rows, maxima = [], []
        for label, group in GRID_BRANCHES:
            d = self.center[label]
            e, f = d['e'].reshape(-1), d['f'].reshape(-1)
            vals = phi(e, f, np.full(len(e), group, np.int64), self.epsilon)
            point = int(np.argmax(vals))
            maxima.append(float(vals[point]))
            rows.append(self._record(label, group, point, {
                'phi': float(vals[point]), 'base_e': float(e[point]),
                'base_f': float(f[point]), 'de_step': 0., 'df_step': 0.,
                'affine_e': float(e[point]), 'affine_f': float(f[point])}))
        return {
            'schema': POLICY+'-four-maxima', 'direction_sha256': array_hash(p),
            'center_binding_sha256': self.binding_sha256,
            'phi': _readonly(np.array(maxima)), 'attainers': rows,
            'from_frozen_zero_direction_values': True,
            'full_grid_coverage': {
                label: self.grids[label].point_count for label in ('coarse', 'fine')}}

    def evaluate(self, direction):
        self._assert_context()
        p = _finite(direction, (N,), 'complete original-grid direction')
        key = array_hash(p)
        if key in self.cache:
            stored, result = self.cache[key]
            if not _same_bytes(stored, p):
                raise ArithmeticError('direction digest collision or shape/byte mismatch')
            self.statistics['cached_direction_reuses'] += 1
            if not np.any(p):
                self.statistics['zero_direction_returns_from_frozen_values'] += 1
            return result
        self.wall()
        event = {
            'ordinal': len(self.events)+1, 'direction_sha256': key,
            'center_binding_sha256': self.binding_sha256,
            'status': 'complete-two-grid-direction-started', 'grid_scans': [],
            'phase': self.phase}
        self.events.append(event)
        self.statistics['new_full_direction_evaluations'] += 1
        started = time.monotonic()
        records = {}
        elapsed_accounted = False
        try:
            for label in ('coarse', 'fine'):
                d, grid, bound = self.center[label], self.grids[label], self.bounds[label]
                r, th, nr, nt = d['radial'], d['theta'], grid.nr, grid.nt
                width_key = ('radial_Jacobian_batch_owned_rows' if label == 'coarse'
                             else 'fine_Jacobian_owned_radial_rows')
                width = self.cfg[width_key]
                if isinstance(width, bool) or not isinstance(width, (int, np.integer)) or not 1 <= width <= 16:
                    raise ValueError('unchanged original one-to-sixteen owned radial width required')
                scan = {
                    'grid': label, 'status': 'started', 'owned_radial_rows': 0,
                    'point_count': 0, 'radial_batches': 0,
                    'maximum_replay_error': 0.,
                    'maximum_direction_array_bytes': 0}
                event['grid_scans'].append(scan)
                maxima = [-np.inf, -np.inf]
                best = [None, None]
                coverage = np.zeros(nr, np.int64)
                for begin in range(0, nr, int(width)):
                    self.wall()
                    owned = np.arange(begin, min(nr, begin+int(width)), dtype=np.int64)
                    query = np.unique(np.r_[0, owned, nr-1])
                    positions = np.searchsorted(query, owned)
                    tick = time.monotonic()
                    old_grid = self.factorized.single.source.grid_for(r[query], th)
                    fields = old_grid.fields(self.reference163)
                    fields['_theta'] = th[None, :]
                    frame = target_frame(fields)
                    _, metric, errors = self.factorized._ordinary_slice_and_replay(
                        self.state, r, th, query, bound, old_grid, fields, frame)
                    self.statistics['total_scalar_replay_seconds'] += time.monotonic()-tick
                    error = max(errors.values(), default=0.)
                    scan['maximum_replay_error'] = max(scan['maximum_replay_error'], error)
                    self.statistics['maximum_current_scalar_replay_error'] = max(
                        self.statistics['maximum_current_scalar_replay_error'], error)
                    tick = time.monotonic()
                    dT, dTs = direction_frame_jets(
                        self.factorized, old_grid, fields, frame, p)
                    self.statistics['total_parameter_contraction_seconds'] += time.monotonic()-tick
                    tick = time.monotonic()
                    P0, P1 = periodic_operator(dT, -1), periodic_operator(dTs, -1)
                    dU = (np.asarray(metric['a_s'])[:, None, None]*P0
                          +np.asarray(metric['a'])[:, None, None]*P1)
                    null = _finite(self.field.null_basis.values(r[query]),
                                   (len(query), 5), 'exact five null height densities')
                    dU[:, :, 2] += (null@p[154:])[:, None]
                    self.statistics['total_complete_Pi_seconds'] += time.monotonic()-tick
                    self.statistics['complete_Pi_calls'] += 2
                    self.statistics['original_owned_radial_batches'] += 1
                    peak = sum(a.nbytes for a in (dT, dTs, P0, P1, dU))
                    scan['maximum_direction_array_bytes'] = max(
                        scan['maximum_direction_array_bytes'], peak)
                    self.statistics['largest_direction_array_bytes'] = max(
                        self.statistics['largest_direction_array_bytes'], peak)
                    tick = time.monotonic()
                    U, T = d['U'][owned], d['T'][owned]
                    du, dt = dU[positions], dT[positions]
                    de = 2*np.sum(U*du, axis=2)
                    df = np.sum(T*du+U*dt, axis=2)
                    E, F = d['e'][owned]+de, d['f'][owned]+df
                    if any(not np.all(np.isfinite(a)) for a in (du, dt, de, df, E, F)):
                        raise FloatingPointError('nonfinite complete-grid affine metric direction')
                    for group in (0, 1):
                        values = phi(E.reshape(-1), F.reshape(-1),
                                     np.full(E.size, group, np.int64), self.epsilon)
                        pos = int(np.argmax(values))
                        local_r, ti = divmod(pos, nt)
                        point = int(owned[local_r])*nt+ti
                        value = float(values[pos])
                        previous_point = (best[group]['original_point_flat_index']
                                          if best[group] is not None else grid.point_count)
                        if value > maxima[group] or (value == maxima[group] and point < previous_point):
                            maxima[group] = value
                            best[group] = self._record(label, group, point, {
                                'phi': value,
                                'base_e': float(d['e'][owned[local_r], ti]),
                                'base_f': float(d['f'][owned[local_r], ti]),
                                'de_step': float(de[local_r, ti]), 'df_step': float(df[local_r, ti]),
                                'affine_e': float(E[local_r, ti]), 'affine_f': float(F[local_r, ti])})
                    self.statistics['total_branch_reduction_seconds'] += time.monotonic()-tick
                    coverage[owned] += 1
                    scan['radial_batches'] += 1
                    scan['owned_radial_rows'] += len(owned)
                    scan['point_count'] += len(owned)*nt
                if not np.all(coverage == 1) or scan['point_count'] != grid.point_count or any(x is None for x in best):
                    raise ArithmeticError('incomplete or repeated original-grid directional coverage')
                scan.update(status='complete', radial_coverage_sha256=array_hash(coverage),
                            complete_original_theta_count=nt)
                records[label] = best
                self.statistics['full_grid_scans'] += 1
            ordered = [records[label][group] for label, group in GRID_BRANCHES]
            result = {
                'schema': POLICY+'-four-maxima', 'direction_sha256': key,
                'center_binding_sha256': self.binding_sha256,
                'phi': _readonly(np.array([x['phi'] for x in ordered])),
                'attainers': ordered, 'from_frozen_zero_direction_values': False,
                'full_grid_coverage': {label: self.grids[label].point_count for label in ('coarse', 'fine')}}
            elapsed = time.monotonic()-started
            event.update(status='complete', elapsed_seconds=elapsed,
                         maxima=[float(x) for x in result['phi']],
                         attainers=copy.deepcopy(ordered))
            self.statistics['total_directional_seconds'] += elapsed
            elapsed_accounted = True
            self.cache[key] = (_readonly(p), result)
            self.wall()
            return result
        except Exception as error:
            elapsed = time.monotonic()-started
            event.update(status='raised', elapsed_seconds=elapsed,
                         error={'type': type(error).__name__, 'message': str(error)})
            if not elapsed_accounted:
                self.statistics['total_directional_seconds'] += elapsed
            raise

    def original_row(self, label, flat_id):
        """Only a new original metric row is differentiated, at this frozen center."""
        self._assert_context()
        self.wall()
        grid = self.grids[label]
        flat = int(grid.ids([flat_id])[0])
        if flat//grid.point_count not in (0, 1):
            raise ValueError('only original metric branches may be added by the new oracle')
        key = _key(label, flat, grid.point_count)
        if key in self.extra_rows:
            return self.extra_rows[key]
        width_key = ('radial_Jacobian_batch_owned_rows' if label == 'coarse'
                     else 'fine_Jacobian_owned_radial_rows')
        event = {
            'ordinal': len(self.extra_row_events)+1, 'original_row': grid.coordinate(flat),
            'center_binding_sha256': self.binding_sha256,
            'status': 'new-original-metric-row-J-started', 'phase': self.phase}
        self.extra_row_events.append(event)
        self.statistics['new_selected_metric_row_calls'] += 1
        started = time.monotonic()
        elapsed_accounted = False
        try:
            J, report, obs = self.factorized.evaluate(
                self.state, self.center[label]['radial'], self.center[label]['theta'],
                [flat], self.bounds[label], side=self.field.port.side,
                owned_width=int(self.cfg[width_key]), wall=self.wall)
            if (J.shape != (1, N) or len(obs['e']) != 1
                    or int(obs['row_ids'][0]) != flat or int(obs['row_positions'][0]) != 0):
                raise ArithmeticError('new selected attainer row lost its exact original identity')
            result = {
                'e': float(obs['e'][0]), 'f': float(obs['f'][0]),
                'de': _readonly(obs['de'][0]), 'df': _readonly(obs['df'][0]),
                'first_original_row': grid.coordinate(flat),
                'selected_observable_binding_sha256': obs['binding_sha256'],
                'source': 'new-single-original-metric-row-at-frozen-center'}
            self.extra_rows[key] = result
            elapsed = time.monotonic()-started
            self.statistics['new_selected_metric_rows'] += 1
            self.statistics['new_selected_metric_J_seconds'] += elapsed
            elapsed_accounted = True
            self.statistics['new_selected_metric_J_bytes'] += (
                J.nbytes+obs['de'].nbytes+obs['df'].nbytes)
            event.update(status='complete', elapsed_seconds=elapsed,
                         selected_factorization=copy.deepcopy(report),
                         e=result['e'], f=result['f'],
                         de_sha256=array_hash(result['de']), df_sha256=array_hash(result['df']),
                         selected_observable_binding_sha256=obs['binding_sha256'])
            return result
        except Exception as error:
            elapsed = time.monotonic()-started
            event.update(status='raised', elapsed_seconds=elapsed,
                         error={'type': type(error).__name__, 'message': str(error)})
            if not elapsed_accounted:
                self.statistics['new_selected_metric_J_seconds'] += elapsed
            raise

    def set_post_primary_phase(self):
        self.phase = 'actual-total-step-prediction'

    def report(self):
        return {
            'schema': POLICY+'-oracle-progress',
            'binding': copy.deepcopy(self.binding),
            'binding_sha256': self.binding_sha256,
            'statistics': copy.deepcopy(self.statistics),
            'initial_four_maxima': [float(v) for v in self.base_maxima],
            'initial_complete_slack': self.base_slack,
            'direction_events': copy.deepcopy(self.events),
            'new_original_row_J_events': copy.deepcopy(self.extra_row_events),
            'cached_step_count': len(self.cache),
            'new_original_metric_point_count': len(self.extra_rows),
            'ordinary_geometry_LP_or_actual_pool_mutations_inside_oracle': 0}


class CompleteGridAffineModel(AffineSpectralModel):
    """The frozen solver's exact protocol: selected functions plus four maxima.

    Inherits the explicit AffineSpectralModel type required by the frozen SOC
    diagnostic. Its separate selected_model is used for old-row error
    decomposition; evaluated() here deliberately has four additional entries.
    """
    def __init__(self, selected, oracle, *, artificial_array_fixture_only=False):
        if not isinstance(selected, AffineSpectralModel):
            raise ValueError('a bound original selected affine model is required')
        if not isinstance(oracle, CompleteDirectionalMetricOracle) and not (
                artificial_array_fixture_only and
                selected.primary.information.get('new_complete_oracle_array_fixture_only') is True):
            raise ValueError('the actual original-grid oracle or explicitly labelled new array fixture required')
        self.__dict__ = selected.__dict__.copy()
        self.selected_model = selected
        self.oracle = oracle
        self.selected_count = len(selected.e)
        self.rho0 = max(0., self.outside, float(oracle.base_slack))
        self.rho0_selected = selected.rho0
        self.cut_events = []
        self.selected_point_lookup = {}
        self.selected_full_row_lookup = {}
        for i, tag in enumerate(selected.tags):
            label = tag['grid']
            point_count = oracle.grids[label].point_count
            self.selected_point_lookup.setdefault(
                _key(label, tag['flat_row_id'], point_count), i)
            self.selected_full_row_lookup.setdefault((label, int(tag['flat_row_id'])), i)
        self.binding = {
            'schema': POLICY+'-complete-model',
            'selected_observable_binding': copy.deepcopy(selected.binding),
            'selected_observable_binding_sha256': selected.binding_sha256,
            'full_grid_oracle_binding': copy.deepcopy(oracle.binding),
            'full_grid_oracle_binding_sha256': oracle.binding_sha256,
            'selected_scalar_function_count': self.selected_count,
            'additional_complete_maximum_function_count': 4,
            'complete_initial_slack': self.rho0,
            'inherited_selected_initial_slack': self.rho0_selected,
            'base_slack_difference_retained_not_assumed_zero': self.rho0-self.rho0_selected}
        self.binding_sha256 = digest(self.binding)
        primary = self.primary
        inherited = primary.information['radius_independent_model_sha256']
        primary.information['inherited_selected_affine_radius_independent_model_sha256'] = inherited
        primary.information['affine_spectral_binding'] = copy.deepcopy(self.binding)
        primary.information['radius_independent_model_sha256'] = digest({
            'inherited_selected_affine_model_sha256': inherited,
            'complete_affine_binding_sha256': self.binding_sha256,
            'policy': definition()})
        primary.affine_spectral_model = self

    def evaluated(self, step):
        p = _finite(step, (N,), 'complete model physical step')
        selected = self.selected_model.evaluated(p)
        complete = self.oracle.evaluate(p)
        return {
            'phi': np.r_[selected['phi'], complete['phi']],
            'slack': max(0., self.outside, float(np.max(complete['phi']))-self.target),
            'selected_slack': float(selected['slack']),
            'old_scalar_slack': float(selected['old_scalar_slack']),
            'complete_maxima': complete,
            'old_selected_evaluation': selected,
            'additional_four_indices_start': self.selected_count}

    def slack(self, step):
        p = _finite(step, (N,), 'complete model physical step')
        result = self.oracle.evaluate(p)
        return max(0., self.outside, float(np.max(result['phi']))-self.target)

    def _attainer_row(self, attainer, step):
        tag = attainer['original_row']
        label, flat = tag['grid'], int(tag['flat_row_id'])
        point_count = self.oracle.grids[label].point_count
        lookup = self.selected_point_lookup.get(_key(label, flat, point_count))
        if lookup is None:
            row = self.oracle.original_row(label, flat)
            source = row['source']
        else:
            row = {
                'e': float(self.selected_model.e[lookup]),
                'f': float(self.selected_model.f[lookup]),
                'de': self.selected_model.de[lookup], 'df': self.selected_model.df[lookup],
                'selected_observable_binding_sha256': self.selected_model.binding_sha256}
            source = 'existing-original-selected-point-de-df'
        E = row['e']+float(np.dot(row['de'], step))
        F = row['f']+float(np.dot(row['df'], step))
        comparisons = [abs(row['e']-attainer['base_e']),
                       abs(row['f']-attainer['base_f']),
                       abs(E-attainer['affine_e']), abs(F-attainer['affine_f'])]
        error = max(comparisons)
        scale = max(1., abs(E), abs(F), abs(row['e']), abs(row['f']))
        tolerance = float(self.oracle.cfg['value_Jacobian_replay_relative_tolerance'])
        if not np.isfinite(error) or error > tolerance*scale:
            raise ArithmeticError('full directional attainer and true original row/J disagree')
        if isinstance(self.oracle, CompleteDirectionalMetricOracle):
            self.oracle.statistics['maximum_attainer_direction_vs_selected_J_error'] = max(
                self.oracle.statistics['maximum_attainer_direction_vs_selected_J_error'], error)
        return row, E, F, {
            'source': source, 'direction_vs_selected_max_absolute_error': error,
            'relative_replay_tolerance': tolerance,
            'selected_observable_binding_sha256': row['selected_observable_binding_sha256']}

    def cuts(self, step, function_indices):
        p = _finite(step, (N,), 'new support point')
        indices = np.asarray(function_indices)
        if (indices.ndim != 1 or indices.dtype.kind not in 'iu'
                or np.any(indices < 0) or np.any(indices >= self.selected_count+4)):
            raise ValueError('indices in original selected functions plus four complete maxima required')
        indices = indices.astype(np.int64, copy=False)
        observed = self.oracle.evaluate(p)
        rows, rhs, metadata = [], [], []
        for j in indices:
            if int(j) < self.selected_count:
                A, b, info = self.selected_model.cuts(p, [int(j)])
                rows.append(A[0])
                rhs.append(float(b[0]))
                metadata.append({
                    'function_index': int(j), 'kind': 'unchanged-original-selected-function',
                    'original_row': copy.deepcopy(self.selected_model.tags[int(j)]),
                    'cut_contact_max_absolute_residual': info['contact_max_absolute_residual'],
                    'original_cut_record': info})
                continue
            branch = int(j)-self.selected_count
            attainer = observed['attainers'][branch]
            row, E, F, replay = self._attainer_row(attainer, p)
            tag = attainer['original_row']
            same = self.selected_full_row_lookup.get((tag['grid'], int(tag['flat_row_id'])))
            if same is not None:
                Aold, bold, old_info = self.selected_model.cuts(p, [same])
                rows.append(Aold[0])
                rhs.append(float(bold[0]))
                metadata.append({
                    'function_index': int(j), 'kind': 'complete-max-attainer-reuses-identical-selected-cut',
                    'maximum_index': branch, 'original_row': copy.deepcopy(tag),
                    'directional_oracle_attainer': copy.deepcopy(attainer),
                    'selected_J_replay': replay, 'original_cut_record': old_info,
                    'cut_contact_max_absolute_residual': old_info['contact_max_absolute_residual']})
                continue
            group = int(tag['group'])
            pe, pf = phi_gradient([E], [F], [group], self.epsilon)
            grad = pe[0]*np.asarray(row['de'])+pf[0]*np.asarray(row['df'])
            value = float(phi([E], [F], [group], self.epsilon)[0])
            intercept = value-float(grad@p)
            A = np.zeros(N+2)
            A[:N] = grad*np.asarray(self.primary.step_scale)
            A[N] = -1.
            b = self.target-intercept
            if not np.all(np.isfinite(A)) or not np.isfinite(b):
                raise FloatingPointError('nonfinite true complete-max supporting cut')
            rows.append(A)
            rhs.append(float(b))
            metadata.append({
                'function_index': int(j), 'kind': 'complete-original-grid-max-attainer',
                'maximum_index': branch, 'original_row': copy.deepcopy(tag),
                'directional_oracle_attainer': copy.deepcopy(attainer),
                'selected_J_replay': replay,
                'same_row_affine_value_for_support': value,
                'oracle_minus_replayed_same_row_phi': attainer['phi']-value,
                'cut_contact_max_absolute_residual': abs(float(grad@p)+intercept-value)})
        A = np.array(rows, dtype=float).reshape(len(indices), N+2)
        b = np.array(rhs, dtype=float)
        record = {
            'schema': POLICY+'-supporting-cuts',
            'soft_indices': indices.tolist(),
            'original_rows': [copy.deepcopy(x['original_row']) for x in metadata],
            'function_index_meaning': 'old selected entries then coarse+/coarse-/fine+/fine- maxima',
            'cut_point_independent_array_sha256': array_hash(p),
            'A_sha256': array_hash(A), 'b_sha256': array_hash(b),
            'observable_binding_sha256': self.binding_sha256,
            'rows': len(indices), 'per_row': metadata,
            'contact_max_absolute_residual': max(
                (x['cut_contact_max_absolute_residual'] for x in metadata), default=0.),
            'no_prediction_driven_actual_pool_mutation': True}
        self.cut_events.append(copy.deepcopy(record))
        return A, b, record

    def summary(self):
        return {
            'schema': POLICY+'-finite-primary',
            'old_selected_function_count': self.selected_count,
            'complete_grid_maximum_functions': 4,
            'total_convex_function_count': self.selected_count+4,
            'full_original_soft_grid_row_counts': {
                label: 2*self.oracle.grids[label].point_count for label in ('coarse', 'fine')},
            'independent_columns': N, 'binding': copy.deepcopy(self.binding),
            'binding_sha256': self.binding_sha256,
            'rho_out': self.outside, 'initial_slack': self.rho0,
            'inherited_selected_initial_slack': self.rho0_selected,
            'target_exact': self.target_exact,
            'epsilon_exact': str(Q(self.oracle.cfg['metric_proposal_epsilon_exact']))}

    def complete_report(self):
        return {
            'schema': POLICY+'-complete-model-progress',
            'summary': self.summary(),
            'oracle': self.oracle.report(),
            'new_support_requests': copy.deepcopy(self.cut_events),
            'old_frozen_inner_solver_and_all_shared_budgets_are_unchanged': True}

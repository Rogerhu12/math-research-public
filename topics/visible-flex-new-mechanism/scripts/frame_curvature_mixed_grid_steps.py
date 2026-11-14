#!/usr/bin/env python3
"""Fixed-70 feasible steps with selected fine-grid physical Jacobian rows.

The physical space, height mean, fixed metric and both complete value grids
are unchanged. Fine derivatives use a complete uniform angle circle in small
radial batches; isolated-angle calls to the periodic primitive are forbidden.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time

import numpy as np
import scipy

from frame_collar_residual_audit import digest
from frame_height_affine_gate import EvaluationBudgetReached, require_public_research_environment
from frame_metric_epigraph import geometry_values, metric_rows
from frame_metric_epigraph_dense import mirror_values
from frame_curvature_epigraph_exchange import GROUPS, POSITION_JETS
from frame_curvature_feasible_steps import (
    FeasibleStepObjective, linear_proposal, compact_decision,
    configuration as previous_configuration, implementation_hashes as previous_hashes,
)

POLICY = 'fixed-70-coarse-curvature-fine-physical-selected-Jacobian-v1'
FINE_GROUPS = GROUPS[:7]


def implementation_hashes():
    result = previous_hashes()
    path = Path(__file__)
    result[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def configuration(base=None):
    cfg = previous_configuration(base)
    cfg.update(mixed_grid_policy=POLICY,
        fine_Jacobian_owned_radial_rows=6,
        fine_initial_metric_activation_exact='1/1000',
        fine_initial_metric_rows_per_radial_branch=2,
        max_fine_physical_pool_rows=4096,
        fine_pool_adds_all_observed_physical_violations_up_to_capacity=True,
        added_fine_rows_restart_only_the_linear_model_at_last_accepted_state=True,
        all_coarse_learned_rows_retained=True,
        fine_Jacobian_uses_full_uniform_circle_not_isolated_angles=True,
        immutable_height_mean_nodes_are_not_changed_by_fine_Jacobian=True,
        no_new_physical_parameter_or_basis=True)
    return cfg


def physical_rows(data, side, cfg):
    values = geometry_values(data)
    cm, cp = metric_rows(values['e'], values['f'], float(Q(cfg['fixed_metric_budget_exact'])))
    X = np.asarray(data['X'], float)
    p = float(Q(cfg['hard_strip_half_width_exact']))
    R = float(Q(cfg['hard_ball_radius_exact']))
    mirror = mirror_values(data, float(Q(cfg['mirror_target_exact'])))
    return np.stack([cm, cp, side*X[..., 2]-float(Q(cfg['minimum_signed_height_exact'])),
        1-np.sum(X*X, axis=-1)/R**2, 1-X[..., 1]/p, 1+X[..., 1]/p,
        mirror['polynomial']])


def selected_physical_derivatives(data, groups, side, cfg):
    """One row per selected point; all derivatives are physical, no auxiliary."""
    groups = np.asarray(groups, int)
    X, U, T = (np.asarray(data[key], float) for key in ['X', 'Xs', 'T'])
    JX, JU, JT = (np.asarray(data['jac_'+key], float) for key in ['X', 'Xs', 'T'])
    if (X.ndim != 2 or X.shape[1] != 3 or U.shape != X.shape or T.shape != X.shape
            or groups.shape != (len(X),) or np.any(groups < 0) or np.any(groups >= 7)
            or JX.ndim != 3 or JX.shape[:2] != X.shape or JU.shape != JX.shape or JT.shape != JX.shape):
        raise ValueError('matching finite selected first jets and seven physical group labels required')
    de = 2*np.einsum('ic,icn->in', U, JU)
    df = np.einsum('ic,icn->in', T, JU)+np.einsum('ic,icn->in', U, JT)
    f = np.sum(U*T, axis=-1)
    bar = float(Q(cfg['fixed_metric_budget_exact']))
    R, p = float(Q(cfg['hard_ball_radius_exact'])), float(Q(cfg['hard_strip_half_width_exact']))
    J = np.empty((len(X), JX.shape[-1]))
    for group in range(7):
        m = groups == group
        if not np.any(m):
            continue
        if group < 2:
            J[m] = (-1 if group == 0 else 1)*de[m]-(2*f[m]/bar)[:, None]*df[m]
        elif group == 2:
            J[m] = side*JX[m, 2]
        elif group == 3:
            J[m] = -2*np.einsum('ic,icn->in', X[m], JX[m])/R**2
        elif group == 4:
            J[m] = -JX[m, 1]/p
        elif group == 5:
            J[m] = JX[m, 1]/p
        else:
            W = np.cross(U[m], T[m]); z = X[m, 2]
            D = z[:, None]**2*W
            D[:, 2] -= float(Q(cfg['mirror_target_exact']))**2*W[:, 2]
            J[m] = (2*z*np.sum(W*W, axis=1))[:, None]*JX[m, 2]
            J[m] += 2*np.einsum('ic,icn->in', np.cross(T[m], D), JU[m])
            J[m] += 2*np.einsum('ic,icn->in', np.cross(D, U[m]), JT[m])
    if not np.all(np.isfinite(J)):
        raise FloatingPointError('nonfinite selected fine physical derivatives')
    return J


def fine_row_coordinates(indices, radial, theta):
    indices = np.asarray(indices, dtype=np.int64)
    radial, theta = np.asarray(radial, float), np.asarray(theta, float)
    Nr, Nt = len(radial), len(theta)
    if indices.ndim != 1 or np.any(indices < 0) or np.any(indices >= 7*Nr*Nt):
        raise ValueError('fine indices must encode an actual seven-group grid row')
    records = []
    for value in indices:
        group, point = divmod(int(value), Nr*Nt)
        ri, ti = divmod(point, Nt)
        records.append({'fine_flat_index':int(value), 'group_index':group, 'group':FINE_GROUPS[group],
            'radial_index':ri, 'fine_theta_index':ti, 't':float(radial[ri]), 'theta':float(theta[ti]),
            't_exact_binary64':str(Q.from_float(float(radial[ri]))),
            'theta_exact_binary64':str(Q.from_float(float(theta[ti]))),
            'theta_over_pi_exact':str(Q(2*ti, Nt)),
            'is_missing_odd_angle_of_coarse_grid':bool(ti % 2),
            'coarse_theta_index_if_even':ti//2 if not ti % 2 else None})
    return records


class MixedGridStepObjective(FeasibleStepObjective):
    def __init__(self, *args, **kwargs):
        self.fine_pool = np.empty(0, dtype=np.int64)
        self.fine_pool_version = 0
        self.fine_pool_history = []
        self.fine_derivative_cache = None
        self.fine_Jacobian_batches = 0
        self.fine_Jacobian_refreshes = 0
        self.fine_Jacobian_seconds = 0.
        self.fine_Jacobian_maximum_returned_bytes = 0
        self.fine_Jacobian_maximum_retained_bytes = 0
        self.fine_Jacobian_maximum_query_radial_rows = 0
        self.fine_batch_replay_maxima = {k:0. for k in POSITION_JETS+('center', 'metric', 'height')}
        super().__init__(*args, **kwargs)
        if (self.cfg['fine_Jacobian_owned_radial_rows'] < 1
                or self.cfg['fine_initial_metric_rows_per_radial_branch'] < 1
                or self.cfg['max_fine_physical_pool_rows'] < 2
                or Q(self.cfg['fine_initial_metric_activation_exact']) < 0):
            raise ValueError('positive fine-pool/batch sizes and nonnegative activation distance required')
        self.fine_theta = np.arange(2*len(self.theta))*np.pi/len(self.theta)
        self.evaluation_definition.update(
            mixed_grid_policy=POLICY,
            fine_selected_Jacobian_definition={
                'full_uniform_angular_nodes':len(self.fine_theta),
                'all_exact_binary64_theta_nodes':[str(Q.from_float(float(x))) for x in self.fine_theta],
                'group_order':list(FINE_GROUPS),
                'fine_flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',
                'owned_radial_rows_per_batch':self.cfg['fine_Jacobian_owned_radial_rows'],
                'each_query_includes_original_radial_indices_0_and_last':True,
                'only_first_position_parameter_jets_requested':True,
                'height_mean_and_height_primitive_evaluation_unchanged':True,
                'known_fine_violations_use_original_physical_tolerances':True},
            implementation_source_sha256=implementation_hashes())
        self.evaluation_sha256 = digest(self.evaluation_definition)

    def set_fine_pool(self, indices, reason):
        raw = list(indices)
        if any(not isinstance(i, (int, np.integer)) for i in raw):
            raise ValueError('fine row IDs must be integers')
        arr = np.asarray(sorted(set(int(i) for i in raw)), dtype=np.int64)
        total = 7*len(self.radial)*len(self.fine_theta)
        if (np.any(arr < 0) or np.any(arr >= total)
                or len(arr) > self.cfg['max_fine_physical_pool_rows']
                or not set(self.fine_pool).issubset(arr)):
            raise ValueError('fine pool must retain all old valid rows within its explicit capacity')
        added = np.setdiff1d(arr, self.fine_pool)
        self.fine_pool = arr; self.fine_pool_version += 1; self.fine_derivative_cache = None
        record = {'version':self.fine_pool_version, 'row_count':len(arr), 'row_indices':arr.tolist(),
            'row_indices_sha256':digest(arr.tolist()), 'added_row_indices':added.tolist(),
            'added_original_grid_coordinates':fine_row_coordinates(added, self.radial, self.fine_theta),
            'group_order':list(FINE_GROUPS), 'total_full_grid_rows':total,
            'flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',
            'coarse_pool_is_separate_and_unchanged_by_this_update':True, 'reason':copy.deepcopy(reason)}
        self.fine_pool_history.append(record)
        return record

    def fine_rows(self, state):
        self.fine_decision(state)
        return physical_rows(self.fine_cache['data'], self.gate.side, self.cfg)

    def initialize_fine_pool(self, state, *, known_metric_locations=()):
        rows = self.fine_rows(state)
        Nr, Nt = len(self.radial), len(self.fine_theta)
        chosen = set(int(i) for i in self.fine_pool)
        level = float(Q(self.cfg['fine_initial_metric_activation_exact']))
        k = min(Nt, int(self.cfg['fine_initial_metric_rows_per_radial_branch']))
        for group in [0, 1]:
            for ri in range(Nr):
                candidates = np.flatnonzero(rows[group, ri] <= level)
                if len(candidates):
                    selected = candidates[np.argsort(rows[group, ri, candidates], kind='stable')[:k]]
                    chosen.update(int(group*Nr*Nt+ri*Nt+ti) for ti in selected)
        bound = []
        for location in known_metric_locations:
            t, angle = float(location['t']), float(location['theta'])
            ri, ti = int(np.argmin(abs(self.radial-t))), int(np.argmin(abs(self.fine_theta-angle)))
            tol = 128*np.finfo(float).eps*max(1., abs(t), abs(angle))
            if abs(self.radial[ri]-t) > tol or abs(self.fine_theta[ti]-angle) > tol:
                raise ValueError('saved fine peak is not an actual node of the unchanged complete grid')
            chosen.update(group*Nr*Nt+ri*Nt+ti for group in [0, 1])
            bound.append({'saved_location':copy.deepcopy(location), 'radial_index':ri, 'fine_theta_index':ti})
        if not chosen:
            for group in [0, 1]:
                point = int(np.argmin(rows[group]))
                chosen.add(group*Nr*Nt+point)
        return self.set_fine_pool(chosen, {'kind':'near-active-fine-metric-plus-published-fine-peaks',
            'activation_exact':self.cfg['fine_initial_metric_activation_exact'],
            'selected_per_radial_branch':k, 'saved_peak_bindings':bound})

    def learn_fine_violations(self, state, reason):
        rows = self.fine_rows(state)
        limits = self.row_tolerances()[:7, None, None]
        violation = rows < -limits
        missing = violation.copy(); missing.reshape(-1)[self.fine_pool] = False
        ids = np.flatnonzero(missing)
        detail = {'omitted_violating_count':int(len(ids)),
            'all_fine_physical_violating_count':int(np.count_nonzero(violation)),
            'group_counts':{name:{'whole_grid':int(np.count_nonzero(violation[g])),
                                  'omitted':int(np.count_nonzero(missing[g]))} for g, name in enumerate(FINE_GROUPS)},
            'original_actual_tolerances':self.row_tolerances()[:7].tolist()}
        if not len(ids):
            return None, detail
        if len(self.fine_pool)+len(ids) > self.cfg['max_fine_physical_pool_rows']:
            detail.update(pool_capacity_would_be_exceeded=True,
                proposed_pool_rows=len(self.fine_pool)+len(ids))
            return None, detail
        record = self.set_fine_pool(np.r_[self.fine_pool, ids], {'kind':reason,
            'full_fine_physical_violation_summary':detail,
            'every_observed_omitted_fine_physical_violation_added':True})
        return record, detail

    def fine_derivatives(self, state):
        self.fine_decision(state)
        if not len(self.fine_pool):
            raise ValueError('initialize the fine metric pool before requesting its Jacobian')
        if (self.fine_derivative_cache is not None
                and self.fine_derivative_cache['pool_version'] == self.fine_pool_version
                and np.array_equal(state, self.fine_derivative_cache['state'])):
            return self.fine_derivative_cache['J']
        before = time.monotonic()
        Nr, Nt = len(self.radial), len(self.fine_theta)
        groups, points = self.fine_pool//(Nr*Nt), self.fine_pool % (Nr*Nt)
        radial_ids = np.unique(points//Nt)
        J = np.empty((len(points), self.n)); covered = np.zeros(len(points), bool)
        width = int(self.cfg['fine_Jacobian_owned_radial_rows'])
        self.fine_Jacobian_refreshes += 1
        for start in range(0, len(radial_ids), width):
            self._wall()
            owned = radial_ids[start:start+width]
            selected = np.flatnonzero(np.isin(points//Nt, owned))
            query = np.unique(np.r_[0, owned, Nr-1])
            data = self.problem.geometry(state, self.radial[query], self.fine_theta, self.order,
                jacobian=True, full_two_jet_jacobian=False)
            self.fine_Jacobian_batches += 1
            self.fine_Jacobian_maximum_query_radial_rows = max(self.fine_Jacobian_maximum_query_radial_rows, len(query))
            scale, maximum = 1., 0.
            for key in POSITION_JETS+('center',):
                current, target = np.asarray(data[key]), np.asarray(self.fine_cache['data'][key])[query]
                if current.shape != target.shape or not np.all(np.isfinite(current)):
                    raise FloatingPointError('bad same-state fine batch ordinary jet: '+key)
                difference = float(np.max(abs(current-target)))
                self.fine_batch_replay_maxima[key] = max(self.fine_batch_replay_maxima[key], difference)
                maximum = max(maximum, difference); scale = max(scale, float(np.max(abs(target))))
            for group in ['metric', 'height']:
                for key, target0 in self.fine_cache['data'][group].items():
                    current, target = np.asarray(data[group][key]), np.asarray(target0)[query]
                    if current.shape != target.shape or not np.all(np.isfinite(current)):
                        raise FloatingPointError('bad same-state fine batch '+group+'/'+key)
                    difference = float(np.max(abs(current-target)))
                    self.fine_batch_replay_maxima[group] = max(self.fine_batch_replay_maxima[group], difference)
                    maximum = max(maximum, difference); scale = max(scale, float(np.max(abs(target))))
            if maximum > self.cfg['value_Jacobian_replay_relative_tolerance']*scale:
                raise ArithmeticError('fine radial batching changed ordinary geometry beyond floating replay tolerance')
            total = 0
            for key in ['X', 'Xs', 'Xt', 'T']:
                item = np.asarray(data['jac_'+key])
                if item.shape != (len(query), Nt, 3, self.n) or not np.all(np.isfinite(item)):
                    raise FloatingPointError('finite complete fine first-jet parameter Jacobian required')
                total += item.nbytes
            self.fine_Jacobian_maximum_returned_bytes = max(self.fine_Jacobian_maximum_returned_bytes, total)
            ri = np.searchsorted(query, points[selected]//Nt); ti = points[selected] % Nt
            small = {key:np.asarray(data[key])[ri, ti] for key in ['X', 'Xs', 'T', 'jac_X', 'jac_Xs', 'jac_T']}
            J[selected] = selected_physical_derivatives(small, groups[selected], self.gate.side, self.cfg)
            covered[selected] = True
            del data, small, item
        if not np.all(covered) or not np.all(np.isfinite(J)):
            raise ArithmeticError('fine selected Jacobian ownership is incomplete')
        J.setflags(write=False)
        self.fine_derivative_cache = {'state':np.asarray(state).copy(), 'pool_version':self.fine_pool_version, 'J':J}
        self.fine_Jacobian_maximum_retained_bytes = max(self.fine_Jacobian_maximum_retained_bytes, J.nbytes)
        self.fine_Jacobian_seconds += time.monotonic()-before
        self._wall()
        return J

    def linear_rows(self, vector):
        coarse = self.constraint_fun(vector)
        coarse_J = self.constraint_jac(vector)[:, :self.n]
        fine = self.fine_rows(vector[:-1]).reshape(-1)[self.fine_pool]
        fine_J = self.fine_derivatives(vector[:-1])
        groups = np.r_[self.pool//(len(self.radial)*len(self.theta)),
                       self.fine_pool//(len(self.radial)*len(self.fine_theta))]
        return np.r_[coarse, fine], np.concatenate([coarse_J, fine_J]), groups, self.row_tolerances()[groups]

    def snapshot(self):
        result = super().snapshot()
        result.update(mixed_grid_policy=POLICY,
            fine_physical_row_pool_history=copy.deepcopy(self.fine_pool_history),
            fine_physical_pool_row_count=len(self.fine_pool),
            fine_selected_Jacobian_batches=self.fine_Jacobian_batches,
            fine_selected_Jacobian_refreshes=self.fine_Jacobian_refreshes,
            fine_selected_Jacobian_seconds=self.fine_Jacobian_seconds,
            fine_selected_Jacobian_maximum_returned_bytes=self.fine_Jacobian_maximum_returned_bytes,
            fine_selected_Jacobian_maximum_retained_bytes=self.fine_Jacobian_maximum_retained_bytes,
            fine_selected_Jacobian_maximum_query_radial_rows=self.fine_Jacobian_maximum_query_radial_rows,
            fine_batch_ordinary_replay_maxima=copy.deepcopy(self.fine_batch_replay_maxima),
            fine_parameter_Jacobian_never_uses_isolated_angle_queries=True,
            physical_height_mean_and_primitive_are_unchanged=True)
        return result


def run_mixed_steps(objective, initial, *, known_metric_locations=(), artificial_inputs_only=False,
                    evaluate_only=False):
    if not artificial_inputs_only:
        require_public_research_environment()
    elif objective.gate.kind != 'artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the declared artificial array family')
    cfg = objective.cfg
    target = float(Q(cfg['fixed_curvature_target_exact']))
    zeta = target/float(Q(cfg['curvature_scale_exact']))
    metadata = {'method':POLICY, 'fixed_target_lambda_exact':cfg['fixed_curvature_target_exact'],
        'nonlinear_minimize_invocation_count':0, 'linear_program_invocation_count':0,
        'max_linear_models':cfg['max_linear_models'],
        'shared_max_physical_evaluations_coarse_plus_fine':cfg['max_physical_evaluations'],
        'shared_optimization_seconds':cfg['max_seconds'],
        'artificial_inputs_only':bool(artificial_inputs_only), 'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__, 'scipy_version':scipy.__version__, 'models':[],
        'acceptance_uses_original_physical_tolerances_on_both_grids':True,
        'rejected_trial_is_never_the_next_linearization_state':True,
        'all_saved_old_coarse_rows_remain_enforced':True}
    def finish(status, error=None, budget=None):
        snap = objective.snapshot()
        if objective.checkpoint:
            objective.checkpoint(snap)
        selected = snap.get('selected_two_grid_physical_point')
        return {'status':status, 'error':error, 'budget_message':budget, 'solver':metadata, 'checkpoint':snap,
            'selected_point':'last both-grid physical accepted point with monotone actual curvature',
            'fixed_target_reached':bool(selected is not None and selected['maximum_curvature_on_both_grids']
                <= target+cfg['direct_curvature_tolerance']),
            'no_metric_parameter_height_reference_or_physical_space_change':True}
    try:
        current = np.asarray(initial, float).copy(); vector = np.r_[current, zeta]
        coarse = objective.evaluate(vector)['decision']
        if not coarse['eligible_under_fixed_metric_and_physical_gates']:
            return finish('initial-coarse-physical-gate-failed')
        fine = objective.fine_decision(current)
        if not fine['eligible_under_fixed_metric_and_physical_gates']:
            return finish('initial-fine-physical-gate-failed')
        accepted = objective.accepted_point(current, coarse, fine, {'kind':'published-two-grid-06a603-accepted-start'})
        if not len(objective.pool):
            objective.initialize_pool(vector)
        objective.expand_pool(vector, 'initial-fixed-70-coarse-violations')
        objective.initialize_fine_pool(current, known_metric_locations=known_metric_locations)
        if evaluate_only:
            return finish('evaluation-only-mixed-grid-baseline')
        if accepted['maximum_curvature_on_both_grids'] <= target+cfg['direct_curvature_tolerance']:
            return finish('fixed-target-already-reached-on-both-grids')
        objective.linear_rows(vector)
        objective.begin_optimization()
        trust = float(Q(cfg['initial_trust_box_fraction_exact']))
        minimum_trust = float(Q(cfg['minimum_trust_box_fraction_exact']))
        drop = float(Q(cfg['minimum_accepted_curvature_decrease_exact']))
        for number in range(int(cfg['max_linear_models'])):
            objective._wall(); vector = np.r_[current, zeta]
            rows, J, groups, tolerances = objective.linear_rows(vector)
            remaining = cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
            local = dict(cfg, linear_program_seconds=min(cfg['linear_program_seconds'], max(.001, remaining)))
            step, lp = linear_proposal(rows, J, groups, tolerances, current, objective.lower, objective.upper,
                objective.gate.row, objective.gate.intercept+float(objective.gate.row@current)-objective.gate.target,
                trust, local)
            metadata['linear_program_invocation_count'] += 1
            model = {'number':number+1, 'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'coarse_pool_rows':len(objective.pool), 'fine_pool_rows':len(objective.fine_pool),
                'linear_program':lp, 'trials':[]}
            metadata['models'].append(model); objective._wall()
            if step is None:
                trust *= .5; model['result'] = 'linear-proposal-failed-trust-shrunk'
                if trust < minimum_trust:
                    return finish('minimum-trust-after-linear-proposal-failure')
                continue
            if lp['predicted_slack_improvement'] <= cfg['linear_model_improvement_floor'] or np.max(abs(step)) == 0:
                model['result'] = 'no-fixed-target-linear-improvement'
                return finish('fixed-target-mixed-linear-model-stalled')
            model['exact_binary64_proposed_step'] = [str(Q.from_float(float(x))) for x in step]
            old_max = accepted['maximum_curvature_on_both_grids']
            succeeded, relearned = False, False
            for k in range(int(cfg['maximum_backtracks_per_model'])):
                candidate = current+2.**(-k)*step
                trial = {'alpha_exact':str(Q(1, 2**k)), 'accepted_as_next_iterate':False,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
                model['trials'].append(trial)
                record = objective.evaluate(np.r_[candidate, zeta]); decision = record['decision']
                trial.update(attempt_status='coarse-value-call-complete',
                    coarse_physical_evaluation=record['physical_geometry_evaluation'],
                    coarse_decision=compact_decision(decision))
                coarse_k = decision['direct_maximum_absolute_principal_curvature']
                potentially_better = coarse_k <= target+cfg['direct_curvature_tolerance'] or old_max-coarse_k >= drop
                fine_dec = None
                if decision['eligible_under_fixed_metric_and_physical_gates'] and potentially_better:
                    fine_dec = objective.fine_decision(candidate)
                    trial.update(fine_decision=compact_decision(fine_dec), fine_value_evaluation=objective.fine_evaluations)
                    new_k = max(coarse_k, fine_dec['direct_maximum_absolute_principal_curvature'])
                    if (fine_dec['eligible_under_fixed_metric_and_physical_gates'] and new_k < old_max
                            and (new_k <= target+cfg['direct_curvature_tolerance'] or old_max-new_k >= drop)):
                        accepted = objective.accepted_point(candidate, decision, fine_dec,
                            {'kind':'mixed-grid-physical-short-step', 'model':number+1,
                             'alpha_exact':str(Q(1, 2**k)), 'previous_maximum_curvature':old_max})
                        current = candidate.copy(); succeeded = True
                        trial.update(accepted_as_next_iterate=True, accepted_index=accepted['accepted_index'])
                added, detail = objective.expand_pool(np.r_[candidate, zeta], 'observed-coarse-trial-violations')
                trial.update(coarse_omitted_rows=detail['omitted_violating_count'],
                    new_coarse_rows=len(added['added_row_indices']) if added else 0)
                if detail.get('pool_capacity_would_be_exceeded'):
                    return finish('coarse-pool-capacity-preserved-last-accepted-state')
                if fine_dec is not None:
                    added_fine, fine_detail = objective.learn_fine_violations(candidate, 'observed-full-fine-trial-violations')
                    trial.update(fine_omitted_rows=fine_detail['omitted_violating_count'],
                        fine_violation_groups=fine_detail['group_counts'],
                        new_fine_rows=len(added_fine['added_row_indices']) if added_fine else 0)
                    if fine_detail.get('pool_capacity_would_be_exceeded'):
                        return finish('fine-pool-capacity-preserved-last-accepted-state')
                    relearned = bool(added_fine)
                if succeeded:
                    model['result'] = 'accepted-two-grid-physical-short-step'
                    if objective.checkpoint:
                        objective.checkpoint(objective.snapshot())
                    if accepted['maximum_curvature_on_both_grids'] <= target+cfg['direct_curvature_tolerance']:
                        return finish('fixed-70-reached-on-both-original-value-grids')
                    break
                if relearned:
                    model['result'] = 'new-fine-rows-relinearize-at-last-accepted-state'
                    break
            if not succeeded and not relearned:
                trust *= .5; model['result'] = 'backtracking-rejected-last-two-grid-state-preserved'
                if trust < minimum_trust:
                    return finish('minimum-trust-after-two-grid-backtracking')
            if objective.checkpoint:
                objective.checkpoint(objective.snapshot())
        return finish('mixed-grid-linear-model-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('mixed-grid-shared-budget-exit', budget=str(error))
    except Exception as error:
        return finish('mixed-grid-short-step-error', error={'type':type(error).__name__, 'message':str(error)})


def developer_check():
    """Only new row mathematics, batch interface and controlled-step branches."""
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_curvature_feasible_steps import _StepToy

    class Array(_CurvatureArrayProblem):
        def geometry(self, state, radial, theta, order, jacobian=False, full_two_jet_jacobian=False):
            data = super().geometry(state, radial, theta, order, jacobian, full_two_jet_jacobian)
            r = np.asarray(radial)
            data['height'] = {'b':np.full(len(r), .5*state[1]+.25*state[2]),
                'b_s':np.zeros(len(r)), 'b_ss':np.zeros(len(r))}
            return data

    p = Array(); state = np.array([.3, .6, .6])
    radial = np.array([0., .2, .4, .7, 1.]); theta = np.arange(12)*np.pi/6
    cfg = configuration(); cfg.update(fixed_metric_budget_exact='1/5', curvature_scale_exact='3',
        mirror_target_exact='1/1000', radial_Jacobian_batch_owned_rows=2,
        fine_Jacobian_owned_radial_rows=2, max_physical_evaluations=80)
    gate = HeightAffineGate.from_artificial_array_problem(p)
    obj = MixedGridStepObjective(p, gate, radial, theta, 3, np.array([-.8, -1., -1.]),
        np.array([2., 1., 1.]), cfg=cfg)
    Nt = len(obj.fine_theta); count = len(radial)*Nt
    rows = [g*count+(1+g % 3)*Nt+(2*g+1) for g in range(7)]
    obj.set_fine_pool(rows, {'kind':'artificial-seven-group-odd-angles'})
    J = obj.fine_derivatives(state)
    calls = p.calls; J2 = obj.fine_derivatives(state); reuse = p.calls == calls
    direction = np.array([.2, -.3, .4]); eps = 1e-6
    plus = obj.fine_rows(state+eps*direction).reshape(-1)[obj.fine_pool]
    minus = obj.fine_rows(state-eps*direction).reshape(-1)[obj.fine_pool]
    fd_error = float(np.max(abs((plus-minus)/(2*eps)-J@direction)))
    data = p.geometry(state, radial, obj.fine_theta, 3, jacobian=True)
    groups = obj.fine_pool//count; point = obj.fine_pool % count
    ri, ti = point//Nt, point % Nt
    small = {key:np.asarray(data[key])[ri, ti] for key in ['X', 'Xs', 'T', 'jac_X', 'jac_Xs', 'jac_T']}
    direct = selected_physical_derivatives(small, groups, 1, cfg)
    batch_error = float(np.max(abs(J-direct)))
    descriptions = fine_row_coordinates(obj.fine_pool, radial, obj.fine_theta)
    odd = all(item['is_missing_odd_angle_of_coarse_grid'] for item in descriptions)
    try:
        obj.set_fine_pool([7*count], {'kind':'bad-index'}); rejects = False
    except ValueError:
        rejects = True

    class Step(_StepToy):
        def __init__(self, failure=False):
            super().__init__(target=2.5, fine_limit=.25, inject_fine_failure=failure)
            self.cfg = configuration(self.cfg)
            self.cfg.update(curvature_scale_exact='1', fixed_curvature_target_exact='5/2',
                max_seconds=10., initial_trust_box_fraction_exact='1/4',
                minimum_accepted_curvature_decrease_exact='1/1000000')
            self.fine_pool = np.array([0], dtype=int)
            self.fine_pool_history = []
        def initialize_fine_pool(self, state, known_metric_locations=()):
            return None
        def linear_rows(self, vector):
            values = self.constraint_fun(vector)
            jac = self.constraint_jac(vector)[:, :1]
            groups = self.pool//2
            if 1 in self.fine_pool:
                values = np.r_[values, self.fine_limit-vector[0]]
                jac = np.r_[jac, [[-1.]]]; groups = np.r_[groups, 0]
            return values, jac, groups, self.row_tolerances()[groups]
        def learn_fine_violations(self, state, reason):
            failed = state[0] > self.fine_limit+1e-9 and 1 not in self.fine_pool
            detail = {'omitted_violating_count':int(failed), 'group_counts':{}}
            if not failed:
                return None, detail
            self.fine_pool = np.array([0, 1]); self.fine_pool_history.append({'reason':reason})
            return {'added_row_indices':[1]}, detail
        def snapshot(self):
            return dict(super().snapshot(), fine_physical_row_pool_history=self.fine_pool_history)

    toy = Step(); result = run_mixed_steps(toy, np.zeros(1), artificial_inputs_only=True)
    learned = any(t.get('new_fine_rows', 0) for m in result['solver']['models'] for t in m['trials'])
    restarted = any(m.get('result') == 'new-fine-rows-relinearize-at-last-accepted-state'
        for m in result['solver']['models'])
    accepted = result['checkpoint']['accepted_iterates']
    feasible = all(x['physical_parameter_coefficients_binary64'][0] <= .25+1e-9 for x in accepted)
    mono = all(b['maximum_curvature_on_both_grids'] < a['maximum_curvature_on_both_grids']
        for a, b in zip(accepted, accepted[1:]))
    failed = run_mixed_steps(Step(True), np.zeros(1), artificial_inputs_only=True)
    preserved = failed['status'] == 'mixed-grid-short-step-error' and len(failed['checkpoint']['accepted_iterates']) == 1
    passed = bool(fd_error < 3e-7 and batch_error < 1e-12 and reuse and np.array_equal(J, J2)
        and odd and rejects and learned and restarted and feasible and mono and preserved
        and not result['fixed_target_reached'])
    return {'schema':'mixed-grid-selected-first-jet-artificial-check-v1', 'artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,
        'seven_group_selected_fine_directional_Jacobian_error':fd_error,
        'fine_selected_batch_vs_full_circle_Jacobian_error':batch_error,
        'same_state_fine_batch_ordinary_replay_maxima':obj.fine_batch_replay_maxima,
        'cached_fine_selected_Jacobian_reused':reuse,
        'all_artificial_selected_angles_are_odd_fine_indices':odd,
        'invalid_fine_row_index_rejected':rejects,
        'new_fine_violation_added_and_relinearized_at_accepted_state':learned and restarted,
        'all_accepted_toy_states_pass_fine_gate':feasible,
        'accepted_toy_actual_curvature_strictly_decreases':mono,
        'unattained_target_not_claimed':not result['fixed_target_reached'],
        'injected_fine_failure_preserves_original_eligible_state':preserved,
        'toy_exit_status':result['status'], 'toy_error':result.get('error'), 'passed':passed}

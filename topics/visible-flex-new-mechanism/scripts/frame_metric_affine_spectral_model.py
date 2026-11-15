#!/usr/bin/env python3
"""Finite affine-(e,f) spectral model inside the original159 mapped LP.

This source is new. Merely storing it runs no development or research.
Only the soft primary model changes: both true metric observables are
linearized, while their regularized spectral norm is evaluated exactly.
All public research, including new artificial checks, is run by Actions.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import ArrayLP, array_digest
from frame_metric_entry_tail_height159 import solve_primary as frozen_solve_primary
from frame_metric_spectral_recovery import EPSILON_EXACT, PROPOSAL_BRANCHES

POLICY = 'same159-affine-ef-convex-spectral-primary-v1'
N = 159
MAX_INNER_PRIMARY_LPS = 3
GAP_GAIN_FRACTION_EXACT = '1/8'


def implementation_hashes():
    from frame_metric_entry_tail_height159 import implementation_hashes as inherited
    result = inherited()
    p = Path(__file__)
    result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def definition():
    return {
        'schema': POLICY + '-definition',
        'physical_independent_dimension': N,
        'primary_variable_count': N + 2,
        'epsilon_exact': EPSILON_EXACT,
        'branch_mapping': copy.deepcopy(PROPOSAL_BRANCHES),
        'primary_epigraph': 'phi_sigma(e+de*p,f+df*p)<=fixed_target+rho',
        'primary_soft_functions_convex_in_independent_step': True,
        'old_primary_scalar_tangents_and_all_hard_box_norm_rows_retained': True,
        'maximum_inner_primary_LPs_per_outer_model': MAX_INNER_PRIMARY_LPS,
        'cut_gap_fraction_of_evaluated_model_gain_exact': GAP_GAIN_FRACTION_EXACT,
        'cut_absolute_floor_is_unchanged_metric_row_tolerance': True,
        'every_inner_LP_counts_in_original_shared_limit': True,
        'epigraph_auxiliary_is_repaired_upward_before_return': True,
        'returned_prediction_is_never_the_LP_cut_relaxation_slack': True,
        'unfinished_cut_model_may_return_only_a_declared_repaired_candidate': True,
        'no_interval_or_exact_nonlinear_optimization_certificate': True,
        'actual_geometry_and_complete_grid_acceptance_are_separate': True}


def _finite(value, shape=None, name='array'):
    result = np.asarray(value, dtype=float)
    if (shape is not None and result.shape != shape) or not np.all(np.isfinite(result)):
        raise ValueError('finite matching ' + name + ' required')
    return result


def _groups(value, count):
    result = np.asarray(value)
    if (result.shape != (count,) or result.dtype.kind not in 'iu'
            or np.any((result < 0) | (result > 1))):
        raise ValueError('original soft branch labels0/1 required')
    return result.astype(np.int64, copy=False)


def phi(e, f, groups, epsilon):
    e = _finite(e, name='metric e')
    f = _finite(f, e.shape, 'metric f')
    if e.ndim != 1 or not np.isfinite(epsilon) or epsilon <= 0:
        raise ValueError('one-dimensional values and positive epsilon required')
    groups = _groups(groups, len(e))
    sign = np.where(groups == 0, 1., -1.)
    radius = np.hypot(np.hypot(e, 2*f), float(epsilon))
    answer = .5*(sign*e + radius)
    if not np.all(np.isfinite(answer)):
        raise FloatingPointError('nonfinite regularized spectral value')
    return answer


def phi_gradient(e, f, groups, epsilon):
    e = _finite(e, name='metric e')
    f = _finite(f, e.shape, 'metric f')
    groups = _groups(groups, len(e))
    radius = np.hypot(np.hypot(e, 2*f), float(epsilon))
    if e.ndim != 1 or epsilon <= 0 or not np.all(np.isfinite(radius)):
        raise ValueError('finite regularized branch derivatives required')
    sign = np.where(groups == 0, 1., -1.)
    return .5*(sign + e/radius), 2*f/radius


def observable_parameter_jacobians(data):
    """True de/df in the already-built small virtual parameter axes."""
    U = _finite(data['Xs'], name='selected Xs')
    T = _finite(data['T'], U.shape, 'selected T')
    JU = _finite(data['jac_Xs'], name='selected dXs')
    JT = _finite(data['jac_T'], JU.shape, 'selected dT')
    if U.ndim != 2 or U.shape[1] != 3 or JU.ndim != 3 or JU.shape[:2] != U.shape:
        raise ValueError('selected vectors and common small derivative axes required')
    de = 2*np.einsum('ic,icn->in', U, JU)
    df = np.einsum('ic,icn->in', T, JU) + np.einsum('ic,icn->in', U, JT)
    return _finite(de), _finite(df)


class AffineSpectralModel:
    """Original selected159 rows plus separately bound, true soft de/df."""

    def __init__(self, primary, e, f, de, df, tags, cfg, *, observable_binding):
        self.primary = primary
        self.soft_positions = np.flatnonzero(np.asarray(primary.active_groups) < 2)
        count = len(self.soft_positions)
        self.e = _finite(e, (count,), 'selected soft e').copy()
        self.f = _finite(f, (count,), 'selected soft f').copy()
        self.de = _finite(de, (count, N), 'selected soft de159').copy()
        self.df = _finite(df, (count, N), 'selected soft df159').copy()
        self.groups = _groups(np.asarray(primary.active_groups)[self.soft_positions], count).copy()
        self.tags = copy.deepcopy(tags)
        self.target_exact = str(Q(cfg['fixed_metric_budget_exact']))
        self.target = float(Q(self.target_exact))
        self.epsilon = float(Q(cfg['metric_proposal_epsilon_exact']))
        self.outside = float(primary.information['rho_out'])
        self.rho0 = float(primary.information['initial_selected_and_constant_metric_slack'])
        if (len(tags) != count or self.target <= 0 or self.epsilon != float(Q(EPSILON_EXACT))
                or min(self.outside, self.rho0) < 0 or not np.isfinite(self.rho0)
                or np.asarray(primary.step_scale).shape != (N,)
                or np.asarray(primary.c).shape != (N+2,)
                or primary.upper[N] != np.inf
                or primary.c[N] != 1.):
            raise ValueError('unchanged original slack and159+2 mapped primary contract required')
        expected_tags = [primary.information['active_original_rows'][int(i)] for i in self.soft_positions]
        if self.tags != expected_tags:
            raise ValueError('soft observables changed original active grid/row order')
        self.base_phi = phi(self.e, self.f, self.groups, self.epsilon)
        pe, pf = phi_gradient(self.e, self.f, self.groups, self.epsilon)
        self.base_gradient = pe[:, None]*self.de + pf[:, None]*self.df
        old_values = np.asarray(primary.active_values)[self.soft_positions]
        old_J = np.asarray(primary.active_J)[self.soft_positions]
        value_error = float(np.max(abs((self.target-self.base_phi)-old_values), initial=0.))
        J_error = float(np.max(abs(self.base_gradient+old_J), initial=0.))
        tol = float(cfg['value_Jacobian_replay_relative_tolerance'])
        value_scale = max(1., float(np.max(abs(old_values), initial=0.)))
        J_scale = max(1., float(np.max(abs(old_J), initial=0.)))
        if value_error > tol*value_scale or J_error > tol*J_scale:
            raise ArithmeticError('true e/f chain does not reproduce the frozen scalar row/J')
        self.binding = {
            'schema': POLICY + '-observables',
            'external_current_cache_binding': copy.deepcopy(observable_binding),
            'soft_original_tags_sha256': digest(self.tags),
            'soft_positions_sha256': array_digest(self.soft_positions),
            'e_sha256': array_digest(self.e), 'f_sha256': array_digest(self.f),
            'de_sha256': array_digest(self.de), 'df_sha256': array_digest(self.df),
            'branch_labels_sha256': array_digest(self.groups),
            'base_value_chain_max_absolute_error': value_error,
            'base_J_chain_max_absolute_error': J_error,
            'chain_relative_tolerance': tol,
            'branch_reconstruction_never_divides_by_f': True}
        self.binding_sha256 = digest(self.binding)
        for arr in (self.e, self.f, self.de, self.df, self.groups, self.base_phi,
                    self.base_gradient, self.soft_positions):
            arr.setflags(write=False)
        inherited_signature = primary.information['radius_independent_model_sha256']
        primary.information['inherited_scalar_radius_independent_model_sha256'] = inherited_signature
        primary.information['affine_spectral_binding'] = copy.deepcopy(self.binding)
        primary.information['radius_independent_model_sha256'] = digest({
            'inherited_scalar_model_sha256': inherited_signature,
            'affine_spectral_observables_sha256': self.binding_sha256,
            'policy': definition()})
        primary.affine_spectral_model = self

    def evaluated(self, step):
        p = _finite(step, (N,), 'actual independent step')
        de = self.de@p
        df = self.df@p
        e, f = self.e+de, self.f+df
        values = phi(e, f, self.groups, self.epsilon)
        linear = self.base_phi+self.base_gradient@p
        slack = max(0., self.outside, float(np.max(values-self.target, initial=-np.inf)))
        old = max(0., self.outside, float(np.max(linear-self.target, initial=-np.inf)))
        return {'e': e, 'f': f, 'de_step': de, 'df_step': df,
                'phi': values, 'scalar_linear_phi': linear,
                'slack': float(slack), 'old_scalar_slack': float(old)}

    def slack(self, step):
        return self.evaluated(step)['slack']

    def cuts(self, step, soft_indices):
        p = _finite(step, (N,), 'cut point')
        selected = np.asarray(soft_indices)
        if (selected.ndim != 1 or selected.dtype.kind not in 'iu'
                or np.any(selected < 0) or np.any(selected >= len(self.e))):
            raise ValueError('cut indices inside the original soft subset required')
        selected = selected.astype(np.int64, copy=False)
        observed = self.evaluated(p)
        e, f = observed['e'][selected], observed['f'][selected]
        pe, pf = phi_gradient(e, f, self.groups[selected], self.epsilon)
        grad = pe[:, None]*self.de[selected]+pf[:, None]*self.df[selected]
        intercept = observed['phi'][selected]-grad@p
        A = np.zeros((len(selected), N+2))
        A[:, :N] = grad*np.asarray(self.primary.step_scale)[None, :]
        A[:, N] = -1.
        rhs = self.target-intercept
        if not np.all(np.isfinite(A)) or not np.all(np.isfinite(rhs)):
            raise FloatingPointError('nonfinite affine spectral supporting cut')
        record = {
            'soft_indices': selected.tolist(),
            'original_rows': [copy.deepcopy(self.tags[int(i)]) for i in selected],
            'cut_point_independent_array_sha256': array_digest(p),
            'A_sha256': array_digest(A), 'b_sha256': array_digest(rhs),
            'observable_binding_sha256': self.binding_sha256,
            'rows': len(selected),
            'contact_max_absolute_residual': float(np.max(
                abs(grad@p+intercept-observed['phi'][selected]), initial=0.))}
        return A, rhs, record

    def summary(self):
        return {'schema': POLICY + '-finite-primary',
                'soft_rows': len(self.e), 'independent_columns': N,
                'binding': copy.deepcopy(self.binding),
                'binding_sha256': self.binding_sha256,
                'rho_out': self.outside, 'initial_slack': self.rho0,
                'target_exact': self.target_exact,
                'epsilon_exact': EPSILON_EXACT}


def _cut_lp(base, rows, rhs, records):
    if not rows:
        result = copy.copy(base)
        result.information = copy.deepcopy(base.information)
    else:
        A = np.concatenate([base.A]+rows, axis=0)
        b = np.concatenate([base.b]+rhs)
        result = ArrayLP(A, b, base.c, base.lower, base.upper,
                         information=copy.deepcopy(base.information))
        # Exact same physical map, original active rows and geometry references.
        for key, value in base.__dict__.items():
            if key not in ('A', 'b', 'c', 'lower', 'upper', 'information'):
                setattr(result, key, value)
    result.information['affine_spectral_cut_rounds'] = copy.deepcopy(records)
    result.information['new_cut_row_count'] = sum(len(x) for x in rhs)
    return result


def _candidate(lp, step, report, model, cfg):
    p = _finite(step, (N,), 'returned physical step')
    rho = model.slack(p)
    h = float(report['normalized_step_norm'])
    old_rho = float(report['predicted_metric_slack'])
    auxiliary_rho = max(rho, old_rho)
    variables = np.r_[p/np.asarray(lp.step_scale), auxiliary_rho, h]
    residual = lp.residual(variables)
    if not all(np.isfinite([rho, h, residual['objective_evaluated']])):
        raise FloatingPointError('nonfinite repaired affine model candidate')
    maximum = max(residual['maximum_original_linear_row_violation'],
                  residual['maximum_original_linear_bound_violation'])
    if maximum > cfg['linear_model_residual_limit']:
        raise ArithmeticError('upward epigraph repair failed original mapped residual gate')
    raw_gap = rho-old_rho
    gain = model.rho0-rho
    tolerance = max(float(cfg['metric_row_tolerance']),
                    float(Q(GAP_GAIN_FRACTION_EXACT))*max(0., gain))
    return {
        'step': p.copy(), 'variables': variables,
        'rho': rho, 'repaired_rho_auxiliary': auxiliary_rho, 'norm_auxiliary': h,
        'inherited_report': copy.deepcopy(report),
        'objective': residual['objective_evaluated'],
        'raw_epigraph_gap': raw_gap,
        'nonnegative_reported_epigraph_gap': max(0., raw_gap),
        'gap_tolerance': tolerance,
        'gap_met': max(0., raw_gap) <= tolerance,
        'gain': gain, 'repaired_residual': residual}


def solve_affine_primary(primary, model, cfg, ledger, *, progress, wall,
                         remaining_seconds, solve_one=None):
    """At most three calls, all charged to the original caller's shared ledger.

    The optional solver is solely for the new labelled-array developer fixture.
    Production supplies None and calls the unchanged original HiGHS function.
    The progress dictionary is installed in the outer model before this call,
    so an exception/budget exit cannot erase already started inner calls.
    """
    if primary is not model.primary:
        raise ValueError('model belongs to a different original mapped LP')
    if not isinstance(progress, dict) or not callable(wall) or not callable(remaining_seconds):
        raise ValueError('explicit progress and original wall-budget callbacks required')
    solver = frozen_solve_primary if solve_one is None else solve_one
    if solve_one is not None and cfg.get('new_affine_array_fixture_only') is not True:
        raise ValueError('custom LP callback is restricted to the labelled new array fixture')
    progress.update(
        policy=POLICY, inner_LPs=[], cut_rounds=[],
        model=model.summary(), status='new-affine-primary-not-yet-solved',
        inner_call_count=0, best_candidate_inner_index=None,
        physical_values_or_Jacobians_inside_inner_solver=0,
        epigraph_status_is_floating_model_status_not_actual_feasibility=True)
    rows, rhs, records, seen = [], [], [], set()
    incumbent = None
    stop = None
    last_lp = primary
    for inner in range(MAX_INNER_PRIMARY_LPS):
        wall()
        if ledger['linear_program_invocation_count'] >= cfg['max_linear_models']:
            stop = 'original-shared-LP-budget-before-next-inner-call'
            break
        remaining = float(remaining_seconds())
        if not np.isfinite(remaining) or remaining <= 0:
            stop = 'original-shared-active-time-before-next-inner-call'
            break
        last_lp = _cut_lp(primary, rows, rhs, records)
        local = dict(cfg, linear_program_seconds=min(
            float(cfg['linear_program_seconds']), remaining))
        event = {
            'inner_index': inner,
            'shared_LP_ordinal': int(ledger['linear_program_invocation_count'])+1,
            'LP_rows': len(last_lp.b), 'LP_variables': len(last_lp.c),
            'LP_matrix_bytes': last_lp.A.nbytes,
            'supporting_cut_rows': sum(len(x) for x in rhs),
            'time_limit_seconds': local['linear_program_seconds'],
            'status': 'LP-call-started'}
        progress['inner_LPs'].append(event)
        # Charge before the actual call. A solver exception is still a started call.
        ledger['linear_program_invocation_count'] += 1
        ledger['primary_LP_invocation_count'] += 1
        progress['inner_call_count'] += 1
        started = time.monotonic()
        try:
            p, reported = solver(last_lp, local)
        except Exception as error:
            event.update(status='LP-call-raised',
                         elapsed_seconds=time.monotonic()-started,
                         error={'type': type(error).__name__, 'message': str(error)})
            raise
        event.update(status='LP-returned', elapsed_seconds=time.monotonic()-started,
                     inherited_scalar_LP_report=copy.deepcopy(reported))
        if p is None:
            stop = 'original-LP-or-residual-gate-failed'
            event['status'] = stop
            break
        current = _candidate(last_lp, p, reported, model, cfg)
        event.update(
            status='evaluated-affine-candidate',
            evaluated_affine_slack=current['rho'],
            inherited_LP_relaxation_slack=float(reported['predicted_metric_slack']),
            raw_epigraph_gap=current['raw_epigraph_gap'],
            nonnegative_reported_epigraph_gap=current['nonnegative_reported_epigraph_gap'],
            gap_tolerance=current['gap_tolerance'],
            gap_met=current['gap_met'],
            repaired_objective=current['objective'],
            repaired_residual=copy.deepcopy(current['repaired_residual']),
            evaluated_model_improvement=current['gain'])
        if incumbent is None or current['objective'] < incumbent['objective']:
            incumbent = current
            incumbent['inner_index'] = inner
            progress['best_candidate_inner_index'] = inner
        if current['gap_met']:
            stop = 'evaluated-affine-epigraph-gap-met'
            break
        if inner+1 >= MAX_INNER_PRIMARY_LPS:
            stop = 'declared-three-inner-primary-LP-cap'
            break
        if ledger['linear_program_invocation_count'] >= cfg['max_linear_models']:
            stop = 'original-shared-LP-budget-after-inner-call'
            break
        evaluated = model.evaluated(p)
        violation = evaluated['phi']-model.target-float(reported['predicted_metric_slack'])
        selected = np.flatnonzero(violation > current['gap_tolerance'])
        if not len(selected):
            stop = 'no-distinct-violated-original-soft-row'
            break
        cut_A, cut_b, record = model.cuts(p, selected)
        keep = []
        for i in range(len(selected)):
            key = array_digest(np.r_[cut_A[i], cut_b[i]])
            if key not in seen:
                keep.append(i)
                seen.add(key)
        if not keep:
            stop = 'all-violated-supporting-cuts-already-present'
            break
        keep = np.asarray(keep, np.int64)
        if len(keep) != len(selected):
            cut_A, cut_b, record = model.cuts(p, selected[keep])
        rows.append(cut_A)
        rhs.append(cut_b)
        records.append(record)
        progress['cut_rounds'] = copy.deepcopy(records)
    if stop is None:
        stop = 'declared-inner-loop-ended'
    progress['status'] = stop
    progress['total_new_cut_rows'] = sum(len(x) for x in rhs)
    progress['all_started_inner_LPs_charged_to_original_ledger'] = True
    if incumbent is None:
        progress.update(returned_candidate=False,
                        proposal_rejected_before_geometry='no_original_gate_qualified_repaired_candidate')
        return None, progress
    # Earlier incumbents also obey every later cut when rho is their full (11).
    final_lp = _cut_lp(primary, rows, rhs, records)
    final_residual = final_lp.residual(incumbent['variables'])
    if max(final_residual['maximum_original_linear_row_violation'],
           final_residual['maximum_original_linear_bound_violation']) > cfg['linear_model_residual_limit']:
        raise ArithmeticError('best repaired incumbent failed a later valid supporting cut')
    report = progress
    source_report = incumbent['inherited_report']
    physical_cost = copy.deepcopy(source_report.get('primary_step_cost_diagnostic', {}))
    physical_cost.update(
        inherited_cut_LP_objective=physical_cost.get('returned_weighted_objective'),
        inherited_cut_LP_slack=physical_cost.get('returned_predicted_metric_slack'),
        returned_weighted_objective=incumbent['objective'],
        returned_predicted_metric_slack=incumbent['rho'],
        predicted_metric_slack_improvement=incumbent['gain'],
        repaired_rho_auxiliary=incumbent['repaired_rho_auxiliary'],
        prediction_uses_evaluated_affine_spectral_norm=True)
    projection = copy.deepcopy(source_report.get('projection', {}))
    legacy_label = projection.pop('original163_geometry_J_still_computed_then159_independent_columns_returned', None)
    projection.update(
        inherited_frozen_projection_label_not_actual_new_J_path=legacy_label,
        original163_geometry_J_still_computed_then159_independent_columns_returned=False,
        selected_J_and_true_de_df_contracted_before_radial_expansion=True)
    report.update(
        returned_candidate=bool(incumbent['gain'] > cfg['linear_model_improvement_floor']),
        returned_inner_index=incumbent['inner_index'],
        returned_epigraph_gap_met=incumbent['gap_met'],
        returned_inexact_cut_model=not incumbent['gap_met'],
        predicted_metric_slack=incumbent['rho'],
        predicted_slack_from_rows_and_outside=incumbent['rho'],
        predicted_slack_improvement=incumbent['gain'],
        normalized_step_norm=incumbent['norm_auxiliary'],
        returned_repaired_objective=incumbent['objective'],
        repaired_rho_auxiliary=incumbent['repaired_rho_auxiliary'],
        returned_LP_status=source_report.get('status'),
        returned_LP_success=source_report.get('success'),
        primary_step_cost_diagnostic=physical_cost,
        projection=projection,
        maximum_linear_row_violation=final_residual['maximum_original_linear_row_violation'],
        maximum_linear_bound_violation=final_residual['maximum_original_linear_bound_violation'],
        exact_convex_optimality_claim=False,
        returned_prediction_source='all selected original affine-e/f spectral norms plus unchanged outside floor')
    if not report['returned_candidate']:
        report['proposal_rejected_before_geometry'] = 'no-evaluated-affine-model-improvement-above-original-floor'
        return None, report
    return incumbent['step'], report


def _extreme_record(values, tags, maximum):
    if not len(values):
        return None
    i = int(np.argmax(values) if maximum else np.argmin(values))
    return {'value': float(values[i]), 'soft_index': i, 'original_row': copy.deepcopy(tags[i])}


def norm_curvature_diagnostic(e, f, de, df, epsilon):
    """Keep both (8) and (9); a rounded zero denominator disables (9).

    These arrays are diagnostics, not a replacement for the complete norm
    model or an assertion of exact nonnegativity of floating differences.
    """
    e = _finite(e, name='base e for norm remainder')
    f = _finite(f, e.shape, 'base f for norm remainder')
    de = _finite(de, e.shape, 'e increment for norm remainder')
    df = _finite(df, e.shape, 'f increment for norm remainder')
    if e.ndim != 1 or not np.isfinite(epsilon) or epsilon <= 0:
        raise ValueError('finite positive smoothing and one-dimensional norm rows required')
    r0 = np.hypot(np.hypot(e, 2*f), epsilon)
    r1 = np.hypot(np.hypot(e+de, 2*(f+df)), epsilon)
    z = (e/r0)*de+(2*f/r0)*(2*df)
    direct = .5*(r1-r0-z)
    numerator = de*de+4*df*df-z*z
    denominator = 2*(r1+r0+z)
    usable = np.isfinite(numerator) & np.isfinite(denominator) & (denominator > 0)
    stable = np.zeros_like(direct)
    with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
        stable[usable] = numerator[usable]/denominator[usable]
    usable &= np.isfinite(stable)
    finite_direct = np.isfinite(direct)
    def extrema(values):
        return None if not len(values) else {'minimum': float(np.min(values)), 'maximum': float(np.max(values))}
    both = usable & finite_direct
    return {
        'rows': len(e), 'direct_finite_rows': int(np.sum(finite_direct)),
        'direct_remainder_range': extrema(direct[finite_direct]),
        'direct_negative_floating_rows': int(np.sum(direct[finite_direct] < 0)),
        'stable_identity_applicable_rows': int(np.sum(usable)),
        'stable_identity_unavailable_rows': int(np.sum(~usable)),
        'stable_identity_requires_positive_finite_rounded_denominator': True,
        'stable_remainder_range_when_applicable': extrema(stable[usable]),
        'stable_negative_floating_rows': int(np.sum(stable[usable] < 0)),
        'stable_numerator_negative_rows': int(np.sum(numerator[np.isfinite(numerator)] < 0)),
        'direct_stable_max_absolute_difference_where_both_available':
            None if not np.any(both) else float(np.max(abs(direct[both]-stable[both]))),
        'no_negative_remainder_or_denominator_clipped_to_zero': True,
        'not_an_interval_nonnegativity_certificate': True}


def error_decomposition(model, step, actual_e, actual_f, *,
                        complete_smooth_slack, complete_true_slack,
                        complete_two_grid_available, observed_grid_labels):
    """Read actual cached e/f only; no geometry, J, LP or inferred fine value."""
    if complete_two_grid_available is not True:
        raise ValueError('joint maximum decomposition requires both actual complete grids')
    actual_e = _finite(actual_e, model.e.shape, 'same-ID actual e')
    actual_f = _finite(actual_f, model.f.shape, 'same-ID actual f')
    evaluated = model.evaluated(step)
    actual = phi(actual_e, actual_f, model.groups, model.epsilon)
    spectral = evaluated['phi']-evaluated['scalar_linear_phi']
    geometry = actual-evaluated['phi']
    total = actual-evaluated['scalar_linear_phi']
    identity = total-(spectral+geometry)
    rho_L = evaluated['old_scalar_slack']
    rho_M = evaluated['slack']
    rho_A = max(0., model.outside, float(np.max(actual-model.target, initial=-np.inf)))
    rho_F, rho_T = float(complete_smooth_slack), float(complete_true_slack)
    if not all(np.isfinite([rho_F, rho_T])) or min(rho_F, rho_T) < 0:
        raise ValueError('finite already-evaluated full-grid slacks required')
    pieces = [rho_M-rho_L, rho_A-rho_M, rho_F-rho_A, rho_T-rho_F]
    return {
        'schema': POLICY + '-actual-original-row-error',
        'observable_binding_sha256': model.binding_sha256,
        'observed_grid_labels': list(observed_grid_labels),
        'complete_two_grid_available': bool(complete_two_grid_available),
        'no_extra_geometry_J_LP_or_value_call': True,
        'same_base_original_row_order_before_pool_learning': True,
        'row_identity_max_absolute_error': float(np.max(abs(identity), initial=0.)),
        'norm_curvature_direct_and_stable_diagnostic': norm_curvature_diagnostic(
            model.e, model.f, evaluated['de_step'], evaluated['df_step'], model.epsilon),
        'row_spectral_curvature': {
            'minimum': _extreme_record(spectral, model.tags, False),
            'maximum': _extreme_record(spectral, model.tags, True),
            'raw_negative_floating_count': int(np.sum(spectral < 0)),
            'raw_negative_values_not_clipped': True},
        'row_actual_ef_nonlinearity': {
            'minimum': _extreme_record(geometry, model.tags, False),
            'maximum': _extreme_record(geometry, model.tags, True),
            'sign_not_constrained': True},
        'selected_scalar_linear_slack': rho_L,
        'selected_affine_ef_spectral_slack': rho_M,
        'selected_actual_smooth_slack': rho_A,
        'complete_actual_smooth_slack': rho_F,
        'complete_actual_true_slack': rho_T,
        'maximum_slack_difference_terms': {
            'selected_spectral_curvature': pieces[0],
            'selected_actual_ef_nonlinearity': pieces[1],
            'omitted_original_grid_rows': pieces[2],
            'smooth_to_true_bias': pieces[3]},
        'global_identity_absolute_error': abs((rho_T-rho_L)-sum(pieces)),
        'smoothing_bias_upper_bound': model.epsilon/2,
        'row_extrema_are_not_substituted_for_differences_of_maxima': True}


def partial_row_error(model, step, soft_indices, actual_e, actual_f, grid_label):
    """Only row-wise identity (14) when the other complete grid was not evaluated."""
    ix = np.asarray(soft_indices)
    if (ix.ndim != 1 or ix.dtype.kind not in 'iu' or np.any(ix < 0)
            or np.any(ix >= len(model.e))):
        raise ValueError('explicit observed subset of frozen soft IDs required')
    ix = ix.astype(np.int64, copy=False)
    e = _finite(actual_e, (len(ix),), 'actually observed e subset')
    f = _finite(actual_f, (len(ix),), 'actually observed f subset')
    evaluated = model.evaluated(step)
    true = phi(e, f, model.groups[ix], model.epsilon)
    spectral = evaluated['phi'][ix]-evaluated['scalar_linear_phi'][ix]
    geometric = true-evaluated['phi'][ix]
    total = true-evaluated['scalar_linear_phi'][ix]
    tags = [model.tags[int(i)] for i in ix]
    return {'schema': POLICY+'-partial-observed-row-error',
            'observed_grid': str(grid_label), 'complete_two_grid_available': False,
            'rows': len(ix), 'no_missing_fine_values_inferred': True,
            'global_maximum_decomposition_available': False,
            'global_maximum_reason': 'the other current physical grid was not evaluated',
            'spectral_curvature_minimum': _extreme_record(spectral, tags, False),
            'spectral_curvature_maximum': _extreme_record(spectral, tags, True),
            'actual_ef_nonlinearity_minimum': _extreme_record(geometric, tags, False),
            'actual_ef_nonlinearity_maximum': _extreme_record(geometric, tags, True),
            'row_identity_max_absolute_error': float(np.max(abs(total-spectral-geometric), initial=0.)),
            'norm_curvature_direct_and_stable_diagnostic': norm_curvature_diagnostic(
                model.e[ix], model.f[ix], evaluated['de_step'][ix], evaluated['df_step'][ix], model.epsilon),
            'no_extra_geometry_J_LP_or_value_call': True}


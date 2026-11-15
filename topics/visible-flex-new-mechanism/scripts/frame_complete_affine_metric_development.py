#!/usr/bin/env python3
"""New public artificial checks for complete-grid affine directional separation.

No old developer entry point, saved research point, scientific optimizer or
local execution is part of this file. Frozen builders supply only a small
original-family fixture and an explicitly labelled array LP stub.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import resource
import time
from unittest.mock import patch

import numpy as np

from frame_collar_bvp import periodic_operator, target_frame
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import ArrayLP, RationalRowGrid
from frame_entry_single_q import SingleQGrid
from frame_selected_row_radial_jacobian import array_hash
from frame_selected_row_metric_observables import SelectedMetricObservables
from frame_selected_row_radial_jacobian_development import _setup
from frame_metric_affine_spectral_development import _stub_solver
from frame_metric_affine_spectral_model import (
    N, EPSILON_EXACT, AffineSpectralModel, phi, phi_gradient, solve_affine_primary)
from frame_metric_height159_affine_spectral import (
    configuration as selected_configuration, AffineSpectralHeight159Objective)
from frame_complete_affine_metric_oracle import (
    POLICY, GRID_BRANCHES, CompleteDirectionalMetricOracle, CompleteGridAffineModel,
    direction_frame_jets)
from frame_metric_height159_complete_affine import (
    configuration, CompleteAffineHeight159Objective, implementation_hashes as inherited)
from frame_metric_height159_soc_hold import require_public_research_environment

SCHEMA = 'complete-two-grid-affine-new-artificial-development-v1'


def implementation_hashes():
    result = inherited()
    import frame_metric_affine_spectral_development as arrays
    import frame_selected_row_radial_jacobian_development as small
    for module in (arrays, small):
        p = Path(module.__file__)
        result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    p = Path(__file__)
    result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def _relative(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    if a.shape != b.shape:
        return float('inf')
    return float(np.max(abs(a-b), initial=0.))/max(
        1., float(np.max(abs(b), initial=0.)))


def _reject(callback):
    try:
        callback()
    except (ValueError, ArithmeticError, KeyError, TypeError):
        return True
    return False


def original_family_direction_checks():
    cases = []
    wrong_context_rejected = []
    for side in (1, -1):
        old, reference, field, state, base, oldcfg, nodes, radial = _setup(side)
        cfg = configuration(selected_configuration(oldcfg))
        evaluator = SelectedMetricObservables(field, cfg)
        ordinary, references, bounds, grids = {}, {}, {}, {}
        for label, nt in (('coarse', 8), ('fine', 16)):
            theta = np.arange(nt)*2*np.pi/nt
            ordinary[label] = field.geometry(state, radial, theta, 2)
            references[label] = field.geometry(
                state, radial, theta, 2, jacobian=True, full_two_jet_jacobian=True)
            bounds[label] = evaluator.bind_ordinary(
                state, radial, theta, ordinary[label], owner='new-artificial-current-cache')
            grids[label] = RationalRowGrid(label, nodes, nt)
        oracle = CompleteDirectionalMetricOracle(
            evaluator, state, bounds, grids, cfg, wall=lambda: None)
        mixed = np.cos(np.arange(N)+.41)
        mixed[153] = .91
        mixed[154:] = [.23, -.19, .17, .29, -.11]
        mixed /= np.linalg.norm(mixed)
        height = np.zeros(N)
        height[154:] = [1., -.5, .25, .3, -.2]
        height /= np.linalg.norm(height)
        for label_direction, direction in (('mixed-all-families', mixed), ('height-only', height)):
            # The independent reference is the small original full geometry J;
            # this reference tensor is never requested by production.
            expected = []
            max_error = 0.
            frame_errors = {}
            for label, group in GRID_BRANCHES:
                g = references[label]
                du = np.einsum('rtcn,n->rtc', g['jac_Xs'], direction)
                dt = np.einsum('rtcn,n->rtc', g['jac_T'], direction)
                de = 2*np.sum(g['Xs']*du, axis=2)
                df = np.sum(g['T']*du+g['Xs']*dt, axis=2)
                e = np.sum(g['Xs']**2, axis=2)-1.
                f = np.sum(g['Xs']*g['T'], axis=2)
                values = phi((e+de).reshape(-1), (f+df).reshape(-1),
                             np.full(e.size, group, np.int64), float(Q(EPSILON_EXACT)))
                expected.append((float(np.max(values)), int(np.argmax(values)),
                                 e, f, de, df))
            with patch.object(field, 'geometry', side_effect=AssertionError('no ordinary geometry inside new oracle')), \
                 patch.object(old, 'geometry', side_effect=AssertionError('no old163 geometry inside new oracle')), \
                 patch.object(SingleQGrid, 'basis_jacobian', side_effect=AssertionError('no full parameter basis')):
                got = oracle.evaluate(direction)
                repeated = oracle.evaluate(direction.copy())
                for label in ('coarse', 'fine'):
                    th = bounds[label]['theta']
                    grid = evaluator.single.source.grid_for(radial, th)
                    fields = grid.fields(field.coordinates.reference_evaluation_state(state))
                    fields['_theta'] = th[None, :]
                    frame = target_frame(fields)
                    dT, dTs = direction_frame_jets(
                        evaluator, grid, fields, frame, direction)
                    a = ordinary[label]['metric']['a'][:, None, None]
                    ap = ordinary[label]['metric']['a_s'][:, None, None]
                    dU = ap*periodic_operator(dT, -1)+a*periodic_operator(dTs, -1)
                    dU[:, :, 2] += (field.null_basis.values(radial)@direction[154:])[:, None]
                    full = references[label]
                    refT = np.einsum('rtcn,n->rtc', full['jac_T'], direction)
                    refU = np.einsum('rtcn,n->rtc', full['jac_Xs'], direction)
                    refST = np.einsum('rtcn,n->rtc', full['jac_Xst'], direction)
                    refTs = (refST-ap*refT)/a
                    frame_errors[label] = {
                        'T': _relative(dT, refT), 'Ts': _relative(dTs, refTs),
                        'Xs': _relative(dU, refU)}
                # A newly requested original metric row uses only the old
                # selected derivative API, with the same nonzero null height.
                row = oracle.original_row('fine', grids['fine'].nt+1)
            for i, (label, group) in enumerate(GRID_BRANCHES):
                exp = expected[i]
                arow = got['attainers'][i]
                point = arow['original_point_flat_index']
                ri, ti = divmod(point, grids[label].nt)
                max_error = max(max_error, abs(float(got['phi'][i])-exp[0]),
                                abs(arow['de_step']-float(exp[4][ri, ti])),
                                abs(arow['df_step']-float(exp[5][ri, ti])))
            full = references['fine']
            refde = 2*np.einsum('c,cn->n', full['Xs'][1, 1], full['jac_Xs'][1, 1])
            refdf = (np.einsum('c,cn->n', full['T'][1, 1], full['jac_Xs'][1, 1])
                     +np.einsum('c,cn->n', full['Xs'][1, 1], full['jac_T'][1, 1]))
            row_error = max(_relative(row['de'], refde), _relative(row['df'], refdf))
            cases.append({
                'side': side, 'direction': label_direction,
                'full_grid_maximum_and_attainer_direction_error': max_error,
                'all_point_analytic_geometry_direction_errors': frame_errors,
                'single_new_attainer_row_de_df_error': row_error,
                'cache_returned_identical_result_object': got is repeated,
                'coverage': got['full_grid_coverage'],
                'current_height_null_coordinates_nonzero': bool(np.any(state[154:])),
                'passes': bool(max_error < 2e-10 and row_error < 2e-10
                    and max(v for errors in frame_errors.values() for v in errors.values()) < 2e-10
                    and got is repeated)})
        baseline = oracle.evaluate(np.zeros(N))
        baseline_errors = []
        for i, (label, group) in enumerate(GRID_BRANCHES):
            g = ordinary[label]
            e = np.sum(g['Xs']**2, axis=2)-1.
            f = np.sum(g['Xs']*g['T'], axis=2)
            values = phi(e.reshape(-1), f.reshape(-1),
                         np.full(e.size, group, np.int64), float(Q(EPSILON_EXACT)))
            baseline_errors.append(abs(float(baseline['phi'][i])-float(np.max(values))))
        bad = dict(bounds)
        bad['fine'] = dict(bounds['fine'], state=np.asarray(state)+1e-6)
        wrong_context_rejected.append(_reject(lambda: CompleteDirectionalMetricOracle(
            evaluator, state, bad, grids, cfg, wall=lambda: None)))
        wrong_context_rejected.append(max(baseline_errors) == 0.)
        wrong_context_rejected.append(
            oracle.statistics['ordinary_geometry_calls_inside_oracle'] == 0 and
            oracle.statistics['full_angle_159_or163_parameter_tensors_formed'] == 0)
    checks = {
        'true_full_direction_matches_original_small_family_for_both_sides_and_both_grids': all(x['passes'] for x in cases),
        'mixed_u_v_Q_null_and_pure_height_directions_are_both_checked': len(cases) == 4,
        'all_point_T_Ts_Xs_not_only_winning_nodes_are_compared': all(
            set(x['all_point_analytic_geometry_direction_errors']) == {'coarse', 'fine'} for x in cases),
        'complete_coverage_and_exact_step_cache_are_checked': all(
            x['coverage']['fine'] == 2*x['coverage']['coarse'] and
            x['cache_returned_identical_result_object'] for x in cases),
        'current_nonzero_exact_null_height_is_used': all(x['current_height_null_coordinates_nonzero'] for x in cases),
        'mismatched_center_rejected_and_zero_step_uses_original_complete_values': all(wrong_context_rejected)}
    return {
        'checks': {k: bool(v) for k, v in checks.items()}, 'all_passed': bool(all(checks.values())),
        'cases': cases, 'new_artificial_original_full_J_references': 4,
        'production_full_parameter_J_path_used': False,
        'old_developer_suites_or_actual_research_inputs': 0,
        'actual_optimizer_LPs': 0}


class ArrayWholeGrid:
    """Only the new labelled mathematical arrays, never a geometry surrogate."""
    def __init__(self, cfg):
        self.cfg = cfg
        self.grids = {label: RationalRowGrid(label, ['0', '9/10'], 4)
                      for label in ('coarse', 'fine')}
        self.data = {}
        for label in ('coarse', 'fine'):
            e, f = np.full(8, .4), np.full(8, .1)
            de, df = np.zeros((8, N)), np.zeros((8, N))
            de[:, 0] = -1.
            df[:, 1] = 1.
            df[1 if label == 'coarse' else 3, 1] = 2.
            df[2 if label == 'coarse' else 4, 1] = -2.
            self.data[label] = (e, f, de, df)
        self.binding = {'schema': 'new-labelled-complete-max-array-fixture-only',
                        'grids': {k: g.definition for k, g in self.grids.items()}}
        self.binding_sha256 = digest(self.binding)
        self.statistics = {'new_full_direction_evaluations': 0}
        self.phase = 'primary-inner'
        self.row_calls = []
        zero = self.evaluate(np.zeros(N))
        self.base_maxima = zero['phi']
        self.base_slack = max(0., float(np.max(self.base_maxima))-.26)

    def evaluate(self, p):
        self.statistics['new_full_direction_evaluations'] += 1
        maxima, rows = [], []
        for label, group in GRID_BRANCHES:
            e, f, de, df = self.data[label]
            d, v = de@p, df@p
            E, F = e+d, f+v
            values = phi(E, F, np.full(8, group, np.int64), float(Q(EPSILON_EXACT)))
            i = int(np.argmax(values))
            maxima.append(float(values[i]))
            rows.append({
                'original_row': self.grids[label].coordinate(group*8+i),
                'original_point_flat_index': i, 'radial_index': i//4, 'theta_index': i % 4,
                'phi': float(values[i]), 'base_e': float(e[i]), 'base_f': float(f[i]),
                'de_step': float(d[i]), 'df_step': float(v[i]),
                'affine_e': float(E[i]), 'affine_f': float(F[i])})
        return {'phi': np.array(maxima), 'attainers': rows,
                'center_binding_sha256': self.binding_sha256,
                'direction_sha256': array_hash(p)}

    def original_row(self, label, flat):
        self.row_calls.append((label, int(flat)))
        e, f, de, df = self.data[label]
        i = int(flat) % 8
        return {'e': float(e[i]), 'f': float(f[i]), 'de': de[i], 'df': df[i],
                'source': 'new-labelled-array-original-row',
                'selected_observable_binding_sha256': self.binding_sha256}

    def set_post_primary_phase(self):
        self.phase = 'actual-total-step-prediction'


def _complete_array_fixture():
    cfg = {
        'fixed_metric_budget_exact': '13/50', 'metric_proposal_epsilon_exact': EPSILON_EXACT,
        'value_Jacobian_replay_relative_tolerance': 5e-12,
        'metric_row_tolerance': 1e-9, 'linear_model_residual_limit': 1e-7,
        'linear_model_improvement_floor': 1e-10, 'linear_program_seconds': 10.,
        'max_linear_models': 12, 'max_seconds': 120.,
        'new_affine_array_fixture_only': True}
    oracle = ArrayWholeGrid(cfg)
    groups = np.array([0, 1], np.int64)
    e, f = np.full(2, .4), np.full(2, .1)
    de, df = np.zeros((2, N)), np.zeros((2, N))
    de[:, 0] = -1.
    df[:, 1] = 1.
    pe, pf = phi_gradient(e, f, groups, float(Q(EPSILON_EXACT)))
    gradient = pe[:, None]*de+pf[:, None]*df
    values = np.r_[.26-phi(e, f, groups, float(Q(EPSILON_EXACT))), 1.]
    J = np.vstack([-gradient, np.zeros(N)])
    A = np.zeros((3+2*N, N+2))
    A[:3, :N] = -J
    A[:2, N] = -1.
    A[3:3+N, :N] = np.eye(N)
    A[3+N:, :N] = -np.eye(N)
    A[3:, -1] = -1.
    b = np.r_[values, np.zeros(2*N)]
    c = np.r_[np.zeros(N), 1., .001]
    lo, hi = np.r_[-np.ones(N), 0., 0.], np.r_[np.ones(N), np.inf, 1.]
    tags = [oracle.grids['coarse'].coordinate(0), oracle.grids['fine'].coordinate(8),
            oracle.grids['coarse'].coordinate(16)]
    primary = ArrayLP(A, b, c, lo, hi, information={
        'rho_out': 0., 'initial_selected_and_constant_metric_slack': max(0., float(np.max(-values[:2]))),
        'active_original_rows': tags, 'radius_independent_model_sha256': digest({'new_complete_array_only': True}),
        'new_complete_oracle_array_fixture_only': True})
    primary.active_values, primary.active_J = values, J
    primary.active_groups = np.array([0, 1, 2], np.int64)
    primary.step_scale, primary.state = np.ones(N), np.zeros(N)
    selected = AffineSpectralModel(primary, e, f, de, df, tags[:2], cfg,
        observable_binding={'new_complete_array_fixture_selected_rows': True})
    model = CompleteGridAffineModel(selected, oracle, artificial_array_fixture_only=True)
    return primary, selected, model, cfg, oracle


def complete_maximum_and_solver_checks():
    primary, selected, model, cfg, oracle = _complete_array_fixture()
    p = np.zeros(N)
    p[:2] = [.2, .03]
    observed = model.evaluated(p)
    indices = np.arange(model.selected_count, model.selected_count+4)
    A, b, cuts = model.cuts(p, indices)
    q = np.zeros(N)
    q[:2] = [.15, -.04]
    qobs = oracle.evaluate(q)
    vector = np.r_[q, 0., float(np.max(abs(q)))]
    supporting = np.max(A@vector-b-(qobs['phi']-.26)) <= 2e-13
    zero = np.zeros(N)
    A0, b0, info0 = model.cuts(zero, [0, model.selected_count])
    same_cut = np.array_equal(A0[0], A0[1]) and b0[0] == b0[1]
    swap = oracle.evaluate(q)['attainers'][0]['original_point_flat_index'] != (
        oracle.evaluate(p)['attainers'][0]['original_point_flat_index'])
    ledger = {'linear_program_invocation_count': 0, 'primary_LP_invocation_count': 0}
    progress, calls = {}, None
    stub, calls = _stub_solver(p)
    got, report = solve_affine_primary(
        primary, model, cfg, ledger, progress=progress, wall=lambda: None,
        remaining_seconds=lambda: 120., solve_one=stub)
    primary2, selected2, model2, cfg2, oracle2 = _complete_array_fixture()
    l2 = {'linear_program_invocation_count': 11, 'primary_LP_invocation_count': 0}
    stub2, calls2 = _stub_solver(p)
    got2, r2 = solve_affine_primary(
        primary2, model2, cfg2, l2, progress={}, wall=lambda: None,
        remaining_seconds=lambda: 120., solve_one=stub2)
    contact = np.r_[p, model.slack(p), float(np.max(abs(p)))]
    Aq, bq, _ = model.cuts(q, indices)
    early_survives = np.max(Aq@contact-bq) < 2e-13
    full_rows = report['inner_LPs'][-1]['supporting_cut_rows']
    checks = {
        'four_maxima_cover_original_rows_missing_from_selected_model': bool(
            model.slack(p)-selected.slack(p) > 1e-3
            and len(observed['phi']) == len(selected.e)+4),
        'attainers_use_real_original_IDs_and_change_with_direction': bool(
            swap and cuts['original_rows'][0]['flat_row_id'] % 8 == 1),
        'all_four_supports_are_contact_cuts_and_global_underestimators': bool(
            supporting and cuts['contact_max_absolute_residual'] < 2e-13),
        'same_existing_original_row_reuses_identical_frozen_cut_bytes': bool(same_cut),
        'original_shared_inner_solver_consumes_only_two_new_stub_LPs': bool(
            len(calls) == 2 and ledger['linear_program_invocation_count'] == 2
            and ledger['primary_LP_invocation_count'] == 2
            and np.array_equal(got, p) and report['returned_epigraph_gap_met']
            and full_rows > 0),
        'prediction_is_full_grid_value_not_LP_relaxation_or_old_selected_value': bool(
            abs(report['predicted_metric_slack']-model.slack(p)) < 2e-13
            and report['predicted_metric_slack'] > selected.slack(p)+1e-3),
        'last_original_LP_budget_keeps_only_honest_complete_repaired_candidate': bool(
            len(calls2) == 1 and l2['linear_program_invocation_count'] == 12
            and r2['returned_inexact_cut_model']
            and abs(r2['repaired_rho_auxiliary']-model2.slack(got2)) < 2e-13),
        'earlier_full_norm_repaired_incumbent_obeys_later_attainer_cuts': bool(early_survives),
        'fake_full_grid_adapter_is_restricted_to_explicit_new_array_fixture': _reject(
            lambda: CompleteGridAffineModel(selected, oracle)),
        'four_maximum_indices_outside_declared_protocol_are_rejected': _reject(
            lambda: model.cuts(p, [model.selected_count+4]))}
    return {
        'checks': {k: bool(v) for k, v in checks.items()}, 'all_passed': bool(all(checks.values())),
        'new_labelled_stub_LP_calls': len(calls)+len(calls2),
        'actual_HiGHS_or_scientific_LPs': 0,
        'full_model_slack': model.slack(p), 'old_selected_slack': selected.slack(p),
        'inner_report': report, 'original_real_learning_pool_mutations': 0}


def error_extension_checks():
    primary, selected, model, cfg, oracle = _complete_array_fixture()
    p = np.zeros(N)
    p[:2] = [.2, .03]
    S, M = selected.slack(p), model.slack(p)
    A, F, T = S+.002, M+.004, M+.004-1e-12
    base = {
        'schema': 'labelled-old-selected-error',
        'no_extra_geometry_J_LP_or_value_call': True,
        'complete_two_grid_available': True,
        'selected_affine_ef_spectral_slack': S,
        'selected_actual_smooth_slack': A,
        'complete_actual_smooth_slack': F,
        'complete_actual_true_slack': T}
    instance = object.__new__(CompleteAffineHeight159Objective)
    with patch.object(AffineSpectralHeight159Objective, 'actual_metric_error', return_value=base):
        result = instance.actual_metric_error(model, p, fine_present=True)
    with patch.object(AffineSpectralHeight159Objective, 'actual_metric_error', return_value={
            'schema': 'labelled-partial', 'complete_two_grid_available': False}):
        partial = instance.actual_metric_error(model, p, fine_present=False)
    terms = result['complete_model_difference_terms']
    checks = {
        'old_selected_error_fields_are_preserved_without_reindexing_as_four_maxima': bool(
            result['selected_affine_ef_spectral_slack'] == S
            and result['inherited_selected_error_schema'] == base['schema']),
        'full_coverage_and_full_actual_nonlinearity_are_separate': bool(
            abs(terms['full_affine_minus_original_selected_affine']-(M-S)) < 2e-13
            and abs(terms['complete_actual_smooth_minus_complete_affine']-.004) < 2e-13),
        'both_new_difference_identities_hold_without_clipping_bias': bool(
            terms['two_term_total_identity_absolute_error'] < 2e-13
            and terms['old_terms_to_full_identity_absolute_error'] < 2e-13
            and terms['complete_true_minus_complete_actual_smooth'] < 0),
        'coarse_only_actual_does_not_infer_missing_complete_actual_values': bool(
            partial['complete_actual_difference_terms_not_inferred_from_missing_fine']
            and 'complete_model_difference_terms' not in partial),
        'post_primary_directional_cost_is_labelled_separately': bool(
            oracle.phase == 'actual-total-step-prediction'
            and result['new_analytic_directional_evaluations_for_full_prediction'] == 1)}
    return {'checks': {k: bool(v) for k, v in checks.items()},
            'all_passed': bool(all(checks.values())),
            'new_fixture_has_no_geometry_or_optimizer_calls': True}


def run_development():
    require_public_research_environment()
    started = time.monotonic()
    groups = []
    for name, callback in (
            ('complete-original-grid-direction', original_family_direction_checks),
            ('four-convex-maxima-and-frozen-inner-protocol', complete_maximum_and_solver_checks),
            ('complete-versus-selected-actual-errors', error_extension_checks)):
        tick = time.monotonic()
        try:
            result = callback()
        except Exception as error:
            part = {'group': name, 'status': 'raised',
                    'elapsed_seconds': time.monotonic()-tick,
                    'error': {'type': type(error).__name__, 'message': str(error)}}
            print('DEVELOPMENT_PART '+json.dumps(part, sort_keys=True), flush=True)
            raise
        part = {'group': name, 'elapsed_seconds': time.monotonic()-tick,
                'result': result}
        groups.append(part)
        print('DEVELOPMENT_PART '+json.dumps(part, sort_keys=True), flush=True)
        if not result['all_passed']:
            raise ArithmeticError('new complete-grid development group failed: '+name)
    return {'schema': SCHEMA, 'status': 'complete',
            'source_files_sha256': implementation_hashes(),
            'groups': groups, 'all_passed': True,
            'elapsed_seconds': time.monotonic()-started,
            'maximum_rss_MiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.,
            'old_developer_suites_called': 0,
            'actual_scientific_research_inputs_or_HiGHS_calls': 0}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--output')
    args = parser.parse_args()
    if not args.check_only:
        parser.error('this source only has the new artificial --check-only entry')
    report = run_development()
    text = json.dumps(report, sort_keys=True, indent=2)+'\n'
    if args.output:
        from frame_collar_bvp import atomic_save
        atomic_save(args.output, report)
    print('COMPLETE_REPORT '+json.dumps(report, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()

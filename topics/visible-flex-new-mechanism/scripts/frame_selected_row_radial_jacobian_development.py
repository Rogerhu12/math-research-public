#!/usr/bin/env python3
"""New public artificial checks for the selected-row radial factorization.

These checks use a newly specified small real family, not a saved research
candidate.  They do not execute any old developer suite or nonlinear solver.
All new execution is restricted to this repository's public GitHub Actions.
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

from frame_collar_bvp import atomic_save
from frame_five_height_field import FiveHeightField, artificial_problem
from frame_entry_single_q import SingleQGrid
from frame_height_affine_gate import HeightAffineGate, require_public_research_environment
from frame_height_null_gate import FiveNullHeightGate
from frame_curvature_soc_steps import configuration as start_configuration
from frame_metric_budget_recovery import configuration as recovery_configuration
from frame_metric_entry_tail_height159 import configuration as mapped_configuration
from frame_metric_height159_soc_hold import (
    SOCHold159Objective, configuration as held_configuration)
from frame_metric_height159_factorized_rows import (
    FactorizedHeight159Objective, configuration as factorized_configuration,
    implementation_hashes as factorized_hashes)
from frame_selected_row_radial_jacobian import (
    SelectedRadialJacobian, POSITION_KEYS, array_hash)
from frame_metric_spectral_recovery import (
    selected_spectral_parameter_jacobian, spectral_proposal_rows, EPSILON_EXACT)
from frame_metric_epigraph import geometry_values
import frame_metric_budget_restoration_rows as rows_api

SCHEMA = 'selected-row-radial-factorization-new-artificial-development-v1'


def implementation_hashes():
    result = factorized_hashes()
    p = Path(__file__)
    result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def _relative(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.max(abs(a-b))/max(1., float(np.max(abs(b)))))


def _reject(callback):
    try:
        callback()
    except (ValueError, ArithmeticError, KeyError, TypeError):
        return True
    return False


def _row_values(data, side, cfg, ids):
    radius = np.broadcast_to(data['metric']['a'][:, None], data['T'].shape[:2])
    result = rows_api.row_values(data, radius, side, cfg)['rows']
    geometry = geometry_values(data)
    result[:2] = spectral_proposal_rows(
        geometry['e'], geometry['f'], float(Q(cfg['fixed_metric_budget_exact'])),
        float(Q(EPSILON_EXACT)))
    return result.reshape(-1)[ids]


def _reference_rows(full_jacobian, ids, side, cfg):
    nr, nt = full_jacobian['T'].shape[:2]
    groups, points = ids//(nr*nt), ids % (nr*nt)
    ri, ti = points//nt, points % nt
    small = {key: full_jacobian[key][ri, ti] for key in POSITION_KEYS}
    small.update({'jac_'+key: full_jacobian['jac_'+key][ri, ti]
                  for key in POSITION_KEYS})
    answer = selected_spectral_parameter_jacobian(
        small, full_jacobian['metric']['a'][ri], groups, side, cfg)
    return answer, ri, ti


def _setup(side):
    old, reference = artificial_problem(side)
    field = FiveHeightField(old, reference)
    state = field.initial_state()
    state[153] = .0013
    state[154:] = .0001*np.array([1., -.3, .2, .4, -.2])
    base = held_configuration(mapped_configuration(recovery_configuration(
        start_configuration(), target='13/50', curvature_cap='58')))
    cfg = factorized_configuration(base)
    # These artificial query nodes include actual entry/cutoff/spline ports.
    exact_nodes = set(Q(x) for x in old.radial_knots)
    exact_nodes.update((Q(0), old.seed.length_exact,
                        old.entry.left_exact,
                        old.entry.left_exact+old.entry.length_exact/3,
                        old.entry.left_exact+old.entry.length_exact,
                        Q('9/100'), Q('117/1000'), Q('33/50')))
    nodes = sorted(x for x in exact_nodes if 0 <= x <= old.seed.length_exact)
    radial = np.array([float(x) for x in nodes])
    return old, reference, field, state, base, cfg, nodes, radial


def _kernel_cases():
    reports = []
    for side in (1, -1):
        old, reference, field, state, base, cfg, nodes, radial = _setup(side)
        evaluator = SelectedRadialJacobian(field, cfg)
        for nt in (8, 16):
            theta = np.arange(nt)*2*np.pi/nt
            ordinary = field.geometry(state, radial, theta, 2)
            full = field.geometry(state, radial, theta, 2,
                                  jacobian=True, full_two_jet_jacobian=True)
            nr, count = len(radial), len(radial)*nt
            raw = [g*count + ir*nt + ((3*g+2*ir+1) % nt)
                   for g in range(11) for ir in range(nr)]
            # Deliberately non-sorted, with exact repeated original row IDs.
            ids = np.array(raw[::-1] + [raw[3], raw[3]], np.int64)
            reference_J, ri, ti = _reference_rows(full, ids, side, cfg)
            bound = evaluator.bind_ordinary(
                state, radial, theta, ordinary, owner='new-artificial-current-cache')
            direction = np.cos(np.arange(159)+.4)
            direction[153] = 1.
            direction /= np.linalg.norm(direction)
            # The new path must not call any original full geometry-J API or
            # a full SingleQ parameter basis expansion.  This isolated patch
            # is an artificial assertion, never a production monkeypatch.
            with patch.object(field, 'geometry', side_effect=AssertionError('unexpected geometry call')), \
                 patch.object(old, 'geometry', side_effect=AssertionError('unexpected old163 geometry call')), \
                 patch.object(SingleQGrid, 'basis_jacobian',
                              side_effect=AssertionError('unexpected full SingleQ parameter basis')):
                new_J, diagnostic, directional = evaluator.evaluate(
                    state, radial, theta, ids, bound, side=side, owned_width=3,
                    development_direction=direction)
            groups = ids//count
            group_errors = {str(g): _relative(new_J[groups == g], reference_J[groups == g])
                            for g in range(11)}
            block_errors = {name: _relative(new_J[:, sl], reference_J[:, sl])
                            for name, sl in [('u', slice(0, 81)), ('v', slice(81, 153)),
                                             ('Q', slice(153, 154)), ('null-height', slice(154, 159))]}
            direct_errors = {}
            for key in POSITION_KEYS:
                old_direction = np.einsum('nck,k->nc', full['jac_'+key][ri, ti], direction)
                direct_errors[key] = _relative(directional[key], old_direction)
            step = 2e-7
            plus = field.geometry(state+step*direction, radial, theta, 2)
            minus = field.geometry(state-step*direction, radial, theta, 2)
            finite = (_row_values(plus, side, cfg, ids)-_row_values(minus, side, cfg, ids))/(2*step)
            finite_errors = {str(g): _relative((new_J@direction)[groups == g], finite[groups == g])
                             for g in range(11)}
            jet_fd = {key: _relative(directional[key],
                       (plus[key][ri, ti]-minus[key][ri, ti])/(2*step))
                      for key in POSITION_KEYS}
            other = state.copy()
            other[4] += 1e-9
            bad = dict(bound)
            bad['coordinate_definition_sha256'] = '0'*64
            wrong_state = _reject(lambda: evaluator.evaluate(
                other, radial, theta, ids, bound, side=side, owned_width=3))
            wrong_identity = _reject(lambda: evaluator.evaluate(
                state, radial, theta, ids, bad, side=side, owned_width=3))
            wrong_circle = _reject(lambda: evaluator.evaluate(
                state, radial, theta+np.pi/nt, ids, bound, side=side, owned_width=3))
            invalid_ids = _reject(lambda: evaluator.evaluate(
                state, radial, theta, [True], bound, side=side, owned_width=3))
            alias = ordinary.copy()
            alias['coordinate_definition_sha256'] = 'f'*64
            wrong_ordinary = _reject(lambda: evaluator.bind_ordinary(
                state, radial, theta, alias, owner='new-artificial-current-cache'))
            # Physical-only branch forms no second-order virtual columns,
            # but retains the same complete ordinary two-jet cache.
            first_ids = ids[groups < 7]
            first_bound = evaluator.bind_ordinary(
                state, radial, theta, ordinary, owner='new-artificial-current-cache')
            first_J, first_info, unused = evaluator.evaluate(
                state, radial, theta, first_ids, first_bound, side=side, owned_width=3)
            first_error = _relative(first_J, reference_J[groups < 7])
            checks = {
                'all_eleven_groups_match_original163_then159_J': max(group_errors.values()) < 5e-10,
                'all_four_column_blocks_keep_original_layout': max(block_errors.values()) < 5e-10,
                'all_six_position_jets_and_T_direction_match_old_J': max(direct_errors.values()) < 5e-10,
                'same_physical_field_row_direction_difference': max(finite_errors.values()) < 3e-5,
                'same_physical_six_jets_direction_difference': max(jet_fd.values()) < 3e-5,
                'physical_only_branch_matches_original_rows': first_error < 5e-10 and unused is None,
                'nonzero_Q_and_nonzero_exact_null_height_used':
                    bool(state[153] != 0 and np.all(state[154:] != 0)),
                'original_order_and_repeated_ids_preserved':
                    bool(np.array_equal(new_J[-1], new_J[-2])
                         and diagnostic['row_ids_sha256'] == array_hash(ids)),
                'full_angular_grid_before_selection_and_virtual_axis_bounded':
                    diagnostic['maximum_selected_virtual_parameter_axis'] == 27
                    and diagnostic['maximum_angular_modes'] == 9,
                'new_path_performs_no_old_full_geometry_or_full_parameter_basis_request':
                    diagnostic['full_angle_163_or159_parameter_tensors_formed'] == 0
                    and diagnostic['ordinary_geometry_calls_inside_factorization'] == 0,
                'wrong_exact_state_rejected': wrong_state,
                'wrong_coordinate_identity_rejected': wrong_identity,
                'isolated_or_shifted_circle_rejected': wrong_circle,
                'boolean_row_ID_rejected': invalid_ids,
                'wrong_ordinary_identity_rejected': wrong_ordinary,
                'fine_odd_angles_and_real_ports_are_in_the_query':
                    bool(np.any(ti % 2 == 1) and 0 in ri and nr-1 in ri)}
            reports.append({
                'side': side, 'radial_count': nr, 'theta_count': nt, 'checks': checks,
                'group_J_relative_errors': group_errors, 'block_J_relative_errors': block_errors,
                'six_jet_direction_relative_errors': direct_errors,
                'row_directional_difference_relative_errors': finite_errors,
                'six_jet_directional_difference_relative_errors': jet_fd,
                'physical_only_J_relative_error': first_error,
                'factorization_diagnostics': diagnostic,
                'original_full_J_used_only_as_new_artificial_comparator': True,
                'research_state_or_solver_used': False})
    return reports


def _objective_cache_case():
    """Exercise the real parent linear_rows and rollback protocol, without a solve."""
    old, reference, field, state, base, cfg, nodes, radial = _setup(1)
    theta = np.arange(8)*2*np.pi/8
    reference_data = old.geometry(reference, radial, theta, 2)
    original_gate = HeightAffineGate.from_frozen_problem(old, reference, reference_data)
    lower = np.r_[np.full(154, -8.), np.full(9, -1.)]
    upper = -lower
    gate = FiveNullHeightGate.from_original(original_gate, field, lower, upper)
    ordinary = SOCHold159Objective(
        field, gate, radial, theta, 2, gate.coordinate_lower, gate.coordinate_upper,
        cfg=base, radial_nodes_exact=[str(x) for x in nodes])
    factored = FactorizedHeight159Objective(
        field, gate, radial, theta, 2, gate.coordinate_lower, gate.coordinate_upper,
        cfg=cfg, radial_nodes_exact=[str(x) for x in nodes])
    def ids(nt):
        count = len(radial)*nt
        return np.array(sorted({g*count+ir*nt+((g+ir+1) % nt)
            for g in range(11) for ir in (0, len(radial)//2, len(radial)-1)}), np.int64)
    for objective in (ordinary, factored):
        objective.set_pool(ids(len(theta)), {'kind': 'new-factorized-J-artificial-complete-group-pool'})
        objective.set_fine_pool(ids(len(objective.fine_theta)), {'kind': 'new-factorized-J-artificial-fine-pool'})
    old_rows, old_J, old_groups, old_tols = ordinary.linear_rows(ordinary.vector(state))
    new_rows, new_J, new_groups, new_tols = factored.linear_rows(factored.vector(state))
    aux_old = ordinary.constraint_jac(ordinary.vector(state))[:, -1]
    aux_new = factored.constraint_jac(factored.vector(state))[:, -1]
    coarse_cache = factored.derivative_cache
    fine_cache = factored.fine_derivative_cache
    before = (factored.geometry_evaluations, factored.fine_evaluations,
              factored.factorized_statistics['coarse']['refreshes'],
              factored.factorized_statistics['fine']['refreshes'])
    repeated = factored.linear_rows(factored.vector(state))
    repeated_counts = (factored.geometry_evaluations, factored.fine_evaluations,
                       factored.factorized_statistics['coarse']['refreshes'],
                       factored.factorized_statistics['fine']['refreshes'])
    # Cache-only fixture: no point is labelled physically admissible or accepted.
    # It uses the exact same saved-cache container that the real accepted_point
    # writes, so the inherited rollback methods themselves are exercised.
    factored.accepted_cache = {
        'state': state.copy(), 'coarse': factored.geometry_cache,
        'fine': factored.fine_cache, 'coarse_derivatives': coarse_cache,
        'fine_derivatives': fine_cache}
    trial = state.copy()
    trial[3] += 1e-8
    factored.evaluate(factored.vector(trial))
    factored.fine_decision(trial)
    after_trial = (factored.geometry_evaluations, factored.fine_evaluations)
    restored = factored.linear_rows(factored.vector(state))
    restored_counts = (factored.geometry_evaluations, factored.fine_evaluations)
    restored_cache_identity = (factored.derivative_cache is coarse_cache
                               and factored.fine_derivative_cache is fine_cache)
    all_ids = set(int(v) for v in factored.pool)
    extra = next(i for i in range(11*len(radial)*len(theta)) if i not in all_ids)
    old_version = factored.pool_version
    coarse_refreshes = factored.factorized_statistics['coarse']['refreshes']
    factored.set_pool(list(factored.pool)+[extra], {'kind': 'new-factorized-J-one-row-cache-invalidation'})
    changed = factored.linear_rows(factored.vector(state))
    checks = {
        'parent_linear_rows_values_groups_tolerances_unchanged':
            np.array_equal(old_rows, new_rows) and np.array_equal(old_groups, new_groups)
            and np.array_equal(old_tols, new_tols),
        'coarse_and_fine_selected_matrix_matches_original_objective':
            _relative(new_J, old_J) < 5e-10,
        'unused_fixed_zeta_column_contract_is_preserved': _relative(aux_new, aux_old) < 5e-12,
        'repeated_same_state_and_pool_reuses_selected_cache':
            before == repeated_counts and np.array_equal(repeated[1], new_J),
        'actual_parent_accepted_cache_rollback_needs_no_new_value_or_J':
            after_trial == restored_counts and restored_cache_identity
            and np.array_equal(restored[1], new_J),
        'pool_growth_retains_ids_and_invalidates_only_affected_selected_cache':
            factored.pool_version == old_version+1
            and all_ids.issubset(set(int(v) for v in factored.pool))
            and factored.factorized_statistics['coarse']['refreshes'] == coarse_refreshes+1
            and changed[1].shape[0] == new_J.shape[0]+1,
        'trimmed_coarse_cache_bound_by_actual_owner_not_missing_Field_metadata':
            'coordinate_definition_sha256' not in factored.geometry_cache
            and factored.factorized_statistics['coarse']['refreshes'] >= 1,
        'ordinary_value_and_gate_methods_are_not_overridden':
            FactorizedHeight159Objective.evaluate is SOCHold159Objective.evaluate
            and FactorizedHeight159Objective.fine_decision is SOCHold159Objective.fine_decision
            and FactorizedHeight159Objective.linear_rows is SOCHold159Objective.linear_rows,
        'original_physical_and_coordinate_identity_unchanged':
            field.identity(state) == ordinary.problem.identity(state)
            and factored.problem is field,
        'evaluation_identity_explicitly_changes':
            factored.evaluation_sha256 != ordinary.evaluation_sha256,
        'no_optimizer_or_new_acceptance_claim_in_cache_fixture':
            not factored.accepted_iterates and not ordinary.accepted_iterates}
    return {
        'checks': {k: bool(v) for k, v in checks.items()},
        'relative_complete_selected_J_error': _relative(new_J, old_J),
        'relative_fixed_auxiliary_column_error': _relative(aux_new, aux_old),
        'factorization_statistics': copy.deepcopy(factored.factorized_statistics),
        'cache_fixture_is_not_an_admissible_or_accepted_geometry_claim': True,
        'LP_invocations': 0, 'nonlinear_optimizer_invocations': 0}


def developer_check():
    require_public_research_environment()
    started = time.monotonic()
    kernel = _kernel_cases()
    objective = _objective_cache_case()
    passed = all(all(item['checks'].values()) for item in kernel) and all(objective['checks'].values())
    return {
        'schema': SCHEMA, 'completion': 'complete',
        'development': {'all_passed': bool(passed)},
        'artificial_inputs_only': True,
        'research_candidate_constructed_evaluated_or_optimized': False,
        'old_developer_suites_repeated': False,
        'new_kernel_cases': kernel, 'new_real_parent_cache_case': objective,
        'source_files_sha256': implementation_hashes(),
        'elapsed_seconds': time.monotonic()-started,
        'maximum_RSS_MiB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
        'numpy_version': np.__version__}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true', required=True)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    report = developer_check()
    if args.out:
        atomic_save(args.out, report)
    print('COMPLETE_REPORT ' + json.dumps(report, ensure_ascii=False, sort_keys=True,
                                         separators=(',', ':'), allow_nan=False), flush=True)
    if not report['development']['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

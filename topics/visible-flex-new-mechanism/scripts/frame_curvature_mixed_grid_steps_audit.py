#!/usr/bin/env python3
"""Resume the saved two-grid 06a603 state, adding true fine-angle Jacobian rows.

Thirteen published inputs are byte-bound. Old optimizers are not replayed.
Only the new mixed-grid fixed-target controller runs; all physical parameters,
the metric, b0, height mean and the two complete acceptance grids are unchanged.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import tempfile
import time
import traceback

import numpy as np

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_entry_paired_repair_audit import require_public_actions
from frame_entry_short_bounded_audit import read_input, audit_data, compare_data
from frame_independent_height_solve import state_record
from frame_curvature_epigraph_exchange import GROUPS, candidate_decision
from frame_metric_epigraph import geometry_values
import frame_curvature_feasible_steps_audit as previous
from frame_curvature_mixed_grid_steps import (
    MixedGridStepObjective, configuration, run_mixed_steps, developer_check as mixed_check,
    implementation_hashes as mixed_hashes, POLICY)

SCHEMA = 'same-g-mixed-grid-fixed-70-short-step-audit-v1'
PRIOR_RUN = '43653520539'
PRIOR_SOURCE = 'aa93b6575acfe5914c3038493dfd5e30864f3b1d'
PRIOR_FINAL_PHYSICAL_SHA = '06a603ec4aa254d29cb44fdcf60190fba356d8a6834eb73748d0755243db8736'
coefficients = previous.coefficients
curvature_grid = previous.curvature_grid
summary_path = previous.summary_path


def implementation_hashes():
    result = previous.implementation_hashes()
    result.update(mixed_hashes())
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def replay_completed_steps(prepared, prior, *, artificial=False):
    restored, bindings, tenth, old_replay, old_pool = prepared
    problem, old_initial, gate, lower, upper, source_cfg, old_cfg = restored
    if (prior.get('schema') != previous.SCHEMA
            or prior.get('status') != 'complete-fixed-target-two-grid-short-step-audit'
            or bool(prior.get('artificial_inputs_only')) != bool(artificial)):
        raise ValueError('a completed matching fixed-target two-grid report is required')
    if (prior.get('source_files_sha256') != previous.implementation_hashes()
            or prior.get('configuration') != old_cfg):
        raise ValueError('thirteenth source or configuration differs from its frozen implementation')
    if not artificial and (str(prior.get('github_run_id')) != PRIOR_RUN or prior.get('github_sha') != PRIOR_SOURCE):
        raise ValueError('thirteenth report source/run differs')
    for name, binding in bindings.items():
        recorded = prior.get('exact_input_storage', {}).get(name, {})
        for key in ['decoded_sha256', 'decoded_bytes', 'stored_sha256', 'stored_bytes', 'gzip_storage']:
            if recorded.get(key) != binding.get(key):
                raise ValueError('thirteenth preceding byte binding differs: '+name+'/'+key)
    if (prior.get('initial_state') != state_record(problem, old_initial)
            or prior.get('input_replay') != old_replay
            or not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_optimizer_calls_this_run') != 0
            or prior.get('old_failed_metric_auxiliary_delta') != tenth['selected_raw_auxiliary_delta']):
        raise ValueError('the original e407/source family, history or complete replay differs')
    stage = prior['fixed_target_short_step_stage']; checkpoint = stage['checkpoint']
    point = checkpoint.get('selected_two_grid_physical_point')
    if not point:
        raise ValueError('no accepted complete two-grid state was saved')
    state = np.asarray(point.get('physical_parameter_coefficients_binary64'), float)
    if (state.shape != (problem.nunknown,) or not np.all(np.isfinite(state))
            or coefficients(state) != point.get('exact_binary64_physical_coefficients')
            or digest(problem.identity(state)) != point.get('physical_state_sha256')):
        raise ValueError('selected full binary64 vector, exact rationals or physical identity differs')
    if not artificial and point['physical_state_sha256'] != PRIOR_FINAL_PHYSICAL_SHA:
        raise ValueError('the real continuation must use the saved accepted 06a603 point')
    expected = state_record(problem, state)
    if prior.get('final_state') != expected:
        raise ValueError('thirteenth final canonical state does not match all selected coefficients')
    if (problem.metric_model(state) != problem.metric_model(old_initial)
            or not prior.get('final_selection_validation', {}).get('both_value_grids_physical_gate_pass')):
        raise ValueError('saved accepted state changed g or did not pass both physical value grids')
    accepted = checkpoint.get('accepted_iterates', [])
    if not accepted or accepted[-1] != point:
        raise ValueError('selected point is not the last recorded accepted physical iterate')
    for name in ['final_full_grid_constraints', 'final_doubled_constraints']:
        decision = prior.get(name, {})
        if not decision.get('eligible_under_fixed_metric_and_physical_gates'):
            raise ValueError('saved fine/coarse physical decision is not eligible')
        for key in ['fixed_metric_budget_exact', 'hard_strip_half_width_exact', 'mirror_target_exact']:
            if decision.get(key) != old_cfg[key]:
                raise ValueError('a saved geometric gate changed: '+key)
    radial, theta, grid = curvature_grid(tenth)
    if prior.get('full_value_sampling_definition') != grid:
        raise ValueError('the thirteenth complete value grid differs')
    history = checkpoint.get('active_row_pool_history', [])
    if not history:
        raise ValueError('the thirteenth report has no learned row pool')
    last = history[-1]; indices = last.get('row_indices')
    if (not isinstance(indices, list) or not indices or any(type(i) is not int for i in indices)
            or indices != sorted(set(indices)) or last.get('row_count') != len(indices)
            or last.get('row_indices_sha256') != digest(indices) or last.get('group_order') != list(GROUPS)
            or last.get('flat_index_rule') != 'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'
            or last.get('total_full_grid_rows') != len(GROUPS)*len(radial)*len(theta)
            or min(indices) < 0 or max(indices) >= len(GROUPS)*len(radial)*len(theta)
            or len(indices) > old_cfg['max_pool_rows'] or not set(old_pool).issubset(indices)):
        raise ValueError('thirteenth coarse pool indices, original coordinates or retention differs')
    locations = {}
    decisions = [prior['final_doubled_constraints']]
    decisions += [x.get('decision', {}) for x in checkpoint.get('saved_fine_trials', [])
        if x.get('status') == 'complete-doubled-angle-value-call']
    for decision in decisions:
        location = decision.get('direct_max_eta_location')
        if location is not None:
            pair = (float(location['t']), float(location['theta']))
            if not all(np.isfinite(pair)):
                raise ValueError('saved fine metric peak coordinates must be finite')
            locations[pair] = {'t':pair[0], 'theta':pair[1]}
    cfg = configuration(old_cfg)
    learned = {'schema':'thirteenth-fixed-target-learned-coarse-pool-v1',
        'source_run':prior.get('github_run_id'), 'source_commit':prior.get('github_sha'),
        'source_pool_version':last['version'], 'source_pool_rows':len(indices),
        'source_row_indices_sha256':last['row_indices_sha256'], 'source_full_value_grid_sha256':grid['definition_sha256'],
        'all_preceding_enforced_coarse_rows_retained':True}
    retained = {'schema':prior['schema'], 'status':stage['status'],
        'source_run':prior.get('github_run_id'), 'source_commit':prior.get('github_sha'),
        'old_fixed_target_lambda_exact':prior['fixed_curvature_target_definition']['exact'],
        'old_fixed_target_reached':bool(stage.get('fixed_target_reached')),
        'old_target_failure_and_rejected_under70_trials_are_not_erased':True,
        'published_final_coarse_decision':copy.deepcopy(prior['final_full_grid_constraints']),
        'published_final_fine_decision':copy.deepcopy(prior['final_doubled_constraints'])}
    replay = {'schema':'thirteen-input-mixed-grid-two-grid-accepted-replay-v1',
        'twelve_input_replay':old_replay, 'canonical_physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'physical_parameter_count':problem.nunknown, 'same_full_saved_accepted_coefficients':True,
        'same_complete_g_b0_space_and_original_two_value_grids':True,
        'learned_pool':learned, 'completed_fixed_target_attempt_retained':retained,
        'known_fine_metric_locations':list(locations.values()), 'new_mixed_grid_policy':POLICY,
        'old_optimizer_calls_replayed':0, 'no_research_geometry_during_structural_replay':True}
    return (problem, state, gate, lower, upper, source_cfg, cfg), replay, np.asarray(indices, dtype=np.int64)


def prepare_run(args, *, artificial=False, process_started=None):
    start = time.monotonic(); process_started = start if process_started is None else process_started
    phase = 'twelve-input-original-accepted-state-replay'; bindings = {}
    try:
        if not artificial:
            paths = [args.input, args.anchor_input, args.short_audit, args.height_audit, args.prior_joint_audit,
                args.resume_audit, args.epigraph_audit, args.trial_audit, args.dense_audit, args.exchange_audit,
                args.curvature_audit, args.feasible_curvature_audit, args.fixed_target_audit]
            require_public_actions(os.environ.get('GITHUB_ACTIONS'), os.environ.get('GITHUB_REPOSITORY'), paths)
        old = previous.prepare_run(args, artificial=artificial, process_started=process_started)
        bindings = copy.deepcopy(old[1]); phase = 'thirteenth-fixed-target-byte-binding'
        if args.fixed_target_audit is None or args.expected_fixed_target_sha256 is None:
            raise ValueError('the thirteenth complete report and exact decoded SHA are required')
        prior, raw, binding = read_input(args.fixed_target_audit, args.expected_fixed_target_sha256)
        phase = 'thirteenth-complete-accepted-state-and-learned-pool-replay'
        restored, replay, pool = replay_completed_steps(old, prior, artificial=artificial)
        bindings['completed_fixed_target_short_steps'] = binding
        return restored, bindings, old[2], replay, pool
    except Exception as error:
        failure = {'schema':SCHEMA, 'status':'input-replay-failed-before-mixed-grid-geometry', 'phase':phase,
            'source_files_sha256':implementation_hashes(), 'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial), 'old_optimizer_calls_this_run':0, 'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-start,
            'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__, 'message':str(error)}}
        save_report(args.out, failure)
        raise


def lean_decision(decision):
    names = ['eligible_under_fixed_metric_and_physical_gates', 'fixed_metric_budget_pass',
        'physical_gate_pass_excluding_fixed_metric', 'direct_max_eta', 'direct_max_eta_location',
        'direct_maximum_absolute_principal_curvature', 'direct_max_curvature_location',
        'direct_curvature_minus_lambda', 'minimum_signed_height', 'ball_radius_squared_normalized_max',
        'maximum_absolute_y', 'inner_strip_absolute_margin', 'direct_mirror_radius_min_finite',
        'regularity_screen_pass']
    result = {k:copy.deepcopy(decision[k]) for k in names if k in decision}
    if 'cap_and_box' in decision:
        result['cap_and_box'] = {k:v for k, v in decision['cap_and_box'].items()
            if not isinstance(v, (list, dict))}
    return result


def lean_point(point):
    if point is None:
        return None
    result = {k:copy.deepcopy(point[k]) for k in ['accepted_index', 'physical_state_sha256',
        'maximum_curvature_on_both_grids', 'reason'] if k in point}
    for key in ['coarse', 'fine']:
        if key in point:
            result[key] = lean_decision(point[key])
    return result


def small_summary(report, out):
    names = ['schema', 'status', 'phase', 'source_files_sha256', 'configuration', 'github_sha', 'github_run_id',
        'github_repository', 'artificial_inputs_only', 'old_optimizer_calls_this_run',
        'old_failed_metric_auxiliary_delta', 'learned_pool_replay', 'fixed_curvature_target_definition',
        'final_selection_validation', 'elapsed_seconds', 'run_audit_elapsed_seconds', 'prepare_elapsed_seconds',
        'process_total_elapsed_seconds', 'optimization_active_seconds', 'process_clock_scope',
        'peak_rss_kib_linux', 'value_evaluation_counts', 'unchanged_complete_metric_and_height_reference',
        'error', 'limitations']
    result = {k:copy.deepcopy(report[k]) for k in names if k in report}
    result['exact_input_storage'] = {name:{k:v for k, v in binding.items()
        if k in ['decoded_sha256', 'decoded_bytes', 'stored_sha256', 'stored_bytes', 'gzip_storage']}
        for name, binding in report.get('exact_input_storage', {}).items()}
    for key in ['initial_state', 'final_state']:
        if key in report:
            state = report[key]
            result[key] = {'canonical_physical_state_sha256':state['canonical_physical_state_sha256'],
                'parameter_count':len(state['parameter_coefficients_binary64']),
                'complete_metric_sha256':state['metric_model']['mathematical_definition_sha256'],
                'evaluation_definition_sha256':digest(state['evaluation_definition'])}
    for key in ['initial_current_constraints', 'initial_doubled_constraints', 'final_full_grid_constraints', 'final_doubled_constraints']:
        if key in report:
            result[key] = lean_decision(report[key])
    if 'completed_fixed_target_attempt_retained' in report:
        old = report['completed_fixed_target_attempt_retained']
        result['completed_fixed_target_attempt_retained'] = {k:v for k, v in old.items()
            if not k.startswith('published_final_')}
    if 'same_parameter_Pi_refinement' in report:
        result['same_parameter_Pi_refinement'] = previous.previous.previous.compact_comparison(report['same_parameter_Pi_refinement'])
    if 'full_value_sampling_definition' in report:
        grid = report['full_value_sampling_definition']
        result['full_value_sampling_definition'] = {k:grid[k] for k in ['schema', 'definition_sha256', 'radial_count', 'angular_nodes']}
    stage = report.get('mixed_grid_short_step_stage')
    if stage:
        item = {k:v for k, v in stage.items() if k not in ['checkpoint', 'solver']}
        item['solver'] = {k:v for k, v in stage.get('solver', {}).items() if k != 'models'}
        item['models'] = []
        for model in stage.get('solver', {}).get('models', []):
            small = {k:copy.deepcopy(v) for k, v in model.items() if k not in ['exact_binary64_proposed_step', 'trials']}
            small['trials'] = []
            for trial in model.get('trials', []):
                t = {k:v for k, v in trial.items() if k not in ['exact_binary64_physical_coefficients', 'coarse_decision', 'fine_decision']}
                for key in ['coarse_decision', 'fine_decision']:
                    if key in trial:
                        t[key] = {k:trial[key][k] for k in ['eligible_under_fixed_metric_and_physical_gates',
                            'direct_max_eta', 'direct_maximum_absolute_principal_curvature'] if k in trial[key]}
                small['trials'].append(t)
            item['models'].append(small)
        snap = stage['checkpoint']
        counts = ['physical_geometry_evaluations', 'doubled_angle_full_value_evaluations',
            'total_full_value_physical_evaluations', 'epigraph_vector_evaluations', 'jacobian_geometry_batches',
            'jacobian_refreshes', 'total_elapsed_seconds', 'initialization_elapsed_seconds',
            'optimization_elapsed_seconds', 'value_geometry_seconds', 'doubled_angle_value_seconds',
            'jacobian_geometry_seconds', 'maximum_retained_selected_derivative_bytes',
            'maximum_returned_batch_Jacobian_bytes', 'maximum_single_constraint_Jacobian_bytes',
            'maximum_batch_query_radial_rows', 'maximum_same_state_batch_ordinary_jet_difference',
            'fine_physical_pool_row_count', 'fine_selected_Jacobian_batches', 'fine_selected_Jacobian_refreshes',
            'fine_selected_Jacobian_seconds', 'fine_selected_Jacobian_maximum_returned_bytes',
            'fine_selected_Jacobian_maximum_retained_bytes', 'fine_selected_Jacobian_maximum_query_radial_rows',
            'fine_batch_ordinary_replay_maxima', 'physical_height_mean_and_primitive_are_unchanged']
        item['checkpoint'] = {k:snap[k] for k in counts if k in snap}
        item['checkpoint']['accepted_iterates'] = [lean_point(p) for p in snap.get('accepted_iterates', [])]
        item['checkpoint']['selected_two_grid_physical_point'] = lean_point(snap.get('selected_two_grid_physical_point'))
        item['checkpoint']['fine_pool_updates'] = [{k:r[k] for k in ['version', 'row_count', 'row_indices_sha256']}
            for r in snap.get('fine_physical_row_pool_history', [])]
        item['checkpoint']['all_original_grid_coordinates_full_trial_coefficients_and_full_pool_histories_in_full_report'] = True
        result['mixed_grid_short_step_stage'] = item
    raw = Path(out).read_bytes()
    result['full_report'] = {'filename':Path(out).name, 'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest()}
    return result


def save_report(out, report):
    atomic_save(out, report)
    atomic_save(summary_path(out), small_summary(report, out))


def run_audit(prepared, out, *, artificial=False, evaluate_only=False,
              process_started=None, prepare_seconds=None):
    restored, bindings, tenth, replay, learned_pool = prepared
    problem, initial, gate, lower, upper, source_cfg, cfg = restored
    started = time.monotonic()
    scope = ('main entrance including thirteen-input loader and restoration' if process_started is not None
             else 'direct run_audit entrance; artificial fixtures constructed outside this clock')
    process_started = started if process_started is None else process_started
    metric = copy.deepcopy(problem.metric_model(initial))
    b0 = copy.deepcopy(problem.height_base_definition)
    target = float(Q(cfg['fixed_curvature_target_exact']))
    zeta = target/float(Q(cfg['curvature_scale_exact']))
    report = {'schema':SCHEMA, 'source_files_sha256':implementation_hashes(), 'configuration':cfg,
        'exact_input_storage':bindings, 'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'), 'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'), 'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':0, 'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':state_record(problem,initial), 'unchanged_complete_metric_and_height_reference':True,
        'process_clock_scope':scope, 'prepare_elapsed_seconds':prepare_seconds,
        'learned_pool_replay':replay['learned_pool'],
        'completed_fixed_target_attempt_retained':replay['completed_fixed_target_attempt_retained'],
        'fixed_curvature_target_definition':{
            'exact':cfg['fixed_curvature_target_exact'], 'evaluated':target,
            'fixed_scaled_zeta_evaluated':zeta, 'not_a_physical_coefficient':True,
            'not_claimed_feasible_at_start':True, 'not_the_final_reach_curvature_target':True,
            'final_reach_design_tau_exact':cfg['curvature_target_radius_exact']},
    }
    def save(status):
        now = time.monotonic()
        report.update(status=status, elapsed_seconds=now-started, run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=report.get('mixed_grid_short_step_stage',{}).get('checkpoint',{}).get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('thirteen-inputs-replayed-before-mixed-grid-step-geometry')
    try:
        report['phase'] = 'two-grid-physical-initialization-outside-active-optimization-clock'
        radial, theta, grid = curvature_grid(tenth)
        order = int(source_cfg['primitive_order'])
        report['full_value_sampling_definition'] = grid
        def checkpoint(snapshot):
            report['mixed_grid_short_step_stage'] = {
                'status':'current-fixed-target-checkpoint', 'checkpoint':snapshot, 'solver':{}}
            save('fixed-target-two-grid-short-step-checkpoint')
        objective = MixedGridStepObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(
            complete_value_sampling_definition=grid,
            thirteenth_report_decoded_sha256=bindings['completed_fixed_target_short_steps']['decoded_sha256'],
            learned_pool_replay=replay['learned_pool'], old_metric_delta_and_curvature_lambda_are_history_only=True)
        objective.evaluation_sha256 = digest(objective.evaluation_definition)
        objective.set_pool(learned_pool, {'kind':'same-grid-pool-retained-from-thirteenth-fixed-target-report',
            'source':replay['learned_pool']})
        first = objective.evaluate(np.r_[initial,zeta])
        report['initial_current_constraints'] = copy.deepcopy(first['decision'])
        report['initial_full_grid_audit'] = audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints'] = copy.deepcopy(objective.fine_decision(initial))
        save('complete-initial-two-grid-physical-and-fixed-target-diagnostics')
        report['phase'] = 'fixed-target-linear-proposals-with-two-grid-acceptance'
        stage = run_mixed_steps(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['mixed_grid_short_step_stage'] = stage
        point = stage['checkpoint'].get('selected_two_grid_physical_point')
        if point is None:
            save('no-two-grid-physical-baseline-eligible')
            return report
        final = np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if (coefficients(final) != point['exact_binary64_physical_coefficients']
                or digest(problem.identity(final)) != point['physical_state_sha256']):
            raise ValueError('the selected two-grid exact coefficient vector or physical identity differs')
        identity = problem.identity(final)
        frozen, fc = problem.frozen_metric_copy(final)
        if (fc.tobytes() != final.tobytes() or frozen.identity(fc) != identity
                or frozen.metric_model(fc) != metric or frozen.height_base_definition != b0):
            raise ArithmeticError('freeze changed g, b0, physical coefficients or selected field')
        problem, final = frozen, fc
        report['final_state'] = state_record(problem,final)
        report['phase'] = 'independent-same-state-final-two-grid-values'
        work = problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit'] = audit_data(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints'] = candidate_decision(problem,gate,final,zeta,work,lower,upper,cfg)
        save('selected-two-grid-state-recomputed-on-coarse-value-grid')
        del objective
        doubled_theta = np.arange(2*len(theta))*np.pi/len(theta)
        doubled = problem.geometry(final,radial,doubled_theta,order)
        report['final_doubled_angle_audit'] = audit_data(problem,final,doubled,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints'] = candidate_decision(problem,gate,final,zeta,doubled,lower,upper,cfg)
        report['same_parameter_Pi_refinement'] = compare_data(problem,work,problem,doubled,final,
            name='one accepted physical field, same fixed target 70, no additional parameter step',theta_stride=2)
        if problem.identity(final) != identity:
            raise ArithmeticError('final angle refinement changed the physical state')
        coarse, fine = report['final_full_grid_constraints'], report['final_doubled_constraints']
        eligible = bool(coarse['eligible_under_fixed_metric_and_physical_gates']
                        and fine['eligible_under_fixed_metric_and_physical_gates'])
        maximum = max(coarse['direct_maximum_absolute_principal_curvature'], fine['direct_maximum_absolute_principal_curvature'])
        initial_maximum = max(report['initial_current_constraints']['direct_maximum_absolute_principal_curvature'],
                              report['initial_doubled_constraints']['direct_maximum_absolute_principal_curvature'])
        report['final_selection_validation'] = {
            'both_value_grids_physical_gate_pass':eligible,
            'both_grid_maximum_curvature':maximum,
            'initial_both_grid_maximum_curvature':initial_maximum,
            'actual_curvature_decrease':initial_maximum-maximum,
            'fixed_target_70_reached':bool(eligible and maximum<=target+cfg['direct_curvature_tolerance']),
            'whole_surface_reach_not_certified':True,
            'new_failure_is_not_silently_promoted_to_an_accepted_state':True,
        }
        count = stage['checkpoint']['total_full_value_physical_evaluations']
        report['value_evaluation_counts'] = {
            'initialization_and_step_coarse_plus_fine_within_shared_cap':count,
            'shared_cap':cfg['max_physical_evaluations'],
            'independent_final_same_state_value_calls':2,
            'total_counted_full_value_calls_in_this_driver':count+2,
            'failed_fine_value_attempts_also_consume_shared_cap':True,
            'Jacobian_batch_calls_recorded_separately':True,
            'no_final_optimizer_or_step':True,
        }
        report['limitations'] = {
            'all_value_gates_and_curvature_diagnostics_sampled_only':True,
            'metric_budget_167_over_625_is_not_exact_isometry':True,
            'goal_70_is_not_target_reach_curvature_1000_over_61':True,
            'target_not_reached_and_actual_decrease_are_different_outcomes':True,
            'LP_linear_feasibility_is_not_actual_geometry_feasibility':True,
            'failed_trials_are_saved_but_not_warm_starts':True,
            'curvature_and_mirror_pairs_do_not_cover_all_surface_pairs':True,
            'no_complete_embedding_or_whole_surface_reach_certificate':True,
            'no_old_optimization_replayed':True,
        }
        save('complete-mixed-grid-fixed-target-short-step-audit' if eligible
             else 'final-same-state-value-recheck-failed-do-not-use-as-new-warm-start')
        return report
    except Exception as error:
        report['error'] = {'type':type(error).__name__, 'message':str(error), 'traceback':traceback.format_exc()}
        save('mixed-grid-short-step-audit-error-checkpoints-preserved')
        return report


def artificial_thirteen_inputs(directory):
    args, unused, twelfth = previous.artificial_twelve_inputs(directory)
    args.out = directory/'completed-fixed-target-artificial.json'
    twelve = previous.prepare_run(args, artificial=True)
    prior = previous.run_audit(twelve, args.out, artificial=True, evaluate_only=True)
    if prior.get('status') != 'complete-fixed-target-two-grid-short-step-audit':
        raise ArithmeticError('artificial thirteenth source fixture failed')
    args.fixed_target_audit = args.out
    args.expected_fixed_target_sha256 = hashlib.sha256(args.out.read_bytes()).hexdigest()
    return args, twelve, prior


def developer_check():
    targeted = mixed_check()
    with tempfile.TemporaryDirectory(prefix='curvature-mixed-grid-artificial-', dir='/dev/shm') as folder:
        directory = Path(folder)
        args, twelve, prior = artificial_thirteen_inputs(directory)
        args.out = directory/'mixed-grid-artificial.json'
        process_started = time.monotonic()
        prepared = prepare_run(args, artificial=True, process_started=process_started)
        report = run_audit(prepared, args.out, artificial=True, evaluate_only=True,
            process_started=process_started, prepare_seconds=time.monotonic()-process_started)
        status = report['status']; error = report.get('error')
        stage = report.get('mixed_grid_short_step_stage', {})
        snap = stage.get('checkpoint', {})
        same = report.get('final_state') == prior['final_state']
        no_old = report.get('old_optimizer_calls_this_run') == 0
        no_lp = stage.get('solver', {}).get('linear_program_invocation_count') == 0
        oldpool = prior['fixed_target_short_step_stage']['checkpoint']['active_row_pool_history'][-1]['row_indices']
        retained = set(oldpool).issubset(snap.get('active_row_pool_history', [{}])[0].get('row_indices', []))
        fine_created = len(snap.get('fine_physical_row_pool_history', [])) == 1
        source = report.get('source_files_sha256') == implementation_hashes()
        summary = json.loads(summary_path(args.out).read_text())
        summary_bound = summary['full_report']['sha256'] == hashlib.sha256(args.out.read_bytes()).hexdigest()
        summary_bytes = summary_path(args.out).stat().st_size

        # The artificial full-frame fixture additionally exercises its real
        # complete periodic primitive and query-independent height interface.
        problem, initial, gate, lower, upper, source_cfg, cfg = prepared[0]
        radial, theta, grid = curvature_grid(prepared[2])
        objective = MixedGridStepObjective(problem, gate, radial, theta, int(source_cfg['primitive_order']), lower, upper, cfg=cfg)
        objective.initialize_fine_pool(initial, known_metric_locations=prepared[3]['known_fine_metric_locations'])
        # Ensure an odd fine angle is tested even when the artificial maximum
        # happens to lie on an even point of its complete angle circle.
        fine_count = len(radial)*len(objective.fine_theta)
        chosen = set(objective.fine_pool)
        chosen.add((len(radial)//2)*len(objective.fine_theta)+1)
        objective.set_fine_pool(chosen, {'kind':'artificial-real-frame-odd-angle-probe'})
        J = objective.fine_derivatives(initial)
        direction = np.sin(np.arange(problem.nunknown)+.3)
        direction /= np.linalg.norm(direction)
        eps = 1e-6
        plus = objective.fine_rows(initial+eps*direction).reshape(-1)[objective.fine_pool]
        plus_values = geometry_values(objective.fine_cache['data'])
        minus = objective.fine_rows(initial-eps*direction).reshape(-1)[objective.fine_pool]
        minus_values = geometry_values(objective.fine_cache['data'])
        raw_fd = float(np.max(abs((plus-minus)/(2*eps)-J@direction)))
        # The inherited artificial fixture sets bar=100000. Differentiate the
        # identical rows after removing that constant *before* floating-point
        # addition, rather than subtracting two rounded numbers near 100000.
        # Actual row evaluation and its acceptance tolerance are not changed.
        branch = objective.fine_pool//fine_count
        points = objective.fine_pool % fine_count
        stable_plus, stable_minus = plus.copy(), minus.copy()
        bar = float(Q(cfg['fixed_metric_budget_exact']))
        for values, output in [(plus_values, stable_plus), (minus_values, stable_minus)]:
            for group in [0, 1]:
                mask = branch == group; at = points[mask]
                output[mask] = (-1 if group == 0 else 1)*values['e'].ravel()[at]-values['f'].ravel()[at]**2/bar
        fd = float(np.max(abs((stable_plus-stable_minus)/(2*eps)-J@direction)))
        replay_error = max(objective.fine_batch_replay_maxima.values())
        physical_before = problem.identity(initial)
        changed_theta_geometry = problem.geometry(initial, radial, objective.fine_theta, int(source_cfg['primitive_order']))
        coarse_geometry = problem.geometry(initial, radial, theta, int(source_cfg['primitive_order']))
        center_same = float(np.max(abs(changed_theta_geometry['center']-coarse_geometry['center'])))
        same_identity = problem.identity(initial) == physical_before

        wrong = copy.copy(args); wrong.out = directory/'wrong-thirteenth-sha.json'
        wrong.expected_fixed_target_sha256 = '0'*64
        try:
            prepare_run(wrong, artificial=True); bad_sha = False
        except ValueError:
            failure = json.loads(wrong.out.read_text())
            bad_sha = failure['phase'] == 'thirteenth-fixed-target-byte-binding' and failure['new_solver_calls'] == 0
        broken = copy.deepcopy(prior)
        broken['fixed_target_short_step_stage']['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0] = '123'
        try:
            replay_completed_steps(twelve, broken, artificial=True); bad_state = False
        except ValueError:
            bad_state = True
        broken = copy.deepcopy(prior)
        broken['fixed_target_short_step_stage']['checkpoint']['active_row_pool_history'][-1]['row_indices'][0] = -1
        try:
            replay_completed_steps(twelve, broken, artificial=True); bad_pool = False
        except ValueError:
            bad_pool = True
        ref = report.get('same_parameter_Pi_refinement')
    passed = bool(targeted['passed'] and same and no_old and no_lp and retained and fine_created and source
        and summary_bound and summary_bytes < 95000 and fd < 3e-7 and replay_error < 1e-10
        and center_same == 0 and same_identity and bad_sha and bad_state and bad_pool
        and status == 'complete-mixed-grid-fixed-target-short-step-audit')
    return {'schema':'mixed-grid-fixed-target-complete-artificial-IO-check-v1',
        'artificial_inputs_only':True, 'research_geometry_evaluated_or_optimized':False,
        'no_Actions_environment_forged':True, 'targeted_new_branch_checks':targeted,
        'complete_thirteen_input_main_status':status, 'complete_main_error':error,
        'no_previous_optimizer_replayed':no_old, 'artificial_main_has_no_LP':no_lp,
        'same_saved_physical_coefficients_and_freeze':same, 'all_old_coarse_rows_retained':retained,
        'fine_pool_created_from_same_grid_saved_peaks':fine_created,
        'artificial_complete_frame_fine_selected_directional_Jacobian_error':fd,
        'uncentered_artificial_large_constant_finite_difference_error_retained':raw_fd,
        'artificial_metric_budget_evaluated':bar,
        'finite_difference_subtracts_only_the_known_metric_row_constant_before_rounding':True,
        'artificial_complete_frame_fine_batch_ordinary_replay_error':replay_error,
        'changing_query_angle_count_keeps_common_center_exact':center_same == 0,
        'fine_derivative_evaluation_preserves_physical_identity':same_identity,
        'summary_binds_complete_bytes':summary_bound, 'summary_bytes':summary_bytes,
        'source_hashes_match':source, 'wrong_thirteenth_SHA_saves_failure':bad_sha,
        'altered_complete_coefficient_rejected':bad_state, 'altered_old_pool_index_rejected':bad_pool,
        'same_state_angle_refinement':ref, 'passed':passed}


def main():
    process_started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['input', 'anchor-input', 'short-audit', 'height-audit', 'prior-joint-audit', 'resume-audit',
                 'epigraph-audit', 'trial-audit', 'dense-audit', 'exchange-audit', 'curvature-audit',
                 'feasible-curvature-audit', 'fixed-target-audit']:
        parser.add_argument('--'+name, type=Path)
    for name in ['input', 'anchor', 'short', 'height', 'prior-joint', 'resume', 'epigraph', 'trial', 'dense',
                 'exchange', 'curvature', 'feasible-curvature', 'fixed-target']:
        parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.check_only:
        try:
            result = developer_check()
        except Exception as error:
            atomic_save(args.out, {'schema':'mixed-grid-development-error-v1', 'passed':False,
                'artificial_inputs_only':True, 'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-process_started,
                'error':{'type':type(error).__name__, 'message':str(error), 'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(), process_total_elapsed_seconds=time.monotonic()-process_started)
        atomic_save(args.out, result)
        print(json.dumps({'out':str(args.out), 'passed':result['passed']}), flush=True)
        if not result['passed']:
            raise SystemExit(1)
        return
    start = time.monotonic()
    try:
        prepared = prepare_run(args, process_started=process_started)
    except Exception:
        raise SystemExit(1)
    report = run_audit(prepared, args.out, process_started=process_started, prepare_seconds=time.monotonic()-start)
    print(json.dumps({'out':str(args.out), 'status':report['status']}), flush=True)
    if report['status'] != 'complete-mixed-grid-fixed-target-short-step-audit':
        raise SystemExit(1)


if __name__ == '__main__':
    main()


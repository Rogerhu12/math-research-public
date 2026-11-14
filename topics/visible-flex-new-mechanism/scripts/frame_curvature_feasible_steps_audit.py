#!/usr/bin/env python3
"""Fixed target 70, small linear proposals, and two-grid physical acceptance.

Twelve byte-bound reports restore e407 and the learned rows. No preceding
optimization is repeated and no unsaved near-feasible old trial is invented.
Each accepted physical step must pass both angular grids and lower their
actual maximum curvature. A failed target is preserved as a failed target.
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
import frame_curvature_feasible_exchange_audit as previous
from frame_curvature_epigraph_exchange import GROUPS, candidate_decision
from frame_curvature_feasible_steps import (
    FeasibleStepObjective, configuration, run_feasible_steps,
    developer_check as steps_check, implementation_hashes as step_hashes, POLICY)

SCHEMA = 'same-g-fixed-curvature-target-two-grid-short-step-audit-v1'
PRIOR_RUN = '43648433010'
PRIOR_SOURCE = 'df535c0c42d76040903b1e89c6d08d13ea360ad2'
coefficients = previous.coefficients
curvature_grid = previous.curvature_grid
summary_path = previous.summary_path


def implementation_hashes():
    result = previous.implementation_hashes()
    result.update(step_hashes())
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def replay_completed_feasible(prepared, prior, *, artificial=False):
    restored, bindings, tenth, old_replay, old_pool = prepared
    problem, initial, gate, lower, upper, source_cfg, old_cfg, old_init = restored
    if (prior.get('schema') != previous.SCHEMA
            or prior.get('status') != 'complete-pooled-feasibility-actual-curvature-exchange-audit'
            or bool(prior.get('artificial_inputs_only')) != bool(artificial)):
        raise ValueError('the completed matching pooled-feasibility curvature report is required')
    if (prior.get('source_files_sha256') != previous.implementation_hashes()
            or prior.get('configuration') != old_cfg):
        raise ValueError('the completed feasible-curvature sources or configuration differ')
    if not artificial and (str(prior.get('github_run_id')) != PRIOR_RUN
            or prior.get('github_sha') != PRIOR_SOURCE):
        raise ValueError('the twelfth report source/run differs')
    for name, binding in bindings.items():
        recorded = prior.get('exact_input_storage', {}).get(name, {})
        for key in ['decoded_sha256', 'decoded_bytes', 'stored_sha256', 'stored_bytes', 'gzip_storage']:
            if recorded.get(key) != binding.get(key):
                raise ValueError('twelfth report preceding input binding differs: '+name+'/'+key)
    expected = state_record(problem, initial)
    if (prior.get('input_replay') != old_replay or prior.get('initial_state') != expected
            or prior.get('final_state') != expected):
        raise ValueError('the start must be the unchanged complete accepted e407 state')
    if (not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_optimizer_calls_this_run') != 0
            or prior.get('old_failed_metric_auxiliary_delta') != tenth['selected_raw_auxiliary_delta']):
        raise ValueError('the original fixed g/b0 or optimizer history differs')
    radial, theta, grid = curvature_grid(tenth)
    if prior.get('full_value_sampling_definition') != grid:
        raise ValueError('the completed feasible report belongs to a different exact value grid')
    stage = prior['curvature_exchange_stage']
    checkpoint = stage['checkpoint']
    point = checkpoint.get('best_physical_curvature_point')
    if (not point or point.get('physical_state_sha256') != digest(problem.identity(initial))
            or point.get('exact_binary64_physical_coefficients') != coefficients(initial)
            or np.asarray(point.get('physical_parameter_coefficients_binary64'), float).tobytes() != initial.tobytes()):
        raise ValueError('the accepted point is not exactly the restored physical coefficient vector')
    for name in ['final_full_grid_constraints', 'final_doubled_constraints']:
        decision = prior.get(name, {})
        if not decision.get('eligible_under_fixed_metric_and_physical_gates'):
            raise ValueError('the published accepted state must pass both original value grids')
        for key in ['fixed_metric_budget_exact', 'hard_strip_half_width_exact', 'mirror_target_exact']:
            if decision.get(key) != old_cfg[key]:
                raise ValueError('a fixed geometric gate changed: '+key)
    history = checkpoint.get('active_row_pool_history', [])
    if not history:
        raise ValueError('the completed feasible report has no saved row pool')
    last = history[-1]
    indices = last.get('row_indices')
    if (not isinstance(indices, list) or not indices or any(type(i) is not int for i in indices)
            or indices != sorted(set(indices)) or last.get('row_count') != len(indices)
            or last.get('row_indices_sha256') != digest(indices)
            or last.get('group_order') != list(GROUPS)
            or last.get('flat_index_rule') != 'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'
            or last.get('total_full_grid_rows') != len(GROUPS)*len(radial)*len(theta)
            or min(indices) < 0 or max(indices) >= len(GROUPS)*len(radial)*len(theta)
            or len(indices) > old_cfg['max_pool_rows'] or not set(old_pool).issubset(indices)):
        raise ValueError('twelfth learned row pool indices, hash, coverage or ordering differ')
    cfg = configuration(old_cfg)
    learned = {
        'schema':'twelfth-report-exact-same-grid-learned-row-pool-v1',
        'original_source_run':prior.get('github_run_id'), 'original_source_commit':prior.get('github_sha'),
        'source_pool_version':last['version'], 'source_pool_rows':len(indices),
        'source_row_indices_sha256':last['row_indices_sha256'],
        'source_full_value_grid_sha256':grid['definition_sha256'],
        'all_preceding_enforced_rows_retained':True,
        'old_ineligible_or_unsaved_trials_are_not_initializers':True,
        'pool_is_an_evaluation_choice_not_a_physical_field':True,
    }
    retained = {
        'schema':prior['schema'], 'status':stage['status'],
        'source_run':prior.get('github_run_id'), 'source_commit':prior.get('github_sha'),
        'physical_evaluations':checkpoint.get('physical_geometry_evaluations'),
        'final_physical_state_sha256':expected['canonical_physical_state_sha256'],
        'old_raw_auxiliary_lambda':prior['selected_raw_auxiliary_lambda'],
        'old_raw_auxiliary_zeta':prior['selected_raw_auxiliary_zeta'],
        'failed_lowest_lambda_trial_is_not_reused':True,
        'no_near_feasible_unsaved_coefficients_are_reconstructed_or_invented':True,
        'published_final_coarse_decision':copy.deepcopy(prior['final_full_grid_constraints']),
        'published_final_fine_decision':copy.deepcopy(prior['final_doubled_constraints']),
    }
    replay = {
        'schema':'twelve-input-fixed-target-short-step-start-replay-v1',
        'eleven_input_replay':old_replay,
        'complete_metric_sha256':problem.metric_model(initial)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'canonical_physical_state_sha256':digest(problem.identity(initial)),
        'physical_parameter_count':problem.nunknown,
        'same_accepted_exact_coefficients':True,
        'same_complete_g_height_reference_and_value_grid':True,
        'learned_pool':learned, 'completed_feasible_attempt_retained':retained,
        'new_short_step_policy':POLICY,
        'fixed_target_lambda_exact':cfg['fixed_curvature_target_exact'],
        'target_is_not_a_physical_coefficient_or_old_converged_bound':True,
        'old_optimizer_calls_replayed':0,
        'no_research_geometry_during_structural_replay':True,
    }
    return (problem, initial, gate, lower, upper, source_cfg, cfg), replay, np.asarray(indices, dtype=np.int64)


def prepare_run(args, *, artificial=False, process_started=None):
    start = time.monotonic()
    process_started = start if process_started is None else process_started
    phase = 'eleven-input-accepted-state-replay'
    bindings = {}
    try:
        if not artificial:
            paths = [args.input, args.anchor_input, args.short_audit, args.height_audit,
                args.prior_joint_audit, args.resume_audit, args.epigraph_audit, args.trial_audit,
                args.dense_audit, args.exchange_audit, args.curvature_audit, args.feasible_curvature_audit]
            require_public_actions(os.environ.get('GITHUB_ACTIONS'), os.environ.get('GITHUB_REPOSITORY'), paths)
        old = previous.prepare_run(args, artificial=artificial, process_started=process_started)
        bindings = copy.deepcopy(old[1])
        phase = 'twelfth-completed-feasible-curvature-byte-binding'
        if args.feasible_curvature_audit is None or args.expected_feasible_curvature_sha256 is None:
            raise ValueError('the twelfth feasible-curvature report and decoded SHA are required')
        prior, raw, binding = read_input(args.feasible_curvature_audit, args.expected_feasible_curvature_sha256)
        phase = 'twelfth-accepted-state-and-row-pool-replay'
        restored, replay, pool = replay_completed_feasible(old, prior, artificial=artificial)
        bindings['completed_pooled_feasible_curvature_exchange'] = binding
        return restored, bindings, old[2], replay, pool
    except Exception as error:
        report = {'schema':SCHEMA, 'status':'input-replay-failed-before-fixed-target-geometry',
            'phase':phase, 'source_files_sha256':implementation_hashes(), 'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial), 'old_optimizer_calls_this_run':0, 'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-start,
            'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__, 'message':str(error)}}
        save_report(args.out, report)
        raise


def compact_point(point):
    if point is None:
        return None
    return {k:copy.deepcopy(v) for k, v in point.items()
            if k not in ['exact_binary64_physical_coefficients', 'physical_parameter_coefficients_binary64']}


def small_summary(report, out):
    keys = ['schema', 'status', 'phase', 'source_files_sha256', 'configuration',
        'github_sha', 'github_run_id', 'github_repository', 'artificial_inputs_only',
        'old_optimizer_calls_this_run', 'old_failed_metric_auxiliary_delta',
        'learned_pool_replay', 'completed_feasible_attempt_retained',
        'fixed_curvature_target_definition', 'initial_current_constraints', 'initial_doubled_constraints',
        'final_full_grid_constraints', 'final_doubled_constraints', 'final_selection_validation',
        'elapsed_seconds', 'run_audit_elapsed_seconds', 'prepare_elapsed_seconds',
        'process_total_elapsed_seconds', 'optimization_active_seconds', 'process_clock_scope',
        'peak_rss_kib_linux', 'value_evaluation_counts',
        'unchanged_complete_metric_and_height_reference', 'error', 'limitations']
    result = {k:copy.deepcopy(report[k]) for k in keys if k in report}
    result['exact_input_storage'] = {name:{k:v for k,v in binding.items()
        if k in ['decoded_sha256', 'decoded_bytes', 'stored_sha256', 'stored_bytes', 'gzip_storage']}
        for name,binding in report.get('exact_input_storage',{}).items()}
    for key in ['initial_state', 'final_state']:
        if key in report:
            result[key] = previous.previous.compact_state(report[key])
    for key in ['initial_full_grid_audit', 'final_full_grid_audit', 'final_doubled_angle_audit']:
        if key in report:
            result[key] = previous.previous.compact_audit(report[key])
    if 'same_parameter_Pi_refinement' in report:
        result['same_parameter_Pi_refinement'] = previous.previous.compact_comparison(report['same_parameter_Pi_refinement'])
    if 'full_value_sampling_definition' in report:
        grid = report['full_value_sampling_definition']
        result['full_value_sampling_definition'] = {k:grid[k]
            for k in ['schema', 'definition_sha256', 'radial_count', 'angular_nodes']}
    stage = report.get('fixed_target_short_step_stage')
    if stage:
        item = {k:copy.deepcopy(v) for k,v in stage.items() if k not in ['checkpoint', 'solver']}
        item['solver'] = {k:copy.deepcopy(v) for k,v in stage['solver'].items() if k != 'models'}
        item['models'] = []
        for old in stage['solver'].get('models',[]):
            model = {k:copy.deepcopy(v) for k,v in old.items() if k not in ['exact_binary64_proposed_step', 'trials']}
            model['trials'] = []
            for trial in old.get('trials',[]):
                entry = {k:copy.deepcopy(v) for k,v in trial.items()
                    if k not in ['coarse_decision', 'fine_decision', 'exact_binary64_physical_coefficients']}
                for key in ['coarse_decision', 'fine_decision']:
                    d = trial.get(key)
                    if d:
                        entry[key] = {k:d[k] for k in [
                            'eligible_under_fixed_metric_and_physical_gates', 'direct_max_eta',
                            'direct_maximum_absolute_principal_curvature', 'direct_curvature_minus_lambda'] if k in d}
                model['trials'].append(entry)
            item['models'].append(model)
        snap = stage['checkpoint']
        names = ['physical_geometry_evaluations', 'doubled_angle_full_value_evaluations',
            'total_full_value_physical_evaluations', 'epigraph_vector_evaluations',
            'jacobian_geometry_batches', 'jacobian_refreshes', 'total_elapsed_seconds',
            'initialization_elapsed_seconds', 'optimization_elapsed_seconds',
            'value_geometry_seconds', 'doubled_angle_value_seconds', 'jacobian_geometry_seconds',
            'pool_Jacobian_including_refresh_seconds', 'maximum_geometry_cache_array_bytes',
            'maximum_retained_selected_derivative_bytes', 'maximum_returned_batch_Jacobian_bytes',
            'maximum_single_constraint_Jacobian_bytes', 'maximum_batch_query_radial_rows',
            'maximum_same_state_batch_ordinary_jet_difference', 'same_state_batch_ordinary_jet_differences_by_field',
            'no_full_grid_constraint_Jacobian_formed', 'full_grid_two_jet_Jacobian_was_requested']
        item['checkpoint'] = {k:snap[k] for k in names if k in snap}
        item['checkpoint']['selected_two_grid_physical_point'] = compact_point(snap.get('selected_two_grid_physical_point'))
        item['checkpoint']['accepted_iterates'] = [compact_point(p) for p in snap.get('accepted_iterates',[])]
        item['checkpoint']['all_full_trial_coefficients_are_in_full_report'] = True
        item['checkpoint']['saved_coarse_trial_count'] = len(snap.get('saved_coarse_trials',[]))
        item['checkpoint']['saved_fine_trial_count'] = len(snap.get('saved_fine_trials',[]))
        result['fixed_target_short_step_stage'] = item
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
    scope = ('main entrance including twelve-input loader and restoration' if process_started is not None
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
        'completed_feasible_attempt_retained':replay['completed_feasible_attempt_retained'],
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
            optimization_active_seconds=report.get('fixed_target_short_step_stage',{}).get('checkpoint',{}).get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('twelve-inputs-replayed-before-fixed-target-short-step-geometry')
    try:
        report['phase'] = 'two-grid-physical-initialization-outside-active-optimization-clock'
        radial, theta, grid = curvature_grid(tenth)
        order = int(source_cfg['primitive_order'])
        report['full_value_sampling_definition'] = grid
        def checkpoint(snapshot):
            report['fixed_target_short_step_stage'] = {
                'status':'current-fixed-target-checkpoint', 'checkpoint':snapshot, 'solver':{}}
            save('fixed-target-two-grid-short-step-checkpoint')
        objective = FeasibleStepObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(
            complete_value_sampling_definition=grid,
            twelfth_report_decoded_sha256=bindings['completed_pooled_feasible_curvature_exchange']['decoded_sha256'],
            learned_pool_replay=replay['learned_pool'], old_metric_delta_and_curvature_lambda_are_history_only=True)
        objective.evaluation_sha256 = digest(objective.evaluation_definition)
        objective.set_pool(learned_pool, {'kind':'same-grid-pool-retained-from-twelfth-completed-report',
            'source':replay['learned_pool']})
        first = objective.evaluate(np.r_[initial,zeta])
        report['initial_current_constraints'] = copy.deepcopy(first['decision'])
        report['initial_full_grid_audit'] = audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints'] = copy.deepcopy(objective.fine_decision(initial))
        save('complete-initial-two-grid-physical-and-fixed-target-diagnostics')
        report['phase'] = 'fixed-target-linear-proposals-with-two-grid-acceptance'
        stage = run_feasible_steps(objective,initial,artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['fixed_target_short_step_stage'] = stage
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
        save('complete-fixed-target-two-grid-short-step-audit' if eligible
             else 'final-same-state-value-recheck-failed-do-not-use-as-new-warm-start')
        return report
    except Exception as error:
        report['error'] = {'type':type(error).__name__, 'message':str(error), 'traceback':traceback.format_exc()}
        save('fixed-target-short-step-audit-error-checkpoints-preserved')
        return report


def artificial_twelve_inputs(directory):
    """Only artificial fixtures; preceding source stages are evaluation-only."""
    p = previous.previous
    args, unused, seventh = p.artificial_seven_inputs(directory)
    saved = p.prepare_saved(args,artificial=True)
    p.run_saved(saved,args.out,artificial=True)
    args.trial_audit=args.out; args.expected_trial_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    args.out=directory/'dense-source-artificial.json'
    dense=p.prepare_dense(args,artificial=True)
    p.run_dense(dense,args.out,artificial=True,evaluate_only=True)
    args.dense_audit=args.out; args.expected_dense_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    args.out=directory/'exchange-source-artificial.json'
    exchange=p.prepare_exchange(args,artificial=True)
    p.run_metric_exchange(exchange,args.out,artificial=True,evaluate_only=True)
    args.exchange_audit=args.out; args.expected_exchange_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    args.out=directory/'completed-curvature-artificial.json'
    ten=p.prepare_run(args,artificial=True)
    p.run_audit(ten,args.out,artificial=True,evaluate_only=True)
    args.curvature_audit=args.out; args.expected_curvature_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    args.out=directory/'completed-feasible-curvature-artificial.json'
    eleven=previous.prepare_run(args,artificial=True)
    prior=previous.run_audit(eleven,args.out,artificial=True,evaluate_only=True)
    if prior.get('status')!='complete-pooled-feasibility-actual-curvature-exchange-audit':
        raise ArithmeticError('artificial twelfth source fixture failed')
    args.feasible_curvature_audit=args.out
    args.expected_feasible_curvature_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
    return args,eleven,prior


def developer_check():
    targeted = steps_check()
    with tempfile.TemporaryDirectory(prefix='curvature-fixed-target-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder)
        args,eleven,prior=artificial_twelve_inputs(directory)
        args.out=directory/'fixed-target-artificial.json'
        flow=time.monotonic()
        prepared=prepare_run(args,artificial=True,process_started=flow)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=flow,prepare_seconds=time.monotonic()-flow)
        snap=report.get('fixed_target_short_step_stage',{}).get('checkpoint',{})
        same=report.get('final_state')==prior['final_state']
        no_old=report.get('old_optimizer_calls_this_run')==0
        no_lp=report.get('fixed_target_short_step_stage',{}).get('solver',{}).get('linear_program_invocation_count')==0
        pool_kept=set(prior['curvature_exchange_stage']['checkpoint']['active_row_pool_history'][-1]['row_indices']).issubset(
            snap.get('active_row_pool_history',[{}])[0].get('row_indices',[]))
        source=report.get('source_files_sha256')==implementation_hashes()
        summary=json.loads(summary_path(args.out).read_text())
        summary_bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        allcoeff=all(len(x['exact_binary64_physical_coefficients'])==prepared[0][0].nunknown
            for x in snap.get('saved_coarse_trials',[])+snap.get('saved_fine_trials',[]))
        wrong=copy.copy(args); wrong.out=directory/'wrong-twelfth-sha.json'; wrong.expected_feasible_curvature_sha256='0'*64
        try:
            prepare_run(wrong,artificial=True); bad_sha=False
        except ValueError:
            fail=json.loads(wrong.out.read_text())
            bad_sha=fail['phase']=='twelfth-completed-feasible-curvature-byte-binding' and fail['new_solver_calls']==0
        bad=copy.deepcopy(prior); bad['final_state']['canonical_physical_state_sha256']='0'*64
        try:
            replay_completed_feasible(eleven,bad,artificial=True); bad_state=False
        except ValueError: bad_state=True
        bad=copy.deepcopy(prior)
        bad['curvature_exchange_stage']['checkpoint']['active_row_pool_history'][-1]['row_indices'][0]=-1
        try:
            replay_completed_feasible(eleven,bad,artificial=True); bad_pool=False
        except ValueError: bad_pool=True
        status=report['status']; error=report.get('error')
        ref=report.get('same_parameter_Pi_refinement')
    passed=bool(targeted['passed'] and same and no_old and no_lp and pool_kept and source
        and summary_bound and allcoeff and bad_sha and bad_state and bad_pool
        and status=='complete-fixed-target-two-grid-short-step-audit')
    return {'schema':'fixed-target-two-grid-short-step-development-v1',
        'artificial_inputs_only':True, 'research_geometry_evaluated_or_optimized':False,
        'no_Actions_environment_forged':True, 'targeted_short_step_checks':targeted,
        'complete_twelve_input_main_status':status, 'complete_main_error':error,
        'no_preceding_optimizer_replayed':no_old, 'artificial_IO_has_no_LP':no_lp,
        'accepted_exact_state_and_freeze_unchanged':same, 'learned_rows_retained':pool_kept,
        'all_evaluated_states_saved_with_complete_exact_coefficients':allcoeff,
        'source_hashes_match':source, 'summary_binds_full_bytes':summary_bound,
        'wrong_twelfth_SHA_saves_failure':bad_sha, 'wrong_final_state_rejected':bad_state,
        'wrong_pool_index_rejected':bad_pool, 'same_state_angle_refinement':ref, 'passed':passed}


def main():
    process_started=time.monotonic()
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['input','anchor-input','short-audit','height-audit','prior-joint-audit','resume-audit',
                 'epigraph-audit','trial-audit','dense-audit','exchange-audit','curvature-audit','feasible-curvature-audit']:
        parser.add_argument('--'+name,type=Path)
    for name in ['input','anchor','short','height','prior-joint','resume','epigraph','trial','dense','exchange',
                 'curvature','feasible-curvature']:
        parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:
            result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'fixed-target-short-step-development-error-v1',
                'passed':False,'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-process_started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(),
            process_total_elapsed_seconds=time.monotonic()-process_started)
        atomic_save(args.out,result)
        print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']: raise SystemExit(1)
        return
    start=time.monotonic()
    try:
        prepared=prepare_run(args,process_started=process_started)
    except Exception:
        raise SystemExit(1)
    report=run_audit(prepared,args.out,process_started=process_started,prepare_seconds=time.monotonic()-start)
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)
    if report['status']!='complete-fixed-target-two-grid-short-step-audit':
        raise SystemExit(1)


if __name__=='__main__':
    main()

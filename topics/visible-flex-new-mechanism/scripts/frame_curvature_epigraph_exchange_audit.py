#!/usr/bin/env python3
"""One actual-curvature row-exchange stage at a fixed direct-metric budget.

Ten byte-bound reports restore the existing physical field. No old optimizer
is called. Initial lambda comes from the two published curvature diagnostics;
the old failed metric delta remains provenance. The new solver uses complete
384-angle value gates and small radial batches of full two-jet derivatives.
Final 384/768 evaluations keep all physical coefficients and raw lambda fixed.
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
from frame_entry_short_bounded_audit import (read_input, audit_data, compare_data,
    compact_audit, compact_state, compact_comparison)
from frame_independent_height_solve import state_record
from frame_metric_epigraph_trial_audit import (artificial_seven_inputs,
    prepare_run as prepare_saved, run_audit as run_saved)
from frame_metric_epigraph_dense_audit import (prepare_run as prepare_dense,
    run_restart as run_dense)
from frame_metric_epigraph_exchange_audit import (prepare_run as prepare_exchange,
    run_audit as run_metric_exchange, exchange_grid,
    implementation_hashes as exchange_audit_hashes, SCHEMA as EXCHANGE_SCHEMA)
from frame_metric_epigraph_exchange import configuration as exchange_configuration
from frame_curvature_epigraph_exchange import (CurvatureExchangeObjective,
    configuration, candidate_decision, run_exchange, curvature_forms,
    developer_check as array_check, implementation_hashes as curvature_hashes)

SCHEMA = 'same-g-fixed-metric-budget-curvature-row-exchange-audit-v1'


def implementation_hashes():
    result = exchange_audit_hashes()
    result.update(curvature_hashes())
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def coefficients(values):
    return [str(Q.from_float(float(x))) for x in values]


def expected_exchange_configuration(artificial):
    cfg = exchange_configuration()
    if artificial:
        cfg.update(minimum_signed_height_exact='-10', hard_ball_radius_exact='10',
            hard_strip_half_width_exact='999/100', outer_strip_half_width_exact='10',
            strip_inner_margin_exact='1/100', mirror_target_exact='1/1000000000000',
            normal_area_numerical_floor=0., maxiter=2, max_physical_evaluations=6, max_seconds=120.)
    return cfg


def run_configuration(artificial=False):
    cfg = configuration()
    if artificial:
        cfg.update(fixed_metric_budget_exact='100000', minimum_signed_height_exact='-10',
            hard_ball_radius_exact='10', hard_strip_half_width_exact='999/100',
            outer_strip_half_width_exact='10', strip_inner_margin_exact='1/100',
            mirror_target_exact='1/1000000000000', normal_area_numerical_floor=0.,
            radial_Jacobian_batch_owned_rows=2,
            maxiter=2, max_physical_evaluations=6, max_seconds=120.)
    return cfg


def stored_curvature_maxima(report):
    names = ['final_full_grid_audit', 'final_doubled_angle_audit']
    result = {}
    for name in names:
        full = report.get(name, {}).get('full', {})
        value = full.get('extrema', {}).get('principal_curvature_absolute', {}).get('magnitude')
        if value is None or not np.isfinite(float(value)) or float(value) < 0:
            raise ValueError('two finite published actual-curvature maxima required')
        result[name] = float(value)
    return result


def initial_lambda_definition(report, cfg):
    values = stored_curvature_maxima(report)
    maximum = max(values.values())
    margin = float(Q(cfg['curvature_initial_margin_exact']))
    proposed = maximum + (1+maximum)*margin
    if proposed < float(Q(cfg['curvature_lambda_min_exact'])):
        proposed = 2*float(Q(cfg['curvature_lambda_min_exact']))
    return {
        'source_curvature_maxima': values,
        'maximum_of_both_published_angle_grids': maximum,
        'relative_margin_exact': cfg['curvature_initial_margin_exact'],
        'operation': 'max_kappa + (1+max_kappa)*float(exact_margin)',
        'proposed_lambda_evaluated': proposed,
        'proposed_lambda_exact_binary64': str(Q.from_float(proposed)),
        'curvature_scale_exact': cfg['curvature_scale_exact'],
        'old_metric_delta_is_not_used_for_lambda': True,
        'current_full_grid_replay_must_independently_pass_this_bound': True,
    }


def replay_exchange_report(prepared, report, *, artificial=False):
    restored, bindings, ninth, prior_replay = prepared
    problem, start, prior_delta, gate, lower, upper, work_cfg, source_cfg = restored
    if (report.get('schema') != EXCHANGE_SCHEMA
            or report.get('status') != 'complete-shared-budget-full-grid-row-exchange-audit'
            or bool(report.get('artificial_inputs_only')) != bool(artificial)):
        raise ValueError('completed matching tenth full-grid exchange report required')
    if report.get('source_files_sha256') != exchange_audit_hashes():
        raise ValueError('tenth report frozen implementation differs')
    if report.get('configuration') != expected_exchange_configuration(artificial):
        raise ValueError('tenth report exchange configuration differs')
    for key, binding in bindings.items():
        previous = report.get('exact_input_storage', {}).get(key, {})
        for field in ['decoded_sha256', 'decoded_bytes', 'stored_sha256', 'stored_bytes', 'gzip_storage']:
            if previous.get(field) != binding.get(field):
                raise ValueError('tenth input binding differs: '+key+'/'+field)
    if (report.get('input_replay') != prior_replay
            or report.get('initial_state') != state_record(problem, start)):
        raise ValueError('tenth initial complete physical/evaluation state differs')
    if (report.get('old_optimizer_calls_this_run') != 0
            or not report.get('unchanged_complete_metric_and_height_reference')
            or report.get('old_raw_auxiliary_delta') != prior_delta):
        raise ValueError('tenth report changed the old history or full metric/reference')
    unused_r, unused_theta, expected_grid = exchange_grid(ninth, source_cfg['angular_nodes'])
    if report.get('full_value_sampling_definition') != expected_grid:
        raise ValueError('tenth complete exact full value grid differs')
    stage = report.get('exchange_stage', {})
    point = stage.get('checkpoint', {}).get('best_physical_max_eta_point')
    if not point:
        raise ValueError('tenth report has no saved whole-grid physical best')
    state = np.asarray(point.get('physical_parameter_coefficients_binary64'), float)
    if state.shape != (problem.nunknown,) or not np.all(np.isfinite(state)):
        raise ValueError('complete finite tenth physical coefficients required')
    if coefficients(state) != point.get('exact_binary64_physical_coefficients'):
        raise ValueError('tenth exact physical coefficient roundtrip failed')
    identity = problem.identity(state)
    if (point.get('physical_state_sha256') != digest(identity)
            or report.get('final_state') != state_record(problem, state)
            or problem.metric_model(state) != problem.metric_model(start)):
        raise ValueError('tenth selected full identity, fixed g, or coefficient layout differs')
    raw_delta = float(Q(point['auxiliary_delta_exact_binary64']))
    if (raw_delta != point.get('auxiliary_delta_evaluated')
            or raw_delta != report.get('selected_raw_auxiliary_delta')
            or not report.get('selected_auxiliary_not_inflated_at_final_audit')):
        raise ValueError('tenth saved raw metric delta or its failure history changed')
    if not point.get('record', {}).get('decision', {}).get('eligible_under_physical_gates_including_mirror'):
        raise ValueError('tenth saved selection did not pass its complete work-grid physical screen')
    cfg = run_configuration(artificial)
    bar = float(Q(cfg['fixed_metric_budget_exact']))
    decisions = {}
    for key in ['final_full_grid_constraints', 'final_doubled_constraints']:
        decision = report.get(key, {})
        if not decision.get('eligible_under_physical_gates_including_mirror'):
            raise ValueError('both published angle grids must pass all inner-strip and mirror physical gates')
        if (decision.get('hard_strip_half_width_exact') != cfg['hard_strip_half_width_exact']
                or decision.get('mirror_target_exact') != cfg['mirror_target_exact']):
            raise ValueError('the preserved physical gate definitions differ')
        if not np.isfinite(decision.get('direct_max_eta', np.nan)) or decision['direct_max_eta'] > bar+cfg['direct_eta_tolerance']:
            raise ValueError('published angle-grid eta exceeds the explicit fixed curvature-stage metric budget')
        decisions[key] = copy.deepcopy(decision)
    lam = initial_lambda_definition(report, cfg)
    replay = {
        'schema': 'ten-input-actual-curvature-start-replay-v1',
        'complete_metric_sha256': problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256': digest(problem.height_base_definition),
        'canonical_physical_state_sha256': digest(identity),
        'physical_parameter_count': problem.nunknown,
        'all_coefficients_and_layout_exactly_replayed': True,
        'both_source_angle_grids_pass_inner_strip_and_existing_physical_gates': True,
        'source_physical_and_auxiliary_decisions_preserved': decisions,
        'old_failed_metric_delta_evaluated': raw_delta,
        'old_failed_metric_delta_exact_binary64': str(Q.from_float(raw_delta)),
        'new_fixed_metric_budget_exact': cfg['fixed_metric_budget_exact'],
        'new_curvature_initialization': lam,
        'old_optimizer_calls_replayed': 0,
        'no_research_geometry_during_structural_replay': True,
        'curvature_auxiliary_is_new_not_a_reinterpretation_of_old_metric_delta': True,
    }
    return (problem, state, gate, lower, upper, source_cfg, cfg, lam), replay


def curvature_grid(report):
    source = copy.deepcopy(report['full_value_sampling_definition'])
    stored_hash = source.pop('definition_sha256')
    if digest(source) != stored_hash:
        raise ValueError('tenth exact value-grid hash does not match its full definition')
    nodes = [Q(x) for x in source['radial_nodes_exact']]
    count = int(source['angular_nodes'])
    if (not nodes or nodes[0] != 0 or any(y <= x for x, y in zip(nodes, nodes[1:]))
            or len(nodes) != source['radial_count'] or count < 4 or count % 4):
        raise ValueError('complete strictly increasing radial grid and uniform periodic angular count required')
    radial = np.asarray([float(x) for x in nodes])
    if np.any(np.diff(radial) <= 0):
        raise ValueError('exact radial nodes collapse in binary64 evaluation')
    theta = np.arange(count)*2*np.pi/count
    definition = {
        'schema': 'same-full-value-grid-for-fixed-metric-curvature-exchange-v1',
        'source_exchange_grid_sha256': stored_hash,
        'radial_nodes_exact': [str(x) for x in nodes],
        'radial_count': len(nodes), 'angular_nodes': count,
        'theta_definition': '2*pi*j/N, complete uniform periodic grid',
        'all_value_gates_use_every_point_at_every_trial': True,
        'selected_Jacobian_batches_change_no_value_grid_point': True,
    }
    definition['definition_sha256'] = digest(definition)
    return radial, theta, definition


def summary_path(out):
    return out.with_name(out.stem+'-summary.json')


def small_summary(report, out):
    keys = ['schema', 'status', 'phase', 'source_files_sha256', 'configuration', 'exact_input_storage',
        'input_replay', 'github_sha', 'github_run_id', 'github_repository', 'artificial_inputs_only',
        'old_optimizer_calls_this_run', 'old_failed_metric_auxiliary_delta', 'new_curvature_initialization',
        'elapsed_seconds', 'run_audit_elapsed_seconds', 'prepare_elapsed_seconds', 'process_total_elapsed_seconds',
        'optimization_active_seconds', 'process_clock_scope', 'peak_rss_kib_linux',
        'initial_current_constraints', 'final_full_grid_constraints', 'final_doubled_constraints',
        'selected_raw_auxiliary_zeta', 'selected_raw_auxiliary_lambda',
        'unchanged_complete_metric_and_height_reference', 'error', 'limitations']
    result = {key: report[key] for key in keys if key in report}
    for key in ['initial_state', 'final_state']:
        if key in report:
            result[key] = compact_state(report[key])
    for key in ['initial_full_grid_audit', 'final_full_grid_audit', 'final_doubled_angle_audit']:
        if key in report:
            result[key] = compact_audit(report[key])
    if 'same_parameter_Pi_refinement' in report:
        result['same_parameter_Pi_refinement'] = compact_comparison(report['same_parameter_Pi_refinement'])
    if 'full_value_sampling_definition' in report:
        grid = report['full_value_sampling_definition']
        result['full_value_sampling_definition'] = {k:grid[k] for k in ['schema','definition_sha256','radial_count','angular_nodes']}
    stage = report.get('curvature_exchange_stage')
    if stage:
        result['curvature_exchange_stage'] = {key:stage.get(key) for key in ['status','error','budget_message','selected_point']}
        solver = stage.get('solver', {})
        result['curvature_exchange_stage']['solver'] = {k:v for k,v in solver.items() if k != 'rounds'}
        rounds = []
        for old in solver.get('rounds', []):
            rd = {k:v for k,v in old.items() if k not in ['initial_vector_exact','pool_addition']}
            addition = old.get('pool_addition')
            if addition:
                rd['pool_addition'] = {k:addition.get(k) for k in ['version','row_count','row_indices_sha256','omitted_violations_after_this_addition']}
            rounds.append(rd)
        result['curvature_exchange_stage']['solver']['rounds'] = rounds
        snap = stage.get('checkpoint', {})
        result['curvature_exchange_stage']['checkpoint'] = {k:snap.get(k) for k in [
            'physical_geometry_evaluations','epigraph_vector_evaluations','jacobian_geometry_batches','jacobian_refreshes',
            'total_elapsed_seconds','initialization_elapsed_seconds','optimization_elapsed_seconds',
            'value_geometry_seconds','jacobian_geometry_seconds','pool_Jacobian_including_refresh_seconds',
            'maximum_geometry_cache_array_bytes','maximum_retained_selected_derivative_bytes',
            'maximum_returned_batch_Jacobian_bytes','maximum_single_constraint_Jacobian_bytes',
            'maximum_batch_query_radial_rows','maximum_same_state_batch_ordinary_jet_difference',
            'same_state_batch_ordinary_jet_differences_by_field','no_full_grid_constraint_Jacobian_formed',
            'full_grid_two_jet_Jacobian_was_requested','all_selected_points_screened_on_whole_value_grid']}
        for key in ['best_physical_curvature_point','best_auxiliary_feasible_lambda_point',
                    'best_auxiliary_feasible_curvature_point','lowest_lambda_trial_may_be_ineligible']:
            item = snap.get(key)
            result['curvature_exchange_stage']['checkpoint'][key] = None if item is None else {
                k:v for k,v in item.items() if k not in ['physical_parameter_coefficients_binary64','exact_binary64_physical_coefficients']}
    raw = out.read_bytes()
    result['full_report'] = {'path':str(out), 'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest(),
        'summary_omits_large_canonical_fields_and_distributions_not_the_complete_deliverable':True}
    return result


def save_report(out, report):
    atomic_save(out, report)
    atomic_save(summary_path(out), small_summary(report, out))


def prepare_run(args, *, artificial=False, process_started=None):
    started = time.monotonic()
    process_started = started if process_started is None else process_started
    bindings = {}
    phase = 'ten-input-public-repository-guard'
    try:
        if args.exchange_audit is None or not args.expected_exchange_sha256:
            raise ValueError('explicit tenth report path and decoded SHA256 required')
        paths = [args.input,args.anchor_input,args.short_audit,args.height_audit,args.prior_joint_audit,
            args.resume_audit,args.epigraph_audit,args.trial_audit,args.dense_audit,args.exchange_audit]
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        phase = 'tenth-exchange-report-byte-binding'
        tenth, raw, binding = read_input(args.exchange_audit, args.expected_exchange_sha256)
        bindings['completed_full_grid_metric_exchange'] = binding
        phase = 'unchanged-nine-input-replay'
        previous = prepare_exchange(args, artificial=artificial, process_started=process_started)
        bindings.update(previous[1])
        phase = 'tenth-physical-inner-strip-fixed-metric-and-two-angle-curvature-replay'
        restored, replay = replay_exchange_report(previous, tenth, artificial=artificial)
        return restored, bindings, tenth, replay
    except Exception as error:
        report = {'schema':SCHEMA,'status':'input-replay-failed-before-curvature-research-geometry','phase':phase,
            'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-started,'run_audit_elapsed_seconds':0.,
            'process_total_elapsed_seconds':time.monotonic()-process_started,'optimization_active_seconds':0.,
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out, report)
        raise


def run_audit(prepared, out, *, artificial=False, evaluate_only=False, process_started=None, prepare_seconds=None):
    restored, bindings, tenth, replay = prepared
    problem, initial, gate, lower, upper, source_cfg, cfg, initialization = restored
    started = time.monotonic()
    scope = ('main entrance including the ten-input loader and object restoration' if process_started is not None
        else 'direct run_audit entrance; artificial fixtures constructed outside this clock')
    process_started = started if process_started is None else process_started
    metric = copy.deepcopy(problem.metric_model(initial))
    b0 = copy.deepcopy(problem.height_base_definition)
    report = {'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':0,'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':state_record(problem,initial),'unchanged_complete_metric_and_height_reference':True,
        'process_clock_scope':scope,'prepare_elapsed_seconds':None if prepare_seconds is None else float(prepare_seconds)}
    def save(status):
        now = time.monotonic()
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=report.get('curvature_exchange_stage',{}).get('checkpoint',{}).get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('ten-inputs-replayed-before-new-curvature-geometry')
    try:
        report['phase'] = 'full-grid-curvature-initialization-outside-optimization-clock'
        radial, theta, grid = curvature_grid(tenth)
        order = int(source_cfg['primitive_order'])
        report['full_value_sampling_definition'] = grid
        def checkpoint(snapshot):
            report['curvature_exchange_stage'] = {'status':'current-curvature-exchange-checkpoint','checkpoint':snapshot}
            save('whole-grid-curvature-exchange-checkpoint')
        objective = CurvatureExchangeObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(tenth_input_decoded_sha256=bindings['completed_full_grid_metric_exchange']['decoded_sha256'],
            complete_value_sampling_definition=grid,old_metric_delta_is_history_only=True)
        objective.evaluation_sha256 = digest(objective.evaluation_definition)
        proposal = float(initialization['proposed_lambda_evaluated'])
        vector = objective.initial_vector(initial, proposal)
        first = objective.evaluate(vector)
        report['new_curvature_initialization'] = copy.deepcopy(initialization)
        report['new_curvature_initialization'].update(
            solver_zeta_evaluated=float(vector[-1]),
            solver_zeta_exact_binary64=str(Q.from_float(float(vector[-1]))),
            effective_lambda_after_scaled_binary64_roundtrip=float(vector[-1])*float(Q(cfg['curvature_scale_exact'])),
            ordinary_replayed_curvature_maximum=first['decision']['direct_maximum_absolute_principal_curvature'],
            old_failed_metric_delta_unchanged=tenth['selected_raw_auxiliary_delta'],
            auxiliary_is_not_a_physical_coefficient=True)
        report['initial_current_constraints'] = first['decision']
        report['initial_full_grid_audit'] = audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        save('complete-curvature-initial-state-and-independent-full-grid-gates')
        report['phase'] = 'shared-budget-curvature-row-exchange'
        stage = run_exchange(objective,initial,lambda_initial=proposal,
            artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['curvature_exchange_stage'] = stage
        point = stage['checkpoint'].get('best_physical_curvature_point')
        if point is None:
            save('no-full-grid-fixed-metric-and-physical-eligible-state-preserved')
            return report
        final = np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if coefficients(final) != point['exact_binary64_physical_coefficients']:
            raise ValueError('selected curvature-stage exact physical coefficients differ')
        zeta = float(Q(point['auxiliary_zeta_exact_binary64']))
        lam = float(Q(point['auxiliary_lambda_exact_binary64']))
        if (zeta != point['auxiliary_zeta_evaluated'] or lam != point['auxiliary_lambda_evaluated']
                or lam != float(Q(cfg['curvature_scale_exact']))*zeta
                or digest(problem.identity(final)) != point['physical_state_sha256']):
            raise ValueError('selected curvature scalar or physical identity differs')
        identity = problem.identity(final)
        frozen, fc = problem.frozen_metric_copy(final)
        if (fc.tobytes() != final.tobytes() or frozen.identity(fc) != identity
                or frozen.metric_model(fc) != metric or frozen.height_base_definition != b0):
            raise ArithmeticError('freeze changed complete g, height reference, physical coefficients or field')
        problem, final = frozen, fc
        report.update(final_state=state_record(problem,final),selected_raw_auxiliary_zeta=zeta,
            selected_raw_auxiliary_lambda=lam,selected_curvature_auxiliary_not_inflated_at_final_audit=True)
        report['phase'] = 'independent-final-full-grid-and-angle-doubling'
        work = problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit'] = audit_data(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints'] = candidate_decision(problem,gate,final,zeta,work,lower,upper,cfg)
        save('selected-curvature-state-recomputed-on-full-grid-before-angle-doubling')
        del objective
        doubled_theta = np.arange(2*len(theta))*np.pi/len(theta)
        doubled = problem.geometry(final,radial,doubled_theta,order)
        report['final_doubled_angle_audit'] = audit_data(problem,final,doubled,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints'] = candidate_decision(problem,gate,final,zeta,doubled,lower,upper,cfg)
        report['same_parameter_Pi_refinement'] = compare_data(problem,work,problem,doubled,final,
            name='one fixed-metric curvature-exchange physical state; raw selected lambda unchanged',theta_stride=2)
        if problem.identity(final) != identity:
            raise ArithmeticError('angle refinement changed the physical state')
        report['limitations'] = {
            'all_constraints_and_curvature_diagnostics_are_sampled_only':True,
            'fixed_metric_budget_is_not_exact_isometry':True,
            'new_fine_or_auxiliary_failures_remain_failures':True,
            'curvature_target_radius_exact':cfg['curvature_target_radius_exact'],
            'curvature_and_mirror_pairs_do_not_cover_all_surface_pairs':True,
            'no_complete_embedding_or_whole_surface_reach_certificate':True,
            'no_second_solve_or_parameter_step_during_final_refinement':True,
        }
        save('complete-shared-budget-actual-curvature-exchange-audit')
        return report
    except Exception as error:
        report['error'] = {'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('curvature-audit-error-preserved-initial-and-checkpoints')
        return report


def developer_check():
    arrays = array_check()
    with tempfile.TemporaryDirectory(prefix='curvature-exchange-artificial-',dir='/dev/shm') as folder:
        directory = Path(folder)
        args, unused, seventh = artificial_seven_inputs(directory)
        saved = prepare_saved(args,artificial=True)
        eighth = run_saved(saved,args.out,artificial=True)
        args.trial_audit = args.out
        args.expected_trial_sha256 = hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out = directory/'dense-source-artificial.json'
        dense_prepared = prepare_dense(args,artificial=True)
        ninth = run_dense(dense_prepared,args.out,artificial=True,evaluate_only=True)
        if ninth['status'] != 'complete-one-dense-mirror-minimax-and-physical-best-audit':
            raise ArithmeticError('artificial ninth fixture failed')
        args.dense_audit = args.out
        args.expected_dense_sha256 = hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out = directory/'exchange-source-artificial.json'
        exchange_prepared = prepare_exchange(args,artificial=True)
        tenth = run_metric_exchange(exchange_prepared,args.out,artificial=True,evaluate_only=True)
        if tenth['status'] != 'complete-shared-budget-full-grid-row-exchange-audit':
            raise ArithmeticError('artificial tenth fixture failed')
        args.exchange_audit = args.out
        args.expected_exchange_sha256 = hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out = directory/'curvature-artificial.json'
        flow = time.monotonic()
        prepared = prepare_run(args,artificial=True,process_started=flow)
        seconds = time.monotonic()-flow
        report = run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=flow,prepare_seconds=seconds)
        summary = json.loads(summary_path(args.out).read_text())
        summary_bound = summary['full_report']['sha256'] == hashlib.sha256(args.out.read_bytes()).hexdigest()
        same = report.get('final_state',{}).get('canonical_physical_state_sha256') == report['initial_state']['canonical_physical_state_sha256']
        no_solve = report.get('curvature_exchange_stage',{}).get('solver',{}).get('minimize_invocation_count') == 0
        wrong = copy.copy(args)
        wrong.expected_exchange_sha256 = '0'*64
        wrong.out = directory/'bad-tenth.json'
        try:
            prepare_run(wrong,artificial=True)
            bad_sha = False
        except ValueError:
            failed = json.loads(wrong.out.read_text())
            bad_sha = failed['phase'] == 'tenth-exchange-report-byte-binding' and failed['new_solver_calls'] == 0
        corrupt = copy.deepcopy(tenth)
        corrupt['final_state']['canonical_physical_state_sha256'] = '0'*64
        try:
            replay_exchange_report(exchange_prepared,corrupt,artificial=True)
            bad_state = False
        except ValueError:
            bad_state = True
        corrupt = copy.deepcopy(tenth)
        corrupt['full_value_sampling_definition']['radial_nodes_exact'][1] = '1/999'
        try:
            replay_exchange_report(exchange_prepared,corrupt,artificial=True)
            bad_grid = False
        except ValueError:
            bad_grid = True
        corrupt = copy.deepcopy(tenth)
        corrupt['final_doubled_constraints']['eligible_under_physical_gates_including_mirror'] = False
        try:
            replay_exchange_report(exchange_prepared,corrupt,artificial=True)
            bad_physical = False
        except ValueError:
            bad_physical = True
        snap = report.get('curvature_exchange_stage',{}).get('checkpoint',{})
        batch = snap.get('same_state_batch_ordinary_jet_differences_by_field',{})
        batch_pass = bool(batch and max(batch.values()) < 1e-8)
        timing = bool(report['process_total_elapsed_seconds'] >= report['prepare_elapsed_seconds']+report['run_audit_elapsed_seconds']
            and report['optimization_active_seconds'] == 0.)
        old_delta = report.get('old_failed_metric_auxiliary_delta') == tenth['selected_raw_auxiliary_delta']
    passed = bool(arrays['passed'] and report['status'] == 'complete-shared-budget-actual-curvature-exchange-audit'
        and same and no_solve and summary_bound and bad_sha and bad_state and bad_grid and bad_physical
        and batch_pass and timing and old_delta)
    return {
        'schema':'ten-input-curvature-exchange-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,'targeted_array_checks':arrays,
        'complete_main_status':report['status'],'complete_main_error':report.get('error'),
        'full_main_calls_no_optimizer':no_solve,'same_physical_state_during_evaluation_only':same,
        'wrong_tenth_SHA_saves_failure':bad_sha,'corrupted_selected_state_rejected':bad_state,
        'corrupted_exact_grid_rejected':bad_grid,'source_fine_physical_failure_rejected':bad_physical,
        'all_ordinary_two_jets_same_state_batch_replay':batch,
        'old_raw_metric_delta_preserved_distinct_from_new_lambda':old_delta,
        'loader_initialization_optimization_and_total_clocks_separate':timing,
        'summary_bound_to_complete_report_bytes':summary_bound,
        'same_state_angle_refinement':report.get('same_parameter_Pi_refinement'),
        'passed':passed,
    }


def main():
    process_started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['input','anchor-input','short-audit','height-audit','prior-joint-audit','resume-audit',
                 'epigraph-audit','trial-audit','dense-audit','exchange-audit']:
        parser.add_argument('--'+name,type=Path)
    for name in ['input','anchor','short','height','prior-joint','resume','epigraph','trial','dense','exchange']:
        parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    if args.check_only:
        try:
            result = developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'curvature-exchange-development-error-v1','passed':False,
                'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-process_started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result['source_files_sha256'] = implementation_hashes()
        result['process_total_elapsed_seconds'] = time.monotonic()-process_started
        atomic_save(args.out,result)
        print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:
            raise SystemExit(1)
        return
    prepare_started = time.monotonic()
    try:
        prepared = prepare_run(args,process_started=process_started)
    except Exception:
        raise SystemExit(1)
    prepare_seconds = time.monotonic()-prepare_started
    report = run_audit(prepared,args.out,process_started=process_started,prepare_seconds=prepare_seconds)
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)
    if report['status'] != 'complete-shared-budget-actual-curvature-exchange-audit':
        raise SystemExit(1)


if __name__ == '__main__':
    main()

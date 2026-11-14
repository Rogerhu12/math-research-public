#!/usr/bin/env python3
"""One same-g curvature continuation with current-pool feasibility recovery.

The first ten reports restore the accepted physical state. The eleventh is
the completed, unchanged-state first curvature attempt; only its learned
constraint indices are reused. Ineligible old trial states are not starts.
No prior optimizer is replayed. All scientific gates and budgets are kept.
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
import frame_curvature_epigraph_exchange_audit as previous
from frame_curvature_epigraph_exchange import candidate_decision, GROUPS
from frame_curvature_feasible_exchange import (
    FeasibleCurvatureExchangeObjective as CurvatureExchangeObjective,
    upgrade_configuration, run_exchange, developer_check as scheduling_check,
    implementation_hashes as feasible_hashes, POLICY)

SCHEMA='same-g-pooled-feasibility-curvature-exchange-audit-v1'
ORIGINAL_CURVATURE_RUN='43645177423'
ORIGINAL_CURVATURE_SOURCE='2f1b809c0b0abb7a26303d36940edc203815f872'
coefficients=previous.coefficients
curvature_grid=previous.curvature_grid
summary_path=previous.summary_path


def implementation_hashes():
    result=previous.implementation_hashes()
    result.update(feasible_hashes())
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def save_report(out,report):
    atomic_save(out,report)
    summary=previous.small_summary(report,out)
    for name in ['learned_pool_replay','original_curvature_stage_retained','new_exchange_scheduling_policy']:
        if name in report: summary[name]=copy.deepcopy(report[name])
    atomic_save(summary_path(out),summary)


def replay_completed_curvature(prepared,prior,*,artificial=False):
    restored,bindings,tenth,old_replay=prepared
    problem,initial,gate,lower,upper,source_cfg,old_cfg,old_initialization=restored
    if (prior.get('schema')!=previous.SCHEMA
            or prior.get('status')!='complete-shared-budget-actual-curvature-exchange-audit'
            or bool(prior.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('the completed matching first-curvature report is required')
    if (prior.get('source_files_sha256')!=previous.implementation_hashes()
            or prior.get('configuration')!=previous.run_configuration(artificial)):
        raise ValueError('the preserved first-curvature source/configuration differs')
    if not artificial and (str(prior.get('github_run_id'))!=ORIGINAL_CURVATURE_RUN
            or prior.get('github_sha')!=ORIGINAL_CURVATURE_SOURCE):
        raise ValueError('the requested original curvature calculation run/source differs')
    for name,binding in bindings.items():
        old=prior.get('exact_input_storage',{}).get(name,{})
        for key in ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']:
            if old.get(key)!=binding.get(key):
                raise ValueError('eleventh report preceding input binding differs: '+name+'/'+key)
    expected=state_record(problem,initial)
    if (prior.get('input_replay')!=old_replay or prior.get('initial_state')!=expected
            or prior.get('final_state')!=expected):
        raise ValueError('this continuation must start from the unchanged accepted first-curvature selection')
    if (not prior.get('unchanged_complete_metric_and_height_reference')
            or prior.get('old_optimizer_calls_this_run')!=0
            or prior.get('old_failed_metric_auxiliary_delta')!=tenth['selected_raw_auxiliary_delta']):
        raise ValueError('the original scientific/history identity changed')
    radial,theta,grid=curvature_grid(tenth)
    if prior.get('full_value_sampling_definition')!=grid:
        raise ValueError('the learned pool belongs to a different exact value grid')
    stage=prior['curvature_exchange_stage']; checkpoint=stage['checkpoint']
    point=checkpoint.get('best_physical_curvature_point')
    if (not point or point.get('physical_state_sha256')!=digest(problem.identity(initial))
            or point.get('exact_binary64_physical_coefficients')!=coefficients(initial)
            or np.asarray(point.get('physical_parameter_coefficients_binary64'),float).tobytes()!=initial.tobytes()):
        raise ValueError('the original accepted coefficients differ from the current complete state')
    for key in ['final_full_grid_constraints','final_doubled_constraints']:
        decision=prior.get(key,{})
        if not decision.get('eligible_under_fixed_metric_and_physical_gates'):
            raise ValueError('both original angle grids must pass the unchanged fixed-metric and physical gates')
        if (decision.get('fixed_metric_budget_exact')!=old_cfg['fixed_metric_budget_exact']
                or decision.get('hard_strip_half_width_exact')!=old_cfg['hard_strip_half_width_exact']
                or decision.get('mirror_target_exact')!=old_cfg['mirror_target_exact']):
            raise ValueError('an original geometric gate definition differs')
    history=checkpoint.get('active_row_pool_history',[])
    if not history: raise ValueError('the completed original run has no saved row pool')
    last=history[-1]
    indices=last.get('row_indices')
    if (not isinstance(indices,list) or any(type(x) is not int for x in indices)
            or indices!=sorted(set(indices)) or not indices
            or last.get('row_count')!=len(indices)
            or last.get('row_indices_sha256')!=digest(indices)
            or last.get('group_order')!=list(GROUPS)
            or last.get('flat_index_rule')!='group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'
            or last.get('total_full_grid_rows')!=len(GROUPS)*len(radial)*len(theta)
            or min(indices)<0 or max(indices)>=len(GROUPS)*len(radial)*len(theta)
            or len(indices)>old_cfg['max_pool_rows']):
        raise ValueError('saved learned row indices, group order, range or exact hash differ')
    cfg=upgrade_configuration(old_cfg)
    initialization=previous.initial_lambda_definition(prior,cfg)
    learned={'schema':'same-grid-learned-curvature-row-pool-replay-v1',
        'original_source_run':prior.get('github_run_id'),'original_source_commit':prior.get('github_sha'),
        'source_pool_version':last['version'],'source_pool_rows':len(indices),
        'source_row_indices_sha256':last['row_indices_sha256'],
        'source_full_value_grid_sha256':grid['definition_sha256'],
        'group_order':list(GROUPS),'flat_index_rule':last['flat_index_rule'],
        'pool_is_an_evaluation_choice_not_a_physical_field':True,
        'all_original_enforced_indices_retained':True,
        'old_ineligible_trial_coefficients_are_not_used':True}
    replay={'schema':'eleven-input-pooled-feasibility-curvature-start-replay-v1',
        'ten_input_replay':old_replay,'complete_metric_sha256':problem.metric_model(initial)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'canonical_physical_state_sha256':digest(problem.identity(initial)),
        'physical_parameter_count':problem.nunknown,'same_accepted_exact_coefficients':True,
        'same_complete_g_height_reference_and_value_grid':True,'learned_pool':learned,
        'new_exchange_scheduling_policy':POLICY,
        'old_failed_metric_delta_unchanged':prior['old_failed_metric_auxiliary_delta'],
        'original_curvature_stage_retained':{
            'status':stage['status'],'solver':{k:v for k,v in stage['solver'].items() if k!='rounds'},
            'final_raw_auxiliary_zeta':prior['selected_raw_auxiliary_zeta'],
            'final_raw_auxiliary_lambda':prior['selected_raw_auxiliary_lambda'],
            'final_canonical_physical_state_sha256':prior['final_state']['canonical_physical_state_sha256']},
        'new_curvature_initialization':initialization,
        'old_optimizer_calls_replayed':0,'no_research_geometry_during_structural_replay':True}
    return (problem,initial,gate,lower,upper,source_cfg,cfg,initialization),replay,np.asarray(indices,dtype=np.int64)


def prepare_run(args,*,artificial=False,process_started=None):
    start=time.monotonic()
    process_started=start if process_started is None else process_started
    phase='ten-input-accepted-state-replay'; bindings={}
    try:
        if not artificial:
            paths=[args.input,args.anchor_input,args.short_audit,args.height_audit,args.prior_joint_audit,
                args.resume_audit,args.epigraph_audit,args.trial_audit,args.dense_audit,args.exchange_audit,args.curvature_audit]
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        old=previous.prepare_run(args,artificial=artificial,process_started=process_started)
        bindings=copy.deepcopy(old[1])
        phase='eleventh-completed-curvature-report-byte-binding'
        if args.curvature_audit is None or args.expected_curvature_sha256 is None:
            raise ValueError('the eleventh completed curvature report and decoded SHA are required')
        prior,raw,binding=read_input(args.curvature_audit,args.expected_curvature_sha256)
        phase='eleventh-learned-pool-and-accepted-state-replay'
        restored,replay,pool=replay_completed_curvature(old,prior,artificial=artificial)
        bindings['completed_first_curvature_exchange']=binding
        return restored,bindings,old[2],replay,pool
    except Exception as error:
        report={'schema':SCHEMA,'status':'input-replay-failed-before-feasibility-controlled-curvature-geometry',
            'phase':phase,'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-start,
            'process_total_elapsed_seconds':time.monotonic()-process_started,
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out,report)
        raise


def run_audit(prepared, out, *, artificial=False, evaluate_only=False, process_started=None, prepare_seconds=None):
    restored, bindings, tenth, replay, learned_pool = prepared
    problem, initial, gate, lower, upper, source_cfg, cfg, initialization = restored
    started = time.monotonic()
    scope = ('main entrance including the eleven-input loader and object restoration' if process_started is not None
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
        'process_clock_scope':scope,'prepare_elapsed_seconds':None if prepare_seconds is None else float(prepare_seconds),
        'learned_pool_replay':replay['learned_pool'],
        'original_curvature_stage_retained':replay['original_curvature_stage_retained'],
        'new_exchange_scheduling_policy':POLICY}
    def save(status):
        now = time.monotonic()
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=report.get('curvature_exchange_stage',{}).get('checkpoint',{}).get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('eleven-inputs-replayed-before-feasibility-controlled-curvature-geometry')
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
        objective.evaluation_definition.update(
            eleventh_input_decoded_sha256=bindings['completed_first_curvature_exchange']['decoded_sha256'],
            learned_pool_replay=replay['learned_pool'])
        objective.evaluation_sha256 = digest(objective.evaluation_definition)
        objective.set_pool(learned_pool,{'kind':'reused-exact-same-grid-pool-from-completed-original-curvature-run',
            'source':replay['learned_pool']})
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
        save('complete-pooled-feasibility-actual-curvature-exchange-audit')
        return report
    except Exception as error:
        report['error'] = {'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('curvature-audit-error-preserved-initial-and-checkpoints')
        return report



def developer_check():
    schedule=scheduling_check()
    with tempfile.TemporaryDirectory(prefix='curvature-feasible-exchange-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder)
        args,unused,seventh=previous.artificial_seven_inputs(directory)
        saved=previous.prepare_saved(args,artificial=True)
        previous.run_saved(saved,args.out,artificial=True)
        args.trial_audit=args.out; args.expected_trial_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'dense-source-artificial.json'
        dense=previous.prepare_dense(args,artificial=True)
        previous.run_dense(dense,args.out,artificial=True,evaluate_only=True)
        args.dense_audit=args.out; args.expected_dense_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'exchange-source-artificial.json'
        exchange=previous.prepare_exchange(args,artificial=True)
        previous.run_metric_exchange(exchange,args.out,artificial=True,evaluate_only=True)
        args.exchange_audit=args.out; args.expected_exchange_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'completed-curvature-artificial.json'
        ten=previous.prepare_run(args,artificial=True)
        prior=previous.run_audit(ten,args.out,artificial=True,evaluate_only=True)
        if prior['status']!='complete-shared-budget-actual-curvature-exchange-audit':
            raise ArithmeticError('artificial eleventh source fixture failed')
        args.curvature_audit=args.out; args.expected_curvature_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'curvature-feasible-artificial.json'
        flow=time.monotonic(); prepared=prepare_run(args,artificial=True,process_started=flow)
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=flow,prepare_seconds=time.monotonic()-flow)
        no_optimizer=report.get('curvature_exchange_stage',{}).get('solver',{}).get('minimize_invocation_count')==0
        same=report.get('final_state',{}).get('canonical_physical_state_sha256')==prior['final_state']['canonical_physical_state_sha256']
        learned=report['learned_pool_replay']
        snap=report['curvature_exchange_stage']['checkpoint']
        exact_pool=snap['active_row_pool_history'][0]['row_indices']==prior['curvature_exchange_stage']['checkpoint']['active_row_pool_history'][-1]['row_indices']
        summary=json.loads(summary_path(args.out).read_text())
        summary_bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args); wrong.out=directory/'bad-eleventh-sha.json'; wrong.expected_curvature_sha256='0'*64
        try:
            prepare_run(wrong,artificial=True); bad_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text())
            bad_sha=failure['phase']=='eleventh-completed-curvature-report-byte-binding' and failure['new_solver_calls']==0
        corrupted=copy.deepcopy(prior)
        corrupted['curvature_exchange_stage']['checkpoint']['active_row_pool_history'][-1]['row_indices'][0]=-1
        try:
            replay_completed_curvature(ten,corrupted,artificial=True); bad_pool=False
        except ValueError: bad_pool=True
        corrupted=copy.deepcopy(prior); corrupted['full_value_sampling_definition']['angular_nodes']*=2
        try:
            replay_completed_curvature(ten,corrupted,artificial=True); bad_grid=False
        except ValueError: bad_grid=True
        corrupted=copy.deepcopy(prior); corrupted['final_state']['canonical_physical_state_sha256']='0'*64
        try:
            replay_completed_curvature(ten,corrupted,artificial=True); bad_state=False
        except ValueError: bad_state=True
    passed=bool(schedule['passed'] and no_optimizer and same and exact_pool and summary_bound
        and bad_sha and bad_pool and bad_grid and bad_state
        and report['status']=='complete-pooled-feasibility-actual-curvature-exchange-audit')
    return {'schema':'pooled-feasibility-curvature-exchange-development-v1',
        'artificial_inputs_only':True,'research_geometry_evaluated_or_optimized':False,
        'targeted_scheduling_checks':schedule,'complete_new_IO_status':report['status'],
        'complete_new_IO_error':report.get('error'),'full_main_calls_no_optimizer':no_optimizer,
        'exact_accepted_physical_state_preserved':same,'learned_indices_reused_exactly':exact_pool,
        'summary_byte_binding_pass':summary_bound,'wrong_eleventh_SHA_saves_failure':bad_sha,
        'bad_learned_index_rejected':bad_pool,'different_value_grid_rejected':bad_grid,
        'different_accepted_state_rejected':bad_state,
        'same_state_angle_refinement':report.get('same_parameter_Pi_refinement'),'passed':passed}


def main():
    process_started=time.monotonic()
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['input','anchor-input','short-audit','height-audit','prior-joint-audit','resume-audit',
                 'epigraph-audit','trial-audit','dense-audit','exchange-audit','curvature-audit']:
        parser.add_argument('--'+name,type=Path)
    for name in ['input','anchor','short','height','prior-joint','resume','epigraph','trial','dense','exchange','curvature']:
        parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True); args=parser.parse_args()
    if args.check_only:
        try:
            result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'pooled-feasibility-curvature-development-error-v1',
                'passed':False,'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-process_started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result['source_files_sha256']=implementation_hashes()
        result['process_total_elapsed_seconds']=time.monotonic()-process_started
        atomic_save(args.out,result)
        print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']: raise SystemExit(1)
        return
    begin=time.monotonic()
    try:
        prepared=prepare_run(args,process_started=process_started)
    except Exception:
        raise SystemExit(1)
    report=run_audit(prepared,args.out,process_started=process_started,prepare_seconds=time.monotonic()-begin)
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)
    if report['status']!='complete-pooled-feasibility-actual-curvature-exchange-audit':
        raise SystemExit(1)


if __name__=='__main__':
    main()

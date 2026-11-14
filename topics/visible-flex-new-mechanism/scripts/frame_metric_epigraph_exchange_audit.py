#!/usr/bin/env python3
"""One shared-budget, full-grid checked row-exchange minimax continuation.

Nine published byte-bound reports replay the latest dense physical state.
The complete value grid is 160 by 384 in the actual configuration; only the
SLSQP row pool changes. Initialization time, all solver calls, pool additions,
whole-grid physical/auxiliary decisions, and fixed-state angle refinement are
retained. --check-only uses explicit artificial reports and no research state.
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
from frame_entry_short_bounded_audit import read_input,audit_data,compare_data,compact_audit,compact_state,compact_comparison
from frame_independent_height_solve import state_record
from frame_metric_epigraph_trial_audit import (artificial_seven_inputs,prepare_run as prepare_saved,
    run_audit as run_saved)
from frame_metric_epigraph_dense_audit import (prepare_run as prepare_dense,run_restart as run_dense,
    implementation_hashes as dense_audit_hashes,union_grid,SCHEMA as DENSE_SCHEMA)
from frame_metric_epigraph_dense import configuration as dense_configuration
from frame_metric_epigraph_exchange import (ExchangeEpigraphObjective,configuration,candidate_decision,
    run_exchange,developer_check as array_check,implementation_hashes as exchange_hashes)

SCHEMA='same-metric-whole-grid-exchanged-constraint-minimax-audit-v1'


def implementation_hashes():
    out=dense_audit_hashes();out.update(exchange_hashes())
    out[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();return out


def coefficients(values):return [str(Q.from_float(float(x))) for x in values]


def expected_dense_configuration(artificial):
    cfg=dense_configuration()
    if artificial:
        cfg.update(minimum_signed_height_exact='-10',hard_ball_radius_exact='10',hard_strip_half_width_exact='10',
            mirror_target_exact='1/1000000000000',normal_area_numerical_floor=0.,maxiter=2,max_physical_evaluations=4,max_seconds=120.)
    return cfg


def replay_dense_report(prepared,report,*,artificial=False):
    restored,bindings,eighth,receipt=prepared
    problem,start,old_delta,gate,lower,upper,old_cfg,work_cfg,source_cfg,unused=restored
    if (report.get('schema')!=DENSE_SCHEMA or report.get('status')!='complete-one-dense-mirror-minimax-and-physical-best-audit'
            or bool(report.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('a completed matching dense continuation report is required')
    if report.get('source_files_sha256')!=dense_audit_hashes():raise ValueError('frozen ninth report implementation differs')
    if report.get('configuration')!=expected_dense_configuration(artificial):raise ValueError('ninth report configuration differs')
    for key,binding in bindings.items():
        old=report.get('exact_input_storage',{}).get(key,{})
        for field in ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']:
            if old.get(field)!=binding.get(field):raise ValueError('ninth input binding differs: '+key+'/'+field)
    if report.get('input_replay')!=receipt or report.get('initial_state')!=state_record(problem,start):
        raise ValueError('ninth report initial complete physical/evaluation state differs')
    if report.get('old_optimizer_calls_this_run')!=0 or not report.get('unchanged_physical_metric_and_b0'):
        raise ValueError('ninth report did not preserve the stated old history and target metric')
    if report.get('old_auxiliary_delta')!=old_delta or not report.get('selected_raw_delta_not_inflated_at_final_audit'):
        raise ValueError('the existing auxiliary failures or recorded raw scalar changed')
    _,_,work_grid=union_grid(eighth,work_cfg['joint_angular_nodes'])
    fine_grid=copy.deepcopy(work_grid);fine_grid.pop('definition_sha256')
    fine_grid['angular_nodes']=int(source_cfg['angular_nodes']);fine_grid['fixed_state_refinement_not_a_second_objective']=True
    fine_grid['definition_sha256']=digest(fine_grid)
    if report.get('work_sampling_definition')!=work_grid or report.get('fine_sampling_definition')!=fine_grid:
        raise ValueError('ninth report complete exact work/fine grids differ')
    stage=report.get('dense_epigraph_stage',{});point=stage.get('checkpoint',{}).get('best_physical_max_eta_point')
    if not point:raise ValueError('ninth report has no saved whole-work-grid physical best')
    final=np.asarray(point.get('physical_parameter_coefficients_binary64'),float)
    if final.shape!=(problem.nunknown,) or not np.all(np.isfinite(final)):
        raise ValueError('finite complete ninth physical state required')
    if coefficients(final)!=point.get('exact_binary64_physical_coefficients'):
        raise ValueError('ninth selected coefficient exact roundtrip failed')
    identity=problem.identity(final);record=state_record(problem,final)
    if (digest(identity)!=point.get('physical_state_sha256') or report.get('final_state')!=record
            or problem.metric_model(final)!=problem.metric_model(start)):
        raise ValueError('ninth full selected state, layout, fixed g, or coefficients differ')
    raw_delta=float(Q(point['auxiliary_delta_exact_binary64']))
    if raw_delta!=point['auxiliary_delta_evaluated'] or raw_delta!=report.get('selected_raw_auxiliary_delta'):
        raise ValueError('ninth saved raw auxiliary scalar differs')
    if not point.get('record',{}).get('decision',{}).get('eligible_under_physical_gates_including_mirror'):
        raise ValueError('ninth selection is not the recorded whole-work-grid physical best')
    # Fine strip failure is intentionally retained: it must not be a replay
    # rejection or relabeled as a pass before the new inner-strip solve.
    replay={'schema':'nine-input-dense-physical-best-exchange-replay-v1',
        'complete_metric_sha256':problem.metric_model(final)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'canonical_physical_state_sha256':digest(identity),'physical_parameter_count':problem.nunknown,
        'all_current_coefficients_and_layout_exactly_replayed':True,
        'ninth_old_raw_auxiliary_delta':raw_delta,'ninth_old_raw_auxiliary_exact_binary64':str(Q.from_float(raw_delta)),
        'ninth_fine_physical_gate_decision_retained':copy.deepcopy(report.get('final_doubled_constraints')),
        'old_optimizer_calls_replayed':0,'no_research_geometry_during_structural_replay':True,
        'new_inner_strip_is_an_explicit_stricter_solver_target_not_a_relabel_of_the_old_failure':True}
    return (problem,final,raw_delta,gate,lower,upper,work_cfg,source_cfg),replay


def exchange_grid(report,angular_nodes):
    source=report['fine_sampling_definition'];nodes=[Q(x) for x in source['radial_nodes_exact']]
    if not nodes or nodes[0]!=0 or any(y<=x for x,y in zip(nodes,nodes[1:])):
        raise ValueError('complete strictly increasing exact radial grid required')
    if source['radial_nodes_exact']!=report['work_sampling_definition']['radial_nodes_exact']:
        raise ValueError('the current dense report must preserve its full radial union')
    count=int(angular_nodes)
    if count<4 or count%4:raise ValueError('a complete multiple-of-four angular grid is required')
    radial=np.asarray([float(x) for x in nodes]);theta=np.arange(count)*2*np.pi/count
    if np.any(np.diff(radial)<=0):raise ValueError('exact nodes collapsed in numerical evaluation')
    definition={'schema':'unchanged-dense-radial-fine-angle-exchange-value-grid-v1',
        'source_dense_work_definition_sha256':digest(report['work_sampling_definition']),
        'source_dense_fine_definition_sha256':digest(source),
        'radial_nodes_exact':[str(x) for x in nodes],'radial_count':len(nodes),'angular_nodes':count,
        'theta_definition':'2*pi*j/N, complete uniform periodic grid',
        'all_value_gates_use_every_point_at_every_trial':True,
        'constraint_pool_changes_no_grid_point_or_physical_definition':True,
        'angle_grid_change_is_explicit_not_old_work_objective_replay':True}
    definition['definition_sha256']=digest(definition);return radial,theta,definition


def summary_path(out):return out.with_name(out.stem+'-summary.json')


def small_summary(report,out):
    keys=['schema','status','phase','source_files_sha256','configuration','exact_input_storage','input_replay',
        'github_sha','github_run_id','github_repository','artificial_inputs_only','old_optimizer_calls_this_run',
        'elapsed_seconds','run_audit_elapsed_seconds','prepare_elapsed_seconds','process_total_elapsed_seconds',
        'optimization_active_seconds','process_clock_scope','peak_rss_kib_linux','initial_current_constraints','final_full_grid_constraints',
        'final_doubled_constraints','selected_raw_auxiliary_delta','new_auxiliary_initialization',
        'old_raw_auxiliary_delta','error','unchanged_complete_metric_and_height_reference']
    result={key:report[key] for key in keys if key in report}
    for key in ['initial_state','final_state']:
        if key in report:result[key]=compact_state(report[key])
    for key in ['initial_full_grid_audit','final_full_grid_audit','final_doubled_angle_audit']:
        if key in report:result[key]=compact_audit(report[key])
    if 'same_parameter_Pi_refinement' in report:result['same_parameter_Pi_refinement']=compact_comparison(report['same_parameter_Pi_refinement'])
    if 'full_value_sampling_definition' in report:
        g=report['full_value_sampling_definition'];result['full_value_sampling_definition']={k:g[k] for k in ['schema','definition_sha256','radial_count','angular_nodes']}
    stage=report.get('exchange_stage')
    if stage:
        result['exchange_stage']={key:stage.get(key) for key in ['status','error','budget_message','selected_point']}
        solver=stage.get('solver',{});result['exchange_stage']['solver']={k:v for k,v in solver.items() if k!='rounds'}
        result['exchange_stage']['solver']['rounds']=[]
        for rd in solver.get('rounds',[]):
            r={k:v for k,v in rd.items() if k not in ['initial_vector_exact','pool_addition']}
            add=rd.get('pool_addition')
            if add:r['pool_addition']={k:add.get(k) for k in ['version','row_count','row_indices_sha256','omitted_violations_after_this_addition']}
            result['exchange_stage']['solver']['rounds'].append(r)
        snap=stage.get('checkpoint',{});result['exchange_stage']['checkpoint']={k:snap.get(k) for k in [
            'physical_geometry_evaluations','jacobian_geometry_evaluations','epigraph_vector_evaluations',
            'total_elapsed_seconds','initialization_elapsed_seconds','optimization_elapsed_seconds',
            'value_geometry_seconds','jacobian_geometry_seconds','pool_Jacobian_including_refresh_seconds',
            'maximum_geometry_cache_array_bytes','maximum_retained_selected_derivative_bytes',
            'maximum_single_constraint_Jacobian_bytes','maximum_value_Jacobian_replay_difference',
            'objective_evaluation_sha256']}
        result['exchange_stage']['checkpoint']['row_pools']=[{k:p.get(k) for k in ['version','row_count','row_indices_sha256','omitted_violations_after_this_addition']}
            for p in snap.get('active_row_pool_history',[])]
        for key in ['best_physical_max_eta_point','best_eligible_direct_max_eta_point','best_eligible_auxiliary_delta_point']:
            point=snap.get(key);result['exchange_stage']['checkpoint'][key]=None if point is None else {
                k:point.get(k) for k in ['physical_state_sha256','auxiliary_delta_evaluated','record']}
    raw=out.read_bytes();result['full_report']={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    result.update(sampled_only=True,task_complete=False,no_whole_surface_reach_certificate=True,
        no_pool_only_point_called_whole_grid_feasible=True)
    return result


def save_report(out,report):
    atomic_save(out,report);atomic_save(summary_path(out),small_summary(report,out))


def prepare_run(args,*,artificial=False,process_started=None):
    prepare_started=time.monotonic();process_started=prepare_started if process_started is None else process_started
    bindings={};phase='nine-input-public-repository-guard'
    try:
        if args.dense_audit is None or not args.expected_dense_sha256:raise ValueError('explicit ninth report path and decoded SHA256 required')
        paths=[args.input,args.anchor_input,args.short_audit,args.height_audit,args.prior_joint_audit,
            args.resume_audit,args.epigraph_audit,args.trial_audit,args.dense_audit]
        if not artificial:require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        phase='ninth-dense-report-byte-binding';ninth,raw,binding=read_input(args.dense_audit,args.expected_dense_sha256)
        bindings['completed_dense_minimax']=binding
        phase='unchanged-eight-input-replay';previous=prepare_dense(args,artificial=artificial);bindings.update(previous[1])
        phase='latest-dense-full-state-fixed-g-and-grid-replay';restored,replay=replay_dense_report(previous,ninth,artificial=artificial)
        return restored,bindings,ninth,replay
    except Exception as error:
        report={'schema':SCHEMA,'status':'input-replay-failed-before-exchange-research-geometry','phase':phase,
            'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,'artificial_inputs_only':bool(artificial),
            'old_optimizer_calls_this_run':0,'new_solver_calls':0,
            'prepare_elapsed_seconds':time.monotonic()-prepare_started,'run_audit_elapsed_seconds':0.,
            'process_total_elapsed_seconds':time.monotonic()-process_started,'optimization_active_seconds':0.,
            'process_clock_scope':'main entrance when explicitly provided, otherwise this input-loader entrance',
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out,report);raise


def run_audit(prepared,out,*,artificial=False,evaluate_only=False,process_started=None,prepare_seconds=None):
    restored,bindings,ninth,replay=prepared
    problem,initial,old_delta,gate,lower,upper,work_cfg,source_cfg=restored
    cfg=configuration()
    if artificial:
        cfg.update(minimum_signed_height_exact='-10',hard_ball_radius_exact='10',hard_strip_half_width_exact='999/100',
            outer_strip_half_width_exact='10',strip_inner_margin_exact='1/100',mirror_target_exact='1/1000000000000',
            normal_area_numerical_floor=0.,maxiter=2,max_physical_evaluations=6,max_seconds=120.)
    started=time.monotonic();clock_scope=('main entrance including the nine-input loader and object restoration'
        if process_started is not None else 'direct run_audit entrance; artificial fixture construction is outside this clock')
    process_started=started if process_started is None else process_started
    metric=copy.deepcopy(problem.metric_model(initial));b0=copy.deepcopy(problem.height_base_definition)
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,'exact_input_storage':bindings,
        'input_replay':replay,'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':0,'old_raw_auxiliary_delta':old_delta,'initial_state':state_record(problem,initial),
        'unchanged_complete_metric_and_height_reference':True,'process_clock_scope':clock_scope,
        'prepare_elapsed_seconds':None if prepare_seconds is None else float(prepare_seconds)}
    def save(status):
        now=time.monotonic();report['status']=status;report['elapsed_seconds']=now-started
        report['run_audit_elapsed_seconds']=now-started;report['process_total_elapsed_seconds']=now-process_started
        report['optimization_active_seconds']=report.get('exchange_stage',{}).get('checkpoint',{}).get('optimization_elapsed_seconds') or 0.
        report['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;save_report(out,report)
    save('nine-inputs-replayed-before-any-new-geometry')
    try:
        report['phase']='full-value-grid-initialization-outside-optimization-clock'
        radial,theta,grid=exchange_grid(ninth,source_cfg['angular_nodes']);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid
        def checkpoint(snap):
            report['exchange_stage']={'status':'current-exchange-checkpoint','checkpoint':snap}
            save('whole-grid-exchange-checkpoint')
        obj=ExchangeEpigraphObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        obj.evaluation_definition.update(ninth_input_decoded_sha256=bindings['completed_dense_minimax']['decoded_sha256'],
            complete_value_sampling_definition=grid,new_inner_strip_and_new_auxiliary_bound_explicit=True)
        obj.evaluation_sha256=digest(obj.evaluation_definition)
        vector=obj.initial_vector(initial);obj.initialize_pool(vector);record=obj.evaluate(vector)
        report['new_auxiliary_initialization']={'old_raw_auxiliary_delta':old_delta,'new_auxiliary_delta':float(vector[-1]),
            'new_exact_binary64_delta':str(Q.from_float(float(vector[-1]))),'full_grid_eta':record['decision']['direct_max_eta'],
            'rule':'max(2*delta_min, full_grid_eta+(1+eta)/1000000)',
            'does_not_modify_old_auxiliary_or_old_acceptance_history':True,'physical_coefficients_unchanged':True}
        report['initial_current_constraints']=record['decision']
        report['initial_full_grid_audit']=audit_data(problem,initial,obj.geometry_cache,source_cfg['tau'])
        save('complete-new-full-grid-initial-audit-including-inner-strip-failure-if-any')
        report['phase']='shared-budget-row-exchange-optimization'
        stage=run_exchange(obj,initial,artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['exchange_stage']=stage;point=stage['checkpoint'].get('best_physical_max_eta_point')
        if point is None:
            save('no-whole-grid-inner-strip-and-mirror-eligible-point-preserved');return report
        final=np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if coefficients(final)!=point['exact_binary64_physical_coefficients']:raise ValueError('selected exact coefficient roundtrip failed')
        delta=float(Q(point['auxiliary_delta_exact_binary64']))
        if delta!=point['auxiliary_delta_evaluated'] or digest(problem.identity(final))!=point['physical_state_sha256']:
            raise ValueError('selected auxiliary or physical identity differs')
        identity=problem.identity(final);frozen,fc=problem.frozen_metric_copy(final)
        if (fc.tobytes()!=final.tobytes() or frozen.identity(fc)!=identity or frozen.metric_model(fc)!=metric
                or frozen.height_base_definition!=b0):raise ArithmeticError('freeze changed complete g, b0, coefficients or field')
        problem=frozen;final=fc
        report.update(final_state=state_record(problem,final),selected_raw_auxiliary_delta=delta,
            selected_auxiliary_not_inflated_at_final_audit=True)
        report['phase']='independent-final-full-grid-and-angle-doubling'
        work=problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit']=audit_data(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints']=candidate_decision(problem,gate,final,delta,work,lower,upper,cfg)
        save('whole-grid-selected-state-recomputed-before-angle-doubling')
        del obj
        doubled_theta=np.arange(2*len(theta))*np.pi/len(theta)
        doubled=problem.geometry(final,radial,doubled_theta,order)
        report['final_doubled_angle_audit']=audit_data(problem,final,doubled,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints']=candidate_decision(problem,gate,final,delta,doubled,lower,upper,cfg)
        report['same_parameter_Pi_refinement']=compare_data(problem,work,problem,doubled,final,
            name='one full-grid exchanged minimax state, raw selected auxiliary scalar unchanged',theta_stride=2)
        if problem.identity(final)!=identity:raise ArithmeticError('final fixed-state angle refinement changed the field')
        report['limitations']={'all_gates_are_sampled_only':True,'unresolved_auxiliary_or_new_fine_violations_remain_failures':True,
            'mirror_points_are_not_all_surface_pairs':True,'curvature_is_diagnosed_not_constrained':True,
            'no_second_objective_or_new_parameter_step_during_final_refinement':True}
        save('complete-shared-budget-full-grid-row-exchange-audit');return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('exchange-audit-error-preserved-initial-and-checkpoints');return report


def developer_check():
    arrays=array_check()
    with tempfile.TemporaryDirectory(prefix='exchange-minimax-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder);args,unused,seventh=artificial_seven_inputs(directory)
        saved=prepare_saved(args,artificial=True);eighth=run_saved(saved,args.out,artificial=True)
        args.trial_audit=args.out;args.expected_trial_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'dense-source-artificial.json';dense_prepared=prepare_dense(args,artificial=True)
        ninth=run_dense(dense_prepared,args.out,artificial=True,evaluate_only=True)
        if ninth['status']!='complete-one-dense-mirror-minimax-and-physical-best-audit':raise ArithmeticError('artificial ninth report failed')
        args.dense_audit=args.out;args.expected_dense_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'exchange-artificial.json';flow_started=time.monotonic()
        prepared=prepare_run(args,artificial=True,process_started=flow_started);prepare_seconds=time.monotonic()-flow_started
        report=run_audit(prepared,args.out,artificial=True,evaluate_only=True,
            process_started=flow_started,prepare_seconds=prepare_seconds)
        summary=json.loads(summary_path(args.out).read_text());bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        same=report.get('final_state',{}).get('canonical_physical_state_sha256')==report['initial_state']['canonical_physical_state_sha256']
        no_solve=report.get('exchange_stage',{}).get('solver',{}).get('minimize_invocation_count')==0
        wrong=copy.copy(args);wrong.expected_dense_sha256='0'*64;wrong.out=directory/'bad-ninth.json'
        try:prepare_run(wrong,artificial=True);bad_sha=False
        except ValueError:
            failed=json.loads(wrong.out.read_text());bad_sha=failed['phase']=='ninth-dense-report-byte-binding' and failed['new_solver_calls']==0
        corrupt=copy.deepcopy(ninth);corrupt['final_state']['canonical_physical_state_sha256']='0'*64
        try:replay_dense_report(dense_prepared,corrupt,artificial=True);bad_state=False
        except ValueError:bad_state=True
        corrupt=copy.deepcopy(ninth);corrupt['fine_sampling_definition']['radial_nodes_exact'][1]='1/999'
        try:replay_dense_report(dense_prepared,corrupt,artificial=True);bad_grid=False
        except ValueError:bad_grid=True
        callback_grid=report.get('full_value_sampling_definition',{})
        row_pool=report.get('exchange_stage',{}).get('checkpoint',{}).get('active_row_pool_history',[])
        whole_grid=bool(callback_grid.get('all_value_gates_use_every_point_at_every_trial') and row_pool)
        timing=bool(report['process_total_elapsed_seconds']>=report['prepare_elapsed_seconds']+report['run_audit_elapsed_seconds']
            and report['optimization_active_seconds']==0.)
    passed=bool(arrays['passed'] and report['status']=='complete-shared-budget-full-grid-row-exchange-audit'
        and same and no_solve and bound and bad_sha and bad_state and bad_grid and whole_grid and timing)
    return {'schema':'nine-input-full-grid-row-exchange-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,'targeted_array_checks':arrays,
        'complete_main_status':report['status'],'complete_main_error':report.get('error'),
        'full_main_calls_no_optimizer':no_solve,'same_physical_state_during_evaluation_only':same,
        'whole_grid_and_separate_row_pool_both_recorded':whole_grid,'wrong_ninth_SHA_saves_failure':bad_sha,
        'corrupted_selected_state_rejected':bad_state,'corrupted_exact_grid_rejected':bad_grid,
        'loader_total_audit_and_zero_optimization_clocks_separate':timing,
        'summary_bound_to_full_report_bytes':bound,'fixed_state_angle_refinement':report.get('same_parameter_Pi_refinement'),
        'passed':passed}


def main():
    process_started=time.monotonic()
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['input','anchor-input','short-audit','height-audit','prior-joint-audit','resume-audit','epigraph-audit','trial-audit','dense-audit']:
        parser.add_argument('--'+name,type=Path)
    for name in ['input','anchor','short','height','prior-joint','resume','epigraph','trial','dense']:
        parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    if args.check_only:
        try:result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'exchange-minimax-development-error-v1','passed':False,
                'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-process_started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}});raise
        result['source_files_sha256']=implementation_hashes();result['process_total_elapsed_seconds']=time.monotonic()-process_started
        atomic_save(args.out,result)
        print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    prepare_started=time.monotonic()
    try:prepared=prepare_run(args,process_started=process_started)
    except Exception:raise SystemExit(1)
    prepare_seconds=time.monotonic()-prepare_started
    report=run_audit(prepared,args.out,process_started=process_started,prepare_seconds=prepare_seconds)
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)
    if report['status']!='complete-shared-budget-full-grid-row-exchange-audit':raise SystemExit(1)


if __name__=='__main__':main()

#!/usr/bin/env python3
"""One dense-radial minimax continuation from the audited saved physical trial.

Eight published inputs bind the unchanged physical state and target metric.
The old auxiliary failure is retained as provenance; a new positive auxiliary
bound is initialized on the exact union of the old work and fine radial grids.
No old optimizer is replayed. New and final states retain separate physical and
auxiliary decisions. Actual research is restricted to the public repository's
GitHub Actions; --check-only uses explicit small artificial input reports.
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
from frame_entry_short_bounded_audit import (read_input,build_grid,audit_data,compare_data,
    compact_audit,compact_state,compact_comparison)
from frame_independent_height_solve import state_record
from frame_metric_epigraph_trial_audit import (prepare_run as prepare_saved_trial,
    run_audit as run_saved_trial_audit,artificial_seven_inputs,
    implementation_hashes as saved_trial_hashes,SCHEMA as SAVED_SCHEMA)
from frame_metric_epigraph_dense import (DenseMirrorEpigraphObjective,configuration,
    candidate_decision,run_dense_epigraph,developer_check as array_check,
    implementation_hashes as dense_hashes)

SCHEMA='audited-physical-trial-dense-mirror-minimax-continuation-v1'


def implementation_hashes():
    result=saved_trial_hashes();result.update(dense_hashes())
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def exact_coefficients(values):return [str(Q.from_float(float(x))) for x in values]


def replay_readonly_audit(prepared,report,*,artificial=False):
    restored,bindings,seventh=prepared
    problem,state,old_delta,gate,lower,upper,old_cfg,work_cfg,source_cfg,receipt=restored
    if (report.get('schema')!=SAVED_SCHEMA or report.get('status')!=
            'complete-one-saved-unaccepted-trial-fixed-state-audit'):
        raise ValueError('one completed read-only saved-trial audit is required')
    if bool(report.get('artificial_inputs_only'))!=bool(artificial):
        raise ValueError('artificial and actual eighth reports cannot be interchanged')
    if report.get('source_files_sha256')!=saved_trial_hashes():
        raise ValueError('read-only audit source implementation differs from its frozen version')
    for key,binding in bindings.items():
        old=report.get('exact_input_storage',{}).get(key,{})
        for field in ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']:
            if old.get(field)!=binding.get(field):raise ValueError('eighth report input storage differs: '+key+'/'+field)
    if report.get('input_replay')!=receipt:raise ValueError('eighth report does not consume the exact seven-input trial')
    if (report.get('optimizer_calls')!=0 or report.get('auxiliary_delta_reassigned')
            or not report.get('same_complete_metric_b0_and_coefficients') or report.get('error')):
        raise ValueError('the input must be a completed fixed-state, unchanged-delta, zero-solve audit')
    if report.get('retained_old_auxiliary_delta')!=old_delta:
        raise ValueError('the old failed auxiliary delta changed in the read-only input')
    if report.get('trial_state')!=state_record(problem,state):
        raise ValueError('eighth report complete physical/evaluation state differs')
    if not report.get('this_trial_remains_unaccepted_by_the_original_run'):
        raise ValueError('the earlier trial acceptance history must remain explicit')
    _,_,work_grid=build_grid(problem,work_cfg['joint_radial_nodes'],work_cfg['joint_collar_subdivisions'],work_cfg['joint_angular_nodes'])
    _,_,fine_grid=build_grid(problem,source_cfg['radial_nodes'],source_cfg['collar_subdivisions'],source_cfg['angular_nodes'])
    if report.get('work_sampling_definition')!=work_grid or report.get('fine_sampling_definition')!=fine_grid:
        raise ValueError('read-only input work/fine exact nodes or structural identities differ')
    for key in ['physical_gates_on_work','physical_gates_on_fine','physical_gates_on_doubled']:
        if not report.get(key,{}).get('all_four_physical_gate_groups_pass'):
            raise ValueError('the declared new start must have passed all recorded prior physical gate groups')
        if report[key].get('old_auxiliary_delta_covers_direct_max_eta'):
            raise ValueError('the consumed old auxiliary failure must not be relabeled as a pass')
    replay={'schema':'eight-input-saved-trial-dense-continuation-replay-v1',
        'physical_state_sha256':digest(problem.identity(state)),
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'physical_parameter_count':problem.nunknown,
        'all_coefficients_and_current_layout_exactly_replayed':True,
        'old_auxiliary_delta_evaluated':old_delta,'old_auxiliary_delta_exact_binary64':str(Q.from_float(old_delta)),
        'source_original_run_did_not_accept_this_trial':True,
        'read_only_audit_had_zero_optimizer_and_zero_delta_changes':True,
        'prior_work_fine_and_doubled_physical_gates_recorded_as_passed':True,
        'prior_auxiliary_failures_are_preserved':True,
        'no_geometry_was_recomputed_during_this_structural_replay':True}
    return restored,replay


def union_grid(report,angular_nodes):
    work=report['work_sampling_definition'];fine=report['fine_sampling_definition']
    a=[Q(x) for x in work['radial_nodes_exact']];b=[Q(x) for x in fine['radial_nodes_exact']]
    for label,values in [('work',a),('fine',b)]:
        if not values or values[0]!=0 or any(y<=x for x,y in zip(values,values[1:])):
            raise ValueError('exact source radial grid is not increasing and complete: '+label)
    if a[-1]!=b[-1]:raise ValueError('source work and fine radial domains differ')
    nodes=sorted(set(a)|set(b));radial=np.asarray([float(x) for x in nodes])
    count=int(angular_nodes)
    if count<4 or count%4 or np.any(np.diff(radial)<=0):raise ValueError('strict numerical radial union and complete angular grid required')
    theta=np.arange(count)*2*np.pi/count
    definition={'schema':'exact-source-work-fine-radial-union-objective-grid-v1',
        'source_work_sampling_definition_sha256':digest(work),
        'source_fine_sampling_definition_sha256':digest(fine),
        'old_work_radial_count':len(a),'old_fine_radial_count':len(b),'union_radial_count':len(nodes),
        'old_work_is_subset_of_old_fine':set(a)<=set(b),
        'radial_nodes_exact':[str(x) for x in nodes],
        'construction':'sorted exact rational set union; no displaced, deleted or fitted source nodes',
        'angular_nodes':count,'angular_definition':'theta_j=2*pi*j/angular_nodes for j=0..N-1',
        'new_sampled_maximum_objective_not_the_old_work_objective':True,
        'physical_metric_and_model_not_changed_by_sampling':True}
    definition['definition_sha256']=digest(definition)
    return radial,theta,definition


def summary_path(out):return out.with_name(out.stem+'-summary.json')


def small_summary(report,out):
    result={key:report[key] for key in ['schema','status','phase','source_files_sha256','configuration',
        'exact_input_storage','input_replay','github_sha','github_run_id','github_repository',
        'artificial_inputs_only','old_optimizer_calls_this_run','old_auxiliary_delta',
        'new_auxiliary_initialization','initial_current_constraints','final_work_constraints',
        'final_fine_constraints','final_doubled_constraints','selected_raw_auxiliary_delta',
        'unchanged_physical_metric_and_b0','elapsed_seconds','peak_rss_kib_linux','error'] if key in report}
    for key in ['initial_state','final_state']:
        if key in report:result[key]=compact_state(report[key])
    for key in ['initial_work_audit','final_work_audit','final_fine_audit','final_doubled_angle_audit']:
        if key in report:result[key]=compact_audit(report[key])
    if 'same_parameter_Pi_refinement' in report:result['same_parameter_Pi_refinement']=compact_comparison(report['same_parameter_Pi_refinement'])
    for key in ['work_sampling_definition','fine_sampling_definition']:
        if key in report:
            grid=report[key];result[key]={name:grid.get(name) for name in ['schema','definition_sha256',
                'old_work_radial_count','old_fine_radial_count','union_radial_count','angular_nodes']}
    stage=report.get('dense_epigraph_stage')
    if stage:
        result['dense_epigraph_stage']={key:stage.get(key) for key in ['status','error','budget_message','solver','selected_point']}
        snapshot=stage.get('checkpoint',{})
        result['dense_epigraph_stage']['checkpoint']={key:snapshot.get(key) for key in ['physical_geometry_evaluations',
            'epigraph_vector_evaluations','elapsed_seconds','final_selection','objective_evaluation_sha256',
            'maximum_geometry_cache_array_bytes','maximum_single_constraint_Jacobian_bytes']}
        for key in ['best_physical_max_eta_point','best_eligible_direct_max_eta_point','best_eligible_auxiliary_delta_point']:
            point=snapshot.get(key);result['dense_epigraph_stage']['checkpoint'][key]=None if point is None else {
                name:point.get(name) for name in ['physical_state_sha256','auxiliary_delta_evaluated','record']}
    raw=out.read_bytes();result['full_report']={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    result.update(sampled_only=True,task_complete=False,no_whole_reach_or_curvature_certificate=True,
        old_underestimated_delta_and_original_run_acceptance_not_rewritten=True)
    return result


def save_report(out,report):
    atomic_save(out,report);atomic_save(summary_path(out),small_summary(report,out))


def prepare_run(args,*,artificial=False):
    bindings={};phase='eight-input-public-repository-guard'
    try:
        if args.trial_audit is None or not args.expected_trial_sha256:
            raise ValueError('explicit eighth read-only audit path and decoded SHA256 required')
        paths=[args.input,args.anchor_input,args.short_audit,args.height_audit,args.prior_joint_audit,
            args.resume_audit,args.epigraph_audit,args.trial_audit]
        if not artificial:require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        phase='eighth-readonly-report-byte-binding'
        eighth,raw,binding=read_input(args.trial_audit,args.expected_trial_sha256)
        bindings['saved_trial_readonly_audit']=binding
        phase='unchanged-seven-input-replay'
        previous=prepare_saved_trial(args,artificial=artificial);bindings.update(previous[1])
        phase='read-only-result-physical-identity-and-exact-grids'
        restored,receipt=replay_readonly_audit(previous,eighth,artificial=artificial)
        return restored,bindings,eighth,receipt
    except Exception as error:
        report={'schema':SCHEMA,'status':'input-replay-failed-before-dense-research-geometry','phase':phase,
            'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,'new_solver_calls':0,
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out,report);raise


def run_restart(prepared,out,*,artificial=False,evaluate_only=False):
    restored,bindings,eighth,replay=prepared
    problem,initial,old_delta,gate,lower,upper,old_cfg,work_cfg,source_cfg,unused=restored
    cfg=configuration()
    if artificial:
        cfg.update(minimum_signed_height_exact='-10',hard_ball_radius_exact='10',hard_strip_half_width_exact='10',
            mirror_target_exact='1/1000000000000',normal_area_numerical_floor=0.,
            maxiter=2,max_physical_evaluations=4,max_seconds=120.)
    started=time.monotonic();metric=copy.deepcopy(problem.metric_model(initial));b0=copy.deepcopy(problem.height_base_definition)
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
        'input_replay':replay,'configuration':cfg,'github_sha':os.environ.get('GITHUB_SHA'),
        'github_run_id':os.environ.get('GITHUB_RUN_ID'),'github_repository':os.environ.get('GITHUB_REPOSITORY'),
        'artificial_inputs_only':bool(artificial),'old_optimizer_calls_this_run':0,
        'old_auxiliary_delta':old_delta,'initial_state':state_record(problem,initial),
        'unchanged_physical_metric_and_b0':True,
        'new_solver_will_use_a_new_explicit_auxiliary_initial_bound':True}
    def save(status):
        report['status']=status;report['elapsed_seconds']=time.monotonic()-started
        report['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        save_report(out,report)
    save('eight-inputs-replayed-original-physical-start-preserved-before-preflight')
    try:
        report['phase']='exact-radial-union-and-one-new-work-preflight'
        radial,theta,grid=union_grid(eighth,work_cfg['joint_angular_nodes'])
        report['work_sampling_definition']=grid;order=int(source_cfg['primitive_order'])
        def checkpoint(value):
            report['dense_epigraph_stage']={'status':'dense-current-checkpoint','checkpoint':value}
            save('dense-minimax-physical-and-auxiliary-best-checkpoint')
        objective=DenseMirrorEpigraphObjective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition.update(eighth_readonly_input_decoded_sha256=bindings['saved_trial_readonly_audit']['decoded_sha256'],
            exact_radial_union_definition=grid,old_auxiliary_delta_is_provenance_not_new_start=True)
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        vector=objective.initial_vector(initial);record=objective.evaluate(vector)
        report['new_auxiliary_initialization']={'old_auxiliary_delta':old_delta,
            'new_auxiliary_delta':float(vector[-1]),'new_exact_binary64_delta':str(Q.from_float(float(vector[-1]))),
            'new_work_direct_max_eta':record['decision']['direct_max_eta'],
            'rule':'max(2*delta_min, new_work_max_eta+(1+new_work_max_eta)/1000000)',
            'does_not_modify_the_old_run_or_old_auxiliary_value':True,
            'does_not_change_the_physical_coefficients_or_g':True}
        report['initial_current_constraints']=record['decision']
        report['initial_work_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        save('new-work-initial-physical-mirror-and-explicit-auxiliary-gates-recorded')
        report['phase']='one-dense-minimax-invocation'
        stage=run_dense_epigraph(objective,initial,artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report['dense_epigraph_stage']=stage
        point=stage['checkpoint'].get('best_physical_max_eta_point')
        if point is None:
            save('dense-initial-or-trials-had-no-physical-and-mirror-eligible-point');return report
        final=np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if exact_coefficients(final)!=point['exact_binary64_physical_coefficients']:
            raise ValueError('physical-best exact coefficient roundtrip failed')
        delta=float(Q(point['auxiliary_delta_exact_binary64']))
        if delta!=point['auxiliary_delta_evaluated']:raise ValueError('saved raw auxiliary scalar changed')
        identity=problem.identity(final)
        if digest(identity)!=point['physical_state_sha256']:raise ValueError('physical-best canonical state differs')
        frozen,fc=problem.frozen_metric_copy(final)
        if (fc.tobytes()!=final.tobytes() or frozen.identity(fc)!=identity
                or frozen.metric_model(fc)!=metric or frozen.height_base_definition!=b0):
            raise ArithmeticError('selected state freeze changed g, b0, coefficients or physical identity')
        problem=frozen;final=fc
        report.update(final_state=state_record(problem,final),selected_raw_auxiliary_delta=delta,
            selection='best physical/mirror-gated actual maximum eta; auxiliary feasibility recorded separately',
            selected_raw_delta_not_inflated_at_final_audit=True)
        report['phase']='independent-selected-state-work-and-fine-audit'
        work=problem.geometry(final,radial,theta,order)
        report['final_work_audit']=audit_data(problem,final,work,source_cfg['tau'])
        report['final_work_constraints']=candidate_decision(problem,gate,final,delta,work,lower,upper,cfg)
        save('selected-physical-best-independent-work-audit-complete')
        del objective,work
        fine_theta=np.arange(int(source_cfg['angular_nodes']))*2*np.pi/int(source_cfg['angular_nodes'])
        fine_grid=copy.deepcopy(grid);fine_grid.pop('definition_sha256');fine_grid['angular_nodes']=len(fine_theta)
        fine_grid['fixed_state_refinement_not_a_second_objective']=True;fine_grid['definition_sha256']=digest(fine_grid)
        report['fine_sampling_definition']=fine_grid
        fine=problem.geometry(final,radial,fine_theta,order)
        report['final_fine_audit']=audit_data(problem,final,fine,source_cfg['tau'])
        report['final_fine_constraints']=candidate_decision(problem,gate,final,delta,fine,lower,upper,cfg)
        save('selected-physical-best-fine-audit-before-angle-doubling')
        doubled_theta=np.arange(2*len(fine_theta))*np.pi/len(fine_theta)
        doubled=problem.geometry(final,radial,doubled_theta,order)
        report['final_doubled_angle_audit']=audit_data(problem,final,doubled,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints']=candidate_decision(problem,gate,final,delta,doubled,lower,upper,cfg)
        report['same_parameter_Pi_refinement']=compare_data(problem,fine,problem,doubled,final,
            name='one dense-mirror-minimax physical-best state, with saved raw auxiliary delta unchanged',theta_stride=2)
        if problem.identity(final)!=identity:raise ArithmeticError('final angle refinement altered the physical state')
        report['limitations']={'finer_angles_can_reveal_a_new_metric_or_mirror_peak':True,
            'raw_auxiliary_failure_does_not_erase_a_gated_physical_point':True,
            'curvature_and_other_nonlocal_pairs_remain_unconstrained_and_diagnosed':True,
            'no_reoptimization_after_fixed_state_refinement':True,'sampled_constraints_are_not_continuous_certificates':True}
        save('complete-one-dense-mirror-minimax-and-physical-best-audit');return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('dense-minimax-error-preserved-initial-and-completed-checkpoints');return report


def developer_check():
    arrays=array_check()
    with tempfile.TemporaryDirectory(prefix='dense-mirror-minimax-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder);args,previous,seventh=artificial_seven_inputs(directory)
        saved=prepare_saved_trial(args,artificial=True)
        eighth=run_saved_trial_audit(saved,args.out,artificial=True)
        if eighth['status']!='complete-one-saved-unaccepted-trial-fixed-state-audit':
            raise ArithmeticError('the artificial zero-solve eighth report failed')
        args.trial_audit=args.out;args.expected_trial_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest()
        args.out=directory/'dense-artificial.json'
        prepared=prepare_run(args,artificial=True)
        report=run_restart(prepared,args.out,artificial=True,evaluate_only=True)
        summary=json.loads(summary_path(args.out).read_text())
        binding=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        old=prepared[0][2];new=report.get('new_auxiliary_initialization',{})
        no_solve=report.get('dense_epigraph_stage',{}).get('solver',{}).get('minimize_invocation_count')==0
        same=(report.get('final_state',{}).get('canonical_physical_state_sha256')==
            report.get('initial_state',{}).get('canonical_physical_state_sha256'))
        wrong=copy.copy(args);wrong.expected_trial_sha256='0'*64;wrong.out=directory/'wrong-eighth.json'
        try:prepare_run(wrong,artificial=True);bad_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text());bad_sha=(failure['phase']=='eighth-readonly-report-byte-binding'
                and failure['new_solver_calls']==0)
        corrupt=copy.deepcopy(eighth);corrupt['trial_state']['canonical_physical_state_sha256']='0'*64
        try:replay_readonly_audit(saved,corrupt,artificial=True);bad_state=False
        except ValueError:bad_state=True
        corrupt=copy.deepcopy(eighth);corrupt['fine_sampling_definition']['radial_nodes_exact'][1]='1/999'
        try:replay_readonly_audit(saved,corrupt,artificial=True);bad_grid=False
        except ValueError:bad_grid=True
        # Independent union coverage check does not touch any candidate geometry.
        synthetic={'work_sampling_definition':{'radial_nodes_exact':['0','1/2','1']},
            'fine_sampling_definition':{'radial_nodes_exact':['0','1/3','2/3','1']}}
        unused_r,unused_t,g=union_grid(synthetic,8)
        union_ok=g['radial_nodes_exact']==['0','1/3','1/2','2/3','1']
    passed=bool(arrays['passed'] and report['status']=='complete-one-dense-mirror-minimax-and-physical-best-audit'
        and no_solve and same and new.get('old_auxiliary_delta')==old
        and new.get('new_auxiliary_delta',0)>new.get('new_work_direct_max_eta',np.inf)
        and binding and bad_sha and bad_state and bad_grid and union_ok)
    return {'schema':'dense-mirror-minimax-eight-input-development-v1','artificial_inputs_only':True,
        'research_candidate_evaluated_or_optimized':False,'targeted_array_checks':arrays,
        'complete_main_status':report['status'],'complete_main_error':report.get('error'),
        'complete_main_calls_no_optimizer':no_solve,'physical_state_unchanged_by_evaluation_only':same,
        'old_delta_preserved_and_new_initial_delta_explicitly_assigned':new,
        'work_grid_keeps_exact_source_union':bool(union_ok),'wrong_eighth_SHA_saves_failure':bad_sha,
        'modified_full_state_rejected':bad_state,'modified_exact_fine_node_rejected':bad_grid,
        'summary_bound_to_actual_full_output_bytes':binding,
        'final_same_physical_Pi_refinement':report.get('same_parameter_Pi_refinement'),'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['input','anchor-input','short-audit','height-audit','prior-joint-audit','resume-audit','epigraph-audit','trial-audit']:
        parser.add_argument('--'+name,type=Path)
    for name in ['input','anchor','short','height','prior-joint','resume','epigraph','trial']:
        parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'dense-mirror-minimax-development-error-v1','passed':False,
                'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result['source_files_sha256']=implementation_hashes();atomic_save(args.out,result)
        print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    try:prepared=prepare_run(args)
    except Exception:raise SystemExit(1)
    report=run_restart(prepared,args.out)
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)
    if report['status']!='complete-one-dense-mirror-minimax-and-physical-best-audit':raise SystemExit(1)


if __name__=='__main__':main()

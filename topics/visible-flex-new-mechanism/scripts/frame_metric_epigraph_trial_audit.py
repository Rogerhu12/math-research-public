#!/usr/bin/env python3
"""Read-only refinement of one published, originally unaccepted epigraph trial.

Seven exact reports bind the physical coefficients and the old auxiliary delta.
No optimizer is called and delta is not enlarged. A trial that failed its old
auxiliary bound remains explicitly unaccepted in that original run.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import gzip
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
    compact_state,compact_audit,compact_comparison)
from frame_independent_height_solve import state_record
from frame_metric_epigraph import MetricEpigraphObjective,candidate_decision,configuration
from frame_metric_epigraph_audit import (prepare_maximum,run_maximum,artificial_fixture,
    implementation_hashes as maximum_hashes,SCHEMA as MAXIMUM_SCHEMA)

SCHEMA='published-unaccepted-epigraph-physical-trial-fixed-state-audit-v1'


def implementation_hashes():
    result=maximum_hashes();result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def exact_coefficients(values):return [str(Q.from_float(float(x))) for x in values]


def physical_gate_summary(decision):
    return {'cap_and_coefficient_boxes':bool(decision['cap_and_box']['eligible_under_declared_numerical_gate_tolerances']),
        'signed_height':bool(decision['signed_height_pass']),'ball':bool(decision['hard_ball_pass']),
        'strip':bool(decision['hard_strip_pass']),
        'all_four_physical_gate_groups_pass':bool(decision['cap_and_box']['eligible_under_declared_numerical_gate_tolerances']
            and decision['signed_height_pass'] and decision['hard_ball_pass'] and decision['hard_strip_pass']),
        'old_auxiliary_delta_passes_divided_metric_rows':bool(decision['divided_metric_row_pass']),
        'old_auxiliary_delta_covers_direct_max_eta':bool(decision['independent_direct_eta_pass']),
        'original_all_gate_eligibility_with_unchanged_delta':bool(decision['eligible_under_all_declared_sampled_constraints']),
        'these_are_sampled_numerical_conditions_not_a_complete_geometric_certificate':True}


def replay_trial(prepared,published,*,artificial=False):
    result,bindings,previous=prepared
    problem,initial,gate,lower,upper,work_cfg,source_cfg,receipt=result
    if (published.get('schema')!=MAXIMUM_SCHEMA or published.get('status')!=
            'complete-one-true-max-metric-epigraph-and-fixed-state-audit'):
        raise ValueError('a complete published maximum-metric audit is required')
    if bool(published.get('artificial_inputs_only'))!=bool(artificial):
        raise ValueError('artificial and research seventh inputs cannot be interchanged')
    if published.get('source_files_sha256')!=maximum_hashes():
        raise ValueError('seventh report implementation differs from its frozen source')
    for key,binding in bindings.items():
        old=published.get('exact_input_storage',{}).get(key,{})
        for field in ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']:
            if old.get(field)!=binding.get(field):raise ValueError('seventh report source binding differs: '+key+'/'+field)
    if published.get('input_replay')!=receipt:raise ValueError('seventh report consumes another six-input physical model')
    if (published.get('previous_optimizer_calls_this_run')!=0 or published.get('error')
            or not published.get('physical_metric_and_b0_unchanged')):
        raise ValueError('seventh report did not preserve its declared physical family')
    if published.get('initial_state')!=state_record(problem,initial):
        raise ValueError('maximum-metric run initial full state does not replay')
    cfg=configuration()
    if artificial:cfg.update(minimum_signed_height_exact='-10',hard_ball_radius_exact='10',
        hard_strip_half_width_exact='10',max_seconds=120.,max_physical_evaluations=4,maxiter=2)
    if published.get('configuration')!=cfg:raise ValueError('the published epigraph configuration changed')
    stage=published['epigraph_stage'];checkpoint=stage['checkpoint']
    if stage.get('solver',{}).get('minimize_invocation_count')!=(0 if artificial else 1):
        raise ValueError('one prior actual optimizer or an explicit zero-solve artificial fixture is required')
    if checkpoint.get('configuration')!=cfg or checkpoint.get('height_gate')!=gate.record():
        raise ValueError('the original epigraph configuration or complete cap row changed')
    if (not np.array_equal(np.asarray(checkpoint['physical_box_lower'],float),lower)
            or not np.array_equal(np.asarray(checkpoint['physical_box_upper'],float),upper)):
        raise ValueError('the published physical boxes changed')
    t,theta,grid=build_grid(problem,work_cfg['joint_radial_nodes'],work_cfg['joint_collar_subdivisions'],work_cfg['joint_angular_nodes'])
    if grid!=published.get('work_sampling_definition'):raise ValueError('the exact original epigraph work grid changed')
    context=MetricEpigraphObjective(problem,gate,t,theta,source_cfg['primitive_order'],lower,upper,cfg=cfg)
    context.evaluation_definition['sixth_input_decoded_sha256']=bindings['latest_joint_resume']['decoded_sha256']
    context.evaluation_definition['one_new_objective_no_repeated_prior_solve']=True
    context.evaluation_sha256=digest(context.evaluation_definition)
    if (checkpoint.get('objective_evaluation_definition')!=context.evaluation_definition
            or checkpoint.get('objective_evaluation_sha256')!=context.evaluation_sha256):
        raise ValueError('complete published objective evaluation identity does not replay')
    accepted=checkpoint['best_eligible_direct_max_eta_point']
    if accepted is None:raise ValueError('the source must separately retain its originally accepted state')
    accepted_state=np.asarray(accepted['physical_parameter_coefficients_binary64'],float)
    if (exact_coefficients(accepted_state)!=accepted['exact_binary64_physical_coefficients']
            or digest(problem.identity(accepted_state))!=accepted['physical_state_sha256']
            or published.get('final_state')!=state_record(problem,accepted_state)):
        raise ValueError('the source originally accepted final physical state is inconsistent')
    point=checkpoint.get('lowest_delta_trial_may_be_ineligible')
    if point is None:raise ValueError('the one declared saved trial is absent')
    state=np.asarray(point['physical_parameter_coefficients_binary64'],float)
    if state.shape!=(problem.nunknown,) or not np.all(np.isfinite(state)):
        raise ValueError('complete finite saved trial coefficients required')
    if exact_coefficients(state)!=point['exact_binary64_physical_coefficients']:
        raise ValueError('trial coefficients do not match their exact binary64 rationals')
    if digest(problem.identity(state))!=point['physical_state_sha256']:
        raise ValueError('saved trial full physical identity does not replay')
    delta=float(Q(point['auxiliary_delta_exact_binary64']))
    if not np.isfinite(delta) or delta<=0 or delta!=point['auxiliary_delta_evaluated']:
        raise ValueError('the exact old auxiliary scalar does not replay')
    old_decision=point['record']['decision'];physical=physical_gate_summary(old_decision)
    if old_decision.get('auxiliary_delta')!=delta or point['record'] not in checkpoint['history']:
        raise ValueError('the declared trial does not match its original saved evaluation record')
    if (not physical['all_four_physical_gate_groups_pass']
            or old_decision['eligible_under_all_declared_sampled_constraints']
            or old_decision['independent_direct_eta_pass']):
        raise ValueError('this consumer is only for the explicit physically screened but under-bounded auxiliary trial')
    if problem.metric_model(state)!=problem.metric_model(initial):raise ValueError('saved trial changed the complete target metric')
    record={'schema':'strict-seven-input-saved-epigraph-trial-replay-v1',
        'source_originally_accepted_physical_sha256':accepted['physical_state_sha256'],
        'trial_physical_sha256':point['physical_state_sha256'],
        'trial_physical_parameter_count':problem.nunknown,
        'all_trial_binary64_rational_coefficients_replayed':True,
        'complete_fixed_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'original_height_gate_boxes_b0_and_current_parameter_layout_retained':True,
        'original_trial_record':copy.deepcopy(point['record']),
        'original_trial_physical_gate_summary':physical,
        'old_auxiliary_delta_exact_binary64':point['auxiliary_delta_exact_binary64'],
        'the_trial_was_not_accepted_in_the_original_run':True,
        'the_original_run_final_state_and_success_claim_are_not_rewritten':True,
        'history_direct_max_eta_minimum':min(row['decision']['direct_max_eta'] for row in checkpoint['history']),
        'history_evaluation_count':len(checkpoint['history']),
        'no_new_trial_search_or_optimizer_invocation':True}
    return problem,state,delta,gate,lower,upper,cfg,work_cfg,source_cfg,record


def summary_path(out):return out.with_name(out.stem+'-summary.json')


def compact_summary(report,out):
    result={key:report[key] for key in ['schema','status','phase','source_files_sha256','exact_input_storage',
        'input_replay','github_sha','github_run_id','github_repository','artificial_inputs_only',
        'optimizer_calls','auxiliary_delta_reassigned','retained_old_auxiliary_delta',
        'same_complete_metric_b0_and_coefficients','current_work_constraints','fine_constraints','doubled_constraints',
        'physical_gates_on_work','physical_gates_on_fine','physical_gates_on_doubled',
        'original_work_grid_replay_scalar_differences',
        'elapsed_seconds','peak_rss_kib_linux','error','input_failure'] if key in report}
    if 'trial_state' in report:result['trial_state']=compact_state(report['trial_state'])
    for key in ['current_work_audit','fine_audit','doubled_angle_audit']:
        if key in report:result[key]=compact_audit(report[key])
    if 'same_parameter_Pi_refinement' in report:result['same_parameter_Pi_refinement']=compact_comparison(report['same_parameter_Pi_refinement'])
    raw=out.read_bytes();result['full_report']={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    result.update(original_run_did_not_accept_this_trial=True,sampled_only=True,task_complete=False,
        no_convergence_embedding_curvature_or_whole_reach_certificate=True)
    return result


def save_report(out,report):
    atomic_save(out,report);atomic_save(summary_path(out),compact_summary(report,out))


def prepare_run(args,*,artificial=False):
    bindings={};phase='seven-input-public-repository-guard'
    try:
        if args.epigraph_audit is None or not args.expected_epigraph_sha256:
            raise ValueError('explicit seventh report and decoded SHA256 required')
        paths=[args.input,args.anchor_input,args.short_audit,args.height_audit,args.prior_joint_audit,args.resume_audit,args.epigraph_audit]
        if not artificial:require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        phase='seventh-report-byte-binding'
        seventh,raw,binding=read_input(args.epigraph_audit,args.expected_epigraph_sha256)
        bindings['completed_epigraph_audit']=binding
        phase='unchanged-six-input-replay'
        previous=prepare_maximum(args,artificial=artificial);bindings.update(previous[1])
        phase='saved-unaccepted-trial-identity-and-original-failure-replay'
        restored=replay_trial(previous,seventh,artificial=artificial)
        return restored,bindings,seventh
    except Exception as error:
        report={'schema':SCHEMA,'status':'input-replay-failed-before-new-trial-geometry','phase':phase,
            'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
            'artificial_inputs_only':bool(artificial),'optimizer_calls':0,'auxiliary_delta_reassigned':False,
            'error':{'type':type(error).__name__,'message':str(error)}}
        save_report(args.out,report);raise


def run_audit(prepared,out,*,artificial=False):
    restored,bindings,seventh=prepared
    problem,state,delta,gate,lower,upper,cfg,work_cfg,source_cfg,receipt=restored
    started=time.monotonic();identity=problem.identity(state);metric=problem.metric_model(state)
    baseline=copy.deepcopy(problem.height_base_definition)
    answer={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'exact_input_storage':bindings,
        'input_replay':receipt,'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'optimizer_calls':0,'auxiliary_delta_reassigned':False,'retained_old_auxiliary_delta':delta,
        'trial_state':state_record(problem,state),'source_original_run_final_state_sha256':
            seventh['final_state']['canonical_physical_state_sha256'],
        'this_trial_remains_unaccepted_by_the_original_run':True}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-started
        answer['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        save_report(out,answer)
    save('saved-physical-trial-and-original-auxiliary-failure-replayed')
    try:
        frozen,fc=problem.frozen_metric_copy(state)
        if fc.tobytes()!=state.tobytes() or frozen.identity(fc)!=identity or frozen.metric_model(fc)!=metric:
            raise ArithmeticError('trial freeze changed the complete physical state')
        problem=frozen;state=fc
        if problem.height_base_definition!=baseline:raise ArithmeticError('trial freeze changed b0')
        answer['same_complete_metric_b0_and_coefficients']=True
        answer['phase']='original-work-grid-trial-diagnostic'
        t,theta,grid=build_grid(problem,work_cfg['joint_radial_nodes'],work_cfg['joint_collar_subdivisions'],work_cfg['joint_angular_nodes'])
        if grid!=seventh['work_sampling_definition']:raise ValueError('saved trial original objective grid changed')
        answer['work_sampling_definition']=grid;order=source_cfg['primitive_order']
        work=problem.geometry(state,t,theta,order)
        answer['current_work_audit']=audit_data(problem,state,work,source_cfg['tau'])
        answer['current_work_constraints']=candidate_decision(problem,gate,state,delta,work,lower,upper,cfg)
        answer['physical_gates_on_work']=physical_gate_summary(answer['current_work_constraints'])
        old=receipt['original_trial_record']['decision'];new=answer['current_work_constraints']
        answer['original_work_grid_replay_scalar_differences']={key:float(new[key]-old[key])
            for key in ['direct_max_eta','minimum_signed_height','ball_radius_squared_normalized_max',
                        'maximum_absolute_y','divided_metric_row_min']}
        answer['original_work_grid_replay_scalar_differences']['common_cap_height']=float(
            new['cap_and_box']['reconstructed_common_cap_height_evaluated']-
            old['cap_and_box']['reconstructed_common_cap_height_evaluated'])
        save('original-grid-physical-and-old-auxiliary-conditions-separated')
        answer['phase']='one-physical-trial-complete-fine-grid'
        fine_t,fine_theta,fine_grid=build_grid(problem,source_cfg['radial_nodes'],source_cfg['collar_subdivisions'],source_cfg['angular_nodes'])
        if fine_grid!=seventh['fine_sampling_definition']:raise ValueError('saved original fine-grid definition changed')
        answer['fine_sampling_definition']=fine_grid
        fine=problem.geometry(state,fine_t,fine_theta,order)
        answer['fine_audit']=audit_data(problem,state,fine,source_cfg['tau'])
        answer['fine_constraints']=candidate_decision(problem,gate,state,delta,fine,lower,upper,cfg)
        answer['physical_gates_on_fine']=physical_gate_summary(answer['fine_constraints'])
        save('one-saved-trial-fine-metric-curvature-mirror-audit-complete')
        answer['phase']='unchanged-trial-angle-doubling'
        doubled_theta=np.arange(2*len(fine_theta))*np.pi/len(fine_theta)
        doubled=problem.geometry(state,fine_t,doubled_theta,order)
        answer['doubled_angle_audit']=audit_data(problem,state,doubled,source_cfg['tau'],with_rows=False)
        answer['doubled_constraints']=candidate_decision(problem,gate,state,delta,doubled,lower,upper,cfg)
        answer['physical_gates_on_doubled']=physical_gate_summary(answer['doubled_constraints'])
        answer['same_parameter_Pi_refinement']=compare_data(problem,fine,problem,doubled,state,
            name='one previously unaccepted saved physical trial, retaining its original auxiliary delta',theta_stride=2)
        if problem.identity(state)!=identity:raise ArithmeticError('read-only trial refinement changed the physical identity')
        answer['limitations']={'old_auxiliary_failure_is_preserved_not_relabeled_as_convergence':True,
            'a_future_restart_would_need_an_explicit_new_auxiliary_initial_bound':True,
            'finite_refinement_is_not_a_continuous_bound':True,
            'curvature_and_mirror_checks_are_independent_of_eta':True}
        save('complete-one-saved-unaccepted-trial-fixed-state-audit');return answer
    except Exception as error:
        answer['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('trial-audit-error-with-preserved-diagnostics');return answer


def artificial_seven_inputs(directory):
    args,unused,latest=artificial_fixture(directory)
    previous=prepare_maximum(args,artificial=True)
    source=run_maximum(previous,args.out,artificial=True,evaluate_only=True)
    if source['status']!='complete-one-true-max-metric-epigraph-and-fixed-state-audit':
        raise ArithmeticError('the explicit six-report artificial source did not complete its no-solve audit')
    problem,initial,gate,lower,upper,work_cfg,source_cfg,receipt=previous[0]
    cfg=source['configuration'];t,theta,grid=build_grid(problem,work_cfg['joint_radial_nodes'],
        work_cfg['joint_collar_subdivisions'],work_cfg['joint_angular_nodes'])
    objective=MetricEpigraphObjective(problem,gate,t,theta,source_cfg['primitive_order'],lower,upper,cfg=cfg)
    objective.evaluation_definition['sixth_input_decoded_sha256']=previous[1]['latest_joint_resume']['decoded_sha256']
    objective.evaluation_definition['one_new_objective_no_repeated_prior_solve']=True
    objective.evaluation_sha256=digest(objective.evaluation_definition)
    vector=objective.initial_vector(initial);objective.evaluate(vector)
    trial=initial.copy();trial[0]+=1e-4
    data=objective.physical_geometry(trial);delta=float(np.max(data['eta']))/2
    record=objective.evaluate(np.r_[trial,delta])
    if not physical_gate_summary(record['decision'])['all_four_physical_gate_groups_pass']:
        raise ArithmeticError('the explicit artificial under-bounded trial must satisfy its relaxed physical gates')
    if record['decision']['eligible_under_all_declared_sampled_constraints']:
        raise ArithmeticError('the explicit artificial auxiliary delta must fail')
    source['epigraph_stage']={'status':'explicit-artificial-two-vectors-no-optimizer',
        'solver':{'minimize_invocation_count':0,'artificial_inputs_only':True},'checkpoint':objective.snapshot(),
        'explicit_artificial_fixture_not_a_claimed_public_solver_run':True}
    source['final_state']=state_record(problem,initial)
    path=directory/'epigraph-seventh.json.gz';raw=json.dumps(source,sort_keys=True).encode();path.write_bytes(gzip.compress(raw))
    args.epigraph_audit=path;args.expected_epigraph_sha256=hashlib.sha256(raw).hexdigest();args.out=directory/'trial-audit.json'
    return args,previous,source


def developer_check():
    with tempfile.TemporaryDirectory(prefix='epigraph-saved-trial-artificial-',dir='/dev/shm') as folder:
        args,previous,seventh=artificial_seven_inputs(Path(folder));prepared=prepare_run(args,artificial=True)
        report=run_audit(prepared,args.out,artificial=True);summary=json.loads(summary_path(args.out).read_text())
        bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args);wrong.expected_epigraph_sha256='0'*64;wrong.out=Path(folder)/'wrong-seventh.json'
        try:prepare_run(wrong,artificial=True);bad_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text());bad_sha=failure['phase']=='seventh-report-byte-binding' and failure['optimizer_calls']==0
        changed=copy.deepcopy(seventh);changed['epigraph_stage']['checkpoint']['lowest_delta_trial_may_be_ineligible']['physical_state_sha256']='0'*64
        try:replay_trial(previous,changed,artificial=True);bad_state=False
        except ValueError:bad_state=True
    constraint=report.get('current_work_constraints',{});old=prepared[0][-1]['original_trial_record']['decision']
    unchanged_delta=report.get('retained_old_auxiliary_delta')==old['auxiliary_delta']
    different_state=(report.get('trial_state',{}).get('canonical_physical_state_sha256')!=
        report.get('source_original_run_final_state_sha256'))
    passed=bool(report['status']=='complete-one-saved-unaccepted-trial-fixed-state-audit'
        and report['optimizer_calls']==0 and not report['auxiliary_delta_reassigned']
        and unchanged_delta and different_state and not constraint.get('independent_direct_eta_pass',True)
        and report.get('physical_gates_on_work',{}).get('all_four_physical_gate_groups_pass')
        and bound and bad_sha and bad_state)
    return {'schema':'seven-input-unaccepted-epigraph-trial-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_evaluated_or_optimized':False,'optimizer_calls':0,
        'full_main_status':report['status'],'full_main_error':report.get('error'),
        'trial_differs_from_original_accepted_physical_state':different_state,
        'original_auxiliary_delta_unchanged':unchanged_delta,'original_auxiliary_failure_preserved':
            not constraint.get('independent_direct_eta_pass',True),
        'physical_gates_reported_separately':report.get('physical_gates_on_work'),
        'wrong_seventh_SHA_saves_small_failure':bad_sha,'modified_trial_canonical_state_rejected':bad_state,
        'summary_byte_binding':bound,'same_state_Pi_refinement':report.get('same_parameter_Pi_refinement'),'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['input','anchor-input','short-audit','height-audit','prior-joint-audit','resume-audit','epigraph-audit']:
        parser.add_argument('--'+name,type=Path)
    for name in ['input','anchor','short','height','prior-joint','resume','epigraph']:
        parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:answer=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'saved-epigraph-trial-development-error-v1','passed':False,
                'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        answer['source_files_sha256']=implementation_hashes();atomic_save(args.out,answer)
        print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
        if not answer['passed']:raise SystemExit(1)
        return
    try:prepared=prepare_run(args)
    except Exception:raise SystemExit(1)
    answer=run_audit(prepared,args.out)
    print(json.dumps({'out':str(args.out),'status':answer['status']}),flush=True)
    if answer['status']!='complete-one-saved-unaccepted-trial-fixed-state-audit':raise SystemExit(1)


if __name__=='__main__':main()

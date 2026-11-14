#!/usr/bin/env python3
"""Reuse a completed quartic report and run only its uncalled joint stage.

The completed quartic candidate is tested on the current joint grid.  If it
fails the declared positive signed-height guard, the original accepted height
state is tested instead.  No coefficient projection and no quartic solve are
performed.  Research evaluation is restricted to this public repository's
Actions; --check-only uses explicit artificial carriers and arrays only.
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

import numpy as np

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_entry_paired_repair_audit import require_public_actions,JETS
from frame_entry_short_bounded_audit import (
    read_input,build_grid,audit_data,compare_data,compact_state,compact_audit,
    compact_comparison,summary_path,artificial_inputs,default_configuration as short_defaults,
    implementation_hashes as short_hashes)
from frame_independent_height_solve import state_record
from frame_entry_paired_repair import EntryRepairProblem
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_height_polytope_audit import (
    load_short_model,proposal_polytope,stage_configuration as height_configuration,
    implementation_hashes as height_hashes)
from frame_height_quartic_joint_audit import (
    SCHEMA as PRIOR_SCHEMA,prepare_run as prepare_original_inputs,
    implementation_hashes as prior_hashes,configuration as prior_configuration,
    exact_evaluated_scalar)
from frame_entry_single_q import SingleQProblem
from frame_height_affine_gate import HeightAffineGate,frozen_family
from frame_joint_height_objective import (
    JointSignedHeightObjective,run_joint_slsqp,_JointArrayProblem)

SCHEMA='published-quartic-reuse-one-joint-with-explicit-warm-selection-v1'


def implementation_hashes():
    result=prior_hashes()
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def configuration(previous=None):
    previous=prior_configuration() if previous is None else previous
    keep=['joint_maxiter','joint_max_evaluations','joint_max_seconds','joint_ftol',
        'joint_radial_nodes','joint_angular_nodes','joint_collar_subdivisions',
        'old_tangent_lower','old_tangent_upper','new_Q_lower','new_Q_upper',
        'height_tolerance','signed_z_tolerance','box_tolerance',
        'height_reconstruction_tolerance','checkpoint_evaluations','checkpoint_seconds']
    result={k:copy.deepcopy(previous[k]) for k in keep}
    result.update(minimum_signed_height_exact='1/10000',
        positive_height_guard_is_numerical_solve_protection_not_reach=True,
        warm_start_order=['published_post_quartic','original_accepted_height'],
        quartic_solver_calls_permitted=0,joint_solver_calls_permitted=1,
        old_metric_height_reference_cap_row_and_parameter_boxes_unchanged=True,
        previous_zero_height_tolerance_is_not_relaxed=True,joint_evaluate_only=False)
    return result


def exact_coefficients(values):
    return [str(Q.from_float(float(x))) for x in values]


def restore_gate(problem,state,record):
    """Retain the already published physical and numerical cap row exactly."""
    physical=record['physical_definition'];numerical=record['numerical_definition']
    if (digest(physical)!=record['physical_gate_sha256']
            or digest(numerical)!=record['numerical_gate_sha256']):
        raise ValueError('published affine gate canonical hashes do not match')
    if physical['family']!=frozen_family(problem,state):
        raise ValueError('published affine gate belongs to a different fixed family')
    if numerical['problem_evaluation']!=problem.evaluation_definition():
        raise ValueError('the immutable height evaluation rules changed')
    gate=HeightAffineGate(family=physical['family'],kind='frozen-frame',
        height_slice=problem.slices['height'],nunknown=problem.nunknown,side=problem.port.side,
        length=problem.seed.length,target_definition=physical['target_definition'],
        intercept=exact_evaluated_scalar(numerical['intercept_evaluated']),
        weights=[exact_evaluated_scalar(x) for x in numerical['weights_evaluated']],
        target=exact_evaluated_scalar(numerical['target_evaluated']),
        evaluation=numerical['problem_evaluation'],
        reference_provenance=record['initial_reference_provenance'])
    if gate.record()!=record:raise ValueError('published complete affine gate does not replay exactly')
    gate.assert_context(problem,state)
    return gate


def replay_completed_stage(problem,reference,accepted,published,bindings,height_prior,*,artificial=False):
    """Check the fifth input without rerunning its geometry or quartic solver."""
    if (published.get('schema')!=PRIOR_SCHEMA or published.get('status')!=
            'complete-one-quartic-one-joint-stage-and-fixed-state-audit'):
        raise ValueError('a completed published quartic/joint audit is required')
    if bool(published.get('artificial_inputs_only'))!=bool(artificial):
        raise ValueError('research and artificial completed reports cannot be interchanged')
    if published.get('source_files_sha256')!=prior_hashes():
        raise ValueError('the completed report was produced by a different frozen implementation')
    for key in ['selected','original_c0','short','height_polytope']:
        old=published.get('exact_input_storage',{}).get(key,{})
        if old.get('decoded_sha256')!=bindings[key]['decoded_sha256']:
            raise ValueError('completed report is not bound to the same '+key+' input')
    if (published.get('error') or not published.get('complete_frozen_metric_retained')
            or not published.get('height_reference_unchanged')):
        raise ValueError('prior report did not retain the declared complete physical family')
    if published['accepted_height_state']!=state_record(problem,accepted):
        raise ValueError('the original accepted 162-parameter state does not replay')
    stage=published['quartic_stage'];selected=stage.get('selected')
    if selected is None or stage.get('status')!='quartic-proposal-selected':
        raise ValueError('a completed selected quartic proposal must be preserved')
    if stage.get('slsqp_calls')!=(0 if artificial else 1):
        raise ValueError('unexpected number of already completed quartic solver calls')
    after=accepted.copy();newh=np.asarray(selected['height_coefficients_binary64'],float)
    if newh.shape!=(problem.height_free,) or not np.all(np.isfinite(newh)):
        raise ValueError('finite selected absolute height coefficients required')
    if exact_coefficients(newh)!=selected['height_coefficients_exact_binary64']:
        raise ValueError('published quartic exact height coefficients do not replay')
    for label,old in [('exact_delta_from_reference',reference[problem.slices['height']]),
                      ('exact_delta_from_feasible_initial',accepted[problem.slices['height']])]:
        delta=[str(Q.from_float(float(x))-Q.from_float(float(y))) for x,y in zip(newh,old)]
        if delta!=selected[label]:raise ValueError('published quartic '+label+' does not replay')
    after[problem.slices['height']]=newh
    if state_record(problem,after)!=published['post_quartic_state']:
        raise ValueError('the complete post-quartic 162-parameter state does not replay')
    joint=SingleQProblem(problem);quartic=joint.lift_state(after);original=joint.lift_state(accepted)
    if state_record(joint,quartic)!=published['joint_initial_state']:
        raise ValueError('published zero-Q 163-parameter state does not replay')
    previous_joint=published['joint_stage']
    if previous_joint.get('solver',{}).get('minimize_invocation_count')!=0:
        raise ValueError('the requested joint solve has already been invoked; refusing an implicit rerun')
    if not artificial and previous_joint.get('status')!='initial-joint-height-or-box-gate-failed':
        raise ValueError('only the specific prior initial-gate failure is resumed in research mode')
    if published['final_state']!=published['joint_initial_state']:
        raise ValueError('the uncalled joint stage nevertheless changed its final state')
    fixed=problem.metric_model(accepted)
    if problem.metric_model(after)!=fixed or joint.metric_model(quartic)!=fixed or joint.metric_model(original)!=fixed:
        raise ValueError('published state reuse changed the complete fixed metric')
    snap=previous_joint['checkpoint'];gate=restore_gate(joint,quartic,snap['height_gate'])
    poly=height_prior['height_stage']['polytope']['definition']
    if exact_evaluated_scalar(poly['cap_target_evaluated'])!=gate.target:
        raise ValueError('the retained cap target differs from the accepted height-stage target')
    lower=np.asarray(snap['box_lower'],float);upper=np.asarray(snap['box_upper'],float)
    if lower.shape!=(joint.nunknown,) or upper.shape!=lower.shape or np.any(lower>upper):
        raise ValueError('published joint boxes do not match the complete layout')
    cfg=configuration(published['configuration'])
    expected_l=np.full(joint.nunknown,float(Q(cfg['old_tangent_lower'])))
    expected_u=np.full(joint.nunknown,float(Q(cfg['old_tangent_upper'])))
    expected_l[joint.q_index]=float(Q(cfg['new_Q_lower']));expected_u[joint.q_index]=float(Q(cfg['new_Q_upper']))
    expected_l[joint.slices['height']]=[float(Q(x)) for x in poly['coefficient_lower']]
    expected_u[joint.slices['height']]=[float(Q(x)) for x in poly['coefficient_upper']]
    if not np.array_equal(lower,expected_l) or not np.array_equal(upper,expected_u):
        raise ValueError('published joint boxes differ from the explicit original parameter boxes')
    record={'schema':'strict-completed-quartic-and-uncalled-joint-reuse-v1',
        'accepted_162_physical_sha256':digest(problem.identity(accepted)),
        'post_quartic_162_physical_sha256':digest(problem.identity(after)),
        'zero_Q_post_quartic_163_physical_sha256':digest(joint.identity(quartic)),
        'zero_Q_accepted_163_physical_sha256':digest(joint.identity(original)),
        'parameter_extension_changes_state_schema_not_the_represented_zero_Q_field':True,
        'complete_frozen_metric_definition_sha256':fixed['mathematical_definition_sha256'],
        'prior_quartic_slsqp_calls':stage['slsqp_calls'],'prior_joint_minimize_invocation_count':0,
        'published_cap_physical_and_numerical_gate_records_retained_exactly':True,
        'prior_quartic_geometry_and_optimizer_not_reexecuted':True,
        'all_original_four_input_bytes_and_both_full_states_replayed':True}
    return joint,quartic,original,after,gate,lower,upper,cfg,record


def select_warm_start(objective,candidates,checkpoint=None):
    """No projection: the first independently eligible current-grid state wins."""
    trials=[]
    for label,values in candidates:
        values=np.asarray(values,float).copy()
        try:
            _,_,record=objective.evaluate(values)
        except Exception as error:
            failure={'candidate':label,'error':{'type':type(error).__name__,'message':str(error)},
                'selected_candidate':None,'trials':trials,'optimizer_calls':0}
            if checkpoint is not None:checkpoint(failure)
            return None,failure
        trial={'candidate':label,'exact_binary64_coefficients':exact_coefficients(values),
            'current_grid_record':copy.deepcopy(record)}
        trials.append(trial)
        result={'candidate_order':[x[0] for x in candidates],'trials':copy.deepcopy(trials),
            'selected_candidate':label if record['eligible_under_all_declared_constraints'] else None,
            'rejected_candidates_not_projected_or_clipped':True,
            'complete_current_position_rechecked_for_each_candidate':True,'optimizer_calls':0}
        if checkpoint is not None:checkpoint(result)
        if record['eligible_under_all_declared_constraints']:return values,result
    return None,result


def small_summary(report,out):
    keys=['schema','status','phase','error','github_sha','github_run_id','github_repository',
        'source_files_sha256','exact_input_storage','configuration','input_replay',
        'prior_quartic_reused','quartic_solver_calls_this_run','warm_start_selection',
        'complete_frozen_metric_retained','height_reference_unchanged','artificial_inputs_only',
        'final_current_constraints','elapsed_seconds','peak_rss_kib_linux']
    result={k:report[k] for k in keys if k in report}
    if 'warm_start_selection' in result:
        result['warm_start_selection']=copy.deepcopy(result['warm_start_selection'])
        for trial in result['warm_start_selection'].get('trials',[]):trial.pop('exact_binary64_coefficients',None)
    for key in ['accepted_height_state','post_quartic_state','joint_initial_state','final_state']:
        if key in report:result[key]=compact_state(report[key])
    for key in ['joint_work_initial_audit','joint_work_final_audit','final_fine_audit','doubled_angle_final_audit']:
        if key in report:result[key]=compact_audit(report[key])
    if 'same_parameter_Pi_refinement' in report:
        result['same_parameter_Pi_refinement']=compact_comparison(report['same_parameter_Pi_refinement'])
    if 'joint_stage' in report:
        stage=report['joint_stage'];snap=stage.get('checkpoint',stage)
        result['joint_stage']={k:stage.get(k) for k in ['status','solver','error','budget_message']}
        result['joint_stage'].update(evaluations=snap.get('evaluations'),elapsed_seconds=snap.get('elapsed_seconds'),
            maximum_cached_array_bytes=snap.get('maximum_cached_array_bytes'))
        for key in ['best_jointly_eligible_point','lowest_objective_trial_point_may_be_ineligible']:
            point=snap.get(key);result['joint_stage'][key]=None if point is None else point['record']
    raw=Path(out).read_bytes()
    result.update(summary_schema='joint-resume-scientific-summary-v1',
        full_report={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},
        sampled_only=True,task_complete=False,embedding_proved=False,whole_surface_reach_proved=False)
    return result


def prepare_resume(args,*,artificial=False):
    bindings={};phase='five-input-public-repository-guard'
    try:
        paths=[args.input,args.anchor_input,args.short_audit,args.height_audit,args.prior_joint_audit]
        if any(x is None for x in paths):raise ValueError('five explicit input paths required')
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        phase='completed-joint-report-byte-binding'
        if not args.expected_prior_joint_sha256:raise ValueError('explicit completed report decoded SHA256 required')
        published,_,binding=read_input(args.prior_joint_audit,args.expected_prior_joint_sha256)
        bindings['prior_completed_joint']=binding
        phase='unchanged-four-parent-inputs-and-original-accepted-state'
        problem,reference,accepted,prior,receipt,source_cfg=prepare_original_inputs(args,artificial=artificial)
        bindings.update(receipt['exact_input_storage'])
        phase='completed-quartic-full-state-and-uncalled-joint-replay'
        replay=replay_completed_stage(problem,reference,accepted,published,bindings,prior,artificial=artificial)
        return problem,reference,accepted,prior,receipt,source_cfg,published,bindings,replay
    except Exception as error:
        report={'schema':SCHEMA,'status':'resume-input-replay-failed-before-geometry','phase':phase,
            'error':{'type':type(error).__name__,'message':str(error)},'exact_input_storage':bindings,
            'source_files_sha256':implementation_hashes(),'quartic_solver_calls_this_run':0,
            'joint_solver_calls_this_run':0,'research_candidate_evaluated':False,
            'artificial_inputs_only':bool(artificial)}
        atomic_save(args.out,report);atomic_save(summary_path(args.out),small_summary(report,args.out))
        raise


def run_resume(prepared,out,*,artificial=False,artificial_evaluate_only=False):
    problem,reference,accepted,prior,receipt,source_cfg,published,bindings,replay=prepared
    joint,quartic,original,after,gate,lower,upper,cfg,replay_record=replay
    cfg=copy.deepcopy(cfg)
    if artificial:
        cfg['joint_evaluate_only']=bool(artificial_evaluate_only)
        # The full IO carrier has explicit relaxed artificial geometry gates;
        # positive signed-height selection itself is checked on array inputs.
        cfg['minimum_signed_height_exact']='-10'
    start=time.monotonic();fixed=problem.metric_model(accepted);height_cfg=prior['configuration']
    answer={'schema':SCHEMA,'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'source_files_sha256':implementation_hashes(),
        'exact_input_storage':bindings,'configuration':cfg,'input_replay':replay_record,
        'accepted_height_state':state_record(problem,accepted),'post_quartic_state':state_record(problem,after),
        'prior_quartic_reused':{k:published['quartic_stage'].get(k) for k in
            ['status','slsqp_calls','objective_evaluations','initial_direct_metric_cost','selected','optimizer_result','elapsed_seconds']},
        'quartic_solver_calls_this_run':0,'artificial_inputs_only':bool(artificial),
        'complete_frozen_metric_retained':True,'height_reference_unchanged':True,
        'task_complete':False,'embedding_proved':False,'whole_surface_reach_proved':False}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-start
        answer['peak_rss_kib_linux']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        atomic_save(out,answer);atomic_save(summary_path(out),small_summary(answer,out))
    save('completed-quartic-replayed-without-rerunning')
    try:
        answer['phase']='current-grid-warm-start-selection'
        work_t,work_theta,work_grid=build_grid(joint,cfg['joint_radial_nodes'],
            cfg['joint_collar_subdivisions'],cfg['joint_angular_nodes'])
        if work_grid!=published['joint_sampling_definition']:
            raise ValueError('resume changed the declared current joint sampling grid')
        order=source_cfg['primitive_order'];answer['joint_sampling_definition']=work_grid
        def joint_checkpoint(snapshot):
            answer['joint_stage']={'status':'joint-resume-checkpoint','checkpoint':snapshot}
            save('joint-resume-current-state-checkpoint')
        objective=JointSignedHeightObjective(joint,gate,work_t,work_theta,order,lower,upper,
            max_evaluations=cfg['joint_max_evaluations'],max_seconds=cfg['joint_max_seconds'],
            box_tolerance=cfg['box_tolerance'],height_tolerance=cfg['height_tolerance'],
            reconstruction_tolerance=cfg['height_reconstruction_tolerance'],
            minimum_signed_height=float(Q(cfg['minimum_signed_height_exact'])),
            signed_height_tolerance=cfg['signed_z_tolerance'],checkpoint=joint_checkpoint,
            checkpoint_every=cfg['checkpoint_evaluations'],checkpoint_seconds=cfg['checkpoint_seconds'])
        objective.objective_evaluation_definition['resume_definition']={
            'source_files_sha256':implementation_hashes(),
            'prior_completed_report_decoded_sha256':bindings['prior_completed_joint']['decoded_sha256'],
            'minimum_signed_height_exact':cfg['minimum_signed_height_exact'],
            'strict_positive_guard_is_not_reach_or_continuous_separation':True,
            'warm_start_order':cfg['warm_start_order'],'original_tolerances_not_relaxed':True}
        objective.objective_evaluation_sha256=digest(objective.objective_evaluation_definition)
        def warm_checkpoint(record):
            answer['warm_start_selection']=record;save('current-grid-warm-candidate-audited')
        initial,selection=select_warm_start(objective,
            [('published_post_quartic',quartic),('original_accepted_height',original)],warm_checkpoint)
        answer['warm_start_selection']=selection
        if initial is None:
            answer['joint_stage']={'status':'no-currently-eligible-warm-start',
                'solver':{'minimize_invocation_count':0},'checkpoint':objective.snapshot()}
            save('warm-starts-rejected-no-joint-solver');return answer
        answer['joint_initial_state']=state_record(joint,initial)
        initial_data=joint.geometry(initial,work_t,work_theta,order)
        answer['joint_work_initial_audit']=audit_data(joint,initial,initial_data,height_cfg['tau'])
        answer['published_cap_gate_exactly_retained']=gate.record()==published['joint_stage']['checkpoint']['height_gate']
        answer['phase']='one-previously-uncalled-joint-stage'
        del initial_data
        result=run_joint_slsqp(objective,initial,maxiter=cfg['joint_maxiter'],ftol=cfg['joint_ftol'],
            artificial_inputs_only=artificial,evaluate_only=cfg['joint_evaluate_only'])
        answer['joint_stage']=result
        chosen=result['checkpoint']['best_jointly_eligible_point']
        if chosen is None:raise ArithmeticError('eligible warm start was not retained by the joint checkpoint')
        final=np.asarray(chosen['parameter_coefficients_binary64'],float)
        if exact_coefficients(final)!=chosen['exact_binary64_coefficients']:
            raise ArithmeticError('final selected joint coefficient bits do not replay')
        if joint.metric_model(final)!=fixed or joint.height_base_definition!=problem.height_base_definition:
            raise ArithmeticError('resume changed the fixed g or immutable height baseline')
        answer['final_state']=state_record(joint,final)
        answer['phase']='full-selected-state-and-fixed-parameter-refinement'
        work_final=joint.geometry(final,work_t,work_theta,order)
        answer['joint_work_final_audit']=audit_data(joint,final,work_final,height_cfg['tau'])
        t,theta,fine_grid=build_grid(problem,source_cfg['radial_nodes'],source_cfg['collar_subdivisions'],source_cfg['angular_nodes'])
        answer['fine_sampling_definition']=fine_grid
        final_data=joint.geometry(final,t,theta,order)
        answer['final_fine_audit']=audit_data(joint,final,final_data,height_cfg['tau'])
        cap=gate.decision(final,final_data,lower,upper,box_tolerance=cfg['box_tolerance'],
            height_tolerance=cfg['height_tolerance'],reconstruction_tolerance=cfg['height_reconstruction_tolerance'])
        threshold=float(Q(cfg['minimum_signed_height_exact']))
        minimum=float(np.min(joint.port.side*final_data['X'][...,2]))
        answer['final_current_constraints']={'cap_and_box':cap,'fine_minimum_signed_height':minimum,
            'signed_height_threshold_exact':cfg['minimum_signed_height_exact'],
            'fine_signed_height_pass':bool(minimum>=threshold-cfg['signed_z_tolerance']),
            'fine_pass_is_not_a_continuous_separation_or_reach_certificate':True}
        save('resumed-joint-selected-fine-state-audited')
        del work_final,objective
        doubled_theta=np.arange(2*len(theta))*np.pi/len(theta)
        doubled=joint.geometry(final,t,doubled_theta,order)
        answer['doubled_angle_final_audit']=audit_data(joint,final,doubled,height_cfg['tau'],with_rows=False)
        answer['same_parameter_Pi_refinement']=compare_data(joint,final_data,joint,doubled,final,
            name='resumed joint selected state, fixed g/b0/coefficients, Pi angle doubling',theta_stride=2)
        save('complete-reused-quartic-and-one-resumed-joint-audit');return answer
    except Exception as error:
        answer['error']={'type':type(error).__name__,'message':str(error)}
        save('resume-error-preserved-completed-checkpoints');raise


def array_selection_check():
    p=_JointArrayProblem();g=HeightAffineGate.from_artificial_array_problem(p)
    t=np.array([0.,1.]);theta=np.arange(4)*np.pi/2
    low=np.array([-2.,-1.,-1.]);up=np.array([2.,1.,1.])
    def make():return JointSignedHeightObjective(p,g,t,theta,3,low,up,
        max_evaluations=20,max_seconds=20.,minimum_signed_height=1e-4,signed_height_tolerance=1e-9)
    rejected=np.array([1.8,.4,0.]);accepted=np.array([0.,.6,.6])
    obj=make();chosen,record=select_warm_start(obj,[('published_post_quartic',rejected),('original_accepted_height',accepted)])
    fallback=(chosen is not None and np.array_equal(chosen,accepted) and
        record['selected_candidate']=='original_accepted_height' and len(record['trials'])==2 and
        not record['trials'][0]['current_grid_record']['eligible_under_all_declared_constraints'])
    obj2=make();first,r2=select_warm_start(obj2,[('published_post_quartic',accepted),('original_accepted_height',rejected)])
    preferred=first is not None and np.array_equal(first,accepted) and len(r2['trials'])==1
    obj3=make();none,r3=select_warm_start(obj3,[('published_post_quartic',rejected),('original_accepted_height',rejected)])
    no_choice=none is None and r3['selected_candidate'] is None
    return {'rejected_quartic_falls_back_without_coefficient_change':bool(fallback),
        'eligible_quartic_is_kept_without_testing_fallback':bool(preferred),
        'two_failed_candidates_do_not_trigger_a_solver':bool(no_choice),
        'positive_signed_guard':1e-4,'unchanged_signed_tolerance':1e-9,
        'optimizer_calls_in_selection':0,'passed':bool(fallback and preferred and no_choice)}


def artificial_check():
    """New replay/selection/full-IO branches; no old solver suite is repeated."""
    arrays=array_selection_check()
    base,state,old_prior,source_receipt,selected_bytes,anchor=artificial_inputs()
    cfg=short_defaults();cfg.update(entry_length='3/25',entry_mean_nodes=32,uniform_panels=8,
        primitive_order=3,radial_nodes=9,angular_nodes=16,collar_subdivisions=6)
    pair=EntryRepairProblem(base,state,'3/25',entry_mean_nodes=32,uniform_panels=8,primitive_order=3)
    bounded=BoundedEntryHeightProblem(pair,state,uniform_panels=8,primitive_order=3)
    _,_,shared=build_grid(pair,9,6,16)
    short={'schema':'short-entry-paired-bounded-one-height-step-audit-v1',
        'status':'complete-two-initial-fields-and-at-most-one-height-step-each',
        'source_files_sha256':short_hashes(),'source_receipt':source_receipt,
        'source_exact_state':state_record(base,state),'configuration':cfg,
        'selected_original_fixed_metric':base.metric_model(state),'sampling_grid':shared,
        'cases':{'bounded_short':{'final_state':state_record(bounded,state)}},'artificial_inputs_only':True}
    with tempfile.TemporaryDirectory(prefix='joint-resume-artificial-',dir='/dev/shm') as directory:
        directory=Path(directory);names=['selected.json','anchor.json','short.json.gz','height.json.gz','prior-joint.json.gz']
        paths=[directory/x for x in names];short_raw=json.dumps(short,sort_keys=True).encode()
        paths[0].write_bytes(selected_bytes);paths[1].write_bytes(anchor);paths[2].write_bytes(gzip.compress(short_raw))
        sha=[hashlib.sha256(x).hexdigest() for x in [selected_bytes,anchor,short_raw]]
        p,ref,rec,scfg=load_short_model(json.loads(selected_bytes),anchor,short,*sha[:2],'bounded_short',artificial=True)
        rec['exact_input_storage']={'short':{'decoded_sha256':sha[2]}}
        t,theta,grid=build_grid(p,9,6,16);data=p.geometry(ref,t,theta,3)
        h=p.port.side*float(data['center'][-1]);hc=height_configuration()
        poly,_=proposal_polytope(p,ref,data,hc,artificial=True,artificial_override=(h-.001,10.,-10.))
        if not poly.decision(ref[p.slices['height']])['eligible_under_declared_sampled_floating_tolerances']:
            raise ArithmeticError('explicit artificial baseline must satisfy its declared relaxed rows')
        heights=ref[p.slices['height']]
        selected={'height_coefficients_binary64':heights.tolist(),'height_coefficients_exact_binary64':exact_coefficients(heights),
            'exact_delta_from_reference':['0']*len(heights),'exact_delta_from_feasible_initial':['0']*len(heights)}
        height={'schema':'fixed-T-a-all-height-polytope-stage-audit-v1',
            'status':'complete-one-height-polytope-stage-no-joint-metric-solve',
            'source_files_sha256':height_hashes(),'source_receipt':rec,'configuration':hc,
            'initial_state':state_record(p,ref),'final_state':state_record(p,ref),
            'sampling_grid':grid,'artificial_inputs_only':True,'complete_frozen_metric_retained':True,
            'tangent_step_applied':False,'metric_step_applied':False,'joint_metric_solver_calls':0,
            'height_stage':{'polytope':poly.record(),'selected':selected},
            'full_reconstruction_checks':{'independent_reconstruction_passes_declared_sample_tolerances':True},
            'explicit_artificial_fixture_no_LP_QP_or_quartic_solver_was_called':True}
        height_raw=json.dumps(height,sort_keys=True).encode();paths[3].write_bytes(gzip.compress(height_raw))
        sha.append(hashlib.sha256(height_raw).hexdigest())
        args=argparse.Namespace(input=paths[0],anchor_input=paths[1],short_audit=paths[2],height_audit=paths[3],
            prior_joint_audit=paths[4],expected_input_sha256=sha[0],expected_anchor_sha256=sha[1],
            expected_short_sha256=sha[2],expected_height_sha256=sha[3],expected_prior_joint_sha256=None,
            out=directory/'resume.json')
        pp,reference,accepted,hprior,receipt,source_cfg=prepare_original_inputs(args,artificial=True)
        joint=SingleQProblem(pp);initial=joint.lift_state(accepted);conf=prior_configuration()
        conf.update(joint_radial_nodes=9,joint_angular_nodes=16,joint_collar_subdivisions=6,joint_evaluate_only=True)
        wt,wth,wgrid=build_grid(joint,9,6,16);wdata=joint.geometry(initial,wt,wth,3)
        weights=joint.port.side*joint.height_basis.integral(np.array([joint.seed.length]))[0]
        gate=HeightAffineGate(family=frozen_family(joint,initial),kind='frozen-frame',
            height_slice=joint.slices['height'],nunknown=joint.nunknown,side=joint.port.side,length=joint.seed.length,
            target_definition={'explicit_artificial_polytope_target':poly.cap_target},
            intercept=joint.port.side*float(wdata['center'][-1])-float(weights@initial[joint.slices['height']]),
            weights=weights,target=poly.cap_target,evaluation=joint.evaluation_definition(),reference_provenance={'artificial_only':True})
        lower=np.full(joint.nunknown,-8.);upper=np.full(joint.nunknown,8.)
        lower[joint.slices['height']]=poly.lower;upper[joint.slices['height']]=poly.upper
        published={'schema':PRIOR_SCHEMA,'status':'complete-one-quartic-one-joint-stage-and-fixed-state-audit',
            'source_files_sha256':prior_hashes(),'exact_input_storage':receipt['exact_input_storage'],
            'configuration':conf,'artificial_inputs_only':True,'complete_frozen_metric_retained':True,
            'height_reference_unchanged':True,'accepted_height_state':state_record(pp,accepted),
            'post_quartic_state':state_record(pp,accepted),'joint_initial_state':state_record(joint,initial),
            'final_state':state_record(joint,initial),'joint_sampling_definition':wgrid,
            'quartic_stage':{'status':'quartic-proposal-selected','slsqp_calls':0,'selected':selected},
            'joint_stage':{'status':'explicit-artificial-no-solve-fixture','solver':{'minimize_invocation_count':0},
                'checkpoint':{'height_gate':gate.record(),'box_lower':lower.tolist(),'box_upper':upper.tolist()}},
            'explicit_artificial_fixture_not_an_Actions_candidate_or_claimed_solver_run':True}
        raw=json.dumps(published,sort_keys=True).encode();paths[4].write_bytes(gzip.compress(raw))
        args.expected_prior_joint_sha256=hashlib.sha256(raw).hexdigest()
        prepared=prepare_resume(args,artificial=True)
        result=run_resume(prepared,args.out,artificial=True,artificial_evaluate_only=True)
        summary=json.loads(summary_path(args.out).read_text())
        bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        changed=copy.deepcopy(published);changed['joint_stage']['solver']['minimize_invocation_count']=1
        try:replay_completed_stage(pp,reference,accepted,changed,receipt['exact_input_storage'],hprior,artificial=True);called_reject=False
        except ValueError:called_reject=True
        changed=copy.deepcopy(published);changed['post_quartic_state']['canonical_physical_state_sha256']='0'*64
        try:replay_completed_stage(pp,reference,accepted,changed,receipt['exact_input_storage'],hprior,artificial=True);state_reject=False
        except ValueError:state_reject=True
        wrong=copy.copy(args);wrong.expected_prior_joint_sha256='0'*64;wrong.out=directory/'bad.json'
        try:prepare_resume(wrong,artificial=True);sha_reject=False
        except ValueError:
            failure=json.loads(wrong.out.read_text());sha_reject=(failure['phase']=='completed-joint-report-byte-binding'
                and failure['quartic_solver_calls_this_run']==0 and failure['joint_solver_calls_this_run']==0)
        no_calls=(result['quartic_solver_calls_this_run']==0 and
            result['joint_stage']['solver']['minimize_invocation_count']==0)
        passed=bool(arrays['passed'] and bound and called_reject and state_reject and sha_reject and no_calls and
            result['status']=='complete-reused-quartic-and-one-resumed-joint-audit')
        return {'schema':'joint-resume-targeted-artificial-branches-v1','artificial_inputs_only':True,
            'research_candidate_evaluated_or_optimized':False,'selection_array_check':arrays,
            'five_input_complete_IO_with_constructed_artificial_no_solve_fixture':True,
            'prior_completed_joint_call_rejected':called_reject,'changed_complete_state_rejected':state_reject,
            'wrong_fifth_SHA_saved_small_failure_JSON':sha_reject,'summary_byte_binding':bound,
            'quartic_and_joint_calls_in_full_IO_test':0 if no_calls else None,
            'published_cap_gate_retained_exactly':result['published_cap_gate_exactly_retained'],
            'same_state_final_Pi_refinement':result['same_parameter_Pi_refinement'],'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--anchor-input',type=Path)
    parser.add_argument('--short-audit',type=Path);parser.add_argument('--height-audit',type=Path)
    parser.add_argument('--prior-joint-audit',type=Path)
    for name in ['input','anchor','short','height','prior-joint']:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        result=artificial_check();result['source_files_sha256']=implementation_hashes()
        atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    try:prepared=prepare_resume(args)
    except Exception:raise SystemExit(1)
    result=run_resume(prepared,args.out)
    print(json.dumps({'out':str(args.out),'status':result['status']}),flush=True)


if __name__=='__main__':main()

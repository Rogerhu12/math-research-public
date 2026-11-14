#!/usr/bin/env python3
"""One true-max-metric trial from the completed positive-height joint state.

Six complete reports are replayed; no old quartic or L2 joint solve is run.
The fixed metric, immutable height reference, physical coefficient boxes and
published cap row are retained. New sampled hard shape gates are explicit.
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
    compact_audit,compact_state,compact_comparison,artificial_inputs,
    default_configuration as short_defaults,implementation_hashes as short_hashes)
from frame_entry_paired_repair import EntryRepairProblem
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_height_polytope_audit import (load_short_model,proposal_polytope,
    stage_configuration as height_configuration,implementation_hashes as height_hashes)
from frame_height_quartic_joint_audit import (prepare_run as prepare_original_inputs,
    configuration as prior_configuration,implementation_hashes as prior_hashes,SCHEMA as PRIOR_SCHEMA)
from frame_height_joint_resume import (prepare_resume,configuration as resume_configuration,
    implementation_hashes as resume_hashes,SCHEMA as RESUME_SCHEMA,restore_gate)
from frame_independent_height_solve import state_record
from frame_entry_single_q import SingleQProblem
from frame_height_affine_gate import HeightAffineGate,frozen_family
from frame_metric_epigraph import (MetricEpigraphObjective,configuration,run_epigraph_slsqp,
    candidate_decision,developer_check as array_check,implementation_hashes as epigraph_hashes)

SCHEMA='fixed-g-true-max-metric-from-completed-joint-audit-v1'


def implementation_hashes():
    result=resume_hashes();result.update(epigraph_hashes())
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def exact_coefficients(values):return [str(Q.from_float(float(x))) for x in values]


def replay_latest(prepared,latest,*,artificial=False):
    problem,reference,accepted,height_prior,receipt,source_cfg,prior,bindings,replay=prepared
    joint,quartic,original,after,gate,lower,upper,old_cfg,replay_record=replay
    if (latest.get('schema')!=RESUME_SCHEMA or latest.get('status')!=
            'complete-reused-quartic-and-one-resumed-joint-audit'):
        raise ValueError('one completed explicit-positive-height joint resume report required')
    if bool(latest.get('artificial_inputs_only'))!=bool(artificial):
        raise ValueError('artificial and research resumed states cannot be interchanged')
    if latest.get('source_files_sha256')!=resume_hashes():
        raise ValueError('completed resume implementation differs from the frozen source')
    for key,expected in bindings.items():
        old=latest.get('exact_input_storage',{}).get(key,{})
        for attribute in ['decoded_sha256','decoded_bytes','stored_sha256','stored_bytes','gzip_storage']:
            if old.get(attribute)!=expected.get(attribute):
                raise ValueError('resume input storage binding changed: '+key+'/'+attribute)
    if latest.get('input_replay')!=replay_record:
        raise ValueError('completed resume is not the same exact five-input model replay')
    if (latest.get('quartic_solver_calls_this_run')!=0 or latest.get('error')
            or not latest.get('complete_frozen_metric_retained') or not latest.get('height_reference_unchanged')):
        raise ValueError('completed resume changed the declared physical family or repeated its quartic')
    expected_cfg=copy.deepcopy(old_cfg)
    if artificial:expected_cfg.update(minimum_signed_height_exact='-10',joint_evaluate_only=True)
    if latest.get('configuration')!=expected_cfg:raise ValueError('resume numerical model/constraint configuration differs')
    if latest.get('accepted_height_state')!=state_record(problem,accepted):
        raise ValueError('resume original accepted complete state differs')
    if latest.get('post_quartic_state')!=state_record(problem,after):
        raise ValueError('resume preserved quartic complete state differs')
    selection=latest.get('warm_start_selection',{})
    if selection.get('selected_candidate')!='original_accepted_height':
        raise ValueError('this pilot starts only from the declared accepted-height fallback continuation')
    if latest.get('joint_initial_state')!=state_record(joint,original):
        raise ValueError('resume actual selected initial full state does not replay')
    stage=latest['joint_stage']
    if stage.get('solver',{}).get('minimize_invocation_count')!=(0 if artificial else 1):
        raise ValueError('the consumed resume must contain exactly its one completed joint invocation')
    checkpoint=stage['checkpoint']
    if checkpoint.get('height_gate')!=gate.record():raise ValueError('the published physical/numerical cap row changed')
    if (not np.array_equal(np.asarray(checkpoint['box_lower'],float),lower)
            or not np.array_equal(np.asarray(checkpoint['box_upper'],float),upper)):
        raise ValueError('the published coefficient boxes changed')
    chosen=checkpoint.get('best_jointly_eligible_point')
    if chosen is None or not chosen.get('record',{}).get('eligible_under_all_declared_constraints'):
        raise ValueError('completed resume has no explicitly selected eligible physical point')
    state=np.asarray(chosen['parameter_coefficients_binary64'],float)
    if state.shape!=(joint.nunknown,) or not np.all(np.isfinite(state)):
        raise ValueError('complete finite selected physical vector required')
    if exact_coefficients(state)!=chosen['exact_binary64_coefficients']:
        raise ValueError('resume selected coefficient rational identity differs')
    if latest.get('final_state')!=state_record(joint,state):
        raise ValueError('resume complete selected final physical/evaluation state differs')
    if joint.metric_model(state)!=problem.metric_model(accepted):
        raise ValueError('new maximum-metric start changed the full frozen target metric')
    _,_,grid=build_grid(joint,old_cfg['joint_radial_nodes'],old_cfg['joint_collar_subdivisions'],old_cfg['joint_angular_nodes'])
    if grid!=latest.get('joint_sampling_definition'):
        raise ValueError('completed resume exact work grid differs')
    record={'schema':'strict-six-input-latest-joint-physical-replay-v1',
        'latest_physical_state_sha256':digest(joint.identity(state)),
        'complete_metric_definition_sha256':joint.metric_model(state)['mathematical_definition_sha256'],
        'original_c0_lineage_and_full_b0_retained':True,
        'selected_physical_parameter_count':joint.nunknown,
        'all_selected_coefficients_replayed_without_refit':True,
        'published_cap_gate_and_coefficient_boxes_exactly_retained':True,
        'previous_quartic_and_both_old_joint_stages_not_reexecuted':True,
        'auxiliary_delta_does_not_yet_exist_in_the_source_state':True}
    return joint,state,gate,lower,upper,old_cfg,source_cfg,record


def summary_path(out):return out.with_name(out.stem+'-summary.json')


def small_summary(report,out):
    answer={key:report.get(key) for key in ['schema','status','phase','configuration','source_files_sha256',
        'exact_input_storage','input_replay','github_sha','github_run_id','github_repository',
        'artificial_inputs_only','previous_optimizer_calls_this_run','physical_metric_and_b0_unchanged',
        'initial_auxiliary_delta','initial_current_constraints','final_work_constraints','final_fine_constraints',
        'final_doubled_constraints','final_auxiliary_delta','elapsed_seconds','peak_rss_kib_linux','error'] if key in report}
    for name in ['initial_state','final_state']:
        if name in report:answer[name]=compact_state(report[name])
    for name in ['initial_work_audit','final_work_audit','final_fine_audit','doubled_angle_final_audit']:
        if name in report:answer[name]=compact_audit(report[name])
    if 'same_parameter_Pi_refinement' in report:answer['same_parameter_Pi_refinement']=compact_comparison(report['same_parameter_Pi_refinement'])
    stage=report.get('epigraph_stage')
    if stage:
        answer['epigraph_stage']={key:stage.get(key) for key in ['status','error','budget_message','solver','selected_point']}
        checkpoint=stage.get('checkpoint',{})
        answer['epigraph_stage']['checkpoint']={key:checkpoint.get(key) for key in
            ['physical_geometry_evaluations','epigraph_vector_evaluations','elapsed_seconds',
             'final_selection','maximum_geometry_cache_array_bytes','maximum_single_constraint_Jacobian_bytes',
             'objective_evaluation_sha256']}
        for key in ['best_eligible_auxiliary_delta_point','best_eligible_direct_max_eta_point']:
            point=checkpoint.get(key)
            answer['epigraph_stage']['checkpoint'][key]=None if point is None else {
                name:point.get(name) for name in ['physical_state_sha256','auxiliary_delta_evaluated','record']}
    raw=out.read_bytes();answer['full_report']={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    answer.update(task_complete=False,sampled_only=True,embedding_or_whole_reach_proved=False,
        curvature_may_worsen_despite_maximum_metric_improvement=True)
    return answer


def save_report(out,report):
    atomic_save(out,report);atomic_save(summary_path(out),small_summary(report,out))


def prepare_maximum(args,*,artificial=False):
    phase='six-input-public-repository-guard';bindings={}
    try:
        paths=[args.input,args.anchor_input,args.short_audit,args.height_audit,args.prior_joint_audit,args.resume_audit]
        if any(path is None for path in paths):raise ValueError('six exact input reports are required')
        if not artificial:require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        phase='latest-resume-decoded-byte-binding'
        if not args.expected_resume_sha256:raise ValueError('explicit sixth decoded SHA256 required')
        latest,raw,binding=read_input(args.resume_audit,args.expected_resume_sha256);bindings['latest_joint_resume']=binding
        phase='unchanged-five-input-physical-replay'
        prepared=prepare_resume(args,artificial=artificial);bindings.update(prepared[7])
        phase='latest-joint-selected-physical-state-replay'
        result=replay_latest(prepared,latest,artificial=artificial)
        return result,bindings,latest
    except Exception as error:
        report={'schema':SCHEMA,'status':'input-replay-failed-before-new-geometry','phase':phase,
            'error':{'type':type(error).__name__,'message':str(error)},'source_files_sha256':implementation_hashes(),
            'exact_input_storage':bindings,'artificial_inputs_only':bool(artificial),
            'previous_optimizer_calls_this_run':0,'new_epigraph_solver_calls':0}
        save_report(args.out,report);raise


def run_maximum(prepared,out,*,artificial=False,evaluate_only=False):
    result,bindings,latest=prepared
    problem,initial,gate,lower,upper,work_cfg,source_cfg,receipt=result
    cfg=configuration()
    if artificial:
        cfg.update(minimum_signed_height_exact='-10',hard_ball_radius_exact='10',hard_strip_half_width_exact='10',
            max_seconds=120.,max_physical_evaluations=4,maxiter=2)
    started=time.monotonic();fixed=problem.metric_model(initial);height_reference=copy.deepcopy(problem.height_base_definition)
    answer={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'exact_input_storage':bindings,
        'input_replay':receipt,'artificial_inputs_only':bool(artificial),'previous_optimizer_calls_this_run':0,
        'initial_state':state_record(problem,initial),'physical_metric_and_b0_unchanged':True,
        'new_shape_constraints_are_not_claimed_to_have_been_old_constraints':True,
        'old_L2_diagnostics_are_not_the_new_optimization_objective':True}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-started
        answer['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        save_report(out,answer)
    save('six-input-physical-state-replayed-no-old-optimizer-called')
    try:
        answer['phase']='one-current-grid-physical-preflight'
        t,theta,grid=build_grid(problem,work_cfg['joint_radial_nodes'],work_cfg['joint_collar_subdivisions'],work_cfg['joint_angular_nodes'])
        if grid!=latest['joint_sampling_definition']:raise ValueError('the declared work grid changed')
        answer['work_sampling_definition']=grid;order=source_cfg['primitive_order']
        def checkpoint(value):
            answer['epigraph_stage']={'status':'current-epigraph-checkpoint','checkpoint':value}
            save('maximum-metric-current-state-checkpoint')
        objective=MetricEpigraphObjective(problem,gate,t,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        objective.evaluation_definition['sixth_input_decoded_sha256']=bindings['latest_joint_resume']['decoded_sha256']
        objective.evaluation_definition['one_new_objective_no_repeated_prior_solve']=True
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        vector=objective.initial_vector(initial);record=objective.evaluate(vector)
        answer['initial_auxiliary_delta']=float(vector[-1]);answer['initial_current_constraints']=record['decision']
        answer['initial_work_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        save('new-hard-shape-and-positive-delta-initial-state-audited')
        answer['phase']='one-new-maximum-metric-epigraph-invocation'
        stage=run_epigraph_slsqp(objective,initial,artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        answer['epigraph_stage']=stage
        chosen=stage['checkpoint']['best_eligible_direct_max_eta_point']
        if chosen is None:
            save('no-eligible-new-epigraph-initial-or-trial-state');return answer
        final=np.asarray(chosen['physical_parameter_coefficients_binary64'],float)
        delta=float(Q(chosen['auxiliary_delta_exact_binary64']))
        if exact_coefficients(final)!=chosen['exact_binary64_physical_coefficients']:
            raise ValueError('selected physical coefficients fail exact binary64 replay')
        if delta!=chosen['auxiliary_delta_evaluated']:raise ValueError('selected auxiliary scalar fails exact replay')
        physical=problem.identity(final)
        if digest(physical)!=chosen['physical_state_sha256']:raise ValueError('auxiliary-free final physical identity differs')
        frozen,fc=problem.frozen_metric_copy(final)
        if (fc.tobytes()!=final.tobytes() or frozen.identity(fc)!=physical
                or frozen.metric_model(fc)!=fixed or frozen.height_base_definition!=height_reference):
            raise ArithmeticError('fixed-state final replay changed g, b0, coefficients or physical identity')
        problem=frozen;final=fc
        answer.update(final_state=state_record(problem,final),final_auxiliary_delta=delta,
            auxiliary_delta_not_added_to_physical_state=True,
            final_selection='minimum direct sampled max_eta among trials passing every declared hard gate')
        answer['phase']='independent-final-geometry-and-unchanged-state-refinement'
        work=problem.geometry(final,t,theta,order)
        answer['final_work_audit']=audit_data(problem,final,work,source_cfg['tau'])
        answer['final_work_constraints']=candidate_decision(problem,gate,final,delta,work,lower,upper,cfg)
        fine_t,fine_theta,fine_grid=build_grid(problem,source_cfg['radial_nodes'],source_cfg['collar_subdivisions'],source_cfg['angular_nodes'])
        answer['fine_sampling_definition']=fine_grid
        fine=problem.geometry(final,fine_t,fine_theta,order)
        answer['final_fine_audit']=audit_data(problem,final,fine,source_cfg['tau'])
        answer['final_fine_constraints']=candidate_decision(problem,gate,final,delta,fine,lower,upper,cfg)
        save('selected-physical-state-fine-audit-before-angle-doubling')
        del objective,work
        doubled_theta=np.arange(2*len(fine_theta))*np.pi/len(fine_theta)
        doubled=problem.geometry(final,fine_t,doubled_theta,order)
        answer['doubled_angle_final_audit']=audit_data(problem,final,doubled,source_cfg['tau'],with_rows=False)
        answer['final_doubled_constraints']=candidate_decision(problem,gate,final,delta,doubled,lower,upper,cfg)
        answer['same_parameter_Pi_refinement']=compare_data(problem,fine,problem,doubled,final,
            name='one maximum-metric selected physical state; auxiliary delta held fixed separately',theta_stride=2)
        answer['continuous_and_curvature_limitations']={
            'finer_max_eta_may_exceed_the_work_grid_auxiliary_delta':True,
            'no_delta_inflation_to_hide_fine_grid_failure':True,
            'curvature_and_mirror_diagnostics_remain_independent':True,
            'no_reoptimization_after_final_sampling_or_angle_doubling':True}
        save('complete-one-true-max-metric-epigraph-and-fixed-state-audit');return answer
    except Exception as error:
        answer['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('new-epigraph-error-preserved-completed-checkpoints');return answer


def artificial_fixture(directory):
    """Construct six marked toy records, without calling any old optimizer."""
    base,state,unused,source_receipt,selected_bytes,anchor=artificial_inputs()
    scfg=short_defaults();scfg.update(entry_length='3/25',entry_mean_nodes=32,uniform_panels=8,
        primitive_order=3,radial_nodes=9,angular_nodes=16,collar_subdivisions=6)
    pair=EntryRepairProblem(base,state,'3/25',entry_mean_nodes=32,uniform_panels=8,primitive_order=3)
    bounded=BoundedEntryHeightProblem(pair,state,uniform_panels=8,primitive_order=3)
    _,_,shared=build_grid(pair,9,6,16)
    short={'schema':'short-entry-paired-bounded-one-height-step-audit-v1',
        'status':'complete-two-initial-fields-and-at-most-one-height-step-each','source_files_sha256':short_hashes(),
        'source_receipt':source_receipt,'source_exact_state':state_record(base,state),'configuration':scfg,
        'selected_original_fixed_metric':base.metric_model(state),'sampling_grid':shared,
        'cases':{'bounded_short':{'final_state':state_record(bounded,state)}},'artificial_inputs_only':True}
    paths=[directory/name for name in ['selected.json','anchor.json','short.json.gz','height.json.gz','prior.json.gz','resume.json.gz']]
    short_raw=json.dumps(short,sort_keys=True).encode();paths[0].write_bytes(selected_bytes);paths[1].write_bytes(anchor)
    paths[2].write_bytes(gzip.compress(short_raw));sha=[hashlib.sha256(x).hexdigest() for x in [selected_bytes,anchor,short_raw]]
    p,ref,receipt,cfg=load_short_model(json.loads(selected_bytes),anchor,short,*sha[:2],'bounded_short',artificial=True)
    receipt['exact_input_storage']={'short':{'decoded_sha256':sha[2]}}
    t,theta,grid=build_grid(p,9,6,16);data=p.geometry(ref,t,theta,3);h=p.port.side*float(data['center'][-1])
    hc=height_configuration();poly,_=proposal_polytope(p,ref,data,hc,artificial=True,artificial_override=(h-.001,10.,-10.))
    if not poly.decision(ref[p.slices['height']])['eligible_under_declared_sampled_floating_tolerances']:
        raise ArithmeticError('artificial relaxed reference rows must be feasible')
    heights=ref[p.slices['height']]
    selected={'height_coefficients_binary64':heights.tolist(),'height_coefficients_exact_binary64':exact_coefficients(heights),
        'exact_delta_from_reference':['0']*len(heights),'exact_delta_from_feasible_initial':['0']*len(heights)}
    height={'schema':'fixed-T-a-all-height-polytope-stage-audit-v1',
        'status':'complete-one-height-polytope-stage-no-joint-metric-solve','source_files_sha256':height_hashes(),
        'source_receipt':receipt,'configuration':hc,'initial_state':state_record(p,ref),'final_state':state_record(p,ref),
        'sampling_grid':grid,'artificial_inputs_only':True,'complete_frozen_metric_retained':True,
        'tangent_step_applied':False,'metric_step_applied':False,'joint_metric_solver_calls':0,
        'height_stage':{'polytope':poly.record(),'selected':selected},
        'full_reconstruction_checks':{'independent_reconstruction_passes_declared_sample_tolerances':True},
        'explicit_artificial_fixture_no_old_optimizer_called':True}
    raw=json.dumps(height,sort_keys=True).encode();paths[3].write_bytes(gzip.compress(raw));sha.append(hashlib.sha256(raw).hexdigest())
    args=argparse.Namespace(input=paths[0],anchor_input=paths[1],short_audit=paths[2],height_audit=paths[3],
        prior_joint_audit=paths[4],resume_audit=paths[5],expected_input_sha256=sha[0],expected_anchor_sha256=sha[1],
        expected_short_sha256=sha[2],expected_height_sha256=sha[3],expected_prior_joint_sha256=None,
        expected_resume_sha256=None,out=directory/'maximum.json')
    pp,reference,accepted,hprior,rec,source_cfg=prepare_original_inputs(args,artificial=True)
    joint=SingleQProblem(pp);initial=joint.lift_state(accepted);pcfg=prior_configuration()
    pcfg.update(joint_radial_nodes=9,joint_angular_nodes=16,joint_collar_subdivisions=6,joint_evaluate_only=True)
    wt,wtheta,wgrid=build_grid(joint,9,6,16);wdata=joint.geometry(initial,wt,wtheta,3)
    weights=joint.port.side*joint.height_basis.integral(np.array([joint.seed.length]))[0]
    gate=HeightAffineGate(family=frozen_family(joint,initial),kind='frozen-frame',height_slice=joint.slices['height'],
        nunknown=joint.nunknown,side=joint.port.side,length=joint.seed.length,
        target_definition={'explicit_artificial_polytope_target':poly.cap_target},
        intercept=joint.port.side*float(wdata['center'][-1])-float(weights@initial[joint.slices['height']]),
        weights=weights,target=poly.cap_target,evaluation=joint.evaluation_definition(),reference_provenance={'artificial_only':True})
    lower=np.full(joint.nunknown,-8.);upper=np.full(joint.nunknown,8.)
    lower[joint.slices['height']]=poly.lower;upper[joint.slices['height']]=poly.upper
    previous={'schema':PRIOR_SCHEMA,'status':'complete-one-quartic-one-joint-stage-and-fixed-state-audit',
        'source_files_sha256':prior_hashes(),'exact_input_storage':rec['exact_input_storage'],
        'configuration':pcfg,'artificial_inputs_only':True,'complete_frozen_metric_retained':True,'height_reference_unchanged':True,
        'accepted_height_state':state_record(pp,accepted),'post_quartic_state':state_record(pp,accepted),
        'joint_initial_state':state_record(joint,initial),'final_state':state_record(joint,initial),'joint_sampling_definition':wgrid,
        'quartic_stage':{'status':'quartic-proposal-selected','slsqp_calls':0,'selected':selected},
        'joint_stage':{'status':'explicit-artificial-no-solve-fixture','solver':{'minimize_invocation_count':0},
            'checkpoint':{'height_gate':gate.record(),'box_lower':lower.tolist(),'box_upper':upper.tolist()}},
        'explicit_artificial_fixture_not_a_claimed_public_solver_run':True}
    raw=json.dumps(previous,sort_keys=True).encode();paths[4].write_bytes(gzip.compress(raw))
    args.expected_prior_joint_sha256=hashlib.sha256(raw).hexdigest()
    prepared=prepare_resume(args,artificial=True);replay=prepared[-1]
    rcfg=copy.deepcopy(replay[-2]);rcfg.update(minimum_signed_height_exact='-10',joint_evaluate_only=True)
    latest={'schema':RESUME_SCHEMA,'status':'complete-reused-quartic-and-one-resumed-joint-audit',
        'source_files_sha256':resume_hashes(),'exact_input_storage':prepared[7],'configuration':rcfg,
        'input_replay':replay[-1],'artificial_inputs_only':True,'quartic_solver_calls_this_run':0,
        'complete_frozen_metric_retained':True,'height_reference_unchanged':True,
        'accepted_height_state':state_record(pp,accepted),'post_quartic_state':state_record(pp,accepted),
        'warm_start_selection':{'selected_candidate':'original_accepted_height'},
        'joint_initial_state':state_record(joint,initial),'final_state':state_record(joint,initial),
        'joint_sampling_definition':wgrid,
        'joint_stage':{'status':'explicit-artificial-no-solve-fixture','solver':{'minimize_invocation_count':0},
            'checkpoint':{'height_gate':gate.record(),'box_lower':lower.tolist(),'box_upper':upper.tolist(),
                'best_jointly_eligible_point':{'parameter_coefficients_binary64':initial.tolist(),
                    'exact_binary64_coefficients':exact_coefficients(initial),
                    'record':{'eligible_under_all_declared_constraints':True}}}},
        'explicit_artificial_fixture_not_a_claimed_public_solver_run':True}
    raw=json.dumps(latest,sort_keys=True).encode();paths[5].write_bytes(gzip.compress(raw))
    args.expected_resume_sha256=hashlib.sha256(raw).hexdigest()
    return args,prepared,latest


def developer_check():
    arrays=array_check()
    with tempfile.TemporaryDirectory(prefix='metric-epigraph-six-input-artificial-',dir='/dev/shm') as folder:
        args,previous,latest=artificial_fixture(Path(folder));prepared=prepare_maximum(args,artificial=True)
        report=run_maximum(prepared,args.out,artificial=True,evaluate_only=True)
        summary=json.loads(summary_path(args.out).read_text())
        bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args);wrong.expected_resume_sha256='0'*64;wrong.out=Path(folder)/'wrong-sixth.json'
        try:prepare_maximum(wrong,artificial=True);bad_sha=False
        except ValueError:
            failure=json.loads(wrong.out.read_text());bad_sha=(failure['phase']=='latest-resume-decoded-byte-binding'
                and failure['new_epigraph_solver_calls']==0)
        changed=copy.deepcopy(latest);changed['final_state']['canonical_physical_state_sha256']='0'*64
        try:replay_latest(previous,changed,artificial=True);bad_state=False
        except ValueError:bad_state=True
        changed=copy.deepcopy(latest);changed['joint_stage']['checkpoint']['height_gate']['numerical_gate_sha256']='0'*64
        try:replay_latest(previous,changed,artificial=True);bad_gate=False
        except ValueError:bad_gate=True
    stage=report.get('epigraph_stage',{})
    no_call=stage.get('solver',{}).get('minimize_invocation_count')==0
    finer=report.get('final_doubled_constraints',{})
    no_delta_inflation=(report.get('final_auxiliary_delta')==report.get('initial_auxiliary_delta'))
    passed=bool(arrays['passed'] and report['status']=='complete-one-true-max-metric-epigraph-and-fixed-state-audit'
        and no_call and bound and bad_sha and bad_state and bad_gate
        and report.get('initial_state')==report.get('final_state')
        and no_delta_inflation and 'eligible_under_all_declared_sampled_constraints' in finer
        and np.isfinite(finer.get('direct_max_eta',np.nan)))
    return {'schema':'metric-epigraph-six-input-main-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_evaluated_or_optimized':False,'new_formula_array_check':arrays,
        'full_six_input_replay_and_main_status':report['status'],'full_main_error':report.get('error'),
        'full_main_calls_no_old_or_new_optimizer':no_call,'physical_state_unchanged_in_evaluation_only_main':report.get('initial_state')==report.get('final_state'),
        'sixth_SHA_error_saves_small_report':bad_sha,'changed_final_physical_state_rejected':bad_state,
        'changed_published_cap_row_rejected':bad_gate,'full_summary_byte_binding':bound,
        'auxiliary_scalar_kept_out_of_physical_identity':report.get('auxiliary_delta_not_added_to_physical_state'),
        'no_auxiliary_delta_inflation_after_finer_sampling':no_delta_inflation,
        'finer_sampled_gate_result_reported_without_being_assumed_true':finer.get('eligible_under_all_declared_sampled_constraints'),
        'same_state_final_Pi_refinement':report.get('same_parameter_Pi_refinement'),'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--anchor-input',type=Path)
    parser.add_argument('--short-audit',type=Path);parser.add_argument('--height-audit',type=Path)
    parser.add_argument('--prior-joint-audit',type=Path);parser.add_argument('--resume-audit',type=Path)
    for key in ['input','anchor','short','height','prior-joint','resume']:parser.add_argument('--expected-'+key+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:answer=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'metric-epigraph-main-development-error-v1','artificial_inputs_only':True,
                'passed':False,'source_files_sha256':implementation_hashes(),
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        answer['source_files_sha256']=implementation_hashes();atomic_save(args.out,answer)
        print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
        if not answer['passed']:raise SystemExit(1)
        return
    try:prepared=prepare_maximum(args)
    except Exception:raise SystemExit(1)
    answer=run_maximum(prepared,args.out)
    print(json.dumps({'out':str(args.out),'status':answer['status']}),flush=True)
    if answer['status']!='complete-one-true-max-metric-epigraph-and-fixed-state-audit':raise SystemExit(1)


if __name__=='__main__':main()

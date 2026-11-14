#!/usr/bin/env python3
"""One fixed-T quartic stage then one 163-variable constrained joint pilot.

Actual use requires this public repository Actions and four SHA-bound input
reports. The old fixed metric and immutable height reference never change.
--check-only covers the complete artificial loader/checkpoint/audit path,
while the joint optimizer itself is tested on explicit array-only data.
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
from frame_entry_paired_repair import EntryRepairProblem
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_entry_paired_repair_audit import require_public_actions,JETS
from frame_entry_short_bounded_audit import (
    read_input,build_grid,audit_data,compare_data,compact_state,compact_audit,
    compact_comparison,summary_path,artificial_inputs,default_configuration as short_defaults,
    implementation_hashes as short_hashes)
from frame_independent_height_solve import state_record
from frame_height_polytope import HeightPolytope
from frame_height_polytope_audit import (
    load_short_model,implementation_hashes as polytope_hashes,
    stage_configuration as polytope_configuration,run_stage as run_polytope_stage)
from frame_height_quartic import FixedTangentHeightQuartic,propose_height_quartic
from frame_entry_single_q import SingleQProblem
from frame_height_affine_gate import HeightAffineGate,frozen_family
from frame_joint_height_objective import (
    JointSignedHeightObjective,run_joint_slsqp,developer_check as joint_array_check)

SCHEMA='fixed-g-quartic-then-one-Q-joint-height-audit-v1'


def implementation_hashes():
    result=polytope_hashes()
    for name in ['frame_height_quartic.py','frame_entry_single_q.py','frame_height_affine_gate.py',
                 'frame_joint_height_objective.py',Path(__file__).name]:
        result[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return result


def configuration():
    return {'quartic_maxiter':120,'quartic_max_evaluations':300,'quartic_max_seconds':30.,
        'quartic_ftol':1e-12,'joint_maxiter':80,'joint_max_evaluations':120,
        'joint_max_seconds':300.,'joint_ftol':1e-10,'joint_radial_nodes':61,
        'joint_angular_nodes':192,'joint_collar_subdivisions':24,
        'old_tangent_lower':'-8','old_tangent_upper':'8','new_Q_lower':'-8','new_Q_upper':'8',
        'height_box_and_signed_z_and_cap_target':'unchanged from the accepted public height polytope',
        'height_tolerance':1e-9,'signed_z_tolerance':1e-9,'box_tolerance':0.,
        'height_reconstruction_tolerance':1e-10,'checkpoint_evaluations':10,'checkpoint_seconds':60.,
        'joint_evaluate_only':False,'no_metric_design_or_height_reference_change':True}


def load_accepted_polytope(original,anchor,short,prior,selected_sha,anchor_sha,short_sha,*,artificial=False):
    if (prior.get('schema')!='fixed-T-a-all-height-polytope-stage-audit-v1'
            or prior.get('status')!='complete-one-height-polytope-stage-no-joint-metric-solve'):
        raise ValueError('completed exact height-polytope audit required')
    if bool(prior.get('artificial_inputs_only'))!=bool(artificial):
        raise ValueError('artificial and research reports cannot be interchanged')
    if prior.get('source_files_sha256')!=polytope_hashes():
        raise ValueError('frozen height-polytope implementation mismatch')
    upstream=prior['source_receipt']
    if upstream.get('exact_input_storage',{}).get('short',{}).get('decoded_sha256')!=short_sha:
        raise ValueError('height stage is not bound to the exact preceding short report')
    case=upstream.get('chosen_short_case')
    if case!='bounded_short':raise ValueError('this declared pilot uses the bounded short model only')
    problem,reference,receipt,source_cfg=load_short_model(original,anchor,short,
        selected_sha,anchor_sha,case,artificial=artificial)
    if state_record(problem,reference)!=prior['initial_state']:
        raise ValueError('height-polytope initial full state does not replay')
    selected=prior.get('height_stage',{}).get('selected')
    if selected is None or not prior.get('full_reconstruction_checks',{}).get(
            'independent_reconstruction_passes_declared_sample_tolerances'):
        raise ValueError('an independently reconstructed accepted height proposal is required')
    current=np.asarray(prior['final_state']['parameter_coefficients_binary64'],float)
    if state_record(problem,current)!=prior['final_state']:
        raise ValueError('height-polytope final complete physical/evaluation state does not replay')
    for name in ['u','v','metric']:
        if not np.array_equal(current[problem.slices[name]],reference[problem.slices[name]]):
            raise ValueError('the accepted height stage changed a nonheight coefficient')
    h=current[problem.slices['height']]
    if ([str(Q.from_float(float(x))) for x in h]!=selected['height_coefficients_exact_binary64']
            or not np.array_equal(h,np.asarray(selected['height_coefficients_binary64']))):
        raise ValueError('selected absolute height coefficients do not replay exactly')
    delta=[str(Q.from_float(float(x))-Q.from_float(float(y)))
           for x,y in zip(h,reference[problem.slices['height']])]
    if delta!=selected['exact_delta_from_reference']:
        raise ValueError('selected height finite change does not replay exactly')
    if (prior.get('tangent_step_applied') or prior.get('metric_step_applied')
            or prior.get('joint_metric_solver_calls')!=0
            or not prior.get('complete_frozen_metric_retained')
            or problem.metric_model(reference)!=problem.metric_model(current)):
        raise ValueError('published stage is not the declared same-g height-only change')
    _,_,grid=build_grid(problem,source_cfg['radial_nodes'],source_cfg['collar_subdivisions'],source_cfg['angular_nodes'])
    if grid!=prior['sampling_grid']:raise ValueError('accepted bounded sampling grid does not replay')
    receipt.update(accepted_height_state_sha256=digest(problem.identity(current)),
        accepted_height_polytope_sha256=prior['height_stage']['polytope']['definition_sha256'],
        accepted_height_complete_state_replayed=True,
        all_old_tangent_coefficients_and_frozen_metric_preserved=True)
    return problem,reference,current,receipt,source_cfg


def exact_evaluated_scalar(record):
    value=float(record['binary64'])
    if str(Q.from_float(value))!=record['exact_binary64_rational']:
        raise ValueError('frozen numerical scalar has inconsistent exact binary64 identity')
    return value


def restore_numerical_polytope(problem,reference,data,prior):
    record=prior['height_stage']['polytope'];definition=record['definition']
    if digest(definition)!=record['definition_sha256']:
        raise ValueError('published numerical polytope digest mismatch')
    if [str(Q.from_float(float(x))) for x in reference[problem.slices['height']]]!=definition['reference_current_coefficients']:
        raise ValueError('published polytope reference coefficient differs')
    poly=HeightPolytope(data['X'],problem.height_basis.integral(data['radial']),
        reference[problem.slices['height']],side=definition['side'],
        cap_intercept=exact_evaluated_scalar(definition['cap_intercept_evaluated']),
        cap_row=[exact_evaluated_scalar(x) for x in definition['cap_row_evaluated']],
        cap_target=exact_evaluated_scalar(definition['cap_target_evaluated']),
        coefficient_lower=[float(Q(x)) for x in definition['coefficient_lower']],
        coefficient_upper=[float(Q(x)) for x in definition['coefficient_upper']],
        ball_radius=exact_evaluated_scalar(definition['ball_radius_evaluated']),
        minimum_signed_height=exact_evaluated_scalar(definition['minimum_signed_height_evaluated']),
        radial=data['radial'],theta=data['theta'],provenance=copy.deepcopy(definition['provenance']))
    if poly.numerical_definition!=definition:
        oldA=np.asarray(definition['row_A_evaluated']);oldb=np.asarray(definition['row_b_evaluated'])
        deltaA=float(np.max(abs(poly.A-oldA))) if poly.A.shape==oldA.shape else None
        deltab=float(np.max(abs(poly.b-oldb))) if poly.b.shape==oldb.shape else None
        raise ValueError('reference evaluation did not reproduce the original numerical polytope: '+
                         json.dumps({'A_max_difference':deltaA,'b_max_difference':deltab,
                                     'new_sha':poly.sha256,'old_sha':record['definition_sha256']}))
    return poly


def reconstruction_gate(problem,data,poly,tolerance):
    cap=problem.port.side*float(data['center'][-1])
    signed=float(np.min(problem.port.side*data['X'][...,2]))
    ball=float(np.max(np.sum(data['X']**2,axis=-1)/poly.ball_radius**2))
    passed=(cap>=poly.cap_target-tolerance and signed>=poly.zmin-tolerance
            and ball<=1+4*tolerance/max(poly.ball_radius,1e-30))
    return {'cap_height':cap,'cap_margin':cap-poly.cap_target,'minimum_signed_height':signed,
        'maximum_ball_squared_normalized':ball,'tolerance':float(tolerance),
        'passes_declared_floating_sampled_height_and_ball_gate':bool(passed),
        'not_continuous_feasibility_or_reach':True}


def brief_summary(report,out):
    keys=['schema','status','github_sha','github_run_id','github_repository','configuration',
        'source_files_sha256','exact_input_storage','elapsed_seconds','peak_rss_kib_linux',
        'complete_frozen_metric_retained','height_reference_unchanged','research_candidate_evaluated',
        'artificial_inputs_only','error','phase','quartic_reconstruction_gate','quartic_six_jet_change_check',
        'zero_Q_warm_six_jet_errors',
        'final_current_constraints','same_parameter_Pi_refinement','input_replay',
        'unchanged_height_integrals_not_repeated']
    result={k:report.get(k) for k in keys if k in report}
    for k in ['accepted_height_state','post_quartic_state','joint_initial_state','final_state']:
        if k in report:result[k]=compact_state(report[k])
    for k in ['accepted_height_audit','post_quartic_audit','joint_work_initial_audit',
              'joint_work_final_audit','final_fine_audit','doubled_angle_final_audit']:
        if k in report:result[k]=compact_audit(report[k])
    if 'same_parameter_Pi_refinement' in result:
        result['same_parameter_Pi_refinement']=compact_comparison(result['same_parameter_Pi_refinement'])
    if 'quartic_stage' in report:
        stage=report['quartic_stage'];relax=stage['objective']['rowwise_unrestricted_height_relaxation']
        result['quartic_stage']={k:stage.get(k) for k in ['status','slsqp_calls','objective_evaluations',
            'initial_direct_metric_cost','selected','optimizer_result','error','budget_exit','elapsed_seconds']}
        result['quartic_stage']['rowwise_relaxation']={k:relax.get(k) for k in
            ['sum_of_independent_row_minima_evaluated','worst_row_by_relaxed_metric_cost',
             'reported_floating_root_estimates_are_not_rigorous_lower_bound_certificates']}
    if 'joint_stage' in report:
        stage=report['joint_stage'];snap=stage.get('checkpoint',stage)
        result['joint_stage']={k:stage.get(k) for k in ['status','solver','error','budget_message']}
        result['joint_stage'].update(evaluations=snap.get('evaluations'),elapsed_seconds=snap.get('elapsed_seconds'),
            maximum_cached_array_bytes=snap.get('maximum_cached_array_bytes'),
            objective_evaluation_sha256=snap.get('objective_evaluation_sha256'))
        for k in ['best_jointly_eligible_point','lowest_objective_trial_point_may_be_ineligible']:
            point=snap.get(k)
            result['joint_stage'][k]=None if point is None else point.get('record')
    raw=Path(out).read_bytes()
    result.update(summary_schema='quartic-joint-scientific-summary-v1',
        full_report={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},
        sampled_only=True,task_complete=False,embedding_proved=False,whole_surface_reach_proved=False)
    return result


def run_chain(problem,reference,accepted,prior,receipt,source_cfg,cfg,out,*,artificial=False):
    start=time.monotonic();fixed_metric=problem.metric_model(accepted)
    reference=np.asarray(reference,float).copy();accepted=np.asarray(accepted,float).copy()
    t,theta,fine_grid=build_grid(problem,source_cfg['radial_nodes'],source_cfg['collar_subdivisions'],source_cfg['angular_nodes'])
    order=source_cfg['primitive_order'];height_cfg=prior['configuration']
    answer={'schema':SCHEMA,'github_sha':os.environ.get('GITHUB_SHA'),
        'github_run_id':os.environ.get('GITHUB_RUN_ID'),'github_repository':os.environ.get('GITHUB_REPOSITORY'),
        'source_files_sha256':implementation_hashes(),'configuration':copy.deepcopy(cfg),
        'exact_input_storage':receipt.get('exact_input_storage',{}),'source_receipt':receipt,
        'fine_sampling_definition':fine_grid,'accepted_height_state':state_record(problem,accepted),
        'complete_frozen_metric_retained':True,'height_reference_unchanged':True,
        'research_candidate_evaluated':False,'artificial_inputs_only':bool(artificial),
        'task_complete':False,'embedding_proved':False,'whole_surface_reach_proved':False}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-start
        answer['peak_rss_kib_linux']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        atomic_save(out,answer);atomic_save(summary_path(out),brief_summary(answer,out))
    save('inputs-replayed-before-geometry')
    try:
        answer['phase']='original-fixed-T-polytope-numerical-replay'
        reference_data=problem.geometry(reference,t,theta,order)
        answer['research_candidate_evaluated']=not artificial
        poly=restore_numerical_polytope(problem,reference,reference_data,prior)
        answer['input_replay']={'accepted_state_complete':True,
            'original_numerical_polytope_reconstructed_exactly':True,'polytope_sha256':poly.sha256}
        accepted_data=problem.geometry(accepted,t,theta,order)
        answer['accepted_height_audit']=audit_data(problem,accepted,accepted_data,height_cfg['tau'])
        objective=FixedTangentHeightQuartic(reference_data,problem.height_basis.evaluate(t),poly,
            provenance={'fixed_metric_sha256':fixed_metric['mathematical_definition_sha256'],
                'reference_field_sha256':digest(problem.identity(reference)),
                'accepted_initial_field_sha256':digest(problem.identity(accepted)),
                'all_inputs_are_exactly_replayed_public_models':True})
        def quartic_checkpoint(stage):
            answer['quartic_stage']=stage;save('quartic-'+stage['status'])
        answer['phase']='one-fixed-T-quartic-stage'
        stage=propose_height_quartic(objective,accepted[problem.slices['height']],
            maxiter=cfg['quartic_maxiter'],max_evaluations=cfg['quartic_max_evaluations'],
            max_seconds=cfg['quartic_max_seconds'],ftol=cfg['quartic_ftol'],
            row_tolerance=height_cfg['row_tolerance'],box_tolerance=height_cfg['box_tolerance'],
            checkpoint=quartic_checkpoint)
        answer['quartic_stage']=stage
        if stage['selected'] is None:
            save('quartic-no-eligible-initial-or-proposal-no-joint');return answer
        after=accepted.copy();newh=np.asarray(stage['selected']['height_coefficients_binary64'])
        if [str(Q.from_float(float(x))) for x in newh]!=stage['selected']['height_coefficients_exact_binary64']:
            raise ArithmeticError('quartic selected height exact coefficients differ')
        for label,oldh in [('exact_delta_from_reference',reference[problem.slices['height']]),
                           ('exact_delta_from_feasible_initial',accepted[problem.slices['height']])]:
            if [str(Q.from_float(float(x))-Q.from_float(float(y))) for x,y in zip(newh,oldh)]!=stage['selected'][label]:
                raise ArithmeticError('quartic selected exact height differences do not replay')
        after[problem.slices['height']]=newh
        after_data=problem.geometry(after,t,theta,order)
        delta=newh-accepted[problem.slices['height']]
        vertical={'X':problem.height_basis.integral(t)@delta,
            'Xs':problem.height_basis.evaluate(t)@delta,
            'Xss':problem.height_basis.evaluate(t,1)@delta}
        changes={}
        for key in JETS:
            expected=np.zeros_like(accepted_data[key])
            if key in vertical:expected[...,2]=vertical[key][:,None]
            changes[key]=float(np.max(abs(after_data[key]-accepted_data[key]-expected)))
        answer['quartic_six_jet_change_check']={'errors':changes,
            'T_bitwise_unchanged':bool(np.array_equal(after_data['T'],accepted_data['T'])),
            'all_nonheight_coefficients_bitwise_unchanged':all(np.array_equal(after[problem.slices[k]],
                accepted[problem.slices[k]]) for k in ['u','v','metric'])}
        if max(changes.values())>1e-8 or not answer['quartic_six_jet_change_check']['T_bitwise_unchanged']:
            raise ArithmeticError('quartic full geometry does not match the height-only finite change')
        answer['post_quartic_state']=state_record(problem,after)
        answer['post_quartic_audit']=audit_data(problem,after,after_data,height_cfg['tau'])
        answer['quartic_reconstruction_gate']=reconstruction_gate(problem,after_data,poly,height_cfg['row_tolerance'])
        if not answer['quartic_reconstruction_gate']['passes_declared_floating_sampled_height_and_ball_gate']:
            save('quartic-full-reconstruction-gate-failed-no-joint');return answer
        if problem.metric_model(after)!=fixed_metric:raise ArithmeticError('height stage changed g')
        del reference_data,accepted_data,after_data,objective

        answer['phase']='zero-Q-lift-and-new-work-grid'
        joint=SingleQProblem(problem);initial=joint.lift_state(after)
        work_t,work_theta,work_grid=build_grid(joint,cfg['joint_radial_nodes'],
            cfg['joint_collar_subdivisions'],cfg['joint_angular_nodes'])
        old_work=problem.geometry(after,work_t,work_theta,order)
        work_initial=joint.geometry(initial,work_t,work_theta,order)
        warm={key:float(np.max(abs(old_work[key]-work_initial[key]))) for key in JETS}
        answer['zero_Q_warm_six_jet_errors']=warm
        if max(warm.values())>1e-10:raise ArithmeticError('zero-Q old-field numerical replay exceeds declared check')
        answer['joint_sampling_definition']=work_grid
        answer['joint_initial_state']=state_record(joint,initial)
        answer['joint_work_initial_audit']=audit_data(joint,initial,work_initial,height_cfg['tau'])
        gate=HeightAffineGate.from_frozen_problem(joint,initial,work_initial,
            tau=height_cfg['tau'],height_margin=height_cfg['height_margin'])
        if artificial:
            # Explicit synthetic full-main data use a relaxed artificial target;
            # no actual optimizer bypass is allowed for this geometry family.
            weights=joint.port.side*joint.height_basis.integral(np.array([joint.seed.length]))[0]
            h=joint.port.side*float(work_initial['center'][-1])
            gate=HeightAffineGate(family=frozen_family(joint,initial),kind='frozen-frame',
                height_slice=joint.slices['height'],nunknown=joint.nunknown,side=joint.port.side,
                length=joint.seed.length,target_definition={'explicit_artificial_polytope_target':poly.cap_target},
                intercept=h-float(weights@initial[joint.slices['height']]),weights=weights,
                target=poly.cap_target,evaluation=joint.evaluation_definition(),reference_provenance={'artificial_only':True})
        elif abs(gate.target-poly.cap_target)>1e-14:
            raise ArithmeticError('joint exact cap target differs from the unchanged height stage target')
        lower=np.full(joint.nunknown,float(Q(cfg['old_tangent_lower'])))
        upper=np.full(joint.nunknown,float(Q(cfg['old_tangent_upper'])))
        lower[joint.q_index]=float(Q(cfg['new_Q_lower']));upper[joint.q_index]=float(Q(cfg['new_Q_upper']))
        lower[joint.slices['height']]=poly.lower;upper[joint.slices['height']]=poly.upper
        def joint_checkpoint(snapshot):
            answer['joint_stage']={'status':'joint-checkpoint','checkpoint':snapshot}
            save('joint-current-state-checkpoint')
        signed=JointSignedHeightObjective(joint,gate,work_t,work_theta,order,lower,upper,
            max_evaluations=cfg['joint_max_evaluations'],max_seconds=cfg['joint_max_seconds'],
            box_tolerance=cfg['box_tolerance'],height_tolerance=cfg['height_tolerance'],
            reconstruction_tolerance=cfg['height_reconstruction_tolerance'],
            minimum_signed_height=poly.zmin,signed_height_tolerance=cfg['signed_z_tolerance'],
            checkpoint=joint_checkpoint,checkpoint_every=cfg['checkpoint_evaluations'],
            checkpoint_seconds=cfg['checkpoint_seconds'])
        answer['joint_memory_accounting']={'sample_count':len(work_t)*len(work_theta),
            'parameter_count':joint.nunknown,
            'signed_constraint_Jacobian_array_bytes':len(work_t)*len(work_theta)*joint.nunknown*8,
            'whole_geometry_and_objective_peak_is_larger_than_this_cache':True,
            'observed_peak_RSS_recorded_at_each_checkpoint':True}
        del old_work,work_initial
        answer['phase']='one-joint-hard-cap-current-signed-z-stage'
        result=run_joint_slsqp(signed,initial,maxiter=cfg['joint_maxiter'],ftol=cfg['joint_ftol'],
            artificial_inputs_only=artificial,evaluate_only=cfg['joint_evaluate_only'])
        answer['joint_stage']=result
        chosen=result['checkpoint']['best_jointly_eligible_point']
        final=initial.copy() if chosen is None else np.asarray(chosen['parameter_coefficients_binary64'],float)
        if chosen is not None and [str(Q.from_float(float(x))) for x in final]!=chosen['exact_binary64_coefficients']:
            raise ArithmeticError('joint selected full state does not replay exact binary64 coefficients')
        answer['final_state']=state_record(joint,final)
        if joint.metric_model(final)!=fixed_metric or joint.height_base_definition!=problem.height_base_definition:
            raise ArithmeticError('joint stage changed the fixed g or immutable height reference')
        answer['phase']='selected-state-full-geometry-and-angle-refinement'
        work_final=joint.geometry(final,work_t,work_theta,order)
        answer['joint_work_final_audit']=audit_data(joint,final,work_final,height_cfg['tau'])
        final_data=joint.geometry(final,t,theta,order)
        answer['final_fine_audit']=audit_data(joint,final,final_data,height_cfg['tau'])
        cap_gate=gate.decision(final,final_data,lower,upper,
            box_tolerance=cfg['box_tolerance'],height_tolerance=cfg['height_tolerance'],
            reconstruction_tolerance=cfg['height_reconstruction_tolerance'])
        minz=float(np.min(joint.port.side*final_data['X'][...,2]))
        answer['final_current_constraints']={'cap_and_box':cap_gate,
            'fine_minimum_signed_height':minz,'signed_height_threshold':poly.zmin,
            'fine_signed_height_pass':bool(minz>=poly.zmin-cfg['signed_z_tolerance']),
            'coarse_optimizer_constraints_do_not_certify_fine_or_continuous_feasibility':True}
        save('selected-fine-state-audited-before-angle-doubling')
        del work_final,signed
        doubled_theta=np.arange(2*len(theta))*np.pi/len(theta)
        doubled=joint.geometry(final,t,doubled_theta,order)
        answer['doubled_angle_final_audit']=audit_data(joint,final,doubled,height_cfg['tau'],with_rows=False)
        answer['same_parameter_Pi_refinement']=compare_data(joint,final_data,joint,doubled,final,
            name='one selected joint state, fixed-g fixed-b0 Pi angle doubling',theta_stride=2)
        answer['unchanged_height_integrals_not_repeated']={
            'same_fixed_b0_GH_Nb_and_query_independent_primitive':True,
            'height_control_integrals_unchanged':True,
            'earlier_finite_integral_comparisons_do_not_certify_this_new_T_field':True,
            'no_reoptimization_after_evaluation_refinement':True}
        save('complete-one-quartic-one-joint-stage-and-fixed-state-audit')
        return answer
    except Exception as error:
        answer['error']={'type':type(error).__name__,'message':str(error)}
        save('stage-error-preserved-completed-checkpoints')
        raise


class InputReplayFailure(RuntimeError):pass


def prepare_run(args,*,artificial=False):
    bindings={};phase='public-repository-and-input-path-guard'
    try:
        paths=[args.input,args.anchor_input,args.short_audit,args.height_audit]
        if any(p is None for p in paths):raise ValueError('four explicit frozen input reports required')
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),paths)
        values={}
        for key,path,sha in zip(['selected','original_c0','short','height_polytope'],paths,
            [args.expected_input_sha256,args.expected_anchor_sha256,args.expected_short_sha256,args.expected_height_sha256]):
            phase=key+'-byte-binding'
            if not sha:raise ValueError('every decoded input SHA256 must be explicit')
            values[key],raw,bindings[key]=read_input(path,sha)
            if key=='original_c0':anchor=raw
        phase='complete-parent-state-and-height-proposal-replay'
        problem,reference,accepted,receipt,source_cfg=load_accepted_polytope(
            values['selected'],anchor,values['short'],values['height_polytope'],
            bindings['selected']['decoded_sha256'],bindings['original_c0']['decoded_sha256'],
            bindings['short']['decoded_sha256'],artificial=artificial)
        receipt['exact_input_storage']=bindings
        return problem,reference,accepted,values['height_polytope'],receipt,source_cfg
    except Exception as error:
        report={'schema':SCHEMA,'status':'input-replay-failed-before-geometry','phase':phase,
            'error':{'type':type(error).__name__,'message':str(error)},'exact_input_storage':bindings,
            'source_files_sha256':implementation_hashes(),'research_candidate_evaluated':False,
            'quartic_solver_calls':0,'joint_solver_calls':0,'artificial_inputs_only':bool(artificial)}
        atomic_save(args.out,report);atomic_save(summary_path(args.out),brief_summary(report,args.out))
        raise InputReplayFailure(str(error)) from error


def artificial_check():
    array_check=joint_array_check()
    base,state,prior,receipt,selected_bytes,anchor=artificial_inputs()
    source_cfg=short_defaults();source_cfg.update(entry_length='3/25',entry_mean_nodes=32,
        uniform_panels=8,primitive_order=3,radial_nodes=9,angular_nodes=16,collar_subdivisions=6)
    pair=EntryRepairProblem(base,state,'3/25',entry_mean_nodes=32,uniform_panels=8,primitive_order=3)
    bounded=BoundedEntryHeightProblem(pair,state,uniform_panels=8,primitive_order=3)
    _,_,shared_grid=build_grid(pair,9,6,16)
    short={'schema':'short-entry-paired-bounded-one-height-step-audit-v1',
        'status':'complete-two-initial-fields-and-at-most-one-height-step-each',
        'source_files_sha256':short_hashes(),'source_receipt':receipt,
        'source_exact_state':state_record(base,state),'configuration':source_cfg,
        'selected_original_fixed_metric':base.metric_model(state),'sampling_grid':shared_grid,
        'cases':{'bounded_short':{'final_state':state_record(bounded,state)}},'artificial_inputs_only':True}
    with tempfile.TemporaryDirectory(prefix='quartic-joint-artificial-',dir='/dev/shm') as directory:
        directory=Path(directory);paths=[directory/name for name in ['selected.json','anchor.json','short.json.gz','height.json.gz']]
        short_raw=json.dumps(short,sort_keys=True).encode();paths[0].write_bytes(selected_bytes)
        paths[1].write_bytes(anchor);paths[2].write_bytes(gzip.compress(short_raw))
        selected_sha=hashlib.sha256(selected_bytes).hexdigest();anchor_sha=hashlib.sha256(anchor).hexdigest()
        short_sha=hashlib.sha256(short_raw).hexdigest()
        original=json.loads(selected_bytes)
        p,ref,rec,cfg=load_short_model(original,anchor,short,selected_sha,anchor_sha,'bounded_short',artificial=True)
        rec['exact_input_storage']={'short':{'decoded_sha256':short_sha}}
        t,theta,_=build_grid(p,9,6,16);data=p.geometry(ref,t,theta,3)
        h=p.port.side*float(data['center'][-1])
        height=run_polytope_stage(p,ref,cfg,rec,directory/'height-raw.json',polytope_configuration(),
            artificial=True,artificial_override=(h+.001,10.,-10.))
        height_raw=json.dumps(height,sort_keys=True).encode();paths[3].write_bytes(gzip.compress(height_raw))
        args=argparse.Namespace(input=paths[0],anchor_input=paths[1],short_audit=paths[2],height_audit=paths[3],
            expected_input_sha256=selected_sha,expected_anchor_sha256=anchor_sha,expected_short_sha256=short_sha,
            expected_height_sha256=hashlib.sha256(height_raw).hexdigest(),out=directory/'joint.json')
        pp,reference,accepted,replayed,replay,scfg=prepare_run(args,artificial=True)
        conf=configuration();conf.update(quartic_max_evaluations=0,joint_evaluate_only=True,
            joint_radial_nodes=9,joint_angular_nodes=16,joint_collar_subdivisions=6,
            joint_max_evaluations=3,joint_max_seconds=120.)
        result=run_chain(pp,reference,accepted,replayed,replay,scfg,conf,args.out,artificial=True)
        small=json.loads(summary_path(args.out).read_text())
        bound=(small['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest())
        wrong=copy.copy(args);wrong.expected_height_sha256='0'*64;wrong.out=directory/'bad.json'
        try:prepare_run(wrong,artificial=True);rejected=False
        except InputReplayFailure:
            failed=json.loads(wrong.out.read_text());rejected=(failed['phase']=='height_polytope-byte-binding'
                and failed['quartic_solver_calls']==0 and failed['joint_solver_calls']==0)
        bad=copy.deepcopy(height);bad['final_state']['canonical_physical_state_sha256']='0'*64
        try:load_accepted_polytope(original,anchor,short,bad,selected_sha,anchor_sha,short_sha,artificial=True);badstate=False
        except ValueError:badstate=True
        warm=result.get('zero_Q_warm_six_jet_errors',{})
        passed=bool(array_check['passed'] and result['status']=='complete-one-quartic-one-joint-stage-and-fixed-state-audit'
            and result['quartic_stage']['slsqp_calls']==0
            and result['joint_stage']['solver']['minimize_invocation_count']==0
            and warm and max(warm.values())<1e-10 and bound and rejected and badstate
            and result['final_current_constraints']['fine_signed_height_pass'])
        return {'schema':'quartic-single-Q-joint-full-main-artificial-check-v1',
            'artificial_inputs_only':True,'research_candidate_evaluated_or_optimized':False,
            'dynamic_constraint_array_check':array_check,
            'full_four_report_state_and_numerical_polytope_replay':True,
            'gzip_decoded_inputs_and_failure_JSON':rejected,'bad_full_state_rejected':badstate,
            'zero_Q_complete_position_jet_differences':warm,'full_summary_byte_binding':bound,
            'full_geometry_path_evaluation_only_without_actual_solver_bypass':True,
            'same_state_final_Pi_refinement':result['same_parameter_Pi_refinement'],
            'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--anchor-input',type=Path)
    parser.add_argument('--short-audit',type=Path);parser.add_argument('--height-audit',type=Path)
    for key in ['input','anchor','short','height']:parser.add_argument('--expected-'+key+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        report=artificial_check();report['source_files_sha256']=implementation_hashes()
        atomic_save(args.out,report);print(json.dumps({'out':str(args.out),'passed':report['passed']}),flush=True)
        if not report['passed']:raise SystemExit(1)
        return
    try:problem,reference,accepted,prior,receipt,source_cfg=prepare_run(args)
    except InputReplayFailure:raise SystemExit(1)
    result=run_chain(problem,reference,accepted,prior,receipt,source_cfg,configuration(),args.out)
    print(json.dumps({'out':str(args.out),'status':result['status']}),flush=True)


if __name__=='__main__':main()

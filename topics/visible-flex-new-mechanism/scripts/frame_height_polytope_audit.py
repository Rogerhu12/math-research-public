#!/usr/bin/env python3
"""Audit one published short-entry field with all height coefficients free.

Only a nine-variable sampled-height feasibility LP and a convex distance QP
are used. The tangent field, exact metric, core and cap stay frozen. No joint
u/v or direct-metric nonlinear solve is performed by this driver.
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
from frame_fixed_height_primitive_audit import load_selected_report
from frame_entry_paired_repair import EntryRepairProblem
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_entry_paired_repair_audit import require_public_actions,polygon_vertex_height_conditions,JETS
from frame_independent_height_solve import state_record
from frame_entry_short_bounded_audit import (
    implementation_hashes as short_hashes,read_input,build_grid,audit_data,compare_data,
    compact_state,compact_audit,compact_comparison,summary_path,
    default_configuration as short_default_configuration,artificial_inputs)
from frame_height_polytope import HeightPolytope,solve_height_polytope,developer_check as polytope_check

SCHEMA='fixed-T-a-all-height-polytope-stage-audit-v1'


def implementation_hashes():
    out=short_hashes()
    for name in ['frame_height_polytope.py',Path(__file__).name]:
        out[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return out


def load_short_model(original,anchor_bytes,short,selected_sha,anchor_sha,case,*,artificial=False):
    if short.get('schema')!='short-entry-paired-bounded-one-height-step-audit-v1':
        raise ValueError('published complete short-entry report required')
    if short.get('status')!='complete-two-initial-fields-and-at-most-one-height-step-each':
        raise ValueError('short-entry report is not complete')
    if bool(short.get('artificial_inputs_only'))!=bool(artificial):
        raise ValueError('artificial and actual short reports cannot be interchanged')
    if short.get('source_files_sha256')!=short_hashes():
        raise ValueError('short-entry frozen source implementation mismatch')
    prior=short['source_receipt']
    if (prior.get('selected_report_sha256')!=selected_sha
            or prior.get('original_c0_report_sha256')!=anchor_sha):
        raise ValueError('short report is not bound to the exact selected and c0 bytes')
    base,state,receipt=load_selected_report(original,anchor_bytes)
    if state_record(base,state)!=short['source_exact_state']:
        raise ValueError('original selected full state replay differs')
    cfg=short['configuration']
    paired=EntryRepairProblem(base,state,cfg['entry_length'],entry_mean_nodes=cfg['entry_mean_nodes'],
        uniform_panels=cfg['uniform_panels'],primitive_order=cfg['primitive_order'])
    if case=='paired_short':problem=paired
    elif case=='bounded_short':
        problem=BoundedEntryHeightProblem(paired,state,uniform_panels=cfg['uniform_panels'],
            primitive_order=cfg['primitive_order'])
    else:raise ValueError('one explicit paired_short or bounded_short case required')
    saved=short['cases'][case]['final_state']
    current=np.asarray(saved['parameter_coefficients_binary64'],float)
    if current.shape!=(problem.nunknown,) or not np.all(np.isfinite(current)):
        raise ValueError('finite full stored coefficient vector required')
    if state_record(problem,current)!=saved:
        raise ValueError('chosen short field canonical state, coefficients, g or evaluation replay differs')
    if problem.metric_model(current)!=short['selected_original_fixed_metric']:
        raise ValueError('chosen short field does not retain the published complete g')
    # The published two-case driver constructs one shared grid from paired
    # before evaluating either case. Replay that full provenance first.
    _,_,published_grid=build_grid(paired,cfg['radial_nodes'],cfg['collar_subdivisions'],cfg['angular_nodes'])
    if published_grid!=short['sampling_grid']:
        raise ValueError('published paired-source exact short audit grid replay differs')
    _,_,selected_grid=build_grid(problem,cfg['radial_nodes'],cfg['collar_subdivisions'],cfg['angular_nodes'])
    for candidate,owner in [(published_grid,paired),(selected_grid,problem)]:
        unhashed=copy.deepcopy(candidate);claimed=unhashed.pop('definition_sha256')
        if digest(unhashed)!=claimed:raise ValueError('sampling definition digest mismatch')
        if candidate['structural_partition']['source_height_base_definition_sha256']!=digest(owner.height_base_definition):
            raise ValueError('sampling height-reference provenance mismatch')
    def coordinate_structure(grid):
        value=copy.deepcopy(grid)
        value.pop('definition_sha256')
        value['structural_partition'].pop('source_height_base_definition_sha256')
        return value
    if coordinate_structure(selected_grid)!=coordinate_structure(published_grid):
        raise ValueError('chosen model changed an exact node, structural source or sampling rule')
    receipt['sampling_replay']={
        'original_shared_grid_owner':'paired_short, as in the published two-case driver',
        'published_complete_grid_definition_sha256':published_grid['definition_sha256'],
        'selected_model_grid_definition_sha256':selected_grid['definition_sha256'],
        'all_exact_nodes_structural_sources_and_sampling_rules_equal':True,
        'only_height_reference_provenance_and_its_derived_grid_digest_may_differ':True,
        'both_reference_hashes_checked_against_their_actual_immutable_models':True}
    receipt.update(selected_report_sha256=selected_sha,original_c0_report_sha256=anchor_sha,
        chosen_short_case=case,chosen_short_field_sha256=digest(problem.identity(current)),
        original_c0_not_replaced_by_the_short_selected_state=True,
        full_short_state_and_sampling_replayed=True)
    return problem,current,receipt,copy.deepcopy(cfg)


def stage_configuration():
    return {'height_coefficient_lower':'-1','height_coefficient_upper':'1',
        'minimum_signed_height':'0','tau':'61/1000','height_margin':'1/1000',
        'row_tolerance':1e-9,'box_tolerance':0.,'lp_seconds':30.,
        'qp_maxiter':200,'qp_ftol':1e-12,'distance_weights':'all one',
        'no_automatic_box_expansion':True}


def proposal_polytope(problem,state,data,cfg,*,artificial=False,artificial_override=None):
    I=problem.height_basis.integral(data['radial'])
    c=np.asarray(state)[problem.slices['height']]
    caprow=problem.port.side*I[-1]
    h=problem.port.side*float(data['center'][-1])
    intercept=h-float(caprow@c)
    conditions=polygon_vertex_height_conditions(problem,data,cfg['tau'])
    target=conditions['upper_branch_height_threshold_if_h_at_least_w']+float(Q(cfg['height_margin']))
    ball=problem.ball_radius;zmin=float(Q(cfg['minimum_signed_height']))
    if artificial_override is not None:
        if not artificial:raise ValueError('artificial constraint override forbidden for research')
        target,ball,zmin=map(float,artificial_override)
    provenance={'fixed_physical_field_sha256':digest(problem.identity(state)),
        'complete_fixed_metric_definition':problem.metric_model(state)['mathematical_definition'],
        'T_scalar_family':problem.source.space_definition(),
        'fixed_tangent_u_v_coefficients':{
            name:[str(Q.from_float(float(x))) for x in state[problem.slices[name]]] for name in ['u','v']},
        'immutable_height_reference':problem.height_base_definition,
        'height_basis_definition':problem.height_basis.identity,
        'core_identity':problem.port.identity,'physical_cap_identity':problem.tail.identity,
        'evaluation_definition':problem.evaluation_definition(),
        'tau_exact':str(Q(cfg['tau'])),'height_margin_exact':str(Q(cfg['height_margin'])),
        'R66_target_branch_formula':conditions['general_necessary_abs_height_gap_formula'],
        'selected_upper_branch_screen_not_a_general_embedding_obstruction':True,
        'artificial_constraint_override':artificial_override}
    poly=HeightPolytope(data['X'],I,c,side=problem.port.side,
        cap_intercept=intercept,cap_row=caprow,cap_target=target,
        coefficient_lower=float(Q(cfg['height_coefficient_lower'])),
        coefficient_upper=float(Q(cfg['height_coefficient_upper'])),
        ball_radius=ball,minimum_signed_height=zmin,radial=data['radial'],theta=data['theta'],
        provenance=provenance)
    return poly,conditions


def brief_summary(answer,out):
    result={key:answer.get(key) for key in [
        'schema','status','github_sha','github_run_id','github_repository','configuration','source_receipt',
        'source_files_sha256','elapsed_seconds','peak_rss_kib_linux','height_step_applied',
        'tangent_step_applied','metric_step_applied','joint_metric_solver_calls',
        'full_reconstruction_checks','complete_frozen_metric_retained','same_parameter_Pi_refinement',
        'unchanged_reference_integrals_not_repeated','artificial_inputs_only']}
    for key in ['initial_state','final_state']:
        if key in answer:result[key]=compact_state(answer[key])
    for key in ['initial_audit','final_audit','doubled_angle_final_audit']:
        if key in answer:result[key]=compact_audit(answer[key])
    if 'same_parameter_Pi_refinement' in answer:
        result['same_parameter_Pi_refinement']=compact_comparison(answer['same_parameter_Pi_refinement'])
    proposal=answer.get('height_stage')
    if proposal is not None:
        result['height_stage']={key:proposal.get(key) for key in [
            'status','lp_calls','qp_calls','lp_result','qp_result','lp_error','qp_error',
            'minimum_uniform_slack_evaluated','lp_candidate_without_slack','selected',
            'largest_LP_marginals_not_a_rigorous_dual_certificate','elapsed_seconds']}
        result['height_stage']['polytope_sha256']=proposal['polytope']['definition_sha256']
        result['height_stage']['horizontal_failure']=proposal['polytope']['horizontal_failure']
        result['height_stage']['individual_row_box_obstructions']=proposal['polytope']['individual_row_box_obstructions_evaluated']
    raw=Path(out).read_bytes()
    result.update(full_report={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},
        summary_schema='fixed-T-a-height-polytope-scientific-summary-v1',
        full_arrays_canonical_states_and_radial_rows_remain_in_bound_full_report=True,
        sampled_only=True,task_complete=False,embedding_proved=False,whole_surface_reach_proved=False)
    return result


def run_stage(problem,state,source_cfg,receipt,out,cfg,*,artificial=False,artificial_override=None):
    start=time.monotonic();state=np.asarray(state,float).copy();state.setflags(write=False)
    if problem.metric_free:raise ValueError('all target metric coefficients must already be frozen')
    t,theta,grid=build_grid(problem,source_cfg['radial_nodes'],source_cfg['collar_subdivisions'],source_cfg['angular_nodes'])
    order=source_cfg['primitive_order']
    answer={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),
        'configuration':copy.deepcopy(cfg),'source_sampling_configuration':copy.deepcopy(source_cfg),
        'source_receipt':receipt,'sampling_grid':grid,
        'initial_state':state_record(problem,state),'complete_frozen_metric_retained':True,
        'height_step_applied':False,'tangent_step_applied':False,'metric_step_applied':False,
        'joint_metric_solver_calls':0,'artificial_inputs_only':bool(artificial),
        'task_complete':False,'embedding_proved':False,'whole_surface_reach_proved':False}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-start
        answer['peak_rss_kib_linux']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        atomic_save(out,answer);atomic_save(summary_path(out),brief_summary(answer,out))
    save('inputs-replayed-before-geometry')
    data=problem.geometry(state,t,theta,order)
    answer['initial_audit']=audit_data(problem,state,data,cfg['tau'])
    poly,conditions=proposal_polytope(problem,state,data,cfg,artificial=artificial,
        artificial_override=artificial_override)
    answer['height_conditions_at_initial']=conditions
    def stage_checkpoint(value):
        answer['height_stage']=value
        save('height-stage-'+value['status'])
    proposal=solve_height_polytope(poly,row_tolerance=cfg['row_tolerance'],
        box_tolerance=cfg['box_tolerance'],lp_seconds=cfg['lp_seconds'],
        qp_maxiter=cfg['qp_maxiter'],qp_ftol=cfg['qp_ftol'],checkpoint=stage_checkpoint)
    answer['height_stage']=proposal
    new=state.copy();final=data
    selected=proposal.get('selected')
    if selected is not None:
        coefficient=np.asarray(selected['height_coefficients_binary64'],float)
        old=state[problem.slices['height']]
        exact=[str(Q.from_float(float(x))-Q.from_float(float(y))) for x,y in zip(coefficient,old)]
        if exact!=selected['exact_delta_from_reference']:
            raise ArithmeticError('selected exact coefficient differences do not replay')
        new[problem.slices['height']]=coefficient
        for name in ['u','v','metric']:
            if not np.array_equal(new[problem.slices[name]],state[problem.slices[name]]):
                raise ArithmeticError('a nonheight coefficient changed')
        if problem.metric_model(new)!=problem.metric_model(state):
            raise ArithmeticError('height proposal changed the complete fixed metric')
        final=problem.geometry(new,t,theta,order)
        delta=coefficient-old
        change={'X':problem.height_basis.integral(t)@delta,
                'Xs':problem.height_basis.evaluate(t)@delta,
                'Xss':problem.height_basis.evaluate(t,1)@delta}
        differences={}
        for key in JETS:
            expected=np.zeros_like(data[key])
            if key in change:expected[...,2]=change[key][:,None]
            differences[key]=float(np.max(abs(final[key]-data[key]-expected)))
        h=problem.port.side*float(final['center'][-1])
        signed=problem.port.side*final['X'][...,2]
        ball=np.sum(final['X']**2,axis=-1)/poly.ball_radius**2
        independently_checked=(h>=poly.cap_target-cfg['row_tolerance']
            and np.min(signed)>=poly.zmin-cfg['row_tolerance']
            and np.max(ball)<=1+4*cfg['row_tolerance']/max(poly.ball_radius,1e-30)
            and np.all(coefficient>=poly.lower-cfg['box_tolerance'])
            and np.all(coefficient<=poly.upper+cfg['box_tolerance']))
        answer['full_reconstruction_checks']={
            'all_nonheight_coefficients_bitwise_unchanged':True,
            'T_samples_bitwise_unchanged':bool(np.array_equal(data['T'],final['T'])),
            'complete_position_two_jet_finite_change_errors':differences,
            'reconstructed_cap_height':h,'cap_height_margin':h-poly.cap_target,
            'minimum_signed_height':float(np.min(signed)),
            'maximum_ball_squared_normalized':float(np.max(ball)),
            'independent_reconstruction_passes_declared_sample_tolerances':bool(independently_checked),
            'numeric_gate_is_not_continuous_feasibility_or_reach':True}
        answer['height_step_applied']=bool(np.any(new!=state))
    else:
        answer['full_reconstruction_checks']={'no_candidate_applied':True}
    answer['final_state']=state_record(problem,new)
    answer['final_audit']=audit_data(problem,new,final,cfg['tau'])
    save('stage-complete-before-fixed-state-angle-refinement')
    doubled_theta=np.arange(2*len(theta))*2*np.pi/(2*len(theta))
    doubled=problem.geometry(new,t,doubled_theta,order)
    if state_record(problem,new)!=answer['final_state']:
        raise ArithmeticError('fixed-state refinement changed the canonical field')
    answer['doubled_angle_final_audit']=audit_data(problem,new,doubled,cfg['tau'])
    answer['same_parameter_Pi_refinement']=compare_data(problem,final,problem,doubled,new,
        name='selected-height-fixed-field-Pi-angle-doubling',theta_stride=2)
    sparse=np.array([0.,problem.entry.left,problem.source.active_end,problem.seed.length])
    sparse_data=problem.geometry(new,sparse,theta,order)
    indexes=[int(np.flatnonzero(t==x)[0]) for x in sparse]
    answer['query_independent_interface_position_two_jet_difference']={
        key:float(np.max(abs(sparse_data[key]-final[key][indexes]))) for key in JETS}
    answer['unchanged_reference_integrals_not_repeated']={
        'immutable_b0_and_height_basis_unchanged':True,
        'prior_short_reference_Nb_and_GL_comparisons_remain_finite_evidence_only':True,
        'current_step_only_changes_exact_declared_height_control_coefficients':True,
        'no_additional_GH_Nb_or_common_primitive_parameter_search':True,
        'new_position_and_metric_fully_reconstructed_then_Pi_doubled':True}
    save('complete-one-height-polytope-stage-no-joint-metric-solve')
    return answer


def artificial_check():
    helper=polytope_check()
    base,state,prior,receipt,selected_bytes,anchor=artificial_inputs()
    source_cfg=short_default_configuration()
    source_cfg.update(entry_length='3/25',entry_mean_nodes=32,uniform_panels=8,primitive_order=3,
        refined_primitive_order=4,radial_nodes=9,angular_nodes=16,collar_subdivisions=6)
    pair=EntryRepairProblem(base,state,source_cfg['entry_length'],entry_mean_nodes=32,
        uniform_panels=8,primitive_order=3)
    bounded=BoundedEntryHeightProblem(pair,state,uniform_panels=8,primitive_order=3)
    _,_,grid=build_grid(pair,9,6,16)
    short={'schema':'short-entry-paired-bounded-one-height-step-audit-v1',
        'status':'complete-two-initial-fields-and-at-most-one-height-step-each',
        'source_files_sha256':short_hashes(),'source_receipt':receipt,
        'source_exact_state':state_record(base,state),'configuration':source_cfg,
        'selected_original_fixed_metric':base.metric_model(state),'sampling_grid':grid,
        'cases':{'bounded_short':{'final_state':state_record(bounded,state)}},'artificial_inputs_only':True}
    with tempfile.TemporaryDirectory(prefix='height-polytope-artificial-',dir='/dev/shm') as tmp:
        tmp=Path(tmp);selected_path=tmp/'selected.json';anchor_path=tmp/'anchor.json'
        short_path=tmp/'short.json.gz';selected_path.write_bytes(selected_bytes);anchor_path.write_bytes(anchor)
        short_raw=json.dumps(short,sort_keys=True).encode();short_path.write_bytes(gzip.compress(short_raw))
        selected_sha=hashlib.sha256(selected_bytes).hexdigest();anchor_sha=hashlib.sha256(anchor).hexdigest()
        original,_,_=read_input(selected_path,selected_sha)
        decoded,_,_=read_input(short_path,hashlib.sha256(short_raw).hexdigest())
        args=argparse.Namespace(input=selected_path,anchor_input=anchor_path,short_audit=short_path,
            expected_input_sha256=selected_sha,expected_anchor_sha256=anchor_sha,
            expected_short_sha256=hashlib.sha256(short_raw).hexdigest(),case='bounded_short',
            height_lower='-1',height_upper='1',minimum_signed_height='0',tau='61/1000',
            height_margin='1/1000',out=tmp/'input.json')
        problem,current,replay,cfg,stage_cfg=prepare_run(args,artificial=True)
        shared_provenance=(replay['sampling_replay']['all_exact_nodes_structural_sources_and_sampling_rules_equal']
            and replay['sampling_replay']['published_complete_grid_definition_sha256']
                !=replay['sampling_replay']['selected_model_grid_definition_sha256'])
        # The geometry is artificial; relaxed screen values force the apply/rebuild path.
        t,theta,_=build_grid(problem,9,6,16)
        data=problem.geometry(current,t,theta,3);h=problem.port.side*float(data['center'][-1])
        out=tmp/'audit.json'
        answer=run_stage(problem,current,cfg,replay,out,stage_configuration(),
            artificial=True,artificial_override=(h+.001,10.,-10.))
        summary=json.loads(summary_path(out).read_text())
        errors=answer['full_reconstruction_checks'].get('complete_position_two_jet_finite_change_errors',{})
        wrong=copy.deepcopy(decoded);wrong['cases']['bounded_short']['final_state']['canonical_physical_state_sha256']='0'*64
        try:load_short_model(original,anchor,wrong,selected_sha,anchor_sha,'bounded_short',artificial=True);reject=False
        except ValueError:reject=True
        tampered=copy.deepcopy(decoded);tampered['sampling_grid']['radial_nodes_exact'][1]='1/999'
        try:load_short_model(original,anchor,tampered,selected_sha,anchor_sha,'bounded_short',artificial=True);nodes_rejected=False
        except ValueError:nodes_rejected=True
        bad_args=copy.copy(args);bad_args.expected_short_sha256='0'*64;bad_args.out=tmp/'rejected-input.json'
        try:prepare_run(bad_args,artificial=True);failure_saved=False
        except InputReplayFailure:
            fail=json.loads(bad_args.out.read_text());small=json.loads(summary_path(bad_args.out).read_text())
            failure_saved=(fail['phase']=='short-report-byte-binding'
                and fail['candidate_geometry_evaluation_started'] is False and fail['lp_calls']==0
                and small['full_report']['sha256']==hashlib.sha256(bad_args.out.read_bytes()).hexdigest())
        guarded=False
        try:require_public_actions('false','Rogerhu12/math-research-public',[])
        except ValueError:guarded=True
        same_binding=(summary['full_report']['sha256']==hashlib.sha256(out.read_bytes()).hexdigest())
        passed=bool(helper['passed'] and answer['height_step_applied'] and errors
            and max(errors.values())<1e-8 and answer['full_reconstruction_checks']['T_samples_bitwise_unchanged']
            and answer['full_reconstruction_checks']['independent_reconstruction_passes_declared_sample_tolerances']
            and answer['height_stage']['lp_calls']==1 and answer['height_stage']['qp_calls']==1
            and answer['joint_metric_solver_calls']==0 and reject and guarded and same_binding
            and shared_provenance and nodes_rejected and failure_saved)
        return {'schema':'height-polytope-full-path-artificial-check-v1',
            'artificial_inputs_only':True,'research_geometry_evaluated':False,
            'helper_check':helper,'complete_position_two_jet_finite_change_errors':errors,
            'complete_short_canonical_state_replay_and_bad_state_rejection':reject,
            'gzip_decoded_byte_identity_check':True,'full_summary_binding':same_binding,
            'published_paired_grid_replays_bounded_coordinates_with_distinct_reference_provenance':shared_provenance,
            'modified_exact_sampling_coordinate_rejected':nodes_rejected,
            'input_loader_failure_preserves_small_JSON_and_bound_summary':failure_saved,
            'public_Actions_guard_rejection':guarded,'no_Actions_environment_forged':True,
            'one_LP_one_QP_then_full_geometry_no_joint_solve':True,'passed':passed}



class InputReplayFailure(RuntimeError):
    pass


def prepare_run(args,*,artificial=False):
    """Full input path; every pre-geometry failure gets a bounded JSON receipt."""
    phase='public-repository-and-path-guard';bindings={}
    try:
        if any(x is None for x in [args.input,args.anchor_input,args.short_audit]):
            raise ValueError('selected report, original c0 and completed short report are required')
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [args.input,args.anchor_input,args.short_audit])
        phase='selected-input-byte-binding'
        original,_,bindings['selected']=read_input(args.input,args.expected_input_sha256)
        phase='original-c0-byte-binding'
        _,anchor,bindings['original_c0']=read_input(args.anchor_input,args.expected_anchor_sha256)
        phase='short-report-byte-binding'
        short,_,bindings['short']=read_input(args.short_audit,args.expected_short_sha256)
        phase='complete-state-metric-and-shared-sampling-replay'
        problem,state,receipt,source_cfg=load_short_model(original,anchor,short,
            bindings['selected']['decoded_sha256'],bindings['original_c0']['decoded_sha256'],
            args.case,artificial=artificial)
        receipt['exact_input_storage']=bindings
        phase='height-stage-configuration'
        cfg=stage_configuration()
        cfg.update(height_coefficient_lower=str(Q(args.height_lower)),height_coefficient_upper=str(Q(args.height_upper)),
            minimum_signed_height=str(Q(args.minimum_signed_height)),tau=str(Q(args.tau)),height_margin=str(Q(args.height_margin)))
        if Q(cfg['height_coefficient_lower'])>=Q(cfg['height_coefficient_upper']):
            raise ValueError('strict coefficient box required')
        if Q(cfg['tau'])<=0 or Q(cfg['height_margin'])<0:
            raise ValueError('invalid declared reach target or margin')
        return problem,state,receipt,source_cfg,cfg
    except Exception as error:
        failure={'schema':'height-polytope-input-replay-failure-v1',
            'status':'input-validation-failed-before-candidate-geometry-or-LP',
            'phase':phase,'error':{'type':type(error).__name__,'message':str(error)},
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'source_files_sha256':implementation_hashes(),
            'input_paths':{key:str(getattr(args,key,None)) for key in ['input','anchor_input','short_audit']},
            'expected_decoded_sha256':{key:getattr(args,key,None) for key in [
                'expected_input_sha256','expected_anchor_sha256','expected_short_sha256']},
            'verified_input_storage_before_failure':bindings,'case':args.case,
            'artificial_inputs_only':bool(artificial),'candidate_geometry_evaluation_started':False,
            'lp_calls':0,'qp_calls':0,'parameter_step_applied':False,
            'task_complete':False,'embedding_proved':False,'whole_surface_reach_proved':False}
        atomic_save(args.out,failure)
        raw=Path(args.out).read_bytes();summary=copy.deepcopy(failure)
        summary['full_report']={'path':str(args.out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
        atomic_save(summary_path(args.out),summary)
        raise InputReplayFailure(str(error)) from error

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true')
    p.add_argument('--input',type=Path);p.add_argument('--anchor-input',type=Path);p.add_argument('--short-audit',type=Path)
    p.add_argument('--expected-input-sha256');p.add_argument('--expected-anchor-sha256');p.add_argument('--expected-short-sha256')
    p.add_argument('--case',choices=['paired_short','bounded_short'],default='bounded_short')
    p.add_argument('--height-lower',default='-1');p.add_argument('--height-upper',default='1')
    p.add_argument('--minimum-signed-height',default='0');p.add_argument('--tau',default='61/1000')
    p.add_argument('--height-margin',default='1/1000')
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    if args.check_only:
        report=artificial_check();report['source_files_sha256']=implementation_hashes()
        atomic_save(args.out,report);print(json.dumps({'out':str(args.out),'passed':report['passed']}),flush=True)
        if not report['passed']:raise SystemExit(1)
        return
    try:problem,state,receipt,source_cfg,cfg=prepare_run(args)
    except InputReplayFailure as error:
        print(json.dumps({'out':str(args.out),'status':'input-replay-failed','error':str(error)}),flush=True)
        raise SystemExit(1)
    answer=run_stage(problem,state,source_cfg,receipt,args.out,cfg)
    print(json.dumps({'out':str(args.out),'status':answer['status'],
        'height_step_applied':answer['height_step_applied'],'joint_metric_solver_calls':0}),flush=True)


if __name__=='__main__':main()

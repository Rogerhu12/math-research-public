#!/usr/bin/env python3
"""Actions-only initial audit of the paired entry repair, with selected g fixed.

No optimizer is called.  The original selected state is first replayed by the
published strict loader.  Identical raw coefficients are then interpreted in
the explicitly new entry space; that change is never called same-field replay.
--check-only executes this complete orchestration on artificial inputs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
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
from frame_fixed_height_primitive import FixedPrimitiveProblem
from frame_fixed_height_primitive_audit import (artificial_carrier,load_selected_report,
    height_conditions,implementation_hashes as primitive_hashes)
from frame_independent_height_solve import (state_record,sampled_audit,radial_distribution,
    point_values,objective_cost,extremum,compare_evaluation)
from frame_entry_paired_repair import EntryRepairProblem


JETS=['X','Xs','Xt','Xss','Xst','Xtt']


def implementation_hashes():
    hashes=primitive_hashes()
    for name in ['frame_entry_paired_repair.py',Path(__file__).name]:
        hashes[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return hashes


def position_difference(before,after):
    return {key:float(np.max(np.linalg.norm(before[key]-after[key],axis=-1))) for key in JETS}


def require_public_actions(actions,repository,paths):
    if actions!='true' or repository!='Rogerhu12/math-research-public':
        raise ValueError('Research candidate evaluation requires this public repository Actions')
    notes=Path(__file__).resolve().parents[1]/'notes'
    if any(not Path(path).resolve().is_relative_to(notes) for path in paths):
        raise ValueError('Research inputs must be published files below this topic notes directory')


def polygon_vertex_height_conditions(problem,data,tau='61/1000'):
    """Sampled height inserted into exact necessary formulas, not a certificate."""
    out=height_conditions(problem,data,tau)
    reach=Q(tau);B=problem.port.B_exact;w=problem.port.width_exact
    R=problem.tail.outer_exact;rc=problem.seed.cut_radius_exact;gap=abs(B-R)
    h=problem.port.side*float(data['center'][-1]);delta=h-float(w)
    denominator=2*max(float(gap),abs(delta))
    bound=(float(gap*gap)+delta*delta)/denominator if denominator else None
    # Inverting both normal-chord inequalities removes the small vertical
    # root even without a separate held-disk witness.  Keep both height
    # branches whenever h>0 alone does not exclude the lower one.
    if gap<reach:
        radicand=reach*reach-gap*gap
        gap_formula=f'{reach}+sqrt({radicand})'
        gap_bound=float(reach)+np.sqrt(float(radicand))
        forced_upper=(w<=reach or (w-reach)**2<=radicand)
        reason='both normals exclude the small vertical root when d<tau'
    elif gap<2*reach:
        radicand=gap*(2*reach-gap)
        gap_formula=f'sqrt({radicand})';gap_bound=np.sqrt(float(radicand))
        forced_upper=(w*w<=radicand)
        reason='horizontal normal at the core requires Delta^2>=d*(2*tau-d)'
    else:
        gap_formula='0';gap_bound=0.;forced_upper=(w==0)
        reason='d>=2*tau gives no nonzero height-gap requirement from these two points'
    selected_exact=f'{w}+({gap_formula})' if forced_upper else None
    selected_float=float(w)+gap_bound if forced_upper else None
    out.update({
        'polygon_vertex_witness':{'core_point':'(0,B,w)','cap_point':'(0,R,h)',
            'core_normal':'horizontal y direction','cap_normal':'vertical z direction',
            'reason_cap_vertex_is_flat':'theta=pi/2 is a common vertex of the j*pi/3 six-cap pattern',
            'B_exact':str(B),'R_exact':str(R),'horizontal_gap_exact':str(gap),
            'normal_chord_upper_formula':'(d^2+(h-w)^2)/(2*max(d,abs(h-w)))',
            'evaluated_normal_chord_upper':bound,
            'evaluated_upper_minus_target':None if bound is None else bound-float(reach)},
        'standard_positive_upper_cap_necessary_height_formula':selected_exact,
        'standard_positive_upper_cap_height_threshold_evaluated':selected_float,
        'height_threshold_branch_reason':reason,
        'general_necessary_abs_height_gap_formula':gap_formula,
        'general_necessary_abs_height_gap_evaluated':gap_bound,
        'general_abs_height_gap_margin_evaluated':abs(delta)-gap_bound,
        'both_height_branches_before_assuming_positive_h':['h <= w-L','h >= w+L'],
        'positive_h_forces_upper_branch_because_L_at_least_w':bool(forced_upper),
        'upper_branch_height_threshold_if_h_at_least_w':float(w)+gap_bound,
        'standard_positive_cap_height_margin_evaluated':
            None if selected_float is None else h-selected_float,
        'height_constraint_is_not_added_to_this_audit_only_objective':True,
        'necessary_formulas_assume_a_complete_C2_embedding_with_reach_at_least_target':True,
        'current_approximate_candidate_is_not_claimed_such_an_embedding':True,
        'no_continuous_height_integral_bound_or_strict_reach_exclusion_claimed':True})
    return out


def region_audit(problem,data):
    t,theta=data['radial'],data['theta'];values=point_values(problem,data)
    tc=problem.entry.left;end=tc+problem.entry.length;patch=problem.source.support_start
    regions={'open_core':(0.,tc),'entry_repair_support':(tc,end),
             'body_after_entry_before_patch':(end,patch),
             'natural_cap_patch':(patch,problem.source.active_end),
             'open_cap':(problem.source.active_end,problem.seed.length)}
    answer={}
    for name,(left,right) in regions.items():
        use=(t>=left)&(t<=right)
        if not np.any(use):
            answer[name]={'empty_sample_region':True,'interval':[left,right]};continue
        answer[name]={'interval':[left,right],'closed_sample_intervals_may_share_boundary_rows':True,
            'radial_sample_count':int(np.count_nonzero(use))}
        for key in ['metric_operator_error','E_minus_one','F_over_a',
                    'principal_curvature_absolute','area','signed_side_height_minus_core_width']:
            kind='min' if key in ['area','signed_side_height_minus_core_width'] else 'abs' if key in ['E_minus_one','F_over_a'] else 'max'
            answer[name][key]=extremum(values[key][use],t[use],theta,kind)
    return {'regions':answer,'all_values_are_sampled_only':True}


def run_audit(base,state,out,*,entry_length='81/500',entry_mean_nodes=1024,
              uniform_panels=120,primitive_order=8,refined_panels=240,refined_order=12,
              radial_nodes=121,angular_nodes=384,source_receipt=None,artificial=False):
    started=time.monotonic();state=np.asarray(state,float).copy();state.setflags(write=False)
    old=FixedPrimitiveProblem(base,uniform_panels,primitive_order)
    new=EntryRepairProblem(base,state,entry_length,entry_mean_nodes=entry_mean_nodes,
        uniform_panels=uniform_panels,primitive_order=primitive_order)
    old_metric=base.metric_model(state);new_metric=new.metric_model(state)
    if old_metric!=new_metric:raise ArithmeticError('entry repair changed the complete frozen metric record')
    if base.port.identity!=new.port.identity:raise ArithmeticError('entry repair changed the core')
    if base.tail.identity!=new.tail.identity:raise ArithmeticError('entry repair changed the physical cap')
    physical=new.identity(state)
    answer={'schema':'paired-entry-selected-fixed-g-initial-only-audit-v1',
        'source_receipt':source_receipt,'source_files_sha256':implementation_hashes(),
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),
        'old_corrected_evaluator_state':state_record(old,state),
        'new_entry_state':state_record(new,state),
        'raw_parameter_coefficients_bitwise_unchanged':True,
        'complete_frozen_metric_record_unchanged':True,'core_and_cap_physical_definitions_unchanged':True,
        'immutable_original_c0_anchor_not_replaced_by_selected_state':True,
        'new_entry_field_not_claimed_equal_to_old_selected_field':True,
        'entry_support_exact':{'left':str(new.entry.left_exact),'length':str(new.entry.length_exact),
            'plateau_end':str(new.entry.left_exact+new.entry.length_exact/3),
            'right':str(new.entry.left_exact+new.entry.length_exact)},
        'entry_mean_coefficients_evaluated':new.entry.mean_data(),
        'configuration':{'entry_mean_nodes':int(entry_mean_nodes),'uniform_panels':int(uniform_panels),
            'primitive_order':int(primitive_order),'refined_panels':int(refined_panels),
            'refined_order':int(refined_order),'radial_nodes':int(radial_nodes),
            'angular_nodes':int(angular_nodes)},
        'artificial_inputs_only':bool(artificial),'optimization_performed':False,'nonlinear_solve_count':0,
        'parameter_step_applied':False,'geometry_change_is_only_the_declared_new_entry_representation':True,
        'task_complete':False,'embedding_proved':False,'whole_surface_reach_proved':False}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-started
        answer['peak_rss_kib_linux']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        atomic_save(out,answer)
    save('validated-selected-input-and-new-identity')
    coarse_t=np.asarray(base.source.radial,float);coarse_theta=np.asarray(base.source.theta,float)
    old_coarse=old.geometry(state,coarse_t,coarse_theta,primitive_order)
    new_coarse=new.geometry(state,coarse_t,coarse_theta,primitive_order)
    answer['old_corrected_coarse_audit']=sampled_audit(old,state,old_coarse)
    answer['new_entry_coarse_audit']=sampled_audit(new,state,new_coarse)
    answer['new_coarse_region_audit']=region_audit(new,new_coarse)
    answer['old_new_coarse_position_two_jet_differences']=position_difference(old_coarse,new_coarse)
    answer['new_coarse_height_conditions']=polygon_vertex_height_conditions(new,new_coarse)
    save('both-coarse-initial-states-saved')
    t=np.linspace(0,base.seed.length,int(radial_nodes));theta=np.arange(int(angular_nodes))*2*np.pi/int(angular_nodes)
    if len(t)<3 or len(theta)<4 or len(theta)%4:raise ValueError('valid radial and uniform complete angle grids required')
    before=old.geometry(state,t,theta,primitive_order);after=new.geometry(state,t,theta,primitive_order)
    answer['old_corrected_fine_audit']=sampled_audit(old,state,before)
    answer['new_entry_fine_audit']=sampled_audit(new,state,after)
    answer['new_fine_radial_distribution']=radial_distribution(new,after)
    answer['new_fine_region_audit']=region_audit(new,after)
    answer['old_new_fine_position_two_jet_differences']=position_difference(before,after)
    answer['old_corrected_fine_height_conditions']=polygon_vertex_height_conditions(new,before)
    answer['new_fine_height_conditions']=polygon_vertex_height_conditions(new,after)
    outside=t>=new.entry.left+new.entry.length
    shift=after['X'][outside]-before['X'][outside]
    common_shift=float(shift[0,0,2]);shift[...,2]-=common_shift
    answer['outside_entry_change']={
        'sampled_nonposition_derivative_differences':{key:float(np.max(abs(after[key][outside]-before[key][outside]))) for key in JETS[1:]},
        'single_common_vertical_translation_evaluated':common_shift,
        'position_after_removing_that_translation_max_difference':float(np.max(abs(shift))),
        'outside_entry_metric_and_curvature_not_improved_by_local_repair':True}
    save('same-grid-fine-initial-comparison-saved')
    sparse=np.array(sorted(set([0.,new.entry.left,new.entry.left+new.entry.length/3,
        new.entry.left+new.entry.length,base.height_basis.right,base.seed.length])))
    union=np.unique(np.r_[t,sparse]);short=new.geometry(state,sparse,theta,primitive_order)
    complete=new.geometry(state,union,theta,primitive_order);indices=np.searchsorted(union,sparse)
    answer['new_complete_interface_chart_audit']=sampled_audit(new,state,complete)
    answer['new_sparse_complete_query_position_two_jet_differences']={key:
        float(np.max(abs(short[key]-complete[key][indices]))) for key in JETS}
    save('query-independent-complete-ports-saved')
    theta2=np.arange(2*len(theta))*np.pi/len(theta)
    doubled=new.geometry(state,t,theta2,primitive_order)
    answer['new_entry_doubled_angle_audit']=sampled_audit(new,state,doubled)
    answer['new_doubled_angle_region_audit']=region_audit(new,doubled)
    answer['new_doubled_angle_height_conditions']=polygon_vertex_height_conditions(new,doubled)
    answer['same_state_Pi_angle_doubling']={
        'physical_identity_sha256':digest(physical),'angular_nodes':[len(theta),len(theta2)],
        'position_jet_differences':{key:float(np.max(np.linalg.norm(after[key]-doubled[key][:,::2],axis=-1))) for key in JETS},
        'center_height_difference':float(after['center'][-1]-doubled['center'][-1]),
        'finite_differences_not_continuous_error_bounds':True}
    save('same-state-angle-refinement-saved')
    refinements=[('entry_exact_mean_refinement',{'entry_mean_nodes':2*int(entry_mean_nodes)}),
        ('fixed_primitive_GL_order_refinement',{'primitive_order':int(refined_order)}),
        ('fixed_primitive_partition_refinement',{'uniform_panels':int(refined_panels)}),
        ('fixed_original_height_mean_refinement',{'height_angular_nodes':2*base.height_angular_nodes}),
        ('infinite_heat_evaluation_refinement',{'heat_order':2*base.source.heat_order})]
    for name,changes in refinements:
        variant=new.evaluation_variant(state,**changes)
        if variant.identity(state)!=physical:raise ArithmeticError('evaluation variant changed the physical state')
        answer[name]=compare_evaluation(new,state,variant,t,theta,primitive_order)
        answer[name]['entry_mean_coefficients_evaluated']=variant.entry.mean_data()
        save(name+'-saved')
        del variant
    if not np.array_equal(state,np.asarray(answer['new_entry_state']['parameter_coefficients_binary64'])):
        raise ArithmeticError('read-only audit altered a coefficient')
    save('complete-initial-only-audit')
    return answer


def developer_check():
    report,raw=artificial_carrier();base,state,receipt=load_selected_report(report,raw)
    with tempfile.TemporaryDirectory(prefix='entry-repair-artificial-',dir='/dev/shm') as directory:
        out=Path(directory)/'audit.json'
        answer=run_audit(base,state,out,entry_length='3/25',entry_mean_nodes=32,
            uniform_panels=8,primitive_order=3,refined_panels=16,refined_order=4,
            radial_nodes=9,angular_nodes=16,source_receipt=receipt,artificial=True)
        saved=json.loads(out.read_text())
    no_step=(answer['nonlinear_solve_count']==0 and not answer['optimization_performed']
             and not answer['parameter_step_applied'])
    final=answer['status']=='complete-initial-only-audit'
    same_g=answer['complete_frozen_metric_record_unchanged']
    query=max(answer['new_sparse_complete_query_position_two_jet_differences'].values())
    outside=answer['outside_entry_change']
    all_refined=all(answer[key]['same_canonical_identity_and_coefficients'] for key in [
        'entry_exact_mean_refinement','fixed_primitive_GL_order_refinement',
        'fixed_primitive_partition_refinement','fixed_original_height_mean_refinement',
        'infinite_heat_evaluation_refinement'])
    try:
        require_public_actions('true','another/repository',[]);wrong_repository_rejected=False
    except ValueError:wrong_repository_rejected=True
    try:
        require_public_actions('true','Rogerhu12/math-research-public',['/dev/shm/outside-topic.json'])
        outside_topic_rejected=False
    except ValueError:outside_topic_rejected=True
    return {'schema':'paired-entry-audit-artificial-main-check-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'complete_research_main_path_executed_on_artificial_carrier':True,
        'status':answer['status'],'JSON_roundtrip_unchanged':saved==answer,
        'no_optimizer_or_parameter_step':no_step,'complete_frozen_g_unchanged':same_g,
        'query_independent_position_two_jet_difference':query,
        'all_five_isolated_evaluation_refinements_preserve_physical_identity':all_refined,
        'wrong_repository_rejected':wrong_repository_rejected,'outside_topic_input_rejected':outside_topic_rejected,
        'outside_entry_nonposition_difference_max':max(outside['sampled_nonposition_derivative_differences'].values()),
        'outside_entry_one_vertical_translation_error':outside['position_after_removing_that_translation_max_difference'],
        'passed':bool(final and saved==answer and no_step and same_g and all_refined and query<1e-10
            and wrong_repository_rejected and outside_topic_rejected)}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check-only',action='store_true')
    p.add_argument('--input',type=Path);p.add_argument('--anchor-input',type=Path)
    p.add_argument('--expected-input-sha256');p.add_argument('--expected-anchor-sha256')
    p.add_argument('--entry-length',default='81/500');p.add_argument('--entry-mean-nodes',type=int,default=1024)
    p.add_argument('--uniform-panels',type=int,default=120);p.add_argument('--primitive-order',type=int,default=8)
    p.add_argument('--refined-panels',type=int,default=240);p.add_argument('--refined-order',type=int,default=12)
    p.add_argument('--radial-nodes',type=int,default=121);p.add_argument('--angular-nodes',type=int,default=384)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    if args.check_only:
        answer=developer_check();answer['source_files_sha256']=implementation_hashes();atomic_save(args.out,answer)
        print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
        if not answer['passed']:raise SystemExit(1)
        return
    if args.input is None or args.anchor_input is None:raise SystemExit('--input and --anchor-input are required')
    require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
        [args.input,args.anchor_input])
    selected=args.input.read_bytes();anchor=args.anchor_input.read_bytes()
    for data,expected,label in [(selected,args.expected_input_sha256,'selected report'),
                                (anchor,args.expected_anchor_sha256,'original c0 report')]:
        if expected and hashlib.sha256(data).hexdigest()!=expected:raise ValueError(label+' byte SHA mismatch')
    base,state,receipt=load_selected_report(json.loads(selected),anchor)
    receipt.update(selected_report_sha256=hashlib.sha256(selected).hexdigest(),
        original_c0_report_sha256=hashlib.sha256(anchor).hexdigest())
    answer=run_audit(base,state,args.out,entry_length=args.entry_length,entry_mean_nodes=args.entry_mean_nodes,
        uniform_panels=args.uniform_panels,primitive_order=args.primitive_order,
        refined_panels=args.refined_panels,refined_order=args.refined_order,
        radial_nodes=args.radial_nodes,angular_nodes=args.angular_nodes,source_receipt=receipt)
    print(json.dumps({'out':str(args.out),'status':answer['status'],'optimization_performed':False}),flush=True)


if __name__=='__main__':main()

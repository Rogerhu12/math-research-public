#!/usr/bin/env python3
"""Public-Actions finite initial comparisons of two shorter entry models.

The old selected report and its original c0 carrier are replayed strictly.
The completed long-entry audit is replayed by identity; its geometry is not
reevaluated here.
Each new model receives at most one proposed height coefficient replacement.
No iterative optimizer is called. --check-only uses artificial carriers only.
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
from frame_fixed_height_primitive_audit import artificial_carrier,load_selected_report
from frame_entry_paired_repair import EntryRepairProblem
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_entry_paired_repair_audit import (
    implementation_hashes as entry_audit_hashes,require_public_actions,
    polygon_vertex_height_conditions,region_audit,JETS)
from frame_fixed_height_primitive import fixed_partition
from frame_independent_height import IndependentHeightProblem
from frame_independent_height_solve import (
    state_record,sampled_audit,radial_distribution,point_values,objective_cost,extremum)
from frame_height_feasible_initializer import choose_height_coefficient


SCHEMA='short-entry-paired-bounded-one-height-step-audit-v1'


def implementation_hashes():
    answer=entry_audit_hashes()
    for name in ['frame_entry_bounded_height.py','frame_height_feasible_initializer.py',Path(__file__).name]:
        answer[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return answer


def read_input(path,expected_decoded_sha256):
    stored=Path(path).read_bytes()
    compressed=stored.startswith(b'\x1f\x8b')
    decoded=gzip.decompress(stored) if compressed else stored
    actual=hashlib.sha256(decoded).hexdigest()
    if not expected_decoded_sha256 or actual!=expected_decoded_sha256:
        raise ValueError('required decoded byte SHA256 mismatch: '+str(path))
    return json.loads(decoded),decoded,{
        'path':str(path),'stored_bytes':len(stored),'stored_sha256':hashlib.sha256(stored).hexdigest(),
        'gzip_storage':compressed,'decoded_bytes':len(decoded),'decoded_sha256':actual}


def replay_prior_entry(prior,base,state,selected_sha,anchor_sha):
    if (prior.get('schema')!='paired-entry-selected-fixed-g-initial-only-audit-v1'
            or prior.get('status')!='complete-initial-only-audit'):
        raise ValueError('a completed published paired-entry initial audit is required')
    if prior.get('source_files_sha256')!=entry_audit_hashes():
        raise ValueError('the completed entry audit uses different frozen implementations')
    receipt=prior['source_receipt']
    if (receipt.get('selected_report_sha256')!=selected_sha
            or receipt.get('original_c0_report_sha256')!=anchor_sha):
        raise ValueError('prior entry audit is not bound to these two exact input byte streams')
    if (prior.get('optimization_performed') or prior.get('parameter_step_applied')
            or prior.get('nonlinear_solve_count')!=0
            or not prior.get('raw_parameter_coefficients_bitwise_unchanged')
            or not prior.get('complete_frozen_metric_record_unchanged')):
        raise ValueError('prior entry audit is not the unchanged selected-coefficient initial audit')
    cfg=prior['configuration']
    previous=EntryRepairProblem(base,state,prior['entry_support_exact']['length'],
        entry_mean_nodes=cfg['entry_mean_nodes'],uniform_panels=cfg['uniform_panels'],
        primitive_order=cfg['primitive_order'])
    if state_record(previous,state)!=prior['new_entry_state']:
        raise ValueError('prior entry full state/space/layout/metric/evaluation replay mismatch')
    if state_record(previous.original_primitive,state)!=prior['old_corrected_evaluator_state']:
        raise ValueError('prior corrected original-state replay mismatch')
    summary={key:prior[key] for key in [
        'entry_support_exact','entry_mean_coefficients_evaluated','configuration']}
    for key in ['old_corrected_fine_audit','new_entry_fine_audit','new_entry_doubled_angle_audit']:
        if key in prior:
            value=prior[key]
            summary[key]={name:value[name] for name in [
                'objective_cost','extrema','center_height_first_last','center_speed_min_max_sample']}
    if 'outside_entry_change' in prior:summary['outside_entry_change']=prior['outside_entry_change']
    return {'complete_prior_state_replayed_without_geometry_evaluation':True,
        'prior_metric_record_equals_selected':previous.metric_model(state)==base.metric_model(state),
        'prior_physical_state_sha256':digest(previous.identity(state)),
        'prior_length_exact':str(previous.entry.length_exact),
        'prior_summary_read_from_published_output_not_recomputed':summary}


def build_grid(problem,radial_nodes,collar_subdivisions,angular_nodes):
    nr,nc,nt=map(int,[radial_nodes,collar_subdivisions,angular_nodes])
    if nr<5 or nc<6 or nc%3 or nt<8 or nt%4:
        raise ValueError('nr>=5, collar subdivisions positive multiple of3 >=6, nt>=8 multiple of4 required')
    partition=fixed_partition(problem,nr-1)
    nodes=set(map(Q,partition['nodes_exact']))
    tc=problem.entry.left_exact;ell=problem.entry.length_exact
    collar=[tc+ell*Q(j,nc) for j in range(nc+1)]
    nodes.update(collar)
    nodes.update(map(Q,problem.body_metric.family_definition['clamped_knots_exact']))
    nodes.update(map(Q,problem.height_basis.original.identity['clamped_knots_exact']))
    points=sorted(nodes)
    if points[0]!=0 or points[-1]!=problem.seed.length_exact:
        raise ArithmeticError('the exact audit grid must contain both physical endpoints')
    radial=np.array([float(x) for x in points])
    if np.any(np.diff(radial)<=0):raise ArithmeticError('binary64 audit nodes are not strictly increasing')
    theta=np.arange(nt)*2*np.pi/nt
    record={'schema':'fixed-uniform-structural-and-relative-entry-audit-grid-v1',
        'radial_nodes_exact':[str(x) for x in points],
        'base_uniform_panel_count':nr-1,'structural_partition':partition,
        'collar_nodes_exact':[str(x) for x in collar],
        'collar_subdivisions':nc,'angular_nodes':nt,
        'angular_definition':'theta_j=2*pi*j/N, j=0,...,N-1',
        'objective_weight':'uniform over these sampled radial and angular rows',
        'different_radial_grids_do_not_define_comparable_sampled_mean_costs':True}
    record['definition_sha256']=digest(record)
    return radial,theta,record


def mirror_diagnostics(problem,data,tau):
    X,U,T=(data[key] for key in ['X','Xs','T'])
    W=np.cross(U,T);norm=np.linalg.norm(W,axis=-1)
    numerator=abs(X[...,2])*norm;denominator=abs(W[...,2])
    regular=np.isfinite(norm)&(norm>0)
    finite_gate=regular&(denominator>0)
    radius=np.full_like(norm,np.inf)
    np.divide(numerator,denominator,out=radius,where=finite_gate)
    signed=problem.port.side*X[...,2]
    finite_radius=np.where(finite_gate,radius,np.nan)
    return {'same_material_coordinate_reflection_pair_normal_chord_upper':
                extremum(finite_radius,data['radial'],data['theta'],'min'),
        'zero_normal_z_pair_gives_no_finite_bound_count':int(np.count_nonzero(regular&(denominator==0))),
        'nonregular_sample_count':int(np.count_nonzero(~regular)),
        'chosen_upper_branch_signed_height_minimum':extremum(signed,data['radial'],data['theta'],'min'),
        'normal_chord_target_evaluated':float(tau),
        'formula':'abs(z)*norm(Xs cross T)/abs((Xs cross T)_z)',
        'requires_distinct_mirrored_material_points_and_a_complete_embedding':True,
        'noncentral_z_zero_points_would_be_coincident_under_this_mirror':True,
        'positive_signed_z_is_the_selected_upper_branch_condition':True,
        'sampled_diagnostic_not_a_continuous_reach_certificate':True}


def audit_data(problem,state,data,tau,with_rows=True):
    result={'full':sampled_audit(problem,state,data),
        'regions':region_audit(problem,data),
        'height_conditions':polygon_vertex_height_conditions(problem,data,str(tau)),
        'mirror_pair_samples':mirror_diagnostics(problem,data,tau)}
    if with_rows:result['radial_distribution']=radial_distribution(problem,data)
    return result


def compare_data(problem,before,variant,after,state,*,name,theta_stride=1):
    if problem.identity(state)!=variant.identity(state):
        raise ArithmeticError('evaluation comparison changed the canonical physical state')
    if not np.array_equal(before['radial'],after['radial']):
        raise ValueError('evaluation comparisons require identical radial points')
    second={key:after[key][:,::theta_stride] for key in JETS}
    positions={key:float(np.max(np.linalg.norm(before[key]-second[key],axis=-1))) for key in JETS}
    v0,v1=point_values(problem,before),point_values(variant,after)
    metric={key:float(np.max(abs(v0[key]-v1[key][:,::theta_stride])))
            for key in ['E_minus_one','F_over_a','metric_operator_error']}
    return {'name':name,'same_canonical_state_and_exact_coefficients':True,
        'physical_identity_sha256':digest(problem.identity(state)),
        'evaluation_before':problem.evaluation_definition(),'evaluation_after':variant.evaluation_definition(),
        'angular_nodes':[len(before['theta']),len(after['theta'])],
        'position_jet_differences':positions,'direct_metric_differences':metric,
        'center_height_difference':float(after['center'][-1]-before['center'][-1]),
        'center_speed_differences':{key:float(np.max(abs(before['height'][key]-after['height'][key])))
                                    for key in ['b','b_s','b_ss']},
        'same_state_objective_costs':[objective_cost(problem,before),objective_cost(variant,after)],
        'no_parameter_step_or_reoptimization_in_this_comparison':True,
        'finite_evaluation_differences_are_not_error_enclosures':True}


def height_column_record(problem,index):
    count=problem.height_basis.count
    if not 0<=index<count:raise ValueError('invalid height coefficient column')
    knots=list(map(Q,problem.height_basis.original.identity['clamped_knots_exact']))
    full=index+3;left,right=knots[full],knots[full+6]
    entry_end=problem.entry.left_exact+problem.entry.length_exact
    preserved=left>=entry_end
    raw_integral=(right-left)/6
    return {'local_height_column':index,'original_full_quintic_B_spline_index':full,
        'support_left_exact':str(left),'support_right_exact':str(right),
        'entry_end_exact':str(entry_end),'support_is_outside_entry':preserved,
        'original_quintic_integral_exact':str(raw_integral),
        'weighted_column_equals_original_everywhere':preserved,
        'weighted_integral_exact_if_unchanged':str(raw_integral) if preserved else None}


def make_height_proposal(problem,state,data,cfg,*,artificial=False,override_minimum=None):
    index=int(cfg['height_column'])
    column_info=height_column_record(problem,index)
    if not artificial and not column_info['support_is_outside_entry']:
        raise ValueError('the selected research height column must preserve the whole entry collar')
    C=problem.height_basis.evaluate(data['radial'])[:,index]
    I=problem.height_basis.integral(data['radial'])[:,index]
    Cprime=problem.height_basis.evaluate(data['radial'],1)[:,index]
    h=problem.port.side*float(data['center'][-1])
    gain=problem.port.side*float(I[-1])
    conditions=polygon_vertex_height_conditions(problem,data,cfg['tau'])
    threshold=conditions['upper_branch_height_threshold_if_h_at_least_w']
    minimum=threshold+float(Q(cfg['height_margin']))
    policy='chosen upper branch of exact R66 formula plus declared margin'
    ball=problem.ball_radius
    signed=None if cfg['minimum_signed_height'] is None else float(Q(cfg['minimum_signed_height']))
    if override_minimum is not None:
        if not artificial:raise ValueError('an artificial threshold override is forbidden for research')
        minimum=float(override_minimum);ball=None;signed=None
        policy='artificial full-path check only; not a research height threshold'
    current=float(state[problem.slices['height'].start+index])
    proposal=choose_height_coefficient(data,C,I,current_coefficient=current,
        coefficient_bounds=tuple(cfg['height_coefficient_bounds']),cap_height=h,cap_height_gain=gain,
        minimum_cap_height=minimum,side=problem.port.side,ball_radius=ball,
        minimum_signed_height=signed)
    proposal['column_definition']=column_info
    proposal['height_target_policy']={'selection':policy,'tau_exact':cfg['tau'],
        'R66_upper_branch_threshold_evaluated':threshold,
        'positive_h_forces_this_branch':conditions['positive_h_forces_upper_branch_because_L_at_least_w'],
        'margin_exact':cfg['height_margin'],'target_passed_to_helper':minimum,
        'exact_formula_is_used_but_current_height_integral_has_no_interval_enclosure':True}
    proposal['strip_constraint_unchanged_and_not_part_of_height_interval']=True
    proposal['original_full_smooth_cost_is_checked_after_rebuilding_geometry']=True
    return proposal,(C,I,Cprime)


def apply_height_proposal(problem,state,data,proposal,columns,order):
    selected=proposal.get('selected')
    if selected is None:return None
    index=proposal['column_definition']['local_height_column']
    location=problem.slices['height'].start+index
    current=float(state[location]);new=float(selected['new_coefficient']['binary64'])
    delta=Q.from_float(new)-Q.from_float(current)
    if str(delta)!=selected['exact_coefficient_difference']:
        raise ValueError('one-column exact binary64 difference does not match the helper proposal')
    changed=np.asarray(state,float).copy();changed[location]=new
    other=np.ones(len(state),bool);other[location]=False
    if not np.array_equal(changed[other],state[other]):
        raise ArithmeticError('a supposedly one-column update changed another coefficient')
    if problem.metric_model(changed)!=problem.metric_model(state):
        raise ArithmeticError('one height coefficient update changed the fixed metric')
    after=problem.geometry(changed,data['radial'],data['theta'],order)
    C,I,Cprime=columns;difference=float(delta)
    expected={key:np.array(data[key],copy=True) for key in JETS}
    expected['X'][...,2]+=difference*I[:,None]
    expected['Xs'][...,2]+=difference*C[:,None]
    expected['Xss'][...,2]+=difference*Cprime[:,None]
    errors={key:float(np.max(np.linalg.norm(after[key]-expected[key],axis=-1))) for key in JETS}
    record={'exact_new_coefficient':str(Q.from_float(new)),'exact_difference':str(delta),
        'only_named_height_column_changed':True,'complete_frozen_metric_unchanged':True,
        'T_field_bitwise_unchanged':bool(np.array_equal(data['T'],after['T'])),
        'reconstructed_six_position_jets_vs_finite_change_formulas':errors,
        'cap_height_from_full_reconstruction':problem.port.side*float(after['center'][-1]),
        'cap_height_predicted_by_helper':proposal['selected_height_predicted'],
        'position_field_has_really_changed_unless_difference_is_zero':bool(delta),
        'all_remaining_gates_are_reaudited_not_inherited':True}
    if not record['T_field_bitwise_unchanged']:raise ArithmeticError('height-only update changed T')
    changed.setflags(write=False)
    return changed,after,record


def default_configuration():
    return {'entry_length':'81/1000','entry_mean_nodes':1024,
        'uniform_panels':120,'primitive_order':8,'refined_primitive_order':12,
        'radial_nodes':121,'angular_nodes':384,'collar_subdivisions':24,
        'height_column':4,'height_coefficient_bounds':[-1.,1.],
        'tau':'61/1000','height_margin':'1/1000','minimum_signed_height':'0',
        'paired_integrals_reused_from_published_comparison_not_claimed_certified':True}



def summary_path(out):
    path=Path(out)
    return path.with_name(path.stem+'-summary.json')


def evaluation_summary(value):
    answer={key:value[key] for key in [
        'source_GH_order','height_mean_angular_nodes','entry_mean_angular_nodes'] if key in value}
    primitive=value.get('query_independent_height_primitive')
    if primitive is None:
        primitive=value.get('original_b0_evaluator',{}).get('query_independent_height_primitive')
    if primitive is not None:
        answer['height_primitive_GL_order']=primitive.get('gauss_order_per_full_or_partial_panel')
        partition=primitive.get('partition',{})
        answer['height_primitive_fixed_partition_nodes']=len(partition.get('nodes_exact',[]))
        answer['height_primitive_partition_definition_sha256']=digest(partition)
    answer['full_evaluation_definition_sha256']=digest(value)
    return answer


def compact_state(record):
    physical=record['canonical_physical_state']
    exact=record['exact_parameter_coefficients']
    binary=np.asarray(record['parameter_coefficients_binary64'],float)
    blocks={}
    for name,(left,right) in record['parameter_slices'].items():
        values=binary[left:right]
        blocks[name]={'count':int(len(values)),
            'exact_rational_vector_sha256':digest(exact[name]),
            'minimum':float(np.min(values)) if len(values) else None,
            'maximum':float(np.max(values)) if len(values) else None,
            'euclidean_norm_evaluated':float(np.linalg.norm(values))}
    return {'physical_state_sha256':record['canonical_physical_state_sha256'],
        'physical_field_schema':physical['schema'],
        'T_space_schema':physical['source_T_scalar_family'].get('schema'),
        'height_base_schema':physical['height_base_definition'].get('schema'),
        'metric_definition_sha256':record['metric_model']['mathematical_definition_sha256'],
        'core_identity_sha256':digest(physical['core_identity']),
        'physical_cap_identity_sha256':digest(physical['tail_identity']),
        'parameter_count':int(len(binary)),'parameter_blocks':blocks,
        'all_exact_parameter_blocks_sha256':digest(exact),
        'evaluation':evaluation_summary(record['evaluation_definition'])}


def compact_audit(value):
    return {key:value[key] for key in ['full','regions','height_conditions','mirror_pair_samples'] if key in value}


def compact_comparison(value):
    answer={key:value[key] for key in [
        'name','same_canonical_state_and_exact_coefficients','physical_identity_sha256',
        'angular_nodes','position_jet_differences','direct_metric_differences',
        'center_height_difference','center_speed_differences','same_state_objective_costs',
        'no_parameter_step_or_reoptimization_in_this_comparison',
        'finite_evaluation_differences_are_not_error_enclosures'] if key in value}
    answer['evaluation_before']=evaluation_summary(value['evaluation_before'])
    answer['evaluation_after']=evaluation_summary(value['evaluation_after'])
    return answer


def compact_proposal(value):
    keys=['schema','status','current_coefficient','coefficient_bounds','sample_shape','normalization',
        'quartic_coefficients_ascending','cap_height_input','cap_height_gain_input',
        'minimum_cap_height_input','minimum_signed_height_input','ball_radius_input','side','interval',
        'selected','selected_height_predicted','column_definition','height_target_policy',
        'numerical_derivative_roots','continuous_feasibility_or_global_minimum_certified',
        'original_smooth_shape_objective_is_not_this_quartic',
        'strip_constraint_unchanged_and_not_part_of_height_interval',
        'original_full_smooth_cost_is_checked_after_rebuilding_geometry']
    answer={key:value[key] for key in keys if key in value}
    table=value.get('candidate_table',[])
    answer['candidate_count']=len(table)
    answer['sample_feasible_candidate_count']=sum(bool(x['sample_feasible_in_current_arithmetic']) for x in table)
    return answer


def scientific_summary(answer,out):
    """Progress/diagnostic view; the separately preserved full report binds it."""
    receipt=answer.get('source_receipt',{})
    complete=Path(out).read_bytes()
    result={'schema':'short-entry-bounded-scientific-checkpoint-summary-v1',
        'full_report_schema':answer['schema'],'status':answer['status'],
        'elapsed_seconds':answer['elapsed_seconds'],'peak_rss_kib_linux':answer['peak_rss_kib_linux'],
        'full_report':{'path':str(out),'bytes':len(complete),'sha256':hashlib.sha256(complete).hexdigest()},
        'github_sha':answer.get('github_sha'),'github_run_id':answer.get('github_run_id'),
        'github_repository':answer.get('github_repository'),
        'source_files_sha256':answer['source_files_sha256'],
        'input_bindings':{key:receipt[key] for key in [
            'selected_report_sha256','original_c0_report_sha256','selected_physical_state_sha256',
            'selected_metric_definition_sha256','source_parameter_count','frozen_parameter_count',
            'exact_input_storage'] if key in receipt},
        'configuration':answer['configuration'],
        'fixed_metric_definition_sha256':answer['selected_original_fixed_metric']['mathematical_definition_sha256'],
        'source_state':compact_state(answer['source_exact_state']),
        'prior_completed_entry_replay':answer['prior_completed_entry_replay'],
        'sampling':{'definition_sha256':answer['sampling_grid']['definition_sha256'],
            'radial_nodes':len(answer['sampling_grid']['radial_nodes_exact']),
            'angular_nodes':answer['sampling_grid']['angular_nodes'],
            'collar_subdivisions':answer['sampling_grid']['collar_subdivisions'],
            'collar_nodes_exact':answer['sampling_grid']['collar_nodes_exact'],
            'objective_weight':answer['sampling_grid']['objective_weight']},
        'unrepaired_selected_same_grid_audit':answer.get('unrepaired_selected_same_grid_audit'),
        'cases':{},'iterative_nonlinear_solve_count':answer['iterative_nonlinear_solve_count'],
        'multivariate_optimization_performed':answer['multivariate_optimization_performed'],
        'finite_one_column_candidate_selections':answer['finite_one_column_candidate_selections'],
        'nonzero_parameter_steps_applied':answer['nonzero_parameter_steps_applied'],
        'artificial_inputs_only':answer['artificial_inputs_only'],
        'sampled_diagnostics_not_continuous_certificates':True,
        'full_canonical_states_and_radial_distributions_preserved_in_bound_full_report':True,
        'task_complete':False,'embedding_proved':False,'whole_surface_reach_proved':False}
    if 'source_original_c0_exact' in receipt:
        result['input_bindings']['immutable_c0_exact_vector_sha256']=digest(receipt['source_original_c0_exact'])
    for name,case in answer['cases'].items():
        value={}
        for key in ['initial_state','final_state']:
            if key in case:value[key]=compact_state(case[key])
        for key in ['initial_audit','final_audit','doubled_angle_final_audit']:
            if key in case:value[key]=compact_audit(case[key])
        if 'height_proposal' in case:value['height_proposal']=compact_proposal(case['height_proposal'])
        for key in ['height_step_status','height_step_record','same_grid_costs_before_after',
                    'query_independent_interface_position_two_jet_difference',
                    'unchanged_integrals_not_repeated','no_iteration_after_this_single_proposal',
                    'artificial_unreachable_height_proposal_status']:
            if key in case:value[key]=case[key]
        for key in ['same_state_Pi_angle_doubling','bounded_height_angular_mean',
                    'bounded_fixed_primitive_GL_order']:
            if key in case:value[key]=compact_comparison(case[key])
        result['cases'][name]=value
    return result


def run_audit(base,state,prior,receipt,out,cfg,*,artificial=False,artificial_step_test=False):
    started=time.monotonic();state=np.asarray(state,float).copy();state.setflags(write=False)
    if Q(cfg['entry_length'])>=Q(prior['prior_length_exact']):
        raise ValueError('the new comparison must use one strictly shorter declared collar')
    paired=EntryRepairProblem(base,state,cfg['entry_length'],entry_mean_nodes=cfg['entry_mean_nodes'],
        uniform_panels=cfg['uniform_panels'],primitive_order=cfg['primitive_order'])
    bounded=BoundedEntryHeightProblem(paired,state,uniform_panels=cfg['uniform_panels'],
        primitive_order=cfg['primitive_order'])
    metric=base.metric_model(state)
    for problem in [paired,bounded]:
        if (problem.metric_model(state)!=metric or problem.port.identity!=base.port.identity
                or problem.tail.identity!=base.tail.identity):
            raise ArithmeticError('a new entry model changed g/core/physical cap')
    t,theta,grid=build_grid(paired,cfg['radial_nodes'],cfg['collar_subdivisions'],cfg['angular_nodes'])
    answer={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),
        'source_receipt':receipt,'prior_completed_entry_replay':prior,
        'configuration':copy.deepcopy(cfg),'sampling_grid':grid,'cases':{},
        'selected_original_fixed_metric':metric,'source_exact_state':state_record(base,state),
        'same_original_c0_anchor_and_complete_g_in_both_new_models':True,
        'new_models_are_not_same_field_as_old_selected_or_long_entry':True,
        'same_selected_raw_coefficients_start_both_cases':True,
        'iterative_nonlinear_solve_count':0,'multivariate_optimization_performed':False,
        'finite_one_column_candidate_selections':0,'nonzero_parameter_steps_applied':0,
        'artificial_inputs_only':bool(artificial),
        'task_complete':False,'embedding_proved':False,'whole_surface_reach_proved':False}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-started
        answer['peak_rss_kib_linux']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        answer['scientific_summary_checkpoint_path']=str(summary_path(out))
        atomic_save(out,answer)
        atomic_save(summary_path(out),scientific_summary(answer,out))
    save('inputs-and-two-new-model-identities-validated')
    old=paired.original_primitive
    old_data=old.geometry(state,t,theta,cfg['primitive_order'])
    answer['unrepaired_selected_same_grid_audit']=sampled_audit(old,state,old_data)
    answer['old_sample_cost_is_comparable_only_on_this_new_shared_grid']=True
    del old_data
    save('unrepaired-selected-same-grid-reference-saved')
    for name,problem in [('paired_short',paired),('bounded_short',bounded)]:
        case={'initial_state':state_record(problem,state),
            'initial_raw_coefficients_bitwise_equal_to_selected':True}
        answer['cases'][name]=case
        initial=problem.geometry(state,t,theta,cfg['primitive_order'])
        case['initial_audit']=audit_data(problem,state,initial,cfg['tau'])
        save(name+'-initial-audit-saved')
        override=None
        if artificial_step_test:
            if not artificial:raise ValueError('artificial step test cannot evaluate a research candidate')
            override=problem.port.side*float(initial['center'][-1])+1e-4
        proposal,columns=make_height_proposal(problem,state,initial,cfg,artificial=artificial,
            override_minimum=override)
        case['height_proposal']=proposal;answer['finite_one_column_candidate_selections']+=1
        save(name+'-one-height-proposal-saved')
        changed=apply_height_proposal(problem,state,initial,proposal,columns,cfg['primitive_order'])
        if changed is None:
            final_state,final_data=state,initial
            case['height_step_status']='no_sample_feasible_candidate; state left unchanged'
        else:
            final_state,final_data,change_record=changed
            case['height_step_status']='single_proposed_coefficient_rebuilt'
            case['height_step_record']=change_record
            answer['nonzero_parameter_steps_applied']+=int(Q(change_record['exact_difference'])!=0)
        case['final_state']=state_record(problem,final_state)
        case['final_audit']=audit_data(problem,final_state,final_data,cfg['tau'])
        case['same_grid_costs_before_after']=[objective_cost(problem,initial),objective_cost(problem,final_data)]
        case['no_iteration_after_this_single_proposal']=True
        save(name+'-rebuilt-final-state-saved')
        sparse=np.array([0.,float(problem.entry.left_exact),
            float(problem.entry.left_exact+problem.entry.length_exact/3),
            float(problem.entry.left_exact+problem.entry.length_exact),
            float(problem.height_basis.right_exact),problem.seed.length])
        sparse=np.unique(sparse)
        indices=np.searchsorted(t,sparse)
        if np.any(indices>=len(t)) or not np.array_equal(t[indices],sparse):
            raise ArithmeticError('the fixed sample grid does not contain every audited interface')
        queried=problem.geometry(final_state,sparse,theta,cfg['primitive_order'])
        case['query_independent_interface_position_two_jet_difference']={
            key:float(np.max(abs(queried[key]-final_data[key][indices]))) for key in JETS}
        del queried
        doubled_theta=np.arange(2*len(theta))*np.pi/len(theta)
        doubled=problem.geometry(final_state,t,doubled_theta,cfg['primitive_order'])
        case['same_state_Pi_angle_doubling']=compare_data(problem,final_data,problem,doubled,final_state,
            name='same state Pi angular doubling',theta_stride=2)
        case['doubled_angle_final_audit']=audit_data(problem,final_state,doubled,cfg['tau'],with_rows=False)
        del doubled
        save(name+'-same-state-angle-refinement-saved')
        if name=='bounded_short':
            for label,changes in [
                ('bounded_height_angular_mean',{'height_angular_nodes':2*problem.height_angular_nodes}),
                ('bounded_fixed_primitive_GL_order',{'primitive_order':cfg['refined_primitive_order']})]:
                variant=problem.evaluation_variant(final_state,**changes)
                other=variant.geometry(final_state,t,theta,cfg['primitive_order'])
                case[label]=compare_data(problem,final_data,variant,other,final_state,name=label)
                del other,variant
                save(name+'-'+label+'-saved')
        else:
            case['unchanged_integrals_not_repeated']={
                'original_b0_mean_and_primitive_and_entry_B6_coefficients':
                    'same source integrals were refined in the checked prior audit; shorter polynomial weights are evaluated anew',
                'this_reuse_does_not_claim_a_continuous_error_bound':True,
                'no_GH_or_full_prefix_parameter_scan_performed':True}
        if artificial_step_test:
            impossible,_=make_height_proposal(problem,state,initial,cfg,artificial=True,override_minimum=1e6)
            case['artificial_unreachable_height_proposal_status']=impossible['status']
            if impossible.get('selected') is not None:
                raise ArithmeticError('artificial impossible cap-height target unexpectedly has a candidate')
        if problem.metric_model(final_state)!=metric:
            raise ArithmeticError('a final state or evaluator changed the frozen target metric')
        del initial,final_data
    if not np.array_equal(state,np.asarray(answer['source_exact_state']['parameter_coefficients_binary64'])):
        raise ArithmeticError('the original selected coefficient vector was mutated')
    save('complete-two-initial-fields-and-at-most-one-height-step-each')
    return answer


def artificial_inputs():
    original,raw=artificial_carrier()
    base,_,_=load_selected_report(original,raw)
    problem=IndependentHeightProblem(base.source,9,height_angular_nodes=base.height_angular_nodes)
    initial=problem.initial_state();selected=initial.copy()
    selected[problem.slices['height']]=.002*np.sin(np.arange(9)+.4)
    selected[problem.slices['metric']]=original['selected_state']['parameter_coefficients_binary64'][
        slice(*original['selected_state']['parameter_slices']['metric'])]
    frozen,fc=problem.frozen_metric_copy(selected)
    report=copy.deepcopy(original);report['configuration']['height_free']=9
    report['initial_exact_state']=state_record(problem,initial)
    report['selected_state']=state_record(problem,selected)
    report['final_metric_freeze']={'metric_model':frozen.metric_model(fc)}
    selected_bytes=json.dumps(report,sort_keys=True).encode()
    base,state,receipt=load_selected_report(report,raw)
    selected_sha=hashlib.sha256(selected_bytes).hexdigest();anchor_sha=hashlib.sha256(raw).hexdigest()
    cfg={'entry_mean_nodes':32,'uniform_panels':8,'primitive_order':3}
    previous=EntryRepairProblem(base,state,'6/25',**cfg)
    prior={'schema':'paired-entry-selected-fixed-g-initial-only-audit-v1',
        'status':'complete-initial-only-audit','source_files_sha256':entry_audit_hashes(),
        'source_receipt':{'selected_report_sha256':selected_sha,'original_c0_report_sha256':anchor_sha},
        'optimization_performed':False,'parameter_step_applied':False,'nonlinear_solve_count':0,
        'raw_parameter_coefficients_bitwise_unchanged':True,'complete_frozen_metric_record_unchanged':True,
        'configuration':cfg,'entry_support_exact':{'length':'6/25'},
        'entry_mean_coefficients_evaluated':previous.entry.mean_data(),
        'new_entry_state':state_record(previous,state),
        'old_corrected_evaluator_state':state_record(previous.original_primitive,state)}
    receipt.update(selected_report_sha256=selected_sha,original_c0_report_sha256=anchor_sha)
    return base,state,prior,receipt,selected_bytes,raw


def developer_check():
    base,state,prior,receipt,selected_bytes,raw=artificial_inputs()
    replay=replay_prior_entry(prior,base,state,receipt['selected_report_sha256'],receipt['original_c0_report_sha256'])
    cfg=default_configuration()
    cfg.update(entry_length='3/25',entry_mean_nodes=32,uniform_panels=8,primitive_order=3,
        refined_primitive_order=4,radial_nodes=9,angular_nodes=16,collar_subdivisions=6)
    with tempfile.TemporaryDirectory(prefix='short-bounded-artificial-',dir='/dev/shm') as directory:
        out=Path(directory)/'audit.json'
        answer=run_audit(base,state,replay,receipt,out,cfg,artificial=True,artificial_step_test=True)
        loaded=json.loads(out.read_text())
        summary=json.loads(summary_path(out).read_text())
        summary_binding=(summary['full_report']['sha256']==hashlib.sha256(out.read_bytes()).hexdigest()
            and summary['full_report']['bytes']==len(out.read_bytes())
            and summary['status']==answer['status'])
        summary_metrics=all(summary['cases'][name]['initial_audit']==compact_audit(case['initial_audit'])
            and summary['cases'][name]['final_audit']==compact_audit(case['final_audit'])
            and summary['cases'][name]['final_state']['physical_state_sha256']==
                case['final_state']['canonical_physical_state_sha256'] for name,case in answer['cases'].items())
        forbidden={'canonical_physical_state','radial_distribution','radial_rows',
            'exact_parameter_coefficients','parameter_coefficients_binary64','mathematical_definition'}
        def no_large_fields(value):
            if isinstance(value,dict):
                return not(forbidden&set(value)) and all(no_large_fields(x) for x in value.values())
            if isinstance(value,list):return all(no_large_fields(x) for x in value)
            return True
        summary_small=no_large_fields(summary)
        summary_bytes=len(summary_path(out).read_bytes())
        selected_path=Path(directory)/'selected.json.gz'
        selected_path.write_bytes(gzip.compress(selected_bytes,mtime=0))
        document,decoded,storage=read_input(selected_path,hashlib.sha256(selected_bytes).hexdigest())
        compressed_roundtrip=(decoded==selected_bytes and document==json.loads(selected_bytes) and storage['gzip_storage'])
        try:read_input(selected_path,'0'*64);wrong_sha_rejected=False
        except ValueError:wrong_sha_rejected=True
    bad=copy.deepcopy(prior);bad['new_entry_state']['parameter_coefficients_binary64'][0]+=1e-4
    try:replay_prior_entry(bad,base,state,receipt['selected_report_sha256'],receipt['original_c0_report_sha256']);bad_prior_rejected=False
    except ValueError:bad_prior_rejected=True
    try:require_public_actions('true','another/repo',[]);wrong_repo_rejected=False
    except ValueError:wrong_repo_rejected=True
    try:require_public_actions('true','Rogerhu12/math-research-public',['/dev/shm/unpublished.json']);wrong_path_rejected=False
    except ValueError:wrong_path_rejected=True
    cases=answer['cases']
    both_applied=all(c['height_step_status']=='single_proposed_coefficient_rebuilt' for c in cases.values())
    finite_errors=max(max(c['height_step_record']['reconstructed_six_position_jets_vs_finite_change_formulas'].values())
        for c in cases.values()) if both_applied else None
    query=max(max(c['query_independent_interface_position_two_jet_difference'].values()) for c in cases.values())
    refinements=all(c['same_state_Pi_angle_doubling']['same_canonical_state_and_exact_coefficients'] for c in cases.values())
    for key in ['bounded_height_angular_mean','bounded_fixed_primitive_GL_order']:
        refinements=refinements and cases['bounded_short'][key]['same_canonical_state_and_exact_coefficients']
    impossible=all(c['artificial_unreachable_height_proposal_status']=='no_feasible_sample_interval' for c in cases.values())
    result={'schema':'short-bounded-entry-full-main-artificial-check-v1',
        'artificial_inputs_only':True,'research_candidate_or_actual_report_evaluated':False,
        'Actions_environment_not_forged':True,'complete_common_main_path_executed_on_artificial_data':True,
        'both_new_models_and_one_proposal_each_rebuilt':both_applied,
        'all_six_finite_height_change_formula_errors_max':finite_errors,
        'query_independent_interface_jet_difference_max':query,
        'all_same_state_single_factor_refinement_identities_match':bool(refinements),
        'empty_height_interval_paths_checked':impossible,
        'gzip_exact_decoded_byte_roundtrip':compressed_roundtrip,
        'wrong_input_SHA_rejected':wrong_sha_rejected,'altered_prior_state_rejected':bad_prior_rejected,
        'wrong_repository_rejected':wrong_repo_rejected,'unpublished_input_path_rejected':wrong_path_rejected,
        'JSON_roundtrip_unchanged':loaded==answer,
        'checkpoint_summary_binds_full_report_bytes_and_status':summary_binding,
        'checkpoint_summary_preserves_case_metrics_and_state_hashes':summary_metrics,
        'checkpoint_summary_omits_large_canonical_and_radial_fields':summary_small,
        'artificial_checkpoint_summary_bytes':summary_bytes,
        'iterative_nonlinear_solve_count':answer['iterative_nonlinear_solve_count'],
        'actual_artificial_parameter_count':base.nunknown,
        'passed':bool(both_applied and finite_errors<1e-9 and query<1e-10 and refinements
            and impossible and compressed_roundtrip and wrong_sha_rejected and bad_prior_rejected
            and wrong_repo_rejected and wrong_path_rejected and loaded==answer
            and summary_binding and summary_metrics and summary_small
            and answer['iterative_nonlinear_solve_count']==0)}
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true')
    p.add_argument('--input',type=Path);p.add_argument('--anchor-input',type=Path)
    p.add_argument('--prior-entry-audit',type=Path)
    p.add_argument('--expected-input-sha256');p.add_argument('--expected-anchor-sha256')
    p.add_argument('--expected-prior-sha256')
    p.add_argument('--entry-length',default='81/1000');p.add_argument('--entry-mean-nodes',type=int,default=1024)
    p.add_argument('--uniform-panels',type=int,default=120);p.add_argument('--primitive-order',type=int,default=8)
    p.add_argument('--refined-primitive-order',type=int,default=12)
    p.add_argument('--radial-nodes',type=int,default=121);p.add_argument('--angular-nodes',type=int,default=384)
    p.add_argument('--collar-subdivisions',type=int,default=24)
    p.add_argument('--height-column',type=int,default=4);p.add_argument('--height-bound',type=float,default=1.)
    p.add_argument('--tau',default='61/1000');p.add_argument('--height-margin',default='1/1000')
    p.add_argument('--minimum-signed-height',default='0',help='exact rational or none; selected upper branch only')
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    if args.check_only:
        result=developer_check();result['source_files_sha256']=implementation_hashes()
        atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    if any(x is None for x in [args.input,args.anchor_input,args.prior_entry_audit]):
        raise SystemExit('--input, --anchor-input, and --prior-entry-audit are required')
    require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
        [args.input,args.anchor_input,args.prior_entry_audit])
    report,selected_bytes,selected_input=read_input(args.input,args.expected_input_sha256)
    _,anchor_bytes,anchor_input=read_input(args.anchor_input,args.expected_anchor_sha256)
    prior_document,prior_bytes,prior_input=read_input(args.prior_entry_audit,args.expected_prior_sha256)
    base,state,receipt=load_selected_report(report,anchor_bytes)
    receipt.update(selected_report_sha256=selected_input['decoded_sha256'],
        original_c0_report_sha256=anchor_input['decoded_sha256'])
    replay=replay_prior_entry(prior_document,base,state,selected_input['decoded_sha256'],anchor_input['decoded_sha256'])
    receipt['exact_input_storage']={'selected':selected_input,'original_c0':anchor_input,'prior_entry_audit':prior_input}
    cfg=default_configuration()
    for name in ['entry_length','entry_mean_nodes','uniform_panels','primitive_order','refined_primitive_order',
                 'radial_nodes','angular_nodes','collar_subdivisions','height_column','tau','height_margin']:
        cfg[name]=getattr(args,name)
    if not np.isfinite(args.height_bound) or args.height_bound<=0:raise ValueError('positive finite height box required')
    if Q(args.tau)<=0 or Q(args.height_margin)<0:raise ValueError('positive tau and nonnegative height margin required')
    cfg['height_coefficient_bounds']=[-args.height_bound,args.height_bound]
    cfg['minimum_signed_height']=None if args.minimum_signed_height.lower()=='none' else str(Q(args.minimum_signed_height))
    answer=run_audit(base,state,replay,receipt,args.out,cfg)
    print(json.dumps({'out':str(args.out),'status':answer['status'],
        'iterative_nonlinear_solve_count':0,'nonzero_parameter_steps_applied':answer['nonzero_parameter_steps_applied']}),flush=True)


if __name__=='__main__':main()

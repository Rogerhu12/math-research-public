#!/usr/bin/env python3
"""Read-only replay of one frozen independent-height state with a fixed primitive.

No optimizer is called here. Research evaluation requires this
public repository's Actions. --check-only covers the same replay/audit path
using an artificial carrier and selected state.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import tempfile

import numpy as np

from frame_collar_bvp import atomic_save,FrameCollarProblem,EllipticCylinderPort,NegativeKRadialSeed
from frame_collar_bent_tail import artificial_enriched_report,load_enriched_report
from frame_collar_enriched import make_enriched
from frame_collar_natural_body_audit import NaturalBodyProblem
from frame_collar_residual_audit import digest
from frame_independent_height import IndependentHeightProblem
from frame_independent_height_solve import (state_record,sampled_audit,radial_distribution,
    compare_evaluation,implementation_hashes as original_hashes)
from frame_fixed_height_primitive import FixedPrimitiveProblem


def implementation_hashes():
    answer=original_hashes()
    for name in ['frame_fixed_height_primitive.py',Path(__file__).name]:
        answer[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return answer


def load_selected_report(report,anchor_bytes):
    """Strict replay of the old source before adding an evaluation wrapper."""
    if report.get('schema')!='independent-height-bounded-direct-metric-solve-v1':
        raise ValueError('a published independent-height bounded report is required')
    if report['source_files_sha256']!=original_hashes():
        raise ValueError('published implementation hashes do not match the frozen original modules')
    record=report['source_record']
    if hashlib.sha256(anchor_bytes).hexdigest()!=record['sha256']:
        raise ValueError('the original c0 carrier bytes do not match their recorded source hash')
    old,c0,replay=load_enriched_report(json.loads(anchor_bytes))
    c0_exact=[str(Q.from_float(float(x))) for x in c0]
    if record['identity']!=replay or record['exact_original_c0']!=c0_exact:
        raise ValueError('source c0 canonical replay or exact coefficient identity mismatch')
    cfg=report['configuration']
    natural=NaturalBodyProblem(old,c0,metric_free=cfg['metric_free'],
        support_width='1/10',plateau_fraction='1/3',tau0='1/128',
        heat_order=cfg['heat_order'],radial_nodes=cfg['radial_nodes'],
        angular_nodes=cfg['angular_nodes'],quadrature_order=cfg['quadrature_order'])
    problem=IndependentHeightProblem(natural,cfg['height_free'],
        height_angular_nodes=cfg['height_angular_nodes'])
    if state_record(problem,problem.initial_state())!=report['initial_exact_state']:
        raise ValueError('initial complete model, source anchor, g, layout or coefficient replay mismatch')
    selected=report['selected_state'];state=np.asarray(selected['parameter_coefficients_binary64'],float)
    if state.shape!=(problem.nunknown,) or not np.all(np.isfinite(state)):
        raise ValueError('invalid selected coefficient vector')
    for name,sl in problem.slices.items():
        values=selected['exact_parameter_coefficients'][name]
        if len(values)!=sl.stop-sl.start or any(Q(x)!=Q.from_float(float(y))
                for x,y in zip(values,state[sl])):
            raise ValueError('selected exact rational coefficients do not match binary64 values')
    if state_record(problem,state)!=selected:
        raise ValueError('selected canonical state, metric, layout or evaluation replay mismatch')
    frozen,coefficient=problem.frozen_metric_copy(state)
    if frozen.identity(coefficient)!=selected['canonical_physical_state']:
        raise ArithmeticError('freezing changed the complete selected physical identity')
    if (frozen.metric_model(coefficient)['mathematical_definition']!=
            report['final_metric_freeze']['metric_model']['mathematical_definition']):
        raise ValueError('published frozen g does not match the reconstructed selected state')
    receipt={'old_report_schema':report['schema'],'source_original_c0_exact':c0_exact,
        'source_record_replayed_exactly':True,'initial_state_replayed_exactly':True,
        'selected_state_replayed_exactly':True,'all_original_source_hashes_match':True,
        'selected_physical_state_sha256':digest(frozen.identity(coefficient)),
        'selected_metric_definition_sha256':frozen.metric_model(coefficient)['mathematical_definition_sha256'],
        'source_parameter_count':problem.nunknown,'frozen_parameter_count':frozen.nunknown,
        'metric_freeze_preserves_the_complete_physical_state':True,
        'frozen_exact_state':state_record(frozen,coefficient)}
    return frozen,coefficient,receipt


def height_conditions(problem,data,tau='61/1000'):
    """Numerical diagnostics for explicitly stated cap/core necessary screens."""
    target=float(Q(tau));h=problem.port.side*float(data['center'][-1])
    w=problem.port.width;B=problem.port.minor;rc=problem.seed.cut_radius
    signed=problem.port.side*data['X'][...,2]-w
    available=0<=B-target<=rc
    return {'target_reach_exact':str(Q(tau)),
        'single_cap_height_evaluated':h,
        'minimum_sampled_signed_side_height_minus_core_width':float(np.min(signed)),
        'signed_height_nonnegative_is_a_chosen_mirror_separation_condition_not_a_general_necessity':True,
        'mirrored_held_flat_disks_normal_chord_upper_formula':'abs(h)',
        'mirrored_held_disks_evaluated_normal_chord_upper':abs(h),
        'mirrored_held_disks_height_margin_to_target':abs(h)-target,
        'core_minor_tangent_ball_witness_available':bool(available),
        'core_minor_tangent_ball_witness_definition':'p=(0,B,w), normal-center=(0,B-tau,w), q=(0,B-tau,h) in held disk',
        'core_minor_tangent_ball_general_necessary_condition':'abs(h-core_half_width) >= tau',
        'evaluated_core_minor_tangent_ball_general_margin':abs(h-w)-target if available else None,
        'cap_is_at_or_above_core_top':bool(h>=w),
        'necessary_upper_cap_height_condition_if_h_at_least_core_width_and_witness_available':'h >= core_half_width + tau',
        'evaluated_upper_cap_height_margin':h-w-target if available and h>=w else None,
        'these_height_values_have_no_continuous_quadrature_error_bound':True,
        'no_strict_reach_exclusion_or_embedding_certificate_claimed':True}


def run_audit(problem,state,out,*,uniform_panels=120,primitive_order=8,
              refined_panels=240,refined_order=12,radial_nodes=121,angular_nodes=384,
              source_receipt=None,artificial=False):
    wrapper=FixedPrimitiveProblem(problem,uniform_panels,primitive_order)
    if wrapper.identity(state)!=problem.identity(state):raise ArithmeticError('wrapper changed physical identity')
    tf=problem.height_basis.right;tc=problem.height_basis.left;L=problem.seed.length
    sparse=np.array([0.,tc,tf,L]);dense=np.linspace(0,L,int(radial_nodes))
    complete=np.unique(np.r_[dense,sparse]);theta=np.arange(int(angular_nodes))*2*np.pi/int(angular_nodes)
    if len(theta)<4 or len(theta)%4:raise ValueError('full-period angle count must be a positive multiple of four')
    result={'schema':'fixed-height-primitive-selected-state-read-only-audit-v1',
        'source_receipt':source_receipt,'source_files_sha256':implementation_hashes(),
        'same_canonical_physical_state':True,'physical_state_sha256':digest(problem.identity(state)),
        'frozen_state':state_record(problem,state),'new_evaluation_definition':wrapper.evaluation_definition(),
        'artificial_inputs_only':bool(artificial),'optimization_performed':False,'nonlinear_solve_count':0,
        'task_complete':False,'embedding_proved':False,'whole_surface_reach_proved':False,
        'status':'before-old-replays'}
    atomic_save(out,result)
    old_sparse=problem.geometry(state,sparse,theta,primitive_order)
    result['old_sparse_audit']=sampled_audit(problem,state,old_sparse)
    old_dense=problem.geometry(state,dense,theta,primitive_order)
    result['old_dense_audit']=sampled_audit(problem,state,old_dense)
    result['old_sparse_dense_cap_height_difference']=float(old_sparse['center'][-1]-old_dense['center'][-1])
    result['status']='old-replays-preserved';atomic_save(out,result)
    new_sparse=wrapper.geometry(state,sparse,theta,primitive_order)
    result['new_sparse_audit']=sampled_audit(wrapper,state,new_sparse)
    new_dense=wrapper.geometry(state,dense,theta,primitive_order)
    result['new_dense_audit']=sampled_audit(wrapper,state,new_dense)
    result['new_dense_radial_distribution']=radial_distribution(wrapper,new_dense)
    result['new_sparse_dense_cap_height_difference']=float(new_sparse['center'][-1]-new_dense['center'][-1])
    result['old_new_dense_position_jet_differences']={key:float(np.max(abs(old_dense[key]-new_dense[key])))
        for key in ['X','Xs','Xt','Xss','Xst','Xtt']}
    result['height_conditions_old_dense']=height_conditions(problem,old_dense)
    result['height_conditions_new_dense']=height_conditions(wrapper,new_dense)
    result['status']='new-fixed-partition-replays-preserved';atomic_save(out,result)
    union=wrapper.geometry(state,complete,theta,primitive_order)
    indexes=np.searchsorted(complete,sparse)
    result['new_complete_chart_audit']=sampled_audit(wrapper,state,union)
    result['sparse_vs_complete_query_position_two_jet_differences']={key:
        float(np.max(abs(new_sparse[key]-union[key][indexes]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt']}
    result['status']='common-interface-chart-checked';atomic_save(out,result)
    order_variant=wrapper.evaluation_variant(state,primitive_order=refined_order)
    result['fixed_partition_GL_order_comparison']=compare_evaluation(wrapper,state,order_variant,
        complete,theta,primitive_order)
    result['status']='same-partition-order-refinement-complete';atomic_save(out,result)
    partition_variant=wrapper.evaluation_variant(state,uniform_panels=refined_panels)
    result['fixed_GL_order_partition_comparison']=compare_evaluation(wrapper,state,partition_variant,
        complete,theta,primitive_order)
    result['status']='complete-read-only-audit';atomic_save(out,result)
    return result


def artificial_carrier():
    core=EllipticCylinderPort('9/10','18/25','1/50',1)
    seed=NegativeKRadialSeed.from_core(core,'11/10','11/50')
    baseline=FrameCollarProblem(core,seed,radial_free=2,angular_modes=2,
        ellipse_envelope=(core.major,core.minor),height_limit=.1,radial_nodes=9,angular_nodes=24,
        radial_quadrature_order=3)
    old=make_enriched(baseline,2,1,9,24,3,strip_half_width='2/5')
    c0=.004*np.sin(np.arange(old.nunknown)+.3)
    carrier=artificial_enriched_report(old,c0,baseline,.003*np.cos(np.arange(baseline.nunknown)))
    raw=json.dumps(carrier,sort_keys=True).encode();old,c0,replay=load_enriched_report(json.loads(raw))
    cfg={'metric_free':2,'height_free':3,'heat_order':8,'height_angular_nodes':24,
         'radial_nodes':9,'angular_nodes':24,'quadrature_order':3}
    source=NaturalBodyProblem(old,c0,metric_free=2,heat_order=8,radial_nodes=9,angular_nodes=24,quadrature_order=3)
    problem=IndependentHeightProblem(source,3,height_angular_nodes=24)
    state=problem.initial_state();state[problem.slices['height']]=[.003,-.002,.001]
    state[problem.slices['metric']]=[.003,-.004]
    frozen,fc=problem.frozen_metric_copy(state)
    report={'schema':'independent-height-bounded-direct-metric-solve-v1','configuration':cfg,
        'source_files_sha256':original_hashes(),'source_record':{
            'sha256':hashlib.sha256(raw).hexdigest(),'identity':replay,
            'exact_original_c0':[str(Q.from_float(float(x))) for x in c0]},
        'initial_exact_state':state_record(problem,problem.initial_state()),
        'selected_state':state_record(problem,state),
        'final_metric_freeze':{'metric_model':frozen.metric_model(fc)}}
    return report,raw


def developer_check():
    report,raw=artificial_carrier();problem,state,receipt=load_selected_report(report,raw)
    with tempfile.TemporaryDirectory(prefix='fixed-height-audit-artificial-',dir='/dev/shm') as folder:
        out=Path(folder)/'audit.json'
        result=run_audit(problem,state,out,uniform_panels=16,primitive_order=4,
            refined_panels=32,refined_order=6,radial_nodes=17,angular_nodes=24,
            source_receipt=receipt,artificial=True)
        roundtrip=json.loads(out.read_text())
    bad=json.loads(json.dumps(report));bad['selected_state']['exact_parameter_coefficients']['height'][0]='1/3'
    try:load_selected_report(bad,raw);rejected=False
    except ValueError:rejected=True
    comparisons=result['sparse_vs_complete_query_position_two_jet_differences']
    passed=(result['status']=='complete-read-only-audit' and result==roundtrip
        and result['nonlinear_solve_count']==0 and rejected and max(comparisons.values())<1e-12
        and result['new_sparse_dense_cap_height_difference']==0
        and result['fixed_partition_GL_order_comparison']['same_canonical_identity_and_coefficients']
        and result['fixed_GL_order_partition_comparison']['same_canonical_identity_and_coefficients'])
    return {'schema':'fixed-height-primitive-audit-artificial-main-check-v1','passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False,
        'same_run_audit_as_actual_main':True,'strict_selected_state_replay_exercised':True,
        'tampered_exact_coefficient_rejected':rejected,'complete_JSON_roundtrip':result==roundtrip,
        'sparse_complete_position_two_jet_differences':comparisons,
        'new_sparse_dense_cap_height_difference':result['new_sparse_dense_cap_height_difference'],
        'old_sparse_dense_cap_height_difference_artificial':result['old_sparse_dense_cap_height_difference'],
        'all_final_audits_and_two_separate_primitive_refinements_completed':True,
        'physical_identity_unchanged_by_primitive_evaluation':True,
        'finite_checks_not_continuous_error_bounds':True}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check-only',action='store_true')
    p.add_argument('--input',type=Path);p.add_argument('--anchor-input',type=Path);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--uniform-panels',type=int,default=120);p.add_argument('--primitive-order',type=int,default=8)
    p.add_argument('--refined-panels',type=int,default=240);p.add_argument('--refined-order',type=int,default=12)
    p.add_argument('--radial-nodes',type=int,default=121);p.add_argument('--angular-nodes',type=int,default=384)
    args=p.parse_args()
    if args.check_only:
        result=developer_check();result['source_files_sha256']=implementation_hashes();atomic_save(args.out,result)
        print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        p.error('actual frozen-state evaluation requires the public repository Actions')
    if not args.input or not args.anchor_input:p.error('both selected report and original c0 report are required')
    notes=Path(__file__).resolve().parents[1]/'notes'
    if any(not q.resolve().is_relative_to(notes.resolve()) for q in [args.input,args.anchor_input]):
        p.error('both source reports must be public topic notes')
    raw=args.input.read_bytes();anchor=args.anchor_input.read_bytes()
    problem,state,receipt=load_selected_report(json.loads(raw),anchor)
    receipt.update(selected_report_path=str(args.input),selected_report_sha256=hashlib.sha256(raw).hexdigest(),
        original_anchor_path=str(args.anchor_input),original_anchor_sha256=hashlib.sha256(anchor).hexdigest())
    result=run_audit(problem,state,args.out,uniform_panels=args.uniform_panels,primitive_order=args.primitive_order,
        refined_panels=args.refined_panels,refined_order=args.refined_order,
        radial_nodes=args.radial_nodes,angular_nodes=args.angular_nodes,source_receipt=receipt)
    print(json.dumps({'out':str(args.out),'status':result['status'],'nonlinear_solve_count':0}),flush=True)


if __name__=='__main__':main()

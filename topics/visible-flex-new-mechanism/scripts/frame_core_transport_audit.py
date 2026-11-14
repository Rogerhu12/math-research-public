#!/usr/bin/env python3
"""Audit one new B=37/100 core with one strictly transported selected state.

No optimizer or parameter step is called. Research input and geometry require
the public repository Actions. --check-only executes the same IO/audit chain
with the core transport factory's one declared artificial carrier.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import tempfile
import traceback

import numpy as np

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_core_transport import (build_core_transport, artificial_source, require_public_actions,
    implementation_hashes as factory_hashes)
from frame_fixed_height_primitive import FixedPrimitiveProblem, fixed_partition
from frame_independent_height_solve import (state_record, sampled_audit, point_values,
    radial_distribution, extremum)


def implementation_hashes():
    out=factory_hashes()
    out[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return out


def default_configuration(artificial=False):
    if artificial:
        return {'target_minor':'2/3','heat_order':8,'height_angular_nodes':24,
            'constructor_radial_nodes':9,'constructor_angular_nodes':24,'constructor_quadrature_order':3,
            'radial_nodes':9,'angular_nodes':24,'doubled_angular_nodes':48,
            'uniform_primitive_panels':8,'primitive_order':3,'query_quadrature_order':3,
            'target_reach':'61/1000','ball_radius':'101/100','strip_half_width':'19/50'}
    return {'target_minor':'37/100','heat_order':32,'height_angular_nodes':384,
        'constructor_radial_nodes':61,'constructor_angular_nodes':192,'constructor_quadrature_order':4,
        'radial_nodes':121,'angular_nodes':384,'doubled_angular_nodes':768,
        'uniform_primitive_panels':120,'primitive_order':8,'query_quadrature_order':8,
        'target_reach':'61/1000','ball_radius':'101/100','strip_half_width':'19/50'}


def structure_grid(problem,uniform_nodes):
    count=int(uniform_nodes)
    if count<3:raise ValueError('at least three full radial query nodes required')
    if problem.metric_free:raise ValueError('the new target metric must be frozen before this audit')
    seed=problem.seed;L=seed.length_exact
    # Use all immutable b0 pieces, even though they are already separately
    # covered by the query-independent primitive's fixed prefix partition.
    structure=fixed_partition(problem,4)['construction_sources_exact']
    structure={key:values for key,values in structure.items() if key!='uniform'}
    structure['height_basis_knots']=list(problem.height_basis.identity['clamped_knots_exact'])
    structure['body_metric_knots']=list(problem.body_metric.family_definition['clamped_knots_exact'])
    structure['query_uniform']=[str(L*Q(j,count-1)) for j in range(count)]
    exact_nodes=sorted({Q(x) for values in structure.values() for x in values})
    if exact_nodes[0]!=0 or exact_nodes[-1]!=L:raise ArithmeticError('the structure chart must span [0,L]')
    points=np.array([float(x) for x in exact_nodes])
    if np.any(np.diff(points)<=0):raise ArithmeticError('distinct exact query nodes rounded to the same binary64 point')
    definition={'schema':'transport-core-complete-structure-query-grid-v1',
        'uniform_nodes_requested':count,'construction_sources_exact':structure,
        'radial_points_exact':[str(x) for x in exact_nodes],
        'height_base_definition_sha256':digest(problem.height_base_definition),
        'complete_metric_definition_sha256':problem.metric_model(np.zeros(problem.nunknown))['mathematical_definition_sha256'],
        'query_grid_does_not_change_the_common_height_primitive':True}
    return points,definition


def mirror_diagnostics(problem,data,tau):
    target=float(Q(tau));U,T,X=(data[key] for key in ['Xs','T','X'])
    W=np.cross(U,T);area=np.linalg.norm(W,axis=-1);Wz=abs(W[...,2]);z=X[...,2]
    valid=(area>0)&np.isfinite(area)&np.isfinite(z)&(Wz>0)
    radius=np.divide(abs(z)*area,Wz,out=np.full_like(z,np.inf),where=valid)
    signed=problem.port.side*z
    return {'schema':'transport-core-mirror-pair-sampled-necessary-screen-v1',
        'target_reach_exact':str(Q(tau)),
        'normal_chord_formula':'abs(X_z)*norm(X_s cross T)/abs((X_s cross T)_z)',
        'smallest_finite_mirror_pair_radius':extremum(radius,data['radial'],data['theta'],'min'),
        'finite_nonzero_normal_witness_count':int(valid.sum()),
        'sampled_witness_below_target_count':int(np.sum(valid&(radius<target))),
        'nonregular_sample_count':int(np.sum((area<=0)|~np.isfinite(area))),
        'exact_floating_zero_height_count':int(np.sum(z==0)),
        'minimum_signed_side_height':extremum(signed,data['radial'],data['theta'],'min'),
        'signed_positive_is_the_selected_upper_mirror_branch_screen':True,
        'these_are_sampled_points_of_the_proposed_reflected_union_not_an_embedding_certificate':True,
        'passing_these_pairs_does_not_certify_other_pairs_or_surface_reach':True}


def r66_height_diagnostics(problem,data,tau):
    """Evaluate the exact three-branch necessary gate, with numerical h."""
    tauq=Q(tau);gap=abs(problem.port.B_exact-problem.tail.outer_exact)
    if tauq<=0:raise ValueError('positive target reach required')
    w=problem.port.width_exact
    if gap>=2*tauq:
        branch='gap_at_least_twice_target';constant=Q(0);root=Q(0)
        forced_upper=False
    elif gap>=tauq:
        branch='target_at_most_gap_below_twice_target';constant=Q(0);root=gap*(2*tauq-gap)
        forced_upper=root>=w*w
    else:
        branch='gap_below_target';constant=tauq;root=tauq*tauq-gap*gap
        forced_upper=(constant>=w or root>=(w-constant)**2)
    lower=float(constant)+np.sqrt(float(root))
    h=problem.port.side*float(data['center'][-1]);delta=abs(h-float(w))
    return {'schema':'R66-new-core-two-normal-height-gate-v1',
        'proof_source':'results/R66-core-flat-cap-two-normal-reach-height-gate.md',
        'assumption':'the completed reflected surface has reach at least the selected target tau',
        'not_inferred_from_README_reach_ratio_without_a_diameter_bound':True,
        'target_reach_exact':str(tauq),'core_minor_exact':str(problem.port.B_exact),
        'cap_vertex_radius_exact':str(problem.tail.outer_exact),'gap_exact':str(gap),
        'core_half_width_exact':str(w),'branch':branch,
        'absolute_height_gap_lower_exact':{'constant':str(constant),'square_root_of':str(root)},
        'general_necessary_condition':'abs(h-w) >= constant + sqrt(square_root_of)',
        'necessary_absolute_gap_evaluated':float(lower),'cap_height_evaluated':h,
        'evaluated_absolute_gap_margin':float(delta-lower),
        'standard_positive_upper_cap_branch':bool(h>0),
        'positive_h_forces_upper_branch_from_exact_L_ge_w':bool(forced_upper),
        'upper_cap_height_lower_evaluated_if_positive_branch_forced':float(w)+float(lower) if forced_upper else None,
        'upper_cap_height_margin_if_positive_branch_forced':h-float(w)-float(lower) if forced_upper else None,
        'reflected_held_disks_necessary_height_margin':abs(h)-float(tauq),
        'numerical_height_primitive_and_square_root_not_interval_certified':True,
        'no_strict_reach_certificate_or_unqualified_exclusion_is_asserted':True}


def full_port_comparison(problem,data):
    t,theta=data['radial'],data['theta'];inside=t<=problem.height_basis.left
    if not np.any(inside):raise ValueError('the complete core prefix is missing')
    exact=problem.port.position_jets(t[inside,None],theta[None,:])
    mapping={'X':'X','Xs':'Xs','Xt':'Xtheta','Xss':'Xss','Xst':'Xst','Xtt':'Xtt'}
    errors={key:float(np.max(np.linalg.norm(data[key][inside]-exact[name],axis=-1)))
            for key,name in mapping.items()}
    return {'complete_open_core_prefix_position_two_jet_errors':errors,
        'core_prefix_radial_nodes':int(inside.sum()),
        'tail_ports_are_in_the_full_sampled_audit_and_use_one_common_h':True,
        'all_differences_include_finite_Pi_and_fixed_primitive_error':True}


def audit_data(problem,state,data,tau):
    return {'sampled':sampled_audit(problem,state,data),
        'core_prefix':full_port_comparison(problem,data),
        'mirror_pairs':mirror_diagnostics(problem,data,tau),
        'R66_height':r66_height_diagnostics(problem,data,tau),
        'radial_distribution':radial_distribution(problem,data)}


def paired_angle_comparison(problem,state,left,right):
    if len(right['theta'])!=2*len(left['theta']) or not np.array_equal(left['radial'],right['radial']):
        raise ValueError('same radial grid and exactly doubled angle count required')
    if not np.array_equal(left['theta'],right['theta'][::2]):
        raise ValueError('angle refinement must contain each original query angle exactly')
    p0,p1=point_values(problem,left),point_values(problem,right)
    return {'same_physical_state_sha256':digest(problem.identity(state)),
        'same_g_height_base_anchor_and_all_exact_coefficients':True,
        'angular_nodes':[len(left['theta']),len(right['theta'])],
        'position_two_jet_differences':{key:float(np.max(np.linalg.norm(left[key]-right[key][:,::2],axis=-1)))
            for key in ['X','Xs','Xt','Xss','Xst','Xtt']},
        'direct_metric_differences':{key:float(np.max(abs(p0[key]-p1[key][:,::2])))
            for key in ['E_minus_one','F_over_a','metric_operator_error']},
        'common_center_difference':float(np.max(abs(left['center']-right['center']))),
        'GH_Nb_fixed_prefix_partition_and_GL_rules_held_fixed':True,
        'no_coefficient_refit_or_optimization':True,'not_a_continuous_error_bound':True}


def summary_path(out):
    return out.with_name(out.stem+'-summary.json')


def compact_summary(report):
    out={key:report.get(key) for key in ['schema','status','source_files_sha256','inputs','configuration',
        'physical_state_sha256','old_selected_physical_state_sha256','new_metric_definition_sha256',
        'old_selected_metric_definition_sha256','target_core_identity','old_core_identity',
        'new_height_base_definition_sha256','artificial_inputs_only','optimization_performed',
        'step_applied','error_type','error','traceback'] if key in report}
    for key in ['initial_audit','doubled_angle_audit']:
        if key in report:out[key]={name:value for name,value in report[key].items() if name!='radial_distribution'}
    for key in ['freeze_preserves_complete_state','sparse_complete_query_comparison','same_parameter_Pi_refinement']:
        if key in report:out[key]=report[key]
    out['isometry_embedding_reach_or_containment_proved']=False
    return out


def save_report(out,report):
    atomic_save(out,report)
    summary=compact_summary(report)
    summary['full_report_bytes_sha256']=hashlib.sha256(out.read_bytes()).hexdigest()
    summary['full_report_filename']=out.name
    atomic_save(summary_path(out),summary)


def run_from_files(selected_path,anchor_path,out,configuration,*,expected_selected_sha256,
        expected_anchor_sha256,artificial=False):
    cfg=dict(configuration)
    report={'schema':'new-elliptic-core-single-transported-selected-audit-v1',
        'status':'before-input-replay','configuration':cfg,'source_files_sha256':implementation_hashes(),
        'artificial_inputs_only':bool(artificial),'optimization_performed':False,'step_applied':False,
        'isometry_embedding_reach_or_containment_proved':False}
    save_report(out,report)
    try:
        if not artificial:
            require_public_actions()
            if Q(cfg['target_minor'])!=Q(37,100):raise ValueError('this research driver audits only B=37/100')
            notes=Path(__file__).resolve().parents[1]/'notes'
            if any(not path.resolve().is_relative_to(notes.resolve()) for path in [selected_path,anchor_path]):
                raise ValueError('both real source inputs must be public topic notes')
        if not expected_selected_sha256 or not expected_anchor_sha256:
            raise ValueError('both exact input byte hashes are required')
        raw=selected_path.read_bytes();anchor=anchor_path.read_bytes()
        report['inputs']={'selected':{'path':str(selected_path),'sha256':hashlib.sha256(raw).hexdigest()},
            'original_enriched_anchor':{'path':str(anchor_path),'sha256':hashlib.sha256(anchor).hexdigest()}}
        if report['inputs']['selected']['sha256']!=expected_selected_sha256:
            raise ValueError('selected input bytes differ from the pinned SHA')
        if report['inputs']['original_enriched_anchor']['sha256']!=expected_anchor_sha256:
            raise ValueError('original anchor bytes differ from the pinned SHA')
        free,initial,receipt=build_core_transport(anchor,target_minor=cfg['target_minor'],
            selected_report_bytes=raw,expected_anchor_sha256=expected_anchor_sha256,
            expected_selected_sha256=expected_selected_sha256,metric_free=5,height_free=9,
            heat_order=cfg['heat_order'],height_angular_nodes=cfg['height_angular_nodes'],
            radial_nodes=cfg['constructor_radial_nodes'],angular_nodes=cfg['constructor_angular_nodes'],
            quadrature_order=cfg['constructor_quadrature_order'],ball_radius=cfg['ball_radius'],
            strip_half_width=cfg['strip_half_width'],artificial=artificial)
        before=free.identity(initial);frozen,state=free.frozen_metric_copy(initial)
        if frozen.identity(state)!=before:raise ArithmeticError('target metric freeze changed the complete field')
        problem=FixedPrimitiveProblem(frozen,cfg['uniform_primitive_panels'],cfg['primitive_order'])
        if problem.identity(state)!=before:raise ArithmeticError('fixed primitive changed the target physical definition')
        source_selected=receipt['initializer']['selected_input']['replay_receipt']
        report.update(transport_factory_receipt=receipt,target_frozen_state=state_record(problem,state),
            physical_state_sha256=digest(before),
            old_selected_physical_state_sha256=source_selected['selected_physical_state_sha256'],
            new_metric_definition_sha256=problem.metric_model(state)['mathematical_definition_sha256'],
            old_selected_metric_definition_sha256=source_selected['selected_metric_definition_sha256'],
            target_core_identity=problem.port.identity,
            old_core_identity=receipt['transport_definition']['source_core_identity'],
            new_height_base_definition_sha256=digest(problem.height_base_definition),
            numerical_evaluation_definition=problem.evaluation_definition(),
            freeze_preserves_complete_state=True)
        if report['new_metric_definition_sha256']==report['old_selected_metric_definition_sha256']:
            raise ArithmeticError('changed core unexpectedly retained the old complete metric identity')
        report['status']='strict-source-replay-new-target-frozen';save_report(out,report)
        radial,sampling=structure_grid(problem,cfg['radial_nodes'])
        n=int(cfg['angular_nodes']);double=int(cfg['doubled_angular_nodes'])
        if n<4 or n%4 or double!=2*n:raise ValueError('positive multiple-of-four angles and exact doubling required')
        theta=np.arange(n)*2*np.pi/n
        report['sampling_grid']=sampling
        report['objective_evaluation']={'kind':'read-only direct metric and original smooth ball-strip diagnostic',
            'radial_nodes':len(radial),'angular_nodes':n,
            'query_quadrature_order':cfg['query_quadrature_order'],'no_minimization':True}
        data=problem.geometry(state,radial,theta,cfg['query_quadrature_order'])
        report['initial_audit']=audit_data(problem,state,data,cfg['target_reach'])
        report['status']='new-core-single-initial-state-audited';save_report(out,report)
        sparse=np.array([0.,problem.height_basis.left,problem.height_basis.right,problem.seed.length])
        index=np.searchsorted(radial,sparse)
        if not np.array_equal(radial[index],sparse):raise ArithmeticError('full exact structure grid misses a port')
        small=problem.geometry(state,sparse,theta,cfg['query_quadrature_order'])
        report['sparse_complete_query_comparison']={
            'position_two_jet_differences':{key:float(np.max(abs(small[key]-data[key][index])))
                for key in ['X','Xs','Xt','Xss','Xst','Xtt']},
            'common_center_difference':float(np.max(abs(small['center']-data['center'][index]))),
            'same_fixed_primitive_definition':True,'query_set_does_not_define_the_physical_height':True}
        report['status']='query-independent-port-chart-checked';save_report(out,report)
        theta2=np.arange(double)*2*np.pi/double
        refined=problem.geometry(state,radial,theta2,cfg['query_quadrature_order'])
        if problem.identity(state)!=before:raise ArithmeticError('the read-only audit changed the exact state')
        report['doubled_angle_audit']=audit_data(problem,state,refined,cfg['target_reach'])
        report['same_parameter_Pi_refinement']=paired_angle_comparison(problem,state,data,refined)
        report['status']='complete-single-new-core-initial-audit';save_report(out,report)
        return report
    except Exception as exc:
        report.update(status='failed-with-preserved-read-only-diagnostics',error_type=type(exc).__name__,
                      error=str(exc),traceback=traceback.format_exc())
        save_report(out,report)
        return report


def developer_check():
    # Factory geometry/column tests are already separate. This check exercises
    # this driver's real IO, freeze, fixed primitive, diagnostics and save path.
    anchor,selected,*_=artificial_source(1)
    expected_anchor=hashlib.sha256(anchor).hexdigest();expected_selected=hashlib.sha256(selected).hexdigest()
    cfg=default_configuration(True)
    with tempfile.TemporaryDirectory(prefix='core-transport-audit-artificial-',dir='/dev/shm') as directory:
        folder=Path(directory);a=folder/'anchor.json';s=folder/'selected.json';out=folder/'audit.json'
        a.write_bytes(anchor);s.write_bytes(selected)
        report=run_from_files(s,a,out,cfg,expected_selected_sha256=expected_selected,
            expected_anchor_sha256=expected_anchor,artificial=True)
        stored=json.loads(out.read_bytes());summary=json.loads(summary_path(out).read_bytes())
        summary_bound=summary['full_report_bytes_sha256']==hashlib.sha256(out.read_bytes()).hexdigest()
        bad_out=folder/'bad-sha.json'
        bad=run_from_files(s,a,bad_out,cfg,expected_selected_sha256='0'*64,
            expected_anchor_sha256=expected_anchor,artificial=True)
        bad_summary=json.loads(summary_path(bad_out).read_bytes())
        inputs_unchanged=(a.read_bytes()==anchor and s.read_bytes()==selected)
    query=report.get('sparse_complete_query_comparison',{})
    difference=max(query.get('position_two_jet_differences',{'missing':np.inf}).values())
    exact=report.get('target_frozen_state',{}).get('exact_parameter_coefficients',{})
    bits=(len(exact.get('metric',[]))==0 and len(exact.get('u',[]))==81
          and len(exact.get('v',[]))==72 and len(exact.get('height',[]))==9)
    passed=(report['status']=='complete-single-new-core-initial-audit' and report==stored
        and summary_bound and inputs_unchanged and difference<1e-11
        and query.get('common_center_difference')==0 and bits
        and bad['status']=='failed-with-preserved-read-only-diagnostics'
        and bad_summary.get('error_type')=='ValueError'
        and report.get('same_parameter_Pi_refinement',{}).get('same_g_height_base_anchor_and_all_exact_coefficients') is True)
    return {'schema':'core-transport-single-initial-audit-artificial-IO-check-v1','passed':bool(passed),
        'same_driver_IO_and_all_geometry_diagnostic_calls':True,'artificial_inputs_only':True,
        'research_core_not_constructed':True,'optimizer_calls':0,'parameter_steps':0,
        'complete_status':report['status'],'error':report.get('error'),'traceback':report.get('traceback'),
        'full_report_JSON_roundtrip':report==stored,'summary_full_bytes_binding':summary_bound,
        'input_bytes_unchanged':inputs_unchanged,'new_frozen_162_layout':bits,
        'sparse_complete_query_position_two_jet_max_difference':float(difference),
        'sparse_complete_common_center_difference':query.get('common_center_difference'),
        'wrong_input_SHA_writes_failure_summary':bad_summary.get('error_type')=='ValueError',
        'Pi_refinement_is_same_state':report.get('same_parameter_Pi_refinement',{}).get('same_g_height_base_anchor_and_all_exact_coefficients'),
        'sampled_feasibility_is_not_required_for_an_artificial_IO_check':True}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true');p.add_argument('--input',type=Path)
    p.add_argument('--anchor-input',type=Path);p.add_argument('--expected-input-sha256')
    p.add_argument('--expected-anchor-sha256');p.add_argument('--out',type=Path,required=True)
    p.add_argument('--radial-nodes',type=int,default=121);p.add_argument('--angular-nodes',type=int,default=384)
    p.add_argument('--heat-order',type=int,default=32);p.add_argument('--height-angular-nodes',type=int,default=384)
    p.add_argument('--uniform-primitive-panels',type=int,default=120);p.add_argument('--primitive-order',type=int,default=8)
    p.add_argument('--query-quadrature-order',type=int,default=8);args=p.parse_args()
    if args.check_only:
        try:answer=developer_check()
        except Exception as exc:
            answer={'schema':'core-transport-single-initial-audit-artificial-IO-check-v1','passed':False,
                'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc(),
                'artificial_inputs_only':True,'research_geometry_evaluated':False}
        answer['source_files_sha256']=implementation_hashes();atomic_save(args.out,answer)
        print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
        if not answer['passed']:raise SystemExit(1)
        return
    cfg=default_configuration()
    for key in ['radial_nodes','angular_nodes','heat_order','height_angular_nodes',
                'uniform_primitive_panels','primitive_order','query_quadrature_order']:
        cfg[key]=getattr(args,key)
    cfg['doubled_angular_nodes']=2*cfg['angular_nodes']
    # Missing arguments also produce a diagnostic JSON rather than an empty
    # artifact.  Nonexistent sentinel paths are never read before the guard.
    result=run_from_files(args.input or Path('__missing_selected__'),
        args.anchor_input or Path('__missing_anchor__'),args.out,cfg,
        expected_selected_sha256=args.expected_input_sha256,
        expected_anchor_sha256=args.expected_anchor_sha256)
    print(json.dumps({'out':str(args.out),'summary':str(summary_path(args.out)),
                      'status':result['status']}),flush=True)
    if result['status']!='complete-single-new-core-initial-audit':raise SystemExit(1)


if __name__=='__main__':main()

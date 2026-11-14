#!/usr/bin/env python3
"""One localized B=.37 initializer after the paired new-core leading repair.

The four published accepted-height inputs are replayed exactly. No optimizer,
height proposal, new Q column or parameter step is called. All actual geometry
is restricted to this public repository's Actions. --check-only uses the
previous initializer's explicit artificial four-report carrier.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import resource
import tempfile
import time
import traceback

import numpy as np

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_core_transport_audit import audit_data,paired_angle_comparison
from frame_entry_paired_repair_audit import JETS
from frame_height_quartic_joint_audit import prepare_run,InputReplayFailure
from frame_independent_height_solve import state_record,point_values,extremum
from frame_localized_core_initializer import (structure_grid as local_grid,artificial_fixture,
    configuration as local_configuration,summary_path)
from frame_localized_core_entry_repair import (LocalizedLeadingRepairProblem,developer_check as factory_check,
    implementation_hashes as factory_hashes)

SCHEMA='localized-core-paired-leading-repair-one-initial-audit-v1'
PUBLISHED_NEW_METRIC='211c1b193eeb38b50933083821b3d32ed8e7bbf6bd627aab64630dd8a6c22a5e'


def implementation_hashes():
    result=factory_hashes();result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def configuration(artificial=False):
    answer=local_configuration(artificial)
    answer.update(repair_length='81/1000',repair_subdivisions=6 if artificial else 24,
        leading_mean_nodes=64 if artificial else 1024,
        unique_new_field='same additive localized metric, new paired leading scalar and compact-center corrections',
        no_added_Q_column=True,no_optimization_or_height_proposal=True)
    return answer


def structure_grid(problem,cfg):
    radial,theta,prior=local_grid(problem.template,cfg)
    count=int(cfg['repair_subdivisions'])
    if count<4:raise ValueError('at least four exact repair-support subintervals required')
    extra=[problem.left_exact+problem.repair_length_exact*Q(j,count) for j in range(count+1)]
    exact=sorted(set(map(Q,prior['radial_nodes_exact']))|set(extra))
    radial=np.array([float(x) for x in exact])
    if np.any(np.diff(radial)<=0):raise ArithmeticError('rational structure nodes collapse in binary64')
    definition={'schema':'localized-and-leading-repair-complete-structure-grid-v1',
        'previous_localized_grid':prior,'repair_nodes_exact':[str(x) for x in extra],
        'radial_nodes_exact':[str(x) for x in exact],'angular_nodes':len(theta),
        'angular_rule':'theta_j=2*pi*j/N','same_query_independent_common_primitive':True,
        'uniform_sampled_mean_costs_are_only_comparable_on_this_identical_grid':True}
    definition['definition_sha256']=digest(definition)
    return radial,theta,definition


def regions(problem,data):
    value=point_values(problem,data);t,theta=data['radial'],data['theta']
    intervals=[('exact_new_open_core',0.,problem.left),
        ('paired_leading_repair',problem.left,problem.repair_right),
        ('remaining_local_metric_change',problem.repair_right,problem.right),
        ('corresponding_old_body',problem.right,problem.source.support_start),
        ('corresponding_old_natural_patch',problem.source.support_start,problem.source.active_end),
        ('same_physical_open_tail',problem.source.active_end,problem.seed.length)]
    answer={}
    for name,left,right in intervals:
        keep=(t>=left)&(t<=right)
        row={'closed_interval_evaluated':[float(left),float(right)],'radial_nodes':int(keep.sum())}
        if np.any(keep):
            row['extrema']={key:extremum(value[key][keep],t[keep],theta,
                'min' if key=='area' else 'abs' if key in ['E_minus_one','F_over_a'] else 'max')
                for key in ['E_minus_one','F_over_a','metric_operator_error','area','principal_curvature_absolute']}
            row['coordinate_min_sample']=data['X'][keep].min(axis=(0,1)).tolist()
            row['coordinate_max_sample']=data['X'][keep].max(axis=(0,1)).tolist()
            row['center_speed_min_max_sample']=[float(np.min(data['height']['b'][keep])),float(np.max(data['height']['b'][keep]))]
        answer[name]=row
    return {'regions':answer,'shared_interface_rows_intentionally_repeat':True,'all_extrema_sampled_only':True}


def exterior_comparison(problem,old,plain,new):
    t=new['radial'];outside=t>=problem.right;after_repair=t>=problem.repair_right
    if not np.any(outside) or not np.any(after_repair):raise ValueError('the full comparison must contain both exterior regions')
    return {'old_exterior_starts_exact':str(problem.right_exact),
        'unrepaired_local_exterior_starts_exact':str(problem.repair_right_exact),
        'outside_local_sixjet_differences_from_corresponding_old_state':{
            key:float(np.max(abs(new[key][outside]-old[key][outside]))) for key in JETS},
        'outside_repair_sixjet_differences_from_unrepaired_local_state':{
            key:float(np.max(abs(new[key][after_repair]-plain[key][after_repair]))) for key in JETS},
        'outside_repair_center_difference':float(np.max(abs(new['center'][after_repair]-old['center'][after_repair]))),
        'outside_repair_b_jets':{key:float(np.max(abs(new['height'][key][after_repair]-old['height'][key][after_repair])))
                                 for key in ['b','b_s','b_ss']},
        'entire_new_metric_two_jet_differences_from_unrepaired_local_metric':{
            key:float(np.max(abs(new['metric'][key]-plain['metric'][key]))) for key in ['a','a_s','a_ss','K']},
        'single_cap_height_difference':float(new['center'][-1]-old['center'][-1]),
        'unit_tangent_error_sample':float(np.max(abs(np.sum(new['T']**2,axis=-1)-1))),
        'mean_tangent_norm_sample':float(np.max(np.linalg.norm(new['T'].mean(axis=1),axis=-1))),
        'finite_evaluation_differences_do_not_replace_the_exact_exterior_proof':True}


def compact_summary(report,out):
    result={key:report[key] for key in ['schema','status','phase','configuration','source_files_sha256',
        'exact_input_storage','accepted_source_physical_sha256','previous_localized_field_sha256',
        'new_physical_state_sha256','new_complete_metric_sha256','old_height_base_sha256','new_height_base_sha256',
        'leading_mean_evaluation','repair_definition','same_metric_as_previous_localized_design',
        'initial_parameter_bits_unchanged','freeze_preserves_state_and_metric','optimizer_calls','height_proposal_calls',
        'artificial_inputs_only','exterior_identity_comparison','sparse_dense_query_comparison',
        'same_parameter_Pi_refinement','elapsed_seconds','peak_rss_kib_linux','error','input_failure'] if key in report}
    for key in ['old_reference_same_grid_audit','unrepaired_local_same_grid_audit','new_initial_audit','new_doubled_angle_audit']:
        if key in report:result[key]={k:v for k,v in report[key].items() if k!='radial_distribution'}
    for key in ['new_initial_regions','new_doubled_regions']:
        if key in report:result[key]=report[key]
    raw=out.read_bytes();result['full_report']={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    result.update(sampled_only=True,task_complete=False,embedding_or_reach_proved=False,
        higher_Cauchy_jets_not_paid_by_leading_repair=True)
    return result


def save_report(out,report):
    atomic_save(out,report);atomic_save(summary_path(out),compact_summary(report,out))


def run_from_files(args,cfg,*,artificial=False):
    started=time.monotonic();answer={'schema':SCHEMA,'status':'before-four-input-replay',
        'source_files_sha256':implementation_hashes(),'configuration':copy.deepcopy(cfg),
        'artificial_inputs_only':bool(artificial),'optimizer_calls':0,'height_proposal_calls':0,
        'no_parameter_step_no_new_Q_no_metric_design_solve':True}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-started
        answer['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        save_report(args.out,answer)
    save('source-replay-started')
    try:
        answer['phase']='strict-four-input-accepted-height-replay'
        reference,unused,state,prior,receipt,source_cfg=prepare_run(args,artificial=artificial)
        answer.update(source_receipt=receipt,exact_input_storage=receipt['exact_input_storage'],
            accepted_source_state=state_record(reference,state),
            accepted_source_physical_sha256=digest(reference.identity(state)))
        answer['phase']='same-localized-new-metric-and-new-leading-height-base'
        if cfg['doubled_angular_nodes']!=2*cfg['angular_nodes']:raise ValueError('one exact angular doubling required')
        problem=LocalizedLeadingRepairProblem(reference,state,cfg['target_minor'],cfg['local_length'],cfg['repair_length'],
            mean_nodes=cfg['leading_mean_nodes'],artificial=artificial)
        fixed=problem.metric_model(state);identity=problem.identity(state)
        if fixed!=problem.template.metric_model(state):raise ArithmeticError('the leading repair changed the complete new target metric')
        if not artificial and fixed['mathematical_definition_sha256']!=PUBLISHED_NEW_METRIC:
            raise ValueError('new initial audit must retain the exact already published localized complete metric')
        frozen,same=problem.frozen_metric_copy(state)
        if same.tobytes()!=state.tobytes() or frozen.identity(same)!=identity or frozen.metric_model(same)!=fixed:
            raise ArithmeticError('freeze changed the initial coefficients, new field or full metric')
        answer.update(previous_localized_field_sha256=digest(problem.template.identity(state)),
            new_initial_state=state_record(problem,state),new_physical_state_sha256=digest(identity),
            new_complete_metric_sha256=fixed['mathematical_definition_sha256'],
            same_metric_as_previous_localized_design=True,initial_parameter_bits_unchanged=True,
            freeze_preserves_state_and_metric=True,repair_definition=problem.repair_definition,
            leading_mean_evaluation=problem.mean_data(),old_height_base_sha256=digest(reference.height_base_definition),
            new_height_base_sha256=digest(problem.height_base_definition),
            immutable_original_c0_and_accepted_f198_have_separate_provenance_roles=True)
        save('new-family-and-unique-initial-state-defined')
        t,theta,grid=structure_grid(problem,cfg);order=int(cfg['query_quadrature_order']);answer['sampling_grid']=grid
        answer['phase']='same-grid-published-reference-and-unique-repaired-initial-field'
        old=reference.geometry(state,t,theta,order)
        plain=problem.template.geometry_from_reference(state,old)
        new=problem.geometry(state,t,theta,order)
        answer['old_reference_same_grid_audit']=audit_data(reference,state,old,cfg['target_reach'])
        answer['unrepaired_local_same_grid_audit']=audit_data(problem.template,state,plain,cfg['target_reach'])
        answer['new_initial_audit']=audit_data(problem,state,new,cfg['target_reach'])
        answer['new_initial_regions']=regions(problem,new)
        answer['exterior_identity_comparison']=exterior_comparison(problem,old,plain,new)
        save('one-repaired-field-and-same-grid-reference-diagnostics-complete')
        exact=sorted({Q(0),problem.left_exact,problem.repair_right_exact,problem.right_exact,
            problem.seed.length_exact*(1-problem.seed.flat_fraction_exact),problem.seed.length_exact})
        sparse=np.array([float(value) for value in exact]);indices=np.searchsorted(t,sparse)
        if not np.array_equal(t[indices],sparse):raise ArithmeticError('all exact sparse interfaces must be in the full grid')
        small=problem.geometry(state,sparse,theta,order)
        answer['sparse_dense_query_comparison']={'radial_points_exact':[str(x) for x in exact],
            'all_six_position_jet_max_differences':{key:float(np.max(abs(small[key]-new[key][indices]))) for key in JETS},
            'common_center_max_difference':float(np.max(abs(small['center']-new['center'][indices]))),
            'fixed_original_prefix_plus_compact_center_no_query_defined_primitive':True}
        save('query-independent-single-center-interface-audit-complete')
        answer['phase']='same-coefficients-and-new-model-angle-doubling'
        theta2=np.arange(cfg['doubled_angular_nodes'])*2*np.pi/cfg['doubled_angular_nodes']
        double=problem.geometry(state,t,theta2,order)
        if problem.identity(state)!=identity:raise ArithmeticError('evaluation changed the new physical model')
        answer['new_doubled_angle_audit']=audit_data(problem,state,double,cfg['target_reach'])
        answer['new_doubled_regions']=regions(problem,double)
        answer['same_parameter_Pi_refinement']=paired_angle_comparison(problem,state,new,double)
        save('complete-one-localized-leading-repaired-core-initial-audit');return answer
    except Exception as error:
        if isinstance(error,InputReplayFailure) and args.out.exists():
            try:answer['input_failure']=json.loads(args.out.read_text())
            except (OSError,ValueError):pass
        answer['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('failed-with-preserved-initial-only-diagnostics');return answer


def developer_check():
    factory=factory_check()
    with tempfile.TemporaryDirectory(prefix='localized-leading-four-input-toy-',dir='/dev/shm') as folder:
        args=artificial_fixture(Path(folder));args.out=Path(folder)/'leading-audit.json';cfg=configuration(True)
        report=run_from_files(args,cfg,artificial=True);summary=json.loads(summary_path(args.out).read_text())
        binding=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        wrong=copy.copy(args);wrong.expected_height_sha256='0'*64;wrong.out=Path(folder)/'wrong-input.json'
        failure=run_from_files(wrong,cfg,artificial=True)
        rejected=failure['status']=='failed-with-preserved-initial-only-diagnostics' and bool(failure.get('input_failure'))
    outside=report.get('exterior_identity_comparison',{})
    differences=outside.get('outside_local_sixjet_differences_from_corresponding_old_state',{'missing':np.inf})
    query=report.get('sparse_dense_query_comparison',{}).get('all_six_position_jet_max_differences',{'missing':np.inf})
    passed=bool(factory['passed'] and report['status']=='complete-one-localized-leading-repaired-core-initial-audit'
        and report['same_metric_as_previous_localized_design'] and report['initial_parameter_bits_unchanged']
        and report['old_height_base_sha256']!=report['new_height_base_sha256']
        and max(differences.values())<2e-11 and max(query.values())<2e-11
        and outside.get('single_cap_height_difference')==0. and binding and rejected)
    return {'schema':'localized-leading-complete-main-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_evaluated_or_optimized':False,'optimizer_calls':0,'factory_check':factory,
        'full_main_status':report['status'],'full_main_error':report.get('error'),
        'same_localized_g_new_height_base':report.get('same_metric_as_previous_localized_design'),
        'new_and_old_height_base_hashes_differ':report.get('old_height_base_sha256')!=report.get('new_height_base_sha256'),
        'exact_current_coefficients_retained':report.get('initial_parameter_bits_unchanged'),
        'outside_local_sixjet_differences':differences,'sparse_dense_sixjet_differences':query,
        'single_cap_height_difference':outside.get('single_cap_height_difference'),
        'complete_summary_byte_binding':binding,'wrong_height_report_SHA_saves_small_failure':rejected,
        'same_state_angle_refinement':report.get('same_parameter_Pi_refinement'),'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['input','anchor-input','short-audit','height-audit']:parser.add_argument('--'+name,type=Path)
    for name in ['input','anchor','short','height']:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:answer=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':'localized-leading-main-development-error-v1','artificial_inputs_only':True,
                'passed':False,'source_files_sha256':implementation_hashes(),
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        answer['source_files_sha256']=implementation_hashes();atomic_save(args.out,answer)
        print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
        if not answer['passed']:raise SystemExit(1)
        return
    answer=run_from_files(args,configuration())
    print(json.dumps({'out':str(args.out),'status':answer['status']}),flush=True)
    if answer['status']!='complete-one-localized-leading-repaired-core-initial-audit':raise SystemExit(1)


if __name__=='__main__':main()

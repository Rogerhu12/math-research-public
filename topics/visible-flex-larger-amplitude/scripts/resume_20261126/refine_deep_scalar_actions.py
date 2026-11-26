#!/usr/bin/env python3
"""Exact SAME fixed-deep-scalar transfer followed by its complete fine solve.

The mathematical deep profile, physical eta, cap radius carrier, mother
norm, spectral parameters and actual parent stopping threshold are kept.
R676's pure restriction and position kernels are used on the new profile.
All actual parent/trial/active/final addresses are retained. Fine Phi is
also read on the literal parent measure and parent a carriers from the
already computed fine residual. No coarse field/J fixture is evaluated.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys

HISTORY_SHA='4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
POSITION_LAUNCHER_SHA='e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4'
TRANSFER_SHA='5f1b285fd021971cdbeb6680d28b8ef0c5ec24cdea5f9a0f830b3e87aebc06df'
LAUNCHER_SHA='6b06187c0bd5957ff0c1658f6da7a4c7077a6b9c59ed948a5a23881b1379cd75'
BASE_DRIVER_SHA='d3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95'
FINE_DRIVER_SHA='1745cfae02b7ad0335577a340cfee52f179e1f27508c8d20ef1487abec00f154'


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def load(name,path,digest):
    if sha(path)!=digest:raise ValueError('Changed complete source '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def write_json(path,value):
    path=Path(path);temp=path.with_name(path.name+'.partial')
    temp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n');temp.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','parent-report','bundle','carrier','node-report','scalar-input','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--manifest',type=Path,action='append',required=True)
    p.add_argument('--radial-factor',type=int,choices=(1,2),default=2)
    p.add_argument('--modes',type=int)
    p.add_argument('--angles',type=int)
    p.add_argument('--directions',type=int,default=2)
    p.add_argument('--maxiter',type=int,default=64)
    p.add_argument('--damping',type=float)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--scalar-admission-seconds',type=float,default=300.)
    p.add_argument('--scalar-integral-tolerance',default='1e-18')
    p.add_argument('--scalar-tail-cutoff',default='1/8')
    p.add_argument('--amplitude-budget-evidence',type=Path)
    a=p.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Physical same-deep-scalar refinement belongs only in this public repository Actions')
    if min(a.directions,a.maxiter,a.stage_block)<1:
        raise ValueError('Use positive actual complete solver budgets')
    repo,work,output=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    here=Path(__file__).resolve().parent
    old=repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    parent=json.loads(a.parent_report.read_text())
    schemas={'complete-fixed-deep-scalar-with-held-amplitude-budgets-v1':BASE_DRIVER_SHA,
        'complete-refined-fixed-deep-scalar-with-held-amplitude-budgets-v1':FINE_DRIVER_SHA}
    if (parent.get('complete') is not True
            or schemas.get(parent.get('schema'))!=parent.get('source_sha256')
            or parent.get('final_bundle_sha256')!=sha(a.bundle)
            or parent.get('observation_carrier_sha256')!=sha(a.carrier)
            or parent.get('exact_tail_node_report_sha256')!=sha(a.node_report)
            or parent.get('exact_tail_scalar_input_sha256')!=sha(a.scalar_input)):
        raise ValueError('Refine the actual completed byte-bound same-target parent and its current inputs')
    fixed=parent['fixed_scalar_metric'];identity=fixed['identity_sha256']
    model=parent['exact_tail_context']['definition']
    if (fixed.get('target_fixed_before_first_direction') is not True
            or fixed.get('moving_mean_projection') is not False
            or fixed.get('all_metric_mean_constraints_retained') is not True
            or model.get('profile_identity_sha256')!=identity
            or model.get('profile_definition')!=fixed['exact_profile_definition']
            or model.get('schema')!='deep-valley-fixed-scalar-fullclosed-lift-v1'
            or model.get('lambda_value')!=1.):
        raise ValueError('Do not replace the exact scalar profile while refining its solve')
    target=parent['target'];spectral=parent['final_statistics']['spectral']
    selected=parent['selected_scalar_objective_key']
    if (not math.isfinite(target) or target<=0
            or selected not in ('centered_phi_normalized','phi_normalized')):
        raise ValueError('Preserve the actual explicit fixed-g stopping threshold and spectral evaluator')
    source_N=int(parent['N']);new_N=source_N if a.angles is None else a.angles
    new_M=int(parent['M']) if a.modes is None else a.modes
    multiplier=new_N//source_N
    if (new_M<parent['M'] or new_N<=4*new_M or new_N%4
            or new_N%source_N or multiplier<1 or multiplier&(multiplier-1)
            or (a.radial_factor==1 and new_M==parent['M'] and new_N==source_N)):
        raise ValueError('Declare a true refinement preserving every old mode and angle')
    mu=parent.get('final_damping') if a.damping is None else a.damping
    if mu is None or not math.isfinite(mu) or mu<=0:
        raise ValueError('Use the actual final adaptive damping or an explicit positive continuation value')
    budgets=parent['amplitude_design_constraints']['budgets']
    amplitude=parent['final_amplitude_filter']
    amplitude_limits=dict(radius=amplitude.get('selected_radius_limit',2),
        distance=amplitude.get('selected_distance_location_limit',4),
        active_band=amplitude.get('working_active_band',.025))
    parent_geometry_passed=bool(parent.get('final_curvature_filter',{}).get('passed'))
    parent_amplitude_passed=bool(amplitude.get('passed'))
    # These fields are recorded, not a new fixture or a replacement for the
    # complete fine driver's own actual initial and per-trial screen.
    source=here/'refine_fixed_deep_scalar.py'
    launcher=here/'launch_refined_deep_scalar_actions.py'
    fine_driver=here/'fullclosed_refined_deep_scalar_amplitude_qp.py'
    base_driver=here/'fullclosed_deep_scalar_amplitude_qp.py'
    history=old/'launch_refinement_from_full_report.py'
    position_source=here/'launch_mean_metric_design_actions.py'
    for path,digest in ((source,TRANSFER_SHA),(launcher,LAUNCHER_SHA),(fine_driver,FINE_DRIVER_SHA),
            (base_driver,BASE_DRIVER_SHA),(history,HISTORY_SHA)):
        if sha(path)!=digest:raise ValueError('Changed complete refinement dependency '+str(path))
    positions=load('_fixed_deep_refinement_complete_parent_locations',position_source,POSITION_LAUNCHER_SHA)
    for path in a.manifest:
        payload=json.loads(path.read_text())
        if payload.get('carrier_sha256',payload.get('observation_carrier_sha256'))!=sha(a.carrier):
            raise ValueError('Supply only complete extra location records on this actual parent carrier')
    solve_output=output.with_name(output.name+'-solve')
    if output.exists() or solve_output.exists():
        raise FileExistsError('Use fresh actual refinement/solve output paths')
    output.mkdir(parents=True,exist_ok=False)
    positions_path=output/'parent-inputs'/'complete-parent-positions.json'
    all_positions=positions.complete_positions(a,history,positions_path)
    transfer_output=output/'transfer'
    transfer=[sys.executable,'-u',str(source),'--repo',str(repo),
        '--bundle',str(a.bundle.resolve()),'--carrier',str(a.carrier.resolve()),
        '--node-report',str(a.node_report.resolve()),'--scalar-input',str(a.scalar_input.resolve()),
        '--manifest',str(positions_path),'--radial-factor',str(a.radial_factor),'--modes',str(new_M),
        '--source-angles',str(source_N),'--angles',str(new_N),'--stage-block',str(a.stage_block),
        '--scalar-admission-seconds',str(a.scalar_admission_seconds),
        '--scalar-integral-tolerance',a.scalar_integral_tolerance,'--scalar-tail-cutoff',a.scalar_tail_cutoff,
        '--outdir',str(transfer_output)]
    plan_path=output/'refinement-plan.json'
    plan=dict(schema='actual-same-fixed-deep-scalar-complete-refinement-v1',
        source_sha256=sha(__file__),source_commit=subprocess.check_output(
            ['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        execution={key:os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')},
        sources=dict(transfer=record(source),launcher=record(launcher),fine_driver=record(fine_driver),
            base_driver=record(base_driver),history=record(history),position_launcher=record(position_source)),
        actual_parent_report=record(a.parent_report),actual_parent_bundle=record(a.bundle),
        fixed_scalar_metric_identity_sha256=identity,exact_profile_definition=fixed['exact_profile_definition'],
        actual_parent_model=model,all_parent_positions=all_positions,
        parent_M=parent['M'],refined_M=new_M,parent_N=source_N,refined_N=new_N,
        radial_factor=a.radial_factor,initial_damping=mu,parent_final_damping=parent['final_damping'],
        damping_explicitly_changed=a.damping is not None and a.damping!=parent['final_damping'],
        spectral_parameters={key:spectral[key] for key in ('p','epsilon','scale')},
        selected_scalar_objective_key=selected,actual_parent_stopping_threshold=target,
        parent_stopping_threshold_preserved=True,stopping_threshold_not_README_floor_claim=True,
        amplitude_budgets=budgets,parent_geometry_screen_passed=parent_geometry_passed,
        parent_amplitude_screen_passed=parent_amplitude_passed,
        original_geometry_rows_not_replaced=True,parent_certificate_inherited=False,
        coarse_parent_field_or_J_fixture=False,transfer_command=transfer,
        transfer_returned=False,solve_returned=False,topic_completion_claimed=False)
    write_json(plan_path,plan)
    env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    try:
        subprocess.run(transfer,cwd=repo,env=env,check=True)
        transfer_report=transfer_output/'refinement-report.json'
        r=json.loads(transfer_report.read_text())
        if (r.get('source_sha256')!=TRANSFER_SHA
                or r.get('fixed_scalar_metric_identity_sha256')!=identity
                or r.get('nonlinear_solve_performed') is not False
                or r.get('finite_metric_or_geometry_readout_performed') is not False
                or r['refined_model']['profile_definition']!=fixed['exact_profile_definition']):
            raise ValueError('The actual transfer must retain the complete exact fixed profile')
        refined=r['outputs'];fine_model=r['refined_model']
        solve=[sys.executable,'-u',str(launcher),'--repo',str(repo),'--work',str(work),
            '--refinement-report',str(transfer_report),'--bundle',refined['bundle']['path'],
            '--carrier',refined['carrier']['path'],'--node-report',refined['node_report']['path'],
            '--scalar-input',str(a.scalar_input.resolve()),'--manifest',refined['permanent_locations']['path'],
            '--comparison-parent-report',str(a.parent_report.resolve()),
            '--comparison-parent-carrier',str(a.carrier.resolve()),
            '--eta-start-node',str(fine_model['eta_start_node']),
            '--angles',str(new_N),'--stage-block',str(a.stage_block),
            '--directions',str(a.directions),'--maxiter',str(a.maxiter),'--damping',str(mu),
            '--target',str(target),'--outdir',str(solve_output)]
        parameters={'spectral-p':spectral['p'],'spectral-epsilon':spectral['epsilon'],
            'spectral-scale':spectral['scale'],'legacy-fraction':parent['radial_weights']['legacy_fraction'],
            'angular-transition':parent['angular_norm']['nu_c'],'low-modes':parent['coarse_low_modes'],
            'line-trials':parent['max_line_trials'],'reach-ratio':parent['requested_reach_ratio'],
            'reach-safety-factor':parent['numerical_reach_safety_factor'],
            'active-rows':parent['active_max_rows'],'active-band':parent['active_band'],
            'active-block-columns':parent['active_block_columns'],
            'active-rank-tolerance':parent['active_rank_tolerance'],
            'active-top-curvature':parent['active_top_curvature'],'active-top-radius':parent['active_top_radius'],
            'qp-atol':parent['qp_atol'],'qp-rtol':parent['qp_rtol'],
            'qp-feasibility-tolerance':parent['qp_feasibility_tolerance'],
            'qp-row-rank-tolerance':parent['qp_row_rank_tolerance'],
            'coarse-moment-stage-block':parent['scalar_coarse_source_binding']['moment_stage_block'],
            'marked-diameter-budget':budgets['marked_diameter_budget'],
            'witness-lower-budget':budgets['witness_lower_budget'],
            'amplitude-height-floor':budgets['height_floor'],
            'amplitude-top-radius':amplitude_limits['radius'],
            'amplitude-top-distance':amplitude_limits['distance'],
            'amplitude-active-band':amplitude_limits['active_band'],
            'scalar-admission-seconds':a.scalar_admission_seconds,
            'scalar-integral-tolerance':a.scalar_integral_tolerance,'scalar-tail-cutoff':a.scalar_tail_cutoff}
        if parent['requested_coarse_centers'] is not None:
            parameters['coarse-centers']=','.join(str(value) for value in parent['requested_coarse_centers'])
        if parent['sampled_curvature_cap'] is not None:parameters['curvature-cap']=parent['sampled_curvature_cap']
        if a.amplitude_budget_evidence is not None:parameters['amplitude-budget-evidence']=a.amplitude_budget_evidence.resolve()
        for key,value in parameters.items():solve.extend(['--'+key,str(value)])
        if selected=='phi_normalized':solve.append('--uncentered-objective')
        plan.update(transfer_returned=True,actual_transfer_report=record(transfer_report),
            actual_refined_seed=refined['bundle'],exact_refined_model=fine_model,
            actual_refined_eta_start_node=fine_model['eta_start_node'],
            common_parent_phi_comparison_uses_parent_literal_a=True,solve_command=solve)
        write_json(plan_path,plan)
        subprocess.run(solve,cwd=repo,env=env,check=True)
        result_path=solve_output/'report.json';result=json.loads(result_path.read_text())
        if (result.get('source_sha256')!=FINE_DRIVER_SHA or result.get('complete') is not True
                or result['fixed_scalar_metric']['identity_sha256']!=identity
                or result['common_parent_measure_comparison']['parent_report_sha256']!=sha(a.parent_report)):
            raise ValueError('The actual complete fine solve changed its fixed target or comparison parent')
        plan.update(solve_returned=True,actual_solve_report=record(result_path),
            actual_final_bundle_sha256=result['final_bundle_sha256'],
            refined_solver_initial_statistics=result['initial'],final_fine_statistics=result['final_statistics'],
            final_known_point_filter=result['final_curvature_filter'],final_amplitude_filter=result['final_amplitude_filter'],
            actual_direction_count=result['actual_direction_count'],
            actual_accepted_direction_count=result['actual_accepted_direction_count'],
            zero_direction_exit=result['zero_direction_exit'],
            actual_fixed_grid_max_change=result['actual_fixed_grid_max_change'],
            actual_common_parent_max_change=result['actual_common_parent_max_change'],
            final_common_parent_measure=result['final_statistics']['common_parent_measure'],
            numerical_floor_or_continued_decrease_not_inferred_from_target_flag=True,
            fixed_g_refinement_convergence_claimed=False,source_or_target_identity_changed=False)
        write_json(plan_path,plan)
    except Exception as error:
        plan.update(actual_failure_type=type(error).__name__,actual_failure=str(error))
        write_json(plan_path,plan);raise
    print(json.dumps(dict(plan=record(plan_path),fixed_scalar_metric_identity_sha256=identity,
        final_bundle_sha256=plan['actual_final_bundle_sha256'],
        fine_max=plan['final_fine_statistics']['max_relative_gram'],
        parent_measure=plan['final_common_parent_measure'],
        actual_direction_count=plan['actual_direction_count'],
        actual_accepted_direction_count=plan['actual_accepted_direction_count'],
        zero_direction_exit=plan['zero_direction_exit'],fixed_g_refinement_convergence_claimed=False),allow_nan=False),flush=True)


if __name__=='__main__':main()

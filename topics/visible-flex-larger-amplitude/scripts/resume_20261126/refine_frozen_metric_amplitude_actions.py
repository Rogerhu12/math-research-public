#!/usr/bin/env python3
"""Exact refinement followed by a complete SAME frozen-target/amplitude solve.

Reuse R676 transfer-only: no old-target p8 readout is evaluated or relabelled.
The entire current parent position history is first collected exactly and
then remapped by that proved transfer. The new fixed-target driver reads
its own fine-grid objective and an additional identical parent measure
from the same residual array. No cross-measure Phi subtraction is made.
"""
import argparse
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys

HISTORY_SHA='4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
MEAN_LAUNCHER_SHA='e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4'
TRANSFER_SHA='2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a'


def sha(path):
    import hashlib
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda:stream.read(1<<20),b''):h.update(part)
    return h.hexdigest()


def load(name,path,digest=None):
    if digest is not None and sha(path)!=digest:raise ValueError('Changed explicit source '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','parent-report','bundle','carrier','node-report','scalar-input',
                'frozen-target-manifest','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--manifest',type=Path,action='append',required=True)
    p.add_argument('--radial-factor',type=int,choices=(1,2),default=2)
    p.add_argument('--modes',type=int)
    p.add_argument('--angles',type=int)
    p.add_argument('--directions',type=int,default=2)
    p.add_argument('--maxiter',type=int,default=64)
    p.add_argument('--damping',type=float)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--fixed-solver-launcher',type=Path)
    p.add_argument('--target',type=float)
    p.add_argument('--marked-diameter-budget',type=float)
    p.add_argument('--witness-lower-budget',type=float)
    p.add_argument('--amplitude-height-floor',type=float)
    p.add_argument('--amplitude-budget-evidence',type=Path)
    for key in ('bundle','node-report','scalar-input','observation-carrier','reference-carrier'):
        p.add_argument('--target-'+key,type=Path)
    a=p.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('All physical refinement and frozen-target solving require this public repository Actions')
    if min(a.directions,a.maxiter,a.stage_block)<1:raise ValueError('Use positive complete solver budgets')
    repo,work,output=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    old=repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    here=Path(__file__).resolve().parent
    history=old/'launch_refinement_from_full_report.py'
    helper_path=here/'launch_mean_metric_design_actions.py'
    helper=load('frozen_refine_complete_history',helper_path,MEAN_LAUNCHER_SHA)
    if sha(history)!=HISTORY_SHA:raise ValueError('Keep the published exact full position history')
    target_source=here/'frozen_mean_metric.py'
    target_module=load('frozen_refine_manifest',target_source)
    target=target_module.read_manifest(a.frozen_target_manifest)
    frozen_sha=sha(a.frozen_target_manifest)
    parent=json.loads(a.parent_report.read_text())
    if parent.get('complete') is not True or parent.get('final_bundle_sha256')!=sha(a.bundle):
        raise ValueError('Refine the actual completed full-parent final bundle')
    fixed=parent.get('frozen_metric_target') or {}
    design=parent.get('mean_metric_design') or {}
    is_fixed=fixed.get('target_identity_sha256')==target['target_identity_sha256']
    is_freeze_member=(parent['final_bundle_sha256']==target['inputs']['bundle']['sha256']
        and design.get('averaging')==target['averaging']
        and design.get('finite_angles')==target['full_angles'])
    if not is_fixed and not is_freeze_member:
        raise ValueError('Do not replace or redefine the target during refinement')
    if is_fixed:
        solve_target=parent['target']
        if a.target is not None and a.target!=solve_target:
            raise ValueError('This refinement keeps the fixed-parent stopping threshold; begin a separate declared continuation to change it')
    else:
        if a.target is None:
            raise ValueError('The design threshold is not a fixed-g convergence tolerance; explicitly declare --target for the first fixed-g solve')
        solve_target=a.target
    if not math.isfinite(solve_target) or solve_target<=0:
        raise ValueError('Use an explicit finite positive fixed-target stopping threshold')
    selected_objective=parent.get('selected_scalar_objective_key','centered_phi_normalized')
    if selected_objective not in ('centered_phi_normalized','phi_normalized'):
        raise ValueError('Keep a declared spectral scalar evaluator')
    coarse_binding=parent.get('fixed_coarse_source_binding',{})
    coarse_choice=coarse_binding.get('selected_preconditioner','coarse')
    coarse_stage_block=coarse_binding.get('stage_block',8)
    old_amplitude=parent.get('amplitude_design_constraints') or {}
    old_budgets=old_amplitude.get('budgets')
    selected_budgets={}
    for cli,key in (('marked_diameter_budget','marked_diameter_budget'),
                    ('witness_lower_budget','witness_lower_budget'),
                    ('amplitude_height_floor','height_floor')):
        value=getattr(a,cli)
        if old_budgets is not None:
            if value is not None and value!=old_budgets[key]:
                raise ValueError('This refinement keeps its existing fixed amplitude budgets')
            value=old_budgets[key]
        if value is None or not math.isfinite(value):
            raise ValueError('The first amplitude-protected refinement needs three explicit finite amplitude budgets')
        selected_budgets[key]=value
    if old_budgets is not None and parent.get('final_amplitude_filter',{}).get('passed') is not True:
        raise ValueError('The actual protected parent failed its necessary amplitude screen; no restoration or inherited acceptance is asserted')
    actual_amplitude_screen=parent.get('final_amplitude_filter') or {}
    amplitude_limits=dict(radius=actual_amplitude_screen.get('selected_radius_limit',2),
        distance=actual_amplitude_screen.get('selected_distance_location_limit',4),
        active_band=actual_amplitude_screen.get('working_active_band',.025))
    if parent.get('final_curvature_filter',{}).get('passed') is not True:
        raise ValueError('This feasible-QP branch needs an actually qualifying parent, not a phase-I claim')
    stats=parent.get('final_statistics') or parent.get('current') or parent['initial']
    spectral=stats['spectral']
    mu=parent.get('final_damping') if a.damping is None else a.damping
    if mu is None or not math.isfinite(mu) or mu<=0:raise ValueError('Need an actual positive declared damping')
    source_N=int(parent['N']);new_N=source_N if a.angles is None else a.angles
    new_M=int(parent['M']) if a.modes is None else a.modes
    if (new_M<parent['M'] or new_N<source_N or new_N%source_N
            or (new_N//source_N)&(new_N//source_N-1)):
        raise ValueError('Keep every original Fourier variable and angle in an actual refinement')
    if a.radial_factor==1 and new_M==parent['M'] and new_N==source_N:
        raise ValueError('Declare an actual radial, M, or N refinement')
    transfer_source=old/'refine_fixed_g_fullclosed.py'
    if sha(transfer_source)!=TRANSFER_SHA:raise ValueError('Keep the already proved R676 exact transfer')
    launcher=(a.fixed_solver_launcher or here/'launch_frozen_metric_amplitude_actions.py').resolve()
    solve_output=output.with_name(output.name+'-solve')
    if output.exists() or solve_output.exists():raise FileExistsError('Use a new actual refinement budget directory')
    output.mkdir(parents=True)
    position_path=output/'parent-inputs'/'complete-parent-positions.json'
    position_record=helper.complete_positions(a,history,position_path)
    transfer_output=output/'transfer'
    transfer=[sys.executable,'-u',str(transfer_source),'--repo',str(repo),
        '--bundle',str(a.bundle.resolve()),'--carrier',str(a.carrier.resolve()),
        '--node-report',str(a.node_report.resolve()),'--scalar-input',str(a.scalar_input.resolve()),
        '--manifest',str(position_path),'--radial-factor',str(a.radial_factor),'--modes',str(new_M),
        '--source-angles',str(source_N),'--angles',str(new_N),'--stage-block',str(a.stage_block),
        '--transfer-only','--outdir',str(transfer_output)]
    plan_path=output/'refinement-plan.json'
    plan=dict(schema='actual-same-frozen-target-and-amplitude-refinement-v1',
        source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        github_run_id=os.environ.get('GITHUB_RUN_ID'),source_sha256=sha(__file__),
        source_sha256_by_role=dict(transfer=TRANSFER_SHA,history=HISTORY_SHA,
            complete_history_launcher=MEAN_LAUNCHER_SHA,frozen_target=sha(target_source),fixed_launcher=sha(launcher)),
        frozen_target_identity_sha256=target['target_identity_sha256'],
        frozen_target_manifest_sha256=frozen_sha,existing_target_redefined=False,
        amplitude_budgets=selected_budgets,existing_amplitude_budgets_preserved=old_budgets is not None,
        original_geometry_rows_not_replaced=True,
        actual_parent_report_sha256=sha(a.parent_report),actual_parent_bundle_sha256=sha(a.bundle),
        complete_parent_positions=position_record,
        parent_M=parent['M'],refined_M=new_M,parent_N=source_N,refined_N=new_N,
        radial_factor=a.radial_factor,initial_damping=mu,transfer_command=transfer,
        fixed_solve_target=solve_target,design_threshold_not_relabelled_as_original_tolerance=True,
        spectral_parameters_preserved=True,selected_scalar_objective_key=selected_objective,
        fixed_parent_stopping_threshold_preserved=is_fixed,
        declared_preconditioner=coarse_choice,coarse_moment_stage_block=coarse_stage_block,
        physical_transfer_only=True,old_original_metric_readout_used=False,
        solve_returned=False,topic_completion_claimed=False)
    def save():plan_path.write_text(json.dumps(plan,indent=2,allow_nan=False)+'\n')
    save()
    env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    try:
        subprocess.run(transfer,cwd=repo,env=env,check=True)
        transfer_report=transfer_output/'refinement-report.json'
        r=json.loads(transfer_report.read_text())
        if r['source_sha256']!=TRANSFER_SHA or r['finite_readout_performed']:
            raise ValueError('The exact transfer unexpectedly ran an old-target numerical readout')
        refined=r['outputs'];model=r['refined_model']
        solve=[sys.executable,'-u',str(launcher),'--repo',str(repo),'--work',str(work),
            '--transfer-report',str(transfer_report),'--bundle',refined['bundle']['path'],
            '--carrier',refined['carrier']['path'],'--node-report',refined['node_report']['path'],
            '--scalar-input',str(a.scalar_input.resolve()),'--manifest',refined['permanent_locations']['path'],
            '--frozen-target-manifest',str(a.frozen_target_manifest.resolve()),
            '--comparison-parent-report',str(a.parent_report.resolve()),
            '--comparison-parent-carrier',str(a.carrier.resolve()),
            '--eta-start-node',str(model['eta_start_node']),'--lambda-value',str(model['lambda_value']),
            '--angles',str(new_N),'--stage-block',str(a.stage_block),
            '--damping',str(mu),'--directions',str(a.directions),'--maxiter',str(a.maxiter),
            '--active-rows',str(parent['active_max_rows']),
            '--qp-atol',str(parent['qp_atol']),'--qp-rtol',str(parent['qp_rtol']),
            '--reach-safety-factor',str(parent['numerical_reach_safety_factor']),
            '--active-band',str(parent['active_band']),
            '--spectral-p',str(spectral['p']),'--spectral-epsilon',str(spectral['epsilon']),
            '--spectral-scale',str(spectral['scale']),'--target',str(solve_target),
            '--coarse-preconditioner',coarse_choice,'--coarse-moment-stage-block',str(coarse_stage_block),
            '--outdir',str(solve_output)]
        solve.extend(['--marked-diameter-budget',str(selected_budgets['marked_diameter_budget']),
            '--witness-lower-budget',str(selected_budgets['witness_lower_budget']),
            '--amplitude-height-floor',str(selected_budgets['height_floor']),
            '--amplitude-top-radius',str(amplitude_limits['radius']),
            '--amplitude-top-distance',str(amplitude_limits['distance']),
            '--amplitude-active-band',str(amplitude_limits['active_band'])])
        if a.amplitude_budget_evidence is not None:
            solve.extend(['--amplitude-budget-evidence',str(a.amplitude_budget_evidence.resolve())])
        if selected_objective=='phi_normalized':solve.append('--uncentered-objective')
        for key in ('bundle','node_report','scalar_input','observation_carrier','reference_carrier'):
            value=getattr(a,'target_'+key)
            if value is not None:solve.extend(['--target-'+key.replace('_','-'),str(value.resolve())])
        plan.update(transfer_returned=True,actual_transfer_report_sha256=sha(transfer_report),
            actual_refined_seed_sha256=refined['bundle']['sha256'],solve_command=solve,
            exact_transferred_model=model)
        save()
        if sha(a.frozen_target_manifest)!=frozen_sha:raise ValueError('The frozen target changed during transfer')
        subprocess.run(solve,cwd=repo,env=env,check=True)
        result=json.loads((solve_output/'report.json').read_text())
        if result['frozen_metric_target']['target_identity_sha256']!=target['target_identity_sha256']:
            raise ValueError('The actual solver changed the target identity')
        plan.update(solve_returned=True,actual_solve_report_sha256=sha(solve_output/'report.json'),
            actual_final_bundle_sha256=result['final_bundle_sha256'],
            final_fine_grid_statistics=result['final_statistics'],
            final_known_point_filter=result['final_curvature_filter'],
            final_amplitude_filter=result['final_amplitude_filter'],
            actual_direction_count=result['actual_direction_count'],
            actual_accepted_direction_count=result['actual_accepted_direction_count'],
            zero_direction_exit=result['zero_direction_exit'],
            actual_fixed_grid_max_change=result['actual_fixed_grid_max_change'],
            refined_solver_initial_statistics=result['initial'],
            numerical_floor_or_continued_decrease_not_inferred_from_target_flag=True,
            source_or_target_identity_changed=False)
        save()
    except Exception as error:
        plan.update(actual_failure_type=type(error).__name__,actual_failure=str(error))
        save();raise
    print(json.dumps(dict(plan=str(plan_path),plan_sha256=sha(plan_path),
        frozen_target_identity_sha256=target['target_identity_sha256'],
        final_bundle_sha256=plan['actual_final_bundle_sha256'],
        final_metric=plan['final_fine_grid_statistics']['max_relative_gram'],
        actual_direction_count=plan['actual_direction_count'],
        actual_accepted_direction_count=plan['actual_accepted_direction_count'],
        zero_direction_exit=plan['zero_direction_exit'],
        common_parent=plan['final_fine_grid_statistics'].get('common_parent_measure'),
        final_known_point_filter=plan['final_known_point_filter'],
        final_amplitude_filter=plan['final_amplitude_filter'],
        continuous_amplitude_certified=False,
        refinement_convergence_certified=False,topic_completion_claimed=False)),flush=True)


if __name__=='__main__':main()

#!/usr/bin/env python3
# Complete launcher derived from the repaired amplitude v2 argv/position pipeline.
# Original complete launcher SHA256: 010aeb981fe1c4f17f31d6bb6af831cd1879ca696d79c2cb9e87a6883d8ecd25
"""Run complete mean/amplitude PCG with one explicitly inward complete-row SOC.

The entire original geometry row set is retained. This branch appends full
original-free-coordinate diameter/distance/cap/height inequalities and true
all-grid/all-known-location screening before any accepted nonlinear trial.
Finite budgets do not replace same-field continuous amplitude or reach proof.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys

FACE_LAUNCHER_SHA='5d0801c363def30b1a65c331363e5fc6a28a7de87e4354341e8d0566424640f4'
DESIGN_LAUNCHER_SHA='e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4'
DRIVER_SHA='3adccbbef31545df8c33bc5144da6db4adb34549300c60da4de6789602b38a11'
BASE_DRIVER_SHA='970f03adc4b11a85f13de9e9d13dcbcb7fef0dce4ab79c0d17b62bd0ed34c775'
DERIVER_SHA='e731954fa5e62ec7b6bb7098f993fcc00ba03e9e924e15f7ea1d64472419d0a4'
SOC_SHA='734c1fcc80006e7da52ea7aa8cda4dea02e75714b4b550c20f64dae9cfe67061'
PROJECTION_SHA='a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
ROWS_SHA='d494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'
SCREEN_SHA='e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f'


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda:stream.read(1<<20),b''):h.update(part)
    return h.hexdigest()


def load_bound(name,path,digest):
    if sha(path)!=digest:raise ValueError('Changed complete source '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def replace(command,flag,value):
    if command.count(flag)!=1:raise ValueError('Expected one explicit flag '+flag)
    command[command.index(flag)+1]=str(value)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','bundle','parent-report','carrier','node-report','scalar-input','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--manifest',type=Path,action='append',required=True)
    p.add_argument('--averaging',choices=('physical','material'),required=True)
    damping_group=p.add_mutually_exclusive_group(required=True)
    damping_group.add_argument('--damping',type=float)
    damping_group.add_argument('--damping-from-parent',action='store_true')
    p.add_argument('--marked-diameter-budget',type=float,required=True)
    p.add_argument('--witness-lower-budget',type=float,required=True)
    p.add_argument('--amplitude-height-floor',type=float,required=True)
    p.add_argument('--amplitude-top-radius',type=int,default=2)
    p.add_argument('--amplitude-top-distance',type=int,default=4)
    p.add_argument('--amplitude-active-band',type=float,default=.025)
    p.add_argument('--amplitude-budget-evidence',type=Path)
    p.add_argument('--eta-start-node',type=int,required=True)
    p.add_argument('--lambda-value',type=float,required=True)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--directions',type=int,default=2)
    p.add_argument('--maxiter',type=int,default=64)
    p.add_argument('--active-rows',type=int,default=192)
    p.add_argument('--qp-atol',type=float,default=0.)
    p.add_argument('--qp-rtol',type=float,default=1e-6)
    p.add_argument('--reach-safety-factor',type=float,default=.992)
    p.add_argument('--active-band',type=float,default=.025)
    p.add_argument('--coarse-centers')
    p.add_argument('--coarse-moment-stage-block',type=int,default=8)
    p.add_argument('--spectral-p',type=int,default=4)
    p.add_argument('--spectral-epsilon',type=float,default=.001)
    p.add_argument('--spectral-scale',type=float,default=.05)
    p.add_argument('--target',type=float,default=5e-7)
    p.add_argument('--driver',type=Path)
    p.add_argument('--base-driver',type=Path)
    p.add_argument('--source-deriver',type=Path)
    p.add_argument('--typed-soc-source',type=Path)
    p.add_argument('--soc-projection-source',type=Path)
    p.add_argument('--soc-tau',type=float,default=0.)
    p.add_argument('--soc-inward-fraction',type=float,default=.125)
    p.add_argument('--soc-separation',choices=('none','rejected-extrema'),default='rejected-extrema')
    p.add_argument('--amplitude-rows-source',type=Path)
    p.add_argument('--amplitude-screen-source',type=Path)
    p.add_argument('--centered-loss-source',type=Path)
    p.add_argument('--uncentered-objective',action='store_true')
    p.add_argument('--print-command',action='store_true')
    a=p.parse_args()
    damping_origin=dict(kind='explicit caller value',value=a.damping)
    if a.damping_from_parent:
        actual_parent=json.loads(a.parent_report.read_text())
        if (actual_parent.get('complete') is not True
                or actual_parent.get('final_bundle_sha256')!=sha(a.bundle)):
            raise ValueError('Parent-sourced damping requires this complete actual parent report and final bundle')
        parent_spectral=actual_parent['final_statistics']['spectral']
        if (actual_parent['mean_metric_design']['averaging']!=a.averaging
                or any(parent_spectral[key]!=value for key,value in
                    (('p',a.spectral_p),('epsilon',a.spectral_epsilon),('scale',a.spectral_scale)))):
            raise ValueError('Parent-sourced damping keeps the same actual mean/spectral functional units')
        a.damping=float(actual_parent['final_damping'])
        if not math.isfinite(a.damping) or a.damping<=0:
            raise ValueError('The actual parent did not return a finite positive damping')
        damping_origin=dict(kind='actual bound parent final_damping',value=a.damping,
            parent_report_sha256=sha(a.parent_report),parent_final_bundle_sha256=sha(a.bundle),
            parent_solver_sha256=actual_parent['source_sha256'],
            mean_and_spectral_units_retained=True)
    if (min(a.amplitude_top_radius,a.amplitude_top_distance,a.stage_block,a.directions,a.maxiter,a.active_rows)<1
            or a.angles<4 or a.angles%4
            or not all(math.isfinite(v) for v in (a.marked_diameter_budget,a.witness_lower_budget,
                a.amplitude_height_floor,a.amplitude_active_band))
            or not .002<a.marked_diameter_budget<=4.5 or a.witness_lower_budget<=0
            or a.amplitude_height_floor<=1 or a.amplitude_active_band<=0):
        raise ValueError('Use explicit finite positive Dmarked/L/Hmin budgets and full working-row limits')
    if (not all(math.isfinite(v) for v in (a.soc_tau,a.soc_inward_fraction))
            or min(a.soc_tau,a.soc_inward_fraction)<0 or a.soc_tau==a.soc_inward_fraction==0):
        raise ValueError('Use an explicit positive inward SOC policy with unchanged true thresholds')
    if a.uncentered_objective and a.centered_loss_source is not None:
        raise ValueError('Select one declared scalar evaluator')
    repo,work,output=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    topic=repo/'topics/visible-flex-larger-amplitude'
    old=topic/'scripts/resume_20261120';published=topic/'scripts/resume_20261126'
    here=Path(__file__).resolve().parent
    face=published/'launch_mean_metric_face_pcg.py'
    if sha(face)!=FACE_LAUNCHER_SHA:raise ValueError('Use the complete published R688 argv preparation')
    design_path=published/'launch_mean_metric_design_actions.py'
    driver=(a.driver or here/'fullclosed_mean_amplitude_complete_soc.py').resolve()
    base_driver=(a.base_driver or here/'fullclosed_mean_metric_amplitude_qp_v2.py').resolve()
    deriver_path=(a.source_deriver or here/'derive_mean_amplitude_complete_soc.py').resolve()
    typed_soc=(a.typed_soc_source or here/'complete_amplitude_rows_soc.py').resolve()
    projection=(a.soc_projection_source or published/'full_phi_all_rows_soc.py').resolve()
    deriver=load_bound('complete_mean_amplitude_SOC_whole_body',deriver_path,DERIVER_SHA)
    if sha(base_driver)!=BASE_DRIVER_SHA or driver.read_text()!=deriver.derive(base_driver):
        raise ValueError('Use the entire exactly derived v2 amplitude/SOC driver body')
    rows=(a.amplitude_rows_source or here/'held_amplitude_inequalities_v2.py').resolve()
    screen=(a.amplitude_screen_source or here/'held_amplitude_screen_v2.py').resolve()
    centered=None if a.uncentered_objective else (a.centered_loss_source or published/'centered_spectral_statistics.py').resolve()
    prepare=[sys.executable,str(face),'--repo',str(repo),'--work',str(work),
        '--bundle',str(a.bundle.resolve()),'--parent-report',str(a.parent_report.resolve()),
        '--carrier',str(a.carrier.resolve()),'--node-report',str(a.node_report.resolve()),
        '--scalar-input',str(a.scalar_input.resolve()),'--outdir',str(output),
        '--averaging',a.averaging,'--damping',str(a.damping),
        '--eta-start-node',str(a.eta_start_node),'--lambda-value',str(a.lambda_value),
        '--directions',str(a.directions),'--maxiter',str(a.maxiter),'--active-rows',str(a.active_rows),
        '--qp-atol',str(a.qp_atol),'--qp-rtol',str(a.qp_rtol),
        '--reach-safety-factor',str(a.reach_safety_factor),'--active-band',str(a.active_band),
        '--coarse-moment-stage-block',str(a.coarse_moment_stage_block),
        '--spectral-p',str(a.spectral_p),'--spectral-epsilon',str(a.spectral_epsilon),
        '--spectral-scale',str(a.spectral_scale),'--target',str(a.target),'--print-command']
    for path in a.manifest:prepare.extend(['--manifest',str(path.resolve())])
    if a.coarse_centers is not None:prepare.extend(['--coarse-centers',a.coarse_centers])
    if centered is not None:prepare.extend(['--centered-loss-source',str(centered)])
    try:
        prepared=subprocess.run(prepare,text=True,capture_output=True,check=True)
    except subprocess.CalledProcessError as error:
        if error.stdout:print(error.stdout,file=sys.stderr,flush=True)
        if error.stderr:print(error.stderr,file=sys.stderr,flush=True)
        raise
    command=shlex.split(prepared.stdout.strip())
    if len(command)<3 or Path(command[2]).name!='derived-mean-metric-face-PCG.py':
        raise ValueError('The complete R688 preparation changed its actual argv layout')
    command[2]=str(driver)
    replace(command,'--angles',a.angles);replace(command,'--stage-block',a.stage_block)
    command.extend(['--amplitude-rows-source',str(rows),'--amplitude-screen-source',str(screen),
        '--marked-diameter-budget',str(a.marked_diameter_budget),
        '--witness-lower-budget',str(a.witness_lower_budget),
        '--amplitude-height-floor',str(a.amplitude_height_floor),
        '--amplitude-top-radius',str(a.amplitude_top_radius),
        '--amplitude-top-distance',str(a.amplitude_top_distance),
        '--amplitude-active-band',str(a.amplitude_active_band)])
    command.extend(['--typed-soc-source',str(typed_soc),'--soc-projection-source',str(projection),
        '--soc-tau',str(a.soc_tau),'--soc-inward-fraction',str(a.soc_inward_fraction),
        '--soc-separation',a.soc_separation])
    if a.amplitude_budget_evidence is not None:
        command.extend(['--amplitude-budget-evidence',str(a.amplitude_budget_evidence.resolve())])
    if a.print_command:
        print(shlex.join(command));return
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Scientific complete amplitude-protected design requires public repository Actions')
    for path,digest in ((driver,DRIVER_SHA),(rows,ROWS_SHA),(screen,SCREEN_SHA),
            (typed_soc,SOC_SHA),(projection,PROJECTION_SHA),(deriver_path,DERIVER_SHA)):
        if sha(path)!=digest:raise ValueError('Changed complete amplitude source '+str(path))
    position_manifest=work/(output.name+'-inputs')/'complete-parent-positions.json'
    plan_path=work/(output.name+'-command.json')
    if output.exists() or position_manifest.parent.exists() or plan_path.exists():
        raise FileExistsError('Use new complete output, position memory and command paths')
    parent=json.loads(a.parent_report.read_text())
    parent_N=int(parent['N']);ratio=a.angles//parent_N
    if a.angles%parent_N or ratio<1 or ratio&(ratio-1):
        raise ValueError('Retain all actual parent angle locations in a dyadic supergrid')
    if (parent['exact_tail_eta_start_node']!=a.eta_start_node
            or parent['exact_tail_lambda']!=a.lambda_value
            or parent['exact_tail_node_report_sha256']!=sha(a.node_report)
            or parent['exact_tail_scalar_input_sha256']!=sha(a.scalar_input)):
        raise ValueError('This amplitude continuation keeps the SAME actual physical model and scalar input')
    previous=parent.get('amplitude_design_constraints',{}).get('budgets')
    if previous is not None and any(previous[key]!=value for key,value in
            (('marked_diameter_budget',a.marked_diameter_budget),
             ('witness_lower_budget',a.witness_lower_budget),('height_floor',a.amplitude_height_floor))):
        raise ValueError('Do not silently relax or redefine established amplitude budgets in a continuation')
    design=load_bound('amplitude_complete_parent_positions',design_path,DESIGN_LAUNCHER_SHA)
    positions=design.complete_positions(a,old/'launch_refinement_from_full_report.py',position_manifest)
    files={Path(__file__).resolve(),face,design_path,driver,rows,screen,typed_soc,projection,
        base_driver,deriver_path,
        old/'launch_refinement_from_full_report.py',published/'derive_mean_metric_face_pcg.py',
        old/'launch_full_phi_exact_tail_actions.py',old/'launch_full_phi_qp_actions.py',
        a.parent_report.resolve(),*map(Path.resolve,a.manifest)}
    explicit={'--bundle','--observations','--operator','--implementation','--helpers',
        '--witness-input','--radius-witness-input','--tail-node-report','--tail-scalar-input',
        '--amplitude-budget-evidence'}
    for index,value in enumerate(command[:-1]):
        if value.startswith('--') and (value.endswith('-source') or value in explicit):
            files.add(Path(command[index+1]).resolve())
    for path in files:
        if not path.is_file():raise FileNotFoundError(path)
    plan=dict(schema='complete-amplitude-mean-PCG-with-inward-all-row-SOC-command-v1',command=command,
        original_R688_command_preparation=prepare,
        source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'),github_run_id=os.environ.get('GITHUB_RUN_ID'),
        source_sha256=sha(__file__),file_sha256={str(path):sha(path) for path in sorted(files)},
        actual_parent_bundle_sha256=sha(a.bundle),actual_parent_report_sha256=sha(a.parent_report),
        complete_parent_permanent_locations=positions,
        amplitude_budgets=dict(marked_diameter_budget=a.marked_diameter_budget,
            witness_lower_budget=a.witness_lower_budget,height_floor=a.amplitude_height_floor,
            body_budget_rule='round down exact Dmarked-2/1000; actual helper validates 5L>=Dmarked',
            cap_radius='actual same FullHold problem.R; helper binds its binary identity'),
        maximum_original_geometry_rows=a.active_rows,
        maximum_additional_amplitude_rows=a.amplitude_top_radius+2*a.amplitude_top_distance+2,
        no_original_row_or_variable_removed=True,all_trial_acceptance_requires_true_amplitude_screen=True,
        complete_SOC=dict(tau=a.soc_tau,inward_fraction=a.soc_inward_fraction,separation=a.soc_separation,
            every_original_row_retained=True,maximum_corrections_per_QP_direction=1,
            negative_new_parent_bound_is_not_feasible_zero=True,
            corrected_model_Az_recomputed_at_same_parent=True,
            original_true_curvature_and_amplitude_thresholds_unchanged=True,
            continuous_correction_theorem_established=False),
        complete_driver_derivation=deriver.lineage(),
        initial_damping=a.damping,damping_source=damping_origin,mean_averaging=a.averaging,
        spectral=dict(p=a.spectral_p,epsilon=a.spectral_epsilon,scale=a.spectral_scale),
        selected_scalar_objective_key='phi_normalized' if centered is None else 'centered_phi_normalized',
        new_automatic_directional_fixture=False,continuous_amplitude_certified=False,
        fixed_final_metric=False,topic_completion_claimed=False,output=str(output))
    work.mkdir(parents=True,exist_ok=True)
    plan_path.write_text(json.dumps(plan,indent=2,allow_nan=False)+'\n')
    env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    subprocess.run(command,cwd=repo,env=env,check=True)


if __name__=='__main__':main()

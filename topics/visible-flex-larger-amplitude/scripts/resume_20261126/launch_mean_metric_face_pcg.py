#!/usr/bin/env python3
"""Run complete R684 mean design with current R688 coarse Gram and R685 PCG.

The published R684 launcher still prepares the complete original physical
argv and exact permanent-position union. The complete new driver is derived
from its frozen body. Every candidate's actual moving mean target and all
true geometry/line-search obligations remain. Public Actions only.
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


DESIGN_LAUNCHER_SHA='e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4'
DERIVER_SHA='b57ab303682f708c6d205cf0d527df2ec16aa2cfa1762a59070599abcade6d75'


def sha(path):
    digest=hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda:source.read(1024*1024),b''):
            digest.update(block)
    return digest.hexdigest()


def load_bound(name,path,digest):
    if not path.is_file() or path.stat().st_size>100000 or sha(path)!=digest:
        raise ValueError('Need the complete published stdlib source: '+name)
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec)
    sys.modules[name]=result
    spec.loader.exec_module(result)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','bundle','parent-report','carrier','node-report','scalar-input','outdir'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--manifest',type=Path,action='append',required=True)
    parser.add_argument('--averaging',choices=('material','physical'),required=True)
    parser.add_argument('--damping',type=float,required=True)
    parser.add_argument('--eta-start-node',type=int,default=885)
    parser.add_argument('--lambda-value',type=float,default=1.)
    parser.add_argument('--maxiter',type=int,default=64)
    parser.add_argument('--directions',type=int,default=2)
    parser.add_argument('--active-rows',type=int,default=192)
    parser.add_argument('--qp-rtol',type=float,default=1e-6)
    parser.add_argument('--qp-atol',type=float,default=1e-12)
    parser.add_argument('--reach-safety-factor',type=float,default=.992)
    parser.add_argument('--active-band',type=float,default=.025)
    parser.add_argument('--coarse-centers')
    parser.add_argument('--spectral-p',type=int,default=4)
    parser.add_argument('--spectral-epsilon',type=float,default=.001)
    parser.add_argument('--spectral-scale',type=float,default=.05)
    parser.add_argument('--target',type=float,default=5e-7)
    parser.add_argument('--design-launcher',type=Path)
    parser.add_argument('--base-driver',type=Path)
    parser.add_argument('--deriver',type=Path)
    parser.add_argument('--transform-source',type=Path)
    parser.add_argument('--mean-coarse-source',type=Path)
    parser.add_argument('--coarse-frame-source',type=Path)
    parser.add_argument('--coarse-v3-source',type=Path)
    parser.add_argument('--face-qp-source',type=Path)
    parser.add_argument('--coarse-moment-stage-block',type=int,default=8)
    parser.add_argument('--centered-loss-source',type=Path)
    parser.add_argument('--print-command',action='store_true')
    parser.add_argument('--prepare-source-only',action='store_true')
    args=parser.parse_args()
    if (not math.isfinite(args.damping) or args.damping<=0 or args.maxiter<1
            or args.directions<1 or args.active_rows<1 or args.coarse_moment_stage_block<1
            or not 0<args.active_band<args.reach_safety_factor<1):
        raise ValueError('Declare a positive current damping/budget and the retained geometric screen')
    if (not math.isfinite(args.lambda_value) or not 0<args.lambda_value<=1
            or args.eta_start_node<1 or args.spectral_p<2 or args.spectral_p%2
            or not math.isfinite(args.spectral_epsilon) or args.spectral_epsilon<=0
            or not math.isfinite(args.spectral_scale) or args.spectral_scale<=0
            or not math.isfinite(args.target) or args.target<=0):
        raise ValueError('Use the declared positive-lambda context and valid spectral parameters')
    for key in ('repo','work','bundle','parent_report','carrier','node_report','scalar_input','outdir'):
        setattr(args,key,getattr(args,key).resolve())
    args.manifest=[path.resolve() for path in args.manifest]
    repo,work,output=args.repo,args.work,args.outdir
    topic=repo/'topics/visible-flex-larger-amplitude'
    old=topic/'scripts/resume_20261120'
    source=Path(__file__).resolve().parent
    published=topic/'scripts/resume_20261126'
    design_path=(args.design_launcher or published/'launch_mean_metric_design_actions.py').resolve()
    derive_path=(args.deriver or source/'derive_mean_metric_face_pcg.py').resolve()
    base_path=(args.base_driver or published/'fullclosed_mean_metric_design_qp.py').resolve()
    transform=(args.transform_source or published/'mean_metric_design.py').resolve()
    moments=(args.mean_coarse_source or source/'mean_metric_coarse_moments.py').resolve()
    frame=(args.coarse_frame_source or old/'full_phi_coarse_frame.py').resolve()
    v3=(args.coarse_v3_source or old/'fullspace_feasible_active_cg_v3.py').resolve()
    v5=(args.face_qp_source or published/'fullspace_feasible_active_pcg_v5.py').resolve()
    centered=args.centered_loss_source.resolve() if args.centered_loss_source else None
    design=load_bound('R688_frozen_R684_complete_launcher',design_path,DESIGN_LAUNCHER_SHA)
    deriver=load_bound('R688_complete_mean_face_deriver',derive_path,DERIVER_SHA)
    driver_text,derivation=deriver.derive(repo,base_path)
    driver_directory=work/(output.name+'-driver')
    driver_path=driver_directory/'derived-mean-metric-face-PCG.py'
    if args.prepare_source_only:
        if driver_directory.exists():
            raise FileExistsError(driver_directory)
        driver_directory.mkdir(parents=True)
        driver_path.write_text(driver_text)
        print(json.dumps(dict(driver=str(driver_path),**derivation),sort_keys=True))
        return
    prepare=[sys.executable,str(design_path),'--repo',str(repo),'--work',str(work),
        '--bundle',str(args.bundle),'--parent-report',str(args.parent_report),
        '--carrier',str(args.carrier),'--node-report',str(args.node_report),
        '--scalar-input',str(args.scalar_input),'--eta-start-node',str(args.eta_start_node),
        '--lambda-value',str(args.lambda_value),'--averaging',args.averaging,
        '--outdir',str(output),'--driver',str(driver_path),
        '--transform-source',str(transform),'--damping',str(args.damping),
        '--maxiter',str(args.maxiter),'--directions',str(args.directions),
        '--active-rows',str(args.active_rows),'--qp-rtol',str(args.qp_rtol),
        '--qp-atol',str(args.qp_atol),'--reach-safety-factor',str(args.reach_safety_factor),
        '--active-band',str(args.active_band),'--spectral-p',str(args.spectral_p),
        '--spectral-epsilon',str(args.spectral_epsilon),'--spectral-scale',str(args.spectral_scale),
        '--target',str(args.target),'--print-command']
    for manifest in args.manifest:
        prepare.extend(['--manifest',str(manifest)])
    if args.coarse_centers is not None:
        prepare.extend(['--coarse-centers',args.coarse_centers])
    prepared=subprocess.run(prepare,text=True,capture_output=True,check=True)
    command=shlex.split(prepared.stdout.strip())
    if len(command)<3 or Path(command[2])!=driver_path:
        raise ValueError('The frozen mean launcher did not retain this complete derived driver')
    design.replace_flag(command,'--qp-source',v5)
    command.extend(['--mean-coarse-source',str(moments),'--coarse-frame-source',str(frame),
        '--coarse-v3-source',str(v3),'--coarse-moment-stage-block',str(args.coarse_moment_stage_block)])
    if centered is not None:
        command.extend(['--centered-loss-source',str(centered)])
    if args.print_command:
        print(shlex.join(command))
        return
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Scientific R688 mean design requires the public repository Actions')
    position_manifest=work/(output.name+'-inputs')/'complete-parent-positions.json'
    plan_path=work/(output.name+'-command.json')
    if (output.exists() or position_manifest.parent.exists() or driver_directory.exists()
            or plan_path.exists()):
        raise FileExistsError('Use fresh complete driver, position, plan and output locations')
    inputs={args.bundle,args.parent_report,args.carrier,args.node_report,args.scalar_input,*args.manifest}
    for path in inputs:
        if not path.is_file():
            raise FileNotFoundError(path)
    expected_paths=dict(mean_coarse=moments,coarse_frame=frame,coarse_qp_v3=v3,
        qp=v5,mean_transform=transform)
    for role,path in expected_paths.items():
        if sha(path)!=deriver.EXPECTED[role]:
            raise ValueError('The actual R688 component differs: '+role)
    if centered is not None and sha(centered)!=deriver.CENTERED_SHA:
        raise ValueError('Use the published optional centered loss source')
    driver_directory.mkdir(parents=True)
    driver_path.write_text(driver_text)
    history_path=old/'launch_refinement_from_full_report.py'
    position_record=design.complete_positions(args,history_path,position_manifest)
    files={driver_path,base_path,design_path,derive_path,history_path,Path(__file__).resolve(),
        old/'launch_full_phi_exact_tail_actions.py',old/'launch_full_phi_qp_actions.py',*inputs}
    explicit_paths={'--operator','--implementation','--helpers','--bundle',
        '--observations','--witness-input','--radius-witness-input',
        '--tail-node-report','--tail-scalar-input'}
    for index,value in enumerate(command[:-1]):
        if value.startswith('--') and (value.endswith('-source') or value in explicit_paths):
            files.add(Path(command[index+1]).resolve())
    for path in files:
        if not path.is_file():
            raise FileNotFoundError(path)
    source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
    plan=dict(schema='R688-public-actions-complete-mean-face-PCG-command-v1',
        command=command,original_complete_mean_command_preparation=prepare,
        driver_derivation=derivation,
        source_commit=source_commit,workflow_trigger_commit=os.environ.get('GITHUB_SHA'),
        github_run_id=os.environ.get('GITHUB_RUN_ID'),
        file_sha256={str(path):sha(path) for path in sorted(files)},
        parent_bundle=str(args.bundle),parent_report=str(args.parent_report),
        complete_permanent_positions=position_record,output=str(output),
        mean_averaging=args.averaging,
        spectral=dict(p=args.spectral_p,epsilon=args.spectral_epsilon,scale=args.spectral_scale),
        damping=args.damping,damping_is_explicit_not_inherited_from_another_target=True,
        selected_scalar_objective_key=('centered_phi_normalized' if centered else 'phi_normalized'),
        current_mean_target_is_recomputed_at_every_trial=True,
        current_true_gradient_Hessian_and_damping_units_unchanged=True,
        original_free_space_mother_norm_and_geometry_preserved=True,
        complete_NEW_mean_coarse_Gram_required=True,old_untransformed_Gram_used=False,
        face_metric='R685 constrained inverse of the actual fixed SPD map',
        unestablished_zero_core_shortcut_or_small_SPD_failure='Explicit original v3 full-mean QP',
        within_PCG_failure='No automatic retry or hidden preconditioner change',
        extra_J_counts='Actual wrapper/base entry counts are measured during real construction',
        final_metric_frozen=False,fixed_g_refinement=False,
        no_continuous_geometric_certificate_inherited=True)
    work.mkdir(parents=True,exist_ok=True)
    plan_path.write_text(json.dumps(plan,indent=2,allow_nan=False)+'\n')
    env=os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    subprocess.run(command,env=env,cwd=repo,check=True)


if __name__=='__main__':
    main()

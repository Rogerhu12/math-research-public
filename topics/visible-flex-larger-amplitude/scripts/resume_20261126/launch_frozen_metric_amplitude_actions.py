#!/usr/bin/env python3
"""Run a complete QP against ONE immutable frozen R684 metric in Actions.

A full solver parent retains its entire exact position history. A genuine
R676 transfer parent supplies its actually remapped complete position file;
no old-cell coordinates are walked out of its provenance records. The
transfer branch is an initializer, not an inherited solver acceptance.
"""
import argparse
import importlib.util
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys

HISTORY_SHA='4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
MEAN_LAUNCHER_SHA='e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4'
TRANSFER_SHA='2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a'


def sha(path):
    import hashlib
    digest=hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda:source.read(1<<20),b''):
            digest.update(block)
    return digest.hexdigest()


def load(name,path,digest=None):
    if digest is not None and sha(path)!=digest:
        raise ValueError('Changed explicit complete-history/transfer source: '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module;spec.loader.exec_module(module)
    return module


def replace(command,flag,value):
    if command.count(flag)!=1:raise ValueError('Expected one flag '+flag)
    command[command.index(flag)+1]=str(value)


def transfer_positions(args,old,manifest_path):
    """Read only the actual R676 output's complete, already remapped points."""
    history=load('frozen_qp_history',old/'launch_refinement_from_full_report.py',HISTORY_SHA)
    if sha(old/'refine_fixed_g_fullclosed.py')!=TRANSFER_SHA:
        raise ValueError('Keep the already proved physical transfer source')
    r=json.loads(args.transfer_report.read_text())
    if (r.get('schema')!='same-fixed-g-fullclosed-refinement-actions-v1'
            or r.get('source_sha256')!=TRANSFER_SHA or 'seconds' not in r):
        raise ValueError('Need the actual completed R676 physical transfer report')
    for role,path in (('bundle',args.bundle),('carrier',args.carrier),('node_report',args.node_report)):
        if r['outputs'][role]['sha256']!=sha(path):
            raise ValueError('The actual refined '+role+' does not match the transfer report')
    if r['inputs']['scalar_input']['sha256']!=sha(args.scalar_input):
        raise ValueError('The original exact scalar input changed after transfer')
    model=r['refined_model']
    if (model['eta_start_node']!=args.eta_start_node or model['lambda_value']!=args.lambda_value
            or r['angular_refinement']['refined_full_angles']!=args.angles):
        raise ValueError('Actual refined model/grid differs from the explicit solve argv')
    if r.get('nonlinear_solve_performed') is not False:
        raise ValueError('This branch is the literal transfer initializer, not another unnamed solver state')
    wanted=r['outputs']['permanent_locations']['sha256']
    if not any(sha(path)==wanted for path in args.manifest):
        raise ValueError('Retain the actual transfer output full permanent-location manifest')
    points=history.Locations(r['transfer']['refined_J'],r['observations']['new_rows'],args.angles)
    sources=[]
    for path in args.manifest:
        value=json.loads(path.read_text())
        if value.get('carrier_sha256')!=sha(args.carrier):
            raise ValueError('Every supplied refined position file must bind the current carrier')
        keys=('curvature_points','radius_points','protected_curvature_points')
        if any(key not in value for key in keys):
            raise ValueError('Use complete pure-position manifests after exact refinement')
        # Source ancestry can name old cells; only these literal current
        # point arrays are in the refined coordinate system.
        points.walk({key:value[key] for key in keys},path=('refined_manifest',path.name))
        sources.append(dict(path=str(path.resolve()),sha256=sha(path)))
    resolved=points.resolve_grid(args.carrier)
    summary=points.summary()
    if not summary['curvature_numeric_tuples'] or not summary['radius_numeric_tuples']:
        raise ValueError('Both permanent geometry roles must remain')
    manifest=dict(schema='R684-exact-refined-position-union-v1',carrier_sha256=sha(args.carrier),
        transfer_report_sha256=sha(args.transfer_report),sources=sources,**points.arrays())
    manifest_path.parent.mkdir(parents=True,exist_ok=False)
    manifest_path.write_text(json.dumps(manifest,separators=(',',':'),allow_nan=False)+'\n')
    return dict(kind='actual R676 transferred initializer',
        transfer_report=str(args.transfer_report.resolve()),transfer_report_sha256=sha(args.transfer_report),
        transfer_source_sha256=TRANSFER_SHA,history_source_sha256=HISTORY_SHA,
        manifest=str(manifest_path),manifest_sha256=sha(manifest_path),
        resolved_grid_positions=resolved,resolved_position_counts=summary,
        all_supplied_actual_refined_locations_retained=True,
        old_cell_locations_reinterpreted_as_refined=False,
        inherited_solver_acceptance=False,field_evaluations=0,J_calls=0,Jtranspose_calls=0)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','bundle','carrier','node-report','scalar-input','outdir','frozen-target-manifest'):
        parser.add_argument('--'+key,type=Path,required=True)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--parent-report',type=Path)
    group.add_argument('--transfer-report',type=Path)
    parser.add_argument('--manifest',type=Path,action='append',required=True)
    parser.add_argument('--eta-start-node',type=int,required=True)
    parser.add_argument('--lambda-value',type=float,required=True)
    parser.add_argument('--angles',type=int,default=2048)
    parser.add_argument('--stage-block',type=int,default=64)
    parser.add_argument('--driver',type=Path)
    parser.add_argument('--amplitude-rows-source',type=Path)
    parser.add_argument('--amplitude-screen-source',type=Path)
    parser.add_argument('--marked-diameter-budget',type=float,required=True)
    parser.add_argument('--witness-lower-budget',type=float,required=True)
    parser.add_argument('--amplitude-height-floor',type=float,required=True)
    parser.add_argument('--amplitude-top-radius',type=int,default=2)
    parser.add_argument('--amplitude-top-distance',type=int,default=4)
    parser.add_argument('--amplitude-active-band',type=float,default=.025)
    parser.add_argument('--amplitude-budget-evidence',type=Path)
    parser.add_argument('--frozen-target-source',type=Path)
    parser.add_argument('--frozen-coarse-source',type=Path)
    parser.add_argument('--coarse-moment-stage-block',type=int,default=8)
    parser.add_argument('--coarse-preconditioner',choices=('coarse','none'),default='coarse')
    parser.add_argument('--centered-loss-source',type=Path)
    parser.add_argument('--uncentered-objective',action='store_true')
    parser.add_argument('--comparison-parent-report',type=Path)
    parser.add_argument('--comparison-parent-carrier',type=Path)
    for key in ('bundle','node-report','scalar-input','observation-carrier','reference-carrier'):
        parser.add_argument('--target-'+key,type=Path)
    parser.add_argument('--damping',type=float,required=True)
    parser.add_argument('--maxiter',type=int,default=64)
    parser.add_argument('--directions',type=int,default=2)
    parser.add_argument('--active-rows',type=int,default=192)
    parser.add_argument('--qp-atol',type=float,default=0.)
    parser.add_argument('--qp-rtol',type=float,default=1e-6)
    parser.add_argument('--reach-safety-factor',type=float,default=.992)
    parser.add_argument('--active-band',type=float,default=.025)
    parser.add_argument('--spectral-p',type=int,default=4)
    parser.add_argument('--spectral-epsilon',type=float,default=.001)
    parser.add_argument('--spectral-scale',type=float,default=.05)
    parser.add_argument('--target',type=float,required=True)
    parser.add_argument('--print-command',action='store_true')
    args=parser.parse_args()
    if (not 0<args.lambda_value<=1 or args.eta_start_node<1 or args.angles<4 or args.angles%4
            or args.stage_block<1 or args.coarse_moment_stage_block<1
            or args.maxiter<1 or args.directions<1 or args.active_rows<1
            or not 0<args.active_band<args.reach_safety_factor<1
            or not math.isfinite(args.damping) or args.damping<=0
            or args.spectral_p<2 or args.spectral_p%2
            or not all(math.isfinite(v) for v in (args.spectral_epsilon,args.spectral_scale,args.target))
            or min(args.spectral_epsilon,args.spectral_scale,args.target)<=0):
        raise ValueError('Need explicit finite positive fixed-target solve parameters')
    repo,work=args.repo.resolve(),args.work.resolve()
    old=repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    source=Path(__file__).resolve().parent
    driver=(args.driver or source/'fullclosed_frozen_metric_amplitude_qp.py').resolve()
    amplitude_rows=(args.amplitude_rows_source or source/'held_amplitude_inequalities_v2.py').resolve()
    amplitude_screen=(args.amplitude_screen_source or source/'held_amplitude_screen_v2.py').resolve()
    frozen=(args.frozen_target_source or source/'frozen_mean_metric.py').resolve()
    moments=(args.frozen_coarse_source or source/'frozen_metric_coarse_moments.py').resolve()
    published=repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    if args.uncentered_objective and args.centered_loss_source is not None:
        raise ValueError('Select exactly one declared scalar objective evaluation')
    centered=None if args.uncentered_objective else (args.centered_loss_source or published/'centered_spectral_statistics.py').resolve()
    original=old/'launch_full_phi_exact_tail_actions.py'
    output=args.outdir.resolve()
    position_manifest=work/(output.name+'-inputs')/'complete-current-positions.json'
    prepare=[sys.executable,str(original),'--repo',str(repo),'--work',str(work),
        '--bundle',str(args.bundle.resolve()),'--carrier',str(args.carrier.resolve()),
        '--node-report',str(args.node_report.resolve()),'--scalar-input',str(args.scalar_input.resolve()),
        '--manifest',str(position_manifest),'--eta-start-node',str(args.eta_start_node),
        '--lambda-value',str(args.lambda_value),'--source-lambda',str(args.lambda_value),'--migration','keep-q',
        '--outdir',str(output),'--damping',str(args.damping),'--directions',str(args.directions),
        '--maxiter',str(args.maxiter),'--active-rows',str(args.active_rows),
        '--qp-atol',str(args.qp_atol),'--qp-rtol',str(args.qp_rtol),
        '--reach-safety-factor',str(args.reach_safety_factor),'--active-band',str(args.active_band),
        '--print-command']
    prepared=subprocess.run(prepare,text=True,capture_output=True,check=True)
    command=shlex.split(prepared.stdout.strip())
    if len(command)<3 or Path(command[2]).name!='fullclosed_gauss_exact_tail_inequality_qp.py':
        raise ValueError('The template must prepare the original complete R671 QP argv')
    command[2]=str(driver)
    for flag,value in (('--qp-source',published/'fullspace_feasible_active_pcg_v5.py'),
            ('--angles',args.angles),('--stage-block',args.stage_block),('--spectral-p',args.spectral_p),
            ('--spectral-epsilon',args.spectral_epsilon),('--spectral-scale',args.spectral_scale),
            ('--target',args.target)):
        replace(command,flag,value)
    command.extend(['--frozen-target-source',str(frozen),
        '--frozen-target-manifest',str(args.frozen_target_manifest.resolve()),
        '--frozen-coarse-source',str(moments),
        '--coarse-frame-source',str(old/'full_phi_coarse_frame.py'),
        '--coarse-v3-source',str(old/'fullspace_feasible_active_cg_v3.py'),
        '--original-coarse-moments-source',str(old/'full_phi_coarse_moments.py'),
        '--coarse-moment-stage-block',str(args.coarse_moment_stage_block),
        '--coarse-preconditioner',args.coarse_preconditioner])
    if centered is not None:command.extend(['--centered-loss-source',str(centered)])
    for key in ('bundle','node_report','scalar_input','observation_carrier','reference_carrier'):
        value=getattr(args,'target_'+key)
        if value is not None:command.extend(['--target-'+key.replace('_','-'),str(value.resolve())])
    for key in ('comparison_parent_report','comparison_parent_carrier'):
        value=getattr(args,key)
        if value is not None:command.extend(['--'+key.replace('_','-'),str(value.resolve())])
    command.extend(['--amplitude-rows-source',str(amplitude_rows),
        '--amplitude-screen-source',str(amplitude_screen),
        '--marked-diameter-budget',str(args.marked_diameter_budget),
        '--witness-lower-budget',str(args.witness_lower_budget),
        '--amplitude-height-floor',str(args.amplitude_height_floor),
        '--amplitude-top-radius',str(args.amplitude_top_radius),
        '--amplitude-top-distance',str(args.amplitude_top_distance),
        '--amplitude-active-band',str(args.amplitude_active_band)])
    if args.amplitude_budget_evidence is not None:
        command.extend(['--amplitude-budget-evidence',str(args.amplitude_budget_evidence.resolve())])
    if args.print_command:
        print(shlex.join(command));return
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Scientific frozen-target solving belongs only in the public repository Actions')
    for path,digest in ((driver,'859ceb836378c3140a0d27877987f3d06546aae2baee0ef316403d3f332d911b'),
            (amplitude_rows,'d494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'),
            (amplitude_screen,'e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f')):
        if sha(path)!=digest:raise ValueError('Changed complete fixed-target amplitude source '+str(path))
    if output.exists() or position_manifest.parent.exists():
        raise FileExistsError('Do not overwrite an actual frozen-target solve budget or position set')
    target_module=load('frozen_qp_manifest_reader',frozen)
    target=target_module.read_manifest(args.frozen_target_manifest)
    if args.parent_report is not None:
        helper_path=source/'launch_mean_metric_design_actions.py'
        helper=load('frozen_qp_complete_parent_history',helper_path,MEAN_LAUNCHER_SHA)
        positions=helper.complete_positions(args,old/'launch_refinement_from_full_report.py',position_manifest)
        parent=json.loads(args.parent_report.read_text())
        previous=parent.get('amplitude_design_constraints',{}).get('budgets')
        if previous is not None and any(previous[key]!=value for key,value in
                (('marked_diameter_budget',args.marked_diameter_budget),
                 ('witness_lower_budget',args.witness_lower_budget),('height_floor',args.amplitude_height_floor))):
            raise ValueError('Keep the same explicitly established amplitude budgets in fixed-target continuation')
        parent_N=int(parent['N'])
        ratio=args.angles//parent_N
        if args.angles%parent_N or ratio<1 or ratio&(ratio-1):
            raise ValueError('Retain the complete parent angular grid in an exact dyadic supergrid')
        if parent.get('frozen_metric_target',{}).get('target_identity_sha256',target['target_identity_sha256'])!=target['target_identity_sha256']:
            raise ValueError('A fixed-target continuation cannot change its frozen metric identity')
        binding_report=args.parent_report
    else:
        positions=transfer_positions(args,old,position_manifest)
        binding_report=args.transfer_report
    files={driver,frozen,original,Path(__file__).resolve(),binding_report.resolve(),
        args.frozen_target_manifest.resolve(),old/'launch_full_phi_qp_actions.py',
        old/'launch_refinement_from_full_report.py'}
    files.add(helper_path if args.parent_report is not None else old/'refine_fixed_g_fullclosed.py')
    files.update(path.resolve() for path in args.manifest)
    explicit={'--operator','--implementation','--helpers','--bundle','--observations',
        '--witness-input','--radius-witness-input','--tail-node-report','--tail-scalar-input',
        '--frozen-target-manifest','--target-bundle','--target-node-report','--target-scalar-input',
        '--target-observation-carrier','--target-reference-carrier',
        '--comparison-parent-report','--comparison-parent-carrier','--amplitude-budget-evidence'}
    for i,value in enumerate(command[:-1]):
        if value.startswith('--') and (value.endswith('-source') or value in explicit):
            files.add(Path(command[i+1]).resolve())
    for path in files:
        if not path.is_file():raise FileNotFoundError(path)
    plan_path=work/(output.name+'-command.json')
    if plan_path.exists():raise FileExistsError(plan_path)
    plan=dict(schema='complete-fixed-frozen-target-with-amplitude-command-v1',command=command,
        original_command_preparation=prepare,
        source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'),github_run_id=os.environ.get('GITHUB_RUN_ID'),
        file_sha256={str(path):sha(path) for path in sorted(files)},
        parent_bundle_sha256=sha(args.bundle),binding_report=str(binding_report.resolve()),
        binding_report_sha256=sha(binding_report),complete_permanent_positions=positions,
        frozen_target_identity_sha256=target['target_identity_sha256'],
        frozen_target_manifest_sha256=sha(args.frozen_target_manifest),
        target_angles=target['full_angles'],current_angles=args.angles,
        final_metric_frozen=True,moving_mean_projection=False,
        amplitude_budgets=dict(marked_diameter_budget=args.marked_diameter_budget,
            witness_lower_budget=args.witness_lower_budget,height_floor=args.amplitude_height_floor),
        amplitude_working_limits=dict(radius_locations=args.amplitude_top_radius,
            distance_locations=args.amplitude_top_distance,active_band=args.amplitude_active_band),
        all_original_geometry_rows_retained=True,continuous_amplitude_certified=False,
        spectral=dict(p=args.spectral_p,epsilon=args.spectral_epsilon,scale=args.spectral_scale),
        initial_damping=args.damping,output=str(output),
        selected_scalar_objective_key='phi_normalized' if centered is None else 'centered_phi_normalized',
        centered_statistics_only_constant_subtraction=centered is not None,
        selected_preconditioner=args.coarse_preconditioner,
        coarse_moment_stage_block=args.coarse_moment_stage_block,
        declared_fixed_target_threshold=args.target,
        threshold_is_not_a_claim_about_README_original_solver_tolerance=True,
        existing_target_redefined=False,old_geometric_acceptance_inherited=False,
        scope='Complete same-frozen-target solve; finite budget alone does not certify refinement convergence')
    work.mkdir(parents=True,exist_ok=True)
    plan_path.write_text(json.dumps(plan,indent=2,allow_nan=False)+'\n')
    env=os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    subprocess.run(command,env=env,cwd=repo,check=True)


if __name__=='__main__':main()

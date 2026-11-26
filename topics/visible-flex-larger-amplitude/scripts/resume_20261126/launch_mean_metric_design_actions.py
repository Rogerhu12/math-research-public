#!/usr/bin/env python3
"""Prepare/run R684 NEW mean-metric design in the public repository Actions.

The R671 launcher is used only to prepare complete source/geometry argv.
The new driver uses every mean-metric J/J* chain and the original H2 norm.
The explicit design Phi is recomputed at the unchanged parent's field and
at each trial. No old Phi value or fixed-g convergence is inherited.
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

HISTORY_SHA='4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'


def sha(path):
    digest=hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda:source.read(1024*1024),b''):
            digest.update(block)
    return digest.hexdigest()


def replace_flag(command,flag,value):
    if command.count(flag)!=1:
        raise ValueError('Expected one literal flag: '+flag)
    command[command.index(flag)+1]=str(value)


def complete_positions(args,history_path,manifest_path):
    """Reuse the published complete-history reader; never round locations."""
    if sha(history_path)!=HISTORY_SHA:
        raise ValueError('Use the published exact-position complete-history helper')
    spec=importlib.util.spec_from_file_location('mean_design_complete_history',history_path)
    history=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=history
    spec.loader.exec_module(history)
    report=json.loads(args.parent_report.read_text())
    if report.get('complete') is not True:
        raise ValueError('The design parent must be an actually completed report')
    if report.get('final_bundle_sha256')!=sha(args.bundle):
        raise ValueError('The actual design-parent bytes do not match its report')
    carrier_sha=sha(args.carrier)
    if report.get('observation_carrier_sha256')!=carrier_sha:
        raise ValueError('Preserve the actual parent observation carrier')
    N,J=int(report['N']),int(report['J'])
    rows=int(report['all_full_rows'])
    if N<4 or N%4 or J<2 or rows%(3*N):
        raise ValueError('The parent full observation dimensions are inconsistent')
    points=history.Locations(J,rows//(3*N),N)
    points.walk(report,path=('parent_report',))
    sources=[dict(role='completed_parent_report',path=str(args.parent_report.resolve()),sha256=sha(args.parent_report))]
    for path in args.manifest:
        payload=json.loads(path.read_text())
        if payload.get('carrier_sha256',carrier_sha)!=carrier_sha:
            raise ValueError('A historical manifest belongs to a different carrier')
        points.walk(payload,path=('historical_manifest',path.name))
        sources.append(dict(role='historical_manifest',path=str(path.resolve()),sha256=sha(path)))
    before=points.summary()
    resolved=points.resolve_grid(args.carrier)
    after=points.summary()
    if not after['curvature_numeric_tuples'] or not after['radius_numeric_tuples']:
        raise ValueError('Both complete permanent point roles are required')
    manifest=dict(schema='R684-exact-complete-parent-location-union-v1',carrier_sha256=carrier_sha,
        parent_report_sha256=sha(args.parent_report),sources=sources,**points.arrays())
    manifest_path.parent.mkdir(parents=True,exist_ok=False)
    manifest_path.write_text(json.dumps(manifest,separators=(',',':'),allow_nan=False)+'\n')
    return dict(history_source=str(history_path),history_source_sha256=HISTORY_SHA,
        source_report_final_bundle_sha256=report['final_bundle_sha256'],
        manifest=str(manifest_path),manifest_sha256=sha(manifest_path),
        extraction_before_grid_resolution=before,resolved_grid_positions=resolved,
        resolved_position_counts=after,field_evaluations=0,J_calls=0,Jtranspose_calls=0,
        coordinate_arrays_read=['observation_cells','observation_u'],
        all_parent_trial_SOC_active_and_final_memory_positions_retained=True,
        no_new_physical_fixture_or_scientific_solve=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--work',type=Path,required=True)
    parser.add_argument('--bundle',type=Path,required=True)
    parser.add_argument('--parent-report',type=Path,required=True)
    parser.add_argument('--carrier',type=Path,required=True)
    parser.add_argument('--manifest',type=Path,action='append',required=True)
    parser.add_argument('--node-report',type=Path,required=True)
    parser.add_argument('--scalar-input',type=Path,required=True)
    parser.add_argument('--eta-start-node',type=int,default=885)
    parser.add_argument('--lambda-value',type=float,default=1.)
    parser.add_argument('--averaging',choices=('material','physical'),required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--source-launcher',type=Path)
    parser.add_argument('--driver',type=Path)
    parser.add_argument('--transform-source',type=Path)
    parser.add_argument('--damping',type=float,required=True)
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
    parser.add_argument('--print-command',action='store_true')
    args=parser.parse_args()
    if (not math.isfinite(args.lambda_value) or not 0<args.lambda_value<=1
            or args.eta_start_node<1):
        raise ValueError('Need an actual positive-lambda R671 parent and its interior eta node')
    if (not math.isfinite(args.damping) or args.damping<=0 or args.maxiter<1
            or args.directions<1 or args.active_rows<1
            or not 0<args.active_band<args.reach_safety_factor<1):
        raise ValueError('Invalid explicit new-design QP budget or geometry screen')
    if (args.spectral_p<2 or args.spectral_p%2
            or not math.isfinite(args.spectral_epsilon) or args.spectral_epsilon<=0
            or not math.isfinite(args.spectral_scale) or args.spectral_scale<=0
            or not math.isfinite(args.target) or args.target<=0):
        raise ValueError('Declare even p>=2 and positive finite epsilon, scale and target')
    repo,work=args.repo.resolve(),args.work.resolve()
    topic=repo/'topics/visible-flex-larger-amplitude'
    old=topic/'scripts/resume_20261120'
    source=Path(__file__).resolve().parent
    original=(args.source_launcher or old/'launch_full_phi_exact_tail_actions.py').resolve()
    driver=(args.driver or source/'fullclosed_mean_metric_design_qp.py').resolve()
    transform=(args.transform_source or source/'mean_metric_design.py').resolve()
    output=args.outdir.resolve()
    history_path=old/'launch_refinement_from_full_report.py'
    position_manifest=work/(output.name+'-inputs')/'complete-parent-positions.json'
    prepare=[sys.executable,str(original),'--repo',str(repo),'--work',str(work),
        '--bundle',str(args.bundle.resolve()),'--carrier',str(args.carrier.resolve()),
        '--node-report',str(args.node_report.resolve()),'--scalar-input',str(args.scalar_input.resolve()),
        '--eta-start-node',str(args.eta_start_node),'--lambda-value',str(args.lambda_value),
        '--source-lambda',str(args.lambda_value),'--migration','keep-q',
        '--outdir',str(output),'--damping',str(args.damping),
        '--maxiter',str(args.maxiter),'--directions',str(args.directions),
        '--active-rows',str(args.active_rows),'--qp-rtol',str(args.qp_rtol),
        '--qp-atol',str(args.qp_atol),'--reach-safety-factor',str(args.reach_safety_factor),
        '--active-band',str(args.active_band),'--print-command']
    prepare.extend(['--manifest',str(position_manifest)])
    if args.coarse_centers is not None:
        prepare.extend(['--coarse-centers',args.coarse_centers])
    prepared=subprocess.run(prepare,text=True,capture_output=True,check=True)
    command=shlex.split(prepared.stdout.strip())
    if len(command)<3 or Path(command[2]).name!='fullclosed_gauss_exact_tail_inequality_qp.py':
        raise ValueError('The original launcher did not return the declared R671 complete-field QP')
    command[2]=str(driver)
    replace_flag(command,'--qp-source',old/'fullspace_feasible_active_cg_v3.py')
    for flag,value in (('--spectral-p',args.spectral_p),
            ('--spectral-epsilon',args.spectral_epsilon),
            ('--spectral-scale',args.spectral_scale),('--target',args.target)):
        replace_flag(command,flag,value)
    command.extend(['--mean-transform-source',str(transform),'--mean-averaging',args.averaging])
    if args.print_command:
        print(shlex.join(command))
        return
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Scientific mean-metric design requires Rogerhu12/math-research-public Actions; --print-command only prepares argv.')
    if output.exists() or position_manifest.parent.exists():
        raise FileExistsError('Use new output and complete-position directories for every design budget')
    position_record=complete_positions(args,history_path,position_manifest)
    files={driver,transform,original,history_path,args.parent_report.resolve(),
        old/'launch_full_phi_qp_actions.py',Path(__file__).resolve()}
    files.update(path.resolve() for path in args.manifest)
    explicit_paths={'--operator','--implementation','--helpers','--bundle',
        '--observations','--witness-input','--radius-witness-input',
        '--tail-node-report','--tail-scalar-input'}
    for index,value in enumerate(command[:-1]):
        if value.startswith('--') and (value.endswith('-source') or value in explicit_paths):
            files.add(Path(command[index+1]).resolve())
    for path in files:
        if not path.is_file():
            raise FileNotFoundError(path)
    if output.exists():
        raise FileExistsError('Use a new output directory for every numerical design budget')
    plan_path=work/(output.name+'-command.json')
    if plan_path.exists():
        raise FileExistsError(plan_path)
    source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
    plan=dict(schema='R684-public-actions-new-mean-metric-design-command-v1',
        command=command,original_command_preparation=prepare,
        source_commit=source_commit,workflow_trigger_commit=os.environ.get('GITHUB_SHA'),
        github_run_id=os.environ.get('GITHUB_RUN_ID'),
        file_sha256={str(path):sha(path) for path in sorted(files)},
        parent_bundle=str(args.bundle.resolve()),output=str(output),
        complete_permanent_positions=position_record,
        eta_start_node=args.eta_start_node,fixed_lambda=args.lambda_value,
        parent_lambda_must_match=True,migration='keep-q',
        unchanged_parent_physical_field=True,original_free_coordinates_preserved=True,
        mean_metric_design=dict(averaging=args.averaging,
            weights=('m*rho/sum(m*rho)' if args.averaging=='material' else 'fixed m/sum(m)'),
            cross_mean='zero on the full circle by exact reflection parity',
            material_Haar_quadrature=args.averaging=='material',
            all_target_and_mean_weight_derivatives_in_J_and_Jstar=True,
            old_metric_unchanged=False,final_target_frozen=False,
            fixed_g_refinement=False),
        spectral=dict(p=args.spectral_p,epsilon=args.spectral_epsilon,scale=args.spectral_scale),
        damping=args.damping,all_comparisons_require_same_design_objective=True,
        inherited_parent_acceptance=False,inherited_continuous_certificates=False,
        geometry='Same actual R671 six jets and permanent complete-field inequality memory',
        step_norm='Original positive nu_c=24 H2-type mother norm; all complete original variables',
        preconditioner='No old unprojected angular-moment normal is used',
        scope='Moving-target design only; freeze an explicit radial metric before refinement')
    work.mkdir(parents=True,exist_ok=True)
    plan_path.write_text(json.dumps(plan,indent=2,allow_nan=False)+'\n')
    env=os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    subprocess.run(command,env=env,cwd=repo,check=True)


if __name__=='__main__':
    main()

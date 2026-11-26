#!/usr/bin/env python3
"""Run full q/core/H after an actual SAME fixed-deep-scalar refinement.

The transfer branch reads only actual fine outputs and their remapped
addresses, never parent ancestry locations under a fine carrier. A solver parent
retains every complete current report/trial/active/final location. Complete
new-field metric/geometry/amplitude values are reread by the real driver.
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

DRIVER_SHA='1745cfae02b7ad0335577a340cfee52f179e1f27508c8d20ef1487abec00f154'
BASE_DRIVER_SHA='d3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95'
TRANSFER_SHA='5f1b285fd021971cdbeb6680d28b8ef0c5ec24cdea5f9a0f830b3e87aebc06df'
FACTORY_SHA='4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'
DEEP_SHA='e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
COARSE_SHA='dcfa30b688104b27efeddfbe6921af25ba33ba6202be43f815d5b8d8bfc69395'
ROWS_SHA='d494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'
SCREEN_SHA='e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f'
HISTORY_SHA='4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
OLD_LAUNCHER_SHA='c9ba1d73db3e3608dffa1dbc9aeeda2a355d2ff4c2b9fc8eed2140c985869ec7'
OLD_BASE_LAUNCHER_SHA='6f021d459c24d5cb5a07853628d6a6a297332d51ad561beab2d09e50e2b34d63'
PARENT_SCHEMA='complete-refined-fixed-deep-scalar-with-held-amplitude-budgets-v1'
TRANSFER_SCHEMA='same-fixed-deep-scalar-complete-refinement-transfer-v1'


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def load_bound(name,path,digest):
    if sha(path)!=digest:raise ValueError('Changed complete source '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def replace(command,flag,value):
    if command.count(flag)!=1:raise ValueError('Expected exactly one flag '+flag)
    command[command.index(flag)+1]=str(value)


def actual_record(path,record,role):
    if sha(path)!=record.get('sha256'):
        raise ValueError('Actual same-byte '+role+' differs from its complete source report')
    return dict(path=str(path.resolve()),sha256=sha(path),source_record=record)


def complete_current_positions(a,history_path,manifest_path):
    history=load_bound('_deep_fixed_scalar_complete_history',history_path,HISTORY_SHA)
    current_carrier_sha=sha(a.carrier);current_bundle_sha=sha(a.bundle)
    source_records=[];read_payloads=[]
    if a.refinement_report is not None:
        report=json.loads(a.refinement_report.read_text())
        if (report.get('schema')!=TRANSFER_SCHEMA or report.get('source_sha256')!=TRANSFER_SHA
                or report.get('nonlinear_solve_performed') is not False
                or report.get('finite_metric_or_geometry_readout_performed') is not False
                or report.get('same_fixed_profile_preserved') is not True):
            raise ValueError('Use the actual complete byte-bound SAME fixed-deep-scalar transfer')
        for path,role in ((a.bundle,'bundle'),(a.carrier,'carrier'),(a.node_report,'node_report')):
            actual_record(path,report['outputs'][role],role)
        actual_record(a.scalar_input,report['inputs']['scalar_input'],'unchanged analytic input')
        definition=report['refined_model'];identity=report['fixed_scalar_metric_identity_sha256']
        if (definition.get('schema')!='deep-valley-fixed-scalar-fullclosed-lift-v1'
                or definition.get('target_is_a_moving_angular_mean') is not False
                or definition.get('profile_identity_sha256')!=identity
                or definition.get('eta_start_node')!=a.eta_start_node
                or definition.get('lambda_value')!=1.):
            raise ValueError('Use the actual refined physical eta and unchanged exact scalar profile')
        parent=json.loads(a.comparison_parent_report.read_text())
        parent_sources={'complete-fixed-deep-scalar-with-held-amplitude-budgets-v1':BASE_DRIVER_SHA,
            PARENT_SCHEMA:DRIVER_SHA}
        if (parent.get('complete') is not True
                or parent_sources.get(parent.get('schema'))!=parent.get('source_sha256')
                or parent.get('final_bundle_sha256')!=report['inputs']['bundle']['sha256']
                or parent.get('observation_carrier_sha256')!=report['inputs']['carrier']['sha256']
                or sha(a.comparison_parent_carrier)!=parent['observation_carrier_sha256']
                or parent['fixed_scalar_metric']['identity_sha256']!=identity):
            raise ValueError('Compare the actual complete parent from which this fine seed was transferred')
        candidates=[path for path in a.manifest if sha(path)==report['outputs']['permanent_locations']['sha256']]
        if len(candidates)!=1:
            raise ValueError('Supply the actual complete remapped fine locations exactly once')
        transferred=json.loads(candidates[0].read_text())
        if (transferred.get('schema')!='fixed-deep-scalar-exact-refinement-location-transfer-v1'
                or transferred.get('carrier_sha256')!=current_carrier_sha
                or transferred.get('bundle_sha256')!=current_bundle_sha
                or transferred.get('refinement_source_sha256')!=TRANSFER_SHA
                or transferred.get('all_declared_exact_locations_retained') is not True
                or transferred.get('old_geometry_or_metric_values_inherited') is not False):
            raise ValueError('Use the actual exact-symbolic fine-carrier location transfer')
        J=int(report['transfer']['refined_J']);P=int(report['observations']['new_rows'])
        N=int(report['angular_refinement']['refined_full_angles'])
        source_records.append(dict(role='actual_fixed_deep_refinement_report',
            path=str(a.refinement_report.resolve()),sha256=sha(a.refinement_report),
            new_seed_sha256=current_bundle_sha,original_parent_bundle_sha256=report['inputs']['bundle']['sha256'],
            old_values_or_certificates_inherited=False))
        previous=parent['amplitude_design_constraints']['budgets']
    else:
        report=json.loads(a.parent_report.read_text())
        if (report.get('schema')!=PARENT_SCHEMA or report.get('complete') is not True
                or report.get('source_sha256')!=DRIVER_SHA
                or report.get('final_bundle_sha256')!=current_bundle_sha
                or report.get('observation_carrier_sha256')!=current_carrier_sha
                or report.get('exact_tail_node_report_sha256')!=sha(a.node_report)
                or report.get('exact_tail_scalar_input_sha256')!=sha(a.scalar_input)
                or report.get('exact_tail_lambda')!=1.
                or report.get('exact_tail_eta_start_node')!=a.eta_start_node):
            raise ValueError('Use the actual complete SAME fine-problem parent and current inputs')
        fixed=report['fixed_scalar_metric'];identity=fixed['identity_sha256']
        common=report['common_parent_measure_comparison']
        if (fixed.get('target_fixed_before_first_direction') is not True
                or fixed.get('moving_mean_projection') is not False
                or common['parent_report_sha256']!=sha(a.comparison_parent_report)
                or common['parent_carrier_sha256']!=sha(a.comparison_parent_carrier)):
            raise ValueError('A fine continuation must retain its same fixed metric and comparison measure')
        J,N=int(report['J']),int(report['N']);rows=int(report['all_full_rows'])
        if rows%(3*N):raise ValueError('The complete current row count changed')
        P=rows//(3*N)
        read_payloads.append((report,('complete_current_parent_report',)))
        source_records.append(dict(role='complete_current_parent_report',path=str(a.parent_report.resolve()),
            sha256=sha(a.parent_report),final_bundle_sha256=current_bundle_sha))
        previous=report['amplitude_design_constraints']['budgets']
    algorithm_parent=parent if a.refinement_report is not None else report
    parent_spectral=algorithm_parent['final_statistics']['spectral']
    selected='phi_normalized' if a.uncentered_objective else 'centered_phi_normalized'
    if (algorithm_parent['target']!=a.target
            or algorithm_parent['selected_scalar_objective_key']!=selected
            or algorithm_parent['radial_weights']['legacy_fraction']!=a.legacy_fraction
            or algorithm_parent['angular_norm']['nu_c']!=a.angular_transition
            or algorithm_parent['coarse_low_modes']!=a.low_modes
            or any(parent_spectral[key]!=value for key,value in
                (('p',a.spectral_p),('epsilon',a.spectral_epsilon),('scale',a.spectral_scale)))):
        raise ValueError('This fixed-problem refinement keeps the actual parent objective, mother norm and stopping threshold')
    if a.angles!=N:
        raise ValueError('Use the actual transferred/current full-angle count; another angular refinement is explicit')
    ratio=a.angles//N
    if a.angles%N or ratio<1 or ratio&(ratio-1):
        raise ValueError('Retain every actual parent angle in a dyadic supergrid')
    if previous is not None and any(previous[key]!=value for key,value in
            (('marked_diameter_budget',a.marked_diameter_budget),
             ('witness_lower_budget',a.witness_lower_budget),('height_floor',a.amplitude_height_floor))):
        raise ValueError('Do not silently change established fixed amplitude budgets')
    points=history.Locations(J,P,N)
    for payload,path in read_payloads:points.walk(payload,path=path)
    for path in a.manifest:
        payload=json.loads(path.read_text())
        tag=payload.get('carrier_sha256',payload.get('observation_carrier_sha256'))
        if tag!=current_carrier_sha:
            raise ValueError('Every explicit extra location source must be on THIS actual new carrier')
        # Do not walk original provenance inside the NEW transfer record.
        if payload.get('schema')=='fixed-deep-scalar-exact-refinement-location-transfer-v1':
            payload={key:payload[key] for key in ('curvature_points','radius_points','protected_curvature_points')}
        points.walk(payload,path=('current_manifest',path.name))
        source_records.append(dict(role='explicit_current_location_source',path=str(path.resolve()),sha256=sha(path)))
    before=points.summary();resolved=points.resolve_grid(a.carrier);after=points.summary()
    if not after['curvature_numeric_tuples'] or not after['radius_numeric_tuples']:
        raise ValueError('Retain complete curvature and radius address sets')
    manifest=dict(schema='fixed-deep-scalar-complete-current-location-union-v1',
        carrier_sha256=current_carrier_sha,bundle_sha256=current_bundle_sha,
        fixed_scalar_metric_identity_sha256=identity,sources=source_records,**points.arrays())
    manifest_path.parent.mkdir(parents=True,exist_ok=False)
    manifest_path.write_text(json.dumps(manifest,separators=(',',':'),allow_nan=False)+'\n')
    return dict(manifest=str(manifest_path),manifest_sha256=sha(manifest_path),
        fixed_scalar_metric_identity_sha256=identity,actual_parent_bundle_sha256=current_bundle_sha,
        source_records=source_records,extraction_before_grid_resolution=before,
        resolved_grid_positions=resolved,resolved_position_counts=after,
        all_current_trial_active_final_positions_retained=True,
        no_old_carrier_grid_addresses_reinterpreted=True,
        field_evaluations=0,J_calls=0,Jtranspose_calls=0,
        coordinate_arrays_read=['observation_cells','observation_u'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','bundle','carrier','node-report','scalar-input','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    origin=p.add_mutually_exclusive_group(required=True)
    origin.add_argument('--refinement-report',type=Path)
    origin.add_argument('--parent-report',type=Path)
    p.add_argument('--comparison-parent-report',type=Path,required=True)
    p.add_argument('--comparison-parent-carrier',type=Path,required=True)
    p.add_argument('--manifest',type=Path,action='append',required=True)
    p.add_argument('--eta-start-node',type=int,required=True)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--legacy-fraction',type=float,default=.5)
    p.add_argument('--angular-transition',type=float,default=24.)
    p.add_argument('--low-modes',type=int,default=12)
    p.add_argument('--line-trials',type=int,default=15)
    p.add_argument('--reach-ratio',type=float,default=.03)
    p.add_argument('--curvature-cap',type=float)
    p.add_argument('--active-block-columns',type=int,default=32768)
    p.add_argument('--active-rank-tolerance',type=float,default=1e-10)
    p.add_argument('--active-top-curvature',type=int,default=16)
    p.add_argument('--active-top-radius',type=int,default=2)
    p.add_argument('--qp-feasibility-tolerance',type=float,default=2e-11)
    p.add_argument('--qp-row-rank-tolerance',type=float,default=2e-12)
    p.add_argument('--damping',type=float,required=True)
    p.add_argument('--marked-diameter-budget',type=float,required=True)
    p.add_argument('--witness-lower-budget',type=float,required=True)
    p.add_argument('--amplitude-height-floor',type=float,required=True)
    p.add_argument('--amplitude-top-radius',type=int,default=2)
    p.add_argument('--amplitude-top-distance',type=int,default=4)
    p.add_argument('--amplitude-active-band',type=float,default=.025)
    p.add_argument('--amplitude-budget-evidence',type=Path)
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
    p.add_argument('--target',type=float,required=True)
    p.add_argument('--scalar-admission-seconds',type=float,default=300.)
    p.add_argument('--scalar-integral-tolerance',default='1e-18')
    p.add_argument('--scalar-tail-cutoff',default='1/8')
    p.add_argument('--uncentered-objective',action='store_true')
    p.add_argument('--print-command',action='store_true')
    a=p.parse_args()
    if (min(a.amplitude_top_radius,a.amplitude_top_distance,a.stage_block,a.directions,a.maxiter,a.active_rows)<1
            or a.angles<4 or a.angles%4 or a.eta_start_node<1
            or not all(math.isfinite(v) for v in (a.marked_diameter_budget,a.witness_lower_budget,
                a.amplitude_height_floor,a.amplitude_active_band,a.damping,a.target,a.spectral_epsilon,a.spectral_scale))
            or not .002<a.marked_diameter_budget<=4.5 or a.witness_lower_budget<=0
            or a.amplitude_height_floor<=1 or a.amplitude_active_band<=0 or a.damping<=0 or a.target<=0
            or a.spectral_p<2 or a.spectral_p%2 or a.spectral_epsilon<=0 or a.spectral_scale<=0):
        raise ValueError('Use explicit valid fixed-target units, budgets and positive direction limits')
    repo,work,output=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    topic=repo/'topics/visible-flex-larger-amplitude';old=topic/'scripts/resume_20261120'
    source=Path(__file__).resolve().parent
    old_launcher=old/'launch_full_phi_exact_tail_actions.py'
    old_base=old/'launch_full_phi_qp_actions.py'
    for path,digest in ((old_launcher,OLD_LAUNCHER_SHA),(old_base,OLD_BASE_LAUNCHER_SHA)):
        if sha(path)!=digest:raise ValueError('Changed complete original argv preparation '+str(path))
    driver=source/'fullclosed_refined_deep_scalar_amplitude_qp.py'
    factory=source/'deep_valley_reference_factory.py';deep=source/'deep_valley_tail_input.py'
    coarse=source/'deep_scalar_coarse_moments.py'
    rows=source/'held_amplitude_inequalities_v2.py';screen=source/'held_amplitude_screen_v2.py'
    positions=work/(output.name+'-inputs')/'complete-current-positions.json'
    plan_path=work/(output.name+'-command.json')
    prepare=[sys.executable,str(old_launcher),'--repo',str(repo),'--work',str(work),
        '--bundle',str(a.bundle.resolve()),'--carrier',str(a.carrier.resolve()),
        '--node-report',str(a.node_report.resolve()),'--scalar-input',str(a.scalar_input.resolve()),
        '--manifest',str(positions),'--eta-start-node',str(a.eta_start_node),
        '--lambda-value','1','--source-lambda','1','--migration','keep-q','--outdir',str(output),
        '--damping',str(a.damping),'--maxiter',str(a.maxiter),'--directions',str(a.directions),
        '--active-rows',str(a.active_rows),'--qp-atol',str(a.qp_atol),'--qp-rtol',str(a.qp_rtol),
        '--reach-safety-factor',str(a.reach_safety_factor),'--active-band',str(a.active_band),'--print-command']
    if a.coarse_centers is not None:prepare.extend(['--coarse-centers',a.coarse_centers])
    prepared=subprocess.run(prepare,text=True,capture_output=True,check=True)
    command=shlex.split(prepared.stdout.strip())
    if len(command)<3 or Path(command[2]).name!='fullclosed_gauss_exact_tail_inequality_qp.py':
        raise ValueError('The original pure argv preparation changed layout')
    command[2]=str(driver)
    for flag,value in (('--exact-tail-source',factory),('--qp-source',source/'fullspace_feasible_active_pcg_v5.py'),
            ('--angles',a.angles),('--stage-block',a.stage_block),('--spectral-p',a.spectral_p),
            ('--spectral-epsilon',a.spectral_epsilon),('--spectral-scale',a.spectral_scale),('--target',a.target)):
        replace(command,flag,value)
    inherited_parameters={'legacy-fraction':a.legacy_fraction,'angular-transition':a.angular_transition,
        'low-modes':a.low_modes,'line-trials':a.line_trials,'reach-ratio':a.reach_ratio,
        'active-block-columns':a.active_block_columns,'active-rank-tolerance':a.active_rank_tolerance,
        'active-top-curvature':a.active_top_curvature,'active-top-radius':a.active_top_radius,
        'qp-feasibility-tolerance':a.qp_feasibility_tolerance,
        'qp-row-rank-tolerance':a.qp_row_rank_tolerance}
    if a.curvature_cap is not None:inherited_parameters['curvature-cap']=a.curvature_cap
    for key,value in inherited_parameters.items():
        flag='--'+key
        if flag in command:replace(command,flag,value)
        else:command.extend([flag,str(value)])
    additions={'comparison-parent-report':a.comparison_parent_report.resolve(),
        'comparison-parent-carrier':a.comparison_parent_carrier.resolve(),'deep-scalar-source':deep,'base-tail-source':old/'exact_reference_tail_lift.py',
        'scalar-coarse-source':coarse,'coarse-frame-source':old/'full_phi_coarse_frame.py',
        'coarse-v3-source':old/'fullspace_feasible_active_cg_v3.py',
        'coarse-moment-stage-block':a.coarse_moment_stage_block,
        'scalar-admission-seconds':a.scalar_admission_seconds,
        'scalar-integral-tolerance':a.scalar_integral_tolerance,'scalar-tail-cutoff':a.scalar_tail_cutoff,
        'amplitude-rows-source':rows,'amplitude-screen-source':screen,
        'marked-diameter-budget':a.marked_diameter_budget,'witness-lower-budget':a.witness_lower_budget,
        'amplitude-height-floor':a.amplitude_height_floor,'amplitude-top-radius':a.amplitude_top_radius,
        'amplitude-top-distance':a.amplitude_top_distance,'amplitude-active-band':a.amplitude_active_band}
    if not a.uncentered_objective:additions['centered-loss-source']=source/'centered_spectral_statistics.py'
    if a.amplitude_budget_evidence is not None:additions['amplitude-budget-evidence']=a.amplitude_budget_evidence.resolve()
    for flag,value in additions.items():command.extend(['--'+flag,str(value)])
    if a.print_command:print(shlex.join(command));return
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Scientific fixed-deep-scalar solving requires this public repository Actions')
    for path,digest in ((driver,DRIVER_SHA),(factory,FACTORY_SHA),(deep,DEEP_SHA),
            (coarse,COARSE_SHA),(rows,ROWS_SHA),(screen,SCREEN_SHA),
            (source/'refine_fixed_deep_scalar.py',TRANSFER_SHA)):
        if sha(path)!=digest:raise ValueError('Changed complete fixed-scalar source '+str(path))
    if output.exists() or positions.parent.exists() or plan_path.exists():
        raise FileExistsError('Use new actual solve, complete-position and command paths')
    position_record=complete_current_positions(a,old/'launch_refinement_from_full_report.py',positions)
    files={Path(__file__).resolve(),old_launcher,old_base,driver,factory,deep,coarse,rows,screen,
        old/'launch_refinement_from_full_report.py',positions,
        (a.refinement_report or a.parent_report).resolve(),
        a.comparison_parent_report.resolve(),a.comparison_parent_carrier.resolve(),
        source/'refine_fixed_deep_scalar.py',*(path.resolve() for path in a.manifest)}
    explicit={'--bundle','--observations','--operator','--implementation','--helpers',
        '--witness-input','--radius-witness-input','--tail-node-report','--tail-scalar-input',
        '--amplitude-budget-evidence'}
    for index,value in enumerate(command[:-1]):
        if value.startswith('--') and (value.endswith('-source') or value in explicit):
            files.add(Path(command[index+1]).resolve())
    file_records={str(path):dict(sha256=sha(path),bytes=path.stat().st_size) for path in sorted(files)}
    plan=dict(schema='complete-refined-fixed-deep-scalar-amplitude-PCG-command-v1',command=command,
        original_pure_argv_preparation=prepare,
        source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'),github_run_id=os.environ.get('GITHUB_RUN_ID'),
        source_sha256=sha(__file__),files=file_records,actual_parent_bundle_sha256=sha(a.bundle),
        complete_current_positions=position_record,
        fixed_scalar_metric_identity_sha256=position_record['fixed_scalar_metric_identity_sha256'],
        metric='g_n=ds^2+a_new(s)^2*dtheta^2',moving_mean_projection=False,
        comparison_parent_report_sha256=sha(a.comparison_parent_report),
        comparison_parent_carrier_sha256=sha(a.comparison_parent_carrier),
        common_parent_carrier_renormalization_from_existing_residual=True,
        full_original_metric_mean_rows_retained=True,old_metric_or_geometry_certificates_inherited=False,
        amplitude_budgets=dict(marked_diameter_budget=a.marked_diameter_budget,
            witness_lower_budget=a.witness_lower_budget,height_floor=a.amplitude_height_floor),
        initial_damping=a.damping,explicit_fixed_target_stopping_threshold=a.target,
        spectral=dict(p=a.spectral_p,epsilon=a.spectral_epsilon,scale=a.spectral_scale),
        spectral_normalization='k/(scale^2*C0) with THIS fixed-target residual and declared current positive observation measure',
        selected_scalar_objective_key='phi_normalized' if a.uncentered_objective else 'centered_phi_normalized',
        maximum_original_geometry_rows=a.active_rows,
        maximum_additional_amplitude_rows=a.amplitude_top_radius+2*a.amplitude_top_distance+2,
        no_original_row_or_variable_removed=True,new_automatic_fixture=False,
        no_cross_target_Phi_subtraction=True,continuous_metric_or_geometry_certified=False,
        fixed_g_refinement_convergence_claimed=False,topic_complete=False,output=str(output))
    plan_path.parent.mkdir(parents=True,exist_ok=True)
    plan_path.write_text(json.dumps(plan,indent=2,allow_nan=False)+'\n')
    env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    subprocess.run(command,cwd=repo,env=env,check=True)


if __name__=='__main__':main()

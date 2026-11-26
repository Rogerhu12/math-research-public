#!/usr/bin/env python3
"""Continue full fixed-deep-scalar q/core/H with finite same-parent separation SOC.

The prepare branch reads only actual new outputs and their transferred
addresses, never old ancestry locations under a new carrier. A solver parent
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

BASE_DRIVER_SHA='d3c35492a9cef5b4b005829f0ce502d8a377195541b64893f4ab063f0676ba95'
DRIVER_SHA='329ebd1828e12d18fcf89137ee0370b7ebafbb61644bbf7bc97cb0b26b284f90'
DERIVER_SHA='d80f9af278b89796d64cebf708080499cd44e3a8cde089be1009b7c26e2105ec'
SOC_SHA='f24765215124ce2615edd70fe15c9560000281938b254171a32dceb398e0e8ce'
PROJECTION_SHA='a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
FACTORY_SHA='4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'
DEEP_SHA='e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
COARSE_SHA='dcfa30b688104b27efeddfbe6921af25ba33ba6202be43f815d5b8d8bfc69395'
ROWS_SHA='d494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'
SCREEN_SHA='e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f'
HISTORY_SHA='4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
OLD_LAUNCHER_SHA='c9ba1d73db3e3608dffa1dbc9aeeda2a355d2ff4c2b9fc8eed2140c985869ec7'
OLD_BASE_LAUNCHER_SHA='6f021d459c24d5cb5a07853628d6a6a297332d51ad561beab2d09e50e2b34d63'
PARENT_SCHEMA='complete-fixed-deep-scalar-with-held-amplitude-budgets-v1'
SOC_PARENT_SCHEMA='complete-fixed-deep-scalar-amplitude-separated-SOC-v1'
PREPARATION_SCHEMA='deep-valley-fixed-scalar-keep-q-preparation-v1'


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


def complete_current_positions(a,history_path,manifest_path,*,deriver,source):
    history=load_bound('_deep_fixed_scalar_complete_history',history_path,HISTORY_SHA)
    current_carrier_sha=sha(a.carrier);current_bundle_sha=sha(a.bundle)
    source_records=[];read_payloads=[]
    if a.preparation_report is not None:
        report=json.loads(a.preparation_report.read_text())
        if report.get('schema')!=PREPARATION_SCHEMA or report.get('source',{}).get('sha256')!=FACTORY_SHA:
            raise ValueError('Use the actual complete byte-bound NEW scalar prepare report')
        actual_record(a.bundle,report['new_seed'],'new seed')
        actual_record(a.carrier,report['new_inputs']['observation_carrier'],'new observation carrier')
        actual_record(a.node_report,report['new_inputs']['node_report'],'new symbolic node report')
        actual_record(a.scalar_input,report['original_inputs']['scalar_input'],'unchanged original analytic input')
        context=report['exact_tail_context'];definition=context['definition']
        identity=report['fixed_scalar_metric_identity_sha256']
        if (report.get('fixed_new_scalar_metric') is not True
                or report.get('current_core_and_q_and_H_words_preserved') is not True
                or report.get('whole_new_seed_Gram_or_geometry_read_performed') is not False
                or definition.get('schema')!='deep-valley-fixed-scalar-fullclosed-lift-v1'
                or definition.get('target_is_a_moving_angular_mean') is not False
                or definition.get('profile_identity_sha256')!=identity
                or definition.get('eta_start_node')!=a.eta_start_node
                or definition.get('lambda_value')!=1.):
            raise ValueError('The prepared NEW scalar/profile and same eta must be explicit')
        candidates=[path for path in a.manifest if sha(path)==report['new_locations']['sha256']]
        if len(candidates)!=1:
            raise ValueError('Supply the actual complete new locations file once, with its recorded bytes')
        transferred=json.loads(candidates[0].read_text())
        if (transferred.get('schema')!='deep-valley-same-symbolic-location-transfer-v1'
                or transferred.get('carrier_sha256')!=current_carrier_sha
                or transferred.get('bundle_sha256')!=current_bundle_sha
                or transferred.get('same_literal_symbolic_mesh') is not True
                or transferred.get('only_locations_transferred') is not True
                or transferred.get('original_metric_or_geometry_values_transferred') is not False):
            raise ValueError('Use only the actual explicit same-symbolic new-carrier address transfer')
        J,P,N=int(report['J']),int(report['complete_observation_stages']),int(report['full_angles'])
        source_records.append(dict(role='actual_new_preparation_report',path=str(a.preparation_report.resolve()),
            sha256=sha(a.preparation_report),new_seed_sha256=current_bundle_sha,
            original_parent_bundle_sha256=report['original_inputs']['bundle']['sha256'],
            old_values_or_certificates_inherited=False))
        previous=None
    else:
        report=json.loads(a.parent_report.read_text())
        if (report.get('complete') is not True
                or report.get('final_bundle_sha256')!=current_bundle_sha
                or report.get('observation_carrier_sha256')!=current_carrier_sha
                or report.get('exact_tail_node_report_sha256')!=sha(a.node_report)
                or report.get('exact_tail_scalar_input_sha256')!=sha(a.scalar_input)
                or report.get('exact_tail_lambda')!=1.
                or report.get('exact_tail_eta_start_node')!=a.eta_start_node):
            raise ValueError('Use the actual completed same-fixed-scalar solver parent and same current inputs')
        if report.get('schema')==PARENT_SCHEMA:
            if report.get('source_sha256')!=BASE_DRIVER_SHA or sha(source/'fullclosed_deep_scalar_amplitude_qp.py')!=BASE_DRIVER_SHA:
                raise ValueError('The base parent must name the entire published d3c3 driver')
            for role,digest in deriver.EXPECTED_ROLES.items():
                if role not in ('typed_soc','soc_projection') and report['source_sha256_by_role'].get(role)!=digest:
                    raise ValueError('Changed actual complete fixed-scalar base parent role '+role)
            target_binding=deriver.verify_fixed_target(report)
            source_binding=dict(kind='literal entire published fixed-scalar base',driver_sha256=BASE_DRIVER_SHA,
                fixed_scalar_target=target_binding)
        elif report.get('schema')==SOC_PARENT_SCHEMA:
            source_binding=deriver.bind_report(report,source/'fullclosed_deep_amplitude_separation_soc.py',a.repo)
        else:
            raise ValueError('Use this exact fixed-scalar base or this whole-source-bound separated-SOC parent')
        fixed=report['fixed_scalar_metric'];identity=fixed['identity_sha256']
        if fixed.get('target_fixed_before_first_direction') is not True or fixed.get('moving_mean_projection') is not False:
            raise ValueError('No moving-mean target may enter a fixed deep-scalar continuation')
        J,N=int(report['J']),int(report['N']);rows=int(report['all_full_rows'])
        if rows%(3*N):raise ValueError('The complete current row count changed')
        P=rows//(3*N)
        read_payloads.append((report,('complete_current_parent_report',)))
        source_records.append(dict(role='complete_current_parent_report',path=str(a.parent_report.resolve()),
            sha256=sha(a.parent_report),final_bundle_sha256=current_bundle_sha,complete_source_binding=source_binding))
        previous=report['amplitude_design_constraints']['budgets']
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
        if payload.get('schema')=='deep-valley-same-symbolic-location-transfer-v1':
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
    origin.add_argument('--preparation-report',type=Path)
    origin.add_argument('--parent-report',type=Path)
    p.add_argument('--manifest',type=Path,action='append',required=True)
    p.add_argument('--eta-start-node',type=int,required=True)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--stage-block',type=int,default=64)
    damping=p.add_mutually_exclusive_group(required=True)
    damping.add_argument('--damping',type=float)
    damping.add_argument('--damping-from-parent',action='store_true')
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
    p.add_argument('--soc-tau',type=float,default=0.)
    p.add_argument('--soc-inward-fraction',type=float,default=.125)
    p.add_argument('--soc-max-rounds',type=int,choices=range(1,9),default=8)
    p.add_argument('--soc-separation',choices=('none','rejected-extrema'),default='rejected-extrema')
    a=p.parse_args()
    damping_origin=dict(kind='explicit current fixed-target value',value=a.damping)
    if a.damping_from_parent:
        if a.parent_report is None:raise ValueError('Read returned damping only from a real completed fixed-target solver parent')
        parent=json.loads(a.parent_report.read_text())
        objective='phi_normalized' if a.uncentered_objective else 'centered_phi_normalized'
        if (parent.get('complete') is not True or parent.get('final_bundle_sha256')!=sha(a.bundle)
                or parent.get('selected_scalar_objective_key')!=objective
                or any(parent['final_statistics']['spectral'][key]!=value for key,value in
                    (('p',a.spectral_p),('epsilon',a.spectral_epsilon),('scale',a.spectral_scale)))):
            raise ValueError('Parent-sourced damping needs this actual field and identical fixed-target functional units')
        a.damping=float(parent['final_damping'])
        damping_origin=dict(kind='actual completed same-fixed-target parent final_damping',value=a.damping,
            parent_report_sha256=sha(a.parent_report),parent_final_bundle_sha256=sha(a.bundle),
            actual_parent_solver_sha256=parent['source_sha256'])
    if (not all(math.isfinite(value) for value in (a.soc_tau,a.soc_inward_fraction))
            or min(a.soc_tau,a.soc_inward_fraction)<0 or a.soc_tau==a.soc_inward_fraction==0):
        raise ValueError('Use a declared positive finite inward policy and unchanged true thresholds')

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
    driver=source/'fullclosed_deep_amplitude_separation_soc.py'
    base_driver=source/'fullclosed_deep_scalar_amplitude_qp.py'
    deriver_path=source/'derive_deep_amplitude_separation_soc.py'
    typed_soc=source/'complete_deep_amplitude_rows_separation_soc.py'
    projection=source/'full_phi_all_rows_soc.py'
    deriver=load_bound('_deep_SOC_complete_whole_body_deriver',deriver_path,DERIVER_SHA)
    if sha(base_driver)!=BASE_DRIVER_SHA or driver.read_text()!=deriver.derive(base_driver):
        raise ValueError('Use the complete precisely derived fixed-deep-scalar SOC body')

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
    prepared=subprocess.run(prepare,text=True,capture_output=True,check=False)
    if prepared.returncode:
        if prepared.stdout:print(prepared.stdout,file=sys.stderr,flush=True)
        if prepared.stderr:print(prepared.stderr,file=sys.stderr,flush=True)
        raise subprocess.CalledProcessError(prepared.returncode,prepare,output=prepared.stdout,stderr=prepared.stderr)

    command=shlex.split(prepared.stdout.strip())
    if len(command)<3 or Path(command[2]).name!='fullclosed_gauss_exact_tail_inequality_qp.py':
        raise ValueError('The original pure argv preparation changed layout')
    command[2]=str(driver)
    for flag,value in (('--exact-tail-source',factory),('--qp-source',source/'fullspace_feasible_active_pcg_v5.py'),
            ('--angles',a.angles),('--stage-block',a.stage_block),('--spectral-p',a.spectral_p),
            ('--spectral-epsilon',a.spectral_epsilon),('--spectral-scale',a.spectral_scale),('--target',a.target)):
        replace(command,flag,value)
    additions={'deep-scalar-source':deep,'base-tail-source':old/'exact_reference_tail_lift.py',
        'scalar-coarse-source':coarse,'coarse-frame-source':old/'full_phi_coarse_frame.py',
        'coarse-v3-source':old/'fullspace_feasible_active_cg_v3.py',
        'coarse-moment-stage-block':a.coarse_moment_stage_block,
        'scalar-admission-seconds':a.scalar_admission_seconds,
        'scalar-integral-tolerance':a.scalar_integral_tolerance,'scalar-tail-cutoff':a.scalar_tail_cutoff,
        'amplitude-rows-source':rows,'amplitude-screen-source':screen,
        'marked-diameter-budget':a.marked_diameter_budget,'witness-lower-budget':a.witness_lower_budget,
        'amplitude-height-floor':a.amplitude_height_floor,'amplitude-top-radius':a.amplitude_top_radius,
        'amplitude-top-distance':a.amplitude_top_distance,'amplitude-active-band':a.amplitude_active_band,
        'typed-soc-source':typed_soc,'soc-projection-source':projection,
        'soc-tau':a.soc_tau,'soc-inward-fraction':a.soc_inward_fraction,
        'soc-max-rounds':a.soc_max_rounds,'soc-separation':a.soc_separation}

    if not a.uncentered_objective:additions['centered-loss-source']=source/'centered_spectral_statistics.py'
    if a.amplitude_budget_evidence is not None:additions['amplitude-budget-evidence']=a.amplitude_budget_evidence.resolve()
    for flag,value in additions.items():command.extend(['--'+flag,str(value)])
    if a.print_command:print(shlex.join(command));return
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Scientific fixed-deep-scalar solving requires this public repository Actions')
    for path,digest in ((driver,DRIVER_SHA),(factory,FACTORY_SHA),(deep,DEEP_SHA),
            (coarse,COARSE_SHA),(rows,ROWS_SHA),(screen,SCREEN_SHA),
            (typed_soc,SOC_SHA),(projection,PROJECTION_SHA),(deriver_path,DERIVER_SHA),(base_driver,BASE_DRIVER_SHA)):
        if sha(path)!=digest:raise ValueError('Changed complete fixed-scalar source '+str(path))
    if output.exists() or positions.parent.exists() or plan_path.exists():
        raise FileExistsError('Use new actual solve, complete-position and command paths')
    position_record=complete_current_positions(a,old/'launch_refinement_from_full_report.py',positions,deriver=deriver,source=source)
    files={Path(__file__).resolve(),old_launcher,old_base,driver,base_driver,deriver_path,typed_soc,projection,factory,deep,coarse,rows,screen,
        old/'launch_refinement_from_full_report.py',positions,
        (a.preparation_report or a.parent_report).resolve(),*(path.resolve() for path in a.manifest)}
    explicit={'--bundle','--observations','--operator','--implementation','--helpers',
        '--witness-input','--radius-witness-input','--tail-node-report','--tail-scalar-input',
        '--amplitude-budget-evidence'}
    for index,value in enumerate(command[:-1]):
        if value.startswith('--') and (value.endswith('-source') or value in explicit):
            files.add(Path(command[index+1]).resolve())
    file_records={str(path):dict(sha256=sha(path),bytes=path.stat().st_size) for path in sorted(files)}
    plan=dict(schema='complete-fixed-deep-scalar-amplitude-separated-SOC-command-v1',command=command,
        original_pure_argv_preparation=prepare,
        source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'),github_run_id=os.environ.get('GITHUB_RUN_ID'),
        source_sha256=sha(__file__),files=file_records,actual_parent_bundle_sha256=sha(a.bundle),
        complete_current_positions=position_record,
        fixed_scalar_metric_identity_sha256=position_record['fixed_scalar_metric_identity_sha256'],
        metric='g_n=ds^2+a_new(s)^2*dtheta^2',moving_mean_projection=False,
        full_original_metric_mean_rows_retained=True,old_metric_or_geometry_certificates_inherited=False,
        amplitude_budgets=dict(marked_diameter_budget=a.marked_diameter_budget,
            witness_lower_budget=a.witness_lower_budget,height_floor=a.amplitude_height_floor),
        initial_damping=a.damping,damping_source=damping_origin,
        complete_driver_derivation=deriver.lineage(),
        complete_SOC=dict(tau=a.soc_tau,inward_fraction=a.soc_inward_fraction,
            maximum_rounds=a.soc_max_rounds,separation=a.soc_separation,
            every_original_row_retained=True,each_round_keeps_original_parent_and_d=True,
            every_corrected_Az_and_true_objective_geometry_read_independent=True,
            single_append_only_capacity_cache=True,unused_capacity_never_enters_projection=True,
            old_R671_canonical_identity_inherited=False,continuous_correction_certified=False),
        explicit_fixed_target_stopping_threshold=a.target,

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

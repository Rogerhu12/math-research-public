#!/usr/bin/env python3
"""Prepare an explicit NEW fixed deep-scalar seed from a complete old parent.

Only old addresses are transferred. The complete report/trial/active/final
position union is read against its actual original carrier first. The new
factory then writes a new scalar target, seed, carrier, nodes and location
manifest. No old field value, direction or geometry certificate transfers.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys

FACTORY_SHA='4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'
DEEP_SHA='e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
COLLECTOR_SHA='e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4'
HISTORY_SHA='4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def load_bound(path,digest):
    if sha(path)!=digest:raise ValueError('Changed complete history source '+str(path))
    spec=importlib.util.spec_from_file_location('_deep_scalar_complete_old_history',path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module);return module


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','bundle','parent-report','carrier','node-report','scalar-input','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--manifest',type=Path,action='append',required=True)
    p.add_argument('--eta-start-node',type=int,required=True)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--scalar-admission-seconds',type=float,default=300.)
    p.add_argument('--scalar-integral-tolerance',default='1e-18')
    p.add_argument('--scalar-tail-cutoff',default='1/8')
    p.add_argument('--print-command',action='store_true')
    a=p.parse_args()
    repo,work,output=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    topic=repo/'topics/visible-flex-larger-amplitude';old=topic/'scripts/resume_20261120'
    source=Path(__file__).resolve().parent;notes=topic/'notes'
    factory=source/'deep_valley_reference_factory.py';deep=source/'deep_valley_tail_input.py'
    collector=source/'launch_mean_metric_design_actions.py'
    history=old/'launch_refinement_from_full_report.py'
    locations=work/(output.name+'-source-inputs')/'complete-old-parent-positions.json'
    plan_path=work/(output.name+'-prepare-command.json')
    named={
        'bundle':a.bundle.resolve(),'observations':a.carrier.resolve(),
        'node-report':a.node_report.resolve(),'scalar-input':a.scalar_input.resolve(),
        'scalar-source':notes/'2026-11-17-parallel-model-full-hold-oracle.py',
        'integer-source':notes/'2026-11-17-parallel-inward-integral-enclosure.py',
        'hold-source':topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py',
        'observed-source':old/'gauss_observed_closed_gram.py',
        'operator-source':notes/'2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
        'batch-source':topic/'scripts/resume_20261120_batched_closed_gram.py'}
    command=[sys.executable,'-u',str(factory)]
    for flag,value in named.items():command.extend(['--'+flag,str(value)])
    for flag,value in (('eta-start-node',a.eta_start_node),('angles',a.angles),
            ('stage-block',a.stage_block),('scalar-admission-seconds',a.scalar_admission_seconds),
            ('scalar-integral-tolerance',a.scalar_integral_tolerance),('scalar-tail-cutoff',a.scalar_tail_cutoff),
            ('witness-input',locations),('radius-witness-input',locations),('outdir',output)):
        command.extend(['--'+flag,str(value)])
    if a.print_command:print(shlex.join(command));return
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Scientific new scalar preparation requires this public repository Actions')
    for path,digest in ((factory,FACTORY_SHA),(deep,DEEP_SHA),(history,HISTORY_SHA)):
        if sha(path)!=digest:raise ValueError('Changed complete new-scalar preparation source '+str(path))
    if output.exists() or locations.parent.exists() or plan_path.exists():
        raise FileExistsError('Use new seed, source-address union and command paths')
    parent=json.loads(a.parent_report.read_text())
    if (parent.get('exact_tail_lambda')!=1. or parent.get('exact_tail_eta_start_node')!=a.eta_start_node
            or parent.get('exact_tail_node_report_sha256')!=sha(a.node_report)
            or parent.get('exact_tail_scalar_input_sha256')!=sha(a.scalar_input)):
        raise ValueError('Bind the actual original lambda=1 model, eta, scalar and symbolic nodes')
    parentN=int(parent['N']);ratio=a.angles//parentN
    if a.angles%parentN or ratio<1 or ratio&(ratio-1):
        raise ValueError('Retain every actual original angle in a dyadic supergrid')
    helper=load_bound(collector,COLLECTOR_SHA)
    positions=helper.complete_positions(a,history,locations)
    files={Path(__file__).resolve(),factory,deep,collector,history,
        old/'exact_reference_tail_lift.py',a.parent_report.resolve(),*named.values(),
        *(path.resolve() for path in a.manifest),locations}
    records={str(path):dict(sha256=sha(path),bytes=path.stat().st_size) for path in sorted(files)}
    plan=dict(schema='complete-old-parent-to-new-deep-scalar-preparation-command-v1',
        source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'),github_run_id=os.environ.get('GITHUB_RUN_ID'),
        source_sha256=sha(__file__),command=command,files=records,
        original_parent_bundle_sha256=sha(a.bundle),original_parent_report_sha256=sha(a.parent_report),
        complete_original_position_union=positions,
        fixed_new_scalar_metric='g_n=ds^2+a_new(s)^2*dtheta^2',moving_angular_mean_target=False,
        all_original_coordinates_retained=True,only_positions_transferred=True,
        old_directions_or_field_values_or_certificates_inherited=False,
        no_nonlinear_solve_performed_by_preparation=True,output=str(output))
    plan_path.parent.mkdir(parents=True,exist_ok=True)
    plan_path.write_text(json.dumps(plan,indent=2,allow_nan=False)+'\n')
    env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
        OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    subprocess.run(command,cwd=repo,env=env,check=True)


if __name__=='__main__':main()

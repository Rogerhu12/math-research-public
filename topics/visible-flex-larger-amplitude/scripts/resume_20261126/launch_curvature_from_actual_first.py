#!/usr/bin/env python3
"""Run R686 with the exact reach target derived from ACTUAL same-field D.

No field is changed and no desired diameter is substituted for a bound.
The child keeps its own corrected R686 schema, source identity and journal.
This launcher pays only report arithmetic; the child does actual interval K.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time


SCHEMA = 'R686-curvature-admission-from-actual-R674-diameter-v1'
PREVIOUS_SHA = '521187ae2df4225ddbda6efd8326db760d2f1bd5bd184a74f3a816408ad19e6c'
PRODUCER_SHA = 'ee3744b39bcb3183931b73f25a34ca390c523a2456737915cf359a7f1c4e7d31'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def outside(path, repo):
    path = Path(path).resolve()
    try:
        path.relative_to(Path(repo).resolve())
    except ValueError:
        return path
    raise ValueError('Generated reports and journals must remain outside the repository')


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp-'+str(os.getpid()))
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n')
    os.replace(temporary,path)


def main():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific report arithmetic and K calculation require public Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo','bundle','node-report','scalar-input','reference-carrier','first-geometry','journal','out'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--admission-record',type=Path)
    parser.add_argument('--resume',action='store_true')
    parser.add_argument('--levels',default='256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96')
    parser.add_argument('--budget-seconds',type=float,default=600.)
    parser.add_argument('--workers',type=int,default=4)
    parser.add_argument('--radial-block',type=int,default=4)
    parser.add_argument('--taylor-degree',type=int,default=12)
    parser.add_argument('--scalar-degree',type=int,default=5)
    parser.add_argument('--panels',type=int,default=128)
    args=parser.parse_args()
    args.repo=args.repo.resolve()
    args.out=outside(args.out,args.repo)
    args.journal=outside(args.journal,args.repo)
    args.admission_record=outside(args.admission_record or args.out.with_name(args.out.stem+'-admission.json'),args.repo)
    if args.out.exists() or args.admission_record.exists():
        raise FileExistsError('Preserve prior actual curvature and admission records')
    if args.admission_record==args.out:
        raise ValueError('Separate the K result and admission provenance files')
    previous_path=args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_geometry_combine_v2.py'
    producer_path=args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/actions_batched_closed_curvature.py'
    if sha(previous_path)!=PREVIOUS_SHA or sha(producer_path)!=PRODUCER_SHA:
        raise ValueError('Frozen identity helper or corrected R686 source changed')
    spec=importlib.util.spec_from_file_location('_R686_admission_first_identity',previous_path)
    old=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=old
    spec.loader.exec_module(old)
    b,_=old.arithmetic(args.repo)
    issues=[]
    actual={key:b.identity(getattr(args,key),issues,key) for key in ('bundle','node_report')}
    node=b.read_json(args.node_report,issues,'Actual node report')
    first=b.read_json(args.first_geometry,issues,'Actual first geometry')
    literal,model=old.literal_bundle(args.bundle,b,issues)
    old.report_identity(first,'first',actual,literal,model,node,b,issues)
    J=len(node.get('true_scalar_nodes',[]))
    rows=first.get('records',[])
    expected=list(range(max(0,J-1)))
    get=b.rational
    positive=lambda value:value is not None and value>0
    full=bool(J>=2 and first.get('complete_scope') is True and first.get('covered_cells')==expected
        and [row.get('cell') for row in rows]==expected)
    b.demand(full,issues,'First report does not cover every actual original cell')
    row_paid=lambda row:(all(positive(get(row.get(key))) for key in
        ('support_lower','minimum_E_lower','minimum_normal_squared_lower'))
        and row.get('unpaid_immersion_boxes')==0)
    caps=first.get('cap_bounds',{})
    b.demand(first.get('embedding_certified') is True and all(row_paid(row) for row in rows)
        and all(positive(get(first.get(key))) for key in ('covered_support_lower','covered_minimum_E_lower',
            'covered_minimum_normal_squared_lower','core_rho_continuous_lower'))
        and positive(get(caps.get('support_lower')))
        and caps.get('upper_and_reflected_lower_flat_disks') is True
        and first.get('exact_closed_caps_and_reflection_included') is True,
        issues,'Complete closed first-geometry hypotheses are unpaid')
    radius=node.get('scalar',{}).get('R',{})
    R=b.exact_box([radius.get('lower_exact'),radius.get('upper_exact')])
    H=literal.get('Hcap')
    b.demand(get(first.get('beta_exact'))==F(1,4) and H is not None and H>1
        and R is not None and R[0]>F(9,20),issues,'R661 marker hypotheses are unpaid')
    b.demand(sha(args.scalar_input)==model.get('scalar_input_sha256'),issues,
        'Requested K scalar input differs from the first report canonical definition')
    b.demand(first.get('source_inputs',{}).get('reference_carrier',{}).get('sha256')==sha(args.reference_carrier),
        issues,'Use the actual same first-report reference profile carrier')
    D=get(first.get('continuous_diameter_upper'))
    b.demand(positive(D),issues,'No actual complete body diameter upper bound')
    if issues:
        raise ValueError('K admission rejected unpaid inputs: '+json.dumps(issues))
    marked_D=D+F(1,500)
    support=min(get(first['covered_support_lower']),F(64,267))
    target=F(100,3)/marked_D
    if support<F(3,100)*marked_D:
        raise ValueError('The actual same-field support bound is insufficient for 3% reach; improve it or change the candidate before K')
    if target<F(5):
        raise ValueError('The published fixed-marker K<=5 alone does not pay 3% reach at this actual D')
    command=[sys.executable,'-u',str(producer_path),'--repo',str(args.repo),'--model','reference',
        '--bundle',str(args.bundle.resolve()),'--node-report',str(args.node_report.resolve()),
        '--scalar-input',str(args.scalar_input.resolve()),'--reference-carrier',str(args.reference_carrier.resolve()),
        '--first-geometry-report',str(args.first_geometry.resolve()),'--journal',str(args.journal),
        '--out',str(args.out),'--cells','all','--target',str(target),'--levels',args.levels,
        '--budget-seconds',str(args.budget_seconds),'--workers',str(args.workers),
        '--radial-block',str(args.radial_block),'--taylor-degree',str(args.taylor_degree),
        '--scalar-degree',str(args.scalar_degree),'--panels',str(args.panels),'--beta','1/4']
    if args.resume:
        command.append('--resume')
    started=time.monotonic()
    report=dict(schema=SCHEMA,source_sha256=sha(__file__),curvature_producer_sha256=PRODUCER_SHA,
        first_identity_helper_sha256=PREVIOUS_SHA,
        execution={key:os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')},
        actual_source_commit=subprocess.check_output(['git','-C',str(args.repo),'rev-parse','HEAD'],text=True).strip(),
        current_bundle_sha256=actual['bundle']['sha256'],current_node_report_sha256=actual['node_report']['sha256'],
        first_geometry_report_sha256=sha(args.first_geometry),model_identity_sha256=literal['model_identity_sha256'],
        body_diameter_upper_exact=str(D),marked_diameter_upper_exact=str(marked_D),
        marked_support_lower_exact=str(support),reach_ratio_target_exact='3/100',
        derived_body_curvature_target_exact=str(target),marker_curvature_upper_exact='5',
        derivation='min(marked_support,1/max(K,5))/(actual_D+2/1000)>=3/100 when K<=100/(3*(actual_D+2/1000))',
        desired_diameter_substituted=False,extra_safety_factor_exact='1',
        journal=str(args.journal),resume=args.resume,command=command,
        state='child_running',child_returncode=None,curvature_report_sha256=None,
        geometric_targets_certified=False,metric_certified=False,topic_completion_certified=False)
    write_json(args.admission_record,report)
    print(json.dumps(dict(event='R686_actual_diameter_K_admission',bundle_sha256=actual['bundle']['sha256'],
        body_D_upper_exact=str(D),marked_D_upper_exact=str(marked_D),K_target_exact=str(target),
        first_geometry_report_sha256=report['first_geometry_report_sha256'])),flush=True)
    process=subprocess.run(command,check=False)
    report.update(state='child_returned' if process.returncode==0 else 'child_failed',
        child_returncode=process.returncode,seconds=time.monotonic()-started,
        curvature_report_sha256=sha(args.out) if args.out.exists() else None)
    write_json(args.admission_record,report)
    print(json.dumps(dict(event='R686_actual_diameter_K_return',returncode=process.returncode,
        admission_record_sha256=sha(args.admission_record),curvature_report_sha256=report['curvature_report_sha256'],
        K_target_exact=str(target),seconds=report['seconds'])),flush=True)
    if process.returncode:
        raise SystemExit(process.returncode if process.returncode>0 else 1)


if __name__=='__main__':
    main()

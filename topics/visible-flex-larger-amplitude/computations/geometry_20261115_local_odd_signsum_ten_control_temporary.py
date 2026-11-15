#!/usr/bin/env python3
"""Request174 one independent new-shape child, complete compact lifecycle.

This file imports no numerical source. Public Actions owns all science.
The original rules runner owns the same process group. The explicit
whole-child wall deadline and original producer checkpoint are separate
resource safeguards, never substitute mathematical acceptance tests.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback
import uuid

HERE=Path(__file__).resolve().parent
ENTRY='geometry_20261115_local_odd_signsum_ten_control_temporary.py'
SCIENCE='geometry_20261115_local_odd_signsum_ten_control_recipe.py'
SCIENCE_SHA='975bb25f1dd879bd88dc1a3b1df451836cadceca1695820050bfe3842efd949f'
READER='root_20261115_local_odd_signsum_ten_control_scalar_readout.py'
READER_SHA='fad015510fcd230211dbff2c12c487a1df4a61d8bdebd6fa97e1f64c8f520037'
SCIENCE_SCHEMA='R259-all-station-fixed-odd-signsum-ten-control-one-real-full3-direction-v1'
STATUS_NAME='local-odd-signsum-ten-control-status.json'
REQUEST_SCHEMA='public-local-odd-signsum-ten-control-real-direction-request-v1'
RECIPE_SCHEMA='R259-actual157-to-independent-local-odd-signsum-ten-control-recipe-v1'
SCHEMA='request174-one-fixed-local-odd-signsum-ten-control-temporary-experiment-v1'
LIMIT=90000
CONTRACT=dict(max_experiments=1,actual_new_shape_directions=1,
    complete_original_real_backtracks=20,all_allowed_station_catalogue=True,
    all_centers_widths_signs_frozen_before_ten_model=True,
    old_nine_coefficients_fixed=True,independent_parameter_dimension=10,
    initial_added_coefficient='0',explicit_absolute_added_step='1',
    parent_radius_is_provenance_only=True,extra_rank_or_response_agreement_gate=False)


def encoded(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=True,allow_nan=False,
                      separators=(',',':')).encode('ascii')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def receipt(path):
    path=Path(path);h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return dict(file=path.name,bytes=path.stat().st_size,sha256=h.hexdigest())


def atomic(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix('.pending')
    tmp.write_bytes(encoded(value)+b'\n');os.replace(tmp,path)


def require_actions():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise RuntimeError('Execute only in this public repository Actions')


def child_environment():
    env=dict(os.environ)
    for name in list(env):
        if name in ('GITHUB_OUTPUT','GH_TOKEN','GITHUB_TOKEN','MR_TOKEN','MR_READ_TOKEN','GIT_ASKPASS','SSH_ASKPASS') or name.startswith('GIT_CONFIG_'):
            env.pop(name,None)
    return env


def bind(args):
    raw=args.request.read_bytes()
    if digest(raw)!=args.request_sha256:
        raise ValueError('Bind the complete actual request')
    r=json.loads(raw)
    if (r.get('schema')!=REQUEST_SCHEMA or r.get('request_number')!=174
            or r.get('repository')!='Rogerhu12/math-research-public'
            or r.get('execution_entry')!=ENTRY or r.get('scientific_entry')!=SCIENCE
            or r.get('experiment_contract')!=CONTRACT):
        raise ValueError('Keep this single independent new-family experiment identity')
    for table,count in (('source_sha256',113),('workflow_support_source_sha256',10)):
        if len(r[table])!=count:
            raise ValueError('Retain all actual157 ancestors and current independent source pins')
        for name,wanted in r[table].items():
            if Path(name).name!=name or digest((HERE/name).read_bytes())!=wanted:
                raise ValueError('Pinned source differs: '+name)
    if r['source_sha256'][SCIENCE]!=SCIENCE_SHA or r['workflow_support_source_sha256'][READER]!=READER_SHA:
        raise ValueError('Do not substitute a producer or scalar reader')
    parent=r['source_closure']['origin_producer'];current=r['source_closure']['current_producer']
    additions=r['source_closure']['new_current_consumed_names']
    if len(parent)!=41 or len(current)!=46 or len(additions)!=5:
        raise ValueError('Keep the exact41-to46 current producer closure')
    if current!={**parent,**{name:r['source_sha256'][name] for name in additions}}:
        raise ValueError('Current producer sources differ')
    if not all(r['source_sha256'].get(name)==value for name,value in current.items()):
        raise ValueError('Every consumed source must be in the whole request source table')
    resource=r['resource_contract']
    if (resource['producer_wall_seconds'],resource['whole_child_wall_seconds'],
        resource['termination_grace_seconds'],resource['metadata_reader_wall_seconds'])!=(2400,2400,90,300):
        raise ValueError('Keep the explicit independent resource contract')
    item=r['parameter_recipe'];rel=Path(item['file'])
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('The recipe is an explicit relative source-tree text')
    recipe_path=args.repository_directory.resolve()/rel
    recipe_raw=recipe_path.read_bytes();recipe=json.loads(recipe_raw)
    if len(recipe_raw)!=item['bytes'] or digest(recipe_raw)!=item['sha256'] or recipe.get('schema')!=RECIPE_SCHEMA:
        raise ValueError('Bind the complete actual157-to-independent-ten recipe')
    if (recipe['origin']!=item['origin']
            or recipe['original_nine_literal_parameters']!=r['diagnostic']['original_nine_literal_parameters']
            or recipe['parent_relative_trust_radius']!=r['diagnostic']['parent_relative_trust_radius']
            or recipe['policy']!=r['scientific_policy']
            or recipe['input_sha256']!={name:value['sha256'] for name,value in r['inputs'].items()}):
        raise ValueError('The actual source/parent/literal recipe differs')
    inputs=json.loads(args.original_input_paths.read_bytes())
    if set(inputs)!=set(r['inputs']):
        raise ValueError('All four original mathematical inputs are required')
    for name,path in inputs.items():
        actual=receipt(path);expected=r['inputs'][name]
        if actual['bytes']!=expected['bytes'] or actual['sha256']!=expected['sha256']:
            raise ValueError('Original input byte identity differs: '+name)
    if args.out.is_symlink():
        raise ValueError('The output is a request-owned temporary directory')
    args.out.resolve().relative_to(Path(os.environ['RUNNER_TEMP']).resolve())
    return r,recipe_path,inputs


class Processes:
    def __init__(self):
        self.active=None
        self.received_signal=None
        self.wall_terminated=False

    def interrupted(self,signum,frame):
        self.received_signal=signum
        if self.active is not None and self.active.poll() is None:
            try:self.active.send_signal(signum)
            except ProcessLookupError:pass

    def run(self,argv,stdout,stderr,*,wall_seconds,grace_seconds,status=None):
        started=time.monotonic();last_progress=started
        sent=None
        with stdout.open('wb') as out,stderr.open('wb') as err:
            self.active=subprocess.Popen(argv,cwd=HERE,env=child_environment(),
                stdout=out,stderr=err,shell=False)
            try:
                while self.active.poll() is None:
                    now=time.monotonic()
                    if sent is None and now-started>=wall_seconds:
                        self.wall_terminated=True;sent=now
                        self.active.send_signal(signal.SIGTERM)
                        print(encoded(dict(event='request174-explicit-resource-stop',
                            whole_child_wall_seconds=wall_seconds,
                            mathematical_rejection_not_inferred=True,
                            child_receives_original_checkpoint_signal=True)).decode(),flush=True)
                    if self.received_signal is not None and sent is None:
                        sent=now
                    if sent is not None and now-sent>=grace_seconds:
                        self.active.kill()
                    if status is not None and now-last_progress>=60:
                        last_progress=now
                        progress=dict(event='request174-original-status-progress',elapsed_seconds=now-started)
                        try:
                            value=json.loads(status.read_bytes())
                            for key in ('phase','frozen_shape_selected','accepted_point_count',
                                        'unvisited_real_trial_indices','resource_partial'):
                                if key in value:progress[key]=value[key]
                            progress['scientific_status_identity']=receipt(status)
                        except (OSError,ValueError) as error:
                            progress['partial_status_read_error']=repr(error)
                        print(encoded(progress).decode(),flush=True)
                    time.sleep(.25)
                return self.active.wait()
            finally:
                if self.active.poll() is None:
                    self.active.send_signal(signal.SIGTERM)
                    try:self.active.wait(timeout=grace_seconds)
                    except subprocess.TimeoutExpired:self.active.kill();self.active.wait()
                self.active=None


def scientific_argv(inputs,recipe,out,request):
    argv=[sys.executable,'-u',str(HERE/SCIENCE)]
    for name in ('accepted','prepared','tail_anchor','tail_config'):
        argv+=['--'+name.replace('_','-'),inputs[name]]
    return argv+['--parameter-recipe',str(recipe),'--parameter-recipe-sha256',request['parameter_recipe']['sha256'],
        '--out',str(out),'--backtracks','20','--decimal-digits','50',
        '--interval-bits','160','--interval-depth','14','--wall-seconds','2400']


def collect_status(out,request=None):
    path=out/'science'/STATUS_NAME
    if not path.is_file():
        return None,dict(present=False)
    value=json.loads(path.read_bytes())
    if value.get('schema')!=SCIENCE_SCHEMA or value.get('source_sha256')!=SCIENCE_SHA:
        raise ValueError('Do not relabel any old or different producer status')
    if request is not None and value.get('consumed_source_sha256')!=request['source_closure']['current_producer']:
        raise ValueError('Actual consumed source closure differs')
    return value,dict(present=True,original=receipt(path),schema=value['schema'],
        consumed_source_count=len(value.get('consumed_source_sha256',{})),
        consumed_source_identity=digest(encoded(value.get('consumed_source_sha256',{}))))


def readout(processes,out,rules,compute_outcome,wall=300):
    if digest((HERE/READER).read_bytes())!=READER_SHA:
        raise ValueError('Use the explicit compact reader source')
    directory=out/'readback'
    argv=[sys.executable,'-u',str(HERE/READER),'--directory',str(out/'science'),
        '--out',str(directory),'--rules-directory',str(rules),'--compute-outcome',compute_outcome]
    code=processes.run(argv,out/'reader-stdout.txt',out/'reader-stderr.txt',
        wall_seconds=wall,grace_seconds=30)
    path=directory/'compact-summary.json'
    return code,path.read_bytes() if path.is_file() else None


def run(args):
    require_actions()
    request,recipe,inputs=bind(args)
    if args.out.exists() and any(args.out.iterdir()):
        raise ValueError('Use a fresh request-owned output directory')
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/'request.json').write_bytes(args.request.read_bytes())
    metadata=dict(schema=SCHEMA,request_number=174,run_id=os.environ['GITHUB_RUN_ID'],
        source_commit=os.environ['GITHUB_SHA'],request_sha256=args.request_sha256,
        wrapper_source=receipt(__file__),current_producer_sha256=SCIENCE_SHA,
        parameter_recipe=request['parameter_recipe'],experiment_contract=CONTRACT,
        started_experiments=1,completed_experiments=0,child_exit_code=None,
        reader_exit_code=None,partial=True,wrapper_exception=None,
        raw_Git_Release_or_artifact_retention=False,scientific_native_acceptance_claimed=False)
    processes=Processes();old={}
    for sig in (signal.SIGTERM,signal.SIGINT):
        old[sig]=signal.signal(sig,processes.interrupted)
    started=time.monotonic();code=1
    try:
        atomic(args.out/'run-metadata.json',metadata)
        argv=scientific_argv(inputs,recipe,args.out/'science',request)
        print(encoded(dict(event='request174-actual-scientific-argv',argv=argv,
            full_current_ten_model_reformed=True,no_old_status_J_or_FD_adopted=True,
            all_original_full3_acceptance_and_projection_final_consumers_retained=True)).decode(),flush=True)
        code=processes.run(argv,args.out/'producer-stdout.txt',args.out/'producer-stderr.txt',
            wall_seconds=2400,grace_seconds=90,status=args.out/'science'/STATUS_NAME)
        metadata.update(child_exit_code=code,received_signal=processes.received_signal,
            explicit_wall_termination=processes.wall_terminated,
            producer_stdout=receipt(args.out/'producer-stdout.txt'),
            producer_stderr=receipt(args.out/'producer-stderr.txt'))
        atomic(args.out/'run-metadata.json',metadata)
        reader_code,compact=readout(processes,args.out,args.rules_directory,
            'success' if code==0 else 'failure-or-resource-partial')
        metadata['reader_exit_code']=reader_code
        status,status_receipt=collect_status(args.out,request)
        metadata['actual_status']=status_receipt
        complete=bool(code==0 and status and status.get('diagnostic_completed') and status.get('phase')=='diagnostic-completed')
        metadata.update(completed_experiments=int(complete),
            scientific_diagnostic_completed=complete,
            scientific_stop_reason=status.get('stop_reason') if status else None,
            accepted_point_count=status.get('accepted_point_count') if status else None,
            frozen_shape_selected=status.get('frozen_shape_selected') if status else False,
            station_catalogue_complete=bool(status and (status.get('station_catalogue') or {}).get('complete')),
            unvisited_station_groups=(status.get('station_catalogue') or {}).get('unvisited_unique_group_ids') if status else None,
            unvisited_real_trial_indices=status.get('unvisited_real_trial_indices') if status else list(range(20)),
            partial=not(complete and reader_code==0),
            scientific_failure_not_inferred_from_resource_or_readout=True)
        code=0 if complete and reader_code==0 else (code if code>0 else 70)
    except Exception as error:
        metadata.update(wrapper_exception=repr(error),traceback=traceback.format_exc(),
            partial=True,scientific_completion_not_inferred=True)
        code=70
    finally:
        metadata['wrapper_wall_seconds']=time.monotonic()-started
        atomic(args.out/'run-metadata.json',metadata)
        for sig,handler in old.items():signal.signal(sig,handler)
    return code


def report(args):
    require_actions()
    args.out.mkdir(parents=True,exist_ok=True)
    path=args.out/'run-metadata.json'
    metadata=json.loads(path.read_bytes()) if path.is_file() else dict(schema=SCHEMA,
        request_number=174,run_id=os.environ['GITHUB_RUN_ID'],source_commit=os.environ['GITHUB_SHA'],
        partial=True,wrapper_exception='No complete wrapper metadata')
    compact_path=args.out/'readback'/'compact-summary.json'
    if not compact_path.is_file():
        try:
            code,_=readout(Processes(),args.out,args.rules_directory,args.compute_outcome)
            metadata['post_step_reader_exit_code']=code
        except Exception as error:
            metadata['post_step_reader_exception']=repr(error)
    if compact_path.is_file():
        raw=compact_path.read_bytes();value=json.loads(raw)
        original=dict(bytes=len(raw),sha256=digest(raw))
    else:
        value=dict(schema='request174-original-status-and-readback-unavailable-v1',
            scientific_completion_not_claimed=True,scientific_failure_not_inferred=True)
        original=None
    value['temporary_wrapper']=dict(**{key:metadata.get(key) for key in (
        'schema','request_number','run_id','source_commit','request_sha256','wrapper_source',
        'started_experiments','completed_experiments','child_exit_code','reader_exit_code',
        'post_step_reader_exit_code','post_step_reader_exception','received_signal',
        'explicit_wall_termination','scientific_diagnostic_completed','scientific_stop_reason',
        'partial','wrapper_exception','traceback','wrapper_wall_seconds','producer_stdout','producer_stderr')},
        compact_reader_output_identity=original,actual_scientific_step_outcome=args.compute_outcome,
        report_did_not_run_or_resume_science=True)
    raw=encoded(value)
    if len(raw)>LIMIT:
        value=dict(schema='request174-final-report-over-budget-v1',
            original_full_compact_report_identity=dict(bytes=len(raw),sha256=digest(raw)),
            original_reader_output_identity=original,
            original_status=value.get('original_status'),phase=value.get('phase'),
            accepted_point_count=value.get('accepted_point_count'),stop_reason=value.get('stop_reason'),
            compact_readback_not_transported_completely=True,
            scientific_failure_not_inferred_from_transport=True,
            wrapper_failure=metadata.get('wrapper_exception'))
        raw=encoded(value);code=70
    else:
        code=0
    (args.out/'report-summary.json').write_bytes(raw)
    token='VISIBLE174_'+uuid.uuid4().hex
    with open(os.environ['GITHUB_OUTPUT'],'a',encoding='utf-8') as stream:
        stream.write('compact_summary<<'+token+'\n'+raw.decode('ascii')+'\n'+token+'\n')
        stream.write('compact_summary_bytes='+str(len(raw))+'\ncompact_summary_sha256='+digest(raw)+'\n')
    print('BEGIN_VISIBLE174_COMPACT_SUMMARY',flush=True)
    print(raw.decode('ascii'),flush=True)
    print('END_VISIBLE174_COMPACT_SUMMARY',flush=True)
    print(encoded(dict(event='request174-final-compact-identity',bytes=len(raw),sha256=digest(raw),
        hash_scope='ASCII JSON bytes excluding log separator LF',
        complete_scientific_acceptance_not_inferred_from_report_job=True)).decode(),flush=True)
    return code


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report-only',action='store_true')
    p.add_argument('--request',type=Path)
    p.add_argument('--request-sha256')
    p.add_argument('--repository-directory',type=Path)
    p.add_argument('--original-input-paths',type=Path)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rules-directory',type=Path,required=True)
    p.add_argument('--compute-outcome',default='not-recorded')
    args=p.parse_args()
    if args.report_only:return report(args)
    if any(value is None for value in (args.request,args.request_sha256,args.repository_directory,args.original_input_paths)):
        p.error('All request/repository/original-input arguments are required')
    return run(args)


if __name__=='__main__':
    raise SystemExit(main())

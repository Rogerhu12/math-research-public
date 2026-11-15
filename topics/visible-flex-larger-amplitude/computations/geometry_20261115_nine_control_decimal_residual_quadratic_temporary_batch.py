#!/usr/bin/env python3
"""One temporary persistent-Decimal50 child and complete scalar lifecycle.

No numerical model is imported here. The child remains in the original
rules-runner process group. All actual scalar records are emitted before
request-owned temporary cleanup by the workflow. A report-only recovery may
read an existing partial status but never resumes or manufactures science.
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

ENTRY='geometry_20261115_nine_control_decimal_residual_quadratic_temporary_batch.py'
SCIENCE='geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py'
SCIENCE_SHA='54167dff0ce67e9f8fe0fa5d2899c35f0f99534077f2530d90b296eee7537100'
READER='root_20261115_nine_control_decimal_residual_quadratic_scalar_readout.py'
READER_SHA='a49ebce03156e8ee620ea7cab62e51c32f2a924458ad6d2320e85cf91398897d'
SCIENCE_SCHEMA='R259-nine-control-persistent-decimal50-residual-quadratic-square-trust-v1'
STATUS_NAME='nine-control-decimal50-residual-quadratic-status.json'
REQUEST_SCHEMA='public-nine-control-persistent-decimal50-residual-quadratic-square-request-v1'
SCHEMA='nine-control-persistent-decimal50-residual-quadratic-square-single-batch-v1'
LIMIT=90000
HERE=Path(__file__).resolve().parent


def encode(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=True,allow_nan=False,
                      separators=(',',':')).encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_receipt(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for b in iter(lambda:stream.read(1<<20),b''):
            h.update(b)
    return dict(file=Path(path).name,bytes=Path(path).stat().st_size,sha256=h.hexdigest())


def atomic(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    raw=encode(value)+b'\n';temp=path.with_suffix('.pending')
    temp.write_bytes(raw);os.replace(temp,path)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
        or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Run this wrapper only in the public repository Actions')


def child_environment():
    env=dict(os.environ)
    for name in list(env):
        if (name in ('GITHUB_OUTPUT','GH_TOKEN','GITHUB_TOKEN','MR_TOKEN','MR_READ_TOKEN',
                     'GIT_ASKPASS','SSH_ASKPASS') or name.startswith('GIT_CONFIG_')):
            env.pop(name,None)
    return env


def bind(args):
    raw=args.request.read_bytes()
    if digest(raw)!=args.request_sha256:
        raise ValueError('Bind the entire actual request')
    request=json.loads(raw)
    if (request['schema']!=REQUEST_SCHEMA or request['request_number']!=157
        or request['repository']!='Rogerhu12/math-research-public'
        or request['execution_entry']!=ENTRY or request['scientific_entry']!=SCIENCE):
        raise ValueError('Do not execute another request or producer under this name')
    if request['batch_chain']!={'max_batches':1,'one_atomic_eight_direction_child':True,
            'reset_initial_relative_radius':True,'carry_actual_radius':False,
            'explicit_exploration_radius':'0.01','separate_primary_and_fallback_budgets':True,
            'extra_numeric_acceptance_or_continuation_gate':False}:
        raise ValueError('Keep the explicit single-child contract')
    if request['source_sha256'][SCIENCE]!=SCIENCE_SHA or request['workflow_support_source_sha256'][READER]!=READER_SHA:
        raise ValueError('The current producer or reader pin differs')
    for table in ('source_sha256','workflow_support_source_sha256'):
        for name,wanted in request[table].items():
            if Path(name).name!=name or digest((HERE/name).read_bytes())!=wanted:
                raise ValueError('Pinned source differs: '+name)
    if len(request['source_sha256'])!=107 or len(request['workflow_support_source_sha256'])!=9:
        raise ValueError('Keep all104 previous source pins plus three new sources and all8 previous plus current reader supports')
    if len(request['source_closure']['origin_producer'])!=39 or len(request['source_closure']['current_producer'])!=41:
        raise ValueError('Retain the exact39-to41 producer source closure')
    if not all(request['source_sha256'].get(n)==s for n,s in request['source_closure']['current_producer'].items()):
        raise ValueError('Current consumed source closure differs')
    repo=args.repository_directory.resolve()
    recipe_info=request['parameter_recipe']
    rel=Path(recipe_info['file'])
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Recipe is a relative explicit repository text')
    recipe_path=repo/rel
    raw_recipe=recipe_path.read_bytes()
    if len(raw_recipe)!=recipe_info['bytes'] or digest(raw_recipe)!=recipe_info['sha256']:
        raise ValueError('Keep the complete actual154 persistent-parameter recipe')
    recipe=json.loads(raw_recipe)
    if recipe['origin']!=recipe_info['origin'] or recipe['literal_parameters']!=request['diagnostic']['parameters']:
        raise ValueError('The actual parent parameters/provenance changed')
    if recipe['algorithm_state']!=recipe_info['algorithm_state']:
        raise ValueError('Retain the recorded parent radius separately; exploration is explicitly declared')
    if recipe['exploration_policy']!=request['exploration_policy'] or request['diagnostic']['initial_relative_radius']!='0.01':
        raise ValueError('Do not silently change the new residual-quadratic exploration policy')
    if recipe['input_sha256']!={n:item['sha256'] for n,item in request['inputs'].items()}:
        raise ValueError('The four actual inputs differ')
    inputs=json.loads(args.original_input_paths.read_bytes())
    if set(inputs)!=set(request['inputs']):
        raise ValueError('All four original inputs are required')
    for name,path in inputs.items():
        actual=file_receipt(Path(path));wanted=request['inputs'][name]
        if actual['bytes']!=wanted['bytes'] or actual['sha256']!=wanted['sha256']:
            raise ValueError('Actual restored input bytes differ: '+name)
    runner=Path(os.environ['RUNNER_TEMP']).resolve()
    if args.out.is_symlink():
        raise ValueError('Output must be a request-owned temporary directory')
    args.out.resolve().relative_to(runner)
    return request,recipe_path,inputs


class Processes:
    def __init__(self):
        self.active=None
        self.signal_number=None

    def interrupted(self,signum,frame):
        self.signal_number=signum
        if self.active is not None and self.active.poll() is None:
            try:
                self.active.send_signal(signum)
            except ProcessLookupError:
                pass

    def run(self,argv,out_path,err_path,env):
        # No detached session or hidden numerical timeout. Original rule
        # termination and the explicit Actions wallclock own the process group.
        with out_path.open('wb') as out,err_path.open('wb') as err:
            self.active=subprocess.Popen(argv,cwd=HERE,env=env,shell=False,
                stdout=subprocess.PIPE,stderr=err)
            try:
                while True:
                    block=self.active.stdout.read1(65536)
                    if not block:
                        break
                    out.write(block)
                    sys.stdout.buffer.write(block);sys.stdout.buffer.flush()
                self.active.stdout.close()
                return self.active.wait()
            finally:
                self.active=None


def scientific_argv(inputs,recipe,out,request):
    command=[sys.executable,'-u',str(HERE/SCIENCE)]
    for name in ('accepted','prepared','tail_anchor','tail_config'):
        command+=['--'+name.replace('_','-'),inputs[name]]
    command+=['--parameter-recipe',str(recipe),'--parameter-recipe-sha256',
              request['parameter_recipe']['sha256'],'--out',str(out),
              '--decimal-digits','50','--candidate-steps','8','--backtracks','20',
              '--normal-iterations','12','--normal-backtracks','20',
              '--normal-target-tolerance','1e-8','--candidate-resonance-tolerance','1e-8',
              '--interval-bits','160','--interval-depth','14']
    return command


def collect_status(out,request=None):
    path=out/'science'/STATUS_NAME
    if not path.is_file():
        return None,dict(present=False)
    raw=path.read_bytes();status=json.loads(raw)
    if status.get('schema')!=SCIENCE_SCHEMA or status.get('source_sha256')!=SCIENCE_SHA:
        raise ValueError('Do not relabel a different or old status as current')
    if request is not None and status.get('consumed_source_sha256')!=request['source_closure']['current_producer']:
        raise ValueError('The actual current producer source closure differs')
    return status,dict(present=True,original_status=file_receipt(path),
        schema=status['schema'],source_sha256=status['source_sha256'],
        consumed_source_closure_count=len(status.get('consumed_source_sha256',{})),
        consumed_source_closure_canonical_sha256=digest(encode(status.get('consumed_source_sha256',{}))),
        scientific_completion_not_inferred_from_identity=True)


def original_rules(directory):
    result=[]
    if directory.is_dir():
        paths=sorted(directory.glob('sync-*-completed.json'))
        if (directory/'runner-result.json').is_file():
            paths.append(directory/'runner-result.json')
        for path in paths:
            result.append(dict(receipt=file_receipt(path),original=json.loads(path.read_bytes())))
    return result


def summary(chain,status,status_record,primary=None):
    result=dict(chain)
    result['actual_status']=status_record
    result['complete_planned_direction_rows']=[]
    rows=status.get('searches',[]) if status else []
    for i in range(8):
        row=rows[i] if i<len(rows) else None
        if row is None:
            result['complete_planned_direction_rows'].append(dict(direction=i,started=False,
                reason='not reached by the actual original child'))
            continue
        trials=row.get('trials',[])
        result['complete_planned_direction_rows'].append(dict(direction=i,started=True,
            actual_iteration=row.get('iteration'),accepted=row.get('accepted',False),
            original_merit_before=row.get('merit_before'),original_radius=row.get('relative_radius'),
            actual_outer_trials=len(trials),
            accepted_alpha=next((t.get('alpha') for t in trials if t.get('accepted')),None),
            actual_accepted_merit=next((t.get('actual_merit') for t in trials if t.get('accepted')),None),
            actual_radius_update=row.get('radius_update'),reason=row.get('reason'),
            direction_model_error=row.get('direction_model_error'),
            accepted_path=row.get('accepted_path'),complete_path_status=row.get('path_status'),
            primary_straight_trial_count=sum(t.get('path')=='residual_quadratic_straight' for t in trials),
            fallback_trial_count=sum(t.get('path')=='original149_normal_fallback' for t in trials),
            all_polynomial_points_candidates_shifts_spectral_and_normal_details_in_complete_reader_groups=True,
            polynomial_model_update_count=len(row.get('direction_model',{}).get('model_updates',[])),
            polynomial_model_candidate_count=row.get('direction_model',{}).get('global_model_candidate_count'),
            polynomial_model_points_evaluated=row.get('direction_model',{}).get('complete_finite_model_points_evaluated'),
            selected_polynomial_model_merit=row.get('direction_model',{}).get('selected_model_merit'),
            polynomial_optimizer_completed=row.get('direction_model',{}).get('model_optimizer_completed')))
    if status:
        for key in ('phase','diagnostic_completed','resource_partial','exception',
                    'search_stop_reason','initial_relative_trust_radius','final_relative_trust_radius',
                    'current_persistent_parameters','current_relative_trust_radius',
                    'last_accepted_parameters','original_Armijo_accepted_point_count',
                    'rejected_direction_count','initial_original_three_equation_merit',
                    'final_original_three_equation_merit','high_precision_original_unit_stopping_tolerance_met',
                    'high_precision_full112_linear_right_tolerance_met',
                    'binary64_projection_original_unit_stopping_tolerance_met',
                    'binary64_projection_full112_linear_right_tolerance_met',
                    'original54_FD_checks_and_high_precision54_FD_checks_completed',
                    'initial_and_final_second_axis_checks_completed','explicit_new_exploration_policy',
                    'native_nonlinear_solver_called','nonzero_field_completed','success','seconds'):
            if key in status:
                result[key]=status[key]
        result['final_persistent_parameters']=status.get('final',{}).get('parameters')
        result['high_precision_call_counts']=status.get('high_precision_call_counts')
        result['exact_persistent_restart_components']=status.get('restart_recipe')
    if primary is not None:
        result['complete_primary']=dict(bytes=len(primary),sha256=digest(primary),
            begin='BEGIN_VISIBLE157_PRIMARY',end='END_VISIBLE157_PRIMARY',
            actual_reader_schema=json.loads(primary).get('schema'))
    result['all_completed_or_uncompleted_direction_rows_retained']=True
    result['scientific_native_or_BVP_acceptance_claimed']=False
    return result


def readout(processes,out,rules,compute_outcome):
    primary=out/'primary.json'
    env=child_environment()
    env['GITHUB_OUTPUT']=str(out/'reader-output.txt')
    argv=[sys.executable,'-u',str(HERE/READER),'--directory',str(out/'science'),
          '--rules-directory',str(rules),'--compute-outcome',compute_outcome,
          '--primary-output',str(primary)]
    print('BEGIN_VISIBLE157_ORIGINAL_READER_STDOUT',flush=True)
    code=processes.run(argv,out/'reader-stdout.txt',out/'reader-stderr.txt',env)
    print('END_VISIBLE157_ORIGINAL_READER_STDOUT',flush=True)
    print(encode(dict(event='visible157-original-reader-stdout-identity',
        exit_code=code,stdout=file_receipt(out/'reader-stdout.txt'),
        stderr=file_receipt(out/'reader-stderr.txt'),
        original_segment_bytes_relayed_without_scientific_recomputation=True)).decode(),flush=True)
    return code,primary.read_bytes() if primary.is_file() else None


def run(args):
    require_actions()
    if Path(__file__).name!=ENTRY:
        raise ValueError('Keep the independent wrapper basename')
    request,recipe,inputs=bind(args)
    if args.out.exists() and any(args.out.iterdir()):
        raise ValueError('Use a fresh independent single-batch directory')
    args.out.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    chain=dict(schema=SCHEMA,request_number=157,run_id=os.environ['GITHUB_RUN_ID'],
        source_commit=os.environ['GITHUB_SHA'],request_sha256=args.request_sha256,
        wrapper_source_sha256=digest(Path(__file__).read_bytes()),
        scientific_source_sha256=SCIENCE_SHA,reader_source_sha256=READER_SHA,
        actual154_origin=request['parameter_recipe']['origin'],
        explicit_exploration_policy=request['exploration_policy'],parent_radius_is_not_carried=True,one_batch_planned=True,
        started_batch_count=0,completed_batch_count=0,child_exit_code=None,
        reader_exit_code=None,wrapper_exception=None,partial=True,
        final_point_is_not_an_accepted_nonzero_field=True,raw_payload_retention=False,
        full_scalar_normal_and_projection_records_in_compute_log=True)
    atomic(args.out/'chain-metadata.json',chain)
    processes=Processes();old={}
    for signum in (signal.SIGTERM,signal.SIGINT):
        old[signum]=signal.signal(signum,processes.interrupted)
    exit_code=1
    try:
        chain['started_batch_count']=1
        atomic(args.out/'chain-metadata.json',chain)
        command=scientific_argv(inputs,recipe,args.out/'science',request)
        print(encode(dict(event='visible157-original-child-argv',argv=command,
            original_acceptance_and_final_gates_unchanged=True,
            primary20_plus_separate_fallback20_with_original12x20_declared=True)).decode(),flush=True)
        code=processes.run(command,args.out/'producer-stdout.txt',args.out/'producer-stderr.txt',child_environment())
        chain['child_exit_code']=code
        chain['producer_stdout']=file_receipt(args.out/'producer-stdout.txt')
        chain['producer_stderr']=file_receipt(args.out/'producer-stderr.txt')
        chain['received_signal']=processes.signal_number
        atomic(args.out/'chain-metadata.json',chain)
        reader_code,primary=readout(processes,args.out,args.rules_directory,
            'success' if code==0 else 'failure-or-resource-partial')
        chain['reader_exit_code']=reader_code
        status,record=collect_status(args.out,request)
        complete=bool(code==0 and status and status.get('diagnostic_completed')
                      and status.get('phase')=='diagnostic-completed')
        chain['completed_batch_count']=int(complete)
        chain['partial']=not(complete and reader_code==0)
        if not complete:
            chain['stop_reason']='original_child_not_diagnostic_completed'
        elif reader_code!=0:
            chain['stop_reason']='original_scalar_readout_incomplete'
        elif status.get('high_precision_original_unit_stopping_tolerance_met'):
            chain['stop_reason']='original_unit_stopping_flag_reached_not_native_acceptance'
        elif not status.get('original_Armijo_accepted_point_count'):
            chain['stop_reason']='zero_original_Armijo_acceptances'
        else:
            chain['stop_reason']='explicit_single_original_eight_direction_batch_completed'
        chain.update(seconds=time.monotonic()-started,actual_rule_sync=original_rules(args.rules_directory))
        chain=summary(chain,status,record,primary)
        exit_code=0 if complete and reader_code==0 else (code if code>0 else 70)
    except Exception as error:
        chain.update(wrapper_exception=repr(error),traceback=traceback.format_exc(),
            partial=True,stop_reason='wrapper_exception_scientific_completion_not_inferred')
        raise
    finally:
        chain['seconds_wrapper']=time.monotonic()-started
        atomic(args.out/'chain-metadata.json',chain)
        for signum,handler in old.items():
            signal.signal(signum,handler)
    return exit_code


def report(args):
    require_actions()
    args.out.mkdir(parents=True,exist_ok=True)
    path=args.out/'chain-metadata.json'
    chain=json.loads(path.read_bytes()) if path.is_file() else dict(
        schema=SCHEMA,request_number=157,run_id=os.environ['GITHUB_RUN_ID'],
        source_commit=os.environ['GITHUB_SHA'],wrapper_exception='No completed wrapper metadata',
        partial=True,stop_reason='wrapper_metadata_not_available')
    primary_path=args.out/'primary.json'
    reader_recovered=False
    # A terminated compute step may leave the original partial status. Read it
    # here without invoking the model or representing a new scientific batch.
    if not primary_path.is_file() and (args.out/'science'/STATUS_NAME).is_file():
        code,primary=readout(Processes(),args.out,args.rules_directory,args.compute_outcome)
        chain['recovery_reader_exit_code']=code;reader_recovered=True
    else:
        primary=primary_path.read_bytes() if primary_path.is_file() else None
    try:
        status,record=collect_status(args.out)
        chain=summary(chain,status,record,primary)
    except Exception as error:
        chain.update(report_status_exception=repr(error),complete_scalar_status_not_claimed=True)
    chain.update(actual_rule_sync=original_rules(args.rules_directory),
        actual_science_step_outcome=args.compute_outcome,
        post_step_partial_readout_attempted=reader_recovered,
        report_stage_did_not_run_or_resume_science=True)
    raw=encode(chain)
    if len(raw)>LIMIT:
        original=dict(bytes=len(raw),sha256=digest(raw))
        raw=encode(dict(schema='request157-chain-index-over-budget-v1',
            run_id=os.environ['GITHUB_RUN_ID'],source_commit=os.environ['GITHUB_SHA'],
            complete_index_identity=original,
            complete_chain_index_not_transported=True,
            scientific_failure_not_inferred_from_transport_size=True,
            original_scientific_segments_remain_in_compute_log=True))
    atomic(args.out/'chain-metadata.json',chain)
    token='VISIBLE157_CHAIN_'+uuid.uuid4().hex
    with open(os.environ['GITHUB_OUTPUT'],'a',encoding='utf-8') as stream:
        stream.write('chain_summary<<'+token+'\n'+raw.decode()+'\n'+token+'\n')
        stream.write('chain_summary_bytes='+str(len(raw))+'\nchain_summary_sha256='+digest(raw)+'\n')
    print('BEGIN_VISIBLE157_CHAIN_SUMMARY',flush=True)
    print(raw.decode(),flush=True)
    print('END_VISIBLE157_CHAIN_SUMMARY',flush=True)
    print(encode(dict(event='visible157-chain-summary-sha256',bytes=len(raw),sha256=digest(raw),
        hash_scope='UTF-8 compact JSON string excluding separator LF',
        actual_science_step_outcome=args.compute_outcome)).decode(),flush=True)
    return 0 if len(encode(chain))<=LIMIT else 70


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report-only',action='store_true')
    parser.add_argument('--request',type=Path)
    parser.add_argument('--request-sha256')
    parser.add_argument('--repository-directory',type=Path)
    parser.add_argument('--original-input-paths',type=Path)
    parser.add_argument('--rules-directory',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--compute-outcome',default='not-recorded')
    args=parser.parse_args()
    if args.report_only:
        return report(args)
    if any(x is None for x in (args.request,args.request_sha256,args.repository_directory,args.original_input_paths)):
        parser.error('All actual request/repository/input arguments are required')
    return run(args)


if __name__=='__main__':
    raise SystemExit(main())

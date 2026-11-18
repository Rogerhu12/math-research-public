#!/usr/bin/env python3
"""One unchanged-H DN solve with the owned native whole-evaluate provider.

Preparation requires the complete same-state transport terminal. Execution
uses the existing recorded worker/client, original target, original 2e-9
gate, original Newton/line search, full Jacobian, cutJets and full audit.
Only initialCheckpoint and traceFile paths change in the original config.
No amplitude warmup list, local state edit, remesh refinement or retry occurs.
"""
import argparse
import datetime
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import struct
import sys
import time
import traceback


def ref(p):
    p=Path(p).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def verify(item):
    if ref(item['path'])!=item:raise ValueError('Changed source/input: '+item['path'])


def load(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def save(p,data):
    with Path(p).open('x') as stream:
        json.dump(data,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
    return ref(p)


def number_hash(values):
    return hashlib.sha256(struct.pack('<'+'d'*len(values),*values)).hexdigest()


def prepare(workspace,out):
    w=workspace.resolve();out=out.resolve()
    topic=w/'math-research-public/topics/visible-flex-held-10pct'
    entry_dir=w/'n4_work/native-node-adapter-v1'
    entry_plan=load(entry_dir/'plan.json')
    entry=load(entry_dir/'entry-summary.json');resource=load(entry_dir/'entry-resource.json')
    if entry['status']!='complete' or entry['native_evaluate_count']!=1:
        raise ValueError('A complete original same-state whole-evaluate entry is required')
    if resource.get('status')!='observed_terminal' or resource.get('child_returncode')!=0:
        raise ValueError('A true successful entry observer terminal is required')
    for item in entry_plan['files'].values():verify(item)
    manifest_path=entry_plan['files']['manifest']['path'];manifest=load(manifest_path)
    for item in [*manifest['owned_sources'],*manifest['native_files'].values(),*manifest['runtime_libraries']]:verify(item)
    source=Path(manifest['source_topic']);cp_ref=entry_plan['files']['production_CP']
    prior=load(cp_ref['path']);old=prior['config'];checkpoint=prior['response']['checkpoint']
    if old['solveTolerance']!=2e-9 or old['maxIterations']!=36 or old['auditSteps']!=32:
        raise ValueError('Unexpected original solve/audit options')
    if old['modes']!=20 or old['shootingParts']!=32 or checkpoint['parameters']['projectionFloor']!=.05:
        raise ValueError('Unexpected complete finite problem')
    if prior['request']['height']!=checkpoint['cutHeight']:
        raise ValueError('Original full H identity is ambiguous')
    if out.exists():raise ValueError('A fresh continuation directory is required')
    out.mkdir(parents=True)
    config=dict(old,initialCheckpoint=cp_ref['path'],traceFile=str(out/'worker-trace.jsonl'))
    for key,value in old.items():
        if key not in ('initialCheckpoint','traceFile') and config[key]!=value:
            raise AssertionError('Original model/solve option changed')
    config_ref=save(out/'config.json',config)
    helper=topic/'scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'
    if not helper.exists():
        helper=w/'publication/topics/visible-flex-held-10pct/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'
    if ref(helper)['sha256']!='a52567b2bfaded2fa9271a08f3cd969dc0291261f22cf2847c83234d93462fa5':
        raise ValueError('Original sparse helper changed')
    observer=ref(topic/'scripts/resume_n4/observe_command_live.py')
    plan_path=out/'plan.json'
    command=[sys.executable,str(Path(__file__).resolve()),'run','--plan',str(plan_path)]
    plan=dict(schema='n4-native-original-DN-continuation-v1',scope=__doc__,
        prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),preparation_command=sys.argv,
        files=dict(source=ref(__file__),manifest=ref(manifest_path),entry_plan=ref(entry_dir/'plan.json'),
            entry_summary=ref(entry_dir/'entry-summary.json'),entry_resource=ref(entry_dir/'entry-resource.json'),
            input_checkpoint=cp_ref,config=config_ref,client=ref(source/'scripts/950f-tail-client-v3.py'),
            worker=ref(source/'scripts/950f-tail-stage-port-v3.mjs'),sparse_helper=ref(helper),
            observer=observer,python=ref(sys.executable)),
        source_topic=str(source),record_prefix=str(out/'tail'),native_run_directory=str(out/'native-evaluates'),
        summary=str(out/'summary.json'),ready=str(out/'worker-ready.json'),
        command=command,observer_command=[sys.executable,observer['path'],'--log',str(out/'process.log'),
            '--out',str(out/'resource.json'),'--',*command],
        request=dict(height=checkpoint['cutHeight'],jacobian=True,audit=True),
        height_sha256=number_hash(checkpoint['cutHeight']),
        full_original_state_sha256=number_hash([v for row in checkpoint['states'] for v in row]),
        configuration_changed_keys=['initialCheckpoint','traceFile'],
        numerical_options={key:config[key] for key in ['modes','spacing','quadrature','depth','shootingParts',
            'steps','linearFar','linearSteps','solveTolerance','maxIterations','auditSteps','cuspAwareFlow']},
        production_projectionFloor=.05,node_heap=1536,prescribed_requests=1,
        initializer='Existing worker reads the complete same-M/same-depth/same-parts CP. Original remesh copies existing nodes; identical H gives ratio1 and zero Dirichlet correction. No mode/part/depth or physical change.',
        acceptance='Original worker dn.solve with original2e-9, fullJac, cutJets, original audit32, heightJetJacobian. No new acceptance threshold or manual state modification.',
        finite_scope='This is an actual finite tail at the same recorded .5H target. It does not complete fullH, prefix coupling, exact arcs, closure or continuous certification.')
    result=save(plan_path,plan)
    print(json.dumps(dict(plan=result,command=plan['observer_command'],requests=1,height_sha256=plan['height_sha256'])),flush=True)


def run(plan_path):
    plan_path=plan_path.resolve();plan=load(plan_path)
    if plan['schema']!='n4-native-original-DN-continuation-v1' or plan['prescribed_requests']!=1:
        raise ValueError('Unexpected continuation plan')
    for item in plan['files'].values():verify(item)
    if ref(__file__)!=plan['files']['source']:raise ValueError('Continuation source changed')
    if Path(plan['summary']).exists() or Path(plan['native_run_directory']).exists():
        raise ValueError('Continuation outputs already exist')
    manifest=load(plan['files']['manifest']['path'])
    for item in [*manifest['owned_sources'],*manifest['native_files'].values(),*manifest['runtime_libraries']]:verify(item)
    os.environ['VISIBLE_FLEX_NATIVE_MANIFEST']=plan['files']['manifest']['path']
    os.environ['VISIBLE_FLEX_NATIVE_MANIFEST_SHA256']=plan['files']['manifest']['sha256']
    os.environ['VISIBLE_FLEX_NATIVE_RUN_DIR']=plan['native_run_directory']
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER']=plan['files']['sparse_helper']['path']
    os.environ['VISIBLE_FLEX_SPARSE_PYTHON']=sys.executable
    source=Path(plan['source_topic']);spec=importlib.util.spec_from_file_location('native_existing_tail_client',plan['files']['client']['path'])
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    summary=dict(scope=__doc__,plan=ref(plan_path),source=ref(__file__),files=plan['files'],
        request_height_sha256=plan['height_sha256'],original_state_sha256=plan['full_original_state_sha256'],
        production_changed=False,physical_parameters_changed=False,original_gate=2e-9,
        requested_calls=1,fullJac_requested=True,full_audit_requested=True)
    start=time.perf_counter();port=None;response=None;failed=None
    try:
        port=module.WeightedTailPort(plan['files']['config']['path'],source/'repro/source-root',
            Path(plan['record_prefix']),node_heap=plan['node_heap'])
        summary['ready']=save(plan['ready'],port.ready)
        print(json.dumps(dict(event='native_original_worker_ready',ready=summary['ready'])),flush=True)
        response=port.solve(plan['request']['height'],jacobian=True,audit=True)
        if not response.get('converged') or not response['residual']<2e-9:
            raise AssertionError('Original finite DN did not meet its strict gate')
        if response.get('heightJetJacobian') is None or response.get('audit') is None:
            raise AssertionError('Original requested Jacobian/audit did not return')
        if response['checkpoint']['cutHeight']!=plan['request']['height']:
            raise AssertionError('Original target H changed')
        summary.update(status='complete',converged=True,residual=response['residual'],
            audit=response['audit'],last_iteration=response['history'][-1],
            iterations=len(response['history']),heightJetJacobian_entries=len(response['heightJetJacobian']),
            original_DN_Jac_audit_completed=True,fullH_or_prefix_coupling_completed=False)
    except Exception as error:
        failed=error
        summary.update(status='failure',error=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc()),
            original_DN_Jac_audit_completed=False)
    finally:
        if port is not None:
            try:port.close()
            except Exception as error:
                summary['close_error']=dict(type=type(error).__name__,message=str(error))
                if failed is None:failed=error;summary['status']='engineering_close_failure'
    prefix=Path(plan['record_prefix'])
    record_path=prefix.with_name(prefix.name+'_0001.json.gz')
    if record_path.exists():
        summary['record']=ref(record_path)
        saved=load(record_path)
        summary['saved_response_failure']=saved['response'].get('failed')
        summary['saved_response_converged']=saved['response'].get('converged')
        summary['saved_response_residual']=saved['response'].get('residual')
        summary['saved_last_iteration']=saved['response'].get('lastIteration')
        if saved['request']!=plan['request']:raise AssertionError('Actual request differs from frozen plan')
    for name,suffix in [('worker_stderr','_worker_stderr.log'),('worker_exit','_worker_exit.json')]:
        p=prefix.with_name(prefix.name+suffix)
        if p.exists():summary[name]=ref(p)
    trace=Path(load(plan['files']['config']['path'])['traceFile'])
    if trace.exists():summary['worker_trace']=ref(trace)
    events=Path(plan['native_run_directory'])/'events.jsonl'
    if events.exists():
        summary['native_events']=ref(events)
        rows=[json.loads(line) for line in events.read_text().splitlines()]
        terminal=[row for row in rows if row['event']=='batch_terminal']
        summary['native_evaluate_terminal_count']=len(terminal)
        summary['native_engineering_failures']=sum(row['status']=='engineering_failure' for row in terminal)
        if summary['native_engineering_failures']:
            summary['engineering_failure_scope']='An original line-search failure after any such event is not classified here as a mathematical obstruction.'
    summary['seconds']=time.perf_counter()-start
    output=save(plan['summary'],summary)
    print(json.dumps(dict(event='native_original_DN_terminal',status=summary['status'],summary=output,
        residual=summary.get('residual'),error=summary.get('error',{}).get('message'))),flush=True)
    return 1 if failed else 0


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='action',required=True)
    p=sub.add_parser('prepare');p.add_argument('--workspace',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True)
    p=sub.add_parser('run');p.add_argument('--plan',type=Path,required=True)
    a=parser.parse_args()
    if a.action=='prepare':prepare(a.workspace,a.out_dir);return 0
    return run(a.plan)


if __name__=='__main__':raise SystemExit(main())

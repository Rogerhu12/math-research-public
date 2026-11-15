#!/usr/bin/env python3
"""Use actual61 final raw states to test a new no-J-matched variational flow.

Every requested stage runs its original complete no-J flow and one new
complete with-J flow. The input/profile/config remain fixed. Full226-state
bit comparisons are diagnostics; no convergence or error gate is added.
Only public Actions may execute the original root/RHS/new Jacobians.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import time
import traceback

HERE = Path(__file__).resolve().parent
HELPER = 'geometry_20261114_current576_same_state_noj_probe.py'
HELPER_SHA = 'fc2c61d35e6eb3b1e8d836f46b75c7dc5ec2f2f69bcd483410a289434637099b'
MODULE = 'geometry_20261114_noj_matched_variational_engine.mjs'
MODULE_SHA = 'f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9'
HOOK = 'geometry_20261114_noj_matched_variational_probe_hook.mjs'
ENVIRONMENT = 'VISIBLE_FLEX_NOJ_MATCHED_PRIMAL_PROBE_SPEC'
DEPENDENCIES = {
    'product_jacobian': '205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25',
    'local_cusp_grid': 'b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f',
}


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY','').lower() != 'rogerhu12/math-research-public'):
        raise RuntimeError('Execute the original numerical flows only in the public repository Actions')
    import hashlib
    if hashlib.sha256((HERE/HELPER).read_bytes()).hexdigest() != HELPER_SHA:
        raise ValueError('Retain the frozen actual61 input-binding helper')
    if hashlib.sha256((HERE/MODULE).read_bytes()).hexdigest() != MODULE_SHA:
        raise ValueError('Bind this new variational implementation explicitly')
    import geometry_20261114_current576_same_state_noj_probe as evidence
    for name, digest in evidence.SOURCE_PINS.items():
        if evidence.sha(HERE/name) != digest:
            raise ValueError('Retain the unchanged original source: '+name)
    from exact_20261114_seeded_zero_tail_client import (
        same, numerical_configuration, numerical_sources, ready_semantics, IO_KEYS)
    import exact_20261114_true_tail_client as original

    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('native-directory','snapshot-directory','source-topic','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--native-result-sha256',required=True)
    parser.add_argument('--snapshot-result-sha256',required=True)
    parser.add_argument('--stage',type=int,action='append',required=True)
    parser.add_argument('--node-heap',type=int,default=6144)
    args=parser.parse_args()
    if (len(set(args.stage))!=len(args.stage)
            or not all(0<=n<576 for n in args.stage)):
        raise ValueError('Declare distinct actual stage indices in [0,575]')
    output=args.out.resolve()
    if output.is_relative_to(args.native_directory.resolve()) or output.is_relative_to(args.snapshot_directory.resolve()):
        raise ValueError('Write the new candidate evidence outside original immutable input directories')
    output.mkdir(parents=True,exist_ok=True)
    if any(output.iterdir()):
        raise ValueError('Use an empty new output directory')

    def equal(a,b,label):
        if not same(a,b):
            raise ValueError('Matched-primal source identity differs: '+label)

    bound=evidence.bind_inputs(args,equal,numerical_configuration,numerical_sources)
    config_path=output/'probe-input-config.json'
    evidence.write(config_path,bound['config'])
    hook=HERE/HOOK
    spec=dict(schema='actual61-noJ-matched-variational-probe-spec-v1',
        source_sha256=evidence.sha(__file__),hook_sha256=evidence.sha(hook),
        input_binding_helper=dict(file=HELPER,sha256=HELPER_SHA),
        candidate_module=dict(file=MODULE,bytes=(HERE/MODULE).stat().st_size,sha256=MODULE_SHA),
        original_dependencies=DEPENDENCIES,frozen_sources=evidence.SOURCE_PINS,
        original_public_run='43645948199',original_native_result_sha256=evidence.NATIVE_RESULT_SHA,
        original_snapshot_result_sha256=evidence.SNAPSHOT_SHA,current_state_sha256=evidence.STATE_SHA,
        original_evaluate_source_sha256=evidence.EVALUATE_SHA,original_core_file_sha256=evidence.CORE_SHA,
        numerical_configuration=bound['config'],numerical_parameters=bound['live']['parameters'],
        original_source_sha256=bound['context']['original_sources'],original_live_identity=bound['live'],
        io_keys=sorted(IO_KEYS),output=str(output),inputs=bound['native_inputs'],
        snapshot_inputs=bound['snapshot_inputs'],original_arrays=bound['arrays'],
        original_J_descriptor_only=bound['original_J_descriptor_only'],saved_withJ_norm=bound['context']['current_original_norm'],
        stages=args.stage,original_native_solve_requested=False,
        source_scope='New with-J state implementation; original no-J functions and original equations remain unchanged',
        full_evaluate_or_Newton_loop_requested=False,no_scientific_acceptance_threshold_added=True)
    spec_path=output/'matched-primal-spec.json.gz'
    spec_receipt=evidence.write(spec_path,spec,compressed=True)
    previous_env=os.environ.get(ENVIRONMENT)
    popen=original.subprocess.Popen
    commands=[]
    client=None
    started=time.monotonic()
    result=dict(schema='actual61-noJ-matched-variational-probe-launcher-v1',
        source_sha256=evidence.sha(__file__),hook_sha256=evidence.sha(hook),candidate_module=spec['candidate_module'],
        specification=spec_receipt,input_native_result=bound['native_result'],input_snapshot_result=bound['snapshot_result'],
        original_state_sha256=evidence.STATE_SHA,selected_stages=args.stage,
        no_TailClient_solve_called=True,old_saved_J_payloads_read=False,
        native_accepted=False,task_completed=False)

    def observed_popen(command,*positional,**keywords):
        worker=str(HERE/'tail_frozen_worker.mjs')
        if not isinstance(command,list) or worker not in command:
            return popen(command,*positional,**keywords)
        if len(command)!=8 or command[0]!='node' or command[4]!='--import' or command[6]!=worker:
            raise ValueError('Only the actual original worker launch gets the diagnostic request loop')
        actual=list(command[:6])+['--import',str(hook)]+list(command[6:])
        commands.append(actual)
        return popen(actual,*positional,**keywords)

    code=2
    try:
        os.environ[ENVIRONMENT]=str(spec_path)
        original.subprocess.Popen=observed_popen
        try:
            client=original.TailClient(config_path,args.source_topic.resolve()/'repro/source-root',
                output/'original-constructor',node_heap=args.node_heap)
        finally:
            original.subprocess.Popen=popen
        equal(numerical_configuration(client._configuration),bound['config'],'original settings')
        equal(numerical_sources(client.sources),bound['context']['original_sources'],'all original source bytes')
        equal(ready_semantics(client.ready),ready_semantics(bound['ready']),'original ready semantics')
        capacity=original.read(client.capacity_record)
        for key in ('name','capacity','requestedCapacity','nodeVersion','adapterSHA256',
                    'originalConstructorCapacity','numericalChange','retained','files'):
            equal(capacity[key],bound['capacity'][key],'original capacity '+key)
        if len(commands)!=1 or client.calls!=0 or client.cache_key is not None:
            raise ValueError('One fresh original constructor with no imported response cache required')
        launch=dict(schema='actual61-noJ-matched-variational-verified-launch-v1',
            source_sha256=evidence.sha(__file__),hook_sha256=evidence.sha(hook),spec_sha256=evidence.sha(spec_path),
            current_sources=client.sources,actual_command=commands[0],identity_verified_before_evaluation=True,
            complete_current_ready=evidence.receipt(output/'original-constructor_ready.json.gz'),
            complete_current_capacity=evidence.receipt(client.capacity_record),original_native_solve_calls=0)
        evidence.write(output/'verified-launch-intent.json',launch)
        result['verified_launch']=evidence.receipt(output/'verified-launch-intent.json')
        client.proc.stdin.write(json.dumps(dict(matched_primal=evidence.sha(spec_path)))+'\n')
        client.proc.stdin.flush()
        with (output/'diagnostic-stdout.jsonl').open('x') as stream:
            for line in client.proc.stdout:
                stream.write(line);stream.flush();print(line.rstrip(),flush=True)
        result['worker_exit_code']=client.proc.wait()
        if result['worker_exit_code']!=0:
            raise RuntimeError('Selected-stage diagnostic failed; retain actual stderr and partial evidence')
        summary=evidence.read(output/'summary.json')
        equal(summary['schema'],'actual61-noJ-matched-variational-selected-stage-probe-v1','actual summary schema')
        equal(summary['stages'],args.stage,'same requested stage sequence')
        equal(summary['probe_completed'],True,'all diagnostic cases observed')
        result.update(probe_completed=True,summary=evidence.receipt(output/'summary.json'),
            every_requested_case_returned=summary['every_requested_case_returned'],
            all_completed_primal_states_bitwise_equal=summary['all_completed_primal_states_bitwise_equal'])
        code=0 if summary['every_requested_case_returned'] else 2
    except Exception as error:
        result.update(probe_completed=False,actual_error=repr(error),traceback=traceback.format_exc())
        raise
    finally:
        original.subprocess.Popen=popen
        if client is not None:
            client.close();result['original_native_solve_calls']=client.calls
            result['worker_exit_code']=client.proc.poll()
        if previous_env is None:os.environ.pop(ENVIRONMENT,None)
        else:os.environ[ENVIRONMENT]=previous_env
        result['elapsed_seconds']=time.monotonic()-started
        evidence.write(output/'launcher-result.json',result)
    return code


if __name__=='__main__':
    raise SystemExit(main())

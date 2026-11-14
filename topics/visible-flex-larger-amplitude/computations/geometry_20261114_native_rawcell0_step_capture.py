#!/usr/bin/env python3
"""Capture every original RK step of all72 original rawCell0 stages.

Bind actual17/19/21/22/23/28 and the unchanged native constructor/source chain.
Keep the complete original226-state path and actual cusp integrationGrid.
Only the tangent origin restarts at each step; blocks stream to large-arrays.
Stop before native solve, whole-tail J, trial, endpoint J or final audit.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
SEED_NAME='geometry_20261114_native_candidate_seeded_solve.py'
SEED_SHA='afa2588db686ba54b3e434e0ddf40503a74061ecd5fa389dbb41ced7a0b085c7'
READER_NAME='geometry_20261114_native_band_trial_replay.py'
READER_SHA='e357426aa6e81cbab526ea74f7f9fd3e1fd69d917000dd7f9847972745823b80'
CAPTURE_READER_NAME='geometry_20261114_native_captured_band_correction.py'
CAPTURE_READER_SHA='b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
WINDOW_NAME='geometry_20261114_native_rawcell0_step_windows.mjs'
WINDOW_SHA='07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b'
CAPTURE_SHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
VARIABLE='VISIBLE_FLEX_NATIVE_RAWCELL0_STEP_CAPTURE_SPEC'
STOP='VISIBLE_NATIVE_RAWCELL0_STEP_CAPTURE_COMPLETE_V1'
SELECTED=tuple(range(72))


def load(name,digest,key):
    source=HERE/name
    if hashlib.sha256(source.read_bytes()).hexdigest()!=digest:raise ValueError('Frozen source changed: '+name)
    spec=importlib.util.spec_from_file_location(key,source)
    module=importlib.util.module_from_spec(spec);sys.modules[key]=module;spec.loader.exec_module(module)
    return module


def reference_packets(capture_directory,out,B):
    C=load(CAPTURE_READER_NAME,CAPTURE_READER_SHA,'_native_split_original_capture')
    capture=C.CapturedArrays(capture_directory,CAPTURE_SHA)
    states=capture.all('base-states');outputs=capture.all('stage-out');guards=capture.all('stage-guard-mean')
    records={str(n):dict(stage=n,original_live_stage=capture.live['stages'][n]) for n in SELECTED}
    def save(n,kind,values):
        raw=C.float_bytes(values);name=f'reference-stage-{n:03d}-{kind}.f64le';p=out/name
        with p.open('xb') as stream:stream.write(raw)
        descriptor=dict(file=name,path=str(p),bytes=len(raw),sha256=B.sha(p),
            dtype='<f8',order='C',shape=list(values.shape),
            origin='Selected exact original actual28 array bytes; no new numerical evaluation')
        records[str(n)][kind]=descriptor
    for n in SELECTED:
        save(n,'input',states[n+1]);save(n,'output',outputs[n]);save(n,'guard-mean',guards[n])
    return dict(capture_binding=capture.binding,selected_stages=records,
        selected_original_stages=72,complete_original_arrays_verified=True,
        original_full_J_sha256=capture.binding['raw_array_sha256']['stage-jacobians'],
        new_J_computed_during_packet_extraction=False)


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('Native original-step capture science belongs only to public repository Actions')
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('failed-directory','cold-probe-summary','first-candidate-summary','v2-candidate-summary',
                 'candidate-directory','capture-directory','source-topic','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--node-heap',type=int,default=6144)
    a=parser.parse_args();a.out=a.out.resolve()
    if a.out.exists() or a.out.is_relative_to(a.capture_directory.resolve()):
        raise ValueError('Use a new independent original-step capture output directory')
    a.out.mkdir(parents=True)
    T=load(READER_NAME,READER_SHA,'_native_split_capture_metadata');B=T.load_base();history=B.load_frozen_history()
    frozen=dict(history.PINNED_SOURCES,**{B.HISTORY_SOURCE:B.HISTORY_SHA,
        'geometry_20261114_zero_rk_native_probe_v3_hook.mjs':B.V3_HOOK_SHA,
        SEED_NAME:SEED_SHA,READER_NAME:READER_SHA,CAPTURE_READER_NAME:CAPTURE_READER_SHA,WINDOW_NAME:WINDOW_SHA,
        'tail_resumable_engine.mjs':'1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8'})
    for name,digest in frozen.items():
        if B.sha(HERE/name)!=digest:raise ValueError('Frozen original/provenance source changed: '+name)
    from exact_20261114_seeded_zero_tail_client import same,numerical_configuration,numerical_sources,ready_semantics,IO_KEYS
    import exact_20261114_true_tail_client as original
    def equal(left,right,label):
        if not same(left,right):raise ValueError('Original-step capture identity differs: '+label)
    prior=B.validate_history(a,history,equal,numerical_configuration)
    candidate=B.validate_candidate(a,prior,equal,numerical_configuration,numerical_sources)
    capture=T.validate_capture(a,B,prior,candidate,equal,numerical_sources)
    references=reference_packets(a.capture_directory.resolve(),a.out,B)
    B.write(a.out/'original-reference-packets.json',references)
    config_path=a.out/'rawcell0-step-input-config.json';original.write(config_path,prior['config'])
    hook=HERE/'geometry_20261114_native_rawcell0_step_capture_hook.mjs'
    request=dict(height=prior['height'],jacobian=True,audit=True)
    spec=dict(schema='original-native-rawcell0-step-capture-spec-v1',source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        window_module_sha256=WINDOW_SHA,frozen_sources=frozen,inputs=prior['inputs'],capture=capture,references=references,
        original_public_run='43598917532',cold_baseline_public_run='43602823170',first_candidate_public_run='43603818345',
        v2_candidate_public_run='43604874829',completed_probe_public_run='43605912092',captured_reference_public_run='43611175099',
        candidate_state_chunks=candidate['state_chunks'],original_graph_scale_chunks=candidate['graph_chunks'],
        candidate_states_float64le_sha256=B.CANDIDATE_BITS_SHA,exact_height_float64le_sha256=B.HEIGHT_BITS_SHA,
        original_scales_float64le_sha256=B.SCALES_BITS_SHA,original_far_graph_float64le_sha256=B.FAR_BITS_SHA,
        restored_negative_zero_count=candidate['restored_negative_zeros'],
        original_source_sha256=prior['intent']['source_sha256'],numerical_configuration=prior['config'],
        numerical_parameters=candidate['summary']['numerical_parameters'],io_keys=sorted(IO_KEYS),
        output=str(a.out),fresh_request=request,planned_probe_stop=STOP,selected_stages=list(SELECTED),
        original_steps=12,expected_original_stages=72,actual_step_count_from_original_profile_schedule=True,
        additional_ODE_steps=0,new_original_long_J_evaluations=0,new_whole_tail_J_evaluations=0,no_J_evaluations=0,
        original_native_solve_called=False,endpoint_J_or_audit_computed=False,
        original_H_far_graphs_gains_sigma_and_tolerances_unchanged=True,task_completed=False)
    spec_path=a.out/'rawcell0-step-spec.json';B.write(spec_path,spec)
    previous=os.environ.get(VARIABLE);os.environ[VARIABLE]=str(spec_path)
    popen=original.subprocess.Popen;commands=[];client=None;started=time.monotonic()
    result=dict(schema='original-native-rawcell0-step-capture-result-v1',capture_completed=False,
        native_accepted=False,task_completed=False,source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        window_module_sha256=WINDOW_SHA,spec_sha256=B.sha(spec_path),capture_result_sha256=CAPTURE_SHA,
        original_native_solve_called=False,new_whole_tail_J_evaluations=0,
        new_original_long_J_evaluations=0,no_J_evaluations=0,additional_ODE_steps=0,
        endpoint_J_or_audit_computed=False)
    def observed_popen(command,*args,**kwargs):
        worker=str(HERE/'tail_frozen_worker.mjs')
        if not isinstance(command,list) or worker not in command:return popen(command,*args,**kwargs)
        if len(command)!=8 or command[0]!='node' or command[4]!='--import' or command[6]!=worker:
            raise ValueError('Instrument only the original native worker launch')
        actual=list(command[:6])+['--import',str(hook)]+list(command[6:]);commands.append(actual)
        return popen(actual,*args,**kwargs)
    try:
        original.subprocess.Popen=observed_popen
        try:client=original.TailClient(config_path,a.source_topic.resolve()/'repro/source-root',a.out/'native',node_heap=a.node_heap)
        finally:original.subprocess.Popen=popen
        equal(numerical_configuration(client._configuration),prior['config'],'current original mathematical config')
        equal(numerical_sources(client.sources),numerical_sources(prior['intent']['source_sha256']),'current original sources')
        equal(ready_semantics(client.ready),ready_semantics(prior['ready']),'current original ready')
        capacity=original.read(client.capacity_record)
        for key in ('name','capacity','requestedCapacity','nodeVersion','adapterSHA256','originalConstructorCapacity','numericalChange','retained','files'):
            equal(capacity[key],prior['capacity'][key],'current original capacity '+key)
        if len(commands)!=1 or client.calls!=0 or client.cache_key is not None:
            raise ValueError('Use one fresh worker with no completed-response cache')
        B.write(a.out/'verified-launch-intent.json',dict(schema='original-native-rawcell0-step-capture-verified-launch-v1',
            spec_sha256=B.sha(spec_path),hook_sha256=B.sha(hook),source_sha256=B.sha(__file__),actual_command=commands[0],
            current_sources=client.sources,current_capacity_sha256=B.sha(client.capacity_record),
            complete_current_ready_sha256=B.sha(a.out/'native_ready.json.gz'),
            identity_verified_before_request=True,initial_native_solve_calls=0,initial_response_cache_empty=True,
            inputs=prior['inputs'],capture_inputs=capture['inputs'],references=references,request=request))
        print(json.dumps(dict(event='original-native-rawcell0-step-identities-verified',
            selected_stages=list(SELECTED),actual_per_step_count_not_presupposed=True,no_J_evaluations=0,no_whole_tail_J=True)),flush=True)
        try:
            client.solve(prior['height'],jacobian=True,audit=True)
            result['unexpected_complete_native_response_returned']=True
        except FloatingPointError as error:
            result['original_client_exception']=repr(error)
            path=a.out/'native_0001.json.gz'
            if path.is_file():result['actual_original_failure_message']=original.read(path)['response'].get('failed')
            else:raise
    except Exception as error:result['unexpected_error']=repr(error)
    finally:
        original.subprocess.Popen=popen
        if client is not None:
            client.close();result['original_protocol_requests']=client.calls
            result['worker_exit_code']=client.proc.poll() if client.proc else None
        if previous is None:os.environ.pop(VARIABLE,None)
        else:os.environ[VARIABLE]=previous
        summary_path=a.out/'rawcell0-step-summary.json'
        if summary_path.is_file():
            summary=B.read(summary_path);result['capture_summary_sha256']=B.sha(summary_path)
            for key in ('completed_local_J_blocks','completed_original_RK_field_calls','completed_original_stages',
                        'completed_local_J_evaluations','original_RK_field_entries',
                        'total_step_count','stage_reports','array_manifest','prospective_layout','actual_failure'):
                result[key]=summary.get(key)
            result['planned_probe_stop_observed']=result.get('actual_original_failure_message')=='Error: '+STOP
            count=summary.get('total_step_count')
            result['capture_completed']=bool(summary.get('capture_completed') is True and
                type(count) is int and count>0 and summary.get('completed_local_J_blocks')==count and
                summary.get('completed_local_J_evaluations')==count and
                summary.get('completed_original_RK_field_calls')==4*count and
                summary.get('original_RK_field_entries')==4*count and
                summary.get('completed_original_stages')==list(SELECTED) and result['planned_probe_stop_observed'] and
                result.get('worker_exit_code')==0 and result.get('original_protocol_requests')==1 and
                not result.get('unexpected_error') and not result.get('unexpected_complete_native_response_returned'))
        result['elapsed_seconds']=time.monotonic()-started
        result['small_output_files']=[dict(file=p.name,bytes=p.stat().st_size,sha256=B.sha(p))
            for p in sorted(a.out.iterdir()) if p.is_file() and p.name!='result.json']
        B.write(a.out/'result.json',result)
    print(json.dumps(dict(event='original_native_rawcell0_step_capture_finished',capture_completed=result['capture_completed'],
        native_accepted=False,task_completed=False)),flush=True)
    return 0 if result['capture_completed'] else 2


if __name__=='__main__':raise SystemExit(main())

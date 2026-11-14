#!/usr/bin/env python3
"""Capture the four actual local Jacobians of old stage43, original flow step11.

Only one already defined original RK step is replayed from its full226 saved
input. No previous step, whole-tail J, native solve, trial or audit is run.
The complete state/mean/tangent arithmetic is the frozen original body.
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
WINDOW_NAME='geometry_20261114_native_stage43_local_j_window.mjs'
WINDOW_SHA='966ddc4946cc63f69260dd1871c2ac31ad0383eb5593f6c3a0b45b0cfcdef5ec'
CAPTURE_SHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
VARIABLE='VISIBLE_FLEX_NATIVE_STAGE43_LOCAL_J_PROBE_SPEC'
STOP='VISIBLE_NATIVE_STAGE43_LOCAL_J_PROBE_COMPLETE_V1'
SELECTED=(43,)


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
        selected_original_stages=1,complete_original_arrays_verified=True,
        original_full_J_sha256=capture.binding['raw_array_sha256']['stage-jacobians'],
        new_J_computed_during_packet_extraction=False)

STEP_RESULT_SHA='6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf'
FIELD_RECEIPT_SHA='d7d00de365b2118e1346e8f8630d5bad408957da91fdf51f38496f73b0e0c5f2'
PARENT_WINDOW_NAME='geometry_20261114_native_rawcell0_step_windows.mjs'
PARENT_WINDOW_SHA='07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b'


def selected_step_references(a,B):
    directory=a.step_directory.resolve()
    receipt_path=a.field_receipt.resolve()
    if B.sha(receipt_path)!=FIELD_RECEIPT_SHA or receipt_path.stat().st_size!=26214:
        raise ValueError('Use the actual44 complete four-field original receipt')
    receipt=B.read(receipt_path)
    if receipt['schema']!='pinned-actual41-stage43-step11-original-field-receipt-v1':
        raise ValueError('Wrong actual44 copied-field schema')
    def pinned(row):
        relative=Path(row['file'])
        path=(directory/relative).resolve()
        if relative.is_absolute() or '..' in relative.parts or not path.is_relative_to(directory):
            raise ValueError('Bound actual41 input path must remain in its immutable extraction')
        if not path.is_file() or path.stat().st_size!=row['bytes'] or B.sha(path)!=row['sha256']:
            raise ValueError('Changed actual41 input: '+row['file'])
        return path
    result_path=pinned(receipt['inputs']['result'])
    if B.sha(result_path)!=STEP_RESULT_SHA:
        raise ValueError('Wrong original completed per-step capture')
    result=B.read(result_path)
    report_path=pinned(receipt['inputs']['completed_report'])
    window_path=pinned(receipt['inputs']['window'])
    report=B.read(report_path);window=B.read(window_path)
    field_packet=pinned(receipt['inputs']['complete_field_packet'])
    import gzip
    raw=gzip.decompress(field_packet.read_bytes())
    packet_descriptor=receipt['inputs']['complete_field_packet']
    if len(raw)!=packet_descriptor['raw_bytes'] or hashlib.sha256(raw).hexdigest()!=packet_descriptor['raw_sha256']:
        raise ValueError('Changed original complete48-field packet')
    packet=json.loads(raw)
    fields=[row for row in packet['fields'] if row['global_step']==11]
    if fields!=receipt['complete_original_fields'] or len(fields)!=4:
        raise ValueError('The actual44 four fields must equal the original packet records')
    if (report['stage'],report['step_count'],report['rawCell'],report['rawSegment'],report['part'])!=(43,12,0,3,4):
        raise ValueError('Fixed selected original stage identity differs')
    if window!=receipt['window_identity'] or report['schedule'][11]!=receipt['original_step_schedule']:
        raise ValueError('Actual44 original window or step schedule changed')
    manifest_path=pinned(result['array_manifest'])
    manifest=B.read(manifest_path)
    if manifest['schema']!='original-native-rawcell0-step-arrays-v1' or manifest['completed'] is not True:
        raise ValueError('Complete actual41 raw-array manifest required')
    entries={row['name']:row for row in manifest['arrays']}
    if len(entries)!=len(manifest['arrays']):
        raise ValueError('Unique actual41 array names required')
    large=a.out/'large-arrays';large.mkdir()
    references={};verified=[]
    def retain(array_name,shape,selections):
        record=entries[array_name]
        if (record['shape']!=shape or record['dtype']!='<f8' or record['order']!='C' or
                record['completed'] is not True):
            raise ValueError('Use complete selected actual41 array '+array_name)
        width=8
        for size in shape[1:]:width*=size
        accumulated=hashlib.sha256();cursor=0;count_bytes=0;chosen={}
        for index,chunk in enumerate(record['chunks']):
            if (chunk['array']!=array_name or chunk['chunk_index']!=index or
                    chunk['row_start']!=cursor or chunk['row_stop']<=cursor):
                raise ValueError('Complete ordered actual41 row chunks required')
            descriptor=dict(file=chunk['file'],bytes=chunk['bytes'],sha256=chunk['raw_sha256'])
            path=pinned(descriptor);payload=path.read_bytes()
            if len(payload)!=(chunk['row_stop']-cursor)*width:
                raise ValueError('Wrong original complete row bytes')
            accumulated.update(payload);count_bytes+=len(payload)
            for row_index,label in selections:
                if cursor<=row_index<chunk['row_stop']:
                    if label in chosen:raise ValueError('Duplicate selected original row')
                    offset=(row_index-cursor)*width
                    chosen[label]=payload[offset:offset+width]
            cursor=chunk['row_stop']
        if (cursor!=shape[0] or count_bytes!=record['total_bytes'] or
                accumulated.hexdigest()!=record['raw_sha256']):
            raise ValueError('Complete selected actual41 array byte identity failed')
        for row_index,label in selections:
            payload=chosen[label];name='reference-'+label+'.f64le';path=large/name
            with path.open('xb') as stream:stream.write(payload)
            references[label]=dict(name='reference-'+label,file='large-arrays/'+name,path=str(path),bytes=len(payload),
                role='Bound original actual41 array bytes',
                sha256=hashlib.sha256(payload).hexdigest(),dtype='<f8',order='C',shape=shape[1:],
                original_array=array_name,original_row=row_index,
                origin='Exact saved actual41 bytes; no numerical recomputation')
        verified.append(dict(name=array_name,shape=shape,total_bytes=count_bytes,
                             raw_sha256=record['raw_sha256'],chunks_verified=len(record['chunks'])))
    names=report['arrays']
    retain(names['full_states'],[13,226],[(11,'full-input'),(12,'full-output')])
    retain(names['shape_outputs'],[12,224],[(11,'shape-output')])
    retain(names['shape_jacobians'],[12,224,224],[(11,'short-J')])
    retain(names['mean_tangent_rows'],[12,2,224],[(11,'mean-tangent-rows')])
    if references['full-input']['sha256']!=fields[0]['state_float64le_sha256']:
        raise ValueError('Initial full226 must be the original field0 state, including both means')
    def described(path):
        return dict(path=str(path),file=path.name,bytes=path.stat().st_size,sha256=B.sha(path))
    return dict(
        schema='original-stage43-step11-input-references-v1',
        actual41_result_sha256=STEP_RESULT_SHA,actual44_field_receipt_sha256=FIELD_RECEIPT_SHA,
        inputs=dict(result=described(result_path),report=described(report_path),
                    window=described(window_path),array_manifest=described(manifest_path),
                    field_receipt=described(receipt_path),
                    full_field_packet=dict(path=str(field_packet),**packet_descriptor)),
        references=references,selected_array_receipts=verified,
        original_stage=43,original_flow_step=11,new_shooting_stage=519,new_input_node=520,
        original_window=window,original_schedule=receipt['original_step_schedule'],
        original_fields=fields,original_sigma=receipt['original_sigma'],
        original_port_ratio=receipt['original_port_ratio'],
        all_four_selected_actual41_arrays_verified=True,
        unselected_actual41_arrays_not_reread_here=True,
        no_RHS_J_root_or_scientific_norm_computed=True)



def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('Native original-step capture science belongs only to public repository Actions')
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('failed-directory','cold-probe-summary','first-candidate-summary','v2-candidate-summary',
                 'candidate-directory','capture-directory','step-directory','field-receipt','source-topic','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--node-heap',type=int,default=6144)
    a=parser.parse_args();a.out=a.out.resolve()
    if a.out.exists() or any(a.out.is_relative_to(p.resolve()) for p in (a.capture_directory,a.step_directory,a.candidate_directory)):
        raise ValueError('Use a new independent original-step capture output directory')
    a.out.mkdir(parents=True)
    T=load(READER_NAME,READER_SHA,'_native_split_capture_metadata');B=T.load_base();history=B.load_frozen_history()
    frozen=dict(history.PINNED_SOURCES,**{B.HISTORY_SOURCE:B.HISTORY_SHA,
        'geometry_20261114_zero_rk_native_probe_v3_hook.mjs':B.V3_HOOK_SHA,
        SEED_NAME:SEED_SHA,READER_NAME:READER_SHA,CAPTURE_READER_NAME:CAPTURE_READER_SHA,WINDOW_NAME:WINDOW_SHA,PARENT_WINDOW_NAME:PARENT_WINDOW_SHA,
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
    local_reference=selected_step_references(a,B)
    B.write(a.out/'selected-step-reference-packets.json',local_reference)
    config_path=a.out/'stage43-local-j-input-config.json';original.write(config_path,prior['config'])
    hook=HERE/'geometry_20261114_native_stage43_local_j_probe_hook.mjs'
    request=dict(height=prior['height'],jacobian=True,audit=True)
    spec=dict(schema='original-native-stage43-local-j-capture-spec-v1',source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        window_module_sha256=WINDOW_SHA,frozen_sources=frozen,inputs=prior['inputs'],capture=capture,references=references,
        local_reference=local_reference,actual41_result_sha256=STEP_RESULT_SHA,actual44_field_receipt_sha256=FIELD_RECEIPT_SHA,
        original_public_run='43598917532',cold_baseline_public_run='43602823170',first_candidate_public_run='43603818345',
        v2_candidate_public_run='43604874829',completed_probe_public_run='43605912092',captured_reference_public_run='43611175099',
        candidate_state_chunks=candidate['state_chunks'],original_graph_scale_chunks=candidate['graph_chunks'],
        candidate_states_float64le_sha256=B.CANDIDATE_BITS_SHA,exact_height_float64le_sha256=B.HEIGHT_BITS_SHA,
        original_scales_float64le_sha256=B.SCALES_BITS_SHA,original_far_graph_float64le_sha256=B.FAR_BITS_SHA,
        restored_negative_zero_count=candidate['restored_negative_zeros'],
        original_source_sha256=prior['intent']['source_sha256'],numerical_configuration=prior['config'],
        numerical_parameters=candidate['summary']['numerical_parameters'],io_keys=sorted(IO_KEYS),
        output=str(a.out),fresh_request=request,planned_probe_stop=STOP,selected_stages=list(SELECTED),
        original_steps=12,expected_original_stages=1,selected_flow_step=11,actual_step_count_from_original_profile_schedule=True,
        additional_ODE_steps=0,new_original_long_J_evaluations=0,new_whole_tail_J_evaluations=0,no_J_evaluations=0,
        original_native_solve_called=False,endpoint_J_or_audit_computed=False,
        original_H_far_graphs_gains_sigma_and_tolerances_unchanged=True,task_completed=False)
    spec_path=a.out/'stage43-local-j-spec.json';B.write(spec_path,spec)
    previous=os.environ.get(VARIABLE);os.environ[VARIABLE]=str(spec_path)
    popen=original.subprocess.Popen;commands=[];client=None;started=time.monotonic()
    result=dict(schema='original-native-stage43-local-j-capture-result-v1',capture_completed=False,
        native_accepted=False,task_completed=False,source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        window_module_sha256=WINDOW_SHA,spec_sha256=B.sha(spec_path),capture_result_sha256=CAPTURE_SHA,
        actual41_result_sha256=STEP_RESULT_SHA,actual44_field_receipt_sha256=FIELD_RECEIPT_SHA,
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
        B.write(a.out/'verified-launch-intent.json',dict(schema='original-native-stage43-local-j-capture-verified-launch-v1',
            spec_sha256=B.sha(spec_path),hook_sha256=B.sha(hook),source_sha256=B.sha(__file__),actual_command=commands[0],
            current_sources=client.sources,current_capacity_sha256=B.sha(client.capacity_record),
            complete_current_ready_sha256=B.sha(a.out/'native_ready.json.gz'),
            identity_verified_before_request=True,initial_native_solve_calls=0,initial_response_cache_empty=True,
            inputs=prior['inputs'],capture_inputs=capture['inputs'],references=references,request=request))
        print(json.dumps(dict(event='original-native-stage43-local-j-identities-verified',
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
        summary_path=a.out/'stage43-local-j-summary.json'
        if summary_path.is_file():
            summary=B.read(summary_path);result['capture_summary_sha256']=B.sha(summary_path)
            for key in ('completed_local_J_blocks','completed_original_RK_field_calls','completed_original_stages',
                        'completed_local_J_evaluations','original_RK_field_entries',
                        'total_step_count','stage_reports','array_manifest','same_state_path_as_actual41','all_four_geometry_records_equal',
                        'field_reports','local_J_arrays','complete_step_comparisons','actual_failure',
                        'original_stage','original_flow_step','new_shooting_stage','new_input_node',
                        'original_h','original_port_ratio','original_sigma','reference_arrays','observed_step_arrays',
                        'returned_pointwise_local_J_matrices','actual41_did_not_save_the_original_four_local_A_arrays',
                        'current_local_A_are_new_calls_to_the_same_original_function'):
                result[key]=summary.get(key)
            result['planned_probe_stop_observed']=result.get('actual_original_failure_message')=='Error: '+STOP
            count=summary.get('total_step_count')
            result['capture_completed']=bool(summary.get('capture_completed') is True and
                type(count) is int and count==1 and summary.get('completed_local_J_blocks')==count and
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
    print(json.dumps(dict(event='original_native_stage43_local_J_probe_finished',capture_completed=result['capture_completed'],
        native_accepted=False,task_completed=False)),flush=True)
    return 0 if result['capture_completed'] else 2


if __name__=='__main__':raise SystemExit(main())

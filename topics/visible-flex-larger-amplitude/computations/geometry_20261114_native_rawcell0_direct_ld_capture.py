#!/usr/bin/env python3
"""Form direct-longdouble maps on all actual41 original868 saved step inputs.

Bind actual17/19/21/22/23/28 and the unchanged native constructor/source chain.
Keep the complete original226-state path and actual cusp integrationGrid.
Four original local A stream to one persistent direct-LD worker; no old tangent product is repeated.
Stop before native solve, whole-tail J, trial, endpoint J or final audit.
"""
from __future__ import annotations
import argparse
import gzip
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
WINDOW_NAME='geometry_20261114_native_rawcell0_direct_ld_window.mjs'
WINDOW_SHA='1ba3f30702b26aa78b4aceb0b2d3d5d71ea8fa858b114d982ead185330faa5d9'
CAPTURE_SHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
VARIABLE='VISIBLE_FLEX_NATIVE_RAWCELL0_DIRECT_LD_SPEC'
STOP='VISIBLE_NATIVE_RAWCELL0_DIRECT_LD_COMPLETE_V1'
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


STEP_RESULT_SHA='6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf'
PARENT_WINDOW_NAME='geometry_20261114_native_rawcell0_step_windows.mjs'
PARENT_WINDOW_SHA='07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b'
STEP_PRODUCER_NAME='geometry_20261114_native_rawcell0_step_capture.py'
STEP_PRODUCER_SHA='c2341018c6293e15ee8e5ba9109b331b29bee2e3e944514e1a0308afe8e6ffd5'
STEP_HOOK_NAME='geometry_20261114_native_rawcell0_step_capture_hook.mjs'
STEP_HOOK_SHA='2695cd2dc0abc66fe3f8ae8987b6ae3b50b884f692a418198347a61dddf24435'
WORKER_NAME='geometry_20261114_rawcell0_direct_ld_worker.py'
WORKER_SHA='87ab92d9234d6e58103d44d125ce5510f9cde34ac37df251b7e63dcb6747a9c8'
DIRECT_NAME='geometry_20261114_saved_stage_rk_covariance.py'
DIRECT_SHA='01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548'


def original_step_references(a,B):
    """Bind only the actual41 state/schedule/geometry evidence consumed here.

    The original short-J files are not consumed or recomputed by this producer.
    The later full-system adapter independently binds the complete old object.
    """
    import gzip
    directory=a.step_directory.resolve()
    result_path=directory/'result.json'
    if B.sha(result_path)!=STEP_RESULT_SHA:
        raise ValueError('Use the exact completed actual41 original-step capture')
    result=B.read(result_path)
    expected=dict(schema='original-native-rawcell0-step-capture-result-v1',capture_completed=True,
        source_sha256=STEP_PRODUCER_SHA,hook_sha256=STEP_HOOK_SHA,window_module_sha256=PARENT_WINDOW_SHA,
        capture_result_sha256=CAPTURE_SHA,original_protocol_requests=1,worker_exit_code=0,
        planned_probe_stop_observed=True,native_accepted=False,task_completed=False)
    for key,value in expected.items():
        if result.get(key)!=value:raise ValueError('Changed original actual41 result contract: '+key)
    small={}
    for row in result['small_output_files']:
        name=row['file']
        if Path(name).name!=name or name in small:
            raise ValueError('Unique original actual41 small-file inventory required')
        small[name]=row
    def pinned(row):
        relative=Path(row['file']);file=(directory/relative).resolve()
        if relative.is_absolute() or '..' in relative.parts or not file.is_relative_to(directory):
            raise ValueError('Consumed actual41 file must stay inside its immutable extraction')
        if not file.is_file() or file.stat().st_size!=row['bytes'] or B.sha(file)!=row['sha256']:
            raise ValueError('Changed original actual41 consumed file: '+row['file'])
        return file
    def obj(row):
        file=pinned(row);raw=file.read_bytes()
        unpacked=gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw
        if 'raw_sha256' in row and (hashlib.sha256(unpacked).hexdigest()!=row['raw_sha256'] or len(unpacked)!=row['raw_bytes']):
            raise ValueError('Changed original complete field packet')
        return json.loads(unpacked)
    summary_descriptor=small['rawcell0-step-summary.json']
    if summary_descriptor['sha256']!=result['capture_summary_sha256']:
        raise ValueError('Original result/summary identity mismatch')
    summary=obj(summary_descriptor)
    manifest_descriptor=result['array_manifest'];manifest=obj(manifest_descriptor)
    if summary['array_manifest']!=manifest_descriptor or manifest['schema']!='original-native-rawcell0-step-arrays-v1' or manifest['completed'] is not True:
        raise ValueError('Complete original array manifest required')
    if summary['capture_completed'] is not True or summary['completed_original_stages']!=list(SELECTED):
        raise ValueError('Every original rawCell0 stage must have completed')
    for key,value in (('source_sha256',STEP_PRODUCER_SHA),('hook_sha256',STEP_HOOK_SHA),
                      ('window_module_sha256',PARENT_WINDOW_SHA),('original_capture_result_sha256',CAPTURE_SHA)):
        if summary.get(key)!=value:raise ValueError('Original completed summary binding changed: '+key)
    entries={row['name']:row for row in manifest['arrays']}
    if len(entries)!=len(manifest['arrays']):raise ValueError('Unique original array names required')
    packets={row['file']:row for row in manifest['metadata_packets']}
    if len(packets)!=len(manifest['metadata_packets']):raise ValueError('Unique original metadata packets required')
    verified=[]
    def array(name,shape):
        record=entries[name]
        if record['shape']!=shape or record['dtype']!='<f8' or record['order']!='C' or record['completed'] is not True:
            raise ValueError('Complete original state/shape array required: '+name)
        width=8
        for size in shape[1:]:width*=size
        cursor=count_bytes=0;accumulated=hashlib.sha256()
        for index,chunk in enumerate(record['chunks']):
            if chunk['array']!=name or chunk['chunk_index']!=index or chunk['row_start']!=cursor or chunk['row_stop']<=cursor:
                raise ValueError('Original consumed array rows must be complete and contiguous')
            descriptor=dict(file=chunk['file'],bytes=chunk['bytes'],sha256=chunk['raw_sha256'])
            raw=pinned(descriptor).read_bytes()
            if len(raw)!=(chunk['row_stop']-cursor)*width:
                raise ValueError('Original state chunk dimensions changed')
            accumulated.update(raw);count_bytes+=len(raw);cursor=chunk['row_stop']
        if cursor!=shape[0] or count_bytes!=record['total_bytes'] or accumulated.hexdigest()!=record['raw_sha256']:
            raise ValueError('Complete original state/shape array byte identity failed')
        verified.append(dict(name=name,shape=shape,total_bytes=count_bytes,raw_sha256=record['raw_sha256'],
                             chunks_verified=len(record['chunks'])))
        return record
    stages={};total=0
    if len(summary['stage_reports'])!=72:raise ValueError('All72 original rawCell0 reports required')
    for n,report_descriptor in zip(SELECTED,summary['stage_reports']):
        report=obj(report_descriptor);count=report['step_count']
        if report['stage']!=n or type(count) is not int or count<=0 or len(report['schedule'])!=count:
            raise ValueError('Actual original stage/step count changed')
        window=obj(report['identity'])
        if window['stage']!=n or window['source']['original_flow_module_sha256']!='717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f':
            raise ValueError('Original complete step window identity changed')
        packet_descriptor=report['field_observations']
        if packets.get(packet_descriptor['file'])!=packet_descriptor:
            raise ValueError('Bind the complete original returned field observations')
        packet=obj(packet_descriptor)
        if packet['stage']!=n or packet['partial'] is not False or len(packet['fields'])!=4*count:
            raise ValueError('Every original four-field record is required')
        for k,schedule in enumerate(report['schedule']):
            if schedule['global_step']!=k or schedule['field_calls']!=4:
                raise ValueError('Keep complete inner-to-outer original step order')
            rows=packet['fields'][4*k:4*k+4]
            if any(row['global_step']!=k or row['field_index']!=j for j,row in enumerate(rows)):
                raise ValueError('Keep the four independent original fields in order')
        records={
            'full_states':array(report['arrays']['full_states'],[count+1,226]),
            'shape_outputs':array(report['arrays']['shape_outputs'],[count,224])}
        stages[str(n)]=dict(report=report_descriptor,window=report['identity'],field_packet=packet_descriptor,
            arrays=records,original_step_count=count)
        total+=count
    if total!=summary['total_step_count'] or result['total_step_count']!=total:
        raise ValueError('Actual original full step count must agree across complete records')
    return dict(schema='actual41-consumed-state-and-geometry-for-direct-LD-v1',directory=str(directory),
        actual41_result_sha256=STEP_RESULT_SHA,original_capture_result_sha256=CAPTURE_SHA,
        source_sha256=STEP_PRODUCER_SHA,hook_sha256=STEP_HOOK_SHA,window_module_sha256=PARENT_WINDOW_SHA,
        result=dict(file='result.json',bytes=result_path.stat().st_size,sha256=STEP_RESULT_SHA),
        summary=summary_descriptor,array_manifest=manifest_descriptor,
        prospective_layout=result['prospective_layout'],stages=stages,total_step_count=total,
        verified_consumed_arrays=verified,all_consumed_source_array_bytes_verified=True,
        original_short_J_arrays_not_read_or_recomputed=True,
        no_RHS_J_root_or_new_residual_computed_during_reference_binding=True)



def write_specification(path,value):
    """Store the complete evidence specification; hashes bind compressed bytes."""
    raw=(json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    packed=gzip.compress(raw,compresslevel=9,mtime=0)
    if len(packed)>=4_900_000:
        raise ValueError('Keep the complete gzip specification below the public5MB file limit')
    with path.open('xb') as stream:stream.write(packed)
    return dict(file=path.name,bytes=len(packed),sha256=hashlib.sha256(packed).hexdigest(),
        raw_bytes=len(raw),raw_sha256=hashlib.sha256(raw).hexdigest(),encoding='json-gzip')


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('Native original-step capture science belongs only to public repository Actions')
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('failed-directory','cold-probe-summary','first-candidate-summary','v2-candidate-summary',
                 'candidate-directory','capture-directory','step-directory','source-topic','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--node-heap',type=int,default=6144)
    a=parser.parse_args();a.out=a.out.resolve()
    if a.out.exists() or any(a.out.is_relative_to(p.resolve()) for p in (a.capture_directory,a.step_directory,a.candidate_directory)):
        raise ValueError('Use a new independent original-step capture output directory')
    a.out.mkdir(parents=True)
    T=load(READER_NAME,READER_SHA,'_native_split_capture_metadata');B=T.load_base();history=B.load_frozen_history()
    frozen=dict(history.PINNED_SOURCES,**{B.HISTORY_SOURCE:B.HISTORY_SHA,
        'geometry_20261114_zero_rk_native_probe_v3_hook.mjs':B.V3_HOOK_SHA,
        SEED_NAME:SEED_SHA,READER_NAME:READER_SHA,CAPTURE_READER_NAME:CAPTURE_READER_SHA,WINDOW_NAME:WINDOW_SHA,
        PARENT_WINDOW_NAME:PARENT_WINDOW_SHA,WORKER_NAME:WORKER_SHA,DIRECT_NAME:DIRECT_SHA,
        STEP_PRODUCER_NAME:STEP_PRODUCER_SHA,STEP_HOOK_NAME:STEP_HOOK_SHA,
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
    step_references=original_step_references(a,B)
    B.write(a.out/'actual41-consumed-reference-packets.json',step_references)
    config_path=a.out/'direct-ld-input-config.json';original.write(config_path,prior['config'])
    hook=HERE/'geometry_20261114_native_rawcell0_direct_ld_capture_hook.mjs'
    request=dict(height=prior['height'],jacobian=True,audit=True)
    spec=dict(schema='original-native-rawcell0-direct-ld-spec-v1',source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        window_module_sha256=WINDOW_SHA,worker_source_sha256=WORKER_SHA,
        direct_arithmetic_source_sha256=DIRECT_SHA,python_executable=sys.executable,
        step_references=step_references,actual41_result_sha256=STEP_RESULT_SHA,frozen_sources=frozen,inputs=prior['inputs'],capture=capture,references=references,
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
    spec_path=a.out/'direct-ld-spec.json.gz';specification=write_specification(spec_path,spec)
    previous=os.environ.get(VARIABLE);os.environ[VARIABLE]=str(spec_path)
    popen=original.subprocess.Popen;commands=[];client=None;started=time.monotonic()
    result=dict(schema='native-rawcell0-saved-step-direct-longdouble-maps-v1',capture_completed=False,completed=False,
        native_accepted=False,task_completed=False,source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        window_module_sha256=WINDOW_SHA,worker_source_sha256=WORKER_SHA,direct_arithmetic_source_sha256=DIRECT_SHA,
        actual41_result_sha256=STEP_RESULT_SHA,original_capture_result_sha256=CAPTURE_SHA,
        spec_sha256=B.sha(spec_path),specification=specification,capture_result_sha256=CAPTURE_SHA,
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
        B.write(a.out/'verified-launch-intent.json',dict(schema='original-native-rawcell0-direct-ld-verified-launch-v1',
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
        summary_path=a.out/'direct-ld-summary.json'
        if summary_path.is_file():
            summary=B.read(summary_path);result['capture_summary_sha256']=B.sha(summary_path)
            for key in ('completed_local_J_blocks','completed_original_RK_field_calls','completed_original_stages',
                        'original_RK_field_entries','direct_ld_worker_summary','working_precision',
                        'total_step_count','stage_reports','array_manifest','actual_failure'):
                result[key]=summary.get(key)
            result['planned_probe_stop_observed']=result.get('actual_original_failure_message')=='Error: '+STOP
            count=summary.get('total_step_count')
            result['capture_completed']=bool(summary.get('capture_completed') is True and
                summary.get('completed') is True and type(count) is int and count==step_references['total_step_count'] and
                count>0 and summary.get('completed_local_J_blocks')==count and
                summary.get('completed_original_RK_field_calls')==4*count and
                summary.get('original_RK_field_entries')==4*count and
                summary.get('completed_original_stages')==list(SELECTED) and result['planned_probe_stop_observed'] and
                result.get('worker_exit_code')==0 and result.get('original_protocol_requests')==1 and
                not result.get('unexpected_error') and not result.get('unexpected_complete_native_response_returned'))
        result['completed']=result['capture_completed']
        if summary_path.is_file():result['summary']=dict(file=summary_path.name,bytes=summary_path.stat().st_size,sha256=B.sha(summary_path))
        result['actual41_input_references']=dict(file='actual41-consumed-reference-packets.json',
            bytes=(a.out/'actual41-consumed-reference-packets.json').stat().st_size,
            sha256=B.sha(a.out/'actual41-consumed-reference-packets.json'))
        result['target_is_new_original_coordinate_binary64_J']=True
        result['original1372_base_residuals_boundaries_scales_and_old_to_new_not_recomputed']=True
        result['elapsed_seconds']=time.monotonic()-started
        result['small_output_files']=[dict(file=p.name,bytes=p.stat().st_size,sha256=B.sha(p))
            for p in sorted(a.out.iterdir()) if p.is_file() and p.name!='result.json']
        B.write(a.out/'result.json',result)
    print(json.dumps(dict(event='original_native_rawcell0_step_capture_finished',capture_completed=result['capture_completed'],
        native_accepted=False,task_completed=False)),flush=True)
    return 0 if result['capture_completed'] else 2


if __name__=='__main__':raise SystemExit(main())


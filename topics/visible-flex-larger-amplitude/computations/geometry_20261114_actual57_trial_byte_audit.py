#!/usr/bin/env python3
"""Read actual57 trial bytes and recorded facts only; never evaluate native math."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import struct
from pathlib import Path

PY_SHA='ebd3110e7ba9b2edeca155370d2c7fd6f02d3757ae285379d54a2b4a39793ccd'
HOOK_SHA='884d2d44439151d0dbc5d474e20ebe5c024e577396088f01717d33a522b50323'
QR_SHA='9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33'
BASE_SHA='6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8'
HEIGHT_SHA='c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f'
SCALE_SHA='ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc'
FAR_SHA='395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54'
CAP28_SHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
CAP41_SHA='6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf'
CAP54_SHA='e60da64312819a87388cfa96c209fc9188dca02c0ab055cbcc934f3507888ac6'
BODY_SHA='603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99'
STOP='Error: VISIBLE_NATIVE_DAMPED_CHAIN_TRIAL_REPLAY_ACCEPTED_STOP_V1'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(value, label):
    if not value:
        raise ValueError('Byte/metadata audit mismatch: '+label)


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def descriptor(root, row):
    relative=Path(row['file'])
    path=(root/relative).resolve()
    require(not relative.is_absolute() and '..' not in relative.parts and path.is_relative_to(root.resolve()),'descriptor path')
    raw=path.read_bytes()
    require(len(raw)==row['bytes'] and sha(raw)==row['sha256'],'file '+row['file'])
    return path,raw


def receipt(path, root):
    raw=path.read_bytes()
    return dict(file=str(path.relative_to(root)),bytes=len(raw),sha256=sha(raw))


def finite_words(raw):
    require(len(raw)%8==0,'f64 byte alignment')
    negative=zero=0
    for (bits,) in struct.iter_unpack('<Q',raw):
        require((bits>>52)&2047!=2047,'finite raw f64 word')
        if bits & ((1<<63)-1)==0:
            zero+=1
            negative+=int(bits==(1<<63))
    return dict(words=len(raw)//8,zero_words=zero,negative_zero_words=negative)


def rebuild_rows(packet, count, width):
    rows=packet['rows']
    require(len(rows)==count,'checkpoint full node count')
    parts=[]
    for n,row in enumerate(rows):
        require(type(row['node']) is int and row['node']==n and len(row['state'])==width,'checkpoint node ordering')
        state=list(row['state'])
        require(all(type(v) in (int,float) for v in state),'checkpoint numeric values')
        seen=set()
        for j in row['negative_zero_columns']:
            require(type(j) is int and 0<=j<width and j not in seen and state[j]==0,'negative-zero sidecar')
            state[j]=-0.0
            seen.add(j)
        parts.append(struct.pack('<'+str(width)+'d',*state))
    raw=b''.join(parts)
    return raw,finite_words(raw)


def number_record(record):
    raw=bytes.fromhex(record['float64le_hex'])
    require(len(raw)==8,'numberRecord width')
    (bits,)=struct.unpack('<Q',raw)
    finite=((bits>>52)&2047)!=2047
    if finite:
        require(record['classification']=='finite','finite scalar classification')
        encoded=struct.pack('<d',record['value'])
        # JSON may print -0 as0; the explicit bits retain its sign.
        require(encoded==raw or ((bits&((1<<63)-1))==0 and record['value']==0),'recorded scalar bits')
    else:
        require(record['value'] is None,'JSON nonfinite scalar value')
    return dict(float64le_hex=record['float64le_hex'],classification=record['classification'])


def audit_direction(qroot, result, spec, summary):
    path=qroot/'result.json.gz'
    require(sha(path.read_bytes())==result['direction_result_sha256'],'actual R273 result bytes')
    q=read(path)
    require(q['schema']=='complete-native-direct-LD-J1372-damped-square-root-direction-v1','R273 producer schema')
    require(q['source_sha256']==QR_SHA and q['linear_direction_computed'] is True,'actual R273 producer')
    require(q['eta_binary64']==result['direction_eta_binary64']==spec['direction']['eta_binary64'],'actual eta record')
    require(q['eta_cli_text']==result['direction_eta_cli_text']==spec['direction']['eta_cli_text'],'eta original CLI text')
    require(q['eta_cli_text']=='1' and q['eta_binary64']['float64le_hex']=='000000000000f03f','request57 explicit eta1 identity')
    require(q['new_matrix_identity_sha256']==result['new_matrix_identity_sha256'],'one same direct54 matrix identity')
    bp,_=descriptor(qroot,q['input_binding']);binding=read(bp)
    require(binding['new_matrix_identity_sha256']==q['new_matrix_identity_sha256']==spec['direction']['new_matrix_identity_sha256'],'same complete matrix binding')
    require(binding['actual41_result_sha256']==CAP41_SHA and binding['actual_direct_result']['sha256']==CAP54_SHA,'same exact input result bindings')
    _,mb=descriptor(qroot,q['array_manifest']);m=json.loads(gzip.decompress(mb))
    entries={e['name']:e for e in m['arrays']}
    require(len(entries)==len(m['arrays']),'unique complete QR inventory')
    output={}
    raws={}
    packets={}
    for label,packet_key,entry_key,entry_name,count,schema in [
        ('full','step_direction_checkpoint','step_delta','complete-original-coordinate-delta',1373,'complete-native-damped-chain-direction-v1'),
        ('restricted','restricted_direction_checkpoint','restricted_old_node_delta','complete-old-node-restricted-delta',577,'complete-original-node-restriction-of-damped-chain-direction-v1')]:
        pp,_=descriptor(qroot,q[packet_key]);packet=read(pp)
        require(packet['schema']==schema and packet['source_sha256']==QR_SHA,'direction checkpoint producer')
        require(packet['eta_binary64']==q['eta_binary64'],'checkpoint actual eta')
        require(packet['input_binding']==binding,'checkpoint complete original-target binding')
        require(packet['model_scope']==spec['direction']['model_scope'],'checkpoint complete damped-model identity')
        require(packet['native_accepted'] is False and packet['task_completed'] is False,'direction not native accepted')
        require(q[entry_key]==entries[entry_name],'complete raw direction manifest alias')
        _,raw=descriptor(qroot,q[entry_key])
        rebuilt,words=rebuild_rows(packet,count,224)
        require(raw==rebuilt and sha(raw)==packet['delta_float64le_sha256'],'complete direction raw/negative-zero rows')
        require(q[entry_key]['shape']==[count,224] and q[entry_key]['finite']==count*224,'actual complete direction shape')
        require(q[entry_key]['negative_zero']==words['negative_zero_words'],'actual negative-zero count')
        raws[label]=raw;packets[label]=packet
        output[label]=dict(packet=q[packet_key],raw=q[entry_key],word_audit=words)
    mapping=packets['full']['old_to_new']
    require(mapping==packets['restricted']['old_to_new']==spec['direction']['old_to_new'],'complete oldToNew identity')
    width=224*8
    require(b''.join(raws['full'][n*width:(n+1)*width] for n in mapping)==raws['restricted'],'all577 rows are byte-exact restriction')
    require(sha(raws['restricted'])==summary['direction_float64le_sha256']==spec['direction']['delta_float64le_sha256'],'trial actual direction SHA')
    output.update(full_row_count=1373,restriction_row_count=577,all_words_verified=True,
        no_QR_factor_or_exact_ledger_payload_reread=True,no_direction_arithmetic=True,
        eta=q['eta_binary64'],result_sha256=sha(path.read_bytes()))
    return output


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact-directory',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args();root=a.artifact_directory.resolve();p=root/'native-damped-chain-original-trial'
    result=read(p/'result.json');summary=read(p/'trial-replay-summary.json')
    checks={}
    files=[]
    for f in sorted(p.rglob('*')):
        if f.is_file():files.append(receipt(f,p))
    entries=result['small_output_files'];require(len({e['file'] for e in entries})==len(entries),'unique trial output inventory')
    for e in entries:descriptor(p,e)
    checks['complete_trial_output_inventory']=dict(files=len(files),listed_files=len(entries),all_listed_bytes_verified=True)
    require(result['schema']=='original-native-damped-chain-trial-replay-result-v1','new replay schema')
    require(result['source_sha256']==PY_SHA and result['hook_sha256']==HOOK_SHA,'actual57 source bytes')
    require(sha((p/'trial-replay-summary.json').read_bytes())==result['trial_replay_summary_sha256'],'summary digest')
    require(result['native_accepted'] is False and result['task_completed'] is False,'one-step-only result scope')
    require(result['original_native_requests']==1 and result['worker_exit_code']==0,'one completed original request')
    require(result['replay_completed'] is True and summary['replay_completed'] is True,'completed actual replay')
    require(result['new_J_evaluations']==0 and result['new_baseline_evaluations']==0,'no new J/baseline')
    spath,sbytes=descriptor(p,result['specification']);spec=read(spath)
    require(sbytes[:2]==b'\x1f\x8b','complete gzip specification')
    uncompressed=gzip.decompress(sbytes)
    require(len(uncompressed)==result['specification']['raw_bytes'] and sha(uncompressed)==result['specification']['raw_sha256'],'complete uncompressed spec identity')
    require(sha(sbytes)==result['spec_sha256']==summary['spec_sha256'],'one compressed spec identity')
    require(spec['source_sha256']==PY_SHA and spec['hook_sha256']==HOOK_SHA,'spec source identity')
    for key,digest in [('capture_result_sha256',CAP28_SHA),('actual_step_result_sha256',CAP41_SHA),('actual_direct_result_sha256',CAP54_SHA)]:
        require(result[key]==summary[key]==digest,'same actual input '+key)
    for key,digest in [('original_base_float64le_sha256',BASE_SHA),('original_height_float64le_sha256',HEIGHT_SHA),('original_scales_float64le_sha256',SCALE_SHA),('original_far_graph_float64le_sha256',FAR_SHA)]:
        require(summary[key]==digest,'original semantic bytes '+key)
    checks['specification']=result['specification']
    checks['direction']=audit_direction(root/'native-damped-chain-qr',result,spec,summary)
    core=read(p/'core-instrumentation.json');inside=core['internal_solve_source_identity']
    original=inside['restored_original_internal_solve_source'];instrumented=inside['instrumented_internal_solve_source']
    require(sha(original.encode())==inside['original_internal_solve_source_sha256'],'original internal solve source digest')
    require(sha(instrumented.encode())==inside['instrumented_internal_solve_source_sha256'],'actual internal solve source digest')
    restored=instrumented
    require(restored.count(inside['finish_insertion'])==1,'one finish insertion')
    restored=restored.replace(inside['finish_insertion'],'',1)
    for item in reversed(inside['replacements']):
        require(restored.count(item['after'])==1,'unique source reversal')
        restored=restored.replace(item['after'],item['before'],1)
    require(restored==original,'exact original internal source restoration')
    require(core['original_trial_loop_sha256']==core['replay_trial_loop_sha256']==BODY_SHA,'original ten-alpha body SHA')
    method=read(p/'actual-replay-method-identities.json')
    require(sha(method['actual_public_tail_solve_function_source'].encode())==method['actual_public_tail_solve_function_sha256'],'actual public solve source')
    require(method['internal_solve_source_identity']==inside,'public/internal identity receipt')
    require(method['core_instrumentation_sha256']==sha((p/'core-instrumentation.json').read_bytes()),'instrumentation file identity')
    checks['source_roundtrip']=dict(original_trial_loop_sha256=BODY_SHA,
        original_internal_solve_source_sha256=inside['original_internal_solve_source_sha256'],
        instrumented_internal_solve_source_sha256=inside['instrumented_internal_solve_source_sha256'],
        exact_original_source_restored=True,public_function_source_sha256=method['actual_public_tail_solve_function_sha256'])
    trials=summary['trials'];require(result['observed_trials']==trials,'result/summary trial identity')
    records=[json.loads(x) for x in (p/'trial-replay-records.jsonl').read_text().splitlines()]
    native_trials=[json.loads(x) for x in (p/'native_trials.jsonl').read_text().splitlines()]
    require(records==trials and len(native_trials)==len(trials),'complete observer/native trial count')
    steps=[1,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125]
    trial_facts=[];rejected_inputs=[]
    for k,(row,native) in enumerate(zip(trials,native_trials)):
        require(k<10 and row['iteration']==0 and row['trial']==k and row['step']==steps[k],'ordered original tenalpha')
        native_values={key:value for key,value in native.items() if key not in ('time','call')}
        observed={key:value for key,value in row.items() if key not in ('number_bits','actual_rejected_stage_input','actual_rejected_stage_node')}
        require(native_values==observed and native['call']==1,'native/observer original event')
        for record in row['number_bits'].values():number_record(record)
        require(row['number_bits']['baseNorm']['float64le_hex']=='c61182e94763a53f','actual28 cached norm bits')
        fact={key:row[key] for key in ('iteration','trial','step','baseNorm','kind','trialNorm','error','stage','rawCell','rawSegment') if key in row}
        fact['number_bits']=row['number_bits'];fact['native_time']=native['time'];trial_facts.append(fact)
        if 'actual_rejected_stage_input' in row:
            descriptor_row=row['actual_rejected_stage_input'];_,packed=descriptor(p,descriptor_row)
            raw=gzip.decompress(packed)
            require(len(raw)==descriptor_row['raw_bytes']==1792 and sha(raw)==descriptor_row['raw_sha256'],'failed-stage input raw bytes')
            require(descriptor_row['shape']==[1,224] and row['actual_rejected_stage_node']==row['stage']+1,'failed-stage input original node')
            rejected_inputs.append(dict(trial=k,node=row['actual_rejected_stage_node'],descriptor=descriptor_row,
                word_audit=finite_words(raw)))
    accepted=[row for row in trials if row['kind']=='accepted']
    require(result['trial_accepted']==summary['trial_accepted'],'one actual acceptance flag')
    selected=None
    if result['trial_accepted']:
        require(len(accepted)==1 and trials[-1]==accepted[0],'first actual accepted is final trial')
        require(accepted[0]['trialNorm']<accepted[0]['baseNorm'],'recorded original strict decrease')
        cp_path,_=descriptor(p,summary['selected_state']);packet=read(cp_path)
        _,packed=descriptor(p,summary['selected_state_binary']);raw=gzip.decompress(packed)
        rebuilt,word_stats=rebuild_rows(packet,577,224)
        require(raw==rebuilt and len(raw)==577*224*8,'full selected raw/rows bits')
        require(sha(raw)==summary['selected_state_binary']['raw_sha256']==packet['selected_state_float64le_sha256'],'selected raw identity')
        require(packet['schema']=='original-native-one-trial-selected-state-v1' and packet['source_sha256']==PY_SHA and packet['hook_sha256']==HOOK_SHA,'selected actual producer')
        require(packet['trial']==accepted[0] and packet['direction_result_sha256']==result['direction_result_sha256'],'selected actual accepted record')
        require(result['selected_state']==summary['selected_state'] and packet['states_binary']==summary['selected_state_binary'],'selected complete file aliases')
        live=read(p/'original-live-identity-before-seed.json')
        require(packet['parameters']==live['parameters'] and packet['rawNode']==live['rawNode'],'selected same complete original parameters and raw node layout')
        require(packet['original_base_float64le_sha256']==BASE_SHA and packet['capture_result_sha256']==CAP28_SHA,'selected original baseline ancestry')
        require(packet['actual_step_result_sha256']==CAP41_SHA and packet['actual_direct_result_sha256']==CAP54_SHA,'selected actual target provenance')
        require(packet['new_matrix_identity_sha256']==result['new_matrix_identity_sha256'],'selected same complete1372 target')
        require(packet['direction_float64le_sha256']==summary['direction_float64le_sha256'],'selected same restricted original-coordinate direction')
        require(packet['direction_eta_binary64']==result['direction_eta_binary64'],'selected actual eta')
        require(all(packet[k] is False for k in ('success','converged','native_tail_response','endpoint_J_computed','fresh_endpoint_audit_computed','task_completed')),'selected not complete native')
        require(sha(struct.pack('<112d',*packet['cutHeight']))==HEIGHT_SHA,'selected same full H bits')
        require(packet['original_direction_cut_or_far_entries_modified'] is False,'unprojected R273 direction')
        require(result['actual_original_failure_message']==STOP,'planned one accepted step stop')
        selected=dict(checkpoint=summary['selected_state'],binary=summary['selected_state_binary'],words=word_stats,
            original_cut_and_far_entries_not_reconstructed_or_projected=True,
            base_plus_alpha_delta_not_recomputed=True,selected_not_complete_native=True)
    else:
        require(not accepted and len(trials)==10 and result['selected_state'] is None and summary['selected_state'] is None,'all ten original trials actually rejected')
        require(result['actual_original_failure_message']==summary['expected_original_failure'],'actual original line search failure')
    native=read(p/'native_0001.json.gz')
    require(native['request']['jacobian'] is True and native['request']['audit'] is True,'unchanged original request flags')
    require(sha(struct.pack('<112d',*native['request']['height']))==HEIGHT_SHA,'original full physical H bytes')
    require(native['response']['failed']==result['actual_original_failure_message'],'actual native response failure/stop')
    require(summary['original_no_J_trial_evaluations']==len(trials)==result['fresh_original_no_J_trial_evaluations'],'complete original evaluation call count')
    require(summary['baseline_reuse_calls']==summary['saved_direction_calls']==1,'one cached baseline and actual direction')
    require(summary['new_corrections']==summary['new_J_evaluations']==summary['new_baseline_evaluations']==0,'no unreported correction or baseline')
    checks['trial']=dict(recorded_original_calls=len(trials),recorded_original_failure=result['actual_original_failure_message'],
        recorded_trials=trial_facts,rejected_stage_inputs=rejected_inputs,selected=selected,
        no_norm_or_guard_or_state_arithmetic_recomputed=True)
    report=dict(schema='actual57-original-trial-byte-and-record-audit-v1',audit_passed=True,
        original_run=43637356027,source_commit='adbdf144b14ae7adc71df09948a5c05f8a30e8b8',
        reader_source_sha256=sha(Path(__file__).read_bytes()),result=receipt(p/'result.json',p),
        scope='Pure stdlib original file SHA, f64 word/negative-zero reconstruction, source-string roundtrip and recorded-event comparisons only; no native/RHS/J/RK/QR/exact-dot/norm recomputation.',
        checks=checks,all_trial_files=files,QR_factor_and_exact_ledger_review_owned_separately=True,
        scientific_completion_claimed=False)
    a.out.write_text(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    print(json.dumps(dict(audit_passed=True,trial_files=len(files),trials=len(trials),trial_accepted=result['trial_accepted'],output_sha256=sha(a.out.read_bytes()))))


if __name__=='__main__':
    main()

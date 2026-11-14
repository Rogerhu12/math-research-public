#!/usr/bin/env python3
"""Audit saved original576 trial bytes and recorded facts; never run native math.

No candidate arithmetic, RHS/J/ODE, norm, argmax, dot product or solver is
recomputed. Max-location witnesses are checked against saved operand bytes.
This is a report consumer, not a native acceptance gate.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import struct
from pathlib import Path

PY_SHA='c337d880c29aaa865b6516fd679ffffe9410d30c893ff2f8e0cc4092f6adbec7'
HOOK_SHA='c104ff11b356cb3993ffd5ae97988259b2f27c91e492c7736d7a96a9ad450e36'
QR_SHA='e1a35bd82433cfe6525047cb3ceb3d0c434c1ebaa62680cb0f1fdab0e76cfaec'
ADAPTER_SHA='c78dfc6a5ef64a9de8bbbc857a927c6cd1078bbfb2281be62be4eb942014b207'
ENGINE_SHA='9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33'
CAP28_SHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
BASE_SHA='6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8'
HEIGHT_SHA='c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f'
SCALE_SHA='ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc'
FAR_SHA='395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54'
BODY_SHA='603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99'
EVALUATE_SHA='9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9'
STOP='Error: VISIBLE_NATIVE_ORIGINAL576_DAMPED_TRIAL_REPLAY_ACCEPTED_STOP_V1'
OBSERVATION_KEYS={'actual_original_noJ_observation','actual_input_state_float64le_sha256',
 'actual_input_changed_words','actual_original_evaluate_returned','original_returned_norm',
 'first_original_argmax_location'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition,label):
    if not condition:
        raise ValueError('Saved-byte/metadata audit mismatch: '+label)


def unpack(raw):
    return gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw


def read(path):
    return json.loads(unpack(path.read_bytes()))


def descriptor(root,row):
    relative=Path(row['file']);p=(root/relative).resolve()
    require(not relative.is_absolute() and '..' not in relative.parts and p.is_relative_to(root.resolve()),'bounded descriptor path')
    raw=p.read_bytes()
    require(len(raw)==row['bytes'] and sha(raw)==row['sha256'],'complete file '+row['file'])
    if 'raw_bytes' in row or 'raw_sha256' in row:
        decoded=unpack(raw)
        if 'raw_bytes' in row:require(len(decoded)==row['raw_bytes'],'unpacked bytes '+row['file'])
        if 'raw_sha256' in row:require(sha(decoded)==row['raw_sha256'],'unpacked SHA '+row['file'])
    return p,raw


def receipt(root,p):
    raw=p.read_bytes()
    return dict(file=str(p.relative_to(root)),bytes=len(raw),sha256=sha(raw))


def stats(raw):
    require(len(raw)%8==0,'complete f64 words')
    result=dict(words=len(raw)//8,finite=0,zero=0,negative_zero=0,nan=0,positive_infinity=0,negative_infinity=0)
    for (bits,) in struct.iter_unpack('<Q',raw):
        magnitude=bits&((1<<63)-1)
        if (bits>>52)&2047!=2047:result['finite']+=1
        elif bits&((1<<52)-1):result['nan']+=1
        elif bits>>63:result['negative_infinity']+=1
        else:result['positive_infinity']+=1
        if magnitude==0:
            result['zero']+=1
            result['negative_zero']+=int(bits==(1<<63))
    return result


def scalar(record):
    raw=bytes.fromhex(record['float64le_hex']);require(len(raw)==8,'scalar word width')
    bits=struct.unpack('<Q',raw)[0]
    finite=((bits>>52)&2047)!=2047
    if finite:
        require(record['classification'] in ('finite','negative-zero'),'finite scalar classification')
        require(type(record['value']) in (int,float),'finite scalar JSON value')
        encoded=struct.pack('<d',record['value'])
        require(encoded==raw or ((bits&((1<<63)-1))==0 and record['value']==0),'scalar JSON/word identity')
    else:
        require(record['value'] is None,'nonfinite JSON sentinel')
        expected='NaN' if bits&((1<<52)-1) else 'negative-infinity' if bits>>63 else 'positive-infinity'
        require(record['classification']==expected,'nonfinite scalar classification')
    return raw


def rows_raw(packet,nodes,width):
    require(len(packet['rows'])==nodes,'complete checkpoint nodes')
    output=[]
    for n,row in enumerate(packet['rows']):
        require(row['node']==n and len(row['state'])==width,'complete checkpoint row order')
        words=[];nonfinite={x['column']:x for x in row.get('nonfinite_columns',[])}
        require(len(nonfinite)==len(row.get('nonfinite_columns',[])),'unique nonfinite sidecar')
        for j,value in enumerate(row['state']):
            if j in nonfinite:
                require(value is None,'nonfinite JSON value omitted exactly')
                words.append(scalar(nonfinite[j]))
            else:
                require(type(value) in (int,float),'numeric checkpoint coordinate')
                words.append(struct.pack('<d',value))
        seen=set()
        for j in row['negative_zero_columns']:
            require(type(j) is int and 0<=j<width and j not in seen and row['state'][j]==0,'valid negative-zero sidecar')
            seen.add(j);words[j]=bytes.fromhex('0000000000000080')
        output.extend(words)
    return b''.join(output)


def byte_changes(raw,base):
    require(len(raw)==len(base)==577*224*8,'complete state word comparison')
    changed=0;nodes=0;first=[]
    for n in range(577):
        any_change=False
        for j in range(224):
            at=(n*224+j)*8;x=raw[at:at+8];b=base[at:at+8]
            if x!=b:
                changed+=1;any_change=True
                if len(first)<32:first.append(dict(node=n,column=j,base_float64le_hex=b.hex(),actual_trial_float64le_hex=x.hex()))
        nodes+=int(any_change)
    return dict(changed_words=changed,changed_nodes=nodes,first_changed_words=first,
                first_changed_word_limit=32,comparison_is_bits_only_no_candidate_arithmetic=True)


def audit_direction(qroot,result,spec,summary):
    qpath=qroot/'result.json.gz';require(sha(qpath.read_bytes())==result['direction_result_sha256'],'actual original576 result')
    q=read(qpath)
    require(q['schema']=='complete-native-original576-damped-square-root-direction-v1','new original576 producer schema')
    require(q['source_sha256']==QR_SHA and q['system_source_sha256']==ADAPTER_SHA and q['factor_engine_source_sha256']==ENGINE_SHA,'actual producer/adapter/borrowed engine identity')
    require(q['linear_direction_computed'] is True,'complete actual finite direction')
    require(q['eta_binary64']==result['direction_eta_binary64']==spec['direction']['eta_binary64'],'eta value/word alias')
    require(q['eta_cli_text']==result['direction_eta_cli_text']==spec['direction']['eta_cli_text'],'eta CLI identity')
    scalar(q['eta_binary64'])
    bp,_=descriptor(qroot,q['input_binding']);binding=read(bp)
    require(binding['schema']=='actual28-original576-complete-linear-system-binding-v1','new original576 target binding')
    require(binding['original_capture_result_sha256']==CAP28_SHA,'same actual28 finite data')
    require(binding['adapter_source_sha256']==ADAPTER_SHA,'same original576 binder')
    require(binding['new_matrix_identity_sha256']==q['new_matrix_identity_sha256']==result['new_matrix_identity_sha256']==spec['direction']['new_matrix_identity_sha256'],'one complete original576 identity')
    require(binding['old_to_new']==list(range(577)),'identity native-node mapping')
    mp,_=descriptor(qroot,q['array_manifest']);manifest=read(mp)
    require(manifest['schema']=='complete-native-original576-damped-direction-arrays-v1','original576 array schema')
    require(manifest['source_sha256']==QR_SHA and manifest['new_matrix_identity_sha256']==binding['new_matrix_identity_sha256'],'manifest producer and target')
    entries={x['name']:x for x in manifest['arrays']};require(len(entries)==len(manifest['arrays']),'unique producer array inventory')
    require(q['native_delta']==entries['complete-original-coordinate-delta'],'native direction manifest alias')
    cp,_=descriptor(qroot,q['native_direction_checkpoint']);packet=read(cp)
    require(packet['schema']=='complete-native-original576-damped-direction-v1' and packet['source_sha256']==QR_SHA,'complete native checkpoint source')
    require(packet['input_binding']==binding and packet['old_to_new']==list(range(577)),'checkpoint full target identity')
    require((packet['M'],packet['K'],packet['depth'],packet['original_depth'])==(112,224,576,576) and 'step_depth' not in packet,'complete original576 non-restriction layout')
    require(packet['eta_binary64']==q['eta_binary64'] and packet['model_scope']==spec['direction']['model_scope'],'checkpoint model identity')
    _,raw=descriptor(qroot,q['native_delta']);rebuilt=rows_raw(packet,577,224)
    require(raw==rebuilt and sha(raw)==packet['delta_float64le_sha256']==summary['direction_float64le_sha256'],'all native577 signed-zero words')
    count=stats(raw)
    require(count['finite']==129248 and count['negative_zero']==q['native_delta']['negative_zero'],'complete finite native direction inventory')
    original={};original_receipts={}
    for name,pin in [('base-states',BASE_SHA),('physical-height',HEIGHT_SHA),('original-scales',SCALE_SHA),('original-far-graph',FAR_SHA),('cut-target',None)]:
        desc=q['original_arrays'][name];_,data=descriptor(qroot,desc)
        require(desc==entries[desc['name']],'original operand manifest alias '+name)
        require(sha(data)==binding['raw_array_sha256'][name],'original target operand identity '+name)
        if pin:require(sha(data)==pin,'fixed actual28 input '+name)
        original[name]=data;original_receipts[name]=desc
    require(binding['raw_array_sha256']['base-states']==BASE_SHA,'same immutable original base')
    return dict(result=receipt(qroot,qpath),new_matrix_identity_sha256=binding['new_matrix_identity_sha256'],
        source_sha256=QR_SHA,checkpoint=q['native_direction_checkpoint'],raw=q['native_delta'],word_audit=count,
        original_operand_receipts=original_receipts,eta=q['eta_binary64'],eta_cli_text=q['eta_cli_text'],
        complete_native_direction_not_1372_restriction=True,
        no_QR_factors_or_exact_ledgers_recomputed_or_reread=True),original


def audit_sources(p):
    core=read(p/'core-instrumentation.json');inside=core['internal_solve_source_identity'];ev=core['evaluate_source_identity']
    restored=inside['instrumented_internal_solve_source']
    require(sha(restored.encode())==inside['instrumented_internal_solve_source_sha256'],'actual internal solve source SHA')
    require(restored.count(inside['finish_insertion'])==1,'unique finish observer')
    restored=restored.replace(inside['finish_insertion'],'',1)
    for item in reversed(inside['replacements']):
        require(restored.count(item['after'])==1,'unique saved-call reversal')
        restored=restored.replace(item['after'],item['before'],1)
    require(restored==inside['restored_original_internal_solve_source'] and sha(restored.encode())==inside['original_internal_solve_source_sha256'],'exact internal solve restoration')
    observed=ev['instrumented_evaluate_source'];restored_evaluate=observed
    require(sha(observed.encode())==ev['instrumented_evaluate_source_sha256'],'actual observed evaluate source SHA')
    for item in reversed(ev['insertions']):
        require(restored_evaluate.count(item['insertion'])==1,'unique evaluate insertion reversal')
        restored_evaluate=restored_evaluate.replace(item['insertion'],'',1)
    require(restored_evaluate==ev['restored_original_evaluate_source'] and sha(restored_evaluate.encode())==ev['original_evaluate_source_sha256']==EVALUATE_SHA,'exact original evaluate source restoration')
    require(core['original_trial_loop_sha256']==core['replay_trial_loop_sha256']==BODY_SHA,'unchanged original ten-trial body')
    method=read(p/'actual-replay-method-identities.json')
    require(method['evaluate_source_identity']==ev and method['internal_solve_source_identity']==inside,'complete method identity aliases')
    require(method['actual_public_evaluate_function_source']==observed and method['actual_public_evaluate_function_sha256']==sha(observed.encode()),'actual public evaluate toString is honestly observed source')
    require(sha(method['actual_public_tail_solve_function_source'].encode())==method['actual_public_tail_solve_function_sha256'],'actual unchanged public solve source')
    require(method['core_instrumentation_sha256']==sha((p/'core-instrumentation.json').read_bytes()),'complete instrumentation receipt')
    view=read(p/'restored-original-mathematical-identity-before-seed.json')
    require(view['evaluate_function_sha256']==EVALUATE_SHA and view['tail_solve_function_sha256']==method['actual_public_tail_solve_function_sha256'],'explicit original comparison view')
    require(view['far_graph_float64le_sha256']==FAR_SHA,'original comparison far identity')
    return dict(original_trial_body_sha256=BODY_SHA,original_evaluate_sha256=EVALUATE_SHA,
       actual_observed_evaluate_sha256=sha(observed.encode()),
       instrumented_internal_solve_sha256=inside['instrumented_internal_solve_source_sha256'],
       original_internal_solve_sha256=inside['original_internal_solve_source_sha256'],
       exact_source_reversal=True,actual_toString_and_restored_comparison_distinguished=True),view


def audit_observation(p,row,original,view):
    op,_=descriptor(p,row['actual_original_noJ_observation']);o=read(op)
    require(o['schema']=='original576-original-noJ-actual-trial-observation-v1' and o['trial']==row['trial'],'actual original noJ observation')
    require(o['source_sha256']==PY_SHA and o['hook_sha256']==HOOK_SHA,'actual observer source')
    require(o['actual_original_evaluate_entered'] is True and o['actual_original_evaluate_returned']==row['actual_original_evaluate_returned'],'observed original entry and return')
    require(o['original_trial_callback']=={k:v for k,v in row.items() if k not in OBSERVATION_KEYS},'original callback before observation aliases')
    enter,_=descriptor(p,o['enter_record']);entry=read(enter)
    require(entry['actual_input_states']==o['actual_input_states'] and entry['trial']==row['trial'],'pre-RHS immutable input receipt')
    require(entry['actual_original_evaluate_returned'] is False,'entry was recorded before original return')
    arrays={};counts={}
    def array(key,shape):
        desc=o[key];_,data=descriptor(p,desc)
        require(desc['shape']==shape and desc['dtype']=='<f8' and desc['order']=='C','complete observed array format '+key)
        require(len(data)==shape[0]*shape[1]*8,'complete observed array size '+key)
        count=stats(data)
        for field in ('finite','negative_zero','nan','positive_infinity','negative_infinity'):
            require(desc[field]==count[field],'observed raw word count '+key+' '+field)
        arrays[key]=data;counts[key]=count
        return data
    actual=array('actual_input_states',[577,224])
    require(sha(actual)==row['actual_input_state_float64le_sha256'],'original trial state raw alias')
    changes=byte_changes(actual,original['base-states'])
    require(changes==o['input_state_changes_against_actual28_base'],'all original input/base word comparisons')
    require(changes['changed_words']==row['actual_input_changed_words'],'word-change summary alias')
    for key,name in [('original_target_float64le_sha256','cut-target'),('original_scales_float64le_sha256','original-scales'),('original_far_graph_float64le_sha256','original-far-graph')]:
        require(o[key]==sha(original[name]),'unchanged observer original operand '+name)
    fact=dict(trial=row['trial'],kind=row['kind'],state=o['actual_input_states'],changed_words=changes['changed_words'],
        changed_nodes=changes['changed_nodes'],state_word_counts=counts['actual_input_states'],
        original_evaluate_returned=o['actual_original_evaluate_returned'],observation=row['actual_original_noJ_observation'])
    if not o['actual_original_evaluate_returned']:
        require(o['original_guard_or_evaluation_failure'] is not None,'actual original failure retained')
        require('actual_stage_residuals' not in o,'no fabricated full result for failed original evaluate')
        fact['original_failure']=o['original_guard_or_evaluation_failure']
        if 'actual_rejected_stage_input' in row:
            _,packed=descriptor(p,row['actual_rejected_stage_input']);failed=unpack(packed)
            node=row['actual_rejected_stage_node'];require(node==row['stage']+1,'original failing flow input node')
            require(actual[node*224*8:(node+1)*224*8]==failed,'failed-stage input equals actual full trial state words')
        return fact
    r=array('actual_stage_residuals',[576,224]);far=array('actual_far_residual',[1,112]);cut=array('original_cut_subtraction_readonly_copy',[1,112])
    for key in ('original_returned_norm','original_returned_minA','original_returned_minD','readonly_argmax_scan_norm'):scalar(o[key])
    require(o['original_returned_norm']==row['original_returned_norm']==row['number_bits']['trialNorm'],'original returned norm/callback same bits')
    require(o['first_argmax_location']==row['first_original_argmax_location'],'argmax small record alias')
    ap,_=descriptor(p,o['all_argmax_locations']);locations=read(ap)
    require(locations['trial']==row['trial'] and locations['original_returned_norm']==o['original_returned_norm'],'complete argmax record identity')
    require(locations['scan_norm']==o['readonly_argmax_scan_norm'],'scan bits are producer record only')
    if locations['argmax_defined']:
        require(len(locations['ties'])==o['argmax_tie_count'],'all reported ties retained')
        require((locations['ties'][0] if locations['ties'] else None)==o['first_argmax_location'],'first tie alias')
    else:require(o['argmax_tie_count'] is None and o['first_argmax_location'] is None,'undefined argmax scope')
    witness_count=0
    for location in locations['ties']+locations['nonfinite_rows']:
        kind=location['kind'];j=location['column']
        if kind=='stage':
            n=location['stage'];require(0<=n<576 and 0<=j<224,'stage witness location')
            require(location['rawCell']==view['stages'][n]['rawCell'] and location['rawSegment']==view['stages'][n]['rawSegment'],'stage witness original cell location')
            expected=r[(n*224+j)*8:(n*224+j+1)*8];sigma=original['original-scales'][n*8:(n+1)*8]
            require(location['original_global_row']==112+n*224+j,'stage witness row layout')
        elif kind=='far':
            require(0<=j<112 and location['original_global_row']==112+576*224+j,'far witness location')
            expected=far[j*8:(j+1)*8];sigma=original['original-scales'][576*8:577*8]
        else:
            require(kind=='cut' and 0<=j<112 and location['original_global_row']==j,'cut witness location')
            expected=cut[j*8:(j+1)*8];sigma=original['original-scales'][:8]
        require(scalar(location['residual'])==expected and scalar(location['original_sigma'])==sigma,'argmax original residual/sigma operand words')
        scalar(location['absolute_original_scaled_value'])
        witness_count+=1
    fact.update(returned_norm=o['original_returned_norm'],minA=o['original_returned_minA'],minD=o['original_returned_minD'],
        original_returned_array_receipts={key:o[key] for key in arrays if key!='actual_input_states'},
        argmax_tie_count=o['argmax_tie_count'],first_argmax=o['first_argmax_location'],
        reported_scan_bits_equal_norm=o['readonly_scan_norm_bits_equal_original_return'],
        saved_location_operand_words_verified=witness_count,
        argmax_and_norm_not_recomputed=True,cut_subtraction_not_recomputed=True)
    return fact


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial-directory',required=True,type=Path)
    parser.add_argument('--direction-directory',required=True,type=Path)
    parser.add_argument('--out',required=True,type=Path)
    a=parser.parse_args();p=a.trial_directory.resolve();qroot=a.direction_directory.resolve()
    result=read(p/'result.json');summary=read(p/'trial-replay-summary.json')
    require(result['schema']=='original-native576-damped-trial-replay-result-v1','new original576 trial schema')
    require(result['source_sha256']==PY_SHA and result['hook_sha256']==HOOK_SHA,'frozen actual trial sources')
    require(result['native_accepted'] is False and result['task_completed'] is False,'trial-only scope')
    files=[receipt(p,f) for f in sorted(p.rglob('*')) if f.is_file()]
    require(len({x['file'] for x in result['small_output_files']})==len(result['small_output_files']),'unique complete small inventory')
    for row in result['small_output_files']:descriptor(p,row)
    require(sha((p/'trial-replay-summary.json').read_bytes())==result['trial_replay_summary_sha256'],'complete summary file identity')
    sp,_=descriptor(p,result['specification']);spec=read(sp)
    require(spec['source_sha256']==PY_SHA and spec['hook_sha256']==HOOK_SHA,'complete gzip spec sources')
    require(sha(sp.read_bytes())==result['spec_sha256']==summary['spec_sha256'],'one stored spec identity')
    require(result['capture_result_sha256']==summary['capture_result_sha256']==CAP28_SHA,'actual28 cached target identity')
    for obj in (result,summary):
        require(obj['new_J_evaluations']==0 and obj['new_baseline_evaluations']==0,'no fresh J or baseline claim')
        require(obj['direction_is_not_a_1372_restriction'] is True,'new native target scope')
        require(obj['original_direction_cut_or_far_entries_modified'] is False,'soft cut/far direction untouched')
    direction,original=audit_direction(qroot,result,spec,summary)
    source,view=audit_sources(p)
    rows=summary['trials'];require(rows==result['observed_trials'],'trial summary/result aliases')
    records=[json.loads(line) for line in (p/'trial-replay-records.jsonl').read_text().splitlines()]
    native=[json.loads(line) for line in (p/'native_trials.jsonl').read_text().splitlines()]
    require(records==rows and len(native)==len(rows),'all original callbacks and observer records')
    steps=[1,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125]
    facts=[]
    for k,(row,nrow) in enumerate(zip(rows,native)):
        require(k<10 and row['trial']==k and row['iteration']==0 and row['step']==steps[k],'ordered original ten-alpha callbacks')
        nv={key:value for key,value in nrow.items() if key not in ('time','call')}
        require(all(key in row and row[key]==value for key,value in nv.items()) and nrow['call']==1,'original native callback values retained')
        for item in row['number_bits'].values():scalar(item)
        require(row['number_bits']['baseNorm']['float64le_hex']=='c61182e94763a53f','actual28 cached norm word')
        fact=audit_observation(p,row,original,view);fact['native_time']=nrow['time'];fact['step']=row['step']
        facts.append(fact)
    require([x['actual_original_noJ_observation'] for x in rows]==summary['actual_trial_observations']==result['actual_trial_observations'],'all complete observation inventory aliases')
    returned=sum(x['original_evaluate_returned'] for x in facts)
    require(summary['original_no_J_trial_returns']==result['returned_original_no_J_trial_evaluations']==returned,'actual original return counts')
    require(result['replay_completed']==summary['replay_completed'] and result['trial_accepted']==summary['trial_accepted'],'actual completion and selection flags')
    selected=None
    if result['replay_completed']:
        require(result['original_native_requests']==1 and result['worker_exit_code']==0,'one completed actual original request')
        require(summary['original_no_J_trial_evaluations']==result['fresh_original_no_J_trial_evaluations']==len(rows),'complete actual original evaluate entry counts')
        require(summary['observer_failure'] is None,'completed replay has no observer failure')
        accepted=[x for x in rows if x['kind']=='accepted']
        if result['trial_accepted']:
            require(len(accepted)==1 and accepted[0]==rows[-1],'first actual selected trial is final callback')
            cp,_=descriptor(p,summary['selected_state']);packet=read(cp)
            _,data=descriptor(p,summary['selected_state_binary']);raw=unpack(data)
            require(rows_raw(packet,577,224)==raw,'complete selected rows/signed-zero raw words')
            require(packet['source_sha256']==PY_SHA and packet['hook_sha256']==HOOK_SHA,'actual selected producer')
            require(sha(raw)==packet['selected_state_float64le_sha256']==facts[-1]['state']['sha256'],'selected equals actual observed accepted input bytes')
            require(packet['trial']==accepted[0] and packet['direction_result_sha256']==result['direction_result_sha256'],'selected original accepted callback/producer')
            require(packet['new_matrix_identity_sha256']==result['new_matrix_identity_sha256'],'selected original576 direction target')
            require(all(packet[k] is False for k in ('success','converged','native_tail_response','endpoint_J_computed','fresh_endpoint_audit_computed','task_completed')),'selected is not complete native')
            require(result['actual_original_failure_message']==STOP,'actual planned one-step stop')
            selected=dict(checkpoint=summary['selected_state'],binary=summary['selected_state_binary'],words=stats(raw),
                selected_equals_actual_original_evaluate_input_bits=True,no_candidate_or_strict_norm_recalculation=True)
        else:
            require(not accepted and len(rows)==10 and summary['selected_state'] is None,'actual complete original rejection')
            require(result['actual_original_failure_message']==summary['expected_original_failure'],'original exhausted failure preserved')
    report=dict(schema='original576-native-trial-saved-byte-audit-v1',auditor_source_sha256=sha(Path(__file__).read_bytes()),
        scope='Pure stdlib file/hash/bit/source comparisons and original reported facts; no candidate/RHS/J/ODE/norm/argmax/dot/solver recomputed',
        result=receipt(p,p/'result.json'),summary=receipt(p,p/'trial-replay-summary.json'),specification=result['specification'],
        trial_source_sha256=PY_SHA,hook_sha256=HOOK_SHA,all_listed_files_verified=True,
        file_count=len(files),listed_small_files=len(result['small_output_files']),files=files,
        direction=direction,source_roundtrip=source,actual_trial_facts=facts,selected=selected,
        replay_completed=result['replay_completed'],trial_accepted=result['trial_accepted'],
        original_failure_message=result.get('actual_original_failure_message'),observer_failure=summary.get('observer_failure'),
        all_actual_state_and_returned_payload_words_verified=True,
        original_returned_norm_and_argmax_values_are_copied_records_not_new_computations=True,
        all_zero_or_guard_or_acceptance_cause_not_inferred_from_metadata_alone=True,
        native_accepted=False,task_completed=False)
    a.out.write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(audit_complete=True,trial_count=len(rows),returned_original_evaluations=returned,
        trial_accepted=result['trial_accepted'],audit_sha256=sha(a.out.read_bytes()))))


if __name__=='__main__':main()

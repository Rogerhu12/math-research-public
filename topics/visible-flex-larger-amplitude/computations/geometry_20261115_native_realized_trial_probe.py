#!/usr/bin/env python3
"""Actual73 final original alpha1/512, one no-J pass and complete returned arrays.

The complete saved577 state and full577 correction are restored by exact
binary64 words. The original JS v+lambda*delta expression generates the
actual rounded trial. Original profile/root/RHS/RK/guard arithmetic and
norm remain; only reversible read-only source observations and a diagnostic
request loop are added. No fresh J, QR, native solve or endpoint audit.
Every scientific operation is confined to this public repository Actions.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import time
import traceback

HERE = Path(__file__).resolve().parent
HOOK = 'geometry_20261115_native_realized_trial_probe_hook.mjs'
ENVIRONMENT = 'VISIBLE_FLEX_ACTUAL73_REALIZED_TRIAL_SPEC'
NATIVE_RESULT_SHA = 'ade4fdac3adce104cb4e216e9d2f40b219bfca47d2c027ac548e6c65f65ab394'
SNAPSHOT_SHA = '2f9bf170c0366e9d5adaf003a9d0746f28a536171a32339e8a5f502313495e92'
STATE_SHA = 'f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6'
PARENT_PY_SHA = '938fbec22f0733fff6ceb22e6e9b7a9e12942c12d1eae31c608d8f517702df8c'
PARENT_HOOK_SHA = '099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d'
DIRECTION_SHA = '9d464f8239c375a2e95f207a3cfbad33e1f36037cd450cfefa2e3b165d86e3ff'
DELTA_SHA = '4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a'
PARENT_QR_SHA = '70bc10dfb31717b662265485d10a15028365dbba5db85ccf9c8f592226e33955'
PARENT_SYSTEM_SHA = '48297483617c56179fdd4d6b80e9aeeb1151bf89c90fd816ca41d2e3ccc0bcb3'
PRIMAL_SHA = 'f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9'
CORE_SHA = 'ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3'
EVALUATE_SHA = '9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9'
SOURCE_PINS = {
    'exact_20261114_true_tail_client.py': '1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09',
    'exact_20261114_seeded_zero_tail_client.py': 'a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776',
    'tail_frozen_worker.mjs': '3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054',
    'tail_resumable_engine.mjs': '1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8',
}
NATIVE_NAMES = (
    'current-correction-summary.json', 'current-input-config.json', 'native_runtime-config.json',
    'native_intent.json', 'native_ready.json.gz', 'native_capacity.json',
    'original-live-identity-before-failed61-seed.json', 'actual-current-method-identities.json',
    'core-instrumentation.json', 'native_trace.jsonl', 'native_trials.jsonl',
    'native_0001.json.gz', 'primal-flow-installation.json',
)
SHAPES = {
    'base-states': [577, 224], 'stage-residuals': [576, 224], 'stage-out': [576, 224],
    'original-scales': [1, 577], 'cut-residual': [1, 112], 'end-residual': [1, 112],
    'original-far-graph': [1, 112], 'physical-height': [1, 112], 'cut-target': [1, 112],
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def safe(root, name):
    root = Path(root).resolve()
    p = Path(name)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError('A relative evidence path is required')
    value = (root / p).resolve()
    if not value.is_relative_to(root) or not value.is_file():
        raise ValueError('Missing or escaping immutable evidence: ' + name)
    return value


def receipt(path, *, root=None, local=False):
    path = Path(path).resolve()
    out = dict(file=str(path.relative_to(Path(root).resolve())) if root else path.name,
               bytes=path.stat().st_size, sha256=sha(path))
    if local:
        out['path'] = str(path)
    return out


def verified(root, item):
    p = safe(root, item['file'])
    if p.stat().st_size != item['bytes'] or sha(p) != item['sha256']:
        raise ValueError('Original evidence bytes differ: ' + item['file'])
    return p


def write(path, value, *, compressed=False):
    path = Path(path)
    raw = (json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()
    stored = gzip.compress(raw, compresslevel=9, mtime=0) if compressed else raw
    if len(stored) >= 4_900_000:
        raise ValueError('Keep all metadata in complete bounded gzip packets')
    with path.open('xb') as stream:
        stream.write(stored)
    out = receipt(path)
    if compressed:
        out.update(encoding='json-gzip', raw_bytes=len(raw), raw_sha256=hashlib.sha256(raw).hexdigest())
    return out


def bind_array(directory, entry, expected_shape):
    if (entry['shape'] != expected_shape or entry['dtype'] != '<f8'
            or entry['order'] != 'C' or entry['completed'] is not True):
        raise ValueError('Complete original array shape and byte order required: ' + entry['name'])
    width = 1
    for n in expected_shape[1:]:
        width *= n
    digest = hashlib.sha256()
    row = 0
    total = 0
    for i, item in enumerate(entry['chunks']):
        if (item['array'] != entry['name'] or item['chunk_index'] != i or item['row_start'] != row
                or type(item['row_stop']) is not int or not row < item['row_stop'] <= expected_shape[0]):
            raise ValueError('Complete ordered original array chunks required')
        p = verified(directory, item)
        raw = p.read_bytes()
        if (len(raw) != (item['row_stop'] - row) * width * 8
                or hashlib.sha256(raw).hexdigest() != item['raw_sha256']):
            raise ValueError('Original chunk raw identity differs')
        for (word,) in struct.iter_unpack('<Q', raw):
            if (word >> 52) & 0x7ff == 0x7ff:
                raise ValueError('The saved original input array contains a nonfinite word')
        digest.update(raw)
        total += len(raw)
        row = item['row_stop']
    if (row != expected_shape[0] or total != entry['total_bytes']
            or digest.hexdigest() != entry['raw_sha256']):
        raise ValueError('Complete original array coverage differs')
    return dict(entry=entry, directory=str(Path(directory).resolve()))


def bind_inputs(args, equal, numerical_configuration, numerical_sources):
    native, snap, direction = (args.native_directory.resolve(), args.snapshot_directory.resolve(),
                               args.direction_directory.resolve())
    equal((args.native_result_sha256,args.snapshot_result_sha256,args.direction_result_sha256),
          (NATIVE_RESULT_SHA,SNAPSHOT_SHA,DIRECTION_SHA),'the three actual73 final-point receipts')
    result_path=safe(native,'result.json');equal(sha(result_path),NATIVE_RESULT_SHA,'actual73 native result')
    result=read(result_path)
    for key,value in dict(schema='native-noj-primal-current576-damped-solve-result-v1',
            source_sha256=PARENT_PY_SHA,hook_sha256=PARENT_HOOK_SHA,success=False,native_accepted=False,
            fresh_withJ_snapshots=3,current_R273_directions_returned=3,bridge_failure=None,
            original_native_requests=1,only_core_nonlinear_correction_call_replaced=True,
            independently_identified_withJ_flow_replaced=True,new_primal_variational_source_sha256=PRIMAL_SHA).items():
        equal(result[key],value,'actual73 native result '+key)
    listed={row['file']:row for row in result['small_output_files']}
    equal(len(listed),len(result['small_output_files']),'unique original native inventory')
    native_inputs={'result.json':receipt(result_path,local=True)};records={}
    for name in NATIVE_NAMES:
        p=verified(native,listed[name]);native_inputs[name]=receipt(p,local=True)
        if not name.endswith('.jsonl'):records[name]=read(p)
    summary=records['current-correction-summary.json']
    equal((summary['snapshots_completed'],summary['directions_returned']),(3,3),'three true current points')
    selected=summary['iterations'][2]
    equal((selected['native_call'],selected['nonlinear_iteration'],selected['snapshot_sequence']),
          (1,2,2),'actual last iteration')
    equal(selected['current_state_sha256'],STATE_SHA,'actual final complete current state')
    snapshot_path=safe(snap,'result.json');equal(sha(snapshot_path),SNAPSHOT_SHA,'actual fresh snapshot result')
    equal(receipt(snapshot_path),dict(file='result.json',bytes=selected['snapshot']['bytes'],
          sha256=selected['snapshot']['sha256']),'summary/snapshot original receipt')
    snapshot=read(snapshot_path)
    for key,value in dict(schema='noj-primal-current-native576-withJ-snapshot-result-v1',snapshot_completed=True,
            source_sha256=PARENT_PY_SHA,hook_sha256=PARENT_HOOK_SHA,native_call=1,nonlinear_iteration=2,
            snapshot_sequence=2,M=112,K=224,depth=576,current_state_sha256=STATE_SHA,
            original_fresh_withJ_already_returned=True).items():
        equal(snapshot[key],value,'original final snapshot '+key)
    context_path=verified(snap,snapshot['context']);manifest_path=verified(snap,snapshot['manifest'])
    context,manifest=read(context_path),read(manifest_path)
    equal(context['current_original_norm'],snapshot['actual_current_original_norm'],'original norm record')
    equal(context['current_original_norm'],selected['source_current_withJ_norm'],'bridge norm record')
    for key in ('source_sha256','hook_sha256','native_call','nonlinear_iteration','snapshot_sequence'):
        equal(context[key],snapshot[key],'current context '+key)
        equal(manifest[key],snapshot[key],'current manifest '+key)
    equal(context['fresh_current_evaluate_completed'],True,'fresh original current evaluation')
    equal(context['no_cached_baseline'],True,'no old numerical baseline')
    equal(context['same_original_noJ_primal_contract'],True,'actual73 same noJ primal contract')
    equal(context['original_evaluate_source_not_instrumented'],True,'actual73 evaluate source')
    equal(context['primal_flow_implementation']['source_sha256'],PRIMAL_SHA,'actual73 fresh-J implementation')
    equal((manifest['M'],manifest['K'],manifest['depth']),(112,224,576),'full original dimensions')
    entries={entry['name']:entry for entry in manifest['arrays']}
    equal(set(entries),set(SHAPES)|{'stage-jacobians'},'complete original snapshot descriptor set')
    arrays={name:bind_array(snap,entries[name],shape) for name,shape in SHAPES.items()}
    for name in SHAPES:
        equal(entries[name]['raw_sha256'],context['raw_array_sha256'][name],'original raw '+name)
    equal(entries['base-states']['raw_sha256'],STATE_SHA,'all577 original current state words')
    equal(entries['stage-jacobians']['shape'],[576,224,224],'J descriptor shape only in native probe')
    equal(entries['stage-jacobians']['raw_sha256'],context['raw_array_sha256']['stage-jacobians'],
          'J descriptor identity only; separate exact consumer reads payload')
    flow_path=verified(snap,context['flow_return_metadata']);core_path=verified(snap,context['core_instrumentation'])
    install_path=verified(snap,context['primal_flow_implementation']['installation_receipt'])
    equal(sha(core_path),native_inputs['core-instrumentation.json']['sha256'],'same original core receipt')
    equal(sha(install_path),native_inputs['primal-flow-installation.json']['sha256'],'same original flow receipt')
    intent,ready=records['native_intent.json'],records['native_ready.json.gz']
    config,runtime=records['current-input-config.json'],records['native_runtime-config.json']
    equal(sha(safe(native,'current-input-config.json')),intent['source_sha256']['input_config'],'input config SHA')
    equal(sha(safe(native,'native_runtime-config.json')),intent['source_sha256']['runtime_config'],'runtime config SHA')
    equal(numerical_configuration(runtime),numerical_configuration(config),'unchanged numerical configuration')
    equal(context['numerical_configuration'],numerical_configuration(config),'current snapshot configuration')
    if 'initialCheckpoint' in config or ready['warmEmbedding'] is not None:
        raise ValueError('No geometric remapping of this actual final state')
    equal(numerical_sources(intent['source_sha256']),context['original_sources'],'every original numerical source')
    live=records['original-live-identity-before-failed61-seed.json']
    equal(live['parameters'],context['parameters'],'original complete numerical parameters')
    equal(live['rawNode'],context['rawNode'],'actual physical raw-node indices')
    equal(live['stages'],context['cells'],'all original stage profiles')
    for source,dest in (('graphs_float64le_sha256','graphs_sha256'),
                       ('gains_float64le_sha256','gains_sha256'),('far_graph_float64le_sha256','far_graph_sha256')):
        equal(live[source],context[dest],'all original '+dest)
    equal(live['evaluate_function_sha256'],EVALUATE_SHA,'original evaluate before new read-only observations')
    packet=records['native_0001.json.gz'];cp=packet['response']['checkpoint']
    equal(packet['response']['failed'],'Error: multiple-shooting line search failed at 0.000060618737006888706',
          'literal original failed-request message')
    equal(cp['rawNode'],[0,72,144,216,288,360,432,504,576],'original nine physical boundaries')
    equal(len(cp['states']),577,'literal original complete checkpoint nodes')
    if any(len(row)!=224 for row in cp['states']):raise ValueError('Complete224-word checkpoint rows required')
    literal=b''.join(struct.pack('<d',v) for row in cp['states'] for v in row)
    equal(hashlib.sha256(literal).hexdigest(),STATE_SHA,'literal failure state versus saved raw state')
    equal(sum(word==0x8000000000000000 for (word,) in struct.iter_unpack('<Q',literal)),0,
          'this actual failure checkpoint had no lost negative zero')
    for node,row in zip(cp['rawNode'],cp['rawStates']):
        equal(b''.join(struct.pack('<d',x) for x in row),literal[node*224*8:(node+1)*224*8],
              'literal original raw physical-node alias')
    physical=b''.join(struct.pack('<d',x) for x in packet['request']['height'])
    equal(hashlib.sha256(physical).hexdigest(),entries['physical-height']['raw_sha256'],'full actual request H')
    trials=[json.loads(line) for line in safe(native,'native_trials.jsonl').read_text().splitlines() if line.strip()]
    actual=[row for row in trials if row['call']==1 and row['iteration']==2 and row['trial']==9]
    equal(len(actual),1,'the one recorded actual73 alpha1/512 trial')
    equal((actual[0]['step'],actual[0]['kind']),(0.001953125,'residual-not-decreasing'),'original selected alpha/class')
    equal(struct.pack('<d',actual[0]['trialNorm']),struct.pack('<d',actual[0]['baseNorm']),
          'original selected scalar plateau, without any complete-state claim')
    qr_path=safe(direction,'result.json.gz');equal(sha(qr_path),DIRECTION_SHA,'original last full direction result')
    qr=read(qr_path)
    for key,value in dict(schema='complete-native-noj-primal-current576-damped-square-root-direction-v1',
            source_sha256=PARENT_QR_SHA,system_source_sha256=PARENT_SYSTEM_SHA,
            native_call=1,nonlinear_iteration=2,snapshot_sequence=2,current_state_sha256=STATE_SHA,
            linear_direction_computed=True,diagnostic_completed=True,primal_flow_source_sha256=PRIMAL_SHA).items():
        equal(qr[key],value,'actual last QR result '+key)
    equal(qr['snapshot_result'],receipt(snapshot_path),'same actual fresh snapshot')
    equal(qr['new_matrix_identity_sha256'],selected['direction']['new_matrix_identity_sha256'],'same full finite matrix')
    direction_inputs={'result':receipt(qr_path,local=True)}
    for key in ('input_binding','native_delta','native_direction_checkpoint','array_manifest'):
        q=verified(direction,qr[key]);direction_inputs[key]=receipt(q,local=True)
    delta_path=Path(direction_inputs['native_delta']['path']);delta=delta_path.read_bytes()
    equal(qr['native_delta']['sha256'],DELTA_SHA,'full actual delta SHA')
    equal((qr['native_delta']['shape'],qr['native_delta']['dtype'],qr['native_delta']['order']),
          ([577,224],'<f8','C'),'complete original-coordinate delta layout')
    equal((len(delta),hashlib.sha256(delta).hexdigest()),(1033984,DELTA_SHA),'complete delta raw words')
    if any((word>>52)&0x7ff==0x7ff for (word,) in struct.iter_unpack('<Q',delta)):
        raise ValueError('The actual complete delta must be finite')
    binding=read(Path(direction_inputs['input_binding']['path']))
    dcp=read(Path(direction_inputs['native_direction_checkpoint']['path']))
    dm=read(Path(direction_inputs['array_manifest']['path']))
    equal(dm['source_sha256'],PARENT_QR_SHA,'original direction manifest source')
    equal(dm['schema'],'complete-native-noj-primal-current576-damped-direction-arrays-v1','original direction manifest schema')
    equal([entry for entry in dm['arrays'] if entry.get('name')==qr['native_delta']['name']],
          [qr['native_delta']],'complete delta descriptor in original manifest')
    equal(dcp['schema'],'complete-native-noj-primal-current576-damped-direction-v1','full current576 checkpoint schema')
    equal(dcp['source_sha256'],PARENT_QR_SHA,'actual direction checkpoint source')
    equal(dcp['input_binding'],binding,'actual checkpoint complete current system binding')
    for key in ('native_call','nonlinear_iteration','snapshot_sequence','current_state_sha256',
                'new_matrix_identity_sha256','snapshot_result','primal_flow_source_sha256'):
        equal(dcp[key],qr[key],'actual current direction point '+key)
    equal((dcp['M'],dcp['K'],dcp['depth'],dcp['original_depth'],dcp['old_to_new']),
          (112,224,576,576,list(range(577))),'complete native layout, not a restriction')
    equal(dcp['delta_float64le_sha256'],DELTA_SHA,'actual CP/raw delta identity')
    equal(len(dcp['rows']),577,'all complete signed-zero direction rows')
    recovered=bytearray()
    for n,row in enumerate(dcp['rows']):
        equal((row['node'],len(row['state'])),(n,224),'complete ordered direction row')
        negative=row['negative_zero_columns']
        equal(negative,sorted(set(negative)),'unique ordered negative-zero sidecar')
        if any(type(j) is not int or not 0<=j<224 for j in negative):raise ValueError('Invalid original signedzero index')
        for j,value in enumerate(row['state']):
            if j in negative:
                if value!=0:raise ValueError('Negative-zero sidecar must identify a zero')
                value=-0.0
            recovered.extend(struct.pack('<d',value))
    equal(bytes(recovered),delta,'full577 actual direction checkpoint including all25 signedzero words')
    return dict(native_inputs=native_inputs,native_result=receipt(result_path),snapshot_result=receipt(snapshot_path),
        direction_result=receipt(qr_path),direction_directory=str(direction),direction_inputs=direction_inputs,
        direction_native_delta=qr['native_delta'],direction_binding=binding,direction_checkpoint_identity={
            key:dcp[key] for key in dcp if key not in ('rows','input_binding')},
        original_selected_trial=actual[0],snapshot_directory=str(snap),
        snapshot_inputs=dict(result=receipt(snapshot_path,local=True),context=receipt(context_path,local=True),
            manifest=receipt(manifest_path,local=True),flow_metadata=receipt(flow_path,local=True),
            core=receipt(core_path,local=True),primal_installation=receipt(install_path,local=True)),
        context=context,arrays=arrays,original_J_descriptor_only=entries['stage-jacobians'],live=live,
        intent=intent,ready=ready,capacity=records['native_capacity.json'],config=numerical_configuration(config))


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public'):
        raise RuntimeError('The original no-J replay runs only in this public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('native-directory', 'snapshot-directory', 'direction-directory', 'source-topic', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--native-result-sha256', required=True)
    parser.add_argument('--snapshot-result-sha256', required=True)
    parser.add_argument('--direction-result-sha256', required=True)
    parser.add_argument('--node-heap', type=int, default=6144)
    args = parser.parse_args()
    output = args.out.resolve()
    if (output.is_relative_to(args.native_directory.resolve())
            or output.is_relative_to(args.snapshot_directory.resolve())
            or output.is_relative_to(args.direction_directory.resolve())):
        raise ValueError('Keep new probe outputs outside immutable original evidence')
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError('Use a fresh diagnostic output directory')
    for name, digest in SOURCE_PINS.items():
        if sha(HERE / name) != digest:
            raise ValueError('The unchanged original source differs: ' + name)
    from exact_20261114_seeded_zero_tail_client import (
        same, numerical_configuration, numerical_sources, ready_semantics, IO_KEYS)
    import exact_20261114_true_tail_client as original

    def equal(left, right, label):
        if not same(left, right):
            raise ValueError('Realized-trial no-J identity differs: ' + label)

    bound = bind_inputs(args, equal, numerical_configuration, numerical_sources)
    config_path = output / 'probe-input-config.json'
    write(config_path, bound['config'])
    hook = HERE / HOOK
    spec = dict(schema='actual73-iteration2-realized-noJ-trial-probe-spec-v1',
        source_sha256=sha(__file__), hook_sha256=sha(hook), frozen_sources=SOURCE_PINS,
        original_public_run='43657001633', original_native_result_sha256=NATIVE_RESULT_SHA,
        original_snapshot_result_sha256=SNAPSHOT_SHA, current_state_sha256=STATE_SHA,
        original_evaluate_source_sha256=EVALUATE_SHA, original_core_file_sha256=CORE_SHA,
        numerical_configuration=bound['config'], numerical_parameters=bound['live']['parameters'],
        original_source_sha256=bound['context']['original_sources'], original_live_identity=bound['live'],
        io_keys=sorted(IO_KEYS), output=str(output), inputs=bound['native_inputs'],
        snapshot_inputs=bound['snapshot_inputs'], original_arrays=bound['arrays'],
        direction_inputs=bound['direction_inputs'],original_direction_result_sha256=DIRECTION_SHA,
        direction_raw_sha256=DELTA_SHA,direction_native_delta=bound['direction_native_delta'],
        original_selected_trial=bound['original_selected_trial'],actual_trial_index=9,
        alpha_expression='2**(-k)',trial_expression='states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*cor.delta[n][j]))',
        original_J_descriptor_only=bound['original_J_descriptor_only'],
        saved_withJ_norm=bound['context']['current_original_norm'],
        original_nonlinear_iteration=2, original_snapshot_sequence=2, original_native_call=1,
        actual_original_trial_expression_without_projection=True, original_native_solve_requested=False,
        new_withJ_requested=False, expected_noJ_evaluate_calls=1, no_scientific_acceptance_threshold_added=True)
    spec_path = output / 'realized-trial-spec.json.gz'
    specification = write(spec_path, spec, compressed=True)
    input_binding=write(output/'input-binding.json.gz',dict(
        schema='actual73-iteration2-realized-noJ-trial-input-binding-v1',
        source_sha256=sha(__file__),hook_sha256=sha(hook),original_public_run=43657001633,
        native_result=bound['native_result'],snapshot_result=bound['snapshot_result'],
        direction_result=bound['direction_result'],current_state_sha256=STATE_SHA,direction_sha256=DELTA_SHA,
        original_context=bound['context'],original_snapshot_arrays={name:value['entry'] for name,value in bound['arrays'].items()},
        original_J_descriptor_only=bound['original_J_descriptor_only'],original_direction_native_delta=bound['direction_native_delta'],
        original_direction_binding=bound['direction_binding'],original_direction_checkpoint_identity=bound['direction_checkpoint_identity'],
        original_selected_trial=bound['original_selected_trial'],actual_trial_index=9,
        alpha=dict(value=0.001953125,float64le_hex=struct.pack('<d',0.001953125).hex(),classification='finite'),
        original_raw_state_and_delta_unchanged=True,old_native_failure_not_a_completed_anchor=True,
        original_J_payload_not_read_by_native_probe=True,no_new_numerical_acceptance_gate=True),compressed=True)
    previous_env = os.environ.get(ENVIRONMENT)
    popen = original.subprocess.Popen
    commands = []
    client = None
    started = time.monotonic()
    result = dict(schema='actual73-iteration2-realized-noJ-trial-probe-result-v1',
        source_sha256=sha(__file__), hook_sha256=sha(hook), specification=specification,
        input_native_result=bound['native_result'], input_snapshot_result=bound['snapshot_result'],
        input_binding=input_binding,original_snapshot_result_sha256=SNAPSHOT_SHA,
        direction_result_sha256=DIRECTION_SHA,base_state_sha256=STATE_SHA,direction_sha256=DELTA_SHA,
        original_state_sha256=STATE_SHA, no_TailClient_solve_called=True,
        saved_J_payloads_read=False, new_J_evaluations=0, newton_corrections=0,
        native_accepted=False, task_completed=False)

    def observed_popen(command, *positional, **keywords):
        worker = str(HERE / 'tail_frozen_worker.mjs')
        if not isinstance(command, list) or worker not in command:
            return popen(command, *positional, **keywords)
        if len(command) != 8 or command[0] != 'node' or command[4] != '--import' or command[6] != worker:
            raise ValueError('Only the original worker launch receives the diagnostic request loop')
        actual = list(command[:6]) + ['--import', str(hook)] + list(command[6:])
        commands.append(actual)
        return popen(actual, *positional, **keywords)

    code = 2
    try:
        os.environ[ENVIRONMENT] = str(spec_path)
        original.subprocess.Popen = observed_popen
        try:
            client = original.TailClient(config_path, args.source_topic.resolve() / 'repro/source-root',
                output / 'original-constructor', node_heap=args.node_heap)
        finally:
            original.subprocess.Popen = popen
        equal(numerical_configuration(client._configuration), bound['config'], 'all current numerical settings')
        equal(numerical_sources(client.sources), bound['context']['original_sources'], 'all current original source bytes')
        equal(ready_semantics(client.ready), ready_semantics(bound['ready']), 'all original/current ready semantics')
        capacity = original.read(client.capacity_record)
        for key in ('name', 'capacity', 'requestedCapacity', 'nodeVersion', 'adapterSHA256',
                    'originalConstructorCapacity', 'numericalChange', 'retained', 'files'):
            equal(capacity[key], bound['capacity'][key], 'original/current capacity ' + key)
        if len(commands) != 1 or client.calls != 0 or client.cache_key is not None:
            raise ValueError('One fresh original constructor with no imported response cache is required')
        launch = dict(schema='actual73-current576-realized-trial-noJ-verified-launch-v1',
            source_sha256=sha(__file__), hook_sha256=sha(hook), spec_sha256=sha(spec_path),
            current_sources=client.sources, actual_command=commands[0], identity_verified_before_evaluation=True,
            complete_current_ready=receipt(output / 'original-constructor_ready.json.gz'),
            complete_current_capacity=receipt(client.capacity_record), original_native_solve_calls=0)
        write(output / 'verified-launch-intent.json', launch)
        result['verified_launch'] = receipt(output / 'verified-launch-intent.json')
        print(json.dumps(dict(event='realized-trial-noJ-identities-verified', current_state_sha256=STATE_SHA,
                              saved_snapshot_sha256=SNAPSHOT_SHA, requested_original_evaluations=1)), flush=True)
        client.proc.stdin.write(json.dumps(dict(realized_trial_noJ=sha(spec_path))) + '\n')
        client.proc.stdin.flush()
        with (output / 'diagnostic-stdout.jsonl').open('x') as stream:
            for line in client.proc.stdout:
                stream.write(line)
                stream.flush()
                print(line.rstrip(), flush=True)
        result['worker_exit_code'] = client.proc.wait()
        if result['worker_exit_code'] != 0:
            raise RuntimeError('The diagnostic protocol failed; preserve the original stderr and identity receipts')
        summary_path = output / 'summary.json'
        summary = read(summary_path)
        equal(summary['schema'], 'actual73-iteration2-realized-noJ-trial-probe-summary-v1', 'actual summary schema')
        equal(summary['probe_completed'], True, 'actual diagnostic reached its end')
        equal(summary['original_noJ_evaluate_calls'], 1, 'one original no-J call')
        result.update(probe_completed=True, evaluation_returned=summary['evaluation_returned'],
            original_noJ_evaluate_calls=summary['original_noJ_evaluate_calls'],
            original_native_solve_calls=client.calls, summary=receipt(summary_path),
            array_manifest=summary['output_array_manifest'],alpha=summary['alpha'],
            observer_io_failure=summary.get('observer_io_failure'),
            completed=summary['evaluation_returned'] and summary.get('observer_io_failure') is None)
        code = 0 if result['completed'] else 2
    except Exception as error:
        result.update(probe_completed=False, actual_error=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        original.subprocess.Popen = popen
        if client is not None:
            client.close()
            result['original_native_solve_calls'] = client.calls
            result['worker_exit_code'] = client.proc.poll()
        if previous_env is None:
            os.environ.pop(ENVIRONMENT, None)
        else:
            os.environ[ENVIRONMENT] = previous_env
        result['elapsed_seconds'] = time.monotonic() - started
        write(output / 'result.json', result)
    return code


if __name__ == '__main__':
    raise SystemExit(main())

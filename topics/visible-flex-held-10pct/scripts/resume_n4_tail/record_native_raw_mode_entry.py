#!/usr/bin/env python3
"""Read one started mode-continuation entry and its first complete native batch.

No model, flow, Jacobian or solve is invoked. An immutable prefix of the
observed logs is retained; the surrounding original solve may continue.
M20 evidence is not relabeled as M24 evidence, and q/controls remain free.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct
import sys


def ref(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def verify(item):
    if ref(item['path'])['sha256']!=item['sha256']:
        raise ValueError('Bound source or saved output changed: '+item['path'])


def load(path):
    path=Path(path)
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)


def save(path,value):
    with Path(path).open('x') as stream:
        json.dump(value,stream,indent=2,ensure_ascii=False,allow_nan=False)
        stream.write('\n')
    return ref(path)


def snapshot(path,lines):
    with Path(path).open('xb') as stream:
        stream.write(b''.join(lines))
    return ref(path)


def number_hash(values):
    return hashlib.sha256(struct.pack('<'+'d'*len(values),*values)).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-directory',type=Path,required=True)
    parser.add_argument('--preparation',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    base=args.run_directory.resolve()
    plan_path=base/'observed-plan.json'
    plan=load(plan_path)
    prep=load(args.preparation)
    if prep['preparation_child_returncode']!=0 or prep['observed_plan']!=ref(plan_path):
        raise ValueError('Source/metadata preparation did not genuinely complete')
    for item in [*plan['files'].values(),*plan['input_coefficient_chunks'],*plan['prefix_sources']]:
        verify(item)
    for key in ('source','previous_manifest','new_manifest','input_checkpoint','input_summary',
                'actual_tail','audit_schema_view','original_arguments',
                'preparation_child_stdout','preparation_child_stderr'):
        verify(prep[key])
    original=Path(plan['files']['original_driver']['path']).read_text()
    restored=Path(plan['files']['derived_driver']['path']).read_text()
    for patch in reversed(plan['recording_insertions']):
        text=patch['marker']+patch['added']
        if restored.count(text)!=1:
            raise ValueError('Recording-only patch changed')
        restored=restored.replace(text,patch['marker'])
    if restored!=original or len(plan['recording_insertions'])!=3:
        raise ValueError('Derived main is not the declared three recording insertions')
    manifest=load(plan['files']['manifest']['path'])
    previous=load(prep['previous_manifest']['path'])
    expected={**previous['fixed_scope'],'M':24}
    if (plan['source_modes'],plan['target_modes'])!=(20,24) or manifest['fixed_scope']!=expected:
        raise ValueError('Expected this explicit M20-to-M24 entry')
    for key in ('owned_sources','native_files','runtime_libraries','execution_provider'):
        if manifest[key]!=previous[key]:
            raise ValueError('The unchanged numerical source/runtime/provider differs')
    for item in [*manifest['owned_sources'],*manifest['native_files'].values(),*manifest['runtime_libraries']]:
        verify(item)
    for key in ('wrapper','python','plan','equivalence_record'):
        verify(manifest['execution_provider'][key])
    returned_lines=(base/'returned-data-events.jsonl').read_bytes().splitlines(keepends=True)
    returned=[json.loads(line) for line in returned_lines]
    seed_index,seed=next((i,row) for i,row in enumerate(returned)
                         if row['event']=='original_complete_seed_returned')
    if seed['modes']!=24 or seed['original_input_nodes']!=2282 or seed['seed_nodes']!=2282:
        raise ValueError('The actual complete nested seed differs')
    trace_lines=(base/'seed-worker-trace.jsonl').read_bytes().splitlines(keepends=True)
    trace=[json.loads(line) for line in trace_lines]
    warm=next(row for row in trace if row['event']=='warm_initial_state')
    request_index,request=next((i,row) for i,row in enumerate(trace)
                               if row['event']=='request' and row['call']==1)
    if (warm['sourceModes'],warm['targetModes'],warm['depth'])!=(20,24,8):
        raise ValueError('The original nested tail initialization differs')
    if Path(warm['source']).resolve()!=Path(plan['files']['input_tail']['path']).resolve():
        raise ValueError('The actual tail initializer has another source')
    if len(request['height'])!=24 or request['jacobian'] or not request['audit']:
        raise ValueError('The original complete-H warmup request differs')
    native_lines=(base/'native-evaluates/events.jsonl').read_bytes().splitlines(keepends=True)
    native=[json.loads(line) for line in native_lines]
    terminal_index,terminal=next((i,row) for i,row in enumerate(native)
                                 if row['event']=='batch_terminal' and row['call']==1)
    verify(terminal['record'])
    batch=load(terminal['record']['path'])
    if batch['status']!='complete' or batch['returncode']!=0 or not batch['withJac']:
        raise ValueError('The first actual complete native batch has not succeeded')
    for key in ('input','output','stdout','stderr','manifest','static_metadata','parallel_record'):
        verify(batch[key])
    if batch['manifest']!=plan['files']['manifest']:
        raise ValueError('The new native source scope is not the declared one')
    meta=load(batch['static_metadata']['path'])
    if meta['scope']!=expected:
        raise ValueError('The actual runtime engine scope differs')
    verify(meta['template'])
    parallel=load(batch['parallel_record']['path'])
    if not parallel['success'] or parallel['parent_returncode']!=0 or len(parallel['records'])!=4:
        raise ValueError('The unchanged four-process provider did not succeed')
    for child in parallel['records']:
        if child['returncode']!=0:
            raise ValueError('An unchanged original CLI child failed')
        for key in ('input','output','stdout','stderr'):
            verify(child[key])
    incoming=Path(batch['input']['path']).read_bytes()
    outgoing=Path(batch['output']['path']).read_bytes()
    if incoming[:8]!=b'VFN4LD01' or outgoing[:8]!=b'VFN4OUT1':
        raise ValueError('Wrong current complete native wire')
    header=struct.unpack_from('<9i',incoming,8)
    if header!=(1,24,512,4,128,30,20,2304,1):
        raise ValueError('The actual M24 complete wire dimensions differ')
    if struct.unpack_from('<4i',outgoing,8)!=(1,24,2304,1):
        raise ValueError('The actual M24 complete output dimensions differ')
    token=hashlib.sha256(incoming[:44]+incoming[108:]).hexdigest()
    if incoming[44:108].decode()!=token or outgoing[24:88].decode()!=token:
        raise ValueError('Payload/source identity was confused or payload changed')
    if len(incoming)!=meta['counts']['inputBytes'] or len(outgoing)!=meta['counts']['fullJacOutputBytes']:
        raise ValueError('Actual complete wire byte counts differ')
    config=load(base/'seed-config.json')
    if (config['modes'],config['spacing'],config['quadrature'],config['steps'],
            config['shootingParts'],config['solveTolerance'])!=(24,4,512,16,32,2e-9):
        raise ValueError('The original finite solver gates changed')
    immutable=dict(
        seed_events=snapshot(base/'entry-returned-events-prefix.jsonl',returned_lines[:seed_index+1]),
        worker_trace=snapshot(base/'entry-worker-trace-prefix.jsonl',trace_lines[:request_index+1]),
        native_events=snapshot(base/'entry-native-events-prefix.jsonl',native_lines[:terminal_index+1]))
    result=dict(scope=__doc__,source=ref(__file__),command=sys.argv,
        plan=ref(plan_path),preparation=ref(args.preparation),execution_source_files=plan['files'],
        unchanged_prefix_source_count=len(plan['prefix_sources']),immutable_execution_prefixes=immutable,
        actual_config=ref(base/'seed-config.json'),actual_runtime_scope=meta['scope'],
        input_coefficient_chunks=plan['input_coefficient_chunks'],
        physical_profile=plan['physical_profile'],core_settings=plan['core_settings'],
        raw_control_anchor_modes=plan['raw_control_anchor_modes'],free_c8=True,
        source_core_controls=19,target_core_controls=23,gauge_amplitude=plan['gauge_amplitude'],
        input_displayed_actual_q=plan['input_actual_q'],parameter_rebuilt_initial_q=seed['original_q'],
        q_and_all_controls_remain_solver_unknowns=True,
        not_README_item5_fixed_all_parameters_certification=True,
        core_jet_identity_sampling=1024,complete_material_core_jet_sample_errors=seed['complete_core_identity_error'],
        complete_map_projection_error=seed['complete_map_projection_error'],preserved_input_mesh_nodes=2282,
        original_nested_tail_initialization=warm,complete_initial_H_components=24,
        complete_initial_H_sha256=number_hash(request['height']),first_height=request['height'][0],
        second_height=request['height'][1],
        first_complete_native_record=terminal['record'],first_complete_native_input=batch['input'],
        first_complete_native_output=batch['output'],static_metadata=batch['static_metadata'],
        actual_grid_and_wire_counts=meta['counts'],actual_first_fullJac_state_scalars=2304*50,
        actual_first_fullJac_tangent_scalars=2304*50*48,
        first_native_process_seconds=batch['processSeconds'] if 'processSeconds'in batch else terminal['processSeconds'],
        first_parallel_record=batch['parallel_record'],unchanged_CLI_child_successes=4,
        observer_session=27744,whole_program_terminal_claimed=False,
        actual_tail_or_prefix_acceptance_claimed=False,
        old_M20_three_fixture_validation_is_not_new_M24_validation=True,
        raw_inner_and_completed_prefix_audit_saves_installed=True,
        no_new_mathematical_evaluation_by_collector=True)
    if len(json.dumps(result,indent=2).encode())>=100000:
        raise ValueError('Compact entry record must stay below100KB')
    output=save(args.out,result)
    print(json.dumps(dict(record=output,first_M24_complete_native_batch=True,read_only=True)),flush=True)


if __name__=='__main__':
    main()

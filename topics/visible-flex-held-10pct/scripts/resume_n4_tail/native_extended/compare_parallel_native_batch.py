#!/usr/bin/env python3
"""Read-only full-wire identity check of one completed parallel native batch.

Check every original input stage and all state/Jacobian/root/geometry output
bytes. Only each stage's actual kernel_seconds field is excluded from the
numerical identity digest; no numerical evaluator or native worker is called.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import sys
from parallel_native_batch import reference, split_wire, output_records


def check_reference(ref):
    p = Path(ref['path'])
    if hashlib.sha256(p.read_bytes()).hexdigest() != ref['sha256']:
        raise ValueError('Bound file changed: '+str(p))
    return p


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan', type=Path, required=True)
    ap.add_argument('--original-terminal', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--tool-session', type=int, required=True)
    ap.add_argument('--tool-launch', required=True)
    ap.add_argument('--tool-terminal', required=True)
    a = ap.parse_args()
    plan = json.loads(a.plan.read_text())
    for key in ('source', 'native_cli', 'original_build', 'original_input', 'baseline_output'):
        check_reference(plan[key])
    data = check_reference(plan['original_input']).read_bytes()
    shape = split_wire(data)
    result_path = Path(plan['output'])
    meta_path = Path(str(result_path)+'.parallel.json')
    meta = json.loads(meta_path.read_text())
    if (meta['source'] != reference(plan['source']['path']) or meta['plan'] != reference(a.plan) or
        meta['original_input'] != reference(plan['original_input']['path']) or
        not meta['success'] or meta['parent_returncode'] != 0 or
        len(meta['records']) != meta['workers']):
        raise ValueError('No completed successful bound parallel execution')
    check_reference(meta['complete_output'])
    original_header_numeric = shape['header'][:36]+shape['header'][40:44]+shape['header'][108:]
    checked = 0
    for rec in meta['records']:
        child = rec['child']
        if rec['returncode'] != 0:
            raise ValueError('A child did not complete successfully')
        chunk = check_reference(rec['input']).read_bytes()
        child_shape = split_wire(chunk)
        child_header_numeric = child_shape['header'][:36]+child_shape['header'][40:44]+child_shape['header'][108:]
        if child_header_numeric != original_header_numeric:
            raise ValueError('A numeric common configuration byte changed')
        for local, (start,end) in enumerate(child_shape['spans']):
            global_stage = local*meta['workers']+child
            left,right = shape['spans'][global_stage]
            if chunk[start:end] != data[left:right]:
                raise ValueError('An input state/coefficient/grid byte changed')
            checked += 1
    if checked != shape['count']:
        raise ValueError('Not every original input stage was checked')
    before = check_reference(plan['baseline_output']).read_bytes()
    after = result_path.read_bytes()
    blocks0, failed0 = output_records(before,shape,shape['count'],shape['token'],0)
    blocks1, failed1 = output_records(after,shape,shape['count'],shape['token'],0)
    if failed0 is not None or failed1 is not None or before[:88] != after[:88]:
        raise ValueError('The original output order/header/status changed')
    hashes = [hashlib.sha256(before[:88]),hashlib.sha256(after[:88])]
    timing_sums = [0.,0.]
    for (l0,r0,s0),(l1,r1,s1) in zip(blocks0,blocks1):
        if s0 or s1 or r0-l0 != r1-l1 or before[l0:r0-8] != after[l1:r1-8]:
            raise ValueError('A state/Jacobian/root/geometry byte differs')
        hashes[0].update(before[l0:r0-8]);hashes[1].update(after[l1:r1-8])
        timing_sums[0] += struct.unpack_from('<d',before,r0-8)[0]
        timing_sums[1] += struct.unpack_from('<d',after,r1-8)[0]
    if hashes[0].hexdigest() != hashes[1].hexdigest():
        raise AssertionError('Numerical digests differ')
    old_text = a.original_terminal.read_text()
    old = json.loads(old_text)
    if any(plan[k]['sha256'] not in old_text for k in ('original_input','baseline_output')):
        raise ValueError('The earlier serial terminal does not bind this input/output pair')
    # This source-bound record supplies the earlier serial process wall time.
    def find_key(value,key):
        if isinstance(value,dict):
            if key in value: return value[key]
            for part in value.values():
                found=find_key(part,key)
                if found is not None:return found
        elif isinstance(value,list):
            for part in value:
                found=find_key(part,key)
                if found is not None:return found
        return None
    serial_seconds = find_key(old,'process_wall_seconds')
    if serial_seconds is None:
        raise ValueError('Original serial elapsed time was not recorded')
    out = dict(scope=__doc__, command=[sys.executable,*sys.argv], collector=reference(__file__),
        plan=reference(a.plan), wrapper=plan['source'], original_cli=plan['native_cli'],
        original_build=plan['original_build'], input=plan['original_input'],
        original_output=plan['baseline_output'], parallel_output=reference(result_path),
        parallel_execution=reference(meta_path), original_terminal=reference(a.original_terminal),
        observer=dict(session=a.tool_session,launch_chunk=a.tool_launch,terminal_chunk=a.tool_terminal,
                      tool_returncode=0,scope='Actual tool completion was observed separately; supplied identifiers bind that observation.'),
        original_stage_bodies_bitwise_equal=True, common_numeric_header_bitwise_equal=True,
        all_original_numeric_output_bitwise_equal=True,
        numerical_wire_sha256=hashes[0].hexdigest(),
        excluded_fields='Exactly the last8-byte kernel_seconds float in each successful stage record',
        stages=shape['count'], modes=shape['modes'], workers=meta['workers'],
        state_scalars=shape['count']*(2*shape['modes']+2),
        Jacobian_scalars=shape['count']*(2*shape['modes']+2)*2*shape['modes'],
        root_count_and_geometry_scalars=shape['count']*7,
        actual_child_returncodes=[rec['returncode'] for rec in meta['records']],
        wrapper_returncode=meta['parent_returncode'],
        serial_process_seconds=serial_seconds,
        parallel_wrapper_seconds=meta['elapsed_seconds'],
        observed_wall_ratio=serial_seconds/meta['elapsed_seconds'],
        timing_scope='Different actual execution times/loads. The parallel measure includes splitting/merge. This one-run ratio is not a universal speed claim.',
        serial_kernel_seconds_sum=timing_sums[0], parallel_kernel_seconds_sum=timing_sums[1],
        collector_invoked_new_equations=False, new_DN_solver_invoked=False,
        mathematical_scope='Same previously rejected fixed-state residual. No new H, accepted tail, metric or coupled prefix is established.')
    with a.out.open('x') as f:
        json.dump(out,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(record=reference(a.out),numeric_byte_identity=True,
        stages=shape['count'],parallel_seconds=meta['elapsed_seconds'],wall_ratio=out['observed_wall_ratio'])))


if __name__ == '__main__':
    main()

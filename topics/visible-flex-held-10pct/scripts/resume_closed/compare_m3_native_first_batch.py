#!/usr/bin/env python3
"""Compare preserved native wires with preserved independent n3 fixtures.

Read and serialize data only: never import a model, run a native library,
evaluate a flow, solve a root, or repeat an accepted tail. The three fixture
outputs use floor .1; the actual first full batch uses the original floor
.05. Equality of their saved binary64 outputs does not assert equality of
unrecorded extended-precision internal trajectories or of all other stages.
"""
import argparse
import datetime
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys


def digest(data):
    return hashlib.sha256(data).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=digest(path.read_bytes()))


def load(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def checked(path, expected):
    item = ref(path)
    if item['sha256'] != expected:
        raise ValueError('A preserved input changed: '+str(path))
    return item


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    w = args.workspace.resolve()
    batch = w/'m3_work/trace-path-lam064-native-literal-v3/native-provider-runs'
    fixtures = w/'m3_work/native-literal-baseline-v1'
    topic = w/'math-research-public/topics/visible-flex-held-10pct'
    paths = {
        'input': (batch/'0001-jac-input.bin', 'aa63eaaaa080b2c195f4d3331e6e462ab9aeb9eda74bbb7622b60e8d9f10589c'),
        'output': (batch/'0001-jac-output.bin', 'c699ebd03472c8be0a276533470863eee3b957948110949137bfa95a6bda8e6c'),
        'coefficients': (fixtures/'capsule-coefficients.json.gz', '739f2c6f79dacbaf2e9612eae34898a3f9cc762940384ccb51e45a32af241769'),
        'fixture_outputs': (fixtures/'native-check/raw.json.gz', '3d5d664bd05bbaf9ef0db8a9398b17c02a213badc7610060a6bcf9e1fde2663e'),
        'original_failed_tail': (w/'m3_work/trace-path-lam064-coupled-v1/seed_tail_0001.json.gz', '753aa9ec4584f0bafa216acbfaffe98fab44a0369e914ca06c7c739d81b365c4'),
        'ABI_helper': (topic/'scripts/resume_n4_tail/native_extended/probe_native_frozen_flow.py', '42893f210b6d31c59abd04cdfec415a2408a543f726f87d808fc99cf8fad45db'),
        'provider_manifest': (w/'m3_work/native-literal-adapter-v3/manifest.json', 'abb2a44fd55d91af60f9f86834ec70e5d40ec73fd8f412eec5ecaaba6bd300be')
    }
    references = {key: checked(*value) for key, value in paths.items()}
    record_path = batch/'0001-jac-record.json'
    record = load(record_path)
    for key in ('input', 'output', 'manifest'):
        name = 'provider_manifest' if key == 'manifest' else key
        if record[key] != references[name]:
            raise ValueError('The actual first-batch record differs: '+key)
    if record['call'] != 1 or record['withJac'] is not True or record['returncode'] != 0:
        raise ValueError('Require the completed original first full-Jacobian batch')
    references['actual_first_batch'] = ref(record_path)
    parallel = load(record['parallel_record']['path'])
    checked(record['parallel_record']['path'], record['parallel_record']['sha256'])
    if parallel['parent_returncode'] != 0 or any(row['returncode'] != 0 for row in parallel['records']):
        raise ValueError('The actual parallel batch did not complete successfully')
    references['parallel_record'] = record['parallel_record']
    capsule = load(paths['coefficients'][0])
    previous = load(paths['fixture_outputs'][0])
    failed = load(paths['original_failed_tail'][0])
    spec = importlib.util.spec_from_file_location('frozen_wire_helper', paths['ABI_helper'][0])
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    # Only helper.fixture_payload is called: it serializes already-saved data.
    data = paths['input'][0].read_bytes()
    if data[:8] != b'VFN4LD01':
        raise ValueError('Unexpected input magic')
    header = struct.unpack_from('<9i', data, 8)
    if header != (1, 8, 128, 3, 128, 30, 20, 1152, 1):
        raise ValueError('Unexpected literal n3/M8 batch dimensions')
    M, nq, nh, stages = header[1], header[4], header[6], header[7]
    if data[44:108].decode() != record['payload_token']:
        raise ValueError('Input token differs from the preserved record')
    rules = capsule['root_rules']
    if rules['floor'] != .1 or data[108:140] != packed([.05, rules['tolerance'], rules['fallback_tolerance'], rules['scale_floor']]):
        raise ValueError('The original .05 and fixture .1 scopes differ unexpectedly')
    shared = packed(rules['halving_factors'])
    for kind in ('state_cos', 'state_sin'):
        shared += packed([v for row in capsule['trig'][kind] for v in row])
    offset = 140 + 8*(nh+nq*(2*M+1))
    if data[140:offset] != shared:
        raise ValueError('Actual halving factors or literal trig table differ from the independent fixture')
    wanted = {fixture['stage']: fixture for fixture in capsule['fixtures']}
    if set(wanted) != {86, 87, 88}:
        raise ValueError('Only the three already-recorded fixtures are supported')
    matching_payloads = {}
    for stage in range(stages):
        begin = offset
        steps, points = struct.unpack_from('<2i', data, offset)
        offset += 8
        initial = data[offset:offset+8*(2*M+2)]
        expected_initial = packed(failed['response']['checkpoint']['states'][stage+1]+[0., 0.])
        if initial != expected_initial:
            raise ValueError('Actual first-batch state differs from the original unmodified initializer: '+str(stage))
        offset += 8*(2*M+2) + 8*points*(12+M) + 36*steps
        if offset > len(data):
            raise ValueError('Truncated stage data')
        if stage in wanted:
            fixture = helper.fixture_payload(capsule, wanted[stage])
            expected = struct.pack('<2i', len(fixture['steps']), len(fixture['points'])) + packed(fixture['initial'])
            expected += packed([v for row in fixture['points'] for v in row])
            for row in fixture['steps']:
                expected += struct.pack('<5i2d', *row)
            actual = data[begin:offset]
            matching_payloads[stage] = dict(stage=stage, input_body_equal=actual == expected,
                actual_input_body_sha256=digest(actual), fixture_input_body_sha256=digest(expected),
                literal_steps=steps, unique_coefficient_points=points)
    if offset != len(data):
        raise ValueError('Unexpected input trailing bytes')
    output = paths['output'][0].read_bytes()
    if (output[:8] != b'VFN4OUT1' or struct.unpack_from('<4i', output, 8) != (1, M, stages, 1) or
            output[24:88] != data[44:108]):
        raise ValueError('Output header/token does not bind the input')
    size = 8+8*(2*M+2)+8*(2*M+2)*2*M+64
    if len(output) != 88+stages*size:
        raise ValueError('Incomplete successful output')
    old_rows = {row['stage']: row for row in previous['rows']}
    rows = []
    for stage in range(stages):
        begin = 88+stage*size
        if struct.unpack_from('<2i', output, begin) != (stage, 0):
            raise ValueError('Original output stage order or status differs')
        if stage in wanted:
            start = begin+8
            middle = start+8*(2*M+2)
            end = middle+8*(2*M+2)*2*M
            state, tangent = output[start:middle], output[middle:end]
            old_state, old_tangent = packed(old_rows[stage]['LD_state']), packed(old_rows[stage]['LD_tangent'])
            row = matching_payloads[stage]
            row.update(binary64_state_equal=state == old_state, binary64_tangent_equal=tangent == old_tangent,
                state_sha256=digest(state), fixture_state_sha256=digest(old_state),
                tangent_sha256=digest(tangent), fixture_tangent_sha256=digest(old_tangent),
                state_values=2*M+2, tangent_values=(2*M+2)*2*M)
            rows.append(row)
    result = dict(schema='m3-preserved-first-native-batch-comparison-v1', scope=__doc__,
        source=ref(__file__), command=[sys.executable, *sys.argv],
        observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), references=references,
        actual_floor=.05, independent_fixture_floor=.1,
        unchanged_original_initial_stage_count=stages, original_physical_state_values=stages*2*M,
        original_zero_auxiliary_values=stages*2, shared_halving_and_trig_bytes_equal=True,
        first_batch_state_values=stages*(2*M+2), first_batch_tangent_values=stages*(2*M+2)*2*M,
        all_output_stage_indices_and_statuses_valid=True, comparisons=rows,
        all_three_inputs_equal=all(row['input_body_equal'] for row in rows),
        all_three_binary64_outputs_equal=all(row['binary64_state_equal'] and row['binary64_tangent_equal'] for row in rows),
        new_flow_evaluations=0, new_DN_calls=0, new_root_calls=0,
        internal_native80_trajectory_equality_claimed=False,
        continuous_or_all_stage_floor_equivalence_claimed=False)
    with args.out.open('x') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.out), inputs_equal=result['all_three_inputs_equal'],
        outputs_equal=result['all_three_binary64_outputs_equal'], preserved_initial_stages=stages,
        new_flow_evaluations=0)), flush=True)


if __name__ == '__main__':
    main()

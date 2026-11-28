#!/usr/bin/env python3
"""Read actual state-only line-search records without another native solve.

The wire input retains nodes 1..S, not node 0. This script therefore reports
the maximum over every available interior component and all deep boundary
components as a LOWER BOUND for the original discrete merit. It never invents
the unrecorded node-0 contribution or a worker test.norm value. A bound above
the actual base merit is sufficient to establish rejection of that trial.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct

import numpy as np


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if data[:2] == b'\x1f\x8b' else data)


def inspect(attempt, first_call, count, base_merit):
    attempt = Path(attempt).resolve()
    scales_path = attempt/'predictor/original-tangent-scales.json'
    background = read(scales_path)
    M, S = background['M'], background['depth']; K = 2*M
    # Exported predictor scales refer to the predecessor height. Recompute the
    # original recurrence for the actual desired full height instead.
    scales = np.empty(S+1)
    scales[0] = max(1e-250, *map(abs, background['desiredTarget']))
    for n in range(S):
        scales[n+1] = float(scales[n])/abs(background['gains0'][n])
    deep = np.asarray(background['deepGraph'], float)
    answer = dict(scope=__doc__, source=ref(__file__), original_scales_metadata=ref(scales_path),
        actual_base_merit=base_merit, first_native_call=first_call,
        original_backtrack_count=count, modes=M, stages=S, rows=[],
        node0_not_in_native_input=True, full_global_merit_claimed=False,
        new_native_calculation_performed=False)
    for k in range(count):
        call, alpha = first_call+k, 2.**(-k)
        path = attempt/'native-runs'/f'{call:04d}-state-record.json'
        row = dict(backtrack=k, alpha=alpha, native_call=call,
                   actual_record_returned=path.exists())
        if not path.exists():
            answer['rows'].append(row)
            continue
        record = read(path)
        row.update(native_record=ref(path), status=record.get('status'),
                   process_wall_seconds=record.get('process_wall_seconds'))
        if record.get('status') != 'complete' or record.get('withJac') is not False:
            row['complete_residual_lower_bound_available'] = False
            answer['rows'].append(row)
            continue
        for key in ('input', 'output', 'static_metadata', 'manifest'):
            if ref(record[key]['path']) != record[key]:
                raise ValueError('Changed actual native evidence '+key)
        metadata = read(record['static_metadata']['path'])
        if len(metadata['stages']) != S or record['returned_flow_count'] != S:
            raise ValueError('An original trial omits finite stages')
        wire = Path(record['input']['path']).read_bytes()
        states = np.empty((S+1, K)); states[0] = np.nan
        for native_row in metadata['stages']:
            n = native_row['stage']
            states[n+1] = np.frombuffer(wire, dtype='<f8', count=K,
                                        offset=native_row['initialOffset'])
        output = Path(record['output']['path']).read_bytes()
        header = b'VFN4OUT1'+struct.pack('<4i', 1, M, S, 0)+record['payload_token'].encode('ascii')
        if output[:88] != header:
            raise ValueError('The complete actual state-only wire identity differs')
        offset = 88; largest, location = 0., None
        for n in range(S):
            index, status = struct.unpack_from('<2i', output, offset); offset += 8
            if index != n or status != 0:
                raise ValueError('Original native stage missing or unsuccessful')
            state = np.frombuffer(output, dtype='<f8', count=K+2, offset=offset).copy()
            offset += 8*(K+2)+64
            state[M:K] /= background['portRatios'][n]
            if n == 0:
                continue
            residual = state[:K]-states[n]
            normalized = np.abs(residual)/scales[n]
            j = int(np.argmax(normalized)); value = float(normalized[j])
            if value > largest:
                largest = value
                location = dict(kind='interior', stage=n, component=j,
                    variable='Q' if j < M else 'Pi', harmonic=3*(j % M+1),
                    signed_absolute_residual=float(residual[j]),
                    original_scale=float(scales[n]), state=float(states[n,j]))
        if offset != len(output):
            raise ValueError('The state-only native byte extent differs')
        residual = states[-1,M:]-deep*states[-1,:M]
        normalized = np.abs(residual)/scales[-1]
        j = int(np.argmax(normalized)); value = float(normalized[j])
        if value > largest:
            largest = value
            location = dict(kind='deep_boundary', stage=S, component=j,
                harmonic=3*(j+1), signed_absolute_residual=float(residual[j]),
                original_scale=float(scales[-1]))
        row.update(complete_residual_lower_bound_available=True,
            original_discrete_merit_lower_bound=largest, maximizing_available_component=location,
            lower_bound_alone_rules_out_original_merit_decrease=largest >= base_merit,
            native_input=record['input'], native_output=record['output'])
        answer['rows'].append(row)
    answer['all_requested_native_records_returned'] = all(r['actual_record_returned'] for r in answer['rows'])
    return answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--attempt', type=Path, required=True)
    parser.add_argument('--first-call', type=int, required=True)
    parser.add_argument('--count', type=int, default=10)
    parser.add_argument('--base-merit', type=float, required=True)
    parser.add_argument('--out', type=Path, required=True)
    a = parser.parse_args()
    result = inspect(a.attempt, a.first_call, a.count, a.base_merit)
    with a.out.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(output=ref(a.out), rows=[{
        key:row.get(key) for key in ('alpha','native_call','actual_record_returned','process_wall_seconds',
        'original_discrete_merit_lower_bound','lower_bound_alone_rules_out_original_merit_decrease')}
        for row in result['rows']]), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()

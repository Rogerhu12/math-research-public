#!/usr/bin/env python3
"""Persistent public-Actions worker for original-coordinate RK4 map formation.

Read four complete saved binary64 local matrices from each pipe request. Use
the unchanged direct_rk function exercised in actual50, keep all226 rows and
224 columns, apply the one original exit Pi port, then cast exactly once.
No native RHS, root, ODE, node state, residual, solve or acceptance is run here.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import struct
import sys
import time
import traceback

M, K, SIZE = 112, 224, 226
LOCAL_BYTES = SIZE * K * 8
FROZEN_NAME = 'geometry_20261114_saved_stage_rk_covariance.py'
FROZEN_SHA = '01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548'
SCHEMA = 'native-rawcell0-direct-longdouble-pipe-v1'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def need(value, message):
    if not value:
        raise ValueError(message)


def send(value):
    payload = (json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()
    sys.stdout.buffer.write(payload)
    sys.stdout.buffer.flush()


def read_exact(stream, size):
    blocks = []
    left = size
    while left:
        block = stream.read(left)
        if not block:
            raise EOFError('Incomplete original local-A pipe payload')
        blocks.append(block)
        left -= len(block)
    return b''.join(blocks)


def f64_record(record):
    raw = bytes.fromhex(record['float64le_hex'])
    need(len(raw) == 8, 'Complete binary64 numberRecord required')
    bits = int.from_bytes(raw, 'little')
    need(((bits >> 52) & 2047) != 2047, 'Finite original h/port required')
    value = struct.unpack('<d', raw)[0]
    need(record['value'] == value, 'NumberRecord numeric value and original bits disagree')
    return raw


def load_frozen():
    file = Path(__file__).resolve().with_name(FROZEN_NAME)
    raw = file.read_bytes()
    need(digest(raw) == FROZEN_SHA, 'Do not alter actual50 direct RK arithmetic')
    spec = importlib.util.spec_from_file_location('_actual50_frozen_direct_rk', file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class OmittedWorkingFiles:
    """The frozen numerical routine is unchanged; debug writes are observers."""
    def save(self, name, values, role, binary64=False):
        return {'name': name, 'working_debug_array_not_persisted': True}


def write_binary(directory, relative, raw, shape):
    rel = Path(relative)
    need(not rel.is_absolute() and '..' not in rel.parts and rel.parts[0] == 'large-arrays',
         'New complete arrays belong only to this independent artifact directory')
    file = directory / rel
    file.parent.mkdir(parents=True, exist_ok=True)
    with file.open('xb') as stream:
        stream.write(raw)
    return dict(file=relative, bytes=len(raw), sha256=digest(raw), raw_sha256=digest(raw),
                dtype='<f8', order='C', shape=shape)


def main():
    need(os.environ.get('GITHUB_ACTIONS') == 'true' and
         os.environ.get('GITHUB_REPOSITORY', '').lower() == 'rogerhu12/math-research-public',
         'Scientific formation is restricted to this public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--spec', type=Path, required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    spec_raw = args.spec.read_bytes()
    spec = json.loads(spec_raw)
    source_sha = digest(Path(__file__).read_bytes())
    need(spec['worker_source_sha256'] == source_sha and Path(spec['output']).resolve() == out,
         'Bind the actual worker source and independent output directory')
    need(spec['direct_arithmetic_source_sha256'] == FROZEN_SHA,
         'Use actual50 unchanged direct arithmetic')
    need(out.is_dir() and (out/'large-arrays').is_dir(), 'Native parent creates the independent output')
    import numpy as np
    frozen = load_frozen()
    working = frozen.working_format(np)
    runtime = dict(python=sys.version, numpy=np.__version__, platform=platform.platform(),
                   machine=platform.machine(), byteorder=sys.byteorder, working_precision=working,
                   public_run=os.environ.get('GITHUB_RUN_ID'),
                   public_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'))
    started = time.monotonic()
    send(dict(schema=SCHEMA, event='ready', source_sha256=source_sha,
              direct_arithmetic_source_sha256=FROZEN_SHA, spec_sha256=digest(spec_raw), runtime=runtime,
              native_RHS_calls=0, local_J_calls=0, new_ODE_steps=0,
              all_local_A_received_as_original_binary64=True, node_residuals_not_computed=True))
    completed = 0
    sequence = 0
    last_stage = -1
    last_step = -1
    while True:
        line = sys.stdin.buffer.readline(65537)
        if not line:
            raise EOFError('The parent must explicitly finish every intended step')
        need(len(line) <= 65536 and line.endswith(b'\n'), 'Bounded complete pipe header required')
        header = json.loads(line)
        if header.get('op') == 'finish':
            need(header['completed_steps'] == completed and completed > 0,
                 'Finish only after the complete acknowledged step inventory')
            send(dict(schema=SCHEMA, event='finished', completed_steps=completed,
                      source_sha256=source_sha, spec_sha256=digest(spec_raw),
                      elapsed_seconds=time.monotonic()-started,
                      maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      all_local_A_payloads_released_between_steps=True,
                      working_debug_arrays_not_persisted=True,
                      final_target_is_once_cast_original_coordinate_binary64=True,
                      native_accepted=False))
            return 0
        raws = []
        try:
            need(header.get('op') == 'step' and header['sequence'] == sequence,
                 'Process each original step once in its declared order')
            stage, step = header['stage'], header['original_step']
            need(type(stage) is int and 0 <= stage < 72 and type(step) is int and step >= 0,
                 'Original rawCell0 stage/step indices required')
            need((stage == last_stage and step == last_step+1) or
                 (stage == last_stage+1 and step == 0), 'Keep actual41 stage then inner-to-outer step order')
            need(header['payload_bytes'] == 4*LOCAL_BYTES and len(header['local_A']) == 4,
                 'Retain four complete226 by224 local matrices')
            h_bytes, port_bytes = f64_record(header['h']), f64_record(header['port_ratio'])
            h = np.longdouble(np.frombuffer(h_bytes, dtype='<f8')[0])
            port = np.longdouble(np.frombuffer(port_bytes, dtype='<f8')[0])
            need(bool(np.isfinite(h)) and h != 0 and bool(np.isfinite(port)) and port != 0,
                 'Original nonzero finite h and Pi port required')
            need(header['final_original_step'] is True or port_bytes == struct.pack('<d', 1.0),
                 'Only an original stage exit may apply a non-unit port')
            A = []
            for index, descriptor in enumerate(header['local_A']):
                need(descriptor['field_index'] == index and descriptor['shape'] == [SIZE, K] and
                     descriptor['dtype'] == '<f8' and descriptor['bytes'] == LOCAL_BYTES,
                     'Every actual original full local Jacobian is required')
                raw = read_exact(sys.stdin.buffer, LOCAL_BYTES)
                raws.append(raw)
                need(digest(raw) == descriptor['sha256'], 'Original local-A pipe bytes changed')
                values = np.frombuffer(raw, dtype='<f8').reshape(SIZE, K)
                need(bool(np.all(np.isfinite(values))), 'Nonfinite original local-A input')
                A.append(values.astype(np.longdouble))
            step_started = time.monotonic()
            value, _work = frozen.direct_rk(np, A, h, port, OmittedWorkingFiles())
            output = np.asarray(value, dtype='<f8', order='C')
            need(output.shape == (SIZE, K) and bool(np.all(np.isfinite(output))),
                 'Cannot export a nonfinite complete original-coordinate target block')
            full_raw = output.tobytes(order='C')
            shape_raw, mean_raw = full_raw[:K*K*8], full_raw[K*K*8:]
            prefix = f'large-arrays/stage-{stage:03d}-'
            shape_desc = write_binary(out, prefix+f'shape-jacobians-{step:06d}.f64le',
                                      shape_raw, [1, K, K])
            mean_desc = write_binary(out, prefix+f'mean-jacobians-{step:06d}.f64le',
                                     mean_raw, [1, 2, K])
            report = dict(schema=SCHEMA, event='step-completed', sequence=sequence, stage=stage,
                original_step=step, source_sha256=source_sha, direct_arithmetic_source_sha256=FROZEN_SHA,
                full_original_output_sha256=digest(full_raw), full_original_output_bytes=len(full_raw),
                arrays=dict(shape_jacobians=shape_desc, mean_jacobians=mean_desc),
                local_A=header['local_A'], original_h=header['h'], original_port_ratio=header['port_ratio'],
                full_input_sha256=header['full_input_sha256'],
                actual41_field_record_sha256=header['actual41_field_record_sha256'],
                once_cast_to_binary64=True, original_Pi_port_paid_once=True,
                two_mean_rows_retained=True, mean_feedback_into_shape=False,
                working_nonzero_to_binary64_zero_entries=int(np.count_nonzero((value != 0) & (output == 0))),
                output_negative_zero_entries=int(np.count_nonzero((output == 0) & np.signbit(output))),
                working_local_A_not_persisted=True,
                same_unchanged_actual50_direct_rk_function=True,
                elapsed_seconds=time.monotonic()-step_started)
            send(report)
            completed += 1
            sequence += 1
            last_stage, last_step = stage, step
            del A, value, output, raws, full_raw, shape_raw, mean_raw, _work
        except Exception as error:
            artifacts = []
            for index, raw in enumerate(raws):
                artifacts.append(write_binary(out, f'large-arrays/failure-sequence-{sequence:06d}-A{index}.f64le',
                                              raw, [SIZE, K]))
            failure = dict(schema=SCHEMA, event='failed', source_sha256=source_sha,
                spec_sha256=digest(spec_raw), completed_steps=completed, attempted_header=header,
                error=repr(error), traceback=traceback.format_exc(), retained_original_A=artifacts,
                native_accepted=False, no_input_height_or_modes_changed=True)
            failure_path = out/'direct-ld-worker-failure.json'
            with failure_path.open('x') as stream:
                json.dump(failure, stream, sort_keys=True, indent=2, allow_nan=False)
                stream.write('\n')
            send(failure)
            return 2


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Record every cached-direction comparison, including a failed strict comparison.

Five retained true M16 frozen inputs are used without changing any state,
coefficient, Fourier table, RK step or guard. The original full-J method in the
independent derived library must first reproduce the retained production
binary64 state/J. Cache applications use all modes and are not accepted tails.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import ctypes as C
import hashlib
import json
from pathlib import Path
import resource
import struct
import time

import numpy as np

from tail_full_state_tangent_predictor import load, ref, module


def verified(item):
    if ref(item['path']) != item:
        raise ValueError('Bound input/source changed: '+item['path'])
    return Path(item['path'])


def canonical_array(raw):
    data = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 10)
    storage = np.zeros((len(data), 16), dtype=np.uint8); storage[:, :10] = data
    return storage.view(np.longdouble).ravel()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--build', type=Path, required=True)
    p.add_argument('--predictor-summary', type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    a = p.parse_args(); out = a.outdir.resolve(); out.mkdir(parents=True, exist_ok=False)
    build = load(a.build)
    for name in ['source', 'original_cpp', 'original_header', 'methods', 'exports', 'derived_cpp', 'library']:
        verified(build[name])
    if build['returncode'] != 0:
        raise ValueError('A completed independent candidate build is required')
    original = a.repo/'topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended'
    h = module('_cached_probe_abi', original/'probe_native_frozen_flow.py')
    splitter = module('_cached_probe_wire', original/'parallel_native_batch.py')
    predictor = load(a.predictor_summary)
    record = load(verified(predictor['actual_fresh_native_record']))
    wire = verified(record['input']).read_bytes(); shape = splitter.split_wire(wire)
    original_output = verified(record['output']).read_bytes()
    blocks, failed = splitter.output_records(original_output, shape, shape['count'], shape['token'], 0)
    if shape['modes'] != 16 or shape['jac'] != 1 or failed is not None:
        raise ValueError('The first cache probe is restricted to the true complete M16 J')
    fields = struct.unpack_from('<9i', wire, 8)
    abi, M, N, spacing, nq, root_iterations, halves, count, with_jac = fields
    K = 2*M; size = K+2
    floor, tolerance, fallback, scale_floor = struct.unpack_from('<4d', wire, 108)
    offset = 140
    powers = np.frombuffer(wire, '<f8', halves, offset).copy(); offset += 8*halves
    cosine = np.frombuffer(wire, '<f8', nq*(M+1), offset).copy(); offset += 8*nq*(M+1)
    sine = np.frombuffer(wire, '<f8', nq*M, offset).copy()
    def ptr(x):
        return x.ctypes.data_as(h.DoublePointer)
    cfg = h.Config(abi, M, N, spacing, nq, root_iterations, halves,
                   floor, tolerance, fallback, scale_floor, ptr(cosine), ptr(sine), ptr(powers))
    lib = C.CDLL(build['library']['path'])
    lib.vf_runtime_info.argtypes = [C.c_char_p, C.c_size_t]; lib.vf_runtime_info.restype = C.c_int
    runtime_buffer = C.create_string_buffer(4096)
    if lib.vf_runtime_info(runtime_buffer, len(runtime_buffer)):
        raise RuntimeError('Native runtime query failed')
    runtime = json.loads(runtime_buffer.value)
    for key, cls in [('config_size', h.Config), ('step_size', h.Step), ('stage_size', h.Stage), ('diagnostics_size', h.Diagnostics)]:
        if runtime[key] != C.sizeof(cls):
            raise ValueError('Declared ABI layout changed: '+key)
    if runtime['long_double_significand_bits'] != 64 or not runtime['round_to_nearest']:
        raise ValueError('Only declared native long-double arithmetic is supported')
    byteptr = C.POINTER(C.c_ubyte)
    lib.vf_run_stage.argtypes = [C.POINTER(h.Config), C.POINTER(h.Stage), C.c_int, C.c_int,
        C.POINTER(h.Callbacks), h.DoublePointer, h.DoublePointer, byteptr, byteptr,
        C.POINTER(h.Diagnostics), C.c_char_p, C.c_size_t]
    lib.vf_run_stage.restype = C.c_int
    lib.vf_cached_stage_create.argtypes = [C.POINTER(h.Config), C.POINTER(h.Stage), h.DoublePointer,
        C.POINTER(h.Diagnostics), C.POINTER(C.c_void_p), C.c_char_p, C.c_size_t]
    lib.vf_cached_stage_create.restype = C.c_int
    lib.vf_cached_stage_apply.argtypes = [C.c_void_p, C.c_int, h.DoublePointer, h.DoublePointer,
        byteptr, C.POINTER(h.Diagnostics), C.c_char_p, C.c_size_t]
    lib.vf_cached_stage_apply.restype = C.c_int
    lib.vf_cached_stage_destroy.argtypes = [C.c_void_p]; lib.vf_cached_stage_destroy.restype = None
    lib.vf_cached_stage_payload_bytes.argtypes = [C.c_void_p]; lib.vf_cached_stage_payload_bytes.restype = C.c_size_t
    rng = np.random.default_rng(20261128)
    single = np.ascontiguousarray(rng.uniform(-1, 1, (K, 1)))
    seeds = np.zeros((K, 18))
    for j in range(K):
        seeds[j, (j//M)*9+(j % M) % 9] = 1
    identity = np.eye(K)
    report = dict(scope=__doc__, source=ref(__file__), build=ref(a.build), runtime=runtime,
        predictor_summary=ref(a.predictor_summary), original_record=predictor['actual_fresh_native_record'],
        original_input=record['input'], original_output=record['output'], M=M, N=N,
        selected_stages=[0, 22, 80, 813, 1151], rows=[], nonlinear_acceptance=False,
        native_JVP_implemented=True, whole_batch_solver_implemented=False, complete_surface=False)
    def save():
        report['resource_peak_self_maxrss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        (out/'summary.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    save()
    for index in report['selected_stages']:
        start, end = shape['spans'][index]
        steps, points = struct.unpack_from('<2i', wire, start)
        cursor = start+8
        initial = np.frombuffer(wire, '<f8', size, cursor).copy(); cursor += 8*size
        coefficients = np.frombuffer(wire, '<f8', points*(M+12), cursor).copy(); cursor += 8*points*(M+12)
        step_array = (h.Step*steps)()
        for k in range(steps):
            step_array[k] = h.Step(*struct.unpack_from('<5i2d', wire, cursor)); cursor += 36
        if cursor != end:
            raise ValueError('Original frozen stage extent changed')
        stage = h.Stage(steps, points, step_array, ptr(coefficients), ptr(initial))
        full_state = np.empty(size); full_J = np.empty((size, K))
        native_state = (C.c_ubyte*(10*size))(); native_J = (C.c_ubyte*(10*size*K))()
        diag = h.Diagnostics(); error = C.create_string_buffer(4096)
        begun = time.monotonic()
        status = lib.vf_run_stage(C.byref(cfg), C.byref(stage), 1, 1, None, ptr(full_state), ptr(full_J),
            native_state, native_J, C.byref(diag), error, len(error))
        full_wall = time.monotonic()-begun
        if status:
            raise RuntimeError('Original full-J method failed: '+error.value.decode())
        old_start = blocks[index][0]+8
        expected = original_output[old_start:old_start+8*size*(K+1)]
        got = full_state.tobytes()+full_J.tobytes()
        if got != expected:
            raise ValueError('Derived original full-J method changed retained production binary64 state/J')
        full_native_J = canonical_array(bytes(native_J)).reshape(size, K)
        cached_state = np.empty(size); create_diag = h.Diagnostics(); handle = C.c_void_p()
        begun = time.monotonic()
        status = lib.vf_cached_stage_create(C.byref(cfg), C.byref(stage), ptr(cached_state), C.byref(create_diag),
            C.byref(handle), error, len(error))
        cache_wall = time.monotonic()-begun
        if status:
            raise RuntimeError('Actual cache creation failed: '+error.value.decode())
        row = dict(stage=index, original_state_J_binary64_bytes_identical=True,
            original_full_J_wall_seconds=full_wall, original_full_J_kernel_seconds=diag.kernel_seconds,
            original_root_calls=diag.root_calls, original_root_updates=diag.root_updates,
            cache_build_wall_seconds=cache_wall, cache_build_kernel_seconds=create_diag.kernel_seconds,
            cache_root_calls=create_diag.root_calls, cache_root_updates=create_diag.root_updates,
            cached_state_binary64_identical=cached_state.tobytes()==full_state.tobytes(),
            cache_payload_native_bytes=int(lib.vf_cached_stage_payload_bytes(handle)), applications=[])
        arrays = dict(original_state=full_state, original_J=full_J,
            original_state_canonical80=np.frombuffer(bytes(native_state), np.uint8),
            original_J_canonical80=np.frombuffer(bytes(native_J), np.uint8))
        try:
            if not row['cached_state_binary64_identical']:
                raise ValueError('Cached state trajectory differs from original full-J path')
            previous_single = None
            for label, seed in [('single', single), ('colored18', seeds), ('identity32', identity), ('single_reuse', single)]:
                b = seed.shape[1]; result = np.empty((size, b)); native = (C.c_ubyte*(10*size*b))()
                apply_diag = h.Diagnostics(); begun = time.monotonic()
                status = lib.vf_cached_stage_apply(handle, b, ptr(seed), ptr(result), native,
                    C.byref(apply_diag), error, len(error))
                wall = time.monotonic()-begun
                if status:
                    raise RuntimeError('Actual cache application failed: '+error.value.decode())
                actual_native = canonical_array(bytes(native)).reshape(size, b)
                expected_native = full_native_J@seed.astype(np.longdouble)
                difference = np.abs(actual_native-expected_native)
                denominator = np.abs(full_native_J)@np.abs(seed.astype(np.longdouble))
                relative = np.divide(difference, denominator, out=np.zeros_like(difference), where=denominator>0)
                if np.any((denominator==0)&(difference!=0)):
                    raise ValueError('A zero complete derivative became nonzero')
                metric = dict(label=label, complete_input_directions=b, wall_seconds=wall,
                    kernel_seconds=apply_diag.kernel_seconds, root_calls_unchanged=apply_diag.root_calls==create_diag.root_calls,
                    root_updates_unchanged=apply_diag.root_updates==create_diag.root_updates,
                    maximum_absolute_difference_from_full_native_J_product=float(np.max(difference)),
                    maximum_componentwise_absolute_product_scaled_difference=float(np.max(relative)),
                    canonical80_sha256=digest(bytes(native)),
                    binary64_sha256=digest(result.tobytes()))
                if label == 'single':
                    previous_single = bytes(native)
                if label == 'single_reuse':
                    metric['repeated_native_result_bytes_identical'] = bytes(native)==previous_single
                if not metric['root_calls_unchanged'] or not metric['root_updates_unchanged']:
                    raise ValueError('The apply path unexpectedly repeated the root solve')
                loc = np.unravel_index(int(np.argmax(relative)), relative.shape)
                metric['largest_relative_discrepancy_location'] = [int(x) for x in loc]
                metric['largest_relative_discrepancy_actual'] = str(actual_native[loc])
                metric['largest_relative_discrepancy_expected'] = str(expected_native[loc])
                metric['largest_relative_discrepancy_absolute_product'] = str(denominator[loc])
                metric['strict_1e12_componentwise_comparison_passed'] = metric['maximum_componentwise_absolute_product_scaled_difference'] <= 1e-12
                metric['global_absolute_product_scaled_difference'] = float(np.max(difference)/np.max(denominator))
                row['applications'].append(metric)
                arrays[label+'_seed'] = seed; arrays[label+'_result'] = result
                arrays[label+'_canonical80'] = np.frombuffer(bytes(native), np.uint8)
        finally:
            lib.vf_cached_stage_destroy(handle)
        artifact = out/f'stage-{index:04d}-complete-directions.npz'
        np.savez_compressed(artifact, **arrays); row['raw'] = ref(artifact)
        report['rows'].append(row); save(); print(json.dumps(row), flush=True)
    report['status'] = 'all_five_actual_native_cached_direction_probes_returned'
    report['all_strict_comparisons_passed'] = all(x['strict_1e12_componentwise_comparison_passed'] for r in report['rows'] for x in r['applications'])
    report['production_source_or_kernel_changed'] = False; save()
    print(json.dumps(dict(summary=ref(out/'summary.json'), status=report['status'])), flush=True)


if __name__ == '__main__':
    main()

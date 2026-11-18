#!/usr/bin/env python3
"""One frozen-library, null-trace long-double probe of three original stages.

Exactly six native calls: state-only then full40-Jac for stages43,38,175.
The two42-component states must agree in every canonical80 and binary64 byte.
All native outputs, including the full42x40 tangent, remain in scratch files.
No traced extra call, precision scan, root/RHS rewrite, batch or DN is invoked.
The MP90 comparison only reads the previously saved nonlinear trajectory.
"""
import argparse
import ctypes as C
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import struct
import sys
import time
import traceback

import mpmath as mp


BUILD_SHA = '6a3bccea3aafe115cb28071ca23986e14e27c9074c67f8f91b094bfb87db0bf8'
CPP_SHA = '916d0a948a15100f9bb68b255c2192460efe249c08a3559ea9fb800fbb59ac3f'
HARNESS_SHA = '42893f210b6d31c59abd04cdfec415a2408a543f726f87d808fc99cf8fad45db'
BASELINE_SHA = '8bc4adafbd655fe5fa5de7b7fbda542a3c4edda5b7505deb579d9ec40a503078'
CAPSULE_SHA = '3785fff5412ec751d2275d3f774b6c7503bfecb7ad781a38068f811f06ab35f7'
MP90_SHA = '316203483014a16efb7a9793c62e2c903e0925a946cd9a30a7ed869b76f766e6'
STAGES = (43, 38, 175)
CALLS = [dict(stage=s, with_jac=j) for s in STAGES for j in (False, True)]
ROOT_DIAGNOSTICS = ('root_calls', 'root_updates', 'root_fallbacks',
                    'trace_events', 'minA', 'minD', 'max_root_relative_residual',
                    'scalar_bytes')
mp.mp.dps = 140


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ident(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def load(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def checked(ref):
    if ident(ref['path']) != ref:
        raise ValueError('Frozen source/input changed: ' + ref['path'])
    return load(ref['path'])


def bytes_sha(data):
    return hashlib.sha256(data).hexdigest()


def packed(values):
    return struct.pack('<' + 'd' * len(values), *values)


def dump(path, value, compressed=False):
    path = Path(path)
    if path.exists():
        raise ValueError('Do not overwrite an executed result: ' + str(path))
    data = (json.dumps(value, ensure_ascii=False, allow_nan=False, indent=None if compressed else 2)
            + '\n').encode()
    path.write_bytes(gzip.compress(data, mtime=0) if compressed else data)
    return ident(path)


def import_harness(ref):
    if ref['sha256'] != HARNESS_SHA or ident(ref['path']) != ref:
        raise ValueError('Only the reviewed unchanged ABI helper may be imported')
    spec = importlib.util.spec_from_file_location('reviewed_native_abi', ref['path'])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_inputs(plan):
    if plan['schema'] != 'n4-native-longdouble-pair-v1' or plan['calls'] != CALLS:
        raise ValueError('The prescribed six-call order changed')
    if plan['trace_callback'] is not False or plan['extra_traced_calls'] != 0:
        raise ValueError('This plan has no trace callback or additional traced run')
    refs = plan['files']
    for ref in refs.values():
        if ident(ref['path']) != ref:
            raise ValueError('A frozen plan source/input changed: ' + ref['path'])
    if refs['probe'] != ident(__file__):
        raise ValueError('The plan does not name this exact probe source')
    expected = dict(build_record=BUILD_SHA, native_baseline=BASELINE_SHA,
                    capsule_summary=CAPSULE_SHA, mp90_summary=MP90_SHA)
    for key, digest in expected.items():
        if refs[key]['sha256'] != digest:
            raise ValueError('This probe is restricted to the already reviewed inputs: ' + key)
    build = checked(refs['build_record'])
    if build['sources']['cpp']['sha256'] != CPP_SHA or build['sources']['harness']['sha256'] != HARNESS_SHA:
        raise ValueError('The original compiled kernel/harness changed')
    for ref in list(build['sources'].values()) + [build['library'], build['batch_executable']]:
        if ident(ref['path']) != ref:
            raise ValueError('The original build source/binary changed')
    if any(row['returncode'] != 0 for row in build['compile_results'].values()):
        raise ValueError('The original native build was unsuccessful')
    cs = checked(refs['capsule_summary'])
    bs = checked(refs['old_float_baseline'])
    nb = checked(refs['native_baseline'])
    ms = checked(refs['mp90_summary'])
    terminal = checked(refs['native_baseline_resource'])
    if terminal['status'] != 'observed_terminal' or terminal['child_returncode'] != 0:
        raise ValueError('The original native double baseline has no successful real terminal')
    for key in ('source_sha256', 'additional_original_root_sources'):
        for path, digest in cs[key].items():
            if sha(path) != digest:
                raise ValueError('A bound original source changed: ' + path)
    for name in ('input', 'fixture', 'original_output', 'coefficients', 'reference'):
        if ident(cs[name]['path']) != cs[name]:
            raise ValueError('A bound original state/fixture changed: ' + name)
    if (nb['mode'] != 'float-baseline' or not nb['all_three_outputs42_bitwise_identical']
            or not nb['all_original_operands_and_judgments_bitwise_identical']
            or nb['verified_event_count'] != 116608 or nb['verified_output_count'] != 126
            or nb['build_record'] != refs['build_record'] or nb['source'] != build['sources']['harness']
            or nb['capsule_summary'] != refs['capsule_summary']
            or nb['mp90_summary'] != refs['mp90_summary']
            or nb['old_float_baseline'] != refs['old_float_baseline']):
        raise ValueError('The exact native double baseline is not for this library and input')
    if ident(nb['raw']['path']) != nb['raw']:
        raise ValueError('The complete saved native double trace changed')
    if (not bs['all_three_outputs42_bitwise_identical']
            or not bs['all_original_operands_and_judgments_bitwise_identical']
            or bs['capsule_summary_sha256'] != refs['capsule_summary']['sha256']
            or ms['validated_baseline_sha256'] != refs['old_float_baseline']['sha256']
            or ms['capsule_summary_sha256'] != refs['capsule_summary']['sha256']
            or ms['precision'] != 'mp' or ms['dps'] != 90):
        raise ValueError('The saved original float/MP90 comparison chain changed')
    capsule, precise = checked(cs['coefficients']), checked(ms['raw'])
    if (capsule['modes'] != 20 or capsule['spacing'] != 4 or capsule['quadrature'] != 512
            or [f['stage'] for f in capsule['fixtures']] != list(STAGES)
            or [r['stage'] for r in precise['rows']] != list(STAGES)):
        raise ValueError('This probe is restricted to the original three complete stage inputs')
    return build, cs, nb, ms, capsule, precise


def bind_library(build, h):
    library = C.CDLL(build['library']['path'])
    library.vf_runtime_info.argtypes = [C.c_char_p, C.c_size_t]
    library.vf_runtime_info.restype = C.c_int
    library.vf_run_stage.argtypes = [C.POINTER(h.Config), C.POINTER(h.Stage), C.c_int, C.c_int,
        C.POINTER(h.Callbacks), h.DoublePointer, h.DoublePointer,
        C.POINTER(C.c_ubyte), C.POINTER(C.c_ubyte), C.POINTER(h.Diagnostics), C.c_char_p, C.c_size_t]
    library.vf_run_stage.restype = C.c_int
    return library


def runtime_info(library, h):
    buf = C.create_string_buffer(4096)
    if library.vf_runtime_info(buf, len(buf)):
        raise ValueError('Runtime metadata call failed')
    row = json.loads(buf.value)
    for key, cls in (('config_size', h.Config), ('step_size', h.Step), ('stage_size', h.Stage),
                     ('callbacks_size', h.Callbacks), ('diagnostics_size', h.Diagnostics)):
        if row[key] != C.sizeof(cls):
            raise ValueError('C ABI mismatch: ' + key)
    if (row['abi'] != 1 or row['long_double_significand_bits'] != 64
            or row['long_double_storage_bytes'] != 16 or not row['round_to_nearest']
            or ((row['x87_control_word'] >> 8) & 3) != 3):
        raise ValueError('Only the declared nearest,64-significand x87 runtime is supported')
    return row


class DlInfo(C.Structure):
    _fields_ = [('dli_fname', C.c_char_p), ('dli_fbase', C.c_void_p),
                ('dli_sname', C.c_char_p), ('dli_saddr', C.c_void_p)]


def runtime_libraries(library, expected_library, path):
    """Read loaded mappings and resolve symbols; never call the math functions.

    Symbol lookup documents the loaded provider, not the number of calls and
    not whether the compiler implements a particular sqrt using an instruction.
    """
    maps = Path('/proc/self/maps').read_text()
    if path.exists():
        raise ValueError('Do not overwrite process mappings')
    path.write_text(maps)
    names = set()
    for line in maps.splitlines():
        parts = line.split(None, 5)
        if len(parts) != 6 or not parts[5].startswith('/'):
            continue
        filename = parts[5]
        if filename.endswith(' (deleted)'):
            raise ValueError('A mapped binary was deleted; cannot bind its actual bytes')
        names.add(str(Path(filename).resolve()))
    mapped = {name: ident(name) for name in sorted(names)}
    if mapped.get(expected_library['path']) != expected_library:
        raise ValueError('The expected original library is not the mapped binary')
    process = C.CDLL(None)
    process.dladdr.argtypes = [C.c_void_p, C.POINTER(DlInfo)]
    process.dladdr.restype = C.c_int
    symbols = {}
    for symbol in ('vf_run_stage', 'sqrtl', 'log1pl', 'expm1l'):
        pointer = C.cast(getattr(library, symbol), C.c_void_p)
        info = DlInfo()
        if not pointer.value or not process.dladdr(pointer, C.byref(info)) or not info.dli_fname:
            raise ValueError('Cannot bind loaded symbol: ' + symbol)
        provider = ident(info.dli_fname.decode())
        if mapped.get(provider['path']) != provider:
            raise ValueError('Resolved symbol provider is absent from actual mappings')
        symbols[symbol] = dict(provider=provider,
            resolved_symbol=info.dli_sname.decode() if info.dli_sname else None,
            provider_relative_offset=pointer.value - info.dli_fbase)
    return dict(maps=ident(path), mapped_binaries=list(mapped.values()), symbol_resolution=symbols,
        symbol_scope='Loaded-handle symbol providers only; no math calls or compiler-inlining claim.',
        python=ident(sys.executable), python_version=sys.version, platform=platform.platform(),
        mpmath=ident(mp.__file__), mpmath_version=mp.__version__,
        byteorder=sys.byteorder, pid=os.getpid())


def arrays_identity(config, stage, keepers):
    # Whole structs are compared only before/after this same call. Their pointer
    # addresses/padding are never treated as cross-process physical identities.
    return dict(arrays=[bytes_sha(C.string_at(C.addressof(a), C.sizeof(a))) for a in keepers],
                config_struct=bytes_sha(C.string_at(C.addressof(config), C.sizeof(config))),
                stage_struct=bytes_sha(C.string_at(C.addressof(stage), C.sizeof(stage))))


def diag_values(diagnostics, h):
    row = {key: getattr(diagnostics, key) for key, _ in h.Diagnostics._fields_}
    return {k: None if isinstance(v, float) and not math.isfinite(v) else v for k, v in row.items()}


def diagnostic_identity(row):
    return [packed([row[k]]).hex() if isinstance(row[k], float) else row[k] for k in ROOT_DIAGNOSTICS]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    a = parser.parse_args()
    plan = load(a.plan)
    build, cs, nb, ms, capsule, precise = check_inputs(plan)
    h = import_harness(build['sources']['harness'])
    prefix = Path(plan['out_prefix'])
    prefix.parent.mkdir(parents=True, exist_ok=True)
    suffixes = ['summary.json', 'raw.json.gz', 'failure.json.gz', 'maps.txt']
    suffixes += [f'stage{s}-{kind}.json.gz' for s in STAGES for kind in ('state-only', 'full-jac')]
    if any(Path(str(prefix) + '-' + suffix).exists() for suffix in suffixes):
        raise ValueError('This execution prefix already contains a result; no overwrite or automatic rerun')
    context = dict(scope=__doc__,plan=ident(a.plan),source=ident(__file__),files=plan['files'],
        build_record=plan['files']['build_record'],sources=build['sources'],library=build['library'],
        original_input=cs['input'],original_fixture=cs['fixture'],original_output=cs['original_output'],
        coefficients=cs['coefficients'],reference=cs['reference'],mp90_raw=ms['raw'],
        native_baseline=plan['files']['native_baseline'],root_rules=capsule['root_rules'],
        command=sys.argv, production_changed=False, full_tail_or_DN_invoked=False,
        nonlinear_mp_recomputed=False, trace_callback=False, prescribed_native_call_count=6)
    rows, scalars, pairs = [], [], []
    last_call = None
    began = time.monotonic()
    try:
        library = bind_library(build, h)
        runtime = runtime_info(library, h)
        context['runtime_initial'] = runtime
        context['loaded_runtime'] = runtime_libraries(library, build['library'], Path(str(prefix) + '-maps.txt'))
        for index, fixture in enumerate(capsule['fixtures']):
            previous = None
            for with_jac in (False, True):
                last_call = dict(stage=fixture['stage'],with_jac=with_jac)
                print(json.dumps(dict(event='native_call_start', **last_call)), flush=True)
                config, stage, keepers = h.abi_inputs(capsule, fixture)
                before_input = arrays_identity(config, stage, keepers)
                before_runtime = runtime_info(library, h)
                if before_runtime != runtime:
                    raise ValueError('The declared runtime control state changed before a call')
                state = (C.c_double * 42)()
                tangent = (C.c_double * 1680)() if with_jac else None
                native_state = (C.c_ubyte * 420)()
                native_tangent = (C.c_ubyte * 16800)() if with_jac else None
                diagnostics = h.Diagnostics()
                error = C.create_string_buffer(4096)
                started_ffi = time.monotonic()
                status = library.vf_run_stage(C.byref(config), C.byref(stage), 1, int(with_jac), None,
                    state, tangent, native_state, native_tangent, C.byref(diagnostics), error, len(error))
                ffi_seconds = time.monotonic() - started_ffi
                after_runtime = runtime_info(library, h)
                after_input = arrays_identity(config, stage, keepers)
                diag = diag_values(diagnostics, h)
                if status:
                    raise RuntimeError(json.dumps(dict(last_call=last_call,status=status,
                        error=error.value.decode(),diagnostics=diag,ffi_seconds=ffi_seconds)))
                decode_start = time.monotonic()
                state64, encoded = list(state), bytes(native_state)
                values80 = [h.native80_value(encoded[k:k+10]) for k in range(0, 420, 10)]
                physical = [v if j < 20 else v / fixture['portRatio'] for j, v in enumerate(state64[:40])]
                residual = [v - fixture['targetNode40'][j] for j, v in enumerate(physical)]
                row = dict(**last_call,state=state64,state64_hex=packed(state64).hex(),
                    native_state_hex=encoded.hex(),diagnostics=diag,
                    runtime_before=before_runtime,runtime_after=after_runtime,
                    input_arrays_before=before_input,input_arrays_after=after_input,
                    fixed_target_residual=residual)
                scalar = dict(**last_call,diagnostics=diag,output42_sha256=bytes_sha(packed(state64)),
                    native_output42_sha256=bytes_sha(encoded),
                    native_error_to_mp90=h.mp_errors(values80, precise['rows'][index]['state'], fixture),
                    boundary64_error_to_mp90=h.mp_errors([mp.mpf(v) for v in state64],
                                                       precise['rows'][index]['state'], fixture),
                    fixed_target_normalized_residual=max(map(abs, residual)) / fixture['normalizationScale'],
                    runtime_unchanged=after_runtime == before_runtime,
                    input_arrays_unchanged=after_input == before_input,ffi_seconds=ffi_seconds)
                if with_jac:
                    tangent64, encoded_tangent = list(tangent), bytes(native_tangent)
                    # Decode all canonical values to reject invalid extended encodings;
                    # their full original10-byte encodings are the stored authority.
                    for k in range(0, 16800, 10):
                        h.native80_value(encoded_tangent[k:k+10])
                    row.update(tangent=tangent64,tangent64_hex=packed(tangent64).hex(),
                               native_tangent_hex=encoded_tangent.hex())
                    scalar.update(tangent42_by40_sha256=bytes_sha(packed(tangent64)),
                                  native_tangent42_by40_sha256=bytes_sha(encoded_tangent))
                scalar['python_decode_compare_seconds'] = time.monotonic() - decode_start
                row['timing'] = dict(ffi_seconds=ffi_seconds,
                    python_decode_compare_seconds=scalar['python_decode_compare_seconds'])
                checkpoint = Path(str(prefix) + f"-stage{fixture['stage']}-"
                                  + ('full-jac' if with_jac else 'state-only') + '.json.gz')
                scalar['checkpoint'] = dump(checkpoint,dict(**context,row=row),True)
                rows.append(row)
                scalars.append(scalar)
                if after_runtime != before_runtime or before_input != after_input:
                    raise ValueError('Runtime control or complete ABI input changed during a call')
                if diag['root_calls'] != 4 * stage.nsteps or diag['trace_events'] != 0 or diag['scalar_bytes'] != 10:
                    raise ValueError('The prescribed null-trace stage/root count or scalar encoding changed')
                if with_jac:
                    if diag['min_literal_Jacobian_pivot'] is None or diag['min_literal_Jacobian_pivot'] <= 0:
                        raise ValueError('The independent literal Jacobian decomposition lacks a positive finite pivot')
                    pair = dict(stage=fixture['stage'],
                        native42_bitwise_identical=previous['native_state_hex'] == row['native_state_hex'],
                        binary64_42_bitwise_identical=previous['state64_hex'] == row['state64_hex'],
                        root_diagnostics_bitwise_identical=diagnostic_identity(previous['diagnostics']) == diagnostic_identity(diag))
                    pairs.append(pair)
                    if not all(value for key, value in pair.items() if key != 'stage'):
                        raise ValueError('State-only/full-Jac complete-state or original root diagnostic identity failed')
                previous = row
                print(json.dumps(dict(event='native_call_complete',**scalar)), flush=True)
        if len(rows) != 6 or len(pairs) != 3 or [dict(stage=r['stage'],with_jac=r['with_jac']) for r in rows] != CALLS:
            raise ValueError('The prescribed six-call inventory is incomplete')
        raw = dump(Path(str(prefix) + '-raw.json.gz'),dict(**context,rows=rows),True)
        summary = dict(**context,raw=raw,named_results=scalars,pairs=pairs,
            native_call_count=len(rows),all_native42_state_pairs_bitwise_identical=True,
            all_binary64_42_state_pairs_bitwise_identical=True,
            all_root_diagnostic_pairs_bitwise_identical=True,
            full40_column_Jacobian_computed=True,independent_Jacobian_reference_verified=False,
            root_diagnostic_scope='All available VFDiagnostics aggregates; null trace does not store per-root iteration/halving sequences.',
            timing_scope='kernel_seconds is null-trace native e.flow wall, including its allocations. FFI adds engine construction/export; Python decoding/comparison is separately timed. Three stages are not a whole-tail benchmark.',
            seconds=time.monotonic()-began,
            original_norm_or_DN_acceptance_performed=False,
            scope_limit='Frozen binary64 coefficients, original finite RK and point-root thresholds. Literal implicit Jacobian is evaluated at approximate returned roots, not AD of stopping branches or a continuous-flow certificate.')
        summary_ref = dump(Path(str(prefix) + '-summary.json'),summary)
        print(json.dumps(dict(event='terminal',summary=summary_ref)), flush=True)
    except Exception:
        failure = dump(Path(str(prefix) + '-failure.json.gz'),dict(**context,last_call=last_call,
            completed_rows=rows,completed_scalars=scalars,pairs=pairs,traceback=traceback.format_exc()),True)
        print(json.dumps(dict(event='failure',record=failure)), flush=True)
        raise


if __name__ == '__main__':
    main()

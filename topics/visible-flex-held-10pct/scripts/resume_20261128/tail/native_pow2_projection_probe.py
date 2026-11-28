#!/usr/bin/env python3
"""Compile an isolated six-site power-of-two projection candidate and replay real stages.

The live native executable and original source are never edited.  Only the six
literal angular divisions are replaced; each existing numerator and summation
order is retained.  Native long-double finite numerators with power-of-two N
and nq use the exactly represented reciprocal.  All other inputs, including
the binary64 callback mode, retain the literal original division.

Comparison covers every binary64 state/Jacobian and every non-timing diagnostic
byte of the actual native wire output.  It does not claim to compare the optional
canonical 80-bit ABI buffers, which the production CLI does not emit.
"""
import argparse
import datetime
import difflib
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import shutil
import struct
import subprocess
import sys
import time

import numpy as np


ORIGINAL_CPP = 'e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf'
ORIGINAL_HEADER = '88d7b9bc6c92a3d73ca33b2152e8bac078b6c9b3f90167f5e0a3409dd01f8356'
FLAGS = ['-std=c++17', '-O2', '-fno-fast-math', '-ffp-contract=off',
         '-fexcess-precision=standard', '-frounding-math']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def ref(path):
    p = Path(path).resolve()
    return dict(path=str(p), sha256=sha(p.read_bytes()), bytes=p.stat().st_size)


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False)+'\n')


def verified(item):
    p = Path(item['path'])
    if sha(p.read_bytes()) != item['sha256']:
        raise ValueError('Reference changed: '+str(p))
    return p


def replace_one(source, old, new):
    if source.count(old) != 1:
        raise ValueError('Expected one exact source occurrence: '+old)
    return source.replace(old, new)


def prepare_source(original):
    source = replace_one(original, '    bool tracing;\n',
        '    R inverse_nq;\n    bool exact_pow2_projection;\n    bool tracing;\n')
    source = replace_one(source, '    void emit(int code,', '''    R angular_mean(R numerator) const {
        if constexpr (std::is_same_v<R,long double>) {
            if(exact_pow2_projection && std::isfinite(numerator))
                return numerator*inverse_nq;
        }
        return numerator/nq;
    }
    void emit(int code,''')
    expressions = ['q*co[i]', 'bm*co[i]*co[j]', 'q[0]*co[i]*co[k]',
                   'chain*co[i]', 'df*si[j]', 'product*sn[n*M+j]']
    for expression in expressions:
        source = replace_one(source, expression+'/nq', 'angular_mean('+expression+')')
    source = replace_one(source, '        scale_floor(c.scale_floor),tracing(cb.trace!=nullptr) {',
        '''        scale_floor(c.scale_floor),inverse_nq(R(1)/R(c.nq)),
        exact_pow2_projection(c.N>0 && (c.N&(c.N-1))==0 &&
                              c.nq>0 && (c.nq&(c.nq-1))==0),
        tracing(cb.trace!=nullptr) {''')
    return source, expressions


def load_wire_helper(path):
    spec = importlib.util.spec_from_file_location('reviewed_parallel_wire', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def records(data, shape, helper):
    blocks, failed = helper.output_records(data, shape, shape['count'], shape['token'], 0)
    if failed is not None:
        raise ValueError('A failed stage cannot be a successful replay baseline')
    return blocks


def normalized(data, shape, helper):
    blocks = records(data, shape, helper)
    # The last eight bytes of each successful record are kernel_seconds only.
    return data[:88]+b''.join(data[a:b-8] for a, b, status in blocks)


def subset_wire(wire, shape, indices):
    header = bytearray(shape['header'])
    struct.pack_into('<i', header, 36, len(indices))
    header[44:108] = b'0'*64
    body = b''.join(wire[shape['spans'][i][0]:shape['spans'][i][1]] for i in indices)
    header[44:108] = sha(header+body).encode('ascii')
    return bytes(header)+body


def subset_output(data, source_shape, indices, target_shape, helper):
    spans = records(data, source_shape, helper)
    out = bytearray(b'VFN4OUT1'+struct.pack('<4i', source_shape['abi'], source_shape['modes'],
                                        len(indices), source_shape['jac'])+target_shape['token'])
    for local, index in enumerate(indices):
        start, end, status = spans[index]
        out.extend(struct.pack('<i', local))
        out.extend(data[start+4:end])
    return bytes(out)


def choose_stages(wire, shape, record):
    m = shape['modes']
    ranked = []
    for index, (start, end) in enumerate(shape['spans']):
        steps, points = struct.unpack_from('<2i', wire, start)
        offset = start+8+8*(2*m+2)
        values = np.frombuffer(wire, dtype='<f8', offset=offset,
                               count=points*(m+12)).reshape(points, m+12)
        radius = np.cbrt(values[:, 0])
        slope = values[:, 6]/values[:, 2]
        order = np.argsort(radius)
        radius, slope = radius[order], slope[order]
        dr = np.diff(radius)
        good = dr != 0
        secant = np.abs(np.diff(slope)[good]/dr[good])
        secant /= (1+((slope[1:][good]+slope[:-1][good])/2)**2)**1.5
        ranked.append(float(np.max(secant)))
    curvature = int(np.argmax(ranked))
    labels = dict(first=0, deepest=shape['count']-1,
        smallest_original_minA=min(record['diagnostics'], key=lambda r: r['minA'])['stage'],
        smallest_original_minD=min(record['diagnostics'], key=lambda r: r['minD'])['stage'],
        largest_background_curvature_secant=curvature)
    return sorted(set(labels.values())), dict(labels=labels,
        curvature_secant_value=ranked[curvature],
        curvature_selection_scope='Adjacent frozen radius/slope secants select a stressed region; not a curvature certificate')


def run_one(binary, inp, output, expected, helper):
    shape = helper.split_wire(inp.read_bytes())
    begun = time.monotonic()
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = subprocess.run([str(binary), str(inp), str(output)], capture_output=True)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    row = dict(command=[str(binary), str(inp), str(output)], returncode=result.returncode,
        wall_seconds=time.monotonic()-begun,
        user_seconds=after.ru_utime-usage.ru_utime,
        system_seconds=after.ru_stime-usage.ru_stime,
        stdout_sha256=sha(result.stdout), stderr_sha256=sha(result.stderr))
    output.with_suffix(output.suffix+'.stdout').write_bytes(result.stdout)
    output.with_suffix(output.suffix+'.stderr').write_bytes(result.stderr)
    if result.returncode != 0:
        raise RuntimeError('Native replay failed: '+result.stderr.decode(errors='replace'))
    data = output.read_bytes()
    actual = normalized(data, shape, helper)
    wanted = normalized(expected, shape, helper)
    row.update(output=ref(output), compared_bytes=len(wanted),
        expected_nontiming_sha256=sha(wanted), actual_nontiming_sha256=sha(actual),
        state_J_and_all_nontiming_diagnostics_byte_equal=(actual == wanted),
        stage_count=shape['count'], jacobian=bool(shape['jac']))
    row['kernel_seconds_sum'] = sum(struct.unpack_from('<d', data, end-8)[0]
        for start, end, status in records(data, shape, helper))
    if actual != wanted:
        row['first_nontiming_different_byte'] = next((i for i, (x, y) in
            enumerate(zip(actual, wanted)) if x != y), min(len(actual), len(wanted)))
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--original-native', type=Path, required=True)
    parser.add_argument('--native-runs', type=Path, required=True)
    parser.add_argument('--jac-record', default='0005-jac-record.json')
    parser.add_argument('--fallback-runs', type=Path)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--full-replay', action='store_true')
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=False)
    native_dir = args.repo/'topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended'
    cpp, header = native_dir/'frozen_flow_production.cpp', native_dir/'frozen_flow.h'
    if sha(cpp.read_bytes()) != ORIGINAL_CPP or sha(header.read_bytes()) != ORIGINAL_HEADER:
        raise ValueError('Reviewed native source changed')
    original = cpp.read_text()
    candidate, sites = prepare_source(original)
    source = args.outdir/'frozen_flow_pow2_projection.cpp'
    source.write_text(candidate)
    shutil.copy2(header, args.outdir/'frozen_flow.h')
    patch = args.outdir/'candidate.patch'
    patch.write_text(''.join(difflib.unified_diff(original.splitlines(True), candidate.splitlines(True),
        fromfile='frozen_flow_production.cpp', tofile=source.name)))
    binary = args.outdir/'frozen_flow_pow2_projection'
    compiler = Path(shutil.which('g++')).resolve()
    command = [str(compiler), *FLAGS, '-DVF_BUILD_MAIN', str(source), '-o', str(binary), '-lm']
    result = dict(scope=__doc__, started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        driver=ref(__file__), original_cpp=ref(cpp), original_header=ref(header),
        original_native=ref(args.original_native), candidate_cpp=ref(source), patch=ref(patch),
        replacement_sites=sites, original_sum_order_retained=True,
        candidate_live_native_installed=False, compiler=ref(compiler), compiler_command=command,
        records=[], accepted_for_future_execution=False)
    summary = args.outdir/'summary.json'
    write_json(summary, result)
    built = subprocess.run(command, capture_output=True)
    (args.outdir/'compiler.stdout').write_bytes(built.stdout)
    (args.outdir/'compiler.stderr').write_bytes(built.stderr)
    result['compiler_returncode'] = built.returncode
    if built.returncode != 0:
        write_json(summary, result)
        raise RuntimeError('Compilation failed: '+built.stderr.decode(errors='replace'))
    result['candidate_native'] = ref(binary)
    helper = load_wire_helper(native_dir/'parallel_native_batch.py')
    result['wire_helper'] = ref(native_dir/'parallel_native_batch.py')
    record_path = args.native_runs/args.jac_record
    record = json.loads(record_path.read_text())
    inp, oldout = verified(record['input']), verified(record['output'])
    wire, expected = inp.read_bytes(), oldout.read_bytes()
    shape = helper.split_wire(wire)
    indices, selection = choose_stages(wire, shape, record)
    result.update(original_record=ref(record_path), original_input=ref(inp), original_output=ref(oldout),
                  selected_stages=indices, selection=selection)
    sample = args.outdir/'selected-input.bin'
    sample.write_bytes(subset_wire(wire, shape, indices))
    sample_shape = helper.split_wire(sample.read_bytes())
    sample_expected = subset_output(expected, shape, indices, sample_shape, helper)
    result['selected_input'] = ref(sample)
    # Alternating order reduces the effect of other live workers on timing.
    for repetition in range(3):
        sequence = [('original', args.original_native), ('candidate', binary)]
        if repetition % 2:
            sequence.reverse()
        for name, executable in sequence:
            row = run_one(executable, sample, args.outdir/f'selected-{repetition}-{name}.bin',
                          sample_expected, helper)
            row.update(label=name, repetition=repetition, scope='selected_actual_M12_J_stages')
            result['records'].append(row)
            write_json(summary, result)
            print(json.dumps(row), flush=True)
            if not row['state_J_and_all_nontiming_diagnostics_byte_equal']:
                return 2
    if args.fallback_runs:
        path = args.fallback_runs/'0001-jac-record.json'
        fallback = json.loads(path.read_text())
        fp, fo = verified(fallback['input']), verified(fallback['output'])
        fw, fe = fp.read_bytes(), fo.read_bytes()
        fs = helper.split_wire(fw)
        fi = [0, fs['count']-1]
        fp2 = args.outdir/'nonpowerN-fallback-input.bin'
        fp2.write_bytes(subset_wire(fw, fs, fi))
        fexpected = subset_output(fe, fs, fi, helper.split_wire(fp2.read_bytes()), helper)
        row = run_one(binary, fp2, args.outdir/'nonpowerN-fallback-candidate.bin', fexpected, helper)
        row.update(label='candidate', scope='actual_nonpowerN_original_division_fallback',
                   original_record=ref(path), selected_stages=fi)
        result['records'].append(row)
        write_json(summary, result)
        if not row['state_J_and_all_nontiming_diagnostics_byte_equal']:
            return 2
    if args.full_replay:
        row = run_one(binary, inp, args.outdir/'all-stages-candidate-output.bin', expected, helper)
        row.update(label='candidate', scope='all_actual_M12_J_stages')
        result['records'].append(row)
        write_json(summary, result)
        print(json.dumps(row), flush=True)
        if not row['state_J_and_all_nontiming_diagnostics_byte_equal']:
            return 2
    result.update(status='completed_all_requested_byte_comparisons',
        all_requested_nontiming_bytes_equal=True,
        ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    write_json(summary, result)
    print(json.dumps(dict(summary=str(summary), status=result['status'])), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())

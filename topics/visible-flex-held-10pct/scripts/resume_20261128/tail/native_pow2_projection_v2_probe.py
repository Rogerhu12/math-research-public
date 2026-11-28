#!/usr/bin/env python3
"""Measure a separate configuration-only power-of-two angular scaling candidate.

This candidate removes V1's per-element isfinite branch.  Positive finite N
and nq and their power-of-two property are checked once in the constructor.
On the original finite evaluation domain, reciprocal multiplication is the
same exact binary exponent shift as division; every original domain, root,
literal-J, output-finiteness, and audit check remains in place.  Non-power-of-
two N or nq and binary64 callback mode retain the original literal division.
No live solver binary is edited or selected by this measurement.
"""
import argparse
import datetime
import difflib
import json
from pathlib import Path
import shutil
import subprocess
import sys

import native_pow2_projection_probe as base


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--original-native', type=Path, required=True)
    parser.add_argument('--native-runs', type=Path, required=True)
    parser.add_argument('--fallback-runs', type=Path)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--full-replay', action='store_true')
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=False)
    own = args.repo/'topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended'
    cpp, header = own/'frozen_flow_production.cpp', own/'frozen_flow.h'
    if (base.sha(cpp.read_bytes()) != base.ORIGINAL_CPP or
            base.sha(header.read_bytes()) != base.ORIGINAL_HEADER):
        raise ValueError('Reviewed original native source changed')
    original = cpp.read_text()
    candidate, sites = base.prepare_source(original)
    candidate = base.replace_one(candidate,
        'if(exact_pow2_projection && std::isfinite(numerator))', 'if(exact_pow2_projection)')
    source = args.outdir/'frozen_flow_pow2_projection_v2.cpp'
    source.write_text(candidate)
    shutil.copy2(header, args.outdir/'frozen_flow.h')
    patch = args.outdir/'candidate.patch'
    patch.write_text(''.join(difflib.unified_diff(original.splitlines(True), candidate.splitlines(True),
        fromfile='frozen_flow_production.cpp', tofile=source.name)))
    compiler = Path(shutil.which('g++')).resolve()
    binary = args.outdir/'frozen_flow_pow2_projection_v2'
    command = [str(compiler), *base.FLAGS, '-DVF_BUILD_MAIN', str(source), '-o', str(binary), '-lm']
    result = dict(scope=__doc__, started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        driver=base.ref(__file__), probe_helper=base.ref(base.__file__), original_cpp=base.ref(cpp),
        original_header=base.ref(header), original_native=base.ref(args.original_native),
        candidate_cpp=base.ref(source), patch=base.ref(patch), replacement_sites=sites,
        finite_domain_scaling_only=True, per_element_finiteness_branch=False,
        all_original_domain_and_output_checks_retained=True,
        original_sum_order_retained=True, candidate_live_native_installed=False,
        compiler=base.ref(compiler), compiler_command=command, records=[])
    summary = args.outdir/'summary.json'
    base.write_json(summary, result)
    built = subprocess.run(command, capture_output=True)
    (args.outdir/'compiler.stdout').write_bytes(built.stdout)
    (args.outdir/'compiler.stderr').write_bytes(built.stderr)
    result['compiler_returncode'] = built.returncode
    if built.returncode != 0:
        base.write_json(summary, result)
        raise RuntimeError(built.stderr.decode(errors='replace'))
    result['candidate_native'] = base.ref(binary)
    helper = base.load_wire_helper(own/'parallel_native_batch.py')
    result['wire_helper'] = base.ref(own/'parallel_native_batch.py')
    record_path = args.native_runs/'0005-jac-record.json'
    record = json.loads(record_path.read_text())
    inp, oldout = base.verified(record['input']), base.verified(record['output'])
    wire, expected = inp.read_bytes(), oldout.read_bytes()
    shape = helper.split_wire(wire)
    indices, selection = base.choose_stages(wire, shape, record)
    result.update(original_record=base.ref(record_path), original_input=base.ref(inp),
        original_output=base.ref(oldout), selected_stages=indices, selection=selection)
    sample = args.outdir/'selected-input.bin'
    sample.write_bytes(base.subset_wire(wire, shape, indices))
    sample_shape = helper.split_wire(sample.read_bytes())
    sample_expected = base.subset_output(expected, shape, indices, sample_shape, helper)
    result['selected_input'] = base.ref(sample)
    for repetition in range(5):
        sequence = [('original', args.original_native), ('candidate', binary)]
        if repetition % 2:
            sequence.reverse()
        for name, executable in sequence:
            row = base.run_one(executable, sample, args.outdir/f'selected-{repetition}-{name}.bin',
                               sample_expected, helper)
            row.update(label=name, repetition=repetition, scope='selected_actual_M12_J_stages')
            result['records'].append(row)
            base.write_json(summary, result)
            print(json.dumps(row), flush=True)
            if not row['state_J_and_all_nontiming_diagnostics_byte_equal']:
                return 2
    if args.fallback_runs:
        path = args.fallback_runs/'0001-jac-record.json'
        fallback = json.loads(path.read_text())
        fp, fo = base.verified(fallback['input']), base.verified(fallback['output'])
        fw, fe = fp.read_bytes(), fo.read_bytes()
        fs = helper.split_wire(fw)
        fi = [0, fs['count']-1]
        fp2 = args.outdir/'nonpowerN-fallback-input.bin'
        fp2.write_bytes(base.subset_wire(fw, fs, fi))
        fexpected = base.subset_output(fe, fs, fi, helper.split_wire(fp2.read_bytes()), helper)
        row = base.run_one(binary, fp2, args.outdir/'nonpowerN-fallback-candidate.bin', fexpected, helper)
        row.update(label='candidate', scope='actual_nonpowerN_original_division_fallback',
                   original_record=base.ref(path), selected_stages=fi)
        result['records'].append(row)
        base.write_json(summary, result)
        if not row['state_J_and_all_nontiming_diagnostics_byte_equal']:
            return 2
    if args.full_replay:
        row = base.run_one(binary, inp, args.outdir/'all-stages-candidate-output.bin', expected, helper)
        row.update(label='candidate', scope='all_actual_M12_J_stages')
        result['records'].append(row)
        base.write_json(summary, result)
        if not row['state_J_and_all_nontiming_diagnostics_byte_equal']:
            return 2
    totals = {}
    for name in ('original', 'candidate'):
        rows = [r for r in result['records'] if r['label'] == name and
                r['scope'] == 'selected_actual_M12_J_stages']
        totals[name] = dict(user_seconds=sum(r['user_seconds'] for r in rows),
            cpu_seconds=sum(r['user_seconds']+r['system_seconds'] for r in rows),
            wall_seconds=sum(r['wall_seconds'] for r in rows))
    result.update(status='completed_all_requested_byte_comparisons',
        all_requested_nontiming_bytes_equal=True, timing=totals,
        candidate_to_original_cpu_ratio=totals['candidate']['cpu_seconds']/totals['original']['cpu_seconds'],
        ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    base.write_json(summary, result)
    print(json.dumps(dict(summary=str(summary), status=result['status'],
        cpu_ratio=result['candidate_to_original_cpu_ratio'])), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Compare only saved native and MP90 42-by-40 matrices, using exact rationals.

No mathematical evaluator/library, shared library, nonlinear flow, root,
derivative solver, tail or BVP is imported or run. The stored MP decimal
strings are a finite numerical reference, not exact mathematical derivatives.
"""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import sys
import time

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[4]
MP_RUN = WORK / 'closed_work/n4-mp90-variational-reference-v1'
LD_RUN = WORK / 'n4_work/native-longdouble-pair-v1'
LOCKS = {
    'mp_plan': (MP_RUN / 'plan.json', 'd4f43809f46fd06a79ac8afce95431fa13a4009268fe3a59e035db01d0af82b4'),
    'mp_summary': (MP_RUN / 'reference-summary.json', '07e09ac83186987a4622805b3a603efa7d4712e65d44c160ec29b115f646f550'),
    'mp_raw': (MP_RUN / 'reference-raw.json.gz', '4ad1e37379b6ffb98ae173f1176e7e228a8d0658b21e6cb9bc6fa08148db4316'),
    'mp_resource': (MP_RUN / 'resource.json', '803d799873ccadfc95b937b935b91d660549a80d8381a4d130cd345e383e399f'),
    'ld_plan': (LD_RUN / 'plan.json', 'b30bdac3396a3ba141b72d3ec0aa67c989cab5da2ef0602db82973acbfb3bd5b'),
    'ld_summary': (LD_RUN / 'readout-summary.json', '94f774a4ebac0c1dcad8f6de8e3796f4e6ab23475694e09acefb9fb7e4c86908'),
    'ld_raw': (LD_RUN / 'readout-raw.json.gz', '9853dc0ae370b775f2bf1441510884632a9afe2b1428b88f2f223d6947ca0b43'),
    'ld_resource': (LD_RUN / 'resource.json', '7c8b285074fad00270bc77cc1fb8c04cef7a4ddcf56da341bb340edf99f4ca0a'),
    'coefficients': (WORK / 'n4_work/parts32-frozen-mp-baseline-v1/capsule-coefficients.json.gz',
                     'e7152958611721905b239ad4bbdda10b54a58459a8dbd153fb02db159fde283a'),
}
STAGES = (43, 38, 175)
BLOCKS = {
    'all42_by40': (0, 42, 0, 40),
    'field40_by40': (0, 40, 0, 40),
    'Q_from_Q': (0, 20, 0, 20),
    'Q_from_pi': (0, 20, 20, 40),
    'pi_from_Q': (20, 40, 0, 20),
    'pi_from_pi': (20, 40, 20, 40),
    'first_mean_row40': (40, 41, 0, 40),
    'second_mean_row41': (41, 42, 0, 40),
}
DEFINITIONS = dict(
    reference='Each saved 98-digit MP90 decimal is interpreted as an exact decimal rational '
        'for this comparison. It remains a finite approximate variational reference.',
    native='Decode each canonical little-endian 10-byte x87 encoding as its exact binary rational.',
    boundary64='Interpret each saved boundary binary64 as its exact binary rational; independently '
        'verify it is the nearest-even conversion of the saved native value, including signed zero.',
    columns='Original stage input Q[0:20], pi[20:40]. No input-column port rescaling.',
    equation_rows='Q[0:20], pi[20:40], first mean[40], second mean[41].',
    physical_rows='Divide only output pi rows 20:40 by the exact binary64 portRatio. '
        'Q and both mean rows are unchanged. Apply the same row conversion to both matrices.',
    error='All differences, maxima and ratios are computed with Fraction, not floating summation.',
    max_absolute='Maximum absolute entry of candidate minus reference over the stated block.',
    global_relative='Block maximum absolute difference divided by the maximum absolute reference '
        'entry in that same block; this is not a componentwise relative error or induced operator norm.',
    zero_denominator='If reference max is zero, return 0 only when the difference is also zero; '
        'otherwise return null with denominator_zero=true. No artificial denominator floor.',
    peak='Zero-based row,column of the first lexicographic maximum nonzero difference; null when all zero.',
    display='Compact decimal strings use 32 significant digits, nearest rounding for presentation; '
        'they are not outward interval bounds. Exact rational differences/statistics stay in scratch.',
    scope='Native and MP variational matrices are evaluated along their respective approximate '
        'LD and MP90 trajectories and roots, with frozen capsule floor 0.1. The discrepancy includes '
        'trajectory/root differences. No derivative of the stopping algorithm, DN acceptance, '
        'matrix conditioning, continuous error or production floor 0.05 adaptor is asserted.',
    acceptance='No new numerical acceptance threshold. Report every prescribed block for all three stages.',
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def check(item):
    if sha(item['path']) != item['sha256']:
        raise ValueError('Changed saved input/source: ' + item['path'])


def load(path):
    path = Path(path)
    blob = path.read_bytes()
    return json.loads(gzip.decompress(blob) if path.suffix == '.gz' else blob)


def payload_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def write_json(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def frozen_files():
    files = {}
    for key, (path, digest) in LOCKS.items():
        item = dict(path=str(path), sha256=digest)
        check(item)
        files[key] = item
    return files


def prepare(directory):
    directory = Path(directory).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    files = frozen_files()
    plan = dict(schema='saved-native-mp90-variational-comparison-v1', source=ref(__file__),
        files=files, stages=list(STAGES), shape=[42, 40], blocks=BLOCKS,
        definitions=DEFINITIONS, output_prefix=str(directory / 'comparison'),
        metadata_only=True, derivative_or_nonlinear_evaluation=False, native_library_loaded=False)
    plan['identity_sha256'] = payload_sha(plan)
    path = directory / 'plan.json'
    write_json(path, plan)
    command = [sys.executable, str(Path(__file__).resolve()), '--run-plan', str(path)]
    write_json(directory / 'launch-command.json', dict(plan=ref(path), command=command))
    print(json.dumps(dict(plan=ref(path), command=command, numerical_evaluation=False)))


def decode80(hex_string, expected_count):
    blob = bytes.fromhex(hex_string)
    if len(blob) != expected_count*10:
        raise ValueError('Wrong canonical80 byte count')
    values, negative_zero = [], []
    for offset in range(0, len(blob), 10):
        significand, sign_exponent = struct.unpack('<QH', blob[offset:offset+10])
        exponent = sign_exponent & 0x7fff
        if exponent == 0x7fff:
            raise ValueError('Nonfinite native value')
        if (exponent and not significand >> 63) or (not exponent and significand >> 63):
            raise ValueError('Noncanonical x87 normal/subnormal encoding')
        shift = (exponent if exponent else 1)-16383-63
        value = Fraction(significand) * Fraction(2)**shift
        if sign_exponent & 0x8000:
            value = -value
        values.append(value)
        negative_zero.append(value == 0 and bool(sign_exponent & 0x8000))
    return values, negative_zero


def boundary_values(row):
    native, negative_zero = decode80(row['native_tangent_hex'], 42*40)
    double = row['tangent']
    assert len(double) == 42*40 and all(math.isfinite(v) for v in double)
    expected_bytes = bytes.fromhex(row['tangent64_hex'])
    actual_bytes = b''.join(struct.pack('<d', v) for v in double)
    assert actual_bytes == expected_bytes
    rounded = b''.join(struct.pack('<d', -0.0 if nz else float(v))
                       for v, nz in zip(native, negative_zero, strict=True))
    assert rounded == actual_bytes
    return native, [Fraction.from_float(v) for v in double]


def exact_metric(reference, difference, rectangle):
    i0, i1, j0, j1 = rectangle
    reference_max = Fraction(0)
    error_max = Fraction(0)
    peak = None
    for i in range(i0, i1):
        for j in range(j0, j1):
            reference_max = max(reference_max, abs(reference[i][j]))
            value = abs(difference[i][j])
            if value > error_max:
                error_max, peak = value, [i, j]
    relative = (error_max/reference_max if reference_max else
                Fraction(0) if not error_max else None)
    return dict(max_absolute_difference=str(error_max), maximum_absolute_reference=str(reference_max),
                global_relative_difference=None if relative is None else str(relative),
                denominator_zero=not bool(reference_max), peak_row_column=peak)


def displayed(value):
    if value is None:
        return None
    number = Fraction(value)
    if not number:
        return '0'
    with localcontext() as context:
        context.prec = 80
        return format(Decimal(number.numerator)/Decimal(number.denominator), '.32g')


def compact_metric(metric):
    return {key: displayed(value) if key in (
        'max_absolute_difference', 'maximum_absolute_reference', 'global_relative_difference')
        else value for key, value in metric.items()}


def physical(matrix, port):
    assert port > 0
    return [[v/port if 20 <= i < 40 else v for v in row] for i, row in enumerate(matrix)]


def reshape(flat):
    assert len(flat) == 1680
    return [flat[40*i:40*(i+1)] for i in range(42)]


def input_data(files):
    mp_plan, mp_summary, mp_raw = [load(files[k]['path']) for k in ('mp_plan', 'mp_summary', 'mp_raw')]
    ld_summary, ld_raw = [load(files[k]['path']) for k in ('ld_summary', 'ld_raw')]
    cap = load(files['coefficients']['path'])
    assert cap['root_rules']['floor'] == ld_raw['root_rules']['floor'] == 0.1
    assert ld_summary['root_rules'] == ld_raw['root_rules'] == cap['root_rules']
    assert ld_summary['raw'] == files['ld_raw'] and mp_summary['raw'] == files['mp_raw']
    assert ld_raw['coefficients'] == mp_plan['coefficients'] == files['coefficients']
    assert ld_raw['mp90_raw'] == mp_plan['saved_mp90_raw']
    for item in (ld_raw['mp90_raw'], ld_raw['original_input']):
        check(item)
    original = load(ld_raw['original_input']['path'])
    assert original['response']['checkpoint']['parameters']['projectionFloor'] == 0.05
    assert 'projectionFloor' not in original['config']
    for key in ('mp_resource', 'ld_resource'):
        resource = load(files[key]['path'])
        assert resource['status'] == 'observed_terminal' and resource['child_returncode'] == 0
    for mapping in (mp_plan['source_sha256'], mp_plan['mpmath_sources']):
        for path, digest in mapping.items():
            check(dict(path=path, sha256=digest))
    for item in ld_raw['files'].values():
        check(item)
    for item in ld_raw['sources'].values():
        check(item)
    assert mp_summary['source'] == mp_raw['source'] == mp_plan['source']
    assert mp_summary['plan'] == mp_raw['plan'] == files['mp_plan']
    assert ld_summary['source'] == ld_raw['source']
    assert ld_summary['plan'] == ld_raw['plan'] == files['ld_plan']
    assert mp_raw['derivative_dps'] == 90 and mp_raw['mpmath_version'] == '1.3.0'
    assert [row['stage'] for row in mp_raw['rows']] == list(STAGES)
    assert [(row['stage'], row['with_jac']) for row in ld_raw['rows']] == [
        (stage, flag) for stage in STAGES for flag in (False, True)]
    for row, item in zip(ld_raw['rows'], ld_summary['named_results'], strict=True):
        check(item['checkpoint'])
        checkpoint = load(item['checkpoint']['path'])
        assert checkpoint['row'] == row
        assert {k: v for k, v in checkpoint.items() if k != 'row'} == {
            k: v for k, v in ld_raw.items() if k != 'rows'}
    for row, item in zip(mp_raw['rows'], mp_summary['named_results'], strict=True):
        check(item['stage_checkpoint'])
        assert load(item['stage_checkpoint']['path'])['row'] == row
        assert row['tangent_serialization_sha256'] == payload_sha(row['tangent42_by40'])
    return mp_plan, mp_raw, ld_raw, cap


def run(plan_path):
    began = time.monotonic()
    plan_path = Path(plan_path).resolve()
    plan = load(plan_path)
    identity = plan.pop('identity_sha256')
    assert payload_sha(plan) == identity
    plan['identity_sha256'] = identity
    assert plan['source'] == ref(__file__)
    assert plan['stages'] == list(STAGES) and plan['shape'] == [42, 40]
    assert plan['definitions'] == DEFINITIONS
    assert plan['blocks'] == {k: list(v) for k, v in BLOCKS.items()}
    assert plan['files'] == frozen_files()
    mp_plan, mp_raw, ld_raw, cap = input_data(plan['files'])
    prefix = Path(plan['output_prefix'])
    raw_path, summary_path = Path(str(prefix)+'-raw.json.gz'), Path(str(prefix)+'-summary.json')
    if raw_path.exists() or summary_path.exists():
        raise FileExistsError('Do not overwrite the comparison')
    raw_rows, compact_rows = [], []
    for index, stage in enumerate(STAGES):
        mp_row = mp_raw['rows'][index]
        simple, ld_row = ld_raw['rows'][2*index:2*index+2]
        assert simple['stage'] == ld_row['stage'] == mp_row['stage'] == stage
        assert simple['native_state_hex'] == ld_row['native_state_hex']
        assert simple['state64_hex'] == ld_row['state64_hex']
        assert ld_row['diagnostics']['root_calls'] == 64
        fixture = cap['fixtures'][index]
        assert fixture['stage'] == stage
        port = Fraction.from_float(float(fixture['portRatio']))
        assert len(mp_row['tangent42_by40']) == 42
        assert all(len(row) == 40 for row in mp_row['tangent42_by40'])
        reference = [[Fraction(v) for v in row] for row in mp_row['tangent42_by40']]
        native_flat, boundary_flat = boundary_values(ld_row)
        raw_result = dict(stage=stage, portRatio_exact=str(port),
            input_columns_rescaled=False, original_input_identity=fixture['input42_sha256'],
            saved_MP_trajectory=mp_row['saved_trajectory_identity'], comparisons={})
        compact_result = dict(stage=stage, portRatio_exact=str(port),
            equation_and_physical_coordinates_identical=(port == 1), comparisons={})
        for precision, flat in (('native80', native_flat), ('boundary64', boundary_flat)):
            candidate = reshape(flat)
            difference = [[candidate[i][j]-reference[i][j] for j in range(40)] for i in range(42)]
            frames = {}
            compact_frames = {}
            for frame in ('equation', 'physical_output'):
                ref_matrix = reference if frame == 'equation' else physical(reference, port)
                diff_matrix = difference if frame == 'equation' else physical(difference, port)
                exact_stats = {name: exact_metric(ref_matrix, diff_matrix, rectangle)
                               for name, rectangle in BLOCKS.items()}
                serial = [[str(v) for v in row] for row in diff_matrix]
                frames[frame] = dict(difference42_by40=serial, statistics=exact_stats,
                                     difference_serialization_sha256=payload_sha(serial))
                compact_frames[frame] = {name: compact_metric(value) for name, value in exact_stats.items()}
            raw_result['comparisons'][precision] = frames
            if port == 1:
                assert frames['equation'] == frames['physical_output']
                compact_result['comparisons'][precision] = dict(
                    equation_and_physical_output=compact_frames['equation'])
            else:
                compact_result['comparisons'][precision] = compact_frames
        raw_rows.append(raw_result)
        compact_rows.append(compact_result)
    raw = dict(plan=ref(plan_path), source=ref(__file__), definitions=DEFINITIONS,
               rows=raw_rows, new_derivative_or_flow_evaluations=0, native_library_loaded=False,
               input_matrix_entries_per_precision=5040)
    with raw_path.open('xb') as stream:
        stream.write(gzip.compress((json.dumps(raw, separators=(',', ':'), allow_nan=False)+'\n').encode(), mtime=0))
    result = dict(classification='Numerical evidence: exact rational comparison of saved finite matrices.',
        plan=ref(plan_path), source=ref(__file__), inputs=plan['files'], raw=ref(raw_path),
        command=[sys.executable, str(Path(__file__).resolve()), '--run-plan', str(plan_path)],
        definitions=DEFINITIONS, named_results=compact_rows,
        compared_stages=3, entries_per_precision=5040, precision_views=['native80', 'boundary64'],
        blocks=BLOCKS, domain_floor=0.1, production_checkpoint_floor=0.05,
        no_input_column_scaling=True, complete_matrices_preserved_in_scratch=True,
        exact_rational_matrix_differences=True, derivative_or_nonlinear_evaluations=0,
        shared_library_loaded=False, tail_or_BVP_invoked=False, acceptance_threshold_added=False,
        continuous_error_bound=False, seconds=time.monotonic()-began)
    write_json(summary_path, result)
    print(json.dumps(dict(summary=ref(summary_path), raw=ref(raw_path),
                          new_derivative_or_flow_evaluations=0, compared_entries_per_precision=5040)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--prepare', type=Path)
    group.add_argument('--run-plan', type=Path)
    args = parser.parse_args()
    if args.prepare is not None:
        prepare(args.prepare)
    else:
        run(args.run_plan)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""R276 exact affine infinity predictions from an already saved native ledger.

Actions-only scientific arithmetic, not a byte-only auditor.  The complete
signed e=A*delta+r ledger, the saved original r, and the actual positive
binary64 sigma determine every affine prediction without another matrix
action, RHS, J, ODE, QR, optimizer, or nonlinear trial.  The original ten
steps are read back; none is added or used as a new acceptance gate.

The input is an existing, upstream-verified public native61 or native73
artifact extraction.  This program neither downloads nor mutates it.
Large J/factor payloads are not read here: their complete source/hash
bindings remain explicit, and their byte audit is a separate operation.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
import gzip
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import time
import traceback


HERE = Path(__file__).resolve().parent
REPOSITORY = 'Rogerhu12/math-research-public'
SCHEMA = 'complete-native-saved-ledger-exact-affine-infinity-diagnostic-v1'
UNIT_EXPONENT = -2148
M, K, DEPTH, ROWS = 112, 224, 576, 129248
MAX_JSON_BYTES = 128 * 1024 * 1024
MAX_LEDGER_LINE_BYTES = 2 * 1024 * 1024
CORE_SHA = 'ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3'
RUNTIME_SHA = 'f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f'
EVALUATE_SHA = '9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9'
INTERNAL_SOLVE_SHA = 'd7d063fe2fca25c1742c68ec8056902a583952b61cdda98e1d9eaab7c09f3615'
TRIAL_SHA = '603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99'
FACTOR_NAME = 'exact_20261114_native_damped_chain_qr.py'
FACTOR_SHA = '9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33'
KERNEL_NAME = 'exact_20261114_native_allrows_dyadic_residual.py'
KERNEL_SHA = '0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
BYTE_NAME = 'geometry_20261114_native_captured_band_correction.py'
BYTE_SHA = 'b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
FLOW_NAME = 'geometry_20261114_noj_matched_variational_engine.mjs'
FLOW_SHA = 'f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9'
MODEL_SCOPE = 'R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates'
SHAPES = {
    'base-states': [577, 224], 'stage-residuals': [576, 224], 'stage-out': [576, 224],
    'original-scales': [1, 577], 'cut-residual': [1, 112], 'end-residual': [1, 112],
    'original-far-graph': [1, 112], 'physical-height': [1, 112], 'cut-target': [1, 112],
    'stage-jacobians': [576, 224, 224]}
INPUT_NAMES = tuple(name for name in SHAPES if name != 'stage-jacobians')
PROFILES = {
    'native61': dict(
        run='43645948199', commit='cf6b51193255dfc713610d2919598451ccdd49e2',
        directory='native-current576-damped',
        launcher='geometry_20261114_native_current576_damped_solve.py',
        launcher_sha='06b8c44c115fcf754e963aeeb3adc04a26500cade3817018bae50e2e50aebc3b',
        hook='geometry_20261114_native_current576_damped_solve_hook.mjs',
        hook_sha='0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc',
        system='exact_20261114_current576_damped_system.py',
        system_sha='695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90',
        producer='exact_20261114_current576_damped_chain_qr.py',
        producer_sha='ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f',
        outer='native-current576-damped-solve-result-v1',
        bridge='native-current576-damped-correction-bridge-summary-v1',
        snapshot='current-native576-withJ-snapshot-result-v1',
        context='current-native576-withJ-snapshot-context-v1',
        snapshot_arrays='current-native576-withJ-snapshot-arrays-v1',
        core='current-native576-correction-only-core-instrumentation-v1',
        qr='complete-native-current576-damped-square-root-direction-v1',
        binding='current-native576-complete-linear-system-binding-v1',
        output_arrays='complete-native-current576-damped-direction-arrays-v1',
        exact='current-native576-complete-exact-direction-readback-v1',
        matrix_scope='fresh-current-native576-finite-binary64-complete-J-r-sigma-chain',
        parent_key='parent_selected59', new_flow=False),
    'native73': dict(
        run='43657001633', commit='9515d5aaf7c68f8efd366438d6bd81ce73c3486f',
        directory='native-noj-primal-current576-damped',
        launcher='geometry_20261114_noj_primal_current576_damped_solve.py',
        launcher_sha='938fbec22f0733fff6ceb22e6e9b7a9e12942c12d1eae31c608d8f517702df8c',
        hook='geometry_20261114_noj_primal_current576_damped_solve_hook.mjs',
        hook_sha='099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d',
        system='exact_20261114_noj_primal_current576_damped_system.py',
        system_sha='48297483617c56179fdd4d6b80e9aeeb1151bf89c90fd816ca41d2e3ccc0bcb3',
        producer='exact_20261114_noj_primal_current576_damped_chain_qr.py',
        producer_sha='70bc10dfb31717b662265485d10a15028365dbba5db85ccf9c8f592226e33955',
        outer='native-noj-primal-current576-damped-solve-result-v1',
        bridge='native-noj-primal-current576-damped-correction-bridge-summary-v1',
        snapshot='noj-primal-current-native576-withJ-snapshot-result-v1',
        context='noj-primal-current-native576-current-point-context-v1',
        snapshot_arrays='noj-primal-current-native576-snapshot-arrays-v1',
        core='noj-primal-current-native576-correction-only-core-instrumentation-v1',
        qr='complete-native-noj-primal-current576-damped-square-root-direction-v1',
        binding='noj-primal-current-native576-complete-linear-system-binding-v1',
        output_arrays='complete-native-noj-primal-current576-damped-direction-arrays-v1',
        exact='noj-primal-current-native576-complete-exact-direction-readback-v1',
        matrix_scope='fresh-noJ-primal-current-native576-finite-binary64-complete-J-r-sigma-chain',
        parent_key='parent_failed61', new_flow=True)}


class InputError(RuntimeError):
    pass


def require(condition, label):
    if not condition:
        raise InputError(label)


def require_actions():
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and
            os.environ.get('GITHUB_REPOSITORY') == REPOSITORY,
            'Scientific exact affine diagnostics run only in this public repository Actions')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def valid_sha(value, label):
    require(isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value), label)
    return value


def canonical_sha(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())


def same_fields(actual, expected, label):
    require(isinstance(actual, dict), label + ': object required')
    for key, value in expected.items():
        require(key in actual and actual[key] == value, label + ': ' + key)


def source_receipts(profile):
    pins = {profile[key]: profile[key + '_sha'] for key in ('launcher', 'hook', 'system', 'producer')}
    pins.update({FACTOR_NAME: FACTOR_SHA, KERNEL_NAME: KERNEL_SHA, BYTE_NAME: BYTE_SHA})
    if profile['new_flow']:
        pins[FLOW_NAME] = FLOW_SHA
    result = []
    for name, expected in pins.items():
        path = HERE / name
        require(path.is_file() and not path.is_symlink(), 'Frozen source file required: ' + name)
        require(digest(path) == expected, 'Frozen source SHA: ' + name)
        result.append(dict(file=name, bytes=path.stat().st_size, sha256=expected))
    return result


def json_bytes(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(',', ':'), allow_nan=False) + '\n').encode()


def write_json(root, name, value, compressed=False):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json_bytes(value)
    if compressed:
        raw = gzip.compress(raw, mtime=0)
    with path.open('xb') as stream:
        stream.write(raw)
    return dict(file=name, bytes=len(raw), sha256=sha(raw))


class Files:
    def __init__(self, root):
        self.root = Path(root).resolve(strict=True)
        require(self.root.is_dir(), 'Input directory required')
        self.seen = {}
        self.stats = {}

    def path(self, name):
        require(isinstance(name, str) and '\\' not in name and '\x00' not in name,
                'Safe relative POSIX file name required')
        parts = PurePosixPath(name)
        require(not parts.is_absolute() and parts.parts and
                all(piece not in ('', '.', '..') for piece in parts.parts) and parts.as_posix() == name,
                'No absolute, parent, or noncanonical relative path')
        path = self.root
        for part in parts.parts:
            path = path / part
            require(not path.is_symlink(), 'Input symbolic links are not accepted')
        require(path.is_file() and path.resolve().is_relative_to(self.root), 'Regular contained input file required')
        return path

    def info(self, name):
        path = self.path(name)
        stat = path.stat()
        observed = (stat.st_size,stat.st_mtime_ns,stat.st_ino,stat.st_dev)
        if name in self.stats:
            require(self.stats[name] == observed, 'Input artifact is immutable while it is read: ' + name)
        if name not in self.seen:
            self.seen[name] = dict(file=name, bytes=path.stat().st_size, sha256=digest(path))
            self.stats[name] = observed
        return self.seen[name]

    def check(self, descriptor):
        require(isinstance(descriptor, dict), 'File descriptor required')
        valid_sha(descriptor.get('sha256'), 'File descriptor SHA')
        require(type(descriptor.get('bytes')) is int and descriptor['bytes'] >= 0, 'File descriptor bytes')
        receipt = self.info(descriptor['file'])
        same_fields(descriptor, receipt, 'Complete actual file bytes/SHA')
        return self.path(descriptor['file'])

    def raw(self, descriptor):
        raw = self.check(descriptor).read_bytes()
        require(len(raw)==descriptor['bytes'] and sha(raw)==descriptor['sha256'],
                'The consumed original raw bytes equal the bound descriptor')
        return raw

    def obj(self, descriptor):
        path = self.check(descriptor)
        with path.open('rb') as source:
            magic = source.read(2)
        opener = gzip.open if magic == b'\x1f\x8b' else open
        with opener(path, 'rb') as stream:
            raw = stream.read(MAX_JSON_BYTES + 1)
        require(len(raw) <= MAX_JSON_BYTES, 'Bounded metadata object required; exact ledger is streamed separately')
        return json.loads(raw)

    def json(self, name):
        return self.obj(self.info(name))


def word_of_number(value, label):
    require(type(value) in (float, int) and math.isfinite(value), label + ': finite JSON numeric value required')
    return int.from_bytes(struct.pack('<d', value), 'little')


def word_hex(word):
    return struct.pack('<Q', word).hex()


def number_record(record, label, finite=True):
    require(isinstance(record, dict) and isinstance(record.get('float64le_hex'), str) and
            re.fullmatch('[0-9a-f]{16}', record['float64le_hex']), label + ': numberRecord bits')
    word = int.from_bytes(bytes.fromhex(record['float64le_hex']), 'little')
    exponent = (word >> 52) & 2047
    fraction = word & ((1 << 52) - 1)
    classification = ('NaN' if fraction else ('negative-infinity' if word >> 63 else 'positive-infinity')) \
        if exponent == 2047 else ('negative-zero' if word == (1 << 63) else 'finite')
    require(record.get('classification') == classification, label + ': exact classification')
    if exponent == 2047:
        require(not finite and record.get('value') is None, label + ': nonfinite metadata only')
    else:
        parsed = word_of_number(record.get('value'), label)
        require(parsed == word or (word == (1 << 63) and parsed == 0), label + ': JSON value and signed-zero bits')
    return word


def unit_from_word(word):
    """Actions arithmetic: exact finite binary64 real in units of2^-2148."""
    exponent = (word >> 52) & 2047
    require(exponent != 2047, 'Finite original scalar required by exact real model')
    mantissa = word & ((1 << 52) - 1)
    power = -1074
    if exponent:
        mantissa |= 1 << 52
        power = exponent - 1075
    if word >> 63:
        mantissa = -mantissa
    return mantissa << (power - UNIT_EXPONENT)


def exact_integer(encoded):
    """Read, do not recompute, the kernel's canonical signed dyadic value."""
    require(isinstance(encoded, list) and len(encoded) == 2 and isinstance(encoded[0], str) and
            type(encoded[1]) is int, 'Canonical saved exact dyadic pair')
    require(re.fullmatch(r'-?0x[0-9a-f]+', encoded[0]) and len(encoded[0]) <= 1060,
            'Bounded hexadecimal exact row coefficient')
    coefficient = int(encoded[0], 16)
    require(hex(coefficient) == encoded[0], 'Canonical coefficient text')
    if coefficient == 0:
        require(encoded == ['0x0', 0], 'Canonical zero exact row')
        return 0
    shift = encoded[1] - UNIT_EXPONENT
    require(coefficient & 1 and 0 <= shift <= 4204 and coefficient.bit_length() + shift <= 4204,
            'Canonical finite224-product kernel range; not a numerical threshold')
    return coefficient << shift


def compact(value):
    if value == 0:
        return ['0x0', 0]
    trailing = (abs(value) & -abs(value)).bit_length() - 1
    return [hex(value >> trailing), UNIT_EXPONENT + trailing]


def rational(numerator, denominator):
    require(denominator > 0, 'Positive exact rational denominator')
    divisor = math.gcd(abs(numerator), denominator)
    n, d = numerator // divisor, denominator // divisor
    with localcontext() as context:
        context.prec = 72
        display = format(Decimal(n) / Decimal(d), '.63E')
    return dict(numerator=str(n), denominator=str(d), decimal_display_64_significant_digits=display,
                display_never_used_for_comparison=True, display_is_not_an_interval_enclosure=True)


def fraction_parts(record):
    n, d = int(record['numerator']), int(record['denominator'])
    require(d > 0, 'Saved exact fraction denominator')
    return n, d


def compare(an, ad, bn, bd):
    left, right = an * bd, bn * ad
    return (left > right) - (left < right)


def relation(sign):
    return 'less' if sign < 0 else 'equal' if sign == 0 else 'greater'


def row_coordinate(kind, node, row):
    global_row = row if kind == 'cut' else M + node * K + row if kind == 'stage' else M + DEPTH * K + row
    return dict(kind=kind, node=node, row=row, global_equation_row=global_row,
        component=('Q' if row < M else 'Pi') if kind == 'stage' else 'Q' if kind == 'cut' else 'Pi-minus-original-GQ',
        mode=(row % M) + 1 if kind == 'stage' else row + 1)


def maxima_update(current, numerator, denominator, coordinate, payload):
    if current is None or compare(abs(numerator), denominator, abs(current['n']), current['d']) > 0:
        return dict(n=numerator, d=denominator, coordinate=coordinate, payload=payload, ties=1)
    if compare(abs(numerator), denominator, abs(current['n']), current['d']) == 0:
        current['ties'] += 1
        if coordinate['global_equation_row'] < current['coordinate']['global_equation_row']:
            current.update(n=numerator, d=denominator, coordinate=coordinate, payload=payload)
    return current


def public_maximum(item):
    require(item is not None, 'A complete finite nonempty row set has a maximum')
    return dict(**item['coordinate'], **item['payload'],
        exact_signed_scaled_value=rational(item['n'], item['d']),
        exact_absolute_scaled_value=rational(abs(item['n']), item['d']),
        maximizing_rows=item['ties'], tie_rule='smallest original global equation row')


def match_saved_maximum(computed, saved, label):
    for key in ('kind', 'node', 'row', 'global_equation_row', 'component', 'mode'):
        require(saved[key] == computed['coordinate'][key], label + ': original row coordinate ' + key)
    require(saved['original_sigma_float64le_hex']==computed['payload']['original_sigma_float64le_hex'] and
            exact_integer(saved['exact_unscaled_dyadic'])==computed['n'],
            label+': actual original sigma bits and exact unscaled endpoint row')
    n, d = fraction_parts(saved['exact_signed_scaled_residual'])
    require(compare(computed['n'], computed['d'], n, d) == 0, label + ': signed exact stored ratio')
    n, d = fraction_parts(saved['exact_absolute_scaled_residual'])
    require(compare(abs(computed['n']), computed['d'], n, d) == 0, label + ': absolute exact stored ratio')


def core_contract(files, descriptor, profile):
    core = files.obj(descriptor)
    same_fields(core, dict(schema=profile['core'], source_sha256=profile['launcher_sha'],
        hook_sha256=profile['hook_sha'], original_core_file_sha256=CORE_SHA,
        original_runtime_core_sha256=RUNTIME_SHA, original_evaluate_source_sha256=EVALUATE_SHA,
        actual_evaluate_source_sha256=EVALUATE_SHA, original_ten_trial_body_sha256=TRIAL_SHA,
        instrumented_ten_trial_body_sha256=TRIAL_SHA, exact_correction_call_roundtrip_verified=True,
        original_evaluate_body_byte_identical=True, original_ten_trial_body_byte_identical=True,
        no_cached_baseline=True, no_planned_one_step_stop=True), 'Original evaluation/ten-trial contract')
    inside = core['internal_solve_source_identity']
    before = inside['original_internal_solve_source']
    after = inside['instrumented_internal_solve_source']
    change = inside['replacement']
    require(sha(before.encode()) == inside['original_internal_solve_source_sha256'] == INTERNAL_SOLVE_SHA,
            'Exact original internal solve source')
    require(sha(after.encode()) == inside['instrumented_internal_solve_source_sha256'] and
            change['before'] == 'const cor=correction(ev,states,target);' and
            before.count(change['before']) == after.count(change['after']) == 1 and
            after.replace(change['after'], change['before'], 1) == before, 'Only original correction call replaced inside solve')
    start = '   for(let k=0;k<10;k++){'
    end = '   if(!accepted)throw new Error("multiple-shooting line search failed at "+ev.norm);'
    require(before.count(start) == before.count(end) == 1, 'Unique original ten-alpha source slice')
    body = before[before.index(start):before.index(end)]
    require(sha(body.encode()) == TRIAL_SHA and 'const lambda=2**(-k)' in body and
            'v+lambda*cor.delta[n][j]' in body and 'test=evaluate(trial,target,false,scales)' in body and
            'if(test.norm<ev.norm)' in body, 'Original alpha/state arithmetic/noJ/strict comparison remain identified')
    if profile['new_flow']:
        same_fields(core, dict(only_core_nonlinear_correction_call_replaced=True,
            independent_withJ_flow_property_also_replaced=True,
            core_scope_does_not_claim_old_withJ_identity=True), 'Honest new-flow scope')
    else:
        same_fields(core, dict(only_nonlinear_correction_call_replaced=True), 'Native61 original-flow scope')
    return dict(receipt=descriptor, original_core_file_sha256=CORE_SHA, original_runtime_core_sha256=RUNTIME_SHA,
                original_evaluate_source_sha256=EVALUATE_SHA, original_ten_trial_body_sha256=TRIAL_SHA,
                spec_sha256=core['spec_sha256'], original_ten_alphas=[dict(k=k, numerator=1, denominator=1 << k)
                    for k in range(10)], source_normalization='cut:sigma0; stage n:sigma_n; far:sigma576')


def manifest_map(value, key):
    rows = value['arrays']
    require(isinstance(rows, list), 'Array manifest list')
    result = {}
    for row in rows:
        require(isinstance(row, dict) and row[key] not in result, 'Distinct array manifest aliases')
        result[row[key]] = row
    return result


def load_native(args, profile, files):
    """Bind a finished producer or explicitly hash-pinned partial journals."""
    root_receipts = {}
    if args.native_result_sha256:
        info = files.info('result.json')
        require(info['sha256'] == valid_sha(args.native_result_sha256, 'Actual native result SHA'),
                'Actual native result file identity')
        outer = files.obj(info)
        same_fields(outer, dict(schema=profile['outer'], source_sha256=profile['launcher_sha'],
            hook_sha256=profile['hook_sha'], current_direction_source_sha256=profile['producer_sha'],
            current_system_source_sha256=profile['system_sha'], factor_engine_source_sha256=FACTOR_SHA,
            original_native_requests=1, original_max_iterations=32), 'Original native producer')
        root_receipts = {item['file']: item for item in outer['small_output_files']}
        require(len(root_receipts) == len(outer['small_output_files']), 'Unique original small-output descriptors')
        bridge = files.obj(outer['current_correction_summary'])
        same_fields(bridge, dict(schema=profile['bridge'], source_sha256=profile['launcher_sha'],
            hook_sha256=profile['hook_sha'], spec_sha256=outer['spec_sha256'], native_call=1,
            current_direction_source_sha256=profile['producer_sha'], current_system_source_sha256=profile['system_sha']),
            'Original completed correction summary')
        records_desc = root_receipts.get('current-corrections.jsonl')
        if bridge['iterations']:
            require(records_desc is not None, 'Every returned iteration has its original journal')
            records = read_jsonl(files, records_desc)
            require(records == bridge['iterations'], 'Final bridge and original correction journal agree')
        else:
            records = []
        require(bridge['snapshots_completed'] == outer['fresh_withJ_snapshots'] and
                bridge['directions_returned'] == outer['current_R273_directions_returned'], 'Original correction counts')
        trial_desc = root_receipts.get('native_trials.jsonl')
        trials = read_jsonl(files, trial_desc) if trial_desc is not None else []
        scope = dict(mode='original-result', original_result=info,
            original_correction_summary=outer['current_correction_summary'],
            original_correction_journal=records_desc, original_trial_journal=trial_desc,
            original_native_accepted=outer.get('native_accepted'),
            original_failure_message=outer.get('actual_original_failure_message'),
            original_actual_error=outer.get('actual_error'), original_tolerance=outer.get('original_tolerance'),
            original_max_iterations=outer['original_max_iterations'], original_producer_outcome_not_changed=True)
    else:
        require(args.partial_records_sha256 is not None, 'Choose a full result or explicit partial journal identity')
        desc = files.info('current-corrections.jsonl')
        require(desc['sha256'] == valid_sha(args.partial_records_sha256, 'Actual partial journal SHA'), 'Partial journal identity')
        records = read_jsonl(files, desc)
        if args.partial_trials_sha256:
            td = files.info('native_trials.jsonl')
            require(td['sha256'] == valid_sha(args.partial_trials_sha256, 'Actual partial trial journal SHA'),
                    'Partial trial journal identity')
            trials = read_jsonl(files, td)
        else:
            require(not (files.root / 'native_trials.jsonl').exists(), 'An existing partial trial journal needs its explicit SHA')
            td, trials = None, []
        outer = None
        scope = dict(mode='explicit-partial-journals', original_result=None,
            original_correction_journal=desc, original_trial_journal=td, original_native_accepted=None,
            native_terminal_outcome_not_available_from_this_mode=True,
            partial_journals_not_relabelled_as_complete_native_artifact=True)
    require(len(records) <= 32, 'Original maximum correction count')
    for i, record in enumerate(records):
        same_fields(record, dict(native_call=1, nonlinear_iteration=i, snapshot_sequence=i,
            iteration_directory='iteration-' + str(i).zfill(3)), 'Actual ordered correction journal')
    grouped = {}
    for trial in trials:
        require(type(trial.get('iteration')) is int and 0 <= trial['iteration'] < 32 and
                trial.get('call') == 1, 'Original trial call/iteration identity')
        grouped.setdefault(trial['iteration'], []).append(trial)
    for iteration, rows in grouped.items():
        require(iteration < len(records) and records[iteration].get('linear_direction_returned') is True,
                'Actual trials follow a recorded returned complete direction')
        require(len(rows) <= 10 and [row['trial'] for row in rows] == list(range(len(rows))), 'Original ordered trial prefix')
        accepted = [i for i, row in enumerate(rows) if row.get('kind') == 'accepted']
        require(not accepted or accepted == [len(rows) - 1], 'Original trial loop stops at first acceptance')
    return scope, records, grouped, outer


def read_jsonl(files, descriptor):
    path = files.check(descriptor)
    values = []
    with path.open('rb') as stream:
        for line in stream:
            require(len(line) <= MAX_LEDGER_LINE_BYTES, 'Bounded journal line')
            if line.strip():
                values.append(json.loads(line))
    return values


def bind_iteration(native, record, profile, outer):
    """Only metadata and the actual non-J operands are read, never a J action."""
    i = record['nonlinear_iteration']
    require(record.get('snapshot_completed') is True and record.get('linear_direction_returned') is True,
            'A complete returned original direction is needed for prediction')
    require(record['qr_exit']['status'] == 0 and record['qr_exit'].get('error') is None,
            'Original child actually returned successfully')
    native.check(record['snapshot'])
    s = Files(native.root / record['iteration_directory'] / 'snapshot')
    q = Files(native.root / record['iteration_directory'] / 'qr')
    snapshot_receipt = s.info('result.json')
    require(snapshot_receipt['sha256'] == record['snapshot']['sha256'] and
            snapshot_receipt['bytes'] == record['snapshot']['bytes'], 'Bridge snapshot bytes')
    snapshot = s.obj(snapshot_receipt)
    same_fields(snapshot, dict(schema=profile['snapshot'], snapshot_completed=True,
        source_sha256=profile['launcher_sha'], hook_sha256=profile['hook_sha'], native_call=1,
        nonlinear_iteration=i, snapshot_sequence=i, M=M, K=K, depth=DEPTH), 'This current original snapshot')
    context = s.obj(snapshot['context'])
    sman = s.obj(snapshot['manifest'])
    same_fields(context, dict(schema=profile['context'], source_sha256=profile['launcher_sha'],
        hook_sha256=profile['hook_sha'], native_call=1, nonlinear_iteration=i, snapshot_sequence=i,
        fresh_current_evaluate_completed=True, no_cached_baseline=True, snapshot_does_not_call_RHS_J_ODE=True),
        'Current context identity')
    same_fields(sman, dict(schema=profile['snapshot_arrays'], source_sha256=profile['launcher_sha'],
        hook_sha256=profile['hook_sha'], native_call=1, nonlinear_iteration=i, snapshot_sequence=i,
        M=M, K=K, depth=DEPTH), 'Complete current snapshot manifest')
    arrays = manifest_map(sman, 'name')
    require(set(arrays) == set(SHAPES), 'All ten original arrays retain their full scope')
    for name, shape in SHAPES.items():
        item = arrays[name]
        same_fields(item, dict(shape=shape, dtype='<f8', order='C', completed=True,
            total_bytes=8 * math.prod(shape), raw_sha256=context['raw_array_sha256'][name]), 'Current full array ' + name)
        valid_sha(item['raw_sha256'], 'Full array hash')
        expected_row = 0
        for j, chunk in enumerate(item['chunks']):
            same_fields(chunk, dict(array=name, chunk_index=j, row_start=expected_row), 'Complete original chunk order')
            stop = chunk['row_stop']
            require(type(stop) is int and expected_row < stop <= shape[0] and
                    chunk['bytes'] == (stop - expected_row) * math.prod(shape[1:]) * 8,
                    'Original complete chunk shape')
            valid_sha(chunk['sha256'], 'Original chunk file SHA')
            require(chunk['sha256'] == chunk['raw_sha256'], 'Original snapshot chunks are raw binary64 files')
            expected_row = stop
        require(expected_row == shape[0], 'Full original array chunk coverage')
    require(context['rawNode'] == [0,72,144,216,288,360,432,504,576] and len(context['cells']) == DEPTH,
            'Original physical-node map and all current stages')
    core = core_contract(s, context['core_instrumentation'], profile)
    if outer is not None:
        require(core['spec_sha256'] == outer['spec_sha256'] and context[profile['parent_key']] == outer[profile['parent_key']],
                'Current snapshot belongs to original native parent/specification')
    for label in ('norm', 'minA', 'minD'):
        rec = context['current_original_' + label]
        require(rec == snapshot['actual_current_original_' + label], 'Original current scalar alias ' + label)
        number_record(rec, 'Current ' + label, finite=(label == 'norm'))
    require(context['current_original_norm'] == record['source_current_withJ_norm'], 'Actual trial baseline is this fresh withJ')
    direction = record['direction']
    qr = q.obj(direction['result'])
    identity = dict(snapshot_result=snapshot_receipt, native_call=1, nonlinear_iteration=i,
                    snapshot_sequence=i, current_state_sha256=arrays['base-states']['raw_sha256'])
    require(identity['current_state_sha256'] == record['current_state_sha256'] == snapshot['current_state_sha256'],
            'Actual current complete state byte identity')
    same_fields(qr, dict(schema=profile['qr'], source_sha256=profile['producer_sha'],
        system_source_sha256=profile['system_sha'], factor_engine_source_sha256=FACTOR_SHA,
        kernel_source_sha256=KERNEL_SHA, model_scope=MODEL_SCOPE, diagnostic_completed=True,
        linear_direction_computed=True, original_native_calls_in_this_child=0,
        new_RHS_calls_in_this_child=0, new_J_calls_in_this_child=0, new_ODE_steps_in_this_child=0,
        nonlinear_trials_in_this_child=0, exact_linear_defect_not_used_as_new_native_trial_gate=True,
        **identity), 'Current returned R273 direction producer')
    number_record(qr['eta_binary64'],'Original explicit algorithm eta')
    if outer is not None:
        require(qr['eta_cli_text']==outer['eta_cli_text'] and qr['eta_binary64']==outer['eta_binary64'],
                'The actual child retains this native request algorithm eta')
    for dkey, rkey in (('input_binding','input_binding'), ('direction_checkpoint','native_direction_checkpoint'),
                       ('array_manifest','array_manifest'), ('native_delta','native_delta')):
        require(direction[dkey] == qr[rkey], 'Original returned direction descriptor ' + dkey)
    same_fields(direction, dict(**identity, new_matrix_identity_sha256=qr['new_matrix_identity_sha256'],
        no_cut_or_far_projection=True, no_extra_L2_or_exact_defect_acceptance_gate=True), 'Actual returned original direction')
    binding = q.obj(qr['input_binding'])
    matrix = valid_sha(binding['new_matrix_identity_sha256'], 'Current complete matrix identity')
    same_fields(binding, dict(schema=profile['binding'], matrix_scope=profile['matrix_scope'],
        adapter_source_sha256=profile['system_sha'], frozen_byte_io_source_sha256=BYTE_SHA,
        snapshot_result_sha256=snapshot_receipt['sha256'], snapshot_context_sha256=snapshot['context']['sha256'],
        snapshot_manifest_sha256=snapshot['manifest']['sha256'], modes=M, shape_dimension=K, depth=DEPTH,
        original_depth=DEPTH, node_count=DEPTH+1, old_to_new=list(range(DEPTH+1)),
        raw_array_sha256=context['raw_array_sha256'], full_current_J_raw_sha256=arrays['stage-jacobians']['raw_sha256'],
        **identity), 'Complete original finite matrix binding')
    for key in (profile['parent_key'], 'original_sources', 'numerical_configuration', 'parameters', 'rawNode', 'cells',
                'graphs_sha256', 'gains_sha256', 'far_graph_sha256'):
        require(binding[key] == context[key], 'Original complete current context ' + key)
    require(binding['actual_current_original_records']=={name:context['current_original_'+name]
                for name in ('norm','minA','minD')},'Original current scalar records preserved in the matrix binding')
    definition = binding['matrix_identity_definition']
    require(canonical_sha(definition) == matrix == qr['new_matrix_identity_sha256'], 'Full canonical matrix definition hash')
    same_fields(definition, dict(M=M, K=K, depth=DEPTH,
        row_order='cut112, all576 stage224 rows, far112', row_sigma_rule='cut:sigma0; stage n:sigma_n; far:sigma576',
        cut_formula='delta[0,Q]+this_fresh_current_cut_residual',
        stage_formula='this_current_J[n]*delta[n+1]-delta[n]+this_current_r[n]',
        far_formula='delta[576,Pi]-original_diagonal_G*delta[576,Q]+this_current_far_residual',
        full_current_J_raw_sha256=arrays['stage-jacobians']['raw_sha256'],
        current_input_raw_sha256={name:arrays[name]['raw_sha256'] for name in INPUT_NAMES}), 'Exact original row/scaling formulas')
    # Native61's definition predates the three redundant call keys.  Its
    # binding, snapshot and ledger still bind them; do not invent those
    # keys inside its saved canonical definition or relabel its hash.
    if profile['new_flow']:
        same_fields(definition,dict(native_call=1,nonlinear_iteration=i,snapshot_sequence=i),
                    'Native73 current coordinates inside the canonical definition')
    for key in ('original_sources','numerical_configuration','parameters','rawNode','cells','graphs_sha256','gains_sha256'):
        require(definition[key]==context[key],'Full matrix definition retains current '+key)
    require(binding['snapshot_result']==snapshot_receipt and binding['snapshot_context']==snapshot['context'] and
            binding['snapshot_manifest']==snapshot['manifest'] and binding['core_instrumentation']==context['core_instrumentation'],
            'Complete descriptor aliases, not only abbreviated SHA fields')
    blocks = binding['complete_block_manifest']
    require(len(blocks) == DEPTH and definition['block_manifest'] ==
            [{key:item[key] for key in ('stage','bytes','raw_sha256')} for item in blocks], 'All original complete J blocks bound')
    for n, block in enumerate(blocks):
        same_fields(block, dict(stage=n, original_stage=n, bytes=K*K*8), 'Every original current J block identity')
        valid_sha(block['raw_sha256'], 'Current J stage SHA')
    if profile['new_flow']:
        implementation = context['primal_flow_implementation']
        same_fields(implementation, dict(source_file=FLOW_NAME, source_sha256=FLOW_SHA,
            only_flowStateWithJacobian_replaced=True, original_root_rhs_rk4_unchanged=True,
            complete_state_dimension=226, shape_dimension=K, captured_root_feed_only=True), 'New matched primal implementation identity')
        installation = s.obj(implementation['installation_receipt'])
        require(installation['implementation'] == {key:value for key,value in implementation.items()
            if key != 'installation_receipt'}, 'Actual installed implementation receipt')
        require(binding['primal_flow_implementation'] == definition['primal_flow_implementation'] == implementation and
                binding['new_variational_implementation_source_sha256'] == qr['primal_flow_source_sha256'] == FLOW_SHA,
                'New-flow matrix and direction identities remain honest')
    oman = q.obj(qr['array_manifest'])
    same_fields(oman, dict(schema=profile['output_arrays'], source_sha256=profile['producer_sha'],
        factor_engine_source_sha256=FACTOR_SHA, new_matrix_identity_sha256=matrix, **identity), 'Current full output manifest')
    by_file = manifest_map(oman, 'file')
    require(set(qr['original_arrays']) == set(INPUT_NAMES), 'All nine non-J original inputs retained')
    raw = {}
    for name in INPUT_NAMES:
        desc = qr['original_arrays'][name]
        require(desc == by_file[desc['file']], 'Copied input full descriptor alias')
        same_fields(desc, dict(shape=SHAPES[name], dtype='<f8', order='C',
            bytes=8*math.prod(SHAPES[name]), sha256=arrays[name]['raw_sha256']), 'Exact original input bytes ' + name)
        raw[name] = q.raw(desc)
        require(all(((word[0] >> 52) & 2047) != 2047 for word in struct.iter_unpack('<Q', raw[name])),
                'Finite copied original real input ' + name)
    delta_desc = qr['native_delta']
    require(delta_desc == by_file[delta_desc['file']], 'Actual direction descriptor alias')
    same_fields(delta_desc, dict(shape=[577,224], dtype='<f8', order='C', bytes=577*224*8), 'Full original-coordinate direction')
    delta_raw = q.raw(delta_desc)
    require(all(((word[0] >> 52) & 2047) != 2047 for word in struct.iter_unpack('<Q', delta_raw)), 'Finite saved direction')
    exact = qr['original_exact_readback']
    detail = q.obj(exact['full_report'])
    same_fields(detail, dict(schema=profile['exact'], source_sha256=profile['producer_sha'],
        system_source_sha256=profile['system_sha'], kernel_sha256=KERNEL_SHA,
        matrix_scope=profile['matrix_scope'], new_matrix_identity_sha256=matrix,
        direction_label='current_damped', direction_float64le_sha256=delta_desc['sha256'],
        exact_rows=ROWS, completed_stages=DEPTH, original_product_positions=DEPTH*K*K+M,
        eta_not_in_original_equations=True, readback_uses_unscaled_J_and_r_before_exact_sigma_division=True,
        no_float_refinement_RHS_formed=True, used_as_new_nonlinear_acceptance_gate=False, **identity), 'Full saved exact ledger origin')
    for key in ('exact_global_original_sigma_norm','exact_stored_base_sigma_norm','actual_original_withJ_norm',
                'exact_rows','completed_stages','original_product_positions','all_exact_residual_rows','worst_witness',
                'no_float_refinement_RHS_formed','used_as_new_nonlinear_acceptance_gate'):
        require(exact[key] == detail[key], 'Saved exact full/summary alias ' + key)
    require(detail['actual_original_withJ_norm'] == context['current_original_norm'] and
            detail['direction_array'] == delta_desc, 'Same actual original baseline and recovered direction')
    if profile['new_flow']:
        require(detail['primal_flow_source_sha256']==FLOW_SHA,'Exact report retains new primal source identity')
    ledger = detail['all_exact_residual_rows']
    require(ledger == by_file[ledger['file']], 'Saved full exact ledger manifest alias')
    same_fields(ledger, dict(dtype='exact-dyadic-jsonl-gzip', shape=[ROWS]), 'Every original exact row retained')
    q.check(ledger)
    return dict(snapshot_files=s, qr_files=q, record=record, snapshot=snapshot, context=context,
        snapshot_receipt=snapshot_receipt, qr=qr, binding=binding, raw=raw, detail=detail, ledger=ledger,
        blocks=blocks, core_contract=core, identity=identity, profile=profile,
        provenance=dict(snapshot_result=snapshot_receipt, snapshot_context=snapshot['context'],
            snapshot_manifest=snapshot['manifest'], input_binding=qr['input_binding'],
            direction_result=direction['result'], output_array_manifest=qr['array_manifest'],
            exact_full_report=exact['full_report'], exact_ledger=ledger,
            original_input_arrays=qr['original_arrays'], actual_direction=delta_desc,
            complete_original_J_raw_sha256=arrays['stage-jacobians']['raw_sha256'],
            new_matrix_identity_sha256=matrix, source_context_and_full_J_descriptor_bound=True,
            J_payload_reread_here=False, factors_reread_here=False,
            copied_nine_non_J_input_payloads_and_direction_reread_and_hashed=True,
            complete_J_and_factor_byte_audit_is_separate=True))


def residual_blocks(raw):
    yield 'cut', 0, raw['cut-residual']
    size = K * 8
    for n in range(DEPTH):
        yield 'stage', n, raw['stage-residuals'][n*size:(n+1)*size]
    yield 'far', DEPTH, raw['end-residual']


def baseline_maximum(raw, sigma_words, denominators):
    maximum = None
    for kind, node, block in residual_blocks(raw):
        for row, (word,) in enumerate(struct.iter_unpack('<Q', block)):
            value = unit_from_word(word)
            maximum = maxima_update(maximum, value, denominators[node], row_coordinate(kind,node,row),
                dict(original_r_float64le_hex=word_hex(word), original_sigma_float64le_hex=word_hex(sigma_words[node]),
                     original_r_exact_dyadic=compact(value)))
    return maximum


def trial_view(rows, baseline_record, predictions):
    result = []
    baseword = number_record(baseline_record, 'Saved original comparison baseNorm')
    baseinteger = unit_from_word(baseword)
    one = 1 << -UNIT_EXPONENT
    for row in rows:
        k = row['trial']
        require(type(k) is int and 0 <= k < 10, 'One of the original ten steps')
        require(word_of_number(row['step'], 'Original actual alpha') == (1023-k) << 52,
                'Actual alpha has the exact original2^-k binary64 bits')
        require(word_of_number(row['baseNorm'], 'Original actual baseNorm') == baseword,
                'Trial and current snapshot have exactly the same original baseNorm bits')
        item = dict(original_record=row, model_trial_index=k, original_complete_trial_residual_saved=False,
                    actual_trial_state_not_reconstructed=True, scalar_difference_is_not_a_residual_vector_remainder=True)
        value = row.get('trialNorm')
        if type(value) in (int, float) and math.isfinite(value):
            word = word_of_number(value, 'Saved actual trialNorm')
            trialinteger = unit_from_word(word)
            strict = trialinteger < baseinteger
            if row['kind'] in ('accepted','residual-not-decreasing'):
                require(strict == (row['kind'] == 'accepted'), 'Original saved scalar comparison agrees with recorded kind')
            pn, pd = fraction_parts(predictions[k]['maximum']['exact_absolute_scaled_value'])
            item.update(actual_trialNorm_float64le_hex=word_hex(word),
                original_actual_scalar_strict_decrease=strict,
                actual_trial_scalar_vs_exact_affine_prediction=relation(compare(trialinteger,one,pn,pd)),
                actual_scalar_minus_exact_affine_norm=rational(trialinteger*pd-pn*one,one*pd))
        else:
            item['actual_trialNorm_finite_numeric_value_available'] = False
        result.append(item)
    return result


def predict(bound, actual_trials, out):
    """Only new science in this file: integer affine combinations/comparisons."""
    require_actions()
    started = time.monotonic()
    raw, detail = bound['raw'], bound['detail']
    sigma_words = [x[0] for x in struct.iter_unpack('<Q',raw['original-scales'])]
    denominators = [unit_from_word(word) for word in sigma_words]
    require(len(denominators) == DEPTH+1 and all(d>0 for d in denominators), 'All actual original sigma finite and positive')
    baseline = baseline_maximum(raw,sigma_words,denominators)
    match_saved_maximum(baseline,detail['exact_stored_base_sigma_norm'],'Complete stored baseline readback')
    rn, rd = abs(baseline['n']), baseline['d']
    divisor = math.gcd(rn,rd); rn //= divisor; rd //= divisor
    predictions = [dict(maximum=None,groups={kind:None for kind in ('cut','stage','far')}) for _ in range(10)]
    active_count = blocking_count = nonzero_slopes = rows_seen = blocks_seen = 0
    first_blocking = first_touch = None
    alpha_n = alpha_d = None
    touch_ties = 0
    derivative = None
    active_path = out/'large-arrays/active-original-rows.jsonl.gz'
    active_path.parent.mkdir(parents=True,exist_ok=True)
    expected_blocks = iter(residual_blocks(raw))
    identity = dict(**bound['identity'],direction_label='current_damped',
        direction_float64le_sha256=bound['qr']['native_delta']['sha256'],
        new_matrix_identity_sha256=bound['binding']['new_matrix_identity_sha256'])
    if bound['profile']['new_flow']:
        identity['primal_flow_source_sha256'] = FLOW_SHA
    path = bound['qr_files'].path(bound['ledger']['file'])
    with active_path.open('xb') as af, gzip.GzipFile(fileobj=af,mode='wb',mtime=0) as active_stream, gzip.open(path,'rb') as stream:
        while True:
            line = stream.readline(MAX_LEDGER_LINE_BYTES+1)
            if not line:
                break
            require(len(line)<=MAX_LEDGER_LINE_BYTES and line.endswith(b'\n'), 'One complete bounded exact ledger record')
            item = json.loads(line)
            expected = next(expected_blocks,None)
            require(expected is not None, 'No extra exact blocks')
            kind,node,rblock = expected
            count = K if kind=='stage' else M
            same_fields(item,dict(kind=kind,node=node,
                first_global_equation_row=row_coordinate(kind,node,0)['global_equation_row'],**identity),
                'Every exact block belongs to this complete current matrix/direction')
            require(item['original_J_stage_sha256'] == (bound['blocks'][node]['raw_sha256'] if kind=='stage' else None),
                    'Exact ledger uses the original complete current J block identity')
            encoded = item['all_exact_unscaled_rows']
            require(isinstance(encoded,list) and len(encoded)==count,'Every original row in this exact block')
            S = denominators[node]
            for row,((rword,),saved) in enumerate(zip(struct.iter_unpack('<Q',rblock),encoded)):
                coordinate = row_coordinate(kind,node,row)
                R,E = unit_from_word(rword),exact_integer(saved)
                D = E-R
                payload = dict(original_r_float64le_hex=word_hex(rword),
                    original_sigma_float64le_hex=word_hex(sigma_words[node]),
                    original_r_exact_dyadic=compact(R),saved_e_exact_dyadic=saved,
                    exact_slope_unscaled_dyadic=compact(D))
                is_active = abs(R)*rd == rn*S
                if is_active:
                    active_count += 1
                    # rho=0 is reported separately; sign(R) is then zero.
                    inward = (R*D < 0) if rn else False
                    active_item = dict(**coordinate,**payload,
                        rho_positive=bool(rn),strictly_inward=inward,
                        sign_of_r_times_e_minus_r=(R*D>0)-(R*D<0))
                    if rn:
                        signed_slope = D if R>0 else -D
                        if derivative is None or compare(signed_slope,S,derivative[0],derivative[1])>0:
                            derivative = (signed_slope,S,coordinate)
                        if not inward:
                            blocking_count += 1
                            if first_blocking is None:first_blocking=active_item
                    active_stream.write(json_bytes(active_item))
                if D:
                    nonzero_slopes += 1
                    # Every nonzero slope contributes, including initially
                    # inactive rows. Negative time cannot occur since rho is
                    # the full baseline max; zero identifies an outward
                    # active row. Alpha* is reported only if all actives enter.
                    tn = rn*S-rd*R if D>0 else rn*S+rd*R
                    td = rd*abs(D)
                    require(tn>=0,'Full baseline interval contains each original row')
                    cmp = -1 if alpha_n is None else compare(tn,td,alpha_n,alpha_d)
                    if cmp<0:
                        alpha_n,alpha_d=tn,td;touch_ties=1
                        first_touch=dict(**coordinate,**payload,hit_boundary='positive' if D>0 else 'negative')
                    elif cmp==0:
                        touch_ties+=1
                for k,p in enumerate(predictions):
                    two=1<<k
                    numerator=(two-1)*R+E
                    denominator=two*S
                    p['maximum']=maxima_update(p['maximum'],numerator,denominator,coordinate,payload)
                    p['groups'][kind]=maxima_update(p['groups'][kind],numerator,denominator,coordinate,payload)
                rows_seen+=1
            blocks_seen+=1
            if kind=='stage' and ((node+1)%64==0 or node+1==DEPTH):
                print(json.dumps(dict(event='native_exact_affine_original_rows',
                    iteration=bound['identity']['nonlinear_iteration'],completed_stages=node+1,
                    original_rows_read=rows_seen)),flush=True)
    require(next(expected_blocks,None) is None and blocks_seen==DEPTH+2 and rows_seen==ROWS,
            'Exactly all578 blocks/all129248 original equations were read')
    bound['qr_files'].check(bound['ledger'])
    require(digest(path)==bound['ledger']['sha256'],'Compressed exact ledger remains identical after the complete read')
    match_saved_maximum(predictions[0]['maximum'],detail['exact_global_original_sigma_norm'],
                        'Alpha1 equals the existing exact recovered-direction defect')
    interval = dict(rho_zero=(rn==0),active_row_count=active_count,
        nonzero_slope_row_count=nonzero_slopes,blocking_active_row_count=blocking_count,
        all_rows_used_for_first_boundary_contact=True,
        strict_descent_is_for_the_exact_saved_array_affine_model_only=True)
    if rn==0:
        interval.update(positive_strict_descent_set='empty',alpha_star=None,
            reason='rho=0 and an infinity norm cannot be strictly negative',
            any_of_original_ten_has_strict_affine_descent=False)
    elif blocking_count:
        interval.update(positive_strict_descent_set='empty',alpha_star=None,
            reason='At least one active original row has r_i*(e_i-r_i)>=0',
            first_blocking_active_row=first_blocking,any_of_original_ten_has_strict_affine_descent=False)
    else:
        require(alpha_n is not None and alpha_n>0 and alpha_d>0,'All active rows enter and a finite positive first exit exists')
        interval.update(positive_strict_descent_set='0 < alpha < alpha_star',
            alpha_star=rational(alpha_n,alpha_d),first_contact_row=first_touch,
            first_contact_tied_rows=touch_ties,at_alpha_star='exact affine infinity norm equals rho',
            after_alpha_star='exact affine infinity norm strictly exceeds rho',
            any_of_original_ten_has_strict_affine_descent=compare(1,512,alpha_n,alpha_d)<0)
    if rn:
        interval['right_derivative_at_zero']=rational(derivative[0],derivative[1])
        interval['right_derivative_first_maximizing_row']=derivative[2]
    baseword=number_record(bound['context']['current_original_norm'],'Actual original baseNorm')
    baseint=unit_from_word(baseword);one=1<<-UNIT_EXPONENT
    public=[]
    for k,p in enumerate(predictions):
        maximum=p['maximum'];comparison=compare(abs(maximum['n']),maximum['d'],rn,rd)
        predicted_by_interval=(rn>0 and not blocking_count and compare(1,1<<k,alpha_n,alpha_d)<0)
        require((comparison<0)==predicted_by_interval,'Direct all-row prediction and R276 interval theorem agree')
        public.append(dict(trial=k,alpha=rational(1,1<<k),alpha_float64le_hex=word_hex((1023-k)<<52),
            maximum=public_maximum(maximum),family_maxima={kind:public_maximum(item) for kind,item in p['groups'].items()},
            exact_affine_norm_vs_exact_stored_baseline=relation(comparison),
            strict_affine_descent=(comparison<0),
            exact_affine_norm_vs_original_baseNorm_binary64=relation(compare(abs(maximum['n']),maximum['d'],baseint,one)),
            original_trial_observed=any(row['trial']==k for row in actual_trials)))
    require(any(row['strict_affine_descent'] for row in public)==interval['any_of_original_ten_has_strict_affine_descent'],
            'Complete ten-alpha and interval declarations agree')
    endpoint_sufficient = public[0]['strict_affine_descent']
    if endpoint_sufficient:
        require(all(row['strict_affine_descent'] for row in public),
                'The exact endpoint sufficient condition implies all ten original affine descents')
    active_desc=dict(file=active_path.relative_to(out).as_posix(),bytes=active_path.stat().st_size,sha256=digest(active_path),
        rows=active_count,format='gzip JSONL; all exact-baseline-active original rows')
    return dict(schema=SCHEMA,**bound['identity'],new_matrix_identity_sha256=bound['binding']['new_matrix_identity_sha256'],
        provenance=bound['provenance'],core_contract=bound['core_contract'],
        original_eta_cli_text=bound['qr']['eta_cli_text'],original_eta_binary64=bound['qr']['eta_binary64'],
        scientific_arithmetic_performed=True,byte_only_audit=False,diagnostic_completed=True,
        exact_original_rows=rows_seen,exact_original_blocks=blocks_seen,integer_unit_exponent=UNIT_EXPONENT,
        exact_stored_baseline=public_maximum(baseline),exact_descent_interval=interval,
        all_active_rows=active_desc,original_ten_alpha_predictions=public,
        exact_endpoint_strictly_below_exact_baseline=endpoint_sufficient,
        all_ten_descents_certified_by_endpoint_sufficient_condition=endpoint_sufficient,
        actual_original_baseNorm=bound['context']['current_original_norm'],
        exact_baseline_vs_original_baseNorm_binary64=relation(compare(rn,rd,baseint,one)),
        actual_original_trial_readback=trial_view(actual_trials,bound['context']['current_original_norm'],public),
        original_reported_formed_model=bound['qr'].get('formed_model_diagnostic'),
        formed_model_not_substituted_for_recovered_original_delta_exact_model=True,
        original_reported_exact_readback=bound['qr']['original_exact_readback'],
        same_alpha1_exact_endpoint_and_original_exact_baseline_confirmed=True,
        no_RHS_J_ODE_QR_or_matrix_action=True,no_new_direction_or_alpha_selected=True,
        no_native_trial_repeated=True,actual_rounded_trial_state_not_reconstructed=True,
        no_componentwise_nonlinear_remainder_claimed=True,
        nonlinear_acceptance_not_inferred_from_affine_prediction=True,
        used_as_new_native_or_other_scientific_acceptance_gate=False,
        elapsed_seconds=time.monotonic()-started)


def compact_iteration(result, full):
    def maximum_view(item):
        return {key:item[key] for key in ('kind','node','row','global_equation_row','component','mode',
            'original_sigma_float64le_hex','exact_signed_scaled_value','exact_absolute_scaled_value',
            'maximizing_rows','tie_rule')}
    return dict(schema='native-affine-infinity-iteration-small-summary-v1',
        diagnostic_completed=True,native_call=result['native_call'],nonlinear_iteration=result['nonlinear_iteration'],
        snapshot_sequence=result['snapshot_sequence'],current_state_sha256=result['current_state_sha256'],
        new_matrix_identity_sha256=result['new_matrix_identity_sha256'],full_result=full,
        original_complete_rows=result['exact_original_rows'],
        exact_stored_baseline=maximum_view(result['exact_stored_baseline']),
        exact_descent_interval=result['exact_descent_interval'],
        original_ten_alpha_predictions=[dict(maximum=maximum_view(row['maximum']),**{key:row[key] for key in ('trial','alpha',
            'exact_affine_norm_vs_exact_stored_baseline','strict_affine_descent',
            'exact_affine_norm_vs_original_baseNorm_binary64','original_trial_observed')})
            for row in result['original_ten_alpha_predictions']],
        actual_original_baseNorm=result['actual_original_baseNorm'],
        actual_original_trial_readback=result['actual_original_trial_readback'],
        scientific_arithmetic_performed=True,byte_only_audit=False,
        used_as_new_native_or_other_scientific_acceptance_gate=False)


def main():
    require_actions()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--native-kind',choices=tuple(PROFILES),required=True)
    parser.add_argument('--native-directory',type=Path,required=True)
    parser.add_argument('--original-run-id',required=True)
    parser.add_argument('--original-source-commit',required=True)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--native-result-sha256')
    group.add_argument('--partial-records-sha256')
    parser.add_argument('--partial-trials-sha256')
    parser.add_argument('--iteration',type=int,action='append',default=[],help='Explicit iteration(s); default all original recorded iterations')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    p=PROFILES[args.native_kind]
    require(args.original_run_id==p['run'] and args.original_source_commit==p['commit'],
            'Explicit actual original run/head must match the selected original source profile')
    require(not args.partial_trials_sha256 or args.partial_records_sha256,
            'Partial trial SHA is only for explicit partial-journal mode')
    require(all(0<=i<32 for i in args.iteration) and len(set(args.iteration))==len(args.iteration),'Distinct original iteration indices')
    native=Files(args.native_directory)
    require(native.root.name==p['directory'],'Use the original native output directory, not a relabelled cache')
    out=args.out.resolve()
    require(not os.path.lexists(args.out) and not out.is_relative_to(native.root) and not native.root.is_relative_to(out),
            'Use one new independent diagnostic output directory')
    out.mkdir(parents=True)
    started=time.monotonic()
    report=dict(schema=SCHEMA,source_sha256=digest(Path(__file__)),original_kind=args.native_kind,
        original_run_id=p['run'],original_source_commit=p['commit'],
        original_artifact_download_and_ZIP_verification_not_repeated_here=True,
        upstream_extraction_is_required_to_come_from_the_identified_public_artifact=True,
        read_only_original_artifact=True,scientific_arithmetic_started=False,
        scientific_arithmetic_performed=False,byte_only_audit=False,
        no_native_or_other_acceptance_gate_added=True,no_new_RHS_J_ODE_QR_or_matrix_action=True,
        diagnostic_completed=False,iterations=[],actual_errors=[])
    try:
        report['frozen_source_receipts']=source_receipts(p)
        scope,records,trial_groups,outer=load_native(args,p,native)
        report['original_scope']=scope
        # Publish the original native outcome before any new scientific
        # arithmetic so a later diagnostic error cannot erase that outcome.
        report['original_readout']=write_json(out,'large-arrays/original-native-readout.json.gz',dict(
            original_scope=scope,original_result=outer,original_correction_records=records,
            original_trial_records=[row for group in trial_groups.values() for row in group],
            new_diagnostic_not_yet_run=True,original_outcome_not_changed=True),compressed=True)
        original_small=dict(original_scope=scope,
            complete_original_readout=report['original_readout'],new_diagnostic_not_yet_run=True,
            original_outcome_not_changed=True)
        if len(json_bytes(original_small))>=95000:
            original_small=dict(complete_original_readout=report['original_readout'],
                original_native_accepted=scope.get('original_native_accepted'),
                compact_transport_fallback=True,new_diagnostic_not_yet_run=True,original_outcome_not_changed=True)
        write_json(out,'original-native-outcome.json',original_small)
        chosen=args.iteration or list(range(len(records)))
        require(all(i<len(records) for i in chosen),'Every requested original iteration exists')
        for i in chosen:
            rec=records[i];name='iteration-'+str(i).zfill(3);directory=out/name;directory.mkdir()
            status=dict(iteration=i,original_record=rec,diagnostic_completed=False,scientific_arithmetic_started=False)
            bound=None
            if not rec.get('linear_direction_returned'):
                status.update(skipped=True,reason='Original native bridge did not return a complete direction; no model invented')
            else:
                try:
                    bound=bind_iteration(native,rec,p,outer)
                    status['scientific_arithmetic_started']=True
                    report['scientific_arithmetic_started']=True
                    result=predict(bound,trial_groups.get(i,[]),directory)
                    report['scientific_arithmetic_performed']=True
                    result['source_sha256']=report['source_sha256']
                    full=write_json(directory,'large-arrays/result.json.gz',result,compressed=True)
                    small=compact_iteration(result,full)
                    if len(json_bytes(small))>=95000:
                        small={key:small[key] for key in ('schema','diagnostic_completed','native_call','nonlinear_iteration',
                            'snapshot_sequence','current_state_sha256','new_matrix_identity_sha256','full_result',
                            'original_complete_rows','scientific_arithmetic_performed','byte_only_audit',
                            'used_as_new_native_or_other_scientific_acceptance_gate')}
                        small['compact_transport_fallback']=True
                    status.update(diagnostic_completed=True,summary=write_json(directory,'summary.json',small),full_result=full)
                except Exception as error:
                    status.update(actual_diagnostic_error=repr(error),traceback=traceback.format_exc(),
                        original_native_outcome_unchanged=True)
                    if status['scientific_arithmetic_started'] and report['scientific_arithmetic_performed'] is False:
                        # No complete result certifies how far a failed
                        # arithmetic pass progressed; do not label it zero.
                        report['scientific_arithmetic_performed']=None
                    report['actual_errors'].append(dict(iteration=i,error=repr(error)))
                finally:
                    if bound is not None:
                        inventory=dict(snapshot_metadata_files=list(bound['snapshot_files'].seen.values()),
                            qr_metadata_nonJ_operand_and_direction_files=list(bound['qr_files'].seen.values()),
                            original_J_and_factor_payloads_not_read=True)
                        status['input_files']=write_json(directory,'large-arrays/input-files.json.gz',inventory,compressed=True)
            relative=write_json(out,name+'/status.json',status)
            report['iterations'].append(dict(iteration=i,status=relative,diagnostic_completed=status['diagnostic_completed'],
                skipped=status.get('skipped',False),summary=(dict(status['summary'],file=name+'/'+status['summary']['file'])
                    if 'summary' in status else None)))
            print(json.dumps(dict(event='native_exact_affine_infinity_diagnostic',iteration=i,
                diagnostic_completed=status['diagnostic_completed'],skipped=status.get('skipped',False))),flush=True)
        report['diagnostic_completed']=not report['actual_errors']
    except Exception as error:
        report['actual_errors'].append(dict(error=repr(error),traceback=traceback.format_exc()))
    finally:
        report['elapsed_seconds']=time.monotonic()-started
        report['root_input_receipts']=list(native.seen.values())
        full=write_json(out,'large-arrays/diagnostic-result.json.gz',report,compressed=True)
        short={key:report[key] for key in ('schema','source_sha256','original_kind','original_run_id','original_source_commit',
            'scientific_arithmetic_started','scientific_arithmetic_performed','byte_only_audit',
            'diagnostic_completed','iterations','actual_errors','elapsed_seconds')}
        short.update(full_result=full,original_scope=report.get('original_scope'),
            original_readout=report.get('original_readout'),used_as_native_acceptance_gate=False,
            no_matrix_action_or_new_nonlinear_trial=True)
        if len(json_bytes(short))>=95000:
            short={key:short[key] for key in ('schema','source_sha256','original_kind','original_run_id',
                'original_source_commit','scientific_arithmetic_started','scientific_arithmetic_performed','byte_only_audit','diagnostic_completed',
                'full_result','original_readout','elapsed_seconds','used_as_native_acceptance_gate')}
            short['compact_transport_fallback']=True
        write_json(out,'summary.json',short)
    return 0 if report['diagnostic_completed'] else 2


if __name__=='__main__':
    raise SystemExit(main())

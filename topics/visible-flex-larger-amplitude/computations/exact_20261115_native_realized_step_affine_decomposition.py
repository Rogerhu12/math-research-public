#!/usr/bin/env python3
"""Actual73/83: exact saved-matrix action on the realized binary64 state step.

All new scientific arithmetic runs only in this public repository's Actions.
The existing signed e=A*delta+r ledger supplies the ideal alpha=1/512 model.
Only A*h is newly evaluated, where h is the exact dyadic difference of the
actual trial and base IEEE words, never a rounded floating subtraction.
Every cut, stage and far row and its original positive sigma are retained.
This is a diagnostic, not another solver, trial selector or acceptance gate.
"""
from __future__ import annotations

import argparse
from collections import deque
from concurrent.futures import ProcessPoolExecutor
import gzip
import hashlib
import importlib.util
import json
import math
import multiprocessing
import os
from pathlib import Path
import re
import resource
import struct
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
REPOSITORY = 'Rogerhu12/math-research-public'
SCHEMA = 'actual73-realized-step-complete-exact-affine-decomposition-v1'
PROBE_SCHEMA = 'actual73-iteration2-realized-noJ-trial-probe-result-v1'
PROBE_NAME = 'geometry_20261115_native_realized_trial_probe.py'
PROBE_SHA = '305f5db2c6bc0fef85bd3115045531b1b366334b33300852634692a537f7d9cb'
PROBE_HOOK = 'geometry_20261115_native_realized_trial_probe_hook.mjs'
PROBE_HOOK_SHA = 'c03f59e4c3b6555a7a47187f1905a70f1e5a92dafacc222c327f4913c3ccdce0'
AFFINE_NAME = 'exact_20261115_native_affine_infinity_prediction.py'
AFFINE_SHA = 'bd4ff360cb27750a98bb9966981949f89d6b6dcf607fd820c34bb71adee9cde4'
KERNEL_NAME = 'exact_20261114_native_allrows_dyadic_residual.py'
KERNEL_SHA = '0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
ORIGINAL_RUN = '43657001633'
ORIGINAL_COMMIT = '9515d5aaf7c68f8efd366438d6bd81ce73c3486f'
NATIVE_RESULT_SHA = 'ade4fdac3adce104cb4e216e9d2f40b219bfca47d2c027ac548e6c65f65ab394'
SNAPSHOT_SHA = '2f9bf170c0366e9d5adaf003a9d0746f28a536171a32339e8a5f502313495e92'
QR_RESULT_SHA = '9d464f8239c375a2e95f207a3cfbad33e1f36037cd450cfefa2e3b165d86e3ff'
BASE_SHA = 'f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6'
DELTA_SHA = '4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a'
J_SHA = '1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4'
MATRIX_SHA = '6ea4b16fa7e41ae1099a3e792b67c19cf6c9d4ae41f5c3209fa84d43c5f8fbd8'
REFERENCE_SHA = 'b7812e06716bb1d22d4d32ff6ca12c62cb926dd9df12f41c199988f933ccd029'
M, K, DEPTH, ROWS, ITERATION = 112, 224, 576, 129248, 2
ALPHA_K, ALPHA_DENOMINATOR = 9, 512
KERNEL_UNIT = -2148
COMMON_UNIT = KERNEL_UNIT - ALPHA_K
NAMES = (
    'stored_base_residual', 'saved_direction_endpoint', 'ideal_affine_residual',
    'realized_affine_residual', 'stored_trial_residual', 'state_addition_term',
    'remaining_flow_tangent_model_term', 'total_trial_minus_ideal',
)
PROBE_SHAPES = {
    'base-states': [577, 224], 'native-delta': [577, 224], 'trial-states': [577, 224],
    'original-scales': [1, 577], 'cut-target': [1, 112], 'physical-height': [1, 112],
    'original-far-graph': [1, 112], 'saved-stage-residuals': [576, 224],
    'saved-cut-residual': [1, 112], 'saved-end-residual': [1, 112],
    'trial-stage-out': [576, 224], 'trial-stage-residuals': [576, 224],
    'trial-cut-residual': [1, 112], 'trial-end-residual': [1, 112],
    'trial-mean-height-increments': [1, 576],
}
_E = _K = None


class BudgetExhausted(RuntimeError):
    pass


def require_actions():
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY:
        raise RuntimeError('New exact scientific arithmetic is restricted to this public repository Actions')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def frozen_module(name, expected, alias):
    path = HERE / name
    if not path.is_file() or path.is_symlink() or digest(path) != expected:
        raise RuntimeError('Frozen source identity mismatch: ' + name)
    spec = importlib.util.spec_from_file_location(alias, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[alias] = module
    spec.loader.exec_module(module)
    return module


def modules():
    global _E, _K
    if _E is None:
        _E = frozen_module(AFFINE_NAME, AFFINE_SHA, '_actual83_frozen_affine')
    if _K is None:
        _K = frozen_module(KERNEL_NAME, KERNEL_SHA, '_actual83_frozen_integer_kernel')
    return _E, _K


def canonical_pair(coefficient, exponent):
    if coefficient == 0:
        return (0, 0)
    trailing = (abs(coefficient) & -abs(coefficient)).bit_length() - 1
    return coefficient >> trailing, exponent + trailing


def pair_difference(left, right):
    """Exact dyadic difference; neither operand nor result is a float subtraction."""
    lm, le = left
    rm, re = right
    if not lm:
        return canonical_pair(-rm, re)
    if not rm:
        return canonical_pair(lm, le)
    exponent = min(le, re)
    return canonical_pair((lm << (le - exponent)) - (rm << (re - exponent)), exponent)


def encoded_pair(pair):
    m, e = canonical_pair(*pair)
    return [hex(m), e] if m else ['0x0', 0]


def common_compact(integer):
    return encoded_pair((integer, COMMON_UNIT))


def realized_kernel_integer(E, encoded):
    """Decode the kernel result for exact h, which can span two finite words.

    |h|<2^1025 and |J|<2^1024. 224 products and the two additive
    terms have magnitude <2^2057, hence <2^4205 in units2^-2148.
    This is a representation bound, not a small-residual acceptance test.
    The frozen R276 decoder's4204-bit bound is only for binary64 delta.
    """
    E.require(isinstance(encoded, list) and len(encoded)==2 and
              isinstance(encoded[0], str) and type(encoded[1]) is int and
              re.fullmatch(r'-?0x[0-9a-f]+', encoded[0]) and len(encoded[0])<=1060,
              'Canonical exact realized-action dyadic pair')
    coefficient=int(encoded[0],16)
    E.require(hex(coefficient)==encoded[0], 'Canonical realized-action coefficient')
    if not coefficient:
        E.require(encoded==['0x0',0], 'Canonical exact realized-action zero')
        return 0
    shift=encoded[1]-KERNEL_UNIT
    E.require(coefficient&1 and 0<=shift<=4205 and coefficient.bit_length()+shift<=4205,
              'Full finite J times a difference of two finite words fits its exact integer representation')
    return coefficient<<shift


def json_bytes(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False) + '\n').encode()


def progress(out, value):
    path = out / 'progress.json'
    temporary = out / 'progress.json.tmp'
    temporary.write_bytes(json_bytes(value))
    os.replace(temporary, path)


class GzipLedger:
    def __init__(self, out, name, schema):
        self.out = out
        self.name = name
        self.path = out / name
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.raw_file = self.path.open('xb')
        self.stream = gzip.GzipFile(fileobj=self.raw_file, mode='wb', mtime=0)
        self.hash = hashlib.sha256()
        self.raw_bytes = 0
        self.records = 0
        self.schema = schema
        self.closed = False

    def write(self, value):
        raw = json_bytes(value)
        self.stream.write(raw)
        self.hash.update(raw)
        self.raw_bytes += len(raw)
        self.records += 1

    def close(self):
        if not self.closed:
            self.stream.close()
            self.raw_file.close()
            self.closed = True
        return dict(file=self.name, bytes=self.path.stat().st_size, sha256=digest(self.path),
                    raw_bytes=self.raw_bytes, raw_sha256=self.hash.hexdigest(), records=self.records,
                    schema=self.schema, encoding='gzip-jsonl')


def bind_reference(E, args, bound):
    path = args.r276_reference
    E.require(path.is_file() and not path.is_symlink(), 'Actual published R276 reference file required')
    files = E.Files(path.parent)
    receipt = files.info(path.name)
    E.require(receipt['sha256'] == args.r276_reference_sha256 == REFERENCE_SHA and receipt['bytes'] == 12153,
              'Actual73 completed R276 iteration2 original compressed bytes')
    ref = files.obj(receipt)
    E.same_fields(ref, dict(schema=E.SCHEMA, source_sha256=AFFINE_SHA,
        native_call=1, nonlinear_iteration=ITERATION, snapshot_sequence=ITERATION,
        current_state_sha256=BASE_SHA, new_matrix_identity_sha256=MATRIX_SHA,
        diagnostic_completed=True, scientific_arithmetic_performed=True,
        exact_original_rows=ROWS, exact_original_blocks=DEPTH+2), 'Actual existing R276 report')
    E.require(ref['snapshot_result'] == bound['snapshot_receipt'] and
              ref['original_reported_exact_readback'] == bound['qr']['original_exact_readback'],
              'R276 report is this exact snapshot and saved original endpoint ledger')
    E.require(ref['provenance']['actual_direction'] == bound['qr']['native_delta'] and
              ref['provenance']['original_input_arrays'] == bound['qr']['original_arrays'] and
              ref['provenance']['complete_original_J_raw_sha256'] == J_SHA,
              'R276 uses the identical complete original J/r/sigma/delta, not a substituted model')
    predictions = ref['original_ten_alpha_predictions']
    E.require(len(predictions) == 10 and [r['trial'] for r in predictions] == list(range(10)), 'Original ten-alpha report')
    chosen = predictions[ALPHA_K]
    E.require(chosen['alpha']['numerator'] == '1' and chosen['alpha']['denominator'] == '512' and
              chosen['alpha_float64le_hex'] == E.word_hex((1023-ALPHA_K) << 52), 'Exactly original alpha1/512')
    return files, receipt, ref, chosen


def same_receipt(E, actual, expected, label):
    E.same_fields(actual, {key:expected[key] for key in ('file','bytes','sha256')}, label)


def bind_probe(E, args, bound, original_trial, out, report):
    files = E.Files(args.probe_directory)
    info = files.info('result.json')
    E.require(info['sha256'] == E.valid_sha(args.probe_result_sha256, 'Actual run-time probe result SHA'),
              'New probe output bytes, not a preannounced result')
    result = files.obj(info)
    # Retain the actual producer outcome before requiring usable mathematical
    # inputs. A failed original evaluation must not disappear behind a binder
    # error. No absent summary is invented for an incomplete producer.
    report['probe_result']=info
    result_copy=out/'original-probe-result.json'
    result_copy.write_bytes(files.raw(info))
    report['original_probe_result_copy']=dict(file=result_copy.name,bytes=result_copy.stat().st_size,sha256=digest(result_copy))
    report['probe_original_result']=result
    summary = files.obj(result['summary']) if isinstance(result.get('summary'),dict) else None
    if summary is not None:
        summary_copy=out/'original-probe-summary.json'
        summary_copy.write_bytes(files.raw(result['summary']))
        report['original_probe_summary_copy']=dict(file=summary_copy.name,bytes=summary_copy.stat().st_size,sha256=digest(summary_copy))
    report['original_probe_outcome']=E.write_json(out,'original-probe-outcome.json',dict(
        actual_result_receipt=info,actual_result=result,actual_summary=summary,
        original_outcome_not_changed=True,new_exact_diagnostic_not_yet_run=True))
    report['probe_original_summary']=summary
    source = HERE / PROBE_NAME
    hook = HERE / PROBE_HOOK
    E.require(source.is_file() and hook.is_file() and not source.is_symlink() and not hook.is_symlink(),
              'The explicitly checked-out probe producer sources exist')
    E.require(digest(source)==PROBE_SHA and digest(hook)==PROBE_HOOK_SHA,'Frozen single-trial producer source bytes')
    E.same_fields(result, dict(schema=PROBE_SCHEMA, source_sha256=PROBE_SHA, hook_sha256=PROBE_HOOK_SHA,
        original_snapshot_result_sha256=SNAPSHOT_SHA, direction_result_sha256=QR_RESULT_SHA,
        base_state_sha256=BASE_SHA, direction_sha256=DELTA_SHA,original_state_sha256=BASE_SHA,
        completed=True,probe_completed=True,evaluation_returned=True,original_noJ_evaluate_calls=1,
        original_native_solve_calls=0,new_J_evaluations=0,newton_corrections=0,
        no_TailClient_solve_called=True,saved_J_payloads_read=False,
        native_accepted=False,task_completed=False,observer_io_failure=None), 'Actual fixed-alpha probe provenance')
    E.require(summary is not None,'A complete returned probe has its original summary')
    binding = files.obj(result['input_binding'])
    manifest = files.obj(result['array_manifest'])
    specification = files.obj(result['specification'])
    identity=dict(source_sha256=result['source_sha256'],hook_sha256=result['hook_sha256'])
    E.same_fields(summary,dict(schema='actual73-iteration2-realized-noJ-trial-probe-summary-v1',
        **identity,spec_sha256=result['specification']['sha256'],original_public_run=ORIGINAL_RUN,
        original_snapshot_result_sha256=SNAPSHOT_SHA,direction_result_sha256=QR_RESULT_SHA,
        base_state_sha256=BASE_SHA,direction_sha256=DELTA_SHA,
        probe_completed=True,evaluation_returned=True,original_noJ_evaluate_calls=1,
        original_solve_calls=0,new_withJ_evaluations=0,new_J_evaluations=0,newton_corrections=0,
        complete_returned_residuals_available=True,completed_stages=DEPTH,
        actual_trial_index=ALPHA_K,original_selected_trial=original_trial,
        complete_state_and_delta_restored_by_raw_bits=True,base_state_unchanged=True,direction_unchanged=True,
        actual_trial_state_unchanged_by_call=True,target_unchanged=True,scales_unchanged=True,
        original_noJ_arithmetic_source_restoration_verified=True,original_noJ_primal_path_used=True,
        actual73_new_withJ_function_not_called=True,saved_J_payloads_read=False,saved_J_descriptor_only=J_SHA,
        no_cut_or_far_projection=True,no_scientific_acceptance_threshold_added=True,
        observer_io_failure=None,all_noJ_flow_J_fields_null=True), 'Actual complete no-J probe summary')
    E.same_fields(binding,dict(schema='actual73-iteration2-realized-noJ-trial-input-binding-v1',
        **identity,original_public_run=int(ORIGINAL_RUN),current_state_sha256=BASE_SHA,direction_sha256=DELTA_SHA,
        original_context=bound['context'],original_direction_binding=bound['binding'],
        original_direction_native_delta=bound['qr']['native_delta'],original_selected_trial=original_trial,
        actual_trial_index=ALPHA_K,original_raw_state_and_delta_unchanged=True,
        old_native_failure_not_a_completed_anchor=True,original_J_payload_not_read_by_native_probe=True,
        no_new_numerical_acceptance_gate=True), 'Probe uses the same complete current operands')
    E.same_fields(manifest,dict(schema='actual73-iteration2-realized-noJ-trial-output-arrays-v1',
        **identity,spec_sha256=result['specification']['sha256'],original_snapshot_result_sha256=SNAPSHOT_SHA,
        direction_result_sha256=QR_RESULT_SHA,base_state_sha256=BASE_SHA,direction_sha256=DELTA_SHA,
        trial_state_sha256=summary['trial_state_sha256']), 'Complete actual trial output manifest')
    E.same_fields(specification,dict(schema='actual73-iteration2-realized-noJ-trial-probe-spec-v1',
        **identity,original_public_run=ORIGINAL_RUN,original_native_result_sha256=NATIVE_RESULT_SHA,
        original_snapshot_result_sha256=SNAPSHOT_SHA,current_state_sha256=BASE_SHA,
        original_direction_result_sha256=QR_RESULT_SHA,direction_raw_sha256=DELTA_SHA,
        original_selected_trial=original_trial,actual_trial_index=ALPHA_K,
        original_nonlinear_iteration=ITERATION,original_snapshot_sequence=ITERATION,original_native_call=1,
        actual_original_trial_expression_without_projection=True,original_native_solve_requested=False,
        new_withJ_requested=False,expected_noJ_evaluate_calls=1,no_scientific_acceptance_threshold_added=True),
        'Actual original single-trial specification')
    same_receipt(E,result['input_native_result'],report['original_scope']['original_result'],'Probe original native result')
    same_receipt(E,binding['native_result'],result['input_native_result'],'Native input aliases')
    same_receipt(E,result['input_snapshot_result'],bound['snapshot_receipt'],'Probe exact snapshot receipt')
    same_receipt(E,binding['snapshot_result'],bound['snapshot_receipt'],'Snapshot input aliases')
    same_receipt(E,binding['direction_result'],bound['provenance']['direction_result'],'Original returned direction result')
    E.require(result['array_manifest']==summary['output_array_manifest'],'Actual probe output manifest alias')
    sman=bound['snapshot_files'].obj(bound['snapshot']['manifest'])
    original_arrays=E.manifest_map(sman,'name')
    E.require(binding['original_snapshot_arrays']=={name:desc for name,desc in original_arrays.items() if name!='stage-jacobians'} and
              binding['original_J_descriptor_only']==original_arrays['stage-jacobians']==specification['original_J_descriptor_only'],
              'The complete saved J descriptor and all nine original non-J descriptors are unchanged')
    alpha_word=(1023-ALPHA_K)<<52
    for label,item in (('result',result),('summary',summary),('binding',binding),('manifest',manifest)):
        E.require(E.number_record(item['alpha'],'Exact original alpha '+label)==alpha_word,'Exactly the original1/512 alpha bits')
    E.require(E.word_of_number(original_trial['step'],'Original stored trial alpha')==alpha_word and
              original_trial['trial']==ALPHA_K and original_trial['iteration']==ITERATION and original_trial['call']==1,
              'The actual completed original trial is precisely this requested fixed step')
    E.require(summary['saved_withJ_norm']==bound['context']['current_original_norm'], 'The same original baseline norm record')
    current_norm_word=E.number_record(summary['actual_original_noJ_norm'],'Actual original probe norm',finite=False)
    scan_norm_word=E.number_record(summary['actual_noJ_residual_readback']['reconstructed_norm'],
                                  'Original probe residual scan norm',finite=False)
    old_trial_norm_word=E.word_of_number(original_trial['trialNorm'],'Actual73 stored original trial norm')
    E.require(summary['actual_noJ_norm_scan_same_bits']==(scan_norm_word==current_norm_word) and
              summary['actual_original_noJ_norm_equals_saved_trial_bits']==(current_norm_word==old_trial_norm_word),
              'Producer scalar comparison flags agree with their actual saved words; equality is not required')
    scalar_comparison=dict(original_actual73_trial=original_trial,
        original_actual73_trial_norm_float64le_hex=E.word_hex(old_trial_norm_word),
        actual_probe_original_norm=summary['actual_original_noJ_norm'],
        actual_probe_scan_norm=summary['actual_noJ_residual_readback']['reconstructed_norm'],
        same_as_original_actual73_trial_norm_bits=current_norm_word==old_trial_norm_word,
        actual_probe_scan_and_original_norm_same_bits=scan_norm_word==current_norm_word,
        scalar_reproducibility_is_not_a_new_acceptance_condition=True)
    arrays = E.manifest_map(manifest, 'name')
    E.require(set(PROBE_SHAPES).issubset(arrays), 'All complete original and actual-trial arrays are present')
    raw = {}
    for name, shape in PROBE_SHAPES.items():
        desc = arrays[name]
        E.same_fields(desc, dict(shape=shape, dtype='<f8', order='C', bytes=8*math.prod(shape)), 'Full probe array ' + name)
        raw[name] = files.raw(desc)
        E.require(all(((word[0] >> 52) & 2047) != 2047 for word in struct.iter_unpack('<Q', raw[name])),
                  'Finite complete saved operands for exact-real diagnostics: ' + name)
    for name, desc in arrays.items():
        files.check(desc)
    aliases = {'base-states': 'base-states', 'original-scales': 'original-scales', 'cut-target': 'cut-target',
        'physical-height': 'physical-height', 'original-far-graph': 'original-far-graph',
        'saved-stage-residuals': 'stage-residuals', 'saved-cut-residual': 'cut-residual', 'saved-end-residual': 'end-residual'}
    for probe_name, original_name in aliases.items():
        E.require(raw[probe_name] == bound['raw'][original_name], 'Exact original probe operand bytes: ' + probe_name)
    delta_raw = bound['qr_files'].raw(bound['qr']['native_delta'])
    E.require(raw['native-delta'] == delta_raw and sha(delta_raw) == DELTA_SHA, 'Complete original returned delta bytes')
    E.require(sha(raw['trial-states'])==summary['trial_state_sha256']==manifest['trial_state_sha256'],
              'Actual rounded trial words are bound to the original evaluation')
    return dict(files=files, result_receipt=info, result=result, summary=summary,
                binding=binding, manifest=manifest, arrays=arrays, raw=raw,
                scalar_comparison=scalar_comparison,norm_word=current_norm_word)


def build_h(E, Kmod, bound, probe, out, deadline):
    """Decode all original words and form exact h and h-alpha*delta pairs."""
    raw = probe['raw']
    base = Kmod.decoded_array(raw['base-states'], ROWS, 'base states')
    trial = Kmod.decoded_array(raw['trial-states'], ROWS, 'actual rounded trial states')
    delta = Kmod.decoded_array(raw['native-delta'], ROWS, 'original full delta')
    base_words = list(struct.iter_unpack('<Q', raw['base-states']))
    trial_words = list(struct.iter_unpack('<Q', raw['trial-states']))
    h = []
    counts = dict(total_coordinates=ROWS, stored_words_changed=0, exact_h_nonzero=0,
        exact_h_zero_with_nonzero_ideal_increment=0, exact_h_equals_ideal_increment=0,
        negative_zero_base_words=0, negative_zero_trial_words=0)
    ledger = GzipLedger(out, 'large-arrays/complete-exact-realized-increments.jsonl.gz',
                        'complete577-node-exact-realized-state-increment-v1')
    try:
        for node in range(DEPTH+1):
            if time.monotonic() > deadline:
                raise BudgetExhausted('Budget ended before another full state-increment node')
            hp, ideal, errors = [], [], []
            start = node*K
            for row in range(K):
                j = start+row
                realized = pair_difference(trial[j], base[j])
                original_ideal = canonical_pair(delta[j][0], delta[j][1]-ALPHA_K)
                error = pair_difference(realized, original_ideal)
                h.append(realized)
                hp.append(encoded_pair(realized)); ideal.append(encoded_pair(original_ideal)); errors.append(encoded_pair(error))
                counts['stored_words_changed'] += base_words[j] != trial_words[j]
                counts['exact_h_nonzero'] += bool(realized[0])
                counts['exact_h_zero_with_nonzero_ideal_increment'] += not realized[0] and bool(original_ideal[0])
                counts['exact_h_equals_ideal_increment'] += not error[0]
                counts['negative_zero_base_words'] += base_words[j][0] == 1 << 63
                counts['negative_zero_trial_words'] += trial_words[j][0] == 1 << 63
            a, b = start*8, (start+K)*8
            ledger.write(dict(schema=ledger.schema, node=node, first_state_coordinate=start,
                base_node_raw_sha256=sha(raw['base-states'][a:b]), trial_node_raw_sha256=sha(raw['trial-states'][a:b]),
                delta_node_raw_sha256=sha(raw['native-delta'][a:b]), exact_h=hp,
                ideal_alpha_delta=ideal, exact_h_minus_ideal_increment=errors,
                exact_difference_not_rounded_to_binary64=True))
    finally:
        receipt = ledger.close()
        E.write_json(out, 'increment-status.json', dict(complete=(len(h)==ROWS), counts=counts,
                     nodes_written=receipt['records'], complete_or_partial_ledger=receipt,
                     no_float_subtraction_used=True, signed_zero_input_words_retained_by_raw_identity=True))
    return h, counts, receipt


class StageStream:
    def __init__(self, E, bound):
        self.E, self.bound = E, bound
        manifest = bound['snapshot_files'].obj(bound['snapshot']['manifest'])
        self.array = E.manifest_map(manifest, 'name')['stage-jacobians']
        self.h = hashlib.sha256()
        self.bytes = self.blocks = 0
        self.complete = False
        self.chunk_receipts = []

    def __iter__(self):
        E = self.E
        for chunk in self.array['chunks']:
            raw = self.bound['snapshot_files'].raw(chunk)
            E.require(sha(raw) == chunk['raw_sha256'], 'Original complete raw J chunk hash')
            self.h.update(raw); self.bytes += len(raw)
            self.chunk_receipts.append(dict(file=chunk['file'], bytes=chunk['bytes'], sha256=chunk['sha256']))
            for stage in range(chunk['row_start'], chunk['row_stop']):
                E.require(stage == self.blocks, 'Original complete J stage order')
                first = (stage-chunk['row_start'])*K*K*8
                block = raw[first:first+K*K*8]
                E.require(len(block)==K*K*8 and sha(block)==self.bound['blocks'][stage]['raw_sha256'],
                          'The complete current J block agrees with the original matrix binding')
                self.blocks += 1
                yield stage, block
        E.require(self.blocks==DEPTH and self.bytes==self.array['total_bytes'] and
                  self.h.hexdigest()==self.array['raw_sha256']==J_SHA, 'All original576 J blocks and bytes consumed')
        self.complete = True

    def receipt(self):
        return dict(complete=self.complete, stage_blocks_streamed=self.blocks, bytes_streamed=self.bytes,
                    streamed_sha256=self.h.hexdigest(), expected_complete_sha256=J_SHA,
                    original_array_descriptor=self.array, chunks_reread=self.chunk_receipts)


def stage_worker(task):
    require_actions()
    E, Kmod = modules()
    # Kmod accepts exact mantissa/exponent pairs. They need not be individual
    # binary64 numbers. Exact h is a multiple of2^-1074, so every J*h product
    # lies on the kernel's2^-2148 lattice without any underflow or rounding.
    return Kmod.stage_job(task)


def ordered_stage_results(stream, raw, h, workers, deadline):
    E, Kmod = modules()
    def tasks():
        for stage, block in stream:
            if time.monotonic() > deadline:
                raise BudgetExhausted('Budget ended before scheduling another original full J*h block')
            a=stage*K; b=(stage+1)*K
            residuals=Kmod.decoded_array(raw['stage-residuals'][a*8:b*8],K,'original residual block')
            yield dict(stage=stage,J=block,residuals=residuals,
                       directions={'realized_h':(h[a:b],h[b:b+K])})
    if workers==1:
        for task in tasks():
            yield stage_worker(task)
        return
    pool=ProcessPoolExecutor(max_workers=workers,mp_context=multiprocessing.get_context('spawn'))
    pending=deque()
    try:
        for task in tasks():
            pending.append(pool.submit(stage_worker,task))
            if len(pending)>=2*workers:
                yield pending.popleft().result()
        while pending:
            yield pending.popleft().result()
    finally:
        for future in pending:
            future.cancel()
        pool.shutdown(wait=True,cancel_futures=True)


class SavedEndpoint:
    def __init__(self, E, bound):
        self.E,self.bound=E,bound
        self.path=bound['qr_files'].check(bound['ledger'])
        self.stream=gzip.open(self.path,'rb')
        self.blocks=self.rows=0
        self.hash=hashlib.sha256()
        self.raw_bytes=0
        self.complete=False

    def block(self,kind,node,count):
        E=self.E
        line=self.stream.readline(E.MAX_LEDGER_LINE_BYTES+1)
        E.require(bool(line) and line.endswith(b'\n') and len(line)<=E.MAX_LEDGER_LINE_BYTES,
                  'One complete saved endpoint ledger block')
        self.hash.update(line);self.raw_bytes+=len(line)
        item=json.loads(line)
        identity=dict(**self.bound['identity'],direction_label='current_damped',
            direction_float64le_sha256=DELTA_SHA,new_matrix_identity_sha256=MATRIX_SHA,
            primal_flow_source_sha256=E.FLOW_SHA)
        E.same_fields(item,dict(kind=kind,node=node,
            first_global_equation_row=E.row_coordinate(kind,node,0)['global_equation_row'],**identity),
            'Saved e block has the same original current matrix and recovered delta')
        E.require(item['original_J_stage_sha256']==(self.bound['blocks'][node]['raw_sha256'] if kind=='stage' else None),
                  'Saved endpoint original J block identity')
        encoded=item['all_exact_unscaled_rows']
        E.require(len(encoded)==count,'All saved endpoint rows in this block')
        values=[E.exact_integer(x) for x in encoded]
        self.blocks+=1;self.rows+=count
        return values,dict(uncompressed_record_sha256=sha(line),original_J_stage_sha256=item['original_J_stage_sha256'])

    def finish(self):
        self.E.require(not self.stream.read(1) and self.blocks==DEPTH+2 and self.rows==ROWS,
                       'Saved endpoint has exactly all578 blocks/all129248 original rows')
        self.stream.close()
        self.E.require(digest(self.path)==self.bound['ledger']['sha256'],'The consumed signed endpoint ledger remains unchanged')
        self.complete=True

    def close(self):
        self.stream.close()
        return dict(complete=self.complete,blocks_read=self.blocks,rows_read=self.rows,
                    uncompressed_bytes_read=self.raw_bytes,uncompressed_sha256_read=self.hash.hexdigest(),
                    source=self.bound['ledger'])


def same_saved_maximum(E, computed, saved, label):
    for key in ('kind','node','row','global_equation_row','component','mode'):
        E.require(computed['coordinate'][key]==saved[key],label+': exact maximizing coordinate '+key)
    for key, sign in (('exact_signed_scaled_value',1),('exact_absolute_scaled_value',0)):
        n,d=E.fraction_parts(saved[key]);cn=computed['n'] if sign else abs(computed['n'])
        E.require(E.compare(cn,computed['d'],n,d)==0,label+': exact saved rational '+key)


def decompose(E,Kmod,bound,probe,reference,reference_choice,h,out,workers,deadline,state):
    sigma_words=[x[0] for x in struct.iter_unpack('<Q',bound['raw']['original-scales'])]
    sigma_kernel=[E.unit_from_word(w) for w in sigma_words]
    E.require(len(sigma_kernel)==DEPTH+1 and all(x>0 for x in sigma_kernel),'All original positive sigma retained')
    maxima={name:None for name in NAMES}
    family={kind:{name:None for name in NAMES} for kind in ('cut','stage','far')}
    zeros={name:0 for name in NAMES}
    rraw=bound['raw'];praw=probe['raw']
    endpoint=SavedEndpoint(E,bound)
    jstream=StageStream(E,bound)
    ledger=GzipLedger(out,'large-arrays/complete-original-row-decomposition.jsonl.gz',
                     'complete129248-original-row-realized-step-decomposition-v1')
    block_reports=GzipLedger(out,'large-arrays/complete-original-block-maxima.jsonl.gz',
                            'complete578-block-realized-step-exact-maxima-v1')
    watch={2539,2762,2128}
    watched=[]

    def consume(kind,node,realized_encoded,source):
        if time.monotonic()>deadline:
            raise BudgetExhausted('Budget ended before another complete original block comparison')
        count=K if kind=='stage' else M
        a=node*K*8
        base_bytes=rraw['stage-residuals'][a:a+K*8] if kind=='stage' else rraw['cut-residual' if kind=='cut' else 'end-residual']
        actual_bytes=praw['trial-stage-residuals'][a:a+K*8] if kind=='stage' else praw['trial-cut-residual' if kind=='cut' else 'trial-end-residual']
        saved_e,old_source=endpoint.block(kind,node,count)
        E.require(len(realized_encoded)==count,'All exact realized original rows returned')
        S=sigma_kernel[node]*ALPHA_DENOMINATOR
        block_values={name:[] for name in NAMES};block_max={name:None for name in NAMES}
        for row,((rw,),(tw,),em,realized) in enumerate(zip(struct.iter_unpack('<Q',base_bytes),struct.iter_unpack('<Q',actual_bytes),saved_e,realized_encoded)):
            R=E.unit_from_word(rw);T=E.unit_from_word(tw);H=realized_kernel_integer(E,realized)
            ideal=(ALPHA_DENOMINATOR-1)*R+em
            real=ALPHA_DENOMINATOR*H
            actual=ALPHA_DENOMINATOR*T
            values=dict(stored_base_residual=ALPHA_DENOMINATOR*R,saved_direction_endpoint=ALPHA_DENOMINATOR*em,
                ideal_affine_residual=ideal,realized_affine_residual=real,stored_trial_residual=actual,
                state_addition_term=real-ideal,remaining_flow_tangent_model_term=actual-real,
                total_trial_minus_ideal=actual-ideal)
            E.require(values['state_addition_term']+values['remaining_flow_tangent_model_term']==values['total_trial_minus_ideal'],
                      'Exact componentwise decomposition identity')
            coordinate=E.row_coordinate(kind,node,row)
            payload=dict(original_sigma_float64le_hex=E.word_hex(sigma_words[node]),
                original_r_float64le_hex=E.word_hex(rw),actual_trial_r_float64le_hex=E.word_hex(tw))
            encoded_values={key:common_compact(value) for key,value in values.items()}
            for name,value in values.items():
                encoded=encoded_values[name]
                block_values[name].append(encoded);zeros[name]+=not value
                vp=dict(payload,exact_unscaled_dyadic=encoded)
                cross=dict(vp,all_exact_unscaled_vectors_at_row=encoded_values)
                maxima[name]=E.maxima_update(maxima[name],value,S,coordinate,cross)
                family[kind][name]=E.maxima_update(family[kind][name],value,S,coordinate,cross)
                block_max[name]=E.maxima_update(block_max[name],value,S,coordinate,vp)
            if coordinate['global_equation_row'] in watch:
                watched.append(dict(**coordinate,**payload,
                    exact_unscaled_values=encoded_values,
                    exact_signed_original_sigma_values={name:E.rational(value,S) for name,value in values.items()}))
            state['rows_completed']+=1
        state['blocks_completed']+=1
        if kind=='stage':state['stages_completed']+=1
        ledger.write(dict(schema=ledger.schema,kind=kind,node=node,first_global_equation_row=E.row_coordinate(kind,node,0)['global_equation_row'],
            count=count,integer_unit_exponent=COMMON_UNIT,original_sigma_float64le_hex=E.word_hex(sigma_words[node]),
            exact_vectors=block_values,saved_endpoint_source=old_source,realized_action_source=source,
            all_componentwise_decomposition_identities_equal=True))
        block_reports.write(dict(schema=block_reports.schema,kind=kind,node=node,count=count,
            exact_original_sigma_maxima={name:E.public_maximum(value) for name,value in block_max.items()}))
        if kind!='stage' or (node+1)%32==0:
            progress(out,dict(schema=SCHEMA,phase='complete-original-row-decomposition',**state,
                elapsed_seconds=time.monotonic()-state['started_monotonic'],scientific_arithmetic_performed=True))
            print(json.dumps(dict(event='realized_step_complete_original_rows',kind=kind,node=node,
                rows_completed=state['rows_completed'],stages_completed=state['stages_completed'])),flush=True)

    try:
        graph=Kmod.decoded_array(rraw['original-far-graph'],M,'original far graph')
        cut=Kmod.boundary_job('cut',Kmod.decoded_array(rraw['cut-residual'],M,'original cut residual'),
                             {'realized_h':h[:K]},graph)
        consume('cut',0,cut['directions']['realized_h']['rows'],dict(kind='original-cut-full-exact-h'))
        for item in ordered_stage_results(jstream,rraw,h,workers,deadline):
            stage=item['stage']
            E.require(stage==state['stages_completed'],'Ordered complete J*h stage results')
            consume('stage',stage,item['directions']['realized_h']['rows'],
                {key:item[key] for key in ('stage','J_stage_raw_sha256','J_words_visited','J_nonzero_words','J_negative_zero_words')})
        far=Kmod.boundary_job('far',Kmod.decoded_array(rraw['end-residual'],M,'original end residual'),
                             {'realized_h':h[DEPTH*K:(DEPTH+1)*K]},graph)
        consume('far',DEPTH,far['directions']['realized_h']['rows'],dict(kind='original-far-full-exact-h'))
        endpoint.finish()
        E.require(jstream.complete and state['rows_completed']==ROWS and state['blocks_completed']==DEPTH+2,
                  'All original576 J blocks and129248 cut/stage/far rows complete')
        same_saved_maximum(E,maxima['stored_base_residual'],reference['exact_stored_baseline'],'Existing R276 baseline')
        same_saved_maximum(E,maxima['ideal_affine_residual'],reference_choice['maximum'],'Existing R276 alpha1/512 maximum')
        for kind in family:
            same_saved_maximum(E,family[kind]['ideal_affine_residual'],reference_choice['family_maxima'][kind],
                              'Existing R276 alpha1/512 '+kind+' family maximum')
        state['complete']=True
        return dict(exact_original_sigma_maxima={name:E.public_maximum(value) for name,value in maxima.items()},
            exact_family_maxima={kind:{name:E.public_maximum(value) for name,value in values.items()} for kind,values in family.items()},
            exact_zero_row_counts=zeros,watched_original_rows=watched,
            norm_readback=norm_readback(E,maxima,probe,bound),
            existing_R276_baseline_and_chosen_alpha_and_all_three_family_maxima_equal=True,
            complete_componentwise_decomposition_verified=True)
    finally:
        state['row_decomposition_ledger']=ledger.close()
        state['block_maxima_ledger']=block_reports.close()
        state['saved_endpoint_ledger_readback']=endpoint.close()
        state['complete_or_partial_original_J_stream']=jstream.receipt()
        E.write_json(out,'decomposition-status.json',dict(schema=SCHEMA,**state,
            scientific_arithmetic_performed=True,not_an_acceptance_gate=True,
            exact_maxima_not_claimed_complete_if_complete_is_false=True))


def norm_readback(E,maxima,probe,bound):
    """Exact differences of scalar norms are explicitly not vector errors."""
    base=maxima['stored_base_residual']
    actual=maxima['stored_trial_residual']
    names=('ideal_affine_residual','realized_affine_residual','stored_trial_residual')
    baseline_word=E.number_record(bound['context']['current_original_norm'],'Original comparison baseline')
    baseline_integer=E.unit_from_word(baseline_word)
    one=1<<(-KERNEL_UNIT)
    against_baselines={}
    for name in names:
        item=maxima[name]
        against_baselines[name]=dict(
            versus_exact_stored_baseline=E.relation(E.compare(abs(item['n']),item['d'],abs(base['n']),base['d'])),
            versus_original_binary64_baseline=E.relation(E.compare(abs(item['n']),item['d'],baseline_integer,one)),
            exact_norm_minus_exact_stored_baseline=E.rational(abs(item['n'])*base['d']-abs(base['n'])*item['d'],item['d']*base['d']))
    differences={}
    for left,right in (('realized_affine_residual','ideal_affine_residual'),
                       ('stored_trial_residual','realized_affine_residual'),
                       ('stored_trial_residual','ideal_affine_residual')):
        a,b=maxima[left],maxima[right]
        differences[left+'_norm_minus_'+right+'_norm']=E.rational(
            abs(a['n'])*b['d']-abs(b['n'])*a['d'],a['d']*b['d'])
    current_word=probe['norm_word']
    current_finite=((current_word>>52)&2047)!=2047
    binary_comparison=None
    if current_finite:
        current_integer=E.unit_from_word(current_word)
        binary_comparison=dict(exact_trial_norm_versus_original_binary64_norm=E.relation(
            E.compare(abs(actual['n']),actual['d'],current_integer,one)),
            exact_trial_norm_minus_original_binary64_norm=E.rational(
                abs(actual['n'])*one-current_integer*actual['d'],actual['d']*one))
    return dict(actual_probe_scalar_comparison=probe['scalar_comparison'],
        original_baseline=bound['context']['current_original_norm'],
        exact_norm_relations=against_baselines,exact_norm_differences=differences,
        actual_probe_norm_is_finite=current_finite,exact_vs_original_binary64_norm=binary_comparison,
        differences_of_norms_are_not_componentwise_remainder_vectors=True,
        no_equality_of_new_and_old_trial_scalar_required=True)


def main():
    require_actions()
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native-directory',type=Path,required=True)
    ap.add_argument('--native-result-sha256',required=True)
    ap.add_argument('--probe-directory',type=Path,required=True)
    ap.add_argument('--probe-result-sha256',required=True)
    ap.add_argument('--r276-reference',type=Path,required=True)
    ap.add_argument('--r276-reference-sha256',required=True)
    ap.add_argument('--workers',type=int,default=2)
    ap.add_argument('--budget-seconds',type=float,default=1800.)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    E,Kmod=modules()
    E.require(args.native_result_sha256==NATIVE_RESULT_SHA,'Exact actual73 original result')
    E.require(args.r276_reference_sha256==REFERENCE_SHA,'Exact already-completed R276 report')
    E.require(args.workers in (1,2,3,4) and math.isfinite(args.budget_seconds) and args.budget_seconds>0,
              'Explicit finite positive resource budget and1..4 workers')
    native=E.Files(args.native_directory)
    E.require(native.root.name==E.PROFILES['native73']['directory'],'Original selected73 tree root, no relabelled input')
    out=args.out.resolve()
    for root in (native.root,args.probe_directory.resolve(),args.r276_reference.parent.resolve()):
        E.require(not out.is_relative_to(root) and not root.is_relative_to(out),'Independent diagnostic output directory')
    E.require(not os.path.lexists(args.out),'One fresh diagnostic output directory')
    out.mkdir(parents=True)
    started=time.monotonic();deadline=started+args.budget_seconds
    state=dict(started_monotonic=started,rows_completed=0,blocks_completed=0,stages_completed=0,complete=False)
    report=dict(schema=SCHEMA,source_sha256=digest(Path(__file__)),original_run_id=ORIGINAL_RUN,
        original_source_commit=ORIGINAL_COMMIT,original_nonlinear_iteration=ITERATION,
        alpha_exact=dict(numerator='1',denominator='512'),workers=args.workers,budget_seconds=args.budget_seconds,
        scientific_arithmetic_started=False,scientific_arithmetic_performed=False,byte_only_audit=False,
        diagnostic_completed=False,actual_errors=[],no_new_RHS_J_ODE_QR_or_nonlinear_trial_in_this_consumer=True,
        requested_new_complete_saved_matrix_actions_on_exact_realized_h=1,
        saved_delta_matrix_action_not_repeated=True,original_native_outcome_not_changed=True,
        used_as_native_or_other_scientific_acceptance_gate=False)
    bound=probe=reference_files=None
    try:
        profile=E.PROFILES['native73']
        report['original_frozen_source_receipts']=E.source_receipts(profile)
        report['additional_frozen_consumer_sources']=[dict(file=AFFINE_NAME,sha256=AFFINE_SHA),
            dict(file=KERNEL_NAME,sha256=KERNEL_SHA),dict(file=PROBE_NAME,sha256=PROBE_SHA),
            dict(file=PROBE_HOOK,sha256=PROBE_HOOK_SHA)]
        original_args=argparse.Namespace(native_result_sha256=args.native_result_sha256,
            partial_records_sha256=None,partial_trials_sha256=None)
        scope,records,groups,outer=E.load_native(original_args,profile,native)
        report['original_scope']=scope
        report['original_outcome']=E.write_json(out,'original-native-outcome.json',dict(original_scope=scope,
            actual_original_last_trials=groups.get(ITERATION,[]),new_diagnostic_not_yet_run=True,
            original_outcome_not_changed=True))
        E.require(len(records)==3 and records[ITERATION]['nonlinear_iteration']==ITERATION,'Actual73 final correction record exists')
        bound=E.bind_iteration(native,records[ITERATION],profile,outer)
        E.require(bound['snapshot_receipt']['sha256']==SNAPSHOT_SHA and
            bound['provenance']['direction_result']['sha256']==QR_RESULT_SHA and
            bound['identity']['current_state_sha256']==BASE_SHA and
            bound['qr']['native_delta']['sha256']==DELTA_SHA and
            bound['binding']['new_matrix_identity_sha256']==MATRIX_SHA and
            bound['provenance']['complete_original_J_raw_sha256']==J_SHA,'Complete fixed actual73 iteration2 identity')
        original_trials=groups.get(ITERATION,[])
        E.require(len(original_trials)==10,'All ten actual final-iteration original trials exist')
        probe=bind_probe(E,args,bound,original_trials[ALPHA_K],out,report)
        reference_files,reference_receipt,reference,reference_choice=bind_reference(E,args,bound)
        report['original_reference']=reference_receipt
        report['original_R276_chosen_prediction']=reference_choice
        report['original_R276_scope_flags']={key:reference[key] for key in ('no_RHS_J_ODE_QR_or_matrix_action',
            'actual_rounded_trial_state_not_reconstructed','no_componentwise_nonlinear_remainder_claimed')}
        report['probe_result']=probe['result_receipt']
        report['probe_original_result']=probe['result']
        report['probe_original_summary']=probe['summary']
        report['probe_scalar_comparison']=probe['scalar_comparison']
        report['binding']=E.write_json(out,'large-arrays/input-binding.json.gz',dict(
            schema='actual73-realized-step-exact-decomposition-input-binding-v1',
            original_current_matrix_binding=bound['binding'],original_provenance=bound['provenance'],
            original_R276_reference=reference_receipt,probe_result=probe['result_receipt'],
            probe_input_binding=probe['binding'],probe_array_manifest=probe['manifest'],
            reference_scope='Only the actual73 fixed finite matrix is used; no new J or solver',
            actual_h_definition='Exact dyadic difference of actual trial-state and base-state IEEE words; never binary64 subtraction'),compressed=True)
        report['scientific_arithmetic_started']=True
        report['scientific_arithmetic_performed']=True
        h,counts,hledger=build_h(E,Kmod,bound,probe,out,deadline)
        report['state_increment_counts']=counts
        report['complete_exact_state_increment_ledger']=hledger
        result=decompose(E,Kmod,bound,probe,reference,reference_choice,h,out,args.workers,deadline,state)
        report.update(result)
        report['diagnostic_completed']=True
        report['scope_limits']=[
            'All quantities are exact reals of the saved finite operands, followed by division by the original positive sigma.',
            'The realized h is an exact two-IEEE-word difference; no floating subtraction, nextafter or alternative trial is used.',
            'State-addition term means A*(h-alpha*delta), including the full original floating v+alpha*delta expression; multiplication and addition effects are not separately identified.',
            'Remaining flow/tangent-model term is stored_trial_r-(stored_base_r+A*h); no unique nonlinear/root/J/forward-error cause is inferred.',
            'Complete native trial mean-height increments are retained as original probe inputs but are not invented as extra native residual equations.',
            'This consumer selects no new direction or alpha and changes no nonlinear, domain, tolerance or acceptance rule.',
            'Decimal displays of exact ratios are not interval enclosures and are never used for comparisons.']
    except Exception as error:
        report['actual_errors'].append(dict(error=repr(error),traceback=traceback.format_exc()))
        report['resource_budget_exhausted']=isinstance(error,BudgetExhausted)
        if report['scientific_arithmetic_started'] and not report['scientific_arithmetic_performed']:
            report['scientific_arithmetic_performed']=None
    finally:
        report['complete_or_partial_decomposition_status']=state
        report['completed_new_complete_saved_matrix_actions_on_exact_realized_h']=int(state['complete'])
        report['elapsed_seconds']=time.monotonic()-started
        report['maximum_RSS_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report['maximum_child_RSS_kib']=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        if (out/'increment-status.json').is_file():
            report['complete_or_partial_increment_status']=dict(file='increment-status.json',
                bytes=(out/'increment-status.json').stat().st_size,sha256=digest(out/'increment-status.json'))
        inputs=dict(native_metadata_files=list(native.seen.values()))
        if bound is not None:
            inputs.update(original_snapshot_files=list(bound['snapshot_files'].seen.values()),
                          original_QR_input_files=list(bound['qr_files'].seen.values()),
                          QR_factor_payloads_not_reread=True)
        if probe is not None:inputs['actual_probe_files']=list(probe['files'].seen.values())
        if reference_files is not None:inputs['R276_reference_files']=list(reference_files.seen.values())
        report['input_files']=E.write_json(out,'large-arrays/complete-input-file-receipts.json.gz',inputs,compressed=True)
        full=E.write_json(out,'large-arrays/result.json.gz',report,compressed=True)
        small={key:report[key] for key in ('schema','source_sha256','original_run_id','original_source_commit',
            'original_nonlinear_iteration','alpha_exact','workers','budget_seconds','scientific_arithmetic_started',
            'scientific_arithmetic_performed','byte_only_audit','diagnostic_completed','actual_errors','elapsed_seconds',
            'maximum_RSS_kib','used_as_native_or_other_scientific_acceptance_gate')}
        small.update(full_result=full,original_outcome=report.get('original_outcome'),
            original_probe_result_copy=report.get('original_probe_result_copy'),
            original_probe_summary_copy=report.get('original_probe_summary_copy'),
            original_probe_outcome=report.get('original_probe_outcome'),
            complete_rows=state['rows_completed'],complete_blocks=state['blocks_completed'],
            complete_stages=state['stages_completed'],state_increment_counts=report.get('state_increment_counts'),
            exact_original_sigma_maxima=report.get('exact_original_sigma_maxima'),
            watched_original_rows=report.get('watched_original_rows'),
            norm_readback=report.get('norm_readback'),
            original_current_matrix_sha256=MATRIX_SHA,original_state_sha256=BASE_SHA,original_delta_sha256=DELTA_SHA,
            resource_budget_exhausted=report.get('resource_budget_exhausted',False),
            no_new_RHS_J_ODE_QR_or_nonlinear_trial_in_this_consumer=True,
            whole_componentwise_decomposition_complete=state['complete'])
        if len(json_bytes(small))>=95000:
            small.pop('watched_original_rows',None)
            small['watched_rows_in_full_report']=True
        if len(json_bytes(small))>=95000 and isinstance(small.get('exact_original_sigma_maxima'),dict):
            small['exact_original_sigma_maxima']={name:{key:value for key,value in item.items()
                if key!='all_exact_unscaled_vectors_at_row'} for name,item in small['exact_original_sigma_maxima'].items()}
            small['maximizing_row_cross_vectors_in_full_report']=True
        if len(json_bytes(small))>=95000:
            small['exact_maximum_brief']={name:{key:item[key] for key in
                ('kind','node','row','global_equation_row','component','mode','maximizing_rows')}
                |dict(exact_absolute_decimal_display=item['exact_absolute_scaled_value']['decimal_display_64_significant_digits'])
                for name,item in (small.pop('exact_original_sigma_maxima',None) or {}).items()}
            small.pop('norm_readback',None)
            small['all_full_exact_fractions_and_norm_relations_in_full_report']=True
        E.write_json(out,'summary.json',small)
    return 0 if report['diagnostic_completed'] else 2


if __name__=='__main__':
    raise SystemExit(main())

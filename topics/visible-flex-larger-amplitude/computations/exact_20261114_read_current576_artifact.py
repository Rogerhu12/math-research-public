#!/usr/bin/env python3
"""Actions-only readback of the actual61 current-native576 artifact.

Only saved bytes, JSON structure, IEEE words and source identities are
checked. Scientific reports are copied, never recomputed. No producer,
NumPy, SciPy, RHS/J/ODE, QR, matrix action, norm or rational arithmetic is
imported or called. A failed native solve remains a failed native solve;
this reader is neither a nonlinear acceptance test nor a new gate.

The complete artifact is fetched by the unchanged, SHA-locked public
transport already used by actual62. Its explicit CLI pin includes the
real run, artifact, complete ZIP size/hash and original head commit.
"""
from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import time
import traceback


HERE = Path(__file__).resolve().parent
REPOSITORY = 'Rogerhu12/math-research-public'
ORIGINAL_RUN = 43645948199
ORIGINAL_COMMIT = 'cf6b51193255dfc713610d2919598451ccdd49e2'
NATIVE_DIRECTORY = 'native-current576-damped'
SCHEMA = 'actual61-current-native576-complete-artifact-byte-readback-v1'
TRANSPORT_NAME = 'exact_20261114_fetch_pinned_public_artifact.py'
TRANSPORT_SHA = '51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859'
UTILITY_NAME = 'exact_20261114_audit_damped_chain_bytes.py'
UTILITY_SHA = '5618d29c41d95d668c959b05cee8295ce4285b2a50961277f557f8cfb717b440'
LAUNCHER = 'geometry_20261114_native_current576_damped_solve.py'
LAUNCHER_SHA = '06b8c44c115fcf754e963aeeb3adc04a26500cade3817018bae50e2e50aebc3b'
HOOK = 'geometry_20261114_native_current576_damped_solve_hook.mjs'
HOOK_SHA = '0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc'
SYSTEM = 'exact_20261114_current576_damped_system.py'
SYSTEM_SHA = '695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90'
PRODUCER = 'exact_20261114_current576_damped_chain_qr.py'
PRODUCER_SHA = 'ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f'
FACTOR = 'exact_20261114_native_damped_chain_qr.py'
FACTOR_SHA = '9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33'
KERNEL = 'exact_20261114_native_allrows_dyadic_residual.py'
KERNEL_SHA = '0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
BYTE_IO = 'geometry_20261114_native_captured_band_correction.py'
BYTE_IO_SHA = 'b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
CORE_SHA = 'ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3'
RUNTIME_SHA = 'f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f'
EVALUATE_SHA = '9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9'
INTERNAL_SOLVE_SHA = 'd7d063fe2fca25c1742c68ec8056902a583952b61cdda98e1d9eaab7c09f3615'
TRIAL_SHA = '603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99'
MODEL_SCOPE = 'R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates'
MATRIX_SCOPE = 'fresh-current-native576-finite-binary64-complete-J-r-sigma-chain'
PARENT_STATE = '384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03'
UNCHANGED = {
    'physical-height': 'c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f',
    'original-scales': 'ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc',
    'original-far-graph': '395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54',
    'cut-target': 'e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d'}
PARENT_PINS = {
    'result': ('result.json', 10047, 'c0a9b191e843e9036e84707ffa1855d5881dce13e4b71bf94812e9526b59d00e'),
    'summary': ('trial-replay-summary.json', 5762, '770b97e62eda7cbcc10b045c42298b95ef2c55a0f2dd5ac1930690175a156709'),
    'checkpoint': ('selected-state-checkpoint.json.gz', 1255992, '7659016c0218b8c2e9ba220ca81a0b410b7e38005ea609e417b9b534d76c3556'),
    'binary': ('selected-state.f64le.gz', 954571, '8ade070f746caed9a45c582c7485a060e55ee589858f5f88255d8ffd0d9112cb')}
SHAPES = {
    'base-states': [577, 224], 'stage-residuals': [576, 224], 'stage-out': [576, 224],
    'original-scales': [1, 577], 'cut-residual': [1, 112], 'end-residual': [1, 112],
    'original-far-graph': [1, 112], 'physical-height': [1, 112], 'cut-target': [1, 112],
    'stage-jacobians': [576, 224, 224]}
INPUT_NAMES = tuple(name for name in SHAPES if name != 'stage-jacobians')
SOURCE_PINS = {LAUNCHER: LAUNCHER_SHA, HOOK: HOOK_SHA, SYSTEM: SYSTEM_SHA,
    PRODUCER: PRODUCER_SHA, FACTOR: FACTOR_SHA, KERNEL: KERNEL_SHA, BYTE_IO: BYTE_IO_SHA,
    UTILITY_NAME: UTILITY_SHA, TRANSPORT_NAME: TRANSPORT_SHA}
CHUNK = 1024 * 1024


class AuditError(RuntimeError):
    pass


def require(condition, label):
    if not condition:
        raise AuditError(label)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(CHUNK), b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def write(out, name, value, compressed=False):
    target = out / name
    target.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    payload = gzip.compress(raw, compresslevel=9, mtime=0) if compressed else raw
    require(compressed or len(payload) < 100000, 'Small original-scalar report must remain below100KB')
    with target.open('xb') as stream:
        stream.write(payload)
    return dict(file=name, bytes=len(payload), sha256=sha(payload),
                raw_bytes=len(raw), raw_sha256=sha(raw), encoding='json-gzip' if compressed else 'json')


def load_byte_module(name, digest, alias):
    path = HERE / name
    require(file_sha(path) == digest, 'Frozen standard-library byte module '+name)
    spec = importlib.util.spec_from_file_location(alias, path)
    require(spec is not None and spec.loader is not None, 'Byte module import interface')
    module = importlib.util.module_from_spec(spec)
    sys.modules[alias] = module
    spec.loader.exec_module(module)
    return module


def fetch_original(args):
    """Same transport as actual62; only explicit pins/provenance are adapted."""
    module = load_byte_module(TRANSPORT_NAME, TRANSPORT_SHA, '_current576_artifact_transport')
    require(module.REPOSITORY == REPOSITORY and module.SCHEMA == 'pinned-public-actions-artifact-fetch-v3',
            'Unchanged complete public transport schema')
    pin = dict(run_id=args.run_id, artifact_id=args.artifact_id, artifact_name=args.artifact_name,
               expected_size=args.expected_size, expected_sha256=args.expected_sha256)
    old_metadata = module.read_metadata
    def metadata(opener, token):
        value, url = old_metadata(opener, token)
        require(value['workflow_run'].get('head_sha') == args.source_commit,
                'Actual native run original source commit')
        return value, url
    old_public = module.public_metadata
    def public(value):
        result = old_public(value)
        result['readback_adapter_not_GitHub_metadata'] = dict(
            schema=SCHEMA, source_file=Path(__file__).name, source_sha256=file_sha(__file__),
            original_transport_source_sha256=TRANSPORT_SHA,
            only_pin_metadata_and_schema_changed_in_memory=True,
            full_original_extraction_unchanged=True, mathematical_computation_performed=False)
        return result
    module.PIN = pin
    module.SCHEMA = 'current576-pinned-complete-public-artifact-readback-fetch-v1'
    module.read_metadata, module.public_metadata = metadata, public
    old_argv = sys.argv
    supplied = [str(HERE / TRANSPORT_NAME)]
    for key, value in pin.items():
        supplied += ['--'+key.replace('_', '-'), str(value)]
    supplied += ['--out', str(args.download_out)]
    try:
        sys.argv = supplied
        code = module.main()
    finally:
        sys.argv = old_argv
    require(code == 0, 'Complete pinned public artifact transport succeeded')
    receipt = read(args.download_out / module.RECEIPT_NAME)
    require(receipt['success'] is True and receipt['pinned_input'] == pin,
            'Complete original artifact receipt pin')
    require(receipt['download']['actual_sha256'] == args.expected_sha256,
            'Full ZIP bytes, not a partial HTTP selection')
    return args.download_out, receipt, module.RECEIPT_NAME


def subset(actual, expected, label):
    require(isinstance(actual, dict), label+' object')
    for key, value in expected.items():
        require(key in actual and actual[key] == value, label+' '+key)


def scalar_view(value):
    return {k:v for k,v in value.items()
            if v is None or isinstance(v, (bool, int, float)) or isinstance(v, str) and len(v) < 4000}


def number_record(record, label):
    """IEEE representation check only; nonfinite guard metadata is retained."""
    require(isinstance(record, dict) and re.fullmatch(r'[0-9a-f]{16}', record.get('float64le_hex', '')),
            label+' complete original word')
    raw = bytes.fromhex(record['float64le_hex'])
    w = int.from_bytes(raw, 'little'); exponent = (w >> 52) & 2047; fraction = w & ((1 << 52)-1)
    if exponent == 2047:
        expected = 'NaN' if fraction else ('negative-infinity' if w >> 63 else 'positive-infinity')
        require(record['classification'] == expected and record['value'] is None,
                label+' nonfinite class and JSON representation')
    else:
        negative_zero = w == (1 << 63)
        require(record['classification'] == ('negative-zero' if negative_zero else 'finite'), label+' finite class')
        require(type(record['value']) in (int, float), label+' numeric JSON value')
        if negative_zero:
            require(record['value'] == 0, label+' signed-zero JSON magnitude')
        else:
            require(struct.pack('<d', record['value']) == raw, label+' original value/word representation')
    return raw


def parent_binding(parent):
    subset(parent, dict(public_run='43640772654', states_float64le_sha256=PARENT_STATE,
                       height_float64le_sha256=UNCHANGED['physical-height']), 'Selected actual59 source')
    for key, values in PARENT_PINS.items():
        require(tuple(parent[key][x] for x in ('file', 'bytes', 'sha256')) == values,
                'Already audited actual59 source receipt '+key)


def descriptor_json(files, descriptor):
    value = files.json(descriptor)
    observed = files.records[descriptor['file']]
    for key, field in (('raw_bytes', 'decompressed_bytes'), ('raw_sha256', 'decompressed_sha256')):
        if key in descriptor:
            require(observed.get(field, observed['bytes' if key == 'raw_bytes' else 'sha256']) == descriptor[key],
                    'Complete compressed descriptor '+key)
    return value


def plain_receipt(files, name):
    """Original JS receipt has only these fields, even after gzip was read."""
    value=files.info(name)
    return {key:value[key] for key in ('file','bytes','sha256')}


def merge_files(parent, child, prefix):
    for relative, record in child.records.items():
        name = prefix+'/'+relative
        copied = dict(record, file=name)
        if name in parent.records:
            require(parent.records[name]['sha256'] == record['sha256'], 'Same original file from overlapping receipts')
        parent.records[name] = copied


def core_identity(files, desc, spec_sha):
    core = descriptor_json(files, desc)
    subset(core, dict(schema='current-native576-correction-only-core-instrumentation-v1',
        source_sha256=LAUNCHER_SHA, hook_sha256=HOOK_SHA, spec_sha256=spec_sha,
        original_core_file_sha256=CORE_SHA, original_runtime_core_sha256=RUNTIME_SHA,
        original_evaluate_source_sha256=EVALUATE_SHA, actual_evaluate_source_sha256=EVALUATE_SHA,
        original_ten_trial_body_sha256=TRIAL_SHA, instrumented_ten_trial_body_sha256=TRIAL_SHA,
        exact_correction_call_roundtrip_verified=True, original_evaluate_body_byte_identical=True,
        original_ten_trial_body_byte_identical=True, only_nonlinear_correction_call_replaced=True,
        no_cached_baseline=True, no_planned_one_step_stop=True), 'Original core source instrumentation')
    inner = core['internal_solve_source_identity']
    before = inner['original_internal_solve_source']; after = inner['instrumented_internal_solve_source']
    change = inner['replacement']
    require(sha(before.encode()) == inner['original_internal_solve_source_sha256'] == INTERNAL_SOLVE_SHA,
            'Original internal solve full source identity')
    require(sha(after.encode()) == inner['instrumented_internal_solve_source_sha256'],
            'Instrumented internal solve full source identity')
    require(change['before'] == 'const cor=correction(ev,states,target);' and
            before.count(change['before']) == 1 and after.count(change['after']) == 1 and
            after.replace(change['after'], change['before'], 1) == before,
            'Exactly reversible one-call correction replacement')
    return core


class SnapshotBytes:
    """Streaming raw-byte binder, independent of the scientific adapter."""
    def __init__(self, U, directory, record, spec, live, spec_sha):
        self.U = U; self.files = U.Files(directory); self.raw_cache = {}; self.stage_records = []
        self.result = self.files.json('result.json'); r = self.result
        subset(r, dict(schema='current-native576-withJ-snapshot-result-v1', snapshot_completed=True,
            source_sha256=LAUNCHER_SHA, hook_sha256=HOOK_SHA, native_call=1,
            nonlinear_iteration=record['nonlinear_iteration'], snapshot_sequence=record['snapshot_sequence'],
            M=112, K=224, depth=576, original_fresh_withJ_already_returned=True,
            new_RHS_J_ODE_calls_by_snapshot=0), 'One actual fresh snapshot')
        require(self.files.info('result.json')['sha256'] == record['snapshot']['sha256'],
                'Bridge points to this complete snapshot result')
        self.context = descriptor_json(self.files, r['context']); c = self.context
        self.manifest = descriptor_json(self.files, r['manifest']); m = self.manifest
        subset(c, dict(schema='current-native576-withJ-snapshot-context-v1', source_sha256=LAUNCHER_SHA,
            hook_sha256=HOOK_SHA, native_call=1, nonlinear_iteration=r['nonlinear_iteration'],
            snapshot_sequence=r['snapshot_sequence'], fresh_current_evaluate_completed=True,
            no_cached_baseline=True, snapshot_does_not_call_RHS_J_ODE=True,
            no_cut_or_far_zero_assumption=True, original_evaluate_and_flow_source_not_instrumented=True),
            'Fresh source context')
        parent_binding(c['parent_selected59'])
        require(c['parent_selected59'] == spec['parent_selected59'], 'Same selected parent provenance at every iteration')
        require(c['numerical_configuration'] == spec['numerical_configuration'], 'Complete frozen numerical configuration')
        require(c['original_sources'] == {k:v for k,v in spec['original_source_sha256'].items()
                                         if k not in ('input_config', 'runtime_config')}, 'Complete numerical source ledger')
        require(c['parameters'] == live['parameters'] and c['rawNode'] == live['rawNode'] == list(range(0,577,72))
                and c['cells'] == live['stages'] and len(c['cells']) == 576, 'Complete original stages and nine physical nodes')
        for a,b in (('graphs_sha256','graphs_float64le_sha256'), ('gains_sha256','gains_float64le_sha256'),
                    ('far_graph_sha256','far_graph_float64le_sha256')):
            require(c[a] == live[b], 'Unchanged complete original '+a)
        self.core = core_identity(self.files, c['core_instrumentation'], spec_sha)
        for name in ('norm', 'minA', 'minD'):
            number_record(c['current_original_'+name], 'Current '+name)
            require(c['current_original_'+name] == r['actual_current_original_'+name], 'Same exact current scalar record')
        require(record['source_current_withJ_norm'] == c['current_original_norm'], 'Original withJ norm recorded before child')
        subset(m, dict(schema='current-native576-withJ-snapshot-arrays-v1', source_sha256=LAUNCHER_SHA,
            hook_sha256=HOOK_SHA, native_call=1, nonlinear_iteration=r['nonlinear_iteration'],
            snapshot_sequence=r['snapshot_sequence'], M=112, K=224, depth=576), 'All current raw arrays manifest')
        self.arrays = {e['name']:e for e in m['arrays']}
        require(len(self.arrays) == len(m['arrays']) and set(self.arrays) == set(SHAPES), 'All ten unique complete snapshot arrays')
        self.locations = []; self.total_bytes = 0; self.chunks = 0; used_files = set()
        for name, shape in SHAPES.items():
            entry = self.arrays[name]
            subset(entry, dict(dtype='<f8', order='C', shape=shape, completed=True), 'Current array '+name)
            width = U.product_shape(shape[1:])*8; count = 0; full = hashlib.sha256(); pieces = []
            for index, chunk in enumerate(entry['chunks']):
                subset(chunk, dict(array=name, chunk_index=index, row_start=count), 'Ordered complete snapshot chunk')
                stop = chunk['row_stop']; require(type(stop) is int and count < stop <= shape[0], 'Complete chunk row interval')
                require(chunk['file'] not in used_files, 'No snapshot payload alias')
                used_files.add(chunk['file'])
                raw = self.files.raw(chunk)
                require(len(raw) == (stop-count)*width and sha(raw) == chunk['raw_sha256'], 'Complete current chunk raw bytes')
                full.update(raw)
                if name == 'stage-jacobians':
                    for n in range(count, stop):
                        offset = (n-count)*width; block = raw[offset:offset+width]
                        self.stage_records.append(dict(stage=n, original_stage=n, bytes=width,
                            raw_sha256=sha(block), origin='this-fresh-current-withJ-evaluate',
                            current_native_stage_location=c['cells'][n]))
                        self.locations.append(dict(file=chunk['file'], offset=offset, bytes=width))
                else:
                    pieces.append(raw)
                count = stop; self.chunks += 1
            require(count == shape[0] and entry['total_bytes'] == U.product_shape(shape)*8 and
                    full.hexdigest() == entry['raw_sha256'] == c['raw_array_sha256'][name],
                    'Every byte and row of current array '+name)
            self.total_bytes += entry['total_bytes']
            if name != 'stage-jacobians': self.raw_cache[name] = b''.join(pieces)
        require(len(self.stage_records) == 576, 'Every current J block independently byte hashed')
        require(set(c['raw_array_sha256']) == set(SHAPES), 'No omitted current raw identity')
        for name, digest in UNCHANGED.items():
            require(self.arrays[name]['raw_sha256'] == digest, 'Unchanged actual source '+name)
        require(record['current_state_sha256'] == r['current_state_sha256'] == self.arrays['base-states']['raw_sha256'],
                'Whole actual current state identity')
        if r['nonlinear_iteration'] == 0:
            require(r['current_state_sha256'] == PARENT_STATE, 'Initial current state is exactly actual59 selected state')
        flow = descriptor_json(self.files, c['flow_return_metadata'])
        subset(flow, dict(schema='current-native576-original-flow-return-scalars-v1', native_call=1,
            nonlinear_iteration=r['nonlinear_iteration'], snapshot_sequence=r['snapshot_sequence']), 'Original per-flow scalar readout')
        require(len(flow['rows']) == 576, 'All original flow scalar rows')
        for n, row in enumerate(flow['rows']):
            subset(row, dict(stage=n, rawCell=c['cells'][n]['rawCell'], rawSegment=c['cells'][n]['rawSegment']), 'Flow location')
            for key in ('meanHeight', 'minA', 'minD'): number_record(row[key], 'Saved flow '+key)
        self.flow = flow
        self.result_receipt = self.files.info('result.json')
        self.record = dict(result=self.result_receipt, context=r['context'], manifest=r['manifest'],
            native_call=1, nonlinear_iteration=r['nonlinear_iteration'], snapshot_sequence=r['snapshot_sequence'],
            current_state_sha256=r['current_state_sha256'], arrays=10, J_blocks=576,
            complete_raw_bytes=self.total_bytes, complete_chunks=self.chunks,
            raw_array_sha256=c['raw_array_sha256'], first_state_is_selected59=(r['nonlinear_iteration']==0),
            saved_original_norm=c['current_original_norm'], saved_original_minA=c['current_original_minA'],
            saved_original_minD=c['current_original_minD'], actual_cut_and_far_arrays_not_reformed=True,
            fresh_evaluate_claim_bound_to_original_source_and_complete_snapshot=True,
            nonlinear_state_update_not_recomputed=True)

    def raw(self, name):
        return self.raw_cache[name]

    def stage(self, n):
        location = self.locations[n]
        with self.files.path(location['file']).open('rb') as stream:
            stream.seek(location['offset']); raw = stream.read(location['bytes'])
        require(sha(raw) == self.stage_records[n]['raw_sha256'], 'Immutable witness current J block')
        return raw, location


def audit_witness(U, files, desc, maximum, binding, delta, original, snapshot):
    report = descriptor_json(files, desc); w = report['operands']; matrix = binding['new_matrix_identity_sha256']
    subset(report, dict(source_sha256=PRODUCER_SHA, kernel_sha256=KERNEL_SHA,
        new_matrix_identity_sha256=matrix, direction_float64le_sha256=sha(delta),
        exact_original_sigma_maximum=maximum, snapshot_result=snapshot.result_receipt,
        native_call=1, nonlinear_iteration=snapshot.result['nonlinear_iteration'],
        snapshot_sequence=snapshot.result['snapshot_sequence'], current_state_sha256=snapshot.result['current_state_sha256']),
        'Current exact witness identity')
    n,j,kind = w['node'],w['row'],w['kind']
    require((n,j,kind) == (maximum['node'],maximum['row'],maximum['kind']), 'Saved witness location')
    subset(w, dict(matrix_scope=MATRIX_SCOPE, new_matrix_identity_sha256=matrix,
        snapshot_result_sha256=snapshot.result_receipt['sha256'], current_state_sha256=snapshot.result['current_state_sha256'],
        nonlinear_iteration=snapshot.result['nonlinear_iteration'], snapshot_sequence=snapshot.result['snapshot_sequence'],
        complete_direction_float64le_sha256=sha(delta)), 'Worst original operand provenance')
    def word(raw,index): return raw[index*8:(index+1)*8].hex()
    require(w['original_sigma_float64le_hex'] == word(original['original-scales'],n), 'Worst original sigma word')
    location = None
    if kind == 'stage':
        require(w['full_next_delta_float64le_hex'] == delta[(n+1)*224*8:(n+2)*224*8].hex() and
                w['current_delta_float64le_hex'] == word(delta,n*224+j) and
                w['original_residual_float64le_hex'] == word(original['stage-residuals'],n*224+j),
                'Worst stage complete delta and original residual words')
        J, location = snapshot.stage(n)
        require(w['original_J_stage_sha256'] == sha(J) == binding['complete_block_manifest'][n]['raw_sha256'] and
                w['full_original_J_row_float64le_hex'] == J[j*224*8:(j+1)*224*8].hex() and
                w['original_stage_location'] == snapshot.context['cells'][n], 'Worst original current J row and cell')
    elif kind == 'cut':
        require(w['current_delta_float64le_hex'] == word(delta,j) and
                w['original_residual_float64le_hex'] == word(original['cut-residual'],j), 'Worst original cut operands')
    elif kind == 'far':
        require(w['delta_Q_float64le_hex'] == word(delta,576*224+j) and
                w['delta_Pi_float64le_hex'] == word(delta,576*224+112+j) and
                w['original_far_G_float64le_hex'] == word(original['original-far-graph'],j) and
                w['original_residual_float64le_hex'] == word(original['end-residual'],j), 'Worst original far operands')
    else:
        raise AuditError('Unknown original current row kind')
    return dict(all_saved_worst_operand_words_equal=True, actual_J_source_chunk=location,
                no_products_sums_divisions_or_rational_comparisons_performed=True)


def qr_arrays(U, files, result):
    manifest = descriptor_json(files, result['array_manifest'])
    subset(manifest, dict(schema='complete-native-current576-damped-direction-arrays-v1',
        source_sha256=PRODUCER_SHA, factor_engine_source_sha256=FACTOR_SHA,
        all_arrays_artifact_only=True, native_accepted=False), 'Current QR array manifest')
    entries = manifest['arrays']; by_name = {d['name']:d for d in entries}; by_file = {d['file']:d for d in entries}
    require(len(entries) == len(by_name) == len(by_file), 'Unique current output array names and paths')
    audits = []
    for n, desc in enumerate(entries):
        if desc['dtype'] == '<f8':
            audits.append(files.classify_f64(desc))
        else:
            require(desc['dtype'] == 'exact-dyadic-jsonl-gzip', 'Known complete integer ledger payload')
            files.check(desc)
        if (n+1) % 128 == 0:
            print(json.dumps(dict(event='current576_saved_array_bytes', iteration=result.get('nonlinear_iteration'),
                                  arrays=n+1, total=len(entries))), flush=True)
    return manifest, by_name, by_file, audits


def audit_complete_qr(U, files, result, snapshot, record, spec):
    iteration = snapshot.result['nonlinear_iteration']; sequence = snapshot.result['snapshot_sequence']
    identity = dict(snapshot_result=snapshot.result_receipt, native_call=1,
        nonlinear_iteration=iteration, snapshot_sequence=sequence,
        current_state_sha256=snapshot.result['current_state_sha256'])
    subset(result, dict(schema='complete-native-current576-damped-square-root-direction-v1',
        source_sha256=PRODUCER_SHA, system_source_sha256=SYSTEM_SHA, factor_engine_source_sha256=FACTOR_SHA,
        kernel_source_sha256=KERNEL_SHA, model_scope=MODEL_SCOPE, diagnostic_completed=True,
        linear_direction_computed=True, native_accepted=False, task_completed=False,
        original_native_calls_in_this_child=0, new_RHS_calls_in_this_child=0,
        new_J_calls_in_this_child=0, new_ODE_steps_in_this_child=0, nonlinear_trials_in_this_child=0,
        exact_linear_defect_not_used_as_new_native_trial_gate=True, **identity), 'Complete fresh-current QR result')
    require(result['eta_cli_text'] == spec['bridge']['eta_cli_text'] and
            result['eta_binary64'] == spec['bridge']['eta_binary64'], 'Same explicit algorithm eta')
    number_record(result['eta_binary64'], 'Explicit eta')
    summary = files.json('summary.json'); files.check(summary['full_result'])
    for key in set(summary).intersection(result)-{'schema'}:
        require(summary[key] == result[key], 'Original small/full QR report '+key)
    binding = descriptor_json(files, result['input_binding']); matrix = binding['new_matrix_identity_sha256']
    subset(binding, dict(schema='current-native576-complete-linear-system-binding-v1', matrix_scope=MATRIX_SCOPE,
        adapter_source_sha256=SYSTEM_SHA, frozen_byte_io_source_sha256=BYTE_IO_SHA,
        snapshot_result_sha256=snapshot.result_receipt['sha256'], snapshot_context_sha256=snapshot.result['context']['sha256'],
        snapshot_manifest_sha256=snapshot.result['manifest']['sha256'], modes=112, shape_dimension=224,
        depth=576, original_depth=576, node_count=577, old_to_new=list(range(577)),
        raw_array_sha256=snapshot.context['raw_array_sha256'], complete_block_manifest=snapshot.stage_records,
        complete_chunks=snapshot.chunks, complete_raw_bytes=snapshot.total_bytes,
        full_current_J_raw_sha256=snapshot.arrays['stage-jacobians']['raw_sha256'],
        fresh_current_evaluate_completed=True, no_cached_baseline=True, no_zero_cut_or_far_assumption=True,
        current_cut_far_errors_not_projected_or_zeroed=True, **identity), 'Complete current matrix binding')
    for key in ('parent_selected59','original_sources','numerical_configuration','parameters','rawNode','cells',
                'graphs_sha256','gains_sha256','far_graph_sha256'):
        require(binding[key] == snapshot.context[key], 'Same complete current context in child '+key)
    require(canonical_sha(binding['matrix_identity_definition']) == matrix == result['new_matrix_identity_sha256'],
            'Canonical complete current matrix identity')
    definition = binding['matrix_identity_definition']
    require(definition['matrix_scope'] == MATRIX_SCOPE and
            definition['full_current_J_raw_sha256'] == snapshot.arrays['stage-jacobians']['raw_sha256'] and
            definition['current_input_raw_sha256'] == {k:snapshot.arrays[k]['raw_sha256'] for k in INPUT_NAMES} and
            definition['block_manifest'] == [{k:d[k] for k in ('stage','bytes','raw_sha256')} for d in snapshot.stage_records],
            'Every J/input member retained in exact target identity')
    manifest, by_name, by_file, raw_audits = qr_arrays(U, files, result)
    subset(manifest, dict(new_matrix_identity_sha256=matrix, **identity), 'Output manifest current identity')
    def member(desc):
        require(desc == by_file[desc['file']], 'Full output descriptor alias')
        return files.raw(desc)
    original = result['original_arrays']; require(set(original) == set(INPUT_NAMES), 'All nine complete copied inputs')
    raw_inputs = {name:member(desc) for name,desc in original.items()}
    for name, desc in original.items():
        require(raw_inputs[name] == snapshot.raw(name) and desc['shape'] == SHAPES[name] and
                desc['sha256'] == snapshot.arrays[name]['raw_sha256'], 'Original snapshot input copied unchanged '+name)
    sigma = raw_inputs['original-scales']
    factor = descriptor_json(files, result['factor_report']); index = descriptor_json(files, result['factor_index'])
    inventory = descriptor_json(files, result['formed_stage_inventory'])
    require(factor['complete'] is True and index['complete'] is True and factor['source_sha256'] == FACTOR_SHA and
            index['source_sha256'] == inventory['source_sha256'] == PRODUCER_SHA and
            index['factor_engine_source_sha256'] == inventory['factor_engine_source_sha256'] == FACTOR_SHA,
            'Borrowed frozen factor engine and current entry identities')
    require(factor['input_matrix_identity_sha256'] == index['new_matrix_identity_sha256'] ==
            inventory['new_matrix_identity_sha256'] == matrix, 'Factor/formation complete current target')
    subset(index, identity, 'Factor-index current identity'); subset(inventory, identity, 'Formed-inventory current identity')
    for key,value in result['factor_summary'].items(): require(factor[key] == value, 'Saved factor summary '+key)
    subset(factor, dict(rows=129248, columns=129248, augmented_rows=258496, stage_count=576, node_count=577,
        block_width=224, node_penalty_blocks=577, pure_constant_rows=129248, qr_calls=1153, formation_calls=1152,
        eta_binary64=result['eta_binary64'], model_scope=MODEL_SCOPE), 'All original R273 rows/penalties/counts')
    factors = index['factors']; require(len(factors) == 577, 'Every complete factor node')
    total_bytes = constants = lower_words = 0
    for n, item in enumerate(factors):
        final = n == 576; cols = 225 if final else 449
        count = 336 if final else 112 if n == 0 else 224
        require(item['node'] == n and item['final'] == final and item['R_columns'] == [0,224] and
                item['S_columns'] == (None if final else [224,448]) and item['affine_column'] == (224 if final else 448),
                'Complete square-root block columns and order')
        require(item['factor']['shape'] == [224,cols] and item['constant']['shape'] == [count],
                'Complete R/S/affine and pure-constant raw shapes')
        raw = member(item['factor']); member(item['constant'])
        for row in range(224):
            require(not any(raw[row*cols*8:(row*cols+row)*8]), 'Literal saved lower R triangle is all zero bytes')
            lower_words += row
        total_bytes += item['factor']['bytes']+item['constant']['bytes']; constants += count
    require(total_bytes == factor['actual_factor_and_constant_bytes'] == factor['expected_factor_and_constant_bytes'] == 464891392
            and constants == 129248, 'All 577 factors and all pure constants physically retained')
    stages = inventory['stages']; require(len(stages) == 576, 'Every formed-stage provenance row')
    for n, item in enumerate(stages):
        require(item['stage'] == n and item['original_J_raw_sha256'] == snapshot.stage_records[n]['raw_sha256'],
                'Formation uses this exact current J block')
        U.number_word(item['original_sigma_current'], sigma[n*8:(n+1)*8], 'Formation current sigma')
        U.number_word(item['original_sigma_next'], sigma[(n+1)*8:(n+2)*8], 'Formation next sigma')
    formed_hash = canonical_sha(dict(original_matrix=matrix, sigma=original['original-scales']['sha256'],
        eta_bits=result['eta_binary64']['float64le_hex'], source_sha256=FACTOR_SHA, precision=factor['working_precision'],
        stages=[{k:d[k] for k in ('stage','original_J_raw_sha256','formed_V_raw_sha256','formed_rho_raw_sha256',
            'combined_formed_bytes_sha256','original_sigma_current','original_sigma_next')} for d in stages],
        cut=factor['formed-cut-rho']['array'], far=factor['formed-far-rho']['array']))
    require(formed_hash == factor['formed_model_identity_sha256'] == inventory['formed_model_identity_sha256'] ==
            result['formed_model_diagnostic']['model_identity_sha256'], 'Actual formed-model complete metadata identity')
    member(factor['formed-cut-rho']['array']); member(factor['formed-far-rho']['array'])
    solve = factor['solve']; z = member(solve['scaled_z']); delta = member(solve['delta'])
    require(solve['delta'] == result['native_delta'] and solve['triangular_solves'] == 577 and
            result['native_delta']['shape'] == solve['scaled_z']['shape'] == [577,224], 'Whole z and original-coordinate direction')
    underflows = sum(1 for (zw,),(dw,) in zip(U.words(z),U.words(delta))
                     if zw & U.MASK_ABS and not dw & U.MASK_ABS)
    require(underflows == solve['nonzero_recovery_to_zero'], 'Saved recovery underflow bit classification')
    for example in solve['recovery_underflow_examples']:
        n,j = example['node'],example['column']; offset = (n*224+j)*8
        U.number_word(example['z'],z[offset:offset+8],'Saved recovery z')
        U.number_word(example['sigma'],sigma[n*8:(n+1)*8],'Saved recovery sigma')
        U.number_word(example['delta'],delta[offset:offset+8],'Saved recovery delta')
    cp = descriptor_json(files, result['native_direction_checkpoint'])
    subset(cp, dict(schema='complete-native-current576-damped-direction-v1', source_sha256=PRODUCER_SHA,
        system_source_sha256=SYSTEM_SHA, factor_engine_source_sha256=FACTOR_SHA, input_binding=binding,
        M=112, K=224, depth=576, original_depth=576, old_to_new=list(range(577)),
        eta_binary64=result['eta_binary64'], model_scope=MODEL_SCOPE, full_current576_direction=True,
        not_a_restriction_of_a1372_direction=True, original_cut_and_far_direction_components_not_projected_or_zeroed=True,
        native_accepted=False, task_completed=False, **identity), 'Complete actual current direction checkpoint')
    require(U.checkpoint_bytes(cp,577,224,'Current576 full direction') == delta,
            'All direction checkpoint words and negative zero signs')
    exact = result['original_exact_readback']; detail = descriptor_json(files,exact['full_report'])
    subset(detail, dict(schema='current-native576-complete-exact-direction-readback-v1',
        source_sha256=PRODUCER_SHA, system_source_sha256=SYSTEM_SHA, kernel_sha256=KERNEL_SHA,
        matrix_scope=MATRIX_SCOPE, new_matrix_identity_sha256=matrix, direction_label='current_damped',
        direction_float64le_sha256=result['native_delta']['sha256'], exact_rows=129248,
        completed_stages=576, original_product_positions=576*224*224+112,
        eta_not_in_original_equations=True, readback_uses_unscaled_J_and_r_before_exact_sigma_division=True,
        no_float_refinement_RHS_formed=True, used_as_new_nonlinear_acceptance_gate=False, **identity),
        'All current original rows exact readback provenance')
    for key in ('exact_global_original_sigma_norm','exact_stored_base_sigma_norm','actual_original_withJ_norm',
                'exact_rows','completed_stages','original_product_positions','all_exact_residual_rows','worst_witness',
                'no_float_refinement_RHS_formed','used_as_new_nonlinear_acceptance_gate'):
        require(exact[key] == detail[key], 'Same saved complete exact readout '+key)
    require(detail['actual_original_withJ_norm'] == snapshot.context['current_original_norm'], 'Recorded original withJ norm is current')
    ledger_desc = exact['all_exact_residual_rows']; require(ledger_desc == by_file[ledger_desc['file']], 'Complete exact ledger descriptor alias')
    ledger = U.audit_ledger(files, ledger_desc, detail, binding, result['native_delta']['sha256'], sigma,112,224,576)
    with gzip.open(files.path(ledger_desc['file']),'rb') as stream:
        for line in stream:
            row = json.loads(line)
            subset(row, dict(direction_label='current_damped', new_matrix_identity_sha256=matrix, **identity), 'Every exact block belongs to this current call')
            subset(row['exact_original_sigma_maximum'], dict(matrix_scope=MATRIX_SCOPE,
                snapshot_result_sha256=snapshot.result_receipt['sha256'], nonlinear_iteration=iteration,
                snapshot_sequence=sequence), 'Each saved exact maximum current source')
    witness = audit_witness(U, files, exact['worst_witness'], detail['exact_global_original_sigma_norm'],
                            binding, delta, raw_inputs, snapshot)
    all_files = files.complete_inventory()
    full = dict(schema='current576-complete-iteration-byte-audit-detail-v1', identity=identity,
        source_result=files.info('result.json.gz'), complete_files=all_files, raw_arrays=raw_audits,
        factors=factors, snapshot=snapshot.record, exact_ledger=ledger, witness=witness,
        snapshot_files=snapshot.files.complete_inventory(), current_matrix_binding=binding)
    short = dict(schema='current576-complete-iteration-byte-audit-summary-v1', passed=True, **identity,
        result=files.info('result.json.gz'), new_matrix_identity_sha256=matrix, formed_model_identity_sha256=formed_hash,
        verified_arrays=len(by_file), verified_float64_arrays=len(raw_audits), complete_factor_nodes=577,
        complete_factor_and_constant_bytes=total_bytes, complete_pure_constant_rows=constants,
        verified_literal_lower_R_zero_words=lower_words, checkpoint_matches_full_raw_delta=True,
        saved_recovery_underflow_count=underflows, exact_ledger=ledger, witness=witness,
        copied_Actions_factor_summary=result['factor_summary'], copied_Actions_solve=solve,
        copied_Actions_formed_model=result['formed_model_diagnostic'], copied_Actions_exact_readback=exact,
        no_scientific_values_recomputed=True, used_as_native_acceptance_gate=False,
        unexported_formed_V_and_rho_only_bound_by_saved_hashes_not_reformed=True)
    return short, full, binding


def audit_partial_qr(U, files, result):
    """Retain an honest partial scope; never promote partial factors to a solve."""
    subset(result, dict(schema='complete-native-current576-damped-square-root-direction-v1',
        source_sha256=PRODUCER_SHA, system_source_sha256=SYSTEM_SHA, factor_engine_source_sha256=FACTOR_SHA,
        kernel_source_sha256=KERNEL_SHA, native_accepted=False, task_completed=False), 'Partial child original identity')
    manifest, names, paths, arrays = qr_arrays(U,files,result)
    factor_index = None
    if 'factor_index' in result:
        factor_index = descriptor_json(files,result['factor_index'])
        require(len(factor_index['factors']) <= 577, 'Partial factor list count')
        for n,item in enumerate(factor_index['factors']):
            require(item['node'] == n and item['factor'] == paths[item['factor']['file']] and
                    item['constant'] == paths[item['constant']['file']], 'All declared partial factor/constant descriptors')
    for key in ('input_binding','factor_report','formed_stage_inventory','native_direction_checkpoint'):
        if key in result: descriptor_json(files,result[key])
    if 'native_delta' in result:
        require(result['native_delta'] == paths[result['native_delta']['file']], 'Partial saved full direction descriptor')
    complete_files = files.complete_inventory()
    return dict(schema='current576-partial-child-byte-audit-v1', passed=True,
        completed_original_row_scope_claimed=False, producer_result=files.info('result.json.gz'),
        original_status=scalar_view(result), verified_arrays=len(paths), raw_arrays=arrays,
        partial_factor_index=factor_index, complete_files=complete_files,
        original_factor_summary=result.get('factor_summary'), original_error=result.get('actual_error'))


def current_loop_metadata(U, files, outer, out):
    """Original saved scalars only; independent of scientific outcome."""
    spec = descriptor_json(files, outer['specification'])
    require(files.info(outer['specification']['file'])['sha256'] == outer['spec_sha256'], 'Current specification original bytes')
    subset(spec, dict(schema='native-current576-damped-solve-spec-v1', source_sha256=LAUNCHER_SHA,
        hook_sha256=HOOK_SHA, selected_state_float64le_sha256=PARENT_STATE,
        current_state_withJ_required_at_every_original_iteration=True, no_cached_baseline=True,
        only_nonlinear_correction_call_replaced=True, original_ten_trial_body_retained=True,
        original_final_endpoint_J_and_fresh_audit_retained=True, soft_cut_and_far_direction_not_projected=True),
        'Full current native request contract')
    parent_binding(spec['parent_selected59'])
    require(spec['parent_selected59'] == outer['parent_selected59'], 'Native outer parent source receipts')
    subset(spec['bridge'], dict(source_file=PRODUCER, source_sha256=PRODUCER_SHA,
        system_source_file=SYSTEM, system_source_sha256=SYSTEM_SHA, factor_engine_source_sha256=FACTOR_SHA,
        kernel_source_sha256=KERNEL_SHA, shell=False, stdout_and_stderr_are_iteration_files=True, model_scope=MODEL_SCOPE),
        'Synchronous scientific child source and I/O contract')
    require(spec['bridge']['eta_cli_text'] == outer['eta_cli_text'] and
            spec['bridge']['eta_binary64'] == outer['eta_binary64'], 'Same explicit outer/child eta')
    require(spec['original_max_iterations'] == outer['original_max_iterations'] ==
            spec['numerical_configuration']['maxIterations'] and
            spec['original_solve_tolerance'] == outer['original_tolerance'] ==
            spec['numerical_configuration']['solveTolerance'], 'Original iteration/tolerance settings copied unchanged')
    source_files = []
    for name,digest in {**spec['frozen_sources'], LAUNCHER:LAUNCHER_SHA, HOOK:HOOK_SHA,
                        UTILITY_NAME:UTILITY_SHA, TRANSPORT_NAME:TRANSPORT_SHA}.items():
        require(Path(name).name == name and re.fullmatch(r'[0-9a-f]{64}',digest), 'Ordinary complete source basename/hash')
        path = HERE/name
        require(path.is_file() and file_sha(path) == digest, 'This reader checkout preserves frozen producer '+name)
        source_files.append(dict(file=name,bytes=path.stat().st_size,sha256=digest))
    launch = files.json('verified-launch-intent.json')
    subset(launch, dict(schema='native-current576-damped-verified-launch-v1', spec_sha256=outer['spec_sha256'],
        source_sha256=LAUNCHER_SHA, hook_sha256=HOOK_SHA, identity_verified_before_request=True,
        initial_native_solve_calls=0, initial_response_cache_empty=True), 'Original verified launch')
    require(launch['parent_selected59'] == spec['parent_selected59'] and launch['inputs'] == spec['inputs'] and
            launch['request'] == spec['fresh_request'] and spec['fresh_request']['jacobian'] is True and
            spec['fresh_request']['audit'] is True, 'Complete unchanged H and requested final J/audit')
    require(files.info('native_ready.json.gz')['sha256'] == launch['complete_current_ready_sha256'] and
            files.info('native_capacity.json')['sha256'] == launch['current_capacity_sha256'], 'Original ready and capacity files')
    live = files.json('original-live-identity-before-selected-seed.json')
    require(live == spec['original_live_identity'] and live['rawNode'] == list(range(0,577,72)) and
            len(live['stages']) == 576, 'Full original live identity and complete stage layout')
    core_desc = files.info('core-instrumentation.json'); core = core_identity(files,core_desc,outer['spec_sha256'])
    methods = files.json('actual-current-method-identities.json')
    for field,hash_field,digest in (
        ('actual_public_evaluate_source','actual_public_evaluate_sha256',EVALUATE_SHA),
        ('actual_public_tail_solve_source','actual_public_tail_solve_sha256','283de19115a958e0268f6a719e17c53aa9c0a5473692d8a22aa09bf28b81378a'),
        ('actual_public_dn_solve_source','actual_public_dn_solve_sha256','f80eaeff1cd31347ddfa9132fa42ff7b330297dc9fd37383b8727fb48ea46b8e')):
        require(sha(methods[field].encode()) == methods[hash_field] == digest, 'Full original actual method '+field)
    require(methods['internal_solve_source_identity'] == core['internal_solve_source_identity'] and
            methods['core_instrumentation_sha256'] == core_desc['sha256'], 'Internal/public source distinction retained')
    seed = files.json('selected-seed-binding.json')
    subset(seed, dict(schema='native-current576-actual59-selected-seed-binding-v1', spec_sha256=outer['spec_sha256'],
        source_sha256=LAUNCHER_SHA,hook_sha256=HOOK_SHA,actual_selected_state_sha256=PARENT_STATE,
        full_height_float64le_sha256=UNCHANGED['physical-height'],nodes=577,shape_dimension=224,
        no_cut_or_far_projection=True,first_initial_assignment_only=True,predicted=True), 'Actual selected complete first state')
    require(seed['parent_selected59'] == spec['parent_selected59'], 'Exact selected provenance in seed')
    for key in ('original_live_identity','actual_method_identity'): files.check(seed[key])
    for item in outer.get('small_output_files',[]): files.check(item)
    metadata = dict(schema='current576-complete-loop-source-byte-audit-v1', source_files=source_files,
        original_specification=outer['specification'], parent_receipts=spec['parent_selected59'],
        parent_payloads_not_redownloaded_by_this_reader=True,
        original_core_and_actual_method_sources_verified=True,
        original_max_iterations=outer['original_max_iterations'],original_tolerance=outer['original_tolerance'],
        original_selected_noJ_norm=seed['original_selected_noJ_norm'], original_eta=outer['eta_binary64'])
    return spec,live,metadata


def audit_iterations(U, native, out, outer, spec, live):
    if 'current_correction_summary' not in outer:
        return [], [], dict(bridge_summary_present=False, complete_current_iterations_claimed=False)
    bridge = descriptor_json(native,outer['current_correction_summary'])
    subset(bridge, dict(schema='native-current576-damped-correction-bridge-summary-v1',source_sha256=LAUNCHER_SHA,
        hook_sha256=HOOK_SHA,spec_sha256=outer['spec_sha256'],native_call=1,
        current_direction_source_sha256=PRODUCER_SHA,current_system_source_sha256=SYSTEM_SHA,
        no_cached_actual28_or_other_baseline=True,current_withJ_only=True,no_cut_or_far_direction_projection=True,
        original_full_native_loop_and_final_endpoint_J_audit_retained=True), 'Original complete bridge summary')
    require(bridge['parent_selected59'] == spec['parent_selected59'] and
            bridge['snapshots_completed'] == outer['fresh_withJ_snapshots'] and
            bridge['directions_returned'] == outer['current_R273_directions_returned'], 'Top/bridge complete correction counts')
    records = bridge['iterations']; require(len(records) <= outer['original_max_iterations'], 'Original iteration budget not enlarged')
    dirs = sorted(p.name for p in native.root.iterdir() if p.is_dir() and re.fullmatch(r'iteration-[0-9]{3}',p.name))
    require(dirs == [r['iteration_directory'] for r in records], 'Every actual correction directory represented')
    jsonl = []
    path = native.root/'current-corrections.jsonl'
    if path.is_file():
        native.info(path.name)
        with path.open('rb') as stream:
            for line in stream:
                if line.strip(): jsonl.append(json.loads(line))
    require(jsonl == records, 'Full retained correction journal exactly matches final bridge records')
    summaries=[]; errors=[]; snapshots=returned=0
    for i,record in enumerate(records):
        name='iteration-'+str(i).zfill(3)
        subset(record,dict(native_call=1,nonlinear_iteration=i,snapshot_sequence=i,iteration_directory=name), 'Actual correction order')
        if record['linear_direction_returned']: returned += 1
        directory=native.root/name; iteration_files=U.Files(directory); qr_files=None; snapshot=None
        report=dict(schema='current576-iteration-reader-status-v1',iteration=i,directory=name,
            producer_record=record, byte_audit_passed=False, complete_qr_scope_verified=False)
        try:
            if record['snapshot_completed']:
                snapshots += 1
                native.check(record['snapshot'])
                snapshot=SnapshotBytes(U,directory/'snapshot',record,spec,live,outer['spec_sha256'])
                report['snapshot']=snapshot.record
                launch=iteration_files.json('qr-launch.json')
                subset(launch,dict(schema='current-native576-synchronous-QR-launch-v1',native_call=1,
                    nonlinear_iteration=i,snapshot_sequence=i,shell=False,source_sha256=PRODUCER_SHA,
                    system_source_sha256=SYSTEM_SHA,original_worker_stdout_protocol_not_used_by_child=True,
                    original_evaluate_already_returned=True,snapshot_result=snapshot.result_receipt), 'Actual per-iteration child invocation')
                require(launch['command'][1].endswith('/'+PRODUCER) and
                        launch['command'][launch['command'].index('--snapshot-result-sha256')+1] == snapshot.result_receipt['sha256'],
                        'Child argv binds the actual current snapshot')
                exit_record=iteration_files.json('qr-exit.json')
                require(exit_record == record['qr_exit'],'Actual child exit and bridge record')
                for key in ('stdout','stderr'): iteration_files.check(exit_record[key])
                result_file=directory/'qr/result.json.gz'
                if result_file.is_file():
                    qr_files=U.Files(directory/'qr'); result=qr_files.json('result.json.gz')
                    provisional=dict(schema='current576-original-child-scalars-v1',
                        result=qr_files.info('result.json.gz'),original_status=scalar_view(result),
                        original_factor_summary=result.get('factor_summary'),original_model=result.get('formed_model_diagnostic'),
                        original_exact=result.get('original_exact_readback'),byte_audit_not_yet_complete=True)
                    write(out,name+'/original-readout.json',provisional)
                    if result.get('diagnostic_completed') is True:
                        short,full,binding=audit_complete_qr(U,qr_files,result,snapshot,record,spec)
                        full_receipt=write(out,name+'/large-arrays/complete-byte-detail.json.gz',full,compressed=True)
                        short['complete_byte_detail']=full_receipt
                        report['audit']=write(out,name+'/byte-summary.json',short)
                        report['complete_qr_scope_verified']=True
                    else:
                        partial=audit_partial_qr(U,qr_files,result)
                        report['partial_child_detail']=write(out,name+'/large-arrays/partial-byte-detail.json.gz',partial,compressed=True)
                    if record['linear_direction_returned']:
                        require(result.get('diagnostic_completed') is True and exit_record['status']==0 and exit_record['error'] is None,
                                'Returned current direction really completed its own child')
                        direction=iteration_files.json('returned-correction.json')
                        require(direction == record['direction'],'Full returned-correction journal identity')
                        subset(direction,dict(schema='current-native576-returned-correction-v1',native_call=1,
                            nonlinear_iteration=i,snapshot_sequence=i,current_state_sha256=snapshot.result['current_state_sha256'],
                            snapshot_result=snapshot.result_receipt,new_matrix_identity_sha256=result['new_matrix_identity_sha256'],
                            no_cut_or_far_projection=True,chartCondition_not_computed=True,returned_maxChartCondition=None,
                            no_extra_L2_or_exact_defect_acceptance_gate=True), 'Actual native direction handoff')
                        for a,b in (('result',None),('input_binding','input_binding'),('direction_checkpoint','native_direction_checkpoint'),
                                    ('array_manifest','array_manifest'),('native_delta','native_delta')):
                            expected=plain_receipt(qr_files,'result.json.gz') if b is None else result[b]
                            require(direction[a] == expected,'Returned whole child payload '+a)
                else:
                    require(not record['linear_direction_returned'],'No returned direction may lack its full result')
                    report['partial_child_without_result']=True
            else:
                require(not record['linear_direction_returned'],'A direction cannot precede the full snapshot')
                report['partial_snapshot_not_claimed_complete']=True
            report['byte_audit_passed']=True
        except Exception as error:
            report['actual_byte_audit_error']=repr(error);report['traceback']=traceback.format_exc()
            errors.append(dict(iteration=i,error=repr(error)))
        finally:
            if snapshot is not None: merge_files(iteration_files,snapshot.files,'snapshot')
            if qr_files is not None: merge_files(iteration_files,qr_files,'qr')
            try:
                remaining=iteration_files.complete_inventory()
                report['complete_existing_files']=len(remaining)
                write(out,name+'/large-arrays/existing-file-inventory.json.gz',remaining,compressed=True)
            except Exception as error:
                report['inventory_error']=repr(error); report['byte_audit_passed']=False
                errors.append(dict(iteration=i,inventory_error=repr(error)))
            merge_files(native,iteration_files,name)
            report_receipt=write(out,name+'/reader-status.json',report)
            summaries.append(dict(iteration=i,status=report_receipt,passed=report['byte_audit_passed'],
                snapshot_completed=record['snapshot_completed'],linear_direction_returned=record['linear_direction_returned'],
                complete_qr_scope_verified=report['complete_qr_scope_verified'],audit=report.get('audit')))
            print(json.dumps(dict(event='current576_iteration_byte_readback',iteration=i,
                passed=report['byte_audit_passed'],complete_qr_scope=report['complete_qr_scope_verified'])),flush=True)
    require(snapshots == bridge['snapshots_completed'] and returned == bridge['directions_returned'],
            'All completed original snapshots/directions accounted for')
    return summaries,errors,dict(original_bridge_summary=outer['current_correction_summary'],
        snapshot_count=snapshots,direction_count=returned,actual_bridge_failure=bridge['actual_bridge_failure'],
        original_elapsed_seconds=bridge['elapsed_seconds'])


def run_reader(args,U,root,transport,transport_name):
    started=time.monotonic();whole=U.Files(root);path=root/NATIVE_DIRECTORY
    receipt_copy=write(args.out,'large-arrays/complete-original-transport-receipt.json.gz',transport,compressed=True)
    request_path=root/'current576-native-request-identity.json'
    if request_path.is_file():
        request=whole.json(request_path.name)
        subset(request,dict(repository=REPOSITORY,lane='current576native',source_commit=args.source_commit,
            current_run=str(args.run_id)),'Original Actions request source')
    else:
        request=None
    source_files=[]
    for name,digest in SOURCE_PINS.items():
        current=HERE/name;require(file_sha(current)==digest,'Frozen source-only consumer dependency '+name)
        source_files.append(dict(file=name,bytes=current.stat().st_size,sha256=digest))
    result=dict(schema=SCHEMA,original_run=args.run_id,original_head_commit=args.source_commit,
        original_artifact=dict(id=args.artifact_id,name=args.artifact_name,bytes=args.expected_size,sha256=args.expected_sha256),
        transport_receipt=receipt_copy,reader_source_sha256=file_sha(__file__),source_files=source_files,
        native_result_present=False,passed=False,mathematical_computation_performed=False,
        not_a_nonlinear_acceptance_gate=True,scientific_values_copied_not_recomputed=True,
        original_request_identity_present=request is not None)
    errors=[];iterations=[]
    if path.is_dir():
        native=U.Files(path)
        if (path/'result.json').is_file():
            outer=native.json('result.json'); result['native_result_present']=True
            # Publish the saved outcome before any optional deeper audit can fail.
            original_readout=dict(schema='actual61-original-native-outcome-readback-v1',
                original_result=native.info('result.json'),original_status=scalar_view(outer),
                original_audit=outer.get('audit'),original_jet_scalars=outer.get('jets_summary'),
                original_bridge_failure=outer.get('bridge_failure'),original_response=outer.get('original_response'),
                original_result_full_hash_bound_to_pinned_artifact=True,complete_byte_audit_not_yet_finished=True)
            result['original_outcome']=write(args.out,'original-native-outcome.json',original_readout)
            try:
                subset(outer,dict(schema='native-current576-damped-solve-result-v1',source_sha256=LAUNCHER_SHA,
                    hook_sha256=HOOK_SHA,current_direction_source_sha256=PRODUCER_SHA,current_system_source_sha256=SYSTEM_SHA,
                    factor_engine_source_sha256=FACTOR_SHA,model_scope=MODEL_SCOPE,
                    requested_full_DN_Jacobian=True,requested_full_finite_audit=True,
                    complete_original_native_loop_requested=True,only_nonlinear_correction_call_replaced=True,
                    cached28_or_other_old_baseline_loaded=False,original_final_endpoint_J_and_audit_retained=True),
                    'Actual complete native producer identity')
                result['original_native_accepted']=outer['native_accepted']
                result['original_status']=scalar_view(outer)
                # Startup failures have no live identity, so retain them without
                # inventing any completed snapshot or demanding mathematical success.
                if 'current_correction_summary' in outer:
                    spec,live,metadata=current_loop_metadata(U,native,outer,args.out)
                    result['source_metadata']=write(args.out,'source-and-loop-byte-identity.json',metadata)
                    iterations,iteration_errors,bridge=audit_iterations(U,native,args.out,outer,spec,live)
                    errors.extend(iteration_errors);result['bridge']=bridge
                else:
                    for item in outer.get('small_output_files',[]): native.check(item)
                    result['no_completed_bridge_scope_claimed']=True
            except Exception as error:
                errors.append(dict(scope='native metadata',error=repr(error),traceback=traceback.format_exc()))
        else:
            result['producer_did_not_write_final_result']=True
            result['no_complete_native_scope_claimed']=True
        merge_files(whole,native,NATIVE_DIRECTORY)
    else:
        result['producer_directory_not_created']=True
        result['no_complete_native_scope_claimed']=True
    # Inventory everything present, including interrupted metadata, worker logs,
    # final response bytes and rule-sync receipts. Payloads already checked above
    # reuse cached file hashes after immutable size/mtime checks.
    try:
        inventory=whole.complete_inventory()
        result['complete_existing_artifact_file_count']=len(inventory)
        result['complete_file_inventory']=write(args.out,'large-arrays/complete-existing-file-inventory.json.gz',inventory,compressed=True)
    except Exception as error:
        errors.append(dict(scope='full existing artifact inventory',error=repr(error),traceback=traceback.format_exc()))
    rules=root/'rule-sync/runner-result.json'
    if rules.is_file():
        result['original_rule_runner_result']=write(args.out,'original-rule-runner-result.json',read(rules))
    result['iterations']=iterations;result['actual_audit_errors']=errors;result['passed']=not errors
    result['complete_scientific_success_inferred_from_byte_audit']=False
    result['elapsed_readback_seconds']=time.monotonic()-started
    result['scope_limits']=[
        'No native producer, NumPy or SciPy module was imported; no scientific operation was repeated.',
        'All scientific values and maximum choices are the saved Actions values. Exact rows were not summed, divided or re-maximized.',
        'Every complete snapshot and returned QR direction is bound to its own current iteration; no actual28 or1372 baseline is substituted.',
        'Formed V/rho metadata hashes are retained; unexported formed coefficient arrays are not recreated.',
        'Original selected59 receipts and the first current-state hash are bound. The separate original parent artifact is not fetched again.',
        'Actual nonlinear state updates, final sensitivity, final audit mathematics and native acceptance are not independently recomputed.',
        'A reported producer failure or partial output is preserved. A byte discrepancy does not erase original scalar observations.']
    write(args.out,'current576-readback-summary.json',result)
    return 0 if result['passed'] else 2


def main():
    require(os.environ.get('GITHUB_ACTIONS')=='true' and os.environ.get('GITHUB_REPOSITORY')==REPOSITORY,
            'This original-artifact reader runs only in the named public Actions repository')
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run-id',type=int,required=True)
    p.add_argument('--artifact-id',type=int,required=True)
    p.add_argument('--artifact-name',required=True)
    p.add_argument('--expected-size',type=int,required=True)
    p.add_argument('--expected-sha256',required=True)
    p.add_argument('--source-commit',required=True)
    p.add_argument('--download-out',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    require(a.run_id==ORIGINAL_RUN and a.source_commit==ORIGINAL_COMMIT,'Only the explicitly reviewed actual61 run/source')
    require(a.artifact_id>0 and a.expected_size>0 and re.fullmatch(r'[0-9a-f]{64}',a.expected_sha256),
            'Complete actual artifact id/size/SHA required')
    require(re.fullmatch('visible-mainline-current576native-'+str(ORIGINAL_RUN)+r'-[1-9][0-9]*',a.artifact_name),
            'Actual current576 artifact name and attempt')
    a.download_out=a.download_out.resolve();a.out=a.out.resolve()
    require(not a.out.exists() and not a.out.is_relative_to(a.download_out) and not a.download_out.is_relative_to(a.out),
            'Independent new original payload and readback output directories')
    a.out.mkdir(parents=True)
    try:
        U=load_byte_module(UTILITY_NAME,UTILITY_SHA,'_current576_byte_utilities')
        root,transport,name=fetch_original(a)
        return run_reader(a,U,root,transport,name)
    except Exception as error:
        write(a.out,'readback-failure.json',dict(schema=SCHEMA,passed=False,error=repr(error),
            traceback=traceback.format_exc(),source_sha256=file_sha(__file__),
            original_run=a.run_id,original_source_commit=a.source_commit,
            scientific_computation_performed=False,partial_readouts_not_removed=True))
        print(json.dumps(dict(event='current576_original_readback_failed',error=repr(error))),flush=True)
        return 2


if __name__=='__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Read-only byte/structure audit of the frozen R273 output packet.

This is not a mathematical validator or a native acceptance gate.  It uses
only the standard library, hashes, gzip CRC, JSON equality, indexing and
IEEE word classification.  It never imports a producer, forms sigma*z,
evaluates a row, compares rational magnitudes, computes a norm or runs QR.
All scientific numbers in the audit are copied from the Actions reports.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import time


PRODUCER = 'exact_20261114_native_damped_chain_qr.py'
PRODUCER_SHA = '9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33'
SYSTEM = 'exact_20261114_rawcell0_direct_ld_system.py'
SYSTEM_SHA = 'b64b6ed8b387834b5cc9332675127a1dcbb15a317c3400f5b768d18cdbdf5a8e'
KERNEL = 'exact_20261114_native_allrows_dyadic_residual.py'
KERNEL_SHA = '0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
EXPECTED_MATRIX = '76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999'
EXPECTED_DIRECT = 'e60da64312819a87388cfa96c209fc9188dca02c0ab055cbcc934f3507888ac6'
MODEL_SCOPE = 'R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates'
MASK_ABS = (1 << 63)-1
HEX_COEFFICIENT = re.compile(r'-?0x[0-9a-f]+\Z')


def require(condition, label):
    if not condition:
        raise ValueError('Saved-byte/structure discrepancy: '+label)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical_sha(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':'),
                          allow_nan=False).encode())


def product_shape(shape):
    count = 1
    for dimension in shape:
        require(type(dimension) is int and dimension >= 0, 'nonnegative integer array dimension')
        count *= dimension
    return count


def stream_sha(path):
    h = hashlib.sha256()
    size = 0
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1 << 20), b''):
            h.update(block)
            size += len(block)
    return size, h.hexdigest()


def read_json_file(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def number_word(record, raw, label):
    require(len(raw) == 8 and record['float64le_hex'] == raw.hex(), label+' word')
    if record.get('value') is not None:
        require(struct.pack('<d', record['value']) == raw, label+' printed binary64 recovery')


def words(raw):
    require(len(raw) % 8 == 0, 'complete IEEE words')
    return struct.iter_unpack('<Q', raw)


def checkpoint_bytes(cp, expected_rows, width, label):
    require(len(cp['rows']) == expected_rows, label+' row count')
    out = bytearray()
    for node, item in enumerate(cp['rows']):
        require(item['node'] == node and len(item['state']) == width, label+' node/width')
        raw = bytearray(struct.pack('<'+str(width)+'d', *item['state']))
        negative = item['negative_zero_columns']
        require(negative == sorted(set(negative)), label+' unique ordered negative-zero columns')
        # The explicit zero-sign list is part of the checkpoint contract;
        # no nonzero word is replaced and no number is inferred from a norm.
        for column in negative:
            require(0 <= column < width, label+' zero column range')
            w = int.from_bytes(raw[8*column:8*(column+1)], 'little')
            require((w & MASK_ABS) == 0, label+' zero-sign annotation is a zero')
            raw[8*column:8*(column+1)] = (1 << 63).to_bytes(8, 'little')
        actual = [j for j,(w,) in enumerate(words(raw)) if w == (1 << 63)]
        require(actual == negative, label+' complete negative-zero annotations')
        out.extend(raw)
    require(sha(out) == cp['delta_float64le_sha256'], label+' full reconstructed byte SHA')
    return bytes(out)


class Files:
    def __init__(self, directory):
        self.root = Path(directory).resolve()
        require(self.root.is_dir(), 'existing input directory')
        self.records = {}
        self.raw_statistics = {}

    def path(self, relative):
        name = PurePosixPath(relative)
        require(not name.is_absolute() and '..' not in name.parts and name.parts,
                'relative artifact path')
        p = self.root.joinpath(*name.parts)
        require(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(self.root),
                'regular in-tree artifact: '+relative)
        return p

    def info(self, relative):
        p = self.path(relative)
        current = (p.stat().st_size, p.stat().st_mtime_ns)
        cached = self.records.get(relative)
        if cached:
            require(tuple(cached['_stat']) == current, 'immutable artifact during audit: '+relative)
            return {k:v for k,v in cached.items() if not k.startswith('_')}
        size, digest = stream_sha(p)
        entry = dict(file=relative, bytes=size, sha256=digest, _stat=current)
        self.records[relative] = entry
        return {k:v for k,v in entry.items() if not k.startswith('_')}

    def check(self, descriptor):
        observed = self.info(descriptor['file'])
        for key in ('file', 'bytes', 'sha256'):
            require(observed[key] == descriptor[key], descriptor['file']+' '+key)
        return observed

    def json(self, descriptor):
        if isinstance(descriptor, str):
            name = descriptor
            self.info(name)
        else:
            self.check(descriptor)
            name = descriptor['file']
        raw = self.path(name).read_bytes()
        if raw[:2] == b'\x1f\x8b':
            raw = gzip.decompress(raw)
            self.records[name].update(decompressed_bytes=len(raw),
                decompressed_sha256=sha(raw), gzip_crc_complete=True)
        return json.loads(raw)

    def raw(self, descriptor):
        self.check(descriptor)
        return self.path(descriptor['file']).read_bytes()

    def classify_f64(self, descriptor):
        name = descriptor['file']
        self.check(descriptor)
        require(descriptor['dtype'] == '<f8' and descriptor['order'] == 'C', name+' dtype/order')
        count = product_shape(descriptor['shape'])
        require(count*8 == descriptor['bytes'], name+' complete shape bytes')
        if name not in self.raw_statistics:
            stats = dict(finite=0, nan=0, positive_infinity=0, negative_infinity=0, negative_zero=0)
            with self.path(name).open('rb') as f:
                for raw in iter(lambda:f.read(1 << 20), b''):
                    for (w,) in words(raw):
                        exponent = (w >> 52) & 2047
                        if exponent != 2047:
                            stats['finite'] += 1
                        elif w & ((1 << 52)-1):
                            stats['nan'] += 1
                        elif w >> 63:
                            stats['negative_infinity'] += 1
                        else:
                            stats['positive_infinity'] += 1
                        if w == (1 << 63):
                            stats['negative_zero'] += 1
            self.raw_statistics[name] = stats
        stats = self.raw_statistics[name]
        for key,value in stats.items():
            require(descriptor[key] == value, name+' saved IEEE classification '+key)
        return dict(self.info(name), shape=descriptor['shape'], dtype='<f8', order='C',
                    raw_IEEE_classification=stats)

    def complete_inventory(self):
        for path in sorted(self.root.rglob('*')):
            require(not path.is_symlink(), 'no artifact symlink')
            if not path.is_file():
                continue
            relative = path.relative_to(self.root).as_posix()
            self.info(relative)
            if path.suffix == '.gz' and not self.records[relative].get('gzip_crc_complete'):
                h = hashlib.sha256()
                size = 0
                with gzip.open(path, 'rb') as f:
                    for block in iter(lambda:f.read(1 << 20), b''):
                        h.update(block)
                        size += len(block)
                self.records[relative].update(decompressed_bytes=size,
                    decompressed_sha256=h.hexdigest(), gzip_crc_complete=True)
        return [self.info(name) for name in sorted(self.records)]


def check_max_record(record, kind, node, row_count, first, sigma, matrix, cells):
    row = record['row']
    require(type(row) is int and 0 <= row < row_count, 'saved maximum row index')
    require(record['kind'] == kind and record['node'] == node, 'saved maximum block location')
    require(record['global_equation_row'] == first+row, 'saved maximum global row index')
    require(record['new_matrix_identity_sha256'] == matrix, 'saved maximum target identity')
    require(record['original_sigma_float64le_hex'] == sigma[node*8:(node+1)*8].hex(),
            'saved maximum sigma raw word')
    if kind == 'stage':
        require(record['source_stage'] == cells[node], 'saved maximum dynamic stage mapping')
    for key in ('exact_signed_scaled_residual', 'exact_absolute_scaled_residual'):
        f = record[key]
        require(isinstance(f['numerator'], str) and re.fullmatch(r'-?[0-9]+', f['numerator']) is not None,
                'saved rational numerator syntax')
        require(isinstance(f['denominator'], str) and re.fullmatch(r'[0-9]+', f['denominator']) is not None
                and f['denominator'].lstrip('0') != '', 'saved rational denominator syntax')
        require(f['display_never_used_for_comparison'] is True, 'saved fraction display scope')
    # No division, rational reduction, magnitude comparison or norm here.


def audit_ledger(files, descriptor, detail, binding, delta_sha, sigma, M, K, D):
    files.check(descriptor)
    require(descriptor['dtype'] == 'exact-dyadic-jsonl-gzip' and
            descriptor['shape'] == [(D+1)*K], 'complete integer ledger shape')
    maxima = detail['typed_block_maxima']
    require(len(maxima) == D+2, 'one maximum record per cut/stage/far block')
    digest = hashlib.sha256()
    size = rows_seen = blocks_seen = 0
    chosen = detail['exact_global_original_sigma_norm']
    chosen_matches = 0
    compact_rows_hash = hashlib.sha256()
    with gzip.open(files.path(descriptor['file']), 'rb') as f:
        for index,line in enumerate(f):
            digest.update(line)
            size += len(line)
            require(index < D+2, 'no extra exact row block')
            row = json.loads(line)
            kind = 'cut' if index == 0 else 'far' if index == D+1 else 'stage'
            node = 0 if kind == 'cut' else D if kind == 'far' else index-1
            count = K if kind == 'stage' else M
            first = 0 if kind == 'cut' else M+D*K if kind == 'far' else M+node*K
            require(row['kind'] == kind and row['node'] == node and
                    row['first_global_equation_row'] == first, 'complete cut/stage/far ledger order')
            require(first == rows_seen, 'contiguous original equation rows')
            values = row['all_exact_unscaled_rows']
            require(len(values) == count, 'all exact rows present in block')
            for coefficient in values:
                require(isinstance(coefficient, list) and len(coefficient) == 2 and
                        isinstance(coefficient[0], str) and HEX_COEFFICIENT.fullmatch(coefficient[0]) and
                        type(coefficient[1]) is int, 'compact dyadic row syntax')
            compact_rows_hash.update(json.dumps(values, separators=(',', ':')).encode())
            require(row['direction_float64le_sha256'] == delta_sha and
                    row['new_matrix_identity_sha256'] == binding['new_matrix_identity_sha256'],
                    'ledger direction/target identity')
            expected_j = binding['complete_block_manifest'][node]['raw_sha256'] if kind == 'stage' else None
            require(row['original_J_stage_sha256'] == expected_j, 'ledger J block identity')
            maximum = row['exact_original_sigma_maximum']
            require(maximum == maxima[index], 'ledger maximum copied to full detail exactly')
            check_max_record(maximum, kind, node, count, first, sigma,
                             binding['new_matrix_identity_sha256'], binding['cells'])
            require(values[maximum['row']] == maximum['exact_unscaled_dyadic'],
                    'saved maximum exact row occurs verbatim in ledger')
            if maximum == chosen:
                chosen_matches += 1
            rows_seen += count
            blocks_seen += 1
    require(rows_seen == detail['exact_rows'] == (D+1)*K and blocks_seen == D+2,
            'complete original exact ledger totals')
    require(chosen_matches == 1, 'Actions-selected global maximum is one exact saved block record')
    files.records[descriptor['file']].update(decompressed_bytes=size,
        decompressed_sha256=digest.hexdigest(), gzip_crc_complete=True)
    return dict(rows=rows_seen, blocks=blocks_seen, uncompressed_bytes=size,
        uncompressed_sha256=digest.hexdigest(), ordered_compact_row_lists_sha256=compact_rows_hash.hexdigest(),
        every_saved_row_read=True, complete_original_row_order=True,
        all_block_J_and_direction_and_sigma_identities_bound=True,
        all_per_block_maximum_records_equal_the_saved_detail=True,
        reported_global_maximum_located_verbatim=True,
        maximum_or_any_dyadic_rational_value_recomputed=False)


def compare_reference54(directory, binding, original_arrays):
    if directory is None:
        return dict(performed=False, reason='No prior54 directory supplied; current complete input binding retained')
    ref = Files(directory)
    old = ref.json('result.json.gz')
    require(ref.info('result.json.gz')['sha256'] ==
        'e1ac6c83434ac3b269663e930b1370a38f280b2d31c5e720955b5ed0aed7e105', 'actual54 result pin')
    prior = ref.json(old['input_binding'])
    require(prior == binding, 'complete mathematical/input metadata unchanged from actual54')
    for name,desc in original_arrays.items():
        before = old['bound_new_system_arrays'][name]
        ref.check(before)
        require(desc['sha256'] == before['sha256'] and desc['shape'] == before['shape'] and
                desc['bytes'] == before['bytes'], 'same original non-J array as actual54: '+name)
    return dict(performed=True, actual54_result=ref.info('result.json.gz'),
        entire_input_binding_equal=True, all_nine_original_nonJ_array_raw_hashes_equal=True,
        files=list(ref.records.values()))


def optional_J_witness(directory, binding, witness, K):
    if witness['kind'] != 'stage':
        return dict(performed=False, reason='Worst row is a boundary and has no J block')
    node = witness['node']
    block = binding['complete_block_manifest'][node]
    if directory is None or block['original_stage'] >= 72:
        return dict(performed=False, reason='No direct-map payload applicable/supplied; J hash still bound to complete manifest')
    ref = Files(directory)
    result = ref.json(binding['actual_direct_result'])
    require(result['completed'] and result['capture_completed'], 'actual54 complete direct-map capture')
    manifest = ref.json(result['array_manifest'])
    report = ref.json(result['stage_reports'][block['original_stage']])
    array_name = report['arrays']['shape_jacobians']
    entry = next(x for x in manifest['arrays'] if x['name'] == array_name)
    step = block['step_index']
    matches = [x for x in entry['chunks'] if x['row_start'] <= step < x['row_stop']]
    require(len(matches) == 1, 'one saved direct-J chunk contains the worst block')
    desc = matches[0]
    raw = ref.raw(desc)
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    require(sha(raw) == desc['raw_sha256'], 'saved direct chunk raw SHA')
    size = K*K*8
    offset = (step-desc['row_start'])*size
    full = raw[offset:offset+size]
    require(len(full) == size and sha(full) == block['raw_sha256'] == witness['complete_stage_J_raw_sha256'],
            'actual54 saved worst complete J block raw bytes')
    lo = witness['row']*K*8
    require(full[lo:lo+K*8].hex() == witness['full_J_row_float64le_hex'], 'worst J row actual source words')
    return dict(performed=True, source_chunk=ref.info(desc['file']), source_block_sha256=sha(full),
                actual_source_J_row_words_equal=True, new_RHS_J_or_matrix_action=False)


def audit(args):
    started = time.monotonic()
    files = Files(args.directory)
    result = files.json('result.json.gz')
    require(files.info('result.json.gz')['sha256'] == args.expected_result_sha256, 'explicit actual result pin')
    require(result['schema'] == 'complete-native-direct-LD-J1372-damped-square-root-direction-v1',
            'frozen R273 producer schema')
    for key,expected in (('source_sha256',PRODUCER_SHA), ('system_source_sha256',SYSTEM_SHA),
                         ('kernel_source_sha256',KERNEL_SHA), ('new_matrix_identity_sha256',EXPECTED_MATRIX),
                         ('actual_direct_result_sha256',EXPECTED_DIRECT)):
        require(result[key] == expected, 'producer '+key)
    require(result['eta_cli_text'] == args.expected_eta_text, 'explicit eta CLI text')
    require(result['native_accepted'] is False and result['task_completed'] is False,
            'direction result does not claim nonlinear acceptance')
    for key in ('original_native_calls','new_RHS_calls','new_J_calls','new_ODE_steps','nonlinear_trials'):
        require(result[key] == 0, 'direction producer zero '+key)
    require(result['diagnostic_completed'] and result['linear_direction_computed'],
            'complete actual direction packet required for this complete audit')
    summary = files.json('summary.json')
    files.check(summary['full_result'])
    for key in set(summary) & set(result) - {'schema'}:
        require(summary[key] == result[key], 'small/full report copied field '+key)
    binding = files.json(result['input_binding'])
    require(binding['new_matrix_identity_sha256'] == EXPECTED_MATRIX, 'full input target identity')
    D,K,M = binding['new_depth'],binding['shape_dimension'],binding['modes']
    require((D,K,M) == (1372,224,112), 'actual54 full target dimensions')
    old_to_new = binding['old_to_new']
    require(len(old_to_new) == 577 and old_to_new == sorted(set(old_to_new)) and
            old_to_new[0] == 0 and old_to_new[-1] == D, 'complete old-to-new node map')
    manifest = files.json(result['array_manifest'])
    require(manifest['schema'] == 'complete-native-damped-chain-direction-arrays-v1' and
            manifest['source_sha256'] == PRODUCER_SHA and manifest['new_matrix_identity_sha256'] == EXPECTED_MATRIX,
            'complete array manifest identity')
    entries = manifest['arrays']
    by_name = {d['name']:d for d in entries}
    by_file = {d['file']:d for d in entries}
    require(len(by_name) == len(by_file) == len(entries), 'unique array names and paths')
    raw_audits = []
    for index,desc in enumerate(entries):
        if desc['dtype'] == '<f8':
            raw_audits.append(files.classify_f64(desc))
        else:
            require(desc['dtype'] == 'exact-dyadic-jsonl-gzip', 'known non-f64 exact ledger type')
            files.check(desc)
        if (index+1) % 128 == 0:
            print(json.dumps(dict(event='damped_chain_byte_audit', arrays_checked=index+1,
                                  total_arrays=len(entries))),flush=True)
    def member(desc):
        require(desc == by_file[desc['file']], 'full descriptor alias equals manifest: '+desc['file'])
        return files.raw(desc)
    original = result['original_arrays']
    require(set(original) == {'base-states','stage-residuals','stage-out','original-scales',
            'cut-residual','end-residual','original-far-graph','physical-height','cut-target'},
            'all nine original arrays')
    original_raw = {name:member(desc) for name,desc in original.items()}
    for name,desc in original.items():
        require(desc['sha256'] == binding['raw_array_sha256'][name], 'bound original array raw hash '+name)
    prior = compare_reference54(args.reference54_directory,binding,original)
    factor = files.json(result['factor_report'])
    index = files.json(result['factor_index'])
    inventory = files.json(result['formed_stage_inventory'])
    require(factor['complete'] and index['complete'], 'complete factorization records')
    require(factor['source_sha256'] == index['source_sha256'] == inventory['source_sha256'] == PRODUCER_SHA,
            'factor/formed source identity')
    require(factor['input_matrix_identity_sha256'] == index['new_matrix_identity_sha256'] ==
            inventory['new_matrix_identity_sha256'] == EXPECTED_MATRIX, 'factor/formed target identity')
    for key,value in result['factor_summary'].items():
        require(factor[key] == value, 'factor summary copy '+key)
    for key,value in dict(rows=(D+1)*K, columns=(D+1)*K, augmented_rows=2*(D+1)*K,
        stage_count=D,node_count=D+1,block_width=K,node_penalty_blocks=D+1,pure_constant_rows=(D+1)*K,
        qr_calls=2*D+1,formation_calls=2*D).items():
        require(factor[key] == value, 'complete recorded dimension/count '+key)
    require(factor['eta_binary64'] == result['eta_binary64'] and factor['model_scope'] == MODEL_SCOPE,
            'same eta and model coordinates')
    factors = index['factors']
    require(len(factors) == D+1, 'all node factors')
    total_factor_bytes = constant_rows = lower_zero_words = 0
    factor_records = []
    for n,item in enumerate(factors):
        final = n == D
        require(item['node'] == n and item['final'] == final and item['R_columns'] == [0,K], 'factor node/layout')
        require(item['S_columns'] == (None if final else [K,2*K]) and
                item['affine_column'] == (K if final else 2*K), 'factor retained blocks')
        cols = K+1 if final else 2*K+1
        require(item['factor']['shape'] == [K,cols], 'complete R/S/affine shape')
        count = K+M if final else M if n == 0 else K
        require(item['constant']['shape'] == [count], 'complete pure-constant row shape')
        raw = member(item['factor'])
        member(item['constant'])
        for row in range(K):
            lower = raw[row*cols*8:(row*cols+row)*8]
            require(not any(lower), 'retained R mathematical lower triangle is literal zero')
            lower_zero_words += row
        total_factor_bytes += item['factor']['bytes']+item['constant']['bytes']
        constant_rows += count
        factor_records.append(dict(node=n, factor=item['factor']['file'],
            factor_sha256=item['factor']['sha256'], constant=item['constant']['file'],
            constant_sha256=item['constant']['sha256'], lower_R_zero_words_verified=K*(K-1)//2))
    require(total_factor_bytes == factor['actual_factor_and_constant_bytes'] ==
            factor['expected_factor_and_constant_bytes'], 'complete factor storage bytes')
    require(constant_rows == (D+1)*K, 'no omitted pure constant row')
    stages = inventory['stages']
    require(len(stages) == D, 'all formed coefficient inventory records')
    sigma = original_raw['original-scales']
    for n,item in enumerate(stages):
        require(item['stage'] == n and item['original_J_raw_sha256'] ==
            binding['complete_block_manifest'][n]['raw_sha256'], 'formed stage source J identity')
        number_word(item['original_sigma_current'],sigma[n*8:(n+1)*8],'formed current sigma')
        number_word(item['original_sigma_next'],sigma[(n+1)*8:(n+2)*8],'formed next sigma')
    model_hash = canonical_sha(dict(original_matrix=EXPECTED_MATRIX,
        sigma=original['original-scales']['sha256'],eta_bits=result['eta_binary64']['float64le_hex'],
        source_sha256=PRODUCER_SHA,precision=factor['working_precision'],
        stages=[{k:r[k] for k in ('stage','original_J_raw_sha256','formed_V_raw_sha256',
            'formed_rho_raw_sha256','combined_formed_bytes_sha256','original_sigma_current',
            'original_sigma_next')} for r in stages],
        cut=factor['formed-cut-rho']['array'],far=factor['formed-far-rho']['array']))
    require(model_hash == factor['formed_model_identity_sha256'] == inventory['formed_model_identity_sha256'] ==
            result['formed_model_diagnostic']['model_identity_sha256'], 'canonical formed-model identity')
    member(factor['formed-cut-rho']['array'])
    member(factor['formed-far-rho']['array'])
    solve = factor['solve']
    z = member(solve['scaled_z'])
    delta = member(solve['delta'])
    require(solve['delta'] == result['step_delta'] and solve['triangular_solves'] == D+1,
            'complete saved back substitution result')
    restricted = member(result['restricted_old_node_delta'])
    require(b''.join(delta[n*K*8:(n+1)*K*8] for n in old_to_new) == restricted,
            '577-node restriction is complete byte selection')
    underflow_count = 0
    for (zw,),(dw,) in zip(words(z),words(delta)):
        if (zw & MASK_ABS) != 0 and (dw & MASK_ABS) == 0:
            underflow_count += 1
    require(underflow_count == solve['nonzero_recovery_to_zero'], 'saved recovery-to-zero bit classification')
    for example in solve['recovery_underflow_examples']:
        n,j=example['node'],example['column']
        offset=(n*K+j)*8
        number_word(example['z'],z[offset:offset+8],'recorded recovery z operand')
        number_word(example['sigma'],sigma[n*8:(n+1)*8],'recorded recovery sigma operand')
        number_word(example['delta'],delta[offset:offset+8],'recorded recovery delta result')
    for restricted_flag,key,raw in ((False,'step_direction_checkpoint',delta),
                                   (True,'restricted_direction_checkpoint',restricted)):
        cp=files.json(result[key])
        schema=('complete-original-node-restriction-of-damped-chain-direction-v1' if restricted_flag
                else 'complete-native-damped-chain-direction-v1')
        require(cp['schema']==schema and cp['source_sha256']==PRODUCER_SHA and cp['input_binding']==binding,
                'checkpoint source/input identity')
        require(cp['eta_binary64']==result['eta_binary64'] and cp['model_scope']==MODEL_SCOPE and
                cp['old_to_new']==old_to_new and cp['restricted_to_original_nodes']==restricted_flag,
                'checkpoint model/restriction identity')
        require(cp['M']==M and cp['K']==K and cp['original_depth']==576 and cp['step_depth']==D and
                cp['depth']==(576 if restricted_flag else D), 'checkpoint dimensions')
        require(checkpoint_bytes(cp,577 if restricted_flag else D+1,K,key)==raw,
                'checkpoint matches every actual direction word')
    exact=result['original_exact_readback']
    detail=files.json(exact['full_report'])
    require(detail['source_sha256']==PRODUCER_SHA and detail['kernel_sha256']==KERNEL_SHA and
            detail['new_matrix_identity_sha256']==EXPECTED_MATRIX and
            detail['direction_float64le_sha256']==result['step_delta']['sha256'], 'exact readback source/target/direction')
    for key in ('exact_global_original_sigma_norm','exact_stored_base_sigma_norm','exact_rows',
                'completed_stages','all_exact_residual_rows','worst_witness','no_float_refinement_RHS_formed',
                'used_as_new_nonlinear_acceptance_gate'):
        require(detail[key]==exact[key], 'exact small/full copied field '+key)
    require(detail['completed_stages']==D and detail['exact_rows']==(D+1)*K and
            detail['original_product_positions']==D*K*K+M, 'complete exact row/product counts')
    ledger=audit_ledger(files,exact['all_exact_residual_rows'],detail,binding,
                       result['step_delta']['sha256'],sigma,M,K,D)
    witness=files.json(exact['worst_witness'])
    maximum=detail['exact_global_original_sigma_norm']
    require(witness['exact_original_sigma_maximum']==maximum and
            witness['complete_direction_float64le_sha256']==result['step_delta']['sha256'] and
            witness['new_matrix_identity_sha256']==EXPECTED_MATRIX, 'worst witness top-level binding')
    w=witness['operands'];n,j,kind=w['node'],w['row'],w['kind']
    require((n,j,kind)==(maximum['node'],maximum['row'],maximum['kind']), 'worst operand row location')
    require(w['explicit_node_sigma_float64le_hex']==sigma[n*8:(n+1)*8].hex(), 'worst sigma bits')
    require(w['complete_direction_float64le_sha256']==result['step_delta']['sha256'] and
            w['new_matrix_identity_sha256']==EXPECTED_MATRIX, 'worst operand target/direction')
    def word(array,index):return array[index*8:(index+1)*8].hex()
    if kind=='stage':
        require(w['full_next_delta_float64le_hex']==delta[(n+1)*K*8:(n+2)*K*8].hex() and
                w['current_delta_float64le_hex']==word(delta,n*K+j) and
                w['residual_float64le_hex']==word(original_raw['stage-residuals'],n*K+j),
                'all stage worst direction/residual operands')
        require(w['complete_stage_J_raw_sha256']==binding['complete_block_manifest'][n]['raw_sha256'] and
                w['source_stage']==binding['cells'][n] and
                len(bytes.fromhex(w['full_J_row_float64le_hex']))==K*8, 'worst complete J row identity')
    elif kind=='cut':
        require(w['delta_float64le_hex']==word(delta,j) and
                w['residual_float64le_hex']==word(original_raw['cut-residual'],j), 'worst cut words')
    elif kind=='far':
        require(w['delta_Q_float64le_hex']==word(delta,D*K+j) and
                w['delta_Pi_float64le_hex']==word(delta,D*K+M+j) and
                w['original_G_float64le_hex']==word(original_raw['original-far-graph'],j) and
                w['residual_float64le_hex']==word(original_raw['end-residual'],j), 'worst far words')
    else:
        raise ValueError('Unknown original worst row kind')
    j_witness=optional_J_witness(args.reference_direct_directory,binding,w,K)
    sources=[]
    if args.source_directory:
        for name,digest in ((PRODUCER,PRODUCER_SHA),(SYSTEM,SYSTEM_SHA),(KERNEL,KERNEL_SHA)):
            size,observed=stream_sha(Path(args.source_directory)/name)
            require(observed==digest,'current frozen source file '+name)
            sources.append(dict(file=name,bytes=size,sha256=observed))
    all_files=files.complete_inventory()
    evidence=dict(schema='R273-complete-output-byte-audit-detail-v1',
        producer_result=files.info('result.json.gz'),files=all_files,raw_arrays=raw_audits,
        factors=factor_records,original_reference54=prior,worst_J_source_byte_check=j_witness,
        source_files=sources,source_ledger_only_when_no_source_directory=not bool(args.source_directory))
    summary_out=dict(schema='R273-complete-output-byte-audit-summary-v1',
        classification='saved-byte and structural audit; all scientific values copied from original Actions',
        scientific_calculation_performed_locally=False,numerical_acceptance_gate=False,
        source_audit_sha256=stream_sha(__file__)[1],producer_result=files.info('result.json.gz'),
        producer_source_sha256=PRODUCER_SHA,new_matrix_identity_sha256=EXPECTED_MATRIX,
        formed_model_identity_sha256=model_hash,eta=result['eta_binary64'],
        all_array_descriptors_verified=len(entries),all_float64_arrays_verified=len(raw_audits),
        complete_file_inventory_count=len(all_files),complete_factor_nodes=D+1,
        complete_factor_and_constant_bytes=total_factor_bytes,complete_pure_constant_rows=constant_rows,
        all_R_lower_triangle_zero_words_checked=lower_zero_words,
        complete_scaled_z_and_original_delta_and_577restriction_verified=True,
        checkpoint_all_words_and_negative_zero_annotations_verified=True,
        actual_sigma_times_z_multiplication_not_recomputed=True,
        saved_recovery_underflow_count=solve['nonzero_recovery_to_zero'],
        original_exact_row_ledger=ledger,worst_operand_words_verified=True,
        worst_J_source_byte_check=j_witness,all_original_input_bytes_match_actual54=prior.get('performed',False),
        source_files=sources,
        copied_Actions_scientific_reports=dict(factor_summary=result['factor_summary'],
            solve=solve,formed_model_diagnostic=result['formed_model_diagnostic'],
            original_exact_readback=result['original_exact_readback']),
        limits=[
            'No QR, triangular solve, RHS, Jacobian, sigma*z, matrix action, norm or exact residual was computed here.',
            'The chosen maximum and per-block maxima are bound to their saved rows, not independently re-maximized.',
            'Formed V/rho arrays are not exported as payloads: their hashes and the canonical model ledger are checked; coefficients are not independently reformed.',
            'Model gradient/energy and factorization accuracy remain original Actions numerical readouts, not a byte-audit proof.',
            'No native trial or nonlinear acceptance is supplied by this audit.'],
        elapsed_byte_audit_seconds=time.monotonic()-started,passed=True)
    return summary_out,evidence


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory',type=Path,required=True)
    p.add_argument('--expected-result-sha256',required=True)
    p.add_argument('--expected-eta-text',default='1')
    p.add_argument('--reference54-directory',type=Path)
    p.add_argument('--reference-direct-directory',type=Path)
    p.add_argument('--source-directory',type=Path)
    p.add_argument('--out-summary',type=Path,required=True)
    p.add_argument('--out-detail',type=Path,required=True)
    a=p.parse_args()
    for output in (a.out_summary,a.out_detail):
        require(not output.exists() and not output.resolve().is_relative_to(a.directory.resolve()),
                'new audit output outside immutable input directory')
    summary,detail=audit(a)
    payload=(json.dumps(detail,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode()
    packed=gzip.compress(payload,mtime=0)
    a.out_detail.parent.mkdir(parents=True,exist_ok=True)
    a.out_detail.write_bytes(packed)
    summary['complete_byte_detail']=dict(file=a.out_detail.name,bytes=len(packed),sha256=sha(packed),
        decompressed_bytes=len(payload),decompressed_sha256=sha(payload))
    raw=(json.dumps(summary,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()
    a.out_summary.parent.mkdir(parents=True,exist_ok=True)
    a.out_summary.write_bytes(raw)
    print(json.dumps(dict(passed=True,summary=str(a.out_summary),summary_bytes=len(raw),
        summary_sha256=sha(raw),detail=str(a.out_detail),detail_sha256=sha(packed))),flush=True)


if __name__=='__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps(dict(passed=False,error=repr(error),
            science_recomputed=False,complete_audit_not_claimed=True)),file=sys.stderr,flush=True)
        raise

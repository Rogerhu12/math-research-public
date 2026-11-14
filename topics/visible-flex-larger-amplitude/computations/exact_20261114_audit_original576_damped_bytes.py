#!/usr/bin/env python3
"""Byte-only audit of original576 R273 output and its two exact ledgers.

This standard-library program imports only the pinned earlier byte-audit
utilities.  It never imports NumPy, SciPy, a scientific producer or a
system adapter; it never evaluates a row, norm, rational magnitude, QR,
matrix action, sigma*z, RHS, Jacobian or nonlinear trial.  Scientific
numbers are copied from the actual public Actions reports.  This audit
does not add a direction or nonlinear acceptance gate.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import struct
import sys
import time


HERE = Path(__file__).resolve().parent
UTIL_NAME = 'exact_20261114_audit_damped_chain_bytes.py'
UTIL_SHA = '5618d29c41d95d668c959b05cee8295ce4285b2a50961277f557f8cfb717b440'
PRODUCER = 'exact_20261114_original576_damped_chain_qr.py'
PRODUCER_SHA = 'e1a35bd82433cfe6525047cb3ceb3d0c434c1ebaa62680cb0f1fdab0e76cfaec'
SYSTEM = 'exact_20261114_original576_damped_system.py'
SYSTEM_SHA = 'c78dfc6a5ef64a9de8bbbc857a927c6cd1078bbfb2281be62be4eb942014b207'
FACTOR = 'exact_20261114_native_damped_chain_qr.py'
FACTOR_SHA = '9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33'
KERNEL = 'exact_20261114_native_allrows_dyadic_residual.py'
KERNEL_SHA = '0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
READER = 'geometry_20261114_native_captured_band_correction.py'
READER_SHA = 'b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
CAPTURE_SHA = 'ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
FULL_J_SHA = '394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19'
MATRIX_SCOPE = 'actual28-original576-finite-binary64-complete-J-r-sigma-chain'
MODEL_SCOPE = 'R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates'
REF_RESULT = 'c6feb54847e96778b076076ba17b4ccd666c2548c72f8c36414b2897d176cdc1'
REF_DELTA = '5b6e7bb4205ce79c6d0f20b63e491def9747e95a3272e8add1712595ea1c4a85'
REF_MATRIX = '76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999'
REF_PINS = {
    'input_binding':'32cb5a0b92ab4ce642b65c0b75ba010ff26dcab5cbf77b1b847b5b469ea5279f',
    'array_manifest':'8a77b6b6365562ae3d41b3ff4832576f0bd880f41f2b5ed0a8fdefa86a650401',
    'restricted_old_node_delta':REF_DELTA,
    'restricted_direction_checkpoint':'691d2b98bbd767c7c524bc9e7d6dd287067a0e9283939401d8b80bf028d72d84'}
INPUT_NAMES = ('base-states','stage-residuals','stage-out','original-scales',
               'cut-residual','end-residual','original-far-graph','physical-height','cut-target')


def utilities():
    path = HERE/UTIL_NAME
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != UTIL_SHA:
        raise ValueError('Pinned standard-library byte-audit utilities changed')
    spec = importlib.util.spec_from_file_location('_original576_byte_audit_utilities', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Original28Bytes:
    """Bind the complete original capture using only byte and JSON operations."""

    def __init__(self, U, directory, binding):
        self.U, self.files, self.binding = U,U.Files(directory),binding
        require = U.require
        files = self.files
        result = files.json('result.json')
        require(files.info('result.json')['sha256'] == CAPTURE_SHA, 'actual28 complete result SHA')
        require(binding['original_capture_result'] == files.info('result.json'),
                'new adapter binds actual28 complete result descriptor')
        original = binding['original_capture_binding']
        require(original['capture_result_sha256'] == CAPTURE_SHA, 'original capture binding result')
        small = {}
        for desc in result['small_output_files']:
            require(desc['file'] not in small, 'unique original28 small-file entry')
            files.check(desc)
            small[desc['file']] = desc
        for name in ('capture-spec.json','capture-summary.json','capture-manifest.json',
                     'capture-begin.json','core-instrumentation.json','large-array-chunks.jsonl',
                     'original-live-identity-before-seed.json'):
            require(name in small, 'complete original28 small output '+name)
        self.manifest = files.json(small['capture-manifest.json'])
        self.summary = files.json(small['capture-summary.json'])
        self.live = files.json(small['original-live-identity-before-seed.json'])
        self.begin = files.json(small['capture-begin.json'])
        core = files.json(small['core-instrumentation.json'])
        for key,name in (('capture_spec_sha256','capture-spec.json'),
                         ('capture_summary_sha256','capture-summary.json'),
                         ('capture_manifest_sha256','capture-manifest.json')):
            require(original[key] == small[name]['sha256'], 'original28 bound '+key)
        require(original['capture_source_sha256'] == result['source_sha256'] and
                original['capture_hook_sha256'] == result['hook_sha256'] and
                original['original_core_sha256'] == core['original_core_file_sha256'],
                'original28 original source identities')
        require(core['exact_insertion_roundtrip_verified'] is True,
                'saved actual28 source roundtrip record')
        require((self.begin['M'],self.begin['K'],self.begin['depth']) == (112,224,576),
                'actual28 full original layout')
        require(self.manifest['completed'] and self.summary['capture_completed'] and
                self.manifest['dtype'] == '<f8' and self.manifest['order'] == 'C',
                'actual28 complete array manifest')
        self.arrays = {entry['name']:entry for entry in self.manifest['arrays']}
        require(len(self.arrays) == len(self.manifest['arrays']) == original['complete_arrays'],
                'all original28 arrays uniquely named')
        require({name:row['raw_sha256'] for name,row in self.arrays.items()} ==
                original['raw_array_sha256'], 'all original28 complete array hashes bound')
        self.J_block_hashes = []
        chunk_count = byte_count = 0
        chunk_ledger = []
        used_files = set()
        for name,entry in self.arrays.items():
            require(entry['completed'] and entry['dtype'] == '<f8' and entry['order'] == 'C',
                    'complete original28 array '+name)
            shape = entry['shape'];width = U.product_shape(shape[1:])*8
            expected_rows = 0;full = hashlib.sha256();total = 0
            for chunk_index,desc in enumerate(entry['chunks']):
                require(desc['array'] == name and desc['chunk_index'] == chunk_index and
                        desc['row_start'] == expected_rows and
                        type(desc['row_stop']) is int and expected_rows < desc['row_stop'] <= shape[0],
                        'original28 complete contiguous chunk order '+name)
                require(desc['file'] not in used_files, 'original28 chunk files are unique')
                used_files.add(desc['file'])
                raw = files.path(desc['file']).read_bytes()
                info = files.info(desc['file'])
                require(len(raw) == desc['bytes'] == (desc['row_stop']-expected_rows)*width and
                        U.sha(raw) == desc['raw_sha256'] == info['sha256'],
                        'complete original28 raw chunk bytes '+name)
                if 'sha256' in desc:
                    require(desc['sha256'] == info['sha256'], 'original28 file/raw SHA alias')
                full.update(raw);total += len(raw);chunk_count += 1
                if name == 'stage-jacobians':
                    require(shape == [576,224,224] and width == 224*224*8,
                            'all original28 J columns retained')
                    for offset in range(0,len(raw),width):
                        self.J_block_hashes.append(U.sha(raw[offset:offset+width]))
                expected_rows = desc['row_stop']
                chunk_ledger.append(desc)
            require(expected_rows == shape[0] and total == U.product_shape(shape)*8 == entry['total_bytes']
                    and full.hexdigest() == entry['raw_sha256'], 'original28 full array bytes '+name)
            byte_count += total
        require(chunk_count == original['complete_chunks'] and byte_count == original['complete_raw_bytes'],
                'original28 complete chunks and bytes')
        saved_ledger = [json.loads(line) for line in files.path('large-array-chunks.jsonl').read_bytes().splitlines()]
        require(saved_ledger == chunk_ledger, 'complete original28 chunk ledger exact metadata')
        require(len(self.J_block_hashes) == 576 and
                self.arrays['stage-jacobians']['raw_sha256'] == FULL_J_SHA,
                'all576 original J blocks and complete stream')
        require(len(binding['cells']) == len(binding['complete_block_manifest']) == 576 and
                len(self.live['stages']) == 576, 'all original stage locations')
        for n,row in enumerate(binding['complete_block_manifest']):
            source = self.live['stages'][n]
            cell = dict(originalStage=n,rawCell=source['rawCell'],rawSegment=source['rawSegment'],
                        kind='original-native-macro-stage')
            require(binding['cells'][n] == cell and row['stage'] == row['original_stage'] == n and
                    row['raw_sha256'] == self.J_block_hashes[n] and row['bytes'] == 224*224*8 and
                    row['origin'] == 'unchanged-actual28-original-J' and row['original_stage_location'] == cell,
                    'original576 block manifest exact source identity')
        self.record = dict(actual28_result=files.info('result.json'),
            complete_raw_arrays=len(self.arrays),complete_chunks=chunk_count,complete_raw_bytes=byte_count,
            all_original576_J_block_hashes_equal=True,complete_original_J_sha256=FULL_J_SHA,
            complete_saved_capture_metadata_equal=True,source_files=list(files.records.values()))

    def raw(self, name):
        return b''.join(self.files.path(d['file']).read_bytes() for d in self.arrays[name]['chunks'])

    def stage(self, node):
        width = 224*224*8
        for desc in self.arrays['stage-jacobians']['chunks']:
            if desc['row_start'] <= node < desc['row_stop']:
                raw = self.files.path(desc['file']).read_bytes()
                self.U.require(self.U.sha(raw) == desc['raw_sha256'], 'immutable original J source chunk')
                start = (node-desc['row_start'])*width
                return raw[start:start+width], self.files.info(desc['file'])
        raise ValueError('No original J block for saved witness')


def reference57(U, directory, saved_receipt, current_binding, exported_raw, exported_descriptor):
    files=U.Files(directory);require=U.require
    result=files.json('result.json.gz')
    require(files.info('result.json.gz')['sha256'] == REF_RESULT and
            saved_receipt['result'] == {key:files.info('result.json.gz')[key]
                                       for key in ('file','bytes','sha256')},
            'actual57 fixed complete result')
    require(result['schema'] == 'complete-native-direct-LD-J1372-damped-square-root-direction-v1' and
            result['source_sha256'] == FACTOR_SHA and result['new_matrix_identity_sha256'] == REF_MATRIX,
            'actual57 source and distinct original1372 target')
    selected={key:result[key] for key in REF_PINS}
    require(saved_receipt['selected_files'] == selected, 'all selected actual57 descriptor aliases')
    for key,digest in REF_PINS.items():
        require(result[key]['sha256'] == digest, 'fixed actual57 selected SHA '+key)
        files.check(result[key])
    binding=files.json(result['input_binding']);manifest=files.json(result['array_manifest'])
    cp=files.json(result['restricted_direction_checkpoint'])
    require(binding['new_matrix_identity_sha256'] == REF_MATRIX and
            binding['original1372_input_binding']['original_capture_binding'] ==
            current_binding['original_capture_binding'], 'both directions share exactly original actual28')
    require(manifest['source_sha256'] == FACTOR_SHA and manifest['new_matrix_identity_sha256'] == REF_MATRIX,
            'actual57 descriptor source/target')
    desc=result['restricted_old_node_delta']
    require([d for d in manifest['arrays'] if d['name'] == desc['name']] == [desc],
            'actual57 complete restricted descriptor alias')
    raw=files.raw(desc)
    require(raw == exported_raw and U.sha(raw) == REF_DELTA and desc['shape'] == [577,224],
            'actual57 saved original-node direction is unchanged in current output')
    require(cp['schema'] == 'complete-original-node-restriction-of-damped-chain-direction-v1' and
            cp['source_sha256'] == FACTOR_SHA and cp['input_binding'] == binding and
            (cp['M'],cp['K'],cp['depth'],cp['original_depth'],cp['step_depth']) == (112,224,576,576,1372) and
            cp['old_to_new'] == binding['old_to_new'] and cp['restricted_to_original_nodes'] is True,
            'actual57 checkpoint retains distinct source depth/restriction')
    require(cp['eta_binary64'] == result['eta_binary64'] and cp['model_scope'] == MODEL_SCOPE,
            'actual57 source eta and coordinates')
    require(U.checkpoint_bytes(cp,577,224,'actual57 saved restriction') == raw,
            'actual57 checkpoint all words and negative zero')
    require(saved_receipt['exported_reference_array'] == exported_descriptor and
            saved_receipt['actual_restricted577_delta_sha256'] == REF_DELTA and
            saved_receipt['source_complete1373_delta_sha256'] == result['step_delta']['sha256'] and
            saved_receipt['source_matrix_identity_sha256'] == REF_MATRIX and
            saved_receipt['current_original576_matrix_identity_sha256'] == current_binding['new_matrix_identity_sha256'],
            'actual57 receipt source/current identities')
    for flag in ('same_original_actual28_capture_binding','source_reference_direction_bytes_unchanged',
                 'current_exact_readback_is_on_the_original576_target_not_the_source1372_target',
                 'source_full1373_direction_not_reloaded','source_factors_not_reloaded',
                 'this_does_not_reaudit_the_original1373_to577_restriction_operation',
                 'reference_is_not_a_new_candidate_or_new_native_state'):
        require(saved_receipt[flag] is True, 'actual57 reference scope '+flag)
    require(len(files.records) == 5, 'read precisely five selected actual57 files')
    return dict(all_five_selected_files_verified=True,checkpoint_all_words_verified=True,
        current_reference_bytes_equal=True,same_original28_capture=True,
        original1373_source_and_current576_target_kept_distinct=True,
        full1373_restriction_operation_not_reaudited=True,
        other_actual57_payloads_not_opened=True,
        files=[files.info(name) for name in sorted(files.records)])


def witness(U, files, desc, maximum, binding, direction_raw, direction_sha, original_raw, capture):
    require=U.require;witness=files.json(desc);w=witness['operands']
    matrix=binding['new_matrix_identity_sha256']
    require(witness['source_sha256'] == PRODUCER_SHA and witness['kernel_sha256'] == KERNEL_SHA and
            witness['new_matrix_identity_sha256'] == matrix and
            witness['direction_float64le_sha256'] == direction_sha and
            witness['exact_original_sigma_maximum'] == maximum, 'actual worst witness report identity')
    n,j,kind=w['node'],w['row'],w['kind']
    require((n,j,kind) == (maximum['node'],maximum['row'],maximum['kind']) and
            w['matrix_scope'] == MATRIX_SCOPE and w['new_matrix_identity_sha256'] == matrix and
            w['complete_direction_float64le_sha256'] == direction_sha, 'worst operands scope/location')
    def word(raw,index):return raw[index*8:(index+1)*8].hex()
    require(w['original_sigma_float64le_hex'] == word(original_raw['original-scales'],n),
            'worst original sigma word')
    source=None
    if kind == 'stage':
        require(w['full_next_delta_float64le_hex'] == direction_raw[(n+1)*224*8:(n+2)*224*8].hex() and
                w['current_delta_float64le_hex'] == word(direction_raw,n*224+j) and
                w['original_residual_float64le_hex'] == word(original_raw['stage-residuals'],n*224+j),
                'all original stage residual/direction operands')
        J,source=capture.stage(n)
        require(w['original_J_stage_sha256'] == binding['complete_block_manifest'][n]['raw_sha256'] == U.sha(J)
                and w['full_original_J_row_float64le_hex'] == J[j*224*8:(j+1)*224*8].hex()
                and w['original_stage_location'] == capture.live['stages'][n],
                'all worst original J row words and source location')
    elif kind == 'cut':
        require(w['current_delta_float64le_hex'] == word(direction_raw,j) and
                w['original_residual_float64le_hex'] == word(original_raw['cut-residual'],j),
                'all worst cut operands')
    elif kind == 'far':
        require(w['delta_Q_float64le_hex'] == word(direction_raw,576*224+j) and
                w['delta_Pi_float64le_hex'] == word(direction_raw,576*224+112+j) and
                w['original_far_G_float64le_hex'] == word(original_raw['original-far-graph'],j) and
                w['original_residual_float64le_hex'] == word(original_raw['end-residual'],j),
                'all worst far operands')
    else:raise ValueError('Unknown original worst row kind')
    return dict(all_saved_worst_operand_words_equal=True,actual_J_source_chunk=source,
                no_product_sum_or_rational_arithmetic_recomputed=True)


def audit(a,U):
    started=time.monotonic();require=U.require;files=U.Files(a.directory)
    result=files.json('result.json.gz')
    require(files.info('result.json.gz')['sha256'] == a.expected_result_sha256,
            'explicit actual original576 result SHA')
    for key,value in dict(schema='complete-native-original576-damped-square-root-direction-v1',
            source_sha256=PRODUCER_SHA,system_source_sha256=SYSTEM_SHA,
            factor_engine_source_sha256=FACTOR_SHA,kernel_source_sha256=KERNEL_SHA,
            diagnostic_completed=True,linear_direction_computed=True,native_accepted=False,task_completed=False,
            original_native_calls=0,new_RHS_calls=0,new_J_calls=0,new_ODE_steps=0,nonlinear_trials=0).items():
        require(result[key] == value, 'complete original576 result '+key)
    require(result['eta_cli_text'] == a.expected_eta_text and result['model_scope'] == MODEL_SCOPE,
            'explicit original576 eta/model')
    U.number_word(result['eta_binary64'],struct.pack('<d',float(a.expected_eta_text)),'eta CLI serialization')
    summary=files.json('summary.json');files.check(summary['full_result'])
    for key in set(summary).intersection(result)-{'schema'}:
        require(summary[key] == result[key], 'actual small/full report field '+key)
    binding=files.json(result['input_binding'])
    for key,value in dict(schema='actual28-original576-complete-linear-system-binding-v1',
        matrix_scope=MATRIX_SCOPE,adapter_source_sha256=SYSTEM_SHA,frozen_capture_reader_sha256=READER_SHA,
        original_capture_result_sha256=CAPTURE_SHA,modes=112,shape_dimension=224,depth=576,
        original_depth=576,node_count=577,old_to_new=list(range(577)),original_J_full_raw_sha256=FULL_J_SHA).items():
        require(binding[key] == value, 'new original576 complete binding '+key)
    matrix=binding['new_matrix_identity_sha256']
    require(U.canonical_sha(binding['matrix_identity_definition']) == matrix == result['new_matrix_identity_sha256'],
            'new matrix canonical byte/metadata identity')
    definition=binding['matrix_identity_definition']
    require(definition['matrix_scope'] == MATRIX_SCOPE and definition['original_J_full_raw_sha256'] == FULL_J_SHA
            and definition['original_input_raw_sha256'] == binding['raw_array_sha256'] and
            definition['block_manifest'] == [{k:r[k] for k in ('stage','bytes','raw_sha256')}
                                             for r in binding['complete_block_manifest']],
            'all original matrix descriptor members')
    capture=Original28Bytes(U,a.capture_directory,binding)
    manifest=files.json(result['array_manifest'])
    require(manifest['schema'] == 'complete-native-original576-damped-direction-arrays-v1' and
            manifest['source_sha256'] == PRODUCER_SHA and manifest['factor_engine_source_sha256'] == FACTOR_SHA
            and manifest['new_matrix_identity_sha256'] == matrix, 'full output array identity')
    entries=manifest['arrays'];by_name={d['name']:d for d in entries};by_file={d['file']:d for d in entries}
    require(len(by_name) == len(by_file) == len(entries), 'unique output array names and paths')
    raw_audits=[]
    for index,desc in enumerate(entries):
        if desc['dtype'] == '<f8':raw_audits.append(files.classify_f64(desc))
        else:
            require(desc['dtype'] == 'exact-dyadic-jsonl-gzip', 'known exact ledger array type')
            files.check(desc)
        if (index+1)%128 == 0:
            print(json.dumps(dict(event='original576_byte_audit',arrays_checked=index+1,
                                  total_arrays=len(entries))),flush=True)
    def member(desc):
        require(desc == by_file[desc['file']], 'complete output descriptor alias')
        return files.raw(desc)
    original=result['original_arrays'];require(set(original) == set(INPUT_NAMES),'all nine original inputs')
    original_raw={name:member(desc) for name,desc in original.items()}
    for name,desc in original.items():
        require(original_raw[name] == capture.raw(name) and desc['sha256'] == binding['raw_array_sha256'][name]
                and desc['shape'] == capture.arrays[name]['shape'], 'unchanged full actual28 '+name)
    sigma=original_raw['original-scales']
    ref_receipt=files.json(result['reference57_binding'])
    ref_desc=ref_receipt['exported_reference_array'];ref_raw=member(ref_desc)
    reference_record=reference57(U,a.reference57_directory,ref_receipt,binding,ref_raw,ref_desc)
    factor=files.json(result['factor_report']);index=files.json(result['factor_index'])
    inventory=files.json(result['formed_stage_inventory'])
    require(factor['complete'] and index['complete'] and factor['source_sha256'] == FACTOR_SHA and
            index['source_sha256'] == inventory['source_sha256'] == PRODUCER_SHA and
            index['factor_engine_source_sha256'] == inventory['factor_engine_source_sha256'] == FACTOR_SHA,
            'actual borrowed factor source distinguished from new entry source')
    require(factor['input_matrix_identity_sha256'] == index['new_matrix_identity_sha256'] ==
            inventory['new_matrix_identity_sha256'] == matrix,'all factor and formed target identities')
    for key,value in result['factor_summary'].items():require(factor[key] == value,'factor summary field '+key)
    for key,value in dict(rows=129248,columns=129248,augmented_rows=258496,stage_count=576,node_count=577,
            block_width=224,node_penalty_blocks=577,pure_constant_rows=129248,qr_calls=1153,formation_calls=1152).items():
        require(factor[key] == value, 'complete original576 factor count '+key)
    require(factor['eta_binary64'] == result['eta_binary64'] and factor['model_scope'] == MODEL_SCOPE,
            'same recorded factor eta and coordinate model')
    factors=index['factors'];require(len(factors) == 577,'all577 complete factors')
    total_factor_bytes=constant_rows=lower_zero_words=0;factor_records=[]
    for n,item in enumerate(factors):
        final=n==576;cols=225 if final else 449;count=336 if final else 112 if n==0 else 224
        require(item['node'] == n and item['final'] == final and item['R_columns'] == [0,224]
                and item['S_columns'] == (None if final else [224,448]) and
                item['affine_column'] == (224 if final else 448),'complete factor block layout')
        require(item['factor']['shape'] == [224,cols] and item['constant']['shape'] == [count],
                'complete R/S/affine and pure constant shapes')
        raw=member(item['factor']);member(item['constant'])
        for row in range(224):
            require(not any(raw[row*cols*8:(row*cols+row)*8]),'literal lower R triangle is zero')
            lower_zero_words+=row
        total_factor_bytes+=item['factor']['bytes']+item['constant']['bytes'];constant_rows+=count
        factor_records.append(dict(node=n,factor=item['factor'],constant=item['constant'],
                                   lower_R_zero_words_verified=224*223//2))
    require(total_factor_bytes == factor['actual_factor_and_constant_bytes'] ==
            factor['expected_factor_and_constant_bytes'] and constant_rows == 129248,
            'all factor and pure constant payloads present')
    stages=inventory['stages'];require(len(stages) == 576,'all576 formed source records')
    for n,item in enumerate(stages):
        require(item['stage'] == n and item['original_J_raw_sha256'] ==
                binding['complete_block_manifest'][n]['raw_sha256'],'formed source J block identity')
        U.number_word(item['original_sigma_current'],sigma[n*8:(n+1)*8],'formed current original sigma')
        U.number_word(item['original_sigma_next'],sigma[(n+1)*8:(n+2)*8],'formed next original sigma')
    model_hash=U.canonical_sha(dict(original_matrix=matrix,sigma=original['original-scales']['sha256'],
        eta_bits=result['eta_binary64']['float64le_hex'],source_sha256=FACTOR_SHA,precision=factor['working_precision'],
        stages=[{k:r[k] for k in ('stage','original_J_raw_sha256','formed_V_raw_sha256','formed_rho_raw_sha256',
            'combined_formed_bytes_sha256','original_sigma_current','original_sigma_next')} for r in stages],
        cut=factor['formed-cut-rho']['array'],far=factor['formed-far-rho']['array']))
    require(model_hash == factor['formed_model_identity_sha256'] == inventory['formed_model_identity_sha256'] ==
            result['formed_model_diagnostic']['model_identity_sha256'], 'canonical formed model identity')
    member(factor['formed-cut-rho']['array']);member(factor['formed-far-rho']['array'])
    solve=factor['solve'];z=member(solve['scaled_z']);delta=member(solve['delta'])
    require(solve['delta'] == result['native_delta'] and solve['triangular_solves'] == 577,
            'complete native original576 saved direction')
    require(result['native_delta']['shape'] == [577,224] and solve['scaled_z']['shape'] == [577,224],
            'full original576 z/delta shape')
    underflows=sum(1 for (zw,),(dw,) in zip(U.words(z),U.words(delta))
                   if (zw&U.MASK_ABS)!=0 and (dw&U.MASK_ABS)==0)
    require(underflows == solve['nonzero_recovery_to_zero'],'saved sigma*z underflow classification only')
    for example in solve['recovery_underflow_examples']:
        n,j=example['node'],example['column'];offset=(n*224+j)*8
        U.number_word(example['z'],z[offset:offset+8],'recovery saved z operand')
        U.number_word(example['sigma'],sigma[n*8:(n+1)*8],'recovery saved sigma operand')
        U.number_word(example['delta'],delta[offset:offset+8],'recovery saved delta result')
    cp=files.json(result['native_direction_checkpoint'])
    for key,value in dict(schema='complete-native-original576-damped-direction-v1',source_sha256=PRODUCER_SHA,
            system_source_sha256=SYSTEM_SHA,factor_engine_source_sha256=FACTOR_SHA,input_binding=binding,
            M=112,K=224,depth=576,original_depth=576,old_to_new=list(range(577)),
            eta_binary64=result['eta_binary64'],model_scope=MODEL_SCOPE,original576_full_direction=True,
            not_a_restriction_of_a1372_direction=True,
            original_cut_and_far_direction_components_not_projected_or_zeroed=True).items():
        require(cp[key] == value,'actual full direction checkpoint '+key)
    require('step_depth' not in cp and U.checkpoint_bytes(cp,577,224,'original576 full direction') == delta,
            'full original576 checkpoint including signed zero; no1372 restriction metadata')
    exact_records={};witness_records={}
    for label,key,raw,desc in (('current_damped','original_exact_readback',delta,result['native_delta']),
                               ('reference57','reference57_original576_exact_readback',ref_raw,ref_desc)):
        exact=result[key];detail=files.json(exact['full_report'])
        for k,v in dict(schema='original576-complete-exact-direction-readback-v1',source_sha256=PRODUCER_SHA,
                system_source_sha256=SYSTEM_SHA,kernel_sha256=KERNEL_SHA,matrix_scope=MATRIX_SCOPE,
                new_matrix_identity_sha256=matrix,direction_label=label,direction_float64le_sha256=desc['sha256'],
                exact_rows=129248,completed_stages=576,original_product_positions=576*224*224+112).items():
            require(detail[k] == v,'complete same-target exact readback '+label+' '+k)
        for k in ('exact_global_original_sigma_norm','exact_stored_base_sigma_norm','exact_rows','completed_stages',
                  'original_product_positions','all_exact_residual_rows','worst_witness',
                  'no_float_refinement_RHS_formed','used_as_new_nonlinear_acceptance_gate'):
            require(detail[k] == exact[k],'exact copied report field '+label+' '+k)
        require(detail['eta_not_in_original_equations'] and
                detail['readback_uses_unscaled_J_and_r_before_exact_sigma_division'] and
                detail['used_as_new_nonlinear_acceptance_gate'] is False,'original exact scope')
        if label=='reference57':require(detail['direction_provenance'] == ref_receipt,'actual57 exact provenance')
        require(exact['all_exact_residual_rows'] == by_file[exact['all_exact_residual_rows']['file']],
                'exact ledger complete array descriptor')
        exact_records[label]=U.audit_ledger(files,exact['all_exact_residual_rows'],detail,binding,
                                           desc['sha256'],sigma,112,224,576)
        with gzip.open(files.path(exact['all_exact_residual_rows']['file']),'rb') as f:
            for line in f:
                row=json.loads(line)
                require(row['direction_label'] == label and row['exact_original_sigma_maximum']['matrix_scope'] ==
                        MATRIX_SCOPE,'all exact block direction labels and original target scope')
        witness_records[label]=witness(U,files,exact['worst_witness'],detail['exact_global_original_sigma_norm'],
                                       binding,raw,desc['sha256'],original_raw,capture)
    require(result['original_exact_readback']['exact_stored_base_sigma_norm'] ==
            result['reference57_original576_exact_readback']['exact_stored_base_sigma_norm'],
            'same stored base record for both complete original576 readbacks')
    sources=[]
    if a.source_directory:
        for name,digest in ((PRODUCER,PRODUCER_SHA),(SYSTEM,SYSTEM_SHA),(FACTOR,FACTOR_SHA),
                            (KERNEL,KERNEL_SHA),(READER,READER_SHA),(UTIL_NAME,UTIL_SHA)):
            size,observed=U.stream_sha(a.source_directory/name)
            require(observed == digest,'frozen original source file '+name)
            sources.append(dict(file=name,bytes=size,sha256=observed))
    all_files=files.complete_inventory()
    detail_out=dict(schema='original576-complete-output-byte-audit-detail-v1',
        producer_result=files.info('result.json.gz'),files=all_files,raw_arrays=raw_audits,
        factors=factor_records,original28=capture.record,selected_actual57=reference_record,
        exact_row_ledgers=exact_records,worst_source_operand_checks=witness_records,source_files=sources,
        source_files_only_bound_by_saved_ledgers_when_no_source_directory=not bool(a.source_directory))
    summary_out=dict(schema='original576-complete-output-byte-audit-summary-v1',
        classification='saved-byte/structure only; scientific values copied from original Actions',
        passed=True,scientific_calculation_performed_locally=False,numerical_acceptance_gate=False,
        source_audit_sha256=U.stream_sha(__file__)[1],byte_utility_source_sha256=UTIL_SHA,
        producer_result=files.info('result.json.gz'),producer_source_sha256=PRODUCER_SHA,
        factor_engine_source_sha256=FACTOR_SHA,new_matrix_identity_sha256=matrix,
        formed_model_identity_sha256=model_hash,eta=result['eta_binary64'],
        all_array_descriptors_verified=len(entries),all_float64_arrays_verified=len(raw_audits),
        complete_file_inventory_count=len(all_files),complete_factor_nodes=577,
        complete_factor_and_constant_bytes=total_factor_bytes,complete_pure_constant_rows=constant_rows,
        all_R_lower_triangle_zero_words_checked=lower_zero_words,complete_full_native_delta_verified=True,
        checkpoint_all_words_and_negative_zero_annotations_verified=True,
        actual57_five_original_files_and_saved_direction_verified=True,
        all_original28_capture_arrays_and_J_blocks_verified=True,
        actual_sigma_times_z_multiplication_not_recomputed=True,
        saved_recovery_underflow_count=solve['nonzero_recovery_to_zero'],
        exact_row_ledgers=exact_records,worst_source_operand_checks=witness_records,source_files=sources,
        copied_Actions_scientific_reports=dict(factor_summary=result['factor_summary'],solve=solve,
            formed_model_diagnostic=result['formed_model_diagnostic'],
            original_exact_readback=result['original_exact_readback'],
            reference57_original576_exact_readback=result['reference57_original576_exact_readback']),
        limits=[
            'No QR, solve, RHS, J, sigma*z, action, norm, rational arithmetic or residual was recomputed.',
            'Saved per-block/global maxima are located verbatim, not independently re-maximized.',
            'Formed V/rho hashes and complete metadata are checked, but these unexported coefficient payloads are not reformed.',
            'All actual28 original input chunks are hashed; their mathematical derivative accuracy is not proved by this audit.',
            'The selected actual57 five files preserve its saved577 direction; the original1373-to577 operation is not repeated.',
            'There is no native nonlinear acceptance claim or new acceptance threshold.'],
        elapsed_byte_audit_seconds=time.monotonic()-started)
    return summary_out,detail_out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory',type=Path,required=True)
    p.add_argument('--expected-result-sha256',required=True)
    p.add_argument('--expected-eta-text',default='1')
    p.add_argument('--capture-directory',type=Path,required=True)
    p.add_argument('--reference57-directory',type=Path,required=True)
    p.add_argument('--source-directory',type=Path)
    p.add_argument('--out-summary',type=Path,required=True)
    p.add_argument('--out-detail',type=Path,required=True)
    a=p.parse_args();U=utilities()
    U.require(re.fullmatch(r'[0-9a-f]{64}',a.expected_result_sha256) is not None,'explicit actual result SHA')
    for output in (a.out_summary,a.out_detail):
        U.require(not output.exists() and not any(output.resolve().is_relative_to(x.resolve())
                  for x in (a.directory,a.capture_directory,a.reference57_directory)),
                  'new audit output outside immutable input directories')
    U.require(a.out_summary.resolve()!=a.out_detail.resolve() and
              a.out_summary.parent.resolve()==a.out_detail.parent.resolve(),
              'two distinct sibling audit outputs preserve the relative detail receipt')
    summary,detail=audit(a,U)
    raw=(json.dumps(detail,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode()
    packed=gzip.compress(raw,mtime=0)
    a.out_detail.parent.mkdir(parents=True,exist_ok=True);a.out_detail.write_bytes(packed)
    summary['complete_byte_detail']=dict(file=a.out_detail.name,bytes=len(packed),sha256=U.sha(packed),
        decompressed_bytes=len(raw),decompressed_sha256=U.sha(raw))
    report=(json.dumps(summary,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()
    a.out_summary.write_bytes(report)
    print(json.dumps(dict(passed=True,summary=str(a.out_summary),summary_bytes=len(report),
        summary_sha256=U.sha(report),detail=str(a.out_detail),detail_sha256=U.sha(packed))),flush=True)


if __name__=='__main__':
    try:main()
    except Exception as error:
        print(json.dumps(dict(passed=False,error=repr(error),science_recomputed=False,
                              complete_audit_not_claimed=True)),file=sys.stderr,flush=True)
        raise

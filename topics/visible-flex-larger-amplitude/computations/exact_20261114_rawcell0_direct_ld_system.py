#!/usr/bin/env python3
"""Bind a new direct-longdouble/f64 Jacobian stream to the actual1372 system.

Only the 868 rawCell0 shape Jacobians change.  This module retains the
already identified actual41 base, residuals, all sigma words, original
cut/far/H and the 504 unchanged actual28 blocks.  It does not evaluate a
field, root, ODE step, Jacobian, nonlinear trial or mathematical norm.
The new source-bound f64 matrix is not either previous finite matrix.
Scientific array binding is restricted to this public repository Actions.
"""
from __future__ import annotations

import hashlib
import gzip
import importlib
import json
import math
from pathlib import Path
import re

import numpy as np


HERE = Path(__file__).resolve().parent
STEP_NAME = 'exact_20261114_rawcell0_step_system.py'
STEP_SHA = 'fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81'
BAND_SHA = 'b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
CAPTURE_SHA = 'ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
STEP_RESULT_SHA = '6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf'
PARENT_MATRIX_SHA = 'e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521'
DIRECT_RESULT_SCHEMA = 'native-rawcell0-saved-step-direct-longdouble-maps-v1'
DIRECT_ARITHMETIC_NAME = 'geometry_20261114_saved_stage_rk_covariance.py'
DIRECT_ARITHMETIC_SHA = '01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548'
MATRIX_SCOPE = 'actual41-base-direct-longdouble-rounded-shape-J1372-system'
SOURCE_NAMES = {
    'source_sha256': 'geometry_20261114_native_rawcell0_direct_ld_capture.py',
    'hook_sha256': 'geometry_20261114_native_rawcell0_direct_ld_capture_hook.mjs',
    'window_module_sha256': 'geometry_20261114_native_rawcell0_direct_ld_window.mjs',
    'worker_source_sha256': 'geometry_20261114_rawcell0_direct_ld_worker.py',
}
SOURCE_SHA = {
    'source_sha256': 'a63ffda643044787cb0ad5fb0d7c2aa4e4b34090fefa4b9053f4f2550bf85dbf',
    'hook_sha256': '3499f7abb96a4f25c4c3a986d97dc8aea3b21742770aabe7abe2822ad8b3caf4',
    'window_module_sha256': '1ba3f30702b26aa78b4aceb0b2d3d5d71ea8fa858b114d982ead185330faa5d9',
    'worker_source_sha256': '87ab92d9234d6e58103d44d125ce5510f9cde34ac37df251b7e63dcb6747a9c8',
}


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for raw in iter(lambda: stream.read(1 << 20), b''):
            h.update(raw)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def load_step():
    source = HERE / STEP_NAME
    if file_sha(source) != STEP_SHA:
        raise ValueError('The complete actual41 system binder changed')
    module = importlib.import_module(Path(STEP_NAME).stem)
    if Path(module.__file__).resolve() != source.resolve():
        raise ValueError('Unexpected complete actual41 binder import path')
    return module


def load_binding():
    return load_step().load_binding()


def sha_text(value, label):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9a-f]{64}', value):
        raise ValueError('A complete SHA256 is required: ' + label)
    return value


class RawCell0DirectLDSystem:
    """One new finite1372 matrix with unchanged nonlinear base data.

    The producer's actual result SHA is mandatory.  Its four source-file
    hashes must match the checked-out source files, and are retained in
    the new identity.  No not-yet-created producer/result SHA is guessed.
    Original actual28/41 sources and actual41's full matrix remain pinned.
    """

    def __init__(self, capture_directory, step_directory, step_result_sha256,
                 direct_directory, direct_result_sha256, B=None):
        S = load_step()
        self.S = S
        self.B = B or S.load_binding()
        B = self.B
        B.actions_only()
        B.same(step_result_sha256, STEP_RESULT_SHA, 'the actual41 complete input')
        sha_text(direct_result_sha256, 'actual completed direct-LD result')
        # This constructs exactly the already published original1372 base.
        # Its r array is not reconstructed from any newly evaluated field.
        self.base = S.RawCell0StepSystem(capture_directory, step_directory,
                                        step_result_sha256, B)
        B.same(self.base.binding['new_matrix_identity_sha256'], PARENT_MATRIX_SHA,
               'the original actual41 expanded finite matrix identity')
        self.original = self.base.original
        self.directory = Path(direct_directory).resolve()
        self.step_result_sha256 = step_result_sha256
        self.direct_result_sha256 = direct_result_sha256
        result_path = B.safe_file(self.directory, 'result.json')
        B.same(file_sha(result_path), direct_result_sha256, 'actual new result bytes')
        self.result = B.read(result_path)
        result = self.result
        B.same(result.get('schema'), DIRECT_RESULT_SCHEMA, 'new finite-map producer schema')
        for key in ('completed', 'capture_completed'):
            B.same(result.get(key), True, 'complete direct-LD result ' + key)
        self.source_hashes = {}
        for key, name in SOURCE_NAMES.items():
            digest = sha_text(result.get(key), 'actual direct-LD producer ' + key)
            B.same(digest, SOURCE_SHA[key], 'frozen direct-LD producer identity ' + name)
            B.same(file_sha(HERE / name), digest, 'actual direct-LD source bytes ' + name)
            self.source_hashes[name] = digest
        B.same(result['original_capture_result_sha256'], CAPTURE_SHA, 'same actual28 result')
        B.same(result['actual41_result_sha256'], STEP_RESULT_SHA, 'same actual41 step result')
        B.same(result['direct_arithmetic_source_sha256'], DIRECT_ARITHMETIC_SHA,
               'same actual50 direct-RK expression')
        B.same(file_sha(HERE / DIRECT_ARITHMETIC_NAME), DIRECT_ARITHMETIC_SHA,
               'unchanged actual50 direct arithmetic source bytes')
        self.packet_receipts = {}
        self.summary = self.read_descriptor(result['summary'], 'complete direct-LD summary')
        self.manifest = self.read_descriptor(result['array_manifest'], 'complete direct-LD array manifest')
        summary, manifest = self.summary, self.manifest
        B.same(summary.get('schema'), 'native-rawcell0-saved-step-direct-longdouble-summary-v1',
               'complete summary schema')
        B.same(manifest.get('schema'), 'native-rawcell0-direct-longdouble-output-arrays-v1',
               'complete new array schema')
        for key in ('completed', 'capture_completed'):
            B.same(summary.get(key), True, 'complete direct-LD summary ' + key)
        for key in SOURCE_NAMES:
            B.same(summary.get(key), result[key], 'summary source identity ' + key)
            B.same(manifest.get(key), result[key], 'manifest source identity ' + key)
        B.same(summary['direct_arithmetic_source_sha256'], DIRECT_ARITHMETIC_SHA,
               'summary original direct-RK source')
        B.same(summary['original_capture_result_sha256'], CAPTURE_SHA, 'summary actual28 identity')
        B.same(summary['actual41_result_sha256'], STEP_RESULT_SHA, 'summary actual41 identity')
        B.same(summary['array_manifest'], result['array_manifest'], 'summary/manifest descriptor')
        B.same(result['stage_reports'], summary['stage_reports'], 'all72 actual stage report descriptors')
        B.same(manifest.get('completed'), True, 'all direct-LD arrays completed')
        self.direct_arrays = S.StepArrays(self.directory, manifest, B)
        # The old frozen raw I/O verifies every full raw hash and row range.
        # Also bind the separate file hashes when present in the new journal.
        for name, entry in self.direct_arrays.arrays.items():
            for row in entry['chunks']:
                path = B.safe_file(self.directory, row['file'])
                B.same(path.stat().st_size, row['bytes'], 'new chunk physical byte count')
                B.same(file_sha(path), row['sha256'], 'new chunk physical byte SHA256')
                B.same(row['sha256'], row['raw_sha256'], 'uncompressed canonical f64 chunk')
        self.validate_chunk_journal(manifest['chunk_ledger'])
        self.metadata_packets = {}
        for row in manifest['metadata_packets']:
            if row['file'] in self.metadata_packets:
                raise ValueError('An actual direct-LD metadata packet was listed twice')
            B.same(row['encoding'], 'json-gzip', 'complete step evidence encoding')
            self.verify_descriptor(row, 'complete streamed step evidence')
            self.metadata_packets[row['file']] = row

        for attr in ('M', 'K', 'depth', 'original_depth', 'selected', 'step_counts',
                     'old_to_new', 'cells', 'spec'):
            setattr(self, attr, getattr(self.base, attr))
        B.same((self.M, self.K, self.depth, self.original_depth), (112, 224, 1372, 576),
               'the complete actual41 dimensions, including all cusp steps')
        self.stage_reports = {}
        self.stage_arrays = {}
        self.step_report_receipts = []
        descriptors = summary['stage_reports']
        B.same(len(descriptors), len(S.SELECTED), 'all72 original rawCell0 stages')
        used_names = set()
        used_packets = set()
        for n, descriptor in zip(S.SELECTED, descriptors):
            report = self.read_descriptor(descriptor, 'direct-LD original stage ' + str(n))
            old = self.base.stage_reports[n]
            B.same(report['stage'], n, 'ordered original stage number')
            B.same(report['original_stage'], n, 'explicit original stage number')
            count = self.step_counts[n]
            B.same(report['step_count'], count, 'actual integrationGrid step count')
            B.same(report['schedule'], old['schedule'], 'complete original x/h/profile/port words')
            B.same(report['original_report'], self.base.summary['stage_reports'][n],
                   'same complete actual41 stage report')
            B.same(report['actual41_field_packet'], old['field_observations'],
                   'same original four-field evidence packet')
            B.same(report['actual41_window'], old['identity'], 'same original finite RK window')
            B.same(S.number_bits(report['original_sigma']), S.number_bits(old['original_sigma']),
                   'same original parent sigma bits')
            B.same(S.number_bits(report['original_port_ratio']), S.number_bits(old['original_port_ratio']),
                   'same original complete-stage port bits')
            for role, key in (
                ('full_states', 'actual41_full_states_raw_sha256'),
                ('shape_outputs', 'actual41_shape_outputs_raw_sha256'),
            ):
                old_name = self.base.stage_arrays[n][role]
                B.same(report[key], self.base.step_arrays.arrays[old_name]['raw_sha256'],
                       'unchanged actual41 ' + role + ' source bytes')
            names = report['arrays']
            for role, shape in (('shape_jacobians', [count, self.K, self.K]),
                                ('mean_jacobians', [count, 2, self.K])):
                name = names[role]
                if name in used_names or name not in self.direct_arrays.arrays:
                    raise ValueError('Every stage/shape/mean role requires one unique complete array')
                used_names.add(name)
                B.same(self.direct_arrays.arrays[name]['shape'], shape, 'complete new ' + role)
            steps = report['direct_ld_step_reports']
            if not isinstance(steps, dict):
                raise ValueError('Every completed stage needs its full source-bound step packet')
            B.same(steps, self.metadata_packets.get(steps['file']), 'declared whole step packet')
            if steps['file'] in used_packets:
                raise ValueError('A complete stage step packet is reused')
            used_packets.add(steps['file'])
            step_packet = self.read_descriptor(steps, 'direct-LD step identity packet ' + str(n))
            B.same(step_packet['schema'], 'native-rawcell0-direct-longdouble-step-evidence-v1',
                   'new complete step packet schema')
            B.same((step_packet['original_stage'], step_packet['completed'], step_packet['partial']),
                   (n, True, False), 'complete and correctly indexed step packet')
            for key in SOURCE_NAMES:
                B.same(step_packet[key], result[key], 'step packet source identity ' + key)
            old_packet = B.read(B.safe_file(self.base.directory, old['field_observations']['file']))
            fields = step_packet['fields']
            B.same(len(fields), 4*count, 'all new four-field source records')
            B.same([{key: value for key, value in row.items() if key != 'local_A'} for row in fields],
                   old_packet['fields'], 'all original four-field records reproduced bitwise')
            steps = step_packet['steps']
            B.same(len(steps), count, 'all individual direct-LD step identities')
            old_full = self.base.step_arrays.all(self.base.stage_arrays[n]['full_states'])
            old_out = self.base.step_arrays.all(self.base.stage_arrays[n]['shape_outputs'])
            for k, step in enumerate(steps):
                self.validate_step_identity(n, k, step, old['schedule'][k],
                    fields[4*k:4*k+4], old_full[k], old_full[k+1], old_out[k], names)
            self.stage_reports[n] = report
            self.stage_arrays[n] = dict(names)
            self.step_report_receipts.append(dict(stage=n, descriptor=descriptor,
                                                  step_count=count))
        B.same(set(self.direct_arrays.arrays), used_names, 'only the complete72 shape/mean array pairs')
        B.same(set(self.metadata_packets), used_packets, 'all complete stage step-evidence packets used')
        total = sum(self.step_counts.values())
        B.same(summary['total_step_count'], total, 'all actual original rawCell0 steps')
        B.same(total, 868, 'actual41 total, not 72 times a guessed12')
        # No allocation or arithmetic on r/base is needed: reuse their exact
        # immutable arrays, including signed zero, and independently rehash.
        self._values = self.base._values
        self.arrays = {name: dict(entry) for name, entry in self.base.arrays.items()
                       if name != 'stage-jacobians'}
        for name, value in self._values.items():
            B.same(hashlib.sha256(B.float_bytes(value)).hexdigest(),
                   self.base.arrays[name]['raw_sha256'], 'unchanged nonlinear data ' + name)
        self.live = dict(stages=[dict(self.original.live['stages'][cell['originalStage']],
            originalStage=cell['originalStage'], newStage=cell['newStage'], expanded_step=cell,
            shape_J_source=('new-direct-longdouble-cast-f64' if cell['originalStage'] in self.selected
                            else 'unchanged-actual28')) for cell in self.cells])
        self.J_rows = []
        full_hash = hashlib.sha256()
        for stage, J in self.stages():
            if not np.isfinite(J).all():
                raise FloatingPointError('Nonfinite complete new Jacobian block ' + str(stage))
            raw = B.float_bytes(J)
            full_hash.update(raw)
            cell = self.cells[stage]
            changed = cell['originalStage'] in self.selected
            if not changed:
                B.same(hashlib.sha256(raw).hexdigest(), self.base.J_rows[stage]['raw_sha256'],
                       'unchanged original504 Jacobian block')
            self.J_rows.append(dict(new_stage=stage, original_stage=cell['originalStage'],
                step_index=cell['stepIndex'], bytes=len(raw), raw_sha256=hashlib.sha256(raw).hexdigest(),
                origin='new-direct-longdouble-cast-f64' if changed else 'unchanged-actual28',
                original41_block_raw_sha256=self.base.J_rows[stage]['raw_sha256']))
        B.same(len(self.J_rows), self.depth, 'every new1372 block')
        self.arrays['stage-jacobians'] = dict(shape=[self.depth, self.K, self.K], dtype='<f8',
            order='C', total_bytes=self.depth*self.K*self.K*8, raw_sha256=full_hash.hexdigest(),
            virtual_stream=True)
        self.binding = dict(schema='native-rawcell0-direct-longdouble-system-binding-v1',
            matrix_scope=MATRIX_SCOPE, adapter_source_sha256=file_sha(__file__),
            frozen_step_binder_sha256=STEP_SHA, original_capture_result_sha256=CAPTURE_SHA,
            actual41_result_sha256=STEP_RESULT_SHA, original1372_matrix_identity_sha256=PARENT_MATRIX_SHA,
            original1372_input_binding=self.base.binding,
            actual_direct_result=dict(file='result.json', bytes=result_path.stat().st_size,
                                      sha256=direct_result_sha256),
            direct_source_sha256=self.source_hashes,
            direct_arithmetic_source=dict(file=DIRECT_ARITHMETIC_NAME, sha256=DIRECT_ARITHMETIC_SHA),
            direct_summary=result['summary'], direct_array_manifest=result['array_manifest'],
            direct_stage_reports=self.step_report_receipts, all_bound_metadata=self.packet_receipts,
            direct_array_raw_sha256={name: row['raw_sha256']
                                    for name, row in self.direct_arrays.arrays.items()},
            direct_verified_chunks=self.direct_arrays.verified_chunks,
            direct_verified_bytes=self.direct_arrays.verified_bytes,
            original_depth=self.original_depth, new_depth=self.depth,
            original_nodes=self.original_depth+1, new_nodes=self.depth+1,
            modes=self.M, shape_dimension=self.K, old_to_new=self.old_to_new, cells=self.cells,
            original_step_counts=[dict(stage=n, step_count=self.step_counts[n]) for n in S.SELECTED],
            new_direct_shape_J_blocks=total, reused_original_stage_J_blocks=504,
            complete_block_manifest=self.J_rows,
            raw_array_sha256={name: row['raw_sha256'] for name, row in self.arrays.items()},
            unchanged_original1372_nonJ_raw_sha256={name: row['raw_sha256']
                                                 for name, row in self.base.arrays.items()
                                                 if name != 'stage-jacobians'},
            new_matrix_is_original_coordinate_binary64=True,
            direct_longdouble_work_is_not_an_exact_reference=True,
            no_G_shadow_or_alternative_target_matrix=True,
            original1372_base_residual_output_sigma_cut_far_H_reused_byte_for_byte=True,
            original226_state_and_geometry_identity_retained_by_producer=True,
            original_schedule_and_final_port_retained=True,
            complete_new_mean_J_preserved_in_input_artifact_but_not_native_shape_equations=True,
            all_original_nonzero_modes_and_equations_retained=True,
            new_rhs_calls_here=0, new_J_calls_here=0, new_ODE_steps_here=0,
            original576_and_original1372_matrix_not_claimed_solved=True,
            no_linear_residual_threshold_added_to_original_nonlinear_acceptance=True,
            final_original_nonlinear_readback_still_required=True,
            no_native_solve_or_trial=True, native_accepted=False, task_completed=False)
        self.binding['new_matrix_identity_sha256'] = canonical_sha(dict(
            adapter_source_sha256=self.binding['adapter_source_sha256'],
            parent1372_identity=PARENT_MATRIX_SHA, direct_result_sha256=direct_result_sha256,
            direct_sources=self.source_hashes, old_to_new=self.old_to_new, cells=self.cells,
            block_manifest=self.J_rows, arrays=self.binding['raw_array_sha256']))

    def verify_descriptor(self, row, label):
        if not isinstance(row, dict):
            raise ValueError('A complete actual file descriptor is required: ' + label)
        name = row['file']
        path = self.B.safe_file(self.directory, name)
        self.B.same(path.stat().st_size, row['bytes'], label + ' byte count')
        self.B.same(file_sha(path), sha_text(row['sha256'], label), label + ' exact bytes')
        receipt = {key: row[key] for key in ('file', 'bytes', 'sha256', 'encoding', 'raw_bytes', 'raw_sha256')
                   if key in row}
        if row.get('encoding') == 'json-gzip':
            h = hashlib.sha256()
            count = 0
            with gzip.open(path, 'rb') as stream:
                for raw in iter(lambda: stream.read(1 << 20), b''):
                    h.update(raw)
                    count += len(raw)
            self.B.same(count, row['raw_bytes'], label + ' complete uncompressed byte count')
            self.B.same(h.hexdigest(), row['raw_sha256'], label + ' complete uncompressed SHA256')
        if name in self.packet_receipts:
            self.B.same(receipt, self.packet_receipts[name], 'unique actual metadata identity')
        self.packet_receipts[name] = receipt
        return path

    def read_descriptor(self, row, label):
        path = self.verify_descriptor(row, label)
        return self.B.read(path)

    def validate_chunk_journal(self, descriptor):
        B = self.B
        path = B.safe_file(self.directory, descriptor['file'])
        B.same(path.stat().st_size, descriptor['bytes'], 'full new chunk journal bytes')
        B.same(file_sha(path), descriptor['sha256'], 'full new chunk journal hash')
        self.packet_receipts[descriptor['file']] = {
            key: descriptor[key] for key in ('file', 'bytes', 'sha256')}
        expected = {(name, row['chunk_index']): row
                    for name, entry in self.direct_arrays.arrays.items() for row in entry['chunks']}
        seen = set()
        next_index = {name: 0 for name in self.direct_arrays.arrays}
        with path.open() as stream:
            for line in stream:
                row = json.loads(line)
                key = (row['array'], row['chunk_index'])
                if key in seen or key not in expected:
                    raise ValueError('Duplicate or unlisted new complete matrix chunk')
                B.same(row, expected[key], 'complete new chunk descriptor')
                B.same(row['chunk_index'], next_index[row['array']], 'per-array streamed chunk order')
                next_index[row['array']] += 1
                seen.add(key)
        B.same(seen, set(expected), 'every completed new chunk exactly once')

    def validate_step_identity(self, n, k, step, original_schedule,
                               fields, full_input, full_output, shape_output, names):
        """Source identity checks, never a numerical-nearness acceptance gate."""
        if isinstance(step, dict) and {'file', 'bytes', 'sha256'} <= step.keys():
            step = self.read_descriptor(step, 'individual direct-LD step identity')
        B = self.B
        B.same(step['original_stage'], n, 'direct-LD original stage')
        B.same(step['original_step'], k, 'direct-LD original step')
        B.same(step['schedule'], original_schedule, 'direct-LD original complete schedule')
        for key in ('same_original_full_input_bits', 'same_four_field_states_bits',
                    'same_four_geometry_records', 'same_original_h_bits',
                    'original_port_applied_only_at_final_step', 'same_four_root_records',
                    'same_original_full_output_bits', 'same_original_shape_output_bits'):
            B.same(step.get(key), True, 'same finite base identity ' + key)
        rows = step['local_A_sha256']
        B.same(len(rows), 4, 'all four newly observed original local derivative arrays')
        for value in rows:
            sha_text(value, 'complete local226x224 derivative bytes')
        B.same(step['four_field_bindings'], [row['local_A'] for row in fields],
               'all full local-A source descriptors')
        B.same(rows, [row['local_A']['sha256'] for row in fields], 'complete four local-A hash aliases')
        for key, value in (('full_input_sha256', full_input), ('full_output_sha256', full_output),
                           ('shape_output_sha256', shape_output)):
            B.same(step[key], hashlib.sha256(B.float_bytes(value)).hexdigest(),
                   'same actual41 per-step raw bytes ' + key)
        for field_index, row in enumerate(fields):
            binding = row['local_A']
            B.same((binding['field_index'], binding['shape'], binding['dtype'], binding['order'], binding['bytes']),
                   (field_index, [226, 224], '<f8', 'C', 226*224*8), 'complete source local-A dimensions')
            B.same(binding['original_full_state_sha256'], row['state_float64le_sha256'],
                   'local-A original full-state identity')
            B.same(binding['observed_full_state_sha256'], row['state_float64le_sha256'],
                   'local-A observed full-state identity')
            for first, second in (('original_geometry_sha256', 'observed_geometry_sha256'),
                                  ('original_field_record_sha256', 'observed_field_record_sha256')):
                B.same(binding[first], binding[second], 'same actual field descriptor ' + first)
        reply = step['worker_reply']
        B.same((reply['event'], reply['stage'], reply['original_step']),
               ('step-completed', n, k), 'same completed direct worker operation')
        B.same(reply['local_A'], step['four_field_bindings'], 'worker exact four local-A operands')
        B.same(reply['source_sha256'], self.result['worker_source_sha256'], 'same original worker bytes')
        B.same(reply['direct_arithmetic_source_sha256'], DIRECT_ARITHMETIC_SHA,
               'same actual50 direct arithmetic path')
        B.same(reply['original_h'], original_schedule['h'], 'worker original h bit record')
        B.same(reply['original_port_ratio'], original_schedule['port_ratio'], 'worker unique original port')
        B.same(reply['full_input_sha256'], step['full_input_sha256'], 'worker original input bytes')
        for key in ('once_cast_to_binary64', 'original_Pi_port_paid_once', 'two_mean_rows_retained',
                    'same_unchanged_actual50_direct_rk_function'):
            B.same(reply[key], True, 'complete new target definition ' + key)
        B.same(reply['mean_feedback_into_shape'], False, 'no mean feedback in original shape tangent')
        combined = hashlib.sha256()
        total_bytes = 0
        for role in ('shape_jacobians', 'mean_jacobians'):
            entry = self.direct_arrays.arrays[names[role]]
            chunks = [row for row in entry['chunks'] if row['row_start'] == k and row['row_stop'] == k+1]
            B.same(len(chunks), 1, 'one complete new original step chunk')
            descriptor = reply['arrays'][role]
            for key in ('file', 'bytes', 'sha256', 'raw_sha256'):
                B.same(descriptor[key], chunks[0][key], 'worker/manifest target chunk ' + key)
            B.same(descriptor['shape'], [1, *entry['shape'][1:]], 'worker whole target shape')
            B.same((descriptor['dtype'], descriptor['order']), ('<f8', 'C'), 'worker complete binary64 target')
            raw = B.safe_file(self.directory, descriptor['file']).read_bytes()
            combined.update(raw)
            total_bytes += len(raw)
        B.same(total_bytes, reply['full_original_output_bytes'], 'all226 output rows retained')
        B.same(combined.hexdigest(), reply['full_original_output_sha256'],
               'shape and mean belong to the same once-cast full map')

    def all(self, name):
        return self.base.all(name)

    def raw(self, name):
        return self.base.raw(name)

    def stages(self):
        expected = 0
        for old, J in self.original.stages():
            if old in self.selected:
                blocks = self.direct_arrays.all(self.stage_arrays[old]['shape_jacobians'])
                for k in range(self.step_counts[old]-1, -1, -1):
                    cell = self.cells[expected]
                    self.B.same((cell['originalStage'], cell['stepIndex']), (old, k),
                                'direct-LD inner-to-outer rows reversed to shooting order')
                    yield expected, blocks[k]
                    expected += 1
            else:
                self.B.same(self.cells[expected]['originalStage'], old,
                            'unchanged actual28 stage order')
                yield expected, J
                expected += 1
        self.B.same(expected, self.depth, 'complete new1372 Jacobian stream')

    def stage_bytes(self):
        for stage, J in self.stages():
            raw = self.B.float_bytes(J)
            self.B.same(hashlib.sha256(raw).hexdigest(), self.J_rows[stage]['raw_sha256'],
                        'reread new full original-coordinate Jacobian block')
            yield stage, raw

    def stage_raw(self, stage):
        if not 0 <= stage < self.depth:
            raise ValueError('Stage outside the complete new system')
        cell = self.cells[stage]
        old = cell['originalStage']
        if old in self.selected:
            array = self.direct_arrays.row(self.stage_arrays[old]['shape_jacobians'], cell['stepIndex'])
            raw = self.B.float_bytes(array)
        else:
            raw = self.base.stage_raw(stage)
        self.B.same(hashlib.sha256(raw).hexdigest(), self.J_rows[stage]['raw_sha256'],
                    'exact witness new full Jacobian bytes')
        return raw

    def export_inputs(self, output):
        return {name: output.save('direct-system-' + name, value,
            'Unchanged actual41 complete nonlinear base array; new868 J is an independently bound virtual stream')
            for name, value in self._values.items()}


class DynamicExactContext:
    """Frozen exact dyadic row kernel, with this matrix's scope and identity."""
    def __init__(self, system, kernel):
        self.system = system
        self.kernel = kernel
        self.inner = system.S.DynamicExactContext(system, kernel)

    def __getattr__(self, name):
        return getattr(self.inner, name)

    def max_record(self, kind, node, row, value, sigma_word):
        result = self.inner.max_record(kind, node, row, value, sigma_word)
        result['matrix_scope'] = MATRIX_SCOPE
        result['original1372_matrix_identity_sha256'] = PARENT_MATRIX_SHA
        return result

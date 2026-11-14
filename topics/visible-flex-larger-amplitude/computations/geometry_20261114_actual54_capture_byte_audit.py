#!/usr/bin/env python3
"""Byte/metadata audit of completed actual54 capture. No scientific source imports."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import struct

RESULT_SHA = 'e60da64312819a87388cfa96c209fc9188dca02c0ab055cbcc934f3507888ac6'
OLD_RESULT_SHA = '6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf'
PINS = dict(
    source_sha256='a63ffda643044787cb0ad5fb0d7c2aa4e4b34090fefa4b9053f4f2550bf85dbf',
    hook_sha256='3499f7abb96a4f25c4c3a986d97dc8aea3b21742770aabe7abe2822ad8b3caf4',
    window_module_sha256='1ba3f30702b26aa78b4aceb0b2d3d5d71ea8fa858b114d982ead185330faa5d9',
    worker_source_sha256='87ab92d9234d6e58103d44d125ce5510f9cde34ac37df251b7e63dcb6747a9c8',
    direct_arithmetic_source_sha256='01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def need(value, message):
    if not value:
        raise ValueError(message)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory', type=Path, required=True)
    p.add_argument('--original41', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    directory, old = a.directory.resolve(), a.original41.resolve()
    files = {}
    raw_array_bytes = chunks_verified = original_state_bytes = 0

    def read_file(root, relative, size=None, digest=None):
        rel = Path(relative)
        f = (root/rel).resolve()
        need(not rel.is_absolute() and '..' not in rel.parts and f.is_relative_to(root), 'Bound relative path')
        raw = f.read_bytes()
        actual = sha(raw)
        need(size is None or len(raw) == size, 'File size: '+relative)
        need(digest is None or actual == digest, 'File hash: '+relative)
        key = ('capture/' if root == directory else 'actual41/')+relative
        receipt = dict(file=key, bytes=len(raw), sha256=actual)
        need(key not in files or files[key] == receipt, 'Repeated file identity')
        files[key] = receipt
        return raw

    def desc(root, row, parsed=False):
        digest = row['sha256'] if 'sha256' in row else row['raw_sha256']
        raw = read_file(root, row['file'], row['bytes'], digest)
        if 'sha256' in row and 'raw_sha256' in row and not ('raw_bytes' in row):
            need(row['sha256'] == row['raw_sha256'], 'Raw binary descriptor aliases')
        if parsed:
            unpacked = gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw
            if 'raw_bytes' in row:
                need(len(unpacked) == row['raw_bytes'] and sha(unpacked) == row['raw_sha256'], 'Complete gzip packet')
            return json.loads(unpacked)
        return raw

    def get_json(root, relative, digest=None):
        raw = read_file(root, relative, digest=digest)
        return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)

    result = get_json(directory, 'result.json', RESULT_SHA)
    need(result['completed'] is True and result['capture_completed'] is True, 'Completed actual54 capture')
    need(result['planned_probe_stop_observed'] is True and result['original_protocol_requests'] == 1 and
         result['worker_exit_code'] == 0 and result['native_accepted'] is False, 'Original planned STOP scope')
    for key, value in PINS.items():
        need(result[key] == value, 'Actual54 source pin '+key)
    for row in result['small_output_files']:
        desc(directory, row)
    summary = desc(directory, result['summary'], True)
    need(result['capture_summary_sha256'] == result['summary']['sha256'], 'Summary alias')
    manifest = desc(directory, result['array_manifest'], True)
    need(summary['array_manifest'] == result['array_manifest'], 'Summary manifest identity')
    need(manifest['completed'] is True and manifest['schema'] == 'native-rawcell0-direct-longdouble-output-arrays-v1', 'Completed new manifest')
    for obj in (summary, manifest):
        for key, value in PINS.items():
            need(obj[key] == value, 'All complete metadata source pins')
        need(obj['actual41_result_sha256'] == OLD_RESULT_SHA, 'Exact original41 parent')
    need(summary['completed_original_stages'] == list(range(72)), 'All72 original stages')
    spec = desc(directory, result['specification'], True)
    need(result['spec_sha256'] == result['specification']['sha256'] == summary['spec_sha256'] == manifest['spec_sha256'], 'Stored compressed specification SHA')
    for key, value in PINS.items():
        need(spec[key] == value, 'Complete decompressed specification source')
    refs = desc(directory, result['actual41_input_references'], True)
    need(refs == spec['step_references'], 'Complete specification references alias')

    old_result = get_json(old, 'result.json', OLD_RESULT_SHA)
    old_small = {row['file']: row for row in old_result['small_output_files']}
    old_summary = desc(old, old_small['rawcell0-step-summary.json'], True)
    old_manifest = desc(old, old_result['array_manifest'], True)
    old_arrays = {row['name']: row for row in old_manifest['arrays']}
    old_packets = {row['file']: row for row in old_manifest['metadata_packets']}
    new_arrays = {row['name']: row for row in manifest['arrays']}
    new_packets = {row['file']: row for row in manifest['metadata_packets']}
    need(len(new_arrays) == len(manifest['arrays']) == 144, 'Unique144 target arrays')
    need(len(new_packets) == len(manifest['metadata_packets']) == 72, 'Unique72 complete field/step packets')

    expected_ledger = {}
    for entry in manifest['arrays']:
        for row in entry['chunks']:
            key = (row['array'], row['chunk_index'])
            need(key not in expected_ledger, 'Unique chunk identifier')
            expected_ledger[key] = row
    ledger = desc(directory, manifest['chunk_ledger'])
    actual_ledger = {}
    for line in ledger.splitlines():
        row = json.loads(line)
        key = (row['array'], row['chunk_index'])
        need(key not in actual_ledger, 'Unique interleaved journal row')
        actual_ledger[key] = row
    need(actual_ledger == expected_ledger, 'Full actual interleaved chunk journal')

    def array(root, entry, shape):
        nonlocal raw_array_bytes, chunks_verified, original_state_bytes
        need(entry['dtype'] == '<f8' and entry['order'] == 'C' and entry['completed'] is True and entry['shape'] == shape,
             'Complete array shape/type')
        width = 8
        for n in shape[1:]:
            width *= n
        cursor = 0
        all_raw = []
        for index, row in enumerate(entry['chunks']):
            need(row['array'] == entry['name'] and row['chunk_index'] == index and row['row_start'] == cursor and row['row_stop'] > cursor,
                 'Complete ordered array chunks')
            raw = desc(root, row)
            need(len(raw) == width*(row['row_stop']-cursor), 'Chunk byte shape')
            all_raw.append(raw)
            cursor = row['row_stop']
            if root == directory:
                chunks_verified += 1
        joined = b''.join(all_raw)
        need(cursor == shape[0] and len(joined) == entry['total_bytes'] and sha(joined) == entry['raw_sha256'], 'Full original array word stream')
        if root == directory:
            raw_array_bytes += len(joined)
        else:
            original_state_bytes += len(joined)
        return joined

    seen_arrays = set()
    stage_records = []
    total_steps = total_fields = negative_zero_words = 0
    reported_cast_to_zero = 0
    complete_shape_stream = hashlib.sha256()
    complete_mean_stream = hashlib.sha256()
    native_field_stream = hashlib.sha256()
    for n in range(72):
        row = summary['stage_reports'][n]
        need(result['stage_reports'][n] == row, 'Result/summary complete report alias')
        report = desc(directory, row, True)
        original = desc(old, report['original_report'], True)
        need(report['original_report'] == old_summary['stage_reports'][n], 'Actual41 same stage report descriptor')
        count = report['step_count']
        need(report['stage'] == report['original_stage'] == original['stage'] == n and count == original['step_count'], 'Same actual stage/step count')
        need(report['schedule'] == original['schedule'] and report['profile_schedules'] == original['profile_schedules'], 'All original schedule records/float64 bit fields')
        desc(directory, report['identity'], True)
        desc(old, report['actual41_window'], True)
        need(report['actual41_window'] == original['identity'], 'Original window descriptor')
        packet_row = report['direct_ld_step_reports']
        need(new_packets[packet_row['file']] == packet_row, 'New field packet manifest descriptor')
        packet = desc(directory, packet_row, True)
        original_packet_row = report['actual41_field_packet']
        need(old_packets[original_packet_row['file']] == original_packet_row == original['field_observations'], 'Original field packet descriptor')
        original_packet = desc(old, original_packet_row, True)
        need(packet['completed'] is True and packet['partial'] is False and packet['original_stage'] == n and
             len(packet['steps']) == count and len(packet['fields']) == 4*count, 'Complete original step and field observations')
        need(original_packet['partial'] is False and len(original_packet['fields']) == 4*count, 'Complete old field observations')
        for key in ('source_sha256','hook_sha256','window_module_sha256','worker_source_sha256'):
            need(packet[key] == PINS[key], 'Packet producer pin')
        full_entry = old_arrays[original['arrays']['full_states']]
        shape_entry = old_arrays[original['arrays']['shape_outputs']]
        need(report['actual41_full_states_raw_sha256'] == full_entry['raw_sha256'] and
             report['actual41_shape_outputs_raw_sha256'] == shape_entry['raw_sha256'], 'Old state/output identity')
        full_states = array(old, full_entry, [count+1,226])
        shape_outputs = array(old, shape_entry, [count,224])
        J_entry = new_arrays[report['arrays']['shape_jacobians']]
        mean_entry = new_arrays[report['arrays']['mean_jacobians']]
        seen_arrays.update((J_entry['name'], mean_entry['name']))
        J = array(directory, J_entry, [count,224,224])
        means = array(directory, mean_entry, [count,2,224])
        for k, step in enumerate(packet['steps']):
            schedule = original['schedule'][k]
            need(step['original_stage'] == n and step['original_step'] == k and step['schedule'] == schedule, 'Exact original per-step schedule')
            for key in ('same_original_full_input_bits','same_four_field_states_bits','same_four_geometry_records',
                        'same_original_h_bits','original_port_applied_only_at_final_step','same_four_root_records',
                        'same_original_full_output_bits','same_original_shape_output_bits'):
                need(step[key] is True, 'Actual completed source identity flag')
            need(step['full_input_sha256'] == sha(full_states[k*1808:(k+1)*1808]), 'Full226 original input bytes')
            need(step['full_output_sha256'] == sha(full_states[(k+1)*1808:(k+2)*1808]), 'Full226 original output bytes')
            need(step['shape_output_sha256'] == sha(shape_outputs[k*1792:(k+1)*1792]), 'Original post-port shape output bytes')
            local = []
            for j in range(4):
                field = packet['fields'][4*k+j]
                original_field = original_packet['fields'][4*k+j]
                copied = {key: value for key, value in field.items() if key != 'local_A'}
                need(copied == original_field, 'Every original field/state/geometry/root numberRecord and bit string')
                A = field['local_A']
                need(A['field_index'] == j and A['shape'] == [226,224] and A['dtype'] == '<f8' and
                     A['order'] == 'C' and A['bytes'] == 404992 and A['sha256'] == A['raw_sha256'], 'Complete captured local-A descriptor')
                need(A['original_full_state_sha256'] == A['observed_full_state_sha256'] == original_field['state_float64le_sha256'], 'Local-A same original state identity')
                need(A['original_geometry_sha256'] == A['observed_geometry_sha256'] and
                     A['original_field_record_sha256'] == A['observed_field_record_sha256'], 'Original/observed metadata hash aliases')
                local.append(A)
                native_field_stream.update(bytes.fromhex(A['sha256']))
            need(step['four_field_bindings'] == local and step['local_A_sha256'] == [x['sha256'] for x in local], 'All four independent source descriptors')
            reply = step['worker_reply']
            need(reply['sequence'] == total_steps and reply['stage'] == n and reply['original_step'] == k and
                 reply['local_A'] == local and reply['source_sha256'] == PINS['worker_source_sha256'], 'Persistent worker full step identity')
            need(reply['direct_arithmetic_source_sha256'] == PINS['direct_arithmetic_source_sha256'] and
                 reply['original_h'] == schedule['h'] and reply['original_port_ratio'] == schedule['port_ratio'], 'Unchanged direct helper and original h/port bits')
            need(reply['full_input_sha256'] == step['full_input_sha256'] and
                 reply['actual41_field_record_sha256'] == [x['original_field_record_sha256'] for x in local], 'Worker input field aliases')
            rawJ = J[k*401408:(k+1)*401408]
            rawMean = means[k*3584:(k+1)*3584]
            for role, raw, expected_shape, entry in (
                ('shape_jacobians',rawJ,[1,224,224],J_entry),
                ('mean_jacobians',rawMean,[1,2,224],mean_entry)):
                d = reply['arrays'][role]
                c = entry['chunks'][k]
                need(c['row_start'] == k and c['row_stop'] == k+1 and c['file'] == d['file'], 'Worker/manifest full row alias')
                need(d['bytes'] == len(raw) and d['sha256'] == d['raw_sha256'] == sha(raw) and
                     d['dtype'] == '<f8' and d['order'] == 'C' and d['shape'] == expected_shape, 'Worker exact saved target bytes')
            full = rawJ+rawMean
            need(reply['full_original_output_bytes'] == len(full) == 404992 and reply['full_original_output_sha256'] == sha(full), 'All226 final map rows')
            minus_zeros = 0
            for (bits,) in struct.iter_unpack('<Q',full):
                need(((bits >> 52) & 2047) != 2047, 'Stored target finite binary64 word')
                if bits == (1 << 63):
                    minus_zeros += 1
            need(reply['output_negative_zero_entries'] == minus_zeros, 'Signed-zero word count')
            for key in ('once_cast_to_binary64','original_Pi_port_paid_once','two_mean_rows_retained','same_unchanged_actual50_direct_rk_function'):
                need(reply[key] is True, 'Worker returned complete map contract')
            need(reply['mean_feedback_into_shape'] is False, 'Mean feedback scope')
            complete_shape_stream.update(rawJ)
            complete_mean_stream.update(rawMean)
            negative_zero_words += minus_zeros
            reported_cast_to_zero += reply['working_nonzero_to_binary64_zero_entries']
            total_steps += 1
            total_fields += 4
        stage_records.append(dict(stage=n,steps=count,report_sha256=row['sha256'],
            packet_sha256=packet_row['sha256'],packet_raw_sha256=packet_row['raw_sha256'],
            shape_array_raw_sha256=J_entry['raw_sha256'],mean_array_raw_sha256=mean_entry['raw_sha256'],
            original_full_states_raw_sha256=full_entry['raw_sha256'],original_shape_outputs_raw_sha256=shape_entry['raw_sha256']))
    need(seen_arrays == set(new_arrays), 'No omitted or extra target arrays')
    need(total_steps == 868 == summary['total_step_count'] == result['completed_local_J_blocks'], 'All868 saved maps')
    need(total_fields == 3472 == summary['completed_original_RK_field_calls'] == result['original_RK_field_entries'], 'All3472 field observations')
    worker_summary = desc(directory, result['direct_ld_worker_summary'], True)
    need(worker_summary['completed_steps'] == 868 and worker_summary['exit_code'] == 0 and worker_summary['spec_sha256'] == result['spec_sha256'], 'Worker completed once')
    ready = get_json(directory, 'direct-ld-worker-ready.json')
    need(ready['runtime']['working_precision'] == result['working_precision'] == summary['working_precision'], 'Actual declared working representation')
    need(ready['spec_sha256'] == result['spec_sha256'], 'Both readers use stored compressed spec hash')
    record = dict(schema='actual54-complete868-capture-byte-and-metadata-audit-v1',audit_passed=True,
        scope='SHA, gzip, complete raw words, descriptors and old/new saved metadata only; no RHS/J/RK/solve/norm or scientific-source import',
        public_run='43634889730',result_sha256=RESULT_SHA,summary=result['summary'],array_manifest=result['array_manifest'],
        specification=result['specification'],source_pins=PINS,
        complete_original_stages=72,total_steps=total_steps,total_fields=total_fields,target_arrays=len(new_arrays),
        binary_chunks=chunks_verified,target_array_bytes=raw_array_bytes,
        target_binary64_words=raw_array_bytes//8,negative_zero_words=negative_zero_words,
        original41_consumed_state_and_output_bytes=original_state_bytes,
        complete_raw_shape_stream_sha256=complete_shape_stream.hexdigest(),
        complete_raw_mean_stream_sha256=complete_mean_stream.hexdigest(),
        ordered_local_A_hash_words_sha256=native_field_stream.hexdigest(),
        local_A_raw_not_saved_and_not_independently_recomputed=True,
        full3472_saved_field_records_equal_actual41_excluding_new_local_A_descriptors=True,
        original_saved_full226_states_outputs_and_single_exit_ports_equal=True,
        interleaved_journal_fully_matches_manifest=True,
        reported_working_nonzero_to_binary64_zero_entries_total=reported_cast_to_zero,
        cast_loss_total_is_sum_of_actual_worker_metadata_not_recomputed=True,
        declared_working_precision=result['working_precision'],working_arrays_not_persisted_no_independent_x87_padding_claim=True,
        capture_elapsed_seconds=result['elapsed_seconds'],hook_elapsed_seconds=summary['elapsed_seconds'],
        worker_report=worker_summary,stage_records=stage_records,
        verified_files_count=len(files),verified_files=list(files.values()),
        native_accepted=False,task_completed=False)
    a.out.write_text(json.dumps(record,sort_keys=True,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ('verified_files','stage_records','source_pins','worker_report')},sort_keys=True))


if __name__ == '__main__':
    main()

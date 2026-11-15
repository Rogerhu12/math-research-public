#!/usr/bin/env python3
"""One complete public actual73 fetch, original packet export, then frozen byte audit.

Only standard-library byte and metadata operations are performed here. The
unaltered c062 reader owns its complete audit. The R276 scientific calculation
is a separate subsequent Actions step, using the same immutable extraction.
No numerical producer, array package, kernel, QR or scientific action is loaded.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import traceback
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
REPOSITORY = 'Rogerhu12/math-research-public'
READER = 'exact_20261115_read_noj_primal_current576_artifact.py'
READER_SHA = 'c062117765addc2acf7b82ca1aa6ad87027ebab8d32c75673af382d24dd26f06'
NATIVE = 'native-noj-primal-current576-damped'
SOURCE_COMMIT = '9515d5aaf7c68f8efd366438d6bd81ce73c3486f'
PIN = {
    'run_id': 43657001633,
    'artifact_id': 14141540502,
    'artifact_name': 'visible-mainline-nojprimalnative-43657001633-1',
    'expected_size': 1752742419,
    'expected_sha256': '3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9',
}
ROOT_PACKETS = (
    'noj-primal-current576-request-identity.json',
    'native-noj-primal-current576-damped.log',
    'rule-sync/runner-result.json',
)
NATIVE_PACKETS = (
    'result.json', 'current-correction-summary.json', 'current-corrections.jsonl',
    'native_trace.jsonl', 'native_trials.jsonl', 'native_stderr.log',
    'native_0001.json.gz', 'native_iteration.json.gz',
)
ITERATION_PACKETS = (
    'qr-launch.json', 'qr-exit.json', 'qr.stdout.log', 'qr.stderr.log',
    'returned-correction.json', 'bridge-failure.json', 'qr/summary.json',
    'snapshot/result.json', 'snapshot/context.json', 'snapshot/context.json.gz',
)
CHUNK = 1024 * 1024


def require(condition, text):
    if not condition:
        raise ValueError(text)


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(CHUNK), b''):
            h.update(block)
    return h.hexdigest()


def packet_info(path, relative):
    return dict(file=relative, bytes=path.stat().st_size, sha256=file_sha(path))


def write_json(directory, name, value, compressed=False):
    path = directory / name
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()
    payload = gzip.compress(raw, compresslevel=9, mtime=0) if compressed else raw
    with path.open('xb') as stream:
        stream.write(payload)
    return dict(file=name, bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest(),
                raw_bytes=len(raw), raw_sha256=hashlib.sha256(raw).hexdigest())


def read_json(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def load_frozen_reader():
    path = HERE / READER
    require(file_sha(path) == READER_SHA, 'Use the unmodified frozen actual73 byte reader')
    spec = importlib.util.spec_from_file_location('_actual73_complete_byte_reader', path)
    require(spec is not None and spec.loader is not None, 'Frozen byte reader loader')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    require(module.ORIGINAL_RUN == PIN['run_id'] and module.ORIGINAL_COMMIT == SOURCE_COMMIT
            and module.NATIVE_DIRECTORY == NATIVE, 'Original actual73 reader scope')
    return module


def copy_packet(root, output, relative):
    source = root / relative
    require(source.is_file() and not source.is_symlink(), 'Existing regular original packet: ' + relative)
    require(source.resolve().is_relative_to(root.resolve()), 'Original packet stays inside verified extraction')
    target = output / 'large-arrays/original-native-packets' / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    before = source.stat()
    h = hashlib.sha256()
    count = 0
    with source.open('rb') as incoming, target.open('xb') as outgoing:
        for block in iter(lambda: incoming.read(CHUNK), b''):
            outgoing.write(block)
            h.update(block)
            count += len(block)
    after = source.stat()
    require((before.st_size, before.st_mtime_ns) == (after.st_size, after.st_mtime_ns)
            and count == before.st_size, 'Original packet was immutable while copied')
    digest = h.hexdigest()
    require(target.stat().st_size == count and file_sha(target) == digest, 'Complete packet copy preserves every byte')
    return dict(original_file=relative, bytes=count, sha256=digest,
                copied_file=target.relative_to(output).as_posix(),
                original_compressed_bytes_preserved=source.suffix == '.gz')


def export_original_packets(root, output):
    """Export original bytes first; neither infer success nor require a final result."""
    relative_names = list(ROOT_PACKETS)
    relative_names.extend(NATIVE + '/' + name for name in NATIVE_PACKETS)
    native = root / NATIVE
    actual_iteration_directories = []
    if native.is_dir():
        for path in sorted(native.iterdir(), key=lambda item: item.name):
            if not re.fullmatch(r'iteration-[0-9]+', path.name):
                continue
            require(path.is_dir() and not path.is_symlink(), 'Actual iteration directory is a regular directory')
            actual_iteration_directories.append(path.name)
            relative_names.extend(NATIVE + '/' + path.name + '/' + name for name in ITERATION_PACKETS)
    copied, absent = [], []
    for relative in relative_names:
        if (root / relative).exists():
            copied.append(copy_packet(root, output, relative))
        else:
            absent.append(relative)
    complete = write_json(output, 'large-arrays/original-native-packet-manifest.json.gz', dict(
        schema='actual73-original-scalar-and-journal-packet-export-v1', original_artifact=PIN,
        original_source_commit=SOURCE_COMMIT, copied_files=copied, absent_files=absent,
        actual_iteration_directories=actual_iteration_directories,
        bytes_copied_without_reformatting=True, mathematical_computation_performed=False,
        original_full_trial_arrays_not_invented=True), compressed=True)
    result_path = native / 'result.json'
    status = dict(original_result_present=result_path.is_file())
    if result_path.is_file():
        try:
            outer = read_json(result_path)
            keys = ('schema', 'native_accepted', 'actual_original_failure_message', 'actual_error',
                    'original_tolerance', 'original_max_iterations', 'fresh_withJ_snapshots',
                    'current_R273_directions_returned', 'requested_full_DN_Jacobian',
                    'requested_full_finite_audit', 'full_J_returned', 'full_audit_returned')
            status['original_fields'] = {key: outer[key] for key in keys if key in outer}
            status['original_result'] = packet_info(result_path, NATIVE + '/result.json')
            if 'current_correction_summary' in outer:
                status['original_correction_summary_descriptor'] = outer['current_correction_summary']
        except Exception as error:
            status['original_result_decode_error'] = repr(error)
    summary = dict(schema='actual73-original-packets-before-byte-audit-v1', original_artifact=PIN,
        original_source_commit=SOURCE_COMMIT, **status, packet_count=len(copied),
        original_iteration_directory_names=actual_iteration_directories,
        complete_original_packet_manifest=complete,
        original_result_and_journals_exported_before_complete_byte_audit=True,
        original_compressed_packets_not_reserialized=True,
        mathematical_computation_performed=False, scientific_success_inferred=False,
        original_outcome_not_changed_by_audit_or_future_R276=True)
    descriptor = write_json(output, 'original-native-packets-before-audit.json', summary)
    print(json.dumps(dict(event='actual73_original_packets_preserved',
        packet_count=len(copied), original_result_present=result_path.is_file(),
        original_fields=status.get('original_fields'), summary=descriptor), allow_nan=False), flush=True)
    return descriptor


def main():
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPOSITORY,
            'Run only in the authorized public Actions repository')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', type=Path, required=True)
    parser.add_argument('--download-out', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    request = json.loads(args.request.read_bytes())
    require(request.get('repository') == REPOSITORY and request.get('readback_kind') == 'native73'
            and request.get('original_request_number') == 73
            and request.get('original_artifact') == PIN
            and request.get('original_source_commit') == SOURCE_COMMIT,
            'Use the exact completed actual73 artifact tuple')
    require(request.get('source_sha256', {}).get(READER) == READER_SHA
            and request.get('source_sha256', {}).get(Path(__file__).name) == file_sha(__file__),
            'The request pins both original reader and this independent packet exporter')
    download_out, out = args.download_out.resolve(), args.out.resolve()
    require(not os.path.lexists(args.download_out) and not os.path.lexists(args.out)
            and not out.is_relative_to(download_out) and not download_out.is_relative_to(out),
            'Independent new complete extraction and report directories')
    out.mkdir(parents=True)
    actual = SimpleNamespace(**PIN, source_commit=SOURCE_COMMIT, download_out=download_out, out=out)
    result = dict(schema='actual73-original-fetch-export-and-byte-audit-route-v1',
        source_sha256=file_sha(__file__), reader_sha256=READER_SHA,
        original_artifact=PIN, original_source_commit=SOURCE_COMMIT,
        original_extraction_completed=False, original_packets_exported=False,
        mathematical_computation_performed=False, R276_not_called_by_this_step=True)
    code = 2
    try:
        reader = load_frozen_reader()
        root, transport, name = reader.fetch_original(actual)
        result['original_extraction_completed'] = True
        result['transport_receipt'] = packet_info(root / name, name)
        # These copied primary files remain available if any deeper byte check fails.
        result['original_packets'] = export_original_packets(root, out)
        result['original_packets_exported'] = True
        utilities = reader.load_byte_module(reader.UTILITY_NAME, reader.UTILITY_SHA, '_current576_byte_utilities')
        code = reader.run_reader(actual, utilities, root, transport, name)
        result['original_byte_reader_returncode'] = code
    except Exception as error:
        result['actual_readback_error'] = repr(error)
        result['traceback'] = traceback.format_exc()
        print(json.dumps(dict(event='actual73_readback_route_failed', error=repr(error))), flush=True)
    finally:
        result['original_and_partial_outputs_not_removed'] = True
        write_json(out, 'actual73-packet-route-result.json', result)
    return code


if __name__ == '__main__':
    raise SystemExit(main())

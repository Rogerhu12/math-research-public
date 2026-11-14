#!/usr/bin/env python3
"""Restore original gzip chunk bytes from a shared exact DEFLATE payload.

Raw checkpoint files have different gzip filename/time headers even when
their complete NPY payloads are identical. This storage helper reuses a
prior archived compressed payload only if both uncompressed bytes and the
raw DEFLATE stream agree exactly. The target's original header/trailer and
full SHA-256 restore its exact original file, without changing raw metadata,
numerical arrays, primary hashes, solver state or mathematical acceptance.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
from pathlib import Path
import struct
import zlib

SCHEMA = 'exact-original-gzip-header-payload-recovery-v1'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def split_member(data):
    if len(data) < 18 or data[:3] != b'\x1f\x8b\x08' or data[3] & 0xe0:
        raise ValueError('Expected one ordinary DEFLATE gzip member')
    flags, offset = data[3], 10
    if flags & 4:
        if len(data) < offset+2:
            raise ValueError('Truncated gzip extra header')
        length = struct.unpack('<H', data[offset:offset+2])[0]
        offset += 2+length
    for flag in (8, 16):
        if flags & flag:
            offset = data.index(b'\0', offset)+1
    if flags & 2:
        if len(data) < offset+2 or struct.unpack('<H', data[offset:offset+2])[0] != zlib.crc32(data[:offset]) & 0xffff:
            raise ValueError('The gzip header checksum differs')
        offset += 2
    if offset > len(data)-8:
        raise ValueError('The gzip header overruns its payload')
    inflater = zlib.decompressobj(-zlib.MAX_WBITS)
    raw = inflater.decompress(data[offset:])+inflater.flush()
    if not inflater.eof or inflater.unconsumed_tail or len(inflater.unused_data) != 8:
        raise ValueError('Exactly one complete gzip member is required')
    crc, size = struct.unpack('<II', inflater.unused_data)
    if crc != zlib.crc32(raw) & 0xffffffff or size != len(raw) & 0xffffffff:
        raise ValueError('The original gzip payload checksum/size differs')
    return data[:offset], data[offset:-8], data[-8:], raw


def make_recipe(source_bytes, target_bytes, source_file, target_file):
    source_header, source_payload, source_trailer, source_raw = split_member(source_bytes)
    target_header, target_payload, target_trailer, target_raw = split_member(target_bytes)
    if source_raw != target_raw or source_payload != target_payload:
        return None
    record = dict(source_file=source_file, source_sha256=sha(source_bytes),
        source_bytes=len(source_bytes), target_file=target_file,
        target_sha256=sha(target_bytes), target_bytes=len(target_bytes),
        uncompressed_sha256=sha(target_raw), uncompressed_bytes=len(target_raw),
        shared_deflate_sha256=sha(target_payload), shared_deflate_bytes=len(target_payload),
        target_original_header_base64=base64.b64encode(target_header).decode('ascii'),
        target_original_trailer_base64=base64.b64encode(target_trailer).decode('ascii'),
        original_uncompressed_bytes_equal=True, original_deflate_bytes_equal=True)
    if restore_bytes(record, source_bytes) != target_bytes:
        raise ValueError('The original target did not reconstruct byte-for-byte')
    record['actual_reconstructed_target_bitwise_equal'] = True
    return record


def restore_bytes(record, source_bytes):
    if len(source_bytes) != record['source_bytes'] or sha(source_bytes) != record['source_sha256']:
        raise ValueError('The exact archived source gzip chunk differs')
    _, payload, _, raw = split_member(source_bytes)
    if (len(payload) != record['shared_deflate_bytes'] or
            sha(payload) != record['shared_deflate_sha256'] or
            len(raw) != record['uncompressed_bytes'] or
            sha(raw) != record['uncompressed_sha256']):
        raise ValueError('The complete shared compressed/uncompressed bytes differ')
    result = (base64.b64decode(record['target_original_header_base64'], validate=True)+payload+
              base64.b64decode(record['target_original_trailer_base64'], validate=True))
    if len(result) != record['target_bytes'] or sha(result) != record['target_sha256']:
        raise ValueError('The exact original target gzip identity differs')
    if split_member(result)[3] != raw:
        raise ValueError('Reconstructed original chunk payload differs')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recipe', type=Path, required=True)
    parser.add_argument('--archive-topic', type=Path, required=True)
    parser.add_argument('--output-directory', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    recipe_bytes = args.recipe.read_bytes()
    recipe = json.loads(recipe_bytes)
    if recipe['schema'] != SCHEMA or recipe['helper_sha256'] != sha(Path(__file__).read_bytes()):
        raise ValueError('The exact storage recipe/helper identity differs')
    args.output_directory.mkdir(parents=True, exist_ok=True)
    entries = []
    for record in recipe['chunks']:
        relative, target_name = Path(record['source_file']), record['target_file']
        if (len(relative.parts) != 2 or relative.parts[0] != 'notes' or
                relative.parts[1] in ('.', '..') or Path(target_name).name != target_name):
            raise ValueError('The original storage chunk paths are invalid')
        source = args.archive_topic/relative
        target = args.output_directory/target_name
        data = restore_bytes(record, source.read_bytes())
        existed = target.exists()
        if existed:
            if target.read_bytes() != data:
                raise ValueError('An existing original target chunk differs')
        else:
            with target.open('xb') as stream:
                stream.write(data)
        if sha(target.read_bytes()) != record['target_sha256']:
            raise ValueError('The written original chunk failed complete SHA readback')
        entries.append(dict(file=str(target), sha256=record['target_sha256'],
                            bytes=len(data), already_existed=existed))
    result = dict(schema=SCHEMA, recipe_file=str(args.recipe), recipe_sha256=sha(recipe_bytes),
        helper_sha256=sha(Path(__file__).read_bytes()),
        all_original_target_bytes_reconstructed_and_read_back=True, files=entries,
        original_numerical_arrays_and_raw_metadata_unchanged=True)
    if args.report.exists():
        raise ValueError('Use a fresh recovery report')
    args.report.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(args.report), report_sha256=sha(args.report.read_bytes()),
        reconstructed_original_chunks=len(entries))), flush=True)


if __name__ == '__main__':
    main()

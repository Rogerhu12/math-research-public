#!/usr/bin/env python3
"""Pure in-memory storage checks on one frozen, already reviewed M12 package.

No solver/geometry reader/backend is imported or invoked.  No shard, logical
container, geometry metadata or future candidate is written; only the small
test report is written, exclusively, after all checks finish.
"""
from __future__ import annotations

import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
META = TOPIC/'notes/2026-11-09-db6f-root-flat17-coupled-m12f24.json'
META_SHA = 'da43f85ee6715254cca3daddd609c80e23bdf97916acb9ba2034282c3c237c7d'
DATA_SHA = '359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0'
CODEC = HERE/'db6f-prefix-shared-jet-byte-shards.py'


def sha(payload):
    return hashlib.sha256(payload).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError('Refusing to replace an existing report')
    meta_blob = META.read_bytes()
    if sha(meta_blob) != META_SHA:
        raise ValueError('Frozen old geometry metadata changed')
    meta = json.loads(meta_blob)
    path = META.parent/meta['data_file']
    original = path.read_bytes()
    if sha(original) != DATA_SHA or meta['data_sha256'] != DATA_SHA:
        raise ValueError('Frozen old logical data changed')
    if type(meta['nodes']) is not int or type(meta['modes']) is not int or (meta['nodes'], meta['modes']) != (2570, 24):
        raise ValueError('Wrong existing positive fixture')
    spec = importlib.util.spec_from_file_location('byte_shard_codec_under_test', CODEC)
    codec = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(codec)
    expected = dict(nodes=meta['nodes'], modes=meta['modes'], logical_sha256=DATA_SHA)
    descriptor, parts = codec.encode_bytes(original, nodes=meta['nodes'], modes=meta['modes'],
                                           part_stem='old-m12-storage-only', chunk_bytes=1_000_000)
    descriptor = codec.parse_descriptor(codec.canonical(descriptor))
    restored = codec.decode_bytes(descriptor, parts, **expected)
    if restored != original:
        raise AssertionError('Container bytes were changed')
    reversed_mapping = dict(reversed(list(parts.items())))
    if codec.decode_bytes(descriptor, reversed_mapping, **expected) != original:
        raise AssertionError('Dictionary enumeration leaked into logical order')
    identity = codec.inspect_container(original, nodes=2570, modes=24)
    if codec.inspect_container(restored, nodes=2570, modes=24) != identity:
        raise AssertionError('Saved array bytes were changed')
    rejected = []
    def reject(name, mutate):
        altered, data = copy.deepcopy(descriptor), dict(parts)
        mutate(altered, data)
        try:
            codec.decode_bytes(altered, data, **expected)
        except ValueError as exc:
            rejected.append(dict(case=name, rejected=True, reason=str(exc)))
        else:
            raise AssertionError('Invalid storage accepted: '+name)
    reject('missing_part', lambda d, p: p.pop(d['parts'][0]['file']))
    reject('extra_part', lambda d, p: p.update({'unexpected.bin.gz': b''}))
    reject('descriptor_parts_reversed', lambda d, p: d['parts'].reverse())
    reject('index_boolean', lambda d, p: d['parts'][0].update(index=False))
    reject('index_wrong', lambda d, p: d['parts'][0].update(index=1))
    reject('offset_gap', lambda d, p: d['parts'][1].update(offset=d['parts'][1]['offset']+1))
    reject('offset_overlap', lambda d, p: d['parts'][1].update(offset=d['parts'][1]['offset']-1))
    reject('raw_length_zero', lambda d, p: d['parts'][0].update(raw_bytes=0))
    reject('raw_length_too_large', lambda d, p: d['parts'][0].update(raw_bytes=4_000_001))
    reject('stored_length_limit', lambda d, p: d['parts'][0].update(stored_bytes=5_000_000))
    reject('stored_length_boolean', lambda d, p: d['parts'][0].update(stored_bytes=True))
    reject('raw_digest_wrong', lambda d, p: d['parts'][0].update(raw_sha256='0'*64))
    reject('stored_digest_wrong', lambda d, p: d['parts'][0].update(stored_sha256='0'*64))
    reject('stored_digest_not_canonical', lambda d, p: d['parts'][0].update(stored_sha256='G'*64))
    reject('escaping_part_filename', lambda d, p: d['parts'][0].update(file='../outside.bin.gz'))
    reject('duplicate_part_filename', lambda d, p: d['parts'][1].update(file=d['parts'][0]['file']))
    reject('logical_trailing_gap', lambda d, p: d.update(logical_bytes=d['logical_bytes']+1))
    reject('logical_length_boolean', lambda d, p: d.update(logical_bytes=True))
    reject('logical_digest_wrong', lambda d, p: d.update(logical_sha256='0'*64))
    reject('unknown_descriptor_field', lambda d, p: d.update(success=True))
    reject('wrong_storage_schema', lambda d, p: d.update(schema='legacy-data-file'))
    reject('nodes_boolean', lambda d, p: d.update(nodes=True))
    reject('wrong_nodes', lambda d, p: d.update(nodes=d['nodes']+1))
    reject('modes_boolean', lambda d, p: d.update(modes=True))
    reject('wrong_modes', lambda d, p: d.update(modes=d['modes']+1))
    reject('array_missing', lambda d, p: d['arrays'].pop('mean_increments'))
    reject('array_extra', lambda d, p: d['arrays'].update({'new': {}}))
    reject('array_dimension_boolean', lambda d, p: d['arrays']['jets'].update(shape=[True,2570,74]))
    reject('array_wrong_dtype', lambda d, p: d['arrays']['jets'].update(dtype='>f8'))
    reject('array_byte_count_wrong', lambda d, p: d['arrays']['jets'].update(c_order_bytes=8))
    reject('array_digest_wrong', lambda d, p: d['arrays']['jets'].update(c_order_sha256='0'*64))
    def truncate_gzip(d, p):
        item = d['parts'][0]
        p[item['file']] = p[item['file']][:-3]
        item['stored_bytes'] = len(p[item['file']])
        item['stored_sha256'] = sha(p[item['file']])
    reject('truncated_gzip_with_updated_storage_hash', truncate_gzip)
    def alter_logical_byte(d, p):
        item = d['parts'][0]
        raw = bytearray(gzip.decompress(p[item['file']]))
        raw[len(raw)//2] ^= 1
        raw = bytes(raw)
        p[item['file']] = gzip.compress(raw, mtime=0)
        item.update(raw_sha256=sha(raw), stored_bytes=len(p[item['file']]),
                    stored_sha256=sha(p[item['file']]))
    reject('changed_logical_byte_with_updated_part_hashes', alter_logical_byte)
    for name, payload in (
        ('duplicate_json_field', b'{"schema":"a","schema":"b"}'),
        ('nonfinite_json_token', b'{"logical_bytes":NaN}')):
        try:
            codec.parse_descriptor(payload)
        except ValueError as exc:
            rejected.append(dict(case=name, rejected=True, reason=str(exc)))
        else:
            raise AssertionError('Invalid JSON accepted: '+name)
    for name, shape in (('original_npz_wrong_expected_nodes', (2571,24)),
                        ('original_npz_wrong_expected_modes', (2570,25))):
        try:
            codec.inspect_container(original, nodes=shape[0], modes=shape[1])
        except ValueError as exc:
            rejected.append(dict(case=name, rejected=True, reason=str(exc)))
        else:
            raise AssertionError('Invalid expected NPZ shape accepted: '+name)
    records = []
    for source in (META, path, CODEC, Path(__file__).resolve()):
        blob = source.read_bytes()
        records.append(dict(path=str(source), bytes=len(blob), sha256=sha(blob)))
    report = dict(
        status='PASS_PURE_OLD_CONTAINER_BYTE_ROUNDTRIP_ONLY',
        scope='Existing reviewed M12 logical container; in-memory storage only. '
              'No new geometry, no consumer adaptation, no solver, no mathematical certificate.',
        inputs=records, logical_bytes=len(original), logical_sha256=sha(original),
        nodes=2570, base_representation_modes=24,
        descriptor_sha256=sha(codec.canonical(descriptor)),
        memory_only_parts=descriptor['parts'],
        stored_total_bytes=sum(map(len, parts.values())),
        largest_part_bytes=max(map(len, parts.values())),
        strict_file_limit=5_000_000,
        exact_logical_bytes_equal=True, exact_c_order_array_bytes_equal=True,
        mapping_enumeration_order_irrelevant=True, array_ledger=identity,
        negative_cases=rejected, negative_case_count=len(rejected),
        files_written=['this small report only'],
        logical_data_or_parts_written=0, geometry_reader_calls=0,
        geometry_backend_calls=0, solver_calls=0, source_root_calls=0,
        future_geometry_manifests=0)
    blob = (json.dumps(report, indent=2, allow_nan=False)+'\n').encode()
    if len(blob) >= 100_000:
        raise ValueError('Unexpectedly large diagnostic report')
    with args.out.open('xb') as stream:
        stream.write(blob)
    print(json.dumps(dict(status=report['status'], report=str(args.out),
                          sha256=sha(blob), bytes=len(blob),
                          parts=len(parts), negative_cases=len(rejected),
                          new_geometry=0, solver_calls=0)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Preserve new native rows while restoring the exact original gzip bytes.

The base and every existing array entry must be unchanged. Metadata,
including a partial native's complete=False status, is retained verbatim.
If native JSON/gzip bytes are not exactly reproducible in this runtime,
the operation refuses; the separate lossless binary-parts tool can be used.
No mathematical row or floating-point proposal is recomputed.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path

KIND = 'exact_original_native_gzip_prefix_delta_v1'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(doc):
    return (json.dumps(doc, indent=2, allow_nan=False) + '\n').encode()


def read_native(path):
    raw = Path(path).read_bytes()
    return raw, json.loads(gzip.decompress(raw))


def write_new(path, raw):
    path = Path(path)
    if path.exists():
        if path.read_bytes() != raw:
            raise FileExistsError('Keep the existing distinct artifact: ' + str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(raw)


def reconstruct(base_raw, base_doc, delta):
    if delta['kind'] != KIND or sha(base_raw) != delta['base_sha256']:
        raise ValueError('The exact original base is required')
    target = dict(delta['target_template'])
    for key, part in delta['array_appends'].items():
        prior = base_doc[key]
        if len(prior) != part['base_count'] or target[key] is not None:
            raise ValueError('The native array base or template changed')
        target[key] = prior + part['new_entries']
        if len(target[key]) != part['target_count']:
            raise ValueError('The complete original prefix count changed')
    plain = encode(target)
    if sha(plain) != delta['original_json_sha256']:
        raise ValueError('The original native JSON bytes were not restored')
    raw = gzip.compress(plain, compresslevel=9, mtime=0)
    if len(raw) != delta['original_bytes'] or sha(raw) != delta['original_sha256']:
        raise ValueError('The original gzip container was not restored exactly')
    return raw


def pack(base, original, output, arrays):
    base_raw, base_doc = read_native(base)
    original_raw, original_doc = read_native(original)
    if base_doc['kind'] != original_doc['kind'] or base_doc['identity'] != original_doc['identity']:
        raise ValueError('The actual mathematical object/source changed')
    template = dict(original_doc)
    appends = {}
    for key in arrays:
        before, after = base_doc[key], original_doc[key]
        if not isinstance(before, list) or not isinstance(after, list) or after[:len(before)] != before:
            raise ValueError('An old native row changed: ' + key)
        if len(after) <= len(before):
            raise ValueError('Only genuinely new rows may be preserved: ' + key)
        appends[key] = dict(base_count=len(before), target_count=len(after), new_entries=after[len(before):])
        template[key] = None
    delta = dict(kind=KIND, base_file=Path(base).name, base_sha256=sha(base_raw),
                 original_file=Path(original).name, original_sha256=sha(original_raw),
                 original_json_sha256=sha(encode(original_doc)), original_bytes=len(original_raw),
                 original_complete=original_doc['complete'], original_failure=original_doc.get('failure'),
                 target_template=template, array_appends=appends,
                 same_original_rows_not_recomputed=True, exact_original_container_required=True)
    if reconstruct(base_raw, base_doc, delta) != original_raw:
        raise ValueError('The input container cannot be reproduced exactly')
    packed = gzip.compress(encode(delta), compresslevel=9, mtime=0)
    if len(packed) > 5_000_000:
        raise ValueError('The delta exceeds the repository file limit')
    write_new(output, packed)
    persisted = json.loads(gzip.decompress(Path(output).read_bytes()))
    if reconstruct(base_raw, base_doc, persisted) != original_raw:
        raise ValueError('The actual saved delta failed byte-exact reconstruction')
    return dict(delta_sha256=sha(packed), delta_bytes=len(packed),
                original_sha256=delta['original_sha256'], original_bytes=len(original_raw),
                original_complete=delta['original_complete'],
                new_entries={k:len(v['new_entries']) for k,v in appends.items()},
                actual_saved_delta_restored_original_gzip_bytes=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='operation', required=True)
    p = sub.add_parser('pack')
    p.add_argument('--base', type=Path, required=True)
    p.add_argument('--original', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--array', action='append', required=True)
    p = sub.add_parser('restore')
    p.add_argument('--base', type=Path, required=True)
    p.add_argument('--delta', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.operation == 'pack':
        result = pack(args.base, args.original, args.out, args.array)
    else:
        raw, doc = read_native(args.base)
        delta = json.loads(gzip.decompress(args.delta.read_bytes()))
        restored = reconstruct(raw, doc, delta)
        write_new(args.out, restored)
        result = dict(original_sha256=sha(restored), bytes=len(restored),
                      complete=delta['original_complete'], exact_container_restored=True)
    print(json.dumps(result, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()

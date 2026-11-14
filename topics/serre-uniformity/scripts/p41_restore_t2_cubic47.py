#!/usr/bin/env python3
"""Restore the three actual T2 branches and verify the original packed bytes."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path,
                        default=Path(__file__).resolve().parent/'data')
    parser.add_argument('--output', type=Path,
                        default=Path('/tmp/p41_hecke2_cubic47_checkpoint.json.gz'))
    args = parser.parse_args()
    index = json.loads((args.data_dir/'p41_hecke2_cubic47_parts.json').read_text())
    result = index['header']
    assert 'targets' not in result
    result['targets'] = []
    for expected in index['parts']:
        raw = (args.data_dir/expected['file']).read_bytes()
        assert len(raw) == expected['bytes']
        assert hashlib.sha256(raw).hexdigest() == expected['sha256']
        part = json.loads(gzip.decompress(raw))
        assert part['target_index_0based'] == len(result['targets'])
        result['targets'].append(part['target'])
    assert len(result['targets']) == 3
    raw = (json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n').encode()
    packed = gzip.compress(raw, mtime=0)
    assert len(packed) == index['original_bytes']
    assert hashlib.sha256(packed).hexdigest() == index['original_sha256']
    # The complete file is an intermediate; repository storage is per branch.
    assert not args.output.resolve().is_relative_to(args.data_dir.resolve())
    temporary = args.output.with_suffix(args.output.suffix+'.new')
    temporary.write_bytes(packed)
    temporary.replace(args.output)
    print('Restored all three actual T2 cubic branches; original bytes and SHA256 PASS')


if __name__ == '__main__':
    main()

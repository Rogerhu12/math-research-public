#!/usr/bin/env python3
"""Extract the complete original M28 metric reference from its archived adapter.

The original successful M28 solve saved this field before its interrupted
physical postprocessing. No lost ready event is fabricated. The resulting
reference is consumed by the unchanged frozen factory and staged audit,
which reconstruct and verify their own actual ready object before solving.
"""
import argparse
import hashlib
import json
from pathlib import Path

STEM = '2026-11-12-strong-q096-sameg-m28-local-recovery6-r1'
MANIFEST_SHA = '42bcef485ba3e1aabbfbe843fbbce1a07a41ffe286b42b7ef83a000256ef4c1f'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic', type=Path,
                        default=Path(__file__).resolve().parents[1])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    topic = args.topic.resolve()
    manifest_file = topic/'notes'/(STEM+'-stable-files.json')
    if digest(manifest_file) != MANIFEST_SHA:
        raise ValueError('The original complete 60-file archive manifest differs')
    manifest = json.loads(manifest_file.read_text())
    if len(manifest['files']) != 60:
        raise ValueError('The original 60-file archive is required')
    for item in manifest['files']:
        relative = Path(item['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('The original archive path is invalid')
        file = topic/relative
        if file.stat().st_size != item['bytes'] or digest(file) != item['sha256']:
            raise ValueError('An original archive member differs: '+str(relative))
    adapter = topic/'notes'/(STEM+'-actual28-tail-response_adapter.json')
    metric = json.loads(adapter.read_text())['stored_metric']
    if (metric['physicalParameters']['modes'] != 28 or metric['cellCount'] != 160
            or metric['profileFingerprintBefore'] != metric['profileFingerprintAfter']):
        raise ValueError('This is not the saved original M28 metric reference')
    result = {
        'storedMetricAdapter': metric,
        'extraction_provenance': {
            'scope': 'Unchanged complete original M28 stored-metric adapter extracted from the already archived original successful solver run. This is a reference wrapper, not a reconstructed lost ready event or a new solve.',
            'source': str(adapter), 'source_sha256': digest(adapter),
            'original_60_files_verified': True,
            'old_unpublished_ready_not_fabricated': True,
        },
    }
    data = (json.dumps(result, indent=2)+'\n').encode()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.out.exists() and args.out.read_bytes() != data:
        raise FileExistsError('A different recovery reference already exists')
    if not args.out.exists():
        args.out.write_bytes(data)
    print(json.dumps({'reference': str(args.out), 'sha256': digest(args.out),
                      'original_m28_field_unchanged': True,
                      'new_geometry_or_Newton_evaluations': 0}))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Restore exact already-paid R738 base blocks and calibrations; no science."""
import argparse
import json
import os
from pathlib import Path, PurePosixPath
import tempfile
import time
import zipfile
from r734_completed_members_transport_20261128 import completed, fetch_zip, require, sha
from restore_completed_r738_inputs_20261128 import retain, safe_name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--request', required=True)
    args = ap.parse_args()
    start = time.monotonic()
    req = json.loads(Path(args.request).read_bytes())
    require(req['repository'] == 'Rogerhu12/math-research-public', 'Wrong repository')
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and
            os.environ.get('GITHUB_REPOSITORY', '').lower() == req['repository'].lower(),
            'Public Actions input transport required')
    for path, digest in req['source_sha256'].items():
        require(sha(Path(path).read_bytes()) == digest, 'Bound source changed: ' + path)
    temp = Path(os.environ['RUNNER_TEMP'])
    directory = req['paid_source_directory']
    checkpoint = req['new_checkpoint_directory']
    require(PurePosixPath(directory).name == directory and
            PurePosixPath(checkpoint).name == checkpoint, 'Invalid state directory')
    out = temp / directory
    target_root = out / 'r738'
    require((target_root / 'ledger.json').is_file(), 'Restore the original shared ledger first')
    ledger = json.loads((target_root / 'ledger.json').read_bytes())
    spec = req['completed_sources']['base_blocks']
    token = os.environ.get('GITHUB_TOKEN', '')
    require(bool(token), 'Read credential required')
    completed(spec['original'], token)
    transported = {}
    with tempfile.TemporaryDirectory(prefix='r738-paid-base-transport-', dir=temp) as folder:
        archive = Path(folder) / 'original.zip'
        fetch_zip(spec['original'], token, archive)
        with zipfile.ZipFile(archive) as source:
            names = source.namelist()
            require(len(names) == len(set(names)), 'Repeated original member')
            for name, meta in spec['files'].items():
                path = safe_name(name)
                require(len(path.parts) == 1 and name.endswith('.npz') and
                        (name.startswith('base_') or name.startswith('r738_angular_calibration_')),
                        'Member outside the already-paid base input scope')
                require(ledger['kept'].get(name[:-4]) == [meta['bytes'], meta['sha256']],
                        'Original kept ledger binding differs: ' + name)
                info = source.getinfo(name)
                require(not info.is_dir() and info.file_size == meta['bytes'] and
                        ((info.external_attr >> 16) & 0o170000) != 0o120000,
                        'Original member type/size differs')
                raw = source.read(info)
                require(len(raw) == meta['bytes'] and sha(raw) == meta['sha256'],
                        'Original member SHA differs: ' + name)
                retain(target_root / path, raw)
                transported[name] = dict(bytes=len(raw), sha256=sha(raw))
    receipt = dict(kind='exact_completed_R738_paid_base_block_restore',
                   original=spec['original'], restoring_run=os.environ['GITHUB_RUN_ID'],
                   restoring_attempt=os.environ.get('GITHUB_RUN_ATTEMPT', '1'),
                   administrative_seconds=time.monotonic() - start,
                   new_scientific_evaluations=0, original_job_log_requests=0,
                   member_count=len(transported), files=transported)
    raw = json.dumps(receipt, sort_keys=True, separators=(',', ':')).encode()
    name = ('base-input-restore-' + os.environ['GITHUB_RUN_ID'] + '-' +
            os.environ.get('GITHUB_RUN_ATTEMPT', '1') + '.json')
    retain(out / name, raw)
    retain(temp / checkpoint / name, raw)
    print('COMPLETED_R738_BASE_BLOCKS_RESTORED ' +
          json.dumps({k: v for k, v in receipt.items() if k != 'files'}, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()

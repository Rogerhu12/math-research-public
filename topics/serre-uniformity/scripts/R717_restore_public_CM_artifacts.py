#!/usr/bin/env python3
"""Restore pinned prior R717 checkpoints, or this run's complete bin artifacts.

All downloads remain on the public GitHub Actions runner.  Large artifacts
are never split, encoded, or transmitted through the chat connector.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import traceback

from R717_public_original_cm_norm import (
    REQUEST, SESSION, archive_sources, check_bin, check_final, now, read,
    result_name, save, sha,
)

REPOSITORY = 'Rogerhu12/math-research-public'


def gh_json(*args):
    process = subprocess.run(['gh', *args], check=True, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return json.loads(process.stdout)


def run_artifacts(run_id):
    pages = gh_json('api', '--paginate', '--slurp',
                   f'repos/{REPOSITORY}/actions/runs/{run_id}/artifacts')
    return [item for page in pages for item in page['artifacts'] if not item.get('expired')]


def select_current_bin(items, result, run_id, maximum_attempt):
    prefix = 'serre-cartier-' + result + '-' + run_id + '-'
    choices = []
    for item in items:
        name = item['name']
        if not name.startswith(prefix):
            continue
        suffix = name[len(prefix):]
        if suffix.isdigit() and 1 <= int(suffix) <= maximum_attempt:
            choices.append((int(suffix), item))
    if not choices:
        raise RuntimeError('No completed artifact was uploaded for ' + result)
    return max(choices, key=lambda pair: pair[0])[1]


def validate_identifiers(spec, request):
    run_id = str(spec['run_id'])
    if not re.fullmatch(r'[0-9]+', run_id):
        raise ValueError('A numeric workflow run ID is required')
    result = spec['result']
    base = request['result']
    allowed = {base, base+'-recover'}
    allowed.update(base+'-bins-'+str(i) for i in range(request['shard_count']))
    if result not in allowed or not re.fullmatch(r'[A-Za-z0-9_-]+', spec['artifact_name']):
        raise ValueError('An artifact is outside this R717 request')
    expected_prefix = 'serre-cartier-' + result + '-' + run_id + '-'
    if not spec['artifact_name'].startswith(expected_prefix):
        raise ValueError('The artifact name is not bound to the selected run and result')
    return run_id, result


def download(spec, request, current=False):
    run_id, result = validate_identifiers(spec, request)
    destination = (Path(os.environ['RUNNER_TEMP'])/'R717-imports'/result
                   /spec['artifact_name'])
    destination.mkdir(parents=True, exist_ok=True)
    marker = destination/'R717-download-checked.json'
    files = spec.get('files_sha256', {})
    if not current:
        if result.startswith(request['result']+'-bins-'):
            suffix = result[len(request['result']+'-bins-'):]
            required = 'R717-bins-' + suffix + '.json.gz'
        else:
            required = 'R717-exact-original-CM-norm.json'
        if required not in files:
            raise ValueError('Every prior-run input must pin its actual checkpoint or final receipt SHA')
    if not marker.exists():
        subprocess.run(['gh', 'run', 'download', run_id, '--repo', REPOSITORY,
                        '--name', spec['artifact_name'], '--dir', str(destination)], check=True)
    pinned = []
    for name, expected in files.items():
        if Path(name).name != name or not re.fullmatch(r'[0-9a-f]{64}', expected):
            raise ValueError('Invalid pinned input filename or SHA')
        path = destination/name
        actual = sha(path)
        if actual != expected:
            raise ValueError('A downloaded prior checkpoint does not match its fixed SHA')
        pinned.append({'file': name, 'sha256': actual})
    base = request['result']
    if result.startswith(base+'-bins-'):
        shard = int(result[len(base+'-bins-'):])
        path = destination/f'R717-bins-{shard}.json.gz'
        state = check_bin(read(path), request, shard, require_complete=current)
        if current:
            summary = read(destination/'run-receipt.json')
            if not summary.get('complete') or summary.get('phase') != 'bins':
                raise ValueError('A current-run bin receipt is incomplete')
            if summary.get('source_commit') != os.environ['GITHUB_SHA']:
                raise ValueError('The current-run bin uses a different source commit')
            if summary.get('arithmetic_sha256') != request['arithmetic_sha256']:
                raise ValueError('The current-run bin uses different arithmetic')
            if summary.get('bin_sha256') != sha(path):
                raise ValueError('The current-run bin does not match its completed receipt')
        result_record = {'file': path.name, 'sha256': sha(path),
                         'complete': state['complete'], 'row_count': state['row_count'],
                         'completed_through_a': state['completed_through_a']}
    else:
        path = destination/'R717-exact-original-CM-norm.json'
        receipt = check_final(path, request)
        result_record = {'file': path.name, 'sha256': sha(path), 'complete': True,
                         'padic_result': receipt['padic_result']}
    record = {'repository': REPOSITORY, 'run_id': run_id,
              'artifact_name': spec['artifact_name'], 'result': result,
              'source': 'same workflow bin dependency' if current else 'explicit fixed prior input',
              'artifact_metadata': spec.get('artifact_metadata'),
              'fixed_input_hashes': pinned, 'verified_output': result_record,
              'destination': str(destination)}
    save(marker, record)
    return record



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase', choices=['bins', 'recover'], required=True)
    parser.add_argument('--shard-index', type=int, default=0)
    args = parser.parse_args()
    request = read(REQUEST)
    result = result_name(request, args.phase, args.shard_index)
    out = Path(os.environ['RUNNER_TEMP'])/'serre-cartier'/result
    out.mkdir(parents=True, exist_ok=True)
    save(SESSION, {'request': request, 'result': result, 'output': str(out),
                   'phase': args.phase, 'shard_index': args.shard_index})
    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    archive_sources(out, request, source)
    incomplete = {
        'result': result, 'phase': args.phase, 'shard_index': args.shard_index,
        'complete': False, 'source_commit': source,
        'execution_environment': 'public-repository-github-actions',
        'started_at_utc': now(), 'mathematical_completion_claimed': False,
        'failure_file': 'R717-artifact-import-failure.txt',
    }
    save(out/'run-receipt.json', incomplete)
    source_archive = out/'R717-artifact-restore-source.py.gz'
    with source_archive.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as stream:
            stream.write(Path(__file__).read_bytes())
    records = []
    code = 0
    try:
        if sha(__file__) != request['restore_driver_sha256']:
            raise ValueError('The artifact restoration source does not match its request SHA')
        for spec in request.get('resume_artifacts', []):
            allowed = args.phase == 'recover' or spec['result'] in {
                request['result'], request['result']+'-recover', result}
            if allowed:
                records.append(download(spec, request, current=False))
        if args.phase == 'recover':
            run_id = os.environ['GITHUB_RUN_ID']
            maximum_attempt = int(os.environ['GITHUB_RUN_ATTEMPT'])
            available = run_artifacts(run_id)
            for shard in range(request['shard_count']):
                name = request['result']+'-bins-'+str(shard)
                item = select_current_bin(available, name, run_id, maximum_attempt)
                records.append(download({
                    'run_id': run_id, 'result': name, 'artifact_name': item['name'],
                    'artifact_metadata': {key: item.get(key) for key in
                                          ('id', 'name', 'size_in_bytes', 'digest', 'created_at')},
                }, request, current=True))
    except Exception:
        (out/'R717-artifact-import-failure.txt').write_text(traceback.format_exc())
        incomplete['finished_at_utc'] = now()
        save(out/'run-receipt.json', incomplete)
        code = 1
    save(out/'R717-artifact-imports.json', {
        'restore_driver_sha256': sha(__file__), 'request_sha256': sha(REQUEST),
        'source_archive': source_archive.name, 'source_archive_sha256': sha(source_archive),
        'phase': args.phase, 'shard_index': args.shard_index, 'imports': records,
        'imports_complete': code == 0, 'no_prior_lattice_terms_recomputed': True,
    })
    print(json.dumps({'restored_artifacts': len(records), 'phase': args.phase,
                      'result': result, 'imports_complete': code == 0}), flush=True)
    return code


if __name__ == '__main__':
    sys.exit(main())

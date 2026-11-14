#!/usr/bin/env python3
"""Create a distinct one-stage-worker resource route from the actual live copy.

The retained stage maps use the original, byte-identical mathematical body.
The new pool checks that its complete body differs only in the allowed worker
count and the explicitly named original cache provenance entry. No old source
or active output is overwritten.
"""
import argparse
import hashlib
import json
from pathlib import Path


def write_once(path, data):
    if path.exists():
        if path.read_bytes() != data:
            raise FileExistsError(f'Existing different source preserved: {path}')
    else:
        path.write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime-root', type=Path, required=True)
    parser.add_argument('--repo-topic', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    live = args.runtime_root/'topics/visible-flexible-closed-surface/scripts'
    repository = args.repo_topic/'scripts'
    mapping = {
        'fd2d-run-prefix-snapshot.py': 'fd2d-run-prefix-single.py',
        'fd2d-snapshot-tail-continuation.py': 'fd2d-single-tail-continuation.py',
        'fd2d-snapshot-tail-client.py': 'fd2d-single-tail-client.py',
        'fd2d-snapshot-tail-stage-worker.mjs': 'fd2d-single-tail-stage-worker.mjs',
    }
    records = []
    for original, renamed in mapping.items():
        text = (live/original).read_text()
        for old, new in mapping.items():
            text = text.replace(old, new)
        text = text.replace('choices=(0, 2, 4)', 'choices=(0, 1, 2, 4)')
        text = text.replace('stage_workers not in (0, 2, 4)', 'stage_workers not in (0, 1, 2, 4)')
        text = text.replace('stage_workers in (2, 4)', 'stage_workers in (1, 2, 4)')
        text = text.replace('Explicit stage workers must be 0, 2 or 4',
                            'Explicit stage workers must be 0, 1, 2 or 4')
        text = text.replace('![2,4].includes(stageWorkers)', '![1,2,4].includes(stageWorkers)')
        if renamed.endswith('stage-worker.mjs'):
            text = text.replace("from './fd2d-cached-tail-stage-pool.mjs'",
                                "from './fd2d-single-tail-stage-pool.mjs'")
        if renamed.endswith('client.py'):
            text = text.replace("sources += ['fd2d-cached-tail-stage-pool.mjs',",
                                "sources += ['fd2d-single-tail-stage-pool.mjs', 'fd2d-cached-tail-stage-pool.mjs',")
            before = '''    def _observe_exception(self, error):
        code = self.proc.poll()
'''
            after = '''    def _observe_exception(self, error):
        code = self.proc.poll()
        waited = 0.0
        # EOF may precede the final process exit notification by a few ms.
        # Observe that natural exit before inherited cleanup can terminate it.
        # Ordinary mathematical exceptions do not wait on a live worker.
        if code is None and 'worker stopped' in str(error).lower():
            began = time.monotonic()
            try:
                code = self.proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                code = self.proc.poll()
            waited = time.monotonic()-began
'''
            if before not in text:
                raise RuntimeError('Original EOF observer not found')
            text = text.replace(before, after)
            text = text.replace("'worker_returncode': code, 'exception': repr(error),",
                                "'worker_returncode': code, 'exception': repr(error),\n            'natural_exit_observation_seconds': waited,")
        data = text.encode()
        for destination in (repository/renamed, live/renamed):
            write_once(destination, data)
        records.append({'source': str(live/original), 'file': str(live/renamed),
                        'repository_file': str(repository/renamed), 'bytes': len(data),
                        'sha256': hashlib.sha256(data).hexdigest()})

    original_pool = 'fd2d-cached-tail-stage-pool.mjs'
    new_pool = 'fd2d-single-tail-stage-pool.mjs'
    source = (live/original_pool).read_text()
    old_guard = "if(![2,4].includes(workers))throw infrastructure('This optional backend uses two or four workers');"
    new_guard = "if(![1,2,4].includes(workers))throw infrastructure('This optional backend uses one, two or four workers');"
    if source.count(old_guard) != 1 or source.count('entryURL:import.meta.url,') != 1:
        raise RuntimeError('Original resource-only replacement positions differ')
    body = source.replace(old_guard, new_guard).replace('entryURL:import.meta.url,',
                                                      'entryURL:canonicalPoolURL,')
    prefix = '''// Resource-only wrapper of the actual cached stage pool.
// Its entire mathematical/control body is checked against the saved original;
// only worker-count admission and explicit cache provenance naming differ.
import fs from 'node:fs';
import {createHash} from 'node:crypto';
const canonicalPoolURL=new URL('./fd2d-cached-tail-stage-pool.mjs',import.meta.url);
const ownResourceText=fs.readFileSync(new URL(import.meta.url),'utf8');
const marker='// FD2D_ORIGINAL_POOL_BODY';
const markerAt=ownResourceText.indexOf('\\n'+marker+'\\n');
if(markerAt<0)throw Error('Resource wrapper body marker missing');
const checkedBody=ownResourceText.slice(markerAt+marker.length+2)
 .replace(NEW_GUARD,OLD_GUARD)
 .replace('entryURL:canonicalPoolURL,','entryURL:import.meta.url,');
const canonicalResourceText=fs.readFileSync(canonicalPoolURL,'utf8');
if(checkedBody!==canonicalResourceText)
 throw Error('Resource wrapper differs from the saved mathematical pool body');
const resourceHash=text=>createHash('sha256').update(text).digest('hex');
console.error(JSON.stringify({event:'resource_only_pool_identity',source:import.meta.url,
 sha256:resourceHash(ownResourceText),canonicalSource:String(canonicalPoolURL),
 canonicalSHA256:resourceHash(canonicalResourceText),completeBodyEqualityAfterDeclaredResourceChanges:true,
 scope:'Original independent map arithmetic and cache identity; one worker is additionally admitted.'}));
// FD2D_ORIGINAL_POOL_BODY
'''.replace('NEW_GUARD', json.dumps(new_guard)).replace('OLD_GUARD', json.dumps(old_guard))
    data = (prefix+body).encode()
    for destination in (repository/new_pool, live/new_pool):
        write_once(destination, data)
    records.append({'source': str(live/original_pool), 'file': str(live/new_pool),
                    'repository_file': str(repository/new_pool), 'bytes': len(data),
                    'sha256': hashlib.sha256(data).hexdigest(),
                    'unchanged_math_body_checked_at_runtime': True,
                    'canonical_source_sha256': hashlib.sha256(source.encode()).hexdigest()})

    supervisor_source = repository/'fd2d-external-exit-supervisor.py'
    supervisor_name = 'fd2d-single-external-exit-supervisor.py'
    text = supervisor_source.read_text().replace('choices=(2, 4), default=4',
                                               'choices=(1, 2, 4), default=1')
    text = text.replace('fd2d-run-prefix-snapshot.py', 'fd2d-run-prefix-single.py')
    data = text.encode()
    for destination in (repository/supervisor_name,
                        args.runtime_root/'control'/supervisor_name):
        write_once(destination, data)
    records.append({'source': str(supervisor_source),
                    'file': str(args.runtime_root/'control'/supervisor_name),
                    'repository_file': str(repository/supervisor_name), 'bytes': len(data),
                    'sha256': hashlib.sha256(data).hexdigest()})
    report = {'scope': 'New distinct one-stage-worker resource route; no new equation, tolerance, physical profile or completed solve',
              'numerical_trial': 'Unchanged centered geometric trial after actual local comparison found canonical worse',
              'cache_policy': 'Keep the original context only after exact whole-body equality with the two declared resource changes',
              'sources': records}
    write_once(args.out, (json.dumps(report, indent=2)+'\n').encode())
    print(json.dumps({'out': str(args.out), 'source_count': len(records)}))


if __name__ == '__main__':
    main()

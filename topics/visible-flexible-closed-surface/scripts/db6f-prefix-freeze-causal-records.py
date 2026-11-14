#!/usr/bin/env python3
"""Inventory only closed M14/N512, failed M15, and endpoint-diagnostic records.

The historical dependency snapshot is preserved as historical evidence; it
is not relabeled as a new runtime import trace. Explicit response/driver
hashes are separately checked against recoverable repository source files.
"""
import gzip
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parent.parent
REPO = TOPIC.parent.parent
NOTES = TOPIC / 'notes'
PREFIX = '2026-11-09-db6f-prefix-'
STEMS = [PREFIX + 'flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14',
         PREFIX + 'flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from14']


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_text())


def row(p):
    return dict(path=str(p.relative_to(REPO)), bytes=p.stat().st_size, sha256=sha(p))


def main():
    files = set()
    for stem in STEMS:
        files.update(p for p in NOTES.glob(stem + '*') if p.is_file())
    source_index = {}
    for folder in (TOPIC/'scripts', TOPIC/'repro', TOPIC/'notes'):
        for p in folder.rglob('*'):
            if p.is_file() and p.suffix in ('.py', '.mjs', '.js', '.cjs'):
                source_index.setdefault(sha(p), []).append(p)
    deps = NOTES/(PREFIX+'source-dependencies-v2.json')
    historical = read(deps)
    bindings = [dict(binding='historical-dependency-snapshot', original=k, sha256=v['sha256'])
                for k, v in historical['files'].items()]
    outcomes = []
    for stem in STEMS:
        repro = read(NOTES/(stem+'-reproduction.json'))
        summ = read(NOTES/(stem+'-summary.json'))
        bindings.append(dict(binding=stem+':driver', original='db6f-prefix-freeze-refine.py',
                             sha256=repro['driver_sha256']))
        for response in NOTES.glob(stem+'_tail_????.json.gz'):
            for name, value in read(response)['source_sha256'].items():
                bindings.append(dict(binding=response.name+':response-source', original=name, sha256=value))
        outcomes.append(dict(stem=stem, actual_driver_exit_code=repro['exit_code'],
                             mathematical_success=summ['solver_success'], error=summ.get('error'),
                             command=repro['command']))
    for binding in bindings:
        choices=source_index.get(binding['sha256'], [])
        if not choices:
            raise RuntimeError('Missing historical source: '+str(binding))
        binding['available_paths']=[str(p.relative_to(REPO)) for p in choices]
        files.add(choices[0])
    extras = [PREFIX+'m14-q512-and-m15-failure.md', PREFIX+'m15-root-seed-diagnostic.md',
              PREFIX+'m15-root-initial-margin.json', PREFIX+'m15-root-initial-margin-v2.json',
              PREFIX+'m15-root-margin-input.json.gz',
              PREFIX+'live-recovery-snapshots-20261109T093205Z.json',
              PREFIX+'source-dependencies-v2.json', PREFIX+'source-dependencies.json']
    files.update(NOTES/name for name in extras)
    files.update([Path(__file__).resolve(), TOPIC/'scripts/db6f-prefix-tail-root-initial-margin.mjs',
                  TOPIC/'scripts/db6f-prefix-tail-root-initial-margin-v2.mjs'])
    # These deterministic front-end sources are additional reproducibility
    # bindings at freeze time, distinct from hashes embedded during execution.
    frontends=['db6f-prefix-flat-coupled.py','db6f-prefix-coupled.py',
               'db6f-prefix-freeze-refine.py','db6f-prefix-tail-raw-lift.mjs',
               'db6f-prefix-preserve-restart.py']
    current=[]
    for name in frontends:
        p=TOPIC/'scripts'/name
        if not p.is_file():
            raise FileNotFoundError(p)
        current.append(row(p));files.add(p)
    records=[row(p) for p in sorted(files)]
    assert all(r['bytes'] < 5_000_000 for r in records)
    assert all(r['bytes'] <= 1_000_000 or r['path'].endswith('.gz') for r in records)
    out=NOTES/(PREFIX+'m14q512-m15failed-publication.json')
    result=dict(scope=__doc__, actual_tool_exits={'M14_N512':0,'M15_failed_DN':0},
                outcomes=outcomes, historical_and_runtime_source_bindings=bindings,
                additional_current_frontend_bindings=current,
                all_source_hashes_recoverable=True, files=records,
                total_bytes=sum(r['bytes'] for r in records),
                maximum_file_bytes=max(r['bytes'] for r in records),
                excludes='All new active trial diagnostic outputs; no old file is overwritten by that run.')
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(dict(inventory=str(out.relative_to(REPO)), files=len(records),
                         total_bytes=result['total_bytes'], maximum_file_bytes=result['maximum_file_bytes'],
                         source_bindings=len(bindings), all_sources_recoverable=True)))


if __name__ == '__main__':
    main()

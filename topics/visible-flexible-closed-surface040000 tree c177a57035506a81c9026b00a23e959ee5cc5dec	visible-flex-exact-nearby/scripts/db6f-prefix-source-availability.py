#!/usr/bin/env python3
"""Resolve recorded source and reproduction hashes to actual repository files.

Only explicit recorded bindings are audited. A command path without a
runtime hash is not silently promoted to a historical source digest.
This reads no GitHub service and never transfers numerical arrays.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_text())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dependencies', type=Path, required=True)
    p.add_argument('--checkpoints', nargs='+', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    topic = Path(__file__).resolve().parent.parent
    repository = topic.parent.parent
    source_files = [x for folder in (topic/'scripts', topic/'notes')
                    for x in folder.iterdir() if x.is_file() and
                    x.suffix in ('.py', '.mjs', '.js', '.cjs')]
    source_files += [x for x in (topic/'repro').rglob('*') if x.is_file() and
                     x.suffix in ('.py', '.mjs', '.js', '.cjs')]
    index = {}
    for f in source_files:
        index.setdefault(digest(f), []).append(str(f.relative_to(repository)))
    bindings, data = [], []
    deps = read(a.dependencies)
    for name, row in deps['files'].items():
        bindings.append(dict(binding=str(a.dependencies), original=name,
                             sha256=row['sha256']))
    def local(path):
        f = Path(path)
        for candidate in (f, repository/f, topic/'notes'/f.name):
            if candidate.is_file():
                return candidate
        raise FileNotFoundError(path)
    def check_data(binding, path, expected):
        f = local(path)
        actual = digest(f)
        data.append(dict(binding=binding, path=str(f), expected_sha256=expected,
                         actual_sha256=actual, passed=actual == expected))
    for path in a.checkpoints:
        cp = read(path)
        assert cp['solver_success'] and cp['config']['actual_nonlinear_tail']
        tailpath = path.parent/cp['tail_seam']['tail_record']
        tail = read(tailpath)
        for name, sha in tail['source_sha256'].items():
            bindings.append(dict(binding=str(tailpath)+':source_sha256',
                                 original='scripts/'+name, sha256=sha))
        stem = path.name.removesuffix('.json.gz')
        reproduction = read(path.with_name(stem+'-reproduction.json'))
        check_data(stem+':baseline', reproduction['baseline'],
                   reproduction['baseline_sha256'])
        if 'initial_tail_sha256' in reproduction:
            check_data(stem+':initial_tail', reproduction['initial_tail_checkpoint'],
                       reproduction['initial_tail_sha256'])
        warm = reproduction.get('warm_conversion')
        if warm:
            check_data(stem+':raw_lift', warm['summary']['output'], warm['sha256'])
        command = reproduction['command']
        port = command[command.index('--linear-port')+1]
        check_data(stem+':physical_port', port, cp['physical_port_sha256'])
        profile = read(local(command[command.index('--profile')+1]))
        chart = read(local(command[command.index('--chart')+1]))
        data.append(dict(binding=stem+':frozen_profile', passed=profile == cp['frozen_profile']))
        data.append(dict(binding=stem+':frozen_chart', passed=chart == cp['chart']))
    for row in bindings:
        row['available_paths'] = index.get(row['sha256'], [])
    missing = [r for r in bindings if not r['available_paths']]
    failed = [r for r in data if not r['passed']]
    out = dict(scope=__doc__, script_sha256=digest(Path(__file__)),
               dependencies=str(a.dependencies), dependencies_sha256=digest(a.dependencies),
               source_bindings=bindings, reproduction_bindings=data,
               unresolved_sources=missing, failed_reproduction_bindings=failed,
               all_passed=not missing and not failed)
    a.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(all_passed=out['all_passed'], source_bindings=len(bindings),
                          reproduction_bindings=len(data), unresolved=len(missing),
                          failed=len(failed))), flush=True)
    if not out['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

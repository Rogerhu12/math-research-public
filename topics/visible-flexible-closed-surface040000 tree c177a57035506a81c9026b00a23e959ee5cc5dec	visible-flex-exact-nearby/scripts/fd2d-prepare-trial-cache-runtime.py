#!/usr/bin/env python3
"""Prepare a distinct actual-trial-construction cache route outside git."""
import argparse
import hashlib
import json
from pathlib import Path


def save(path, data):
    if path.exists():
        if path.read_bytes() != data:
            raise FileExistsError(f'Different source already exists: {path}')
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
        'fd2d-run-prefix-single.py': 'fd2d-run-prefix-trial-cache.py',
        'fd2d-single-tail-continuation.py': 'fd2d-trial-cache-tail-continuation.py',
        'fd2d-single-tail-client.py': 'fd2d-trial-cache-tail-client.py',
        'fd2d-single-tail-stage-worker.mjs': 'fd2d-trial-cache-tail-stage-worker.mjs',
    }
    records = []
    for old, new in mapping.items():
        text = (live/old).read_text()
        for before, after in mapping.items():
            text = text.replace(before, after)
        if new.endswith('client.py'):
            text = text.replace("sources += ['fd2d-single-tail-stage-pool.mjs',",
                                "sources += ['fd2d-geometric-trial-cache.mjs', 'fd2d-single-tail-stage-pool.mjs',")
        if new.endswith('stage-worker.mjs'):
            before = "import {createGeometricTrialHook} from './78718-tail-geometric-newton-retraction-centered-v3.mjs';"
            after = "import {createCachedGeometricTrialHook as createGeometricTrialHook} from './fd2d-geometric-trial-cache.mjs';"
            if before not in text:
                raise RuntimeError('Original geometric helper import not found')
            text = text.replace(before, after)
            before = 'const geometricTrial=createGeometricTrialHook(dn.tail.cells,{spacing:cfg.spacing});'
            after = '''const geometricTrial=createGeometricTrialHook(dn.tail.cells,{spacing:cfg.spacing,
 parameters:dn.tail.parameters,cacheRoot:process.env.VISIBLE_FLEX_STAGE_CACHE_ROOT,
 diagnostic:row=>trace(row)});'''
            if before not in text:
                raise RuntimeError('Original geometric helper constructor not found')
            text = text.replace(before, after)
            text = text.replace('const observed={...row,rhsRootStatistics:rhsRootStatistics()};',
                                'const observed={...row,rhsRootStatistics:rhsRootStatistics(),hostMemory:process.memoryUsage()};')
        data = text.encode()
        for target in (repository/new, live/new):
            save(target, data)
        records.append({'source': str(live/old), 'file': str(live/new),
                        'repository_file': str(repository/new), 'bytes': len(data),
                        'sha256': hashlib.sha256(data).hexdigest()})
    name = 'fd2d-geometric-trial-cache.mjs'
    data = (repository/name).read_bytes()
    save(live/name, data)
    records.append({'source': str(repository/name), 'file': str(live/name),
                    'repository_file': str(repository/name), 'bytes': len(data),
                    'sha256': hashlib.sha256(data).hexdigest()})
    old = args.runtime_root/'control/fd2d-single-external-exit-supervisor.py'
    name = 'fd2d-trial-cache-external-exit-supervisor.py'
    text = old.read_text().replace('fd2d-run-prefix-single.py', 'fd2d-run-prefix-trial-cache.py')
    data = text.encode()
    for target in (repository/name, args.runtime_root/'control'/name):
        save(target, data)
    records.append({'source': str(old), 'file': str(args.runtime_root/'control'/name),
                    'repository_file': str(repository/name), 'bytes': len(data),
                    'sha256': hashlib.sha256(data).hexdigest()})
    report = {'scope': 'Prepared complete-UNACCEPTED-trial cache; actual launch and residual still required',
              'unchanged': 'One-worker original stage pool, exact stage cache, original geometric construction, original F and acceptance',
              'trial_cache_identity': 'Exact original complete states, delta, lambda, fixed-node profiles, parameters, sources, architecture and V8',
              'closure_policy': 'Release original prepared retraction closures after each actual complete construction; an uncached backtrack recomputes the original helper',
              'sources': records}
    save(args.out, (json.dumps(report, indent=2)+'\n').encode())
    print(json.dumps({'out': str(args.out), 'source_count': len(records)}))


if __name__ == '__main__':
    main()

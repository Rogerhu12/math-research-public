#!/usr/bin/env python3
"""Assemble an explicit closed incremental payload without moving source Git."""
import argparse
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

TOPIC = Path('topics/visible-flexible-closed-surface')
WORKFLOW = '.github/workflows/visible-flex-fd2d-publish-checkpoint.yml'
REQUEST = TOPIC / 'notes/2026-11-12-fd2d-ci-publication-request.json'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--snapshot', type=Path, required=True)
    args = parser.parse_args()
    repo = Path.cwd().resolve()
    plan = json.loads(args.plan.read_text())
    base = plan['base_commit']
    if not re.fullmatch(r'[0-9a-f]{40}', base):
        raise ValueError('Exact common main base required')
    label = plan['label']
    if not re.fullmatch(r'[a-z0-9-]+', label):
        raise ValueError('Invalid batch label')
    manifest = TOPIC / ('notes/2026-11-12-fd2d-live-recovery-' + label + '-batch-manifest.json')
    paths, checked = set(), set()

    def relative(value):
        path = Path(value)
        if path.is_absolute():
            path = path.relative_to(repo)
        elif not str(path).startswith(('topics/', '.github/')):
            path = TOPIC / path
        if '..' in path.parts or not (str(path).startswith(str(TOPIC) + '/') or str(path) == WORKFLOW):
            raise ValueError('Path outside explicit session ownership')
        return path

    def collect(group):
        group = relative(group)
        if str(group) in checked:
            return
        data = json.loads(group.read_text())
        checked.add(str(group))
        paths.add(str(group))
        for item in data['files']:
            path = relative(item['path'])
            body = path.read_bytes()
            if len(body) != item['bytes'] or hashlib.sha256(body).hexdigest() != item['sha256']:
                raise ValueError('Closed identity changed: ' + str(path))
            paths.add(str(path))
        for dependency in data.get('dependencies_closed_manifests', []):
            collect(dependency)

    for group in plan['closed_groups']:
        collect(group)
    for value in plan.get('extra_files', []):
        paths.add(str(relative(value)))
    for rel in ['HANDOFF.md', 'results.md', 'open.md', 'log.md',
                'scripts/fd2d_ci_publish_checkpoint.py',
                'scripts/fd2d_publish_tree_overlay_checkpoint.py',
                'scripts/fd2d_publish_tree_overlay_checkpoint_only.py',
                'scripts/fd2d_publish_rebase_checkpoint.py',
                'scripts/fd2d_build_closed_publication_batch.py']:
        paths.add(str(TOPIC / rel))
    paths.update([WORKFLOW, str(REQUEST), str(manifest), str(relative(args.plan))])
    now = datetime.datetime.now(datetime.timezone.utc)
    REQUEST.write_text(json.dumps(dict(schema='fd2d-explicit-ci-git-publication-v2',
        base_commit=base, message=plan['message'],
        publication_policy='No root LOG writes; rejected main pushes immediately pull --rebase, then inspect both README differences',
        owned_paths=sorted(paths)), ensure_ascii=False, indent=2) + '\n')
    files = []
    for name in sorted(paths - {str(manifest)}):
        body = Path(name).read_bytes()
        if len(body) >= 5_000_000 or (name.endswith('.md') and len(body) >= 100_000):
            raise ValueError('File exceeds repository size limit: ' + name)
        if len(body) > 1_000_000 and not name.endswith('.gz'):
            raise ValueError('Large data must be compressed: ' + name)
        if not name.endswith('HANDOFF.md'):
            files.append(dict(path=name, bytes=len(body), sha256=hashlib.sha256(body).hexdigest()))
    handoff = (TOPIC / 'HANDOFF.md').read_text()
    if len(handoff.encode()) >= 10_000:
        raise ValueError('HANDOFF exceeds repository limit')
    manifest.write_text(json.dumps(dict(schema='fd2d-closed-publication-batch-v1',
        utc=now.isoformat(), base_commit=base, closed_group_manifests=sorted(checked),
        files=files, excluded=plan.get('excluded', []) + ['HANDOFF hash refreshed after every literal pull'],
        scope=plan['scope']), ensure_ascii=False, indent=2) + '\n')
    ordered = sorted(paths)
    hashes = subprocess.check_output(['git', 'hash-object', '-w', '--stdin-paths'],
        input='\n'.join(ordered) + '\n', text=True).splitlines()
    if len(hashes) != len(ordered):
        raise RuntimeError('Incomplete Git object materialization')
    snapshot = dict(message=plan['message'],
        entries=[['100644', sha, path] for sha, path in zip(hashes, ordered)],
        handoff=handoff, base_commit=base)
    args.snapshot.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(snapshot=str(args.snapshot), manifest=str(manifest), groups=len(checked),
        files=len(ordered), bytes=sum(Path(path).stat().st_size for path in paths))))


if __name__ == '__main__':
    main()

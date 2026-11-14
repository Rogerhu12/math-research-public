#!/usr/bin/env python3
"""Collect closed artifacts; preserve historical manifests and live source files."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

repo = Path.cwd().resolve()
topic = Path('topics/visible-flexible-closed-surface')
notes = topic / 'notes'
prefix = '2026-11-12-fd2d-'
prior = json.loads((notes / (prefix + 'live-recovery-sixth-batch-manifest.json')).read_text())
groups = list(prior['closed_group_manifests'])
groups += [str(notes / (prefix + name)) for name in [
    'normal-ball-closed-inputs-manifest-02.json',
    'geometry-R151-closed-manifest.json',
    'metric-hybrid-lifting-closed-manifest-01.json',
    'positive-n-Gauss-proof-closed-manifest.json',
    'geometry-R154-closed-manifest.json',
    'raw-bump-atlas13-closed-group.json',
    'positive-gauss-warm01-closed-group.json',
    'raw-bump-gauss14-closed-group.json',
    'metric-positive-gauss-native-closed-manifest-01.json',
]]
paths = set()
checked = set()


def relative(path):
    path = Path(path)
    if path.is_absolute():
        return path.relative_to(repo)
    return path if str(path).startswith('topics/') else topic / path


def collect(group):
    path = relative(group)
    if str(path) in checked:
        return
    checked.add(str(path))
    data = json.loads(path.read_text())
    paths.add(str(path))
    for item in data['files']:
        child = relative(item['path'])
        body = child.read_bytes()
        assert len(body) == item['bytes'], child
        assert hashlib.sha256(body).hexdigest() == item['sha256'], child
        paths.add(str(child))
    for dependency in data.get('dependencies_closed_manifests', []):
        collect(dependency)


for group in groups:
    collect(group)
for rel in ['HANDOFF.md', 'open.md', 'log.md', 'results.md',
            'scripts/fd2d_ci_publish_checkpoint.py',
            'scripts/fd2d_publish_tree_overlay_checkpoint_only.py',
            'scripts/fd2d_build_seventh_publication_batch.py',
            'notes/' + prefix + 'publication-operations-v2.json',
            'notes/' + prefix + 'live-recovery-fifth-batch-manifest.json',
            'notes/' + prefix + 'live-recovery-sixth-batch-manifest.json']:
    paths.add(str(topic / rel))
paths.add('.github/workflows/visible-flex-fd2d-publish-checkpoint.yml')
request = notes / (prefix + 'ci-publication-request.json')
manifest = notes / (prefix + 'live-recovery-seventh-batch-manifest.json')
paths.update([str(request), str(manifest)])
base = '929f7c8ed289b673a83d5a90d72d245059dda3ac'
now = datetime.datetime.now(datetime.timezone.utc)
message = 'Preserve complete coast and cap certificates, Gauss branch progress, and ordinary Git publication'
log = (f'{now:%Y-%m-%d %H:%M} UTC — Astra-visible-flex-fd2d：合存R143–154及13/14真实主态；'
       '完整coast/帽交叉已付，强核继续。新增本题专用CI工作流，以终端普通Git修复main持续并发推送竞争。\n')
assert len(log) <= 200
request.write_text(json.dumps(dict(schema='fd2d-explicit-ci-git-publication-v1',
    base_commit=base, message=message, root_log_entry=log,
    owned_paths=sorted(paths)), ensure_ascii=False, indent=2) + '\n')
files = []
for name in sorted(paths - {str(manifest)}):
    body = Path(name).read_bytes()
    assert len(body) < 5_000_000, name
    if name.endswith('.md'):
        assert len(body) < 100_000, name
    if len(body) > 1_000_000:
        assert name.endswith('.gz'), name
    if not name.endswith('HANDOFF.md'):
        files.append(dict(path=name, bytes=len(body), sha256=hashlib.sha256(body).hexdigest()))
handoff = (topic / 'HANDOFF.md').read_text()
assert len(handoff.encode()) < 10_000
manifest.write_text(json.dumps(dict(schema='fd2d-closed-publication-batch-v1',
    utc=now.isoformat(), base_commit=base,
    incorporates_checkpoint6='f6f380277536a5b6dd94413489f52959bb171272',
    closed_group_manifests=sorted(checked), files=files,
    excluded=['active post14 numerical and sign diagnostics',
              'active R155 proof', 'regenerable intermediate state arrays',
              'HANDOFF hash refreshed after every literal pull'],
    scope='Complete R143–154 closed groups and real numerical outcomes; strong complete surface remains open'),
    ensure_ascii=False, indent=2) + '\n')
ordered = sorted(paths)
hashes = subprocess.check_output(['git', 'hash-object', '-w', '--stdin-paths'],
    input='\n'.join(ordered) + '\n', text=True).splitlines()
assert len(hashes) == len(ordered)
snapshot = dict(message=message, entries=[['100644', sha, path] for sha, path in zip(hashes, ordered)],
    handoff=handoff, base_commit=base, root_log_entry=log)
output = Path('/tmp/fd2d-seventh-batch-object-snapshot.json')
output.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(snapshot=str(output), groups=len(checked), files=len(ordered),
    bytes=sum(Path(path).stat().st_size for path in paths), handoff_bytes=len(handoff.encode()))))

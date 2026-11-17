#!/usr/bin/env python3
"""Restore the complete immutable tail/prefix source closure into scratch.

The default coupling manifest includes required .cjs factories missing from
the historical 39-file stage1 subset. This does not restore numerical states.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--repo', type=Path, required=True)
p.add_argument('--dest', type=Path, required=True)
p.add_argument('--manifest', type=Path,
               default=Path(__file__).parent.parent/'coupling/coupling_recovery_manifest.json')
a = p.parse_args()
repo, dest = a.repo.resolve(), a.dest.resolve()
if dest == repo or repo in dest.parents:
    raise ValueError('Recovered sources and generated data belong outside the repository')
rows = json.loads(a.manifest.read_text())['files']
for row in rows:
    target = dest / row['target']
    payload = (target.read_bytes() if target.exists() else
               subprocess.check_output(['git', '-C', str(repo), 'show',
                                        row['revision']+':'+row['path']]))
    if len(payload) != row['bytes'] or hashlib.sha256(payload).hexdigest() != row['sha256']:
        raise ValueError('Immutable source checksum mismatch: '+row['path'])
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
print(json.dumps(dict(recovered=len(rows), destination=str(dest),
                      manifest_sha256=hashlib.sha256(a.manifest.read_bytes()).hexdigest())))

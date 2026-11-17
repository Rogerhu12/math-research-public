"""Restore only the five immutable source dependencies named by the manifest."""
import argparse, hashlib, json, subprocess
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--repo', type=Path, required=True)
p.add_argument('--scratch', type=Path, required=True)
p.add_argument('--manifest', type=Path, default=Path(__file__).with_name('mixed_source_manifest.json'))
a = p.parse_args()
manifest = json.loads(a.manifest.read_text())
a.scratch.mkdir(parents=True, exist_ok=True)
rows = []
for dep in manifest['immutable_dependencies']:
    payload = subprocess.check_output(['git', '-C', str(a.repo), 'show', dep['revision']+':'+dep['path']])
    digest = hashlib.sha256(payload).hexdigest()
    if digest != dep['sha256']:
        raise ValueError('Archived source hash mismatch: '+dep['path'])
    target = a.scratch/dep['target']
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_bytes() != payload:
        raise FileExistsError('Refusing to replace a different local source: '+str(target))
    target.write_bytes(payload)
    rows.append(dict(path=str(target), sha256=digest, bytes=len(payload)))
print(json.dumps(dict(scope=__doc__, files=rows), indent=2))

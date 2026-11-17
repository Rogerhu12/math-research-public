#!/usr/bin/env python3
"""Export the existing m3 checkpoint as an exact finite C2 tail definition.

No BVP/Newton solve is run. The original exporter is copied byte-for-byte,
then its conditional background-curvature metadata is changed explicitly.
All generated arrays stay in the selected scratch output directory.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--source-topic', type=Path, required=True)
p.add_argument('--checkpoint', type=Path, required=True)
p.add_argument('--outdir', type=Path, required=True)
p.add_argument('--steps', type=int, default=32)
p.add_argument('--angular', type=int, default=256)
p.add_argument('--degree', type=int, default=96)
p.add_argument('--audit-angular', type=int, default=128)
p.add_argument('--background-curvature', type=float, default=8.001)
a = p.parse_args()
source = a.source_topic.resolve()
out = a.outdir.resolve()
out.mkdir(parents=True, exist_ok=False)
runtime = out / 'runtime'
(runtime / 'scripts').mkdir(parents=True)
(runtime / 'notes').mkdir()
sha = lambda q: hashlib.sha256(q.read_bytes()).hexdigest()
names = ['closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs',
         'closing_tail_sources.mjs', '950f-tail-subdivision.mjs']
for name in names:
    shutil.copyfile(source / 'scripts' / name, runtime / 'scripts' / name)
shutil.copyfile(source / 'notes/closing_tail_dependency_blobs.json',
                runtime / 'notes/closing_tail_dependency_blobs.json')
original = source / 'scripts/db6f-tail-increment-export-v2.mjs'
original_text = original.read_text()
needle = 'assumedBackgroundCurvature:6.001'
assert original_text.count(needle) == 1
replacement = 'assumedBackgroundCurvature:' + repr(a.background_curvature)
script = runtime / 'scripts/db6f-tail-increment-export-v2-B8.mjs'
script.write_text(original_text.replace(needle, replacement))
cmd = ['node', str(script), str(a.checkpoint.resolve()), str(out / 'tail'),
       '--source-root', str(source / 'repro/source-root'), '--depth', '8',
       '--steps', str(a.steps), '--angular-nodes', str(a.angular),
       '--degree', str(a.degree), '--difference-step', '.00005',
       '--audit-angular-nodes', str(a.audit_angular),
       '--audit-fractions', '0.25,0.5,0.75']
record = dict(scope=__doc__, command=cmd,
              checkpoint=str(a.checkpoint.resolve()),
              checkpoint_sha256=sha(a.checkpoint),
              original_exporter_sha256=sha(original),
              executed_exporter_sha256=sha(script),
              transformation=dict(old=needle, new=replacement, count=1),
              source_files={name: sha(source / 'scripts' / name)
                            for name in names},
              mathematical_background_bound_is_a_separate_obligation=True,
              bvp_solves_executed=0)
(out / 'execution_record.json').write_text(json.dumps(record, indent=2) + '\n')
with (out / 'export.log').open('w') as log:
    result = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT)
record['exit_code'] = result.returncode
record['finished'] = result.returncode == 0
for name in ['tail-manifest.json', 'tail-collar.json']:
    q = out / name
    if q.exists():
        record[name + '_sha256'] = sha(q)
(out / 'execution_record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({k: v for k, v in record.items()
                  if k in ['finished', 'exit_code', 'checkpoint_sha256',
                           'tail-manifest.json_sha256', 'tail-collar.json_sha256']}))
sys.exit(result.returncode)

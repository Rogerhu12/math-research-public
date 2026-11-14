#!/usr/bin/env python3
"""Resolve one fixed tail Dirichlet problem at a new radial integration grid.

The source geometry and full cut-height vector are copied unchanged. This
does not recouple a prefix, certify an infinite tail, or prove existence.
Large response arrays stay in local compressed files.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('checkpoint')
ap.add_argument('config')
ap.add_argument('out_prefix')
ap.add_argument('--source-root', required=True)
ap.add_argument('--steps', type=int, required=True)
ap.add_argument('--tolerance', type=float, default=2e-10)
args = ap.parse_args()
source = Path(args.checkpoint).resolve()
record = json.load(gzip.open(source, 'rt') if source.suffix == '.gz' else source.open())
r = record.get('response', record)
cp = r.get('checkpoint', r.get('tail_checkpoint', r.get('seam', {}).get('tail_checkpoint', r)))
cfg = json.loads(Path(args.config).read_text())
out = Path(args.out_prefix).resolve()
out.parent.mkdir(parents=True, exist_ok=True)
output = Path(str(out) + '.json.gz')
if output.exists():
    raise FileExistsError(output)
cfg.update(initialCheckpoint=str(source), steps=args.steps, auditSteps=args.steps,
           solveTolerance=args.tolerance, maxIterations=24,
           traceFile=str(out) + '-trace.jsonl')
cfg_file = Path(str(out) + '-config.json')
cfg_file.write_text(json.dumps(cfg, indent=2) + '\n')
worker = Path(__file__).with_name('950f-tail-stage-port-v3.mjs')
env = os.environ.copy()
env['VISIBLE_FLEX_SOURCE_ROOT'] = str(Path(args.source_root).resolve())
env['CLOSING_TAIL_CACHE'] = str(Path(args.source_root).resolve() / 'topics/large-amplitude-twist-flex/scripts')
request = {'height': cp['cutHeight'], 'jacobian': False, 'audit': True}
raw_file = Path(str(out) + '-worker.jsonl')
err_file = Path(str(out) + '-worker.log')
with raw_file.open('w') as stdout, err_file.open('w') as stderr:
    proc = subprocess.Popen(['node', str(worker), str(cfg_file)], stdin=subprocess.PIPE,
                            stdout=stdout, stderr=stderr, env=env, text=True)
    proc.communicate(json.dumps(request) + '\n' + json.dumps({'stop': True}) + '\n')
if proc.returncode:
    raise RuntimeError('worker failed; inspect ' + str(err_file))
rows = [json.loads(s) for s in raw_file.read_text().splitlines() if s.strip()]
responses = [x for x in rows if 'checkpoint' in x]
if len(responses) != 1:
    raise RuntimeError('expected one response')
response = responses[0]
result = {'scope': __doc__, 'input': str(source),
          'inputSHA256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'config': cfg, 'request': request, 'response': response}
with gzip.open(output, 'wt', compresslevel=9) as f:
    json.dump(result, f, separators=(',', ':'))
if output.stat().st_size >= 5_000_000:
    raise RuntimeError('compressed response exceeds repository file limit')
raw_file.unlink()
summary = {'output': str(output), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
           'steps': args.steps, 'converged': response.get('converged'),
           'residual': response.get('residual'), 'audit': response.get('audit'),
           'failed': response.get('failed')}
Path(str(out) + '-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary))

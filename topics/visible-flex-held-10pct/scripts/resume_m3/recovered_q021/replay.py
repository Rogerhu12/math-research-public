#!/usr/bin/env python3
"""Regenerate the second genuine m3 amplitude from the accepted radial2 pair.

The original source recovery and sparse-v2 stage transformation are supplied
by the previously published packages. This script stores no DN or field data.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

p = argparse.ArgumentParser()
p.add_argument('--source-topic', type=Path, required=True)
p.add_argument('--short-bridge', type=Path, required=True)
p.add_argument('--sparse-helper', type=Path, required=True)
p.add_argument('--chart', type=Path, required=True)
p.add_argument('--prefix-restart', type=Path, required=True)
p.add_argument('--tail-restart', type=Path, required=True)
p.add_argument('--outdir', type=Path, required=True)
a = p.parse_args()
here = Path(__file__).resolve().parent
sha = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
if sha(a.prefix_restart) != '7bab356153195aed714bcdd68c893755891bda8235c88cbc4cf065354ee30a6f':
    raise ValueError('Replay requires the recorded accepted radial2 prefix')
if sha(a.tail_restart) != '7d29ca238ddcd623659ccdae7814432a615ef85a89faae82970c93402add0c06':
    raise ValueError('Replay requires the recorded accepted radial2 tail')
if sha(a.sparse_helper) != 'a52567b2bfaded2fa9271a08f3cd969dc0291261f22cf2847c83234d93462fa5':
    raise ValueError('Sparse-v2 helper differs')
core = a.source_topic / 'scripts/950f-tail-stage-core.mjs'
if sha(core) != 'fdf5943ea9655f98cacd2c749d0155cfad08111c88915ce31b2c832bea68d68e':
    raise ValueError('Recovered source is not the recorded sparse-v2 stage engine')
out = a.outdir.resolve()
out.mkdir(parents=True, exist_ok=True)
env = dict(os.environ)
env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
           VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(a.sparse_helper.resolve()),
           VISIBLE_FLEX_SPARSE_TRACE=str(out / 'linear-trace.jsonl'))
cfg = json.loads((here / 'tail-settings.json').read_text())
prefix = cfg.pop('valleyControlsPrefix')
length = cfg.pop('valleyControlsLength')
cfg['valleyControls'] = prefix + [0] * (length - len(prefix))
startup = out / 'startup-config.json'
startup.write_text(json.dumps(cfg, indent=2) + '\n')
rawport = out / 'worker-port8.json'
subprocess.run([sys.executable, str(here / 'export_original_worker_port.py'),
                '--source-topic', str(a.source_topic.resolve()),
                '--config', str(startup), '--out', str(rawport)], check=True, env=env)
port = json.loads(rawport.read_text())
profile = json.loads((here / 'baseline-profile.json').read_text())
port['cut']['_prefix_bridge'] = profile['prefix_bridge']
portfile = out / 'port8.json'
portfile.write_text(json.dumps(port, indent=2) + '\n')
cfg['initialCheckpoint'] = str(a.tail_restart.resolve())
cfg['traceFile'] = str(out / 'worker-trace.jsonl')
config = out / 'config.json'
config.write_text(json.dumps(cfg, indent=2) + '\n')
command = [sys.executable, str(here / 'couple_m3_smallcut.py'),
           '--source-topic', str(a.source_topic.resolve()),
           '--short-bridge', str(a.short_bridge.resolve()),
           '--profile', str(here / 'baseline-profile.json'),
           '--chart', str(a.chart.resolve()), '--linear-port', str(portfile),
           '--tail-config', str(config), '--out-prefix', str(out / 'seed'),
           '--restart', str(a.prefix_restart.resolve()), '--amplitude', '.021',
           '--warp-reference', '.021', '--modes', '8', '--angular', '256',
           '--audit-angular', '512', '--nodes', '601', '--max-nodes', '4000',
           '--tol', '1e-6', '--bc-tol', '1e-7', '--physical-bc-tol', '2e-9',
           '--node-heap', '2304', '--warmup-scales', '1', '--lagged-tail']
(out / 'replay-command.json').write_text(json.dumps(command, indent=2) + '\n')
subprocess.run(command, check=True, env=env)

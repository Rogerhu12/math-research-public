#!/usr/bin/env python3
"""Continue two accepted actual m3 coupled states without changing solve gates.

This is a design-amplitude continuation. The prefix delta is solved again.
Only the initial guess changes; no same-metric convergence is claimed.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--short-bridge', type=Path, required=True)
    p.add_argument('--sparse-helper', type=Path, required=True)
    p.add_argument('--chart', type=Path, required=True)
    p.add_argument('--linear-port', type=Path, required=True)
    p.add_argument('--low-prefix', type=Path, required=True)
    p.add_argument('--high-prefix', type=Path, required=True)
    p.add_argument('--high-tail', type=Path, required=True)
    p.add_argument('--amplitude', type=float, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    p.add_argument('--nodes', type=int, default=801)
    p.add_argument('--max-nodes', type=int, default=6000)
    a = p.parse_args()
    out = a.outdir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    hi = json.load(gzip.open(a.high_prefix, 'rt'))
    cfg = dict(hi['tail_config'])
    cfg['initialCheckpoint'] = str(a.high_tail.resolve())
    cfg['traceFile'] = str(out / 'worker-trace.jsonl')
    config = out / 'config.json'
    profile = out / 'profile.json'
    config.write_text(json.dumps(cfg, indent=2) + '\n')
    profile.write_text(json.dumps(hi['frozen_profile'], indent=2) + '\n')
    mode = int(hi['config']['modes'])
    angular = int(hi['config']['angular'])
    command = [sys.executable, str(Path(__file__).with_name('couple_m3_smallcut_secant.py')),
               '--source-topic', str(a.source_topic.resolve()), '--short-bridge', str(a.short_bridge.resolve()),
               '--secant-low', str(a.low_prefix.resolve()), '--profile', str(profile),
               '--chart', str(a.chart.resolve()), '--linear-port', str(a.linear_port.resolve()),
               '--tail-config', str(config), '--out-prefix', str(out / 'seed'),
               '--restart', str(a.high_prefix.resolve()), '--amplitude', str(a.amplitude),
               '--warp-reference', str(a.amplitude), '--modes', str(mode),
               '--angular', str(angular), '--audit-angular', str(2 * angular),
               '--nodes', str(a.nodes), '--max-nodes', str(a.max_nodes),
               '--tol', str(hi['config']['tol']), '--bc-tol', str(hi['config']['bc_tol']),
               '--physical-bc-tol', str(hi['config']['physical_bc_tol']),
               '--node-heap', '2304', '--warmup-scales', '1', '--lagged-tail']
    env = dict(os.environ)
    env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
               VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(a.sparse_helper.resolve()),
               VISIBLE_FLEX_SPARSE_TRACE=str(out / 'linear-trace.jsonl'))
    record = dict(scope=__doc__, command=command,
                  inputs={str(f.resolve()): hashlib.sha256(f.read_bytes()).hexdigest()
                          for f in [a.low_prefix, a.high_prefix, a.high_tail, a.linear_port,
                                    a.chart, a.short_bridge, a.sparse_helper]},
                  tail_acceptance=cfg['solveTolerance'],
                  same_metric_refinement=False)
    (out / 'continuation-command.json').write_text(json.dumps(record, indent=2) + '\n')
    result = subprocess.run(command, env=env)
    record['returncode'] = result.returncode
    (out / 'continuation-command.json').write_text(json.dumps(record, indent=2) + '\n')
    raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()

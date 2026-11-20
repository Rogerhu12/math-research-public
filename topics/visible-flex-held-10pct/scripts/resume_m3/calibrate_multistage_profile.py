#!/usr/bin/env python3
"""Archive the executed mode3 BackwardLine calibration for the new profile.

The original bridge is unchanged. This is a floating linear seed calibration,
not a nonlinear isometry or a rigorous existence interval.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[4])
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--short-bridge', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--profile-out', type=Path, required=True)
    a = p.parse_args()
    T = a.repo.resolve()/'topics/visible-flex-held-10pct/scripts/resume_m3'
    profile = T/'multistage_profile_reference.json'; cfg = json.loads(profile.read_text())
    portp = a.inputs/'q060-port.json'; port = json.loads(portp.read_text())
    port['cut']['_prefix_bridge'] = cfg['prefix_bridge']
    chartp = a.inputs/'reference/chart.json'; chart = json.loads(chartp.read_text())
    spec = importlib.util.spec_from_file_location('newg_linear_root_model', T/'actual_m3_metric_model.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    record = dict(command=['python', 'newg_linear_probe', '--source-topic', str(a.source_topic),
        '--short-bridge', str(a.short_bridge), '--profile', str(profile), '--chart', str(chartp),
        '--port', str(portp)], physical_profile=cfg, angular_chart=chart,
        physical_tail_parameters=port['parameters'], physical_tail_cut=port['cut'],
        modes=8, angular=256, gauge_q=.06, warp_reference=.06,
        gates=dict(physical_bc_tol=2e-9, bc_tol=1e-7))
    o = m.load_model(record)
    report = dict(scope=__doc__, rows=[], source_topic=str(a.source_topic),
        profile_sha256=hashlib.sha256(profile.read_bytes()).hexdigest(), complete_surface=False)
    cache = {}

    def scalar(delta):
        if delta in cache:
            return cache[delta]['core_slope_ratio']
        f = o.flow(delta-.06); line = f.backward_line(); core = np.asarray(line.core, float)
        row = dict(delta=delta, ratio=delta/.06, mode=3, normalized_core=core.tolist(),
            core_slope_ratio=float(core[1]/core[0]), prefix_length=f.prefix_end, total_length=f.end)
        cache[delta] = row; report['rows'].append(row)
        a.out.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(row), flush=True)
        return row['core_slope_ratio']

    for delta in [.06, .0615, .063, .0645, .066]:
        scalar(delta)
    root = brentq(scalar, .063, .066, xtol=2e-12, rtol=1e-13)
    report.update(linear_root=cache[root], status='new_metric_mode3_linear_root_located',
        root_method='brentq(.063,.066), xtol2e-12, rtol1e-13; original BackwardLine integration',
        bridge_unchanged=True, new_nonlinear_candidate=False)
    a.out.write_text(json.dumps(report, indent=2)+'\n')
    a.profile_out.write_text(json.dumps({**cfg, 'delta':root}, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], root=report['linear_root'])))


if __name__ == '__main__':
    main()

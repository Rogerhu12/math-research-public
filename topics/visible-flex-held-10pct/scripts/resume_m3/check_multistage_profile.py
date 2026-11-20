#!/usr/bin/env python3
"""Archive of the executed new-profile checks, with configurable input paths.

This checks the same endpoint, scaling, chart and parameter identities used in
multistage-profile-check-v2.json. It performs no BVP or tail solve.
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


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[4])
    p.add_argument('--workdir', type=Path, required=True)
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--short-bridge', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    T = a.repo.resolve()/'topics/visible-flex-held-10pct/scripts/resume_m3'
    S = a.source_topic.resolve()
    cp = T/'multistage_profile_reference.json'
    cfg = json.loads(cp.read_text())
    port_path = a.inputs/'q060-port.json'
    port = json.loads(port_path.read_text())
    port['cut']['_prefix_bridge'] = cfg['prefix_bridge']
    chart_path = a.inputs/'reference/chart.json'
    chart = json.loads(chart_path.read_text())
    spec = importlib.util.spec_from_file_location('multistage_model_check', T/'actual_m3_metric_model.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    record = dict(command=['python', 'profile_check', '--source-topic', str(S),
        '--short-bridge', str(a.short_bridge), '--profile', str(cp), '--chart', str(chart_path),
        '--port', str(port_path)], physical_profile=cfg, angular_chart=chart,
        physical_tail_parameters=port['parameters'], physical_tail_cut=port['cut'],
        modes=8, angular=256, gauge_q=.06, warp_reference=.06,
        gates=dict(physical_bc_tol=2e-9, bc_tol=1e-7))
    o = m.load_model(record); f0 = o.flow(0.)
    s0 = np.linspace(0, f0.prefix_end, 3001)
    g0 = np.asarray(f0.prefix_profile(s0)); tb = o.inverse_chart(f0.breakpoints, 0.)
    rows = []
    for delta in (.06, .0615, .063):
        par = delta-.06; r = delta/.06; f = o.flow(par); knots = f.breakpoints
        internal = knots[(knots > 0) & (knots < f.prefix_end)]
        ends = np.asarray(f.profile([0, f.Tu, f.prefix_end])).T
        jump = np.max(abs(np.asarray(f.profile(np.nextafter(internal, -np.inf)))
                         -np.asarray(f.profile(np.nextafter(internal, np.inf)))), axis=1)
        expected = np.vstack((1+r*(g0[0]-1), g0[1], g0[2]/r))
        scale = np.max(abs(np.asarray(f.prefix_profile(r*s0))-expected), axis=1)
        mapped, _ = o.chart(tb, par)
        chart_error = max(float(abs(mapped-knots).max()), float(abs(o.inverse_chart(knots, par)-tb).max()))
        tf = np.r_[np.linspace(0, 1, 1001), o.chart_breaks]
        sf, df = o.chart(tf, par); inverse = float(abs(o.inverse_chart(sf, par)-tf).max())
        bridgejump = np.asarray(f.profile([f.prefix_end-1e-14, f.prefix_end+1e-14]))
        assert np.array_equal(ends, np.array([[1, 0, 0], [1+delta, 0, 0], [1, 0, 0]]))
        assert max(jump) < 2e-10 and max(scale) < 2e-10 and chart_error < 1e-12
        assert inverse < 1e-12 and df.min() > 0
        assert len(knots) == 18 and len(f.breaks) == 21 and np.diff(f.breaks).min() > 1e-6
        rows.append(dict(delta=delta, ratio=r, Tu=f.Tu, Td=f.Td, prefix_end=f.prefix_end,
            end=f.end, endpoint_jets=ends.tolist(), one_ulp_knot_jumps=jump.tolist(),
            scaling_errors=scale.tolist(), chart_break_error=chart_error,
            inverse_chart_error=inverse, chart_ds_min=float(df.min()),
            bridge_near_join_difference=float(abs(bridgejump[:, 1]-bridgejump[:, 0]).max()),
            prefix_knots=len(knots), all_breaks=len(f.breaks),
            min_break_separation=float(np.diff(f.breaks).min())))
    par = .0015; h = 2e-7; r = (.06+par)/.06
    t = np.linspace(.003, .997, 79)*o.chart_join
    s, _ = o.chart(t, par); aa, _, acc = o.flow(par).profile(s)
    sp, _ = o.chart(t, par+h); gp = np.asarray(o.flow(par+h).profile(sp))
    sm, _ = o.chart(t, par-h); gm = np.asarray(o.flow(par-h).profile(sm))
    truth = np.vstack(((aa-1)/(.06*r), np.zeros_like(aa), -acc/(.06*r)))
    errors = np.max(abs((gp-gm)/(2*h)-truth), axis=1)
    assert max(errors) < 2e-6
    out = dict(status='profile_interface_check_passed', scope=__doc__, source_topic=str(S),
        provider_sha256=hashlib.sha256((S/'scripts/held10_multistage_flat_profile.py').read_bytes()).hexdigest(),
        config_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(), rows=rows,
        parameter_derivative_errors=errors.tolist(), complete_surface=False)
    a.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()

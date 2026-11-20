#!/usr/bin/env python3
"""Regenerate a lost n4 field from the committed compact physical definition.

The 2026-11-18 M20 field is not distributed under the repository data policy.
This script reads its recorded physical profile and core parameters, constructs
a two-mode linear initial guess, and solves the original finite prefix BVP.
The boundary operator here is the original *linear* physical tail port.  No
old checkpoint, accepted nonlinear DN, or complete closed surface is claimed.
Use the regenerated field as an initializer for new nonlinear continuation.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def initial_two_mode_field(obj, par, nodes, eta):
    """Use physical linear solutions and the full current reference lift."""
    from fixed_metric_mode3_bvp import merge_profile_mesh
    obj.initial(par)
    flow = obj.flow(par[0])
    t = merge_profile_mesh(np.linspace(0, 1, nodes), obj.chart_breaks)
    s, _ = obj.chart(t, par[0])
    N = max(2048, 64 * obj.M)
    B = flow.basis(N)[0]
    weights = (1 + eta, -15 * eta / 63)
    line_values = []
    for j in range(2):
        line = flow.backward_line(j)
        fg = np.empty((2, len(s)))
        for k, (lo, hi, solution, scale) in enumerate(line.segments):
            mask = (s >= lo) & ((s < hi) if k + 1 < len(line.segments) else (s <= hi))
            if np.any(mask):
                fg[:, mask] = solution(s[mask]) * np.exp(scale - line.logscale) / line.core[0]
        line_values.append(fg)
    y = np.empty((obj.n, len(t)))
    amplitude_ratio = obj.support_amplitude / obj.q
    for first in range(0, len(s), 32):
        sl = slice(first, first + 32)
        g = flow.geo(s[sl], N)
        theta = g['theta']
        er = np.stack((np.cos(theta), np.sin(theta), np.zeros_like(theta)), axis=-1)
        et = np.stack((-np.sin(theta), np.cos(theta), np.zeros_like(theta)), axis=-1)
        shape = np.zeros_like(er)
        for j, (weight, fg) in enumerate(zip(weights, line_values)):
            mode = 4 * (j + 1)
            shape += amplitude_ratio * weight * fg[0, sl, None, None] * (
                np.cos(mode * theta)[:, :, None] * er - np.sin(mode * theta)[:, :, None] * et / mode)
            shape[:, :, 2] += amplitude_ratio * weight * fg[1, sl, None] * np.cos(mode * theta)
        ar = flow.profile(s[sl])[0]
        shape -= (g['pos'] - ar[:, None, None] * er) / obj.q
        y[:, sl] = flow.project(shape, B)
    ar = flow.profile(s)[0]
    u = np.clip((s - .5 * flow.prefix_end) / (.4 * flow.prefix_end), 0., 1.)
    taper = ar * (1 - u**3 * (10 - 15*u + 6*u*u))
    y += (obj.initial(par) - y[:, 0])[:, None] * taper[None, :]
    return t, y


def build_model(source, loader, record, port, modes, angular, homotopy=None):
    sys.path.insert(0, str(loader))
    sys.path[:0] = [str(source / 'notes'), str(source / 'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    from tight_moment_interval_bounds import install
    install()
    from bimodal_chart_loader import load
    from plateau_core import PlateauSupportCore as ReferenceCore
    from raw_fixed_core import make_core_class
    settings = dict(record['core_settings'])
    if homotopy is not None:
        settings['homotopy'] = homotopy
    eta = settings['bimodal_eta']
    ad = load(source, 4, eta)
    load_module('held10_n4_recovery_short_bridge', source.parent / 'visible-flex-larger-amplitude/computations/root_short_bridge.py').install()
    Core = make_core_class(ReferenceCore, record['raw_control_anchor_modes'])
    coremod = __import__('fixed_metric_mode3_core')
    coremod.PlanarSupportCore = lambda q, corrections=(), base_mode=4: Core(q, corrections, base_mode, arc_nodes=1024, **settings)
    backend = load_module('held10_n4_recovery_fourier_jac', source / 'scripts/78718-prefix-fourier-jacobian.py')
    backend.install(ad)
    Flow, BVP = ad.build_classes(dict(knots=[0., 1.], values=[1., 1.], final_derivative=0.))
    from exact_core_lift import install_core_lift
    BVP = install_core_lift(Flow, BVP)
    from analytic_adaptive_core_jac import install as install_jac
    install_jac(BVP)
    cfg = dict(record['fixed_physical_profile'])
    port['cut']['_prefix_bridge'] = cfg['prefix_bridge']
    q0 = record['final_prefix']['gauge_amplitude']
    obj = BVP(cfg, port, q0, modes, angular, True, q0)
    obj.pscale = np.full(modes - 1, q0)
    obj.bcweights = np.full(modes, .01)
    par = np.zeros(modes)
    old = np.array(record['final_prefix']['parameters'])
    par[:min(modes, len(old))] = old[:modes]
    obj.initial(par)
    return obj, ad, par, cfg, settings


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'loader', 'definition', 'port', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--modes', type=int, default=20)
    p.add_argument('--angular', type=int, default=1280)
    p.add_argument('--nodes', type=int, default=601)
    p.add_argument('--max-nodes', type=int, default=6000)
    p.add_argument('--tol', type=float, default=1e-8)
    p.add_argument('--homotopy', type=float)
    p.add_argument('--check-only', action='store_true')
    a = p.parse_args()
    source, loader = a.source_topic.resolve(), a.loader.resolve()
    a.out.parent.mkdir(parents=True, exist_ok=True)
    if a.out.with_suffix('.json.gz').exists() or a.out.with_suffix('.json').exists():
        raise FileExistsError('Use a fresh output prefix')
    record = json.loads(a.definition.read_text())
    port = json.loads(a.port.read_text())
    obj, ad, par, cfg, settings = build_model(source, loader, record, port, a.modes, a.angular, a.homotopy)
    x, y = initial_two_mode_field(obj, par, a.nodes, settings['bimodal_eta'])
    row = dict(scope=__doc__, command=sys.argv, script_sha256=digest(__file__),
               definition_sha256=digest(a.definition), port_sha256=digest(a.port),
               physical_profile=cfg, settings=settings, modes=a.modes,
               initial_parameters=par.tolist(), initial_nodes=len(x),
               initial_bc=float(abs(obj.bc(y[:,0], y[:,-1], par)).max()),
               original_field_available=False, old_nonlinear_tail_reused=False,
               status='seed_ready', success=False)
    summary = a.out.with_suffix('.json')
    def persist():
        tmp = summary.with_suffix('.json.tmp')
        tmp.write_text(json.dumps(row, indent=2) + '\n')
        tmp.replace(summary)
    persist()
    print(json.dumps({k:v for k,v in row.items() if k != 'initial_parameters'}), flush=True)
    if a.check_only:
        return
    from f6curve_domain_newton import install, STATS
    from trace_domain_newton import install as observe_newton
    from curve_stable_prefix_bvp import save_checkpoint
    install()
    observe_newton(a.out.with_name(a.out.name + '-newton.jsonl'))
    begin = time.monotonic()
    try:
        sol = solve_bvp(obj.fun, obj.bc, x, y, par, tol=a.tol, bc_tol=1e-8,
                        max_nodes=a.max_nodes, fun_jac=obj.fun_jac, bc_jac=obj.bc_jac, verbose=2)
        np.savez(a.out.with_name(a.out.name+'-raw.npz'), x=sol.x, y=sol.y, p=sol.p, c=sol.sol.c,
                 rms_residuals=sol.rms_residuals)
        row.update(status='inner_returned', success=bool(sol.success), message=sol.message,
                   nodes=len(sol.x), parameters=sol.p.tolist(),
                   max_rms=float(sol.rms_residuals.max()),
                   max_bc=float(abs(obj.bc(sol.y[:,0], sol.y[:,-1], sol.p)).max()),
                   domain_newton=dict(STATS), seconds=time.monotonic()-begin)
        persist()
        print(json.dumps(dict(event='inner_returned', **{k:row[k] for k in ('success','nodes','max_rms','max_bc','seconds')})), flush=True)
        obj.initial(sol.p)
        f = obj.flow(sol.p[0])
        physical = SimpleNamespace(x=obj.chart(sol.x, sol.p[0])[0], y=sol.y, p=sol.p)
        physical.sol = f.c2_interpolant(physical)
        saved = dict(config=dict(modes=a.modes, base_mode=4, core_kind='n4_fixed_raw_mean_circle', angular=a.angular),
                     fixed_metric=True, raw_control_anchor_modes=record['raw_control_anchor_modes'],
                     solver_success=bool(sol.success), angular_chart_eta=settings['bimodal_eta'],
                     profile=cfg, physical_profile=cfg, physical_port=port,
                     physical_port_sha256=digest(a.port), plateau_settings=settings,
                     gauge_amplitude=obj.q, parameters=sol.p.tolist(), central_correction_scales=obj.pscale.tolist(),
                     mesh=physical.x.tolist(), pp_coefficients=physical.sol.c, meridian_length=f.end,
                     core_summary=obj._core.summary(), recovery_definition_sha256=digest(a.definition))
        save_checkpoint(a.out.with_suffix('.json.gz'), saved)
        row.update(checkpoint_sha256=digest(a.out.with_suffix('.json.gz')),
                   actual_q=float(obj.support_amplitude), central_correction_scales=obj.pscale.tolist())
        if sol.success:
            row['summary'] = ad.audit(obj, physical, 512)
        row.update(status='completed', seconds=time.monotonic()-begin)
    except Exception as exc:
        row.update(status='exception', error=repr(exc), seconds=time.monotonic()-begin, domain_newton=dict(STATS))
        print(json.dumps(dict(event='exception', error=repr(exc))), flush=True)
        persist()
        raise
    persist()
    print(json.dumps(dict(event='terminal', status=row['status'], success=row['success'], seconds=row['seconds'],
                         metric=row.get('summary',{}).get('metric_l1'), actual_q=row.get('actual_q'))), flush=True)


if __name__ == '__main__':
    main()
